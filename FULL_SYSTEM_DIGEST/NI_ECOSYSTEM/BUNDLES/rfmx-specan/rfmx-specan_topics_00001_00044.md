# NI DOCUMENT BUNDLE: rfmx-specan

<!--NI_BUNDLE_CHUNK bundle=rfmx-specan start=1 end=44 -->
<!--NI_TOPIC bundle=rfmx-specan path=acp.html language=enus -->
## TOPIC 00001: ACP

- bundle_id: `rfmx-specan`
- source_path: `acp.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan/raw/resource/enus/acp.html
- document_id: `rfmx-specan`
- page_type: `leaf`
- content_type: `concept`
- source_description: Adjacent channel power (ACP) measurement measures the power leakage from the carrier channels into the neighboring frequency channels, commonly referred to as offset channels. The following figure shows a typical carrier channel and offset channel configuration. Carrier Channels Carriers are channel

### ACP

Adjacent channel power (ACP) measurement measures the power leakage from the carrier
 channels into the neighboring frequency channels, commonly referred to as offset
 channels. The following figure shows a typical carrier channel and offset channel
 configuration.

[IMAGE alt='image' src='GUID-6B279466-7DC2-4C92-86A8-7DD49CBE9244-a5.gif']

#### Carrier Channels

Carriers are channels in which significant power is transmitted, and for which power
 leakage in the offset channels is measured. Multiple carriers are configured relative to
 the RF center frequency by specifying the carrier offset, integration bandwidth (IBW),
 and root raised cosine (RRC) channel filter. Power in each carrier is measured by
 integrating the power in the specified IBW after applying the channel filter. The total
 carrier power measured is the aggregate power of all the active carriers. To exclude a
 carrier in the total carrier power, set the carrier to passive mode.

#### Offset Channels

Offset channel center frequency is specified relative to the center frequency of the
 closest carrier. The placement of offset channels from the nearest carrier is defined by
 the ACP offset frequency definition.

Offset Frequency Definition

The frequency offset of the offset channels from the closest carrier is defined by the
 ACP offset frequency definition. The offset frequency definition defines the offset
 frequency in one of the following ways:

- Carrier Center to Offset Center —The offset frequency is
 defined from the center of the closest carrier to the center of the offset
 channel.
- Carrier Center to Offset Edge —The offset frequency is defined
 from the center of the closest carrier to the nearest edge of the offset
 channel.

The following image describes the offset frequency definitions:

[IMAGE alt='image' src='GUID-2CCE5031-8AC6-4A76-ADF4-2E272BAAD159-a5.png']

Offset Sideband

Two offset channels are configured on either side of the carriers when you set the offset
 sideband to BOTH. Only one offset channel is configured when you set the sideband to
 either positive (POS) or negative (NEG). A negative sideband creates a lower offset
 channel to the left of the leftmost carrier. A positive sideband creates an upper offset
 channel to the right of the rightmost carrier. You can independently configure the IBW,
 RRC filter, power reference, and relative attenuation for each offset channel.

Power Reference

Power reference refers to the carrier channel relative to which the offset channel power
 is measured. The power reference is one of the following carriers:

- Closest carrier —Power in the carrier with center frequency
 closest to the offset channel center frequency
- Highest carrier power —Highest power among all the ACTIVE
 carriers
- Composite carrier —Total power of all the ACTIVE carriers
- Specific carrier —Power in the carrier specified by the
 carrier index

Note

Note

#### RBW and Sweep Time

When you set the ACP RBW Auto to True, the measurement sets the
 RBW using the following ratio:

Min (Carrier IBW, Offset Channel IBW):RBW<sub>3dB</sub> = 100, where
 RBW<sub>3dB</sub> is a value between 1 Hz and 1 MHz

When you set the ACP Sweep Time Auto to True, the measurement sets
 the sweep time to the following values:

- k/RBW 3dB when the RBW filter is FFT based, where k is
 a constant which depends on the FFT window
- 10/RBW 3dB for other RBW filter types

#### Power Measurement

Power Units

The absolute power values measured are reported in dBm (integrated power) or dBm/Hz
 (power spectral density). The relative power values are not affected by the units
 specified. Use relative attenuation to compensate for external attenuation for each
 offset channel.

Measurement Method

ACP measurement supports two measurement methods based on the requirement of measurement
 speed and dynamic range.

When you set the measurement method to Normal, the measurement acquires the signal using
 a wideband front-end filter. This measurement acquires the spectrum with a large span
 and perform FFT-based processing.

The following steps help improve the dynamic range of the measurement:

- The RF input attenuation must be set such that the mixer operates at optimal
 operating level. Refer to the dynamic range chart of the device to know the optimum
 mixer level. Mixer Level = Reference Level -
 RF Attenuation
- The reference level must be adjusted to the power level of the test signal. Doing so
 sets the signal at the A/D converter (ADC) to full scale, which results in the best
 SNR and SFDR performance.
- Narrowband spectrum analysis mode allows dynamic range beyond that of the ADC.
- Re-ranging the reference level when measuring the distortion amplitude allows the
 best dynamic range.

When you set the measurement method to Dynamic Range, the measurement uses hardware
 features, such as the IF filter and IF gain. The measurement acquires the signal using
 narrowband IF filters available on the analyzer. Analog IF filters used for each offset
 channel may vary based on the device in use. Narrow bandwidth IF filters are used to
 acquire a spectrum closer to the carrier channel to filter out the high power seen from
 the carrier in the adjacent channels. A wideband IF filter is used to acquire a spectrum
 farther from the carrier to reduce measurement time. The carrier channels are not
 filtered.

The measurement resets the ranges for each offset channel based on the reference level
 set for the measurement and the analog IF filters to increase the power seen by the ADC
 of the digitizer.

Note

| Supported Analyzer | IF Filters | Max RBW |
| --- | --- | --- |
| PXIe-5665 (3.6 GHz) | 300 kHz | 300 kHz |
| PXIe-5665 (14 GHz) | 300 kHz, 5 MHz | 300 kHz |
| PXIe-5668 | 300 kHz, 5 MHz | 300 kHz |

Note

#### Noise Compensation

Noise compensation enables the measurement of the inherent noise floor of the signal
 analyzer for the RF path used by the measurement, and uses this result to compensate the
 signal measurement. For a given set of measurement configurations and the state of the
 signal analyzer, noise floors are constant. Because measuring the noise floor adds to
 the measurement time, the noise floor results are cached so that the measurement can use
 it later. When the signal analyzer or measurement parameters change, the noise floor
 measurement is reinitiated to return valid measurements.

Note

Note

Related concepts:

- Spectral Measurements Concepts

<!--NI_TOPIC bundle=rfmx-specan path=ampm.html language=enus -->
## TOPIC 00002: AMPM

- bundle_id: `rfmx-specan`
- source_path: `ampm.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan/raw/resource/enus/ampm.html
- document_id: `rfmx-specan`
- page_type: `leaf`
- content_type: `concept`
- source_description: The AMPM measurement requires Power Amplifier license activation. If you install RFmx SpecAn but do not activate the Power Amplifier license, you will have 30 days from the first time you use the measurement to evaluate it. One of the fundamental assumptions in the study and design of signal process

### AMPM

Note

One of the fundamental assumptions in the study and design of signal processing and
 communication systems is that the systems under investigation are more or less linear. While
 the linearity assumption holds in digital subsystems, the response of analog subsystems can
 only be treated as being approximately linear over a certain range of input power or frequency
 band.

An example of a nonlinear subsystem used in the ubiquitous wireless communication systems is
 a power amplifier (PA). While the overall response of the PA is clearly nonlinear, many
 applications where the region of operation is limited to a relatively linear portion of the PA
 response do not face any serious problem because of the nonlinear nature of the PA. This
 limitation is true for cellular standards such as GSM or EDGE.

The following figure shows the typical input-output response of a PA.

[IMAGE alt='image' src='GUID-C8BACEF7-7F00-4551-A826-D5C6673559F6-a5.png']

With the rapid migration of cellular and connectivity technologies towards multicarrier
 modulation schemes, such as HSPA+, LTE-Advanced and IEEE 802.11ac in which the RF envelope
 fluctuations vary from 6 dB to 12 dB relative to the average signal power, it has become
 impractical to back-off the operating point to continue to operate the PA in a relatively
 linear region because operating efficiency of PAs diminishes as the operating point is
 backed-off. Technologies such as envelope tracking and digital predistortion have been
 developed to linearize power amplifier response without resorting to power back-off and thus
 continue to operate the PA in a high-efficiency mode.

The AMPM measurement in RFmx characterizes the instantaneous gain applied to the input
 signal and instantaneous phase distortion observed in signal at the device under test (DUT)
 output with respect to the instantaneous power of the input signal. The instantaneous gain
 versus signal power characteristic of the DUT is referred to as AM to AM (AMAM) profile, and
 the instantaneous phase distortion versus signal power characteristic of the DUT is referred
 to as the AM to PM (AMPM) profile of the DUT.

The following figure shows the typical AMAM response of a PA.

[IMAGE alt='image' src='GUID-A0FF91FA-8E7B-40F4-921E-88E46AB8B7DF-a5.png']

The following figure shows the typical AMPM response of a PA.

[IMAGE alt='image' src='GUID-AB999D5B-93E1-4F04-A6B4-2125B4800FBD-a5.png']

AMAM and AMPM traces are useful to characterize and visualize the nonlinear nature of the
 DUT. Some memoryless predistortion techniques can use the AMAM and AMPM traces to linearize
 the DUT response.

#### Recommended Settings

The following settings are recommended for AMPM measurements:

Sample Rate

The minimum recommended sample rate, expressed in samples per second, is given by:

[IMAGE alt='image' src='GUID-85B77250-3ACE-4187-AABC-45736CE4AB0B-a5.gif']

where, B is the bandwidth of the signal in Hz and K is the highest significant order of PA
 non-linearity.

Synchronization Method

For computing the gain and phase characteristics of the DUT, AMPM measurement requires
 reliable time-synchronization between the acquired and reference waveforms.

AMPM measurement provides two synchronization methods, Direct and Alias Protected.

Direct

This method synchronizes the acquired and reference waveforms with the assumption that the
 sample rate is high enough for preventing aliasing in intermediate nonlinear operations during
 the estimation of subsample delay between the two waveforms.

Alias Protected

This method synchronizes the acquired and reference waveforms while also ensuring that
 intermediate nonlinear operations during the estimation of sub-sample delay between the two
 waveforms are not affected by aliasing. This synchronization method should be used for the
 following test configurations:

- signal is either single-carrier or contiguous multi-carrier, and measurement sample rate
 is less than approximately three times the occupied-bandwidth.
- signal is non-contiguous multi-carrier and the component carriers are sparsely allocated
 in frequency.

This method uses the offset and bandwidth information of all component carriers comprising
 the signal. If you set the AMPM Auto Carrier Detection Enabled property to
 True, the measurement auto detects the carrier offsets and
 bandwidths. If you set the AMPM Auto Carrier Detection Enabled property to
 False, you must configure the carrier offsets and bandwidths by
 setting the AMPM Number of Carriers, AMPM Carrier Offset, and AMPM Carrier Bandwidth
 properties.

The following diagram illustrates the offsets and bandwidths of the component carriers in a
 multi-carrier signal with a sample rate of
 F<sub>S</sub>(S/s), expressed in
 samples per second.

[IMAGE alt='image' src='GUID-6A7A76DA-A44F-4C7B-A6AC-A406CAB636BA-a5.png']

Threshold

Use appropriate threshold settings to reject low power noise corrupted samples. The default
 threshold is set to -20 dB relative to the peak power of the acquired waveform.

Equalization

Enable the equalizer filter to compensate for the effect of the channel. Equalization helps
 compensate for heterogeneous group delays in component carriers and is particularly useful for
 non-contiguous multi-carrier signals where the component carriers are sparsely allocated in
 frequency.

Recommended Settings for Faster Speed

- AMPM measurement corrects for impairments such as the frequency and origin offset between
 the acquired and the reference waveform. However, when the test setup ensures that these
 impairments are absent, these corrections can be disabled for speed if you set the AMPM
 Freq Offset Correction Enabled and the AMPM IQ Origin Offset Correction Enabled properties
 to False .
- AMPM measurement allows disabling of one or more results for faster speed. 
 If you set the AMPM AM to AM Enabled property to False, the
 measurement skips the computation of results that rely on the AM to AM
 characteristics. 
 The following scalar results are disabled: 
 
 The following traces are disabled: 
 
 Similarly, if you set the AMPM AM to PM Enabled property to False,
 the measurement skips the computation of results that rely on the AM to PM
 characteristics. 
 The following scalar results are disabled: 
 
 The following traces are disabled:
  - AMPM Results Mean Linear Gain
  - AMPM Results 1 dB Compression Point
  - AMPM Results Input Compression Point
  - AMPM Results Output Compression Point
  - AMPM Results Gain Error Range
  - AMPM Results AM to AM Curve Fit Residual
  - AMPM Results AM to AM Curve Fit Coeff
  - Measured AM to AM (dB)
  - Curve Fit AM to AM (dB)
  - Relative Power Trace (dB)
  - AMPM Results Mean Phase Error
  - AMPM Results Phase Error Range
  - AMPM Results AM to PM Curve Fit Residual
  - AMPM Results AM to PM Curve Fit Coeff
  - Measured AM to PM (deg)
  - Curve Fit AM to PM (deg)
  - Relative Phase Trace (deg)
- EVM computation can be skipped if you set the AMPM EVM Enabled property to
 False .
- AMPM traces can be disabled for faster speed when you set the AMPM All Traces Enabled
 property to FALSE.

<!--NI_TOPIC bundle=rfmx-specan path=averaging.html language=enus -->
## TOPIC 00003: Averaging

- bundle_id: `rfmx-specan`
- source_path: `averaging.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan/raw/resource/enus/averaging.html
- document_id: `rfmx-specan`
- page_type: `leaf`
- content_type: `concept`
- source_description: Power Measurements Averaging helps in improving the accuracy of power measurements of stationary signals. The spectrum is averaged over multiple acquisitions based on the averaging count. This helps in reducing noise in the acquired signal based on the averaging type. The following table lists the s

### Averaging

#### Power Measurements

Averaging helps in improving the accuracy of power measurements of stationary signals.
 The spectrum is averaged over multiple acquisitions based on the averaging count. This
 helps in reducing noise in the acquired signal based on the averaging type.

The following table lists the supported averaging types for traces.

| Type | Formula | Application |
| --- | --- | --- |
| RMS | where, P = averaged power trace in Watts pm = iteration power trace in Watts M = number of iterations | To reduce the effect of phase noise |
| Log |  | To distinguish low power continuous wave signals from noise |
| Scalar |  | Field measurements |
| Max |  | To observe transient effects in spectrum |
| Min |  | To observe transient effects in spectrum |
| Vector | where, | To reduce noise (non phase coherent signals) in a synchronous signal. The acquisitions must be triggered to synchronize the signal. |

#### Other Measurements

The following table lists the supported averaging types for results.

| Type | Formula |
| --- | --- |
| Mean | where, |
| Max |  |
| Min |  |
| Min Max | The sign of V corresponds to the actual sample. |

<!--NI_TOPIC bundle=rfmx-specan path=ccdf.html language=enus -->
## TOPIC 00004: Complementary Cumulative Distribution Function (CCDF)

- bundle_id: `rfmx-specan`
- source_path: `ccdf.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan/raw/resource/enus/ccdf.html
- document_id: `rfmx-specan`
- page_type: `leaf`
- content_type: `concept`
- source_description: The CCDF measurement estimates the CCDF of the random variable as defined by the following equation: where The following equation defines the CCDF of . where Pr {e} denotes the probability of the event e. This equation can be interpreted in logarithmic scale as the probability of the event that inst

### Complementary Cumulative Distribution Function
 (CCDF)

The CCDF measurement estimates the CCDF of the random variable [IMAGE alt='image' src='GUID-121DF2E7-993B-43FA-8212-95F6F2DE29F7-a5.png'] as defined
 by the following equation:

[IMAGE alt='image' src='GUID-49F1A0CA-F9C7-4133-801B-4358C0D4D811-a5.png']

where

[IMAGE alt='image' src='GUID-BEADDEBC-E181-4D04-8DD4-DA43C7087764-a5.png']

The following equation defines the CCDF of [IMAGE alt='image' src='GUID-121DF2E7-993B-43FA-8212-95F6F2DE29F7-a5.png'].

[IMAGE alt='image' src='GUID-7A2DEE99-9721-4C64-863D-8E64C2A2B0CB-a5.png']

where Pr {e} denotes the probability of the event
 e.

This equation can be interpreted in logarithmic scale as the probability of the event that
 instantaneous signal power exceeds the mean power by at least X dB.

The following list describes the basic properties that you can configure for a CCDF
 measurement:

- RBW: Configure RBW to specify the 3 dB bandwidth over which time domain
 signal needs to be analyzed. Ensure that RBW does not exceed the
 instantaneous bandwidth of the signal analyzer. NI recommends that you use
 no filter or a flat RBW filter. Refer to the Zero Span section of the
 Spectrum topic for information on the sample rate required by
 the measurement.
- Measurement Interval and Number of Records :
 Configure such that the number of samples analyzed by the measurement are enough to get
 sufficient accuracy in the statistical data reported.
- Threshold: While analyzing signals with dead time, NI recommends to
 specify a threshold such that only the samples with instantaneous power
 above this threshold are considered for the measurement.

#### Probabilities Measurement

Mean power is the linear average of the power of all samples considered for the measurement.
 When threshold is enabled, only the samples above the threshold are considered. Mean power
 percentile represents the percentage of samples for which the amplitude is above the mean
 signal power.

The power, which is relative to the mean power, of 10%, 1%, 0.1%, 0.01%, 0.001%, and 0.0001%
 of the samples above the mean power is measured. These results help you select the headroom
 power to be set on the transmitter such that a major portion of the signal is generated with
 high power without distortion and with only a small percentage of the samples being
 clipped.

The measurement returns a probabilities trace, which is also called CCDF trace, on which you can
 interpret any point as follows:

x is the power, in dB, relative to the mean signal power

y is the probability, as a percentage, that any sample in the acquired signal
 exceeds the mean power by at least x

The CCDF of the power of a complex Gaussian random variable is often used as the reference
 for comparing the power distribution in the signal under analysis.

The following figure shows the CCDF curve of a QAM 4096 signal.

[IMAGE alt='image' src='GUID-5E17FA4E-A66D-4440-BEC8-B34CAAA0A096-a5.png']

Related concepts:

- Spectrum

<!--NI_TOPIC bundle=rfmx-specan path=chp.html language=enus -->
## TOPIC 00005: CHP

- bundle_id: `rfmx-specan`
- source_path: `chp.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan/raw/resource/enus/chp.html
- document_id: `rfmx-specan`
- page_type: `leaf`
- content_type: `concept`
- source_description: Channel power (CHP) measures the RMS power in the carrier channel. The spectrum is configured for span, RBW, sweep time, and carrier channels. The channel filter is applied after RBW filtering and averaging, and it affects the measured power. The power units specify whether to report the integrated

### CHP

Channel power (CHP) measures the RMS power in the carrier channel. The spectrum is
 configured for span, RBW, sweep time, and carrier channels. The channel filter is
 applied after RBW filtering and averaging, and it affects the measured power. The power
 units specify whether to report the integrated power or the power spectral density of
 the channel.

The following figure shows the spectrum span and integration bandwidth. [IMAGE alt='image' src='GUID-32060897-75B2-431B-8574-A20F62FDB4B7-a5.png']

#### Carrier Channels

Carriers are channels in which significant power is transmitted. You can configure
 multiple carriers relative to the RF center frequency by specifying the carrier offset,
 integration bandwidth (IBW), and root raised cosine (RRC) channel filter. Power in each
 carrier is measured by integrating the power in the specified IBW after applying the
 channel filter. The total carrier power measured is the aggregate power of all the
 carriers.

#### RBW and Sweep Time

When you set the CHP RBW Auto property to True, the measurement
 sets the RBW using the following ratio:

IBW:RBW<sub>3dB</sub> = 100, where RBW<sub>3dB</sub> is a value
 between 1 Hz and 1 MHz

When you set the CHP Sweep Time Auto property to True, the
 measurement sets the sweep time to the following values:

- k/RBW 3dB when the RBW filter is FFT based, where k is
 a constant which depends on the FFT window
- 10/RBW 3dB for other RBW filter types

|  | Note The standard specific CHP measurement does not support configuring all the properties and fetching all the results mentioned in this topic. The standard-specific measurements do not expose some properties with settings that are specified by the standard or are not relevant to the standard. |
| --- | --- |

Related concepts:

- Spectral Measurements Concepts

<!--NI_TOPIC bundle=rfmx-specan path=crest-factor-reduction.html language=enus -->
## TOPIC 00006: Crest Factor Reduction

- bundle_id: `rfmx-specan`
- source_path: `crest-factor-reduction.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan/raw/resource/enus/crest-factor-reduction.html
- document_id: `rfmx-specan`
- page_type: `leaf`
- content_type: `concept`
- source_description: Crest Factor Reduction (CFR) is a technique to reduce the peak to average power ratio (PAPR) of a waveform to a desired value. CFR techniques can be used in conjunction with DPD to improve the overall linearization of the system ^[4]. Pre-DPD Signal Conditioning For highly non-linear power amplifier

### Crest Factor Reduction

Crest Factor Reduction (CFR) is a technique to reduce the peak to average power ratio
 (PAPR) of a waveform to a desired value. CFR techniques can be used in conjunction with
 DPD to improve the overall linearization of the system <sup>[4]</sup>.

#### Pre-DPD Signal Conditioning

For highly non-linear power amplifiers, the peaks in the signal input to the PA
 experience significant gain compression. As a result,

1. the PA transfer function is ill-conditioned for converging to a satisfactory inverse
 transfer function. Therefore, the quality of predistorter, as indicated by a high
 value of the normalized mean squared error (NMSE), is poor, and
2. the computed predistorter often increases the PAPR of the waveform to restore the
 peaks that are almost saturated by the PA. Extremely high PAPR of the pre-DPD
 waveform further worsens the performance of the PA; very high input peak powers may
 even damage PA circuitry.

CFR can be applied on the reference waveform to reduce the signal peak levels such that
 the obtained PA transfer function can be inverted effectively by the selected DPD
 model.

#### CFR on Predistorted Waveform

CFR can be applied to the pre-distorted waveform to limit the peak input power to the PA
 after applying DPD <sup>[5]</sup>.

#### CFR Methods

DPD measurement supports three CFR methods namely Clipping,
 Peak Windowing and Sigmoid.

Clipping

This method hard clips the signal to achieve the target PAPR set by you. The following
 figure shows how the PAPR of a signal can be reduced by using
 Clipping.

[IMAGE alt='image' src='GUID-B7DFA43C-F7F9-4460-9F05-1FDB4FE0F4E4-a5.png']

Clipping operation can be expressed as:

[IMAGE alt='image' src='GUID-8B5D8C68-4C7F-4B58-99D8-0571A24E9CBF-a5.gif']

where,

x[n] is the signal on which CFR is applied.

x<sub>clipping</sub>[n] is the clipped signal.

A is the threshold level determined by target PAPR.

The Clipping transfer function is represented by the following figure.

[IMAGE alt='image' src='GUID-2A6D15CB-D183-4204-9784-D5FC2F948FEF-a5.png']

Peak Windowing

Peak Windowing is a CFR method that scales the peaks in signal using a weighted window
 function to get smooth peaks and achieve the target PAPR. This technique involves the
 following steps:

1. Detect peaks above the threshold, A, determined by the target PAPR. Samples above
 the threshold, in the vicinity of the detected peaks are referred to as the ‘peak
 region’.
2. Scale all the peak regions with a weighted window function such that the resultant
 peaks are equal to the threshold level, A. The window type and maximum window length
 are user configurable.

The following figure shows the input signal, the threshold level, and the signal obtained
 after applying the Peak Windowing method of CFR.

[IMAGE alt='image' src='GUID-2D8C7A40-BE00-45B3-813C-B9972D47C06B-a5.png']

Sigmoid

This CFR method scales the peaks using modified sigmoid transfer function to get smooth
 peaks and achieve target PAPR. The following figure shows the input signal, the
 threshold level, and the signal obtained after applying the Sigmoid method of CFR.

[IMAGE alt='image' src='GUID-2A689B99-40AE-46B9-8158-34A269B4C2BC-a5.png']

Sigmoid method follows the relation shown below.

[IMAGE alt='image' src='GUID-68F0AB95-DCB4-46BE-9022-3DE6750F82AA-a5.gif']

where,

A is clipping threshold, determined by target PAPR.

Δ is the shaping threshold which defines the minimum signal level, A/Δ, above which
 sigmoid function starts to impact the signal to be clipped.

K is the shaping factor which controls the smoothness of the modified sigmoid transfer
 function

Shaping threshold and shaping factor are user configurable.

The following figure shows the transfer function of Sigmoid method for various values of
 the shaping factor, K.

[IMAGE alt='image' src='GUID-0764BA51-9DE0-4B03-82A3-2AF2B0ED602C-a5.png']

CFR with Filtering for Pre-DPD Signal Conditioning

CFR is a non-linear operation that introduces out-of-band distortion in the signal. This
 distortion can be filtered out after the CFR operation <sup>[6]</sup>.

CFR with filter can be applied on the reference waveform by enabling filter and
 specifying the carrier offsets and carrier bandwidths. The block diagram below shows one
 iteration of CFR operation with filtering. The waveform x<sub>CFR+Filter</sub>[n] is
 used as the Reference Waveform by the DPD measurement.

[IMAGE alt='image' src='GUID-59735C3F-BD88-4385-83CB-B358111CE79B-a5.png']

The diagram below shows an example of carrier offsets and bandwidths configuration for a
 signal sampled at S samples per second.

[IMAGE alt='image' src='GUID-E4A3F3FB-7CEB-434D-B4C3-7FCFE86CD651-a5.png']

1. CFR with filter is not supported when CFR method is set to Sigmoid.
2. CFR with filter is not supported for pre-distorted waveform.

Guidelines for Using CFR

CFR can be a useful technique for improved linearization of the Predistorter + PA System,
 especially when operating under very high compression region of the PA.

The configured target PAPR should follow the relation below.

[IMAGE alt='image' src='GUID-4382FEA6-78B7-4869-8F10-2BB7A4938547-a5.gif']

where,

P<sub>out</sub> is the desired average output power from the PA in dB.

P<sub>XdB</sub> is the peak output power from the PA, in dBm, where the compressed gain
 is X dB below the ideal gain. Typically, X is 1 or 3 dB.

The target PAPR can be lowered gradually until the desired performance metrics like
 adjacent channel power (ACP), and error vector magnitude (EVM) are met.

| CFR Method | Usage |
| --- | --- |
| Clipping | For measurement speed Trade-off ACP for EVM. |
| Peak Windowing | Trade-off between ACP and EVM. |
| Sigmoid | Trade-off EVM for ACP. |

NI recommends the Clipping method of CFR, with filter enabled, for
 performing Pre-DPD Signal Conditioning to obtain a Reference Waveform with desired PAPR,
 and Clipping method for applying CFR on the pre-distorted
 waveform.

#### References

<sup>[4]</sup>Sperlich, Roland, et al. "Power amplifier linearization with digital
 pre-distortion and crest factor reduction." Microwave Symposium Digest, 2004 IEEE
 MTT-S International. Vol. 2. IEEE, 2004.

<sup>[5]</sup> Braithwaite, R. Neil. "A combined approach to digital predistortion
 and crest factor reduction for the linearization of an RF power amplifier." IEEE
 Transactions on Microwave Theory and Techniques 61.1 (2013): 291-302.

<sup>[6]</sup> Armstrong, Jean. "Peak-to-average power reduction for OFDM by repeated
 clipping and frequency domain filtering." Electronics letters 38.5 (2002): 246-247.

<!--NI_TOPIC bundle=rfmx-specan path=decomposed-vector-rotation-model.html language=enus -->
## TOPIC 00007: Decomposed Vector Rotation Model

- bundle_id: `rfmx-specan`
- source_path: `decomposed-vector-rotation-model.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan/raw/resource/enus/decomposed-vector-rotation-model.html
- document_id: `rfmx-specan`
- page_type: `leaf`
- content_type: `concept`
- source_description: The digital predistortion (DPD) models can be sorted into the following categories.Global models are DPD models that cater to the entire amplitude range of the input waveform as a monolith with no special consideration given to high or low power regions.Segmented or piecewise models are models that

### Decomposed Vector Rotation Model

The digital predistortion (DPD) models can be sorted into the following
 categories.

- Global
 models are DPD models that cater to the entire amplitude range of
 the input waveform as a monolith with no special consideration given to high or low
 power regions.
- Segmented or piecewise models are
 models that divide the amplitude range of the input waveform into multiple smaller
 segments and optimize model accuracy for each segment while maintaining smooth
 continuity at segment boundaries.

Decomposed vector rotation (DVR) is a
 segmented DPD model inspired by a modified form of the canonical piece-wise-linear
 functions (CPWL). The nonlinear operation in this model is achieved by using the
 absolute operation and the nonlinear functions are represented in a piecewise
 manner.

The following equation is a complex baseband representation of the DVR
 based DPD model.

y

n

=

y

[

n

]

L

i

n

e

a

r

_

F

i

l

t

e

r

+

y

[

n

]

B

a

s

i

c

_

D

V

R

+

y

[

n

]

D

D

R

_

B

a

s

e

d

_

D

V

R

→

(

1

)

In
 the equation above, each term is defined as follows.

y

[

n

]

L

i

n

e

a

r

_

F

i

l

t

e

r

=

∑

i

=

0

M

l

a

i

x

[

n

-

i

]

→

(

2

)

y

[

n

]

B

a

s

i

c

_

D

V

R

=

∑

k

=

1

K

∑

i

=

0

M

n

l

C

k

i

,

1

x

[

n

-

i

]

-

β

k

e

j

θ

[

n

-

i

]

+

∑

k

=

1

K

∑

i

=

0

M

n

l

C

k

i

,

21

x

[

n

-

i

]

-

β

k

e

j

θ

[

n

-

i

]

.

x

[

n

]

+

∑

k

=

1

K

∑

i

=

1

M

n

l

C

k

i

,

23

x

[

n

-

i

]

-

β

k

.

x

[

n

-

i

]

→

(

3

)

y

[

n

]

D

D

R

_

B

a

s

e

d

_

D

V

R

=

∑

k

=

1

K

∑

i

=

1

M

n

l

C

k

i

,

24

x

[

n

]

-

β

k

.

x

[

n

-

i

]

+

∑

k

=

1

K

∑

i

=

0

M

n

l

C

k

i

,

25

x

[

n

]

-

β

k

.

x

n

2

.

x

*

[

n

-

i

]

+

∑

k

=

1

K

∑

i

=

0

M

n

l

C

k

i

,

26

x

[

n

]

-

β

k

.

x

[

n

]

.

x

[

n

-

i

]

2

+

∑

k

=

1

K

∑

i

=

0

M

n

l

C

k

i

,

27

x

n

-

β

k

.

x

*

n

.

x

2

[

n

-

i

]

→

(

4

)

where

- y[n] is the predistorted
 signal
- x[n] is the original input
 signal
- C_ki are the DPD model
 coefficients
- K is the number of
 segments
- M_l is the linear memory
 depth
- M_nl is the nonlinear memory
 depth

Note

〖y[n]〗_(DDR_Based_DVR)

<!--NI_TOPIC bundle=rfmx-specan path=detectors.html language=enus -->
## TOPIC 00008: Detector Types

- bundle_id: `rfmx-specan`
- source_path: `detectors.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan/raw/resource/enus/detectors.html
- document_id: `rfmx-specan`
- page_type: `leaf`
- content_type: `concept`
- source_description: Following are the various detector types supported in RFmx. In all the graphs that follow for detectors, the connected points in different colors correspond to different buckets and the yellow dot corresponds to the detected point. None - No detector is applied when detector type is None. Sample - T

### Detector Types

Following are the various detector types supported in RFmx. In all the graphs that follow for
 detectors, the connected points in different colors correspond to different buckets and the
 yellow dot corresponds to the detected point.

None - No detector is applied when detector type is None.

Sample - The middle sample is detected in each bucket.

[IMAGE alt='image' src='GUID-AAA3D661-3A13-47E2-B77A-E03E5EE36BE1-a5.gif']

Peak - The sample with highest value is detected in each bucket.

[IMAGE alt='image' src='GUID-153FE732-9542-4F79-9F85-6FD60DE37B50-a5.gif']

Negative Peak - The sample with least value is detected in each bucket.

[IMAGE alt='image' src='GUID-45F95199-59FA-40E8-82BB-CA2963AFAC83-a5.gif']

Normal - If the signal only rises or only falls within a bucket, then
 the sample with the highest value in that bucket is detected. If the signal both rises and falls
 within a bucket, then the sample with the highest or the least value is detected based on whether
 that bucket index is odd or even. When the bucket index is odd, the highest value from that
 bucket is compared with the highest value from the previous bucket and the higher of those two
 values is detected. When the bucket index is even, the sample with the least value is detected in
 that bucket.

[IMAGE alt='image' src='GUID-EEE0FEA4-366B-4982-AF8A-8962C3142D79-a5.gif']

Average RMS - The resultant sample in each bucket is the RMS average of
 all the sample points in that bucket. The averaging is performed on power samples in
 (Volt)<sup>2</sup> units.

[IMAGE alt='image' src='GUID-78B75F76-FCA4-4FCC-B8AA-0E34B12C7975-a5.gif']

Average Voltage - The resultant sample in each bucket is the scalar
 average of all the sample points in that bucket. The averaging is performed on voltage samples.

[IMAGE alt='image' src='GUID-204FC598-C33E-4534-9B08-68DAA695B121-a5.gif']

Average Log - The resultant sample in each bucket is the log average of
 all the sample points in that bucket. The averaging is performed on power samples in dBm units.

[IMAGE alt='image' src='GUID-B162D454-9002-4688-A9E6-6D2F961952F4-a5.gif']

Note

- Detector type might sometimes be coerced to a particular detector type based on the
 averaging type and detector type as mentioned in the following table. [IMAGE alt='image' src='GUID-45853E2F-899C-43F4-8797-FC81C40E2027-a5.gif']
- Noise compensation support is limited based on averaging type and detector type as
 mentioned in the following table. [IMAGE alt='image' src='GUID-99AA3F5B-D11D-48D5-8CD1-BF1E3546B359-a5.gif']
- Subspan Overlap support is limited to the following cases. [IMAGE alt='image' src='GUID-F07F0C2E-0CFD-441A-8F51-0014390DCBCB-a5.gif']

<!--NI_TOPIC bundle=rfmx-specan path=digital-emulation-rbw-filters.html language=enus -->
## TOPIC 00009: Digital Emulation of Analog RBW Filters

- bundle_id: `rfmx-specan`
- source_path: `digital-emulation-rbw-filters.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan/raw/resource/enus/digital-emulation-rbw-filters.html
- document_id: `rfmx-specan`
- page_type: `leaf`
- content_type: `concept`
- source_description: A traditional swept-spectrum analyzer computes the spectrum of the incident signal by continuously frequency shifting the signal from start to end of the frequency-span of interest, and filtering the resultant signal using an analog filter, called the RBW Filter. The frequency-response of the RBW fi

### Digital Emulation of Analog RBW Filters

A traditional swept-spectrum analyzer computes the spectrum of the incident signal by
 continuously frequency shifting the signal from start to end of the frequency-span of
 interest, and filtering the resultant signal using an analog filter, called the RBW
 Filter. The frequency-response of the RBW filter shapes the spectrum computed by the
 swept-spectrum analyzer. Using an FFT based instrument, this behavior is achieved by
 emulating the RBW filter digitally. The RBW specified is the minimum frequency spacing
 between two tones that can be distinguished from each other.

The following figure shows a digital RBW filter sweep.

[IMAGE alt='image' src='GUID-7159080D-1965-496A-AA71-775BFF7C4960-a5.gif']

When you set RBW to Auto, the measurement sets RBW as per the
 following relation:

RBW = min {1MHz, Span/100}

Span is computed based on the measurement configuration. The following table shows the
 supported RBW filter types:

| RBW Filter Type | Excess Span (Hz) | Filter Response |
| --- | --- | --- |
| FFT Based | 0 | DFT of the windowing function |
| Gaussian | 5 × RBW |  |
| Flat | RBW |  |

RBW filter type affects the total span required for the measurement. The lowest and
 highest frequency measurable is limited by the device frequency limits and the excess
 bandwidth required by the RBW filter. For zero span or time domain measurements, the
 sample rate required is determined by the 3dB bandwidth and the excess bandwidth
 required to realize the digital RBW filter.

The maximum RBW is restricted by the instantaneous bandwidth of the signal analyzer. When
 you use IF filters available on certain signal analyzers, the instantaneous bandwidth of
 the signal analyzer is limited to the IF filter bandwidth. For example, the PXIe-5665
 has IF filters with 3dB bandwidth of 300 kHz and 5 MHz. These filters improve the
 dynamic range of measurements such as the adjacent channel power (ACP) measurement.
 Hence the RBW is limited to 300 kHz while using dynamic range method in ACP.

The following table lists the cases where narrowband IF filters are used.

| Configuration | Hardware | Max RBW |
| --- | --- | --- |
| ACP Measurement Method = Dynamic Range | PXIe-5665, PXIe-5668 | 300 kHz |
| Cleaner Spectrum Enabled= True (Enabled by default for Spectrum, Spur) | PXIe-5665 | 300 kHz (Center Frequency < 80 MHz) |
| PXIe-5668 | 100 MHz |  |

#### Effect of RBW on Displayed Average Noise Level (DANL)

While measuring local oscillator (LO) amplitude spurs, configure the RBW such that the
 DANL of the spectrum is lower than the spur.

RBW and DANL are related as shown in the following equation:

[IMAGE alt='image' src='GUID-60B88E32-CCF1-4F07-9A51-8C729DCE5F15-a5.png']

<!--NI_TOPIC bundle=rfmx-specan path=digital-emulation-vbw-filters.html language=enus -->
## TOPIC 00010: Digital Emulation of Analog VBW Filters

- bundle_id: `rfmx-specan`
- source_path: `digital-emulation-vbw-filters.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan/raw/resource/enus/digital-emulation-vbw-filters.html
- document_id: `rfmx-specan`
- page_type: `leaf`
- content_type: `concept`
- source_description: The video bandwidth filter (VBW) filter is used to smoothen the trace for display. In a traditional swept spectrum analyzer, a single pole low-pass filter is used for VBW filtering. A low-pass filter removes high frequency components from the trace giving it a smoothened appearance. In general, an V

### Digital Emulation of Analog VBW
 Filters

The video bandwidth filter (VBW) filter is used to smoothen the trace for display. In a
 traditional swept spectrum analyzer, a single pole low-pass filter is used for VBW
 filtering. A low-pass filter removes high frequency components from the trace giving it
 a smoothened appearance.

In general, an VBW to RBW ratio of 0.01 or lesser provides good smoothening, and a VBW to
 RBW ratio greater than or equal to 3 provides no smoothening at all.

#### Emulation in Zero Span Measurements

A simple RC circuit with output voltage taken across the capacitance is used to
 realize the low pass filter in traditional analyzers.

[IMAGE alt='image' src='GUID-386CFB58-20E4-4012-B981-DC1F820DD282-a5.gif']

The relationship between the output and the input voltage is as shown in the
 following equation.

[IMAGE alt='image' src='GUID-CAD3F8F0-D544-4863-AF9C-891BAF847268-a5.gif']

In a discrete domain, this RC based low-pass filter can be realized by the following
 equation with the input x[n] sampled every t
 duration to obtain the output y[n].

[IMAGE alt='image' src='GUID-CE3849A8-FE36-402C-B7B5-8E292BAEA877-a5.gif']

By re-arranging the preceding equation, we get the following equation.

[IMAGE alt='image' src='GUID-A4696E78-2576-4E4B-91D9-37A8E5208DF2-a5.gif']

where,

[IMAGE alt='image' src='GUID-3ADCAB85-A5EE-4F05-A0F8-1BFE4813BF60-a5.gif']

The VBW digital filter is applied on the zero span waveforms in dBm.

#### Emulation in Spectral Measurements

Averaging over multiple spectrums also reduces the variance of the spectrum and gives
 it a smoothened appearance. For spectral measurements, the VBW filter is emulated by
 averaging, to make use of the advantages of the FFT based signal
 analyzer<sup>[1]</sup>. The number of VBW averages is determined in such a way
 that the resulting averaged trace has a similar variance reduction to that of a VBW
 filter in a swept analyzer. This number of VBW averages is factored in sweep time
 required by the measurement.

#### Determining Number of VBW Averages

When you set the RBW Filter Type property to FFT Based, the
 number of VBW averages is given by the following equation<sup>[1]</sup>.

[IMAGE alt='image' src='GUID-3F10EA58-6CE9-4920-B00C-B5AB3F398D15-a5.png']

When you set the RBW Filter Type property to Gaussian or
 Flat, the number of VBW averages is given by the
 following equation.

[IMAGE alt='image' src='GUID-6FD1AF6B-D5B1-4BA1-91BA-E3BFFE4B6542-a5.gif']

where,

[IMAGE alt='image' src='GUID-2AD91D50-7686-4017-8FA6-CA05562029BE-a5.gif']

The following table lists the values of y for different RBW filter
 types.

[IMAGE alt='image' src='GUID-5196E54B-4D43-4746-9E0F-FDBD847D84CA-a5.gif']

Note

- Set VBW = 3*RBW to bypass VBW filter emulation. Number of VBW averages
 is set to 1 when you bypass VBW emulation.
- VBW averaging is performed on (Volts) 2 units in spectral
 measurement.

#### Sweep Time

In a traditional sweep analyzer, sweep time is defined as the duration within which a
 specified span is swept by the analog RBW filter. The accuracy of the measurement
 depends on the duration for which the RBW stays in a frequency range and also on VBW
 filter’s settling time. The following equations describe how traditional swept
 analyzers relate Sweep Time, Span, RBW and VBW.

when,

[IMAGE alt='image' src='GUID-484BCC8C-A824-476C-A99C-FDF0DD4ACBF5-a5.gif']

[IMAGE alt='image' src='GUID-17203A33-34DD-42E1-8613-0D2504384423-a5.png']

when,

[IMAGE alt='image' src='GUID-16EDDFF6-47A7-47FD-B7F2-37F0AC4F7F68-a5.gif']

[IMAGE alt='image' src='GUID-AA8995EB-5E20-43C4-B4C6-31577FC7FEEE-a5.gif']

where, RBW is the RBW filter bandwidth and VBW is the VBW filter bandwidth.

FFT based signal analyzers use Windowed FFT to compute the spectrum. To emulate the
 RBW and VBW filters available in the traditional swept analyzers, RFmx uses digital
 RBW filtering and averaging on computed spectrum. Sweep time, RBW and VBW are
 related in RFmx as shown in the following equations.

when,

[IMAGE alt='image' src='GUID-484BCC8C-A824-476C-A99C-FDF0DD4ACBF5-a5.gif'],

[IMAGE alt='image' src='GUID-291D9B01-DCE1-4AC5-BB21-724E793BBE27-a5.png']

when,

[IMAGE alt='image' src='GUID-CAF83F4E-A8B0-4FCB-902F-A5D056C3DD06-a5.gif']

where,

[IMAGE alt='image' src='GUID-ECC5DA3F-9D25-4CCA-9EF3-CBDC7A84B6DE-a5.png']

RFmx measurements use the preceding relationship to determine the auto sweep
 time.

When you specify the sweep time, the measurement behaviors are observed.

- If VBW is bypassed (VBW ≥ 3*RBW) , the measurement computes the spectrum with a
 bin spacing 1/sweep time.
- If VBW is not bypassed (VBW < 3*RBW), the measurement computes the spectrum
 with a bin spacing 1/FFT time. Number of VBW averages is determined by sweep
 time and FFT time using the following equation.

[IMAGE alt='image' src='GUID-CBF58F5F-0B11-42AD-93CC-397BF86349CA-a5.gif']

Note

- Typically, FFT based spectral measurement requires a much smaller sweep
 time than the sweep time required by traditional swept spectrum
 analyzers for the same measurement quality.
- Setting a large sweep time results in higher FFT time thereby leading to
 more samples being acquired, potentially making the measurement
 increasingly more memory intensive and computationally intensive.
- The minimum RBW and maximum sweep time that you can specify are
 dependent on the RBW filter type as shown in the following table.

| RBW Filter Type | Minimum RBW (Hz) | Maximum Sweep Time |
| --- | --- | --- |
| FFT Based | 1 | Ignored |
| Others | 10 | Depends on processing power |

#### References

[1] National Instruments, Emulating Video Bandwidth and Detectors in an FFT-based
 Vector Signal Analyzer, (http://www.ni.com/tutorial/13869/en/)

<!--NI_TOPIC bundle=rfmx-specan path=dpd.html language=enus -->
## TOPIC 00011: DPD

- bundle_id: `rfmx-specan`
- source_path: `dpd.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan/raw/resource/enus/dpd.html
- document_id: `rfmx-specan`
- page_type: `leaf`
- content_type: `concept`
- source_description: The DPD measurement requires Power Amplifier license activation. If you install RFmx SpecAn but do not activate the Power Amplifier license, you will have 30 days from the first time you use the measurement to evaluate it. One of the fundamental assumptions in the study and design of signal processi

### DPD

Note

One of the fundamental assumptions in the study and design of signal processing and
 communication systems is that the systems under investigation are more or less linear.
 While the linearity assumption holds in digital subsystems, the response of analog
 subsystems can only be treated as being approximately linear over a certain range of
 input power or frequency band.

An example of a nonlinear subsystem used in the ubiquitous wireless communication systems
 is a power amplifier (PA). While the overall response of the PA is clearly nonlinear,
 many applications where the region of operation is limited to a relatively linear
 portion of the PA response do not face any serious problem due to the nonlinear nature
 of the PA. This is true for cellular standards such as GSM or EDGE.

The following figure shows the typical input-output response of a PA.

[IMAGE alt='image' src='GUID-C8BACEF7-7F00-4551-A826-D5C6673559F6-a5.png']

With the rapid migration of cellular and connectivity technologies towards multicarrier
 modulation schemes, such as HSPA+, LTE-Advanced and IEEE 802.11ac where the RF envelope
 fluctuations vary from 6 dB to 12 dB relative to the average signal power, it has become
 impractical to back-off the operating point to continue to operate the PA in a
 relatively linear region because operating efficiency of PAs diminishes as the operating
 point is backed-off. Technologies such as envelope tracking and digital predistortion
 have been developed in order to linearize power amplifier response without resorting to
 power back-off and thus continue to operate the PA in a high efficiency mode.

Digital predistortion (DPD) is a generic name for all power amplifier linearization
 techniques that modify the complex baseband representation of the RF signal at the input
 to the PA under test in such a way that the RF signal at the output of the PA is as
 close to the expected output as possible, had the PA been a linear memoryless device.
 The exact implementation of individual DPD techniques may require PA characterization or
 PA modeling.

The following figure shows a simplified representation of the signal processing chain
 where PA is preceded by digital predistortion.

[IMAGE alt='image' src='GUID-C99CB534-EF48-419A-AB7B-6A0CD2CD1EAD-a5.png']

[IMAGE alt='image' src='GUID-989DB900-132F-4363-B483-CDDFF4CFAECD-a5.jpg']

<!--NI_TOPIC bundle=rfmx-specan path=dut-types.html language=enus -->
## TOPIC 00012: DUT Types

- bundle_id: `rfmx-specan`
- source_path: `dut-types.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan/raw/resource/enus/dut-types.html
- document_id: `rfmx-specan`
- page_type: `leaf`
- content_type: `concept`
- source_description: RFmx Noise Figure measurement supports fixed frequency as well as frequency converting DUTs. The frequency of interest at the input port of the DUT is referred as f[RF] and that at the output port is referred as f[IF]. Fixed Frequency DUTs Fixed frequency DUTs, such as low noise amplifiers, do not t

### DUT Types

RFmx Noise Figure measurement supports fixed frequency as well as frequency converting
 DUTs. The frequency of interest at the input port of the DUT is referred as
 f<sub>RF</sub> and that at the output port is referred as f<sub>IF</sub>.

#### Fixed Frequency DUTs

Fixed frequency DUTs, such as low noise amplifiers, do not translate the input
 frequency to a different output frequency. For such DUTs,
 f<sub>IF</sub>=f<sub>RF</sub>.

[IMAGE alt='image' src='GUID-0051777D-B442-4A66-BED8-2A82CAE7910B-a5.png']

#### Frequency Converting DUTs

Frequency converting DUTs, or mixers, translate the input frequency to a different
 output frequency using a local oscillator (LO). For such DUTs,
 f<sub>IF</sub>≠f<sub>RF</sub>.

[IMAGE alt='image' src='GUID-E70BE7E9-1187-484F-8687-DBE5735AF7F1-a5.png']

Frequency converting DUTs can further be classified as upconverters or downconverters
 based on the frequency at the output port. The two possible frequency products at
 the output port for a given f<sub>RF</sub> and f<sub>LO</sub> are |f<sub>RF</sub> -
 f<sub>LO</sub>| and f<sub>RF</sub> + f<sub>LO</sub>.

For downconverters, f<sub>IF</sub> = |f<sub>RF</sub> - f<sub>LO</sub>|, and for
 upconverters, f<sub>IF</sub> = f<sub>RF</sub> + f<sub>LO</sub>

#### Image Mixing and Sidebands

For a given f<sub>IF</sub> and f<sub>LO</sub>, there exists two input frequencies
 that can map to f<sub>IF</sub>. These frequencies are f<sub>IF</sub> =
 |f<sub>RF</sub> - f<sub>LO</sub>| and f<sub>IF</sub> = f<sub>RF</sub> +
 f<sub>LO</sub>. One of these frequencies is the signal frequency
 (f<sub>RF</sub>), while the other frequency is the image frequency (f<sub>IM</sub>).
 To distinguish between the signal and image frequency, sideband information for
 f<sub>RF</sub> is required.

- When the sideband is Lower Side Band (LSB), f RF = min {f IF 
 + f LO , |f IF - f LO |} = |f IF -
 f LO |.
- When the sideband is Upper Side Band (USB), f RF = f IF +
 f LO

| Sideband | fRF | fIM |
| --- | --- | --- |
| LSB | min {fIF + fLO, \|fIF - fLO\|} = \|fIF - fLO\| | fIF + fLO |
| USB | max {fIF + fLO, \|fIF - fLO\|} = fIF + fLO | \|fIF - fLO\| |

The following diagram shows an example of the signal and image frequency mixing in a
 downconverter with signal sideband as LSB.

[IMAGE alt='image' src='GUID-3F5A312C-74E3-4817-8DE9-7F1F1A0A374A-a5.png']

#### Image Rejection

Image rejection is the relative gain suppression of image and is defined as the ratio
 of the gain of the DUT at the image frequency to that at the RF frequency.

Noise Figure measurement requires knowledge of the image rejection specification of
 the DUT for accurate noise figure measurements. Image rejection of 0 dB implies that
 both the signal and image frequencies undergo the same DUT gain, while image
 rejection of 999.99 dB implies that the image is almost entirely suppressed. Any
 value between 0 dB and 999.99 dB implies partial suppression of the image, relative
 to the RF frequency.

The following figure describes the noise model for frequency translating DUTs, where
 the signal and image frequency paths are modelled independently.

[IMAGE alt='image' src='GUID-2BA471CC-D8C8-4EBA-BE98-38C0145467E2-a5.png']

where,

N<sub>S</sub>(f<sub>RF</sub>) is the noise power incident at the input port of the
 DUT, at f<sub>RF</sub>

N<sub>S</sub>(f<sub>IM</sub>) is the noise power incident at the input port of the
 DUT, at f<sub>IM</sub>

N<sub>D</sub>(f<sub>RF</sub>) is the noise power added by the DUT, at
 f<sub>RF</sub>

N<sub>D</sub>(f<sub>IM</sub>) is the noise power added by the DUT, at
 f<sub>IM</sub>

G(f<sub>IF</sub>, f<sub>RF</sub>) is the DUT frequency translation gain from
 f<sub>IF</sub> to f<sub>RF</sub>

G(f<sub>IF</sub>, f<sub>IM</sub>) is the DUT gain from f<sub>IF</sub> to
 f<sub>IM</sub>

N<sub>out</sub>(f<sub>IF</sub>) is the noise power at the
 output port of the DUT at f<sub>IF</sub>

IEEE definition for frequency translating DUTs [1] is as mentioned in the following
 equation. The noise factor of the DUT, F<sub>D</sub>(f<sub>IF</sub>,
 f<sub>RF</sub>), is defined for a pair of input and output frequencies, where
 f<sub>RF</sub> is the input frequency and f<sub>IF</sub> is the output
 frequency.

[IMAGE alt='image' src='GUID-B29C9BCF-AD8A-4885-8A51-5A16F8B1A53C-a5.png']

[IMAGE alt='image' src='GUID-C306DC74-A6C1-46F2-B696-A1D213272130-a5.png']

where,

T<sub>D</sub>(f<sub>IF</sub>, f<sub>RF</sub>) is the noise temperature of the DUT at
 f<sub>RF</sub>

T<sub>D</sub>(f<sub>IM</sub>, f<sub>RF</sub>) is the noise temperature of the DUT at
 f<sub>IM</sub>

G<sub>REJ</sub>(f<sub>IF</sub>, f<sub>IM</sub>) is the image rejection

#### References

<sup>[1]</sup> Otegi, N., et al. "SSB noise figure measurements of frequency
 translating devices." IEEE MTT-S International Microwave Symposium
 Digest. IEEE, 2006.

<!--NI_TOPIC bundle=rfmx-specan path=extracting-dpd-model-coefficients.html language=enus -->
## TOPIC 00013: Extracting DPD Model Coefficients

- bundle_id: `rfmx-specan`
- source_path: `extracting-dpd-model-coefficients.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan/raw/resource/enus/extracting-dpd-model-coefficients.html
- document_id: `rfmx-specan`
- page_type: `leaf`
- content_type: `task`
- source_description: RFmxSpecAn DPD allows two modes for extracting DPD model coefficients:Acquire and ExtractAcquires the training waveform required for the extraction of the DPD model coefficients from the hardware and computes the model coefficients. Extract Only Uses the user configured training waveform for extract

### Extracting DPD Model Coefficients

RFmxSpecAn DPD allows two modes
 for extracting DPD model coefficients:

Acquire and
 Extract

Extract Only

Extract Only

The following example steps describe the extraction of DVR DPD model coefficients
 using a training waveform obtained from an iterative learning control based DPD
 using RFmxSpecAn IDPD measurement.

1. Enable IDPD measurement.
2. Set any appropriate IDPD-related properties for your
 application.
3. Initiate IDPD measurement and fetch the IDPD predistorted waveform.
4. Perform a sufficient number of IDPD iterations to produce a stable IDPD
 predistorted waveform.
5. Enable DPD
 measurement.
6. Set any relevant DPD properties, such as: 
 DPD Measurement Mode, 
 DPD DUT Average Input Power, 
 DPD Measurement Sampling Rate.
7. Set the DPD Model to
 DVR.
8. Set any other appropriate DVR Model parameters for your
 application.
9. Configure the *Predistorted waveform* fetched from IDPD as a
 target waveform in the DPD measurement. This instructs the RFmxSpecAn DPD
 measurement to find DVR model coefficients that can nonlinearly transform the
 reference waveform into the desired predistorted *target
 waveform*.
10. Initiate the DPD measurement to extract
 the DVR model coefficients.
11. Apply Digital Predistortion
 to obtain the predistorted waveform based on the DVR model.

Parent topic:

Decomposed Vector Rotation Model

<!--NI_TOPIC bundle=rfmx-specan path=faqs.html language=enus -->
## TOPIC 00014: FAQs

- bundle_id: `rfmx-specan`
- source_path: `faqs.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan/raw/resource/enus/faqs.html
- document_id: `rfmx-specan`
- page_type: `leaf`
- content_type: `concept`
- source_description: Answers common questions about RFmx SpecAn features and measurements. Why do spectrum traces have more variation after noise compensation as compared to the spectrum without noise compensation?Example: assume that without noise compensation, the measured noise power is 5E–6 ± 0.5E–6 watts. The corre

### FAQs

Answers common questions about RFmx SpecAn features and
 measurements.

#### Why do spectrum traces have more variation after
 noise compensation as compared to the spectrum without noise
 compensation?

Example: assume that without noise compensation, the
 measured noise power is 5E–6 ± 0.5E–6 watts. The corresponding power, in dBm, would
 be –42.23 ± 0.36 dBm. Observe that the variation in power is 0.36 dB. Further,
 assume that the instrument noise is estimated to be 4E–6 watts. After noise
 compensation, the reported power would be 1E–6 ± 0.5E–6 watts. On a logarithmic
 scale, this would translate to –50.62 ± 2.38 dBm. This implies that the variation in
 power when represented on a logarithmic scale, has increased from 0.36 dB to 2.38
 dB.

The following figure illustrates this example graphically.

[IMAGE alt='image' src='GUID-BE8C6A10-E3EA-4978-A9FC-578E5A3B8FFA-a5.png']

Power is expressed in Watts on the x-axis, and in dBm on the y-axis. The blue
 '+' denotes the point (5E–6 watts, –42.23 dBm). The blue
 vertical guides around this point illustrate a variation of ± 0.5E–6 watts on the
 x-axis. The blue horizontal guides around the same point illustrate the
 corresponding variation of ± 0.36 dB.

The red '+'
 denotes the point (1E–6 watts, –50.62 dBm), obtained after noise compensation,
 assuming an instrument noise of 4E–6 watts. Analogous to the previous observations,
 the red vertical guides around this point illustrate a variation of ±0.5E–6 watts on
 the x-axis, same as the blue vertical guides.

The red horizontal guides around
 this point illustrate the corresponding variation of ±2.38 dB, illustrating the
 magnification of power variation after noise compensation, when viewed in
 logarithmic scale. scale. This emerges from the fact that slope of a logarithmic
 curve, logx, is inversely proportional to x.
 Smaller values of x result in large changes in
 logx and vice-versa.

You can use RFmx SpecAn Spectrum
 measurement and enable the Average RMS Detectors to reduce trace variation after
 noise compensation.

<!--NI_TOPIC bundle=rfmx-specan path=fcnt.html language=enus -->
## TOPIC 00015: Frequency Counter (FCnt)

- bundle_id: `rfmx-specan`
- source_path: `fcnt.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan/raw/resource/enus/fcnt.html
- document_id: `rfmx-specan`
- page_type: `leaf`
- content_type: `concept`
- source_description: FCnt is used to accurately measure the frequency of a tone, for example, the tone generated by a local oscillator. The rate of change in the instantaneous phase of the time domain signal determines the signal frequency. The signal is acquired for a duration specified by the measurement interval and

### Frequency Counter (FCnt)

FCnt is used to accurately measure the frequency of a tone, for example, the tone
 generated by a local oscillator. The rate of change in the instantaneous phase of the
 time domain signal determines the signal frequency. The signal is acquired for a
 duration specified by the measurement interval and is digitally filtered by an RBW
 filter.

The following list describes the basic properties that you can configure for an FCnt
 measurement:

- RBW: Configure RBW to specify the 3 dB bandwidth over which time domain
 signal needs to be analyzed. Ensure that RBW does not exceed the instantaneous bandwidth of
 the signal analyzer. NI recommends using no filter or a flat RBW filter. Refer to the
 Zero Span section of the Spectrum topic for information on the sample rate
 required by the measurement.
- Measurement Interval : Configure the measurement interval to
 specify the duration of acquisition.

#### Allan Deviation

Frequency stability of oscillators is affected by different types of noises such as
 flicker noise and random walk noise apart from stationary white noise. Allan deviation
 is a measure of the frequency jitter arising from these types of noises. If [IMAGE alt='image' src='GUID-C30083E3-7218-4FBD-831E-D175F6BE9463-a5.png']are instantaneous frequencies measured at regular time intervals,
 Allan deviation is computed as two-sample standard deviation of this data as shown in
 the following equation.

[IMAGE alt='image' src='GUID-8051923A-1F68-4078-B7E2-ECBA99FF3A5E-a5.png']

Related concepts:

- Spectrum

<!--NI_TOPIC bundle=rfmx-specan path=harmonics.html language=enus -->
## TOPIC 00016: Harmonics

- bundle_id: `rfmx-specan`
- source_path: `harmonics.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan/raw/resource/enus/harmonics.html
- document_id: `rfmx-specan`
- page_type: `leaf`
- content_type: `concept`
- source_description: A harmonic of a signal, referred to as the fundamental, is the signal at an integer multiple of the fundamental frequency. If the fundamental frequency is f, the harmonics are signals at frequencies 2f, 3f, 4f, and so on. These harmonics are identified by order. For example, the harmonic at 2f is ca

### Harmonics

A harmonic of a signal, referred to as the fundamental, is the signal at an integer multiple of
 the fundamental frequency. If the fundamental frequency is f, the
 harmonics are signals at frequencies 2f, 3f,
 4f, and so on. These harmonics are identified by order. For
 example, the harmonic at 2f is called the second-order harmonic.
 Similarly, the harmonic at n×f is called the
 n<sup>th</sup> order harmonic.

The following figure shows the configuration of fundamental and harmonics.

[IMAGE alt='image' src='GUID-7FF301B4-2B58-47C5-9ADF-7CC687373B45-a5.png']

Harmonic distortions are inherent to devices and systems that have nonlinear
 characteristics. The total harmonic distortion (THD(%)) is a measure of these
 distortions. THD is calculated using the following formula:

[IMAGE alt='image' src='GUID-4F55E02F-ACBA-41C0-9EB6-24157A8E788B-a5.png']

#### Fundamental and Harmonics Configuration

The RF center frequency is considered as the fundamental frequency. The power
 measured at the fundamental is as seen through an RBW filter for the duration
 specified by the measurement interval.

A harmonic is defined by the order, the RBW filter bandwidth, and the measurement
 interval.

The fundamental RBW filter type and RRC alpha settings configured using the
 fundamental configuration are applicable for all harmonics in both auto and manual
 harmonic setup.

You can configure harmonics in the following ways:

Auto Harmonic Setup

Auto harmonic setup uses the fundamental configuration to derive the harmonic
 configuration. You must specify the number of harmonics to be measured. The
 configured number of harmonics includes the fundamental. The n<sup>th</sup> harmonic
 configuration is derived from the fundamental configuration using the following
 equations. Auto harmonics setup can be enabled by setting Harm Harmonics
 Auto Setup Enabled property to True.

[IMAGE alt='image' src='GUID-B65BB5E8-33E9-46AA-96A4-0B377CB835F6-a5.png']

The RBW filter type and RRC alpha settings for each harmonic are same as those
 configured for the fundamental.

For a specified RBW filter type, the digital filter response includes the excess
 bandwidth to realize the shape of the traditional analog RBW filter. Refer to the
 Spectral Measurements topic for more details on RBW filters.

If the excess span of the resolution bandwidth filter corresponding to the
 n<sup>th</sup> harmonic exceeds the device instantaneous bandwidth (DIBW) of the
 signal analyzer, the measurement coerces n<sup>th</sup> harmonic 3dB RBW and
 measurement interval. This coercion is required only when the measurement method is
 set to Time Domain.

The measurement coerces the n<sup>th</sup> harmonic 3dB RBW using the following
 equation:

[IMAGE alt='image' src='GUID-5C574767-3A76-42DD-A9FF-CFB59F417B73-a5.png']

The measurement coerces the n<sup>th</sup> harmonic measurement interval using the
 following equation:

[IMAGE alt='image' src='GUID-5CEE4D1D-CBB6-41A3-86DD-6CA735408A94-a5.png']

Manual Harmonic Setup

Manual harmonic setup allows you to set the order, RBW filter bandwidth, and the
 measurement interval for the fundamental and each harmonic by using the per-harmonic
 configuration. The fundamental RBW and measurement interval configured using
 fundamental configuration are ignored. Instead, the fundamental is configured using
 the first element of the per-harmonic configuration, and therefore, must be enabled
 with order set to 1. The harmonics are configured from second element onwards. When
 the harmonics are configured using selector strings, the fundamental must be
 configured using the “harmonic<0>” string. Manual harmonics setup can be
 enabled by setting the Harm Harmonics Auto Setup Enabled property to
 False.

#### Measurement Method

Harmonics measurement supports two measurement methods based on the requirements of
 measurement speed and dynamic range.

- Time Domain – This method performs zero span measurement
 using the time-domain signal as seen through RBW filter for the specified
 measurement interval.
- Dynamic Range – This method improves the dynamic range when
 measuring harmonics in presence of the fundamental signal. To achieve this, the
 measurement performs acquisition using narrow band IF filters to isolate the
 harmonic being measured, followed by IF gain stages for reducing quantization noise
 of the digitizer. This method performs harmonic power measurements in the
 frequency-domain. Supported signal analyzers: PXIe-5665,
 PXIe-5668

#### Noise Compensation

Noise compensation can be used to further improve the dynamic range by reducing the
 impact of signal analyzer’s thermal noise contribution to the measurement. When noise
 compensation is enabled, the measurement is performed in two steps. The first step
 approximates the noise contribution of the signal analyzer. The acquisitions are
 averaged to obtain a reliable estimate of the signal analyzer's noise. The second step
 measures the power at the fundamental and the harmonics followed by subtraction of the
 signal analyzer's noise measured in the first step.

To optimize the execution speed of the measurement, the noise measured in the first step
 is cached so that the measurement can use it later, provided, the measurement
 configurations and state of the signal analyzer remains the same. When the signal
 analyzer or measurement parameters change, the first step is reinitiated to return valid
 measurements.

Supported signal analyzers: PXIe-5665, PXIe-5668

#### Recommended Settings

Signal Generator Considerations

The non-linearity in the signal generator can produce harmonics and limit the dynamic
 range when measuring harmonics from a DUT. To generate a clean signal, use a band pass
 or a low pass filter after the signal generator to filter out the harmonics. The
 following diagram shows a typical hardware setup for harmonics measurement.

[IMAGE alt='image' src='GUID-ACC56E6F-28D5-4743-9DD7-2EECBC53BE06-a5.png']

Signal Analyzer Considerations

Operate the analyzer at an optimal mixer level to minimize the distortion contributed by
 the signal analyzer.

Mixer Level (dBm) = Reference Level (dBm) – RF Attenuation (dB)

The following steps help to improve the dynamic range of the measurement:

- The RF input attenuation must be set such that the mixer operates at optimal
 operating level. Refer to the dynamic range chart of the device to know the optimum
 mixer level.
- To maximize the dynamic range of the ADC, configure the reference level equal to the
 peak power of the fundamental signal assuming the test setup is such that the
 fundamental is not filtered out.

To verify if the signal analyzer is contributing to the distortions, vary the RF input
 attenuator setting. If the measured distortion amplitude does not change on varying RF
 attenuation, the distortion is entirely because of the DUT. However, if the distortion
 amplitude changes, then signal analyzer is also contributing to the distortion.

Note

- The power at the fundamental and the harmonics are measured
 using the same reference level and is not adjusted on
 per-harmonic basis.
- Consider using RBW for all harmonics equal to that of the fundamental signal when
 the fundamental signal is a sinusoid. This can be achieved by using manual
 harmonic setup.
- Recommended signal analyzers: PXIe-5665, PXIe-5668

High Pass Filters

The fundamental signal can be filtered out, using a high pass filter (HPF) before the
 signal analyzer, to further improve the dynamic range by setting very low reference
 level. The following figure shows test setup with an external high pass filter before
 signal analyzer.

[IMAGE alt='image' src='GUID-59A042D5-FDBC-4A28-89B8-E08D7FF5077E-a5.png']

Note

Related concepts:

- Spectral Measurements Concepts

<!--NI_TOPIC bundle=rfmx-specan path=ilc-dpd.html language=enus -->
## TOPIC 00017: Iterative Learning Control based DPD

- bundle_id: `rfmx-specan`
- source_path: `ilc-dpd.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan/raw/resource/enus/ilc-dpd.html
- document_id: `rfmx-specan`
- page_type: `leaf`
- content_type: `concept`
- source_description: Introduction One of the fundamental assumptions in the study and design of signal processing and communication systems is that the systems under investigation are linear. While the linearity assumption remains true in digital subsystems, the response of analog subsystems can only be treated as being

### Iterative Learning Control based DPD

#### Introduction

One of the fundamental assumptions in the study and design of signal processing and
 communication systems is that the systems under investigation are linear. While the
 linearity assumption remains true in digital subsystems, the response of analog
 subsystems can only be treated as being approximately linear over a certain range of
 input power or frequency band.

An example of a nonlinear subsystem used in the ubiquitous wireless communication
 systems is a power amplifier (PA). While the overall response of the PA is clearly
 nonlinear, many applications where the region of operation is limited to a
 relatively linear portion of the PA response do not face any serious problem because
 of the nonlinear nature of the PA. This limitation is true for cellular standards
 such as GSM or EDGE.

The following figure shows the typical input-output response of a PA.

Figure 1.

[IMAGE alt='image' src='GUID-6E63F5A5-21DD-48DC-BA7F-DC0CA8B57236-a5.png']

Cellular and connectivity technologies are rapidly migrating to multicarrier
 modulation schemes such as HSPA+, LTE-Advanced, IEEE 802.11ac, and 5G-NR in which
 the RF envelope fluctuations vary from 6 dB to 12 dB relative to the average signal
 power. Backing off the PA operating point to a relatively linear region in such
 cases is impractical because the PA operating efficiency declines as the operating
 point is backed-off. Technologies such as envelope tracking and digital
 predistortion have been developed to linearize the power amplifier response without
 resorting to power back-off, allowing the PA to operate in a high-efficiency
 mode.

Digital predistortion (DPD) refers to power amplifier linearization techniques that
 modify the complex baseband representation of the RF signal at the input to the PA
 under test. This input signal is modified in such a way that, the RF signal at the
 output of the PA is as close to the expected output as possible, had the PA been a
 linear memoryless device. The exact individual DPD implementation techniques may
 require PA characterization or PA modelling.

The following figure shows a simplified representation of the signal processing
 chain, where the PA is preceded by digital predistortion. A number of DPD models
 exist in the literature; LUT-based DPD Models are used for linearizing PAs with
 negligible memory effects. Whereas DPD models based on Memory polynomial (MP) and
 Generalized Memory Polynomial (GMP) are used for linearizing PAs that exhibit memory
 effects and significantly high memory effects, respectively.

Figure 2.

[IMAGE alt='image' src='GUID-77A92988-693C-42CB-A1B8-6C304BDD77E6-a5.png']

#### ILC DPD

Iterative Learning Control (ILC) is a control theory technique used for iteratively
 learning the input that minimizes the difference between the system’s output and the
 desired reference signal. This is a non-model-based technique that can be applied to
 PAs for determining the the optimal input signal that drives the PA output to the
 desired linearized output response. The optimal input signal so obtained is also the
 optimal predistorted signal which can be used as a reference to identify the
 model-based DPD parameters.

The following figure shows the schematic of the ILC-based DPD.

Figure 3.

[IMAGE alt='image' src='GUID-E2570FAA-ED92-432B-99BE-DC293ACFF4AA-a5.png']

The first iteration, initializes u<sub>1</sub> [n] to the reference signal x[n]. The
 learning control algorithm outputs the predistorted signal u <sub>k+1</sub> [n] by
 correcting from the PA input u <sub>k</sub> [n], the sample-by-sample error between
 the desired signal y <sub>d</sub> [n] and the signal y <sub>k</sub> [n]/G in the kth
 iteration . y <sub>k</sub> [n] is the acquired output signal in the kth iteration
 and G is the scaling factor that is set equal to the target gain of the PA.

ILC is a feedback control system where convergence of the loop is expected by design,
 albeit with certain assumptions. One of them is the differentiability of the PA
 response. As the PA is driven deep into compression, its response tends towards the
 response of a hard-clipper (as shown in the following figure) which is a
 non-differentiable function. In this case even a small feedback error correction e
 <sub>k</sub>[n] can potentially destabilize the loop. Reference<sup>[1]</sup>
 details the convergence conditions for the ILC based DPD.

Figure 4.

[IMAGE alt='image' src='GUID-B8E6783D-5F15-4C41-8C00-3553E4D091F6-a5.png']

#### Practical Considerations

- Sampling Rate: For configuring the measurement sample rate, IDPD measurement
 provides two modes: Reference Waveform and User. Reference Waveform mode uses
 the sampling rate of configured reference waveform for the computation and
 skips software resampling throughout the signal processing chain. In this
 mode, NI recommends using an input reference signal that is at least three
 times oversampled. Using an oversampled reference signal improves the
 ACLR. User mode allows the user to configure a custom sampling rate.
 The measurement enables software resampling before computation. NI
 recommends setting the sampling rate to at least 3-times the sampling rate
 of the input reference signal.
- Equalizer Modes: Synchronization fails when the channel is dispersive and has
 large group delay variation over the bandwidth of interest. Equalization helps
 compensate for these large group delay variations and is particularly useful for
 non-contiguous multi-carrier signals with sparse frequency allocation of
 component carriers. The following figure shows the channel phase deviation from
 the linear phase response and how the equalizer compensates for it over the BW
 of +/-0.4Fs. Figure 5.Channel phase
 deviation from linear response
 
 
[IMAGE alt='image' src='GUID-58BCEADD-B384-4DE2-8BA4-425AF199D8B4-a5.png'] To compensate for the effect of the channel set the IDPD Equalizer Mode
 property to Hold. These Equalizer coefficients are obtained by using the
 Train-mode of the Equalizer , wherein, the group delay profile of the PA is
 learnt over +/-0.4Fs frequency range and filter coefficients are determined
 for the configured equalizer filter length. Here, Fs is the configured
 sampling frequency of the signal. Since the Equalization filter is
 trained over BW of +/-0.4Fs, the same coefficients may be re-used with
 signals of different BWs and spectral occupancy as long as the signal
 generator and the analyser settings, the DUT test setup and the sampling
 frequency setting are not altered. The default Off-mode is expected to
 work for most of the single-carrier signal configurations. Note You must ensure the Generator
 and the Analyzer gain states do not change or drift over time. Any change in
 gain states results in a change in the system channel response. The ILC loop
 could diverge in such cases.
- Power-Linearity Tradeoff: This property configures the gain tradeoff factor (in
 percentage) that determines if the PA output is optimized for maximum output
 power or maximum linearity. A 100 % gain value indicates gain at maximum input
 power and a 0 % indicates gain at maximum linearity. The tradeoff factor in-turn
 sets the ILC target gain G to be achieved. As indicated in the following figure,
 the default value of 50% achieves a target gain equal to the Average-power gain
 of the PA. Figure 6.Gain vs
 Power-linearity tradeoff
 
 
[IMAGE alt='image' src='GUID-BE9F28FD-64EC-48A7-BFF7-21B17C6E9B9D-a5.png'] The following figure shows the target gain achieved at different
 power-linearity tradeoff values. Figure 7.AM/AM plots for
 different Power-Linearity Tradeoff values
 
 
[IMAGE alt='image' src='GUID-2348BC06-916F-4C36-97A7-95AF9B4C4963-a5.png']
- Gain Expansion: The learning control algorithm corrects for the PA’s
 non-linearity by correcting the input signal samples that have undergone
 compression at the PA’s output. In this process, the PAPR of the pre-distorted
 waveform is expected to increase from one iteration to the next. Gain
 expansion is the allowable increase in the predistorted signal’s peak power
 relative to the Reference signal’s peak power. If the peak power exceeds
 this limit, the predistorted signal is hard clipped. This could typically
 happen when the PA is driven deep into compression, where its response is
 that of a hard-clipper. To linearize the output, the pre-distorted signal
 PAPR is expected to grow much larger as shown in the following figure. This
 property ensures that the PA is not driven into such a state. Figure 8.Impact of Gain
 expansion on the PA response
 
 
[IMAGE alt='image' src='GUID-E2762025-3AB9-411F-BAC1-A8B49EC2228E-a5.png']

#### Measurement Results

Figure 9.

[IMAGE alt='image' src='GUID-AC21A074-5536-49ED-A365-821C83DEDEA0-a5.png']

Figure 10.

[IMAGE alt='image' src='GUID-864908D8-2E0A-4B9B-86A4-8E6615A4428F-a5.png']

Figure 11.

[IMAGE alt='image' src='GUID-43624061-EFAB-46D5-8A7A-8E889B23CA28-a5.png']

#### Conclusion

Iterative Learning Control based DPD is a non-model-based technique that gives a near
 ideal pre-distorted waveform for a given PA and reference signal input. This is done
 by pre-distorting each and every sample in the input signal that undergoes
 non-linear transformation due to the PA.

The output of ILC-DPD, the pre-distorted waveform, can be used by the customers as
 the benchmark against which the performance of their DPD IP solution performance can
 be compared. This method can also be used to generate a labelled training dataset to
 train conventional (MP, GMP etc.) as well as modern (AI/ML based) DPD models.

#### References

<sup>[1]</sup> J. Chani-Cahuana, P. N. Landin, C. Fager and T. Eriksson, "Iterative
 Learning Control for RF Power Amplifier Linearization," in *IEEE Transactions
 on Microwave Theory and Techniques*, vol. 64, no. 9, pp. 2778-2789, Sept.
 2016, doi: 10.1109/TMTT.2016.2588483.

<!--NI_TOPIC bundle=rfmx-specan path=im.html language=enus -->
## TOPIC 00018: Intermodulation (IM)

- bundle_id: `rfmx-specan`
- source_path: `im.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan/raw/resource/enus/im.html
- document_id: `rfmx-specan`
- page_type: `leaf`
- content_type: `concept`
- source_description: One of the methods to characterize non-linearity of a device is to excite its input with a two-tone signal and measure the power of undesired distortion products that are generated at the output. While a single tone at the input of such DUT would generate harmonics at integer multiple of tone freque

### Intermodulation (IM)

One of the methods to characterize non-linearity of a device is to excite its input with a
 two-tone signal and measure the power of undesired distortion products that are generated at
 the output. While a single tone at the input of such DUT would generate harmonics at integer
 multiple of tone frequency, a two-tone signal, with tone frequencies at f<sub>1</sub> and
 f<sub>2</sub>, would generate distortion products at frequencies which are linear
 combination of f<sub>1</sub> and f<sub>2</sub>. Such distortion products are called
 intermodulation products or intermods. The following figure shows a spectrum containing
 fundamental tones and intermods.

[IMAGE alt='image' src='GUID-D2ABE034-1CC0-4208-AEED-5180F700BD79-a5.png']

The input-output voltage relationship of such non-linear devices can be expressed as a Taylor
 series as shown in the following equation:

[IMAGE alt='image' src='GUID-83F6B6F5-24CB-4724-80A8-3EB7D2FD02C4-a5.png']

[IMAGE alt='image' src='GUID-53D4C3ED-F2D3-404B-BE9F-818C1D93620A-a5.png']

Let the tone frequencies in the input signal be f<sub>1</sub> and f<sub>2</sub>, initial
 phases be φ<sub>1</sub> and φ<sub>2</sub> and amplitudes be a<sub>1</sub> and a<sub>2</sub>.
 You can calculate the input and output voltages using the following equations:

[IMAGE alt='image' src='GUID-62D9403F-1DFE-4233-8E5C-3D9343793634-a5.png']

[IMAGE alt='image' src='GUID-B05E9D79-FF1B-4B58-9D3C-66F5B503427E-a5.png']

The second order term in equation (3) generates second order harmonics and second order
 intermods. Similarly, the third order term generates third order harmonics and third order
 intermods. The following table lists the frequencies at which these distortion products are
 generated by first few terms in equation (3).

[IMAGE alt='image' src='GUID-681EF1A8-3277-4A96-B465-8613094DFFDD-a5.png']

In general, nth order term will generate harmonics and intermods at frequencies:

[IMAGE alt='image' src='GUID-88053D3A-FDB9-4EBF-B81E-E4C829453F1B-a5.png']

The third-order intermods at 2f<sub>1</sub>- f<sub>2</sub> and 2f<sub>2</sub>- f<sub>1</sub>
 lie close to the fundamental tones. The third-order intermods are followed by fifth-order
 components at 3f<sub>1</sub>-2f<sub>2</sub> and 3f<sub>2</sub>-2f<sub>1</sub>, followed by
 seventh-order components 4f<sub>1</sub>-3f<sub>2</sub> and 4f<sub>2</sub>-3f<sub>1</sub>, and
 so on. These consecutive odd order intermods are separated in frequency by the fundamental
 tone separation as shown in the following equation:

Δf = f<sub>2</sub> - f<sub>1</sub>

#### Intercept Points

The following figure shows the output power one of the fundamental tones and one of the
 third order intermods plotted against input power of the fundamental tone, provided that the
 two input tones are of equal power.

[IMAGE alt='image' src='GUID-9AE1E47E-B615-47EC-B255-0F8D361B47AC-a5.png']

These plots are straight lines for low input powers and deviate from the straight line
 behavior as input power is increased due to gain compression in real world DUTs. If these
 straight lines are extrapolated, they intersect at a theoretical point known as the third
 order intercept (IP<sub>3</sub> or TOI). At this
 point, the output power of the fundamental tone is equal to the output power of the third
 order intermod. This output power is called third order output intercept power
 (OIP<sub>3</sub>) and the corresponding tone input power is called third order input
 intercept power (IIP<sub>3</sub>).

In general, you can define IP<sub>n</sub>,
 IIP<sub>n</sub>, and OIP<sub>n</sub> points for any nth order intermod.
 The IM measurement computes only OIP<sub>n</sub> powers. The
 IP<sub>n</sub> point acts as a figure of merit
 when evaluating multiple DUTs, where a higher
 IP<sub>n</sub> DUT is expected to provide a better
 signal-to-distortion ratio.

When the input signal consists of two tones of unequal powers, the
 nth order intermods will be at different power levels. This can also
 happen when the frequency response of the DUT is not flat in the region of operation. This
 leads to two definitions of OIP<sub>n</sub>: nth order lower output
 intercept power (OIP<sub>n,lower</sub>)  and upper output intercept power
 (OIP<sub>n,upper</sub>) These intercept powers are computed using the following equations
 <sup>[2]</sup>.

[IMAGE alt='image' src='GUID-9F0EDB8B-AD51-41DC-8D16-7020D137F63F-a5.png']

where,

[IMAGE alt='image' src='GUID-22B54489-A1D1-478A-9FAA-82C13B2092D1-a5.png']

The
 intermod relative powers are computed as follows:

Δ

P

n

,

l

o

w

e

r

i

n

t

e

r

m

o

d

=

P

n

,

l

o

w

e

r

i

n

t

e

r

m

o

d

-

n

-

1

P

o

u

t

p

u

t

,

l

o

w

e

r

+

P

o

u

t

p

u

t

,

u

p

p

e

r

n

(

6

)

Δ

P

n

,

u

p

p

e

r

i

n

t

e

r

m

o

d

=

P

n

,

u

p

p

e

r

i

n

t

e

r

m

o

d

-

n

-

1

P

o

u

t

p

u

t

,

u

p

p

e

r

+

P

o

u

t

p

u

t

,

l

o

w

e

r

n

(

7

)

where,

ΔP<sub>n,lower intermod</sub> represents the lower intermod relative power for
 nth intermod

ΔP<sub>n,upper intermod</sub> represents the upper intermod relative
 power for nth intermod

#### Hardware Setup

Although a single generator can be used to generate a two-tone signal, the resultant signal
 may contain intermods generated by non-linear components of the generator itself. A better
 way to generate a clean two-tone signal is by using two independent generators with a power
 combiner. The following figure shows a typical hardware setup for IM measurement.

[IMAGE alt='image' src='GUID-1F3F930E-EC1D-4019-BC0A-7B8F0F1F28AA-a5.png']

The power combiner should have high return loss at all three ports, high isolation among
 the input ports and high reverse isolation from output port to the input ports. To further
 increase the return losses at the ports of the power combiner, you can use isolators or
 directional couplers.

Measurement Configuration

The RFmxSpecAn IM measurement allows you to configure two fundamental tone frequencies. You
 can configure the intermod frequencies by setting Auto Intermods Setup Enabled property to
 either True or False.

Auto Intermods Setup Enabled

When you set the Auto Intermods Setup Enabled property to True, the
 measurement auto-computes the intermod frequencies by using Maximum Intermod Order property,
 which you can set to either 3, 5, 7, or 9. This mode supports measurements of only odd order
 upper and lower intermods that are close to the fundamental tones. When you set the Auto
 Intermods Setup Enabled property to False, you can manually configure
 each intermod by setting intermod enabled/disabled, intermod order, intermod side, lower and
 upper intermod frequencies, and number of intermods. The measurement ignores the Maximum
 Intermod Order property in this mode. This mode allows measurement of even order intermods
 as well.

#### Measurement Method

The RFmxSpecAn IM measurement supports the following measurement methods to cater to
 multiple use cases:

- Normal —The RFmxSpecAn IM measurement acquires the spectrum using
 same signal analyzer settings across frequency bands. NI recommends this method when
 fundamental tone separation is not large and intermod powers are high enough to be
 measured accurately without using hardware specific optimizations like IF filters and IF
 gain. Supported Analyzers: PXIe-5644/5645/5646, PXIe-5663/5665,
 PXIe-5668
- Dynamic Range —Use this measurement method to maximize the dynamic
 range of digitizer when measuring low power intermods in presence of high power two-tone
 signal. The following are the relevant impairments reducing the dynamic range of the
 digitizer when measuring intermods: Note 
The tone separation should be more than the minimum IF filter bandwidth of the
 signal analyzer so that intermods can be isolated from tones before
 digitization.
No IF gain is applied when measuring fundamental tones.
IF filter used for an intermod may vary based on the signal analyzer and the
 proximity of that intermod to the fundamental tones. A narrowband IF filter is used
 for intermods close to the fundamental tones. A wider IF filter is used for
 intermods that are farther from the fundamental tones to reduce measurement
 time.
This method involves multiple acquisitions, with each tone and intermod having
 separate acquisition. Span of each acquisition is given by following equation: S
p
a
n
p
e
r

a
c
q
u
i
s
i
t
i
o
n
=
m
i
n
i
m
u
m

∆
f
,

1

M
H
z























(
8
) 
 Supported Analyzers: PXIe-5665, PXIe-5668
  - Quantization error due to the inability of using the full-scale of the digitizer.
 To utilize the full-scale of the digitizer more efficiently when measuring low power
 intermods, narrowband IF filters are used to isolate the intermod of interest while
 attenuating any power leakage from the two-tone signal. After knocking out the power
 leakage from the two-tones, sufficient IF gain is applied to the intermod, thereby
 increasing its power to match the full-scale of the digitizer.
  - Intermods generated by the digitizer due to the fundamental tones also impede its
 dynamic range. Dynamic Range measurement method eliminates the intermods generated by
 the digitizer by using narrowband IF filters while measuring the intermods, knocking
 out the high power fundamental tones before the signal reaches the digitizer.
- Segmented —This method is similar to Dynamic Range method, except
 that no hardware-specific optimizations are applied. This method acquires spectrum only
 around frequencies of interest, and is recommended when fundamental tone separation is
 large and measurement speed is desirable. The span of each segment is given by equation
 (8). Supported Analyzers: PXIe-5644/5645/5646, NI 5663/5665,
 PXIe-5668 Note Dynamic Range method is not
 supported when PXIe-5668 is used with PXIe-5698 preamp.

#### Recommended Settings

You can improve the dynamic range of the measurement by setting the RF input attenuation
 such that the mixer operates at optimal operating level. Refer to the dynamic range chart of
 the device mentioned in the device specification to know the optimum mixer level.

M

i

x

e

r

l

e

v

e

l

=

R

e

f

e

r

e

n

c

e

l

e

v

e

l

-

R

F

A

t

t

e

n

u

a

t

i

o

n

(

9

)

For a given reference level, RF attenuation can be varied to check if the distortion from
 first mixer in the signal analyzer has significant contribution to intermod generated by the
 DUT. Increasing RF attenuation decreases the power level at the first mixer, thereby
 reducing the distortion introduced by that mixer. If an increase in RF attenuation decreases
 the intermod power, then analyzer is contributing to the distortion. However, if intermod
 power remains constant with increase in RF attenuation, then the measured distortion can be
 attributed to the DUT.

#### References

<sup>[1]</sup>Egan, William F. Practical RF system design. John Wiley & Sons, 2004.

<sup>[2]</sup>Kundert, Ken. "Accurate and Rapid Measurement of IP2 and
 IP3."Designer’s Guide Consulting, 2006.

<!--NI_TOPIC bundle=rfmx-specan path=iterative-and-user-dpd.html language=enus -->
## TOPIC 00019: Iterative and User DPD

- bundle_id: `rfmx-specan`
- source_path: `iterative-and-user-dpd.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan/raw/resource/enus/iterative-and-user-dpd.html
- document_id: `rfmx-specan`
- page_type: `leaf`
- content_type: `concept`
- source_description: Iterative DPD performs DPD polynomial computation in multiple iterations. Each iteration involves a fresh acquisition of PA output signal and uses previous iteration’s DPD polynomial to compute current iteration’s polynomial. The NMSE result, which is an indicator of the predistortion modeling error

### Iterative and User DPD

Iterative DPD performs DPD polynomial computation in multiple iterations. Each iteration
 involves a fresh acquisition of PA output signal and uses previous iteration’s DPD
 polynomial to compute current iteration’s polynomial. The NMSE result, which is an
 indicator of the predistortion modeling error, can be monitored determine if the
 modeling error reduces with each iteration.

Note

<!--NI_TOPIC bundle=rfmx-specan path=marker.html language=enus -->
## TOPIC 00020: Marker

- bundle_id: `rfmx-specan`
- source_path: `marker.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan/raw/resource/enus/marker.html
- document_id: `rfmx-specan`
- page_type: `leaf`
- content_type: `concept`
- source_description: A marker is a utility to fetch the amplitude (y-location) and position (x-location) of a particular sample in a trace. You must select a measurement trace on which the marker operations need to be performed. Marker types are described in the following list: Off: No operation is done using this marke

### Marker

A marker is a utility to fetch the amplitude (y-location) and position (x-location) of a
 particular sample in a trace. You must select a measurement trace on which the marker
 operations need to be performed.

Marker types are described in the following list:

- Off: No operation is done using this marker.
- Normal: This marker is placed at the x-location that you specify on
 the trace. The amplitude of the sample is returned as the y-location.
- Delta: This marker is placed at the x-location that you specify
 relative to a reference marker on the trace. A reference marker can be another normal,
 delta, or a fixed marker. The amplitude of the sample relative to the amplitude of the
 reference marker is returned as the y-location.
- Fixed : This marker is placed at the x and y-locations that you
 specify. A fixed marker, unlike normal and delta markers, is not confined to the current
 trace but is free to move anywhere on the trace area. Once configured, this marker retains
 its position even if the trace gets updated.

The following figure shows the various marker types.

[IMAGE alt='image' src='GUID-FF44D825-0891-459E-BCD5-437252EC300C-a5.gif']

Note

- At least one delta marker must reference a normal or fixed marker.
- If the x-location that you specify for a normal or delta marker does not fit in the trace,
 "NAN" is returned as the y-location.
- You must configure the reference marker before configuring the delta
 marker.

#### Marker Functions

Peak Search

Peaks are defined as the samples for which the amplitude rises and falls around a threshold.
 The peak search function finds all the peaks in the trace and sets the marker to the highest
 peak.

Next Peak

The marker is moved to another peak, which can be either the next highest peak in the trace
 or a peak to the left or right of the current x-location.

Fetch XY

Returns the current x-location and the amplitude of the marker.

#### Peak Excursion

Peak excursion specifies the minimum amplitude variation required in a signal to be
 considered as a peak. Peak excursion is always specified with respect to a threshold value.
 A signal must rise and fall above threshold level by at least the peak excursion value to be
 considered as an eligible peak.

The following figure shows how to identify a valid peak that meets excursion criteria.
 [IMAGE alt='image' src='GUID-7B24C26A-1CF5-4412-8EA8-8EB5A2F2FFE5-a5.gif']

- Peak 1 rises and falls by at least the peak excursion value above the threshold. Hence,
 it follows the excursion criteria.
- Peak 2 is above the threshold level, but it does not rise and fall by the excursion
 value above the threshold level. Hence, it does not satisfy excursion criteria.
- Peak 3 rises above the threshold value by at least the excursion value, but it does not
 completely fall by the excursion value. The signal rises and crosses the peak 3 amplitude
 level. Hence, it is not an eligible peak.
- Peak 4 rises and falls by at least the peak excursion value above the threshold.
 Although during the rise it slightly falls (peak 3) the net rise from the threshold level
 exceeds the excursion value. Hence, it is considered an eligible peak.
- Peak 5 is below the threshold level. Hence, it is not detected as a peak.
- Peak 6 rises by at least the peak excursion value above the threshold. During the fall,
 signal slightly rises (as peak 7), but it does not rise above peak 6 amplitude level
 before falling again. The total fall, which starts at the peak 6 amplitude level, is more
 than the excursion value. Hence, it is an eligible peak.
- Peak 7 falls by the excursion value, but it does not rise by the excursion value. Hence,
 it does not satisfy excursion criteria.

<!--NI_TOPIC bundle=rfmx-specan path=measurement-methods.html language=enus -->
## TOPIC 00021: Measurement Methods

- bundle_id: `rfmx-specan`
- source_path: `measurement-methods.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan/raw/resource/enus/measurement-methods.html
- document_id: `rfmx-specan`
- page_type: `leaf`
- content_type: `concept`
- source_description: RFmx SpecAn provides Y-Factor and Cold Source methods for measuring the noise figure of a two port DUT. Noise figure measurement consists of two steps, calibration and measurement. Noise figure of the signal analyzer is measured during the calibration step, which is then used in the measurement step

### Measurement Methods

RFmx SpecAn provides Y-Factor and Cold Source methods for measuring the noise figure of a
 two port DUT.

Noise figure measurement consists of two steps, calibration and measurement. Noise figure
 of the signal analyzer is measured during the calibration step, which is then used in
 the measurement step.

#### Y-Factor Method

The Y-Factor method measures the insertion-gain [1] and the noise figure of the DUT with
 the help of a calibrated noise source.

Noise Source

A calibrated noise source is a broadband noise generator whose level is determined by the
 effective noise ratio (ENR) specific to the noise source module. The definition of
 effective noise ratio used by the noise source manufacturers to characterize a noise
 source is related to the power generated by the noise source when it is turned on.

The following equation describes the ENR specific to the noise source module.

[IMAGE alt='image' src='GUID-39181B4F-BD14-4B38-880A-AF698F13EBEE-a5.png']

where,

T<sup>HOT</sup> is the equivalent noise temperature, in kelvin, of the noise source when
 it is powered on

T<sub>0</sub> is 290 K

The definition of ENR used by the Y-Factor method, as shown in the following equation, is
 related to the difference between the noise power levels when the noise source is turned
 on versus when it is turned off.

[IMAGE alt='image' src='GUID-C832FE62-E139-413D-910C-04302DF4ABE1-a5.png']

T<sup>COLD</sup> is the calibration cold temperature specific to each noise source

If the ambient temperature during measurement, T<sup>OFF</sup> , is different from the
 calibration cold temperature, T<sup>COLD</sup>  of the noise source, the ENR is
 calculated as shown in the following equation:

[IMAGE alt='image' src='GUID-3CB36FB3-1106-41AF-88C3-8D250B3C6627-a5.png']

Y-Factor Calibration Step

A calibration step is required to remove the effect of noise generated by the signal
 analyzer on the reported noise figure of the DUT. In order to perform this calibration,
 the noise source is connected directly to the RF input port of the signal analyzer and
 two power measurements are performed, one with the noise source turned on and the other
 with noise source turned off.

The following figure shows the setup and signal model for NF calibration with a noise
 source.

[IMAGE alt='image' src='GUID-9A345D6A-0B91-4D84-8815-F8D881383528-a5.png']

During the calibration step, two types of losses that need to be considered are the noise
 source loss and the calibration loss. The signal path for the calibration step is shown
 in the following figure.

[IMAGE alt='image' src='GUID-89568D9B-C1F8-4198-AD2D-1415F5931E8D-a5.png']

The calibration Y-factor is defined as the ratio of the noise power measured when the
 noise source is turned on to the noise power measured when the noise source is turned
 off in the absence of the DUT from the signal path. The calibration Y-factor is defined
 in the following equation using the simplified signal model. Frequency notation in
 parenthesis is required for frequency converting DUTs, but can be removed for fixed
 frequency DUTs.

[IMAGE alt='image' src='GUID-F6805A61-0697-44D9-B9CA-03BD365A2C18-a5.png']

Here, [IMAGE alt='image' src='GUID-113578A6-03E3-4BD2-985B-809D5EE49CFB-a5.png'] and [IMAGE alt='image' src='GUID-7B8F6E8E-CA69-4CB5-8770-61F6C9263382-a5.png'] are the calibration step noise powers measured when noise source is
 turned on and off respectively.  T<sub>A</sub> is the equivalent noise temperature of
 the signal analyzer, which can be obtained by rearranging equation (17) as shown in the
 following equation:

[IMAGE alt='image' src='GUID-CC624AC5-A401-4E56-8744-5979D967927C-a5.png']

Y-Factor Measurement Step

In the measurement step, the noise source, DUT, and the signal analyzer are cascaded and
 two power measurements are made; one with the noise source turned on and the other with
 the noise source turned off.

[IMAGE alt='image' src='GUID-CAD0CFC2-AE06-4B80-8140-6F55FC74A43F-a5.png']

During the measurement step, the three types of losses that needs to be considered are
 the noise source loss, the DUT input loss, and output loss. The signal path for the
 measurement step is shown in the following figure.

[IMAGE alt='image' src='GUID-E052FBBE-3D18-4FB2-AAED-C908AC87403F-a5.png']

Measurement Y-Factor is defined as the ratio of noise power measured when the noise
 source is turned on to the noise power measured when the noise source is turned off when
 the DUT is present in the signal path. The measurement Y-factor is defined as shown in
 the following equation using the simplified signal model. Frequency notation in
 parenthesis is required for frequency converting DUTs, and can be removed for fixed
 frequency DUTs.

[IMAGE alt='image' src='GUID-D03AFF92-19FA-4263-833D-B1BAEE7734D7-a5.png']

For fixed frequency DUTs, the equation simplifies to

[IMAGE alt='image' src='GUID-0DAC3A8A-8513-4CFC-9BD5-1219C7230E3C-a5.png']

You can rearrange this as shown in the following equation:

[IMAGE alt='image' src='GUID-3B25E238-00EC-41F3-96DB-4DCB4E65B0A1-a5.png']

For fixed frequency DUTs, the equation simplifies to

[IMAGE alt='image' src='GUID-B4327C13-F538-465C-A712-359E91D5D5AD-a5.png']

The insertion gain, G<sub>D</sub>, of the DUT is obtained as shown in the following
 equation:

[IMAGE alt='image' src='GUID-E6F30588-1CF8-4E2D-B444-21193273B020-a5.png']

For fixed frequency DUTs, the equation simplifies to

[IMAGE alt='image' src='GUID-31ABC3CC-4508-4E60-8BC2-BB18111E84A9-a5.png']

Using equations (18), (19), (21), and (22), we can obtain the equivalent noise
 temperature, T<sub>D</sub>, of the DUT. Noise figure of the DUT can then be determined
 in dB as shown in the following equation:

[IMAGE alt='image' src='GUID-9504A8A8-13BE-48F8-A633-44B1DDC43BED-a5.png']

#### Cold Source Method

Cold source method of measuring noise figure does not rely upon a calibrated noise
 source. An RF termination is used as the noise source. The signal path for performing a
 cold source method based noise figure calibration, assuming that the characteristic
 impedance for the entire signal path is 50 ohms, is shown in the following figure.

[IMAGE alt='image' src='GUID-9F742204-5D13-4CFE-ABFF-4C615A429740-a5.png']

The signal path for performing a measurement on a DUT, assuming that the characteristic
 impedance for the entire signal path is 50 ohms, is shown in the following figure.

[IMAGE alt='image' src='GUID-FE6B3528-ABF3-4F2B-95BE-9FBACB6CD8C9-a5.png']

Unlike the Y-Factor method, the cold source method does not compute the power gain of the
 DUT by making power measurements. Instead, this method expects that the S-parameters of
 the DUT are already available. Using the S-parameters, the NF measurement derives the
 available-power-gain as shown in the following equations.

[IMAGE alt='image' src='GUID-108A6A45-6F9E-48E9-B66C-51003A715DEF-a5.png']

[IMAGE alt='image' src='GUID-F864B8FE-7F8C-4916-A396-849D31AA220B-a5.png']

[IMAGE alt='image' src='GUID-55BBAF16-C6E7-4C21-834D-EE727F830E8F-a5.png']

where s<sub>11</sub>, s<sub>12</sub>, s<sub>21</sub>, and s<sub>22</sub> are the
 scattering parameters of the DUT. Using the available-power-gain of the DUT and the
 power measured, noise figure of the DUT is computed.

Note

#### References

<sup>[1]</sup> Egan, William F. Practical RF system design. John Wiley
 & Sons, 2004.

<!--NI_TOPIC bundle=rfmx-specan path=measurement-settings.html language=enus -->
## TOPIC 00022: Measurement Settings

- bundle_id: `rfmx-specan`
- source_path: `measurement-settings.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan/raw/resource/enus/measurement-settings.html
- document_id: `rfmx-specan`
- page_type: `leaf`
- content_type: `concept`
- source_description: Sample Rate DPD measurement provides two modes for configuring the measurement sample rate, namely Reference Waveform and User. Reference Waveform mode uses the sampling rate of reference waveform for computation as well as application of DPD lookup table or polynomial. Measurement skips software re

### Measurement Settings

#### Sample Rate

DPD measurement provides two modes for configuring the measurement sample rate, namely
 Reference Waveform and User.

Reference Waveform mode uses the sampling rate of reference waveform for computation as
 well as application of DPD lookup table or polynomial. Measurement skips software
 resampling throughout signal processing chain.

User mode allows you to configure custom sample rate. Measurement enables software
 resampling before computing and applying DPD lookup table or polynomial.

The minimum recommended sample rate, expressed in samples per second, is given by:

[IMAGE alt='image' src='GUID-081485B3-8850-4617-886F-833A68ADA86D-a5.gif']

where,

B is the bandwidth of the signal in Hz,

and K is the highest order of PA non-linearity

#### Synchronization Method

For computing the gain and phase characteristics of the DUT, DPD measurement requires
 reliable time-synchronization between the acquired and reference waveforms.

DPD measurement provides two synchronization methods, Direct and Alias Protected.

Direct

This method synchronizes the acquired and reference waveforms with the assumption that
 the sample rate is high enough for preventing aliasing in intermediate nonlinear
 operations during the estimation of sub-sample delay between the two waveforms.

Alias Protected

This method synchronizes the acquired and reference waveforms while also ensuring that
 intermediate nonlinear operations during the estimation of sub-sample delay between the
 two waveforms are not affected by aliasing. This synchronization method should be used
 for the following test configurations:

- signal is either single-carrier or contiguous multi-carrier, and measurement sample
 rate is less than approximately three times the occupied-bandwidth.
- signal is non-contiguous multi-carrier and the component carriers are sparsely
 allocated in frequency.

This method uses the offset and bandwidth information of all component carriers
 comprising the signal. If you set the DPD Auto Carrier Detection Enabled property to
 True, the measurement auto detects the carrier offsets
 and bandwidths. If you set the DPD Auto Carrier Detection Enabled property to
 False, you must configure the carrier offsets and
 bandwidths by setting the DPD Number of Carriers, DPD Carrier Offset, and DPD
 Carrier Bandwidth properties.

The following diagram illustrates the offsets and bandwidths of the component carriers in
 a multi-carrier signal with a sample rate of
 F<sub>S</sub>(S/s).

[IMAGE alt='image' src='GUID-6A7A76DA-A44F-4C7B-A6AC-A406CAB636BA-a5.png']

#### Target Gain Type

The average gain of the predistorter and the PA, considered together as a linearized DUT,
 can be controlled by tweaking the gain of the predistorter. The following figure shows a
 simplified representation of the signal processing chain where PA is preceded by a
 predistorter.

[IMAGE alt='image' src='GUID-C99CB534-EF48-419A-AB7B-6A0CD2CD1EAD-a5.png']

DPD measurement supports three target gain types, namely
 Average Gain, Linear Region Gain and
 Peak Input Power Gain.

Average Gain

The predistorter is computed such that the average gain of the Predistorter + PA System
 is equal to the average gain of the PA.

Linear Region Gain

The predistorter is computed such that the average gain of the Predistorter + PA System
 is equal to the linear region gain of the PA.

Peak Input Power Gain

The predistorter is computed such that the average gain of the Predistorter + PA System
 is equal to the gain provided by the PA to all the samples in the reference waveform
 with power levels in the vicinity of the peak power level in the waveform.

The figure below shows the expected gain vs input power plot after DPD for various target
 gain types.

[IMAGE alt='image' src='GUID-511D09AA-219A-443F-B53E-54A89434FC92-a5.png']

#### Threshold and Curve Fit

NI recommends that the Log LUT-based DPD use the appropriate threshold settings to reject
 low-power, noise-corrupted samples. Polynomial curve fit order should typically be
 between 3 and 10. The recommended polynomial curve fit type is Least Absolute Residual.
 Use appropriate threshold settings to reject low power noise corrupted samples. The
 default threshold is set to -20 dB relative to the peak power of the acquired
 waveform.

<!--NI_TOPIC bundle=rfmx-specan path=memory-dpd.html language=enus -->
## TOPIC 00023: Memory DPD

- bundle_id: `rfmx-specan`
- source_path: `memory-dpd.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan/raw/resource/enus/memory-dpd.html
- document_id: `rfmx-specan`
- page_type: `leaf`
- content_type: `concept`
- source_description: In addition to being nonlinear devices, the instantaneous output of a power amplifiers is a function not only of the current signal amplitude and phase but also of the past signal amplitude and phase. This is commonly referred to as memory in a device. The following equation expresses the instantane

### Memory DPD

In addition to being nonlinear devices, the instantaneous output of a power amplifiers is
 a function not only of the current signal amplitude and phase but also of the past
 signal amplitude and phase. This is commonly referred to as memory in a device. The
 following equation expresses the instantaneous output.

[IMAGE alt='image' src='GUID-F63CE266-CBB5-4618-A757-BE7705FDF4F4-a5.gif']

[IMAGE alt='image' src='GUID-36DCBB75-2C6F-48BC-88BC-FFBB0C88D2C4-a5.gif']

The most general form that the nonlinear function can take is the Volterra Series. The
 following equation is a discrete version of Volterra Series <sup>[1]</sup>.

[IMAGE alt='image' src='GUID-3F851988-F372-4310-B832-199686C13F88-a5.gif']

[IMAGE alt='image' src='GUID-43AA0D1B-C62B-4F89-AED6-D526CEB34583-a5.gif']

To digitally compensate for memory and nonlinearity of the PAs, the most general
 structure of DPD also takes the same form as equation (4). While Volterra Series is the
 most general way of modeling DPD, extraction of large number of Volterra Kernels is
 usually both computationally intensive and unnecessary. Instead, many pruned versions of
 Volterra Series have been developed. DPD measurement in RFmx supports two such DPD
 models–Memory Polynomial Model and Generalized Memory Polynomial Model.

#### Memory Polynomial Model

PAs that display significant memory effects are not satisfactorily linearized using the
 LUT approach of DPD. Such PAs require compensation for memory effects. A well known
 structure for memory and nonlinearity compensation in PAs is the memory polynomial model
 <sup>[2]</sup>, the complex baseband representation of which is shown in the
 following equation.

[IMAGE alt='image' src='GUID-9FDC1B05-0673-442A-8AFF-8696A53226E0-a5.gif']

[IMAGE alt='image' src='GUID-E42E687F-C3C6-4780-9FC5-E550F24AA40A-a5.gif']

[IMAGE alt='image' src='GUID-BD2DFDA6-7709-47AB-A7CF-87EEEFAF70FE-a5.gif']

[IMAGE alt='image' src='GUID-A84CB830-3277-4E0A-9CD7-C88607297BEC-a5.png']

#### Generalized Memory Polynomial (GMP)

PAs that display significantly high memory effects are not completely linearized using
 memory polynomial. GMP <sup>[3]</sup> can be employed for such PAs. For the purpose of
 further discussion on GMP, we shall introduce the following terms:

| Expression | Type | Description |
| --- | --- | --- |
| x[n] | Signal | Signal value at the current time index |
| x[n-q] | Signal | Signal value q samples before the current time index |
| \|x[n]\|k | Envelope | Signal's kth order envelope of the signal x[n] |
| \|x[n-q]\|k | Envelope | Signal's kth order envelope of the signal x[n-q] |
| \|x[n-q-m]\|k | Envelope | Signal's kth order envelope lagging behind the signal x[n-q] by m samples |
| \|x[n-q+m]\|k | Envelope | Signal's kth order envelope leading the signal x[n-q] by m samples |

The following equation is a complex baseband representation of the GMP-based
 predistorter.

[IMAGE alt='image' src='GUID-1DB427FE-6141-4C88-B9A8-B223B7EA27A8-a5.gif']

[IMAGE alt='image' src='GUID-2CBE5F35-0D97-4243-8873-E70963B58E6F-a5.png']

The first double sum in GMP in equation (6) is exactly the same as MPM, capturing the
 memory effects and nonlinearity of the PA. The other two triple sums account for the lag
 and lead between the signal and envelope, compensating for the staggered memory effects
 of the cross terms.

The representation of DPD polynomial coefficients returned by the RFmx DPD measurement is
 as shown:

[IMAGE alt='image' src='GUID-518F7D84-0FCD-424A-87A8-9377B330EF49-a5.gif']

where each entry in the column vector is a column vector itself, represented as
 shown:

[IMAGE alt='image' src='GUID-43C776C5-96CD-459F-A6EA-ADAB70087A62-a5.gif']

#### References

<sup>[1]</sup> Schetzen, Martin. "The Volterra and Wiener theories of nonlinear systems." (1980).
 <sup>[2]</sup> Ding, Lei, et al. "Memory polynomial predistorter based on the indirect learning
 architecture." Global Telecommunications Conference, 2002. GLOBECOM'02. IEEE. Vol. 1.
 IEEE, 2002. <sup>[3]</sup> Morgan, Dennis R., et al. "A generalized memory polynomial model for
 digital predistortion of RF power amplifiers." Signal Processing, IEEE Transactions
 on54.10 (2006): 3852-3860.

<!--NI_TOPIC bundle=rfmx-specan path=memoryless-dpd.html language=enus -->
## TOPIC 00024: Memoryless DPD

- bundle_id: `rfmx-specan`
- source_path: `memoryless-dpd.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan/raw/resource/enus/memoryless-dpd.html
- document_id: `rfmx-specan`
- page_type: `leaf`
- content_type: `concept`
- source_description: Lookup Table Based DPD PAs with negligible memory effects can be easily linearized by suitably modifying or predistorting amplitude and phase of the complex baseband representation of the input signal. Lookup table (LUT) based DPD assumes that the instantaneous output power from the PA and the phase

### Memoryless DPD

Lookup Table Based DPD

PAs with negligible memory effects can be easily linearized by suitably modifying or
 predistorting amplitude and phase of the complex baseband representation of the input
 signal. Lookup table (LUT) based DPD assumes that the instantaneous output power from
 the PA and the phase distortion introduced by the PA are nonlinear functions of the
 instantaneous input signal power.

The input-output characteristics of a non-linear PA can be approximated by using a
 polynomial as shown in the following equations:

[IMAGE alt='image' src='GUID-A2EA367C-FE6F-4D40-B8C6-F0C877D8DBEB-a5.gif']

[IMAGE alt='image' src='GUID-D86D0BD2-87AD-45BF-B290-033AD95577DC-a5.gif']

LUT based digital predistortion coefficients can be computed in a logarithmic or a linear
 scale. The first step is obtaining the output power (dBm or watts) and phase distortion
 (degrees) vs. input power (dBm or watts) characteristics of the PA as expressed in
 equations (1) and (2) respectively. In the second step, we use these characteristics to
 create a predistortion lookup table which consists of complex correction factors and
 corresponding input powers (dBm or watts). The input powers in the lookup table are
 equally spaced in logarithmic or linear scale.

<!--NI_TOPIC bundle=rfmx-specan path=new-features-and-changes.html language=enus -->
## TOPIC 00025: RFmx SpecAn New Features and Changes

- bundle_id: `rfmx-specan`
- source_path: `new-features-and-changes.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan/raw/resource/enus/new-features-and-changes.html
- document_id: `rfmx-specan`
- page_type: `leaf`
- content_type: `concept`
- source_description: Learn about updates, including new features and behavior changes, introduced in each version of RFmx SpecAn. Discover what is new in the latest releases of RFmx SpecAn.If you cannot find new features and changes for your version, it might not include user-facing updates. However, your version might

### RFmx SpecAn
 New Features and Changes

Learn about updates, including new features and behavior changes, introduced in each
 version of RFmx SpecAn.

RFmx SpecAn

Note

Release Notes

Related information:

- Software and Driver Downloads

#### RFmx SpecAn
 2026 Q2 Changes

The RFmx SpecAn 2026 Q2 release includes behavior
 changes for Auto Level measurement interval handling and behavior changes with ACP
 measurements and Spectrum measurements that use the Sequential FFT measurement method. This
 release also adds support for the PXIe-5841 with 200 MHz bandwidth.

##### Behavior Changes

This version of RFmx SpecAn support for the following features:

- Auto level: Setting the Measurement Interval parameter to
 -1 causes the system to use a default value of 1 ms.
- Adjacent Channel Power (ACP) and Spectrum: When you use the Sequential
 FFT measurement method, you can configure the Configuring
 the Number of Analysis Threads property to a value greater than
 1.

##### New
 Hardware Support

This version of RFmx SpecAn
 adds support for the following hardware:

- PXIe-5841 ( 200 MHz ) bandwidth

#### RFmx SpecAn
 2026 Q1 Changes

Learn about new features, behavior changes, and other updates in RFmx SpecAn 2026 Q1.

This version of RFmx SpecAn adds support for the following
 features:

- Extended auto level functionality to work with Spectrum measurement configurations
 where the user does not have to provide the Bandwidth & Measurement
 interval.

#### RFmx SpecAn 2025 Q4 New Features and
 Changes

- Support for S2P file Load for Y-Factor Noise Source Loss, External Preamp Gain and
 S1P file for Cold Source Input Termination in Noise Figure (NF) measurements.

#### RFmx SpecAn 2025 Q3 New Features and
 Changes

- Support for Self-Cal Validity Check for PXIe-5860.
- Support for DDR Enabled and Linear Memory Depth properties in DVR DPD
 Measurement.
- Support for PowerList measurement.
- Support for S2P file load for Noise Figure (NF) measurement.
- Added Python API support.

#### RFmx SpecAn 2025 Q2 New Features and
 Changes

- Synchronization robustness improvements for periodic modulated waveform types in
 AMPM, DPD and IDPD measurements.

#### RFmx SpecAn 2025 Q1 New Features and
 Changes

- Updated minimal sample rate for NF measurement in 5840/1.
- Support for Threshold Definition in AMPM and DPD.
- Added support for FCnt in InstrumentStudio SpecAn.

##### Behavior Changes

- AMPM: Default threshold behavior changed from “Reference Waveform >= Threshold
 AND Acquired Waveform >= Threshold” to “X Axis Waveform >= Threshold” where X
 axis could be input or output waveform as decided by Reference Power
 Type configuration. To switch to previous behaviour, set the
 AMPM Threshold Definition property value to
 Input AND Output .
- DPD: Default threshold behavior in LUT DPD changed from “Reference Waveform >=
 Threshold AND Acquired Waveform >= Threshold” to “Reference Waveform >=
 Threshold”. To switch to previous behaviour, set the LUT DPD
 Threshold Definition property value to Input AND
 Output .

#### RFmx SpecAn 2024 Q4 New Features and
 Changes

- Added DVR extension for DPD functionality.
- Added support to reduce the IQ measurement overhead by not copying and storing the
 data in RFmx.

##### Behavior Changes

- Uninstalling RFmx SpecAn software also removes any previous versions of RFmx SpecAn
 .NET runtimes that were leaked in .NET Global Assembly Cache directory.

#### RFmx SpecAn 2024 Q3 New Features and
 Changes

- Support for PXIe-5860
- Support for Sequential FFT mode in Spectrum measurement

#### RFmx SpecAn 2024 Q2 New Features and
 Changes

- Support for Band Power Markers
- Obsoleted the RFmxInstr Load All Configurations VI. Use the
 RFmxInstr Load Configurations VI along with the appropriate
 RFmxInstr Load Options property, instead.

#### RFmx SpecAn 2024 Q1 New Features and
 Changes

- Support for Subspan Overlap in 5842 for Spectrum and Spur measurements

#### RFmx SpecAn 2023 Q4 New Features and Changes

- Support for a new Marker Type called Fixed within the Markers
- Support for IM results in dBc
- Speed enhancements in the Equalizer Train mode of the IDPD Measurment
- Support for obtaining unprocessed I/Q data utilized for RFmx measurements

#### RFmx SpecAn 2023 Q3 New Features and
 Changes

- Iterative Learning Control for DPD measurement
- Support for Noise Compensation in ACP measurement for Sequential FFT mode
- Added support for saving and loading RFmx configurations into/from rfmxconfig files.
 Load from TDMS is supported but save into TDMS files is discontinued.

<!--NI_TOPIC bundle=rfmx-specan path=nf.html language=enus -->
## TOPIC 00026: Noise Figure (NF)

- bundle_id: `rfmx-specan`
- source_path: `nf.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan/raw/resource/enus/nf.html
- document_id: `rfmx-specan`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Noise Figure measurement requires license activation. If you install RFmx SpecAn but do not activate the Noise Figure measurement license, you will have 30 days from the first time you use the measurement to evaluate it. Introduction Fidelity of electromagnetic circuits is most commonly compromi

### Noise Figure (NF)

Note

#### Introduction

Fidelity of electromagnetic circuits is most commonly compromised by, among other
 impairments, the noise generated by the components constituting the circuit. For
 example, additive thermal white noise (also called Johnson-Nyquist noise) is
 generated by any electronic component whose temperature is above absolute 0 K. An
 ideal resistance of R ohms generates voltage v<sub>n</sub> in a bandwidth
 B Hz (see <sup>[1]</sup> and <sup>[2]</sup>)

[IMAGE alt='image' src='GUID-2C0F5D64-7167-4F4D-BE29-8E0E6DA71BD6-a5.png']

where k<sub>B</sub> = 1.38 * 10<sup>-23</sup>m<sup>2</sup>kg
 s<sup>-2</sup>K<sup>-1</sup> is the Boltzmann
 constant.

The relevant figure of merit of signal fidelity is called the signal-to-noise ratio
 (SNR), which is the ratio of power of the desired signal (P<sub>s</sub>) to the power of
 the noise affecting the quality of the signal (N<sub>s</sub>) in watts. SNR is
 calculated as shown in the following equation.

[IMAGE alt='image' src='GUID-E66AE51E-52C6-4A81-968A-C6BF4FECF169-a5.png']

Since every electrical component adds some additive thermal noise to the signal, the
 signal fidelity at the input port of the electrical component is bound to be better than
 at the output port. This degradation in signal fidelity is characterized by the noise
 factor of the electrical component, defined as shown in the following equation.

[IMAGE alt='image' src='GUID-9BD7CA1F-7E64-4BEE-90DD-B5933B13C93E-a5.png']

The following equation shows the noise factor of an electrical component with power gain,
 G.

[IMAGE alt='image' src='GUID-11CE6F48-DC18-4047-8463-6120A15C407F-a5.png']

where,

N<sub>S</sub> is the power of the noise at the input port of the DUT

G(N<sub>S</sub>+N<sub>D</sub>) is the power of the noise at
 the input port of the DUT

N<sub>D</sub> is the noise power added by the DUT referred at its input plane

The following figure describes the additive DUT noise:

[IMAGE alt='image' src='GUID-5540B707-1306-47C5-80E5-91C2FD0981F4-a5.png']

In order to standardize the definition of noise factor, the source noise power is always
 considered to be equal to N<sub>0</sub>, defined as shown in the following equation.

[IMAGE alt='image' src='GUID-442FD97D-6100-4D15-983C-38EF9C57BF65-a5.png']

where T<sub>0</sub>=290 K

The standardized definition of noise factor is calculated as shown in the following
 equation.

[IMAGE alt='image' src='GUID-F50F1ED0-50C8-4637-A6E5-2D608B8E5939-a5.png']

Noise figure is defined as the log of noise factor as shown in the following
 equation.

[IMAGE alt='image' src='GUID-B78C2AFF-F1F8-4A62-A6BB-0E2D7FF0809A-a5.png']

The noise temperature of an electronic component is figure of merit equivalent to its
 noise figure. The noise temperature is defined as shown in the following equation.

[IMAGE alt='image' src='GUID-090DD419-5532-4AB3-AA62-B889184AFE6B-a5.png']

Using (6) and (8),  you can expressFas shown in the following
 equation:

[IMAGE alt='image' src='GUID-F6742FE3-1869-4647-8F1F-89AD1BAAC184-a5.png']

For an ideal resistive loss element it can be shown that its noise factor is determined
 by its physical temperature (T<sub>Loss</sub>) and the power loss (L)
 of the resistive element [4].

[IMAGE alt='image' src='GUID-F2A6C1A0-26F2-44B9-BCA3-A9BE023C4E75-a5.png']

For a cascade of electrical components, each with different power gains and noise
 factors/temperatures, Friis concluded that the noise factor or temperature of the
 cascade can be expressed as shown in the following equations:(see [3])

[IMAGE alt='image' src='GUID-3C092C25-6832-4CFC-85E6-C70A32807FC7-a5.png']

The following figure shows a cascade of electronic components with different noise
 factors and power gains:

[IMAGE alt='image' src='GUID-2B1B9F9C-7E3A-40BA-9D40-B18BD83C7832-a5.png']

The gain values used in the equations (11a) and (11b) correspond to available-power-gain
 [4] of the two port DUT.

#### References

<sup>[1]</sup> Nyquist, Harry. "Thermal agitation of electric charge in
 conductors." Physical review 32.1 (1928): 110.

<sup>[2]</sup> Abbott, Derek, et al. "Simple derivation of the thermal noise formula
 using window-limited Fourier transforms and other conundrums." Education,
 IEEE Transactions on 39.1 (1996): 1-13.

<sup>[3]</sup> Friis, Harald T. "Noise figures of radio receivers." Proceedings of
 the IRE 32.7 (1944): 419-422.

<sup>[4]</sup> Egan, William F. Practical RF system design. John
 Wiley & Sons, 2004.

<!--NI_TOPIC bundle=rfmx-specan path=noise-compensation-algorithm.html language=enus -->
## TOPIC 00027: Noise Compensation Algorithm

- bundle_id: `rfmx-specan`
- source_path: `noise-compensation-algorithm.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan/raw/resource/enus/noise-compensation-algorithm.html
- document_id: `rfmx-specan`
- page_type: `leaf`
- content_type: `concept`
- source_description: Compensates for noise during 5G NR signal testing, ensuring precise modulation metrics and reliable RFmx SpecAn measurements. Noise compensation details are described by assuming the following model test setup. When the switch connects to the DUT path, the noise power measured by the signal analyzer

### Noise Compensation Algorithm

Compensates for noise during 5G NR signal testing, ensuring precise modulation
 metrics and reliable RFmx SpecAn measurements.

Noise compensation details are described by assuming the following model test setup.

[IMAGE alt='image' src='GUID-4EBE318B-E506-409B-BB62-CE6A6F4B6977-a5.png']

When the switch connects to the DUT path, the noise power measured by the signal
 analyzer, P<sub>MEAS</sub>, is

P<sub>MEAS</sub> =
 P<sub>DUT</sub> +
 P<sub>ANALYZER</sub>    (1)

where P<sub>DUT</sub> denotes the average noise
 power of the DUT, and P<sub>ANALYZER</sub> denotes
 the noise power of the signal analyzer and the switch.

When the switch is connected to a 50 Ω termination path, the average noise power measured
 by the signal analyzer is

P<sub>CAL</sub> = kTB +
 P<sub>ANALYZER</sub>    (2)

where k = 1.38 × 10<sup>-23</sup> m<sup>2</sup>kg s<sup>-2</sup>K<sup>-1</sup>
 is the Boltzmann constant, T = 290 K is the approximate
 room/reference temperature, and B is the bandwidth, in Hz, over which
 power measurements are done.

Equations (1) and (2) assume that the analyzer's noise power
 (P<sub>ANALYZER</sub>) is uncorrelated
 with the DUT noise power (P<sub>DUT</sub>) and the
 noise added by the 50 Ω termination.

When you set the Noise Compensation Type property to Analyzer Only, the DUT noise power
 is

P<sub>DUT</sub> ← kTB +
 max{P<sub>MEAS</sub> –
 P<sub>CAL</sub>,0.0630957 ×
 P<sub>CAL</sub>}    (3A)

When you set the Noise Compensation Type property to Analyzer and Termination, the
 portion of the DUT noise power that is in excess of the thermal noise floor,
 kTB, is

P<sub>DUT</sub> ←
 max{P<sub>MEAS</sub> –
 P<sub>CAL</sub>, 0.0630957 ×
 P<sub>CAL</sub>}     (3B)

Note

1. Noise powers P MEAS and
 P CAL are random variables
 and therefore it is possible that
 P MEAS –
 P CAL may turn out to be
 less than or equal to zero. To avoid returning absurd results, powers reported
 after noise compensation are never allowed to fall to values less than 0.0630957
 × P CAL , that is, 12 dB less
 than P CAL on a logarithmic
 scale.
2. When you set the Noise Compensation Type property to Analyzer and
 Termination , the reported DUT power can be lower than the
 thermal noise floor of kT or –174 dBm/Hz. The reported power
 should be interpreted to be in excess of the thermal noise floor of –174
 dB/Hz.

#### Measurement Guidelines

The general flow of spectral measurements with noise compensation is shown in the
 following figure.

[IMAGE alt='image' src='GUID-08738243-6F3C-4181-B721-3E980095B0CE-a5.png']

For the PXIe-5668 with PXIe-5698 Preamplifier Module,
 when you perform spectral measurements with noise compensation, RFmx throws an
 exception, as illustrated:

[IMAGE alt='image' src='GUID-0135E382-F98E-4051-93D8-5FBC77EFA489-a5.png']

For
 PXIe-5644, 5645, 5646, and 5820 devices, when you perform spectral measurements with
 noise compensation, RFmx throws an exception, as illustrated:

[IMAGE alt='image' src='GUID-4DA7EFAB-D552-43E2-81E3-8F710CFDE1DA-a5.png']

Recommended Settings

1. Noise added by the signal analyzer reduces with reduction in RF Attenuation.
 Keep the instrument’s RF Attenuation as low as possible.
2. Enabling RF Preamplifier also reduces the noise figure of the signal analyzer.
 Whenever possible, enable the RF Preamplifier.

#### Noise Compensation
 Guidelines

When performing noise compensation in a measurement, it is crucial to understand the
 different signal analyzer parameters that affect the noise calibration. In order to
 achieve the noise compensated measurement result, same parameter values for noise
 calibration and noise compensation must be maintained. The properties that you use
 for calibration changes depending on the hardware used. The following table lists
 the RFmx properties for calibration and their corresponding hardware.

| Hardware | RFmx Noise Calibration Properties |
| --- | --- |
| PXIe-5830/PXIe-5831/PXIe-5832 | Center Frequency, Selected Port, LO Source, Downconverter Frequency/Downconverter Frequency Offset, Reference Level, Reference Level Headroom, Preamp Enabled, Cleaner Spectrum, Optimize Path for Signal Bandwidth, External Attenuation, Thermal Correction Headroom Range, Gain from S-Parameter, and Averaging Count |
| PXIe-5603, PXIe-5605, PXIe-5665, PXIe-5668 | Center Frequency, Downconverter Frequency/Downconverter Frequency Offset, Reference Level, Preamp Enabled, Cleaner Spectrum, and Averaging Count |
| PXIe-5601, PXIe-5663E | Center Frequency, Downconverter Frequency/Downconverter Frequency Offset, Reference Level, and Averaging Count |

#### Noise Calibration Database

The noise calibration database is a storage that RFmx maintains to store all the noise
 calibration data. This database is maintained individually for each device. Based on the
 device used, the noise calibration data is stored to their respective databases.

#### Validate Noise Calibration
 Database

RFmx provides a utility to check whether noise data is present in the database for
 the given configuration. This utility references an initialized RFmx session and
 checks the noise calibration database using the specified configuration. This
 utility does not require a Measurement Initiate or Commit to be called to obtain the
 status. It returns True if the noise data is present, else it returns False based on
 either of the following conditions:

1. Calibration data is not present for the specified configuration
2. Difference between the current device temperature and the device temperature at
 which calibration was performed is beyond the [–5°C, +5°C] range

This utility does not return error if the noise data is not present, but it
 returns error for the following conditions:

1. Using this utility on a session initialized as AnalysisOnly mode.
2. Using this utility on a session initialized with a device that does not support
 noise compensation

#### Clear Noise Calibration
 Database

RFmx provides a utility to clear all the noise calibration database entries. Calling
 the Clear Noise Calibration Database utility clears all the noise calibration data
 associated with the device, including the data in the current session. This utility
 depends on the Noise Calibration Mode property that you configure on the RFmx
 session. For the same device, RFmx maintains two different databases based on the
 Noise Calibration Mode property (Manual/Auto). You must set the Noise Calibration
 Mode property before calling the Clear Noise Calibration database utility to select
 the database to be cleared.

While performing self-calibration on a device,
 clear the already existing noise database. This ensures that the previous noise data
 before the self-calibration is not considered. This utility does not return any
 error if there is no existing calibration database to be cleared.

#### Manual Noise Calibration Using C
 and .NET APIs

Noise calibration, in the context of noise compensation for spectral measurements
 such as ACP and others, involves noise statistics estimation of the signal analyzer.
 While performing noise calibration, RFmx estimates and saves all relevant noise
 statistics to a file on the disk. As long as the RFmx session is kept alive, the
 noise calibration data, including traces, are cached in the program memory. Data is
 saved to disk only when the RFmx session is closed, and the cached data is purged
 from the memory.

Noise spectrum traces are a notable exception to the data
 saved on the disk considering limiting the noise-calibration file on disk from
 growing to unreasonably big sizes. Therefore, to ensure that spectral measurements
 trace results are noise-compensated, you must perform noise calibration and
 measurement in the same process. Under such conditions, RFmx uses noise calibration
 data cached in the program memory, instead of retrieving it from a file on the
 disk.

This constraint of performing noise calibration and measurement in the
 same process is not applicable if traces are irrelevant to your tests, and therefore
 you set the All Traces Enabled property to
 False. Disabling traces is helpful in scenarios where the
 execution speed of tests is critical.

<!--NI_TOPIC bundle=rfmx-specan path=noise-fundamentals.html language=enus -->
## TOPIC 00028: Noise Fundamentals

- bundle_id: `rfmx-specan`
- source_path: `noise-fundamentals.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan/raw/resource/enus/noise-fundamentals.html
- document_id: `rfmx-specan`
- page_type: `leaf`
- content_type: `concept`
- source_description: Introduces key concepts of noise in RF measurements, explaining its impact on 5G NR signal analysis and accuracy in RFmx SpecAn testing workflows. Thermal Noise Fidelity of electromagnetic circuits is most commonly compromised by the noise generated by the components constituting the circuit, among

### Noise Fundamentals

Introduces key concepts of noise in RF measurements, explaining its impact on 5G NR
 signal analysis and accuracy in RFmx SpecAn testing
 workflows.

#### Thermal Noise

Fidelity of electromagnetic circuits is most commonly compromised by the noise
 generated by the components constituting the circuit, among other impairments,. For
 example, additive thermal white noise (also called Johnson-Nyquist noise) is
 generated by any electronic component whose temperature is above absolute 0 K. An
 ideal resistance of R ohms at temperature T
 Kelvin generates a thermal-noise RMS voltage v<sub>n</sub> in a bandwidth
 B Hz, given by the following expression (see <sup>[1]</sup>
 and <sup>[2]</sup>).

[IMAGE alt='image' src='GUID-794118B2-27BD-4B72-B241-821E857D026D-a5.png']

where k = 1.38 × 10<sup>-23</sup> m<sup>2</sup>kg
 s<sup>-2</sup>K<sup>-1</sup> is the Boltzmann constant.

#### The -174 dBm/Hz Noise
 Floor

Consider the following circuit diagram.

[IMAGE alt='image' src='GUID-D30AEF63-CA67-4FCF-A6E1-69DE384D3CA5-a5.png']

The power delivered to the load resistance
 R<sub>L</sub> is obtained as shown in
 the following equation.

[IMAGE alt='image' src='GUID-9F7840EC-5AD9-4014-929E-542F23872188-a5.png']

Maximum power is transferred to the load when the load impedance matches the
 source impedance, that is, when R<sub>L</sub>
 = R.

Using
 v<sub>n</sub> from (1), we get the
 expression for maximum noise power,
 P<sub>MAX</sub>, delivered from a noisy
 resistor to a matched noiseless load.

[IMAGE alt='image' src='GUID-8A97BF5B-CB50-4FA1-8E4A-661223789589-a5.png']

Power spectral density, kT, is obtained as the ratio between
 delivered power and bandwidth. At a reference temperature of 290 K, this power
 spectral density expressed in dBm/Hz is obtained as shown:

[IMAGE alt='image' src='GUID-F32649E8-54B9-4015-8A7F-BD417A838DA8-a5.png']

This is the often cited -174 dBm/Hz noise floor of RF and microwave devices.

#### General Two Port Networks Noise
 Model

Consider the following noise model:

[IMAGE alt='image' src='GUID-59637E8B-371B-4803-A357-BA4AE8A04048-a5.png']

The terms used in the model and other related terms are defined in the following
 table.

| Term | Definition |
| --- | --- |
| IS | Source intrinsic noise current |
| YS | Source admittanceImpedance is ZS = 1/YSConductance GS and susceptance BS are related to admittance as YS = GS + BS |
| VA | Analyzer intrinsic noise voltage |
| RA | Fictitious equivalent noise resistance such that E{\|VA\|2 } = 4kT0RAB in a bandwidth B Hz |
| rA | Normalized fictitious equivalent noise resistance such that rA = RA/Z0, where, Z0 is the characteristic impedance, usually 50-ohms |
| IU | Analyzer uncorrelated intrinsic noise current |
| GU | Fictitious equivalent noise conductance such that E{\|IU\|2 } = 4kT0GUB in a bandwidth B Hz |
| IC | Analyzer correlated intrinsic noise current |
| YC | Fictitious admittance, relating the analyzer’s intrinsic noise voltage to the correlated noise current such that IC = VAYC. Fictitious equivalent noise conductance, GC, and fictitious equivalent noise susceptance, BC, are related to admittance as YC = GC + jBC |
| YL | Analyzer load admittance |
| Γ | Reflection coefficient. Related to impedance and characteristic impedance as |

It can be shown that the noise factor of the signal analyzer when presented
 with a source with reflection coefficient, Γ<sub>S</sub> is (see
 [3], [4])

[IMAGE alt='image' src='GUID-86934DB8-187B-491C-86F1-89ED72A8A413-a5.png']

where

- Γ OPT is the optimal source impedance, resulting in the minimum
 possible noise factor for the signal analyzer. This is easily verified by
 evaluating F (Γ S )/ Γ S by setting
 Γ S to Γ OPT .
 Complete description of the noise factor of the signal analyzer using this
 equation requires estimation of the unknown parameters
 F MIN ,
 r A , and
 Γ OPT .

Refer to the *Derivation: Noise Factor of Two Port Networks* section
 for detailed derivation of these parameters.

Noise figure of the signal
 analyzer characterizes how the signal-to-noise ratio (SNR) degrades as a function of
 source impedance. However, for noise compensation, the noise power delivered to the
 signal analyzer load, denoted by admittance,
 Y<sub>L</sub>, is the quantity of
 interest and not the degradation in SNR.

The total noise power delivered to
 the signal analyzer load is a superposition of the noise power delivered by the
 source noise current source (I<sub>S</sub>), analyzer noise
 voltage (V<sub>A</sub>), analyzer uncorrelated noise current
 (I<sub>U</sub>), and analyzer correlated
 noise current I<sub>C</sub> =
 V<sub>A</sub>Y<sub>C</sub>.

[IMAGE alt='image' src='GUID-BB38B349-C59E-4948-87AD-373D67BA74AE-a5.png']

Write the noise current (I<sub>IN</sub>) as
 a superposition of noise current due to the source
 (I<sub>IN;S</sub>) and the analyzer
 (I<sub>IN;A</sub>).

[IMAGE alt='image' src='GUID-75AC728A-23C7-4FA1-86DE-48EFFDF9EC5A-a5.png']

where

[IMAGE alt='image' src='GUID-B0F6FFED-853F-4FB1-9369-627824582F4E-a5.png']

and

[IMAGE alt='image' src='GUID-F91DC4D6-419D-4309-BDD0-262A88B2C054-a5.png']

Noise power delivered to the signal analyzer
 load(Y<sub>L</sub>) that can be
 attributed to the signal analyzer is proportional to
 E{|I<sub>IN;A</sub>|<sup>2</sup>},
 where E{·} denotes the statistical expectation operator, and is expressed by the
 following equation:

[IMAGE alt='image' src='GUID-DF34D2B4-3FA1-467E-97C1-FB1CA8EFA090-a5.png']

Using the expressions for mean squared thermal noise currents and voltages
 measured over bandwidth B Hz, we get the following
 expression:

[IMAGE alt='image' src='GUID-4D575BBC-24A3-4629-8123-7FD26D92FF89-a5.png']

This shows that the noise power attributed to the signal analyzer, delivered to
 the load is a function of the source impedance.

For example, an RF short
 source (infinite admittance, Y<sub>S</sub> =
 ∞) results in mean squared noise current:

[IMAGE alt='image' src='GUID-35F76078-5A16-471D-8552-D081D066A55F-a5.png']

and an RF open source (zero admittance,
 Y<sub>S</sub> = 0) results in a mean
 squared noise current:

[IMAGE alt='image' src='GUID-1D458567-D0D2-4292-BB0B-8F9DFA744371-a5.png']

Note

#### Derivation: Noise Factor of Two
 Port Networks

For the noise model depicted in the previous section, we can see that the total noise
 current delivered to the analyzer is a superposition of the intrinsic noise current
 in the source, the intrinsic noise voltage of the analyzer, the intrinsic
 uncorrelated noise current of the analyzer and the intrinsic correlated noise
 current of the analyzer.

[IMAGE alt='image' src='GUID-FB86050C-AB49-475E-9C8C-183C1E31D788-a5.png']

By substituting the correlated intrinsic noise current of the analyzer
 I<sub>C</sub> =
 Y<sub>C</sub>V<sub>A</sub>,
 where Y<sub>C</sub> is a fictitious admittance
 representing the correlation between
 I<sub>C</sub> and
 V<sub>A</sub>, we get the expression
 for the total input current:

[IMAGE alt='image' src='GUID-805B843D-9BAE-42C9-B232-C16A32699F2D-a5.png']

Using the statistical expectation operator, E{·}, the average
 noise power measured by the analyzer is as shown in the following expression:

[IMAGE alt='image' src='GUID-3034ACDE-6055-4158-93AF-550527EF6F1A-a5.png']

Using the expressions for mean squared thermal noise currents and voltages
 measured over bandwidth B Hz, we get

[IMAGE alt='image' src='GUID-ED799FBD-F945-4559-A43E-2B69BE432FB6-a5.png']

Similarly, in absence of any noise in the analyzer, the noise power delivered to
 the load from the source noise is given by the following expression:

[IMAGE alt='image' src='GUID-B844D10E-F166-4ACA-AF14-FE68A01CCE61-a5.png']

By the definition of noise factor,

[IMAGE alt='image' src='GUID-1949606C-B57F-45EA-AE1D-855EA7E16B78-a5.png']

Selecting appropriate source conductance
 (G<sub>S</sub>) and source susceptance
 (B<sub>S</sub>) minimizes the analyzer
 noise factor, F.

Clearly, optimal
 B<sub>S</sub> would be equal to
 -B<sub>C</sub>.

Thus,
 B<sub>OPT</sub> ≔
 -B<sub>C</sub>

To optimize noise
 factor with respect to G<sub>S</sub>, set the
 partial derivative to zero.

[IMAGE alt='image' src='GUID-91B74870-02FD-4890-9AAA-F4AEE3867442-a5.png']

Thus, optimal source conductance,
 G<sub>S</sub>, for minimizing noise factor
 is

[IMAGE alt='image' src='GUID-82C3374C-1F21-41A5-BD6C-79522FD102FA-a5.png']

and the optimal source admittance,
 Y<sub>S</sub>, is

[IMAGE alt='image' src='GUID-957BC067-44D8-4C94-8B35-6E7AF2945252-a5.png']

With optimal source admittance, the minimum noise factor is

[IMAGE alt='image' src='GUID-08A4BC2C-F059-403A-94C6-83CA8E410ED5-a5.png']

Eliminating G<sub>U</sub> from the minimum
 noise factor (F<sub>MIN</sub>) expression by
 re-writing the following expression for
 G<sub>U</sub>:

[IMAGE alt='image' src='GUID-4413C623-6241-41A9-B6F0-7AF8D336EC7D-a5.png']

Thus,

[IMAGE alt='image' src='GUID-41A83ED0-7272-4407-AA16-1DB1B6BF0427-a5.png']

Re-writing noise factor, F, in terms of
 F<sub>MIN</sub>:

[IMAGE alt='image' src='GUID-D24197D9-3A87-4AE2-8493-D0DC5FAF9D71-a5.png']

Again, eliminating G<sub>U</sub>,

[IMAGE alt='image' src='GUID-23D267B0-5542-42C1-9288-851C165322D9-a5.png']

or,

[IMAGE alt='image' src='GUID-BB5ED0AC-40D3-4CB7-822E-EA22C7D039B7-a5.png']

Normalizing with respect to characteristic impedance, noting that any normalized
 admittance, y, is

[IMAGE alt='image' src='GUID-DDCCE462-F715-4F16-AE63-CA4F031F3C6A-a5.png']

Thus, we arrive at the desired expression for noise factor of the analyzer as a
 function of source reflection coefficient, Γ<sub>S</sub>:

[IMAGE alt='image' src='GUID-E2B6D91B-EFB5-4040-B0B9-45DEBEBE9796-a5.png']

#### References

<sup>[1]</sup> Nyquist, Harry. "Thermal agitation of electric charge in
 conductors." Physical review 32.1 (1928): 110.

<sup>[2]</sup> Abbott, Derek, et al. "Simple derivation of the thermal noise formula
 using window-limited Fourier transforms and other conundrums." Education,
 IEEE Transactions on 39.1 (1996): 1-13.

<sup>[3]</sup> Harter,
 Alphonse. "LNA matching techniques for optimizing noise figures." RF
 design 2.03 (2003).

<sup>[4]</sup>S. Long.  "Design of Low Noise Amplifiers
 (https://www.ece.ucsb.edu/~long/ece145a/LNAdesign.pdf)", UC Berkeley(2007).

<!--NI_TOPIC bundle=rfmx-specan path=obw.html language=enus -->
## TOPIC 00029: OBW

- bundle_id: `rfmx-specan`
- source_path: `obw.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan/raw/resource/enus/obw.html
- document_id: `rfmx-specan`
- page_type: `leaf`
- content_type: `concept`
- source_description: Occupied bandwidth (OBW) measures the bandwidth that occupies a certain power specified as a percentage of the total power in the acquired spectrum. A spectrum is configured for span, resolution bandwidth, and sweep time. The total power is measured after RBW filtering and averaging. Then, the start

### OBW

Occupied bandwidth (OBW) measures the bandwidth that occupies a certain power specified
 as a percentage of the total power in the acquired spectrum. A spectrum is configured
 for span, resolution bandwidth, and sweep time. The total power is measured after RBW
 filtering and averaging. Then, the start and stop frequencies are measured such that the
 power in this occupied bandwidth is equal to percentage of the total power that you
 specify. The power units are reported in dBm (average total power) or dBm/Hz (power
 spectral density).

The following figure shows the spectrum span and OBW.

[IMAGE alt='image' src='GUID-2BACD07B-2EE4-41DC-82D4-033EDE44BBB4-a5.png']

#### RBW and Sweep Time

When you set the OBW RBW Auto property to True, the measurement
 sets the RBW using the following ratio:

Span:RBW<sub>3dB</sub> = 100, where RBW<sub>3dB</sub> is a value
 between 1 Hz and 1 MHz

When you set the OBW Sweep Time Auto property to True, the
 measurement sets the sweep time to the following values:

- k/RBW 3dB when the RBW filter is FFT based, where k is
 a constant which depends on the FFT window
- 10/RBW 3dB for other RBW filter types

|  | Note The standard specific OBW measurement does not support configuring all the properties and fetching all the results mentioned in this topic. The standard specific measurements do not expose some properties whose settings are specified by the standard or are not relevant to the standard. |
| --- | --- |

Related concepts:

- Spectral Measurements Concepts

<!--NI_TOPIC bundle=rfmx-specan path=pavt.html language=enus -->
## TOPIC 00030: Phase and Amplitude versus Time (PAVT)

- bundle_id: `rfmx-specan`
- source_path: `pavt.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan/raw/resource/enus/pavt.html
- document_id: `rfmx-specan`
- page_type: `leaf`
- content_type: `concept`
- source_description: PAVT measures the phase and amplitude at the DUT ports for beamforming applications. Beamforming is used for directional transmission or reception of radio signals. The direction of transmission or reception is controlled by changing the phase and amplitude of the signal at each antenna port. PAVT i

### Phase and Amplitude versus Time
 (PAVT)

PAVT measures the phase and amplitude at the DUT ports for beamforming applications.

Beamforming is used for directional transmission or reception of radio signals. The
 direction of transmission or reception is controlled by changing the phase and amplitude
 of the signal at each antenna port. PAVT is used to measure the accuracy of the phase
 and amplitude changes introduced at the antenna ports by the beamforming DUT.

The following block diagram depicts the transmit path testing of a typical bidirectional
 beamforming DUT. The setup would have one RF In or IF In port and multiple RF Out
 ports.

[IMAGE alt='image' src='GUID-F7AEC2F8-2A59-4CDB-A6FF-D7D60E572B39-a5.png']

In order to measure the phase and amplitude changes, the test signal used is a DC signal
 (tone at 0 Hz) upconverted to IF or RF. PAVT measurement computes the absolute and
 relative mean amplitudes and absolute and relative mean phases.

#### Measurement Location Type

PAVT measurement can be performed in two possible ways as specified by the Measurement
 Location Type at predefined time instants (Time) or whenever
 external triggers are received (Trigger).

Time

This type uses a single trigger to acquire the full signal on a given port as shown in
 the above figure. The full signal duration includes all the segments over which the
 measurement is made. The start time instants for each of the segments are configured by
 the user.

[IMAGE alt='image' src='GUID-309A4422-F6F6-4AF8-9707-A4220CB65BD1-a5.png']

Trigger

This type uses multiple triggers to acquire multiple segments on a given port as shown in
 the following figure.

[IMAGE alt='image' src='GUID-BB77ED0B-3977-4C3F-B37B-7F502D82E3CF-a5.png']

#### Measurement Interval Mode

PAVT measurement supports uniform and variable measurement intervals depending on the
 Measurement Interval Mode property.

Uniform

In this mode, all the segments use the same measurement offset and measurement length.
 This mode is as illustrated in the figures that depict the Time and Trigger
 Measurement Location Type.

Variable

[IMAGE alt='image' src='GUID-0E6884DA-6268-4554-9155-011F61AAA221-a5.png']

In this mode each segment uses a different measurement offset and measurement length.
 This mode only supports the Time Measurement Location Type.

#### Segment Types

PAVT measurement supports three segment types:

Phase and Amplitude

If a segment is configured as Phase and Amplitude, then Phase
 (deg) and Amplitude (dBm) are measured for that segment. The expected signal type is a
 Continuous Wave (CW).

Amplitude

If a segment is configured as Amplitude, then only Amplitude (dBm)
 is measured for that segment. The expected signal type is any modulated signal like 5G
 NR waveform.

Frequency Error Measurement

If a segment is configured as Frequency Error Measurement, then
 the frequency error is computed over that segment and if frequency offset correction is
 enabled, the computed frequency error is compensated on the subsequent segments. This
 segment is supported only for Time Measurement Location Type. Only Segment0 can be
 configured as Frequency Error Measurement.

[IMAGE alt='image' src='GUID-0BDC3D2A-C4EA-42AB-A3AC-81E1872DB66E-a5.png']

If there is no Frequency Error Measurement segment and the Frequency Offset Correction
 is enabled, then the measurement computes Frequency Error using Phase and Amplitude
 segments.

#### Recommended Settings

In order to improve the accuracy of the measurement the following are recommended:

- Offset the LO at signal generator and signal analyzer to avoid carrier leakage. This
 can be achieved at the signal analyzer by setting the LO Leakage Avoidance Enabled
 property to True .
- Share the LO between signal generator and signal analyzer. This can be achieved by
 setting the LO Source property to Automatic_SG_SA_Shared or
 to SG_SA_Shared .
- Initiate the measurement before generating the signal, especially in
 Trigger Measurement Location Type , so that the SA
 acquires the generated signal from the beginning of the first segment.
- Use Digital Edge trigger to ensure measurements are triggered at the most accurate
 positions.

<!--NI_TOPIC bundle=rfmx-specan path=phase-noise.html language=enus -->
## TOPIC 00031: Phase Noise

- bundle_id: `rfmx-specan`
- source_path: `phase-noise.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan/raw/resource/enus/phase-noise.html
- document_id: `rfmx-specan`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Phase Noise measurement requires license activation. If you install RFmx SpecAn but do not activate the Phase Noise measurement license, you will have 30 days from the first time you use the measurement to evaluate it. Oscillators are ubiquitous to radio frequency (RF) communication systems. Osc

### Phase Noise

Note

Oscillators are ubiquitous to radio frequency (RF) communication systems. Oscillators are
 used for frequency mixing during up conversion and down conversion stages in signal
 generation and analysis, and as reference clocks. The signal produced by oscillators is
 corrupted by, among other impairments, the phase noise.

Phase noise is the random phase fluctuations in a signal produced by the oscillator. Phase noise
 increases the inter-carrier interference in RF communication systems that rely on
 multi-carrier technologies such as Orthogonal Frequency Division Multiplexing (OFDM)
 <sup>[1]</sup>, Orthogonal Frequency Division Multiple Access (OFDMA) and Single
 Carrier Frequency Division Multiple Access (SC-FDMA) <sup>[2]</sup>, and thus becomes a
 figure of merit when evaluating oscillators.

An ideal sinusoidal signal, generated by an oscillator, at a frequency f<sub>c</sub>, amplitude
 A and initial phase Φ<sub>0</sub>, sampled at frequency
 F<sub>s</sub> can be represented as:

[IMAGE alt='image' src='GUID-1AD1E6DE-6308-4BBB-AE30-63977F87FB5D-a5.gif']

Phase noise, L[k], is conventionally expressed as a single side band PSD of
 Φ[n]<sup>[4]</sup>. An example of a phase noise plot, 10 logL[k]
 vs k, is illustrated in the following image.

[IMAGE alt='image' src='GUID-7F4C0C33-B166-494B-8B4B-04F1424E0C8A-a5.gif']

The frequency axis k is usually expressed in a logarithmic scale and
 hence the phase noise plot is also called as the log plot. The units of phase noise,
 10logL[k], is dBc/Hz.

#### Range Definition

RFmxSpecAn PhaseNoise measurement allows you to configure phase noise offset frequency
 range by setting the Range Definition property to Auto or
 Manual.

Auto

In this mode, you can specify the complete phase noise offset frequency range using the
 Start Frequency (Hz) and Stop Frequency (Hz) properties. The measurement divides this
 range into multiple decades (sub-ranges ). A separate acquisition is done for each
 sub-range. This division into multiple sub-ranges is done for two reasons:

- To get similar number of trace points for each decade when the frequency axis of
 plot is viewed in a logarithmic scale. A single acquisition for complete measurement
 range leads to fewer number of trace points for lower offset frequencies and larger
 number of points for far offset frequencies.
- To optimize the measurement for speed if the measurement range happens to be
 wide.

The resolution bandwidth, RBW<sub>Bin Width</sub>(Hz), is specified as a percentage of
 the start frequency of each sub-range by configuring the RBW(%) property. This property
 affects the measurement interval and the number of trace points for each
 sub-range,i, as shown in the following equations.

[IMAGE alt='image' src='GUID-4A96EC8A-F97D-4E95-9AFB-472D85738B80-a5.gif']

In this mode, the measurement uses pre-computed number of averages for each sub-range, as
 shown in the following table.

[IMAGE alt='image' src='GUID-1410E778-9899-4ADE-BBDC-D48D3A00A2A9-a5.gif']

The averaging counts for different sub-ranges are heuristically selected to strike a
 balance between measurement speed and quality.

Manual

In this mode, you can configure each offset frequency sub-range by setting the Range
 Start Frequency (Hz), Range Stop Frequency (Hz), Range RBW Percentage (%) and Range
 Averaging Count properties for each sub-range.

#### Averaging Multiplier

The averaging count for each sub-range can be increased by setting the Averaging
 Multiplier property. This multiplies the averaging count for each sub-range by the
 factor specified. This setting applies to both the Auto and
 theManualrange definitions. When the range definition is
 Auto, the pre-computed averaging count for each decade range
 is increased by this factor. When the range definition is Manual,
 the averaging count specified by you for each range is increased by this factor.

#### Smoothing

In order to extract the underlying trend of phase noise across frequencies, trace
 smoothing can be performed on a measured log plot trace. The following image illustrates
 measured and smoothed log plot traces.

[IMAGE alt='image' src='GUID-931C4F48-3731-4326-90C6-65E78DAD1673-a5.gif']

The three supported smoothing types are Linear,
 Logarithmic, and Median that perform
 linear moving average, logarithmic moving average, and moving median filtering
 respectively as expressed in the following equations.

[IMAGE alt='image' src='GUID-A67632FD-134F-4F66-A603-9988BC3833C9-a5.gif']

The parameter w controls the amount of smoothing, and is derived from
 the Smoothing Percentage (%) property.

#### Spot Noise

Spot noise is the phase noise, in dBc/Hz, at a specified offset frequency.

#### Integrated Noise

Phase noise generates unwanted modulation products, also called as residual noise.
 Residual noise can be measured by integrating the phase noise log plot trace over a
 specified frequency range.

In addition to integrated phase noise, PhaseNoise measurement computes Residual PM,
 Residual FM and Jitter.

Integrated Phase Noise (dBc)

[IMAGE alt='image' src='GUID-5E11BE59-9AA2-42A7-B1E1-9CE2C1CAA23D-a5.gif']

Residual PM (rad)

Residual PM is the contribution of phase noise to phase modulation of the carrier at
 frequency f<sub>c</sub> evaluated over a frequency range.

[IMAGE alt='image' src='GUID-6281893A-FC77-4086-8DE8-C426F4FE23AE-a5.gif']

Residual FM (Hz)

Residual FM is the contribution of phase noise to frequency modulation of the carrier at
 frequency f<sub>c</sub> evaluated over a frequency range.

[IMAGE alt='image' src='GUID-CF3A9DFE-EC62-4E28-82DB-ED9A4E28347E-a5.gif']

Jitter (s)

Jitter is the time domain fluctuation of a signal due to phase noise evaluated over a
 frequency range.

[IMAGE alt='image' src='GUID-7B447172-7D86-4A0F-8E9D-D1879764BD38-a5.gif']

where,

[IMAGE alt='image' src='GUID-7BA7CE2B-0A2B-475A-95C4-D0ED7EE451B4-a5.gif']

#### Spur Removal

The phase noise log plot trace may contain spurs due to presence of non-random
 interfering signals. The presence of such interference skews phase noise measurement
 results and therefore should be eliminated from the measured log plot trace. The
 following image below shows two traces, one with spurs and the other with spurs
 removed.

[IMAGE alt='image' src='GUID-503EFA99-7BA5-4AB4-85F7-FC62155E2E6F-a5.gif']

The spur removal algorithm detects the spur region on a measured log plot trace and
 replaces this region with a smoother trace.

Spur detection is based on peak excursion specified by the user and is performed on the
 difference between the measured and smooth trace, with the peak threshold set to 0 dBm.
 Refer to the Marker topic for more information on peak excursion and peak threshold.

#### Phase Noise Cancellation

Phase noise cancellation is used to reduce the contribution of the signal analyzer’s
 phase noise to the phase noise measurement of the device under test (DUT). A reference
 source, whose phase noise is at least 10 dB better than that of signal analyzer, is used
 to obtain a good approximation of signal analyzer’s phase noise, L<sub>Ref</sub>[k]. The
 obtained trace is subtracted from the phase noise trace of device under test,
 L<sub>DUT</sub>[k], to get the post cancellation trace, L<sub>Post
 Cancellation</sub>[k].

The following image shows the effect of phase noise cancellation.

[IMAGE alt='image' src='GUID-A2C69132-8EBD-4BD5-A491-AF485A6951D4-a5.gif']

The cancellation follows the following relationship.

[IMAGE alt='image' src='GUID-AA5BEBC6-EADF-40A3-B4BD-4BF0A227274B-a5.gif']

where,

L<sub>Ref</sub>[k],L<sub>DUT</sub>[k], and L<sub>Post Cancellation</sub>[k] are expressed
 in dBc/Hz.

T is the threshold, in dB, which specifies the minimum difference
 between L<sub>DUT</sub>[k] and L<sub>Ref</sub>[k] that must exist before cancellation is
 performed.

Note

1. Sufficient averaging should be performed for obtaining
 reasonable estimates of L Ref [k] and
 L DUT [k].
2. Same hardware and measurement settings should be used to obtain
 estimates of L Ref [k] and L DUT [k].

#### Order of Operations

The following block diagram depicts the order of operations used by the RFmxSpecAn
 PhaseNoise measurement.

[IMAGE alt='image' src='GUID-61DD5C4D-3CFB-49C2-A253-50CE6E6BB595-a5.gif']

#### Recommended Settings

The following are the recommended settings for the phase noise measurement.

Reference Level

Reference level should be set equal to the peak power of the input signal to utilize the
 full-scale of the digitizer more efficiently. Setting such a reference level brings the
 power level of the IF signal at the input of digitizer closer to the digitizer’s full
 scale.

Supported Analyzers: PXIe-5665, PXIe-5668, PXIe-5644/5645/5646,
 PXIe-5840

RF Attenuation

The input signal for phase noise measurement is usually a continuous wave signal. This
 allows for a higher signal power at the input of first mixer in the signal analyzer to
 get a better dynamic range. Refer to the dynamic range chart of the device mentioned in
 the device specification sheet. The mixer level follows the relationship shown in the
 following equation.

[IMAGE alt='image' src='GUID-C9F9E26C-9ED6-4306-B2FF-06E852146452-a5.gif']

For a fixed reference level, the RF Attenuation can be decreased to get a higher mixer
 level.

Supported Analyzers:PXIe-5665, PXIe-5668

Note

1. The RFmxSpecAn PhaseNoise measurement sets the IF
 Output Power Offset as 6 dB by default.
2. The measured log plot trace may contain discontinuities at the
 edges of sub-ranges under low Carrier-to-Noise Ratio (CNR)
 conditions. This behavior can be easily seen when no carrier is
 present at the RF input of signal analyzer. In this scenario,
 the acquired complex signal is almost entirely Additive White
 Gaussian Noise, whose phase is distributed uniformly between
 [-π,π) radians. Unwrapping this phase is highly prone to errors,
 leading to discontinuities in measured log plot trace.

#### References

<sup>[1]</sup>Wu, Songping, and Yeheskel Bar-Ness. "OFDM systems in the presence of phase noise:
 consequences and solutions." IEEE Transactions on Communications
 52.11 (2004): 1988-1996.

<sup>[2]</sup> Sridharan, Gokul, and Teng Joon Lim. "Performance analysis of SC-FDMA in the
 presence of receiver phase noise." IEEE Transactions on
 Communications 60.12 (2012): 3876-3885.

<sup>[3]</sup> Cohen, Leon. "The generalization of the Wiener-Khinchin theorem."
 Acoustics, Speech and Signal Processing, 1998. Proceedings of the 1998
 IEEE International Conference on. Vol. 3. IEEE, 1998.

<sup>[4]</sup> Vig, John R. "IEEE standard definitions of physical quantities for
 fundamental frequency and time metrology–random instabilities (IEEE standard
 1139-1999)." IEEE, New York 1 (1999).

Related concepts:

- Marker

<!--NI_TOPIC bundle=rfmx-specan path=rbw-and-sweep-time.html language=enus -->
## TOPIC 00032: RBW and Sweep Time

- bundle_id: `rfmx-specan`
- source_path: `rbw-and-sweep-time.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan/raw/resource/enus/rbw-and-sweep-time.html
- document_id: `rfmx-specan`
- page_type: `leaf`
- content_type: `concept`
- source_description: Effect of Windowing Function on the Resolution of the Spectrum Using properties of Fourier transform for convolution^[1], the following equation describes the frequency domain representation of the windowed signal. where, W[k] is the DFT of the windowing function * is the circular convolution opera

### RBW and Sweep Time

#### Effect of Windowing Function on the Resolution of the Spectrum

Using properties of Fourier transform for convolution<sup>[1]</sup>, the following
 equation describes the frequency domain representation of the windowed signal.

[IMAGE alt='image' src='GUID-B1C9BD42-E592-4301-A039-893A5EBB1A27-a5.png']

where,

W[k] is the DFT of the windowing function

* is the circular convolution operator

This equation implies that the DFT of the windowing function acts as a filter on the
 spectrum of the signal being analyzed.

The FFT-based RBW filter in RFmx uses  W[k] as the RBW filter. The
 bandwidth of this filter  is also called the RBW associated with the windowing
 function. The 3 dB and 6 dB RBW definitions are defined as follows.

[IMAGE alt='image' src='GUID-BE6A152E-095C-4DA3-AB65-47D6A58E4242-a5.png']

The following figure shows the frequency response of a window.

[IMAGE alt='image' src='GUID-607A1EEB-3FA0-4951-98D2-781DCD3DB0D7-a5.png']

Refer to the Window and FFT section for more information about the relation between
 RBW<sub>3dB</sub>,
 RBW<sub>6dB</sub>, and
 RBW<sub>Bins</sub>.

#### References

[1] Proakis, John G., and Dimitris G. Manolakis. Introduction to digital
 signal processing. Prentice Hall Professional Technical Reference,
 1988.

<!--NI_TOPIC bundle=rfmx-specan path=recommended-settings.html language=enus -->
## TOPIC 00033: Recommended Settings

- bundle_id: `rfmx-specan`
- source_path: `recommended-settings.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan/raw/resource/enus/recommended-settings.html
- document_id: `rfmx-specan`
- page_type: `leaf`
- content_type: `concept`
- source_description: Signal Analyzer and Preamplifier NI recommends the following settings: For DUT characterization, use the PXIe-5668 with PXIe-5698 preamp with Y-Factor method to minimize uncertainty in the NF measurement. The preselector is enabled by default in order to reject images for measurements at center freq

### Recommended Settings

#### Signal Analyzer and Preamplifier

NI recommends the following settings:

- For DUT characterization, use the PXIe-5668 with PXIe-5698 preamp with
 Y-Factor method to minimize uncertainty in the NF
 measurement.
  - The preselector is enabled by default in order
 to reject images for measurements at center
 frequencies ranging from 3.6 GHz to 26.5 GHz.
 Enabling the preselector increases tuning time and
 hence takes longer time to complete the
 measurement. Disabling the preselector will reduce
 the measurement time, but may introduce
 measurement error. NI recommends you to verify the
 measurement with preselector enabled and disabled
 to trade off measurement error with measurement
 speed.
  - When using PXIe-5668 with PXIe-5698 and preamp
 is enabled, RF Attenuation is fixed to 5 dB. The
 maximum supported reference level is -35 dBm.
- For production test applications, use NI Vector Signal Transceiver
 (PXIe-5644/45/46) with cold source method for fast and repeatable NF
 measurement.
  - To minimize the noise figure of the signal analyzer, enable
 internal preamp by setting the reference level to -50 dBm or
 lower.
- Keep the reference level and RF attenuation constant between calibration
 and measurement steps. Use the Recommend Reference Level VI to
 compute and set optimal reference level based on the measurement
 settings. Call this utility after configuring all RFmxSpecAn NF
 properties.
- When you are using more than one calibration setups, specify a unique
 string identifier as Calibration Setup ID for each hardware setup
 used to perform calibration for NF measurement. When performing the
 measurement step, specify the same Calibration Setup ID string used
 during calibration step, for RFmx to retrieve the appropriate
 calibration information for computing results.
- For frequency converting DUTs, incorrect image rejection setting can
 lead to errors of up to 3 dB in NF and DUT gain.

#### Measurement

- Keep the following measurement parameters constant between calibration
 and measurement steps:
  - Measurement Bandwidth
  - Calibration Setup ID
  - Calibration Loss
- Set a sufficiently large measurement interval to obtain repeatable
 results.
- Insert attenuators in the signal path to reduce impedance mismatches
 between the noise source and DUT or the DUT and the signal analyzer.
 For every dB of attenuation, mismatch improves by 2 dB.
- Configure s 21 of the DUT when using cold source method. To
 minimize NF measurement uncertainty you should configure all
 S-parameters of the DUT.

<!--NI_TOPIC bundle=rfmx-specan path=sem.html language=enus -->
## TOPIC 00034: SEM

- bundle_id: `rfmx-specan`
- source_path: `sem.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan/raw/resource/enus/sem.html
- document_id: `rfmx-specan`
- page_type: `leaf`
- content_type: `concept`
- source_description: Spectral emission mask (SEM) measurements measure out-of-band emissions in the neighboring bands of the carrier. In measurements such as ACP, the emissions may remain undetected when measuring the integrated power in the band. SEM uses the spectral mask or limit you specify to measure the margin of

### SEM

Spectral emission mask (SEM) measurements measure out-of-band emissions in the
 neighboring bands of the carrier. In measurements such as ACP, the emissions may remain
 undetected when measuring the integrated power in the band. SEM uses the spectral mask
 or limit you specify to measure the margin of the emission level from the limit and
 reports the measurement status.

The following figure shows the configuration of SEM carriers and offset segments.

[IMAGE alt='image' src='GUID-52B27080-1891-4329-B8DA-65A4D1F4FFB8-a5.gif']

#### Carrier Channels

Carriers are channels in which significant power is transmitted and for which power
 leakage in the offset channels is measured. Multiple carriers are configured relative to
 the RF center frequency by specifying the carrier offset. Each carrier is configured for
 the integration bandwidth (IBW), RBW, and RRC channel filter. Power in each carrier is
 measured by integrating the power in the specified IBW after applying the channel
 filter. The total carrier power measured is the aggregate power of all the active
 carriers.

#### Offset Segments

Offset segment start and stop frequencies are specified relative to the closest carrier
 offset frequency. The placement of the offset segments with respect to the nearest
 carrier is defined by the SEM offset frequency definition.

Offset Frequency Definition

The offset frequency definition defines the offset start and stop frequency of the offset
 segment with respect to the nearest carrier channel in one of the following ways:

- Carrier Center to Meas BW Center —The start frequency and stop
 frequency are defined from the center of the closest carrier channel bandwidth to
 the center of the offset segment measurement bandwidth respectively.
- Carrier Center to Meas BW Edge —The start frequency and stop
 frequency are defined from the center of the closest carrier channel bandwidth to
 the nearest edge of the offset segment measurement bandwidth respectively.
- Carrier Edge to Meas BW Center —The start frequency and stop
 frequency are defined from the nearest edge of the closest carrier channel bandwidth
 to the center of the nearest offset segment measurement bandwidth respectively.
- Carrier Edge to Meas BW Edge —The start frequency and stop
 frequency are defined from the nearest edge of the closest carrier channel bandwidth
 to the edge of the nearest offset segment measurement bandwidth respectively.

The measurement bandwidth of the offset segment is the bandwidth represented by the RBW
 and bandwidth integral values as shown in the following equation: Measurement
 Bandwidth = RBW * Bandwidth
 Integral

The following image describes the offset frequency definitions:

[IMAGE alt='image' src='GUID-0DA055FD-C98F-47ED-8403-3F0BAA93CC5D-a5.png']

Offset Sideband

An offset segment is configured on either side of the carrier when you set the offset
 sideband to BOTH. Only one offset sideband is configured when you configure a positive
 (POS) or negative (NEG) sideband. Negative sideband creates a lower offset segment to
 the left of the leftmost carrier. Positive sideband creates an upper offset segment to
 the right of the rightmost carrier. Each offset segment is configured for IBW, RBW, RRC
 filter, relative attenuation, spectral mask, and measurement failure criteria.

#### RBW and Sweep Time

RBW is configured for each carrier and offset segment. When you set the RBW to Auto, the
 measurement sets the RBW using the following ratio:

IBW:RBW<sub>3dB</sub> = 100, where RBW<sub>3dB</sub> is a value
 between 1 Hz and 1 MHz

When you set the sweep time to Auto, the measurement sets the sweep time using the
 following value:

- k /RBW 3dB when the RBW filter is FFT based, where
 k is a constant that depends on the FFT window
- 10/RBW 3dB for other RBW filters

#### Power Measurement

Power Units

The absolute power values measured are reported in dBm (integrated power) or dBm/Hz
 (power spectral density). The relative power values are not affected by the units
 specified.

Use relative attenuation to compensate for external attenuation for each offset
 channel.

Relative Power Reference

Carriers are measured relative to the total power of all enabled carriers.

Offset segment power is measured relative to either integrated power or the peak power of
 the closest carrier. Use the SEM Ref Type property to specify integrated power or peak
 power as reference.

Note

#### Spectral Mask

Limit Lines

The absolute and/or relative limit lines for each offset segment define the spectral
 mask. A limit line is defined by a start and stop power. Start power corresponds to the
 frequency point closer to the carrier. A level line can be configured by specifying the
 start power limit and coupling it to the stop power using the SEM Offset Relative Limit
 Mode.

Relative limits are specified relative to the integrated power or peak power of the
 carrier closest to the offset segment. Use the SEM Ref Type property to specify whether
 to use integrated power or peak power.

Margin and Measurement Status

The spectrum is corrected for external attenuation for each offset based on the specified
 relative attenuation. This spectrum is compared against the limit lines to report margin
 and measurement PASS/FAIL status. Margin, in dB, is the largest difference between the
 measured spectrum and the limit line.

The measurement failure criteria, also called the limit fail mask, can be one of the
 following criteria:

- Absolute —Checks for emissions crossing the absolute limit
 line.
- Relative —Checks for emissions crossing the relative limit
 line.
- Absolute AND Relative —Checks for emissions crossing both the
 absolute and relative limit lines. The highest margin with respect to the higher
 limit mask is reported.
- Absolute OR Relative —Checks for emissions crossing either the
 absolute or relative limit lines. The highest margin with respect to the lower limit
 mask is reported.

The measurement returns the frequency and absolute power (dBm or dBm/Hz) at the reported
 margin, and it also returns the power relative to the integrated power or the peak power
 based on the value of the SEM Ref Type property.

Note

Related concepts:

- Spectral Measurements Concepts

<!--NI_TOPIC bundle=rfmx-specan path=sequential-fft.html language=enus -->
## TOPIC 00035: Sequential FFT

- bundle_id: `rfmx-specan`
- source_path: `sequential-fft.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan/raw/resource/enus/sequential-fft.html
- document_id: `rfmx-specan`
- page_type: `leaf`
- content_type: `concept`
- source_description: Sequential FFT is a technique where the frequency spectrum of the underlying signal is computed by first dividing the signal into overlapping chunks and then computing the FFT-based spectrum of each chunk. The spectrum of the signal is then obtained by averaging the spectra of all the chunks. This t

### Sequential FFT

Sequential FFT is a technique where the frequency spectrum of the underlying signal is
 computed by first dividing the signal into overlapping chunks and then computing the
 FFT-based spectrum of each chunk. The spectrum of the signal is then obtained by
 averaging the spectra of all the chunks.

This technique is also referred to as Overlap and Add Short Time Fourier
 Transform (Overlap and Add STFT) or simply Overlapped
 FFT.

The figure below shows an example of Sequential FFT processing with 50% overlap between
 sequential chunks of time-domain samples.

[IMAGE alt='image' src='GUID-39F1855A-0895-466A-BC30-B8DA19035AA0-a5.png']

Sequential FFT in RFmxSpecAn involves the following steps:

1. The measurement acquires I/Q samples for a duration specified by the sweep time
 property. The acquired I/Q samples are divided into smaller overlapping chunks of
 equal size. The size of each chunk is referred to as Sequential FFT
 Size . In general, Sequential FFT size and RBW
 filter bandwidth are coupled. Specifying one automatically fixes the other. You can
 configure the amount of overlap between sequential chunks as a percentage of
 Sequential FFT Size .
  - When using RFmxSpecAn Spectrum measurement, you can
    - specify the desired FFT size using the Spectrum
 Sequential FFT Size property with
 Spectrum RBW Auto property set to
 True , or
    - specify desired resolution bandwidth by using Spectrum
 RBW (Hz) property and setting Spectrum
 RBW Auto property to False ;
 RFmx derives the Sequential FFT Size from RBW
 filter bandwidth.
  - When using RFmxSpecAn ACP measurement,
    - you must specify desired FFT Size by using the ACP
 Sequential FFT Size property with ACP RBW
 Auto property set to
 True .
    - Setting RBW filter bandwidth is not allowed.
2. FFT spectrum of each chunk is computed by first multiplying the time-domain signal
 by a window function followed by FFT. Refer to the Window and FFT section for
 more details.
3. Spectra of all chunks are averaged to obtain spectrum of the underlying signal.

Use Sequential FFT for the following purposes:

1. Fast spectral measurements by utilizing smaller FFT sizes and
 setting overlap between time-domain data chunks to 0. This ensures that time-domain
 data chunks are not overlapped, resulting in fewer overall number of FFT operations. Note Using smaller FFT sizes can lead to poorer resolution in the
 spectrum.
 Eliminating time-overlap between sequential time-domain data chunks can
 suppress spectral information contained in the beginning and end of each
 chunk because these parts susceptible to get attenuated by the windowing
 operation. Sufficient time-overlapping of chunks ensures that no part of
 the overall signal is completely attenuated by the window
 operation.
2. Measuring signals with time-varying spectral characteristics .
 In this case, use sufficient overlap between time-domain chunks. To enable
 overlapping sequential chunks, set the FFT Overlap Mode 
 property to Automatic (uses 50% overlap) or directly
 configure the desired overlap using the FFT Overlap (%) 
 property with the FFT Overlap Mode property set to
 User-Defined .

RFmxSpecAn supports sequential FFT in Spectrum and ACP measurements. You can enable
 sequential FFT by setting the Spectrum Measurement Method
 property or ACP Measurement Method property to
 Sequential FFT. The following properties have limited support
 in Sequential FFT method.

| Property | Supported Value |
| --- | --- |
| ACP RBW Auto | True |
| ACP RBW Filter Type, Spectrum RBW Filter Type | FFT Based |
| ACP Sweep Time Auto, Spectrum Sweep Time Auto | False |
| ACP Amplitude Correction Type, Spectrum Amplitude Correction Type | RF Center Frequency |
| ACP Offset Rel Attn | 0 |
| Spectrum VBW Auto | True |
| Spectrum VBW to RBW Ratio | >=3 |
| ACP Num Analysis Threads, Spectrum Num Analysis Threads | 1 |

Note

<!--NI_TOPIC bundle=rfmx-specan path=spectral-measurements-concepts.html language=enus -->
## TOPIC 00036: Spectral Measurements Concepts

- bundle_id: `rfmx-specan`
- source_path: `spectral-measurements-concepts.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan/raw/resource/enus/spectral-measurements-concepts.html
- document_id: `rfmx-specan`
- page_type: `leaf`
- content_type: `concept`
- source_description: Spectrum is the frequency-domain representation of a time-domain electromagnetic signal. RFmx spectrum measurements are implemented using time-domain acquisitions at multiple RF center frequencies, converting the acquired data to frequency domain using Fast Fourier transform, and then stitching the

### Spectral Measurements Concepts

Spectrum is the frequency-domain representation of a time-domain electromagnetic
 signal.

RFmx spectrum measurements are implemented using time-domain acquisitions at multiple RF
 center frequencies, converting the acquired data to frequency domain using Fast Fourier
 transform, and then stitching the various spectrums together to form the complete
 spectrum.

The following figure shows the important stages in the signal processing chain to obtain
 a spectrum of a finite duration signal. [IMAGE alt='image' src='GUID-72B960C3-1561-4F37-8BF0-B7E12C497039-a5.png']

<!--NI_TOPIC bundle=rfmx-specan path=spectrum.html language=enus -->
## TOPIC 00037: Spectrum

- bundle_id: `rfmx-specan`
- source_path: `spectrum.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan/raw/resource/enus/spectrum.html
- document_id: `rfmx-specan`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Spectrum measurement allows you to view signal in the frequency domain within the frequency span that you have configured. The following list contains the basic properties to configure in a Spectrum measurement: RF Center Frequency and Span—Configure RF center frequency and span to observe the f

### Spectrum

The Spectrum measurement allows you to view signal in the frequency domain within
 the frequency span that you have configured.

The following list contains the basic properties to configure in a Spectrum
 measurement:

- RF Center Frequency and Span— Configure RF center
 frequency and span to observe the frequencies of interest around the
 RF center frequency. Alternatively, you can specify the start and
 stop RF frequencies.
- Resolution Bandwidth (RBW)— Configure RBW based on
 the required resolution of frequencies and DANL.
- RBW Filter— Configure RBW filter to Gaussian or
 Flat in order to digitally emulate the RBW filters used in
 traditional swept analyzers. NI recommends using FFT based RBW
 filtering to get the best speed performance.
- FFT Window— Configure the FFT window type when you
 are using FFT based RBW filtering based on the tolerance in spectral
 leakage requirements of the application as mentioned in the Spectral
 Measurements topic. When using other RBW filters, NI recommends
 using the Flat Top window.

The amplitude of the frequencies is reported in dBm, a logarithm scale
 referenced to 1 mW. Other units supported are dBm/Hz, dBW, dBV, dBmV, dBuV,
 W, V, and V<sup>2</sup>.

The following image shows the RF center frequency and span for a Spectrum
 measurement.

[IMAGE alt='image' src='GUID-937B0C45-E628-47CB-ADE7-5816555BF6D4-a5.png']

#### Zero Span

Zero span is a special type of spectrum measurement in which you set the span to
 zero. The spectrum measurement returns the time-domain power trace as seen
 through an RBW filter. Sweep time specifies the duration of the acquisition.

The RBW specifies the acquisition bandwidth and cannot exceed the signal
 analyzer’s maximum device instantaneous bandwidth.

Zero span acquisition bandwidth is calculated using the following formula:

Zero Span Acquisition Bandwidth = RBW +
 Excess Span required by RBW Filter

Zero span acquisition sample rate is calculated using the following formula:

Zero Span Acquisition Sample Rate = 1.25 * Zero Span
 Acquisition Bandwidth

The following figure shows a zero span acquisition.

[IMAGE alt='image' src='GUID-A4E1F4B4-48E8-4F37-88AB-CCD44873581B-a5.gif']

NI recommends the following settings to configure a zero span measurement:

- Span: Set span to 0 Hz.
- RBW: Configure the RBW to specify the 3 dB
 bandwidth over which the time domain signal needs to be analyzed.
 Ensure that the RBW does not exceed the instantaneous bandwidth of
 the signal analyzer.
- RBW Filter: NI recommends using the flat or
 FFT-based RBW filter when using a zero span measurement. The
 FFT-based RBW filter implies an all pass filter.
- Sweep Time: Configure the sweep time to specify
 the duration of acquisition.

Related concepts:

- Spectral Measurements Concepts

<!--NI_TOPIC bundle=rfmx-specan path=spur.html language=enus -->
## TOPIC 00038: Spur

- bundle_id: `rfmx-specan`
- source_path: `spur.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan/raw/resource/enus/spur.html
- document_id: `rfmx-specan`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Spur measurement measures unwanted spurs at frequency ranges that are at a greater distance from the operating band of the carrier. These emissions are usually of low power; and hence, require a signal analyzer with a displayed average noise level (DANL) lower than the spur level. The following

### Spur

The Spur measurement measures unwanted spurs at frequency ranges that are at a
 greater distance from the operating band of the carrier. These emissions are
 usually of low power; and hence, require a signal analyzer with a displayed
 average noise level (DANL) lower than the spur level.

The following spectrum analyzers are recommended for spur measurement.

| Supported Analyzers | Noise Power Spectral Density (PSD) |
| --- | --- |
| PXIe-5665 | -153 dBm/Hz at 1 GHz with preamplifier disabled |
| PXIe-5668 | -155 dBm/Hz at 1 GHz with preamplifier disabled |

Selection of resolution bandwidth (RBW) affects the measurable noise floor as
 shown by the following equation:[IMAGE alt='image' src='GUID-46251BAE-628C-4334-B548-D8537CCE296B-a5.gif']

#### Ranges

A range is defined by start frequency, stop frequency, RBW filter, sweep time,
 absolute limits, peak threshold, peak excursion, and the number of spurs to
 report.

The spur measurement uses FFTs to obtain a spectrum by acquiring multiple
 wideband signals and stitching the spectrum together in the frequency
 domain. Because the RBW filters are emulated digitally, the sweep time
 required is less than the traditional swept spectrum approach for the same
 measurement accuracy.

The signal should rise and fall by at least the peak excursion value, above the threshold, to be
 considered as a spur. Refer to the *Peak Excursion section of the Marker topic*
 for more information about peak excursion.

The absolute limit lines specified for each frequency range define the spectral
 mask. A limit line is defined by a start and stop power. Start power
 corresponds to the start frequency bin. You can configure a level line by
 specifying the start power limit and coupling it to the stop power.

#### Spur Measurements

A spur rises and falls in amplitude around the specified threshold within a few
 frequency bins. The margin of the spur from the limit line is returned along
 with the measurement status for every range configured. The spurs are
 reported in descending order of margin from the limit line.

Note

- Supported signal analyzer: PXIe-5665,
 PXIe-5668
- A narrower RBW results in a lower DANL, thus
 exposing spurs previously masked by the noise
 floor of the spectrum analyzer. However, analyzing
 a wide frequency range with a narrow RBW increases
 measurement time, and requires higher memory and
 processing power. When using narrow RBW with a
 large span, NI recommends splitting the span into
 multiple ranges, each configured for a smaller
 span.

- Refer to the specifications for your signal
 analyzer to learn more about the inherent spurs
 and their levels.

Related concepts:

- Marker

<!--NI_TOPIC bundle=rfmx-specan path=supported-hw.html language=enus -->
## TOPIC 00039: Supported Hardware

- bundle_id: `rfmx-specan`
- source_path: `supported-hw.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan/raw/resource/enus/supported-hw.html
- document_id: `rfmx-specan`
- page_type: `leaf`
- content_type: `concept`
- source_description: RFmx supports a number of NI devices. 1 RFmx SpecAn Supported Hardware RFmx SpecAn Hardware Earliest Driver Version Support (Windows 11) PXIe-5644 2022 Q3 PXIe-5645 2022 Q3 PXIe-5646 2022 Q3 PXIe-5663 2022 Q3 PXIe-5663E 2022 Q3 PXIe-5665 2022 Q3 PXIe-5668 2022 Q3 PXIe-5820 2022 Q3 PXIe-5830 2022 Q3

### Supported Hardware

RFmx supports a number of NI devices.

| RFmx SpecAn Hardware | Earliest Driver Version Support (Windows 11) |
| --- | --- |
| PXIe-5644 | 2022 Q3 |
| PXIe-5645 | 2022 Q3 |
| PXIe-5646 | 2022 Q3 |
| PXIe-5663 | 2022 Q3 |
| PXIe-5663E | 2022 Q3 |
| PXIe-5665 | 2022 Q3 |
| PXIe-5668 | 2022 Q3 |
| PXIe-5820 | 2022 Q3 |
| PXIe-5830 | 2022 Q3 |
| PXIe-5831 | 2022 Q3 |
| PXIe-5832 | 2022 Q3 |
| PXIe-5840 | 2022 Q3 |
| PXIe-5841 (1 GHz Bandwidth) | 2022 Q3 |
| PXIe-5841 (200 MHz Bandwidth) | 2026 Q2 |
| PXIe-5842 | 2022 Q4 |
| PXIe-5860 | 2024 Q3 |

Note

RFmx SpecAn

NI-RFSA Properties

NI-RFSA LabVIEW VI Reference

For more information about your hardware and functionality, refer to the *NI-RFSA User
 Manual*.

<!--NI_TOPIC bundle=rfmx-specan path=system-requirements.html language=enus -->
## TOPIC 00040: RFmx SpecAn System Requirements

- bundle_id: `rfmx-specan`
- source_path: `system-requirements.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan/raw/resource/enus/system-requirements.html
- document_id: `rfmx-specan`
- page_type: `leaf`
- content_type: `concept`
- source_description: RFmx SpecAn has the following requirements: Processor—1 GHz 64-bit (x64) processor 4 GB RAM * A screen resolution of 1,024 x 768 Any supported OS, with all available critical updates and service packs * Depending on the amount of data acquired and/or processed, a larger amount of memory may be requi

### RFmx SpecAn System Requirements

RFmx SpecAn has the following requirements:

- Processor—1 GHz 64-bit (x64) processor
- 4 GB RAM *
- A screen resolution of 1,024 x 768
- Any supported OS, with all available critical updates and service packs

* Depending on the amount of data acquired and/or processed, a larger amount of memory
 may be required.

<!--NI_TOPIC bundle=rfmx-specan path=txp.html language=enus -->
## TOPIC 00041: TXP

- bundle_id: `rfmx-specan`
- source_path: `txp.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan/raw/resource/enus/txp.html
- document_id: `rfmx-specan`
- page_type: `leaf`
- content_type: `concept`
- source_description: TXP is a zero span measurement of transmitted power using the time-domain signal as seen through a resolution bandwidth (RBW) filter for the specified measurement interval. The following list describes the properties that you can configure in a TXP measurement: RBW: Configure RBW to specify the 3 dB

### TXP

TXP is a zero span measurement of transmitted power using the time-domain signal as seen
 through a resolution bandwidth (RBW) filter for the specified measurement interval.

The following list describes the properties that you can configure in a TXP
 measurement:

- RBW: Configure RBW to specify the 3 dB bandwidth over which
 the time-domain signal needs to be analyzed. Ensure that RBW does not exceed the
 instantaneous bandwidth of the signal analyzer. NI recommends selecting no filter or
 a flat filter. Refer to the Zero Span section of the Spectrum topic for more information about the sample rate required by
 the measurement.
- Measurement Interval : Configure measurement interval to
 specify the duration of acquisition.
- Threshold: While analyzing signals with dead time, NI
 recommends to specifying a threshold such that only the samples with instantaneous
 power above this threshold are considered for the measurement.

Note

Related concepts:

- Spectrum

<!--NI_TOPIC bundle=rfmx-specan path=user-dpd.html language=enus -->
## TOPIC 00042: User DPD

- bundle_id: `rfmx-specan`
- source_path: `user-dpd.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan/raw/resource/enus/user-dpd.html
- document_id: `rfmx-specan`
- page_type: `leaf`
- content_type: `concept`
- source_description: RFmxSpecAn DPD allows two modes for applying DPD on an input waveform. These are the Measurement mode and the User mode. Measurement mode uses the computed DPD lookup table or polynomial for applying DPD on an input waveform using the same RFmx session handle. The configuration parameters for applyi

### User DPD

RFmxSpecAn DPD allows two modes for applying DPD on an input waveform. These are the
 Measurement mode and the User
 mode.

Measurement mode uses the computed DPD lookup table or polynomial for applying DPD on an
 input waveform using the same RFmx session handle. The configuration parameters for
 applying DPD such as the DPD DUT Avg Input Pwr, DPD Model, DPD Meas Sample Rate, DPD
 polynomial, and lookup table are obtained from the DPD measurement configuration.

User mode allows you to apply DPD on an input waveform by configuring a previously
 computed DPD lookup table or polynomial. User mode can be enabled by setting DPD Apply
 DPD Configuration Input property to User. You must also set the configuration parameters
 for applying DPD such as the DPD Apply DPD User DUT Avg Input Pwr, DPD Apply DPD User
 DPD Model, DPD Apply DPD User Meas Sample Rate, DPD polynomial, and lookup table.

The following steps show one of the implementations of user mode of apply DPD, using a
 custom LUT.

1. Enable DPD measurement.
2. Set Apply DPD Configuration Input property to User .
3. Set Apply DPD User DUT Average Input Power, Apply DPD User Measurement Sampling
 Rate, Apply DPD User DPD Model properties.
4. Set Apply DPD User LUT Correction Type and Apply DPD User LUT Type properties.
5. Configure lookup table by setting LUT Input Powers and LUT Complex Gains.
6. Apply Digital Predistortion.

Note

User

<!--NI_TOPIC bundle=rfmx-specan path=user-manual-welcome.html language=enus -->
## TOPIC 00043: RFmx SpecAn User Manual

- bundle_id: `rfmx-specan`
- source_path: `user-manual-welcome.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan/raw/resource/enus/user-manual-welcome.html
- document_id: `rfmx-specan`
- page_type: `leaf`
- content_type: `concept`
- source_description: The RFmx SpecAn User Manual provides detailed descriptions of the product functionality and the step by step processes for use. Looking for Something Else?For information not found in the User Manual for your product, such as specifications and API reference, browse Related Information.

### RFmx SpecAn
 User Manual

The RFmx SpecAn User Manual provides detailed
 descriptions of the product functionality and the step by step processes for use.

#### Looking for Something Else?

For information not found in the User Manual
 for your product, such as specifications and API reference, browse *Related
 Information*.

Related information:

- Download RFmx SpecAn
- License Setup and Activation
- RFmx SpecAn Release Notes
- Getting Started with RFmx
- RFmx SpecAn LabVIEW Reference
- RFmx SpecAn .NET Reference
- RFmx SpecAn C Reference
- RFmx Instr LabVIEW Reference
- RFmx Instr .NET Reference
- RFmx Instr C Reference

<!--NI_TOPIC bundle=rfmx-specan path=window-and-fft.html language=enus -->
## TOPIC 00044: Window and FFT

- bundle_id: `rfmx-specan`
- source_path: `window-and-fft.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan/raw/resource/enus/window-and-fft.html
- document_id: `rfmx-specan`
- page_type: `leaf`
- content_type: `concept`
- source_description: Frequency domain representation of time domain discrete data is achieved using a linear transformation called Discrete Fourier Transform (DFT). The following equation defines DFT: where, k is the discrete frequency index n is the discrete time index N is the number of discrete time domain samples un

### Window and FFT

Frequency domain representation of time domain discrete data is achieved using a linear
 transformation called Discrete Fourier Transform (DFT). The following equation defines
 DFT:[IMAGE alt='image' src='GUID-102A5EE0-42A2-40D8-A366-1E93A8BC02CF-a5.png']

where,

kis the discrete frequency index

n is the discrete time index

N is the number of discrete time domain samples undergoing DFT

x[n] is the n<sup>th</sup> time domain signal sample

X <sub>DFT</sub> is the k<sup>th</sup> frequency component of the
 signal

The following relation shows how average power can be computed using the time-domain
 representation or using the frequency-domain representation of the signal. This result is also
 known as Parseval's Theorem <sup>[1]</sup>.

[IMAGE alt='image' src='GUID-12EF5912-913C-41E4-AA08-DA3EDD1C73B4-a5.png']

Naive implementation for computing DFT of a signal is computationally expensive. As such, a
 well-known and widely used efficient implementation of this transform, called the Fast Fourier
 Transform (FFT) is predominantly used for computation. You can use the abbreviations DFT and
 FFT interchangeably, referring to the same transform operation.

Fourier transform<sup>[1]</sup> assumes that the signal being transformed is periodic with a
 period equal to the number of samples in the signal. This assumption means that if the start
 and end portions of the signal x[n] undergoing FFT are of considerably different magnitudes,
 the periodic version of that signal appears to have a periodic discontinuity appearing with a
 period N. This discontinuity results in an FFT that appears to have high
 frequency components with large magnitudes, which are actually absent from the true signal
 under analysis. This phenomenon is referred to as spectral leakage<sup>[2]</sup>.

To minimize spectral leakage in FFT, the signal x[n] has to be modified in such a way that
 the start and end portions of this signal appear to have approximately similar magnitudes,
 leading to a periodic signal with no sudden discontinuity. The windowed signal
 x<sub>w</sub>[n] is obtained by multiplying the signal under analysis  with a
 windowing functionw[n] as shown in the following equation.

[IMAGE alt='image' src='GUID-FD0A0424-41B1-402B-B416-BCF2E7C161DD-a5.png']

Effects of windowing a signal <sup>[3]</sup> on the magnitude of the resulting spectrum are
 compensated digitally.

The size of the FFT (N), also referred to as bins, depends on sample rate
 (F<sub>s</sub>) and duration of acquisition required for the measurement. The resultant
 spectrum has unique spectral content between -F<sub>s</sub>/2 and  +F<sub>s</sub>/2 with bin
 spacing (RBW<sub>Bins</sub>) of
 F<sub>s</sub>/N. To add more points in the spectrum, you can pad the time
 domain signal with zeros by configuring the FFT padding factor. If the number of samples in
 the signal x[N] are N, padding factor used is
 P, then the number of points used to compute FFT is
 N'. The following equation defines the number of points used to compute
 FFT.

[IMAGE alt='image' src='GUID-E2E14AB6-CCA3-4794-8E84-D8FF399520DD-a5.png']

|  | Note Padding is available only when the span of acquisition is less than the signal analyzer instantaneous bandwidth. If N' is less than N, only the first N' samples are used for FFT computation. If N' is equal to N, FFT size is coerced to N. When N' > N, N' - N zeros are padded in the signal before taking an FFT. If the value of padding is negative, the spectral measurement uses an appropriate FFT padding factor to implement FFT optimally. |
| --- | --- |

The following table lists the window functions supported by spectral measurements in RFmx and
 applications of the window functions:

| Window | RBW3dB:RBWBins | RBW6dB:RBWBins | Application |
| --- | --- | --- | --- |
| None | 0.89 | 1.21 | Analyzing transients with a duration that is shorter than the window length. Separation of two tones with frequencies that are close to each other but with almost equal amplitudes. |
| Flat Top | 3.72 | 4.58 | Accurate single-tone amplitude measurements |
| Hanning | 1.44 | 2.0 | Analyzing transients with durations that are longer than the length of the window. For noise measurements where better frequency resolution is desired. |
| Hamming | 1.30 | 1.82 | Analyzing closely spaced sine waves |
| Gaussian | 1.65 | 2.30 | Provides a good balance of spectral leakage, frequency resolution and amplitude attenuation. Useful for time-frequency analysis. |
| Blackman | 1.64 | 2.35 | Analyzing a single tone as it has a low maximum side lobe level and a high side lobe roll-off rate. |
| Blackman-Harris | 1.62 | 2.27 | Useful as a good general purpose window, having side lobe rejection >90 dB and having a moderately wide main lobe. |
| Kaiser-Bessel | 1.71 | 2.39 | Separation of two tones with frequencies very close to each other but with widely differing amplitudes. |

References

[1] Proakis, John G., and Dimitris G. Manolakis. Introduction to digital signal
 processing. Prentice Hall Professional Technical Reference, 1988.

[2] National Instruments, Spectral Leakage, (http://www.ni.com/white-paper/4892/en/)

[3] Harris Fredric J., On the use of Windows for Harmonic Analysis with the Discrete
 Fourier Transform, Proc. IEEE Vol 66, No. 1, January 1978.

Related concepts:

- RBW and Sweep Time

Related information:

- 
