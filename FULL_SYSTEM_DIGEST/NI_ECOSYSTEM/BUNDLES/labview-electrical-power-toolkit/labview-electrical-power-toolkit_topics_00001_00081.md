# NI DOCUMENT BUNDLE: labview-electrical-power-toolkit

<!--NI_BUNDLE_CHUNK bundle=labview-electrical-power-toolkit start=1 end=81 -->
<!--NI_TOPIC bundle=labview-electrical-power-toolkit path=1-discrete-fourier-transform.html language=enus -->
## TOPIC 00001: Discrete Fourier Transform

- bundle_id: `labview-electrical-power-toolkit`
- source_path: `1-discrete-fourier-transform.html`
- source_url: https://docs-be.ni.com/bundle/labview-electrical-power-toolkit/raw/resource/enus/1-discrete-fourier-transform.html
- document_id: `labview-electrical-power-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: A discrete Fourier transform (DFT) processor calculates the Fourier transform components for a voltage waveform or a current waveform. You can use the LabVIEW Electrical Power Toolkit to break down voltage waveforms and current waveforms into harmonic components.Breaking down the waveforms into harm

### Discrete Fourier Transform

A discrete Fourier transform (DFT) processor calculates the Fourier transform
 components for a voltage waveform or a current waveform. You can use the LabVIEW
 Electrical Power Toolkit to break down voltage waveforms and current waveforms into
 harmonic components.

Breaking down the waveforms into harmonic components provides a frequency resolution of
 approximately 5 Hz, which is calculated by dividing the fundamental frequency by
 10 or 12. The Electrical Power Toolkit calculates the fast Fourier transform (FFT)
 of a block of time-domain data. The Electrical Power Toolkit then provides the
 frequency spectrum of the data within the observation window, following the IEC
 61000-4-30:2008 standard. The width of the observation window is 10 cycles for a
 50 Hz electrical power system or 12 cycles for a 60 Hz electrical power system.
 The FFT is a digital implementation of the Fourier transform. Thus, the FFT does
 not yield a continuous spectrum. Instead, the FFT resolves the frequency content
 of the waveform into a discrete spectrum with a finite number of frequency lines,
 or bins.

Parent topic:

Measuring Harmonics

Related concepts:

- Measuring Signaling Voltages

<!--NI_TOPIC bundle=labview-electrical-power-toolkit path=2-grouping.html language=enus -->
## TOPIC 00002: Grouping

- bundle_id: `labview-electrical-power-toolkit`
- source_path: `2-grouping.html`
- source_url: https://docs-be.ni.com/bundle/labview-electrical-power-toolkit/raw/resource/enus/2-grouping.html
- document_id: `labview-electrical-power-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The LabVIEW Electrical Power Toolkit returns the frequency spectra of voltage waveforms and current waveforms by performing a fast Fourier transform (FFT) on the time-domain data. The Electrical Power Toolkit groups the spectral components and analyzes the resulting harmonic and interharmonic groups

### Grouping

The LabVIEW Electrical Power Toolkit returns the frequency spectra of voltage waveforms
 and current waveforms by performing a fast Fourier transform (FFT) on the time-domain data. The
 Electrical Power Toolkit groups the spectral components and analyzes the resulting harmonic and
 interharmonic groups or subgroups according to IEC 61000-4-7:2009.

A harmonic group includes all spectral components adjacent to the harmonic frequency within the
 observation window. The width of the observation window is as follows:

- 10 harmonic-centered spectral components for a 50 Hz electrical power system
- 12 harmonic-centered spectral components for a 60 Hz electrical power system

An interharmonic group includes all spectral components between two consecutive harmonic
 frequencies.

A harmonic subgroup includes the harmonic frequency and the two immediately adjacent spectral
 components. An interharmonic subgroup includes all spectral components between two
 consecutive harmonic frequencies, excluding the spectral components immediately adjacent
 to the harmonic frequencies.

Harmonic grouping ensures that the evaluation of the total power is accurate because harmonic
 grouping accounts for spectral leakage. Spectral leakage results in a loss of information from
 a single harmonic spectral line to surrounding spectral lines. The following figure shows the
 amplitude of a 50 Hz voltage signal with the 6th harmonic component.

[IMAGE alt='Graph showing amplitude of a 50 Hz voltage signal with the 6th harmonic component.' src='GUID-9CC2949E-D9AC-4224-B861-117FAAC293AC-a5.gif']

The voltage signal changes from 100 V to 20 V. Meanwhile, the 6th harmonic component changes
 from 5 V to 1 V. The expected RMS value of the 6th harmonic component is 3.606.

The following figure shows the RMS values of magnitudes in the frequency domain, obtained by
 performing a discrete Fourier transform (DFT) on the 50 Hz voltage signal and the 6th harmonic
 group.

[IMAGE alt='Graph showing RMS values of harmonic components around 300 Hz.' src='GUID-5ACB9701-4BA0-4A1B-987E-6BAAC59F361B-a5.gif']

In the previous figure, there is a spectral leakage from the harmonic spectral line at 300 Hz to
 the surrounding interharmonics. The single bin at 300 Hz shows an RMS voltage value of 3,
 which has a 16.8% error compared to the expected value. If you use the harmonic subgroup
 instead of just the single bin, the result is 3.5, which has an error of 3%. Finally, when
 using the harmonic group, which significantly reduces spectral leakage, the measured RMS value
 is 3.564. This results in a lower error rate of 1.1%. Therefore, measurement using the
 harmonic group rather than just the single harmonic spectral line gives a more accurate value
 for the total energy of a harmonic component.

If interharmonic components are present in a signal, using the harmonic subgroup rather than
 harmonic group might return more accurate results. The following figure shows the amplitude of
 a 50 Hz voltage signal with the 6th harmonic component and an interharmonic component present
 at 325 Hz.

[IMAGE alt='Graph showing amplitude of a 50 Hz voltage signal with harmonic and interharmonic components.' src='GUID-9A61C76D-8C2C-4A45-90E0-DDF579ED95AC-a5.gif']

The voltage signal fluctuates from 100 V to 20 V. Meanwhile, both the 6th harmonic component and
 the interharmonic component fluctuate from 5 V to 1 V. The expected RMS value during this
 block is 3.606 for both the harmonic components and the interharmonic components.

The following figure illustrates the RMS values of voltage components in the frequency
 domain. These values are derived by applying a DFT to the 50 Hz voltage signal, and the 6th
 harmonic group and subgroup.

[IMAGE alt='Graph showing RMS values of voltage components in the frequency domain.' src='GUID-D4C4A54B-4915-4F5E-8704-BB7158D73924-a5.gif']

There is a spectral leakage from the 6th harmonic at 300 Hz and from the interharmonic at 325 Hz.
 If you use the harmonic group, the measured RMS value is 4.378, which has an error of 21.4%
 compared to the expected value. This large error is because of the spectral leakage from the
 interharmonic overlapping with the 6th harmonic group. However, if you use the harmonic
 subgroup, the measured RMS value of the 6th harmonic is 3.511, which has an error of 2.6%.
 Thus, you use the harmonic subgroup rather than the harmonic group for RMS measurements when
 there are interharmonics present in a signal.

Parent topic:

Measuring Harmonics

<!--NI_TOPIC bundle=labview-electrical-power-toolkit path=acquiring-signals.html language=enus -->
## TOPIC 00003: Acquiring Signals

- bundle_id: `labview-electrical-power-toolkit`
- source_path: `acquiring-signals.html`
- source_url: https://docs-be.ni.com/bundle/labview-electrical-power-toolkit/raw/resource/enus/acquiring-signals.html
- document_id: `labview-electrical-power-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: You usually acquire electrical power signals with a data acquisition module, such as NI 9225 or NI 9227. The following are common considerations in measurement analysis when you obtain data from a data acquisition module: Anti-aliasing. Sample rate. Block size. Synchronous sampling. Resampling.

### Acquiring Signals

You usually acquire electrical power signals with a data acquisition module, such as NI 9225 or
 NI 9227. The following are common considerations in measurement analysis when you obtain
 data from a data acquisition module:

- Anti-aliasing.
- Sample rate.
- Block size.
- Synchronous sampling.
- Resampling.

Parent topic:

Measuring Signals

<!--NI_TOPIC bundle=labview-electrical-power-toolkit path=active-power.html language=enus -->
## TOPIC 00004: Active Power

- bundle_id: `labview-electrical-power-toolkit`
- source_path: `active-power.html`
- source_url: https://docs-be.ni.com/bundle/labview-electrical-power-toolkit/raw/resource/enus/active-power.html
- document_id: `labview-electrical-power-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: In an AC circuit, the voltage and current are sinusoidal and are a function of time. Use the following equation to calculate active power.where T is the cycle time of U(t) and I(t), U[RMS] and I[RMS] are RMS values of U(t) and I(t), and cosθ is the angle difference between U(t) and I(t).You measure

### Active Power

In an AC circuit, the voltage and current are sinusoidal and are a function of time. Use the
 following equation to calculate active power.

[IMAGE alt='image' src='GUID-605AF2B9-6143-4495-8C38-0A0FB4BD67F5-a5.gif']

where T is the cycle time of U(t) and
 I(t),
 U<sub>RMS</sub> and
 I<sub>RMS</sub> are RMS values of
 U(t) and
 I(t), and cosθ is the angle difference between
 U(t) and
 I(t).

You measure active power in watts (W).

Parent topic:

Power Measurement

<!--NI_TOPIC bundle=labview-electrical-power-toolkit path=advanced-triggering.html language=enus -->
## TOPIC 00005: Advanced Triggering

- bundle_id: `labview-electrical-power-toolkit`
- source_path: `advanced-triggering.html`
- source_url: https://docs-be.ni.com/bundle/labview-electrical-power-toolkit/raw/resource/enus/advanced-triggering.html
- document_id: `labview-electrical-power-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can combine multiple triggers by using Boolean logic, such as AND, OR, and NOT Boolean operators. The following figure shows the RMS voltages for each phase in a three-phase voltage signal. In the previous figure, the voltage dip, swell, and interruption are three types of voltage events as defi

### Advanced Triggering

You can combine multiple triggers by using Boolean logic, such as AND, OR, and NOT Boolean
 operators. The following figure shows the RMS voltages for each phase in a three-phase
 voltage signal.

[IMAGE alt='image' src='GUID-486D4AAB-090E-4BF2-9F35-1D3D158670DF-a5.gif']

In the previous figure, the voltage dip, swell, and interruption are three types of voltage
 events as defined in IEC 61000-4-30:2008. The duration of a voltage swell on phases A
 and B is T<sub>1</sub>. The sum T<sub>1</sub> +
 T<sub>2</sub> is the duration of a voltage dip on phase B.
 T<sub>3</sub> is the duration of a voltage interruption on phase
 A and T<sub>2</sub> + T<sub>3</sub> is a voltage
 dip on phases A and C. The sum T<sub>1</sub> +
 T<sub>2</sub> + T<sub>3</sub> is the duration
 of a voltage dip spanning all phases.

You can define three triggers that fire when the voltage crosses the voltage dip, swell, or
 interruption thresholds and then use Boolean operators to combine the triggers. For
 example, the combination dip AND swell NOT interruption results in a
 total record duration equals to T<sub>1</sub>. The combination
 dip OR swell OR interruption results in a total record duration
 equals to T<sub>1</sub> + T<sub>2</sub> +
 T<sub>3</sub>.

Parent topic:

Triggers

<!--NI_TOPIC bundle=labview-electrical-power-toolkit path=aggregation-intervals.html language=enus -->
## TOPIC 00006: Aggregation Intervals

- bundle_id: `labview-electrical-power-toolkit`
- source_path: `aggregation-intervals.html`
- source_url: https://docs-be.ni.com/bundle/labview-electrical-power-toolkit/raw/resource/enus/aggregation-intervals.html
- document_id: `labview-electrical-power-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: IEC 61000-4-30:2008 specifies to aggregate data for 150/180-cycle, 10-minute, and 2-hour intervals. IEC 61000-4-30:2008 defines three classes of aggregation: Class A, Class S, and Class B. The LabVIEW Electrical Power Toolkit follows Class S and uses the following intervals for aggregating data: 150

### Aggregation Intervals

IEC 61000-4-30:2008 specifies to aggregate data for 150/180-cycle, 10-minute, and 2-hour
 intervals. IEC 61000-4-30:2008 defines three classes of aggregation: Class A, Class S,
 and Class B. The LabVIEW Electrical Power Toolkit follows Class S and uses the following
 intervals for aggregating data:

- 150/180-cycle aggregation —Aggregate data using a 150-cycle interval for 50 Hz systems and a 180-cycle interval for 60 Hz systems. The 150/180-cycle interval corresponds to fifteen 10/12-cycle blocks without gap.
- 10-minute aggregation —Aggregate data using a 10-minute interval, which corresponds to 3,000 10/12-cycle blocks. There is no overlap between adjacent aggregation intervals.
- 2-hour aggregation —Aggregate data using a 2-hour interval. The data for the 2-hour aggregation is from the values of twelve 10-minute intervals. There is no overlap between adjacent aggregation intervals.

The Electrical Power Toolkit automatically restarts data accumulation at the beginning of the next aggregation interval after the previous aggregation interval expires.

#### Frequency Aggregation

In frequency aggregation, you aggregate frequency values by using 10-second intervals that corresponds to a non-integer number of cycles because the power frequency might not be exactly 50 Hz or 60 Hz within a given 10-second interval. The Electrical Power Toolkit automatically restarts data accumulation at the beginning of the next 10/12-cycle block after the previous 10-second aggregation interval expires. You can use 10-second values to calculate site and system indexes.

#### Flicker Aggregation

The Electrical Power Toolkit complies with IEC 61000-4-15:2010 for the aggregation of *flicker measurements*. The basic aggregation intervals are the short-term flicker and long-term flicker.

Parent topic:

Time Aggregation

Related concepts:

- Flickers

<!--NI_TOPIC bundle=labview-electrical-power-toolkit path=aggregation-intervals_2.html language=enus -->
## TOPIC 00007: Aggregation Intervals

- bundle_id: `labview-electrical-power-toolkit`
- source_path: `aggregation-intervals_2.html`
- source_url: https://docs-be.ni.com/bundle/labview-electrical-power-toolkit/raw/resource/enus/aggregation-intervals_2.html
- document_id: `labview-electrical-power-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: IEC 61000-4-30:2008 specifies to aggregate data for 150/180-cycle, 10-minute, and 2-hour intervals. IEC 61000-4-30:2008 defines three classes of aggregation: Class A, Class S, and Class B. The LabVIEW Electrical Power Toolkit follows Class S and uses the following intervals for aggregating data: 150

### Aggregation Intervals

IEC 61000-4-30:2008 specifies to aggregate data for 150/180-cycle, 10-minute, and 2-hour
 intervals. IEC 61000-4-30:2008 defines three classes of aggregation: Class A, Class S,
 and Class B. The LabVIEW Electrical Power Toolkit follows Class S and uses the following
 intervals for aggregating data:

- 150/180-cycle aggregation —Aggregate data using a 150-cycle interval for 50 Hz systems and a 180-cycle interval for 60 Hz systems. The 150/180-cycle interval corresponds to fifteen 10/12-cycle blocks without gap.
- 10-minute aggregation —Aggregate data using a 10-minute interval, which corresponds to 3,000 10/12-cycle blocks. There is no overlap between adjacent aggregation intervals.
- 2-hour aggregation —Aggregate data using a 2-hour interval. The data for the 2-hour aggregation is from the values of twelve 10-minute intervals. There is no overlap between adjacent aggregation intervals.

The Electrical Power Toolkit automatically restarts data accumulation at the beginning of the next aggregation interval after the previous aggregation interval expires.

#### Frequency Aggregation

In frequency aggregation, you aggregate frequency values by using 10-second intervals that corresponds to a non-integer number of cycles because the power frequency might not be exactly 50 Hz or 60 Hz within a given 10-second interval. The Electrical Power Toolkit automatically restarts data accumulation at the beginning of the next 10/12-cycle block after the previous 10-second aggregation interval expires. You can use 10-second values to calculate site and system indexes.

#### Flicker Aggregation

The Electrical Power Toolkit complies with IEC 61000-4-15:2010 for the aggregation of *flicker measurements*. The basic aggregation intervals are the short-term flicker and long-term flicker.

Parent topic:

Time Aggregation

<!--NI_TOPIC bundle=labview-electrical-power-toolkit path=anti-aliasing.html language=enus -->
## TOPIC 00008: Anti-Aliasing

- bundle_id: `labview-electrical-power-toolkit`
- source_path: `anti-aliasing.html`
- source_url: https://docs-be.ni.com/bundle/labview-electrical-power-toolkit/raw/resource/enus/anti-aliasing.html
- document_id: `labview-electrical-power-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Aliasing is the phenomenon that frequencies greater than the Nyquist frequency are shifted erroneously to lower frequencies. Use the following equation to calculate the Nyquist frequency:f[Nyquist] = sample rate / 2The only way to protect data from aliasing is to apply appropriate aliasing protectio

### Anti-Aliasing

Aliasing is the phenomenon that frequencies greater than the Nyquist frequency are shifted
 erroneously to lower frequencies. Use the following equation to calculate the Nyquist
 frequency:

f<sub>Nyquist</sub> = sample rate /
 2

The only way to protect data from aliasing is to apply appropriate aliasing protection before you
 generate or acquire data. Aliasing occurs when you generate or sample the data. You
 cannot remove aliased components from the data without detailed knowledge of the
 original signal. In general, you cannot distinguish between true frequency components
 and aliased frequency components. Therefore, accurate frequency measurements require
 adequate aliasing protection.

Aliasing protection is automatic in any acquisition when you perform voltage and current
 measurements with an NI 9225 or NI 9227.

Parent topic:

Acquiring Signals

<!--NI_TOPIC bundle=labview-electrical-power-toolkit path=apparent-power.html language=enus -->
## TOPIC 00009: Apparent Power

- bundle_id: `labview-electrical-power-toolkit`
- source_path: `apparent-power.html`
- source_url: https://docs-be.ni.com/bundle/labview-electrical-power-toolkit/raw/resource/enus/apparent-power.html
- document_id: `labview-electrical-power-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Apparent power is the product of the voltage and current without considering the phase shift that may be present between the voltage and current. You can use the following equation to calculate apparent power.S = U[RMS]I[RMS]You measure apparent power in volt-amperes (VA).

### Apparent Power

Apparent power is the product of the voltage and current without considering the phase shift that
 may be present between the voltage and current. You can use the following equation to
 calculate apparent power.

S =
 U<sub>RMS</sub>I<sub>RMS</sub>

You measure apparent power in volt-amperes (VA).

Parent topic:

Power Measurement

<!--NI_TOPIC bundle=labview-electrical-power-toolkit path=applications-of-signaling-voltages.html language=enus -->
## TOPIC 00010: Applications of Signaling Voltages

- bundle_id: `labview-electrical-power-toolkit`
- source_path: `applications-of-signaling-voltages.html`
- source_url: https://docs-be.ni.com/bundle/labview-electrical-power-toolkit/raw/resource/enus/applications-of-signaling-voltages.html
- document_id: `labview-electrical-power-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: A common application of signaling voltages is for utilities to exercise load control on an electrical grid, also known as applying ripple control signals. The signaling voltage contains commands that can remotely control industrial and domestic equipment, such as relays, hot water heaters, revenue m

### Applications of Signaling Voltages

A common application of signaling voltages is for utilities to exercise load control on an
 electrical grid, also known as applying ripple control signals. The signaling voltage
 contains commands that can remotely control industrial and domestic equipment, such as
 relays, hot water heaters, revenue meters, and irrigation systems. For example, a
 utility experiencing a surge in demand during peak time can use a signaling voltage to
 remotely switch off domestic hot water heaters. The utility then can use a signaling
 voltage to remotely switch the hot water heaters back on during off-peak time when the
 demand is lower. The application of signaling voltages benefits utilities by allowing
 the utilities to balance the load. The application of signaling voltages also benefits
 consumers, who can save money by using power during off-peak hours.

Parent topic:

Signaling

<!--NI_TOPIC bundle=labview-electrical-power-toolkit path=automatic-extension-triggering.html language=enus -->
## TOPIC 00011: Automatic Extension Triggering

- bundle_id: `labview-electrical-power-toolkit`
- source_path: `automatic-extension-triggering.html`
- source_url: https://docs-be.ni.com/bundle/labview-electrical-power-toolkit/raw/resource/enus/automatic-extension-triggering.html
- document_id: `labview-electrical-power-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use automatic extension triggering to capture data for multiple faults in the same recording period. If a second trigger fires while a disturbance recorder is capturing data because of the firing of a prior trigger, the disturbance recorder can automatically extend the recording period to ca

### Automatic Extension Triggering

You can use automatic extension triggering to capture data for multiple faults in the same
 recording period. If a second trigger fires while a disturbance recorder is capturing
 data because of the firing of a prior trigger, the disturbance recorder can
 automatically extend the recording period to capture both faults. Recording stops when
 the second trigger is no longer active. Automatic extension triggering is especially
 useful for monitoring multi-phase power systems, because a second fault may occur on a
 channel that is different from the first fault. The following figure shows automatic
 extension triggering.

[IMAGE alt='image' src='GUID-A8AF809E-A694-4595-94FA-F9B4ED1C8299-a5.gif']

Parent topic:

Triggers

<!--NI_TOPIC bundle=labview-electrical-power-toolkit path=block-size.html language=enus -->
## TOPIC 00012: Block Size

- bundle_id: `labview-electrical-power-toolkit`
- source_path: `block-size.html`
- source_url: https://docs-be.ni.com/bundle/labview-electrical-power-toolkit/raw/resource/enus/block-size.html
- document_id: `labview-electrical-power-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: When performing voltage and current measurements, you must take the block size of the data into consideration. You can measure the block size either in terms of samples or time, as long as the sample rate is constant. The following equation calculates the acquisition duration:T = N * dt where T is t

### Block Size

When performing voltage and current measurements, you must take the block size of the data into
 consideration. You can measure the block size either in terms of samples or time, as
 long as the sample rate is constant. The following equation calculates the acquisition
 duration:

T = N * dt

where T is the acquisition duration; N is the block
 size; dt is the sample interval.

The acquisition duration determines the time resolution that you can achieve in a continuous
 acquisition. The duration of each measurement block impacts the rate at which the data
 acquisition loop must run and the time/frequency resolution of all block-based
 measurements. When you perform power quality measurement in compliance with IEC
 61000-4-30:2008, the block size must be cycle-based and is 10 cycles for a 50 Hz
 electrical power system and 12 cycles for a 60 Hz electrical power system.

Parent topic:

Acquiring Signals

<!--NI_TOPIC bundle=labview-electrical-power-toolkit path=calibration-process.html language=enus -->
## TOPIC 00013: Calibration Process

- bundle_id: `labview-electrical-power-toolkit`
- source_path: `calibration-process.html`
- source_url: https://docs-be.ni.com/bundle/labview-electrical-power-toolkit/raw/resource/enus/calibration-process.html
- document_id: `labview-electrical-power-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: A general process of calibrating a measurement instrument contains the following steps: Generate a standard signal of known or assigned accuracy. Use the measurement instrument to measure the standard signal. Compare the measured results with the standard and record the correction values. In future

### Calibration Process

A general process of calibrating a measurement instrument contains the following steps:

1. Generate a standard signal of known or assigned accuracy.
2. Use the measurement instrument to measure the standard signal.
3. Compare the measured results with the standard and record the correction values.

In future measurement, you compensate for inaccurate measurements by adding the correction values
 to measured results.

The following figure shows a typical calibration system architecture in power quality
 measurement.

[IMAGE alt='image' src='GUID-CEB0920B-066A-42EE-85A7-553E9775F7A0-a5.gif']

In the previous figure, the measurement instrument is a power quality analyzer that consists of
 data acquisition modules, leads, transducers, transformers, and other components.

The standard signal generator is a highly accurate and scalable instrument for calibrating the
 power quality analyzer. You use standard signal generators to ensure a thorough,
 accurate, and consistent process of calibration and to guarantee traceability to
 national and international standards. Standard signal generators can generate
 comprehensive electrical power signals that have high accuracy and can operate with one,
 two, three, or four phases independently and simultaneously. For example, you can use
 standard signal generators to generate sinusoidal electrical power signals or irregular
 electrical power signals with phenomena of voltage harmonics, interharmonics, flicker,
 dips, swell, interruption, and so on.

You use the PC to support the functionality of standard signal generators by using documented,
 controlled, and automated procedures.

In this typical calibration system architecture, the PC controls the standard signal generator
 through various instrument control interfaces and directs the standard signal generator
 to generate standard signals for calibration. The power quality analyzer measures the
 standard signals that the standard signal generator generates. Ethernet communication
 between the power quality analyzer and the PC helps to transmit the measured results to
 the PC and receive commands from the PC. The PC then calculates and records correction
 values in certain file format by comparing the measured values and the standard
 values.

Parent topic:

Calibration

<!--NI_TOPIC bundle=labview-electrical-power-toolkit path=calibration.html language=enus -->
## TOPIC 00014: Calibration

- bundle_id: `labview-electrical-power-toolkit`
- source_path: `calibration.html`
- source_url: https://docs-be.ni.com/bundle/labview-electrical-power-toolkit/raw/resource/enus/calibration.html
- document_id: `labview-electrical-power-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Calibration with the LabVIEW Electrical Power Toolkit adjusts instruments for accuracy against standards. In test and measurement systems, various conditions affect the operation of a measurement instrument. Conditions vary beyond the tolerance of the measurement instrument and lead to inaccurate me

### Calibration

Calibration with the LabVIEW Electrical Power Toolkit adjusts instruments for
 accuracy against standards.

In *test and measurement systems*, various conditions affect the operation of a
 measurement instrument. Conditions vary beyond the tolerance of the measurement
 instrument and lead to inaccurate measurements. Measuring electrical power involves
 using various transducers and data acquisition devices to capture voltage and current
 signals separately. This approach can sometimes lead to inaccurate measurement results.
 Calibration helps to check and adjust inaccurate measurements and thus to make certain
 that the measurement instrument measures accurately. You calibrate the measurement
 instrument against a standard of known accuracy to find out how far the measured results
 are from the standard. In future measurement, you compensate for inaccurate measurements
 to ensure the accuracy. The process of calibration also provides traceable verification
 that proves the accuracy of measurements.

In power quality measurement, IEC 61000-4-30:2008 defines measurement methods
 and accuracy requirements of power quality parameters. You use the LabVIEW Electrical
 Power Toolkit to calibrate power quality analyzers built with National Instruments
 software and hardware. The calibration ensures the power quality analyzers meet the
 Class A compliance certificate of IEC 61000-4-30:2008.

- [Calibration Process](calibration-process.html)
- [Performing Calibration](performing-calibration.html)

Related concepts:

- Power Quality

<!--NI_TOPIC bundle=labview-electrical-power-toolkit path=choosing-a-file-format.html language=enus -->
## TOPIC 00015: Choosing a File Format

- bundle_id: `labview-electrical-power-toolkit`
- source_path: `choosing-a-file-format.html`
- source_url: https://docs-be.ni.com/bundle/labview-electrical-power-toolkit/raw/resource/enus/choosing-a-file-format.html
- document_id: `labview-electrical-power-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The LabVIEW Electrical Power Toolkit supports the Common Format for Transient Data Exchange (COMTRADE) file format and the Technical Data Management Streaming (TDMS) file format for logging electrical power data. The TDMS file format is a file format that LabVIEW provides. The TDMS file format and t

### Choosing a File Format

The LabVIEW Electrical Power Toolkit supports the *Common Format for Transient Data Exchange
 (COMTRADE)* file format and the Technical Data Management Streaming
 (TDMS) file format for logging electrical power data. The
 TDMS file format is a file format that LabVIEW provides. The
 TDMS file format and the COMTRADE file
 format are useful for logging different types of fault, test, and
 simulation data from electrical power systems.

Use the following guidelines to determine whether to use the Technical Data Management
 Streaming (TDMS) file format or the Common Format for
 Transient Data Exchange (COMTRADE) file format to read data from files
 or write data to files:

- Use the COMTRADE file format when you want to make your data available to
 other applications, devices, and companies, because the COMTRADE file
 format is the most common industrial standard format.
- Use the COMTRADE file format when you need to log data with a variable
 sample rate.
- Use the COMTRADE file format for real-time CompactRIO controllers when
 speed is important to you. The COMTRADE file format is more
 efficient than the TDMS file format because the
 TDMS file format uses both text and binary files.
- Use the TDMS file format when you want to manipulate complex records of
 data or different data types in LabVIEW.

Parent topic:

Data Logging

Related concepts:

- COMTRADE File Format

<!--NI_TOPIC bundle=labview-electrical-power-toolkit path=comtrade-file-format.html language=enus -->
## TOPIC 00016: COMTRADE File Format

- bundle_id: `labview-electrical-power-toolkit`
- source_path: `comtrade-file-format.html`
- source_url: https://docs-be.ni.com/bundle/labview-electrical-power-toolkit/raw/resource/enus/comtrade-file-format.html
- document_id: `labview-electrical-power-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: IEEE Std C37.111-1999 defines the Common Format for Transient Data Exchange (COMTRADE) file format for transient waveform and event data of electrical power systems. Manufacturers and utilities usually record and store data by using proprietary systems. The COMTRADE file format provides a standardiz

### COMTRADE File Format

IEEE Std C37.111-1999 defines the Common Format for Transient Data Exchange (COMTRADE)
 file format for transient waveform and
 event data of electrical power systems.
 Manufacturers and utilities usually record and store
 data by using proprietary systems. The
 COMTRADE file format
 provides a standardized, non-proprietary, and easy
 to interpret method for exchanging data. IEEE Std
 C37.111-1999 defines the following four files
 associated with each COMTRADE record:

- Data (.dat) file — Mandatory binary or ASCII text file. A data file
 contains a time-stamped numerical value for each input channel for each sample in
 the record. Values can be zero-based or have a zero offset.
- Configuration (.cfg) file — Mandatory ASCII text file. A configuration
 file contains information to interpret the data file such as the sample rates,
 number of channels, line frequency, and channel information. A configuration file
 also specifies whether the data file is in ASCII or binary format.
- Header (.hdr) file — Optional ASCII text file. A header file contains
 supplementary information describing an electrical power system and test conditions.
 A header file can include information like fault description, voltage ratings of
 transformer windings, line length, and a description of the test conditions.
- Information (.inf) file — Optional ASCII text file. An information file
 contains public sections and private sections. A public section contains information
 in a format that equipment and software from multiple manufacturers can use. A
 private section contains information in a format that is unique to a specific
 manufacturer. An information file may contain multiple private sections for a single
 manufacturer or for multiple manufacturers.

Parent topic:

Data Logging

Related concepts:

- Choosing a File Format

<!--NI_TOPIC bundle=labview-electrical-power-toolkit path=connections-and-wiring.html language=enus -->
## TOPIC 00017: Connections and Wiring

- bundle_id: `labview-electrical-power-toolkit`
- source_path: `connections-and-wiring.html`
- source_url: https://docs-be.ni.com/bundle/labview-electrical-power-toolkit/raw/resource/enus/connections-and-wiring.html
- document_id: `labview-electrical-power-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Three-phase alternating current systems transmit electrical power using three or four wires. Power transmission typically uses three wires that have a mutual phase difference of 120 degrees. Distribution grids often use four wires, where the fourth wire is neutral. You can connect three one-phase tr

### Connections and Wiring

Three-phase alternating current systems transmit electrical power using three or four wires.
 *Power transmission* typically uses three wires that have a mutual phase
 difference of 120 degrees. *Distribution grids* often use four wires, where
 the fourth wire is neutral. You can connect three one-phase transformers to develop a
 three-phase voltage. You can connect the three transformers by using a wye-to-wye,
 delta-to-delta, delta-to-wye, or wye-to-delta connection. The supply voltage, the
 requirements of the loads, and the practice of the local power company determine the
 connection method.

Parent topic:

Electrical Power Signals

Related concepts:

- Power Transmission
- Power Distribution
- Line and Bus Configurations

<!--NI_TOPIC bundle=labview-electrical-power-toolkit path=conversion.html language=enus -->
## TOPIC 00018: Conversion

- bundle_id: `labview-electrical-power-toolkit`
- source_path: `conversion.html`
- source_url: https://docs-be.ni.com/bundle/labview-electrical-power-toolkit/raw/resource/enus/conversion.html
- document_id: `labview-electrical-power-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: A delta to wye (D to Y) conversion converts a line voltage to a phase voltage. You use a D to Y conversion when you calculate power, impedance, and signaling voltage, which are always phase-based no matter what the connection is. However, a D to Y conversion is useful only when a three-phase electri

### Conversion

A delta to wye (D to Y) conversion converts a line voltage to a phase voltage. You use a D to Y
 conversion when you calculate power, impedance, and signaling voltage, which are always
 phase-based no matter what the connection is. However, a D to Y conversion is useful
 only when a three-phase electrical power system is symmetric. Otherwise the values from
 the conversion do not correspond to actual phase values.

A wye to delta (Y to D) conversion converts a phase voltage to a line voltage. In some
 high-voltage systems, you can specify the nominal voltage as the line voltage because a
 high-voltage system is usually isolated and there is no neutral wire. However, sometimes
 voltage transformers have connections that produce phase voltage on the output. The
 output phase voltage returns precise information about the phase on which the
 disturbance occurs. On the line voltage side you have voltages from two phases combined
 so that you do not directly see voltage fluctuations on individual phases. Thus you
 perform a Y to D conversion when you have phase voltage outputs from voltage
 transformers but the high-voltage side connects to delta.

Parent topic:

Connections and Wiring

Related concepts:

- Power Measurement

<!--NI_TOPIC bundle=labview-electrical-power-toolkit path=data-logging.html language=enus -->
## TOPIC 00019: Data Logging

- bundle_id: `labview-electrical-power-toolkit`
- source_path: `data-logging.html`
- source_url: https://docs-be.ni.com/bundle/labview-electrical-power-toolkit/raw/resource/enus/data-logging.html
- document_id: `labview-electrical-power-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The section highlights the significance of data logging in analyzing electrical power systems. This process is crucial for preventing faults and enhancing both power quality and consumption efficiency.Logging data for offline post-processing and further analysis is important for administering electr

### Data Logging

The section highlights the significance of data logging in analyzing electrical power
 systems. This process is crucial for preventing faults and enhancing both power quality and
 consumption efficiency.

Logging data for offline post-processing and further analysis is important for administering
 electrical power systems. For example, if a voltage event disturbs an electrical power grid,
 analyze the logged data. Analyzing the logged data helps you identify the location and cause
 of the fault. Analyzing logged data can help to avoid such fault occurring again in the
 future. Long-term monitoring of power quality and consumption data can be beneficial to the
 electrical power industry.

The following three types of data logging are common in the electrical power industry:

- Waveform data logging for data with high sample rates
- Disturbance data logging for slower-speed data
- Trend data logging over a long term

For more information, see the following sections:

- [Waveform Data Logging](waveform-data-logging.html)
- [Disturbance Data Logging](disturbance-data-logging.html)
- [Trend Data Logging](trend-data-logging.html)
- [COMTRADE File Format](comtrade-file-format.html)
- [Choosing a File Format](choosing-a-file-format.html)

Related concepts:

- Voltage Events
- Triggers

<!--NI_TOPIC bundle=labview-electrical-power-toolkit path=delta-connections.html language=enus -->
## TOPIC 00020: Delta Connections

- bundle_id: `labview-electrical-power-toolkit`
- source_path: `delta-connections.html`
- source_url: https://docs-be.ni.com/bundle/labview-electrical-power-toolkit/raw/resource/enus/delta-connections.html
- document_id: `labview-electrical-power-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: In a delta connection, transformer coils connect with each other to form a closed loop, with each connection point connecting to incoming wires or to supplying power to loads. The following figure shows a delta connection. In the previous figure, V[AB], V[BC], and V[CA] are the three line voltages.

### Delta Connections

In a delta connection, transformer coils connect with each other to form a closed loop, with each
 connection point connecting to incoming wires or to supplying power to loads. The
 following figure shows a delta connection.

[IMAGE alt='image' src='GUID-E9498DE2-93FF-44CE-86DE-4A7BBB874B1F-a5.gif']

In the previous figure, V<sub>AB</sub>,
 V<sub>BC</sub>, and
 V<sub>CA</sub> are the three line
 voltages. The voltage between any two conductors in a delta connection is the same.

Low voltage distribution systems typically use delta connections. Delta connections offer the
 advantage of high reliability. If one winding fails, the remaining two wires can operate
 as an open delta connection and maintain a full line voltage to loads.

Parent topic:

Connections and Wiring

<!--NI_TOPIC bundle=labview-electrical-power-toolkit path=disturbance-data-logging.html language=enus -->
## TOPIC 00021: Disturbance Data Logging

- bundle_id: `labview-electrical-power-toolkit`
- source_path: `disturbance-data-logging.html`
- source_url: https://docs-be.ni.com/bundle/labview-electrical-power-toolkit/raw/resource/enus/disturbance-data-logging.html
- document_id: `labview-electrical-power-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Disturbance data is useful for the analysis of voltage events, such as voltage dips, swells, and interruptions. Disturbance data includes RMS values for voltage and current, harmonics data, voltage unbalance data, and flagged values. You typically log disturbance data every half cycle or every cycle

### Disturbance Data Logging

Disturbance data is useful for the analysis of voltage events, such as *voltage dips,
 swells, and interruptions*. Disturbance data includes RMS values for voltage
 and current, harmonics data, voltage unbalance data, and flagged values. You typically
 log disturbance data every half cycle or every cycle, over several minutes.

Parent topic:

Data Logging

Related concepts:

- Voltage Dips, Swells, and Interruptions

<!--NI_TOPIC bundle=labview-electrical-power-toolkit path=duration-triggers.html language=enus -->
## TOPIC 00022: Duration Triggers

- bundle_id: `labview-electrical-power-toolkit`
- source_path: `duration-triggers.html`
- source_url: https://docs-be.ni.com/bundle/labview-electrical-power-toolkit/raw/resource/enus/duration-triggers.html
- document_id: `labview-electrical-power-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: A duration trigger includes two triggers with a variable recording length and initiates recording on a rising or falling edge slope. After a duration trigger fires, a disturbance recorder starts to record data for the entire duration of a fault while the trigger remains active. The recording ends wh

### Duration Triggers

A duration trigger includes two triggers with a variable recording length and initiates recording
 on a rising or falling edge slope. After a duration trigger fires, a disturbance
 recorder starts to record data for the entire duration of a fault while the trigger
 remains active. The recording ends when the input signal crosses the trigger threshold
 for a second time. You can specify the amount of pre- and post-trigger data to record.
 The total recording length is equal to the fault duration plus the length of time
 required for recording the specified amount of pre- and post-trigger data. The following
 figure shows duration triggering.

[IMAGE alt='image' src='GUID-623D05D0-0571-4234-9DE1-3FBE3CE400B8-a5.gif']

You can use duration triggers to initiate data recording for voltage dips, swells, interruptions,
 and rapid voltage changes as defined in IEC 61000-4-30:2008. You also can use duration
 triggers to initiate data recording for customized events.

Parent topic:

Triggers

<!--NI_TOPIC bundle=labview-electrical-power-toolkit path=edge-triggers.html language=enus -->
## TOPIC 00023: Edge Triggers

- bundle_id: `labview-electrical-power-toolkit`
- source_path: `edge-triggers.html`
- source_url: https://docs-be.ni.com/bundle/labview-electrical-power-toolkit/raw/resource/enus/edge-triggers.html
- document_id: `labview-electrical-power-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: An edge trigger is a trigger with a specified recording length and initiates recording on a rising or falling edge slope. After an edge trigger fires, a disturbance recorder records data for a specified recording length, after which the recording ends. If a fault lasts for a duration longer than the

### Edge Triggers

An edge trigger is a trigger with a specified recording length and initiates recording on a
 rising or falling edge slope. After an edge trigger fires, a disturbance recorder
 records data for a specified recording length, after which the recording ends. If a
 fault lasts for a duration longer than the specified recording length, the disturbance
 recorder may miss some important power quality data. You can specify the amount of pre-
 and post-trigger data to record. The total recording duration is equal to the specified
 recording length, including the length of time required for recording the specified
 amount of pre- and post-trigger data. The following figure shows edge triggering.

[IMAGE alt='image' src='GUID-84473EA9-BE58-4C36-8233-0BD4BF211797-a5.gif']

You can use edge triggers to initiate data recording for voltage dips, swells, interruptions, and
 rapid voltage changes as defined in IEC 61000-4-30:2008. You also can use edge triggers
 to initiate data recording for customized events.

Parent topic:

Triggers

<!--NI_TOPIC bundle=labview-electrical-power-toolkit path=electric-vehicle-power-measurement.html language=enus -->
## TOPIC 00024: Electric Vehicle Power Measurement

- bundle_id: `labview-electrical-power-toolkit`
- source_path: `electric-vehicle-power-measurement.html`
- source_url: https://docs-be.ni.com/bundle/labview-electrical-power-toolkit/raw/resource/enus/electric-vehicle-power-measurement.html
- document_id: `labview-electrical-power-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: In an electric vehicle, the battery pack supplies DC power to the inverter that converts the DC power to three-phase power. The motor converts three-phase power to mechanical power that propels the electric vehicle forward. The following figure shows the major electric components of a typical electr

### Electric Vehicle Power Measurement

In an electric vehicle, the battery pack supplies DC power to the inverter that converts the DC
 power to three-phase power. The motor converts three-phase power to mechanical power
 that propels the electric vehicle forward. The following figure shows the major electric
 components of a typical electric vehicle.

[IMAGE alt='image' src='GUID-832AB85A-0AB5-4316-AA8F-8E87B3BF3894-a5.png']

You can use the Electrical Power Toolkit to perform power tests on the following components:

- High Voltage Battery —Stores the only source of power that can be converted
 into mechanical energy to propel the electric vehicle. The high-voltage battery is a
 battery pack comprised of smaller battery cells. Because of its importance to the
 overall range of an electric vehicle, the battery pack must be tested many times in
 various environmental conditions, during different stages of aging, and with
 different cell chemistries before it is commissioned for a vehicle.
- Auxiliary Battery —Provides power for many of the conventional components
 distributed throughout an electric vehicle. The auxiliary battery, often 12 V or 48
 V, exists in many internal combustion vehicles.
- Inverter —Converts the DC power from the battery pack to three-phase AC power
 to provide power for the motor. The inverter, also referred to as the traction
 inverter, is one of the power electronics components of an electric vehicle. The
 more efficient the power conversion, the more mileage an electric vehicle can travel
 in a single charge.
- DC/DC Converter —Enables the high-voltage battery pack to charge the auxiliary
 battery when needed.
- Onboard Charger —Converts the power that the electric vehicle supply equipment
 (EVSE) or the power grid supplies to DC power that charges the battery. The onboard
 charger is important in converting energy efficiently so that power is not lost in
 the charging process. The onboard charger is also important for enabling faster
 charging rates.
- Traction Motor —Converts the three-phase AC power supplied and controlled by
 the inverter to mechanical power that propels the electric vehicle. The more
 efficiently the motor converts the three-phase AC power to mechanical power, the
 more mileage an electric vehicle can travel in a single charge.

#### Battery Power Measurement

Battery packs are required to power all aspects of an electric vehicle and determine the range of an electric vehicle per full charge. A battery pack must be rigorously tested to ensure the electric vehicle gets the furthest possible range in all possible driving conditions.

In battery power testing, a battery pack is charged and discharged through simulated drive cycles for multiple times. These simulated drive cycles pull power from the battery pack as if the battery pack is in a real electric vehicle. These tests, which can potentially run for months, are completed in environmental test chambers so that temperature, humidity, and other factors can be simulated as well. Accurate battery power measurement is necessary to ensure that the rated vehicle mileage per full charge is accurate in all conditions so that correct design decisions can be made to improve the possible range or performance of the electric vehicle. Use the *Battery VIs* to perform battery power measurement.

#### Three-Phase Power Measurement

The inverter takes DC power from the battery pack, converts the DC power to three-phase AC power, which drives the motor that propels the electric vehicle forward. The efficiency of the power delivery to the motor affects the range, performance, and customer experience of the electric vehicle.

In inverter efficiency testing, an inverter is tested in multiple drive cycles and different operating conditions. Accurate inverter efficiency is necessary to ensure that the rated vehicle mileage per full charge is accurate in all conditions so that design decisions can be made to the inverter hardware or the control algorithms to improve the possible range or performance of the electric vehicle. Use the *Three Phase Power Measurement VIs* to perform three-phase power measurement.

Related information:

- Battery VIs
- Three Phase Power Measurement
 VIs

<!--NI_TOPIC bundle=labview-electrical-power-toolkit path=electrical-power-grids.html language=enus -->
## TOPIC 00025: Electrical Power Grids

- bundle_id: `labview-electrical-power-toolkit`
- source_path: `electrical-power-grids.html`
- source_url: https://docs-be.ni.com/bundle/labview-electrical-power-toolkit/raw/resource/enus/electrical-power-grids.html
- document_id: `labview-electrical-power-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: An electrical power grid is a network that delivers electricity from power suppliers to consumers. An electrical power grid contains the following three major components: Power generation by power stations Power transmission by utilities Power distribution to end users The following figure shows a t

### Electrical Power Grids

An electrical power grid is a network that delivers electricity from power suppliers to
 consumers. An electrical power grid contains the following three major components:

- Power generation by power stations
- Power transmission by utilities
- Power distribution to end users

The following figure shows a typical electrical power grid.

[IMAGE alt='Diagram of an electrical power grid showing generation, transmission, and distribution.' src='GUID-D85B9761-F7AC-4E22-A477-20EA25DBE501-a5.gif']

Use this section to learn about electrical power grids.

<!--NI_TOPIC bundle=labview-electrical-power-toolkit path=electrical-power-signals.html language=enus -->
## TOPIC 00026: Electrical Power Signals

- bundle_id: `labview-electrical-power-toolkit`
- source_path: `electrical-power-signals.html`
- source_url: https://docs-be.ni.com/bundle/labview-electrical-power-toolkit/raw/resource/enus/electrical-power-signals.html
- document_id: `labview-electrical-power-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use this section to learn about electrical power signals that you can analyze with the LabVIEW Electrical Power Toolkit.

### Electrical Power Signals

Use this section to learn about electrical power signals that you can analyze with the
 LabVIEW Electrical Power Toolkit.

- [Voltage and Current Signals](voltage-and-current-signals.html)
- [Connections and Wiring](connections-and-wiring.html)
- [Measuring Signals](measuring-signals.html)
- [Magnitude of Voltage and Current](magnitude-of-voltage-and-current.html)
- [Frequency](frequency.html)

<!--NI_TOPIC bundle=labview-electrical-power-toolkit path=energy-measurement.html language=enus -->
## TOPIC 00027: Energy Measurement

- bundle_id: `labview-electrical-power-toolkit`
- source_path: `energy-measurement.html`
- source_url: https://docs-be.ni.com/bundle/labview-electrical-power-toolkit/raw/resource/enus/energy-measurement.html
- document_id: `labview-electrical-power-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Energy is the amount of power during a period of duration. If you measure power in kilowatts and measure time in hours, the unit of electrical energy is kilowatt-hour (kWh). Kilowatt-hour is the standard unit of energy that electricity meters use to calculate the amount of electrical energy. One kil

### Energy Measurement

Energy is the amount of power during a period of duration. If you measure power in kilowatts and
 measure time in hours, the unit of electrical energy is kilowatt-hour (kWh).
 Kilowatt-hour is the standard unit of energy that electricity meters use to calculate
 the amount of electrical energy. One kilowatt-hour is the amount of electricity that a
 device rated at 1,000 watts uses in one hour. For example, if you switch on an electric
 fire with an element rated at 1,000 watts and leave it on for one hour you use one
 kilowatt-hour of electricity. Use the following equation to calculate energy.

E = PT

where P is the power and T is the duration.

You can use the LabVIEW Electrical Power Toolkit to calculate active energy, reactive energy, and
 apparent energy.

Parent topic:

Power & Energy Measurement

<!--NI_TOPIC bundle=labview-electrical-power-toolkit path=evaluation-standards.html language=enus -->
## TOPIC 00028: Evaluation Standards

- bundle_id: `labview-electrical-power-toolkit`
- source_path: `evaluation-standards.html`
- source_url: https://docs-be.ni.com/bundle/labview-electrical-power-toolkit/raw/resource/enus/evaluation-standards.html
- document_id: `labview-electrical-power-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Electrical utilities and end users need power quality evaluation standards to protect electrical power systems from malfunctioning or failing. Power quality evaluation standards help electrical utilities prevent electrical disturbances from affecting the operation of equipment that end users and ele

### Evaluation Standards

Electrical utilities and end users need power quality evaluation standards to protect electrical
 power systems from malfunctioning or failing. Power quality evaluation standards help
 electrical utilities prevent electrical disturbances from affecting the operation of
 equipment that end users and electrical utilities own. End users use power quality
 evaluation standards to prevent user-generated electrical disturbances from affecting
 the operation of equipment that end users and electrical utilities own.

EN 50160:2007 defines the limits within which voltage characteristics of electricity can remain
 normal operations over public distribution networks. The European Union is the leader in
 using EN 50160:2007 to implement supply quality standards. Several countries use EN
 50160:2007 as the basis of their national regulations about supply quality.

EN 50160:2007 defines the following characteristics of a supply voltage:

- Power frequency.
- Magnitude of the supply voltage.
- Supply voltage variations.
- Rapid voltage changes and flickers.
- Supply voltage dips.
- Short interruptions of the supply voltage.
- Long interruptions of the supply voltage.
- Temporary power frequency overvoltages.
- Transient overvoltages.
- Supply voltage unbalance.
- Harmonic voltage.
- Interharmonic voltage.
- Mains signaling voltage.

EN 50160:2007 specifies that each characteristic must not exceed defined limits for a specific
 period. For example, when you measure fundamental frequency over 10 seconds for
 electrical power systems with a synchronous connection to an interconnected electrical
 power system, 99.5% of the fundamental frequency measurements of a year must be within
 the range of 49.5 Hz to 50.5 Hz under normal operating conditions.

Parent topic:

Power Quality

Related concepts:

- Time Aggregation

<!--NI_TOPIC bundle=labview-electrical-power-toolkit path=events-indexes.html language=enus -->
## TOPIC 00029: Events Indexes

- bundle_id: `labview-electrical-power-toolkit`
- source_path: `events-indexes.html`
- source_url: https://docs-be.ni.com/bundle/labview-electrical-power-toolkit/raw/resource/enus/events-indexes.html
- document_id: `labview-electrical-power-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Indexes quantify the severity and frequency of voltage events in the analysis of electrical power systems. Site indexes quantify the power quality at a specific geographical location. Typically, site indexed show the number of events within a specified range of voltage magnitude and duration for a g

### Events Indexes

Indexes quantify the severity and frequency of voltage events in the analysis of electrical power
 systems. Site indexes quantify the power quality at a specific geographical location.
 Typically, site indexed show the number of events within a specified range of voltage
 magnitude and duration for a given time period. Aggregate site indexes to form system indexes.
 System indexes quantify the power quality across an entire electrical power system or
 grid.

The most commonly used index for voltage dips is the *System Average RMS Variation Frequency
 Index (SARFI)*. SAFRI quantifies the measurement period, the number of voltage dips,
 and the number of affected users for a specified voltage range. For example, SARFI-70 measures
 the average number of voltage dips per customer. The measurement occurs during the measurement
 period when the voltage magnitude drops below 70% of the nominal or sliding reference
 value.

SARFI-ITIC (CBEMA) is commonly used for most electrical equipment. SARFI-ITIC (CBEMA) measures
 voltage events that go beyond the limits set by the *Information Technology Industry
 Council (ITI)*. ITI previously was the *Computer & Business Equipment
 Manufacturer’s Association (CBEMA)*.

SARFI-SEMI is typically used for electrical equipment in the semiconductor industry, which
 quantifies voltage events that exceed the values specified by the Semiconductor
 Equipment and Materials International (SEMI) F47.

Parent topic:

Voltage Events

<!--NI_TOPIC bundle=labview-electrical-power-toolkit path=flagging.html language=enus -->
## TOPIC 00030: Flagging

- bundle_id: `labview-electrical-power-toolkit`
- source_path: `flagging.html`
- source_url: https://docs-be.ni.com/bundle/labview-electrical-power-toolkit/raw/resource/enus/flagging.html
- document_id: `labview-electrical-power-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: IEC 61000-4-30:2008 defines conditions of flagging. If a voltage event occurs, the 10/12-cycle block in which the event occurs is flagged. If a given interval contains a flagged value, the aggregated value for that interval also is flagged, indicating that the aggregated value may be unreliable.The

### Flagging

IEC 61000-4-30:2008 defines conditions of flagging. If a voltage event occurs, the 10/12-cycle
 block in which the event occurs is flagged. If a given interval contains a flagged
 value, the *aggregated value* for that interval also is flagged, indicating
 that the aggregated value may be unreliable.

The LabVIEW Electrical Power Toolkit complies with IEC 61000-4-30:2008 and supports flagging for
 the following measurements:

- Frequency.
- Voltage magnitude.
- Harmonics and interharmonics.
- Flicker.
- Unbalance.
- Signaling.
- Underdeviation and overdeviation.

If any of the previous measured values are flagged, the aggregated value that includes the
 measured values also is flagged.

Parent topic:

Voltage Events

Related concepts:

- Time Aggregation

<!--NI_TOPIC bundle=labview-electrical-power-toolkit path=flickers.html language=enus -->
## TOPIC 00031: Flickers

- bundle_id: `labview-electrical-power-toolkit`
- source_path: `flickers.html`
- source_url: https://docs-be.ni.com/bundle/labview-electrical-power-toolkit/raw/resource/enus/flickers.html
- document_id: `labview-electrical-power-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use this section to learn about methods for obtaining voltage fluctuation data that you can analyze with the LabVIEW Electrical Power Toolkit. This section also introduces flickermeter standards for evaluating light flickers.Flickers are the results of voltage fluctuations. Voltage fluctuations caus

### Flickers

Use this section to learn about methods for obtaining voltage fluctuation data that you
 can analyze with the LabVIEW Electrical Power Toolkit. This section also introduces flickermeter
 standards for evaluating light flickers.

Flickers are the results of voltage fluctuations. Voltage fluctuations cause light flickers.
 Voltage fluctuations can also cause flickers in sensitive electronic equipment such as
 television receivers or in industrial processes that rely on constant electrical
 power.

- [Voltage Fluctuations](voltage-fluctuations.html)
- [Light Flickers](light-flickers.html)
- [Measuring Flickers](measuring-flickers.html)

Related concepts:

- Aggregation Intervals

<!--NI_TOPIC bundle=labview-electrical-power-toolkit path=frequency.html language=enus -->
## TOPIC 00032: Frequency

- bundle_id: `labview-electrical-power-toolkit`
- source_path: `frequency.html`
- source_url: https://docs-be.ni.com/bundle/labview-electrical-power-toolkit/raw/resource/enus/frequency.html
- document_id: `labview-electrical-power-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Frequency is the number of cycles per second in an AC waveform. Synchronous generators provide electrical power to an electrical power grid and the rotational speed of synchronous generators determines the line frequency. AC electrical power transmits across electrical power grids at a line frequenc

### Frequency

Frequency is the number of cycles per second in an AC waveform. Synchronous generators provide
 electrical power to an electrical power grid and the rotational speed of synchronous
 generators determines the line frequency. AC electrical power transmits across
 electrical power grids at a line frequency of 50 Hz or 60 Hz. The advantage of having a
 standardized frequency is that multiple generators can connect to one grid and operate
 in parallel.

The LabVIEW Electrical Power Toolkit complies with IEC 61000-4-30:2008 for frequency measurement.
 The Electrical Power Toolkit specifies to measure frequency values every 10 second and
 the measurement periods are non-overlapping. The Electrical Power Toolkit discards a
 cycle if variations in the fundamental frequency cause the individual cycle to overlap a
 real-time clock (RTC) 10 seconds tick. Because multiple zero crossings cause frequency
 distortions, the Electrical Power Toolkit attenuates harmonic and interharmonic
 frequency components prior to measuring the fundamental frequency in order to minimize
 frequency distortions.

Parent topic:

Electrical Power Signals

<!--NI_TOPIC bundle=labview-electrical-power-toolkit path=gain-calibration.html language=enus -->
## TOPIC 00033: Gain Calibration

- bundle_id: `labview-electrical-power-toolkit`
- source_path: `gain-calibration.html`
- source_url: https://docs-be.ni.com/bundle/labview-electrical-power-toolkit/raw/resource/enus/gain-calibration.html
- document_id: `labview-electrical-power-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Gain is the degree of increase in the power or amplitude of a signal from the input to the output. In power quality measurement, it is more useful to quantify the gain from sensor to digitization than to quantify the gain of each component in a measurement instrument. You calibrate all the component

### Gain Calibration

Gain is the degree of increase in the power or amplitude of a signal from the input to the
 output. In power quality measurement, it is more useful to quantify the gain from sensor
 to digitization than to quantify the gain of each component in a measurement instrument.
 You calibrate all the components including sensors, amplifiers, and data acquisition
 devices in order to produce the most accurate measurements. You also need to calibrate
 several times for different range percentages to reduce nonlinearity of transducers over
 a wide measurement range.

To calibrate gains, you first use a standard signal generator to generate sinusoidal signals with
 known precise amplitude and then use the measurement instrument to measure the
 sinusoidal signals. You get the gain values by comparing the measured amplitude results
 with the standard sinusoidal signals. In future measurement, you multiply the gain
 values with the original signals you measure to ensure accurate measurements.

Parent topic:

Performing Calibration

<!--NI_TOPIC bundle=labview-electrical-power-toolkit path=harmonics-and-interharmonics.html language=enus -->
## TOPIC 00034: Harmonics and Interharmonics

- bundle_id: `labview-electrical-power-toolkit`
- source_path: `harmonics-and-interharmonics.html`
- source_url: https://docs-be.ni.com/bundle/labview-electrical-power-toolkit/raw/resource/enus/harmonics-and-interharmonics.html
- document_id: `labview-electrical-power-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: In theory, electrical generators produce power with sinusoidal voltage and current waveforms that oscillate at the line frequency. The line frequency is usually 50 Hz or 60 Hz. In practice, voltage and current waveforms are not sinusoidal, especially when nonlinear loads are present, but are distort

### Harmonics and Interharmonics

In theory, electrical generators produce power with sinusoidal voltage and current waveforms that
 oscillate at the line frequency. The line frequency is usually 50 Hz or 60 Hz. In
 practice, voltage and current waveforms are not sinusoidal, especially when nonlinear
 loads are present, but are distorted because of the presence of harmonics.

Harmonics are components of a periodic waveform that oscillate with a frequency that is an
 integer multiple of the line frequency. For a 60 Hz electrical power system, the second
 harmonic is 120 Hz, the fifth harmonic is 300 Hz, and so on. Components with frequencies
 that are between these harmonics are called interharmonics. For a 60 Hz system, a
 component with a frequency of 150 Hz is an interharmonic that exists between the second
 and third harmonics.

The most common sources of current harmonics are rectifiers and inverters, which consist of
 diodes that convert AC voltages to DC voltages and vice versa. Other sources of current
 harmonics include variable speed drives, fluorescent lighting, arc furnaces, and
 semiconductor devices. Such devices also can lead to variations in the amplitude and/or
 phase of the fundamental and harmonic components, giving rise to interharmonics.

Harmonics can cause power to dissipate as heat. Harmonics at higher frequencies can lead to more
 power dissipation, which can damage electrical components permanently.

Interharmonics can lead to interruption of ripple control devices that use signaling voltages
 with interharmonic frequencies. Interharmonics also can cause increased noise,
 especially in audio equipment, and additional stresses on motors and generators.

#### Triplen Harmonics

Triplen harmonics are odd integer multiples of the 3rd harmonic: 3rd, 9th, 15th, 21st, and so on. In a three-phase electrical power system, where there is a 120 degrees phase difference, triplen harmonics are additive in the neutral conductor, as shown in the following figure.

[IMAGE alt='image' src='GUID-F2B5D9DA-F1FD-4784-AEA1-6C1EC98FF2EE-a5.gif']

Triplen harmonics can lead to large currents in the neutral conductor, resulting in significant overheating of wires and components, especially three-phase delta transformers.

Parent topic:

Harmonics

<!--NI_TOPIC bundle=labview-electrical-power-toolkit path=harmonics.html language=enus -->
## TOPIC 00035: Harmonics

- bundle_id: `labview-electrical-power-toolkit`
- source_path: `harmonics.html`
- source_url: https://docs-be.ni.com/bundle/labview-electrical-power-toolkit/raw/resource/enus/harmonics.html
- document_id: `labview-electrical-power-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use this section to learn about methods for obtaining voltage harmonics and interharmonics data that you can analyze with the LabVIEW Electrical Power Toolkit.The Electrical Power Toolkit complies with IEC 61000-4-7:2009 and Class A of IEC 61000-4-30:2008 for measuring harmonics.

### Harmonics

Use this section to learn about methods for obtaining voltage harmonics and
 interharmonics data that you can analyze with the LabVIEW Electrical Power Toolkit.

The Electrical Power Toolkit complies with IEC 61000-4-7:2009 and Class A of
 IEC 61000-4-30:2008 for measuring harmonics.

- [Harmonics and Interharmonics](harmonics-and-interharmonics.html)
- [Measuring Harmonics](measuring-harmonics.html)
- [Total Harmonic Distortion](total-harmonic-distortion.html)

Related concepts:

- Spectrum Calibration

<!--NI_TOPIC bundle=labview-electrical-power-toolkit path=hysteresis.html language=enus -->
## TOPIC 00036: Hysteresis

- bundle_id: `labview-electrical-power-toolkit`
- source_path: `hysteresis.html`
- source_url: https://docs-be.ni.com/bundle/labview-electrical-power-toolkit/raw/resource/enus/hysteresis.html
- document_id: `labview-electrical-power-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Hysteresis is a secondary trigger threshold. The LabVIEW Electrical Power Toolkit uses hysteresis to reduce false triggering on noisy signals. A trigger occurs only when an input signal crosses both the trigger threshold and the hysteresis threshold in the correct order. When an input signal crosses

### Hysteresis

Hysteresis is a secondary trigger threshold. The LabVIEW Electrical Power Toolkit uses hysteresis
 to reduce false triggering on noisy signals. A trigger occurs only when an input signal
 crosses both the trigger threshold and the hysteresis threshold in the correct order. When an
 input signal crosses the trigger threshold, the system arms a trigger. A trigger fires only
 when the trigger is armed and the input signal crosses the hysteresis threshold.

For a rising edge slope, an input signal must cross a trigger threshold plus a hysteresis
 threshold for a trigger to fire. For a falling edge slope, an input signal must cross a
 trigger threshold minus a hysteresis threshold for a trigger to fire.

The following figure shows a noisy input signal crossing a trigger threshold in a rising edge
 slope for multiple times in a single cycle.

[IMAGE alt='Waveform graph showing a noisy input signal crossing a trigger threshold multiple times.' src='GUID-A0A65709-B29D-4A8C-8637-4651090810FD-a5.gif']

In the previous figure, the four arrows indicate triggering points of four crossings. The three
 crossings on the left do not represent a true power quality disturbance but are the
 result of noise. Only the one crossing on the right represents a true power quality
 disturbance. The following figure shows the same input signal. However, a hysteresis
 threshold is specified in addition to the trigger threshold.

[IMAGE alt='Waveform graph showing input signal with trigger and hysteresis thresholds.' src='GUID-1FE343EE-7DBE-433D-9FFB-4DA073B2B4B7-a5.gif']

In the previous figure, the input signal first crosses the trigger threshold multiple times,
 which arms but does not fire a trigger. The trigger fires only when the input signal finally
 crosses the hysteresis threshold after crossing the trigger threshold. The arrow indicates the
 trigger.

In the following figure, an input signal stays above the trigger threshold and crosses only the
 hysteresis threshold. The trigger is neither armed nor fired.

[IMAGE alt='image' src='GUID-F1F2AD91-8269-4B68-88CD-B74E40280BBB-a5.gif']

You also can specify a time delay as the hysteresis. For example, a trigger activates when an
 input signal crosses the trigger threshold. The imput signal must remain above or below that
 threshold for a duration equal to or longer than the specified time delay.

Parent topic:

Triggers

<!--NI_TOPIC bundle=labview-electrical-power-toolkit path=light-flickers.html language=enus -->
## TOPIC 00037: Light Flickers

- bundle_id: `labview-electrical-power-toolkit`
- source_path: `light-flickers.html`
- source_url: https://docs-be.ni.com/bundle/labview-electrical-power-toolkit/raw/resource/enus/light-flickers.html
- document_id: `labview-electrical-power-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Light flickers, as a result of rapid voltage fluctuations, are visible changes in the brightness of a lamp. Rapid voltage fluctuations is the result of a changing load current that occurs at subharmonic frequencies less than 25 Hz.An incandescent lamp consists of a tungsten filament sealed inside a

### Light Flickers

Light flickers, as a result of rapid voltage fluctuations, are visible changes in the brightness
 of a lamp. Rapid voltage fluctuations is the result of a changing load current that
 occurs at subharmonic frequencies less than 25 Hz.

An incandescent lamp consists of a tungsten filament sealed inside a glass bulb with an inert
 gas. When a current flows through the filament, the temperature of the tungsten rises
 and reaches a value that is high enough to cause emission of light. If the temperature
 of the filament remains steady, the lamp emits light at a constant intensity. Voltage
 fluctuations cause the current in the filament to change, which leads to temperature
 variations. The resulting change in temperature causes fluctuations in the intensity of
 the light that the lamp emits.

Observable fluctuations in light intensity may be annoying and even lead to psychological stress
 for a human being. The frequency at which light changes is important for measuring
 flickers. If the frequency is too low, an observer notices the corresponding slow
 changes over time instead of perceiving the changes as flickers. If the frequency is too
 high, the light intensity appears continuous and the observer is unaware of the
 flickers.

A flicker curve shows voltage fluctuations that lead to observable changes in light intensity as
 a function of the fluctuation frequency. Flicker curves are derived from controlled
 experiments measuring the human perception of fluctuations in light intensity. The
 following figure shows the flicker curve of a 60 W and 120 V incandescent bulb.

[IMAGE alt='image' src='GUID-1EAF18FD-EE65-4E37-A1F7-72F4079663ED-a5.gif']

In the previous figure, a voltage fluctuation of 0.2% at 8.8 Hz results in an observable flicker.
 Electrical utilities must ensure that the frequencies of voltage fluctuations are above
 or below the flicker curve for a specific light source. The critical flicker frequency
 corresponds to the frequency at which observers no longer perceive light as continuous
 but notice flickers.

Lamps that operate at a power that is higher than 60 W contain a thicker filament, which can
 support a higher current. Such lamps are less sensitive to voltage fluctuations because
 the lamps have a higher thermal constant and, consequently, are less likely to exhibit
 light flickers. These types of lamps include luminescent lamps and LEDs. Luminescent
 lamps use an electric current to ionize a gas or vapor, which emits light. Examples of
 luminescent lamps are fluorescent lamps, sodium-vapor lamps, and mercury-vapor lamps.
 Luminescent lamps usually are less sensitive to voltage fluctuations than incandescent
 lamps. The following figure shows the lamp-eye-brain response for an incandescent lamp,
 a magnetic ballast fluorescent lamp, and an electronic ballast fluorescent lamp.

[IMAGE alt='image' src='GUID-E2554E3E-3665-4151-AA44-F9FC23659B56-a5.gif']

Parent topic:

Flickers

<!--NI_TOPIC bundle=labview-electrical-power-toolkit path=line-and-bus-configurations.html language=enus -->
## TOPIC 00038: Line and Bus Configurations

- bundle_id: `labview-electrical-power-toolkit`
- source_path: `line-and-bus-configurations.html`
- source_url: https://docs-be.ni.com/bundle/labview-electrical-power-toolkit/raw/resource/enus/line-and-bus-configurations.html
- document_id: `labview-electrical-power-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Lines and buses are basic components of a power substation. Lines load power for transmission and distribution. Each line has different wiring methods. Buses connect lines, concentrating the power from the incoming lines and distributing the power to the outgoing lines.A power substation can have an

### Line and Bus Configurations

Lines and buses are basic components of a power substation. Lines load power for
 *transmission* and *distribution*. Each line has different
 *wiring* methods. Buses connect lines, concentrating the power from the
 incoming lines and distributing the power to the outgoing lines.

A power substation can have any of the following line and bus configurations:

- Single-bus single-line configuration.
- Single-bus multiple-line configuration.
- Multiple-bus configuration.

#### Single-Bus Single-Line Configuration

In the single-bus single-line configuration, a single bus connects to a single line. This configuration supports measuring power signals that pass through the single bus and the single line.

#### Single-Bus Multiple-Line Configuration

In the single-bus multiple-line configuration, a single bus connects to multiple lines. This configuration supports measuring power signals that pass through the single bus and multiple lines. The nominal voltages of different lines across one bus are the same, but the currents can be different. The following figure shows a typical single-bus multiple-line configuration.

[IMAGE alt='image' src='GUID-A1734BF7-B8D7-4B0B-A190-A6BB03CEB4E6-a5.gif']

#### Multiple-Bus Configuration

In the multiple-bus configuration, the power substation has multiple buses. Each
 incoming or outgoing line connects to any number of buses. This configuration
 supports measuring power signals that pass through multiple buses. The voltages and
 currents of different buses can be different. The following figure shows a typical
 multiple-bus configuration.

[IMAGE alt='image' src='GUID-DEBEC52B-84BA-443F-9725-57DD94B541F0-a5.gif']

Related concepts:

- Power Transmission
- Power Distribution
- Connections and Wiring

<!--NI_TOPIC bundle=labview-electrical-power-toolkit path=magnitude-of-voltage-and-current.html language=enus -->
## TOPIC 00039: Magnitude of Voltage and Current

- bundle_id: `labview-electrical-power-toolkit`
- source_path: `magnitude-of-voltage-and-current.html`
- source_url: https://docs-be.ni.com/bundle/labview-electrical-power-toolkit/raw/resource/enus/magnitude-of-voltage-and-current.html
- document_id: `labview-electrical-power-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: A root mean square (RMS) voltage/current equals the DC voltage/current that produces the same amount of power transfer in a conductor or the same amount of power dissipation in a load. For sinusoidal waveforms, the RMS voltage/current value is half of the multiplication result of the square root of

### Magnitude of Voltage and Current

A root mean square (RMS) voltage/current equals the DC voltage/current that produces the same
 amount of power transfer in a conductor or the same amount of power dissipation in a
 load. For sinusoidal waveforms, the RMS voltage/current value is half of the
 multiplication result of the square root of two timing peak voltage/current. The LabVIEW
 Electrical Power Toolkit complies with IEC 61000-4-30:2008 for magnitude measurement.
 The Electrical Power Toolkit specifies to measure voltage and current signals over a
 10-cycle interval for a 50 Hz electrical power system and a 12-cycle interval for a 60
 Hz electrical power system. The measured values are RMS voltage and current values. The
 10/12-cycle blocks are gapless and not overlapping, with a subsequent block commencing
 at the point where the previous block ends.

Parent topic:

Electrical Power Signals

<!--NI_TOPIC bundle=labview-electrical-power-toolkit path=measurement-standards.html language=enus -->
## TOPIC 00040: Measurement Standards

- bundle_id: `labview-electrical-power-toolkit`
- source_path: `measurement-standards.html`
- source_url: https://docs-be.ni.com/bundle/labview-electrical-power-toolkit/raw/resource/enus/measurement-standards.html
- document_id: `labview-electrical-power-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Power quality measurement standards define measurement methods of power quality parameters. The power quality measurement standards that the LabVIEW Electrical Power Toolkit complies with are IEC power quality standards. IEC power quality standards are also called electromagnetic compatibility (EMC)

### Measurement Standards

Power quality measurement standards define measurement methods of power quality parameters. The
 power quality measurement standards that the LabVIEW Electrical Power Toolkit complies
 with are IEC power quality standards. IEC power quality standards are also called
 electromagnetic compatibility (EMC) standards, which means these standards are more
 concerned about the compatibility between equipment of end users and equipment of
 utilities.

The Electrical Power Toolkit complies with the following IEC power quality standards:

- IEC 61000-4-7:2009, Electromagnetic Compatibility (EMC) - Part 4-7: Testing and Measurement
 Techniques - General Guide on Harmonics and Interharmonics Measurements and
 Instrumentation, for Power Supply Systems and Equipment Connected Thereto.
- IEC 61000-4-15:2010, Electromagnetic Compatibility (EMC) - Part 4-15: Testing and Measurement
 Techniques - Flickermeter - Functional and Design Specifications.
- IEC 61000-4-30:2008, Electromagnetic Compatibility (EMC) - Part 4-30: Testing and Measurement
 Techniques - Power Quality Measurement Methods.

The following table lists measurement methods and aggregation methods in IEC 61000-4-30:2008,
 with which the Electrical Power Toolkit complies.

| Power Quality Parameters | Measurement Method | Aggregation Method |
| --- | --- | --- |
| Power frequency | Class A | No requirement |
| Magnitude of the supply voltage | Class A | Class S |
| Flicker | IEC 61000-4-15:2010 | IEC 61000-4-15:2010 |
| Supply voltage dips and swells | Class A | No requirement |
| Voltage interruptions | Class A | No requirement |
| Supply voltage unbalance | Class A | Class S |
| Voltage harmonics | Class A | Class S |
| Voltage interharmonics | Class A | Class S |
| Mains signaling voltage on the supply voltage | Class A | No requirement |
| Rapid voltage changes | No requirement | Not applicable |
| Measurement of underdeviation and overdeviation | Class A | Class S |

IEC 61000-4-30:2008 is a performance specification instead of a design specification. Refer to
 the standard for detailed information.

Parent topic:

Power Quality

<!--NI_TOPIC bundle=labview-electrical-power-toolkit path=measuring-flickers.html language=enus -->
## TOPIC 00041: Measuring Flickers

- bundle_id: `labview-electrical-power-toolkit`
- source_path: `measuring-flickers.html`
- source_url: https://docs-be.ni.com/bundle/labview-electrical-power-toolkit/raw/resource/enus/measuring-flickers.html
- document_id: `labview-electrical-power-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The LabVIEW Electrical Power Toolkit complies with Class A of IEC 61000-4-15:2010 for measuring flickers. The Electrical Power Toolkit provides flicker measurement for the following systems: 60 W 120 V 50 Hz 60 W 230 V 50 Hz 60 W 120 V 60 Hz 60 W 230 V 60 Hz A flickermeter consists of several functi

### Measuring Flickers

The LabVIEW Electrical Power Toolkit complies with Class A of IEC
 61000-4-15:2010 for measuring flickers. The Electrical Power Toolkit
 provides flicker measurement for the following systems:

- 60 W 
 120 V 
 50 Hz
- 60 W 
 230 V 
 50 Hz
- 60 W 
 120 V 
 60 Hz
- 60 W 
 230 V 
 60 Hz

A flickermeter consists of several function blocks that simulate an incandescent lamp and the
 eye-brain response of the human perception system. The flickermeter standard has
 replaced the use of flicker curves in the evaluation of voltage fluctuations.
 Flickermeters calculate the short-term and long-term flicker for a voltage fluctuation
 waveform. Refer to IEC 61000-4-15:2010 for details about the
 filtering parameters of the function blocks. Using a flickermeter contains the following
 five stages:

1. Voltage adaptation — Scale the input voltage so that the RMS output
 voltage maintains at a constant long-term average. While preserving voltage
 fluctuations on the waveform, voltage adaptation enables flicker calculation to be
 independent of the input voltage.
2. Square multiplier — Extract the amplitude modulation,
 m ( t ), from the input voltage waveform. The
 following equation defines the input voltage waveform: v
 (
 t
 )
 =
 2
 V
 ×
 [
 1
 +
 m
 (
 t
 )
 ]
 ×
 cos
 (
 2
 π
 f
 0
 t
 ) 
 Square the previous equation to calculate the squared voltage waveform, as shown
 in the following equation: v
 (
 t
 )
 2
 =
 2
 V
 2
 ×
 [
 1
 +
 2
 m
 (
 t
 )
 +
 m
 (
 t
 )
 2
 ]
 ×
 1
 2
 +
 1
 2
 cos
 (
 4
 π
 f
 0
 t
 )
3. Weighting filters — Weighting filters include a lowpass
 filter, a highpass filter, and a bandpass filter with a center frequency of 8.8 Hz. The lowpass filter, highpass filter, and
 square multiplier work together as a demodulator. The lowpass filter first
 removes the double-frequency term from the squared voltage waveform. The
 highpass filter then eliminates the DC components. The following equation
 describes the filtered voltage: v(t) =
 2V<sup>2</sup>m(t)
 +
 V<sup>2</sup>m(t)<sup>2</sup> 
 Because m(t) ≤ 1 for small voltage
 fluctuations, you can ignore the second term
 V<sup>2</sup>m(t)<sup>2</sup>
 in the previous equation. You can approximate a voltage signal for small
 fluctuations as
 2V<sup>2</sup>m(t).The
 bandpass filter simulates the frequency response of the eyes and brain. This
 bandpass filter returns the following scaled and phase-shifted modulation signal: m
 '
 (
 t
 )
 =
 2
 ⁢
 ν
 2
 ⁢
 M
 F
 (
 f
 M
 )
 ⁢
 cos
 (
 2
 ⁢
 π
 ⁢
 f
 M
 ⁢
 t
 +
 φ
 '
 M
 )
4. Squaring and smoothing — Use squaring and smoothing to simulate the
 storage effect in the brain and to obtain the instantaneous flicker value. The
 squaring multiplier returns the following squared modulation signal: m
 '
 (
 t
 )
 2
 =
 2
 ⁢
 ν
 4
 ⁢
 [
 M
 F
 (
 f
 M
 )
 ]
 2
 +
 2
 ⁢
 ν
 4
 ⁢
 [
 M
 F
 (
 f
 M
 )
 ]
 2
 ⁢
 cos
 (
 4
 ⁢
 π
 ⁢
 f
 M
 ⁢
 t
 +
 2
 ⁢
 φ
 '
 M
 ) The lowpass filter removes the second term in the previous
 equation and returns the instantaneous flicker value: P
 =
 2
 ⁢
 V
 4
 ⁢
 [
 M
 F
 (
 f
 M
 )
 ]
 2 The instantaneous flicker value is normalized because of the
 voltage adaptation and different minimum human perception of fluctuations at
 different modulation frequencies. An instantaneous flicker value of 1.0 represents
 the threshold above which 50% of observers can notice the flickering of a 60 W and 230 V incandescent lamp.
5. Statistical analysis — Perform statistical processing on the
 instantaneous flicker value to calculate the short-term and long-term flicker
 values. Refer to IEC 61000-4-15:2010 for details about
 calculating short-term and long-term flicker values. You can use the short-term
 flicker value to evaluate the degree of irritation for voltage fluctuations. A
 short-term flicker value of 1.0 represents the level below which complaints about
 flicker are unlikely to arise. A short-term flicker value greater than 1.0 indicates
 that voltage fluctuations are observable and likely to lead to complaints. You can
 use the long-term flicker value to evaluate the combined effect of flicker-causing
 loads over long periods. A long-term flicker value of 0.8 represents the level below
 which complaints about flicker are unlikely to arise.

Note

You can apply the flickermeter standard to other types of lamps by separating the lamp response
 from the eye-brain response. You can modify the bandpass filters in Stage 3 to simulate
 different types of lamps, without modifying other stages.

Parent topic:

Flickers

<!--NI_TOPIC bundle=labview-electrical-power-toolkit path=measuring-harmonics.html language=enus -->
## TOPIC 00042: Measuring Harmonics

- bundle_id: `labview-electrical-power-toolkit`
- source_path: `measuring-harmonics.html`
- source_url: https://docs-be.ni.com/bundle/labview-electrical-power-toolkit/raw/resource/enus/measuring-harmonics.html
- document_id: `labview-electrical-power-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The number of samples per cycle determines the maximum order in harmonics measurement, as the following equation shows: maximum harmonic order = number of samples per cycle 2 Class A of IEC 61000-4-30:2008 requires the measuring of harmonics up to the 50th order. The LabVIEW Electrical Power Toolkit

### Measuring Harmonics

The number of samples per cycle determines the maximum order in harmonics measurement, as the
 following equation shows:

maximum harmonic order

=

number of samples per cycle

2

IEC 61000-4-30:2008

- Using a 10-cycle interval for a 50 Hz electrical power system
- Using a 12-cycle interval for a 60 Hz electrical power system

Measuring harmonics usually contains the following two stages:

1. Discrete Fourier Transform A discrete Fourier transform (DFT) processor calculates the Fourier transform components for a voltage waveform or a current waveform. You can use the LabVIEW Electrical Power Toolkit to break down voltage waveforms and current waveforms into harmonic components.
2. Grouping The LabVIEW Electrical Power Toolkit returns the frequency spectra of voltage waveforms and current waveforms by performing a fast Fourier transform (FFT) on the time-domain data. The Electrical Power Toolkit groups the spectral components and analyzes the resulting harmonic and interharmonic groups or subgroups according to IEC 61000-4-7:2009.

Parent topic:

Harmonics

<!--NI_TOPIC bundle=labview-electrical-power-toolkit path=measuring-signaling-voltages.html language=enus -->
## TOPIC 00043: Measuring Signaling Voltages

- bundle_id: `labview-electrical-power-toolkit`
- source_path: `measuring-signaling-voltages.html`
- source_url: https://docs-be.ni.com/bundle/labview-electrical-power-toolkit/raw/resource/enus/measuring-signaling-voltages.html
- document_id: `labview-electrical-power-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The LabVIEW Electrical Power Toolkit complies with Class A of IEC 61000-4-30:2008 for the measurement of signaling voltages at frequencies below 3 kHz. Class A of IEC 61000-4-30:2008 specifies a measurement interval of 10 cycles for a 50 Hz electrical power system and 12 cycles for a 60 Hz electrica

### Measuring Signaling Voltages

The LabVIEW Electrical Power Toolkit complies with Class A of IEC 61000-4-30:2008 for the
 measurement of signaling voltages at frequencies below 3 kHz. Class A of IEC
 61000-4-30:2008 specifies a measurement interval of 10 cycles for a 50 Hz electrical
 power system and 12 cycles for a 60 Hz electrical power system. If the actual frequency
 is equal to the nominal value, the LabVIEW Electrical Power Toolkit has a frequency
 resolution of 5 Hz after performing *discrete Fourier transform (DFT)*.

If the specified frequency is at the center of a DFT bin, the measurement uses the corresponding
 10/12-cycle RMS value interharmonic bin. The following figure shows the 10/12-cycle RMS
 value interharmonic bin for measuring a signaling voltage at a specified frequency of
 305 Hz.

[IMAGE alt='image' src='GUID-70A13EF3-5790-4B70-A970-D2EE92B3928D-a5.gif']

If the specified frequency is not at the center of a DFT bin, the measurement uses the root of
 the sum of the squares of the four nearest 10/12-cycle RMS value interharmonic bins. The
 following figure shows the 10/12-cycle RMS value interharmonic bins for measuring a
 signaling voltage at a specified frequency of 314.4 Hz.

[IMAGE alt='image' src='GUID-F7449A46-07BC-4C44-864F-D57536FA8834-a5.gif']

In the previous figure, the nearest interharmonic bins to the specified frequency are the 305 Hz,
 310 Hz, 315 Hz, and 320 Hz bins. Therefore, you can use the following equation to
 calculate the signaling voltage:

[IMAGE alt='image' src='GUID-62386286-C4C2-40E0-900F-CC06F410C27B-a5.gif']

where C<sub>i</sub> is the RMS value i
 Hz interharmonic bin.

To receive a signaling message, you must specify a detection threshold, a recording period, and
 the time length of one and zero in the synchronous code. A measured RMS voltage at the
 specified frequency that is above the detection threshold corresponds to a value of one.
 A measured RMS voltage below the detection threshold corresponds to a value of zero.

A signaling message occurs when a measured RMS voltage above the detection threshold is followed
 by a measured RMS voltage below the detection threshold. The remaining duration of the
 specified recording period contains the message content. The following figure shows a
 simulated signaling message and the corresponding detected signal.

[IMAGE alt='image' src='GUID-1756E895-57C5-4758-941F-FEC37D1815ED-a5.gif']

In the previous figure, the first five bits in the synchronous code correspond to a measured
 signaling voltage greater than the detection threshold for the specified time length of
 one. The second five bits correspond to a measured signaling voltage less than the
 detection threshold for the specified time length of zero. These bits indicate the
 presence of a signaling voltage. The remaining bits are the message content.

Parent topic:

Signaling

Related concepts:

- Discrete Fourier Transform

<!--NI_TOPIC bundle=labview-electrical-power-toolkit path=measuring-signals.html language=enus -->
## TOPIC 00044: Measuring Signals

- bundle_id: `labview-electrical-power-toolkit`
- source_path: `measuring-signals.html`
- source_url: https://docs-be.ni.com/bundle/labview-electrical-power-toolkit/raw/resource/enus/measuring-signals.html
- document_id: `labview-electrical-power-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use this section to learn about methods for measuring voltage, current, and frequency signals with the LabVIEW Electrical Power Toolkit.

### Measuring Signals

Use this section to learn about methods for measuring voltage, current, and frequency signals
 with the LabVIEW Electrical Power Toolkit.

Parent topic:

Electrical Power Signals

<!--NI_TOPIC bundle=labview-electrical-power-toolkit path=measuring-unbalance.html language=enus -->
## TOPIC 00045: Measuring Unbalance

- bundle_id: `labview-electrical-power-toolkit`
- source_path: `measuring-unbalance.html`
- source_url: https://docs-be.ni.com/bundle/labview-electrical-power-toolkit/raw/resource/enus/measuring-unbalance.html
- document_id: `labview-electrical-power-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: When measuring the unbalance of an electrical power system, you can use the symmetrical components or voltage values to calculate unbalance based on different standards. The LabVIEW Electrical Power Toolkit supports measuring unbalance in compliance with Class A of IEC 61000-4-30:2008 or NEMA MG 1-2

### Measuring Unbalance

When measuring the unbalance of an electrical power system, you can use the symmetrical
 components or voltage values to calculate unbalance based on different standards. The
 LabVIEW Electrical Power Toolkit supports measuring unbalance in compliance with Class A
 of IEC 61000-4-30:2008 or NEMA MG 1-2014.

The following equations define the unbalance factor using Class A of IEC 61000-4-30:2008.

[IMAGE alt='image' src='GUID-7C766418-9883-4DC6-86AB-55E123F8BB6E-a5.gif']

In the previous equations, the fundamental component of a voltage input signal is measured over a
 10-cycle time interval for a 50 Hz electrical power system and a 12-cycle time interval
 for a 60 Hz electrical power system.

The following equation defines the unbalance using NEMA MG 1-2014.

[IMAGE alt='image' src='GUID-7A9BC850-0380-4F41-86CF-E2D54711C3DE-a5.gif']

Parent topic:

Unbalance

<!--NI_TOPIC bundle=labview-electrical-power-toolkit path=measuring-voltage-dips-and-swells.html language=enus -->
## TOPIC 00046: Measuring Voltage Dips and Swells

- bundle_id: `labview-electrical-power-toolkit`
- source_path: `measuring-voltage-dips-and-swells.html`
- source_url: https://docs-be.ni.com/bundle/labview-electrical-power-toolkit/raw/resource/enus/measuring-voltage-dips-and-swells.html
- document_id: `labview-electrical-power-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The LabVIEW Electrical Power Toolkit complies with IEC 61000-4-30:2008 when measuring voltage dips and swells. You can specify whether to measure voltage dips and swells relative to the nominal voltage or to a sliding reference voltage. The basic measurement is the half-cycle RMS voltage on each cha

### Measuring Voltage Dips and Swells

The LabVIEW Electrical Power Toolkit complies with IEC 61000-4-30:2008 when measuring voltage
 dips and swells. You can specify whether to measure voltage dips and swells relative to
 the nominal voltage or to a sliding reference voltage. The basic measurement is the
 half-cycle RMS voltage on each channel, which is the value of the RMS voltage measured
 over a half-cycle and updated every half-cycle. In polyphase electrical power systems,
 the value of the half-cycle RMS voltage is independent for each channel and produces
 values at successive times for different channels.

A voltage dip starts when the RMS voltage falls below a specified dip threshold. A voltage dip
 ends when the RMS voltage rises above or equal to the dip threshold plus a hysteresis.
 For polyphase electrical power systems, a voltage dip may occur on one or more channels
 and may start on one channel and terminate on another. Refer to IEC 61000-4-30:2008 for
 details about single-phase voltage dip events and polyphase voltage dip events.

The expected number of voltage dips occurring annually in an electrical power system is from tens
 to a thousand, with the majority having a voltage magnitude greater than 40% of the
 nominal or sliding reference value and a duration of less than one second. Voltage dips
 with a voltage magnitude of 85-90% of the nominal value can occur frequently in some
 areas because of load switching. However, voltage dips with a voltage magnitude smaller
 than 40% of the nominal or sliding reference value and/or a duration longer than one
 second are infrequent.

A voltage swell starts when the RMS voltage rises above a specified swell threshold. A voltage
 swell ends when the RMS voltage falls below or equal to the swell threshold minus a
 hysteresis. For polyphase electrical power systems, a voltage swell may occur on one or
 more channels and may start on one channel and terminate on another. Refer to IEC
 61000-4-30:2008 for details about single-phase voltage swell events and polyphase
 voltage swell events.

The Electrical Power Toolkit can measure the following voltage dips and swells parameters
 according to IEC 61000-4-30:2008:

- Residual voltage or maximum swell voltage.
- Start time.
- Duration.

Parent topic:

Voltage Events

<!--NI_TOPIC bundle=labview-electrical-power-toolkit path=measuring-voltage-interruptions.html language=enus -->
## TOPIC 00047: Measuring Voltage Interruptions

- bundle_id: `labview-electrical-power-toolkit`
- source_path: `measuring-voltage-interruptions.html`
- source_url: https://docs-be.ni.com/bundle/labview-electrical-power-toolkit/raw/resource/enus/measuring-voltage-interruptions.html
- document_id: `labview-electrical-power-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The basic measurement of voltage interruptions is the half-cycle RMS voltage on each channel, which is the value of the RMS voltage measured over a half-cycle and updated every half-cycle. In polyphase systems, the value of half-cycle RMS voltage is independent for each channel and produces values a

### Measuring Voltage Interruptions

The basic measurement of voltage interruptions is the half-cycle RMS voltage on each channel,
 which is the value of the RMS voltage measured over a half-cycle and updated every
 half-cycle. In polyphase systems, the value of half-cycle RMS voltage is independent for
 each channel and produces values at successive times for different channels. Refer to
 IEC 61000-4-30:2008 for details about single-phase voltage interruptions and polyphase
 voltage interruptions.

The LabVIEW Electrical Power Toolkit can measure the following voltage interruptions parameters
 according to IEC 61000-4-30:2008:

- Start time.
- Duration.

Parent topic:

Voltage Events

<!--NI_TOPIC bundle=labview-electrical-power-toolkit path=new-features-and-changes.html language=enus -->
## TOPIC 00048: LabVIEW Electrical Power Toolkit New Features and Changes

- bundle_id: `labview-electrical-power-toolkit`
- source_path: `new-features-and-changes.html`
- source_url: https://docs-be.ni.com/bundle/labview-electrical-power-toolkit/raw/resource/enus/new-features-and-changes.html
- document_id: `labview-electrical-power-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Learn about updates, including new features and behavior changes, introduced in each version of LabVIEW Electrical Power Toolkit. Discover what is new in the latest releases of LabVIEW Electrical Power Toolkit.If you cannot find new features and changes for your version, it might not include user-fa

### LabVIEW Electrical Power Toolkit
 New Features and Changes

Learn about updates, including new features and behavior changes, introduced in each
 version of LabVIEW Electrical Power Toolkit.

LabVIEW Electrical Power Toolkit

Note

Release Notes

Related information:

- Software and Driver Downloads

#### LabVIEW Electrical Power Toolkit
 2026 Q1 Changes

Learn about new features, behavior changes, and other updates in LabVIEW Electrical Power Toolkit 2026 Q1.

##### New
 Features

This version of the LabVIEW Electrical Power Toolkit adds
 support for the following features:

- Support for 64-bit LabVIEW.

<!--NI_TOPIC bundle=labview-electrical-power-toolkit path=offset-calibration.html language=enus -->
## TOPIC 00049: Offset Calibration

- bundle_id: `labview-electrical-power-toolkit`
- source_path: `offset-calibration.html`
- source_url: https://docs-be.ni.com/bundle/labview-electrical-power-toolkit/raw/resource/enus/offset-calibration.html
- document_id: `labview-electrical-power-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: An offset is the mean amplitude of a periodic function waveform in the time domain. The existence of offsets in electrical power sinusoidal signals leads to inaccurate measurements of all electrical power parameters. Each component in a measurement instrument may cause offsets. For example, offsets

### Offset Calibration

An offset is the mean amplitude of a periodic function waveform in the time domain. The existence
 of offsets in electrical power sinusoidal signals leads to inaccurate measurements of
 all electrical power parameters. Each component in a measurement instrument may cause
 offsets. For example, offsets may appear in a hall-effect transducer because of the
 condition of temperature or the magnetization state of a magnetic circuit. Intense solar
 flares can cause a strong electromagnetic field, which leads to offsets in an electrical
 power grid.

To calibrate offsets, you first use a standard signal generator to generate sinusoidal signals
 with zero offset and then use the measurement instrument to measure the sinusoidal
 signals. You get the offset values by comparing the measured results with the standard
 sinusoidal signals. In future measurement, you subtract the offset values from measured
 results to ensure accurate measurements.

Parent topic:

Performing Calibration

<!--NI_TOPIC bundle=labview-electrical-power-toolkit path=overview.html language=enus -->
## TOPIC 00050: LabVIEW Electrical Power Toolkit Overview

- bundle_id: `labview-electrical-power-toolkit`
- source_path: `overview.html`
- source_url: https://docs-be.ni.com/bundle/labview-electrical-power-toolkit/raw/resource/enus/overview.html
- document_id: `labview-electrical-power-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following documents contain information that might be helpful as you use the LabVIEW Electrical Power Toolkit. LabVIEW Electrical Power Toolkit Readme Use this file to obtain introductory information about the Electrical Power Toolkit, such as product overview, system requirements, installation

### LabVIEW Electrical Power Toolkit
 Overview

The following documents contain information that might be helpful as you use the LabVIEW
 Electrical Power Toolkit.

LabVIEW Electrical Power Toolkit Readme

labview\readme

readme_EPT.html

LabVIEW Electrical Power Toolkit Example VIs

labview\examples\Electrical Power

Help

»

Find Examples

Toolkits and Modules

»

Electrical Power

Additional LabVIEW documentation

The following list contains reference materials that produce the Electrical Power
 Toolkit. These references contain more information on the theory that the Electrical
 Power Toolkit implements.

Note

| Standard | Title |
| --- | --- |
| EN 50160:2007 | Voltage Characteristics of Electricity Supplied by Public Distribution Networks |
| IEC 60255-127:2010 | Measuring relays and protection equipmentPart 127: Functional requirements for over/under voltage protection |
| IEC 60255-151:2009 | Measuring relays and protection equipmentPart 151: Functional requirements for over/under current protection |
| IEC 61000-4-7:2009 | Electromagnetic Compatibility (EMC)Part 4-7: Testing and Measurement Techniques - General Guide on Harmonics and Interharmonics Measurements and Instrumentation, for Power Supply Systems and Equipment Connected Thereto |
| IEC 61000-4-15:2010 | Electromagnetic Compatibility (EMC)Part 4-15: Testing and Measurement Techniques - Flickermeter - Functional and Design Specifications |
| IEC 61000-4-30:2008 | Electromagnetic Compatibility (EMC)Part 4-30: Testing and Measurement Techniques - Power Quality Measurement Methods |
| IEEE Std 1159-1995 | IEEE Recommended Practice for Monitoring Electric Power Quality |
| IEEE Std 1459-2010 | IEEE Standard Definitions for the Measurement of Electric Power Quantities Under Sinusoidal, Nonsinusoidal, Balanced, or Unbalanced Conditions |
| IEEE Std C37.111-1999 | IEEE Standard Common Format for Transient Data Exchange (COMTRADE) for Power Systems |
| IEEE Std C37.112-1996 | IEEE Standard Inverse-Time Characteristic Equations for Overcurrent Relays |
| IEEE Std C37.118.1-2011 | IEEE Standard for Synchrophasor Measurements for Power Systems |
| IEEE Std C37.118.1a-2014 | IEEE Standard for Synchrophasor Measurements for Power Systems Amendment 1: Modification of Selected Performance Requirements |
| IEEE Std C37.118.2-2011 | IEEE Standard for Synchrophasor Data Transfer for Power Systems |
| NEMA MG 1-2014 | Motors and Generators |

<!--NI_TOPIC bundle=labview-electrical-power-toolkit path=performing-calibration.html language=enus -->
## TOPIC 00051: Performing Calibration

- bundle_id: `labview-electrical-power-toolkit`
- source_path: `performing-calibration.html`
- source_url: https://docs-be.ni.com/bundle/labview-electrical-power-toolkit/raw/resource/enus/performing-calibration.html
- document_id: `labview-electrical-power-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following are the major parameters to calibrate in electrical power measurement: Offset. Gain. Spectrum. Offset and gain calibrations apply to all electrical power measurements, while spectrum calibration is a unique requirement for power quality measurement. You perform offset, gain, and spectr

### Performing Calibration

The following are the major parameters to calibrate in electrical power measurement:

- Offset.
- Gain.
- Spectrum.

Offset and gain calibrations apply to all electrical power measurements, while spectrum
 calibration is a unique requirement for power quality measurement. You perform offset,
 gain, and spectrum calibrations with the LabVIEW Electrical Power Toolkit to ensure that
 power quality analyzers that you build with National Instruments software and hardware
 have Class A compliance certificate of IEC 61000-4-30:2008.

Parent topic:

Calibration

<!--NI_TOPIC bundle=labview-electrical-power-toolkit path=power-distribution.html language=enus -->
## TOPIC 00052: Power Distribution

- bundle_id: `labview-electrical-power-toolkit`
- source_path: `power-distribution.html`
- source_url: https://docs-be.ni.com/bundle/labview-electrical-power-toolkit/raw/resource/enus/power-distribution.html
- document_id: `labview-electrical-power-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Power distribution is the movement of electrical power from substations in a transmission grid to end users, such as residential and light industries. Substations use transformers to step down the voltage to a lower level that is appropriate for the needs of end users. Distribution lines typically u

### Power Distribution

Power distribution is the movement of electrical power from substations in a transmission grid to end users, such as residential and light industries. Substations use transformers to step down the voltage to a lower level that is appropriate for the needs of end users. Distribution lines typically use voltages from 1 kV to 50 kV down to 120 V to 240 V. Distribution grids might provide single-phase, two-phase, or three-phase electrical power, depending on the geographic location and user requirements.

Parent topic:

Electrical Power Grids

Related concepts:

- Connections and Wiring
- Line and Bus Configurations

<!--NI_TOPIC bundle=labview-electrical-power-toolkit path=power-energy-measurement.html language=enus -->
## TOPIC 00053: Power & Energy Measurement

- bundle_id: `labview-electrical-power-toolkit`
- source_path: `power-energy-measurement.html`
- source_url: https://docs-be.ni.com/bundle/labview-electrical-power-toolkit/raw/resource/enus/power-energy-measurement.html
- document_id: `labview-electrical-power-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use this section to learn about methods for obtaining power and energy data that you can analyze with the LabVIEW Electrical Power Toolkit.

### Power & Energy Measurement

Use this section to learn about methods for obtaining power and energy data that you
 can analyze with the LabVIEW Electrical Power Toolkit.

- [Power Measurement](power-measurement.html)
- [Energy Measurement](energy-measurement.html)

<!--NI_TOPIC bundle=labview-electrical-power-toolkit path=power-factor.html language=enus -->
## TOPIC 00054: Power Factor

- bundle_id: `labview-electrical-power-toolkit`
- source_path: `power-factor.html`
- source_url: https://docs-be.ni.com/bundle/labview-electrical-power-toolkit/raw/resource/enus/power-factor.html
- document_id: `labview-electrical-power-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: In an AC circuit, the power factor (PF) is the ratio of active power to apparent power, given by the following equation:2 where θ is the angle difference between voltage and current. The power factor is a measure of the efficiency of an electrical power distribution system. A system with a higher po

### Power Factor

In an AC circuit, the power factor (PF) is the ratio of active power to apparent power, given by
 the following equation:

Figure 2.

[IMAGE alt='image' src='GUID-CD056589-A426-452E-9FE0-8073FBB5820E-a5.gif']

where θ is the angle difference between voltage and current. The power factor is a measure of the
 efficiency of an electrical power distribution system. A system with a higher power
 factor is more efficient because reactive loads cause lower energy losses. If voltage
 and current are in phase, PF has a value of one. If voltage and
 current are 90 degrees out of phase, PF has a value of zero.

Power factors less than one increase the overall cost of an electrical power distribution system.
 A poor power factor in a circuit describes a power factor that is less than 0.85. A poor
 power factor can result in heat damage to insulation and other circuit components,
 reduce the amount of useful power available, and require increased conductor and
 equipment sizes.

Parent topic:

Power Measurement

<!--NI_TOPIC bundle=labview-electrical-power-toolkit path=power-generation.html language=enus -->
## TOPIC 00055: Power Generation

- bundle_id: `labview-electrical-power-toolkit`
- source_path: `power-generation.html`
- source_url: https://docs-be.ni.com/bundle/labview-electrical-power-toolkit/raw/resource/enus/power-generation.html
- document_id: `labview-electrical-power-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: A generator converts mechanical energy to electrical energy. Electrical power generation uses generators that produce AC power. An AC generator consists of a rotating magnetic core enclosed by conducting windings. The rotating magnetic core generates varying magnetic flux that induces a current to f

### Power Generation

A generator converts mechanical energy to electrical energy. Electrical power generation uses generators that produce AC power. An AC generator consists of a rotating magnetic core enclosed by conducting windings. The rotating magnetic core generates varying magnetic flux that induces a current to flow in the windings. A typical AC generator uses three sets of windings that contain a physical angle difference to produce three-phase electric current with a mutual phase difference of 120 degrees. The magnetic core rotates at a constant speed synchronized with the line frequency of an electrical power grid. The line frequency is usually 50 Hz or 60 Hz, depending on geographic locations. Most of the world has a line frequency of 50 Hz, whereas North America uses 60 Hz as the line frequency.

Parent topic:

Electrical Power Grids

<!--NI_TOPIC bundle=labview-electrical-power-toolkit path=power-measurement.html language=enus -->
## TOPIC 00056: Power Measurement

- bundle_id: `labview-electrical-power-toolkit`
- source_path: `power-measurement.html`
- source_url: https://docs-be.ni.com/bundle/labview-electrical-power-toolkit/raw/resource/enus/power-measurement.html
- document_id: `labview-electrical-power-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: In three-phase electrical power measurement applications, the current you measure is usually the line current, while the voltage you measure can be either the phase voltage or line voltage. If the voltage you measure is the line voltage, you need to perform a delta to wye (D to Y) conversion to conv

### Power Measurement

In three-phase electrical power measurement applications, the current you measure is usually the
 line current, while the voltage you measure can be either the phase voltage or line
 voltage. If the voltage you measure is the line voltage, you need to perform a
 *delta to wye (D to Y) conversion* to convert the line voltage to phase
 voltage in order to calculate the electrical power. The following figure represents
 fundamental electrical power measurements in a power triangle.

[IMAGE alt='image' src='GUID-379E427F-ABDF-43F4-9103-C4F132A724F8-a5.gif']

The following factors might affect the accuracy of electrical power measurements:

- Accuracy of measured voltage amplitude and current amplitude.
- Phase shift between voltage and current.
- Measurement errors from transducers.

Use the LabVIEW Electrical Power Toolkit to calculate electrical power by using time-domain or
 frequency-domain voltage and current signals. To calculate electrical power accurately
 in the frequency domain, you perform a *spectrum calibration* before
 measuring. You also can use the Electrical Power Toolkit to calculate cycle-by-cycle
 fundamental electrical power values.

Parent topic:

Power & Energy Measurement

Related concepts:

- Conversion
- Spectrum Calibration

<!--NI_TOPIC bundle=labview-electrical-power-toolkit path=power-quality.html language=enus -->
## TOPIC 00057: Power Quality

- bundle_id: `labview-electrical-power-toolkit`
- source_path: `power-quality.html`
- source_url: https://docs-be.ni.com/bundle/labview-electrical-power-toolkit/raw/resource/enus/power-quality.html
- document_id: `labview-electrical-power-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Power quality is important for the powering and the grounding of electrical power systems. Power quality analysis ensures that the quality of the electrical power is suitable for electrical power systems to operate as intended. Without proper electrical power, electrical power systems might malfunct

### Power Quality

Power quality is important for the powering and the grounding of electrical power systems. Power
 quality analysis ensures that the quality of the electrical power is suitable for
 electrical power systems to operate as intended. Without proper electrical power,
 electrical power systems might malfunction or fail. During power generation, power
 quality refers to the generator's ability to generate power with variations in proper
 limits. During power transmission and distribution, power quality means that the voltage
 variations are in proper limits.

- Electrical utilities
- End users
- Instruments manufacturers
- Standards organizations
- Research organizations

- Definitions of voltage events on single-phase systems and polyphase systems
- Duration of measurements
- Calculation of sliding reference voltage
- Trigger threshold values for recording fault data
- Location, specifications, and connection of equipment that measures power quality
- Aggregation methods

#### Power Quality Standards

Power quality standards define measurement methods for power quality parameters. The
 standards also set limits for changes in voltage, current, and frequency. The
 following table lists standards organizations and types of standards that the
 organizations published for power quality analysis.

| Organization | Type of Standards |
| --- | --- |
| American National Standards Institute (ANSI) | Steady-state voltage ratings (ANSI C84.1) |
| European Committee for Electrotechnical Standardization (CENELEC) | Regional standards |
| Comite International Special des Perturbations Radioelectriques (CISPR) | International standards |
| Electric Power Research Institute (EPRI) | Signature newsletter on power quality standards |
| International Electrotechnical Commission (IEC) | International standards |
| Institute of Electrical and Electronics Engineers (IEEE) | International and United States standards |
| Information Technology Industry Council (ITI) | Equipment guides |
| National Electrical Manufacturers Association (NEMA) | Equipment standards |
| National Fire Protection Association (NFPA) | Lighting protection National Electric Code |
| National Institute of Standards and Technology (NIST) | General Information on all standards |
| Underwriters Laboratories (UL) | Safety standards for equipment |

Related concepts:

- Calibration
- Voltage Events

<!--NI_TOPIC bundle=labview-electrical-power-toolkit path=power-transmission.html language=enus -->
## TOPIC 00058: Power Transmission

- bundle_id: `labview-electrical-power-toolkit`
- source_path: `power-transmission.html`
- source_url: https://docs-be.ni.com/bundle/labview-electrical-power-toolkit/raw/resource/enus/power-transmission.html
- document_id: `labview-electrical-power-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Power transmission is the movement of electrical power from the power generation source over a large distance to electrical substations in a distribution grid.Electrical power transmits at high voltages by using three-phase AC. By increasing the voltage and decreasing the current in proportion, you

### Power Transmission

Power transmission is the movement of electrical power from the power generation source over a
 large distance to electrical substations in a distribution grid.

Electrical power transmits at high voltages by using three-phase AC. By increasing the voltage
 and decreasing the current in proportion, you can transmit the same amount of power as
 the power input but reduce energy loss significantly. In an AC electrical power system,
 you can use transformers to step up the voltage at the power source and step down the
 voltage at the destination.

Three-phase electrical power systems use three transmission lines to carry AC signals of the same
 frequency with a 120-degree phase difference. Three-phase electrical power systems have
 the following advantages:

- A three-phase electrical power system is more economical than a single-phase electrical power system because a three-phase electrical power system delivers 73% more power for a 50% increase in conducting cable.
- The sum of symmetrical components is zero for a balanced load, which enables utilities to deliver a steady amount of power. Steady power can reduce vibrations in motors and generators, which might lead to faults.
- A three-phase electrical power system can produce a rotating magnetic field that simplifies the design and operation of electric motors.

Heavy industries use three-phase electrical power. For residential and light industries,
 utilities convert three-phase electrical power to a single-phase connection in
 distribution grids before delivery.

Parent topic:

Electrical Power Grids

Related concepts:

- Connections and Wiring
- Line and Bus Configurations
- Symmetrical Components

<!--NI_TOPIC bundle=labview-electrical-power-toolkit path=rapid-voltage-changes.html language=enus -->
## TOPIC 00059: Rapid Voltage Changes

- bundle_id: `labview-electrical-power-toolkit`
- source_path: `rapid-voltage-changes.html`
- source_url: https://docs-be.ni.com/bundle/labview-electrical-power-toolkit/raw/resource/enus/rapid-voltage-changes.html
- document_id: `labview-electrical-power-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: A rapid voltage change (RVC) is a transition in RMS voltage between two steady-state conditions, not exceeding ±5% typically and ±10% generally of the nominal voltage under normal operating conditions. The voltage during an RVC must not exceed the voltage dip or swell threshold values, otherwise the

### Rapid Voltage Changes

A rapid voltage change (RVC) is a transition in RMS voltage between two steady-state conditions,
 not exceeding ±5% typically and ±10% generally of the nominal voltage under normal
 operating conditions. The voltage during an RVC must not exceed the voltage dip or swell
 threshold values, otherwise the RVC is considered to be a voltage dip or swell.

The basic measurement of RVC is the half-cycle RMS voltage on each channel, which is the value of
 the RMS voltage measured over a single-cycle and updated every half-cycle. In polyphase
 systems, the value of the half-cycle RMS voltage is independent for each channel and
 produces values at successive times for different channels.

The following figure shows threshold parameters for an RVC between two steady states.

[IMAGE alt='image' src='GUID-557C3109-61D8-4281-8207-465B94FF4724-a5.gif']

You can use the LabVIEW Electrical Power Toolkit to measure the following RVC parameters
 according to IEC 61000-4-30:2008:

- Start time.
- Duration.
- Maximum voltage change.
- Voltage difference between two steady-state conditions.
- Duration when a voltage is higher than the maximum voltage change.

Parent topic:

Voltage Events

<!--NI_TOPIC bundle=labview-electrical-power-toolkit path=reactive-power.html language=enus -->
## TOPIC 00060: Reactive Power

- bundle_id: `labview-electrical-power-toolkit`
- source_path: `reactive-power.html`
- source_url: https://docs-be.ni.com/bundle/labview-electrical-power-toolkit/raw/resource/enus/reactive-power.html
- document_id: `labview-electrical-power-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Capacitive and inductive loads in a circuit temporarily store energy in the form of electric and magnetic fields. Energy that capacitive and inductive loads store returns to the source each cycle.In an AC circuit, the voltage across a capacitor varies with time. Capacitors oppose the voltage changes

### Reactive Power

Capacitive and inductive loads in a circuit temporarily store energy in the form of electric and
 magnetic fields. Energy that capacitive and inductive loads store returns to the source
 each cycle.

In an AC circuit, the voltage across a capacitor varies with time. Capacitors oppose the voltage
 changes, which causes a phase difference between voltage and current waveforms, where
 the voltage lags the current. Capacitors therefore generates reactive power. In an
 inductor, the current lags the voltage. Consequently, inductors consume reactive power.
 You use capacitors and inductors in electrical power systems to balance reactive power
 and control the power factor.

The following equation calculates reactive power.

Figure 1.

[IMAGE alt='image' src='GUID-10C8A95D-3185-4733-9E51-971E9AAF6163-a5.gif']

where Q is the reactive power, S is the apparent power, and
 P is the active power.

You measure reactive power in volt-ampere reactives (VAR).

Parent topic:

Power Measurement

<!--NI_TOPIC bundle=labview-electrical-power-toolkit path=resampling.html language=enus -->
## TOPIC 00061: Resampling

- bundle_id: `labview-electrical-power-toolkit`
- source_path: `resampling.html`
- source_url: https://docs-be.ni.com/bundle/labview-electrical-power-toolkit/raw/resource/enus/resampling.html
- document_id: `labview-electrical-power-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: When applying a fast Fourier transform (FFT) to even-time-spaced samples, or a time waveform, you can calculate the frequency components that are periodic in time. However, harmonic components in electrical power signal take place n times per cycle and are periodic in rotational angle.IEC 61000-4-30

### Resampling

When applying a fast Fourier transform (FFT) to even-time-spaced samples, or a time waveform, you
 can calculate the frequency components that are periodic in time. However, harmonic
 components in electrical power signal take place n times per cycle
 and are periodic in rotational angle.

IEC 61000-4-30:2008 defines the measurement methods and the uncertainty compliance level of a
 series of power quality parameters. The basic measurement time interval of these
 parameters is 10 cycles for a 50 Hz electrical power system and 12 cycles for a 60 Hz
 electrical power system. However, the line frequency might vary over time because of
 load changes or changes of other components in an electrical power grid, which makes the
 number of samples per cycle different. Class A of IEC 61000-4-30:2008 requires that all
 the measured frequency in a power quality analyzer must be within a specified
 uncertainty within a specified frequency range. For example, the measured parameters in
 a power quality analyzer must have an accuracy of 0.01 Hz within the range of 42.5 Hz to
 57.5 Hz for a 50 Hz electrical power system and 51 Hz to 69 Hz for a 60 Hz electrical
 power system.

Signals that are evenly-spaced in rotation angle are even-angle signals. You can think of
 even-angle signals as signals acquired at a constant angle interval relative to the
 fundamental component. If acquired samples of electrical power signals are evenly-spaced
 in rotation angle, you can apply an FFT to the even-angle-spaced samples to calculate
 the harmonic components that are periodic in rotational angle. You can use standard FFT
 methods to perform further analysis with an even-angle signal.

In order to acquire even-angle samples, you must adjust the sample rate of data acquisition
 devices according to the fundamental frequency. The adjusted sample rate is the
 synchronous sample rate. In practice, you need complex additional hardware to set a
 variable sample rate to acquire samples with a synchronous sample rate. Applying
 anti-alias filtering also is difficult when the sample rate is variable. The LabVIEW
 Electrical Power Toolkit provides software resampling that can avoid the challenges of
 hardware implementation. You can acquire a voltage or current signal with a fixed sample
 rate and then use the Electrical Power Toolkit to resample the signal with a synchronous
 sample rate.

Parent topic:

Acquiring Signals

<!--NI_TOPIC bundle=labview-electrical-power-toolkit path=sample-rate.html language=enus -->
## TOPIC 00062: Sample Rate

- bundle_id: `labview-electrical-power-toolkit`
- source_path: `sample-rate.html`
- source_url: https://docs-be.ni.com/bundle/labview-electrical-power-toolkit/raw/resource/enus/sample-rate.html
- document_id: `labview-electrical-power-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Sample rate determines how often an analog-to-digital (A/D) conversion takes place. A high input sample rate acquires more points in a given time and can form a more accurate representation of the original signal than a low input sample rate.The basic equation for sample rate is as follows:f[sampled

### Sample Rate

Sample rate determines how often an analog-to-digital (A/D) conversion takes place. A high input
 sample rate acquires more points in a given time and can form a more accurate
 representation of the original signal than a low input sample rate.

The basic equation for sample rate is as follows:

f<sub>sampled</sub> ≥ 2.56 * maximum frequency of
 interest

NI 9225 or NI 9227 supports a range of sample rates from 1.613 KS/s to 50 KS/s for performing
 voltage and current measurements. In most cases, you specify a sample rate of 50 KS/s to
 perform voltage and current measurements. A sample rate of 50 KS/s ensures the minimum
 input delay and the most accurate representation of the original signal.

Parent topic:

Acquiring Signals

<!--NI_TOPIC bundle=labview-electrical-power-toolkit path=signaling.html language=enus -->
## TOPIC 00063: Signaling

- bundle_id: `labview-electrical-power-toolkit`
- source_path: `signaling.html`
- source_url: https://docs-be.ni.com/bundle/labview-electrical-power-toolkit/raw/resource/enus/signaling.html
- document_id: `labview-electrical-power-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use this section to learn about methods for obtaining mains signaling voltage data that you can analyze with the LabVIEW Electrical Power Toolkit.A mains signaling voltage is a burst of signals at a specific frequency of a voltage waveform. A typical application is at interharmonic frequencies to av

### Signaling

Use this section to learn about methods for obtaining mains signaling voltage data that
 you can analyze with the LabVIEW Electrical Power Toolkit.

A mains signaling voltage is a burst of signals at a specific frequency of a voltage waveform. A
 typical application is at interharmonic frequencies to avoid interference with harmonics
 measurements. Use mains signaling voltages to send instructions to
 equipment connected to an electrical power grid. The following are three types of
 mains signaling voltages:

- 
- Ripple control signals —Voltage signals applied at interharmonic frequencies that are typically in the range
 of 0.11 kHz to 3 kHz.
- 
- Power line carrier signals —Voltage signals applied at interharmonic frequencies that are typically in the range
 of 3 kHz to 148.5 kHz.
- 
- Mains marking signals —Voltage transients applied at specific points in a waveform.

- [Applications of Signaling Voltages](applications-of-signaling-voltages.html)
- [Measuring Signaling Voltages](measuring-signaling-voltages.html)

<!--NI_TOPIC bundle=labview-electrical-power-toolkit path=spectrum-calibration.html language=enus -->
## TOPIC 00064: Spectrum Calibration

- bundle_id: `labview-electrical-power-toolkit`
- source_path: `spectrum-calibration.html`
- source_url: https://docs-be.ni.com/bundle/labview-electrical-power-toolkit/raw/resource/enus/spectrum-calibration.html
- document_id: `labview-electrical-power-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The frequency spectrum of a time-domain signal presents magnitude and phase values of the signal in the frequency domain. The Fourier transform converts a time-domain signal into the frequency spectrum of the signal. Components in a measurement instrument may perform differently under different freq

### Spectrum Calibration

The frequency spectrum of a time-domain signal presents magnitude and phase values of the signal
 in the frequency domain. The Fourier transform converts a time-domain signal into the
 frequency spectrum of the signal. Components in a measurement instrument may perform
 differently under different frequencies and thus affect the accuracy in measuring the
 magnitude and phase of *harmonics*. Calibration helps to find out waveforms
 with harmonic distortion and ensures that a measurement instrument meets harmonic
 measurement accuracy requirements as defined in IEC 61000-4-7:2009. You need to
 calibrate several times for different range percentages to reduce nonlinearity of
 transducers over a wide measurement range. You also need to calibrate for each harmonic
 up to the 50th order as defined in IEC 61000-4-30:2008.

To calibrate frequency spectra, you first use a standard signal generator to generate sinusoidal
 signals with one harmonic component whose magnitude and phase are known and precise. You
 then use the measurement instrument to measure the magnitude and phase of the harmonic
 component. You get the error values by comparing the measured results with the harmonic
 component that you generate with the standard signal generator. In future measurement,
 you compensate for both magnitude and phase errors to ensure accurate measurements.

Parent topic:

Performing Calibration

Related concepts:

- Power Measurement
- Harmonics

<!--NI_TOPIC bundle=labview-electrical-power-toolkit path=symmetrical-components.html language=enus -->
## TOPIC 00065: Symmetrical Components

- bundle_id: `labview-electrical-power-toolkit`
- source_path: `symmetrical-components.html`
- source_url: https://docs-be.ni.com/bundle/labview-electrical-power-toolkit/raw/resource/enus/symmetrical-components.html
- document_id: `labview-electrical-power-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use the method of symmetrical components to calculate unbalance in a three-phase electrical power system. The method of symmetrical components expresses a set of N unbalanced phasors as the sum of N symmetrical sets of balanced phasors. The method of symmetrical components linearly transform

### Symmetrical Components

You can use the method of symmetrical components to calculate unbalance in a three-phase
 electrical power system. The method of symmetrical components expresses a set of
 N unbalanced phasors as the sum of N
 symmetrical sets of balanced phasors. The method of symmetrical components linearly
 transforms unbalanced three phase voltages and currents into three sets of balanced
 voltages and currents, or the symmetrical components.

The following table lists symmetrical components of voltages.

| Components | Equations | Vector | Note |
| --- | --- | --- | --- |
| Positive Sequence Component | U1A = U1U1B = a2U1U1C = aU1 |  | - |
| Negative Sequence Component | U2A = U2U2B = aU2U2C = a2U2 |  | Negative sequence components have reverse phase rotation or sequence from positive sequence components. |
| Zero Sequence Component | U0A = U0B = U0C = U0 |  | Zero sequence components exist in phase and are equal in magnitude. |

In the previous table, U<sub>1</sub>, U<sub>2</sub>, and
 U<sub>0</sub> are the corresponding initial voltage vectors for
 the positive, negative, and zero sequences. a is the rotational
 operator defined by the following equation:

[IMAGE alt='image' src='GUID-1F86470C-E0CA-4CD3-BA02-C5E49DEDB082-a5.gif']

The actual phase voltage is the sum of its corresponding components:

U<sub>A</sub> =
 U<sub>1</sub><sub>A</sub> +
 U<sub>2</sub><sub>A</sub> +
 U<sub>0</sub><sub>A</sub> =
 U<sub>1</sub> + U<sub>2</sub> +
 U<sub>0</sub>

U<sub>B</sub> =
 U<sub>1</sub><sub>B</sub> +
 U<sub>2</sub><sub>B</sub> +
 U<sub>0</sub><sub>B</sub> =
 a<sup>2</sup>U<sub>1</sub> +
 aU<sub>2</sub> +
 U<sub>0</sub>

U<sub>C</sub> =
 U<sub>1</sub><sub>C</sub> +
 U<sub>2</sub><sub>C</sub> +
 U<sub>0</sub><sub>C</sub> =
 aU<sub>1</sub> +
 a<sup>2</sup>U<sub>2</sub> +
 U<sub>0</sub>

The following equation defines the sequence quantities from an unbalanced three-phase electrical
 power system:

U<sub>0</sub> = 1/3
 (U<sub>A</sub> +
 U<sub>B</sub> +
 U<sub>C</sub>)

U<sub>1</sub> = 1/3
 (U<sub>A</sub> +
 aU<sub>B</sub> +
 a<sup>2</sup>U<sub>C</sub>)

U<sub>2</sub> = 1/3
 (U<sub>A</sub> +
 a<sup>2</sup>U<sub>B</sub>
 + aU<sub>C</sub>)

The following figure shows phase voltages as the sum of symmetrical components in an
 unsymmetrical system.

[IMAGE alt='image' src='GUID-9EE54AF1-0779-44FC-8920-E87F7AF1225A-a5.gif']

Parent topic:

Unbalance

Related concepts:

- Power Transmission

<!--NI_TOPIC bundle=labview-electrical-power-toolkit path=synchronous-sampling.html language=enus -->
## TOPIC 00066: Synchronous Sampling

- bundle_id: `labview-electrical-power-toolkit`
- source_path: `synchronous-sampling.html`
- source_url: https://docs-be.ni.com/bundle/labview-electrical-power-toolkit/raw/resource/enus/synchronous-sampling.html
- document_id: `labview-electrical-power-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Synchronous sampling is a key feature of a data acquisition module for acquiring voltage and current signals. Some power measurements require the following types of synchronous sampling: Active power Reactive power Power factor Synchronous sampling is automatic in any acquisition when you perform vo

### Synchronous Sampling

- Active power
- Reactive power
- Power factor

- Perfect, shared timing and triggering in order to achieve zero inter-channel sampling
 delay.
- Deterministic timing and triggering to achieve a deterministic nonzero inter-channel
 sampling delay.
- Shared, non-deterministic triggering and/or independent timing in which the separate
 clocks are not phase-locked.
- Independent subsystems with free-running timing and separate triggers.

- Post-trigger delay
- Signal conditioning through an all-pass filter
- Scaling the measured phase responses directly

Time

=

Samples

Samples rate

=

Phase

360

×

Frequency

where

- The time is in seconds.
- The sample rate is in hertz.
- The phase is in degrees.
- The frequency is in hertz.

The following figure demonstrates the relationships among these units.

[IMAGE alt='Waveform graph showing amplitude versus time with two overlaid waveforms.' src='GUID-EFEBCE5B-D083-4013-8963-A7D4B8C6C2C8-a5.gif']

In the previous figure, the delay time is 0.01 seconds. This delay time equals 10
 samples/1000 (samples/s) and 90 deg/(360 deg * 25 Hz).

Parent topic:

Acquiring Signals

<!--NI_TOPIC bundle=labview-electrical-power-toolkit path=time-aggregation.html language=enus -->
## TOPIC 00067: Time Aggregation

- bundle_id: `labview-electrical-power-toolkit`
- source_path: `time-aggregation.html`
- source_url: https://docs-be.ni.com/bundle/labview-electrical-power-toolkit/raw/resource/enus/time-aggregation.html
- document_id: `labview-electrical-power-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use this section to learn about methods for aggregating power quality data that you can analyze with the LabVIEW Electrical Power Toolkit.Aggregation is the statistical averaging of values that are recorded over time to acquire a single and representative value for the total time period. Aggregation

### Time Aggregation

Use this section to learn about methods for aggregating power quality data that you can
 analyze with the LabVIEW Electrical Power Toolkit.

Aggregation is the statistical averaging of values that are recorded over time to acquire a
 single and representative value for the total time period. Aggregation is useful for the
 *evaluation of power quality* across a large electrical power system. A large
 electrical power system typically experiences constant disturbance levels over short periods.
 To obtain representative values without recording all the data continuously, you use
 aggregation. Aggregation can also reduce the amount of data that you need to store for a long
 period of time.

- [Aggregation Intervals](aggregation-intervals.html)

Related concepts:

- Flagging
- Evaluation Standards

<!--NI_TOPIC bundle=labview-electrical-power-toolkit path=time-aggregation_2.html language=enus -->
## TOPIC 00068: Time Aggregation

- bundle_id: `labview-electrical-power-toolkit`
- source_path: `time-aggregation_2.html`
- source_url: https://docs-be.ni.com/bundle/labview-electrical-power-toolkit/raw/resource/enus/time-aggregation_2.html
- document_id: `labview-electrical-power-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use this section to learn about methods for aggregating power quality data that you can analyze with the LabVIEW Electrical Power Toolkit.Aggregation is the statistical averaging of values that are recorded over time to acquire a single and representative value for the total time period. Aggregation

### Time Aggregation

Use this section to learn about methods for aggregating power quality data that you can
 analyze with the LabVIEW Electrical Power Toolkit.

Aggregation is the statistical averaging of values that are recorded over time to acquire a
 single and representative value for the total time period. Aggregation is useful for the
 *evaluation of power quality* across a large electrical power system. A large
 electrical power system typically experiences constant disturbance levels over short periods.
 To obtain representative values without recording all the data continuously, you use
 aggregation. Aggregation can also reduce the amount of data that you need to store for a long
 period of time.

- [Aggregation Intervals](aggregation-intervals_2.html)

<!--NI_TOPIC bundle=labview-electrical-power-toolkit path=total-harmonic-distortion.html language=enus -->
## TOPIC 00069: Total Harmonic Distortion

- bundle_id: `labview-electrical-power-toolkit`
- source_path: `total-harmonic-distortion.html`
- source_url: https://docs-be.ni.com/bundle/labview-electrical-power-toolkit/raw/resource/enus/total-harmonic-distortion.html
- document_id: `labview-electrical-power-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: When a voltage or current signal passes through an electrical power system, additional content is added at the harmonics of the original frequencies. Total harmonic distortion (THD) is the level of undesired harmonics present in a voltage or current signal. THD is defined as the ratio of the RMS val

### Total Harmonic Distortion

When a voltage or current signal passes through an electrical power system, additional content is
 added at the harmonics of the original frequencies. Total harmonic distortion (THD) is
 the level of undesired harmonics present in a voltage or current signal. THD is defined
 as the ratio of the RMS value of the sum of all harmonic components up to a specified
 order to the RMS value of the fundamental frequency. THD is usually expressed as a
 percentage. Use the following equation to calculate THD.

[IMAGE alt='image' src='GUID-FF80749E-14C9-4899-A047-5D2D13262CD8-a5.gif']

where Y<sub>H,2</sub>, Y<sub>H,3</sub>,
 Y<sub>H,4</sub>, ..,
 Y<sub>H,h<sub>max</sub></sub> is the RMS value of each harmonic
 component; Y<sub>H,1</sub> is the RMS value of the fundamental
 frequency; h<sub>max</sub> is the maximum specified order, which has a value of 50
 according to Class A of IEC 61000-4-30:2008 and a value of 40 according to EN
 50160:2007.

#### Group Total Harmonic
 Distortion

Group total harmonic distortion (THDG) is the ratio of the RMS values of the sum of
 all harmonic groups up to a specified order to the harmonic group associated with
 the fundamental frequency. THDG is usually expressed as a percentage. Use the
 following equation to calculate THDG.

[IMAGE alt='image' src='GUID-ECDDF18E-26F4-46FE-AAA3-794FC08A8932-a5.gif']

where Y<sub>g</sub><sub>,2</sub>,
 Y<sub>g</sub><sub>,3</sub>,
 Y<sub>g</sub><sub>,4</sub>, ..,
 Y<sub>g</sub><sub>,</sub><sub>h<sub>max</sub></sub>
 is the RMS value of each harmonic group;
 Y<sub>g</sub><sub>,1</sub> is the RMS
 value of the fundamental frequency harmonic group; h<sub>max</sub> is the maximum
 specified order, which has a value of 50 according to Class A of IEC 61000-4-30:2008
 and a value of 40 according to EN 50160:2007.

#### Subgroup Total Harmonic
 Distortion

Subgroup total harmonic distortion (THDS) is the ratio of the RMS values of the sum
 of all harmonic subgroups up to a specified order to the harmonic subgroup
 associated with the fundamental frequency. THDS is usually expressed as a
 percentage. Use the following equation to calculate THDS.

[IMAGE alt='image' src='GUID-BCB7846D-AE7F-47C4-BA2F-9CF1C29C4413-a5.gif']

where Y<sub>sg</sub><sub>,2</sub>,
 Y<sub>sg</sub><sub>,3</sub>,
 Y<sub>sg</sub><sub>,4</sub>, ..,
 Y<sub>sg</sub><sub>,</sub><sub>h<sub>max</sub></sub>
 is the RMS value of each harmonic subgroup;
 Y<sub>sg</sub><sub>,1</sub> is the RMS
 value of the fundamental frequency harmonic subgroup; h<sub>max</sub> is the maximum
 specified order, which has a value of 50 according to Class A of IEC 61000-4-30:2008
 and a value of 40 according to EN 50160:2007.

Parent topic:

Harmonics

<!--NI_TOPIC bundle=labview-electrical-power-toolkit path=transients.html language=enus -->
## TOPIC 00070: Transients

- bundle_id: `labview-electrical-power-toolkit`
- source_path: `transients.html`
- source_url: https://docs-be.ni.com/bundle/labview-electrical-power-toolkit/raw/resource/enus/transients.html
- document_id: `labview-electrical-power-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: A transient is a voltage event that has an extremely short duration, typically less than half a cycle or a single cycle. Many transients show both impulsive and oscillatory transient behavior.Impulsive Transients An impulsive transient is a sudden unidirectional variation in the steady-state conditi

### Transients

A transient is a voltage event that has an extremely short duration, typically less than half a
 cycle or a single cycle. Many transients show both impulsive and oscillatory transient
 behavior.

#### Impulsive Transients

An impulsive transient is a sudden unidirectional variation in the steady-state condition of a voltage or current waveform. Lightning strikes close to power lines are the most common source of impulsive transients. Lightning strikes create an electromagnetic field in the vicinity of power lines, which can lead to a transient overvoltage in power lines.

#### Oscillatory Transients

Oscillatory transients show a damped oscillation, with a voltage or current waveform continuing to oscillate for half a cycle to three cycles and reaching a new steady-state value. Oscillatory transients arise because of switching actions in circuits, namely the energizing and de-energizing of capacitors and inductors. A sudden change in an electrical power system when a component is energized or de-energized leads to high-frequency damped oscillations until the system reaches a new steady state.

#### Effects of Transients

Transients can cause temporary or permanent damage to electrical equipment. A transient overvoltage can damage components, especially semiconductors, which are not designed to withstand high voltages. Transient overvoltages of sufficient duration can dissipate an amount of energy that is larger than a component is designed to withstand, which causes permanent damage.

Transients can cause data errors in data processing and storage equipment because transients in electrical power circuits can couple to communications and control circuits or cause adjustable speed drives to trip accidentally.

#### Measurement of Transients

Because transients intrinsically have a very short duration, the measurement of transients requires wide bandwidth circuits with high sample rates.

Parent topic:

Voltage Events

<!--NI_TOPIC bundle=labview-electrical-power-toolkit path=trend-data-logging.html language=enus -->
## TOPIC 00071: Trend Data Logging

- bundle_id: `labview-electrical-power-toolkit`
- source_path: `trend-data-logging.html`
- source_url: https://docs-be.ni.com/bundle/labview-electrical-power-toolkit/raw/resource/enus/trend-data-logging.html
- document_id: `labview-electrical-power-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Trend data is useful for overall system analysis. Trend data can help to ensure that utility feeder and substation capacities meet demand. Trend data is also helpful for planning expansions to existing systems, such as adding new loads and backup systems. Trend data can include any periodically reco

### Trend Data Logging

Trend data is useful for overall system analysis. Trend data can help to ensure that utility
 feeder and substation capacities meet demand. Trend data is also helpful for planning
 expansions to existing systems, such as adding new loads and backup systems. Trend data
 can include any periodically recorded measurements of power quality and flagged values.
 You log trend data over different time intervals, which can range from every 10 or 12
 cycles to several minutes, hours, days, or years.

Parent topic:

Data Logging

<!--NI_TOPIC bundle=labview-electrical-power-toolkit path=triggers.html language=enus -->
## TOPIC 00072: Triggers

- bundle_id: `labview-electrical-power-toolkit`
- source_path: `triggers.html`
- source_url: https://docs-be.ni.com/bundle/labview-electrical-power-toolkit/raw/resource/enus/triggers.html
- document_id: `labview-electrical-power-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: This section discusses methods to trigger data logging that you can analyze with the LabVIEW Electrical Power Toolkit.You specify trigger threshold values to start non-continuous data recording that can capture voltage and current waveforms with a high sample rate. The data logging process captures

### Triggers

This section discusses methods to trigger data logging that you can analyze with the
 LabVIEW Electrical Power Toolkit.

- Power quality parameters or events data
- Timestamps of power quality parameters
- Sequences of power quality events

- RMS values
- Waveforms
- Power values
- Spectra
- Complex spectra

Methods to trigger data logging:

- [Hysteresis](hysteresis.html)
- [Edge Triggers](edge-triggers.html)
- [Duration Triggers](duration-triggers.html)
- [Automatic Extension Triggering](automatic-extension-triggering.html)
- [Advanced Triggering](advanced-triggering.html)

Related concepts:

- Data Logging

<!--NI_TOPIC bundle=labview-electrical-power-toolkit path=unbalance.html language=enus -->
## TOPIC 00073: Unbalance

- bundle_id: `labview-electrical-power-toolkit`
- source_path: `unbalance.html`
- source_url: https://docs-be.ni.com/bundle/labview-electrical-power-toolkit/raw/resource/enus/unbalance.html
- document_id: `labview-electrical-power-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: This section describes the causes and effects of unbalance in three-phase electrical power systems. This section emphasizes the inefficiencies and potential damage that can result from unbalanced currents.Synchronous generators generate voltages in a three-phase electrical power system. A balanced t

### Unbalance

This section describes the causes and effects of unbalance in three-phase electrical
 power systems. This section emphasizes the inefficiencies and potential damage that can result
 from unbalanced currents.

- Voltages are equal in magnitude.
- Voltages have a mutual phase difference of 120 degrees.

The source of unbalance is usually unbalanced loads, especially low-voltage loads and
 medium-voltage loads. Most of these loads are single-phase loads
 that can cause unsymmetrical voltage drops in each phase of a
 three-phase electrical power system. Consequently, voltages at
 all nodes of the system become unbalanced. Three-phase loads in
 high-voltage systems, such as arc furnaces and railway-traction
 supplies, can also introduce unbalance. Another source of
 unbalance is the difference between phases in a three-phase
 equipment. Because of different values of phase parameters, the
 values of voltage loss in each phase are different.
 Unsymmetrical transformer windings can cause a balanced current
 to flow through unbalanced impedance, which can also produce
 unbalance.

A three-phase electrical power system becomes inefficient when there are unbalanced currents
 flowing in the system. The following are some consequences of
 unbalance:

- Losses of power and energy.
- Overheating that may damage components, such as motors, generators, transformers, and
 wiring.
- Unbalance at all nodes.

- [Symmetrical Components](symmetrical-components.html)
- [Measuring Unbalance](measuring-unbalance.html)

<!--NI_TOPIC bundle=labview-electrical-power-toolkit path=user-manual-welcome.html language=enus -->
## TOPIC 00074: LabVIEW Electrical Power Toolkit User Manual

- bundle_id: `labview-electrical-power-toolkit`
- source_path: `user-manual-welcome.html`
- source_url: https://docs-be.ni.com/bundle/labview-electrical-power-toolkit/raw/resource/enus/user-manual-welcome.html
- document_id: `labview-electrical-power-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The LabVIEW Electrical Power Toolkit User Manual provides detailed descriptions of the product functionality and the step by step processes for use. Looking for Something Else?For information not found in the User Manual for your product, such as specifications and API reference, browse Related Info

### LabVIEW Electrical Power Toolkit
 User Manual

The LabVIEW Electrical Power Toolkit User Manual provides detailed
 descriptions of the product functionality and the step by step processes for use.

#### Looking for Something Else?

For information not found in the User Manual
 for your product, such as specifications and API reference, browse *Related
 Information*.

Related information:

- Download LabVIEW Electrical Power Toolkit
- LabVIEW Electrical Power Toolkit Release Notes
- Interactive Activation Guide
- LabVIEW Electrical Power Toolkit
 Programming Reference Manual
- Discussion Forums
- NI Learning Center
- Hardware and Software Operating System
 Compatibility

<!--NI_TOPIC bundle=labview-electrical-power-toolkit path=voltage-and-current-signals.html language=enus -->
## TOPIC 00075: Voltage and Current Signals

- bundle_id: `labview-electrical-power-toolkit`
- source_path: `voltage-and-current-signals.html`
- source_url: https://docs-be.ni.com/bundle/labview-electrical-power-toolkit/raw/resource/enus/voltage-and-current-signals.html
- document_id: `labview-electrical-power-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Voltage and current signals are common signal types for electrical power analysis.Voltage Signals Voltage is the energy per unit charge flowing through a conductor. The following equation describes the voltage associated with an alternating current. where V[0] is the peak voltage, or the maximum amp

### Voltage and Current Signals

Voltage and current signals are common signal types for electrical power analysis.

#### Voltage Signals

Voltage is the energy per unit charge flowing through a conductor. The following
 equation describes the voltage associated with an alternating current.

[IMAGE alt='image' src='GUID-06076893-558B-4300-B091-66C45A307C26-a5.gif']

where V<sub>0</sub> is the peak voltage, or the maximum
 amplitude of the voltage waveform; Φ is the initial phase;
 t is the time.

You can obtain voltage signals through the analog input channel of a data acquisition
 device that contains an analog-to-digital converter (ADC). An ADC converts a
 continuous analog voltage signal into a discrete digital signal.

#### Current Signals

DC is the flow of electric charge with a constant polarity. Batteries, fuel cells, photovoltaic cells, dynamos, and thermocouples produce DC.

AC is the flow of electric charge that periodically reverses polarity. AC generators and alternators produce AC. AC typically takes the form of a sine wave that oscillates at a fundamental frequency of 50 Hz or 60 Hz, depending on geographic locations.

You can obtain current signals through the analog input channel of a data acquisition device that contains an analog-to-digital converter (ADC). An ADC converts a continuous analog current signal into a discrete digital current signal.

#### Transformers

A transformer transfers electrical energy between two circuits in an electrical power system or an electrical device. A transformer consists of two inductively coupled coils that wind around a ferromagnetic core. A time-varying current in the primary winding creates a varying magnetic flux in the core that, subsequently, induces a voltage in the secondary winding. The induced voltage in the secondary winding is proportional to the primary voltage. The following figure shows a transformer as a circuit element.

[IMAGE alt='image' src='GUID-3939733A-545B-47B4-80CC-B6EE8A7E8D20-a5.gif']

In an ideal transformer, the ratio of the secondary voltage to the primary voltage is equal to the ratio of the number of turns on the secondary coil to the primary coil.

[IMAGE alt='image' src='GUID-98E0545B-C060-4E90-BAF9-BBC37203FEA4-a5.gif']

You use transformers to step up the voltage at the source before transmission and step down the voltage at the destination.

Voltage transformers are useful in high-voltage circuits for measurement and protection of electrical components. Voltage transformers can transform a high voltage to a lower voltage that you can measure safely. You can use a low voltage to operate a protective relay.

Current transformers are useful for measurement and protection of electrical components. A current transformer induces a current in the secondary winding that is proportional to the current in the primary winding. You can use a current transformer to measure a high current in an electrical circuit by inducing a low current in the secondary winding that you can safely measure.

Parent topic:

Electrical Power Signals

<!--NI_TOPIC bundle=labview-electrical-power-toolkit path=voltage-dips-swells-and-interruptions.html language=enus -->
## TOPIC 00076: Voltage Dips, Swells, and Interruptions

- bundle_id: `labview-electrical-power-toolkit`
- source_path: `voltage-dips-swells-and-interruptions.html`
- source_url: https://docs-be.ni.com/bundle/labview-electrical-power-toolkit/raw/resource/enus/voltage-dips-swells-and-interruptions.html
- document_id: `labview-electrical-power-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Depending on the severity and duration of the variation in voltage, you can classify voltage events as follows: Voltage dips Voltage swells Voltage interruptions Different standards define differently on a voltage event. IEC 61000-4-30:2008 defines voltage dips, swells, and interruptions as variatio

### Voltage Dips, Swells, and Interruptions

Depending on the severity and duration of the variation in voltage, you can classify voltage
 events as follows:

- Voltage dips
- Voltage swells
- Voltage interruptions

IEC 61000-4-30:2008

- A voltage dip occurs when the voltage falls below 90% of the nominal or sliding
 reference voltage.
- A voltage swell happens when the voltage rises above 110%.
- An interruption is when the voltage drops below 10%.

IEC 61000-4-30:2008

IEEE Std 1159-1995

IEEE Std 1159-1995

The LabVIEW Electrical Power Toolkit obtains voltage events data in compliance with IEC
 61000-4-30:2008.

#### Voltage Dips

A voltage dip is a decrease in the RMS voltage below the nominal voltage or a sliding
 reference voltage. The decrease lasts from half a cycle to several seconds.

Faults on
 an electrical power system cause voltage dips. For example, a short circuit can cause
 voltage dips. A short circuit produces a large current to flow, which results in a drop in
 the voltage across system loads. A short circuit can cause a component to draw a large
 amount of energy because the energy is proportional to the square of the current. This
 excessive energy flow can potentially damage the component. Short circuits are usually the
 result of an insulation breakdown or an overvoltage caused by switching operations or
 lightning strikes.

#### Voltage Swells

A voltage swell is an increase in the RMS voltage above the nominal voltage or a sliding
 reference voltage. The increase lasts from half a cycle to several seconds.

- Switching off large loads
- Capacitor banks energizing
- Transfer of loads from one power source to another power source

#### Voltage Interruptions

A voltage interruption occurs when the RMS voltage drops significantly. A significant
 voltage drop occurs when the RMS voltage decreases to less than a small percentage of the
 nominal voltage or when there is a complete loss of voltage.

- Malfunction of a switching device
- Intentional or accidental activation of a fuse, circuit breaker, or recloser due to
 faults and disturbances

#### Effects of Voltage Events

A change in voltage can lead to an increase or decrease in the energy supplied to
 components within an electrical power system. This change results in an energy level that
 differs from what normal operations need. A drop in energy during a voltage dip can lead to
 equipment resetting or shutting down. The drop can also cause mechanical devices, like
 motors, to stall or overheat. An increase in voltage during a voltage swell can cause
 immediate or long-term breakdown of components because of overheating.

When a voltage
 interruption occurs, the voltage level quickly drops to zero or nearly zero. As a result,
 the components within an electrical power system do not receive any energy during these
 interruptions. A voltage interruption can cause a complete shutdown of equipment. The
 voltage interruption might also lead to damage. A voltage interruption over a large
 geographical area that lasts for a long time is known as a
 *blackout*.

Parent topic:

Voltage Events

Related concepts:

- Disturbance Data Logging

<!--NI_TOPIC bundle=labview-electrical-power-toolkit path=voltage-events.html language=enus -->
## TOPIC 00077: Voltage Events

- bundle_id: `labview-electrical-power-toolkit`
- source_path: `voltage-events.html`
- source_url: https://docs-be.ni.com/bundle/labview-electrical-power-toolkit/raw/resource/enus/voltage-events.html
- document_id: `labview-electrical-power-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: A voltage event is an abnormal and temporary variation in the RMS voltage in an electrical power system. Different standards define differently on a voltage event. The LabVIEW Electrical Power Toolkit obtains voltage events data in compliance with IEC 61000-4-30:2008.

### Voltage Events

A voltage event is an abnormal and temporary variation in the RMS voltage in an electrical power
 system. Different standards define differently on a voltage event. The LabVIEW Electrical
 Power Toolkit obtains voltage events data in compliance with IEC
 61000-4-30:2008.

- [Voltage Dips, Swells, and Interruptions](voltage-dips-swells-and-interruptions.html)
- [Measuring Voltage Dips and Swells](measuring-voltage-dips-and-swells.html)
- [Measuring Voltage Interruptions](measuring-voltage-interruptions.html)
- [Rapid Voltage Changes](rapid-voltage-changes.html)
- [Flagging](flagging.html)
- [Transients](transients.html)
- [Events Indexes](events-indexes.html)

Related concepts:

- Data Logging
- Power Quality

<!--NI_TOPIC bundle=labview-electrical-power-toolkit path=voltage-fluctuations.html language=enus -->
## TOPIC 00078: Voltage Fluctuations

- bundle_id: `labview-electrical-power-toolkit`
- source_path: `voltage-fluctuations.html`
- source_url: https://docs-be.ni.com/bundle/labview-electrical-power-toolkit/raw/resource/enus/voltage-fluctuations.html
- document_id: `labview-electrical-power-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Voltage fluctuations are amplitude modulations of the fundamental frequency. The following equation describes a voltage, v, at a given time, t: where V is the RMS voltage, f[0] is the fundamental frequency, and m(t) is the modulation. By choosing an appropriate expression for m(t), you can use the p

### Voltage Fluctuations

Voltage fluctuations are amplitude modulations of the fundamental frequency. The following
 equation describes a voltage, v, at a given time,
 t:

[IMAGE alt='image' src='GUID-96FDAC33-6911-4CC0-B47D-CB44C5EDD335-a5.gif']

where V is the RMS voltage, f<sub>0</sub> is the
 fundamental frequency, and m(t) is the modulation.
 By choosing an appropriate expression for m(t),
 you can use the previous equation to describe any voltage fluctuation. For example, for
 a sinusoidal voltage fluctuation, you can express the modulation,
 m(t), by using the following equation:

[IMAGE alt='image' src='GUID-52F7FC36-5BB4-4FA4-9ECA-1418FA63ED4C-a5.gif']

where M is the modulation amplitude, f<sub>M</sub> is the modulation frequency, and φ<sub>M</sub> is the initial phase of the modulation.

#### Causes of Voltage Fluctuations

Voltage fluctuations in an electrical power system typically come from loads that cause variations in voltage and devices that continuously draw rapidly changing currents.

Loads that cause variations in voltage include refrigerators, air conditioners, photocopiers, and variable speed drives. These loads usually have an electric motor that draws a high current when the electric motor starts.

Devices that continuously draw rapidly changing currents are usually industrial devices like arc furnaces, arc welders, and wind turbines. These industrial devices often connect to transmission grids and can cause voltage fluctuations that lead to light flickers over large geographical areas.

Parent topic:

Flickers

<!--NI_TOPIC bundle=labview-electrical-power-toolkit path=waveform-data-logging.html language=enus -->
## TOPIC 00079: Waveform Data Logging

- bundle_id: `labview-electrical-power-toolkit`
- source_path: `waveform-data-logging.html`
- source_url: https://docs-be.ni.com/bundle/labview-electrical-power-toolkit/raw/resource/enus/waveform-data-logging.html
- document_id: `labview-electrical-power-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Waveform data is useful for the analysis of power quality, system faults, motor initialization, breakers, and timing.Waveform data typically is resampled raw voltage and current values in the cycle domain for analog input channels. For digital channels, waveform data is the status of relay switches.

### Waveform Data Logging

Waveform data is useful for the analysis of power quality, system faults, motor initialization,
 breakers, and timing.

Waveform data typically is resampled raw voltage and current values in the cycle domain for
 analog input channels. For digital channels, waveform data is the status of relay
 switches. Waveform data logging starts when an analog input signal crosses a trigger
 threshold or when a digital input channel changes its state. You also can manually start
 waveform data logging.

Waveform data usually contains pre- and post-fault data, which are values logged for several
 cycles before and after a trigger fires. Pre- and post-fault data are useful in
 determining the causes and effects of faults. By default, the LabVIEW Electrical Power
 Toolkit samples data at 192 samples per cycle. However, because the system frequency
 synchronizes with the sample rate, the number of samples per second may change as the
 system frequency changes. A higher sample rate ensures a more accurate description of a
 system. Because logged waveform data usually contains hundreds of samples acquired over
 one second, you need to take the amount of system memory into consideration. For
 example, data logged at 256 samples per cycle for a 50 Hz system occupies 102.4 KB
 system memory every second.

Parent topic:

Data Logging

<!--NI_TOPIC bundle=labview-electrical-power-toolkit path=wiring.html language=enus -->
## TOPIC 00080: Wiring

- bundle_id: `labview-electrical-power-toolkit`
- source_path: `wiring.html`
- source_url: https://docs-be.ni.com/bundle/labview-electrical-power-toolkit/raw/resource/enus/wiring.html
- document_id: `labview-electrical-power-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Line voltage is the voltage between any two live wires in a three-phase electrical power system. Phase voltage is the voltage between any live wire and the neutral wire in a three-phase electrical power system. The following table shows the wiring methods that the LabVIEW Electrical Power Toolkit su

### Wiring

Line voltage is the voltage between any two live wires in a three-phase electrical power system.
 Phase voltage is the voltage between any live wire and the neutral wire in a three-phase
 electrical power system. The following table shows the wiring methods that the LabVIEW
 Electrical Power Toolkit supports.

Note

| Wiring Method | Illustration |
| --- | --- |
| Four phase voltage channels and four current channels |  |
| Three phase voltage channels and four current channels |  |
| Three line voltage channels and four current channels |  |
| Three phase voltage channels and three current channels |  |
| Three line voltage channels and three current channels |  |
| Three phase voltage channels and two current channels |  |
| Three line voltage channels and two current channels |  |
| One phase voltage channel and one current channel |  |

Parent topic:

Connections and Wiring

<!--NI_TOPIC bundle=labview-electrical-power-toolkit path=wye-connections.html language=enus -->
## TOPIC 00081: Wye Connections

- bundle_id: `labview-electrical-power-toolkit`
- source_path: `wye-connections.html`
- source_url: https://docs-be.ni.com/bundle/labview-electrical-power-toolkit/raw/resource/enus/wye-connections.html
- document_id: `labview-electrical-power-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: In a wye connection, each transformer coil connects one end to each other and each transformer connects the other end to incoming wires or to supplying power to loads. The following figure shows a wye connection. In the previous figure, three live wires, A, B, and C, connect with a neutral wire N at

### Wye Connections

In a wye connection, each transformer coil connects one end to each other and each transformer
 connects the other end to incoming wires or to supplying power to loads. The following
 figure shows a wye connection.

[IMAGE alt='image' src='GUID-976D98D6-21EF-45D1-A0B8-69346DC228FC-a5.gif']

In the previous figure, three live wires, A, B, and C, connect with a neutral wire N at the
 center. V<sub>AN</sub>,
 V<sub>BN</sub>, and
 V<sub>CN</sub> are the three-phase
 voltages.

The following equation shows the relationship of the voltages between any two phases or lines,
 V<sub>LL</sub>, and the phase voltage of the
 phase with respect to the neutral point,
 V<sub>LN</sub>, in a wye connection.

[IMAGE alt='image' src='GUID-5ED7D0D6-34E1-45CF-B1F0-1CA61F003CD9-a5.gif']

High voltage transmission systems typically use wye connections. Wye connections offer the
 advantage of providing multiple voltages.

Parent topic:

Connections and Wiring
