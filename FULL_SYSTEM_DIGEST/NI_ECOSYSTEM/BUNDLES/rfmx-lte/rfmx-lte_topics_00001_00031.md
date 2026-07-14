# NI DOCUMENT BUNDLE: rfmx-lte

<!--NI_BUNDLE_CHUNK bundle=rfmx-lte start=1 end=31 -->
<!--NI_TOPIC bundle=rfmx-lte path=acquisition-bandwidth-optimization.html language=enus -->
## TOPIC 00001: Acquisition Bandwidth Optimization

- bundle_id: `rfmx-lte`
- source_path: `acquisition-bandwidth-optimization.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte/raw/resource/enus/acquisition-bandwidth-optimization.html
- document_id: `rfmx-lte`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can optimize the acquisition bandwidth for a multi-carrier measurement using the Acquisition Bandwidth Optimization Enabled property. This property places the acquisition center frequency or the local oscillator (LO) at a different position than configured. When you set the Acquisition Bandwidth

### Acquisition Bandwidth Optimization

You can optimize the acquisition bandwidth for a multi-carrier measurement using the
 Acquisition Bandwidth Optimization Enabled property. This property places the
 acquisition center frequency or the local oscillator (LO) at a different position than
 configured.

When you set the Acquisition Bandwidth Optimization Enabled property to
 False, RFmx does not optimize the acquisition bandwidth and
 the acquired bandwidth will be based on the Nyquist criterion. The value of the
 acquisition center frequency is same as the value of the center frequency that you
 configure.

When you set the Acquisition Bandwidth Optimization Enabled property to
 True, RFmx positions the acquisition center frequency to
 acquire the least bandwidth, based on the configuration and span needed for the
 measurement, which helps in reducing the amount of data that needs to be processed for
 the measurement thus, improving the speed. However, this might cause the LO to be
 positioned at a Non-DC subcarrier position, hence the measurement sensitive to LO
 leakage should have this property disabled.

The following image illustrates this property with an example.

[IMAGE alt='image' src='GUID-65717A2A-2FF1-4BB5-A49F-DA3B9AECA6A8-a5.gif']

Consider a user configuration, where two component carriers of 10 MHz and 20 MHz
 bandwidth are placed at a distance of 15 MHz between their centers. Let the center
 frequency be configured at 1 GHz. The frequency offset of CC1 is 0 Hz and of CC2 is 15
 MHz with respect to the center frequency.

If you set the Acquisition Bandwidth Optimization Enabled property to
 False, RFmx keeps the acquisition frequency same as the
 center frequency that you configure. In some cases, this leads to a higher acquisition
 bandwidth due to the asymmetric positioning of component carriers with respect to the
 center frequency as shown in the following image.

[IMAGE alt='image' src='GUID-AD9928D7-4EF4-4896-8821-9270933CEDF5-a5.gif']

If you set the Acquisition Bandwidth Optimization Enabled property to
 True, RFmx positions the acquisition frequency (LO) within
 the aggregated bandwidth to acquire the least acquisition bandwidth specified by Nyquist
 criterion as shown in the following image. In this example, the acquisition bandwidth is
 reduced to 30 MHz.

[IMAGE alt='image' src='GUID-33C2B850-D9A5-48E1-95CE-C38BB3DC3DD7-a5.gif']

#### Alternative way to achieve the Acquisition Bandwidth Optimization

When
 you set the Acquisition Bandwidth Optimization Enabled property to
 False, the span obtained is very high. When you set the
 Acquisition Bandwidth Optimization Enabled property to True,
 the span obtained is the least, but there might be an issue with the peak
 EVM.

Note

False

The
 following image illustrates the most effective method of configuring the Acquisition
 Bandwidth Optimization Enabled property for a configuration that consists of four 20
 MHz and one 10 MHz component carriers.

[IMAGE alt='image' src='GUID-74DD4AE4-E984-45F3-BBE7-7C5763D8FC98-a5.gif']

<!--NI_TOPIC bundle=rfmx-lte path=carrier-frequency-offset-definition-and-refer.html language=enus -->
## TOPIC 00002: Carrier Frequency Offset Definition and Reference Frequency

- bundle_id: `rfmx-lte`
- source_path: `carrier-frequency-offset-definition-and-refer.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte/raw/resource/enus/carrier-frequency-offset-definition-and-refer.html
- document_id: `rfmx-lte`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can configure multiple component carriers within a subblock by specifying the carrier spacing so that the carriers do not overlap. Component Carrier Spacing TypeComponent carrier spacing defines the spacing between adjacent component carriers within a subblock. If you set the Component Carrier S

### Carrier Frequency Offset Definition and Reference Frequency

You can configure multiple component carriers within a subblock by specifying the carrier
 spacing so that the carriers do not overlap.

#### Component Carrier Spacing Type

Component
 carrier spacing defines the spacing between adjacent component carriers within a
 subblock. If you set the Component Carrier Spacing Type property to
 Nominal or Minimum, the
 measurement calculates the frequency spacing between component carriers based on
 section 5.4.1A of the *3GPP TS 36.521* specification and updates the
 component carrier frequency for each of the component carriers. If you set the
 Component Carrier Spacing Type property to User, you must set
 the component carrier frequency for each of the component carriers as an offset
 relative to the center frequency of the subblock.

#### Component
 Carrier at Center Frequency

Specifies the index of the component carrier
 having its center at the user-configured center frequency. RFmx LTE uses this
 property along with the component carrier spacing type to calculate the component
 carrier frequency. This property is ignored if you set the CC Spacing Type property
 to User.

Valid values are {-1, 0, 1,... n - 1}, where
 n is the number of component carriers in this subblock. If a
 value between 0 and n - 1 is specified, the specified component
 carrier is centered on the value specified in the subblock Center Frequency
 property. If the value is -1, the component carrier frequency values for each
 carrier are calculated such that the center of aggregated carriers (subblock) lies
 at the value specified in the subblock Center Frequency property.

The
 following image is an example of configuring multiple component carriers within a
 subblock, where the configuration and implication are as follows:

- Configuration:
  - Spacing: Nominal, -1
  - Bandwidth: 20 MHz + 10 MHz
  - Center Freq: 1 GHz
- Implication:
  - CC Frequency Offsets: Located -4.95 MHz and +9.45 MHz from the center
 frequency so that 1 GHz is in the middle of the aggregated
 bandwidth
  - Center Freq: 1 GHz

[IMAGE alt='image' src='GUID-FFA483FD-7AB7-4754-93C1-9B0C9DA97A14-a5.gif']

If you set the subblock
 frequency to 1 GHz, the component carrier at center frequency to -1, and the
 bandwidth combination of {20 MHz +10 MHz} with a nominal spacing of 14.4 MHz, the
 component carriers (CC-A0 and CC-A1) are placed such that 1 GHz becomes the center
 of the aggregated carriers.

The CC-A0 carrier offset, with respect to 1 GHz,
 is -4.95 MHz, and the CC-A1 carrier offset, with respect to 1 GHz, is +9.45 MHz,
 while keeping their nominal spacing unchanged.

The following image is another
 example of configuring multiple component carriers within a subblock, where the
 configuration and implication are as follows:

- Configuration:
  - Spacing: Nominal, 1
  - Bandwidth: 20 MHz + 10 MHz
  - Center Freq: 1 GHz

- Implication:
  - CC Frequency Offsets: Located -14.4 MHz and 0 from center frequency
  - Center Freq: 1 GHz

[IMAGE alt='image' src='GUID-0C966D99-C67F-4D4F-84DB-0E58AC947F90-a5.gif']

If you set the center frequency
 to 1 GHz, the component carrier at center frequency to 1, and the bandwidth
 combination is {20 MHz +10 MHz} with nominal spacing of 14.4 MHz.

The second
 component carrier (CC-A1) is centered at 1 GHz and the first component carrier
 (CC-A0) is nominally spaced in the left side from 1 GHz.

The component carrier
 frequencies or frequency offsets for CC-A0 and CC-A1 from 1 GHz are considered as
 -14.4 MHz and 0 while their relative spacing is unchanged.

<!--NI_TOPIC bundle=rfmx-lte path=carrier-integration-bandwidth.html language=enus -->
## TOPIC 00003: Carrier Integration Bandwidth

- bundle_id: `rfmx-lte`
- source_path: `carrier-integration-bandwidth.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte/raw/resource/enus/carrier-integration-bandwidth.html
- document_id: `rfmx-lte`
- page_type: `leaf`
- content_type: `concept`
- source_description: Carrier integration bandwidth is the measurement bandwidth defined by the 3GPP specification. The assigned LTE carrier is filtered with a rectangular filter with this integration bandwidth and is used to calculate channel power. Single CarrierFor a single carrier, the following table specifies the i

### Carrier Integration Bandwidth

Carrier integration bandwidth is the measurement bandwidth defined by the 3GPP
 specification. The assigned LTE carrier is filtered with a rectangular filter with this
 integration bandwidth and is used to calculate channel power.

#### Single Carrier

For a single carrier, the following table specifies the
 integration or measurement bandwidths.

| Channel Bandwidth (MHz) | LTE Measurement Bandwidth (MHz) |
| --- | --- |
| 1.4 | 1.08 |
| 3.0 | 2.7 |
| 5 | 4.5 |
| 10 | 9 |
| 15 | 13.5 |
| 20 | 18 |

#### Carrier Aggregation

In a carrier aggregation scenario, the
 inter-component carrier is included in the aggregated integration bandwidth. Hence,
 the aggregated integration bandwidth of a subblock is the sum of all component
 carriers within the subblock and the inter-carrier gaps.

In the following
 figure, two component carriers are configured within a subblock having bandwidths of
 20 MHz and 10 MHz respectively. While the integration bandwidths of the individual
 carrier are 18 MHz and 9 MHz, respectively, the aggregated integration bandwidth
 (CA_IBW) is 27.9 MHz, as aggregated integration bandwidth includes the gap between the component
 carriers.

The CA_IBW is used as a measurement bandwidth to calculate subblock
 power in any measurement.

[IMAGE alt='image' src='GUID-0CEA87D3-C199-4A84-958A-F71A43EAFFD0-a5.gif']

<!--NI_TOPIC bundle=rfmx-lte path=channel-spacing.html language=enus -->
## TOPIC 00004: Channel Spacing

- bundle_id: `rfmx-lte`
- source_path: `channel-spacing.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte/raw/resource/enus/channel-spacing.html
- document_id: `rfmx-lte`
- page_type: `leaf`
- content_type: `concept`
- source_description: Channel spacing is the distance between center frequencies of two adjacent component carriers for intra-band contiguous carrier aggregation. The channel spacing between the center frequencies of contiguously aggregated component carriers is a multiple of 300 KHz, in order to be compatible with the 1

### Channel Spacing

Channel spacing is the distance between center frequencies of two adjacent component
 carriers for intra-band contiguous carrier aggregation.

The channel spacing between the center frequencies of contiguously aggregated component
 carriers is a multiple of 300 KHz, in order to be compatible with the 100 KHz frequency
 raster of LTE Rel-8 and to preserve orthogonality of the subcarriers with 15 KHz
 spacing.

For more information about channel spacing, refer to section 5.4.1A of the *3GPP TS
 36.521-1* specification.

#### Nominal Channel Spacing

Nominal channel spacing is the maximum allowed spacing between the center frequencies
 of two adjacent component carriers for intra-band contiguous carrier aggregation.
 Set the Component Carrier Spacing Type property to Nominal to
 configure nominal channel spacing.

[IMAGE alt='image' src='GUID-DDA0D702-FDAE-4D4F-94AB-45969C00372A-a5.gif']

where
 BW<sub>Channel(1)</sub> and BW<sub>Channel(2)</sub> are the channel bandwidths,
 in MHz, of the two adjacent E-UTRA component carriers.

For example, in a 20
 MHz + 20 MHz intra-band contiguous carrier aggregation scenario, the nominal spacing
 is 19.8 MHz.

Refer to section 5.4.1A of the *3GPP* specification
 for more information about nominal channel spacing.

The following table
 denotes the nominal channel spacing between adjacent carriers for specified channel
 bandwidths.

| Channel Bandwidth (MHz) | Nominal Channel Spacing Between Adjacent Carriers (MHz) |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| 1.4 | 3.0 | 5 | 10 | 15 | 20 |  |
| 1.4 | 1.20 | 2.10 | 3.00 | 5.10 | 7.50 | 9.60 |
| 3 | — | 3.00 | 3.90 | 6.00 | 8.40 | 10.50 |
| 5 | — | — | 4.80 | 7.20 | 9.30 | 11.70 |
| 10 | — | — | — | 9.90 | 12.00 | 14.40 |
| 15 | — | — | — | — | 15.00 | 17.10 |
| 20 | — | — | — | — | — | 19.80 |

#### Minimum Channel Spacing

Minimum channel spacing is the smallest possible
 value of channel spacing. Minimum channel spacing ensures that the transmission
 bandwidth configurations do not overlap when setting the channel spacing to a
 multiple of 300 KHz. To configure minimum channel spacing, set the Component Carrier
 Spacing Type property to Minimum.

Refer to table
 5.7.1-2 of the *3GPP TS 36.808* specification for more information about
 minimum channel spacing.

The following table denotes the minimum channel
 spacing between adjacent carriers for specified channel bandwidths.

| Channel Bandwidth (MHz) | Minimum Channel Spacing between Adjacent Carriers (MHz) |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| 1.4 | 3.0 | 5 | 10 | 15 | 20 |  |
| 1.4 | 1.20 | 2.10 | 3.00 | 5.10 | 7.50 | 9.60 |
| 3 | — | 3.00 | 3.90 | 6.00 | 8.40 | 10.50 |
| 5 | — | — | 4.80 | 6.90 | 9.30 | 11.40 |
| 10 | — | — | — | 9.30 | 11.40 | 13.80 |
| 15 | — | — | — | — | 13.80 | 15.90 |
| 20 | — | — | — | — | — | 18.30 |

#### User-Specific Channel Spacing

You can configure the spacing type between
 component carriers by setting the Component Carrier Spacing Type property to
 User and configuring the component carrier frequency for
 each component carrier.

<!--NI_TOPIC bundle=rfmx-lte path=enhanced-machine-type-communication.html language=enus -->
## TOPIC 00005: Enhanced Machine Type Communication

- bundle_id: `rfmx-lte`
- source_path: `enhanced-machine-type-communication.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte/raw/resource/enus/enhanced-machine-type-communication.html
- document_id: `rfmx-lte`
- page_type: `leaf`
- content_type: `concept`
- source_description: Enhanced machine type communication (eMTC) or LTE Cat-M1 is a low power wide area (LPWA) technology introduced in the Release 13 LTE 3GPP specification. eMTC supports low complexity IoT devices, which leverages the existing LTE network infrastructure. eMTC is used in IoT devices that require higher

### Enhanced Machine Type Communication

Enhanced machine type communication (eMTC) or LTE Cat-M1 is a low power wide area (LPWA)
 technology introduced in the *Release 13 LTE 3GPP* specification. eMTC
 supports low complexity IoT devices, which leverages the existing LTE network
 infrastructure. eMTC is used in IoT devices that require higher data rate than that
 supported by NB-IoT devices. eMTC has a reduced bandwidth compared to LTE but has an
 extended coverage.

eMTC is referred as BL/CE, where BL is bandwidth reduced low complexity and CE is
 coverage enhancement.

eMTC supports half-duplex frequency division duplex (HD-FDD), frequency division duplex
 (FDD), and time division duplex (TDD) operations.

eMTC supports two transmission modes - Cat-M1 and Cat-M2. Cat-M1 eMTC uses 1.08 MHz of
 integration bandwidth (6 resource blocks or narrow band) for transmission and reception,
 while Cat-M2 eMTC uses 5 MHz of integration bandwidth (24 resource blocks or wideband)
 for transmission and reception.

#### Narrow Band Retuning or Frequency
 Hopping

Six consecutive non-overlapping resource blocks constitute a
 narrow band. Each LTE bandwidth is divided into a set of pre-defined narrow bands as
 per section 5.2.4 of *3GPP 36.211* specification.

For channel
 bandwidths other than 1.4 MHz, the transmission can be retuned from one narrow band
 to another at the subframe boundary. This retuning operation called frequency
 hopping or narrow band retuning requires sufficient guard symbols to be
 allocated.

Narrow band hopping interval defines the periodicity of frequency
 hopping. The frequency separation between the narrow bands used before and after
 retuning is called narrow band hopping offset. Hopping offset and hopping interval
 is specified by higher layers.

Wideband Retuning or Frequency
 Hopping

Four consecutive non-overlapping narrow bands constitute a wideband as
 defined in section 5.2.4 of 3GPP 36.211 specification. For 1.4
 MHz and 3 MHz, wideband is composed of all available narrow bands (1 and 2
 respectively).

For channel bandwidths higher than 5 MHz, the transmission can
 be retuned from one wideband to another at the subframe boundary. This retuning
 operation called frequency hopping or wideband retuning requires sufficient guard
 symbols to be allocated.

#### Guard Symbols

During frequency hopping, the local oscillator (LO) of
 transmitter will retune to a different frequency. The LO requires some time to
 settle to the new frequency, hence some empty symbols are allocated. These symbols
 are referred to as guard symbols. In case of Cat-M2, guard symbols are allocated
 only if the hopping happens from one wideband to another. Number of guard symbols
 for different conditions are defined in section 5.2.5 of *3GPP 36.211*
 specification.

[IMAGE alt='image' src='GUID-1064A8D0-58FA-4B0F-9593-2B6468964101-a5.gif']

Note

- In RFmx LTE, when you set the eMTC Analysis Enabled property to
 True , the measurement auto-detects the active
 subframes (avoiding empty slots in HD-FDD operation), and frequency
 allocation of each subframe along with guard symbols at hopping boundary.
 This control is applicable for both Cat-M1 and Cat-M2.
- In RFmx LTE, carrier aggregation of more than one eMTC carrier is not
 supported.

<!--NI_TOPIC bundle=rfmx-lte path=faqs.html language=enus -->
## TOPIC 00006: FAQs

- bundle_id: `rfmx-lte`
- source_path: `faqs.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte/raw/resource/enus/faqs.html
- document_id: `rfmx-lte`
- page_type: `leaf`
- content_type: `concept`
- source_description: Answers common questions about RFmx LTE features and measurements. Why do spectrum traces have more variation after noise compensation as compared to the spectrum without noise compensation?Example: assume that without noise compensation, the measured noise power is 5E–6 ± 0.5E–6 watts. The correspo

### FAQs

Answers common questions about RFmx LTE features and
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

<!--NI_TOPIC bundle=rfmx-lte path=internet-of-things-overview.html language=enus -->
## TOPIC 00007: Internet of Things Overview

- bundle_id: `rfmx-lte`
- source_path: `internet-of-things-overview.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte/raw/resource/enus/internet-of-things-overview.html
- document_id: `rfmx-lte`
- page_type: `leaf`
- content_type: `concept`
- source_description: Internet of things (IoT) is a system of interconnected computing devices embedded in everyday physical objects. IoT connectivity standards enable these devices to send and receive data via existing internet infrastructure. The primary end-user requirements for these devices are low cost and reduced

### Internet of Things Overview

Internet of things (IoT) is a system of interconnected computing devices embedded in
 everyday physical objects. IoT connectivity standards enable these devices to send and
 receive data via existing internet infrastructure.

The primary end-user requirements for these devices are low cost and reduced power
 consumption. Personal Area Network (PAN) and Wireless Local Area Network (WLAN)
 technologies meet the cost and power requirements for IoT connectivity. However, these
 technologies have less coverage. Wide coverage is one of the key requirements for many
 emerging IoT use cases. The existing cellular standards have wide coverage but because
 of the complexity, results in higher cost devices and more power consumption.

To ensure IoT devices cost less, consume low power and have wide coverage; low power wide
 area (LPWA) technologies like narrowband internet of things (NB-IoT) and enhanced
 machine type communication (eMTC) were developed by 3GPP. While eMTC was developed on
 top of existing LTE infrastructure, NB-IoT was developed as a new radio interface with
 some similarities to LTE.

In RFmx LTE, we are supporting both eMTC (Cat-M1 and Cat-M2) and NB-IoT (Cat-M1 and
 Cat-M2) .

<!--NI_TOPIC bundle=rfmx-lte path=licensed-assisted-access.html language=enus -->
## TOPIC 00008: Licensed Assisted Access

- bundle_id: `rfmx-lte`
- source_path: `licensed-assisted-access.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte/raw/resource/enus/licensed-assisted-access.html
- document_id: `rfmx-lte`
- page_type: `leaf`
- content_type: `concept`
- source_description: Licensed assisted access (LAA) is introduced in release 13 of 3GPP specification to enable the operation of an LTE system in an unlicensed band. LAA combines an LTE carrier in the unlicensed spectrum with an LTE carrier in the licensed band using carrier aggregation. Frame structure type 3 is the ne

### Licensed Assisted Access

Licensed assisted access (LAA) is introduced in release 13 of 3GPP specification to
 enable the operation of an LTE system in an unlicensed band. LAA combines an LTE carrier
 in the unlicensed spectrum with an LTE carrier in the licensed band using carrier
 aggregation. Frame structure type 3 is the new type of frame structure defined by 3GPP
 specification for LAA.

#### Frame structure Type 3

Frame structure type 3 is applicable to LAA
 unlicensed carrier with normal cyclic prefix only. Each radio frame is 10 ms long
 and consists of 10 subframes of length 1 ms. Any of these 10 subframes can be used
 for uplink/downlink transmission or can be empty. LAA transmission can start and end
 at any subframe and can consist of one or more consecutive subframes in the
 burst.

[IMAGE alt='image' src='GUID-68FA49F7-6A02-4E93-A637-28ECD72D26FC-a5.gif']

#### Partial Subframes

Partial subframes are introduced by 3GPP specification,
 as a part of frame structure type 3, to cater to the needs of listen before talk
 (LBT) principles and for efficient use of unlicensed spectrum by LAA.

Partial
 subframes in uplink

- LAA uplink burst gets transmitted either from the start of the 0 th 
 symbol or from the start of the 1 st symbol in a subframe. The
 transmission can also start between the 0 th and the 1 st 
 symbol, as defined in section 5.6 of 3GPP 36.211 
 specification. Thus, the 0 th symbol in the first subframe of an LAA
 uplink burst can be partially filled, completely filled, or completely
 empty.
- LAA uplink transmission can end either at the 12 th or 13 th 
 OFDM symbol in a subframe as mentioned in sections 5.3.3.1.1A and 5.3.3.1.1B of
 3GPP 36.212 specification. Therefore, the last subframe
 in an LAA uplink transmission can be completely filled with 14 OFDM symbols or
 can be partially filled with 13 OFDM symbols.

[IMAGE alt='image' src='GUID-DE8EA909-8687-4A89-B9B2-99D2F8119ED3-a5.gif']

#### Partial subframes in downlink

- LAA downlink transmission can start from 0th OFDM symbol (Subframe boundary) or
 from 7 th OFDM symbol (Second Slot Starting Position) of a subframe.
 Refer to section 13A of 3GPP 36.213 specification for more
 information.
- LAA downlink transmission can either end at the subframe boundary or at any of
 the DwPTS symbols. Therefore, the last subframe can be completely occupied with
 14 OFDM symbols or can consist of any of DwPTS duration symbols i.e. 3, 6, 9,
 10, 11, or 12 OFDM symbols. Refer to section 4.3 of 3GPP
 36.211 specification for more information.

[IMAGE alt='image' src='GUID-C0C8F501-A753-4A07-AD84-5C032D217C79-a5.gif']

Note

- In RFmx LTE, LAA follows frame structure type 3 and measures only one burst
 per measurement interval.
- In RFmx LTE, carrier aggregation of multiple LAA carriers is supported while
 carrier aggregation of LAA with FDD/TDD carrier is not supported.
- In RFmx LTE, different LAA configurations across carriers are not supported
 for power trigger. NI recommends to use same LAA configuration for all
 configured carriers irrespective of trigger types.
- In RFmx LTE, for uplink, EVM's for the 0 th symbol of the first
 subframe in the LAA burst is not measured if it is partially occupied.

<!--NI_TOPIC bundle=rfmx-lte path=lte-channel-power.html language=enus -->
## TOPIC 00009: LTE Channel Power

- bundle_id: `rfmx-lte`
- source_path: `lte-channel-power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte/raw/resource/enus/lte-channel-power.html
- document_id: `rfmx-lte`
- page_type: `leaf`
- content_type: `concept`
- source_description: The LTE channel power (CHP) measurement uses the configurations specified by 3GPP TS 36.521-1 specification. This topic explains the configurations used by the RFmx LTE CHP measurement. The period of measurement for LTE CHP is at least the continuous duration of one sub-frame (1 ms) as defined in 3G

### LTE Channel Power

The LTE channel power (CHP) measurement uses the configurations specified by *3GPP
 TS 36.521-1* specification. This topic explains the configurations used by the
 RFmx LTE CHP measurement.

The period of measurement for LTE CHP is at least the continuous duration of one
 sub-frame (1 ms) as defined in *3GPP TS 36.521-1* specification. Hence, when
 you set the Sweep Time Auto property to True, the sweep time is
 set to 1 ms for the LTE CHP measurement.

Refer to the CHP Overview topic for a general overview of CHP measurement concepts.

- Single carrier —The power is measured over the integration
 bandwidth of the carrier.
- Intra-band contiguous carrier aggregation —The power is
 measured over the integration bandwidth of the aggregated carrier and includes the
 inter-carrier gaps within the subblocks.
- Intra-band noncontiguous carrier aggregation —The power is the
 sum of all powers.

#### CHP
 Integration Bandwidth Type

CHP integration bandwidth type specifies the
 integration bandwidth type used to measure the power of the acquired signal.
 Integration bandwidth is the frequency span over which power in each frequency bin
 is added to measure the total power in that span.

When you set the CHP IBW
 Type property to Signal Bandwidth, the IBW excludes the guard
 bands at the edges of the carrier or subblock. Signal bandwidth is used to calculate
 minimum output power as given in section 6.3.2 of *3GPP TS 36.521-1*
 specification.

Channel
 Bandwidth

3GPP TS 36.521-1

[IMAGE alt='image' src='GUID-95CB17B0-1D3E-471A-96A7-5815E4823D82-a5.gif']

#### NB-IoT Channel Power

To select Narrowband Internet of Things (NB-IoT)
 CHP, you can set CC Bandwidth property to 200.0 k in RFmx LTE
 CHP measurement.

The period of measurement for NB-IoT ACP is at least one
 sub-frame (1 ms) for 15 kHz channel spacing and at least a 2 ms slot (excluding the
 2304Ts gap when user equipment (UE) is not transmitting) for 3.75 kHz channel
 spacing, as defined in section 6.6.2.3F.4 of *3GPP TS 36.521-1*
 specification. Hence, when you set the Sweep Time Auto property to true, the sweep
 time is set accordingly for the NB-IoT CHP measurement.

For NB-IoT CHP, signal
 bandwidth is used to calculate minimum output power as given in section 6.3.2F of
 *3GPP TS 36.521-1* specification.

For NB-IoT CHP, channel
 bandwidth is used to calculate maximum output power as given in section 6.2.2F of
 *3GPP TS 36.521-1* specification.

Related information:

- Channel Power

<!--NI_TOPIC bundle=rfmx-lte path=lte-channels-and-carrier-aggregation.html language=enus -->
## TOPIC 00010: LTE Channels and Carrier Aggregation

- bundle_id: `rfmx-lte`
- source_path: `lte-channels-and-carrier-aggregation.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte/raw/resource/enus/lte-channels-and-carrier-aggregation.html
- document_id: `rfmx-lte`
- page_type: `leaf`
- content_type: `concept`
- source_description: Carrier channels are transmitted by the user equipment (UE) when the measurement is performed. You can configure single or multiple LTE (E-UTRA) carrier channels. Single CarrierLTE channel bandwidth is the RF bandwidth supporting a single E-UTRA RF carrier with the transmission bandwidth configured

### LTE Channels and Carrier Aggregation

Carrier channels are transmitted by the user equipment (UE) when the measurement is performed. You can
 configure single or multiple LTE (E-UTRA) carrier channels.

#### Single Carrier

LTE channel bandwidth is the
 RF bandwidth supporting a single E-UTRA RF carrier with the transmission bandwidth
 configured in the uplink. The channel bandwidth is used as a reference for transmitter
 and receiver RF requirements. This bandwidth includes the guard band.

LTE
 measurement bandwidth is the highest transmission bandwidth allowed for uplink in a
 given channel bandwidth, which is measured in megahertz (MHz). Measurement bandwidths
 for all LTE channel bandwidths are specified in the following table.

| Channel Bandwidth (MHz) | LTE Measurement Bandwidth (MHz) |
| --- | --- |
| 1.4 | 1.08 |
| 3.0 | 2.7 |
| 5 | 4.5 |
| 10 | 9 |
| 15 | 13.5 |
| 20 | 18 |

#### Carrier Aggregation

Carrier aggregation is
 one of the main feature in LTE-Advanced as defined by the 3GPP
 specification. Carrier aggregation enables multiple carriers to be combined to support
 wider transmission bandwidths, thereby increasing the data rate.

For more
 information about carrier aggregation, refer to section 5.4.1A and 5.4.2A of the
 *3GPP TS 36.521-1* specification.

You can configure multiple
 carrier channels by specifying the carrier offsets. You can configure contiguous
 and noncontiguous carrier aggregation by configuring LTE carrier spacing.

Carrier Bandwidths

To maintain backward compatibility, carrier
 aggregation is performed with release 8 carrier bandwidths, for example, 1.4 MHz, 3 MHz,
 5 MHz, 10 MHz, 15 MHz, and 20 MHz. Each aggregated carrier is referred to as a component
 carrier (CC).

#### Types
 of Carrier Aggregation

- Intra-band Contiguous—Component carriers are placed side-by-side within the same
 operating frequency band. This type is supported in RFmx LTE.
- Intra-band Noncontiguous—Component carriers are placed with some gap within the same
 operating frequency band. This type is supported in RFmx LTE.
- Inter-band Noncontiguous—One or more component carriers are placed in different
 operating frequency bands. This type is not supported in RFmx LTE.

[IMAGE alt='image' src='GUID-AD35C81F-3EB5-42ED-891E-27D720AB9C38-a5.gif']

<!--NI_TOPIC bundle=rfmx-lte path=lte-downlink-adjacent-channel-power.html language=enus -->
## TOPIC 00011: LTE Downlink Adjacent Channel Power

- bundle_id: `rfmx-lte`
- source_path: `lte-downlink-adjacent-channel-power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte/raw/resource/enus/lte-downlink-adjacent-channel-power.html
- document_id: `rfmx-lte`
- page_type: `leaf`
- content_type: `concept`
- source_description: This topic explains the following configurations used by the RFmx LTE downlink adjacent channel power (ACP) measurement. The RFmx LTE ACP measurement uses the configurations as specified by the 3GPP TS 36.141 specification. Refer to the ACP Overview topic for a general overview of single and multica

### LTE Downlink Adjacent Channel Power

This topic explains the following configurations used by the RFmx LTE downlink adjacent
 channel power (ACP) measurement.

The RFmx LTE ACP measurement uses the configurations as specified by the *3GPP TS
 36.141* specification.

Refer to the ACP Overview topic for a general overview of single and multicarrier ACP
 measurement concepts.

#### Offset Channels

LTE downlink ACP
 measurement is performed in frequency domain across LTE signal in the carrier
 channel and adjacent channels called the offset channels. The *3GPP TS
 36.141* specification defines two types of offset channels for LTE;
 universal terrestrial radio access (UTRA) and evolved universal terrestrial radio
 access (E-UTRA). The UTRA channels are WCDMA or TDMA/CDMA channels, and the E-UTRA
 channels are LTE channels.

#### Types of Measurements

The LTE downlink
 ACP measurements can be categorized into following three types:

- Single carrier ACP
- Intra-band contiguous carrier aggregation ACP
- Non-contiguous carrier aggregation ACP

Note

#### Single Carrier ACP

The types of
 single-carrier ACP are E-UTRA Offset Channels for Single Carrier and UTRA Offset
 Channels for Single Carrier.

#### E-UTRA Offset Channels for Single
 Carrier

This measurement provides the adjacent channel leakage power ratio
 (ACLR) values to gauge the extent of contamination from the LTE signal in adjacent
 channels. The E-UTRA ACLR (E-UTR<sub>ACLR</sub>) is the ratio of the filtered
 average power centered on an adjacent E-UTRA channel to the filtered average power
 centered on the carrier channel with channel spacing and measurement bandwidths as
 shown in the table below.

Table 1: The following table shows the configuration of
 E-UTRA offset channels and their measurement bandwidths for LTE configurations. For
 more information, refer to section 6.6.2-1 of *3GPP 36.141*
 specification.

|  | Offset Frequency (from the Center of the Carrier to the Center of the Offset Channel) | Channel Measurement Bandwidth |
| --- | --- | --- |
| E-UTRA 1 | BWChannel | Transmission Bandwidth of E-UTRA carrier |
| E-UTRA 2 | 2 * BWChannel | Transmission Bandwidth of E-UTRA carrier |

Table 2: The following table gives the transmission bandwidth of LTE
 carriers, where transmission bandwidth of the carrier is used as measurement
 bandwidth while measuring the E-UTRA<sub>ACLR</sub>. The power of the E-UTRA
 adjacent channel is measured with a rectangular filter.

| LTE E-UTRA Carrier | Transmission Bandwidth |
| --- | --- |
| 1.4 MHz | 1.08 MHz |
| 3 MHz | 2.7 MHz |
| 5 MHz | 4.5 MHz |
| 10 MHz | 9 MHz |
| 15 MHz | 13.5 MHz |
| 20 MHz | 18 MHz |

#### UTRA Offset Channels for Single
 Carrier

The UTRA ACLR (UTRA<sub>ACLR</sub>) is the ratio of the filtered
 average power centered on an adjacent UTRA channel to the filtered average power
 centered on the carrier channel with channel spacing and measurement bandwidths as
 specified in Tables 3, 4, and 5. For LTE-FDD, the measurement measures two UTRA
 adjacent channels as specified in Table 3. For LTE-TDD with channel bandwidths 1.4
 MHz and 3 MHz, the measurement measures two UTRA adjacent channels as specified in
 Table 4. For LTE-TDD with channel bandwidths 3 MHz, 5 MHz, 10 MHz, 15 MHz, and 20
 MHz, the measurement measures six UTRA adjacent channels as specified in Table 5.
 When base station is operating in Band 46, only the E-UTRA offset channels are
 measured and UTRA offset channels are not measured as specified by the *3GPP
 TS 36.141-1* specification.

The UTRA channel power is measured
 with a RRC bandwidth filter with a roll-off factor α = 0.22. For LTE-FDD, the UTRA
 offset channels are assumed to be WCDMA channels. For LTE-TDD, the UTRA offset
 channels are assumed to be TDMA/CDMA channels. The position of offsets in frequency
 with respect to the center of the LTE carrier (E-UTRA) and their measurement
 bandwidths are specified in the following tables.

Table 3: The following table
 gives the configurations of UTRA offset channels for BS operating in FDD. For more
 information refer to section 6.6.2-1 of *3GPP 36.141*
 specification.

|  | Offset Frequency (from the Center of the Carrier to the Center of the Offset Channel) | Channel Measurement Bandwidth |
| --- | --- | --- |
| UTRA 1 | BWChannel/2 + 2.5 MHz | 3.84 MHz |
| UTRA 2 | BWChannel/2 + 7.5 MHz | 3.84 MHz |

Table 4: The following table gives the configurations of UTRA offset channels
 for BS operating in TDD and channel bandwidths 1.4 MHz and 3 MHz. For more
 information refer to section 6.6.2-2 of *3GPP 36.141*
 specification.

|  | Center Frequency Offset | Channel Measurement Bandwidth |
| --- | --- | --- |
| UTRA 1 | BWChannel/2 + 0.8 MHz | 1.28 MHz |
| UTRA 2 | BWChannel/2 + 2.4 MHz | 1.28 MHz |

Table 5: The following table gives the configurations of UTRA offset channels
 for BS operating in TDD and channel bandwidths 5 MHz and 10 MHz, and 15 MHz and 20
 MHz. For more information refer to the section 6.6.2-2 of *3GPP
 36.141* specification.

|  | Center Frequency Offset | Channel Measurement Bandwidth |
| --- | --- | --- |
| UTRA 1 | BWChannel/2 + 0.8 MHz | 1.28 MHz |
| UTRA 2 | BWChannel/2 + 2.4 MHz | 1.28 MHz |
| UTRA 3 | BWChannel/2 + 2.5 MHz | 3.84 MHz |
| UTRA 4 | BWChannel/2 + 7.5 MHz | 3.84 MHz |
| UTRA 5 | BWChannel/2 + 5 MHz | 7.68 MHz |
| UTRA 6 | BWChannel/2 + 15 MHz | 7.68 MHz |

#### Intraband Contiguous Carrier Aggregation
 ACP

In intra-band contiguous carrier aggregation ACP, the adjacent offset
 channels are placed relative to the center of the closet E-UTRA
 carrier.

#### E-UTRA Offset Channels for Contiguous Carrier
 Aggregation

The E-UTRA ACLR is the ratio of the filtered average power
 centered on an adjacent E-UTRA channel to the filtered average power centered on the
 closest E-UTRA carrier. The E-UTRA bandwidth of closest E-UTRA carrier is used as
 the measurement bandwidth for measuring E-UTRA ACLR. The power of closest E-UTRA
 carrier is used as power reference for measuring E-UTRA ACLR. The E-UTRA offset
 channels are placed relative to the center of closest E-UTRA carrier of a subblock.
 The center of successive E-UTRA offset channels is (m *
 E-UTRA bandwidth of closest carrier) away from the center of
 closest E-UTRA carrier. When the base station is operating in Band 46, only the
 E-UTRA offset channels are measured and the UTRA offset channels are not measured as
 specified by the *3GPP TS 36.141-1* specification. The power of
 this E-UTRA adjacent channel is measured with a rectangular filter.

#### UTRA
 Offset Channels for Contiguous Carrier Aggregation

The UTRA ACLR
 (UTRA<sub>ACLR</sub>) is the ratio of the filtered average power centered on an
 adjacent UTRA channel to the filtered average power centered on the closest E-UTRA
 carrier of the subblock. The power of closest E-UTRA carrier of a subblock is used
 as power reference for measuring UTRA ACLR. The UTRA offset channels are placed
 relative to center of the closest E-UTRA carrier of a subblock. The power of this
 E-UTRA adjacent channel is measured with a rectangular filter.

For example,
 three LTE component carriers (C0 = 10 MHz, C1 = 5 MHz and C2 = 20 MHz) are
 configured within a subblock as shown in the following figure. In this scenario, the
 E-UTRA offset channels (E1:C2 and E2:C2) are positioned relative to the center of
 component carrier C2. The E-UTRA offset channels (E1:C0 and E2:C0) are positioned
 relative to the center of the component carrier C0. The UTRA offset channels (U1:C2
 and U2:C2) are positioned relative to the center of the component carrier C2. The
 UTRA offset channels (U1:C0 and U2:C0) are positioned relative to the center of the
 component carrier C0.

[IMAGE alt='image' src='GUID-36A63B4D-93B4-4DFC-B7A3-3A7C5138FC81-a5.gif']

#### Non-contiguous Carrier Aggregation ACP

In intra-band or inter-band
 non-contiguous carrier aggregation ACP, the UTRA and the E-UTRA offset channels to
 the left and right of each subblock are measured. Here, the offset channels between
 two subblocks are called the inner offset channels and remaining offset channels are
 called the outer offset channels. The outer offset channels are configured similarly
 to contiguous carrier aggregation ACP.

The following image shows a typical
 carrier channel and offset channel configuration for the LTE advanced non-contiguous
 configuration with two subblocks each comprising of two component carriers. The
 inner offset channels (I1:S0:C1 and I2:S0:C1) are positioned relative to the center
 of component carrier S0:C1. Inner offset channels (I1:S1:C0 and I2:S1:C0) are
 positioned relative to the center of component carrier S1:C0. The outer E-UTRA
 offset channels and the UTRA offset channels are positioned relative to the center
 of component carrier S0:C0 and outer E-UTRA offset channels and UTRA offset channels
 are positioned relative to the center of component carrier S1:C1

[IMAGE alt='image' src='GUID-1608DC21-B0BC-4EB0-830C-731799B36C4B-a5.gif']

#### Inner Offset Channels for Intra-band Non-contiguous
 Carrier Aggregation

#### Cumulative Adjacent Channel Leakage Power
 Ratio

When a subblock gap is small, the carriers located in both the
 subblocks contribute to the leakage in the gap region. To measure this leakage a new
 concept called cumulative adjacent channel leakage power ratio (CACLR) is
 introduced.

As mentioned in the section 6.6.2.2 of *3GPP TS
 36.141* specification, the CACLR in a subblock gap or inter RF
 bandwidth gap is defined as A / B. Where,
 A is the sum of the filtered mean power centered on the
 assigned channel frequencies for the two carriers adjacent to each side of the
 subblock gap or inter RF bandwidth gap, and B is the filtered
 mean power centered on a frequency channel adjacent to one of the respective
 subblock edges or RF bandwidth edges.

#### Base
 station operating in bands other than Band 46:

For LTE-FDD, the inner
 offset channels are assumed to be UTRA offset channels of bandwidth 5 MHz as
 specified in the Table 6.6.2-5 of *3GPP TS 36.141* specification.
 For LTE-TDD, the inner offset channels are assumed to be E-UTRA offset channels of
 bandwidth 5 MHz as specified in the Table 6.6.2-6 of *3GPP TS
 36.141* specification. Inner offset channels between the two subblocks
 returns ACLR and CALR results based on subblock gap as tabulated below.

The
 configurations of inner offset channels for BS operating in FDD are given in the
 following table.

| Subblock Gap or Inter-band Gap (Wgap) | 1st Inner Offset Channel | 2nd Inner Offset Channel |
| --- | --- | --- |
| Wgap < 5 MHz | NaN | NaN |
| 5 MHz ≤ Wgap ≤ 10 MHz | CACLR | NaN |
| 10 MHz < Wgap < 15 MHz | CACLR | CACLR |
| 15 MHz ≤ Wgap < 20 MHz | ACLR | CACLR |
| 20 MHz ≤ Wgap | ACLR | ACLR |

The following image depicts all possible cases with inner offset, where SB-A
 and SB-B are two subblocks. Inner offset channel (I1:A, I2:A) are defined relative
 to subblock A. Inner offset channel (I1:B, I2:B) are defined relative to subblock B.
 The outer offset channel (O1:A, O2:A,) are defined relative to subblock A. The outer
 offset channel (O1:B, O2:B) are defined relative to subblock B.

[IMAGE alt='image' src='GUID-3E742E2F-E04A-492E-BEEF-0D1A6616936B-a5.gif']

#### Base
 station operating in Band 46

Band 46 supports only time division duplex
 (TDD). In Band 46, the inner offset channels are assumed to be E- UTRA offset
 channels of bandwidth 20 MHz as specified in the Table 6.6.2-6a of *3GPP TS
 36.141*. The inner offset channels between the two subblocks returns
 ACLR and CALR results based on subblock gap as tabulated below.

The
 configurations of inner offset channels for BS operating in Band 46 and FDD are
 given in the following table.

| Subblock Gap or Inter-band Gap (Wgap) | 1st Inner Offset Channel | 2nd Inner Offset Channel |
| --- | --- | --- |
| Wgap < 20 MHz | NaN | NaN |
| 20 MHz ≤ Wgap ≤ 40 MHz | CACLR | NaN |
| 40 MHz < Wgap < 60 MHz | CACLR | CACLR |
| 60 MHz ≤ Wgap < 80 MHz | ACLR | CACLR |
| 80 MHz ≤ Wgap | ACLR | ACLR |

The following image depicts all possible cases with inner offset, where SB-A
 and SB-B are two subblocks. The inner offset channel (I1:A, I2:A) are defined
 relative to subblock A. The inner offset channel (I1:B, I2:B) are defined relative
 to subblock B. The E-UTRA offset channel (E1:A, E2:A) are defined relative to
 subblock A. The E-UTRA offset channel (E1:B, E2:B) are defined relative to subblock
 B.

[IMAGE alt='image' src='GUID-6C03BACD-A4D6-493B-A37E-F95C0419D488-a5.gif']

Related information:

- Adjacent Channel Power Overview

<!--NI_TOPIC bundle=rfmx-lte path=lte-downlink-spectral-emission-mask.html language=enus -->
## TOPIC 00012: LTE Downlink Spectral Emission Mask

- bundle_id: `rfmx-lte`
- source_path: `lte-downlink-spectral-emission-mask.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte/raw/resource/enus/lte-downlink-spectral-emission-mask.html
- document_id: `rfmx-lte`
- page_type: `leaf`
- content_type: `concept`
- source_description: The RFmx LTE spectral emission mask (SEM) measurement uses the configurations and masks specified by the 3GPP standard. This topic explains the configurations and masks used by the RFmx LTE Downlink SEM measurement. Refer to the SEM Overview topic for a general overview of single and multicarrier SE

### LTE Downlink Spectral Emission Mask

The RFmx LTE spectral emission mask (SEM) measurement uses the configurations and masks
 specified by the 3GPP standard. This topic explains the configurations and masks used by
 the RFmx LTE Downlink SEM measurement.

Refer to the SEM Overview topic for a general overview of single and multicarrier SEM
 measurement concepts.

#### Offset Segments

The offset segments are
 the channels adjacent to the carrier channels and are specified by their start and
 stop frequencies (Δf) relative to the nearest edge of the closest
 E-UTRA carrier. This applies to a single carrier, intraband contiguous, intraband
 non-contiguous, and multiband operations. The offset segment frequencies,
 bandwidths, and limits are defined by 3GPP specification.

The power of any
 offset segment is measured with the measurement filter defined in section 6.6.3 of
 the *3GPP 36.141* specification. Unlike uplink, the masks of
 downlink depend on the operating band as well. The masks are defined from a few MHz
 below the lowest frequency of each supported downlink operating band, up to 10 MHz
 above the highest frequency of each supported downlink operating band. The limit
 requirements apply inside any subblock gap and the inside inter-RF bandwidth gap, if
 any. These cumulative evaluation requirements are not applicable, where the multiple
 bands are mapped on separate antenna connectors, in such case the requirements of a
 single band is applied to each of the bands.

The RBW filter for all offset
 segments are Gaussian, and the resolution bandwidths are set according to the
 measurement bandwidth defined in 3GPP specification.

According to the 3GPP
 specification, the resolution bandwidth of the measuring equipment should be equal
 to the measurement bandwidth. However, to improve the measurement accuracy,
 sensitivity, and efficiency, the resolution bandwidth the measuring equipment may be
 smaller than the measurement bandwidth. When the resolution bandwidth is smaller
 than the measurement bandwidth, the result is integrated over the measurement
 bandwidth to obtain the equivalent noise bandwidth of the measurement
 bandwidth.

The measurement improves the resolution of the spectrum by using
 bandwidth integrals, which specifies the resolution of the spectrum to compare with
 spectral mask limits as an integer multiple of the RBW filter bandwidth. The
 measurement acquires the spectrum with a narrow resolution and processes it
 digitally to get a wider resolution that is equal to the product of the bandwidth
 integral and the RBW filter bandwidth. When resolutions of the overlapping masks are
 different, the lowest resolution is used to compute the composite
 mask.

#### Masks

The power of any base station (BS)
 emission must not exceed the levels specified for a mask type for different offset
 segments. As per the 3GPP specification, the measurement passes if all the offset
 segments are less than this limit.

The masks are specified based on the eNodeB
 categories, E-UTRA BS operating band, and Edge carrier bandwidths. The unlicensed
 TDD band 46 is used for LAA or license assisted operation and is a special case with
 different test requirements than other bands.

There are few additional
 requirements mentioned for certain regions and bands defined by 3GPP
 Specification.

You can choose the SEM Downlink Mask Type property and eNodeB
 Category property to specify test requirements defined by 3GPP
 specification.

#### Home Base Station

Masks for Home Base
 Station are dependent on the SEM Aggregated Max Pwr property. The aggregated maximum
 power is defined as the total power of all transmitted antenna ports.

#### Medium Base Station

The table for masks is selected based on configured
 SEM CC Max Output Power property as specified by 3GPP specification. The maximum
 output power is defined as the mean power level per carrier measured at the antenna
 connector during the transmitter ON period. Masks for Medium Base Station are
 dependent on measured carrier power(s).

Occasionally, the emission masks may
 overlap for BS capable of transmitting in multiple bands or multiple subblocks. In
 such scenarios, the limit mask requirement is defined as a composite emission masks,
 which is a combination of carriers’ general emissions masks, and is as stated
 below:

- Masks within 10 MHz (20 MHz for band 46) from the edges for some frequency out
 of band, the cumulative sum of the spectral emission masks specified at the
 edges on each side of the overlap will be applicable. Here, the edge refers to
 the carrier edge, the subblock edge, or the RF bandwidth edge.
- Masks beyond 10 MHz (20 MHz for band 46) from the edges for some frequency out
 of band, the spectrum emission mask with the higher power spectral density
 applies for these frequencies.

The mask does not apply for frequency, where the sub-block spectrum emission
 mask overlaps with the sub-block bandwidth of another sub-block. The masks are
 defined in multiple tables in the section 6.6.3 of 3GPP specification.

For
 example, the following image shows the carrier channel and the offset channel
 configurations for DL SEM with two operating bands (X, Y) and three subblocks (A, B,
 C).

- Subblock A is comprised of 2 contiguous component carriers (CC-A0 and CC-A1).
 Subblock B is comprised of 3 contiguous component carriers (CC-B0, CC-B1, and
 CC-B2). Subblock C is comprised of 2 contiguous component carriers (CC-C0 and
 CC-C1).
- Offset segments are denoted as OA and OB.
- The Δf max is the frequency separation between the carrier edge or
 subblock edge (in case of multicarrier) and the nominal -3 dB point of last
 measurement bandwidth filter. Configure the Δf<sub>max</sub> using the SEM
 Delta F_Max property. When you specify the SEM downlink mask type property
 as Custom, the SEM measurement ignores this
 parameter.

[IMAGE alt='image' src='GUID-A0B5BEB3-6E05-4CBF-BAFC-A68B57B20F69-a5.png']

The cumulative regions are
 present in the inter subblock gap with a span of 10 MHz. The cumulative region for
 Band 46 is 20 MHz wide.

- If the multiple masks belonging to the adjacent subblocks overlap in this
 region, the sum of PSD of the limits is used for those overlapping
 frequencies.
- If the multiple masks belonging to the adjacent subblocks overlap within inter
 subblock gap but outside cumulative regions, the maximum of the PSD of limits is
 used for those overlapping frequencies.

All masks are defined with respect to the closest carrier.

If you set the
 SEM Downlink Mask Type property to Custom, the following
 parameters are ignored:

- Delta F_Max (Hz)
- Aggregated Maximum Power (dBm)
- Max Output Power (dBm)
- eNodeB Category

Related information:

- SEM

<!--NI_TOPIC bundle=rfmx-lte path=lte-modulation-accuracy.html language=enus -->
## TOPIC 00013: LTE Modulation Accuracy

- bundle_id: `rfmx-lte`
- source_path: `lte-modulation-accuracy.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte/raw/resource/enus/lte-modulation-accuracy.html
- document_id: `rfmx-lte`
- page_type: `leaf`
- content_type: `concept`
- source_description: The key results of this measurement are Mean RMS Composite EVM, Max Peak Composite EVM, Mean Frequency Error, Mean IQ Origin Offset, Mean IQ Gain Imbalance, Mean IQ Quadrature Error, and In-Band Emission Margin. For more information on modulation accuracy measurements in LTE refer to the Transmit Si

### LTE Modulation Accuracy

The key results of this measurement are Mean RMS Composite EVM, Max Peak Composite EVM,
 Mean Frequency Error, Mean IQ Origin Offset, Mean IQ Gain Imbalance, Mean IQ Quadrature
 Error, and In-Band Emission Margin. For more information on modulation accuracy
 measurements in LTE refer to the Transmit Signal Quality Measurements
 section of the Introduction to LTE Device Testingapplication
 note<sup>[1]</sup>.

#### Auto Resource Block Detection
 Enabled

ModAcc measurement supports auto detection of carrier resource
 configurations. You can configure auto-detection by using the Auto RB Detection
 Enabled property, which defaults to True, where the
 modulation type, number of PUSCH clusters, PUSCH resource block offsets and PUSCH
 resource block sizes are automatically detected by the measurement.

#### Synchronization Mode

The frame and slot synchronization modes enable you
 to synchronize to the frame or slot boundaries. For more information on the frame
 structure of an LTE frame refer to LTE Frame Structure
 application note<sup>[1]</sup>. The ModAcc measurement is made over the Measurement
 Length (slots) property, starting at the Measurement Offset (slots) property from
 that boundary. The frame synchronization mode allows you to measure specific slots
 in a frame, while the slot mode starts the measurement at the first complete slot in
 the acquisition.

The marker synchronization mode is a unique mode that
 enables you to obtain the fastest modulation accuracy measurements. In the marker
 mode, you must provide a digital trigger at the start of the frame and use this
 trigger in ModAcc. The measurement internally uses the fact that the acquisition is
 triggered at the start of the frame and optimizes some processing to offer a faster
 measurement time.

The following images illustrate the slots that are measured
 in various synchronization modes, measurement offsets, and trigger configurations.
 The measurement length is 2 slots in all the examples.

[IMAGE alt='image' src='GUID-D56A07DF-7A73-44F1-AAF3-2DD6864D19DC-a5.gif']

[IMAGE alt='image' src='GUID-1FCD223D-BEF4-44DE-A150-670897834D34-a5.gif']

[IMAGE alt='image' src='GUID-80D88799-85CA-42FC-B52B-ED7CA551ED44-a5.gif']

[IMAGE alt='image' src='GUID-C343D4BC-2948-4DAF-AF91-6651D8707717-a5.gif']

[IMAGE alt='image' src='GUID-2BEA31B7-5D8E-4D1B-B74A-C735C89EA3D0-a5.gif']

[IMAGE alt='image' src='GUID-AB1EDA7F-EA61-49CA-BF07-9794DB1EAF58-a5.gif']

#### ModAcc FFT Window Type, Length and Offset

An OFDM symbol consists of FFT
 length worth data samples (N) and cyclic prefix samples (CP). An FFT is taken only
 on N samples and hence the position in time for FFT can start at any instant within
 the cyclic prefix. The EVM requirements are met within a window, which has a length
 lesser than the CP length. The FFT start positions are relative to the center of the
 CP such that adjacent FFT start positions or FFT Window Length apart from each
 other.

Refer to annex E of *3GPP 36.521* specification for
 more details.

The samples used for FFT are determined by the FFT window length
 or the FFT window offset.

The following image illustrates the FFT window types
 and the flow of action.

[IMAGE alt='image' src='GUID-F7F744A5-6379-4349-81D2-5DC54C01ADEA-a5.gif']

If you set ModAcc FFT Window Type property to 3GPP, EVM
 calculation uses two reduced windows. You can specify the window's starting
 positions by setting the FFT Window Length property. The windows are determined as
 (ΔC – W/2) and (ΔC + W/2), where
 ΔC is the center of CP and the center of FFT Window, and
 W is the window length. For each OFDM symbol, the EVM is
 calculated for these reduced windows each having a length of the FFT size (N). These
 two timings leads to two different EVMs: EVM<sub>low</sub> and EVM<sub>high</sub>.
 The averaging is done separately and the maximum of EVM<sub>low</sub> and
 EVM<sub>high</sub> is returned as the final EVM.

All results related to
 EVM, phase error, magnitude error, and all other corresponding traces are affected
 by this selection and are reported with respect to the window resulting in maximum
 averaged EVM.

If you set FFT Window Length property to -1, RFmx automatically
 selects the FFT window length based on the Channel Bandwidth as given in below
 table. Refer to annex E.5.1 of the *3GPP 36.104* specification for
 more details.

| Channel Bandwidth (MHz) | FFT Size | Normal CP | Extended CP |  |  |
| --- | --- | --- | --- | --- | --- |
| EVM Window Length (W) | W/(CP length) for Symbols 1-6 (%)* | EVM Window Length (W) | W/(CP length) for Symbols 1-6 (%) |  |  |
| 1.4 | 128 | 5 | 55.6 | 28 | 87.5 |
| 3 | 256 | 12 | 66.7 | 58 | 90.6 |
| 5 | 512 | 32 | 88.9 | 124 | 96.9 |
| 10 | 1,024 | 66 | 91.7 | 250 | 97.7 |
| 15 | 1,536 | 102 | 94.4 | 378 | 98.4 |
| 20 | 2,048 | 136 | 94.4 | 504 | 98.4 |

* For normal CP, symbol 0 has a lower percentage value.

If you set the
 ModAcc FFT Window Type property to Custom, only one FFT
 window offset is used for EVM calculation. The start of the FFT window is relative
 to the start of OFDM symbol excluding the CP. You can specify the window offset by
 setting the FFT Window Offset property.

The following image illustrates the
 FFT Window Type, the FFT Window Length, and the FFT Window Offset compared with the
 window positions and offset.

[IMAGE alt='image' src='GUID-3B322C5B-D122-4A4D-BCD3-9732C3D6DB10-a5.gif']

#### References

<sup>[1]</sup> NI RF Academy.
 (2014, February 01). Introduction to LTE Device Testing. Retrieved March 10, 2015,
 from
 http://download.ni.com/evaluation/rf/Introduction_to_LTE_Device_Testing.pdf

<!--NI_TOPIC bundle=rfmx-lte path=lte-occupied-bandwidth.html language=enus -->
## TOPIC 00014: LTE Occupied Bandwidth

- bundle_id: `rfmx-lte`
- source_path: `lte-occupied-bandwidth.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte/raw/resource/enus/lte-occupied-bandwidth.html
- document_id: `rfmx-lte`
- page_type: `leaf`
- content_type: `concept`
- source_description: The RFmx LTE occupied bandwidth (OBW) measurement uses the configurations specified by the 3GPP standard. This topic explains the configurations used by the RFmx LTE OBW measurement. Refer to the OBW Overview topic for a general overview of OBW measurement concepts. Single-Carrier OBWAccording to 3G

### LTE Occupied Bandwidth

The RFmx LTE occupied bandwidth (OBW) measurement uses the configurations specified by
 the 3GPP standard. This topic explains the configurations used by the RFmx LTE OBW
 measurement.

Refer to the OBW Overview topic for a general overview of OBW measurement concepts.

#### Single-Carrier OBW

According to *3GPP TS 36.521-1*
 specification, LTE OBW measures the bandwidth that occupies 99% of the total power
 in the acquired spectrum. The occupied channel bandwidth should be less than the
 channel bandwidth specified in following table. For more information about OBW
 configurations, refer to section 6.6.1 of *3GPP TS 36.521-1*
 specification.

| Occupied Bandwidth | 1.4 MHz | 3.0 MHz | 5 MHz | 10 MHz | 15 MHz | 20 MHz |
| --- | --- | --- | --- | --- | --- | --- |
| Channel Bandwidth (MHz) | 1.4 | 3.0 | 5.0 | 10.0 | 15.0 | 20.0 |

To select narrowband internet of things (NB-IoT) OBW, you can set CC
 Bandwidth property to 200.0 k in RFmx LTE OBW
 measurement.

For NB-IoT OBW, the occupied bandwidth should be less than 200
 kHz, which is the channel bandwidth for NB-IoT.

The occupied bandwidth is
 measured using a span that is two times the channel bandwidth centered on the
 carrier.

For more information on the occupied bandwidth measurement an LTE
 signal refer to the Occupied Bandwidth section of the
 Introduction to LTE Device Testing application
 note<sup>[1]</sup>.

#### Intraband Contiguous Carrier Aggregated
 OBW

In the intra-band contiguous carrier aggregation scenario, occupied
 bandwidth is a measure of the bandwidth containing 99% of the total integrated power
 of the transmitted spectrum. The OBW is less than the aggregated channel
 bandwidth.

The occupied bandwidth is measured using a span that is two times
 the aggregated channel bandwidth centered on the aggregated carrier.

#### Intra-band Noncontiguous Carrier Aggregated OBW

In the intra-band
 noncontiguous carrier aggregation, each subblock (contiguous aggregated carriers) is
 measured separately where occupied bandwidth is a measure of the bandwidth
 containing 99% of the total integrated power of the transmitted spectrum for each
 subblock. The OBW for each subblock is less than the aggregated channel bandwidth
 for that subblock.

In the intra-band noncontiguous carrier aggregation, the
 occupied bandwidth is measured using a calculated span for each subblock centered on
 the subblock. This span is calculated such that it does not cross the middle of
 subblock gap with respect to its adjacent subblocks. However, the span is never more
 than twice the aggregated channel bandwidth for any subblock.

[IMAGE alt='image' src='GUID-3197F964-75AE-431D-9454-9710B43AEAD6-a5.gif']

#### References

<sup>[1]</sup> NI RF Academy.
 (2014, February 01). Introduction to LTE Device Testing. Retrieved March 10, 2015,
 from
 http://download.ni.com/evaluation/rf/Introduction_to_LTE_Device_Testing.pdf

Related information:

- Occupied Bandwidth

<!--NI_TOPIC bundle=rfmx-lte path=lte-power-vs-time.html language=enus -->
## TOPIC 00015: LTE Power Vs Time

- bundle_id: `rfmx-lte`
- source_path: `lte-power-vs-time.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte/raw/resource/enus/lte-power-vs-time.html
- document_id: `rfmx-lte`
- page_type: `leaf`
- content_type: `concept`
- source_description: The LTE Power Vs Time (PVT) measurement measures the time domain power dynamics of an LTE/LTE-A signal. This measurement is also known as Transmit ON-OFF Time Mask measurement. 3GPP specification limits the average OFF power that a user equipment (UE) can emit. The higher OFF power increases the ris

### LTE Power Vs Time

The LTE Power Vs Time (PVT) measurement measures the time domain power dynamics of an
 LTE/LTE-A signal. This measurement is also known as Transmit ON-OFF Time Mask
 measurement. 3GPP specification limits the average OFF power that a user equipment (UE)
 can emit. The higher OFF power increases the rise over thermal noise (ROT) and causes
 interference to other users.

#### Measurement Overview

According to the 3GPP specification, if the carrier
 frequency is less than or equal to 3.0 GHz, the average OFF power of a UE must be
 less than or equal to -48.5 dBm. If the carrier frequency is more than 3.0 GHz and
 less than or equal to 4.2 GHz, the average OFF power of a UE must be less than or
 equal to -48.2 dBm.

The following image shows the various regions of the PVT
 measurement:

[IMAGE alt='image' src='GUID-6DD7F762-0EE3-4CBC-BAF1-5F96663E9508-a5.gif']

The LTE PVT measurement
 measures the power in the following segments:

OFF Power
 Before—This segment is defined as the OFF power region before the
 captured burst. The length is defined as 1 subframe for FDD and 10 SC-FDMA symbols
 for TDD signals.

ON Power—This segment is defined as
 the ON power region in the captured burst excluding the transient period of 20 µs at
 the beginning of the burst. The length of this region depends on the UL/DL
 configuration used for the transmission in case of TDD. The length of the captured
 burst is calculated by the measurement automatically.

OFF Power
 After—This segment is defined as the OFF power region of one
 sub-frame duration after the captured burst excluding the transient period of 20 µs
 at the beginning of the subframe.

The LTE PVT measurement is supported only
 with the triggered acquisitions: IQ Power Edge and Digital Edge Triggers. In case of
 Digital Edge Trigger, a marker is expected at the start of a frame.

#### LTE
 PVT Dynamic Range Mode

LTE UE transmits the maximum power of +23 dBm, the
 OFF power limit being -50 dBm, and the dynamic range required is around 73 dB. The
 theoretical OFF power limit can go even lower based on the thermal noise floor. For
 example, for 20 MHz bandwidth, the OFF power value is -96 dBm, for 10 MHz bandwidth,
 the OFF power value is -99 dBm, and so on. To measure this OFF power accurately, the
 dynamic range needed is very high (~120 dB) and none of the available instruments in
 the market provide this dynamic range. LTE PVT dynamic range mode provides a dual
 acquisition solution to achieve the required dynamic range.

The first
 acquisition captures the I/Q with the user defined reference level, which will
 measure the ON power accurately. However, OFF power will not be represented
 adequately due to the limited dynamic range of the device, which leads to an
 inaccurate measurement of OFF power. To solve this, a second acquisition is done at
 a lower reference level which ensures the OFF power regions are represented
 adequately. These two acquisitions are combined by the measurement to get a
 composite power trace having OFF region from the second acquisition and ON region
 from the first acquisition as shown in the picture below. The power measurement is
 done on this composite trace.

Supported Devices: PXIe-5644/5645/5646

[IMAGE alt='image' src='GUID-B8A31B6F-1767-45F2-9E1F-EB51646F9CB8-a5.gif']

#### LTE
 PVT OFF Power Exclusion Periods

The LTE PVT measurement supports the
 exclusion period on both sides of the burst that can be used to move OFF region
 boundaries.

RFmx LTE provides the OFF Power Exclusion Before property and OFF
 Power Exclusion After property, which allows you to configure/set a different
 exclusion period on each side of the burst. The following image shows the effect of
 configuring the exclusion period compared with 3GPP defined boundaries.

Note

[IMAGE alt='image' src='GUID-2CEB4D50-F642-4573-9736-123DBE5DF3D0-a5.gif']

The default value for both, the
 OFF Power Exclusion Before property and OFF Power Exclusion After property, is 0,
 which ensures the value adheres to the 3GPP definition. The maximum time value is
 limited to 100 µs on both the sides.

<!--NI_TOPIC bundle=rfmx-lte path=lte-uplink-adjacent-channel-power.html language=enus -->
## TOPIC 00016: LTE Uplink Adjacent Channel Power

- bundle_id: `rfmx-lte`
- source_path: `lte-uplink-adjacent-channel-power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte/raw/resource/enus/lte-uplink-adjacent-channel-power.html
- document_id: `rfmx-lte`
- page_type: `leaf`
- content_type: `concept`
- source_description: This topic explains the different configurations used by the RFmx LTE adjacent channel power (ACP) measurement. The RFmx LTE ACP measurement uses the configurations as specified by the 3GPP TS 36.521-1 specification. The period of measurement for LTE Uplink ACP is at least the continuous duration of

### LTE Uplink Adjacent Channel Power

This topic explains the different configurations used by the RFmx LTE adjacent channel
 power (ACP) measurement.

The RFmx LTE ACP measurement uses the configurations as specified by the *3GPP TS
 36.521-1* specification. The period of measurement for LTE Uplink ACP is at
 least the continuous duration of one sub-frame (1 ms) as defined in *3GPP TS
 36.521-1* specification. Hence, when you set the Sweep Time Auto property to
 True, the sweep time is set to 1 ms for the LTE Uplink ACP
 measurement.

Refer to the ACP Overview topic for a general overview of single and multicarrier ACP
 measurement concepts.

#### Offset Channels

The offset channels are adjacent to the carrier channels.
 The *3GPP TS 36.521-1* specification defines two types of offset channels
 for LTE; universal terrestrial radio Access (UTRA) and evolved universal terrestrial
 radio access (E-UTRA).

The number of UTRA offset channels defaults to 2, and
 the number for E-UTRA offset channels defaults to 1, as specified in the *3GPP
 TS 36.521-1* specification. For ACP carrier aggregation, the power
 reference defaults to sum of the subblock powers to conform to the *3GPP TS
 36.521-1* specification.

You can change the number of UTRA and
 E-UTRA offset channels in a measurement by configuring the ACP Num UTRA Offsets and
 ACP Num EUTRA Offsets properties respectively provided you set the ACP Configurable
 Number of Offsets Enabled property to True.

#### Types of Measurements

The LTE downlink ACP measurements can be
 categorized into following three types:

- Single carrier ACP
- Intra-band contiguous carrier aggregation ACP
- Non-contiguous carrier aggregation ACP

Note

#### Single-Carrier ACP

The types of single-carrier ACP are E-UTRA Offset
 Channels for Single Carrier and UTRA Offset Channels for Single
 Carrier.

#### E-UTRA Offset Channels for Single Carrier

The E-UTRA ACLR
 (E-UTRA<sub>ACLR</sub>) is the ratio of the filtered average power centered on
 an adjacent E-UTRA channel to the filtered average power centered on the carrier
 channel, with channel spacing and measurement bandwidths as specified in the
 following table.

| Number Of EUTRA Offsets = m | Channel Bandwidth |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| 1.4 MHz | 3.0 MHz | 5 MHz | 10 MHz | 15 MHz | 20 MHz |  |
| E-UTRA Center Frequency Offset (MHz) | m * 1.4 or -m * 1.4 | m * 3 or -m * 3 | m * 5 or -m * 5 | m * 10 or -m * 10 | m * 15 or -m * 15 | m * 20 or -m * 20 |
| E-UTRA Channel Measurement Bandwidth (MHz) | 1.08 | 2.7 | 4.5 | 9 | 13.5 | 18 |

#### UTRA
 Offset Channels for Single Carrier

The UTRA ACLR (UTRA<sub>ACLR</sub>) is
 the ratio of the filtered average power centered on an adjacent UTRA channel to the
 filtered average power centered on the carrier channel, with channel spacing and
 measurement bandwidths as specified in the preceding table. UTRA ACLR is measured
 for two UTRA adjacent channels by default.

The UTRA channel power is measured
 with a RRC bandwidth filter with roll-off factor α = 0.22. For LTE-FDD, the UTRA
 offset channels are assumed to be WCDMA channels. For LTE-TDD, the UTRA offset
 channels are assumed to be TD-SCDMA channels. The position of offsets in frequency
 with respect to the center of the LTE carrier (E-UTRA) and their measurement
 bandwidths are specified in the following table.

| Number Of UTRA Offsets = n k = 2 * n - 1 | Channel Bandwidth/UTRAACLR(n)/Measurement Bandwidth |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| 1.4 MHz | 3.0 MHz | 5 MHz | 10 MHz | 15 MHz | 20 MHz |  |
| UTRAACLR(n) Center Frequency Offset (MHz) | 0.7 + (k * BWUTRA / 2) and -0.7 + (k * BWUTRA / 2) | 1.5 + (k * BWUTRA/ 2) and -1.5 + (k * BWUTRA / 2) | +2.5 + (k * BWUTRA / 2) and -2.5 + (k * BWUTRA / 2) | +5 + (k * BWUTRA / 2) and -2.5 + (k * BWUTRA/ 2) | +7.5 + (k * BWUTRA / 2) and -7.5 + (k * BWUTRA / 2) | +10 + (k * BWUTRA / 2) and -10 + (k * BWUTRA / 2) |
| Example: UTRAACLR(n) Center Frequency Offset For FDD (MHz) | 3.2 and -3.2 | 4 and -4 | 5 and -5 | 7.5 and -7.5 | 10 and -10 | 12.5 and -12.5 |
| FDD UTRA Measurement Bandwidth | 3.84 MHz | 3.84 MHz | 3.84 MHz | 3.84 MHz | 3.84 MHz | 3.84 MHz |
| TDD UTRA Measurement Bandwidth | 1.28 MHz | 1.28 MHz | 1.28 MHz | 1.28 MHz | 1.28 MHz | 1.28 MHz |

BW<sub>UTRA</sub> for FDD UTRA offset channel is 5
 MHz.

BW<sub>UTRA</sub> for TDD UTRA offset channel is 1.6
 MHz.

#### Intra-band Contiguous Carrier Aggregation ACP

Intra-band contiguous
 carrier aggregation ACP is similar to the single-carrier scenario, and the
 aggregated carrier is considered to be one EUTRA carrier. UTRA channel
 configurations are similar to the single-carrier configuration scenarios. The
 adjacent offset channels are placed relative to the center of aggregated carrier
 bandwidth.

#### E-UTRA Offset Channels for Contiguous Carrier Aggregation

The center of
 the first adjacent E-UTRA channel is located at the aggregated carrier bandwidth
 away from the center of assigned E-UTRA channel frequency. The measurement bandwidth
 is the same as the measurement bandwidth of the assigned E-UTRA channel (aggregated
 LTE carriers). The power of this E-UTRA adjacent channel is measured with a
 rectangular filter.

Similarly, the center of successive E-UTRA offset channels
 are (m * CA_BW) away from the center of the assigned E-UTRA
 channel (aggregated LTE carriers) for the mth E-UTRA offset, where
 CA_BW signifies the aggregated channel bandwidth.

For
 example, if two component carriers are configured as 20 MHz + 20 MHz with nominal
 spacing, the aggregated channel (EUTRA) bandwidth is 39.8 MHz. In this scenario, one
 EUTRA offset channel with 37.8 MHz of measurement bandwidth is placed 39.8 MHz away
 from the center of the aggregated carriers on both the sides. This E-UTRA offset
 channel is measured with a rectangular filter.

#### UTRA
 Offset Channels for Contiguous Carrier Aggregation

The UTRA measurement
 bandwidths are similar to the measurement bandwidths of the single carrier. The
 center of the UTRA offset channels are [CA_BW + (2 * n - 1) *
 BW<sub>UTRA</sub>]/2 away from the center of the assigned
 E-UTRA channel (aggregated LTE carriers) for the n<sup>th</sup>
 UTRA offset, where CA_BW signifies the aggregated carriers
 channel bandwidth.

#### Intra-band Non-contiguous Carrier Aggregation ACP

In the intra-band
 non-contiguous carrier aggregation scenario, UTRA and E-UTRA offset channels to the
 right and left of each subblock are measured, which means that some offset channels
 between the two subblocks are called the inner offset channels.

[IMAGE alt='image' src='GUID-EB54AE1C-7D40-4BD8-B268-29B0BCBC3589-a5.gif']

#### E-UTRA Offset Channels for Intra-band Non-contiguous Carrier
 Aggregation

Normally, one E-UTRA offset channel is considered for
 intra-band non-contiguous carrier aggregation. If the inner E-UTRA offset channel of
 a subblock overlaps with another subblock, the inner E-UTRA offset is not measured
 and a NaN is returned as the result.

The following image depicts all possible
 cases for inner E-UTRA offsets with and without overlap with the adjacent subblock,
 where SB-A and SB-B are two subblocks, EU-A is the E-UTRA offset channel for
 subblock A, and EU-B is the E-UTRA offset channel for subblock B.

[IMAGE alt='image' src='GUID-F6286118-17D3-40AC-8C8D-FEAF6F38D58B-a5.gif']

#### UTRA
 Offset Channels for Intra-band Non-contiguous Carrier Aggregation

Two UTRA
 offset channels are always considered for intra-band non-contiguous carrier
 aggregation.

If the gap between two adjacent subblocks is less than 5 MHz, no
 inner UTRA offset channel is measured, and NaNs are returned for both the inner UTRA
 channels.

If the gap between two adjacent subblocks is less than 15 MHz but
 greater than or equal to 5 MHz, UTRA offset channel is not measured and NaNs are
 returned for  the other inner UTRA channels.

For any subblock, if any of its
 (inner) UTRA offset channel overlaps with another subblock, the UTRA offset is not
 measured, and a NaN is returned as the result.

The following image depicts all
 possible cases with inner E-UTRA offset with and without overlap with the adjacent
 subblock, where SB-A and SB-B are two subblocks, U1 is the first UTRA offset
 channel, U1-A is the first UTRA offset channels for subblock A, U2 is the second
 UTRA offset channel, and U2-B is the second UTRA offset channels for subblock
 B.

[IMAGE alt='image' src='GUID-29D2AC47-63B6-47A4-B74B-65407BCE827E-a5.gif']

Related information:

- Adjacent Channel Power Overview

<!--NI_TOPIC bundle=rfmx-lte path=lte-uplink-spectral-emission-mask.html language=enus -->
## TOPIC 00017: LTE Uplink Spectral Emission Mask

- bundle_id: `rfmx-lte`
- source_path: `lte-uplink-spectral-emission-mask.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte/raw/resource/enus/lte-uplink-spectral-emission-mask.html
- document_id: `rfmx-lte`
- page_type: `leaf`
- content_type: `concept`
- source_description: The RFmx LTE spectral emission mask (SEM) measurement uses the configurations and masks specified by the 3GPP TS 36.521-1 specification. This topic explains the configurations and masks used by the RFmx LTE Uplink SEM measurement. The period of measurement for LTE Uplink SEM is at least the continuo

### LTE Uplink Spectral Emission Mask

The RFmx LTE spectral emission mask (SEM) measurement uses the configurations and masks
 specified by the *3GPP TS 36.521-1* specification. This topic explains the
 configurations and masks used by the RFmx LTE Uplink SEM measurement.

The period of measurement for LTE Uplink SEM is at least the continuous duration of one
 sub-frame (1 ms) as defined in *3GPP TS 36.521-1* specification. Hence, when
 you set the Sweep Time Auto property to True, the sweep time is set to
 1 ms for the LTE Uplink SEM measurement.

Refer to the SEM Overview topic for a general overview of single and multicarrier SEM
 measurement concepts.

#### Offset Segments

The offset segments are the
 channels adjacent to the carrier channels and are specified by their start and stop
 frequencies (Δf<sub>OOB</sub>) relative to the nearest edge of assigned
 E-UTRA channel or carrier aggregated channels. The offset segment frequencies and bandwidths
 are defined by *3GPP TS 36.521-1* specification for all E-UTRA carrier
 channels and few selected CA bandwidth combinations.

The power of any offset segment
 is measured with the measurement filter defined in section 6.6.2 of the *3GPP TS
 36.521-1* specification. While measuring offset segment power, the following
 rules are followed, which are defined by *3GPP TS 36.521-1* specification
 test requirements:

- For any of the first offset segments, the first and last measurement position with a 30
 kHz filter is at Δf OOB equals to 0.015 MHz and 0.985
 MHz.
- For rest of the offset segments, at the boundary of the spectrum emission limit, the
 first and last measurement position with a 1 MHz filter is the inside of +0.5 MHz and -0.5
 MHz, respectively.
- The measurements are performed above the upper edge of the channel and below the lower
 edge of the channel.
- A special case for the third offset segment for a 1.4 MHz carrier—For the 2.5 MHz to 2.8
 MHz offset range with 1.4 MHz channel bandwidth, the measurement position is at
 Δf OOB equals to 3 MHz.

The RBW filter for all offset segments are Gaussian, and the resolution bandwidths are
 set according to the measurement bandwidth defined in 3GPP specification.

The accuracy
 of the measurement is increased by using a resolution bandwidth smaller than the measurement
 bandwidth. The measurement bandwidth gets divided by the bandwidth integral to realize a
 lower resolution bandwidth. However, the results are obtained by integrating over the
 measurement bandwidth.

For the first offset segments, the RBW is set to 10 KHz with
 the bandwidth integral value of 3, resulting in a measurement bandwidth of 30 KHz.

For
 the second offset segments, the RBW is set to 250 KHz with the bandwidth integral value of
 4, resulting a measurement bandwidth of 1 MHz.

#### Masks

The power of any UE emission must not
 exceed the limits specified for a mask type for different offset segments. As per the
 *3GPP TS 36.521-1* specification, the measurement passes if the power
 spectrum values for all offset segments are less than this limit.

There are two kinds
 of requirements as defined by *3GPP TS 36.521-1* specification for these
 mask types—minimum requirement and test requirement.

RFmx LTE uses the test
 requirement tables. These tables are dependent on frequency band.

You can configure the
 Standard Mask Type to specify either general masks/ limits or any other additional mask
 defined by 3GPP.

#### Single-Carrier SEM

The following sections
 list the tables that are defined by the *3GPP TS 36.521-1* specification
 for a single carrier.

Single Carrier – Base Requirements

For more information
 about the base requirements, refer to the following tables:

- Table 6.6.2.1_1.5-1, General E-UTRA spectrum emission mask, E-UTRA bands ≤ 3
 GHz
- Table 6.6.2.1_1.5-2, General E-UTRA spectrum emission mask, 3 GHz ≤ E-UTRA
 bands ≤ 4.2 GHz

#### Single Carrier – Additional Requirements

For
 more information about the additional requirements, refer to the following tables:

- Table 6.6.2.2.5.1-1, Additional requirements (network signalled value "NS_03",
 “NS_11”, “NS_20” and “NS_21”), E-UTRA bands ≤ 3 GHz
- Table 6.6.2.2.5.1-2, Additional requirements (network signalled value "NS_03",
 “NS_11”, “NS_20” and “NS_21”), 3 GHz ≤ E-UTRA bands ≤ 4.2 GHz
- Table 6.6.2.2.3.2-3, Additional requirements (network signalled value "NS_04"),
 (Release 12 and onwards)
- Table 6.6.2.2.5.3-1, Additional requirements (network signalled value "NS_06"
 or "NS_07"), E UTRA bands = 3 GHz
- Table 6.6.2.2.5.3-2, Additional requirements (network signalled value "NS_06"
 or "NS_07"), 3 GHz < E UTRA bands = 4.2 GHz
- Table 6.6.2.2A.3.5-1, Additional requirements (network signalled value
 "CA_NC_NS_01"), E UTRA bands ≤ 3 GHz
- Table 6.6.2.2A.3.5-2, Additional requirements (network signalled value
 "CA_NC_NS_01"), 3 GHz < E UTRA bands ≤ 4.2 GHz
- Table 6.6.2.2.5.4, Additional requirements (network signalled value
 "NS_27")
- Table 6.6.2.2.5.5, Additional requirements (network signalled value
 "NS_35")

#### Intra-Band Contiguous Carrier Aggregated
 SEM

3GPP has defined spectrum emission limit for a few bandwidth combinations
 where the offset segments are defined Δf<sub>OOB</sub> frequency away
 from the edge of the aggregated carrier. The rest of the requirements are the same as that
 of a single carrier. The following tables are defined for different bandwidth
 combinations.

#### Intra-Band Contiguous Carrier Aggregated SEM - Base
 Requirements

For more information about the base requirements, refer to the
 following tables:

- Table 6.6.2.1A.1.5-1, General E-UTRA spectrum emission mask for CA Class C, E
 UTRA bands ≤ 3 GHz
- Table 6.6.2.1A.1.5-2, General E-UTRA spectrum emission mask for CA Class C, 3
 GHz < E UTRA bands ≤ 4.2 GHz
- Table 6.6.2.1A.1.5-3, General E-UTRA spectrum emission mask for CA Bandwidth
 Class B, E-UTRA bands ≤ 3 GHz
- Table 6.6.2.1A.1.5-4, General E-UTRA spectrum emission mask for CA Bandwidth
 Class B, 3 GHz < E UTRA bands ≤ 4.2 GHz

#### Intra-band Contiguous Carrier Aggregated SEM -
 Additional Requirements

For more information about the additional requirements,
 refer to the Table 6.6.2.2A.1.5.1-1, Additional requirements for
 CA_NS_04.

#### Intra-band Non-Contiguous Carrier Aggregated SEM

For intra-band
 non-contiguous, the requirement is the same as the single carrier and intraband
 contiguous configurations, and each subblock is treated separately as long as the
 subblock gaps have no overlapping offset segments.

Sometimes the offset
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

For the first offset segment, to get a 3GPP specification mandated
 measurement bandwidth of 30 kHz, the RBW is set to 10 kHz with bandwidth integral
 value of 3.

For all other offset segments, to get a 3GPP specification
 mandated measurement bandwidth of 1 MHz, the RBW is set to 250 kHz with bandwidth
 integral value of 4.

The following figure shows two carrier channel and offset
 channel configurations for the LTE-Advanced intra-band non-contiguous configuration
 with two subblocks A and B. Subblock A is comprised of two contiguous component
 carriers (CC-A0 and CC-A1). Similarly, subblock B is comprised of three contiguous
 component carriers (CC-B0, CC-B1 and CC-B2). Offset segments are denoted as OA and
 OB.

[IMAGE alt='image' src='GUID-61E812C7-9B19-46B6-9656-7BD91BA7D4C5-a5.gif']

The rightmost offset segment of
 subblock A, OA-R1 and leftmost offset segment of subblock B, OB-L2 overlaps in the
 above picture. In this case, the combined spectral emission mask is calculated
 considering highest power spectral density (PSD) value of all overlapping masks for
 that frequency.

[IMAGE alt='image' src='GUID-21F319D8-437B-4696-B67F-6429992C815A-a5.gif']

Related information:

- SEM

<!--NI_TOPIC bundle=rfmx-lte path=lte-v2x-overview.html language=enus -->
## TOPIC 00018: LTE V2X Overview

- bundle_id: `rfmx-lte`
- source_path: `lte-v2x-overview.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte/raw/resource/enus/lte-v2x-overview.html
- document_id: `rfmx-lte`
- page_type: `leaf`
- content_type: `concept`
- source_description: LTE V2X is introduced as sidelink transmission mode 3 and mode 4 in the Release 14 of 3GPP specification. In V2X, vehicles communicate directly with everything around them. V2X comprises of vehicle-to-vehicle (V2V) communications, vehicle-to-infrastructure (V2I) communications, vehicle-to-pedestrian

### LTE V2X Overview

LTE V2X is introduced as sidelink transmission mode 3 and mode 4 in the Release 14 of
 3GPP specification. In V2X, vehicles communicate directly with everything around them.
 V2X comprises of vehicle-to-vehicle (V2V) communications, vehicle-to-infrastructure
 (V2I) communications, vehicle-to-pedestrian (V2P) communications.

V2X is used for low latency safety services and out of coverage operations. V2X supports
 half duplex frequency division duplex (HD-FDD) operations as well as 10 MHz and 20 MHz
 channel bandwidths.

Sidelink uses the single-carrier frequency-division multiple access (SC-FDMA)
 transmission scheme and consists of 14 symbols in each subframe.

Note

#### Guard Symbol

The last SC-FDMA symbol in a
 sidelink subframe serves as a guard period and not used for sidelink
 transmission.

#### Physical Channels

Physical sidelink shared channel (PSSCH) is used to
 carry sidelink data. Supported modulation schemes are QPSK, 16-QAM and
 64-QAM.

Physical sidelink control channel (PSCCH) is used to carry sidelink
 control information (SCI). SCI Format 1 consists of PSSCH transmission information
 and is transmitted in two consecutive resource blocks (RBs). For more information
 on PSCCH, refer to section 5.4.3.1 of *3GPP 36.212*
 specification.

3GPP 36.213

[IMAGE alt='image' src='GUID-617927D1-4D91-4651-9EAF-6BC057B71521-a5.png']

#### Demodulation Reference Signal (DMRS)

3GPP 36.211

[IMAGE alt='image' src='GUID-1A9B8B18-7920-48BE-B0F7-078F58ADDE79-a5.png']

#### Retransmission

Data and control
 information transmitted in a subframe can be retransmitted. Frequency allocation and
 subframe time gap between initial transmission and retransmission can be varied. For
 more information on retransmission, refer to section 14.1.1.4C of *3GPP
 36.213* specification.

<!--NI_TOPIC bundle=rfmx-lte path=nb-iot-downlink-adjacent-channel-power.html language=enus -->
## TOPIC 00019: NB-IoT Downlink Adjacent Channel Power

- bundle_id: `rfmx-lte`
- source_path: `nb-iot-downlink-adjacent-channel-power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte/raw/resource/enus/nb-iot-downlink-adjacent-channel-power.html
- document_id: `rfmx-lte`
- page_type: `leaf`
- content_type: `concept`
- source_description: The RFmx LTE Narrowband Internet of Things (NB-IoT) Downlink Adjacent Channel Power (ACP) measurement uses the configurations defined in the 3GPP TS 36.141 specification. To select NB-IoT ACP, set CC Bandwidth property to 200.0 k in RFmx LTE ACP measurement. For a general overview of single and mult

### NB-IoT Downlink Adjacent Channel Power

The RFmx LTE Narrowband Internet of Things (NB-IoT) Downlink Adjacent Channel Power
 (ACP) measurement uses the configurations defined in the 3GPP TS
 36.141 specification.

To select NB-IoT ACP, set CC Bandwidth property to 200.0
 k in RFmx LTE ACP measurement.

For a general overview of single and multicarrier ACP measurement concepts, refer to
 *Adjacent Channel Power Overview*.

#### Offset
 Channels

The offset channels are adjacent to the carrier channels. Section
 6.6.2.5 of the 3GPP TS
 36.141 specification defines Stand-alone NB-IoT offset channels for NB-IoT.

In RFmx LTE, the number of
 Stand-alone NB-IoT offset channels defaults to 2, as specified in the 3GPP TS 36.141 specification.

To change the
 number of Stand-alone NB-IoT offset channels in the measurement, configure the
 ACP Num Standalone NB-IoT Offsets property. You must also
 set the ACP Configurable Number of Offsets Enabled property
 to True.

#### NB-IoT
 Single Carrier ACP

The Standalone NB-IoT Offsets ACLR (Standalone NB-IoT
 Offsets ACLR) is the ratio of the filtered average power centered on an adjacent
 Standalone NB-IoT Offsets channel to the filtered average power centered on the
 carrier channel.

The following table specifies the channel spacing, channel
 measurement bandwidth for adjacent channels and channel measurement bandwidth for
 NB-IoT carrier.

| Number of Standalone NB-IoT Offsets = m | Standalone NB-IoT Offsets |
| --- | --- |
| Adjacent channel center frequency offset from NB-IoT channel center. | [100 + (m + 1) * 200] kHz |
| Adjacent channel measurement bandwidth | 180 kHz |
| NB-IoT channel measurement bandwidth | 180 kHz |

Related information:

- Adjacent Channel Power Overview

<!--NI_TOPIC bundle=rfmx-lte path=nb-iot-downlink-spectral-emission-mask.html language=enus -->
## TOPIC 00020: NB-IoT Downlink Spectral Emission Mask

- bundle_id: `rfmx-lte`
- source_path: `nb-iot-downlink-spectral-emission-mask.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte/raw/resource/enus/nb-iot-downlink-spectral-emission-mask.html
- document_id: `rfmx-lte`
- page_type: `leaf`
- content_type: `concept`
- source_description: Spectral emission mask (SEM) measurements measure out-of-band emissions in the neighboring bands of the carrier. To select a narrowband internet of things (NB-IoT) Downlink spectral emission mask (SEM) in RFmx LTE SEM measurement, set the following properties: Set the CC Bandwidth property to 200.0

### NB-IoT Downlink Spectral Emission Mask

Spectral emission mask (SEM) measurements measure out-of-band emissions in the
 neighboring bands of the carrier.

- Set the CC Bandwidth property to 200.0
 k
- Set the SEM Downlink Mask Type property to
 eNodeB Category

For a general overview of SEM measurement concepts, refer to the *SEM* section.

#### Offset
 Segments

The offset segments are the channels adjacent to the carrier
 channels. To specify offset segments, define their start and stop frequencies (Δf)
 relative to the NB‑IoT carrier edge.

Section *6.6.3.5.2E - 6.6.3.5.2H* of the *3GPP TS 36.141* specification defines the offset segment
 frequencies, bandwidths, and limits.

The RBW filter for all offset segments is
 Gaussian. The measurement bandwidth defined in section *6.6.3.5.2E - 6.6.3.5.2H* of the *3GPP TS 36.141* specification sets the
 resolution bandwidths.

#### Masks

An NB‑IoT UE must keep its emission power within the limits for
 each offset segment. According to 3GPP TS 36.141, the measurement passes when the
 power‑spectrum values for all offset segments are less than the limit.

The
 eNodeB categories and the E‑UTRA BS operating band are used to specify the
 masks.

Section *6.6.3.5.2E -
 6.6.3.5.2H* of the *3GPP TS
 36.141* specification defines the limits for NB-IoT SEM
 measurement.

Related concepts:

- RFmx LTE 2026 Q2 Changes

Related information:

- SEM

<!--NI_TOPIC bundle=rfmx-lte path=nb-iot-uplink-adjacent-channel-power.html language=enus -->
## TOPIC 00021: NB-IoT Uplink Adjacent Channel Power

- bundle_id: `rfmx-lte`
- source_path: `nb-iot-uplink-adjacent-channel-power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte/raw/resource/enus/nb-iot-uplink-adjacent-channel-power.html
- document_id: `rfmx-lte`
- page_type: `leaf`
- content_type: `concept`
- source_description: This topic is an introduction to Narrowband Internet of Things (NB-IoT) Uplink Adjacent Channel Power (ACP) measurement. To select NB-IoT ACP, you can set CC Bandwidth property to 200.0 k in RFmx LTE ACP measurement. The period of measurement for NB-IoT ACP is at least one sub-frame (1 ms) for 15 kH

### NB-IoT Uplink Adjacent Channel Power

This topic is an introduction to Narrowband Internet of Things (NB-IoT) Uplink Adjacent
 Channel Power (ACP) measurement. To select NB-IoT ACP, you can set CC Bandwidth property
 to 200.0 k in RFmx LTE ACP measurement.

The period of measurement for NB-IoT ACP is at least one sub-frame (1 ms) for 15 kHz
 channel spacing and at least a 2 ms slot (excluding the 2304Ts gap when user equipment
 (UE) is not transmitting) for 3.75 kHz channel spacing, as defined in section 6.6.2.3F.4
 of *3GPP TS 36.521-1* specification. Hence, when you set the Sweep Time
 Auto property to True, the sweep time is set accordingly for the NB-IoT ACP
 measurement.

Refer to the *ACP Overview* topic for a general overview of ACP measurement
 concepts.

#### Offset Channels

The offset channels are
 adjacent to the carrier channels. The section 6.6.2.3F of *3GPP TS
 36.521-1* specification defines two types of offset channels for
 NB-IoT; universal terrestrial radio access (UTRA) and global system for mobile
 communications (GSM).

In RFmx LTE, the number of UTRA offset channels and the
 number for GSM offset channels defaults to 1, as specified in the *3GPP TS
 36.521-1* specification.

You can change the number of UTRA and
 GSM offset channels in the measurement by configuring the ACP Num UTRA Offsets and
 ACP Num GSM Offsets properties respectively provided you set the ACP Configurable
 Number of Offsets Enabled property to True.

#### NB-IoT Single Carrier ACP

The 3GPP
 specification has defined only single Carrier ACP for NB-IoT.

The GSM ACLR
 (GSM<sub>ACLR</sub>) is the ratio of the filtered average power centered on an
 adjacent GSM channel to the filtered average power centered on the carrier channel.
 UTRA ACLR (UTRA<sub>ACLR</sub>) is the ratio of the filtered average power centered
 on an adjacent UTRA channel to the filtered average power centered on the carrier
 channel.

The following table specifies the channel spacing, channel
 measurement bandwidth for adjacent channels and channel measurement bandwidth for
 NB-IoT carrier.

| Number of GSM Offsets = m, Number of UTRA Offsets = n, k = 2n - 1 | GSM Offsets | UTRA Offsets |
| --- | --- | --- |
| Adjacent channel center frequency offset from NB-IoT channel center. | [100 + (m + 1) * 200] kHz | [100 + (k * BWUTRA/2)] kHz |
| Adjacent channel measurement bandwidth | 180 kHz | 3.84 MHz |
| NB-IoT channel measurement bandwidth | 180 kHz | 180 kHz |

BW<sub>UTRA</sub> for UTRA offset channel is 5 MHz.

Related information:

- Adjacent Channel Power Overview

<!--NI_TOPIC bundle=rfmx-lte path=nb-iot-uplink-spectral-emission-mask.html language=enus -->
## TOPIC 00022: NB-IoT Uplink Spectral Emission Mask

- bundle_id: `rfmx-lte`
- source_path: `nb-iot-uplink-spectral-emission-mask.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte/raw/resource/enus/nb-iot-uplink-spectral-emission-mask.html
- document_id: `rfmx-lte`
- page_type: `leaf`
- content_type: `concept`
- source_description: This topic is an introduction to narrowband internet of things (NB-IoT) uplink spectral emission mask (SEM) measurement. To select NB-IoT SEM, you can set CC Bandwidth property to 200.0 k and SEM Uplink Mask Type property to General_NS01 in RFmx LTE SEM measurement. The period of measurement for NB-

### NB-IoT Uplink Spectral Emission Mask

This topic is an introduction to narrowband internet of things (NB-IoT) uplink spectral
 emission mask (SEM) measurement. To select NB-IoT SEM, you can set CC Bandwidth property
 to 200.0 k and SEM Uplink Mask Type property to
 General_NS01 in RFmx LTE SEM measurement.

The period of measurement for NB-IoT Uplink SEM is at least one sub-frame (1 ms) for 15
 kHz channel spacing and at least a 2 ms slot (excluding the 2304Ts gap when user
 equipment (UE) is not transmitting) for 3.75 kHz channel spacing, as defined in section
 6.6.2.1F.4 of *3GPP TS 36.521-1* specification. Hence, when you set the
 Sweep Time Auto property to True, the sweep time is set accordingly for the NB-IoT
 Uplink SEM measurement.

Refer to the SEM Overview topic for a general overview of SEM measurement concepts.

#### Offset Segments

The offset segments are
 the channels adjacent to the carrier channels and are specified by their start and
 stop frequencies (Δf<sub>OOB</sub>) relative to the edge of of
 NB-IoT carrier.

The power of any offset segment is measured with the
 measurement filter bandwidth defined in section 6.6.2.1F of *3GPP TS
 36.521-1* specification. While measuring offset segment power, at the
 boundary of spectrum emission limit, the first and last measurement position with a
 30 kHz filter is the inside of + 15 kHz and - 15 kHz, respectively. The filter shall
 be stepped to cover the whole range.

The RBW filter for all offset segments is
 Gaussian, and the resolution bandwidths are set according to the measurement
 bandwidth defined in 3GPP specification. The accuracy of the measurement is
 increased by using a resolution bandwidth smaller than the measurement bandwidth.
 The measurement bandwidth gets divided by the bandwidth integral to realize a lower
 resolution bandwidth. However, the results are obtained by integrating over the
 measurement bandwidth.

For NB-IoT SEM, for the first and second offset
 segments, the RBW is set to 7.5 kHz with the bandwidth integral value of 4,
 resulting in a measurement bandwidth of 30 kHz which is the measurement bandwidth
 defined by the 3GPP specification. For rest of the offset segments, RBW is set to
 30kHz with bandwidth integral value of 1.

#### Masks

The power of any NB-IoT UE emission
 must not exceed the limits specified for different offset segments. As per the
 *3GPP TS 36.521-1* specification, the measurement passes if the
 power spectrum values for all offset segments are less than this limit.

There
 are two kinds of requirements as defined by *3GPP TS 36.521-1*
 specification minimum requirement and test requirement.

In RFmx LTE, test
 requirement tables are used for NB-IoT SEM.

The limits for NB-IoT SEM
 measurement are defined in section 6.6.2.1F of 3GPP TS 36.521-1
 specification.

Related information:

- SEM

<!--NI_TOPIC bundle=rfmx-lte path=new-features-and-changes.html language=enus -->
## TOPIC 00023: RFmx LTE New Features and Changes

- bundle_id: `rfmx-lte`
- source_path: `new-features-and-changes.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte/raw/resource/enus/new-features-and-changes.html
- document_id: `rfmx-lte`
- page_type: `leaf`
- content_type: `concept`
- source_description: Learn about updates, including new features and behavior changes, introduced in each version of RFmx LTE. Discover what is new in the latest releases of RFmx LTE.If you cannot find new features and changes for your version, it might not include user-facing updates. However, your version might includ

### RFmx LTE
 New Features and Changes

Learn about updates, including new features and behavior changes, introduced in each
 version of RFmx LTE.

RFmx LTE

Note

Release Notes

Related information:

- Software and Driver Downloads

#### RFmx LTE
 2026 Q2 Changes

RFmx LTE 2026 Q2 adds NBIoT Downlink Spectral measurements and expands NBIoT Downlink
 ModAcc measurement capabilities. This release also adds support for the PXIe-5841 with 200
 MHz bandwidth.

##### New
 Features

This version of RFmx LTE adds support for the following
 features:

- NBIoT Downlink Spectral measurements.
- 16 QAM modulation and two NRS antenna ports in
 NBIoT Downlink ModAcc measurement.

##### Behavior Changes

This version of RFmx LTE updates support for the following feature:

- Adjacent Channel Power (ACP): Configuring the Number of Analysis
 Threads property to a value greater than 1 is allowed when using
 the Sequential FFT measurement method.

##### New
 Hardware Support

This version of RFmx LTE
 adds support for the following hardware:

- PXIe-5841 ( 200 MHz ) bandwidth

Related concepts:

- NB-IoT Downlink Spectral Emission Mask

#### RFmx LTE 2026 Q1 Changes

Learn about new features, behavior changes, and other updates in RFmx LTE 2026 Q1.

- Added support for NTN bands 246 and 249.
- Added support for Python API.

#### RFmx LTE 2025 Q4 Changes

Learn about new features, behavior changes, and other updates in RFmx LTE 2025 Q4.

- Added support for Bands 112 and 113, and NTN Band 252.

#### RFmx LTE 2025 Q3 Changes

Learn about new features, behavior changes, and other updates in RFmx LTE 2025 Q3.

- Added support for band n111.
- Added support for Self-Cal Validity Check for PXIe-5860.

#### RFmx LTE 2025 Q1 Changes

Learn about new features, behavior changes, and other updates in RFmx LTE 2025 Q1.

- Added support for NBIoT Downlink ModAcc measurement.

#### RFmx LTE 2024 Q4 Changes

Learn about new features, behavior changes, and other updates in RFmx LTE 2024 Q4.

##### New Features

- Added support for extended frequency error estimation in LTE ModAcc.
- Added ‘Maximum EVM-High per Symbol Trace’ and ‘Maximum EVM-Low per Symbol Trace’
 APIs.
- Added support for bands 54, 103, 106 & NTN bands 253, 254.

##### Behavior Changes

- Uninstalling RFmx LTE software also removes any
 previous versions of RFmx LTE .NET runtimes that
 were leaked in .NET Global Assembly Cache directory.

#### RFmx LTE 2024 Q3 Changes

Learn about new features, behavior changes, and other updates in RFmx LTE 2024 Q3.

- Added support for TXP measurement.
- Added support for PXIe-5860.
- Added support for List Mode on the following devices:
  - PXIe-5840
  - PXIe-5841
  - PXIe-5842
  - PXIe-5830
  - PXIe-5831
  - PXIe-5832

#### RFmx LTE
 2024 Q2 Changes

Learn about new features, behavior changes, and other updates in RFmx LTE 2024 Q2.

- Obsoleted the RFmxInstr Load All Configurations VI. Use the
 RFmxInstr Load Configurations VI along with the appropriate
 RFmxInstr Load Options property, instead.

#### RFmx LTE 2024 Q1 Changes

Learn about new features, behavior changes, and other updates in RFmx LTE 2024 Q1.

- Added support for Band 256 in SEM measurements.

#### RFmx LTE 2023 Q4 Changes

Learn about new features, behavior changes, and other updates in RFmx LTE 2023 Q4.

- Updated the multiple constellation trace in DL in SFP.
- Added support for obtaining unprocessed I/Q data utilized for RFmx
 measurements.

#### RFmx LTE 2023 Q3 Changes

Learn about new features, behavior changes, and other updates in RFmx LTE 2023 Q3.

- Added support for Noise Compensation in ACP measurements for Sequential FFT
 mode.

<!--NI_TOPIC bundle=rfmx-lte path=noise-compensation-algorithm.html language=enus -->
## TOPIC 00024: Noise Compensation Algorithm

- bundle_id: `rfmx-lte`
- source_path: `noise-compensation-algorithm.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte/raw/resource/enus/noise-compensation-algorithm.html
- document_id: `rfmx-lte`
- page_type: `leaf`
- content_type: `concept`
- source_description: Compensates for noise during 5G NR signal testing, ensuring precise modulation metrics and reliable RFmx LTE measurements. Noise compensation details are described by assuming the following model test setup. When the switch connects to the DUT path, the noise power measured by the signal analyzer, P

### Noise Compensation Algorithm

Compensates for noise during 5G NR signal testing, ensuring precise modulation
 metrics and reliable RFmx LTE measurements.

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

<!--NI_TOPIC bundle=rfmx-lte path=noise-fundamentals.html language=enus -->
## TOPIC 00025: Noise Fundamentals

- bundle_id: `rfmx-lte`
- source_path: `noise-fundamentals.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte/raw/resource/enus/noise-fundamentals.html
- document_id: `rfmx-lte`
- page_type: `leaf`
- content_type: `concept`
- source_description: Introduces key concepts of noise in RF measurements, explaining its impact on 5G NR signal analysis and accuracy in RFmx LTE testing workflows. Thermal Noise Fidelity of electromagnetic circuits is most commonly compromised by the noise generated by the components constituting the circuit, among oth

### Noise Fundamentals

Introduces key concepts of noise in RF measurements, explaining its impact on 5G NR
 signal analysis and accuracy in RFmx LTE testing
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

<!--NI_TOPIC bundle=rfmx-lte path=rfmxlte-overview.html language=enus -->
## TOPIC 00026: RFmx LTE Overview

- bundle_id: `rfmx-lte`
- source_path: `rfmxlte-overview.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte/raw/resource/enus/rfmxlte-overview.html
- document_id: `rfmx-lte`
- page_type: `leaf`
- content_type: `concept`
- source_description: This user manual contains introduction to RFmx LTE measurement concepts.

### RFmx LTE Overview

This user manual contains introduction to RFmx LTE
 measurement concepts.

<!--NI_TOPIC bundle=rfmx-lte path=subblock.html language=enus -->
## TOPIC 00027: Subblock

- bundle_id: `rfmx-lte`
- source_path: `subblock.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte/raw/resource/enus/subblock.html
- document_id: `rfmx-lte`
- page_type: `leaf`
- content_type: `concept`
- source_description: A subblock is a collection of contiguous component carriers used for transmission and reception by the same user equipment (UE). Intra-band contiguous carrier aggregation uses one subblock. Intra-band noncontiguous and inter-band noncontiguous carrier aggregation use two or more subblocks. The follo

### Subblock

A subblock is a collection of contiguous component carriers used for transmission and
 reception by the same user equipment (UE). Intra-band contiguous carrier aggregation
 uses one subblock. Intra-band noncontiguous and inter-band noncontiguous carrier
 aggregation use two or more subblocks.

The following table lists some aggregated bandwidth combinations as defined by the 3GPP
 specification.

| Subblock Component Carriers (MHz) | Aggregated Channel Bandwidth (MHz) | Aggregated Measurement Bandwidth (MHz) |
| --- | --- | --- |
| 10 MHz + 20 MHz | 29.90 | 27.90 |
| 15 MHz + 15 MHz | 30.00 | 28.50 |
| 15 MHz + 20 MHz | 34.85 | 32.85 |
| 20 MHz + 20 MHz | 39.80 | 37.80 |
| 5 MHz + 20 MHz | 24.95 | 22.95 |

The nominal guard band on either side of aggregated carriers is defined in the following
 table,

where, a<sub>1</sub> = 0.16/1.4 for BW<sub>Channel(1)</sub> of 1.4 MHz

and a<sub>1</sub> = 0.05 for all other channel bandwidths.

| Maximum Number Of CCs | Nominal Guard Band (At Both Edges Of The Subblock) |
| --- | --- |
| 1 | a1 * BWChannel(1) |
| n (where n > 1) | 0.05 * max(BWChannel(1), BWChannel(2), ...BWChannel(n)) |

For more information about noncontiguous carrier aggregation, refer to Table 5.4.2A-1 in
 the *3GPP TS 36.521-1* specification.

[IMAGE alt='image' src='GUID-54D4C4FF-44D1-4F7C-ABB8-FCD47F6C61FB-a5.gif']

<!--NI_TOPIC bundle=rfmx-lte path=supported-hw.html language=enus -->
## TOPIC 00028: Supported Hardware

- bundle_id: `rfmx-lte`
- source_path: `supported-hw.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte/raw/resource/enus/supported-hw.html
- document_id: `rfmx-lte`
- page_type: `leaf`
- content_type: `concept`
- source_description: RFmx supports a number of NI devices. 1 RFmx LTE Supported Hardware RFmx LTE Hardware Earliest Driver Version Support (Windows 11) PXIe-5644 2022 Q3 PXIe-5645 2022 Q3 PXIe-5646 2022 Q3 PXIe-5663 2022 Q3 PXIe-5665 2022 Q3 PXIe-5668 2022 Q3 PXIe-5820 2022 Q3 PXIe-5840 2022 Q3 PXIe-5841 (1 GHz Bandwidt

### Supported Hardware

RFmx supports a number of NI devices.

| RFmx LTE Hardware | Earliest Driver Version Support (Windows 11) |
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
| PXIe-5841 (200 GHz Bandwidth) | 2026 Q2 |
| PXIe-5842 | 2022 Q4 |
| PXIe-5860 | 2024 Q3 |

Note

RFmx LTE

NI-RFSA
 Properties

NI-RFSA LabVIEW VI Reference

For more information about your hardware and functionality, refer to the *NI-RFSA User Manual*.

Related information:

- NI-RFSA Properties
- NI-RFSA User Manual

<!--NI_TOPIC bundle=rfmx-lte path=system-requirements.html language=enus -->
## TOPIC 00029: RFmx LTE System Requirements

- bundle_id: `rfmx-lte`
- source_path: `system-requirements.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte/raw/resource/enus/system-requirements.html
- document_id: `rfmx-lte`
- page_type: `leaf`
- content_type: `concept`
- source_description: RFmx LTE has the following requirements: Processor—1 GHz 64-bit (x64) processor 4 GB RAM * A screen resolution of 1,024 x 768 Any supported OS, with all available critical updates and service packs * Depending on the amount of data acquired and/or processed, a larger amount of memory may be required

### RFmx LTE System Requirements

RFmx LTE has the following requirements:

- Processor—1 GHz 64-bit (x64) processor
- 4 GB RAM *
- A screen resolution of 1,024 x 768
- Any supported OS, with all available critical updates and service packs

* Depending on the amount of data acquired and/or processed, a larger amount of memory
 may be required.

<!--NI_TOPIC bundle=rfmx-lte path=uplink-narrowband-internet-of-things-overview.html language=enus -->
## TOPIC 00030: Uplink Narrowband Internet of Things Overview

- bundle_id: `rfmx-lte`
- source_path: `uplink-narrowband-internet-of-things-overview.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte/raw/resource/enus/uplink-narrowband-internet-of-things-overview.html
- document_id: `rfmx-lte`
- page_type: `leaf`
- content_type: `concept`
- source_description: Narrowband-internet of things (NB-IoT) is introduced in Release 13 of LTE 3GPP specification as a part of LTE Advanced Pro. NB-IoT is a low power wide area (LPWA) technology developed to cater to the needs of IoT devices. Its emphasis is on low cost and long battery life of the IoT devices and on le

### Uplink Narrowband Internet of Things Overview

Narrowband-internet of things (NB-IoT) is introduced in Release 13 of LTE
 3GPP specification as a part of LTE Advanced Pro. NB-IoT is a low power
 wide area (LPWA) technology developed to cater to the needs of IoT devices. Its emphasis
 is on low cost and long battery life of the IoT devices and on leveraging the existing
 LTE and GSM infrastructure. For NB-IoT, only half duplex FDD operation is supported.

Note

#### Physical
 Structure

The bandwidth of an uplink NB-IoT carrier is fixed to 200 kHz
 with 180 kHz as the transmission bandwidth and 10 kHz as the guard-band on either
 side. Uplink NB-IoT uses single-carrier frequency-division multiple access (SC-FDMA)
 transmission scheme and has 7 symbols in each slot. The subcarrier spacing can be
 either 15 kHz or 3.75 kHz. Per SC-FDMA symbol, there are 12 subcarriers with 15 kHz
 spacing or 48 subcarriers with 3.75 kHz spacing (180 kHz/15 kHz or 180 kHz/3.75
 kHz).

There are differences in the time domain structure of an NB-IoT uplink
 carrier, based on subcarrier spacing.

[IMAGE alt='image' src='GUID-1692F191-13F4-4B6D-8561-A3F85A276BEC-a5.gif']

[IMAGE alt='image' src='GUID-6240A545-201A-4E9D-AB4E-FE9E2992F77D-a5.gif']

Note

- Ts is the sampling time when sampling rate is 30.72 MHz.
- When the subcarrier spacing is 15 kHz, for symbol 0, the cyclic prefix
 duration is 160Ts. Therefore, the duration of symbol 0 is slightly more than
 the rest of the symbols at 71.88 us.

For uplink NB-IoT a new type of allocation, called resource unit, is defined
 to describe the mapping of the NPUSCH to resource elements.

Resource unit is
 the basic unit of narrowband physical uplink shared channel (NPUSCH) allocation in
 NB-IoT. A resource unit has N<sup>UL</sup><sub>symb</sub> *
 N<sup>UL</sup><sub>Slots</sub> consecutive SC-FDMA symbols in the time domain
 and N<sup>RU</sup><sub>SC</sub> consecutive subcarriers in the frequency domain.
 N<sup>UL</sup><sub>Slots</sub> and N<sup>RU</sup><sub>SC</sub> are as specified
 in the following table.

| NPUSCH Format | Δf | N RU sc | N UL slots | N UL symb |
| --- | --- | --- | --- | --- |
| 1 | 3.75 kHz | 1 | 16 | 7 |
| 15 kHz | 1 | 16 |  |  |
| 3 | 8 |  |  |  |
| 6 | 4 |  |  |  |
| 12 | 2 |  |  |  |
| 2 | 3.75 kHz | 1 | 4 |  |
| 15 kHz | 1 | 4 |  |  |

Note

- N UL Symb is the number of symbols in an uplink
 slot.
- N UL Slots is the number of consecutive slots in an
 uplink resource unit for NB-IoT.
- N RU SC is the number of consecutive subcarriers in an
 uplink resource unit for NB-IoT.
- Δf is the subcarrier spacing.

#### Narrowband
 Physical Uplink Shared Channel

The NPUSCH supports two formats.

- Format 1 is used to carry uplink shared channel (UL-SCH) which contains actual
 user data.
- Format 2 is used to carry uplink control information.

As seen in the preceding table, multi-tone configurations are allowed only for
 NPUSCH Format 1 with 15 kHz subcarrier spacing.

NPUSCH Modulation

The
 following table specifies the modulation schemes applicable for the NPUSCH
 channel.

| NPUSCH Format | N sc RU | Modulation Scheme |
| --- | --- | --- |
| 1 | 1 | BPSK, QPSK |
| >1 | QPSK |  |
| 2 | 1 | BPSK |

Demodulation Reference Signal

Based on NPUSCH format and subcarrier
 spacing, demodulation reference signal (DMRS) symbols can be at different positions
 in a slot and each slot can contain multiple DMRS symbols. The following table
 specifies the DMRS locations in a slot. l specifies the symbol
 index number in an NPUSCH slot.

| NPUSCH Format | Values for l |  |
| --- | --- | --- |
| Δf = 3.75 kHz | Δf = 15 kHz |  |
| 1 | 4 | 3 |
| 2 | 0, 1, 2 | 2, 3, 4 |

[IMAGE alt='image' src='GUID-2908FD7F-C509-432F-A9B4-C43C19909BFD-a5.gif']

#### Subcarrier Indication Field

Subcarrier
 indication field (I<sub>sc</sub>), in uplink DCI format N0, is a 6-bit unsigned
 integer with values ranging from 0 to 63. Subcarrier indication field determines the set of contiguously
 allocated subcarriers (n<sub>sc</sub>) in the resource unit of NB-IoT.

3.75
 kHz Subcarrier Spacing

When Δf = 3.75 kHz, n<sub>sc</sub> = I<sub>sc</sub>.
 This implies only a single tone can be transmitted when subcarrier spacing is 3.75
 kHz.

In RFmx LTE, you cannot set the
 I<sub>sc</sub>; instead you need to set the values of the NPUSCH Tone Offset property and
 NPUSCH Number of Tones property to specify where the tone is placed.

For
 example, if I<sub>sc</sub> = 25, it implies a tone is transmitted at 25<sup>th</sup>
 index out of the available 48 indexed subcarrier locations starting from
 0<sup>th</sup> index. In RFmx LTE the equivalent configuration would be to set
 NPUSCH Tone Offset property to 25 and NPUSCH Number of Tones property to 1.

Note

sc

#### 15 kHz Subcarrier Spacing

For 15 kHz
 subcarrier spacing, the subcarrier indication field (I<sub>sc</sub>) determines the
 set of contiguously allocated subcarriers (n<sub>sc</sub>) according to the
 following table.

| Subcarrier Indication Field (Isc) | Set of Allocated Subcarriers (nsc) |
| --- | --- |
| 0-11 | I sc |
| 12-15 | 3(Isc-12) + {0,1,2} |
| 16-17 | 6(Isc - 16) + {0,1,2,3,4,5} |
| 18 | {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11} |
| 19-63 | Reserved |

The following table specifies the relationship of I<sub>sc</sub> with NPUSCH
 Tone Offset and NPUSCH Number of Tones.

| Subcarrier Indication Field (Isc) | NPUSCH Tone Offset | NPUSCH Number of Tones |
| --- | --- | --- |
| 0-11 | I sc | 1 |
| 12 | 0 | 3 |
| 13 | 3 | 3 |
| 14 | 6 | 3 |
| 15 | 9 | 3 |
| 16 | 0 | 6 |
| 17 | 6 | 6 |
| 18 | 0 | 12 |
| 19-63 | Undefined | Undefined |

Note

- In RFmx LTE, to select NB-IoT mode, you need to set the CC Bandwidth
 property to 200.0 k .
- In RFmx LTE, carrier aggregation of more than one NB-IoT carrier is not
 supported.
- In RFmx LTE, only a single burst per measurement interval is supported.
- In RFmx LTE, when you set the Trigger Type property to Digital
 Edge , the marker should be provided at the start of the burst or 
 configure the trigger delay at the analyzer corresponding to the
 time delay between the marker and start of the burst.
 
 [IMAGE alt='image' src='GUID-1D307957-7CB3-4EF8-857D-F6BB10E26415-a5.png'] 
 [IMAGE alt='image' src='GUID-E373FF30-CA37-432A-BC04-9A218CF086D0-a5.png']
- In RFmx LTE, for reliable auto-detection of NPUSCH Modulation Type, the
 measurement interval for ModAcc measurement should consist of at-least 2
 consecutive active slots.

<!--NI_TOPIC bundle=rfmx-lte path=user-manual-welcome.html language=enus -->
## TOPIC 00031: RFmx LTE User Manual

- bundle_id: `rfmx-lte`
- source_path: `user-manual-welcome.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte/raw/resource/enus/user-manual-welcome.html
- document_id: `rfmx-lte`
- page_type: `leaf`
- content_type: `concept`
- source_description: The RFmx LTE User Manual provides detailed descriptions of the product functionality and the step by step processes for use. Looking for Something Else?For information not found in the User Manual for your product, such as specifications and API reference, browse Related Information.

### RFmx LTE
 User Manual

The RFmx LTE User Manual provides detailed
 descriptions of the product functionality and the step by step processes for use.

#### Looking for Something Else?

For information not found in the User Manual
 for your product, such as specifications and API reference, browse *Related
 Information*.

Related information:

- Download RFmx LTE/LTE-Advanced
- Download RFmx LTE-V2X
- Interactive Activation Guide
- RFmx LTE/LTE-Advanced Release Notes
- RFmx LTE-V2X Release Notes
- Getting Started with RFmx
- RFmx LTE LabVIEW Reference
- RFmx LTE .NET Reference
- RFmx LTE C Reference
- RFmx Instr LabVIEW Reference
- RFmx Instr .NET Reference
- RFmx Instr C Reference
