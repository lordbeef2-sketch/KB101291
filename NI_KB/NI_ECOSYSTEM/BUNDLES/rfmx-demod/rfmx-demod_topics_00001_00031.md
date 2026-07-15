# NI DOCUMENT BUNDLE: rfmx-demod

<!--NI_BUNDLE_CHUNK bundle=rfmx-demod start=1 end=31 -->
<!--NI_TOPIC bundle=rfmx-demod path=amplitude-and-phase-shift-keying.html language=enus -->
## TOPIC 00001: Amplitude and Phase Shift Keying

- bundle_id: `rfmx-demod`
- source_path: `amplitude-and-phase-shift-keying.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod/raw/resource/enus/amplitude-and-phase-shift-keying.html
- document_id: `rfmx-demod`
- page_type: `leaf`
- content_type: `concept`
- source_description: Amplitude and Phase Shift Keying (APSK) is a digital modulation scheme that combines both amplitude and phase variations to represent data bits. APSK is widely used in satellite communication standards such as DVB-S2. APSK modulation arranges constellation symbols in concentric rings. The R[2] to R[

### Amplitude and Phase Shift Keying

Amplitude and Phase Shift Keying (APSK) is a digital modulation
 scheme that combines both amplitude and phase variations to represent data bits. APSK is
 widely used in satellite communication standards such as DVB-S2.

APSK modulation arranges constellation symbols in concentric rings. The R<sub>2</sub> to R<sub>1</sub> Ratio and the R<sub>3</sub> to R<sub>1</sub> Ratio
 determine the ring radii.

The following table shows the supported M-ary number for APSK.

| Modulation Type | M-ary |
| --- | --- |
| APSK | 16, 32 |

To obtain a reliable constellation, set the number of symbols to be greater than the
 minimum number specified in the following table.

| M-APSK | Minimum Number of Symbols |
| --- | --- |
| 16 | 500 |
| 32 | 1500 |

16‑APSK

Figure 3.

[IMAGE alt='Plot showing 16-APSK Constellation Mapping' src='GUID-6905B5D6-F8E1-4C2C-B5BF-6933D965A233-a5.svg']

32‑APSK

Figure 4.

[IMAGE alt='Plot showing 32-APSK Constellation Mapping' src='GUID-AFDEDEBB-3EE5-4063-A505-0521CDB60F91-a5.svg']

Parent topic:

Modulation Types

<!--NI_TOPIC bundle=rfmx-demod path=amplitude-droop.html language=enus -->
## TOPIC 00002: Amplitude Droop

- bundle_id: `rfmx-demod`
- source_path: `amplitude-droop.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod/raw/resource/enus/amplitude-droop.html
- document_id: `rfmx-demod`
- page_type: `leaf`
- content_type: `concept`
- source_description: Amplitude droop, measured in dB/symbol, measures the decrease in the signal power from the start of measurement window (d[i]) to the end of that window (d[f]), per symbol. Amplitude droop is as shown in the following figure. 1 Amplitude Droop

### Amplitude Droop

Amplitude droop, measured in dB/symbol, measures the decrease in the signal power from
 the start of measurement window (d<sub>i</sub>) to the end of that
 window (d<sub>f</sub>), per symbol.

Amplitude droop is as shown in the following figure.

|  |
| --- |
| 1 Amplitude Droop |

Parent topic:

Measurements

<!--NI_TOPIC bundle=rfmx-demod path=amplitude-shift-keying.html language=enus -->
## TOPIC 00003: Amplitude Shift Keying

- bundle_id: `rfmx-demod`
- source_path: `amplitude-shift-keying.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod/raw/resource/enus/amplitude-shift-keying.html
- document_id: `rfmx-demod`
- page_type: `leaf`
- content_type: `concept`
- source_description: Amplitude-shift keying (ASK) refers to a type of amplitude modulation that assigns bit values to discrete amplitude levels. The following table shows the supported M-ary number for ASK. Modulation Type M-ary ASK 2, 4, 8 On-off keying (OOK) is equivalent to two-level ASK (0, 1), that is, a sinusoidal

### Amplitude Shift Keying

Amplitude-shift keying (ASK) refers to a type of amplitude modulation that assigns bit
 values to discrete amplitude levels. The following table shows the supported M-ary
 number for ASK.

| Modulation Type | M-ary |
| --- | --- |
| ASK | 2, 4, 8 |

On-off keying (OOK) is equivalent to two-level ASK (0, 1), that is, a sinusoidal carrier
 signal on and off with a unipolar binary signal. The following image shows a unipolar
 binary baseband signal and the resulting OOK modulated signal.

[IMAGE alt='image' src='GUID-6E9A6CDD-4F9D-4869-A197-C26EFC88368C-a5.gif']

The ASK demodulator uses the discrete levels in the carrier amplitude as the default
 symbol map. The carrier amplitude of the recovered symbol closest to the ideal symbol in
 the map decides the bits it represents. The bits mentioned in the symbol map are read as
 b<sub>(log<sub>2</sub>M)-1</sub> ... b<sub>0</sub>.

The bit stream returned after analyzing the complete waveform is reported as follows:

{b<sub>0</sub> ... b<sub>(log<sub>2</sub>M)-1</sub>}<sub>0</sub>
 {b<sub>0</sub> ... b<sub>(log<sub>2</sub>M)-1</sub>}<sub>1</sub>
 ... {b<sub>0</sub> ...
 b<sub>(log<sub>2</sub>M)-1</sub>}<sub>n-1</sub>

where M is the M-ary and n is the number of symbols
 analyzed.

The amplitude levels are as shown below.

[IMAGE alt='image' src='GUID-6B47D8D5-6064-4151-87AE-00CA482A3D1C-a5.gif']

[IMAGE alt='image' src='GUID-CF5543CE-53F3-42F9-808B-FAFAA52789F9-a5.gif']

[IMAGE alt='image' src='GUID-FE0CAE8E-F08E-45EF-881F-356673D62642-a5.gif']

Parent topic:

Modulation Types

<!--NI_TOPIC bundle=rfmx-demod path=analog-demod.html language=enus -->
## TOPIC 00004: Analog Demodulation

- bundle_id: `rfmx-demod`
- source_path: `analog-demod.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod/raw/resource/enus/analog-demod.html
- document_id: `rfmx-demod`
- page_type: `leaf`
- content_type: `concept`
- source_description: Analog demodulation (ADEM) is the process of recovering the message signal from an analog modulated signal. Let c(t)=A[c]e^j(2πf[c]t + θ[c]) be the carrier that is modulated by the message signal m(t), with a maximum message frequency content of f[m] Hz. where A[c][]is the carrier amplitude f[c][] i

### Analog Demodulation

Analog demodulation (ADEM) is the process of recovering the message signal from an
 analog modulated signal.

Let c(t)=A<sub>c</sub>e<sup>j(2πf<sub>c</sub>t + θ<sub>c</sub>)</sup> be the carrier that
 is modulated by the message signal m(t), with a maximum message frequency content of
 f<sub>m</sub> Hz.

- A c is the carrier amplitude
- f c is the carrier frequency
- θ c is the carrier phase

The following table shows the types of analog modulation based on the carrier parameter
 being varied by the message signal.

| Modulation Type | Transmitted Signal | Bandwidth |
| --- | --- | --- |
| Amplitude modulation double sideband with carrier (AM DSB) | where k is the modulation depth, usually expressed as a percentage of Ac | 2*fm |
| Amplitude modulation double sideband with carrier suppressed (AM DSBSC) |  | 2*fm |
| Frequency modulation (FM) | where fd is the frequency deviation, in Hz | 2(fm+fd) |
| Phase modulation (PM) | where θd is the phase deviation in degrees. |  |

To measure the transmit quality, the analyzer must acquire a signal with bandwidth
 greater than the minimum bandwidth. Specify the acquisition bandwidth by configuring the
 RBW filter to be used. RFmx recommends that you use a Flat Top RBW filter. The analyzer
 signal processing chain is as shown in the following image.

Figure 1.

[IMAGE alt='Analyzer Signal Processing Chain Diagram' src='GUID-193B2E72-080A-4D2A-A4A7-1E687210BE8E-a5.gif']

The demodulator recovers the message signal based on the modulation type specified. For
 demodulating AM signals, specify whether the carrier is suppressed, in order to recover
 the message signal amplitude correctly. For demodulating FM and PM signals, specify
 whether the demodulator needs to correct the carrier frequency error. Carrier phase
 error correction is applicable only for PM signals.

Often, audio signals are pre-emphasized before frequency modulation. At the receiver, a
 de-emphasis filter is used on the demodulated signal to compensate for the pre-emphasis
 applied at the transmitter. This filter is a low pass filter with a 6 dB/octave roll-off
 having the following transfer function.

[IMAGE alt='image' src='GUID-5857A733-B536-4AF6-8017-F6C8E3B58C60-a5.gif']

where τ is the de-emphasis filter time constant, in seconds

This filter is bypassed when the de-emphasis is 0 seconds. Typical de-emphasis time
 constant values used for FM are 50 μs and 75 μs.

Enable audio filtering to filter the demodulated signal. The following table shows the
 response of supported audio filter types.

| Audio Filter Type | Filter Response |
| --- | --- |
| Custom | A band pass filter is designed using the specified lower and upper cut off frequency. |
| A-Weight |  |
| B-Weight |  |
| C-Weight |  |
| CCITT |  |
| ITU-R 468-4 |  |

The following table shows the sample rate of the demodulated signal. The sample rate
 updates based on the filter settings.

| Audio Filter Type | Demodulated Signal Sample Rate (Hz) |
| --- | --- |
| None | 1.25 * RBW |
| Custom | 2 * upper cut off frequency |
| Others | 100 kHz |

<!--NI_TOPIC bundle=rfmx-demod path=bits.html language=enus -->
## TOPIC 00005: Bits

- bundle_id: `rfmx-demod`
- source_path: `bits.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod/raw/resource/enus/bits.html
- document_id: `rfmx-demod`
- page_type: `leaf`
- content_type: `concept`
- source_description: Demodulated PSK ,QAM and APSK signals are known to have ambiguity in phase if the transmitted signal is not known. If this phase ambiguity is not resolved, the hard decision of symbols returns in incorrect bits. Some communication schemes resolve the phase ambiguity issue by using differential mappi

### Bits

Demodulated PSK ,QAM and APSK signals are known to have ambiguity in phase if the transmitted
 signal is not known. If this phase ambiguity is not resolved, the hard decision of symbols
 returns in incorrect bits.

Some communication schemes resolve the phase ambiguity issue by using differential mapping. Refer
 to *Phase Shift Keying* for more information about differential mapping.

Another solution to the issue is to transmit a known bit pattern to the receiver. Such
 known bit patterns are called synchronization bits. When synchronization is enabled, the
 demodulator attempts to find the phase ambiguity using the known bits.

If synchronization bits are found, the demodulator corrects for phase ambiguity, and then the
 signal from this location is used for the measurement. You can
 specify a measurement that offset from this synchronized
 location. In this case, the number of symbols measured for
 transmit quality might be less than the specified number of
 symbols.

If synchronization bits are not found in the measurement interval, the demodulator uses
 all the symbols acquired for measuring the transmit quality.

In some communication schemes, synchronization bits are used to mark the start of message
 frame. Enable bit synchronization to measure only the signal corresponding to the
 message frame.

Specify the synchronization bits, read from left to right, as shown below.

{b<sub>0</sub> ... b<sub>(log<sub>2</sub>M)-1</sub>}<sub>0</sub> {b<sub>0</sub> ...
 b<sub>(log<sub>2</sub>M)-1</sub>}<sub>1</sub> ... {b<sub>0</sub> ...
 b<sub>(log<sub>2</sub>M)-1</sub>}<sub>n-1</sub>

- M is the M-ary.
- n is the number of symbols
 that form the synchronization pattern.

The length of the synchronization bits are truncated to an integer multiple of
 log<sub>2</sub>M bits per symbol.

Note

Filters

Parent topic:

Digital Demodulation

Related concepts:

- Phase Shift Keying
- Filters

<!--NI_TOPIC bundle=rfmx-demod path=burst-detection.html language=enus -->
## TOPIC 00006: Burst Detection

- bundle_id: `rfmx-demod`
- source_path: `burst-detection.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod/raw/resource/enus/burst-detection.html
- document_id: `rfmx-demod`
- page_type: `leaf`
- content_type: `concept`
- source_description: A signal that has significant power for a known duration is defined as a burst signal. This signal has no power (dead time) outside the known duration. To demodulate such signals, the dead time must be avoided. There are two ways to ensure that the intended part of the signal is used for demodulatio

### Burst Detection

A signal that has significant power for a known duration is defined as a burst signal. This
 signal has no power (dead time) outside the known duration. To demodulate such signals, the
 dead time must be avoided. There are two ways to ensure that the intended part of the
 signal is used for demodulation and measurement.

- Configuring the signal structure as Continuous
- Configuring the signal structure as Bursted

#### Configuring Signal Structure as Continuous

Configure a trigger to align acquisition to the burst. Specify the number of symbols such
 that the measurement interval does not exceed the burst duration from the start of trigger.
 The following equation illustrates the relationship between the measurement interval and
 number of symbols.

[IMAGE alt='image' src='GUID-75198CDE-3BE9-418F-9AE0-1298829EFF8B-a5.gif']

The analyzer acquires an additional duration to account for filter delays in the
 measurement.

The EVM at the two ends of the burst might be higher when the signal beyond the burst
 duration is acquired. Reduce the number of symbols and configure trigger delay so that only
 the intended part of the burst is used for demodulation and measurement.

#### Configuring Signal Structure as Bursted

Configure a trigger to align acquisition to the burst with Signal Structure property set to
 Bursted. The demodulator will detect the falling edge of the
 first burst which can occur anywhere within the defined measurement interval. However, the
 measurement will NOT be detecting the rising edge of the burst and hence,
 you need to give appropriate trigger settings. The trigger point will be considered as the
 start of the burst.

The following equation illustrates the relationship between the Measurement Interval,
 Number Of Symbols, Burst Start Exclusion Symbols, and Burst End Exclusion Symbols.

[IMAGE alt='image' src='GUID-1C9C68F8-6532-4DA7-B522-2458C1C9932C-a5.gif']

Acquisition Time is calculated using the following equation.

[IMAGE alt='image' src='GUID-DC596880-1FB1-424C-9074-D99419D3BFD2-a5.gif']

Where, Burst Start Exclusion Symbol specifies the number of symbols from the start of the
 burst trigger that is excluded from the measurement, and Burst End Exclusion Symbols
 specifies the number of symbols that is excluded from the measurement before the falling
 edge of the burst.

If the signal is bursty, NI recommends that you set the Signal Structure property to
 Bursted.

Symbols beyond the detected falling edge of the first burst are not used for demodulation.

In all the following images, Acquisition Length does not show the extra
 acquisitions done for filter delays.

[IMAGE alt='image' src='GUID-060E322F-A03B-48E3-A8CE-A15BE49B1B43-a5.gif']

If the burst length is less than the acquisition length, then the burst analysis algorithm
 will detect the falling edge well within the acquisition length. In such a case, the number
 of symbols is coerced to a lower value such that the Burst Length = Burst Start Exclusion
 Symbols + Number Of symbols + Burst End Exclusion Symbols. This is illustrated in the
 following image.

[IMAGE alt='image' src='GUID-AF12D368-CAA2-4424-9C1B-A4C28E3D255F-a5.gif']

If the burst length is greater than the acquisition length, then the measurement will not
 find the falling edge within the acquisition length. In such a case, the number of symbols
 is not coerced and the specified number of symbols is used for demodulation, as illustrated
 in the following image.

[IMAGE alt='image' src='GUID-C025B9CA-F167-48B8-895D-79199590220C-a5.gif']

Parent topic:

Digital Demodulation

<!--NI_TOPIC bundle=rfmx-demod path=custom-filters.html language=enus -->
## TOPIC 00007: Custom Filters

- bundle_id: `rfmx-demod`
- source_path: `custom-filters.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod/raw/resource/enus/custom-filters.html
- document_id: `rfmx-demod`
- page_type: `leaf`
- content_type: `concept`
- source_description: The filter coefficients must be provided in the following format. Filter Coefficient Description y Specifies the array coefficients of the custom filter. dx Specifies the spacing between the coefficients as a fraction of the symbol. If four coefficients correspond to one symbol, the spacing is 1/4.

### Custom Filters

The filter coefficients must be provided in the following format.

| Filter Coefficient | Description |
| --- | --- |
| y | Specifies the array coefficients of the custom filter. |
| dx | Specifies the spacing between the coefficients as a fraction of the symbol. If four coefficients correspond to one symbol, the spacing is 1/4. |
| x0 | Specifies the start index of the coefficients such that the center coefficient occurs at index 0. |

[IMAGE alt='image' src='GUID-1A7F8929-8C0E-4172-B0F4-2F03783B2A5B-a5.gif']

Parent topic:

Filters

<!--NI_TOPIC bundle=rfmx-demod path=digital-demod.html language=enus -->
## TOPIC 00008: Digital Demodulation

- bundle_id: `rfmx-demod`
- source_path: `digital-demod.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod/raw/resource/enus/digital-demod.html
- document_id: `rfmx-demod`
- page_type: `leaf`
- content_type: `concept`
- source_description: Digital demodulation (DDEM) is the process of recovering the message bits from a digital modulated signal. This process includes the estimation and correction for carrier and channel impairments introduced between transmission and reception. The signal that is corrected for impairments is used for m

### Digital Demodulation

Digital demodulation (DDEM) is the process of recovering the message bits from a
 digital modulated signal.

This process includes the estimation and correction for carrier and channel impairments
 introduced between transmission and reception. The signal that is corrected for
 impairments is used for measurement of modulation accuracy.

Figure 2.

[IMAGE alt='Digital Signal Processing Chain for Measuring the Transmission Quality of Digital Modulated Schemes' src='GUID-435240E0-B22A-426B-98E7-A939F7EE6820-a5.gif']

To demodulate the signal, you must know the following parameters.

- Transmitter parameters:
  - ModulationType, M-ary
  - Symbol Rate
  - Pulse Shaping Filter
- Analysis parameters:
  - Samples per Symbol
  - Number of Symbols
  - Measurement Filter

To recover bits correctly, specify the following parameters:

- Symbol Map
- Differential/Normal Symbol Map, Bit Encoding
- Synchronization Bits

<!--NI_TOPIC bundle=rfmx-demod path=equalization.html language=enus -->
## TOPIC 00009: Equalization

- bundle_id: `rfmx-demod`
- source_path: `equalization.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod/raw/resource/enus/equalization.html
- document_id: `rfmx-demod`
- page_type: `leaf`
- content_type: `concept`
- source_description: An adaptive feed‑forward equalizer compensates channel and filter effects, reduces intersymbol interference, and improves demodulation accuracy. When analyzing a modulated signal, the error vector magnitude might be higher in the following cases: The exact parameters of the transmit filter is unknow

### Equalization

An adaptive feed‑forward equalizer compensates channel and filter effects,
 reduces intersymbol interference, and improves demodulation
 accuracy.

When analyzing a modulated signal, the error vector magnitude might be higher in the following
 cases:

- The exact parameters of the transmit filter is unknown.
- The measurement filter that the analyzer uses is
 unknown.
- A channel exists between the transmitter and the analyzer.

The measurement implements an adaptive feed-forward equalizer, which implies that the
 equalizer filter taps adapt their coefficients to compensate for the action of the
 channel filter or any other filter. This adaptation ensures that the convolution of the
 channel filter and the equalizer coefficient filter yields a delta function, thereby
 removing any inter symbol interference in the equalized output complex waveform. The
 adaptive feed-forward equalizer uses a feed-forward adaptive least-mean-squared (LMS)
 algorithm to adjust the equalizer taps.

ASK, PSK, QAM, and APSK modulation types support equalization. SOQPSK does not support
 equalization.

At the start of the equalization process, you must set the equalizer mode to Train for
 iterations specified by training count. The equalizer tap spacing is specified by the
 number of taps per symbol. The incremental amount by which the equalizer taps adapt is
 controlled by specifying the convergence factor. A smaller value of the convergence
 factor requires a larger number of iterations to adapt the equalizer, and it provides a
 better estimate of the channel. The training starts with an impulse as the initial
 coefficients.

After training, the equalizer coefficients are applied before the demodulation
 process.

To continue training of the equalizer in further iterations, specify the previous
 equalizer coefficients as the initial coefficients, with equalizer mode set to
 Train.

Refer to the Custom Filters topic for more information about how to specify the
 coefficients and the coefficient spacing.

After verifying that the channel has been accurately represented by the equalizer, the
 equalizer mode can be set to Hold to stop adapting and use the coefficients prior to the
 demodulation process.

Parent topic:

Digital Demodulation

Related concepts:

- Custom Filters

<!--NI_TOPIC bundle=rfmx-demod path=error-vector-magnitude.html language=enus -->
## TOPIC 00010: Error Vector Magnitude

- bundle_id: `rfmx-demod`
- source_path: `error-vector-magnitude.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod/raw/resource/enus/error-vector-magnitude.html
- document_id: `rfmx-demod`
- page_type: `leaf`
- content_type: `concept`
- source_description: Error Vector Magnitude (EVM) is a measure of demodulator performance in the presence of impairments. The demodulated symbols are compared against ideal symbol locations over the measurement window to measure EVM, magnitude error, and phase error. The following image shows the comparison of demodulat

### Error Vector Magnitude

Error Vector Magnitude (EVM) is a measure of demodulator performance in the presence
 of impairments.

The demodulated symbols are compared against ideal symbol locations over the measurement window
 to measure EVM, magnitude error, and phase error.

The following image shows the comparison of demodulated symbols against ideal symbol
 locations.

Figure 5.

[IMAGE alt='Comparison of Demodulated Symbols Against Ideal Symbol Locations' src='GUID-CBA3499D-4731-43CC-8F3C-3102C3F74561-a5.gif']

[IMAGE alt='image' src='GUID-62378FEE-CA43-4FB1-98B5-3192BCD294B5-a5.gif']

[IMAGE alt='image' src='GUID-6C1AF48B-7189-4EAB-9422-29CBEB4C118C-a5.gif']

where

I<sub>n</sub>+jQ<sub>n</sub> is
 the vector representing the symbol being measured at index
 n
[IMAGE alt='image' src='GUID-168C0C7E-A308-4305-A51B-57A9DB6C7AFA-a5.gif'] is the ideal vector close to the actual symbol
 being measured

N is the number of symbols to be measured

[IMAGE alt='image' src='GUID-21E974B6-0602-4806-AD56-F6BDF301D045-a5.gif']

Note

- The EVM normalization parameter is supported only for QAM and APSK modulations.
- EVM measured on OQPSK symbols uses two samples per symbol
 because the maximum instance of I and Q are separated by half
 the symbol duration.
- Offset EVM in OQPSK is measured on symbols after aligning the I
 and Q channels by removing the half symbol duration in the Q
 channel.

Parent topic:

Measurements

<!--NI_TOPIC bundle=rfmx-demod path=filters.html language=enus -->
## TOPIC 00011: Filters

- bundle_id: `rfmx-demod`
- source_path: `filters.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod/raw/resource/enus/filters.html
- document_id: `rfmx-demod`
- page_type: `leaf`
- content_type: `concept`
- source_description: Configure custom filters within RFmx Demod to tailor measurement processing to specific signal‑analysis needs. After the transmitter maps bits to symbols, it generates a stream of rectangular‑pulse symbols. Because these pulses include sharp transition, you must limit the bandwidth of the signal to

### Filters

Configure custom filters within RFmx Demod to tailor
 measurement processing to specific signal‑analysis needs.

After the transmitter maps bits to symbols, it generates a stream of rectangular‑pulse symbols.
 Because these pulses include sharp transition, you must limit the bandwidth of the signal
 to be transmitted. To smoothen the symbol transitions, these pulses are shaped using a
 pulse-shaping filter. Filters such as root-raised cosine (RRC) introduce
 intersymbol interference (ISI). During demodulation, a receiver filter
 restricts the demodulation signal bandwidth, maximizes the signal-to-noise ratio, and
 removes ISI in the signal. This receiver filter is also known as the matched
 filter.

- Symbol timing
- Carrier frequency offset
- Phase offset

In most modulation schemes, the matched filter is used as the measurement filter. If you
 set the Measurement Filter Type property to
 Auto, use the following table to determine the measurement
 filter.

| Modulation Type | Pulse-Shaping Filter | Measurement Filter | Reference Filter |
| --- | --- | --- | --- |
| ASK, FSK, PSK, QAM, APSK, MSK | Rectangular | Rectangular | Rectangular ⊗ Rectangular |
| ASK, FSK, PSK, QAM, APSK, MSK | Raised Cosine | None | Raised Cosine |
| ASK, FSK, PSK, QAM, APSK, MSK | Root-Raised Cosine | Root-Raised Cosine | Root-Raised Cosine |
| FSK, MSK | Gaussian | None | Gaussian |
| PSK | Linearized GMSK-EDGE | None | Linearized GMSK-EDGE ⊗ Windowed RC-EDGE |
| PSK | Half Sine | None | Half Sine |
| PSK | SOQPSK-TG | None | SOQPSK-TG |

Note

To demodulate the EDGE PSK signals, consider the following factors.

- When you set the Pulse Shaping Filter to Linearized
 GMSK-EDGE , a standard-specific filter is selected, as defined by
 ETSI GSM 05.04 
 [[1]](#note-d961e221) [<sup>1</sup>](#fnsrc_1-d961e221) Digital cellular telecommunications system (Phase 2+); Modulation (GSM 05.04
 version 8.1.2 Release 1999). .
- When you set Measurement Filter to None , a standard-specific
 filter is selected, as defined by ETSI GSM 05.05, chapter 4.6 Modulation Accuracy
 [[2]](#note-d961e230) [<sup>2</sup>](#fnsrc_2-d961e230) 3rd Generation Partnership Project; Technical Specification Group GSM/EDGE
 Radio Access Network; Radio transmission and reception (Release 1999). .
- The alpha of the above filters is fixed and its value does not affect the filters.

The bits recovered from the demodulation process are re-modulated using a reference filter to
 obtain a reference waveform. The measurement waveform is compared against this reference waveform
 to measure error vector and waveform correlation factor (Rho).

A reference filter is defined as shown in the following equation:

[IMAGE alt='image' src='GUID-755EFEBF-AB9E-401F-B305-F979C9ABDECA-a5.gif']

To provide pulse shaping and measurement filters, specify the filter type as
 Custom.

For more information about how to specify the filter coefficients and the coefficient spacing,
 refer to *Custom Filters*.

#### Measurement Filter Information

| Number of Coefficients | Size for FSK | Size for MSK | Size for PSK | Size for QAM/ASK/APSK |
| --- | --- | --- | --- | --- |
| Rectangular | (samples/symbol) | (samples/symbol) | (samples/symbol) | (samples/symbol) |
| Raised Cosine | 1 | 1 | 1 | 1 |
| Root-Raised Cosine | 1 + (samples/symbol) * filter length | 1 + (samples/symbol) * filter length | 1 + (samples/symbol) * filter length | 1 + (samples/symbol) * filter length |
| Gaussian | 14 * (samples/symbol) + 1 | 3 * (samples/symbol) - 1 | N/A | N/A |
| Windowed RC-EDGE | N/A | N/A | 1 + 15 * (samples/symbol) | N/A |
| Half Sine | N/A | N/A | 1 | N/A |
| SOQPSK-TG | N/A | N/A | 1 + 5 * (samples/symbol) | N/A |

Note

Filter length = 20 if alpha
 ≥ 0.2

Filter length = 40 if alpha < 0.2

Parent topic:

Digital Demodulation

Related concepts:

- Custom Filters

[<sup>1</sup>](#note_ref-d961e221) Digital cellular telecommunications system (Phase 2+); Modulation (GSM 05.04
 version 8.1.2 Release 1999).

[<sup>2</sup>](#note_ref-d961e230) 3rd Generation Partnership Project; Technical Specification Group GSM/EDGE
 Radio Access Network; Radio transmission and reception (Release 1999).

<!--NI_TOPIC bundle=rfmx-demod path=frequency-shift-keying.html language=enus -->
## TOPIC 00012: Frequency-shift Keying

- bundle_id: `rfmx-demod`
- source_path: `frequency-shift-keying.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod/raw/resource/enus/frequency-shift-keying.html
- document_id: `rfmx-demod`
- page_type: `leaf`
- content_type: `concept`
- source_description: FSK refers to a type of frequency modulation that assigns bit values to discrete frequency levels. The supported M-ary values for FSK are 2, 4, 8, and 16. The FSK demodulator uses the discrete levels in frequency as the symbol map. The recovered frequency symbol closest to the ideal symbol in the ma

### Frequency-shift Keying

FSK refers to a type of frequency modulation that assigns bit values to discrete
 frequency levels. The supported M-ary values for FSK are 2, 4, 8, and 16.

The FSK demodulator uses the discrete levels in frequency as the symbol map. The
 recovered frequency symbol closest to the ideal symbol in the map decides the bits it
 represents. The bits mentioned in the symbol map are read as
 b<sub>(log<sub>2</sub>M)-1</sub> ...
 b<sub>0</sub>.

The bit stream returned after analyzing the complete waveform is reported as follows:

{b<sub>0</sub> ...
 b<sub>(log<sub>2</sub>M)-1</sub>}<sub>0</sub>
 {b<sub>0</sub> ...
 b<sub>(log<sub>2</sub>M)-1</sub>}<sub>1</sub>
 ... {b<sub>0</sub> ...
 b<sub>(log<sub>2</sub>M)-1</sub>}<sub>n-1</sub>

where M is the M-ary and n is the number of symbols
 analyzed.

Let f<sub>d</sub> be the frequency deviation of the modulated signal. Then, for a
 specified M-ary, the frequency levels are defined as follows:

f<sub>i</sub> = -f<sub>d</sub> + 2if<sub>d</sub>/(M-1)

where 0 >= i < = M-1

The default symbol map is as shown in the following equations:

[IMAGE alt='image' src='GUID-856DCDAE-9F20-42A4-A126-2A1FDBBC59BF-a5.gif']

[IMAGE alt='image' src='GUID-5B09C30B-4C3D-4F2D-8482-1EADE0CF022B-a5.gif']

[IMAGE alt='image' src='GUID-75DAEDC9-1B8C-4763-9DB1-8FFBAB39424F-a5.gif']

[IMAGE alt='image' src='GUID-91F13724-D0BD-455F-85E4-F59D36C91AE7-a5.gif']

Parent topic:

Modulation Types

<!--NI_TOPIC bundle=rfmx-demod path=fsk-measurements.html language=enus -->
## TOPIC 00013: Frequency-Shift Keying Measurements

- bundle_id: `rfmx-demod`
- source_path: `fsk-measurements.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod/raw/resource/enus/fsk-measurements.html
- document_id: `rfmx-demod`
- page_type: `leaf`
- content_type: `concept`
- source_description: In frequency modulation, frequency deviation refers to the maximum difference between the instantaneous frequency of the modulated wave and the carrier frequency. For an M-FSK system, RMS FSK error is the measure of modulation error and is defined as the RMS of the difference of the measured and the

### Frequency-Shift Keying Measurements

In frequency modulation, frequency deviation refers to the maximum difference between the
 instantaneous frequency of the modulated wave and the carrier frequency.

For an M-FSK system, RMS FSK error is the measure of modulation error and is defined as
 the RMS of the difference of the measured and the reference FSK symbols.

If f<sub>ref</sub> is the transmitted symbol and f<sub>received</sub> is the received
 symbol, the measured frequency symbol f<sub>meas,n</sub> is as shown in the following
 equation.

[IMAGE alt='image' src='GUID-B767F55F-80E0-4DC1-97B1-A059BDB16CC6-a5.gif']

[IMAGE alt='image' src='GUID-4633625F-6165-4F5E-8A9C-2B802B980771-a5.gif']

where

[IMAGE alt='image' src='GUID-2EE4C3C2-E3E1-4241-8B43-CD62F24F905A-a5.gif']is the carrier frequency error

α is the gain between measured symbol and the reference
 symbol

[IMAGE alt='image' src='GUID-890D3390-C771-4C06-B3DF-CE5BA3E67B50-a5.gif']N is the number of
 symbols

[IMAGE alt='image' src='GUID-8E97373F-8E1A-41FD-8DDA-46175DA3A04E-a5.gif']

[IMAGE alt='image' src='GUID-C9996677-37F3-4592-8AEF-211852F23261-a5.gif']

where

[IMAGE alt='image' src='GUID-25D4D6FA-85D8-4F33-801F-153DC5EAE2DA-a5.gif']

Parent topic:

Measurements

<!--NI_TOPIC bundle=rfmx-demod path=iq-impairments.html language=enus -->
## TOPIC 00014: I/Q Impairments

- bundle_id: `rfmx-demod`
- source_path: `iq-impairments.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod/raw/resource/enus/iq-impairments.html
- document_id: `rfmx-demod`
- page_type: `leaf`
- content_type: `concept`
- source_description: In a quadrature modulated (QM) system, the ideal QM waveform is the sum of the I and Q components of the signal, as shown in the following equation. where, i(t) is the baseband I waveform q(t)is the baseband Q waveform The practical QM waveform differs from the ideal QM waveform. A generalized adjus

### I/Q Impairments

In a quadrature modulated (QM) system, the ideal QM waveform is the sum of the I and Q
 components of the signal, as shown in the following equation.

[IMAGE alt='image' src='GUID-D4BF61D8-8743-4D24-B0B9-FC312E0B8482-a5.gif']

where,

i(t) is the baseband I waveform

q(t)is the baseband Q waveform

The practical QM waveform differs from the ideal QM waveform. A generalized adjusted QM
 waveform can be expressed as shown in the following equation.

[IMAGE alt='image' src='GUID-A71E7FD1-6EA0-4C99-B3EC-F55F835B8F06-a5.gif']

[IMAGE alt='image' src='GUID-4BF0599D-4A36-4D74-98CF-EEAEC5A3B774-a5.gif']

and,

g is the gain imbalance

φ is the quadrature skew

Δ<sub>I</sub> is the in-phase DC offset

Δ<sub>Q</sub> is the quadrature-phase DC
 Offset

The vector sum of the in-phase DC offset and the quadrature –phase DC offset results in
 origin offset.

#### Origin offset

The origin offset, measured in dB, is the distance between the ideal constellation
 center to the actual constellation center, as shown in the following figure.

[IMAGE alt='image' src='GUID-95DD6C8E-9144-41B4-8C9F-1807F9F364F9-a5.gif']

Before measuring EVM, the symbols are corrected for origin offset.

#### I/Q Gain Imbalance

I/Q gain imbalance refers to the difference in scaling
 between the I and Q components of I/Q
 data.

When expressed in dB, I/Q gain imbalance
 can be either positive or negative, with the sign
 indicating which component has been impaired, as
 denoted in the following figure.

[IMAGE alt='image' src='GUID-85323B8D-E8A6-42F0-B8E7-B8AFEF074E0B-a5.gif']

#### Quadrature Skew

Quadrature skew describes a complex signal impairment of the
 I and Q components that are not perfectly
 orthogonal.

Quadrature skew can be either
 positive or negative, with the sign indicating the
 orientation of the error, as shown in the following
 figure.

[IMAGE alt='image' src='GUID-FD183641-BEB2-45F5-8BA8-1E9EFA00E5D3-a5.gif']

Parent topic:

Measurements

<!--NI_TOPIC bundle=rfmx-demod path=magnitude-error.html language=enus -->
## TOPIC 00015: Magnitude Error

- bundle_id: `rfmx-demod`
- source_path: `magnitude-error.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod/raw/resource/enus/magnitude-error.html
- document_id: `rfmx-demod`
- page_type: `leaf`
- content_type: `concept`
- source_description: Magnitude error is the difference between the magnitude of the vector representing the demodulated symbol and the ideal vector. where I[n]+jQ[n] is the vector representing the symbol being measured at index n is the ideal vector close to the actual symbol being measured N is the number of symbols

### Magnitude Error

Magnitude error is the difference between the magnitude of the vector representing the
 demodulated symbol and the ideal vector.

[IMAGE alt='image' src='GUID-79AB0B68-538C-43F8-95AE-0E7033F26646-a5.gif']

[IMAGE alt='image' src='GUID-1996D599-7DC6-4839-AA3B-4B6713AE1A1C-a5.gif']

[IMAGE alt='image' src='GUID-A23E8EF0-4A92-4094-8A5D-E8AB6B3DE4A9-a5.gif']

where

I<sub>n</sub>+jQ<sub>n</sub>
 is the vector representing the symbol being measured at index
 n

[IMAGE alt='image' src='GUID-168C0C7E-A308-4305-A51B-57A9DB6C7AFA-a5.gif'] is the ideal vector close to the actual symbol
 being measured

N is the number of symbols to be measured.

Parent topic:

Measurements

<!--NI_TOPIC bundle=rfmx-demod path=measurements-overview.html language=enus -->
## TOPIC 00016: Measurements

- bundle_id: `rfmx-demod`
- source_path: `measurements-overview.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod/raw/resource/enus/measurements-overview.html
- document_id: `rfmx-demod`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following table shows the measurements supported by each modulation type. 11 Supported Measurements per Modulation Type Measurement TypeSupported MeasurementModulation Type Carrier measurements Mean frequency offset (Hz) ASK, FSK, PSK, QAM, APSK, MSK Mean frequency drift (Hz) ASK, FSK, PSK, QAM,

### Measurements

The following table shows the measurements supported by each modulation type.

| Measurement Type | Supported Measurement | Modulation Type |
| --- | --- | --- |
| Carrier measurements | Mean frequency offset (Hz) | ASK, FSK, PSK, QAM, APSK, MSK |
| Mean frequency drift (Hz) | ASK, FSK, PSK, QAM, APSK, MSK |  |
| Mean phase offset (degrees) | ASK, PSK, QAM, APSK |  |
| Error vector magnitude | Mean RMS EVM (%) | ASK, PSK, QAM, APSK, MSK |
| Mean peak EVM (%) | ASK, PSK, QAM, APSK, MSK |  |
| Maximum RMS EVM (%) | ASK, PSK, QAM, APSK, MSK |  |
| Maximum peak EVM (%) | ASK, PSK, QAM, APSK, MSK |  |
| Mean MER (dB) | ASK, PSK, QAM, APSK, MSK |  |
| Mean RMS offset EVM (%) | Offset QPSK, SOQPSK |  |
| Mean peak offset EVM (%) | Offset QPSK, SOQPSK |  |
| Maximum RMS offset EVM (%) | Offset QPSK, SOQPSK |  |
| Maximum peak offset EVM (%) | Offset QPSK, SOQPSK |  |
| Magnitude error | Mean magnitude error (%) | ASK, FSK, PSK, QAM, APSK, MSK |
| Maximum magnitude error (%) | ASK, FSK, PSK, QAM, APSK, MSK |  |
| Phase error | Mean phase error (%) | ASK, PSK, QAM, APSK, MSK |
| Maximum phase error (%) | ASK, PSK, QAM, APSK, MSK |  |
| FSK measurements | Frequency deviation (Hz) | FSK |
| Mean RMS deviation error (Hz) | FSK |  |
| Maximum peak deviation error (Hz) | FSK |  |
| I/Q impairments | Mean I/Q origin offset (dB) | ASK, PSK, QAM, APSK, MSK |
| Mean I/Q gain imbalance (dB) | PSK, QAM, APSK, MSK |  |
| Mean quadrature skew (degrees) | PSK, QAM, APSK, MSK |  |
| Miscellaneous | Mean Rho factor | PSK, QAM, APSK, MSK |
| Mean amplitude droop (dB/Symbol) | PSK, QAM, APSK, MSK |  |

<!--NI_TOPIC bundle=rfmx-demod path=measurements.html language=enus -->
## TOPIC 00017: Measurements

- bundle_id: `rfmx-demod`
- source_path: `measurements.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod/raw/resource/enus/measurements.html
- document_id: `rfmx-demod`
- page_type: `leaf`
- content_type: `concept`
- source_description: Carrier measurements include carrier frequency offset (applicable for FM and PM) and phase offset (applicable for PM). Modulation parameters include statistics of modulation depth (in case of AM), frequency deviation (in case of FM), and phase deviation (in case of PM). AM modulation depth is a meas

### Measurements

Carrier measurements include carrier frequency offset (applicable for FM and PM) and
 phase offset (applicable for PM).

Modulation parameters include statistics of modulation depth (in case of AM), frequency
 deviation (in case of FM), and phase deviation (in case of PM).

AM modulation depth is a measure of amplitude variation of the message signal around the
 carrier amplitude, and it is expressed as a percentage. If the AM carrier is suppressed,
 the modulation depth is the amplitude deviation from DC.

FM frequency deviation is the frequency variation, in Hz, around the nominal center.

PM phase deviation is the phase variation, in degrees, from the carrier phase.

To measure transmit signal quality, the analyzer performs the following distortion
 measurement on the demodulated signal. The distortions are measured on the demodulated
 signal spectrum obtained using a Hanning windowed FFT.

| Distortion Measurement | Equation |
| --- | --- |
| Signal in noise and distortion (SINAD) |  |
| Total harmonic distortion (THD) with noise |  |
| Total harmonic distortion |  |
| Signal-to-noise ratio (SNR) |  |

where

[IMAGE alt='image' src='GUID-3F0C471B-4160-4AC7-8CD6-FB60952692E6-a5.gif']

[IMAGE alt='image' src='GUID-00030F2B-3DFE-4CB8-A8F5-3D8388C0E2A0-a5.gif']

Parent topic:

Analog Demodulation

<!--NI_TOPIC bundle=rfmx-demod path=minimum-shift-keying.html language=enus -->
## TOPIC 00018: Minimum Shift Keying

- bundle_id: `rfmx-demod`
- source_path: `minimum-shift-keying.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod/raw/resource/enus/minimum-shift-keying.html
- document_id: `rfmx-demod`
- page_type: `leaf`
- content_type: `concept`
- source_description: Minimum-shift keying (MSK) is a special case of 2-FSK with a frequency deviation of 1/4 times the symbol rate. MSK uses a half-cycle sinusoidal pulse, thus making the phase change linear and keeping the side lobes low to control adjacent-channel interference. When differential encoding is enabled, t

### Minimum Shift Keying

Minimum-shift keying (MSK) is a special case of 2-FSK with a frequency deviation of 1/4
 times the symbol rate. MSK uses a half-cycle sinusoidal pulse, thus making the phase
 change linear and keeping the side lobes low to control adjacent-channel
 interference.

When differential encoding is enabled, the bits are encoded as
 y<sub>n</sub> = b<sub>n</sub> XOR
 b<sub>n-1</sub>, and then mapped according to the symbol
 map.

Parent topic:

Modulation Types

<!--NI_TOPIC bundle=rfmx-demod path=modulation-error-ratio.html language=enus -->
## TOPIC 00019: Modulation Error Ratio

- bundle_id: `rfmx-demod`
- source_path: `modulation-error-ratio.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod/raw/resource/enus/modulation-error-ratio.html
- document_id: `rfmx-demod`
- page_type: `leaf`
- content_type: `concept`
- source_description: Modulation Error Ration (MER) is a measure of the signal-to-noise ratio (SNR) in a digitally-modulated signal. MER is usually expressed in dB. MER over N symbols is defined as follows: where I[n]+jQ[n] is the vector representing the symbol being measured at index n is the ideal vector close to the a

### Modulation Error Ratio

Modulation Error Ration (MER) is a measure of the signal-to-noise ratio (SNR) in a
 digitally-modulated signal. MER is usually expressed in dB. MER over
 N symbols is defined as follows:

[IMAGE alt='image' src='GUID-8F973E1E-1820-4CE1-B56C-DD749B36F10B-a5.gif']

where

I<sub>n</sub>+jQ<sub>n</sub>
 is the vector representing the symbol being measured at index
 n

[IMAGE alt='image' src='GUID-168C0C7E-A308-4305-A51B-57A9DB6C7AFA-a5.gif'] is the ideal vector close to the actual symbol
 being measured

Nis the number of symbols

Parent topic:

Measurements

<!--NI_TOPIC bundle=rfmx-demod path=modulation-types.html language=enus -->
## TOPIC 00020: Modulation Types

- bundle_id: `rfmx-demod`
- source_path: `modulation-types.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod/raw/resource/enus/modulation-types.html
- document_id: `rfmx-demod`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following table shows the supported modulation types and the corresponding M-ary values. 6 Modulation Types and Corresponding M-ary Values Modulation Type M-ary ASK 2, 4, 8 FSK 2, 4, 8, 16 PSK 2, 4, 8, 16, OQPSK, SOQPSK, π/4-QPSK, π/8-8PSK, 3π/8-8PSK QAM 4, 8, 16, 32, 64, 128, 256, 512, 1024, 20

### Modulation Types

The following table shows the supported modulation types and the corresponding M-ary
 values.

| Modulation Type | M-ary |
| --- | --- |
| ASK | 2, 4, 8 |
| FSK | 2, 4, 8, 16 |
| PSK | 2, 4, 8, 16, OQPSK, SOQPSK, π/4-QPSK, π/8-8PSK, 3π/8-8PSK |
| QAM | 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096 |
| MSK | 2 |
| APSK | 16, 32 |

Note

- OQPSK, SOQPSK, π/4-QPSK, π/8-8PSK, and 3π/8-8PSK are configured using
 PSK format.
- PSK modulation types support differential symbol mapping.
- The MSK modulation type supports differential bit decoding.
- For SOQPSK modulation, Number of Symbols equals the data length
 in bits. Number of Symbols must be an even number.

Parent topic:

Digital Demodulation

<!--NI_TOPIC bundle=rfmx-demod path=new-features-and-changes.html language=enus -->
## TOPIC 00021: RFmx Demod New Features and Changes

- bundle_id: `rfmx-demod`
- source_path: `new-features-and-changes.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod/raw/resource/enus/new-features-and-changes.html
- document_id: `rfmx-demod`
- page_type: `leaf`
- content_type: `concept`
- source_description: Learn about updates, including new features and behavior changes, introduced in each version of RFmx Demod. Discover what is new in the latest releases of RFmx Demod.If you cannot find new features and changes for your version, it might not include user-facing updates. However, your version might in

### RFmx Demod
 New Features and Changes

Learn about updates, including new features and behavior changes, introduced in each
 version of RFmx Demod.

RFmx Demod

Note

Release Notes

Related information:

- Software and Driver Downloads

#### RFmx Demod
 2026 Q2 Changes

The RFmx Demod 2026 Q2 release adds new demodulation
 support, including shaped offset QPSK and 16-APSK/32-APSK. This release also adds support for Python API and for the
 PXIe-5841 with 200 MHz
 bandwidth.

##### New
 Features

This version of RFmx Demod
 adds support for the following features:

- Shaped Offset QPSK demodulation for SOQPSK-TG modulated waveforms.
- 16-APSK and 32-APSK 
 demodulation.
- Python API support.

##### New
 Hardware Support

This version of RFmx Demod adds
 support for the following hardware:

- PXIe-5841 ( 200 MHz ) bandwidth

Related concepts:

- Amplitude and Phase Shift Keying

#### RFmx Demod
 2025 Q3 Changes

Learn about new features, behavior changes, and other updates in RFmx Demod 2025 Q3.

##### New
 Features

This version of the RFmx Demod
 adds support for the following features:

- PXIe-5860 Self-Cal Validity Check

#### RFmx Demod
 2024 Q4 Changes

Learn about new features, behavior changes, and other updates in RFmx Demod 2024 Q4.

##### New
 Features

This version of the RFmx Demod
 adds support for the following features:

- Uninstalling RFmx Demod software also removes any
 previous versions of RFmx Demod .NET runtimes that
 were leaked in .NET Global Assembly Cache directory.

#### RFmx Demod
 2024 Q3 Changes

Learn about new features, behavior changes, and other updates in RFmx Demod 2024 Q3.

##### New
 Hardware Support

This version of the RFmx Demod adds support for the following
 hardware:

- PXIe-5860

#### RFmx Demod
 2024 Q2 Changes

Learn about new features, behavior changes, and other updates in RFmx Demod 2024 Q2.

##### New
 Features

This version of the RFmx Demod
 removes support for the following features:

- Obsoleted the RFmxInstr Load All Configurations VI. Use the
 RFmxInstr Load Configurations VI along with the
 appropriate RFmxInstr Load Options property, instead.

#### RFmx Demod 2023 Q4 Changes

Learn about new features, behavior changes, and other updates in RFmx Demod 2023 Q4.

##### New
 Features

This version of the RFmx Demod
 adds support for the following features:

- Obtaining unprocessed I/Q data utilized for RFmx measurements

#### RFmx Demod 2023 Q1 New Features and
 Changes

Learn about new features, behavior changes, and other updates in RFmx Demod 2023 Q1.

##### New
 Hardware Support

This version of the RFmx Demod adds support for the following
 hardware:

- Support for LabVIEW 2023 Q1 (64-bit)

#### RFmx Demod 2022 Q4 Changes

Learn about new features, behavior changes, and other updates in RFmx Demod 2022 Q4.

##### New
 Hardware Support

This version of the RFmx Demod adds support for the following
 hardware:

- Support for PXIe-5842

<!--NI_TOPIC bundle=rfmx-demod path=phase-error.html language=enus -->
## TOPIC 00022: Phase Error

- bundle_id: `rfmx-demod`
- source_path: `phase-error.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod/raw/resource/enus/phase-error.html
- document_id: `rfmx-demod`
- page_type: `leaf`
- content_type: `concept`
- source_description: Phase error is the difference between the phase of the vector representing the demodulated symbol and the ideal vector. where I[n] + jQ[n] is the vector representing the symbol being measured at index n is the ideal vector close to the actual symbol being measured N is the number of symbols to be m

### Phase Error

Phase error is the difference between the phase of the vector representing the
 demodulated symbol and the ideal vector.

[IMAGE alt='image' src='GUID-43778296-50CE-4768-AD1E-89329EEDC294-a5.gif']

[IMAGE alt='image' src='GUID-EE3495C6-4EB1-45DC-A47C-26C3569E34D3-a5.gif']

[IMAGE alt='image' src='GUID-C48AFE14-B94E-49EB-BCC4-404B000255BE-a5.gif']

where

I<sub>n</sub> +
 jQ<sub>n</sub> is the vector
 representing the symbol being measured at index
 n

[IMAGE alt='image' src='GUID-168C0C7E-A308-4305-A51B-57A9DB6C7AFA-a5.gif'] is the ideal vector close to the actual symbol
 being measured

Nis the number of symbols to be measured.

Parent topic:

Measurements

<!--NI_TOPIC bundle=rfmx-demod path=phase-shift-keying.html language=enus -->
## TOPIC 00023: Phase Shift Keying

- bundle_id: `rfmx-demod`
- source_path: `phase-shift-keying.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod/raw/resource/enus/phase-shift-keying.html
- document_id: `rfmx-demod`
- page_type: `leaf`
- content_type: `concept`
- source_description: Phase-shift keying (PSK) in digital transmission refers to a type of angle modulation in which the carrier phase is discretely varied to represent data being transmitted, either in relation to a reference phase or to the phase of the immediately preceding signal element. Modulation PSK Format M-ary

### Phase Shift Keying

Phase-shift keying (PSK) in digital transmission refers to a type of angle
 modulation in which the carrier phase is discretely varied to represent data
 being transmitted, either in relation to a reference phase or to the phase
 of the immediately preceding signal element.

| Modulation | PSK Format | M-ary | Differential |
| --- | --- | --- | --- |
| BPSK | Normal | 2 |  |
| DBPSK | Enable |  |  |
| QPSK | 4 |  |  |
| DQPSK | Enable |  |  |
| 8-PSK | 8 |  |  |
| D8-PSK | Enable |  |  |
| 16-PSK | 16 |  |  |
| D16-PSK | Enable |  |  |
| Offset QPSK | OQPSK | — |  |
| π/4-QPSK | π/4-QPSK | — |  |
| π/4-DQPSK | Enable |  |  |
| π/8-8PSK | π/8-8PSK | — |  |
| π/8-D8PSK | Enable |  |  |
| 3π/8-8PSK | 3π/8-8PSK | — |  |
| 3π/8-D8PSK | Enable |  |  |

#### Normal PSK

Demodulated bits correspond to the ideal symbol in the symbol map that is closest to the
 demodulated symbol.

The following images show the default symbol map used by each of the PSK modulation
 types.

[IMAGE alt='image' src='GUID-6727773E-970A-491B-8AA5-071602D49CD9-a5.gif']

[IMAGE alt='image' src='GUID-1AB7E4E6-9363-48C1-BBF8-3715863575ED-a5.gif']

#### Differential PSK

When differential mapping is enabled, the demodulated bits
 represent the phase transition between two
 consecutive symbols.

The default differential
 mapping used by each of the PSK modulation types is
 shown in the following images. The differential map
 is obtained using the Normal PSK map rotated by π/M
 radians, where M is the number of states in the
 map.

[IMAGE alt='image' src='GUID-3D2CDD2D-3590-4607-9522-63B4A6D9D799-a5.gif']

#### Offset QPSK (OQPSK)

During transmission using the OQPSK modulation scheme, the
 quadrature (Q) channel is offset by half the symbol
 period with respect to the in-phase (I) channel of
 the QPSK symbol.

To obtain demodulated bits
 during demodulation, the Q channel of the
 demodulated signal is unoffset by half the symbol
 duration to align with the I channel to get a QPSK
 constellation. These symbols are then mapped to bits
 using a process similar to that used in
 QPSK.

The measurement waveform samples are not
 compensated for the Q channel offset.

#### Shaped Offset QPSK
 (SOQPSK)

Shaped Offset QPSK (SOQPSK) is a
 continuous-phase modulation (CPM) variant of Offset
 QPSK in which the I and Q symbol transitions are
 offset by half a symbol period, as in OQPSK.
 Additionally, the symbol transitions pass through a
 pulse shaping filter. This shaping ensures
 constant-envelope behavior and controlled spectral
 characteristics, making SOQPSK more
 bandwidth-efficient.

After matched filtering,
 the demodulator removes the Q-channel offset by half
 symbol time to realign the I and Q symbol decisions,
 forming an equivalent QPSK-like symbol
 constellation.

The measurement waveform
 samples are not compensated for the Q channel
 offset.

#### π/4-QPSK

During transmission using the π/4-QPSK modulation scheme, the
 QPSK symbols are shifted by π/4 radians for every
 symbol, in a counter-clockwise
 direction.

During demodulation, the symbol
 phase is unshifted by π/4 for every symbol, in a
 clockwise direction, to get a QPSK constellation.
 These symbols are then mapped to bits using a
 process similar to that used in QPSK.

When
 differential mapping is enabled, the symbols are
 mapped to bits, thus representing the phase
 transition between two consecutive QPSK symbols. The
 measurement waveform samples are not compensated for
 the π/4 phase shift introduced by the modulation.
 Hence, the constellation looks like that of 8-PSK as
 shown in the following image.

[IMAGE alt='image' src='GUID-9A062F32-B3CB-413B-95A2-BDB7CA742A12-a5.gif']

#### π/8-8PSK

During transmission using the π/8-8PSK modulation scheme, the
 8-PSK symbols are shifted by π/8 radians for every
 symbol, in an anticlockwise direction.

During
 demodulation, the symbol phase is unshifted by π/8
 for every symbol, in a clockwise direction, to get
 an 8-PSK constellation. These symbols are then
 mapped to bits using a process similar to that used
 in 8-PSK.

When differential mapping is
 enabled, the symbols are mapped to bits, thus
 representing the phase transition between two
 consecutive 8-PSK symbols. The measurement waveform
 samples are not compensated for the π/8 phase shift
 introduced by the modulation. Hence, the
 constellation looks like that of 16-PSK, as shown in
 the following image.

[IMAGE alt='image' src='GUID-0D0E5F30-8182-4A83-828A-CD9607C261D8-a5.gif']

#### 3π/8-8PSK

During transmission using the 3π/8-8PSK modulation scheme,
 the 8-PSK symbols are shifted by 3π/8 radians for
 every symbol, in an anticlockwise
 direction.

During demodulation, the symbol
 phase is unshifted by 3π/8 for every symbol, in a
 clockwise direction, to get an 8-PSK constellation.
 These symbols are then mapped to bits using a
 process similar to that used in 8-PSK.

When
 differential mapping is enabled, the symbols are
 mapped to bits, thus representing the phase
 transition between two consecutive 8-PSK symbols.
 The measurement waveform samples are not compensated
 for the 3π/8 phase shift introduced by the
 modulation. Hence, the constellation is similar to
 that of 16-PSK, as seen in the following image.

[IMAGE alt='image' src='GUID-454F3CA0-957C-407B-8D26-DF3CE489C998-a5.gif']

Parent topic:

Modulation Types

<!--NI_TOPIC bundle=rfmx-demod path=quadrature-amplitude-modulation.html language=enus -->
## TOPIC 00024: Quadrature-amplitude Modulation

- bundle_id: `rfmx-demod`
- source_path: `quadrature-amplitude-modulation.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod/raw/resource/enus/quadrature-amplitude-modulation.html
- document_id: `rfmx-demod`
- page_type: `leaf`
- content_type: `concept`
- source_description: Quadrature-amplitude modulation (QAM) is a form of quadrature modulation in which both the carriers are amplitude-modulated. The following table shows the supported M-ary number for QAM. Modulation Type M-ary QAM 4, 8, 16, 32, 64, 128, 256, 512, 1,024, 2,048, 4,096 To get a reliable constellation, s

### Quadrature-amplitude Modulation

Quadrature-amplitude modulation (QAM) is a form of quadrature modulation in which both
 the carriers are amplitude-modulated. The following table shows the supported M-ary
 number for QAM.

| Modulation Type | M-ary |
| --- | --- |
| QAM | 4, 8, 16, 32, 64, 128, 256, 512, 1,024, 2,048, 4,096 |

To get a reliable constellation, specify the number of symbols that are greater than the
 minimum number specified in the following table.

| M-QAM | Minimum Number of Symbols |
| --- | --- |
| 4, 8, 16 | 500 |
| 32, 64, 128, 256 | 1,500 |
| 512, 1024 | 3,000 |
| 2048, 4096 | 5,000 |

The following images show the default symbol map used by each of the QAM modulation
 types.

[IMAGE alt='image' src='GUID-8591486A-F353-4260-9FCC-1C250EE5D31F-a5.gif']

[IMAGE alt='image' src='GUID-12061589-1C14-45A3-A26C-326F1360C6D7-a5.gif']

[IMAGE alt='image' src='GUID-07DB6DC6-CD22-4FAA-99E4-DC58D82225EC-a5.gif']

[IMAGE alt='image' src='GUID-26EE1F71-8C24-4F8A-B52F-B444F7BB73B7-a5.gif']

[IMAGE alt='image' src='GUID-6C056570-1CA2-4DE2-BDE7-84796D433999-a5.gif']

[IMAGE alt='image' src='GUID-A70C0BD0-E5D1-4949-8E55-5E59D51350DE-a5.gif']

[IMAGE alt='image' src='GUID-4F166DB1-B8D0-4DAF-862A-261EBC66D277-a5.gif']

Parent topic:

Modulation Types

<!--NI_TOPIC bundle=rfmx-demod path=rfmxdemod-overview.html language=enus -->
## TOPIC 00025: RFmx Demod Overview

- bundle_id: `rfmx-demod`
- source_path: `rfmxdemod-overview.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod/raw/resource/enus/rfmxdemod-overview.html
- document_id: `rfmx-demod`
- page_type: `leaf`
- content_type: `concept`
- source_description: This user manual contains introduction to RFmx Demod measurement concepts.

### RFmx Demod Overview

This user manual contains introduction to RFmx Demod measurement concepts.

<!--NI_TOPIC bundle=rfmx-demod path=rho.html language=enus -->
## TOPIC 00026: Rho

- bundle_id: `rfmx-demod`
- source_path: `rho.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod/raw/resource/enus/rho.html
- document_id: `rfmx-demod`
- page_type: `leaf`
- content_type: `concept`
- source_description: Rho (ρ) is a measure of correlation between the measurement waveform and the reference waveform that has been reconstructed using the demodulated bits. The value of ρ can range from 0 to 1.0, inclusive. Range of ρ Degree of Correlation ρ = 0 Uncorrelated 0 > ρ < 1 Partially correlated ρ = 1 Perfectl

### Rho

Rho (ρ) is a measure of correlation between the measurement waveform and the reference
 waveform that has been reconstructed using the demodulated bits. The value of ρ can
 range from 0 to 1.0, inclusive.

| Range of ρ | Degree of Correlation |
| --- | --- |
| ρ = 0 | Uncorrelated |
| 0 > ρ < 1 | Partially correlated |
| ρ = 1 | Perfectly correlated |

Parent topic:

Measurements

<!--NI_TOPIC bundle=rfmx-demod path=samples-per-symbol.html language=enus -->
## TOPIC 00027: Samples Per Symbol

- bundle_id: `rfmx-demod`
- source_path: `samples-per-symbol.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod/raw/resource/enus/samples-per-symbol.html
- document_id: `rfmx-demod`
- page_type: `leaf`
- content_type: `concept`
- source_description: Samples Per Symbol determine the acquisition bandwidth. The bandwidth occupied by the transmitted signal is based on these variables: Modulation type Symbol rate Pulse-shaping filter used To successfully perform demodulation, the analyzer must acquire the complete bandwidth. The analyzer uses the fo

### Samples Per Symbol

Samples Per Symbol determine the acquisition
 bandwidth.

- Modulation type
- Symbol rate
- Pulse-shaping filter used

Acquisition Bandwidth = 0.8 * Acquisition Sample
 Rate

Acquisition Sample Rate = Min(Samples Per Symbol * Symbol Rate, Max
 Device I/Q Rate)

If you do not specify Samples Per
 Symbol or set it to Auto
 (-1), the analyzer uses the values in
 the following table.

| Modulation Type | Samples per Symbol = Auto (-1) | Pulse Shaping Filter |
| --- | --- | --- |
| ASK, PSK, QAM , APSK | 4 | Raised Cosine, Root-Raised Cosine |
| ASK, PSK, QAM , APSK | 8 | Rectangular |
| Offset QPSK | 8 | Raised Cosine, Root-Raised Cosine, Rectangular |
| FSK, MSK | 8 | Gaussian, Raised Cosine, Root-Raised Cosine, Rectangular |
| PSK | 4 | Linearized GMSK-EDGE |
| PSK | 16 | Half Sine |
| PSK | 16 | SOQPSK-TG |

Parent topic:

Digital Demodulation

<!--NI_TOPIC bundle=rfmx-demod path=supported-hw.html language=enus -->
## TOPIC 00028: Supported Hardware

- bundle_id: `rfmx-demod`
- source_path: `supported-hw.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod/raw/resource/enus/supported-hw.html
- document_id: `rfmx-demod`
- page_type: `leaf`
- content_type: `concept`
- source_description: RFmx supports a number of NI devices. 1 RFmx Demod Supported Hardware RFmx Demod Hardware Earliest Driver Version Support (Windows 11) PXIe-5644 2022 Q3 PXIe-5645 2022 Q3 PXIe-5646 2022 Q3 PXIe-5663 2022 Q3 PXIe-5665 2022 Q3 PXIe-5668 2022 Q3 PXIe-5820 2022 Q3 PXIe-5830 2022 Q3 PXIe-5831 2022 Q3 PXI

### Supported Hardware

RFmx supports a number of NI devices.

| RFmx Demod Hardware | Earliest Driver Version Support (Windows 11) |
| --- | --- |
| PXIe-5644 | 2022 Q3 |
| PXIe-5645 | 2022 Q3 |
| PXIe-5646 | 2022 Q3 |
| PXIe-5663 | 2022 Q3 |
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

NI-RFSA Properties

NI-RFSA LabVIEW VI
 Reference

For more information about your hardware and functionality, refer
 to the *NI-RFSA User Manual*.

Related information:

- NI-RFSA Properties
- NI-RFSA User Manual

<!--NI_TOPIC bundle=rfmx-demod path=symbols.html language=enus -->
## TOPIC 00029: Symbols

- bundle_id: `rfmx-demod`
- source_path: `symbols.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod/raw/resource/enus/symbols.html
- document_id: `rfmx-demod`
- page_type: `leaf`
- content_type: `concept`
- source_description: A symbol is constituted from a group of bits that are mapped onto a defined set of values known as a symbol map on the transmitter. The rate at which the symbols are transmitted per second is called the symbol rate. For the analyzer to demodulate the signal correctly, the transmitted symbol rate mus

### Symbols

A symbol is constituted from a group of bits that are mapped onto a defined set of values
 known as a symbol map on the transmitter. The rate at which the symbols are transmitted
 per second is called the symbol rate. For the analyzer to demodulate the signal
 correctly, the transmitted symbol rate must be specified.

When demodulating the signal, impairments are corrected, and the recovered symbols are
 then compared against all points on the symbol map to find the closest ideal symbol. In
 RFmx, the bit representation in the symbol map is read as
 b<sub>(log<sub>2</sub>M)-1</sub> ... b<sub>0</sub>, with the least significant bit
 on the right.

For example, the default symbol map for QPSK (Modulation Type = PSK, M = 4) is as shown
 in the following image.

[IMAGE alt='image' src='GUID-7A51618D-175F-4607-AE17-39080169186C-a5.gif']

The demodulated bits are as follows.

[IMAGE alt='image' src='GUID-82EF3619-3B3A-4419-A018-F13DE8372F31-a5.gif']

The demodulated bits are reported as an array of bits in the following order.

{b<sub>0</sub> ... b<sub>(log<sub>2</sub>M)-1</sub>}<sub>0</sub> {b<sub>0</sub> ...
 b<sub>(log<sub>2</sub>M)-1</sub>}<sub>1</sub> ... {b<sub>0</sub> ...
 b<sub>(log<sub>2</sub>M)-1</sub>}<sub>n-1</sub>

where M is the M-ary and n is the number of symbols
 analyzed.

To provide a custom symbol map, set the Symbol Map Type to Custom and provide an array of
 symbols. The index of the array determines the grouped bits that are to be mapped onto
 the symbol.

Note

Modulation Types

Parent topic:

Digital Demodulation

<!--NI_TOPIC bundle=rfmx-demod path=system-requirements.html language=enus -->
## TOPIC 00030: RFmx Demod System Requirements

- bundle_id: `rfmx-demod`
- source_path: `system-requirements.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod/raw/resource/enus/system-requirements.html
- document_id: `rfmx-demod`
- page_type: `leaf`
- content_type: `concept`
- source_description: RFmx Demod has the following requirements: Processor—1 GHz 64-bit (x64) processor 4 GB RAM * A screen resolution of 1,024 x 768 Any supported OS, with all available critical updates and service packs * Depending on the amount of data acquired and/or processed, a larger amount of memory may be requir

### RFmx Demod System Requirements

RFmx Demod has the following requirements:

- Processor—1 GHz 64-bit (x64) processor
- 4 GB RAM *
- A screen resolution of 1,024 x 768
- Any supported OS, with all available critical updates and service packs

* Depending on the amount of data acquired and/or processed, a larger amount of memory
 may be required.

<!--NI_TOPIC bundle=rfmx-demod path=user-manual-welcome.html language=enus -->
## TOPIC 00031: RFmx Demod User Manual

- bundle_id: `rfmx-demod`
- source_path: `user-manual-welcome.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod/raw/resource/enus/user-manual-welcome.html
- document_id: `rfmx-demod`
- page_type: `leaf`
- content_type: `concept`
- source_description: The RFmx Demod User Manual provides detailed descriptions of the product functionality and the step by step processes for use. Looking for Something Else?For information not found in the User Manual for your product, such as specifications and API reference, browse Related Information.

### RFmx Demod
 User Manual

The RFmx Demod User Manual provides detailed
 descriptions of the product functionality and the step by step processes for use.

#### Looking for Something Else?

For information not found in the User Manual
 for your product, such as specifications and API reference, browse *Related
 Information*.

Related information:

- Download RFmx Digital Modulation
- Download RFmx Analog Modulation
- License Setup and Activation
- RFmx Analog Modulation Release Notes
- RFmx Digital Modulation Release Notes
- Getting Started with RFmx
- RFmx Demod LabVIEW Reference
- RFmx Demod .NET Reference
- RFmx Demod C Reference
- RFmx Instr LabVIEW Reference
- RFmx Instr .NET Reference
- RFmx Instr C Reference
