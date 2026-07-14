# NI DOCUMENT BUNDLE: rfmx-cdma2k

<!--NI_BUNDLE_CHUNK bundle=rfmx-cdma2k start=1 end=32 -->
<!--NI_TOPIC bundle=rfmx-cdma2k path=auto-detection-capabilities.html language=enus -->
## TOPIC 00001: Auto Detection Capabilities

- bundle_id: `rfmx-cdma2k`
- source_path: `auto-detection-capabilities.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k/raw/resource/enus/auto-detection-capabilities.html
- document_id: `rfmx-cdma2k`
- page_type: `leaf`
- content_type: `concept`
- source_description: CDMA2k CDA supports auto detection of the active physical channels by setting the Channel Configuration Mode property to Auto Detect.

### Auto Detection Capabilities

CDMA2k CDA supports auto detection of the active physical channels by setting the Channel
 Configuration Mode property to Auto Detect.

<!--NI_TOPIC bundle=rfmx-cdma2k path=cda-measurement-interval.html language=enus -->
## TOPIC 00002: CDA Measurement Interval

- bundle_id: `rfmx-cdma2k`
- source_path: `cda-measurement-interval.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k/raw/resource/enus/cda-measurement-interval.html
- document_id: `rfmx-cdma2k`
- page_type: `leaf`
- content_type: `concept`
- source_description: RFmx CDMA2k determines the measurement interval of modulation accuracy metrics using the following values. Interval start—Configure the start of the measurement interval using the offset relative to a synchronization event. The synchronization event can be configured as the first detected symbol, sl

### CDA Measurement Interval

RFmx CDMA2k determines the measurement interval of modulation accuracy metrics using the
 following values.

- Interval start —Configure the start of the measurement
 interval using the offset relative to a synchronization event. The synchronization
 event can be configured as the first detected symbol, slot, or frame boundary within
 the acquired signal. This value is expressed in slots. Configure the mode of
 synchronization event using the CDA Sync Mode property. This property can be set
 to Arbitrary, Slot, or
 Frame based on the following type of
 synchronizations. 
 Configure the offset using the CDA Meas Offset property.
  - Symbol synchronization —The synchronization event is configured as
 the first detected symbol boundary within the acquired signal. In this case,
 symbol refers to the symbols with the largest spreading factor, which is 64
 chips. Symbol synchronization synchronizes to a chip offset relative to the
 frame start which is an integer multiple of 64 chips.
  - Slot synchronization —The synchronization event is
 configured as the first detected slot boundary within the acquired signal. A
 slot is a segment of a signal having a length equal to the duration of a
 power control group (PCG) of 1.25 ms or 1536 chips. Slot synchronization
 synchronizes to a chip offset relative to the frame start being an integer
 multiple of 1536 chips.
  - Frame synchronization —The synchronization event
 configured as the first detected frame boundary within the acquired signal.
 The R-FCH frame duration is 20ms, 16 slots, or 24576 chips.
- Interval duration —Specifies the length of the signal to be
 analyzed. This value is expressed in slots. Configure the interval duration using
 the Measurement Length property.

<!--NI_TOPIC bundle=rfmx-cdma2k path=cda-modacc.html language=enus -->
## TOPIC 00003: CDA Modulation Accuracy Measurements for Selected Code Channel

- bundle_id: `rfmx-cdma2k`
- source_path: `cda-modacc.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k/raw/resource/enus/cda-modacc.html
- document_id: `rfmx-cdma2k`
- page_type: `leaf`
- content_type: `concept`
- source_description: CDA provides the ability to analyze the modulation accuracy for a specific user-configurable code channel. The code channel, which has to be analyzed, is configured using the spreading factor, channelization code, and branch using the CDA Meas Ch Walsh Code Length, CDA Meas Ch Walsh Code Number Code

### CDA Modulation Accuracy Measurements for Selected Code Channel

CDA provides the ability to analyze the modulation accuracy for a specific
 user-configurable code channel. The code channel, which has to be analyzed, is
 configured using the spreading factor, channelization code, and branch using the CDA
 Meas Ch Walsh Code Length, CDA Meas Ch Walsh Code Number Code, and CDA Meas Ch Branch
 properties respectively.

RFmx CDA measurements compute the following measurements for the selected code
 channel:

- CDA Results RMS Symbol EVM —Returns the RMS symbol EVM for the
 selected channel. This value is expressed as a percentage.
- CDA Results Peak Symbol EVM —Returns the peak symbol EVM for
 the selected channel. This value is expressed as a percentage.
- CDA Results RMS Symbol Magnitude Error —Returns the RMS symbol
 magnitude error for the selected channel. This value is expressed as a
 percentage.
- CDA Results RMS Symbol Phase Error —Returns the RMS symbol
 phase error for the selected channel. This value is expressed in degrees.
- CDA Results Mean Symbol Pwr —Returns the mean symbol power of
 the selected channel.

Additional measurements for I/Q impairments are reported as follows:

- I/Q Origin Offset —Returns the DC Offset of I/Q samples from
 the origin. This value is expressed in dB.
- I/Q Gain Imbalance —Returns the IQ gain imbalance between the
 in-phase and quadrature components within the complex baseband signal. This value is
 expressed in dB.
- I/Q Quadrature Error —Returns the phase difference from ideal
 90 degrees between the in-phase and quadrature components within the complex
 baseband signal. This value is expressed in degrees.

<!--NI_TOPIC bundle=rfmx-cdma2k path=cdma2k-acp.html language=enus -->
## TOPIC 00004: CDMA2k ACP

- bundle_id: `rfmx-cdma2k`
- source_path: `cdma2k-acp.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k/raw/resource/enus/cdma2k-acp.html
- document_id: `rfmx-cdma2k`
- page_type: `leaf`
- content_type: `concept`
- source_description: CDMA2k ACP Offset Channels The RFmx CDMA2k ACP measurement uses predefined configurations derived from the spectral emission limits defined in the 3GPP2 standard. ACP measurements perform offset power measurements of 30 kHz integration bandwidth at specific, band-class-dependent offset frequencies,

### CDMA2k ACP

#### CDMA2k ACP Offset Channels

The RFmx CDMA2k ACP measurement uses predefined configurations derived from the spectral
 emission limits defined in the 3GPP2 standard. ACP measurements perform offset power
 measurements of 30 kHz integration bandwidth at specific, band-class-dependent offset
 frequencies, where offset frequency refers to the difference of the
 carrier center frequency and the closer measurement edge frequency.

The following table defines the ACP measurement according to band class.

| Band Class | Offset Frequency | Integration Bandwidth |
| --- | --- | --- |
| 0,2,5,9,11,12 | ±885 kHz | 30 kHz |
| ±1.98 MHz | 30 kHz |  |
| ±4 MHz | 30 kHz |  |
| 1,4,8,14,15 | ±1.25 MHz | 30 kHz |
| ±1.98 MHz | 30 kHz |  |
| ±4 MHz | 30 kHz |  |
| 3 | ±885 kHz | 30 kHz |
| ±1.98 MHz | 30 kHz |  |
| ±4 MHz | 30 kHz |  |
| 6 | ±1.25 MHz | 30 kHz |
| ±1.98 MHz | 30 kHz |  |
| ±2.25 MHz | 30 kHz |  |
| 7 | ±885 kHz | 30 kHz |
| ±1.98 MHz | 30 kHz |  |
| ±2.25 MHz | 6.25 kHz |  |
| 10 | ±885 kHz | 30 kHz |
| ±1.25 MHz | 30 kHz |  |
| ±4 MHz | 30 kHz |  |

Related information:

- ACP

<!--NI_TOPIC bundle=rfmx-cdma2k path=cdma2k-cda.html language=enus -->
## TOPIC 00005: CDMA2k Code Domain Analysis Measurements

- bundle_id: `rfmx-cdma2k`
- source_path: `cdma2k-cda.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k/raw/resource/enus/cdma2k-cda.html
- document_id: `rfmx-cdma2k`
- page_type: `leaf`
- content_type: `concept`
- source_description: The code domain analysis (CDA) measurement provides measurements in the code domain. It provides code domain power analysis and calculation of modulation accuracy measures for a selected code channel. CDA Code Domain Power Measurements For code domain power measurements, CDA analyzes the code domain

### CDMA2k Code Domain Analysis Measurements

The code domain analysis (CDA) measurement provides measurements in the code domain. It provides code domain power analysis and calculation of modulation accuracy measures for a selected code channel.

#### CDA Code Domain Power Measurements

For code domain power measurements, CDA analyzes the code domain power of one or more slots
 for the configured base spreading factor. Configure the base spreading factor using the CDA
 Base Spreading Factor property.

The measured power values can be configured to be
 absolute power values, in dBm, or relative power values, in dB, with respect to the total
 code domain power using the CDA Pwr Unit property.

RFmx CDMA2k CDA measurements
 compute the following code domain measurements:

- CDA Results Total Pwr —Returns the total code domain power. This
 value is expressed in dBm.
- CDA Results Total Active Pwr —Returns the total active code power
 either as an absolute measure, in dBm, or as a relative measure, in dB.
- CDA Results Mean Active Pwr —Returns the average active code power
 either as an absolute measure, in dBm, or as a relative measure, in dB.
- CDA Results Pk Active Pwr —Returns the maximum power among all
 active code channels either as an absolute measure, in dBm, or as relative measure, in
 dB.
- CDA Results Mean Inactive Pwr —Returns the average code power
 measured among the set of inactive channels either as an absolute measure, in dBm, or as
 relative measure, in dB.
- CDA Results Pk Inactive Pwr —Returns the largest measured code
 power among the set of inactive channels either as an absolute measure, in dBm, or as
 relative measure, in dB.
- CDA Results I Mean Active Pwr —Returns the average power of all
 active code channels measured on the I-branch.
- CDA Results I Pk Inactive Pwr —Returns the largest measured code
 power among the set of inactive channels on the I-branch and in the code domain of the
 base spreading factor.
- CDA Results Q Mean Active Pwr —Returns the average power of all
 active code channels measured on the Q-branch.
- CDA Results Q Pk Inactive Pwr —Returns the largest measured code
 power among the set of inactive channels on the Q-branch and in the code domain of the
 base spreading factor.

<!--NI_TOPIC bundle=rfmx-cdma2k path=cdma2k-chp.html language=enus -->
## TOPIC 00006: CDMA2k Channel Power (CHP)

- bundle_id: `rfmx-cdma2k`
- source_path: `cdma2k-chp.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k/raw/resource/enus/cdma2k-chp.html
- document_id: `rfmx-cdma2k`
- page_type: `leaf`
- content_type: `concept`
- source_description: The CDMA2k CHP measurement measures the power of the RF signal within the CDMA2k signal bandwidth of 1.2288 MHz.

### CDMA2k Channel Power (CHP)

The CDMA2k CHP measurement measures the power of the RF signal within the CDMA2k signal
 bandwidth of 1.2288 MHz.

Related information:

- CHP

<!--NI_TOPIC bundle=rfmx-cdma2k path=cdma2k-modacc.html language=enus -->
## TOPIC 00007: CDMA2k Modulation Accuracy Measurements

- bundle_id: `rfmx-cdma2k`
- source_path: `cdma2k-modacc.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k/raw/resource/enus/cdma2k-modacc.html
- document_id: `rfmx-cdma2k`
- page_type: `leaf`
- content_type: `concept`
- source_description: RFmx CDMA2k modulation accuracy (ModAcc) measurements calculate the following performance metrics: Rho—Returns the normalized correlation coefficient of the signal to measure the generated reference signal. According to the 3GPP2 specification, Rho is the primary metric to evaluate modulation accura

### CDMA2k Modulation Accuracy Measurements

RFmx CDMA2k modulation accuracy (ModAcc) measurements calculate the following performance
 metrics:

- Rho —Returns the normalized correlation coefficient of the
 signal to measure the generated reference signal. According to the 3GPP2
 specification, Rho is the primary metric to evaluate modulation accuracy.
- RMS EVM —Returns the RMS of the normalized EVM.
- Peak EVM —Returns the peak normalized EVM observed within the
 measurement interval.
- Peak Code Domain Error (CDE) —Returns the largest error among
 the error projected onto the individual codes for a base spreading factor. The base
 spreading factor is the constant 32.
- Peak Active CDE —Returns the maximum CDE among all active code
 channels.
- Frequency Error —Returns the frequency error averaged over all
 measured slots. The frequency error is determined only as an overall metric for the
 analyzed signal.
- Chip Rate Error —Returns the chip rate error. The chip rate
 error is determined only as an overall metric for the analyzed signal.

Additionally, RFmx CDMA2k ModAcc measurements also calculate the following I/Q
 impairments :

- I/Q Origin Offset —Returns the DC offset of the I/Q samples
 from the origin.
- I/Q Gain Imbalance —Returns the I/Q gain imbalance between
 inphase and quadrature component within the complex baseband signal.
- I/Q Quadrature Error —Returns the I/Q quadrature error of the
 composite signal, averaged over all measured slots.

<!--NI_TOPIC bundle=rfmx-cdma2k path=cdma2k-obw.html language=enus -->
## TOPIC 00008: CDMA2k OBW

- bundle_id: `rfmx-cdma2k`
- source_path: `cdma2k-obw.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k/raw/resource/enus/cdma2k-obw.html
- document_id: `rfmx-cdma2k`
- page_type: `leaf`
- content_type: `concept`
- source_description: The CDMA2k OBW measurement measures the occupied signal bandwidth as the bandwidth where 99% of the RF power is concentrated.

### CDMA2k OBW

The CDMA2k OBW measurement measures the occupied signal bandwidth as the bandwidth where
 99% of the RF power is concentrated.

Related information:

- OBW

<!--NI_TOPIC bundle=rfmx-cdma2k path=cdma2k-qevm-averaging.html language=enus -->
## TOPIC 00009: CDMA2k QEVM Averaging

- bundle_id: `rfmx-cdma2k`
- source_path: `cdma2k-qevm-averaging.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k/raw/resource/enus/cdma2k-qevm-averaging.html
- document_id: `rfmx-cdma2k`
- page_type: `leaf`
- content_type: `concept`
- source_description: The QEVM measurement supports averaging of measurement values over a configurable number of averaging iterations. Every measurement result has two corresponding statistical results: Mean—Returns the mean of the specific measurement result over the number of averaging iterations. Maximum—Returns the

### CDMA2k QEVM Averaging

The QEVM measurement supports averaging of measurement values over a configurable number
 of averaging iterations. Every measurement result has two corresponding statistical
 results:

- Mean —Returns the mean of the specific measurement result over
 the number of averaging iterations.
- Maximum —Returns the maximum of the specific measurement
 result over the number of averaging iterations.

The traces of different averaging iterations are not averaged. Only the trace of the last
 iteration is returned.

<!--NI_TOPIC bundle=rfmx-cdma2k path=cdma2k-qevm.html language=enus -->
## TOPIC 00010: CDMA2k QEVM Measurements

- bundle_id: `rfmx-cdma2k`
- source_path: `cdma2k-qevm.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k/raw/resource/enus/cdma2k-qevm.html
- document_id: `rfmx-cdma2k`
- page_type: `leaf`
- content_type: `concept`
- source_description: RFmx CDMA2k QEVM measurements calculate the following performance metrics: RMS EVM—Returns the root mean square of the normalized error vector magnitude. Peak EVM—Returns the peak normalized EVM observed within the measurement interval. Frequency Error—Returns the frequency error averaged over all m

### CDMA2k QEVM Measurements

RFmx CDMA2k QEVM measurements calculate the following performance metrics:

- RMS EVM —Returns the root mean square of the normalized error
 vector magnitude.
- Peak EVM —Returns the peak normalized EVM observed within the
 measurement interval.
- Frequency Error —Returns the frequency error averaged over all
 measured slots. The frequency error is determined only as an overall metric for the
 analyzed signal.
- Chip Rate Error —Returns the chip rate error. The chip rate
 error is determined only as an overall metric for the analyzed signal.

Additionally, RFmx CDMA2k QEVM measurements also calculate the following I/Q impairments
 :

- I/Q Origin Offset —Returns the DC offset of the I/Q samples
 from the origin.
- I/Q Gain Imbalance —Returns the I/Q gain imbalance between
 in-phase and quadrature components within the complex baseband signal.
- I/Q Quadrature Error —Returns the phase difference from the
 ideal 90 degrees between in-phase and quadrature components within the complex
 baseband signal.

<!--NI_TOPIC bundle=rfmx-cdma2k path=cdma2k-sem.html language=enus -->
## TOPIC 00011: CDMA2k SEM

- bundle_id: `rfmx-cdma2k`
- source_path: `cdma2k-sem.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k/raw/resource/enus/cdma2k-sem.html
- document_id: `rfmx-cdma2k`
- page_type: `leaf`
- content_type: `concept`
- source_description: CDMA2k SEM Offset Segments and Limit Masks The RFmx CDMA2k SEM measurement uses predefined definitions for the offset segments to measure as well as the limit masks to apply for these offset segments. The offset segments are defined by the measurement offset frequency Δƒ, where Δƒ is the difference

### CDMA2k SEM

#### CDMA2k SEM Offset Segments and Limit Masks

The RFmx CDMA2k SEM measurement uses predefined definitions for the offset segments to
 measure as well as the limit masks to apply for these offset segments. The offset
 segments are defined by the measurement offset frequency Δƒ, where Δƒ is the difference
 between the carrier center frequency and the closer measurement edge frequency.

The configurations are dependent on band class, as shown in the following spectral
 emission limit tables specified in the 3GPP2 standard.

| Band Class | Offset Segment | RBW | Relative Mask Limit | Absolute Mask Limit |
| --- | --- | --- | --- | --- |
| 0,2,5,9,11,12 | 885 kHz ≤ \|Δƒ\|≤ 1.98 MHz | 30 kHz | -42 dB | -70.13 dBm |
| 1.98 MHz ≤ \|Δƒ\|≤ 4 MHz | 30 kHz | -54 dB | -70.13 dBm |  |
| 1,4,8,14,15 | 1.25 MHz ≤ \|Δƒ\|≤ 1.98 MHz | 30 kHz | -42 dB | -70.13 dBm |
| 1.98 MHz ≤ \|Δƒ\|≤ 4 MHz | 30 kHz | -50 dB | -70.13 dBm |  |
| 3 | 885 kHz ≤ \|Δƒ\|≤ 1.98 MHz | 30 kHz | -42 dB | -70.13 dBm |
| 1.98 MHz ≤ \|Δƒ\|≤ 4 MHz | 30 kHz | -54 dB | — |  |
| 6 | 1.25 MHz ≤ \|Δƒ\|≤ 1.98 MHz | 30 kHz | -42 dB | -70.13 dBm |
| 1.98 MHz ≤ \|Δƒ\|≤ 2.25 MHz | 30 kHz | -50 dB | -70.13 dBm |  |
| 2.25 MHz ≤ \|Δƒ\|≤ 4 MHz | 1 MHz | — | -13 dBm to -14.75 dBm |  |
| 7 | 885 kHz ≤ \|Δƒ\|≤ 1.98 MHz | 30 kHz | -42 dB | -70.13 dBm |
| 1.98 MHz ≤ \|Δƒ\|≤ 2.25 MHz | 30 kHz | -54 dB | -70.13 dBm |  |
| 2.25 MHz ≤ \|Δƒ\|≤ 4 MHz | 6.25 kHz | — | -35 dBm |  |
| 10 | 885 kHz ≤ \|Δƒ\|≤ 1.25 MHz | 30 kHz | -42 dB | -70.13 dBm |
| 1.25 MHz ≤ \|Δƒ\|≤ 4 MHz | 30 kHz | — | -13 dBm |  |

Related information:

- SEM

<!--NI_TOPIC bundle=rfmx-cdma2k path=cdma2k-slotphase.html language=enus -->
## TOPIC 00012: CDMA2k SlotPhase Measurements

- bundle_id: `rfmx-cdma2k`
- source_path: `cdma2k-slotphase.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k/raw/resource/enus/cdma2k-slotphase.html
- document_id: `rfmx-cdma2k`
- page_type: `leaf`
- content_type: `concept`
- source_description: The SlotPhase measurement is used to determine the phase discontinuity between adjacent time slots, or PCGs, in a CDMA2k signal. This measurement can be used to check for phase changes within the signal when a closed-loop power control is used on the reverse link. The phase discontinuity at a specif

### CDMA2k SlotPhase Measurements

The SlotPhase measurement is used to determine the phase discontinuity between adjacent
 time slots, or PCGs, in a CDMA2k signal. This measurement can be used to check for phase
 changes within the signal when a closed-loop power control is used on the reverse
 link.

The phase discontinuity at a specific time slot boundary is calculated as the difference
 between the extrapolated phase error at the end of the time slot preceding the slot
 boundary, and the extrapolated phase error at the start of the time slot following the
 slot boundary.

The extrapolated phase error for each time slot is calculated using the linear
 interpolation of the individual chip phase errors of that time slot, excluding a
 transient period on either side of the slot boundary. The chip phase errors, subject to
 the interpolation process, are determined as the phase differences of the chip phase of
 the signal to be measured and the chip phase of the ideal reference signal. Configure
 the transient duration using SlotPhase Transient Duration property.

RFmx SlotPhase measurements calculate the following results and traces:

- Chip Phase Error —Returns the trace of chip phase error. This
 value is expressed in degrees.
- Chip Phase Error Linear Fit —Returns the trace of per-slot
 linear interpolation of chip phase error. This value is expressed in degrees.
- Slot Phase Discontinuity —Returns the phase difference of Chip
 Phase Error Linear Fit between the last chip in a slot and the first chip in the
 subsequent slot. This value is expressed in degrees.
- SlotPhase Results Max Phase Disc —Returns the maximum value of
 slotphase discontinuity within the measured signal. This value is expressed in
 degrees.

<!--NI_TOPIC bundle=rfmx-cdma2k path=cdma2k-slotpower.html language=enus -->
## TOPIC 00013: CDMA2k SlotPower Measurements

- bundle_id: `rfmx-cdma2k`
- source_path: `cdma2k-slotpower.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k/raw/resource/enus/cdma2k-slotpower.html
- document_id: `rfmx-cdma2k`
- page_type: `leaf`
- content_type: `concept`
- source_description: The SlotPower measurement is used to determine the power values per PCG in a CDMA2k signal. This measurement can be used to measure closed-loop power control patterns of the reverse link. The reverse link of CDMA2k employs closed-loop power control at a rate of 800 Hz, resulting in possible power ch

### CDMA2k SlotPower Measurements

The SlotPower measurement is used to determine the power values per PCG in a CDMA2k
 signal. This measurement can be used to measure closed-loop power control patterns of
 the reverse link. The reverse link of CDMA2k employs closed-loop power control at a rate
 of 800 Hz, resulting in possible power changes from one slot (PCG) to subsequent slot.

RFmx SlotPower measurements calculate the following performance metrics:

- Slot Power —Returns an array of absolute powers for all slots
 within the measurement length. This value is expressed in dBm.
- Slot Power Delta —Returns array of power differences of
 adjacent slots. This value is expressed in dB.

<!--NI_TOPIC bundle=rfmx-cdma2k path=modacc-measurement-interval.html language=enus -->
## TOPIC 00014: Measurement Interval

- bundle_id: `rfmx-cdma2k`
- source_path: `modacc-measurement-interval.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k/raw/resource/enus/modacc-measurement-interval.html
- document_id: `rfmx-cdma2k`
- page_type: `leaf`
- content_type: `concept`
- source_description: RFmx CDMA2k determines the measurement interval for modulation accuracy (ModAcc) measurements using the following values. You can configure the values independently or use the ModAcc Configure and Synchronization Mode and Interval VI/function to configure the values at the same time. Interval start—

### Measurement Interval

RFmx CDMA2k determines the measurement interval for modulation accuracy (ModAcc)
 measurements using the following values. You can configure the values independently or
 use the ModAcc Configure and Synchronization Mode and Interval VI/function to configure
 the values at the same time.

- Interval start —Specifies the offset relative to a
 synchronization event. The synchronization event is configurable as the first
 detected symbol, slot, or frame boundary within the acquired signal. This value is
 expressed in slots. Each synchronization mode synchronizes to a chip offset
 relative to the frame start as an integer multiple of the following sizes: 
 
 Configure the interval start using the Synchronization Mode property and
 Measurement Offset property.
  - Symbol synchronization —64 chips
  - Slot synchronization —1,536 chips
  - Frame synchronization —24,576 chips
- Interval duration —Specifies the length of the signal to be
 analyzed. This value is expressed in slots. Configure the interval duration using
 the Measurement Length property.

<!--NI_TOPIC bundle=rfmx-cdma2k path=modacc-rcs.html language=enus -->
## TOPIC 00015: ModAcc Supported Radio Configurations (RCs)

- bundle_id: `rfmx-cdma2k`
- source_path: `modacc-rcs.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k/raw/resource/enus/modacc-rcs.html
- document_id: `rfmx-cdma2k`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following radio configurations are supported by the modulation accuracy (ModAcc) measurement for the reverse link (uplink): RC1/RC2—These radio configurations employ 64-ary orthogonal modulation. For these radio configurations, one mobile terminal can transmit one reverse fundamental channel (R-

### ModAcc Supported Radio Configurations (RCs)

The following radio configurations are supported by the modulation accuracy (ModAcc)
 measurement for the reverse link (uplink):

- RC1/RC2 —These radio configurations employ 64-ary orthogonal
 modulation. For these radio configurations, one mobile terminal can transmit one
 reverse fundamental channel (R-FCH) and up to seven reverse supplemental code
 channels (R-SCCHs) simultaneously. The ModAcc measurement for RC1/RC2 does not
 support multiple active channels at the same time.
- RC3/RC4 —These radio configurations use binary phase-shift
 keying (BPSK) modulation and orthogonal Walsh spreading. Individual physical
 channels use a specific Walsh code assignment and are mapped to either the in-phase
 or quadrature phase. For these radio configurations, one mobile terminal can
 transmit one R-FCH and up to two R-SCHs simultaneously. The ModAcc measurement for
 RC3/RC4 supports any combination of R-FCH and R-SCHs.

<!--NI_TOPIC bundle=rfmx-cdma2k path=modacc-synchronization.html language=enus -->
## TOPIC 00016: Synchronization

- bundle_id: `rfmx-cdma2k`
- source_path: `modacc-synchronization.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k/raw/resource/enus/modacc-synchronization.html
- document_id: `rfmx-cdma2k`
- page_type: `leaf`
- content_type: `concept`
- source_description: The measurement uses the RFmx CDMA2k scrambling sequence consisting of short and long PN code to synchronize to slot boundaries. The synchronization for signals scrambled with a non-zero long code mask is constrained by the internal scrambling sequence length of 80 ms. If the long code mask of the

### Synchronization

The measurement uses the RFmx CDMA2k scrambling sequence consisting of short and long PN code
 to synchronize to slot boundaries.

Note

<!--NI_TOPIC bundle=rfmx-cdma2k path=new-features-and-changes.html language=enus -->
## TOPIC 00017: RFmx CDMA2k New Features and Changes

- bundle_id: `rfmx-cdma2k`
- source_path: `new-features-and-changes.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k/raw/resource/enus/new-features-and-changes.html
- document_id: `rfmx-cdma2k`
- page_type: `leaf`
- content_type: `concept`
- source_description: Learn about updates, including new features and behavior changes, introduced in each version of RFmx CDMA2k. Discover what is new in the latest releases of RFmx CDMA2k.If you cannot find new features and changes for your version, it might not include user-facing updates. However, your version might

### RFmx CDMA2k
 New Features and Changes

Learn about updates, including new features and behavior changes, introduced in each
 version of RFmx CDMA2k.

RFmx CDMA2k

Note

Release Notes

Related information:

- Software and Driver Downloads

#### RFmx CDMA2k
 2026 Q2 Changes

RFmx CDMA2k 2026 Q2 includes behavior changes with ACP
 measurements that use the Sequential FFT measurement method.

##### Behavior Changes

This version of RFmx CDMA2k updates support for the following feature:

- Adjacent Channel Power (ACP): When you use the Sequential FFT 
 measurement method, you can configure the Configuring the Number of
 Analysis Threads property to a value greater than 1.

#### RFmx CDMA2k
 2025 Q3 Changes

Learn about new features, behavior changes, and other updates in RFmx CDMA2k 2025 Q3.

##### New
 Features

This version of the RFmx CDMA2k
 adds support for the following features:

- PXIe-5860 Self-Cal Validity Check

#### RFmx CDMA2k
 2024 Q4 Changes

Learn about new features, behavior changes, and other updates in RFmx CDMA2k 2024 Q4.

##### New
 Features

This version of the RFmx CDMA2k
 adds support for the following features:

- Uninstalling RFmx CDMA2k software also removes any
 previous versions of RFmx CDMA2k .NET runtimes that
 were leaked in .NET Global Assembly Cache directory.

#### RFmx CDMA2k
 2024 Q2 Changes

Learn about new features, behavior changes, and other updates in RFmx CDMA2k 2024 Q2.

- Obsoleted the RFmxInstr Load All Configurations VI. Use the
 RFmxInstr Load Configurations VI along with the appropriate
 RFmxInstr Load Options property, instead.

#### RFmx CDMA2k 2023 Q4 New Features and Changes

- Support for obtaining unprocessed I/Q data utilized for RFmx measurements

#### RFmx CDMA2k 2023 Q2 New Features and
 Changes

- Speed improvements for Composite and Spectral measurements

#### RFmx CDMA2k 2023 Q1 New Features and
 Changes

- Support for LabVIEW 2023 Q1 (64-bit)

<!--NI_TOPIC bundle=rfmx-cdma2k path=qevm-measurement-interval.html language=enus -->
## TOPIC 00018: QEVM Measurement Interval

- bundle_id: `rfmx-cdma2k`
- source_path: `qevm-measurement-interval.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k/raw/resource/enus/qevm-measurement-interval.html
- document_id: `rfmx-cdma2k`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Meas Length property defines the measurement interval on which the QEVM measurement results are based.

### QEVM Measurement Interval

The Meas Length property defines the measurement interval on which the QEVM measurement
 results are based.

<!--NI_TOPIC bundle=rfmx-cdma2k path=qevm-rcs.html language=enus -->
## TOPIC 00019: QEVM Supported Radio Configurations

- bundle_id: `rfmx-cdma2k`
- source_path: `qevm-rcs.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k/raw/resource/enus/qevm-rcs.html
- document_id: `rfmx-cdma2k`
- page_type: `leaf`
- content_type: `concept`
- source_description: The QEVM measurement for the reverse link and uplink supports the following radio configurations: RC1/RC2—These radio configurations use the 64-ary orthogonal modulation. For these radio configurations, one R-FCH and up to seven R-SCCHs can be transmitted simultaneously from one mobile terminal. The

### QEVM Supported Radio Configurations

The QEVM measurement for the reverse link and uplink supports the following radio
 configurations:

- RC1/RC2 —These radio configurations use the 64-ary orthogonal
 modulation. For these radio configurations, one R-FCH and up to seven R-SCCHs can be
 transmitted simultaneously from one mobile terminal. The modulation scheme used in
 RC1/RC2 is Offset-QPSK. The QEVM measurement supports only channel configurations
 that result in an O-QPSK constellation diagram. For example, R-FCH.
- RC3/RC4 —These radio configurations use BPSK modulation and
 orthogonal Walsh spreading codes. Individual physical channels use a specific Walsh
 code and are mapped to either the inphase or quadrature phase. For these radio
 configurations, one R-FCH and up to two R-SCHs can be transmitted simultaneously
 from one mobile terminal. The QEVM measurement supports only channel configurations
 that result in a QPSK constellation diagram. For example, R-PICH.

<!--NI_TOPIC bundle=rfmx-cdma2k path=qevm-supported-spreading-rates.html language=enus -->
## TOPIC 00020: QEVM Supported Spreading Rates

- bundle_id: `rfmx-cdma2k`
- source_path: `qevm-supported-spreading-rates.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k/raw/resource/enus/qevm-supported-spreading-rates.html
- document_id: `rfmx-cdma2k`
- page_type: `leaf`
- content_type: `concept`
- source_description: QEVM measurement only supports a spreading rate of 1 (SR1).

### QEVM Supported Spreading Rates

QEVM measurement only supports a spreading rate of 1 (SR1).

<!--NI_TOPIC bundle=rfmx-cdma2k path=rfmxcdma2k-overview.html language=enus -->
## TOPIC 00021: RFmx CDMA2k Overview

- bundle_id: `rfmx-cdma2k`
- source_path: `rfmxcdma2k-overview.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k/raw/resource/enus/rfmxcdma2k-overview.html
- document_id: `rfmx-cdma2k`
- page_type: `leaf`
- content_type: `concept`
- source_description: This user manual contains introduction to RFmx CDMA2k measurement concepts.

### RFmx CDMA2k Overview

This user manual contains introduction to RFmx CDMA2k measurement concepts.

<!--NI_TOPIC bundle=rfmx-cdma2k path=slotphase-measurement-interval.html language=enus -->
## TOPIC 00022: SlotPhase Measurement Interval

- bundle_id: `rfmx-cdma2k`
- source_path: `slotphase-measurement-interval.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k/raw/resource/enus/slotphase-measurement-interval.html
- document_id: `rfmx-cdma2k`
- page_type: `leaf`
- content_type: `concept`
- source_description: RFmx CDMA2k determines the measurement interval of SlotPhase measurements using the following values. Interval start—Configure the start of the measurement interval using the offset relative to a synchronization event. The synchronization event can be configured as the first detected slot or frame b

### SlotPhase Measurement Interval

RFmx CDMA2k determines the measurement interval of SlotPhase measurements using the
 following values.

- Interval start —Configure the start of the measurement
 interval using the offset relative to a synchronization event. The synchronization
 event can be configured as the first detected slot or frame boundary within the
 acquired signal. This value is expressed in slots. Configure the mode of
 synchronization event using the SlotPhase Sync Mode property. This property can
 be set to Slot or Frame based on
 the following type of synchronizations. 
 Configure the offset using the SlotPhase Meas Offset property.
  - Slot synchronization —The synchronization event is
 configured as the first detected slot boundary within the acquired signal. A
 slot is a segment of a signal having a length equal to the duration of a PCG
 of 1.25 ms or 1536 chips. Slot synchronization synchronizes to a chip offset
 relative to the frame start being an integer multiple of 1536 chips.
  - Frame synchronization —The synchronization event is
 configured as the first detected frame boundary within the acquired signal.
 The R-FCH frame duration is 20ms, 16 slots, or 24576 chips.
- Interval duration —Specifies the length of the signal to be
 analyzed. This value is expressed in slots. Configure the interval duration using
 the SlotPhase Meas Length property.

<!--NI_TOPIC bundle=rfmx-cdma2k path=slotphase-rcs.html language=enus -->
## TOPIC 00023: Supported Radio Configurations (RCs)

- bundle_id: `rfmx-cdma2k`
- source_path: `slotphase-rcs.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k/raw/resource/enus/slotphase-rcs.html
- document_id: `rfmx-cdma2k`
- page_type: `leaf`
- content_type: `concept`
- source_description: Supported Radio Configurations (RCs) The slot phase measurement supports radio configurations RC3-RC4. To comply with the CDMA2k standard, RC1-RC2 are not supported by SlotPhase measurements. The slot phase measures can be determined for arbitrary standard-compliant Walsh code configurations.

### Supported Radio Configurations (RCs)

#### Supported Radio Configurations (RCs)

The slot phase measurement supports radio configurations RC3-RC4. To comply with the
 CDMA2k standard, RC1-RC2 are not supported by SlotPhase measurements. The slot phase
 measures can be determined for arbitrary standard-compliant Walsh code
 configurations.

<!--NI_TOPIC bundle=rfmx-cdma2k path=slotpower-measurement-interval.html language=enus -->
## TOPIC 00024: SlotPower Measurement Interval

- bundle_id: `rfmx-cdma2k`
- source_path: `slotpower-measurement-interval.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k/raw/resource/enus/slotpower-measurement-interval.html
- document_id: `rfmx-cdma2k`
- page_type: `leaf`
- content_type: `concept`
- source_description: RFmx CDMA2k determines the measurement interval of SlotPower measurements using the following values. Interval start—Configure the start of the measurement interval using the offset relative to a synchronization event. The synchronization event can be configured as the first detected slot or frame b

### SlotPower Measurement Interval

RFmx CDMA2k determines the measurement interval of SlotPower measurements using the
 following values.

- Interval start —Configure the start of the measurement
 interval using the offset relative to a synchronization event. The synchronization
 event can be configured as the first detected slot or frame boundary within the
 acquired signal. This value is expressed in slots. Configure the mode of
 synchronization event using the SlotPower Sync Mode property. This property can
 be set to Slot or Frame based on
 the following type of synchronizations. 
 Configure the offset using the SlotPower Meas Offset property.
  - Slot synchronization —The synchronization event is
 configured as the first detected slot boundary within the acquired signal. A
 slot is a segment of a signal having a length equal to the duration of a PCG
 of 1.25 ms or 1536 chips. Slot synchronization synchronizes to a chip offset
 relative to the frame start being an integer multiple of 1536 chips.
  - Frame synchronization —The synchronization event is
 configured as the first detected frame boundary within the acquired signal.
 The R-FCH frame duration is 20ms, 16 slots, or 24576 chips.
- Interval duration —Specifies the length of the signal to be
 analyzed. This value is expressed in slots. Configure the interval duration using
 the SlotPower Meas Length property.

<!--NI_TOPIC bundle=rfmx-cdma2k path=slotpower-rcs.html language=enus -->
## TOPIC 00025: SlotPower Supported Radio Configurations (RCs)

- bundle_id: `rfmx-cdma2k`
- source_path: `slotpower-rcs.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k/raw/resource/enus/slotpower-rcs.html
- document_id: `rfmx-cdma2k`
- page_type: `leaf`
- content_type: `concept`
- source_description: The slot power measurement supports radio configurations RC3-RC4.

### SlotPower Supported Radio Configurations (RCs)

The slot power measurement supports radio configurations RC3-RC4.

<!--NI_TOPIC bundle=rfmx-cdma2k path=supported-hw.html language=enus -->
## TOPIC 00026: Supported Hardware

- bundle_id: `rfmx-cdma2k`
- source_path: `supported-hw.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k/raw/resource/enus/supported-hw.html
- document_id: `rfmx-cdma2k`
- page_type: `leaf`
- content_type: `concept`
- source_description: RFmx supports a number of NI devices. 1 RFmx CDMA2k Supported Hardware RFmx CDMA2k Hardware Earliest Driver Version Support (Windows 11) PXIe-5644 2022 Q3 PXIe-5645 2022 Q3 PXIe-5646 2022 Q3 PXIe-5663 2022 Q3 PXIe-5665 2022 Q3 PXIe-5668 2022 Q3 PXIe-5820 2022 Q3 PXIe-5840 2022 Q3 PXIe-5841 2022 Q3 P

### Supported Hardware

RFmx supports a number of NI devices.

| RFmx CDMA2k Hardware | Earliest Driver Version Support (Windows 11) |
| --- | --- |
| PXIe-5644 | 2022 Q3 |
| PXIe-5645 | 2022 Q3 |
| PXIe-5646 | 2022 Q3 |
| PXIe-5663 | 2022 Q3 |
| PXIe-5665 | 2022 Q3 |
| PXIe-5668 | 2022 Q3 |
| PXIe-5820 | 2022 Q3 |
| PXIe-5840 | 2022 Q3 |
| PXIe-5841 | 2022 Q3 |
| PXIe-5842 | 2022 Q4 |
| PXIe-5860 | 2024 Q3 |

Note

RFmx CDMA2k

NI-RFSA
 Properties

NI-RFSA LabVIEW VI Reference

For more information about your hardware and functionality, refer to the *NI-RFSA User Manual*.

<!--NI_TOPIC bundle=rfmx-cdma2k path=supported-spreading-rates.html language=enus -->
## TOPIC 00027: Supported Spreading Rates

- bundle_id: `rfmx-cdma2k`
- source_path: `supported-spreading-rates.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k/raw/resource/enus/supported-spreading-rates.html
- document_id: `rfmx-cdma2k`
- page_type: `leaf`
- content_type: `concept`
- source_description: The modulation accuracy (ModAcc) measurement supports only spreading rate 1 (SR1).

### Supported Spreading Rates

The modulation accuracy (ModAcc) measurement supports only spreading rate 1 (SR1).

<!--NI_TOPIC bundle=rfmx-cdma2k path=synchronization.html language=enus -->
## TOPIC 00028: Slot Power Synchronization

- bundle_id: `rfmx-cdma2k`
- source_path: `synchronization.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k/raw/resource/enus/synchronization.html
- document_id: `rfmx-cdma2k`
- page_type: `leaf`
- content_type: `concept`
- source_description: The measurement uses the CDMA2k scrambling sequence consisting of short and long PN codes to synchronize to slot boundaries. The synchronization of signals scrambled with a non-zero long code mask is constrained by the internal scrambling sequence length of 80 ms. If the long code mask of the long

### Slot Power Synchronization

The measurement uses the CDMA2k scrambling sequence consisting of short and long PN codes
 to synchronize to slot boundaries.

Note

<!--NI_TOPIC bundle=rfmx-cdma2k path=synchronization_2.html language=enus -->
## TOPIC 00029: Slot Power Synchronization

- bundle_id: `rfmx-cdma2k`
- source_path: `synchronization_2.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k/raw/resource/enus/synchronization_2.html
- document_id: `rfmx-cdma2k`
- page_type: `leaf`
- content_type: `concept`
- source_description: The measurement uses the CDMA2k scrambling sequence consisting of short and long PN codes to synchronize to slot boundaries. The synchronization of signals scrambled with a non-zero long code mask is constrained by the internal scrambling sequence length of 80 ms. If the long code mask of the long

### Slot Power Synchronization

The measurement uses the CDMA2k scrambling sequence consisting of short and long PN codes
 to synchronize to slot boundaries.

Note

<!--NI_TOPIC bundle=rfmx-cdma2k path=synchronization_3.html language=enus -->
## TOPIC 00030: Slot Power Synchronization

- bundle_id: `rfmx-cdma2k`
- source_path: `synchronization_3.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k/raw/resource/enus/synchronization_3.html
- document_id: `rfmx-cdma2k`
- page_type: `leaf`
- content_type: `concept`
- source_description: The measurement uses the CDMA2k scrambling sequence consisting of short and long PN codes to synchronize to slot boundaries. The synchronization of signals scrambled with a non-zero long code mask is constrained by the internal scrambling sequence length of 80 ms. If the long code mask of the long

### Slot Power Synchronization

The measurement uses the CDMA2k scrambling sequence consisting of short and long PN codes
 to synchronize to slot boundaries.

Note

<!--NI_TOPIC bundle=rfmx-cdma2k path=system-requirements.html language=enus -->
## TOPIC 00031: RFmx CDMA2k System Requirements

- bundle_id: `rfmx-cdma2k`
- source_path: `system-requirements.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k/raw/resource/enus/system-requirements.html
- document_id: `rfmx-cdma2k`
- page_type: `leaf`
- content_type: `concept`
- source_description: RFmx CDMA2k has the following requirements: Processor—1 GHz 64-bit (x64) processor 4 GB RAM * A screen resolution of 1,024 x 768 Any supported OS, with all available critical updates and service packs * Depending on the amount of data acquired and/or processed, a larger amount of memory may be requi

### RFmx CDMA2k System Requirements

RFmx CDMA2k has the following requirements:

- Processor—1 GHz 64-bit (x64) processor
- 4 GB RAM *
- A screen resolution of 1,024 x 768
- Any supported OS, with all available critical updates and service packs

* Depending on the amount of data acquired and/or processed, a larger amount of memory
 may be required.

<!--NI_TOPIC bundle=rfmx-cdma2k path=user-manual-welcome.html language=enus -->
## TOPIC 00032: RFmx CDMA2k User Manual

- bundle_id: `rfmx-cdma2k`
- source_path: `user-manual-welcome.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k/raw/resource/enus/user-manual-welcome.html
- document_id: `rfmx-cdma2k`
- page_type: `leaf`
- content_type: `concept`
- source_description: The RFmx CDMA2k User Manual provides detailed descriptions of the product functionality and the step by step processes for use. Looking for Something Else?For information not found in the User Manual for your product, such as specifications and API reference, browse Related Information.

### RFmx CDMA2k
 User Manual

The RFmx CDMA2k User Manual provides detailed
 descriptions of the product functionality and the step by step processes for use.

#### Looking for Something Else?

For information not found in the User Manual
 for your product, such as specifications and API reference, browse *Related
 Information*.

Related information:

- Download RFmx CDMA2k
- License Setup and Activation
- RFmx CDMA2k Release Notes
- Getting Started with RFmx
- RFmx CDMA2k LabVIEW Reference
- RFmx CDMA2k .NET Reference
- RFmx CDMA2k C Reference
- RFmx Instr LabVIEW Reference
- RFmx Instr .NET Reference
- RFmx Instr C Reference
