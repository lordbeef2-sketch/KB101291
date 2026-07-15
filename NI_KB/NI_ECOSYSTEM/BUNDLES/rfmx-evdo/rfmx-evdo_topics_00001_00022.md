# NI DOCUMENT BUNDLE: rfmx-evdo

<!--NI_BUNDLE_CHUNK bundle=rfmx-evdo start=1 end=22 -->
<!--NI_TOPIC bundle=rfmx-evdo path=cda-interval.html language=enus -->
## TOPIC 00001: CDA Measurement Interval

- bundle_id: `rfmx-evdo`
- source_path: `cda-interval.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo/raw/resource/enus/cda-interval.html
- document_id: `rfmx-evdo`
- page_type: `leaf`
- content_type: `concept`
- source_description: The measurement interval for which the Code Domain Analysis metrics are calculated is given by: Interval start - Start of the interval defined by an offset in slots relative to a synchronization event where the synchronization event can be configured to be at the first detected symbol, slot, or fram

### CDA Measurement Interval

The measurement interval for which the Code Domain Analysis metrics are calculated is
 given by:

Interval start - Start of the interval defined by an offset in
 slots relative to a synchronization event where the synchronization event can be
 configured to be at the first detected symbol, slot, or frame boundary within the
 acquired signal.

The synchronization event that the offset refers to is configured by the CDA
 Synchronization Mode property which can be set to Arbitrary,
 Slot, and Frame referring to symbol,
 slot, and frame synchronization, where:

- Symbol synchronization refers to the synchronization to the first detected symbol
 boundary within the acquired signal where the symbol definition refers to symbols
 with largest spreading factor of 64 chips. That is, symbol synchronization
 synchronizes to a chip offset relative to the frame start being an integer multiple
 of 64 chips.
- Slot synchronization refers to the synchronization to the first detected slot
 boundary within the acquired signal, where a slot is defined as a segment of the
 signal having a duration of 1.667 ms or equally 2048 chips. That is, slot
 synchronization synchronizes to a chip offset relative to the frame start being an
 integer multiple of 2048 chips.
- Frame synchronization refers to the synchronization to the first detected frame
 boundary within the acquired signal where a frame is defined as the segment of the
 signal having a duration 26.67 ms or equally 16 slots or 32768 chips. The offset is
 configured by the CDA Measurement Offset property.

Interval Duration - Duration of the interval configured as length
 in terms of slots. The duration is configured by the Measurement Length property.

<!--NI_TOPIC bundle=rfmx-evdo path=ev-do-acp.html language=enus -->
## TOPIC 00002: EV-DO ACP

- bundle_id: `rfmx-evdo`
- source_path: `ev-do-acp.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo/raw/resource/enus/ev-do-acp.html
- document_id: `rfmx-evdo`
- page_type: `leaf`
- content_type: `concept`
- source_description: EV-DO ACP Carrier Channels Carrier channels are the channels transmitted by the user equipment when the measurement is performed. For ACP measurements, you can configure multiple carrier channels by specifying their carrier offsets with respect to the configured analyzer center frequency. ACP measur

### EV-DO ACP

#### EV-DO ACP Carrier Channels

Carrier channels are the channels transmitted by the user equipment when the measurement
 is performed. For ACP measurements, you can configure multiple carrier channels by
 specifying their carrier offsets with respect to the configured analyzer center
 frequency. ACP measurements measure the individual channel power for each configured
 carrier channel as well as the total transmitted carrier power of the mobile terminal.
 The total transmitted carrier power is the sum of the powers of the carrier channels.
 The total transmitted carrier power is used as the power reference for the offset
 channel measurements.

#### EV-DO ACP Offset Channels

ACP measurements measure the absolute and relative power for a specific set of offset
 channels adjacent to the carrier channels. ACP measurements use predefined
 configurations derived from the spectral emission limits defined in the 3GPP
 standard.

#### Single Carrier Offset Channels

Single carrier EV-DO ACP measurements perform offset power measurements of 30 kHz
 integration bandwidth at specific, band class-dependent offset frequencies where offset
 frequency refers to the difference between the carrier center frequency and the closer
 measurement edge frequency, or the edge of the RBW filter.

The offset channel definitions for single carrier operation and for the individual band
 classes are listed in the following tables.

ACP Measurement Definition for Band Classes 0, 2, 5, 9, 11, and
 12

| Offset Frequency | RBW |
| --- | --- |
| ±885 kHz | 30 kHz |
| ±1.98 MHz | 30 kHz |
| ±4 MHz | 30 kHz |

ACP Measurement Definition for Band Classes 1 and 4

| Offset Frequency | RBW |
| --- | --- |
| ±1.25 MHz | 30 kHz |
| ±1.98 MHz | 30 kHz |
| ±4 MHz | 30 kHz |

ACP Measurement Definition for Band Class 3

| Offset Frequency | RBW |
| --- | --- |
| ±900 kHz | 30 kHz |
| ±1.98 MHz | 30 kHz |
| ±4 MHz | 30 kHz |

ACP Measurement Definition for Band Classes 6, 8 and 13

| Offset Frequency | RBW |
| --- | --- |
| ±1.25 MHz | 30 kHz |
| ±1.98 MHz | 30 kHz |
| ±2.25 MHz | 30 kHz |

ACP Measurement Definition for Band Class 7

| Offset Frequency | RBW |
| --- | --- |
| ±885 kHz | 30 kHz |
| ±1.98 MHz | 30 kHz |
| ±2.25 MHz | 6.25 kHz |

ACP Measurement Definition for Band Class 10

| Offset Frequency | RBW |
| --- | --- |
| ±885 kHz | 30 kHz |
| ±1.25 MHz | 30 kHz |
| ±4 MHz | 6.25 kHz |

#### Multicarrier Offsets

Multicarrier EV-DO ACP measurements perform offset power measurements of 30 kHz
 integration bandwidth at specific, partially band class-dependent offset frequencies.
 Offset frequency refers to the difference between the middle frequency of the
 multi carrier signal and the closer measurement edge frequency, or the edge of the RBW
 filter.

The offset channel definitions for multi-carrier operation are listed in the following
 tables.

ACP Measurement Definition for Multicarrier Operation Number or Carriers
 N = 3 for All Band Classes except Band Class 6

| Offset Frequency | RBW |
| --- | --- |
| ±2.5 MHz | 30 kHz |
| ±2.7 MHz | 30 kHz |
| ±3.5 MHz | 30 kHz |
| ±7.5 MHz | 30 kHz |
| ±8.5 MHz | 30 kHz |
| ±12.5 MHz | 30 kHz |

ACP Measurement Definition for Multicarrier Operation Number or Carriers
 N = 3 for Band Class 6

| Offset Frequency | RBW |
| --- | --- |
| ±2.5 MHz | 30 kHz |
| ±2.7 MHz | 30 kHz |
| ±3.08 MHz | 30 kHz |
| ±3.5 MHz | 30 kHz |
| ±7.5 MHz | 30 kHz |
| ±8.08 MHz | 30 kHz |
| ±8.5 MHz | 30 kHz |
| ±12.5 MHz | 30 kHz |

ACP Measurement Definition for Multicarrier Operation Number or Carriers
 N ≠ 3 for All Band Classes

| Offset Frequency | RBW |
| --- | --- |
| (2.5 + (N-3) · 0.625) MHz | 30 kHz |
| (3.5 + (N-3) · 0.625) MHz | 30 kHz |
| (3.125 · (N-1)) MHz | 30 kHz |

Related information:

- ACP

<!--NI_TOPIC bundle=rfmx-evdo path=ev-do-cda.html language=enus -->
## TOPIC 00003: EV-DO CDA

- bundle_id: `rfmx-evdo`
- source_path: `ev-do-cda.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo/raw/resource/enus/ev-do-cda.html
- document_id: `rfmx-evdo`
- page_type: `leaf`
- content_type: `concept`
- source_description: CDA measurement provides measurements in the code domain. Basically, it provides code domain power analysis and the calculation of modulation accuracy measures for a selected code channel. In detail, it provides the measures listed below. CDA Code Domain Power Measures For code domain power measures

### EV-DO CDA

CDA measurement provides measurements in the code domain. Basically, it provides code
 domain power analysis and the calculation of modulation accuracy measures for a selected
 code channel.

In detail, it provides the measures listed below.

#### CDA Code Domain Power
 Measures

For code domain power measures, CDA analyzes the code domain power of one or more
 slots for the base spreading factor configured through the Physical Layer Subtype
 property. The base spreading factor depends on the configured physical layer subtype
 and is 16 for subtype 0/1 and 32 otherwise.

Using the CDA Pwr Unit property,
 the measured power values can be configured to be absolute power values in dBm or
 relative power values in dB (in relation to the total code domain power).

The
 following code domain measures are computed:

- CDA Results UL Total Pwr - Returns the total code domain
 power in dBm.
- CDA Results UL Total Active Pwr - Returns total active
 code power either as absolute measure, in dBm, or as relative measure in
 dB.
- CDA Results UL Mean Active Pwr - Returns the average
 active code power either as absolute measure in dBm or as relative measure in
 dB.
- CDA Results UL Pk Active Pwr - Returns the maximum power
 among all active code channels either as absolute measure in dBm or as relative
 measure in dB.
- CDA Results UL Mean Inactive Pwr - Returns the average
 code power measured among the set of inactive channels either as absolute
 measure in dBm or as relative measure in dB.
- CDA Results UL Pk Inactive Pwr - Returns the largest
 measured code power among the set of inactive channels either as absolute
 measure in dBm or as relative measure in dB.
- CDA Results UL I Mean Active Pwr - Returns the average
 power of all active code channels measured on the I-branch.
- CDA Results UL I Pk Inactive Pwr - Returns the largest
 measured code power among the set of inactive channels on the I-branch and in
 the code domain of the base spreading factor.
- CDA Results UL Q Mean Active Pwr - Returns the average
 power of all active code channels measured on the Q-branch.
- CDA Results UL Q Pk Inactive Pwr - Returns the largest
 measured code power among the set of inactive channels on the Q-branch and in
 the code domain of the base spreading factor.
- CDA Results UL Mean Pilot Pwr - Returns the mean power of
 the R-PICH.
- CDA Results UL Mean Aux Pilot Pwr - Returns the mean
 power of the R-APICH.

<!--NI_TOPIC bundle=rfmx-evdo path=ev-do-chp.html language=enus -->
## TOPIC 00004: EV-DO CHP

- bundle_id: `rfmx-evdo`
- source_path: `ev-do-chp.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo/raw/resource/enus/ev-do-chp.html
- document_id: `rfmx-evdo`
- page_type: `leaf`
- content_type: `concept`
- source_description: RFmx EV-DO Carrier Channels RFmx EV-DO CHP carrier channels are the channels transmitted by the UE when the measurement is performed. For multicarrier analysis, multiple carrier channels can be configured by specifying their carrier offsets with respect to the configured analyzer center frequency. T

### EV-DO CHP

#### RFmx EV-DO Carrier
 Channels

RFmx EV-DO CHP carrier channels are the channels transmitted by the UE when the
 measurement is performed. For multicarrier analysis, multiple carrier channels can
 be configured by specifying their carrier offsets with respect to the configured
 analyzer center frequency.

The RFmx EV-DO CHP measurement measures the power of the RF signal for each
 individual carrier having a signal bandwidth of 1.2288 MHz as well as the total
 carrier power. The total carrier power is the sum of the powers of the individual
 carrier channels.

Related information:

- CHP

<!--NI_TOPIC bundle=rfmx-evdo path=ev-do-modacc-cda.html language=enus -->
## TOPIC 00005: CDA Modulation Accuracy Measures for Selected Code Channel

- bundle_id: `rfmx-evdo`
- source_path: `ev-do-modacc-cda.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo/raw/resource/enus/ev-do-modacc-cda.html
- document_id: `rfmx-evdo`
- page_type: `leaf`
- content_type: `concept`
- source_description: CDA provides the ability to analyze the modulation accuracy for a specific, user-configurable code channel. The code channel to be analyzed is configured by means of the spreading factor, channelization code, and branch using the CDA Meas Ch UL Walsh Code Length, CDA Meas Ch UL Walsh Code Number and

### CDA Modulation Accuracy Measures for Selected Code Channel

CDA provides the ability to analyze the modulation accuracy for a specific,
 user-configurable code channel. The code channel to be analyzed is configured by means
 of the spreading factor, channelization code, and branch using the CDA Meas Ch UL Walsh
 Code Length, CDA Meas Ch UL Walsh Code Number and CDA Meas Ch UL Branch properties,
 respectively.

For the selected code channel, the following measures are computed:

- CDA Results UL RMS Symbol EVM - Returns the RMS Symbol EVM
 for the selected channel as a percentage.
- CDA Results UL Pk Symbol EVM - Returns the Peak Symbol EVM
 for the selected channel as a percentage.
- CDA Results UL RMS Symbol Magnitude Error - Returns the RMS
 Symbol Magnitude Error for the selected channel in degrees.
- CDA Results UL RMS Symbol Phase Error - Returns the RMS
 Symbol Phase Error for the selected channel as a percentage.
- CDA Results UL Mean Symbol Pwr - Returns the Mean Symbol
 Power of the selected channel.

Additional measures for I/Q impairments are reported, such as:

- I/Q Origin Offset - Gives the DC Offset of IQ samples from
 the origin in dB.
- I/Q Gain Imbalance - Gives the IQ gain imbalance between
 inphase and quadrature component within the complex baseband signal in dB.
- I/Q Quadrature Error - Gives the phase difference from ideal
 90deg between inphase and quadrature component within the complex baseband signal in
 deg.

<!--NI_TOPIC bundle=rfmx-evdo path=ev-do-modacc.html language=enus -->
## TOPIC 00006: RFmx EV-DO Modulation Accuracy Measurements

- bundle_id: `rfmx-evdo`
- source_path: `ev-do-modacc.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo/raw/resource/enus/ev-do-modacc.html
- document_id: `rfmx-evdo`
- page_type: `leaf`
- content_type: `concept`
- source_description: RFmx EV-DO ModAcc measurements calculate the following performance metrics: Rho—Returns the normalized correlation coefficient of the measured signal and the generated reference signal. RMS EVM—Returns the RMS of the normalized EVM for the analyzed signal. Peak EVM—Returns the peak normalized EVM ob

### RFmx EV-DO Modulation Accuracy
 Measurements

RFmx EV-DO ModAcc measurements calculate the following performance metrics:

- Rho —Returns the normalized correlation coefficient of the
 measured signal and the generated reference signal.
- RMS EVM —Returns the RMS of the normalized EVM for the
 analyzed signal.
- Peak EVM —Returns the peak normalized EVM observed within
 the measurement interval for the analyzed signal.
- Peak CDE —Returns the maximum value among the code domain
 errors (CDEs), averaged over all the measured slots for the analyzed
 signal.
- Peak Active CDE —Returns the peak value of all CDEs of the
 active channels, averaged over all the measured slots for the analyzed
 signal.
- Frequency Error —Returns the frequency error averaged over
 all measured slots for the analyzed signal.
- Chip Rate Error —Returns the chip rate error for the
 analyzed signal.

Additionally, RFmx EV-DO ModAcc measurements also calculate the following I/Q
 impairments :

- I/Q Origin Offset —Returns the DC Offset of the I/Q
 samples from the origin.
- I/Q Gain Imbalance —Returns the I/Q gain imbalance between
 the in-phase and quadrature components within the complex baseband signal.
- I/Q Quadrature Error —Returns the phase difference from the
 ideal value of 90 degrees between the in-phase and quadrature component within
 the complex baseband signal.

<!--NI_TOPIC bundle=rfmx-evdo path=ev-do-obw.html language=enus -->
## TOPIC 00007: EV-DO OBW

- bundle_id: `rfmx-evdo`
- source_path: `ev-do-obw.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo/raw/resource/enus/ev-do-obw.html
- document_id: `rfmx-evdo`
- page_type: `leaf`
- content_type: `concept`
- source_description: EV-DO Carrier Channels EV-DO OBW carrier channels are the channels transmitted by the UE when the measurement is performed. For multicarrier analysis, you can configure multiple carrier channels by specifying their carrier offsets with respect to the configured analyzer center frequency. EV-DO OBW m

### EV-DO OBW

#### EV-DO Carrier Channels

EV-DO OBW carrier channels are the channels transmitted by the UE when the measurement is
 performed. For multicarrier analysis, you can configure multiple carrier channels by
 specifying their carrier offsets with respect to the configured analyzer center
 frequency.

EV-DO OBW measurements measure the signal bandwidth as the bandwidth where 99% of the RF
 power is concentrated. The span for the OBW measurement is automatically adapted
 according to the lowest and highest carrier frequencies of the configured carrier
 channels such that measurement span is 3 MHz +
 (ƒ<sub>Carrier,High</sub> - ƒ<sub>Carrier,Low</sub>).

Related information:

- OBW

<!--NI_TOPIC bundle=rfmx-evdo path=ev-do-sem.html language=enus -->
## TOPIC 00008: RFmx EV-DO SEM

- bundle_id: `rfmx-evdo`
- source_path: `ev-do-sem.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo/raw/resource/enus/ev-do-sem.html
- document_id: `rfmx-evdo`
- page_type: `leaf`
- content_type: `concept`
- source_description: RFmx EV-DO SEM Carrier Channels Carrier channels are the channels transmitted by the user equipment when the measurement is performed. For SEM measurements, you can configure multiple carrier channels by specifying their carrier offsets with respect to the configured analyzer center frequency. SEM m

### RFmx EV-DO SEM

#### RFmx EV-DO SEM Carrier Channels

Carrier channels are the channels transmitted by the user equipment when
 the measurement is performed. For SEM measurements, you can
 configure multiple carrier channels by specifying their carrier
 offsets with respect to the configured analyzer center frequency.
 SEM measurements measure the individual channel power for each
 configured carrier channel as well as the total transmitted carrier
 power of the mobile terminal. The total transmitted carrier power is
 the sum of the powers of the carrier channels. The total transmitted
 carrier power is used as the power reference for the SEM offset
 segment power measurements.

#### RFmx EV-DO SEM Offset Segments and Limit Masks

RFmx EV-DO SEM measurements use predefined definitions for the offset
 segments to measure and for the applied limit masks for these offset
 segments. The configurations are band class dependent and follow
 from the spectral emission limit tables specified for band classes 0
 to 13 in the *3GPP2* standard.

#### Single Carrier Offset Segments and Limit Masks

RFmx EV-DO SEM offset segments are defined by the measurement offset
 frequency Δf, where Δf is the
 difference between the carrier center frequency and the closer
 measurement edge frequency, or the edge of the RBW filter.

The
 offset segment definitions and corresponding emission limits for
 single carrier operation and for the individual band classes are
 listed in the following tables.

SEM Limits for Band Classes 0, 2, 5, 9, 11, and
 12

| Offset Segment | RBW | Relative Mask Limit | Absolute Mask Limit |
| --- | --- | --- | --- |
| 885 kHz ≤ \|Δƒ\| ≤ 1.98 MHz | 30 kHz | -42 dB | -70.13 dBm |
| 1.98 MHz ≤ \|Δƒ\| ≤ 4 MHz | 30 kHz | -54 dB | -70.13 dBm |

SEM Limits for Band Classes 1 and 4

| Offset Segment | RBW | Relative Mask Limit | Absolute Mask Limit |
| --- | --- | --- | --- |
| 1.25 MHz ≤ \|Δƒ\| ≤ 1.98 MHz | 30 kHz | -42 dB | -70.13 dBm |
| 1.98 MHz ≤ \|Δƒ\| ≤ 4 MHz | 30 kHz | -50 dB | -70.13 dBm |

SEM Limits for Band Classes 6, 8, and 13

| Offset Segment | RBW | Relative Mask Limit | Absolute Mask Limit |
| --- | --- | --- | --- |
| 1.25 MHz ≤ \|Δƒ\| ≤ 1.98 MHz | 30 kHz | -42 dB | -70.13 dBm |
| 1.98 MHz ≤ \|Δƒ\| ≤ 2.25 MHz | 30 kHz | -50 dB | -70.13 dBm |
| 2.25 MHz ≤ \|Δƒ\| ≤ 4 MHz | 1 MHz | n/a | -13 dBm to -14.75 dBm |

SEM Limits for Band Class 7

| Offset Segment | RBW | Relative Mask Limit | Absolute Mask Limit |
| --- | --- | --- | --- |
| 885 kHz ≤ \|Δƒ\| ≤ 1.98 MHz | 30 kHz | -42 dB | -70.13 dBm |
| 1.98 MHz ≤ \|Δƒ\| ≤ 2.25 MHz | 30 kHz | -54 dB | -70.13 dBm |
| 2.25 MHz ≤ \|Δƒ\| ≤ 4 MHz | 6.25 kHz | n/a | -35 dBm |

SEM Limits for Band Class 10

| Offset Segment | RBW | Relative Mask Limit | Absolute Mask Limit |
| --- | --- | --- | --- |
| 885 kHz ≤ \|Δƒ\| ≤ 1.25 MHz | 30 kHz | -42 dB | -70.13 dBm |
| 1.25 MHz ≤ \|Δƒ\| ≤ 4 MHz | 30 kHz | n/a | -13 dBm |

RFmx EV-DO SEM measurements for Band Class 3 differ from the SEM
 measurements for all other band classes because the offset segment
 definitions depend on the absolute measurement frequency as shown in
 the following table.

SEM Limits for Band Class 3

| Measurement Frequency | Offset Segment | RBW | Relative Mask Limit | Absolute Mask Limit |
| --- | --- | --- | --- | --- |
| 815 MHz < ƒ ≤ 850 MHz 893 MHz < ƒ ≤ 901 MHz 893 MHz < ƒ ≤ 850 MHz 915 MHz < ƒ ≤ 925 MHz | 900 kHz ≤ \|Δƒ\| ≤ 1.98 MHz | 30 kHz | -42 dB | n/a |
| 1.98 kHz ≤ \|Δƒ\| ≤ 4 MHz | 100 kHz | n/a | -16 dBm |  |
| 885 MHz < ƒ ≤ 958 MHz excluding: 887 MHz < ƒ ≤ 889 MHz 893 MHz < ƒ ≤ 901 MHz 915 MHz < ƒ ≤ 925 MHz | 0 kHz ≤ \|Δƒ\| ≤ 1.98 MHz | 30 kHz | n/a | -16 dBm |
| 1.98 kHz ≤ \|Δƒ\| ≤ 4 MHz | 100 kHz | n/a | -16 dBm |  |
| ƒ ≤ 958 MHz 958 MHz < ƒ excluding: 815 MHz < ƒ ≤ 850 MHz | 0 kHz ≤ \|Δƒ\| ≤ 1.98 MHz | 30 kHz | n/a | -16 dBm |
| 1.98 kHz ≤ \|Δƒ\| ≤ 4 MHz | 1 MHz | n/a | -16 dBm |  |

#### Multicarrier Offset Segments and Limit Masks

Multicarrier (MC) EV-DO SEM measurements use predefined definitions for
 the offset segments to measure and for the applied limit masks for
 these offset segments. The offset segments are defined by the
 measurement offset frequency Δf, where
 Δf refers to the difference between the
 middle frequency of the multicarrier signal and the closer
 measurement edge frequency, or the edge of the RBW filter.

The offset segment definitions and corresponding emission limits for MC
 operation are listed in the following tables.

SEM Limits for MC Operation with Number of Carriers
 N = 3 for All Band Classes except
 Band Class 6

| Offset Segment | RBW | Relative Mask Limit | Absolute Mask Limit |
| --- | --- | --- | --- |
| 2.5 MHz ≤ \|Δƒ\| ≤ 2.7 MHz | 30 kHz | n/a | -14 dBm |
| 2.7 MHz ≤ \|Δƒ\| ≤ 3.5 MHz | 30 kHz | n/a | -14 dBm to -26 dBm |
| 3.5 MHz ≤ \|Δƒ\| ≤ 7.5 MHz | 1 MHz | n/a | -13 dBm to -17 dBm |
| 7.5 MHz ≤ \|Δƒ\| ≤ 8.5 MHz | 1 MHz | n/a | -17 dBm to -27 dBm |
| 8.5 MHz ≤ \|Δƒ\| ≤ 12.5 MHz | 1 MHz | n/a | -27 dBm |

SEM Limits for MC operation number of carriers N=3 for
 Band Class 6

| Offset Segment | RBW | Relative Mask Limit | Absolute Mask Limit |
| --- | --- | --- | --- |
| 2.5 MHz ≤ \|Δƒ\| ≤ 2.7 MHz | 30 kHz | n/a | -14 dBm |
| 2.7 MHz ≤ \|Δƒ\| ≤ 3.5 MHz | 30 kHz | n/a | -14 dBm to -26 dBm |
| \|Δƒ\| = 3.08 MHz | 3.84 MHz | -33 dB | n/a |
| 3.5 MHz ≤ \|Δƒ\| ≤ 7.5 MHz | 1 MHz | n/a | -13 dBm to -17 dBm |
| 7.5 MHz ≤ \|Δƒ\| ≤ 8.5 MHz | 1 MHz | n/a | -17 dBm to -27 dBm |
| \|Δƒ\| = 8.08 MHz | 3.84 MHz | -43 dB | n/a |
| 8.5 MHz ≤ \|Δƒ\| ≤ 12.5 MHz | 1 MHz | n/a | -27 dBm |

SEM Limits for MC Operation with Number of Carriers
 N≠ 3 for All Band
 Classes

| Offset Segment | RBW | Relative Mask Limit | Absolute Mask Limit |
| --- | --- | --- | --- |
| (2.5+(N-3)·0.625) MHz ≤ \|Δƒ\| ≤ (3.5+(N·-3)·0.625) MHz | (12.5·N) kHz | n/a | -13 dBm |
| (3.5+(N-3)·0.625) MHz ≤ \|Δƒ\| ≤ (3.125·(N+1)) MHz | 1 MHz | n/a | -13 dBm |

Related information:

- SEM

<!--NI_TOPIC bundle=rfmx-evdo path=modacc-interval.html language=enus -->
## TOPIC 00009: Measurement Interval

- bundle_id: `rfmx-evdo`
- source_path: `modacc-interval.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo/raw/resource/enus/modacc-interval.html
- document_id: `rfmx-evdo`
- page_type: `leaf`
- content_type: `concept`
- source_description: RFmx EV-DO determines the measurement interval used for modulation accuracy (ModAcc) measurements using the following values. You can configure the values independently or use the ModAcc Configure Synchronization Mode and Interval VI/function to configure them at the same time. Interval Start—Specif

### Measurement Interval

RFmx EV-DO determines the measurement interval used for modulation accuracy (ModAcc)
 measurements using the following values. You can configure the values independently or
 use the ModAcc Configure Synchronization Mode and Interval VI/function to configure them
 at the same time.

- Interval Start —Specifies the offset in slots relative to a
 synchronization event. The synchronization event is configurable as the first
 detected symbol, slot, or frame boundary within the acquired signal. Each
 synchronization mode synchronizes to a chip offset relative to the frame start as an
 integer multiple of the following sizes: Configure the interval start using the Measurement Offset (slots) property.
  - Symbol synchronization —64 chips
  - Slot synchronization —2048 chips
  - Frame synchronization —32,768 chips
- Interval Duration —Specifies the length of the signal to be
 analyzed. This length is expressed in slots. Configure the interval duration using
 the Measurement Length (slots) property.

Note

<!--NI_TOPIC bundle=rfmx-evdo path=modacc-subtypes.html language=enus -->
## TOPIC 00010: Supported Physical Layer Subtypes

- bundle_id: `rfmx-evdo`
- source_path: `modacc-subtypes.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo/raw/resource/enus/modacc-subtypes.html
- document_id: `rfmx-evdo`
- page_type: `leaf`
- content_type: `concept`
- source_description: Modulation accuracy (ModAcc) measurement for RFmx EV-DO supports the following physical layer subtypes: 0/1 2 3

### Supported Physical Layer Subtypes

Modulation accuracy (ModAcc) measurement for RFmx EV-DO supports the following physical
 layer subtypes:

- 0/1
- 2
- 3

<!--NI_TOPIC bundle=rfmx-evdo path=new-features-and-changes.html language=enus -->
## TOPIC 00011: RFmx EV-DO New Features and Changes

- bundle_id: `rfmx-evdo`
- source_path: `new-features-and-changes.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo/raw/resource/enus/new-features-and-changes.html
- document_id: `rfmx-evdo`
- page_type: `leaf`
- content_type: `concept`
- source_description: Learn about updates, including new features and behavior changes, introduced in each version of RFmx EV-DO. Discover what is new in the latest releases of RFmx EV-DO.If you cannot find new features and changes for your version, it might not include user-facing updates. However, your version might in

### RFmx EV-DO
 New Features and Changes

Learn about updates, including new features and behavior changes, introduced in each
 version of RFmx EV-DO.

RFmx EV-DO

Note

Release Notes

Related information:

- Software and Driver Downloads

#### RFmx EV-DO
 2026 Q2 Changes

The RFmx EV-DO 2026 Q2 release updates Adjacent Channel
 Power (ACP) to allow more than one analysis thread with the Sequential FFT method and adds
 support for PXIe-5841 (200 MHz bandwidth) hardware.

##### Behavior Changes

This version of RFmx EV-DO updates support for the following feature:

- Adjacent Channel Power (ACP): Configuring the Number of Analysis
 Threads property to a value greater than 1 is allowed when using
 the Sequential FFT measurement method.

##### New
 Hardware Support

This version of RFmx EV-DO
 adds support for the following hardware:

- PXIe-5841 ( 200 MHz ) bandwidth

#### RFmx EV-DO
 2025 Q3 Changes

Learn about new features, behavior changes, and other updates in RFmx EV-DO 2025 Q3.

##### New
 Features

This version of the RFmx EV-DO
 adds support for the following features:

- PXIe-5860 Self-Cal Validity Check

#### RFmx EV-DO
 2024 Q4 Changes

Learn about new features, behavior changes, and other updates in RFmx EV-DO 2024 Q4.

##### New
 Features

This version of the RFmx EV-DO
 adds support for the following features:

- Uninstalling RFmx EV-DO software also removes any
 previous versions of RFmx EV-DO .NET runtimes that
 were leaked in .NET Global Assembly Cache directory.

#### RFmx EV-DO
 2024 Q3 Changes

Learn about new features, behavior changes, and other updates in RFmx EV-DO 2024 Q3.

##### New
 Hardware Support

This version of the RFmx EV-DO adds support for the following
 hardware:

- PXIe-5860

#### RFmx EV-DO
 2024 Q2 Changes

Learn about new features, behavior changes, and other updates in RFmx EV-DO 2024 Q2.

- Obsoleted the RFmxInstr Load All Configurations VI. Use the
 RFmxInstr Load Configurations VI along with the appropriate
 RFmxInstr Load Options property, instead.

#### RFmx EV-DO 2023 Q4 New Features and
 Changes

- Support for obtaining unprocessed I/Q data utilized for RFmx measurements

#### RFmx EV-DO 2023 Q2 New Features and
 Changes

- Speed improvements for Composite and Spectral measurements

#### RFmx EV-DO 2023 Q1 New Features and
 Changes

- Support for LabVIEW 2023 Q1 (64-bit)

<!--NI_TOPIC bundle=rfmx-evdo path=rfmxevdo-overview.html language=enus -->
## TOPIC 00012: RFmx EV-DO Overview

- bundle_id: `rfmx-evdo`
- source_path: `rfmxevdo-overview.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo/raw/resource/enus/rfmxevdo-overview.html
- document_id: `rfmx-evdo`
- page_type: `leaf`
- content_type: `concept`
- source_description: This user manual contains introduction to RFmx EV-DO measurement concepts.

### RFmx EV-DO Overview

This user manual contains introduction to RFmx EV-DO measurement concepts.

<!--NI_TOPIC bundle=rfmx-evdo path=slot-phase-measurement-interval.html language=enus -->
## TOPIC 00013: Slot Phase Measurement Interval

- bundle_id: `rfmx-evdo`
- source_path: `slot-phase-measurement-interval.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo/raw/resource/enus/slot-phase-measurement-interval.html
- document_id: `rfmx-evdo`
- page_type: `leaf`
- content_type: `concept`
- source_description: The measurement interval for which the Slot Phase metrics are calculated is given by: - Start of the interval defined by an offset, in slots, relative to a synchronization event where the synchronization event can be configured to be at the first detected slot or frame boundary within the acquired s

### Slot Phase Measurement Interval

The measurement interval for which the Slot Phase metrics are calculated is given by:

- Start of the interval defined by an offset, in slots, relative to a synchronization event
 where the synchronization event can be configured to be at the first detected slot or frame
 boundary within the acquired signal. The synchronization event the offset refers to is
 configured by the SlotPhase Synchronization Mode property which can be set to
 Slot and Frame referring to slot and frame
 synchronization where:

- Slot synchronization refers to the synchronization to the first detected slot boundary
 within the acquired signal, where a slot is defined as a segment of the signal having a
 duration of 1.667 ms or equally 2048 chips. That is, slot synchronization synchronizes to a
 chip offset relative to the frame start being an integer multiple of 2048 chips.
- Frame synchronization refers to the synchronization to the first detected frame boundary
 within the acquired signal where a frame is defined as the segment of the signal having a
 duration 26.67 ms or equally 16 slots or 32768 chips.

The offset is configured by the SlotPhase Measurement Offset property.

- Duration of the interval configured as length in terms of slots. The duration is configured
 by the Measurement Length property.

<!--NI_TOPIC bundle=rfmx-evdo path=slot-phase-measures.html language=enus -->
## TOPIC 00014: Slot Phase Measures

- bundle_id: `rfmx-evdo`
- source_path: `slot-phase-measures.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo/raw/resource/enus/slot-phase-measures.html
- document_id: `rfmx-evdo`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Slot Phase Measurement calculates the following results and traces: - Chip Phase Error: Returns the chip phase error measured and reference signal as a trace in degrees. - Chip Phase Error Linear Fit: Returns the per-half-slot linear interpolation of Chip Phase Error as a trace in degrees. - Hal

### Slot Phase Measures

The Slot Phase Measurement calculates the following results and traces:

- Chip Phase Error: Returns the chip phase error measured and reference signal as a
 trace in degrees.

- Chip Phase Error Linear Fit: Returns the per-half-slot linear interpolation of Chip
 Phase Error as a trace in degrees.

- Half Slot Phase Discontinuity: Returns the phase difference of Chip Phase Error Linear
 Fit between the last chip in a half-slot and the first chip in the subsequent half-slot
 in degrees.

- SlotPhase Results Max Half Slot Phase Disc: Returns the maximum value of Half Slot
 Phase Discontinuity within the measured signal.

<!--NI_TOPIC bundle=rfmx-evdo path=slot-phase-overview.html language=enus -->
## TOPIC 00015: Slot Phase Overview

- bundle_id: `rfmx-evdo`
- source_path: `slot-phase-overview.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo/raw/resource/enus/slot-phase-overview.html
- document_id: `rfmx-evdo`
- page_type: `leaf`
- content_type: `concept`
- source_description: The slot phase measurement determines the phase discontinuity between any adjacent half slots in an EV-DO signal and can be used to check phase change within the signal when closed-loop power control is used on the reverse link. The phase discontinuity at a specific half-slot boundary is calculated

### Slot Phase Overview

The slot phase measurement determines the phase discontinuity between any adjacent half
 slots in an EV-DO signal and can be used to check phase change within the signal when
 closed-loop power control is used on the reverse link.

The phase discontinuity at a specific half-slot boundary is calculated as the difference
 of the extrapolated phase error at the end of the half-slot preceding the half-slot
 boundary and the extrapolated phase error at the start of the half-slot following the
 half-slot boundary. The extrapolated phase error for each half-slot is calculated by
 linear interpolation of the individual chip phase errors of that half-slot excluding a
 transient period on either side of the half-slot boundary.

The chip phase errors subject to the interpolation process are determined as the phase
 differences of the chip phase of the signal to measure and the chip phase of the ideal
 reference signal. The transient duration can be configured by the SlotPhase Transient
 Duration property.

<!--NI_TOPIC bundle=rfmx-evdo path=slot-phase-subtypes.html language=enus -->
## TOPIC 00016: Supported Physical Layer Subtypes

- bundle_id: `rfmx-evdo`
- source_path: `slot-phase-subtypes.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo/raw/resource/enus/slot-phase-subtypes.html
- document_id: `rfmx-evdo`
- page_type: `leaf`
- content_type: `concept`
- source_description: Slot Phase measurement for EV-DO supports physical layer subtypes 0/1, 2, and 3.

### Supported Physical Layer Subtypes

Slot Phase measurement for EV-DO supports physical layer subtypes 0/1, 2, and 3.

<!--NI_TOPIC bundle=rfmx-evdo path=slot-power-measurement-interval.html language=enus -->
## TOPIC 00017: Slot Power Measurement Interval

- bundle_id: `rfmx-evdo`
- source_path: `slot-power-measurement-interval.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo/raw/resource/enus/slot-power-measurement-interval.html
- document_id: `rfmx-evdo`
- page_type: `leaf`
- content_type: `concept`
- source_description: The measurement interval for which the Slot Power metrics are calculated is defined by: The start of the interval is defined by an offset, in slots, relative to a synchronization event, where the synchronization event can be configured to be at the first detected slot or the frame boundary within th

### Slot Power Measurement Interval

The measurement interval for which the Slot Power metrics are calculated is defined
 by:

- The start of the interval is defined by an offset, in slots, relative to a
 synchronization event, where the synchronization event can be configured to be at
 the first detected slot or the frame boundary within the acquired signal. The
 synchronization event that the offset refers to, is configured by the SlotPower
 Synchronization Mode property which can be set to Slot and
 Frame referring to slot and frame synchronization where:
  - Slot synchronization refers to the synchronization to the first detected
 slot boundary within the acquired signal, where a slot is defined as a
 segment of the signal having a duration of 1.667 ms or equally 2048 chips.
 That is, slot synchronization synchronizes to a chip offset relative to the
 frame start being an integer multiple of 2048 chips.
  - Frame synchronization refers to the synchronization to the first detected
 frame boundary within the acquired signal where a frame is defined as the
 segment of the signal having a duration 26.67 ms or equally 16 slots or
 32768 chips.
- The offset is configured by the SlotPower Measurement Offset property.
- Duration of the interval configured as length in terms of slots. The duration is
 configured by the Measurement Length property.

<!--NI_TOPIC bundle=rfmx-evdo path=slot-power-measures.html language=enus -->
## TOPIC 00018: Slot Power Measures

- bundle_id: `rfmx-evdo`
- source_path: `slot-power-measures.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo/raw/resource/enus/slot-power-measures.html
- document_id: `rfmx-evdo`
- page_type: `leaf`
- content_type: `concept`
- source_description: The slot power measurement is used to determine power values per half-slot in a EV-DO signal and can be used to measure closed-loop power control patterns of the reverse link. The reverse link of EV-DO employs closed-loop power control with a rate of 800 Hz. Due to the possibility of channels shifte

### Slot Power Measures

The slot power measurement is used to determine power values per half-slot in a EV-DO
 signal and can be used to measure closed-loop power control patterns of the reverse
 link. The reverse link of EV-DO employs closed-loop power control with a rate of 800 Hz.
 Due to the possibility of channels shifted by a half-slot, the EV-DO slot power
 measurement runs on a half-slot basis.

The Slot Power Measurement calculates the following result traces:

- Half Slot Power: Returns an array of absolute powers, in dBm, for all half-slots
 within the measurement length
- Half Slot Power Delta: Returns an array of power differences of adjacent half-slots
 in dB.

<!--NI_TOPIC bundle=rfmx-evdo path=slot-power-subtypes.html language=enus -->
## TOPIC 00019: Supported Physical Layer Subtypes

- bundle_id: `rfmx-evdo`
- source_path: `slot-power-subtypes.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo/raw/resource/enus/slot-power-subtypes.html
- document_id: `rfmx-evdo`
- page_type: `leaf`
- content_type: `concept`
- source_description: Slot Power measurement for EV-DO supports physical layer subtypes 0/1, 2, and 3.

### Supported Physical Layer Subtypes

Slot Power measurement for EV-DO supports physical layer subtypes 0/1, 2, and 3.

<!--NI_TOPIC bundle=rfmx-evdo path=supported-hw.html language=enus -->
## TOPIC 00020: Supported Hardware

- bundle_id: `rfmx-evdo`
- source_path: `supported-hw.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo/raw/resource/enus/supported-hw.html
- document_id: `rfmx-evdo`
- page_type: `leaf`
- content_type: `concept`
- source_description: RFmx supports a number of NI devices. 1 RFmx EV-DO Supported Hardware RFmx EV-DO Hardware Earliest Driver Version Support (Windows 11) PXIe-5644 2022 Q3 PXIe-5645 2022 Q3 PXIe-5646 2022 Q3 PXIe-5663 2022 Q3 PXIe-5665 2022 Q3 PXIe-5668 2022 Q3 PXIe-5820 2022 Q3 PXIe-5840 2022 Q3 PXIe-5841 (1 GHz Band

### Supported Hardware

RFmx supports a number of NI devices.

| RFmx EV-DO Hardware | Earliest Driver Version Support (Windows 11) |
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
| PXIe-5841 (200 MHz Bandwidth) | 2026 Q2 |
| PXIe-5842 | 2022 Q4 |
| PXIe-5860 | 2024 Q3 |

Note

RFmx EV-DO

NI-RFSA
 Properties

NI-RFSA LabVIEW VI Reference

For more information about your hardware and functionality, refer to the *NI-RFSA User Manual*.

<!--NI_TOPIC bundle=rfmx-evdo path=system-requirements.html language=enus -->
## TOPIC 00021: RFmx EV-DO System Requirements

- bundle_id: `rfmx-evdo`
- source_path: `system-requirements.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo/raw/resource/enus/system-requirements.html
- document_id: `rfmx-evdo`
- page_type: `leaf`
- content_type: `concept`
- source_description: RFmx EV-DO has the following requirements: Processor—1 GHz 64-bit (x64) processor 4 GB RAM * A screen resolution of 1,024 x 768 Any supported OS, with all available critical updates and service packs * Depending on the amount of data acquired and/or processed, a larger amount of memory may be requir

### RFmx EV-DO System Requirements

RFmx EV-DO has the following requirements:

- Processor—1 GHz 64-bit (x64) processor
- 4 GB RAM *
- A screen resolution of 1,024 x 768
- Any supported OS, with all available critical updates and service packs

* Depending on the amount of data acquired and/or processed, a larger amount of memory
 may be required.

<!--NI_TOPIC bundle=rfmx-evdo path=user-manual-welcome.html language=enus -->
## TOPIC 00022: RFmx EV-DO User Manual

- bundle_id: `rfmx-evdo`
- source_path: `user-manual-welcome.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo/raw/resource/enus/user-manual-welcome.html
- document_id: `rfmx-evdo`
- page_type: `leaf`
- content_type: `concept`
- source_description: The RFmx EV-DO User Manual provides detailed descriptions of the product functionality and the step by step processes for use. Looking for Something Else?For information not found in the User Manual for your product, such as specifications and API reference, browse Related Information.

### RFmx EV-DO
 User Manual

The RFmx EV-DO User Manual provides detailed
 descriptions of the product functionality and the step by step processes for use.

#### Looking for Something Else?

For information not found in the User Manual
 for your product, such as specifications and API reference, browse *Related
 Information*.

Related information:

- Download RFmx EV-DO
- License Setup and Activation
- RFmx EV-DO Release Notes
- Getting Started with RFmx
- RFmx EV-DO LabVIEW Reference
- RFmx EV-DO .NET Reference
- RFmx EV-DO C Reference
- RFmx Instr LabVIEW Reference
- RFmx Instr .NET Reference
- RFmx Instr C Reference
