# NI DOCUMENT BUNDLE: ni-dcpower-ac-noise-rejection-dc-measurements

<!--NI_BUNDLE_CHUNK bundle=ni-dcpower-ac-noise-rejection-dc-measurements start=1 end=1 -->
<!--NI_TOPIC bundle=ni-dcpower-ac-noise-rejection-dc-measurements path=ni-dcpower-ac-noise-rejection-dc-measurements.html language=enus -->
## TOPIC 00001: AC Noise Rejection in NI-DCPower Measurements

- bundle_id: `ni-dcpower-ac-noise-rejection-dc-measurements`
- source_path: `ni-dcpower-ac-noise-rejection-dc-measurements.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-ac-noise-rejection-dc-measurements/raw/resource/enus/ni-dcpower-ac-noise-rejection-dc-measurements.html
- document_id: `ni-dcpower-ac-noise-rejection-dc-measurements`
- page_type: `leaf`
- content_type: `topic`
- source_description: How NI Power Supplies and SMUs Reject AC Noise from Measurements You can manipulate the aperture time of measurements made with NI-DCPower instruments to reject specific AC noise frequencies in DC voltage and current measurements. Each measurement that an NI-DCPower instrument returns is an average

### AC Noise Rejection in NI-DCPower Measurements

#### How NI Power Supplies and SMUs Reject
 AC Noise from Measurements

You can manipulate the aperture time of measurements made
 with NI-DCPower instruments to reject specific AC noise
 frequencies in DC voltage and current measurements.

Each measurement that an NI-DCPower
 instrument returns is an average of one or more higher-speed samples. The exact rate of these
 samples varies by instrument, but for all instruments, it is a multiple of 50 Hz and 60 Hz to enable
 rejection of power line noise.

You can reject AC noise by adjusting the number of samples in a measurement so that the
 aperture time of the measurement is a multiple of the AC noise period. For most NI-DCPower instruments, you can set the aperture time directly;
 for a few older instruments, you can configure the number of samples to average to reject AC
 noise.

When you know the frequency of noise you want to reject, you can use the aperture time, which
 determines the number of samples in a measurement, to reject that frequency. Setting the
 aperture time to a multiple of an AC noise frequency averages out that frequency from your
 measurements.

Additionally, several NI-DCPower
 instruments support multiple noise rejection profiles. The choice of noise rejection profile
 offers a tradeoff between measurement speed and effectiveness of noise rejection.

##### Normal DC Measurement Noise
 Rejection

With normal noise rejection, the instrument assigns
 equal weight to each sample. This setting mimics the behavior of most traditional
 power supplies and SMUs.

Normal noise rejection is the default behavior for all NI-DCPower instruments.

[Figure 1](ni-dcpower-ac-noise-rejection-dc-measurements.html#GUID-35FD8C5D-5948-4D6A-AE42-FBDF0CD819D1__FIGWITHCALLOUTS_TRQ_TYH_5MB) shows normal weighting, with aperture times on the x-axis and relative weighting on the y-axis.

Figure 1.

[IMAGE alt='image' src='GUID-AA091212-0643-4B4D-9814-8370AAF5123A-a5.svg']

1. Sample 1
2. Sample 2
3. Sample 3
4. Sample 4

[Figure 2](ni-dcpower-ac-noise-rejection-dc-measurements.html#GUID-35FD8C5D-5948-4D6A-AE42-FBDF0CD819D1__FIG_MXW_BZH_5MB) shows the resulting noise rejection as a function of frequency, with
 multiples of 1 / *Aperture Time* on the x-axis and magnitude response, in dB, on the y-axis.

Figure 2.

[IMAGE alt='image' src='GUID-F8B69F25-5B54-46FE-AB93-4CDE9A1336C5-a5.svg']

The best frequency rejection is available only near integer
 multiples of 1 / *Aperture Time*. You can achieve the fastest
 possible readings along with good power-line noise rejection by setting the
 aperture to one power-line cycle (PLC) and noise rejection to
 Normal.

###### Support for Normal AC Noise
 Rejection

All NI-DCPower support normal AC noise rejection, the
 default noise rejection behavior of NI-DCPower
 instruments.

##### Second-Order DC Measurement Noise
 Rejection

With second-order noise rejection, the instrument
 assigns a triangular weighting to measurement samples. Samples taken in the middle
 of the aperture time have more weight than samples taken at the beginning and end of
 that measurement.

[Figure 1](ni-dcpower-ac-noise-rejection-dc-measurements.html#GUID-A099BFEB-7504-4048-87B1-D43481E024AC__FIGWITHCALLOUTS_CFC_4C3_5MB) shows second-order weighting, with aperture times on the x-axis and relative weighting on the y-axis.

Figure 3.

[IMAGE alt='image' src='GUID-541B6CA2-758D-4751-B9F9-3F996645EFFF-a5.svg']

1. Sample 1
2. Sample 2
3. Sample 3

[Figure 2](ni-dcpower-ac-noise-rejection-dc-measurements.html#GUID-A099BFEB-7504-4048-87B1-D43481E024AC__FIG_XW2_WC3_5MB) shows the resulting noise rejection as a function of
 frequency, with multiples of 1 / *Aperture Time* on the x-axis and magnitude response, in dB, on
 the y-axis.

Figure 4.

[IMAGE alt='image' src='GUID-3AB106C3-EB73-425C-8B35-1DD95EE51593-a5.svg']

With second-order noise rejection, the instrument provides
 superior noise rejection even near multiples of 1 / *Aperture
 Time*, and noise rejection increases more rapidly with
 frequency compared to normal noise rejection. Notches are also wider than
 they would be with normal weighting, which results in less sensitivity to
 slight variations in noise frequency.

Use second-order noise rejection if you need better power-line
 noise rejection or better high-frequency noise rejection than you can obtain
 with normal noise rejection.

You can achieve the fastest possible readings with
 second-order noise rejection, along with excellent power-line noise
 rejection, by setting the aperture to two power-line cycles (PLC) and noise
 rejection to Second-Order.

In this configuration, one measurement is produced in the
 first full aperture, followed by two measurements for each subsequent
 aperture time. This results in approximately the same measurement rate as
 normal filtering for large measure records.

###### Support for Second-Order AC Noise
 Rejection

The following NI-DCPower instruments support second-order AC noise rejection:

- PXIe-4135
- PXIe-4137
- PXIe-4139
- PXIe-4141
- PXIe-4143
- PXIe-4145
- PXIe-4147
- PXIe-4162
- PXIe-4163

#### Choosing an AC Noise Rejection Profile for NI-DCPower Instruments

For some NI-DCPower instruments, you have a choice of AC
 noise rejection profiles: *normal* and *second-order*. Normal noise
 rejection is the default noise rejection behavior for all NI-DCPower instruments, while second-order noise rejection can provide better frequency
 rejection in some situations.

The length of the measurement aperture time
 affects which noise frequencies are rejected. The noise rejection profile changes how
 frequencies are rejected with respect to the measurement aperture time and affects the minimum
 time required for the instrument to make a single measurement.

##### Support
 for AC Noise Rejection Profiles

All NI-DCPower support normal AC noise rejection, the
 default noise rejection behavior of NI-DCPower
 instruments.

The following NI-DCPower instruments support second-order AC noise rejection:

- PXIe-4135
- PXIe-4137
- PXIe-4139
- PXIe-4141
- PXIe-4143
- PXIe-4145
- PXIe-4147
- PXIe-4162
- PXIe-4163

Choose the AC noise rejection profile that suits your application based on the
 following criteria.

| Lowest Frequency Rejection Notch | High-Frequency Noise Rejection | Minimum Measurement Time Required | Recommended Noise Rejection Profile |
| --- | --- | --- | --- |
| 1 / Aperture Time | Good | Shorter: Aperture Time | Normal |
| 2 / Aperture Time | Better | Longer: 2 × Aperture Time | Second-Order |

#### Rejecting AC Noise in DC Measurements with NI-DCPower

Many environments and systems include unwanted periodic signals that can degrade
 measurement quality. By manipulating measurement aperture time, you can use the NI-DCPower API to reject specific AC noise frequencies from
 measurements you make with NI-DCPower instruments.

With a short aperture time, measurements are completed faster, but
 noise from the environment, such as the 50 Hz or 60 Hz power line noise introduced by cabling,
 increases measurement uncertainty. Longer aperture times improve measurement
 resolution, and internal noise also decreases; your instrument specifications may
 describe this relationship. Specific aperture times can reject specific noise
 frequencies in DC measurements.

Different NI-DCPower instruments
 require different ways of using aperture time to reject noise. Additionally, some
 instruments support multiple noise rejection profiles that offer a trade-off between
 measurement speed and improved noise rejection.

Choose the noise rejection method supported by your instrument.

- Rejecting AC Noise in DC Measurements with Aperture Time
- Rejecting AC Noise in DC Measurements with Measurement Averaging

##### Rejecting AC Noise in DC Measurements
 with Aperture Time

Directly adjusting the aperture time of your
 measurements allows you to reject specific AC noise frequencies in your DC
 measurements with NI-DCPower.

Complete the following steps to reject AC noise
 frequencies by adjusting the aperture time of your measurements.

###### Support for Measurement Aperture
 Time

The following NI-DCPower instruments
 support direct control over measurement aperture time:

- PXIe-4112
- PXIe-4113
- PXI-4132
- PXIe-4135
- PXIe-4136
- PXIe-4137
- PXIe-4138
- PXIe-4139
- PXIe-4140
- PXIe-4141
- PXIe-4142
- PXIe-4143
- PXIe-4144
- PXIe-4145
- PXIe-4147
- PXIe-4162
- PXIe-4163

1. If your instrument supports multiple options, choose the noise
 rejection profile that suits your application.
  - Normal
    - Default behavior. Good
 noise rejection, shorter time per measurement
 required.
    - Best frequency rejection
 at nonzero integer multiples of 1 / Aperture
 Time
  - Second-Order
    - Available on some
 instruments. Best noise rejection, longer time per
 measurement required.
    - Best frequency rejection
 at nonzero integer multiples of 2 / Aperture
 Time
2. Based on the aperture time units and the noise rejection
 profile you intend to use, calculate the aperture time
 required to reject the frequency f (Hz)
 you need to reject. 
 
 Note Each NI-DCPower instrument supports discrete
 aperture times: an instrument-specific minimum value
 and integer multiples of that value. When you set an
 unsupported aperture time, NI-DCPower coerces the value to the nearest
 longer supported value for your instrument.
  - Aperture time units:
 seconds Noise Rejection ProfileTarget Aperture Time (s)Normal*Aperture Time* = 1 /
 fSecond-Order*Aperture Time* = 2 /
 f
  - Aperture time units: power
 line cycles (PLC) Noise Rejection
 ProfilePower Line FrequencyTarget Aperture Time
 (PLC)Normal60
 Hz*Aperture Time* = 60 Hz /
 f50
 Hz*Aperture Time* = 50 Hz /
 fSecond-Order60
 Hz*Aperture Time* = 2 × (60 Hz /
 f)50
 Hz*Aperture Time* = 2 × (50 Hz /
 f)
3. Configure the aperture time you calculated.
  1. Set the aperture time and the appropriate units
 with Configure Aperture
 Time.
  2. If using power line cycle units, provide the
 frequency of the AC power line for your system to
 Configure Power Line
 Frequency.
4. Use DC Noise Rejection to set the noise
 rejection profile you chose.

##### Rejecting AC Noise in DC Measurements
 with Measurement Averaging

For NI-DCPower
 instruments that do not support directly changing the aperture time, you can adjust
 the number of samples averaged in each measurement to influence the aperture time of
 your measurements, which allows you to reject specific AC noise
 frequencies.

The number of samples you choose to average in a
 measurement implicitly controls the aperture time based on the
 following relationship:

*Aperture Time* = *Samples To
 Average* / *Maximum Sample Rate*

where

- Samples To Average is the number of samples, as
 determined by Samples To Average ,
 that compose each measurement; the default value and valid
 range of samples to average depend on your instrument
- Maximum Sample Rate is the maximum sample rate of
 the instrument as documented in the specifications for your
 instrument

The overall hardware measurement rate of the
 instrument is the reciprocal of the aperture time.

Complete the following steps to reject AC noise
 frequencies by manipulating the aperture time of your measurements
 with measurement averaging.

###### Support for Measurement
 Averaging

The following NI-DCPower
 instruments support measurement averaging:

- PXI-4110
- PXI-4130
- PXIe-4154

1. Based on the frequency f (Hz) you need to
 reject and the maximum sample rate of your instrument as
 indicated in the specifications, calculate the number of
 samples you need to average to reject the frequency. 
 *Samples To Average* =
 *Maximum Sample Rate* /
 f
2. Set Samples To Average to the value you
 calculated. 
 Tip To improve noise
 reduction while keeping frequency rejection, you can
 use integer multiples of *Samples To
 Average*, as long as that multiple is a
 supported value of Samples To
 Average for your instrument and the
 longer aperture time that results is appropriate for
 your application.
 Note If you
 set the Samples To Average
 property in the Running state, the output channel
 measurements may move out of synchronization. If this occurs, set
 Reset Average Before
 Measurement to True
 before calling Measure
 Multiple in your program. You can set
 Reset Average Before
 Measurement to False
 after Measure Multiple
 runs.
