# NI DOCUMENT BUNDLE: rfmx-wcdma

<!--NI_BUNDLE_CHUNK bundle=rfmx-wcdma start=1 end=13 -->
<!--NI_TOPIC bundle=rfmx-wcdma path=marker-mode.html language=enus -->
## TOPIC 00001: Marker Mode

- bundle_id: `rfmx-wcdma`
- source_path: `marker-mode.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma/raw/resource/enus/marker-mode.html
- document_id: `rfmx-wcdma`
- page_type: `leaf`
- content_type: `concept`
- source_description: You must complete the following tasks in the Marker synchronization mode: Provide a digital trigger at the start of the frame. Configure a reference waveform corresponding to the transmitted signal. Set the Channel Configuration Mode property to Test Model and configure the UL Test model property

### Marker Mode

You must complete the following tasks in the Marker synchronization mode:

- Provide a digital trigger at the start of the frame.
- Configure a reference waveform corresponding to the transmitted signal.
- Set the Channel Configuration Mode property to Test Model and configure the UL Test model property according to the signal being transmitted, or set the Channel Configuration Mode property to User Defined and configure the Number of Channels and User Defined Channel (Array) properties according to the signal being transmitted.

You can create the reference waveform to be configured on the measurement in the following ways:

- Create the reference waveform using the NI WCDMA Waveform Generation Interactive Panel. This panel allows you to configure and save a waveform to file. Load the waveform from the file using the niRFSGPlayback Read Waveform From File VI and use the RFmxWCDMA ModAcc Configure Reference Waveform VI to configure it on the ModAcc measurement. To get the fastest measurement times, NI recommends that you use the shortest waveforms that satisfy the measurement length you want to use.
- Execute the ModAcc measurement in the Marker synchronization mode once without configuring the reference waveform. If you initiate a ModAcc measurement in the Marker synchronization mode without configuring the reference waveform, the measurement is performed and it detects the reference waveform from the acquired data, and stores the reference waveform as a result. You must fetch the reference waveform using the RFmxWCDMA
 ModAcc Fetch Reference Waveform VI after executing the measurement once, and you use the RFmxWCDMA ModAcc Configure Reference Waveform VI to configure the fetched waveform as the reference waveform. The measurement does not automatically use the detected reference waveform as the reference waveform. It is important to configure the reference waveform because executing the ModAcc measurement in Marker mode without configuring the reference waveform does not provide any speed benefits over executing the measurement in other synchronization modes.

<!--NI_TOPIC bundle=rfmx-wcdma path=new-features-and-changes.html language=enus -->
## TOPIC 00002: RFmx WCDMA New Features and Changes

- bundle_id: `rfmx-wcdma`
- source_path: `new-features-and-changes.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma/raw/resource/enus/new-features-and-changes.html
- document_id: `rfmx-wcdma`
- page_type: `leaf`
- content_type: `concept`
- source_description: Learn about updates, including new features and behavior changes, introduced in each version of RFmx WCDMA. Discover what is new in the latest releases of RFmx WCDMA.If you cannot find new features and changes for your version, it might not include user-facing updates. However, your version might in

### RFmx WCDMA
 New Features and Changes

Learn about updates, including new features and behavior changes, introduced in each
 version of RFmx WCDMA.

RFmx WCDMA

Note

Release Notes

Related information:

- Software and Driver Downloads

#### RFmx WCDMA
 2026 Q2 Changes

RFmx WCDMA 2026 Q2 includes behavior changes with ACP
 measurements that use the Sequential FFT measurement method. This release also adds support
 for the PXIe-5841 with 200
 MHz bandwidth.

##### Behavior Changes

This version of RFmx WCDMA updates support for the following feature:

- Adjacent Channel Power (ACP): When you use the Sequential FFT 
 measurement method, you can configure the Configuring the Number of
 Analysis Threads property to a value greater than 1.

##### New
 Hardware Support

This version of RFmx WCDMA
 adds support for the following hardware:

- PXIe-5841 ( 200 MHz ) bandwidth

#### RFmx WCDMA
 2025 Q3 Changes

Learn about new features, behavior changes, and other updates in RFmx WCDMA 2025 Q3.

##### New
 Features

This version of the RFmx WCDMA
 adds support for the following features:

- PXIe-5860 Self-Cal Validity Check

#### RFmx WCDMA
 2024 Q4 Changes

Learn about new features, behavior changes, and other updates in RFmx WCDMA 2024 Q4.

##### New
 Features

This version of the RFmx WCDMA
 adds support for the following features:

- Uninstalling RFmx WCDMA software also removes any
 previous versions of RFmx WCDMA .NET runtimes that
 were leaked in .NET Global Assembly Cache directory.

#### RFmx WCDMA
 2024 Q3 Changes

Learn about new features, behavior changes, and other updates in RFmx WCDMA 2024 Q3.

##### New
 Hardware Support

This version of the RFmx WCDMA adds support for the following
 hardware:

- PXIe-5860

#### RFmx WCDMA
 2024 Q2 Changes

Learn about new features, behavior changes, and other updates in RFmx WCDMA 2024 Q2.

- Obsoleted the RFmxInstr Load All Configurations VI. Use the
 RFmxInstr Load Configurations VI along with the appropriate
 RFmxInstr Load Options property, instead.

#### RFmx WCDMA 2023 Q4 New Features and
 Changes

- Support for obtaining unprocessed I/Q data utilized for RFmx measurements

#### RFmx WCDMA 2023 Q2 New Features and
 Changes

- Speed improvements for Composite and Spectral measurements

#### RFmx WCDMA 2023 Q1 New Features and
 Changes

- Support for LabVIEW 2023 Q1 (64-bit)

<!--NI_TOPIC bundle=rfmx-wcdma path=rfmxwcdma-overview.html language=enus -->
## TOPIC 00003: RFmx WCDMA Overview

- bundle_id: `rfmx-wcdma`
- source_path: `rfmxwcdma-overview.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma/raw/resource/enus/rfmxwcdma-overview.html
- document_id: `rfmx-wcdma`
- page_type: `leaf`
- content_type: `concept`
- source_description: This user manual contains introduction to RFmx WCDMA measurement concepts.

### RFmx WCDMA Overview

This user manual contains introduction to RFmx WCDMA
 measurement concepts.

<!--NI_TOPIC bundle=rfmx-wcdma path=supported-hw.html language=enus -->
## TOPIC 00004: Supported Hardware

- bundle_id: `rfmx-wcdma`
- source_path: `supported-hw.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma/raw/resource/enus/supported-hw.html
- document_id: `rfmx-wcdma`
- page_type: `leaf`
- content_type: `concept`
- source_description: RFmx supports a number of NI devices. 1 RFmx WCDMA Supported Hardware RFmx WCDMA Hardware Earliest Driver Version Support (Windows 11) PXIe-5644 2022 Q3 PXIe-5645 2022 Q3 PXIe-5646 2022 Q3 PXIe-5663 2022 Q3 PXIe-5663E 2022 Q3 PXIe-5665 2022 Q3 PXIe-5668 2022 Q3 PXIe-5820 2022 Q3 PXIe-5840 2022 Q3 PX

### Supported Hardware

RFmx supports a number of NI devices.

| RFmx WCDMA Hardware | Earliest Driver Version Support (Windows 11) |
| --- | --- |
| PXIe-5644 | 2022 Q3 |
| PXIe-5645 | 2022 Q3 |
| PXIe-5646 | 2022 Q3 |
| PXIe-5663 | 2022 Q3 |
| PXIe-5663E | 2022 Q3 |
| PXIe-5665 | 2022 Q3 |
| PXIe-5668 | 2022 Q3 |
| PXIe-5820 | 2022 Q3 |
| PXIe-5840 | 2022 Q3 |
| PXIe-5841 (1 GHz Bandwidth) | 2022 Q3 |
| PXIe-5841 (200 MHz Bandwidth) | 2026 Q2 |
| PXIe-5842 | 2022 Q4 |
| PXIe-5860 | 2024 Q3 |

Note

RFmx WCDMA

NI-RFSA
 Properties

NI-RFSA LabVIEW VI Reference

For more information about your hardware and functionality, refer to the *NI-RFSA
 User Manual*.

<!--NI_TOPIC bundle=rfmx-wcdma path=system-requirements.html language=enus -->
## TOPIC 00005: RFmx WCDMA System Requirements

- bundle_id: `rfmx-wcdma`
- source_path: `system-requirements.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma/raw/resource/enus/system-requirements.html
- document_id: `rfmx-wcdma`
- page_type: `leaf`
- content_type: `concept`
- source_description: RFmx WCDMA has the following requirements: Processor—1 GHz 64-bit (x64) processor 4 GB RAM * A screen resolution of 1,024 x 768 Any supported OS, with all available critical updates and service packs * Depending on the amount of data acquired and/or processed, a larger amount of memory may be requir

### RFmx WCDMA System Requirements

RFmx WCDMA has the following requirements:

- Processor—1 GHz 64-bit (x64) processor
- 4 GB RAM *
- A screen resolution of 1,024 x 768
- Any supported OS, with all available critical updates and service packs

* Depending on the amount of data acquired and/or processed, a larger amount of memory
 may be required.

<!--NI_TOPIC bundle=rfmx-wcdma path=user-manual-welcome.html language=enus -->
## TOPIC 00006: RFmx WCDMA User Manual

- bundle_id: `rfmx-wcdma`
- source_path: `user-manual-welcome.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma/raw/resource/enus/user-manual-welcome.html
- document_id: `rfmx-wcdma`
- page_type: `leaf`
- content_type: `concept`
- source_description: The RFmx WCDMA User Manual provides detailed descriptions of the product functionality and the step by step processes for use. Looking for Something Else?For information not found in the User Manual for your product, such as specifications and API reference, browse Related Information.

### RFmx WCDMA
 User Manual

The RFmx WCDMA User Manual provides detailed
 descriptions of the product functionality and the step by step processes for use.

#### Looking for Something Else?

For information not found in the User Manual
 for your product, such as specifications and API reference, browse *Related
 Information*.

Related information:

- Download RFmx WCDMA
- License Setup and Activation
- RFmx WCDMA Release Notes
- Getting Started with RFmx
- RFmx WCDMA LabVIEW Reference
- RFmx WCDMA .NET Reference
- RFmx WCDMA C Reference
- RFmx Instr LabVIEW Reference
- RFmx Instr .NET Reference
- RFmx Instr C Reference

<!--NI_TOPIC bundle=rfmx-wcdma path=wcdma-adjacent-channel-power-acp.html language=enus -->
## TOPIC 00007: WCDMA Adjacent Channel Power (ACP)

- bundle_id: `rfmx-wcdma`
- source_path: `wcdma-adjacent-channel-power-acp.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma/raw/resource/enus/wcdma-adjacent-channel-power-acp.html
- document_id: `rfmx-wcdma`
- page_type: `leaf`
- content_type: `concept`
- source_description: The RFmx WCDMA ACP measurement uses the configurations specified in 3GPP TS 34.121-1, version 11.5.0. This topic describes the configuration used by the RFmx WCDMA ACP measurement. For more details on WCDMA ACP measurement refer to the Adjacent Channel Leakage Ratio (ACLR) section in the Introductio

### WCDMA Adjacent Channel Power (ACP)

The RFmx WCDMA ACP measurement uses the configurations specified in *3GPP TS
 34.121-1*, version 11.5.0. This topic describes the configuration used by the RFmx
 WCDMA ACP measurement. For more details on WCDMA ACP measurement refer to the
 Adjacent Channel Leakage Ratio (ACLR) section in the
 Introduction to UMTS Device Testing application note<sup>[1]</sup>

ACP Overview

Refer to Adjacent Channel Power (ACP) for an overview of ACP measurements.

#### Single Carrier

Single-carrier ACP is the ratio of the RRC-filtered mean power centered on the carrier
 channel to the RRC-filtered mean power centered on an adjacent channel, according to the 3GPP
 WCDMA standard.

#### Multicarrier

Multicarrier ACP is the ratio of the sum of the RRC-filtered mean powers centered on each of
 the carrier channels to the RRC-filtered mean power centered on an adjacent channel, according
 to the 3GPP WCDMA standard.

#### Carrier Channels

Carrier channels are transmitted by the user equipment (UE) when the measurement is
 performed. You can configure multiple carrier channels by specifying the carrier offsets. The
 spacing between neighboring carrier channels should be a minimum of 5 MHz to avoid any overlap
 between the channels. To configure contiguous channels, the spacing should be 5 MHz between
 neighboring channels. The carrier channels are RRC filtered with a roll-off factor of 0.22
 over a bandwidth of 3.84 MHz. The carrier powers are obtained on the RRC-filtered signal.

#### Offset Channels

Offset channels are adjacent to the carrier channels. Each offset channel is RRC filtered
 with a roll-off factor of 0.22 over a bandwidth of 3.84 MHz. The offset powers are obtained on
 the RRC-filtered signal. For a single-carrier ACP measurement, the adjacent channels are
 centered at integral multiples of the WCDMA channel bandwidth (5 MHz) from the center of the
 carrier channel. For multicarrier ACP measurements, the adjacent channels are centered at
 integral multiples of the WCDMA channel bandwidth (5 MHz) from the centers of the first and
 last carrier channels. The number of offset channels defaults to 2 as specified in the 3GPP
 standard. For multicarrier ACP, the power reference defaults to the sum of the carrier channel
 powers (Composite), to conform to the 3GPP standard.

#### References

[1] NI RF Academy. (2014, February 01). Introduction to UMTS Device Testing. Retrieved March
 10, 2015, from
 http://download.ni.com/evaluation/rf/Introduction_to_UMTS_Device_Testing.pdf

<!--NI_TOPIC bundle=rfmx-wcdma path=wcdma-channel-power-chp.html language=enus -->
## TOPIC 00008: WCDMA Channel Power (CHP)

- bundle_id: `rfmx-wcdma`
- source_path: `wcdma-channel-power-chp.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma/raw/resource/enus/wcdma-channel-power-chp.html
- document_id: `rfmx-wcdma`
- page_type: `leaf`
- content_type: `concept`
- source_description: The RFmx WCDMA CHP measurement uses the configurations specified in 3GPP TS 34.121-1, version 11.5.0. The following section describes the configurations used by the RFmx WCDMA CHP measurement. The channel power is useful for measuring the maximum output power as defined in the 3GPP WCDMA standard. I

### WCDMA Channel Power (CHP)

The RFmx WCDMA CHP measurement uses the configurations specified in *3GPP TS
 34.121-1*, version 11.5.0. The following section describes the configurations used
 by the RFmx WCDMA CHP measurement.

The channel power is useful for measuring the maximum output power as defined in the 3GPP
 WCDMA standard. It indicates the maximum power that the user equipment (UE) can transmit. For
 multicarrier CHP, the transmit power is equal to the sum of the individual powers of each
 carrier channel. Each carrier channel power should be measured over a minimum bandwidth 1 + α
 times the chip rate, where α is the roll-off factor of the RRC filter. The time interval over
 which the measurement takes place should be a minimum of one time slot. The measurement
 bandwidth defaults to 5 MHz, and the sweep time defaults to one slot duration.

CHP Overview

Refer to Channel Power (CHP) for an overview of CHP measurements.

#### Carrier Channels

The carrier channels are transmitted by the UE when the measurement is performed. You can
 configure multiple carrier channels by specifying the carrier offsets. The spacing between
 neighboring carrier channels should be a minimum of 5 MHz to avoid any overlap between the
 channels. To configure contiguous channels, the spacing should be 5 MHz between neighboring
 channels. The carrier channels are RRC-filtered with a roll-off factor of 0.22 over a
 bandwidth of 3.84 MHz.

<!--NI_TOPIC bundle=rfmx-wcdma path=wcdma-modulation-accuracy-modacc.html language=enus -->
## TOPIC 00009: WCDMA Modulation Accuracy (ModAcc)

- bundle_id: `rfmx-wcdma`
- source_path: `wcdma-modulation-accuracy-modacc.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma/raw/resource/enus/wcdma-modulation-accuracy-modacc.html
- document_id: `rfmx-wcdma`
- page_type: `leaf`
- content_type: `concept`
- source_description: The key results of RFmx WCDMA ModAcc measurements are the RMS EVM, peak EVM, Rho, frequency error, chip rate error, and code domain errors (CDEs). The CDE results include results related to peak CDE, peak RCDE, peak active CDE, and active CDE. For more information on WCDMA modulation accuracy measur

### WCDMA Modulation Accuracy (ModAcc)

The key results of RFmx WCDMA ModAcc measurements are the RMS EVM, peak EVM, Rho,
 frequency error, chip rate error, and code domain errors (CDEs). The CDE results include
 results related to peak CDE, peak RCDE, peak active CDE, and active CDE. For more
 information on WCDMA modulation accuracy measurement refer to the *Transmit
 Modulation Quality* section in the *Introduction to UMTS Device
 Testing* application note<sup>[1]</sup>.

The ModAcc measurement supports the following channel configuration modes:

- Set the Channel Configuration Mode property to Auto Detect ,
 so the measurement detects the channels. This value is the default.
- Set the Channel Configuration Mode property to Test Model, and set the UL Test Model property to use a predefined test model.
- Set the Channel Configuration Mode property to User Defined 
 to use a custom channel configuration.

The WCDMA ModAcc Frame, Slot, and Arbitrary synchronization modes enable you to
 synchronize to the frame, slot, or symbol boundary. RFmx WCDMA does ModAcc measurements
 over the configured number of slots, starting at the configured offset, in slots, from
 that boundary. The Frame synchronization mode allows you to measure specific slots in a
 frame, while slot mode allows you to start the measurement from the first complete slot
 in the acquisition. The Arbitrary synchronization mode allows you to start the
 measurement from the first complete symbol in the acquisition while the Marker
 synchronization mode enables you to obtain the fastest ModAcc measurement. For more
 information on the structure of the WCDMA frame, refer to the *UMTS Frame
 Structure* section in the *Introduction to UMTS Device
 Testing* application note<sup>[1]</sup>.

#### Single Carrier

The default value of the Number of Carriers property is 1. Using this property, the ModAcc
 results for a single WCDMA carrier will be obtained.

#### Multi Carrier

- UL Scrambling Type and UL Scrambling Code.
- DL Scrambling Type, DL Scrambling Primary Code, and DL Scrambling Secondary
 Code.

Additionally, you must configure Test Model or User Defined Channels for each
 carrier, when you set the Channel Configuration Mode property to Test
 Model or User Defined, respectively.

Multicarrier ModAcc gives out the ModAcc measurement results separately for each of
 the configured carriers. Multicarrier ModAcc gives out an additional result called
 Multicarrier I/Q Origin Offset when the Transmitter Architecture property is set to
 LO per Band.

Set the Transmitter Architecture property to LO per Carrier
 when your transmitter has an LO at the center of each carrier or has the LO at the
 center of one of the carriers. The estimate of I/Q origin offset of each carrier is
 available in the IQ Origin Offset result.

[IMAGE alt='image' src='GUID-6865C1C4-6496-4200-AD8A-65876D6A3B8D-a5.png']

Set Transmitter Architecture property to LO per Band when your
 transmitter has the LO at the center of all the carriers in the band. The measured
 I/Q origin offset for the LO per Band architecture is available in the Multicarrier
 IQ Origin Offset result.

[IMAGE alt='image' src='GUID-AF693416-10D2-48FB-9B63-C307EFAD7E9B-a5.png']

Note: The carrier-specific I/Q origin offset is always
 calculated irrespective of the value of the Transmitter Architecture property.

#### Carrier Channels

Carrier channels are transmitted by the user equipment (UE) when the measurement is
 performed. You can configure multiple carrier channels by specifying the carrier
 offsets. The spacing between neighboring carrier channels should be a minimum of 5 MHz
 to avoid any overlap between the channels. To configure contiguous channels, the spacing
 should be 5 MHz between neighboring channels. The carrier channels are RRC filtered with
 a roll-off factor of 0.22 over a bandwidth of 3.84 MHz.

Note: The following settings are not supported for multicarrier
 ModAcc:

- ModAcc Synchronization Mode = Marker
- RRC Filter Enabled = False

#### References

[1] NI RF Academy. (2014, February 01). Introduction to UMTS Device Testing. Retrieved
 March 10, 2015, from
 http://download.ni.com/evaluation/rf/Introduction_to_UMTS_Device_Testing.pdf

<!--NI_TOPIC bundle=rfmx-wcdma path=wcdma-occupied-bandwidth-obw.html language=enus -->
## TOPIC 00010: WCDMA Occupied Bandwidth (OBW)

- bundle_id: `rfmx-wcdma`
- source_path: `wcdma-occupied-bandwidth-obw.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma/raw/resource/enus/wcdma-occupied-bandwidth-obw.html
- document_id: `rfmx-wcdma`
- page_type: `leaf`
- content_type: `concept`
- source_description: The RFmx WCDMA OBW measurement uses the configurations specified in 3GPP TS 34.121-1, version 11.5.0. The following sections describe the configurations used by the RFmx WCDMA OBW measurement. OBW Overview Refer to Occupied Bandwidth (OBW) for an overview of OBW measurements. Single-Carrier OBW OBW

### WCDMA Occupied Bandwidth (OBW)

The RFmx WCDMA OBW measurement uses the configurations specified in *3GPP TS
 34.121-1,* version 11.5.0. The following sections describe the configurations used
 by the RFmx WCDMA OBW measurement.

OBW Overview

Refer to Occupied Bandwidth (OBW) for an overview of OBW measurements.

#### Single-Carrier OBW

OBW indicates the bandwidth that contains 99 percent of the total power of the transmitted
 spectrum at the center of the transmitted carrier. The OBW is measured using a span of twice
 the WCDMA channel bandwidth (5 MHz), that is, a span of 10 MHz.

#### Multicarrier OBW

You can configure multiple carrier channels by specifying the carrier offsets. The spacing
 between neighboring carrier channels should be at least a channel bandwidth of 5 MHz to avoid
 any overlap between the channels. OBW indicates the bandwidth that contains 99 percent of the
 total power centered around the center frequencies of the carriers. The span used for the
 measurement is twice the bandwidth from the start of channel bandwidth of the first carrier to
 the end of the channel bandwidth of the last carrier. Thus when two contiguous carriers are
 configured, the span used is 20 MHz.

#### RBW Filter

RBW filter type defaults to Gaussian to conform to the 3GPP standard.
 RBW Bandwidth Auto defaults to True, which configures the RBW value to
 30 kHz so that it conforms to the 3GPP standard.

<!--NI_TOPIC bundle=rfmx-wcdma path=wcdma-qpsk-evm.html language=enus -->
## TOPIC 00011: WCDMA QPSK EVM (QEVM)

- bundle_id: `rfmx-wcdma`
- source_path: `wcdma-qpsk-evm.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma/raw/resource/enus/wcdma-qpsk-evm.html
- document_id: `rfmx-wcdma`
- page_type: `leaf`
- content_type: `concept`
- source_description: QEVM Measurement is similar to the Modulation accuracy measurement with the exception that it expects the acquired waveform to be a QPSK modulated signal. The acquired waveform can typically be one of the following: An uplink WCDMA signal with one BPSK code channel An uplink WCDMA signal with BPSK c

### WCDMA QPSK EVM (QEVM)

QEVM Measurement is similar to the Modulation accuracy measurement with the exception that it expects the acquired waveform to be a QPSK modulated signal. The acquired waveform can typically be one of the following:

- An uplink WCDMA signal with one BPSK code channel
- An uplink WCDMA signal with BPSK code channels of equal powers present in the in-phase and quadrature branch
- A QPSK modulated signal with transmit filtering
- A BPSK modulated signal with scrambling and transmit filtering

For any of the previously mentioned transmit signals, the sampling rate should be equal to the WCDMA chip rate. The transmit filter should be an RRC filter with a roll-off factor (α) of 0.22. The spreading and scrambling, if used, should be compliant to the WCDMA standard.

This measurement is useful during the initial stages of development, when only the transmit modulator and transmit RRC filter are ready to be evaluated. Subsequently the same measurement can continue to be used when the transmitter development progresses to be more WCDMA compliant. Thus, QEVM measurement is useful across the design cycle of the transmitter.

Scrambling and number of channels can change the absolute phase of the signal by 45 degrees. However, all the previously mentioned typical test signals will be seen as QPSK constellation, since the measurement is agnostic to the absolute phase of the received signal and always assumes QPSK.
 The key results of the RFmx WCDMA QEVM measurements are RMS EVM, peak EVM, frequency error, chip rate error, and I/Q origin offset.
QEVM measurement allows averaging across multiple acquisitions.

Related concepts:

- WCDMA Modulation Accuracy (ModAcc)

<!--NI_TOPIC bundle=rfmx-wcdma path=wcdma-slotphase.html language=enus -->
## TOPIC 00012: WCDMA SlotPhase

- bundle_id: `rfmx-wcdma`
- source_path: `wcdma-slotphase.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma/raw/resource/enus/wcdma-slotphase.html
- document_id: `rfmx-wcdma`
- page_type: `leaf`
- content_type: `concept`
- source_description: The primary objective of the SlotPhase measurement is to obtain the phase discontinuity at each slot boundary. SlotPhase measurement is also useful to obtain the phase of the corrected received signal with respect to an ideal signal. This phase information is obtained for all the chips within the me

### WCDMA SlotPhase

The primary objective of the SlotPhase measurement is to obtain the phase discontinuity at
 each slot boundary. SlotPhase measurement is also useful to obtain the phase of the
 corrected received signal with respect to an ideal signal. This phase information is
 obtained for all the chips within the measurement interval.

#### Phase Discontinuity

According to the 3GPP standard, phase discontinuity result is the change in phase between
 adjacent timeslots. Phase discontinuity is obtained as follows:

1. The received signal is corrected for frequency, absolute phase, absolute amplitude, and
 chip clock timing based on the ideal signal.
2. The transient period of 25 microseconds is removed from the start and end of the slot, and
 a linear fit of the phase of the corrected signal is obtained for the slot.
3. This linear fit of the phase is extrapolated to the slot boundaries. The slope of this
 linear fit indicates the frequency error.
4. The same steps are repeated for all the slots. The difference between the first
 extrapolated chip phase of the current slot and the last extrapolated chip phase of the
 preceding slot is measured as the phase discontinuity. There is a provision to disable the
 removal of the transient period, if required, for signals which do not have a power change
 between slots.

[IMAGE alt='image' src='GUID-54EF2A4E-C67A-4366-B1CF-2B2A961A455B-a5.gif']

The key result of SlotPhase measurement is the array of phase discontinuity values for all
 slot boundaries within the selected measurement interval. Apart from this, the measurement
 returns results corresponding to the Maximum Phase Discontinuity, Discontinuity Count > 36
 degrees , Discontinuity Count > 66 degrees, and Minimum Distance between Discontinuities
 > 36 degrees.

The measurement allows us to view the traces for chip phase error and chip phase error linear
 fit. The WCDMA SlotPhase measurement supports the following channel configuration modes:

- Set the Channel Configuration Mode property to Auto Detect, so the measurement detects the
 transmitted channels. This value is the default.
- Set the Channel Configuration Mode property to Test Model, and set the UL Test Model
 property to use a predefined test model.
- Set the Channel Configuration Mode property to User Defined to use a custom channel
 configuration.

The WCDMA SlotPhase synchronization modes enable you to synchronize to the frame or slot
 boundaries. It allows you to measure specific slots in a frame, where as the slot mode starts
 the measurement from the first complete slot in the acquisition.

RFmx WCDMA supports the following synchronization modes:

- Slot synchronization mode—Allows you to make SlotPhase measurements over the configured
 number of slots, starting at the configured offset from the first complete slot in the
 acquisition.
- Frame synchronization mode—Allows you to make SlotPhase measurements over the configured
 number of slots, starting at the configured offset from the first complete frame in the
 acquisition. This mode allows you to measure specific slots in a frame.

The WCDMA SlotPhase measurement allows multi-frame measurement.

<!--NI_TOPIC bundle=rfmx-wcdma path=wcdma-spectral-emission-mask-sem.html language=enus -->
## TOPIC 00013: WCDMA Spectral Emission Mask (SEM)

- bundle_id: `rfmx-wcdma`
- source_path: `wcdma-spectral-emission-mask-sem.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma/raw/resource/enus/wcdma-spectral-emission-mask-sem.html
- document_id: `rfmx-wcdma`
- page_type: `leaf`
- content_type: `concept`
- source_description: The RFmx WCDMA SEM measurement uses the configurations and masks specified in 3GPP TS 34.121-1 specification, version 11.5.0. Spectrum emissions mask is one of the two spectral emissions measurements defined by the UMTS, also known as WCDMA, standard. The SEM measurement has easier acceptance criter

### WCDMA Spectral Emission Mask (SEM)

The RFmx WCDMA SEM measurement uses the configurations and masks specified in *3GPP TS
 34.121-1* specification, version 11.5.0. Spectrum emissions mask is one of the two
 spectral emissions measurements defined by the UMTS, also known as WCDMA, standard. The SEM
 measurement has easier acceptance criteria, and is designed to capture unwanted spurious
 products that the user equipment (UE) might emit. By contrast, the ACP measurement is
 generally considered to have a more difficult acceptance criteria, and is predominantly used
 as a metric of the non-linearity of the transmitter’s PA. The SEM is a mask defined for
 out-of-channel emissions relative to the in-channel power and this measurement ensures that
 the signal in adjacent channels falls off in a manner that minimizes interference. The SEM of
 the UE applies to frequencies between 2.5 MHz and 12.5 MHz away from the UE center frequency.
 You can measure the emissions in the frequency range that are closest to the carrier (2.5 MHz
 to 3.5 MHz) by using a Gaussian filter with a bandwidth of 30 kHz. By contrast, emissions
 measured in a frequency offset ranging from 4 MHz to 12.5 MHz require a measurement bandwidth
 of 1 MHz <sup>[1]</sup>. The following sections describe the configuration and masks used by
 the RFmx WCDMA SEM measurement.

SEM Overview

Refer to Spectral Emission Mask (SEM) for an overview of SEM measurements.

#### Carrier Channels

The user equipment (UE) transmits the carrier channels when the measurement is performed. You
 can configure multiple carrier channels by specifying the carrier offsets. Ensure that there
 is at least 5 MHz between neighboring carrier channels to avoid any overlap between the
 channels. To configure contiguous channels, the spacing should be 5 MHz between neighboring
 channels. The carrier channels are RRC filtered with a roll-off factor of 0.22 over a
 bandwidth of 3.84 MHz. The carrier powers are obtained on the RRC-filtered signal.

#### Offset Segments

You can measure the offset segment powers with the corresponding measurement bandwidths using
 a Gaussian RBW filter.

#### Masks

The power of any UE emission does not exceed the levels specified in the following tables
 for different offset segments.  The requirements shown in the tables take into account the
 tolerance allowed by the standard.

#### Single Carrier

The SEM of the UE applies to frequencies that are between 2.5 MHz and 12.5 MHz away from the
 center of the UE carrier. The power of any UE emission does not exceed the levels specified in
 the following tables. For absolute masks, the additional requirements for specific masks are
 also provided in the following tables. However, since these additional masks are less
 stringent than the default mask, these do not impact the measurement results. For the relative
 mask, the power of the out-of-channel emission is specified relative to the RRC-filtered mean
 power of the UE carrier. According to 3GPP TS 34.121-1 specification,
 version 11.5.0, the measurement passes if either the absolute or the relative masks are met
 for each offset segment.

The following table describes the base requirements of a single carrier.

| Frequency Offsets from Center of the Carrier to the Center of the Measurement Bandwidth in the Offset segments Δf (MHz) | Absolute Requirement (dBm) | Relative Requirement (dBc) | Measurement Bandwidth |
| --- | --- | --- | --- |
| 2.515 to 3.485 | -69.6 | -33.5 - 15*(Δf/MHz - 2.5) | 30 kHz |
| 4.0 to 7.5 | -54.3 | -33.5 - 1*(Δf/MHz - 3.5) | 1 MHz |
| 7.5 to 8.5 | -54.3 | -37.5 - 10*(Δf/MHz - 7.5) | 1 MHz |
| 8.5 to 12.0 | -54.3 | -47.5 | 1 MHz |

The following table describes the additional requirements of a single carrier.

| Frequency Offsets from Center of the Carrier to the Center of the Measurement bandwidth in the Offset segments Δf (MHz) | Absolute Requirement (dBm) | Measurement Bandwidth | Band |
| --- | --- | --- | --- |
| 2.515 to 3.485 | -15 | 30 KHz | II, IV, X, XXV |
| 4.000 to 12.000 | -13 | 1 MHz |  |
| 2.515 to 3.485 | -15 | 30 KHz | V, XXVI |
| 3.550 to 12.450 | -13 | 100 KHz |  |
| 2.515 to 3.485 | -13 | 30 KHz | XII, XIII, XXIV |
| 3.550 to 12.450 | -13 | 100 KHz |  |

#### Multi-Carrier

For dual-carrier SEM, the spectrum emission mask of the UE applies to frequencies that are
 between 5 MHz and 20 MHz away from the center frequency of the two assigned channel
 frequencies. The requirements assume that the UE output power is the maximum output power
 level. The test requirements take into account the tolerance allowed by the standard.
 Additional masks, applicable for specific bands, are specified in the following table. There
 are no relative masks for dual-carrier SEM. The dual-carrier masks described in the following
 tables are extended to more than two carriers by increasing all the absolute frequency offsets
 by 2.5 MHz for each additional carrier beyond two carriers. The measurement passes if the
 absolute mask is met for each offset segment.

The following table describes the base requirements of a dual-carrier SEM.

| Frequency Offsets from Center of the Carriers to Center of the Measurement bandwidth in the Offset segments Δf (MHz) | Absolute Requirement (dBm) | Measurement Bandwidth |
| --- | --- | --- |
| ±5.015 to ±5.985 | -16.5 | 30 kHz |
| ±6.5 to ±10.0 | -8.5 | 1 MHz |
| ±10.0 to ±19.0 | -11.5 | 1 MHz |
| ±19.0 to ±19.5 | -23.5 | 1 MHz |

The following table describes the additional requirements of a dual-carrier SEM.

| Frequency Offsets from Center of the Carriers to center of the Measurement Bandwidth in the Offset Segments Δf (MHz) | Absolute Requirement (dBm) | Measurement Bandwidth | Band |
| --- | --- | --- | --- |
| 5.015 to 5.985 | -18 | 30 kHz | II, IV, V, X, XXV and XXVI |
| 6.5 to 19.0 | -13 | 1 MHz |  |
| 19.0 to 19.5 | -25 | 1 MHz |  |

#### References

[1] NI RF Academy. (2014, February 01). Introduction to UMTS Device Testing. Retrieved March
 10, 2015, from
 http://download.ni.com/evaluation/rf/Introduction_to_UMTS_Device_Testing.pdf
