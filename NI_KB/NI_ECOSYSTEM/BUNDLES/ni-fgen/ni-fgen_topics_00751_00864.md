# NI DOCUMENT BUNDLE: ni-fgen

<!--NI_BUNDLE_CHUNK bundle=ni-fgen start=751 end=864 -->
<!--NI_TOPIC bundle=ni-fgen path=ni-5451-fir-filter-type.html language=enus -->
## TOPIC 00751: NI 5451 FIR Filter Type

- bundle_id: `ni-fgen`
- source_path: `ni-5451-fir-filter-type.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5451-fir-filter-type.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the FIR Filter Type property or the NIFGEN_ATTR_OSP_FIR_FILTER_TYPE attribute to set the FIR filter type. The following filter types are supported: Flat Raised Cosine Root Raised Cosine

### NI 5451 FIR Filter Type

Use the 
FIR Filter
Type property or the 
NIFGEN_ATTR_OSP_FIR_FILTER_TYPE attribute to set the FIR filter type. The following filter
types are supported:

- Flat
- Raised
Cosine
- Root
Raised Cosine

Parent topic:

NI 5451 Basic Onboard Signal Processing Properties

Related concepts:

- NI 5451 FIR Filter Type: Flat
- NI 5451 FIR Filter Type: Raised Cosine
- NI 5451 FIR Filter Type: Root Raised Cosine

<!--NI_TOPIC bundle=ni-fgen path=ni-5451-fir-filter-types.html language=enus -->
## TOPIC 00752: NI 5451 FIR Filter Types

- bundle_id: `ni-fgen`
- source_path: `ni-5451-fir-filter-types.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5451-fir-filter-types.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: There are a number of built-in low-pass pulse-shaping filters available in NI-FGEN. Because the coefficients are scaled for unity-gain, the filters may overflow if transients (such as step response) are presented at the input of the filter. Use the Filter Type property or the NIFGEN_ATTR_OSP_FIR_FIL

### NI 5451 FIR Filter Types

There are a number of built-in low-pass pulse-shaping filters
available in NI-FGEN. 
 Because the coefficients are scaled for unity-gain,
the filters may overflow if transients (such as step response) are
presented at the input of the filter. Use the 
Filter
Type property or the 
NIFGEN_ATTR_OSP_FIR_FILTER_TYPE attribute to set the *FIR filter type*. The following filters
are currently available:

- Flat
- Raised
Cosine
- Root
Raised Cosine

Note

NIFGEN_ATTR_OSP_COMPENSATE_FILTER_GROUP_DELAY

#### Digital Filter Overflow

FIR filters may overflow. If an overflow occurs, data is clipped and NI-FGEN returns an error.

Digital filter overflows can be caused by transients. Transients can occur as an abrupt jump at the beginning of a waveform or they may be present in the data you supply. NI-FGEN ignores overflows that are caused by transients at the beginning of a waveform. You can choose to ignore overflow errors caused by transients present in your data with the 
OSP Overflow Error Reporting property or the 
NIFGEN_ATTR_OSP_OVERFLOW_ERROR_REPORTING attribute.

Parent topic:

NI 5451 Filtering and Interpolation

Related concepts:

- NI 5451 FIR Filter Type
- NI 5451 FIR Filter Type: Flat
- NI 5451 FIR Filter Type: Raised Cosine
- NI 5451 FIR Filter Type: Root Raised Cosine

<!--NI_TOPIC bundle=ni-fgen path=ni-5451-flatness-correction.html language=enus -->
## TOPIC 00753: NI 5451 Flatness Correction

- bundle_id: `ni-fgen`
- source_path: `ni-5451-flatness-correction.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5451-flatness-correction.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5451 can use flatness correction to ensure a consistent power level across frequencies when generating arbitrary waveforms or I/Q data. Flatness correction is disabled by default in NI-FGEN. You can enable or disable flatness correction by setting the Flatness Correction Enabled property or t

### NI 5451 Flatness Correction

The NI 5451 can use flatness correction to ensure
a consistent power level across frequencies when generating arbitrary waveforms or I/Q data. Flatness correction is disabled by default in NI-FGEN. You can enable or disable flatness correction by setting the 
Flatness Correction Enabled property or the 
NIFGEN_ATTR_FLATNESS_CORRECTION_ENABLED attribute.

During external calibration, the frequency response
of the analog path in its different configurations is measured
using the 
niFgen Initialize Flatness Calibration VI or the 
niFgen_InitializeFlatnessCalibration function and the 
niFgen Cal Adjust Flatness
VI or the 
niFgen_CalAdjustFlatness function.

During generation, these measured values are used
to compensate for any attenuation at the requested sample rate. The
compensation is applied by a flatness-correcting FIR filter. This FIR filter applies attenuation to higher power frequencies so that they become equal to the attenuated frequencies. As a result, the maximum gain is reduced as described in the *Analog Gain Settings* topic.

Flatness correction applies to a limited frequency band. Refer to the 
*device
specifications* for information about the flatness correction available on your device.

Parent topic:

NI 5451 Waveform Amplitude Control

Related concepts:

- NI 5451 Analog Gain Settings

<!--NI_TOPIC bundle=ni-fgen path=ni-5451-frequency-shift-property.html language=enus -->
## TOPIC 00754: NI 5451 Frequency Shift Property

- bundle_id: `ni-fgen`
- source_path: `ni-5451-frequency-shift-property.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5451-frequency-shift-property.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Frequency Shift property or the NIFGEN_ATTR_OSP_FREQUENCY_SHIFT attribute can be used to shift the frequency of a baseband signal. This property can only be used when the OSP mode has been configured for baseband by setting the OSP Mode property or the NIFGEN_ATTR_OSP_MODE attribute. When you ar

### NI 5451 Frequency Shift Property

The Frequency Shift property or the NIFGEN_ATTR_OSP_FREQUENCY_SHIFT attribute can be used to shift the frequency of a baseband signal. This property can only be used when the OSP mode has been configured for baseband by setting the OSP Mode property or the NIFGEN_ATTR_OSP_MODE attribute.

NIFGEN_ATTR_OSP_FREQUENCY_SHIFT

Note

Related Topics

*Frequency Shift* component

Parent topic:

NI 5451 Basic Onboard Signal Processing Properties

Related concepts:

- NI 5451 Frequency Shift

<!--NI_TOPIC bundle=ni-fgen path=ni-5451-frequency-shift.html language=enus -->
## TOPIC 00755: NI 5451 Frequency Shift

- bundle_id: `ni-fgen`
- source_path: `ni-5451-frequency-shift.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5451-frequency-shift.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can perform a complex frequency shift on the I/Q data coming from the OSP. This capability is typically used when the NI 5451 is used in conjunction with an external I/Q modulator. Applying a frequency shift modifies the generated I/Q data such that the resulting RF output of the I/Q modulator i

### NI 5451 Frequency Shift

You can perform a complex frequency shift on the I/Q data coming from the OSP. This capability is typically used when the NI 5451 is used in conjunction with an external I/Q modulator. Applying a frequency shift modifies the generated I/Q data such that the resulting RF output of the I/Q modulator is shifted in frequency. This modification is a complex multiply of the I/Q data with a complex exponential (output of the NCO).

The amount of frequency shift is controlled by setting the Frequency Shift property or the 
NIFGEN_ATTR_OSP_FREQUENCY_SHIFT attribute and can be updated during generation. Frequency shift can be applied only when the 
OSP
Enabled property or the NIFGEN_ATTR_OSP_ENABLED attribute is set to True and the OSP
Mode property is set to BaseBand or the NIFGEN_ATTR_OSP_MODE attribute is set to NIFGEN_VAL_OSP_BASEBAND. Typically, frequency shift is used only when the Data
Processing Mode property is set to Complex or the NIFGEN_ATTR_OSP_DATA_PROCESSING_MODE attribute is set to NIFGEN_VAL_OSP_COMPLEX. When the data processing mode is set to Real or NIFGEN_VAL_OSP_REAL, double sideband amplitude modulation (AM) occurs at the output of the NI 5451, centered at the frequency shift value.

[IMAGE alt='image' src='GUID-EEDE90E8-98DE-4CFE-84F9-84244A753117-a5.gif']

Parent topic:

NI 5451 Numerically Controlled Oscillator (NCO)

<!--NI_TOPIC bundle=ni-fgen path=ni-5451-front-panel.html language=enus -->
## TOPIC 00756: NI 5451 Front Panel

- bundle_id: `ni-fgen`
- source_path: `ni-5451-front-panel.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5451-front-panel.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the NI PXIe-5451 front panel. This front panel has two SMB connectors and six SMA connectors. The CLK IN SMA connector accepts an external clock that can be used as a Reference clock, a Sample clock, or a Sample clock timebase. The CLK OUT SMA connector provides a clock si

### NI 5451 Front Panel

The following figure shows the NI PXIe-5451 front panel. This front panel has
two SMB connectors and six SMA connectors.

[IMAGE alt='image' src='GUID-5641B352-50D3-4F3E-ACC7-9335E8B21E20-a5.gif']

The 
*CLK IN* SMA connector accepts an external clock that can be used as a Reference clock, a Sample clock, or a Sample clock timebase.

The 
*CLK OUT* SMA connector provides a clock signal that can be shared by other devices.

The 
*PFI 0 and PFI 1* SMB
connectors are bidirectional connections that can accept a trigger from an external source and can start or step through waveform generation or route signals from several clock, event, and trigger sources.

The 
*CH 0+/I+* SMA connector provides differential and single-ended waveform output for channel 0.

The 
*CH 0−/I−* SMA connector provides complementary differential waveform output for channel 0.

The 
*CH 1+/Q+* SMA connector provides differential and single-ended waveform output for channel 1.

The 
*CH 1−/Q−* SMA connector provides complementary differential waveform output for channel 1.

Parent topic:

NI 5451 NI 5451 Overview

Related concepts:

- NI 5451 CLK IN Connector
- NI 5451 CLK OUT Connector
- NI 5451 PFI Connectors
- NI 5451 Differential and Single-Ended Channel Connectors

<!--NI_TOPIC bundle=ni-fgen path=ni-5451-hardware-state-diagram.html language=enus -->
## TOPIC 00757: NI 5451 Hardware State Diagram

- bundle_id: `ni-fgen`
- source_path: `ni-5451-hardware-state-diagram.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5451-hardware-state-diagram.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following diagram shows the hardware states of the signal generator. The signal generator can be in one of the following six basic states during the course of operation. Idle—The device is not generating a waveform. All session properties or attributes can be programmed in the Idle state. In the

### NI 5451 Hardware State Diagram

The following diagram shows the hardware states of
the signal generator.

[IMAGE alt='image' src='GUID-AE1082E0-4FAC-4A9B-9983-B34BD71D9568-a5.gif']

The signal generator can be in one of the following six basic
states during the course of operation.

Idle—The device is not generating a
waveform. All session properties or attributes can be programmed in the Idle
state. In the Idle state, the properties or attributes have not necessarily been
applied to hardware, so the hardware configuration of the device
may not match the session property or attribute values. The device remains
configured as it was the last time a session was committed. Refer
to 
*NI-FGEN Programming State
Model* for information about when attributes are applied to the
device. If the computer has just been powered on, reset, or the 
niFgen Reset
Device VI or the 
niFgen_ResetDevice function has just been called, the device is in the default
hardware state.

Wait for Trigger—After initiating
generation, the device shifts to the Wait for Trigger state. If the
trigger source is immediate, the device immediately shifts from
this state and generates a Started event. If the trigger sources
are configured for a software trigger or for a hardware trigger
from one of the available sources, the device remains in this state
until the configured trigger occurs. When the device recognizes a
trigger condition, the device immediately shifts out of this state
and generates a Started event.

First Data Appears—This state is temporary
and indicates that waveform data is just starting to appear at the front panel connector.

Generation—In the Generation state, the
device is generating a waveform as specified by the session
attributes configured. Dynamic (or on-the-fly) properties and
attributes, such as the 
Amplitude, 
Arbitrary
Waveform Gain, and 
Arbitrary
Waveform Offset properties, or the 
NIFGEN_ATTR_FUNC_AMPLITUDE, 
NIFGEN_ATTR_ARB_GAIN, and the 
NIFGEN_ATTR_ARB_OFFSET attributes, are applied immediately to hardware. Started Event
trigger is generated as the device recognizes triggers. Depending
on the configured trigger mode, the device may stay in the
Generation state until the generation is aborted.

Dynamic properties and attributes, such as
amplitude, gain, and offset, can be applied to the device
immediately if you set them while the session is in the Generation
state. Refer to the 
*NI-FGEN LabVIEW
Reference* or the 
NI-FGEN C Function
Reference for information about the specific property or
attribute that you want to set during generation.

Done—The device has completed the waveform
generation as configured for this session. This state only occurs
at the end of a generation state configured for the Single trigger
mode. The device remains in this state until you use NI-FGEN to
abort the waveform generation and to return the device to the Idle
state.

Hardware Error—An internal hardware error
occurred, such as data underflow, the PLL became unlocked, the
device shut down due to an over-temperature condition, and so on.
The signal generator may still be generating and may be
unpredictable at this point. When the driver software checks the
status of the device, an error is returned.

Parent topic:

NI 5451 Theory of Operation

Related concepts:

- Programming State Model

<!--NI_TOPIC bundle=ni-fgen path=ni-5451-i-q-combiner.html language=enus -->
## TOPIC 00758: NI 5451 I/Q Combiner

- bundle_id: `ni-fgen`
- source_path: `ni-5451-i-q-combiner.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5451-i-q-combiner.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: When the waveform data is configured for complex data points by setting the Data Processing Mode property or the NIFGEN_ATTR_OSP_DATA_PROCESSING_MODE attribute, the I and Q data streams are combined after they are multiplied with the carriers. The I/Q combiner is implemented as I [p] − Q [p]. The co

### NI 5451 I/Q Combiner

When the waveform data is configured for complex data points by setting the 
Data
Processing Mode property or the 
NIFGEN_ATTR_OSP_DATA_PROCESSING_MODE attribute, the I and Q data
streams are combined after they are multiplied with the carriers.
The I/Q combiner is implemented as I 
<sub>p</sub> − Q 
<sub>p</sub>. The combiner block dictates that the following
conditions must be true at any given time during the generation, or
an overflow can occur:

-1 ≤ I<sub>p</sub>Cos(ωt + Φ<sub>I</sub>) − Q<sub>p</sub>Cos(ωt + Φ<sub>Q</sub>) ≤ 1 if the carrier is enabled or

-1 ≤ (I<sub>p</sub> − Q<sub>p</sub>) ≤ 1 if the carrier is disabled

p

p

Tip

quadrature
upconversion

NIFGEN_ATTR_OSP_CARRIER_PHASE_I

NIFGEN_ATTR_OSP_CARRIER_PHASE_Q

p

2

p

2

Tip

NIFGEN_ATTR_OSP_OVERFLOW_ERROR_REPORTING

Parent topic:

NI 5451 Numerically Controlled Oscillator (NCO)

Related concepts:

- NI 5451 Quadrature Upconversion

<!--NI_TOPIC bundle=ni-fgen path=ni-5451-i-q-rate-controller.html language=enus -->
## TOPIC 00759: NI 5451 I/Q Rate Controller

- bundle_id: `ni-fgen`
- source_path: `ni-5451-i-q-rate-controller.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5451-i-q-rate-controller.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The I/Q rate component pulls the data from the generation engine such that a new sample is returned once every Total_OSP_Interpolation Sample clocks. The Total_OSP_Interpolation is the amount of interpolation applied within the Filtering and Interpolation component.

### NI 5451 I/Q Rate Controller

Note

Parent topic:

NI 5451 Onboard Signal Processing Components

<!--NI_TOPIC bundle=ni-fgen path=ni-5451-interleaved-waveform-data.html language=enus -->
## TOPIC 00760: NI 5451 Interleaved Waveform Data

- bundle_id: `ni-fgen`
- source_path: `ni-5451-interleaved-waveform-data.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5451-interleaved-waveform-data.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: In order to write data to multiple channels on the same device simultaneously, the data must be interleaved. Interleaved samples prioritize samples before channels, such that the array lists the first sample from every channel in the task, then the second sample from every channel, up to the last sa

### NI 5451 Interleaved Waveform Data

In order to write data to multiple channels on the same device simultaneously, the data must be interleaved.

Note

| Channel 0—Sample 1 |
| --- |
| Channel 1—Sample 1 |
| Channel 0—Sample 2 |
| Channel 1—Sample 2 |
| ... |
| Channel 0—Sample N |
| Channel 1—Sample N |

Parent topic:

NI 5451 Multichannel Configuration

<!--NI_TOPIC bundle=ni-fgen path=ni-5451-internal-sample-clock.html language=enus -->
## TOPIC 00761: NI 5451 Internal Sample Clock

- bundle_id: `ni-fgen`
- source_path: `ni-5451-internal-sample-clock.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5451-internal-sample-clock.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5451 can derive a Sample clock from its main internal timing source—the Sample clock timebase. The signal generator provides a high-precision 400 MHz oscillator clock source for the Sample clock timebase. The NI 5451 has a high-resolution internal clock. You can change the frequency of this c

### NI 5451 Internal Sample Clock

The NI 5451 can derive a Sample
clock from its main internal timing source—the Sample clock
timebase. The signal generator provides a high-precision
400 MHz oscillator clock
source for the Sample clock timebase.

[IMAGE alt='image' src='GUID-B9DD67D6-16F7-4555-9B06-9E6AB1B3F51A-a5.gif']

The NI 5451 has a high-resolution internal clock. You can change the frequency of this clock by calling the niFgen Set Sample Rate VI or the niFgen_ConfigureSampleRate function. When you set a desired sample rate, NI-FGEN will internally determine and apply appropriate divide-down factors.

Parent topic:

NI 5451 Clocking Options

<!--NI_TOPIC bundle=ni-fgen path=ni-5451-iq-rate.html language=enus -->
## TOPIC 00762: NI 5451 IQ Rate

- bundle_id: `ni-fgen`
- source_path: `ni-5451-iq-rate.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5451-iq-rate.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The IQ Rate property or the NIFGEN_ATTR_OSP_IQ_RATE attribute defines the rate at which data is processed by the OSP block. If the waveform data is configured for real data points by setting the Data Processing Mode property or the NIFGEN_ATTR_OSP_DATA_PROCESSING_MODE attribute, then it is the rate

### NI 5451 IQ Rate

NIFGEN_ATTR_OSP_IQ_RATE

NIFGEN_ATTR_OSP_DATA_PROCESSING_MODE

NIFGEN_ATTR_OSP_DATA_PROCESSING_MODE

Note

NIFGEN_ATTR_OSP_ENABLED

NIFGEN_ATTR_ARB_SAMPLE_RATE

Parent topic:

NI 5451 Basic Onboard Signal Processing Properties

<!--NI_TOPIC bundle=ni-fgen path=ni-5451-memory-fragmentation.html language=enus -->
## TOPIC 00763: NI 5451 Memory Fragmentation

- bundle_id: `ni-fgen`
- source_path: `ni-5451-memory-fragmentation.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5451-memory-fragmentation.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: When storing multiple waveforms in NI 5451 memory, fragmentation can become a problem. Both waveforms and instructions are stored in NI 5451 memory in contiguous blocks. These blocks are allocated in multiples of 128 bytes, and they are written in the order that you configure them. Fragmentation occ

### NI 5451 Memory Fragmentation

When storing multiple waveforms in
NI 5451 memory, fragmentation can become a
problem. Both waveforms and instructions are stored in
NI 5451 memory in contiguous blocks. These
blocks are allocated in multiples of 128 bytes, and they are
written in the order that you configure them. Fragmentation occurs
when you delete a waveform or script from memory that was not the
last block written.

Every new NI-FGEN session begins with empty memory.
First, multiple waveforms are written to memory, nearly filling the
device memory, as shown in the following diagram.

[IMAGE alt='image' src='GUID-9AAED100-EC9C-49B4-8E78-465B1D5BF93C-a5.gif']

If you now try to write Waveform 5 (shown
in the following figure) to the device, you find there is not
enough memory. To make room for the waveform, you could delete
Waveform 3 to create enough space in memory for Waveform 5.

[IMAGE alt='image' src='GUID-75E79D4C-9716-40F4-A437-8D27E68C6D5E-a5.gif']

You now have enough free
memory space for Waveform 5, but this space is fragmented, so you must
also clear and re-download all waveforms and generation
instructions following the deleted waveform. The following figure
illustrates the result.

[IMAGE alt='image' src='GUID-C20A61F2-E015-4DE5-95FC-A5D7323F6518-a5.gif']

Parent topic:

NI 5451 Onboard Memory

<!--NI_TOPIC bundle=ni-fgen path=ni-5451-multichannel-configuration.html language=enus -->
## TOPIC 00764: NI 5451 Multichannel Configuration

- bundle_id: `ni-fgen`
- source_path: `ni-5451-multichannel-configuration.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5451-multichannel-configuration.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5451 has two channels. By default, both are active. You can configure one or both channels as active by calling the niFgen Configure Channels VI or the niFgen_ConfigureChannels function immediately after calling the niFgen Initialize VI or the niFgen_init function. The niFgen Configure Channe

### NI 5451 Multichannel Configuration

The NI 5451 has two channels. By default, both are active. You can configure one or both channels as active by calling the niFgen Configure Channels VI or the niFgen_ConfigureChannels function immediately after calling the niFgen Initialize VI or the niFgen_init function. The niFgen Configure Channels VI or the niFgen_ConfigureChannels function cannot be called after the session has been committed. If a channel is inactive, it will maintain its output voltage and state until it is made active again or until the device is reset.

The NI 5451 has two memory banks, one for each channel. When the niFgen Configure Channels VI or the niFgen_ConfigureChannels function is called to configure only one channel as active, both channel memory banks will be configured. This allows you to use the entire onboard memory for one channel of generation.

#### Configuring Channels for OSP

The NI 5451 supports one channel of real or complex baseband or IF OSP generation. When the OSP is enabled, only one channel may be configured as active. Individual OSP properties can be configured using the I and Q channel strings ("I" and "Q", respectively).

Parent topic:

NI 5451 Theory of Operation

<!--NI_TOPIC bundle=ni-fgen path=ni-5451-multichannel-waveform-allocation.html language=enus -->
## TOPIC 00765: NI 5451 Multichannel Waveform Allocation

- bundle_id: `ni-fgen`
- source_path: `ni-5451-multichannel-waveform-allocation.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5451-multichannel-waveform-allocation.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: A waveform consists of all of the data to be generated on all active channels of a device. A waveform is allocated on a per–device basis, and when waveform allocation occurs, space is allocated on the device onboard memory for each channel. Waveform data must therefore be the same size for each chan

### NI 5451 Multichannel Waveform Allocation

A waveform consists of all of the data to be generated on all active channels of a device. A waveform is allocated on a per–device basis, and when waveform allocation occurs, space is allocated on the device onboard memory for each channel. Waveform data must therefore be the same size for each channel.

Because waveforms contain data for all channels, you can only generate one script, sequence, or arbitrary waveform at a time for all active channels of the device; you cannot generate separate scripts, sequences, or arbitrary waveforms on different channels at the same time.

#### Writing Data

On the NI 5451, data can be written to channel 0 and 1 independently, to I and Q independently, or to both channels simultaneously.

Tip

I/Q generation

To write waveform data to an individual channel, begin by allocating space for waveform data by calling the niFgen Allocate Waveform or niFgen Allocate Named Waveform VI or the niFgen_AllocateWaveform or niFgen_AllocateNamedWaveform function. Once you have allocated the waveform data, call the appropriate niFgen Write Waveform (poly) VI or one of the niFgen Write Waveform functions with the Channel Name parameter set to "0" or "1" and the Waveform Name or waveformHandle parameter set to the name of the waveform previously allocated. You can repeat these steps to write waveform data to another channel.

To write waveform data to both channels at once, you must first *interleave* the data. Once the data is interleaved, call the niFgen Write Waveform (poly) VI or one of the niFgen Write Waveform functions with the Channel parameter set to "0,1".

Parent topic:

NI 5451 Multichannel Configuration

Related concepts:

- NI 5451 Writing I/Q Data
- NI 5451 Interleaved Waveform Data

<!--NI_TOPIC bundle=ni-fgen path=ni-5451-ni-5451-overview.html language=enus -->
## TOPIC 00766: NI 5451 NI 5451 Overview

- bundle_id: `ni-fgen`
- source_path: `ni-5451-ni-5451-overview.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5451-ni-5451-overview.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5451 is a 400 MS/s, 16-bit dual-channel arbitrary waveform generator for the PXI Express platform with the following features: 16-bit resolution output, two channels, differential and single-ended output Differential output amplitude with a maximum of 5 V[pk-pk] into a 100 Ω differential load

### NI 5451 NI 5451 Overview

The NI 5451 is a 400 MS/s, 16-bit dual-channel arbitrary waveform generator for the PXI Express platform with the following
features:

- 16-bit resolution output, two channels, differential and single-ended output
- Differential output amplitude with a maximum of 5 V pk-pk into a 100 Ω differential load
- Single-ended output amplitude with a maximum of 2.5 V pk-pk into a 50 Ω load
- Onboard signal processing (OSP)
with 135 MHz of baseband I/Q bandwidth, flatness correction, interpolation, pulse-shaping, and 160 MHz of digital upconverter bandwidth
- 50 Ω output impedance (100 Ω differential output impedance), and output attenuation levels from 0 to 63 dB
- High-resolution, low phase noise internal clocking
- External clocking options
- PLL synchronization to external clocks or to PXI clock
- TClk synchronization
- Sample rate up to 400 MS/s
- Up to 2 GB of onboard waveform memory
- Waveform linking and looping for arbitrary waveform generation
- Digital gain, Analog gain and offset
- 2 bidirectional PFI lines for importing triggers and exporting events
- PXI trigger lines
- Selectable reconstruction filter on the main path for time or frequency domain performance

All NI 5451 devices follow industry-standard
Plug and Play specifications for the PXI Express bus and offer
seamless integration with compliant systems.

Parent topic:

Devices

Related concepts:

- NI 5451 Onboard Signal Processing (OSP)

<!--NI_TOPIC bundle=ni-fgen path=ni-5451-numerically-controlled-oscillator-nco.html language=enus -->
## TOPIC 00767: NI 5451 Numerically Controlled Oscillator (NCO)

- bundle_id: `ni-fgen`
- source_path: `ni-5451-numerically-controlled-oscillator-nco.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5451-numerically-controlled-oscillator-nco.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The numerically controlled oscillator (NCO) is a digital circuit that creates two cosine waves of the same frequency with two potentially independent phases. Depending on the configuration of the OSP, the NCO can be used for Baseband Frequency Shift, or for multiplying by a Carrier Frequency. These

### NI 5451 Numerically Controlled Oscillator (NCO)

The numerically controlled oscillator (NCO) is a
digital circuit that creates two cosine waves of the same frequency
with two potentially independent phases. 
Depending on the configuration of the OSP, the NCO can be used for *Baseband Frequency Shift*, or for multiplying by a *Carrier Frequency*. These different functions of the NCO require different attributes when configuring the NCO-based hardware.

Parent topic:

NI 5451 Onboard Signal Processing Components

Related concepts:

- NI 5451 Frequency Shift
- NI 5451 Carrier Frequency

<!--NI_TOPIC bundle=ni-fgen path=ni-5451-offset.html language=enus -->
## TOPIC 00768: NI 5451 Offset

- bundle_id: `ni-fgen`
- source_path: `ni-5451-offset.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5451-offset.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure illustrates the relationship between the differential offset voltage and the common-mode offset voltage, along with a generated peak-to-peak AC signal for single-ended and differential configurations. The peak-to-peak differential receiver voltage rejects the common-mode offset

### NI 5451 Offset

The following figure illustrates the relationship between the differential offset voltage and the common-mode offset voltage, along with a generated peak-to-peak AC signal for single-ended and differential configurations. The peak-to-peak differential receiver voltage rejects the common-mode offset voltage and other common-mode noise present in the signal.

[IMAGE alt='image' src='GUID-718AD73F-80E3-4A03-9168-FAE6F093FC19-a5.gif']

V<sub>PPD</sub> = V<sub>PPSE+</sub> + V<sub>PPSE</sub>

where

V<sub>PPD</sub>
 represents the differential voltage peak to peak

V<sub>PPSE</sub>
 represents the single-ended voltage peak to peak

V<sub>DO</sub>
 represents the differential offset voltage

CMO

Note

The software model used with the NI 5451 assumes that when the Terminal Configuration property is set to Differential or the NIFGEN_ATTR_TERMINAL_CONFIGURATION attribute is set to NIFGEN_VAL_DIFFERENTIAL, the load impedance is comprised of separate matched loads to ground on each terminal. The software scales the gain and offset by the voltage divider created by the source and set load impedance to match the user-specified voltage to the generated output voltage as shown below.

[IMAGE alt='image' src='GUID-8774E529-7384-44DD-9A7F-8308554135B8-a5.gif']

Note

Common-Mode Offset and Differential Loads

Parent topic:

NI 5451 Analog Output

Related concepts:

- NI 5451 Common-Mode Offset and Differential Loads

<!--NI_TOPIC bundle=ni-fgen path=ni-5451-onboard-memory.html language=enus -->
## TOPIC 00769: NI 5451 Onboard Memory

- bundle_id: `ni-fgen`
- source_path: `ni-5451-onboard-memory.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5451-onboard-memory.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5451 signal generator uses an onboard memory that is 16-bits wide. The minimum standard memory size for the NI 5451 is 128 MB. With the minimum standard memory size, you can store very long waveforms on the device and obtain reliable waveform generation at full sample rate of 400 MS/s. The NI

### NI 5451 Onboard Memory

The NI 5451 signal generator
uses an onboard memory that is 16-bits wide. The minimum standard
memory size for the NI 5451 is 128 MB. With the minimum
standard memory size, you can store very long waveforms on the
device and obtain reliable waveform generation at full sample rate
of 400 MS/s. The
NI 5451 is also available with higher memory options of 512 MB or 2 GB.

The onboard memory is a single large memory area per channel that stores both waveforms and sequence instructions to generate
the waveforms. The instructions for a complicated sequence can
occupy a significant portion of memory. The architecture of the
NI 5451 allows you to load multiple
waveforms and multiple sequence instructions into the memory. The
following diagram illustrates NI 5451
memory allocation. A number of waveforms are stored in the onboard
memory ranging from 1 to 
n; there are also a number of sequence instructions
ranging in number from 1 to 
m. The values of 
n and 
m depend on the waveform and instructions configured and
are ultimately limited by the amount of memory.

[IMAGE alt='image' src='GUID-84BB06FA-B7C3-44C6-B2D1-0CB400485AB6-a5.gif']

The following tables list the types of information
that are used to make up the instructions that are saved to memory.
You can store the instructions for multiple sequences to the
onboard memory ahead of time and generate them later, allowing for
quick reconfiguration times between tests. There are two example
sequences. The first table, Sequence 1, represents the instructions
for a sequence containing a maximum number of segments 
k. The second table, Sequence m, is an example of a
sequence containing 8 segments. Each sequence uses different
waveforms that are downloaded to the onboard memory, as well as
various looping and Marker placement options to construct each
resulting waveform.

| Sequence 1: Burst Trigger Mode |  |  |  |
| --- | --- | --- | --- |
| Sequence Segment | Waveform | Number of Loops | Marker Placement |
| 1 | 1 | 1 | 0 |
| 2 | 5 | 14 | 100 |
| 3 | 17 | 1 | -1 |
| 4 | 12 | 18,045 | 10,000 |
| 5 | 12 | 64,000 | 12 |
| 6 | 34 | 64,000 | 0 |
| ......... |  |  |  |
| k | 15 | 20 | 10,000 |

| Sequence m: Stepped Trigger Mode |  |  |  |
| --- | --- | --- | --- |
| Sequence Segment | Waveform | Number of Loops | Marker Placement |
| 1 | 1 | 1 | 0 |
| 2 | 2 | 340 | 4 |
| 3 | 35 | 1 | -1 |
| 4 | 2 | 10 | 0 |
| 5 | 340 | 5 | 10,000 |
| 6 | 34 | 64,000 | 0 |
| 7 | 20,000 | 1,000,000 | 13 |
| 8 | 1 | 1 | 0 |

#### Onboard Memory for Multichannel Waveform Generation

On multichannel devices, onboard memory is allocated separately for each configured channel. When you write a waveform to the onboard memory of a multichannel device, the space required for the waveform is allocated in the onboard memory for each channel.

You can write different data to the waveform allocated for each channel, as long as the data written requires the same amount of memory on each channel. For example, Waveform 1 can contain a ramp wave on channel 0 and a square wave on channel 1, as shown in the following figure.

[IMAGE alt='image' src='GUID-89789D56-953C-4ADC-956B-F48CF4B67FDF-a5.gif']

Parent topic:

NI 5451 Theory of Operation

<!--NI_TOPIC bundle=ni-fgen path=ni-5451-onboard-signal-processing-components.html language=enus -->
## TOPIC 00770: NI 5451 Onboard Signal Processing Components

- bundle_id: `ni-fgen`
- source_path: `ni-5451-onboard-signal-processing-components.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5451-onboard-signal-processing-components.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the block diagram of the OSP block. The OSP block includes the following components: I/Q Rate Controller Prefilter Gain and Offset Filtering and Interpolation FIR Filter Types Numerically Controlled Oscillator (NCO) I/Q Combiner

### NI 5451 Onboard Signal Processing Components

The following figure shows the block diagram of the
OSP block.

[IMAGE alt='image' src='GUID-5E0FFD2E-0DA4-4DAC-BC72-6C340350B964-a5.gif']

The OSP block includes the following
components:

- I/Q Rate Controller
- Prefilter Gain and Offset
- Filtering and Interpolation
- FIR Filter Types
- Numerically Controlled Oscillator (NCO)
- I/Q Combiner

Parent topic:

NI 5451 Onboard Signal Processing (OSP)

Related concepts:

- NI 5451 I/Q Rate Controller
- NI 5451 Prefilter Gain and Offset
- NI 5451 Filtering and Interpolation
- NI 5451 FIR Filter Types
- NI 5451 Numerically Controlled Oscillator (NCO)
- NI 5451 I/Q Combiner

<!--NI_TOPIC bundle=ni-fgen path=ni-5451-onboard-signal-processing-osp.html language=enus -->
## TOPIC 00771: NI 5451 Onboard Signal Processing (OSP)

- bundle_id: `ni-fgen`
- source_path: `ni-5451-onboard-signal-processing-osp.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5451-onboard-signal-processing-osp.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The onboard signal processing (OSP) block is a general-purpose block of digital signal processing components that can be used to modify the data pulled from waveform memory during generation. The OSP block can be used for the following common applications: Baseband I/Q Interpolation Quadrature Upcon

### NI 5451 Onboard Signal Processing (OSP)

The onboard signal processing (OSP) block is a
general-purpose block of digital signal processing components that
can be used to modify the data pulled from waveform memory during
generation.

The OSP block can be used for the following common applications:

- Baseband I/Q
Interpolation
- Quadrature
Upconversion
- Amplitude Modulation (AM) or Double Sideband
- Tone Generation

The OSP block includes the following
components:

- I/Q Rate Controller
- Prefilter Gain and Offset
- Filtering and Interpolation
- FIR Filter Types
- Numerically Controlled Oscillator (NCO)
- Frequency Shift
- Carrier Frequency
- I/Q Combiner

The following properties configure the OSP block:

- OSP Mode
- OSP Enabled
- Data Processing
Mode
- IQ Rate
- Carrier
Frequency
- Frequency Shift
- FIR Filter Type

Parent topic:

NI 5451 Theory of Operation

Related concepts:

- NI 5451 Baseband I/Q Interpolation
- NI 5451 Quadrature Upconversion
- NI 5451 Amplitude Modulation (AM) or Double Sideband
- NI 5451 Tone
- NI 5451 I/Q Rate Controller
- NI 5451 Prefilter Gain and Offset
- NI 5451 Filtering and Interpolation
- NI 5451 FIR Filter Types
- NI 5451 Numerically Controlled Oscillator (NCO)
- NI 5451 Frequency Shift
- NI 5451 Carrier Frequency
- NI 5451 I/Q Combiner
- NI 5451 OSP Mode
- NI 5451 OSP Enabled
- NI 5451 Data Processing Mode
- NI 5451 IQ Rate
- NI 5451 Carrier Frequency Property
- NI 5451 Frequency Shift Property
- NI 5451 FIR Filter Type

<!--NI_TOPIC bundle=ni-fgen path=ni-5451-osp-enabled.html language=enus -->
## TOPIC 00772: NI 5451 OSP Enabled

- bundle_id: `ni-fgen`
- source_path: `ni-5451-osp-enabled.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5451-osp-enabled.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The OSP Enabled property or the NIFGEN_ATTR_OSP_ENABLED attribute activates the functionality of the OSP block. To use any of the features in the OSP block, you must enable onboard signal processing by setting this property or attribute.

### NI 5451 OSP Enabled

The 
OSP
Enabled property or the 
NIFGEN_ATTR_OSP_ENABLED attribute activates the functionality of the OSP block. To use
any of the features in the OSP block, you must enable onboard
signal processing by setting this property or attribute.

Parent topic:

NI 5451 Basic Onboard Signal Processing Properties

<!--NI_TOPIC bundle=ni-fgen path=ni-5451-osp-mode.html language=enus -->
## TOPIC 00773: NI 5451 OSP Mode

- bundle_id: `ni-fgen`
- source_path: `ni-5451-osp-mode.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5451-osp-mode.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The OSP Mode property or the NIFGEN_ATTR_OSP_MODE attribute specifies the generation mode implemented by the OSP block. The OSP block can operate in IF or Baseband mode. On the NI 5451, the default OSP mode is Baseband generation. The NI 5451 can generate single-ended or differential output dependin

### NI 5451 OSP Mode

The 
OSP
Mode property or the 
NIFGEN_ATTR_OSP_MODE attribute specifies the generation mode implemented by the OSP block. The OSP block can operate in IF or Baseband mode. 
 On the NI 5451, the default OSP mode is Baseband generation. The NI 5451 can generate single-ended or differential output depending on the analog configuration.

In either mode, I/Q data is filtered, interpolated, and scaled in the device OSP.

In baseband mode, the device generates I data on the CH 0 output terminals and Q data on the CH 1 output terminals.

In IF mode, the device generates IF data on the CH 0 output terminals.

Parent topic:

NI 5451 Basic Onboard Signal Processing Properties

<!--NI_TOPIC bundle=ni-fgen path=ni-5451-output-enable.html language=enus -->
## TOPIC 00774: NI 5451 Output Enable

- bundle_id: `ni-fgen`
- source_path: `ni-5451-output-enable.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5451-output-enable.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can disable the analog output signal at the differential channel connectors by controlling the output enable relay, as shown in the following figure. When the output enable relay is disabled, the output signal is connected to ground through a 50 Ω resistance. The output enable relay is enabled f

### NI 5451 Output Enable

You can disable the analog output signal at the differential channel connectors by controlling the output enable relay, as shown in the
following figure.

[IMAGE alt='image' src='GUID-29DAC0CB-64DB-44B3-B7EC-C8B3A2A44BF6-a5.gif']

When the output enable relay is disabled, the
output signal is connected to ground through a 50 Ω resistance. The output enable relay is enabled for normal waveform
generation and connects the differential channel SMA connectors to the 
*Analog Output path*. You
can change the output enable state at any time during waveform
generation, and generation continues internally.

niFgen_ConfigureOutputEnabled

Note

Parent topic:

NI 5451 Analog Output

Related concepts:

- NI 5451 Analog Output

<!--NI_TOPIC bundle=ni-fgen path=ni-5451-output-modes.html language=enus -->
## TOPIC 00775: NI 5451 Output Modes

- bundle_id: `ni-fgen`
- source_path: `ni-5451-output-modes.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5451-output-modes.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The output mode of your signal generator determines the type of waveforms your signal generator produces. To select an output mode, set the Output Mode parameter of the niFgen Configure Output Mode VI or the niFgen_ConfigureOutputMode function.

### NI 5451 Output Modes

The output mode of your signal generator determines the type of
waveforms your signal generator produces. To select an output mode,
set the 
Output Mode parameter of the 
niFgen
Configure Output Mode VI or the 
niFgen_ConfigureOutputMode function.

Parent topic:

NI 5451 Waveform Generation

<!--NI_TOPIC bundle=ni-fgen path=ni-5451-pfi-connectors.html language=enus -->
## TOPIC 00776: NI 5451 PFI Connectors

- bundle_id: `ni-fgen`
- source_path: `ni-5451-pfi-connectors.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5451-pfi-connectors.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: PFI 0 and PFI 1 are bidirectional connectors. As an input, the PFI terminals can accept a trigger from an external source that can start or step through waveform generation. As an output, the PFI lines route a signal out from the following sources: Marker events Start trigger PLL Reference clock sou

### NI 5451 PFI Connectors

PFI 0 and PFI 1 are bidirectional connectors. As an
input, the PFI terminals can accept a trigger from an external
source that can start or step through waveform generation.

As an output, the PFI lines route a signal out
from the following sources:

- Marker events
- Start trigger
- PLL Reference clock source
- Sample Clock Out (with /
 K where K is an integer used to divide the Sample
clock)
- Started, Done, and Ready for Start events
- Sample clock timebase (with /
 M where M is an integer used to divide the Sample clock
timebase frequency)

- Script trigger

Refer to the 
*device specifications* for information about acceptable input signal
characteristics for the PFI lines and output signal
characteristics.

Parent topic:

NI 5451 Front Panel

<!--NI_TOPIC bundle=ni-fgen path=ni-5451-power-up-and-reset-conditions.html language=enus -->
## TOPIC 00777: NI 5451 Power-Up and Reset Conditions

- bundle_id: `ni-fgen`
- source_path: `ni-5451-power-up-and-reset-conditions.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5451-power-up-and-reset-conditions.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The signal generator is in the following state from the time at which the computer begins to power up until the operating system is fully booted and NI-FGEN is loaded. The CH 0+/− and CH 1+/− differential output connectors are disabled and each has 50 Ω impedance to ground. This impedance is the sam

### NI 5451 Power-Up and Reset Conditions

The signal generator is in the following state from
the time at which the computer begins to power up until the operating system is
fully booted and NI-FGEN is loaded.

- The CH 0+/− and CH 1+/− differential output connectors are disabled and each has
50 Ω impedance to ground. This
impedance is the same as its previous setting before the device was
powered down. The output voltage amplitude of this connector
is 0 V.
- The CLK IN connector has high-impedance to
ground.
- PFI 0 and PFI 1 are tristated and have a 10 kΩ impedance to ground.
- The CLK OUT connector is tristated and has a high-impedance to ground.

- PXI trigger lines are tristated and floating.

After the operating system is fully booted and
NI-FGEN is loaded, or when you perform a hard reset to the device
directly from MAX or using NI-FGEN, the signal generator is in the
following state:

- Single-ended main path
- CH 0+/− and CH 1+/− output is enabled.
- CH 0+/− and CH 1+/− output attenuation is set to 0 dB.
- CLK OUT output impedance is set to high-impedance.
- CLK IN is disabled and has a high-impedance to ground.
- PFI 0 and PFI 1 are tristated and have a 10 kΩ impedance to ground.

- PXI trigger lines are tristated and floating.
- The sample rate is set to the maximum rate, with the Sample
clock source set to the internal Sample clock timebase.
- The Sample clock timebase is tuned by the internal reference
control voltage.

Parent topic:

NI 5451 NI 5451 Overview

<!--NI_TOPIC bundle=ni-fgen path=ni-5451-prefilter-gain-and-offset.html language=enus -->
## TOPIC 00778: NI 5451 Prefilter Gain and Offset

- bundle_id: `ni-fgen`
- source_path: `ni-5451-prefilter-gain-and-offset.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5451-prefilter-gain-and-offset.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use the following prefiltering components to add impairments to your data and/or to eliminate overflows that occur later in the OSP block. Related Topics Prefilter Gain Prefilter Offset

### NI 5451 Prefilter Gain and Offset

You can use the following prefiltering components
to add impairments to your data and/or to eliminate overflows that
occur later in the 
*OSP* block.

#### Related Topics

- Prefilter Gain
- Prefilter
Offset

Parent topic:

NI 5451 Onboard Signal Processing Components

Related concepts:

- NI 5451 Onboard Signal Processing (OSP)
- NI 5451 Prefilter Gain
- NI 5451 Prefilter Offset

<!--NI_TOPIC bundle=ni-fgen path=ni-5451-prefilter-gain.html language=enus -->
## TOPIC 00779: NI 5451 Prefilter Gain

- bundle_id: `ni-fgen`
- source_path: `ni-5451-prefilter-gain.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5451-prefilter-gain.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Prefilter gain can change the gain of the I and Q stream during signal generation. You can change the I and Q prefilter gains independently by setting the Pre-Filter Gain I and Pre-Filter Gain Q properties or the NIFGEN_ATTR_OSP_PRE_FILTER_GAIN_I and NIFGEN_ATTR_OSP_PRE_FILTER_GAIN_Q attributes. The

### NI 5451 Prefilter Gain

Prefilter gain can change the gain of the I and Q
stream during signal generation. You can change the I and Q
prefilter gains independently by setting the 
Pre-Filter
Gain I and 
Pre-Filter
Gain Q properties or the 
NIFGEN_ATTR_OSP_PRE_FILTER_GAIN_I and 
NIFGEN_ATTR_OSP_PRE_FILTER_GAIN_Q attributes. The gain can range from 
-16.0 to +16.0 (unitless). Any
time the prefilter gain changes, the OSP block ignores all
overflows for the next 
 several I/Q samples. If an overflow occurs during
these 
 
 samples, the data is clipped and no error is returned. The prefilter gain can be
used to attenuate the I/Q data to eliminate overflows in later
stages of the OSP block.

#### Prefilter Gain Overflow

Any time the following condition is not true for
the I or Q data stream, an overflow occurs when prefilter gain is
applied:

-1 ≤ User Data × Prefilter Gain ≤ 1

If an overflow occurs, the data is clipped and
NI-FGEN returns an error. To prevent data clipping, attenuate the
waveform data or reduce the prefilter gain.

Tip

NIFGEN_ATTR_OSP_OVERFLOW_ERROR_REPORTING

Parent topic:

NI 5451 Prefilter Gain and Offset

<!--NI_TOPIC bundle=ni-fgen path=ni-5451-prefilter-offset.html language=enus -->
## TOPIC 00780: NI 5451 Prefilter Offset

- bundle_id: `ni-fgen`
- source_path: `ni-5451-prefilter-offset.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5451-prefilter-offset.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Prefilter offset can add offset to the I and Q stream during signal generation. Change the I and Q prefilter offsets independently by setting the Pre-Filter Offset I and Pre-Filter Offset Q properties or the NIFGEN_ATTR_OSP_PRE_FILTER_OFFSET_I and NIFGEN_ATTR_OSP_PRE_FILTER_OFFSET_Q attributes. The

### NI 5451 Prefilter Offset

Prefilter offset can add offset to the I and Q
stream during signal generation. Change the I and Q
prefilter offsets independently by setting the 
Pre-Filter
Offset I and 
Pre-Filter
Offset Q properties or the 
NIFGEN_ATTR_OSP_PRE_FILTER_OFFSET_I and 
NIFGEN_ATTR_OSP_PRE_FILTER_OFFSET_Q attributes. The offset can range from negative full scale
(−1) to positive full scale (+1). Any time the prefilter
offset changes, the OSP block ignores all overflows for the next several
I/Q samples. If an overflow occurs during these samples, the data
is clipped and no error is returned.

#### Prefilter Offset Overflow

Any time the following condition is not true for
the I or Q data stream, an overflow occurs when prefilter offset is
applied:

-1 ≤ (User Data × Pre-Filter Gain) +
Pre-Filter Offset ≤ 1

If an overflow occurs, the data is clipped and
NI-FGEN returns an error. To prevent data clipping, reduce the 
*prefilter gain*,
attenuate the waveform data, or reduce the prefilter offset.

Tip

NIFGEN_ATTR_OSP_OVERFLOW_ERROR_REPORTING

Parent topic:

NI 5451 Prefilter Gain and Offset

Related concepts:

- NI 5451 Prefilter Gain

<!--NI_TOPIC bundle=ni-fgen path=ni-5451-pxi-express-bandwidth-considerations.html language=enus -->
## TOPIC 00781: NI 5451 PXI Express Bandwidth Considerations

- bundle_id: `ni-fgen`
- source_path: `ni-5451-pxi-express-bandwidth-considerations.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5451-pxi-express-bandwidth-considerations.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: National Instruments PXI Express signal generators use PCI Express as the interface to the computer. The physical connection between a PXI Express signal generator and a computer is called a PCI Express link. When a signal generator generates a waveform, it can saturate this link. Saturation occurs

### NI 5451 PXI Express Bandwidth Considerations

National Instruments PXI Express signal generators use PCI Express as the interface to the computer. The physical connection between a PXI Express signal generator and a computer is called a PCI Express link. When a signal generator generates a waveform, it can saturate this link. Saturation occurs when the signal generator is copying data to its onboard memory from computer memory as rapidly as possible, utilizing all of the bandwidth of the PCI Express link.

The theoretical bandwidth of the onboard memory of the signal generator is 3.2 GB/s, and the theoretical bandwidth of the PCIe link is approximately 850 MB/s. This difference in bandwidths means that transferring data to the onboard memory can saturate the PCI Express link. The waveform data download rate is dependent on the system configuration, with a maximum of approximately 600 MB/s.

High-speed transfers that saturate the PCI Express link can affect other devices when multiple devices share a single PCI Express link. For example, if an NI PXI Express signal generator is installed in slot 9 of an NI PXIe-1065 chassis controlled by an NI PXIe-8130 controller, the signal generator will share bandwidth with any devices installed in Slots 10 through 14. This bandwidth sharing becomes a problem if other devices in the application require guaranteed bandwidth to the PCI Express bus.

You can configure the NI PXI Express signal generator to limit its use of the PCI Express bus, leaving bandwidth for other devices that are more susceptible to short-term bursts of traffic on a shared PCI Express link. You may also be able improve the performance of your device based on your system configuration. The following table lists the properties and attributes that allow you to modify the way that the signal generator uses the PXI Express bus.

| LabVIEW Property | C/C++ Attribute | Purpose |
| --- | --- | --- |
| Maximum Bandwidth | NIFGEN_ATTR_DATA_TRANSFER_MAXIMUM_BANDWIDTH | Allows you to optimize bus bandwidth usage for multi-device streaming applications. |
| Maximum In-Flight Read Requests | NIFGEN_ATTR_DATA_TRANSFER_MAXIMUM_IN_FLIGHT_READ_REQUESTS | Allows you to specify, based on the requirements of your application, the maximum number of in-flight read requests for data transfers. |
| Preferred Packet Size | NIFGEN_ATTR_DATA_TRANSFER_PREFERRED_PACKET_SIZE | Allows you to configure, based on the requirements of your system, the preferred size of the data field in the PCI Express data transfer packet. |

Parent topic:

NI 5451 Streaming

<!--NI_TOPIC bundle=ni-fgen path=ni-5451-quadrature-upconversion.html language=enus -->
## TOPIC 00782: NI 5451 Quadrature Upconversion

- bundle_id: `ni-fgen`
- source_path: `ni-5451-quadrature-upconversion.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5451-quadrature-upconversion.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the behavior of the OSP block during quadrature upconversion. In quadrature upconversion, you give the I and Q complex waveform data to the OSP block. This data is then pulse shaped, interpolated up to a high sample rate, and then upconverted to a programmable carrier freq

### NI 5451 Quadrature Upconversion

The following figure shows the behavior of the OSP
block during quadrature upconversion.

[IMAGE alt='image' src='GUID-2F0C03AD-F58F-430F-9105-F8FE560D37D2-a5.gif']

In quadrature upconversion, you give the I and Q
complex waveform data to the OSP block. This data is then pulse
shaped, interpolated up to a high sample rate, and then upconverted
to a programmable carrier frequency. For quadrature upconversion,
complete the following steps.

1. Enable onboard signal processing by setting the 
OSP
Enabled property or the 
 NIFGEN_ATTR_OSP_ENABLED attribute.
2. Specify the use of complex numbers for the waveform data by
setting the 
Data
Processing Mode property or the 
 NIFGEN_ATTR_OSP_DATA_PROCESSING_MODE attribute.
3. Set the 
IQ Rate
property or the 
 NIFGEN_ATTR_OSP_IQ_RATE attribute.
4. Set the 
FIR Filter
Type property or the 
 NIFGEN_ATTR_OSP_FIR_FILTER_TYPE attribute.
5. Set the corresponding filter parameter.
6. Enable the carrier by setting the 
Carrier
Enabled property or the 
 NIFGEN_ATTR_OSP_CARRIER_ENABLED attribute.
7. Set the 
Carrier
Frequency property or the 
 NIFGEN_ATTR_OSP_CARRIER_FREQUENCY attribute.
8. Download the complex waveform data to the signal
generator.

Note

Pre-Filter Gain

#### With Signal Impairments

Signal impairments can be dynamically added to a
quadrature upconverted signal. 
I/Q Gain Imbalance impairments can be simulated by changing
the I or Q prefilter gain. The following formula converts from 
I/Q Gain Imbalance (dB, must be negative) to prefilter
gain.

Note

Prefilter Gain = 10 
<sup>(I/Q Gain Imbalance / 20)</sup>

I/Q DC offset impairments can be simulated by
changing the I and Q prefilter offset. The following formula
converts from I/Q DC offset (%) to I/Q prefilter offset.

Prefilter Offset = (DC Offset / 100) × Prefilter
gain

You can simulate quadrature skew impairments by
changing the I or Q carrier phase. Change the I or Q carrier phase
by the required quadrature skew to simulate this impairment.

Parent topic:

NI 5451 Common Onboard Signal Processing Applications

Related concepts:

- NI 5451 Prefilter Gain

<!--NI_TOPIC bundle=ni-fgen path=ni-5451-reference-clock.html language=enus -->
## TOPIC 00783: NI 5451 Reference Clock

- bundle_id: `ni-fgen`
- source_path: `ni-5451-reference-clock.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5451-reference-clock.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the NI 5451 Reference Clock Source path. The NI 5451 can phase-lock its Sample clock to an external signal that is present on the CLK IN front panel connector. PXI devices can also phase–lock to a 10 MHz Reference clock signal provided by the PXI bus (PXI_CLK10). Refer to

### NI 5451 Reference Clock

The following figure shows the NI 5451 Reference Clock Source path.

[IMAGE alt='image' src='GUID-B8EBE8BF-FC7F-45E7-8DCB-EEE72D0F4218-a5.gif']

The NI 5451 can
phase-lock its Sample clock to an external signal
that is present on the CLK IN front panel connector. PXI devices
can also phase–lock to a 10 MHz Reference clock signal
provided by the PXI bus (PXI_CLK10).

Clocking Options

Note

device 
specifications

Related Topics
*Configuring a Reference
Clock*

Parent topic:

NI 5451 Clocking Options

Related concepts:

- NI 5451 Clocking Options
- Configuring a Reference Clock

<!--NI_TOPIC bundle=ni-fgen path=ni-5451-sample-size-and-resolution.html language=enus -->
## TOPIC 00784: NI 5451 Sample Size and Resolution

- bundle_id: `ni-fgen`
- source_path: `ni-5451-sample-size-and-resolution.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5451-sample-size-and-resolution.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5451 stores arbitrary waveforms in memory as signed 16-bit digital words. On the NI 5451, the entire 16 bits are sent to the digital gain circuit, the OSP and the DAC. Related Topics Onboard Memory Waveform Sizes

### NI 5451 Sample Size and Resolution

The NI 5451 stores arbitrary
waveforms in memory as signed 16-bit digital words. On the
NI 5451, the entire 16 bits are sent to the digital
gain circuit, the OSP and the DAC.

Related Topics

*Onboard Memory*

*Waveform Sizes*

Parent topic:

NI 5451 Waveform Generation

Related concepts:

- NI 5451 Onboard Memory
- NI 5451 Waveform Size and Quantum

<!--NI_TOPIC bundle=ni-fgen path=ni-5451-script-mode.html language=enus -->
## TOPIC 00785: NI 5451 Script Mode

- bundle_id: `ni-fgen`
- source_path: `ni-5451-script-mode.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5451-script-mode.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Script Mode allows you to use scripting to link and loop multiple waveforms in complex combinations using a script. A script is a series of instructions that indicates how waveforms saved in the onboard memory should be sent to the DUT. Scripts have many different uses, including specifying the orde

### NI 5451 Script Mode

*Script Mode* allows you to use scripting to link and
loop multiple waveforms in complex combinations using a 
script. A script is a series of instructions that
indicates how waveforms saved in the onboard memory should be sent
to the DUT. Scripts have many different uses, including specifying the order in which the waveforms
are generated, the number of times they are generated, and the
triggers and markers associated with the generation.

Parent topic:

NI 5451 Output Modes

Related concepts:

- Script Mode

<!--NI_TOPIC bundle=ni-fgen path=ni-5451-signal-routing.html language=enus -->
## TOPIC 00786: NI 5451 Signal Routing

- bundle_id: `ni-fgen`
- source_path: `ni-5451-signal-routing.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5451-signal-routing.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: An NI signal generator is capable of sending and receiving signals through the front panel and the PXI or RTSI trigger bus. The front panel connectors provides connectivity for the output channel as well as for control lines for sending and receiving clocks, triggers, and events. You can use the PXI

### NI 5451 Signal Routing

An NI signal generator is capable of sending and
receiving signals through the front panel and the PXI or RTSI
trigger bus. The front panel connectors provides connectivity for
the output channel as well as for control lines for sending and
receiving clocks, triggers, and events. You can use the PXI and
RTSI trigger bus to send and receive events, triggers, and Sample
and Reference clocks.

All signal routing operations can be characterized
by a 
source and a 
destination. To determine the possible signal routes for
your device, complete the following steps.

1. Launch MAX, either by navigating to 
 Start»All Programs»National Instruments»Measurement &
Automation or by double-clicking the 
 Measurement & Automation icon on the desktop.
2. Expand 
 Devices and Interfaces .

 Note 

 
 If you are using a remote RT
target, expand 
Remote Systems, find and expand your target, and
then expand 
Devices and Interfaces.
3. Select your device. The view to the right of the MAX
configuration tree shows the attributes of your device.
4. Click the 
 Device Routes tab below the attributes view. A
table in the 
 Device Routes view shows the possible sources and
destinations for the signal generator. Sources are listed in the
far left column, and the possible destinations span the top of the
table. Each cell in the table is an index with the valid source and
destination terminal for the device.
 If a route is possible between a source and
destination terminal, the intersecting cell is colored green or
yellow. A green cell indicates the route can be made without
consuming any important resource of your device. A yellow cell
indicates that although the route is possible, something important
must be consumed to create the route. Placing the cursor over a
yellow square reveals the resource used in the 
subsystem used indicator.
5. Use the 
niFgen Export
Signal VI or the 
 niFgen_ExportSignal 
 function to route the signals. For terminal name syntax, refer
to 
 Syntax for Terminal
Names .

Tip

niFgen_ExportSignal

Parent topic:

NI 5451 Theory of Operation

Related concepts:

- NI 5451 Syntax for Terminal Names

<!--NI_TOPIC bundle=ni-fgen path=ni-5451-single-trigger-mode.html language=enus -->
## TOPIC 00787: NI 5451 Single Trigger Mode

- bundle_id: `ni-fgen`
- source_path: `ni-5451-single-trigger-mode.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5451-single-trigger-mode.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: When your application is configured for Single trigger mode, only one Start trigger is required to begin waveform generation. All Start triggers after the first Start trigger are ignored. Once the waveform generation is complete, the analog output indefinitely settles at the DC value of the last sam

### NI 5451 Single Trigger Mode

When your application is configured for Single
trigger mode, only one Start trigger is required to begin waveform
generation. All Start triggers after the first Start trigger are
ignored. Once the waveform generation is complete, the analog
output indefinitely settles at the DC value of the last sample in
the waveform. The
following table provides more information about
waveform generation behavior in Arbitrary Waveform and Arbitrary
Sequence output modes.

| Output Mode | Trigger Behavior |
| --- | --- |
| Arbitrary Waveform Mode | The waveform you downloaded generates only once and waveform generation halts, unless the Arbitrary Waveform Repeat Count property or the NIFGEN_ATTR_ARB_REPEAT_COUNT attribute is set, in which case the waveform generates the specified number of times. |
| Arbitrary Sequence Mode | The waveform pattern you define in the sequence list generates only once. When a Start trigger is received, generation begins at the first segment and continues through the last segment, after which the waveform generation halts. You can determine the DC value at which waveform generation ends by configuring the last point in the final segment as the desired DC value, or you can add an extra segment filled with the same DC value. |

Parent topic:

NI 5451 Trigger Modes

<!--NI_TOPIC bundle=ni-fgen path=ni-5451-specifications.html language=enus -->
## TOPIC 00788: NI 5451 Specifications

- bundle_id: `ni-fgen`
- source_path: `ni-5451-specifications.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5451-specifications.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: For information about the signal generator specifications, refer to the device specifications. You can access these specifications by navigating to Start»All Programs»National Instruments» NI-FGEN»Documentation»NI Signal Generators Specifications, or you can visit ni.com/manuals.

### NI 5451 Specifications

For information about the signal generator
specifications, refer to the 
*device
specifications*. You can access these specifications by
navigating to 
Start»All Programs»National Instruments»
NI-FGEN»Documentation»NI Signal Generators Specifications, or you can visit 
ni.com/manuals.

Parent topic:

NI 5451 NI 5451 Overview

<!--NI_TOPIC bundle=ni-fgen path=ni-5451-standard-function-mode.html language=enus -->
## TOPIC 00789: NI 5451 Standard Function Mode

- bundle_id: `ni-fgen`
- source_path: `ni-5451-standard-function-mode.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5451-standard-function-mode.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Standard Function output mode is used to generate standard function waveforms such as sine, square, triangle, and so on. On the NI 5451, Standard Function mode is implemented through direct digital synthesis (DDS). DDS is a technique for deriving, under digital control, an analog frequency source fr

### NI 5451 Standard Function Mode

Standard Function output mode is used to generate standard
function waveforms such as sine, square, triangle, and so on. 
On the NI 5451, *Standard Function mode* is implemented
through *direct digital synthesis* (DDS). DDS is a technique for
deriving, under digital control, an analog frequency source from a
single Reference clock frequency. This technique produces
high-frequency accuracy and resolution, temperature stability,
wideband tuning, and rapid, phase-continuous frequency
switching.

In DDS mode, a fixed–size memory (called *lookup memory*) stores one cycle of a periodic waveform. A phase accumulator indexes the lookup memory. For each cycle of the device Sample clock, the sample of the waveform in lookup memory that is addressed by the phase accumulator is returned. The accumulator is then incremented by the value in the frequency control word (FCW). By adjusting the Frequency property or the NIFGEN_ATTR_FUNC_FREQUENCY attribute, NI-FGEN calculates the corresponding FCW, and you can vary the output frequency of the waveform in lookup memory. The phase accumulator increments in smaller steps for smaller FCWs. Accordingly, you need more samples to generate one waveform cycle, so the frequency is lower. A higher FCW results in a higher frequency. In DDS mode, the Sample clock does not vary with the frequency of the generated waveform. At higher frequencies, some waveform samples in lookup memory are skipped; at lower frequencies, some samples output multiple times in succession.

Parent topic:

NI 5451 Output Modes

Related concepts:

- Standard Function Mode
- Direct Digital Synthesis

<!--NI_TOPIC bundle=ni-fgen path=ni-5451-stepped-trigger-mode.html language=enus -->
## TOPIC 00790: NI 5451 Stepped Trigger Mode

- bundle_id: `ni-fgen`
- source_path: `ni-5451-stepped-trigger-mode.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5451-stepped-trigger-mode.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The waveform you downloaded generates each time a Start trigger occurs. After a waveform finishes generating, the last sample of the waveform repeats continuously until the next Start trigger is received. When the next Start trigger is received, the waveform generates again. If a Start trigger is re

### NI 5451 Stepped Trigger Mode

The waveform you downloaded generates each time a
Start trigger occurs. After a waveform finishes generating, the
last sample of the waveform repeats continuously until the next
Start trigger is received. When the next Start trigger is received,
the waveform generates again. If a Start trigger is received while
a waveform is generating, the Start trigger is ignored and another
Start trigger is required to regenerate the waveform after the last
sample generates. The
following table provides more information about
waveform generation behavior in Arbitrary Waveform and Arbitrary
Sequence output modes.

| Output Mode | Trigger Behavior |
| --- | --- |
| Arbitrary Waveform Mode | If the Arbitrary Waveform Repeat Count property or the NIFGEN_ATTR_ARB_REPEAT_COUNT attribute is set, the waveform generates the specified number of times instead of just once. |
| Arbitrary Sequence Mode | The waveforms you define in the sequence list generate one segment at a time, each time a Start trigger occurs. The waveform loops as many times as has been configured for that particular segment. After the generation of a segment has halted, the last sample of the waveform repeats continuously until the next Start trigger is received. After the sequence list is exhausted, the waveform generation returns to the first segment and subsequent Start triggers restart the process. |

Parent topic:

NI 5451 Trigger Modes

<!--NI_TOPIC bundle=ni-fgen path=ni-5451-streaming.html language=enus -->
## TOPIC 00791: NI 5451 Streaming

- bundle_id: `ni-fgen`
- source_path: `ni-5451-streaming.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5451-streaming.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Streaming is a way to generate waveforms that are too large to fit in the onboard memory of the signal generator. Streaming can be used in Arbitrary Waveform, Arbitrary Sequence, or Script output modes. To stream waveform data, allocate and identify all or a portion of the signal generator onboard m

### NI 5451 Streaming

Streaming is a way to generate waveforms that are too large to fit in the onboard memory of the signal generator. Streaming can be used in *Arbitrary Waveform*, *Arbitrary Sequence*, or *Script* output modes.

Note

#### Streaming Waveform Data

The following instructions are a guide for configuring your application for streaming. For a programmatic example, refer to Fgen Arb Waveform Streaming.vi for LabVIEW or ArbitraryWaveformStreaming.prj for LabWindows/CVI.

As an example, we have a 1.6 GB waveform we want to generate and an NI arbitrary waveform generator with 256 MB of onboard memory. This 1.6 GB waveform may be in the host memory, on disk, or data that your application generates dynamically during generation.

[IMAGE alt='image' src='GUID-0E592A7C-01F5-4B62-B514-F1A4F09AC3F9-a5.svg']

1. Specify the amount of onboard memory to be used for streaming —Call the niFgen Allocate Waveform VI or the niFgen_AllocateWaveform function to specify the amount of onboard memory to reserve for streaming. The allocated memory, known as the streaming waveform , serves as a buffer for the streaming process. The size of the waveform you wish to stream must be evenly divisible by the amount of onboard memory allocated for streaming to prevent the streaming waveform from being overwritten before it has generated.
2. Identify the streaming waveform —Set the Streaming Waveform Handle property or the NIFGEN_ATTR_STREAMING_WAVEFORM_HANDLE attribute to the waveform handle returned in Step 1. Setting this property or attribute ensures that none of your streaming data is overwritten before it is generated. NI-FGEN monitors your progress to ensure that you write fresh data fast enough to keep up with the generation. If your application fails to keep up or attempts to write fresh data over data that has not been generated, NI-FGEN returns an error.
3. Fill the streaming waveform with initial data —Call the niFgen Write Waveform VI or the niFgen_WriteWaveform function to write the first part of the waveform data to the streaming waveform in onboard memory.

 Tip 

 When transferring large blocks of waveform data, break the data into smaller blocks and call the niFgen Write Waveform VI or the niFgen_WriteWaveform function multiple times. The data is appended sequentially. A computer can allocate smaller blocks of a large waveform faster than allocating a single large contiguous block in memory. Depending on the amount of RAM on the computer, transferring ten 16 MB blocks may be faster than transferring one 160 MB block.

1. Begin generating the waveform —Call the niFgen Initiate Generation VI or the niFgen_InitiateGeneration function to begin the waveform generation. As the waveform generates, space in the streaming waveform becomes free.
2. (Optional) Monitor available memory as the waveform generates —Use the Space Available in Streaming Waveform property or the NIFGEN_ATTR_STREAMING_SPACE_AVAILABLE_IN_WAVEFORM attribute to determine how much of the streaming waveform is free for writing new data. As the waveform generates, space becomes available to write more waveform data.

1. Write a block of waveform data —Call niFgen Write Waveform VI or the niFgen_WriteWaveform function to write a new block of waveform data to the streaming waveform in onboard memory.
 
If the size of the new block of waveform data is larger than the space available, niFgen waits until sufficient space becomes available or the streaming write time expires. Use the Streaming Write Timeout property or the NIFGEN_ATTR_STREAMING_WRITE_TIMEOUT attribute to change the streaming write time.
2. Repeat steps 5 and 6 until all waveform data is written.

#### Streaming to Multiple Channels

To stream data to multiple channels, you must provide data that is interleaved. You cannot stream to two or more channels with individual, non-interleaved writes for each channel.

#### Average Performance Rates

The following tables list the average data rates possible for PXI, PCI, and PXI Express signal generators. Average data transfer rates are highly system dependent. The following table is intended to give you an idea of the average sustainable transfer rates using 16-bit (or 2 byte) samples.

#### PXI and PCI

| Data Source | Data Rate (MB/s)* |
| --- | --- |
| Host memory on desktop computer or PXI embedded controller | ~90 to 115 |
| Desktop IDE or SATA hard drive | ~55 to 70† |
| Laptop or low RPM hard drive | 25 to 30† |
| Host memory on desktop across MXI-3 to PXI board | 25 |
| Host memory on desktop across MXI-4 to PXI board | 25 |
| * All data rates highly dependent on chipset. † Measurements were taken using the Windows API for unbuffered file I/O. For more information about streaming, refer to Data Streaming Architecture in PXI Systems. |  |

#### PXI Express

| Data Source | Data Rate (MB/s)* |
| --- | --- |
| From disk, such as a redundant array of independent disks (RAID). | > 600 |
| * Data transfer rates are limited by the speed of your streaming storage solution. Refer to Data Streaming for more information. † These numbers were obtained using several file I/O optimizations. For more information about this streaming process, refer to Stream to Disk Using Win32 File IO. |  |

#### Improving Streaming Performance

To improve your maximum sustainable transfer rate for streaming, consider the following recommendations:

- Adjust the Data Transfer Block Size property or the NIFGEN_ATTR_DATA_TRANSFER_BLOCK_SIZE attribute. The default data transfer block size for NI-FGEN is 2 MS (or 4 MB). If you were to write a 16 MB waveform to the signal generator, the complete transfer would occur using four separate DMA transfers. If you modify the data transfer block size to 8 MS (16 MB), for example, the data transfer is more efficient and is instead accomplished in a single transfer.
- Configure advanced streaming properties by calling the Maximum In-Flight Read Requests, PCI DMA Optimization Enabled, or Preferred Packet Size property or the NIFGEN_ATTR_DATA_TRANSFER_MAXIMUM_IN_FLIGHT_READS , NIFGEN_ATTR_DATA_TRANSFER_PCI_DMA_OPTIMIZATIONS , or NIFGEN_ATTR_DATA_TRANSFER_PREFERRED_PACKET_SIZE attributes.
- Optimize the bus bandwidth usage for multi-device streaming applications by calling the Maximum Bandwidth property or the NIFGEN_ATTR_DATA_TRANSFER_MAXIMUM_BANDWIDTH attribute.
- When streaming from hard drives, consider the hard drive speed for maximum sustainable rates. Laptop hard drives typically have a data transfer rate of 25 to 30 MB/s. Desktop hard drives often can meet 55 to 70 MB/s. 
 Transfer rates from hard drives can vary for a number of reasons, including where the data is physically stored on the hard drive and how much data is stored. Storing your waveform files on a fairly empty, defragmented hard drive may help increase performance.
- Consider using a redundant array of independent disks (RAID) configuration to utilize striping to increase data transfer rates from disk.
- When using 18-slot PXI chassis, install the signal generator used for streaming in the first segment (Slots 2 to 6) of the PXI chassis.
- Utilize Direct DMA .

Parent topic:

NI 5451 Waveform Generation

Related concepts:

- Arbitrary Waveform Output Mode
- Arbitrary Sequence Mode
- Script Mode
- Direct DMA

<!--NI_TOPIC bundle=ni-fgen path=ni-5451-synchronization.html language=enus -->
## TOPIC 00792: NI 5451 Synchronization

- bundle_id: `ni-fgen`
- source_path: `ni-5451-synchronization.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5451-synchronization.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Your signal generator is based on the National Instruments Synchronization and Memory Core (SMC) technology and therefore supports TClk synchronization. Refer to the NI-TClk Synchronization Help for more information about NI-TClk Synchronization.

### NI 5451 Synchronization

Your signal generator is based on the 
National Instruments
Synchronization and Memory Core (SMC) technology and therefore
supports TClk synchronization. Refer to the 
NI-TClk
Synchronization Help for more information about NI-TClk
Synchronization.

Parent topic:

NI 5451 NI 5451 Overview

<!--NI_TOPIC bundle=ni-fgen path=ni-5451-syntax-for-terminal-names.html language=enus -->
## TOPIC 00793: NI 5451 Syntax for Terminal Names

- bundle_id: `ni-fgen`
- source_path: `ni-5451-syntax-for-terminal-names.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5451-syntax-for-terminal-names.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The syntax for terminal names is a unique identifier that refers to a physical terminal in your system. To guarantee the uniqueness of a terminal name across multiple devices, terminal names begin with a forward slash, followed by the name of the device as configured in MAX, such as Dev1. A forward

### NI 5451 Syntax for Terminal Names

The syntax for terminal names is a unique
identifier that refers to a physical terminal in your system. To
guarantee the uniqueness of a terminal name across multiple
devices, terminal names begin with a forward slash, followed by the
name of the device as configured in MAX, such as 
Dev1. A forward slash and the name
of the terminal follow the device identifier, such as 
PFI1. For example, the fully
qualified terminal name for 
PFI1 on 
Dev1 is 
/Dev1/PFI1.

Parent topic:

NI 5451 Signal Routing

<!--NI_TOPIC bundle=ni-fgen path=ni-5451-theory-of-operation.html language=enus -->
## TOPIC 00794: NI 5451 Theory of Operation

- bundle_id: `ni-fgen`
- source_path: `ni-5451-theory-of-operation.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5451-theory-of-operation.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Expand this topic for information about the theory of operation of your signal generator.

### NI 5451 Theory of Operation

Expand this topic for information about the theory
of operation of your signal generator.

Parent topic:

NI 5451 NI 5451 Overview

<!--NI_TOPIC bundle=ni-fgen path=ni-5451-thermal-shutdown.html language=enus -->
## TOPIC 00795: NI 5451 Thermal Shutdown

- bundle_id: `ni-fgen`
- source_path: `ni-5451-thermal-shutdown.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5451-thermal-shutdown.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: NI-FGEN supports thermal shutdown capability for the NI 5451. This capability allows the signal generator to detect when it has reached a dangerously high temperature and to then power down to prevent damage to the device. Air circulation paths, fan settings, and space allowances are several factors

### NI 5451 Thermal Shutdown

NI-FGEN supports thermal shutdown capability for
the NI 5451. This
capability allows the signal generator to detect when it has
reached a dangerously high temperature and to then power down to
prevent damage to the device.

Air circulation paths, fan settings, and space
allowances are several factors that can influence device
temperature. To prevent thermal shutdown, follow the guidelines
described in the Maintain Forced-Air Cooling Note to Users document
that shipped with your device. Refer to the 
*device specifications* to find the correct operating temperature
range.

In the event that the signal generator powers down,
you are notified with an error message in one of the following
ways:

- NI-FGEN returns an error when you use any of the VIs or
functions that program the hardware or check hardware status, for
example, the 
niFgen Commit VI or
the 
 niFgen_commit function and the 
niFgen Self Cal
VI or the 
 niFgen_SelfCal function.
- MAX returns an error
message if you run a self-test on your device after it exceeds the
thermal shutdown temperature.

To re-enable your device after thermal shutdown,
use one of the following methods:

- Power down the computer or chassis that contains the signal
generator.

OR

- Call the 
niFgen Reset
Device VI or the 
 niFgen_ResetDevice function or perform a device reset in MAX. For more
information about resetting a device in MAX, select 
 Help»Help Topics»NI-DAQmx»MAX Help for NI-DAQmx 
within MAX.

Review the guidelines in the 
Maintain Forced-Air Cooling Note to Users document that
shipped with the product and make any necessary adjustments to
ensure that the signal generator cools effectively. The thermal
shutdown error continues to be reported until the device is
successfully reset.

Parent topic:

NI 5451 NI 5451 Overview

<!--NI_TOPIC bundle=ni-fgen path=ni-5451-tone.html language=enus -->
## TOPIC 00796: NI 5451 Tone

- bundle_id: `ni-fgen`
- source_path: `ni-5451-tone.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5451-tone.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the behavior of the OSP block during tone generation. Use the Standard Function output mode to generate a tone. During tone generation, the NCO is used to create the output signal.

### NI 5451 Tone

The following figure shows the behavior of the OSP
block during tone generation.

[IMAGE alt='image' src='GUID-302E96F5-636C-4A9D-BFFE-B79B6B151212-a5.gif']

Use the 
*Standard Function output
mode* to generate a tone. During tone generation,
the 
*NCO* is used to create the
output signal.

Parent topic:

NI 5451 Common Onboard Signal Processing Applications

Related concepts:

- Standard Function Mode
- NI 5451 Numerically Controlled Oscillator (NCO)

<!--NI_TOPIC bundle=ni-fgen path=ni-5451-trigger-modes.html language=enus -->
## TOPIC 00797: NI 5451 Trigger Modes

- bundle_id: `ni-fgen`
- source_path: `ni-5451-trigger-modes.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5451-trigger-modes.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5451 has four trigger modes: Single, Continuous, Stepped, and Burst. These trigger modes are available for Arbitrary Waveform, and Arbitrary Sequence output modes. Refer to the niFgen Configure Trigger Mode VI or the niFgen_ConfigureTriggerMode function for information about setting the trigg

### NI 5451 Trigger Modes

The NI 5451 has four trigger modes: Single, Continuous, Stepped,
and Burst. These trigger modes are available for Arbitrary
Waveform, and Arbitrary Sequence output modes.
Refer to the 
niFgen
Configure Trigger Mode VI or the 
niFgen_ConfigureTriggerMode function for information about setting the trigger mode.

Parent topic:

NI 5451 Triggering

<!--NI_TOPIC bundle=ni-fgen path=ni-5451-trigger-sources.html language=enus -->
## TOPIC 00798: NI 5451 Trigger Sources

- bundle_id: `ni-fgen`
- source_path: `ni-5451-trigger-sources.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5451-trigger-sources.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Trigger sources are software selectable. You can use any of the following external input triggers: PFI 0 or PFI 1 on the front panel connectors PXI_TRIG<0..7> lines on the PXI trigger bus backplane The following figure shows the possible trigger sources for the NI 5451. ^ § Refer to Exporting Signal

### NI 5451 Trigger Sources

Trigger sources are software selectable. You can
use any of the following external input triggers:

- PFI 0 or PFI 1 on the front panel connectors

- PXI_TRIG<0..7> lines on the PXI trigger bus backplane

The following figure shows the possible trigger
sources for the NI 5451.

[IMAGE alt='image' src='GUID-800E238B-D859-498D-84F0-2863F4969FAA-a5.gif']

<sup>§</sup>Refer to 
*Exporting Signals* for
more information routing signals.

All triggers are ignored until you call the 
niFgen
Initiate Generation VI or the 
niFgen_InitiateGeneration function.

The default trigger source for NI-FGEN is
Immediate, which causes an automatic Start trigger pulse to be
generated internally as soon as hardware can generate signals after
generation has been initiated. You can configure the trigger source
with 
niFgen
Configure Trigger VI or the 
niFgen_ConfigureTriggerSource function. Refer to the 
niFgen
Send Software Edge Trigger VI or the 
niFgen_SendSoftwareEdgeTrigger function for more information about programmatically
triggering the device.

Refer to the 
*device
specifications* for the minimum Start trigger pulse width
required for operation.

#### Related Topics

*PXI Trigger Lines*

Parent topic:

NI 5451 Triggering

Related concepts:

- NI 5451 Exporting Signals
- PXI Trigger Lines

<!--NI_TOPIC bundle=ni-fgen path=ni-5451-trigger-timing.html language=enus -->
## TOPIC 00799: NI 5451 Trigger Timing

- bundle_id: `ni-fgen`
- source_path: `ni-5451-trigger-timing.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5451-trigger-timing.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the relationship between Start trigger and the waveform output. t[s1] is the required pulse width on the Start trigger signal. t[s2] is the delay from the Start trigger to the waveform output. Refer to the NI PXIe-5451 specifications for more information about these timing

### NI 5451 Trigger Timing

The following figure shows the relationship between
Start trigger and the waveform output. t<sub>s1</sub> is the required pulse width on the Start trigger
signal. t<sub>s2</sub> is the delay from the Start trigger to the waveform
output. Refer to the 
*NI PXIe-5451
specifications* for more information about these timing
parameters.

[IMAGE alt='image' src='GUID-9DD6A51C-2BCA-4129-9C8D-0A821181925F-a5.gif']

The NI 5451 also allows you to export
signals to trigger other devices based on the waveform output of
the signal generator. The exported Start trigger can be exported from the signal
generator to signal other devices that waveform generation has
started.

The exported Start Trigger is a slightly
delayed version of the Start trigger used for waveform generation.
It is guaranteed to be at least 150 ns wide. The preceding
figure also shows the relationship between Start trigger and the
exported Start trigger. t<sub>s3</sub> is the delay between the Start trigger and the time
the device generates the exported Start trigger. t<sub>s4</sub> is the pulse width of the exported Start trigger
signal.

Parent topic:

NI 5451 Triggering

<!--NI_TOPIC bundle=ni-fgen path=ni-5451-triggering.html language=enus -->
## TOPIC 00800: NI 5451 Triggering

- bundle_id: `ni-fgen`
- source_path: `ni-5451-triggering.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5451-triggering.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can define the signal generator functionality by using the various triggering techniques. Expand this section to learn more about using triggers with your signal generator.

### NI 5451 Triggering

You can define the signal generator functionality
by using the various triggering techniques. Expand this section to
learn more about using triggers with your signal generator.

Parent topic:

NI 5451 NI 5451 Overview

<!--NI_TOPIC bundle=ni-fgen path=ni-5451-waveform-amplitude-control.html language=enus -->
## TOPIC 00801: NI 5451 Waveform Amplitude Control

- bundle_id: `ni-fgen`
- source_path: `ni-5451-waveform-amplitude-control.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5451-waveform-amplitude-control.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5451 can be configured to achieve required amplitude settings. Output Paths and Amplifiers Main Path The following figure shows the Main path. The Main path can generate single-ended or differential output depending on the configuration. The Main path can generate a maximum of 5 V[pk-pk] DC d

### NI 5451 Waveform Amplitude Control

The NI 5451 can be configured to achieve required amplitude settings.

#### Output Paths and Amplifiers

#### Main Path

The following figure shows the Main path.

[IMAGE alt='image' src='GUID-721289BC-ADEC-4CA7-9815-3BFE73A53263-a5.gif']

Note

The Main path can generate a maximum of 5 V<sub>pk-pk</sub> DC differential output into 50 Ω with up to 63 dB of selectable attenuation. The Main path also has a selectable lowpass filter for image rejection.

#### Direct Path

The following figure shows the Direct path.

[IMAGE alt='image' src='GUID-53F287B0-F155-4DDF-8380-C55DFDB58A40-a5.gif']

The Direct path provides the output of the main DAC
to the CH 0+/− connectors with the fewest electronic components in the path.
There are no programmable amplifiers and there is no method for adding DC
offset to the waveform. The Direct path can generate a maximum of 
1.0 V<sub>pk-pk</sub> differential output into 50 Ω. The maximum gain setting for an Analog Output path
configured to the Direct path is 0.5 (gain is a unitless
value).

Parent topic:

NI 5451 Analog Output

<!--NI_TOPIC bundle=ni-fgen path=ni-5451-waveform-and-generation-instruction-m.html language=enus -->
## TOPIC 00802: NI 5451 Waveform and Generation Instruction Memory Size

- bundle_id: `ni-fgen`
- source_path: `ni-5451-waveform-and-generation-instruction-m.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5451-waveform-and-generation-instruction-m.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Waveform Memory Size Waveforms are stored in the NI 5451 onboard memory in contiguous blocks. These blocks are allocated in multiples of 128 bytes. This allocation style means that while waveform sizes may be multiples of two samples (four bytes) on the NI 5451, the amount of onboard memory allocate

### NI 5451 Waveform and Generation Instruction Memory Size

#### Waveform Memory Size

Waveforms are stored in the
NI 5451 onboard memory in contiguous
blocks. These blocks are allocated in multiples of 128 bytes. This
allocation style means that while waveform sizes may be multiples
of 
two samples (four bytes) on the NI 5451, the amount of
onboard memory allocated for each waveform is a multiple of 128
bytes. The following figure represents the total memory of a device
and shows memory that was initially empty, but it now has multiple
waveforms written to it, nearly filling the device memory.

[IMAGE alt='image' src='GUID-84BB06FA-B7C3-44C6-B2D1-0CB400485AB6-a5.gif']

Calculate the amount of memory that a waveform takes up in
the onboard memory with the
following two rules.

1. Each sample in the waveform uses two bytes of memory space.
Four bytes are used when the onboard signal processing block is
enabled and the 
Data
Processing Mode property is set to Complex or the 
 NIFGEN_ATTR_OSP_DATA_PROCESSING_MODE is set to 
 NIFGEN_VAL_OSP_COMPLEX .
2. Memory is written to in blocks of 4 bytes.

Calculate the memory size by multiplying the number
of samples in the waveform by two (or four) and then rounding this
value up to the nearest multiple of 128.

#### Examples

1. A waveform containing 16 samples occupies 32 bytes in memory.
By rounding up to the nearest multiple of 128, you can determine
that the waveform occupies 128 bytes in memory.
2. A waveform containing 64 samples occupies 128 bytes in memory.
By rounding up to the nearest multiple of 128, you can determine
that the waveform occupies 128 bytes in memory.
3. A waveform containing 68 samples occupies 136 bytes in memory.
By rounding up to the nearest multiple of 128, you can determine
that the waveform occupies 256 bytes in memory.
4. A waveform containing 10,000 samples occupies
20,000 bytes in memory. By rounding up to the nearest multiple
of 128, you can determine that the waveform occupies 20,096 bytes
in memory.
5. A waveform containing 64 complex samples occupies 256 bytes in
memory. By rounding up to the nearest multiple of 256, you can
determine that the waveform occupies 256 bytes in memory. This
example is only possible with the OSP block
enabled.

#### Instruction Memory Size

| Instruction Memory Size* Formulae |  |
| --- | --- |
| Arbitrary Waveform Mode | Size in bytes = 256 per waveform |
| Arbitrary Sequence ModeN = Number of segments in sequence | Stepped: Size in bytes = 208 + (80 × N) |
| Continuous: Size in bytes = 208 + (64 × N) |  |
| Single: Size in bytes = 80 + (64 × N) |  |
| Burst: Size in bytes = 160 + (128 × N) |  |
| *The instruction size in memory is the size, in bytes, rounded up to the nearest multiple of 128 bytes. |  |

#### Examples

1. The memory size required to generate a waveform in Arbitrary
Waveform mode is always 256 bytes of onboard memory for that
specific waveform. Each waveform that is saved to onboard memory
uses 256 byes of memory for instructions.
2. The memory size required to generate a waveform using Arbitrary
Sequence mode and Stepped trigger mode with 50 segments in a
sequence list is determined by the following formula:
 Size in Bytes = 208 + (80 × 50) = 4,208
bytes. 
 Size in memory = 4,208 coerced up to the next
multiple of 128 = 4,224 bytes.
3. The memory size required to generate a waveform using Arbitrary
Sequence mode and Continuous trigger mode with 500 segments in
a sequence list is determined by the following formula:
 Size in Bytes = 208 + (64 × 500) = 32,208
bytes. 
 Size in memory = 32,208 coerced up to the next
multiple of 128 = 32,256 bytes.
4. The memory size required to generate a waveform using Arbitrary
Sequence mode and Single trigger mode with 1,003 segments in a
sequence list is determined by the following formula:
 Size in Bytes = 80 + (64 × 1,003) = 64,272
bytes. 
 Size in memory = 64,272 coerced up to the next
multiple of 128 = 64,284 bytes.
5. The memory size required to generate a waveform using Arbitrary
Sequence mode and Burst trigger mode with 2345 segments in a
sequence list is determined by the following formula:
 Size in Bytes = 160 + (128 × 2,345) =
300,320 bytes. 
 Size in memory = 300,320 coerced up to the
next multiple of 128 = 300,416 bytes.

#### Total Memory Size

The following examples show how to calculate total
memory for an application. The examples use each of the four
trigger modes for the Arbitrary Sequence mode and use varying
numbers of waveforms, waveform sizes, and number of segments in the
sequences.

Note

#### Examples

1. An application requires using three waveforms with the
following sizes: 72; 132; and 260 samples. The waveforms are
generated by using Arbitrary Sequence mode and Single trigger mode
to configure 20,000 segments in a sequence list. The following
tables show all the numbers used to determine the total memory
stored in the onboard memory: 1,281,408 bytes.

| Waveforms | Samples | Bytes | Rounded Size |
| --- | --- | --- | --- |
| A | 72 | 144 | 256 |
| B | 132 | 264 | 384 |
| C | 260 | 520 | 640 |
| Memory Size = |  |  | 1,280 |

| Number of Segments in Sequence | Memory Calculation | Bytes | Rounded Size |
| --- | --- | --- | --- |
| 20,000 | 80 + (64 × 20,000) = | 1,280,080 | 1,280,128 |

Total Onboard Memory Used = 1,281,408 bytes

1. An application requires using six waveforms with the following
sizes: 480; 260; 960; 492; 516; and 604 samples. The waveforms are
generated by using Arbitrary Sequence mode and Burst trigger mode
to configure 10,000 segments in a sequence list. The following
table shows all the numbers used to determine the total memory
stored in the onboard memory: 135,296 bytes.

| Waveforms | Samples | Bytes | Rounded Size |
| --- | --- | --- | --- |
| A | 480 | 960 | 1,024 |
| B | 260 | 520 | 640 |
| C | 960 | 1,920 | 1,920 |
| D | 492 | 984 | 1,024 |
| E | 516 | 1,032 | 1,152 |
| F | 604 | 1,208 | 1,280 |
| Memory Size = |  |  | 7,040 |

| Number of Segments in Sequence | Memory Calculation | Bytes | Rounded Size |
| --- | --- | --- | --- |
| 10,000 | 160 + (128 × 10,000) = | 128,160 | 128,256 |

Total Onboard Memory Used = 135,296 bytes

1. An application requires using five waveforms with the following
sizes: 10,000; 1,000,000; 2,000,000; 30,000,000; and
5,000 samples. The waveforms are generated by using Arbitrary
Sequence mode and Stepped trigger mode to configure
2,000 segments in a sequence list. The following table shows
all the numbers used to determine the total memory stored in the
onboard memory: 66,190,464 bytes.

| Waveforms | Samples | Bytes | Rounded Size |
| --- | --- | --- | --- |
| A | 10,000 | 20,000 | 20,096 |
| B | 1,000,000 | 2,000,000 | 2,000,000 |
| C | 2,000,000 | 4,000,000 | 4,000,000 |
| D | 30,000,000 | 60,000,000 | 60,000,000 |
| E | 5,000 | 10,000 | 10,112 |
| Memory Size = |  |  | 66,030,208 |

| Number of Segments in Sequence | Memory Calculation | Bytes | Rounded Size |
| --- | --- | --- | --- |
| 2,000 | 208 + (80 × 2,000) = | 160,208 | 160,256 |

Total Onboard Memory Used = 66,190,464 bytes

1. An application requires using seven waveforms with the
following sizes: 1,000; 2,000; 2,000; 10,000; 20,000; 500; and
260 samples. The waveforms are generated by using Arbitrary
Sequence mode and Continuous trigger mode to configure
100 segments in a sequence list. The following table shows all
the numbers used to determine the total memory stored in the
onboard memory: 78,720 bytes.

| Waveforms | Samples | Bytes | Rounded Size |
| --- | --- | --- | --- |
| A | 1,000 | 2,000 | 2,048 |
| B | 2,000 | 4,000 | 4,096 |
| C | 2,000 | 4,000 | 4,096 |
| D | 10,000 | 20,000 | 20,096 |
| E | 20,000 | 40,000 | 40,064 |
| F | 500 | 1,000 | 1,024 |
| G | 260 | 520 | 640 |
| Memory Size = |  |  | 72,064 |

| Number of Segments in Sequence | Memory Calculation | Bytes | Rounded Size |
| --- | --- | --- | --- |
| 100 | 208 + (64 × 100) = | 6,608 | 6,656 |

Total Onboard Memory Used = 78,720 bytes

1. An application requires using seven complex waveforms with the
following sizes: 500; 1,000; 1,000; 5,000; 10,000; 250; and
130 samples with the 
OSP block enabled and the Data
Processing Mode property set to Complex or the 
 NIFGEN_ATTR_OSP_DATA_PROCESSING_MODE 
attribute set to 
 NIFGEN_VAL_OSP_COMPLEX .
Additionally, the signal generator is configured for Arbitrary
Sequence mode and Continuous trigger mode with 100 segments in
a sequence list. The following table shows all the numbers used to
determine the total memory stored in the onboard memory:
78,720 bytes.

| Waveforms | Samples | Bytes | Rounded Size |
| --- | --- | --- | --- |
| A | 500 | 2,000 | 2,048 |
| B | 1,000 | 4,000 | 4,096 |
| C | 1,000 | 4,000 | 4,096 |
| D | 5,000 | 20,000 | 20,096 |
| E | 10,000 | 40,000 | 40,064 |
| F | 250 | 1,000 | 1,024 |
| G | 130 | 520 | 640 |
| Memory Size = |  |  | 72,064 |

| Number of Segments in Sequence | Memory Calculation | Bytes | Rounded Size |
| --- | --- | --- | --- |
| 100 | 208 + (64 × 100) = | 6,608 | 6,656 |

Total Onboard Memory Used = 78,720 bytes

Parent topic:

NI 5451 Onboard Memory

<!--NI_TOPIC bundle=ni-fgen path=ni-5451-waveform-generation.html language=enus -->
## TOPIC 00803: NI 5451 Waveform Generation

- bundle_id: `ni-fgen`
- source_path: `ni-5451-waveform-generation.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5451-waveform-generation.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5451 supports the following output, or generation, modes: Standard Function Arbitrary Waveform Arbitrary Sequence Script To select an output mode, set the Output Mode parameter of the niFgen Configure Output Mode VI or the niFgen_ConfigureOutputMode function.

### NI 5451 Waveform Generation

The NI 5451 supports the
following output, or generation, modes:

- Standard Function

- Arbitrary Waveform
- Arbitrary Sequence
- Script

To select an output mode, set the 
Output Mode parameter of the 
niFgen
Configure Output Mode VI or the 
niFgen_ConfigureOutputMode function.

Parent topic:

NI 5451 NI 5451 Overview

Related concepts:

- NI 5451 Standard Function Mode
- NI 5451 Arbitrary Waveform Mode
- NI 5451 Arbitrary Sequence Mode
- NI 5451 Script Mode

<!--NI_TOPIC bundle=ni-fgen path=ni-5451-waveform-quantum.html language=enus -->
## TOPIC 00804: NI 5451 Waveform Quantum

- bundle_id: `ni-fgen`
- source_path: `ni-5451-waveform-quantum.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5451-waveform-quantum.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Quantum is the increment in samples that waveform sizes must adhere to. The NI 5450 has a sample quantum of two, allowing waveforms of any even numbered size (between the maximum and minimum waveform sizes) to be downloaded. For example, if while in Arbitrary Waveform mode, you request to load a wav

### NI 5451 Waveform Quantum

Quantum is the increment in samples that waveform
sizes must adhere to. The NI 5450 has a sample quantum of two, allowing waveforms of any even numbered size (between the maximum and minimum waveform
sizes) to be downloaded.

For example, if while in Arbitrary Waveform mode, you request to load a waveform of seven samples, the task will not complete successfully because the waveform is not an integer multiple of the quantum size. Waveform sizes that meet the conditions include 2, 4, 8, 10, 12, and so on, up to maximum allowable waveform size.

Parent topic:

NI 5451 Waveform Size and Quantum

<!--NI_TOPIC bundle=ni-fgen path=ni-5451-waveform-size-and-quantum.html language=enus -->
## TOPIC 00805: NI 5451 Waveform Size and Quantum

- bundle_id: `ni-fgen`
- source_path: `ni-5451-waveform-size-and-quantum.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5451-waveform-size-and-quantum.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5451 onboard memory architecture imposes certain requirements on the waveform size and quantum.

### NI 5451 Waveform Size and Quantum

The NI 5451 onboard memory architecture
imposes certain requirements on the waveform *size* and *quantum*.

Parent topic:

NI 5451 Waveform Generation

Related concepts:

- NI 5451 Waveform Size
- NI 5451 Waveform Quantum

<!--NI_TOPIC bundle=ni-fgen path=ni-5451-waveform-size.html language=enus -->
## TOPIC 00806: NI 5451 Waveform Size

- bundle_id: `ni-fgen`
- source_path: `ni-5451-waveform-size.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5451-waveform-size.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Minimum Waveform Size The minimum waveform size on the NI 5451 depends on the output mode and the trigger mode. Refer to the device specifications for the minimum waveform size values for the different modes. To provide greater programming flexibility, NI-FGEN does not strictly enforce the minimum

### NI 5451 Waveform Size

#### Minimum Waveform Size

The
minimum waveform size on the NI 5451 depends on the output mode and the 
*trigger mode*. Refer to
the 
*device
specifications* for the minimum waveform size values for the
different modes.

Note

device
specifications

NIFGEN_ATTR_OSP_DATA_PROCESSING_MODE

niFgen_AbortGeneration

niFgen_WaitUntilDone

niFgen_IsDone

niFgen_IsDone

#### Maximum Waveform Size

The maximum waveform size allowed depends on the
remaining available space in the onboard memory of the device. The 
remaining available space depends on factors such as any waveforms
and generation instructions currently occupying memory space in the
onboard memory. The maximum allowable size equals the 
*memory size* of the device
minus the data already in memory. Query the 
Max
Waveform Size property or the 
NIFGEN_ATTR_MAX_WAVEFORM_SIZE attribute for the current largest size waveform that can be
downloaded to the device.

You can download floating point, signed 16-bit
binary, or complex floating-point waveforms to the device onboard
memory. For information about downloading waveforms to the onboard
memory in LabVIEW, refer to the 
niFgen
Create Waveform or 
niFgen
Write Waveform VIs for more information. For information about
downloading waveforms to the onboard memory in C, refer to the 
niFgen_CreateWaveformF64, 
niFgen_CreateWaveformI16, 
niFgen_CreateWaveformComplexF64, 
niFgen_WriteWaveform, 
niFgen_WriteBinary16Waveform, or 
niFgen_WriteWaveformComplexF64 functions for more information.

Parent topic:

NI 5451 Waveform Size and Quantum

Related concepts:

- NI 5451 Trigger Modes
- NI 5451 Waveform and Generation Instruction Memory Size

<!--NI_TOPIC bundle=ni-fgen path=ni-5451-writing-i-q-data.html language=enus -->
## TOPIC 00807: NI 5451 Writing I/Q Data

- bundle_id: `ni-fgen`
- source_path: `ni-5451-writing-i-q-data.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5451-writing-i-q-data.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: On multichannel devices, I/Q data can either be written to individual channels (for example, designating one channel for I data and one channel for Q data) or to both channels of the device at once when following the multichannel waveform allocation guidelines.

### NI 5451 Writing I/Q Data

On multichannel devices, I/Q data can either be written to individual channels (for example, designating one channel for I data and one channel for Q data) or to both channels of the device at once when following the *multichannel waveform allocation* guidelines.

Parent topic:

NI 5451 Theory of Operation

Related concepts:

- NI 5451 Multichannel Waveform Allocation

<!--NI_TOPIC bundle=ni-fgen path=ni-fgen-error-codes.html language=enus -->
## TOPIC 00808: NI-FGEN Error Codes

- bundle_id: `ni-fgen`
- source_path: `ni-fgen-error-codes.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-fgen-error-codes.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: When the NI-FGEN driver encounters an error, it returns an error code. This code value can be in hexadecimal, decimal, or text depending on your application. To understand the error code, you need to read the error description. For example, the error "-1074135039" or "(0xBFFA0001 - Instrument Specif

### NI-FGEN Error Codes

When the NI-FGEN driver encounters an error, it
returns an error code. This code value can be in hexadecimal,
decimal, or text depending on your application. To understand the
error code, you need to read the error description.

For example, the error "-1074135039" or
"(0xBFFA0001 - Instrument Specific error)" encompasses many
different error cases. To better understand the error specific to
your application, you need to read the error description.

#### LabVIEW Example

LabVIEW users can read the error description by
creating an error indicator from one of the NI-FGEN VIs as shown in
the following figure.

[IMAGE alt='image' src='GUID-A176419C-4F11-4FD3-95CE-79CA8AFD1EC4-a5.gif']

#### C Example

void ErrorBox() {

ViUInt32 errMsgSize;

ViChar* errMsg;

if(error <0) {

errMsgSize = niFgen_GetError(vi, VI_NULL, 0, VI_NULL);

errMsg = (ViChar *) malloc(sizeof(ViChar) * errMsgSize);

niFgen_GetError(vi, &error, errMsgSize, errMsg);

ResetTextBox(fgenPanel, FGEN_PANEL_ERROR_MESSAGE, errMsg);

free(errMsg);

}

else if(error == VI_SUCCESS) ResetTextBox(fgenPanel,
FGEN_PANEL_ERROR_MESSAGE, "");

}

Parent topic:

NI-FGEN Tutorial

<!--NI_TOPIC bundle=ni-fgen path=ni-fgen-tutorial.html language=enus -->
## TOPIC 00809: NI-FGEN Tutorial

- bundle_id: `ni-fgen`
- source_path: `ni-fgen-tutorial.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-fgen-tutorial.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Example Programs NI-FGEN ships with several examples that demonstrate basic signal generator applications. You can access these examples through the Start menu, by navigating to Start»All Programs»National Instruments»NI-FGEN»Examples. The NI-FGEN examples assume that you are already familiar wit

### NI-FGEN Tutorial

#### Example Programs

NI-FGEN ships with several examples that
demonstrate basic signal generator applications. You can access
these examples through the Start menu, by navigating to 
Start»All Programs»National
Instruments»NI-FGEN»Examples.

Note

NI-FGEN provides the same functionality in two
different formats—as virtual instruments (VIs) in LabVIEW and
as functions in C-based programming languages.

#### Basic Steps

The tutorial explains how to complete the following
programming steps:

1. Initialize the session
2. Configure an
application
3. Initiate generation
4. Abort generation
5. Close the session
6. Retrieve error information

After you understand the programming process
outlined in this tutorial, you can find advanced information about
programming specific signal generator features with the NI-FGEN
instrument driver in the 
*Features* section.

Parent topic:

Programming

Related concepts:

- Initialize
- Configuration
- Initiate Generation
- Abort Generation
- Closing the Session
- NI-FGEN Error Codes
- Features

<!--NI_TOPIC bundle=ni-fgen path=nyquist-and-shannon-s-sampling-theorems.html language=enus -->
## TOPIC 00810: Nyquist and Shannon's Sampling Theorems

- bundle_id: `ni-fgen`
- source_path: `nyquist-and-shannon-s-sampling-theorems.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/nyquist-and-shannon-s-sampling-theorems.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Nyquist theorem concerns digital sampling of a continuous time analog waveform, while Shannon’s Sampling theorem concerns the creation of a continuous time analog waveform from digital, discrete samples. Nyquist Theorem The Nyquist theorem states that an analog signal must be sampled at least tw

### Nyquist and Shannon's Sampling Theorems

The Nyquist theorem concerns digital sampling of a continuous time analog waveform, while Shannon’s Sampling theorem concerns the creation of a continuous time analog waveform from digital, discrete samples.

#### Nyquist Theorem

The Nyquist theorem states that an analog signal must be sampled at least twice as fast as the bandwidth of the signal to accurately reconstruct the waveform; otherwise, the high-frequency content creates an alias at a frequency inside the spectrum of interest (passband). An *alias* is a false lower frequency component that appears in sampled data acquired at too low a sampling rate. The following figure shows a 5 MHz sine wave digitized by a 6 MS/s analog-to-digital converter (ADC). In this figure, the dotted line represents the sine wave being digitized, while the solid line represents the aliased signal recorded by the ADC at that sample rate.

[IMAGE alt='image' src='GUID-3D8A62FB-61A8-4B11-9E78-311AE33FB903-a5.gif']

The 5 MHz frequency aliases back in the passband, falsely appearing as a 1 MHz sine wave.

#### Shannon’s Sampling Theorem

Shannon’s Sampling theorem states that a digital waveform must be updated at least twice as fast as the bandwidth of the signal to be accurately generated. The same image that was used for the Nyquist example can be used to demonstrate Shannon’s Sampling theorem. The following figure shows a desired 5 MHz sine wave generated by a 6 MS/s DAC. The dotted line represents the desired waveform, and the arrows represent the digitized samples that are available to recreate the continuous time 5 MHz sine wave. The solid line indicates the signal that would be seen, for example, with an oscilloscope at the output of a DAC.

[IMAGE alt='image' src='GUID-3D8A62FB-61A8-4B11-9E78-311AE33FB903-a5.gif']

In this case, the high–frequency sine wave is the desired signal, but was severely undersampled by only being generated by a 6 MS/s DAC; the actual resulting waveform is a 1 MHz signal.

In systems where you want to generate accurate signals using sampled data, you must set the sampling rate high enough to prevent aliasing.

Parent topic:

Sample Rate

Related concepts:

- Aliased Images

<!--NI_TOPIC bundle=ni-fgen path=output-attenuation.html language=enus -->
## TOPIC 00811: Output Attenuation

- bundle_id: `ni-fgen`
- source_path: `output-attenuation.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/output-attenuation.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Output attenuation is a method of controlling the output voltage level of the signal being generated. NI signal generators typically generate signals with a digital-to-analog converter (DAC) that has an output voltage range from ±1.0 V to ±5.0 V with a number of bits of resolution. This signal is th

### Output Attenuation

Output attenuation is a method of controlling the output voltage level of
 the signal being generated. NI signal generators typically generate signals
 with a digital-to-analog converter (DAC) that has an output voltage range from ±1.0 V to ±5.0 V with a number
 of bits of resolution. This signal is then applied to switchable amplifiers and attenuators
 to control the output voltage range of the signal source.

By attenuating the DAC output signal, you keep the dynamic range of the DAC; that is, you do not
 lose any bits from the digital representation of the signal because the attenuation is
 done after the DAC and not before it.

For example, if a DAC with a range from –5.0 V to +5.0 V and a resolution of 12 bits with each bit
 corresponding to 2.44 mV [ ( +5.0 – (–5.0) ) / 2<sup>12</sup> ] does not use output
 attenuation, and the desired signal is +2.0 V<sub>pk-pk</sub> (–1.0 V to +1.0 V), waveform values can be generated with the DAC
 that only use <sup>1</sup>/<sub>5</sub> of the DAC range. The resolution of each digital
 bit is still 2.44 mV.

However, if the same DAC uses the output attenuation, the full range of the DAC generates the
 signal, creating the signal at the full 10.0 V<sub>pk-pk</sub>. The value of each digital bit is still the original
 2.44 mV. The signal is applied to an attenuator,
 which reduces the voltage level by a factor of 5 to 2 V<sub>pk-pk</sub>. The attenuator also reduces the value of each bit, which
 results in an effective bit value of 0.488 mV at the
 analog output connector. The attenuator allows the use of the full range of the DAC, and
 reduces the effective value of each bit corresponding to the degree of attenuation.

Parent topic:

Waveform Fundamentals

<!--NI_TOPIC bundle=ni-fgen path=output-enable.html language=enus -->
## TOPIC 00812: Output Enable

- bundle_id: `ni-fgen`
- source_path: `output-enable.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/output-enable.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can switch off the waveform generation at the output connector by controlling the output enable relay on the signal generator. When the output enable relay is disabled, the output signal level goes to ground level and waveform generation continues.

### Output Enable

You can switch off the waveform generation at the output connector by
 controlling the output enable relay on the signal generator. When the output
 enable relay is disabled, the output signal level goes to ground level and waveform
 generation continues.

Parent topic:

Waveform Fundamentals

<!--NI_TOPIC bundle=ni-fgen path=output-impedance.html language=enus -->
## TOPIC 00813: Output Impedance

- bundle_id: `ni-fgen`
- source_path: `output-impedance.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/output-impedance.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: NI signal generators have an output impedance of 50 Ω and an optional 75 Ω on select devices. If the load impedance matches the output impedance, the voltage at the signal output connector is at the needed level. The voltage at the signal output connector varies with load output impedance, up to dou

### Output Impedance

NI signal generators have an output impedance of 50 Ω
 and an optional 75 Ω on select devices.

If the load impedance matches the output impedance, the voltage at the signal output connector is
 at the needed level. The voltage at the signal output connector varies with load output
 impedance, up to doubling the voltage for a high impedance load, as shown in the following
 figure.

[IMAGE alt='image' src='GUID-1BF9FAF4-5B96-4FDC-A8CD-45E6281A38B8-a5.gif']

In the previous figure, the required output voltage is ±5 V. The
 NI signal generator internal voltage source generates twice this voltage, ±10 V, expecting the voltage to be halved due to the voltage divider
 formed by R <sub>O</sub> and R <sub>L</sub> . The relationship between the output voltage and the
 load can be calculated using the following equation:

V <sub>out</sub>
 = [ R <sub>L</sub>
/( R <sub>L</sub>
 + R <sub>O</sub>
)] × [ V <sub>S</sub>
]

where

V<sub>out</sub> = the voltage level delivered to R<sub>L</sub>

R<sub>L</sub>
 = the load impedance in ohms

R<sub>O</sub>
 = the output impedance on the NI signal generator

V<sub>S</sub>
 = the voltage level generated by the source previous to R<sub>O</sub>

By default, R<sub>O</sub> = 50 Ω, but you can use NI-FGEN to set
 it to 75 Ω on select devices. Also, with some devices you can
 enter the value of R<sub>L</sub> , and the device changes V<sub>S</sub> accordingly to deliver
 the requested V<sub>out</sub> .

Parent topic:

Waveform Fundamentals

<!--NI_TOPIC bundle=ni-fgen path=output-modes.html language=enus -->
## TOPIC 00814: Output Modes

- bundle_id: `ni-fgen`
- source_path: `output-modes.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/output-modes.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The output mode of your signal generator determines the type of waveforms your signal generator produces. To select an output mode, set the Output Mode parameter of the niFgen Configure Output Mode VI or the outputMode parameter of the niFgen_ConfigureOutputMode function.

### Output Modes

The output mode of your signal generator determines the type of waveforms
 your signal generator produces. To select an output mode, set the
 Output Mode parameter of the niFgen Configure Output
 Mode VI or the outputMode parameter of the
 niFgen_ConfigureOutputMode function.

Parent topic:

Waveform Fundamentals

<!--NI_TOPIC bundle=ni-fgen path=pci-chassis-cooling.html language=enus -->
## TOPIC 00815: PCI Chassis Cooling

- bundle_id: `ni-fgen`
- source_path: `pci-chassis-cooling.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/pci-chassis-cooling.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Not all PCI chassis provide the same cooling, when selecting a PCI chassis, consideration should be given to providing adequate airflow for high power and sensitive devices such as NI PCI signal generators. NI PCI signal generators are high-precision instruments and may be sensitive to interference

### PCI Chassis Cooling

Not all PCI chassis provide the same cooling, when
selecting a PCI chassis, consideration should be given to providing
adequate airflow for high power and sensitive devices such as
NI PCI signal generators.

NI PCI signal generators are high-precision
instruments and may be sensitive to interference from other
electronic devices. To optimize the accuracy and performance of the
device, you may need to locate the device in a slot away from
devices with power supplies and other noisy circuitry. The device
may also be sensitive to heat generated by high-power products in
neighboring slots. When possible, consider locating the device away
from high-power devices to optimize cooling.

Parent topic:

PCI Systems

<!--NI_TOPIC bundle=ni-fgen path=pci-systems.html language=enus -->
## TOPIC 00816: PCI Systems

- bundle_id: `ni-fgen`
- source_path: `pci-systems.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/pci-systems.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Expand this topic for information about using PCI systems with your NI signal generator.

### PCI Systems

Expand this topic for information about using PCI systems with your NI signal generator.

Parent topic:

Integration and System Considerations

<!--NI_TOPIC bundle=ni-fgen path=peer-to-peer-data-streaming.html language=enus -->
## TOPIC 00817: Peer-to-Peer Data Streaming

- bundle_id: `ni-fgen`
- source_path: `peer-to-peer-data-streaming.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/peer-to-peer-data-streaming.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXIe-5450 module revision C and later only and the NI PXIe-5451 support peer-to-peer (P2P) data streaming using the NI-P2P API. Peer-to-peer streaming exchanges data directly between supported devices, bypassing the host computer memory and making applications that require real-time data tran

### Peer-to-Peer Data Streaming

The NI PXIe-5450 module revision C and later only and the NI PXIe-5451 support peer-to-peer (P2P) data streaming using the NI-P2P API. Peer-to-peer streaming exchanges data directly between supported devices, bypassing the host computer memory and making applications that require real-time data transfer between devices possible.

For more information about using NI-P2P to stream data between devices, refer to the NI Peer-to-Peer Streaming Help. The NI-FGEN C Function Reference and the *NI-FGEN LabVIEW Reference* provide more information about configuring the signal generator endpoint resources.

For more information about the following terms, refer to the Understanding the Peer-to-Peer Data Streaming Architecture topic in the NI Peer To Peer Streaming Help.

- Stream—The data path connection between two peer-to-peer endpoints. A peer-to-peer stream is independent of the data generation and consumption of the two peers.
- Endpoint—The collection of hardware resources needed to support one end of a peer-to-peer stream. Multiple peer-to-peer endpoints may exist in a single device.
- Writer Peer—The peer that sends the data over the bus to the reader peer.
- Reader Peer—The peer that receives the data over the bus from the writer peer.

Signal generators take the role of the reader peer endpoint in a peer-to-peer stream because they read data from the writer peer using the peer-to-peer stream and then generate it to physical channels.

Parent topic:

Features

<!--NI_TOPIC bundle=ni-fgen path=peer-to-peer-streaming-properties-attributes.html language=enus -->
## TOPIC 00818: Peer-to-Peer Streaming Properties/Attributes

- bundle_id: `ni-fgen`
- source_path: `peer-to-peer-streaming-properties-attributes.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/peer-to-peer-streaming-properties-attributes.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the following properties and attributes to configure a peer-to-peer streaming session. LabVIEWC/C++P2P EnabledNIFGEN_ATTR_P2P_ENABLED Destination ChannelsNIFGEN_ATTR_P2P_DESTINATION_CHANNELS Endpoint SizeNIFGEN_ATTR_P2P_ENDPOINT_SIZESpace Available In Endpoint NIFGEN_ATTR_P2P_SPACE_AVAILABLE_IN_

### Peer-to-Peer Streaming Properties/Attributes

Use the following properties and attributes to configure a peer-to-peer streaming session.

| LabVIEW | C/C++ |
| --- | --- |
| P2P Enabled | NIFGEN_ATTR_P2P_ENABLED |
| Destination Channels | NIFGEN_ATTR_P2P_DESTINATION_CHANNELS |
| Endpoint Size | NIFGEN_ATTR_P2P_ENDPOINT_SIZE |
| Space Available In Endpoint | NIFGEN_ATTR_P2P_SPACE_AVAILABLE_IN_ENDPOINT |
| Most Space Available In Endpoint | NIFGEN_ATTR_P2P_MOST_SPACE_AVAILABLE_IN_ENDPOINT |
| Endpoint Count | NIFGEN_ATTR_P2P_ENDPOINT_COUNT |
| Data Transfer Permission Interval | NIFGEN_ATTR_P2P_DATA_TRANSFER_PERMISSION_INTERVAL |
| Data Transfer Permission Initial Credits | NIFGEN_ATTR_P2P_DATA_TRANSFER_PERMISSION_INITIAL_CREDITS |
| P2P Endpoint Fullness Start Trigger Level | NIFGEN_ATTR_P2P_ENDPOINT_FULLNESS_START_TRIGGER_LEVEL |

Parent topic:

Peer-to-Peer Data Streaming

<!--NI_TOPIC bundle=ni-fgen path=peer-to-peer-streaming-vis-functions.html language=enus -->
## TOPIC 00819: Peer-to-Peer Streaming VIs/Functions

- bundle_id: `ni-fgen`
- source_path: `peer-to-peer-streaming-vis-functions.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/peer-to-peer-streaming-vis-functions.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following table shows the VIs and functions that are used for creating a peer-to-peer streaming operation. LabVIEW C/C++Streaming Session—Use the following NI-P2P VI to configure a peer-to-peer streaming session.niFgen Get Stream Endpoint Handle VIniFgen_GetStreamEndpointHandle functionP2P Endpo

### Peer-to-Peer Streaming VIs/Functions

The following table shows the VIs and functions that are used for creating a peer-to-peer streaming operation.

| LabVIEW | C/C++ |
| --- | --- |
| Streaming Session—Use the following NI-P2P VI to configure a peer-to-peer streaming session. |  |
| niFgen Get Stream Endpoint Handle VI | niFgen_GetStreamEndpointHandle function |
| P2P Endpoint Fullness Start Trigger—Use the following VI/function to configure the signal generator to begin generation when the peer-to-peer endpoint receives a specified number of samples from the writer peer to avoid underflow at start. |  |
| niFgen Configure P2P Endpoint Fullness Start Trigger VI | niFgen_ConfigureP2PEndpointFullnessStartTrigger function |
| Write P2P Endpoint—Use the following VI/function to write initial data to the endpoint before starting generation to avoid underflow at start. |  |
| niFgen Write P2P Endpoint I16 VI | niFgen_WriteP2PEndpointI16 function |

Parent topic:

Peer-to-Peer Data Streaming

<!--NI_TOPIC bundle=ni-fgen path=pfi-lines.html language=enus -->
## TOPIC 00820: PFI Lines

- bundle_id: `ni-fgen`
- source_path: `pfi-lines.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/pfi-lines.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: PFI lines are multipurpose programmable function input/outputs. These lines serve as connections to virtually all internal timing signals. The PFI lines of NI signal generators can accept or generate a trigger, generate a marker, accept or generate a reference clock. The function of each PFI line is

### PFI Lines

PFI lines are multipurpose programmable function input/outputs. These lines serve as connections
 to virtually all internal timing signals. The PFI lines of NI signal generators can
 accept or generate a trigger, generate a marker, accept or generate a reference clock.
 The function of each PFI line is independent.

If you are using LabVIEW to program your signal generator and you want to connect external signal
 generators to the PFI lines, you can use the niFgen Configure Sample Clock
 Source VI, the niFgen Configure Reference Clock VI, or
 the niFgen Configure Trigger VI to route external signals to internal
 sources. You can use the niFgen Export Signal VI to route internal
 signals to the PFI lines on the front panel.

niFgen_ConfigureSampleClockSource

niFgen_ConfigureReferenceClock

niFgen_ConfigureTriggerSource

niFgen_ExportSignal

Notice

Parent topic:

PXI/PXI Express Systems

<!--NI_TOPIC bundle=ni-fgen path=pfi-lines_2.html language=enus -->
## TOPIC 00821: PFI Lines

- bundle_id: `ni-fgen`
- source_path: `pfi-lines_2.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/pfi-lines_2.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: PFI lines are multipurpose programmable function input/outputs. These lines serve as connections to virtually all internal timing signals. The PFI lines of NI signal generators can accept or generate a trigger, generate a marker, accept or generate a reference clock. The function of each PFI line is

### PFI Lines

PFI lines are multipurpose programmable function input/outputs. These lines serve as connections
 to virtually all internal timing signals. The PFI lines of NI signal generators can
 accept or generate a trigger, generate a marker, accept or generate a reference clock.
 The function of each PFI line is independent.

If you are using LabVIEW to program your signal generator and you want to connect external signal
 generators to the PFI lines, you can use the niFgen Configure Sample Clock
 Source VI, the niFgen Configure Reference Clock VI, or
 the niFgen Configure Trigger VI to route external signals to internal
 sources. You can use the niFgen Export Signal VI to route internal
 signals to the PFI lines on the front panel.

niFgen_ConfigureSampleClockSource

niFgen_ConfigureReferenceClock

niFgen_ConfigureTriggerSource

niFgen_ExportSignal

Notice

Parent topic:

PCI Systems

<!--NI_TOPIC bundle=ni-fgen path=phase-locked-looping.html language=enus -->
## TOPIC 00822: Phase-Locked Loop

- bundle_id: `ni-fgen`
- source_path: `phase-locked-looping.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/phase-locked-looping.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: A phase-locked loop (PLL) is a circuit that adjusts a main clock to synchronize to a reference clock. The frequency stability of the sample clock timebase matches that of the reference clock when the two are phase-locked. Phase locking also synchronizes clocks of multiple instruments that are phase-

### Phase-Locked Loop

A *phase-locked loop (PLL)* is a circuit that adjusts a main clock to synchronize to a
 reference clock. The frequency stability of the sample clock timebase matches that of
 the reference clock when the two are phase-locked. Phase locking also synchronizes
 clocks of multiple instruments that are phase-locked to the same reference clock.

Figure 1.

[IMAGE alt='image' src='GUID-6E63FDB0-2B47-4433-8066-C6C6426D723A-a5.gif']

The operation of this circuit is typical of all PLLs. A PLL is a feedback control system that
 controls the phase of a voltage-controlled oscillator (VCO). The frequency reference
 signal is applied to a phase detector. The output of the VCO connects to the other
 input. Normally the frequencies of both signals are almost the same. The output of the
 phase detector has a voltage proportional to the phase difference between the two input
 signals. The loop filter receives this signal from the phase detector. The loop filter
 determines the dynamic characteristics of the PLL.

Parent topic:

Waveform Fundamentals

<!--NI_TOPIC bundle=ni-fgen path=programming-state-model.html language=enus -->
## TOPIC 00823: Programming State Model

- bundle_id: `ni-fgen`
- source_path: `programming-state-model.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/programming-state-model.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: In this topic, the word "property," when not referring to a specific property, refers to both properties in LabVIEW and attributes in C or LabWindows/CVI. The NI-FGEN programming model has three main states: Idle, Committed, and Generating, as shown in the following figure. Idle—You can program all

### Programming State Model

In this topic, the word "property," when not
referring to a specific property, refers to both properties in
LabVIEW and attributes in C or LabWindows/CVI.

The NI-FGEN programming model has three main
states: Idle, Committed, and Generating, as shown in the following
figure.

[IMAGE alt='image' src='GUID-1A3DB93E-4365-40FC-9B85-01F1E43DE5F4-a5.gif']

Idle—You can program all session properties
in the Idle state. However, when in the Idle state, the properties
may not have been applied to the device yet, so the device hardware
configuration may not match the session property values–the
device remains configured as it was the last time a session was
committed. If the computer has just been reset or the 
niFgen Reset
Device VI or the 
niFgen_ResetDevice function has just been called, the device is in the default
hardware state. This means the device is not generating a waveform,
although, depending on the previous state, a constant DC voltage
from the last waveform sample generated on the output connector may
be present.

Committed—All of the session properties are
applied to the device when the session enters the Committed state.
In the Committed state, waveforms and sequences can be loaded into
onboard memory. If any properties are changed, the session
implicitly transitions back to idle, and the hardware configuration
still reflects the previously committed properties. Calling the 
niFgen Commit VI or
the 
niFgen_Commit function from the Idle state verifies all properties,
configures the device, and transitions to the Committed state.

Generating—In the Generating state, session
properties always reflect the current state of the device, and the
device is either waiting on a trigger or generating a signal.
Dynamic properties, such as the 
Arbitrary
Waveform Gain property or the 
NIFGEN_ATTR_ARB_GAIN attribute and the 
Arbitrary
Waveform Offset property or the 
NIFGEN_ATTR_ARB_OFFSET attribute, are applied to the device immediately if set while
the session is in the Generating state.

The following actions or settings cause a
transition from one state to another:

- Calling the 
niFgen
Initiate Generation VI or the 
 niFgen_InitiateGeneration function in the Idle state causes a transition to the
Generating state.
- Calling the 
niFgen Commit VI or
the 
 niFgen_Commit function in the Idle state causes a transition to the
Committed state.
- Calling a create or write waveform VI or function in the Idle
state causes a transition to the Committed state.
- Calling the 
niFgen
Create Arbitrary Sequence VI or the 
 niFgen_CreateArbSequence 
function, or the 
niFgen
Create Advanced Arb Sequence VI or the 
 niFgen_CreateAdvancedArbSequence function in the Idle state causes a transition to the
Committed state.
- Changing any property in the Committed state causes a
transition to the Idle state.
- Changing a property that is not dynamic in the Generating state
returns an error, but does not transition out of the Generating
state.
- Calling the 
niFgen Abort
Generation VI or the 
 niFgen_AbortGeneration function in the Generating state causes a transition to the
Committed state.
- Calling the 
niFgen Close VI or
the 
 niFgen_close function from any state closes the NI-FGEN session and
transitions to the close state. If the session is in the Generating
state, the generation is aborted first.
- Calling the 
niFgen Reset VI or
the 
 niFgen_reset function from any state causes a transition to the Idle state.
If the session is in the Generating state, the generation is
aborted first.

Parent topic:

Programming

<!--NI_TOPIC bundle=ni-fgen path=programming.html language=enus -->
## TOPIC 00824: Programming

- bundle_id: `ni-fgen`
- source_path: `programming.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/programming.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Review the following topics for information about programming with NI-FGEN and NI Composite Video Generator.

### Programming

Review the following topics for information about programming with NI-FGEN and NI Composite Video
 Generator.

- [Programming State Model](programming-state-model.html)
- [General Programming Flow](general-programming-flow.html)
- [Creating an Application with NI-FGEN and Your ADE](creating-application-with-ni-fgen.html) Learn how to use NI-FGEN with your application development environment (ADE). Locate files that you need to include in your application.
- [NI-FGEN Tutorial](ni-fgen-tutorial.html)
- [Features](features.html)
- [Scripting Instructions](scripting-instructions.html) Learn about core scripting instructions and the structure of scripts.
- [Using the Standard Functionality for error in Parameters](using-the-standard-functionality-for-error-in.html)
- [Using the Standard Functionality for error out Parameters](using-the-standard-functionality-for-error-ou.html)
- [How the NI Video Software Toolkit Filters Video Components](how-the-ni-video-software-toolkit-filters-vid.html)

<!--NI_TOPIC bundle=ni-fgen path=pxi-express-bandwidth-considerations.html language=enus -->
## TOPIC 00825: PXI Express Bandwidth Considerations

- bundle_id: `ni-fgen`
- source_path: `pxi-express-bandwidth-considerations.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/pxi-express-bandwidth-considerations.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: NI PXI Express signal generators use PCI Express as the interface to the computer. The physical connection between a PXI Express signal generator and a computer is called a PCI Express link. When a signal generator generates a waveform, it can saturate this link. Saturation occurs when the signal ge

### PXI Express Bandwidth Considerations

NI PXI Express signal generators use PCI Express as the interface to the computer. The physical
 connection between a PXI Express signal generator and a computer is called a
 PCI Express link. When a signal generator generates a waveform,
 it can saturate this link. Saturation occurs when the signal generator is copying data
 to its onboard memory from computer memory as rapidly as possible, utilizing all of the
 bandwidth of the PCI Express link.

The theoretical bandwidth of the onboard memory of the signal generator is 3.2 GB/s, and the theoretical bandwidth of the PCIe link is approximately 850 MB/s. This difference in bandwidths means that transferring data to the onboard memory can saturate the PCI Express link. The waveform data download rate is dependent on the system configuration, with a maximum of approximately 600 MB/s.

High-speed transfers that saturate the PCI Express link can affect other devices when multiple
 devices share a single PCI Express link. For example, if an NI PXI Express signal
 generator is installed in slot 9 of an NI PXIe-1065 chassis controlled by an NI
 PXIe-8130 controller, the signal generator will share bandwidth with any devices
 installed in slots 10 through 14. This bandwidth sharing becomes a problem if other
 devices in the application require guaranteed bandwidth to the PCI Express bus.

You can configure the NI PXI Express signal generator to limit its use of the PCI Express bus,
 leaving bandwidth for other devices that are more susceptible to short-term bursts of
 traffic on a shared PCI Express link. You can also improve the performance of your
 device based on your system configuration. The following table lists the properties and
 attributes that allow you to modify the way that the signal generator uses the PXI
 Express bus.

| LabVIEW Property | C/C++ Attribute | Purpose |
| --- | --- | --- |
| Maximum Bandwidth | NIFGEN_ATTR_DATA_TRANSFER_MAXIMUM_BANDWIDTH | Allows you to optimize bus bandwidth usage for multi-device streaming applications. |
| Maximum In-Flight Read Requests | NIFGEN_ATTR_DATA_TRANSFER_MAXIMUM_IN_FLIGHT_READ_REQUESTS | Allows you to specify, based on the requirements of your application, the maximum number of in-flight read requests for data transfers. |
| Preferred Packet Size | NIFGEN_ATTR_DATA_TRANSFER_PREFERRED_PACKET_SIZE | Allows you to configure, based on the requirements of your system, the preferred size of the data field in the PCI Express data transfer packet. |

Parent topic:

Streaming

<!--NI_TOPIC bundle=ni-fgen path=pxi-express-modules.html language=enus -->
## TOPIC 00826: PXI Express Modules

- bundle_id: `ni-fgen`
- source_path: `pxi-express-modules.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/pxi-express-modules.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The PXI Express Specification integrates PCI Express signaling into the PXI standard, which increases backplane bandwidth and enhancing PXI timing and synchronization features while maintaining backward compatibility with PXI. NI Signal Generators Available as PXI Express Modules The NI 5442/5450/54

### PXI Express Modules

The PXI Express Specification integrates PCI
Express signaling into the PXI standard, which increases backplane
bandwidth and enhancing PXI timing and synchronization features
while maintaining backward compatibility with PXI.

[IMAGE alt='image' src='GUID-A07E5A59-A097-431F-80EC-CC9EC4C3553D-a5.gif']

#### NI Signal Generators Available as PXI Express Modules

The NI 5442/5450/5451 and PXIe-5413/5423/5433 arbitrary waveform generators are
available in the PXI Express form factor.

#### Chassis Guidelines

NI PXI Express signal generators can be installed
in the following PXI Express chassis slots:

- PXI hybrid slots —Accepts either PXI modules
that are hybrid slot-compatible or PXI Express modules
- PXI Express slots —Accepts PXI Express
modules

Note

#### Using PXI Express Products with CompactPCI Express
Products

The CompactPCI/PXI Express backplane integrates PCI
Express while still preserving compatibility with current PXI
modules. PXI Express hybrid slots are capable of delivering signals
for both PCI and PCI Express. Thus, the hybrid slot allows you to
install a PXI module that uses PCI signaling or a PXI Express
module that uses PCI Express signaling.

#### Related Web Topics

For an overview of the PXI Express specification,
refer to 
PXI Express Specification
Tutorial

Parent topic:

Modules

<!--NI_TOPIC bundle=ni-fgen path=pxi-modules.html language=enus -->
## TOPIC 00827: PXI Modules

- bundle_id: `ni-fgen`
- source_path: `pxi-modules.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/pxi-modules.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: PCI eXtensions for Instrumentation (PXI) modular instrumentation delivers a PC-based, standardized, high-performance measurement and automation system. PXI combines the high-speed PCI bus with integrated timing and triggering designed specifically for measurement and automation applications to deliv

### PXI Modules

PCI eXtensions for Instrumentation (PXI) modular
instrumentation delivers a PC-based, standardized, high-performance
measurement and automation system. PXI combines the high-speed PCI
bus with integrated timing and triggering designed specifically for
measurement and automation applications to deliver significant
performance improvements over older architectures. The following
figure shows a typical PXI chassis installation.

[IMAGE alt='image' src='GUID-46A6033F-87FA-406E-BECA-9041FC8CC96E-a5.gif']

#### NI Signal Generators Available as PXI Modules

The NI 5402/5404/5406/5412/5421/5422/5441 signal
generators are available in the PXI form factor.

#### Chassis Guidelines

NI PXI signal generators can be installed in the
following chassis and slots:

- PXI chassis —PXI signal generators can be
installed in any peripheral slot of a PXI chassis.
- PXI-Express chassis —PXI signal generators
can be installed in the following PXI Express chassis slots:
- PXI-1 slots —Accepts PXI modules
- PXI hybrid slots —Accepts either PXI modules
that are hybrid slot-compatible or PXI Express modules

#### Using PXI-Compatible Products with Standard CompactPCI
Products

The ability to use PXI-compatible products with
standard CompactPCI products is an important feature provided by
the 
PXI Specification, revision 2.1. If you use a
PXI-compatible plug-in device in a standard CompactPCI chassis, you
cannot use PXI-specific functions, but you can still use the basic
plug-in device functions. For example, the PXI trigger bus on
NI signal generators is available in a PXI chassis but not in
a CompactPCI chassis. The CompactPCI specification permits vendors
to develop sub-buses that co-exist with the basic PCI interface on
the CompactPCI bus. Compatible operation is not guaranteed between
CompactPCI devices with different sub-buses nor between CompactPCI
devices with sub-buses and PXI. The standard implementation for
CompactPCI does not include these sub-buses. NI signal
generators work in any standard CompactPCI chassis. PXI-specific
features, such as PXI_Trig bus and PXI_CLK10 reference are
implemented on the J2 connector of the CompactPCI bus.

#### Related Topics

*PXI Star Trigger
Line*

#### Related Web Topics

For an overview of the PXI Specification, refer to PXI Specification
Tutorial

For an overview of PXI-specific functions, refer to How do National Instruments
PXI Boards map to the PXI Backplane?

Parent topic:

Modules

Related concepts:

- PXI Star Trigger Line

<!--NI_TOPIC bundle=ni-fgen path=pxi-pxi-express-chassis-cooling.html language=enus -->
## TOPIC 00828: PXI/PXI Express Chassis Cooling

- bundle_id: `ni-fgen`
- source_path: `pxi-pxi-express-chassis-cooling.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/pxi-pxi-express-chassis-cooling.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Not all PXI or PXI Express chassis provide the same cooling. When selecting a PXI or PXI Express chassis, consideration should be given to providing adequate airflow for high power and sensitive devices such as NI signal generators. NI PXI and PXI Express signal generators are high-precision instrum

### PXI/PXI Express Chassis Cooling

Not all PXI or PXI Express chassis provide the same
cooling. When selecting a PXI or PXI Express chassis, consideration
should be given to providing adequate airflow for high power and
sensitive devices such as NI signal generators.

NI PXI and PXI Express signal generators are
high-precision instruments and may be sensitive to interference
from other electronic devices. To optimize the accuracy and
performance of the device, you may need to locate the device in a
slot away from devices with power supplies and other noisy
circuitry. The device may also be sensitive to heat generated by
high-power products in neighboring slots. When possible, consider
locating the device away from high-power devices to optimize
cooling.

Parent topic:

PXI/PXI Express Systems

<!--NI_TOPIC bundle=ni-fgen path=pxi-pxi-express-systems.html language=enus -->
## TOPIC 00829: PXI/PXI Express Systems

- bundle_id: `ni-fgen`
- source_path: `pxi-pxi-express-systems.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/pxi-pxi-express-systems.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Expand this topic for information about using PXI and PXI Express systems with your NI signal generator.

### PXI/PXI Express Systems

Expand this topic for information about using PXI and PXI Express systems with your NI signal generator.

Parent topic:

Integration and System Considerations

<!--NI_TOPIC bundle=ni-fgen path=pxi-star-trigger-line.html language=enus -->
## TOPIC 00830: PXI Star Trigger Line

- bundle_id: `ni-fgen`
- source_path: `pxi-star-trigger-line.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/pxi-star-trigger-line.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The PXI star trigger is a feature implemented on National Instruments PXI chassis. PXI chassis have a PXI trigger bus that is linked to all slots in the chassis. In addition, PXI chassis have a PXI star trigger that is linked to the system timing slot (Slot 2 on PXI chassis). The PXI star trigger is

### PXI Star Trigger Line

The PXI star trigger is a feature implemented on
National Instruments PXI chassis. PXI chassis have a PXI trigger
bus that is linked to all slots in the chassis. In addition, PXI
chassis have a PXI star trigger that is linked to the system timing
slot (Slot 2 on PXI chassis). The PXI star trigger is a
high-performance trigger signal that you can use to synchronize all
the devices in a chassis. You can also do this using the normal PXI
trigger bus, but the PXI star trigger offers increased performance,
specifically a propagation delay of no more than 5 ns and skew
of no more than 1 ns.

[IMAGE alt='image' src='GUID-0F93896A-6F97-4B7B-BB00-802CA0CCA4DC-a5.gif']

The PXI star trigger lines allow a PXI star
controller in Slot 2 to route signals to or from other peripheral
slots with very low skew and at higher bandwidth than other PXI
trigger lines.

When not using PXI star, you can use Slot 2 as a
standard peripheral slot. However, when using PXI star, you must
have a PXI star controller, (master) device in Slot 2, and one or
more peripheral devices in the other slots.

If placed in a peripheral slot—Slot 3 or
higher—all NI PXI signal generators can receive a signal
from PXI star.

Note

#### Related Topics

*PXI Modules*

Parent topic:

PXI/PXI Express Systems

Related concepts:

- PXI Modules

<!--NI_TOPIC bundle=ni-fgen path=pxi-trigger-lines.html language=enus -->
## TOPIC 00831: PXI Trigger Lines

- bundle_id: `ni-fgen`
- source_path: `pxi-trigger-lines.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/pxi-trigger-lines.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Eight PXI bus trigger lines are highly flexible and can be used in a variety of ways. For example, triggers can be used to synchronize the operation of several different PXI peripheral devices. In other applications, one device can control carefully timed sequences of operations performed on other d

### PXI Trigger Lines

Eight PXI bus trigger lines are highly flexible and
can be used in a variety of ways. For example, triggers can be used
to synchronize the operation of several different PXI peripheral
devices. In other applications, one device can control carefully
timed sequences of operations performed on other devices in the
system. Triggers may be passed from one device to another, allowing
precisely timed responses to asynchronous external events that are
being monitored or controlled. The number of triggers that a
particular application requires varies with the complexity and
number of events involved.

[IMAGE alt='image' src='GUID-EC6AF675-EC47-4106-BBC0-93D90C4CCB69-a5.gif']

The PXI Specification is implemented with the RTSI
bus through the PXI trigger lines. PXI Specification requires eight
lines, PXI_Trig<0..7>, on the P2/J2 connector of the PXI
chassis for the trigger lines. The RTSI features of NI signal
generators is implemented on this sub-bus. The RTSI triggers
<0..6> are implemented on PXI_Trig<0..6>, and the RTSI
clock is routed on PXI_Trig7.

For an overview of PXI-specific functions, refer to *How do NI PXI Boards map to the PXI
 Backplane?*

#### Related Topics

*PXI Star Trigger*

Parent topic:

PXI/PXI Express Systems

Related concepts:

- PXI Star Trigger Line

<!--NI_TOPIC bundle=ni-fgen path=reconfiguring-a-stream.html language=enus -->
## TOPIC 00832: Reconfiguring a Stream

- bundle_id: `ni-fgen`
- source_path: `reconfiguring-a-stream.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/reconfiguring-a-stream.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Consider the following scenarios when reconfiguring an NI-FGEN session for peer-to-peer data streaming. If the generation from the previous session completed with a Done Notification, the stream remains linked, but it is disabled. If using the P2P Endpoint Fullness Start Trigger property or the NIFG

### Reconfiguring a Stream

Consider the following scenarios when reconfiguring an NI-FGEN session for peer-to-peer data streaming.

- If the generation from the previous session completed with a Done Notification, the stream remains linked, but it is disabled. If using the P2P Endpoint Fullness Start Trigger property or the NIFGEN_ATTR_P2P_ENDPOINT_FULLNESS_START_TRIGGER_LEVEL attribute, re-enable the stream using the P2P Enabled property or NIFGEN_ATTR_P2P_ENABLED attribute and initiate generation.
If priming from the host using the niFgen Write P2P Endpoint I16 VI or niFgen_WriteP2PEndpointI16 , write to the endpoint again to prime it with data before re-enabling the stream and initiating generation. For the manual start generation method, ensure that the writer peer writes to the signal generator endpoint prior to calling the niFgen Initiate Generation VI or niFgen_InitiateGeneration function.
- If the previous session was aborted, the stream is disabled and you can simply re-enable the stream to perform subsequent generations.

Parent topic:

Configuring a Peer-to-Peer Stream

<!--NI_TOPIC bundle=ni-fgen path=repeatend-repeat.html language=enus -->
## TOPIC 00833: repeat/end repeat

- bundle_id: `ni-fgen`
- source_path: `repeatend-repeat.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/repeatend-repeat.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the repeat/end repeat instruction to describe how to loop sections of a script until a particular condition is met. Usage Execute a set of instructions n times.repeat <n> <instructions> end repeat Execute a set of instructions until the device receives a Script trigger.repeat until scriptTrigger

### repeat/end
 repeat

Use the repeat/end repeat instruction to
 describe how to loop sections of a script until a particular condition is met.

#### Usage

- Execute a set of instructions n
 times. repeat <n>
 <instructions>
end repeat
- Execute a set of instructions until the device receives a Script
 trigger. repeat until scriptTrigger0
 <instructions>
end repeat Upon receiving the Script trigger, a device completes all
 instructions still in the repeat until loop before proceeding.
 Therefore, receiving the Script trigger does not immediately exit the repeat
 loop.
- Execute a set of instructions until the abortion of the generation operation using the
 Abort VI or function for your
 driver. repeat forever
 <instructions>
end repeat
- Nest repeat <N> or repeat
 until instructions inside a repeat forever 
 instruction. repeat forever
 <instructions>
 repeat <N>
 <instructions>
 end repeat
 <instructions>
end repeat repeat forever
 <instructions>
 repeat until scripttrigger0
 <instructions>
 end repeat
 <instructions>
end repeat Note You can nest
 repeat <N> and repeat until
 instructions, one level deep, inside a repeat forever instruction. You
 can use the if/else/end if instruction inside a repeat
 forever instruction. You cannot use the if/else/end if
 instruction inside of the repeat <N> and the
 repeat until instructions. You cannot use other nesting, such as
 repeat <N> inside another repeat
 <N>.

#### repeat/end
 repeat Examples

- Generate myWfmA followed by myWfmB five
 times. repeat 5
 generate myWfmA
 generate myWfmB
end repeat
- Generate the sequence myWfmA , myWfmB ,
 myWfmC until the device receives a Script
 trigger. repeat until scripttrigger0
 generate myWfmA
 generate myWfmB
 generate myWfmC
end repeat
- Generate myWfmA forever until aborting the
 operation. repeat forever
 generate myWfmA
end repeat
- Continuously generate the following sequence: repeat forever
 generate initialWfm
 repeat 1000
 generate myWfmA
 generate myWfmB
 generate myWfmC
 end repeat
 generate myWfmD
end repeat
  - initialWfm once
  - myWfmA , myWfmB , myWfmC 1000
 times
  - myWfmD once
- Switch between two waveforms the device receives a Script trigger until aborting the
 operation. repeat forever
 repeat until scripttrigger0
 generate myWfmA
 end repeat
 repeat until scripttrigger0
 generate myWfmB
 end repeat
end repeat

Parent topic:

Scripting Instructions

<!--NI_TOPIC bundle=ni-fgen path=rtsi-bus.html language=enus -->
## TOPIC 00834: RTSI Bus

- bundle_id: `ni-fgen`
- source_path: `rtsi-bus.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/rtsi-bus.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: RTSI stands for Real-Time System Integration. It is a bus found on many National Instruments devices that, when cabled together with a RTSI cable, is used to share and exchange timing and control signals between multiple boards. It is usually used for synchronization purposes. The previous figure sh

### RTSI Bus

RTSI stands for Real-Time System Integration. It is
a bus found on many National Instruments devices that, when cabled
together with a RTSI cable, is used to share and exchange timing
and control signals between multiple boards. It is usually used for
synchronization purposes.

[IMAGE alt='image' src='GUID-5333D370-87A2-4787-BF59-D54C67CD64DF-a5.gif']

The previous figure shows an example of an extended
five-board cable setup.

The RTSI bus cables are short, 34-conductor ribbon
cables equipped with two to five connectors to link together a
group of boards. The cable options include connections for two,
three, four, and five boards, plus an extended cable length to
connect up to five long and short boards.

Parent topic:

PCI Systems

<!--NI_TOPIC bundle=ni-fgen path=sample-rate.html language=enus -->
## TOPIC 00835: Sample Rate

- bundle_id: `ni-fgen`
- source_path: `sample-rate.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/sample-rate.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Sample rate is the rate at which digital data is transferred from the memory to the digital-to-analog converter (DAC). According to Shannon’s Sampling theorem, a digital waveform must be updated at least twice as fast as the bandwidth of the signal to be accurately generated. Ideally, a sample rate

### Sample Rate

Sample rate is the rate at which digital data is transferred from the memory to the digital-to-analog converter (DAC). According to *Shannon’s Sampling theorem*, a digital waveform must be updated at least twice as fast as the bandwidth of the signal to be accurately generated. Ideally, a sample rate many times greater than the frequency of the signal produces accurate waveforms. A higher sample rate also captures more waveform details. The following figure illustrates a 1 MHz sine wave generated by a sampled 2 MS/s DAC and a 20 MS/s DAC. The faster DAC generates 20 points per cycle of the expected signal compared with 2 points per cycle with the slower DAC. In this example, the higher sample rate more accurately defines the waveform shape.

[IMAGE alt='image' src='GUID-A322214E-BB65-4A5A-8999-5A916E64BCC6-a5.gif']

Parent topic:

Waveform Fundamentals

Related concepts:

- Nyquist and Shannon's Sampling Theorems

<!--NI_TOPIC bundle=ni-fgen path=scanning-speed.html language=enus -->
## TOPIC 00836: Scanning Speed

- bundle_id: `ni-fgen`
- source_path: `scanning-speed.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/scanning-speed.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The scanning speed is the number of video frames generated per second. The scanning speed and the number of lines per frame depend on the video format. The prefix M in the M-NTSC and M-PAL formats refers to a scanning speed of approximately 30 frames per second and a scanning system of 525 lines per

### Scanning Speed

The scanning speed is the number of video frames generated per second. The scanning speed and the number of lines per frame depend on the video format. The prefix M in the M-NTSC and M-PAL formats refers to a scanning speed of approximately 30 frames per second and a scanning system of 525 lines per complete frame. All other formats specify a rate of 25 frames per second and 625 lines per frame.

Parent topic:

Video Signal Fundamentals

<!--NI_TOPIC bundle=ni-fgen path=script-mode.html language=enus -->
## TOPIC 00837: Script Mode

- bundle_id: `ni-fgen`
- source_path: `script-mode.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/script-mode.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Script mode allows you to use scripting to link and loop multiple waveforms in complex combinations using a script. A script is a series of instructions that indicates how waveforms saved in the onboard memory should be sent to the DUT. The script can specify the order of the generated waveforms, th

### Script Mode

Script mode allows you to use scripting to link and loop multiple
 waveforms in complex combinations using a script. A *script*
 is a series of instructions that indicates how waveforms saved in the onboard memory
 should be sent to the DUT. The script can specify the order of the generated waveforms,
 the number of times they are generated, and the triggers and markers associated with the
 generation.

Parent topic:

Output Modes

Related concepts:

- Configure Script Mode
- Scripting Instructions

<!--NI_TOPIC bundle=ni-fgen path=scriptend-script.html language=enus -->
## TOPIC 00838: script/end script

- bundle_id: `ni-fgen`
- source_path: `scriptend-script.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/scriptend-script.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the script/end script statement to define a set of instructions and also assign a name to that script. UsageScript names must be unique. Script names cannot have the same name as a waveform name.script <script name> <instructions> end script Create a simple script named myScript to generate myWf

### script/end script

Use the script/end script statement to define a set of instructions
 and also assign a name to that script.

#### Usage

Script names must be
 unique. Script names cannot have the same name as a waveform
 name.

```text
script <script name>
  <instructions>
end script
```

#### Create a simple script named myScript to generate
 myWfm

```text
script myScript
  generate myWfm
end script
```

#### Create multiple scripts named myScript1 &
 myScript2

```text
script myScript1
  generate myWfmA
end script

script myScript2
  generate myWfmB
end script
```

Parent topic:

Scripting Instructions

<!--NI_TOPIC bundle=ni-fgen path=scripting-instructions.html language=enus -->
## TOPIC 00839: Scripting Instructions

- bundle_id: `ni-fgen`
- source_path: `scripting-instructions.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/scripting-instructions.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Learn about core scripting instructions and the structure of scripts. Scripts consist of following eight primary instructions: script/end script generate repeat/end repeat if/else/end if break wait clear stream n Additionally, the keywords script <script name>/end script surround all instructions in

### Scripting Instructions

Learn about core scripting instructions and the structure of scripts.

- script/end script
- generate
- repeat/end repeat
- if/else/end if
- break
- wait
- clear
- stream n

<script name>

- [script/end script](scriptend-script.html) Use the script/end script statement to define a set of instructions and also assign a name to that script.
- [generate](generate.html) Use the generate instruction to describe which waveform to generate.
- [repeat/end repeat](repeatend-repeat.html) Use the repeat/end repeat instruction to describe how to loop sections of a script until a particular condition is met.
- [if/else/end if](ifelseend-if.html) Use the if/else/end if instruction to determine which sections of a script to execute. The decision depends on whether the device receives a particular Script trigger.
- [break](break.html) Enable the execution of instructions to skip directly to the next instruction after the break block once the device receives a trigger.
- [wait](wait.html) Pause execution of a script. You can pause the script until the device receives a particular Script trigger or until the device generates a specified number of samples.
- [clear](clear.html) Clear a received Script trigger.
- [stream n](stream-n.html) The stream n instruction streams n samples of waveform data from host memory to the signal generator for immediate generation.

Parent topic:

Programming

Related concepts:

- Script Mode

<!--NI_TOPIC bundle=ni-fgen path=setting-attributes-before-reading-attributes.html language=enus -->
## TOPIC 00840: Setting Attributes Before Reading Attributes

- bundle_id: `ni-fgen`
- source_path: `setting-attributes-before-reading-attributes.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/setting-attributes-before-reading-attributes.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Attributes—which are also called properties in LabVIEW—are modified when you set them or when you call a configuration VI or function that sets them. It is important to set the attributes or call any configuration VIs or functions before reading back any attribute values for the following reasons: V

### Setting Attributes Before Reading Attributes

Attributes—which are also called properties in LabVIEW—are modified when you set them or when you call a configuration VI or function that sets them. 
It is important to set the attributes or call any configuration VIs or functions before reading back any attribute values for 
the following reasons:

- Values read are coerced depending on the current configuration of the session. If you read an attribute value and then 
set other attributes, the value read may no longer be valid.
- The driver verifies that the configuration of the device is valid at the time the attribute is read. It is possible to get
an error when reading an attribute if the configuration is not valid at that point, even when a setting later could make it valid.
- Reading attributes causes the driver to verify the current configuration. If you change some of the settings later, those 
settings need to be validated again.

Note

Parent topic:

NI-FGEN Tutorial

<!--NI_TOPIC bundle=ni-fgen path=sfdr.html language=enus -->
## TOPIC 00841: SFDR

- bundle_id: `ni-fgen`
- source_path: `sfdr.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/sfdr.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Spurious-free dynamic range (SFDR) is the usable dynamic range before spurious noise interferes with or distorts the fundamental signal. For specification purposes, the amplitude of the fundamental signal is usually -1 dBFS. SFDR is the measure of the difference in amplitude between the fundamental

### SFDR

Spurious-free dynamic range (SFDR) is the usable dynamic range before spurious
 noise interferes with or distorts the fundamental signal.

For specification purposes, the amplitude of the fundamental signal is usually -1 dBFS. SFDR is the measure of the difference in
 amplitude between the fundamental signal and the largest harmonically or nonharmonically
 related spur from DC to the full Nyquist bandwidth (half the sampling rate). A spur is
 any frequency bin on a spectrum analyzer, or from a Fourier transform, of the analog
 signal. SFDR is expressed in dBc.

The following figure illustrates how SFDR is measured.

[IMAGE alt='image' src='GUID-ED0AE39D-C610-4A73-8754-B2F5E76ED2D5-a5.gif']

Parent topic:

Frequency Domain Fundamentals

Related concepts:

- Nyquist and Shannon's Sampling Theorems

<!--NI_TOPIC bundle=ni-fgen path=simulation-mode.html language=enus -->
## TOPIC 00842: Simulation Mode

- bundle_id: `ni-fgen`
- source_path: `simulation-mode.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/simulation-mode.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: NI signal generators support simulation. Simulating a device enables you to perform the following tasks: Protect your devices by first testing settings and configurations on simulated devices. Verify device behaviors under a wide variety of operating conditions. Start or speed up application develop

### Simulation Mode

NI signal generators support simulation. Simulating a device enables you to perform the following tasks:

- Protect your devices by first testing settings and configurations on simulated devices.
- Verify device behaviors under a wide variety of operating conditions.
- Start or speed up application development before you have the hardware.
- Optimize designs and determine ideal design parameters.

Enabling simulation allows you to verify that you have correctly configured the device. For example, if a parameter is set to an invalid value for the device, NI-FGEN returns the same error it would for a real device. While simulation is useful for verifying your configuration, there are some areas where simulation is not sufficient to verify that your configuration is correct. For example, no errors will be returned for configurations that involve or depend upon external signals, such as configuring an external Sample clock or routing signals. Also, the amount of time a generation takes to complete will be ignored in simulation mode; a finite generation will finish immediately after it is initiated, regardless of how much data is downloaded and how fast it is generated.

#### LabVIEW Example

In LabVIEW, simulation is enabled with the Option String parameter of the niFgen Initialize With Options VI. Enable simulation (Simulate=1) and specify the device you want to simulate with the option string input.

The following example enables simulation of the NI PCI-5421 with 256 MB of onboard memory:

[IMAGE alt='image' src='GUID-C14F18CA-06D3-4B1D-AD2F-B109C89D1466-a5.gif']

For more information, refer to the niFgen Initialize With Options VI.

#### C Example

In LabWindows/CVI, simulation is enabled with the niFgen_InitWithOptions function. Enable simulation (Simulate=1) and specify the device you want to simulate with the option string parameter.

The following example enables simulation of the NI PCI-5421 with 256 MB of onboard memory:

niFgen_InitWithOptions (Resource, VI_TRUE, VI_TRUE, "Simulate=1, DriverSetup=Model:5421;BoardType:PCI;MemorySize:268435456",&vi );

For more information, refer to the niFgen_InitWithOptions function.

Parent topic:

Features

<!--NI_TOPIC bundle=ni-fgen path=sinad.html language=enus -->
## TOPIC 00843: SINAD

- bundle_id: `ni-fgen`
- source_path: `sinad.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/sinad.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Signal-to-noise-and-distortion ratio (SINAD) is the ratio of the RMS signal amplitude to the RMS sum of all other spectral components, including the harmonics but excluding DC. SINAD is usually expressed in dB.

### SINAD

Signal-to-noise-and-distortion ratio (SINAD) is the ratio of the RMS signal amplitude to the RMS sum of all other spectral components, including the harmonics but excluding DC. SINAD is usually expressed in dB.

Parent topic:

Frequency Domain Fundamentals

<!--NI_TOPIC bundle=ni-fgen path=software-trigger.html language=enus -->
## TOPIC 00844: Software Trigger

- bundle_id: `ni-fgen`
- source_path: `software-trigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/software-trigger.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: A software trigger is generated internally by a programmatic call to the niFgen Send Software Edge Trigger VI or the niFgen_SendSoftwareEdgeTrigger function and can occur at any time, based upon the conditions specified in the program.

### Software Trigger

A software trigger is generated internally by a programmatic call to the niFgen Send Software Edge Trigger VI or the niFgen_SendSoftwareEdgeTrigger function and can occur at any time, based upon the conditions specified in the program.

Parent topic:

Types of Triggers

<!--NI_TOPIC bundle=ni-fgen path=standard-function-mode.html language=enus -->
## TOPIC 00845: Standard Function Mode

- bundle_id: `ni-fgen`
- source_path: `standard-function-mode.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/standard-function-mode.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Standard Function output mode is used to generate standard function waveforms such as sine, square, triangle, and so on. DDS Implementation Standard Function output mode is implemented through direct digital synthesis (DDS) on the NI 5402/5406/5441/5442/5450/5451. DDS is a technique for deriving, un

### Standard Function Mode

Standard Function output mode is used to generate standard function waveforms such as sine, square, triangle, and so on.

#### DDS Implementation

Standard Function output mode is implemented through *direct digital synthesis* (DDS) on the NI 5402/5406/5441/5442/5450/5451. DDS is a technique for deriving, under digital control, an analog frequency source from a single Reference clock frequency. This technique produces high-frequency accuracy and resolution, temperature stability, wideband tuning, and rapid, phase-continuous frequency switching.

#### Software Implementation

Standard Function output mode is implemented primarily in software on the NI 5412/5421/5422. Instead of using separate DDS hardware to generate standard function waveforms, NI-FGEN creates and downloads standard function waveforms to arbitrary waveform memory and generates them just like arbitrary waveforms. NI-FGEN automatically selects the best clock mode, sample rate, and buffer size to produce the most accurate waveform possible. To determine how much arbitrary memory is used, query the Buffer Size property or the NIFGEN_ATTR_FUNC_BUFFER_SIZE attribute. To adjust the maximum amount of memory used by NI-FGEN for generating standard function waveforms, set the Max Buffer Size property NIFGEN_ATTR_FUNC_MAX_BUFFER_SIZE attribute. Increasing the maximum buffer size may result in a more accurate waveform.

Note

Frequency hopping and sweeping

Parent topic:

Output Modes

Related concepts:

- Direct Digital Synthesis
- Frequency Hopping and Sweeping

<!--NI_TOPIC bundle=ni-fgen path=starting-a-peer-to-peer-generation.html language=enus -->
## TOPIC 00846: Starting a Peer-to-Peer Generation

- bundle_id: `ni-fgen`
- source_path: `starting-a-peer-to-peer-generation.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/starting-a-peer-to-peer-generation.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: If the signal generator begins generating data from a peer-to-peer stream immediately after the first sample is received, the device may not have enough data to continue the generation and can underflow at startup. This problem is due to latency across the bus, and it is especially likely when heavy

### Starting a Peer-to-Peer Generation

If the signal generator begins generating data from a peer-to-peer stream immediately after the first sample is received, the device may not have enough data to continue the generation and can underflow at startup. This problem is due to latency across the bus, and it is especially likely when heavy, possibly unrelated, traffic is on the bus. To avoid underflow at startup, prime the endpoint with data before starting generation so that the device has a backlog of data to insulate the generation from the bursty nature of data flowing across the bus. There are three methods of preparing the signal generator endpoint for startup:

- P2P Endpoint Fullness Start Trigger property or NIFGEN_ATTR_P2P_ENDPOINT_FULLNESS_START_TRIGGER_LEVEL attribute —Starts generation after the endpoint receives the specified number of samples. If you do not specify the number of samples, NI-FGEN automatically selects an appropriate value. This method should work for most applications, and it requires the least amount of configuration.
- niFgen Write P2P Endpoint I16 VI or niFgen_WriteP2PEndpointI16 function—Primes the endpoint with initial data from the host to attempt to give the writer peer enough time to start sending data after the signal generator is started.
- Manual—Manually design the application so that the writer peer sends data to the signal generator endpoint prior to the signal generator initiating generation, as described in the following steps:
  - Configure both peers for peer-to-peer streaming.
  - Link both peers using the niP2P Create Peer to Peer Stream VI, the nip2pCreateAndLinkStream function, or through manual flow control .
  - Enable the stream using the niP2P Enable Peer to Peer Stream VI or the nip2pEnableStream function. After you enable the stream, the signal generator begins issuing credits to the writer peer.
  - Start the writer peer first so that it begins sending data to the signal generator prior to initiation.
  - Query the Space Available in Endpoint property or NIFGEN_ATTR_P2P_SPACE_AVAILABLE_IN_ENDPOINT attribute after starting the writer peer to ensure that sufficient data is transferred to the signal generator.
  - Call the niFgen Initiate Generation VI or the niFgen_InitiateGeneration function.

Note

NIFGEN_ATTR_P2P_ENDPOINT_FULLNESS_START_TRIGGER_LEVEL

NIFGEN_ATTR_P2P_SPACE_AVAILABLE_IN_ENDPOINT

Parent topic:

Configuring a Peer-to-Peer Stream

Related concepts:

- Flow Control

<!--NI_TOPIC bundle=ni-fgen path=stopping-a-peer-to-peer-generation.html language=enus -->
## TOPIC 00847: Stopping a Peer-to-Peer Generation

- bundle_id: `ni-fgen`
- source_path: `stopping-a-peer-to-peer-generation.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/stopping-a-peer-to-peer-generation.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: There are two methods to stop generation without an underflow error. Finite generation (stream n)—If the signal generator receives at least the specified number of samples from the writer peer, the NI-FGEN session completes without an underflow error. Infinite Generation with Done Notification—NI si

### Stopping a Peer-to-Peer Generation

There are two methods to stop generation without an underflow error.

- Finite generation ( stream n )—If the signal generator receives at least the specified number of samples from the writer peer, the NI-FGEN session completes without an underflow error.
- Infinite Generation with Done Notification—NI signal generators with peer-to-peer functionality support automatic Done Notification messages. If the writer peer also supports Done Notification messages, the signal generator is automatically configured to receive the message when the two peers are linked into a stream. When the writer peer completes sending data and disables the stream, a control message is sent across the bus. This message alerts the signal generator that the peer has no more data to send. The signal generator then waits until all data is played out the physical channels, asserts the Done event, and moves to the configured Idle behavior. Applications between two National Instruments devices, linked using NI-P2P, automatically use this behavior.

niFgen_IsDone

done

Note

nip2pFlushAndDisableStream

nip2pDisableStream

done

niFgen_IsDone

niFgen_AbortGeneration

#### Other Methods of Completing Peer-to-Peer Generation

The following methods are other ways to stop generation that are not considered graceful completion, but they may be suitable for some applications.

- User Requested Abort—Using the niFgen Abort Generation VI, the NI-FGEN session does not return an error and the niFgen Is Done VI or niFgen_IsDone function returns TRUE for done . However, if the writer peer is not configured carefully for this event, the writer peer may overflow because the signal generator is no longer allowing the writer to send data through the stream.
- Infinite Generation without Done Notification—If the writer peer stops sending data and does not send a Done Notification message, the signal generator underflows after playing the last of the data received without a configured Done Notification. NI-FGEN does not support determining if the underflow error is genuine or if the signal generator received and played all the expected data from the writer peer. However, if the generation proceeded without an underflow error up until the writer peer stopped sending data, then the underflow error can likely be ignored. This is not recommended, but may be suitable for applications that cannot send Done Notifications but have a method to determine if all data was played.

Parent topic:

Configuring a Peer-to-Peer Stream

<!--NI_TOPIC bundle=ni-fgen path=stream-n.html language=enus -->
## TOPIC 00848: stream n

- bundle_id: `ni-fgen`
- source_path: `stream-n.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/stream-n.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The stream n instruction streams n samples of waveform data from host memory to the signal generator for immediate generation. Usage Stream <n> samples.stream <n> Stream the data and generate a Marker event when a position within the data is generated.stream <n> marker0 (position 1, position 2, ...

### stream
 *n*

The stream n instruction streams n samples of
 waveform data from host memory to the signal generator for immediate generation.

#### Usage

- Stream <n> 
 samples. stream <n>
- Stream the data and generate a Marker event when a position within the data is
 generated. stream <n> marker0 (position 1, position 2, ... , position n) Specify
 each position in samples. Use the Export Signal VI or function for
 your driver to specify the destination terminal of the marker. Marker position is
 zero-based. For example, 0 refers to the first point in the data,
 63 refers to the 64th point in the data, and so on.

The following restrictions apply when using the stream
 <n> statement:

- The script cannot contain conditional statements, including if-else ,
 repeat until , and break statements.
- Markers must be on 128-byte boundaries.

#### stream
 n Examples

- Stream 1,280 samples. script myScript
 stream 1280
end script
- Stream forever. script myScript
 repeat forever
 stream 1280
 end repeat
end script

Parent topic:

Scripting Instructions

<!--NI_TOPIC bundle=ni-fgen path=streaming.html language=enus -->
## TOPIC 00849: Streaming

- bundle_id: `ni-fgen`
- source_path: `streaming.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/streaming.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Streaming is a way to generate waveforms that are too large to fit in the onboard memory of the signal generator. Streaming can be used in Arbitrary Waveform, Arbitrary Sequence, or Script output modes. To stream waveform data, allocate and identify all or a portion of the signal generator onboard m

### Streaming

Streaming is a way to generate waveforms that are too large to fit in the onboard memory of the signal generator. Streaming can be used in *Arbitrary Waveform*, *Arbitrary Sequence*, or *Script* output modes.

Note

#### Streaming Waveform Data

The following instructions are a guide for configuring your application for streaming. For a programmatic example, refer to Fgen Arb Waveform Streaming.vi for LabVIEW or ArbitraryWaveformStreaming.prj for LabWindows/CVI.

As an example, we have a 1.6 GB waveform we want to generate and an NI arbitrary waveform generator with 256 MB of onboard memory. This 1.6 GB waveform may be in the host memory, on disk, or data that your application generates dynamically during generation.

[IMAGE alt='image' src='GUID-0E592A7C-01F5-4B62-B514-F1A4F09AC3F9-a5.svg']

1. Specify the amount of onboard memory to be used for streaming —Call the niFgen Allocate Waveform VI or the niFgen_AllocateWaveform function to specify the amount of onboard memory to reserve for streaming. The allocated memory, known as the streaming waveform , serves as a buffer for the streaming process. The size of the waveform you wish to stream must be evenly divisible by the amount of onboard memory allocated for streaming to prevent the streaming waveform from being overwritten before it has generated.
2. Identify the streaming waveform —Set the Streaming Waveform Handle property or the NIFGEN_ATTR_STREAMING_WAVEFORM_HANDLE attribute to the waveform handle returned in Step 1. Setting this property or attribute ensures that none of your streaming data is overwritten before it is generated. NI-FGEN monitors your progress to ensure that you write fresh data fast enough to keep up with the generation. If your application fails to keep up or attempts to write fresh data over data that has not been generated, NI-FGEN returns an error.
3. Fill the streaming waveform with initial data —Call the niFgen Write Waveform VI or the niFgen_WriteWaveform function to write the first part of the waveform data to the streaming waveform in onboard memory.

 Tip 

 When transferring large blocks of waveform data, break the data into smaller blocks and call the niFgen Write Waveform VI or the niFgen_WriteWaveform function multiple times. The data is appended sequentially. A computer can allocate smaller blocks of a large waveform faster than allocating a single large contiguous block in memory. Depending on the amount of RAM on the computer, transferring ten 16 MB blocks may be faster than transferring one 160 MB block.

1. Begin generating the waveform —Call the niFgen Initiate Generation VI or the niFgen_InitiateGeneration function to begin the waveform generation. As the waveform generates, space in the streaming waveform becomes free.
2. (Optional) Monitor available memory as the waveform generates —Use the Space Available in Streaming Waveform property or the NIFGEN_ATTR_STREAMING_SPACE_AVAILABLE_IN_WAVEFORM attribute to determine how much of the streaming waveform is free for writing new data. As the waveform generates, space becomes available to write more waveform data.

1. Write a block of waveform data —Call niFgen Write Waveform VI or the niFgen_WriteWaveform function to write a new block of waveform data to the streaming waveform in onboard memory.
 
If the size of the new block of waveform data is larger than the space available, NI-FGEN waits until sufficient space becomes available or the streaming write time expires. Use the Streaming Write Timeout property or the NIFGEN_ATTR_STREAMING_WRITE_TIMEOUT attribute to change the streaming write time.
2. Repeat steps 5 and 6 until all waveform data is written.

#### Streaming to Multiple Channels

To stream data to multiple channels, you must provide interleaved data. You cannot stream to two or more channels with individual, non-interleaved writes for each channel.

#### Average Performance Rates

The following tables list the average data rates possible for PXI, PCI, and PXI Express signal generators. Average data transfer rates are highly system dependent. The following table is intended to give you an idea of the average sustainable transfer rates using 16-bit (or 2 byte) samples.

#### PXI and PCI

| Data Source | Data Rate (MB/s) * |
| --- | --- |
| Host memory on desktop computer or PXI embedded controller | ~90 to 115 |
| Desktop IDE or SATA hard drive | ~55 to 70† |
| Laptop or low RPM hard drive | 25 to 30† |
| Host memory on desktop across MXI-3 to PXI device | 25 |
| Host memory on desktop across MXI-4 to PXI device | 25 |
| * All data rates highly dependent on chip set. † Measurements were taken using the Windows API for unbuffered file I/O. For more information about streaming, refer to Data Streaming Architecture in PXI Systems. |  |

#### PXI Express

| Data Source | Data Rate (MB/s)* |
| --- | --- |
| From disk, such as a redundant array of independent disks (RAID). | > 600 |
| * Data transfer rates are limited by the speed of your streaming storage solution. Refer to Data Streaming for more information. † These numbers were obtained using several file I/O optimizations. For more information about this streaming process, refer to Stream to Disk Using Win32 File IO. |  |

#### Improving Streaming Performance

To improve your maximum sustainable transfer rate for streaming, consider the following recommendations:

- Adjust the Data Transfer Block Size property or the NIFGEN_ATTR_DATA_TRANSFER_BLOCK_SIZE attribute. The default data transfer block size for NI-FGEN is 2 MS (or 4 MB). If you were to write a 16 MB waveform to the signal generator, the complete transfer would occur using four separate DMA transfers. If you modify the data transfer block size to 8 MS (16 MB), for example, the data transfer is more efficient and is instead accomplished in a single transfer.
- Configure advanced streaming properties by calling the Maximum In-Flight Read Requests, PCI DMA Optimization Enabled, or Preferred Packet Size property or the NIFGEN_ATTR_DATA_TRANSFER_MAXIMUM_IN_FLIGHT_READS , NIFGEN_ATTR_DATA_TRANSFER_PCI_DMA_OPTIMIZATIONS , or NIFGEN_ATTR_DATA_TRANSFER_PREFERRED_PACKET_SIZE attributes.
- Optimize the bus bandwidth usage for multi-device streaming applications by calling the Maximum Bandwidth property or the NIFGEN_ATTR_DATA_TRANSFER_MAXIMUM_BANDWIDTH attribute.
- When streaming from hard drives, consider the hard drive speed for maximum sustainable rates. Laptop hard drives typically have a data transfer rate of 25 to 30 MB/s. Desktop hard drives often can meet 55 to 70 MB/s. 
 Transfer rates from hard drives can vary for a number of reasons, including where the data is physically stored on the hard drive and how much data is stored. Storing your waveform files on a fairly empty, defragmented hard drive may help increase performance.
- Consider using a redundant array of independent disks (RAID) configuration to utilize striping to increase data transfer rates from disk.
- When using 18-slot PXI chassis, install the signal generator used for streaming in the first segment (Slots 2 to 6) of the PXI chassis.
- Utilize Direct DMA .

Parent topic:

Waveform Fundamentals

Related concepts:

- Arbitrary Waveform Output Mode
- Arbitrary Sequence Mode
- Script Mode
- Direct DMA

<!--NI_TOPIC bundle=ni-fgen path=synchronization.html language=enus -->
## TOPIC 00850: Synchronization

- bundle_id: `ni-fgen`
- source_path: `synchronization.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/synchronization.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Synchronization occurs when two or more measurement devices operate in step with a common Reference clock. You can synchronize NI signal generators with other instruments, including digitizers and digital I/O devices, or you can synchronize several signal generators with each other. For an overview

### Synchronization

Synchronization occurs when two or more measurement
devices operate in step with a common Reference clock. You can
synchronize NI signal generators with other instruments,
including digitizers and digital I/O devices, or you can
synchronize several signal generators with each other.

For an overview of synchronization, refer to 
Think Synchronization First to
Optimize Automated Test at NI Developer Zone.

Parent topic:

Integration and System Considerations

<!--NI_TOPIC bundle=ni-fgen path=system-reference-clock-pxi-clk10.html language=enus -->
## TOPIC 00851: System Reference Clock, PXI_CLK10

- bundle_id: `ni-fgen`
- source_path: `system-reference-clock-pxi-clk10.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/system-reference-clock-pxi-clk10.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The PXI chassis supplies the PXI 10 MHz system Reference clock signal (PXI_CLK10) independently to each peripheral slot. An independent buffer drives the clock signal to each peripheral slot. The buffer has a source impedance matched to the backplane and a skew ranging from less than 1 ns to better

### System Reference Clock, PXI_CLK10

The PXI chassis supplies the PXI 10 MHz system Reference clock signal (PXI_CLK10) independently
 to each peripheral slot. An independent buffer drives the clock signal to each
 peripheral slot. The buffer has a source impedance matched to the backplane and a skew
 ranging from less than 1 ns to better than 250 ps between slots. You can use this common
 Reference clock signal to synchronize multiple devices in a measurement or control
 system. You can drive PXI_CLK10 from an external source through the PXI_CLK10_IN pin on
 the P2 connector of the PXI star trigger, which is controlled from slot 2 in PXI chassis
 or from system timing slot in PXIe chassis. Sourcing an external clock on this pin
 automatically disables the 10 MHz source on the backplane. You can synchronize multiple
 chassis that have connectors on the back panel for 10 MHz reference in and 10 MHz
 reference out. Refer to your PXI chassis documentation for more information.

Parent topic:

PXI/PXI Express Systems

<!--NI_TOPIC bundle=ni-fgen path=thd.html language=enus -->
## TOPIC 00852: THD

- bundle_id: `ni-fgen`
- source_path: `thd.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/thd.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The total harmonic distortion (THD) of a signal is the ratio of the sum of the powers of the first five harmonics above the measured fundamental frequency to the power of the fundamental frequency. THD is usually expressed in dB or dBc. Measurements for calculating the THD are made at the output of

### THD

The total harmonic distortion (THD) of a signal is the ratio of the sum of the powers of the first five harmonics above the measured fundamental frequency to the power of the fundamental frequency. THD is usually expressed in dB or dBc. Measurements for calculating the THD are made at the output of a device under specified conditions.

Parent topic:

Frequency Domain Fundamentals

<!--NI_TOPIC bundle=ni-fgen path=trigger-modes.html language=enus -->
## TOPIC 00853: Trigger Modes

- bundle_id: `ni-fgen`
- source_path: `trigger-modes.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/trigger-modes.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Frequency List, Arbitrary Waveform, and Arbitrary Sequence output modes support multiple trigger modes that affect the behavior of the signal generator when receiving triggers. These trigger modes include Single trigger mode, Continuous trigger mode, Stepped trigger mode, and Burst trigger mode. Ref

### Trigger Modes

Frequency List

Arbitrary Waveform

Arbitrary Sequence

Note

Parent topic:

Triggers

Related concepts:

- Frequency List Mode
- Arbitrary Waveform Output Mode
- Arbitrary Sequence Mode

<!--NI_TOPIC bundle=ni-fgen path=trigger-sources.html language=enus -->
## TOPIC 00854: Trigger Sources

- bundle_id: `ni-fgen`
- source_path: `trigger-sources.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/trigger-sources.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: NI signal generators support the following possible trigger sources: Immediate, also known as software Digital front panel connector RTSI bus trigger lines (PCI devices) PXI trigger bus lines (backplane of PXI devices) PXI star trigger line PFI inputs (SMB front panel connectors) The following figur

### Trigger Sources

NI signal generators support the following possible trigger sources:

- Immediate, also known as software
- Digital front panel connector
- RTSI bus trigger lines (PCI devices)
- PXI trigger bus lines (backplane of PXI devices)
- PXI star trigger line
- PFI inputs (SMB front panel connectors)

The following figure shows the trigger sources for NI signal generators.

[IMAGE alt='image' src='GUID-C4F0DB2D-363C-4752-888F-2B7E4086FC53-a5.gif']

For NI signal generators, trigger sources are software selectable. To set a trigger source, use
 the parameters in the niFGEN Configure Trigger VI or the
 niFgen_ConfigureTriggerSource function.

Parent topic:

Triggers

<!--NI_TOPIC bundle=ni-fgen path=triggering.html language=enus -->
## TOPIC 00855: Triggers

- bundle_id: `ni-fgen`
- source_path: `triggering.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/triggering.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: A trigger is an input signal that cause the signal generator to perform an action such as starting or stopping a generation operation. Triggers can be internal (software-generated) or external. Confirm whether the following sentence can be deleted. The meaning seems to be the same.A trigger is an ex

### Triggers

A *trigger* is an input signal that cause the signal generator to
 perform an action such as starting or stopping a generation operation. Triggers can be
 internal (software-generated) or external.

External digital triggers have different types and can be re-exported. When used with
 *events*, triggers can enable you to synchronize the hardware operation
 with external circuitry or other NI devices.

When triggering your NI signal generator, you can select the trigger type, the trigger
 source, and the trigger mode that you want to use.

Parent topic:

Waveform Fundamentals

Related concepts:

- Types of Triggers
- Events
- Triggers Summary
- Trigger Sources
- Trigger Modes

<!--NI_TOPIC bundle=ni-fgen path=triggers-summary.html language=enus -->
## TOPIC 00856: Triggers Summary

- bundle_id: `ni-fgen`
- source_path: `triggers-summary.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/triggers-summary.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following table describes the triggers supported by signal generators. The Supported Types column denotes which trigger types are valid for a given trigger. Trigger Name Supported Types Description Start Digital Edge, Software The Start trigger transitions a device from an idle state to a genera

### Triggers Summary

The following table describes the triggers supported by signal generators. The Supported Types column denotes which trigger types are valid for a given trigger.

| Trigger Name | Supported Types | Description |
| --- | --- | --- |
| Start | Digital Edge, Software | The Start trigger transitions a device from an idle state to a generation state where the device can respond to Sample clocks. |
| Script | Digital Edge, Digital Level, Software | The Script trigger is a general-purpose trigger with a role that is entirely determined by the context of the generation script. A script allows you to create sophisticated generation operations. For example, the script could configure the device to generate waveform A, then wait for the Script trigger, then generate waveform B. You can create multiple Script triggers for use in your application. Once a digital edge Script trigger has been received, that trigger remains true for all subsequent instructions until the clear instruction is called or the trigger is reset after being used in the wait, repeat/end repeat, or if instructions. |

Parent topic:

Triggers

Related concepts:

- Edge Trigger
- Software Trigger
- Level Trigger
- Script Mode

<!--NI_TOPIC bundle=ni-fgen path=types-of-triggers.html language=enus -->
## TOPIC 00857: Types of Triggers

- bundle_id: `ni-fgen`
- source_path: `types-of-triggers.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/types-of-triggers.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: A trigger is an external stimulus that initiates one or more device functions. Trigger stimuli include digital edges, software functions, and analog levels. You can trigger your NI signal generator with one of the following types of triggers: Edge Level Software Individual triggers may not support

### Types of Triggers

A trigger is an external stimulus that initiates one or more device functions. Trigger stimuli include digital edges, software functions, and analog levels.

You can trigger your NI signal generator with one of the following types of triggers:

- Edge
- Level
- Software

Note

Triggers Summary

Parent topic:

Triggers

Related concepts:

- Edge Trigger
- Level Trigger
- Software Trigger
- Triggers Summary

<!--NI_TOPIC bundle=ni-fgen path=user-manual-welcome.html language=enus -->
## TOPIC 00858: NI-FGEN User Manual

- bundle_id: `ni-fgen`
- source_path: `user-manual-welcome.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/user-manual-welcome.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI-FGEN User Manual provides detailed descriptions of the product functionality and the step by step processes for use. Looking for Something Else?For information not found in the User Manual for your product, such as specifications and API reference, browse Related Information.

### NI-FGEN
 User Manual

The NI-FGEN User Manual provides detailed
 descriptions of the product functionality and the step by step processes for use.

#### Looking for Something Else?

For information not found in the User Manual
 for your product, such as specifications and API reference, browse *Related
 Information*.

Related information:

- Download NI-FGEN
- NI-FGEN Release Notes
- Interactive Activation Guide
- NI-FGEN LabVIEW VI Reference
- NI-FGEN C Function Reference

<!--NI_TOPIC bundle=ni-fgen path=using-the-standard-functionality-for-error-in.html language=enus -->
## TOPIC 00859: Using the Standard Functionality for error in Parameters

- bundle_id: `ni-fgen`
- source_path: `using-the-standard-functionality-for-error-in.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/using-the-standard-functionality-for-error-in.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Many LabVIEW nodes such as VIs contain error in parameters you can use to manage errors. These parameters typically provide the same, standard functionality. When a node exhibits different parameter functionality, the exceptions are documented in the reference material for that node. Standard error

### Using the Standard Functionality for error in Parameters

error in

error in

Note

error in

error in

|  | error in describes error conditions that occur before this node runs. The default is no error. If an error occurred before this node runs, the node passes the error in value to error out. This node runs normally only if no error occurred before this node runs. If an error occurs while this node runs, it runs normally and sets its own error status in error out. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. |
| --- | --- |

The error in cluster contains the following cluster elements:

|  | status is TRUE (X) if an error occurred before this node ran or FALSE (checkmark) to indicate a warning or that no error occurred before this node ran. The default is FALSE. |
| --- | --- |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is an error code. If status is FALSE, code is 0 or a warning code. |
|  | source specifies the origin of the error or warning and is, in most cases, the name of the node that produced the error or warning. The default is an empty string. |

Parent topic:

Programming

<!--NI_TOPIC bundle=ni-fgen path=using-the-standard-functionality-for-error-ou.html language=enus -->
## TOPIC 00860: Using the Standard Functionality for error out Parameters

- bundle_id: `ni-fgen`
- source_path: `using-the-standard-functionality-for-error-ou.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/using-the-standard-functionality-for-error-ou.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Many LabVIEW nodes such as VIs contain an error out parameter you can use to manage errors. These parameters typically provide the same, standard functionality. When a node exhibits different parameter functionality, the exceptions are documented in the reference material for that node. Standard err

### Using the Standard Functionality for error out Parameters

Many LabVIEW nodes such as VIs contain an error out parameter you can use to manage errors. These parameters typically provide the same, standard functionality. When a node exhibits different parameter functionality, the exceptions are documented in the reference material for that node.

Standard error out functionality is as follows:

|  | error out contains error information. If error in indicates that an error occurred before this VI ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- | --- |

error out contains the following cluster elements:

|  | status is TRUE (X) if an error occurred before this node ran or during the running of this node or FALSE (checkmark) to indicate a warning or that no error occurred before this node ran or during the running of this node. |
| --- | --- |
|  | code is the error or warning code. If status is TRUE, code is an error code. If status is FALSE, code is 0 or a warning code. |
|  | source specifies the origin of the error or warning and is, in most cases, the name of the node that produced the error or warning. |

Parent topic:

Programming

<!--NI_TOPIC bundle=ni-fgen path=video-levels.html language=enus -->
## TOPIC 00861: Video Levels

- bundle_id: `ni-fgen`
- source_path: `video-levels.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/video-levels.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The video levels define the levels and ranges for the different parts of the video signal. The unit used to define video levels is the IRE (Institute of Radio Engineers). The blanking level refers to 0 IRE and the white level refers to +100 IRE. The blanking level, which is the reference level for t

### Video Levels

The video levels define the levels and ranges for the different parts of the video signal. The unit used to define video levels is the IRE (Institute of Radio Engineers). The blanking level refers to 0 IRE and the white level refers to +100 IRE. The blanking level, which is the reference level for the video signal (usually 0 V), is different from the black level if a setup is applied to the signal as shown in the following figure.

[IMAGE alt='image' src='GUID-04BEDAF9-2EF3-425D-ABCC-A8324F8F642C-a5.gif']

For the M-NTSC, M-PAL and N-PAL video formats, a setup of 7.5 IRE is usually applied, moving the black level to +7.5 IRE. For all other formats, the black level is aligned with the blanking level at 0 IRE.

The following table shows the different video levels depending on the video format.

| Video Format | Sync Level | Blanking Level | Black Level | White Level | Peak Level | Burst Amplitude |
| --- | --- | --- | --- | --- | --- | --- |
| M-NTSC | –40 IRE | 0 IRE | +7.5 IRE | +100 IRE | +120 IRE | 20.0 IRE |
| B/G-PAL | –43 IRE | 0 IRE | 0 IRE | +100 IRE | +133 IRE | 21.5 IRE |
| SECAM | –43 IRE | 0 IRE | 0 IRE | +100 IRE | +130 IRE | N/A |
| M-PAL | –40 IRE | 0 IRE | +7.5 IRE | +100 IRE | +120 IRE | 20.0 IRE |
| N-PAL | –40 IRE | 0 IRE | +7.5 IRE | +100 IRE | +133 IRE | 20.0 IRE |
| Comb. N-PAL | –43 IRE | 0 IRE | 0 IRE | +100 IRE | +133 IRE | 21.5 IRE |

The analog composite video signal is defined as a voltage source with an output impedance of 75 Ω. The sync-to-white level is normally 1 V <sub>pk-pk</sub> when loaded with a 75 Ω resistance. Therefore, the unloaded signal is nominally 2 V <sub>pk-pk</sub>.

For NTSC, the difference between white and sync levels is 140 IRE, so the analog level corresponds to approximately 7.143 mV/IRE. For B/G-PAL or SECAM, the difference between white and sync levels is 143 IRE, so the analog level corresponds to approximately 7.000 mV/IRE.

Parent topic:

Video Signal Fundamentals

<!--NI_TOPIC bundle=ni-fgen path=video-signal-fundamentals.html language=enus -->
## TOPIC 00862: Video Signal Fundamentals

- bundle_id: `ni-fgen`
- source_path: `video-signal-fundamentals.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/video-signal-fundamentals.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Review the following topics to learn about the fundamentals of video signals.

### Video Signal Fundamentals

Review the following topics to learn about the fundamentals of video signals.

- [Generating Composite Video Signals](generating-composite-video-signals.html)
- [Different Video Formats](different-video-formats.html)
- [Scanning Speed](scanning-speed.html)
- [Color Coding](color-coding.html)
- [Interlaced Scanning](interlaced-scanning.html)
- [Active Image](active-image.html)
- [Video Levels](video-levels.html)

<!--NI_TOPIC bundle=ni-fgen path=wait.html language=enus -->
## TOPIC 00863: wait

- bundle_id: `ni-fgen`
- source_path: `wait.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/wait.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Pause execution of a script. You can pause the script until the device receives a particular Script trigger or until the device generates a specified number of samples. Usage Pause the execution until the device receives a particular Script trigger.wait until scripttrigger0If the device receive a Sc

### wait

Pause execution of a script. You can pause the script
 until the device receives a particular Script trigger or until the device generates a
 specified number of samples.

#### Usage

- Pause the execution until the device receives a particular Script
 trigger. wait until scripttrigger0 Note If the device receive a Script trigger before the
 wait instruction, then the script moves to the next
 instruction with the smallest possible delay. If you want to ignore Script
 triggers received before a wait statement, use the
 clear instruction.
- Pause the execution for a finite amount of
 time. wait <number of samples>
- Pause the execution for a finite amount of time and generate markers while
 waiting. wait 256 marker1(0, 128) marker0(64)

#### wait Examples

- Generate myWfmA , wait for receipt of a Script trigger, then
 generate myWfmB . generate myWfmA
wait until scripttrigger0
generate myWfmB
- Execute the following sequence: repeat forever
 repeat 5
 generate myWfmA
 generate myWfmB
 end repeat
 wait until scripttrigger0
 repeat 10
 generate myWfmC
 generate myWfmD
 end repeat
 wait until scripttrigger0
end repeat
  1. Generate myWfmA , myWfmB 5 times.
  2. Wait for receipt of a Script trigger.
  3. Generate myWfmC , myWfmD 10 times.
  4. Wait for receipt of a Script trigger.
- Execute the following sequence: generate myWfmA
wait 100
generate myWfmB
  1. Generate myWfmA .
  2. Wait 100 samples.
  3. Generate myWfmB .
- Execute the following sequence: script waitWithMarkers
 wait 256 marker1(0, 128) marker0(64)
 wait until scripttrigger marker0(0)
end script
  1. Wait 256 samples, generating Marker 1 at samples 0 and 128, and
 generating Marker 0 at sample 64.
  2. Generate Marker 0 and wait for receipt of a Script trigger.

Parent topic:

Scripting Instructions

<!--NI_TOPIC bundle=ni-fgen path=waveform-fundamentals.html language=enus -->
## TOPIC 00864: Waveform Fundamentals

- bundle_id: `ni-fgen`
- source_path: `waveform-fundamentals.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/waveform-fundamentals.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Review the following topics to learn about waveform fundamentals.

### Waveform Fundamentals

Review the following topics to learn about waveform fundamentals.

- [Bandwidth and Passband Flatness](bandwidth-and-passband-flatness.html)
- [Sample Rate](sample-rate.html)
- [DAC Resolution](dac-resolution.html)
- [Output Modes](output-modes.html) The output mode of your signal generator determines the type of waveforms your signal generator produces.
- [Frequency Hopping and Sweeping](frequency-hopping-and-sweeping.html)
- [Clocking](clocking.html)
- [Impedance Matching](impedance-matching.html)
- [Output Attenuation](output-attenuation.html) Output attenuation is a method of controlling the output voltage level of the signal being generated.
- [Output Enable](output-enable.html) You can switch off the waveform generation at the output connector by controlling the output enable relay on the signal generator.
- [Output Impedance](output-impedance.html) NI signal generators have an output impedance of 50 Ω and an optional 75 Ω on select devices.
- [Differential Output](differential-output.html) An NI signal generator that is configured for differential output generates waveforms using two complementary signals. Each signal is generated at a different differential output connector.
- [Phase-Locked Loop](phase-locked-looping.html)
- [Triggers](triggering.html) A trigger is an input signal that cause the signal generator to perform an action such as starting or stopping a generation operation. Triggers can be internal (software-generated) or external.
- [Events](events.html)
- [Streaming](streaming.html)
- [Frequency Domain Fundamentals](frequency-domain-fundamentals.html)
- [Filtering and Interpolation](filtering-and-interpolation.html)
