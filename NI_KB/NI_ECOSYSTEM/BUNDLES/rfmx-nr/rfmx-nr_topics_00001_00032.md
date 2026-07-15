# NI DOCUMENT BUNDLE: rfmx-nr

<!--NI_BUNDLE_CHUNK bundle=rfmx-nr start=1 end=32 -->
<!--NI_TOPIC bundle=rfmx-nr path=acp.html language=enus -->
## TOPIC 00001: Adjacent Channel Power

- bundle_id: `rfmx-nr`
- source_path: `acp.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr/raw/resource/enus/acp.html
- document_id: `rfmx-nr`
- page_type: `leaf`
- content_type: `concept`
- source_description: Adjacent channel power (ACP) measurement measures the power leakage from the carrier channels into the neighboring frequency channels, commonly referred to as offset channels. The following figure shows a typical carrier channel and offset channel configuration. 1 Typical Carrier Channel and Offset

### Adjacent Channel Power

Adjacent channel power (ACP) measurement measures the power leakage from
 the carrier channels into the neighboring frequency channels, commonly referred to as offset
 channels.

The following figure shows a typical carrier channel and offset
 channel configuration.

Figure 1.

[IMAGE alt='Digram of a Typical Carrier Channel and Offset Channel Configuration' src='GUID-DD28EB33-FB2B-4E7B-83D5-DD0A11054360-a5.gif']

#### Carrier Channels

Carriers are channels in which significant power
 is transmitted, and for which power leakage in the
 offset channels is measured. Multiple carriers are
 configured relative to the RF center frequency by
 specifying the carrier offset and integration
 bandwidth (IBW). Power in each carrier is measured
 by integrating the power in the specified IBW
 after applying the channel filter. The total
 carrier power measured is the aggregate power of
 all the active carriers.

Offset channel
 center frequency is specified relative to the
 center frequency of the closest carrier. The
 placement of offset channels from the nearest
 carrier is defined by the ACP offset frequency
 definition.

#### Offset Frequency Definition

The frequency offset of the offset channels from
 the closest carrier is defined by the ACP offset
 frequency definition. The offset frequency is
 defined in one of the following ways:

Carrier Center to Offset Center

Carrier Center to Offset Edge

Figure 2.

[IMAGE alt='Offset Frequency Definitions Diagram' src='GUID-841DD12B-3E69-4D04-B632-730C5EED213B-a5.png']

#### Offset Sideband

Two offset channels are configured on either side
 of the carriers when you set the ACP Offset
 Sideband to Both. Only one
 offset channel is configured when you set the ACP
 Offset Sideband to either
 Neg or
 Pos. A negative sideband
 creates a lower offset channel to the left of the
 leftmost carrier. A positive sideband creates an
 upper offset channel to the right of the rightmost
 carrier. You can independently configure the IBW,
 RRC filter, power reference, and relative
 attenuation for each offset channel.

#### Power Reference

Power reference refers to the carrier channel relative to which the offset channel power is
 measured. The power reference is one of the following carriers:

- Closest carrier —Power in the carrier with center frequency
 closest to the offset channel center frequency
- Highest carrier power —Highest power among all the active
 carriers
- Composite carrier —Total power of all the active carriers
- Specific carrier —Power in the carrier specified by the carrier
 index

Note

Note

#### RBW and Sweep Time

When you set the ACP RBW Auto property to True, the measurement sets
 the RBW using the following ratio:

Min (Carrier IBW, Offset Channel
 IBW):RBW<sub>3dB</sub> = 100, where RBW<sub>3dB</sub> is a value between 1 Hz
 and 1 MHz

When you set the ACP Sweep Time Auto property to
 True, the measurement sets the sweep time to the following
 values:

- k/RBW 3dB when the RBW filter is FFT based, where k is a
 constant which depends on the FFT window
- 10/RBW 3dB for other RBW filter types

For more information about RBW, sweep time, and averaging, refer to the topics in the
 *RFmx SpecAn User Manual*.

#### Power Measurement

The absolute power values measured are reported in dBm (integrated power) or dBm/Hz (power
 spectral density). The relative power values are not affected by the units specified. Use
 relative attenuation to compensate for external attenuation for each offset
 channel.

- ACP Meas Method = Normal
- ACP Meas Method = Dynamic Range

When the ACP Meas Method is set to
 Normal, the measurement acquires the signal using a wideband
 front-end filter. This measurement acquires the spectrum with a large span and perform
 FFT-based processing.

The following steps help improve the dynamic range of the
 measurement:

- Set the RF input attenuation such that the mixer operates at optimal operating level.
 Refer to the dynamic range chart of the device to know the optimum mixer level.
 Mixer Level = Reference Level - RF Attenuation
- The reference level must be adjusted to the power level of the test signal. Doing so
 sets the signal at the A/D converter (ADC) to full scale, which results in the best SNR
 and SFDR performance.
- Narrowband spectrum analysis mode allows dynamic range beyond that of the ADC.
- Re-ranging the reference level when measuring the distortion amplitude allows the best
 dynamic range.

When the ACP Meas Method is set to Dynamic
 Range, the measurement uses hardware features, such as the IF filter and IF
 gain.

- The measurement acquires the signal using narrowband IF filters available on the
 analyzer.
- Analog IF filters used for each offset channel may vary based on the device in
 use.
- Narrow bandwidth IF filters are used to acquire a spectrum closer to the carrier
 channel to filter out the high power seen from the carrier in the adjacent
 channels.
- A wideband IF filter is used to acquire a spectrum farther from the carrier to reduce
 measurement time.
- The carrier channels are not filtered.

To increase the power seen by the ADC of the digitizer, the measurement resets the
 ranges for each offset channel based on the reference level set for the measurement and the
 analog IF filters.

Note

| Supported Analyzer | IF Filters | Max RBW |
| --- | --- | --- |
| NI PXIe-5665 (3.6 GHz) | 300 kHz | 300 kHz |
| NI PXIe-5665 (14 GHz) | 300 kHz, 5 MHz | 300 kHz |
| NI PXIe-5668 | 300 kHz, 5 MHz | 300 kHz |

Note

#### Noise Compensation

Noise compensation enables the measurement of the inherent noise floor of the signal
 analyzer for the RF path used by the measurement, and uses this result to compensate the
 signal measurement. For a given set of measurement configurations and the state of the
 signal analyzer, noise floors are constant. Because measuring the noise floor adds to the
 measurement time, the noise floor results are cached so that the measurement can use it
 later. When the signal analyzer or measurement parameters change, the noise floor
 measurement is reinitiated to return valid measurements.

Note

Note

#### Custom ACP

Custom ACP enables you to perform ACP measurement on channels with custom settings. Set
 ACP Channel Configuration Type to Custom to enable
 Custom ACP. This allows you to change the following parameters in order to configure custom
 channels. These parameters are valid only for Custom ACP mode.

- Subblock Offset specifies the offset of the subblock measurement relative to the
 subblock center as computed in the Standard ACP mode.
- Subblock Integration Bandwidth specifies the integration bandwidth for subblock
 measurement.
- Carrier Integration Bandwidth specifies the integration bandwidth for carrier
 measurement.
- Number of Offsets specifies the number of configured offset channels.
- Offset Frequency specifies the offset frequency where the offset channel should be
 measured. This offset is with reference to the subblock/carrier shifted by Subblock
 Offset.
- Offset Integration Bandwidth specifies the integration bandwidth for offset channel
 measurement.
- Offset Sideband specifies which sidebands of the offset channel should be measured.

In Custom ACP mode, the parameters in the following table are configured as defined in
 the standard specifications.

| ACP Mode Parameter | Uplink | Downlink |
| --- | --- | --- |
| Offset Frequency Definition | Subblock Center to Offset Center | Carrier Center to Offset Center |
| Power Reference | Composite Subblock | Closest Carrier |

Parent topic:

RFmx NR Measurement Concepts

Related information:

- RFmx SpecAn User Manual

<!--NI_TOPIC bundle=rfmx-nr path=acquisition-bandwidth-optimization.html language=enus -->
## TOPIC 00002: Acquisition Bandwidth Optimization

- bundle_id: `rfmx-nr`
- source_path: `acquisition-bandwidth-optimization.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr/raw/resource/enus/acquisition-bandwidth-optimization.html
- document_id: `rfmx-nr`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can optimize the acquisition bandwidth for a multi-carrier measurement using the Acq BW Optimization Enabled property. This property places the acquisition center frequency at a different position than configured. When you set the Acq BW Optimization Enabled property to False, RFmx does not opti

### Acquisition Bandwidth Optimization

You can optimize the acquisition bandwidth for a multi-carrier measurement using the Acq
 BW Optimization Enabled property. This property places the acquisition center frequency
 at a different position than configured.

When you set the Acq BW Optimization Enabled property to False,
 RFmx does not optimize the acquisition bandwidth and the acquired bandwidth will be
 based on the Nyquist criterion. The value of the acquisition center frequency is same as
 the first subblock absolute frequency that you configure.

When you set the Acq BW Optimization Enabled property to True,
 RFmx positions the acquisition center frequency to acquire the least bandwidth based on
 the signal configuration. This reduces the acquisition sample rate and the
 amount of data processed for the measurement, thereby, improving the
 measurement speed. However, this might cause the LO of the analyzer to be positioned at
 a Non-DC subcarrier position. Hence, the measurement sensitive to LO leakage should have
 this property disabled.

The following image illustrates this property with an example.

Consider a user configuration where two component carriers of 10 MHz and 20 MHz
 bandwidths are placed at a distance of 15 MHz between their centers. Let the center
 frequency be configured at 1 GHz. The frequency offset with respect to the center
 frequency of CC1 is 0 Hz and of CC2 is 15 MHz.

[IMAGE alt='image' src='GUID-9FA36D82-1F7B-4EA3-85F0-CEFABE8FC8E0-a5.png']

If you set the Acq BW Optimization Enabled property to False, RFmx
 keeps the acquisition frequency same as the center frequency that you configure. In some
 cases, this leads to a higher acquisition bandwidth due to the asymmetric positioning of
 component carriers with respect to the center frequency as shown in the following
 image.

[IMAGE alt='image' src='GUID-9E807E06-ACAB-4A75-8BB1-93354CCFB7EE-a5.png']

If you set the Acq BW Optimization Enabled property to True, RFmx
 positions the acquisition frequency within the aggregated bandwidth to acquire the least
 acquisition bandwidth specified by the Nyquist criterion as shown in the following
 image. In this example, the acquisition bandwidth is reduced to 30 MHz and acquisition
 frequency is computed as the center of 'Subblock Bandwidth' bandwidth as shown
 below.

[IMAGE alt='image' src='GUID-74BC2B66-B5C4-4A7D-8648-93BD57A3C5D9-a5.png']

Parent topic:

Carrier Aggregation

<!--NI_TOPIC bundle=rfmx-nr path=carrier-aggregation.html language=enus -->
## TOPIC 00003: Carrier Aggregation

- bundle_id: `rfmx-nr`
- source_path: `carrier-aggregation.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr/raw/resource/enus/carrier-aggregation.html
- document_id: `rfmx-nr`
- page_type: `leaf`
- content_type: `concept`
- source_description: Carrier aggregation enables multiple carriers to be combined to support wider transmission bandwidths, thereby increasing the data rate. For more information about carrier aggregation, refer to section 5.4A of 3GPP TS 38.101-1 specification and section 5.4A of the 3GPP TS 38.101-2 specification. You

### Carrier Aggregation

Carrier aggregation enables multiple carriers to be combined to support wider
 transmission bandwidths, thereby increasing the data rate.

Note

3GPP TS
 38.101-1

3GPP TS 38.101-2

You can configure multiple carrier channels by specifying the carrier offsets. You can
 configure contiguous and non-contiguous carrier aggregation by configuring the spacing
 between carriers.

#### Types of Carrier Aggregation

- Intra-band Contiguous—Component carriers are placed side-by-side within the same
 operating frequency band. We can analyse these signals using RFmx NR by configuring
 component carriers in a single subblock.
- Intra-band Noncontiguous—Component carriers are placed with some gap within the same
 operating frequency band. We can analyse these signals using RFmx NR by configuring
 component carriers in multiple subblocks.
- Inter-band Noncontiguous—One or more component carriers are placed in different
 operating frequency bands. We can analyse these signals using RFmx NR by configuring
 component carriers in multiple subblocks.

[IMAGE alt='image' src='GUID-57EF71D6-E7F9-4A8B-8F39-81E074BFA455-a5.png']

- [Channel Spacing](channel-spacing.html)
- [E-UTRA NR - Dual Connectivity (EN-DC)](endc.html)
- [Subblock](subblock.html)
- [Acquisition Bandwidth Optimization](acquisition-bandwidth-optimization.html)

Parent topic:

RFmx NR Signal Configuration Concepts

<!--NI_TOPIC bundle=rfmx-nr path=channel-spacing.html language=enus -->
## TOPIC 00004: Channel Spacing

- bundle_id: `rfmx-nr`
- source_path: `channel-spacing.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr/raw/resource/enus/channel-spacing.html
- document_id: `rfmx-nr`
- page_type: `leaf`
- content_type: `concept`
- source_description: Channel spacing is the distance between center frequencies of two adjacent component carriers for intra-band contiguous carrier aggregation. The channel spacing between the center frequencies of contiguously aggregated component carriers is a multiple of channel raster and preserves orthogonality of

### Channel Spacing

Channel spacing is the distance between center frequencies of two adjacent component
 carriers for intra-band contiguous carrier aggregation.

The channel spacing between the center frequencies of contiguously aggregated component
 carriers is a multiple of channel raster and preserves orthogonality of the subcarriers.
 You can configure the value by setting the Channel Raster (Hz)
 property to the default value of 15 kHz. Channel raster for different NR operating Bands
 are defined in Table 5.4.2.3-1 of *3GPP TS 38.101-1* specification for
 FR1 and Table 5.4.2.3-1 of *3GPP TS 38.101-2* specification for
 FR2.

For more information about channel spacing, refer to section 5.4A.1 of the 3GPP
 TS 38.101-1 specification for FR1 and 5.4A.1 of the 3GPP TS
 38.101-2 specification for FR2.

#### Nominal Channel Spacing

Nominal channel spacing defines the spacing between carriers in each NR operating band
 with a defined channel raster. To configure nominal channel spacing, you need to set the
 CC Spacing Type property to Nominal.

For uplink, nominal channel spacing is computed using the below formula:

For NR operating bands with a 100 kHz channel raster:

[IMAGE alt='image' src='GUID-E5866D71-9109-4140-BACB-CE972E9AB5F6-a5.png']

For NR operating bands without a 100 kHz channel raster:

[IMAGE alt='image' src='GUID-DDD2827C-18A2-492E-9C52-EABF9C6F2960-a5.png']

with n = µ<sub>0</sub>

For NR operating bands with 60 kHz channel raster:

[IMAGE alt='image' src='GUID-D49C0668-BBD8-4C67-B7ED-E42C7F50A797-a5.png']

with n = µ<sub>0</sub>-2n

where BW<sub>Channel(1)</sub> and
 BW<sub>Channel(2)</sub> are the channel
 bandwidths of the two respective NR component carriers according to Table 5.3.2-1 with
 values in MHz, µ<sub>0</sub> is the largest µ value among the
 subcarrier spacing configurations supported in the operating band for the two channel
 bandwidths according to Table 5.3.5-1, and GB<sub>Channel(i)</sub> is the minimum guard
 band for the channel bandwidth i according to Table 5.3.3-1 for the
 said µ value with µ as defined in *3GPP
 TS 38.211* specification.

For more information about nominal channel spacing:

- For uplink, refer to section 5.4.1A of the 3GPP 38.101-1 
 specification and section 5.4A.1 of 3GPP 38.101-2 specification
 for FR1 and FR2, respectively.
- For downlink, refer to section 5.4.1.2 of the 3GPP 38.104 
 specification.

#### User-Specific Channel Spacing

You can configure the spacing type between component carriers by setting the CC Spacing
 Type property to User and configuring the component carrier
 frequency for each component carrier.

#### Channel Raster

Channel raster is the distance between neighboring channels in a frequency band. Channel
 raster defines the step-size for search procedure and consequently and influences the
 time UE will take to complete initial search procedure. Channel raster is used to
 compute the nominal spacing. For more information about Channel raster, refer to section
 5.4.2 of the *3GPP TS 38.101-1* specification.

Parent topic:

Carrier Aggregation

<!--NI_TOPIC bundle=rfmx-nr path=chp-overview.html language=enus -->
## TOPIC 00005: Channel Power Overview

- bundle_id: `rfmx-nr`
- source_path: `chp-overview.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr/raw/resource/enus/chp-overview.html
- document_id: `rfmx-nr`
- page_type: `leaf`
- content_type: `concept`
- source_description: Channel power (CHP) measures the RMS power in the carrier channel. The spectrum is configured for span, RBW, sweep time, and carrier channels. The channel filter is applied after RBW filtering and averaging and affects the measured power. The power units specify whether to report the integrated powe

### Channel Power Overview

Channel power (CHP) measures the RMS power in the carrier channel.

The spectrum is configured for span, RBW, sweep time, and
 carrier channels. The channel filter is applied
 after RBW filtering and averaging and affects the
 measured power. The power units specify whether to
 report the integrated power or the power spectral
 density of the channel.

The following figure shows the spectrum span and integration
 bandwidth.

Figure 8.

[IMAGE alt='Graph showing Spectrum Span and Integration Bandwidth' src='GUID-ABA7DCCD-379B-4CA6-B630-670743425FE6-a5.png']

#### Carrier Channels

Carriers
 are channels in which significant power is
 transmitted. You can configure multiple carriers
 relative to the RF center frequency by specifying
 the carrier offset and integration bandwidth (IBW).
 Power in each carrier is measured by integrating the
 power in the specified IBW after applying the
 channel filter. The total carrier power measured is
 the aggregate power of all the
 carriers.

#### RBW and Sweep Time

When
 you set the CHP RBW Auto property
 to True, the measurement sets
 the RBW using the following
 ratio:

*IBW:RBW<sub>3dB</sub>
 = 100*,

where
 RBW<sub>3dB</sub> is a value
 between 1 Hz and 1 MHz.

When you
 set the CHP Sweep Time Auto property to
 True, the measurement sets
 the sweep time to the following values:

- k/RBW 3dB when the RBW filter is FFT
 based, where k is a constant
 which depends on the FFT window
- 10/RBW 3dB for other RBW filter
 types

For more information about RBW, sweep time, and
 averaging, refer to the topics in the *RFmx
 SpecAn User Manual*.

Note

Parent topic:

RFmx NR Measurement Concepts

Related information:

- RFmx SpecAn User Manual

<!--NI_TOPIC bundle=rfmx-nr path=configuring-signal-configuration-concepts.html language=enus -->
## TOPIC 00006: RFmx NR Signal Configuration Concepts

- bundle_id: `rfmx-nr`
- source_path: `configuring-signal-configuration-concepts.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr/raw/resource/enus/configuring-signal-configuration-concepts.html
- document_id: `rfmx-nr`
- page_type: `leaf`
- content_type: `concept`

### RFmx NR
 Signal Configuration Concepts

- [Valid Channel Bandwidth and Subcarrier Spacing Combination](valid-channel-bandwidth-and-subcarrier-spacin.html) Valid channel bandwidth and spacing options for 5G NR enables accurate setup and testing in RFmx NR applications.
- [Symbol Phase Compensation](symbol-phase-compensation.html) Adjusts for phase discontinuities caused by differing center frequencies between transmitter and receiver in 5G NR signals, ensuring accurate analysis and measurement in RFmx NR applications.
- [TDD Signal Configuration](tdd-signal-configuration.html) Sets uplink/downlink timing for TDD-based 5G NR signals, improving signal integrity and compliance testing in RFmx NR workflows.
- [Resource Grid Configuration](resource-grid-configuration.html) Defines resource grid size and start for 5G NR carriers, enabling accurate bandwidth part alignment and signal analysis in RFmx NR.
- [Carrier Aggregation](carrier-aggregation.html) Carrier aggregation enables multiple carriers to be combined to support wider transmission bandwidths, thereby increasing the data rate.

<!--NI_TOPIC bundle=rfmx-nr path=endc.html language=enus -->
## TOPIC 00007: E-UTRA NR - Dual Connectivity (EN-DC)

- bundle_id: `rfmx-nr`
- source_path: `endc.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr/raw/resource/enus/endc.html
- document_id: `rfmx-nr`
- page_type: `leaf`
- content_type: `concept`
- source_description: RFmx supports carrier aggregation of LTE (E-UTRA) carriers and NR carriers as per sections 5.3B, 5.4B, 5.5B of 3GPP TS 38.101-3 specification. EN-DC Channel Spacing for Intra-Band Carrier Aggregation The nominal channel spacing between an E-UTRA carrier and an adjacent NR carrier for intra-band cont

### E-UTRA NR - Dual Connectivity (EN-DC)

RFmx supports carrier aggregation of LTE (E-UTRA) carriers and NR carriers as per
 sections 5.3B, 5.4B, 5.5B of *3GPP TS 38.101-3* specification.

#### EN-DC Channel Spacing for Intra-Band Carrier Aggregation

The nominal channel spacing between an E-UTRA carrier and an adjacent NR carrier for
 intra-band contiguous EN-DC is defined as following:

- For NR operating bands with 100 kHz channel raster: Nominal Channel Spacing =
 (BW E-UTRA_Channel + BW NR_Channel )/2
- For NR operating bands with 15 kHz channel raster: Nominal Channel Spacing =
 (BW E-UTRA_Channel + BW NR_Channel )/2 +{-5 kHz, 0 kHz, 5
 kHz}
- For NR operating bands with 30 kHz channel raster: Nominal Channel Spacing =
 (BW E-UTRA_Channel + BW NR_Channel )/2 +{-10 kHz, 0 kHz, 10
 kHz}

where BW<sub>E-UTRA_Channel</sub> and BW<sub>NR_Channel</sub> are the channel bandwidths
 of E-UTRA and NR carriers, respectively. The channel spacing can be adjusted depending
 on the channel raster to optimize performance in a particular deployment scenario. The
 adjustment may be configured with EN-DC nominal spacing adjustment.

For intra-band non-contiguous EN-DC, the channel spacing between E-UTRA and NR carriers
 shall be larger than the nominal channel spacing defined in this subclause. Contiguous
 carrier aggregation uses a single subblock for E-UTRA and NR carriers. Non-contiguous
 carrier aggregation uses separate subblocks for E-UTRA and NR carriers.

#### EN-DC Channel Bandwidth for Intra-Band Carrier Aggregation

For intra-band contiguous EN-DC, the aggregated channel bandwidth is the sum of
 individual NR and E-UTRA channel bandwidths assuming nominal EN-DC channel with 0 kHz
 offset spacing as specified in subclause 5.4 of *3GPP TS 38.101-3*
 specification.

ENBW = BW<sub>NR_Channel</sub> + BW<sub>E-UTRA_Channel</sub>

In cases where the NR sub-block and/or the E-UTRA sub-block itself is composed of
 intra-band contiguous CA carriers, the EN-DC aggregated channel bandwidth is the sum of
 the aggregated channel bandwidths of the NR and E-UTRA subblocks assuming nominal EN-DC
 channel spacing between the NR sub-block and E-UTRA sub-block.

ENBW = BW<sub>NR_Channel_CA</sub> + BW<sub>E-UTRA_Channel_CA</sub>

Intra-band contiguous EN-DC configurations are defined using intra-band contiguous EN-DC
 bandwidth class notation, where the first EN-DC bandwidth class letter indicates the
 number of contiguous E-UTRA carriers, and the second EN-DC bandwidth class letter
 indicates the number of contiguous NR carriers. Applicable contiguous intraband EN-DC
 bandwidth classes are listed in table below.

| Intra-Band Contiguous EN-DC Bandwidth Class | Number of Contiguous CC |  |
| --- | --- | --- |
| E-UTRA | NR |  |
| AA | 1 | 1 |
| CA | 2 | 1 |
| DA | 3 | 1 |

EN-DC configurations and bandwidth combination sets are defined for intra-band contiguous
 EN-DC in Table 5.3B.1.2-1 of *3GPP 38.101-3* specification.

#### Radio Access Technology (CC RAT)

The CC RAT specifies if a carrier is an NR or an EUTRA carrier when using dual
 connectivity (EN-DC) signal.

Parent topic:

Carrier Aggregation

<!--NI_TOPIC bundle=rfmx-nr path=faqs.html language=enus -->
## TOPIC 00008: FAQs

- bundle_id: `rfmx-nr`
- source_path: `faqs.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr/raw/resource/enus/faqs.html
- document_id: `rfmx-nr`
- page_type: `leaf`
- content_type: `concept`
- source_description: Answers common questions about RFmx NR features and measurements. Why do spectrum traces have more variation after noise compensation as compared to the spectrum without noise compensation?Example: assume that without noise compensation, the measured noise power is 5E–6 ± 0.5E–6 watts. The correspon

### FAQs

Answers common questions about RFmx NR features and
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

Parent topic:

RFmx NR Measurement Concepts

<!--NI_TOPIC bundle=rfmx-nr path=measurement-concepts.html language=enus -->
## TOPIC 00009: RFmx NR Measurement Concepts

- bundle_id: `rfmx-nr`
- source_path: `measurement-concepts.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr/raw/resource/enus/measurement-concepts.html
- document_id: `rfmx-nr`
- page_type: `leaf`
- content_type: `concept`

### RFmx NR
 Measurement Concepts

- [Adjacent Channel Power](acp.html) Adjacent channel power (ACP) measurement measures the power leakage from the carrier channels into the neighboring frequency channels, commonly referred to as offset channels.
- [Channel Power Overview](chp-overview.html) Channel power (CHP) measures the RMS power in the carrier channel.
- [NR Channel Power](nr-chp.html) RFmx NR channel power (CHP) measurements for NR signals include bandwidth integration and carrier aggregation.
- [NR Modulation Accuracy](nr-modulation-accuracy.html) NR modulation accuracy measures modulation accuracy for 5G NR signals, providing EVM and error analysis to validate performance in RFmx NR applications.
- [NR Occupied Bandwidth](nr-occupied-bandwidth.html) Occupied bandwidth (OBW) measures the bandwidth that occupies a certain power specified as a percentage of the total power in the acquired spectrum.
- [Spectral Emission Mask](sem-overview.html) Measures spectrum emissions for 5G NR signals, ensuring compliance with emission masks and standards in RFmx NR analysis.
- [NR Uplink Spectral Emission Mask](nr-uplink-sem.html) Measures the uplink spectrum emission mask for 5G NR signals, ensuring compliance with emission limits in RFmx NR testing workflows.
- [NR Uplink EN-DC Spectral Emission Mask](nr-uplink-en-dc-sem.html) Measures Spectrum Emission Mask for 5G NR uplink in EN-DC mode, ensuring compliance with emission limits and validating transmitter performance in RFmx NR.
- [NR Downlink Spectral Emission Mask](nr-downlink-sem.html) Measures the downlink spectrum emission mask for 5G NR signals, ensuring compliance with emission limits in RFmx NR testing workflows.
- [NR Transmit Power](nr-transmit-power.html) Measures total transmit power for 5G NR signals, ensuring compliance with power limits and validating performance in RFmx NR testing workflows.
- [Noise Compensation Algorithm](noise-compensation-algorithm.html) Compensates for noise during 5G NR signal testing, ensuring precise modulation metrics and reliable RFmx NR measurements.
- [NR Power Vs Time](nr-power-vs-time.html) Measures 5G NR signal power variations over time, ensuring compliance with transmission masks and validating performance in RFmx NR testing workflows.
- [Noise Fundamentals](noise-fundamentals.html) Introduces key concepts of noise in RF measurements, explaining its impact on 5G NR signal analysis and accuracy in RFmx NR testing workflows.
- [FAQs](faqs.html) Answers common questions about RFmx NR features and measurements.

<!--NI_TOPIC bundle=rfmx-nr path=new-features-and-changes.html language=enus -->
## TOPIC 00010: RFmx NR New Features and Changes

- bundle_id: `rfmx-nr`
- source_path: `new-features-and-changes.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr/raw/resource/enus/new-features-and-changes.html
- document_id: `rfmx-nr`
- page_type: `leaf`
- content_type: `concept`
- source_description: Learn about updates, including new features and behavior changes, introduced in each version of RFmx NR. Discover what is new in the latest releases of RFmx NR.If you cannot find new features and changes for your version, it might not include user-facing updates. However, your version might include

### RFmx NR
 New Features and Changes

Learn about updates, including new features and behavior changes, introduced in each
 version of RFmx NR.

RFmx NR

Note

Release Notes

Related concepts:

- RFmx NR New Features and Changes

Related information:

- Software and Driver Downloads

#### RFmx NR
 2026 Q2 Changes

The RFmx NR 2026 Q2 release adds support for NTN
 Uplink Spectral Emission Masks. This release also includes behavior changes with ACP
 measurements that use the Sequential FFT measurement method.

##### New
 Features

- SEM measurement for the following NTN Uplink Spectral Emission Masks: NS_09N, NS_10N,
 NS_11N, and NS_12N.

##### Behavior
 Changes

This version of RFmx NR updates support
 for the following feature:

- Adjacent Channel Power (ACP): When you use the Sequential FFT 
 measurement method, you can configure the Configuring the Number of Analysis
 Threads property to a value greater than 1.

#### RFmx NR
 2026 Q1 Changes

Learn about new features, behavior changes, and other updates in RFmx NR 2026 Q1.

This version of the RFmx NR adds support for the
 following features:

- Added support for the Power Integration Method API to the RFmx NR Occupied Bandwidth (OBW) measurement.
- Added support for NTN Band 250, 251, 253, 248 and 247.
- Added support for 3 MHz Channel Bandwidth for SEM
 measurement for NTN.
- Added support for 7 MHz Channel Bandwidth.
- Added support for Python API.
- Corrected the reference names of existing FRC A.10 and A.11.

#### RFmx NR 2025 Q4 Changes

Learn about new features, behavior changes, and other updates in RFmx NR 2025 Q4.

- Added support for Band n252.

#### RFmx NR 2025 Q3 Changes

Learn about new features, behavior changes, and other updates in RFmx NR 2025 Q3.

- Added support for Self-Cal Validity Check for PXIe-5860.
- Added support for UL 2x2 MIMO ModAcc measurement API.
- Added support for bands n68, n87, n88, and n110.

#### RFmx NR 2025 Q1 Changes

Learn about new features, behavior changes, and other updates in RFmx NR 2025 Q1.

- • Updated UTRA offsets in ACP measurement as per sections 6.5A 2.4.1.2 and 6.5A 2.4.2.4 of 3GPP TS 38.101-1 V18.7.0.

#### RFmx NR 2024 Q4 Changes

Learn about new features, behavior changes, and other updates in RFmx NR 2024 Q4.

##### New
 Features

This version of the RFmx NR
 adds support for the following features:

- Added ‘Peak EVM-High per Symbol Maximum Trace‘ and ‘Peak EVM-Low per Symbol
 Maximum Trace‘ APIs.

##### Behavior Changes

- Uninstalling RFmx NR software also removes any
 previous versions of RFmx NR .NET runtimes that
 were leaked in .NET Global Assembly Cache directory.

#### RFmx NR 2024 Q3 Changes

Learn about new features, behavior changes, and other updates in RFmx NR 2024 Q3.

- Support for UL PvT measurement for NTN bands
- Support for PXIe-5860

#### RFmx NR 2024 Q2 Changes

Learn about new features, behavior changes, and other updates in RFmx NR 2024 Q2.

- Support for 3 MHz Bandwidth
- Support for bands n31, n72, n105, n106, and n109
- Support for NTN bands n255 and n256
- Obsoleted the RFmxInstr Load All Configurations VI. Use the
 RFmxInstr Load Configurations VI, along with the appropriate
 RFmxInstr Load Options property, instead.

#### RFmx NR 2023 Q4 Changes

Learn about new features, behavior changes, and other updates in RFmx NR 2023 Q4.

- Support for Power Class 7 in IBE Measurement
- Support for 25 MHz and 30 MHz bandwidths in Uplink NS_35 mask in SEM
 Measurement
- Support for updated IBE limits according to Section 6.4A.2.1.0 in 3GPP
 38.101-1(V18.2) and Section 6.4A.2.0 18.2 in 3GPP 38.101-2(V18.2)
- Support for obtaining unprocessed I/Q data utilized for RFmx measurements

#### RFmx NR 2023 Q3 Changes

Learn about new features, behavior changes, and other updates in RFmx NR 2023 Q3.

- Support for Noise Compensation in ACP measurement for Sequential FFT mode
- Support for Reference Signal Transmit (RSTX) power measurement in ModAcc
 measurement
- Support for NS_03U and NS_21 (Rel-17 onwards) masks in SEM measurement
- Support for Band n54 in downlink SEM measurement

#### RFmx NR 2023 Q2 Changes

Learn about new features, behavior changes, and other updates in RFmx NR 2023 Q2.

- Support for Phase Offset measurement
- Support for Test Tolerance for NR-U band n46 in SEM measurement as per 3GPP
 Release 17 (December-2022)
- Speed improvements for Composite and Spectral measurements

<!--NI_TOPIC bundle=rfmx-nr path=noise-compensation-algorithm.html language=enus -->
## TOPIC 00011: Noise Compensation Algorithm

- bundle_id: `rfmx-nr`
- source_path: `noise-compensation-algorithm.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr/raw/resource/enus/noise-compensation-algorithm.html
- document_id: `rfmx-nr`
- page_type: `leaf`
- content_type: `concept`
- source_description: Compensates for noise during 5G NR signal testing, ensuring precise modulation metrics and reliable RFmx NR measurements. Noise compensation details are described by assuming the following model test setup. When the switch connects to the DUT path, the noise power measured by the signal analyzer, P[

### Noise Compensation Algorithm

Compensates for noise during 5G NR signal testing, ensuring precise modulation
 metrics and reliable RFmx NR measurements.

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

Parent topic:

RFmx NR Measurement Concepts

<!--NI_TOPIC bundle=rfmx-nr path=noise-fundamentals.html language=enus -->
## TOPIC 00012: Noise Fundamentals

- bundle_id: `rfmx-nr`
- source_path: `noise-fundamentals.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr/raw/resource/enus/noise-fundamentals.html
- document_id: `rfmx-nr`
- page_type: `leaf`
- content_type: `concept`
- source_description: Introduces key concepts of noise in RF measurements, explaining its impact on 5G NR signal analysis and accuracy in RFmx NR testing workflows. Thermal Noise Fidelity of electromagnetic circuits is most commonly compromised by the noise generated by the components constituting the circuit, among othe

### Noise Fundamentals

Introduces key concepts of noise in RF measurements, explaining its impact on 5G NR
 signal analysis and accuracy in RFmx NR testing
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

Parent topic:

RFmx NR Measurement Concepts

<!--NI_TOPIC bundle=rfmx-nr path=nr-chp.html language=enus -->
## TOPIC 00013: NR Channel Power

- bundle_id: `rfmx-nr`
- source_path: `nr-chp.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr/raw/resource/enus/nr-chp.html
- document_id: `rfmx-nr`
- page_type: `leaf`
- content_type: `concept`
- source_description: RFmx NR channel power (CHP) measurements for NR signals include bandwidth integration and carrier aggregation. The NR CHP measurement uses the configurations specified by 3GPP TS 38.521-1 specification. The period of measurement for NR CHP is at least the continuous duration of one sub-frame (1 ms)

### NR Channel Power

RFmx NR channel power (CHP) measurements for NR signals include bandwidth integration
 and carrier aggregation.

The NR CHP measurement uses the configurations specified by *3GPP TS 38.521-1*
 specification.

The period of measurement for NR CHP is at least the continuous duration of one sub-frame (1 ms)
 as defined in *3GPP TS 38.521-1* specification. When you set the
 Sweep Time Auto property to True, the sweep
 time is set to 1 ms for the NR CHP measurement.

Refer to the *CHP* topic in the *RFmx SpecAn User Manual* for a general
 overview of CHP measurement concepts.

Single carrier

Intra-band contiguous carrier aggregation

Intra-band noncontiguous carrier aggregation

Parent topic:

RFmx NR Measurement Concepts

Related information:

- RFmx SpecAn User Manual
- CHP

<!--NI_TOPIC bundle=rfmx-nr path=nr-downlink-acp.html language=enus -->
## TOPIC 00014: NR Downlink Adjacent Channel Power

- bundle_id: `rfmx-nr`
- source_path: `nr-downlink-acp.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr/raw/resource/enus/nr-downlink-acp.html
- document_id: `rfmx-nr`
- page_type: `leaf`
- content_type: `concept`
- source_description: NR downlink adjacent channel power (ACP) measurements for single-carrier and carrier aggregation scenarios, offset channels, and compliance with 3GPP TS 38.141 specifications for FR1 and FR2. The RFmx NR ACP measurement uses configurations specified by the 3GPP TS 38.141-x specifications. Refer to t

### NR Downlink Adjacent Channel Power

NR downlink adjacent channel power (ACP) measurements for single-carrier and carrier
 aggregation scenarios, offset channels, and compliance with 3GPP TS 38.141 specifications
 for FR1 and FR2.

The RFmx NR ACP measurement uses configurations specified by the *3GPP TS
 38.141-x* specifications.

Refer to the *ACP* topic in the *RFmx SpecAn User Manual* for a general
 overview of single and multicarrier ACP measurement concepts.

#### NR Downlink ACP Measurement
 Types

- Single carrier ACP
- Intra-band contiguous carrier aggregation ACP
- Non-contiguous carrier aggregation ACP

#### Offset Channels

NR downlink ACP measurement is performed in the frequency domain across the NR signal
 in the carrier channel and adjacent channels called the offset channels. The
 *3GPP TS 38.141-x* specifications define two types of offset channels
 for NR; 3GPP 5G New Radio (NR) and evolved universal terrestrial radio access
 (E-UTRA). The E-UTRA channels are defined for FR1 only.

Outer
 offset channels are all offsets with absolute offset frequencies
 either lower or higher than the lowest or highest NR carrier in a configuration.
 Outer offset channels are all offset channels in both single carrier and intra-band
 contiguous carrier aggregation configurations.

Inner offset
 channels are offset channels with absolute offset frequencies placed
 between the lowest and the highest NR carrier in a configuration. Inner offset
 channels only exist in non-contiguous carrier aggregation configurations.

#### Single Carrier ACP

- NR Offset Channels for Single Carrier.
- E-UTRA Offset Channels for Single Carrier.

With NR Offset Channels for Single Carrier, the NR ACLR
 (NR<sub>ACLR</sub>) is the ratio of the filtered average power centered on an
 adjacent NR channel to the filtered average power centered on the carrier channel,
 with channel spacing and measurement bandwidths as specified in the following tables
 for FR1 and FR2.

| Number Of NR Offsets = m | Channel Bandwidth, FR1 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 3 MHz | 5 MHz | 7 MHz | 10 MHz | 15 MHz | 20 MHz | 25 MHz | 30 MHz | 35 MHz | 40 MHz | 45 MHz | 50 MHz | 60 MHz | 70 MHz | 80 MHz | 90 MHz | 100 MHz |  |
| NR Center Frequency Offset (MHz) | m * 3 or -m * 3 | m * 5 or -m * 5 | m * 7 or -m * 7 | m * 10 or -m * 10 | m * 15 or -m * 15 | m * 20 or -m * 20 | m * 25 or -m * 25 | m * 30 or -m * 30 | m * 35 or -m * 35 | m * 40 or -m * 40 | m * 45 or -m * 45 | m * 50 or -m * 50 | m * 60 or -m * 60 | m * 70 or -m * 70 | m * 80 or -m * 80 | m * 90 or -m * 90 | m * 100 or -m * 100 |
| NR Channel Measurement Bandwidth (MHz) | 2.7 | 4.5 | 6.3 | 9.360 | 14.220 | 19.080 | 23.940 | 28.800 | 33.840 | 38.880 | 43.560 | 48.600 | 58.320 | 68.040 | 78.120 | 88.200 | 98.280 |

| Number Of NR Offsets = m | Channel Bandwidth, FR2 |  |  |  |
| --- | --- | --- | --- | --- |
| 50 MHz | 100 MHz | 200 MHz | 400 MHz |  |
| NR Center Frequency Offset (MHz) | m * 50 or -m * 50 | m * 100 or -m * 100 | m * 200 or -m * 200 | m * 400 or -m * 400 |
| NR Channel Measurement Bandwidth (MHz) | 47.52 | 95.04 | 190.08 | 380.16 |

Note

#### UTRA Offset Channels for Single
 Carrier (FR1 only)

This measurement provides the adjacent channel leakage
 power ratio (ACLR) values to gauge the extent of contamination from the NR signal in
 adjacent channels. The E-UTRA ACLR is the ratio of the filtered average power
 centered on an adjacent E-UTRA channel to the filtered average power centered on the
 carrier channel with channel spacing and measurement bandwidths are defined as
 follows:

Channel Bandwidth: BW<sub>NR</sub> e{3, 5, 7, 10, 15, 20, 25,
 30, 35, 40, 45, 50, 60, 70, 80, 90, 100} MHz

BW<sub>E-UTRA</sub>
 for UTRA offset channel = 5
 MHz.

E-UTRA<sub>ACLR(n)</sub> Center Frequency Offset (MHz) is
 calculated as follows:

B

W

N

R

/

2

+

2

×

n

+

1

×

B

W

U

T

R

A

/

2

E-UTRA Measurement Bandwidth = 4.5 MHz.

Note

#### Intra-band Contiguous Carrier
 Aggregation ACP

In intra-band contiguous carrier aggregation ACP, the adjacent offset channels are
 placed relative to the center of the closest NR carrier.

Note

#### NR Offset Channels for Contiguous Carrier
 Aggregation

The NR ACLR is the ratio of the filtered average power
 centered on an adjacent NR channel to the filtered average power centered on the
 closest NR carrier. The NR bandwidth of closest NR carrier is used as the
 measurement bandwidth for measuring NR ACLR. The power of closest NR carrier is used
 as power reference for measuring NR ACLR. The NR offset channels are placed relative
 to the center of closest NR carrier of a subblock. The center of successive NR
 offset channels is (m * NR bandwidth of closest
 carrier) away from the center of closest NR carrier. The power of this
 NR adjacent channel is measured with a rectangular filter.

#### E-UTRA Offset Channels for
 Contiguous Carrier Aggregation (FR1 Only)

The E-UTRA ACLR (E-UTRA<sub>ACLR</sub>) is the ratio of the filtered average power
 centered on an adjacent E-UTRA channel to the filtered average power centered on the
 closest NR carrier of the subblock. The power of closest NR carrier of a subblock is
 used as power reference for measuring E-UTRA ACLR. The E-UTRA offset channels are
 placed relative to center of the closest NR carrier of a subblock. The power of this
 E-UTRA adjacent channel is measured with a rectangular filter.

E-UTRA ACLR is
 measured for two E-UTRA adjacent channels by default.

For example, three NR
 component carriers (C0 = 10 MHz, C1 = 5 MHz and C2 = 20 MHz) are configured within a
 subblock as shown in the following figure. In this scenario, the NR offset channels
 (E1:C2 and E2:C2) are positioned relative to the center of component carrier C2. The
 NR offset channels (E1:C0 and E2:C0) are positioned relative to the center of the
 component carrier C0. The E-UTRA offset channels (U1:C2 and U2:C2) are positioned
 relative to the center of the component carrier C2. The E-UTRA offset channels
 (U1:C0 and U2:C0) are positioned relative to the center of the component carrier C0.

Figure 6.

[IMAGE alt='Chart showing E-UTRA and UTRA Offset Channels Configurations for Contiguous Carrier Aggregation' src='GUID-2B190EB9-4F59-48CD-AA1C-95FA3B219756-a5.png']

#### Non-contiguous Carrier Aggregation
 ACP

In intra-band or inter-band non-contiguous carrier aggregation ACP, the NR and the
 E-UTRA offset channels to the left and right of each subblock are measured. Here,
 the offset channels between two subblocks are called the inner offset channels and
 remaining offset channels are called the outer offset channels. The outer offset
 channels are configured similarly to contiguous carrier aggregation ACP.

The
 following image shows a typical carrier channel and offset channel configuration for
 the NR non-contiguous configuration with two subblocks each comprising of two
 component carriers. The inner offset channels (I1:S0:C1 and I2:S0:C1) are positioned
 relative to the center of component carrier S0:C1. Inner offset channels (I1:S1:C0
 and I2:S1:C0) are positioned relative to the center of component carrier S1:C0. The
 outer NR offset channels and the E-UTRA offset channels are positioned relative to
 the center of component carriers S0:C0 and S1:C1

Figure 7.

[IMAGE alt='Chart showing E-UTRA and UTRA Offset Channels Configurations for Non-Contiguous Carrier Aggregation' src='GUID-CE453263-27A5-4A91-9D00-66B72BF65A2A-a5.png']

#### Inner Offset Channels for
 Intra-band Non-contiguous Carrier Aggregation

Cumulative Adjacent Channel Leakage Power Ratio

When a
 subblock gap is small, the carriers located in both the subblocks contribute to the
 leakage in the gap region. To measure this leakage a new concept called
 cumulative adjacent channel leakage power ratio (CACLR) is
 introduced.

As mentioned in the section 6.6.3.2 of *3GPP TS 38.141*
 specification, the CACLR in a subblock gap or inter RF bandwidth gap is defined as
 A / B. Where, A is the
 sum of the filtered mean power centered on the assigned channel frequencies for the
 two carriers adjacent to each side of the subblock gap or inter RF bandwidth gap,
 and B is the filtered mean power centered on a frequency channel
 adjacent to one of the respective subblock edges or RF bandwidth edges.

#### Inner Offset Channel Measurement
 Type: Frequency Range 1 (FR1)

For NR, the inner offset channels are assumed to be NR offset channels of bandwidth 5
 MHz or 20 MHz as specified in the Table 6.6.3.5.2-4 (CACLR) and
 Table 6.6.3.5.2-3 (ACLR) of *3GPP TS 38.141-1*
 specification.

Inner offset channels between the two subblocks returns ACLR
 and CACLR results based on subblock gap as shown in the following table.

|  | BS channel bandwidth of the NR Carrier Transmitted at the Other Edge of the Gap (MHz) |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Channel Bandwidth of Lowest/Highest NR transmitted BW_Channel (MHz) | 3, 5, 7, 10, 15, 20 | 25, 30, 35, 40, 45, 50, 60, 70, 80, 90, 100 |  |  |  |  |  |  |
| 3, 5, 7, 10, 15, 20 | 5 ≤ Wgap < 15 | Wgap ≥ 15 | 10 ≤ Wgap < 20 | Wgap ≥ 20 | 5 ≤ Wgap < 45 | Wgap ≥ 45 | 10 ≤ Wgap < 50 | Wgap ≥ 50 |
| 2.5 MHz Offset, 5 MHz NR, CACLR1 | 2.5 MHz Offset, 5 MHz NR, ACLR1 | 7.5 MHz Offset, 5 MHz NR, CACLR2 | 7.5 MHz Offset, 5 MHz NR, ACLR2 | 2.5 MHz Offset, 5 MHz NR, CACLR1 | 2.5 MHz Offset, 5 MHz NR, ACLR1 | 7.5 MHz Offset, 5 MHz NR, CACLR2 | 7.5 MHz Offset, 5 MHz NR, ACLR2 |  |
| 25, 30, 35, 40, 45, 50, 60, 70, 80, 90, 100 | 20 ≤ Wgap < 30 | Wgap ≥ 30 | 40 ≤ Wgap < 50 | Wgap ≥ 50 | 20 ≤ Wgap < 60 | Wgap ≥ 60 | 40 ≤ Wgap < 80 | Wgap ≥ 80 |
| 10 MHz Offset, 20 MHz NR, CACLR1 | 10 MHz Offset, 20 MHz NR, ACLR1 | 30 MHz Offset, 20 MHz NR, CACLR2 | 30 MHz Offset, 20 MHz NR, ACLR2 | 10 MHz Offset, 20 MHz NR, CACLR1 | 10 MHz Offset, 20 MHz NR, ACLR1 | 30 MHz Offset, 20 MHz NR, CACLR2 | 30 MHz Offset, 20 MHz NR, ACLR2 |  |

The following example describes how to determine the inner offset
 measurements according to the *3GPP TS 38.141-1*
 specification.

Consider the inner offsets for a subblock 0 (SB0) with an edge
 carrier of 10 MHz bandwidth. The gap between SB0 and the neighboring subblock (SB1),
 Wgap is 45 MHz and the edge carrier on SB1 has a 50 MHz bandwidth. The inner offset measurements can
 be read from the table above for line "3, 5, 7, 10, 15, 20" (SB0, 10 MHz edges falls
 into this category) and column "25, 30, 35, 40, 45, 50, 60, 70, 80, 90, 100" (the
 50 MHz edge carrier on the other side of the gap
 falls into this category). The ACP offset measurements contain both, ACLR1 and
 CACLR2 according to the conditions given for Wgap = 45
 MHz.

#### Inner Offset Channel Measurement Type: Frequency
 Range 2 (FR2)

For NR, the inner offset channels are assumed to be NR
 offset channels of bandwidth 50 MHz or 200 MHz as specified in the Table 6.7.3.5.2-4
 (CACLR) and Table 6.7.3.5.2-3 (ACLR) of *3GPP TS 38.141-2*
 specification.

Inner offset channels between the two subblocks returns ACLR
 and CACLR results based on subblock gap as tabulated below.

Inner offset
 channels between the two subblocks returns ACLR and CACLR results based on subblock
 gap as shown in the following table.

|  | BS channel bandwidth of the NR carrier transmitted at the other edge of the gap (MHz) |  |  |  |
| --- | --- | --- | --- | --- |
| Channel Bandwidth of Lowest/Highest NR transmitted BW_Channel (MHz) | 50, 100 | 200, 400 |  |  |
| 50, 100 | 50 ≤ Wgap < 100 | Wgap ≥ 100 | 50 ≤ Wgap < 250 | Wgap ≥ 250 |
| 25 MHz Offset, 50 MHz NR, CACLR | 25 MHz Offset, 50 MHz NR, ACLR | 25 MHz Offset, 50 MHz NR, CACLR | 25 MHz Offset, 50 MHz NR, ACLR |  |
| 200, 400 | 200 ≤ Wgap < 250 | Wgap ≥ 250 | 200 ≤ Wgap < 400 | Wgap ≥ 400 |
| 100 MHz Offset, 200 MHz NR, CACLR | 100 MHz Offset, 200 MHz NR, ACLR | 100 MHz Offset, 200 MHz NR, CACLR | 100 MHz Offset, 200 MHz NR, ACLR |  |

#### Offset Result Ordering

Offset
 Result Ordering The offset measurement results are reported per
 subblock. Depending on the frequency of the subblock relative to other subblocks,
 the order of result reporting is affected.

|  | Left Subblock | Inner Subblock (optional) | Right Subblock |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | Lower | Upper | Lower | Upper | Lower | Upper |
| EUTRA Offsets | EUTRA0 | NaN | - | - | NaN | EUTRA0 |
| EUTRA1 | NaN | - | - | NaN | EUTRA1 |  |
| NR Offsets | OuterNR0 | NaN | InnerNR0 | NaN | InnerNR0 | NaN |
| NaN | InnerNR0 | NaN | InnerNR0 | NaN | OuterNR0 |  |
| OuterNR1 | NaN | InnerNR1 | NaN | InnerNR0 | NaN |  |
| NaN | InnerNR1 | NaN | InnerNR1 | NaN | OuterNR1 |  |

Note

Parent topic:

Adjacent Channel Power

Related information:

- ACP

<!--NI_TOPIC bundle=rfmx-nr path=nr-downlink-sem.html language=enus -->
## TOPIC 00015: NR Downlink Spectral Emission Mask

- bundle_id: `rfmx-nr`
- source_path: `nr-downlink-sem.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr/raw/resource/enus/nr-downlink-sem.html
- document_id: `rfmx-nr`
- page_type: `leaf`
- content_type: `concept`
- source_description: Measures the downlink spectrum emission mask for 5G NR signals, ensuring compliance with emission limits in RFmx NR testing workflows. The RFmx NR spectral emission mask (SEM) measurement uses the configurations and masks specified by the 3GPP TS 38.104 specification. This topic explains the configu

### NR Downlink Spectral Emission Mask

Measures the downlink spectrum emission mask for 5G NR signals, ensuring compliance
 with emission limits in RFmx NR testing workflows.

The RFmx NR spectral emission mask (SEM) measurement uses the configurations and masks
 specified by the *3GPP TS 38.104* specification. This topic explains
 the configurations and masks used by the RFmx NR Downlink SEM measurement.

Refer to the SEM Overview topic for a general overview of single and multicarrier SEM
 measurement concepts.

#### Offset Segments

The offset segments are the channels adjacent to the carrier channels and are specified
 by their start and stop frequencies (Δf) relative to the nearest edge
 of the closest NR carrier. This applies to a single carrier, intraband contiguous and
 intraband non-contiguous operations. The offset segment frequencies, bandwidths, and
 limits are defined by the 3GPP specification.

The power of any offset segment is measured with the measurement filter defined in
 section 6.6.4 for FR1 and section 9.7.4 for FR2 of the *3GPP 38.104*
 specification. Unlike uplink, the masks of downlink depend on the operating band. The masks are defined from a few MHz below the lowest
 frequency of each supported downlink operating band, up to 10 MHz above the highest
 frequency of each supported downlink operating band. The limit requirements apply inside
 any subblock gap and the inside inter-RF bandwidth gap, if any.

The RBW filter for all offset segments is Gaussian, and the resolution bandwidths are set
 according to the measurement bandwidth defined in 3GPP specification.

According to the 3GPP specification, the resolution bandwidth of the measuring equipment
 should be equal to the measurement bandwidth. However, to improve the measurement
 accuracy, sensitivity, and efficiency, the resolution bandwidth the measuring equipment
 may be smaller than the measurement bandwidth. When the resolution bandwidth is smaller
 than the measurement bandwidth, the result is integrated over the measurement bandwidth
 to obtain the equivalent noise bandwidth of the measurement bandwidth.

The measurement improves the resolution of the spectrum by using bandwidth integrals,
 which specifies the resolution of the spectrum to compare with spectral mask limits as
 an integer multiple of the RBW filter bandwidth. The measurement acquires the spectrum
 with a narrow resolution and processes the spectrum digitally to get a wider resolution that is
 equal to the product of the bandwidth integral and the RBW filter bandwidth. When
 resolutions of the overlapping masks are different, the lowest resolution is used to
 compute the composite mask.

#### Masks

The power of any base station (BS) emission must not exceed the levels specified for a
 mask type for different offset segments. As per the 3GPP specification, the measurement
 passes if all the offset segments are less than this limit.

The masks are specified based on the gNodeB categories, NR BS operating band, and edge
 carrier bandwidths.

There are few additional requirements mentioned for certain regions and bands defined by
 3GPP Specification.

You can choose the SEM Downlink Mask Type property and gNodeB Category property to
 specify test requirements defined by 3GPP specification.

#### Medium Base Station

The table for masks is selected based on configuration you specify for the SEM CC Max Output Power property as
 specified by 3GPP specification. The maximum output power is defined as the mean power
 level per carrier measured at the antenna connector during the transmitter ON period.
 Masks for medium base station are dependent on measured carrier power(s).

Occasionally, the emission masks may overlap for BS capable of transmitting multiple
 subblocks. In such scenarios, the limit mask requirement is defined as a composite
 emission masks, which is a combination of carriers' general emissions masks, and is as
 stated below:

- For Masks within 10 MHz from the edges for some frequency out of band, the cumulative
 sum of the spectral emission masks specified at the edges on each side of the
 overlap will be applicable. Here, the edge refers to the carrier edge, the subblock
 edge, or the RF bandwidth edge.
- For Masks beyond 10 MHz from the edges for some frequency out of band, the spectrum
 emission mask with the higher power spectral density applies for these
 frequencies.

The mask does not apply for frequency, where the sub-block spectrum emission mask
 overlaps with the sub-block bandwidth of another sub-block. The masks are defined in
 multiple tables in the section 6.6.4 of 3GPP specification.

For example, the following image shows the carrier channel and the offset channel
 configurations for DL SEM with two subblocks (A, B).

- Subblock A is comprised of 2 contiguous component carriers (CC-A0 and CC-A1).
 Subblock B is comprised of 3 contiguous component carriers (CC-B0, CC-B1, and
 CC-B2).
- Offset segments are denoted as OA and OB.
- The Δf max is the frequency separation between the carrier edge or
 subblock edge (in case of multicarrier) and the nominal -3 dB point of last
 measurement bandwidth filter. Configure the Δf<sub>max</sub> using the SEM Delta
 F_Max property. When you specify the SEM downlink mask type property as
 Custom, the SEM measurement ignores this
 parameter.

[IMAGE alt='image' src='GUID-429640D2-0EBD-4717-B144-4CD151A63EA5-a5.png']

The cumulative regions are present in the inter subblock gap with a span of 10 MHz. If
 the multiple masks belonging to the adjacent subblocks overlap in this region, the sum
 of PSD of the limits is used for those overlapping frequencies.

If the multiple masks belonging to the adjacent subblocks overlap within inter
 subblock gap but outside cumulative regions, the maximum of the PSD of limits is
 used for those overlapping frequencies.

Note

If you set the SEM Downlink Mask Type property to Custom, the
 following parameters are ignored:

- Delta F_Max (Hz)
- Aggregated Maximum Power (dBm)
- Max Output Power (dBm)
- gNodeB Category

Parent topic:

RFmx NR Measurement Concepts

Related information:

- SEM

<!--NI_TOPIC bundle=rfmx-nr path=nr-modulation-accuracy.html language=enus -->
## TOPIC 00016: NR Modulation Accuracy

- bundle_id: `rfmx-nr`
- source_path: `nr-modulation-accuracy.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr/raw/resource/enus/nr-modulation-accuracy.html
- document_id: `rfmx-nr`
- page_type: `leaf`
- content_type: `concept`
- source_description: NR modulation accuracy measures modulation accuracy for 5G NR signals, providing EVM and error analysis to validate performance in RFmx NR applications. Basic Signal Configuration Requirements Minimum NR signal configurations for successful demodulation are as follows: Link Direction Frequency Range

### NR Modulation Accuracy

NR modulation accuracy measures modulation accuracy for 5G NR signals, providing EVM
 and error analysis to validate performance in RFmx NR applications.

#### Basic Signal Configuration
 Requirements

Minimum NR signal configurations for successful demodulation are as follows:

- Link Direction
- Frequency Range
- CC Bandwidth
- BWP Subcarrier Spacing
- Uplink
  1. Cell ID
  2. User0/PUSCH0/Slot Allocation
  3. User0/PUSCH0/Symbol Allocation
  4. User0/PUSCH0/Mapping Type
  5. User0/PUSCH0/DMRS Type A Position
- Downlink, Channel Configuration Mode: Test Model
  1. Test Model
  2. Test Model Duplex Scheme
- Downlink, Channel Configuration Mode: User Defined
  1. Cell ID
  2. User0/PDSCH0/Slot Allocation
  3. User0/PDSCH0/Symbol Allocation
  4. User0/PDSCH0/Mapping Type
  5. User0/PDSCH0/DMRS Type A Position
- Advanced
  1. Phase Compensation

Minimum NR measurement configurations are as follows:

- Synchronization Mode
- Measurement Offset
- Measurement Length

#### Auto Resource Block Detection Enabled

ModAcc measurement supports auto detection of carrier resource configurations for the
 shared channels (PUSCH in uplink and PDSCH in downlink). You can configure
 auto-detection by using the Auto RB Detection Enabled property, which defaults to True,
 where the PDSCH/PUSCH modulation type, number of PUSCH/PDSCH clusters, PUSCH/PDSCH
 resource block offsets, and PUSCH/PDSCH resource block sizes are automatically detected
 by the measurement.

ModAcc measurement supports signal containing same value of modulation type, resource block allocation,
 and transform precoding enabled (in case of uplink) across slots.

For downlink, when RB Autodetection Enabled property is set to True, ModAcc measurement
 will return an error, if any other physical channel other than PDSCH is present.

#### Synchronization Mode and Trigger Type

The frame and slot synchronization modes enable you to synchronize to the frame or slot
 boundaries. For more information on the frame structure of an NR frame, refer to
 *5G New Radio: Introduction to Physical Layer* white paper[1].
 Modacc measurements are made over the ModAcc Meas Length starting at the ModAcc Meas
 Offset from the specified boundary. The units for ModAcc Meas Length and ModAcc Meas
 Offset properties are specified by the ModAcc Meas Length Unit property. The units can be set to slot,
 subframe, or time. The frame synchronization mode allows you to measure specific slots
 in a frame, while the slot synchronization mode starts the measurement at the first
 complete slot in the acquisition.

When a digital trigger is used, the trigger must occur at the start of a slot for slot
 synchronization mode and start of frame for frame synchronization mode.

In the presence of multiple carriers, all carriers are assumed to be aligned in their
 frame timing, and their frame synchronization will be established on only one carrier
 and applied to all carriers equally.

| Trigger Type | Synchronization Mode | Notes |
| --- | --- | --- |
| Digital | Slot | Marker must be at start of any slot. |
| Digital | Frame | Marker must be at start of slot0 of the frame. |
| IQ Power Edge | Slot | Measures from the first complete slot in the acquisition. |
| IQ Power Edge | Frame | Measures from slot0 of the frame. Not recommended when using DFT-s-OFDM waveforms. |
| Immediate | Slot | Measures from the first complete slot in the acquisition. Not recommended when using low number of RBs. |
| Immediate | Frame | Measures from slot0 of the frame. Not recommended when using low number of RBs or when using DFT-s-OFDM waveforms. |

#### Fast Measurements

Digital triggers and frame synchronization enable fast measurements with full-frame
 signals. For even faster measurements, short frames comprising of partial frame with
 integral number of slots and a digital trigger at the start of the short frame
 should be used. NI recommends analyzing short frames with a digital trigger.

The following images illustrate the measured region in various synchronization modes,
 measurement offsets, and trigger configurations. The measurement length is 2 and
 measurement length unit is slot in all the examples.

[IMAGE alt='image' src='GUID-422DD714-8946-4A85-98C1-67ADBE84447F-a5.png']

[IMAGE alt='image' src='GUID-1BEF9B76-8625-4968-BC99-30D1E860A063-a5.png']

[IMAGE alt='image' src='GUID-C6DF60FC-AA01-4349-99CE-691EF2497360-a5.png']

#### EVM FFT Window

An OFDM symbol consists of FFT length worth data samples (N) and cyclic prefix samples
 (CP). An FFT is taken only on N samples, and hence, the position in time for FFT can
 start at any instant within the cyclic prefix. The EVM requirements are met within a
 window, which has a length less than the CP length.

There are two FFT window types that are defined:

- 3GPP
- Custom

If you set the ModAcc FFT Window Type property to 3GPP, the EVM calculation uses two
 windows. You can specify the window starting positions by setting the FFT Window Length
 property as a percentage of CP. The windows are determined as (ΔC –
 W/2) and (ΔC + W/2), where ΔC is the center of CP and
 the center of FFT Window and W is the window length. For each OFDM symbol, the EVM is
 calculated for these windows each having a length of the FFT size (N). This leads to
 computation of two different EVMs: EVM<sub>low</sub> and EVM<sub>high</sub>. The
 averaging is done separately, and the maximum of EVM<sub>low</sub> and
 EVM<sub>high</sub> is returned as the final EVM.

All results related to EVM, phase error, magnitude error, and other corresponding traces
 are affected by this selection. They are reported with regards to the window resulting
 in maximum averaged EVM.

If you set FFT Window Length property to -1, RFmx automatically selects the FFT window
 length based on channel bandwidth and subcarrier spacing as mentioned in the
 *3GPP 38.104* specification Annex B.5.2 and C.5.2 for downlink and
 *3GPP 38.101-1* specification Annex F.5 for uplink frequency range
 1 and *3GPP 38.101-2* specification Annex F.5 for uplink frequency
 range 2.

If you set the ModAcc FFT Window Type property to Custom, only one FFT window offset is
 used for EVM calculation. The start of the FFT window is relative to the start of OFDM
 symbol excluding the CP. You can specify the window offset by setting the FFT Window
 Offset property as a percentage of CP.

The following image illustrates the FFT window type, the FFT window length, and the FFT
 window offset compared with the window positions and offset.

[IMAGE alt='image' src='GUID-BB2BF8F6-D623-4037-9F65-03277FCFDF4C-a5.png']

#### Noise Compensation for EVM

You may use noise compensation for EVM to improve residual EVM of vector signal
 analyzers. Due to additional calibration requirements and certain measurement
 restrictions, NI recommends that you use noise compensation for EVM only if the residual
 EVM performance without noise compensation does not meet your EVM performance
 requirements.

Noise compensation for EVM involves calibration of noise floor of the instrument first,
 and then use of calibrated noise floor data to compensate the measured EVM.

#### Calibrate Noise Floor

This calibration measures the noise floor of the instrument. The calibrated noise
 floor data is used to compensate EVM results and traces during the ModAcc
 measurement. Calibrate the noise floor only if you want to apply noise compensation
 to EVM.

Noise floor is calibrated for the specified instrument and measurement settings like
 Reference Level and Center Frequency and the settings that define nominal bandwidth
 of the signal. You must use the same settings while performing the ModAcc
 measurement. Follow the below instructions to calibrate noise floor of the signal
 analyzer:

1. Turn off the signal output of the DUT.
2. Make sure that the rest of the physical hardware connections on the signal
 analyzer remain the same as what will be used during a successful ModAcc
 measurement on the DUT output signal.
3. Configure the ModAcc measurement and the instrument and signal configurations
 required for a successful ModAcc measurement on the DUT output signal.
4. Configure ModAcc Meas Mode property to Calibrate
 Noise Floor .
5. Initiate the ModAcc measurement. This will calibrate the noise floor and store
 it in an internal database.

When performing the ModAcc measurement to measure EVM of the DUT RF
 OUT signal, the DUT must be on. To avoid frequent power fluctuations of
 the DUT RF OUT, NI recommends that you perform noise floor calibration for all
 configurations that you want to test by repeating steps 3-5 for all configuration
 before measuring EVM.

Use RFmx NR
 ModAcc Validate Calibration Data VI to check if calibration data
 for the current configuration is already present. You may skip noise floor
 calibration for a configuration that has valid calibration data.

Use the RFmx NR
 ModAcc Clear Noise Calibration Database VI to clear any existing
 noise floor calibration data.

Note:

- After self-calibration
- When the difference between the current device temperature and the device
 temperature at which calibration was performed is beyond the [–5°C, +5°C]
 range
- If you change any physical hardware connection that impacts noise floor
 calibration

#### Noise Compensation for EVM

The ModAcc measurement makes use of the calibrated noise floor to compensate EVM
 results and traces. The following instructions will guide you through the noise
 compensation process:

1. To successfully measure the DUT output signal, configure the ModAcc measurement,
 as well as instrument and signal configurations required. Make sure that these
 configurations are same as those used during noise calibration.
2. Set ModAcc Noise Comp Enabled property to True and ModAcc
 Meas Mode property to Measure .
3. Make sure that the rest of the physical hardware connections on the signal
 analyzer are the same as during noise floor calibration.
4. Turn on the signal output of the DUT.
5. Initiate the ModAcc measurement. This will return EVM with noise compensation
 applied. The measurement reads the previously calibrated noise floor data from
 the internal database created during noise floor calibration. Read the value of
 the Noise Comp Applied property to check whether the noise compensation was
 successful.

#### References

*<sup>[1]</sup>5G New Radio: Introduction to the Physical Layer available for download
 from 5G New Radio: Introduction to the Physical Layer*

Parent topic:

RFmx NR Measurement Concepts

<!--NI_TOPIC bundle=rfmx-nr path=nr-occupied-bandwidth.html language=enus -->
## TOPIC 00017: NR Occupied Bandwidth

- bundle_id: `rfmx-nr`
- source_path: `nr-occupied-bandwidth.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr/raw/resource/enus/nr-occupied-bandwidth.html
- document_id: `rfmx-nr`
- page_type: `leaf`
- content_type: `concept`
- source_description: Occupied bandwidth (OBW) measures the bandwidth that occupies a certain power specified as a percentage of the total power in the acquired spectrum. The RFmx NR Occupied Bandwidth (OBW) measurement uses the configurations specified by the 3GPP specification. For a general overview of OBW measurement

### NR Occupied Bandwidth

Occupied bandwidth (OBW) measures the bandwidth that occupies a certain power specified
 as a percentage of the total power in the acquired spectrum.

The RFmx NR Occupied Bandwidth (OBW) measurement uses the configurations specified by the 3GPP
 specification.

For a general overview of OBW measurement concepts, refer to the *OBW* topic in the
 *RFmx SpecAn User Manual*.

#### Single-Carrier OBW

According to the 3GPP NR specification, OBW is a
 measure of the bandwidth containing 99% of the
 total integrated mean power of the transmitted
 spectrum on the assigned channel. The occupied
 channel bandwidth for all transmission bandwidth
 configurations are listed in the following tables.

- Frequency Range 1 (FR1) references table
 6.5.1.3-1 of 3GPP 38.521-1 
 specification.
- FR2 reference table 6.5.1.2-1 of 3GPP
 38.521-2 specification).

| Occupied Channel Bandwidth | 3 MHz | 5 MHz | 7 MHz | 10 MHz | 15 MHz | 20 MHz | 25 MHz | 30 MHz | 35 MHz | 40 MHz | 45 MHz | 50 MHz | 60 MHz | 70 MHz | 80 MHz | 90 MHz | 100 MHz |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Channel bandwidth (MHz) | 3 | 5 | 7 | 10 | 15 | 20 | 25 | 30 | 35 | 40 | 45 | 50 | 60 | 70 | 80 | 90 | 100 |

| Occupied Channel Bandwidth | 50 MHz | 100 MHz | 200 MHz | 400 MHz |
| --- | --- | --- | --- | --- |
| Channel bandwidth (MHz) | 50 | 100 | 200 | 400 |

For uplink, OBW is measured over a
 subframe duration that is 1 ms in time with
 Auto RBW property set to
 True, by default. For
 downlink, OBW is measured using RBW of 30 kHz with
 Auto Sweep Time property set to
 True.

For more
 details about Auto Sweep Time and Auto RBW, refer
 to the *OBW* topic in the *RFmx
 SpecAn User Manual*.

#### Intra-band Contiguous Carrier Aggregated OBW

For intra-band contiguous carrier aggregation scenario, the OBW is a measure of the
 bandwidth containing 99% of the total integrated power of the transmitted spectrum. The
 OBW shall be less than the aggregated channel bandwidth.

#### Intra-band Non-contiguous Carrier Aggregated
 OBW

For intra-band non-contiguous carrier
 aggregation, each subblock (set of contiguous
 aggregated carriers OBW) is a measure of the
 bandwidth containing 99% of the total integrated
 power of the transmitted spectrum for each
 subblock. The OBW for each subblock shall be less
 than the aggregated channel bandwidth for that
 subblock.

Figure 9.

[IMAGE alt='Image showing the Intra-band Non-contiguous Carrier Aggregated Occupied Bandwidth' src='GUID-30F4F802-6193-4E40-9F54-EDC6A6CE70F6-a5.png']

The Carrier Aggregation Type
 property and the Span Auto
 property values determine the OBW measurement
 using a span based on the following table.

| Carrier Aggregation Type | Span Auto = True | Span Auto = False |
| --- | --- | --- |
| Single Carrier | 2 * Channel Bandwidth | Min: Channel Bandwidth Max: 2 * Channel Bandwidth |
| Contiguous Carrier | 2 * Aggregated Channel Bandwidth | Min: Aggregated Channel Bandwidth Max: 2 * Aggregated Channel Bandwidth |
| Non-Contiguous Carrier | Subblock Bandwidth + Min (Subblock Bandwidth, Left Gap, Right Gap) | Min: Subblock Bandwidth Max: Subblock Bandwidth + Min (Subblock Bandwidth, Left Gap, Right Gap) |

- Span Auto = True column
 contains span value internally used by the
 measurement.
- Span Auto = False 
 column contains the range for span that can be
 configured.

Parent topic:

RFmx NR Measurement Concepts

Related information:

- RFmx SpecAn User Manual
- OBW

<!--NI_TOPIC bundle=rfmx-nr path=nr-power-vs-time.html language=enus -->
## TOPIC 00018: NR Power Vs Time

- bundle_id: `rfmx-nr`
- source_path: `nr-power-vs-time.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr/raw/resource/enus/nr-power-vs-time.html
- document_id: `rfmx-nr`
- page_type: `leaf`
- content_type: `concept`
- source_description: Measures 5G NR signal power variations over time, ensuring compliance with transmission masks and validating performance in RFmx NR testing workflows. NR Power Vs Time Overview The NR Power Vs Time (PVT) measurement measures the time domain power dynamics of an NR signal. This measurement is also kn

### NR Power Vs Time

Measures 5G NR signal power variations over time, ensuring compliance
 with transmission masks and validating performance in RFmx NR testing
 workflows.

#### NR Power Vs Time Overview

The NR Power Vs Time (PVT) measurement measures the time domain power dynamics of an NR
 signal. This measurement is also known as Transmit ON-OFF Time Mask measurement. The
 3GPP specification defines limits for the signal power for signal OFF periods. The
 higher OFF power increases the rise over thermal noise (ROT) and causes interference to
 other users.

#### Measurement Overview Uplink PVT

The average OFF power for frequency range 1 and frequency range 2 shall not exceed the
 limits specified in *3GPP TS 38.521-1* specification and *3GPP TS
 38.521-2* specification, respectively.

| Carrier Frequency | Channel Bandwidth | OFF Power Limit |
| --- | --- | --- |
| f ≤ 3 GHz | BW ≤ 40 MHz | -48.5 dBm |
| BW ≤ 100 MHz | -48.3 dBm |  |
| 3 < f ≤ 6 GHz | - | -48.2 dBm |

| Carrier Frequency | Channel Bandwidth | OFF Power Limit |
| --- | --- | --- |
| - | - | -30 dBm |

Figure 10.

[IMAGE alt='PVT measurement regions' src='GUID-0F4A780A-A1CB-4A77-A643-F7292E3E71EE-a5.png']

OFF Power Before

ON Power

OFF Power After

- IQ Power Edge Trigger
- Digital Edge Trigger

#### Measurement Overview Downlink PVT

According to 3GPP (38.104, 38.141-1, 38.141-2)
 for Downlink PVT, the OFF power spectral density
 is measured over 70/N µs (N = SCS/15, where SCS is
 Sub Carrier Spacing in kHz) filtered with a square
 filter of bandwidth equal to the RF bandwidth. The
 measured OFF power spectral density in the time
 window from 35/N µs after end of one transmitter
 ON period (excluding transient time) to 35/N µs
 before start of next transmitter ON period
 (excluding transient time) shall not exceed the
 limits specified in 38.141-1 for conducted testing
 and 38.141-2 for radiated testing.

Depending
 on the base station type being either BS type 1-C,
 BS type 1-O or BS type 2-O the limits for FR1
 conducted, FR1 radiated or FR2 radiated are
 selected as shown in the tables below.

Note

The base
 station type can be configured by gNodeB Type
 property. The additional rated power parameters
 P<sub>rated,c,EIRP</sub> and
 P<sub>rated,c,TRP</sub> required to calculate the
 limits for Base Station Type 2-O can be configured
 by the properties Rated TRP (dBm) and Rated EIRP
 (dBm).

| Carrier Frequency | OFF Power Limit |
| --- | --- |
| f ≤ 3 GHz | -81 dBm/MHz |
| 3 < f ≤ 6 GHz | -80 dBm/MHz |

| Carrier Frequency | OFF Power Limit |
| --- | --- |
| f ≤ 3 GHz | -99.2 dBm/MHz |
| 3 < f ≤ 6 GHz | -98.8 dBm/MHz |

| Carrier Frequency | OFF Power Limit |
| --- | --- |
| 24.15 < f ≤ 29.5 GHz | -30.2 + Prated,c,EIRP - Prated,c,TRP dBm/MHz |
| 37 < f ≤ 43.5 GHz | -29.4 + Prated,c,EIRP - Prated,c,TRP dBm/MHz |

The Downlink PVT measurement is performed
 as follows:

- The signal is acquired depending on the
 configured trigger and measurement interval. NR
 Downlink PVT measurement supports IQ Power Edge
 Trigger and Digital Edge Trigger marking the start
 of a frame.
- The length of the acquired signal is
 controlled by the properties Measurement
 Interval Auto and Measurement
 Interval (s) .
  - If you set Measurement Interval Auto to
 True , the acquisition
 length is automatically derived from the signal
 configuration such that the measurement spans the
 first sequence of ON-OFF-ON regions.
  - If you set Measurement Interval Auto to
 False , the acquisition
 length is configured such that the measurement
 spans the configured Measurement Interval (s). In
 this case, all ON and OFF segments identified in
 the acquired signal are used for measurement.

With the acquired data, the instantaneous
 signal power and the 70/N µs windowed signal power
 is calculated. In addition, the location of the ON
 regions and the location of the regions where the
 OFF power limit applies are derived.

The
 Downlink PVT measurement calculates the following
 measurement results:

Peak
 Windowed OFF Power (dBm/MHz) — This
 result returns the peak power value of the 70/N µs
 windowed power among all OFF regions in the
 measurement interval in dBm/MHz.

Peak Windowed OFF Power Margin (dB)

Peak Windowed OFF Power Time (s)

ON Power

[IMAGE alt='image' src='GUID-E5A7C3F6-ADF5-4099-8BBF-FF8A2F08BD65-a5.png']

#### NR PVT Dynamic Range Mode

PVT measurement provides a high dynamic range measurement mode to handle the 3GPP ON-OFF
 power measurement requirements.

For example, in frequency range 1, an NR UE transmits
 the maximum power of +26 dBm, the OFF-power limit being -50
 dBm, and the dynamic range required is around 75 dB. For frequency range 2, an NR UE
 might transmit at 55 dBm EIRP, which, with the OFF-power limit being -30 dBm, would require
 the dynamic range to be around 85 dB. The theoretical OFF
 power limit can go even lower based on the thermal noise floor. For example, for 20 MHz
 bandwidth, the OFF-power value is -96 dBm; for 10 MHz
 bandwidth, the OFF-power value is -99 dBm; and so on. To
 measure this OFF power accurately, the dynamic range needed is very high (~120 dB) and none
 of the available instruments in the market provide this dynamic range. NR PVT dynamic range
 mode provides a dual acquisition solution to achieve the required dynamic range.

The
 first acquisition captures the I/Q with a user-defined reference level, which will measure
 the ON power accurately. However, the OFF power will not be represented adequately due to
 the limited dynamic range of the device, which leads to an inaccurate measurement of the OFF
 power. To solve this, a second acquisition is done at a lower reference level, which ensures
 the OFF-power regions are represented adequately. These two acquisitions are combined by the
 measurement to get a composite power trace having an OFF region from the second acquisition
 and an ON region from the first acquisition as shown in the picture below. The power
 measurement is done on this composite trace.

[IMAGE alt='image' src='GUID-89B0C37E-5CA1-4427-B032-2A76BED658D5-a5.png']

#### NR
 PVT OFF Power Exclusion Periods

The NR PVT measurement allows to extend the
 transient duration separately for the ON-OFF and
 OFF-ON transition regions by assigning a non-zero
 value to the properties OFF Power Exclusion Before
 (s) and OFF Power Exclusion After (s).

Note

[IMAGE alt='image' src='GUID-C8868BE8-32EA-463C-B57B-4628809CD442-a5.png']

The default value for the OFF Power Exclusion
 Before property and OFF Power Exclusion After
 property is 0, which ensures it adheres to the
 3GPP definition. The maximum time value is limited
 to 100 µs on both
 the sides.

Parent topic:

RFmx NR Measurement Concepts

<!--NI_TOPIC bundle=rfmx-nr path=nr-transmit-power.html language=enus -->
## TOPIC 00019: NR Transmit Power

- bundle_id: `rfmx-nr`
- source_path: `nr-transmit-power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr/raw/resource/enus/nr-transmit-power.html
- document_id: `rfmx-nr`
- page_type: `leaf`
- content_type: `concept`
- source_description: Measures total transmit power for 5G NR signals, ensuring compliance with power limits and validating performance in RFmx NR testing workflows. NR Transmit Power Overview RFmx NR TxP is a time domain measurement which is not defined in the NR standard. The objective of this measurement is to measure

### NR Transmit Power

Measures total transmit power for 5G NR signals, ensuring compliance with power
 limits and validating performance in RFmx NR testing workflows.

#### NR Transmit Power Overview

RFmx NR TxP is a time domain measurement which is not
 defined in the NR standard. The objective of this measurement is to measure the
 overall transmitted power in time domain, which makes the measurement faster than
 the frequency domain power measurements. TxP is a zero-span measurement, that is,
 RBW (Hz) determines the measurement bandwidth over which the power is measured.

For a general overview, refer to the Transmit Power (*TXP*) topic
 in the *RFmx SpecAn User Manual*. The properties listed below are
 internally configured by RFmx NR TxP and are not
 exposed in the RFmx NR API:

- RBW Filter Type: The property is internally set to None .
 That is, no filtering is performed.
- RBW (Hz): The property is internally set based on the configured NR
 carrier/subblock. For more details, refer to RBW Computation section.
- Thresholding Enabled: The property is internally set to
 False . That is, no thresholding is performed.

#### RBW Computation

This topic covers the RBW computation by the TxP measurement across different signal
 configurations.

- Single Carrier: The power is measured over the
 integration bandwidth of the carrier as per Table 6.5.2.4.1-1 in 3GPP TS
 38.101-1 for FR1 and Table 6.5.2.3-1 in 3GPP TS 38.101-2 
 for FR2. [IMAGE alt='image' src='GUID-27DBB7B4-9275-4020-B3FD-12224B5ADEF8-a5.png']
- Intra-band Contiguous Carrier Aggregation: The power is
 measured over the integration bandwidth of the aggregated carriers, which
 include the guard bands between the carriers. [IMAGE alt='image' src='GUID-6698101A-D2C8-49F8-B1E8-A1520DE9D56B-a5.png']
- Intra-band Non-contiguous Carrier Aggregation: The power
 is measured over the integration bandwidth of all the configured subblocks,
 which includes the subblock gap. [IMAGE alt='image' src='GUID-DC89DC4E-532D-411C-8495-8C73BD9B8E8E-a5.png']

#### Measurement Offset/Measurement
 Length

Using measurement offset and measurement length, TxP determines the measurement
 region in time domain. Measurement Offset determines the time offset to the
 measurement region from the acquisition start, while measurement length determines
 the measurement region over which the power is measured. The unit of these controls
 is in seconds.

The following figures illustrate the measurement region using
 NR carrier with 30k subcarrier (ie., slot duration is 0.5msec) for various signal
 configurations (continuous/bursty) and trigger types as defined below:

- Continuous Signal; Measurement Offset = 2.5 msec 
 (5 slots); Measurement Length = 1 msec (2 slots);
 Trigger Type = None [IMAGE alt='image' src='GUID-ECEF0A12-100F-4071-9CFE-6EDEE394F7D7-a5.png']
- Continuous Signal; Measurement Offset = 2.5 msec 
 (5 slots); Measurement Length = 1 msec (2 slots);
 Trigger Type = Digital [IMAGE alt='image' src='GUID-AB8864D8-AE6B-4548-AA30-9927212A86D4-a5.png']
- Bursty Signal (Slot Allocation = 4 to 9); Measurement Offset = 2.5 msec (5 slots) and Measurement Length = 1 msec (2 slots); Trigger Type = IQ Power Edge
 [IMAGE alt='image' src='GUID-A927F93E-3016-4C16-8A60-64C9D5456154-a5.png']
- Bursty Signal (Slot Allocation = 4 to 9); Measurement Offset = 1.5 msec (3 slots) and Measurement Length = 1 msec (2 slots); Trigger Type = Digital
 [IMAGE alt='image' src='GUID-666E4EEE-DE00-4435-9CBE-88F9E7024CAC-a5.png']

Parent topic:

RFmx NR Measurement Concepts

Related information:

- TXP

<!--NI_TOPIC bundle=rfmx-nr path=nr-uplink-acp.html language=enus -->
## TOPIC 00020: NR Uplink Adjacent Channel Power

- bundle_id: `rfmx-nr`
- source_path: `nr-uplink-acp.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr/raw/resource/enus/nr-uplink-acp.html
- document_id: `rfmx-nr`
- page_type: `leaf`
- content_type: `concept`
- source_description: NR uplink adjacent channel power (ACP) measurements for single-carrier and carrier aggregation scenarios, offset channels, and compliance with 3GPP TS 38.521 specifications for FR1 and FR2. RFmx NR ACP measurement uses the configurations specified by the 3GPP TS 38.521-1 specification. The period of

### NR Uplink Adjacent Channel Power

NR uplink adjacent channel power (ACP) measurements for single-carrier and carrier
 aggregation scenarios, offset channels, and compliance with 3GPP TS 38.521 specifications
 for FR1 and FR2.

RFmx NR ACP measurement uses the configurations specified by the *3GPP TS
 38.521-1* specification.

The period of measurement for NR Uplink ACP is at least the continuous duration of
 one sub-frame (1 ms) as defined in the *3GPP TS 38.521-1* specification.
 When the Sweep Time Auto property is
 True, the sweep time is set to 1 ms for the NR Uplink ACP
 measurement.

Refer to the *ACP* topic in the *RFmx SpecAn User Manual* for a
 general overview of single and multicarrier ACP measurement concepts.

#### Offset Channels

With Frequency Range 1 (FR1), the offset channels are adjacent to
 the carrier channels. The *3GPP TS 38.521-1* specification defines two
 types of offset channels for NR; 3GPP 5G new radio (NR), and universal terrestrial
 radio access (UTRA). For FR1, the number of UTRA offset channels defaults to 2, and
 the number for NR offset channels defaults to 1, as specified in the 3GPP
 TS 38.521-1 specification. For ACP carrier aggregation, the power
 reference defaults to sum of the subblock powers to conform to the *3GPP TS
 38.521-1* specification.

With Frequency Range 2
 (FR2), the offset channels are adjacent to the carrier channels. The
 *3GPP TS 38.521-2* specification defines only 3GPP 5G NR offset
 channels for NR FR2. For FR2, the number for NR offset channels defaults to 1, as
 specified in the *3GPP TS 38.521-2* specification. For ACP carrier
 aggregation, the power reference defaults to sum of the subblock powers to conform
 to the *3GPP TS 38.521-2* specification.

Note

ACP Num UTRA
 Offsets

ACP Num NR Offsets

#### NR Uplink
 ACP Measurement Types

- Single carrier ACP
- Intra-band contiguous carrier aggregation ACP
- Non-contiguous carrier aggregation ACP

Non-contiguous carrier aggregation ACP measurements apply to both
 intra-band and inter-band scenarios. These types of measurements are currently not
 defined in the *3GPP TS 38.521-x (Release 15)* specifications and hence
 not supported by RFmx NR.

#### Single-Carrier ACP

- NR offset channels for single carrier
- UTRA offset channels for single carrier

For the NR Offset Channels for Single Carrier type, the
 NR ACLR (NR<sub>ACLR</sub>) is the ratio of the filtered average
 power centered on an adjacent NR channel to the filtered average power centered on
 the carrier channel.

The following table shows channel spacing and measurement
 bandwidths for FR1.

| Number Of NR Offsets = m | Channel Bandwidth, FR1 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 3 MHz | 5 MHz | 7 MHz | 10 MHz | 15 MHz | 20 MHz | 25 MHz | 30 MHz | 35 MHz | 40 MHz | 45 MHz | 50 MHz | 60 MHz | 70 MHz | 80 MHz | 90 MHz | 100 MHz |  |
| NR Center Frequency Offset (MHz) | m * 3 or -m * 3 | m * 5 or -m * 5 | m * 7 or -m * 7 | m * 10 or -m * 10 | m * 15 or -m * 15 | m * 20 or -m * 20 | m * 25 or -m * 25 | m * 30 or -m * 30 | m * 35 or -m * 35 | m * 40 or -m * 40 | m * 45 or -m * 45 | m * 50 or -m * 50 | m * 60 or -m * 60 | m * 70 or -m * 70 | m * 80 or -m * 80 | m * 90 or -m * 90 | m * 100 or -m * 100 |
| NR Channel Measurement Bandwidth (MHz) | 2.715 | 4.515 | 6.315 | 9.375 | 14.235 | 19.095 | 23.955 | 28.815 | 33.855 | 38.895 | 43.575 | 48.615 | 58.35 | 68.07 | 78.15 | 88.23 | 98.31 |

*70 MHz Channel Bandwidth are not specified in
 the *3GPP TS 38.101-1* specification. The measurement bandwidth was added
 for consistency with DL configurations.

| Number Of NR Offsets = m | Channel Bandwidth, FR2 |  |  |  |
| --- | --- | --- | --- | --- |
| 50 MHz | 100 MHz | 200 MHz | 400 MHz |  |
| NR Center Frequency Offset (MHz) | m * 50 or -m * 50 | m * 100 or -m * 100 | m * 200 or -m * 200 | m * 400 or -m * 400 |
| NR Channel Measurement Bandwidth (MHz) | 47.58 | 95.16 | 190.20 | 380.28 |

#### UTRA Offset Channels for Single
 Carrier (FR1 only)

The UTRA ACLR (UTRA<sub>ACLR</sub>) is the ratio of the filtered average power
 centered on an adjacent UTRA channel to the filtered average power centered on the
 carrier channel, with channel spacing and measurement bandwidths as specified in the
 preceding table. UTRA ACLR is measured for two UTRA adjacent channels by default for
 FR1 only.

Channel Bandwidth: BW<sub>NR</sub> e{3, 5, 7, 10, 15, 20, 25, 30, 35, 40,
 45, 50, 60, 70, 80, 90, 100} MHz

BW<sub>UTRA</sub> for UTRA
 offset channel = 5 MHz.

UTRA<sub>ACLR(n)</sub>
 Center Frequency Offset (MHz) is calculated as follows:

B

W

N

R

/

2

+

2

×

n

+

1

×

B

W

U

T

R

A

/

2

UTRA Measurement Bandwidth = 3.84 MHz.

#### Intra-band Contiguous Carrier
 Aggregation ACP

Intra-band contiguous carrier aggregation ACP is similar to the single-carrier
 scenario, and the aggregated carrier is considered to be one NR carrier. UTRA
 channel configurations are similar to the single-carrier configuration scenarios.
 The adjacent offset channels are placed relative to the center of aggregated carrier
 bandwidth.

#### NR Offset Channels for Contiguous
 Carrier Aggregation

The center of the first adjacent NR channel is located at the aggregated carrier
 bandwidth away from the center of assigned NR channel frequency. The measurement
 bandwidth is the same as the measurement bandwidth of the assigned NR channel
 (aggregated NR carriers). The power of this NR adjacent channel is measured with a
 rectangular filter.

Similarly, the center of successive NR offset channels are
 (m × CA_BW) away from the center of the assigned NR channel
 (aggregated NR carriers) for the m the NR offset, where
 CA_BW is the aggregated channel bandwidth.

#### UTRA Offset Channels for
 Contiguous Carrier Aggregation (FR1 only)

The UTRA measurement bandwidths are similar to the measurement bandwidths of the
 single carrier. The center of the UTRA offset channels are [CA_BW + (2 ×
 n - 1) BW <sub>UTRA</sub>]/2 away from the
 center of the assigned NR channel (aggregated NR carriers) for the
 nth UTRA offset, where CA_BW is the
 aggregated carriers channel bandwidth.

#### Intra-band Non-contiguous Carrier
 Aggregation ACP

In the intra-band non-contiguous carrier aggregation scenario, UTRA (for FR1 only)
 and NR offset channels to the right and left of each subblock are measured, which
 means that some offset channels between the two subblocks are called inner offset
 channels.

The following image shows a typical carrier channel and offset
 channel configuration for the NR intra-band non-contiguous configuration with two
 subblocks each comprising of two component carriers.

- U1, U2, U3, and U4 UTRA offset channels and NR1 and NR2 NR offset channels
 are positioned relative to the first subblock comprising component carriers
 S0:C0 and S0:C1, similar to performing a contiguous carrier aggregation ACP
 measurement with component carriers S0:C0 and S0:C1.
- U5 through U8, NR3, and NR4 are positioned relative to the subblock
 consisting of component carriers S1:C0 and S1:C1.

Similarly, the relative power of the offset channel is reported as
 relative to the sum of the aggregated powers of the two subblocks.

Figure 3.

[IMAGE alt='Chart showing NR and UTRA Offset Channels Configurations for Non-Contiguous Carrier Aggregation' src='GUID-D573F2E8-0827-4727-BAF6-331A500C14B1-a5.png']

#### NR Offset Channels for Intra-band
 Non-contiguous Carrier Aggregation

Normally, one NR offset channel is considered for intra-band non-contiguous carrier
 aggregation. If the inner NR offset channel of a subblock overlaps with another
 subblock, the inner NR offset is not measured, and NaN is returned as a
 result.

The following figure shows all possible cases for inner NR offsets
 with and without overlap with the adjacent subblock.

- SB-A and SB-B are two subblocks.
- NR-A is the NR offset channel for subblock A.
- NR-B is the NR offset channel for subblock B.

Figure 4.

[IMAGE alt='Flowchart showing Intraband Non-contiguous ACP: Inner NR Offset Channel and Subblock Gap Size' src='GUID-1BF9ED42-F3ED-4DA4-A61C-BE87E018589E-a5.png']

#### UTRA Offset Channels for
 Intra-band Non-contiguous Carrier Aggregation (FR1 only)

Two UTRA offset channels are always considered for intra-band non-contiguous carrier
 aggregation. If the gap between two adjacent subblocks is less than 5 MHz, no inner UTRA offset channel is measured. In
 this case NaNs are returned for both the inner UTRA channels.

If the gap
 between two adjacent subblocks greater than or equal to 5
 MHz but is less than 15 MHz, one inner UTRA
 offset channel is measured. In this case, NaNs are returned for other inner UTRA
 channels. Both inner UTRA offset channels are measured if the gap between two
 adjacent subblocks is greater than or equal to 15
 MHz.

For any subblock, if any of its UTRA offset channel (inner) overlaps
 with another subblock, the UTRA offset is not measured. In this case, NaN is
 returned as the result.

The following figure depicts all possible cases of
 inner UTRA offset with and without overlap with the adjacent subblock.

- SB-A and SB-B are two subblocks.
- U1 is the first UTRA offset channel.
- U1-A is the first UTRA offset channels for subblock A.
- U2 is the second UTRA offset channel.
- U2-B is the second UTRA offset channels for subblock B.

Figure 5.

[IMAGE alt='Flowchart showing Intraband Non-contiguous ACP: UTRA Offset Channel and Subblock Gap Size' src='GUID-E23F4AAF-9049-4BA8-858A-1EE0A93FDD13-a5.png']

#### Offset Result Ordering

The offset measurement results are reported per subblock. Depending on the frequency
 of the subblock with relative to other subblocks, the order of reporting of results
 is affected.

| Offset | Left Sublock | Inner Subblock (optional) | Right Subblock |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Lower | Upper | Lower | Upper | Lower | Upper |  |
| UTRA0 Offsets | OuterUTRA0 | InnerUTRA0 | InnerUTRA0 | InnerUTRA0 | InnerUTRA0 | OuterUTRA0 |
| UTRA1 Offsets | OuterUTRA1 | InnerUTRA1 | InnerUTRA1 | InnerUTRA1 | InnerUTRA1 | OuterUTRA1 |
| NR Offsets | OuterNR0 | InnerNR0 | InnerNR0 | InnerNR0 | InnerNR0 | OuterNR0 |

In this table:

- OuterNR [x] are NR ACLR outer offset measurements.
- InnerNR [x] are NR ACLR inner offset measurements.
- OuterUTRA [x] are UTRA ACLR outer offset measurements.
- InnerUTRA [x] are UTRA ACLR inner offset measurements.

The number of inner offset measurements depends on the gap between subblocks.
 UTRA offsets apply only to FR1 ACP measurements.

Parent topic:

Adjacent Channel Power

Related information:

- ACP
- RFmx SpecAn User Manual

<!--NI_TOPIC bundle=rfmx-nr path=nr-uplink-en-dc-acp.html language=enus -->
## TOPIC 00021: NR Uplink EN-DC Adjacent Channel Power (FR1 Only)

- bundle_id: `rfmx-nr`
- source_path: `nr-uplink-en-dc-acp.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr/raw/resource/enus/nr-uplink-en-dc-acp.html
- document_id: `rfmx-nr`
- page_type: `leaf`
- content_type: `concept`
- source_description: RFmx NR measures adjacent channel power for NR uplink in EN-DC configurations, including bandwidth, frequency offsets, and ACLR calculations per 3GPP specifications for FR1 scenarios. Intra-band Contiguous Carrier Aggregation ACP This applies for cases where the NR subblock is immediately adjacent t

### NR Uplink EN-DC Adjacent Channel Power (FR1 Only)

RFmx NR measures adjacent channel power for NR uplink
 in EN-DC configurations, including bandwidth, frequency offsets, and ACLR calculations per
 3GPP specifications for FR1 scenarios.

#### Intra-band Contiguous Carrier
 Aggregation ACP

Section 6.5B.2.1.3.1

3GPP TS
 38.521-3

E-UTRA

- Measurement bandwidth of EN-DC channel: 1.00 * ENBW
- Measurement bandwidth of offset channel: 0.95 * ENBW
- Frequency offset with respect to the center of the aggregated subblock: ENBW
 and -ENBW

where ENBW denotes the sum of the subblock bandwidths.

Note

#### Intra-band Non-Contiguous Carrier
 Aggregation ACP

The ACLR for intra-band non-contiguous EN-DC is defined as the ratio of the subblock
 power to the power of the adjacent channel at nominal spacing. In case the subblock
 gap is smaller than the measurement bandwidth of the offset channel, ACLR is not
 measured. The measurement bandwidth for the E-UTRA subblock is defined in the
 *3GPP 36.521* specification and for the NR subblock is defined in the
 *3GPP 38.521-1* specification.

Note

Parent topic:

Adjacent Channel Power

<!--NI_TOPIC bundle=rfmx-nr path=nr-uplink-en-dc-sem.html language=enus -->
## TOPIC 00022: NR Uplink EN-DC Spectral Emission Mask

- bundle_id: `rfmx-nr`
- source_path: `nr-uplink-en-dc-sem.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr/raw/resource/enus/nr-uplink-en-dc-sem.html
- document_id: `rfmx-nr`
- page_type: `leaf`
- content_type: `concept`
- source_description: Measures Spectrum Emission Mask for 5G NR uplink in EN-DC mode, ensuring compliance with emission limits and validating transmitter performance in RFmx NR. The RFmx NR spectral emission mask (SEM) measurement uses the configurations and masks specified by the 3GPP TS 38.101-3 specification. This top

### NR Uplink EN-DC Spectral Emission Mask

Measures Spectrum Emission Mask for 5G NR uplink in EN-DC mode, ensuring compliance
 with emission limits and validating transmitter performance in RFmx NR.

The RFmx NR spectral emission mask (SEM) measurement uses the
 configurations and masks specified by the 3GPP TS 38.101-3
 specification. This topic explains the configurations and masks used by the RFmx NR Uplink EN-DC SEM measurement.

For a general overview of single and multicarrier SEM measurement concepts, refer to the
 *SEM* topic in the *RFmx SpecAn User Manual*.

#### Offset Segments

The offset segments are the channels adjacent to the carrier channels and are
 specified by their start and stop frequencies (Δf<sub>OOB</sub>)
 relative to the nearest edge of assigned NR channel or carrier aggregated channels.
 The offset segment frequencies and bandwidths are defined by *3GPP TS
 38.101-3* specification.

The power of any offset segment is
 measured with the measurement filter defined in section 6.5B.2 of the *3GPP TS
 38.101-3* specification. While measuring offset segment power, the
 following rules are followed that are defined by *3GPP TS 38.101-3*
 specification test requirements:

- For all the offset segments, the first and last measurement position is at
 Δf OOB ± ( Measurement
 Bandwidth/2 ), respectively.
- The measurements are performed above the upper edge of the channel and below the
 lower edge of the channel.

The RBW filter for all offset segments is Gaussian, and the resolution
 bandwidths are set according to the measurement bandwidth defined in 3GPP
 specification.

The accuracy of the measurement is increased by using a
 resolution bandwidth smaller than the measurement bandwidth. The measurement
 bandwidth gets divided by the bandwidth integral to realize a lower resolution
 bandwidth. However, the results are obtained by integrating over the measurement
 bandwidth.

#### Masks

The power of any UE emission must not exceed the limits specified for a mask type for
 different offset segments. As per the 3GPP TS 38.101-3
 specification, the measurement passes if the power spectrum values for all offset
 segments are less than this limit.

You can choose the Standard Mask
 Type to specify either general masks/ limits or any other additional
 mask defined by 3GPP.

#### Intra-Band Contiguous EN-DC
 SEM

3GPP has defined spectrum emission limit where the offset segments are defined
 Δf<sub>OOB</sub> frequency away from the edge of the
 aggregated carrier. The rest of the requirements are the same as that of uplink
 single carrier. The following table is defined for intra-band contiguous
 EN-DC.

For more information about intra-band contiguous EN-DC SEM base
 requirements, refer to the following table:

- Table 6.5B.2.1.1-1, General spectrum emission mask for intra-band contiguous
 EN-DC from 3GPP TS 38.101-3 specification.

For more information about intra-band contiguous EN-DC SEM additional
 requirements base requirements, refer to the following table:

- Table 6.5B.2.1.2.1-1, Additional Requirement from 3GPP TS 38.101-3 
 specification.
- Table 6.5B.2.1.2.2-1, DC_(n)41 SEM with NS_04 from 3GPP TS 38.101-3 
 specification.

#### Intra-band Non-Contiguous Carrier
 Aggregated SEM

For intra-band non-contiguous, the requirement is same as the intra-band contiguous
 configurations, and each subblock is treated separately if the subblock gaps have no
 overlapping offset segments. If a subblock has only E-UTRA carrier(s) or NR
 carrier(s), then standard specific mask is applied on that Subblock.

Note

Sometimes, the offset segments between two adjacent subblocks may overlap.
 In such scenarios, the general spectrum emission mask requirement is defined as a
 composite general emission mask.

Composite spectrum emission
 mask is defined as follows:

- The composite spectrum emission mask is a combination of subblock general
 emissions masks.
- Subblock (general and additional) emission masks are the same as that of single
 carrier and contiguous carrier aggregation requirements.
- If the subblock (general or additional) spectrum emission masks overlap for a
 frequency, the spectrum emission mask with the higher power spectral density
 applies for that frequency.

If a subblock spectrum emission mask overlaps with the subblock bandwidth of
 another subblock for a frequency, the mask does not apply for that frequency.

Parent topic:

RFmx NR Measurement Concepts

Related information:

- SEM

<!--NI_TOPIC bundle=rfmx-nr path=nr-uplink-sem.html language=enus -->
## TOPIC 00023: NR Uplink Spectral Emission Mask

- bundle_id: `rfmx-nr`
- source_path: `nr-uplink-sem.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr/raw/resource/enus/nr-uplink-sem.html
- document_id: `rfmx-nr`
- page_type: `leaf`
- content_type: `concept`
- source_description: Measures the uplink spectrum emission mask for 5G NR signals, ensuring compliance with emission limits in RFmx NR testing workflows. The RFmx NR spectral emission mask (SEM) measurement uses the configurations and masks specified by the 3GPP TS 38.101-1(FR1) and 3GPP TS 38.101-2(FR2) specification.

### NR Uplink Spectral Emission Mask

Measures the uplink spectrum emission mask for 5G NR signals, ensuring compliance
 with emission limits in RFmx NR testing workflows.

The RFmx NR spectral emission mask (SEM) measurement uses the configurations and masks specified
 by the *3GPP TS 38.101-1(FR1)* and *3GPP TS 38.101-2(FR2)*
 specification.

For a general overview of single and multicarrier SEM measurement concepts, refer to the
 *SEM* topic in the *RFmx SpecAn User Manual*.

#### Offset Segments

The offset segments are the channels adjacent to the carrier channels and are
 specified by their start and stop frequencies (Δf<sub>OOB</sub>)
 relative to the nearest edge of assigned NR channel or carrier aggregated channels.
 The offset segment frequencies and bandwidths are defined by *3GPP TS 38.101-1
 (FR1)* and *3GPP TS 38.101-2(FR2)* specification for all NR
 carrier channels and CA for FR2.

The power of any offset segment is measured
 with the measurement filter defined in section 6.5.2 of the *3GPP TS
 38.101-1(FR1)* and *3GPP TS 38.101-2(FR2)* specification. While
 measuring offset segment power, the following rules are followed that are defined by
 *3GPP TS 38.101-1(FR1)* and *3GPP TS 38.101-2(FR2)*
 specification test requirements:

- For all offset segments, the first measurement position is computed as (lower
 limit of Δf OOB + Measurement
 Bandwidth/2 ), and the last measurement position is computed as
 (upper limit of Δf OOB - Measurement
 Bandwidth/2 ).
- The measurements are performed above the upper edge of the channel and below the
 lower edge of the channel.

The RBW filter for all offset segments are Gaussian, and the resolution
 bandwidths are set according to the measurement bandwidth defined in 3GPP
 specification.

The accuracy of the measurement is increased by using a
 resolution bandwidth smaller than the measurement bandwidth. The measurement
 bandwidth is divided by the SEM Offset BW Integral property to realize a lower
 resolution bandwidth. However, the results are obtained by integrating over the
 measurement bandwidth.

#### Masks

The power of any UE emission must not exceed the limits specified for a mask type for
 different offset segments. As per the *3GPP TS 38.101-1(FR1)* and
 *3GPP TS 38.101-2(FR2)* specification, the measurement passes if the
 power spectrum values for all offset segments are less than this limit.

You
 can choose the Standard Mask Type to specify either general masks/ limits or any
 other additional mask defined by 3GPP.

#### Single-Carrier SEM

The following sections list the tables that are defined by the *3GPP TS
 38.101-1(FR1)* and *3GPP TS 38.101-2(FR2)* specification for a
 single carrier.

single-carrier base
 requirements

- Table 6.5.2.2-1, General NR spectrum emission mask for frequency range 1 from
 3GPP TS 38.101-1 specification
- Table 6.5.2.1-1, General NR spectrum emission mask for frequency range 2 from
 3GPP TS 38.101-2 specification

For more information about single-carrier additional
 requirements, refer to the following tables defined for frequency range
 1:

- Table 6.5.2.3.1-1, Additional requirements (network signaled value "NS_35") from
 3GPP TS 38.101-1 specification
- Table 6.5.2.3.2-3, Additional requirements (network signaled value "NS_04") from
 3GPP TS 38.101-1 f82 and 38.101-1 g20 
 specification
- Table 6.5.2.3.3-1, Additional requirements (network signaled value "NS_03") from
 3GPP TS 38.101-1 f82 and 38.101-1 g20 
 specification
- Table 6.5.2.3.4-1, Additional requirements (network signaled value "NS_06") from
 3GPP TS 38.101-1 specification
- Table 6.5.2.3.3-1, Additional requirements (network signaled value "NS_21") from
 3GPP TS 38.101-1 g20 specification
- Table 6.5.2.3.8-1, Additional requirements (network signaled value "NS_27") from
 3GPP TS 38.101-1 g60 specification

Note

#### Intra-Band Contiguous Carrier
 Aggregated SEM

3GPP has defined spectrum emission limit for carrier aggregation in frequency range
 2, where the offset segments are defined Δf<sub>OOB</sub>
 frequency away from the edge of the aggregated carrier. The rest of the requirements
 are the same as that of single carrier. The following table is defined for frequency
 range 2.

For more information about Intra-Band Contiguous Carrier
 Aggregated SEM base requirements, refer to the following tables:

- Table 6.5A.2.2.1-1, General NR CA spectrum emission mask for intra-band
 contiguous CA in frequency range 1
- Table 6.5A.2.1-1, General NR spectrum emission mask for intra-band contiguous CA
 in frequency range 2

For more information about Intra-Band Contiguous Carrier Aggregated SEM
 additional requirements, refer to the following tables defined for
 frequency range 1:

- Table 6.5A.2.3.1.1-1, Additional requirements (network signaled value
 "CA_NS_04") from 3GPP TS 38.101-1 g60 specification
- Table 6.2A.2.3.2.1-1, Additional requirements (network signaled value
 "CA_NS_27") from 3GPP TS 38.101-1 g60 specification

#### Intra-band Non-Contiguous Carrier
 Aggregated SEM

For intra-band non-contiguous, the requirement is the same as the single carrier and
 intra-band contiguous configurations, and each subblock is treated separately if the
 subblock gaps have no overlapping offset segments.

At times, the offset
 segments between two adjacent subblocks may overlap. In such scenarios, the general
 spectrum emission mask requirement is defined as a composite general emission
 mask.

Composite spectrum emission mask is defined as follows:

- The composite spectrum emission mask is a combination of subblock general
 emissions masks.
- Subblock (general and additional) emission masks are the same as that of single
 carrier and contiguous carrier aggregation requirements.
- If the subblock (general or additional) spectrum emission masks overlap for a
 frequency, the spectrum emission mask with the higher power spectral density
 applies for that frequency.

If a subblock spectrum emission mask overlaps with the subblock bandwidth of
 another subblock for a frequency, the mask does not apply for that frequency.

The following figure shows two carrier channel and offset channel
 configurations for the NR intra-band non-contiguous configuration with two subblocks
 A and B. Subblock A is comprised of two contiguous component carriers (CC-A0 and
 CC-A1). Similarly, subblock B is comprised of three contiguous component carriers
 (CC-B0, CC-B1, and CC-B2). Offset segments are denoted as OA and OB.

[IMAGE alt='image' src='GUID-D807E7BC-C4A0-43F6-931F-1B2131479089-a5.png']

The rightmost offset segment of subblock A, OA-R1 and leftmost offset segment of
 subblock B, OB-L2 overlaps in the above picture. In this case, the combined spectral
 emission mask is calculated considering highest power spectral density (PSD) value
 of all overlapping masks for that frequency.

[IMAGE alt='image' src='GUID-2B1D13EE-1694-4F40-AED6-5B8E7303EC10-a5.png']

Parent topic:

RFmx NR Measurement Concepts

Related information:

- SEM

<!--NI_TOPIC bundle=rfmx-nr path=resource-grid-configuration.html language=enus -->
## TOPIC 00024: Resource Grid Configuration

- bundle_id: `rfmx-nr`
- source_path: `resource-grid-configuration.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr/raw/resource/enus/resource-grid-configuration.html
- document_id: `rfmx-nr`
- page_type: `leaf`
- content_type: `concept`
- source_description: Defines resource grid size and start for 5G NR carriers, enabling accurate bandwidth part alignment and signal analysis in RFmx NR. The 5G NR standard allows the use of multiple resource grids with different numerology (parameter μ and the equivalent subcarrier spacing) within a single carrier. The

### Resource Grid Configuration

Defines resource grid size and start for 5G NR carriers, enabling accurate bandwidth
 part alignment and signal analysis in RFmx NR.

The 5G NR standard allows the use of multiple resource grids with different numerology
 (parameter μ and the equivalent subcarrier spacing) within a single carrier. The
 combination of configured resource grids in a single carrier determines their location
 with respect to each other in the frequency domain.

In RFmx NR, you can specify the resource grid parameters
 Grid Start and Grid Size for each active
 numerology.

Common use cases are:

- Configurations with one BWP in UL or DL for measurements on shared channels (PUSCH
 and PDSCH) or control channels (PDCCH) in the presence of a Reference Grid with a
 numerology other than the BWP numerology.
- Configurations for DL signals with active BWP and SS/PBCH blocks each with a
 different numerology.

#### Reference Point A and Carrier Center
 Frequency

The 5G NR standard uses the concept of a so-called Point A as a common reference
 frequency for all defined resource grids and the SS/PBCH (SSB) location in
 frequency.

However, RFmx NR defines the center of the allocated carrier as the
 center of the reference resource grid transmission bandwidth configuration. The
 reference resource grid is given by the RFmx NR user either explicitly set by you or
 automatically set based on the signal configuration.

The following figure
 illustrates the frequency relationship of two resource grids within a single
 carrier. For a 10 MHz bandwidth signal, the default
 transmission bandwidth configuration (N<sub>RB</sub>) is given as 11 RB for the 60 kHz
 subcarrier spacing grid, and 24 RB for the 30 kHz subcarrier spacing grid. For each subcarrier
 spacing grid, there is also a different guard band spacing between the transmission
 bandwidth and the defined channel edge (See section 5.3.2 and
 section 5.3.3 of the 3GPP TS 38.104
 specification).

[IMAGE alt='image' src='GUID-D2E96338-372E-4B87-BD83-1474870D06A5-a5.png']

The example shows the usage of a non-standard grid start configuration for the
 reference grid (Grid Start = 3) and the BWP grid μ (Grid Start = 5) to set the
 offset to Point A, specifically. As previously mentioned, the carrier center
 frequency falls on the subcarrier in the center of the reference grid
 μ<sub>0</sub>.

#### Signal Configuration Options

RFmx NR provides different options to simplify the configuration of resource grids.
 The configuration is differentiated between the alignment of resource grids relative
 to Point A (Reference Grid Alignment Mode) and the transmission bandwidth
 configuration (Grid Size Mode).

In most test applications, the default
 resource grid configuration will be sufficient. However, for advanced use cases,
 RFmx NR also supports a manual configuration of the Grid Size and the Grid Start
 parameter.

The 3GPP standard does not define a default Point A for test
 applications. A manual configuration of the Grid Start parameter allows you to
 define Point A to match your test signal configuration.

In order to increase
 flexibility, the Grid Size is configured to a value that exceeds the transmission
 bandwidth configuration for a given carrier bandwidth as defined in the 3GPP
 specification.

If you set the Grid Size Mode property to
 Auto, the following restrictions apply:

- The Grid Size of the resource grids are automatically set to transmission
 bandwidth configuration (N RB ) as specified by the 3GPP
 RAN4 specifications.
- The BWP configuration is limited to the specified guard band within the channel
 bandwidth, irrespective of Ref Grid Alignment Mode.
- The location of the transmission bandwidth configuration is limited to the
 channel bandwidth.

Setting the Grid Size Mode property to Manual results in
 a few restrictions being relaxed:

- The location of the transmission bandwidth configuration is limited to the
 channel bandwidth.
- The BWP configuration is limited by the channel bandwidth only and not by the
 guard band.

#### References

- Section 4.4.4 - Resource Blocks and Section 5.3.1 - OFDM baseband signal generation
 of the 3GPP TS 38.211 specification for all channels except PRACH
 and RIM-RS
- Section 5.3 - BS channel bandwidth of the 3GPP TS 38.104
 specification
- Section 5.3 - UE channel bandwidth of the 3GPP TS 38.101-1/-2
 specification

Parent topic:

RFmx NR Signal Configuration Concepts

<!--NI_TOPIC bundle=rfmx-nr path=sem-overview.html language=enus -->
## TOPIC 00025: Spectral Emission Mask

- bundle_id: `rfmx-nr`
- source_path: `sem-overview.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr/raw/resource/enus/sem-overview.html
- document_id: `rfmx-nr`
- page_type: `leaf`
- content_type: `concept`
- source_description: Measures spectrum emissions for 5G NR signals, ensuring compliance with emission masks and standards in RFmx NR analysis. Spectral emission mask (SEM) measurements measure out-of-band emissions in the neighboring bands of the carrier. In measurements such as ACP, the emissions may remain undetected

### Spectral Emission Mask

Measures spectrum emissions for 5G NR signals, ensuring compliance with emission
 masks and standards in RFmx NR analysis.

Spectral emission mask (SEM) measurements measure out-of-band emissions in the
 neighboring bands of the carrier. In measurements such as ACP, the emissions may remain
 undetected when measuring the integrated power in the band. SEM uses the spectral mask
 or limit you specify to measure the margin of the emission level from the limit and
 reports the measurement status.

The following figure shows the configuration of SEM carriers and offset segments.

[IMAGE alt='image' src='GUID-FD590869-4050-449B-8301-77989184B600-a5.png']

#### Carrier Channels

Carriers are channels in
 which significant power is transmitted and for which power leakage in the offset
 channels is measured. Multiple carriers are configured relative to the RF center
 frequency by specifying the carrier offset. Each carrier is configured for the
 integration bandwidth (IBW), RBW, and RRC channel filter. Power in each carrier is
 measured by integrating the power in the specified IBW after applying the channel
 filter. The total carrier power measured is the aggregate power of all the active
 carriers.

#### Offset Segments

Offset segment start and
 stop frequencies are specified relative to the closest carrier offset frequency. The
 placement of the offset segments with respect to the nearest carrier is defined by
 the SEM offset frequency definition.

Offset Frequency
 Definition

The offset frequency definition defines the offset start and
 stop frequency of the offset segment with respect to the nearest carrier channel in
 one of the following ways:

- Carrier Center to Meas BW Center —The start frequency and
 stop frequency are defined from the center of the closest carrier channel
 bandwidth to the center of the offset segment measurement bandwidth
 respectively.
- Carrier Center to Meas BW Edge —The start frequency and
 stop frequency are defined from the center of the closest carrier channel
 bandwidth to the nearest edge of the offset segment measurement bandwidth
 respectively.
- Carrier Edge to Meas BW Center —The start frequency and
 stop frequency are defined from the nearest edge of the closest carrier channel
 bandwidth to the center of the nearest offset segment measurement bandwidth
 respectively.
- Carrier Edge to Meas BW Edge —The start frequency and stop
 frequency are defined from the nearest edge of the closest carrier channel
 bandwidth to the edge of the nearest offset segment measurement bandwidth
 respectively.

The measurement bandwidth of the offset segment is the bandwidth represented by
 the RBW and bandwidth integral values as shown in the following equation:
 Measurement Bandwidth = RBW *
 Bandwidth Integral

The following image describes the
 offset frequency definitions:

[IMAGE alt='image' src='GUID-02E7352C-2011-41A2-BF76-57FEEE3A97CE-a5.png']

Offset Sideband

An offset segment is configured on either side of
 the carrier when you set the offset sideband to BOTH. Only one offset sideband is
 configured when you configure a positive (POS) or negative (NEG) sideband. Negative
 sideband creates a lower offset segment to the left of the leftmost carrier.
 Positive sideband creates an upper offset segment to the right of the rightmost
 carrier. Each offset segment is configured for IBW, RBW, RRC filter, relative
 attenuation, spectral mask, and measurement failure criteria.

#### RBW and Sweep Time

RBW is configured for
 each carrier and offset segment. When you set the RBW to Auto, the measurement sets
 the RBW using the following ratio:

IBW:RBW<sub>3dB</sub> =
 100, where RBW<sub>3dB</sub> is a value between 1 Hz and 1 MHz

When you set
 the sweep time to Auto, the measurement sets the sweep time using the following
 value:

- k /RBW 3dB when the RBW filter is FFT based, where
 k is a constant that depends on the FFT window
- 10/RBW 3dB for other RBW filters

For more information about RBW, sweep time, and averaging, refer to the topics
 in the *RFmx SpecAn User Manual*.

#### Power Measurement

Power
 Units

The absolute power values measured are reported in dBm (integrated
 power) or dBm/Hz (power spectral density). The relative power values are not
 affected by the units specified.

Use relative attenuation to compensate for
 external attenuation for each offset channel.

Relative Power
 Reference

Carriers are measured relative to the total power of all
 enabled carriers.

Offset segment power is measured relative to either
 integrated power or the peak power of the closest carrier. Use the SEM Ref Type
 property to specify integrated power or peak power as reference.

Note

#### Spectral Mask

Limit
 Lines

The absolute and/or relative limit lines for each offset segment
 define the spectral mask. A limit line is defined by a start and stop power. Start
 power corresponds to the frequency point closer to the carrier. A level line can be
 configured by specifying the start power limit and coupling it to the stop power
 using the SEM Offset Relative Limit Mode.

Relative limits are specified
 relative to the integrated power or peak power of the carrier closest to the offset
 segment. Use the SEM Ref Type property to specify whether to use integrated power or
 peak power.

Margin and Measurement Status

The spectrum is
 corrected for external attenuation for each offset based on the specified relative
 attenuation. This spectrum is compared against the limit lines to report margin and
 measurement PASS/FAIL status. Margin, in dB, is the largest difference between the
 measured spectrum and the limit line.

The measurement failure criteria, also
 called the limit fail mask, can be one of the following criteria:

- Absolute —Checks for emissions crossing the absolute limit
 line.
- Relative —Checks for emissions crossing the relative limit
 line.
- Absolute AND Relative —Checks for emissions crossing both
 the absolute and relative limit lines. The highest margin with respect to the
 higher limit mask is reported.
- Absolute OR Relative —Checks for emissions crossing either
 the absolute or relative limit lines. The highest margin with respect to the
 lower limit mask is reported.

The measurement returns the frequency and absolute power (dBm or dBm/Hz) at the
 reported margin, and it also returns the power relative to the integrated power or
 the peak power based on the value of the SEM Ref Type property.

Note

Parent topic:

RFmx NR Measurement Concepts

Related information:

- RFmx SpecAn User Manual

<!--NI_TOPIC bundle=rfmx-nr path=subblock.html language=enus -->
## TOPIC 00026: Subblock

- bundle_id: `rfmx-nr`
- source_path: `subblock.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr/raw/resource/enus/subblock.html
- document_id: `rfmx-nr`
- page_type: `leaf`
- content_type: `concept`
- source_description: A subblock is a collection of contiguous component carriers used for transmission and reception by the same user equipment (UE). Intra-band contiguous carrier aggregation uses one subblock. Intra-band and inter-band noncontiguous carrier aggregation use two or more subblocks. The following image sho

### Subblock

A subblock is a collection of contiguous component carriers used for transmission and
 reception by the same user equipment (UE). Intra-band contiguous carrier aggregation
 uses one subblock. Intra-band and inter-band noncontiguous carrier aggregation use two
 or more subblocks.

The following image shows the two subblocks, subblock A and subblock B.

[IMAGE alt='image' src='GUID-5048FFBC-FAFB-4B5A-AC93-3F30211F47ED-a5.png']

Parent topic:

Carrier Aggregation

<!--NI_TOPIC bundle=rfmx-nr path=supported-hw.html language=enus -->
## TOPIC 00027: Supported Hardware

- bundle_id: `rfmx-nr`
- source_path: `supported-hw.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr/raw/resource/enus/supported-hw.html
- document_id: `rfmx-nr`
- page_type: `leaf`
- content_type: `concept`
- source_description: RFmx supports a number of NI devices. 1 RFmx NR Supported Hardware RFmx NR Hardware Earliest Driver Version Support (Windows 11) PXIe-5644 2022 Q3 PXIe-5645 2022 Q3 PXIe-5646 2022 Q3 PXIe-5663 2022 Q3 PXIe-5665 2022 Q3 PXIe-5668 2022 Q3 PXIe-5820 2022 Q3 PXIe-5840 2022 Q3 PXIe-5841 (1 GHz Bandwidth)

### Supported Hardware

RFmx supports a number of NI devices.

| RFmx NR Hardware | Earliest Driver Version Support (Windows 11) |
| --- | --- |
| PXIe-5644 | 2022 Q3 |
| PXIe-5645 | 2022 Q3 |
| PXIe-5646 | 2022 Q3 |
| PXIe-5663 | 2022 Q3 |
| PXIe-5665 | 2022 Q3 |
| PXIe-5668 | 2022 Q3 |
| PXIe-5820 | 2022 Q3 |
| PXIe-5840 | 2022 Q3 |
| PXIe-5841 (1 GHz Bandwidth) | 2022 Q3 |
| PXIe-5842 | 2022 Q4 |
| PXIe-5860 | 2024 Q3 |

Note

RFmx NR

NI-RFSA
 Properties

NI-RFSA LabVIEW VI Reference

For more information about your hardware and functionality, refer to the *NI-RFSA User Manual*.

Related information:

- NI-RFSA User Manual
- NI-RFSA Properties

<!--NI_TOPIC bundle=rfmx-nr path=symbol-phase-compensation.html language=enus -->
## TOPIC 00028: Symbol Phase Compensation

- bundle_id: `rfmx-nr`
- source_path: `symbol-phase-compensation.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr/raw/resource/enus/symbol-phase-compensation.html
- document_id: `rfmx-nr`
- page_type: `leaf`
- content_type: `concept`
- source_description: Adjusts for phase discontinuities caused by differing center frequencies between transmitter and receiver in 5G NR signals, ensuring accurate analysis and measurement in RFmx NR applications. The 3GPP NR compliant signal has a unique feature of the base station (BS) with a wider bandwidth being able

### Symbol Phase Compensation

Adjusts for phase discontinuities caused by differing center frequencies between
 transmitter and receiver in 5G NR signals, ensuring accurate analysis and measurement in
 RFmx NR applications.

The 3GPP NR compliant signal has a unique feature of the base station (BS) with a wider
 bandwidth being able to communicate with the user equipment (UE) of a narrower
 bandwidth. Due to this feature, the BS may generate reference signals relative to its
 center frequency, and the UE can tune the center of its bandwidth to receive this
 reference signal.

Due to the difference in center frequencies between BS and UE, the phase of a symbol jumps at
 symbol boundaries. To address this issue, Section 5.3 of the *3GPP 38.211*
 specification introduces phase compensation at the transmitter and the receiver, which
 is a function of absolute center frequency used at the transmitter and the receiver.
 This impacts the cases where the BS and UE center frequencies are different as well.

To support analyzing such signals using RFmx NR, Ph Compensation
 property is set to User Defined and Ph Comp Freq
 (Hz) property for each subblock, where Ph Comp Freq (Hz) property specifies
 the absolute frequency used for phase compensation of the signal by the transmitter, or
 Ph Compensation property is set to Auto for the measurement to
 automatically use the RF center frequency of the analyzer as phase compensation
 frequency. By default, Ph Compensation is Disabled.

RF characteristics do not change when using signals with and without phase compensation.
 The characteristics are laborious to create signals with phase compensation as signals must be created for
 each frequency that the RFIC or transceiver sweeps. It is recommended to not use signals
 with Phase Compensation for characterization and production test applications.

Parent topic:

RFmx NR Signal Configuration Concepts

<!--NI_TOPIC bundle=rfmx-nr path=system-requirements.html language=enus -->
## TOPIC 00029: RFmx NR System Requirements

- bundle_id: `rfmx-nr`
- source_path: `system-requirements.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr/raw/resource/enus/system-requirements.html
- document_id: `rfmx-nr`
- page_type: `leaf`
- content_type: `concept`
- source_description: RFmx NR has the following requirements: Processor—1 GHz 64-bit (x64) processor 4 GB RAM * A screen resolution of 1,024 x 768 Any supported OS, with all available critical updates and service packs * Depending on the amount of data acquired and/or processed, a larger amount of memory may be required.

### RFmx NR System Requirements

RFmx NR has the following requirements:

- Processor—1 GHz 64-bit (x64) processor
- 4 GB RAM *
- A screen resolution of 1,024 x 768
- Any supported OS, with all available critical updates and service packs

* Depending on the amount of data acquired and/or processed, a larger amount of memory
 may be required.

<!--NI_TOPIC bundle=rfmx-nr path=tdd-signal-configuration.html language=enus -->
## TOPIC 00030: TDD Signal Configuration

- bundle_id: `rfmx-nr`
- source_path: `tdd-signal-configuration.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr/raw/resource/enus/tdd-signal-configuration.html
- document_id: `rfmx-nr`
- page_type: `leaf`
- content_type: `concept`
- source_description: Sets uplink/downlink timing for TDD-based 5G NR signals, improving signal integrity and compliance testing in RFmx NR workflows. The following tables define the NR TDD signal configurations to test different base stations. 3 TDD Configurations for BS type 1-C and BS type 1-H Test Models Field Name V

### TDD Signal Configuration

Sets uplink/downlink timing for TDD-based 5G NR signals, improving signal integrity
 and compliance testing in RFmx NR workflows.

The following tables define the NR TDD signal configurations to test different base stations.

| Field Name | Value |  |  |
| --- | --- | --- | --- |
| referenceSubcarrierSpacing (kHz) | 15 | 30 | 60 |
| Periodicity (ms) for dl-UL-TransmissionPeriodicity | 5 | 5 | 5 |
| nrofDownlinkSlots | 3 | 7 | 14 |
| nrofDownlinkSymbols | 10 | 6 | 12 |
| nrofUplinkSlots | 1 | 2 | 4 |
| nrofUplinkSymbols | 2 | 4 | 8 |

| Field Name | Value |  |
| --- | --- | --- |
| referenceSubcarrierSpacing (kHz) | 60 | 120 |
| Periodicity (ms) for dl-UL-TransmissionPeriodicity | 1.25 | 1.25 |
| nrofDownlinkSlots | 3 | 7 |
| nrofDownlinkSymbols | 10 | 6 |
| nrofUplinkSlots | 1 | 2 |
| nrofUplinkSymbols | 2 | 4 |

The NR TDD signal structure over a duration of 1 periodicity, which is 5 ms, for a
 different subcarrier spacing is represented in the below diagram.

[IMAGE alt='image' src='GUID-9AE3C3D5-9568-4164-A1C3-E1421318F75A-a5.png']

To analyze the TDD downlink test model signal using RFmx NR, you
 must set the DL Test Model Duplex Scheme property to TDD. The
 default value of this property is FDD.

To analyze the NR signal with different SCH symbol allocation across slots, configure
 PDSCH/PUSCH configurations. Slots with same SCH symbol allocation can be configured
 using single PDSCH/PUSCH configuration. Resource allocation including the modulation
 scheme of SCH of each user should be same across all PDSCH/PUSCH configurations.

For example, a TDD signal with 30KHz subcarrier spacing as shown in above figure can be
 analyzed in RFmx NR by configuring two PDSCH configurations. Slot allocation and symbol
 allocation of these two PDSCH configurations are given below:

- PDSCH 0:Slot Allocation=0:6, PDSCH 0:Symbol Allocation=0:last
- PDSCH 1:Slot Allocation=7, PDSCH 1:Symbol Allocation=0:5

More information on TDD-UL-DL-Config is defined in section 6.3.2 of *3GPP TS
 38.331* specification.

Parent topic:

RFmx NR Signal Configuration Concepts

<!--NI_TOPIC bundle=rfmx-nr path=user-manual-welcome.html language=enus -->
## TOPIC 00031: RFmx NR User Manual

- bundle_id: `rfmx-nr`
- source_path: `user-manual-welcome.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr/raw/resource/enus/user-manual-welcome.html
- document_id: `rfmx-nr`
- page_type: `leaf`
- content_type: `concept`
- source_description: The RFmx NR User Manual provides detailed descriptions of the product functionality and the step by step processes for use. Looking for Something Else?For information not found in the User Manual for your product, such as specifications and API reference, browse Related Information.

### RFmx NR
 User Manual

The RFmx NR User Manual provides detailed
 descriptions of the product functionality and the step by step processes for use.

#### Looking for Something Else?

For information not found in the User Manual
 for your product, such as specifications and API reference, browse *Related
 Information*.

Related information:

- Download RFmx NR
- Interactive Activation Guide
- RFmx NR Release Notes
- RFmx User Manual
- RFmx NR LabVIEW Reference
- RFmx NR .NET API Reference
- RFmx NR C API Reference
- RFmx Instr LabVIEW Reference
- RFmx Instr .NET API Reference
- RFmx Instr C API Reference
- Discussion Forums
- NI Learning Center

<!--NI_TOPIC bundle=rfmx-nr path=valid-channel-bandwidth-and-subcarrier-spacin.html language=enus -->
## TOPIC 00032: Valid Channel Bandwidth and Subcarrier Spacing Combination

- bundle_id: `rfmx-nr`
- source_path: `valid-channel-bandwidth-and-subcarrier-spacin.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr/raw/resource/enus/valid-channel-bandwidth-and-subcarrier-spacin.html
- document_id: `rfmx-nr`
- page_type: `leaf`
- content_type: `concept`
- source_description: Valid channel bandwidth and spacing options for 5G NR enables accurate setup and testing in RFmx NR applications. Different combinations of channel bandwidth, subcarrier spacing, and operating bands are defined in Table 5.3.5-1 in the 3GPP 38.101-1 specification and 3GPP 38.101-2 specification. The

### Valid Channel Bandwidth and Subcarrier Spacing Combination

Valid channel bandwidth and spacing options for 5G NR enables accurate setup
 and testing in RFmx NR applications.

Different combinations of channel bandwidth, subcarrier spacing, and operating bands are defined
 in *Table 5.3.5-1* in the *3GPP 38.101-1* specification and *3GPP
 38.101-2* specification.

The following table lists the supported channel bandwidth and subcarrier
 spacing combination for the operating bands supported in
 RFmx.

| Frequency Range | Subcarrier Spacing (kHz) | Channel Bandwidth (MHz) |
| --- | --- | --- |
| FR1 | 15 | 3, 5, 7, 10, 15, 20, 25, 30, 35, 40, 45, 50 |
| 30, 60 | 10, 15, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 90, 100 |  |
| FR2 | 60 | 50, 100, 200 |
| 120 | 50, 100, 200, 400 |  |

Parent topic:

RFmx NR Signal Configuration Concepts
