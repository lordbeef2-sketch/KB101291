# NI DOCUMENT BUNDLE: rfmxdemod-labview-api-ref

<!--NI_BUNDLE_CHUNK bundle=rfmxdemod-labview-api-ref start=1 end=147 -->
<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=menus/categories/measurement/rfmx/demod/rfmx-demod-mx-advanced-mnu.html language=enus -->
## TOPIC 00001: Advanced

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `menus/categories/measurement/rfmx/demod/rfmx-demod-mx-advanced-mnu.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/menus/categories/measurement/rfmx/demod/rfmx-demod-mx-advanced-mnu.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the VIs on this palette to use advanced features. You can use the RFmxDemod Property Node to configure additional properties. icon

### Advanced

Use the VIs on this palette to use advanced features. You can use the RFmxDemod Property Node to configure additional properties.

[IMAGE alt='icon' src='rfmx-demod-mx-advanced-mnu.png']

- [RFmxDemod Abort Measurements VI](../../../../../vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-abort-measurements-vi.html) Stops acquisition as well as the measurements that are associated with the signal instance and that were previously initiated by the RFmxDemod Initiate VI or measurement read VIs.
- [RFmxDemod Analyze (IQ, 1 Wfm) VI](../../../../../vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-analyze-iq-1-wfm-vi.html) Performs the enabled measurements on the I/Q complex waveform that you specify in IQ parameter. Call this VI after you configure the signal and measurement properties. You can fetch measurement results using the Fetch VIs or result properties in the property node. Use this VI only if the Recommended Acquisition Type property value is IQ .
- [RFmxDemod Create Signal Configuration VI](../../../../../vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-create-signal-configuration-vi.html) Creates a new instance of a signal.
- [RFmxDemod Clone Signal Configuration VI](../../../../../vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-clone-signal-configuration-vi.html) Creates a new instance of a signal by copying all the property values from an existing signal instance.
- [RFmxDemod Delete Signal Configuration VI](../../../../../vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-delete-signal-configuration-vi.html) Deletes an instance of the signal that you specify in the Signal Name parameter.
- [RFmxDemod Get All Named Result Names VI](../../../../../vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-get-all-named-result-names-vi.html) Returns all the named result names of the signal that you specify in the Selector String parameter.
- [RFmxDemod Clear Named Result VI](../../../../../vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-clear-named-result-vi.html) Clears an instance of the result that you specify in the Selector String parameter.
- [RFmxDemod Clear All Named Results VI](../../../../../vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-clear-all-named-results-vi.html) Clears all results for the signal that you specify in the Selector String parameter.

Parent topic:

Demod

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=menus/categories/measurement/rfmx/demod/rfmx-demod-mx-build-string-mnu.html language=enus -->
## TOPIC 00002: Build String

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `menus/categories/measurement/rfmx/demod/rfmx-demod-mx-build-string-mnu.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/menus/categories/measurement/rfmx/demod/rfmx-demod-mx-build-string-mnu.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the VIs on this palette to create strings for configurations and results that require a selector string. icon

### Build String

Use the VIs on this palette to create strings for configurations and results that require a selector string.

[IMAGE alt='icon' src='rfmx-demod-mx-build-string-mnu.png']

- [RFmxDemod Build Signal String VI](../../../../../vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-build-signal-string-vi.html) Creates a selector string for use with Configuration or Fetch properties and VIs.

Parent topic:

Demod

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=menus/categories/measurement/rfmx/demod/utility/dir-mnu.html language=enus -->
## TOPIC 00003: Utility

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `menus/categories/measurement/rfmx/demod/utility/dir-mnu.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/menus/categories/measurement/rfmx/demod/utility/dir-mnu.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the VIs on this palette to configure utility VIs. icon

### Utility

Use the VIs on this palette to configure utility VIs.

[IMAGE alt='icon' src='dir-mnu.png']

- [RFmxDemod Commit VI](../../../../../../vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-commit-vi.html) Commits settings to the hardware. Calling this VI is optional. RFmxDemod commits settings to the hardware when you call the RFmxDemod Initiate VI or any of the measurement Read VIs.
- [RFmxDemod Reset to Default VI](../../../../../../vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-reset-to-default-vi.html) Resets a signal to the default values.
- [RFmxDemod Wait for Measurement Complete VI](../../../../../../vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-wait-for-measurement-complete-vi.html) Waits for the specified number for seconds for all the measurements to complete.
- [RFmxDemod Check Measurement Status VI](../../../../../../vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-check-measurement-status-vi.html) Checks the status of the measurement. Use this VI to check for any errors that may occur during measurement or to check whether the measurement is complete and results are available.
- [RFmxDemod DDemod Get Equalizer Initial Coefficients VI](../../../../../../vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-get-equalizer-initial-coefficients-vi.html) Gets the initial equalizer coefficients used by the digital demodulation measurement.
- [RFmxDemod DDemod Get Symbol Map VI](../../../../../../vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-get-symbol-map-vi.html) Gets the symbol map that is used for digital demodulation measurements. Call this VI after calling RFmxDemod Commit VI.

Parent topic:

Demod

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=resource/objmgr/rfmxdemod-rc/rfmxdemod-p.html language=enus -->
## TOPIC 00004: RFmxDemod Properties

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `resource/objmgr/rfmxdemod-rc/rfmxdemod-p.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxdemod-rc/rfmxdemod-p.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the RFmxDemod properties to access options for configuring and fetching measurements. © 2014–2026 National Instruments Corporation. All rights reserved.

### RFmxDemod Properties

Use the RFmxDemod properties to access options for configuring and fetching measurements.

© 2014–2026 National Instruments Corporation. All rights reserved.

- [Advanced:Auto Level Initial Reference Level (dBm)](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr20200d.html) Specifies the initial reference level which the RFmxDemod Auto Level VI uses to estimate the peak power of the input signal. This value is expressed in dBm.
- [Advanced:Limited Configuration Change](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr20200e.html) Specifies the set of properties that are considered by RFmx in the locked signal configuration state.
- [Analog Demod:AM Carrier Suppressed](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr200002.html) Specifies whether the carrier of the AM (amplitude modulated) signal is absent.
- [Analog Demod:All Traces Enabled](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr200013.html) Specifies whether to enable the traces to be stored and retrieved after performing the analog demodulation measurement.
- [Analog Demod:Audio Filter:Lower Cutoff Frequency (Hz)](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr200004.html) Specifies the lower cutoff frequency of the custom audio filter. This property is applicable only when you set the ADemod Audio Filter Type property to Custom . This value is expressed in Hz.
- [Analog Demod:Audio Filter:Type](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr200003.html) Specifies the audio filter to be applied on the analog demodulated signal.
- [Analog Demod:Audio Filter:Upper Cutoff Frequency (Hz)](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr200005.html) Specifies the upper cutoff frequency of the custom audio filter. This property is applicable only when you set the ADemod Audio Filter Type property to Custom . This value is expressed in Hz.
- [Analog Demod:Audio Measurement Enabled](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr200040.html) Specifies whether to enable the audio signal measurements, such as SINAD, SNR, THD and THD+Noise.
- [Analog Demod:Averaging:Count](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr200007.html) Specifies the number of acquisitions used for averaging when you set the ADemod Averaging Enabled property to True .
- [Analog Demod:Averaging:Enabled](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr200006.html) Specifies whether to enable averaging for the analog demodulation measurement.
- [Analog Demod:Averaging:Type](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr200009.html) Specifies the averaging type for the measurement.
- [Analog Demod:Carrier Correction:Frequency Enabled](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr20000a.html) Specifies whether to correct the frequency error in the carrier when demodulating frequency-modulated (FM) or phase-modulated (PM) signals.
- [Analog Demod:Carrier Correction:Phase Enabled](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr20000b.html) Specifies whether to correct the carrier phase error when demodulating phase-modulated signals.
- [Analog Demod:FM DeEmphasis (s)](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr20000c.html) Specifies the time constant of de-emphasis filter, which compensates for the pre-emphasis filter in the FM transmitter. This value is expressed in seconds.
- [Analog Demod:Measurement Enabled](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr200039.html) Specifies whether to enable analog demodulation measurements.
- [Analog Demod:Measurement Interval (s)](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr20000d.html) Specifies the signal acquisition time for the analog demodulation measurement. This value is expressed in seconds.
- [Analog Demod:Modulation Type](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr20000e.html) Specifies the analog modulation type of the signal that needs to be analyzed.
- [Analog Demod:RBW Filter:Alpha](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr200012.html) Specifies the roll-off factor of the root-raised cosine (RRC) filter.
- [Analog Demod:RBW Filter:Bandwidth (Hz)](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr200011.html) Specifies the bandwidth of the resolution bandwidth (RBW) filter to be applied to the acquired signal. This value is expressed in Hz.
- [Analog Demod:RBW Filter:Type](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr200010.html) Specifies the shape of the digital RBW filter.
- [Analog Demod:Results:AM Modulation Depth:Maximum Negative Peak (%)](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr200023.html) Returns the maximum negative peak amplitude of the modulating signal measured across multiple acquisitions, as a percentage.
- [Analog Demod:Results:AM Modulation Depth:Maximum Peak to Peak /2 (%)](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr200021.html) Returns the maximum (peak-to-peak)/2 amplitude of the modulating signal measured across multiple acquisitions, as a percentage.
- [Analog Demod:Results:AM Modulation Depth:Maximum Positive Peak (%)](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr200022.html) Returns the maximum positive peak amplitude of the modulating signal measured across multiple acquisitions, as a percentage.
- [Analog Demod:Results:AM Modulation Depth:Maximum RMS (%)](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr200024.html) Returns the maximum RMS amplitude of the modulating signal measured across multiple acquisitions, as a percentage.
- [Analog Demod:Results:AM Modulation Depth:Maximum Standard Deviation (%)](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr200020.html) Returns the maximum modulation depth measured across multiple acquisitions, as a percentage.
- [Analog Demod:Results:AM Modulation Depth:Mean Negative Peak (%)](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr20001e.html) Returns the mean negative peak amplitude of the modulating signal, as a percentage.
- [Analog Demod:Results:AM Modulation Depth:Mean Peak to Peak /2 (%)](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr20001c.html) Returns the mean (peak-to-peak)/2 amplitude of the modulating signal, as a percentage.
- [Analog Demod:Results:AM Modulation Depth:Mean Positive Peak (%)](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr20001d.html) Returns the mean positive peak amplitude of the modulating signal, as a percentage.
- [Analog Demod:Results:AM Modulation Depth:Mean RMS (%)](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr20001f.html) Returns the mean RMS amplitude of the modulating signal, as a percentage.
- [Analog Demod:Results:AM Modulation Depth:Mean Standard Deviation (%)](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr20001b.html) Returns the mean amplitude variation around the unmodulated carrier amplitude, as a percentage. If the carrier is suppressed, the amplitude variation of the modulating signal is returned.
- [Analog Demod:Results:Average SINAD (dB)](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr200017.html) Returns the averaged signal-to-noise and distortion ratio of the demodulated signal. This value is expressed in dB.
- [Analog Demod:Results:Average SNR (dB)](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr20001a.html) Returns the averaged signal-to-noise ratio of the demodulated signal. This value is expressed in dB.
- [Analog Demod:Results:Average THD (%)](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr200019.html) Returns the averaged total harmonic distortion of the demodulated signal, as a percentage.
- [Analog Demod:Results:Average THD with Noise (%)](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr200018.html) Returns the averaged total harmonic distortion with noise of the demodulated signal, as a percentage.
- [Analog Demod:Results:FM Deviation:Maximum Negative Peak (Hz)](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr20002d.html) Returns the maximum negative peak frequency deviation of the frequency-modulated signal measured across multiple acquisitions. This value is expressed in Hz.
- [Analog Demod:Results:FM Deviation:Maximum Peak to Peak /2 (Hz)](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr20002b.html) Returns the maximum (peak-to-peak)/2 frequency variation around the nominal frequency of the FM carrier measured across multiple acquisitions. This value is expressed in Hz.
- [Analog Demod:Results:FM Deviation:Maximum Positive Peak (Hz)](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr20002c.html) Returns the maximum positive peak frequency deviation of the frequency-modulated signal measured across multiple acquisitions. This value is expressed in Hz.
- [Analog Demod:Results:FM Deviation:Maximum RMS (Hz)](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr20002e.html) Returns the maximum RMS frequency deviation of the frequency-modulated signal measured across multiple acquisitions. This value is expressed in Hz.
- [Analog Demod:Results:FM Deviation:Maximum Standard Deviation (Hz)](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr20002a.html) Returns the maximum frequency deviation of the frequency-modulated signal measured across multiple acquisitions. This value is expressed in Hz.
- [Analog Demod:Results:FM Deviation:Mean Negative Peak (Hz)](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr200028.html) Returns the mean negative peak frequency deviation of the frequency-modulated signal. This value is expressed in Hz.
- [Analog Demod:Results:FM Deviation:Mean Peak to Peak /2 (Hz)](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr200026.html) Returns the mean (peak-to-peak)/2 frequency variation around the nominal frequency of the FM carrier. This value is expressed in Hz.
- [Analog Demod:Results:FM Deviation:Mean Positive Peak (Hz)](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr200027.html) Returns the mean positive peak frequency deviation of the frequency-modulated signal. This value is expressed in Hz.
- [Analog Demod:Results:FM Deviation:Mean RMS (Hz)](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr200029.html) Returns the mean RMS frequency deviation of the frequency-modulated signal. This value is expressed in Hz.
- [Analog Demod:Results:FM Deviation:Mean Standard Deviation (Hz)](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr200025.html) Returns the mean frequency deviation around the nominal frequency of the FM carrier. This value is expressed in Hz.
- [Analog Demod:Results:Mean Carrier Frequency Error (Hz)](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr200014.html) Returns the mean of the measured carrier frequency offset. This value is expressed in Hz.
- [Analog Demod:Results:Mean Carrier Power (dBm)](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr200015.html) Returns the mean of the measured carrier power. This value is expressed in dBm.
- [Analog Demod:Results:Mean Modulation Frequency (Hz)](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr200016.html) Returns the mean of the demodulated signal frequency. This value is expressed in Hz.
- [Analog Demod:Results:PM Deviation:Maximum Negative Peak (deg)](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr200037.html) Returns the maximum negative peak phase deviation around the unmodulated carrier phase, measured across multiple acquisitions. This value is expressed in degrees.
- [Analog Demod:Results:PM Deviation:Maximum Peak to Peak /2 (deg)](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr200035.html) Returns the maximum (peak-to-peak)/2 phase deviation around the unmodulated carrier phase, measured across multiple acquisitions. This value is expressed in degrees.
- [Analog Demod:Results:PM Deviation:Maximum Positive Peak (deg)](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr200036.html) Returns the maximum positive peak phase deviation around the unmodulated carrier phase, measured across multiple acquisitions. This value is expressed in degrees.
- [Analog Demod:Results:PM Deviation:Maximum RMS (deg)](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr200038.html) Returns the maximum RMS phase deviation of the phase-modulated signal measured across multiple acquisitions. This value is expressed in degrees.
- [Analog Demod:Results:PM Deviation:Maximum Standard Deviation (deg)](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr200034.html) Returns the maximum phase deviation around the unmodulated carrier phase, measured across multiple acquisitions. This value is expressed in degrees.
- [Analog Demod:Results:PM Deviation:Mean Negative Peak (deg)](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr200032.html) Returns the mean negative peak phase deviation around the unmodulated carrier phase. This value is expressed in degrees.
- [Analog Demod:Results:PM Deviation:Mean Peak to Peak /2 (deg)](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr200030.html) Returns the mean (peak-to-peak)/2 phase deviation around the unmodulated carrier phase. This value is expressed in degrees.
- [Analog Demod:Results:PM Deviation:Mean Positive Peak (deg)](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr200031.html) Returns the mean positive peak phase deviation around the unmodulated carrier phase. This value is expressed in degrees.
- [Analog Demod:Results:PM Deviation:Mean RMS (deg)](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr200033.html) Returns the mean RMS phase deviation of the phase-modulated signal. This value is expressed in degrees.
- [Analog Demod:Results:PM Deviation:Mean Standard Deviation (deg)](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr20002f.html) Returns the mean phase deviation around the unmodulated carrier phase. This value is expressed in degrees.
- [Center Frequency (Hz)](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr202001.html) Specifies the carrier frequency of the RF signal that needs to be acquired. This value is expressed in Hz. The signal analyzer tunes to this frequency.
- [Digital Demod:APSK:R2 to R1 Ratio](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr201049.html) Specifies the ratio of the magnitude of symbols on a ring(R2) to the magnitude of symbols on the inner ring(R1). It is applicable for both 16-APSK and 32-APSK.
- [Digital Demod:APSK:R3 to R1 Ratio](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr20104a.html) Specifies the ratio of the magnitude of symbols on a ring(R3) to the magnitude of symbols on the inner ring(R1). It is applicable for 32-APSK.
- [Digital Demod:All Traces Enabled](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr201015.html) Specifies whether to enable the traces to be stored and retrieved after performing the digital demodulation.
- [Digital Demod:Averaging:Count](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr201003.html) Specifies the number of acquisitions used for averaging when you set the DDemod Averaging Enabled property to True .
- [Digital Demod:Averaging:Enabled](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr201002.html) Enables averaging for digital demodulation measurements.
- [Digital Demod:Burst End Exclusion Symbols](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr201043.html) Specifies the number of symbols that is excluded from the measurement before the falling edge of the burst.
- [Digital Demod:Burst Start Exclusion Symbols](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr201042.html) Specifies the number of symbols from the start of the burst trigger that is excluded from the measurement.
- [Digital Demod:Compensation:CFO Estimation Mode](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr201045.html) Specifies the carrier frequency offset estimation capability of the demodulator. If you select Narrow , coarse carrier frequency offset estimation is disabled and only fine carrier frequency offset estimation is performed. This is useful when analysing low SNR signals.
- [Digital Demod:Compensation:IQ Offset Removal Enabled](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr201044.html) Specifies whether to remove the I/Q offset before the EVM measurement.
- [Digital Demod:Differential Enabled](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr201005.html) Specifies whether the symbols are differentially encoded. This property is applicable only to PSK and MSK modulation types.
- [Digital Demod:EVM Normalization Reference](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr201039.html) Specifies the reference used to normalize the error vector magnitude (EVM).
- [Digital Demod:Equalizer:Convergence Factor](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr201007.html) Specifies the incremental step used by the equalizer to adapt to the channel during the training stage.
- [Digital Demod:Equalizer:Filter Length (Symbols)](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr201036.html) Specifies the length of the equalization filter to be computed. The length is specified in terms of symbols.
- [Digital Demod:Equalizer:Mode](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr201006.html) Specifies whether the measurement needs to perform equalization.
- [Digital Demod:Equalizer:Training Count](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr201037.html) Specifies the number of iterations during which the equalizer adapts its coefficients in the training stage. After the training stage, the measurement is performed over the specified number of averages.
- [Digital Demod:FSK:Deviation (Hz)](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr201008.html) Specifies the expected FSK frequency deviation At baseband frequencies, deviations for individual symbols are evenly spaced in the interval [- fd , fd ], where fd represents the frequency deviation. This value is expressed in Hz.
- [Digital Demod:FSK:Reference Compensation Enabled](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr201038.html) Specifies whether the FSK deviation that you specify is used to compensate for gain errors and compute FSK error.
- [Digital Demod:M](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr201009.html) Specifies the M-ary number, which is the number of distinct states that represent symbols in the complex baseband modulated waveform.
- [Digital Demod:Measurement Enabled](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr201000.html) Enables digital demodulation measurements.
- [Digital Demod:Measurement Filter:Type](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr20100a.html) Specifies whether the measurement needs to compute the measurement filter based on the pulse-shaping filter type or uses the custom measurement filter coefficients.
- [Digital Demod:Modulation Type](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr20100b.html) Specifies the digital modulation type of the signal that needs to be analyzed.
- [Digital Demod:Number of Symbols](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr20100d.html) Specifies the number of symbols to be analyzed. The measurement acquires additional symbols to account for filter delays.
- [Digital Demod:PSK:Format](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr20100e.html) Specifies the PSK format.
- [Digital Demod:Pulse Shaping Filter:Parameter](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr201010.html) Specifies the rolloff factor for raised cosine and root-raised cosine filter that is used as pulse-shaping filter and measurement filter respectively.
- [Digital Demod:Pulse Shaping Filter:Type](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr20100f.html) Specifies the pulse-shaping filter used to transmit the signal. This property determines the measurement filter to be used for analysis when you set the DDemod Meas Filter Type property to Auto .
- [Digital Demod:Results:Carrier:Mean Frequency Drift (Hz)](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr201022.html) Returns the measured carrier frequency drift. This value is expressed in Hz.
- [Digital Demod:Results:Carrier:Mean Frequency Offset (Hz)](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr201021.html) Returns the measured frequency offset from the transmitted carrier frequency. This value is expressed in Hz.
- [Digital Demod:Results:Carrier:Mean Phase Error (deg)](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr201023.html) Returns the measured phase offset from the transmitted carrier phase. This value is expressed in degrees.
- [Digital Demod:Results:EVM:Maximum Peak (%)](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr201027.html) Returns the maximum of the peak EVM measured per acquisition, as a percentage.
- [Digital Demod:Results:EVM:Maximum RMS (%)](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr201025.html) Returns the maximum of the RMS EVM measured per acquisition, as a percentage.
- [Digital Demod:Results:EVM:Mean Modulation Error Ratio (dB)](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr201028.html) Returns the modulation error ratio. This value is expressed in dB.
- [Digital Demod:Results:EVM:Mean Peak (%)](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr201026.html) Returns the mean of the peak EVM measured per acquisition, as a percentage.
- [Digital Demod:Results:EVM:Mean RMS (%)](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr201024.html) Returns the mean of the RMS EVM measured per acquisition, as a percentage.
- [Digital Demod:Results:FSK:Max Peak FSK Error (Hz)](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr20102f.html) Returns the maximum of peak frequency error of the FSK symbols measured per acquisition. This value is expressed in Hz.
- [Digital Demod:Results:FSK:Mean Deviation (Hz)](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr20102d.html) Returns the reference FSK deviation used to measure the FSK error. This value is expressed in Hz.
- [Digital Demod:Results:FSK:Mean RMS FSK Error (Hz)](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr20102e.html) Returns the mean of the RMS frequency error of the FSK symbols measured per acquisition. This value is expressed in Hz.
- [Digital Demod:Results:IQ Impairments:Mean IQ Gain Imbalance (dB)](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr201030.html) Returns the measured ratio of I gain to Q gain. This value is expressed in dB.
- [Digital Demod:Results:IQ Impairments:Mean IQ Origin Offset (dB)](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr201032.html) Returns the offset from the ideal location of the constellation origin. This value is expressed in dB.
- [Digital Demod:Results:IQ Impairments:Mean Quadrature Skew (deg)](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr201031.html) Returns a measure of I and Q components in the signal that are not perfectly orthogonal. Quadrature error can be either positive or negative, with the sign indicating the orientation of the error.
- [Digital Demod:Results:Magnitude Error:Maximum (%)](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr20102a.html) Returns the maximum of the magnitude error measured per acquisition, as a percentage.
- [Digital Demod:Results:Magnitude Error:Mean (%)](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr201029.html) Returns the mean of the magnitude error measured per acquisition, as a percentage.
- [Digital Demod:Results:Mean Amplitude Droop (dB/Symbol)](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr20103f.html) Returns the mean amplitude droop per symbol.
- [Digital Demod:Results:Mean Rho Factor](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr20103e.html) Returns the correlation of the measurement waveform and the reference waveform.
- [Digital Demod:Results:Offset EVM:Maximum Peak (%)](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr20103d.html) Returns the maximum of the peak EVM, as a percentage, measured per acquisition, after removing the offset between the I and Q channels of OQPSK demodulated signal.
- [Digital Demod:Results:Offset EVM:Maximum RMS (%)](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr20103c.html) Returns the maximum of the RMS EVM, as a percentage, measured per acquisition, after removing the offset between the I and Q channels of OQPSK demodulated signal.
- [Digital Demod:Results:Offset EVM:Mean Peak (%)](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr20103b.html) Returns the mean of the peak EVM, as a percentage, measured per acquisition, after removing the offset between the I and Q channels of OQPSK demodulated signal.
- [Digital Demod:Results:Offset EVM:Mean RMS (%)](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr20103a.html) Returns the mean of the RMS EVM, as a percentage, measured per acquisition, after removing the offset between the I and Q channels of OQPSK demodulated signal.
- [Digital Demod:Results:Phase Error:Maximum (deg)](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr20102c.html) Returns the maximum of the phase error measured per acquisition. This value is expressed in degrees.
- [Digital Demod:Results:Phase Error:Mean (deg)](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr20102b.html) Returns the mean of the phase error measured per acquisition. This value is expressed in degrees.
- [Digital Demod:Results:Sync Found?](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr201035.html) Indicates whether the synchronization bits were found in the demodulated signal.
- [Digital Demod:Samples Per Symbol](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr201011.html) Specifies the samples per symbol used to acquire the signal for the measurement.
- [Digital Demod:Search:Search Length (s)](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr201048.html) Specifies the length of the waveform within which the synchronization bit pattern needs to be searched when you set the DDemod Search Length Auto property to True .
- [Digital Demod:Search:Search Length Auto](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr201047.html) Specifies whether the measurement should search for synchronization bit pattern in the waveform of length determined by the measurement or search for length duration.
- [Digital Demod:Signal Structure](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr201041.html) Specifies whether the signal is either a bursty signal or a continuous signal.
- [Digital Demod:Spectrum Inverted](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr201012.html) Specifies whether to swap the acquired I and Q samples for demodulation.
- [Digital Demod:Symbol Map Type](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr201040.html) Specifies whether the measurement uses the default symbol map or the map that you configure using the RFmxDemod DDemod Configure Symbol Map VI.
- [Digital Demod:Symbol Rate (Hz)](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr201013.html) Specifies the number of symbols transmitted in one second. This value is expressed in Hz.
- [Digital Demod:Synchronization:Bits](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr20101f.html) Specifies the synchronization bits used to create the reference sequence that must be located in the demodulated signal. The synchronization bits are modulated based on the modulation type to create the reference sequence.
- [Digital Demod:Synchronization:Enabled](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr201014.html) Specifies whether the demodulator needs to search and synchronize the signal to a known reference sequence. The reference sequence is the symbol representation of a defined set of bits known to be present in the transmitted signal. If the synchronization is found in the demodulated signal, the measurement is performed from this point onward. If the synchronization is not found, the entire signal is used for the measurement.
- [Digital Demod:Synchronization:Measurement Offset](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr201034.html) Specifies the offset, which is the location from which the signal is considered for further measurements. The offset is specified in symbols of the reference sequence. This offset is not applicable when the synchronization bits are not found.
- [External Attenuation (dB)](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr202002.html) Specifies the attenuation of a switch (or cable) connected to the RF IN connector of the signal analyzer. For more information about attenuation, refer to the Attenuation and Signal Levels topic for your device in the NI RF Vector Signal Analyzers Help . This value is expressed in dB.
- [Reference Level](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr202003.html) Specifies the reference level which represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices.
- [Reference Level Headroom](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr202ffc.html) Specifies the margin RFmx adds to the Reference Level property. The margin avoids clipping and overflow warnings if the input signal exceeds the configured reference level.
- [Result Fetch Timeout (s)](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr203000.html) Specifies the time to wait before results are available in the RFmxDemod Property Node . Set this value to a time longer than expected for fetching the measurement. A value of -1 specifies that the RFmxDemod Property Node waits until the measurement is complete. This value is expressed in seconds.
- [Selected Ports](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr202ffd.html) Specifies the instrument port to be configured to acquire a signal. Use RFmxInstr Get Available Ports VI to get the valid port names.
- [Selector String](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr0.html) Specifies the selector string used to access all subsequent selector string-based properties in this instance of the property node.
- [Trigger:Delay (s)](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr20200a.html) Specifies the trigger delay time. This value is expressed in seconds.
- [Trigger:Digital Edge:Edge](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr202006.html) Specifies whether the signal analyzer detects a rising or falling edge on the digital-edge trigger signal. This property is applicable only when you set the Trigger Type property to Digital Edge .
- [Trigger:Digital Edge:Source](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr202005.html) Specifies the source terminal for the digital-edge trigger. This property is applicable only when you set the Trigger Type property to Digital Edge .
- [Trigger:IQ Power Edge:Level (dB or dBm)](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr202008.html) Specifies the power level at which the device triggers. This value is expressed in dB when you set the IQ Power Edge Level Type property to Relative and in dBm when you set the IQ Power Edge Level Type property to Absolute . The device asserts the trigger when the signal exceeds the level specified by the value of this property, taking into consideration the specified slope. This property is used only when you set the Trigger Type property to IQ Power Edge .
- [Trigger:IQ Power Edge:Level Type](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr202fff.html) Specifies the reference for the IQ Power Edge Level property. This property is used only when you set the Trigger Type property to IQ Power Edge .
- [Trigger:IQ Power Edge:Slope](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr202009.html) Specifies whether the device asserts the trigger when the signal power is rising or falling. The device asserts the trigger when the signal power exceeds the specified level with the slope you specify. This property is used only when you set the Trigger Type property to IQ Power Edge .
- [Trigger:IQ Power Edge:Source](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr202007.html) Specifies the channel from which the device monitors the trigger. This property is applicable only when you set the Trigger Type property to IQ Power Edge .
- [Trigger:Minimum Quiet Time:Duration (s)](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr20200c.html) Specifies the time duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. If you set the IQ Power Edge Slope property to Rising Slope , the signal is quiet below the trigger level. If you set the IQ Power Edge Slope property to Falling Slope , the signal is quiet above the trigger level. This value is expressed in seconds.
- [Trigger:Minimum Quiet Time:Mode](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr20200b.html) Specifies whether the measurement computes the minimum quiet time used for triggering.
- [Trigger:Type](../../../resource/objmgr/rfmxdemod-rc/rfmxdemod/attr202004.html) Specifies the type of Reference Trigger to use for signal acquisition.

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=resource/objmgr/rfmxdemod-rc/rfmxdemod/attr200003.html language=enus -->
## TOPIC 00005: Analog Demod:Audio Filter:Type

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `resource/objmgr/rfmxdemod-rc/rfmxdemod/attr200003.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxdemod-rc/rfmxdemod/attr200003.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the audio filter to be applied on the analog demodulated signal. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is

### Analog Demod:Audio Filter:Type

Specifies the audio filter to be applied on the analog demodulated signal.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **None**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ADemod Audio Filter Type |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxDemod ADemod Configure Audio Filter |
| Resettable | Yes |

| None | 0 | Does not use any audio filter. |
| --- | --- | --- |
| Custom | 1 | Uses the filter specified by the Ademod Audio Filter Lower Cutoff property and the Ademod Audio Filter Upper Cutoff property. |
| A - Weight | 2 | Uses an A-weighted filter. |
| B - Weight | 3 | Uses a B-weighted filter. |
| C - Weight | 4 | Uses a C-weighted filter. |
| CCITT | 5 | Uses the filter specified by CCITT. |
| ITU-R 468-4 | 6 | Uses the filter specified by ITU-R 468-4. |

Parent topic:

RFmxDemod Properties

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=resource/objmgr/rfmxdemod-rc/rfmxdemod/attr200005.html language=enus -->
## TOPIC 00006: Analog Demod:Audio Filter:Upper Cutoff Frequency (Hz)

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `resource/objmgr/rfmxdemod-rc/rfmxdemod/attr200005.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxdemod-rc/rfmxdemod/attr200005.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the upper cutoff frequency of the custom audio filter. This property is applicable only when you set the ADemod Audio Filter Type property to Custom. This value is expressed in Hz. You do not need to use a selector string to configure or read this property for the default signal instance.

### Analog Demod:Audio Filter:Upper Cutoff Frequency (Hz)

Specifies the upper cutoff frequency of the custom audio filter. This property is applicable only when you set the [ADemod Audio Filter Type](/csh?topicname=attr200003.html) property to **Custom**. This value is expressed in Hz.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is 10,000.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ADemod Audio Filter Upper Cutoff (Hz) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxDemod ADemod Configure Audio Filter |
| Resettable | Yes |

Parent topic:

RFmxDemod Properties

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=resource/objmgr/rfmxdemod-rc/rfmxdemod/attr200028.html language=enus -->
## TOPIC 00007: Analog Demod:Results:FM Deviation:Mean Negative Peak (Hz)

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `resource/objmgr/rfmxdemod-rc/rfmxdemod/attr200028.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxdemod-rc/rfmxdemod/attr200028.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean negative peak frequency deviation of the frequency-modulated signal. This value is expressed in Hz. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string synta

### Analog Demod:Results:FM Deviation:Mean Negative Peak (Hz)

Returns the mean negative peak frequency deviation of the frequency-modulated signal. This value is expressed in Hz.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ADemod Results FM Mean Deviation Neg Pk (Hz) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxDemod ADemod Fetch |
| Resettable | No |

Parent topic:

RFmxDemod Properties

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=resource/objmgr/rfmxdemod-rc/rfmxdemod/attr20002a.html language=enus -->
## TOPIC 00008: Analog Demod:Results:FM Deviation:Maximum Standard Deviation (Hz)

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `resource/objmgr/rfmxdemod-rc/rfmxdemod/attr20002a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxdemod-rc/rfmxdemod/attr20002a.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum frequency deviation of the frequency-modulated signal measured across multiple acquisitions. This value is expressed in Hz. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for informa

### Analog Demod:Results:FM Deviation:Maximum Standard Deviation (Hz)

Returns the maximum frequency deviation of the frequency-modulated signal measured across multiple acquisitions. This value is expressed in Hz.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ADemod Results FM Max Std Dev (Hz) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxDemod ADemod Fetch |
| Resettable | No |

Parent topic:

RFmxDemod Properties

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=resource/objmgr/rfmxdemod-rc/rfmxdemod/attr20002b.html language=enus -->
## TOPIC 00009: Analog Demod:Results:FM Deviation:Maximum Peak to Peak /2 (Hz)

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `resource/objmgr/rfmxdemod-rc/rfmxdemod/attr20002b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxdemod-rc/rfmxdemod/attr20002b.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum (peak-to-peak)/2 frequency variation around the nominal frequency of the FM carrier measured across multiple acquisitions. This value is expressed in Hz. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Sele

### Analog Demod:Results:FM Deviation:Maximum Peak to Peak /2 (Hz)

Returns the maximum (peak-to-peak)/2 frequency variation around the nominal frequency of the FM carrier measured across multiple acquisitions. This value is expressed in Hz.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ADemod Results FM Max Deviation Pk to Pk /2 (Hz) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxDemod ADemod Fetch |
| Resettable | No |

Parent topic:

RFmxDemod Properties

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=resource/objmgr/rfmxdemod-rc/rfmxdemod/attr20002d.html language=enus -->
## TOPIC 00010: Analog Demod:Results:FM Deviation:Maximum Negative Peak (Hz)

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `resource/objmgr/rfmxdemod-rc/rfmxdemod/attr20002d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxdemod-rc/rfmxdemod/attr20002d.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum negative peak frequency deviation of the frequency-modulated signal measured across multiple acquisitions. This value is expressed in Hz. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings top

### Analog Demod:Results:FM Deviation:Maximum Negative Peak (Hz)

Returns the maximum negative peak frequency deviation of the frequency-modulated signal measured across multiple acquisitions. This value is expressed in Hz.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ADemod Results FM Max Deviation Neg Pk (Hz) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxDemod ADemod Fetch |
| Resettable | No |

Parent topic:

RFmxDemod Properties

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=resource/objmgr/rfmxdemod-rc/rfmxdemod/attr20100b.html language=enus -->
## TOPIC 00011: Digital Demod:Modulation Type

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `resource/objmgr/rfmxdemod-rc/rfmxdemod/attr20100b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxdemod-rc/rfmxdemod/attr20100b.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the digital modulation type of the signal that needs to be analyzed. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value

### Digital Demod:Modulation Type

Specifies the digital modulation type of the signal that needs to be analyzed.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **PSK**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DDemod Modulation Type |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxDemod DDemod Configure Modulation Type |
| Resettable | Yes |

| ASK | 0 | The modulation type is amplitude-shift keying (ASK). |
| --- | --- | --- |
| FSK | 1 | The modulation type is frequency-shift keying (FSK). |
| PSK | 2 | The modulation type is phase-shift keying (PSK). |
| QAM | 3 | The modulation type is quadrature-amplitude modulation (QAM). |
| MSK | 4 | The modulation type is minimum shift keying (MSK). |
| APSK | 5 | The modulation type is amplitude phase-shift keying (APSK). |

Parent topic:

RFmxDemod Properties

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=resource/objmgr/rfmxdemod-rc/rfmxdemod/attr20100d.html language=enus -->
## TOPIC 00012: Digital Demod:Number of Symbols

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `resource/objmgr/rfmxdemod-rc/rfmxdemod/attr20100d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxdemod-rc/rfmxdemod/attr20100d.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of symbols to be analyzed. The measurement acquires additional symbols to account for filter delays. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string

### Digital Demod:Number of Symbols

Specifies the number of symbols to be analyzed. The measurement acquires additional symbols to account for filter delays.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is 1,000.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DDemod Num Symbols |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxDemod DDemod Configure Number of Symbols |
| Resettable | Yes |

Parent topic:

RFmxDemod Properties

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=resource/objmgr/rfmxdemod-rc/rfmxdemod/attr20100e.html language=enus -->
## TOPIC 00013: Digital Demod:PSK:Format

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `resource/objmgr/rfmxdemod-rc/rfmxdemod/attr20100e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxdemod-rc/rfmxdemod/attr20100e.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the PSK format. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is Normal. Remarks The following table lists the cha

### Digital Demod:PSK:Format

Specifies the PSK format.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **Normal**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DDemod PSK Format |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxDemod DDemod Configure PSK Format |
| Resettable | Yes |

| Normal | 0 | Sets the modulation type to PSK. |
| --- | --- | --- |
| Offset QPSK | 1 | Sets the modulation type to offset quadrature PSK (OQPSK). The ideal symbol timing of Q is offset by half of a symbol period from the ideal symbol timing of I. |
| PI/4 - QPSK | 2 | Sets the modulation type to pi/4 QPSK. In this modulation, each QPSK symbol is rotated by pi/4. |
| PI/8 - 8PSK | 3 | Sets the modulation type to pi/8-8 PSK. In this modulation, each 8 PSK symbol is rotated by pi/8. |
| 3*PI/8 - 8PSK | 4 | Sets the modulation type to 3*pi/8-8 PSK. In this modulation, each 8 PSK symbol is rotated by 3*pi/8. |
| Shaped Offset QPSK | 5 | Sets the modulation type to Shaped Offset QPSK.The ideal symbol timing of Q is offset by half of a symbol period from the ideal symbol timing of I and the waveform is shaped using frequency pulse filter. |

Parent topic:

RFmxDemod Properties

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=resource/objmgr/rfmxdemod-rc/rfmxdemod/attr20100f.html language=enus -->
## TOPIC 00014: Digital Demod:Pulse Shaping Filter:Type

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `resource/objmgr/rfmxdemod-rc/rfmxdemod/attr20100f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxdemod-rc/rfmxdemod/attr20100f.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the pulse-shaping filter used to transmit the signal. This property determines the measurement filter to be used for analysis when you set the DDemod Meas Filter Type property to Auto. You do not need to use a selector string to configure or read this property for the default signal instan

### Digital Demod:Pulse Shaping Filter:Type

Specifies the pulse-shaping filter used to transmit the signal. This property determines the measurement filter to be used for analysis when you set the [DDemod Meas Filter Type](/csh?topicname=attr20100a.html) property to **Auto**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **Root Raised Cosine**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DDemod Pulse Shaping Filter Type |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxDemod DDemod Configure Pulse Shaping Filter |
| Resettable | Yes |

| Rectangular | 0 | The transmitted waveform is filtered using a rectangular filter. |
| --- | --- | --- |
| Raised Cosine | 1 | The transmitted waveform is filtered using a raised cosine filter. Specify the filter Alpha in the DDemod Pulse Shaping Filter Parameter property. |
| Root Raised Cosine | 2 | The transmitted waveform is filtered using a root raised cosine filter. Specify the filter Alpha in the DDemod Pulse Shaping Filter Parameter property. |
| Gaussian | 3 | The transmitted waveform is filtered using a Gaussian filter. Specify the filter bandwidth * sample duration in the DDemod Pulse Shaping Filter Parameter property. This filter is applicable only to FSK and MSK modulation types. |
| Custom | 4 | The transmitted waveform is filtered using the coefficients that you specify in the RFmxDemod DDemod Configure Pulse Shaping Filter Custom Coefficients VI. |
| Half Sine | 5 | The transmitted waveform is filtered using a half sine filter. |
| Linearized GMSK - EDGE | 6 | The transmitted waveform is filtered using an EDGE-specific linearized GMSK filter. |
| SOQPSK - TG | 7 | The transmitted waveform is filtered using a SOQPSK - TG filter as defined in IRIG standard. |

Parent topic:

RFmxDemod Properties

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=resource/objmgr/rfmxdemod-rc/rfmxdemod/attr201010.html language=enus -->
## TOPIC 00015: Digital Demod:Pulse Shaping Filter:Parameter

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `resource/objmgr/rfmxdemod-rc/rfmxdemod/attr201010.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxdemod-rc/rfmxdemod/attr201010.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the rolloff factor for raised cosine and root-raised cosine filter that is used as pulse-shaping filter and measurement filter respectively. For Gaussian filter, this property specifies bandwidth * sample duration. You do not need to use a selector string to configure or read this property

### Digital Demod:Pulse Shaping Filter:Parameter

Specifies the rolloff factor for raised cosine and root-raised cosine filter that is used as pulse-shaping filter and measurement filter respectively.

For Gaussian filter, this property specifies bandwidth * sample duration.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is 0.5.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DDemod Pulse Shaping Filter Parameter |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxDemod DDemod Configure Pulse Shaping Filter |
| Resettable | Yes |

Parent topic:

RFmxDemod Properties

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=resource/objmgr/rfmxdemod-rc/rfmxdemod/attr201011.html language=enus -->
## TOPIC 00016: Digital Demod:Samples Per Symbol

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `resource/objmgr/rfmxdemod-rc/rfmxdemod/attr201011.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxdemod-rc/rfmxdemod/attr201011.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the samples per symbol used to acquire the signal for the measurement. Sample rate = Symbol rate * Samples per symbol. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the

### Digital Demod:Samples Per Symbol

Specifies the samples per symbol used to acquire the signal for the measurement.

*Sample rate* = *Symbol rate* * *Samples per symbol*.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **Auto**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DDemod Samples Per Symbol |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxDemod DDemod Configure Samples Per Symbol |
| Resettable | Yes |

| Auto | -1 | The measurement uses appropriate samples per symbol(SPS) based on modulation type and pulse shaping filter. SPS=8, for FSK. SPS=4, for ASK,PSK, QAM, MSK when pulse shape filter is not rectangular. SPS=8, for ASK, PSK, QAM, MSK when pulse shape filter is rectangular. |
| --- | --- | --- |
| 4 | 4 | The samples per symbol value is 4. |
| 8 | 8 | The samples per symbol value is 8. |
| 16 | 16 | The samples per symbol value is 16. |

Parent topic:

RFmxDemod Properties

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=resource/objmgr/rfmxdemod-rc/rfmxdemod/attr201012.html language=enus -->
## TOPIC 00017: Digital Demod:Spectrum Inverted

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `resource/objmgr/rfmxdemod-rc/rfmxdemod/attr201012.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxdemod-rc/rfmxdemod/attr201012.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to swap the acquired I and Q samples for demodulation. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is Fa

### Digital Demod:Spectrum Inverted

Specifies whether to swap the acquired I and Q samples for demodulation.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **False**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DDemod Spectrum Inverted |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxDemod DDemod Configure Spectrum Inverted |
| Resettable | Yes |

| False | 0 | The acquired I and Q samples are used for demodulation as is. |
| --- | --- | --- |
| True | 1 | The acquired I and Q samples are swapped before using the signal for demodulation. |

Parent topic:

RFmxDemod Properties

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=resource/objmgr/rfmxdemod-rc/rfmxdemod/attr201013.html language=enus -->
## TOPIC 00018: Digital Demod:Symbol Rate (Hz)

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `resource/objmgr/rfmxdemod-rc/rfmxdemod/attr201013.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxdemod-rc/rfmxdemod/attr201013.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of symbols transmitted in one second. This value is expressed in Hz. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The de

### Digital Demod:Symbol Rate (Hz)

Specifies the number of symbols transmitted in one second. This value is expressed in Hz.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is 100 kHz.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DDemod Symbol Rate (Hz) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxDemod DDemod Configure Symbol Rate |
| Resettable | Yes |

Parent topic:

RFmxDemod Properties

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=resource/objmgr/rfmxdemod-rc/rfmxdemod/attr201014.html language=enus -->
## TOPIC 00019: Digital Demod:Synchronization:Enabled

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `resource/objmgr/rfmxdemod-rc/rfmxdemod/attr201014.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxdemod-rc/rfmxdemod/attr201014.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the demodulator needs to search and synchronize the signal to a known reference sequence. The reference sequence is the symbol representation of a defined set of bits known to be present in the transmitted signal. If the synchronization is found in the demodulated signal, the measu

### Digital Demod:Synchronization:Enabled

Specifies whether the demodulator needs to search and synchronize the signal to a known reference sequence. The reference sequence is the symbol representation of a defined set of bits known to be present in the transmitted signal. If the synchronization is found in the demodulated signal, the measurement is performed from this point onward. If the synchronization is not found, the entire signal is used for the measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **False**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DDemod Sync Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxDemod DDemod Configure Synchronization |
| Resettable | Yes |

| False | 0 | Does not search and synchronize the signal. |
| --- | --- | --- |
| True | 1 | Searches and synchronizes the signal. |

Parent topic:

RFmxDemod Properties

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=resource/objmgr/rfmxdemod-rc/rfmxdemod/attr201015.html language=enus -->
## TOPIC 00020: Digital Demod:All Traces Enabled

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `resource/objmgr/rfmxdemod-rc/rfmxdemod/attr201015.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxdemod-rc/rfmxdemod/attr201015.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the traces to be stored and retrieved after performing the digital demodulation. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for na

### Digital Demod:All Traces Enabled

Specifies whether to enable the traces to be stored and retrieved after performing the digital demodulation.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is FALSE.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DDemod All Traces Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxDemod Select Measurement |
| Resettable | Yes |

Parent topic:

RFmxDemod Properties

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=resource/objmgr/rfmxdemod-rc/rfmxdemod/attr20101f.html language=enus -->
## TOPIC 00021: Digital Demod:Synchronization:Bits

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `resource/objmgr/rfmxdemod-rc/rfmxdemod/attr20101f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxdemod-rc/rfmxdemod/attr20101f.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the synchronization bits used to create the reference sequence that must be located in the demodulated signal. The synchronization bits are modulated based on the modulation type to create the reference sequence. You do not need to use a selector string to configure or read this property f

### Digital Demod:Synchronization:Bits

Specifies the synchronization bits used to create the reference sequence that must be located in the demodulated signal. The synchronization bits are modulated based on the modulation type to create the reference sequence.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DDemod Sync Bits |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxDemod DDemod Configure Synchronization |
| Resettable | Yes |

Parent topic:

RFmxDemod Properties

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=resource/objmgr/rfmxdemod-rc/rfmxdemod/attr201021.html language=enus -->
## TOPIC 00022: Digital Demod:Results:Carrier:Mean Frequency Offset (Hz)

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `resource/objmgr/rfmxdemod-rc/rfmxdemod/attr201021.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxdemod-rc/rfmxdemod/attr201021.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the measured frequency offset from the transmitted carrier frequency. This value is expressed in Hz. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for na

### Digital Demod:Results:Carrier:Mean Frequency Offset (Hz)

Returns the measured frequency offset from the transmitted carrier frequency. This value is expressed in Hz.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DDemod Results Carrier Mean Freq Offset (Hz) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxDemod DDemod Fetch |
| Resettable | No |

Parent topic:

RFmxDemod Properties

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=resource/objmgr/rfmxdemod-rc/rfmxdemod/attr201032.html language=enus -->
## TOPIC 00023: Digital Demod:Results:IQ Impairments:Mean IQ Origin Offset (dB)

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `resource/objmgr/rfmxdemod-rc/rfmxdemod/attr201032.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxdemod-rc/rfmxdemod/attr201032.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the offset from the ideal location of the constellation origin. This value is expressed in dB. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named si

### Digital Demod:Results:IQ Impairments:Mean IQ Origin Offset (dB)

Returns the offset from the ideal location of the constellation origin. This value is expressed in dB.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DDemod Results Mean IQ Origin Offset (dB) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxDemod DDemod Fetch |
| Resettable | No |

Parent topic:

RFmxDemod Properties

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=resource/objmgr/rfmxdemod-rc/rfmxdemod/attr201036.html language=enus -->
## TOPIC 00024: Digital Demod:Equalizer:Filter Length (Symbols)

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `resource/objmgr/rfmxdemod-rc/rfmxdemod/attr201036.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxdemod-rc/rfmxdemod/attr201036.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the length of the equalization filter to be computed. The length is specified in terms of symbols. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for na

### Digital Demod:Equalizer:Filter Length (Symbols)

Specifies the length of the equalization filter to be computed. The length is specified in terms of symbols.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is 20.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DDemod Equalizer Filter Length (Symbols) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxDemod DDemod Configure Equalizer |
| Resettable | Yes |

Parent topic:

RFmxDemod Properties

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=resource/objmgr/rfmxdemod-rc/rfmxdemod/attr201038.html language=enus -->
## TOPIC 00025: Digital Demod:FSK:Reference Compensation Enabled

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `resource/objmgr/rfmxdemod-rc/rfmxdemod/attr201038.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxdemod-rc/rfmxdemod/attr201038.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the FSK deviation that you specify is used to compensate for gain errors and compute FSK error. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax f

### Digital Demod:FSK:Reference Compensation Enabled

Specifies whether the FSK deviation that you specify is used to compensate for gain errors and compute FSK error.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **False**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DDemod FSK Ref Comp Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxDemod DDemod Configure FSK Deviation |
| Resettable | Yes |

| False | 0 | Does not compensate for gain errors. |
| --- | --- | --- |
| True | 1 | Compensates for gain errors. |

Parent topic:

RFmxDemod Properties

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=resource/objmgr/rfmxdemod-rc/rfmxdemod/attr201039.html language=enus -->
## TOPIC 00026: Digital Demod:EVM Normalization Reference

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `resource/objmgr/rfmxdemod-rc/rfmxdemod/attr201039.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxdemod-rc/rfmxdemod/attr201039.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the reference used to normalize the error vector magnitude (EVM). You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is

### Digital Demod:EVM Normalization Reference

Specifies the reference used to normalize the error vector magnitude (EVM).

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **Peak**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DDemod EVM Norm Ref |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxDemod DDemod Configure EVM Normalization Reference |
| Resettable | Yes |

| Peak | 0 | The EVM is normalized to the peak magnitude of the reference symbols. |
| --- | --- | --- |
| RMS | 1 | The EVM is normalized to the RMS magnitude of the reference symbols. This value is applicable only to modulation types, such as quadrature-amplitude modulation (QAM). This value is expressed in which the symbols in the map do not have a constant amplitude. |

Parent topic:

RFmxDemod Properties

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=resource/objmgr/rfmxdemod-rc/rfmxdemod/attr20103a.html language=enus -->
## TOPIC 00027: Digital Demod:Results:Offset EVM:Mean RMS (%)

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `resource/objmgr/rfmxdemod-rc/rfmxdemod/attr20103a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxdemod-rc/rfmxdemod/attr20103a.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean of the RMS EVM, as a percentage, measured per acquisition, after removing the offset between the I and Q channels of OQPSK demodulated signal. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings t

### Digital Demod:Results:Offset EVM:Mean RMS (%)

Returns the mean of the RMS EVM, as a percentage, measured per acquisition, after removing the offset between the I and Q channels of OQPSK demodulated signal.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DDemod Results Mean RMS Offset EVM (%) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxDemod DDemod Fetch |
| Resettable | No |

Parent topic:

RFmxDemod Properties

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=resource/objmgr/rfmxdemod-rc/rfmxdemod/attr20103b.html language=enus -->
## TOPIC 00028: Digital Demod:Results:Offset EVM:Mean Peak (%)

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `resource/objmgr/rfmxdemod-rc/rfmxdemod/attr20103b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxdemod-rc/rfmxdemod/attr20103b.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean of the peak EVM, as a percentage, measured per acquisition, after removing the offset between the I and Q channels of OQPSK demodulated signal. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings

### Digital Demod:Results:Offset EVM:Mean Peak (%)

Returns the mean of the peak EVM, as a percentage, measured per acquisition, after removing the offset between the I and Q channels of OQPSK demodulated signal.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DDemod Results Mean Peak Offset EVM (%) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxDemod DDemod Fetch |
| Resettable | No |

Parent topic:

RFmxDemod Properties

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=resource/objmgr/rfmxdemod-rc/rfmxdemod/attr20103c.html language=enus -->
## TOPIC 00029: Digital Demod:Results:Offset EVM:Maximum RMS (%)

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `resource/objmgr/rfmxdemod-rc/rfmxdemod/attr20103c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxdemod-rc/rfmxdemod/attr20103c.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum of the RMS EVM, as a percentage, measured per acquisition, after removing the offset between the I and Q channels of OQPSK demodulated signal. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector String

### Digital Demod:Results:Offset EVM:Maximum RMS (%)

Returns the maximum of the RMS EVM, as a percentage, measured per acquisition, after removing the offset between the I and Q channels of OQPSK demodulated signal.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DDemod Results Max RMS Offset EVM (%) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxDemod DDemod Fetch |
| Resettable | No |

Parent topic:

RFmxDemod Properties

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=resource/objmgr/rfmxdemod-rc/rfmxdemod/attr20103d.html language=enus -->
## TOPIC 00030: Digital Demod:Results:Offset EVM:Maximum Peak (%)

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `resource/objmgr/rfmxdemod-rc/rfmxdemod/attr20103d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxdemod-rc/rfmxdemod/attr20103d.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum of the peak EVM, as a percentage, measured per acquisition, after removing the offset between the I and Q channels of OQPSK demodulated signal. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strin

### Digital Demod:Results:Offset EVM:Maximum Peak (%)

Returns the maximum of the peak EVM, as a percentage, measured per acquisition, after removing the offset between the I and Q channels of OQPSK demodulated signal.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DDemod Results Max Peak Offset EVM (%) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxDemod DDemod Fetch |
| Resettable | No |

Parent topic:

RFmxDemod Properties

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=resource/objmgr/rfmxdemod-rc/rfmxdemod/attr20103e.html language=enus -->
## TOPIC 00031: Digital Demod:Results:Mean Rho Factor

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `resource/objmgr/rfmxdemod-rc/rfmxdemod/attr20103e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxdemod-rc/rfmxdemod/attr20103e.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the correlation of the measurement waveform and the reference waveform. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. Remarks The foll

### Digital Demod:Results:Mean Rho Factor

Returns the correlation of the measurement waveform and the reference waveform.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DDemod Results Mean Rho Factor |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxDemod DDemod Fetch |
| Resettable | No |

Parent topic:

RFmxDemod Properties

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=resource/objmgr/rfmxdemod-rc/rfmxdemod/attr20103f.html language=enus -->
## TOPIC 00032: Digital Demod:Results:Mean Amplitude Droop (dB/Symbol)

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `resource/objmgr/rfmxdemod-rc/rfmxdemod/attr20103f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxdemod-rc/rfmxdemod/attr20103f.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean amplitude droop per symbol. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. Remarks The following table lists the characteristi

### Digital Demod:Results:Mean Amplitude Droop (dB/Symbol)

Returns the mean amplitude droop per symbol.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DDemod Results Mean Amplitude Droop |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxDemod DDemod Fetch |
| Resettable | No |

Parent topic:

RFmxDemod Properties

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=resource/objmgr/rfmxdemod-rc/rfmxdemod/attr201040.html language=enus -->
## TOPIC 00033: Digital Demod:Symbol Map Type

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `resource/objmgr/rfmxdemod-rc/rfmxdemod/attr201040.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxdemod-rc/rfmxdemod/attr201040.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement uses the default symbol map or the map that you configure using the RFmxDemod DDemod Configure Symbol Map VI. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for informa

### Digital Demod:Symbol Map Type

Specifies whether the measurement uses the default symbol map or the map that you configure using the [RFmxDemod DDemod Configure Symbol Map](/csh?context=rfmxdemod_rfmxdemodvi_rfmxdemod_ddemod_configure_symbol_map) VI.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **Auto**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DDemod Symbol Map Type |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxDemod DDemod Configure Symbol Map |
| Resettable | Yes |

| Auto | 0 | Uses a default symbol map. |
| --- | --- | --- |
| Custom | 1 | Uses the map that you specify using the RFmxDemod DDemod Configure Symbol Map VI . |

Parent topic:

RFmxDemod Properties

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=resource/objmgr/rfmxdemod-rc/rfmxdemod/attr201041.html language=enus -->
## TOPIC 00034: Digital Demod:Signal Structure

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `resource/objmgr/rfmxdemod-rc/rfmxdemod/attr201041.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxdemod-rc/rfmxdemod/attr201041.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the signal is either a bursty signal or a continuous signal. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value

### Digital Demod:Signal Structure

Specifies whether the signal is either a bursty signal or a continuous signal.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **Continuous**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DDemod Signal Structure |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| Bursted | 0 | The signal is a bursty signal. |
| --- | --- | --- |
| Continuous | 1 | The signal is a continuous signal. |

Parent topic:

RFmxDemod Properties

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=resource/objmgr/rfmxdemod-rc/rfmxdemod/attr201042.html language=enus -->
## TOPIC 00035: Digital Demod:Burst Start Exclusion Symbols

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `resource/objmgr/rfmxdemod-rc/rfmxdemod/attr201042.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxdemod-rc/rfmxdemod/attr201042.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of symbols from the start of the burst trigger that is excluded from the measurement. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for name

### Digital Demod:Burst Start Exclusion Symbols

Specifies the number of symbols from the start of the burst trigger that is excluded from the measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is 0.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DDemod Burst Start Exclusion Symbols |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxDemod Properties

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=resource/objmgr/rfmxdemod-rc/rfmxdemod/attr201043.html language=enus -->
## TOPIC 00036: Digital Demod:Burst End Exclusion Symbols

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `resource/objmgr/rfmxdemod-rc/rfmxdemod/attr201043.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxdemod-rc/rfmxdemod/attr201043.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of symbols that is excluded from the measurement before the falling edge of the burst. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for nam

### Digital Demod:Burst End Exclusion Symbols

Specifies the number of symbols that is excluded from the measurement before the falling edge of the burst.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is 0.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DDemod Burst End Exclusion Symbols |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxDemod Properties

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=resource/objmgr/rfmxdemod-rc/rfmxdemod/attr201044.html language=enus -->
## TOPIC 00037: Digital Demod:Compensation:IQ Offset Removal Enabled

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `resource/objmgr/rfmxdemod-rc/rfmxdemod/attr201044.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxdemod-rc/rfmxdemod/attr201044.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to remove the I/Q offset before the EVM measurement. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is True

### Digital Demod:Compensation:IQ Offset Removal Enabled

Specifies whether to remove the I/Q offset before the EVM measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **True**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DDemod IQ Offset Removal Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| False | 0 | The IQ offset is not removed before the EVM measurement. |
| --- | --- | --- |
| True | 1 | The IQ offset is removed before the EVM measurement. |

Parent topic:

RFmxDemod Properties

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=resource/objmgr/rfmxdemod-rc/rfmxdemod/attr201045.html language=enus -->
## TOPIC 00038: Digital Demod:Compensation:CFO Estimation Mode

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `resource/objmgr/rfmxdemod-rc/rfmxdemod/attr201045.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxdemod-rc/rfmxdemod/attr201045.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the carrier frequency offset estimation capability of the demodulator. If you select Narrow, coarse carrier frequency offset estimation is disabled and only fine carrier frequency offset estimation is performed. This is useful when analysing low SNR signals. Remarks The following table lis

### Digital Demod:Compensation:CFO Estimation Mode

Specifies the carrier frequency offset estimation capability of the demodulator. If you select **Narrow**, coarse carrier frequency offset estimation is disabled and only fine carrier frequency offset estimation is performed. This is useful when analysing low SNR signals.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DDemod CFO Estimation Mode |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| Narrow | 0 | The measurement disables coarse carrier frequency offset estimation. |
| --- | --- | --- |
| Wide | 1 | The measurement enables coarse and fine carrier frequency offset estimation. |

Parent topic:

RFmxDemod Properties

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=resource/objmgr/rfmxdemod-rc/rfmxdemod/attr201047.html language=enus -->
## TOPIC 00039: Digital Demod:Search:Search Length Auto

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `resource/objmgr/rfmxdemod-rc/rfmxdemod/attr201047.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxdemod-rc/rfmxdemod/attr201047.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement should search for synchronization bit pattern in the waveform of length determined by the measurement or search for length duration. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector St

### Digital Demod:Search:Search Length Auto

Specifies whether the measurement should search for synchronization bit pattern in the waveform of length determined by the measurement or search for length duration.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **True**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DDemod Search Length Auto |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| False | 0 | Synchronization bit pattern is searched in a waveform within the search Length duration. |
| --- | --- | --- |
| True | 1 | Synchronization bit pattern is searched in a waveform of length determined by the measurement. |

Parent topic:

RFmxDemod Properties

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=resource/objmgr/rfmxdemod-rc/rfmxdemod/attr201048.html language=enus -->
## TOPIC 00040: Digital Demod:Search:Search Length (s)

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `resource/objmgr/rfmxdemod-rc/rfmxdemod/attr201048.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxdemod-rc/rfmxdemod/attr201048.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the length of the waveform within which the synchronization bit pattern needs to be searched when you set the DDemod Search Length Auto property to True. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strin

### Digital Demod:Search:Search Length (s)

Specifies the length of the waveform within which the synchronization bit pattern needs to be searched when you set the [DDemod Search Length Auto](/csh?topicname=attr201047.html) property to **True**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is 0.001 seconds.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DDemod Search Length (s) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxDemod Properties

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=resource/objmgr/rfmxdemod-rc/rfmxdemod/attr201049.html language=enus -->
## TOPIC 00041: Digital Demod:APSK:R2 to R1 Ratio

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `resource/objmgr/rfmxdemod-rc/rfmxdemod/attr201049.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxdemod-rc/rfmxdemod/attr201049.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the ratio of the magnitude of symbols on a ring(R2) to the magnitude of symbols on the inner ring(R1). It is applicable for both 16-APSK and 32-APSK. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings t

### Digital Demod:APSK:R2 to R1 Ratio

Specifies the ratio of the magnitude of symbols on a ring(R2) to the magnitude of symbols on the inner ring(R1). It is applicable for both 16-APSK and 32-APSK.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is 2.84. Valid values are from 2 to 8, inclusive.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DDemod APSK R2 to R1 Ratio |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxDemod Properties

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=resource/objmgr/rfmxdemod-rc/rfmxdemod/attr202001.html language=enus -->
## TOPIC 00042: Center Frequency (Hz)

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `resource/objmgr/rfmxdemod-rc/rfmxdemod/attr202001.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxdemod-rc/rfmxdemod/attr202001.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the carrier frequency of the RF signal that needs to be acquired. This value is expressed in Hz. The signal analyzer tunes to this frequency. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for

### Center Frequency (Hz)

Specifies the carrier frequency of the RF signal that needs to be acquired. This value is expressed in Hz. The signal analyzer tunes to this frequency.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default of this property is hardware dependent.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Center Freq (Hz) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxDemod Configure Frequency |
| Resettable | Yes |

Parent topic:

RFmxDemod Properties

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=resource/objmgr/rfmxdemod-rc/rfmxdemod/attr202002.html language=enus -->
## TOPIC 00043: External Attenuation (dB)

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `resource/objmgr/rfmxdemod-rc/rfmxdemod/attr202002.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxdemod-rc/rfmxdemod/attr202002.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the attenuation of a switch (or cable) connected to the RF IN connector of the signal analyzer. For more information about attenuation, refer to the Attenuation and Signal Levels topic for your device in the NI RF Vector Signal Analyzers Help. This value is expressed in dB. You do not need

### External Attenuation (dB)

Specifies the attenuation of a switch (or cable) connected to the RF IN connector of the signal analyzer. For more information about attenuation, refer to the *Attenuation and Signal Levels* topic for your device in the *NI RF Vector Signal Analyzers Help*. This value is expressed in dB.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is 0.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | External Attenuation (dB) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxDemod Configure External Attenuation |
| Resettable | Yes |

Parent topic:

RFmxDemod Properties

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=resource/objmgr/rfmxdemod-rc/rfmxdemod/attr202003.html language=enus -->
## TOPIC 00044: Reference Level

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `resource/objmgr/rfmxdemod-rc/rfmxdemod/attr202003.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxdemod-rc/rfmxdemod/attr202003.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the reference level which represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the S

### Reference Level

Specifies the reference level which represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default of this property is hardware dependent.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Reference Level |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxDemod Configure Reference Level |
| Resettable | Yes |

Parent topic:

RFmxDemod Properties

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=resource/objmgr/rfmxdemod-rc/rfmxdemod/attr202004.html language=enus -->
## TOPIC 00045: Trigger:Type

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `resource/objmgr/rfmxdemod-rc/rfmxdemod/attr202004.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxdemod-rc/rfmxdemod/attr202004.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the type of Reference Trigger to use for signal acquisition. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is None

### Trigger:Type

Specifies the type of Reference Trigger to use for signal acquisition.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **None**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Trigger Type |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxDemod Configure Trigger |
| Resettable | Yes |

| None | 0 | No reference trigger is used for signal acquisition. |
| --- | --- | --- |
| Digital Edge | 1 | A digital-edge trigger is used for signal acquisition. The source of the digital edge is specified using the Digital Edge Source property. |
| IQ Power Edge | 2 | An I/Q power-edge trigger is used for signal acquisition, which is configured using the IQ Power Edge Slope property. |
| Software | 3 | A software trigger is used for signal acquisition. |

Parent topic:

RFmxDemod Properties

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=resource/objmgr/rfmxdemod-rc/rfmxdemod/attr202005.html language=enus -->
## TOPIC 00046: Trigger:Digital Edge:Source

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `resource/objmgr/rfmxdemod-rc/rfmxdemod/attr202005.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxdemod-rc/rfmxdemod/attr202005.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the source terminal for the digital-edge trigger. This property is applicable only when you set the Trigger Type property to Digital Edge. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for in

### Trigger:Digital Edge:Source

Specifies the source terminal for the digital-edge trigger. This property is applicable only when you set the [Trigger Type](/csh?topicname=attr202004.html) property to **Digital Edge**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default of this property is hardware dependent.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Digital Edge Source |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxDemod Configure Trigger |
| Resettable | Yes |

| PFI0 | PFI0 | The trigger is received on PFI 0. For the PXIe-5841 with PXIe-5655, the trigger is received on the PXIe-5841 PFI 0. |
| --- | --- | --- |
| PFI1 | PFI1 | The trigger is received on PFI 1. |
| PXI_Trig0 | PXI_Trig0 | The trigger is received on PXI trigger line 0. |
| PXI_Trig1 | PXI_Trig1 | The trigger is received on PXI trigger line 1. |
| PXI_Trig2 | PXI_Trig2 | The trigger is received on PXI trigger line 2. |
| PXI_Trig3 | PXI_Trig3 | The trigger is received on PXI trigger line 3. |
| PXI_Trig4 | PXI_Trig4 | The trigger is received on PXI trigger line 4. |
| PXI_Trig5 | PXI_Trig5 | The trigger is received on PXI trigger line 5. |
| PXI_Trig6 | PXI_Trig6 | The trigger is received on PXI trigger line 6. |
| PXI_Trig7 | PXI_Trig7 | The trigger is received on PXI trigger line 7. |
| PXI_STAR | PXI_STAR | The trigger is received on the PXI star trigger line. This value is not valid for the PXIe-5644/5645/5646. |
| PXIe_DStarB | PXIe_DStarB | The trigger is received on the PXIe DStar B trigger line. This value is valid only on the PXIe-5820/5830/5831/5832/5840/5841/5842/5860. |
| TimerEvent | TimerEvent | The trigger is received from the Timer event. This value is valid only on the PXIe-5820/5840/5841/5842/5860 and for digital edge Advance Triggers on the PXIe-5663E/5665. |
| PulseIn | PulseIn | The trigger is received from the PULSE IN terminal. This value is valid only on the PXIe-5842. |
| DIO/PFI0 | DIO/PFI0 | The trigger is received on PFI 0 of the DIO front panel connector. |
| DIO/PFI1 | DIO/PFI1 | The trigger is received on PFI 1 of the DIO front panel connector. |
| DIO/PFI2 | DIO/PFI2 | The trigger is received on PFI 2 of the DIO front panel connector. |
| DIO/PFI3 | DIO/PFI3 | The trigger is received on PFI 3 of the DIO front panel connector. |
| DIO/PFI4 | DIO/PFI4 | The trigger is received on PFI 4 of the DIO front panel connector. |
| DIO/PFI5 | DIO/PFI5 | The trigger is received on PFI 5 of the DIO front panel connector. |
| DIO/PFI6 | DIO/PFI6 | The trigger is received on PFI 6 of the DIO front panel connector. |
| DIO/PFI7 | DIO/PFI7 | The trigger is received on PFI 7 of the DIO front panel connector. |

Parent topic:

RFmxDemod Properties

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=resource/objmgr/rfmxdemod-rc/rfmxdemod/attr202ffd.html language=enus -->
## TOPIC 00047: Selected Ports

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `resource/objmgr/rfmxdemod-rc/rfmxdemod/attr202ffd.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxdemod-rc/rfmxdemod/attr202ffd.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the instrument port to be configured to acquire a signal. Use RFmxInstr Get Available Ports VI to get the valid port names. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about

### Selected Ports

Specifies the instrument port to be configured to acquire a signal. Use [RFmxInstr Get Available Ports](/csh?context=rfmxinstr_rfmxinstrvi_rfmxinstr_get_available_ports) VI to get the valid port names.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

**Valid values**

| PXIe-5830 | if0, if1 |
| --- | --- |
| PXIe-5831/5832 | if0, if1, rf<0-1>/port<x>, where 0-1 indicates one (0) or two (1) mmRH-5582 connections and x is the port number on the mmRH-5582 front panel |
| Other devices | "" (empty string) |

**Default values**

| PXIe-5830/5831/5832 | if1 |
| --- | --- |
| Other devices | "" (empty string) |

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Selected Ports |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxDemod Properties

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=resource/objmgr/rfmxdemod-rc/rfmxdemod/attr202fff.html language=enus -->
## TOPIC 00048: Trigger:IQ Power Edge:Level Type

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `resource/objmgr/rfmxdemod-rc/rfmxdemod/attr202fff.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxdemod-rc/rfmxdemod/attr202fff.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the reference for the IQ Power Edge Level property. This property is used only when you set the Trigger Type property to IQ Power Edge. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for infor

### Trigger:IQ Power Edge:Level Type

Specifies the reference for the [IQ Power Edge Level](/csh?topicname=attr202008.html) property. This property is used only when you set the [Trigger Type](/csh?topicname=attr202004.html) property to **IQ Power Edge**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **Absolute**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | IQ Power Edge Level Type |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| Relative | 0 | The value of the IQ Power Edge Level property is relative to the value of the Reference Level property. |
| --- | --- | --- |
| Absolute | 1 | The IQ Power Edge Level property specifies the absolute power. |

Parent topic:

RFmxDemod Properties

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=resource/objmgr/rfmxdemod-rc/rfmxdemod/attr203000.html language=enus -->
## TOPIC 00049: Result Fetch Timeout (s)

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `resource/objmgr/rfmxdemod-rc/rfmxdemod/attr203000.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxdemod-rc/rfmxdemod/attr203000.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the time to wait before results are available in the RFmxDemod Property Node. Set this value to a time longer than expected for fetching the measurement. A value of -1 specifies that the RFmxDemod Property Node waits until the measurement is complete. This value is expressed in seconds. Yo

### Result Fetch Timeout (s)

Specifies the time to wait before results are available in the [RFmxDemod Property Node](/csh?context=rfmxdemod_rfmxdemodvi_rfmxdemod_property_node). Set this value to a time longer than expected for fetching the measurement. A value of -1 specifies that the RFmxDemod Property Node waits until the measurement is complete.
 This value is expressed in seconds.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is 10.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Result Fetch Timeout (s) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxDemod Properties

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-abort-measurements-vi.html language=enus -->
## TOPIC 00050: RFmxDemod Abort Measurements VI

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-abort-measurements-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-abort-measurements-vi.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Stops acquisition as well as the measurements that are associated with the signal instance and that were previously initiated by the RFmxDemod Initiate VI or measurement read VIs. icon Inputs/Outputs cstr.png Selector String Selector String comprises of the signal name. If you do not specify the sig

### RFmxDemod Abort Measurements VI

Stops acquisition as well as the measurements that are associated with the signal instance and that were previously initiated by the [RFmxDemod Initiate](/csh?context=rfmxdemod_rfmxdemodvi_rfmxdemod_initiate) VI or measurement read VIs.

[IMAGE alt='icon' src='rfmxdemod-abort-measurements-vi.png']

#### Inputs/Outputs

| Selector String — Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxDemod Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ademod-configure-am-carrier-suppressed-vi.html language=enus -->
## TOPIC 00051: RFmxDemod ADemod Configure AM Carrier Suppressed VI

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ademod-configure-am-carrier-suppressed-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ademod-configure-am-carrier-suppressed-vi.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the presence of the amplitude modulated (AM) carrier. icon Inputs/Outputs cstr.png Selector String Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" Y

### RFmxDemod ADemod Configure AM Carrier Suppressed VI

Configures the presence of the amplitude modulated (AM) carrier.

[IMAGE alt='icon' src='rfmxdemod-ademod-configure-am-carrier-suppressed-vi.png']

#### Inputs/Outputs

| Selector String — Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxDemod Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. AM Carrier Suppressed — AM Carrier Suppressed specifies whether the carrier of the AM signal is absent. The default value is False. False (0) The carrier of the AM signal is present. True (1) The carrier of the AM signal is absent. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| False (0) | The carrier of the AM signal is present. |
| True (1) | The carrier of the AM signal is absent. |

Parent topic:

ADemod

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ademod-configure-audio-filter-vi.html language=enus -->
## TOPIC 00052: RFmxDemod ADemod Configure Audio Filter VI

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ademod-configure-audio-filter-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ademod-configure-audio-filter-vi.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the audio filter for analog demodulation measurements. icon Inputs/Outputs cstr.png Selector String Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1"

### RFmxDemod ADemod Configure Audio Filter VI

Configures the audio filter for analog demodulation measurements.

[IMAGE alt='icon' src='rfmxdemod-ademod-configure-audio-filter-vi.png']

#### Inputs/Outputs

| Selector String — Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxDemod Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Audio Filter Type — Audio Filter Type specifies the audio filter to be applied on the analog demodulated signal. The default value is None. For more information about filter response refer to the Analog Demod topic page. None (0) Does not use any audio filter. Custom (1) Uses the filter specified by the Ademod Audio Filter Lower Cutoff property and the Ademod Audio Filter Upper Cutoff property. A - Weight (2) Uses an A-weighted filter. B - Weight (3) Uses a B-weighted filter. C - Weight (4) Uses a C-weighted filter. CCITT (5) Uses the filter specified by CCITT. ITU-R 468-4 (6) Uses the filter specified by ITU-R 468-4. Audio Filter Lower Cutoff (Hz) — Audio Filter Lower Cutoff specifies the lower cutoff frequency, in Hz, of the custom audio filter. Audio Filter Upper Cutoff (Hz) — Audio Filter Upper Cutoff specifies the upper cutoff frequency, in Hz, of the custom audio filter. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| None (0) | Does not use any audio filter. |
| Custom (1) | Uses the filter specified by the Ademod Audio Filter Lower Cutoff property and the Ademod Audio Filter Upper Cutoff property. |
| A - Weight (2) | Uses an A-weighted filter. |
| B - Weight (3) | Uses a B-weighted filter. |
| C - Weight (4) | Uses a C-weighted filter. |
| CCITT (5) | Uses the filter specified by CCITT. |
| ITU-R 468-4 (6) | Uses the filter specified by ITU-R 468-4. |

Parent topic:

ADemod

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ademod-configure-averaging-vi.html language=enus -->
## TOPIC 00053: RFmxDemod ADemod Configure Averaging VI

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ademod-configure-averaging-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ademod-configure-averaging-vi.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures averaging for analog demodulation measurements. icon Inputs/Outputs cstr.png Selector String Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can

### RFmxDemod ADemod Configure Averaging VI

Configures averaging for analog demodulation measurements.

[IMAGE alt='icon' src='rfmxdemod-ademod-configure-averaging-vi.png']

#### Inputs/Outputs

| Selector String — Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxDemod Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Averaging Enabled — Averaging Enabled enables averaging for analog demodulation measurement. False (0) The measurement is performed on a single acquisition. True (1) The measurement uses the value of the Averaging Count parameter for the number of acquisitions over which the measurement is averaged. The traces are not averaged. Averaging Count — Averaging Count specifies the number of acquisitions used for averaging when you set the Averaging Enabled parameter to True. Averaging Type — Averaging Type specifies the averaging type for the measurement. Linear (0) The averaged result is the mean value measured across multiple acquisitions. Max (1) The averaged result is the maximum value measured across multiple acquisitions. Min (2) The averaged result is the minimum value measured across multiple acquisitions. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| False (0) | The measurement is performed on a single acquisition. |
| True (1) | The measurement uses the value of the Averaging Count parameter for the number of acquisitions over which the measurement is averaged. The traces are not averaged. |
| Linear (0) | The averaged result is the mean value measured across multiple acquisitions. |
| Max (1) | The averaged result is the maximum value measured across multiple acquisitions. |
| Min (2) | The averaged result is the minimum value measured across multiple acquisitions. |

Parent topic:

ADemod

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ademod-configure-carrier-correction-vi.html language=enus -->
## TOPIC 00054: RFmxDemod ADemod Configure Carrier Correction VI

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ademod-configure-carrier-correction-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ademod-configure-carrier-correction-vi.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the carrier correction in analog demodulation measurements. icon Inputs/Outputs cstr.png Selector String Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::s

### RFmxDemod ADemod Configure Carrier Correction VI

Configures the carrier correction in analog demodulation measurements.

[IMAGE alt='icon' src='rfmxdemod-ademod-configure-carrier-correction-vi.png']

#### Inputs/Outputs

| Selector String — Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxDemod Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Carrier Frequency Correction Enabled — Carrier Frequency Correction Enabled specifies whether to correct the frequency error in the carrier when demodulating frequency-modulated or phase-modulated signals. The default value is True. False (0) Does not correct the carrier frequency error. True (1) Corrects the carrier frequency error. Carrier Phase Correction Enabled — Carrier Phase Correction Enabled specifies whether to correct the phase error in the carrier when demodulating phase-modulated signals. The default value is True. False (0) Does not correct the carrier phase error. True (1) Corrects the carrier phase error. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| False (0) | Does not correct the carrier frequency error. |
| True (1) | Corrects the carrier frequency error. |
| False (0) | Does not correct the carrier phase error. |
| True (1) | Corrects the carrier phase error. |

Parent topic:

ADemod

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ademod-configure-fm-deemphasis-vi.html language=enus -->
## TOPIC 00055: RFmxDemod ADemod Configure FM DeEmphasis VI

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ademod-configure-fm-deemphasis-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ademod-configure-fm-deemphasis-vi.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the FM de-emphasis filter for analog demodulation measurements. icon Inputs/Outputs cstr.png Selector String Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signa

### RFmxDemod ADemod Configure FM DeEmphasis VI

Configures the FM de-emphasis filter for analog demodulation measurements.

[IMAGE alt='icon' src='rfmxdemod-ademod-configure-fm-deemphasis-vi.png']

#### Inputs/Outputs

| Selector String — Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxDemod Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. FM DeEmphasis (s) — FM DeEmphasis specifies the time constant, in seconds, of the de-emphasis filter, which compensates for the pre-emphasis filter in the FM transmitter. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

ADemod

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ademod-configure-measurement-interval-vi.html language=enus -->
## TOPIC 00056: RFmxDemod ADemod Configure Measurement Interval VI

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ademod-configure-measurement-interval-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ademod-configure-measurement-interval-vi.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the measurement interval for analog demodulation measurements. icon Inputs/Outputs cstr.png Selector String Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal

### RFmxDemod ADemod Configure Measurement Interval VI

Configures the measurement interval for analog demodulation measurements.

[IMAGE alt='icon' src='rfmxdemod-ademod-configure-measurement-interval-vi.png']

#### Inputs/Outputs

| Selector String — Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxDemod Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Measurement Interval (s) — Measurement Interval specifies the signal acquisition time, in seconds, for the analog demodulation measurement. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

ADemod

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ademod-configure-modulation-type-vi.html language=enus -->
## TOPIC 00057: RFmxDemod ADemod Configure Modulation Type VI

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ademod-configure-modulation-type-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ademod-configure-modulation-type-vi.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the modulation type for analog demodulation measurements. icon Inputs/Outputs cstr.png Selector String Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig

### RFmxDemod ADemod Configure Modulation Type VI

Configures the modulation type for analog demodulation measurements.

[IMAGE alt='icon' src='rfmxdemod-ademod-configure-modulation-type-vi.png']

#### Inputs/Outputs

| Selector String — Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxDemod Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Modulation Type — Modulation Type specifies the analog modulation type of the signal that needs to be analyzed. The default value is AM. AM (0) The signal to be analyzed is amplitude modulated. FM (1) The signal to be analyzed is frequency modulated. PM (2) The signal to be analyzed is phase modulated. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| AM (0) | The signal to be analyzed is amplitude modulated. |
| FM (1) | The signal to be analyzed is frequency modulated. |
| PM (2) | The signal to be analyzed is phase modulated. |

Parent topic:

ADemod

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ademod-configure-rbw-filter-vi.html language=enus -->
## TOPIC 00058: RFmxDemod ADemod Configure RBW Filter VI

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ademod-configure-rbw-filter-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ademod-configure-rbw-filter-vi.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the resolution bandwidth (RBW) filter for analog demodulation measurements. icon Inputs/Outputs cstr.png Selector String Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Exampl

### RFmxDemod ADemod Configure RBW Filter VI

Configures the resolution bandwidth (RBW) filter for analog demodulation measurements.

[IMAGE alt='icon' src='rfmxdemod-ademod-configure-rbw-filter-vi.png']

#### Inputs/Outputs

| Selector String — Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxDemod Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. RBW (Hz) — RBW specifies the bandwidth, in Hz, of the resolution bandwidth (RBW) filter to be applied to the acquired signal. RBW Filter Type — RBW Filter Type specifies the shape of the digital RBW filter. None (0) RBW filter is not applied on the acquired signal. Gaussian (1) RBW filter has a Gaussian response. Flat (2) RBW filter has a Flat response. Synch Tuned - 4 (3) RBW filter has a response of a 4-pole synchronously-tuned filter. Synch Tuned - 5 (4) RBW filter has a response of a 5-pole synchronously-tuned filter. RRC (5) RRC filter with roll-off specified by the ADemod RBW RRC Alpha property is used as the RBW filter. RBW RRC Alpha — RBW RRC Alpha specifies the roll-off factor of the root-raised cosine (RRC) filter. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| None (0) | RBW filter is not applied on the acquired signal. |
| Gaussian (1) | RBW filter has a Gaussian response. |
| Flat (2) | RBW filter has a Flat response. |
| Synch Tuned - 4 (3) | RBW filter has a response of a 4-pole synchronously-tuned filter. |
| Synch Tuned - 5 (4) | RBW filter has a response of a 5-pole synchronously-tuned filter. |
| RRC (5) | RRC filter with roll-off specified by the ADemod RBW RRC Alpha property is used as the RBW filter. |

Parent topic:

ADemod

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ademod-fetch-am-maximum-modulation-depth-vi.html language=enus -->
## TOPIC 00059: RFmxDemod ADemod Fetch AM Maximum Modulation Depth VI

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ademod-fetch-am-maximum-modulation-depth-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ademod-fetch-am-maximum-modulation-depth-vi.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the AM maximum modulation depth. icon Inputs/Outputs cstr.png Selector String Selector String comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The

### RFmxDemod ADemod Fetch AM Maximum Modulation Depth VI

Fetches the AM maximum modulation depth.

[IMAGE alt='icon' src='rfmxdemod-ademod-fetch-am-maximum-modulation-depth-vi.png']

#### Inputs/Outputs

| Selector String — Selector String comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxDemod Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. This value is expressed in seconds. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Maximum Negative Peak (%) — Maximum Negative Peak returns the maximum negative peak amplitude, as a percentage, of the modulating signal measured across multiple acquisitions. Maximum Positive Peak (%) — Maximum Positive Peak returns the maximum positive peak amplitude, as a percentage, of the modulating signal measured across multiple acquisitions. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Maximum Modulation Depth (%) — Maximum Modulation Depth returns the maximum modulation depth, as a percentage, measured across multiple acquisitions. Maximum Peak to Peak /2 (%) — Maximum Peak to Peak /2 returns the maximum (peak-to-peak)/2 amplitude, as a percentage, of the modulating signal measured across multiple acquisitions. Maximum RMS (%) — Maximum RMS returns the maximum RMS amplitude, as a percentage, of the modulating signal measured across multiple acquisitions. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxDemod ADemod Fetch VI

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ademod-fetch-am-mean-modulation-depth-vi.html language=enus -->
## TOPIC 00060: RFmxDemod ADemod Fetch AM Mean Modulation Depth VI

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ademod-fetch-am-mean-modulation-depth-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ademod-fetch-am-mean-modulation-depth-vi.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches AM mean modulation depth for analog demodulation measurements. icon Inputs/Outputs cstr.png Selector String Selector String comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the defaul

### RFmxDemod ADemod Fetch AM Mean Modulation Depth VI

Fetches AM mean modulation depth for analog demodulation measurements.

[IMAGE alt='icon' src='rfmxdemod-ademod-fetch-am-mean-modulation-depth-vi.png']

#### Inputs/Outputs

| Selector String — Selector String comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxDemod Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. This value is expressed in seconds. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Mean Negative Peak (%) — Mean Negative Peak returns the mean negative peak amplitude, as a percentage, of the modulating signal. Mean Positive Peak (%) — Mean Positive Peak returns the mean positive peak amplitude, as a percentage, of the modulating signal. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Mean Modulation Depth (%) — Mean Modulation Depth returns the mean amplitude variation, as a percentage, around the unmodulated carrier amplitude. If the carrier is suppressed, the amplitude variation of the modulating signal is returned. Mean Peak to Peak /2 (%) — Mean Peak to Peak /2 returns the mean (peak-to-peak)/2 amplitude, as a percentage, of the modulating signal. Mean RMS (%) — Mean RMS returns the mean RMS amplitude of the modulating signal. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxDemod ADemod Fetch VI

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ademod-fetch-carrier-measurement-vi.html language=enus -->
## TOPIC 00061: RFmxDemod ADemod Fetch Carrier Measurement VI

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ademod-fetch-carrier-measurement-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ademod-fetch-carrier-measurement-vi.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the carrier measurement. icon Inputs/Outputs cstr.png Selector String Selector String comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default

### RFmxDemod ADemod Fetch Carrier Measurement VI

Fetches the carrier measurement.

[IMAGE alt='icon' src='rfmxdemod-ademod-fetch-carrier-measurement-vi.png']

#### Inputs/Outputs

| Selector String — Selector String comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxDemod Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. This value is expressed in seconds. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Mean Carrier Frequency Error (Hz) — Mean Carrier Frequency Error returns the mean of the measured carrier frequency error, in Hz. Mean Carrier Power (dBm) — Mean Carrier Power returns the mean of the measured carrier power, in dBm. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxDemod ADemod Fetch VI

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ademod-fetch-demod-signal-trace-vi.html language=enus -->
## TOPIC 00062: RFmxDemod ADemod Fetch Demod Signal Trace VI

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ademod-fetch-demod-signal-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ademod-fetch-demod-signal-trace-vi.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the demodulated signal trace. icon Inputs/Outputs cstr.png Selector String Selector String comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The de

### RFmxDemod ADemod Fetch Demod Signal Trace VI

Fetches the demodulated signal trace.

[IMAGE alt='icon' src='rfmxdemod-ademod-fetch-demod-signal-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxDemod Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. This value is expressed in seconds. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Demodulated Signal (% or Hz or degrees) — Demodulated Signal returns the demodulated signal. x0 — x0 returns the start time, in seconds. dx — dx returns the sample duration, in seconds. y — y returns the signal amplitude in % for AM, Hz for FM, degrees for PM signals, at each time instance. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| x0 — x0 returns the start time, in seconds. dx — dx returns the sample duration, in seconds. y — y returns the signal amplitude in % for AM, Hz for FM, degrees for PM signals, at each time instance. |

Parent topic:

RFmxDemod ADemod Fetch VI

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ademod-fetch-demod-spectrum-trace-vi.html language=enus -->
## TOPIC 00063: RFmxDemod ADemod Fetch Demod Spectrum Trace VI

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ademod-fetch-demod-spectrum-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ademod-fetch-demod-spectrum-trace-vi.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the demodulated signal spectrum trace. icon Inputs/Outputs cstr.png Selector String Selector String comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is use

### RFmxDemod ADemod Fetch Demod Spectrum Trace VI

Fetches the demodulated signal spectrum trace.

[IMAGE alt='icon' src='rfmxdemod-ademod-fetch-demod-spectrum-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxDemod Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. This value is expressed in seconds. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Demodulated Spectrum (% or Hz or degrees) — Demodulated Spectrum returns the demodulated signal spectrum. x0 — x0 returns the start bin frequency, in Hz. dx — dx returns the frequency bin spacing, in Hz. y — y returns the amplitude, as a percentage for AM, in Hz for FM, and in degrees for PM signals, measured at each frequency bin. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| x0 — x0 returns the start bin frequency, in Hz. dx — dx returns the frequency bin spacing, in Hz. y — y returns the amplitude, as a percentage for AM, in Hz for FM, and in degrees for PM signals, measured at each frequency bin. |

Parent topic:

RFmxDemod ADemod Fetch VI

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ademod-fetch-distortions-vi.html language=enus -->
## TOPIC 00064: RFmxDemod ADemod Fetch Distortions VI

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ademod-fetch-distortions-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ademod-fetch-distortions-vi.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches distortions for analog demodulation measurements. icon Inputs/Outputs cstr.png Selector String Selector String comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result inst

### RFmxDemod ADemod Fetch Distortions VI

Fetches distortions for analog demodulation measurements.

[IMAGE alt='icon' src='rfmxdemod-ademod-fetch-distortions-vi.png']

#### Inputs/Outputs

| Selector String — Selector String comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxDemod Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. This value is expressed in seconds. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Average THD with Noise (%) — Average THD with Noise returns the averaged total harmonic distortion with noise, as a percentage, of the demodulated signal. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Average SINAD (dB) — Average SINAD returns the averaged signal-to-noise and distortion ratio, in dB, of the demodulated signal. Average SNR (dB) — Average SNR returns the averaged signal-to-noise ratio, in dB, of the demodulated signal. Average THD (%) — Average THD returns the averaged total harmonic distortion, as a percentage, of demodulated signal. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxDemod ADemod Fetch VI

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ademod-fetch-fm-maximum-deviation-vi.html language=enus -->
## TOPIC 00065: RFmxDemod ADemod Fetch FM Maximum Deviation VI

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ademod-fetch-fm-maximum-deviation-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ademod-fetch-fm-maximum-deviation-vi.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the FM maximum deviation measurements. icon Inputs/Outputs cstr.png Selector String Selector String comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is use

### RFmxDemod ADemod Fetch FM Maximum Deviation VI

Fetches the FM maximum deviation measurements.

[IMAGE alt='icon' src='rfmxdemod-ademod-fetch-fm-maximum-deviation-vi.png']

#### Inputs/Outputs

| Selector String — Selector String comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxDemod Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. This value is expressed in seconds. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Maximum Negative Peak (Hz) — Maximum Negative Peak returns the maximum negative peak frequency deviation, in Hz, of the frequency-modulated signal measured across multiple acquisitions. Maximum Positive Peak (Hz) — Maximum Positive Peak returns the maximum positive peak frequency deviation, in Hz, of the frequency-modulated signal measured across multiple acquisitions. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Maximum Deviation (Hz) — Maximum Deviation returns the maximum frequency deviation, in Hz, of the frequency-modulated signal measured across multiple acquisitions. Maximum Peak to Peak /2 (Hz) — Maximum Peak to Peak /2 returns the maximum (peak-to-peak)/2 frequency variation, in Hz, around the nominal frequency of the FM carrier measured across multiple acquisitions. Maximum RMS (Hz) — Maximum RMS returns the maximum RMS frequency deviation, in Hz, of the frequency-modulated signal measured across multiple acquisitions. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxDemod ADemod Fetch VI

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ademod-fetch-fm-mean-deviation-vi.html language=enus -->
## TOPIC 00066: RFmxDemod ADemod Fetch FM Mean Deviation VI

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ademod-fetch-fm-mean-deviation-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ademod-fetch-fm-mean-deviation-vi.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the FM mean deviation measurements. icon Inputs/Outputs cstr.png Selector String Selector String comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used.

### RFmxDemod ADemod Fetch FM Mean Deviation VI

Fetches the FM mean deviation measurements.

[IMAGE alt='icon' src='rfmxdemod-ademod-fetch-fm-mean-deviation-vi.png']

#### Inputs/Outputs

| Selector String — Selector String comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxDemod Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. This value is expressed in seconds. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Mean Negative Peak (Hz) — Mean Negative Peak returns the mean negative peak frequency deviation of the frequency-modulated signal. Mean Positive Peak (Hz) — Mean Positive Peak returns the mean positive peak frequency deviation, in Hz, of the frequency-modulated signal. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Mean Deviation (Hz) — Mean Deviation returns the mean deviation, in Hz, of the frequency-modulated signal. Mean Peak to Peak /2 (Hz) — Mean Peak to Peak /2 returns the mean (peak-to-peak)/2 frequency variation, in Hz, around the nominal frequency of the FM carrier. Mean RMS (Hz) — Mean RMS returns the mean RMS frequency deviation, in Hz, of the frequency-modulated signal. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxDemod ADemod Fetch VI

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ademod-fetch-mean-modulation-frequency-vi.html language=enus -->
## TOPIC 00067: RFmxDemod ADemod Fetch Mean Modulation Frequency VI

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ademod-fetch-mean-modulation-frequency-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ademod-fetch-mean-modulation-frequency-vi.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the mean modulation frequency. icon Inputs/Outputs cstr.png Selector String Selector String comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The d

### RFmxDemod ADemod Fetch Mean Modulation Frequency VI

Fetches the mean modulation frequency.

[IMAGE alt='icon' src='rfmxdemod-ademod-fetch-mean-modulation-frequency-vi.png']

#### Inputs/Outputs

| Selector String — Selector String comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxDemod Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. This value is expressed in seconds. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Mean Modulation Frequency (Hz) — Mean Modulation Frequency returns the mean of the demodulated signal frequency. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxDemod ADemod Fetch VI

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ademod-fetch-pm-maximum-deviation-vi.html language=enus -->
## TOPIC 00068: RFmxDemod ADemod Fetch PM Maximum Deviation VI

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ademod-fetch-pm-maximum-deviation-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ademod-fetch-pm-maximum-deviation-vi.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the PM maximum deviation measurements. icon Inputs/Outputs cstr.png Selector String Selector String comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is use

### RFmxDemod ADemod Fetch PM Maximum Deviation VI

Fetches the PM maximum deviation measurements.

[IMAGE alt='icon' src='rfmxdemod-ademod-fetch-pm-maximum-deviation-vi.png']

#### Inputs/Outputs

| Selector String — Selector String comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxDemod Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. This value is expressed in seconds. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Maximum Negative Peak (deg) — Maximum Negative Peak returns the maximum negative peak phase deviation, in degrees, around the unmodulated carrier phase, measured across multiple acquisitions. Maximum Positive Peak (deg) — Maximum Positive Peak returns the maximum positive peak phase deviation, in degrees, around the unmodulated carrier phase, measured across multiple acquisitions. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Maximum Deviation (deg) — Maximum Deviation returns the maximum phase deviation, in degrees, around the unmodulated carrier phase measured over multiple acquisitions. Maximum Peak to Peak /2 (deg) — Maximum Peak to Peak /2 returns the maximum (peak to peak)/2 phase deviation, in degrees, around the unmodulated carrier phase measured over multiple acquisitions. Maximum RMS (deg) — Maximum RMS returns the maximum RMS phase deviation, in degrees, of the PM signal measured over multiple acquisitions. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxDemod ADemod Fetch VI

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ademod-fetch-pm-mean-deviation-vi.html language=enus -->
## TOPIC 00069: RFmxDemod ADemod Fetch PM Mean Deviation VI

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ademod-fetch-pm-mean-deviation-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ademod-fetch-pm-mean-deviation-vi.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the PM mean deviation measurements. icon Inputs/Outputs cstr.png Selector String Selector String comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used.

### RFmxDemod ADemod Fetch PM Mean Deviation VI

Fetches the PM mean deviation measurements.

[IMAGE alt='icon' src='rfmxdemod-ademod-fetch-pm-mean-deviation-vi.png']

#### Inputs/Outputs

| Selector String — Selector String comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxDemod Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. This value is expressed in seconds. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Mean Negative Peak (deg) — Mean Negative Peak returns the mean negative peak phase deviation, in degrees, around the unmodulated carrier phase. Mean Positive Peak (deg) — Mean Positive Peak returns the mean positive peak phase deviation, in degrees, around the unmodulated carrier phase. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Mean Deviation (deg) — Mean Deviation returns the mean deviation around the unmodulated carrier phase. Mean Peak to Peak /2 (deg) — Mean Peak to Peak /2 returns the mean (peak-to-peak)/2 phase deviation, in degrees, around the unmodulated carrier phase. Mean RMS (deg) — Mean RMS returns the mean RMS phase deviation, in degrees, of the phase-modulated signal. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxDemod ADemod Fetch VI

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ademod-fetch-vi.html language=enus -->
## TOPIC 00070: RFmxDemod ADemod Fetch VI

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ademod-fetch-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ademod-fetch-vi.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the analog demodulation measurements. icon

### RFmxDemod ADemod Fetch VI

Fetches the analog demodulation measurements.

[IMAGE alt='icon' src='rfmxdemod-ademod-fetch-vi.png']

- [RFmxDemod ADemod Fetch Carrier Measurement VI](../../../../../vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ademod-fetch-carrier-measurement-vi.html) Fetches the carrier measurement.
- [RFmxDemod ADemod Fetch Mean Modulation Frequency VI](../../../../../vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ademod-fetch-mean-modulation-frequency-vi.html) Fetches the mean modulation frequency.
- [RFmxDemod ADemod Fetch Distortions VI](../../../../../vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ademod-fetch-distortions-vi.html) Fetches distortions for analog demodulation measurements.
- [RFmxDemod ADemod Fetch AM Mean Modulation Depth VI](../../../../../vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ademod-fetch-am-mean-modulation-depth-vi.html) Fetches AM mean modulation depth for analog demodulation measurements.
- [RFmxDemod ADemod Fetch FM Mean Deviation VI](../../../../../vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ademod-fetch-fm-mean-deviation-vi.html) Fetches the FM mean deviation measurements.
- [RFmxDemod ADemod Fetch PM Mean Deviation VI](../../../../../vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ademod-fetch-pm-mean-deviation-vi.html) Fetches the PM mean deviation measurements.
- [RFmxDemod ADemod Fetch AM Maximum Modulation Depth VI](../../../../../vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ademod-fetch-am-maximum-modulation-depth-vi.html) Fetches the AM maximum modulation depth.
- [RFmxDemod ADemod Fetch FM Maximum Deviation VI](../../../../../vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ademod-fetch-fm-maximum-deviation-vi.html) Fetches the FM maximum deviation measurements.
- [RFmxDemod ADemod Fetch PM Maximum Deviation VI](../../../../../vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ademod-fetch-pm-maximum-deviation-vi.html) Fetches the PM maximum deviation measurements.
- [RFmxDemod ADemod Fetch Demod Signal Trace VI](../../../../../vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ademod-fetch-demod-signal-trace-vi.html) Fetches the demodulated signal trace.
- [RFmxDemod ADemod Fetch Demod Spectrum Trace VI](../../../../../vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ademod-fetch-demod-spectrum-trace-vi.html) Fetches the demodulated signal spectrum trace.

Parent topic:

Fetch

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ademod-read-am-vi.html language=enus -->
## TOPIC 00071: RFmxDemod ADemod Read AM VI

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ademod-read-am-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ademod-read-am-vi.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures hardware for acquisition, performs measurement on acquired data, and returns the AM measurement results. icon Inputs/Outputs cstr.png Selector String Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value

### RFmxDemod ADemod Read AM VI

Configures hardware for acquisition, performs measurement on acquired data, and returns the AM measurement results.

[IMAGE alt='icon' src='rfmxdemod-ademod-read-am-vi.png']

#### Inputs/Outputs

| Selector String — Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxDemod Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. This value is expressed in seconds. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Mean Modulation Depth (%) — Mean Modulation Depth returns the mean amplitude variation, as a percentage, around the unmodulated carrier amplitude. If the carrier is suppressed, the amplitude variation of the modulating signal is returned. Mean Carrier Power (dBm) — Mean Carrier Power returns the mean of the measured carrier power, in dBm. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxDemod Read VI

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ademod-read-fm-vi.html language=enus -->
## TOPIC 00072: RFmxDemod ADemod Read FM VI

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ademod-read-fm-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ademod-read-fm-vi.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures hardware for acquisition, performs measurement on acquired data, and returns the FM measurement results. icon Inputs/Outputs cstr.png Selector String Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value

### RFmxDemod ADemod Read FM VI

Configures hardware for acquisition, performs measurement on acquired data, and returns the FM measurement results.

[IMAGE alt='icon' src='rfmxdemod-ademod-read-fm-vi.png']

#### Inputs/Outputs

| Selector String — Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxDemod Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. This value is expressed in seconds. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Mean Deviation (Hz) — Mean Deviation returns the mean frequency deviation, in Hz, around the nominal frequency of the FM carrier. Mean Carrier Frequency Error (Hz) — Mean Carrier Frequency Error returns the mean of the measured carrier frequency error, in Hz. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxDemod Read VI

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ademod-read-pm-vi.html language=enus -->
## TOPIC 00073: RFmxDemod ADemod Read PM VI

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ademod-read-pm-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ademod-read-pm-vi.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures hardware for acquisition, performs measurement on acquired data, and returns the PM measurement results. icon Inputs/Outputs cstr.png Selector String Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value

### RFmxDemod ADemod Read PM VI

Configures hardware for acquisition, performs measurement on acquired data, and returns the PM measurement results.

[IMAGE alt='icon' src='rfmxdemod-ademod-read-pm-vi.png']

#### Inputs/Outputs

| Selector String — Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxDemod Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. This value is expressed in seconds. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Mean Deviation (deg) — Mean Deviation returns the mean phase deviation, in degrees, of a phase modulated signal. Mean Carrier Frequency Error (Hz) — Mean Carrier Frequency Error returns the mean of the measured carrier frequency error, in Hz. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxDemod Read VI

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-analyze-iq-1-wfm-vi.html language=enus -->
## TOPIC 00074: RFmxDemod Analyze (IQ, 1 Wfm) VI

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-analyze-iq-1-wfm-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-analyze-iq-1-wfm-vi.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs the enabled measurements on the I/Q complex waveform that you specify in IQ parameter. Call this VI after you configure the signal and measurement properties. You can fetch measurement results using the Fetch VIs or result properties in the property node. Use this VI only if the Recommended

### RFmxDemod Analyze (IQ, 1 Wfm) VI

Performs the enabled measurements on the I/Q complex waveform that you specify in **IQ** parameter. Call this VI after you configure the signal and measurement properties. You can fetch measurement results using the Fetch VIs or result properties in the property node.
Use this VI only if the [Recommended Acquisition Type](/csh?context=rfmxinstr_rfmxinstrprop_attr27) property value is **IQ**.

Note

RFmxInstr Property Node

RFmxDemod Commit

[IMAGE alt='icon' src='rfmxdemod-analyze-iq-1-wfm-vi.png']

#### Inputs/Outputs

| Result Name — Result Name specifies the name to be associated with measurement results. Provide a unique name, such as "r1" to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. The default value is "" (empty string) which refers to default result instance. Example: "result::r1" "r1" Selector String — Selector String specifies a selector string comprising of the signal name and result name. The result name can either be specified through this input or the Result Name parameter. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name in this input, either the result name specified by Result Name parameter or the default result instance is used. The default is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxDemod Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize VI with option string as "AnalysisOnly=1". IQ — IQ specifies the data for a complex waveform including the start, delta, and actual values. x0 — x0 specifies the start time of the input Y array. This value is expressed in seconds. dx — dx specifies the time interval between the samples in the input Y array. This value is expressed in seconds. The reciprocal of dx indicates the I/Q rate of the input signal. y — y specifies an array of complex-valued time domain data. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively. Reset? — Reset? resets measurement averaging. If you enable averaging, set this parameter to TRUE for first record and FALSE for subsequent records. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Selector String Out — Selector String Out returns the selector string that can be passed to the Selector String parameter of Configure, Initiate, and Fetch VIs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| x0 — x0 specifies the start time of the input Y array. This value is expressed in seconds. dx — dx specifies the time interval between the samples in the input Y array. This value is expressed in seconds. The reciprocal of dx indicates the I/Q rate of the input signal. y — y specifies an array of complex-valued time domain data. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively. |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-auto-level-vi.html language=enus -->
## TOPIC 00075: RFmxDemod Auto Level VI

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-auto-level-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-auto-level-vi.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Examines the input signal to calculate the peak power level and sets it as the value of the Reference Level property. Use this VI to help calculate an approximate setting for the reference level. The RFmxDemod Auto Level VI does the following tasks: Resets the mixer level, mixer level offset, and IF

### RFmxDemod Auto Level VI

Examines the input signal to calculate the peak power level and sets it as the value of the [Reference Level](/csh?context=rfmxdemod_rfmxdemodprop_attr202003) property. Use this VI to help calculate an approximate setting for the reference level.

The RFmxDemod Auto Level VI does the following tasks:

1. Resets the mixer level, mixer level offset, and IF output power level offset.
2. Sets the starting reference level to the maximum reference level supported by the device based on the current RF attenuation, mechanical attenuation, and preamp enabled settings.
3. Iterates to adjust the reference level based on the input signal peak power.
4. Uses immediate triggering and restores the trigger settings back to user setting after the execution.

You can also specify the starting reference level using the [Auto Level Initial Ref Level](/csh?context=rfmxdemod_rfmxdemodprop_attr20200d) property.

When using NI 5663, 5665, or 5668R devices, NI recommends that you set an appropriate value for mechanical attenuation before calling the RFmxDemod Auto Level VI. Setting an appropriate value for mechanical attenuation reduces the number of times the attenuator settings are changed by this function; thus reducing wear and tear, and maximizing the life time of the attenuator.

[IMAGE alt='icon' src='rfmxdemod-auto-level-vi.png']

#### Inputs/Outputs

| Selector String — Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxDemod Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Bandwidth (Hz) — Bandwidth specifies the bandwidth, in Hz, of the signal to be analyzed. Measurement Interval (s) — Measurement Interval specifies the acquisition length. This value is used to compute the number of samples to acquire from the signal analyzer. This value is expressed in seconds. The default value is 10 ms. Auto Level VI does not use any trigger for acquisition. It ignores the user-configured trigger properties. NI recommends that you set a sufficiently high measurement interval to ensure that the acquired waveform is at least as long as one period of the signal. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Reference Level — Reference Level returns the estimated peak power level of the input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-build-signal-string-vi.html language=enus -->
## TOPIC 00076: RFmxDemod Build Signal String VI

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-build-signal-string-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-build-signal-string-vi.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a selector string for use with Configuration or Fetch properties and VIs. icon Inputs/Outputs cstr.png Result Name Result Name specifies the result name for building the selector string. This input accepts the result name with or without the "result::" prefix. The default value is "" (empty

### RFmxDemod Build Signal String VI

Creates a selector string for use with Configuration or Fetch properties and VIs.

[IMAGE alt='icon' src='rfmxdemod-build-signal-string-vi.png']

#### Inputs/Outputs

| Result Name — Result Name specifies the result name for building the selector string. This input accepts the result name with or without the "result::" prefix. The default value is "" (empty string). Example: "" "result::r1" "r1" Signal Name — Signal Name specifies the signal name for building the selector string. This input accepts the signal name with or without the "signal::" prefix. The default value is "" (empty string). Example: "" "signal::sig1" "sig1" Selector String — Selector String returns the selector string created by this VI. |
| --- |

Parent topic:

Build String

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-check-measurement-status-vi.html language=enus -->
## TOPIC 00077: RFmxDemod Check Measurement Status VI

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-check-measurement-status-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-check-measurement-status-vi.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Checks the status of the measurement. Use this VI to check for any errors that may occur during measurement or to check whether the measurement is complete and results are available. icon Inputs/Outputs cstr.png Selector String Selector String comprises the signal name and result name. If you do not

### RFmxDemod Check Measurement Status VI

Checks the status of the measurement. Use this VI to check for any errors that may occur during measurement or to check whether the measurement is complete and results are available.

[IMAGE alt='icon' src='rfmxdemod-check-measurement-status-vi.png']

#### Inputs/Outputs

| Selector String — Selector String comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxDemod Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. done? — done? indicates whether the measurement is complete. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-clear-all-named-results-vi.html language=enus -->
## TOPIC 00078: RFmxDemod Clear All Named Results VI

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-clear-all-named-results-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-clear-all-named-results-vi.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Clears all results for the signal that you specify in the Selector String parameter. icon Inputs/Outputs cstr.png Selector String Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example:

### RFmxDemod Clear All Named Results VI

Clears all results for the signal that you specify in the **Selector String** parameter.

[IMAGE alt='icon' src='rfmxdemod-clear-all-named-results-vi.png']

#### Inputs/Outputs

| Selector String — Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxDemod Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-clear-named-result-vi.html language=enus -->
## TOPIC 00079: RFmxDemod Clear Named Result VI

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-clear-named-result-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-clear-named-result-vi.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Clears an instance of the result that you specify in the Selector String parameter. icon Inputs/Outputs cstr.png Selector String Selector String comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result nam

### RFmxDemod Clear Named Result VI

Clears an instance of the result that you specify in the **Selector String** parameter.

[IMAGE alt='icon' src='rfmxdemod-clear-named-result-vi.png']

#### Inputs/Outputs

| Selector String — Selector String comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxDemod Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-clone-signal-configuration-vi.html language=enus -->
## TOPIC 00080: RFmxDemod Clone Signal Configuration VI

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-clone-signal-configuration-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-clone-signal-configuration-vi.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a new instance of a signal by copying all the property values from an existing signal instance. icon Inputs/Outputs cstr.png Old Signal Name Old Signal Name specifies the name of the existing signal. This parameter accepts the signal name with or without the "signal::" prefix. Example: "sign

### RFmxDemod Clone Signal Configuration VI

Creates a new instance of a signal by copying all the property values from an existing signal instance.

[IMAGE alt='icon' src='rfmxdemod-clone-signal-configuration-vi.png']

#### Inputs/Outputs

| Old Signal Name — Old Signal Name specifies the name of the existing signal. This parameter accepts the signal name with or without the "signal::" prefix. Example: "signal::OldSigName" "OldSigName" Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. New Signal Name — New Signal Name specifies the name of the new signal. This parameter accepts the signal name with or without the "signal::" prefix. Example: "signal::NewSigName" "NewSigName" error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Selector String Out — Selector String Out returns the selector string that can be passed to the Selector String parameter on Configure, Initiate, and Fetch VIs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-commit-vi.html language=enus -->
## TOPIC 00081: RFmxDemod Commit VI

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-commit-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-commit-vi.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Commits settings to the hardware. Calling this VI is optional. RFmxDemod commits settings to the hardware when you call the RFmxDemod Initiate VI or any of the measurement Read VIs. icon Inputs/Outputs cstr.png Selector String Selector String comprises of the signal name. If you do not specify the s

### RFmxDemod Commit VI

Commits settings to the hardware. Calling this VI is optional. RFmxDemod commits settings to the hardware when you call the [RFmxDemod Initiate](/csh?context=rfmxdemod_rfmxdemodvi_rfmxdemod_initiate) VI or any of the measurement Read VIs.

[IMAGE alt='icon' src='rfmxdemod-commit-vi.png']

#### Inputs/Outputs

| Selector String — Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxDemod Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-configure-digital-edge-trigger-vi.html language=enus -->
## TOPIC 00082: RFmxDemod Configure Digital Edge Trigger VI

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-configure-digital-edge-trigger-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-configure-digital-edge-trigger-vi.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the digital edge trigger. icon Inputs/Outputs cbool.png Enable Trigger? Enable Trigger? specifies whether to enable the trigger. The default value is TRUE. cstr.png Selector String Selector String comprises of the signal name. If you do not specify the signal name, the default signal inst

### RFmxDemod Configure Digital Edge Trigger VI

Configures the digital edge trigger.

[IMAGE alt='icon' src='rfmxdemod-configure-digital-edge-trigger-vi.png']

#### Inputs/Outputs

| Enable Trigger? — Enable Trigger? specifies whether to enable the trigger. The default value is TRUE. Selector String — Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxDemod Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Digital Edge Source — Digital Edge Source specifies the source terminal for the digital-edge trigger. This parameter is used only when you set the Trigger Type property to Digital Edge. The default value is PFI0. PFI0 (PFI0) The trigger is received on PFI 0. PFI1 (PFI1) The trigger is received on PFI 1. PXI_Trig0 (PXI_Trig0) The trigger is received on PXI trigger line 0. PXI_Trig1 (PXI_Trig1) The trigger is received on PXI trigger line 1. PXI_Trig2 (PXI_Trig2) The trigger is received on PXI trigger line 2. PXI_Trig3 (PXI_Trig3) The trigger is received on PXI trigger line 3. PXI_Trig4 (PXI_Trig4) The trigger is received on PXI trigger line 4. PXI_Trig5 (PXI_Trig5) The trigger is received on PXI trigger line 5. PXI_Trig6 (PXI_Trig6) The trigger is received on PXI trigger line 6. PXI_Trig7 (PXI_Trig7) The trigger is received on PXI trigger line 7. PXI_STAR (PXI_STAR) The trigger is received on the PXI star trigger line. PXIe_DStarB (PXIe_DStarB) The trigger is received on the PXIe DStar B trigger line. TimerEvent (TimerEvent) The trigger is received from the Timer Event. Digital Edge — Digital Edge specifies whether the signal analyzer detects a rising or falling edge on the digital-edge trigger signal. The parameter is used only when you set the Trigger Type property to Digital Edge. The default value is Rising Edge. Rising Edge (0) The trigger asserts on the rising edge of the signal. Falling Edge (1) The trigger asserts on the falling edge of the signal. Trigger Delay (s) — Trigger Delay specifies the trigger delay time, in seconds. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
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
| Rising Edge (0) | The trigger asserts on the rising edge of the signal. |
| Falling Edge (1) | The trigger asserts on the falling edge of the signal. |

Parent topic:

RFmxDemod Configure Trigger VI

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-configure-external-attenuation-vi.html language=enus -->
## TOPIC 00083: RFmxDemod Configure External Attenuation VI

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-configure-external-attenuation-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-configure-external-attenuation-vi.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the attenuation of a switch (or cable) connected to the RF IN connector of the signal analyzer. icon Inputs/Outputs cstr.png Selector String Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (e

### RFmxDemod Configure External Attenuation VI

Configures the attenuation of a switch (or cable) connected to the RF IN connector of the signal analyzer.

[IMAGE alt='icon' src='rfmxdemod-configure-external-attenuation-vi.png']

#### Inputs/Outputs

| Selector String — Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxDemod Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. External Attenuation (dB) — External Attenuation specifies the attenuation, in dB, of a switch (or cable) connected to the RF IN connector of the signal analyzer. For more information about attenuation, refer to the Attenuation and Signal Levels topic for your device in the NI RF Vector Signal Analyzers Help. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-configure-frequency-vi.html language=enus -->
## TOPIC 00084: RFmxDemod Configure Frequency VI

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-configure-frequency-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-configure-frequency-vi.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the expected carrier frequency of the RF signal that needs to be acquired. The signal analyzer tunes to this frequency. icon Inputs/Outputs cstr.png Selector String Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. Th

### RFmxDemod Configure Frequency VI

Configures the expected carrier frequency of the RF signal that needs to be acquired. The signal analyzer tunes to this frequency.

[IMAGE alt='icon' src='rfmxdemod-configure-frequency-vi.png']

#### Inputs/Outputs

| Selector String — Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxDemod Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Center Frequency (Hz) — Center Frequency specifies the carrier frequency, in Hz, of the RF signal that needs to be acquired. The signal analyzer tunes to this frequency. The default of this property is hardware dependent. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-configure-iq-power-edge-trigger-vi.html language=enus -->
## TOPIC 00085: RFmxDemod Configure IQ Power Edge Trigger VI

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-configure-iq-power-edge-trigger-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-configure-iq-power-edge-trigger-vi.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the I/Q power edge trigger. icon Inputs/Outputs cbool.png Enable Trigger? Enable Trigger? specifies whether to enable the trigger. The default value is TRUE. cdbl.png Trigger Delay (s) Trigger Delay specifies the trigger delay time, in seconds. cstr.png Selector String Selector String com

### RFmxDemod Configure IQ Power Edge Trigger VI

Configures the I/Q power edge trigger.

[IMAGE alt='icon' src='rfmxdemod-configure-iq-power-edge-trigger-vi.png']

#### Inputs/Outputs

| Enable Trigger? — Enable Trigger? specifies whether to enable the trigger. The default value is TRUE. Trigger Delay (s) — Trigger Delay specifies the trigger delay time, in seconds. Selector String — Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxDemod Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. IQ Power Edge Source — IQ Power Edge Source specifies the channel from which the device monitors the trigger. The default value is 0. IQ Power Edge Slope — IQ Power Edge Slope specifies whether the device asserts the trigger when the signal power is rising or falling. The device asserts the trigger when the signal power exceeds the specified level with the slope you specify. This parameter is used only when you set the Trigger Type property to IQ Power Edge. The default value is Rising Slope. Rising Slope (0) The trigger asserts when the signal power is rising. Falling Slope (1) The trigger asserts when the signal power is falling. IQ Power Edge Level (dB or dBm) — IQ Power Edge Level specifies the power level at which the device triggers. This value is expressed in dB when you set the IQ Power Edge Level Type parameter to Relative, and this value is expressed in dBm when you set the IQ Power Edge Level Type parameter to Absolute. The device asserts the trigger when the signal exceeds the level specified by the value of this parameter, taking into consideration the specified slope. The default of this property is hardware dependent. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Minimum Quiet Time Mode — Minimum Quiet Time Mode specifies whether the measurement computes the minimum quiet time used for triggering. The default value is Manual. Manual (0) The minimum quiet time for triggering is the value of the Min Quiet Time parameter. Auto (1) The measurement computes the minimum quiet time used for triggering. Minimum Quiet Time (s) — Minimum Quiet Time specifies the time duration, in seconds, for which the signal must be quiet before the signal analyzer arms the I/Q power-edge trigger. IQ Power Edge Level Type — IQ Power Edge Level Type specifies the reference for the IQ Power Edge Level parameter. The IQ Power Edge Level Type parameter is used only when you set the Trigger Type property to IQ Power Edge. The default value is Absolute. Relative (0) The IQ Power Edge Level property is relative to the value of the Reference Level property. Absolute (1) The IQ Power Edge Level property specifies the absolute power. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Rising Slope (0) | The trigger asserts when the signal power is rising. |
| Falling Slope (1) | The trigger asserts when the signal power is falling. |
| Manual (0) | The minimum quiet time for triggering is the value of the Min Quiet Time parameter. |
| Auto (1) | The measurement computes the minimum quiet time used for triggering. |
| Relative (0) | The IQ Power Edge Level property is relative to the value of the Reference Level property. |
| Absolute (1) | The IQ Power Edge Level property specifies the absolute power. |

Parent topic:

RFmxDemod Configure Trigger VI

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-configure-reference-level-vi.html language=enus -->
## TOPIC 00086: RFmxDemod Configure Reference Level VI

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-configure-reference-level-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-configure-reference-level-vi.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the reference level that represents the maximum expected power of an RF input signal. icon Inputs/Outputs cstr.png Selector String Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty strin

### RFmxDemod Configure Reference Level VI

Configures the reference level that represents the maximum expected power of an RF input signal.

[IMAGE alt='icon' src='rfmxdemod-configure-reference-level-vi.png']

#### Inputs/Outputs

| Selector String — Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxDemod Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Reference Level — Reference Level specifies the reference level which represents the maximum expected power of an RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices. The default of this parameter is hardware dependent. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-configure-rf-vi.html language=enus -->
## TOPIC 00087: RFmxDemod Configure RF VI

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-configure-rf-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-configure-rf-vi.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the RF properties of the signal by specifying the selector string. icon Inputs/Outputs cstr.png Selector String Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "si

### RFmxDemod Configure RF VI

Configures the RF properties of the signal by specifying the selector string.

[IMAGE alt='icon' src='rfmxdemod-configure-rf-vi.png']

#### Inputs/Outputs

| Selector String — Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxDemod Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Center Frequency (Hz) — Center Frequency specifies the carrier frequency, in Hz, of the RF signal that needs to be acquired. The signal analyzer tunes to this frequency. The default of this property is hardware dependent. Reference Level — Reference Level specifies the reference level which represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices. The default of this property is hardware dependent. External Attenuation (dB) — External Attenuation specifies the attenuation, in dB, of a switch (or cable) connected to the RF IN connector of the signal analyzer. For more information about attenuation, refer to the Attenuation and Signal Levels topic for your device in the NI RF Vector Signal Analyzers Help. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-configure-software-edge-trigger-vi.html language=enus -->
## TOPIC 00088: RFmxDemod Configure Software Edge Trigger VI

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-configure-software-edge-trigger-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-configure-software-edge-trigger-vi.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the software-edge trigger. icon Inputs/Outputs cbool.png Enable Trigger? Enable Trigger? specifies whether to enable the trigger. The default value is TRUE. cstr.png Selector String Selector String comprises of the signal name. If you do not specify the signal name, the default signal ins

### RFmxDemod Configure Software Edge Trigger VI

Configures the software-edge trigger.

[IMAGE alt='icon' src='rfmxdemod-configure-software-edge-trigger-vi.png']

#### Inputs/Outputs

| Enable Trigger? — Enable Trigger? specifies whether to enable the trigger. The default value is TRUE. Selector String — Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxDemod Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Trigger Delay (s) — Trigger Delay specifies the trigger delay time, in seconds. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxDemod Configure Trigger VI

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-configure-trigger-vi.html language=enus -->
## TOPIC 00089: RFmxDemod Configure Trigger VI

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-configure-trigger-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-configure-trigger-vi.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the Reference Trigger to use to acquire the signal. icon

### RFmxDemod Configure Trigger VI

Configures the Reference Trigger to use to acquire the signal.

[IMAGE alt='icon' src='rfmxdemod-configure-trigger-vi.png']

- [RFmxDemod Disable Trigger VI](../../../../../vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-disable-trigger-vi.html) Disables the trigger.
- [RFmxDemod Configure Digital Edge Trigger VI](../../../../../vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-configure-digital-edge-trigger-vi.html) Configures the digital edge trigger.
- [RFmxDemod Configure IQ Power Edge Trigger VI](../../../../../vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-configure-iq-power-edge-trigger-vi.html) Configures the I/Q power edge trigger.
- [RFmxDemod Configure Software Edge Trigger VI](../../../../../vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-configure-software-edge-trigger-vi.html) Configures the software-edge trigger.

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-create-signal-configuration-vi.html language=enus -->
## TOPIC 00090: RFmxDemod Create Signal Configuration VI

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-create-signal-configuration-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-create-signal-configuration-vi.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a new instance of a signal. icon Inputs/Outputs cstr.png Signal Name Signal Name specifies the name of the signal. This parameter accepts the signal name with or without the "signal::" prefix. Example: "signal::sig1" "sig1" cgenclassrntag.png Instrument Handle In Instrument Handle In specifi

### RFmxDemod Create Signal Configuration VI

Creates a new instance of a signal.

[IMAGE alt='icon' src='rfmxdemod-create-signal-configuration-vi.png']

#### Inputs/Outputs

| Signal Name — Signal Name specifies the name of the signal. This parameter accepts the signal name with or without the "signal::" prefix. Example: "signal::sig1" "sig1" Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Selector String Out — Selector String Out returns the selector string that can be passed to the Selector String parameter on Configure, Initiate, and Fetch VIs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-configure-averaging-vi.html language=enus -->
## TOPIC 00091: RFmxDemod DDemod Configure Averaging VI

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-configure-averaging-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-configure-averaging-vi.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures averaging for digital demodulation measurements. icon Inputs/Outputs cstr.png Selector String Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You ca

### RFmxDemod DDemod Configure Averaging VI

Configures averaging for digital demodulation measurements.

[IMAGE alt='icon' src='rfmxdemod-ddemod-configure-averaging-vi.png']

#### Inputs/Outputs

| Selector String — Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxDemod Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Averaging Enabled — Averaging Enabled enables averaging for digital demodulation measurement. False (0) The measurement is performed on a single acquisition. True (1) The measurement uses the value of the Averaging Count parameter for the number of acquisitions over which the measurement is averaged. The traces are not averaged. Averaging Count — Averaging Count specifies the number of acquisitions used for averaging when you set the Averaging Enabled parameter to True. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| False (0) | The measurement is performed on a single acquisition. |
| True (1) | The measurement uses the value of the Averaging Count parameter for the number of acquisitions over which the measurement is averaged. The traces are not averaged. |

Parent topic:

DDemod

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-configure-equalizer-initial-coefficients-vi.html language=enus -->
## TOPIC 00092: RFmxDemod DDemod Configure Equalizer Initial Coefficients VI

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-configure-equalizer-initial-coefficients-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-configure-equalizer-initial-coefficients-vi.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the equalizer coefficients. icon Inputs/Outputs cstr.png Selector String Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxDemod B

### RFmxDemod DDemod Configure Equalizer Initial Coefficients VI

Configures the equalizer coefficients.

[IMAGE alt='icon' src='rfmxdemod-ddemod-configure-equalizer-initial-coefficients-vi.png']

#### Inputs/Outputs

| Selector String — Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxDemod Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. — Equalizer Initial Coefficients specifies the equalizer initial coefficients. x0 — x0 always pass 0 to this parameter. Any other values are ignored. dx — dx specifies the spacing between the coefficients as a fraction of the symbol spacing. For example, if four coefficients correspond to one symbol, the spacing is 1/4. y — y specifies the initial coefficients to be used by the equalizer. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| x0 — x0 always pass 0 to this parameter. Any other values are ignored. dx — dx specifies the spacing between the coefficients as a fraction of the symbol spacing. For example, if four coefficients correspond to one symbol, the spacing is 1/4. y — y specifies the initial coefficients to be used by the equalizer. |

Parent topic:

DDemod

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-configure-equalizer-vi.html language=enus -->
## TOPIC 00093: RFmxDemod DDemod Configure Equalizer VI

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-configure-equalizer-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-configure-equalizer-vi.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the equalizer. icon Inputs/Outputs ci32.png Equalizer Training Count Equalizer Training Count specifies the number of iterations during which the equalizer adapts its coefficients in the training stage. cstr.png Selector String Selector String comprises of the signal name. If you do not s

### RFmxDemod DDemod Configure Equalizer VI

Configures the equalizer.

[IMAGE alt='icon' src='rfmxdemod-ddemod-configure-equalizer-vi.png']

#### Inputs/Outputs

| Equalizer Training Count — Equalizer Training Count specifies the number of iterations during which the equalizer adapts its coefficients in the training stage. Selector String — Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxDemod Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Equalizer Mode — Equalizer Mode specifies whether the measurement needs to perform equalization. The default value is Off. Off (0) Equalization is not performed. Train (1) The adaptive feedforward equalizer is turned ON to compensate for the effect of the channel. You can set the initial coefficients to be used by the equalizer. If you do not specify the initial coefficients, an impulse is used. Hold (2) The filter that you specify using the initial coefficients is used as the channel filter and is applied before demodulating the acquired signal. Equalizer Filter Length (Symbols) — Equalizer Filter Length specifies the length of the equalization filter to be computed. The length is specified in terms of symbols. This parameter is ignored when the equalizer initial coefficients are specified. — Equalizer Initial Coefficients specifies the equalizer initial coefficients. x0 — x0 always pass 0 to this parameter. Any other values are ignored. dx — dx specifies the spacing between the coefficients as a fraction of the symbol spacing. For example, if four coefficients correspond to one symbol, the spacing is 1/4. y — y specifies the initial coefficients to be used by the equalizer. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Equalizer Convergence Factor — Equalizer Convergence Factor specifies the incremental step used to adapt the equalizer to the channel during the training stage. The default value is 0.0001. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Off (0) | Equalization is not performed. |
| Train (1) | The adaptive feedforward equalizer is turned ON to compensate for the effect of the channel. You can set the initial coefficients to be used by the equalizer. If you do not specify the initial coefficients, an impulse is used. |
| Hold (2) | The filter that you specify using the initial coefficients is used as the channel filter and is applied before demodulating the acquired signal. |
| x0 — x0 always pass 0 to this parameter. Any other values are ignored. dx — dx specifies the spacing between the coefficients as a fraction of the symbol spacing. For example, if four coefficients correspond to one symbol, the spacing is 1/4. y — y specifies the initial coefficients to be used by the equalizer. |  |

Parent topic:

DDemod

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-configure-evm-normalization-reference-vi.html language=enus -->
## TOPIC 00094: RFmxDemod DDemod Configure EVM Normalization Reference VI

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-configure-evm-normalization-reference-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-configure-evm-normalization-reference-vi.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the error vector magnitude (EVM) normalization reference. icon Inputs/Outputs cstr.png Selector String Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig

### RFmxDemod DDemod Configure EVM Normalization Reference VI

Configures the error vector magnitude (EVM) normalization reference.

[IMAGE alt='icon' src='rfmxdemod-ddemod-configure-evm-normalization-reference-vi.png']

#### Inputs/Outputs

| Selector String — Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxDemod Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. EVM Normalization Reference — EVM Normalization Reference specifies the reference used to normalize the EVM. Peak (0) The EVM is normalized to the peak magnitude of the reference symbols. RMS (1) The EVM is normalized to the RMS magnitude of the reference symbols. This value is applicable only to modulation types, such as quadrature-amplitude modulation (QAM). This value is expressed in which the symbols in the map do not have a constant amplitude. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Peak (0) | The EVM is normalized to the peak magnitude of the reference symbols. |
| RMS (1) | The EVM is normalized to the RMS magnitude of the reference symbols. This value is applicable only to modulation types, such as quadrature-amplitude modulation (QAM). This value is expressed in which the symbols in the map do not have a constant amplitude. |

Parent topic:

DDemod

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-configure-fsk-deviation-vi.html language=enus -->
## TOPIC 00095: RFmxDemod DDemod Configure FSK Deviation VI

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-configure-fsk-deviation-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-configure-fsk-deviation-vi.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the expected FSK deviation. icon Inputs/Outputs cstr.png Selector String Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxDemod B

### RFmxDemod DDemod Configure FSK Deviation VI

Configures the expected FSK deviation.

[IMAGE alt='icon' src='rfmxdemod-ddemod-configure-fsk-deviation-vi.png']

#### Inputs/Outputs

| Selector String — Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxDemod Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. FSK Deviation (Hz) — FSK Deviation specifies the expected FSK frequency deviation, in Hz. FSK Reference Compensation Enabled — FSK Reference Compensation Enabled specifies whether the FSK deviation that you specify is used to compensate for gain errors and to compute the FSK error. Default value is False. False (0) Does not compensate for gain errors. True (1) Compensates for gain errors. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| False (0) | Does not compensate for gain errors. |
| True (1) | Compensates for gain errors. |

Parent topic:

DDemod

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-configure-m-vi.html language=enus -->
## TOPIC 00096: RFmxDemod DDemod Configure M VI

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-configure-m-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-configure-m-vi.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the M-ary number. icon Inputs/Outputs cstr.png Selector String Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxDemod Build Signa

### RFmxDemod DDemod Configure M VI

Configures the M-ary number.

[IMAGE alt='icon' src='rfmxdemod-ddemod-configure-m-vi.png']

#### Inputs/Outputs

| Selector String — Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxDemod Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. M — M specifies the M-ary number, which is the number of distinct states that represent symbols in the complex baseband modulated waveform. Note Recommended values of M for modulation types are as follows: ASK: 2, 4, 8 FSK , PSK: 2, 4, 8, 16 QAM: 16, 32, 64, 128, 256, 512, 1028, 2048, 4096. The default value is 4. 2 (2) The M-ary number is 2. 4 (4) The M-ary number is 4. 8 (8) The M-ary number is 8. 16 (16) The M-ary number is 16. 32 (32) The M-ary number is 32. 64 (64) The M-ary number is 64. 128 (128) The M-ary number is 128. 256 (256) The M-ary number is 256. 512 (512) The M-ary number is 512. 1024 (1024) The M-ary number is 1,024. 2048 (2048) The M-ary number is 2,048. 4096 (4096) The M-ary number is 4,096. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
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

Parent topic:

DDemod

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-configure-measurement-filter-custom-coefficients-vi.html language=enus -->
## TOPIC 00097: RFmxDemod DDemod Configure Measurement Filter Custom Coefficients VI

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-configure-measurement-filter-custom-coefficients-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-configure-measurement-filter-custom-coefficients-vi.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the measurement filter custom coefficients. icon Inputs/Outputs cstr.png Selector String Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use

### RFmxDemod DDemod Configure Measurement Filter Custom Coefficients VI

Configures the measurement filter custom coefficients.

[IMAGE alt='icon' src='rfmxdemod-ddemod-configure-measurement-filter-custom-coefficients-vi.png']

#### Inputs/Outputs

| Selector String — Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxDemod Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. — Measurement Filter Custom Coefficients specifies the measurement filter custom coefficients. Note To configure an impulse, set x0=0, dx=1, y[0]=1. x0 — x0 always pass 0 to this parameter. Any other values are ignored. dx — dx specifies the spacing between the coefficients as a fraction of the symbol spacing. For example, if four coefficients correspond to one symbol, the spacing is 1/4. y — y specifies the filter coefficients to be used by demodulator. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| x0 — x0 always pass 0 to this parameter. Any other values are ignored. dx — dx specifies the spacing between the coefficients as a fraction of the symbol spacing. For example, if four coefficients correspond to one symbol, the spacing is 1/4. y — y specifies the filter coefficients to be used by demodulator. |

Parent topic:

DDemod

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-configure-measurement-filter-vi.html language=enus -->
## TOPIC 00098: RFmxDemod DDemod Configure Measurement Filter VI

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-configure-measurement-filter-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-configure-measurement-filter-vi.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the measurement filter. icon Inputs/Outputs cstr.png Selector String Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxDemod Build

### RFmxDemod DDemod Configure Measurement Filter VI

Configures the measurement filter.

[IMAGE alt='icon' src='rfmxdemod-ddemod-configure-measurement-filter-vi.png']

#### Inputs/Outputs

| Selector String — Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxDemod Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Measurement Filter Type — Measurement Filter Type specifies whether the measurement needs to compute the measurement filter based on the pulse shaping filter type or uses the custom measurement filter coefficients. The default value is Auto. Auto (0) The signal analyzer computes the measurement filter coefficients based on the pulse-shaping filter information that you specify in the Pulse Shaping Filter Type parameter of the RFmxDemod DDemod Configure Pulse Shaping Filter VI. If the Pulse Shaping Filter Type parameter is set to Custom, the signal analyzer enables equalization. Custom (1) The signal analyzer uses the coefficients specified by RFmxDemod DDemod Configure Measurement Filter Custom Coefficients VI. — Measurement Filter Custom Coefficients specifies the measurements coefficients. Note To configure an impulse, set x0=0, dx=1, y[0]=1. x0 — x0 always pass 0 to this parameter. Any other values are ignored. dx — dx specifies the spacing between the coefficients as a fraction of the symbol spacing. For example, if four coefficients correspond to one symbol, the spacing is 1/4. y — y specifies the filter coefficients to be used by demodulator. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Auto (0) | The signal analyzer computes the measurement filter coefficients based on the pulse-shaping filter information that you specify in the Pulse Shaping Filter Type parameter of the RFmxDemod DDemod Configure Pulse Shaping Filter VI. If the Pulse Shaping Filter Type parameter is set to Custom, the signal analyzer enables equalization. |
| Custom (1) | The signal analyzer uses the coefficients specified by RFmxDemod DDemod Configure Measurement Filter Custom Coefficients VI. |
| x0 — x0 always pass 0 to this parameter. Any other values are ignored. dx — dx specifies the spacing between the coefficients as a fraction of the symbol spacing. For example, if four coefficients correspond to one symbol, the spacing is 1/4. y — y specifies the filter coefficients to be used by demodulator. |  |

Parent topic:

DDemod

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-configure-modulation-type-vi.html language=enus -->
## TOPIC 00099: RFmxDemod DDemod Configure Modulation Type VI

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-configure-modulation-type-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-configure-modulation-type-vi.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the modulation type of the signal to be analyzed. icon Inputs/Outputs cstr.png Selector String Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You c

### RFmxDemod DDemod Configure Modulation Type VI

Configures the modulation type of the signal to be analyzed.

[IMAGE alt='icon' src='rfmxdemod-ddemod-configure-modulation-type-vi.png']

#### Inputs/Outputs

| Selector String — Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxDemod Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Modulation Type — Modulation Type specifies the digital modulation type of the signal that needs to be analyzed. The default value is PSK. ASK (0) The modulation type is amplitude-shift keying (ASK). FSK (1) The modulation type is frequency-shift keying (FSK). PSK (2) The modulation type is phase-shift keying (PSK). QAM (3) The modulation type is quadrature-amplitude modulation (QAM). MSK (4) The modulation type is minimum shift keying (MSK). M — M specifies the M-ary number, which is the number of distinct states that represent symbols in the complex baseband modulated waveform. Note Recommended values of M for modulation types are as follows: ASK: 2, 4, 8 FSK , PSK: 2, 4, 8, 16 QAM: 16, 32, 64, 128, 256, 512, 1028, 2048, 4096. The default value is 4. 2 (2) The M-ary number is 2. 4 (4) The M-ary number is 4. 8 (8) The M-ary number is 8. 16 (16) The M-ary number is 16. 32 (32) The M-ary number is 32. 64 (64) The M-ary number is 64. 128 (128) The M-ary number is 128. 256 (256) The M-ary number is 256. 512 (512) The M-ary number is 512. 1024 (1024) The M-ary number is 1,024. 2048 (2048) The M-ary number is 2,048. 4096 (4096) The M-ary number is 4,096. Differential Enabled — Differential Enabled specifies whether the symbols are differentially encoded. This property is applicable only to PSK and MSK modulation types. The default value is False. False (0) The symbols are directly mapped onto the symbol map. True (1) In case of PSK modulation, the transition between two consecutive symbols is mapped onto the symbol map. In case of MSK modulation, the consecutive bits are XORed. Other modulation types do not have any impact. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| ASK (0) | The modulation type is amplitude-shift keying (ASK). |
| FSK (1) | The modulation type is frequency-shift keying (FSK). |
| PSK (2) | The modulation type is phase-shift keying (PSK). |
| QAM (3) | The modulation type is quadrature-amplitude modulation (QAM). |
| MSK (4) | The modulation type is minimum shift keying (MSK). |
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
| False (0) | The symbols are directly mapped onto the symbol map. |
| True (1) | In case of PSK modulation, the transition between two consecutive symbols is mapped onto the symbol map. In case of MSK modulation, the consecutive bits are XORed. Other modulation types do not have any impact. |

Parent topic:

DDemod

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-configure-number-of-symbols-vi.html language=enus -->
## TOPIC 00100: RFmxDemod DDemod Configure Number of Symbols VI

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-configure-number-of-symbols-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-configure-number-of-symbols-vi.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the number of symbols to be measured. icon Inputs/Outputs cstr.png Selector String Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the R

### RFmxDemod DDemod Configure Number of Symbols VI

Configures the number of symbols to be measured.

[IMAGE alt='icon' src='rfmxdemod-ddemod-configure-number-of-symbols-vi.png']

#### Inputs/Outputs

| Selector String — Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxDemod Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Number of Symbols — Number of Symbols specifies the number of symbols to be analyzed. The measurement acquires additional symbols to account for filter delays. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

DDemod

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-configure-psk-format-vi.html language=enus -->
## TOPIC 00101: RFmxDemod DDemod Configure PSK Format VI

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-configure-psk-format-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-configure-psk-format-vi.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the PSK format. icon Inputs/Outputs cstr.png Selector String Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxDemod Build Signal

### RFmxDemod DDemod Configure PSK Format VI

Configures the PSK format.

[IMAGE alt='icon' src='rfmxdemod-ddemod-configure-psk-format-vi.png']

#### Inputs/Outputs

| Selector String — Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxDemod Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. PSK Format — PSK Format specifies the PSK format. The default value is Normal. Normal (0) Sets the modulation type to PSK. Offset QPSK (1) Sets the modulation type to offset quadrature PSK (OQPSK). The ideal symbol timing of Q is offset by half of a symbol period from the ideal symbol timing of I. PI/4 - QPSK (2) Sets the modulation type to pi/4 QPSK. In this modulation, each QPSK symbol is rotated by pi/4. PI/8 - 8PSK (3) Sets the modulation type to pi/8 8PSK. In this modulation, each 8PSK symbol is rotated by pi/8. 3*PI/8 - 8PSK (4) Sets the modulation type to 3*pi/8-8 PSK. In this modulation, each 8 PSK symbol is rotated by 3*pi/8. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Normal (0) | Sets the modulation type to PSK. |
| Offset QPSK (1) | Sets the modulation type to offset quadrature PSK (OQPSK). The ideal symbol timing of Q is offset by half of a symbol period from the ideal symbol timing of I. |
| PI/4 - QPSK (2) | Sets the modulation type to pi/4 QPSK. In this modulation, each QPSK symbol is rotated by pi/4. |
| PI/8 - 8PSK (3) | Sets the modulation type to pi/8 8PSK. In this modulation, each 8PSK symbol is rotated by pi/8. |
| 3*PI/8 - 8PSK (4) | Sets the modulation type to 3*pi/8-8 PSK. In this modulation, each 8 PSK symbol is rotated by 3*pi/8. |

Parent topic:

DDemod

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-configure-pulse-shaping-filter-custom-coefficients-vi.html language=enus -->
## TOPIC 00102: RFmxDemod DDemod Configure Pulse Shaping Filter Custom Coefficients VI

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-configure-pulse-shaping-filter-custom-coefficients-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-configure-pulse-shaping-filter-custom-coefficients-vi.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the pulse-shaping filter coefficients. icon Inputs/Outputs cstr.png Selector String Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the

### RFmxDemod DDemod Configure Pulse Shaping Filter Custom Coefficients VI

Configures the pulse-shaping filter coefficients.

[IMAGE alt='icon' src='rfmxdemod-ddemod-configure-pulse-shaping-filter-custom-coefficients-vi.png']

#### Inputs/Outputs

| Selector String — Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxDemod Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. — Pulse Shaping Filter Custom Coefficients specifies the pulse-shaping filter custom coefficients. Note To configure an impulse, set x0=0, dx=1, y[0]=1. x0 — x0 always pass 0 to this parameter. Any other values are ignored. dx — dx specifies the spacing between the coefficients as a fraction of the symbol spacing. For example, if four coefficients correspond to one symbol, the spacing is 1/4. y — y specifies the filter coefficients used as the pulse shaping filter on the transmitter. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| x0 — x0 always pass 0 to this parameter. Any other values are ignored. dx — dx specifies the spacing between the coefficients as a fraction of the symbol spacing. For example, if four coefficients correspond to one symbol, the spacing is 1/4. y — y specifies the filter coefficients used as the pulse shaping filter on the transmitter. |

Parent topic:

DDemod

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-configure-pulse-shaping-filter-vi.html language=enus -->
## TOPIC 00103: RFmxDemod DDemod Configure Pulse Shaping Filter VI

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-configure-pulse-shaping-filter-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-configure-pulse-shaping-filter-vi.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the pulse-shaping filter. icon Inputs/Outputs cstr.png Selector String Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxDemod Bui

### RFmxDemod DDemod Configure Pulse Shaping Filter VI

Configures the pulse-shaping filter.

[IMAGE alt='icon' src='rfmxdemod-ddemod-configure-pulse-shaping-filter-vi.png']

#### Inputs/Outputs

| Selector String — Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxDemod Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Pulse Shaping Filter Type — Pulse Shaping Filter Type specifies the pulse-shaping filter used to transmit the signal and determines the measurement filter to be used for analysis when the Measurement Filter property is set to Auto. Rectangular (0) The transmitted waveform is filtered using a rectangular filter. Raised Cosine (1) The transmitted waveform is filtered using a raised cosine filter. Specify the filter Alpha in the DDemod Pulse Shaping Filter Parameter property. Root Raised Cosine (2) The transmitted waveform is filtered using a root raised cosine filter. Specify the filter Alpha in the DDemod Pulse Shaping Filter Parameter property. Gaussian (3) The transmitted waveform is filtered using a Gaussian filter. Specify the filter bandwidth * sample duration in the DDemod Pulse Shaping Filter Parameter property. This filter is applicable only to FSK and MSK modulation types. Custom (4) The transmitted waveform is filtered using the coefficients that you specify in the RFmxDemod DDemod Configure Pulse Shaping Filter Custom Coefficients VI. Half Sine (5) The transmitted waveform is filtered using a half sine filter. Linearised GMSK - EDGE (6) The transmitted waveform is filtered using an EDGE-specific linearized GMSK filter. Pulse Shaping Filter Parameter — Pulse Shaping Filter Parameter specifies the rolloff factor for the raised cosine and root-raised cosine filters that are used as pulse shaping filter, and measurement filter respectively. When pulse-shaping filter type is Gaussian, this property specifies bandwidth * sample duration (BT). — Pulse Shaping Filter Custom Coefficients specifies the pulse-shaping filter custom coefficients. Note To configure an impulse, set x0=0, dx=1, y[0]=1. x0 — x0 always pass 0 to this parameter. Any other values are ignored. dx — dx specifies the spacing between the coefficients as a fraction of the symbol spacing. For example, if four coefficients correspond to one symbol, the spacing is 1/4. y — y specifies the filter coefficients used as the pulse shaping filter on the transmitter. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Rectangular (0) | The transmitted waveform is filtered using a rectangular filter. |
| Raised Cosine (1) | The transmitted waveform is filtered using a raised cosine filter. Specify the filter Alpha in the DDemod Pulse Shaping Filter Parameter property. |
| Root Raised Cosine (2) | The transmitted waveform is filtered using a root raised cosine filter. Specify the filter Alpha in the DDemod Pulse Shaping Filter Parameter property. |
| Gaussian (3) | The transmitted waveform is filtered using a Gaussian filter. Specify the filter bandwidth * sample duration in the DDemod Pulse Shaping Filter Parameter property. This filter is applicable only to FSK and MSK modulation types. |
| Custom (4) | The transmitted waveform is filtered using the coefficients that you specify in the RFmxDemod DDemod Configure Pulse Shaping Filter Custom Coefficients VI. |
| Half Sine (5) | The transmitted waveform is filtered using a half sine filter. |
| Linearised GMSK - EDGE (6) | The transmitted waveform is filtered using an EDGE-specific linearized GMSK filter. |
| x0 — x0 always pass 0 to this parameter. Any other values are ignored. dx — dx specifies the spacing between the coefficients as a fraction of the symbol spacing. For example, if four coefficients correspond to one symbol, the spacing is 1/4. y — y specifies the filter coefficients used as the pulse shaping filter on the transmitter. |  |

Parent topic:

DDemod

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-configure-samples-per-symbol-vi.html language=enus -->
## TOPIC 00104: RFmxDemod DDemod Configure Samples Per Symbol VI

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-configure-samples-per-symbol-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-configure-samples-per-symbol-vi.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the samples per symbol to be used to acquire the signal for the measurement. icon Inputs/Outputs cstr.png Selector String Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examp

### RFmxDemod DDemod Configure Samples Per Symbol VI

Configures the samples per symbol to be used to acquire the signal for the measurement.

[IMAGE alt='icon' src='rfmxdemod-ddemod-configure-samples-per-symbol-vi.png']

#### Inputs/Outputs

| Selector String — Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxDemod Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Samples Per Symbol — Samples Per Symbol specifies the samples per symbol used to acquire the signal for the measurement. Auto (-1) The measurement uses appropriate samples per symbol (SPS) based on modulation type and pulse shaping filter. SPS=8, for FSK. SPS=4, for ASK,PSK, QAM, MSK when pulse shape filter is not rectangular. SPS=8, for ASK, PSK, QAM, MSK when pulse shape filter is rectangular. 4 (4) The samples per symbol value is 4. 8 (8) The samples per symbol value is 8. 16 (16) The samples per symbol value is 16. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Auto (-1) | The measurement uses appropriate samples per symbol (SPS) based on modulation type and pulse shaping filter. SPS=8, for FSK. SPS=4, for ASK,PSK, QAM, MSK when pulse shape filter is not rectangular. SPS=8, for ASK, PSK, QAM, MSK when pulse shape filter is rectangular. |
| 4 (4) | The samples per symbol value is 4. |
| 8 (8) | The samples per symbol value is 8. |
| 16 (16) | The samples per symbol value is 16. |

Parent topic:

DDemod

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-configure-signal-structure-vi.html language=enus -->
## TOPIC 00105: RFmxDemod DDemod Configure Signal Structure VI

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-configure-signal-structure-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-configure-signal-structure-vi.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the structure of the incoming signal to be either a continuous signal or a bursty signal. icon Inputs/Outputs cstr.png Selector String Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty s

### RFmxDemod DDemod Configure Signal Structure VI

Configures the structure of the incoming signal to be either a continuous signal or a bursty signal.

[IMAGE alt='icon' src='rfmxdemod-ddemod-configure-signal-structure-vi.png']

#### Inputs/Outputs

| Selector String — Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxDemod Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Signal Structure — Signal Structure specifies whether the signal is either a bursty signal or a continuous signal. The default value is Continuous. Bursted (0) The signal is a bursty signal. Continuous (1) The signal is a continuous signal. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Bursted (0) | The signal is a bursty signal. |
| Continuous (1) | The signal is a continuous signal. |

Parent topic:

DDemod

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-configure-spectrum-inverted-vi.html language=enus -->
## TOPIC 00106: RFmxDemod DDemod Configure Spectrum Inverted VI

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-configure-spectrum-inverted-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-configure-spectrum-inverted-vi.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures swapping of I and Q channels in the acquired waveform before demodulation. icon Inputs/Outputs cstr.png Selector String Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example

### RFmxDemod DDemod Configure Spectrum Inverted VI

Configures swapping of I and Q channels in the acquired waveform before demodulation.

[IMAGE alt='icon' src='rfmxdemod-ddemod-configure-spectrum-inverted-vi.png']

#### Inputs/Outputs

| Selector String — Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxDemod Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Spectrum Inverted — Spectrum Inverted specifies whether to swap the acquired I and Q samples for demodulation. The default value is False. False (0) The acquired I and Q samples are used for demodulation as is. True (1) The acquired I and Q samples are swapped before using the signal for demodulation. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| False (0) | The acquired I and Q samples are used for demodulation as is. |
| True (1) | The acquired I and Q samples are swapped before using the signal for demodulation. |

Parent topic:

DDemod

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-configure-symbol-map-vi.html language=enus -->
## TOPIC 00107: RFmxDemod DDemod Configure Symbol Map VI

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-configure-symbol-map-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-configure-symbol-map-vi.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the symbol map that you use during measurements. icon Inputs/Outputs cstr.png Selector String Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You ca

### RFmxDemod DDemod Configure Symbol Map VI

Configures the symbol map that you use during measurements.

[IMAGE alt='icon' src='rfmxdemod-ddemod-configure-symbol-map-vi.png']

#### Inputs/Outputs

| Selector String — Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxDemod Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Symbol Map Type — Symbol Map Type specifies whether the measurement uses the default symbol map or the map that you configure using the RFmxDemod DDemod Configure Symbol Map VI. Auto (0) Uses a default symbol map. Custom (1) Uses the map that you specify. Symbol Map — Symbol Map specifies the custom symbol map. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Auto (0) | Uses a default symbol map. |
| Custom (1) | Uses the map that you specify. |

Parent topic:

DDemod

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-configure-symbol-rate-vi.html language=enus -->
## TOPIC 00108: RFmxDemod DDemod Configure Symbol Rate VI

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-configure-symbol-rate-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-configure-symbol-rate-vi.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the symbol rate for digital demodulation measurements. icon Inputs/Outputs cstr.png Selector String Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1"

### RFmxDemod DDemod Configure Symbol Rate VI

Configures the symbol rate for digital demodulation measurements.

[IMAGE alt='icon' src='rfmxdemod-ddemod-configure-symbol-rate-vi.png']

#### Inputs/Outputs

| Selector String — Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxDemod Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Symbol Rate (Hz) — Symbol Rate specifies the symbol rate in Hz. The default value is 100 kHz. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

DDemod

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-configure-synchronization-vi.html language=enus -->
## TOPIC 00109: RFmxDemod DDemod Configure Synchronization VI

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-configure-synchronization-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-configure-synchronization-vi.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures bit pattern synchronization. icon Inputs/Outputs cstr.png Selector String Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxDemod

### RFmxDemod DDemod Configure Synchronization VI

Configures bit pattern synchronization.

[IMAGE alt='icon' src='rfmxdemod-ddemod-configure-synchronization-vi.png']

#### Inputs/Outputs

| Selector String — Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxDemod Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Synchronization Enabled — Synchronization Enabled specifies whether the demodulator needs to search and synchronize the signal to a known reference sequence. The reference sequence is the symbol representation of a defined set of bits known to be present in the transmitted signal. If the synchronization is found in the demodulated signal, the measurement is performed from this point onward. If the synchronization is not found, the entire signal is used for the measurement. False (0) Does not search and synchronize the signal. True (1) Searches and synchronizes the signal. Synchronization Bits — Synchronization Bits specifies the synchronization bits used to create the reference sequence that needs to be searched in the demodulated signal. Measurement Offset (Symbols) — Measurement Offset specifies the offset, which is the location from which the signal is considered for further measurements. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| False (0) | Does not search and synchronize the signal. |
| True (1) | Searches and synchronizes the signal. |

Parent topic:

DDemod

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-fetch-carrier-measurement-vi.html language=enus -->
## TOPIC 00110: RFmxDemod DDemod Fetch Carrier Measurement VI

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-fetch-carrier-measurement-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-fetch-carrier-measurement-vi.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the carrier measurement. icon Inputs/Outputs cstr.png Selector String Selector String comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default

### RFmxDemod DDemod Fetch Carrier Measurement VI

Fetches the carrier measurement.

[IMAGE alt='icon' src='rfmxdemod-ddemod-fetch-carrier-measurement-vi.png']

#### Inputs/Outputs

| Selector String — Selector String comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxDemod Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. This value is expressed in seconds. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Mean Frequency Offset (Hz) — Mean Frequency Offset returns the mean of the measured carrier frequency offset, in Hz. Mean Frequency Drift (Hz) — Mean Frequency Drift returns the mean of the measured carrier frequency drift, in Hz. Mean Phase Error (deg) — Mean Phase Error returns the mean of the measured phase offset, in degrees, from the transmitted carrier phase. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxDemod DDemod Fetch VI

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-fetch-constellation-trace-vi.html language=enus -->
## TOPIC 00111: RFmxDemod DDemod Fetch Constellation Trace VI

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-fetch-constellation-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-fetch-constellation-trace-vi.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the constellation trace. icon Inputs/Outputs cstr.png Selector String Selector String comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default

### RFmxDemod DDemod Fetch Constellation Trace VI

Fetches the constellation trace.

[IMAGE alt='icon' src='rfmxdemod-ddemod-fetch-constellation-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxDemod Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. This value is expressed in seconds. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Constellation Trace — Constellation Trace returns the constellation trace. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxDemod DDemod Fetch VI

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-fetch-demodulated-bits-vi.html language=enus -->
## TOPIC 00112: RFmxDemod DDemod Fetch Demodulated Bits VI

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-fetch-demodulated-bits-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-fetch-demodulated-bits-vi.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the demodulated bit stream. icon Inputs/Outputs cstr.png Selector String Selector String comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The defa

### RFmxDemod DDemod Fetch Demodulated Bits VI

Fetches the demodulated bit stream.

[IMAGE alt='icon' src='rfmxdemod-ddemod-fetch-demodulated-bits-vi.png']

#### Inputs/Outputs

| Selector String — Selector String comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxDemod Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. This value is expressed in seconds. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Demodulated Bits — Demodulated Bits returns the demodulated bit stream. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxDemod DDemod Fetch VI

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-fetch-equalizer-coefficients-vi.html language=enus -->
## TOPIC 00113: RFmxDemod DDemod Fetch Equalizer Coefficients VI

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-fetch-equalizer-coefficients-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-fetch-equalizer-coefficients-vi.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the updated equalizer coefficients. icon Inputs/Outputs cstr.png Selector String Selector String comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used.

### RFmxDemod DDemod Fetch Equalizer Coefficients VI

Fetches the updated equalizer coefficients.

[IMAGE alt='icon' src='rfmxdemod-ddemod-fetch-equalizer-coefficients-vi.png']

#### Inputs/Outputs

| Selector String — Selector String comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxDemod Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. This value is expressed in seconds. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Equalizer Coefficients — Equalizer Coefficients returns the updated coefficients. x0 — x0 this parameter always returns 0. dx — dx returns the spacing between the coefficients as a fraction of the symbol spacing. For example, if four coefficients correspond to one symbol, the spacing is 1/4. y — y returns the updated equalizer coefficients. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| x0 — x0 this parameter always returns 0. dx — dx returns the spacing between the coefficients as a fraction of the symbol spacing. For example, if four coefficients correspond to one symbol, the spacing is 1/4. y — y returns the updated equalizer coefficients. |

Parent topic:

RFmxDemod DDemod Fetch VI

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-fetch-evm-trace-vi.html language=enus -->
## TOPIC 00114: RFmxDemod DDemod Fetch EVM Trace VI

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-fetch-evm-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-fetch-evm-trace-vi.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the EVM trace. icon Inputs/Outputs cstr.png Selector String Selector String comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is

### RFmxDemod DDemod Fetch EVM Trace VI

Fetches the EVM trace.

[IMAGE alt='icon' src='rfmxdemod-ddemod-fetch-evm-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxDemod Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. This value is expressed in seconds. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. EVM (%) — EVM returns the EVM measured per symbol. x0 — x0 returns the start symbol index. dx — dx returns the spacing between symbols normalized to symbol rate. y — y returns the offset EVM per symbol. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| x0 — x0 returns the start symbol index. dx — dx returns the spacing between symbols normalized to symbol rate. y — y returns the offset EVM per symbol. |

Parent topic:

RFmxDemod DDemod Fetch VI

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-fetch-evm-vi.html language=enus -->
## TOPIC 00115: RFmxDemod DDemod Fetch EVM VI

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-fetch-evm-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-fetch-evm-vi.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the EVM measurements. icon Inputs/Outputs cstr.png Selector String Selector String comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default va

### RFmxDemod DDemod Fetch EVM VI

Fetches the EVM measurements.

[IMAGE alt='icon' src='rfmxdemod-ddemod-fetch-evm-vi.png']

#### Inputs/Outputs

| Selector String — Selector String comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxDemod Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. This value is expressed in seconds. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Mean Peak EVM (%) — Mean Peak EVM returns the mean of the peak EVM measured per acquisition. Maximum Peak EVM (%) — Maximum Peak EVM returns the maximum of the peak EVM measured per acquisition. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Mean RMS EVM (%) — Mean RMS EVM returns the mean of the RMS EVM, as a percentage, measured per acquisition. Maximum RMS EVM (%) — Maximum RMS EVM returns the maximum of the RMS EVM, as a percentage, measured per acquisition. Mean Modulation Error Ratio (dB) — Mean Modulation Error Ratio returns the modulation error ratio, in dB. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxDemod DDemod Fetch VI

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-fetch-fsk-deviation-trace-vi.html language=enus -->
## TOPIC 00116: RFmxDemod DDemod Fetch FSK Deviation Trace VI

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-fetch-fsk-deviation-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-fetch-fsk-deviation-trace-vi.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the frequency-shift keying (FSK) deviation trace. icon Inputs/Outputs cstr.png Selector String Selector String comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result inst

### RFmxDemod DDemod Fetch FSK Deviation Trace VI

Fetches the frequency-shift keying (FSK) deviation trace.

[IMAGE alt='icon' src='rfmxdemod-ddemod-fetch-fsk-deviation-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxDemod Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. This value is expressed in seconds. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. FSK Deviation Error (Hz) — FSK Error returns the mean of the RMS frequency error of the FSK symbols measured per acquisition. x0 — x0 returns the start symbol index. dx — dx returns the spacing between symbols normalized to symbol rate. y — y returns the FSK deviation error per symbol. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| x0 — x0 returns the start symbol index. dx — dx returns the spacing between symbols normalized to symbol rate. y — y returns the FSK deviation error per symbol. |

Parent topic:

RFmxDemod DDemod Fetch VI

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-fetch-fsk-results-vi.html language=enus -->
## TOPIC 00117: RFmxDemod DDemod Fetch FSK Results VI

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-fetch-fsk-results-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-fetch-fsk-results-vi.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches frequency-shift keying (FSK) results. icon Inputs/Outputs cstr.png Selector String Selector String comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used

### RFmxDemod DDemod Fetch FSK Results VI

Fetches frequency-shift keying (FSK) results.

[IMAGE alt='icon' src='rfmxdemod-ddemod-fetch-fsk-results-vi.png']

#### Inputs/Outputs

| Selector String — Selector String comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxDemod Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. This value is expressed in seconds. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Mean FSK Deviation (Hz) — Mean FSK Deviation returns the measured FSK deviation, in Hz. Mean RMS FSK Error (Hz) — Mean RMS FSK Error returns the mean of the RMS frequency error, in Hz, of the FSK symbols measured per acquisition. Maximum Peak FSK Error (Hz) — Maximum Peak FSK Error returns the maximum of peak frequency error of the FSK symbols measured per acquisition. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxDemod DDemod Fetch VI

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-fetch-iq-impairments-vi.html language=enus -->
## TOPIC 00118: RFmxDemod DDemod Fetch IQ Impairments VI

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-fetch-iq-impairments-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-fetch-iq-impairments-vi.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches I/Q impairments. icon Inputs/Outputs cstr.png Selector String Selector String comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value i

### RFmxDemod DDemod Fetch IQ Impairments VI

Fetches I/Q impairments.

[IMAGE alt='icon' src='rfmxdemod-ddemod-fetch-iq-impairments-vi.png']

#### Inputs/Outputs

| Selector String — Selector String comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxDemod Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. This value is expressed in seconds. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Mean IQ Gain Imbalance (dB) — Mean IQ Gain Imbalance returns the measured ratio of I gain to Q gain, in dB. Mean Quadrature Skew (deg) — Mean Quadrature Skew returns a measure of I and Q components in the signal that are not perfectly orthogonal. Mean IQ Origin Offset (dB) — Mean IQ Origin Offset returns the offset, in dB, from the ideal location of the constellation origin. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxDemod DDemod Fetch VI

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-fetch-magnitude-error-trace-vi.html language=enus -->
## TOPIC 00119: RFmxDemod DDemod Fetch Magnitude Error Trace VI

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-fetch-magnitude-error-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-fetch-magnitude-error-trace-vi.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the magnitude error trace. icon Inputs/Outputs cstr.png Selector String Selector String comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The defau

### RFmxDemod DDemod Fetch Magnitude Error Trace VI

Fetches the magnitude error trace.

[IMAGE alt='icon' src='rfmxdemod-ddemod-fetch-magnitude-error-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxDemod Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. This value is expressed in seconds. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Magnitude Error (%) — Magnitude Error returns the magnitude error. x0 — x0 returns the start symbol index. dx — dx returns the spacing between symbols normalized to symbol rate. y — y returns the magnitude error per symbol. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| x0 — x0 returns the start symbol index. dx — dx returns the spacing between symbols normalized to symbol rate. y — y returns the magnitude error per symbol. |

Parent topic:

RFmxDemod DDemod Fetch VI

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-fetch-magnitude-error-vi.html language=enus -->
## TOPIC 00120: RFmxDemod DDemod Fetch Magnitude Error VI

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-fetch-magnitude-error-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-fetch-magnitude-error-vi.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the magnitude error measurements. icon Inputs/Outputs cstr.png Selector String Selector String comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Th

### RFmxDemod DDemod Fetch Magnitude Error VI

Fetches the magnitude error measurements.

[IMAGE alt='icon' src='rfmxdemod-ddemod-fetch-magnitude-error-vi.png']

#### Inputs/Outputs

| Selector String — Selector String comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxDemod Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. This value is expressed in seconds. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Mean Magnitude Error (%) — Mean Magnitude Error returns the mean of the magnitude error measured per acquisition. Maximum Magnitude Error (%) — Maximum Magnitude Error returns the maximum of the magnitude error measured per acquisition. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxDemod DDemod Fetch VI

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-fetch-mean-amplitude-droop-vi.html language=enus -->
## TOPIC 00121: RFmxDemod DDemod Fetch Mean Amplitude Droop VI

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-fetch-mean-amplitude-droop-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-fetch-mean-amplitude-droop-vi.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the mean amplitude droop per symbol. icon Inputs/Outputs cstr.png Selector String Selector String comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used.

### RFmxDemod DDemod Fetch Mean Amplitude Droop VI

Fetches the mean amplitude droop per symbol.

[IMAGE alt='icon' src='rfmxdemod-ddemod-fetch-mean-amplitude-droop-vi.png']

#### Inputs/Outputs

| Selector String — Selector String comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxDemod Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. This value is expressed in seconds. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Mean Amplitude Droop (dB/Symbol) — Mean Amplitude Droop returns the mean amplitude droop per symbol. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxDemod DDemod Fetch VI

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-fetch-mean-iq-origin-offset-vi.html language=enus -->
## TOPIC 00122: RFmxDemod DDemod Fetch Mean IQ Origin Offset VI

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-fetch-mean-iq-origin-offset-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-fetch-mean-iq-origin-offset-vi.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the offset, in dB, from the ideal location of the constellation origin. icon Inputs/Outputs cstr.png Selector String Selector String comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, t

### RFmxDemod DDemod Fetch Mean IQ Origin Offset VI

Fetches the offset, in dB, from the ideal location of the constellation origin.

[IMAGE alt='icon' src='rfmxdemod-ddemod-fetch-mean-iq-origin-offset-vi.png']

#### Inputs/Outputs

| Selector String — Selector String comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxDemod Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. This value is expressed in seconds. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Mean IQ Origin Offset (dB) — Mean IQ Origin Offset returns the offset, in dB, from the ideal location of the constellation origin. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxDemod DDemod Fetch VI

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-fetch-mean-quadrature-skew-vi.html language=enus -->
## TOPIC 00123: RFmxDemod DDemod Fetch Mean Quadrature Skew VI

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-fetch-mean-quadrature-skew-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-fetch-mean-quadrature-skew-vi.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the mean quadrature skew. icon Inputs/Outputs cstr.png Selector String Selector String comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The defaul

### RFmxDemod DDemod Fetch Mean Quadrature Skew VI

Fetches the mean quadrature skew.

[IMAGE alt='icon' src='rfmxdemod-ddemod-fetch-mean-quadrature-skew-vi.png']

#### Inputs/Outputs

| Selector String — Selector String comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxDemod Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. This value is expressed in seconds. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Mean Quadrature Skew (deg) — Mean Quadrature Skew returns a measure of I and Q components in the signal that are not perfectly orthogonal. Quadrature error can be either positive or negative, with the sign indicating the orientation of the error. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxDemod DDemod Fetch VI

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-fetch-mean-rho-factor-vi.html language=enus -->
## TOPIC 00124: RFmxDemod DDemod Fetch Mean Rho Factor VI

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-fetch-mean-rho-factor-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-fetch-mean-rho-factor-vi.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the correlation of the measurement waveform and the reference waveform. icon Inputs/Outputs cstr.png Selector String Selector String comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, t

### RFmxDemod DDemod Fetch Mean Rho Factor VI

Fetches the correlation of the measurement waveform and the reference waveform.

[IMAGE alt='icon' src='rfmxdemod-ddemod-fetch-mean-rho-factor-vi.png']

#### Inputs/Outputs

| Selector String — Selector String comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxDemod Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. This value is expressed in seconds. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Mean Rho Factor — Mean Rho Factor returns the correlation of the measurement waveform and the reference waveform. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxDemod DDemod Fetch VI

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-fetch-measurement-waveform-vi.html language=enus -->
## TOPIC 00125: RFmxDemod DDemod Fetch Measurement Waveform VI

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-fetch-measurement-waveform-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-fetch-measurement-waveform-vi.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the measurement waveform. icon Inputs/Outputs cstr.png Selector String Selector String comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The defaul

### RFmxDemod DDemod Fetch Measurement Waveform VI

Fetches the measurement waveform.

[IMAGE alt='icon' src='rfmxdemod-ddemod-fetch-measurement-waveform-vi.png']

#### Inputs/Outputs

| Selector String — Selector String comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxDemod Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. This value is expressed in seconds. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Measurement Waveform — Measurement Waveform returns the demodulated waveform used for measurement. x0 — x0 returns the start sample index. dx — dx returns the spacing between samples normalized to samples per symbol. y — y returns the measured samples. Samples Per Symbol — Samples Per Symbol returns the samples per symbol. Symbol Rate (Hz) — Symbol Rate returns the symbol rate in Hz. The default value is 100 kHz. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| x0 — x0 returns the start sample index. dx — dx returns the spacing between samples normalized to samples per symbol. y — y returns the measured samples. |

Parent topic:

RFmxDemod DDemod Fetch VI

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-fetch-offset-constellation-trace-vi.html language=enus -->
## TOPIC 00126: RFmxDemod DDemod Fetch Offset Constellation Trace VI

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-fetch-offset-constellation-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-fetch-offset-constellation-trace-vi.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the offset constellation trace. icon Inputs/Outputs cstr.png Selector String Selector String comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The

### RFmxDemod DDemod Fetch Offset Constellation Trace VI

Fetches the offset constellation trace.

[IMAGE alt='icon' src='rfmxdemod-ddemod-fetch-offset-constellation-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxDemod Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. This value is expressed in seconds. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Offset Constellation Trace — Offset Constellation Trace returns the offset constellation trace. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxDemod DDemod Fetch VI

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-fetch-offset-evm-trace-vi.html language=enus -->
## TOPIC 00127: RFmxDemod DDemod Fetch Offset EVM Trace VI

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-fetch-offset-evm-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-fetch-offset-evm-trace-vi.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the offset error vector magnitude (EVM) trace measured on OQPSK signal. icon Inputs/Outputs cstr.png Selector String Selector String comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, t

### RFmxDemod DDemod Fetch Offset EVM Trace VI

Fetches the offset error vector magnitude (EVM) trace measured on OQPSK signal.

[IMAGE alt='icon' src='rfmxdemod-ddemod-fetch-offset-evm-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxDemod Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. This value is expressed in seconds. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Offset EVM (%) — Offset EVM returns the offset EVM trace. x0 — x0 returns the start symbol index. dx — dx returns the spacing between symbols normalized to symbol rate. y — y returns the offset EVM per symbol. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| x0 — x0 returns the start symbol index. dx — dx returns the spacing between symbols normalized to symbol rate. y — y returns the offset EVM per symbol. |

Parent topic:

RFmxDemod DDemod Fetch VI

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-fetch-offset-evm-vi.html language=enus -->
## TOPIC 00128: RFmxDemod DDemod Fetch Offset EVM VI

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-fetch-offset-evm-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-fetch-offset-evm-vi.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the offset error vector magnitude (EVM). icon Inputs/Outputs cstr.png Selector String Selector String comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is u

### RFmxDemod DDemod Fetch Offset EVM VI

Fetches the offset error vector magnitude (EVM).

[IMAGE alt='icon' src='rfmxdemod-ddemod-fetch-offset-evm-vi.png']

#### Inputs/Outputs

| Selector String — Selector String comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxDemod Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. This value is expressed in seconds. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Mean Peak Offset EVM (%) — Mean Peak Offset EVM returns the mean of the peak EVM, measured per acquisition, after removing the offset between the I and Q channels of OQPSK demodulated signal. Maximum Peak Offset EVM (%) — Maximum Peak Offset EVM returns the maximum of the peak EVM, measured per acquisition, after removing the offset between the I and Q channels of OQPSK demodulated signal. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Mean RMS Offset EVM (%) — Mean RMS Offset EVM returns the mean of the RMS EVM, measured per acquisition, after removing the offset between the I and Q channels of OQPSK demodulated signal. Maximum RMS Offset EVM (%) — Maximum RMS Offset EVM returns the maximum of the RMS EVM, measured per acquisition, after removing the offset between the I and Q channels of OQPSK demodulated signal. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxDemod DDemod Fetch VI

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-fetch-phase-error-trace-vi.html language=enus -->
## TOPIC 00129: RFmxDemod DDemod Fetch Phase Error Trace VI

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-fetch-phase-error-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-fetch-phase-error-trace-vi.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the phase error trace. icon Inputs/Outputs cstr.png Selector String Selector String comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default v

### RFmxDemod DDemod Fetch Phase Error Trace VI

Fetches the phase error trace.

[IMAGE alt='icon' src='rfmxdemod-ddemod-fetch-phase-error-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxDemod Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. This value is expressed in seconds. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Phase Error (deg) — Phase Error returns the phase error. x0 — x0 returns the start symbol index. dx — dx returns the spacing between symbols normalized to symbol rate. y — y returns the phase error per symbol. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| x0 — x0 returns the start symbol index. dx — dx returns the spacing between symbols normalized to symbol rate. y — y returns the phase error per symbol. |

Parent topic:

RFmxDemod DDemod Fetch VI

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-fetch-phase-error-vi.html language=enus -->
## TOPIC 00130: RFmxDemod DDemod Fetch Phase Error VI

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-fetch-phase-error-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-fetch-phase-error-vi.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the phase error measurements. icon Inputs/Outputs cstr.png Selector String Selector String comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The de

### RFmxDemod DDemod Fetch Phase Error VI

Fetches the phase error measurements.

[IMAGE alt='icon' src='rfmxdemod-ddemod-fetch-phase-error-vi.png']

#### Inputs/Outputs

| Selector String — Selector String comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxDemod Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. This value is expressed in seconds. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Mean Phase Error (deg) — Mean Phase Error returns the mean of the phase error. Maximum Phase Error (deg) — Maximum Phase Error returns the maximum of the phase error. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxDemod DDemod Fetch VI

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-fetch-reference-waveform-vi.html language=enus -->
## TOPIC 00131: RFmxDemod DDemod Fetch Reference Waveform VI

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-fetch-reference-waveform-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-fetch-reference-waveform-vi.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the reference waveform. icon Inputs/Outputs cstr.png Selector String Selector String comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default

### RFmxDemod DDemod Fetch Reference Waveform VI

Fetches the reference waveform.

[IMAGE alt='icon' src='rfmxdemod-ddemod-fetch-reference-waveform-vi.png']

#### Inputs/Outputs

| Selector String — Selector String comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxDemod Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. This value is expressed in seconds. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Reference Waveform — Reference Waveform returns the reference waveform. x0 — x0 returns the start sample index. dx — dx returns the spacing between samples normalized to samples per symbol. y — y returns the reference samples. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| x0 — x0 returns the start sample index. dx — dx returns the spacing between samples normalized to samples per symbol. y — y returns the reference samples. |

Parent topic:

RFmxDemod DDemod Fetch VI

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-fetch-sync-found-vi.html language=enus -->
## TOPIC 00132: RFmxDemod DDemod Fetch Sync Found VI

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-fetch-sync-found-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-fetch-sync-found-vi.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates whether synchronization bits were found in the demodulated symbol. icon Inputs/Outputs cstr.png Selector String Selector String comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the

### RFmxDemod DDemod Fetch Sync Found VI

Indicates whether synchronization bits were found in the demodulated symbol.

[IMAGE alt='icon' src='rfmxdemod-ddemod-fetch-sync-found-vi.png']

#### Inputs/Outputs

| Selector String — Selector String comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxDemod Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. This value is expressed in seconds. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Sync Found? — Sync Found? returns TRUE if the synchronization bits was found in the demodulated signal. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxDemod DDemod Fetch VI

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-fetch-vi.html language=enus -->
## TOPIC 00133: RFmxDemod DDemod Fetch VI

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-fetch-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-fetch-vi.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the digital demodulation measurements. icon

### RFmxDemod DDemod Fetch VI

Fetches the digital demodulation measurements.

[IMAGE alt='icon' src='rfmxdemod-ddemod-fetch-vi.png']

- [RFmxDemod DDemod Fetch Carrier Measurement VI](../../../../../vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-fetch-carrier-measurement-vi.html) Fetches the carrier measurement.
- [RFmxDemod DDemod Fetch EVM VI](../../../../../vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-fetch-evm-vi.html) Fetches the EVM measurements.
- [RFmxDemod DDemod Fetch Offset EVM VI](../../../../../vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-fetch-offset-evm-vi.html) Fetches the offset error vector magnitude (EVM).
- [RFmxDemod DDemod Fetch Magnitude Error VI](../../../../../vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-fetch-magnitude-error-vi.html) Fetches the magnitude error measurements.
- [RFmxDemod DDemod Fetch Phase Error VI](../../../../../vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-fetch-phase-error-vi.html) Fetches the phase error measurements.
- [RFmxDemod DDemod Fetch FSK Results VI](../../../../../vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-fetch-fsk-results-vi.html) Fetches frequency-shift keying (FSK) results.
- [RFmxDemod DDemod Fetch Sync Found VI](../../../../../vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-fetch-sync-found-vi.html) Indicates whether synchronization bits were found in the demodulated symbol.
- [RFmxDemod DDemod Fetch IQ Impairments VI](../../../../../vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-fetch-iq-impairments-vi.html) Fetches I/Q impairments.
- [RFmxDemod DDemod Fetch Mean Amplitude Droop VI](../../../../../vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-fetch-mean-amplitude-droop-vi.html) Fetches the mean amplitude droop per symbol.
- [RFmxDemod DDemod Fetch Mean IQ Origin Offset VI](../../../../../vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-fetch-mean-iq-origin-offset-vi.html) Fetches the offset, in dB, from the ideal location of the constellation origin.
- [RFmxDemod DDemod Fetch Mean Quadrature Skew VI](../../../../../vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-fetch-mean-quadrature-skew-vi.html) Fetches the mean quadrature skew.
- [RFmxDemod DDemod Fetch Mean Rho Factor VI](../../../../../vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-fetch-mean-rho-factor-vi.html) Fetches the correlation of the measurement waveform and the reference waveform.
- [RFmxDemod DDemod Fetch EVM Trace VI](../../../../../vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-fetch-evm-trace-vi.html) Fetches the EVM trace.
- [RFmxDemod DDemod Fetch Offset EVM Trace VI](../../../../../vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-fetch-offset-evm-trace-vi.html) Fetches the offset error vector magnitude (EVM) trace measured on OQPSK signal.
- [RFmxDemod DDemod Fetch Magnitude Error Trace VI](../../../../../vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-fetch-magnitude-error-trace-vi.html) Fetches the magnitude error trace.
- [RFmxDemod DDemod Fetch Phase Error Trace VI](../../../../../vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-fetch-phase-error-trace-vi.html) Fetches the phase error trace.
- [RFmxDemod DDemod Fetch FSK Deviation Trace VI](../../../../../vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-fetch-fsk-deviation-trace-vi.html) Fetches the frequency-shift keying (FSK) deviation trace.
- [RFmxDemod DDemod Fetch Constellation Trace VI](../../../../../vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-fetch-constellation-trace-vi.html) Fetches the constellation trace.
- [RFmxDemod DDemod Fetch Offset Constellation Trace VI](../../../../../vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-fetch-offset-constellation-trace-vi.html) Fetches the offset constellation trace.
- [RFmxDemod DDemod Fetch Measurement Waveform VI](../../../../../vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-fetch-measurement-waveform-vi.html) Fetches the measurement waveform.
- [RFmxDemod DDemod Fetch Reference Waveform VI](../../../../../vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-fetch-reference-waveform-vi.html) Fetches the reference waveform.
- [RFmxDemod DDemod Fetch Demodulated Bits VI](../../../../../vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-fetch-demodulated-bits-vi.html) Fetches the demodulated bit stream.
- [RFmxDemod DDemod Fetch Equalizer Coefficients VI](../../../../../vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-fetch-equalizer-coefficients-vi.html) Fetches the updated equalizer coefficients.

Parent topic:

Fetch

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-get-equalizer-initial-coefficients-vi.html language=enus -->
## TOPIC 00134: RFmxDemod DDemod Get Equalizer Initial Coefficients VI

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-get-equalizer-initial-coefficients-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-get-equalizer-initial-coefficients-vi.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the initial equalizer coefficients used by the digital demodulation measurement. icon Inputs/Outputs cstr.png Selector String Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example

### RFmxDemod DDemod Get Equalizer Initial Coefficients VI

Gets the initial equalizer coefficients used by the digital demodulation measurement.

[IMAGE alt='icon' src='rfmxdemod-ddemod-get-equalizer-initial-coefficients-vi.png']

#### Inputs/Outputs

| Selector String — Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxDemod Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. — Equalizer Initial Coefficients returns the equalizer initial coefficients. x0 — x0 this parameter always returns 0. dx — dx returns the spacing between the coefficients as a fraction of the symbol spacing. For example, if four coefficients correspond to one symbol, the spacing is 1/4. y — y returns the filter coefficients used as the equalizer initial coefficients. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| x0 — x0 this parameter always returns 0. dx — dx returns the spacing between the coefficients as a fraction of the symbol spacing. For example, if four coefficients correspond to one symbol, the spacing is 1/4. y — y returns the filter coefficients used as the equalizer initial coefficients. |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-get-symbol-map-vi.html language=enus -->
## TOPIC 00135: RFmxDemod DDemod Get Symbol Map VI

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-get-symbol-map-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-get-symbol-map-vi.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the symbol map that is used for digital demodulation measurements. Call this VI after calling RFmxDemod Commit VI. icon Inputs/Outputs cstr.png Selector String Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default v

### RFmxDemod DDemod Get Symbol Map VI

Gets the symbol map that is used for digital demodulation measurements. Call this VI after calling [RFmxDemod Commit](/csh?context=rfmxdemod_rfmxdemodvi_rfmxdemod_commit) VI.

[IMAGE alt='icon' src='rfmxdemod-ddemod-get-symbol-map-vi.png']

#### Inputs/Outputs

| Selector String — Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxDemod Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. — Symbol Map returns the symbol map used for demodulation. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-read-vi.html language=enus -->
## TOPIC 00136: RFmxDemod DDemod Read VI

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-read-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-read-vi.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures hardware for acquisition, performs measurement on acquired data for modulation type configured using the RFmxDemod DDemod Configure Modulation Type VI, and returns the frequency offset, EVM, and MER results. icon Inputs/Outputs cstr.png Selector String Selector String comprises of the sig

### RFmxDemod DDemod Read VI

Configures hardware for acquisition, performs measurement on acquired data for modulation type configured using the [RFmxDemod DDemod Configure Modulation Type](/csh?context=rfmxdemod_rfmxdemodvi_rfmxdemod_ddemod_configure_modulation_type) VI, and returns the frequency offset, EVM, and MER results.

[IMAGE alt='icon' src='rfmxdemod-ddemod-read-vi.png']

#### Inputs/Outputs

| Selector String — Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxDemod Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. This value is expressed in seconds. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Mean Modulation Error Ratio (dB) — Mean Modulation Error Ratio returns the modulation error ratio, in dB. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Mean Frequency Offset (Hz) — Mean Frequency Offset returns the mean of the measured carrier frequency offset, in Hz. Mean RMS EVM (%) — Mean RMS EVM returns the mean of the RMS EVM measured per acquisition. Maximum Peak EVM (%) — Maximum Peak EVM returns the maximum of the peak EVM measured per acquisition. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxDemod Read VI

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-delete-signal-configuration-vi.html language=enus -->
## TOPIC 00137: RFmxDemod Delete Signal Configuration VI

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-delete-signal-configuration-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-delete-signal-configuration-vi.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Deletes an instance of the signal that you specify in the Signal Name parameter. icon Inputs/Outputs cstr.png Signal Name Signal Name specifies the name of the signal. This parameter accepts the signal name with or without the "signal::" prefix. Example: "signal::sig1" "sig1" cgenclassrntag.png Inst

### RFmxDemod Delete Signal Configuration VI

Deletes an instance of the signal that you specify in the **Signal Name** parameter.

[IMAGE alt='icon' src='rfmxdemod-delete-signal-configuration-vi.png']

#### Inputs/Outputs

| Signal Name — Signal Name specifies the name of the signal. This parameter accepts the signal name with or without the "signal::" prefix. Example: "signal::sig1" "sig1" Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-disable-trigger-vi.html language=enus -->
## TOPIC 00138: RFmxDemod Disable Trigger VI

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-disable-trigger-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-disable-trigger-vi.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Disables the trigger. icon Inputs/Outputs cstr.png Selector String Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxDemod Build Signal Strin

### RFmxDemod Disable Trigger VI

Disables the trigger.

[IMAGE alt='icon' src='rfmxdemod-disable-trigger-vi.png']

#### Inputs/Outputs

| Selector String — Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxDemod Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxDemod Configure Trigger VI

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-get-all-named-result-names-vi.html language=enus -->
## TOPIC 00139: RFmxDemod Get All Named Result Names VI

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-get-all-named-result-names-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-get-all-named-result-names-vi.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns all the named result names of the signal that you specify in the Selector String parameter. icon Inputs/Outputs cstr.png Selector String Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty st

### RFmxDemod Get All Named Result Names VI

Returns all the named result names of the signal that you specify in the Selector String parameter.

[IMAGE alt='icon' src='rfmxdemod-get-all-named-result-names-vi.png']

#### Inputs/Outputs

| Selector String — Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxDemod Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Result Names — Result Names returns an array of result names. Default Result Exists? — Default Result Exists? indicates whether the default result exists. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-initiate-vi.html language=enus -->
## TOPIC 00140: RFmxDemod Initiate VI

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-initiate-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-initiate-vi.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initiates all enabled measurements. Call this VI after configuring the signal and measurement. This VI asynchronously launches measurements in the background and immediately returns to the caller program. You can fetch measurement results using the Fetch VIs or result properties in the property node

### RFmxDemod Initiate VI

Initiates all enabled measurements. Call this VI after configuring the signal and measurement. This VI asynchronously launches measurements in the background and immediately returns to the caller program. You can fetch measurement results using the Fetch VIs or result properties in the property node. To get the status of measurements, you can use the [RFmxDemod Wait for Measurement Complete](/csh?context=rfmxdemod_rfmxdemodvi_rfmxdemod_wait_for_measurement_complete) VI or the [RFmxDemod Check Measurement Status](/csh?context=rfmxdemod_rfmxdemodvi_rfmxdemod_check_measurement_status) VI.

[IMAGE alt='icon' src='rfmxdemod-initiate-vi.png']

#### Inputs/Outputs

| Result Name — Result Name specifies the name to be associated with measurement results. Provide a unique name, such as "r1" to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. The default value is "" (empty string) which refers to default result instance. Example: "result::r1" "r1" Selector String — Selector String specifies a selector string comprising of the signal name and result name. The result name can either be specified through this input or the Result Name parameter. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name in this input, either the result name specified by Result Name parameter or the default result instance is used. The default is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxDemod Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Selector String Out — Selector String Out returns the selector string that can be passed to the Selector String parameter on Fetch VIs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Demod

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-property-node-vi.html language=enus -->
## TOPIC 00141: RFmxDemod Property Node VI

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-property-node-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-property-node-vi.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets (writes), gets (reads), or resets (sets to default value) RFmxDemod properties. icon Inputs/Outputs cgenclassrntag.png niRFmx Instrument Handle Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. cerrcodeclst.png erro

### RFmxDemod Property Node VI

Sets (writes), gets (reads), or resets (sets to default value) RFmxDemod properties.

[IMAGE alt='icon' src='rfmxdemod-property-node-vi.png']

#### Inputs/Outputs

| niRFmx Instrument Handle — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Property — RFmx Demod Property Node is used to get (read), set (write), or reset (set to default value) RFmx Demod properties. niRFmx Instrument Handle — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Demod

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-read-vi.html language=enus -->
## TOPIC 00142: RFmxDemod Read VI

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-read-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-read-vi.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures hardware for acquisition, performs measurement on acquired data, and returns measurement results. icon

### RFmxDemod Read VI

Configures hardware for acquisition, performs measurement on acquired data, and returns measurement results.

[IMAGE alt='icon' src='rfmxdemod-read-vi.png']

- [RFmxDemod ADemod Read AM VI](../../../../../vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ademod-read-am-vi.html) Configures hardware for acquisition, performs measurement on acquired data, and returns the AM measurement results.
- [RFmxDemod ADemod Read FM VI](../../../../../vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ademod-read-fm-vi.html) Configures hardware for acquisition, performs measurement on acquired data, and returns the FM measurement results.
- [RFmxDemod ADemod Read PM VI](../../../../../vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ademod-read-pm-vi.html) Configures hardware for acquisition, performs measurement on acquired data, and returns the PM measurement results.
- [RFmxDemod DDemod Read VI](../../../../../vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-ddemod-read-vi.html) Configures hardware for acquisition, performs measurement on acquired data for modulation type configured using the RFmxDemod DDemod Configure Modulation Type VI, and returns the frequency offset, EVM, and MER results.

Parent topic:

Demod

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-reset-to-default-vi.html language=enus -->
## TOPIC 00143: RFmxDemod Reset to Default VI

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-reset-to-default-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-reset-to-default-vi.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Resets a signal to the default values. icon Inputs/Outputs cstr.png Selector String Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxDemod B

### RFmxDemod Reset to Default VI

Resets a signal to the default values.

[IMAGE alt='icon' src='rfmxdemod-reset-to-default-vi.png']

#### Inputs/Outputs

| Selector String — Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxDemod Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-select-measurement-multiple-vi.html language=enus -->
## TOPIC 00144: RFmxDemod Select Measurement (Multiple) VI

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-select-measurement-multiple-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-select-measurement-multiple-vi.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enables all the measurements that you specify in the Measurements parameter and disables all other measurements. icon Inputs/Outputs cstr.png Selector String Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is

### RFmxDemod Select Measurement (Multiple) VI

Enables all the measurements that you specify in the **Measurements** parameter and disables all other measurements.

[IMAGE alt='icon' src='rfmxdemod-select-measurement-multiple-vi.png']

#### Inputs/Outputs

| Selector String — Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxDemod Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Measurements — Measurements specifies an array of measurements to perform. You can specify the following measurements. ADemod (0) Enables analog demodulation measurements. DDemod (1) Enables digital demodulation measurements. Enable All Traces — Enable All Traces specifies whether to enable all the traces for the selected measurements. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| ADemod (0) | Enables analog demodulation measurements. |
| DDemod (1) | Enables digital demodulation measurements. |

Parent topic:

RFmxDemod Select Measurement VI

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-select-measurement-single-vi.html language=enus -->
## TOPIC 00145: RFmxDemod Select Measurement (Single) VI

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-select-measurement-single-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-select-measurement-single-vi.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enables the measurement that you specify in the Measurement parameter and disables all other measurements. icon Inputs/Outputs cstr.png Selector String Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (e

### RFmxDemod Select Measurement (Single) VI

Enables the measurement that you specify in the **Measurement** parameter and disables all other measurements.

[IMAGE alt='icon' src='rfmxdemod-select-measurement-single-vi.png']

#### Inputs/Outputs

| Selector String — Selector String comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxDemod Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Measurement — Measurement specifies the measurement to perform. You can specify one of the following measurements. ADemod (0) Enables analog demodulation measurement. DDemod (1) Enables digital demodulation measurement. Enable All Traces — Enable All Traces specifies whether to enable all the traces for the selected measurement. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| ADemod (0) | Enables analog demodulation measurement. |
| DDemod (1) | Enables digital demodulation measurement. |

Parent topic:

RFmxDemod Select Measurement VI

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-vi-tree-vi.html language=enus -->
## TOPIC 00146: RFmxDemod VI Tree VI

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-vi-tree-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/vi-lib/rfmx/demod/mx/rfmxdemod-llb/rfmxdemod-vi-tree-vi.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Displays all the VIs available in RFmxDemod for measurement configuration, control, and fetching results. The VIs are organized in the order they are supposed to be used in a program that you create. icon

### RFmxDemod VI Tree VI

Displays all the VIs available in RFmxDemod for measurement configuration, control, and fetching results. The VIs are organized in the order they are supposed to be used in a program that you create.

[IMAGE alt='icon' src='rfmxdemod-vi-tree-vi.png']

Parent topic:

Demod

<!--NI_TOPIC bundle=rfmxdemod-labview-api-ref path=vi-lib/rfmx/demod/mx/rfmxdemod-llb/standard-functionality-for-error-in-parameters.html language=enus -->
## TOPIC 00147: Using the Standard Functionality for error in Parameters

- bundle_id: `rfmxdemod-labview-api-ref`
- source_path: `vi-lib/rfmx/demod/mx/rfmxdemod-llb/standard-functionality-for-error-in-parameters.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-labview-api-ref/raw/resource/enus/vi-lib/rfmx/demod/mx/rfmxdemod-llb/standard-functionality-for-error-in-parameters.html
- document_id: `rfmxdemod-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Many LabVIEW nodes such as VIs contain error in parameters you can use to manage errors. These parameters typically provide the same, standard functionality. When a node exhibits different parameter functionality, the exceptions are documented in the reference material for that node. Standard error

### Using the Standard Functionality for error in Parameters

Many LabVIEW nodes such as VIs contain error in parameters you can use to manage errors. These parameters typically provide the same, standard functionality. When a node exhibits different parameter functionality, the exceptions are documented in the reference material for that node. Standard error in behavior is as follows

Note

error in

error in

|  | error in describes error conditions that occur before this node runs. The default is no error. If an error occurred before this node runs, the node passes the error in value to error out. This node runs normally only if no error occurred before this node runs. If an error occurs while this node runs, it runs normally and sets its own error status in error out. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. |
| --- | --- |

The error in cluster contains the following cluster elements:

|  | status is TRUE (X) if an error occurred before this node ran or FALSE (checkmark) to indicate a warning or that no error occurred before this node ran. The default is FALSE. |
| --- | --- |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is an error code. If status is FALSE, code is 0 or a warning code. |
|  | source specifies the origin of the error or warning and is, in most cases, the name of the node that produced the error or warning. The default is an empty string. |
