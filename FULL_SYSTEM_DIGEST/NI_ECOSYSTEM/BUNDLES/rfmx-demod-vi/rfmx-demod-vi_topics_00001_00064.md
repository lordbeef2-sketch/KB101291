# NI DOCUMENT BUNDLE: rfmx-demod-vi

<!--NI_BUNDLE_CHUNK bundle=rfmx-demod-vi start=1 end=64 -->
<!--NI_TOPIC bundle=rfmx-demod-vi path=rfmxdemodvi/ademod_pal.html language=enus -->
## TOPIC 00001: rfmxdemodvi/ademod_pal.html

- bundle_id: `rfmx-demod-vi`
- source_path: `rfmxdemodvi/ademod_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-vi/raw/resource/enus/rfmxdemodvi/ademod_pal.html
- document_id: `rfmx-demod-vi`
- page_type: `leaf`
- content_type: ``

ADemod

ADemod

Owning Palette:

Configuration

Use the VIs on your palette to configure analog demodulated measurements.

| Palette Object | Description |
| --- | --- |
| RFmxDemod ADemod Configure Modulation Type | Configures the modulation type for analog demodulation measurements. |
| RFmxDemod ADemod Configure RBW Filter | Configures the resolution bandwidth (RBW) filter for analog demodulation measurements. |
| RFmxDemod ADemod Configure Measurement Interval | Configures the measurement interval for analog demodulation measurements. |
| RFmxDemod ADemod Configure AM Carrier Suppressed | Configures the presence of the amplitude modulated (AM) carrier. |
| RFmxDemod ADemod Configure Carrier Correction | Configures the carrier correction in analog demodulation measurements. |
| RFmxDemod ADemod Configure FM DeEmphasis | Configures the FM de-emphasis filter for analog demodulation measurements. |
| RFmxDemod ADemod Configure Audio Filter | Configures the audio filter for analog demodulation measurements. |
| RFmxDemod ADemod Configure Averaging | Configures averaging for analog demodulation measurements. |

<!--NI_TOPIC bundle=rfmx-demod-vi path=rfmxdemodvi/advanced_pal.html language=enus -->
## TOPIC 00002: rfmxdemodvi/advanced_pal.html

- bundle_id: `rfmx-demod-vi`
- source_path: `rfmxdemodvi/advanced_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-vi/raw/resource/enus/rfmxdemodvi/advanced_pal.html
- document_id: `rfmx-demod-vi`
- page_type: `leaf`
- content_type: ``

Advanced

Advanced

Owning Palette:

RFmx Demod VIs

Use the VIs on this palette to use advanced features. You can use the RFmxDemod Property Node to configure additional properties.

| Palette Object | Description |
| --- | --- |
| RFmxDemod Abort Measurements | Stops acquisition as well as the measurements that are associated with the signal instance and that were previously initiated by the RFmxDemod Initiate VI or measurement read VIs. |
| RFmxDemod Analyze (IQ, 1 Wfm) | Performs the enabled measurements on the I/Q complex waveform that you specify in IQ parameter. Call this VI after you configure the signal and measurement properties. You can fetch measurement results using the Fetch VIs or result properties in the property node. Use this VI only if the Recommended Acquisition Type property value is IQ. |
| RFmxDemod Create Signal Configuration | Creates a new instance of a signal. |
| RFmxDemod Clone Signal Configuration | Creates a new instance of a signal by copying all the property values from an existing signal instance. |
| RFmxDemod Delete Signal Configuration | Deletes an instance of the signal that you specify in the Signal Name parameter. |
| RFmxDemod Clear Named Result | Clears an instance of the result that you specify in the Selector String parameter. |
| RFmxDemod Clear All Named Results | Clears all results for the signal that you specify in the Selector String parameter. |

<!--NI_TOPIC bundle=rfmx-demod-vi path=rfmxdemodvi/build_string_pal.html language=enus -->
## TOPIC 00003: rfmxdemodvi/build_string_pal.html

- bundle_id: `rfmx-demod-vi`
- source_path: `rfmxdemodvi/build_string_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-vi/raw/resource/enus/rfmxdemodvi/build_string_pal.html
- document_id: `rfmx-demod-vi`
- page_type: `leaf`
- content_type: ``

Build String

Build String

Owning Palette:

RFmx Demod VIs

Use the VIs on this palette to create strings for configurations and results that require a selector string.

| Palette Object | Description |
| --- | --- |
| RFmxDemod Build Signal String | Creates a selector string for use with Configuration or Fetch properties and VIs. |

<!--NI_TOPIC bundle=rfmx-demod-vi path=rfmxdemodvi/configuration_pal.html language=enus -->
## TOPIC 00004: rfmxdemodvi/configuration_pal.html

- bundle_id: `rfmx-demod-vi`
- source_path: `rfmxdemodvi/configuration_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-vi/raw/resource/enus/rfmxdemodvi/configuration_pal.html
- document_id: `rfmx-demod-vi`
- page_type: `leaf`
- content_type: ``

Configuration

Configuration

Owning Palette:

RFmx Demod VIs

Use the VIs on this palette to configure various parameters for RFmxDemod measurements.

| Palette Object | Description |
| --- | --- |
| RFmxDemod Configure RF | Configures the RF properties of the signal by specifying the selector string. |
| RFmxDemod Configure Frequency | Configures the expected carrier frequency of the RF signal that needs to be acquired. The signal analyzer tunes to this frequency. |
| RFmxDemod Configure Reference Level | Configures the reference level that represents the maximum expected power of an RF input signal. |
| RFmxDemod Auto Level | Examines the input signal to calculate the peak power level and sets it as the value of the Reference Level property. Use this VI to help calculate an approximate setting for the reference level. |
| RFmxDemod Configure External Attenuation | Configures the attenuation of a switch (or cable) connected to the RF IN connector of the signal analyzer. |
| RFmxDemod Configure Trigger | Configures the Reference Trigger to use to acquire the signal. |
| RFmxDemod Send Software Edge Trigger | Sends a trigger to the device when you use the RFmxDemod Configure Trigger VI to choose a software version of a trigger, and the device is waiting for the trigger to be sent. You can also use this VI to override a hardware trigger. |

| Subpalette | Description |
| --- | --- |
| ADemod | Use the VIs on your palette to configure analog demodulated measurements. |
| DDemod | Use the VIs on this palette to configure digital demodulated measurements. |

<!--NI_TOPIC bundle=rfmx-demod-vi path=rfmxdemodvi/ddemod_pal.html language=enus -->
## TOPIC 00005: rfmxdemodvi/ddemod_pal.html

- bundle_id: `rfmx-demod-vi`
- source_path: `rfmxdemodvi/ddemod_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-vi/raw/resource/enus/rfmxdemodvi/ddemod_pal.html
- document_id: `rfmx-demod-vi`
- page_type: `leaf`
- content_type: ``

DDemod

DDemod

Owning Palette:

Configuration

Use the VIs on this palette to configure digital demodulated measurements.

| Palette Object | Description |
| --- | --- |
| RFmxDemod DDemod Configure Modulation Type | Configures the modulation type of the signal to be analyzed. |
| RFmxDemod DDemod Configure M | Configures the M-ary number. |
| RFmxDemod DDemod Configure PSK Format | Configures the PSK format. |
| RFmxDemod DDemod Configure Symbol Rate | Configures the symbol rate for digital demodulation measurements. |
| RFmxDemod DDemod Configure FSK Deviation | Configures the expected FSK deviation. |
| RFmxDemod DDemod Configure Symbol Map | Configures the symbol map that you use during measurements. |
| RFmxDemod DDemod Configure Number of Symbols | Configures the number of symbols to be measured. |
| RFmxDemod DDemod Configure Samples Per Symbol | Configures the samples per symbol to be used to acquire the signal for the measurement. |
| RFmxDemod DDemod Configure Pulse Shaping Filter | Configures the pulse-shaping filter. |
| RFmxDemod DDemod Configure Pulse Shaping Filter Custom Coefficients | Configures the pulse-shaping filter coefficients. |
| RFmxDemod DDemod Configure Measurement Filter | Configures the measurement filter. |
| RFmxDemod DDemod Configure Measurement Filter Custom Coefficients | Configures the measurement filter custom coefficients. |
| RFmxDemod DDemod Configure Equalizer | Configures the equalizer. |
| RFmxDemod DDemod Configure Equalizer Initial Coefficients | Configures the equalizer coefficients. |
| RFmxDemod DDemod Configure EVM Normalization Reference | Configures the error vector magnitude (EVM) normalization reference. |
| RFmxDemod DDemod Configure Synchronization | Configures bit pattern synchronization. |
| RFmxDemod DDemod Configure Spectrum Inverted | Configures swapping of I and Q channels in the acquired waveform before demodulation. |
| RFmxDemod DDemod Configure Averaging | Configures averaging for digital demodulation measurements. |

<!--NI_TOPIC bundle=rfmx-demod-vi path=rfmxdemodvi/demod_pal.html language=enus -->
## TOPIC 00006: rfmxdemodvi/demod_pal.html

- bundle_id: `rfmx-demod-vi`
- source_path: `rfmxdemodvi/demod_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-vi/raw/resource/enus/rfmxdemodvi/demod_pal.html
- document_id: `rfmx-demod-vi`
- page_type: `leaf`
- content_type: ``

RFmx Demod VIs

RFmx Demod VIs

Use the VIs on this palette to perform demodulation measurements. You can use the [RFmxDemod Property Node](../rfmxdemodvi/rfmxdemod_property_node.html) to configure additional properties.

| Palette Object | Description |
| --- | --- |
| RFmxDemod Read | Configures hardware for acquisition, performs measurement on acquired data, and returns measurement results. |
| RFmxDemod Select Measurement | Specifies the measurements that you want to enable. To select a single measurement, use the Single Measurement instance. To select multiple measurements, use the Multiple Measurements instance. |
| RFmxDemod Initiate | Initiates all enabled measurements. Call this VI after configuring the signal and measurement. This VI asynchronously launches measurements in the background and immediately returns to the caller program. You can fetch measurement results using the Fetch VIs or result properties in the property node. To get the status of measurements, you can use the RFmxDemod Wait for Measurement Complete VI or the RFmxDemod Check Measurement Status VI. |
| RFmxDemod Property Node | Sets (writes), gets (reads), or resets (sets to default value) RFmxDemod properties. |
| RFmxDemod VI Tree | Displays all the VIs available in RFmxDemod for measurement configuration, control, and fetching results. The VIs are organized in the order they are supposed to be used in a program that you create. |

| Subpalette | Description |
| --- | --- |
| Configuration | Use the VIs on this palette to configure various parameters for RFmxDemod measurements. |
| Fetch | Use the VIs on this palette to fetch analog and digital demodulated measurements. |
| Utility | Use the VIs on this palette to configure utility VIs. |
| Advanced | Use the VIs on this palette to use advanced features. You can use the RFmxDemod Property Node to configure additional properties. |
| Build String | Use the VIs on this palette to create strings for configurations and results that require a selector string. |

<!--NI_TOPIC bundle=rfmx-demod-vi path=rfmxdemodvi/fetch_pal.html language=enus -->
## TOPIC 00007: rfmxdemodvi/fetch_pal.html

- bundle_id: `rfmx-demod-vi`
- source_path: `rfmxdemodvi/fetch_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-vi/raw/resource/enus/rfmxdemodvi/fetch_pal.html
- document_id: `rfmx-demod-vi`
- page_type: `leaf`
- content_type: ``

Fetch

Fetch

Owning Palette:

RFmx Demod VIs

Use the VIs on this palette to fetch analog and digital demodulated measurements.

| Palette Object | Description |
| --- | --- |
| RFmxDemod DDemod Fetch | Fetches the digital demodulation measurements. |
| RFmxDemod ADemod Fetch | Fetches the analog demodulation measurements. |

<!--NI_TOPIC bundle=rfmx-demod-vi path=rfmxdemodvi/rfmxdemod_abort_measurements.html language=enus -->
## TOPIC 00008: rfmxdemodvi/rfmxdemod_abort_measurements.html

- bundle_id: `rfmx-demod-vi`
- source_path: `rfmxdemodvi/rfmxdemod_abort_measurements.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-vi/raw/resource/enus/rfmxdemodvi/rfmxdemod_abort_measurements.html
- document_id: `rfmx-demod-vi`
- page_type: `leaf`
- content_type: ``

RFmxDemod Abort Measurements (VI)

RFmxDemod Abort Measurements (VI)

Owning Palette:

Advanced

Stops acquisition as well as the measurements that are associated with the signal instance and that were previously initiated by the [RFmxDemod Initiate](../rfmxdemodvi/rfmxdemod_initiate.html) VI or measurement read VIs.

[IMAGE alt='RFmxDemod Abort Measurements' src='rfmxdemod_abort_measurements.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxDemod Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-demod-vi path=rfmxdemodvi/rfmxdemod_ademod_configure_am_carrier_suppressed.html language=enus -->
## TOPIC 00009: rfmxdemodvi/rfmxdemod_ademod_configure_am_carrier_suppressed.html

- bundle_id: `rfmx-demod-vi`
- source_path: `rfmxdemodvi/rfmxdemod_ademod_configure_am_carrier_suppressed.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-vi/raw/resource/enus/rfmxdemodvi/rfmxdemod_ademod_configure_am_carrier_suppressed.html
- document_id: `rfmx-demod-vi`
- page_type: `leaf`
- content_type: ``

RFmxDemod ADemod Configure AM Carrier Suppressed (VI)

RFmxDemod ADemod Configure AM Carrier Suppressed (VI)

Owning Palette:

ADemod

Configures the presence of the amplitude modulated (AM) carrier.

[IMAGE alt='RFmxDemod ADemod Configure AM Carrier Suppressed' src='rfmxdemod_ademod_configure_am_carrier_suppressed.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | AM Carrier Suppressed specifies whether the carrier of the AM signal is absent. The default value is False. False (0) The carrier of the AM signal is present. True (1) The carrier of the AM signal is absent. |
| False (0) | The carrier of the AM signal is present. |
| True (1) | The carrier of the AM signal is absent. |
|  | Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxDemod Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-demod-vi path=rfmxdemodvi/rfmxdemod_ademod_configure_audio_filter.html language=enus -->
## TOPIC 00010: rfmxdemodvi/rfmxdemod_ademod_configure_audio_filter.html

- bundle_id: `rfmx-demod-vi`
- source_path: `rfmxdemodvi/rfmxdemod_ademod_configure_audio_filter.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-vi/raw/resource/enus/rfmxdemodvi/rfmxdemod_ademod_configure_audio_filter.html
- document_id: `rfmx-demod-vi`
- page_type: `leaf`
- content_type: ``

RFmxDemod ADemod Configure Audio Filter (VI)

RFmxDemod ADemod Configure Audio Filter (VI)

Owning Palette:

ADemod

Configures the audio filter for analog demodulation measurements.

[IMAGE alt='RFmxDemod ADemod Configure Audio Filter' src='rfmxdemod_ademod_configure_audio_filter.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Audio Filter Type specifies the audio filter to be applied on the analog demodulated signal. The default value is None. For more information about filter response refer to the Analog Demod topic page. None (0) Does not use any audio filter. Custom (1) Uses the filter specified by the Ademod Audio Filter Lower Cutoff property and the Ademod Audio Filter Upper Cutoff property. A - Weight (2) Uses an A-weighted filter. B - Weight (3) Uses a B-weighted filter. C - Weight (4) Uses a C-weighted filter. CCITT (5) Uses the filter specified by CCITT. ITU-R 468-4 (6) Uses the filter specified by ITU-R 468-4. |
| None (0) | Does not use any audio filter. |
| Custom (1) | Uses the filter specified by the Ademod Audio Filter Lower Cutoff property and the Ademod Audio Filter Upper Cutoff property. |
| A - Weight (2) | Uses an A-weighted filter. |
| B - Weight (3) | Uses a B-weighted filter. |
| C - Weight (4) | Uses a C-weighted filter. |
| CCITT (5) | Uses the filter specified by CCITT. |
| ITU-R 468-4 (6) | Uses the filter specified by ITU-R 468-4. |
|  | Audio Filter Lower Cutoff specifies the lower cutoff frequency, in Hz, of the custom audio filter. |
|  | Audio Filter Upper Cutoff specifies the upper cutoff frequency, in Hz, of the custom audio filter. |
|  | Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxDemod Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-demod-vi path=rfmxdemodvi/rfmxdemod_ademod_configure_averaging.html language=enus -->
## TOPIC 00011: rfmxdemodvi/rfmxdemod_ademod_configure_averaging.html

- bundle_id: `rfmx-demod-vi`
- source_path: `rfmxdemodvi/rfmxdemod_ademod_configure_averaging.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-vi/raw/resource/enus/rfmxdemodvi/rfmxdemod_ademod_configure_averaging.html
- document_id: `rfmx-demod-vi`
- page_type: `leaf`
- content_type: ``

RFmxDemod ADemod Configure Averaging (VI)

RFmxDemod ADemod Configure Averaging (VI)

Owning Palette:

ADemod

Configures averaging for analog demodulation measurements.

[IMAGE alt='RFmxDemod ADemod Configure Averaging' src='rfmxdemod_ademod_configure_averaging.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Averaging Enabled enables averaging for analog demodulation measurement. False (0) The measurement is performed on a single acquisition. True (1) The measurement uses the value of the Averaging Count parameter for the number of acquisitions over which the measurement is averaged. The traces are not averaged. |
| False (0) | The measurement is performed on a single acquisition. |
| True (1) | The measurement uses the value of the Averaging Count parameter for the number of acquisitions over which the measurement is averaged. The traces are not averaged. |
|  | Averaging Count specifies the number of acquisitions used for averaging when you set the Averaging Enabled parameter to True. |
|  | Averaging Type specifies the averaging type for the measurement. Linear (0) The averaged result is the mean value measured across multiple acquisitions. Max (1) The averaged result is the maximum value measured across multiple acquisitions. Min (2) The averaged result is the minimum value measured across multiple acquisitions. |
| Linear (0) | The averaged result is the mean value measured across multiple acquisitions. |
| Max (1) | The averaged result is the maximum value measured across multiple acquisitions. |
| Min (2) | The averaged result is the minimum value measured across multiple acquisitions. |
|  | Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxDemod Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-demod-vi path=rfmxdemodvi/rfmxdemod_ademod_configure_carrier_correction.html language=enus -->
## TOPIC 00012: rfmxdemodvi/rfmxdemod_ademod_configure_carrier_correction.html

- bundle_id: `rfmx-demod-vi`
- source_path: `rfmxdemodvi/rfmxdemod_ademod_configure_carrier_correction.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-vi/raw/resource/enus/rfmxdemodvi/rfmxdemod_ademod_configure_carrier_correction.html
- document_id: `rfmx-demod-vi`
- page_type: `leaf`
- content_type: ``

RFmxDemod ADemod Configure Carrier Correction (VI)

RFmxDemod ADemod Configure Carrier Correction (VI)

Owning Palette:

ADemod

Configures the carrier correction in analog demodulation measurements.

[IMAGE alt='RFmxDemod ADemod Configure Carrier Correction' src='rfmxdemod_ademod_configure_carrier_correction.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Carrier Frequency Correction Enabled specifies whether to correct the frequency error in the carrier when demodulating frequency-modulated or phase-modulated signals. The default value is True. False (0) Does not correct the carrier frequency error. True (1) Corrects the carrier frequency error. |
| False (0) | Does not correct the carrier frequency error. |
| True (1) | Corrects the carrier frequency error. |
|  | Carrier Phase Correction Enabled specifies whether to correct the phase error in the carrier when demodulating phase-modulated signals. The default value is True. False (0) Does not correct the carrier phase error. True (1) Corrects the carrier phase error. |
| False (0) | Does not correct the carrier phase error. |
| True (1) | Corrects the carrier phase error. |
|  | Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxDemod Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-demod-vi path=rfmxdemodvi/rfmxdemod_ademod_configure_fm_deemphasis.html language=enus -->
## TOPIC 00013: rfmxdemodvi/rfmxdemod_ademod_configure_fm_deemphasis.html

- bundle_id: `rfmx-demod-vi`
- source_path: `rfmxdemodvi/rfmxdemod_ademod_configure_fm_deemphasis.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-vi/raw/resource/enus/rfmxdemodvi/rfmxdemod_ademod_configure_fm_deemphasis.html
- document_id: `rfmx-demod-vi`
- page_type: `leaf`
- content_type: ``

RFmxDemod ADemod Configure FM DeEmphasis (VI)

RFmxDemod ADemod Configure FM DeEmphasis (VI)

Owning Palette:

ADemod

Configures the FM de-emphasis filter for analog demodulation measurements.

[IMAGE alt='RFmxDemod ADemod Configure FM DeEmphasis' src='rfmxdemod_ademod_configure_fm_deemphasis.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | FM DeEmphasis specifies the time constant, in seconds, of the de-emphasis filter, which compensates for the pre-emphasis filter in the FM transmitter. |
|  | Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxDemod Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-demod-vi path=rfmxdemodvi/rfmxdemod_ademod_configure_measurement_interval.html language=enus -->
## TOPIC 00014: rfmxdemodvi/rfmxdemod_ademod_configure_measurement_interval.html

- bundle_id: `rfmx-demod-vi`
- source_path: `rfmxdemodvi/rfmxdemod_ademod_configure_measurement_interval.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-vi/raw/resource/enus/rfmxdemodvi/rfmxdemod_ademod_configure_measurement_interval.html
- document_id: `rfmx-demod-vi`
- page_type: `leaf`
- content_type: ``

RFmxDemod ADemod Configure Measurement Interval (VI)

RFmxDemod ADemod Configure Measurement Interval (VI)

Owning Palette:

ADemod

Configures the measurement interval for analog demodulation measurements.

[IMAGE alt='RFmxDemod ADemod Configure Measurement Interval' src='rfmxdemod_ademod_configure_measurement_interval.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Measurement Interval specifies the signal acquisition time, in seconds, for the analog demodulation measurement. |
|  | Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxDemod Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-demod-vi path=rfmxdemodvi/rfmxdemod_ademod_configure_modulation_type.html language=enus -->
## TOPIC 00015: rfmxdemodvi/rfmxdemod_ademod_configure_modulation_type.html

- bundle_id: `rfmx-demod-vi`
- source_path: `rfmxdemodvi/rfmxdemod_ademod_configure_modulation_type.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-vi/raw/resource/enus/rfmxdemodvi/rfmxdemod_ademod_configure_modulation_type.html
- document_id: `rfmx-demod-vi`
- page_type: `leaf`
- content_type: ``

RFmxDemod ADemod Configure Modulation Type (VI)

RFmxDemod ADemod Configure Modulation Type (VI)

Owning Palette:

ADemod

Configures the modulation type for analog demodulation measurements.

[IMAGE alt='RFmxDemod ADemod Configure Modulation Type' src='rfmxdemod_ademod_configure_modulation_type.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Modulation Type specifies the analog modulation type of the signal that needs to be analyzed. The default value is AM. AM (0) The signal to be analyzed is amplitude modulated. FM (1) The signal to be analyzed is frequency modulated. PM (2) The signal to be analyzed is phase modulated. |
| AM (0) | The signal to be analyzed is amplitude modulated. |
| FM (1) | The signal to be analyzed is frequency modulated. |
| PM (2) | The signal to be analyzed is phase modulated. |
|  | Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxDemod Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-demod-vi path=rfmxdemodvi/rfmxdemod_ademod_configure_rbw_filter.html language=enus -->
## TOPIC 00016: rfmxdemodvi/rfmxdemod_ademod_configure_rbw_filter.html

- bundle_id: `rfmx-demod-vi`
- source_path: `rfmxdemodvi/rfmxdemod_ademod_configure_rbw_filter.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-vi/raw/resource/enus/rfmxdemodvi/rfmxdemod_ademod_configure_rbw_filter.html
- document_id: `rfmx-demod-vi`
- page_type: `leaf`
- content_type: ``

RFmxDemod ADemod Configure RBW Filter (VI)

RFmxDemod ADemod Configure RBW Filter (VI)

Owning Palette:

ADemod

Configures the resolution bandwidth (RBW) filter for analog demodulation measurements.

[IMAGE alt='RFmxDemod ADemod Configure RBW Filter' src='rfmxdemod_ademod_configure_rbw_filter.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | RBW specifies the bandwidth, in Hz, of the resolution bandwidth (RBW) filter to be applied to the acquired signal. |
|  | RBW Filter Type specifies the shape of the digital RBW filter. None (0) RBW filter is not applied on the acquired signal. Gaussian (1) RBW filter has a Gaussian response. Flat (2) RBW filter has a Flat response. Synch Tuned - 4 (3) RBW filter has a response of a 4-pole synchronously-tuned filter. Synch Tuned - 5 (4) RBW filter has a response of a 5-pole synchronously-tuned filter. RRC (5) RRC filter with roll-off specified by the ADemod RBW RRC Alpha property is used as the RBW filter. |
| None (0) | RBW filter is not applied on the acquired signal. |
| Gaussian (1) | RBW filter has a Gaussian response. |
| Flat (2) | RBW filter has a Flat response. |
| Synch Tuned - 4 (3) | RBW filter has a response of a 4-pole synchronously-tuned filter. |
| Synch Tuned - 5 (4) | RBW filter has a response of a 5-pole synchronously-tuned filter. |
| RRC (5) | RRC filter with roll-off specified by the ADemod RBW RRC Alpha property is used as the RBW filter. |
|  | RBW RRC Alpha specifies the roll-off factor of the root-raised cosine (RRC) filter. |
|  | Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxDemod Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-demod-vi path=rfmxdemodvi/rfmxdemod_ademod_fetch.html language=enus -->
## TOPIC 00017: rfmxdemodvi/rfmxdemod_ademod_fetch.html

- bundle_id: `rfmx-demod-vi`
- source_path: `rfmxdemodvi/rfmxdemod_ademod_fetch.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-vi/raw/resource/enus/rfmxdemodvi/rfmxdemod_ademod_fetch.html
- document_id: `rfmx-demod-vi`
- page_type: `leaf`
- content_type: ``

RFmxDemod ADemod Fetch (VI)

RFmxDemod ADemod Fetch (VI)

Owning Palette:

Fetch

Fetches the analog demodulation measurements.

#### RFmxDemod ADemod Fetch Carrier Measurement

Fetches the carrier measurement.

[IMAGE alt='RFmxDemod ADemod Fetch Carrier Measurement' src='rfmxdemod_ademod_fetch_carrier_measurement.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. This value is expressed in seconds. |
|  | Selector String comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxDemod Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Mean Carrier Frequency Error returns the mean of the measured carrier frequency error, in Hz. |
|  | Mean Carrier Power returns the mean of the measured carrier power, in dBm. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxDemod ADemod Fetch Mean Modulation Frequency

Fetches the mean modulation frequency.

[IMAGE alt='RFmxDemod ADemod Fetch Mean Modulation Frequency' src='rfmxdemod_ademod_fetch_mean_modulation_frequency.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. This value is expressed in seconds. |
|  | Selector String comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxDemod Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Mean Modulation Frequency returns the mean of the demodulated signal frequency. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxDemod ADemod Fetch Distortions

Fetches distortions for analog demodulation measurements.

[IMAGE alt='RFmxDemod ADemod Fetch Distortions' src='rfmxdemod_ademod_fetch_distortions.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. This value is expressed in seconds. |
|  | Selector String comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxDemod Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Average SINAD returns the averaged signal-to-noise and distortion ratio, in dB, of the demodulated signal. |
|  | Average SNR returns the averaged signal-to-noise ratio, in dB, of the demodulated signal. |
|  | Average THD returns the averaged total harmonic distortion, as a percentage, of demodulated signal. |
|  | Average THD with Noise returns the averaged total harmonic distortion with noise, as a percentage, of the demodulated signal. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxDemod ADemod Fetch AM Mean Modulation Depth

Fetches AM mean modulation depth for analog demodulation measurements.

[IMAGE alt='RFmxDemod ADemod Fetch AM Mean Modulation Depth' src='rfmxdemod_ademod_fetch_am_mean_modulation_depth.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. This value is expressed in seconds. |
|  | Selector String comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxDemod Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Mean Modulation Depth returns the mean amplitude variation, as a percentage, around the unmodulated carrier amplitude. If the carrier is suppressed, the amplitude variation of the modulating signal is returned. |
|  | Mean Peak to Peak /2 returns the mean (peak-to-peak)/2 amplitude, as a percentage, of the modulating signal. |
|  | Mean RMS returns the mean RMS amplitude of the modulating signal. |
|  | Mean Negative Peak returns the mean negative peak amplitude, as a percentage, of the modulating signal. |
|  | Mean Positive Peak returns the mean positive peak amplitude, as a percentage, of the modulating signal. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxDemod ADemod Fetch FM Mean Deviation

Fetches the FM mean deviation measurements.

[IMAGE alt='RFmxDemod ADemod Fetch FM Mean Deviation' src='rfmxdemod_ademod_fetch_fm_mean_deviation.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. This value is expressed in seconds. |
|  | Selector String comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxDemod Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Mean Deviation returns the mean deviation, in Hz, of the frequency-modulated signal. |
|  | Mean Peak to Peak /2 returns the mean (peak-to-peak)/2 frequency variation, in Hz, around the nominal frequency of the FM carrier. |
|  | Mean RMS returns the mean RMS frequency deviation, in Hz, of the frequency-modulated signal. |
|  | Mean Negative Peak returns the mean negative peak frequency deviation of the frequency-modulated signal. |
|  | Mean Positive Peak returns the mean positive peak frequency deviation, in Hz, of the frequency-modulated signal. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxDemod ADemod Fetch PM Mean Deviation

Fetches the PM mean deviation measurements.

[IMAGE alt='RFmxDemod ADemod Fetch PM Mean Deviation' src='rfmxdemod_ademod_fetch_pm_mean_deviation.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. This value is expressed in seconds. |
|  | Selector String comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxDemod Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Mean Deviation returns the mean deviation around the unmodulated carrier phase. |
|  | Mean Peak to Peak /2 returns the mean (peak-to-peak)/2 phase deviation, in degrees, around the unmodulated carrier phase. |
|  | Mean RMS returns the mean RMS phase deviation, in degrees, of the phase-modulated signal. |
|  | Mean Negative Peak returns the mean negative peak phase deviation, in degrees, around the unmodulated carrier phase. |
|  | Mean Positive Peak returns the mean positive peak phase deviation, in degrees, around the unmodulated carrier phase. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxDemod ADemod Fetch AM Maximum Modulation Depth

Fetches the AM maximum modulation depth.

[IMAGE alt='RFmxDemod ADemod Fetch AM Maximum Modulation Depth' src='rfmxdemod_ademod_fetch_am_maximum_modulation_depth.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. This value is expressed in seconds. |
|  | Selector String comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxDemod Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Maximum Modulation Depth returns the maximum modulation depth, as a percentage, measured across multiple acquisitions. |
|  | Maximum Peak to Peak /2 returns the maximum (peak-to-peak)/2 amplitude, as a percentage, of the modulating signal measured across multiple acquisitions. |
|  | Maximum RMS returns the maximum RMS amplitude, as a percentage, of the modulating signal measured across multiple acquisitions. |
|  | Maximum Negative Peak returns the maximum negative peak amplitude, as a percentage, of the modulating signal measured across multiple acquisitions. |
|  | Maximum Positive Peak returns the maximum positive peak amplitude, as a percentage, of the modulating signal measured across multiple acquisitions. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxDemod ADemod Fetch FM Maximum Deviation

Fetches the FM maximum deviation measurements.

[IMAGE alt='RFmxDemod ADemod Fetch FM Maximum Deviation' src='rfmxdemod_ademod_fetch_fm_maximum_deviation.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. This value is expressed in seconds. |
|  | Selector String comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxDemod Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Maximum Deviation returns the maximum frequency deviation, in Hz, of the frequency-modulated signal measured across multiple acquisitions. |
|  | Maximum Peak to Peak /2 returns the maximum (peak-to-peak)/2 frequency variation, in Hz, around the nominal frequency of the FM carrier measured across multiple acquisitions. |
|  | Maximum RMS returns the maximum RMS frequency deviation, in Hz, of the frequency-modulated signal measured across multiple acquisitions. |
|  | Maximum Negative Peak returns the maximum negative peak frequency deviation, in Hz, of the frequency-modulated signal measured across multiple acquisitions. |
|  | Maximum Positive Peak returns the maximum positive peak frequency deviation, in Hz, of the frequency-modulated signal measured across multiple acquisitions. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxDemod ADemod Fetch PM Maximum Deviation

Fetches the PM maximum deviation measurements.

[IMAGE alt='RFmxDemod ADemod Fetch PM Maximum Deviation' src='rfmxdemod_ademod_fetch_pm_maximum_deviation.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. This value is expressed in seconds. |
|  | Selector String comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxDemod Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Maximum Deviation returns the maximum phase deviation, in degrees, around the unmodulated carrier phase measured over multiple acquisitions. |
|  | Maximum Peak to Peak /2 returns the maximum (peak to peak)/2 phase deviation, in degrees, around the unmodulated carrier phase measured over multiple acquisitions. |
|  | Maximum RMS returns the maximum RMS phase deviation, in degrees, of the PM signal measured over multiple acquisitions. |
|  | Maximum Negative Peak returns the maximum negative peak phase deviation, in degrees, around the unmodulated carrier phase, measured across multiple acquisitions. |
|  | Maximum Positive Peak returns the maximum positive peak phase deviation, in degrees, around the unmodulated carrier phase, measured across multiple acquisitions. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxDemod ADemod Fetch Demod Signal Trace

Fetches the demodulated signal trace.

[IMAGE alt='RFmxDemod ADemod Fetch Demod Signal Trace' src='rfmxdemod_ademod_fetch_demod_signal_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. This value is expressed in seconds. |
|  | Selector String comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxDemod Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Demodulated Signal returns the demodulated signal. x0 returns the start time, in seconds. dx returns the sample duration, in seconds. y returns the signal amplitude in % for AM, Hz for FM, degrees for PM signals, at each time instance. |
|  | x0 returns the start time, in seconds. |
|  | dx returns the sample duration, in seconds. |
|  | y returns the signal amplitude in % for AM, Hz for FM, degrees for PM signals, at each time instance. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxDemod ADemod Fetch Demod Spectrum Trace

Fetches the demodulated signal spectrum trace.

[IMAGE alt='RFmxDemod ADemod Fetch Demod Spectrum Trace' src='rfmxdemod_ademod_fetch_demod_spectrum_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. This value is expressed in seconds. |
|  | Selector String comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxDemod Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Demodulated Spectrum returns the demodulated signal spectrum. x0 returns the start bin frequency, in Hz. dx returns the frequency bin spacing, in Hz. y returns the amplitude, as a percentage for AM, in Hz for FM, and in degrees for PM signals, measured at each frequency bin. |
|  | x0 returns the start bin frequency, in Hz. |
|  | dx returns the frequency bin spacing, in Hz. |
|  | y returns the amplitude, as a percentage for AM, in Hz for FM, and in degrees for PM signals, measured at each frequency bin. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-demod-vi path=rfmxdemodvi/rfmxdemod_analyze_(iq_1_wfm).html language=enus -->
## TOPIC 00018: rfmxdemodvi/rfmxdemod_analyze_(iq_1_wfm).html

- bundle_id: `rfmx-demod-vi`
- source_path: `rfmxdemodvi/rfmxdemod_analyze_(iq_1_wfm).html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-vi/raw/resource/enus/rfmxdemodvi/rfmxdemod_analyze_(iq_1_wfm).html
- document_id: `rfmx-demod-vi`
- page_type: `leaf`
- content_type: ``

RFmxDemod Analyze (IQ, 1 Wfm) (VI)

RFmxDemod Analyze (IQ, 1 Wfm) (VI)

Owning Palette:

Advanced

Performs the enabled measurements on the I/Q complex waveform that you specify in **IQ** parameter. Call this VI after you configure the signal and measurement properties. You can fetch measurement results using the Fetch VIs or result properties in the property node.

Use this VI only if the Recommended Acquisition Type property value is **IQ**.

|  | Note Query the Recommended Acquisition Type property from the RFmxInstr Property Node after calling the RFmxDemod Commit VI. |
| --- | --- |

[IMAGE alt='RFmxDemod Analyze (IQ 1 Wfm)' src='rfmxdemod_analyze_(iq_1_wfm).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize VI with option string as "AnalysisOnly=1". |
| --- | --- |
|  | IQ specifies the data for a complex waveform including the start, delta, and actual values. x0 specifies the start time of the input Y array. This value is expressed in seconds. dx specifies the time interval between the samples in the input Y array. This value is expressed in seconds. The reciprocal of dx indicates the I/Q rate of the input signal. y specifies an array of complex-valued time domain data. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively. |
|  | x0 specifies the start time of the input Y array. This value is expressed in seconds. |
|  | dx specifies the time interval between the samples in the input Y array. This value is expressed in seconds. The reciprocal of dx indicates the I/Q rate of the input signal. |
|  | y specifies an array of complex-valued time domain data. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively. |
|  | Reset? resets measurement averaging. If you enable averaging, set this parameter to TRUE for first record and FALSE for subsequent records. |
|  | Result Name specifies the name to be associated with measurement results. Provide a unique name, such as "r1" to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. The default value is "" (empty string) which refers to default result instance. Example: "result::r1" "r1" |
|  | Selector String specifies a selector string comprising of the signal name and result name. The result name can either be specified through this input or the Result Name parameter. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name in this input, either the result name specified by Result Name parameter or the default result instance is used. The default is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxDemod Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Selector String Out returns the selector string that can be passed to the Selector String parameter of Configure, Initiate, and Fetch VIs. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-demod-vi path=rfmxdemodvi/rfmxdemod_auto_level.html language=enus -->
## TOPIC 00019: rfmxdemodvi/rfmxdemod_auto_level.html

- bundle_id: `rfmx-demod-vi`
- source_path: `rfmxdemodvi/rfmxdemod_auto_level.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-vi/raw/resource/enus/rfmxdemodvi/rfmxdemod_auto_level.html
- document_id: `rfmx-demod-vi`
- page_type: `leaf`
- content_type: ``

RFmxDemod Auto Level (VI)

RFmxDemod Auto Level (VI)

Owning Palette:

Configuration

Examines the input signal to calculate the peak power level and sets it as the value of the Reference Level property. Use this VI to help calculate an approximate setting for the reference level.

The RFmxDemod Auto Level VI does the following tasks:

1. Resets the mixer level, mixer level offset, and IF output power level offset.
2. Sets the starting reference level to the maximum reference level supported by the device based on the current RF attenuation, mechanical attenuation, and preamp enabled settings.
3. Iterates to adjust the reference level based on the input signal peak power.
4. Uses immediate triggering and restores the trigger settings back to user setting after the execution.

You can also specify the starting reference level using the Auto Level Initial Ref Level property.

When using NI 5663, 5665, or 5668R devices, NI recommends that you set an appropriate value for mechanical attenuation before calling the RFmxDemod Auto Level VI. Setting an appropriate value for mechanical attenuation reduces the number of times the attenuator settings are changed by this function; thus reducing wear and tear, and maximizing the life time of the attenuator.

[IMAGE alt='RFmxDemod Auto Level' src='rfmxdemod_auto_level.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Bandwidth specifies the bandwidth, in Hz, of the signal to be analyzed. |
|  | Measurement Interval specifies the acquisition length. This value is used to compute the number of samples to acquire from the signal analyzer. This value is expressed in seconds. The default value is 10 ms. Auto Level VI does not use any trigger for acquisition. It ignores the user-configured trigger properties. NI recommends that you set a sufficiently high measurement interval to ensure that the acquired waveform is at least as long as one period of the signal. |
|  | Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxDemod Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Reference Level returns the estimated peak power level of the input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-demod-vi path=rfmxdemodvi/rfmxdemod_build_signal_string.html language=enus -->
## TOPIC 00020: rfmxdemodvi/rfmxdemod_build_signal_string.html

- bundle_id: `rfmx-demod-vi`
- source_path: `rfmxdemodvi/rfmxdemod_build_signal_string.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-vi/raw/resource/enus/rfmxdemodvi/rfmxdemod_build_signal_string.html
- document_id: `rfmx-demod-vi`
- page_type: `leaf`
- content_type: ``

RFmxDemod Build Signal String (VI)

RFmxDemod Build Signal String (VI)

Owning Palette:

Build String

Creates a selector string for use with Configuration or Fetch properties and VIs.

[IMAGE alt='RFmxDemod Build Signal String' src='rfmxdemod_build_signal_string.gif']

|  | Result Name specifies the result name for building the selector string. This input accepts the result name with or without the "result::" prefix. The default value is "" (empty string). Example: "" "result::r1" "r1" |
| --- | --- |
|  | Signal Name specifies the signal name for building the selector string. This input accepts the signal name with or without the "signal::" prefix. The default value is "" (empty string). Example: "" "signal::sig1" "sig1" |
|  | Selector String returns the selector string created by this VI. |

<!--NI_TOPIC bundle=rfmx-demod-vi path=rfmxdemodvi/rfmxdemod_check_measurement_status.html language=enus -->
## TOPIC 00021: rfmxdemodvi/rfmxdemod_check_measurement_status.html

- bundle_id: `rfmx-demod-vi`
- source_path: `rfmxdemodvi/rfmxdemod_check_measurement_status.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-vi/raw/resource/enus/rfmxdemodvi/rfmxdemod_check_measurement_status.html
- document_id: `rfmx-demod-vi`
- page_type: `leaf`
- content_type: ``

RFmxDemod Check Measurement Status (VI)

RFmxDemod Check Measurement Status (VI)

Owning Palette:

Utility

Checks the status of the measurement. Use this VI to check for any errors that may occur during measurement or to check whether the measurement is complete and results are available.

[IMAGE alt='RFmxDemod Check Measurement Status' src='rfmxdemod_check_measurement_status.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Selector String comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxDemod Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | done? indicates whether the measurement is complete. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-demod-vi path=rfmxdemodvi/rfmxdemod_clear_all_named_results.html language=enus -->
## TOPIC 00022: rfmxdemodvi/rfmxdemod_clear_all_named_results.html

- bundle_id: `rfmx-demod-vi`
- source_path: `rfmxdemodvi/rfmxdemod_clear_all_named_results.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-vi/raw/resource/enus/rfmxdemodvi/rfmxdemod_clear_all_named_results.html
- document_id: `rfmx-demod-vi`
- page_type: `leaf`
- content_type: ``

RFmxDemod Clear All Named Results (VI)

RFmxDemod Clear All Named Results (VI)

Owning Palette:

Advanced

Clears all results for the signal that you specify in the **Selector String** parameter.

[IMAGE alt='RFmxDemod Clear All Named Results' src='rfmxdemod_clear_all_named_results.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxDemod Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-demod-vi path=rfmxdemodvi/rfmxdemod_clear_named_result.html language=enus -->
## TOPIC 00023: rfmxdemodvi/rfmxdemod_clear_named_result.html

- bundle_id: `rfmx-demod-vi`
- source_path: `rfmxdemodvi/rfmxdemod_clear_named_result.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-vi/raw/resource/enus/rfmxdemodvi/rfmxdemod_clear_named_result.html
- document_id: `rfmx-demod-vi`
- page_type: `leaf`
- content_type: ``

RFmxDemod Clear Named Result (VI)

RFmxDemod Clear Named Result (VI)

Owning Palette:

Advanced

Clears an instance of the result that you specify in the **Selector String** parameter.

[IMAGE alt='RFmxDemod Clear Named Result' src='rfmxdemod_clear_named_result.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Selector String comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxDemod Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-demod-vi path=rfmxdemodvi/rfmxdemod_clone_signal_configuration.html language=enus -->
## TOPIC 00024: rfmxdemodvi/rfmxdemod_clone_signal_configuration.html

- bundle_id: `rfmx-demod-vi`
- source_path: `rfmxdemodvi/rfmxdemod_clone_signal_configuration.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-vi/raw/resource/enus/rfmxdemodvi/rfmxdemod_clone_signal_configuration.html
- document_id: `rfmx-demod-vi`
- page_type: `leaf`
- content_type: ``

RFmxDemod Clone Signal Configuration (VI)

RFmxDemod Clone Signal Configuration (VI)

Owning Palette:

Advanced

Creates a new instance of a signal by copying all the property values from an existing signal instance.

[IMAGE alt='RFmxDemod Clone Signal Configuration' src='rfmxdemod_clone_signal_configuration.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | New Signal Name specifies the name of the new signal. This parameter accepts the signal name with or without the "signal::" prefix. Example: "signal::NewSigName" "NewSigName" |
|  | Old Signal Name specifies the name of the existing signal. This parameter accepts the signal name with or without the "signal::" prefix. Example: "signal::OldSigName" "OldSigName" |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Selector String Out returns the selector string that can be passed to the Selector String parameter on Configure, Initiate, and Fetch VIs. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-demod-vi path=rfmxdemodvi/rfmxdemod_commit.html language=enus -->
## TOPIC 00025: rfmxdemodvi/rfmxdemod_commit.html

- bundle_id: `rfmx-demod-vi`
- source_path: `rfmxdemodvi/rfmxdemod_commit.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-vi/raw/resource/enus/rfmxdemodvi/rfmxdemod_commit.html
- document_id: `rfmx-demod-vi`
- page_type: `leaf`
- content_type: ``

RFmxDemod Commit (VI)

RFmxDemod Commit (VI)

Owning Palette:

Utility

Commits settings to the hardware. Calling this VI is optional. RFmxDemod commits settings to the hardware when you call the [RFmxDemod Initiate](../rfmxdemodvi/rfmxdemod_initiate.html) VI or any of the measurement Read VIs.

[IMAGE alt='RFmxDemod Commit' src='rfmxdemod_commit.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxDemod Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-demod-vi path=rfmxdemodvi/rfmxdemod_configure_external_attenuation.html language=enus -->
## TOPIC 00026: rfmxdemodvi/rfmxdemod_configure_external_attenuation.html

- bundle_id: `rfmx-demod-vi`
- source_path: `rfmxdemodvi/rfmxdemod_configure_external_attenuation.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-vi/raw/resource/enus/rfmxdemodvi/rfmxdemod_configure_external_attenuation.html
- document_id: `rfmx-demod-vi`
- page_type: `leaf`
- content_type: ``

RFmxDemod Configure External Attenuation (VI)

RFmxDemod Configure External Attenuation (VI)

Owning Palette:

Configuration

Configures the attenuation of a switch (or cable) connected to the RF IN connector of the signal analyzer.

[IMAGE alt='RFmxDemod Configure External Attenuation' src='rfmxdemod_configure_external_attenuation.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | External Attenuation specifies the attenuation, in dB, of a switch (or cable) connected to the RF IN connector of the signal analyzer. For more information about attenuation, refer to the Attenuation and Signal Levels topic for your device in the NI RF Vector Signal Analyzers Help. |
|  | Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxDemod Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-demod-vi path=rfmxdemodvi/rfmxdemod_configure_frequency.html language=enus -->
## TOPIC 00027: rfmxdemodvi/rfmxdemod_configure_frequency.html

- bundle_id: `rfmx-demod-vi`
- source_path: `rfmxdemodvi/rfmxdemod_configure_frequency.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-vi/raw/resource/enus/rfmxdemodvi/rfmxdemod_configure_frequency.html
- document_id: `rfmx-demod-vi`
- page_type: `leaf`
- content_type: ``

RFmxDemod Configure Frequency (VI)

RFmxDemod Configure Frequency (VI)

Owning Palette:

Configuration

Configures the expected carrier frequency of the RF signal that needs to be acquired. The signal analyzer tunes to this frequency.

[IMAGE alt='RFmxDemod Configure Frequency' src='rfmxdemod_configure_frequency.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Center Frequency specifies the carrier frequency, in Hz, of the RF signal that needs to be acquired. The signal analyzer tunes to this frequency. The default of this property is hardware dependent. |
|  | Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxDemod Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-demod-vi path=rfmxdemodvi/rfmxdemod_configure_reference_level.html language=enus -->
## TOPIC 00028: rfmxdemodvi/rfmxdemod_configure_reference_level.html

- bundle_id: `rfmx-demod-vi`
- source_path: `rfmxdemodvi/rfmxdemod_configure_reference_level.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-vi/raw/resource/enus/rfmxdemodvi/rfmxdemod_configure_reference_level.html
- document_id: `rfmx-demod-vi`
- page_type: `leaf`
- content_type: ``

RFmxDemod Configure Reference Level (VI)

RFmxDemod Configure Reference Level (VI)

Owning Palette:

Configuration

Configures the reference level that represents the maximum expected power of an RF input signal.

[IMAGE alt='RFmxDemod Configure Reference Level' src='rfmxdemod_configure_reference_level.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Reference Level specifies the reference level which represents the maximum expected power of an RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices. The default of this parameter is hardware dependent. |
|  | Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxDemod Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-demod-vi path=rfmxdemodvi/rfmxdemod_configure_rf.html language=enus -->
## TOPIC 00029: rfmxdemodvi/rfmxdemod_configure_rf.html

- bundle_id: `rfmx-demod-vi`
- source_path: `rfmxdemodvi/rfmxdemod_configure_rf.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-vi/raw/resource/enus/rfmxdemodvi/rfmxdemod_configure_rf.html
- document_id: `rfmx-demod-vi`
- page_type: `leaf`
- content_type: ``

RFmxDemod Configure RF (VI)

RFmxDemod Configure RF (VI)

Owning Palette:

Configuration

Configures the RF properties of the signal by specifying the selector string.

[IMAGE alt='RFmxDemod Configure RF' src='rfmxdemod_configure_rf.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Center Frequency specifies the carrier frequency, in Hz, of the RF signal that needs to be acquired. The signal analyzer tunes to this frequency. The default of this property is hardware dependent. |
|  | Reference Level specifies the reference level which represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices. The default of this property is hardware dependent. |
|  | External Attenuation specifies the attenuation, in dB, of a switch (or cable) connected to the RF IN connector of the signal analyzer. For more information about attenuation, refer to the Attenuation and Signal Levels topic for your device in the NI RF Vector Signal Analyzers Help. |
|  | Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxDemod Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-demod-vi path=rfmxdemodvi/rfmxdemod_configure_trigger.html language=enus -->
## TOPIC 00030: rfmxdemodvi/rfmxdemod_configure_trigger.html

- bundle_id: `rfmx-demod-vi`
- source_path: `rfmxdemodvi/rfmxdemod_configure_trigger.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-vi/raw/resource/enus/rfmxdemodvi/rfmxdemod_configure_trigger.html
- document_id: `rfmx-demod-vi`
- page_type: `leaf`
- content_type: ``

RFmxDemod Configure Trigger (VI)

RFmxDemod Configure Trigger (VI)

Owning Palette:

Configuration

Configures the Reference Trigger to use to acquire the signal.

#### RFmxDemod Disable Trigger

Disables the trigger.

[IMAGE alt='RFmxDemod Disable Trigger' src='rfmxdemod_disable_trigger.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxDemod Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxDemod Configure Digital Edge Trigger

Configures the digital edge trigger.

[IMAGE alt='RFmxDemod Configure Digital Edge Trigger' src='rfmxdemod_configure_digital_edge_trigger.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Digital Edge Source specifies the source terminal for the digital-edge trigger. This parameter is used only when you set the Trigger Type property to Digital Edge. The default value is PFI0. PFI0 (PFI0) The trigger is received on PFI 0. PFI1 (PFI1) The trigger is received on PFI 1. PXI_Trig0 (PXI_Trig0) The trigger is received on PXI trigger line 0. PXI_Trig1 (PXI_Trig1) The trigger is received on PXI trigger line 1. PXI_Trig2 (PXI_Trig2) The trigger is received on PXI trigger line 2. PXI_Trig3 (PXI_Trig3) The trigger is received on PXI trigger line 3. PXI_Trig4 (PXI_Trig4) The trigger is received on PXI trigger line 4. PXI_Trig5 (PXI_Trig5) The trigger is received on PXI trigger line 5. PXI_Trig6 (PXI_Trig6) The trigger is received on PXI trigger line 6. PXI_Trig7 (PXI_Trig7) The trigger is received on PXI trigger line 7. PXI_STAR (PXI_STAR) The trigger is received on the PXI star trigger line. PXIe_DStarB (PXIe_DStarB) The trigger is received on the PXIe DStar B trigger line. TimerEvent (TimerEvent) The trigger is received from the Timer Event. |
| PFI0 (PFI0) | The trigger is received on PFI 0. |
| PFI1 (PFI1) | The trigger is received on PFI 1. |
| PXI_Trig0 (PXI_Trig0) | The trigger is received on PXI trigger line 0. |
| PXI_Trig1 (PXI_Trig1) | The trigger is received on PXI trigger line 1. |
| PXI_Trig2 (PXI_Trig2) | The trigger is received on PXI trigger line 2. |
| PXI_Trig3 (PXI_Trig3) | The trigger is received on PXI trigger line 3. |
| PXI_Trig4 (PXI_Trig4) | The trigger is received on PXI trigger line 4. |
| PXI_Trig5 (PXI_Trig5) | The trigger is received on PXI trigger line 5. |
| PXI_Trig6 (PXI_Trig6) | The trigger is received on PXI trigger line 6. |
| PXI_Trig7 (PXI_Trig7) | The trigger is received on PXI trigger line 7. |
| PXI_STAR (PXI_STAR) | The trigger is received on the PXI star trigger line. |
| PXIe_DStarB (PXIe_DStarB) | The trigger is received on the PXIe DStar B trigger line. |
| TimerEvent (TimerEvent) | The trigger is received from the Timer Event. |
|  | Digital Edge specifies whether the signal analyzer detects a rising or falling edge on the digital-edge trigger signal. The parameter is used only when you set the Trigger Type property to Digital Edge. The default value is Rising Edge. Rising Edge (0) The trigger asserts on the rising edge of the signal. Falling Edge (1) The trigger asserts on the falling edge of the signal. |
| Rising Edge (0) | The trigger asserts on the rising edge of the signal. |
| Falling Edge (1) | The trigger asserts on the falling edge of the signal. |
|  | Trigger Delay specifies the trigger delay time, in seconds. |
|  | Enable Trigger? specifies whether to enable the trigger. The default value is TRUE. |
|  | Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxDemod Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxDemod Configure IQ Power Edge Trigger

Configures the I/Q power edge trigger.

[IMAGE alt='RFmxDemod Configure IQ Power Edge Trigger' src='rfmxdemod_configure_iq_power_edge_trigger.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | IQ Power Edge Source specifies the channel from which the device monitors the trigger. The default value is 0. |
|  | IQ Power Edge Slope specifies whether the device asserts the trigger when the signal power is rising or falling. The device asserts the trigger when the signal power exceeds the specified level with the slope you specify. This parameter is used only when you set the Trigger Type property to IQ Power Edge. The default value is Rising Slope. Rising Slope (0) The trigger asserts when the signal power is rising. Falling Slope (1) The trigger asserts when the signal power is falling. |
| Rising Slope (0) | The trigger asserts when the signal power is rising. |
| Falling Slope (1) | The trigger asserts when the signal power is falling. |
|  | IQ Power Edge Level specifies the power level at which the device triggers. This value is expressed in dB when you set the IQ Power Edge Level Type parameter to Relative, and this value is expressed in dBm when you set the IQ Power Edge Level Type parameter to Absolute. The device asserts the trigger when the signal exceeds the level specified by the value of this parameter, taking into consideration the specified slope. The default of this property is hardware dependent. |
|  | Enable Trigger? specifies whether to enable the trigger. The default value is TRUE. |
|  | Trigger Delay specifies the trigger delay time, in seconds. |
|  | Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxDemod Build Signal String VI to build the selector string. |
|  | Minimum Quiet Time Mode specifies whether the measurement computes the minimum quiet time used for triggering. The default value is Manual. Manual (0) The minimum quiet time for triggering is the value of the Min Quiet Time parameter. Auto (1) The measurement computes the minimum quiet time used for triggering. |
| Manual (0) | The minimum quiet time for triggering is the value of the Min Quiet Time parameter. |
| Auto (1) | The measurement computes the minimum quiet time used for triggering. |
|  | Minimum Quiet Time specifies the time duration, in seconds, for which the signal must be quiet before the signal analyzer arms the I/Q power-edge trigger. |
|  | IQ Power Edge Level Type specifies the reference for the IQ Power Edge Level parameter. The IQ Power Edge Level Type parameter is used only when you set the Trigger Type property to IQ Power Edge. The default value is Absolute. Relative (0) The IQ Power Edge Level property is relative to the value of the Reference Level property. Absolute (1) The IQ Power Edge Level property specifies the absolute power. |
| Relative (0) | The IQ Power Edge Level property is relative to the value of the Reference Level property. |
| Absolute (1) | The IQ Power Edge Level property specifies the absolute power. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxDemod Configure Software Edge Trigger

Configures the software-edge trigger.

[IMAGE alt='RFmxDemod Configure Software Edge Trigger' src='rfmxdemod_configure_software_edge_trigger.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Trigger Delay specifies the trigger delay time, in seconds. |
|  | Enable Trigger? specifies whether to enable the trigger. The default value is TRUE. |
|  | Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxDemod Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-demod-vi path=rfmxdemodvi/rfmxdemod_create_signal_configuration.html language=enus -->
## TOPIC 00031: rfmxdemodvi/rfmxdemod_create_signal_configuration.html

- bundle_id: `rfmx-demod-vi`
- source_path: `rfmxdemodvi/rfmxdemod_create_signal_configuration.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-vi/raw/resource/enus/rfmxdemodvi/rfmxdemod_create_signal_configuration.html
- document_id: `rfmx-demod-vi`
- page_type: `leaf`
- content_type: ``

RFmxDemod Create Signal Configuration (VI)

RFmxDemod Create Signal Configuration (VI)

Owning Palette:

Advanced

Creates a new instance of a signal.

[IMAGE alt='RFmxDemod Create Signal Configuration' src='rfmxdemod_create_signal_configuration.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Signal Name specifies the name of the signal. This parameter accepts the signal name with or without the "signal::" prefix. Example: "signal::sig1" "sig1" |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Selector String Out returns the selector string that can be passed to the Selector String parameter on Configure, Initiate, and Fetch VIs. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-demod-vi path=rfmxdemodvi/rfmxdemod_ddemod_configure_averaging.html language=enus -->
## TOPIC 00032: rfmxdemodvi/rfmxdemod_ddemod_configure_averaging.html

- bundle_id: `rfmx-demod-vi`
- source_path: `rfmxdemodvi/rfmxdemod_ddemod_configure_averaging.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-vi/raw/resource/enus/rfmxdemodvi/rfmxdemod_ddemod_configure_averaging.html
- document_id: `rfmx-demod-vi`
- page_type: `leaf`
- content_type: ``

RFmxDemod DDemod Configure Averaging (VI)

RFmxDemod DDemod Configure Averaging (VI)

Owning Palette:

DDemod

Configures averaging for digital demodulation measurements.

[IMAGE alt='RFmxDemod DDemod Configure Averaging' src='rfmxdemod_ddemod_configure_averaging.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Averaging Enabled enables averaging for digital demodulation measurement. False (0) The measurement is performed on a single acquisition. True (1) The measurement uses the value of the Averaging Count parameter for the number of acquisitions over which the measurement is averaged. The traces are not averaged. |
| False (0) | The measurement is performed on a single acquisition. |
| True (1) | The measurement uses the value of the Averaging Count parameter for the number of acquisitions over which the measurement is averaged. The traces are not averaged. |
|  | Averaging Count specifies the number of acquisitions used for averaging when you set the Averaging Enabled parameter to True. |
|  | Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxDemod Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-demod-vi path=rfmxdemodvi/rfmxdemod_ddemod_configure_equalizer.html language=enus -->
## TOPIC 00033: rfmxdemodvi/rfmxdemod_ddemod_configure_equalizer.html

- bundle_id: `rfmx-demod-vi`
- source_path: `rfmxdemodvi/rfmxdemod_ddemod_configure_equalizer.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-vi/raw/resource/enus/rfmxdemodvi/rfmxdemod_ddemod_configure_equalizer.html
- document_id: `rfmx-demod-vi`
- page_type: `leaf`
- content_type: ``

RFmxDemod DDemod Configure Equalizer (VI)

RFmxDemod DDemod Configure Equalizer (VI)

Owning Palette:

DDemod

Configures the equalizer.

[IMAGE alt='RFmxDemod DDemod Configure Equalizer' src='rfmxdemod_ddemod_configure_equalizer.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Equalizer Mode specifies whether the measurement needs to perform equalization. The default value is Off. Off (0) Equalization is not performed. Train (1) The adaptive feedforward equalizer is turned ON to compensate for the effect of the channel. You can set the initial coefficients to be used by the equalizer. If you do not specify the initial coefficients, an impulse is used. Hold (2) The filter that you specify using the initial coefficients is used as the channel filter and is applied before demodulating the acquired signal. |
| Off (0) | Equalization is not performed. |
| Train (1) | The adaptive feedforward equalizer is turned ON to compensate for the effect of the channel. You can set the initial coefficients to be used by the equalizer. If you do not specify the initial coefficients, an impulse is used. |
| Hold (2) | The filter that you specify using the initial coefficients is used as the channel filter and is applied before demodulating the acquired signal. |
|  | Equalizer Filter Length specifies the length of the equalization filter to be computed. The length is specified in terms of symbols. This parameter is ignored when the equalizer initial coefficients are specified. |
|  | Equalizer Initial Coefficients specifies the equalizer initial coefficients. x0 always pass 0 to this parameter. Any other values are ignored. dx specifies the spacing between the coefficients as a fraction of the symbol spacing. For example, if four coefficients correspond to one symbol, the spacing is 1/4. y specifies the initial coefficients to be used by the equalizer. |
|  | x0 always pass 0 to this parameter. Any other values are ignored. |
|  | dx specifies the spacing between the coefficients as a fraction of the symbol spacing. For example, if four coefficients correspond to one symbol, the spacing is 1/4. |
|  | y specifies the initial coefficients to be used by the equalizer. |
|  | Equalizer Training Count specifies the number of iterations during which the equalizer adapts its coefficients in the training stage. |
|  | Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxDemod Build Signal String VI to build the selector string. |
|  | Equalizer Convergence Factor specifies the incremental step used to adapt the equalizer to the channel during the training stage. The default value is 0.0001. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-demod-vi path=rfmxdemodvi/rfmxdemod_ddemod_configure_equalizer_initial_coefficients.html language=enus -->
## TOPIC 00034: rfmxdemodvi/rfmxdemod_ddemod_configure_equalizer_initial_coefficients.html

- bundle_id: `rfmx-demod-vi`
- source_path: `rfmxdemodvi/rfmxdemod_ddemod_configure_equalizer_initial_coefficients.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-vi/raw/resource/enus/rfmxdemodvi/rfmxdemod_ddemod_configure_equalizer_initial_coefficients.html
- document_id: `rfmx-demod-vi`
- page_type: `leaf`
- content_type: ``

RFmxDemod DDemod Configure Equalizer Initial Coefficients (VI)

RFmxDemod DDemod Configure Equalizer Initial Coefficients (VI)

Owning Palette:

DDemod

Configures the equalizer coefficients.

[IMAGE alt='RFmxDemod DDemod Configure Equalizer Initial Coefficients' src='rfmxdemod_ddemod_configure_equalizer_initial_coefficients.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Equalizer Initial Coefficients specifies the equalizer initial coefficients. x0 always pass 0 to this parameter. Any other values are ignored. dx specifies the spacing between the coefficients as a fraction of the symbol spacing. For example, if four coefficients correspond to one symbol, the spacing is 1/4. y specifies the initial coefficients to be used by the equalizer. |
|  | x0 always pass 0 to this parameter. Any other values are ignored. |
|  | dx specifies the spacing between the coefficients as a fraction of the symbol spacing. For example, if four coefficients correspond to one symbol, the spacing is 1/4. |
|  | y specifies the initial coefficients to be used by the equalizer. |
|  | Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxDemod Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-demod-vi path=rfmxdemodvi/rfmxdemod_ddemod_configure_evm_normalization_reference.html language=enus -->
## TOPIC 00035: rfmxdemodvi/rfmxdemod_ddemod_configure_evm_normalization_reference.html

- bundle_id: `rfmx-demod-vi`
- source_path: `rfmxdemodvi/rfmxdemod_ddemod_configure_evm_normalization_reference.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-vi/raw/resource/enus/rfmxdemodvi/rfmxdemod_ddemod_configure_evm_normalization_reference.html
- document_id: `rfmx-demod-vi`
- page_type: `leaf`
- content_type: ``

RFmxDemod DDemod Configure EVM Normalization Reference (VI)

RFmxDemod DDemod Configure EVM Normalization Reference (VI)

Owning Palette:

DDemod

Configures the error vector magnitude (EVM) normalization reference.

[IMAGE alt='RFmxDemod DDemod Configure EVM Normalization Reference' src='rfmxdemod_ddemod_configure_evm_normalization_reference.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | EVM Normalization Reference specifies the reference used to normalize the EVM. Peak (0) The EVM is normalized to the peak magnitude of the reference symbols. RMS (1) The EVM is normalized to the RMS magnitude of the reference symbols. This value is applicable only to modulation types, such as quadrature-amplitude modulation (QAM). This value is expressed in which the symbols in the map do not have a constant amplitude. |
| Peak (0) | The EVM is normalized to the peak magnitude of the reference symbols. |
| RMS (1) | The EVM is normalized to the RMS magnitude of the reference symbols. This value is applicable only to modulation types, such as quadrature-amplitude modulation (QAM). This value is expressed in which the symbols in the map do not have a constant amplitude. |
|  | Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxDemod Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-demod-vi path=rfmxdemodvi/rfmxdemod_ddemod_configure_fsk_deviation.html language=enus -->
## TOPIC 00036: rfmxdemodvi/rfmxdemod_ddemod_configure_fsk_deviation.html

- bundle_id: `rfmx-demod-vi`
- source_path: `rfmxdemodvi/rfmxdemod_ddemod_configure_fsk_deviation.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-vi/raw/resource/enus/rfmxdemodvi/rfmxdemod_ddemod_configure_fsk_deviation.html
- document_id: `rfmx-demod-vi`
- page_type: `leaf`
- content_type: ``

RFmxDemod DDemod Configure FSK Deviation (VI)

RFmxDemod DDemod Configure FSK Deviation (VI)

Owning Palette:

DDemod

Configures the expected FSK deviation.

[IMAGE alt='RFmxDemod DDemod Configure FSK Deviation' src='rfmxdemod_ddemod_configure_fsk_deviation.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | FSK Deviation specifies the expected FSK frequency deviation, in Hz. |
|  | FSK Reference Compensation Enabled specifies whether the FSK deviation that you specify is used to compensate for gain errors and to compute the FSK error. Default value is False. False (0) Does not compensate for gain errors. True (1) Compensates for gain errors. |
| False (0) | Does not compensate for gain errors. |
| True (1) | Compensates for gain errors. |
|  | Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxDemod Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-demod-vi path=rfmxdemodvi/rfmxdemod_ddemod_configure_m.html language=enus -->
## TOPIC 00037: rfmxdemodvi/rfmxdemod_ddemod_configure_m.html

- bundle_id: `rfmx-demod-vi`
- source_path: `rfmxdemodvi/rfmxdemod_ddemod_configure_m.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-vi/raw/resource/enus/rfmxdemodvi/rfmxdemod_ddemod_configure_m.html
- document_id: `rfmx-demod-vi`
- page_type: `leaf`
- content_type: ``

RFmxDemod DDemod Configure M (VI)

RFmxDemod DDemod Configure M (VI)

Owning Palette:

DDemod

Configures the M-ary number.

[IMAGE alt='RFmxDemod DDemod Configure M' src='rfmxdemod_ddemod_configure_m.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | M specifies the M-ary number, which is the number of distinct states that represent symbols in the complex baseband modulated waveform. Note Recommended values of M for modulation types are as follows: ASK: 2, 4, 8 FSK , PSK: 2, 4, 8, 16 QAM: 16, 32, 64, 128, 256, 512, 1028, 2048, 4096. The default value is 4. 2 (2) The M-ary number is 2. 4 (4) The M-ary number is 4. 8 (8) The M-ary number is 8. 16 (16) The M-ary number is 16. 32 (32) The M-ary number is 32. 64 (64) The M-ary number is 64. 128 (128) The M-ary number is 128. 256 (256) The M-ary number is 256. 512 (512) The M-ary number is 512. 1024 (1024) The M-ary number is 1,024. 2048 (2048) The M-ary number is 2,048. 4096 (4096) The M-ary number is 4,096. |
|  | Note Recommended values of M for modulation types are as follows: ASK: 2, 4, 8 FSK , PSK: 2, 4, 8, 16 QAM: 16, 32, 64, 128, 256, 512, 1028, 2048, 4096. |
| 2 (2) | The M-ary number is 2. |
| 4 (4) | The M-ary number is 4. |
| 8 (8) | The M-ary number is 8. |
| 16 (16) | The M-ary number is 16. |
| 32 (32) | The M-ary number is 32. |
| 64 (64) | The M-ary number is 64. |
| 128 (128) | The M-ary number is 128. |
| 256 (256) | The M-ary number is 256. |
| 512 (512) | The M-ary number is 512. |
| 1024 (1024) | The M-ary number is 1,024. |
| 2048 (2048) | The M-ary number is 2,048. |
| 4096 (4096) | The M-ary number is 4,096. |
|  | Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxDemod Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-demod-vi path=rfmxdemodvi/rfmxdemod_ddemod_configure_measurement_filter.html language=enus -->
## TOPIC 00038: rfmxdemodvi/rfmxdemod_ddemod_configure_measurement_filter.html

- bundle_id: `rfmx-demod-vi`
- source_path: `rfmxdemodvi/rfmxdemod_ddemod_configure_measurement_filter.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-vi/raw/resource/enus/rfmxdemodvi/rfmxdemod_ddemod_configure_measurement_filter.html
- document_id: `rfmx-demod-vi`
- page_type: `leaf`
- content_type: ``

RFmxDemod DDemod Configure Measurement Filter (VI)

RFmxDemod DDemod Configure Measurement Filter (VI)

Owning Palette:

DDemod

Configures the measurement filter.

[IMAGE alt='RFmxDemod DDemod Configure Measurement Filter' src='rfmxdemod_ddemod_configure_measurement_filter.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Measurement Filter Type specifies whether the measurement needs to compute the measurement filter based on the pulse shaping filter type or uses the custom measurement filter coefficients. The default value is Auto. Auto (0) The signal analyzer computes the measurement filter coefficients based on the pulse-shaping filter information that you specify in the Pulse Shaping Filter Type parameter of the RFmxDemod DDemod Configure Pulse Shaping Filter VI. If the Pulse Shaping Filter Type parameter is set to Custom, the signal analyzer enables equalization. Custom (1) The signal analyzer uses the coefficients specified by RFmxDemod DDemod Configure Measurement Filter Custom Coefficients VI. |
| Auto (0) | The signal analyzer computes the measurement filter coefficients based on the pulse-shaping filter information that you specify in the Pulse Shaping Filter Type parameter of the RFmxDemod DDemod Configure Pulse Shaping Filter VI. If the Pulse Shaping Filter Type parameter is set to Custom, the signal analyzer enables equalization. |
| Custom (1) | The signal analyzer uses the coefficients specified by RFmxDemod DDemod Configure Measurement Filter Custom Coefficients VI. |
|  | Measurement Filter Custom Coefficients specifies the measurements coefficients. Note To configure an impulse, set x0=0, dx=1, y[0]=1. x0 always pass 0 to this parameter. Any other values are ignored. dx specifies the spacing between the coefficients as a fraction of the symbol spacing. For example, if four coefficients correspond to one symbol, the spacing is 1/4. y specifies the filter coefficients to be used by demodulator. |
|  | Note To configure an impulse, set x0=0, dx=1, y[0]=1. |
|  | x0 always pass 0 to this parameter. Any other values are ignored. |
|  | dx specifies the spacing between the coefficients as a fraction of the symbol spacing. For example, if four coefficients correspond to one symbol, the spacing is 1/4. |
|  | y specifies the filter coefficients to be used by demodulator. |
|  | Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxDemod Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-demod-vi path=rfmxdemodvi/rfmxdemod_ddemod_configure_measurement_filter_custom_coefficients.html language=enus -->
## TOPIC 00039: rfmxdemodvi/rfmxdemod_ddemod_configure_measurement_filter_custom_coefficients.html

- bundle_id: `rfmx-demod-vi`
- source_path: `rfmxdemodvi/rfmxdemod_ddemod_configure_measurement_filter_custom_coefficients.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-vi/raw/resource/enus/rfmxdemodvi/rfmxdemod_ddemod_configure_measurement_filter_custom_coefficients.html
- document_id: `rfmx-demod-vi`
- page_type: `leaf`
- content_type: ``

RFmxDemod DDemod Configure Measurement Filter Custom Coefficients (VI)

RFmxDemod DDemod Configure Measurement Filter Custom Coefficients (VI)

Owning Palette:

DDemod

Configures the measurement filter custom coefficients.

[IMAGE alt='RFmxDemod DDemod Configure Measurement Filter Custom Coefficients' src='rfmxdemod_ddemod_configure_measurement_filter_custom_coefficients.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Measurement Filter Custom Coefficients specifies the measurement filter custom coefficients. Note To configure an impulse, set x0=0, dx=1, y[0]=1. x0 always pass 0 to this parameter. Any other values are ignored. dx specifies the spacing between the coefficients as a fraction of the symbol spacing. For example, if four coefficients correspond to one symbol, the spacing is 1/4. y specifies the filter coefficients to be used by demodulator. |
|  | Note To configure an impulse, set x0=0, dx=1, y[0]=1. |
|  | x0 always pass 0 to this parameter. Any other values are ignored. |
|  | dx specifies the spacing between the coefficients as a fraction of the symbol spacing. For example, if four coefficients correspond to one symbol, the spacing is 1/4. |
|  | y specifies the filter coefficients to be used by demodulator. |
|  | Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxDemod Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-demod-vi path=rfmxdemodvi/rfmxdemod_ddemod_configure_modulation_type.html language=enus -->
## TOPIC 00040: rfmxdemodvi/rfmxdemod_ddemod_configure_modulation_type.html

- bundle_id: `rfmx-demod-vi`
- source_path: `rfmxdemodvi/rfmxdemod_ddemod_configure_modulation_type.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-vi/raw/resource/enus/rfmxdemodvi/rfmxdemod_ddemod_configure_modulation_type.html
- document_id: `rfmx-demod-vi`
- page_type: `leaf`
- content_type: ``

RFmxDemod DDemod Configure Modulation Type (VI)

RFmxDemod DDemod Configure Modulation Type (VI)

Owning Palette:

DDemod

Configures the modulation type of the signal to be analyzed.

[IMAGE alt='RFmxDemod DDemod Configure Modulation Type' src='rfmxdemod_ddemod_configure_modulation_type.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Modulation Type specifies the digital modulation type of the signal that needs to be analyzed. The default value is PSK. ASK (0) The modulation type is amplitude-shift keying (ASK). FSK (1) The modulation type is frequency-shift keying (FSK). PSK (2) The modulation type is phase-shift keying (PSK). QAM (3) The modulation type is quadrature-amplitude modulation (QAM). MSK (4) The modulation type is minimum shift keying (MSK). |
| ASK (0) | The modulation type is amplitude-shift keying (ASK). |
| FSK (1) | The modulation type is frequency-shift keying (FSK). |
| PSK (2) | The modulation type is phase-shift keying (PSK). |
| QAM (3) | The modulation type is quadrature-amplitude modulation (QAM). |
| MSK (4) | The modulation type is minimum shift keying (MSK). |
|  | M specifies the M-ary number, which is the number of distinct states that represent symbols in the complex baseband modulated waveform. Note Recommended values of M for modulation types are as follows: ASK: 2, 4, 8 FSK , PSK: 2, 4, 8, 16 QAM: 16, 32, 64, 128, 256, 512, 1028, 2048, 4096. The default value is 4. 2 (2) The M-ary number is 2. 4 (4) The M-ary number is 4. 8 (8) The M-ary number is 8. 16 (16) The M-ary number is 16. 32 (32) The M-ary number is 32. 64 (64) The M-ary number is 64. 128 (128) The M-ary number is 128. 256 (256) The M-ary number is 256. 512 (512) The M-ary number is 512. 1024 (1024) The M-ary number is 1,024. 2048 (2048) The M-ary number is 2,048. 4096 (4096) The M-ary number is 4,096. |
|  | Note Recommended values of M for modulation types are as follows: ASK: 2, 4, 8 FSK , PSK: 2, 4, 8, 16 QAM: 16, 32, 64, 128, 256, 512, 1028, 2048, 4096. |
| 2 (2) | The M-ary number is 2. |
| 4 (4) | The M-ary number is 4. |
| 8 (8) | The M-ary number is 8. |
| 16 (16) | The M-ary number is 16. |
| 32 (32) | The M-ary number is 32. |
| 64 (64) | The M-ary number is 64. |
| 128 (128) | The M-ary number is 128. |
| 256 (256) | The M-ary number is 256. |
| 512 (512) | The M-ary number is 512. |
| 1024 (1024) | The M-ary number is 1,024. |
| 2048 (2048) | The M-ary number is 2,048. |
| 4096 (4096) | The M-ary number is 4,096. |
|  | Differential Enabled specifies whether the symbols are differentially encoded. This property is applicable only to PSK and MSK modulation types. The default value is False. False (0) The symbols are directly mapped onto the symbol map. True (1) In case of PSK modulation, the transition between two consecutive symbols is mapped onto the symbol map. In case of MSK modulation, the consecutive bits are XORed. Other modulation types do not have any impact. |
| False (0) | The symbols are directly mapped onto the symbol map. |
| True (1) | In case of PSK modulation, the transition between two consecutive symbols is mapped onto the symbol map. In case of MSK modulation, the consecutive bits are XORed. Other modulation types do not have any impact. |
|  | Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxDemod Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-demod-vi path=rfmxdemodvi/rfmxdemod_ddemod_configure_number_of_symbols.html language=enus -->
## TOPIC 00041: rfmxdemodvi/rfmxdemod_ddemod_configure_number_of_symbols.html

- bundle_id: `rfmx-demod-vi`
- source_path: `rfmxdemodvi/rfmxdemod_ddemod_configure_number_of_symbols.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-vi/raw/resource/enus/rfmxdemodvi/rfmxdemod_ddemod_configure_number_of_symbols.html
- document_id: `rfmx-demod-vi`
- page_type: `leaf`
- content_type: ``

RFmxDemod DDemod Configure Number of Symbols (VI)

RFmxDemod DDemod Configure Number of Symbols (VI)

Owning Palette:

DDemod

Configures the number of symbols to be measured.

[IMAGE alt='RFmxDemod DDemod Configure Number of Symbols' src='rfmxdemod_ddemod_configure_number_of_symbols.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Number of Symbols specifies the number of symbols to be analyzed. The measurement acquires additional symbols to account for filter delays. |
|  | Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxDemod Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-demod-vi path=rfmxdemodvi/rfmxdemod_ddemod_configure_psk_format.html language=enus -->
## TOPIC 00042: rfmxdemodvi/rfmxdemod_ddemod_configure_psk_format.html

- bundle_id: `rfmx-demod-vi`
- source_path: `rfmxdemodvi/rfmxdemod_ddemod_configure_psk_format.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-vi/raw/resource/enus/rfmxdemodvi/rfmxdemod_ddemod_configure_psk_format.html
- document_id: `rfmx-demod-vi`
- page_type: `leaf`
- content_type: ``

RFmxDemod DDemod Configure PSK Format (VI)

RFmxDemod DDemod Configure PSK Format (VI)

Owning Palette:

DDemod

Configures the PSK format.

[IMAGE alt='RFmxDemod DDemod Configure PSK Format' src='rfmxdemod_ddemod_configure_psk_format.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | PSK Format specifies the PSK format. The default value is Normal. Normal (0) Sets the modulation type to PSK. Offset QPSK (1) Sets the modulation type to offset quadrature PSK (OQPSK). The ideal symbol timing of Q is offset by half of a symbol period from the ideal symbol timing of I. PI/4 - QPSK (2) Sets the modulation type to pi/4 QPSK. In this modulation, each QPSK symbol is rotated by pi/4. PI/8 - 8PSK (3) Sets the modulation type to pi/8 8PSK. In this modulation, each 8PSK symbol is rotated by pi/8. 3*PI/8 - 8PSK (4) Sets the modulation type to 3*pi/8-8 PSK. In this modulation, each 8 PSK symbol is rotated by 3*pi/8. |
| Normal (0) | Sets the modulation type to PSK. |
| Offset QPSK (1) | Sets the modulation type to offset quadrature PSK (OQPSK). The ideal symbol timing of Q is offset by half of a symbol period from the ideal symbol timing of I. |
| PI/4 - QPSK (2) | Sets the modulation type to pi/4 QPSK. In this modulation, each QPSK symbol is rotated by pi/4. |
| PI/8 - 8PSK (3) | Sets the modulation type to pi/8 8PSK. In this modulation, each 8PSK symbol is rotated by pi/8. |
| 3*PI/8 - 8PSK (4) | Sets the modulation type to 3*pi/8-8 PSK. In this modulation, each 8 PSK symbol is rotated by 3*pi/8. |
|  | Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxDemod Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-demod-vi path=rfmxdemodvi/rfmxdemod_ddemod_configure_pulse_shaping_filter.html language=enus -->
## TOPIC 00043: rfmxdemodvi/rfmxdemod_ddemod_configure_pulse_shaping_filter.html

- bundle_id: `rfmx-demod-vi`
- source_path: `rfmxdemodvi/rfmxdemod_ddemod_configure_pulse_shaping_filter.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-vi/raw/resource/enus/rfmxdemodvi/rfmxdemod_ddemod_configure_pulse_shaping_filter.html
- document_id: `rfmx-demod-vi`
- page_type: `leaf`
- content_type: ``

RFmxDemod DDemod Configure Pulse Shaping Filter (VI)

RFmxDemod DDemod Configure Pulse Shaping Filter (VI)

Owning Palette:

DDemod

Configures the pulse-shaping filter.

[IMAGE alt='RFmxDemod DDemod Configure Pulse Shaping Filter' src='rfmxdemod_ddemod_configure_pulse_shaping_filter.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Pulse Shaping Filter Type specifies the pulse-shaping filter used to transmit the signal and determines the measurement filter to be used for analysis when the Measurement Filter property is set to Auto. Rectangular (0) The transmitted waveform is filtered using a rectangular filter. Raised Cosine (1) The transmitted waveform is filtered using a raised cosine filter. Specify the filter Alpha in the DDemod Pulse Shaping Filter Parameter property. Root Raised Cosine (2) The transmitted waveform is filtered using a root raised cosine filter. Specify the filter Alpha in the DDemod Pulse Shaping Filter Parameter property. Gaussian (3) The transmitted waveform is filtered using a Gaussian filter. Specify the filter bandwidth * sample duration in the DDemod Pulse Shaping Filter Parameter property. This filter is applicable only to FSK and MSK modulation types. Custom (4) The transmitted waveform is filtered using the coefficients that you specify in the RFmxDemod DDemod Configure Pulse Shaping Filter Custom Coefficients VI. Half Sine (5) The transmitted waveform is filtered using a half sine filter. Linearised GMSK - EDGE (6) The transmitted waveform is filtered using an EDGE-specific linearized GMSK filter. |
| Rectangular (0) | The transmitted waveform is filtered using a rectangular filter. |
| Raised Cosine (1) | The transmitted waveform is filtered using a raised cosine filter. Specify the filter Alpha in the DDemod Pulse Shaping Filter Parameter property. |
| Root Raised Cosine (2) | The transmitted waveform is filtered using a root raised cosine filter. Specify the filter Alpha in the DDemod Pulse Shaping Filter Parameter property. |
| Gaussian (3) | The transmitted waveform is filtered using a Gaussian filter. Specify the filter bandwidth * sample duration in the DDemod Pulse Shaping Filter Parameter property. This filter is applicable only to FSK and MSK modulation types. |
| Custom (4) | The transmitted waveform is filtered using the coefficients that you specify in the RFmxDemod DDemod Configure Pulse Shaping Filter Custom Coefficients VI. |
| Half Sine (5) | The transmitted waveform is filtered using a half sine filter. |
| Linearised GMSK - EDGE (6) | The transmitted waveform is filtered using an EDGE-specific linearized GMSK filter. |
|  | Pulse Shaping Filter Parameter specifies the rolloff factor for the raised cosine and root-raised cosine filters that are used as pulse shaping filter, and measurement filter respectively. When pulse-shaping filter type is Gaussian, this property specifies bandwidth * sample duration (BT). |
|  | Pulse Shaping Filter Custom Coefficients specifies the pulse-shaping filter custom coefficients. Note To configure an impulse, set x0=0, dx=1, y[0]=1. x0 always pass 0 to this parameter. Any other values are ignored. dx specifies the spacing between the coefficients as a fraction of the symbol spacing. For example, if four coefficients correspond to one symbol, the spacing is 1/4. y specifies the filter coefficients used as the pulse shaping filter on the transmitter. |
|  | Note To configure an impulse, set x0=0, dx=1, y[0]=1. |
|  | x0 always pass 0 to this parameter. Any other values are ignored. |
|  | dx specifies the spacing between the coefficients as a fraction of the symbol spacing. For example, if four coefficients correspond to one symbol, the spacing is 1/4. |
|  | y specifies the filter coefficients used as the pulse shaping filter on the transmitter. |
|  | Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxDemod Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-demod-vi path=rfmxdemodvi/rfmxdemod_ddemod_configure_pulse_shaping_filter_custom_coefficients.html language=enus -->
## TOPIC 00044: rfmxdemodvi/rfmxdemod_ddemod_configure_pulse_shaping_filter_custom_coefficients.html

- bundle_id: `rfmx-demod-vi`
- source_path: `rfmxdemodvi/rfmxdemod_ddemod_configure_pulse_shaping_filter_custom_coefficients.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-vi/raw/resource/enus/rfmxdemodvi/rfmxdemod_ddemod_configure_pulse_shaping_filter_custom_coefficients.html
- document_id: `rfmx-demod-vi`
- page_type: `leaf`
- content_type: ``

RFmxDemod DDemod Configure Pulse Shaping Filter Custom Coefficients (VI)

RFmxDemod DDemod Configure Pulse Shaping Filter Custom Coefficients (VI)

Owning Palette:

DDemod

Configures the pulse-shaping filter coefficients.

[IMAGE alt='RFmxDemod DDemod Configure Pulse Shaping Filter Custom Coefficients' src='rfmxdemod_ddemod_configure_pulse_shaping_filter_custom_coefficients.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Pulse Shaping Filter Custom Coefficients specifies the pulse-shaping filter custom coefficients. Note To configure an impulse, set x0=0, dx=1, y[0]=1. x0 always pass 0 to this parameter. Any other values are ignored. dx specifies the spacing between the coefficients as a fraction of the symbol spacing. For example, if four coefficients correspond to one symbol, the spacing is 1/4. y specifies the filter coefficients used as the pulse shaping filter on the transmitter. |
|  | Note To configure an impulse, set x0=0, dx=1, y[0]=1. |
|  | x0 always pass 0 to this parameter. Any other values are ignored. |
|  | dx specifies the spacing between the coefficients as a fraction of the symbol spacing. For example, if four coefficients correspond to one symbol, the spacing is 1/4. |
|  | y specifies the filter coefficients used as the pulse shaping filter on the transmitter. |
|  | Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxDemod Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-demod-vi path=rfmxdemodvi/rfmxdemod_ddemod_configure_samples_per_symbol.html language=enus -->
## TOPIC 00045: rfmxdemodvi/rfmxdemod_ddemod_configure_samples_per_symbol.html

- bundle_id: `rfmx-demod-vi`
- source_path: `rfmxdemodvi/rfmxdemod_ddemod_configure_samples_per_symbol.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-vi/raw/resource/enus/rfmxdemodvi/rfmxdemod_ddemod_configure_samples_per_symbol.html
- document_id: `rfmx-demod-vi`
- page_type: `leaf`
- content_type: ``

RFmxDemod DDemod Configure Samples Per Symbol (VI)

RFmxDemod DDemod Configure Samples Per Symbol (VI)

Owning Palette:

DDemod

Configures the samples per symbol to be used to acquire the signal for the measurement.

[IMAGE alt='RFmxDemod DDemod Configure Samples Per Symbol' src='rfmxdemod_ddemod_configure_samples_per_symbol.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Samples Per Symbol specifies the samples per symbol used to acquire the signal for the measurement. Auto (-1) The measurement uses appropriate samples per symbol (SPS) based on modulation type and pulse shaping filter. SPS=8, for FSK. SPS=4, for ASK,PSK, QAM, MSK when pulse shape filter is not rectangular. SPS=8, for ASK, PSK, QAM, MSK when pulse shape filter is rectangular. 4 (4) The samples per symbol value is 4. 8 (8) The samples per symbol value is 8. 16 (16) The samples per symbol value is 16. |
| Auto (-1) | The measurement uses appropriate samples per symbol (SPS) based on modulation type and pulse shaping filter. SPS=8, for FSK. SPS=4, for ASK,PSK, QAM, MSK when pulse shape filter is not rectangular. SPS=8, for ASK, PSK, QAM, MSK when pulse shape filter is rectangular. |
| 4 (4) | The samples per symbol value is 4. |
| 8 (8) | The samples per symbol value is 8. |
| 16 (16) | The samples per symbol value is 16. |
|  | Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxDemod Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-demod-vi path=rfmxdemodvi/rfmxdemod_ddemod_configure_signal_structure.html language=enus -->
## TOPIC 00046: rfmxdemodvi/rfmxdemod_ddemod_configure_signal_structure.html

- bundle_id: `rfmx-demod-vi`
- source_path: `rfmxdemodvi/rfmxdemod_ddemod_configure_signal_structure.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-vi/raw/resource/enus/rfmxdemodvi/rfmxdemod_ddemod_configure_signal_structure.html
- document_id: `rfmx-demod-vi`
- page_type: `leaf`
- content_type: ``

RFmxDemod DDemod Configure Signal Structure (VI)

RFmxDemod DDemod Configure Signal Structure (VI)

Configures the structure of the incoming signal to be either a continuous signal or a bursty signal.

[IMAGE alt='RFmxDemod DDemod Configure Signal Structure' src='rfmxdemod_ddemod_configure_signal_structure.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Signal Structure specifies whether the signal is either a bursty signal or a continuous signal. The default value is Continuous. Bursted (0) The signal is a bursty signal. Continuous (1) The signal is a continuous signal. |
| Bursted (0) | The signal is a bursty signal. |
| Continuous (1) | The signal is a continuous signal. |
|  | Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxDemod Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-demod-vi path=rfmxdemodvi/rfmxdemod_ddemod_configure_spectrum_inverted.html language=enus -->
## TOPIC 00047: rfmxdemodvi/rfmxdemod_ddemod_configure_spectrum_inverted.html

- bundle_id: `rfmx-demod-vi`
- source_path: `rfmxdemodvi/rfmxdemod_ddemod_configure_spectrum_inverted.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-vi/raw/resource/enus/rfmxdemodvi/rfmxdemod_ddemod_configure_spectrum_inverted.html
- document_id: `rfmx-demod-vi`
- page_type: `leaf`
- content_type: ``

RFmxDemod DDemod Configure Spectrum Inverted (VI)

RFmxDemod DDemod Configure Spectrum Inverted (VI)

Owning Palette:

DDemod

Configures swapping of I and Q channels in the acquired waveform before demodulation.

[IMAGE alt='RFmxDemod DDemod Configure Spectrum Inverted' src='rfmxdemod_ddemod_configure_spectrum_inverted.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Spectrum Inverted specifies whether to swap the acquired I and Q samples for demodulation. The default value is False. False (0) The acquired I and Q samples are used for demodulation as is. True (1) The acquired I and Q samples are swapped before using the signal for demodulation. |
| False (0) | The acquired I and Q samples are used for demodulation as is. |
| True (1) | The acquired I and Q samples are swapped before using the signal for demodulation. |
|  | Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxDemod Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-demod-vi path=rfmxdemodvi/rfmxdemod_ddemod_configure_symbol_map.html language=enus -->
## TOPIC 00048: rfmxdemodvi/rfmxdemod_ddemod_configure_symbol_map.html

- bundle_id: `rfmx-demod-vi`
- source_path: `rfmxdemodvi/rfmxdemod_ddemod_configure_symbol_map.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-vi/raw/resource/enus/rfmxdemodvi/rfmxdemod_ddemod_configure_symbol_map.html
- document_id: `rfmx-demod-vi`
- page_type: `leaf`
- content_type: ``

RFmxDemod DDemod Configure Symbol Map (VI)

RFmxDemod DDemod Configure Symbol Map (VI)

Owning Palette:

DDemod

Configures the symbol map that you use during measurements.

[IMAGE alt='RFmxDemod DDemod Configure Symbol Map' src='rfmxdemod_ddemod_configure_symbol_map.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Symbol Map Type specifies whether the measurement uses the default symbol map or the map that you configure using the RFmxDemod DDemod Configure Symbol Map VI. Auto (0) Uses a default symbol map. Custom (1) Uses the map that you specify. |
| Auto (0) | Uses a default symbol map. |
| Custom (1) | Uses the map that you specify. |
|  | Symbol Map specifies the custom symbol map. |
|  | Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxDemod Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-demod-vi path=rfmxdemodvi/rfmxdemod_ddemod_configure_symbol_rate.html language=enus -->
## TOPIC 00049: rfmxdemodvi/rfmxdemod_ddemod_configure_symbol_rate.html

- bundle_id: `rfmx-demod-vi`
- source_path: `rfmxdemodvi/rfmxdemod_ddemod_configure_symbol_rate.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-vi/raw/resource/enus/rfmxdemodvi/rfmxdemod_ddemod_configure_symbol_rate.html
- document_id: `rfmx-demod-vi`
- page_type: `leaf`
- content_type: ``

RFmxDemod DDemod Configure Symbol Rate (VI)

RFmxDemod DDemod Configure Symbol Rate (VI)

Owning Palette:

DDemod

Configures the symbol rate for digital demodulation measurements.

[IMAGE alt='RFmxDemod DDemod Configure Symbol Rate' src='rfmxdemod_ddemod_configure_symbol_rate.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Symbol Rate specifies the symbol rate in Hz. The default value is 100 kHz. |
|  | Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxDemod Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-demod-vi path=rfmxdemodvi/rfmxdemod_ddemod_configure_synchronization.html language=enus -->
## TOPIC 00050: rfmxdemodvi/rfmxdemod_ddemod_configure_synchronization.html

- bundle_id: `rfmx-demod-vi`
- source_path: `rfmxdemodvi/rfmxdemod_ddemod_configure_synchronization.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-vi/raw/resource/enus/rfmxdemodvi/rfmxdemod_ddemod_configure_synchronization.html
- document_id: `rfmx-demod-vi`
- page_type: `leaf`
- content_type: ``

RFmxDemod DDemod Configure Synchronization (VI)

RFmxDemod DDemod Configure Synchronization (VI)

Owning Palette:

DDemod

Configures bit pattern synchronization.

[IMAGE alt='RFmxDemod DDemod Configure Synchronization' src='rfmxdemod_ddemod_configure_synchronization.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Synchronization Enabled specifies whether the demodulator needs to search and synchronize the signal to a known reference sequence. The reference sequence is the symbol representation of a defined set of bits known to be present in the transmitted signal. If the synchronization is found in the demodulated signal, the measurement is performed from this point onward. If the synchronization is not found, the entire signal is used for the measurement. False (0) Does not search and synchronize the signal. True (1) Searches and synchronizes the signal. |
| False (0) | Does not search and synchronize the signal. |
| True (1) | Searches and synchronizes the signal. |
|  | Synchronization Bits specifies the synchronization bits used to create the reference sequence that needs to be searched in the demodulated signal. |
|  | Measurement Offset specifies the offset, which is the location from which the signal is considered for further measurements. |
|  | Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxDemod Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-demod-vi path=rfmxdemodvi/rfmxdemod_ddemod_fetch.html language=enus -->
## TOPIC 00051: rfmxdemodvi/rfmxdemod_ddemod_fetch.html

- bundle_id: `rfmx-demod-vi`
- source_path: `rfmxdemodvi/rfmxdemod_ddemod_fetch.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-vi/raw/resource/enus/rfmxdemodvi/rfmxdemod_ddemod_fetch.html
- document_id: `rfmx-demod-vi`
- page_type: `leaf`
- content_type: ``

RFmxDemod DDemod Fetch (VI)

RFmxDemod DDemod Fetch (VI)

Owning Palette:

Fetch

Fetches the digital demodulation measurements.

#### RFmxDemod DDemod Fetch Carrier Measurement

Fetches the carrier measurement.

[IMAGE alt='RFmxDemod DDemod Fetch Carrier Measurement' src='rfmxdemod_ddemod_fetch_carrier_measurement.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. This value is expressed in seconds. |
|  | Selector String comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxDemod Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Mean Frequency Offset returns the mean of the measured carrier frequency offset, in Hz. |
|  | Mean Frequency Drift returns the mean of the measured carrier frequency drift, in Hz. |
|  | Mean Phase Error returns the mean of the measured phase offset, in degrees, from the transmitted carrier phase. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxDemod DDemod Fetch EVM

Fetches the EVM measurements.

[IMAGE alt='RFmxDemod DDemod Fetch EVM' src='rfmxdemod_ddemod_fetch_evm.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. This value is expressed in seconds. |
|  | Selector String comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxDemod Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Mean RMS EVM returns the mean of the RMS EVM, as a percentage, measured per acquisition. |
|  | Maximum RMS EVM returns the maximum of the RMS EVM, as a percentage, measured per acquisition. |
|  | Mean Modulation Error Ratio returns the modulation error ratio, in dB. |
|  | Mean Peak EVM returns the mean of the peak EVM measured per acquisition. |
|  | Maximum Peak EVM returns the maximum of the peak EVM measured per acquisition. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxDemod DDemod Fetch Offset EVM

Fetches the offset error vector magnitude (EVM).

[IMAGE alt='RFmxDemod DDemod Fetch Offset EVM' src='rfmxdemod_ddemod_fetch_offset_evm.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. This value is expressed in seconds. |
|  | Selector String comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxDemod Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Mean RMS Offset EVM returns the mean of the RMS EVM, measured per acquisition, after removing the offset between the I and Q channels of OQPSK demodulated signal. |
|  | Maximum RMS Offset EVM returns the maximum of the RMS EVM, measured per acquisition, after removing the offset between the I and Q channels of OQPSK demodulated signal. |
|  | Mean Peak Offset EVM returns the mean of the peak EVM, measured per acquisition, after removing the offset between the I and Q channels of OQPSK demodulated signal. |
|  | Maximum Peak Offset EVM returns the maximum of the peak EVM, measured per acquisition, after removing the offset between the I and Q channels of OQPSK demodulated signal. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxDemod DDemod Fetch Magnitude Error

Fetches the magnitude error measurements.

[IMAGE alt='RFmxDemod DDemod Fetch Magnitude Error' src='rfmxdemod_ddemod_fetch_magnitude_error.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. This value is expressed in seconds. |
|  | Selector String comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxDemod Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Mean Magnitude Error returns the mean of the magnitude error measured per acquisition. |
|  | Maximum Magnitude Error returns the maximum of the magnitude error measured per acquisition. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxDemod DDemod Fetch Phase Error

Fetches the phase error measurements.

[IMAGE alt='RFmxDemod DDemod Fetch Phase Error' src='rfmxdemod_ddemod_fetch_phase_error.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. This value is expressed in seconds. |
|  | Selector String comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxDemod Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Mean Phase Error returns the mean of the phase error. |
|  | Maximum Phase Error returns the maximum of the phase error. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxDemod DDemod Fetch FSK Results

Fetches frequency-shift keying (FSK) results.

[IMAGE alt='RFmxDemod DDemod Fetch FSK Results' src='rfmxdemod_ddemod_fetch_fsk_results.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. This value is expressed in seconds. |
|  | Selector String comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxDemod Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Mean FSK Deviation returns the measured FSK deviation, in Hz. |
|  | Mean RMS FSK Error returns the mean of the RMS frequency error, in Hz, of the FSK symbols measured per acquisition. |
|  | Maximum Peak FSK Error returns the maximum of peak frequency error of the FSK symbols measured per acquisition. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxDemod DDemod Fetch Sync Found

Indicates whether synchronization bits were found in the demodulated symbol.

[IMAGE alt='RFmxDemod DDemod Fetch Sync Found' src='rfmxdemod_ddemod_fetch_sync_found.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. This value is expressed in seconds. |
|  | Selector String comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxDemod Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Sync Found? returns TRUE if the synchronization bits was found in the demodulated signal. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxDemod DDemod Fetch IQ Impairments

Fetches I/Q impairments.

[IMAGE alt='RFmxDemod DDemod Fetch IQ Impairments' src='rfmxdemod_ddemod_fetch_iq_impairments.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. This value is expressed in seconds. |
|  | Selector String comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxDemod Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Mean IQ Gain Imbalance returns the measured ratio of I gain to Q gain, in dB. |
|  | Mean Quadrature Skew returns a measure of I and Q components in the signal that are not perfectly orthogonal. |
|  | Mean IQ Origin Offset returns the offset, in dB, from the ideal location of the constellation origin. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxDemod DDemod Fetch Mean Amplitude Droop

Fetches the mean amplitude droop per symbol.

[IMAGE alt='RFmxDemod DDemod Fetch Mean Amplitude Droop' src='rfmxdemod_ddemod_fetch_mean_amplitude_droop.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. This value is expressed in seconds. |
|  | Selector String comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxDemod Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Mean Amplitude Droop returns the mean amplitude droop per symbol. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxDemod DDemod Fetch Mean IQ Origin Offset

Fetches the offset, in dB, from the ideal location of the constellation origin.

[IMAGE alt='RFmxDemod DDemod Fetch Mean IQ Origin Offset' src='rfmxdemod_ddemod_fetch_mean_iq_origin_offset.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. This value is expressed in seconds. |
|  | Selector String comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxDemod Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Mean IQ Origin Offset returns the offset, in dB, from the ideal location of the constellation origin. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxDemod DDemod Fetch Mean Quadrature Skew

Fetches the mean quadrature skew.

[IMAGE alt='RFmxDemod DDemod Fetch Mean Quadrature Skew' src='rfmxdemod_ddemod_fetch_mean_quadrature_skew.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. This value is expressed in seconds. |
|  | Selector String comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxDemod Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Mean Quadrature Skew returns a measure of I and Q components in the signal that are not perfectly orthogonal. Quadrature error can be either positive or negative, with the sign indicating the orientation of the error. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxDemod DDemod Fetch Mean Rho Factor

Fetches the correlation of the measurement waveform and the reference waveform.

[IMAGE alt='RFmxDemod DDemod Fetch Mean Rho Factor' src='rfmxdemod_ddemod_fetch_mean_rho_factor.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. This value is expressed in seconds. |
|  | Selector String comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxDemod Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Mean Rho Factor returns the correlation of the measurement waveform and the reference waveform. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxDemod DDemod Fetch EVM Trace

Fetches the EVM trace.

[IMAGE alt='RFmxDemod DDemod Fetch EVM Trace' src='rfmxdemod_ddemod_fetch_evm_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. This value is expressed in seconds. |
|  | Selector String comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxDemod Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | EVM returns the EVM measured per symbol. x0 returns the start symbol index. dx returns the spacing between symbols normalized to symbol rate. y returns the offset EVM per symbol. |
|  | x0 returns the start symbol index. |
|  | dx returns the spacing between symbols normalized to symbol rate. |
|  | y returns the offset EVM per symbol. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxDemod DDemod Fetch Offset EVM Trace

Fetches the offset error vector magnitude (EVM) trace measured on OQPSK signal.

[IMAGE alt='RFmxDemod DDemod Fetch Offset EVM Trace' src='rfmxdemod_ddemod_fetch_offset_evm_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. This value is expressed in seconds. |
|  | Selector String comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxDemod Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Offset EVM returns the offset EVM trace. x0 returns the start symbol index. dx returns the spacing between symbols normalized to symbol rate. y returns the offset EVM per symbol. |
|  | x0 returns the start symbol index. |
|  | dx returns the spacing between symbols normalized to symbol rate. |
|  | y returns the offset EVM per symbol. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxDemod DDemod Fetch Magnitude Error Trace

Fetches the magnitude error trace.

[IMAGE alt='RFmxDemod DDemod Fetch Magnitude Error Trace' src='rfmxdemod_ddemod_fetch_magnitude_error_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. This value is expressed in seconds. |
|  | Selector String comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxDemod Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Magnitude Error returns the magnitude error. x0 returns the start symbol index. dx returns the spacing between symbols normalized to symbol rate. y returns the magnitude error per symbol. |
|  | x0 returns the start symbol index. |
|  | dx returns the spacing between symbols normalized to symbol rate. |
|  | y returns the magnitude error per symbol. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxDemod DDemod Fetch Phase Error Trace

Fetches the phase error trace.

[IMAGE alt='RFmxDemod DDemod Fetch Phase Error Trace' src='rfmxdemod_ddemod_fetch_phase_error_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. This value is expressed in seconds. |
|  | Selector String comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxDemod Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Phase Error returns the phase error. x0 returns the start symbol index. dx returns the spacing between symbols normalized to symbol rate. y returns the phase error per symbol. |
|  | x0 returns the start symbol index. |
|  | dx returns the spacing between symbols normalized to symbol rate. |
|  | y returns the phase error per symbol. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxDemod DDemod Fetch FSK Deviation Trace

Fetches the frequency-shift keying (FSK) deviation trace.

[IMAGE alt='RFmxDemod DDemod Fetch FSK Deviation Trace' src='rfmxdemod_ddemod_fetch_fsk_deviation_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. This value is expressed in seconds. |
|  | Selector String comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxDemod Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | FSK Error returns the mean of the RMS frequency error of the FSK symbols measured per acquisition. x0 returns the start symbol index. dx returns the spacing between symbols normalized to symbol rate. y returns the FSK deviation error per symbol. |
|  | x0 returns the start symbol index. |
|  | dx returns the spacing between symbols normalized to symbol rate. |
|  | y returns the FSK deviation error per symbol. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxDemod DDemod Fetch Constellation Trace

Fetches the constellation trace.

[IMAGE alt='RFmxDemod DDemod Fetch Constellation Trace' src='rfmxdemod_ddemod_fetch_constellation_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. This value is expressed in seconds. |
|  | Selector String comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxDemod Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Constellation Trace returns the constellation trace. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxDemod DDemod Fetch Offset Constellation Trace

Fetches the offset constellation trace.

[IMAGE alt='RFmxDemod DDemod Fetch Offset Constellation Trace' src='rfmxdemod_ddemod_fetch_offset_constellation_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. This value is expressed in seconds. |
|  | Selector String comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxDemod Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Offset Constellation Trace returns the offset constellation trace. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxDemod DDemod Fetch Measurement Waveform

Fetches the measurement waveform.

[IMAGE alt='RFmxDemod DDemod Fetch Measurement Waveform' src='rfmxdemod_ddemod_fetch_measurement_waveform.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. This value is expressed in seconds. |
|  | Selector String comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxDemod Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Measurement Waveform returns the demodulated waveform used for measurement. x0 returns the start sample index. dx returns the spacing between samples normalized to samples per symbol. y returns the measured samples. |
|  | x0 returns the start sample index. |
|  | dx returns the spacing between samples normalized to samples per symbol. |
|  | y returns the measured samples. |
|  | Samples Per Symbol returns the samples per symbol. |
|  | Symbol Rate returns the symbol rate in Hz. The default value is 100 kHz. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxDemod DDemod Fetch Reference Waveform

Fetches the reference waveform.

[IMAGE alt='RFmxDemod DDemod Fetch Reference Waveform' src='rfmxdemod_ddemod_fetch_reference_waveform.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. This value is expressed in seconds. |
|  | Selector String comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxDemod Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Reference Waveform returns the reference waveform. x0 returns the start sample index. dx returns the spacing between samples normalized to samples per symbol. y returns the reference samples. |
|  | x0 returns the start sample index. |
|  | dx returns the spacing between samples normalized to samples per symbol. |
|  | y returns the reference samples. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxDemod DDemod Fetch Demodulated Bits

Fetches the demodulated bit stream.

[IMAGE alt='RFmxDemod DDemod Fetch Demodulated Bits' src='rfmxdemod_ddemod_fetch_demodulated_bits.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. This value is expressed in seconds. |
|  | Selector String comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxDemod Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Demodulated Bits returns the demodulated bit stream. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxDemod DDemod Fetch Equalizer Coefficients

Fetches the updated equalizer coefficients.

[IMAGE alt='RFmxDemod DDemod Fetch Equalizer Coefficients' src='rfmxdemod_ddemod_fetch_equalizer_coefficients.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. This value is expressed in seconds. |
|  | Selector String comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxDemod Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Equalizer Coefficients returns the updated coefficients. x0 this parameter always returns 0. dx returns the spacing between the coefficients as a fraction of the symbol spacing. For example, if four coefficients correspond to one symbol, the spacing is 1/4. y returns the updated equalizer coefficients. |
|  | x0 this parameter always returns 0. |
|  | dx returns the spacing between the coefficients as a fraction of the symbol spacing. For example, if four coefficients correspond to one symbol, the spacing is 1/4. |
|  | y returns the updated equalizer coefficients. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-demod-vi path=rfmxdemodvi/rfmxdemod_ddemod_get_equalizer_initial_coefficients.html language=enus -->
## TOPIC 00052: rfmxdemodvi/rfmxdemod_ddemod_get_equalizer_initial_coefficients.html

- bundle_id: `rfmx-demod-vi`
- source_path: `rfmxdemodvi/rfmxdemod_ddemod_get_equalizer_initial_coefficients.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-vi/raw/resource/enus/rfmxdemodvi/rfmxdemod_ddemod_get_equalizer_initial_coefficients.html
- document_id: `rfmx-demod-vi`
- page_type: `leaf`
- content_type: ``

RFmxDemod DDemod Get Equalizer Initial Coefficients (VI)

RFmxDemod DDemod Get Equalizer Initial Coefficients (VI)

Owning Palette:

Utility

Gets the initial equalizer coefficients used by the digital demodulation measurement.

[IMAGE alt='RFmxDemod DDemod Get Equalizer Initial Coefficients' src='rfmxdemod_ddemod_get_equalizer_initial_coefficients.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxDemod Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Equalizer Initial Coefficients returns the equalizer initial coefficients. x0 this parameter always returns 0. dx returns the spacing between the coefficients as a fraction of the symbol spacing. For example, if four coefficients correspond to one symbol, the spacing is 1/4. y returns the filter coefficients used as the equalizer initial coefficients. |
|  | x0 this parameter always returns 0. |
|  | dx returns the spacing between the coefficients as a fraction of the symbol spacing. For example, if four coefficients correspond to one symbol, the spacing is 1/4. |
|  | y returns the filter coefficients used as the equalizer initial coefficients. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-demod-vi path=rfmxdemodvi/rfmxdemod_ddemod_get_symbol_map.html language=enus -->
## TOPIC 00053: rfmxdemodvi/rfmxdemod_ddemod_get_symbol_map.html

- bundle_id: `rfmx-demod-vi`
- source_path: `rfmxdemodvi/rfmxdemod_ddemod_get_symbol_map.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-vi/raw/resource/enus/rfmxdemodvi/rfmxdemod_ddemod_get_symbol_map.html
- document_id: `rfmx-demod-vi`
- page_type: `leaf`
- content_type: ``

RFmxDemod DDemod Get Symbol Map (VI)

RFmxDemod DDemod Get Symbol Map (VI)

Owning Palette:

Utility

Gets the symbol map that is used for digital demodulation measurements. Call this VI after calling [RFmxDemod Commit](../rfmxdemodvi/rfmxdemod_commit.html) VI.

[IMAGE alt='RFmxDemod DDemod Get Symbol Map' src='rfmxdemod_ddemod_get_symbol_map.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxDemod Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Symbol Map returns the symbol map used for demodulation. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-demod-vi path=rfmxdemodvi/rfmxdemod_delete_signal_configuration.html language=enus -->
## TOPIC 00054: rfmxdemodvi/rfmxdemod_delete_signal_configuration.html

- bundle_id: `rfmx-demod-vi`
- source_path: `rfmxdemodvi/rfmxdemod_delete_signal_configuration.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-vi/raw/resource/enus/rfmxdemodvi/rfmxdemod_delete_signal_configuration.html
- document_id: `rfmx-demod-vi`
- page_type: `leaf`
- content_type: ``

RFmxDemod Delete Signal Configuration (VI)

RFmxDemod Delete Signal Configuration (VI)

Owning Palette:

Advanced

Deletes an instance of the signal that you specify in the **Signal Name** parameter.

[IMAGE alt='RFmxDemod Delete Signal Configuration' src='rfmxdemod_delete_signal_configuration.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Signal Name specifies the name of the signal. This parameter accepts the signal name with or without the "signal::" prefix. Example: "signal::sig1" "sig1" |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-demod-vi path=rfmxdemodvi/rfmxdemod_get_all_named_result_names.html language=enus -->
## TOPIC 00055: rfmxdemodvi/rfmxdemod_get_all_named_result_names.html

- bundle_id: `rfmx-demod-vi`
- source_path: `rfmxdemodvi/rfmxdemod_get_all_named_result_names.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-vi/raw/resource/enus/rfmxdemodvi/rfmxdemod_get_all_named_result_names.html
- document_id: `rfmx-demod-vi`
- page_type: `leaf`
- content_type: ``

RFmxDemod Get All Named Result Names (VI)

RFmxDemod Get All Named Result Names (VI)

Owning Palette:

Utility

Returns all the named result names of the signal that you specify in the Selector String parameter.

[IMAGE alt='RFmxDemod Get All Named Result Names' src='rfmxdemod_get_all_named_result_names.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxDemod Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Result Names returns an array of result names. |
|  | Default Result Exists? indicates whether the default result exists. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-demod-vi path=rfmxdemodvi/rfmxdemod_initiate.html language=enus -->
## TOPIC 00056: rfmxdemodvi/rfmxdemod_initiate.html

- bundle_id: `rfmx-demod-vi`
- source_path: `rfmxdemodvi/rfmxdemod_initiate.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-vi/raw/resource/enus/rfmxdemodvi/rfmxdemod_initiate.html
- document_id: `rfmx-demod-vi`
- page_type: `leaf`
- content_type: ``

RFmxDemod Initiate (VI)

RFmxDemod Initiate (VI)

Owning Palette:

RFmx Demod VIs

Initiates all enabled measurements. Call this VI after configuring the signal and measurement. This VI asynchronously launches measurements in the background and immediately returns to the caller program. You can fetch measurement results using the Fetch VIs or result properties in the property node. To get the status of measurements, you can use the [RFmxDemod Wait for Measurement Complete](../rfmxdemodvi/rfmxdemod_wait_for_measurement_complete.html) VI or the [RFmxDemod Check Measurement Status](../rfmxdemodvi/rfmxdemod_check_measurement_status.html) VI.

[IMAGE alt='RFmxDemod Initiate' src='rfmxdemod_initiate.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Result Name specifies the name to be associated with measurement results. Provide a unique name, such as "r1" to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. The default value is "" (empty string) which refers to default result instance. Example: "result::r1" "r1" |
|  | Selector String specifies a selector string comprising of the signal name and result name. The result name can either be specified through this input or the Result Name parameter. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name in this input, either the result name specified by Result Name parameter or the default result instance is used. The default is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxDemod Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Selector String Out returns the selector string that can be passed to the Selector String parameter on Fetch VIs. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-demod-vi path=rfmxdemodvi/rfmxdemod_property_node.html language=enus -->
## TOPIC 00057: rfmxdemodvi/rfmxdemod_property_node.html

- bundle_id: `rfmx-demod-vi`
- source_path: `rfmxdemodvi/rfmxdemod_property_node.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-vi/raw/resource/enus/rfmxdemodvi/rfmxdemod_property_node.html
- document_id: `rfmx-demod-vi`
- page_type: `leaf`
- content_type: ``

RFmxDemod Property Node (VI)

RFmxDemod Property Node (VI)

Owning Palette:

RFmx Demod VIs

Sets (writes), gets (reads), or resets (sets to default value) RFmxDemod properties.

[IMAGE alt='RFmxDemod Property Node' src='rfmxdemod_property_node.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-demod-vi path=rfmxdemodvi/rfmxdemod_read.html language=enus -->
## TOPIC 00058: rfmxdemodvi/rfmxdemod_read.html

- bundle_id: `rfmx-demod-vi`
- source_path: `rfmxdemodvi/rfmxdemod_read.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-vi/raw/resource/enus/rfmxdemodvi/rfmxdemod_read.html
- document_id: `rfmx-demod-vi`
- page_type: `leaf`
- content_type: ``

RFmxDemod Read (VI)

RFmxDemod Read (VI)

Owning Palette:

RFmx Demod VIs

Configures hardware for acquisition, performs measurement on acquired data, and returns measurement results.

#### RFmxDemod ADemod Read AM

Configures hardware for acquisition, performs measurement on acquired data, and returns the AM measurement results.

[IMAGE alt='RFmxDemod ADemod Read AM' src='rfmxdemod_ademod_read_am.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. This value is expressed in seconds. |
|  | Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxDemod Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Mean Modulation Depth returns the mean amplitude variation, as a percentage, around the unmodulated carrier amplitude. If the carrier is suppressed, the amplitude variation of the modulating signal is returned. |
|  | Mean Carrier Power returns the mean of the measured carrier power, in dBm. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxDemod ADemod Read FM

Configures hardware for acquisition, performs measurement on acquired data, and returns the FM measurement results.

[IMAGE alt='RFmxDemod ADemod Read FM' src='rfmxdemod_ademod_read_fm.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. This value is expressed in seconds. |
|  | Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxDemod Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Mean Deviation returns the mean frequency deviation, in Hz, around the nominal frequency of the FM carrier. |
|  | Mean Carrier Frequency Error returns the mean of the measured carrier frequency error, in Hz. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxDemod ADemod Read PM

Configures hardware for acquisition, performs measurement on acquired data, and returns the PM measurement results.

[IMAGE alt='RFmxDemod ADemod Read PM' src='rfmxdemod_ademod_read_pm.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. This value is expressed in seconds. |
|  | Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxDemod Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Mean Deviation returns the mean phase deviation, in degrees, of a phase modulated signal. |
|  | Mean Carrier Frequency Error returns the mean of the measured carrier frequency error, in Hz. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxDemod DDemod Read

Configures hardware for acquisition, performs measurement on acquired data for modulation type configured using the [RFmxDemod DDemod Configure Modulation Type](../rfmxdemodvi/rfmxdemod_ddemod_configure_modulation_type.html) VI, and returns the frequency offset, EVM, and MER results.

[IMAGE alt='RFmxDemod DDemod Read' src='rfmxdemod_ddemod_read.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. This value is expressed in seconds. |
|  | Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxDemod Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Mean Frequency Offset returns the mean of the measured carrier frequency offset, in Hz. |
|  | Mean RMS EVM returns the mean of the RMS EVM measured per acquisition. |
|  | Maximum Peak EVM returns the maximum of the peak EVM measured per acquisition. |
|  | Mean Modulation Error Ratio returns the modulation error ratio, in dB. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-demod-vi path=rfmxdemodvi/rfmxdemod_reset_to_default.html language=enus -->
## TOPIC 00059: rfmxdemodvi/rfmxdemod_reset_to_default.html

- bundle_id: `rfmx-demod-vi`
- source_path: `rfmxdemodvi/rfmxdemod_reset_to_default.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-vi/raw/resource/enus/rfmxdemodvi/rfmxdemod_reset_to_default.html
- document_id: `rfmx-demod-vi`
- page_type: `leaf`
- content_type: ``

RFmxDemod Reset to Default (VI)

RFmxDemod Reset to Default (VI)

Owning Palette:

Utility

Resets a signal to the default values.

[IMAGE alt='RFmxDemod Reset to Default' src='rfmxdemod_reset_to_default.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxDemod Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-demod-vi path=rfmxdemodvi/rfmxdemod_select_measurement.html language=enus -->
## TOPIC 00060: rfmxdemodvi/rfmxdemod_select_measurement.html

- bundle_id: `rfmx-demod-vi`
- source_path: `rfmxdemodvi/rfmxdemod_select_measurement.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-vi/raw/resource/enus/rfmxdemodvi/rfmxdemod_select_measurement.html
- document_id: `rfmx-demod-vi`
- page_type: `leaf`
- content_type: ``

RFmxDemod Select Measurement (VI)

RFmxDemod Select Measurement (VI)

Owning Palette:

RFmx Demod VIs

Specifies the measurements that you want to enable. To select a single measurement, use the Single Measurement instance. To select multiple measurements, use the Multiple Measurements instance.

#### RFmxDemod Select Measurement (Single)

Enables the measurement that you specify in the **Measurement** parameter and disables all other measurements.

[IMAGE alt='RFmxDemod Select Measurement (Single)' src='rfmxdemod_select_measurement_(single).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Measurement specifies the measurement to perform. You can specify one of the following measurements. ADemod (0) Enables analog demodulation measurement. DDemod (1) Enables digital demodulation measurement. |
| ADemod (0) | Enables analog demodulation measurement. |
| DDemod (1) | Enables digital demodulation measurement. |
|  | Enable All Traces specifies whether to enable all the traces for the selected measurement. |
|  | Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxDemod Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxDemod Select Measurement (Multiple)

Enables all the measurements that you specify in the **Measurements** parameter and disables all other measurements.

[IMAGE alt='RFmxDemod Select Measurement (Multiple)' src='rfmxdemod_select_measurement_(multiple).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Measurements specifies an array of measurements to perform. You can specify the following measurements. ADemod (0) Enables analog demodulation measurements. DDemod (1) Enables digital demodulation measurements. |
| ADemod (0) | Enables analog demodulation measurements. |
| DDemod (1) | Enables digital demodulation measurements. |
|  | Enable All Traces specifies whether to enable all the traces for the selected measurements. |
|  | Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxDemod Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-demod-vi path=rfmxdemodvi/rfmxdemod_send_software_edge_trigger.html language=enus -->
## TOPIC 00061: rfmxdemodvi/rfmxdemod_send_software_edge_trigger.html

- bundle_id: `rfmx-demod-vi`
- source_path: `rfmxdemodvi/rfmxdemod_send_software_edge_trigger.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-vi/raw/resource/enus/rfmxdemodvi/rfmxdemod_send_software_edge_trigger.html
- document_id: `rfmx-demod-vi`
- page_type: `leaf`
- content_type: ``

RFmxDemod Send Software Edge Trigger (VI)

RFmxDemod Send Software Edge Trigger (VI)

Owning Palette:

Configuration

Sends a trigger to the device when you use the [RFmxDemod Configure Trigger](rfmxdemod_configure_trigger.html) VI to choose a software version of a trigger, and the device is waiting for the trigger to be sent. You can also use this VI to override a hardware trigger.

This VI returns an error in the following situations:

- You configure an invalid trigger.
- You have not previously called the RFmxDemod Initiate VI.

[IMAGE alt='RFmxDemod Send Software Edge Trigger' src='rfmxdemod_send_software_edge_trigger.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-demod-vi path=rfmxdemodvi/rfmxdemod_vi_tree.html language=enus -->
## TOPIC 00062: rfmxdemodvi/rfmxdemod_vi_tree.html

- bundle_id: `rfmx-demod-vi`
- source_path: `rfmxdemodvi/rfmxdemod_vi_tree.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-vi/raw/resource/enus/rfmxdemodvi/rfmxdemod_vi_tree.html
- document_id: `rfmx-demod-vi`
- page_type: `leaf`
- content_type: ``

RFmxDemod VI Tree (VI)

RFmxDemod VI Tree (VI)

Owning Palette:

RFmx Demod VIs

Displays all the VIs available in RFmxDemod for measurement configuration, control, and fetching results. The VIs are organized in the order they are supposed to be used in a program that you create.

[IMAGE alt='RFmxDemod VI Tree' src='rfmxdemod_vi_tree.gif']

<!--NI_TOPIC bundle=rfmx-demod-vi path=rfmxdemodvi/rfmxdemod_wait_for_measurement_complete.html language=enus -->
## TOPIC 00063: rfmxdemodvi/rfmxdemod_wait_for_measurement_complete.html

- bundle_id: `rfmx-demod-vi`
- source_path: `rfmxdemodvi/rfmxdemod_wait_for_measurement_complete.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-vi/raw/resource/enus/rfmxdemodvi/rfmxdemod_wait_for_measurement_complete.html
- document_id: `rfmx-demod-vi`
- page_type: `leaf`
- content_type: ``

RFmxDemod Wait for Measurement Complete (VI)

RFmxDemod Wait for Measurement Complete (VI)

Owning Palette:

Utility

Waits for the specified number for seconds for all the measurements to complete.

[IMAGE alt='RFmxDemod Wait for Measurement Complete' src='rfmxdemod_wait_for_measurement_complete.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. This value is expressed in seconds. |
|  | Selector String comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxDemod Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-demod-vi path=rfmxdemodvi/utility_pal.html language=enus -->
## TOPIC 00064: rfmxdemodvi/utility_pal.html

- bundle_id: `rfmx-demod-vi`
- source_path: `rfmxdemodvi/utility_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-vi/raw/resource/enus/rfmxdemodvi/utility_pal.html
- document_id: `rfmx-demod-vi`
- page_type: `leaf`
- content_type: ``

Utility

Utility

Owning Palette:

RFmx Demod VIs

Use the VIs on this palette to configure utility VIs.

| Palette Object | Description |
| --- | --- |
| RFmxDemod Commit | Commits settings to the hardware. Calling this VI is optional. RFmxDemod commits settings to the hardware when you call the RFmxDemod Initiate VI or any of the measurement Read VIs. |
| RFmxDemod Reset to Default | Resets a signal to the default values. |
| RFmxDemod Wait for Measurement Complete | Waits for the specified number for seconds for all the measurements to complete. |
| RFmxDemod Check Measurement Status | Checks the status of the measurement. Use this VI to check for any errors that may occur during measurement or to check whether the measurement is complete and results are available. |
| RFmxDemod DDemod Get Equalizer Initial Coefficients | Gets the initial equalizer coefficients used by the digital demodulation measurement. |
| RFmxDemod DDemod Get Symbol Map | Gets the symbol map that is used for digital demodulation measurements. Call this VI after calling RFmxDemod Commit VI. |
| RFmxDemod Get All Named Result Names | Returns all the named result names of the signal that you specify in the Selector String parameter. |
