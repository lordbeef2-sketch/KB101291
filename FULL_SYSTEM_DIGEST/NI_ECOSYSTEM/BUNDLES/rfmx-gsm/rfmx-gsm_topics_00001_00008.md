# NI DOCUMENT BUNDLE: rfmx-gsm

<!--NI_BUNDLE_CHUNK bundle=rfmx-gsm start=1 end=8 -->
<!--NI_TOPIC bundle=rfmx-gsm path=modacc.html language=enus -->
## TOPIC 00001: Modulation Accuracy (ModAcc) Measurement

- bundle_id: `rfmx-gsm`
- source_path: `modacc.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm/raw/resource/enus/modacc.html
- document_id: `rfmx-gsm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The key results for the GSM ModAcc measurement are RMS phase error, peak phase error, peak symbol, frequency error, IQ gain imbalance, and IQ origin offset. For EDGE and EGPRS, the key results of the ModAcc measurement are RMS EVM, peak EVM, 95 percentile EVM, IQ gain imbalance, peak EVM symbol, mag

### Modulation Accuracy (ModAcc) Measurement

The key results for the GSM ModAcc measurement are RMS phase error, peak phase error,
 peak symbol, frequency error, IQ gain imbalance, and IQ origin offset. For EDGE and
 EGPRS, the key results of the ModAcc measurement are RMS EVM, peak EVM, 95 percentile
 EVM, IQ gain imbalance, peak EVM symbol, magnitude error, frequency error, amplitude
 droop, and IQ origin offset. For more information on the ModAcc measurement refer to
 *3GPP TS 45.005* specifications.

The TSC, modulation type, burst type, and filter width of the signal should remain same
 for each time slot in the ModAcc measurements. RFmx GSM and EDGE support normal burst,
 while EGPRS supports normal burst and higher symbol rate burst. If you enable auto TSC
 detection, the measurement is possible even in the case of different TSCs in different
 slots. RFmx allows measurement averaging for ModAcc over multiple signal acquisitions.
 RFmx also allows optional droop compensation.

The following image shows an example of a GSM phase error trace in RFmx for a single time
 slot.

[IMAGE alt='image' src='GUID-585CD939-4092-4EED-9BA3-812B4BA41B5D-a5.png']

The following image shows an example of an EDGE EVM trace in RFmx for two time slots.

[IMAGE alt='image' src='GUID-1E83A6E7-6D79-4C15-8F2F-818694875548-a5.png']

<!--NI_TOPIC bundle=rfmx-gsm path=new-features-and-changes.html language=enus -->
## TOPIC 00002: RFmx GSM New Features and Changes

- bundle_id: `rfmx-gsm`
- source_path: `new-features-and-changes.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm/raw/resource/enus/new-features-and-changes.html
- document_id: `rfmx-gsm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Learn about updates, including new features and behavior changes, introduced in each version of RFmx GSM. Discover what is new in the latest releases of RFmx GSM.If you cannot find new features and changes for your version, it might not include user-facing updates. However, your version might includ

### RFmx GSM
 New Features and Changes

Learn about updates, including new features and behavior changes, introduced in each
 version of RFmx GSM.

RFmx GSM

Note

Release Notes

Related information:

- Software and Driver Downloads

#### RFmx GSM
 2026 Q2 Changes

The RFmx GSM 2026 Q2 release adds support for the
 PXIe-5841 with 200 MHz bandwidth.

##### New
 Hardware Support

This version of RFmx GSM
 adds support for the following hardware:

- PXIe-5841 ( 200 MHz ) bandwidth

#### RFmx GSM 2025 Q4 New Features and
 Changes

- Added support for analysis of Access Burst in ORFS and ModAcc measurement.
- Added support for analysis of user configured slot in a frame with different slot
 properties (Burst type and Modulation type) in ModAcc and ORFS measurement.

#### RFmx GSM
 2025 Q3 Changes

Learn about new features, behavior changes, and other updates in RFmx GSM 2025 Q3.

##### New
 Features

This version of the RFmx GSM
 adds support for the following features:

- PXIe-5860 Self-Cal Validity Check

#### RFmx GSM
 2024 Q4 Changes

Learn about new features, behavior changes, and other updates in RFmx GSM 2024 Q4.

##### New
 Features

This version of the RFmx GSM
 adds support for the following features:

- Uninstalling RFmx GSM software also removes any
 previous versions of RFmx GSM .NET runtimes that
 were leaked in .NET Global Assembly Cache directory.

#### RFmx GSM
 2024 Q3 Changes

Learn about new features, behavior changes, and other updates in RFmx GSM 2024 Q3.

##### New
 Hardware Support

This version of the RFmx GSM adds support for the following
 hardware:

- PXIe-5860

#### RFmx GSM
 2024 Q2 Changes

Learn about new features, behavior changes, and other updates in RFmx GSM 2024 Q2.

- Obsoleted the RFmxInstr Load All Configurations VI. Use the
 RFmxInstr Load Configurations VI along with the appropriate
 RFmxInstr Load Options property, instead.

#### RFmx GSM 2023 Q4 New Features and
 Changes

- Support for obtaining unprocessed I/Q data utilized for RFmx measurements

#### RFmx GSM 2023 Q2 New Features and
 Changes

- Speed improvements for Composite and Spectral measurements

#### RFmx GSM 2023 Q1 New Features and
 Changes

- Support for LabVIEW 2023 Q1 (64-bit)

<!--NI_TOPIC bundle=rfmx-gsm path=orfs.html language=enus -->
## TOPIC 00003: ORFS Measurement

- bundle_id: `rfmx-gsm`
- source_path: `orfs.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm/raw/resource/enus/orfs.html
- document_id: `rfmx-gsm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Output radio frequency spectrum (ORFS) is a frequency-domain measurement in which the spread of GSM signal power outside the channel is assessed. The spectrum of GSM is influenced by two major factors, namely, modulation in the transmitted signal and the switching transient of the GSM transmitter. T

### ORFS Measurement

Output radio frequency spectrum (ORFS) is a frequency-domain measurement in which the
 spread of GSM signal power outside the channel is assessed. The spectrum of GSM is
 influenced by two major factors, namely, modulation in the transmitted signal and the
 switching transient of the GSM transmitter.

The digital modulation incorporated in the GSM signal, for example, GMSK, 8-PSK with
 3π/8 rotation, causes the spectrum of the modulated carrier wave to spread to the
 adjacent channel. To test the effect of adjacent channel power, you can perform what is
 known as a spectrum due to modulation
measurement.

GSM has bursty signals, so the transmitter quickly ramps signal power up at the beginning
 of the burst and then down at the end of the burst. Also, the transmit power is switched
 on and off in accordance with the presence of active and idle time slots. These
 switching intervals may cause the distribution of transmit power to some unwanted
 spectral component. You can assess these unwanted spectral components of the spectrum
 using a spectrum due to the switching measurement. For more
 information on the GSM ORFS measurement and best practices, refer to the Output
 RF Spectrum (ORFS) section in the *Introduction to GSM Device
 Testing* application note<sup>[1]</sup>.

You can configure RFmxGSM ORFS measurements to use a predefined list of offset
 frequencies at which the power spectrum of the signal is assessed. These lists include
 standard and short offset frequency mode. For a spectrum due to modulation
 measurement, the standard mode contains the offset frequencies specified
 in section 13.4.4 of *3GPP TS 51.010-1* specifications.

| List | Modulation Offsets (kHz) | Switching Offsets (kHz) |
| --- | --- | --- |
| Standard | ±100, ±200, ±250, ±400, ±600, ±800, ±1000, ±1200, ±1400, ±1600, ±1800 | ±400, ±600, ±1200, ±1800 |
| Short | ±200, ±250, ±400, ±600, ±1200, ±1800 | ±400, ±600, ±1200, ±1800 |

Alternatively, you can specify the set of offset frequencies for which the ORFS
 measurement is performed. This feature is known as custom frequency
 mode.

For frequencies greater than or equal to 1800 KHz, the measurement bandwidth is 100 KHz,
 as defined in the *3GPP TS 45.005* specifications. For all other
 frequencies, the measurement bandwidth is 30 KHz.

#### Evaluation Symbols

Evaluation symbols are applicable to the spectrum due to modulation
 measurement. GSM standard specifies that 50% to 90% portion of the burst
 excluding the midamble is used for measurement. However, RFmx GSM allows you to specify
 which portion of the burst to use for the spectrum due to modulation
 measurement. RFmx GSM considers the measurement over evaluation symbols for
 a single burst as one average.

#### References

[1] NI RF Academy. (2014, February 01). Introduction to GSM Device Testing. Retrieved
 March 10, 2015, from
 http://download.ni.com/evaluation/rf/Introduction_to_GSM_Device_Testing.pdf

<!--NI_TOPIC bundle=rfmx-gsm path=pvt.html language=enus -->
## TOPIC 00004: PVT Measurement

- bundle_id: `rfmx-gsm`
- source_path: `pvt.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm/raw/resource/enus/pvt.html
- document_id: `rfmx-gsm`
- page_type: `leaf`
- content_type: `concept`
- source_description: Power versus time (PVT) is a time-domain measurement that compares the transmit power of the signal with standard-defined upper and lower masks. RFmx GSM uses the masks defined in Annex B of 3GPP TS 45.005 Technical Specifications. Masks vary according to the burst type, modulation type, power contr

### PVT Measurement

Power versus time (PVT) is a time-domain measurement that compares the transmit power of
 the signal with standard-defined upper and lower masks. RFmx GSM uses the masks defined
 in Annex B of *3GPP TS 45.005 Technical Specifications*. Masks vary
 according to the burst type, modulation type, power control level (PCL), link direction,
 and frequency band of the signal. To choose the mask, you must set the link direction
 and band, even if you have configured the center frequency. For more information on GSM
 PVT measurement refer to the *Power versus Time (PvT)* section in the
 *Introduction to GSM Device Testing* application
 note<sup>[1]</sup>.

The following image shows an example of an RFmx PVT trace with signal power, upper mask,
 and lower mask.

[IMAGE alt='image' src='GUID-53A165E7-3639-4AE0-A6A0-516067B5CDD9-a5.png']

#### PVT Multislot Mask

RFmx GSM supports PVT measurement for two or more consecutive occupied time slots.
 You can configure each occupied slot with a different burst type, modulation type,
 and PCL value. Multislot masks are formed from single slot masks as elaborated in
 section 4.5 of*3GPP TS 45.005 Technical Specifications*.

The following image shows the example of an RFmx GSM multislot PVT trace with an
 8-PSK slot followed by a GMSK slot.

[IMAGE alt='image' src='GUID-8D2514DE-B15F-4A20-B3C1-1A9867D08711-a5.png']

#### References

[1] NI RF Academy. (2014, February 01). Introduction to GSM Device Testing. Retrieved
 March 10, 2015, from
 http://download.ni.com/evaluation/rf/Introduction_to_GSM_Device_Testing.pdf

<!--NI_TOPIC bundle=rfmx-gsm path=rfmxgsm-overview.html language=enus -->
## TOPIC 00005: RFmx GSM Overview

- bundle_id: `rfmx-gsm`
- source_path: `rfmxgsm-overview.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm/raw/resource/enus/rfmxgsm-overview.html
- document_id: `rfmx-gsm`
- page_type: `leaf`
- content_type: `concept`
- source_description: This user manual contains introduction to RFmx GSM measurement concepts.

### RFmx GSM Overview

This user manual contains introduction to RFmx GSM measurement concepts.

<!--NI_TOPIC bundle=rfmx-gsm path=supported-hw.html language=enus -->
## TOPIC 00006: Supported Hardware

- bundle_id: `rfmx-gsm`
- source_path: `supported-hw.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm/raw/resource/enus/supported-hw.html
- document_id: `rfmx-gsm`
- page_type: `leaf`
- content_type: `concept`
- source_description: RFmx supports a number of NI devices. 1 RFmx GSM Supported Hardware RFmx GSM Hardware Earliest Driver Version Support (Windows 11) PXIe-5644 2022 Q3 PXIe-5645 2022 Q3 PXIe-5646 2022 Q3 PXIe-5663 2022 Q3 PXIe-5665 2022 Q3 PXIe-5668 2022 Q3 PXIe-5820 2022 Q3 PXIe-5840 2022 Q3 PXIe-5841 (200 MHz Bandwi

### Supported Hardware

RFmx supports a number of NI devices.

| RFmx GSM Hardware | Earliest Driver Version Support (Windows 11) |
| --- | --- |
| PXIe-5644 | 2022 Q3 |
| PXIe-5645 | 2022 Q3 |
| PXIe-5646 | 2022 Q3 |
| PXIe-5663 | 2022 Q3 |
| PXIe-5665 | 2022 Q3 |
| PXIe-5668 | 2022 Q3 |
| PXIe-5820 | 2022 Q3 |
| PXIe-5840 | 2022 Q3 |
| PXIe-5841 (200 MHz Bandwidth) | 2026 Q2 |
| PXIe-5842 | 2022 Q4 |
| PXIe-5860 | 2024 Q3 |

Note

RFmx GSM

NI-RFSA
 Properties

NI-RFSA LabVIEW VI Reference

For more information about your hardware and functionality, refer to the *NI-RFSA User Manual*.

<!--NI_TOPIC bundle=rfmx-gsm path=system-requirements.html language=enus -->
## TOPIC 00007: RFmx GSM System Requirements

- bundle_id: `rfmx-gsm`
- source_path: `system-requirements.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm/raw/resource/enus/system-requirements.html
- document_id: `rfmx-gsm`
- page_type: `leaf`
- content_type: `concept`
- source_description: RFmx GSM has the following requirements: Processor—1 GHz 64-bit (x64) processor 4 GB RAM * A screen resolution of 1,024 x 768 Any supported OS, with all available critical updates and service packs * Depending on the amount of data acquired and/or processed, a larger amount of memory may be required

### RFmx GSM System Requirements

RFmx GSM has the following requirements:

- Processor—1 GHz 64-bit (x64) processor
- 4 GB RAM *
- A screen resolution of 1,024 x 768
- Any supported OS, with all available critical updates and service packs

* Depending on the amount of data acquired and/or processed, a larger amount of memory
 may be required.

<!--NI_TOPIC bundle=rfmx-gsm path=user-manual-welcome.html language=enus -->
## TOPIC 00008: RFmx GSM User Manual

- bundle_id: `rfmx-gsm`
- source_path: `user-manual-welcome.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm/raw/resource/enus/user-manual-welcome.html
- document_id: `rfmx-gsm`
- page_type: `leaf`
- content_type: `concept`
- source_description: The RFmx GSM User Manual provides detailed descriptions of the product functionality and the step by step processes for use. Looking for Something Else?For information not found in the User Manual for your product, such as specifications and API reference, browse Related Information.

### RFmx GSM
 User Manual

The RFmx GSM User Manual provides detailed
 descriptions of the product functionality and the step by step processes for use.

#### Looking for Something Else?

For information not found in the User Manual
 for your product, such as specifications and API reference, browse *Related
 Information*.

Related information:

- Download RFmx GSM
- License Setup and Activation
- RFmx GSM Release Notes
- Getting Started with RFmx
- RFmx GSM LabVIEW Reference
- RFmx GSM .NET Reference
- RFmx GSM C Reference
- RFmx Instr LabVIEW Reference
- RFmx Instr .NET Reference
- RFmx Instr C Reference
