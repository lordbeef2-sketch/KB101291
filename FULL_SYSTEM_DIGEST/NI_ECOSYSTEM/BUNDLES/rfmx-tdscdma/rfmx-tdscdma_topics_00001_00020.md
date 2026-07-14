# NI DOCUMENT BUNDLE: rfmx-tdscdma

<!--NI_BUNDLE_CHUNK bundle=rfmx-tdscdma start=1 end=20 -->
<!--NI_TOPIC bundle=rfmx-tdscdma path=auto-detection-capabilities.html language=enus -->
## TOPIC 00001: Auto Detection Capabilities

- bundle_id: `rfmx-tdscdma`
- source_path: `auto-detection-capabilities.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma/raw/resource/enus/auto-detection-capabilities.html
- document_id: `rfmx-tdscdma`
- page_type: `leaf`
- content_type: `concept`
- source_description: RFmx TD-SCDMA ModAcc measurements support the auto detection of active physical channels, by setting the Channel Configuration Mode property to Auto Detect. The default channel configuration mode value is Auto Detect. RFmx TD-SCDMA provides auto detection capabilities for the midamble parameters con

### Auto Detection Capabilities

RFmx TD-SCDMA ModAcc measurements support the auto detection of active physical channels,
 by setting the Channel Configuration Mode property to Auto
 Detect. The default channel configuration mode value is Auto
 Detect.

RFmx TD-SCDMA provides auto detection capabilities for the midamble parameters configured
 by the Midamble Auto Detection Mode property. You can set the Midamble Auto Detection
 Mode property to Off or Midamble Shift.
 The default value is Midamble Shift. To detect the Midamble shift
 accurately, set the Max Num Users property. The midamble code is always derived from the
 configured scrambling code.

<!--NI_TOPIC bundle=rfmx-tdscdma path=averaging.html language=enus -->
## TOPIC 00002: Averaging

- bundle_id: `rfmx-tdscdma`
- source_path: `averaging.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma/raw/resource/enus/averaging.html
- document_id: `rfmx-tdscdma`
- page_type: `leaf`
- content_type: `concept`
- source_description: RFmx TD-SCDMA ModAcc measurements support averaging of the results among multiple acquisitions. You can enable averaging by setting the ModAcc Averaging Enabled property to True and configuring the ModAcc Averaging Count property.

### Averaging

RFmx TD-SCDMA ModAcc measurements support averaging of the results among multiple
 acquisitions.

You can enable averaging by setting the ModAcc Averaging Enabled property to
 True and configuring the ModAcc Averaging Count property.

<!--NI_TOPIC bundle=rfmx-tdscdma path=cda-auto-detection.html language=enus -->
## TOPIC 00003: Auto Detection Capabilities

- bundle_id: `rfmx-tdscdma`
- source_path: `cda-auto-detection.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma/raw/resource/enus/cda-auto-detection.html
- document_id: `rfmx-tdscdma`
- page_type: `leaf`
- content_type: `concept`
- source_description: RFmx TD-SCDMA Code Domain Analysis (CDA) measurements support the auto detection of the active physical channels, by setting the Channel Configuration Mode property to Auto Detect. The default channel configuration mode value is Auto Detect. RFmx TD-SCDMA provides auto detection capabilities for the

### Auto Detection Capabilities

RFmx TD-SCDMA Code Domain Analysis (CDA) measurements support the auto detection of the
 active physical channels, by setting the Channel Configuration Mode property to
 Auto Detect. The default channel configuration mode value is
 Auto Detect.

RFmx TD-SCDMA provides auto detection capabilities for the midamble parameters configured
 by the Midamble Auto Detection Mode property. You can set the Midamble Auto Detection
 Mode property to Off or Midamble Shift.
 The default value is Midamble Shift. To detect the Midamble shift
 accurately, set the Max Num Users property. The midamble code is always derived from the
 configured scrambling code.

<!--NI_TOPIC bundle=rfmx-tdscdma path=cda-averaging.html language=enus -->
## TOPIC 00004: Averaging

- bundle_id: `rfmx-tdscdma`
- source_path: `cda-averaging.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma/raw/resource/enus/cda-averaging.html
- document_id: `rfmx-tdscdma`
- page_type: `leaf`
- content_type: `concept`
- source_description: RFmx TD-SCDMA code domain analysis (CDA) measurements support averaging of the results among multiple acquisitions. You can enable averaging by setting the CDA Averaging Enabled property to True and configuring the CDA Averaging Count property.

### Averaging

RFmx TD-SCDMA code domain analysis (CDA) measurements support averaging of the results
 among multiple acquisitions.

You can enable averaging by setting the CDA Averaging Enabled property to
 True and configuring the CDA Averaging Count property.

<!--NI_TOPIC bundle=rfmx-tdscdma path=measurement-interval.html language=enus -->
## TOPIC 00005: Measurement Interval

- bundle_id: `rfmx-tdscdma`
- source_path: `measurement-interval.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma/raw/resource/enus/measurement-interval.html
- document_id: `rfmx-tdscdma`
- page_type: `leaf`
- content_type: `concept`
- source_description: RFmx TD-SCDMA determines the measurement interval used for ModAcc measurements using the following values. You can configure the values independently or use the RFmxTDSCDMA ModAcc Configure Synchronization Mode and Interval VI to configure them at the same time. Interval Start—Specifies the offset a

### Measurement Interval

RFmx TD-SCDMA determines the measurement interval used for ModAcc measurements using the
 following values. You can configure the values independently or use the RFmxTDSCDMA
 ModAcc Configure Synchronization Mode and Interval VI to configure them at the same
 time.

- Interval Start —Specifies the offset at which the measurement
 starts. When the synchronization mode is Slot , the offset is
 relative to the first detected slot boundary within the acquired signal. When the
 synchronization mode is Subframe , the offset is relative to
 the first detected subframe boundary within the acquired signal. The start of the
 acquisition is controlled by trigger settings. Configure the Interval Start using
 the ModAcc Meas Offset property.
- Interval Duration —Specifies the length of the signal to be
 analyzed. The interval duration is expressed in slots. Configure the interval
 duration using the ModAcc Meas Length property.

Note

<!--NI_TOPIC bundle=rfmx-tdscdma path=new-features-and-changes.html language=enus -->
## TOPIC 00006: RFmx TD-SCDMA New Features and Changes

- bundle_id: `rfmx-tdscdma`
- source_path: `new-features-and-changes.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma/raw/resource/enus/new-features-and-changes.html
- document_id: `rfmx-tdscdma`
- page_type: `leaf`
- content_type: `concept`
- source_description: Learn about updates, including new features and behavior changes, introduced in each version of RFmx TD-SCDMA. Discover what is new in the latest releases of RFmx TD-SCDMA.If you cannot find new features and changes for your version, it might not include user-facing updates. However, your version mi

### RFmx TD-SCDMA
 New Features and Changes

Learn about updates, including new features and behavior changes, introduced in each
 version of RFmx TD-SCDMA.

RFmx TD-SCDMA

Note

Release Notes

Related information:

- Software and Driver Downloads

#### RFmx TD-SCDMA
 2026 Q2 Changes

RFmx TD-SCDMA 2026 Q2 includes behavior changes with ACP
 measurements that use the Sequential FFT measurement method. This release also adds support
 for the PXIe-5841 with 200
 MHz bandwidth.

##### Behavior Changes

This version of RFmx TD-SCDMA updates support for the following feature:

- Adjacent Channel Power (ACP): When you use the Sequential FFT 
 measurement method, you can configure the Configuring the Number of
 Analysis Threads property to a value greater than 1.

##### New
 Hardware Support

This version of RFmx TD-SCDMA
 adds support for the following hardware:

- PXIe-5841 ( 200 MHz ) bandwidth

#### RFmx TD-SCDMA
 2025 Q3 Changes

Learn about new features, behavior changes, and other updates in RFmx TD-SCDMA 2025 Q3.

##### New
 Features

This version of the RFmx TD-SCDMA
 adds support for the following features:

- PXIe-5860 Self-Cal Validity Check

#### RFmx TD-SCDMA
 2024 Q4 Changes

Learn about new features, behavior changes, and other updates in RFmx TD-SCDMA 2024 Q4.

##### New
 Features

This version of the RFmx TD-SCDMA
 adds support for the following features:

- Uninstalling RFmx TD-SCDMA software also removes any
 previous versions of RFmx TD-SCDMA .NET runtimes that
 were leaked in .NET Global Assembly Cache directory.

#### RFmx TD-SCDMA
 2024 Q3 Changes

Learn about new features, behavior changes, and other updates in RFmx TD-SCDMA 2024 Q3.

##### New
 Hardware Support

This version of the RFmx TD-SCDMA adds support for the following
 hardware:

- PXIe-5860

#### RFmx TD-SCDMA
 2024 Q2 Changes

Learn about new features, behavior changes, and other updates in RFmx TD-SCDMA 2024 Q2.

- Obsoleted the RFmxInstr Load All Configurations VI. Use the
 RFmxInstr Load Configurations VI along with the appropriate
 RFmxInstr Load Options property, instead.

#### RFmx TD-SCDMA 2023 Q4 New Features and
 Changes

- Support for obtaining unprocessed I/Q data utilized for RFmx measurements

#### RFmx TD-SCDMA 2023 Q2 New Features and
 Changes

- Speed improvements for Composite and Spectral measurements

#### RFmx TD-SCDMA 2023 Q1 New Features and
 Changes

- Support for LabVIEW 2023 Q1 (64-bit)

<!--NI_TOPIC bundle=rfmx-tdscdma path=pvt-auto-detection.html language=enus -->
## TOPIC 00007: PVT Auto Detection Capabilities

- bundle_id: `rfmx-tdscdma`
- source_path: `pvt-auto-detection.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma/raw/resource/enus/pvt-auto-detection.html
- document_id: `rfmx-tdscdma`
- page_type: `leaf`
- content_type: `concept`
- source_description: RFmx TD-SCDMA provides auto detection capabilities for the midamble parameters configured by the Midamble Auto Detection Mode property. You can set the Midamble Auto Detection Mode property to Off or Midamble Shift. The default value is Midamble Shift. To detect the Midamble shift accurately, set th

### PVT Auto Detection Capabilities

RFmx TD-SCDMA provides auto detection capabilities for the midamble parameters configured
 by the Midamble Auto Detection Mode property. You can set the Midamble Auto Detection
 Mode property to Off or Midamble Shift.
 The default value is Midamble Shift. To detect the Midamble shift
 accurately, set the Max Num Users property. The midamble code is always derived from the
 configured scrambling code.

<!--NI_TOPIC bundle=rfmx-tdscdma path=pvt-averaging.html language=enus -->
## TOPIC 00008: Averaging

- bundle_id: `rfmx-tdscdma`
- source_path: `pvt-averaging.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma/raw/resource/enus/pvt-averaging.html
- document_id: `rfmx-tdscdma`
- page_type: `leaf`
- content_type: `concept`
- source_description: RFmx TD-SCDMA power versus time (PVT) measurements support averaging of the results among multiple acquisitions. You can enable averaging by setting the PVT Averaging Enabled property to True and configuring the PVT Averaging Count property.

### Averaging

RFmx TD-SCDMA power versus time (PVT) measurements support averaging of the results among
 multiple acquisitions.

You can enable averaging by setting the PVT Averaging Enabled property to
 True and configuring the PVT Averaging Count property.

<!--NI_TOPIC bundle=rfmx-tdscdma path=rfmxtdscdma-overview.html language=enus -->
## TOPIC 00009: RFmx TD-SCDMA Overview

- bundle_id: `rfmx-tdscdma`
- source_path: `rfmxtdscdma-overview.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma/raw/resource/enus/rfmxtdscdma-overview.html
- document_id: `rfmx-tdscdma`
- page_type: `leaf`
- content_type: `concept`
- source_description: This user manual contains an introduction to RFmx TD-SCDMA measurement concepts.

### RFmx TD-SCDMA Overview

This user manual contains an introduction to RFmx TD-SCDMA measurement concepts.

<!--NI_TOPIC bundle=rfmx-tdscdma path=supported-hw.html language=enus -->
## TOPIC 00010: Supported Hardware

- bundle_id: `rfmx-tdscdma`
- source_path: `supported-hw.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma/raw/resource/enus/supported-hw.html
- document_id: `rfmx-tdscdma`
- page_type: `leaf`
- content_type: `concept`
- source_description: RFmx supports a number of NI devices. 1 RFmx TD-SCDMA Supported Hardware RFmx TD-SCDMA Hardware Earliest Driver Version Support (Windows 11) PXIe-5644 2022 Q3 PXIe-5645 2022 Q3 PXIe-5646 2022 Q3 PXIe-5663 2022 Q3 PXIe-5665 2022 Q3 PXIe-5668 2022 Q3 PXIe-5820 2022 Q3 PXIe-5840 2022 Q3 PXIe-5841 (1 GH

### Supported Hardware

RFmx supports a number of NI devices.

| RFmx TD-SCDMA Hardware | Earliest Driver Version Support (Windows 11) |
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

RFmx TD-SCDMA

NI-RFSA
 Properties

NI-RFSA LabVIEW VI Reference

For more information about your hardware and functionality, refer to the *NI-RFSA User Manual*.

<!--NI_TOPIC bundle=rfmx-tdscdma path=supported-physical-channels.html language=enus -->
## TOPIC 00011: Supported Physical Channels

- bundle_id: `rfmx-tdscdma`
- source_path: `supported-physical-channels.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma/raw/resource/enus/supported-physical-channels.html
- document_id: `rfmx-tdscdma`
- page_type: `leaf`
- content_type: `concept`
- source_description: RFmx TD-SCDMA ModAcc measurements support all physical channels employing a dedicated physical channel (DPCH) time slot format or an enhanced dedicated channel physical uplink channel (E-PUCH) time slot format. Additionally, the measurements also support the physical synchronization channel for upli

### Supported Physical Channels

RFmx TD-SCDMA ModAcc measurements support all physical channels employing a dedicated
 physical channel (DPCH) time slot format or an enhanced dedicated channel physical
 uplink channel (E-PUCH) time slot format. Additionally, the measurements also support
 the physical synchronization channel for uplink called Uplink Pilot Channel (UpPCH).
 RFmx TD-SCDMA supports the following physical channels:

- DPCH
- E-DCH Physical Uplink Channel
- High Speed Shared Information Channel (HS-SICH)
- Uplink Pilot Channel

<!--NI_TOPIC bundle=rfmx-tdscdma path=system-requirements.html language=enus -->
## TOPIC 00012: RFmx TD-SCDMA System Requirements

- bundle_id: `rfmx-tdscdma`
- source_path: `system-requirements.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma/raw/resource/enus/system-requirements.html
- document_id: `rfmx-tdscdma`
- page_type: `leaf`
- content_type: `concept`
- source_description: RFmx TD-SCDMA has the following requirements: Processor—1 GHz 64-bit (x64) processor 4 GB RAM * A screen resolution of 1,024 x 768 Any supported OS, with all available critical updates and service packs * Depending on the amount of data acquired and/or processed, a larger amount of memory may be req

### RFmx TD-SCDMA System Requirements

RFmx TD-SCDMA has the following requirements:

- Processor—1 GHz 64-bit (x64) processor
- 4 GB RAM *
- A screen resolution of 1,024 x 768
- Any supported OS, with all available critical updates and service packs

* Depending on the amount of data acquired and/or processed, a larger amount of memory
 may be required.

<!--NI_TOPIC bundle=rfmx-tdscdma path=td-scdma-acp.html language=enus -->
## TOPIC 00013: TD-SCDMA ACP

- bundle_id: `rfmx-tdscdma`
- source_path: `td-scdma-acp.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma/raw/resource/enus/td-scdma-acp.html
- document_id: `rfmx-tdscdma`
- page_type: `leaf`
- content_type: `concept`
- source_description: TD-SCDMA ACP Offset Channels For TD-SCDMA, the 3GPP standard defines ACP as the measurement of the ratio of the RRC-filtered mean power of the carrier and the RRC-filtered mean power of adjacent TD-SCDMA channels with a bandwidth of 1.28 MHz and a carrier spacing of 1.6 MHz. Configure the number of

### TD-SCDMA ACP

#### TD-SCDMA ACP Offset Channels

For TD-SCDMA, the 3GPP standard defines ACP as the measurement of the ratio of the
 RRC-filtered mean power of the carrier and the RRC-filtered mean power of adjacent
 TD-SCDMA channels with a bandwidth of 1.28 MHz and a carrier spacing of 1.6 MHz.

Configure the number of measured offset channels using the Number of Offsets property or
 the ACP Configure Number of Offsets VI/function.

Related information:

- ACP

<!--NI_TOPIC bundle=rfmx-tdscdma path=td-scdma-cda.html language=enus -->
## TOPIC 00014: Code Domain Analysis (CDA)

- bundle_id: `rfmx-tdscdma`
- source_path: `td-scdma-cda.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma/raw/resource/enus/td-scdma-cda.html
- document_id: `rfmx-tdscdma`
- page_type: `leaf`
- content_type: `concept`
- source_description: RFmx TD-SCDMA CDA measurement provides measurements in the code domain for a specific RFmx TD-SCDMA time slot. It provides the analysis of the code domain power and the calculation of modulation accuracy for a selected code channel. RFmx TD-SCDMA CDA Code Domain Power (CDP) Measurements For measurin

### Code Domain Analysis (CDA)

RFmx TD-SCDMA CDA measurement provides measurements in the code domain for a specific
 RFmx TD-SCDMA time slot. It provides the analysis of the code domain power and the
 calculation of modulation accuracy for a selected code channel.

#### RFmx TD-SCDMA CDA Code Domain Power (CDP) Measurements

For measuring the CDP, RFmx TD-SCDMA analyzes the CDP of the TD-SCDMA time slot data.
 This analysis is performed for the configured base spreading factor, specified by the
 CDA Base Spreading Factor property. The default value for the Base Spreading Factor
 property is 16.

You can use the CDA Pwr Unit property to configure the absolute power values in dBm, or
 the relative power values in dB. This value is configured relative to the total code
 domain power.

RFmx TD-SCDMA CDA measurement computes the following code domain measurements:

- CDA Results Total Pwr —Returns the total CDP.

- CDA Results Total Active Pwr —Returns the total active code
 power, either as an absolute value in dBm, or as a relative value in dB.
- CDA Results Mean Active Pwr —Returns the average active code
 power, either as an absolute value in dBm, or as a relative value in dB.
- CDA Results Pk Active Pwr —Returns the maximum power among all
 active code channels, either as an absolute value in dBm, or as a relative value in
 dB.
- CDA Results Mean Inactive Pwr —Returns the average code power
 measured among the set of inactive channels, either as an absolute value in dBm, or
 as a relative value in dB.
- CDA Results Pk Inactive Pwr —Returns the largest measured code
 power among the set of inactive channels, either as an absolute value in dBm, or as
 a relative value in dB.

#### RFmx TD-SCDMA CDA Modulation Accuracy Measurement for Selected Code Channel

RFmx TD-SCDMA CDA measurement provides the ability to analyze the modulation accuracy for
 a specific, user configurable code channel. You can configure the code channel to be
 analyzed by using the spreading factor and the channelization code. The spreading factor
 and the channelization code are calculated using the CDA Meas Ch Spreading Factor and
 the CDA Meas Ch Channelization Code properties, respectively.

For the selected code channel, RFmx TD-SCDMA CDA computes the following measurements:

- CDA Results RMS Symbol EVM —Returns the RMS symbol EVM for the
 selected time slot and channel.

- CDA Results Pk Symbol EVM —Returns the peak symbol EVM for the
 selected time slot and channel.
- CDA Results RMS Symbol Magnitude Error —Returns the RMS symbol
 magnitude error for the selected time slot and channel.
- CDA Results RMS Symbol Phase Error —Returns the RMS symbol
 phase error for the selected time slot and channel.

RFmx TD-SCDMA CDA measurements calculate the following additional metrics for I/Q
 impairments:

- CDA Results I/Q Origin Offset —Returns the DC offset of the
 I/Q samples from the origin.
- CDA Results I/Q Gain Imbalance —Returns the I/Q gain imbalance
 between the inphase (I) and quadrature (Q) components within the complex baseband
 signal.
- CDA Results I/Q Quadrature Error —Returns the phase difference
 from the ideal 90 degrees between the I and Q components within the complex baseband
 signal.

<!--NI_TOPIC bundle=rfmx-tdscdma path=td-scdma-chp.html language=enus -->
## TOPIC 00015: TD-SCDMA CHP

- bundle_id: `rfmx-tdscdma`
- source_path: `td-scdma-chp.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma/raw/resource/enus/td-scdma-chp.html
- document_id: `rfmx-tdscdma`
- page_type: `leaf`
- content_type: `concept`
- source_description: TD-SCDMA CHP Bandwidth The RFmx TD-SCDMA CHP measurement measures the power of the RF signal as the RRC-filtered power within the TD-SCDMA signal bandwidth of 1.28 MHz.

### TD-SCDMA CHP

#### TD-SCDMA CHP Bandwidth

The RFmx TD-SCDMA CHP measurement measures the power of the RF signal as the RRC-filtered
 power within the TD-SCDMA signal bandwidth of 1.28 MHz.

Related information:

- CHP

<!--NI_TOPIC bundle=rfmx-tdscdma path=td-scdma-modacc.html language=enus -->
## TOPIC 00016: TD-SCDMA Modulation Accuracy Measurements

- bundle_id: `rfmx-tdscdma`
- source_path: `td-scdma-modacc.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma/raw/resource/enus/td-scdma-modacc.html
- document_id: `rfmx-tdscdma`
- page_type: `leaf`
- content_type: `concept`
- source_description: RFmx TD-SCDMA ModAcc measurements calculate the following performance metrics: RMS EVM—Returns the RMS value of the normalized EVM. RFmx returns the following RMS EVM measurements: Traffic Slot Overall or composite RMS EVM for the analyzed traffic signal RMS EVM for the data portion of the traffic s

### TD-SCDMA Modulation Accuracy Measurements

RFmx TD-SCDMA ModAcc measurements calculate the following performance metrics:

- RMS EVM —Returns the RMS value of the normalized EVM. RFmx
 returns the following RMS EVM measurements:
  - Traffic Slot
    - Overall or composite RMS EVM for the analyzed traffic signal
    - RMS EVM for the data portion of the traffic signal
    - RMS EVM for the midamble portion of the traffic signal
  - Pilot Slot
    - RMS EVM for the analyzed pilot signal
- Peak EVM —Returns the peak normalized EVM observed within the
 measurement interval. RFmx returns the following peak EVM measurements:
  - Traffic Slot
    - Overall or composite peak EVM for the analyzed traffic signal
    - Peak EVM for the data portion of the traffic signal
    - Peak EVM for the midamble portion of the traffic signal
  - Pilot Slot
    - Peak EVM for the analyzed pilot signal
- Rho —Returns the normalized correlation coefficient of the
 measured signal and the generated reference signal. RFmx returns the following peak
 rho measurements:
  - Traffic Slot
    - Overall or composite rho for the analyzed traffic signal
    - Rho for the data portion of the traffic signal
    - Rho for the midamble portion of the traffic signal
  - Pilot Slot
    - Rho for the analyzed pilot signal
- Peak CDE —Returns the maximum value among the code domain
 errors (CDEs). The base spreading factor is 16. RFmx returns the peak CDE only for
 the data portion of the analyzed signal. This result is not supported when the
 Slot Type is configured as
 Pilot .
- Peak RCDE —Returns the maximum value among the relative code
 domain errors (RCDEs) for all active channels. RFmx returns the peak RCDE only for
 the data portion of the analyzed signal. This result is not supported when the
 Slot Type is configured as
 Pilot .
- Peak Active CDE —Returns the peak value of all CDEs of the
 active channels. RFmx returns the peak active CDE only for the data portion of the
 analyzed signal. This result is not supported when the Slot
 Type is configured as Pilot .
- Frequency Error —Returns the frequency error. This result is
 not supported when the Slot Type is configured as
 Pilot .
- Chip Rate Error —Returns the chip rate error. This result is
 not supported when the Slot Type is configured as
 Pilot .

RFmx TD-SCDMA ModAcc measurements calculate the following additional metrics for I/Q
 impairments:

- I/Q Origin Offset —Returns the DC offset of the I/Q samples
 from the origin.
- I/Q Gain Imbalance —Returns the I/Q gain imbalance between the
 inphase (I) and quadrature (Q) components within the complex baseband signal.
- I/Q Quadrature Error —Returns the phase difference from the
 ideal 90 degrees between the I and Q components within the complex baseband signal.

<!--NI_TOPIC bundle=rfmx-tdscdma path=td-scdma-obw.html language=enus -->
## TOPIC 00017: TD-SCDMA OBW

- bundle_id: `rfmx-tdscdma`
- source_path: `td-scdma-obw.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma/raw/resource/enus/td-scdma-obw.html
- document_id: `rfmx-tdscdma`
- page_type: `leaf`
- content_type: `concept`
- source_description: TD-SCDMA OBW Definition The RFmx TD-SCDMA OBW measurement measures the occupied signal bandwidth as the bandwidth where 99% of the RF power is concentrated.

### TD-SCDMA OBW

#### TD-SCDMA OBW Definition

The RFmx TD-SCDMA OBW measurement measures the occupied signal bandwidth as the bandwidth
 where 99% of the RF power is concentrated.

Related information:

- OBW

<!--NI_TOPIC bundle=rfmx-tdscdma path=td-scdma-pvt.html language=enus -->
## TOPIC 00018: Power versus Time (PVT)

- bundle_id: `rfmx-tdscdma`
- source_path: `td-scdma-pvt.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma/raw/resource/enus/td-scdma-pvt.html
- document_id: `rfmx-tdscdma`
- page_type: `leaf`
- content_type: `concept`
- source_description: RFmx TD-SCDMA PVT measurement performs the transmit ON/OFF time mask test according to 3GPP TS 34.122 specification. The test analyzes the RRC-filtered transmit power according to the test definition in 3GPP TS 34.122 specification, by measuring the transmit power present in specific time segments a

### Power versus Time (PVT)

RFmx TD-SCDMA PVT measurement performs the transmit ON/OFF time mask test according to
 *3GPP TS 34.122* specification.

The test analyzes the RRC-filtered transmit power according to the test definition in
 *3GPP TS 34.122* specification, by measuring the transmit power
 present in specific time segments around an active time slot. You can obtain the
 built-in definition of the individual power segments by querying the PVT Segment Start
 and the PVT Segment Stop results.

According to the *3GPP TS 34.122* specification, the PVT measurement
 uses the midamble of the active time slot as the timing reference to apply the ON/OFF
 time mask. Thus, you must configure the midamble basic sequence and shift values, or
 activate the midamble auto detection for this measurement.

To achieve the required measurement dynamic range, the PVT measurement provides a high
 Dynamic Range mode that you can activate using the PVT Meas
 Method property. In this mode, the data acquired with the configured reference level are
 combined with the data acquired at a lower reference level to accurately measure the ON
 as well as the OFF power.

Note

RFmx TD-SCDMA measurements calculate the following performance metrics:

- Measurement Status —Returns the overall measurement status.
 The overall status is Pass if the power in all the PVT
 measurement segments is below the limits defined in the 3GPP TS
 34.122 specification.

- Mean Absolute ON Power —Returns the mean ON power.
- Mean Absolute OFF Power —Returns the mean OFF power.
- Burst Width —Returns the duration of the ON power.

Additionally, the PVT measurement provides segment specific results, such as the segment
 measurement status and segment margin.

<!--NI_TOPIC bundle=rfmx-tdscdma path=td-scdma-sem.html language=enus -->
## TOPIC 00019: TD-SCDMA SEM

- bundle_id: `rfmx-tdscdma`
- source_path: `td-scdma-sem.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma/raw/resource/enus/td-scdma-sem.html
- document_id: `rfmx-tdscdma`
- page_type: `leaf`
- content_type: `concept`
- source_description: TD-SCDMA SEM Offset Segments and Limit Masks The RFmx TD-SCDMA SEM measurement uses predefined definitions for the offset segments to measure the emissions around the carrier. The offset segments are defined by the measurement offset frequency , where is the difference of the carrier center frequen

### TD-SCDMA SEM

#### TD-SCDMA SEM Offset Segments and Limit Masks

The RFmx TD-SCDMA SEM measurement uses predefined definitions for the offset segments to
 measure the emissions around the carrier. The offset segments are defined by the
 measurement offset frequency [IMAGE alt='image' src='GUID-8E731688-6E1E-4171-B1FF-3FB7B15CE907-a5.png'], where [IMAGE alt='image' src='GUID-56465C87-EB60-41E8-A52A-839FFC352E75-a5.png'] is the difference of the carrier center frequency and the center of
 the measurement frequency. The following table describes offset segments to measure and
 the limits that are defined according to the *3GPP* specification.

| Offset Segment | Measurement Bandwidth | Relative Mask Limit | Absolute Mask Limit |
| --- | --- | --- | --- |
| 0.815 MHz ≤\|Δƒ\|≤ 1.8 MHz | 30 kHz | -35.21 dB to -49 dB | -71.30 dBm |
| 1.8 MHz ≤\|Δƒ\|≤ 2.385 MHz | 30 kHz | -49 dB to -58.95 dB | -71.30 dBm |
| 2.9 MHz ≤\|Δƒ\|≤ 3.5 MHz | 1 MHz | -44 dB | -56.07 dBm |

Related information:

- SEM

<!--NI_TOPIC bundle=rfmx-tdscdma path=user-manual-welcome.html language=enus -->
## TOPIC 00020: RFmx TD-SCDMA User Manual

- bundle_id: `rfmx-tdscdma`
- source_path: `user-manual-welcome.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma/raw/resource/enus/user-manual-welcome.html
- document_id: `rfmx-tdscdma`
- page_type: `leaf`
- content_type: `concept`
- source_description: The RFmx TD-SCDMA User Manual provides detailed descriptions of the product functionality and the step by step processes for use. Looking for Something Else?For information not found in the User Manual for your product, such as specifications and API reference, browse Related Information.

### RFmx TD-SCDMA
 User Manual

The RFmx TD-SCDMA User Manual provides detailed
 descriptions of the product functionality and the step by step processes for use.

#### Looking for Something Else?

For information not found in the User Manual
 for your product, such as specifications and API reference, browse *Related
 Information*.

Related information:

- Download RFmx TD-SCDMA
- License Setup and Activation
- RFmx TD-SCDMA Release Notes
- Getting Started with RFmx
- RFmx TD-SCDMA LabVIEW Reference
- RFmx TD-SCDMA .NET Reference
- RFmx TD-SCDMA C Reference
- RFmx Instr LabVIEW Reference
- RFmx Instr .NET Reference
- RFmx Instr C Reference
