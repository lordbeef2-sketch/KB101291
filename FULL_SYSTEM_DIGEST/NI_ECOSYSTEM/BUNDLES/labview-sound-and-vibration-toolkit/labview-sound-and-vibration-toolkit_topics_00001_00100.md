# NI DOCUMENT BUNDLE: labview-sound-and-vibration-toolkit

<!--NI_BUNDLE_CHUNK bundle=labview-sound-and-vibration-toolkit start=1 end=100 -->
<!--NI_TOPIC bundle=labview-sound-and-vibration-toolkit path=a-b-and-c-weighting-filters.html language=enus -->
## TOPIC 00001: A- and C-Weighting Filters

- bundle_id: `labview-sound-and-vibration-toolkit`
- source_path: `a-b-and-c-weighting-filters.html`
- source_url: https://docs-be.ni.com/bundle/labview-sound-and-vibration-toolkit/raw/resource/enus/a-b-and-c-weighting-filters.html
- document_id: `labview-sound-and-vibration-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: An A-weighting filter is a highpass filter designed to simulate the loudness of low-level tones. An A-weighting filter progressively de-emphasizes frequencies below 500 Hz. A C-weighting filter removes sounds outside the audio range of 20 Hz to 20 kHz and simulates the loudness of high-level tones.

A- and C-Weighting Filters

An A-weighting filter is a highpass filter designed to simulate the loudness of
 low-level tones. An A-weighting filter progressively de-emphasizes frequencies below 500 Hz. A
 C-weighting filter removes sounds outside the audio range of 20 Hz to 20 kHz and simulates the
 loudness of high-level tones.

The ANSI S1.4 standard defines the frequency responses of the A- and C-weighting filters.
 The following figure shows the relative attenuation defined for A- and C-weighting
 filters.

Figure 22.

[IMAGE alt='1378' src='GUID-78A23741-0C48-49E6-AEB1-DC58D61E93D9-a5.gif']

Note

Parent topic:

Acoustic Weighting Filters

<!--NI_TOPIC bundle=labview-sound-and-vibration-toolkit path=ac-coupling.html language=enus -->
## TOPIC 00002: AC Coupling

- bundle_id: `labview-sound-and-vibration-toolkit`
- source_path: `ac-coupling.html`
- source_url: https://docs-be.ni.com/bundle/labview-sound-and-vibration-toolkit/raw/resource/enus/ac-coupling.html
- document_id: `labview-sound-and-vibration-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: AC coupling is the connection of a signal from one circuit to another in a manner that rejects DC components.The signal acquired from the sensor consists of both DC and AC components, where the DC portion offsets the AC portion from zero. In an analog system, simple AC coupling removes the DC offset

AC Coupling

AC coupling is the connection of a signal from one circuit to another in a manner
 that rejects DC components.

The signal acquired from the sensor consists of both DC and AC components, where the DC portion
 offsets the AC portion from zero. In an analog system, simple AC
 coupling removes the DC offset in the system by means of a
 capacitor in series with the signal. An AC-coupled sensor system
 attenuates voltage offset due to constant current
 excitation.

AC coupling also attenuates the long-term DC drift that sensors have due to age and temperature
 effect. When implemented in hardware, AC coupling can prevent
 the saturation of an input channel and can enable the use of a
 more narrow input range to improve AC amplitude resolution and
 usable dynamic range of the channel. When implemented in
 software, AC coupling can remove erroneous DC data that would
 otherwise invalidate signal processing such as integration and
 measurement results such as RMS and Peak levels.

Parent topic:

Waveform Conditioning

<!--NI_TOPIC bundle=labview-sound-and-vibration-toolkit path=accelerometers.html language=enus -->
## TOPIC 00003: Accelerometers

- bundle_id: `labview-sound-and-vibration-toolkit`
- source_path: `accelerometers.html`
- source_url: https://docs-be.ni.com/bundle/labview-sound-and-vibration-toolkit/raw/resource/enus/accelerometers.html
- document_id: `labview-sound-and-vibration-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Accelerometers, sensors that represent acceleration as voltage, come in two axial types: single axis and tri-axial. Choosing between the two depends on the type of vibration you are measuring. The most common accelerometer measures acceleration along only a single axis. You often use this type of ac

Accelerometers

Accelerometers, sensors that represent acceleration as voltage, come in two axial
 types: single axis and tri-axial. Choosing between the two depends on the type of vibration you
 are measuring.

The most common accelerometer measures acceleration along only a single axis. You often use
 this type of accelerometer to measure mechanical vibration levels. The second type is a
 tri-axial accelerometer. This accelerometer can create a 3D vector of acceleration in the form
 of orthogonal components. Use this type when you need to determine the type of
 vibration—lateral, transverse, rotational, and so on—that a component is undergoing or the
 direction of acceleration of the component.

Both types of accelerometers come with either both leads insulated, or isolated, from the
 case or with one lead grounded to the case. Some accelerometers rely on the piezoelectric
 effect to generate voltage. To measure acceleration with this type of sensor, the sensor must
 be connected to a charge-sensitive amplifier. Other accelerometers have a charge-sensitive
 amplifier built inside them.

Accelerometers are the most widely used vibration transducers for measuring vibrations on
 stationary machine elements. The benefits of an accelerometer include linearity over a wide
 frequency range and a large dynamic range. You can use most accelerometers in hazardous
 environments because of their rugged and reliable construction.

When choosing an accelerometer, pay attention to the most critical parameters. If the sensor
 must operate in extreme temperatures, you are limited to a sensor that relies on the
 piezoelectric effect to generate voltage. If the environment is very noisy, a sensor with a
 charge-sensitive amplifier built in might be the only usable choice.

You can use accelerometers in applications involving frequencies from a few hertz to tens of
 kilohertz. The following illustration shows the typical frequency response characteristics of
 an accelerometer.

Figure 2.

[IMAGE alt='1378' src='GUID-837AAECE-9F1E-41FE-9156-A17F6CF447C2-a5.gif']

Because most accelerometers have a low dynamic signal response below 10 Hz, you cannot use
 accelerometers for low frequency measurements. The usable frequency range of an accelerometer
 is typically 15 Hz to 10 Hz or above.

Parent topic:

Vibration

<!--NI_TOPIC bundle=labview-sound-and-vibration-toolkit path=acoustic-weighting-filters.html language=enus -->
## TOPIC 00004: Acoustic Weighting Filters

- bundle_id: `labview-sound-and-vibration-toolkit`
- source_path: `acoustic-weighting-filters.html`
- source_url: https://docs-be.ni.com/bundle/labview-sound-and-vibration-toolkit/raw/resource/enus/acoustic-weighting-filters.html
- document_id: `labview-sound-and-vibration-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Applications involving acoustic measurements use instrumentation devices that provide a linear response, but rely on the human ear as the final, nonlinear sensor. Accounting for these nonlinear limitations with psophometric weighting filters is crucial. The following figure shows the linear frequenc

Acoustic Weighting Filters

Applications involving acoustic measurements use instrumentation devices that provide a
 linear response, but rely on the human ear as the final, nonlinear sensor. Accounting for these
 nonlinear limitations with psophometric weighting filters is crucial.

The following figure shows the linear frequency response of a microphone.

Figure 21.

[IMAGE alt='1378' src='GUID-16FC6D8A-8516-41C4-B5A4-F12D2B6A920E-a5.gif']

The frequency response of the microphone is designed to be as flat as possible in the
 frequency range of 10 Hz to 10 kHz.

The NI Sound and Vibration Measurement Suite provides the following psophometric weighting
 filters for you to apply acoustic weighting.

- [A- and C-Weighting Filters](a-b-and-c-weighting-filters.html) An A-weighting filter is a highpass filter designed to simulate the loudness of low-level tones. An A-weighting filter progressively de-emphasizes frequencies below 500 Hz. A C-weighting filter removes sounds outside the audio range of 20 Hz to 20 kHz and simulates the loudness of high-level tones.
- [Radiocommunications Weighting Filters](radiocommunications-weighting-filters.html) ITU-R 468-4 and Dolby weighting filters are bandpass filters you use to emphasize the response to the types of impulsive noise that often couple into audio cables. Typically, you use these filters to measure audio frequency noise in broadcasting, sound-recording systems, and sound program circuits.
- [Telecommunications Weighting Filters](telecommunications-weighting-filters.html) CCITT and C-message weighting filters are bandpass filters used to measure audio-frequency noise on telephone circuits. The CCITT (ITU-T) filter is used for international telephone circuits. The C-message filter is typically used for North American telephone circuits.
- [Acoustic Weighting Standards](acoustic-weighting-standards.html) Acoustic weighting filters in the NI Sound and Vibration Measurement Suite comply with different acoustic weighting standards depending on the type of filter.

Parent topic:

Weighting Filters

<!--NI_TOPIC bundle=labview-sound-and-vibration-toolkit path=acoustic-weighting-standards.html language=enus -->
## TOPIC 00005: Acoustic Weighting Standards

- bundle_id: `labview-sound-and-vibration-toolkit`
- source_path: `acoustic-weighting-standards.html`
- source_url: https://docs-be.ni.com/bundle/labview-sound-and-vibration-toolkit/raw/resource/enus/acoustic-weighting-standards.html
- document_id: `labview-sound-and-vibration-toolkit`
- page_type: `leaf`
- content_type: `reference`
- source_description: Acoustic weighting filters in the NI Sound and Vibration Measurement Suite comply with different acoustic weighting standards depending on the type of filter. Acoustic Weighting Filter Standards A- and C- Weighting Filters Radiocommunications Weighting Filters Telecommunications Weighting Filters AN

Acoustic Weighting Standards

Acoustic weighting filters in the NI Sound and Vibration Measurement Suite comply
 with different acoustic weighting standards depending on the type of filter.

| A- and C- Weighting Filters | Radiocommunications Weighting Filters | Telecommunications Weighting Filters |
| --- | --- | --- |
| ANSI S1.4-1983 ANSI S1.42-2001 IEC 61672-1:2002 JIS C 1509-1:2005 | ITU-R 468-4 JIS C 6102:1998 Dolby | ITU-T O.41 Bell System Technical Reference 41009 |

Parent topic:

Acoustic Weighting Filters

<!--NI_TOPIC bundle=labview-sound-and-vibration-toolkit path=acquiring-and-simulating-dynamic-signals.html language=enus -->
## TOPIC 00006: Methods for Acquiring and Simulating Dynamic Signals

- bundle_id: `labview-sound-and-vibration-toolkit`
- source_path: `acquiring-and-simulating-dynamic-signals.html`
- source_url: https://docs-be.ni.com/bundle/labview-sound-and-vibration-toolkit/raw/resource/enus/acquiring-and-simulating-dynamic-signals.html
- document_id: `labview-sound-and-vibration-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Dynamic signals can be acquired using a DAQ device system or they can be simulated using generation VIs. This section describes methods for obtaining data and some key issues when acquiring or simulating dynamic signals to ensure valid measurement results.You can use the following two methods to obt

Methods for Acquiring and Simulating Dynamic
 Signals

Dynamic signals can be acquired using a DAQ device system or they can be
 simulated using generation VIs.

This section describes methods for obtaining data and some key issues
 when acquiring or simulating dynamic signals to ensure valid
 measurement results.

You can use the following two methods to obtain data:

- Acquire data with a data acquisition (DAQ) device system
- Simulate data with a generation VI or other source

The measurement and analysis tools in the NI Sound and Vibration Measurement Suite do not
 compensate for inaccurate data. You must calibrate the test
 equipment to ensure accurate results. Generally, the test
 equipment must have specifications at least 10 times better than
 the specifications of the device under test. Use a verifiable
 and repeatable test procedure to get accurate results.

Whether you are obtaining data from a DAQ system or simulating data, the following are common
 considerations in measurement analysis:

- [Anti-Aliasing](anti-aliasing.html) Anti-aliasing protects frequency measurements from distortion ensuring accurate data representation.
- [Sampling Rate](sampling-rate.html) The scan rate, or the sampling rate in NI-DAQmx, determines how often an analog-to-digital (A/D) conversion takes place.
- [Block Size](block-size.html) When you use NI-DAQmx to control the data acquisition (DAQ) hardware, you must take the block size—in either number of samples or block duration—into consideration.
- [Synchronous Sampling](synchronous-sampling.html) Synchronous sampling is a key feature of the data acquisition system for acquiring dynamic signals. Traditionally, you implement synchronous sampling by using simultaneous sample-and-hold circuitry.
- [Time Continuity](time-continuity.html) When you acquire data in a continuous acquisition, you can use the timestamp parameter in the waveform data type to verify no gaps exist between successive blocks of waveforms returned by sequential calls to the DAQmx Read VI or AI Read VI.

Parent topic:

Dynamic Signals

<!--NI_TOPIC bundle=labview-sound-and-vibration-toolkit path=analog-tachometer-signals.html language=enus -->
## TOPIC 00007: Analog Tachometer Signals

- bundle_id: `labview-sound-and-vibration-toolkit`
- source_path: `analog-tachometer-signals.html`
- source_url: https://docs-be.ni.com/bundle/labview-sound-and-vibration-toolkit/raw/resource/enus/analog-tachometer-signals.html
- document_id: `labview-sound-and-vibration-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Analog tachometer signals are obtained through the analog input channel of a data acquisition (DAQ) device.By synchronizing the tachometer and sound or vibration acquisition channels, you can acquire the analog tachometer signal with the same DAQ device that you use to acquire sound or vibration sig

Analog Tachometer Signals

Analog tachometer signals are obtained through the analog input channel of a
 data acquisition (DAQ) device.

By synchronizing the tachometer and sound or vibration acquisition channels, you can acquire the
 analog tachometer signal with the same DAQ device that you use
 to acquire sound or vibration signals. Some DAQ devices might
 have difficulty acquiring very high rotational speed signals
 from tachometers or from encoders that generate hundreds of
 pulses per revolution. Even if you choose a DAQ device that can
 sustain high enough sampling rates to provide sufficient
 resolution for the tachometer signal, sampling the sound or
 vibration signals at the same high rate is not efficient because
 of the demands that synchronization places on the measurement
 and computational effort. In this case, you cannot acquire the
 tachometer signal with an analog measurement channel. Instead,
 you can avoid unnecessary computation and system resource
 expenditure by running the acquisition of the sound or vibration
 signals at a lower frequency and by using a counter device to
 acquire a digital tachometer signal.

Parent topic:

Rotational Speed

Related concepts:

- Sampling Rate
- Digital Tachometer Signals

<!--NI_TOPIC bundle=labview-sound-and-vibration-toolkit path=anti-aliasing.html language=enus -->
## TOPIC 00008: Anti-Aliasing

- bundle_id: `labview-sound-and-vibration-toolkit`
- source_path: `anti-aliasing.html`
- source_url: https://docs-be.ni.com/bundle/labview-sound-and-vibration-toolkit/raw/resource/enus/anti-aliasing.html
- document_id: `labview-sound-and-vibration-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Anti-aliasing protects frequency measurements from distortion ensuring accurate data representation. Aliasing is the phenomenon that frequencies greater than the Nyquist frequency are shifted erroneously to lower frequencies. The Nyquist frequency is calculated with the following equation: f [Nyquis

Anti-Aliasing

Anti-aliasing protects frequency measurements from distortion ensuring accurate data
 representation.

Aliasing is the phenomenon that frequencies greater than the Nyquist frequency are shifted
 erroneously to lower frequencies.

The Nyquist frequency is calculated with the following equation:

f
 <sub>Nyquist</sub> = sampling rate / 2

When you acquire data with an NI dynamic signal acquisition (DSA) device, aliasing protection
 is automatic in any acquisition. The sharp anti-aliasing filters on DSA devices track the
 sampling rate and filter out or attenuate all frequencies above the Nyquist frequency.

When performing frequency measurements with an NI E Series, M Series, or X Series DAQ device,
 you must manually eliminate aliasing using the following methods:

- Increasing the sampling rate
- Applying an external lowpass filter
- Using an inherently bandlimited DUT

Simulated data also can contain aliasing. Simulated signals usually are generated according
 to a time-domain expression. Therefore, simulated signals usually have high-frequency
 components that are aliased in the discretely sampled data. The following figure shows an
 example of the aliasing for a simulated square wave.

Figure 7.

[IMAGE alt='1378' src='GUID-349CF478-A877-4AA9-96E7-90116B63B417-a5.gif']

The only way to protect data from aliasing is to apply appropriate aliasing protection before
 the data is generated or acquired. Aliasing occurs when the data is generated or sampled. You
 cannot remove aliased components from the data without detailed knowledge of the original
 signal. In general, you cannot distinguish between true frequency components and aliased
 frequency components. Therefore, accurate frequency measurements require adequate aliasing
 protection.

Parent topic:

Methods for Acquiring and Simulating Dynamic Signals

<!--NI_TOPIC bundle=labview-sound-and-vibration-toolkit path=applications-of-limit-testing.html language=enus -->
## TOPIC 00009: Applications of Limit Testing

- bundle_id: `labview-sound-and-vibration-toolkit`
- source_path: `applications-of-limit-testing.html`
- source_url: https://docs-be.ni.com/bundle/labview-sound-and-vibration-toolkit/raw/resource/enus/applications-of-limit-testing.html
- document_id: `labview-sound-and-vibration-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use limit testing in a wide range of test and measurement applications. including modem manufacturing, digital filter design, and pulse mask testing.Standards-generating bodies, such as the CCITT, ITU-T, ANSI, and IEC, provide limit testing specifications to ensure that all the test and meas

Applications of Limit Testing

You can use limit testing in a wide range of test and measurement applications.
 including modem manufacturing, digital filter design, and pulse mask testing.

Standards-generating bodies, such as the CCITT, ITU-T, ANSI, and IEC, provide limit testing
 specifications to ensure that all the test and measurement
 systems conform to a universally accepted standard. In some
 other cases, the limit testing specifications are proprietary
 and are strictly enforced by companies for quality control.

- [Limit Testing in Modem Manufacturing](limit-testing-in-modem-manufacturing.html) Limit testing is used in modem manufacturing to make sure the transmit spectrum of the line signal meets the V.34 modem specification.
- [Limit Testing in Digital Filter Design](limit-testing-in-digital-filter-design.html) You can use limit testing in the area of digital filter design.
- [Limit Testing in Pulse Mask Testing](limit-testing-in-pulse-mask-testing.html) T1 signals must lie in the mask specified by the upper and lower limit. These limits are set to properly enable the interconnection of digital network components to form a digital path or connection.

Parent topic:

Limit Testing

<!--NI_TOPIC bundle=labview-sound-and-vibration-toolkit path=averaged-order-spectra.html language=enus -->
## TOPIC 00010: Averaged Order Spectra

- bundle_id: `labview-sound-and-vibration-toolkit`
- source_path: `averaged-order-spectra.html`
- source_url: https://docs-be.ni.com/bundle/labview-sound-and-vibration-toolkit/raw/resource/enus/averaged-order-spectra.html
- document_id: `labview-sound-and-vibration-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: An averaged spectrum displays steady-state vibration components while reducing noise. An order spectrum provides a view of all order components of a signal and can help you find significant orders and compare the level of different order components.Refer to the following sections for more informatio

Averaged Order Spectra

An averaged spectrum displays steady-state vibration components while reducing noise.
 An order spectrum provides a view of all order components of a signal and can help you find
 significant orders and compare the level of different order components.

Refer to the following sections for more information.

- [Order Power Spectrum](order-power-spectrum.html) An order power spectrum provides a quantitative description of the amplitude or power of the orders in a signal.
- [Full Spectrum](full-spectrum.html) Full spectrum is the spectrum of an orbit. The amplitude of the full spectrum indicates the vibration level at each frequency/order.
- [Spectrum Averaging](spectrum-averaging.html) Averaging successive measurements can improve measurement accuracy.

Parent topic:

Order-Domain Analysis Functions

<!--NI_TOPIC bundle=labview-sound-and-vibration-toolkit path=bandwidth.html language=enus -->
## TOPIC 00011: Bandwidth

- bundle_id: `labview-sound-and-vibration-toolkit`
- source_path: `bandwidth.html`
- source_url: https://docs-be.ni.com/bundle/labview-sound-and-vibration-toolkit/raw/resource/enus/bandwidth.html
- document_id: `labview-sound-and-vibration-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The bandwidth of a filter denotes the range of frequencies the filter allows to pass through. Calculating the bandedge frequencies informs you of the bandwidth's characteristics. The quality constant Q is defined as the ratio of the bandwidth over the center frequency of the filter. Q remains consta

Bandwidth

The bandwidth of a filter denotes the range of frequencies the filter allows to pass
 through. Calculating the bandedge frequencies informs you of the bandwidth's
 characteristics.

The quality constant Q is defined as the ratio of the bandwidth over the
 center frequency of the filter. Q remains constant across all
 octave bands for octave filters. For example, an octave filter
 with a center frequency of 1,000 Hz leads to the following
 bandedge frequencies:

f

1

=

1

,

000

2

=

707

⁢

H

z

f

2

=

(

1

,

000

)

(

2

)

=

1

,

414

⁢

H

z

B

W

=

f

2

−

f

1

=

707

⁢

H

z

Q

=

707

1

,

000

=

0.707

where

f
 <sub>1</sub> and f<sub>2</sub> are bandedge
 frequencies

Q is the quality constant

BW is the bandwidth

An octave filter with a center frequency of 8,000 Hz leads to the
 following bandedge frequencies:

f

1

=

8

,

000

2

=

5

,

657

⁢

H

z

f

2

=

(

8

,

000

)

(

2

)

=

11

,

314

⁢

H

z

B

W

=

f

2

−

f

1

=

5

,

657

⁢

H

z

Q

=

5

,

657

8

,

000

=

0.707

where

f
 <sub>1</sub> and f<sub>2</sub> are bandedge
 frequencies

BW is the bandwidth

Q is the quality constant

The results obtained from calculating the bandedge frequencies indicate
 the following bandwidth characteristics:

- The bandwidth of the octave filters is narrow when the
 center frequency is low.
- The bandwidth of the octave filters is wider when the center
 frequency is higher.

Because of the bandwidth characteristics, fractional-octave analysis uses
 a logarithmic frequency scale to compute and display octave
 spectra.

Parent topic:

Fractional-Octave Filtering

<!--NI_TOPIC bundle=labview-sound-and-vibration-toolkit path=baseband-analysis.html language=enus -->
## TOPIC 00012: Baseband Analysis

- bundle_id: `labview-sound-and-vibration-toolkit`
- source_path: `baseband-analysis.html`
- source_url: https://docs-be.ni.com/bundle/labview-sound-and-vibration-toolkit/raw/resource/enus/baseband-analysis.html
- document_id: `labview-sound-and-vibration-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Baseband analysis involves applying the FFT to each component of a time-domain signal from the minimum resolvable frequency, 0, to the maximum resolvable frequency. The sampled time waveform input to an FFT determines the computed spectrum. If an arbitrary signal is sampled at a rate equal to f [s]o

Baseband Analysis

Baseband analysis involves applying the FFT to each component of a time-domain signal
 from the minimum resolvable frequency, 0, to the maximum resolvable frequency.

The sampled time waveform input to an FFT determines the computed spectrum. If an arbitrary
 signal is sampled at a rate equal to f
 <sub>s</sub>over an acquisition time T, N samples are
 acquired. Compute T with the following equation:

T

=

N

f

s

where

T is the acquisition time

N is the number of samples acquired

f
 <sub>s</sub> is the sampling frequency

Compute N with the following equation:

N

=

T

⋅

f

s

For FFT, the spectrum computed from the sampled signal has a frequency resolution df.
 Calculate the frequency resolution with the following equation:

d

f

=

1

T

=

f

s

N

Note

The resolution bandwidth (RBW) is an additional property that describes the minimum frequency
 spacing required to distinguish between two closely spaced frequency components. The following
 equation defines RBW:

R

B

W

=

d

f

⋅

E

N

B

W

where ENBW is the equivalent noise bandwidth.

You often apply a window to the time-domain signal prior to the FFT. A key parameter of the
 window is the ENBW.

The sampling rate of a time waveform determines the maximum resolvable frequency. According
 to the Shannon Sampling Theorem, the maximum resolvable frequency must be half the sampling
 frequency. To calculate the maximum resolvable frequency, use the following equation:

f

max

⁡

=

f

N

y

q

u

i

s

t

=

f

s

2

where

f
 <sub>max</sub> is the maximum resolvable frequency

f
 <sub>Nyquist</sub> is the Nyquist frequency

f
 <sub>s</sub> is the sampling frequency

The minimum resolvable frequency is 0 (DC). The analysis from 0 to
 f<sub>Nyquist</sub> is the baseband analysis.

- [Relationship between Time-Domain and Frequency-Domain Specifications and Parameters](relationship-between-time-domain-and-frequenc.html) This section summarizes the relationship of time-domain specifications to frequency-domain parameters.
- [Frequency Resolution](frequency-resolution.html) The frequency resolution in a Fast Fourier Transform (FFT) must be fine enough to identify distinct tonal components of the signal independently of the DC value and the noise.

Parent topic:

FFT, DFT, and Zoom

<!--NI_TOPIC bundle=labview-sound-and-vibration-toolkit path=block-by-block-averaging.html language=enus -->
## TOPIC 00013: Block-by-Block Averaging

- bundle_id: `labview-sound-and-vibration-toolkit`
- source_path: `block-by-block-averaging.html`
- source_url: https://docs-be.ni.com/bundle/labview-sound-and-vibration-toolkit/raw/resource/enus/block-by-block-averaging.html
- document_id: `labview-sound-and-vibration-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Some applications require you to perform level measurements continuously using a specific integration time. Typically, this specific integration time is the block duration time, whose result is cumulative only from the beginning of each block. In block-by-block averaging, you reset the process at th

Block-by-Block Averaging

Some applications require you to perform level measurements continuously using a
 specific integration time. Typically, this specific integration time is the block duration time,
 whose result is cumulative only from the beginning of each block.

In block-by-block averaging, you reset the process at the beginning of each time block, as
 shown in the following figure.

Figure 26.

[IMAGE alt='1378' src='GUID-E0B84431-B534-44CE-AE3A-7A8810C38FE4-a5.gif']

The total measurement time is t<sub>f</sub> and the measurement is
 returned as a history of levels versus time.

Parent topic:

Linear Averaging

Related concepts:

- Level Measurements

<!--NI_TOPIC bundle=labview-sound-and-vibration-toolkit path=block-size.html language=enus -->
## TOPIC 00014: Block Size

- bundle_id: `labview-sound-and-vibration-toolkit`
- source_path: `block-size.html`
- source_url: https://docs-be.ni.com/bundle/labview-sound-and-vibration-toolkit/raw/resource/enus/block-size.html
- document_id: `labview-sound-and-vibration-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: When you use NI-DAQmx to control the data acquisition (DAQ) hardware, you must take the block size—in either number of samples or block duration—into consideration. You can measure the block size either in terms of samples or time as long as the sampling rate is constant.The following equation calcu

Block Size

When you use NI-DAQmx to control the data acquisition (DAQ) hardware, you must take
 the block size—in either number of samples or block duration—into consideration.

You can measure the block size either in terms of samples or time as long as the sampling
 rate is constant.

The following equation calculates the acquisition duration:

T = N * dt

where

T is the acquisition duration

N is the block size

dt is the sample interval

The acquisition duration determines the maximum length of an event that you can measure in a
 finite acquisition or the time resolution that you can achieve
 in a continuous acquisition. In a continuous acquisition the
 duration of each measurement block impacts the rate at which the
 data acquisition loop must run, the time/frequency resolution of
 all block-based measurements, and the latency of your DAQ
 application. The sound and vibration analysis tools in the NI
 Sound and Vibration Measurement Suite generally check for either
 time continuity or block size. For example, time-domain
 weighting filters, resampling, level measurements, octave
 analysis, zoom FFT analysis, and order analysis require
 continuous blocks of data even though the blocks do not have to
 be of equal size. Limit testing, baseband FFT analysis, and
 subset FFT analysis requires a constant block size but place no
 restrictions on the timestamp of each block of data.

Parent topic:

Methods for Acquiring and Simulating Dynamic Signals

Related concepts:

- Methods for Acquiring and Simulating Dynamic Signals
- Sampling Rate
- Time Continuity
- Weighting Filters
- Resampling
- Level Measurements
- Fractional-Octave Analysis
- Zoom FFT Analysis
- Baseband Analysis
- Subset Analysis

Related reference:

- Supported Data Types for Limit Testing

<!--NI_TOPIC bundle=labview-sound-and-vibration-toolkit path=broadband.html language=enus -->
## TOPIC 00015: Broadband

- bundle_id: `labview-sound-and-vibration-toolkit`
- source_path: `broadband.html`
- source_url: https://docs-be.ni.com/bundle/labview-sound-and-vibration-toolkit/raw/resource/enus/broadband.html
- document_id: `labview-sound-and-vibration-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: A broadband measurement uses a broadband signal with a flat frequency power spectrum. Broadband signals ensure that all the frequencies of interest are excited during acquisition. Typical broadband signals include white noise, pink noise, impulses, and chirp signals. The following figure shows the s

Broadband

A broadband measurement uses a broadband signal with a flat frequency power spectrum.
 Broadband signals ensure that all the frequencies of interest are excited during
 acquisition.

Typical broadband signals include white noise, pink noise, impulses, and chirp
 signals.

The following figure shows the simulated frequency response function for a
 four-degree-of-freedom system.

Figure 72.

[IMAGE alt='1378' src='GUID-B4F4C494-4E17-4C76-B29D-63F1E872C59E-a5.png']

The peak at 17.6 Hz has a magnitude roughly 1,000 times larger than the peak at 5.8 Hz.
 To use the broadband measurement, use broadband excitation to excite the entire
 frequency range of interest to measure the frequency response. This situation forces you
 to set the input range so that the overall response does not overload the DUT or the
 acquisition device. Therefore, when you measure the response at 5.8 Hz, you lose 60 dB
 of the measurement dynamic range. The swept-sine measurement enables you to tailor the
 excitation amplitude to the specific test frequency, preserving the full measurement
 dynamic range.

The broadband measurement is limited to a linearly-spaced frequency resolution determined
 by the sampling rate and the block size. When the response changes rapidly, this
 frequency resolution may not yield enough information about the dynamic response. Also,
 a linear resolution might yield an excessive amount of information in frequency regions
 where the dynamic response is relatively constant. The stepped swept-sine measurement
 has the ability to test arbitrary frequency resolutions that are linear, logarithmic, or
 adapted to the dynamic response of the DUT. When the frequency resolution is adapted to
 the DUT dynamic response, you can test more frequencies in regions where the dynamic
 response is of interest to the application and less where it is not.

The main benefit of a swept-sine measurement is the ability to measure harmonic
 distortion simultaneously with a linear response. A broadband measurement offers a speed
 advantage for broadband measurements with many test frequencies.

Parent topic:

Frequency Response and Stimulus Signal

<!--NI_TOPIC bundle=labview-sound-and-vibration-toolkit path=buffering.html language=enus -->
## TOPIC 00016: Buffering

- bundle_id: `labview-sound-and-vibration-toolkit`
- source_path: `buffering.html`
- source_url: https://docs-be.ni.com/bundle/labview-sound-and-vibration-toolkit/raw/resource/enus/buffering.html
- document_id: `labview-sound-and-vibration-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: When a group of channels share timestamp, sample rate, and channel length properties, a buffer can be used to accumulate and share data between different sections of code. You can use a buffer to decouple one source (producer) of dynamic signals from one or multiple readers (consumers). Log files, s

Buffering

When a group of channels share timestamp, sample rate, and channel length
 properties, a buffer can be used to accumulate and share data between different sections
 of code. You can use a buffer to decouple one source (producer) of dynamic signals from
 one or multiple readers (consumers).

Log files, snapshots, data acquisition, and waveform generation VIs can all be sources
 of dynamic data. Generally, this data can be one or more channels. When the data
 includes multiple channels, all channels should share the following properties
 characteristic of simultaneously sampled data:

1. Timestamp (t0)
2. Sample rate (Fs = 1/dt)
3. Channel length

Different buffer interfaces have different attributes; the waveform buffer and the
 queue share the following attributes: non-deterministic timing, flexible sizing, and
 flexible access options. Generally, a single writer is used to append new, continuous
 data to the data already in the buffer. Readers can read subsets of this buffered
 data as needed for processing in that section of code.

| Buffer Read | Processing |
| --- | --- |
| Read next measurement samples | Stimulus-response measurements |
| Read next continuous samples | Filtering Integration Statistical level Continuous level Fractional-octave analysis Zoom FFT Time-varying loudness Envelope Detection Tachometer processing Angular resampling Save to disk |
| Read next samples with overlap | Averaged FFT Tone measurements Averaged frequency response Short-time fourier transform (STFT) Block AC/DC level |
| Read specific samples at timestamp | Subset analysis of waveforms |
| Read last N samples | Instantaneous frequency Current speed Historical chart |
| Read all samples | Block processing when overwriting buffer |

In the table above, the read modes are listed from strictest to loosest timing
 requirements. A unique reader timestamp allows each reader to access the 'next' data
 without creating a unique copy of all data per waveform buffer reader.

Parent topic:

Dynamic Signals

<!--NI_TOPIC bundle=labview-sound-and-vibration-toolkit path=calculating-characteristic-frequencies-and-or.html language=enus -->
## TOPIC 00017: Calculate Characteristic Frequencies and Orders

- bundle_id: `labview-sound-and-vibration-toolkit`
- source_path: `calculating-characteristic-frequencies-and-or.html`
- source_url: https://docs-be.ni.com/bundle/labview-sound-and-vibration-toolkit/raw/resource/enus/calculating-characteristic-frequencies-and-or.html
- document_id: `labview-sound-and-vibration-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Faults on the inner race, outer race, or rolling elements of a rolling-element bearing exhibit peaks of characteristic frequencies or orders in the power spectrum of the envelope signal of the vibration signal. You can calculate the characteristic frequencies or orders of a rolling-element bearing a

Calculate Characteristic Frequencies and
 Orders

Faults on the inner race, outer race, or rolling elements of a rolling-element bearing
 exhibit peaks of characteristic frequencies or orders in the power spectrum of the envelope
 signal of the vibration signal. You can calculate the characteristic frequencies or orders of a
 rolling-element bearing and compare them with the peaks in the power spectrum of the envelope
 signal to identify the source of the bearing faults.

The following illustration shows the structure and the geometric parameters of a typical
 rolling-element bearing:

Figure 58.

[IMAGE alt='1378' src='GUID-71A2CE23-4A55-4301-B651-5DB1E0816649-a5.gif']

D<sub>ball</sub> is the bearing ball diameter,
 D<sub>pitch</sub> is the pitch diameter, and Φ is the
 contact angle between the ball and the race.

You can use the following equations to calculate the characteristic frequencies of the
 bearing:

| Characteristic Bearing Frequency | Equation |
| --- | --- |
| Fundamental train frequency, fFTF | f F T F = f s 2 [ 1 − D b a l l D p i t c h cos ϕ ] |
| Ball spin frequency, fBS | f B S = f s 2 D p i t c h D b a l l [ 1 − ( D b a l l D p i t c h ) 2 cos 2 ( ϕ ) ] |
| Outer race frequency, fOR | f O R = N f F T F |
| Inner race frequency, fIR | f I R = N ( f s − f F T F ) |

where f<sub>s</sub> is the rotational frequency of the shaft in
 revolutions per second, and N is the number of rollers or balls.

You can use the following equations to calculate the characteristic orders of the
 bearing:

| Characteristic Order | Equation |
| --- | --- |
| Fundamental train order, oFTF | o F T F = 1 2 [ 1 − D b a l l D p i t c h cos ⁡ ϕ ] |
| Ball spin order, oBS | o B S = 1 2 D b a l l D p i t c h [ 1 − ( D b a l l D p i t c h ) 2 cos 2 ϕ ] |
| Outer race order, oOR | o O R = N o F T F |
| Inner race order, oIR | O I R = N ( 1 − o F T F ) |

As shown in the table above, the characteristic orders are functions of the geometric
 parameters of the bearing and therefore are constant values.

The equations for calculating the characteristic frequencies and orders assume no slippage of
 the rollers or balls when the bearing is running. In real-world applications, however, the
 actual characteristic frequencies or orders might differ slightly from the calculated
 frequencies or orders because of slippage.

Parent topic:

Bearings

Related concepts:

- Envelope Detection

<!--NI_TOPIC bundle=labview-sound-and-vibration-toolkit path=calibration-and-scaling.html language=enus -->
## TOPIC 00018: Calibration and Scaling

- bundle_id: `labview-sound-and-vibration-toolkit`
- source_path: `calibration-and-scaling.html`
- source_url: https://docs-be.ni.com/bundle/labview-sound-and-vibration-toolkit/raw/resource/enus/calibration-and-scaling.html
- document_id: `labview-sound-and-vibration-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Accurate measurement and analysis are critical for producing meaningful results. By correctly calibrating the system's channels and references, and by translating raw signals into linear units or decibels, you can ensure the reliability and accuracy of your test data.

Calibration and Scaling

Accurate measurement and analysis are critical for producing meaningful results. By
 correctly calibrating the system's channels and references, and by translating raw signals
 into linear units or decibels, you can ensure the reliability and accuracy of your test
 data.

- [System Calibration](performing-system-calibration.html) The system calibration tools in the NI Sound and Vibration Measurement Suite provide default values commonly found for dedicated calibrators, such as pistonphones for microphones or hand-held shakers for accelerometers.
- [Scale Signals to Engineering Units](scaling-signals-to-engineering-units.html) You must scale a signal to the appropriate engineering units (EU) before you perform measurement analysis.

<!--NI_TOPIC bundle=labview-sound-and-vibration-toolkit path=channel-characterization.html language=enus -->
## TOPIC 00019: Channel Characterization

- bundle_id: `labview-sound-and-vibration-toolkit`
- source_path: `channel-characterization.html`
- source_url: https://docs-be.ni.com/bundle/labview-sound-and-vibration-toolkit/raw/resource/enus/channel-characterization.html
- document_id: `labview-sound-and-vibration-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI Sound and Vibration Measurement Suite offers the means for various measurements that assess the performance and behavior of the communication or signal pathway your channel performance is optimized, ensuring your channel performance is optimized. Refer to the following sections for more infor

Channel Characterization

The NI Sound and Vibration Measurement Suite offers the means for various
 measurements that assess the performance and behavior of the communication or signal pathway
 your channel performance is optimized, ensuring your channel performance is
 optimized.

Refer to the following sections for more information.

- [Idle-Channel Noise](idle-channel-noise.html) Idle-channel noise is noise present in a communications channel when no signals are applied.
- [Gain](gain.html) A gain measurement measures the amplification between the amplitude of the identified tone in the input signal and the reference amplitude.
- [Calculating Dual-Channel Gain and Phase](dual-channel-gain-and-phase.html) Gain and phase measure the amplification and the phase lag between the stimulus channel and the response channel at the test frequency. This lag time must be accounted for.
- [Dual-Channel Crosstalk](dual-channel-crosstalk.html) A crosstalk measurement analyzes the amplification and phase lag between the reference channel and the idle response channel at the test frequency.
- [Spurious Free Dynamic Range](spurious-free-dynamic-range.html) A spurious free dynamic range (SFDR) measurement quantifies the lowest level peaks identifiable as actual components of the signal instead of device under test artifacts.
- [Dynamic Range](dynamic-range.html) A dynamic range measurement quantifies the distortion and noise found in the device under test (DUT) output when a low-level signal is provided.
- [Group Delay](group-delay.html) Group delay is often used as a criterion to evaluate the phase nonlinearity of a filter.
- [Phase Linearity](phase-linearity.html) Phase linearity is one way to measure the amount of group delay distortion that a device under test (DUT) introduces.

Parent topic:

Detection, Distortion, and Channel Characterization

<!--NI_TOPIC bundle=labview-sound-and-vibration-toolkit path=comparing-fft-analysis-and-order-analysis.html language=enus -->
## TOPIC 00020: FFT Analysis Versus Order Analysis

- bundle_id: `labview-sound-and-vibration-toolkit`
- source_path: `comparing-fft-analysis-and-order-analysis.html`
- source_url: https://docs-be.ni.com/bundle/labview-sound-and-vibration-toolkit/raw/resource/enus/comparing-fft-analysis-and-order-analysis.html
- document_id: `labview-sound-and-vibration-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use an FFT power spectrum to identify and quantify the frequency components of a sound or vibration signal. However, changes in rotational speed can cause these frequency components to overlap, preventing you from identifying individual components. Order analysis solves this issue by monitor

FFT Analysis Versus Order Analysis

You can use an FFT power spectrum to identify and quantify the frequency components
 of a sound or vibration signal. However, changes in rotational speed can cause these
 frequency components to overlap, preventing you from identifying individual components.
 Order analysis solves this issue by monitoring the harmonics that result from these same
 rotational speed changes.

One of the most common methods for analyzing sound and vibration signals is Fast Fourier
 Transform (FFT) analysis. The following figure shows an FFT analysis on the vibration
 signal of a PC fan with seven blades and four coils. Order components are the
 solution

Figure 47.

[IMAGE alt='1378' src='GUID-6F1B09D9-995E-49B9-8BDA-11234BEC5116-a5.gif']

Notice that the overall vibration signal of the PC fan is the superposition of the
 vibration from the shaft, coils, and blades. The PC fan rotates at 3,300 RPM. The shaft
 rotates at the same rate as the rotational speed of the PC fan, whereas the rotational
 speeds of the coils and blades are four and seven times that of the PC fan,
 respectively. The vibration signal of the shaft has the same frequency as the rotational
 speed of the PC fan, which is 55 Hz. The coil and blade vibration signals are the fourth
 and seventh harmonics of the rotational speed of the PC fan, which are 220 Hz and 385
 Hz, respectively.

The following figure shows the FFT power spectrum of the PC fan.

Figure 48.

[IMAGE alt='1378' src='GUID-73081DA5-F6CC-4D0F-857A-9A084010E3B6-a5.gif']

The FFT power spectrum of the vibration signal shows peaks at the rotational speed and at
 the fourth and seventh harmonics of the rotational speed. You thus can use the FFT power
 spectrum for machinery diagnostic purposes by associating certain frequency components
 with specific mechanical parts.

Many mechanical characteristics of rotating or reciprocating machinery change with speed.
 You can observe some mechanical faults, such as resonance, only as the rotational speed
 approaches or passes the critical speed. For this reason, machine sound and vibration
 tests usually require a run-up or run-down test. However, when the rotational speed
 changes, the frequency bandwidth of each individual harmonic gets wider. As a result,
 some frequency components might overlap. The resulting FFT power spectrum can no longer
 help you identify characteristic vibration components because no obvious peaks appear in
 the spectrum. The following figure shows the FFT power spectrum of the PC fan when the
 rotational speed changes from 1,000 to 4,000 revolutions per minute (RPM).

Figure 49.

[IMAGE alt='1378' src='GUID-88B47938-88C3-47A6-9DA3-889B9DE82E48-a5.gif']

Notice that you cannot identify any obvious peaks associated with particular mechanical
 parts in the FFT power spectrum plot.

Order analysis techniques enable you to analyze sound and vibration signals when the
 rotational speed changes over time. An order is the normalization of the rotational
 speed. The first order is the rotational speed, and order n is
 n times the rotational speed. Order components thus are the
 harmonics of the rotational speed. In the case of the PC fan, the shaft vibration is the
 first order vibration. The coil and blade vibrations are the fourth and seventh order
 vibrations, respectively. With order analysis, you can uncover information about
 harmonics buried in the FFT power spectrum due to changing rotational speed.

The order power spectrum is one of the order analysis functions that the NI Sound and
 Vibration Measurement Suite provides. The following figure shows the order power
 spectrum of the same signal used to compute the FFT power spectrum plot above.

Figure 50.

[IMAGE alt='1378' src='GUID-73DDCFCC-6E56-4C89-B46F-C3434DC49714-a5.gif']

The Order power spectrum plot shows clearly-defined peaks associated with different
 mechanical parts. The peak at the first order corresponds to the shaft vibration. The
 peak at the fourth order corresponds to the vibration of the coils. The peak at the
 seventh order corresponds to the vibration of the blades.

In general, order analysis techniques relate sound and vibration signals to the
 rotational speed. Order analysis techniques also reduce these signals to characteristic
 components, associate the components with mechanical parts, and provide repeatable sound
 and vibration measurements. You can obtain information about individual mechanical parts
 as well as the entire machine with order analysis.

Parent topic:

Order-Domain Analysis

Related concepts:

- FFT, DFT, and Zoom
- Order Power Spectrum

<!--NI_TOPIC bundle=labview-sound-and-vibration-toolkit path=comparing-techniques-for-measuring-frequency.html language=enus -->
## TOPIC 00021: Techniques for Measuring Frequency Response

- bundle_id: `labview-sound-and-vibration-toolkit`
- source_path: `comparing-techniques-for-measuring-frequency.html`
- source_url: https://docs-be.ni.com/bundle/labview-sound-and-vibration-toolkit/raw/resource/enus/comparing-techniques-for-measuring-frequency.html
- document_id: `labview-sound-and-vibration-toolkit`
- page_type: `leaf`
- content_type: `reference`
- source_description: Frequency response can be measured using single-tone, stepped swept-sine, continuous swept-sine, and broadband methods.The following table lists the basic features of four techniques for measuring frequency response. Frequency Response Measurement Techniques Single-Tone Stepped Swept-Sine Continuous

Techniques for Measuring Frequency
 Response

Frequency response can be measured using single-tone, stepped swept-sine, continuous
 swept-sine, and broadband methods.

The following table lists the basic features of four techniques for measuring frequency
 response.

| Single-Tone | Stepped Swept-Sine | Continuous Swept-Sine | Broadband |
| --- | --- | --- | --- |
| Pure-tone excitation Arbitrary test frequencies Single-point spectral resolution Optimal dynamic range Simple and simultaneous measurement of linear response, harmonic distortion, and noise | Stepped-sine excitation Arbitrary test frequencies Test time dominated by low-frequency test points Can optimize dynamic range by using custom amplitudes Simultaneous measurement of linear response and harmonic distortion | Stepped-sine excitation Arbitrary test frequencies Test time dominated by low-frequency test points Can optimize dynamic range by using custom amplitudes Simultaneous measurement of linear response and harmonic distortion | Broadband excitation (chirp, noise, and impulse) Arbitrary frequency distribution of excitation Test time dominated by required frequency resolution and averaging Signals with high crest factors sacrifice dynamic range Simultaneous measurement of linear response over the entire frequency spectrum |

Parent topic:

Frequency Response and Stimulus Signal

<!--NI_TOPIC bundle=labview-sound-and-vibration-toolkit path=continuous-averaging.html language=enus -->
## TOPIC 00022: Continuous Averaging

- bundle_id: `labview-sound-and-vibration-toolkit`
- source_path: `continuous-averaging.html`
- source_url: https://docs-be.ni.com/bundle/labview-sound-and-vibration-toolkit/raw/resource/enus/continuous-averaging.html
- document_id: `labview-sound-and-vibration-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Continuous linear averaging can process small chunks of data, keep track of the intermediate results, and integrate the measurement over time, allowing you to perform level measurements over a longer period of time than other linear averaging methods. Sometimes you might need to perform level measur

Continuous Averaging

Continuous linear averaging can process small chunks of data, keep track of the
 intermediate results, and integrate the measurement over time, allowing you to perform level
 measurements over a longer period of time than other linear averaging methods.

Sometimes you might need to perform level measurements over a longer period of time, for
 example, for one hour of data with a sampling frequency of 51.2 kS/s. You would need to
 acquire more than 184 million samples. The memory required to accumulate such a large number
 of samples might prohibit you from obtaining the number of samples required for the
 analysis.

In continuous averaging, you reset the process once at the beginning, or
 t<sub>1</sub>, of the measurement, as shown in the following figure.

Figure 27.

[IMAGE alt='1378' src='GUID-6A692B69-98F3-48E0-B0F6-55C775B23710-a5.gif']

The final result at time t<sub>f</sub> is the result of processing all
 samples and is the same result as processing all the samples in one block that includes all
 samples from t<sub>1</sub> to t<sub>f</sub>.

Parent topic:

Linear Averaging

Related concepts:

- Level Measurements

<!--NI_TOPIC bundle=labview-sound-and-vibration-toolkit path=continuous-frequency-sweep.html language=enus -->
## TOPIC 00023: Continuous Frequency Sweep

- bundle_id: `labview-sound-and-vibration-toolkit`
- source_path: `continuous-frequency-sweep.html`
- source_url: https://docs-be.ni.com/bundle/labview-sound-and-vibration-toolkit/raw/resource/enus/continuous-frequency-sweep.html
- document_id: `labview-sound-and-vibration-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: A continuous swept-sine measurement uses a chirp signal to excite the device under test (DUT). A chirp signal is a signal whose frequency varies with time. The following figure shows a logarithmic chirp signal, a linear chirp signal, and corresponding frequency profiles. Frequency Profiles of Exampl

Continuous Frequency Sweep

A continuous swept-sine measurement uses a chirp signal to excite the device
 under test (DUT).

A chirp signal is a signal whose frequency varies with time. The
 following figure shows a logarithmic chirp signal, a linear
 chirp signal, and corresponding frequency profiles.

Figure 69.

[IMAGE alt='1378' src='GUID-614CBAC7-BCB5-4373-871C-236C136CA13F-a5.png']

The frequency of the linear chirp signal varies with time linearly. The
 frequency of the logarithmic chirp signal varies exponentially
 as a function of time.

You analyze the output of the DUT to acquire swept-sine measurement
 results, such as the frequency response, distortion, and time
 waveform of one or multiple harmonics. The following figure
 shows the process of a continuous swept-sine measurement.

Figure 70.

[IMAGE alt='1378' src='GUID-0B749327-1B49-439F-8F3A-A75E7B3A9C46-a5.png']

The continuous swept-sine measurement acquires the time-domain response
 of the DUT under excitation. The time-domain response signal is
 even-time-spaced. You use the resampling method to convert the
 time-domain response signal to an even-angle signal. You sample
 the even-angle response signal at a constant phase-angle
 interval of the excitation signal. Because you know the phase
 and time relationship of the excitation signal, you can
 calculate the signal amplitude at the time instance that
 corresponds to even-angle positions. You then use the calculated
 values to form the even-angle signal. The following figure shows
 the effect of resampling on a chirp signal in a continuous
 swept-sine measurement.

Figure 71.

[IMAGE alt='1378' src='GUID-AC97E709-4E05-4FD9-AB6B-AA7C05D3E7F6-a5.png']

In the upper-left time signal, as the frequency content of the chirp
 signal becomes higher, the phase-angle interval between adjacent
 time samples becomes larger. Accordingly, the period of the
 signal becomes smaller and the frequency span becomes wider.
 Identifying the fundamental and harmonic components in the
 frequency spectrum becomes difficult. In the upper-right
 even-angle signal, the phase-angle interval between adjacent
 samples remains constant despite the frequency variation. The
 period of the even-angle signal is constant. Thus you can apply
 FFT or filtering to the even-angle signal to extract the
 fundamental and harmonic components of specified harmonics in
 the response signal. The magnitude and phase of the fundamental
 component or the first harmonic component are the frequency
 response of the DUT. Use the harmonic components to determine
 whether the DUT produces specific undesired distortion or
 nonlinear effects.

You can use the same resampling method to convert the even-angle signal
 to an even-time signal. You can filter out fundamental and
 harmonic components in angular domain and convert them to time
 waveforms. Use these time waveforms to perform a sound quality
 analysis. You also can subtract the fundamental signal from the
 original time-response signal to detect any residual components
 in the time-response signal.

The following list describes the advantages of using a continuous
 swept-sine measurement.

- You can set the frequency range and chirp duration
 separately to excite the DUT over the test frequency
 range in the required test duration.
- A continuous swept-sine measurement requires less time than
 a stepped swept-sine measurement. The chirp signal
 is phase-continuous, which allows for smooth
 broadband excitation. Smoother broadband excitation
 can minimize disturbances and abrupt signal changes
 to the DUT.
- A continuous swept-sine measurement can produce time
 waveforms of fundamental, harmonic, or residue
 components. You can perform a sound quality analysis
 on the swept-sine measurement results using these
 time waveforms.
- The sinusoidal chirp signal enables you to perform a
 simultaneous measurement of the linear response and
 harmonic distortion.
- You can perform a continuous swept-sine measurement in
 real-time by processing sequential blocks of data.
 You can take advantage of the multi-core processing
 capability that LabVIEW provides for multi-channel
 computation-intensive applications. You also can
 perform a continuous swept-sine measurement in
 one-shot to allow for finite acquisitions and
 post-processing logged data.

Parent topic:

Frequency Sweep

<!--NI_TOPIC bundle=labview-sound-and-vibration-toolkit path=coordinate-systems.html language=enus -->
## TOPIC 00024: Coordinate Systems

- bundle_id: `labview-sound-and-vibration-toolkit`
- source_path: `coordinate-systems.html`
- source_url: https://docs-be.ni.com/bundle/labview-sound-and-vibration-toolkit/raw/resource/enus/coordinate-systems.html
- document_id: `labview-sound-and-vibration-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following coordinate systems are used to measure human vibration's effects on the body. The following figure shows the coordinate system used to measure hand-arm human vibration, as defined by ISO 5348:1986. Human Hand-Arm Coordinate System The following figure shows the coordinate system used t

Coordinate Systems

The following coordinate systems are used to measure human vibration's
 effects on the body.

The following figure shows the coordinate system used to measure hand-arm
 human vibration, as defined by ISO 5348:1986.

Figure 64.

[IMAGE alt='1378' src='GUID-2345D9E1-305B-4FDB-BBD3-078F9E192CF6-a5.gif']

The following figure shows the coordinate system used to measure
 whole-body human vibration, as defined by ISO 2631-1:1997.

Figure 65.

[IMAGE alt='1378' src='GUID-76EF354E-532B-4877-BBCB-23AC475C77BE-a5.gif']

Parent topic:

Effects of Vibration

<!--NI_TOPIC bundle=labview-sound-and-vibration-toolkit path=crest-factor.html language=enus -->
## TOPIC 00025: Crest Factor

- bundle_id: `labview-sound-and-vibration-toolkit`
- source_path: `crest-factor.html`
- source_url: https://docs-be.ni.com/bundle/labview-sound-and-vibration-toolkit/raw/resource/enus/crest-factor.html
- document_id: `labview-sound-and-vibration-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The relative phases of the constituent tones with respect to each other determine the crest factor of a multitone signal with specified amplitude. The crest factor is the ratio of the peak magnitude to the RMS value of the signal.As an example, a sine wave has a crest factor of 1.414:1. The followin

Crest Factor

The relative phases of the constituent tones with respect to each other
 determine the crest factor of a multitone signal with specified
 amplitude. The crest factor is the ratio of the peak magnitude to the
 RMS value of the signal.

As an example, a sine wave has a crest factor of 1.414:1. The following equation defines the
 crest factor:

F

c

=

V

p

k

V

r

m

s

where

F<sub>c</sub> is the crest
 factor

V<sub>pk</sub> is the peak value of the
 signal

V<sub>rms</sub> is the RMS value of the
 signal.

Parent topic:

Level Measurements

<!--NI_TOPIC bundle=labview-sound-and-vibration-toolkit path=delay-compensation.html language=enus -->
## TOPIC 00026: Delay Compensation

- bundle_id: `labview-sound-and-vibration-toolkit`
- source_path: `delay-compensation.html`
- source_url: https://docs-be.ni.com/bundle/labview-sound-and-vibration-toolkit/raw/resource/enus/delay-compensation.html
- document_id: `labview-sound-and-vibration-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: All dynamic signal acquisition (DSA) devices and some data acquisition (DAQ) devices with anti-aliasing filters or other filter protection have an input filter delay for which you might need to compensate.When acquiring a tachometer signal with an analog data acquisition channel, you do not have to

Delay Compensation

All dynamic signal acquisition (DSA) devices and some data acquisition (DAQ) devices
 with anti-aliasing filters or other filter protection have an input filter delay for which
 you might need to compensate.

When acquiring a tachometer signal with an analog data acquisition channel, you do not have to
 compensate for the input filter delay. The vibration, sound, and tachometer acquisition
 channels use the same anti-aliasing filter, and the vibration, sound, and tachometer
 signals therefore contain the same delay. A counter device does not have an
 anti-aliasing filter that delays the signal. If you acquire the tachometer signal with a
 counter device, you must compensate for the input filter delay in the vibration or sound
 acquisition channel.

For the NI 446x, NI 447x, and NI 449x series DSA devices, and for the NI 9229, NI 9233, NI 9234,
 and NI 9239 C Series devices, the OAT Build Digital Tacho Info
 VI computes the phase delay automatically. For other types of
 DAQ devices, you must specify the appropriate device information
 to perform the compensation. You can find the group delay
 information for individual DAQ devices in the device
 specifications.

Parent topic:

Waveform Conditioning

Related concepts:

- Anti-Aliasing
- Analog Tachometer Signals

<!--NI_TOPIC bundle=labview-sound-and-vibration-toolkit path=delay-measurements.html language=enus -->
## TOPIC 00027: Delay Measurements

- bundle_id: `labview-sound-and-vibration-toolkit`
- source_path: `delay-measurements.html`
- source_url: https://docs-be.ni.com/bundle/labview-sound-and-vibration-toolkit/raw/resource/enus/delay-measurements.html
- document_id: `labview-sound-and-vibration-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The propagation delay is the interval between when a sample is generated on the output of your measurement device and when the corresponding sample is acquired on the input side. Quantifying the signal propagation delay is important in many applications involving stimulus and response testing. Propa

Delay Measurements

The propagation delay is the interval between when a sample is generated on the
 output of your measurement device and when the corresponding sample is acquired on the input
 side. Quantifying the signal propagation delay is important in many applications involving
 stimulus and response testing.

Propagation delay can be expressed either in terms of samples or time.

The two main sources of propagation delay are signal propagation from the measurement device to
 and from the device under test (DUT) and the measurement device
 itself. In electrical systems, propagation delay caused by
 signal propagation from the measurement device to and from the
 DUT is often negligible, unless you are testing at very high
 frequencies. However, the delay is often significant in
 mechanical or acoustical tests. For example, if the DUT is a
 speaker, it is important to consider the time for sound to
 travel from the speaker to the microphone.

Determining the propagation delay of the measurement system allows you measure and evaluate
 additional delay from the DUT.

Parent topic:

Time-Domain Analysis

Related concepts:

- Propagation Delay Calibration

<!--NI_TOPIC bundle=labview-sound-and-vibration-toolkit path=detection-distortion-and-channel-characteriza.html language=enus -->
## TOPIC 00028: Detection, Distortion, and Channel Characterization

- bundle_id: `labview-sound-and-vibration-toolkit`
- source_path: `detection-distortion-and-channel-characteriza.html`
- source_url: https://docs-be.ni.com/bundle/labview-sound-and-vibration-toolkit/raw/resource/enus/detection-distortion-and-channel-characteriza.html
- document_id: `labview-sound-and-vibration-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Detection is the measurement of specific signal components including DC, tones, and noise. Detection and distortion measurements quantify linear and non-linear components of a signal. Channel characterization measurements quantify the quality of the signal path, or the channel. Channel characterizat

Detection, Distortion, and Channel
 Characterization

Detection is the measurement of specific signal components including DC, tones, and
 noise. Detection and distortion measurements quantify linear and non-linear components of a
 signal. Channel characterization measurements quantify the quality of the signal path, or the
 channel. Channel characterization often compares detected signal components with a reference,
 such as a known excitation amplitude, full scale, or the same signal components on a reference
 signal or channel.

The following table shows different measurements in detection, distortion, and channel
 characterization:

| Detection | Distortion | Channel Characterization |
| --- | --- | --- |
| DC level AC level Tone frequencies Tone amplitudes Tone phases Noise floor Power in band | Total harmonic distortion Total harmonic distortion plus noise Signal in noise and distortion Signal-to-noise ratio Intermodulation distortion | Idle-channel noise Gain and phase Crosstalk Spurious free dynamic range Dynamic range Group delay Phase linearity |

- [Tone Detection](tone-detection.html) Tone detection identifies the tone with maximum amplitude or all the tones with an amplitude that exceeds a specified threshold. You also can confine the tone detection to a specific frequency range.
- [Distortion](distortion.html) Distortion is the addition of signal components that are not part of the original signal. You can find these additional components in harmonics and intermodulations of the input frequencies.
- [Channel Characterization](channel-characterization.html) The NI Sound and Vibration Measurement Suite offers the means for various measurements that assess the performance and behavior of the communication or signal pathway your channel performance is optimized, ensuring your channel performance is optimized.

<!--NI_TOPIC bundle=labview-sound-and-vibration-toolkit path=digital-tachometer-signals.html language=enus -->
## TOPIC 00029: Digital Tachometer Signals

- bundle_id: `labview-sound-and-vibration-toolkit`
- source_path: `digital-tachometer-signals.html`
- source_url: https://docs-be.ni.com/bundle/labview-sound-and-vibration-toolkit/raw/resource/enus/digital-tachometer-signals.html
- document_id: `labview-sound-and-vibration-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: A digital tachometer signal is properly conditioned for acquisition from the input channel of a counter device.A counter device typically operates at a much higher sampling rate than the analog input channels used to acquire sound and vibration signals. The counter device also can detect pulses dire

Digital Tachometer Signals

A digital tachometer signal is properly conditioned for acquisition from the input
 channel of a counter device.

A counter device typically operates at a much higher sampling rate than the analog input
 channels used to acquire sound and vibration signals. The counter device also can detect
 pulses directly without using additional VIs to set a threshold for the tachometer
 signal. For these reasons, a counter device is ideal for acquiring tachometer signals at
 high speeds or tachometer signals that encoders generate. A digital tachometer signal is
 usually more accurate than an analog tachometer signal.

Digital tachometer signals must be transistor-transistor logic (TTL) compatible. Acquiring a
 digital tachometer signal requires additional devices, such as a
 counter or timer device and a signal conditioning device, to
 condition the tachometer signal for TTL compatibility.

You also can acquire a digital tachometer signal using a multi-function reconfigurable I/O
 device, such as the NI PXI-7831R. This kind of device allows you
 to use the LabVIEW FPGA Module to configure the digital lines as
 inputs, outputs, or counters. You also can perform tachometer
 signal conditioning with the device or configure a 64-bit
 counter.

Parent topic:

Rotational Speed

Related concepts:

- Sampling Rate
- Analog Tachometer Signals

<!--NI_TOPIC bundle=labview-sound-and-vibration-toolkit path=displacement-transducers.html language=enus -->
## TOPIC 00030: Displacement Transducers

- bundle_id: `labview-sound-and-vibration-toolkit`
- source_path: `displacement-transducers.html`
- source_url: https://docs-be.ni.com/bundle/labview-sound-and-vibration-toolkit/raw/resource/enus/displacement-transducers.html
- document_id: `labview-sound-and-vibration-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use displacement transducers to obtain measurements like the relative displacement of a rotating shaft surface.A typical displacement transducer is a shaft-sensing proximity probe. A proximity probe is a non-contacting transducer mounted on a stationary mechanical structure to measure the di

Displacement Transducers

You can use displacement transducers to obtain measurements like the relative
 displacement of a rotating shaft surface.

A typical displacement transducer is a shaft-sensing proximity probe. A proximity probe is a
 non-contacting transducer mounted on a stationary mechanical structure to measure the
 distance between the probe tip and the shaft surface. A proximity probe has signal
 response between DC and 1.5 kHz, as well as flat phase response in the operational
 range. You typically use proximity probes in lower frequency measurements.

You can use a proximity probe to perform machine monitoring and protection measurements for DUTs
 with fluid film bearings. Because the flexible fluid film
 bearing and heavy housing usually generate low-frequency,
 external vibration responses, an accelerometer or a velocity
 transducer cannot measure the vibration effectively. By
 measuring the relative displacement of the shaft, a permanently
 mounted proximity probe can measure the vibration through shaft
 motion. You also can use proximity probes for functions such as
 radial or axial position monitoring and rotational speed
 calculation. A proximity probe is a common type of
 tachometer.

A proximity probe is susceptible to shaft surface scratches, circular irregularity, shaft bow,
 and variations in electrical properties. Accurate displacement
 signal measurements require compensation to remove these signal
 errors. The NI Sound and Vibration Measurement Suite provides
 Weighting and Filtering VIs and Reference Data Processing VIs to
 perform compensation to remove these signal errors.

Parent topic:

Vibration

<!--NI_TOPIC bundle=labview-sound-and-vibration-toolkit path=distortion.html language=enus -->
## TOPIC 00031: Distortion

- bundle_id: `labview-sound-and-vibration-toolkit`
- source_path: `distortion.html`
- source_url: https://docs-be.ni.com/bundle/labview-sound-and-vibration-toolkit/raw/resource/enus/distortion.html
- document_id: `labview-sound-and-vibration-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Distortion is the addition of signal components that are not part of the original signal. You can find these additional components in harmonics and intermodulations of the input frequencies. Distortion is generally an unwanted response because of non-linearities in the device under test.Distortion m

Distortion

Distortion is the addition of signal components that are not part of the
 original signal. You can find these additional components in harmonics and
 intermodulations of the input frequencies.

Distortion is generally an unwanted response because of non-linearities in the device under
 test.

Distortion measurements use the following equations:

∑

P

Harmonics

=

(

H

2

)

2

+

(

H

3

)

2

+

...

+

(

H

K

)

2

∑

P

Harmonics

+

∑

P

Noise

=

(

H

2

)

2

+

(

H

3

)

2

+

...

+

(

H

K

)

2

+

(

N

)

2

∑

P

Noise

=

(

F

)

2

+

(

H

2

)

2

+

...

+

(

H

K

)

2

+

(

N

)

2

where specific signal components are identified as

F is the fundamental tone root mean square (RMS) level

K is the maximum harmonic in the measurement bandwidth

H
 <sub>i</sub> is the i<sup>th</sup> harmonic
 RMS level, where i is an integer
 <2..K>

N is the noise RMS level

- [Signal-to-Noise Ratio](signal-to-noise-ratio.html) The signal-to-noise ratio (SNR) compares the level of the input signal to the background noise present at detection.
- [Total Harmonic Distortion (THD)](total-harmonic-distortion-thd.html) To determine the total amount of nonlinear distortion, also known as total harmonic distortion (THD), a system introduces, measure the amplitudes of the harmonics the system introduces relative to the amplitude of the fundamental frequency.
- [Total Harmonic Distortion Plus Noise (THD + N)](total-harmonic-distortion-plus-noise-thd-n.html) Real-world signals usually contain noise. A system can introduce additional noise into the signal. Total harmonic distortion plus noise (THD + N) measures signal distortion while taking into account the amount of noise power present in the signal.
- [Signal Noise and Distortion (SINAD)](signal-noise-and-distortion-sinad.html) Signal noise and distortion (SINAD) is the reciprocal of THD+N. SINAD takes into account both harmonics and noise.
- [Intermodulation Distortion](intermodulation-distortion.html) Intermodulation distortion (IMD) is the measurement of distortion due to nonlinearity in the device under test (DUT). IMD measurements use a dual-tone test signal composed of a low-frequency tone at f 1 and a high-frequency tone at f 2 .
- [Intermodulation Distortion Standards](intermodulation-distortion-standards.html) Several standards define IMD measurements. These standards are best used depending on the type of intermodulation distortion you are trying to capture or similar.

Parent topic:

Detection, Distortion, and Channel Characterization

<!--NI_TOPIC bundle=labview-sound-and-vibration-toolkit path=dual-channel-crosstalk.html language=enus -->
## TOPIC 00032: Dual-Channel Crosstalk

- bundle_id: `labview-sound-and-vibration-toolkit`
- source_path: `dual-channel-crosstalk.html`
- source_url: https://docs-be.ni.com/bundle/labview-sound-and-vibration-toolkit/raw/resource/enus/dual-channel-crosstalk.html
- document_id: `labview-sound-and-vibration-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: A crosstalk measurement analyzes the amplification and phase lag between the reference channel and the idle response channel at the test frequency. You can identify the detected tone amplitude and phase on the stimulus channel. The stimulus tone amplitude and phase are treated as references when spe

Dual-Channel Crosstalk

A crosstalk measurement analyzes the amplification and phase lag between the
 reference channel and the idle response channel at the test frequency.

You can identify the detected tone amplitude and phase on the stimulus channel. The
 stimulus tone amplitude and phase are treated as references when specifying the tone
 relative amplitude and phase of the idle response channel. You can search for an idle
 response tone at the same frequency as the stimulus tone.

The measurement analysis of crosstalk is equivalent to that performed for a gain and
 phase measurement. The difference between these two measurements is that the gain and
 phase measurement is applied on the active response channel, while the crosstalk
 measurement is applied to the idle response channel. The following figure shows this
 difference.

Figure 75.

[IMAGE alt='1378' src='GUID-079FA6B3-E473-4BAD-BF59-0E53CE472952-a5.gif']

Parent topic:

Channel Characterization

<!--NI_TOPIC bundle=labview-sound-and-vibration-toolkit path=dual-channel-gain-and-phase.html language=enus -->
## TOPIC 00033: Calculating Dual-Channel Gain and Phase

- bundle_id: `labview-sound-and-vibration-toolkit`
- source_path: `dual-channel-gain-and-phase.html`
- source_url: https://docs-be.ni.com/bundle/labview-sound-and-vibration-toolkit/raw/resource/enus/dual-channel-gain-and-phase.html
- document_id: `labview-sound-and-vibration-toolkit`
- page_type: `leaf`
- content_type: `task`
- source_description: Gain and phase measure the amplification and the phase lag between the stimulus channel and the response channel at the test frequency. This lag time must be accounted for. Gain and phase perform a dual-channel measurement that requires both stimulus and response signals. A single-channel measuremen

Calculating Dual-Channel Gain and
 Phase

Gain and phase measure the amplification and the phase lag between the stimulus
 channel and the response channel at the test frequency. This lag time must be accounted
 for.

Gain and phase perform a dual-channel
 measurement that requires both stimulus and response signals. A single-channel
 measurement reads only the response signal. To account for the the lag time between the
 stimulus channel and the response channel:

1. Identify the detected tone amplitude and phase on the stimulus channel.
2. Treat the stimulus tone amplitude and phase as references when specifying the
 tone relative amplitude and phase of the response channel.
3. Search for a response channel tone at the same frequency as the stimulus
 tone.

You have the option of generating
 the stimulus signal from the acquisition device, a separate output device, or an
 external source when the stimulus and response measurements are acquired. If you are
 using a dynamic signal acquisition (DSA) device, NI recommends that you perform a
 dual-channel instead of a single-channel measurement when possible. Performing a
 dual-channel measurement takes full advantage of the interchannel gain mismatch and
 simultaneous sampling of the analog input channels. Refer to the DSA device
 specifications for more information. For example, in single-channel mode, the
 measurement uncertainty when using an NI PXI-4461 is 0.1 dB, whereas in dual-channel
 mode, the measurement uncertainty is typically 0.01 dB.

Parent topic:

Channel Characterization

<!--NI_TOPIC bundle=labview-sound-and-vibration-toolkit path=dynamic-range.html language=enus -->
## TOPIC 00034: Dynamic Range

- bundle_id: `labview-sound-and-vibration-toolkit`
- source_path: `dynamic-range.html`
- source_url: https://docs-be.ni.com/bundle/labview-sound-and-vibration-toolkit/raw/resource/enus/dynamic-range.html
- document_id: `labview-sound-and-vibration-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: A dynamic range measurement quantifies the distortion and noise found in the device under test (DUT) output when a low-level signal is provided. Typically, the dynamic range is measured with the amplitude of the excitation signal set to –60 dB FS, where FS is the DUT input channel full-scale amplitu

Dynamic Range

A dynamic range measurement quantifies the distortion and noise found in the device
 under test (DUT) output when a low-level signal is provided.

Typically, the dynamic range is measured with the amplitude of the excitation signal set
 to –60 dB FS, where FS is the DUT input channel full-scale amplitude. Use the following
 equation to calculate a dynamic range.

DR

=

F

∑

P

N

o

i

s

e

+

∑

P

H

a

r

m

o

n

i

c

s

The following figure shows the connection scheme for a dynamic range measurement.

Figure 77.

[IMAGE alt='1378' src='GUID-376706C5-B3F0-4FE1-AB33-8E0D9A77AF35-a5.gif']

Parent topic:

Channel Characterization

<!--NI_TOPIC bundle=labview-sound-and-vibration-toolkit path=dynamic-signals.html language=enus -->
## TOPIC 00035: Dynamic Signals

- bundle_id: `labview-sound-and-vibration-toolkit`
- source_path: `dynamic-signals.html`
- source_url: https://docs-be.ni.com/bundle/labview-sound-and-vibration-toolkit/raw/resource/enus/dynamic-signals.html
- document_id: `labview-sound-and-vibration-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: This section describes methods for obtaining sound and vibration data that you can analyze with the NI Sound and Vibration Measurement Suite.This section also describes sensing devices, basic requirements for data acquisition, and additional requirements for dynamic signal analysis. Refer to the fol

Dynamic Signals

This section describes methods for obtaining sound and vibration data that you can
 analyze with the NI Sound and Vibration Measurement Suite.

This section also describes sensing devices, basic requirements for data acquisition, and
 additional requirements for dynamic signal analysis. Refer to the following sections for
 more information.

- [Measurement Types and Transducers](measurement-types-and-transducers.html) This section describes the measurement types you use in sound and vibration analysis, as well as the transducers for obtaining appropriate signals.
- [Methods for Acquiring and Simulating Dynamic Signals](acquiring-and-simulating-dynamic-signals.html) Dynamic signals can be acquired using a DAQ device system or they can be simulated using generation VIs.
- [Buffering](buffering.html) When a group of channels share timestamp, sample rate, and channel length properties, a buffer can be used to accumulate and share data between different sections of code. You can use a buffer to decouple one source (producer) of dynamic signals from one or multiple readers (consumers).

<!--NI_TOPIC bundle=labview-sound-and-vibration-toolkit path=effects-of-vibration.html language=enus -->
## TOPIC 00036: Effects of Vibration

- bundle_id: `labview-sound-and-vibration-toolkit`
- source_path: `effects-of-vibration.html`
- source_url: https://docs-be.ni.com/bundle/labview-sound-and-vibration-toolkit/raw/resource/enus/effects-of-vibration.html
- document_id: `labview-sound-and-vibration-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Human vibration refers to the effects of mechanical vibration on the human body. Excessive exposure to mechanical vibrations can negatively affect the human body.For example, exposure to whole-body vibration from operating machinery can lead to physical problems such as spinal disorders. Measuring a

Effects of Vibration

Human vibration refers to the effects of mechanical vibration on the human body.
 Excessive exposure to mechanical vibrations can negatively affect the human
 body.

For example, exposure to whole-body vibration from operating machinery can lead to physical
 problems such as spinal disorders. Measuring and analyzing human vibration signals can
 help control the negative effects of mechanical vibration on the human body. The
 following list includes three types of human vibration signals that you might measure
 and analyze.

- hand-arm vibration signals
- whole-body vibration signals
- low-frequency whole-body vibration signals

Parent topic:

Human Response

<!--NI_TOPIC bundle=labview-sound-and-vibration-toolkit path=end-to-end-channel-gain-calibration.html language=enus -->
## TOPIC 00037: End-to-End Channel Gain Calibration

- bundle_id: `labview-sound-and-vibration-toolkit`
- source_path: `end-to-end-channel-gain-calibration.html`
- source_url: https://docs-be.ni.com/bundle/labview-sound-and-vibration-toolkit/raw/resource/enus/end-to-end-channel-gain-calibration.html
- document_id: `labview-sound-and-vibration-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Accurate digitization of a measured signal depends on calibrating the entire measurement channel and factoring in each of the individual component gains.A measurement system must digitize a measured signal accurately. In a real-world measurement system, each component has some influence on the signa

End-to-End Channel Gain Calibration

Accurate digitization of a measured signal depends on calibrating the entire
 measurement channel and factoring in each of the individual component gains.

A measurement system must digitize a measured signal accurately. In a real-world measurement
 system, each component has some influence on the signal. The
 sensor sensitivity is a useful measurement. However, you can
 assume that any external cables pass the signal with zero
 attenuation, that all external amplifiers are set correctly and
 apply a precise amount of gain, and that the absolute gain of
 the data acquisition channel is specified with tolerances.
 Rather than quantify the gain of each component in the
 measurement system, you measure the gain of the entire
 measurement channel from end to end, or from sensor to
 digitization, which is more accurate and useful. You can achieve
 the most accurate measurements when you calibrate the sensor
 along with the specific cables, amplifier, and data acquisition
 channel where you use the sensor. Thus, you can factor the
 individual component gains into the calibrated sensor
 sensitivity.

Parent topic:

System Calibration

<!--NI_TOPIC bundle=labview-sound-and-vibration-toolkit path=envelope-detection.html language=enus -->
## TOPIC 00038: Envelope Detection

- bundle_id: `labview-sound-and-vibration-toolkit`
- source_path: `envelope-detection.html`
- source_url: https://docs-be.ni.com/bundle/labview-sound-and-vibration-toolkit/raw/resource/enus/envelope-detection.html
- document_id: `labview-sound-and-vibration-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Envelope detection is a technique to extract the modulating signal, or envelope signal, from an amplitude-modulated signal.You can use the envelope detection technique to identify mechanical faults that have an amplitude-modulating effect on the vibration signal of a machine. The power spectrum of t

Envelope Detection

Envelope detection is a technique to extract the modulating signal, or envelope
 signal, from an amplitude-modulated signal.

You can use the envelope detection technique to identify mechanical faults that have an
 amplitude-modulating effect on the vibration signal of a machine. The power spectrum of
 the envelope signal exhibits peaks that can reveal the source of faults. A fault on a
 rolling-element bearing typically has an amplitude-modulating effect on the vibration
 signal of the bearing. You thus can use the envelope detection technique to perform
 fault detection on rolling-element bearings.

You can use an accelerometer and a tachometer to measure the vibration signal and the rotational
 speed, respectively, of a rolling-element bearing. Choose a
 sampling rate that is at least 2.56 times higher than the
 highest frequency component of the signal of interest. Also
 choose an accelerometer with a high cutoff frequency to cover
 the frequency band that the envelope detection technique uses.
 Then place the accelerometer close to the bearing so the
 distance between the fault location and the accelerometer does
 not affect the signal transmission. When the accelerometer is
 far away from the fault location, the envelope detection
 technique might fail.

A fault on a rolling-element bearing generates a low-level impulse every time the local fault
 contacts another part of the bearing. This low-level impulse has
 an amplitude-modulating effect on the vibration signal. The
 modulating effect spreads over a wide frequency range because
 the impulse has a short period. In the low frequency band of the
 vibration signal, imbalance, misalignment, or mechanical
 looseness of the bearing might generate vibration signals that
 overwhelm the low-level impulses. Thus the envelope detection
 technique focuses on a narrow band range in the high frequency
 band, which is useful for detecting the low-level impulses that
 are below the noise level in the normal spectrum. The lower
 frequency of the band range is typically greater than ten times
 the rotational speed in order to eliminate common harmonics of
 the rotational speed. The upper frequency of the band range is
 usually sixty times the outer race frequency or two hundred
 times the rotational speed in order to attenuate high frequency
 noise and vibration components. The envelope detection technique
 involves the following three steps: shifting the narrow band
 range in the high frequency band to the base band, filtering the
 frequency-shifted signal using a lowpass filter, and calculating
 the envelope signal of the lowpass-filtered signal.

You usually use the results of envelope detection in trend analysis. The trend of the magnitude
 of faulty components can indicate the condition of the bearing.
 You must use the same transducers mounted on the same location
 to ensure consistent measurement of the vibration signal and the
 rotational speed. Trend analysis is ideal for early fault
 detection because the magnitude of the faulty component might
 decrease when a fault becomes severe.

Parent topic:

Bearings

Related concepts:

- Accelerometers
- Rotational Speed
- Sampling Rate

<!--NI_TOPIC bundle=labview-sound-and-vibration-toolkit path=equal-confidence.html language=enus -->
## TOPIC 00039: Equal Confidence

- bundle_id: `labview-sound-and-vibration-toolkit`
- source_path: `equal-confidence.html`
- source_url: https://docs-be.ni.com/bundle/labview-sound-and-vibration-toolkit/raw/resource/enus/equal-confidence.html
- document_id: `labview-sound-and-vibration-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Equal confidence averaging is exponential averaging with a specific time constant set for each individual band.Each time constant is set so that the standard deviation of the band power measurement equals the confidence value in decibels.

Equal Confidence

Equal confidence averaging is exponential averaging with a specific time constant set
 for each individual band.

Each time constant is set so that the standard deviation of the band power measurement equals the
 confidence value in decibels.

Parent topic:

Fractional-Octave Averaging

<!--NI_TOPIC bundle=labview-sound-and-vibration-toolkit path=equal-loudness.html language=enus -->
## TOPIC 00040: Equal Loudness

- bundle_id: `labview-sound-and-vibration-toolkit`
- source_path: `equal-loudness.html`
- source_url: https://docs-be.ni.com/bundle/labview-sound-and-vibration-toolkit/raw/resource/enus/equal-loudness.html
- document_id: `labview-sound-and-vibration-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Loudness is a subjective indicator of the perceived noise level expressed in phons. The loudness level in phons is the sound pressure level in decibels of a 1 kHz tone having the same perceived loudness as the tone being evaluated. Thus, a 1 kHz tone with a loudness level of 30 phons is equally as l

Equal Loudness

Loudness is a subjective indicator of the perceived noise level expressed in phons.
 The loudness level in phons is the sound pressure level in decibels of a 1 kHz tone having
 the same perceived loudness as the tone being evaluated.

Thus, a 1 kHz tone with a loudness level of 30 phons is equally as loud as a 1 kHz tone
 with a sound pressure level of 30 dB referenced to 20 µPa. However, a signal frequency
 of 100 Hz requires a sound pressure level of 44 dB referenced to 20 µPa to provide the
 same loudness level.

The following figure shows equal loudness curves.

Figure 61.

[IMAGE alt='1378' src='GUID-B0D6D5DF-5482-4C7D-92EE-A5D5E44F7735-a5.gif']

Parent topic:

Perception of Sound

<!--NI_TOPIC bundle=labview-sound-and-vibration-toolkit path=exponential-averaging.html language=enus -->
## TOPIC 00041: Exponential Averaging

- bundle_id: `labview-sound-and-vibration-toolkit`
- source_path: `exponential-averaging.html`
- source_url: https://docs-be.ni.com/bundle/labview-sound-and-vibration-toolkit/raw/resource/enus/exponential-averaging.html
- document_id: `labview-sound-and-vibration-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Exponential averaging is a continuous averaging process that weights current and past data differently. The amount of weight given to past data as compared to current data depends on the exponential time constant. In exponential averaging, the averaging process continues indefinitely.The exponential

Exponential Averaging

Exponential averaging is a continuous averaging process that weights current
 and past data differently. The amount of weight given to past data as
 compared to current data depends on the exponential time constant.
 In exponential averaging, the averaging process continues
 indefinitely.

The exponential averaging mode supports the following time constants:

- Slow—Uses a time constant of 1,000 ms. Slow averaging is useful for tracking the sound pressure
 levels of signals with sound pressure levels that vary slowly.
- Fast—Uses a time constant of 125 ms. Fast averaging is useful for tracking the sound pressure of
 signals with sound pressure levels that vary quickly.
- Impulse—Uses a time constant of 35 ms if the signal is rising and 1,500 ms if the signal is
 falling. Impulse averaging is useful for tracking sudden increases in the sound pressure
 level and recording the increases so that you have a record of the changes.
- Custom—Enables you to specify a time constant suitable for your particular application.

Exponential averaging requires time-continuous blocks of data. The measurement restarts when a
 discontinuity is detected.

Parent topic:

Time-Domain Analysis

<!--NI_TOPIC bundle=labview-sound-and-vibration-toolkit path=exponential.html language=enus -->
## TOPIC 00042: Exponential

- bundle_id: `labview-sound-and-vibration-toolkit`
- source_path: `exponential.html`
- source_url: https://docs-be.ni.com/bundle/labview-sound-and-vibration-toolkit/raw/resource/enus/exponential.html
- document_id: `labview-sound-and-vibration-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Exponential averaging is a continuous averaging process that weights current and past data differently. The amount of weight given to past data as compared to current data depends on the exponential time constant. Exponential averaging can be used to average data over a long period of time, such as

Exponential

Exponential averaging is a continuous averaging process that weights current and past
 data differently. The amount of weight given to past data as compared to current data
 depends on the exponential time constant.

Exponential averaging can be used to average data over a long period of time, such as
 during machine startup, where data closer to operational temperatures is more important
 than data collected during startup.

Parent topic:

Fractional-Octave Averaging

<!--NI_TOPIC bundle=labview-sound-and-vibration-toolkit path=extended-measurement.html language=enus -->
## TOPIC 00043: Extended Measurement

- bundle_id: `labview-sound-and-vibration-toolkit`
- source_path: `extended-measurement.html`
- source_url: https://docs-be.ni.com/bundle/labview-sound-and-vibration-toolkit/raw/resource/enus/extended-measurement.html
- document_id: `labview-sound-and-vibration-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can perform extended measurements on an order power spectrum, such as unit conversion, spectrum peak search, power in band, and limit testing.Extended measurement refers to additional techniques used beyond power spectrum analysis that grant deeper insights.

Extended Measurement

You can perform extended measurements on an order power spectrum, such as unit
 conversion, spectrum peak search, power in band, and limit testing.

Extended measurement refers to additional techniques used beyond power spectrum analysis that
 grant deeper insights.

Parent topic:

Order Power Spectrum

<!--NI_TOPIC bundle=labview-sound-and-vibration-toolkit path=fault-detection-and-diagnosis.html language=enus -->
## TOPIC 00044: Fault Detection and Diagnosis

- bundle_id: `labview-sound-and-vibration-toolkit`
- source_path: `fault-detection-and-diagnosis.html`
- source_url: https://docs-be.ni.com/bundle/labview-sound-and-vibration-toolkit/raw/resource/enus/fault-detection-and-diagnosis.html
- document_id: `labview-sound-and-vibration-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI Sound and Vibration Measurement Suite supports data acquisition and calculations for diagnosing and addressing bearing faults and torsional vibration, which are the most common issues observed in rotational machinery. Refer to the following sections for more information.

Fault Detection and Diagnosis

The NI Sound and Vibration Measurement Suite supports data acquisition and
 calculations for diagnosing and addressing bearing faults and torsional vibration, which are
 the most common issues observed in rotational machinery.

Refer to the following sections for more information.

- [Bearings](bearings.html) Faults on a rolling-element bearing exhibit peaks of characteristic frequencies or orders in the power spectrum of the envelope signal.
- [Torsional Vibration](torsional-vibration.html) Torsional vibration is a common phenomenon for rotating machinery such as engines, compressors, and turbines. You must monitor and control torsional vibration in a rotating system to ensure that the system operates properly.

<!--NI_TOPIC bundle=labview-sound-and-vibration-toolkit path=fft-dft-and-zoom.html language=enus -->
## TOPIC 00045: FFT, DFT, and Zoom

- bundle_id: `labview-sound-and-vibration-toolkit`
- source_path: `fft-dft-and-zoom.html`
- source_url: https://docs-be.ni.com/bundle/labview-sound-and-vibration-toolkit/raw/resource/enus/fft-dft-and-zoom.html
- document_id: `labview-sound-and-vibration-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: FFT, DFT, and Zoom are transforms used to convert data from the time domain into the frequency domain.The Fast Fourier Transform (FFT) resolves a time waveform into its sinusoidal components. The FFT takes a block of time-domain data and returns the frequency spectrum of the data. The FFT is a digit

FFT, DFT, and Zoom

FFT, DFT, and Zoom are transforms used to convert data from the time domain
 into the frequency domain.

The Fast Fourier Transform (FFT) resolves a time waveform into its sinusoidal components. The FFT
 takes a block of time-domain data and returns the frequency
 spectrum of the data. The FFT is a digital implementation of the
 Fourier transform. Thus, the FFT does not yield a continuous
 spectrum. Instead, the FFT returns a discrete spectrum, in which
 the frequency content of the waveform is resolved into a finite
 number of frequency lines, or bins.

The algorithm used to transform samples of the data from the time domain into the frequency
 domain is the discrete Fourier transform (DFT). The DFT
 establishes the relationship between the samples of a signal in
 the time domain and their representation in the frequency
 domain. The DFT is widely used in the fields of spectral
 analysis, applied mechanics, acoustics, medical imaging,
 numerical analysis, instrumentation, and telecommunications.

Note

- [Baseband Analysis](baseband-analysis.html) Baseband analysis involves applying the FFT to each component of a time-domain signal from the minimum resolvable frequency, 0, to the maximum resolvable frequency.
- [Subset Analysis](subset-analysis.html) Subset analysis enables you to compute a subset of the baseband FFT measurement.
- [Zoom FFT Analysis](zoom-fft-analysis.html) Zoom FFT analysis achieves a finer frequency resolution than the baseband FFT.
- [Periodicity, Leakage, and Windowing](periodicity-leakage-and-windowing.html) Periodicity is a basic assumption made in FFT-based frequency analysis. The FFT algorithm implicitly assumes that every block of acquired data indefinitely repeats in both positive and negative time. When the input signal is not periodic within the block, energy appears to leak into neighboring spectral bins. This spectral leakage can hide and/or distort low-amplitude spectral components. Windowing both ensures periodicity and limits leakage.
- [Averaging Modes](averaging-modes.html) You can perform averaged measurements in frequency analysis. Averaging successive measurements usually improves measurement accuracy.

Parent topic:

Frequency-Domain Analysis

<!--NI_TOPIC bundle=labview-sound-and-vibration-toolkit path=filter-banks.html language=enus -->
## TOPIC 00046: Filter Banks

- bundle_id: `labview-sound-and-vibration-toolkit`
- source_path: `filter-banks.html`
- source_url: https://docs-be.ni.com/bundle/labview-sound-and-vibration-toolkit/raw/resource/enus/filter-banks.html
- document_id: `labview-sound-and-vibration-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Octave filter resolution is limited because only 11 octaves exist in the 16 Hz–16 KHz range. To overcome the limited resolution of octave filters, you can use other filters known as fractional-octave filters. Rather than covering one octave with a single filter, N filters are applied per octave in o

Filter Banks

Octave filter resolution is limited because only 11 octaves exist in the 16 Hz–16 KHz
 range. To overcome the limited resolution of octave filters, you can use other filters known as
 fractional-octave filters.

Rather than covering one octave with a single filter, N filters are applied per octave in
 order to improve resolution. Of the fractional-octave filters, the third-octave (1/3) filter
 is used widely for fractional-octave analysis. The following figure shows the 1/3 octave
 response at frequencies of 500 Hz, 630 Hz, and 800 Hz.

Figure 32.

[IMAGE alt='1378' src='GUID-616A29C2-251F-4554-BFB2-16452893E08A-a5.gif']

Fractional-octave analysis is a CPU-intensive operation. Increasing the number of filters
 applied to a signal increases the demands placed on the CPU and can result in increased
 computation time.

Parent topic:

Fractional-Octave Filtering

<!--NI_TOPIC bundle=labview-sound-and-vibration-toolkit path=fractional-octave-averaging.html language=enus -->
## TOPIC 00047: Fractional-Octave Averaging

- bundle_id: `labview-sound-and-vibration-toolkit`
- source_path: `fractional-octave-averaging.html`
- source_url: https://docs-be.ni.com/bundle/labview-sound-and-vibration-toolkit/raw/resource/enus/fractional-octave-averaging.html
- document_id: `labview-sound-and-vibration-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can perform the following averaged measurements with fractional-octave analysis: linear, exponential, equal confidence, and peak hold.Perform averaged measurements in the following conditions: You have continuous or gap-free blocks of time data. The number of samples in each block of time data c

Fractional-Octave Averaging

You can perform the following averaged measurements with fractional-octave analysis:
 linear, exponential, equal confidence, and peak hold.

Perform averaged measurements in the following conditions:

- You have continuous or gap-free blocks of time data.
- The number of samples in each block of time data can vary and has no impact on the filter design.
- All filters must settle before the averaged measurement is valid.
- The averaging automatically restarts when the filters are reset or when the averaging parameters change.

Refer to the following sections for more information.

- [Linear](linear.html) Linear averaging calculates an average set of values that reduces the signal, noise, and background vibration.
- [Exponential](exponential.html) Exponential averaging is a continuous averaging process that weights current and past data differently. The amount of weight given to past data as compared to current data depends on the exponential time constant.
- [Equal Confidence](equal-confidence.html) Equal confidence averaging is exponential averaging with a specific time constant set for each individual band.
- [Peak Hold Fractional-Octave Averaging](peak-hold-fractional-octave-averaging.html) In peak-hold averaging, the largest measured level value of all previous values is returned for each band until a new value exceeds the current maximum.

Parent topic:

Fractional-Octave Analysis

<!--NI_TOPIC bundle=labview-sound-and-vibration-toolkit path=fractional-octave-filtering.html language=enus -->
## TOPIC 00048: Fractional-Octave Filtering

- bundle_id: `labview-sound-and-vibration-toolkit`
- source_path: `fractional-octave-filtering.html`
- source_url: https://docs-be.ni.com/bundle/labview-sound-and-vibration-toolkit/raw/resource/enus/fractional-octave-filtering.html
- document_id: `labview-sound-and-vibration-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Fractional-octave analysis primarily depends on filters, take all of the following into consideration when performing your analysis:

Fractional-Octave Filtering

Fractional-octave analysis primarily depends on filters, take all of the following
 into consideration when performing your analysis:

- [Octave Filters](octave-filters.html) An octave filter is a filter whose passband covers one octave. An octave is the interval between two frequencies where one frequency is twice the rate of the other.
- [Bandwidth](bandwidth.html) The bandwidth of a filter denotes the range of frequencies the filter allows to pass through. Calculating the bandedge frequencies informs you of the bandwidth's characteristics.
- [Settling Time](settling-time.html) When starting or resetting the filtering operation of fractional-octave filters, a settling time is required before the measurements are valid.
- [Filter Banks](filter-banks.html) Octave filter resolution is limited because only 11 octaves exist in the 16 Hz–16 KHz range. To overcome the limited resolution of octave filters, you can use other filters known as fractional-octave filters.

Parent topic:

Fractional-Octave Analysis

<!--NI_TOPIC bundle=labview-sound-and-vibration-toolkit path=fractional-octave.html language=enus -->
## TOPIC 00049: Fractional-Octave Analysis

- bundle_id: `labview-sound-and-vibration-toolkit`
- source_path: `fractional-octave.html`
- source_url: https://docs-be.ni.com/bundle/labview-sound-and-vibration-toolkit/raw/resource/enus/fractional-octave.html
- document_id: `labview-sound-and-vibration-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Fractional-octave analysis is a technique for analyzing audio and acoustic signals. Fractional-octave analyses, especially 1/3 and 1/12 octave, exhibit characteristics analogous to the response of the human ear. Many industry standards, such as ANSI and IEC, require fractional-octave analysis. The f

Fractional-Octave Analysis

Fractional-octave analysis is a technique for analyzing audio and acoustic signals.
 Fractional-octave analyses, especially 1/3 and 1/12 octave, exhibit characteristics analogous to
 the response of the human ear. Many industry standards, such as ANSI and IEC, require
 fractional-octave analysis.

The following steps summarize fractional-octave measurement:

1. Send a time-domain signal through a bank of N bandpass filters.
2. Compute the instantaneous square value for the outputs of the N filters.
3. Average the instantaneous square values according to a selected averaging mode.
4. Display the averaged values in a bar graph.

The type of fractional-octave measurement you perform, 1/1 through 1/24 octave, determines
 the number of filters to apply, as well as the passband of those filters. The filters used are
 known as constant Q filters.

The following example is an illustration of full-octave analysis. In the example, an input
 signal acquired by a microphone is sent through 10 bandpass filters centered at the
 frequencies listed in the following illustration.

Figure 29.

[IMAGE alt='1378' src='GUID-113BEC68-9454-472E-B567-D4B7746DE2FA-a5.gif']

Figure 30.

[IMAGE alt='1378' src='GUID-5121CEBD-9625-4D1C-B0C9-BE4A356B4097-a5.gif']

- [Fractional-Octave Filtering](fractional-octave-filtering.html) Fractional-octave analysis primarily depends on filters, take all of the following into consideration when performing your analysis:
- [Fractional-Octave Averaging](fractional-octave-averaging.html) You can perform the following averaged measurements with fractional-octave analysis: linear, exponential, equal confidence, and peak hold.
- [Octave Analysis Standards](octave-analysis-standards.html) This topic contains information about the ANSI, IEC, and JIS standards regarding midband frequencies, the nominal frequencies returned by the octave analysis tools in the NI Sound and Vibration Measurement Suite, and compliance with ANSI, IEC, and JIS standards by the octave analysis tools.

Parent topic:

Frequency-Domain Analysis

Related concepts:

- Bandwidth

<!--NI_TOPIC bundle=labview-sound-and-vibration-toolkit path=frequency-domain-analysis.html language=enus -->
## TOPIC 00050: Frequency-Domain Analysis

- bundle_id: `labview-sound-and-vibration-toolkit`
- source_path: `frequency-domain-analysis.html`
- source_url: https://docs-be.ni.com/bundle/labview-sound-and-vibration-toolkit/raw/resource/enus/frequency-domain-analysis.html
- document_id: `labview-sound-and-vibration-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: This section focuses on two broad categories of frequency-domain analysis: fractional-octave and Fourier transform.This section describes frequency-domain analysis of sound and vibration signals. A discrete time-domain signal shows how a signal evolves sample-by-sample over time. The corresponding f

Frequency-Domain Analysis

This section focuses on two broad categories of frequency-domain analysis:
 fractional-octave and Fourier transform.

This section describes frequency-domain analysis of sound and vibration signals. A discrete
 time-domain signal shows how a signal evolves sample-by-sample over time. The
 corresponding frequency-domain spectrum shows how much components of different
 frequencies contribute to the overall signal. Typically, strict frequency analysis does
 not look at the time evolution of these contributions but, instead, quantifies the
 averaged contribution of each frequency component.

- [Fractional-Octave Analysis](fractional-octave.html) Fractional-octave analysis is a technique for analyzing audio and acoustic signals. Fractional-octave analyses, especially 1/3 and 1/12 octave, exhibit characteristics analogous to the response of the human ear. Many industry standards, such as ANSI and IEC, require fractional-octave analysis.
- [FFT, DFT, and Zoom](fft-dft-and-zoom.html) FFT, DFT, and Zoom are transforms used to convert data from the time domain into the frequency domain.

<!--NI_TOPIC bundle=labview-sound-and-vibration-toolkit path=frequency-domain-integration.html language=enus -->
## TOPIC 00051: Frequency-Domain Integration

- bundle_id: `labview-sound-and-vibration-toolkit`
- source_path: `frequency-domain-integration.html`
- source_url: https://docs-be.ni.com/bundle/labview-sound-and-vibration-toolkit/raw/resource/enus/frequency-domain-integration.html
- document_id: `labview-sound-and-vibration-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Frequency-domain integration is used to separate and analyze the different frequency components which make up measured signals. You can use the following strategies to obtain the spectrum of an integrated signal: Perform the integration in the time domain before computing the spectrum. Compute the s

Frequency-Domain Integration

Frequency-domain integration is used to separate and analyze the different frequency
 components which make up measured signals.

You can use the following strategies to obtain the spectrum of an integrated signal:

- Perform the integration in the time domain before computing the spectrum.
- Compute the spectrum before performing the integration in the frequency domain.

The following figure shows the results of integration in the time and frequency domains.

Figure 19.

[IMAGE alt='1378' src='GUID-F51AFAAE-F677-4134-B19F-337EE7B338CF-a5.gif']

The power spectrum is computed after the time-domain integration filters settle. The
 frequency-domain integration scales the spectrum at each frequency line. No settling time is
 necessary for the frequency-domain integration because integration filters are not involved in
 the frequency-domain integration.

Perform frequency-domain integration in the following situations to maximize performance:

- When the integrated signal is not needed in the time domain
- When spectral measurements are performed

Parent topic:

Integration

<!--NI_TOPIC bundle=labview-sound-and-vibration-toolkit path=frequency-masking.html language=enus -->
## TOPIC 00052: Frequency Masking

- bundle_id: `labview-sound-and-vibration-toolkit`
- source_path: `frequency-masking.html`
- source_url: https://docs-be.ni.com/bundle/labview-sound-and-vibration-toolkit/raw/resource/enus/frequency-masking.html
- document_id: `labview-sound-and-vibration-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: It is common for background noise to mask your test signal. When this is the case, filters are necessary to remove the masking noise. Broadband white noise can mask test tones. White noise has a spectral density that is independent of frequency. Other types of noise and signals, such as pink noise,

Frequency Masking

It is common for background noise to mask your test signal. When this is the case,
 filters are necessary to remove the masking noise.

Broadband white noise can mask test tones. White noise has a spectral density that is
 independent of frequency. Other types of noise and signals, such as pink noise,
 narrow-band noise, pure tones, and complex tones, also can mask a test signal. When
 narrow-band noise is the masking signal, masked thresholds show a very steep rise
 greater than 100 dB per decade as the test tone increases in frequency up to the center
 frequency of the narrow-band noise. This test tone increase is independent of the level
 of the masking noise. For frequencies greater than the center frequency of the noise,
 the masked threshold decreases quickly for low levels of masking noise but more slowly
 for high levels of masking noise. When pure tones are the masking signal, the signal
 needs additional filters to remove measurement artifacts such as audible beating and
 difference tones. The following figure shows the masked threshold for a masking signal
 at a frequency of 1 kHz.

Figure 63.

[IMAGE alt='1378' src='GUID-55B3CE86-E1C3-4B58-8802-6946910CD488-a5.gif']

Parent topic:

Masking

<!--NI_TOPIC bundle=labview-sound-and-vibration-toolkit path=frequency-resolution.html language=enus -->
## TOPIC 00053: Frequency Resolution

- bundle_id: `labview-sound-and-vibration-toolkit`
- source_path: `frequency-resolution.html`
- source_url: https://docs-be.ni.com/bundle/labview-sound-and-vibration-toolkit/raw/resource/enus/frequency-resolution.html
- document_id: `labview-sound-and-vibration-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The frequency resolution in a Fast Fourier Transform (FFT) must be fine enough to identify distinct tonal components of the signal independently of the DC value and the noise. Improving the frequency resolution helps you distinguish two individual tones that are close together. For example, if you a

Frequency Resolution

The frequency resolution in a Fast Fourier Transform (FFT) must be fine enough to
 identify distinct tonal components of the signal independently of the DC value and the
 noise.

Improving the frequency resolution helps you distinguish two individual tones that are close
 together. For example, if you analyze a signal that contains two tones at 1,000 Hz and 1,100
 Hz, use a sampling frequency of 10,000 Hz. Acquire data for 10 ms with a frequency resolution
 of 100 Hz. The following figure shows the results of this analysis.

Figure 33.

[IMAGE alt='1378' src='GUID-587201E6-68A9-48A6-A695-12EA6A7735DB-a5.gif']

Notice that you cannot distinguish the two tones from one another because the frequency
 spacing is less than the resolution bandwidth.

Increase the acquisition time to 1 s to achieve a frequency resolution of 1 Hz. The following
 figure shows the results obtained with a 1 s acquisition time.

Figure 34.

[IMAGE alt='1378' src='GUID-E85E32D9-D54B-4714-A739-1239B6F8F053-a5.gif']

You can distinguish the individual tones with the increased acquisition time.

The following strategies achieve a finer frequency resolution:

- Decrease the sampling frequency, f s . Decreasing
 f s usually is not practical because decreasing
 f s reduces the frequency range.
- Increase the number of samples, N . Increasing N 
 yields an increased number of lines over the original frequency range.

Implement the decreased f<sub>s</sub> strategy with zoom FFT analysis. Use
 baseband FFT and FFT-subset analyses to implement the increased N strategy. Baseband FFT
 analysis and FFT-subset analysis both achieve the same frequency resolution. However,
 FFT-subset analysis computes only a narrow subset of the spectrum.

Parent topic:

Baseband Analysis

<!--NI_TOPIC bundle=labview-sound-and-vibration-toolkit path=frequency-response-and-stimulus-signal.html language=enus -->
## TOPIC 00054: Frequency Response and Stimulus Signal

- bundle_id: `labview-sound-and-vibration-toolkit`
- source_path: `frequency-response-and-stimulus-signal.html`
- source_url: https://docs-be.ni.com/bundle/labview-sound-and-vibration-toolkit/raw/resource/enus/frequency-response-and-stimulus-signal.html
- document_id: `labview-sound-and-vibration-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Frequency response measurements compute the frequency response function (FRF) of the device under test (DUT) by comparing a stimulus signal and a response signal.The FRF expresses the complex ratio of output-to-input in the frequency domain and fully characterizes linear, time-invariant systems. The

Frequency Response and Stimulus Signal

Frequency response measurements compute the frequency response function (FRF) of the
 device under test (DUT) by comparing a stimulus signal and a response signal.

The FRF expresses the complex ratio of output-to-input in the frequency domain and fully
 characterizes linear, time-invariant systems. The magnitude and phase of the FRF
 characterize the frequency response. The magnitude is equivalent to the gain, or
 amplitude ratio, expressed as a function of frequency. The phase is equivalent to the
 relative delay, or phase shift, of each frequency component through the DUT.

Frequency response computes the transfer function of the response signal to the stimulus signal.
 You usually use the coherence to validate the frequency response
 results. The coherence quantifies the portion of the response
 signal that is linearly dependent on, or coherent with, the
 stimulus signal. The coherence ranges from 0 to 1. A coherence
 value of 1 indicates a perfect coherence.

Use the complex FRF, either real and imaginary parts or magnitude and phase components, to
 characterize the dynamic response of the DUT. Use the magnitude
 curve of the FRF to indicate the amplitude accuracy of the DUT.
 When the DUT reproduces the stimulus signal with no attenuation
 of any particular frequency band, the DUT has a flat magnitude
 curve.

Performing FRF measurements requires a signal source. Valid stimulus signals are pure tones,
 frequency sweeps, and broadband signals.

- [Single Tone](single-tone.html) A single-tone measurement requires a stimulus signal, which is always a single-tone sine wave that excites the device under test (DUT) at a specific frequency. A single-tone measurement characterizes the magnitude and phase of one specific frequency of the DUT.
- [Frequency Sweep](frequency-sweep.html) A swept-sine measurement characterizes the dynamic frequency response of a device under test (DUT).
- [Broadband](broadband.html) A broadband measurement uses a broadband signal with a flat frequency power spectrum. Broadband signals ensure that all the frequencies of interest are excited during acquisition.
- [Techniques for Measuring Frequency Response](comparing-techniques-for-measuring-frequency.html) Frequency response can be measured using single-tone, stepped swept-sine, continuous swept-sine, and broadband methods.

<!--NI_TOPIC bundle=labview-sound-and-vibration-toolkit path=frequency-response-for-time-domain-single-int.html language=enus -->
## TOPIC 00055: Frequency Response for Time-Domain Single Integration and Double Integration

- bundle_id: `labview-sound-and-vibration-toolkit`
- source_path: `frequency-response-for-time-domain-single-int.html`
- source_url: https://docs-be.ni.com/bundle/labview-sound-and-vibration-toolkit/raw/resource/enus/frequency-response-for-time-domain-single-int.html
- document_id: `labview-sound-and-vibration-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the frequency response for time-domain single integration. Frequency Response for Time-Domain Single Integration You can see the characteristic 20 dB per decade roll-off of the magnitude response of the single integration. The following figure shows the frequency response

Frequency Response for Time-Domain Single
 Integration and Double Integration

The following figure shows the frequency response for time-domain single integration.

Figure 17.

[IMAGE alt='1378' src='GUID-9C6CEE14-1339-4D5C-8020-B3A901AD72AC-a5.gif']

You can see the characteristic 20 dB per decade roll-off of the magnitude response of the
 single integration.

The following figure shows the frequency response for time-domain double integration.

Figure 18.

[IMAGE alt='1378' src='GUID-C48A30E6-288C-4DFC-B61D-FF0CEA9CB295-a5.gif']

You can see the characteristic 40 dB per decade roll-off of the magnitude response of the
 double integration.

Parent topic:

Time-Domain Integration

<!--NI_TOPIC bundle=labview-sound-and-vibration-toolkit path=frequency-sweep.html language=enus -->
## TOPIC 00056: Frequency Sweep

- bundle_id: `labview-sound-and-vibration-toolkit`
- source_path: `frequency-sweep.html`
- source_url: https://docs-be.ni.com/bundle/labview-sound-and-vibration-toolkit/raw/resource/enus/frequency-sweep.html
- document_id: `labview-sound-and-vibration-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: A swept-sine measurement characterizes the dynamic frequency response of a device under test (DUT). Swept-sine measurements use two signal-generation techniques: continuous swept-sine measurement and stepped swept-sine measurement. A continuous swept-sine measurement sweeps through a set of frequenc

Frequency Sweep

A swept-sine measurement characterizes the dynamic frequency response of a device
 under test (DUT).

Swept-sine measurements use two signal-generation techniques: continuous swept-sine
 measurement and stepped swept-sine measurement. A continuous swept-sine measurement
 sweeps through a set of frequencies to generate a chirp pattern. The following figure
 shows an example of the excitation signal for a continuous swept-sine measurement.

Figure 66.

[IMAGE alt='1378' src='GUID-5805D023-4982-4755-8D9F-98AEB7F1E5B4-a5.png']

In the previous chirp signal, the frequency linearly sweeps with time. In audio
 applications, you also use chirp signals in which the frequency exponentially sweeps
 with time.

A stepped swept-sine measurement steps through a set of frequencies. The following figure
 shows an example of the excitation signal for a stepped swept-sine measurement.

Figure 67.

[IMAGE alt='1378' src='GUID-1568223C-66AE-4C8C-A9A2-29FBFED8C643-a5.png']

A swept-sine measurement requires an excitation signal. The excitation signal is always a
 single-tone signal that excites the DUT at the test frequency. A swept-sine measurement
 can measure harmonic distortion and linear response simultaneously.

A swept-sine measurement compares the response signal from the DUT to the excitation
 signal in order to compute the frequency response function (FRF) of the DUT. The
 magnitude of the FRF is equivalent to the gain and represents the ratio of the output
 level to the input level for each test frequency. The phase of the FRF is equivalent to
 the phase lag that the DUT introduces for each test frequency.

- [Stepped Frequency Sweep](stepped-frequency-sweep.html) A stepped swept-sine measurement steps through a set of frequencies. A stepped swept-sine measurement includes dynamic measurement for the stimulus level, response level, frequency response, total harmonic distortion (THD), and individual harmonic distortion.
- [Continuous Frequency Sweep](continuous-frequency-sweep.html) A continuous swept-sine measurement uses a chirp signal to excite the device under test (DUT).

Parent topic:

Frequency Response and Stimulus Signal

<!--NI_TOPIC bundle=labview-sound-and-vibration-toolkit path=full-spectrum.html language=enus -->
## TOPIC 00057: Full Spectrum

- bundle_id: `labview-sound-and-vibration-toolkit`
- source_path: `full-spectrum.html`
- source_url: https://docs-be.ni.com/bundle/labview-sound-and-vibration-toolkit/raw/resource/enus/full-spectrum.html
- document_id: `labview-sound-and-vibration-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Full spectrum is the spectrum of an orbit. The amplitude of the full spectrum indicates the vibration level at each frequency/order. The relative amplitude between the forward and reverse components indicates the orbit eccentricity and the direction of precession. Forward precession is precession in

Full Spectrum

Full spectrum is the spectrum of an orbit. The amplitude of the full spectrum
 indicates the vibration level at each frequency/order.

Note

Figure 53.

[IMAGE alt='1378' src='GUID-9D5F22CD-B99E-4CEA-BC1A-D719FAAC8AC3-a5.png']

While absolute probe orientation is required to accurately compute orbit
 plots, the full spectrum depends only on the measured vibration
 and the relative angle between the paired sensor
 measurements.

Parent topic:

Averaged Order Spectra

<!--NI_TOPIC bundle=labview-sound-and-vibration-toolkit path=gabor-transform.html language=enus -->
## TOPIC 00058: Gabor Transform

- bundle_id: `labview-sound-and-vibration-toolkit`
- source_path: `gabor-transform.html`
- source_url: https://docs-be.ni.com/bundle/labview-sound-and-vibration-toolkit/raw/resource/enus/gabor-transform.html
- document_id: `labview-sound-and-vibration-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Like Short-Time Fourier Transform (STFT) analysis, the Gabor transform can help you identify the order components in the time-frequency domain when the speed is variable.The Gabor transform is a special type of time-frequency analysis called an invertible joint time-frequency transform. With inverti

Gabor Transform

Like Short-Time Fourier Transform (STFT) analysis, the Gabor transform can help you
 identify the order components in the time-frequency domain when the speed is
 variable.

The Gabor transform is a special type of time-frequency analysis called an invertible joint
 time-frequency transform. With invertible joint time-frequency transforms, you can
 recover any time-domain input signal or an approximation of the signal by applying an
 inverse transform to the transform of the signal. The inverse Gabor transform is known
 as the Gabor expansion. You can recover the time-domain signal from a Gabor transform by
 using the Gabor expansion, but you cannot recover the time-domain signal from general
 STFT analysis. The results of the Gabor transform are Gabor coefficients.

The ability to recover time-domain signals is a feature of Gabor transforms and Gabor expansions.
 Gabor transforms and expansions enable you to extract signal
 components related to rotational speed from the Gabor
 coefficients, or from the time-frequency representation. With
 the Gabor technique, you can extract the signal components
 associated with any particular orders.

Parent topic:

Order-Domain Analysis Methods

Related concepts:

- FFT, DFT, and Zoom

<!--NI_TOPIC bundle=labview-sound-and-vibration-toolkit path=gain.html language=enus -->
## TOPIC 00059: Gain

- bundle_id: `labview-sound-and-vibration-toolkit`
- source_path: `gain.html`
- source_url: https://docs-be.ni.com/bundle/labview-sound-and-vibration-toolkit/raw/resource/enus/gain.html
- document_id: `labview-sound-and-vibration-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: A gain measurement measures the amplification between the amplitude of the identified tone in the input signal and the reference amplitude.The accuracy of gain measurement depends on the absolute amplitude accuracies of the output channel and the input channel. For example, when you generate and acq

Gain

A gain measurement measures the amplification between the amplitude of the identified
 tone in the input signal and the reference amplitude.

The accuracy of gain measurement depends on the absolute amplitude accuracies of the output
 channel and the input channel. For example, when you generate and acquire the signal
 with an NI PXI-4461, the expected measurement uncertainty is less than 0.3 dB.

A gain distortion occurs when the output amplitude is not a linear function of the input
 amplitude at an identified frequency. You must identify the
 expected fundamental frequency and the amplitude of the stimulus
 tone regardless of whether you are using the output of the
 acquisition device or an external source.

Parent topic:

Channel Characterization

<!--NI_TOPIC bundle=labview-sound-and-vibration-toolkit path=gap-reference-calibration.html language=enus -->
## TOPIC 00060: Gap Reference Calibration

- bundle_id: `labview-sound-and-vibration-toolkit`
- source_path: `gap-reference-calibration.html`
- source_url: https://docs-be.ni.com/bundle/labview-sound-and-vibration-toolkit/raw/resource/enus/gap-reference-calibration.html
- document_id: `labview-sound-and-vibration-toolkit`
- page_type: `leaf`
- content_type: `task`
- source_description: You must compensate for DC gap offset when you compute the centerline plot of shafts. This compensation requires another type of reference signal, called DC gap reference. The DC gap reference contains the DC values of the probe when the shaft is at rest. Complete the following steps to perform shaf

Gap Reference Calibration

You must compensate for DC gap offset when you compute the centerline plot of
 shafts. This compensation requires another type of reference signal, called DC gap
 reference. The DC gap reference contains the DC values of the probe when the shaft
 is at rest.

Complete the following steps to perform shaft centerline position
 compensation.

1. Measure the DC gap voltage values of the proximity probes when the shaft is at rest.
2. Subtract the at-rest DC gap voltage values from the DC voltages measured during normal operation
 and combine the results to form the shaft centerline plot.

Parent topic:

System Calibration

<!--NI_TOPIC bundle=labview-sound-and-vibration-toolkit path=group-delay.html language=enus -->
## TOPIC 00061: Group Delay

- bundle_id: `labview-sound-and-vibration-toolkit`
- source_path: `group-delay.html`
- source_url: https://docs-be.ni.com/bundle/labview-sound-and-vibration-toolkit/raw/resource/enus/group-delay.html
- document_id: `labview-sound-and-vibration-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Group delay is often used as a criterion to evaluate the phase nonlinearity of a filter. The following equation defines the group delay: GD ( f ) = − 1 2 π d d f phase ( f ) where phase(f) is the phase response. If the phase response is linear, the group delay of the filter is constant, which means

Group Delay

Group delay is often used as a criterion to evaluate the phase nonlinearity of a
 filter.

The following equation defines the group delay:

GD

(

f

)

=

−

1

2

π

d

d

f

phase

(

f

)

where phase(f) is the phase response.

If the phase response is linear, the group delay of the filter is constant, which means
 each frequency component experiences the same delay. Otherwise, the frequency components
 have different delays, which cause the smearing phenomenon of the time-domain
 signal.

The following figure compares the effects of a Kaiser FIR lowpass filter and an Elliptic
 lowpass filter on the same input signal.

Figure 78.

[IMAGE alt='1378' src='GUID-3E896928-EF83-4878-A921-7E11B04AECF9-a5.png']

The first waveform, which is the input signal, is a periodic sinc pattern with an order
 of 12.

The second waveform shows the effects of a Kaiser FIR lowpass filter on the input signal.
 The Kaiser filter has a linear phase response, so the filter delays the input without
 distorting the signal. The waveform is similar to the input signal, except for the delay
 and the attenuation.

The third waveform shows the effects of an Elliptic lowpass filter on the input signal.
 The phase response of the Elliptic filter is nonlinear, so the frequency components
 experience different delays. Thus, the shape of the waveform is different from the input
 signal.

Parent topic:

Channel Characterization

<!--NI_TOPIC bundle=labview-sound-and-vibration-toolkit path=human-response.html language=enus -->
## TOPIC 00062: Human Response

- bundle_id: `labview-sound-and-vibration-toolkit`
- source_path: `human-response.html`
- source_url: https://docs-be.ni.com/bundle/labview-sound-and-vibration-toolkit/raw/resource/enus/human-response.html
- document_id: `labview-sound-and-vibration-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Human vibration weighting standards are incorporated into the NI Sound and Vibration Measurement Suite to mitigate the health risks associated with certain frequencies and vibrations.Such standards are crucial because such stimuli heavily influence the sensitivity of the ear and the tactile percepti

Human Response

Human vibration weighting standards are incorporated into the NI Sound and Vibration
 Measurement Suite to mitigate the health risks associated with certain frequencies and
 vibrations.

Such standards are crucial because such stimuli heavily influence the sensitivity of the ear and
 the tactile perception of the body, directly impacting our comfort, productivity, and
 overall well-being.

- [Perception of Sound](perception-of-sound.html) Human hearing relies on the ability of the ear and the neural system to sense and process variations in sound pressure.
- [Effects of Vibration](effects-of-vibration.html) Human vibration refers to the effects of mechanical vibration on the human body. Excessive exposure to mechanical vibrations can negatively affect the human body.

<!--NI_TOPIC bundle=labview-sound-and-vibration-toolkit path=human-vibration-weighting-filters.html language=enus -->
## TOPIC 00063: Human Vibration Weighting Filters

- bundle_id: `labview-sound-and-vibration-toolkit`
- source_path: `human-vibration-weighting-filters.html`
- source_url: https://docs-be.ni.com/bundle/labview-sound-and-vibration-toolkit/raw/resource/enus/human-vibration-weighting-filters.html
- document_id: `labview-sound-and-vibration-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI Sound and Vibration Measurement Suite provides weighting filters that you can apply to human vibration signals. Applying weighting to human vibration signals can isolate the directional components that you are interested in and help you further analyze different types of human vibration.The S

Human Vibration Weighting Filters

The NI Sound and Vibration Measurement Suite provides weighting filters that you can
 apply to human vibration signals. Applying weighting to human vibration signals can isolate the
 directional components that you are interested in and help you further analyze different types
 of human vibration.

The Sound and Vibration Measurement Suite provides the following weighting filters that you can
 apply to human vibration signals:

- W 
 b —Weighting for vertical whole-body vibration,
 z-axis, seated, standing or recumbent person, based
 on ISO 2631-4.
- W 
 c —Weighting for horizontal whole-body
 vibration, x-axis, seat back, seated person, based
 on ISO 2631-1.
- W 
 d —Weighting for horizontal whole-body
 vibration, x- or y-axis, seated, standing or
 recumbent person, based on ISO 2631-1.
- W 
 e —Weighting for rotational whole-body
 vibration, all directions, seated person, based on
 ISO 2631-1.
- W 
 f —Weighting for vertical whole-body vibration,
 z-axis motion sickness, seated or standing person,
 based on ISO 2631-1.
- W 
 h —Weighting for hand-arm vibration, all
 directions, based on ISO 5349-1.
- W 
 j —Weighting for vertical head vibration, x-axis
 recumbent person, based on ISO 2631-1.
- W 
 k —Weighting for vertical whole-body vibration,
 z-axis seated, standing or recumbent person, based
 on ISO 2631-1.
- W 
 m —Weighting for whole-body vibration in buildings, all directions, based on ISO
 2631-2.

Use the W<sub>h</sub> weighting filter for hand-arm
 vibration signals. Use the W<sub>b</sub>,
 W<sub>c</sub>,
 W<sub>d</sub>,
 W<sub>e</sub>,
 W<sub>j</sub>,
 W<sub>k</sub>, and
 W<sub>m</sub> weighting filters for whole-body
 vibration signals. Use the W<sub>f</sub> weighting
 filter for low-frequency whole-body vibration signals.

Parent topic:

Weighting Filters

<!--NI_TOPIC bundle=labview-sound-and-vibration-toolkit path=human-vibration-weighting-standards.html language=enus -->
## TOPIC 00064: Human Vibration Weighting Standards

- bundle_id: `labview-sound-and-vibration-toolkit`
- source_path: `human-vibration-weighting-standards.html`
- source_url: https://docs-be.ni.com/bundle/labview-sound-and-vibration-toolkit/raw/resource/enus/human-vibration-weighting-standards.html
- document_id: `labview-sound-and-vibration-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Human vibration weighting filters in the NI Sound and Vibration Measurement Suite comply with industry standards to properly assess human response to vibration.The human vibration weighting filters in the NI Sound and Vibration Measurement Suite comply to the following standards: ISO 8041:2005 (E):

Human Vibration Weighting Standards

Human vibration weighting filters in the NI Sound and Vibration Measurement
 Suite comply with industry standards to properly assess human response to
 vibration.

The human vibration weighting filters in the NI Sound and Vibration Measurement Suite comply to
 the following standards:

- ISO 8041:2005 (E): Human Response to Vibration – Measuring Instrumentation
- JIS B 7760:2004: Whole-Body Vibration
- JIS B 7761:2004: Hand-Transmitted Vibration

Parent topic:

Human Vibration Weighting Filters

<!--NI_TOPIC bundle=labview-sound-and-vibration-toolkit path=idle-channel-noise.html language=enus -->
## TOPIC 00065: Idle-Channel Noise

- bundle_id: `labview-sound-and-vibration-toolkit`
- source_path: `idle-channel-noise.html`
- source_url: https://docs-be.ni.com/bundle/labview-sound-and-vibration-toolkit/raw/resource/enus/idle-channel-noise.html
- document_id: `labview-sound-and-vibration-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Idle-channel noise is noise present in a communications channel when no signals are applied. The NI Sound and Vibration Measurement Suite measures the total power, the median noise density level, the maximum spur, and the signal-to-noise ratio (SNR) within the specified frequency range on waveform d

Idle-Channel Noise

Idle-channel noise is noise present in a communications channel when no
 signals are applied.

The NI Sound and Vibration Measurement Suite measures the total power,
 the median noise density level, the maximum spur, and the
 signal-to-noise ratio (SNR) within the specified frequency range
 on waveform data or the complex spectrum returned by the other
 audio measurements.

For practical purposes, the returned idle-channel noise is a power-in-band measurement that
 returns the aggregate noise energy in the specified frequency
 range. The Sound and Vibration Measurement Suite computes the
 SNR as the full-scale level divided by the idle-channel
 noise.

The median noise level is normalized by the bin width, df, and is one measurement of the noise
 floor, or noise density level. You might find noise floor
 knowledge useful in advanced measurements.

Note

Parent topic:

Channel Characterization

<!--NI_TOPIC bundle=labview-sound-and-vibration-toolkit path=implementing-integration.html language=enus -->
## TOPIC 00066: Implementing Integration

- bundle_id: `labview-sound-and-vibration-toolkit`
- source_path: `implementing-integration.html`
- source_url: https://docs-be.ni.com/bundle/labview-sound-and-vibration-toolkit/raw/resource/enus/implementing-integration.html
- document_id: `labview-sound-and-vibration-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: If you need to perform measurements on velocity or displacement data when you have only acquired acceleration or velocity data, respectively, integrate the measured signal to yield the desired data.You can perform integration either in the time domain as a form of signal conditioning or in the frequ

Implementing Integration

If you need to perform measurements on velocity or displacement data when you
 have only acquired acceleration or velocity data, respectively, integrate
 the measured signal to yield the desired data.

You can perform integration either in the time domain as a form of signal conditioning or in the
 frequency domain as a stage of analysis. When performed in the
 frequency domain, integration is one of the extended
 measurements for frequency analysis.

Converting acceleration data to velocity or displacement data presents a pair of unique
 challenges. Measured signals typically contain some unwanted DC components. The second
 challenge is the fact that many transducers, especially vibration transducers, have
 lower-frequency limits. A transducer cannot accurately measure frequency components below
 the lower-frequency limit of the transducer.

- DC Component—Even though a DC component in the measured signal might be valid, the presence of a
 DC component indicates that the device under test (DUT) has a net acceleration along the
 axis of the transducer. For a typical vibration measurement, the DUT is mounted or
 suspended in the test setup. The net acceleration of the DUT is zero. Therefore, any DC
 component in the measured acceleration is an artifact and must be ignored.
- Transducers—Most acceleration and velocity transducers are not designed to accurately measure
 frequency components close to DC. Closeness to DC is relative and depends on the
 specific transducer. A typical accelerometer can accurately measure components down to
 about 10 Hz. A typical velocity probe can accurately measure components down to 2–3 Hz.
 Inaccurately measured low-frequency vibrations can dominate the response when the signal
 is integrated because integration attenuates low-frequency components less than
 high-frequency components.

Parent topic:

Integration

Related concepts:

- Frequency-Domain Analysis
- Vibration

<!--NI_TOPIC bundle=labview-sound-and-vibration-toolkit path=integration.html language=enus -->
## TOPIC 00067: Integration

- bundle_id: `labview-sound-and-vibration-toolkit`
- source_path: `integration.html`
- source_url: https://docs-be.ni.com/bundle/labview-sound-and-vibration-toolkit/raw/resource/enus/integration.html
- document_id: `labview-sound-and-vibration-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Integration is the conversion of acceleration data to velocity or displacement data. This section describes the integration process, including basic theory and implementation in the time and frequency domains. The conversion between acceleration, velocity, and displacement is based on one of the fun

Integration

Integration is the conversion of acceleration data to velocity or displacement data.
 This section describes the integration process, including basic theory and implementation in the
 time and frequency domains.

The conversion between acceleration, velocity, and displacement is based
 on one of the fundamental laws in Newtonian physics, represented
 by the following equations:

x

=

d

d

t

(

x

)

x

=

d

d

t

(

x

)

=

d

2

d

t

2

(

x

)

Velocity is the first derivative of displacement with respect to time.
 Acceleration is the first derivative of velocity and the second
 derivative of displacement with respect to time. Therefore,
 given acceleration, perform a single integration with respect to
 time to compute the velocity or perform a double integration
 with respect to time to compute the displacement.

When representing the acceleration of a point by a simple sinusoid, the
 velocity and the displacement of the point are represented by
 the following equations:

a = Asin(ω
 t)

v

=

−

A

ω

cos

⁡

(

ω

⁢

t

)

=

A

ω

sin

(

ω

⁢

t

⁢

−

π

2

)

d

=

−

A

ω

2

sin

(

ω

⁢

t

)

=

A

ω

2

sin

(

ω

⁢

t

⁢

−

π

)

Note

The amplitude of the velocity is inversely proportional to the frequency
 of the vibration. The amplitude of the displacement is inversely
 proportional to the square of the frequency of the vibration.
 Furthermore, the phase of the velocity lags the acceleration by
 90°. The phase of the displacement lags the acceleration by
 180°. The following figure illustrates the relationship between
 acceleration, velocity, and displacement for a 0.5 Hz
 sinusoid.

Figure 14.

[IMAGE alt='1378' src='GUID-06D42584-A680-4154-AE73-5952D37A887E-a5.gif']

Note that for this low frequency sine wave, the amplitude of the
 displacement is attenuated nearly by a factor of 10. This
 follows from the 1/w^2 term in the equation above. For higher
 frequencies, the attenuation is more pronounced. For instance,
 double integration attenuates a 1000 Hz sinusoid by a factor of
 3.95E7. Significant attenuation can necessitate converting units
 during integration. For example, conversion allows 1 g
 vibrations to be displayed as .248 micron instead of 2.48E-7
 m.

Common units for velocity are:

- mm/s (read 'millimeters per second')
- in/s = ips (read 'inches per second')

Common units for displacement are

- micron (1e-6 m; read 'microns')
- mil (1e-3 in; read 'mils')

The integration of a sinusoid is known in closed form. Integration of an
 arbitrary waveform typically requires a numerical approach. You
 can use several numerical integration schemes to evaluate an
 integral in the time domain.

In the frequency domain, you can define any arbitrary band-limited
 waveform as a sum of sinusoids. Because the amplitude and phase
 relationships are known for sinusoids, you can carry out the
 integration in the frequency domain.

- [Implementing Integration](implementing-integration.html) If you need to perform measurements on velocity or displacement data when you have only acquired acceleration or velocity data, respectively, integrate the measured signal to yield the desired data.
- [Time-Domain Integration](time-domain-integration.html) Time-domain integration is a technique used to determine displacement and velocity from acceleration data. You can use integration to convert acceleration data to displacement data in a single-shot acquisition and integration.
- [Frequency-Domain Integration](frequency-domain-integration.html) Frequency-domain integration is used to separate and analyze the different frequency components which make up measured signals.

Parent topic:

Waveform Conditioning

<!--NI_TOPIC bundle=labview-sound-and-vibration-toolkit path=intermodulation-distortion-standards.html language=enus -->
## TOPIC 00068: Intermodulation Distortion Standards

- bundle_id: `labview-sound-and-vibration-toolkit`
- source_path: `intermodulation-distortion-standards.html`
- source_url: https://docs-be.ni.com/bundle/labview-sound-and-vibration-toolkit/raw/resource/enus/intermodulation-distortion-standards.html
- document_id: `labview-sound-and-vibration-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Several standards define IMD measurements. These standards are best used depending on the type of intermodulation distortion you are trying to capture or similar.The following table lists two standards and their associated test signals and typical use cases. IMD Standard Test Signals and Typical Use

Intermodulation Distortion Standards

Several standards define IMD measurements. These standards are best used depending on
 the type of intermodulation distortion you are trying to capture or similar.

The following table lists two standards and their associated test signals and typical use
 cases.

| IMD Standard | Test Signal (f1, f2, ratio) | Typical Use Cases |
| --- | --- | --- |
| SMPTE/DIN | (60, 7000, 4) (250, 8000, 4) others | Excite low-frequency distortion mechanisms such as thermal distortion in power amplifiers; disk recording and film |
| ITU-R (CCIF) | (11000, 12000, 1) (14000, 15000, 1) (19000, 20000, 1) others | ADC and DAC slope-induced distortion |

f

1

f

2

Note

Parent topic:

Distortion

<!--NI_TOPIC bundle=labview-sound-and-vibration-toolkit path=intermodulation-distortion.html language=enus -->
## TOPIC 00069: Intermodulation Distortion

- bundle_id: `labview-sound-and-vibration-toolkit`
- source_path: `intermodulation-distortion.html`
- source_url: https://docs-be.ni.com/bundle/labview-sound-and-vibration-toolkit/raw/resource/enus/intermodulation-distortion.html
- document_id: `labview-sound-and-vibration-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Intermodulation distortion (IMD) is the measurement of distortion due to nonlinearity in the device under test (DUT). IMD measurements use a dual-tone test signal composed of a low-frequency tone at f[1] and a high-frequency tone at f[2]. When a dual-tone signal is the input to a nonlinear device, t

Intermodulation Distortion

Intermodulation distortion (IMD) is the measurement of distortion due to
 nonlinearity in the device under test (DUT). IMD measurements use a
 dual-tone test signal composed of a low-frequency tone at
 f<sub>1</sub> and a high-frequency tone at
 f<sub>2</sub>.

When a dual-tone signal is the input to a nonlinear device, the device
 output contains intermodulation components of
 f<sub>1</sub> and
 f<sub>2</sub> given by
 m*f<sub>2</sub>
 ± n*f<sub>1</sub>, where
 m and n are
 integers.

You often use IMD to measure the distortion of a DUT near the
 high-frequency limit of the DUT or the measurement system. You
 also can arrange the test so that many IMD components occur
 within the measurement bandwidth.

Several standard configurations for IMD measurements exist, and these
 configurations use one of two types of IMD test signals.

In the first type of IMD test signal, with a low-frequency modulation
 tone and a high-frequency carrier tone, the intermodulation
 components appear as sidebands around the high-frequency carrier
 tone, as calculated in the following equation:

f
 <sub>2</sub> ± n *
 f<sub>1</sub>

The following figure shows the sidebands around the 8 kHz carrier
 tone.

Figure 73.

[IMAGE alt='1378' src='GUID-EBFA3D4F-76CB-4443-B484-DDB7F37A64BB-a5.png']

In the second type of IMD test signal, with two closely spaced tones
 near the high-frequency limit of the measurement bandwidth, the
 intermodulation components appear at multiples of the difference
 frequency calculated by the following equation:

m * (f<sub>2</sub> -
 f<sub>1</sub>)

The following figure shows a typical IMD test spectrum.

Figure 74.

[IMAGE alt='1378' src='GUID-126A3587-C966-47A2-8B56-A425E4AFD8C2-a5.png']

[IMAGE alt='1378' src='GUID-126A3587-C966-47A2-8B56-A425E4AFD8C2-a5.png']

The intermodulation components are found at multiples of 1,000 Hz, the
 difference frequency between the twin 11 kHz and 12 kHz
 tones.

Parent topic:

Distortion

<!--NI_TOPIC bundle=labview-sound-and-vibration-toolkit path=level-measurements.html language=enus -->
## TOPIC 00070: Level Measurements

- bundle_id: `labview-sound-and-vibration-toolkit`
- source_path: `level-measurements.html`
- source_url: https://docs-be.ni.com/bundle/labview-sound-and-vibration-toolkit/raw/resource/enus/level-measurements.html
- document_id: `labview-sound-and-vibration-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: A level measurement provides a quantitative description of the overall vibration acquired from a transducer. You can perform sound level and vibration level measurements with time-domain or even-angle signals.A level measurement is a common measurement technique for performing sound and vibration an

Level Measurements

A level measurement provides a quantitative description of the overall vibration
 acquired from a transducer. You can perform sound level and vibration level measurements
 with time-domain or even-angle signals.

A level measurement is a common measurement technique for performing sound and vibration
 analysis.

Use the NI Sound and Vibration Measurement Suite to develop and configure the following sound
 level measurements:

- L eq
- Running L eq
- Peak
- Exponential average

You can combine different sound level measurements and use them simultaneously to provide
 flexibility with acoustic measurements.

Use the Sound and Vibration Measurement Suite to develop and configure the following vibration
 level measurements:

- [RMS and Leq](rms-and-leq.html) The vibration level of the signal that a sensor returns is expressed in root mean square acceleration (g rms ). L eq is the RMS sound level with the measurement duration used as the averaging time. Calculating these provides a concise representation of fluctuating noise levels.
- [Peak Hold](peak-hold.html) Peak-hold averaging captures the highest measured value during the averaging period.
- [Max-Min](max-min.html) Max-Min averaging not only computes the largest measured vibration pressure level value of all previous values until a new value exceeds the current maximum value, but also computes the minimum level of all previous values.
- [Crest Factor](crest-factor.html) The relative phases of the constituent tones with respect to each other determine the crest factor of a multitone signal with specified amplitude. The crest factor is the ratio of the peak magnitude to the RMS value of the signal.

Parent topic:

Time-Domain Analysis

<!--NI_TOPIC bundle=labview-sound-and-vibration-toolkit path=limit-testing-in-digital-filter-design.html language=enus -->
## TOPIC 00071: Limit Testing in Digital Filter Design

- bundle_id: `labview-sound-and-vibration-toolkit`
- source_path: `limit-testing-in-digital-filter-design.html`
- source_url: https://docs-be.ni.com/bundle/labview-sound-and-vibration-toolkit/raw/resource/enus/limit-testing-in-digital-filter-design.html
- document_id: `labview-sound-and-vibration-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use limit testing in the area of digital filter design. You might want to design lowpass filters with a passband ripple of 10 dB and stopband attenuation of 60 dB. You can use limit testing to make sure the frequency response of the filter always meets these specifications. The first step in

Limit Testing in Digital Filter Design

You can use limit testing in the area of digital filter design.

You might want to design lowpass filters with a passband ripple of 10 dB and stopband
 attenuation of 60 dB. You can use limit testing to make sure the frequency response of
 the filter always meets these specifications. The first step in this process is to
 specify the limits. You can specify a lower limit of -10 dB in the passband region and
 an upper limit of -60 dB in the stopband region, as shown in the following figure. After
 you specify these limits, you can run the actual test repeatedly to make sure that all
 the frequency responses of all the filters are designed to meet these
 specifications.

Figure 87.

[IMAGE alt='1378' src='GUID-3946E8C0-AEC5-43E1-A725-3160803F1154-a5.png']

Parent topic:

Applications of Limit Testing

<!--NI_TOPIC bundle=labview-sound-and-vibration-toolkit path=limit-testing-in-modem-manufacturing.html language=enus -->
## TOPIC 00072: Limit Testing in Modem Manufacturing

- bundle_id: `labview-sound-and-vibration-toolkit`
- source_path: `limit-testing-in-modem-manufacturing.html`
- source_url: https://docs-be.ni.com/bundle/labview-sound-and-vibration-toolkit/raw/resource/enus/limit-testing-in-modem-manufacturing.html
- document_id: `labview-sound-and-vibration-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Limit testing is used in modem manufacturing to make sure the transmit spectrum of the line signal meets the V.34 modem specification. The following figure shows how limit testing is used to check if a signal meets specifications: Limit Testing as Used for the Transmit Spectrum of a Line Signal The

Limit Testing in Modem Manufacturing

Limit testing is used in modem manufacturing to make sure the transmit spectrum of
 the line signal meets the V.34 modem specification.

The following figure shows how limit testing is used to check if a signal meets
 specifications:

Figure 86.

[IMAGE alt='1378' src='GUID-8A88DA1C-63A5-441A-979E-25C5F599F888-a5.png']

The ITU-T V.34 recommendation contains specifications for a modem operating at data
 signaling rates up to 33,600 bits/s. It specifies that the spectrum for the line signal
 that transmits data conforms to the template shown in the previous figure. For example,
 for a normalized frequency of 1.0, the spectrum must always lie between 3 dB and 1 dB.
 All the modems must meet this specification. A modem manufacturer can set up an
 automated test system to monitor the transmit spectrum for the signals that the modem
 outputs. If the spectrum conforms to the specification, the modem passes the test and is
 ready for customer use. Recommendations such as the ITU-T V.34 are essential to ensure
 interoperability between modems from different manufacturers and to provide high-quality
 service to customers.

Parent topic:

Applications of Limit Testing

<!--NI_TOPIC bundle=labview-sound-and-vibration-toolkit path=limit-testing-in-pulse-mask-testing.html language=enus -->
## TOPIC 00073: Limit Testing in Pulse Mask Testing

- bundle_id: `labview-sound-and-vibration-toolkit`
- source_path: `limit-testing-in-pulse-mask-testing.html`
- source_url: https://docs-be.ni.com/bundle/labview-sound-and-vibration-toolkit/raw/resource/enus/limit-testing-in-pulse-mask-testing.html
- document_id: `labview-sound-and-vibration-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: T1 signals must lie in the mask specified by the upper and lower limit. These limits are set to properly enable the interconnection of digital network components to form a digital path or connection. The ITU-T G.703 recommendation specifies the pulse mask for signals with bit rates, n × 64, where n

Limit Testing in Pulse Mask Testing

T1 signals must lie in the mask specified by the upper and lower limit. These
 limits are set to properly enable the interconnection of digital network
 components to form a digital path or connection.

The ITU-T G.703 recommendation specifies the pulse mask for signals with
 bit rates, n × 64, where n
 is between 2 and 31. The following figure shows the pulse mask
 for interface at 1,544 kbits/s. Signals with this bit rate also
 are referred to as T1 signals.

Figure 88.

[IMAGE alt='1378' src='GUID-DFFE6BF1-8121-42FD-A86F-057635849524-a5.png']

Parent topic:

Applications of Limit Testing

<!--NI_TOPIC bundle=labview-sound-and-vibration-toolkit path=limit-testing.html language=enus -->
## TOPIC 00074: Limit Testing

- bundle_id: `labview-sound-and-vibration-toolkit`
- source_path: `limit-testing.html`
- source_url: https://docs-be.ni.com/bundle/labview-sound-and-vibration-toolkit/raw/resource/enus/limit-testing.html
- document_id: `labview-sound-and-vibration-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use limit testing to monitor a waveform and determine if it always satisfies a set of conditions, usually upper and lower limits.The region bounded by the specified limits is a mask. The result of a limit or mask test is generally a pass or fail. Limits are classified into two types—continuo

Limit Testing

You can use limit testing to monitor a waveform and determine if it always
 satisfies a set of conditions, usually upper and lower limits.

The region bounded by the specified limits is a mask. The result of a limit or mask test is
 generally a pass or fail. Limits are classified into two types—continuous
 limits and segmented limits.

You can use the same method to create and control many different automated test systems.
 Complete the following basic steps to set up an automated test
 system for limit testing.

1. Configure the measurement by specifying arbitrary upper and lower limits. This defines the mask
 or region of interest.
2. Acquire data using a DAQ device.
3. Monitor the data to make sure it always falls within the specified mask.
4. Log the pass/fail results from step 3 to a file or visually inspect the input data and the
 points that fall outside the mask.
5. Repeat steps 2 through 4 to continue limit testing.

Refer to the following sections for more information.

- [Specify a Limit](specifying-a-limit.html) Limits are specified as either continuous or segmented.
- [Specify a Limit Using a Formula](specifying-a-limit-using-a-formula.html) You can specify limits using formulas. Such limits are best classified as segmented limits.
- [Performing Limit Testing](performing-limit-testing.html) To perform limit testing, you define a mask, acquire the signal using a DAQ device, then compare the signal with the limit.
- [Applications of Limit Testing](applications-of-limit-testing.html) You can use limit testing in a wide range of test and measurement applications. including modem manufacturing, digital filter design, and pulse mask testing.
- [Supported Data Types for Limit Testing](supported-data-types-for-limit-testing.html) The NI Sound and Vibration Measurement Suite supports a range of different data types including: waveform measurement, frequency spectrum measurement, XY data, peak measurement, and scalar measurement.

<!--NI_TOPIC bundle=labview-sound-and-vibration-toolkit path=limits-of-hearing.html language=enus -->
## TOPIC 00075: Limits of Hearing

- bundle_id: `labview-sound-and-vibration-toolkit`
- source_path: `limits-of-hearing.html`
- source_url: https://docs-be.ni.com/bundle/labview-sound-and-vibration-toolkit/raw/resource/enus/limits-of-hearing.html
- document_id: `labview-sound-and-vibration-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The ear is a very sophisticated auditory organ and can be thought of as a complex instrument for auditory signals. However, there remain frequencies and pressures that we cannot detect. Human hearing can detect small variations in air pressure, ranging from 10 µPa up to 100 Pa. The detection of thes

Limits of Hearing

The ear is a very sophisticated auditory organ and can be thought of as a
 complex instrument for auditory signals. However, there remain frequencies
 and pressures that we cannot detect.

Human hearing can detect small variations in air pressure, ranging from
 10 µPa up to 100 Pa. The detection of these small variations
 occurs in the presence of atmospheric pressure, where 1 atm =
 101.3 kPa. Furthermore, humans perceive loudness on a
 logarithmic scale. The international standard reference for
 sound pressure level measurements is 20 µPa (0 dB), which is the
 threshold of quiet. This is considered the nominal threshold of
 hearing, although approximately half of the general population
 can sense sounds at even lower levels. On the opposite end of
 sound pressure level measurements, humans experience discomfort
 and pain from sounds with sound pressure levels greater than 100
 Pa (134 dB). Within this range in level, humans can typically
 discern changes as small as 1 dB.

Human hearing can detect frequencies between 20 Hz and 20 kHz. Frequency
 components outside this range are not generally considered to
 impact the human perception of sound, regardless of the sound
 pressure level. As explained in the previous section, there are
 physical reasons why human hearing is most sensitive to
 frequency components around 1 kHz and 4 kHz. Many studies have
 demonstrated the sensitivity of the ear as a function of
 frequency, which is typically plotted in equal loudness curves
 as in the following figure.

Figure 60.

[IMAGE alt='1378' src='GUID-FA4146F6-C0AA-480F-B1FA-97D0115291B3-a5.gif']

Besides the sound pressure level-dependent sensitivity of hearing, humans
 also can distinguish very fine changes in frequency. Below
 frequencies of 500 Hz, the ear can differentiate tone bursts
 with a frequency difference of approximately 1 Hz. Above 500 Hz,
 the barely-noticeable distinction is proportional to the
 frequency (0.002 x f ).

Parent topic:

Perception of Sound

<!--NI_TOPIC bundle=labview-sound-and-vibration-toolkit path=linear-averaging.html language=enus -->
## TOPIC 00076: Linear Averaging

- bundle_id: `labview-sound-and-vibration-toolkit`
- source_path: `linear-averaging.html`
- source_url: https://docs-be.ni.com/bundle/labview-sound-and-vibration-toolkit/raw/resource/enus/linear-averaging.html
- document_id: `labview-sound-and-vibration-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: In linear averaging, every input sample contributes equally to the measurement result.

Linear Averaging

In linear averaging, every input sample contributes equally to the measurement
 result.

- [Single-Shot Averaging](single-shot-averaging.html) Single-shot averaging allows you to average a single set of measurements obtained over a specified duration.
- [Block-by-Block Averaging](block-by-block-averaging.html) Some applications require you to perform level measurements continuously using a specific integration time. Typically, this specific integration time is the block duration time, whose result is cumulative only from the beginning of each block.
- [Continuous Averaging](continuous-averaging.html) Continuous linear averaging can process small chunks of data, keep track of the intermediate results, and integrate the measurement over time, allowing you to perform level measurements over a longer period of time than other linear averaging methods.
- [Running Window Averaging](running-window.html) Running RMS level, or L eq , is the root mean square (RMS) value computed over the last N seconds, or the integration time. The single-shot, continuous, and block-by-block linear averaging are three special cases of running RMS level or L eq .

Parent topic:

Time Averaging

<!--NI_TOPIC bundle=labview-sound-and-vibration-toolkit path=linear-units-eu.html language=enus -->
## TOPIC 00077: Linear Units (EU)

- bundle_id: `labview-sound-and-vibration-toolkit`
- source_path: `linear-units-eu.html`
- source_url: https://docs-be.ni.com/bundle/labview-sound-and-vibration-toolkit/raw/resource/enus/linear-units-eu.html
- document_id: `labview-sound-and-vibration-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Linear units are necessary for accurately depicting time-domain signals, allowing for precise analysis of signal characteristics.Use linear units to see the overall characteristic and dominant components of a time-domain signal, a level measurement versus time, a frequency spectrum, or an order spec

Linear Units (EU)

Linear units are necessary for accurately depicting time-domain signals, allowing
 for precise analysis of signal characteristics.

Use linear units to see the overall characteristic and dominant components of a time-domain
 signal, a level measurement versus time, a frequency spectrum, or an order spectrum.

Parent topic:

Scale Signals to Engineering Units

<!--NI_TOPIC bundle=labview-sound-and-vibration-toolkit path=linear.html language=enus -->
## TOPIC 00078: Linear

- bundle_id: `labview-sound-and-vibration-toolkit`
- source_path: `linear.html`
- source_url: https://docs-be.ni.com/bundle/labview-sound-and-vibration-toolkit/raw/resource/enus/linear.html
- document_id: `labview-sound-and-vibration-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Linear averaging calculates an average set of values that reduces the signal, noise, and background vibration.Linear averaging is computed by integrating the square of the filtered signal over a fixed time interval and dividing by the time interval. Linear averaging starts when the lowest fractional

Linear

Linear averaging calculates an average set of values that reduces the signal, noise,
 and background vibration.

Linear averaging is computed by integrating the square of the filtered signal over a fixed time
 interval and dividing by the time interval. Linear averaging
 starts when the lowest fractional-octave filter settles.

Parent topic:

Fractional-Octave Averaging

<!--NI_TOPIC bundle=labview-sound-and-vibration-toolkit path=masking.html language=enus -->
## TOPIC 00079: Masking

- bundle_id: `labview-sound-and-vibration-toolkit`
- source_path: `masking.html`
- source_url: https://docs-be.ni.com/bundle/labview-sound-and-vibration-toolkit/raw/resource/enus/masking.html
- document_id: `labview-sound-and-vibration-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Masking describes the phenomenon in which a sound becomes imperceptible due to the presence of another sound, such as loud music masking the sound of emergency sirens or background noise partially masking conversational speech.The transition between an unmasked tone and a completely masked tone is c

Masking

Masking describes the phenomenon in which a sound becomes imperceptible due to the
 presence of another sound, such as loud music masking the sound of emergency sirens or
 background noise partially masking conversational speech.

The transition between an unmasked tone and a completely masked tone is continuous. The masked
 threshold is the sound pressure level of a barely-audible test tone in the presence of a
 masking sound.

- [Time Masking](time-masking.html) Masking can occur between sounds that are not present simultaneously. Non-simultaneous masking is also known as time masking, and can occur as pre- or post-masking on a test tone.
- [Frequency Masking](frequency-masking.html) It is common for background noise to mask your test signal. When this is the case, filters are necessary to remove the masking noise.

Parent topic:

Perception of Sound

<!--NI_TOPIC bundle=labview-sound-and-vibration-toolkit path=max-min.html language=enus -->
## TOPIC 00080: Max-Min

- bundle_id: `labview-sound-and-vibration-toolkit`
- source_path: `max-min.html`
- source_url: https://docs-be.ni.com/bundle/labview-sound-and-vibration-toolkit/raw/resource/enus/max-min.html
- document_id: `labview-sound-and-vibration-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Max-Min averaging not only computes the largest measured vibration pressure level value of all previous values until a new value exceeds the current maximum value, but also computes the minimum level of all previous values.Max-Min averaging actually is not a true form of averaging because successive

Max-Min

Max-Min averaging not only computes the largest measured vibration pressure level
 value of all previous values until a new value exceeds the current maximum value, but also
 computes the minimum level of all previous values.

Max-Min averaging actually is not a true form of averaging because successive measurements are
 not mathematically averaged. However, Max-Min averaging can combine the results of
 several measurements into two final measurements.

Parent topic:

Level Measurements

<!--NI_TOPIC bundle=labview-sound-and-vibration-toolkit path=measurement-types-and-transducers.html language=enus -->
## TOPIC 00081: Measurement Types and Transducers

- bundle_id: `labview-sound-and-vibration-toolkit`
- source_path: `measurement-types-and-transducers.html`
- source_url: https://docs-be.ni.com/bundle/labview-sound-and-vibration-toolkit/raw/resource/enus/measurement-types-and-transducers.html
- document_id: `labview-sound-and-vibration-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: This section describes the measurement types you use in sound and vibration analysis, as well as the transducers for obtaining appropriate signals. Three common signal types for sound and vibration analysis are sound pressure, vibration, and rotational speed signals. The characteristic difference am

Measurement Types and Transducers

This section describes the measurement types you use in sound and vibration analysis,
 as well as the transducers for obtaining appropriate signals.

Three common signal types for sound and vibration analysis are sound pressure, vibration, and
 rotational speed signals. The characteristic difference among these types of dynamic
 signals is the propagation medium or how the dynamic response is coupled to the
 environment.

- [Sound Pressure](sound-pressure.html) Sound pressure consists of dynamic pressure variations that travel through air or water. The most common sound transducer is the microphone.
- [Vibration](vibration.html) Vibration is the movement about an equilibrium position of a machine or component. Vibration travels through mechanical couplings such as components, fasteners, and suspension systems.
- [Rotational Speed](rotational-speed.html) NI Sound and Vibration Measurement Suite supports three different types of tachometers for measuring rotational speed: proximity probes, optical transducers, and encoders.

Parent topic:

Dynamic Signals

<!--NI_TOPIC bundle=labview-sound-and-vibration-toolkit path=measuring-a-shock-response-spectrum.html language=enus -->
## TOPIC 00082: Shock Response Spectrum Measurements

- bundle_id: `labview-sound-and-vibration-toolkit`
- source_path: `measuring-a-shock-response-spectrum.html`
- source_url: https://docs-be.ni.com/bundle/labview-sound-and-vibration-toolkit/raw/resource/enus/measuring-a-shock-response-spectrum.html
- document_id: `labview-sound-and-vibration-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the shock response spectrum (SRS) to characterize a dynamic mechanical environment and to estimate the damage potential of a specific shock to a component. The following figure shows a single-degree-of-freedom (SDOF) mechanical system. Single-Degree-of-Freedom Mechanical System An SDOF mechanica

Shock Response Spectrum Measurements

Use the shock response spectrum (SRS) to characterize a dynamic mechanical environment
 and to estimate the damage potential of a specific shock to a component.

The following figure shows a single-degree-of-freedom (SDOF) mechanical system.

Figure 43.

[IMAGE alt='1378' src='GUID-B88E564E-E5F0-4BB9-98F9-88CB95686FAF-a5.gif']

An SDOF mechanical system consists of the following components:

- Mass, whose value is represented with the variable m
- Spring, whose stiffness is represented with the variable k
- Damper, whose damping coefficient is represented with the variable
 c

x represents the motion of the base and y represents
 the motion of the mass.

The input to the SDOF system is the base acceleration
 ẍ(t). The response of the SDOF system is the absolute
 acceleration of the mass ÿ(t). SRS measurements often use
 this absolute acceleration model. The following equation represents the transfer function in
 the Laplace domain for the SDOF system:

H

(

s

)

=

n

s

2

ζ

ω

+

n

2

ω

s

2

+

2

ζ

ω

n

s

+

ω

n

2

Another common model for SRS measurements is the relative displacement model. You use the
 relative displacement model when the damage potential is correlated with relative displacement
 between the component and the base. The relative displacement model uses an additional
 coordinate z, where z(t) =
 y(t) - x(t). Use
 the following equation to calculate the transfer function.

H

(

s

)

=

1

s

2

+

2

ζ

ω

n

s

+

ω

n

2

To keep the stimulus signal and response signal in the same physical units, you also can
 represent the relative displacement in terms of the equivalent static acceleration, as defined
 in the following equation:

Y

¨

e

q

=

z

ω

n

2

You then calculate the transfer function using the following equation:

H

(

s

)

=

ω

n

2

s

2

+

2

ζ

ω

n

s

+

ω

n

2

The resonance frequency, f<sub>n</sub>, and the critical damping factor,
 ζ, characterize an SDOF system, where

f

n

=

2

x

ω

n

=

1

2

x

k

m

ζ

=

c

2

k

m

For light damping where ζ is less than or equal to 0.05, the peak value of the frequency
 response occurs in the immediate vicinity of f<sub>n</sub> and is given by
 the following equation, where Q is the resonant gain:

Q

∼

1

2

ζ

=

k

m

c

Obtain SRS by applying the acquired shock pulse to a series of SDOF mechanical systems. Plot
 the system maximum response as a function of the resonance frequency of the system.

The following figure illustrates the response of an SDOF system to a half-sine pulse with a
 10 g acceleration amplitude and 10 ms duration.

Figure 44.

[IMAGE alt='1378' src='GUID-C70D2CB9-5C9B-468E-9F32-DB3D530E8F7B-a5.gif']

The top graph shows the time-domain acceleration. The middle graph is the SDOF system
 response with a 50 Hz resonance frequency. The bottom graph is the SDOF system response with a
 150 Hz resonance frequency. In both cases, ζ is 0.05.

Use the signals shown in the previous figure to construct the SRS. For example, the maximax,
 the absolute maximum response of the calculated shock response signal over the entire signal
 duration, uses the absolute maximum system response as a function of the system natural
 frequency. The following figure illustrates the maximax SRS for the same half-sine pulse.

Figure 45.

[IMAGE alt='1378' src='GUID-FF0077F7-FEBF-4DDF-8CC7-02A33B26D2C0-a5.gif']

Note

You can use other types of shock spectra depending on the application. These spectra include
 the initial shock response from the system response over the pulse duration or from the
 residual shock spectrum of the system response after the pulse. You can use the positive
 maximum, the negative maximum, or the absolute maximum response signal value. The following
 figure shows different types of SRS measurements.

Figure 46.

[IMAGE alt='1378' src='GUID-3A530268-EC2D-4E96-BC80-05D5E59756EF-a5.gif']

Parent topic:

Transient Analysis

<!--NI_TOPIC bundle=labview-sound-and-vibration-toolkit path=new-features-and-changes.html language=enus -->
## TOPIC 00083: LabVIEW Sound and Vibration Toolkit New Features and Changes

- bundle_id: `labview-sound-and-vibration-toolkit`
- source_path: `new-features-and-changes.html`
- source_url: https://docs-be.ni.com/bundle/labview-sound-and-vibration-toolkit/raw/resource/enus/new-features-and-changes.html
- document_id: `labview-sound-and-vibration-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Learn about updates—including new features and behavior changes—introduced in each version of LabVIEW Sound and Vibration Toolkit. Discover what's new in the latest releases of LabVIEW Sound and Vibration Toolkit.If you cannot find new features and changes for your version, it may not include user-f

LabVIEW Sound and Vibration
 Toolkit
 New Features and Changes

Learn about updates—including new features and behavior changes—introduced in each
 version of LabVIEW Sound and Vibration
 Toolkit.

LabVIEW Sound and Vibration
 Toolkit

Note

Release Notes

Related information:

- Software and Driver Downloads

#### LabVIEW Sound and Vibration Toolkit 2023 Q3
 Changes

Learn about new features, behavior changes, and other updates in LabVIEW Sound and
 Vibration Toolkit 2023 Q3.

##### New
 Features

- Added support for LabVIEW 2022 Q3 and later.
- Added support for LabVIEW RT Module 2022 Q3 64-bit and later.

#### LabVIEW Sound and Vibration Toolkit 21.5
 Changes

Learn about new features, behavior changes, and other updates in LabVIEW Sound and
 Vibration Toolkit 21.5.

##### New
 Features

- Support for LabVIEW 2021 does not remove previously installed support for LabVIEW 2020
 and earlier.
- Improved memory and speed performance of SV Aures Tonality and SV Aures Roughness
 VIs.
- Enhanced Sample Projects:
  - Dynamic Signal Generator (DSG) refactored for scalability
  - Audio Analyzer refactored for readability
  - Impact Test refactored for speed performance

#### LabVIEW Sound and Vibration Toolkit 20.0.0
 Changes

Learn about new features, behavior changes, and other updates in LabVIEW Sound and
 Vibration Toolkit 20.0.0.

##### New
 Features

- Support for LabVIEW 2020 does not remove previously installed support for LabVIEW 2019
 and earlier.
- Support for different sample rates between input and output during stimulus-response
 measurements.
  - Fully synchronized stimulus-response measurements can now be performed while
 running analog input and analog output at different rates. DAQmx AI devices such as
 the 4464 can be run at full rate of 204.8 kHz while DAQmx AO devices such as the
 4463 can be run at full rate of 51.2 kHz. This allows for the measurement of
 harmonic components outside the bandwidth of the AO device.
- Enhanced Examples and Sample Projects:
  - Simplified examples to improve function and readability.
  - Refactored Impact Test sample project to modularize functionality and improve
 readability. Use the new LabVIEW TDMS File Viewer to review saved impacts.
  - Simplified DSA and DSG sample projects to improve readability and
 performance.

#### LabVIEW Sound and Vibration Toolkit 19.0.0
 Changes

Learn about new features, behavior changes, and other updates in
 <PRODUCT><VERSION>.

##### New
 Features

- Support for LabVIEW 2019 does not remove previously installed support for LabVIEW 2018
 and earlier.
- Support for Gabor Analyses on Linux real-time targets.
  - Runtime support on Linux targets is supported for online and offline
 analyses.
- Enhanced Examples for Audio Test:
  - Stimulus-Response Examples use channel wires to communicate data from DAQmx Engine
 to Measurement-Analysis Loop.
  - Synchronization pulse automatically correlated to align channels with different
 signal path delays.

<!--NI_TOPIC bundle=labview-sound-and-vibration-toolkit path=octave-analysis-standards.html language=enus -->
## TOPIC 00084: Octave Analysis Standards

- bundle_id: `labview-sound-and-vibration-toolkit`
- source_path: `octave-analysis-standards.html`
- source_url: https://docs-be.ni.com/bundle/labview-sound-and-vibration-toolkit/raw/resource/enus/octave-analysis-standards.html
- document_id: `labview-sound-and-vibration-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: This topic contains information about the ANSI, IEC, and JIS standards regarding midband frequencies, the nominal frequencies returned by the octave analysis tools in the NI Sound and Vibration Measurement Suite, and compliance with ANSI, IEC, and JIS standards by the octave analysis tools. The octa

Octave Analysis Standards

This topic contains information about the ANSI, IEC, and JIS standards regarding
 midband frequencies, the nominal frequencies returned by the octave analysis tools in the NI
 Sound and Vibration Measurement Suite, and compliance with ANSI, IEC, and JIS standards by the
 octave analysis tools.

Note

According to the IEC 61260:2014 and the ANSI S1.11-2014 standards, the exact mid-band
 frequencies, f<sub>m</sub>, of any filter in
 a set of filters shall be determined from the following
 expression:

f<sub>m</sub> =
 f<sub>r</sub>G<sup>x/b</sup>,
 when b is odd

f<sub>m</sub> =
 f<sub>r</sub>G<sup>(2x
 + 1)/2b</sup>, when
 b is even

where f<sub>r</sub> is the reference frequency,

G = 10<sup>0.3</sup> is the octave frequency ratio,

1/b is the bandwidth designator, and equals 1 for octave, 1/3 for 1/3 octave,
 1/6 for 1/6 octave, 1/12 for 1/12 octave, and 1/24 for 1/24
 octave,

x is any integer, positive or negative, or
 zero.

The exact midband frequencies are used to design the filters for fractional-octave analysis.
 However, all the octave analysis tools in the Sound and
 Vibration Measurement Suite return the nominal midband
 frequencies, also called the preferred frequencies. In the case
 of octave and 1/3 octave analyses, the nominal frequencies are
 calculated in accordance with the ANSI and IEC standards. In the
 case of 1/6, 1/12, and 1/24 octave analyses, the nominal
 frequencies are calculated in accordance with the Annex E
 (informative) of the IEC 61260:2014 and the ANSI S1.11-2014
 standards.

When combined with any National Instruments DSA device, the appropriate microphone, and proper
 signal conditioning, the filters produced by the octave analysis
 tools in the Sound and Vibration Measurement Suite comply with
 the following standards:

- ANSI S1.11-2014: Electroacoustics - Octave-band and fractional-octave-band filters, class 1
- IEC 61260:2014: Electroacoustics - Octave-band and fractional-octave-band filters, class 1
- JIS C 1514:2002: Electroacoustics - Octave-band and fractional-octave-band filters, class 1

For octave filters, choose a sampling frequency at least three times the exact center frequency
 of the highest frequency band. For fractional-octave filters,
 choose a sampling frequency at least 2.5 times the exact center
 frequency of the highest frequency band.

Parent topic:

Fractional-Octave Analysis

<!--NI_TOPIC bundle=labview-sound-and-vibration-toolkit path=octave-filters.html language=enus -->
## TOPIC 00085: Octave Filters

- bundle_id: `labview-sound-and-vibration-toolkit`
- source_path: `octave-filters.html`
- source_url: https://docs-be.ni.com/bundle/labview-sound-and-vibration-toolkit/raw/resource/enus/octave-filters.html
- document_id: `labview-sound-and-vibration-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: An octave filter is a filter whose passband covers one octave. An octave is the interval between two frequencies where one frequency is twice the rate of the other. For example, frequencies of 250 Hz and 500 Hz are one octave apart, as are frequencies of 1 kHz and 2 kHz. The following illustration s

Octave Filters

An octave filter is a filter whose passband covers one octave. An octave is the
 interval between two frequencies where one frequency is twice the rate of the other.

For example, frequencies of 250 Hz and 500 Hz are one octave apart, as are frequencies of 1
 kHz and 2 kHz. The following illustration shows an octave filter, a filter whose passband
 covers one octave.

Figure 31.

[IMAGE alt='1378' src='GUID-7CB58507-49A8-48E1-9035-E94ACD09AA6E-a5.gif']

Just as a tuning fork provides a 440 Hz reference frequency for musicians, a reference
 frequency is needed to fully define octave filters. Instrumentation equipment typically uses a
 1 kHz reference frequency.

Parent topic:

Fractional-Octave Filtering

<!--NI_TOPIC bundle=labview-sound-and-vibration-toolkit path=order-domain-analysis-functions.html language=enus -->
## TOPIC 00086: Order-Domain Analysis Functions

- bundle_id: `labview-sound-and-vibration-toolkit`
- source_path: `order-domain-analysis-functions.html`
- source_url: https://docs-be.ni.com/bundle/labview-sound-and-vibration-toolkit/raw/resource/enus/order-domain-analysis-functions.html
- document_id: `labview-sound-and-vibration-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: This section describes order-domain analysis functions that you can use to present sound and vibration information and improve your knowledge of a device under test.Refer to the following sections for more information.

Order-Domain Analysis Functions

This section describes order-domain analysis functions that you can use to present
 sound and vibration information and improve your knowledge of a device under
 test.

Refer to the following sections for more information.

- [Averaged Order Spectra](averaged-order-spectra.html) An averaged spectrum displays steady-state vibration components while reducing noise. An order spectrum provides a view of all order components of a signal and can help you find significant orders and compare the level of different order components.
- [Spectral Map](spectral-map.html) A spectral map is a three-dimensional display of sound or vibration spectra as a function of time or speed. The spectra can be frequency or order spectra.
- [Order Tracking](order-tracking.html) You can perform order tracking by computing the order magnitude and phase from an even-angle signal. You also can compute the magnitude and phase of a specific order from the order waveform.
- [Order Waveform Extraction](order-waveform-extraction.html) An order waveform is the time signal associated with a certain order, which is synchronous to the rotational speed. Unlike an order power spectrum, which provides information for all of the orders of a certain time block signal, an order waveform provides information only for one particular order relative to time.

Parent topic:

Order-Domain Analysis

<!--NI_TOPIC bundle=labview-sound-and-vibration-toolkit path=order-domain-analysis-methods.html language=enus -->
## TOPIC 00087: Order-Domain Analysis Methods

- bundle_id: `labview-sound-and-vibration-toolkit`
- source_path: `order-domain-analysis-methods.html`
- source_url: https://docs-be.ni.com/bundle/labview-sound-and-vibration-toolkit/raw/resource/enus/order-domain-analysis-methods.html
- document_id: `labview-sound-and-vibration-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The order analysis tools in the NI Sound and Vibration Measurement Suite provide two methods for performing order analysis: the Gabor transform method and the resampling method.

Order-Domain Analysis Methods

The order analysis tools in the NI Sound and Vibration Measurement Suite provide two
 methods for performing order analysis: the Gabor transform method and the resampling
 method.

- [Gabor Transform](gabor-transform.html) Like Short-Time Fourier Transform (STFT) analysis, the Gabor transform can help you identify the order components in the time-frequency domain when the speed is variable.
- [Resampling](resampling.html) The NI Sound and Vibration Measurement Suite provides order analysis tools for software resampling that can circumvent the challenges of hardware implementation.

Parent topic:

Order-Domain Analysis

<!--NI_TOPIC bundle=labview-sound-and-vibration-toolkit path=order-domain-analysis.html language=enus -->
## TOPIC 00088: Order-Domain Analysis

- bundle_id: `labview-sound-and-vibration-toolkit`
- source_path: `order-domain-analysis.html`
- source_url: https://docs-be.ni.com/bundle/labview-sound-and-vibration-toolkit/raw/resource/enus/order-domain-analysis.html
- document_id: `labview-sound-and-vibration-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Order analysis is a technique for analyzing sound and vibration signals from rotating or reciprocating machinery, such as engines, compressors, turbines, and pumps.These machines have a variety of parts, and each part contributes unique sound and vibration patterns to the sound and vibration pattern

Order-Domain Analysis

Order analysis is a technique for analyzing sound and vibration signals from rotating
 or reciprocating machinery, such as engines, compressors, turbines, and pumps.

These machines have a variety of parts, and each part contributes unique sound and vibration
 patterns to the sound and vibration pattern of the whole machine. With order analysis,
 you can identify and isolate these sound and vibration patterns to analyze the
 performance and quality of each machine part individually.

- [FFT Analysis Versus Order Analysis](comparing-fft-analysis-and-order-analysis.html) You can use an FFT power spectrum to identify and quantify the frequency components of a sound or vibration signal. However, changes in rotational speed can cause these frequency components to overlap, preventing you from identifying individual components. Order analysis solves this issue by monitoring the harmonics that result from these same rotational speed changes.
- [Rotational Speed Measurements](rotational-speed-measurements.html) The NI Sound and Vibration Measurement Suite supports rotational speed measurements from signals generated from digital tachometers, analog tachometers, as well as simulated tachometers.
- [Order-Domain Analysis Methods](order-domain-analysis-methods.html) The order analysis tools in the NI Sound and Vibration Measurement Suite provide two methods for performing order analysis: the Gabor transform method and the resampling method.
- [Order-Domain Analysis Functions](order-domain-analysis-functions.html) This section describes order-domain analysis functions that you can use to present sound and vibration information and improve your knowledge of a device under test.

<!--NI_TOPIC bundle=labview-sound-and-vibration-toolkit path=order-power-spectrum.html language=enus -->
## TOPIC 00089: Order Power Spectrum

- bundle_id: `labview-sound-and-vibration-toolkit`
- source_path: `order-power-spectrum.html`
- source_url: https://docs-be.ni.com/bundle/labview-sound-and-vibration-toolkit/raw/resource/enus/order-power-spectrum.html
- document_id: `labview-sound-and-vibration-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: An order power spectrum provides a quantitative description of the amplitude or power of the orders in a signal. Order power spectrum is also called the half spectrum—magnitudes are calculated from a single sensor rather than a sensor pair. When analyzing machinery sound and vibration, you typically

Order Power Spectrum

An order power spectrum provides a quantitative description of the amplitude or power
 of the orders in a signal.

Order power spectrum is also called the half spectrum—magnitudes are calculated from a
 single sensor rather than a sensor pair.

When analyzing machinery sound and vibration, you typically compute an order power
 spectrum after displaying the spectral map. After you identify a certain block of a
 signal as the signal of interest on the spectral map, you can compute an order power
 spectrum on this signal block to get more detailed order information. You can identify
 the characteristic order components, form a quantitative spectrum measurement of the
 orders, and compare the amplitudes of different orders. The following figure shows a
 typical order power spectrum for a gearbox.

Figure 52.

[IMAGE alt='1378' src='GUID-30CD9599-4C4E-4AFB-8034-623C941E834A-a5.gif']

You can identify the significant orders, like the 48th and 72nd orders, measure the
 amplitude of the orders, and compare different orders in this plot.

Parent topic:

Averaged Order Spectra

Related concepts:

- Spectral Map

<!--NI_TOPIC bundle=labview-sound-and-vibration-toolkit path=order-tracking.html language=enus -->
## TOPIC 00090: Order Tracking

- bundle_id: `labview-sound-and-vibration-toolkit`
- source_path: `order-tracking.html`
- source_url: https://docs-be.ni.com/bundle/labview-sound-and-vibration-toolkit/raw/resource/enus/order-tracking.html
- document_id: `labview-sound-and-vibration-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can perform order tracking by computing the order magnitude and phase from an even-angle signal. You also can compute the magnitude and phase of a specific order from the order waveform.Unlike an order power spectrum, which provides information for all of the orders of a certain time block signa

Order Tracking

You can perform order tracking by computing the order magnitude and phase from an
 even-angle signal. You also can compute the magnitude and phase of a specific order from the
 order waveform.

Unlike an order power spectrum, which provides information for all of the orders of a certain
 time block signal, the magnitude and phase provide information only for one particular
 order relative to time. Order magnitude and phase also can provide order information
 relative to speed when you perform a run-up or run-down test. Thus, order magnitude and
 phase can help you analyze sound or vibration signals by focusing on specific
 orders.

Use a spectral map or order power spectrum to identify the most significant orders in a sound or
 vibration signal. After identifying the most significant orders,
 you can extract an order waveform or its magnitude and phase to
 get detailed information for individual orders.

Many mechanical faults are associated with certain orders. Analyzing order magnitude and phase
 can help you detect mechanical faults directly. For example, a
 strong first order magnitude indicates imbalance of a machine in
 most cases. Analyzing the first order magnitude can help you
 identify the source of the imbalance. Moreover, the magnitude
 and phase of the first order can help you correct the imbalance
 when you add weights on the appropriate rotor positions.

Parent topic:

Order-Domain Analysis Functions

Related concepts:

- Spectral Map
- Order Power Spectrum

<!--NI_TOPIC bundle=labview-sound-and-vibration-toolkit path=order-waveform-extraction.html language=enus -->
## TOPIC 00091: Order Waveform Extraction

- bundle_id: `labview-sound-and-vibration-toolkit`
- source_path: `order-waveform-extraction.html`
- source_url: https://docs-be.ni.com/bundle/labview-sound-and-vibration-toolkit/raw/resource/enus/order-waveform-extraction.html
- document_id: `labview-sound-and-vibration-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: An order waveform is the time signal associated with a certain order, which is synchronous to the rotational speed. Unlike an order power spectrum, which provides information for all of the orders of a certain time block signal, an order waveform provides information only for one particular order re

Order Waveform Extraction

An order waveform is the time signal associated with a certain order, which is
 synchronous to the rotational speed. Unlike an order power spectrum, which provides
 information for all of the orders of a certain time block signal, an order waveform provides
 information only for one particular order relative to time.

Use a spectral map or order power spectrum to identify the most significant orders in a
 sound or vibration signal. After identifying the most significant orders, you can
 extract an order waveform to get detailed information for individual orders.

You can extract order waveforms to isolate specific orders from a sound or vibration
 signal. The following figure shows a waveform signal and an extracted order
 waveform.

Figure 57.

[IMAGE alt='1378' src='GUID-05DE2387-60CC-4C14-9F17-F8D622DB9E1D-a5.gif']

You can see the contribution of the fourth order to the overall waveform signal. You also
 can calculate the running root-mean-square (RMS) value of a certain order from the order
 waveform. You then can use the running RMS value to indicate the amplitude of a certain
 order.

One feature of order waveform extraction is the ability to play back a time signal.
 Playing back a time signal enables you to listen to the sound of a certain order or a
 combination of orders. This feature is useful for applications where a microphone
 acquires the signal. You can use order waveforms to perform noise analysis and to locate
 a noise source by comparing the noises that different orders or order combinations
 generate. The most common applications of this feature are in sound quality engineering.
 You can analyze and synthesize the sound of several orders and evaluate the subjective
 perception of these sounds. In automotive noise, vibration, and harshness tests, one
 example of sound quality engineering is the evaluation of power train components, like
 the engine, to obtain a more comfortable noise level for passengers.

Parent topic:

Order-Domain Analysis Functions

Related concepts:

- Order Power Spectrum
- Spectral Map

<!--NI_TOPIC bundle=labview-sound-and-vibration-toolkit path=peak-hold-averaging.html language=enus -->
## TOPIC 00092: Peak Hold Averaging

- bundle_id: `labview-sound-and-vibration-toolkit`
- source_path: `peak-hold-averaging.html`
- source_url: https://docs-be.ni.com/bundle/labview-sound-and-vibration-toolkit/raw/resource/enus/peak-hold-averaging.html
- document_id: `labview-sound-and-vibration-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: A peak hold averaging measurement is performed at each individual frequency line and retains the RMS peak levels of the averaged quantities from one FFT record to the next record. Peak-hold averaging is most useful when configuring a measurement system or when applying limit or upper limit testing t

Peak Hold Averaging

A peak hold averaging measurement is performed at each individual frequency line and
 retains the RMS peak levels of the averaged quantities from one FFT record to the next
 record.

Peak-hold averaging is most useful when configuring a measurement system
 or when applying limit or upper limit testing to a frequency spectrum.

Peak-hold averaged measurements are computed according to the following
 equations:

FFT spectrum

M

A

X

X

*

⋅

X

power spectrum

M

A

X

(

X

*

⋅

X

)

where

X is the complex FFT of the stimulus signal
 x.

X

Note

Parent topic:

Averaging Modes

<!--NI_TOPIC bundle=labview-sound-and-vibration-toolkit path=peak-hold-fractional-octave-averaging.html language=enus -->
## TOPIC 00093: Peak Hold Fractional-Octave Averaging

- bundle_id: `labview-sound-and-vibration-toolkit`
- source_path: `peak-hold-fractional-octave-averaging.html`
- source_url: https://docs-be.ni.com/bundle/labview-sound-and-vibration-toolkit/raw/resource/enus/peak-hold-fractional-octave-averaging.html
- document_id: `labview-sound-and-vibration-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: In peak-hold averaging, the largest measured level value of all previous values is returned for each band until a new value exceeds the current maximum. Because the maximum value is determined by the highest spectral value recorded during the averaging time and remains as the maximum value until a n

Peak Hold Fractional-Octave Averaging

In peak-hold averaging, the largest measured level value of all previous values is
 returned for each band until a new value exceeds the current maximum.

Because the maximum value is determined by the highest spectral value recorded during the
 averaging time and remains as the maximum value until a new returned value exceeds it,
 peak hold is technically not a true averaging process.

Parent topic:

Fractional-Octave Averaging

<!--NI_TOPIC bundle=labview-sound-and-vibration-toolkit path=peak-hold-spectrum-sound-and-vibration.html language=enus -->
## TOPIC 00094: Peak Hold (Spectrum)

- bundle_id: `labview-sound-and-vibration-toolkit`
- source_path: `peak-hold-spectrum-sound-and-vibration.html`
- source_url: https://docs-be.ni.com/bundle/labview-sound-and-vibration-toolkit/raw/resource/enus/peak-hold-spectrum-sound-and-vibration.html
- document_id: `labview-sound-and-vibration-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Peak hold averaging is performed at each individual order and retains the RMS peak levels of the averaged quantities from one FFT spectrum to the next. Peak hold averaging is most useful when configuring a measurement system or when applying a limit to an order spectrum. The NI Sound and Vibration M

Peak Hold (Spectrum)

Peak hold averaging is performed at each individual order and retains the RMS peak
 levels of the averaged quantities from one FFT spectrum to the next.

Peak hold averaging is most useful when configuring a measurement system
 or when applying a limit to an order spectrum. The NI Sound and Vibration Measurement Suite
 computes peak hold averaging for order power spectra according to the following equation:

M

A

X

(

X

*

⋅

X

)

where X is the complex FFT of the even-angle signal
 X, and X<sup>*</sup> is the complex conjugate of
 X.

Parent topic:

Spectrum Averaging

<!--NI_TOPIC bundle=labview-sound-and-vibration-toolkit path=peak-hold.html language=enus -->
## TOPIC 00095: Peak Hold

- bundle_id: `labview-sound-and-vibration-toolkit`
- source_path: `peak-hold.html`
- source_url: https://docs-be.ni.com/bundle/labview-sound-and-vibration-toolkit/raw/resource/enus/peak-hold.html
- document_id: `labview-sound-and-vibration-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Peak-hold averaging captures the highest measured value during the averaging period.In peak-hold averaging, the largest measured sound pressure level value of all previous values is computed and returned until a new value exceeds the current maximum. The new value becomes the new maximum value and i

Peak Hold

Peak-hold averaging captures the highest measured value during the averaging
 period.

In peak-hold averaging, the largest measured sound pressure level value of all previous values is
 computed and returned until a new value exceeds the current
 maximum. The new value becomes the new maximum value and is the
 value returned until a new value exceeds it. Peak hold actually
 is not a true form of averaging because successive measurements
 are not mathematically averaged. However, as with other
 averaging processes, peak-hold averaging combines the results of
 several measurements into one final measurement. As with
 exponential averaging, the averaging process continues
 indefinitely. The formula for peak averaging is defined by the
 following equation.

y[k] = max(y[k‑1],
 x[k])

where

x[k] is the new measurement.

y[k] is the new average.

y[k – 1] is the previous average.

Parent topic:

Level Measurements

<!--NI_TOPIC bundle=labview-sound-and-vibration-toolkit path=perception-of-sound.html language=enus -->
## TOPIC 00096: Perception of Sound

- bundle_id: `labview-sound-and-vibration-toolkit`
- source_path: `perception-of-sound.html`
- source_url: https://docs-be.ni.com/bundle/labview-sound-and-vibration-toolkit/raw/resource/enus/perception-of-sound.html
- document_id: `labview-sound-and-vibration-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Human hearing relies on the ability of the ear and the neural system to sense and process variations in sound pressure.Accordingly, the act of hearing has both subconscious and conscious effects. Subconscious effects, such as hearing loss, are due to prolonged exposure to high sound pressure levels.

Perception of Sound

Human hearing relies on the ability of the ear and the neural system to sense and
 process variations in sound pressure.

Accordingly, the act of hearing has both subconscious and conscious effects. Subconscious
 effects, such as hearing loss, are due to prolonged exposure to high sound pressure
 levels. Conscious effects are a direct result of the ears' acute response to a sound and
 how the cognitive part of the brain evaluates the sound. An example of an acute response
 to a sound is the pain and resultant ringing felt in the ear when a whistle is blown
 close to the ear in an enclosed environment. An example of utilizing conscious response
 is using sound to convey information to consumers, such as designing a product to emit
 sounds that indicate operation and/or status. Psychoacoustics is the field of study that
 seeks to better understand our perception of sound by investigating its conscious
 effects.

For speech and music, the verbal content conveys much of the information. Furthermore, for
 speech, music, and many other sounds, the physical
 characteristics of the sound produce hearing sensations in the
 listener. The table below lists three primary physical
 characteristics of sound and their corresponding hearing
 sensations.

| Physical Characteristics | Hearing Sensation |
| --- | --- |
| Sound pressure level | Loudness |
| Frequency | Pitch |
| Duration | Subjective duration |

These three hearing sensations directly correlate with their corresponding physical
 characteristic. However, human hearing is a complex system and
 many sensations do not correlate directly to just one physical
 characteristic. For example, in the table above, the sensation
 of pitch is also dependent on the sound pressure level.

Much of the challenge in the field of psychoacoustics stems from the fact that different
 listeners perceive identical sounds differently. Age, gender,
 nationality, and many other diversity factors affect human
 perception. In addition to this challenge of a heterogeneous
 population, consumer expectations vary based on the different
 types of products they purchase. For example, a customer expects
 different sound characteristics from motorcycles, dishwashers,
 and personal computers. Therefore, sound quality evaluations are
 usually specific to the type of product and the target
 consumer.

There are three basic components to a sound quality program: calibrated recording, listening
 evaluations, and preference models. The audio recording and the
 playback must not have any distortion and must be calibrated to
 the sound pressure level. The goal of sound quality measurement
 is to develop the preference model, or the basis for future
 evaluation of sounds.

Because hearing is one of the integral processes through which humans receive information and
 because the sound of a product carries so much information,
 there is significant, ongoing research to classify hearing
 sensations and correlate these sensations to physical
 characteristics of the signal. Through ongoing investigation,
 researchers continue to identify physical characteristics of
 interest and propose improved objective sound quality metrics
 that correlate better to human perception.

- [Physiology of Human Hearing](physiology-of-human-hearing.html) Scientists typically divide the human ear into three main regions: the outer ear, the middle ear, and the inner ear.
- [Limits of Hearing](limits-of-hearing.html) The ear is a very sophisticated auditory organ and can be thought of as a complex instrument for auditory signals. However, there remain frequencies and pressures that we cannot detect.
- [Equal Loudness](equal-loudness.html) Loudness is a subjective indicator of the perceived noise level expressed in phons. The loudness level in phons is the sound pressure level in decibels of a 1 kHz tone having the same perceived loudness as the tone being evaluated.
- [Masking](masking.html) Masking describes the phenomenon in which a sound becomes imperceptible due to the presence of another sound, such as loud music masking the sound of emergency sirens or background noise partially masking conversational speech.

Parent topic:

Human Response

<!--NI_TOPIC bundle=labview-sound-and-vibration-toolkit path=performing-an-stft-versus-time.html language=enus -->
## TOPIC 00097: Performing an STFT versus Time

- bundle_id: `labview-sound-and-vibration-toolkit`
- source_path: `performing-an-stft-versus-time.html`
- source_url: https://docs-be.ni.com/bundle/labview-sound-and-vibration-toolkit/raw/resource/enus/performing-an-stft-versus-time.html
- document_id: `labview-sound-and-vibration-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Short-Time Fourier Transform (STFT) in the NI Sound and Vibration Measurement Suite computes multiple Fourier transforms on a time-domain signal with or without overlapping. For example, suppose you analyze a waveform containing 10 s of data acquired at 51.2 kS/s. The signal is a chirp signal wi

Performing an STFT versus Time

The Short-Time Fourier Transform (STFT) in the NI Sound and Vibration Measurement
 Suite computes multiple Fourier transforms on a time-domain signal with or without
 overlapping.

For example, suppose you analyze a waveform containing 10 s of data acquired at 51.2
 kS/s. The signal is a chirp signal with the following attributes:

- Start frequency = 10 Hz
- End frequency = 10,000 Hz

The following figure shows the signal corresponding to the first 200 ms of the
 waveform.

Figure 37.

[IMAGE alt='1378' src='GUID-C7AA081A-1F59-4DD3-B625-EFB0B9870B22-a5.gif']

The following figure shows the result of applying a baseband Fast Fourier Transform (FFT)
 on the entire waveform.

Figure 38.

[IMAGE alt='1378' src='GUID-030DDE14-8CA8-4CF9-93C5-4BD8802A8D1E-a5.gif']

Note

The spectrum is flat from 10 Hz to 10 kHz. Only noise is measured at frequencies above 10
 kHz. This measurement does not provide any information about how the frequency content
 of the signal changes with time. However, the STFT can reveal useful information about
 the time dependence of the frequency content.

Instead of computing a single FFT on the whole data set, you can divide the data set into
 smaller blocks and compute FFTs on these smaller data blocks. For example, divide the
 signal into 100 ms blocks and perform an FFT on each of the blocks.

In addition to the time segment, you can adjust the FFT block size. For example, analyze
 a chirp signal with the following attributes:

- Start frequency = 10 Hz
- End frequency = 10,000 Hz

The measurement is performed using the following settings:

- Acquisition time = 10 s
- Sampling frequency = 51.2 kS/s
- FFT block size = 1,024 samples, or 512 lines (400 alias-free lines)
- Time increment= 100 ms

Based on the sampling frequency of 51,200 Hz, a 1,024 sample FFT requires a 20 ms block
 of data, leading to a frequency resolution of 50 Hz.

Because the time increment is 100 ms and a 1,024 sample FFT requires only a 20 ms block,
 only one block out of five is used for computation. The following figure shows the
 result obtained with a 1,024 sample FFT.

Figure 39.

[IMAGE alt='1378' src='GUID-34D0F765-3F7A-4A98-B799-83C1B10ACC5E-a5.gif']

If you select an FFT block size of 4,096 samples, or 1,600 alias-free lines, the
 resolution improves, as illustrated in the following figure.

Figure 40.

[IMAGE alt='1378' src='GUID-CEF87B68-6389-4D39-8623-6AE7BCA1790B-a5.gif']

However, the increased resolution comes with the expense of extra processing.

Overlapping is a method that uses a percentage of the previous data block to compute the
 FFT of the current data block. When combined with windowing, overlapping maximizes the
 use of the entire data set. If no overlapping is used, the part of the signal close to
 the window edges becomes greatly attenuated. The attenuation of the signal near the
 window edges might result in the loss of information in the region near the window
 edges.

The following figure shows a 50% overlapping process.

Figure 41.

[IMAGE alt='1378' src='GUID-D7C4BE6B-A5D8-43FD-8CC7-047542D86B3D-a5.gif']

The following figure shows the resulting subdivisions when you use a 50% overlap and a
 Hamming window.

Figure 42.

[IMAGE alt='1378' src='GUID-32C3C739-5E66-4635-B993-70020F92C760-a5.gif']

Parent topic:

Transient Analysis

Related concepts:

- FFT, DFT, and Zoom

<!--NI_TOPIC bundle=labview-sound-and-vibration-toolkit path=performing-limit-testing.html language=enus -->
## TOPIC 00098: Performing Limit Testing

- bundle_id: `labview-sound-and-vibration-toolkit`
- source_path: `performing-limit-testing.html`
- source_url: https://docs-be.ni.com/bundle/labview-sound-and-vibration-toolkit/raw/resource/enus/performing-limit-testing.html
- document_id: `labview-sound-and-vibration-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: To perform limit testing, you define a mask, acquire the signal using a DAQ device, then compare the signal with the limit. After you define the mask, you acquire a signal using a DAQ device. The sample rate is set at 1/dx S/s. Compare the signal with the limit. For the upper limit, if the data poin

Performing Limit Testing

To perform limit testing, you define a mask, acquire the signal using a DAQ device,
 then compare the signal with the limit.

After you define the mask, you acquire a signal using a DAQ device. The sample rate is
 set at 1/dx S/s. Compare the signal with the limit. For the upper limit, if the data
 point is less than or equal to the limit point, the test passes. If the data point is
 greater than the limit point, the test fails. For the lower limit, if the data point is
 greater than or equal to the limit point, the test passes. If the data point is less
 than the limit point, the test fails.

The following figure shows the result of limit testing in a continuous mask case. The
 test signal falls within the mask at all the points it is sampled, other than points b
 and c. Thus, the limit test fails. Point d is not tested because it falls outside the
 mask.

Figure 84.

[IMAGE alt='1378' src='GUID-C65761D2-C737-4B5C-94F0-A95C6697FA35-a5.png']

The following figure shows the result of limit testing in a segmented mask case. All the
 points fall within the mask. Points b and c are not tested because the mask is undefined
 at those points. Thus, the limit test passes. Point d is not tested because it falls
 outside the mask.

Figure 85.

[IMAGE alt='1378' src='GUID-709E1502-9DBA-452B-9095-5F525653BA2D-a5.png']

Parent topic:

Limit Testing

<!--NI_TOPIC bundle=labview-sound-and-vibration-toolkit path=total-harmonic-distortion-plus-noise-thd-n.html language=enus -->
## TOPIC 00099: Total Harmonic Distortion Plus Noise (THD + N)

- bundle_id: `labview-sound-and-vibration-toolkit`
- source_path: `total-harmonic-distortion-plus-noise-thd-n.html`
- source_url: https://docs-be.ni.com/bundle/labview-sound-and-vibration-toolkit/raw/resource/enus/total-harmonic-distortion-plus-noise-thd-n.html
- document_id: `labview-sound-and-vibration-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Real-world signals usually contain noise. A system can introduce additional noise into the signal. Total harmonic distortion plus noise (THD + N) measures signal distortion while taking into account the amount of noise power present in the signal.Measuring THD + N requires measuring the amplitude of

Total Harmonic Distortion Plus Noise (THD + N)

Real-world signals usually contain noise. A system can introduce additional
 noise into the signal. Total harmonic distortion plus noise (THD + N)
 measures signal distortion while taking into account the amount of noise
 power present in the signal.

Measuring THD + N requires measuring the amplitude of the fundamental frequency and the power
 present in the remaining signal after removing the fundamental
 frequency. The following equation yields THD + N:

THD

+

N

=

A

2

2

+

A

3

2

+

…

+

N

2

A

1

2

+

A

2

2

+

A

3

2

+

…

+

N

2

where N is the noise power.

A low THD + N measurement means that the system has a low amount of harmonic distortion and a low
 amount of noise from interfering signals, such as AC mains hum
 and wideband white noise.

As with THD, you usually report the results of a THD + N measurement in terms of the highest
 order harmonic present in the measurement, such as THD + N
 through the third harmonic.

The following equation yields percentage total harmonic distortion + noise (%THD + N):

%

THD

+

N

=

(

100

)

(

A

2

2

+

A

3

2

+

…

+

N

2

A

1

2

+

A

2

2

+

A

3

2

+

…

+

N

2

)

Parent topic:

Distortion

<!--NI_TOPIC bundle=labview-sound-and-vibration-toolkit path=vector-averaging.1.html language=enus -->
## TOPIC 00100: Vector Averaging

- bundle_id: `labview-sound-and-vibration-toolkit`
- source_path: `vector-averaging.1.html`
- source_url: https://docs-be.ni.com/bundle/labview-sound-and-vibration-toolkit/raw/resource/enus/vector-averaging.1.html
- document_id: `labview-sound-and-vibration-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Vector averaging eliminates noise from synchronous signals and computes the average of complex quantities directly.In vector averaging, the real part is averaged separately from the imaginary part. Averaging the real part separately from the imaginary part can reduce the noise floor for random signa

Vector Averaging

Vector averaging eliminates noise from synchronous signals and computes the average
 of complex quantities directly.

In vector averaging, the real part is averaged separately from the imaginary part. Averaging the
 real part separately from the imaginary part can reduce the noise floor for random
 signals because random signals are not phase coherent from one time record to the
 next. The real and imaginary parts are averaged separately, reducing noise but
 usually requiring a trigger.

Vector-averaged measurements are computed according to the following equations:

| Measurement | Equation |
| --- | --- |
| FFT spectrum | 〈 X 〉 |
| Power spectrum | 〈 X * 〉 ⋅ 〈 X 〉 |
| Cross spectrum | 〈 X * 〉 ⋅ 〈 Y 〉 |
| Frequency response | ( Y ) ( X ) |

where

X is the complex FFT of signal
 x (stimulus)

Y is the complex FFT of signal
 y (response)

X* is the complex conjugate of
 X

(X) is the average of
 X, real and imaginary parts
 being averaged separately

Parent topic:

Averaging Modes
