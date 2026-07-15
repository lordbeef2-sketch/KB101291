# NI DOCUMENT BUNDLE: rfmxpulse-labview-api-ref

<!--NI_BUNDLE_CHUNK bundle=rfmxpulse-labview-api-ref start=1 end=118 -->
<!--NI_TOPIC bundle=rfmxpulse-labview-api-ref path=menus/categories/measurement/rfmx/pulse/rfmx-pulse-mx-advanced-mnu.html language=enus -->
## TOPIC 00001: Advanced

- bundle_id: `rfmxpulse-labview-api-ref`
- source_path: `menus/categories/measurement/rfmx/pulse/rfmx-pulse-mx-advanced-mnu.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-labview-api-ref/raw/resource/enus/menus/categories/measurement/rfmx/pulse/rfmx-pulse-mx-advanced-mnu.html
- document_id: `rfmxpulse-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the VIs on this palette to use advanced features. icon

### Advanced

Use the VIs on this palette to use advanced features.

[IMAGE alt='icon' src='rfmx-pulse-mx-advanced-mnu.png']

- [RFmxPulse Abort Measurements VI](../../../../../vi-lib/rfmx/pulse/mx/rfmxpulse-llb/rfmxpulse-abort-measurements-vi.html) Stops acquisition and measurements associated with signal instance that you specify in the Selector String parameter, which were previously initiated by the RFmxPulse Initiate VI or measurement read VIs. Calling this VI is optional, unless you want to stop a measurement before it is complete. This VI executes even if there is an incoming error.
- [RFmxPulse Analyze (IQ, 1 Wfm) VI](../../../../../vi-lib/rfmx/pulse/mx/rfmxpulse-llb/rfmxpulse-analyze-iq-1-wfm-vi.html) Performs the enabled measurements on the I/Q complex waveform that you specify in IQ parameter. Call this VI after you configure the signal and measurement properties. You can fetch measurement results using the Fetch VIs or result properties in the property node. Use this VI only if the Recommended Acquisition Type property value is either IQ or IQ or Spectral .
- [RFmxPulse Create Signal Configuration VI](../../../../../vi-lib/rfmx/pulse/mx/rfmxpulse-llb/rfmxpulse-create-signal-configuration-vi.html) Creates a new instance of a signal.
- [RFmxPulse Clone Signal Configuration VI](../../../../../vi-lib/rfmx/pulse/mx/rfmxpulse-llb/rfmxpulse-clone-signal-configuration-vi.html) Creates a new instance of a signal by copying all the property values from an existing signal instance.
- [RFmxPulse Delete Signal Configuration VI](../../../../../vi-lib/rfmx/pulse/mx/rfmxpulse-llb/rfmxpulse-delete-signal-configuration-vi.html) Deletes an instance of a signal that you specify in the Signal Name parameter.
- [RFmxPulse Get All Named Result Names VI](../../../../../vi-lib/rfmx/pulse/mx/rfmxpulse-llb/rfmxpulse-get-all-named-result-names-vi.html) Returns all the named result names of the signal that you specify in the Selector String parameter.
- [RFmxPulse Clear Named Result VI](../../../../../vi-lib/rfmx/pulse/mx/rfmxpulse-llb/rfmxpulse-clear-named-result-vi.html) Clears a result instance specified by the result name in the Selector String parameter.
- [RFmxPulse Clear All Named Results VI](../../../../../vi-lib/rfmx/pulse/mx/rfmxpulse-llb/rfmxpulse-clear-all-named-results-vi.html) Clears all results for the signal that you specify in the Selector String parameter.

Parent topic:

Pulse

<!--NI_TOPIC bundle=rfmxpulse-labview-api-ref path=resource/objmgr/rfmxpulse-rc/rfmxpulse-p.html language=enus -->
## TOPIC 00002: RFmxPulse Properties

- bundle_id: `rfmxpulse-labview-api-ref`
- source_path: `resource/objmgr/rfmxpulse-rc/rfmxpulse-p.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxpulse-rc/rfmxpulse-p.html
- document_id: `rfmxpulse-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the RFmxPulse properties to access options for configuring and fetching measurements. © 2022–2026 National Instruments Corporation. All rights reserved.

### RFmxPulse Properties

Use the RFmxPulse properties to access options for configuring and fetching measurements.

© 2022–2026 National Instruments Corporation. All rights reserved.

- [Acquisition Length (s)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc00011.html) Specifies the acquisition length for the pulse measurement. This value is expressed in seconds.
- [Advanced:Auto Level Initial Reference Level (dBm)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0000d.html) Specifies the initial reference level, in dBm, which the RFmxPulse Auto Level VI uses to estimate the peak power of the input signal.
- [Center Frequency (Hz)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc00001.html) Specifies the expected carrier frequency of the acquired RF signal. This value is expressed in Hz. The signal analyzer tunes to this frequency.
- [External Attenuation (dB)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc00003.html) Specifies the attenuation of a switch or cable connected to the RF IN connector of the signal analyzer. This value is expressed in dB. For more information about attenuation, refer to the RF Attenuation and Signal Levels topic for your device in the NI RF Vector Signal Analyzers Help .
- [Maximum Pulse Count:Enabled](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc00012.html) Specifies whether to enable the maximum pulse count for pulse measurements.
- [Maximum Pulse Count:Value](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc00013.html) Specifies the maximum number of pulses to be measured when you set the Max Pulse Count Enabled property to True .
- [Measurement Bandwidth (Hz)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc00017.html) Specifies the bandwidth of the filter used for the required sample rate. This value is expressed in Hz.
- [Measurement Filter Type](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc00018.html) Specifies the demodulation filter type to be used in the measurements.
- [Pulse:Acquisition Trace:Select](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0110e.html) Specifies the mode to select all pulses or the subset of acquired pulses available for display acquisition trace, limited to Max Pulse Count Enabled property if set to True .
- [Pulse:Acquisition Trace:Subset Length](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01110.html) Specifies the total number of pulses starting from offset to be used for display acquisition trace. You must configure this property when you set the Pulse Acquisition Trace Select property to Subset .
- [Pulse:Acquisition Trace:Subset Offset](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0110f.html) Specifies the offset in number of pulses to be used for display acquisition trace. You must configure this property when you set the Pulse Acquisition Trace Select property to Subset .
- [Pulse:All Traces Enabled](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0100e.html) Specifies whether to enable storing and retrieving traces after performing the measurements.
- [Pulse:Amplitude Trace Unit](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010dc.html) Specifies the unit of the amplitude level. This property is applicable only for the amplitude and acquired amplitude trace.
- [Pulse:Detection:Hysteresis (dB)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01004.html) Specifies the hysteresis for pulse detection in dB for the defined threshold.
- [Pulse:Detection:Maximum Width (s)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01007.html) Specifies the maximum pulse width time to be considered for pulse detection. Any detected pulse width time above the specified value will be ignored by the pulse detection. This value is expressed in seconds.
- [Pulse:Detection:Minimum Off Duration (s)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01005.html) Specifies the minimum pulse off duration to be ignored by the pulse detection. This value is expressed in seconds.
- [Pulse:Detection:Minimum Width (s)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01006.html) Specifies the minimum pulse width time to be considered for pulse detection. Any detected pulse width time below the specified value will be ignored by the pulse detection. This value is expressed in seconds.
- [Pulse:Detection:Reference](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01002.html) Specifies the reference used for Pulse Detection Threshold property.
- [Pulse:Detection:Threshold](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01003.html) Specifies the threshold used for pulse detection. The unit dB or dBm is based on the value you set to the Pulse Detection Reference property.
- [Pulse:Frequency and Phase: Deviation Range:Reference](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0108d.html) Specifies the reference used for the measurement range in phase/frequency deviation and error measurements.
- [Pulse:Frequency and Phase:CW Frequency Offset (Hz)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0109d.html) Specifies to manually enter the CW frequency offset. This property is valid only when you set the Pulse Modulation Type property to CW .
- [Pulse:Frequency and Phase:CW Frequency Offset Auto](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0109c.html) Specifies whether the CW frequency offset computation of every detected pulse is automatic or manual. This property is valid only when you set the Pulse Modulation Type property to CW .
- [Pulse:Frequency and Phase:Deviation Range:Edge Start (s)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0108f.html) Specifies the start of the pulse data used for the phase/frequency deviation and error measurements when you set the Pulse Freq Phase Dev Range Reference property to Edge .
- [Pulse:Frequency and Phase:Deviation Range:Edge Stop (s)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01090.html) Specifies the stop of the pulse data used for the phase/frequency deviation and error measurements when you set the Pulse Freq Phase Dev Range Reference property to Edge .
- [Pulse:Frequency and Phase:Deviation Range:Length (%)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0108e.html) Specifies the length of the pulse data used for the phase/frequency deviation and error measurements when you set the Pulse Freq Phase Dev Range Reference property to Center .
- [Pulse:Frequency and Phase:Modulation Type](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0109b.html) Specifies the pulse modulation type used for the phase and frequency error, and pulsed FM Measurement.
- [Pulse:Level:Amplitude Domain](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01009.html) Specifies whether voltage or power to be used as domain for pulse measurements.
- [Pulse:Level:Computation Method](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01008.html) Specifies the algorithm used to detect the pulse levels. The algorithm is based on the histogram method of level detection as defined in IEEE Std 181-2011 .
- [Pulse:Level:Droop Compensation Enabled](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0100d.html) Specifies whether to compensate the droop detected in pulse level when applying thresholds.
- [Pulse:Level:Lower Threshold (%)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0100c.html) Specifies the lower threshold level as a percentage of the pulse amplitude used to signify the start of a rising or end of a falling edge.
- [Pulse:Level:Upper Threshold (%)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0100a.html) Specifies the upper threshold level as a percentage of the pulse amplitude used to signify the end of a rising edge or beginning of a falling edge.
- [Pulse:Level:Width Threshold (%)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0100b.html) Specifies the middle threshold level as a percentage of the pulse amplitude used to signify the mid-transition level between pulse states used for pulse width computation.
- [Pulse:Measurement Enabled](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01000.html) Specifies whether pulse measurements are enabled.
- [Pulse:Measurement Point:Averaging Duration (s)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0108c.html) Specifies the length of the averaging window centered at the measurement point. A minimum of 1 sample is used internally.
- [Pulse:Measurement Point:Offset (s)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0108b.html) Specifies the time offset of the measurement point within the pulse for phase, frequency, and stability measurements.
- [Pulse:Measurement Point:Reference](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0108a.html) Specifies the reference used for the measurement point calculation, in phase, frequency, and stability measurements. You can set measurement point based on a reference and offset.
- [Pulse:Metrics:Amplitude Deviation Unit](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010dd.html) Specifies the unit for amplitude deviation results. This property is applicable only for droop, ripple and overshoot results.
- [Pulse:Metrics:Enabled](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0109a.html) Specifies whether to enable pulse metrics results computation.
- [Pulse:Multiburst:Enabled](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010de.html) Specifies whether to enable pulse measurements on the multiple burst transmission.
- [Pulse:Multiburst:Length (Pulses)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010df.html) Specifies the number of pulses assigned to a single burst.
- [Pulse:Multiple Measurement Points:Enabled](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010e3.html) Specifies whether to enable pulse stability measurements on multiple measurement points. This property enables the stability traces over multiple measurement points when you set the Pulse All Traces Enabled property to TRUE.
- [Pulse:Multiple Measurement Points:Window:Start (%)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010e4.html) Specifies the start of the measurement window used for multiple measurement points selection over pulse ON duration.
- [Pulse:Multiple Measurement Points:Window:Step Size (%)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010e6.html) Specifies the step size of multiple measurement points selection within the measurement window over pulse ON duration. A minimum of 1 sample step size is used internally.
- [Pulse:Multiple Measurement Points:Window:Stop (%)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010e5.html) Specifies the stop of the measurement window used for multiple measurement points selection over pulse ON duration.
- [Pulse:Number of Analysis Threads](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01088.html) Specifies the maximum number of threads used for parallelism for the pulse measurement.
- [Pulse:Results:Burst Index](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010e1.html) Returns the burst indices of all the measured pulses.
- [Pulse:Results:FM Chirp:Rate (Hz/us)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010b4.html) Returns the frequency slope rate of a best-fit linear least square regression line measured over user specified sample analysis time interval as determined by Pulse Freq Phase Dev Range Length (%) property for each pulse. This value is expressed in Hz/us. This result is valid for linear FM and triangular FM modulation.
- [Pulse:Results:FM Chirp:Rate Maximum (Hz/us)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010b6.html) Returns the maximum FM chirp rate across the measured pulses. This value is expressed in Hz/us. This result is valid for linear FM and triangular FM modulation.
- [Pulse:Results:FM Chirp:Rate Mean (Hz/us)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010b5.html) Returns the mean of the FM chirp rates across the measured pulses. This value is expressed in Hz/us. This result is valid for linear FM and triangular FM modulation.
- [Pulse:Results:FM Chirp:Rate Minimum (Hz/us)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010b7.html) Returns the minimum FM chirp rate across the measured pulses. This value is expressed in Hz/us. This result is valid for linear FM and triangular FM modulation.
- [Pulse:Results:FM Chirp:Rate Standard Deviation (Hz/us)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010b8.html) Returns the standard deviation of the FM chirp rates across the measured pulses. This value is expressed in Hz/us. This result is valid for linear FM and triangular FM modulation.
- [Pulse:Results:FM Chirp:Rate2 (Hz/us)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010cd.html) Returns the frequency slope rate of the 2nd best-fit linear least square regression line measured over user specified sample analysis time interval as determined by Pulse Freq Phase Dev Range Length (%) property for the measured pulses. This value is expressed in Hz/us. This result is valid only for triangular FM modulation.
- [Pulse:Results:FM Chirp:Rate2 Maximum (Hz/us)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010cf.html) Returns the maximum FM chirp rate2 value across the measured pulses. This value is expressed in Hz/us. This result is valid only for triangular FM modulation.
- [Pulse:Results:FM Chirp:Rate2 Mean (Hz/us)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010ce.html) Returns the mean of the FM chirp rate2 values across the measured pulses. This value is expressed in Hz/us. This result is valid only for triangular FM modulation.
- [Pulse:Results:FM Chirp:Rate2 Minimum (Hz/us)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010d0.html) Returns the minimum FM chirp rate2 value across the measured pulses. This value is expressed in Hz/us. This result is valid only for triangular FM modulation.
- [Pulse:Results:FM Chirp:Rate2 Standard Deviation (Hz/us)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010d1.html) Returns the standard deviation of the FM chirp rate2 values across the measured pulses. This value is expressed in Hz/us. This result is valid only for triangular FM modulation.
- [Pulse:Results:FM Chirp:Start Frequency (Hz)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010b9.html) Returns the start frequencies of the best-fit linear least square regression line measured over user specified sample analysis time interval as determined by Pulse Freq Phase Dev Range Length (%) property for the measured pulses. This value is expressed in Hz. This result is valid for linear FM and triangular FM modulation.
- [Pulse:Results:FM Chirp:Start Frequency Maximum (Hz)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010bb.html) Returns the maximum FM chirp start frequency among the measured pulses. This value is expressed in Hz. This result is valid for linear FM and triangular FM modulation.
- [Pulse:Results:FM Chirp:Start Frequency Mean (Hz)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010ba.html) Returns the mean of the FM chirp start frequency across the measured pulses. This value is expressed in Hz. This result is valid for linear FM and triangular FM modulation.
- [Pulse:Results:FM Chirp:Start Frequency Minimum (Hz)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010bc.html) Returns the minimum FM chirp start frequency among the measured pulses. This value is expressed in Hz. This result is valid for linear FM and triangular FM modulation.
- [Pulse:Results:FM Chirp:Start Frequency Standard Deviation (Hz)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010bd.html) Returns the FM chirp start frequency standard deviation across the measured pulses. This value is expressed in Hz. This result is valid for linear FM and triangular FM modulation.
- [Pulse:Results:FM Chirp:Start Frequency2 (Hz)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010d2.html) Returns the start frequency of the 2nd best-fit linear least square regression line measured over user specified sample analysis time interval as determined by Pulse Freq Phase Dev Range Length (%) property for the measured pulses. This value is expressed in Hz. This result is valid only for triangular FM modulation.
- [Pulse:Results:FM Chirp:Start Frequency2 Maximum (Hz)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010d4.html) Returns the maximum FM chirp start frequency2 among the measured pulses. This value is expressed in Hz. This result is valid only for triangular FM modulation.
- [Pulse:Results:FM Chirp:Start Frequency2 Mean (Hz)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010d3.html) Returns the mean of the FM chirp start frequency2 across the measured pulses. This value is expressed in Hz. This result is valid only for triangular FM modulation.
- [Pulse:Results:FM Chirp:Start Frequency2 Minimum (Hz)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010d5.html) Returns the minimum FM chirp start frequency2 among the measured pulses. This value is expressed in Hz. This result is valid only for triangular FM modulation.
- [Pulse:Results:FM Chirp:Start Frequency2 Standard Deviation (Hz)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010d6.html) Returns the FM chirp start frequency2 standard deviation across the measured pulses. This value is expressed in Hz. This result is valid only for triangular FM modulation.
- [Pulse:Results:FM Chirp:Stop Frequency (Hz)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010be.html) Returns the stop frequencies of the best-fit linear least square regression line measured over user specified sample analysis time interval as determined by Pulse Freq Phase Dev Range Length (%) property for the measured pulses. This value is expressed in Hz. This result is valid for linear FM and triangular FM modulation.
- [Pulse:Results:FM Chirp:Stop Frequency Maximum (Hz)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010c0.html) Returns the maximum FM chirp stop frequency among the measured pulses. This value is expressed in Hz. This result is valid for linear FM and triangular FM modulation.
- [Pulse:Results:FM Chirp:Stop Frequency Mean (Hz)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010bf.html) Returns the mean of the FM chirp stop frequency across the measured pulses. This value is expressed in Hz. This result is valid for linear FM and triangular FM modulation.
- [Pulse:Results:FM Chirp:Stop Frequency Minimum (Hz)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010c1.html) Returns the minimum FM chirp stop frequency among the measured pulses. This value is expressed in Hz. This result is valid for linear FM and triangular FM modulation.
- [Pulse:Results:FM Chirp:Stop Frequency Standard Deviation (Hz)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010c2.html) Returns the FM chirp stop frequency standard deviation across the measured pulses. This value is expressed in Hz. This result is valid for linear FM and triangular FM modulation.
- [Pulse:Results:FM Chirp:Stop Frequency2 (Hz)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010d7.html) Returns the stop frequency of the 2nd best-fit linear least square regression line measured over user specified sample analysis time interval as determined by Pulse Freq Phase Dev Range Length (%) property for the measured pulses. This value is expressed in Hz. This result is valid only for triangular FM modulation.
- [Pulse:Results:FM Chirp:Stop Frequency2 Maximum (Hz)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010d9.html) Returns the maximum FM chirp stop frequency2 among the measured pulses. This value is expressed in Hz. This result is valid only for triangular FM modulation.
- [Pulse:Results:FM Chirp:Stop Frequency2 Mean (Hz)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010d8.html) Returns the mean of the FM chirp stop frequency2 across the measured pulses. This value is expressed in Hz. This result is valid only for triangular FM modulation.
- [Pulse:Results:FM Chirp:Stop Frequency2 Minimum (Hz)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010da.html) Returns the minimum FM chirp stop frequency2 among the measured pulses. This value is expressed in Hz. This result is valid only for triangular FM modulation.
- [Pulse:Results:FM Chirp:Stop Frequency2 Standard Deviation (Hz)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010db.html) Returns the FM chirp stop frequency2 standard deviation across the measured pulses. This value is expressed in Hz. This result is valid only for triangular FM modulation.
- [Pulse:Results:Frequency and Phase:Average Frequency (Hz)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0106a.html) Returns the average frequencie for all measured pulses. This value is expressed in Hz.
- [Pulse:Results:Frequency and Phase:Average Frequency Maximum (Hz)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0106c.html) Returns the maximum average frequency across the measured pulses. This value is expressed in Hz.
- [Pulse:Results:Frequency and Phase:Average Frequency Mean (Hz)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0106b.html) Returns the mean of the average frequency across the measured pulses. This value is expressed in Hz.
- [Pulse:Results:Frequency and Phase:Average Frequency Minimum (Hz)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0106d.html) Returns the minimum average frequency across the measured pulses. This value is expressed in Hz.
- [Pulse:Results:Frequency and Phase:Average Frequency Standard Deviation (Hz)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0106e.html) Returns the standard deviation of the average frequency across the measured pulses. This value is expressed in Hz.
- [Pulse:Results:Frequency and Phase:Average Phase (deg)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0105b.html) Returns the average phase for all measured pulses. This value is expressed in degrees.
- [Pulse:Results:Frequency and Phase:Average Phase Maximum (deg)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0105d.html) Returns the maximum average phase across the measured pulses. This value is expressed in degrees.
- [Pulse:Results:Frequency and Phase:Average Phase Mean (deg)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0105c.html) Returns the mean of the average phase across the measured pulses. This value is expressed in degrees.
- [Pulse:Results:Frequency and Phase:Average Phase Minimum (deg)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0105e.html) Returns the minimum average phase across the measured pulses. This value is expressed in degrees.
- [Pulse:Results:Frequency and Phase:Average Phase Standard Deviation (deg)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0105f.html) Returns the standard deviation of the average phase across the measured pulses. This value is expressed in degrees.
- [Pulse:Results:Frequency and Phase:Frequency Deviation (Hz)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01074.html) Returns the peak-to-peak frequency deviation for all measured pulses. This value is expressed in Hz.
- [Pulse:Results:Frequency and Phase:Frequency Deviation Maximum (Hz)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01076.html) Returns the maximum peak-to-peak phase deviation across the measured pulses. This value is expressed in Hz.
- [Pulse:Results:Frequency and Phase:Frequency Deviation Mean (Hz)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01075.html) Returns the mean of the peak-to-peak phase deviation across the measured pulses. This value is expressed in Hz.
- [Pulse:Results:Frequency and Phase:Frequency Deviation Minimum (Hz)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01077.html) Returns the minimum peak-to-peak frequency deviation across the measured pulses. This value is expressed in Hz.
- [Pulse:Results:Frequency and Phase:Frequency Deviation Standard Deviation (Hz)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01078.html) Returns the standard deviation of the peak-to-peak frequency deviation across the measured pulses. This value is expressed in Hz.
- [Pulse:Results:Frequency and Phase:Frequency Error Peak (Hz)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010ae.html) Returns the peak frequency error for all measured pulses. This value is expressed in Hz.
- [Pulse:Results:Frequency and Phase:Frequency Error Peak Location (s)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010b3.html) Returns the time locations corresponding to the peak frequency error of the measured pulses. This value is expressed in seconds.
- [Pulse:Results:Frequency and Phase:Frequency Error Peak Maximum (Hz)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010b0.html) Returns the maximum peak frequency error across the measured pulses. This value is expressed in Hz.
- [Pulse:Results:Frequency and Phase:Frequency Error Peak Mean (Hz)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010af.html) Returns the mean of the peak frequency error across the measured pulses. This value is expressed in Hz.
- [Pulse:Results:Frequency and Phase:Frequency Error Peak Minimum (Hz)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010b1.html) Returns the minimum peak frequency error across the measured pulses. This value is expressed in Hz.
- [Pulse:Results:Frequency and Phase:Frequency Error Peak Standard Deviation (Hz)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010b2.html) Returns the standard deviation of the peak frequency error across the measured pulses. This value is expressed in Hz.
- [Pulse:Results:Frequency and Phase:Frequency Error RMS (Hz)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010a9.html) Returns the RMS frequency error for all measured pulses. This value is expressed in Hz.
- [Pulse:Results:Frequency and Phase:Frequency Error RMS Maximum (Hz)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010ab.html) Returns the maximum RMS frequency error across the measured pulses. This value is expressed in Hz.
- [Pulse:Results:Frequency and Phase:Frequency Error RMS Mean (Hz)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010aa.html) Returns the mean of the RMS frequency error across the measured pulses. This value is expressed in Hz.
- [Pulse:Results:Frequency and Phase:Frequency Error RMS Minimum (Hz)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010ac.html) Returns the minimum RMS frequency error across the measured pulses. This value is expressed in Hz.
- [Pulse:Results:Frequency and Phase:Frequency Error RMS Standard Deviation (Hz)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010ad.html) Returns the standard deviation of the RMS frequency error across the measured pulses. This value is expressed in Hz.
- [Pulse:Results:Frequency and Phase:Phase Deviation (deg)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01065.html) Returns the peak-to-peak phase deviation for all measured pulses. This value is expressed in degrees.
- [Pulse:Results:Frequency and Phase:Phase Deviation Maximum (deg)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01067.html) Returns the maximum peak-to-peak phase deviation across the measured pulses. This value is expressed in degrees.
- [Pulse:Results:Frequency and Phase:Phase Deviation Mean (deg)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01066.html) Returns the mean of the peak-to-peak phase deviation across the measured pulses. This value is expressed in degrees.
- [Pulse:Results:Frequency and Phase:Phase Deviation Minimum (deg)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01068.html) Returns the minimum peak-to-peak phase deviation across the measured pulses. This value is expressed in degrees.
- [Pulse:Results:Frequency and Phase:Phase Deviation Standard Deviation (deg)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01069.html) Returns the standard deviation of the peak-to-peak phase deviation across the measured pulses. This value is expressed in degrees.
- [Pulse:Results:Frequency and Phase:Phase Error Peak (deg)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010a3.html) Returns the peak phase error for all measured pulses. This value is expressed in degrees.
- [Pulse:Results:Frequency and Phase:Phase Error Peak Location (s)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010a8.html) Returns the time locations corresponding to the peak phase error for all measured pulses. This value is expressed in seconds.
- [Pulse:Results:Frequency and Phase:Phase Error Peak Maximum (deg)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010a5.html) Returns the maximum peak phase error across the measured pulses. This value is expressed in degrees.
- [Pulse:Results:Frequency and Phase:Phase Error Peak Mean (deg)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010a4.html) Returns the mean of the peak phase error across the measured pulses. This value is expressed in degrees.
- [Pulse:Results:Frequency and Phase:Phase Error Peak Minimum (deg)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010a6.html) Returns the minimum peak phase error across the measured pulses. This value is expressed in degrees.
- [Pulse:Results:Frequency and Phase:Phase Error Peak Standard Deviation (deg)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010a7.html) Returns the standard deviation of the peak phase error across the measured pulses. This value is expressed in degrees.
- [Pulse:Results:Frequency and Phase:Phase Error RMS (deg)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0109e.html) Returns the RMS phase error for all measured pulses. This value is expressed in degrees.
- [Pulse:Results:Frequency and Phase:Phase Error RMS Maximum (deg)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010a0.html) Returns the maximum RMS phase error across the measured pulses. This value is expressed in degrees.
- [Pulse:Results:Frequency and Phase:Phase Error RMS Mean (deg)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0109f.html) Returns the mean of the RMS phase error across the measured pulses. This value is expressed in degrees.
- [Pulse:Results:Frequency and Phase:Phase Error RMS Minimum (deg)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010a1.html) Returns the minimum RMS phase error across the measured pulses. This value is expressed in degrees.
- [Pulse:Results:Frequency and Phase:Phase Error RMS Standard Deviation (deg)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010a2.html) Returns the standard deviation of the RMS phase errors across the measured pulses. This value is expressed in degrees.
- [Pulse:Results:Frequency and Phase:Pulse to Pulse Frequency Difference (Hz)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0106f.html) Returns the frequency difference of the pulses with respect to the frequency of the first pulse. This value is expressed in Hz.
- [Pulse:Results:Frequency and Phase:Pulse to Pulse Frequency Difference Maximum (Hz)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01071.html) Returns the maximum pulse-to-pulse frequency difference across the measured pulses. This value is expressed in Hz.
- [Pulse:Results:Frequency and Phase:Pulse to Pulse Frequency Difference Mean (Hz)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01070.html) Returns the mean of the pulse-to-pulse frequency difference across the measured pulses. This value is expressed in Hz.
- [Pulse:Results:Frequency and Phase:Pulse to Pulse Frequency Difference Minimum (Hz)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01072.html) Returns the minimum pulse-to-pulse frequency difference across the measured pulses. This value is expressed in Hz.
- [Pulse:Results:Frequency and Phase:Pulse to Pulse Frequency Difference Standard Deviation (Hz)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01073.html) Returns the standard deviation of the pulse-to-pulse frequency difference across the measured pulses. This value is expressed in Hz.
- [Pulse:Results:Frequency and Phase:Pulse to Pulse Phase Difference (deg)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01098.html) Returns the phase difference of the pulses with respect to the phase of the first pulse. This value is expressed in degrees.
- [Pulse:Results:Frequency and Phase:Pulse to Pulse Phase Difference Maximum (deg)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01062.html) Returns the maximum pulse-to-pulse phase difference across the measured pulses. This value is expressed in degrees.
- [Pulse:Results:Frequency and Phase:Pulse to Pulse Phase Difference Mean (deg)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01061.html) Returns the mean of the pulse-to-pulse phase difference across the measured pulses. This value is expressed in degrees.
- [Pulse:Results:Frequency and Phase:Pulse to Pulse Phase Difference Minimum (deg)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01063.html) Returns the minimum pulse-to-pulse phase difference across the measured pulses. This value is expressed in degrees.
- [Pulse:Results:Frequency and Phase:Pulse to Pulse Phase Difference Standard Deviation (deg)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01064.html) Returns the standard deviation of the pulse-to-pulse phase difference across the measured pulses. This value is expressed in degrees.
- [Pulse:Results:Level:Average Level (dBm)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01024.html) Returns the average power levels during the pulse period for all measured pulses. The values are expressed in dBm.
- [Pulse:Results:Level:Average Level Maximum (dBm)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01026.html) Returns the maximum average power level during the pulse period across the measured pulses. This value is expressed in dBm.
- [Pulse:Results:Level:Average Level Mean (dBm)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01025.html) Returns the mean of the average power levels during the pulse period across the measured pulses. This value is expressed in dBm.
- [Pulse:Results:Level:Average Level Minimum (dBm)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01027.html) Returns the minimum average power level during the pulse period across the measured pulses. This value is expressed in dBm.
- [Pulse:Results:Level:Average Level Standard Deviation (dBm)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01028.html) Returns the standard deviation of the average power levels during the pulse period across the measured pulses. This value is expressed in dBm.
- [Pulse:Results:Level:Average On Level (dBm)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0101a.html) Returns the average power levels during the ON duration for all measured pulses. The values are expressed in dBm.
- [Pulse:Results:Level:Average On Level Maximum (dBm)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0101c.html) Returns the maximum average power level during the ON duration across the measured pulses. This value is expressed in dBm.
- [Pulse:Results:Level:Average On Level Mean (dBm)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0101b.html) Returns the mean of the average power levels during the ON duration across the measured pulses. This value is expressed in dBm.
- [Pulse:Results:Level:Average On Level Minimum (dBm)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0101d.html) Returns the minimum average power level during the ON duration across the measured pulses. This value is expressed in dBm.
- [Pulse:Results:Level:Average On Level Standard Deviation (dBm)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0101e.html) Returns the standard deviation of the average power levels during the ON duration across the measured pulses. This value is expressed in dBm.
- [Pulse:Results:Level:Base Level (dBm)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01015.html) Returns the base levels for all measured pulses. The values are expressed in dBm.
- [Pulse:Results:Level:Base Level Maximum (dBm)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01017.html) Returns the maximum base level across the measured pulses. This value is expressed in dBm.
- [Pulse:Results:Level:Base Level Mean (dBm)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01016.html) Returns the mean of the base levels across the measured pulses. This value is expressed in dBm.
- [Pulse:Results:Level:Base Level Minimum (dBm)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01018.html) Returns the minimum base level across the measured pulses. This value is expressed in dBm.
- [Pulse:Results:Level:Base Level Standard Deviation(dBm)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01019.html) Returns the standard deviation of the base levels across the measured pulses. This value is expressed in dBm.
- [Pulse:Results:Level:Droop (% or dB)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0102e.html) Returns the droop values computed for all measured pulses. Droop values are defined as the rate at which the pulse top levels decays from the beginning to the end during On duration. This value is expressed in units specified by Pulse Amplitude Deviation Unit property.
- [Pulse:Results:Level:Droop Maximum (% or dB)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01030.html) Returns the maximum of droop values computed for all measured pulses. This value is expressed in units specified by Pulse Amplitude Deviation Unit property.
- [Pulse:Results:Level:Droop Mean (% or dB)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0102f.html) Returns the mean of the droop values computed for all measured pulses. This value is expressed in units specified by Pulse Amplitude Deviation Unit property.
- [Pulse:Results:Level:Droop Minimum (% or dB)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01031.html) Returns the minimum of droop values computed for all measured pulses. This value is expressed in units specified by Pulse Amplitude Deviation Unit property.
- [Pulse:Results:Level:Droop Standard Deviation (% or dB)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01032.html) Returns the standard deviation of the droop values computed for all measured pulses. This value is expressed in units specified by Pulse Amplitude Deviation Unit property.
- [Pulse:Results:Level:Overshoot (% or dB)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01029.html) Returns the overshoot values computed for all measured pulses. The overshoot value is defined as the ratio of height of the local peak after a rising edge to the pulse amplitude. This value is expressed in units specified by Pulse Amplitude Deviation Unit property.
- [Pulse:Results:Level:Overshoot Maximum (% or dB)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0102b.html) Returns the maximum of overshoot values computed for all measured pulses. This value is expressed in units specified by Pulse Amplitude Deviation Unit property.
- [Pulse:Results:Level:Overshoot Mean (% or dB)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0102a.html) Returns the mean of the overshoot values computed for all measured pulses. This value is expressed in units specified by Pulse Amplitude Deviation Unit property.
- [Pulse:Results:Level:Overshoot Minimum (% or dB)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0102c.html) Returns the minimum of overshoot values computed for all measured pulses. This value is expressed in units specified by Pulse Amplitude Deviation Unit property.
- [Pulse:Results:Level:Overshoot Standard Deviation (% or dB)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0102d.html) Returns the standard deviation of the overshoot values computed for all measured pulses. This value is expressed in units specified by Pulse Amplitude Deviation Unit property.
- [Pulse:Results:Level:Peak Level (dBm)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0101f.html) Returns the peak power levels during the pulse period for all measured pulses. The values are expressed in dBm.
- [Pulse:Results:Level:Peak Level Maximum (dBm)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01021.html) Returns the maximum peak power level during the pulse period across the measured pulses. This value is expressed in dBm.
- [Pulse:Results:Level:Peak Level Mean (dBm)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01020.html) Returns the mean of the peak power levels during the pulse period across the measured pulses. This value is expressed in dBm.
- [Pulse:Results:Level:Peak Level Minimum (dBm)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01022.html) Returns the minimum peak power level during the pulse period across the measured pulses. This value is expressed in dBm.
- [Pulse:Results:Level:Peak Level Standard Deviation (dBm)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01023.html) Returns the standard deviation of the peak power levels during the pulse period across the measured pulses. This value is expressed in dBm.
- [Pulse:Results:Level:Ripple (% or dB)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01033.html) Returns the ripple values computed for all measured pulses. Ripple values are the difference between the maximum and minimum deviation from the pulse top reference. This value is expressed in units specified by Pulse Amplitude Deviation Unit property.
- [Pulse:Results:Level:Ripple Maximum (% or dB)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01035.html) Returns the maximum of ripple values computed for all measured pulses. This value is expressed in units specified by Pulse Amplitude Deviation Unit property.
- [Pulse:Results:Level:Ripple Mean (% or dB)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01034.html) Returns the mean of the ripple values computed for all measured pulses. This value is expressed in units specified by Pulse Amplitude Deviation Unit property.
- [Pulse:Results:Level:Ripple Minimum (% or dB)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01036.html) Returns the minimum of ripple values computed for all measured pulses. This value is expressed in units specified by Pulse Amplitude Deviation Unit property.
- [Pulse:Results:Level:Ripple Standard Deviation (% or dB)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01037.html) Returns the standard deviation of the ripple values computed for all measured pulses. This value is expressed in units specified by Pulse Amplitude Deviation Unit property.
- [Pulse:Results:Level:Top Level (dBm)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01010.html) Returns the top levels for all measured pulses. The values are expressed in dBm.
- [Pulse:Results:Level:Top Level Maximum (dBm)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01012.html) Returns the maximum top level across the measured pulses. This value is expressed in dBm.
- [Pulse:Results:Level:Top Level Mean (dBm)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01011.html) Returns the mean of the top levels across the measured pulses. This value is expressed in dBm.
- [Pulse:Results:Level:Top Level Minimum (dBm)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01013.html) Returns the minimum top level across the measured pulses. This value is expressed in dBm.
- [Pulse:Results:Level:Top Level Standard Deviation (dBm)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01014.html) Returns the standard deviation of the top levels across the measured pulses. This value is expressed in dBm.
- [Pulse:Results:Pulse Count](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0100f.html) Returns the measured pulse count.
- [Pulse:Results:Pulse Position Index](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010e2.html) Returns the position indices of all the measured pulses within a burst.
- [Pulse:Results:Stability:Amplitude (dB)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01079.html) Returns the amplitude stability of the measured pulses. This value is expressed in dB. This value is computed as the deviation of amplitude from the reference.
- [Pulse:Results:Stability:Amplitude Maximum (dB)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0107b.html) Returns the maximum amplitude stability across the measured pulses. This value is expressed in dB.
- [Pulse:Results:Stability:Amplitude Mean (dB)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0107a.html) Returns the mean of the amplitude stability values across the measured pulses. This value is expressed in dB.
- [Pulse:Results:Stability:Amplitude Minimum (dB)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0107c.html) Returns the minimum amplitude stability across the measured pulses. This value is expressed in dB.
- [Pulse:Results:Stability:Amplitude Standard Deviation (dB)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0107d.html) Returns the amplitude stability standard deviation across the measured pulses. This value is expressed in dB.
- [Pulse:Results:Stability:Average Amplitude (dB)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01095.html) Returns the average amplitude stability over the measured pulses. This value is expressed in dB. The stability is computed as the variance of the amplitude over the measured pulses.
- [Pulse:Results:Stability:Average Phase (dB)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01096.html) Returns the average phase stability over the measured pulses. This value is expressed in dB. The stability is computed as the variance of the phase over the measured pulses.
- [Pulse:Results:Stability:Average Total (dB)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01097.html) Returns the average total stability over measured pulses. This value is expressed in dB.
- [Pulse:Results:Stability:Phase (dB)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0107e.html) Returns the phase stability of the measured pulses. This value is expressed in dB. This value is computed as the deviation of phase from the reference.
- [Pulse:Results:Stability:Phase Maximum (dB)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01080.html) Returns the maximum phase stability across the measured pulses. This value is expressed in dB.
- [Pulse:Results:Stability:Phase Mean (dB)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0107f.html) Returns the mean of the phase stability values across the measured pulses. This value is expressed in dB.
- [Pulse:Results:Stability:Phase Minimum (dB)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01081.html) Returns the minimum phase stability across the measured pulses. This value is expressed in dB.
- [Pulse:Results:Stability:Phase Standard Deviation (dB)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01082.html) Returns the phase stability standard deviation across the measured pulses. This value is expressed in dB.
- [Pulse:Results:Stability:Total (dB)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01083.html) Returns the total stability of the measured pulses. This value is expressed in dB.
- [Pulse:Results:Stability:Total Maximum (dB)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01085.html) Returns the maximum total stability across the measured pulses. This value is expressed in dB.
- [Pulse:Results:Stability:Total Mean (dB)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01084.html) Returns the mean of the total stability values across the measured pulses. This value is expressed in dB.
- [Pulse:Results:Stability:Total Minimum (dB)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01086.html) Returns the minimum total stability across the measured pulses. This value is expressed in dB.
- [Pulse:Results:Stability:Total Standard Deviation (dB)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01087.html) Returns the total stability standard deviation across the measured pulses. This value is expressed in dB.
- [Pulse:Results:Time Sidelobe: Peak Sidelobe Level Minimum (dB)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010f9.html) Returns the minimum peak sidelobe level across the measured pulses. This value is expressed in dB.
- [Pulse:Results:Time Sidelobe:Compression Ratio (%)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010fb.html) Returns the compression ratio for all measured pulses. Compression ratio is the ratio of the mainlobe width to the pulse width. This value is expressed as a percentage.
- [Pulse:Results:Time Sidelobe:Compression Ratio Maximum (%)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010fd.html) Returns the maximum compression ratio across the measured pulses. This value is expressed as a percentage.
- [Pulse:Results:Time Sidelobe:Compression Ratio Mean (%)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010fc.html) Returns the mean of the compression ratio values across the measured pulses. This value is expressed as a percentage.
- [Pulse:Results:Time Sidelobe:Compression Ratio Minimum (%)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010fe.html) Returns the minimum compression ratio across the measured pulses. This value is expressed as a percentage.
- [Pulse:Results:Time Sidelobe:Compression Ratio Standard Deviation (%)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010ff.html) Returns the standard deviation of the compression ratio values across the measured pulses. This value is expressed as a percentage.
- [Pulse:Results:Time Sidelobe:Delay (s)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010f1.html) Returns the sidelobe delay for all measured pulses. Sidelobe delay is the time elapsed between the highest sidelobe peak and mainlobe peak level. This value is expressed in seconds.
- [Pulse:Results:Time Sidelobe:Delay Maximum (s)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010f3.html) Returns the maximum sidelobe delay across the measured pulses. This value is expressed in seconds.
- [Pulse:Results:Time Sidelobe:Delay Mean (s)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010f2.html) Returns the mean of the sidelobe delay values across the measured pulses. This value is expressed in seconds.
- [Pulse:Results:Time Sidelobe:Delay Minimum (s)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010f4.html) Returns the minimum sidelobe delay across the measured pulses. This value is expressed in seconds.
- [Pulse:Results:Time Sidelobe:Delay Standard Deviation (s)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010f5.html) Returns the standard deviation of the sidelobe delay values across the measured pulses. This value is expressed in seconds.
- [Pulse:Results:Time Sidelobe:Mainlobe Width (s)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010ec.html) Returns the mainlobe width for all measured pulses. Mainlobe width is the width at 3dB below from its peak level. This value is expressed in seconds.
- [Pulse:Results:Time Sidelobe:Mainlobe Width Maximum (s)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010ee.html) Returns the maximum mainlobe width across the measured pulses. This value is expressed in seconds.
- [Pulse:Results:Time Sidelobe:Mainlobe Width Mean (s)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010ed.html) Returns the mean of the mainlobe width values across the measured pulses. This value is expressed in seconds.
- [Pulse:Results:Time Sidelobe:Mainlobe Width Minimum (s)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010ef.html) Returns the minimum mainlobe width across the measured pulses. This value is expressed in seconds.
- [Pulse:Results:Time Sidelobe:Mainlobe Width Standard Deviation (s)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010f0.html) Returns the standard deviation of the mainlobe width values across the measured pulses. This value is expressed in seconds.
- [Pulse:Results:Time Sidelobe:Peak Correlation](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01100.html) Returns the peak correlation for all measured pulses. Peak correlation is the normalized peak power of the correlated output by both measured and reference pulse powers. This values ranges in between 0 to 1.
- [Pulse:Results:Time Sidelobe:Peak Correlation Maximum](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01102.html) Returns the maximum peak correlation across the measured pulses.
- [Pulse:Results:Time Sidelobe:Peak Correlation Mean](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01101.html) Returns the mean of the peak correlation values across the measured pulses.
- [Pulse:Results:Time Sidelobe:Peak Correlation Minimum](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01103.html) Returns the minimum peak correlation across the measured pulses.
- [Pulse:Results:Time Sidelobe:Peak Correlation Standard Deviation](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01104.html) Returns the standard deviation of the peak correlation values across the measured pulses.
- [Pulse:Results:Time Sidelobe:Peak Sidelobe Level (dB)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010f6.html) Returns the peak sidelobe level for all measured pulses. Peak sidelobe level is the ratio of the highest sidelobe peak to the mainlobe peak level. This value is expressed in dB.
- [Pulse:Results:Time Sidelobe:Peak Sidelobe Level Maximum (dB)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010f8.html) Returns the maximum peak sidelobe level across the measured pulses. This value is expressed in seconds.
- [Pulse:Results:Time Sidelobe:Peak Sidelobe Level Mean (dB)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010f7.html) Returns the mean of the peak sidelobe level values across the measured pulses. This value is expressed in dB.
- [Pulse:Results:Time Sidelobe:Peak Sidelobe Level Standard Deviation (dB)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010fa.html) Returns the standard deviation of the peak sidelobe level values across the measured pulses. This value is expressed in dB.
- [Pulse:Results:Time:Duty Cycle (%)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0104c.html) Returns the duty cycle values for all measured pulses. Duty cycle is the ratio of pulse ON duration to the pulse period. This value is expressed as a percentage.
- [Pulse:Results:Time:Duty Cycle Maximum (%)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0104e.html) Returns the maximum duty cycle across the measured pulses. This value is expressed as a percentage.
- [Pulse:Results:Time:Duty Cycle Mean (%)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0104d.html) Returns the mean of duty cycle values across the measured pulses. This value is expressed as a percentage.
- [Pulse:Results:Time:Duty Cycle Minimum (%)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0104f.html) Returns the minimum duty cycle across the measured pulses. This value is expressed as a percentage.
- [Pulse:Results:Time:Duty Cycle Standard Deviation (%)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01050.html) Returns the standard deviation of duty cycle values across the measured pulses. This value is expressed as a percentage.
- [Pulse:Results:Time:Fall Edge (s)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0110d.html) Returns the fall edge for all measured pulses. Fall edge is the absolute time instant when the pulse exceeds the falling edge width threshold. This value is expressed in seconds.
- [Pulse:Results:Time:Fall Time (s)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0103d.html) Returns the fall time for all measured pulses. Fall time is the difference between the time when the pulse drops below the upper and lower thresholds. This value is expressed in seconds.
- [Pulse:Results:Time:Fall Time Maximum (s)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0103f.html) Returns the maximum fall time across the measured pulses. This value is expressed in seconds.
- [Pulse:Results:Time:Fall Time Mean (s)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0103e.html) Returns the mean of the fall time values across the measured pulses. This value is expressed in seconds.
- [Pulse:Results:Time:Fall Time Minimum (s)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01040.html) Returns the minimum fall time across the measured pulses. This value is expressed in seconds.
- [Pulse:Results:Time:Fall Time Standard Deviation (s)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01041.html) Returns the standard deviation of the fall time values across the measured pulses. This value is expressed in seconds.
- [Pulse:Results:Time:Pulse Off Duration (s)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01047.html) Returns the OFF duration values for all measured pulses. OFF duration value is the duration of the pulse for the first falling-edge and the subsequent rising-edge transition at width threshold. This value is expressed in seconds.
- [Pulse:Results:Time:Pulse Off Duration Maximum (s)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01049.html) Returns the maximum OFF duration across the measured pulses. This value is expressed in seconds.
- [Pulse:Results:Time:Pulse Off Duration Mean (s)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01048.html) Returns the mean of the OFF duration values across the measured pulses. This value is expressed in seconds.
- [Pulse:Results:Time:Pulse Off Duration Minimum (s)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0104a.html) Returns the minimum OFF duration across the measured pulses. This value is expressed in seconds.
- [Pulse:Results:Time:Pulse Off Duration Standard Deviation (s)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0104b.html) Returns the standard deviation of OFF duration values across the measured pulses. This value is expressed in seconds.
- [Pulse:Results:Time:Pulse Repetition Interval (s)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01051.html) Returns the pulse period values for all measured pulses. Period values are the time difference between two consecutive transitions of the same polarity, either positive or negative, where the transitions occur at crossings of the width threshold. This value is expressed in seconds.
- [Pulse:Results:Time:Pulse Repetition Interval Maximum (s)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01053.html) Returns the maximum pulse period across the measured pulses. This value is expressed in seconds.
- [Pulse:Results:Time:Pulse Repetition Interval Mean (s)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01052.html) Returns the mean of pulse period values across the measured pulses. This value is expressed in seconds.
- [Pulse:Results:Time:Pulse Repetition Interval Minimum (s)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01054.html) Returns the minimum pulse period across the measured pulses. This value is expressed in seconds.
- [Pulse:Results:Time:Pulse Repetition Interval Standard Deviation (s)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01055.html) Returns the standard deviation of pulse period values across the measured pulses. This value is expressed in seconds.
- [Pulse:Results:Time:Pulse Width (s)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01042.html) Returns the ON duration for all measured pulses. ON duration value is the duration of the pulse for the first rising-edge and the subsequent falling-edge transition at width threshold. This value is expressed in seconds.
- [Pulse:Results:Time:Pulse Width Maximum (s)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01044.html) Returns the maximum ON duration across the measured pulses. This value is expressed in seconds.
- [Pulse:Results:Time:Pulse Width Mean (s)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01043.html) Returns the mean of the ON duration values across the measured pulses. This value is expressed in seconds.
- [Pulse:Results:Time:Pulse Width Minimum(s)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01045.html) Returns the minimum ON duration across the measured pulses. This value is expressed in seconds.
- [Pulse:Results:Time:Pulse Width Standard Deviation (s)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01046.html) Returns the standard deviation of ON duration values across the measured pulses. This value is expressed in seconds.
- [Pulse:Results:Time:Rise Edge (s)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0110c.html) Returns the rise edge for all measured pulses. Rise edge is the absolute time instant when the pulse exceeds the rising edge lower threshold. This value is expressed in seconds.
- [Pulse:Results:Time:Rise Time (s)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01038.html) Returns the rise time for all measured pulses. Rise time is the difference between the time when the pulse exceeds the lower and upper thresholds. This value is expressed in seconds.
- [Pulse:Results:Time:Rise Time Maximum (s)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0103a.html) Returns the maximum rise time across the measured pulses. This value is expressed in seconds.
- [Pulse:Results:Time:Rise Time Mean (s)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01039.html) Returns the mean of the rise time values across the measured pulses. This value is expressed in seconds.
- [Pulse:Results:Time:Rise Time Minimum (s)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0103b.html) Returns the minimum rise time across the measured pulses. This value is expressed in seconds.
- [Pulse:Results:Time:Rise Time Standard Deviation (s)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0103c.html) Returns the standard deviation of the rise time values across the measured pulses. This value is expressed in seconds.
- [Pulse:Selected Burst Trace](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010e0.html) Specifies the burst number selected for the display of traces. This property is applicable for IQ, amplitude and pulse stability traces.
- [Pulse:Selected Pulse Trace](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01091.html) Specifies the pulse number selected for displaying the traces. This property is valid only for IQ, amplitude and pulse stability traces.
- [Pulse:Stability:Enabled](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01099.html) Specifies whether to enable pulse stability results computation.
- [Pulse:Stability:Frequency Error Compensation](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01089.html) Specifies whether to compute and correct the frequency offset for stability results computation. This is an optional setting and in negligible frequency error condition you must set this property to Off to avoid incorrect results.
- [Pulse:Stability:Measurement Offset](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01092.html) Specifies the offset in number of pulses to be used for pulse stability measurement. This property is applicable for average stability results and pulse-to-pulse stabilty trace.
- [Pulse:Stability:Pulse To Pulse Offset](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01094.html) Specifies the offset in number of pulses used for pulse-to-pulse stability measurement trace.
- [Pulse:Stability:Reference Offset](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01093.html) Specifies the offset in number of pulses used for pulse stability reference computation.
- [Pulse:Time Sidelobe:Enabled](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010e7.html) Specifies whether to enable pulse time sidelobe results computation. You can use the RFmxPulse Configure Reference Waveform (1 Wfm) VI to set the reference waveform for correlation computation.
- [Pulse:Time Sidelobe:Keep Out Time (s)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010ea.html) Specifies keep out time for the time sidelobe measurements.
- [Pulse:Time Sidelobe:Keep Out Time Auto](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010e9.html) Specifies whether the keep out time computation for the time sidelobe measurements is automatic or manual.
- [Pulse:Time Sidelobe:Minimum Correlation](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010eb.html) Specifies the minimum peak correlation value for the time sidelobe measurements.
- [Pulse:Time Sidelobe:Reference Window Type](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010e8.html) Specifies the window type to be applied to the reference pulse to obtain correlated output for the time sidelobe measurements.
- [Pulse:Trace Range:Auto](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01108.html) Specifies whether the trace range computation of the selected pulse is automatic or manually configured by you.
- [Pulse:Trace Range:Length (s)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0110b.html) Specifies the length in seconds of the trace range centered at the reference point.
- [Pulse:Trace Range:Offset (s)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0110a.html) Specifies the time offset in seconds from the reference point to position the trace range.
- [Pulse:Trace Range:Reference](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01109.html) Specifies the reference point for positioning of trace range. You can set reference point based on reference and Pulse Trace Range Offset (s) value.
- [Reference Level](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc00002.html) Specifies the reference level that represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices.
- [Reference Level Headroom](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc00ffc.html) Specifies the margin RFmx adds to the Reference Level property. The margin avoids clipping and overflow warnings if the input signal exceeds the configured reference level.
- [Result Fetch Timeout (s)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0c000.html) Specifies the wait time before results are available in the RFmxPulse Property Node . This value is expressed in seconds.
- [Segmented Acquisition:Enabled](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc00014.html) Specifies whether to enable Segmented Acquisition. This mode is best applied when the pulses are sparsely spaced.
- [Segmented Acquisition:Length (s)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc00016.html) Specifies the acquisition length for the pulse measurement when you set the Segmented Acquisition Enabled property to True . This value is expressed in seconds.
- [Segmented Acquisition:Number of Segments](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc00015.html) Specifies the number of segments to acquire when you set the Segmented Acquisition Enabled property to True .
- [Selected Ports](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc00ffd.html) Specifies the instrument port to be configured to acquire a signal. Use RFmxInstr Get Available Ports VI to get the valid port names.
- [Selector String](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc00000.html) Specifies the selector string used to access all subsequent channel-based properties in this instance of the property node.
- [Trigger:Delay (s)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0000a.html) Specifies the trigger delay time. This value is expressed in seconds.
- [Trigger:Digital Edge:Edge](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc00006.html) Specifies the active edge for the trigger. This property is used only when you set the Trigger Type property to Digital Edge .
- [Trigger:Digital Edge:Source](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc00005.html) Specifies the source terminal for the digital edge trigger. This property is used only when you set the Trigger Type property to Digital Edge .
- [Trigger:IQ Power Edge:Level (dB or dBm)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc00008.html) Specifies the power level at which the device triggers. This value is expressed in dB when you set the IQ Power Edge Level Type property to Relative and in dBm when you set the IQ Power Edge Level Type property to Absolute . The device asserts the trigger when the signal exceeds the level specified by the value of this property, taking into consideration the specified slope. This property is used only when you set the Trigger Type property to IQ Power Edge .
- [Trigger:IQ Power Edge:Level Type](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc00fff.html) Specifies the reference for the IQ Power Edge Level property. The IQ Power Edge Level Type property is used only when you set the Trigger Type property to IQ Power Edge .
- [Trigger:IQ Power Edge:Slope](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc00009.html) Specifies whether the device asserts the trigger when the signal power is rising or when it is falling. The device asserts the trigger when the signal power exceeds the level that you specify in the IQ Power Edge Level property with the slope you specify. This property is used only when you set the Trigger Type property to IQ Power Edge .
- [Trigger:IQ Power Edge:Source](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc00007.html) Specifies the channel from which the device monitors the trigger. This property is used only when you set the Trigger Type property to IQ Power Edge .
- [Trigger:Minimum Quiet Time:Duration (s)](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0000c.html) Specifies the time duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. This value is expressed in seconds.
- [Trigger:Minimum Quiet Time:Mode](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0000b.html) Specifies whether the measurement computes the minimum quiet time used for triggering.
- [Trigger:Type](../../../resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc00004.html) Specifies the trigger type.

<!--NI_TOPIC bundle=rfmxpulse-labview-api-ref path=resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0000a.html language=enus -->
## TOPIC 00003: Trigger:Delay (s)

- bundle_id: `rfmxpulse-labview-api-ref`
- source_path: `resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0000a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0000a.html
- document_id: `rfmxpulse-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the trigger delay time. This value is expressed in seconds. If the delay is negative, the measurement acquires pretrigger samples. If the delay is positive, the measurement acquires post-trigger samples. You do not need to use a selector string to configure or read this property for the de

### Trigger:Delay (s)

Specifies the trigger delay time. This value is expressed in seconds.

If the delay is negative, the measurement acquires pretrigger samples. If the delay is positive, the measurement acquires post-trigger samples.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is 0.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Trigger Delay (s) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxPulse Properties

<!--NI_TOPIC bundle=rfmxpulse-labview-api-ref path=resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc00011.html language=enus -->
## TOPIC 00004: Acquisition Length (s)

- bundle_id: `rfmxpulse-labview-api-ref`
- source_path: `resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc00011.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc00011.html
- document_id: `rfmxpulse-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the acquisition length for the pulse measurement. This value is expressed in seconds. You configure this property when you set the Segmented Acquisition Enabled property to False. You do not need to use a selector string to configure or read this property for the default signal instance. R

### Acquisition Length (s)

Specifies the acquisition length for the pulse measurement. This value is expressed in seconds.

You configure this property when you set the [Segmented Acquisition Enabled](attrc00014.html) property to **False**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is 0.001 seconds.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Acquisition Length (s) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxPulse Properties

<!--NI_TOPIC bundle=rfmxpulse-labview-api-ref path=resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc00014.html language=enus -->
## TOPIC 00005: Segmented Acquisition:Enabled

- bundle_id: `rfmxpulse-labview-api-ref`
- source_path: `resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc00014.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc00014.html
- document_id: `rfmxpulse-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable Segmented Acquisition. This mode is best applied when the pulses are sparsely spaced. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax f

### Segmented Acquisition:Enabled

Specifies whether to enable Segmented Acquisition. This mode is best applied when the pulses are sparsely spaced.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **False**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Segmented Acquisition Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| False | 0 | Segmented acquisition is disabled. |
| --- | --- | --- |
| True | 1 | Segmented acquisition is enabled. |

Parent topic:

RFmxPulse Properties

<!--NI_TOPIC bundle=rfmxpulse-labview-api-ref path=resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc00016.html language=enus -->
## TOPIC 00006: Segmented Acquisition:Length (s)

- bundle_id: `rfmxpulse-labview-api-ref`
- source_path: `resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc00016.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc00016.html
- document_id: `rfmxpulse-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the acquisition length for the pulse measurement when you set the Segmented Acquisition Enabled property to True. This value is expressed in seconds. You must set this property to a value slightly higher than the desired pulse ON duration. You do not need to use a selector string to config

### Segmented Acquisition:Length (s)

Specifies the acquisition length for the pulse measurement when you set the [Segmented Acquisition Enabled](/csh?topicname=attrc00014.html) property to **True**. This value is expressed in seconds.

You must set this property to a value slightly higher than the desired pulse ON duration.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is 0.00001 seconds.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Segmented Acquisition Length (s) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxPulse Properties

<!--NI_TOPIC bundle=rfmxpulse-labview-api-ref path=resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc00ffc.html language=enus -->
## TOPIC 00007: Reference Level Headroom

- bundle_id: `rfmxpulse-labview-api-ref`
- source_path: `resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc00ffc.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc00ffc.html
- document_id: `rfmxpulse-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the margin RFmx adds to the Reference Level property. The margin avoids clipping and overflow warnings if the input signal exceeds the configured reference level. RFmx configures the input gain to avoid clipping and associated overflow warnings provided the instantaneous power of the input

### Reference Level Headroom

Specifies the margin RFmx adds to the [Reference Level](/csh?topicname=attrc00002.html) property. The margin avoids clipping and overflow warnings if the input signal exceeds the configured reference level.

RFmx configures the input gain to avoid clipping and associated overflow warnings provided the instantaneous power of the input signal remains within the Reference Level plus the Reference Level Headroom. If you know the input power of the signal precisely or previously included the margin in the Reference Level, you could improve the signal-to-noise ratio by reducing the Reference Level Headroom.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

**Supported devices:**PXIe-5668R, PXIe-5830/5831/5832/5840/5841/5842/5860.

**Default values**

| PXIe-5668 | 6 dB |
| --- | --- |
| PXIe-5830/5831/5832/5841/5842/5860 | 1 dB |
| PXIe-5840 | 0 dB |

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Reference Level Headroom |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxPulse Properties

<!--NI_TOPIC bundle=rfmxpulse-labview-api-ref path=resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc00ffd.html language=enus -->
## TOPIC 00008: Selected Ports

- bundle_id: `rfmxpulse-labview-api-ref`
- source_path: `resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc00ffd.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc00ffd.html
- document_id: `rfmxpulse-labview-api-ref`
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

RFmxPulse Properties

<!--NI_TOPIC bundle=rfmxpulse-labview-api-ref path=resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01006.html language=enus -->
## TOPIC 00009: Pulse:Detection:Minimum Width (s)

- bundle_id: `rfmxpulse-labview-api-ref`
- source_path: `resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01006.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01006.html
- document_id: `rfmxpulse-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the minimum pulse width time to be considered for pulse detection. Any detected pulse width time below the specified value will be ignored by the pulse detection. This value is expressed in seconds. You do not need to use a selector string to configure or read this property for the default

### Pulse:Detection:Minimum Width (s)

Specifies the minimum pulse width time to be considered for pulse detection. Any detected pulse width time below the specified value will be ignored by the pulse detection. This value is expressed in seconds.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is 0.00000005 seconds.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Min Pulse Width (s) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxPulse Properties

<!--NI_TOPIC bundle=rfmxpulse-labview-api-ref path=resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01007.html language=enus -->
## TOPIC 00010: Pulse:Detection:Maximum Width (s)

- bundle_id: `rfmxpulse-labview-api-ref`
- source_path: `resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01007.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01007.html
- document_id: `rfmxpulse-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the maximum pulse width time to be considered for pulse detection. Any detected pulse width time above the specified value will be ignored by the pulse detection. This value is expressed in seconds. You do not need to use a selector string to configure or read this property for the default

### Pulse:Detection:Maximum Width (s)

Specifies the maximum pulse width time to be considered for pulse detection. Any detected pulse width time above the specified value will be ignored by the pulse detection. This value is expressed in seconds.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is 0.005 seconds.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Max Pulse Width (s) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxPulse Properties

<!--NI_TOPIC bundle=rfmxpulse-labview-api-ref path=resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0100c.html language=enus -->
## TOPIC 00011: Pulse:Level:Lower Threshold (%)

- bundle_id: `rfmxpulse-labview-api-ref`
- source_path: `resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0100c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0100c.html
- document_id: `rfmxpulse-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the lower threshold level as a percentage of the pulse amplitude used to signify the start of a rising or end of a falling edge. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information

### Pulse:Level:Lower Threshold (%)

Specifies the lower threshold level as a percentage of the pulse amplitude used to signify the start of a rising or end of a falling edge.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is 10. Valid values are 0 to 100, inclusive.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Lower Threshold Level (%) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxPulse Properties

<!--NI_TOPIC bundle=rfmxpulse-labview-api-ref path=resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0100d.html language=enus -->
## TOPIC 00012: Pulse:Level:Droop Compensation Enabled

- bundle_id: `rfmxpulse-labview-api-ref`
- source_path: `resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0100d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0100d.html
- document_id: `rfmxpulse-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to compensate the droop detected in pulse level when applying thresholds. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The

### Pulse:Level:Droop Compensation Enabled

Specifies whether to compensate the droop detected in pulse level when applying thresholds.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **False**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Droop Comp Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| False | 0 | Droop Compensation is disabled. |
| --- | --- | --- |
| True | 1 | Droop Compensation is enabled. |

Parent topic:

RFmxPulse Properties

<!--NI_TOPIC bundle=rfmxpulse-labview-api-ref path=resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01010.html language=enus -->
## TOPIC 00013: Pulse:Results:Level:Top Level (dBm)

- bundle_id: `rfmxpulse-labview-api-ref`
- source_path: `resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01010.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01010.html
- document_id: `rfmxpulse-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the top levels for all measured pulses. The values are expressed in dBm. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Remarks The

### Pulse:Results:Level:Top Level (dBm)

Returns the top levels for all measured pulses. The values are expressed in dBm.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Results Top Level (dBm) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxPulse Properties

<!--NI_TOPIC bundle=rfmxpulse-labview-api-ref path=resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01013.html language=enus -->
## TOPIC 00014: Pulse:Results:Level:Top Level Minimum (dBm)

- bundle_id: `rfmxpulse-labview-api-ref`
- source_path: `resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01013.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01013.html
- document_id: `rfmxpulse-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the minimum top level across the measured pulses. This value is expressed in dBm. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Re

### Pulse:Results:Level:Top Level Minimum (dBm)

Returns the minimum top level across the measured pulses. This value is expressed in dBm.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Results Top Level Min (dBm) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxPulse Properties

<!--NI_TOPIC bundle=rfmxpulse-labview-api-ref path=resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0102f.html language=enus -->
## TOPIC 00015: Pulse:Results:Level:Droop Mean (% or dB)

- bundle_id: `rfmxpulse-labview-api-ref`
- source_path: `resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0102f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0102f.html
- document_id: `rfmxpulse-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean of the droop values computed for all measured pulses. This value is expressed in units specified by Pulse Amplitude Deviation Unit property. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for i

### Pulse:Results:Level:Droop Mean (% or dB)

Returns the mean of the droop values computed for all measured pulses. This value is expressed in units specified by [Pulse Amplitude Deviation Unit](/csh?context=rfmxpulse_rfmxpulseprop_attrc010dd) property.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Results Droop Mean (% or dB) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxPulse Properties

<!--NI_TOPIC bundle=rfmxpulse-labview-api-ref path=resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01032.html language=enus -->
## TOPIC 00016: Pulse:Results:Level:Droop Standard Deviation (% or dB)

- bundle_id: `rfmxpulse-labview-api-ref`
- source_path: `resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01032.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01032.html
- document_id: `rfmxpulse-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the standard deviation of the droop values computed for all measured pulses. This value is expressed in units specified by Pulse Amplitude Deviation Unit property. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strin

### Pulse:Results:Level:Droop Standard Deviation (% or dB)

Returns the standard deviation of the droop values computed for all measured pulses. This value is expressed in units specified by [Pulse Amplitude Deviation Unit](/csh?context=rfmxpulse_rfmxpulseprop_attrc010dd) property.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Results Droop SD (% or dB) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxPulse Properties

<!--NI_TOPIC bundle=rfmxpulse-labview-api-ref path=resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01037.html language=enus -->
## TOPIC 00017: Pulse:Results:Level:Ripple Standard Deviation (% or dB)

- bundle_id: `rfmxpulse-labview-api-ref`
- source_path: `resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01037.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01037.html
- document_id: `rfmxpulse-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the standard deviation of the ripple values computed for all measured pulses. This value is expressed in units specified by Pulse Amplitude Deviation Unit property. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Stri

### Pulse:Results:Level:Ripple Standard Deviation (% or dB)

Returns the standard deviation of the ripple values computed for all measured pulses. This value is expressed in units specified by [Pulse Amplitude Deviation Unit](/csh?context=rfmxpulse_rfmxpulseprop_attrc010dd) property.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Results Ripple SD (% or dB) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxPulse Properties

<!--NI_TOPIC bundle=rfmxpulse-labview-api-ref path=resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0103c.html language=enus -->
## TOPIC 00018: Pulse:Results:Time:Rise Time Standard Deviation (s)

- bundle_id: `rfmxpulse-labview-api-ref`
- source_path: `resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0103c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0103c.html
- document_id: `rfmxpulse-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the standard deviation of the rise time values across the measured pulses. This value is expressed in seconds. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for

### Pulse:Results:Time:Rise Time Standard Deviation (s)

Returns the standard deviation of the rise time values across the measured pulses. This value is expressed in seconds.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Results Rise Time SD (s) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxPulse Properties

<!--NI_TOPIC bundle=rfmxpulse-labview-api-ref path=resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0103d.html language=enus -->
## TOPIC 00019: Pulse:Results:Time:Fall Time (s)

- bundle_id: `rfmxpulse-labview-api-ref`
- source_path: `resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0103d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0103d.html
- document_id: `rfmxpulse-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the fall time for all measured pulses. Fall time is the difference between the time when the pulse drops below the upper and lower thresholds. This value is expressed in seconds. You do not need to use a selector string to read this result for default signal and result instance. Refer to the

### Pulse:Results:Time:Fall Time (s)

Returns the fall time for all measured pulses. Fall time is the difference between the time when the pulse drops below the upper and lower thresholds. This value is expressed in seconds.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Results Fall Time (s) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxPulse Properties

<!--NI_TOPIC bundle=rfmxpulse-labview-api-ref path=resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0103f.html language=enus -->
## TOPIC 00020: Pulse:Results:Time:Fall Time Maximum (s)

- bundle_id: `rfmxpulse-labview-api-ref`
- source_path: `resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0103f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0103f.html
- document_id: `rfmxpulse-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum fall time across the measured pulses. This value is expressed in seconds. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results

### Pulse:Results:Time:Fall Time Maximum (s)

Returns the maximum fall time across the measured pulses. This value is expressed in seconds.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Results Fall Time Max (s) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxPulse Properties

<!--NI_TOPIC bundle=rfmxpulse-labview-api-ref path=resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01040.html language=enus -->
## TOPIC 00021: Pulse:Results:Time:Fall Time Minimum (s)

- bundle_id: `rfmxpulse-labview-api-ref`
- source_path: `resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01040.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01040.html
- document_id: `rfmxpulse-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the minimum fall time across the measured pulses. This value is expressed in seconds. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results

### Pulse:Results:Time:Fall Time Minimum (s)

Returns the minimum fall time across the measured pulses. This value is expressed in seconds.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Results Fall Time Min (s) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxPulse Properties

<!--NI_TOPIC bundle=rfmxpulse-labview-api-ref path=resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01049.html language=enus -->
## TOPIC 00022: Pulse:Results:Time:Pulse Off Duration Maximum (s)

- bundle_id: `rfmxpulse-labview-api-ref`
- source_path: `resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01049.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01049.html
- document_id: `rfmxpulse-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum OFF duration across the measured pulses. This value is expressed in seconds. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and resu

### Pulse:Results:Time:Pulse Off Duration Maximum (s)

Returns the maximum OFF duration across the measured pulses. This value is expressed in seconds.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Results Pulse Off Duration Max (s) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxPulse Properties

<!--NI_TOPIC bundle=rfmxpulse-labview-api-ref path=resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0104a.html language=enus -->
## TOPIC 00023: Pulse:Results:Time:Pulse Off Duration Minimum (s)

- bundle_id: `rfmxpulse-labview-api-ref`
- source_path: `resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0104a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0104a.html
- document_id: `rfmxpulse-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the minimum OFF duration across the measured pulses. This value is expressed in seconds. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and resu

### Pulse:Results:Time:Pulse Off Duration Minimum (s)

Returns the minimum OFF duration across the measured pulses. This value is expressed in seconds.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Results Pulse Off Duration Min (s) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxPulse Properties

<!--NI_TOPIC bundle=rfmxpulse-labview-api-ref path=resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0104b.html language=enus -->
## TOPIC 00024: Pulse:Results:Time:Pulse Off Duration Standard Deviation (s)

- bundle_id: `rfmxpulse-labview-api-ref`
- source_path: `resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0104b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0104b.html
- document_id: `rfmxpulse-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the standard deviation of OFF duration values across the measured pulses. This value is expressed in seconds. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for n

### Pulse:Results:Time:Pulse Off Duration Standard Deviation (s)

Returns the standard deviation of OFF duration values across the measured pulses. This value is expressed in seconds.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Results Pulse Off Duration SD (s) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxPulse Properties

<!--NI_TOPIC bundle=rfmxpulse-labview-api-ref path=resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0104c.html language=enus -->
## TOPIC 00025: Pulse:Results:Time:Duty Cycle (%)

- bundle_id: `rfmxpulse-labview-api-ref`
- source_path: `resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0104c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0104c.html
- document_id: `rfmxpulse-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the duty cycle values for all measured pulses. Duty cycle is the ratio of pulse ON duration to the pulse period. This value is expressed as a percentage. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic f

### Pulse:Results:Time:Duty Cycle (%)

Returns the duty cycle values for all measured pulses. Duty cycle is the ratio of pulse ON duration to the pulse period. This value is expressed as a percentage.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Results Duty Cycle (%) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxPulse Properties

<!--NI_TOPIC bundle=rfmxpulse-labview-api-ref path=resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0104d.html language=enus -->
## TOPIC 00026: Pulse:Results:Time:Duty Cycle Mean (%)

- bundle_id: `rfmxpulse-labview-api-ref`
- source_path: `resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0104d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0104d.html
- document_id: `rfmxpulse-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean of duty cycle values across the measured pulses. This value is expressed as a percentage. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signal

### Pulse:Results:Time:Duty Cycle Mean (%)

Returns the mean of duty cycle values across the measured pulses. This value is expressed as a percentage.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Results Duty Cycle Mean (%) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxPulse Properties

<!--NI_TOPIC bundle=rfmxpulse-labview-api-ref path=resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01050.html language=enus -->
## TOPIC 00027: Pulse:Results:Time:Duty Cycle Standard Deviation (%)

- bundle_id: `rfmxpulse-labview-api-ref`
- source_path: `resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01050.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01050.html
- document_id: `rfmxpulse-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the standard deviation of duty cycle values across the measured pulses. This value is expressed as a percentage. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax fo

### Pulse:Results:Time:Duty Cycle Standard Deviation (%)

Returns the standard deviation of duty cycle values across the measured pulses. This value is expressed as a percentage.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Results Duty Cycle SD (%) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxPulse Properties

<!--NI_TOPIC bundle=rfmxpulse-labview-api-ref path=resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01051.html language=enus -->
## TOPIC 00028: Pulse:Results:Time:Pulse Repetition Interval (s)

- bundle_id: `rfmxpulse-labview-api-ref`
- source_path: `resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01051.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01051.html
- document_id: `rfmxpulse-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the pulse period values for all measured pulses. Period values are the time difference between two consecutive transitions of the same polarity, either positive or negative, where the transitions occur at crossings of the width threshold. This value is expressed in seconds. You do not need t

### Pulse:Results:Time:Pulse Repetition Interval (s)

Returns the pulse period values for all measured pulses. Period values are the time difference between two consecutive transitions of the same polarity, either positive or negative, where the transitions occur at crossings of the width threshold.
 This value is expressed in seconds.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Results PRI (s) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxPulse Properties

<!--NI_TOPIC bundle=rfmxpulse-labview-api-ref path=resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01052.html language=enus -->
## TOPIC 00029: Pulse:Results:Time:Pulse Repetition Interval Mean (s)

- bundle_id: `rfmxpulse-labview-api-ref`
- source_path: `resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01052.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01052.html
- document_id: `rfmxpulse-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean of pulse period values across the measured pulses. This value is expressed in seconds. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals a

### Pulse:Results:Time:Pulse Repetition Interval Mean (s)

Returns the mean of pulse period values across the measured pulses. This value is expressed in seconds.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Results PRI Mean (s) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxPulse Properties

<!--NI_TOPIC bundle=rfmxpulse-labview-api-ref path=resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01053.html language=enus -->
## TOPIC 00030: Pulse:Results:Time:Pulse Repetition Interval Maximum (s)

- bundle_id: `rfmxpulse-labview-api-ref`
- source_path: `resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01053.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01053.html
- document_id: `rfmxpulse-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum pulse period across the measured pulses. This value is expressed in seconds. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and resu

### Pulse:Results:Time:Pulse Repetition Interval Maximum (s)

Returns the maximum pulse period across the measured pulses. This value is expressed in seconds.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Results PRI Max (s) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxPulse Properties

<!--NI_TOPIC bundle=rfmxpulse-labview-api-ref path=resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01054.html language=enus -->
## TOPIC 00031: Pulse:Results:Time:Pulse Repetition Interval Minimum (s)

- bundle_id: `rfmxpulse-labview-api-ref`
- source_path: `resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01054.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01054.html
- document_id: `rfmxpulse-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the minimum pulse period across the measured pulses. This value is expressed in seconds. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and resu

### Pulse:Results:Time:Pulse Repetition Interval Minimum (s)

Returns the minimum pulse period across the measured pulses. This value is expressed in seconds.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Results PRI Min (s) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxPulse Properties

<!--NI_TOPIC bundle=rfmxpulse-labview-api-ref path=resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01055.html language=enus -->
## TOPIC 00032: Pulse:Results:Time:Pulse Repetition Interval Standard Deviation (s)

- bundle_id: `rfmxpulse-labview-api-ref`
- source_path: `resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01055.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01055.html
- document_id: `rfmxpulse-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the standard deviation of pulse period values across the measured pulses. This value is expressed in seconds. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for n

### Pulse:Results:Time:Pulse Repetition Interval Standard Deviation (s)

Returns the standard deviation of pulse period values across the measured pulses. This value is expressed in seconds.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Results PRI SD (s) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxPulse Properties

<!--NI_TOPIC bundle=rfmxpulse-labview-api-ref path=resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0105b.html language=enus -->
## TOPIC 00033: Pulse:Results:Frequency and Phase:Average Phase (deg)

- bundle_id: `rfmxpulse-labview-api-ref`
- source_path: `resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0105b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0105b.html
- document_id: `rfmxpulse-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the average phase for all measured pulses. This value is expressed in degrees. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Remar

### Pulse:Results:Frequency and Phase:Average Phase (deg)

Returns the average phase for all measured pulses. This value is expressed in degrees.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Results Avg Phase (deg) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxPulse Properties

<!--NI_TOPIC bundle=rfmxpulse-labview-api-ref path=resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0105c.html language=enus -->
## TOPIC 00034: Pulse:Results:Frequency and Phase:Average Phase Mean (deg)

- bundle_id: `rfmxpulse-labview-api-ref`
- source_path: `resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0105c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0105c.html
- document_id: `rfmxpulse-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean of the average phase across the measured pulses. This value is expressed in degrees. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and

### Pulse:Results:Frequency and Phase:Average Phase Mean (deg)

Returns the mean of the average phase across the measured pulses. This value is expressed in degrees.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Results Avg Phase Mean (deg) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxPulse Properties

<!--NI_TOPIC bundle=rfmxpulse-labview-api-ref path=resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0105d.html language=enus -->
## TOPIC 00035: Pulse:Results:Frequency and Phase:Average Phase Maximum (deg)

- bundle_id: `rfmxpulse-labview-api-ref`
- source_path: `resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0105d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0105d.html
- document_id: `rfmxpulse-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum average phase across the measured pulses. This value is expressed in degrees. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and res

### Pulse:Results:Frequency and Phase:Average Phase Maximum (deg)

Returns the maximum average phase across the measured pulses. This value is expressed in degrees.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Results Avg Phase Max (deg) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxPulse Properties

<!--NI_TOPIC bundle=rfmxpulse-labview-api-ref path=resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0105e.html language=enus -->
## TOPIC 00036: Pulse:Results:Frequency and Phase:Average Phase Minimum (deg)

- bundle_id: `rfmxpulse-labview-api-ref`
- source_path: `resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0105e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0105e.html
- document_id: `rfmxpulse-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the minimum average phase across the measured pulses. This value is expressed in degrees. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and res

### Pulse:Results:Frequency and Phase:Average Phase Minimum (deg)

Returns the minimum average phase across the measured pulses. This value is expressed in degrees.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Results Avg Phase Min (deg) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxPulse Properties

<!--NI_TOPIC bundle=rfmxpulse-labview-api-ref path=resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0105f.html language=enus -->
## TOPIC 00037: Pulse:Results:Frequency and Phase:Average Phase Standard Deviation (deg)

- bundle_id: `rfmxpulse-labview-api-ref`
- source_path: `resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0105f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0105f.html
- document_id: `rfmxpulse-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the standard deviation of the average phase across the measured pulses. This value is expressed in degrees. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for nam

### Pulse:Results:Frequency and Phase:Average Phase Standard Deviation (deg)

Returns the standard deviation of the average phase across the measured pulses. This value is expressed in degrees.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Results Avg Phase SD (deg) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxPulse Properties

<!--NI_TOPIC bundle=rfmxpulse-labview-api-ref path=resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01061.html language=enus -->
## TOPIC 00038: Pulse:Results:Frequency and Phase:Pulse to Pulse Phase Difference Mean (deg)

- bundle_id: `rfmxpulse-labview-api-ref`
- source_path: `resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01061.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01061.html
- document_id: `rfmxpulse-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean of the pulse-to-pulse phase difference across the measured pulses. This value is expressed in degrees. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for

### Pulse:Results:Frequency and Phase:Pulse to Pulse Phase Difference Mean (deg)

Returns the mean of the pulse-to-pulse phase difference across the measured pulses. This value is expressed in degrees.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Results Pulse to Pulse Phase Diff Mean (deg) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxPulse Properties

<!--NI_TOPIC bundle=rfmxpulse-labview-api-ref path=resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01065.html language=enus -->
## TOPIC 00039: Pulse:Results:Frequency and Phase:Phase Deviation (deg)

- bundle_id: `rfmxpulse-labview-api-ref`
- source_path: `resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01065.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01065.html
- document_id: `rfmxpulse-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the peak-to-peak phase deviation for all measured pulses. This value is expressed in degrees. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and

### Pulse:Results:Frequency and Phase:Phase Deviation (deg)

Returns the peak-to-peak phase deviation for all measured pulses. This value is expressed in degrees.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Results Phase Dev (deg) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxPulse Properties

<!--NI_TOPIC bundle=rfmxpulse-labview-api-ref path=resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0106b.html language=enus -->
## TOPIC 00040: Pulse:Results:Frequency and Phase:Average Frequency Mean (Hz)

- bundle_id: `rfmxpulse-labview-api-ref`
- source_path: `resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0106b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0106b.html
- document_id: `rfmxpulse-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean of the average frequency across the measured pulses. This value is expressed in Hz. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and

### Pulse:Results:Frequency and Phase:Average Frequency Mean (Hz)

Returns the mean of the average frequency across the measured pulses. This value is expressed in Hz.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Results Avg Freq Mean (Hz) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxPulse Properties

<!--NI_TOPIC bundle=rfmxpulse-labview-api-ref path=resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0106d.html language=enus -->
## TOPIC 00041: Pulse:Results:Frequency and Phase:Average Frequency Minimum (Hz)

- bundle_id: `rfmxpulse-labview-api-ref`
- source_path: `resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0106d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0106d.html
- document_id: `rfmxpulse-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the minimum average frequency across the measured pulses. This value is expressed in Hz. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and resu

### Pulse:Results:Frequency and Phase:Average Frequency Minimum (Hz)

Returns the minimum average frequency across the measured pulses. This value is expressed in Hz.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Results Avg Freq Min (Hz) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxPulse Properties

<!--NI_TOPIC bundle=rfmxpulse-labview-api-ref path=resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01070.html language=enus -->
## TOPIC 00042: Pulse:Results:Frequency and Phase:Pulse to Pulse Frequency Difference Mean (Hz)

- bundle_id: `rfmxpulse-labview-api-ref`
- source_path: `resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01070.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01070.html
- document_id: `rfmxpulse-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean of the pulse-to-pulse frequency difference across the measured pulses. This value is expressed in Hz. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for

### Pulse:Results:Frequency and Phase:Pulse to Pulse Frequency Difference Mean (Hz)

Returns the mean of the pulse-to-pulse frequency difference across the measured pulses. This value is expressed in Hz.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Results Pulse to Pulse Freq Diff Mean (Hz) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxPulse Properties

<!--NI_TOPIC bundle=rfmxpulse-labview-api-ref path=resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0107a.html language=enus -->
## TOPIC 00043: Pulse:Results:Stability:Amplitude Mean (dB)

- bundle_id: `rfmxpulse-labview-api-ref`
- source_path: `resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0107a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0107a.html
- document_id: `rfmxpulse-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean of the amplitude stability values across the measured pulses. This value is expressed in dB. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named sig

### Pulse:Results:Stability:Amplitude Mean (dB)

Returns the mean of the amplitude stability values across the measured pulses. This value is expressed in dB.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Results Amplitude Stability Mean (dB) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxPulse Properties

<!--NI_TOPIC bundle=rfmxpulse-labview-api-ref path=resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0107c.html language=enus -->
## TOPIC 00044: Pulse:Results:Stability:Amplitude Minimum (dB)

- bundle_id: `rfmxpulse-labview-api-ref`
- source_path: `resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0107c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0107c.html
- document_id: `rfmxpulse-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the minimum amplitude stability across the measured pulses. This value is expressed in dB. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and re

### Pulse:Results:Stability:Amplitude Minimum (dB)

Returns the minimum amplitude stability across the measured pulses. This value is expressed in dB.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Results Amplitude Stability Min (dB) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxPulse Properties

<!--NI_TOPIC bundle=rfmxpulse-labview-api-ref path=resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0107d.html language=enus -->
## TOPIC 00045: Pulse:Results:Stability:Amplitude Standard Deviation (dB)

- bundle_id: `rfmxpulse-labview-api-ref`
- source_path: `resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0107d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0107d.html
- document_id: `rfmxpulse-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the amplitude stability standard deviation across the measured pulses. This value is expressed in dB. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named sig

### Pulse:Results:Stability:Amplitude Standard Deviation (dB)

Returns the amplitude stability standard deviation across the measured pulses. This value is expressed in dB.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Results Amplitude Stability SD (dB) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxPulse Properties

<!--NI_TOPIC bundle=rfmxpulse-labview-api-ref path=resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01082.html language=enus -->
## TOPIC 00046: Pulse:Results:Stability:Phase Standard Deviation (dB)

- bundle_id: `rfmxpulse-labview-api-ref`
- source_path: `resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01082.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01082.html
- document_id: `rfmxpulse-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the phase stability standard deviation across the measured pulses. This value is expressed in dB. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals

### Pulse:Results:Stability:Phase Standard Deviation (dB)

Returns the phase stability standard deviation across the measured pulses. This value is expressed in dB.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Results Phase Stability SD (dB) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxPulse Properties

<!--NI_TOPIC bundle=rfmxpulse-labview-api-ref path=resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01084.html language=enus -->
## TOPIC 00047: Pulse:Results:Stability:Total Mean (dB)

- bundle_id: `rfmxpulse-labview-api-ref`
- source_path: `resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01084.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01084.html
- document_id: `rfmxpulse-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean of the total stability values across the measured pulses. This value is expressed in dB. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals

### Pulse:Results:Stability:Total Mean (dB)

Returns the mean of the total stability values across the measured pulses. This value is expressed in dB.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Results Total Stability Mean (dB) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxPulse Properties

<!--NI_TOPIC bundle=rfmxpulse-labview-api-ref path=resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01085.html language=enus -->
## TOPIC 00048: Pulse:Results:Stability:Total Maximum (dB)

- bundle_id: `rfmxpulse-labview-api-ref`
- source_path: `resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01085.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01085.html
- document_id: `rfmxpulse-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum total stability across the measured pulses. This value is expressed in dB. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and result

### Pulse:Results:Stability:Total Maximum (dB)

Returns the maximum total stability across the measured pulses. This value is expressed in dB.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Results Total Stability Max (dB) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxPulse Properties

<!--NI_TOPIC bundle=rfmxpulse-labview-api-ref path=resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0109f.html language=enus -->
## TOPIC 00049: Pulse:Results:Frequency and Phase:Phase Error RMS Mean (deg)

- bundle_id: `rfmxpulse-labview-api-ref`
- source_path: `resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0109f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0109f.html
- document_id: `rfmxpulse-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean of the RMS phase error across the measured pulses. This value is expressed in degrees. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals a

### Pulse:Results:Frequency and Phase:Phase Error RMS Mean (deg)

Returns the mean of the RMS phase error across the measured pulses. This value is expressed in degrees.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Results Phase Err RMS Mean (deg) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxPulse Properties

<!--NI_TOPIC bundle=rfmxpulse-labview-api-ref path=resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010a3.html language=enus -->
## TOPIC 00050: Pulse:Results:Frequency and Phase:Phase Error Peak (deg)

- bundle_id: `rfmxpulse-labview-api-ref`
- source_path: `resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010a3.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010a3.html
- document_id: `rfmxpulse-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the peak phase error for all measured pulses. This value is expressed in degrees. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Re

### Pulse:Results:Frequency and Phase:Phase Error Peak (deg)

Returns the peak phase error for all measured pulses. This value is expressed in degrees.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Results Phase Err Pk (deg) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxPulse Properties

<!--NI_TOPIC bundle=rfmxpulse-labview-api-ref path=resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010a7.html language=enus -->
## TOPIC 00051: Pulse:Results:Frequency and Phase:Phase Error Peak Standard Deviation (deg)

- bundle_id: `rfmxpulse-labview-api-ref`
- source_path: `resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010a7.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010a7.html
- document_id: `rfmxpulse-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the standard deviation of the peak phase error across the measured pulses. This value is expressed in degrees. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for

### Pulse:Results:Frequency and Phase:Phase Error Peak Standard Deviation (deg)

Returns the standard deviation of the peak phase error across the measured pulses. This value is expressed in degrees.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Results Phase Err Pk SD (deg) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxPulse Properties

<!--NI_TOPIC bundle=rfmxpulse-labview-api-ref path=resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010aa.html language=enus -->
## TOPIC 00052: Pulse:Results:Frequency and Phase:Frequency Error RMS Mean (Hz)

- bundle_id: `rfmxpulse-labview-api-ref`
- source_path: `resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010aa.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010aa.html
- document_id: `rfmxpulse-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean of the RMS frequency error across the measured pulses. This value is expressed in Hz. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals an

### Pulse:Results:Frequency and Phase:Frequency Error RMS Mean (Hz)

Returns the mean of the RMS frequency error across the measured pulses. This value is expressed in Hz.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Results Freq Err RMS Mean (Hz) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxPulse Properties

<!--NI_TOPIC bundle=rfmxpulse-labview-api-ref path=resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010ad.html language=enus -->
## TOPIC 00053: Pulse:Results:Frequency and Phase:Frequency Error RMS Standard Deviation (Hz)

- bundle_id: `rfmxpulse-labview-api-ref`
- source_path: `resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010ad.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010ad.html
- document_id: `rfmxpulse-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the standard deviation of the RMS frequency error across the measured pulses. This value is expressed in Hz. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for na

### Pulse:Results:Frequency and Phase:Frequency Error RMS Standard Deviation (Hz)

Returns the standard deviation of the RMS frequency error across the measured pulses. This value is expressed in Hz.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Results Freq Err RMS SD (Hz) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxPulse Properties

<!--NI_TOPIC bundle=rfmxpulse-labview-api-ref path=resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010b0.html language=enus -->
## TOPIC 00054: Pulse:Results:Frequency and Phase:Frequency Error Peak Maximum (Hz)

- bundle_id: `rfmxpulse-labview-api-ref`
- source_path: `resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010b0.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010b0.html
- document_id: `rfmxpulse-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum peak frequency error across the measured pulses. This value is expressed in Hz. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and r

### Pulse:Results:Frequency and Phase:Frequency Error Peak Maximum (Hz)

Returns the maximum peak frequency error across the measured pulses. This value is expressed in Hz.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Results Freq Err Pk Max (Hz) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxPulse Properties

<!--NI_TOPIC bundle=rfmxpulse-labview-api-ref path=resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010b6.html language=enus -->
## TOPIC 00055: Pulse:Results:FM Chirp:Rate Maximum (Hz/us)

- bundle_id: `rfmxpulse-labview-api-ref`
- source_path: `resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010b6.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010b6.html
- document_id: `rfmxpulse-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum FM chirp rate across the measured pulses. This value is expressed in Hz/us. This result is valid for linear FM and triangular FM modulation. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic fo

### Pulse:Results:FM Chirp:Rate Maximum (Hz/us)

Returns the maximum FM chirp rate across the measured pulses. This value is expressed in Hz/us.
 This result is valid for linear FM and triangular FM modulation.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Results Chirp Rate Max (Hz/us) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxPulse Properties

<!--NI_TOPIC bundle=rfmxpulse-labview-api-ref path=resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010b7.html language=enus -->
## TOPIC 00056: Pulse:Results:FM Chirp:Rate Minimum (Hz/us)

- bundle_id: `rfmxpulse-labview-api-ref`
- source_path: `resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010b7.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010b7.html
- document_id: `rfmxpulse-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the minimum FM chirp rate across the measured pulses. This value is expressed in Hz/us. This result is valid for linear FM and triangular FM modulation. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic fo

### Pulse:Results:FM Chirp:Rate Minimum (Hz/us)

Returns the minimum FM chirp rate across the measured pulses. This value is expressed in Hz/us.
 This result is valid for linear FM and triangular FM modulation.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Results Chirp Rate Min (Hz/us) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxPulse Properties

<!--NI_TOPIC bundle=rfmxpulse-labview-api-ref path=resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010b8.html language=enus -->
## TOPIC 00057: Pulse:Results:FM Chirp:Rate Standard Deviation (Hz/us)

- bundle_id: `rfmxpulse-labview-api-ref`
- source_path: `resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010b8.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010b8.html
- document_id: `rfmxpulse-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the standard deviation of the FM chirp rates across the measured pulses. This value is expressed in Hz/us. This result is valid for linear FM and triangular FM modulation. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Select

### Pulse:Results:FM Chirp:Rate Standard Deviation (Hz/us)

Returns the standard deviation of the FM chirp rates across the measured pulses. This value is expressed in Hz/us.
 This result is valid for linear FM and triangular FM modulation.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Results Chirp Rate SD (Hz/us) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxPulse Properties

<!--NI_TOPIC bundle=rfmxpulse-labview-api-ref path=resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010b9.html language=enus -->
## TOPIC 00058: Pulse:Results:FM Chirp:Start Frequency (Hz)

- bundle_id: `rfmxpulse-labview-api-ref`
- source_path: `resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010b9.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010b9.html
- document_id: `rfmxpulse-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the start frequencies of the best-fit linear least square regression line measured over user specified sample analysis time interval as determined by Pulse Freq Phase Dev Range Length (%) property for the measured pulses. This value is expressed in Hz. This result is valid for linear FM and

### Pulse:Results:FM Chirp:Start Frequency (Hz)

Returns the start frequencies of the best-fit linear least square regression line measured over user specified sample analysis time interval as determined by [Pulse Freq Phase Dev Range Length (%)](/csh?context=rfmxpulse_rfmxpulseprop_attrc0108e) property for the measured pulses. This value is expressed in Hz.
 This result is valid for linear FM and triangular FM modulation.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Results Chirp Start Freq (Hz) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxPulse Properties

<!--NI_TOPIC bundle=rfmxpulse-labview-api-ref path=resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010ba.html language=enus -->
## TOPIC 00059: Pulse:Results:FM Chirp:Start Frequency Mean (Hz)

- bundle_id: `rfmxpulse-labview-api-ref`
- source_path: `resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010ba.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010ba.html
- document_id: `rfmxpulse-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean of the FM chirp start frequency across the measured pulses. This value is expressed in Hz. This result is valid for linear FM and triangular FM modulation. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Stri

### Pulse:Results:FM Chirp:Start Frequency Mean (Hz)

Returns the mean of the FM chirp start frequency across the measured pulses. This value is expressed in Hz.
 This result is valid for linear FM and triangular FM modulation.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Results Chirp Start Freq Mean (Hz) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxPulse Properties

<!--NI_TOPIC bundle=rfmxpulse-labview-api-ref path=resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010bb.html language=enus -->
## TOPIC 00060: Pulse:Results:FM Chirp:Start Frequency Maximum (Hz)

- bundle_id: `rfmxpulse-labview-api-ref`
- source_path: `resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010bb.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010bb.html
- document_id: `rfmxpulse-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum FM chirp start frequency among the measured pulses. This value is expressed in Hz. This result is valid for linear FM and triangular FM modulation. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings t

### Pulse:Results:FM Chirp:Start Frequency Maximum (Hz)

Returns the maximum FM chirp start frequency among the measured pulses. This value is expressed in Hz.
 This result is valid for linear FM and triangular FM modulation.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Results Chirp Start Freq Max (Hz) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxPulse Properties

<!--NI_TOPIC bundle=rfmxpulse-labview-api-ref path=resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010bc.html language=enus -->
## TOPIC 00061: Pulse:Results:FM Chirp:Start Frequency Minimum (Hz)

- bundle_id: `rfmxpulse-labview-api-ref`
- source_path: `resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010bc.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010bc.html
- document_id: `rfmxpulse-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the minimum FM chirp start frequency among the measured pulses. This value is expressed in Hz. This result is valid for linear FM and triangular FM modulation. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings t

### Pulse:Results:FM Chirp:Start Frequency Minimum (Hz)

Returns the minimum FM chirp start frequency among the measured pulses. This value is expressed in Hz.
 This result is valid for linear FM and triangular FM modulation.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Results Chirp Start Freq Min (Hz) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxPulse Properties

<!--NI_TOPIC bundle=rfmxpulse-labview-api-ref path=resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010bd.html language=enus -->
## TOPIC 00062: Pulse:Results:FM Chirp:Start Frequency Standard Deviation (Hz)

- bundle_id: `rfmxpulse-labview-api-ref`
- source_path: `resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010bd.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010bd.html
- document_id: `rfmxpulse-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the FM chirp start frequency standard deviation across the measured pulses. This value is expressed in Hz. This result is valid for linear FM and triangular FM modulation. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Select

### Pulse:Results:FM Chirp:Start Frequency Standard Deviation (Hz)

Returns the FM chirp start frequency standard deviation across the measured pulses. This value is expressed in Hz.
 This result is valid for linear FM and triangular FM modulation.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Results Chirp Start Freq SD (Hz) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxPulse Properties

<!--NI_TOPIC bundle=rfmxpulse-labview-api-ref path=resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010be.html language=enus -->
## TOPIC 00063: Pulse:Results:FM Chirp:Stop Frequency (Hz)

- bundle_id: `rfmxpulse-labview-api-ref`
- source_path: `resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010be.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010be.html
- document_id: `rfmxpulse-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the stop frequencies of the best-fit linear least square regression line measured over user specified sample analysis time interval as determined by Pulse Freq Phase Dev Range Length (%) property for the measured pulses. This value is expressed in Hz. This result is valid for linear FM and t

### Pulse:Results:FM Chirp:Stop Frequency (Hz)

Returns the stop frequencies of the best-fit linear least square regression line measured over user specified sample analysis time interval as determined by [Pulse Freq Phase Dev Range Length (%)](/csh?context=rfmxpulse_rfmxpulseprop_attrc0108e) property for the measured pulses. This value is expressed in Hz.
 This result is valid for linear FM and triangular FM modulation.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Results Chirp Stop Freq (Hz) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxPulse Properties

<!--NI_TOPIC bundle=rfmxpulse-labview-api-ref path=resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010bf.html language=enus -->
## TOPIC 00064: Pulse:Results:FM Chirp:Stop Frequency Mean (Hz)

- bundle_id: `rfmxpulse-labview-api-ref`
- source_path: `resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010bf.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010bf.html
- document_id: `rfmxpulse-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean of the FM chirp stop frequency across the measured pulses. This value is expressed in Hz. This result is valid for linear FM and triangular FM modulation. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strin

### Pulse:Results:FM Chirp:Stop Frequency Mean (Hz)

Returns the mean of the FM chirp stop frequency across the measured pulses. This value is expressed in Hz.
 This result is valid for linear FM and triangular FM modulation.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Results Chirp Stop Freq Mean (Hz) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxPulse Properties

<!--NI_TOPIC bundle=rfmxpulse-labview-api-ref path=resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010c0.html language=enus -->
## TOPIC 00065: Pulse:Results:FM Chirp:Stop Frequency Maximum (Hz)

- bundle_id: `rfmxpulse-labview-api-ref`
- source_path: `resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010c0.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010c0.html
- document_id: `rfmxpulse-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum FM chirp stop frequency among the measured pulses. This value is expressed in Hz. This result is valid for linear FM and triangular FM modulation. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings to

### Pulse:Results:FM Chirp:Stop Frequency Maximum (Hz)

Returns the maximum FM chirp stop frequency among the measured pulses. This value is expressed in Hz.
 This result is valid for linear FM and triangular FM modulation.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Results Chirp Stop Freq Max (Hz) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxPulse Properties

<!--NI_TOPIC bundle=rfmxpulse-labview-api-ref path=resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010c1.html language=enus -->
## TOPIC 00066: Pulse:Results:FM Chirp:Stop Frequency Minimum (Hz)

- bundle_id: `rfmxpulse-labview-api-ref`
- source_path: `resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010c1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010c1.html
- document_id: `rfmxpulse-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the minimum FM chirp stop frequency among the measured pulses. This value is expressed in Hz. This result is valid for linear FM and triangular FM modulation. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings to

### Pulse:Results:FM Chirp:Stop Frequency Minimum (Hz)

Returns the minimum FM chirp stop frequency among the measured pulses. This value is expressed in Hz.
 This result is valid for linear FM and triangular FM modulation.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Results Chirp Stop Freq Min (Hz) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxPulse Properties

<!--NI_TOPIC bundle=rfmxpulse-labview-api-ref path=resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010c2.html language=enus -->
## TOPIC 00067: Pulse:Results:FM Chirp:Stop Frequency Standard Deviation (Hz)

- bundle_id: `rfmxpulse-labview-api-ref`
- source_path: `resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010c2.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010c2.html
- document_id: `rfmxpulse-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the FM chirp stop frequency standard deviation across the measured pulses. This value is expressed in Hz. This result is valid for linear FM and triangular FM modulation. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selecto

### Pulse:Results:FM Chirp:Stop Frequency Standard Deviation (Hz)

Returns the FM chirp stop frequency standard deviation across the measured pulses. This value is expressed in Hz.
 This result is valid for linear FM and triangular FM modulation.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Results Chirp Stop Freq SD (Hz) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxPulse Properties

<!--NI_TOPIC bundle=rfmxpulse-labview-api-ref path=resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010d0.html language=enus -->
## TOPIC 00068: Pulse:Results:FM Chirp:Rate2 Minimum (Hz/us)

- bundle_id: `rfmxpulse-labview-api-ref`
- source_path: `resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010d0.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010d0.html
- document_id: `rfmxpulse-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the minimum FM chirp rate2 value across the measured pulses. This value is expressed in Hz/us. This result is valid only for triangular FM modulation. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for

### Pulse:Results:FM Chirp:Rate2 Minimum (Hz/us)

Returns the minimum FM chirp rate2 value across the measured pulses. This value is expressed in Hz/us.
 This result is valid only for triangular FM modulation.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Results Chirp Rate2 Min (Hz/us) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxPulse Properties

<!--NI_TOPIC bundle=rfmxpulse-labview-api-ref path=resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010d1.html language=enus -->
## TOPIC 00069: Pulse:Results:FM Chirp:Rate2 Standard Deviation (Hz/us)

- bundle_id: `rfmxpulse-labview-api-ref`
- source_path: `resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010d1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010d1.html
- document_id: `rfmxpulse-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the standard deviation of the FM chirp rate2 values across the measured pulses. This value is expressed in Hz/us. This result is valid only for triangular FM modulation. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector

### Pulse:Results:FM Chirp:Rate2 Standard Deviation (Hz/us)

Returns the standard deviation of the FM chirp rate2 values across the measured pulses. This value is expressed in Hz/us.
 This result is valid only for triangular FM modulation.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Results Chirp Rate2 SD (Hz/us) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxPulse Properties

<!--NI_TOPIC bundle=rfmxpulse-labview-api-ref path=resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010d2.html language=enus -->
## TOPIC 00070: Pulse:Results:FM Chirp:Start Frequency2 (Hz)

- bundle_id: `rfmxpulse-labview-api-ref`
- source_path: `resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010d2.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010d2.html
- document_id: `rfmxpulse-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the start frequency of the 2nd best-fit linear least square regression line measured over user specified sample analysis time interval as determined by Pulse Freq Phase Dev Range Length (%) property for the measured pulses. This value is expressed in Hz. This result is valid only for triangu

### Pulse:Results:FM Chirp:Start Frequency2 (Hz)

Returns the start frequency of the 2nd best-fit linear least square regression line measured over user specified sample analysis time interval as determined by [Pulse Freq Phase Dev Range Length (%)](/csh?context=rfmxpulse_rfmxpulseprop_attrc0108e) property for the measured pulses. This value is expressed in Hz.
 This result is valid only for triangular FM modulation.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Results Chirp Start Freq2 (Hz) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxPulse Properties

<!--NI_TOPIC bundle=rfmxpulse-labview-api-ref path=resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010d3.html language=enus -->
## TOPIC 00071: Pulse:Results:FM Chirp:Start Frequency2 Mean (Hz)

- bundle_id: `rfmxpulse-labview-api-ref`
- source_path: `resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010d3.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010d3.html
- document_id: `rfmxpulse-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean of the FM chirp start frequency2 across the measured pulses. This value is expressed in Hz. This result is valid only for triangular FM modulation. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topi

### Pulse:Results:FM Chirp:Start Frequency2 Mean (Hz)

Returns the mean of the FM chirp start frequency2 across the measured pulses. This value is expressed in Hz.
 This result is valid only for triangular FM modulation.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Results Chirp Start Freq2 Mean (Hz) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxPulse Properties

<!--NI_TOPIC bundle=rfmxpulse-labview-api-ref path=resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010d4.html language=enus -->
## TOPIC 00072: Pulse:Results:FM Chirp:Start Frequency2 Maximum (Hz)

- bundle_id: `rfmxpulse-labview-api-ref`
- source_path: `resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010d4.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010d4.html
- document_id: `rfmxpulse-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum FM chirp start frequency2 among the measured pulses. This value is expressed in Hz. This result is valid only for triangular FM modulation. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for

### Pulse:Results:FM Chirp:Start Frequency2 Maximum (Hz)

Returns the maximum FM chirp start frequency2 among the measured pulses. This value is expressed in Hz.
 This result is valid only for triangular FM modulation.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Results Chirp Start Freq2 Max (Hz) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxPulse Properties

<!--NI_TOPIC bundle=rfmxpulse-labview-api-ref path=resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010d5.html language=enus -->
## TOPIC 00073: Pulse:Results:FM Chirp:Start Frequency2 Minimum (Hz)

- bundle_id: `rfmxpulse-labview-api-ref`
- source_path: `resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010d5.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010d5.html
- document_id: `rfmxpulse-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the minimum FM chirp start frequency2 among the measured pulses. This value is expressed in Hz. This result is valid only for triangular FM modulation. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for

### Pulse:Results:FM Chirp:Start Frequency2 Minimum (Hz)

Returns the minimum FM chirp start frequency2 among the measured pulses. This value is expressed in Hz.
 This result is valid only for triangular FM modulation.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Results Chirp Start Freq2 Min (Hz) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxPulse Properties

<!--NI_TOPIC bundle=rfmxpulse-labview-api-ref path=resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010d6.html language=enus -->
## TOPIC 00074: Pulse:Results:FM Chirp:Start Frequency2 Standard Deviation (Hz)

- bundle_id: `rfmxpulse-labview-api-ref`
- source_path: `resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010d6.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010d6.html
- document_id: `rfmxpulse-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the FM chirp start frequency2 standard deviation across the measured pulses. This value is expressed in Hz. This result is valid only for triangular FM modulation. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strin

### Pulse:Results:FM Chirp:Start Frequency2 Standard Deviation (Hz)

Returns the FM chirp start frequency2 standard deviation across the measured pulses. This value is expressed in Hz.
 This result is valid only for triangular FM modulation.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Results Chirp Start Freq2 SD (Hz) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxPulse Properties

<!--NI_TOPIC bundle=rfmxpulse-labview-api-ref path=resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010d7.html language=enus -->
## TOPIC 00075: Pulse:Results:FM Chirp:Stop Frequency2 (Hz)

- bundle_id: `rfmxpulse-labview-api-ref`
- source_path: `resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010d7.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010d7.html
- document_id: `rfmxpulse-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the stop frequency of the 2nd best-fit linear least square regression line measured over user specified sample analysis time interval as determined by Pulse Freq Phase Dev Range Length (%) property for the measured pulses. This value is expressed in Hz. This result is valid only for triangul

### Pulse:Results:FM Chirp:Stop Frequency2 (Hz)

Returns the stop frequency of the 2nd best-fit linear least square regression line measured over user specified sample analysis time interval as determined by [Pulse Freq Phase Dev Range Length (%)](/csh?context=rfmxpulse_rfmxpulseprop_attrc0108e) property for the measured pulses. This value is expressed in Hz.
 This result is valid only for triangular FM modulation.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Results Chirp Stop Freq2 (Hz) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxPulse Properties

<!--NI_TOPIC bundle=rfmxpulse-labview-api-ref path=resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010d8.html language=enus -->
## TOPIC 00076: Pulse:Results:FM Chirp:Stop Frequency2 Mean (Hz)

- bundle_id: `rfmxpulse-labview-api-ref`
- source_path: `resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010d8.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010d8.html
- document_id: `rfmxpulse-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean of the FM chirp stop frequency2 across the measured pulses. This value is expressed in Hz. This result is valid only for triangular FM modulation. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic

### Pulse:Results:FM Chirp:Stop Frequency2 Mean (Hz)

Returns the mean of the FM chirp stop frequency2 across the measured pulses. This value is expressed in Hz.
 This result is valid only for triangular FM modulation.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Results Chirp Stop Freq2 Mean (Hz) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxPulse Properties

<!--NI_TOPIC bundle=rfmxpulse-labview-api-ref path=resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010d9.html language=enus -->
## TOPIC 00077: Pulse:Results:FM Chirp:Stop Frequency2 Maximum (Hz)

- bundle_id: `rfmxpulse-labview-api-ref`
- source_path: `resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010d9.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010d9.html
- document_id: `rfmxpulse-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum FM chirp stop frequency2 among the measured pulses. This value is expressed in Hz. This result is valid only for triangular FM modulation. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for

### Pulse:Results:FM Chirp:Stop Frequency2 Maximum (Hz)

Returns the maximum FM chirp stop frequency2 among the measured pulses. This value is expressed in Hz.
 This result is valid only for triangular FM modulation.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Results Chirp Stop Freq2 Max (Hz) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxPulse Properties

<!--NI_TOPIC bundle=rfmxpulse-labview-api-ref path=resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010da.html language=enus -->
## TOPIC 00078: Pulse:Results:FM Chirp:Stop Frequency2 Minimum (Hz)

- bundle_id: `rfmxpulse-labview-api-ref`
- source_path: `resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010da.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010da.html
- document_id: `rfmxpulse-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the minimum FM chirp stop frequency2 among the measured pulses. This value is expressed in Hz. This result is valid only for triangular FM modulation. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for

### Pulse:Results:FM Chirp:Stop Frequency2 Minimum (Hz)

Returns the minimum FM chirp stop frequency2 among the measured pulses. This value is expressed in Hz.
 This result is valid only for triangular FM modulation.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Results Chirp Stop Freq2 Min (Hz) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxPulse Properties

<!--NI_TOPIC bundle=rfmxpulse-labview-api-ref path=resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010db.html language=enus -->
## TOPIC 00079: Pulse:Results:FM Chirp:Stop Frequency2 Standard Deviation (Hz)

- bundle_id: `rfmxpulse-labview-api-ref`
- source_path: `resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010db.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010db.html
- document_id: `rfmxpulse-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the FM chirp stop frequency2 standard deviation across the measured pulses. This value is expressed in Hz. This result is valid only for triangular FM modulation. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector String

### Pulse:Results:FM Chirp:Stop Frequency2 Standard Deviation (Hz)

Returns the FM chirp stop frequency2 standard deviation across the measured pulses. This value is expressed in Hz.
 This result is valid only for triangular FM modulation.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Results Chirp Stop Freq2 SD (Hz) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxPulse Properties

<!--NI_TOPIC bundle=rfmxpulse-labview-api-ref path=resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010dc.html language=enus -->
## TOPIC 00080: Pulse:Amplitude Trace Unit

- bundle_id: `rfmxpulse-labview-api-ref`
- source_path: `resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010dc.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010dc.html
- document_id: `rfmxpulse-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the unit of the amplitude level. This property is applicable only for the amplitude and acquired amplitude trace. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the strin

### Pulse:Amplitude Trace Unit

Specifies the unit of the amplitude level. This property is applicable only for the amplitude and acquired amplitude trace.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **dBm**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Amplitude Trace Unit |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| dBm | 0 | Amplitude trace is expressed in dBm. |
| --- | --- | --- |
| Volts | 1 | Amplitude trace is expressed in Volts. |
| Watts | 2 | Amplitude trace is expressed in Watts. |

Parent topic:

RFmxPulse Properties

<!--NI_TOPIC bundle=rfmxpulse-labview-api-ref path=resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010dd.html language=enus -->
## TOPIC 00081: Pulse:Metrics:Amplitude Deviation Unit

- bundle_id: `rfmxpulse-labview-api-ref`
- source_path: `resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010dd.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010dd.html
- document_id: `rfmxpulse-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the unit for amplitude deviation results. This property is applicable only for droop, ripple and overshoot results. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the str

### Pulse:Metrics:Amplitude Deviation Unit

Specifies the unit for amplitude deviation results. This property is applicable only for droop, ripple and overshoot results.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **Percentage**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Amplitude Deviation Unit |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| Percentage | 0 | Amplitude deviation results are returned as a percentage. |
| --- | --- | --- |
| dB | 1 | Amplitude deviation results are returned in dB. |

Parent topic:

RFmxPulse Properties

<!--NI_TOPIC bundle=rfmxpulse-labview-api-ref path=resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010df.html language=enus -->
## TOPIC 00082: Pulse:Multiburst:Length (Pulses)

- bundle_id: `rfmxpulse-labview-api-ref`
- source_path: `resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010df.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010df.html
- document_id: `rfmxpulse-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of pulses assigned to a single burst. A minimum of 10 pulses per burst is required for pulse measurements. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the s

### Pulse:Multiburst:Length (Pulses)

Specifies the number of pulses assigned to a single burst.

A minimum of 10 pulses per burst is required for pulse measurements.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is 10.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Burst Length (Pulses) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxPulse Properties

<!--NI_TOPIC bundle=rfmxpulse-labview-api-ref path=resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010e0.html language=enus -->
## TOPIC 00083: Pulse:Selected Burst Trace

- bundle_id: `rfmxpulse-labview-api-ref`
- source_path: `resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010e0.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010e0.html
- document_id: `rfmxpulse-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the burst number selected for the display of traces. This property is applicable for IQ, amplitude and pulse stability traces. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information ab

### Pulse:Selected Burst Trace

Specifies the burst number selected for the display of traces. This property is applicable for IQ, amplitude and pulse stability traces.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is 0.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Selected Burst Trace |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxPulse Properties

<!--NI_TOPIC bundle=rfmxpulse-labview-api-ref path=resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010e7.html language=enus -->
## TOPIC 00084: Pulse:Time Sidelobe:Enabled

- bundle_id: `rfmxpulse-labview-api-ref`
- source_path: `resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010e7.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010e7.html
- document_id: `rfmxpulse-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable pulse time sidelobe results computation. You can use the RFmxPulse Configure Reference Waveform (1 Wfm) VI to set the reference waveform for correlation computation. You do not need to use a selector string to configure or read this property for the default signal instanc

### Pulse:Time Sidelobe:Enabled

Specifies whether to enable pulse time sidelobe results computation. You can use the [RFmxPulse Configure Reference Waveform (1 Wfm)](/csh?context=rfmxpulse_rfmxpulsevi_rfmxpulse_configure_reference_waveform_(1_wfm)) VI to set the reference waveform for correlation computation.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **False**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Time Sidelobe Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| False | 0 | Pulse Time Sidelobe results computation is disabled. |
| --- | --- | --- |
| True | 1 | Pulse Time Sidelobe results computation is enabled. |

Parent topic:

RFmxPulse Properties

<!--NI_TOPIC bundle=rfmxpulse-labview-api-ref path=resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010ed.html language=enus -->
## TOPIC 00085: Pulse:Results:Time Sidelobe:Mainlobe Width Mean (s)

- bundle_id: `rfmxpulse-labview-api-ref`
- source_path: `resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010ed.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010ed.html
- document_id: `rfmxpulse-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean of the mainlobe width values across the measured pulses. This value is expressed in seconds. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named sig

### Pulse:Results:Time Sidelobe:Mainlobe Width Mean (s)

Returns the mean of the mainlobe width values across the measured pulses. This value is expressed in seconds.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Results Mainlobe Width Mean (s) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxPulse Properties

<!--NI_TOPIC bundle=rfmxpulse-labview-api-ref path=resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010ee.html language=enus -->
## TOPIC 00086: Pulse:Results:Time Sidelobe:Mainlobe Width Maximum (s)

- bundle_id: `rfmxpulse-labview-api-ref`
- source_path: `resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010ee.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010ee.html
- document_id: `rfmxpulse-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum mainlobe width across the measured pulses. This value is expressed in seconds. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and re

### Pulse:Results:Time Sidelobe:Mainlobe Width Maximum (s)

Returns the maximum mainlobe width across the measured pulses. This value is expressed in seconds.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Results Mainlobe Width Max (s) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxPulse Properties

<!--NI_TOPIC bundle=rfmxpulse-labview-api-ref path=resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010ef.html language=enus -->
## TOPIC 00087: Pulse:Results:Time Sidelobe:Mainlobe Width Minimum (s)

- bundle_id: `rfmxpulse-labview-api-ref`
- source_path: `resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010ef.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010ef.html
- document_id: `rfmxpulse-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the minimum mainlobe width across the measured pulses. This value is expressed in seconds. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and re

### Pulse:Results:Time Sidelobe:Mainlobe Width Minimum (s)

Returns the minimum mainlobe width across the measured pulses. This value is expressed in seconds.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Results Mainlobe Width Min (s) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxPulse Properties

<!--NI_TOPIC bundle=rfmxpulse-labview-api-ref path=resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010f0.html language=enus -->
## TOPIC 00088: Pulse:Results:Time Sidelobe:Mainlobe Width Standard Deviation (s)

- bundle_id: `rfmxpulse-labview-api-ref`
- source_path: `resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010f0.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010f0.html
- document_id: `rfmxpulse-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the standard deviation of the mainlobe width values across the measured pulses. This value is expressed in seconds. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax

### Pulse:Results:Time Sidelobe:Mainlobe Width Standard Deviation (s)

Returns the standard deviation of the mainlobe width values across the measured pulses. This value is expressed in seconds.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Results Mainlobe Width SD (s) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxPulse Properties

<!--NI_TOPIC bundle=rfmxpulse-labview-api-ref path=resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010f1.html language=enus -->
## TOPIC 00089: Pulse:Results:Time Sidelobe:Delay (s)

- bundle_id: `rfmxpulse-labview-api-ref`
- source_path: `resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010f1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010f1.html
- document_id: `rfmxpulse-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the sidelobe delay for all measured pulses. Sidelobe delay is the time elapsed between the highest sidelobe peak and mainlobe peak level. This value is expressed in seconds. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Sele

### Pulse:Results:Time Sidelobe:Delay (s)

Returns the sidelobe delay for all measured pulses. Sidelobe delay is the time elapsed between the highest sidelobe peak and mainlobe peak level. This value is expressed in seconds.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Results Sidelobe Delay (s) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxPulse Properties

<!--NI_TOPIC bundle=rfmxpulse-labview-api-ref path=resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010f2.html language=enus -->
## TOPIC 00090: Pulse:Results:Time Sidelobe:Delay Mean (s)

- bundle_id: `rfmxpulse-labview-api-ref`
- source_path: `resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010f2.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010f2.html
- document_id: `rfmxpulse-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean of the sidelobe delay values across the measured pulses. This value is expressed in seconds. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named sig

### Pulse:Results:Time Sidelobe:Delay Mean (s)

Returns the mean of the sidelobe delay values across the measured pulses. This value is expressed in seconds.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Results Sidelobe Delay Mean (s) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxPulse Properties

<!--NI_TOPIC bundle=rfmxpulse-labview-api-ref path=resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010f3.html language=enus -->
## TOPIC 00091: Pulse:Results:Time Sidelobe:Delay Maximum (s)

- bundle_id: `rfmxpulse-labview-api-ref`
- source_path: `resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010f3.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010f3.html
- document_id: `rfmxpulse-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum sidelobe delay across the measured pulses. This value is expressed in seconds. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and re

### Pulse:Results:Time Sidelobe:Delay Maximum (s)

Returns the maximum sidelobe delay across the measured pulses. This value is expressed in seconds.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Results Sidelobe Delay Max (s) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxPulse Properties

<!--NI_TOPIC bundle=rfmxpulse-labview-api-ref path=resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010f4.html language=enus -->
## TOPIC 00092: Pulse:Results:Time Sidelobe:Delay Minimum (s)

- bundle_id: `rfmxpulse-labview-api-ref`
- source_path: `resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010f4.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010f4.html
- document_id: `rfmxpulse-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the minimum sidelobe delay across the measured pulses. This value is expressed in seconds. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and re

### Pulse:Results:Time Sidelobe:Delay Minimum (s)

Returns the minimum sidelobe delay across the measured pulses. This value is expressed in seconds.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Results Sidelobe Delay Min (s) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxPulse Properties

<!--NI_TOPIC bundle=rfmxpulse-labview-api-ref path=resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010f5.html language=enus -->
## TOPIC 00093: Pulse:Results:Time Sidelobe:Delay Standard Deviation (s)

- bundle_id: `rfmxpulse-labview-api-ref`
- source_path: `resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010f5.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010f5.html
- document_id: `rfmxpulse-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the standard deviation of the sidelobe delay values across the measured pulses. This value is expressed in seconds. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax

### Pulse:Results:Time Sidelobe:Delay Standard Deviation (s)

Returns the standard deviation of the sidelobe delay values across the measured pulses. This value is expressed in seconds.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Results Sidelobe Delay SD (s) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxPulse Properties

<!--NI_TOPIC bundle=rfmxpulse-labview-api-ref path=resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010f6.html language=enus -->
## TOPIC 00094: Pulse:Results:Time Sidelobe:Peak Sidelobe Level (dB)

- bundle_id: `rfmxpulse-labview-api-ref`
- source_path: `resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010f6.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010f6.html
- document_id: `rfmxpulse-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the peak sidelobe level for all measured pulses. Peak sidelobe level is the ratio of the highest sidelobe peak to the mainlobe peak level. This value is expressed in dB. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector

### Pulse:Results:Time Sidelobe:Peak Sidelobe Level (dB)

Returns the peak sidelobe level for all measured pulses. Peak sidelobe level is the ratio of the highest sidelobe peak to the mainlobe peak level. This value is expressed in dB.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Results Pk Sidelobe Level (dB) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxPulse Properties

<!--NI_TOPIC bundle=rfmxpulse-labview-api-ref path=resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010f9.html language=enus -->
## TOPIC 00095: Pulse:Results:Time Sidelobe: Peak Sidelobe Level Minimum (dB)

- bundle_id: `rfmxpulse-labview-api-ref`
- source_path: `resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010f9.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010f9.html
- document_id: `rfmxpulse-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the minimum peak sidelobe level across the measured pulses. This value is expressed in dB. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and re

### Pulse:Results:Time Sidelobe: Peak Sidelobe Level Minimum (dB)

Returns the minimum peak sidelobe level across the measured pulses. This value is expressed in dB.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Results Pk Sidelobe Level Min (dB) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxPulse Properties

<!--NI_TOPIC bundle=rfmxpulse-labview-api-ref path=resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010fd.html language=enus -->
## TOPIC 00096: Pulse:Results:Time Sidelobe:Compression Ratio Maximum (%)

- bundle_id: `rfmxpulse-labview-api-ref`
- source_path: `resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010fd.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc010fd.html
- document_id: `rfmxpulse-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum compression ratio across the measured pulses. This value is expressed as a percentage. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signal

### Pulse:Results:Time Sidelobe:Compression Ratio Maximum (%)

Returns the maximum compression ratio across the measured pulses. This value is expressed as a percentage.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Results Compression Ratio Max (%) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxPulse Properties

<!--NI_TOPIC bundle=rfmxpulse-labview-api-ref path=resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01101.html language=enus -->
## TOPIC 00097: Pulse:Results:Time Sidelobe:Peak Correlation Mean

- bundle_id: `rfmxpulse-labview-api-ref`
- source_path: `resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01101.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01101.html
- document_id: `rfmxpulse-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean of the peak correlation values across the measured pulses. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Remarks The foll

### Pulse:Results:Time Sidelobe:Peak Correlation Mean

Returns the mean of the peak correlation values across the measured pulses.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Results Pk Correlation Mean |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxPulse Properties

<!--NI_TOPIC bundle=rfmxpulse-labview-api-ref path=resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01102.html language=enus -->
## TOPIC 00098: Pulse:Results:Time Sidelobe:Peak Correlation Maximum

- bundle_id: `rfmxpulse-labview-api-ref`
- source_path: `resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01102.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01102.html
- document_id: `rfmxpulse-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum peak correlation across the measured pulses. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Remarks The following table

### Pulse:Results:Time Sidelobe:Peak Correlation Maximum

Returns the maximum peak correlation across the measured pulses.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Results Pk Correlation Max |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxPulse Properties

<!--NI_TOPIC bundle=rfmxpulse-labview-api-ref path=resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0110d.html language=enus -->
## TOPIC 00099: Pulse:Results:Time:Fall Edge (s)

- bundle_id: `rfmxpulse-labview-api-ref`
- source_path: `resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0110d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0110d.html
- document_id: `rfmxpulse-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the fall edge for all measured pulses. Fall edge is the absolute time instant when the pulse exceeds the falling edge width threshold. This value is expressed in seconds. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selecto

### Pulse:Results:Time:Fall Edge (s)

Returns the fall edge for all measured pulses. Fall edge is the absolute time instant when the pulse exceeds the falling edge width threshold. This value is expressed in seconds.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Results Fall Edge (s) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxPulse Properties

<!--NI_TOPIC bundle=rfmxpulse-labview-api-ref path=resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0110e.html language=enus -->
## TOPIC 00100: Pulse:Acquisition Trace:Select

- bundle_id: `rfmxpulse-labview-api-ref`
- source_path: `resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0110e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0110e.html
- document_id: `rfmxpulse-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the mode to select all pulses or the subset of acquired pulses available for display acquisition trace, limited to Max Pulse Count Enabled property if set to True. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Sele

### Pulse:Acquisition Trace:Select

Specifies the mode to select all pulses or the subset of acquired pulses available for display acquisition trace, limited to [Max Pulse Count Enabled](/csh?topicname=attrc00012.html) property if set to **True**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **Subset**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Acquisition Trace Select |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| All Pulses | 0 | Selects all the acquired pulses. |
| --- | --- | --- |
| Subset | 1 |  |

Parent topic:

RFmxPulse Properties

<!--NI_TOPIC bundle=rfmxpulse-labview-api-ref path=resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0110f.html language=enus -->
## TOPIC 00101: Pulse:Acquisition Trace:Subset Offset

- bundle_id: `rfmxpulse-labview-api-ref`
- source_path: `resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0110f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0110f.html
- document_id: `rfmxpulse-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the offset in number of pulses to be used for display acquisition trace. You must configure this property when you set the Pulse Acquisition Trace Select property to Subset. You do not need to use a selector string to configure or read this property for the default signal instance. Refer t

### Pulse:Acquisition Trace:Subset Offset

Specifies the offset in number of pulses to be used for display acquisition trace. You must configure this property when you set the [Pulse Acquisition Trace Select](/csh?topicname=attrc0110e.html) property to **Subset**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is 0. Valid values are 0 to 9999, inclusive.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Acquisition Trace Offset |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxPulse Properties

<!--NI_TOPIC bundle=rfmxpulse-labview-api-ref path=resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01110.html language=enus -->
## TOPIC 00102: Pulse:Acquisition Trace:Subset Length

- bundle_id: `rfmxpulse-labview-api-ref`
- source_path: `resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01110.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc01110.html
- document_id: `rfmxpulse-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the total number of pulses starting from offset to be used for display acquisition trace. You must configure this property when you set the Pulse Acquisition Trace Select property to Subset. Set length to 0 to disable the acquisition trace. You do not need to use a selector string to confi

### Pulse:Acquisition Trace:Subset Length

Specifies the total number of pulses starting from offset to be used for display acquisition trace. You must configure this property when you set the [Pulse Acquisition Trace Select](/csh?topicname=attrc0110e.html) property to **Subset**.

Set length to 0 to disable the acquisition trace.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is 10. Valid values are 0 to 10000, inclusive.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Acquisition Trace Length |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxPulse Properties

<!--NI_TOPIC bundle=rfmxpulse-labview-api-ref path=resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0c000.html language=enus -->
## TOPIC 00103: Result Fetch Timeout (s)

- bundle_id: `rfmxpulse-labview-api-ref`
- source_path: `resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0c000.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxpulse-rc/rfmxpulse/attrc0c000.html
- document_id: `rfmxpulse-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the wait time before results are available in the RFmxPulse Property Node. This value is expressed in seconds. Set this value to a time longer than expected for fetching the measurement. A value of -1 specifies that the RFmxPulse Property Node waits until the measurement is complete. You d

### Result Fetch Timeout (s)

Specifies the wait time before results are available in the [RFmxPulse Property Node](/csh?context=rfmxpulse_rfmxpulsevi_rfmxpulse_property_node). This value is expressed in seconds.

Set this value to a time longer than expected for fetching the measurement. A value of -1 specifies that the RFmxPulse Property Node waits until the measurement is complete.

You do not need to use a [selector string](/csh?context=rfmxspecan_rfmxspecan_selector_string) to configure or read this property for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

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

RFmxPulse Properties

<!--NI_TOPIC bundle=rfmxpulse-labview-api-ref path=vi-lib/rfmx/pulse/mx/rfmxpulse-llb/rfmxpulse-abort-measurements-vi.html language=enus -->
## TOPIC 00104: RFmxPulse Abort Measurements VI

- bundle_id: `rfmxpulse-labview-api-ref`
- source_path: `vi-lib/rfmx/pulse/mx/rfmxpulse-llb/rfmxpulse-abort-measurements-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-labview-api-ref/raw/resource/enus/vi-lib/rfmx/pulse/mx/rfmxpulse-llb/rfmxpulse-abort-measurements-vi.html
- document_id: `rfmxpulse-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Stops acquisition and measurements associated with signal instance that you specify in the Selector String parameter, which were previously initiated by the RFmxPulse Initiate VI or measurement read VIs. Calling this VI is optional, unless you want to stop a measurement before it is complete. This V

### RFmxPulse Abort Measurements VI

Stops acquisition and measurements associated with signal instance that you specify in the **Selector String** parameter, which were previously initiated by the [RFmxPulse Initiate](/csh?topicname=rfmxpulse-initiate-vi.html) VI or measurement read VIs. Calling this VI is optional, unless you want to stop a measurement before it is complete. This VI executes even if there is an incoming error.

[IMAGE alt='icon' src='rfmxpulse-abort-measurements-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies the signal name and result name. The result name can either be specified through this input or the Result Name parameter. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name in this parameter, either the result name specified by the Result Name parameter or the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxpulse-labview-api-ref path=vi-lib/rfmx/pulse/mx/rfmxpulse-llb/rfmxpulse-analyze-iq-1-wfm-vi.html language=enus -->
## TOPIC 00105: RFmxPulse Analyze (IQ, 1 Wfm) VI

- bundle_id: `rfmxpulse-labview-api-ref`
- source_path: `vi-lib/rfmx/pulse/mx/rfmxpulse-llb/rfmxpulse-analyze-iq-1-wfm-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-labview-api-ref/raw/resource/enus/vi-lib/rfmx/pulse/mx/rfmxpulse-llb/rfmxpulse-analyze-iq-1-wfm-vi.html
- document_id: `rfmxpulse-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs the enabled measurements on the I/Q complex waveform that you specify in IQ parameter. Call this VI after you configure the signal and measurement properties. You can fetch measurement results using the Fetch VIs or result properties in the property node. Use this VI only if the Recommended

### RFmxPulse Analyze (IQ, 1 Wfm) VI

Performs the enabled measurements on the I/Q complex waveform that you specify in **IQ** parameter. Call this VI after you configure the signal and measurement properties. You can fetch measurement results using the Fetch VIs or result properties in the property node.
Use this VI only if the [Recommended Acquisition Type](/csh?context=rfmxinstr_rfmxinstrprop_attr27) property value is either **IQ** or **IQ or Spectral**.

Note

RFmxInstr Property Node

RFmx Pulse Commit

[IMAGE alt='icon' src='rfmxpulse-analyze-iq-1-wfm-vi.png']

#### Inputs/Outputs

| Result Name — Result Name specifies the name to be associated with measurement results. Provide a unique name, such as "r1" to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. The default value is "" (empty string) which refers to default result instance. Example: "result::r1" "r1" Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize VI with the option string as "AnalysisOnly=1". IQ — IQ specifies the data for a complex waveform including the start, delta, and actual values. x0 — x0 specifies the start time of the input y array. This value is expressed in seconds. dx — dx specifies the time interval between the samples in the input y array. This value is expressed in seconds. The reciprocal of dx indicates the I/Q rate of the input signal. y — y specifies an array of complex-valued time domain data. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively. Reset? — Reset? resets measurement averaging. If you enable averaging, set this parameter to TRUE for the first record and FALSE for the subsequent records. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. Selector String Out — Selector String Out returns the selector string that can be passed to the Selector String parameter on Fetch VIs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| x0 — x0 specifies the start time of the input y array. This value is expressed in seconds. dx — dx specifies the time interval between the samples in the input y array. This value is expressed in seconds. The reciprocal of dx indicates the I/Q rate of the input signal. y — y specifies an array of complex-valued time domain data. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively. |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxpulse-labview-api-ref path=vi-lib/rfmx/pulse/mx/rfmxpulse-llb/rfmxpulse-auto-level-vi.html language=enus -->
## TOPIC 00106: RFmxPulse Auto Level VI

- bundle_id: `rfmxpulse-labview-api-ref`
- source_path: `vi-lib/rfmx/pulse/mx/rfmxpulse-llb/rfmxpulse-auto-level-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-labview-api-ref/raw/resource/enus/vi-lib/rfmx/pulse/mx/rfmxpulse-llb/rfmxpulse-auto-level-vi.html
- document_id: `rfmxpulse-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Examines the input signal to calculate the peak power level and sets it as the value of the Reference Level property. Use this VI to help calculate an approximate setting for the reference level. The RFmxPulse Auto Level VI does the following: Resets the mixer level, mixer level offset and IF output

### RFmxPulse Auto Level VI

Examines the input signal to calculate the peak power level and sets it as the value of the [Reference Level](/csh?context=rfmxpulse_rfmxpulseprop_attrc00002) property. Use this VI to help calculate an approximate setting for the reference level.

The RFmxPulse Auto Level VI does the following:

1. Resets the mixer level, mixer level offset and IF output power offset.
2. Sets the starting reference level to the maximum reference level supported by the device based on the current RF attenuation, mechanical attenuation and preamp enabled settings.
3. Iterates to adjust the reference level based on the input signal peak power.
4. Uses immediate triggering and restores the trigger settings back to user setting after completing execution.

You can also specify the starting reference level using the [Auto Level Initial Reference Level](/csh?context=rfmxpulse_rfmxpulseprop_attrc0000d) property.

When using PXIe-5663, 5665, or 5668R devices, NI recommends that you set an appropriate value for mechanical attenuation before calling the RFmx Pulse Auto Level VI. Setting an appropriate value for mechanical attenuation reduces the number of times the attenuator settings are changed by this VI, thus reducing wear and tear, and maximizing the life time of the attenuator.

[IMAGE alt='icon' src='rfmxpulse-auto-level-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Bandwidth (Hz) — Bandwidth (Hz) specifies the bandwidth, in Hz, of the signal to be analyzed. The default value is 80 MHz. Measurement Interval (s) — Measurement Interval (s) specifies the acquisition length. Use this value to compute the number of samples to acquire from the signal analyzer. This value is expressed in seconds. The default value is 10 ms. Auto Level VI does not use any trigger for acquisition. It ignores the user-configured trigger properties. NI recommends that you set a sufficiently high measurement interval to ensure that the acquired waveform is at least as long as one period of the signal. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. Reference Level — Reference Level returns the estimated peak power level of the input signal. This value is expressed in dBm for RF devices and as Vpk-pk for baseband devices. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxpulse-labview-api-ref path=vi-lib/rfmx/pulse/mx/rfmxpulse-llb/rfmxpulse-check-measurement-status-vi.html language=enus -->
## TOPIC 00107: RFmxPulse Check Measurement Status VI

- bundle_id: `rfmxpulse-labview-api-ref`
- source_path: `vi-lib/rfmx/pulse/mx/rfmxpulse-llb/rfmxpulse-check-measurement-status-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-labview-api-ref/raw/resource/enus/vi-lib/rfmx/pulse/mx/rfmxpulse-llb/rfmxpulse-check-measurement-status-vi.html
- document_id: `rfmxpulse-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Checks the status of the measurement. Use this VI to check for any errors that may occur during measurement or to check whether the measurement is complete and results are available. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal nam

### RFmxPulse Check Measurement Status VI

Checks the status of the measurement. Use this VI to check for any errors that may occur during measurement or to check whether the measurement is complete and results are available.

[IMAGE alt='icon' src='rfmxpulse-check-measurement-status-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. done? — done? indicates whether the measurement is complete. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfmxpulse-labview-api-ref path=vi-lib/rfmx/pulse/mx/rfmxpulse-llb/rfmxpulse-clear-all-named-results-vi.html language=enus -->
## TOPIC 00108: RFmxPulse Clear All Named Results VI

- bundle_id: `rfmxpulse-labview-api-ref`
- source_path: `vi-lib/rfmx/pulse/mx/rfmxpulse-llb/rfmxpulse-clear-all-named-results-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-labview-api-ref/raw/resource/enus/vi-lib/rfmx/pulse/mx/rfmxpulse-llb/rfmxpulse-clear-all-named-results-vi.html
- document_id: `rfmxpulse-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Clears all results for the signal that you specify in the Selector String parameter. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value i

### RFmxPulse Clear All Named Results VI

Clears all results for the signal that you specify in the **Selector String** parameter.

[IMAGE alt='icon' src='rfmxpulse-clear-all-named-results-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxpulse-labview-api-ref path=vi-lib/rfmx/pulse/mx/rfmxpulse-llb/rfmxpulse-clone-signal-configuration-vi.html language=enus -->
## TOPIC 00109: RFmxPulse Clone Signal Configuration VI

- bundle_id: `rfmxpulse-labview-api-ref`
- source_path: `vi-lib/rfmx/pulse/mx/rfmxpulse-llb/rfmxpulse-clone-signal-configuration-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-labview-api-ref/raw/resource/enus/vi-lib/rfmx/pulse/mx/rfmxpulse-llb/rfmxpulse-clone-signal-configuration-vi.html
- document_id: `rfmxpulse-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a new instance of a signal by copying all the property values from an existing signal instance. icon Inputs/Outputs cstr.png Old Signal Name Old Signal Name specifies the name of an existing signal. This parameter accepts the signal name with or without the "signal::" prefix. Example: "signa

### RFmxPulse Clone Signal Configuration VI

Creates a new instance of a signal by copying all the property values from an existing signal instance.

[IMAGE alt='icon' src='rfmxpulse-clone-signal-configuration-vi.png']

#### Inputs/Outputs

| Old Signal Name — Old Signal Name specifies the name of an existing signal. This parameter accepts the signal name with or without the "signal::" prefix. Example: "signal::OldSigName" "OldSigName" Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. New Signal Name — New Signal Name specifies the name of the new signal. This parameter accepts the signal name with or without the "signal::" prefix. Example: "signal::NewSigName" "NewSigName" error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. Selector String Out — Selector String Out returns the selector string that can be passed to the Selector String parameter on Configure, Initiate, and Fetch VIs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxpulse-labview-api-ref path=vi-lib/rfmx/pulse/mx/rfmxpulse-llb/rfmxpulse-configure-digital-edge-trigger-vi.html language=enus -->
## TOPIC 00110: RFmxPulse Configure Digital Edge Trigger VI

- bundle_id: `rfmxpulse-labview-api-ref`
- source_path: `vi-lib/rfmx/pulse/mx/rfmxpulse-llb/rfmxpulse-configure-digital-edge-trigger-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-labview-api-ref/raw/resource/enus/vi-lib/rfmx/pulse/mx/rfmxpulse-llb/rfmxpulse-configure-digital-edge-trigger-vi.html
- document_id: `rfmxpulse-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the device to wait for a digital edge trigger and then marks a reference point within the record. icon Inputs/Outputs cbool.png Enable Trigger? Enable Trigger? specifies whether to enable the trigger. The default value is TRUE. cstr.png Selector String Selector String specifies a selector

### RFmxPulse Configure Digital Edge Trigger VI

Configures the device to wait for a digital edge trigger and then marks a reference point within the record.

[IMAGE alt='icon' src='rfmxpulse-configure-digital-edge-trigger-vi.png']

#### Inputs/Outputs

| Enable Trigger? — Enable Trigger? specifies whether to enable the trigger. The default value is TRUE. Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Digital Edge Source — Digital Edge Source specifies the source terminal for the digital edge trigger. The default of this property is hardware dependent. PFI0 (PFI0) The trigger is received on PFI 0. PFI1 (PFI1) The trigger is received on PFI 1. PXI_Trig0 (PXI_Trig0) The trigger is received on PXI trigger line 0. PXI_Trig1 (PXI_Trig1) The trigger is received on PXI trigger line 1. PXI_Trig2 (PXI_Trig2) The trigger is received on PXI trigger line 2. PXI_Trig3 (PXI_Trig3) The trigger is received on PXI trigger line 3. PXI_Trig4 (PXI_Trig4) The trigger is received on PXI trigger line 4. PXI_Trig5 (PXI_Trig5) The trigger is received on PXI trigger line 5. PXI_Trig6 (PXI_Trig6) The trigger is received on PXI trigger line 6. PXI_Trig7 (PXI_Trig7) The trigger is received on PXI trigger line 7. PXI_STAR (PXI_STAR) The trigger is received on the PXI star trigger line. PXIe_DStarB (PXIe_DStarB ) The trigger is received on the PXIe DStar B trigger line. TimerEvent (TimerEvent) The trigger is received from the timer event. Digital Edge — Digital Edge specifies the trigger edge to detect. The default value is Rising Edge. Rising Edge (0) The trigger asserts on the rising edge of the signal. Falling Edge (1) The trigger asserts on the falling edge of the signal. Trigger Delay (s) — Trigger Delay (s) specifies the trigger delay time, in seconds. The default value is 0. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
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
| PXIe_DStarB (PXIe_DStarB ) | The trigger is received on the PXIe DStar B trigger line. |
| TimerEvent (TimerEvent) | The trigger is received from the timer event. |
| Rising Edge (0) | The trigger asserts on the rising edge of the signal. |
| Falling Edge (1) | The trigger asserts on the falling edge of the signal. |

Parent topic:

RFmxPulse Configure Trigger VI

<!--NI_TOPIC bundle=rfmxpulse-labview-api-ref path=vi-lib/rfmx/pulse/mx/rfmxpulse-llb/rfmxpulse-configure-iq-power-edge-trigger-vi.html language=enus -->
## TOPIC 00111: RFmxPulse Configure IQ Power Edge Trigger VI

- bundle_id: `rfmxpulse-labview-api-ref`
- source_path: `vi-lib/rfmx/pulse/mx/rfmxpulse-llb/rfmxpulse-configure-iq-power-edge-trigger-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-labview-api-ref/raw/resource/enus/vi-lib/rfmx/pulse/mx/rfmxpulse-llb/rfmxpulse-configure-iq-power-edge-trigger-vi.html
- document_id: `rfmxpulse-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the device to wait for the complex power of the I/Q data to cross the specified threshold and then marks a reference point within the record. To trigger on bursty signals, specify a minimum quiet time, which ensures that the trigger does not occur in the middle of the burst signal. The qu

### RFmxPulse Configure IQ Power Edge Trigger VI

Configures the device to wait for the complex power of the I/Q data to cross the specified threshold and then marks a reference point within the record.

To trigger on bursty signals, specify a minimum quiet time, which ensures that the trigger does not occur in the middle of the burst signal. The quiet time must be set to a value smaller than the time between bursts, but large enough to ignore power changes within a burst.

[IMAGE alt='icon' src='rfmxpulse-configure-iq-power-edge-trigger-vi.png']

#### Inputs/Outputs

| Enable Trigger? — Enable Trigger? specifies whether to enable the trigger. The default value is TRUE. Trigger Delay (s) — Trigger Delay (s) specifies the trigger delay time, in seconds. The default value is 0. Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. IQ Power Edge Source — IQ Power Edge Source specifies the channel from which the device monitors the trigger. The default of this property is hardware dependent. IQ Power Edge Slope — IQ Power Edge Slope specifies whether the device asserts the trigger when the signal power is rising or when it is falling. The device asserts the trigger when the signal power exceeds the specified level with the slope you specify. The default value is Rising Slope. Rising Slope (0) The trigger asserts when the signal power is rising. Falling Slope (1) The trigger asserts when the signal power is falling. IQ Power Edge Level (dB or dBm) — IQ Power Edge Level (dB or dBm) specifies the power level at which the device triggers. This value is expressed in dB when you set the IQ Power Edge Level Type parameter to Relative and is expressed in dBm when you set the IQ Power Edge Level Type parameter to Absolute. The device asserts the trigger when the signal exceeds the level specified by the value of this parameter, taking into consideration the specified slope. The default of this property is hardware dependent. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Min Quiet Time Mode — Minimum Quiet Time Mode specifies whether the measurement computes the minimum quiet time used for triggering. The default value is Manual. Manual (0) The minimum quiet time used for triggering is the value of the Min Quiet Time parameter. Auto (1) The measurement computes the minimum quiet time used for triggering. Min Quiet Time (s) — Minimum Quiet Time (s) specifies the duration, in seconds, for which the signal must be quiet before the signal analyzer arms the I/Q Power Edge trigger. If you set the IQ Power Edge Slope parameter to Rising Slope, the signal is quiet when it is below the trigger level. If you set the IQ Power Edge Slope parameter to Falling Slope, the signal is quiet when it is above the trigger level. The default of this property is hardware dependent. IQ Power Edge Level Type — IQ Power Edge Level Type specifies the reference for the IQ Power Edge Level parameter. The default value is Absolute. Relative (0) The IQ Power Edge Level parameter is relative to the value of the Reference Level property. Absolute (1) The IQ Power Edge Level parameter specifies the absolute power. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Rising Slope (0) | The trigger asserts when the signal power is rising. |
| Falling Slope (1) | The trigger asserts when the signal power is falling. |
| Manual (0) | The minimum quiet time used for triggering is the value of the Min Quiet Time parameter. |
| Auto (1) | The measurement computes the minimum quiet time used for triggering. |
| Relative (0) | The IQ Power Edge Level parameter is relative to the value of the Reference Level property. |
| Absolute (1) | The IQ Power Edge Level parameter specifies the absolute power. |

Parent topic:

RFmxPulse Configure Trigger VI

<!--NI_TOPIC bundle=rfmxpulse-labview-api-ref path=vi-lib/rfmx/pulse/mx/rfmxpulse-llb/rfmxpulse-configure-reference-waveform-1-wfm-vi.html language=enus -->
## TOPIC 00112: RFmxPulse Configure Reference Waveform (1 Wfm) VI

- bundle_id: `rfmxpulse-labview-api-ref`
- source_path: `vi-lib/rfmx/pulse/mx/rfmxpulse-llb/rfmxpulse-configure-reference-waveform-1-wfm-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-labview-api-ref/raw/resource/enus/vi-lib/rfmx/pulse/mx/rfmxpulse-llb/rfmxpulse-configure-reference-waveform-1-wfm-vi.html
- document_id: `rfmxpulse-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the reference pulse waveform used for time sidelobe measurements. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (em

### RFmxPulse Configure Reference Waveform (1 Wfm) VI

Configures the reference pulse waveform used for time sidelobe measurements.

[IMAGE alt='icon' src='rfmxpulse-configure-reference-waveform-1-wfm-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Reference Waveform — Reference Waveform specifies the reference waveform used for correlation computation in time sidelobe Measurements. The default value is an empty waveform. x0 — x0 specifies the starting time of the reference waveform. This value is expressed in seconds. dx — dx specifies the sampling interval of the reference waveform. This value is expressed in seconds. y — y specifies an array of waveform samples of the reference waveform. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| x0 — x0 specifies the starting time of the reference waveform. This value is expressed in seconds. dx — dx specifies the sampling interval of the reference waveform. This value is expressed in seconds. y — y specifies an array of waveform samples of the reference waveform. |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxpulse-labview-api-ref path=vi-lib/rfmx/pulse/mx/rfmxpulse-llb/rfmxpulse-configure-trigger-vi.html language=enus -->
## TOPIC 00113: RFmxPulse Configure Trigger VI

- bundle_id: `rfmxpulse-labview-api-ref`
- source_path: `vi-lib/rfmx/pulse/mx/rfmxpulse-llb/rfmxpulse-configure-trigger-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-labview-api-ref/raw/resource/enus/vi-lib/rfmx/pulse/mx/rfmxpulse-llb/rfmxpulse-configure-trigger-vi.html
- document_id: `rfmxpulse-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the reference trigger to use to acquire the signal. icon

### RFmxPulse Configure Trigger VI

Configures the reference trigger to use to acquire the signal.

[IMAGE alt='icon' src='rfmxpulse-configure-trigger-vi.png']

- [RFmxPulse Disable Trigger VI](../../../../../vi-lib/rfmx/pulse/mx/rfmxpulse-llb/rfmxpulse-disable-trigger-vi.html) Configures the device to not wait for a trigger to mark a reference point within a record. This VI defines the signal triggering as immediate.
- [RFmxPulse Configure Digital Edge Trigger VI](../../../../../vi-lib/rfmx/pulse/mx/rfmxpulse-llb/rfmxpulse-configure-digital-edge-trigger-vi.html) Configures the device to wait for a digital edge trigger and then marks a reference point within the record.
- [RFmxPulse Configure IQ Power Edge Trigger VI](../../../../../vi-lib/rfmx/pulse/mx/rfmxpulse-llb/rfmxpulse-configure-iq-power-edge-trigger-vi.html) Configures the device to wait for the complex power of the I/Q data to cross the specified threshold and then marks a reference point within the record.
- [RFmxPulse Configure Software Edge Trigger VI](../../../../../vi-lib/rfmx/pulse/mx/rfmxpulse-llb/rfmxpulse-configure-software-edge-trigger-vi.html) Configures the device to wait for a software trigger and then marks a reference point within the record.

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxpulse-labview-api-ref path=vi-lib/rfmx/pulse/mx/rfmxpulse-llb/rfmxpulse-create-signal-configuration-vi.html language=enus -->
## TOPIC 00114: RFmxPulse Create Signal Configuration VI

- bundle_id: `rfmxpulse-labview-api-ref`
- source_path: `vi-lib/rfmx/pulse/mx/rfmxpulse-llb/rfmxpulse-create-signal-configuration-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-labview-api-ref/raw/resource/enus/vi-lib/rfmx/pulse/mx/rfmxpulse-llb/rfmxpulse-create-signal-configuration-vi.html
- document_id: `rfmxpulse-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a new instance of a signal. icon Inputs/Outputs cstr.png Signal Name Signal Name specifies the name of the signal. This parameter accepts the signal name with or without the "signal::" prefix. Example: "signal::s1" "sig1" cgenclassrntag.png Instrument Handle In Instrument Handle In specifies

### RFmxPulse Create Signal Configuration VI

Creates a new instance of a signal.

[IMAGE alt='icon' src='rfmxpulse-create-signal-configuration-vi.png']

#### Inputs/Outputs

| Signal Name — Signal Name specifies the name of the signal. This parameter accepts the signal name with or without the "signal::" prefix. Example: "signal::s1" "sig1" Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. Selector String Out — Selector String Out returns the selector string that can be passed to the Selector String parameter on Configure, Initiate, and Fetch VIs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxpulse-labview-api-ref path=vi-lib/rfmx/pulse/mx/rfmxpulse-llb/rfmxpulse-delete-signal-configuration-vi.html language=enus -->
## TOPIC 00115: RFmxPulse Delete Signal Configuration VI

- bundle_id: `rfmxpulse-labview-api-ref`
- source_path: `vi-lib/rfmx/pulse/mx/rfmxpulse-llb/rfmxpulse-delete-signal-configuration-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-labview-api-ref/raw/resource/enus/vi-lib/rfmx/pulse/mx/rfmxpulse-llb/rfmxpulse-delete-signal-configuration-vi.html
- document_id: `rfmxpulse-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Deletes an instance of a signal that you specify in the Signal Name parameter. icon Inputs/Outputs cstr.png Signal Name Signal Name specifies the name of the signal. This parameter accepts the signal name with or without the "signal::" prefix. Example: "signal::s1" "sig1" cgenclassrntag.png Instrume

### RFmxPulse Delete Signal Configuration VI

Deletes an instance of a signal that you specify in the **Signal Name** parameter.

[IMAGE alt='icon' src='rfmxpulse-delete-signal-configuration-vi.png']

#### Inputs/Outputs

| Signal Name — Signal Name specifies the name of the signal. This parameter accepts the signal name with or without the "signal::" prefix. Example: "signal::s1" "sig1" Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxpulse-labview-api-ref path=vi-lib/rfmx/pulse/mx/rfmxpulse-llb/rfmxpulse-fetch-acquired-amplitude-trace-vi.html language=enus -->
## TOPIC 00116: RFmxPulse Fetch Acquired Amplitude Trace VI

- bundle_id: `rfmxpulse-labview-api-ref`
- source_path: `vi-lib/rfmx/pulse/mx/rfmxpulse-llb/rfmxpulse-fetch-acquired-amplitude-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-labview-api-ref/raw/resource/enus/vi-lib/rfmx/pulse/mx/rfmxpulse-llb/rfmxpulse-fetch-acquired-amplitude-trace-vi.html
- document_id: `rfmxpulse-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the acquired amplitude trace in the measurement, where the Amplitude array forms the y-axis of the trace. You can use the Pulse Acquisition Trace Select property to select all pulses or the subset of acquired pulses. When you set the Segmented Acquisition Enabled property to False, returns a

### RFmxPulse Fetch Acquired Amplitude Trace VI

Fetches the acquired amplitude trace in the measurement, where the Amplitude array forms the y-axis of the trace. You can use the [Pulse Acquisition Trace Select](/csh?topicname=attrc0110e.html) property to select all pulses or the subset of acquired pulses. When you set the [Segmented Acquisition Enabled](/csh?topicname=attrc00014.html) property to **False**, returns a single element in the Start Indices and Start Time Stamp array.

[IMAGE alt='icon' src='rfmxpulse-fetch-acquired-amplitude-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout (s) specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Sample Duration (s) — Sample Duration (s) returns the sample duration, in seconds. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. Amplitude — Amplitude returns the trace of amplitude measured in units specified by Amplitude Trace Unit property. Start Index — Start Index returns the array of sample indices for the start of each segment. Start Time Stamp (s) — Start Time Stamp (s) returns the array of timestamps of each segment start, in seconds. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxPulse Fetch VI

<!--NI_TOPIC bundle=rfmxpulse-labview-api-ref path=vi-lib/rfmx/pulse/mx/rfmxpulse-llb/standard-functionality-for-error-in-parameters.html language=enus -->
## TOPIC 00117: Using the Standard Functionality for error in Parameters

- bundle_id: `rfmxpulse-labview-api-ref`
- source_path: `vi-lib/rfmx/pulse/mx/rfmxpulse-llb/standard-functionality-for-error-in-parameters.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-labview-api-ref/raw/resource/enus/vi-lib/rfmx/pulse/mx/rfmxpulse-llb/standard-functionality-for-error-in-parameters.html
- document_id: `rfmxpulse-labview-api-ref`
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

<!--NI_TOPIC bundle=rfmxpulse-labview-api-ref path=vi-lib/rfmx/pulse/mx/rfmxpulse-llb/standard-functionality-for-error-out-parameters.html language=enus -->
## TOPIC 00118: Using the Standard Functionality for error out Parameters

- bundle_id: `rfmxpulse-labview-api-ref`
- source_path: `vi-lib/rfmx/pulse/mx/rfmxpulse-llb/standard-functionality-for-error-out-parameters.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-labview-api-ref/raw/resource/enus/vi-lib/rfmx/pulse/mx/rfmxpulse-llb/standard-functionality-for-error-out-parameters.html
- document_id: `rfmxpulse-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Many LabVIEW nodes such as VIs contain an error out parameter you can use to manage errors. These parameters typically provide the same, standard functionality. When a node exhibits different parameter functionality, the exceptions are documented in the reference material for that node. Standard err

### Using the Standard Functionality for error out Parameters

Many LabVIEW nodes such as VIs contain an error out parameter you can use to manage errors. These parameters typically provide the same, standard functionality. When a node exhibits different parameter functionality, the exceptions are documented in the reference material for that node.

Standard error out functionality is as follows:

|  | error out contains error information. If error in indicates that an error occurred before this VI ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- | --- |

error out contains the following cluster elements:

|  | status is TRUE (X) if an error occurred before this node ran or during the running of this node or FALSE (checkmark) to indicate a warning or that no error occurred before this node ran or during the running of this node. |
| --- | --- |
|  | code is the error or warning code. If status is TRUE, code is an error code. If status is FALSE, code is 0 or a warning code. |
|  | source specifies the origin of the error or warning and is, in most cases, the name of the node that produced the error or warning. |
