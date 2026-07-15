# NI DOCUMENT BUNDLE: ni-fgen

<!--NI_BUNDLE_CHUNK bundle=ni-fgen start=251 end=500 -->
<!--NI_TOPIC bundle=ni-fgen path=ni-5412-memory-fragmentation.html language=enus -->
## TOPIC 00251: NI 5412 Memory Fragmentation

- bundle_id: `ni-fgen`
- source_path: `ni-5412-memory-fragmentation.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5412-memory-fragmentation.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: When storing multiple waveforms in NI 5412 memory, fragmentation can become a problem. Both waveforms and instructions are stored in NI 5412 memory in contiguous blocks. These blocks are allocated in multiples of 128 bytes, and they are written in the order that you configure them. Fragmentation occ

### NI 5412 Memory Fragmentation

When storing multiple waveforms in
NI 5412 memory, fragmentation can become a
problem. Both waveforms and instructions are stored in
NI 5412 memory in contiguous blocks. These
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

NI 5412 Onboard Memory

<!--NI_TOPIC bundle=ni-fgen path=ni-5412-ni-5412-overview.html language=enus -->
## TOPIC 00252: NI 5412 NI 5412 Overview

- bundle_id: `ni-fgen`
- source_path: `ni-5412-ni-5412-overview.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5412-ni-5412-overview.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5412 is a 100 MS/s, 14-bit arbitrary waveform generator with the following features: One 14-bit resolution output channel Output amplitude up to 12 V [pk-pk] into a 50 Ω load Offset up to ±25% of V [pk-pk] Up to 20 MHz sine waveform output Up to 5 MHz square waveform output Up to 1 MHz triang

### NI 5412 NI 5412 Overview

The NI 5412 is a 100 MS/s, 14-bit arbitrary
waveform generator with the following features:

- One 14-bit resolution output channel
- Output amplitude up to 12 V 
 pk-pk into a 50 Ω load
- Offset up to ±25% of V 
 pk-pk
- Up to 20 MHz sine waveform output
- Up to 5 MHz square waveform output
- Up to 1 MHz triangle, ramp-up, and ramp-down waveform output
- Software-selectable output impedances (50 Ω or
75 Ω) and output attenuation levels from 0 dB to
51 dB
- High-Resolution, Divide by 
 N , and external clocking
- PLL synchronization to external clocks or to
PXI_CLK10
- NI-TClk support for multi-module synchronization. Refer to 
 Start»All Programs»National Instruments»NI-TClk 
for more information.
- Sampling rate up to 100 MS/s
- Up to 256 MB of onboard waveform memory
- Waveform linking and looping for arbitrary waveform
generation
- Digital filters
- Digital gain
- Two external trigger inputs
- Marker as trigger output
- PXI trigger/RTSI lines

All NI 5412 devices follow industry-standard
Plug and Play specifications for the PXI bus, and offer seamless
integration with compliant systems.

Parent topic:

Devices

<!--NI_TOPIC bundle=ni-fgen path=ni-5412-onboard-memory.html language=enus -->
## TOPIC 00253: NI 5412 Onboard Memory

- bundle_id: `ni-fgen`
- source_path: `ni-5412-onboard-memory.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5412-onboard-memory.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5412 signal generator uses an onboard memory that is 16-bits wide. The minimum standard memory size for the NI 5412 is 8 MB which translates to 8,338,608 usable bytes. With the minimum standard memory size, you can store very long waveforms on the device and obtain reliable waveform generatio

### NI 5412 Onboard Memory

The NI 5412 signal generator
uses an onboard memory that is 16-bits wide. The minimum standard
memory size for the NI 5412 is 8 MB
which translates to 8,338,608 usable bytes. With the minimum
standard memory size, you can store very long waveforms on the
device and obtain reliable waveform generation at full sample rate
of 100 MS/s. The NI 5412 comes with
higher memory options of 32 MB and 256 MB.

The onboard memory is a single large memory area that stores both waveforms and sequence instructions to generate
the waveforms. The instructions for a complicated sequence can
occupy a significant portion of memory. The architecture of the
NI 5412 allows you to load multiple
waveforms and multiple sequence instructions into the memory. The
following diagram illustrates NI 5412
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

Parent topic:

NI 5412 Theory of Operation

<!--NI_TOPIC bundle=ni-fgen path=ni-5412-output-enable.html language=enus -->
## TOPIC 00254: NI 5412 Output Enable

- bundle_id: `ni-fgen`
- source_path: `ni-5412-output-enable.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5412-output-enable.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can disable the analog output signal at the CH 0 connector by controlling the output enable relay, as shown in the following figure. When the output enable relay is disabled, the output signal is connected to ground through a 50 or 75 Ω resistance depending on the output impedance selected. The

### NI 5412 Output Enable

You can disable the analog output signal at the CH
0 connector by controlling the output enable relay, as shown in the
following figure.

[IMAGE alt='image' src='GUID-BFAEDBE6-696A-4B0B-9A41-C8FD2A49A5A8-a5.gif']

When the output enable relay is disabled, the
output signal is connected to ground through a 50 or
75 Ω resistance depending on the output impedance
selected. The output enable relay is enabled for normal waveform
generation, connecting the CH 0 SMB connector to the 
*Analog Output path*. You
can change the output enable state at any time during waveform
generation, and the generation continues on internally.

niFgen_ConfigureOutputEnabled

Note

Parent topic:

NI 5412 Analog Output

Related concepts:

- NI 5412 Analog Output

<!--NI_TOPIC bundle=ni-fgen path=ni-5412-output-impedance.html language=enus -->
## TOPIC 00255: NI 5412 Output Impedance

- bundle_id: `ni-fgen`
- source_path: `ni-5412-output-impedance.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5412-output-impedance.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5412 Analog Out path is designed to have an output impedance of 50 Ω from the Output Enable relay looking back towards the Main DAC. There is a selectable 25 Ω resistance that can be switched into the Analog Output path between the Output Enable Relay and the CH 0 SMB connector for applicatio

### NI 5412 Output Impedance

The NI 5412 Analog Out path is designed to
have an output impedance of 50 Ω from the Output Enable
relay looking back towards the Main DAC. There is a selectable
25 Ω resistance that can be switched into the Analog
Output path between the Output Enable Relay and the CH 0 SMB
connector for applications requiring a 75 Ω impedance.
Most applications use a load impedance of 50 Ω, but
applications such as video testing, require 75 Ω. Refer
to the following figure.

[IMAGE alt='image' src='GUID-6D4C36D6-D454-4961-979E-9F00D4097CE0-a5.gif']

If the load impedance is a high impedance (~1
MΩ), you may see output levels up to twice the selected
output value for a matched input/output impedance. These levels can
be as high as 24 V 
<sub>pk-pk</sub> for the High-Gain Amplifier path. Normally, the
output levels increase as the load impedance increases. The
NI 5412 can compensate for different load impedance values.
Refer to 
*CH 0 Connector* for more
information.

Note

Parent topic:

NI 5412 Analog Output

Related concepts:

- NI 5412 CH 0 Connector

<!--NI_TOPIC bundle=ni-fgen path=ni-5412-output-modes.html language=enus -->
## TOPIC 00256: NI 5412 Output Modes

- bundle_id: `ni-fgen`
- source_path: `ni-5412-output-modes.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5412-output-modes.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The output mode of your signal generator determines the type of waveforms your signal generator produces. To select an output mode, set the Output Mode parameter of the niFgen Configure Output Mode VI or the niFgen_ConfigureOutputMode function.

### NI 5412 Output Modes

The output mode of your signal generator determines the type of
waveforms your signal generator produces. To select an output mode,
set the 
Output Mode parameter of the 
niFgen
Configure Output Mode VI or the 
niFgen_ConfigureOutputMode function.

Parent topic:

NI 5412 Waveform Generation

<!--NI_TOPIC bundle=ni-fgen path=ni-5412-pci-block-diagram.html language=enus -->
## TOPIC 00257: NI 5412 PCI Block Diagram

- bundle_id: `ni-fgen`
- source_path: `ni-5412-pci-block-diagram.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5412-pci-block-diagram.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: This topic contains information about the NI PCI-5412 top-level block diagram and descriptions of the individual blocks. The following list describes the individual blocks: Onboard Reference clock derives frequencies and sample rates when generating waveforms. Onboard Memory stores the waveform data

### NI 5412 PCI Block Diagram

This topic contains information about the
NI PCI-5412 top-level block diagram and descriptions of the
individual blocks.

[IMAGE alt='image' src='GUID-BB0E45BE-FCBB-49FE-905A-0E0F73A42555-a5.gif']

The following list describes the individual
blocks:

- Onboard Reference clock derives frequencies and sample
rates when generating waveforms.
- Onboard Memory stores the waveform data and generation
instructions that you load into the device.
- Clocking allows you to create your Sample clock and
Reference clock.
- The 
 Waveform Generation Engine retrieves the waveform data and
instructions from the 
 Onboard Memory using the Sample clock. The 
 Waveform Generation Engine also uses this clock to
retrieve triggers from 
 Trigger and Event Control .
- The output from the 
 Waveform Generation Engine is sent to the 
 DAC device after any digital gain is applied.
- The 
 DAC also contains an selectable 
 Digital Filter , which interpolates and filters the
waveform data.
- The waveform data is sent from the 
 DAC to the 
 Analog Output path where the waveform data is
amplified.
- The 
 Routing Matrix allows flexible routing of the RTSI trigger
lines and the external PFI lines.

Parent topic:

NI 5412 Theory of Operation

<!--NI_TOPIC bundle=ni-fgen path=ni-5412-pci-clock-source-and-frequency.html language=enus -->
## TOPIC 00258: NI 5412 PCI Clock Source and Frequency

- bundle_id: `ni-fgen`
- source_path: `ni-5412-pci-clock-source-and-frequency.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5412-pci-clock-source-and-frequency.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5412 has a Sample clock rate of 10 Hz to 100 MHz. The timing of the NI 5412 is very flexible, and you have multiple choices for deriving the Sample clock. There are modes for deriving the Sample clock from the internal Sample clock timebase, as well as modes to provide external clocks. You al

### NI 5412 PCI Clock Source and Frequency

The NI 5412 has a Sample clock rate of
10 Hz to 100 MHz. The timing of the NI 5412 is
very flexible, and you have multiple choices for deriving the
Sample clock. There are modes for deriving the Sample clock from
the internal Sample clock timebase, as well as modes to provide
external clocks. You also have several choices for providing the
frequency reference for the onboard phase-locked loop.

[IMAGE alt='image' src='GUID-9C4A080E-538D-4087-AE39-C87D528E679E-a5.gif']

#### Related Topics

*Sample Clock Sources*

*Internal Sample Clock
Sources*

*PLL Reference
Sources*

*External Sample Clock Sources*

*Exporting Clocks*

Parent topic:

NI 5412 Theory of Operation

Related concepts:

- NI 5412 Clocking Options
- NI 5412 Internal Sample Clock
- NI 5412 Phase-Locked Loop Reference Clock
- NI 5412 External Sample Clock
- NI 5412 Exporting Clocks

<!--NI_TOPIC bundle=ni-fgen path=ni-5412-pci-front-panel.html language=enus -->
## TOPIC 00259: NI 5412 PCI Front Panel

- bundle_id: `ni-fgen`
- source_path: `ni-5412-pci-front-panel.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5412-pci-front-panel.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the NI PCI-5412 front panel. This front panel has four SMB connectors and an optional 68-pin male VHDCI connector. The CLK IN Connector SMB connector provides the device with an external reference or external Sample clock. The PFI 0 and PFI 1 SMB connectors are multi-direc

### NI 5412 PCI Front Panel

The following figure shows the
NI PCI-5412 front panel. This front panel has four SMB
connectors and an optional 68-pin male VHDCI connector.

[IMAGE alt='image' src='GUID-8277C84B-898F-4DCA-B527-E2DB5F5045B1-a5.gif']

The 
*CLK IN Connector* SMB connector
provides the device with an external reference or external Sample
clock.

The 
*PFI 0 and PFI 1* SMB
connectors are multi-direction connections for a number of
different signals.

The 
*CH 0* SMB connector is the analog
output from which arbitrary waveforms are generated.

Parent topic:

NI 5412 NI 5412 Overview

Related concepts:

- NI 5412 CLK IN Connector
- NI 5412 PFI Connectors
- NI 5412 CH 0 Connector

<!--NI_TOPIC bundle=ni-fgen path=ni-5412-pfi-connectors.html language=enus -->
## TOPIC 00260: NI 5412 PFI Connectors

- bundle_id: `ni-fgen`
- source_path: `ni-5412-pfi-connectors.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5412-pfi-connectors.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: PFI 0 and PFI 1 are bidirectional connectors. As an input, the PFI terminals can accept a trigger from an external source that can start or step through waveform generation. As an output, the PFI lines route a signal out from the following sources: Marker events Start trigger PLL Reference clock sou

### NI 5412 PFI Connectors

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

device specifications

Note

Parent topic:

NI 5412 NI 5412 Overview

<!--NI_TOPIC bundle=ni-fgen path=ni-5412-phase-locked-loop-reference-clock.html language=enus -->
## TOPIC 00261: NI 5412 Phase-Locked Loop Reference Clock

- bundle_id: `ni-fgen`
- source_path: `ni-5412-phase-locked-loop-reference-clock.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5412-phase-locked-loop-reference-clock.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: A phase-locked loop (PLL) is a circuit that tunes the Sample clock timebase to phase–lock to an external Reference clock. The PLL Reference clock source controls the source of the control voltage that tunes the VCXO of the Sample clock timebase for internal clock update sources. The frequency stabil

### NI 5412 Phase-Locked Loop Reference Clock

Note

device
specifications

The following figure shows the NI 5412 Reference Clock Source path.

[IMAGE alt='image' src='GUID-928A3C7A-05C9-46C0-86CE-DCD9AFB72E85-a5.gif']

Note

NIFGEN_ATTR_REFERENCE_CLOCK_SOURCE

#### Reference Clock Sources

The NI 5412 can
phase-lock its Sample clock timebase to an external signal
that is present on the CLK IN front panel connector. PXI devices
can also phase–lock to a 10 MHz Reference clock signal
provided by the PXI bus (PXI_CLK10), while PCI devices can
phase–lock to RTSI line 7 or to the onboard Reference
clock.

Refer to the table in 
*Clocking Options*,
for the valid NI-FGEN property value combinations that can be used
to configure the NI 5412 clock settings
for an external Reference clock.

Note

device 
specifications

Related Topics

Configuring a Reference
Clock

Parent topic:

NI 5412 Clocking Options

Related concepts:

- NI 5412 Clocking Options
- Configuring a Reference Clock

<!--NI_TOPIC bundle=ni-fgen path=ni-5412-postamplifier-attenuation.html language=enus -->
## TOPIC 00262: NI 5412 Postamplifier Attenuation

- bundle_id: `ni-fgen`
- source_path: `ni-5412-postamplifier-attenuation.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5412-postamplifier-attenuation.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The postamplifier attenuation section is after the High-Gain and Low-Gain Amplifiers in the analog path. The attenuators provide a range of attenuation from 0 dB to a maximum of 36 dB in steps of 12 dB. NI-FGEN automatically controls the value of attenuation set in the postamplifier attenuation sect

### NI 5412 Postamplifier Attenuation

The postamplifier attenuation section is after the
High-Gain and Low-Gain Amplifiers in the *analog path*. The attenuators provide a
range of attenuation from 0 dB to a maximum of 36 dB in steps
of 12 dB. NI-FGEN automatically controls the value of attenuation
set in the postamplifier attenuation section dependent on the set
gain. You can read the value NI-FGEN has selected for postamplifier
attenuation using the 
Post-Amplifier Attenuation property or the 
NIFGEN_ATTR_POST_AMPLIFIER_ATTENUATION attribute.

Parent topic:

NI 5412 Attenuation

Related concepts:

- NI 5412 Analog Output

<!--NI_TOPIC bundle=ni-fgen path=ni-5412-power-up-and-reset-conditions.html language=enus -->
## TOPIC 00263: NI 5412 Power-Up and Reset Conditions

- bundle_id: `ni-fgen`
- source_path: `ni-5412-power-up-and-reset-conditions.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5412-power-up-and-reset-conditions.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The signal generator is in the following state from the time at which the computer begins to power up until the operating system is fully booted and NI-FGEN is loaded. The CH 0 analog output connector is disabled and has 50 Ω or 75 Ω impedance to ground. This impedance is the same as its previous se

### NI 5412 Power-Up and Reset Conditions

The signal generator is in the following state from
the time at which the computer begins to power up until the operating system is
fully booted and NI-FGEN is loaded.

- The CH 0 analog output connector is disabled and has
50 Ω or 75 Ω impedance to ground. This
impedance is the same as its previous setting before the device was
powered down. The output voltage amplitude of this connector
is 0 V.
- The CLK IN connector has 50 Ω impedance to
ground.
- PFI 0 and PFI 1 are tristated and have a 1
kΩ impedance to ground.

- PXI trigger or RTSI lines are tristated and floating.

After the operating system is fully booted and
NI-FGEN is loaded, or when you perform a hard reset to the device
directly from MAX or using NI-FGEN, the signal generator is in the
following state:

- CH 0 output is enabled.
- CH 0 output attenuation is set to 0 dB.
- Output impedance is set to 50 Ω.
- The Low-Gain Amplifier path is enabled in the Analog Output
path.
- The analog filter is disabled.

- The digital filter of the NI 5412
inside the DAC is disabled.

- CLK IN is disabled and has a 50 Ω
impedance to ground.
- PFI 0 and PFI 1 are tristated and have a 1
kΩ impedance to ground.

- PXI trigger or RTSI lines are tristated and floating.
- The sample rate is set to the maximum rate, with the Sample
clock source set to the internal Sample clock timebase.
- The Sample clock timebase is tuned by the internal reference
control voltage.

Parent topic:

NI 5412 NI 5412 Overview

<!--NI_TOPIC bundle=ni-fgen path=ni-5412-preamplifier-attenuation.html language=enus -->
## TOPIC 00264: NI 5412 Preamplifier Attenuation

- bundle_id: `ni-fgen`
- source_path: `ni-5412-preamplifier-attenuation.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5412-preamplifier-attenuation.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The preamplifier attenuation section is before the Low-Gain and High-Gain amplifiers in the analog path. The attenuators provide a range of attenuation from 0 to a maximum of 12 dB in steps of 3 dB. NI-FGEN automatically controls the value of attenuation set in the preamplifier attenuation section d

### NI 5412 Preamplifier Attenuation

The preamplifier attenuation section is before the
Low-Gain and High-Gain amplifiers in the *analog path*. The attenuators provide a
range of attenuation from 0 to a maximum of 12 dB in steps of
3 dB. NI-FGEN automatically controls the value of attenuation set
in the preamplifier attenuation section depending on the set
gain. You can read the value NI-FGEN has selected for preamplifier attenuation using the 
Pre-Amplifier Attenuation property or the 
NIFGEN_ATTR_PRE_AMPLIFIER_ATTENUATION attribute.

Preamplifier attenuation improves the signal
distortion because amplifiers provide lower distortion performance
with smaller signals. However, attenuation lowers the amplitude of
both the signal and the noise in a signal as the signal-to-noise
ratio (SNR) is unchanged upon attenuation. Amplifiers also have a
fixed noise associated with them. The total noise at the amplifier
output is obtained by taking the root of the sum of squares of the
following factors:

- The input signal noise multiplied by the gain of the
amplifier
- The amplifier noise

The total noise is dominated by the larger factor.
If the signal is attenuated so that its noise when multiplied by
gain at the amplifier input is smaller than the amplifier noise,
then the output has a higher SNR. This higher SNR is a good reason
to implement some of the signal generator overall attenuation as preamplifier
attenuation.

Parent topic:

NI 5412 Attenuation

Related concepts:

- NI 5412 Analog Output

<!--NI_TOPIC bundle=ni-fgen path=ni-5412-pxi-block-diagram.html language=enus -->
## TOPIC 00265: NI 5412 PXI Block Diagram

- bundle_id: `ni-fgen`
- source_path: `ni-5412-pxi-block-diagram.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5412-pxi-block-diagram.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: This topic contains information about the NI PXI-5412 top-level block diagram and descriptions of the individual blocks. If it is installed in any slot other than Slot 2 of the PXI chassis, the NI 5412 can receive a signal on the PXI_STAR line and can route a signal on the PXI_STAR line back to Sl

### NI 5412 PXI Block Diagram

This topic contains information about the
NI PXI-5412 top-level block diagram and descriptions of the
individual blocks.

[IMAGE alt='image' src='GUID-A93B1A01-DF0B-427D-8294-AA9B6C33D396-a5.gif']

Note

The following list describes the individual
blocks:

- Onboard Memory stores the waveform data and generation
instructions that you load into the device.
- Clocking allows you to create your Sample clock and
Reference clock.
- The 
 Waveform Generation Engine retrieves the waveform data and
instructions from the 
 Onboard Memory using the Sample clock. The 
 Waveform Generation Engine also uses this clock to
retrieve triggers from 
 Trigger and Event Control .
- The output from the 
 Waveform Generation Engine is sent to the 
 DAC device after any digital gain is applied.
- The 
 DAC also contains a selectable 
 Digital Filter , which interpolates and filters the
waveform data.
- The waveform data is sent from the 
 DAC to the 
 Analog Output path where the waveform data is
amplified.
- The 
 Routing Matrix allows flexible routing of the PXI Trigger
lines (RTSI) and the external PFI lines.

Parent topic:

NI 5412 Theory of Operation

<!--NI_TOPIC bundle=ni-fgen path=ni-5412-sample-size-and-resolution.html language=enus -->
## TOPIC 00266: NI 5412 Sample Size and Resolution

- bundle_id: `ni-fgen`
- source_path: `ni-5412-sample-size-and-resolution.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5412-sample-size-and-resolution.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5412 stores arbitrary waveforms in memory as signed 16-bit digital words. On the NI 5412, the upper 14 bits are sent to the digital gain circuit, the digital filter, and the DAC. Related Topics Onboard Memory Waveform Sizes

### NI 5412 Sample Size and Resolution

The NI 5412 stores arbitrary
waveforms in memory as signed 16-bit digital words. On the NI 5412,
the upper 14 bits are sent to the digital gain circuit, the digital
filter, and the DAC.

Related Topics

*Onboard Memory*

*Waveform Sizes*

Parent topic:

NI 5412 Waveform Generation

Related concepts:

- NI 5412 Onboard Memory
- NI 5412 Waveform Size and Quantum

<!--NI_TOPIC bundle=ni-fgen path=ni-5412-signal-routing.html language=enus -->
## TOPIC 00267: NI 5412 Signal Routing

- bundle_id: `ni-fgen`
- source_path: `ni-5412-signal-routing.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5412-signal-routing.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: An NI signal generator is capable of sending and receiving signals through the front panel and the PXI or RTSI trigger bus. The front panel connectors provides connectivity for the output channel as well as for control lines for sending and receiving clocks, triggers, and events. You can use the PXI

### NI 5412 Signal Routing

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
2. Expand Devices and Interfaces . 

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

NI 5412 Theory of Operation

Related concepts:

- NI 5412 Syntax for Terminal Names

<!--NI_TOPIC bundle=ni-fgen path=ni-5412-single-trigger-mode.html language=enus -->
## TOPIC 00268: NI 5412 Single Trigger Mode

- bundle_id: `ni-fgen`
- source_path: `ni-5412-single-trigger-mode.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5412-single-trigger-mode.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: When your application is configured for Single trigger mode, only one Start trigger is required to begin waveform generation. All Start triggers after the first Start trigger are ignored. Once the waveform generation is complete, the analog output indefinitely settles at the DC value of the last sam

### NI 5412 Single Trigger Mode

When your application is configured for Single
trigger mode, only one Start trigger is required to begin waveform
generation. All Start triggers after the first Start trigger are
ignored. Once the waveform generation is complete, the analog
output indefinitely settles at the DC value of the last sample in
the waveform.

| Output Mode | Trigger Behavior |
| --- | --- |
| Arbitrary Waveform Mode | The waveform you downloaded generates only once and waveform generation halts, unless the Arbitrary Waveform Repeat Count property or the NIFGEN_ATTR_ARB_REPEAT_COUNT attribute is set, in which case the waveform generates the specified number of times. |
| Arbitrary Sequence Mode | The waveform pattern you define in the sequence list generates only once. When a Start trigger is received, generation begins at the first segment and continues through the last segment, after which the waveform generation halts. You can determine the DC value at which waveform generation ends by configuring the last point in the final segment as the desired DC value, or you can add an extra segment filled with the same DC value. |

Parent topic:

NI 5412 Trigger Modes

<!--NI_TOPIC bundle=ni-fgen path=ni-5412-specifications.html language=enus -->
## TOPIC 00269: NI 5412 Specifications

- bundle_id: `ni-fgen`
- source_path: `ni-5412-specifications.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5412-specifications.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: For information about the signal generator specifications, refer to the device specifications. You can access these specifications by navigating to Start»All Programs»National Instruments» NI-FGEN»Documentation»NI Signal Generators Specifications, or you can visit ni.com/manuals.

### NI 5412 Specifications

For information about the signal generator
specifications, refer to the 
*device
specifications*. You can access these specifications by
navigating to 
Start»All Programs»National Instruments»
NI-FGEN»Documentation»NI Signal Generators Specifications, or you can visit 
ni.com/manuals.

Parent topic:

NI 5412 NI 5412 Overview

<!--NI_TOPIC bundle=ni-fgen path=ni-5412-standard-function-mode.html language=enus -->
## TOPIC 00270: NI 5412 Standard Function Mode

- bundle_id: `ni-fgen`
- source_path: `ni-5412-standard-function-mode.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5412-standard-function-mode.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Standard Function output mode is used to generate standard function waveforms such as sine, square, triangle, and so on. On the NI 5412, Standard Function mode is implemented primarily in software. NI-FGEN creates and downloads standard function waveforms to arbitrary waveform memory and generates t

### NI 5412 Standard Function Mode

Standard Function output mode is used to generate standard
function waveforms such as sine, square, triangle, and so on. 
On the NI 5412, *Standard Function mode* is implemented primarily in software. NI-FGEN creates and downloads standard function waveforms to arbitrary waveform memory and generates them the same way that it generates arbitrary waveforms. NI-FGEN automatically selects the best clock mode, sample rate, and buffer size to produce the most accurate waveform possible.

Parent topic:

NI 5412 Output Modes

Related concepts:

- Standard Function Mode

<!--NI_TOPIC bundle=ni-fgen path=ni-5412-stepped-trigger-mode.html language=enus -->
## TOPIC 00271: NI 5412 Stepped Trigger Mode

- bundle_id: `ni-fgen`
- source_path: `ni-5412-stepped-trigger-mode.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5412-stepped-trigger-mode.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The waveform you downloaded generates each time a Start trigger occurs. After a waveform finishes generating, the last sample of the waveform repeats continuously until the next Start trigger is received. When the next Start trigger is received, the waveform generates again. If a Start trigger is re

### NI 5412 Stepped Trigger Mode

The waveform you downloaded generates each time a
Start trigger occurs. After a waveform finishes generating, the
last sample of the waveform repeats continuously until the next
Start trigger is received. When the next Start trigger is received,
the waveform generates again. If a Start trigger is received while
a waveform is generating, the Start trigger is ignored and another
Start trigger is required to regenerate the waveform after the last
sample generates.

| Output Mode | Trigger Behavior |
| --- | --- |
| Arbitrary Waveform Mode | If the Arbitrary Waveform Repeat Count property or the NIFGEN_ATTR_ARB_REPEAT_COUNT attribute is set, the waveform generates the specified number of times instead of just once. |
| Arbitrary Sequence Mode | The waveforms you define in the sequence list generate one segment at a time, each time a Start trigger occurs. The waveform loops as many times as has been configured for that particular segment. After the generation of a segment has halted, the last sample of the waveform repeats continuously until the next Start trigger is received. After the sequence list is exhausted, the waveform generation returns to the first segment and subsequent Start triggers restart the process. |

Parent topic:

NI 5412 Trigger Modes

<!--NI_TOPIC bundle=ni-fgen path=ni-5412-synchronization.html language=enus -->
## TOPIC 00272: NI 5412 Synchronization

- bundle_id: `ni-fgen`
- source_path: `ni-5412-synchronization.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5412-synchronization.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Your signal generator is based on the National Instruments Synchronization and Memory Core (SMC) technology and therefore supports TClk synchronization. Refer to the NI-TClk Synchronization Help for more information about NI-TClk Synchronization.

### NI 5412 Synchronization

Your signal generator is based on the 
National Instruments
Synchronization and Memory Core (SMC) technology and therefore
supports TClk synchronization. Refer to the 
NI-TClk
Synchronization Help for more information about NI-TClk
Synchronization.

Parent topic:

NI 5412 NI 5412 Overview

<!--NI_TOPIC bundle=ni-fgen path=ni-5412-syntax-for-terminal-names.html language=enus -->
## TOPIC 00273: NI 5412 Syntax for Terminal Names

- bundle_id: `ni-fgen`
- source_path: `ni-5412-syntax-for-terminal-names.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5412-syntax-for-terminal-names.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The syntax for terminal names is a unique identifier that refers to a physical terminal in your system. To guarantee the uniqueness of a terminal name across multiple devices, terminal names begin with a forward slash, followed by the name of the device as configured in MAX, such as Dev1. A forward

### NI 5412 Syntax for Terminal Names

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

NI 5412 Signal Routing

<!--NI_TOPIC bundle=ni-fgen path=ni-5412-theory-of-operation.html language=enus -->
## TOPIC 00274: NI 5412 Theory of Operation

- bundle_id: `ni-fgen`
- source_path: `ni-5412-theory-of-operation.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5412-theory-of-operation.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Expand this topic for information about the theory of operation of your signal generator.

### NI 5412 Theory of Operation

Expand this topic for information about the theory
of operation of your signal generator.

Parent topic:

NI 5412 NI 5412 Overview

<!--NI_TOPIC bundle=ni-fgen path=ni-5412-thermal-shutdown.html language=enus -->
## TOPIC 00275: NI 5412 Thermal Shutdown

- bundle_id: `ni-fgen`
- source_path: `ni-5412-thermal-shutdown.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5412-thermal-shutdown.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: NI-FGEN supports thermal shutdown capability for the NI 5412. This capability allows the signal generator to detect when it has reached a dangerously high temperature and to then power down to prevent damage to the device. Air circulation paths, fan settings, and space allowances are several factors

### NI 5412 Thermal Shutdown

NI-FGEN supports thermal shutdown capability for
the NI 5412. This
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

NI 5412 NI 5412 Overview

<!--NI_TOPIC bundle=ni-fgen path=ni-5412-trigger-modes.html language=enus -->
## TOPIC 00276: NI 5412 Trigger Modes

- bundle_id: `ni-fgen`
- source_path: `ni-5412-trigger-modes.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5412-trigger-modes.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5412 has four trigger modes: Single, Continuous, Stepped, and Burst. These trigger modes are available for Arbitrary Waveform, Arbitrary Sequence, and Frequency List output mode. Refer to the niFgen Configure Trigger Mode VI or the niFgen_ConfigureTriggerMode function for information about se

### NI 5412 Trigger Modes

The NI 5412 has four trigger modes: Single, Continuous, Stepped,
and Burst. These trigger modes are available for Arbitrary
Waveform, Arbitrary Sequence, and Frequency List output mode.
Refer to the 
niFgen
Configure Trigger Mode VI or the 
niFgen_ConfigureTriggerMode function for information about setting the trigger mode.

Parent topic:

NI 5412 Triggering

<!--NI_TOPIC bundle=ni-fgen path=ni-5412-trigger-sources.html language=enus -->
## TOPIC 00277: NI 5412 Trigger Sources

- bundle_id: `ni-fgen`
- source_path: `ni-5412-trigger-sources.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5412-trigger-sources.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Trigger sources are software selectable. You can use any of the following external input triggers: PFI 0 or PFI 1 on the front panel connectors RTSI<0..7> (PCI) lines or PXI_TRIG<0..7> lines and PXI_STAR on the PXI trigger bus backplane The following figure shows the possible trigger sources for the

### NI 5412 Trigger Sources

Trigger sources are software selectable. You can
use any of the following external input triggers:

- PFI 0 or PFI 1 on the front panel connectors

- RTSI<0..7> (PCI) lines or PXI_TRIG<0..7> lines and
PXI_STAR on the PXI trigger bus backplane

The following figure shows the possible trigger
sources for the NI 5412.

[IMAGE alt='image' src='GUID-1C4628B0-B1AB-4165-B6B6-0E91EB739FBA-a5.gif']

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

*PXI Star Trigger
Line*

Parent topic:

NI 5412 Triggering

Related concepts:

- NI 5412 Exporting Signals
- PXI Trigger Lines
- PXI Star Trigger Line

<!--NI_TOPIC bundle=ni-fgen path=ni-5412-trigger-timing.html language=enus -->
## TOPIC 00278: NI 5412 Trigger Timing

- bundle_id: `ni-fgen`
- source_path: `ni-5412-trigger-timing.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5412-trigger-timing.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the relationship between Start trigger and the waveform output. t[s1] is the required pulse width on the Start trigger signal. t[s2] is the delay from the Start trigger to the waveform output. Refer to the NI PXI/PCI-5412 Specifications for more information about these tim

### NI 5412 Trigger Timing

The following figure shows the relationship between
Start trigger and the waveform output. t<sub>s1</sub> is the required pulse width on the Start trigger
signal. t<sub>s2</sub> is the delay from the Start trigger to the waveform
output. Refer to the 
*NI PXI/PCI-5412
Specifications* for more information about these timing
parameters.

[IMAGE alt='image' src='GUID-9DD6A51C-2BCA-4129-9C8D-0A821181925F-a5.gif']

The NI 5412 also allows you to export
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

NI 5412 Triggering

<!--NI_TOPIC bundle=ni-fgen path=ni-5412-triggering.html language=enus -->
## TOPIC 00279: NI 5412 Triggering

- bundle_id: `ni-fgen`
- source_path: `ni-5412-triggering.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5412-triggering.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can define the signal generator functionality by using the various triggering techniques. Expand this section to learn more about using triggers with your signal generator.

### NI 5412 Triggering

You can define the signal generator functionality
by using the various triggering techniques. Expand this section to
learn more about using triggers with your signal generator.

Parent topic:

NI 5412 NI 5412 Overview

<!--NI_TOPIC bundle=ni-fgen path=ni-5412-waveform-amplitude-control.html language=enus -->
## TOPIC 00280: NI 5412 Waveform Amplitude Control

- bundle_id: `ni-fgen`
- source_path: `ni-5412-waveform-amplitude-control.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5412-waveform-amplitude-control.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5412 uses both amplifiers and attenuators to achieve required amplitude settings. Output Paths and Amplifiers The following figure shows two different gain paths: the Direct path and the Main path with High-Gain and Low-Gain amplifiers. The Low-Gain Amplifier path has a 2 V[pk-pk] amplifier a

### NI 5412 Waveform Amplitude Control

The NI 5412 uses both amplifiers and
attenuators to achieve required amplitude settings.

#### Output Paths and Amplifiers

The following figure shows two different gain
paths: the Direct path and the Main path with High-Gain and Low-Gain amplifiers.

[IMAGE alt='image' src='GUID-6D4C36D6-D454-4961-979E-9F00D4097CE0-a5.gif']

The 
 Low-Gain Amplifier path has a 
2 V<sub>pk-pk</sub> amplifier and is used for waveforms that
have all output voltages equal to or smaller than 
2.0 V<sub>pk-pk</sub> into matched load impedance.
The High-Gain
Amplifier path has a 12 V<sub>pk-pk</sub> amplifier and is used for waveforms that have output voltages greater than 2.0 V<sub>pk-pk</sub> into matched load impedance. The gains of the amplifiers are constant. NI-FGEN automatically selects by default
between the high-gain and low-gain amplifiers, depending on the
NI-FGEN gain setting. You can configure the gain by calling the 
Arbitrary Waveform Gain or 
Amplitude
property or the 
NIFGEN_ATTR_ARB_GAIN or
NIFGEN_ATTR_FUNC_AMPLITUDE attribute.

You can configure the High-Gain or the Low-Gain
Amplifiers to remain in the Analog Output path regardless of gain
setting by calling the 
Analog Path
property or the 
NIFGEN_ATTR_ANALOG_PATH attribute. Configuring the Low-Gain
Amplifier path to remain constant regardless of the gain setting
affects the maximum output value allowable for that particular gain
setting. The maximum gain setting for an Analog Output path
configured to Low-Gain Amplifier path is 
 1.0. The maximum allowable
gain setting with NI-FGEN automatically selecting the Gain
Amplifier path is 
 6.0. Gain is a unitless value.

In addition, the DC offset amplifier, which adds 
*DC offset* to the signal, is
located in the High-Gain and Low-Gain Amplifier paths prior to the
attenuators and amplifiers. The DC offset amplifier can be
fine-tuned to add offset to your signal. This fine-tuning of the
main DC offset amplifier is performed by the offset DAC.

Parent topic:

NI 5412 Analog Output

Related concepts:

- NI 5412 DC Offset

<!--NI_TOPIC bundle=ni-fgen path=ni-5412-waveform-and-generation-instruction-m.html language=enus -->
## TOPIC 00281: NI 5412 Waveform and Generation Instruction Memory Size

- bundle_id: `ni-fgen`
- source_path: `ni-5412-waveform-and-generation-instruction-m.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5412-waveform-and-generation-instruction-m.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Waveform Memory Size Waveforms are stored in the NI 5412 onboard memory in contiguous blocks. These blocks are allocated in multiples of 128 bytes. This allocation style means that while waveform sizes may be multiples of four samples (eight bytes) on the NI 5412 , the amount of onboard memory alloc

### NI 5412 Waveform and Generation Instruction Memory Size

#### Waveform Memory Size

Waveforms are stored in the
NI 5412 onboard memory in contiguous
blocks. These blocks are allocated in multiples of 128 bytes. This
allocation style means that while waveform sizes may be multiples
of four samples (eight bytes) on the NI 5412
, the amount of
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
2. Memory is written to in blocks of 128 bytes.

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

The NI 5412 uses a
waveform generation engine that processes instructions that govern
how a waveform or a sequence of waveforms is generated. These
instructions determine which waveforms are generated, how the
device responds to triggers, how many times a waveform is looped,
when Marker events are generated, and so forth. The instructions
depend on the output mode, trigger mode, trigger source, waveforms
in onboard memory, and sequence lists that are configured. The
instructions are stored in the onboard memory along with the
waveform data. The calculations to determine the instruction size
that is stored in the onboard memory depends on the NI-FGEN output
mode and the NI-FGEN trigger mode. The following table includes
basic equations for determining the amount of memory, in bytes,
that are used for the different generation configurations.

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

Parent topic:

NI 5412 Onboard Memory

<!--NI_TOPIC bundle=ni-fgen path=ni-5412-waveform-generation.html language=enus -->
## TOPIC 00282: NI 5412 Waveform Generation

- bundle_id: `ni-fgen`
- source_path: `ni-5412-waveform-generation.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5412-waveform-generation.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5412 supports the following output, or generation, modes: Standard Function Arbitrary Waveform Arbitrary Sequence To select an output mode, set the Output Mode parameter of the niFgen Configure Output Mode VI or the niFgen_ConfigureOutputMode function.

### NI 5412 Waveform Generation

The NI 5412 supports the
following output, or generation, modes:

- Standard Function
- Arbitrary Waveform
- Arbitrary Sequence

To select an output mode, set the 
Output Mode parameter of the 
niFgen
Configure Output Mode VI or the 
niFgen_ConfigureOutputMode function.

Parent topic:

NI 5412 NI 5412 Overview

Related concepts:

- NI 5412 Standard Function Mode
- NI 5412 Arbitrary Waveform Mode
- NI 5412 Arbitrary Sequence Mode

<!--NI_TOPIC bundle=ni-fgen path=ni-5412-waveform-quantum.html language=enus -->
## TOPIC 00283: NI 5412 Waveform Quantum

- bundle_id: `ni-fgen`
- source_path: `ni-5412-waveform-quantum.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5412-waveform-quantum.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Quantum is the increment in samples that waveform sizes must adhere to. Waveforms must be downloaded in integer multiples of the four samples (or two for complex samples), the quantum for the NI 5412. For example, if while in Arbitrary Waveform mode, you request to load a waveform of seven samples,

### NI 5412 Waveform Quantum

Quantum is the increment in samples that waveform
sizes must adhere to. Waveforms must be downloaded in integer multiples of the four samples (or two for complex samples), the quantum for the NI 5412.

For example, if while in Arbitrary Waveform mode, you request to load a waveform of seven samples, the task will not complete successfully because the waveform is not an integer multiple of the quantum size. Waveform sizes that meet the conditions include 4, 8, 12, 16, 20, and so on, up to maximum allowable waveform size.

Parent topic:

NI 5412 Waveform Size and Quantum

<!--NI_TOPIC bundle=ni-fgen path=ni-5412-waveform-size-and-quantum.html language=enus -->
## TOPIC 00284: NI 5412 Waveform Size and Quantum

- bundle_id: `ni-fgen`
- source_path: `ni-5412-waveform-size-and-quantum.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5412-waveform-size-and-quantum.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5412 onboard memory architecture imposes certain requirements on the waveform size and quantum.

### NI 5412 Waveform Size and Quantum

The NI 5412 onboard memory architecture
imposes certain requirements on the waveform *size* and *quantum*.

Parent topic:

NI 5412 Waveform Generation

Related concepts:

- NI 5412 Waveform Size
- NI 5412 Waveform Quantum

<!--NI_TOPIC bundle=ni-fgen path=ni-5412-waveform-size.html language=enus -->
## TOPIC 00285: NI 5412 Waveform Size

- bundle_id: `ni-fgen`
- source_path: `ni-5412-waveform-size.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5412-waveform-size.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Minimum Waveform Size The minimum waveform size on the NI 5412 depends on the output mode and the trigger mode. Refer to the device specifications for the minimum waveform size values for the different modes. To provide greater programming flexibility, NI-FGEN does not strictly enforce the minimum

### NI 5412 Waveform Size

#### Minimum Waveform Size

The
minimum waveform size on the NI 5412 depends on the output mode and the 
*trigger mode*. Refer to
the 
*device
specifications* for the minimum waveform size values for the
different modes.

Note

device
specifications

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

NI 5412 Waveform Size and Quantum

Related concepts:

- NI 5412 Trigger Modes
- NI 5412 Waveform and Generation Instruction Memory Size

<!--NI_TOPIC bundle=ni-fgen path=ni-5421-aborting-generation.html language=enus -->
## TOPIC 00286: NI 5421 Aborting Generation

- bundle_id: `ni-fgen`
- source_path: `ni-5421-aborting-generation.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5421-aborting-generation.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can abort the generation of the current waveform. Aborting the generation exhibits different behaviors for different waveform output modes. Output Mode Abort Behavior Standard Function Abort to Ground—Signal remains at the level for which the DC offset is configured. Arbitrary Waveform, Arbitrar

### NI 5421 Aborting Generation

You can abort the generation of the current
waveform. Aborting the generation exhibits different behaviors for
different 
*waveform output
modes*.

| Output Mode | Abort Behavior |
| --- | --- |
| Standard Function | Abort to Ground—Signal remains at the level for which the DC offset is configured. |
| Arbitrary Waveform, Arbitrary Sequence, Script* | Abort to a Known Voltage—Signal remains at the last sample voltage level prior to the abort. |
| * These modes can also abort to ground. |  |

Related Topics

*Aborting to Ground*

*Aborting to a
Known Voltage*

Parent topic:

NI 5421 Waveform Generation

Related concepts:

- NI 5421 Waveform Generation
- Abort to Ground
- Abort to a Known Voltage

<!--NI_TOPIC bundle=ni-fgen path=ni-5421-access-and-active-leds.html language=enus -->
## TOPIC 00287: NI 5421 ACCESS and ACTIVE LEDs

- bundle_id: `ni-fgen`
- source_path: `ni-5421-access-and-active-leds.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5421-access-and-active-leds.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The ACCESS and ACTIVE LEDs indicate the status of the PXI module: ACCESS LED The ACCESS LED indicates basic hardware status as shown in the following table. Color Indications Off Device is not yet functional, or the device has detected a problem with a power rail. Amber The device is being accessed.

### NI 5421 ACCESS and ACTIVE LEDs

The ACCESS and ACTIVE LEDs indicate the status of
the PXI module:

#### ACCESS LED

The ACCESS LED indicates basic hardware status as
shown in the following table.

| Color | Indications |
| --- | --- |
| Off | Device is not yet functional, or the device has detected a problem with a power rail. |
| Amber | The device is being accessed. |
| Green | The device is ready to be programmed by NI-FGEN. |

#### ACTIVE LED

The ACTIVE LED indicates the device state as shown
in the following table.

| Color | Indications |
| --- | --- |
| Off | Device is not generating. |
| Amber | The device is armed and waiting for a trigger. |
| Green | The device has received a trigger. Also indicates that the device is generating a waveform. |
| Red | The device has detected an error. NI-FGEN must access the device to determine the cause of the error. The LED remains red until the error condition is removed. Example errors include the following: PLL Unlocked–The device has detected an unlocked condition on a previously locked PLL. A PLL that is unlocked while in reset does not show an error. The device has powered down because the internal temperature exceeded the maximum limit. The over-temperature condition must be corrected and the device reset. For more information about keeping your device cool, refer to the Maintain Forced-Air Cooling Note to Users included with your signal generator. To reset the device, call the niFgen Reset Device VI or the niFgen_ResetDevice function, or perform a device reset in MAX. |

Parent topic:

NI 5421 NI 5421 Overview

<!--NI_TOPIC bundle=ni-fgen path=ni-5421-accessories.html language=enus -->
## TOPIC 00288: NI 5421 Accessories

- bundle_id: `ni-fgen`
- source_path: `ni-5421-accessories.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5421-accessories.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: National Instruments offers a variety of products to use with your signal generator, including cables and other accessories. Visit ni.com for more information.

### NI 5421 Accessories

National Instruments offers a variety of products
to use with your signal generator, including cables and other
accessories. Visit 
ni.com for more
information.

Parent topic:

NI 5421 NI 5421 Overview

<!--NI_TOPIC bundle=ni-fgen path=ni-5421-analog-filter.html language=enus -->
## TOPIC 00289: NI 5421 Analog Filter

- bundle_id: `ni-fgen`
- source_path: `ni-5421-analog-filter.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5421-analog-filter.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The analog filter is a lowpass filter that is used to eliminate aliased images and artifacts due to the digital-to-analog conversion from the signal from the DAC. In general, use the analog filter for signals containing a large portion of sinusoidal content, such as AM and FM, sinc pulse, and sinuso

### NI 5421 Analog Filter

aliased images

niFgen_EnableAnalogFilter

niFgen_DisableAnalogFilter

Note

The delay from the time the device receives a Start
trigger to the time a signal is generated at the analog output
increases if the analog filter in the Analog Output path is
enabled. Refer to the 
*device
specifications* for information about the delay from the trigger
to the analog output based on the configured filter settings.

#### Related Topic

*Filtering and
Interpolation*

Parent topic:

NI 5421 Filtering Effects

Related concepts:

- Aliased Images
- Filtering and Interpolation

<!--NI_TOPIC bundle=ni-fgen path=ni-5421-analog-gain-settings.html language=enus -->
## TOPIC 00290: NI 5421 Analog Gain Settings

- bundle_id: `ni-fgen`
- source_path: `ni-5421-analog-gain-settings.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5421-analog-gain-settings.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following table summarizes the maximum and minimum gain setting that you can apply for the NI-FGEN analog path options. Refer to the device specifications for more information about gain resolution. Analog Path Gain Summary (Matched Load Impedance) NI-FGEN Analog Path Maximum Gain Value Minimum

### NI 5421 Analog Gain Settings

The following table summarizes the maximum and
minimum gain setting that you can apply for the NI-FGEN analog path
options. Refer to the 
*device
specifications* for more information about gain resolution.

| Analog Path Gain Summary (Matched Load Impedance) |  |  |
| --- | --- | --- |
| NI-FGEN Analog Path | Maximum Gain Value | Minimum Gain Value |
| Automatic (default) | 6.000 | 2.817 m |
| Fixed Low-Gain Amplifier | 1.027 | 2.817 m |
| Fixed High-Gain Amplifier | 6.000 | 16.91 m |
| Direct Path | 0.527 | 0.354 |
| Note: Gain is unitless. |  |  |

Note

Parent topic:

NI 5421 Waveform Amplitude Control

<!--NI_TOPIC bundle=ni-fgen path=ni-5421-analog-output.html language=enus -->
## TOPIC 00291: NI 5421 Analog Output

- bundle_id: `ni-fgen`
- source_path: `ni-5421-analog-output.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5421-analog-output.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the NI 5421 Analog Output signal path. NI 5421 analog waveforms are generated as follows: The 16-bit digital waveform data from the Waveform Generation Engine or OSP is passed to a digital gain circuit and then high-speed DAC. This DAC also implements a portion of the Anal

### NI 5421 Analog Output

The following figure shows the NI 5421 Analog Output signal path.

[IMAGE alt='image' src='GUID-1168A294-D930-4645-8DF7-E4E6E841D015-a5.gif']

NI 5421 analog waveforms are
generated as follows:

1. The 16-bit digital waveform data from the Waveform Generation
Engine or OSP is passed to a digital gain circuit and then
high-speed DAC. This DAC also implements a portion of the Analog
Output signal path attenuation with a range of 0 dB to
3 dB. Refer to the NI PXI/PCI-5421 Specifications for the exact resolution. You can adjust the amount
of attenuation by configuring the 
Arbitrary
Waveform Gain or 
Amplitude
properties or the 
 NIFGEN_ATTR_ARB_GAIN or 
 NIFGEN_ATTR_FUNC_AMPLITUDE attributes. NI-FGEN calculates and sets the correct amount of
attenuation required, corresponding to the gain setting.
2. Following the DAC, the signal can take one of two paths: the
Direct path or the Main path with High-Gain and Low-Gain
amplifiers. NI-FGEN selects the Main path by default. To select the
Direct path manually, use the 
Analog Path
property or the 
 NIFGEN_ATTR_ANALOG_PATH attribute.
  1. The Direct path bypasses the Analog Filter, the attenuation
sections, and the amplifiers. Taking the amplifiers out of the
signal path yields an output signal with the lowest distortion and
a flat frequency response. Use the Direct path for communication
signals. The Direct path can provide a maximum of 1 V pk-pk output into 50 Ω with no offset and a
maximum of 3 dB attenuation. A signal taking the Direct path
skips steps 3 through 5 and continues at step 6.
  2. If the Main path is selected, the
signal passes through a switchable lowpass Analog Filter,
attenuators, and amplifiers.
3. The signal then passes through a switchable lowpass Analog
Filter to remove 
 Aliased Images . You can
select whether to include the Analog Filter in the Analog Output
path using either the 
niFgen
Configure Analog Filter VI or the 
 niFgen_EnableAnalogFilter or 
 niFgen_DisableAnalogFilter functions.
4. The signal then passes through the DC Offset Amplifier that
adds the desired DC offset voltage. You can adjust the amount of DC
offset added to the signal, up to one half the value of the NI-FGEN
gain setting by using either the 
Arbitrary
Waveform Offset or 
DC Offset
properties or the 
 NIFGEN_ATTR_ARB_OFFSET or 
 NIFGEN_ATTR_FUNC_DC_OFFSET attributes.
5. The signal then passes through the Preamplifier Attenuation section,
a set of selectable solid-state attenuators that provide 0 dB
to 12 dB of attenuation in 3 dB increments. You can adjust the
amount of attenuation by adjusting the Arbitrary Waveform Gain
property or the 
 NIFGEN_ATTR_ARB_GAIN attribute.
NI-FGEN calculates and sets the correct amount of attenuation
required, corresponding to the gain setting configured with the 
Arbitrary
Waveform Gain or 
Amplitude
properties, or the 
 NIFGEN_ATTR_ARB_GAIN or 
 NIFGEN_ATTR_FUNC_AMPLITUDE attributes.
6. Following the Preamplifier Attenuation section, the signal can take
one of two paths: the High-Gain or Low-Gain Amplifier path. The High-Gain Amplifier path is used for waveform output
voltages greater than ±1.0 V into 50 Ω. The
amplifier has a fixed gain and is included in the signal path to
enable the AWG to provide the maximum V pk-pk . The Low-Gain Amplifier path is used for waveforms that have all
output voltages equal to or smaller than ±1.0 V into
50 Ω. The amplifier has a fixed gain. NI-FGEN
automatically selects the best amplifier path between the High-Gain
and Low-Gain amplifiers by default based on the gain or amplitude
setting. Alternatively, you can use the 
Analog Path
property or the 
 NIFGEN_ATTR_ANALOG_PATH attribute to set the signal path to remain
constant regardless of the gain setting for applications requiring
one path or the other.
7. The signal passes through the Postamplifier Attenuation section, a
set of two passive attenuators 12 dB and 24 dB. You can adjust the
amount of attenuation by configuring either the 
Arbitrary
Waveform Gain or 
Amplitude
properties, or the 
 NIFGEN_ATTR_ARB_GAIN or 
 NIFGEN_ATTR_FUNC_AMPLITUDE attributes. NI-FGEN calculates and sets the correct amount of
attenuation required, corresponding to the gain setting.
8. The signal then passes through the Output Enable relay. When
the Output Enable relay is disabled, ground is connected to the
output through a 50 Ω or a 75 Ω resistor.
Intentionally, waveform generation continues while the output
enable relay is disabled. When the relay is enabled, the analog
waveform is seen at the CH 0 connector. You can enable or
disable the output of the analog waveform generator by using the 
niFgen Output
Enable VI or the 
 niFgen_ConfigureOutputEnabled function.
9. The signal then passes through a
50 Ω/75 Ω selector to the
CH 0 connector. You can configure the output impedance of
the analog waveform generator by using the 
niFgen
Configure Output Impedance VI or the 
 niFgen_ConfigureOutputImpedance function.

Note

Parent topic:

NI 5421 Theory of Operation

Related concepts:

- Aliased Images

<!--NI_TOPIC bundle=ni-fgen path=ni-5421-arbitrary-sequence-mode.html language=enus -->
## TOPIC 00292: NI 5421 Arbitrary Sequence Mode

- bundle_id: `ni-fgen`
- source_path: `ni-5421-arbitrary-sequence-mode.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5421-arbitrary-sequence-mode.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Arbitrary Sequence mode allows you to load multiple waveforms in the onboard memory of the NI 5421. A finite number of samples make a waveform. To generate these downloaded waveforms in a specific order, you must prepare a sequence, which contains a number of segments in a specific order. Each segme

### NI 5421 Arbitrary Sequence Mode

*Arbitrary Sequence mode* allows you to load multiple
waveforms in the onboard memory of the NI 5421. A finite
number of samples make a waveform. To generate these downloaded
waveforms in a specific order, you must prepare a sequence, which
contains a number of segments in a specific order. Each segment
specifies a downloaded waveform, a number of loops to repeat the
selected waveform, and a numeric offset in which a marker is
generated by the device.

Parent topic:

NI 5421 Output Modes

Related concepts:

- Arbitrary Sequence Mode

<!--NI_TOPIC bundle=ni-fgen path=ni-5421-arbitrary-waveform-mode.html language=enus -->
## TOPIC 00293: NI 5421 Arbitrary Waveform Mode

- bundle_id: `ni-fgen`
- source_path: `ni-5421-arbitrary-waveform-mode.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5421-arbitrary-waveform-mode.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5421 supports Arbitrary Waveform output mode. Arbitrary Waveform mode generates waveforms from user-created/provided waveform arrays of numeric data. The waveform arrays are downloaded to the arbitrary waveform generator onboard memory. Arbitrary Waveform mode also uses memory to store the in

### NI 5421 Arbitrary Waveform Mode

The NI 5421 supports Arbitrary Waveform output mode. Arbitrary Waveform mode generates waveforms from
user-created/provided waveform arrays of numeric data. The waveform
arrays are downloaded to the arbitrary waveform generator onboard
memory. *Arbitrary Waveform mode* also uses memory to
store the instructions for generating waveform sequences in the
onboard memory.

Parent topic:

NI 5421 Output Modes

Related concepts:

- Arbitrary Waveform Output Mode

<!--NI_TOPIC bundle=ni-fgen path=ni-5421-attenuation.html language=enus -->
## TOPIC 00294: NI 5421 Attenuation

- bundle_id: `ni-fgen`
- source_path: `ni-5421-attenuation.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5421-attenuation.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Analog Output path has two passive attenuation sections. Preamplifier attenuation is prior to the High-Gain and Low-Gain Amplifier paths, and postamplifier attenuation is after the High-Gain and Low-Gain Amplifier paths. The main DAC provides 0 to 3 dB of signal attenuation. Amplitude control is

### NI 5421 Attenuation

The Analog Output path has two passive attenuation
sections. *Preamplifier attenuation* is prior to the High-Gain
and Low-Gain Amplifier paths, and *postamplifier attenuation* is after the
High-Gain and Low-Gain Amplifier paths.

The main *DAC* provides 0 to 3 dB of signal attenuation. Amplitude control is implemented after the DAC. Attenuating the DAC output signal allows you to vary the signal amplitude while maintaining the dynamic range of the DAC. You do not lose any bits from the digital representation of the signal and you do not sacrifice dynamic range, as you would if you control amplitude by using smaller data ranges of the DAC. Passive attenuation by preamplifier and postamplifier attenuation is not available if the Direct path is selected.

For the Low-Gain and the High-Gain Amplifier paths, maximum attenuation is
51 dB. For the Direct path, maximum output attenuation is 3
dB. NI-FGEN automatically determines the correct value of attenuation in dB and configures the attenuation based on the set
gain. The minimum gain setting for the Direct path is 0.354. The
minimum gain setting for an Analog Output path configured to
High-Gain Amplifier path is .01691. The minimum allowable gain
setting with NI-FGEN automatically selecting the Low-Gain Amplifier
path is .00282 (gain is a unitless value).

NI-FGEN calculates and sets the correct amount of
attenuation required that corresponds to your NI-FGEN gain setting.
The correct amount of attenuation is implemented in the 
preamplifier and postamplifier attenuation blocks to best achieve
the desired output signal amplitude. You can set the amount of gain
with the Arbitrary Waveform Gain property or the 
NIFGEN_ATTR_ARB_GAIN attribute.

Parent topic:

NI 5421 Waveform Amplitude Control

Related concepts:

- NI 5421 Preamplifier Attenuation
- NI 5421 Postamplifier Attenuation
- NI 5421 DAC Attenuation

<!--NI_TOPIC bundle=ni-fgen path=ni-5421-burst-trigger-mode.html language=enus -->
## TOPIC 00295: NI 5421 Burst Trigger Mode

- bundle_id: `ni-fgen`
- source_path: `ni-5421-burst-trigger-mode.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5421-burst-trigger-mode.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: In Burst trigger mode, calling the first Start trigger begins waveform generation. The waveform then generates continually. The following table provides more information about waveform generation behavior in Arbitrary Waveform and Arbitrary Sequence output modes. Output Mode Trigger Behavior Arbitra

### NI 5421 Burst Trigger Mode

In Burst trigger mode, calling the first Start
trigger begins waveform generation. The waveform then generates
continually. The
following table provides more information about
waveform generation behavior in Arbitrary Waveform and Arbitrary
Sequence output modes.

| Output Mode | Trigger Behavior |
| --- | --- |
| Arbitrary Waveform Mode | Burst trigger mode operates the same as Continuous trigger mode when the device is operating in Arbitrary Waveform mode. |
| Arbitrary Sequence Mode | Each waveform you define in the sequence list generates continuously until another Start trigger occurs. A Start trigger causes the waveform generation to switch to the waveform defined by the next segment, after the current waveform finishes. After the sequence list is exhausted, the waveform generation returns to the waveform defined by the first segment and subsequent Start triggers will restart the process. Only the first Start trigger which signals a transition to the next segment is recognized, all subsequent Start triggers are ignored until the currently generating waveform finishes. The transition of one waveform to the next can be made amplitude continuous if waveforms in all segments start and end at the same amplitude. Alternatively, this also can be accomplished by ensuring that the waveforms from one segment to the next end and start at the same amplitude. This amplitude continuous transition is shown in the previous Arbitrary Sequence Mode examples by the transitions of Segments 1 to Segment 2, and Segment 3 to Segment 4. The transition from Segment 2 to Segment 3 shows a discontinuous transition, going from a positive value on the last sample of the ramp waveform right to a midrange value of the sine waveform. |

Parent topic:

NI 5421 Trigger Modes

Related concepts:

- NI 5421 Continuous Trigger Mode

<!--NI_TOPIC bundle=ni-fgen path=ni-5421-calibration.html language=enus -->
## TOPIC 00296: NI 5421 Calibration

- bundle_id: `ni-fgen`
- source_path: `ni-5421-calibration.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5421-calibration.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Before shipping your signal generator, NI calibrated your device to ensure that all features are within specifications. Calibration is a set of operations that compares the values indicated by a measuring instrument or measuring system to the corresponding values realized by external standards. You

### NI 5421 Calibration

Before shipping your signal generator,
NI calibrated your device to ensure that all features are
within specifications.

Calibration is a set of operations that compares
the values indicated by a measuring instrument or measuring system
to the corresponding values realized by external standards. You can
use the results of calibration to determine the measurement error
and can then correct for it in the adjustment process.

The calibration process consists of verifying,
adjusting, and reverifying a device. During verification, you
compare the measured performance to an external standard of known
measurement uncertainty to confirm that the product meets or
exceeds specifications. During adjustment, you correct the
measurement error of the device by adjusting the calibration
constants and storing the new calibration constants in the EEPROM.
The host computer reads the calibration constants and the software
uses them to compensate for errors in the data and to present
calibrated data to the user.

For more information about calibrating the signal
generator, refer to the 
*device calibration*
procedures.

For more information about calibration in general,
refer to ni.com/calibration.

Parent topic:

NI 5421 NI 5421 Overview

<!--NI_TOPIC bundle=ni-fgen path=ni-5421-ch-0-connector.html language=enus -->
## TOPIC 00297: NI 5421 CH 0 Connector

- bundle_id: `ni-fgen`
- source_path: `ni-5421-ch-0-connector.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5421-ch-0-connector.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The CH 0 connector is the analog waveform output terminal. The maximum output levels from this connector depend on the type of load termination. For example, if the output of the device terminates into a 50 Ω load, the maximum output levels are ±6 V, while the maximum output levels are ±12 V when th

### NI 5421 CH 0 Connector

The CH 0 connector is the analog waveform
output terminal. The maximum output levels from this connector
depend on the type of load termination. For example, if the output of the device
terminates into a 50 Ω load, the maximum output levels
are ±6 V, while the maximum output levels are ±12 V when the
device terminates into a high-impedance load (HiZ). This difference
is illustrated in the following figure.

[IMAGE alt='image' src='GUID-836822F7-163C-475A-B0EB-3D94BB52CBAB-a5.gif']

If the output terminates into any other load, the
levels are defined by the following formula:

V<sub>out</sub>
 = ± [ 
R<sub>L</sub>
 / ( 
R<sub>L</sub>
 + 
R<sub>O</sub>
 ) ] × 12 V

where

V<sub>out</sub> is the maximum peak output voltage level

R<sub>L</sub>
 is the load impedance in ohms

O

Note

out

By default, 
R<sub>O</sub>
 = 50 Ω, but you can set the output
impedance to 75 Ω in NI-FGEN. You can configure the output impedance by calling the 
niFgen Configure Output Impedance VI or the 
niFgen_ConfigureOutputImpedance function.

You can set the amplitude of the generated output
signal in terms of peak voltage by setting the gain value. NI-FGEN
calculates and sets the correct amount of attenuation required for
the desired gain value. You can configure the output signal amplitude by calling the Amplitude property
 or NIFGEN_ATTR_FUNC_AMPLITUDE attribute, or the
 
Arbitrary Waveform Gain property or
NIFGEN_ATTR_ARB_GAIN attribute.

#### Load Impedance Compensation

The NI 5421 has the ability to configure the
output signal amplitude based on a user-configured load impedance
setting. This capability is desirable when you use the NI 5421
with loads that are between 0 Ω and a high impedance.
Refer to the 
*device
specifications* for information about the output impedance
tolerance.

By default, NI-FGEN assumes that the load impedance
is equal to the output impedance. If they do not match, you can
change the load impedance value that NI-FGEN uses in its load
impedance compensation algorithm. NI-FGEN takes the load impedance
into account when setting the amplitude and provides the amplitude
specified in the configured gain setting, eliminating the need to use
the voltage divider equation. NI-FGEN compensates to give the
desired peak-to-peak voltage amplitude or arbitrary gain (relative to 1 V). You can configure the load impedance by calling the 
Load
Impedance property or 
NIFGEN_ATTR_LOAD_IMPEDANCE attribute.

Note

For waveform output
signal specifications, refer to the 
*device
specifications*.

Parent topic:

NI 5421 NI 5421 Overview

<!--NI_TOPIC bundle=ni-fgen path=ni-5421-clk-in-connector.html language=enus -->
## TOPIC 00298: NI 5421 CLK IN Connector

- bundle_id: `ni-fgen`
- source_path: `ni-5421-clk-in-connector.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5421-clk-in-connector.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The CLK IN front panel connector can accept an external Reference clock, external Sample clock, or external Sample clock timebase. Do not change the external clocks while generating waveforms. Only modify the frequency of the external clock before you start the waveform generation or after you sto

### NI 5421 CLK IN Connector

Caution

not

before

after

#### External Reference Clock Input

The CLK IN connector can accept a Reference clock
from an external source and phase-lock the internal clock of the
signal generator to this external Reference clock. Refer to the 
*device
specifications* for the allowable Reference clock frequencies
and signal characteristics.

The Reference clock uses the internal clock by
default. Call the 
niFgen
Configure Reference Clock VI or the 
niFgen_ConfigureReferenceClock function to configure the Reference
clock source.

When configuring an external Reference clock, you
must configure the external Reference clock frequency if it is
different from the 10 MHz default setting. Set the Reference clock frequency with the 
niFgen
Configure Reference Clock VI or the niFgen_ConfigureReferenceClock function.

Note

PLL Reference
Sources

#### External Sample Clock Input

In addition to phase-locking, the CLK IN connector
also can receive an external Sample clock. Refer to the 
*device
specifications* for the allowable external Sample clock
frequencies and signal characteristics.

Tip

niFgen_ConfigureSampleRate

Configure the Sample clock source with 
niFgen
Configure Sample Clock Source VI or the 
niFgen_ConfigureSampleClockSource function. The Sample clock uses the internal clock by
default.

Parent topic:

NI 5421 NI 5421 Overview

Related concepts:

- NI 5421 Phase-Locked Loop Reference Clock

<!--NI_TOPIC bundle=ni-fgen path=ni-5421-clocking-options.html language=enus -->
## TOPIC 00299: NI 5421 Clocking Options

- bundle_id: `ni-fgen`
- source_path: `ni-5421-clocking-options.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5421-clocking-options.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Waveform generation is driven by the Sample clock; depending on your application, some sources may be better choices than others. You can use the following sources for the NI 5421 Sample clock: Internal Sample clock—the onboard clock is used as the Sample clock source and the Sample clock is derived

### NI 5421 Clocking Options

Waveform generation is driven by the Sample clock;
depending on your application, some sources may be better choices
than others. You can use the following sources for the
NI 5421 Sample clock:

- Internal Sample clock —the onboard clock is used as the
Sample clock source and the Sample clock is derived from the Sample
clock timebase via either Divide by N or High–Resolution clock
mode.
- External Sample clock —the Sample clock has an external
source that derives device clocking by directly driving the DAC and all waveform generation operations on the device.
- Reference clock —the Sample clock is derived from an
external source that is phase–locked to the Sample clock
timebase. The phase-locked loop (PLL) Reference clock source
specifies the source of the control voltage that tunes the VCXO of
the Sample clock timebase for internal clock update sources. The
PLL circuit adjusts the Sample clock timebase VCXO to synchronize
to a Reference clock. The frequency stability of the Sample clock
timebase matches that of the PLL Reference clock when the two are
phase-locked. Phase-locking also synchronizes multiple device
clocks that are phase–locked to the same Reference clock.

The following table shows the valid NI-FGEN
property or attribute value combinations that can be used to
configure the NI 5421 clock settings for
an internal Sample clock, an external Sample clock, or a Reference
clock. The term 
Update clock is synonymous with 
Sample clock.

| Sample Clock Source* | Clock Mode * | PLL Reference Clock Source * |
| --- | --- | --- |
| "OnboardClk" (default) | NIFGEN_VAL_DIVIDE_DOWN | "None" (default) |
| "PXI_CLK10", "RTSI7" |  |  |
| "ClkIn" |  |  |
| "OnboardRefClk" |  |  |
| NIFGEN_VAL_HIGH_RESOLUTION | "None" (default) |  |
| "PXI_CLK10", "RTSI7" |  |  |
| "ClkIn" |  |  |
| "OnboardRefClk" |  |  |
| NIFGEN_VAL_AUTOMATIC (default) | "None" (default) |  |
| "PXI_CLK10", "RTSI7" |  |  |
| "ClkIn" |  |  |
| "OnboardRefClk" |  |  |
| "ClkIn" | Not Applicable | Not Applicable |
| "PXI_STAR" |  |  |
| "PXI_Trig<0..6>" |  |  |
| "DDC_ClkIn" |  |  |
| *These column headings refer to NI-FGEN properties. The attributes that correspond to these properties are NIFGEN_ATTR_SAMPLE_CLOCK_SOURCE, NIFGEN_ATTR_CLOCK_MODE, and NIFGEN_ATTR_REFERENCE_CLOCK_SOURCE. The values in the columns represent the values that can be set on these properties or attributes. Settings that line up horizontally show valid combinations of the NI-FGEN settings. |  |  |

Parent topic:

NI 5421 Theory of Operation

Related concepts:

- NI 5421 Internal Sample Clock
- NI 5421 External Sample Clock
- NI 5421 Phase-Locked Loop Reference Clock

<!--NI_TOPIC bundle=ni-fgen path=ni-5421-clocking.html language=enus -->
## TOPIC 00300: NI 5421 Clocking

- bundle_id: `ni-fgen`
- source_path: `ni-5421-clocking.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5421-clocking.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5421 has a Sample clock rate of 10 Hz to 100 MHz. The timing of the device is very flexible, and you have multiple choices for deriving the Sample clock. There are modes for deriving the Sample clock from the internal Sample clock timebase, as well as modes to provide external clocks. You als

### NI 5421 Clocking

The NI 5421 has a Sample clock
rate of 10 Hz to 100 MHz. The timing of the device
is very flexible, and you have multiple choices for deriving the
Sample clock. There are modes for deriving the Sample clock from
the internal Sample clock timebase, as well as modes to provide
external clocks. You also have several choices for providing the
frequency reference for the onboard phase-locked loop.

[IMAGE alt='image' src='GUID-E29E53C4-1CBC-4D93-BB7D-9772D14E126A-a5.gif']

Note

Related Topics

*Clocking Options*

*Internal Sample Clock
Sources*

*Phase-Locked Loop
Reference Clock Sources*

*External Sample
Clock Sources*

*Exporting Clocks*

Parent topic:

NI 5421 Theory of Operation

Related concepts:

- NI 5421 Clocking Options
- NI 5421 Internal Sample Clock
- NI 5421 Phase-Locked Loop Reference Clock
- NI 5421 External Sample Clock
- NI 5421 Exporting Clocks

<!--NI_TOPIC bundle=ni-fgen path=ni-5421-continuous-trigger-mode.html language=enus -->
## TOPIC 00301: NI 5421 Continuous Trigger Mode

- bundle_id: `ni-fgen`
- source_path: `ni-5421-continuous-trigger-mode.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5421-continuous-trigger-mode.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The waveform you downloaded generates continuously after receiving one Start trigger. All Start triggers after the first Start trigger are ignored. The following table provides more information about waveform generation behavior in Arbitrary Waveform and Arbitrary Sequence output modes. Output Mode

### NI 5421 Continuous Trigger Mode

The waveform you downloaded generates continuously
after receiving one Start trigger. All Start triggers after the
first Start trigger are ignored. The
following table provides more information about
waveform generation behavior in Arbitrary Waveform and Arbitrary
Sequence output modes.

| Output Mode | Trigger Behavior |
| --- | --- |
| Arbitrary Waveform Mode | The waveform you downloaded generates continuously after receiving one Start trigger. All Start triggers after the first Start trigger are ignored. |
| Arbitrary Sequence Mode | The waveform pattern you define in the sequence list generates continuously by continually cycling through the sequence list. Only one Start trigger is required to start waveform generation. After the device receives a Start trigger, the waveform generation starts at the first segment and continues through the last segment, and then loops back to the start of the first segment, continuing indefinitely. All Start triggers after the first Start trigger that starts waveform generation are ignored. |

Parent topic:

NI 5421 Trigger Modes

<!--NI_TOPIC bundle=ni-fgen path=ni-5421-dac-attenuation.html language=enus -->
## TOPIC 00302: NI 5421 DAC Attenuation

- bundle_id: `ni-fgen`
- source_path: `ni-5421-dac-attenuation.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5421-dac-attenuation.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The main DAC output can be fine-tuned for attenuation, which provides 0 to 3 dB of the Analog Output path signal attenuation. This fine-tuning of the main DAC attenuation is performed by the gain DAC. Adjust the gain DAC using the Gain DAC Value property or the NIFGEN_ATTR_GAIN_DAC_VALUE attribute.

### NI 5421 DAC Attenuation

The main DAC output can be fine-tuned for
attenuation, which provides 0 to 3 dB of the Analog Output
path signal attenuation. This fine-tuning of the main DAC
attenuation is performed by the gain DAC. Adjust the gain
DAC using the 
Gain
DAC Value property or the 
NIFGEN_ATTR_GAIN_DAC_VALUE attribute. The main DAC also
provides the fine resolution for the attenuation settings.

Parent topic:

NI 5421 Attenuation

<!--NI_TOPIC bundle=ni-fgen path=ni-5421-data-mask.html language=enus -->
## TOPIC 00303: NI 5421 Data Mask

- bundle_id: `ni-fgen`
- source_path: `ni-5421-data-mask.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5421-data-mask.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The signal generator supports analog and digital data masks and static values. The data mask allows you to shield bits of the data to be replaced with the corresponding static value bits. For example, a mask of 0xFF00 and a static value of 0xAAAA applied to a DC waveform with a value of 0x1111 produ

### NI 5421 Data Mask

The signal generator supports analog and digital
data masks and static values. The data mask allows you to shield
bits of the data to be replaced with the corresponding static value
bits. For example, a mask of 0xFF00 and a static value of 0xAAAA
applied to a DC waveform with a value of 0x1111 produces a DC
waveform with a value of 0x11AA.

NI-FGEN supports separate and independent analog
and digital data masks and static values. The analog data mask and
analog static value apply to the digital data applied to the DAC,
and ultimately to the signal on the analog output terminal. The
analog data mask and analog static value do not affect the signals
on the digital connector. You can configure an analog data mask by calling the 
Analog Data
Mask or 
Analog
Static Value properties or the 
NIFGEN_ATTR_ANALOG_DATA_MASK and 
NIFGEN_ATTR_ANALOG_STATIC_VALUE attributes. The digital data mask and digital static value
apply to the signals on the digital connector and they do not
affect the signal on the analog output terminal. You can configure a digital data mask by calling the 
Digital
Data Mask or 
Digital
Static Value properties or the 
NIFGEN_ATTR_DIGITAL_DATA_MASK and 
NIFGEN_ATTR_DIGITAL_STATIC_VALUE attributes.

Parent topic:

NI 5421 NI 5421 Overview

<!--NI_TOPIC bundle=ni-fgen path=ni-5421-dc-offset.html language=enus -->
## TOPIC 00304: NI 5421 DC Offset

- bundle_id: `ni-fgen`
- source_path: `ni-5421-dc-offset.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5421-dc-offset.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5421 supports a DC offset before the attenuation chain that affects the maximum value of DC offset for a given gain setting. This preattenuation architecture requires two rules for setting the DC offset: The magnitude of the maximum value of offset can be no more than ½ of the configured gain

### NI 5421 DC Offset

The NI 5421 supports a DC offset before the attenuation chain that affects the maximum value of DC offset for a given gain setting. This preattenuation architecture requires two rules for setting the DC offset:

1. The magnitude of the maximum value of offset can be no more than ½ of the configured gain setting for the NI 5421.
2. The waveform maximum plus the offset must not exceed 
 ±6 V into 50 Ω; if it does, the waveform is clipped. For example, if you have set a gain of 
 5, which corresponds to an amplitude of 
 5 V pk , and the waveform is a sine wave using the full range of the DAC, the maximum DC offset you can apply without clipping the sine wave is 
 ±1 V. At this point, output voltages of the sine waveform have reached the maximum amplitude that the device supports. If you increase the DC offset further, the top portion of the waveform at 
 6 V is clipped.

NI-FGEN automatically calculates the preattenuation
offset value based on the set DC offset and gain values. The DC offset can be changed at any time during waveform generation by calling the 
Arbitrary Waveform Offset property or the 
NIFGEN_ATTR_ARB_OFFSET attribute.

The DC offset cannot be set if you selected the
Direct path. The Direct path offset is near zero. Refer to the 
*device
specifications* for information about the maximum value of the
DC offset.

Parent topic:

NI 5421 Waveform Amplitude Control

<!--NI_TOPIC bundle=ni-fgen path=ni-5421-digital-data-control-connector.html language=enus -->
## TOPIC 00305: NI 5421 DIGITAL DATA & CONTROL Connector

- bundle_id: `ni-fgen`
- source_path: `ni-5421-digital-data-control-connector.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5421-digital-data-control-connector.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The DIGITAL DATA & CONTROL (DDC) front panel connector is a 68-pin female VHDCI connector that contains the 16-bit LVDS digital pattern output. The DDC connector is an optional feature for the NI 5421. DIGITAL DATA & CONTROL Pin Assignments The following figure shows the NI 5421 DDC 68-pin connector

### NI 5421 DIGITAL DATA & CONTROL Connector

The DIGITAL DATA & CONTROL (DDC) front panel
connector is a 68-pin female VHDCI connector that contains the
16-bit LVDS digital pattern output. The DDC connector is an
optional feature for the NI 5421.

#### DIGITAL DATA & CONTROL Pin
Assignments

The following figure shows the
NI 5421 DDC 68-pin connector.

[IMAGE alt='image' src='GUID-73285A03-5DAA-4DED-BC9D-A39AD44D354A-a5.gif']

The following table lists the pin names and signal
descriptions used for the NI 5421 DDC connector. All
lines are at standard 
*LVDS* levels.

| Signal Name | Type | Description |
| --- | --- | --- |
| D<0..15> | Output | Digital pattern outputs–The 16-bit digital representation of the analog waveform is available on these output pins as digital pattern outputs. This data is available directly from the memory after several Sample clock pipeline delays. The digital pattern outputs are standard LVDS output levels. All data bits change on the falling edge of the DDC CLK OUT. |
| DDC CLK IN | Input | Digital Data Clock In–These lines are used as a source for an external Sample clock. You can feed a LVDS level clock to this line with a maximum frequency of the signal generator. |
| DDC CLK OUT | Output | Digital Data Clock Out–The Sample clock is always routed to the DDC CLK OUT line of the DDC front panel connector when the digital pattern is enabled. |
| Ground | – | Digital ground |
| PFI<2..3> (Inputs) | Input | PFI<2:3>–These PFI lines can accept a trigger from an external source that can start or step through waveform generation. You can select this functionality on the NI 5421 through the software. Refer to Trigger Sources for more information. |
| PFI<4:5> | Output | PFI<4..5>–These PFI lines can route out a signal from Marker events or the Out Start trigger. |
| Reserved | – | Reserved for future use. Do not connect signals to this line. |
| Refer to the device specifications for information about acceptable input signal characteristics to connect to the DDC lines, as well as the output signal characteristics. |  |  |

You must enable the DDC connector before the
signals in this table are available for use. You can enable digital patterning by calling the
niFgen
Configure Digital Patterning VI or the 
niFgen_EnableDigitalPatterning and 
niFgen_DisableDigitalPatterning functions.

Parent topic:

NI 5421 NI 5421 Overview

Related concepts:

- NI 5421 Low-Voltage Differential Signaling (LVDS)
- NI 5421 Trigger Sources

<!--NI_TOPIC bundle=ni-fgen path=ni-5421-digital-filter.html language=enus -->
## TOPIC 00306: NI 5421 Digital Filter

- bundle_id: `ni-fgen`
- source_path: `ni-5421-digital-filter.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5421-digital-filter.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The main DAC provides an internal digital filter. When digital filtering is enabled, the main DAC runs at a faster rate, referred to as the effective sample rate (ESR). The waveform data transfers to the main DAC at the configured Sample clock rate; the internal digital filter interpolates by a fact

### NI 5421 Digital Filter

The main DAC provides an internal digital filter.
When digital filtering is enabled, the main DAC runs at a faster
rate, referred to as the effective sample rate (ESR). The waveform
data transfers to the main DAC at the configured Sample clock rate;
the internal digital filter interpolates by a factor of 2x, 4x, or
8x; and the DAC generates the data at the ESR.

Effective sample rate is calculated with the
following formula:

ESR = 
I<sub>fac</sub>
 × 
SR

where

ESR = the Effective Sample Rate (MS/s)

I<sub>fac</sub>
 = the interpolation factor

SR = configured Sample Clock Rate (MS/s)

The effective sample rate only applies when the
digital filter is enabled. The maximum ESR is 400 MS/s. NI recommends that you make the
effective sample rate as high as possible
without exceeding 400 MS/s. The following table lists the
allowed update and interpolation rates.

| Recommended Interpolation Settings |  |
| --- | --- |
| Sample Clock Rate (MS/s) | Interpolation |
| 12.5 to 105 | 2x |
| 10 to 100 | 4x |
| 10 to 50 | 8x |

Note

The delay from the Start trigger to the analog
output increases if the digital filter is enabled. The delay
increases with an increase in the interpolation factor. Refer to
the 
*device
specifications* for information about the delay from the trigger
to the analog output based on the configured filter settings.

niFgen_EnableDigitalFilter

niFgen_DisableDigitalFilter

Note

#### Related Topics

*Filtering and
Interpolation*

*Aliased Images*

Parent topic:

NI 5421 Filtering Effects

Related concepts:

- Filtering and Interpolation
- Aliased Images

<!--NI_TOPIC bundle=ni-fgen path=ni-5421-digital-gain.html language=enus -->
## TOPIC 00307: NI 5421 Digital Gain

- bundle_id: `ni-fgen`
- source_path: `ni-5421-digital-gain.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5421-digital-gain.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Digital gain multiplies waveform data by a factor you specify in the Digital Gain property or the NIFGEN_ATTR_DIGITAL_GAIN attribute before converting the data to an analog signal in the DAC. Digital gain can be changed during generation without the glitches caused by switching that are common when

### NI 5421 Digital Gain

Digital gain multiplies waveform data by a factor
you specify in the 
Digital Gain
property or the 
NIFGEN_ATTR_DIGITAL_GAIN attribute before converting the data to an analog signal in
the DAC. Digital gain can be changed during generation without the
glitches caused by switching that are common when changing
analog gains. However, the output resolution of the DAC is a
function of digital gain, meaning that only analog gain makes full use of the
resolution of the DAC.

Parent topic:

NI 5421 Waveform Amplitude Control

<!--NI_TOPIC bundle=ni-fgen path=ni-5421-direct-dma.html language=enus -->
## TOPIC 00308: NI 5421 Direct DMA

- bundle_id: `ni-fgen`
- source_path: `ni-5421-direct-dma.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5421-direct-dma.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Direct DMA can transfer waveform data to the signal generator onboard memory at rates well beyond the typical 5 to 30 MB/s range in a standard PC-based architecture. To achieve such high rates, direct DMA establishes a direct connection between the signal generator onboard memory and a specialized w

### NI 5421 Direct DMA

*Direct DMA* can transfer waveform data to the signal generator onboard memory at rates well beyond the typical 5 to 30 MB/s range in a standard PC-based architecture. To achieve such high rates, direct DMA establishes a direct connection between the signal generator onboard memory and a specialized waveform data source. Direct DMA is commonly used to *stream* waveform data from disk at data rates of 100+ MB/sec. Conduant's StreamStor™ products are one example of direct DMA-compatible data sources.

#### Related Topics

*Configuring an Application for Direct DMA*

*DMA Fundamentals*

Parent topic:

NI 5421 Streaming

Related concepts:

- Direct DMA
- Streaming
- Configuring Your Application for Direct DMA

<!--NI_TOPIC bundle=ni-fgen path=ni-5421-events.html language=enus -->
## TOPIC 00309: NI 5421 Events

- bundle_id: `ni-fgen`
- source_path: `ni-5421-events.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5421-events.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use events to indicate when a specific hardware condition has been met on the NI 5421. An event is a signal generated by the NI device at a device state. The NI 5421 supports Ready for Start, Started, Data Marker, Marker, and Done events. The NI 5421 also supports the use of event delays. Re

### NI 5421 Events

You can use *events* to indicate when a specific
hardware condition has been met on the NI 5421. An event is a
signal generated by the NI device at a device state. The NI 5421
supports Ready for Start, Started, *Data Marker*, *Marker*, and Done
events. The NI 5421 also supports the use of *event delays*.

#### Related Topics

*Creating a Marker
Event*

*Creating a Data Marker
Event*

Parent topic:

NI 5421 NI 5421 Overview

Related concepts:

- Events
- Data Marker Events
- Marker Events
- Event Delays
- Creating a Marker Event
- Creating a Data Marker Event

<!--NI_TOPIC bundle=ni-fgen path=ni-5421-exporting-clocks.html language=enus -->
## TOPIC 00310: NI 5421 Exporting Clocks

- bundle_id: `ni-fgen`
- source_path: `ni-5421-exporting-clocks.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5421-exporting-clocks.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5421 provides resources for exporting your clocks and multiple destinations for routing. The following table shows the available clock signals that can be routed to devices external to the signal generator and the destination options. Clock to be Exported Destination Options Sample Clock PFI

### NI 5421 Exporting Clocks

The NI 5421 provides resources for exporting your clocks and multiple destinations for
routing.

[IMAGE alt='image' src='GUID-83FF9972-7F6E-4301-B879-BF4E8D5189AD-a5.gif']

The following table shows the available clock
signals that can be routed to devices external to the
signal generator and the destination options.

| Clock to be Exported | Destination Options |
| --- | --- |
| Sample Clock | PFI <0..1> SMB connector |
| PXI_Trig<0..6>, RTSI<0..6>> |  |
| DDC CLK OUT |  |
| Sample Clock Timebase | PFI <0..1> SMB connector |
| PXI_Trig<0..6>, RTSI<0..6> |  |
| DDC CLK OUT |  |
| Reference Clock | PFI <0..1> SMB connector |
| PXI_Trig<0..6>, RTSI<0..6> |  |
| Onboard Reference Clock | RTSI7 |

For synchronization purposes, the
NI 5421 allows you to export your clocks 
so that other devices can share the timing of the NI 5421. The following sections describe the possible clock routing configurations.

#### Sample Clock

The Sample clock can be routed to the
PFI <0..1> front panel SMB connectors, PXI_Trig<0..6>
lines on the PXI trigger bus, or the RTSI<0..6> lines.
Additionally, the Sample clock has a direct route to the DDC CLK
OUT line on the DIGITAL DATA & CONTROL connector on the front
panel.

Additionally, the exported clock can be divided
down by an integer value (no less than 2) before being exported to
the PFI<0..1> SMB connectors, PXI_Trig<0..6> lines, or
the RTSI<0..6> lines. Refer to the 
Exported Sample Clock Divisor property or the 
NIFGEN_ATTR_EXPORTED_SAMPLE_CLOCK_DIVISOR attribute for more information about configuring the Sample
clock divisor.

#### Sample Clock Timebase

The Sample clock timebase can be routed to the
PFI <0..1> SMB connectors on the front panel, the
PXI_Trig<0..6> lines on the PXI trigger bus, or the
RTSI<0..6> lines. Additionally, the Sample clock timebase has
a direct route to the DDC CLK OUT line on the DIGITAL DATA &
CONTROL connector on the front panel.

Additionally, the exported clock can be divided
down by an integer value before being exported to the
PFI<0..1> SMB connectors, the PXI_Trig<0..6> lines, or
the RTSI<0..6> lines. You can configure the Sample clock divisor by calling the 
Exported Sample Clock Timebase Divisor property or the 
NIFGEN_ATTR_EXPORTED_SAMPLE_CLOCK_TIMEBASE_DIVISOR attribute.

#### Reference Clock

The Reference clock is the
actual clock that is configured for the signal generator
phase-locked loop circuit to use as a reference. You configure a
Reference clock as a PLL Reference clock source for the signal to
be available for exporting. The Reference clock can be routed to
the PFI<0..1> SMB connectors on the front panel, the
PXI_Trig<0..6> lines on the PXI trigger bus, or the
RTSI<0..6> lines.

Note

#### Onboard Reference Clock

The onboard Reference clock is a dedicated 10 MHz
clock for PCI modules only. The onboard Reference clock can only be
exported to RTSI7, for other devices to use and reimport as the
Reference clock.

Tip

#### Destination Options

The following sections define the destinations for
exported clocks.

DDC CLK OUT—You can export the Sample clock
to the DDC CLK OUT line on the optional DIGITAL DATA & CONTROL (DDC)
connector. Exporting the clock from
this connection allows for synchronous clocking of the DDC data.
You must enable the DDC connector before using the Sample clock by calling the 
niFgen
Configure Digital Patterning VI or the 
niFgen_EnableDigitalPatterning and 
niFgen_DisableDigitalPatterning functions.

PFI <0..1>—The Sample clock and the
Reference clock can be exported to the PFI 0 and PFI 1 SMB
connectors on the front panel to synchronize external devices. You
must configure the device to export the desired clock to the PFI
SMB connectors.

Note

PXI_Trig<0..6>—The Sample clock and
the Reference clock can be exported to the PXI_Trig lines or RTSI
lines. The PXI and PCI standards allow for devices to route signals
to other devices in your PXI chassis to enhance device to device
synchronization. Refer to the chassis documentation for
specifications to ensure the reference signal is within tolerance.
You must configure the device to export the desired clock to the
PXI_Trig line or RTSI line. When exporting signals, the following
lines are equivalent:

- PXI_Trig<0..6> = RTSI_<0..6>
- PXI_STAR

Refer to 
niFgen Export
Signal VI or the 
niFgen_ExportSignal function for more information about configuring the
destinations for the desired clock signal.

Parent topic:

NI 5421 Theory of Operation

<!--NI_TOPIC bundle=ni-fgen path=ni-5421-exporting-signals.html language=enus -->
## TOPIC 00311: NI 5421 Exporting Signals

- bundle_id: `ni-fgen`
- source_path: `ni-5421-exporting-signals.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5421-exporting-signals.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The signal generator contains seven PXI trigger lines or seven RTSI (PCI devices only) lines that are available for sending signal generator-specific information to other devices that have PXI trigger or RTSI bus connectors. The signal generator also connects to the PXI star trigger line, which you

### NI 5421 Exporting Signals

Note

ni.com/products

The signal generator has connectors on the front
panel to route signals to devices external to a PXI or PCI
chassis. The following table shows the signals available for export
and the lines they can be routed to. To determine all possible
signal routes for your device, refer to 
*Signal Routing*.

|  |  | Destination |  |  |
| --- | --- | --- | --- | --- |
| PXI_Trig<0..6>, RTSI<0..6>, or PXI_STAR | PFI 0 and PFI 1 Connectors | PFI<4..5> on DIGITAL DATA & CONTROL Connector |  |  |
| Exported Clocks, Triggers, and Events | Sample Clock | Yes | Yes * | – |
| Sample Clock Timebase | Yes | Yes | – |  |
| PLL Reference Source | Yes | Yes* | – |  |
| Out Start trigger | Yes | Yes | Yes |  |
| Marker Event | Yes | Yes | Yes |  |
| * SYNC OUT/PFI 0 is optimized for the Sample clock and PLL reference source signals and has slightly less jitter than PFI 1. SYNC OUT/PFI 0 is the recommended terminal to use for exporting clocks. |  |  |  |  |

Sample Clock–The clock signal that tells the
DAC when to convert the digital waveform values to an analog
voltage. The Sample clock frequency is referred to as the Sample
clock rate; the rate at which the digital waveforms from device
memory are generated. The Sample clock is also known as update
clock.

Note

Sample Clock Timebase

Note

PLL Reference source–A clock signal that is
only available when a PLL Reference source has been configured. The
clock is the source selected as the PLL Reference Clock source.

Out Start trigger–A signal generated by the
device upon recognizing a start condition that can be routed out
various connectors to signal other devices.

Marker event–A digital signal that can be
used as a trigger corresponding to a specific sample in the
waveform generation. This signal controls other devices that
require timing information related to a specific point in the
generated waveform.

#### Routing Signals

You can route signals in the following ways:

- The Marker event generated during an Arbitrary Waveform
Generation mode waveform generation to any of the PXI trigger
lines, RTSI lines (PCI devices only), PXI_STAR, or front panel
connectors.
- The signal generator Start trigger output signal to other
devices through any of the PXI trigger lines, RTSI lines (PCI devices only), PXI_STAR, or front panel connectors.
- The signal generator Sample clock signal to other devices
through any of the PXI trigger lines, RTSI lines (PCI devices only), PXI_STAR, or front panel connectors.
- The PLL Reference clock source to other devices through any of
the PXI trigger lines, RTSI lines (PCI devices only), PXI_STAR, or
front panel connectors.

In NI-FGEN, the PXI trigger lines are referred to
as RTSI<0..6>. The correlation between PXI_TRIG<
x> and RTSI<
x> is one to one. You can
configure and route the device internal signals by calling the 
niFgen Export Signal VI
or the 
niFgen_ExportSignal function.

Parent topic:

NI 5421 NI 5421 Overview

Related concepts:

- NI 5421 Signal Routing

<!--NI_TOPIC bundle=ni-fgen path=ni-5421-external-sample-clock.html language=enus -->
## TOPIC 00312: NI 5421 External Sample Clock

- bundle_id: `ni-fgen`
- source_path: `ni-5421-external-sample-clock.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5421-external-sample-clock.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5421 can accept an external clock to directly drive the Sample clock. When using an external Sample clock, the frequency stability and accuracy of the Sample clock is determined by the provided external Sample clock. The following figure shows possible Sample Clock paths. You can set the cloc

### NI 5421 External Sample Clock

The NI 5421 can accept an
external clock to directly drive the Sample clock. When using an
external Sample clock, the frequency stability and accuracy of the
Sample clock is determined by the provided external Sample
clock.

The following figure shows possible Sample
Clock paths.

[IMAGE alt='image' src='GUID-8812ED51-9200-4A44-85CC-727D2EA85B31-a5.gif']

You can set the clock source by calling the
niFgen
Configure Sample Clock Source VI or the 
niFgen_ConfigureSampleClockSource function.

niFgen_ConfigureSampleRate

Note

device specifications

#### External Sample Clock Considerations

The NI 5421 incorporates
high-speed digital clocking technology and requires a stable,
free-running Sample clock to operate properly. When the
signal generator is committed—either explicitly by
calling the 
niFgen Commit VI or
the 
niFgen_Commit function or implicitly by writing waveforms or scripts or
initiating a generation—the external Sample clock must be
available to the device. If the external clock becomes unstable due
to glitching or changing frequency, or is removed entirely, NI-FGEN
returns a hardware clocking error.

If necessary, you can change the rate or the source
of the external Sample clock between generations by
first calling the 
niFgen Abort
Generation VI or the 
niFgen_AbortGeneration function, changing the rate or source, and then calling the
niFgen Commit VI or the 
niFgen_Commit function. NI-FGEN
reprograms the NI 5421 for the new settings,
and you can call the 
niFgen
Initiate Generation VI or the 
niFgen_InitiateGeneration function to start the next generation.

If you must remove the external Sample clock
between generations (after calling the niFgen Abort Generation VI
or 
niFgen_AbortGeneration function, but
before calling the niFgen Initiate VI or the 
niFgen_Init function), but are not
changing the frequency or source of the external clock, you can
choose one of the following options:

- Call the niFgen Initiate VI or the 
 niFgen_Init function, which returns
a hardware clocking error because the external Sample clock is
gone, then clear the error and call the niFgen Initiate VI or the 
 niFgen_Init function
again. NI-FGEN then reprograms the hardware to use the
external clock again.
- Force the device to be recommitted by changing a property or
attribute to another value and then back to its original value.
This action causes NI-FGEN to re-commit the settings to hardware,
which does not happen otherwise because NI-FGEN does not know
that the external Sample clock is gone.

Caution

niFgen_ConfigureSampleRate

Parent topic:

NI 5421 Clocking Options

<!--NI_TOPIC bundle=ni-fgen path=ni-5421-filtering-effects.html language=enus -->
## TOPIC 00313: NI 5421 Filtering Effects

- bundle_id: `ni-fgen`
- source_path: `ni-5421-filtering-effects.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5421-filtering-effects.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The delay from the time at which the device receives a trigger to the time at which the analog output signal is generated increases if the digital and/or analog filters in the Analog Output path are enabled. In the case of digital filtering, delay also increases with increase in interpolation. The

### NI 5421 Filtering Effects

Analog Output path

Note

Refer to 
*Digital
Filter* for interpolation options. Refer to the 
*device
specifications* for the delay from trigger to analog output
based on different filtering options.

Parent topic:

NI 5421 Analog Output

Related concepts:

- NI 5421 Analog Output
- NI 5421 Digital Filter

<!--NI_TOPIC bundle=ni-fgen path=ni-5421-filtering-effects_2.html language=enus -->
## TOPIC 00314: NI 5421 Filtering Effects

- bundle_id: `ni-fgen`
- source_path: `ni-5421-filtering-effects_2.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5421-filtering-effects_2.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The delay from the time at which the device receives a trigger to the time at which the analog output signal is generated increases if the digital and/or analog filters in the Analog Output path are enabled. In the case of digital filtering, delay also increases with increase in interpolation. The

### NI 5421 Filtering Effects

Analog Output path

Note

Refer to 
*Digital
Filter* for interpolation options. Refer to the 
*device
specifications* for the delay from trigger to analog output
based on different filtering options.

Parent topic:

NI 5421 Triggering

<!--NI_TOPIC bundle=ni-fgen path=ni-5421-front-panel.html language=enus -->
## TOPIC 00315: NI 5421 Front Panel

- bundle_id: `ni-fgen`
- source_path: `ni-5421-front-panel.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5421-front-panel.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the NI PXI-5421 front panel. This front panel has four SMB connectors and an optional 68-pin male VHDCI connector. The male VHDCI (Digital Data & Control) connector is not available on the NI 5421 with the 8 MB memory option. The ACCESS and ACTIVE LEDs indicate the status

### NI 5421 Front Panel

The following figure shows the NI PXI-5421 front panel. This front panel has
four SMB connectors and an optional 68-pin male VHDCI connector.
The male VHDCI (Digital Data & Control) connector is not
available on the NI 5421 with the 8 MB memory
option.

[IMAGE alt='image' src='GUID-497C7D50-AEB1-45E9-8F21-E61F39725EE0-a5.gif']

The *ACCESS and ACTIVE LEDs* indicate the status of the PXI module.

The 
*CH 0* SMB connector is the analog
output from which arbitrary waveforms are generated.

The 
*CLK IN* SMB connector provides the
device with an external reference or external Sample clock.

The 
*PFI 0 and PFI 1* SMB
connectors are multi-directional connections for a number of
different signals.

*DIGITAL DATA &
CONTROL* is an optional 68-pin male VHDCI connector that
contains the 16-bit LVDS digital pattern outputs.

Parent topic:

NI 5421 NI 5421 Overview

Related concepts:

- NI 5421 ACCESS and ACTIVE LEDs
- NI 5421 CH 0 Connector
- NI 5421 CLK IN Connector
- NI 5421 PFI Connectors
- NI 5421 DIGITAL DATA & CONTROL Connector

<!--NI_TOPIC bundle=ni-fgen path=ni-5421-hardware-state-diagram.html language=enus -->
## TOPIC 00316: NI 5421 Hardware State Diagram

- bundle_id: `ni-fgen`
- source_path: `ni-5421-hardware-state-diagram.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5421-hardware-state-diagram.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following diagram shows the hardware states of the signal generator. The signal generator can be in one of the following six basic states during the course of operation. Idle—The device is not generating a waveform. All session properties or attributes can be programmed in the Idle state. In the

### NI 5421 Hardware State Diagram

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

NI 5421 Theory of Operation

Related concepts:

- Programming State Model

<!--NI_TOPIC bundle=ni-fgen path=ni-5421-internal-sample-clock.html language=enus -->
## TOPIC 00317: NI 5421 Internal Sample Clock

- bundle_id: `ni-fgen`
- source_path: `ni-5421-internal-sample-clock.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5421-internal-sample-clock.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5421 can derive a Sample clock from its main internal timing source—the onboard Sample clock timebase. The signal generator provides a high-precision 100 MHz Voltage Controlled Crystal Oscillator (VCXO) clock source for the Sample clock timebase. As shown in the following figure, the Sample c

### NI 5421 Internal Sample Clock

The NI 5421 can derive a Sample
clock from its main internal timing source—the onboard Sample clock
timebase. The signal generator provides a high-precision
100 MHz Voltage Controlled Crystal Oscillator (VCXO) clock
source for the Sample clock timebase. As shown in the following
figure, the Sample clock timebase frequency is tuned by an Internal
Calibration DAC control voltage when the 
Reference
Clock Source property or the 
NIFGEN_ATTR_REFERENCE_CLOCK_SOURCE attribute is set to "None." The Internal Calibration DAC,
which is calibrated at the factory and which you also can
calibrate, provides for the Sample clock Timebase to maintain a
high quality frequency source.

[IMAGE alt='image' src='GUID-3FA29193-B2A4-4322-BE88-52DBA4119C65-a5.gif']

There are two methods, referred to as clock modes,
for creating an internal Sample clock from the Sample clock
timebase: Divide-Down (Divide by N) Sampling and High-Resolution Sampling.

In Divide-Down Sampling mode, the
Divide by 
N circuit uses the Sample clock timebase of 100 MHz
to create the frequency available for use as the Sample clock.
Divide-Down Sampling mode can generate any internal timebase
frequency of 100 MHz/
N, where 
N is any integer from 1 to 4,194,304. For example, the
internal timebase can run at 100 MHz, 50.0 MHz, 33.33
MHz, 25.0 MHz, 20.0 MHz, 16.666 MHz, and so on. The low
frequency limit in Divide-Down Sampling mode is
23.84185 (100 MHz/4,194,304) Hz. Divide-Down Sampling
mode provides a high-quality clock with the lowest jitter.

The High-Resolution Sampling mode also uses the
Sample clock timebase at 100 MHz to generate a frequency from
10 Hz to 100 MHz. In addition, the High-Resolution mode
uses direct digital synthesis to generate very fine resolution
increments on the order of microhertz. Refer to the 
*device
specifications* for more information about jitter.

Note

device
specifications

Parent topic:

NI 5421 Clocking Options

<!--NI_TOPIC bundle=ni-fgen path=ni-5421-low-voltage-differential-signaling-lv.html language=enus -->
## TOPIC 00318: NI 5421 Low-Voltage Differential Signaling (LVDS)

- bundle_id: `ni-fgen`
- source_path: `ni-5421-low-voltage-differential-signaling-lv.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5421-low-voltage-differential-signaling-lv.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Low-voltage differential signaling (LVDS) is a low-noise, low-power, low-amplitude method for high-speed digital data transfer. The following figure shows a diagram of a typical LVDS circuit. As you can see in the previous figure, a current source at the driver provides approximately 3.5 mA of curre

### NI 5421 Low-Voltage Differential Signaling (LVDS)

Low-voltage differential signaling (LVDS) is a
low-noise, low-power, low-amplitude method for high-speed digital
data transfer.

The following figure shows a diagram of a typical
LVDS circuit.

[IMAGE alt='image' src='GUID-33D1EFAE-90F1-4A1C-8B90-A6B07019D4EA-a5.gif']

As you can see in the previous figure, a current
source at the driver provides approximately 3.5 mA of current.
The direction of the current across the transmission line depends
on whether the driver drives a logic high level or low level. When
the current reaches the receiver, a 100 Ω terminating
resistor connects the two ends of the differential transmission
line to provide a return path for the current. In addition, a
voltage of approximately 350 mV is established across the two
input terminals of the receiver. The differential voltage at the
receiver is either positive or negative, depending on the direction
of the current. The receiver recognizes a positive voltage signal
as a logic high level (1) and a negative voltage as a logic low
level (0).

The electrical characteristics of an LVDS signal
offers some performance improvements compared to single-ended
standards. For example, since the received voltage is a
differential between two signals, the voltage difference between
the logic high level and low level state can be smaller, allowing
for faster rise and fall times. Also, the differential transmission
scheme is less susceptible to common-mode noise than single-ended
transmission methods.

Note

Electrical Characteristics of Low-Voltage Differential
Signaling (LVDS) Interface Circuits

Parent topic:

NI 5421 DIGITAL DATA & CONTROL Connector

<!--NI_TOPIC bundle=ni-fgen path=ni-5421-memory-fragmentation.html language=enus -->
## TOPIC 00319: NI 5421 Memory Fragmentation

- bundle_id: `ni-fgen`
- source_path: `ni-5421-memory-fragmentation.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5421-memory-fragmentation.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: When storing multiple waveforms in NI 5421 memory, fragmentation can become a problem. Both waveforms and instructions are stored in NI 5421 memory in contiguous blocks. These blocks are allocated in multiples of 128 bytes, and they are written in the order that you configure them. Fragmentation occ

### NI 5421 Memory Fragmentation

When storing multiple waveforms in
NI 5421 memory, fragmentation can become a
problem. Both waveforms and instructions are stored in
NI 5421 memory in contiguous blocks. These
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

NI 5421 Onboard Memory

<!--NI_TOPIC bundle=ni-fgen path=ni-5421-ni-5421-overview.html language=enus -->
## TOPIC 00320: NI 5421 NI 5421 Overview

- bundle_id: `ni-fgen`
- source_path: `ni-5421-ni-5421-overview.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5421-ni-5421-overview.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5421 is a 100 MS/s, 16-bit arbitrary waveform generator with the following features: One 16-bit resolution output channel Output amplitude up to 12 V[pk-pk] into a 50 Ω load Offset up to ±25% of V[pk-pk] Up to 43 MHz sine output Up to 12.5 MHz square Up to 5 MHz triangle, ramp-up, and ramp-do

### NI 5421 NI 5421 Overview

The NI 5421 is a 100 MS/s, 16-bit arbitrary
waveform generator with the following features:

- One 16-bit resolution output channel
- Output amplitude up to 12 V pk-pk into a 50 Ω load
- Offset up to ±25% of V pk-pk
- Up to 43 MHz sine output
- Up to 12.5 MHz square
- Up to 5 MHz triangle, ramp-up, and ramp-down
- Software-selectable output impedances (50 Ω or
75 Ω) and output attenuation levels from 0 dB to
51 dB
- High-Resolution, Divide by 
 N , and external clocking
- PLL synchronization to external clocks or to
PXI_CLK10
- NI-TClk support for multi-module synchronization. Refer to 
 Start»All Programs»National Instruments»NI-TClk 
for more information.
- Sampling rate up to 100 MS/s
- Up to 256 MB of onboard waveform memory
- Waveform linking and looping for arbitrary waveform
generation
- Digital and analog filters
- Digital gain
- Four external trigger inputs
- 4 Marker events as trigger output
- Optional 16-bit digital pattern generation with clock and LVDS
output
- PXI trigger/RTSI lines

All NI 5421 devices follow industry-standard
Plug and Play specifications for the PXI bus and offer seamless
integration with compliant systems.

Parent topic:

Devices

<!--NI_TOPIC bundle=ni-fgen path=ni-5421-onboard-memory.html language=enus -->
## TOPIC 00321: NI 5421 Onboard Memory

- bundle_id: `ni-fgen`
- source_path: `ni-5421-onboard-memory.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5421-onboard-memory.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5421 signal generator uses an onboard memory that is 16-bits wide. The minimum standard memory size for the NI 5421 is 8 MB which translates to 8,338,608 usable bytes. With the minimum standard memory size, you can store very long waveforms on the device and obtain reliable waveform generatio

### NI 5421 Onboard Memory

The NI 5421 signal generator
uses an onboard memory that is 16-bits wide. The minimum standard
memory size for the NI 5421 is 8 MB
which translates to 8,338,608 usable bytes. With the minimum
standard memory size, you can store very long waveforms on the
device and obtain reliable waveform generation at full sample rate
of 100 MS/s. The
NI 5421 is also available with higher memory options
of 32 MB, 256 MB, and 512 MB.

The onboard memory is a single large memory area that stores both waveforms and sequence instructions to generate
the waveforms. The instructions for a complicated sequence can
occupy a significant portion of memory. The architecture of the
NI 5421 allows you to load multiple
waveforms and multiple sequence instructions into the memory. The
following diagram illustrates NI 5421
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

Parent topic:

NI 5421 Theory of Operation

<!--NI_TOPIC bundle=ni-fgen path=ni-5421-output-enable.html language=enus -->
## TOPIC 00322: NI 5421 Output Enable

- bundle_id: `ni-fgen`
- source_path: `ni-5421-output-enable.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5421-output-enable.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can disable the analog output signal at the CH 0 connector by controlling the output enable relay, as shown in the following figure. When the output enable relay is disabled, the output signal is connected to ground through a 50 or 75 Ω resistance depending on the output impedance selected. The

### NI 5421 Output Enable

You can disable the analog output signal at the CH
0 connector by controlling the output enable relay, as shown in the
following figure.

[IMAGE alt='image' src='GUID-BFAEDBE6-696A-4B0B-9A41-C8FD2A49A5A8-a5.gif']

When the output enable relay is disabled, the
output signal is connected to ground through a 50 or
75 Ω resistance depending on the output impedance
selected. The output enable relay is enabled for normal waveform
generation, connecting the CH 0 SMB connector to the 
*Analog Output path*. You
can change the output enable state at any time during waveform
generation, and the generation continues on internally.

niFgen_ConfigureOutputEnabled

Note

Parent topic:

NI 5421 Analog Output

Related concepts:

- NI 5421 Analog Output

<!--NI_TOPIC bundle=ni-fgen path=ni-5421-output-impedance.html language=enus -->
## TOPIC 00323: NI 5421 Output Impedance

- bundle_id: `ni-fgen`
- source_path: `ni-5421-output-impedance.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5421-output-impedance.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5421 Analog Output path is designed to have an output impedance of 50 Ω from the Output Enable relay looking back towards the Main DAC. There is a selectable 25 Ω resistance that can be switched into the Analog Output path between the Output Enable relay and the CH 0 connector for application

### NI 5421 Output Impedance

The NI 5421 Analog Output path is
designed to have an output impedance of 50 Ω from the
*Output Enable relay* looking back towards the Main DAC. There is a
selectable 25 Ω resistance that can be switched into the
Analog Output path between the Output Enable relay and the CH
0 connector for applications requiring a 75 Ω
impedance. Most applications use a load impedance of
50 Ω, but applications such as video testing, require
75 Ω. Refer to the following figure.

[IMAGE alt='image' src='GUID-1168A294-D930-4645-8DF7-E4E6E841D015-a5.gif']

If the load impedance is a high impedance (~1
MΩ), you may see output levels up to twice the selected
output value for a matched input/output impedance. These levels can
be as high as 24 V<sub>pk-pk</sub> for the High-Gain Amplifier path. Normally, the
output levels increase as the load impedance increases. The
NI 5421 can compensate for different load impedance
values. Refer to 
*CH 0 Connector* for more
information.

niFgen_ConfigureOutputImpedance

Note

Parent topic:

NI 5421 Analog Output

Related concepts:

- NI 5421 Output Enable
- NI 5421 CH 0 Connector

<!--NI_TOPIC bundle=ni-fgen path=ni-5421-output-modes.html language=enus -->
## TOPIC 00324: NI 5421 Output Modes

- bundle_id: `ni-fgen`
- source_path: `ni-5421-output-modes.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5421-output-modes.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The output mode of your signal generator determines the type of waveforms your signal generator produces. To select an output mode, set the Output Mode parameter of the niFgen Configure Output Mode VI or the niFgen_ConfigureOutputMode function.

### NI 5421 Output Modes

The output mode of your signal generator determines the type of
waveforms your signal generator produces. To select an output mode,
set the 
Output Mode parameter of the 
niFgen
Configure Output Mode VI or the 
niFgen_ConfigureOutputMode function.

Parent topic:

NI 5421 Waveform Generation

<!--NI_TOPIC bundle=ni-fgen path=ni-5421-pci-block-diagram.html language=enus -->
## TOPIC 00325: NI 5421 PCI Block Diagram

- bundle_id: `ni-fgen`
- source_path: `ni-5421-pci-block-diagram.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5421-pci-block-diagram.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: This topic contains information about the NI PCI-5421 top-level block diagram and descriptions of the individual blocks. You can drive the PXI_STAR line only if the signal generator is installed in Slot 2 of the PXI chassis. The following list describes the individual blocks: Onboard Reference clo

### NI 5421 PCI Block Diagram

This topic contains information about the
NI PCI-5421 top-level block diagram and descriptions of the
individual blocks.

[IMAGE alt='image' src='GUID-9DEB8AFF-5AD9-4E73-A9B8-5F8D07478FC0-a5.gif']

Note

The following list describes the individual
blocks:

- Onboard Reference clock derives frequencies and sample
rates when generating waveforms.
- Onboard Memory stores the waveform data and generation
instructions that you load into the device.
- Clocking allows you to create your Sample clock and
Reference clock.
- The 
 Waveform Generation Engine retrieves the waveform data and
instructions from the 
 Onboard Memory using the Sample clock. The 
 Waveform Generation Engine also uses this clock to
retrieve triggers from 
 Trigger and Event Control .
- The output from the 
 Waveform Generation Engine is sent to the 
 DAC device and the 
 DIGITAL DATA & CONTROL Connector on the front panel
after any digital gain is applied.
- The 
 DAC also contains a selectable 
 Digital Filter , which interpolates and filters the
waveform data.
- The waveform data is sent from the 
 DAC to the 
 Analog Output path where the waveform data is filtered and
amplified.
- The 
 Routing Matrix allows flexible routing of the RTSI trigger
lines and the external PFI lines.

Parent topic:

NI 5421 Theory of Operation

<!--NI_TOPIC bundle=ni-fgen path=ni-5421-pci-clock-source-and-frequency.html language=enus -->
## TOPIC 00326: NI 5421 PCI Clock Source and Frequency

- bundle_id: `ni-fgen`
- source_path: `ni-5421-pci-clock-source-and-frequency.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5421-pci-clock-source-and-frequency.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5421 has a Sample clock rate of 10 Hz to 100 MHz. The timing of the NI 5421 is very flexible, and you have multiple choices for deriving the Sample clock. There are modes for deriving the Sample clock from the internal Sample clock timebase, as well as modes to provide external clocks. You al

### NI 5421 PCI Clock Source and Frequency

The NI 5421 has a Sample clock rate of
10 Hz to 100 MHz. The timing of the NI 5421 is
very flexible, and you have multiple choices for deriving the
Sample clock. There are modes for deriving the Sample clock from
the internal Sample clock timebase, as well as modes to provide
external clocks. You also have several choices for providing the
frequency reference for the onboard phase-locked loop.

[IMAGE alt='image' src='GUID-9C4A080E-538D-4087-AE39-C87D528E679E-a5.gif']

Note

#### Related Topics

*Sample Clock Sources*

*Internal Sample Clock
Sources*

*PLL Reference
Sources*

*External Sample Clock Sources*

*Exporting Clocks*

Parent topic:

NI 5421 Theory of Operation

Related concepts:

- NI 5421 Clocking Options
- NI 5421 Internal Sample Clock
- NI 5421 Phase-Locked Loop Reference Clock
- NI 5421 External Sample Clock
- NI 5421 Exporting Clocks

<!--NI_TOPIC bundle=ni-fgen path=ni-5421-pci-front-panel.html language=enus -->
## TOPIC 00327: NI 5421 PCI Front Panel

- bundle_id: `ni-fgen`
- source_path: `ni-5421-pci-front-panel.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5421-pci-front-panel.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the NI PCI-5421 front panel. This front panel has four SMB connectors and an optional 68-pin male VHDCI connector. The male VHDCI (Digital Data & Control) connector is not available on the NI 5421 with the 8 MB memory option. The CLK IN Connector SMB connector provides the

### NI 5421 PCI Front Panel

The following figure shows the
NI PCI-5421 front panel. This front panel has four SMB
connectors and an optional 68-pin male VHDCI connector. The male
VHDCI (Digital Data & Control) connector is not available on
the NI 5421 with the 8 MB memory option.

[IMAGE alt='image' src='GUID-43F863E7-E29A-4152-ABC5-B4141B044F9C-a5.gif']

The 
*CLK IN Connector* SMB connector
provides the device with an external reference or external Sample
clock.

The 
*PFI 0 and PFI 1* SMB
connectors are multi-direction connections for a number of
different signals.

*DIGITAL DATA &
CONTROL* is an optional 68-pin male VHDCI connector that
contains the 16-bit LVDS digital pattern outputs.

The 
*CH 0* SMB connector is the analog
output from which arbitrary waveforms are generated.

Parent topic:

NI 5421 NI 5421 Overview

Related concepts:

- NI 5421 CLK IN Connector
- NI 5421 PFI Connectors
- NI 5421 DIGITAL DATA & CONTROL Connector
- NI 5421 CH 0 Connector

<!--NI_TOPIC bundle=ni-fgen path=ni-5421-pfi-connectors.html language=enus -->
## TOPIC 00328: NI 5421 PFI Connectors

- bundle_id: `ni-fgen`
- source_path: `ni-5421-pfi-connectors.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5421-pfi-connectors.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: PFI 0 and PFI 1 are bidirectional connectors. As an input, the PFI terminals can accept a trigger from an external source that can start or step through waveform generation. As an output, the PFI lines route a signal out from the following sources: Marker events Start trigger PLL Reference clock sou

### NI 5421 PFI Connectors

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

device specifications

Note

Parent topic:

NI 5421 NI 5421 Overview

<!--NI_TOPIC bundle=ni-fgen path=ni-5421-phase-locked-loop-reference-clock.html language=enus -->
## TOPIC 00329: NI 5421 Phase-Locked Loop Reference Clock

- bundle_id: `ni-fgen`
- source_path: `ni-5421-phase-locked-loop-reference-clock.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5421-phase-locked-loop-reference-clock.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: A phase-locked loop (PLL) is a circuit that tunes the Sample clock timebase to phase–lock to an external Reference clock. The PLL Reference clock source controls the source of the control voltage that tunes the VCXO of the Sample clock timebase for internal clock update sources. The frequency stabil

### NI 5421 Phase-Locked Loop Reference Clock

Note

device
specifications

The following figure shows the NI 5421 Reference Clock Source path.

[IMAGE alt='image' src='GUID-928A3C7A-05C9-46C0-86CE-DCD9AFB72E85-a5.gif']

Note

NIFGEN_ATTR_REFERENCE_CLOCK_SOURCE

#### Reference Clock Sources

The NI 5421 can
phase-lock its Sample clock timebase to an external signal
that is present on the CLK IN front panel connector. PXI devices
can also phase–lock to a 10 MHz Reference clock signal
provided by the PXI bus (PXI_CLK10), while PCI devices can
phase–lock to RTSI line 7 or to the onboard Reference
clock.

Refer to the table in 
*Clocking Options*,
for the valid NI-FGEN property value combinations that can be used
to configure the NI 5421 clock settings
for an external Reference clock.

Note

device 
specifications

Related Topics

Configuring a Reference
Clock

Parent topic:

NI 5421 Clocking Options

Related concepts:

- NI 5421 Clocking Options
- Configuring a Reference Clock

<!--NI_TOPIC bundle=ni-fgen path=ni-5421-postamplifier-attenuation.html language=enus -->
## TOPIC 00330: NI 5421 Postamplifier Attenuation

- bundle_id: `ni-fgen`
- source_path: `ni-5421-postamplifier-attenuation.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5421-postamplifier-attenuation.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The postamplifier attenuation section is after the High-Gain and Low-Gain Amplifiers in the analog path. The attenuators provide a range of attenuation from 0 dB to a maximum of 36 dB in steps of 12 dB. NI-FGEN automatically controls the value of attenuation set in the postamplifier attenuation sect

### NI 5421 Postamplifier Attenuation

The postamplifier attenuation section is after the
High-Gain and Low-Gain Amplifiers in the *analog path*. The attenuators provide a
range of attenuation from 0 dB to a maximum of 36 dB in steps
of 12 dB. NI-FGEN automatically controls the value of attenuation
set in the postamplifier attenuation section dependent on the set
gain. You can read the value NI-FGEN has selected for postamplifier
attenuation using the 
Post-Amplifier Attenuation property or the 
NIFGEN_ATTR_POST_AMPLIFIER_ATTENUATION attribute.

Parent topic:

NI 5421 Attenuation

Related concepts:

- NI 5421 Analog Output

<!--NI_TOPIC bundle=ni-fgen path=ni-5421-power-up-and-reset-conditions.html language=enus -->
## TOPIC 00331: NI 5421 Power-Up and Reset Conditions

- bundle_id: `ni-fgen`
- source_path: `ni-5421-power-up-and-reset-conditions.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5421-power-up-and-reset-conditions.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The signal generator is in the following state from the time at which the computer begins to power up until the operating system is fully booted and NI-FGEN is loaded. The CH 0 analog output connector is disabled and has 50 Ω or 75 Ω impedance to ground. This impedance is the same as its previous se

### NI 5421 Power-Up and Reset Conditions

The signal generator is in the following state from
the time at which the computer begins to power up until the operating system is
fully booted and NI-FGEN is loaded.

- The CH 0 analog output connector is disabled and has
50 Ω or 75 Ω impedance to ground. This
impedance is the same as its previous setting before the device was
powered down. The output voltage amplitude of this connector
is 0 V.
- The CLK IN connector has 50 Ω impedance to
ground.
- PFI 0 and PFI 1 are tristated and have a 1
kΩ impedance to ground.

- In devices with a DDC connector, DIGITAL DATA & CONTROL
output lines are disabled and floating; inputs have a
100 Ω differential termination.

- PXI trigger or RTSI lines are tristated and floating.

After the operating system is fully booted and
NI-FGEN is loaded, or when you perform a hard reset to the device
directly from MAX or using NI-FGEN, the signal generator is in the
following state:

- CH 0 output is enabled.
- CH 0 output attenuation is set to 0 dB.
- Output impedance is set to 50 Ω.
- The Low-Gain Amplifier path is enabled in the Analog Output
path.
- The analog filter is disabled.

- The digital filter of the NI 5421
inside the DAC is disabled.

- CLK IN is disabled and has a 50 Ω
impedance to ground.
- PFI 0 and PFI 1 are tristated and have a 1
kΩ impedance to ground.

- On devices with a DDC connector, all output lines on the DIGITAL DATA
& CONTROL Connector are disabled and floating; inputs have a
100 Ω differential termination.

- PXI trigger or RTSI lines are tristated and floating.
- The sample rate is set to the maximum rate, with the Sample
clock source set to the internal Sample clock timebase.
- The Sample clock timebase is tuned by the internal reference
control voltage.

Parent topic:

NI 5421 NI 5421 Overview

<!--NI_TOPIC bundle=ni-fgen path=ni-5421-preamplifier-attenuation.html language=enus -->
## TOPIC 00332: NI 5421 Preamplifier Attenuation

- bundle_id: `ni-fgen`
- source_path: `ni-5421-preamplifier-attenuation.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5421-preamplifier-attenuation.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The preamplifier attenuation section is before the Low-Gain and High-Gain amplifiers in the analog path. The attenuators provide a range of attenuation from 0 to a maximum of 12 dB in steps of 3 dB. NI-FGEN automatically controls the value of attenuation set in the preamplifier attenuation section d

### NI 5421 Preamplifier Attenuation

The preamplifier attenuation section is before the
Low-Gain and High-Gain amplifiers in the *analog path*. The attenuators provide a
range of attenuation from 0 to a maximum of 12 dB in steps of
3 dB. NI-FGEN automatically controls the value of attenuation set
in the preamplifier attenuation section depending on the set
gain. You can read the value NI-FGEN has selected for preamplifier attenuation using the 
Pre-Amplifier Attenuation property or the 
NIFGEN_ATTR_PRE_AMPLIFIER_ATTENUATION attribute.

Preamplifier attenuation improves the signal
distortion because amplifiers provide lower distortion performance
with smaller signals. However, attenuation lowers the amplitude of
both the signal and the noise in a signal as the signal-to-noise
ratio (SNR) is unchanged upon attenuation. Amplifiers also have a
fixed noise associated with them. The total noise at the amplifier
output is obtained by taking the root of the sum of squares of the
following factors:

- The input signal noise multiplied by the gain of the
amplifier
- The amplifier noise

The total noise is dominated by the larger factor.
If the signal is attenuated so that its noise when multiplied by
gain at the amplifier input is smaller than the amplifier noise,
then the output has a higher SNR. This higher SNR is a good reason
to implement some of the signal generator overall attenuation as preamplifier
attenuation.

Parent topic:

NI 5421 Attenuation

Related concepts:

- NI 5421 Analog Output

<!--NI_TOPIC bundle=ni-fgen path=ni-5421-pxi-block-diagram.html language=enus -->
## TOPIC 00333: NI 5421 PXI Block Diagram

- bundle_id: `ni-fgen`
- source_path: `ni-5421-pxi-block-diagram.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5421-pxi-block-diagram.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: This topic contains information about the NI PXI-5421 top-level block diagram and descriptions of the individual blocks. If it is installed in any slot other than Slot 2 of the PXI chassis, the NI 5421 can receive a signal on the PXI_STAR line and can route a signal on the PXI_STAR line back to Sl

### NI 5421 PXI Block Diagram

This topic contains information about the
NI PXI-5421 top-level block diagram and descriptions of the
individual blocks.

[IMAGE alt='image' src='GUID-99F0CB90-025D-4A7E-ACA2-DC0F55487348-a5.gif']

Note

The following list describes the individual
blocks:

- Onboard Memory stores the waveform data and generation
instructions that you load into the device.
- Clocking allows you to create your Sample clock and
Reference clock.
- The 
 Waveform Generation Engine retrieves the waveform data and
instructions from the 
 Onboard Memory using the Sample clock. The 
 Waveform Generation Engine also uses this clock to
retrieve triggers from 
 Trigger and Event Control .
- The output from the 
 Waveform Generation Engine is sent to the 
 DAC device and the 
 DIGITAL DATA & CONTROL Connector on the front panel
after any digital gain is applied.
- The 
 DAC also contains a selectable 
 Digital Filter , which interpolates and filters the
waveform data.
- The waveform data is sent from the 
 DAC to the 
 Analog Output path where the waveform data is filtered and
amplified.
- The 
 Routing Matrix allows flexible routing of the PXI Trigger
lines (RTSI) and the external PFI lines.

Parent topic:

NI 5421 Theory of Operation

<!--NI_TOPIC bundle=ni-fgen path=ni-5421-sample-size-and-resolution.html language=enus -->
## TOPIC 00334: NI 5421 Sample Size and Resolution

- bundle_id: `ni-fgen`
- source_path: `ni-5421-sample-size-and-resolution.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5421-sample-size-and-resolution.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5421 stores arbitrary waveforms in memory as signed 16-bit digital words. On the NI 5421, the entire 16 bits are sent to the digital gain circuit, the digital filter, and the DAC. Related Topics Onboard Memory Waveform Sizes

### NI 5421 Sample Size and Resolution

The NI 5421 stores arbitrary
waveforms in memory as signed 16-bit digital words. On the
NI 5421, the entire 16 bits are sent to the digital
gain circuit, the digital filter, and the DAC.

Related Topics

*Onboard Memory*

*Waveform Sizes*

Parent topic:

NI 5421 Waveform Generation

Related concepts:

- NI 5421 Onboard Memory
- NI 5421 Waveform Size and Quantum

<!--NI_TOPIC bundle=ni-fgen path=ni-5421-script-mode.html language=enus -->
## TOPIC 00335: NI 5421 Script Mode

- bundle_id: `ni-fgen`
- source_path: `ni-5421-script-mode.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5421-script-mode.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Script Mode allows you to use scripting to link and loop multiple waveforms in complex combinations using a script. A script is a series of instructions that indicates how waveforms saved in the onboard memory should be sent to the DUT. Scripts have many different uses, including specifying the orde

### NI 5421 Script Mode

*Script Mode* allows you to use scripting to link and
loop multiple waveforms in complex combinations using a 
script. A script is a series of instructions that
indicates how waveforms saved in the onboard memory should be sent
to the DUT. Scripts have many different uses, including specifying the order in which the waveforms
are generated, the number of times they are generated, and the
triggers and markers associated with the generation.

Parent topic:

NI 5421 Output Modes

Related concepts:

- Script Mode

<!--NI_TOPIC bundle=ni-fgen path=ni-5421-signal-routing.html language=enus -->
## TOPIC 00336: NI 5421 Signal Routing

- bundle_id: `ni-fgen`
- source_path: `ni-5421-signal-routing.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5421-signal-routing.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: An NI signal generator is capable of sending and receiving signals through the front panel and the PXI or RTSI trigger bus. The front panel connectors provides connectivity for the output channel as well as for control lines for sending and receiving clocks, triggers, and events. You can use the PXI

### NI 5421 Signal Routing

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
2. Expand Devices and Interfaces . 

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

NI 5421 Theory of Operation

Related concepts:

- NI 5421 Syntax for Terminal Names

<!--NI_TOPIC bundle=ni-fgen path=ni-5421-single-trigger-mode.html language=enus -->
## TOPIC 00337: NI 5421 Single Trigger Mode

- bundle_id: `ni-fgen`
- source_path: `ni-5421-single-trigger-mode.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5421-single-trigger-mode.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: When your application is configured for Single trigger mode, only one Start trigger is required to begin waveform generation. All Start triggers after the first Start trigger are ignored. Once the waveform generation is complete, the analog output indefinitely settles at the DC value of the last sam

### NI 5421 Single Trigger Mode

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

NI 5421 Trigger Modes

<!--NI_TOPIC bundle=ni-fgen path=ni-5421-specifications.html language=enus -->
## TOPIC 00338: NI 5421 Specifications

- bundle_id: `ni-fgen`
- source_path: `ni-5421-specifications.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5421-specifications.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: For information about the signal generator specifications, refer to the device specifications. You can access these specifications by navigating to Start»All Programs»National Instruments» NI-FGEN»Documentation»NI Signal Generators Specifications, or you can visit ni.com/manuals.

### NI 5421 Specifications

For information about the signal generator
specifications, refer to the 
*device
specifications*. You can access these specifications by
navigating to 
Start»All Programs»National Instruments»
NI-FGEN»Documentation»NI Signal Generators Specifications, or you can visit 
ni.com/manuals.

Parent topic:

NI 5421 NI 5421 Overview

<!--NI_TOPIC bundle=ni-fgen path=ni-5421-standard-function-mode.html language=enus -->
## TOPIC 00339: NI 5421 Standard Function Mode

- bundle_id: `ni-fgen`
- source_path: `ni-5421-standard-function-mode.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5421-standard-function-mode.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Standard Function output mode is used to generate standard function waveforms such as sine, square, triangle, and so on. On the NI 5421, Standard Function mode is implemented primarily in software. NI-FGEN creates and downloads standard function waveforms to arbitrary waveform memory and generates t

### NI 5421 Standard Function Mode

Standard Function output mode is used to generate standard
function waveforms such as sine, square, triangle, and so on. 
On the NI 5421, *Standard Function mode* is implemented primarily in software. NI-FGEN creates and downloads standard function waveforms to arbitrary waveform memory and generates them the same way that it generates arbitrary waveforms. NI-FGEN automatically selects the best clock mode, sample rate, and buffer size to produce the most accurate waveform possible.

Parent topic:

NI 5421 Output Modes

Related concepts:

- Standard Function Mode

<!--NI_TOPIC bundle=ni-fgen path=ni-5421-stepped-trigger-mode.html language=enus -->
## TOPIC 00340: NI 5421 Stepped Trigger Mode

- bundle_id: `ni-fgen`
- source_path: `ni-5421-stepped-trigger-mode.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5421-stepped-trigger-mode.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The waveform you downloaded generates each time a Start trigger occurs. After a waveform finishes generating, the last sample of the waveform repeats continuously until the next Start trigger is received. When the next Start trigger is received, the waveform generates again. If a Start trigger is re

### NI 5421 Stepped Trigger Mode

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

NI 5421 Trigger Modes

<!--NI_TOPIC bundle=ni-fgen path=ni-5421-streaming.html language=enus -->
## TOPIC 00341: NI 5421 Streaming

- bundle_id: `ni-fgen`
- source_path: `ni-5421-streaming.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5421-streaming.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Streaming is a way to generate waveforms that are too large to fit in the onboard memory of the signal generator. Streaming can be used in Arbitrary Waveform, Arbitrary Sequence, or Script output modes. To stream waveform data, allocate and identify all or a portion of the signal generator onboard m

### NI 5421 Streaming

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
| * All data rates highly dependent on chipset. †Measurements were taken using the Windows API for unbuffered file I/O. For more information about streaming, refer to Data Streaming Architecture in PXI Systems. |  |

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
- When streaming from hard drives, consider the hard drive speed for maximum sustainable rates. Laptop hard drives typically have a data transfer rate of 25 to 30 MB/s. Desktop hard drives often can meet 55 to 70 MB/s. Transfer rates from hard drives can vary for a number of reasons, including where the data is physically stored on the hard drive and how much data is stored. Storing your waveform files on a fairly empty, defragmented hard drive may help increase performance.
- Consider using a redundant array of independent disks (RAID) configuration to utilize striping to increase data transfer rates from disk.
- When using 18-slot PXI chassis, install the signal generator used for streaming in the first segment (Slots 2 to 6) of the PXI chassis.
- Utilize Direct DMA .

Parent topic:

NI 5421 Waveform Generation

Related concepts:

- Arbitrary Waveform Output Mode
- Arbitrary Sequence Mode
- Script Mode
- Direct DMA

<!--NI_TOPIC bundle=ni-fgen path=ni-5421-synchronization.html language=enus -->
## TOPIC 00342: NI 5421 Synchronization

- bundle_id: `ni-fgen`
- source_path: `ni-5421-synchronization.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5421-synchronization.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Your signal generator is based on the National Instruments Synchronization and Memory Core (SMC) technology and therefore supports TClk synchronization. Refer to the NI-TClk Synchronization Help for more information about NI-TClk Synchronization.

### NI 5421 Synchronization

Your signal generator is based on the 
National Instruments
Synchronization and Memory Core (SMC) technology and therefore
supports TClk synchronization. Refer to the 
NI-TClk
Synchronization Help for more information about NI-TClk
Synchronization.

Parent topic:

NI 5421 NI 5421 Overview

<!--NI_TOPIC bundle=ni-fgen path=ni-5421-syntax-for-terminal-names.html language=enus -->
## TOPIC 00343: NI 5421 Syntax for Terminal Names

- bundle_id: `ni-fgen`
- source_path: `ni-5421-syntax-for-terminal-names.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5421-syntax-for-terminal-names.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The syntax for terminal names is a unique identifier that refers to a physical terminal in your system. To guarantee the uniqueness of a terminal name across multiple devices, terminal names begin with a forward slash, followed by the name of the device as configured in MAX, such as Dev1. A forward

### NI 5421 Syntax for Terminal Names

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

NI 5421 Signal Routing

<!--NI_TOPIC bundle=ni-fgen path=ni-5421-theory-of-operation.html language=enus -->
## TOPIC 00344: NI 5421 Theory of Operation

- bundle_id: `ni-fgen`
- source_path: `ni-5421-theory-of-operation.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5421-theory-of-operation.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Expand this topic for information about the theory of operation of your signal generator.

### NI 5421 Theory of Operation

Expand this topic for information about the theory
of operation of your signal generator.

Parent topic:

NI 5421 NI 5421 Overview

<!--NI_TOPIC bundle=ni-fgen path=ni-5421-thermal-shutdown.html language=enus -->
## TOPIC 00345: NI 5421 Thermal Shutdown

- bundle_id: `ni-fgen`
- source_path: `ni-5421-thermal-shutdown.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5421-thermal-shutdown.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: NI-FGEN supports thermal shutdown capability for the NI 5421. This capability allows the signal generator to detect when it has reached a dangerously high temperature and to then power down to prevent damage to the device. Air circulation paths, fan settings, and space allowances are several factors

### NI 5421 Thermal Shutdown

NI-FGEN supports thermal shutdown capability for
the NI 5421. This
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

NI 5421 NI 5421 Overview

<!--NI_TOPIC bundle=ni-fgen path=ni-5421-trigger-modes.html language=enus -->
## TOPIC 00346: NI 5421 Trigger Modes

- bundle_id: `ni-fgen`
- source_path: `ni-5421-trigger-modes.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5421-trigger-modes.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5421 has four trigger modes: Single, Continuous, Stepped, and Burst. These trigger modes are available for Arbitrary Waveform, Arbitrary Sequence, and Frequency List output mode. Refer to the niFgen Configure Trigger Mode VI or the niFgen_ConfigureTriggerMode function for information about se

### NI 5421 Trigger Modes

The NI 5421 has four trigger modes: Single, Continuous, Stepped,
and Burst. These trigger modes are available for Arbitrary
Waveform, Arbitrary Sequence, and Frequency List output mode.
Refer to the 
niFgen
Configure Trigger Mode VI or the 
niFgen_ConfigureTriggerMode function for information about setting the trigger mode.

Parent topic:

NI 5421 Triggering

<!--NI_TOPIC bundle=ni-fgen path=ni-5421-trigger-sources.html language=enus -->
## TOPIC 00347: NI 5421 Trigger Sources

- bundle_id: `ni-fgen`
- source_path: `ni-5421-trigger-sources.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5421-trigger-sources.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Trigger sources are software selectable. You can use any of the following external input triggers: PFI 0 or PFI 1 on the front panel connectors PFI 2 or PFI 3 on the DIGITAL DATA & CONTROL front panel connector RTSI<0..7> (PCI) lines or PXI_TRIG<0..7> lines and PXI_STAR on the PXI trigger bus backpl

### NI 5421 Trigger Sources

Trigger sources are software selectable. You can
use any of the following external input triggers:

- PFI 0 or PFI 1 on the front panel connectors

- PFI 2 or PFI 3 on the DIGITAL DATA & CONTROL front panel
connector

- RTSI<0..7> (PCI) lines or PXI_TRIG<0..7> lines and
PXI_STAR on the PXI trigger bus backplane

The following figure shows the possible trigger
sources for the NI 5421.

[IMAGE alt='image' src='GUID-3D9E272C-29DC-41E1-8DF1-6E390A3EE66C-a5.gif']

§

Exporting Signals

Note

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

*PXI Star Trigger
Line*

Parent topic:

NI 5421 Triggering

Related concepts:

- NI 5421 Exporting Signals
- PXI Trigger Lines
- PXI Star Trigger Line

<!--NI_TOPIC bundle=ni-fgen path=ni-5421-trigger-timing.html language=enus -->
## TOPIC 00348: NI 5421 Trigger Timing

- bundle_id: `ni-fgen`
- source_path: `ni-5421-trigger-timing.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5421-trigger-timing.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the relationship between Start trigger and the waveform output. t[s1] is the required pulse width on the Start trigger signal. t[s2] is the delay from the Start trigger to the waveform output. Refer to the NI PXI/PCI-5421 Specifications for more information about these tim

### NI 5421 Trigger Timing

The following figure shows the relationship between
Start trigger and the waveform output. t<sub>s1</sub> is the required pulse width on the Start trigger
signal. t<sub>s2</sub> is the delay from the Start trigger to the waveform
output. Refer to the 
*NI PXI/PCI-5421
Specifications* for more information about these timing
parameters.

[IMAGE alt='image' src='GUID-9DD6A51C-2BCA-4129-9C8D-0A821181925F-a5.gif']

The NI 5421 also allows you to export
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

NI 5421 Triggering

<!--NI_TOPIC bundle=ni-fgen path=ni-5421-triggering.html language=enus -->
## TOPIC 00349: NI 5421 Triggering

- bundle_id: `ni-fgen`
- source_path: `ni-5421-triggering.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5421-triggering.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can define the signal generator functionality by using the various triggering techniques. Expand this section to learn more about using triggers with your signal generator.

### NI 5421 Triggering

You can define the signal generator functionality
by using the various triggering techniques. Expand this section to
learn more about using triggers with your signal generator.

Parent topic:

NI 5421 NI 5421 Overview

<!--NI_TOPIC bundle=ni-fgen path=ni-5421-waveform-amplitude-control.html language=enus -->
## TOPIC 00350: NI 5421 Waveform Amplitude Control

- bundle_id: `ni-fgen`
- source_path: `ni-5421-waveform-amplitude-control.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5421-waveform-amplitude-control.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5421 uses both amplifiers and attenuators to achieve required amplitude settings. Output Paths and Amplifiers The following figure shows two different gain paths: the Direct path and the Main path with High-Gain and Low-Gain amplifiers. The Direct path provides the output of the main DAC to t

### NI 5421 Waveform Amplitude Control

The NI 5421 uses both amplifiers and
attenuators to achieve required amplitude settings.

#### Output Paths and Amplifiers

The following figure shows two different gain
paths: the Direct path and the Main path with High-Gain and Low-Gain amplifiers.

[IMAGE alt='image' src='GUID-1168A294-D930-4645-8DF7-E4E6E841D015-a5.gif']

The Direct path provides the output of the main DAC
to the CH 0 connector with the fewest electronic components in the path.
There are no programmable amplifiers and there is no method for adding DC
offset to the waveform. The Direct path can generate a maximum of 
1 V<sub>pk-pk</sub> at the CH 0 output into matched load
impedance. The maximum gain setting for an Analog Output path
configured to the Direct path is 0.527 (gain is a unitless
value).

The 
 Low-Gain Amplifier path has a 
2 V<sub>pk-pk</sub> amplifier and is used for waveforms that
have all output voltages equal to or smaller than 
2.0 V<sub>pk-pk</sub> into matched load impedance.
The High-Gain
Amplifier path has a 12 V<sub>pk-pk</sub> amplifier and is used for waveforms that have output voltages greater than 2.0 V<sub>pk-pk</sub> into matched load impedance. The gains of the amplifiers are constant. NI-FGEN automatically selects by default
between the high-gain and low-gain amplifiers, depending on the
NI-FGEN gain setting. You can configure the gain by calling the 
Arbitrary Waveform Gain or 
Amplitude
property or the 
NIFGEN_ATTR_ARB_GAIN or
NIFGEN_ATTR_FUNC_AMPLITUDE attribute.

You can configure the High-Gain or the Low-Gain
Amplifiers to remain in the Analog Output path regardless of gain
setting by calling the 
Analog Path
property or the 
NIFGEN_ATTR_ANALOG_PATH attribute. Configuring the Low-Gain
Amplifier path to remain constant regardless of the gain setting
affects the maximum output value allowable for that particular gain
setting. The maximum gain setting for an Analog Output path
configured to Low-Gain Amplifier path is 2.0
 . The maximum allowable
gain setting with NI-FGEN automatically selecting the Gain
Amplifier path is 12.0
 . Gain is a unitless value.

In addition, the DC offset amplifier, which adds 
*DC offset* to the signal, is
located in the High-Gain and Low-Gain Amplifier paths prior to the
attenuators and amplifiers. The DC offset amplifier can be
fine-tuned to add offset to your signal. This fine-tuning of the
main DC offset amplifier is performed by the offset DAC.

Parent topic:

NI 5421 Analog Output

Related concepts:

- NI 5421 DC Offset

<!--NI_TOPIC bundle=ni-fgen path=ni-5421-waveform-and-generation-instruction-m.html language=enus -->
## TOPIC 00351: NI 5421 Waveform and Generation Instruction Memory Size

- bundle_id: `ni-fgen`
- source_path: `ni-5421-waveform-and-generation-instruction-m.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5421-waveform-and-generation-instruction-m.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Waveform Memory Size Waveforms are stored in the NI 5421 onboard memory in contiguous blocks. These blocks are allocated in multiples of 128 bytes. This allocation style means that while waveform sizes may be multiples of four samples (eight bytes) on the NI 5421 , the amount of onboard memory alloc

### NI 5421 Waveform and Generation Instruction Memory Size

#### Waveform Memory Size

Waveforms are stored in the
NI 5421 onboard memory in contiguous
blocks. These blocks are allocated in multiples of 128 bytes. This
allocation style means that while waveform sizes may be multiples
of four samples (eight bytes) on the NI 5421
, the amount of
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
2. Memory is written to in blocks of 128 bytes.

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

The NI 5421 uses a
waveform generation engine that processes instructions that govern
how a waveform or a sequence of waveforms is generated. These
instructions determine which waveforms are generated, how the
device responds to triggers, how many times a waveform is looped,
when Marker events are generated, and so forth. The instructions
depend on the output mode, trigger mode, trigger source, waveforms
in onboard memory, and sequence lists that are configured. The
instructions are stored in the onboard memory along with the
waveform data. The calculations to determine the instruction size
that is stored in the onboard memory depends on the NI-FGEN output
mode and the NI-FGEN trigger mode. The following table includes
basic equations for determining the amount of memory, in bytes,
that are used for the different generation configurations.

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

Parent topic:

NI 5421 Onboard Memory

<!--NI_TOPIC bundle=ni-fgen path=ni-5421-waveform-generation.html language=enus -->
## TOPIC 00352: NI 5421 Waveform Generation

- bundle_id: `ni-fgen`
- source_path: `ni-5421-waveform-generation.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5421-waveform-generation.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5421 supports the following output, or generation, modes: Standard Function Arbitrary Waveform Arbitrary Sequence Script To select an output mode, set the Output Mode parameter of the niFgen Configure Output Mode VI or the niFgen_ConfigureOutputMode function.

### NI 5421 Waveform Generation

The NI 5421 supports the
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

NI 5421 NI 5421 Overview

Related concepts:

- NI 5421 Standard Function Mode
- NI 5421 Arbitrary Waveform Mode
- NI 5421 Arbitrary Sequence Mode
- NI 5421 Script Mode

<!--NI_TOPIC bundle=ni-fgen path=ni-5421-waveform-quantum.html language=enus -->
## TOPIC 00353: NI 5421 Waveform Quantum

- bundle_id: `ni-fgen`
- source_path: `ni-5421-waveform-quantum.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5421-waveform-quantum.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Quantum is the increment in samples that waveform sizes must adhere to. Waveforms must be downloaded in integer multiples of the four samples (or two for complex samples), the quantum for the NI 5421. For example, if while in Arbitrary Waveform mode, you request to load a waveform of seven samples,

### NI 5421 Waveform Quantum

Quantum is the increment in samples that waveform
sizes must adhere to. Waveforms must be downloaded in integer multiples of the four samples (or two for complex samples), the quantum for the NI 5421.

For example, if while in Arbitrary Waveform mode, you request to load a waveform of seven samples, the task will not complete successfully because the waveform is not an integer multiple of the quantum size. Waveform sizes that meet the conditions include 4, 8, 12, 16, 20, and so on, up to maximum allowable waveform size.

Parent topic:

NI 5421 Waveform Size and Quantum

<!--NI_TOPIC bundle=ni-fgen path=ni-5421-waveform-size-and-quantum.html language=enus -->
## TOPIC 00354: NI 5421 Waveform Size and Quantum

- bundle_id: `ni-fgen`
- source_path: `ni-5421-waveform-size-and-quantum.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5421-waveform-size-and-quantum.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5421 onboard memory architecture imposes certain requirements on the waveform size and quantum.

### NI 5421 Waveform Size and Quantum

The NI 5421 onboard memory architecture
imposes certain requirements on the waveform *size* and *quantum*.

Parent topic:

NI 5421 Waveform Generation

Related concepts:

- NI 5421 Waveform Size
- NI 5421 Waveform Quantum

<!--NI_TOPIC bundle=ni-fgen path=ni-5421-waveform-size.html language=enus -->
## TOPIC 00355: NI 5421 Waveform Size

- bundle_id: `ni-fgen`
- source_path: `ni-5421-waveform-size.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5421-waveform-size.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Minimum Waveform Size The minimum waveform size on the NI 5421 depends on the output mode and the trigger mode. Refer to the device specifications for the minimum waveform size values for the different modes. To provide greater programming flexibility, NI-FGEN does not strictly enforce the minimum

### NI 5421 Waveform Size

#### Minimum Waveform Size

The
minimum waveform size on the NI 5421 depends on the output mode and the 
*trigger mode*. Refer to
the 
*device
specifications* for the minimum waveform size values for the
different modes.

Note

device
specifications

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

NI 5421 Waveform Size and Quantum

Related concepts:

- NI 5421 Trigger Modes
- NI 5421 Waveform and Generation Instruction Memory Size

<!--NI_TOPIC bundle=ni-fgen path=ni-5422-aborting-generation.html language=enus -->
## TOPIC 00356: NI 5422 Aborting Generation

- bundle_id: `ni-fgen`
- source_path: `ni-5422-aborting-generation.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5422-aborting-generation.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can abort the generation of the current waveform. Aborting the generation exhibits different behaviors for different waveform output modes. Output Mode Abort Behavior Standard Function Abort to Ground—Signal remains at the level for which the DC offset is configured. Arbitrary Waveform, Arbitrar

### NI 5422 Aborting Generation

You can abort the generation of the current
waveform. Aborting the generation exhibits different behaviors for
different 
*waveform output
modes*.

| Output Mode | Abort Behavior |
| --- | --- |
| Standard Function | Abort to Ground—Signal remains at the level for which the DC offset is configured. |
| Arbitrary Waveform, Arbitrary Sequence, Script* | Abort to a Known Voltage—Signal remains at the last sample voltage level prior to the abort. |
| * These modes can also abort to ground. |  |

Related Topics

*Aborting to Ground*

*Aborting to a
Known Voltage*

Parent topic:

NI 5422 Waveform Generation

Related concepts:

- NI 5422 Waveform Generation
- Abort to Ground
- Abort to a Known Voltage

<!--NI_TOPIC bundle=ni-fgen path=ni-5422-access-and-active-leds.html language=enus -->
## TOPIC 00357: NI 5422 ACCESS and ACTIVE LEDs

- bundle_id: `ni-fgen`
- source_path: `ni-5422-access-and-active-leds.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5422-access-and-active-leds.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The ACCESS and ACTIVE LEDs indicate the status of the PXI module: ACCESS LED The ACCESS LED indicates basic hardware status as shown in the following table. Color Indications Off Device is not yet functional, or the device has detected a problem with a power rail. Amber The device is being accessed.

### NI 5422 ACCESS and ACTIVE LEDs

The ACCESS and ACTIVE LEDs indicate the status of
the PXI module:

#### ACCESS LED

The ACCESS LED indicates basic hardware status as
shown in the following table.

| Color | Indications |
| --- | --- |
| Off | Device is not yet functional, or the device has detected a problem with a power rail. |
| Amber | The device is being accessed. |
| Green | The device is ready to be programmed by NI-FGEN. |

#### ACTIVE LED

The ACTIVE LED indicates the device state as shown
in the following table.

| Color | Indications |
| --- | --- |
| Off | Device is not generating. |
| Amber | The device is armed and waiting for a trigger. |
| Green | The device has received a trigger. Also indicates that the device is generating a waveform. |
| Red | The device has detected an error. NI-FGEN must access the device to determine the cause of the error. The LED remains red until the error condition is removed. Example errors include the following: PLL Unlocked–The device has detected an unlocked condition on a previously locked PLL. A PLL that is unlocked while in reset does not show an error. The device has powered down because the internal temperature exceeded the maximum limit. The over-temperature condition must be corrected and the device reset. For more information about keeping your device cool, refer to the Maintain Forced-Air Cooling Note to Users included with your signal generator. To reset the device, call the niFgen Reset Device VI or the niFgen_ResetDevice function, or perform a device reset in MAX. |

Parent topic:

NI 5422 Front Panel

<!--NI_TOPIC bundle=ni-fgen path=ni-5422-accessories.html language=enus -->
## TOPIC 00358: NI 5422 Accessories

- bundle_id: `ni-fgen`
- source_path: `ni-5422-accessories.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5422-accessories.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: National Instruments offers a variety of products to use with your signal generator, including cables and other accessories. Visit ni.com for more information.

### NI 5422 Accessories

National Instruments offers a variety of products
to use with your signal generator, including cables and other
accessories. Visit 
ni.com for more
information.

Parent topic:

NI 5422 NI 5422 Overview

<!--NI_TOPIC bundle=ni-fgen path=ni-5422-analog-filter.html language=enus -->
## TOPIC 00359: NI 5422 Analog Filter

- bundle_id: `ni-fgen`
- source_path: `ni-5422-analog-filter.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5422-analog-filter.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The analog filter is a lowpass filter that is used to eliminate aliased images and artifacts due to the digital-to-analog conversion from the signal from the DAC. In general, use the analog filter for signals containing a large portion of sinusoidal content, such as AM and FM, sinc pulse, and sinuso

### NI 5422 Analog Filter

aliased images

niFgen_EnableAnalogFilter

niFgen_DisableAnalogFilter

Note

The delay from the time the device receives a Start
trigger to the time a signal is generated at the analog output
increases if the analog filter in the Analog Output path is
enabled. Refer to the 
*device
specifications* for information about the delay from the trigger
to the analog output based on the configured filter settings.

#### Related Topic

*Filtering and
Interpolation*

Parent topic:

NI 5422 Filtering Effects

Related concepts:

- Aliased Images
- Filtering and Interpolation

<!--NI_TOPIC bundle=ni-fgen path=ni-5422-analog-gain-settings.html language=enus -->
## TOPIC 00360: NI 5422 Analog Gain Settings

- bundle_id: `ni-fgen`
- source_path: `ni-5422-analog-gain-settings.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5422-analog-gain-settings.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following table summarizes the maximum and minimum gain setting that you can apply for the NI-FGEN analog path options. Refer to the device specifications for more information about gain resolution. Analog Path Gain Summary (Matched Load Impedance) NI-FGEN Analog Path Maximum Gain Value Minimum

### NI 5422 Analog Gain Settings

The following table summarizes the maximum and
minimum gain setting that you can apply for the NI-FGEN analog path
options. Refer to the 
*device
specifications* for more information about gain resolution.

| Analog Path Gain Summary (Matched Load Impedance) |  |  |
| --- | --- | --- |
| NI-FGEN Analog Path | Maximum Gain Value | Minimum Gain Value |
| Automatic (default) | 6.000 | 2.817 m |
| Fixed Low-Gain Amplifier | 1.027 | 2.817 m |
| Fixed High-Gain Amplifier | 6.000 | 16.91 m |
| Direct Path | 0.527 | 0.354 |
| Note: Gain is unitless. |  |  |

Note

Parent topic:

NI 5422 Waveform Amplitude Control

<!--NI_TOPIC bundle=ni-fgen path=ni-5422-analog-output.html language=enus -->
## TOPIC 00361: NI 5422 Analog Output

- bundle_id: `ni-fgen`
- source_path: `ni-5422-analog-output.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5422-analog-output.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the NI 5422 Analog Output signal path. NI 5422 analog waveforms are generated as follows: The 16-bit digital waveform data from the Waveform Generation Engine or OSP is passed to a digital gain circuit and then high-speed DAC. This DAC also implements a portion of the Anal

### NI 5422 Analog Output

The following figure shows the NI 5422 Analog Output signal path.

[IMAGE alt='image' src='GUID-1168A294-D930-4645-8DF7-E4E6E841D015-a5.gif']

NI 5422 analog waveforms are
generated as follows:

1. The 16-bit digital waveform data from the Waveform Generation
Engine or OSP is passed to a digital gain circuit and then
high-speed DAC. This DAC also implements a portion of the Analog
Output signal path attenuation with a range of 0 dB to
3 dB. Refer to the NI PXI-5422 Specifications for the exact resolution. You can adjust the amount
of attenuation by configuring the 
Arbitrary
Waveform Gain or 
Amplitude
properties or the 
 NIFGEN_ATTR_ARB_GAIN or 
 NIFGEN_ATTR_FUNC_AMPLITUDE attributes. NI-FGEN calculates and sets the correct amount of
attenuation required, corresponding to the gain setting.
2. Following the DAC, the signal can take one of two paths: the
Direct path or the Main path with High-Gain and Low-Gain
amplifiers. NI-FGEN selects the Main path by default. To select the
Direct path manually, use the 
Analog Path
property or the 
 NIFGEN_ATTR_ANALOG_PATH attribute.
  1. The Direct path bypasses the Analog Filter, the attenuation
sections, and the amplifiers. Taking the amplifiers out of the
signal path yields an output signal with the lowest distortion and
a flat frequency response. Use the Direct path for communication
signals. The Direct path can provide a maximum of 1 V pk-pk output into 50 Ω with no offset and a
maximum of 3 dB attenuation. A signal taking the Direct path
skips steps 3 through 5 and continues at step 6.
  2. If the Main path is selected, the
signal passes through a switchable lowpass Analog Filter,
attenuators, and amplifiers.
3. The signal then passes through a switchable lowpass Analog
Filter to remove 
 Aliased Images . You can
select whether to include the Analog Filter in the Analog Output
path using either the 
niFgen
Configure Analog Filter VI or the 
 niFgen_EnableAnalogFilter or 
 niFgen_DisableAnalogFilter functions.
4. The signal then passes through the DC Offset Amplifier that
adds the desired DC offset voltage. You can adjust the amount of DC
offset added to the signal, up to one half the value of the NI-FGEN
gain setting by using either the 
Arbitrary
Waveform Offset or 
DC Offset
properties or the 
 NIFGEN_ATTR_ARB_OFFSET or 
 NIFGEN_ATTR_FUNC_DC_OFFSET attributes.
5. The signal then passes through the Preamplifier Attenuation section,
a set of selectable solid-state attenuators that provide 0 dB
to 12 dB of attenuation in 3 dB increments. You can adjust the
amount of attenuation by adjusting the Arbitrary Waveform Gain
property or the 
 NIFGEN_ATTR_ARB_GAIN attribute.
NI-FGEN calculates and sets the correct amount of attenuation
required, corresponding to the gain setting configured with the 
Arbitrary
Waveform Gain or 
Amplitude
properties, or the 
 NIFGEN_ATTR_ARB_GAIN or 
 NIFGEN_ATTR_FUNC_AMPLITUDE attributes.
6. Following the Preamplifier Attenuation section, the signal can take
one of two paths: the High-Gain or Low-Gain Amplifier path. The High-Gain Amplifier path is used for waveform output
voltages greater than ±1.0 V into 50 Ω. The
amplifier has a fixed gain and is included in the signal path to
enable the AWG to provide the maximum V pk-pk . The Low-Gain Amplifier path is used for waveforms that have all
output voltages equal to or smaller than ±1.0 V into
50 Ω. The amplifier has a fixed gain. NI-FGEN
automatically selects the best amplifier path between the High-Gain
and Low-Gain amplifiers by default based on the gain or amplitude
setting. Alternatively, you can use the 
Analog Path
property or the 
 NIFGEN_ATTR_ANALOG_PATH attribute to set the signal path to remain
constant regardless of the gain setting for applications requiring
one path or the other.
7. The signal passes through the Postamplifier Attenuation section, a
set of two passive attenuators 12 dB and 24 dB. You can adjust the
amount of attenuation by configuring either the 
Arbitrary
Waveform Gain or 
Amplitude
properties, or the 
 NIFGEN_ATTR_ARB_GAIN or 
 NIFGEN_ATTR_FUNC_AMPLITUDE attributes. NI-FGEN calculates and sets the correct amount of
attenuation required, corresponding to the gain setting.
8. The signal then passes through the Output Enable relay. When
the Output Enable relay is disabled, ground is connected to the
output through a 50 Ω or a 75 Ω resistor.
Intentionally, waveform generation continues while the output
enable relay is disabled. When the relay is enabled, the analog
waveform is seen at the CH 0 connector. You can enable or
disable the output of the analog waveform generator by using the 
niFgen Output
Enable VI or the 
 niFgen_ConfigureOutputEnabled function.
9. The signal then passes through a
50 Ω/75 Ω selector to the
CH 0 connector. You can configure the output impedance of
the analog waveform generator by using the 
niFgen
Configure Output Impedance VI or the 
 niFgen_ConfigureOutputImpedance function.

Note

Parent topic:

NI 5422 Theory of Operation

Related concepts:

- Aliased Images

<!--NI_TOPIC bundle=ni-fgen path=ni-5422-arbitrary-sequence-mode.html language=enus -->
## TOPIC 00362: NI 5422 Arbitrary Sequence Mode

- bundle_id: `ni-fgen`
- source_path: `ni-5422-arbitrary-sequence-mode.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5422-arbitrary-sequence-mode.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Arbitrary Sequence mode allows you to load multiple waveforms in the onboard memory of the NI 5422. A finite number of samples make a waveform. To generate these downloaded waveforms in a specific order, you must prepare a sequence, which contains a number of segments in a specific order. Each segme

### NI 5422 Arbitrary Sequence Mode

*Arbitrary Sequence mode* allows you to load multiple
waveforms in the onboard memory of the NI 5422. A finite
number of samples make a waveform. To generate these downloaded
waveforms in a specific order, you must prepare a sequence, which
contains a number of segments in a specific order. Each segment
specifies a downloaded waveform, a number of loops to repeat the
selected waveform, and a numeric offset in which a marker is
generated by the device.

Parent topic:

NI 5422 Output Modes

Related concepts:

- Arbitrary Sequence Mode

<!--NI_TOPIC bundle=ni-fgen path=ni-5422-arbitrary-waveform-mode.html language=enus -->
## TOPIC 00363: NI 5422 Arbitrary Waveform Mode

- bundle_id: `ni-fgen`
- source_path: `ni-5422-arbitrary-waveform-mode.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5422-arbitrary-waveform-mode.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5422 supports Arbitrary Waveform output mode. Arbitrary Waveform mode generates waveforms from user-created/provided waveform arrays of numeric data. The waveform arrays are downloaded to the arbitrary waveform generator onboard memory. Arbitrary Waveform mode also uses memory to store the in

### NI 5422 Arbitrary Waveform Mode

The NI 5422 supports Arbitrary Waveform output mode. Arbitrary Waveform mode generates waveforms from
user-created/provided waveform arrays of numeric data. The waveform
arrays are downloaded to the arbitrary waveform generator onboard
memory. *Arbitrary Waveform mode* also uses memory to
store the instructions for generating waveform sequences in the
onboard memory.

Parent topic:

NI 5422 Output Modes

Related concepts:

- Arbitrary Waveform Output Mode

<!--NI_TOPIC bundle=ni-fgen path=ni-5422-attenuation.html language=enus -->
## TOPIC 00364: NI 5422 Attenuation

- bundle_id: `ni-fgen`
- source_path: `ni-5422-attenuation.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5422-attenuation.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Analog Output path has two passive attenuation sections. Preamplifier attenuation is prior to the High-Gain and Low-Gain Amplifier paths, and postamplifier attenuation is after the High-Gain and Low-Gain Amplifier paths. The main DAC provides 0 to 3 dB of signal attenuation. Amplitude control is

### NI 5422 Attenuation

The Analog Output path has two passive attenuation
sections. *Preamplifier attenuation* is prior to the High-Gain
and Low-Gain Amplifier paths, and *postamplifier attenuation* is after the
High-Gain and Low-Gain Amplifier paths.

The main *DAC* provides 0 to 3 dB of signal attenuation. Amplitude control is implemented after the DAC. Attenuating the DAC output signal allows you to vary the signal amplitude while maintaining the dynamic range of the DAC. You do not lose any bits from the digital representation of the signal and you do not sacrifice dynamic range, as you would if you control amplitude by using smaller data ranges of the DAC. Passive attenuation by preamplifier and postamplifier attenuation is not available if the Direct path is selected.

For the Low-Gain and the High-Gain Amplifier paths, maximum attenuation is
51 dB. For the Direct path, maximum output attenuation is 3
dB. NI-FGEN automatically determines the correct value of attenuation in dB and configures the attenuation based on the set
gain. The minimum gain setting for the Direct path is 0.354. The
minimum gain setting for an Analog Output path configured to
High-Gain Amplifier path is .01691. The minimum allowable gain
setting with NI-FGEN automatically selecting the Low-Gain Amplifier
path is .00282 (gain is a unitless value).

NI-FGEN calculates and sets the correct amount of
attenuation required that corresponds to your NI-FGEN gain setting.
The correct amount of attenuation is implemented in the 
preamplifier and postamplifier attenuation blocks to best achieve
the desired output signal amplitude. You can set the amount of gain
with the Arbitrary Waveform Gain property or the 
NIFGEN_ATTR_ARB_GAIN attribute.

Parent topic:

NI 5422 Waveform Amplitude Control

Related concepts:

- NI 5422 Preamplifier Attenuation
- NI 5422 Postamplifier Attenuation
- NI 5422 DAC Attenuation

<!--NI_TOPIC bundle=ni-fgen path=ni-5422-block-diagram.html language=enus -->
## TOPIC 00365: NI 5422 Block Diagram

- bundle_id: `ni-fgen`
- source_path: `ni-5422-block-diagram.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5422-block-diagram.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: This topic contains information about the NI PXI-5422 top-level block diagram and descriptions of the individual blocks. If it is installed in any slot other than Slot 2 of the PXI chassis, the NI 5422 can receive a signal on the PXI_STAR line and can route a signal on the PXI_STAR line back to Sl

### NI 5422 Block Diagram

This topic contains information about the
NI PXI-5422 top-level block diagram and descriptions of the
individual blocks.

[IMAGE alt='image' src='GUID-38C484AE-611B-42E0-8557-E3A4131FBE56-a5.gif']

Note

The following list describes the individual
blocks:

- Onboard Memory stores the waveform data and generation
instructions that you load into the device.
- Clocking allows you to create your Sample clock and
Reference clock.
- The 
 Waveform Generation Engine retrieves the waveform data and
instructions from the 
 Onboard Memory using the Sample clock. The 
 Waveform Generation Engine also uses this clock to
retrieve triggers from 
 Trigger and Event Control .
- The output from the 
 Waveform Generation Engine is sent to the 
 DAC and the 
 DIGITAL DATA & CONTROL Connector on the front panel
after any digital gain is applied.
- The waveform data is sent from the 
 DAC to the 
 Analog Output path where the waveform data is filtered and
amplified.
- The 
 Routing Matrix allows flexible routing of the PXI Trigger
lines (RTSI) and the external PFI lines.

Parent topic:

NI 5422 Theory of Operation

<!--NI_TOPIC bundle=ni-fgen path=ni-5422-burst-trigger-mode.html language=enus -->
## TOPIC 00366: NI 5422 Burst Trigger Mode

- bundle_id: `ni-fgen`
- source_path: `ni-5422-burst-trigger-mode.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5422-burst-trigger-mode.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: In Burst trigger mode, calling the first Start trigger begins waveform generation. The waveform then generates continually. The following table provides more information about waveform generation behavior in Arbitrary Waveform and Arbitrary Sequence output modes. Output Mode Trigger Behavior Arbitra

### NI 5422 Burst Trigger Mode

In Burst trigger mode, calling the first Start
trigger begins waveform generation. The waveform then generates
continually. The
following table provides more information about
waveform generation behavior in Arbitrary Waveform and Arbitrary
Sequence output modes.

| Output Mode | Trigger Behavior |
| --- | --- |
| Arbitrary Waveform Mode | Burst trigger mode operates the same as Continuous trigger mode when the device is operating in Arbitrary Waveform mode. |
| Arbitrary Sequence Mode | Each waveform you define in the sequence list generates continuously until another Start trigger occurs. A Start trigger causes the waveform generation to switch to the waveform defined by the next segment, after the current waveform finishes. After the sequence list is exhausted, the waveform generation returns to the waveform defined by the first segment and subsequent Start triggers will restart the process. Only the first Start trigger which signals a transition to the next segment is recognized, all subsequent Start triggers are ignored until the currently generating waveform finishes. The transition of one waveform to the next can be made amplitude continuous if waveforms in all segments start and end at the same amplitude. Alternatively, this also can be accomplished by ensuring that the waveforms from one segment to the next end and start at the same amplitude. This amplitude continuous transition is shown in the previous Arbitrary Sequence Mode examples by the transitions of Segments 1 to Segment 2, and Segment 3 to Segment 4. The transition from Segment 2 to Segment 3 shows a discontinuous transition, going from a positive value on the last sample of the ramp waveform right to a midrange value of the sine waveform. |

Parent topic:

NI 5422 Trigger Modes

Related concepts:

- NI 5422 Continuous Trigger Mode

<!--NI_TOPIC bundle=ni-fgen path=ni-5422-calibration.html language=enus -->
## TOPIC 00367: NI 5422 Calibration

- bundle_id: `ni-fgen`
- source_path: `ni-5422-calibration.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5422-calibration.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Before shipping your signal generator, NI calibrated your device to ensure that all features are within specifications. Calibration is a set of operations that compares the values indicated by a measuring instrument or measuring system to the corresponding values realized by external standards. You

### NI 5422 Calibration

Before shipping your signal generator,
NI calibrated your device to ensure that all features are
within specifications.

Calibration is a set of operations that compares
the values indicated by a measuring instrument or measuring system
to the corresponding values realized by external standards. You can
use the results of calibration to determine the measurement error
and can then correct for it in the adjustment process.

The calibration process consists of verifying,
adjusting, and reverifying a device. During verification, you
compare the measured performance to an external standard of known
measurement uncertainty to confirm that the product meets or
exceeds specifications. During adjustment, you correct the
measurement error of the device by adjusting the calibration
constants and storing the new calibration constants in the EEPROM.
The host computer reads the calibration constants and the software
uses them to compensate for errors in the data and to present
calibrated data to the user.

For more information about calibrating the signal
generator, refer to the 
*device calibration*
procedures.

For more information about calibration in general,
refer to ni.com/calibration.

Parent topic:

NI 5422 NI 5422 Overview

<!--NI_TOPIC bundle=ni-fgen path=ni-5422-ch-0-connector.html language=enus -->
## TOPIC 00368: NI 5422 CH 0 Connector

- bundle_id: `ni-fgen`
- source_path: `ni-5422-ch-0-connector.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5422-ch-0-connector.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The CH 0 connector is the analog waveform output terminal. The maximum output levels from this connector depend on the type of load termination. For example, if the output of the device terminates into a 50 Ω load, the maximum output levels are ±6 V, while the maximum output levels are ±12 V when th

### NI 5422 CH 0 Connector

The CH 0 connector is the analog waveform
output terminal. The maximum output levels from this connector
depend on the type of load termination. For example, if the output of the device
terminates into a 50 Ω load, the maximum output levels
are ±6 V, while the maximum output levels are ±12 V when the
device terminates into a high-impedance load (HiZ). This difference
is illustrated in the following figure.

[IMAGE alt='image' src='GUID-836822F7-163C-475A-B0EB-3D94BB52CBAB-a5.gif']

If the output terminates into any other load, the
levels are defined by the following formula:

V<sub>out</sub>
 = ± [ 
R<sub>L</sub>
 / ( 
R<sub>L</sub>
 + 
R<sub>O</sub>
 ) ] × 12 V

where

V<sub>out</sub> is the maximum peak output voltage level

R<sub>L</sub>
 is the load impedance in ohms

O

Note

out

By default, 
R<sub>O</sub>
 = 50 Ω, but you can set the output
impedance to 75 Ω in NI-FGEN. You can configure the output impedance by calling the 
niFgen Configure Output Impedance VI or the 
niFgen_ConfigureOutputImpedance function.

You can set the amplitude of the generated output
signal in terms of peak voltage by setting the gain value. NI-FGEN
calculates and sets the correct amount of attenuation required for
the desired gain value. You can configure the output signal amplitude by calling the Amplitude property
 or NIFGEN_ATTR_FUNC_AMPLITUDE attribute, or the
 
Arbitrary Waveform Gain property or
NIFGEN_ATTR_ARB_GAIN attribute.

#### Load Impedance Compensation

The NI 5422 has the ability to configure the
output signal amplitude based on a user-configured load impedance
setting. This capability is desirable when you use the NI 5422
with loads that are between 0 Ω and a high impedance.
Refer to the 
*device
specifications* for information about the output impedance
tolerance.

By default, NI-FGEN assumes that the load impedance
is equal to the output impedance. If they do not match, you can
change the load impedance value that NI-FGEN uses in its load
impedance compensation algorithm. NI-FGEN takes the load impedance
into account when setting the amplitude and provides the amplitude
specified in the configured gain setting, eliminating the need to use
the voltage divider equation. NI-FGEN compensates to give the
desired peak-to-peak voltage amplitude or arbitrary gain (relative to 1 V). You can configure the load impedance by calling the 
Load
Impedance property or 
NIFGEN_ATTR_LOAD_IMPEDANCE attribute.

Note

For waveform output
signal specifications, refer to the 
*device
specifications*.

Parent topic:

NI 5422 Front Panel

<!--NI_TOPIC bundle=ni-fgen path=ni-5422-clk-in-connector.html language=enus -->
## TOPIC 00369: NI 5422 CLK IN Connector

- bundle_id: `ni-fgen`
- source_path: `ni-5422-clk-in-connector.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5422-clk-in-connector.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The CLK IN front panel connector can accept an external Reference clock, external Sample clock, or external Sample clock timebase. Do not change the external clocks while generating waveforms. Only modify the frequency of the external clock before you start the waveform generation or after you sto

### NI 5422 CLK IN Connector

Caution

not

before

after

#### External Reference Clock Input

The CLK IN connector can accept a Reference clock
from an external source and phase-lock the internal clock of the
signal generator to this external Reference clock. Refer to the 
*device
specifications* for the allowable Reference clock frequencies
and signal characteristics.

The Reference clock uses the internal clock by
default. Call the 
niFgen
Configure Reference Clock VI or the 
niFgen_ConfigureReferenceClock function to configure the Reference
clock source.

When configuring an external Reference clock, you
must configure the external Reference clock frequency if it is
different from the 10 MHz default setting. Set the Reference clock frequency with the 
niFgen
Configure Reference Clock VI or the niFgen_ConfigureReferenceClock function.

Note

PLL Reference
Sources

#### External Sample Clock Input

In addition to phase-locking, the CLK IN connector
also can receive an external Sample clock. Refer to the 
*device
specifications* for the allowable external Sample clock
frequencies and signal characteristics.

Tip

niFgen_ConfigureSampleRate

Configure the Sample clock source with 
niFgen
Configure Sample Clock Source VI or the 
niFgen_ConfigureSampleClockSource function. The Sample clock uses the internal clock by
default.

Parent topic:

NI 5422 Front Panel

Related concepts:

- NI 5422 Phase-Locked Loop Reference Clock

<!--NI_TOPIC bundle=ni-fgen path=ni-5422-clocking-options.html language=enus -->
## TOPIC 00370: NI 5422 Clocking Options

- bundle_id: `ni-fgen`
- source_path: `ni-5422-clocking-options.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5422-clocking-options.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Waveform generation is driven by the Sample clock; depending on your application, some sources may be better choices than others. You can use the following sources for the NI 5422 Sample clock: Internal Sample clock—the onboard clock is used as the Sample clock source and the Sample clock is derived

### NI 5422 Clocking Options

Waveform generation is driven by the Sample clock;
depending on your application, some sources may be better choices
than others. You can use the following sources for the
NI 5422 Sample clock:

- Internal Sample clock —the onboard clock is used as the
Sample clock source and the Sample clock is derived from the Sample
clock timebase via either Divide by N or High–Resolution clock
mode.
- External Sample clock —the Sample clock has an external
source that derives device clocking by directly driving the DAC and all waveform generation operations on the device.
- Reference clock —the Sample clock is derived from an
external source that is phase–locked to the Sample clock
timebase. The phase-locked loop (PLL) Reference clock source
specifies the source of the control voltage that tunes the VCXO of
the Sample clock timebase for internal clock update sources. The
PLL circuit adjusts the Sample clock timebase VCXO to synchronize
to a Reference clock. The frequency stability of the Sample clock
timebase matches that of the PLL Reference clock when the two are
phase-locked. Phase-locking also synchronizes multiple device
clocks that are phase–locked to the same Reference clock.

The following table shows the valid NI-FGEN
property or attribute value combinations that can be used to
configure the NI 5422 clock settings for
an internal Sample clock, an external Sample clock, or a Reference
clock. The term 
Update clock is synonymous with 
Sample clock.

| Sample Clock Source* | Clock Mode * | PLL Reference Clock Source * |
| --- | --- | --- |
| "OnboardClk" (default) | NIFGEN_VAL_DIVIDE_DOWN | "None" (default) |
| "PXI_CLK10", "RTSI7" |  |  |
| "ClkIn" |  |  |
| "OnboardRefClk" |  |  |
| NIFGEN_VAL_HIGH_RESOLUTION | "None" (default) |  |
| "PXI_CLK10", "RTSI7" |  |  |
| "ClkIn" |  |  |
| "OnboardRefClk" |  |  |
| NIFGEN_VAL_AUTOMATIC (default) | "None" (default) |  |
| "PXI_CLK10", "RTSI7" |  |  |
| "ClkIn" |  |  |
| "OnboardRefClk" |  |  |
| "ClkIn" | Not Applicable | Not Applicable |
| "PXI_STAR" |  |  |
| "PXI_Trig<0..6>" |  |  |
| "DDC_ClkIn" |  |  |
| *These column headings refer to NI-FGEN properties. The attributes that correspond to these properties are NIFGEN_ATTR_SAMPLE_CLOCK_SOURCE, NIFGEN_ATTR_CLOCK_MODE, and NIFGEN_ATTR_REFERENCE_CLOCK_SOURCE. The values in the columns represent the values that can be set on these properties or attributes. Settings that line up horizontally show valid combinations of the NI-FGEN settings. |  |  |

Parent topic:

NI 5422 Clocking

Related concepts:

- NI 5422 Internal Sample Clock
- NI 5422 External Sample Clock
- NI 5422 Phase-Locked Loop Reference Clock

<!--NI_TOPIC bundle=ni-fgen path=ni-5422-clocking.html language=enus -->
## TOPIC 00371: NI 5422 Clocking

- bundle_id: `ni-fgen`
- source_path: `ni-5422-clocking.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5422-clocking.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5422 has a Sample clock rate of 5 MHz to 200 MHz. The timing of the device is very flexible, and you have multiple choices for deriving the Sample clock. There are modes for deriving the Sample clock from the internal Sample clock timebase, as well as modes to provide external clocks. You als

### NI 5422 Clocking

The NI 5422 has a Sample
clock rate of 5 MHz to 200 MHz. The timing of the device
is very flexible, and you have multiple choices for deriving the
Sample clock. There are modes for deriving the Sample clock from
the internal Sample clock timebase, as well as modes to provide
external clocks. You also have several choices for providing the
frequency reference for the onboard phase-locked loop.

[IMAGE alt='image' src='GUID-E29E53C4-1CBC-4D93-BB7D-9772D14E126A-a5.gif']

Note

Related Topics

*Clocking Options*

*Internal Sample Clock
Sources*

*Phase-Locked Loop
Reference Clock Sources*

*External Sample
Clock Sources*

*Exporting Clocks*

Parent topic:

NI 5422 Theory of Operation

Related concepts:

- NI 5422 Clocking Options
- NI 5422 Internal Sample Clock
- NI 5422 Phase-Locked Loop Reference Clock
- NI 5422 External Sample Clock
- NI 5422 Exporting Clocks

<!--NI_TOPIC bundle=ni-fgen path=ni-5422-continuous-trigger-mode.html language=enus -->
## TOPIC 00372: NI 5422 Continuous Trigger Mode

- bundle_id: `ni-fgen`
- source_path: `ni-5422-continuous-trigger-mode.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5422-continuous-trigger-mode.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The waveform you downloaded generates continuously after receiving one Start trigger. All Start triggers after the first Start trigger are ignored. The following table provides more information about waveform generation behavior in Arbitrary Waveform and Arbitrary Sequence output modes. Output Mode

### NI 5422 Continuous Trigger Mode

The waveform you downloaded generates continuously
after receiving one Start trigger. All Start triggers after the
first Start trigger are ignored. The
following table provides more information about
waveform generation behavior in Arbitrary Waveform and Arbitrary
Sequence output modes.

| Output Mode | Trigger Behavior |
| --- | --- |
| Arbitrary Waveform Mode | The waveform you downloaded generates continuously after receiving one Start trigger. All Start triggers after the first Start trigger are ignored. |
| Arbitrary Sequence Mode | The waveform pattern you define in the sequence list generates continuously by continually cycling through the sequence list. Only one Start trigger is required to start waveform generation. After the device receives a Start trigger, the waveform generation starts at the first segment and continues through the last segment, and then loops back to the start of the first segment, continuing indefinitely. All Start triggers after the first Start trigger that starts waveform generation are ignored. |

Parent topic:

NI 5422 Trigger Modes

<!--NI_TOPIC bundle=ni-fgen path=ni-5422-dac-attenuation.html language=enus -->
## TOPIC 00373: NI 5422 DAC Attenuation

- bundle_id: `ni-fgen`
- source_path: `ni-5422-dac-attenuation.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5422-dac-attenuation.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The main DAC output can be fine-tuned for attenuation, which provides 0 to 3 dB of the Analog Output path signal attenuation. This fine-tuning of the main DAC attenuation is performed by the gain DAC. Adjust the gain DAC using the Gain DAC Value property or the NIFGEN_ATTR_GAIN_DAC_VALUE attribute.

### NI 5422 DAC Attenuation

The main DAC output can be fine-tuned for
attenuation, which provides 0 to 3 dB of the Analog Output
path signal attenuation. This fine-tuning of the main DAC
attenuation is performed by the gain DAC. Adjust the gain
DAC using the 
Gain
DAC Value property or the 
NIFGEN_ATTR_GAIN_DAC_VALUE attribute. The main DAC also
provides the fine resolution for the attenuation settings.

Parent topic:

NI 5422 Attenuation

<!--NI_TOPIC bundle=ni-fgen path=ni-5422-data-mask.html language=enus -->
## TOPIC 00374: NI 5422 Data Mask

- bundle_id: `ni-fgen`
- source_path: `ni-5422-data-mask.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5422-data-mask.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The signal generator supports analog and digital data masks and static values. The data mask allows you to shield bits of the data to be replaced with the corresponding static value bits. For example, a mask of 0xFF00 and a static value of 0xAAAA applied to a DC waveform with a value of 0x1111 produ

### NI 5422 Data Mask

The signal generator supports analog and digital
data masks and static values. The data mask allows you to shield
bits of the data to be replaced with the corresponding static value
bits. For example, a mask of 0xFF00 and a static value of 0xAAAA
applied to a DC waveform with a value of 0x1111 produces a DC
waveform with a value of 0x11AA.

NI-FGEN supports separate and independent analog
and digital data masks and static values. The analog data mask and
analog static value apply to the digital data applied to the DAC,
and ultimately to the signal on the analog output terminal. The
analog data mask and analog static value do not affect the signals
on the digital connector. You can configure an analog data mask by calling the 
Analog Data
Mask or 
Analog
Static Value properties or the 
NIFGEN_ATTR_ANALOG_DATA_MASK and 
NIFGEN_ATTR_ANALOG_STATIC_VALUE attributes. The digital data mask and digital static value
apply to the signals on the digital connector and they do not
affect the signal on the analog output terminal. You can configure a digital data mask by calling the 
Digital
Data Mask or 
Digital
Static Value properties or the 
NIFGEN_ATTR_DIGITAL_DATA_MASK and 
NIFGEN_ATTR_DIGITAL_STATIC_VALUE attributes.

Parent topic:

NI 5422 NI 5422 Overview

<!--NI_TOPIC bundle=ni-fgen path=ni-5422-dc-offset.html language=enus -->
## TOPIC 00375: NI 5422 DC Offset

- bundle_id: `ni-fgen`
- source_path: `ni-5422-dc-offset.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5422-dc-offset.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5422 supports a DC offset before the attenuation chain that affects the maximum value of DC offset for a given gain setting. This preattenuation architecture requires two rules for setting the DC offset: The magnitude of the maximum value of offset can be no more than the gain setting for the

### NI 5422 DC Offset

The NI 5422 supports a DC offset before the attenuation chain that affects the maximum value of DC offset for a given gain setting. This preattenuation architecture requires two rules for setting the DC offset:

1. The magnitude of the maximum value of offset can be no more than the gain setting for the NI 5422.
2. The waveform maximum plus the offset must not exceed 
 ±6 V into 50 Ω; if it does, the waveform is clipped. For example, if you have set a gain of 
 5, which corresponds to an amplitude of 
 5 V pk , and the waveform is a sine wave using the full range of the DAC, the maximum DC offset you can apply without clipping the sine wave is 
 ±1 V. At this point, output voltages of the sine waveform have reached the maximum amplitude that the device supports. If you increase the DC offset further, the top portion of the waveform at 
 6 V is clipped.

NI-FGEN automatically calculates the preattenuation
offset value based on the set DC offset and gain values. The DC offset can be changed at any time during waveform generation by calling the 
Arbitrary Waveform Offset property or the 
NIFGEN_ATTR_ARB_OFFSET attribute.

The DC offset cannot be set if you selected the
Direct path. The Direct path offset is near zero. Refer to the 
*device
specifications* for information about the maximum value of the
DC offset.

Parent topic:

NI 5422 Waveform Amplitude Control

<!--NI_TOPIC bundle=ni-fgen path=ni-5422-digital-data-control-connector.html language=enus -->
## TOPIC 00376: NI 5422 DIGITAL DATA & CONTROL Connector

- bundle_id: `ni-fgen`
- source_path: `ni-5422-digital-data-control-connector.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5422-digital-data-control-connector.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The DIGITAL DATA & CONTROL (DDC) front panel connector is a 68-pin female VHDCI connector that contains the 16-bit LVDS digital pattern output. The DDC connector is an optional feature for the NI 5422. DIGITAL DATA & CONTROL Pin Assignments The following figure shows the NI 5422 DDC 68-pin connector

### NI 5422 DIGITAL DATA & CONTROL Connector

The DIGITAL DATA & CONTROL (DDC) front panel
connector is a 68-pin female VHDCI connector that contains the
16-bit LVDS digital pattern output. The DDC connector is an
optional feature for the NI 5422.

#### DIGITAL DATA & CONTROL Pin
Assignments

The following figure shows the
NI 5422 DDC 68-pin connector.

[IMAGE alt='image' src='GUID-73285A03-5DAA-4DED-BC9D-A39AD44D354A-a5.gif']

The following table lists the pin names and signal
descriptions used for the NI 5422 DDC connector. All
lines are at standard 
*LVDS* levels.

| Signal Name | Type | Description |
| --- | --- | --- |
| D<0..15> | Output | Digital pattern outputs–The 16-bit digital representation of the analog waveform is available on these output pins as digital pattern outputs. This data is available directly from the memory after several Sample clock pipeline delays. The digital pattern outputs are standard LVDS output levels. All data bits change on the falling edge of the DDC CLK OUT. |
| DDC CLK IN | Input | Digital Data Clock In–These lines are used as a source for an external Sample clock. You can feed a LVDS level clock to this line with a maximum frequency of the signal generator. |
| DDC CLK OUT | Output | Digital Data Clock Out–The Sample clock is always routed to the DDC CLK OUT line of the DDC front panel connector when the digital pattern is enabled. |
| Ground | – | Digital ground |
| PFI<2..3> (Inputs) | Input | PFI<2:3>–These PFI lines can accept a trigger from an external source that can start or step through waveform generation. You can select this functionality on the NI 5422 through the software. Refer to Trigger Sources for more information. |
| PFI<4:5> | Output | PFI<4..5>–These PFI lines can route out a signal from Marker events or the Out Start trigger. |
| Reserved | – | Reserved for future use. Do not connect signals to this line. |
| Refer to the device specifications for information about acceptable input signal characteristics to connect to the DDC lines, as well as the output signal characteristics. |  |  |

You must enable the DDC connector before the
signals in this table are available for use. You can enable digital patterning by calling the
niFgen
Configure Digital Patterning VI or the 
niFgen_EnableDigitalPatterning and 
niFgen_DisableDigitalPatterning functions.

Parent topic:

NI 5422 Front Panel

Related concepts:

- NI 5422 Low-Voltage Differential Signaling (LVDS)
- NI 5422 Trigger Sources

<!--NI_TOPIC bundle=ni-fgen path=ni-5422-digital-gain.html language=enus -->
## TOPIC 00377: NI 5422 Digital Gain

- bundle_id: `ni-fgen`
- source_path: `ni-5422-digital-gain.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5422-digital-gain.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Digital gain multiplies waveform data by a factor you specify in the Digital Gain property or the NIFGEN_ATTR_DIGITAL_GAIN attribute before converting the data to an analog signal in the DAC. Digital gain can be changed during generation without the glitches caused by switching that are common when

### NI 5422 Digital Gain

Digital gain multiplies waveform data by a factor
you specify in the 
Digital Gain
property or the 
NIFGEN_ATTR_DIGITAL_GAIN attribute before converting the data to an analog signal in
the DAC. Digital gain can be changed during generation without the
glitches caused by switching that are common when changing
analog gains. However, the output resolution of the DAC is a
function of digital gain, meaning that only analog gain makes full use of the
resolution of the DAC.

Parent topic:

NI 5422 Waveform Amplitude Control

<!--NI_TOPIC bundle=ni-fgen path=ni-5422-direct-dma.html language=enus -->
## TOPIC 00378: NI 5422 Direct DMA

- bundle_id: `ni-fgen`
- source_path: `ni-5422-direct-dma.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5422-direct-dma.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Direct DMA can transfer waveform data to the signal generator onboard memory at rates well beyond the typical 5 to 30 MB/s range in a standard PC-based architecture. To achieve such high rates, direct DMA establishes a direct connection between the signal generator onboard memory and a specialized w

### NI 5422 Direct DMA

*Direct DMA* can transfer waveform data to the signal generator onboard memory at rates well beyond the typical 5 to 30 MB/s range in a standard PC-based architecture. To achieve such high rates, direct DMA establishes a direct connection between the signal generator onboard memory and a specialized waveform data source. Direct DMA is commonly used to *stream* waveform data from disk at data rates of 100+ MB/sec. Conduant's StreamStor™ products are one example of direct DMA-compatible data sources.

#### Related Topics

*Configuring an Application for Direct DMA*

*DMA Fundamentals*

Parent topic:

NI 5422 Streaming

Related concepts:

- Direct DMA
- Streaming
- Configuring Your Application for Direct DMA

<!--NI_TOPIC bundle=ni-fgen path=ni-5422-events.html language=enus -->
## TOPIC 00379: NI 5422 Events

- bundle_id: `ni-fgen`
- source_path: `ni-5422-events.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5422-events.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use events to indicate when a specific hardware condition has been met on the NI 5422. An event is a signal generated by the NI device at a device state. The NI 5422 supports Ready for Start, Started, Data Marker, Marker, and Done events. The NI 5422 also supports the use of event delays. Re

### NI 5422 Events

You can use *events* to indicate when a specific
hardware condition has been met on the NI 5422. An event is a
signal generated by the NI device at a device state. The NI 5422
supports Ready for Start, Started, *Data Marker*, *Marker*, and Done
events. The NI 5422 also supports the use of *event delays*.

#### Related Topics

*Creating a Marker
Event*

*Creating a Data Marker
Event*

Parent topic:

NI 5422 NI 5422 Overview

Related concepts:

- Events
- Data Marker Events
- Marker Events
- Event Delays
- Creating a Marker Event
- Creating a Data Marker Event

<!--NI_TOPIC bundle=ni-fgen path=ni-5422-exporting-clocks.html language=enus -->
## TOPIC 00380: NI 5422 Exporting Clocks

- bundle_id: `ni-fgen`
- source_path: `ni-5422-exporting-clocks.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5422-exporting-clocks.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5422 provides resources for exporting your clocks and multiple destinations for routing. The following table shows the available clock signals that can be routed to devices external to the signal generator and the destination options. Clock to be Exported Destination Options Sample Clock PFI

### NI 5422 Exporting Clocks

The NI 5422 provides resources for exporting your clocks and multiple destinations for
routing.

[IMAGE alt='image' src='GUID-83FF9972-7F6E-4301-B879-BF4E8D5189AD-a5.gif']

The following table shows the available clock
signals that can be routed to devices external to the
signal generator and the destination options.

| Clock to be Exported | Destination Options |
| --- | --- |
| Sample Clock | PFI <0..1> SMB connector |
| PXI_Trig<0..6> |  |
| Sample Clock Timebase | PFI <0..1> SMB connector |
| PXI_Trig<0..6> |  |
| Reference Clock | PFI <0..1> SMB connector |
| PXI_Trig<0..6> |  |

For synchronization purposes, the
NI 5422 allows you to export your clocks 
so that other devices can share the timing of the NI 5422. The following sections describe the possible clock routing configurations.

#### Sample Clock

The Sample clock can be routed to the
PFI <0..1> front panel SMB connectors, PXI_Trig<0..6>
lines on the PXI trigger bus, or the RTSI<0..6> lines.
Additionally, the Sample clock has a direct route to the DDC CLK
OUT line on the DIGITAL DATA & CONTROL connector on the front
panel.

Additionally, the exported clock can be divided
down by an integer value (no less than 2) before being exported to
the PFI<0..1> SMB connectors, PXI_Trig<0..6> lines, or
the RTSI<0..6> lines. Refer to the 
Exported Sample Clock Divisor property or the 
NIFGEN_ATTR_EXPORTED_SAMPLE_CLOCK_DIVISOR attribute for more information about configuring the Sample
clock divisor.

#### Sample Clock Timebase

The Sample clock timebase can be routed to the
PFI <0..1> SMB connectors on the front panel, the
PXI_Trig<0..6> lines on the PXI trigger bus, or the
RTSI<0..6> lines. Additionally, the Sample clock timebase has
a direct route to the DDC CLK OUT line on the DIGITAL DATA &
CONTROL connector on the front panel.

Additionally, the exported clock can be divided
down by an integer value before being exported to the
PFI<0..1> SMB connectors, the PXI_Trig<0..6> lines, or
the RTSI<0..6> lines. You can configure the Sample clock divisor by calling the 
Exported Sample Clock Timebase Divisor property or the 
NIFGEN_ATTR_EXPORTED_SAMPLE_CLOCK_TIMEBASE_DIVISOR attribute.

#### Reference Clock

The Reference clock is the
actual clock that is configured for the signal generator
phase-locked loop circuit to use as a reference. You configure a
Reference clock as a PLL Reference clock source for the signal to
be available for exporting. The Reference clock can be routed to
the PFI<0..1> SMB connectors on the front panel, the
PXI_Trig<0..6> lines on the PXI trigger bus, or the
RTSI<0..6> lines.

Note

#### Destination Options

The following sections define the destinations for
exported clocks.

DDC CLK OUT—You can export the Sample clock
to the DDC CLK OUT line on the optional DIGITAL DATA & CONTROL (DDC)
connector. Exporting the clock from
this connection allows for synchronous clocking of the DDC data.
You must enable the DDC connector before using the Sample clock by calling the 
niFgen
Configure Digital Patterning VI or the 
niFgen_EnableDigitalPatterning and 
niFgen_DisableDigitalPatterning functions.

PFI <0..1>—The Sample clock and the
Reference clock can be exported to the PFI 0 and PFI 1 SMB
connectors on the front panel to synchronize external devices. You
must configure the device to export the desired clock to the PFI
SMB connectors.

Note

PXI_Trig<0..6>—The Sample clock and
the Reference clock can be exported to the PXI_Trig lines or RTSI
lines. The PXI and PCI standards allow for devices to route signals
to other devices in your PXI chassis to enhance device to device
synchronization. Refer to the chassis documentation for
specifications to ensure the reference signal is within tolerance.
You must configure the device to export the desired clock to the
PXI_Trig line or RTSI line. When exporting signals, the following
lines are equivalent:

- PXI_Trig<0..6> = RTSI_<0..6>
- PXI_STAR

Refer to 
niFgen Export
Signal VI or the 
niFgen_ExportSignal function for more information about configuring the
destinations for the desired clock signal.

Parent topic:

NI 5422 Clocking

<!--NI_TOPIC bundle=ni-fgen path=ni-5422-exporting-signals.html language=enus -->
## TOPIC 00381: NI 5422 Exporting Signals

- bundle_id: `ni-fgen`
- source_path: `ni-5422-exporting-signals.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5422-exporting-signals.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The signal generator contains seven PXI trigger lines that are available for sending signal generator-specific information to other devices that have PXI trigger or RTSI bus connectors. The signal generator also connects to the PXI star trigger line, which you can use to send or receive signals to o

### NI 5422 Exporting Signals

Note

ni.com/products

The signal generator has connectors on the front
panel to route signals to devices external to a PXI
chassis. The following table shows the signals available for export
and the lines they can be routed to. To determine all possible
signal routes for your device, refer to 
*Signal Routing*.

|  |  | Destination |  |  |
| --- | --- | --- | --- | --- |
| PXI_Trig<0..6>, or PXI_STAR | PFI 0 and PFI 1 Connectors | PFI<4..5> on DIGITAL DATA & CONTROL Connector |  |  |
| Exported Clocks, Triggers, and Events | Sample Clock | Yes | Yes * | – |
| Sample Clock Timebase | Yes | Yes | – |  |
| PLL Reference Source | Yes | Yes* | – |  |
| Out Start trigger | Yes | Yes | Yes |  |
| Marker Event | Yes | Yes | Yes |  |
| * SYNC OUT/PFI 0 is optimized for the Sample clock and PLL reference source signals and has slightly less jitter than PFI 1. SYNC OUT/PFI 0 is the recommended terminal to use for exporting clocks. |  |  |  |  |

Sample Clock–The clock signal that tells the
DAC when to convert the digital waveform values to an analog
voltage. The Sample clock frequency is referred to as the Sample
clock rate; the rate at which the digital waveforms from device
memory are generated. The Sample clock is also known as update
clock.

Note

Sample Clock Timebase

Note

PLL Reference source–A clock signal that is
only available when a PLL Reference source has been configured. The
clock is the source selected as the PLL Reference Clock source.

Out Start trigger–A signal generated by the
device upon recognizing a start condition that can be routed out
various connectors to signal other devices.

Marker event–A digital signal that can be
used as a trigger corresponding to a specific sample in the
waveform generation. This signal controls other devices that
require timing information related to a specific point in the
generated waveform.

#### Routing Signals

You can route signals in the following ways:

- The Marker event generated during an Arbitrary Waveform
Generation mode waveform generation to any of the PXI trigger
lines, PXI_STAR, or front panel
connectors.
- The signal generator Start trigger output signal to other
devices through any of the PXI trigger lines, PXI_STAR, or front panel connectors.
- The signal generator Sample clock signal to other devices
through any of the PXI trigger lines, PXI_STAR, or front panel connectors.
- The PLL Reference clock source to other devices through any of
the PXI trigger lines, PXI_STAR, or
front panel connectors.

In NI-FGEN, the PXI trigger lines are referred to
as RTSI<0..6>. The correlation between PXI_TRIG<
x> and RTSI<
x> is one to one. You can
configure and route the device internal signals by calling the 
niFgen Export Signal VI
or the 
niFgen_ExportSignal function.

Parent topic:

NI 5422 NI 5422 Overview

Related concepts:

- NI 5422 Signal Routing

<!--NI_TOPIC bundle=ni-fgen path=ni-5422-external-sample-clock.html language=enus -->
## TOPIC 00382: NI 5422 External Sample Clock

- bundle_id: `ni-fgen`
- source_path: `ni-5422-external-sample-clock.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5422-external-sample-clock.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5422 can accept an external clock to directly drive the Sample clock. When using an external Sample clock, the frequency stability and accuracy of the Sample clock is determined by the provided external Sample clock. The following figure shows possible Sample Clock paths. You can set the cloc

### NI 5422 External Sample Clock

The NI 5422 can accept an
external clock to directly drive the Sample clock. When using an
external Sample clock, the frequency stability and accuracy of the
Sample clock is determined by the provided external Sample
clock.

The following figure shows possible Sample
Clock paths.

[IMAGE alt='image' src='GUID-8812ED51-9200-4A44-85CC-727D2EA85B31-a5.gif']

You can set the clock source by calling the
niFgen
Configure Sample Clock Source VI or the 
niFgen_ConfigureSampleClockSource function.

niFgen_ConfigureSampleRate

Note

device specifications

#### External Sample Clock Considerations

The NI 5422 incorporates
high-speed digital clocking technology and requires a stable,
free-running Sample clock to operate properly. When the
signal generator is committed—either explicitly by
calling the 
niFgen Commit VI or
the 
niFgen_Commit function or implicitly by writing waveforms or scripts or
initiating a generation—the external Sample clock must be
available to the device. If the external clock becomes unstable due
to glitching or changing frequency, or is removed entirely, NI-FGEN
returns a hardware clocking error.

If necessary, you can change the rate or the source
of the external Sample clock between generations by
first calling the 
niFgen Abort
Generation VI or the 
niFgen_AbortGeneration function, changing the rate or source, and then calling the
niFgen Commit VI or the 
niFgen_Commit function. NI-FGEN
reprograms the NI 5422 for the new settings,
and you can call the 
niFgen
Initiate Generation VI or the 
niFgen_InitiateGeneration function to start the next generation.

If you must remove the external Sample clock
between generations (after calling the niFgen Abort Generation VI
or 
niFgen_AbortGeneration function, but
before calling the niFgen Initiate VI or the 
niFgen_Init function), but are not
changing the frequency or source of the external clock, you can
choose one of the following options:

- Call the niFgen Initiate VI or the 
 niFgen_Init function, which returns
a hardware clocking error because the external Sample clock is
gone, then clear the error and call the niFgen Initiate VI or the 
 niFgen_Init function
again. NI-FGEN then reprograms the hardware to use the
external clock again.
- Force the device to be recommitted by changing a property or
attribute to another value and then back to its original value.
This action causes NI-FGEN to re-commit the settings to hardware,
which does not happen otherwise because NI-FGEN does not know
that the external Sample clock is gone.

Caution

niFgen_ConfigureSampleRate

Parent topic:

NI 5422 Clocking Options

<!--NI_TOPIC bundle=ni-fgen path=ni-5422-filtering-effects.html language=enus -->
## TOPIC 00383: NI 5422 Filtering Effects

- bundle_id: `ni-fgen`
- source_path: `ni-5422-filtering-effects.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5422-filtering-effects.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The delay from the time at which the device receives a trigger to the time at which the analog output signal is generated increases if the digital and/or analog filters in the Analog Output path are enabled. In the case of digital filtering, delay also increases with increase in interpolation. The

### NI 5422 Filtering Effects

Analog Output path

Note

Refer to the 
*device
specifications* for the delay from trigger to analog output
based on different filtering options.

Parent topic:

NI 5422 Analog Output

Related concepts:

- NI 5422 Analog Output

<!--NI_TOPIC bundle=ni-fgen path=ni-5422-filtering-effects_2.html language=enus -->
## TOPIC 00384: NI 5422 Filtering Effects

- bundle_id: `ni-fgen`
- source_path: `ni-5422-filtering-effects_2.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5422-filtering-effects_2.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The delay from the time at which the device receives a trigger to the time at which the analog output signal is generated increases if the digital and/or analog filters in the Analog Output path are enabled. In the case of digital filtering, delay also increases with increase in interpolation. The

### NI 5422 Filtering Effects

Analog Output path

Note

Refer to the 
*device
specifications* for the delay from trigger to analog output
based on different filtering options.

Parent topic:

NI 5422 Triggering

<!--NI_TOPIC bundle=ni-fgen path=ni-5422-front-panel.html language=enus -->
## TOPIC 00385: NI 5422 Front Panel

- bundle_id: `ni-fgen`
- source_path: `ni-5422-front-panel.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5422-front-panel.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the NI PXI-5422 front panel. This front panel has four SMB connectors and an optional 68-pin male VHDCI connector. The male VHDCI (Digital Data & Control) connector is not available on the NI 5422 with the 8 MB memory option. The ACCESS and ACTIVE LEDs indicate the status

### NI 5422 Front Panel

The following figure shows the NI PXI-5422 front panel. This front panel has
four SMB connectors and an optional 68-pin male VHDCI connector.
The male VHDCI (Digital Data & Control) connector is not
available on the NI 5422 with the 8 MB memory
option.

[IMAGE alt='image' src='GUID-C1F72A05-C651-4DE1-AFEF-E45946B5C1F5-a5.gif']

The *ACCESS and ACTIVE LEDs* indicate the status of the PXI module.

The 
*CH 0* SMB connector is the analog
output from which arbitrary waveforms are generated.

The 
*CLK IN* SMB connector provides the
device with an external reference or external Sample clock.

The 
*PFI 0 and PFI 1* SMB
connectors are multi-directional connections for a number of
different signals.

*DIGITAL DATA &
CONTROL* is an optional 68-pin male VHDCI connector that
contains the 16-bit LVDS digital pattern outputs.

Parent topic:

NI 5422 NI 5422 Overview

Related concepts:

- NI 5422 ACCESS and ACTIVE LEDs
- NI 5422 CH 0 Connector
- NI 5422 CLK IN Connector
- NI 5422 PFI Connectors
- NI 5422 DIGITAL DATA & CONTROL Connector

<!--NI_TOPIC bundle=ni-fgen path=ni-5422-hardware-state-diagram.html language=enus -->
## TOPIC 00386: NI 5422 Hardware State Diagram

- bundle_id: `ni-fgen`
- source_path: `ni-5422-hardware-state-diagram.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5422-hardware-state-diagram.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following diagram shows the hardware states of the signal generator. The signal generator can be in one of the following six basic states during the course of operation. Idle—The device is not generating a waveform. All session properties or attributes can be programmed in the Idle state. In the

### NI 5422 Hardware State Diagram

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

NI 5422 Theory of Operation

Related concepts:

- Programming State Model

<!--NI_TOPIC bundle=ni-fgen path=ni-5422-internal-sample-clock.html language=enus -->
## TOPIC 00387: NI 5422 Internal Sample Clock

- bundle_id: `ni-fgen`
- source_path: `ni-5422-internal-sample-clock.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5422-internal-sample-clock.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5422 can derive a Sample clock from its main internal timing source—the onboard Sample clock timebase. The signal generator provides a high-precision 200MHz Voltage Controlled Crystal Oscillator (VCXO) clock source for the Sample clock timebase. As shown in the following figure, the Sample cl

### NI 5422 Internal Sample Clock

The NI 5422 can derive a Sample
clock from its main internal timing source—the onboard Sample clock
timebase. The signal generator provides a high-precision
200MHz Voltage Controlled Crystal Oscillator (VCXO) clock
source for the Sample clock timebase. As shown in the following
figure, the Sample clock timebase frequency is tuned by an Internal
Calibration DAC control voltage when the 
Reference
Clock Source property or the 
NIFGEN_ATTR_REFERENCE_CLOCK_SOURCE attribute is set to "None." The Internal Calibration DAC,
which is calibrated at the factory and which you also can
calibrate, provides for the Sample clock Timebase to maintain a
high quality frequency source.

[IMAGE alt='image' src='GUID-D03A5DF8-0676-4454-9B09-82794E66EF97-a5.gif']

There are two methods, referred to as clock modes,
for creating an internal Sample clock from the Sample clock
timebase: Divide-Down (Divide by N) Sampling and High-Resolution Sampling.

In Divide-Down Sampling mode, the
Divide by  
N circuit uses the Sample clock timebase of 200 MHz
to create the frequency available for use as the Sample clock.
Divide-Down Sampling mode can generate any Sample clock frequency
of 200 MHz/ 
N, where 
N is any integer from 1 to 40. The Divide-Down Sample
clock can run at 200 MHz, 100.0 MHz, 66.66 MHz,
50.0 MHz, 40.0 MHz, 33.332 MHz, and so on. The low
frequency limit in Divide-Down Sampling mode is 5 MHz
(200 MHz/40). Divide-Down Sampling mode provides a
high-quality clock with the lowest jitter.

The High-Resolution Sampling mode also uses the
Sample clock timebase at 200 MHz to generate a frequency from
5 MHz to 200 MHz. In addition, the High-Resolution mode
uses direct digital synthesis to generate very fine resolution
increments on the order of microhertz. Refer to the 
*device specifications* for more information.

Note

device
specifications

Parent topic:

NI 5422 Clocking Options

<!--NI_TOPIC bundle=ni-fgen path=ni-5422-low-voltage-differential-signaling-lv.html language=enus -->
## TOPIC 00388: NI 5422 Low-Voltage Differential Signaling (LVDS)

- bundle_id: `ni-fgen`
- source_path: `ni-5422-low-voltage-differential-signaling-lv.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5422-low-voltage-differential-signaling-lv.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Low-voltage differential signaling (LVDS) is a low-noise, low-power, low-amplitude method for high-speed digital data transfer. The following figure shows a diagram of a typical LVDS circuit. As you can see in the previous figure, a current source at the driver provides approximately 3.5 mA of curre

### NI 5422 Low-Voltage Differential Signaling (LVDS)

Low-voltage differential signaling (LVDS) is a
low-noise, low-power, low-amplitude method for high-speed digital
data transfer.

The following figure shows a diagram of a typical
LVDS circuit.

[IMAGE alt='image' src='GUID-33D1EFAE-90F1-4A1C-8B90-A6B07019D4EA-a5.gif']

As you can see in the previous figure, a current
source at the driver provides approximately 3.5 mA of current.
The direction of the current across the transmission line depends
on whether the driver drives a logic high level or low level. When
the current reaches the receiver, a 100 Ω terminating
resistor connects the two ends of the differential transmission
line to provide a return path for the current. In addition, a
voltage of approximately 350 mV is established across the two
input terminals of the receiver. The differential voltage at the
receiver is either positive or negative, depending on the direction
of the current. The receiver recognizes a positive voltage signal
as a logic high level (1) and a negative voltage as a logic low
level (0).

The electrical characteristics of an LVDS signal
offers some performance improvements compared to single-ended
standards. For example, since the received voltage is a
differential between two signals, the voltage difference between
the logic high level and low level state can be smaller, allowing
for faster rise and fall times. Also, the differential transmission
scheme is less susceptible to common-mode noise than single-ended
transmission methods.

Note

Electrical Characteristics of Low-Voltage Differential
Signaling (LVDS) Interface Circuits

Parent topic:

NI 5422 DIGITAL DATA & CONTROL Connector

<!--NI_TOPIC bundle=ni-fgen path=ni-5422-memory-fragmentation.html language=enus -->
## TOPIC 00389: NI 5422 Memory Fragmentation

- bundle_id: `ni-fgen`
- source_path: `ni-5422-memory-fragmentation.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5422-memory-fragmentation.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: When storing multiple waveforms in NI 5422 memory, fragmentation can become a problem. Both waveforms and instructions are stored in NI 5422 memory in contiguous blocks. These blocks are allocated in multiples of 128 bytes, and they are written in the order that you configure them. Fragmentation occ

### NI 5422 Memory Fragmentation

When storing multiple waveforms in
NI 5422 memory, fragmentation can become a
problem. Both waveforms and instructions are stored in
NI 5422 memory in contiguous blocks. These
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

NI 5422 Onboard Memory

<!--NI_TOPIC bundle=ni-fgen path=ni-5422-ni-5422-overview.html language=enus -->
## TOPIC 00390: NI 5422 NI 5422 Overview

- bundle_id: `ni-fgen`
- source_path: `ni-5422-ni-5422-overview.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5422-ni-5422-overview.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5422 is a 200 MS/s, 16-bit arbitrary waveform generator with the following features: One 16-bit resolution output channel Output amplitude up to 12 V[pk-pk] into a 50 Ω load up to 80 MHz Offset up to ± full scale Up to 80 MHz sine output Up to 100 MHz square output Up to 10 MHz triangle, ramp

### NI 5422 NI 5422 Overview

The NI 5422 is a 200 MS/s, 16-bit arbitrary
waveform generator with the following features:

- One 16-bit resolution output channel
- Output amplitude up to 12 V pk-pk into a 50 Ω load up to 80 MHz
- Offset up to ± full scale
- Up to 80 MHz sine output
- Up to 100 MHz square output
- Up to 10 MHz triangle, ramp-up, and ramp-down output
- Software-selectable output impedances (50 Ω or
75 Ω) and output attenuation levels from 0 dB to
51 dB
- High-Resolution, Divide by 
 N , and external clocking
- PLL synchronization to external Reference clocks or to
PXI_CLK10
- NI-TClk support for multi-module synchronization. Refer to 
 Start»All Programs»National Instruments»NI-TClk 
for more information.
- Sampling rate up to 200 MS/s
- Up to 512 MB of onboard waveform memory
- Waveform linking and looping for arbitrary waveform
generation
- Analog filtering
- Digital gain
- Four external trigger inputs
- 4 Marker events as trigger output
- Optional 16-bit digital pattern generation with clock and LVDS
output
- PXI trigger lines

All NI 5422 devices follow industry-standard
Plug and Play specifications for the PXI bus and offer seamless
integration with compliant systems.

Parent topic:

Devices

<!--NI_TOPIC bundle=ni-fgen path=ni-5422-onboard-memory.html language=enus -->
## TOPIC 00391: NI 5422 Onboard Memory

- bundle_id: `ni-fgen`
- source_path: `ni-5422-onboard-memory.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5422-onboard-memory.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5422 signal generator uses an onboard memory that is 16-bits wide. The minimum standard memory size for the NI 5422 is 8 MB which translates to 8,338,608 usable bytes. With the minimum standard memory size, you can store very long waveforms on the device and obtain reliable waveform generatio

### NI 5422 Onboard Memory

The NI 5422 signal generator
uses an onboard memory that is 16-bits wide. The minimum standard
memory size for the NI 5422 is 8 MB
which translates to 8,338,608 usable bytes. With the minimum
standard memory size, you can store very long waveforms on the
device and obtain reliable waveform generation at full sample rate
of 200 MS/s. The
NI 5422 is also available with higher memory options
of 32 MB, 256 MB, and 512 MB.

The onboard memory is a single large memory area that stores both waveforms and sequence instructions to generate
the waveforms. The instructions for a complicated sequence can
occupy a significant portion of memory. The architecture of the
NI 5422 allows you to load multiple
waveforms and multiple sequence instructions into the memory. The
following diagram illustrates NI 5422
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

Parent topic:

NI 5422 Theory of Operation

<!--NI_TOPIC bundle=ni-fgen path=ni-5422-output-enable.html language=enus -->
## TOPIC 00392: NI 5422 Output Enable

- bundle_id: `ni-fgen`
- source_path: `ni-5422-output-enable.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5422-output-enable.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can disable the analog output signal at the CH 0 connector by controlling the output enable relay, as shown in the following figure. When the output enable relay is disabled, the output signal is connected to ground through a 50 or 75 Ω resistance depending on the output impedance selected. The

### NI 5422 Output Enable

You can disable the analog output signal at the CH
0 connector by controlling the output enable relay, as shown in the
following figure.

[IMAGE alt='image' src='GUID-BFAEDBE6-696A-4B0B-9A41-C8FD2A49A5A8-a5.gif']

When the output enable relay is disabled, the
output signal is connected to ground through a 50 or
75 Ω resistance depending on the output impedance
selected. The output enable relay is enabled for normal waveform
generation, connecting the CH 0 SMB connector to the 
*Analog Output path*. You
can change the output enable state at any time during waveform
generation, and the generation continues on internally.

niFgen_ConfigureOutputEnabled

Note

Parent topic:

NI 5422 Analog Output

Related concepts:

- NI 5422 Analog Output

<!--NI_TOPIC bundle=ni-fgen path=ni-5422-output-impedance.html language=enus -->
## TOPIC 00393: NI 5422 Output Impedance

- bundle_id: `ni-fgen`
- source_path: `ni-5422-output-impedance.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5422-output-impedance.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5422 Analog Output path is designed to have an output impedance of 50 Ω from the Output Enable relay looking back towards the Main DAC. There is a selectable 25 Ω resistance that can be switched into the Analog Output path between the Output Enable relay and the CH 0 connector for application

### NI 5422 Output Impedance

The NI 5422 Analog Output path is
designed to have an output impedance of 50 Ω from the
*Output Enable relay* looking back towards the Main DAC. There is a
selectable 25 Ω resistance that can be switched into the
Analog Output path between the Output Enable relay and the CH
0 connector for applications requiring a 75 Ω
impedance. Most applications use a load impedance of
50 Ω, but applications such as video testing, require
75 Ω. Refer to the following figure.

[IMAGE alt='image' src='GUID-1168A294-D930-4645-8DF7-E4E6E841D015-a5.gif']

If the load impedance is a high impedance (~1
MΩ), you may see output levels up to twice the selected
output value for a matched input/output impedance. These levels can
be as high as 24 V<sub>pk-pk</sub> for the High-Gain Amplifier path. Normally, the
output levels increase as the load impedance increases. The
NI 5422 can compensate for different load impedance
values. Refer to 
*CH 0 Connector* for more
information.

niFgen_ConfigureOutputImpedance

Note

Parent topic:

NI 5422 Analog Output

Related concepts:

- NI 5422 Output Enable
- NI 5422 CH 0 Connector

<!--NI_TOPIC bundle=ni-fgen path=ni-5422-output-modes.html language=enus -->
## TOPIC 00394: NI 5422 Output Modes

- bundle_id: `ni-fgen`
- source_path: `ni-5422-output-modes.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5422-output-modes.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The output mode of your signal generator determines the type of waveforms your signal generator produces. To select an output mode, set the Output Mode parameter of the niFgen Configure Output Mode VI or the niFgen_ConfigureOutputMode function.

### NI 5422 Output Modes

The output mode of your signal generator determines the type of
waveforms your signal generator produces. To select an output mode,
set the 
Output Mode parameter of the 
niFgen
Configure Output Mode VI or the 
niFgen_ConfigureOutputMode function.

Parent topic:

NI 5422 Waveform Generation

<!--NI_TOPIC bundle=ni-fgen path=ni-5422-pfi-connectors.html language=enus -->
## TOPIC 00395: NI 5422 PFI Connectors

- bundle_id: `ni-fgen`
- source_path: `ni-5422-pfi-connectors.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5422-pfi-connectors.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: PFI 0 and PFI 1 are bidirectional connectors. As an input, the PFI terminals can accept a trigger from an external source that can start or step through waveform generation. As an output, the PFI lines route a signal out from the following sources: Marker events Start trigger PLL Reference clock sou

### NI 5422 PFI Connectors

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

device specifications

Note

Parent topic:

NI 5422 Front Panel

<!--NI_TOPIC bundle=ni-fgen path=ni-5422-phase-locked-loop-reference-clock.html language=enus -->
## TOPIC 00396: NI 5422 Phase-Locked Loop Reference Clock

- bundle_id: `ni-fgen`
- source_path: `ni-5422-phase-locked-loop-reference-clock.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5422-phase-locked-loop-reference-clock.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: A phase-locked loop (PLL) is a circuit that tunes the Sample clock timebase to phase–lock to an external Reference clock. The PLL Reference clock source controls the source of the control voltage that tunes the VCXO of the Sample clock timebase for internal clock update sources. The frequency stabil

### NI 5422 Phase-Locked Loop Reference Clock

Note

device
specifications

The following figure shows the NI 5422 Reference Clock Source path.

[IMAGE alt='image' src='GUID-928A3C7A-05C9-46C0-86CE-DCD9AFB72E85-a5.gif']

Note

NIFGEN_ATTR_REFERENCE_CLOCK_SOURCE

#### Reference Clock Sources

The NI 5422 can
phase-lock its Sample clock timebase to an external signal
that is present on the CLK IN front panel connector. PXI devices
can also phase–lock to a 10 MHz Reference clock signal
provided by the PXI bus (PXI_CLK10).

Refer to the table in 
*Clocking Options*,
for the valid NI-FGEN property value combinations that can be used
to configure the NI 5422 clock settings
for an external Reference clock.

Note

device 
specifications

Related Topics

Configuring a Reference
Clock

Parent topic:

NI 5422 Clocking Options

Related concepts:

- NI 5422 Clocking Options
- Configuring a Reference Clock

<!--NI_TOPIC bundle=ni-fgen path=ni-5422-postamplifier-attenuation.html language=enus -->
## TOPIC 00397: NI 5422 Postamplifier Attenuation

- bundle_id: `ni-fgen`
- source_path: `ni-5422-postamplifier-attenuation.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5422-postamplifier-attenuation.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The postamplifier attenuation section is after the High-Gain and Low-Gain Amplifiers in the analog path. The attenuators provide a range of attenuation from 0 dB to a maximum of 36 dB in steps of 12 dB. NI-FGEN automatically controls the value of attenuation set in the postamplifier attenuation sect

### NI 5422 Postamplifier Attenuation

The postamplifier attenuation section is after the
High-Gain and Low-Gain Amplifiers in the *analog path*. The attenuators provide a
range of attenuation from 0 dB to a maximum of 36 dB in steps
of 12 dB. NI-FGEN automatically controls the value of attenuation
set in the postamplifier attenuation section dependent on the set
gain. You can read the value NI-FGEN has selected for postamplifier
attenuation using the 
Post-Amplifier Attenuation property or the 
NIFGEN_ATTR_POST_AMPLIFIER_ATTENUATION attribute.

Parent topic:

NI 5422 Attenuation

Related concepts:

- NI 5422 Analog Output

<!--NI_TOPIC bundle=ni-fgen path=ni-5422-power-up-and-reset-conditions.html language=enus -->
## TOPIC 00398: NI 5422 Power-Up and Reset Conditions

- bundle_id: `ni-fgen`
- source_path: `ni-5422-power-up-and-reset-conditions.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5422-power-up-and-reset-conditions.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The signal generator is in the following state from the time at which the computer begins to power up until the operating system is fully booted and NI-FGEN is loaded. The CH 0 analog output connector is disabled and has 50 Ω or 75 Ω impedance to ground. This impedance is the same as its previous se

### NI 5422 Power-Up and Reset Conditions

The signal generator is in the following state from
the time at which the computer begins to power up until the operating system is
fully booted and NI-FGEN is loaded.

- The CH 0 analog output connector is disabled and has
50 Ω or 75 Ω impedance to ground. This
impedance is the same as its previous setting before the device was
powered down. The output voltage amplitude of this connector
is 0 V.
- The CLK IN connector has 50 Ω impedance to
ground.
- PFI 0 and PFI 1 are tristated and have a 1
kΩ impedance to ground.

- In devices with a DDC connector, DIGITAL DATA & CONTROL
output lines are disabled and floating; inputs have a
100 Ω differential termination.

- PXI trigger lines are tristated and floating.

After the operating system is fully booted and
NI-FGEN is loaded, or when you perform a hard reset to the device
directly from MAX or using NI-FGEN, the signal generator is in the
following state:

- CH 0 output is enabled.
- CH 0 output attenuation is set to 0 dB.
- Output impedance is set to 50 Ω.
- The Low-Gain Amplifier path is enabled in the Analog Output
path.
- The analog filter is disabled.

- CLK IN is disabled and has a 50 Ω
impedance to ground.
- PFI 0 and PFI 1 are tristated and have a 1
kΩ impedance to ground.

- On devices with a DDC connector, all output lines on the DIGITAL DATA
& CONTROL Connector are disabled and floating; inputs have a
100 Ω differential termination.

- PXI trigger lines are tristated and floating.
- The sample rate is set to the maximum rate, with the Sample
clock source set to the internal Sample clock timebase.
- The Sample clock timebase is tuned by the internal reference
control voltage.

Parent topic:

NI 5422 NI 5422 Overview

<!--NI_TOPIC bundle=ni-fgen path=ni-5422-preamplifier-attenuation.html language=enus -->
## TOPIC 00399: NI 5422 Preamplifier Attenuation

- bundle_id: `ni-fgen`
- source_path: `ni-5422-preamplifier-attenuation.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5422-preamplifier-attenuation.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The preamplifier attenuation section is before the Low-Gain and High-Gain amplifiers in the analog path. The attenuators provide a range of attenuation from 0 to a maximum of 12 dB in steps of 3 dB. NI-FGEN automatically controls the value of attenuation set in the preamplifier attenuation section d

### NI 5422 Preamplifier Attenuation

The preamplifier attenuation section is before the
Low-Gain and High-Gain amplifiers in the *analog path*. The attenuators provide a
range of attenuation from 0 to a maximum of 12 dB in steps of
3 dB. NI-FGEN automatically controls the value of attenuation set
in the preamplifier attenuation section depending on the set
gain. You can read the value NI-FGEN has selected for preamplifier attenuation using the 
Pre-Amplifier Attenuation property or the 
NIFGEN_ATTR_PRE_AMPLIFIER_ATTENUATION attribute.

Preamplifier attenuation improves the signal
distortion because amplifiers provide lower distortion performance
with smaller signals. However, attenuation lowers the amplitude of
both the signal and the noise in a signal as the signal-to-noise
ratio (SNR) is unchanged upon attenuation. Amplifiers also have a
fixed noise associated with them. The total noise at the amplifier
output is obtained by taking the root of the sum of squares of the
following factors:

- The input signal noise multiplied by the gain of the
amplifier
- The amplifier noise

The total noise is dominated by the larger factor.
If the signal is attenuated so that its noise when multiplied by
gain at the amplifier input is smaller than the amplifier noise,
then the output has a higher SNR. This higher SNR is a good reason
to implement some of the signal generator overall attenuation as preamplifier
attenuation.

Parent topic:

NI 5422 Attenuation

Related concepts:

- NI 5422 Analog Output

<!--NI_TOPIC bundle=ni-fgen path=ni-5422-sample-size-and-resolution.html language=enus -->
## TOPIC 00400: NI 5422 Sample Size and Resolution

- bundle_id: `ni-fgen`
- source_path: `ni-5422-sample-size-and-resolution.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5422-sample-size-and-resolution.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5422 stores arbitrary waveforms in memory as signed 16-bit digital words. On the NI 5422, the entire 16 bits are sent to the digital gain circuit, the digital filter, and the DAC. Related Topics Onboard Memory Waveform Sizes

### NI 5422 Sample Size and Resolution

The NI 5422 stores arbitrary
waveforms in memory as signed 16-bit digital words. On the
NI 5422, the entire 16 bits are sent to the digital
gain circuit, the digital filter, and the DAC.

Related Topics

*Onboard Memory*

*Waveform Sizes*

Parent topic:

NI 5422 Waveform Generation

Related concepts:

- NI 5422 Onboard Memory
- NI 5422 Waveform Size and Quantum

<!--NI_TOPIC bundle=ni-fgen path=ni-5422-script-mode.html language=enus -->
## TOPIC 00401: NI 5422 Script Mode

- bundle_id: `ni-fgen`
- source_path: `ni-5422-script-mode.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5422-script-mode.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Script Mode allows you to use scripting to link and loop multiple waveforms in complex combinations using a script. A script is a series of instructions that indicates how waveforms saved in the onboard memory should be sent to the DUT. Scripts have many different uses, including specifying the orde

### NI 5422 Script Mode

*Script Mode* allows you to use scripting to link and
loop multiple waveforms in complex combinations using a 
script. A script is a series of instructions that
indicates how waveforms saved in the onboard memory should be sent
to the DUT. Scripts have many different uses, including specifying the order in which the waveforms
are generated, the number of times they are generated, and the
triggers and markers associated with the generation.

Parent topic:

NI 5422 Output Modes

Related concepts:

- Script Mode

<!--NI_TOPIC bundle=ni-fgen path=ni-5422-signal-routing.html language=enus -->
## TOPIC 00402: NI 5422 Signal Routing

- bundle_id: `ni-fgen`
- source_path: `ni-5422-signal-routing.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5422-signal-routing.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: An NI signal generator is capable of sending and receiving signals through the front panel and the PXI or RTSI trigger bus. The front panel connectors provides connectivity for the output channel as well as for control lines for sending and receiving clocks, triggers, and events. You can use the PXI

### NI 5422 Signal Routing

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
2. Expand Devices and Interfaces .

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

NI 5422 Theory of Operation

Related concepts:

- NI 5422 Syntax for Terminal Names

<!--NI_TOPIC bundle=ni-fgen path=ni-5422-single-trigger-mode.html language=enus -->
## TOPIC 00403: NI 5422 Single Trigger Mode

- bundle_id: `ni-fgen`
- source_path: `ni-5422-single-trigger-mode.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5422-single-trigger-mode.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: When your application is configured for Single trigger mode, only one Start trigger is required to begin waveform generation. All Start triggers after the first Start trigger are ignored. Once the waveform generation is complete, the analog output indefinitely settles at the DC value of the last sam

### NI 5422 Single Trigger Mode

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

NI 5422 Trigger Modes

<!--NI_TOPIC bundle=ni-fgen path=ni-5422-specifications.html language=enus -->
## TOPIC 00404: NI 5422 Specifications

- bundle_id: `ni-fgen`
- source_path: `ni-5422-specifications.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5422-specifications.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: For information about the signal generator specifications, refer to the device specifications. You can access these specifications by navigating to Start»All Programs»National Instruments» NI-FGEN»Documentation»NI Signal Generators Specifications, or you can visit ni.com/manuals.

### NI 5422 Specifications

For information about the signal generator
specifications, refer to the 
*device
specifications*. You can access these specifications by
navigating to 
Start»All Programs»National Instruments»
NI-FGEN»Documentation»NI Signal Generators Specifications, or you can visit 
ni.com/manuals.

Parent topic:

NI 5422 NI 5422 Overview

<!--NI_TOPIC bundle=ni-fgen path=ni-5422-standard-function-mode.html language=enus -->
## TOPIC 00405: NI 5422 Standard Function Mode

- bundle_id: `ni-fgen`
- source_path: `ni-5422-standard-function-mode.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5422-standard-function-mode.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Standard Function output mode is used to generate standard function waveforms such as sine, square, triangle, and so on. On the NI 5422, Standard Function mode is implemented primarily in software. NI-FGEN creates and downloads standard function waveforms to arbitrary waveform memory and generates t

### NI 5422 Standard Function Mode

Standard Function output mode is used to generate standard
function waveforms such as sine, square, triangle, and so on. 
On the NI 5422, *Standard Function mode* is implemented primarily in software. NI-FGEN creates and downloads standard function waveforms to arbitrary waveform memory and generates them the same way that it generates arbitrary waveforms. NI-FGEN automatically selects the best clock mode, sample rate, and buffer size to produce the most accurate waveform possible.

Parent topic:

NI 5422 Output Modes

Related concepts:

- Standard Function Mode

<!--NI_TOPIC bundle=ni-fgen path=ni-5422-stepped-trigger-mode.html language=enus -->
## TOPIC 00406: NI 5422 Stepped Trigger Mode

- bundle_id: `ni-fgen`
- source_path: `ni-5422-stepped-trigger-mode.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5422-stepped-trigger-mode.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The waveform you downloaded generates each time a Start trigger occurs. After a waveform finishes generating, the last sample of the waveform repeats continuously until the next Start trigger is received. When the next Start trigger is received, the waveform generates again. If a Start trigger is re

### NI 5422 Stepped Trigger Mode

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

NI 5422 Trigger Modes

<!--NI_TOPIC bundle=ni-fgen path=ni-5422-streaming.html language=enus -->
## TOPIC 00407: NI 5422 Streaming

- bundle_id: `ni-fgen`
- source_path: `ni-5422-streaming.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5422-streaming.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Streaming is a way to generate waveforms that are too large to fit in the onboard memory of the signal generator. Streaming can be used in Arbitrary Waveform, Arbitrary Sequence, or Script output modes. To stream waveform data, allocate and identify all or a portion of the signal generator onboard m

### NI 5422 Streaming

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

NI 5422 Waveform Generation

Related concepts:

- Arbitrary Waveform Output Mode
- Arbitrary Sequence Mode
- Script Mode
- Direct DMA

<!--NI_TOPIC bundle=ni-fgen path=ni-5422-synchronization.html language=enus -->
## TOPIC 00408: NI 5422 Synchronization

- bundle_id: `ni-fgen`
- source_path: `ni-5422-synchronization.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5422-synchronization.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Your signal generator is based on the National Instruments Synchronization and Memory Core (SMC) technology and therefore supports TClk synchronization. Refer to the NI-TClk Synchronization Help for more information about NI-TClk Synchronization.

### NI 5422 Synchronization

Your signal generator is based on the 
National Instruments
Synchronization and Memory Core (SMC) technology and therefore
supports TClk synchronization. Refer to the 
NI-TClk
Synchronization Help for more information about NI-TClk
Synchronization.

Parent topic:

NI 5422 NI 5422 Overview

<!--NI_TOPIC bundle=ni-fgen path=ni-5422-syntax-for-terminal-names.html language=enus -->
## TOPIC 00409: NI 5422 Syntax for Terminal Names

- bundle_id: `ni-fgen`
- source_path: `ni-5422-syntax-for-terminal-names.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5422-syntax-for-terminal-names.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The syntax for terminal names is a unique identifier that refers to a physical terminal in your system. To guarantee the uniqueness of a terminal name across multiple devices, terminal names begin with a forward slash, followed by the name of the device as configured in MAX, such as Dev1. A forward

### NI 5422 Syntax for Terminal Names

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

NI 5422 Signal Routing

<!--NI_TOPIC bundle=ni-fgen path=ni-5422-theory-of-operation.html language=enus -->
## TOPIC 00410: NI 5422 Theory of Operation

- bundle_id: `ni-fgen`
- source_path: `ni-5422-theory-of-operation.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5422-theory-of-operation.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Expand this topic for information about the theory of operation of your signal generator.

### NI 5422 Theory of Operation

Expand this topic for information about the theory
of operation of your signal generator.

Parent topic:

NI 5422 NI 5422 Overview

<!--NI_TOPIC bundle=ni-fgen path=ni-5422-thermal-shutdown.html language=enus -->
## TOPIC 00411: NI 5422 Thermal Shutdown

- bundle_id: `ni-fgen`
- source_path: `ni-5422-thermal-shutdown.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5422-thermal-shutdown.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: NI-FGEN supports thermal shutdown capability for the NI 5422. This capability allows the signal generator to detect when it has reached a dangerously high temperature and to then power down to prevent damage to the device. Air circulation paths, fan settings, and space allowances are several factors

### NI 5422 Thermal Shutdown

NI-FGEN supports thermal shutdown capability for
the NI 5422. This
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

NI 5422 NI 5422 Overview

<!--NI_TOPIC bundle=ni-fgen path=ni-5422-trigger-modes.html language=enus -->
## TOPIC 00412: NI 5422 Trigger Modes

- bundle_id: `ni-fgen`
- source_path: `ni-5422-trigger-modes.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5422-trigger-modes.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5422 has four trigger modes: Single, Continuous, Stepped, and Burst. These trigger modes are available for Arbitrary Waveform, Arbitrary Sequence, and Frequency List output mode. Refer to the niFgen Configure Trigger Mode VI or the niFgen_ConfigureTriggerMode function for information about se

### NI 5422 Trigger Modes

The NI 5422 has four trigger modes: Single, Continuous, Stepped,
and Burst. These trigger modes are available for Arbitrary
Waveform, Arbitrary Sequence, and Frequency List output mode.
Refer to the 
niFgen
Configure Trigger Mode VI or the 
niFgen_ConfigureTriggerMode function for information about setting the trigger mode.

Parent topic:

NI 5422 Triggering

<!--NI_TOPIC bundle=ni-fgen path=ni-5422-trigger-sources.html language=enus -->
## TOPIC 00413: NI 5422 Trigger Sources

- bundle_id: `ni-fgen`
- source_path: `ni-5422-trigger-sources.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5422-trigger-sources.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Trigger sources are software selectable. You can use any of the following external input triggers: PFI 0 or PFI 1 on the front panel connectors PFI 2 or PFI 3 on the DIGITAL DATA & CONTROL front panel connector RTSI<0..7> (PCI) lines or PXI_TRIG<0..7> lines and PXI_STAR on the PXI trigger bus backpl

### NI 5422 Trigger Sources

Trigger sources are software selectable. You can
use any of the following external input triggers:

- PFI 0 or PFI 1 on the front panel connectors

- PFI 2 or PFI 3 on the DIGITAL DATA & CONTROL front panel
connector

- RTSI<0..7> (PCI) lines or PXI_TRIG<0..7> lines and
PXI_STAR on the PXI trigger bus backplane

The following figure shows the possible trigger
sources for the NI 5422.

[IMAGE alt='image' src='GUID-3D9E272C-29DC-41E1-8DF1-6E390A3EE66C-a5.gif']

§

Exporting Signals

Note

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

*PXI Star Trigger
Line*

Parent topic:

NI 5422 Triggering

Related concepts:

- NI 5422 Exporting Signals
- PXI Trigger Lines
- PXI Star Trigger Line

<!--NI_TOPIC bundle=ni-fgen path=ni-5422-trigger-timing.html language=enus -->
## TOPIC 00414: NI 5422 Trigger Timing

- bundle_id: `ni-fgen`
- source_path: `ni-5422-trigger-timing.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5422-trigger-timing.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the relationship between Start trigger and the waveform output. t[s1] is the required pulse width on the Start trigger signal. t[s2] is the delay from the Start trigger to the waveform output. Refer to the NI PXI-5422 Specifications for more information about these timing

### NI 5422 Trigger Timing

The following figure shows the relationship between
Start trigger and the waveform output. t<sub>s1</sub> is the required pulse width on the Start trigger
signal. t<sub>s2</sub> is the delay from the Start trigger to the waveform
output. Refer to the 
*NI PXI-5422
Specifications* for more information about these timing
parameters.

[IMAGE alt='image' src='GUID-9DD6A51C-2BCA-4129-9C8D-0A821181925F-a5.gif']

The NI 5422 also allows you to export
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

NI 5422 Triggering

<!--NI_TOPIC bundle=ni-fgen path=ni-5422-triggering.html language=enus -->
## TOPIC 00415: NI 5422 Triggering

- bundle_id: `ni-fgen`
- source_path: `ni-5422-triggering.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5422-triggering.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can define the signal generator functionality by using the various triggering techniques. Expand this section to learn more about using triggers with your signal generator.

### NI 5422 Triggering

You can define the signal generator functionality
by using the various triggering techniques. Expand this section to
learn more about using triggers with your signal generator.

Parent topic:

NI 5422 NI 5422 Overview

<!--NI_TOPIC bundle=ni-fgen path=ni-5422-waveform-amplitude-control.html language=enus -->
## TOPIC 00416: NI 5422 Waveform Amplitude Control

- bundle_id: `ni-fgen`
- source_path: `ni-5422-waveform-amplitude-control.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5422-waveform-amplitude-control.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5422 uses both amplifiers and attenuators to achieve required amplitude settings. Output Paths and Amplifiers The following figure shows two different gain paths: the Direct path and the Main path with High-Gain and Low-Gain amplifiers. The Direct path provides the output of the main DAC to t

### NI 5422 Waveform Amplitude Control

The NI 5422 uses both amplifiers and
attenuators to achieve required amplitude settings.

#### Output Paths and Amplifiers

The following figure shows two different gain
paths: the Direct path and the Main path with High-Gain and Low-Gain amplifiers.

[IMAGE alt='image' src='GUID-1168A294-D930-4645-8DF7-E4E6E841D015-a5.gif']

The Direct path provides the output of the main DAC
to the CH 0 connector with the fewest electronic components in the path.
There are no programmable amplifiers and there is no method for adding DC
offset to the waveform. The Direct path can generate a maximum of 
1 V<sub>pk-pk</sub> at the CH 0 output into matched load
impedance. The maximum gain setting for an Analog Output path
configured to the Direct path is 0.527 (gain is a unitless
value).

The 
 Low-Gain Amplifier path has a 
2 V<sub>pk-pk</sub> amplifier and is used for waveforms that
have all output voltages equal to or smaller than 
2.0 V<sub>pk-pk</sub> into matched load impedance.
The High-Gain
Amplifier path has a 12 V<sub>pk-pk</sub> amplifier and is used for waveforms that have output voltages greater than 2.0 V<sub>pk-pk</sub> into matched load impedance. The gains of the amplifiers are constant. NI-FGEN automatically selects by default
between the high-gain and low-gain amplifiers, depending on the
NI-FGEN gain setting. You can configure the gain by calling the 
Arbitrary Waveform Gain or 
Amplitude
property or the 
NIFGEN_ATTR_ARB_GAIN or
NIFGEN_ATTR_FUNC_AMPLITUDE attribute.

You can configure the High-Gain or the Low-Gain
Amplifiers to remain in the Analog Output path regardless of gain
setting by calling the 
Analog Path
property or the 
NIFGEN_ATTR_ANALOG_PATH attribute. Configuring the Low-Gain
Amplifier path to remain constant regardless of the gain setting
affects the maximum output value allowable for that particular gain
setting. The maximum gain setting for an Analog Output path
configured to Low-Gain Amplifier path is 2.0
 . The maximum allowable
gain setting with NI-FGEN automatically selecting the Gain
Amplifier path is 12.0
 . Gain is a unitless value.

In addition, the DC offset amplifier, which adds 
*DC offset* to the signal, is
located in the High-Gain and Low-Gain Amplifier paths prior to the
attenuators and amplifiers. The DC offset amplifier can be
fine-tuned to add offset to your signal. This fine-tuning of the
main DC offset amplifier is performed by the offset DAC.

Parent topic:

NI 5422 Analog Output

Related concepts:

- NI 5422 DC Offset

<!--NI_TOPIC bundle=ni-fgen path=ni-5422-waveform-and-generation-instruction-m.html language=enus -->
## TOPIC 00417: NI 5422 Waveform and Generation Instruction Memory Size

- bundle_id: `ni-fgen`
- source_path: `ni-5422-waveform-and-generation-instruction-m.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5422-waveform-and-generation-instruction-m.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Waveform Memory Size Waveforms are stored in the NI 5422 onboard memory in contiguous blocks. These blocks are allocated in multiples of 128 bytes. This allocation style means that while waveform sizes may be multiples of four samples (eight bytes) on the NI 5422 , the amount of onboard memory alloc

### NI 5422 Waveform and Generation Instruction Memory Size

#### Waveform Memory Size

Waveforms are stored in the
NI 5422 onboard memory in contiguous
blocks. These blocks are allocated in multiples of 128 bytes. This
allocation style means that while waveform sizes may be multiples
of four samples (eight bytes) on the NI 5422
, the amount of
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
2. Memory is written to in blocks of 128 bytes.

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

The NI 5422 uses a
waveform generation engine that processes instructions that govern
how a waveform or a sequence of waveforms is generated. These
instructions determine which waveforms are generated, how the
device responds to triggers, how many times a waveform is looped,
when Marker events are generated, and so forth. The instructions
depend on the output mode, trigger mode, trigger source, waveforms
in onboard memory, and sequence lists that are configured. The
instructions are stored in the onboard memory along with the
waveform data. The calculations to determine the instruction size
that is stored in the onboard memory depends on the NI-FGEN output
mode and the NI-FGEN trigger mode. The following table includes
basic equations for determining the amount of memory, in bytes,
that are used for the different generation configurations.

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

Parent topic:

NI 5422 Onboard Memory

<!--NI_TOPIC bundle=ni-fgen path=ni-5422-waveform-generation.html language=enus -->
## TOPIC 00418: NI 5422 Waveform Generation

- bundle_id: `ni-fgen`
- source_path: `ni-5422-waveform-generation.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5422-waveform-generation.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5422 supports the following output, or generation, modes: Standard Function Arbitrary Waveform Arbitrary Sequence Script To select an output mode, set the Output Mode parameter of the niFgen Configure Output Mode VI or the niFgen_ConfigureOutputMode function.

### NI 5422 Waveform Generation

The NI 5422 supports the
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

NI 5422 NI 5422 Overview

Related concepts:

- NI 5422 Standard Function Mode
- NI 5422 Arbitrary Waveform Mode
- NI 5422 Arbitrary Sequence Mode
- NI 5422 Script Mode

<!--NI_TOPIC bundle=ni-fgen path=ni-5422-waveform-quantum.html language=enus -->
## TOPIC 00419: NI 5422 Waveform Quantum

- bundle_id: `ni-fgen`
- source_path: `ni-5422-waveform-quantum.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5422-waveform-quantum.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Quantum is the increment in samples that waveform sizes must adhere to. Waveforms must be downloaded in integer multiples of the four samples (or two for complex samples), the quantum for the NI 5422. For example, if while in Arbitrary Waveform mode, you request to load a waveform of seven samples,

### NI 5422 Waveform Quantum

Quantum is the increment in samples that waveform
sizes must adhere to. Waveforms must be downloaded in integer multiples of the four samples (or two for complex samples), the quantum for the NI 5422.

For example, if while in Arbitrary Waveform mode, you request to load a waveform of seven samples, the task will not complete successfully because the waveform is not an integer multiple of the quantum size. Waveform sizes that meet the conditions include 4, 8, 12, 16, 20, and so on, up to maximum allowable waveform size.

Parent topic:

NI 5422 Waveform Size and Quantum

<!--NI_TOPIC bundle=ni-fgen path=ni-5422-waveform-size-and-quantum.html language=enus -->
## TOPIC 00420: NI 5422 Waveform Size and Quantum

- bundle_id: `ni-fgen`
- source_path: `ni-5422-waveform-size-and-quantum.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5422-waveform-size-and-quantum.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5422 onboard memory architecture imposes certain requirements on the waveform size and quantum.

### NI 5422 Waveform Size and Quantum

The NI 5422 onboard memory architecture
imposes certain requirements on the waveform *size* and *quantum*.

Parent topic:

NI 5422 Waveform Generation

Related concepts:

- NI 5422 Waveform Size
- NI 5422 Waveform Quantum

<!--NI_TOPIC bundle=ni-fgen path=ni-5422-waveform-size.html language=enus -->
## TOPIC 00421: NI 5422 Waveform Size

- bundle_id: `ni-fgen`
- source_path: `ni-5422-waveform-size.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5422-waveform-size.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Minimum Waveform Size The minimum waveform size on the NI 5422 depends on the output mode and the trigger mode. Refer to the device specifications for the minimum waveform size values for the different modes. To provide greater programming flexibility, NI-FGEN does not strictly enforce the minimum

### NI 5422 Waveform Size

#### Minimum Waveform Size

The
minimum waveform size on the NI 5422 depends on the output mode and the 
*trigger mode*. Refer to
the 
*device
specifications* for the minimum waveform size values for the
different modes.

Note

device
specifications

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

NI 5422 Waveform Size and Quantum

Related concepts:

- NI 5422 Trigger Modes
- NI 5422 Waveform and Generation Instruction Memory Size

<!--NI_TOPIC bundle=ni-fgen path=ni-5441-aborting-generation.html language=enus -->
## TOPIC 00422: NI 5441 Aborting Generation

- bundle_id: `ni-fgen`
- source_path: `ni-5441-aborting-generation.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5441-aborting-generation.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can abort the generation of the current waveform. Aborting the generation exhibits different behaviors for different waveform output modes. Output Mode Abort Behavior Standard Function, Frequency List Abort to Ground—Signal remains at the level for which the DC offset is configured. Arbitrary Wa

### NI 5441 Aborting Generation

You can abort the generation of the current
waveform. Aborting the generation exhibits different behaviors for
different 
*waveform output
modes*.

| Output Mode | Abort Behavior |
| --- | --- |
| Standard Function, Frequency List | Abort to Ground—Signal remains at the level for which the DC offset is configured. |
| Arbitrary Waveform, Arbitrary Sequence, Script* | Abort to a Known Voltage—Signal remains at the last sample voltage level prior to the abort. |
| * These modes can also abort to ground. |  |

Related Topics

*Aborting to Ground*

*Aborting to a
Known Voltage*

Parent topic:

NI 5441 Waveform Generation

Related concepts:

- NI 5441 Waveform Generation
- Abort to Ground
- Abort to a Known Voltage

<!--NI_TOPIC bundle=ni-fgen path=ni-5441-access-and-active-leds.html language=enus -->
## TOPIC 00423: NI 5441 ACCESS and ACTIVE LEDs

- bundle_id: `ni-fgen`
- source_path: `ni-5441-access-and-active-leds.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5441-access-and-active-leds.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The ACCESS and ACTIVE LEDs indicate the status of the PXI module: ACCESS LED The ACCESS LED indicates basic hardware status as shown in the following table. Color Indications Off Device is not yet functional, or the device has detected a problem with a power rail. Amber The device is being accessed.

### NI 5441 ACCESS and ACTIVE LEDs

The ACCESS and ACTIVE LEDs indicate the status of
the PXI module:

#### ACCESS LED

The ACCESS LED indicates basic hardware status as
shown in the following table.

| Color | Indications |
| --- | --- |
| Off | Device is not yet functional, or the device has detected a problem with a power rail. |
| Amber | The device is being accessed. |
| Green | The device is ready to be programmed by NI-FGEN. |

#### ACTIVE LED

The ACTIVE LED indicates the device state as shown
in the following table.

| Color | Indications |
| --- | --- |
| Off | Device is not generating. |
| Amber | The device is armed and waiting for a trigger. |
| Green | The device has received a trigger. Also indicates that the device is generating a waveform. |
| Red | The device has detected an error. NI-FGEN must access the device to determine the cause of the error. The LED remains red until the error condition is removed. Example errors include the following: PLL Unlocked–The device has detected an unlocked condition on a previously locked PLL. A PLL that is unlocked while in reset does not show an error. The device has powered down because the internal temperature exceeded the maximum limit. The over-temperature condition must be corrected and the device reset. For more information about keeping your device cool, refer to the Maintain Forced-Air Cooling Note to Users included with your signal generator. To reset the device, call the niFgen Reset Device VI or the niFgen_ResetDevice function, or perform a device reset in MAX. |

Parent topic:

NI 5441 Front Panel

<!--NI_TOPIC bundle=ni-fgen path=ni-5441-accessories.html language=enus -->
## TOPIC 00424: NI 5441 Accessories

- bundle_id: `ni-fgen`
- source_path: `ni-5441-accessories.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5441-accessories.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: National Instruments offers a variety of products to use with your signal generator, including cables and other accessories. Visit ni.com for more information.

### NI 5441 Accessories

National Instruments offers a variety of products
to use with your signal generator, including cables and other
accessories. Visit 
ni.com for more
information.

Parent topic:

NI 5441 NI 5441 Overview

<!--NI_TOPIC bundle=ni-fgen path=ni-5441-amplitude-modulation-am-or-double-sid.html language=enus -->
## TOPIC 00425: NI 5441 Amplitude Modulation (AM) or Double Sideband

- bundle_id: `ni-fgen`
- source_path: `ni-5441-amplitude-modulation-am-or-double-sid.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5441-amplitude-modulation-am-or-double-sid.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can generate an AM radio signal with the OSP block. To generate an AM signal, complete the following steps. Enable onboard signal processing by setting the OSP Enabled property or the NIFGEN_ATTR_OSP_ENABLED attribute. Specify the use of real numbers for the waveform data by setting the Data Pro

### NI 5441 Amplitude Modulation (AM) or Double Sideband

[IMAGE alt='image' src='GUID-41744235-FED4-49B2-B15C-52247C47FD04-a5.gif']

You can generate an AM radio signal with the OSP
block. To generate an AM signal, complete the following steps.

1. Enable onboard signal processing by setting the 
OSP
Enabled property or the 
 NIFGEN_ATTR_OSP_ENABLED attribute.
2. Specify the use of real numbers for the waveform data by
setting the 
Data
Processing Mode property or the 
 NIFGEN_ATTR_OSP_DATA_PROCESSING_MODE attribute.
3. Set the 
IQ Rate
property or the 
 NIFGEN_ATTR_OSP_IQ_RATE attribute to the sample rate of the baseband data.
4. Set the 
Pre-Filter
Gain I property or the 
 NIFGEN_ATTR_OSP_PRE_FILTER_GAIN_I attribute to 0.5.
5. Set the 
Pre-Filter
Offset I property or the 
 NIFGEN_ATTR_OSP_PRE_FILTER_OFFSET_I attribute to 0.5. Steps 4 and 5 ensure that all interpolated
data is positive when it is mixed with the carrier.
6. Enable the carrier by setting the 
Carrier
Enabled property or the 
 NIFGEN_ATTR_OSP_CARRIER_ENABLED attribute.
7. Set the 
Carrier
Frequency property or the 
 NIFGEN_ATTR_OSP_CARRIER_FREQUENCY attribute to the station frequency.
8. Specify a flat FIR filter by setting the 
FIR Filter
Type property or the 
 NIFGEN_ATTR_OSP_FIR_FILTER_TYPE attribute.
9. Set the 
Flat
Filter Passband property or the 
 NIFGEN_ATTR_OSP_FIR_FILTER_FLAT_PASSBAND attribute to 0.4.
10. Download the waveform data to the signal generator.

Parent topic:

NI 5441 Common Onboard Signal Processing Applications

<!--NI_TOPIC bundle=ni-fgen path=ni-5441-analog-filter.html language=enus -->
## TOPIC 00426: NI 5441 Analog Filter

- bundle_id: `ni-fgen`
- source_path: `ni-5441-analog-filter.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5441-analog-filter.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The analog filter is a lowpass filter that is used to eliminate aliased images and artifacts due to the digital-to-analog conversion from the signal from the DAC. In general, use the analog filter for signals containing a large portion of sinusoidal content, such as AM and FM, sinc pulse, and sinuso

### NI 5441 Analog Filter

aliased images

niFgen_EnableAnalogFilter

niFgen_DisableAnalogFilter

Note

The delay from the time the device receives a Start
trigger to the time a signal is generated at the analog output
increases if the analog filter in the Analog Output path is
enabled. Refer to the 
*device
specifications* for information about the delay from the trigger
to the analog output based on the configured filter settings.

#### Related Topic

*Filtering and
Interpolation*

Parent topic:

NI 5441 Filtering Effects

Related concepts:

- Aliased Images
- Filtering and Interpolation

<!--NI_TOPIC bundle=ni-fgen path=ni-5441-analog-gain-settings.html language=enus -->
## TOPIC 00427: NI 5441 Analog Gain Settings

- bundle_id: `ni-fgen`
- source_path: `ni-5441-analog-gain-settings.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5441-analog-gain-settings.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following table summarizes the maximum and minimum gain setting that you can apply for the NI-FGEN analog path options. Refer to the device specifications for more information about gain resolution. Analog Path Gain Summary (Matched Load Impedance) NI-FGEN Analog Path Maximum Gain Value Minimum

### NI 5441 Analog Gain Settings

The following table summarizes the maximum and
minimum gain setting that you can apply for the NI-FGEN analog path
options. Refer to the 
*device
specifications* for more information about gain resolution.

| Analog Path Gain Summary (Matched Load Impedance) |  |  |
| --- | --- | --- |
| NI-FGEN Analog Path | Maximum Gain Value | Minimum Gain Value |
| Automatic (default) | 6.000 | 2.817 m |
| Fixed Low-Gain Amplifier | 1.027 | 2.817 m |
| Fixed High-Gain Amplifier | 6.000 | 16.91 m |
| Direct Path | 0.527 | 0.354 |
| Note: Gain is unitless. |  |  |

Note

Parent topic:

NI 5441 Waveform Amplitude Control

<!--NI_TOPIC bundle=ni-fgen path=ni-5441-analog-output.html language=enus -->
## TOPIC 00428: NI 5441 Analog Output

- bundle_id: `ni-fgen`
- source_path: `ni-5441-analog-output.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5441-analog-output.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the NI 5441 Analog Output signal path. NI 5441 analog waveforms are generated as follows: The 16-bit digital waveform data from the Waveform Generation Engine or OSP is passed to a digital gain circuit and then high-speed DAC. This DAC also implements a portion of the Anal

### NI 5441 Analog Output

The following figure shows the NI 5441 Analog Output signal path.

[IMAGE alt='image' src='GUID-1168A294-D930-4645-8DF7-E4E6E841D015-a5.gif']

NI 5441 analog waveforms are
generated as follows:

1. The 16-bit digital waveform data from the Waveform Generation
Engine or OSP is passed to a digital gain circuit and then
high-speed DAC. This DAC also implements a portion of the Analog
Output signal path attenuation with a range of 0 dB to
3 dB. Refer to the NI PXI-5441 Specifications for the exact resolution. You can adjust the amount
of attenuation by configuring the 
Arbitrary
Waveform Gain or 
Amplitude
properties or the 
 NIFGEN_ATTR_ARB_GAIN or 
 NIFGEN_ATTR_FUNC_AMPLITUDE attributes. NI-FGEN calculates and sets the correct amount of
attenuation required, corresponding to the gain setting.
2. Following the DAC, the signal can take one of two paths: the
Direct path or the Main path with High-Gain and Low-Gain
amplifiers. NI-FGEN selects the Main path by default. To select the
Direct path manually, use the 
Analog Path
property or the 
 NIFGEN_ATTR_ANALOG_PATH attribute.
  1. The Direct path bypasses the Analog Filter, the attenuation
sections, and the amplifiers. Taking the amplifiers out of the
signal path yields an output signal with the lowest distortion and
a flat frequency response. Use the Direct path for communication
signals. The Direct path can provide a maximum of 1 V pk-pk output into 50 Ω with no offset and a
maximum of 3 dB attenuation. A signal taking the Direct path
skips steps 3 through 5 and continues at step 6.
  2. If the Main path is selected, the
signal passes through a switchable lowpass Analog Filter,
attenuators, and amplifiers.
3. The signal then passes through a switchable lowpass Analog
Filter to remove 
 Aliased Images . You can
select whether to include the Analog Filter in the Analog Output
path using either the 
niFgen
Configure Analog Filter VI or the 
 niFgen_EnableAnalogFilter or 
 niFgen_DisableAnalogFilter functions.
4. The signal then passes through the DC Offset Amplifier that
adds the desired DC offset voltage. You can adjust the amount of DC
offset added to the signal, up to one half the value of the NI-FGEN
gain setting by using either the 
Arbitrary
Waveform Offset or 
DC Offset
properties or the 
 NIFGEN_ATTR_ARB_OFFSET or 
 NIFGEN_ATTR_FUNC_DC_OFFSET attributes.
5. The signal then passes through the Preamplifier Attenuation section,
a set of selectable solid-state attenuators that provide 0 dB
to 12 dB of attenuation in 3 dB increments. You can adjust the
amount of attenuation by adjusting the Arbitrary Waveform Gain
property or the 
 NIFGEN_ATTR_ARB_GAIN attribute.
NI-FGEN calculates and sets the correct amount of attenuation
required, corresponding to the gain setting configured with the 
Arbitrary
Waveform Gain or 
Amplitude
properties, or the 
 NIFGEN_ATTR_ARB_GAIN or 
 NIFGEN_ATTR_FUNC_AMPLITUDE attributes.
6. Following the Preamplifier Attenuation section, the signal can take
one of two paths: the High-Gain or Low-Gain Amplifier path. The High-Gain Amplifier path is used for waveform output
voltages greater than ±1.0 V into 50 Ω. The
amplifier has a fixed gain and is included in the signal path to
enable the AWG to provide the maximum V pk-pk . The Low-Gain Amplifier path is used for waveforms that have all
output voltages equal to or smaller than ±1.0 V into
50 Ω. The amplifier has a fixed gain. NI-FGEN
automatically selects the best amplifier path between the High-Gain
and Low-Gain amplifiers by default based on the gain or amplitude
setting. Alternatively, you can use the 
Analog Path
property or the 
 NIFGEN_ATTR_ANALOG_PATH attribute to set the signal path to remain
constant regardless of the gain setting for applications requiring
one path or the other.
7. The signal passes through the Postamplifier Attenuation section, a
set of two passive attenuators 12 dB and 24 dB. You can adjust the
amount of attenuation by configuring either the 
Arbitrary
Waveform Gain or 
Amplitude
properties, or the 
 NIFGEN_ATTR_ARB_GAIN or 
 NIFGEN_ATTR_FUNC_AMPLITUDE attributes. NI-FGEN calculates and sets the correct amount of
attenuation required, corresponding to the gain setting.
8. The signal then passes through the Output Enable relay. When
the Output Enable relay is disabled, ground is connected to the
output through a 50 Ω or a 75 Ω resistor.
Intentionally, waveform generation continues while the output
enable relay is disabled. When the relay is enabled, the analog
waveform is seen at the CH 0 connector. You can enable or
disable the output of the analog waveform generator by using the 
niFgen Output
Enable VI or the 
 niFgen_ConfigureOutputEnabled function.
9. The signal then passes through a
50 Ω/75 Ω selector to the
CH 0 connector. You can configure the output impedance of
the analog waveform generator by using the 
niFgen
Configure Output Impedance VI or the 
 niFgen_ConfigureOutputImpedance function.

Note

Parent topic:

NI 5441 Theory of Operation

Related concepts:

- Aliased Images

<!--NI_TOPIC bundle=ni-fgen path=ni-5441-arbitrary-sequence-mode.html language=enus -->
## TOPIC 00429: NI 5441 Arbitrary Sequence Mode

- bundle_id: `ni-fgen`
- source_path: `ni-5441-arbitrary-sequence-mode.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5441-arbitrary-sequence-mode.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Arbitrary Sequence mode allows you to load multiple waveforms in the onboard memory of the NI 5441. A finite number of samples make a waveform. To generate these downloaded waveforms in a specific order, you must prepare a sequence, which contains a number of segments in a specific order. Each segme

### NI 5441 Arbitrary Sequence Mode

*Arbitrary Sequence mode* allows you to load multiple
waveforms in the onboard memory of the NI 5441. A finite
number of samples make a waveform. To generate these downloaded
waveforms in a specific order, you must prepare a sequence, which
contains a number of segments in a specific order. Each segment
specifies a downloaded waveform, a number of loops to repeat the
selected waveform, and a numeric offset in which a marker is
generated by the device.

Parent topic:

NI 5441 Output Modes

Related concepts:

- Arbitrary Sequence Mode

<!--NI_TOPIC bundle=ni-fgen path=ni-5441-arbitrary-waveform-generation.html language=enus -->
## TOPIC 00430: NI 5441 Arbitrary Waveform Generation

- bundle_id: `ni-fgen`
- source_path: `ni-5441-arbitrary-waveform-generation.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5441-arbitrary-waveform-generation.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the behavior of the OSP block during basic arbitrary waveform generation . For basic arbitrary waveform generation, disable onboard signal processing by setting the OSP Enabled property or the NIFGEN_ATTR_OSP_ENABLED attribute.

### NI 5441 Arbitrary Waveform Generation

The following figure shows the behavior of the OSP
block during basic arbitrary waveform generation .

[IMAGE alt='image' src='GUID-43D36FE5-31A6-47BB-AC1B-B87EFB58A3A1-a5.gif']

For basic arbitrary waveform generation, disable
onboard signal processing by setting the 
OSP
Enabled property or the 
NIFGEN_ATTR_OSP_ENABLED attribute.

Parent topic:

NI 5441 Common Onboard Signal Processing Applications

<!--NI_TOPIC bundle=ni-fgen path=ni-5441-arbitrary-waveform-mode.html language=enus -->
## TOPIC 00431: NI 5441 Arbitrary Waveform Mode

- bundle_id: `ni-fgen`
- source_path: `ni-5441-arbitrary-waveform-mode.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5441-arbitrary-waveform-mode.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5441 supports Arbitrary Waveform output mode. Arbitrary Waveform mode generates waveforms from user-created/provided waveform arrays of numeric data. The waveform arrays are downloaded to the arbitrary waveform generator onboard memory. Arbitrary Waveform mode also uses memory to store the in

### NI 5441 Arbitrary Waveform Mode

The NI 5441 supports Arbitrary Waveform output mode. Arbitrary Waveform mode generates waveforms from
user-created/provided waveform arrays of numeric data. The waveform
arrays are downloaded to the arbitrary waveform generator onboard
memory. *Arbitrary Waveform mode* also uses memory to
store the instructions for generating waveform sequences in the
onboard memory.

Parent topic:

NI 5441 Output Modes

Related concepts:

- Arbitrary Waveform Output Mode

<!--NI_TOPIC bundle=ni-fgen path=ni-5441-attenuation.html language=enus -->
## TOPIC 00432: NI 5441 Attenuation

- bundle_id: `ni-fgen`
- source_path: `ni-5441-attenuation.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5441-attenuation.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Analog Output path has two passive attenuation sections. Preamplifier attenuation is prior to the High-Gain and Low-Gain Amplifier paths, and postamplifier attenuation is after the High-Gain and Low-Gain Amplifier paths. The main DAC provides 0 to 3 dB of signal attenuation. Amplitude control is

### NI 5441 Attenuation

The Analog Output path has two passive attenuation
sections. *Preamplifier attenuation* is prior to the High-Gain
and Low-Gain Amplifier paths, and *postamplifier attenuation* is after the
High-Gain and Low-Gain Amplifier paths.

The main *DAC* provides 0 to 3 dB of signal attenuation. Amplitude control is implemented after the DAC. Attenuating the DAC output signal allows you to vary the signal amplitude while maintaining the dynamic range of the DAC. You do not lose any bits from the digital representation of the signal and you do not sacrifice dynamic range, as you would if you control amplitude by using smaller data ranges of the DAC. Passive attenuation by preamplifier and postamplifier attenuation is not available if the Direct path is selected.

For the Low-Gain and the High-Gain Amplifier paths, maximum attenuation is
51 dB. For the Direct path, maximum output attenuation is 3
dB. NI-FGEN automatically determines the correct value of attenuation in dB and configures the attenuation based on the set
gain. The minimum gain setting for the Direct path is 0.354. The
minimum gain setting for an Analog Output path configured to
High-Gain Amplifier path is .01691. The minimum allowable gain
setting with NI-FGEN automatically selecting the Low-Gain Amplifier
path is .00282 (gain is a unitless value).

NI-FGEN calculates and sets the correct amount of
attenuation required that corresponds to your NI-FGEN gain setting.
The correct amount of attenuation is implemented in the 
preamplifier and postamplifier attenuation blocks to best achieve
the desired output signal amplitude. You can set the amount of gain
with the Arbitrary Waveform Gain property or the 
NIFGEN_ATTR_ARB_GAIN attribute.

Parent topic:

NI 5441 Waveform Amplitude Control

Related concepts:

- NI 5441 Preamplifier Attenuation
- NI 5441 Postamplifier Attenuation
- NI 5441 DAC Attenuation

<!--NI_TOPIC bundle=ni-fgen path=ni-5441-baseband-interpolation.html language=enus -->
## TOPIC 00433: NI 5441 Baseband Interpolation

- bundle_id: `ni-fgen`
- source_path: `ni-5441-baseband-interpolation.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5441-baseband-interpolation.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the behavior of the OSP block during baseband interpolation. Baseband interpolation allows the OSP block to interpolate signals at a low sample rate up to a high sample rate. Arbitrary pulse shaping of the data can also be done in the FIR filter. For baseband interpolation

### NI 5441 Baseband Interpolation

The following figure shows the behavior of the OSP
block during baseband interpolation.

[IMAGE alt='image' src='GUID-65E54B53-67B7-4DC9-A63A-DC9474580C25-a5.gif']

Baseband interpolation allows the OSP block to
interpolate signals at a low sample rate up to a high sample rate.
Arbitrary pulse shaping of the data can also be done in the FIR
filter. For baseband interpolation, complete the following
steps.

1. Enable onboard signal processing by setting the 
OSP
Enabled property or the 
 NIFGEN_ATTR_OSP_ENABLED attribute.
2. Specify the use of real numbers for the waveform data by
setting the 
Data
Processing Mode property or the 
 NIFGEN_ATTR_OSP_DATA_PROCESSING_MODE attribute.
3. Set the 
IQ Rate
property or the 
 NIFGEN_ATTR_OSP_IQ_RATE attribute to the low sample rate of the waveform data.
4. Set the 
FIR Filter
Type property or the 
 NIFGEN_ATTR_OSP_FIR_FILTER_TYPE attribute.
5. Set the corresponding filter parameter or download a 
 custom set of FIR
filter coefficients .
6. Disable the carrier by setting the 
Carrier
Enabled property or the 
 NIFGEN_ATTR_OSP_CARRIER_ENABLED attribute.
7. Download the low sample rate waveform(s) to the signal
generator.

Parent topic:

NI 5441 Common Onboard Signal Processing Applications

Related concepts:

- NI 5441 FIR Filter Type: Custom

<!--NI_TOPIC bundle=ni-fgen path=ni-5441-basic-onboard-signal-processing-prope.html language=enus -->
## TOPIC 00434: NI 5441 Basic Onboard Signal Processing Properties

- bundle_id: `ni-fgen`
- source_path: `ni-5441-basic-onboard-signal-processing-prope.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5441-basic-onboard-signal-processing-prope.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following properties configure the OSP block: OSP Enabled Data Processing Mode IQ Rate Carrier Enabled Carrier Frequency FIR Filter Type

### NI 5441 Basic Onboard Signal Processing Properties

The following properties configure the OSP block:

- OSP Enabled
- Data Processing
Mode
- IQ Rate

- Carrier
Enabled

- Carrier
Frequency

- FIR Filter Type

Parent topic:

NI 5441 Onboard Signal Processing (OSP)

Related concepts:

- NI 5441 OSP Enabled
- NI 5441 Data Processing Mode
- NI 5441 IQ Rate
- NI 5441 Carrier Frequency
- NI 5441 FIR Filter Type

<!--NI_TOPIC bundle=ni-fgen path=ni-5441-block-diagram.html language=enus -->
## TOPIC 00435: NI 5441 Block Diagram

- bundle_id: `ni-fgen`
- source_path: `ni-5441-block-diagram.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5441-block-diagram.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: This topic contains information about the NI PXI-5441 top-level block diagram and descriptions of the individual blocks. If it is installed in any slot other than Slot 2 of the PXI chassis, the NI 5441 can receive a signal on the PXI_STAR line and can route a signal on the PXI_STAR line back to Sl

### NI 5441 Block Diagram

This topic contains information about the
NI PXI-5441 top-level block diagram and descriptions of the
individual blocks.

[IMAGE alt='image' src='GUID-D7D673A0-326F-463D-BB96-9729C3842100-a5.gif']

Note

The following list describes the individual
blocks:

- Onboard Memory stores the waveform data and generation
instructions that you load into the device.
- Clocking allows you to create your Sample clock and
Reference clock.
- The 
 Waveform Generation Engine retrieves the waveform data and
instructions from the 
 Onboard Memory using the Sample clock. The 
 Waveform Generation Engine also uses this clock to
retrieve triggers from 
 Trigger and Event Control .
- The output from the 
 Waveform Generation Engine is sent to the 
 DAC device and the 
 DIGITAL DATA & CONTROL Connector on the front panel
after any digital gain or onboard signal processing is
applied.
- The 
 DAC also contains a selectable 
 Digital Filter , which interpolates and filters the
waveform data.
- The waveform data is sent from the 
 DAC to the 
 Analog Output path where the waveform data is filtered and
amplified.
- The 
 Routing Matrix allows flexible routing of the PXI Trigger
lines (RTSI) and the external PFI lines.

Parent topic:

NI 5441 Theory of Operation

<!--NI_TOPIC bundle=ni-fgen path=ni-5441-burst-trigger-mode.html language=enus -->
## TOPIC 00436: NI 5441 Burst Trigger Mode

- bundle_id: `ni-fgen`
- source_path: `ni-5441-burst-trigger-mode.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5441-burst-trigger-mode.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: In Burst trigger mode, calling the first Start trigger begins waveform generation. The waveform then generates continually. The following table provides more information about waveform generation behavior in Arbitrary Waveform, Arbitrary Sequence, and Frequency List output modes. Output Mode Trigger

### NI 5441 Burst Trigger Mode

In Burst trigger mode, calling the first Start
trigger begins waveform generation. The waveform then generates
continually. The
following table provides more information about
waveform generation behavior in Arbitrary Waveform, Arbitrary
Sequence, and Frequency List output modes.

| Output Mode | Trigger Behavior |
| --- | --- |
| Arbitrary Waveform Mode | Burst trigger mode operates the same as Continuous trigger mode when the device is operating in Arbitrary Waveform mode. |
| Arbitrary Sequence Mode | Each waveform you define in the sequence list generates continuously until another Start trigger occurs. A Start trigger causes the waveform generation to switch to the waveform defined by the next segment, after the current waveform finishes. After the sequence list is exhausted, the waveform generation returns to the waveform defined by the first segment and subsequent Start triggers will restart the process. Only the first Start trigger which signals a transition to the next segment is recognized, all subsequent Start triggers are ignored until the currently generating waveform finishes. The transition of one waveform to the next can be made amplitude continuous if waveforms in all segments start and end at the same amplitude. Alternatively, this also can be accomplished by ensuring that the waveforms from one segment to the next end and start at the same amplitude. This amplitude continuous transition is shown in the previous Arbitrary Sequence Mode examples by the transitions of Segments 1 to Segment 2, and Segment 3 to Segment 4. The transition from Segment 2 to Segment 3 shows a discontinuous transition, going from a positive value on the last sample of the ramp waveform right to a midrange value of the sine waveform. |
| Frequency List Mode | The device generates the next step in the active frequency list every time a Start trigger occurs. After the duration for a step elapses, the waveform generates until the next Start trigger is received. When the next Start trigger is received, the next step in the frequency list generates. If a Start trigger is received within the specified duration of the step, the Start trigger is applied after the duration elapses. Any additional Start triggers received within the duration are ignored. If the Trigger Source property or the NIFGEN_ATTR_TRIGGER_SOURCE attribute is set to NIFGEN_VAL_IMMEDIATE, the only way to advance to the next step in the frequency list is to call the niFgen Send Software Edge Trigger VI or the niFgen_SendSoftwareEdgeTrigger function. |

Parent topic:

NI 5441 Trigger Modes

Related concepts:

- NI 5441 Continuous Trigger Mode

<!--NI_TOPIC bundle=ni-fgen path=ni-5441-calibration.html language=enus -->
## TOPIC 00437: NI 5441 Calibration

- bundle_id: `ni-fgen`
- source_path: `ni-5441-calibration.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5441-calibration.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Before shipping your signal generator, NI calibrated your device to ensure that all features are within specifications. Calibration is a set of operations that compares the values indicated by a measuring instrument or measuring system to the corresponding values realized by external standards. You

### NI 5441 Calibration

Before shipping your signal generator,
NI calibrated your device to ensure that all features are
within specifications.

Calibration is a set of operations that compares
the values indicated by a measuring instrument or measuring system
to the corresponding values realized by external standards. You can
use the results of calibration to determine the measurement error
and can then correct for it in the adjustment process.

The calibration process consists of verifying,
adjusting, and reverifying a device. During verification, you
compare the measured performance to an external standard of known
measurement uncertainty to confirm that the product meets or
exceeds specifications. During adjustment, you correct the
measurement error of the device by adjusting the calibration
constants and storing the new calibration constants in the EEPROM.
The host computer reads the calibration constants and the software
uses them to compensate for errors in the data and to present
calibrated data to the user.

For more information about calibrating the signal
generator, refer to the 
*device calibration*
procedures.

For more information about calibration in general,
refer to ni.com/calibration.

Parent topic:

NI 5441 NI 5441 Overview

<!--NI_TOPIC bundle=ni-fgen path=ni-5441-carrier-frequency.html language=enus -->
## TOPIC 00438: NI 5441 Carrier Frequency

- bundle_id: `ni-fgen`
- source_path: `ni-5441-carrier-frequency.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5441-carrier-frequency.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The carrier frequency determines the frequency of the cosine waves (both I and Q) exported from the NCO . You can use the Carrier Frequency property or the NIFGEN_ATTR_OSP_CARRIER_FREQUENCY attribute to set the carrier frequency. This frequency is programmable during signal generation. For I/Q Rates

### NI 5441 Carrier Frequency

The carrier frequency determines the frequency of
the cosine waves (both I and Q) exported from the 
*NCO* . You can use the 
Carrier
Frequency property or the 
NIFGEN_ATTR_OSP_CARRIER_FREQUENCY attribute to set the carrier frequency. This frequency is
programmable during signal generation.

For 
*I/Q Rates* below the
interpolation range of the OSP block, NI-FGEN selects a lower
Sample clock rate in order to achieve the requested I/Q Rate.
Because the carrier cannot be more than 0.43 × Sample Rate, these
lower sample rates translate to lower valid carrier rates. The
largest carrier frequency that can be generated for a given I/Q Rate
with a maximum 
*CIC interpolation* of 256× can
be calculated using the following formula:

Max Carrier Frequency = I/Q Rate × 256 × FIR
Interpolation × 0.43

The following table summarizes the maximum carrier
frequency for all FIR interpolation factors.

| FIR Interpolation Factor | Approximate MaximumCarrier Frequency |
| --- | --- |
| 2 | 220 × I/Q Rate |
| 4 | 440 × I/Q Rate |
| 8 | 880 × I/Q Rate |

Parent topic:

NI 5441 Basic Onboard Signal Processing Properties

Related concepts:

- NI 5441 Numerically Controlled Oscillator (NCO)
- NI 5441 IQ Rate
- NI 5441 CIC Filter

<!--NI_TOPIC bundle=ni-fgen path=ni-5441-ch-0-connector.html language=enus -->
## TOPIC 00439: NI 5441 CH 0 Connector

- bundle_id: `ni-fgen`
- source_path: `ni-5441-ch-0-connector.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5441-ch-0-connector.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The CH 0 connector is the analog waveform output terminal. The maximum output levels from this connector depend on the type of load termination. For example, if the output of the device terminates into a 50 Ω load, the maximum output levels are ±6 V, while the maximum output levels are ±12 V when th

### NI 5441 CH 0 Connector

The CH 0 connector is the analog waveform
output terminal. The maximum output levels from this connector
depend on the type of load termination. For example, if the output of the device
terminates into a 50 Ω load, the maximum output levels
are ±6 V, while the maximum output levels are ±12 V when the
device terminates into a high-impedance load (HiZ). This difference
is illustrated in the following figure.

[IMAGE alt='image' src='GUID-836822F7-163C-475A-B0EB-3D94BB52CBAB-a5.gif']

If the output terminates into any other load, the
levels are defined by the following formula:

V<sub>out</sub>
 = ± [ 
R<sub>L</sub>
 / ( 
R<sub>L</sub>
 + 
R<sub>O</sub>
 ) ] × 12 V

where

V<sub>out</sub> is the maximum peak output voltage level

R<sub>L</sub>
 is the load impedance in ohms

O

Note

out

By default, 
R<sub>O</sub>
 = 50 Ω, but you can set the output
impedance to 75 Ω in NI-FGEN. You can configure the output impedance by calling the 
niFgen Configure Output Impedance VI or the 
niFgen_ConfigureOutputImpedance function.

You can set the amplitude of the generated output
signal in terms of peak voltage by setting the gain value. NI-FGEN
calculates and sets the correct amount of attenuation required for
the desired gain value. You can configure the output signal amplitude by calling the Amplitude property
 or NIFGEN_ATTR_FUNC_AMPLITUDE attribute, or the
 
Arbitrary Waveform Gain property or
NIFGEN_ATTR_ARB_GAIN attribute.

#### Load Impedance Compensation

The NI 5441 has the ability to configure the
output signal amplitude based on a user-configured load impedance
setting. This capability is desirable when you use the NI 5441
with loads that are between 0 Ω and a high impedance.
Refer to the 
*device
specifications* for information about the output impedance
tolerance.

By default, NI-FGEN assumes that the load impedance
is equal to the output impedance. If they do not match, you can
change the load impedance value that NI-FGEN uses in its load
impedance compensation algorithm. NI-FGEN takes the load impedance
into account when setting the amplitude and provides the amplitude
specified in the configured gain setting, eliminating the need to use
the voltage divider equation. NI-FGEN compensates to give the
desired peak-to-peak voltage amplitude or arbitrary gain (relative to 1 V). You can configure the load impedance by calling the 
Load
Impedance property or 
NIFGEN_ATTR_LOAD_IMPEDANCE attribute.

Note

For waveform output
signal specifications, refer to the 
*device
specifications*.

Parent topic:

NI 5441 Front Panel

<!--NI_TOPIC bundle=ni-fgen path=ni-5441-cic-filter.html language=enus -->
## TOPIC 00440: NI 5441 CIC Filter

- bundle_id: `ni-fgen`
- source_path: `ni-5441-cic-filter.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5441-cic-filter.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: A CIC (Cascaded Integrator Comb) filter is designed to allow high levels of interpolation without high levels of computation. Most of the interpolation in the OSP block is done in the CIC filter. The interpolation range of the CIC filter is 6x to 256x. The CIC filter is a series of combs (differenti

### NI 5441 CIC Filter

Note

When using the CIC filter, consider the
following:

- Frequency
Response
- Gain
- Overflow

[IMAGE alt='image' src='GUID-5737DACE-1842-4F45-8DC1-DC525BAB4180-a5.gif']

Parent topic:

NI 5441 Onboard Signal Processing Components

Related concepts:

- NI 5441 CIC Frequency Response
- NI 5441 CIC Gain
- NI 5441 CIC Overflow

<!--NI_TOPIC bundle=ni-fgen path=ni-5441-cic-frequency-response.html language=enus -->
## TOPIC 00441: NI 5441 CIC Frequency Response

- bundle_id: `ni-fgen`
- source_path: `ni-5441-cic-frequency-response.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5441-cic-frequency-response.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The frequency response (in dB) of the CIC follows the following formula: where R = CIC Interpolation Rate f = Frequency (fraction of CIC input sample rate) The following diagram shows the response of a six stage CIC filter with 8x interpolation. Notice that the frequency response has a significant a

### NI 5441 CIC Frequency Response

The frequency response (in dB) of the CIC follows
the following formula:

[IMAGE alt='image' src='GUID-894C0C14-D219-4CCE-9148-D50CC6A05EA9-a5.gif']

where

R = CIC Interpolation Rate

f = Frequency (fraction of CIC input sample
rate)

The following diagram shows the response of a six
stage CIC filter with 8x interpolation.

[IMAGE alt='image' src='GUID-3058C851-24B4-4162-B82E-BAA5C9D7695E-a5.gif']

Notice that the frequency response has a
significant amount of roll-off in the passband. You must compensate
for 
*CIC* roll-off in custom 
*FIR filters* in order to
obtain an overall flat response.

Parent topic:

NI 5441 CIC Filter

Related concepts:

- NI 5441 CIC Filter
- NI 5441 FIR Filter

<!--NI_TOPIC bundle=ni-fgen path=ni-5441-cic-gain.html language=enus -->
## TOPIC 00442: NI 5441 CIC Gain

- bundle_id: `ni-fgen`
- source_path: `ni-5441-cic-gain.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5441-cic-gain.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The CIC gain is applied after the CIC filter. The CIC filter gain is used to compensate for attenuation in the FIR filter and CIC filter. NI-FGEN automatically calculates and applies this gain when an FIR filter type other than Custom is used. You can override the CIC filter gain by setting the CIC

### NI 5441 CIC Gain

The CIC gain is applied after the 
*CIC filter*. The CIC filter
gain is used to compensate for attenuation in the 
*FIR filter* and CIC filter.
NI-FGEN automatically calculates and applies this gain when an FIR
filter type other than Custom is used. You can override the CIC
filter gain by setting the 
CIC
Filter Gain property or the 
NIFGEN_ATTR_OSP_CIC_FILTER_GAIN attribute. You should be careful when setting the CIC gain to
prevent 
*CIC overflows* from
occurring. The CIC gain range is from 1.0 to 16.0.

Parent topic:

NI 5441 CIC Filter

Related concepts:

- NI 5441 CIC Filter
- NI 5441 FIR Filter
- NI 5441 CIC Overflow

<!--NI_TOPIC bundle=ni-fgen path=ni-5441-cic-overflow.html language=enus -->
## TOPIC 00443: NI 5441 CIC Overflow

- bundle_id: `ni-fgen`
- source_path: `ni-5441-cic-overflow.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5441-cic-overflow.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: A CIC overflow can occur if the CIC gain is set too high for the incoming data set. When the CIC overflows, the data is clipped at the rail where the overflow occurred and the OSP block continues to process data. NI-FGEN returns an error when the status of the signal generator is checked. To disab

### NI 5441 CIC Overflow

Tip

NIFGEN_ATTR_OSP_OVERFLOW_ERROR_REPORTING

Parent topic:

NI 5441 CIC Filter

<!--NI_TOPIC bundle=ni-fgen path=ni-5441-clk-in-connector.html language=enus -->
## TOPIC 00444: NI 5441 CLK IN Connector

- bundle_id: `ni-fgen`
- source_path: `ni-5441-clk-in-connector.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5441-clk-in-connector.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The CLK IN front panel connector can accept an external Reference clock, external Sample clock, or external Sample clock timebase. Do not change the external clocks while generating waveforms. Only modify the frequency of the external clock before you start the waveform generation or after you sto

### NI 5441 CLK IN Connector

Caution

not

before

after

#### External Reference Clock Input

The CLK IN connector can accept a Reference clock
from an external source and phase-lock the internal clock of the
signal generator to this external Reference clock. Refer to the 
*device
specifications* for the allowable Reference clock frequencies
and signal characteristics.

The Reference clock uses the internal clock by
default. Call the 
niFgen
Configure Reference Clock VI or the 
niFgen_ConfigureReferenceClock function to configure the Reference
clock source.

When configuring an external Reference clock, you
must configure the external Reference clock frequency if it is
different from the 10 MHz default setting. Set the Reference clock frequency with the 
niFgen
Configure Reference Clock VI or the niFgen_ConfigureReferenceClock function.

Note

PLL Reference
Sources

#### External Sample Clock Input

In addition to phase-locking, the CLK IN connector
also can receive an external Sample clock. Refer to the 
*device
specifications* for the allowable external Sample clock
frequencies and signal characteristics.

Tip

niFgen_ConfigureSampleRate

Configure the Sample clock source with 
niFgen
Configure Sample Clock Source VI or the 
niFgen_ConfigureSampleClockSource function. The Sample clock uses the internal clock by
default.

Parent topic:

NI 5441 Front Panel

Related concepts:

- NI 5441 Phase-Locked Loop Reference Clock

<!--NI_TOPIC bundle=ni-fgen path=ni-5441-clocking-options.html language=enus -->
## TOPIC 00445: NI 5441 Clocking Options

- bundle_id: `ni-fgen`
- source_path: `ni-5441-clocking-options.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5441-clocking-options.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Waveform generation is driven by the Sample clock; depending on your application, some sources may be better choices than others. You can use the following sources for the NI 5441 Sample clock: Internal Sample clock—the onboard clock is used as the Sample clock source and the Sample clock is derived

### NI 5441 Clocking Options

Waveform generation is driven by the Sample clock;
depending on your application, some sources may be better choices
than others. You can use the following sources for the
NI 5441 Sample clock:

- Internal Sample clock —the onboard clock is used as the
Sample clock source and the Sample clock is derived from the Sample
clock timebase via either Divide by N or High–Resolution clock
mode.
- External Sample clock —the Sample clock has an external
source that derives device clocking by directly driving the DAC and all waveform generation operations on the device.
- Reference clock —the Sample clock is derived from an
external source that is phase–locked to the Sample clock
timebase. The phase-locked loop (PLL) Reference clock source
specifies the source of the control voltage that tunes the VCXO of
the Sample clock timebase for internal clock update sources. The
PLL circuit adjusts the Sample clock timebase VCXO to synchronize
to a Reference clock. The frequency stability of the Sample clock
timebase matches that of the PLL Reference clock when the two are
phase-locked. Phase-locking also synchronizes multiple device
clocks that are phase–locked to the same Reference clock.

The following table shows the valid NI-FGEN
property or attribute value combinations that can be used to
configure the NI 5441 clock settings for
an internal Sample clock, an external Sample clock, or a Reference
clock. The term 
Update clock is synonymous with 
Sample clock.

| Sample Clock Source* | Clock Mode * | PLL Reference Clock Source * |
| --- | --- | --- |
| "OnboardClk" (default) | NIFGEN_VAL_DIVIDE_DOWN | "None" (default) |
| "PXI_CLK10", "RTSI7" |  |  |
| "ClkIn" |  |  |
| "OnboardRefClk" |  |  |
| NIFGEN_VAL_HIGH_RESOLUTION | "None" (default) |  |
| "PXI_CLK10", "RTSI7" |  |  |
| "ClkIn" |  |  |
| "OnboardRefClk" |  |  |
| NIFGEN_VAL_AUTOMATIC (default) | "None" (default) |  |
| "PXI_CLK10", "RTSI7" |  |  |
| "ClkIn" |  |  |
| "OnboardRefClk" |  |  |
| "ClkIn" | Not Applicable | Not Applicable |
| "PXI_STAR" |  |  |
| "PXI_Trig<0..6>" |  |  |
| "DDC_ClkIn" |  |  |
| *These column headings refer to NI-FGEN properties. The attributes that correspond to these properties are NIFGEN_ATTR_SAMPLE_CLOCK_SOURCE, NIFGEN_ATTR_CLOCK_MODE, and NIFGEN_ATTR_REFERENCE_CLOCK_SOURCE. The values in the columns represent the values that can be set on these properties or attributes. Settings that line up horizontally show valid combinations of the NI-FGEN settings. |  |  |

Parent topic:

NI 5441 Clocking

Related concepts:

- NI 5441 Internal Sample Clock
- NI 5441 External Sample Clock
- NI 5441 Phase-Locked Loop Reference Clock

<!--NI_TOPIC bundle=ni-fgen path=ni-5441-clocking.html language=enus -->
## TOPIC 00446: NI 5441 Clocking

- bundle_id: `ni-fgen`
- source_path: `ni-5441-clocking.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5441-clocking.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5441 has a Sample clock rate of 10 Hz to 100 MHz. The timing of the device is very flexible, and you have multiple choices for deriving the Sample clock. There are modes for deriving the Sample clock from the internal Sample clock timebase, as well as modes to provide external clocks. You als

### NI 5441 Clocking

The NI 5441 has a Sample clock
rate of 10 Hz to 100 MHz. The timing of the device
is very flexible, and you have multiple choices for deriving the
Sample clock. There are modes for deriving the Sample clock from
the internal Sample clock timebase, as well as modes to provide
external clocks. You also have several choices for providing the
frequency reference for the onboard phase-locked loop.

[IMAGE alt='image' src='GUID-E29E53C4-1CBC-4D93-BB7D-9772D14E126A-a5.gif']

Related Topics

*Clocking Options*

*Internal Sample Clock
Sources*

*Phase-Locked Loop
Reference Clock Sources*

*External Sample
Clock Sources*

*Exporting Clocks*

Parent topic:

NI 5441 Theory of Operation

Related concepts:

- NI 5441 Clocking Options
- NI 5441 Internal Sample Clock
- NI 5441 Phase-Locked Loop Reference Clock
- NI 5441 External Sample Clock
- NI 5441 Exporting Clocks

<!--NI_TOPIC bundle=ni-fgen path=ni-5441-common-onboard-signal-processing-appl.html language=enus -->
## TOPIC 00447: NI 5441 Common Onboard Signal Processing Applications

- bundle_id: `ni-fgen`
- source_path: `ni-5441-common-onboard-signal-processing-appl.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5441-common-onboard-signal-processing-appl.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The OSP block is particularly useful for the following common applications: Arbitrary Waveform Generation Single-Tone Generation Quadrature Upconversion Amplitude Modulation (AM) or Double Sideband Baseband Interpolation

### NI 5441 Common Onboard Signal Processing Applications

The OSP block is particularly useful for the
following common applications:

- Arbitrary Waveform
Generation

- Single-Tone
Generation
- Quadrature
Upconversion
- Amplitude Modulation
(AM) or Double Sideband
- Baseband
Interpolation

Parent topic:

NI 5441 Onboard Signal Processing (OSP)

Related concepts:

- NI 5441 Arbitrary Waveform Generation
- NI 5441 Single-Tone
- NI 5441 Quadrature Upconversion
- NI 5441 Amplitude Modulation (AM) or Double Sideband
- NI 5441 Baseband Interpolation

<!--NI_TOPIC bundle=ni-fgen path=ni-5441-continuous-trigger-mode.html language=enus -->
## TOPIC 00448: NI 5441 Continuous Trigger Mode

- bundle_id: `ni-fgen`
- source_path: `ni-5441-continuous-trigger-mode.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5441-continuous-trigger-mode.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The waveform you downloaded generates continuously after receiving one Start trigger. All Start triggers after the first Start trigger are ignored. The following table provides more information about waveform generation behavior in Arbitrary Waveform, Arbitrary Sequence, and Frequency List output mo

### NI 5441 Continuous Trigger Mode

The waveform you downloaded generates continuously
after receiving one Start trigger. All Start triggers after the
first Start trigger are ignored. The
following table provides more information about
waveform generation behavior in Arbitrary Waveform, Arbitrary
Sequence, and Frequency List output modes.

| Output Mode | Trigger Behavior |
| --- | --- |
| Arbitrary Waveform Mode | The waveform you downloaded generates continuously after receiving one Start trigger. All Start triggers after the first Start trigger are ignored. |
| Arbitrary Sequence Mode | The waveform pattern you define in the sequence list generates continuously by continually cycling through the sequence list. Only one Start trigger is required to start waveform generation. After the device receives a Start trigger, the waveform generation starts at the first segment and continues through the last segment, and then loops back to the start of the first segment, continuing indefinitely. All Start triggers after the first Start trigger that starts waveform generation are ignored. |
| Frequency List Mode | The device generates the next step in the active frequency list once the duration of the step has elapsed. The frequency list repeats until generation is aborted. The frequency list generates continuously after receiving one Start trigger. All Start triggers after the first Start trigger are ignored. |

Parent topic:

NI 5441 Trigger Modes

<!--NI_TOPIC bundle=ni-fgen path=ni-5441-dac-attenuation.html language=enus -->
## TOPIC 00449: NI 5441 DAC Attenuation

- bundle_id: `ni-fgen`
- source_path: `ni-5441-dac-attenuation.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5441-dac-attenuation.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The main DAC output can be fine-tuned for attenuation, which provides 0 to 3 dB of the Analog Output path signal attenuation. This fine-tuning of the main DAC attenuation is performed by the gain DAC. Adjust the gain DAC using the Gain DAC Value property or the NIFGEN_ATTR_GAIN_DAC_VALUE attribute.

### NI 5441 DAC Attenuation

The main DAC output can be fine-tuned for
attenuation, which provides 0 to 3 dB of the Analog Output
path signal attenuation. This fine-tuning of the main DAC
attenuation is performed by the gain DAC. Adjust the gain
DAC using the 
Gain
DAC Value property or the 
NIFGEN_ATTR_GAIN_DAC_VALUE attribute. The main DAC also
provides the fine resolution for the attenuation settings.

Parent topic:

NI 5441 Attenuation

<!--NI_TOPIC bundle=ni-fgen path=ni-5441-data-mask.html language=enus -->
## TOPIC 00450: NI 5441 Data Mask

- bundle_id: `ni-fgen`
- source_path: `ni-5441-data-mask.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5441-data-mask.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The signal generator supports analog and digital data masks and static values. The data mask allows you to shield bits of the data to be replaced with the corresponding static value bits. For example, a mask of 0xFF00 and a static value of 0xAAAA applied to a DC waveform with a value of 0x1111 produ

### NI 5441 Data Mask

The signal generator supports analog and digital
data masks and static values. The data mask allows you to shield
bits of the data to be replaced with the corresponding static value
bits. For example, a mask of 0xFF00 and a static value of 0xAAAA
applied to a DC waveform with a value of 0x1111 produces a DC
waveform with a value of 0x11AA.

NI-FGEN supports separate and independent analog
and digital data masks and static values. The analog data mask and
analog static value apply to the digital data applied to the DAC,
and ultimately to the signal on the analog output terminal. The
analog data mask and analog static value do not affect the signals
on the digital connector. You can configure an analog data mask by calling the 
Analog Data
Mask or 
Analog
Static Value properties or the 
NIFGEN_ATTR_ANALOG_DATA_MASK and 
NIFGEN_ATTR_ANALOG_STATIC_VALUE attributes. The digital data mask and digital static value
apply to the signals on the digital connector and they do not
affect the signal on the analog output terminal. You can configure a digital data mask by calling the 
Digital
Data Mask or 
Digital
Static Value properties or the 
NIFGEN_ATTR_DIGITAL_DATA_MASK and 
NIFGEN_ATTR_DIGITAL_STATIC_VALUE attributes.

Parent topic:

NI 5441 NI 5441 Overview

<!--NI_TOPIC bundle=ni-fgen path=ni-5441-data-processing-mode.html language=enus -->
## TOPIC 00451: NI 5441 Data Processing Mode

- bundle_id: `ni-fgen`
- source_path: `ni-5441-data-processing-mode.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5441-data-processing-mode.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Data Processing mode determines whether the OSP block uses only the I signal path to generate waveforms or uses the I and Q signal paths to generate complex waveforms. If the waveform data is configured for real data points by setting the Data Processing Mode property or the NIFGEN_ATTR_OSP_DATA_PRO

### NI 5441 Data Processing Mode

Data Processing mode determines whether the OSP
block uses only the I signal path to generate waveforms or uses the
I and Q signal paths to generate complex waveforms. If the waveform data is configured for real data points by setting the 
Data
Processing Mode property or the 
NIFGEN_ATTR_OSP_DATA_PROCESSING_MODE attribute, only the I
signal path is used. If the Data Processing Mode property is set to
Complex or the 
NIFGEN_ATTR_OSP_DATA_PROCESSING_MODE
attribute is set to 
NIFGEN_VAL_OSP_COMPLEX, both the I
and Q signal paths are used. Complex waveform data should be
downloaded to the signal generator using the 
niFgen
Write Waveform Complex VI or the 
niFgen_WriteWaveformComplexF64 function.

Parent topic:

NI 5441 Basic Onboard Signal Processing Properties

<!--NI_TOPIC bundle=ni-fgen path=ni-5441-dc-offset.html language=enus -->
## TOPIC 00452: NI 5441 DC Offset

- bundle_id: `ni-fgen`
- source_path: `ni-5441-dc-offset.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5441-dc-offset.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5441 supports a DC offset before the attenuation chain that affects the maximum value of DC offset for a given gain setting. This preattenuation architecture requires two rules for setting the DC offset: The magnitude of the maximum value of offset can be no more than ½ of the configured gain

### NI 5441 DC Offset

The NI 5441 supports a DC offset before the attenuation chain that affects the maximum value of DC offset for a given gain setting. This preattenuation architecture requires two rules for setting the DC offset:

1. The magnitude of the maximum value of offset can be no more than ½ of the configured gain setting for the NI 5441.
2. The waveform maximum plus the offset must not exceed 
 ±6 V into 50 Ω; if it does, the waveform is clipped. For example, if you have set a gain of 
 5, which corresponds to an amplitude of 
 5 V pk , and the waveform is a sine wave using the full range of the DAC, the maximum DC offset you can apply without clipping the sine wave is 
 ±1 V. At this point, output voltages of the sine waveform have reached the maximum amplitude that the device supports. If you increase the DC offset further, the top portion of the waveform at 
 6 V is clipped.

NI-FGEN automatically calculates the preattenuation
offset value based on the set DC offset and gain values. The DC offset can be changed at any time during waveform generation by calling the 
Arbitrary Waveform Offset property or the 
NIFGEN_ATTR_ARB_OFFSET attribute.

The DC offset cannot be set if you selected the
Direct path. The Direct path offset is near zero. Refer to the 
*device
specifications* for information about the maximum value of the
DC offset.

Parent topic:

NI 5441 Waveform Amplitude Control

<!--NI_TOPIC bundle=ni-fgen path=ni-5441-digital-data-control-connector.html language=enus -->
## TOPIC 00453: NI 5441 DIGITAL DATA & CONTROL Connector

- bundle_id: `ni-fgen`
- source_path: `ni-5441-digital-data-control-connector.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5441-digital-data-control-connector.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The DIGITAL DATA & CONTROL (DDC) front panel connector is a 68-pin female VHDCI connector that contains the 16-bit LVDS digital pattern output. The DDC connector is an optional feature for the NI 5441. DIGITAL DATA & CONTROL Pin Assignments The following figure shows the NI 5441 DDC 68-pin connector

### NI 5441 DIGITAL DATA & CONTROL Connector

The DIGITAL DATA & CONTROL (DDC) front panel
connector is a 68-pin female VHDCI connector that contains the
16-bit LVDS digital pattern output. The DDC connector is an
optional feature for the NI 5441.

#### DIGITAL DATA & CONTROL Pin
Assignments

The following figure shows the
NI 5441 DDC 68-pin connector.

[IMAGE alt='image' src='GUID-73285A03-5DAA-4DED-BC9D-A39AD44D354A-a5.gif']

The following table lists the pin names and signal
descriptions used for the NI 5441 DDC connector. All
lines are at standard 
*LVDS* levels.

| Signal Name | Type | Description |
| --- | --- | --- |
| D<0..15> | Output | Digital pattern outputs–The 16-bit digital representation of the analog waveform is available on these output pins as digital pattern outputs. This data is available directly from the memory after several Sample clock pipeline delays. The digital pattern outputs are standard LVDS output levels. All data bits change on the falling edge of the DDC CLK OUT. |
| DDC CLK IN | Input | Digital Data Clock In–These lines are used as a source for an external Sample clock. You can feed a LVDS level clock to this line with a maximum frequency of the signal generator. |
| DDC CLK OUT | Output | Digital Data Clock Out–The Sample clock is always routed to the DDC CLK OUT line of the DDC front panel connector when the digital pattern is enabled. |
| Ground | – | Digital ground |
| PFI<2..3> (Inputs) | Input | PFI<2:3>–These PFI lines can accept a trigger from an external source that can start or step through waveform generation. You can select this functionality on the NI 5441 through the software. Refer to Trigger Sources for more information. |
| PFI<4:5> | Output | PFI<4..5>–These PFI lines can route out a signal from Marker events or the Out Start trigger. |
| Reserved | – | Reserved for future use. Do not connect signals to this line. |
| Refer to the device specifications for information about acceptable input signal characteristics to connect to the DDC lines, as well as the output signal characteristics. |  |  |

You must enable the DDC connector before the
signals in this table are available for use. You can enable digital patterning by calling the
niFgen
Configure Digital Patterning VI or the 
niFgen_EnableDigitalPatterning and 
niFgen_DisableDigitalPatterning functions.

Parent topic:

NI 5441 Front Panel

Related concepts:

- NI 5441 Low-Voltage Differential Signaling (LVDS)
- NI 5441 Trigger Sources

<!--NI_TOPIC bundle=ni-fgen path=ni-5441-digital-filter.html language=enus -->
## TOPIC 00454: NI 5441 Digital Filter

- bundle_id: `ni-fgen`
- source_path: `ni-5441-digital-filter.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5441-digital-filter.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The main DAC provides an internal digital filter. When digital filtering is enabled, the main DAC runs at a faster rate, referred to as the effective sample rate (ESR). The waveform data transfers to the main DAC at the configured Sample clock rate; the internal digital filter interpolates by a fact

### NI 5441 Digital Filter

The main DAC provides an internal digital filter.
When digital filtering is enabled, the main DAC runs at a faster
rate, referred to as the effective sample rate (ESR). The waveform
data transfers to the main DAC at the configured Sample clock rate;
the internal digital filter interpolates by a factor of 2x, 4x, or
8x; and the DAC generates the data at the ESR.

Effective sample rate is calculated with the
following formula:

ESR = 
I<sub>fac</sub>
 × 
SR

where

ESR = the Effective Sample Rate (MS/s)

I<sub>fac</sub>
 = the interpolation factor

SR = configured Sample Clock Rate (MS/s)

Note

onboard signal processing block

NIFGEN_ATTR_ARB_SAMPLE_RATE

I/Q Rate

| Recommended Interpolation Settings |  |
| --- | --- |
| Sample Clock Rate (MS/s) | Interpolation |
| 12.5 to 105 | 2x |
| 10 to 100 | 4x |
| 10 to 50 | 8x |

Note

The delay from the Start trigger to the analog
output increases if the digital filter is enabled. The delay
increases with an increase in the interpolation factor. Refer to
the 
*device
specifications* for information about the delay from the trigger
to the analog output based on the configured filter settings.

niFgen_EnableDigitalFilter

niFgen_DisableDigitalFilter

Note

#### Related Topics

*Filtering and
Interpolation*

*Aliased Images*

Parent topic:

NI 5441 Filtering Effects

Related concepts:

- NI 5441 Onboard Signal Processing (OSP)
- NI 5441 IQ Rate
- Filtering and Interpolation
- Aliased Images

<!--NI_TOPIC bundle=ni-fgen path=ni-5441-digital-gain.html language=enus -->
## TOPIC 00455: NI 5441 Digital Gain

- bundle_id: `ni-fgen`
- source_path: `ni-5441-digital-gain.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5441-digital-gain.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Digital gain multiplies waveform data by a factor you specify in the Digital Gain property or the NIFGEN_ATTR_DIGITAL_GAIN attribute before converting the data to an analog signal in the DAC. Digital gain can be changed during generation without the glitches caused by switching that are common when

### NI 5441 Digital Gain

Digital gain multiplies waveform data by a factor
you specify in the 
Digital Gain
property or the 
NIFGEN_ATTR_DIGITAL_GAIN attribute before converting the data to an analog signal in
the DAC. Digital gain can be changed during generation without the
glitches caused by switching that are common when changing
analog gains. However, the output resolution of the DAC is a
function of digital gain, meaning that only analog gain makes full use of the
resolution of the DAC.

Parent topic:

NI 5441 Waveform Amplitude Control

<!--NI_TOPIC bundle=ni-fgen path=ni-5441-direct-dma.html language=enus -->
## TOPIC 00456: NI 5441 Direct DMA

- bundle_id: `ni-fgen`
- source_path: `ni-5441-direct-dma.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5441-direct-dma.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Direct DMA can transfer waveform data to the signal generator onboard memory at rates well beyond the typical 5 to 30 MB/s range in a standard PC-based architecture. To achieve such high rates, direct DMA establishes a direct connection between the signal generator onboard memory and a specialized w

### NI 5441 Direct DMA

*Direct DMA* can transfer waveform data to the signal generator onboard memory at rates well beyond the typical 5 to 30 MB/s range in a standard PC-based architecture. To achieve such high rates, direct DMA establishes a direct connection between the signal generator onboard memory and a specialized waveform data source. Direct DMA is commonly used to *stream* waveform data from disk at data rates of 100+ MB/sec. Conduant's StreamStor™ products are one example of direct DMA-compatible data sources.

#### Related Topics

*Configuring an Application for Direct DMA*

*DMA Fundamentals*

Parent topic:

NI 5441 Streaming

Related concepts:

- Direct DMA
- Streaming
- Configuring Your Application for Direct DMA

<!--NI_TOPIC bundle=ni-fgen path=ni-5441-events.html language=enus -->
## TOPIC 00457: NI 5441 Events

- bundle_id: `ni-fgen`
- source_path: `ni-5441-events.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5441-events.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use events to indicate when a specific hardware condition has been met on the NI 5441. An event is a signal generated by the NI device at a device state. The NI 5441 supports Ready for Start, Started, Data Marker, Marker, and Done events. The NI 5441 also supports the use of event delays. Re

### NI 5441 Events

You can use *events* to indicate when a specific
hardware condition has been met on the NI 5441. An event is a
signal generated by the NI device at a device state. The NI 5441
supports Ready for Start, Started, *Data Marker*, *Marker*, and Done
events. The NI 5441 also supports the use of *event delays*.

#### Related Topics

*Creating a Marker
Event*

*Creating a Data Marker
Event*

Parent topic:

NI 5441 NI 5441 Overview

Related concepts:

- Events
- Data Marker Events
- Marker Events
- Event Delays
- Creating a Marker Event
- Creating a Data Marker Event

<!--NI_TOPIC bundle=ni-fgen path=ni-5441-exporting-clocks.html language=enus -->
## TOPIC 00458: NI 5441 Exporting Clocks

- bundle_id: `ni-fgen`
- source_path: `ni-5441-exporting-clocks.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5441-exporting-clocks.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5441 provides resources for exporting your clocks and multiple destinations for routing. The following table shows the available clock signals that can be routed to devices external to the signal generator and the destination options. Clock to be Exported Destination Options Sample Clock PFI

### NI 5441 Exporting Clocks

The NI 5441 provides resources for exporting your clocks and multiple destinations for
routing.

[IMAGE alt='image' src='GUID-83FF9972-7F6E-4301-B879-BF4E8D5189AD-a5.gif']

The following table shows the available clock
signals that can be routed to devices external to the
signal generator and the destination options.

| Clock to be Exported | Destination Options |
| --- | --- |
| Sample Clock | PFI <0..1> SMB connector |
| PXI_Trig<0..6>, RTSI<0..6>> |  |
| DDC CLK OUT |  |
| Sample Clock Timebase | PFI <0..1> SMB connector |
| PXI_Trig<0..6>, RTSI<0..6> |  |
| DDC CLK OUT |  |
| Reference Clock | PFI <0..1> SMB connector |
| PXI_Trig<0..6>, RTSI<0..6> |  |

For synchronization purposes, the
NI 5441 allows you to export your clocks 
so that other devices can share the timing of the NI 5441. The following sections describe the possible clock routing configurations.

#### Sample Clock

The Sample clock can be routed to the
PFI <0..1> front panel SMB connectors, PXI_Trig<0..6>
lines on the PXI trigger bus, or the RTSI<0..6> lines.
Additionally, the Sample clock has a direct route to the DDC CLK
OUT line on the DIGITAL DATA & CONTROL connector on the front
panel.

Additionally, the exported clock can be divided
down by an integer value (no less than 2) before being exported to
the PFI<0..1> SMB connectors, PXI_Trig<0..6> lines, or
the RTSI<0..6> lines. Refer to the 
Exported Sample Clock Divisor property or the 
NIFGEN_ATTR_EXPORTED_SAMPLE_CLOCK_DIVISOR attribute for more information about configuring the Sample
clock divisor.

#### Sample Clock Timebase

The Sample clock timebase can be routed to the
PFI <0..1> SMB connectors on the front panel, the
PXI_Trig<0..6> lines on the PXI trigger bus, or the
RTSI<0..6> lines. Additionally, the Sample clock timebase has
a direct route to the DDC CLK OUT line on the DIGITAL DATA &
CONTROL connector on the front panel.

Additionally, the exported clock can be divided
down by an integer value before being exported to the
PFI<0..1> SMB connectors, the PXI_Trig<0..6> lines, or
the RTSI<0..6> lines. You can configure the Sample clock divisor by calling the 
Exported Sample Clock Timebase Divisor property or the 
NIFGEN_ATTR_EXPORTED_SAMPLE_CLOCK_TIMEBASE_DIVISOR attribute.

#### Reference Clock

The Reference clock is the
actual clock that is configured for the signal generator
phase-locked loop circuit to use as a reference. You configure a
Reference clock as a PLL Reference clock source for the signal to
be available for exporting. The Reference clock can be routed to
the PFI<0..1> SMB connectors on the front panel, the
PXI_Trig<0..6> lines on the PXI trigger bus, or the
RTSI<0..6> lines.

Note

#### Destination Options

The following sections define the destinations for
exported clocks.

DDC CLK OUT—You can export the Sample clock
to the DDC CLK OUT line on the optional DIGITAL DATA & CONTROL (DDC)
connector. Exporting the clock from
this connection allows for synchronous clocking of the DDC data.
You must enable the DDC connector before using the Sample clock by calling the 
niFgen
Configure Digital Patterning VI or the 
niFgen_EnableDigitalPatterning and 
niFgen_DisableDigitalPatterning functions.

PFI <0..1>—The Sample clock and the
Reference clock can be exported to the PFI 0 and PFI 1 SMB
connectors on the front panel to synchronize external devices. You
must configure the device to export the desired clock to the PFI
SMB connectors.

Note

PXI_Trig<0..6>—The Sample clock and
the Reference clock can be exported to the PXI_Trig lines or RTSI
lines. The PXI and PCI standards allow for devices to route signals
to other devices in your PXI chassis to enhance device to device
synchronization. Refer to the chassis documentation for
specifications to ensure the reference signal is within tolerance.
You must configure the device to export the desired clock to the
PXI_Trig line or RTSI line. When exporting signals, the following
lines are equivalent:

- PXI_Trig<0..6> = RTSI_<0..6>
- PXI_STAR

Refer to 
niFgen Export
Signal VI or the 
niFgen_ExportSignal function for more information about configuring the
destinations for the desired clock signal.

Parent topic:

NI 5441 Clocking

<!--NI_TOPIC bundle=ni-fgen path=ni-5441-exporting-signals.html language=enus -->
## TOPIC 00459: NI 5441 Exporting Signals

- bundle_id: `ni-fgen`
- source_path: `ni-5441-exporting-signals.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5441-exporting-signals.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The signal generator contains seven PXI trigger lines that are available for sending signal generator-specific information to other devices that have PXI trigger or RTSI bus connectors. The signal generator also connects to the PXI star trigger line, which you can use to send or receive signals to o

### NI 5441 Exporting Signals

Note

ni.com/products

The signal generator has connectors on the front
panel to route signals to devices external to a PXI
chassis. The following table shows the signals available for export
and the lines they can be routed to. To determine all possible
signal routes for your device, refer to 
*Signal Routing*.

|  |  | Destination |  |  |
| --- | --- | --- | --- | --- |
| PXI_Trig<0..6>, or PXI_STAR | PFI 0 and PFI 1 Connectors | PFI<4..5> on DIGITAL DATA & CONTROL Connector |  |  |
| Exported Clocks, Triggers, and Events | Sample Clock | Yes | Yes * | – |
| Sample Clock Timebase | Yes | Yes | – |  |
| PLL Reference Source | Yes | Yes* | – |  |
| Out Start trigger | Yes | Yes | Yes |  |
| Marker Event | Yes | Yes | Yes |  |
| * SYNC OUT/PFI 0 is optimized for the Sample clock and PLL reference source signals and has slightly less jitter than PFI 1. SYNC OUT/PFI 0 is the recommended terminal to use for exporting clocks. |  |  |  |  |

Sample Clock–The clock signal that tells the
DAC when to convert the digital waveform values to an analog
voltage. The Sample clock frequency is referred to as the Sample
clock rate; the rate at which the digital waveforms from device
memory are generated. The Sample clock is also known as update
clock.

Note

Sample Clock Timebase

Note

PLL Reference source–A clock signal that is
only available when a PLL Reference source has been configured. The
clock is the source selected as the PLL Reference Clock source.

Out Start trigger–A signal generated by the
device upon recognizing a start condition that can be routed out
various connectors to signal other devices.

Marker event–A digital signal that can be
used as a trigger corresponding to a specific sample in the
waveform generation. This signal controls other devices that
require timing information related to a specific point in the
generated waveform.

#### Routing Signals

You can route signals in the following ways:

- The Marker event generated during an Arbitrary Waveform
Generation mode waveform generation to any of the PXI trigger
lines, PXI_STAR, or front panel
connectors.
- The signal generator Start trigger output signal to other
devices through any of the PXI trigger lines, PXI_STAR, or front panel connectors.
- The signal generator Sample clock signal to other devices
through any of the PXI trigger lines, PXI_STAR, or front panel connectors.
- The PLL Reference clock source to other devices through any of
the PXI trigger lines, PXI_STAR, or
front panel connectors.

In NI-FGEN, the PXI trigger lines are referred to
as RTSI<0..6>. The correlation between PXI_TRIG<
x> and RTSI<
x> is one to one. You can
configure and route the device internal signals by calling the 
niFgen Export Signal VI
or the 
niFgen_ExportSignal function.

Parent topic:

NI 5441 NI 5441 Overview

Related concepts:

- NI 5441 Signal Routing

<!--NI_TOPIC bundle=ni-fgen path=ni-5441-external-sample-clock.html language=enus -->
## TOPIC 00460: NI 5441 External Sample Clock

- bundle_id: `ni-fgen`
- source_path: `ni-5441-external-sample-clock.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5441-external-sample-clock.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5441 can accept an external clock to directly drive the Sample clock. When using an external Sample clock, the frequency stability and accuracy of the Sample clock is determined by the provided external Sample clock. The following figure shows possible Sample Clock paths. You can set the cloc

### NI 5441 External Sample Clock

The NI 5441 can accept an
external clock to directly drive the Sample clock. When using an
external Sample clock, the frequency stability and accuracy of the
Sample clock is determined by the provided external Sample
clock.

The following figure shows possible Sample
Clock paths.

[IMAGE alt='image' src='GUID-8812ED51-9200-4A44-85CC-727D2EA85B31-a5.gif']

You can set the clock source by calling the
niFgen
Configure Sample Clock Source VI or the 
niFgen_ConfigureSampleClockSource function.

niFgen_ConfigureSampleRate

Note

device specifications

#### External Sample Clock Considerations

The NI 5441 incorporates
high-speed digital clocking technology and requires a stable,
free-running Sample clock to operate properly. When the
signal generator is committed—either explicitly by
calling the 
niFgen Commit VI or
the 
niFgen_Commit function or implicitly by writing waveforms or scripts or
initiating a generation—the external Sample clock must be
available to the device. If the external clock becomes unstable due
to glitching or changing frequency, or is removed entirely, NI-FGEN
returns a hardware clocking error.

Note

Sample Clock
Considerations

If necessary, you can change the rate or the source
of the external Sample clock between generations by
first calling the 
niFgen Abort
Generation VI or the 
niFgen_AbortGeneration function, changing the rate or source, and then calling the
niFgen Commit VI or the 
niFgen_Commit function. NI-FGEN
reprograms the NI 5441 for the new settings,
and you can call the 
niFgen
Initiate Generation VI or the 
niFgen_InitiateGeneration function to start the next generation.

If you must remove the external Sample clock
between generations (after calling the niFgen Abort Generation VI
or 
niFgen_AbortGeneration function, but
before calling the niFgen Initiate VI or the 
niFgen_Init function), but are not
changing the frequency or source of the external clock, you can
choose one of the following options:

- Call the niFgen Initiate VI or the 
 niFgen_Init function, which returns
a hardware clocking error because the external Sample clock is
gone, then clear the error and call the niFgen Initiate VI or the 
 niFgen_Init function
again. NI-FGEN then reprograms the hardware to use the
external clock again.
- Force the device to be recommitted by changing a property or
attribute to another value and then back to its original value.
This action causes NI-FGEN to re-commit the settings to hardware,
which does not happen otherwise because NI-FGEN does not know
that the external Sample clock is gone.

Caution

niFgen_ConfigureSampleRate

Parent topic:

NI 5441 Clocking Options

Related concepts:

- NI 5441 Sample Clock Considerations

<!--NI_TOPIC bundle=ni-fgen path=ni-5441-filtering-effects.html language=enus -->
## TOPIC 00461: NI 5441 Filtering Effects

- bundle_id: `ni-fgen`
- source_path: `ni-5441-filtering-effects.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5441-filtering-effects.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The delay from the time at which the device receives a trigger to the time at which the analog output signal is generated increases if the digital and/or analog filters in the Analog Output path are enabled. In the case of digital filtering, delay also increases with increase in interpolation. Enabl

### NI 5441 Filtering Effects

Analog Output path

onboard signal processing block

Note

Refer to 
*Digital
Filter* for interpolation options. Refer to the 
*device
specifications* for the delay from trigger to analog output
based on different filtering options.

Parent topic:

NI 5441 Analog Output

Related concepts:

- NI 5441 Analog Output
- NI 5441 Onboard Signal Processing (OSP)
- NI 5441 Digital Filter

<!--NI_TOPIC bundle=ni-fgen path=ni-5441-filtering-effects_2.html language=enus -->
## TOPIC 00462: NI 5441 Filtering Effects

- bundle_id: `ni-fgen`
- source_path: `ni-5441-filtering-effects_2.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5441-filtering-effects_2.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The delay from the time at which the device receives a trigger to the time at which the analog output signal is generated increases if the digital and/or analog filters in the Analog Output path are enabled. In the case of digital filtering, delay also increases with increase in interpolation. Enabl

### NI 5441 Filtering Effects

Analog Output path

onboard signal processing block

Note

Refer to 
*Digital
Filter* for interpolation options. Refer to the 
*device
specifications* for the delay from trigger to analog output
based on different filtering options.

Parent topic:

NI 5441 Triggering

<!--NI_TOPIC bundle=ni-fgen path=ni-5441-fir-filter-interpolation.html language=enus -->
## TOPIC 00463: NI 5441 FIR Filter Interpolation

- bundle_id: `ni-fgen`
- source_path: `ni-5441-fir-filter-interpolation.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5441-fir-filter-interpolation.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The FIR filter is an interpolating filter. The interpolation options are 2x, 4x, and 8x. The 2x interpolation option allows some aliasing in the spectrum which can create fairly significant spurs near the FIR output sample rate. The size of these spurs depend on the type of pulse shaping used in the

### NI 5441 FIR Filter Interpolation

The FIR filter is an interpolating filter. The
interpolation options are 2x, 4x, and 8x.

The 2x interpolation option allows some aliasing in
the spectrum which can create fairly significant spurs near the FIR
output sample rate. The size of these spurs depend on the type of
pulse shaping used in the FIR filter.

Parent topic:

NI 5441 FIR Filter

<!--NI_TOPIC bundle=ni-fgen path=ni-5441-fir-filter-overflow.html language=enus -->
## TOPIC 00464: NI 5441 FIR Filter Overflow

- bundle_id: `ni-fgen`
- source_path: `ni-5441-fir-filter-overflow.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5441-fir-filter-overflow.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The FIR filter implementation in the OSP is designed for unity-gain. If the coefficients for the FIR are not scaled correctly, or there are transients in the input waveform to the FIR, then an overflow can occur. If such transients are expected, you should attenuate the data or adjust the prefilter

### NI 5441 FIR Filter Overflow

prefilter gain

prefilter
offset

Tip

NIFGEN_ATTR_OSP_OVERFLOW_ERROR_REPORTING

Parent topic:

NI 5441 FIR Filter

Related concepts:

- NI 5441 Prefilter Gain
- NI 5441 Prefilter Offset

<!--NI_TOPIC bundle=ni-fgen path=ni-5441-fir-filter-type-custom.html language=enus -->
## TOPIC 00465: NI 5441 FIR Filter Type: Custom

- bundle_id: `ni-fgen`
- source_path: `ni-5441-fir-filter-type-custom.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5441-fir-filter-type-custom.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The custom filter lets you define the coefficients of the FIR filter. Custom Coefficients You can define the coefficients for the FIR filter and download them to the signal generator with the niFgen Configure Custom FIR Filter Coefficients VI or the niFgen_ConfigureCustomFIRFilterCoefficients functi

### NI 5441 FIR Filter Type: Custom

The custom filter lets you define the coefficients
of the FIR filter.

#### Custom Coefficients

You can define the coefficients for the FIR filter
and download them to the signal generator with the 
niFgen Configure Custom FIR Filter Coefficients VI or the 
niFgen_ConfigureCustomFIRFilterCoefficients function. Coefficients should be 
scaled correctly and 
compensate for the 
*CIC Filter* roll-off. To use
the coefficients you define, specify a custom filter by setting the Filter
Type property or the 
NIFGEN_ATTR_OSP_FIR_FILTER_TYPE attribute. The NI 5441 has 95 
*symmetrical
coefficients* defined for the FIR filter.

#### FIR Coefficient Scaling

The coefficients should be scaled between -1 and 1.
NI-FGEN quantizes the floating point inputs and downloads them into
the OSP block. The coerced coefficients can be queried with the 
niFgen Get FIR Filter Coefficients VI or the 
niFgen_GetFIRFilterCoefficients function. When scaling the coefficients, consider that the FIR
is architected for unity gain. This means that if a data set of all
full-scale positive values is passed into the FIR and the sum of
the coefficients is equal to 1, then positive full scale is output
from the FIR. In general, the coefficients should be scaled as high
as possible so that the FIR does not overflow the incoming data set
and the coefficients are still within the range of -1 to 1.

#### CIC Compensation in the
FIR

In order to flatten the OSP block in the passband,
the FIR coefficients should compensate for the roll-off in the 
*CIC filter*. The frequency
response (in dB) of the CIC follows the following formula:

[IMAGE alt='image' src='GUID-894C0C14-D219-4CCE-9148-D50CC6A05EA9-a5.gif']

where

R = CIC Interpolation Rate

f = Frequency (fraction of CIC input sample
rate)

The first zero of the CIC filter is always at the
same frequency as the output of the FIR filter. The FIR response
should be peaked the same amount that the CIC rolls off in the
passband of your FIR response. For example, the following diagram
shows the desired response from the FIR with 4x interpolation.

[IMAGE alt='image' src='GUID-7C06492A-8CAF-4F76-BFA7-6C71D1ACDD3E-a5.gif']

But, the CIC has the following response:

[IMAGE alt='image' src='GUID-182783BF-778C-4510-B2EB-941826DB6771-a5.gif']

The CIC compensated FIR response is:

[IMAGE alt='image' src='GUID-834B6ABF-4970-458A-B536-190CFE4FB1F2-a5.gif']

The final response after the FIR (with CIC
compensation) and CIC filters:

[IMAGE alt='image' src='GUID-DC804422-EC87-4612-A012-A1E1684921FF-a5.gif']

Parent topic:

NI 5441 FIR Filter Types

Related concepts:

- NI 5441 CIC Filter
- NI 5441 FIR Filter

<!--NI_TOPIC bundle=ni-fgen path=ni-5441-fir-filter-type-flat.html language=enus -->
## TOPIC 00466: NI 5441 FIR Filter Type: Flat

- bundle_id: `ni-fgen`
- source_path: `ni-5441-fir-filter-type-flat.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5441-fir-filter-type-flat.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Passband Values : 0.1 to 0.4 This lowpass filter is designed to give a flat response until the passband value. The passband value is a fraction of the I/Q Rate coming into the FIR filter. Use the Flat Filter Passband property or the NIFGEN_ATTR_OSP_FIR_FILTER_FLAT_PASSBAND attribute to set the passb

### NI 5441 FIR Filter Type: Flat

Passband Values : 0.1 to 0.4

I/Q Rate

NIFGEN_ATTR_OSP_FIR_FILTER_FLAT_PASSBAND

Caution

I/Q Rate

I/Q Rate

I/Q Rate

The following diagram shows the Flat Filter
response with a passband of 0.4. The frequency axis is scaled as a
fraction of the 
I/Q
Rate.

[IMAGE alt='image' src='GUID-3A885655-0620-4693-B4AC-CCFC6CC59A71-a5.gif']

Parent topic:

NI 5441 FIR Filter Types

Related concepts:

- NI 5441 I/Q Rate Controller

<!--NI_TOPIC bundle=ni-fgen path=ni-5441-fir-filter-type-gaussian.html language=enus -->
## TOPIC 00467: NI 5441 FIR Filter Type: Gaussian

- bundle_id: `ni-fgen`
- source_path: `ni-5441-fir-filter-type-gaussian.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5441-fir-filter-type-gaussian.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: BT Values: 0.1 to 0.9 This low-pass filter is commonly used in communications applications. The Gaussian filter follows the following formula: where f = Frequency (fraction of the I/Q Rate) Use the Gaussian Filter BT property or the NIFGEN_ATTR_OSP_FIR_FILTER_GAUSSIAN_BT attribute to set the BT valu

### NI 5441 FIR Filter Type: Gaussian

BT Values: 0.1 to 0.9

This low-pass filter is commonly used in
communications applications. The Gaussian filter follows the
following formula:

[IMAGE alt='image' src='GUID-54956432-E393-4888-96EE-A0E18A5CD854-a5.gif']

where

f = Frequency (fraction of the I/Q Rate)

Use the 
Gaussian
Filter BT property or the 
NIFGEN_ATTR_OSP_FIR_FILTER_GAUSSIAN_BT attribute to set the BT value.

The following diagram shows an ideal Gaussian
filter response with a BT of 0.3. The frequency axis is scaled as a
fraction of the 
I/Q
Rate.

[IMAGE alt='image' src='GUID-1A20AF5B-5ACC-4B86-A040-986E850A5A55-a5.gif']

Parent topic:

NI 5441 FIR Filter Types

<!--NI_TOPIC bundle=ni-fgen path=ni-5441-fir-filter-type-raised-cosine.html language=enus -->
## TOPIC 00468: NI 5441 FIR Filter Type: Raised Cosine

- bundle_id: `ni-fgen`
- source_path: `ni-5441-fir-filter-type-raised-cosine.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5441-fir-filter-type-raised-cosine.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Alpha Values: 0.1 to 0.9 This lowpass filter is commonly used in communications applications. The passband of the raised cosine filter with the roll-off factor, α, stops at 0.5 × (1 − α) times the I/Q Rate. The stopband of the raised cosine filter begins at 0.5 × (1 + α) times the I/Q Rate. The tran

### NI 5441 FIR Filter Type: Raised Cosine

Alpha Values: 0.1 to 0.9

This lowpass filter is commonly used in
communications applications. The passband of the raised cosine
filter with the roll-off factor, α, stops at 0.5 × (1 − 
α) times the 
*I/Q Rate*. The stopband of the
raised cosine filter begins at 0.5 × (1 + 
α) times the I/Q Rate. The
transition band of the raised cosine filter (in dB) follows the
following formula:

[IMAGE alt='image' src='GUID-2C855ADB-1C58-4913-8A80-F0D24C5AC04C-a5.gif']

where

S is 0.5×(1 − 
α)

f is Frequency (fraction of the I/Q Rate)

Use the 
Raised Cosine Filter Alpha property or the 
NIFGEN_ATTR_OSP_FIR_FILTER_RAISED_COSINE_ALPHA attribute to set the 
α value.

The following diagram shows an ideal raised cosine
filter response with an 
α of 0.5. The frequency
axis is scaled as a fraction of the 
I/Q
Rate.

[IMAGE alt='image' src='GUID-BEF4AF03-7BAB-48EA-B639-084D3ABC103B-a5.gif']

The MER/EVM (measurement of modulation accuracy)
and stopband attenuation improve with a higher 
α.

Parent topic:

NI 5441 FIR Filter Types

Related concepts:

- NI 5441 I/Q Rate Controller

<!--NI_TOPIC bundle=ni-fgen path=ni-5441-fir-filter-type-root-raised-cosine.html language=enus -->
## TOPIC 00469: NI 5441 FIR Filter Type: Root Raised Cosine

- bundle_id: `ni-fgen`
- source_path: `ni-5441-fir-filter-type-root-raised-cosine.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5441-fir-filter-type-root-raised-cosine.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Alpha Values: 0.1 to 0.9 This lowpass filter is commonly used in communications applications. The passband of the root raised cosine filter with the roll-off factor, α, stops at 0.5 × (1 − α) times the I/Q Rate. The stopband of the root raised cosine filter begins at 0.5 × (1 + α) times the I/Q Rate

### NI 5441 FIR Filter Type: Root Raised Cosine

Alpha Values: 0.1 to 0.9

This lowpass filter is commonly used in
communications applications. The passband of the root raised cosine
filter with the roll-off factor, α, stops at 0.5 × (1 − 
α) times the 
*I/Q Rate*. The stopband of the
root raised cosine filter begins at 0.5 × (1 + 
α) times the I/Q Rate. The
transition band of the root raised cosine filter (in dB) follows
the following formula:

[IMAGE alt='image' src='GUID-569A8FBC-A941-4D3B-8BA7-6B9A01D0E5BD-a5.gif']

where

S is 0.5×(1 − 
α)

f is the frequency in Hz as a fraction of the I/Q rate

Use the 
Root Raised Cosine Filter Alpha property or the 
NIFGEN_ATTR_OSP_FIR_FILTER_ROOT_RAISED_COSINE_ALPHA attribute to set the 
α value.

The following diagram shows an ideal root raised
cosine filter response with an 
α of 0.5. The frequency
axis is scaled as a fraction of the 
I/Q
Rate.

[IMAGE alt='image' src='GUID-AAD8865C-5B03-4E67-8E39-2FD2389E6EBA-a5.gif']

The MER/EVM (measurement of modulation accuracy)
and stopband attenuation improve with a higher 
α.

Parent topic:

NI 5441 FIR Filter Types

Related concepts:

- NI 5441 I/Q Rate Controller

<!--NI_TOPIC bundle=ni-fgen path=ni-5441-fir-filter-type.html language=enus -->
## TOPIC 00470: NI 5441 FIR Filter Type

- bundle_id: `ni-fgen`
- source_path: `ni-5441-fir-filter-type.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5441-fir-filter-type.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The FIR Filter type determines the spectral shaping of the data done in the FIR filter. Use the FIR Filter Type property or the NIFGEN_ATTR_OSP_FIR_FILTER_TYPE attribute to set the FIR filter type. The following filter types are supported: Flat Raised Cosine Root Raised Cosine Gaussian Custom

### NI 5441 FIR Filter Type

The FIR Filter type determines the spectral shaping
of the data done in the 
*FIR filter*. Use the 
FIR Filter
Type property or the 
NIFGEN_ATTR_OSP_FIR_FILTER_TYPE attribute to set the FIR filter type. The following filter
types are supported:

- Flat
- Raised
Cosine
- Root
Raised Cosine

- Gaussian
- Custom

Parent topic:

NI 5441 Basic Onboard Signal Processing Properties

Related concepts:

- NI 5441 FIR Filter
- NI 5441 FIR Filter Type: Flat
- NI 5441 FIR Filter Type: Raised Cosine
- NI 5441 FIR Filter Type: Root Raised Cosine
- NI 5441 FIR Filter Type: Gaussian
- NI 5441 FIR Filter Type: Custom

<!--NI_TOPIC bundle=ni-fgen path=ni-5441-fir-filter-types.html language=enus -->
## TOPIC 00471: NI 5441 FIR Filter Types

- bundle_id: `ni-fgen`
- source_path: `ni-5441-fir-filter-types.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5441-fir-filter-types.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: There are a number of built-in low-pass pulse-shaping filters available in NI-FGEN. These filters compensate for the CIC roll-off and handle scaling issues. NI-FGEN calculates the coefficients for each filter which can then be queried with the niFgen Get FIR Filter Coefficients VI or the niFgen_GetF

### NI 5441 FIR Filter Types

There are a number of built-in low-pass pulse-shaping filters
available in NI-FGEN. These filters compensate for the CIC roll-off
and handle scaling issues. NI-FGEN calculates the coefficients for
each filter which can then be queried with the 
niFgen Get FIR Filter Coefficients VI or the 
niFgen_GetFIRFilterCoefficients function.
 NI-FGEN calculates the coefficients for
each filter. Because the coefficients are scaled for unity-gain,
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

Parent topic:

NI 5441 FIR Filter

Related concepts:

- NI 5441 FIR Filter Type
- NI 5441 FIR Filter Type: Flat
- NI 5441 FIR Filter Type: Raised Cosine
- NI 5441 FIR Filter Type: Root Raised Cosine

<!--NI_TOPIC bundle=ni-fgen path=ni-5441-fir-filter.html language=enus -->
## TOPIC 00472: NI 5441 FIR Filter

- bundle_id: `ni-fgen`
- source_path: `ni-5441-fir-filter.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5441-fir-filter.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Finite Impulse Response (FIR) filter shapes the incoming data and compensates for roll-off in the CIC filter. The I and Q FIR filters share the same set of coefficients. These coefficients must be symmetric. The FIR filters can be enabled/disabled by setting FIR Filter Enabled and CIC Filter Ena

### NI 5441 FIR Filter

CIC filter

Note

When using the FIR filter, consider the
following:

- Interpolation
- Overflow
- FIR Filter Types

#### Basic FIR Structure

The following figure shows a diagram of a typical
N-tap FIR filter:

[IMAGE alt='image' src='GUID-974F5936-D380-485F-83BC-C661293EC53A-a5.gif']

The structure of the FIR filter is a long shift
register. Each tap in the shift register is multiplied by an
associated coefficient (c( 
x) in the figure above). The results for all of the taps
are then summed to create the final output of the filter.

#### Symmetric FIR filters

The FIR filters in the OSP block are symmetric.
This means that the first and last taps have the same coefficient,
the second and second to last taps have the same coefficient, and
so on. Because the FIR filter in the OSP has an odd number of taps,
the center tap does not have a matching tap.

Parent topic:

NI 5441 Onboard Signal Processing Components

Related concepts:

- NI 5441 CIC Filter
- NI 5441 FIR Filter Interpolation
- NI 5441 FIR Filter Overflow
- NI 5441 FIR Filter Types

<!--NI_TOPIC bundle=ni-fgen path=ni-5441-frequency-list-mode.html language=enus -->
## TOPIC 00473: NI 5441 Frequency List Mode

- bundle_id: `ni-fgen`
- source_path: `ni-5441-frequency-list-mode.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5441-frequency-list-mode.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Frequency List output mode allows you to configure the device to generate a standard function using a list of frequencies you define. A frequency list is composed of steps, each one with a frequency/duration pair. Frequency lists are commonly used for frequency hops and sweeps and frequency shift ke

### NI 5441 Frequency List Mode

*Frequency List output mode* allows you to configure the
device to generate a standard function using a list of frequencies
you define. A frequency list is composed of steps, each one with a
frequency/duration pair. Frequency lists are commonly used for
*frequency hops and sweeps* and frequency shift keying (FSK) applications.

Parent topic:

NI 5441 Output Modes

Related concepts:

- Frequency List Mode
- Frequency Hopping and Sweeping

<!--NI_TOPIC bundle=ni-fgen path=ni-5441-front-panel.html language=enus -->
## TOPIC 00474: NI 5441 Front Panel

- bundle_id: `ni-fgen`
- source_path: `ni-5441-front-panel.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5441-front-panel.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the NI PXI-5441 front panel. This front panel has four SMB connectors and an optional 68-pin male VHDCI connector. The ACCESS and ACTIVE LEDs indicate the status of the PXI module. The CH 0 SMB connector is the analog output from which arbitrary waveforms are generated. Th

### NI 5441 Front Panel

The following figure shows the NI PXI-5441 front panel. This front panel has
four SMB connectors and an optional 68-pin male VHDCI connector.

[IMAGE alt='image' src='GUID-6B626E9B-25D1-4869-9F28-A5183AB4E27A-a5.gif']

The *ACCESS and ACTIVE LEDs* indicate the status of the PXI module.

The 
*CH 0* SMB connector is the analog
output from which arbitrary waveforms are generated.

The 
*CLK IN* SMB connector provides the
device with an external reference or external Sample clock.

The 
*PFI 0 and PFI 1* SMB
connectors are multi-directional connections for a number of
different signals.

*DIGITAL DATA &
CONTROL* is an optional 68-pin male VHDCI connector that
contains the 16-bit LVDS digital pattern outputs.

Parent topic:

NI 5441 NI 5441 Overview

Related concepts:

- NI 5441 ACCESS and ACTIVE LEDs
- NI 5441 CH 0 Connector
- NI 5441 CLK IN Connector
- NI 5441 PFI Connectors
- NI 5441 DIGITAL DATA & CONTROL Connector

<!--NI_TOPIC bundle=ni-fgen path=ni-5441-hardware-state-diagram.html language=enus -->
## TOPIC 00475: NI 5441 Hardware State Diagram

- bundle_id: `ni-fgen`
- source_path: `ni-5441-hardware-state-diagram.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5441-hardware-state-diagram.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following diagram shows the hardware states of the signal generator. The signal generator can be in one of the following six basic states during the course of operation. Idle—The device is not generating a waveform. All session properties or attributes can be programmed in the Idle state. In the

### NI 5441 Hardware State Diagram

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

NI 5441 Theory of Operation

Related concepts:

- Programming State Model

<!--NI_TOPIC bundle=ni-fgen path=ni-5441-i-q-combiner.html language=enus -->
## TOPIC 00476: NI 5441 I/Q Combiner

- bundle_id: `ni-fgen`
- source_path: `ni-5441-i-q-combiner.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5441-i-q-combiner.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: When the waveform data is configured for complex data points by setting the Data Processing Mode property or the NIFGEN_ATTR_OSP_DATA_PROCESSING_MODE attribute, the I and Q data streams are combined after they are multiplied with the carriers. The I/Q combiner is implemented as I [p] − Q [p]. The co

### NI 5441 I/Q Combiner

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

NI 5441 Onboard Signal Processing Components

Related concepts:

- NI 5441 Quadrature Upconversion

<!--NI_TOPIC bundle=ni-fgen path=ni-5441-i-q-rate-controller.html language=enus -->
## TOPIC 00477: NI 5441 I/Q Rate Controller

- bundle_id: `ni-fgen`
- source_path: `ni-5441-i-q-rate-controller.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5441-i-q-rate-controller.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The I/Q rate component pulls the data from the generation engine such that a new sample is returned once every Total_OSP_Interpolation Sample clocks. Total_OSP_Interpolation is calculated by the following equation: Total_OSP_Interpolation = FIR Interpolation × CIC Interpolation The Total_OSP_Inter

### NI 5441 I/Q Rate Controller

The I/Q rate component pulls the data from the
generation engine such that a new sample is returned once every
Total_OSP_Interpolation Sample clocks. Total_OSP_Interpolation is calculated by the following equation:

Note

Tip

Parent topic:

NI 5441 Onboard Signal Processing Components

<!--NI_TOPIC bundle=ni-fgen path=ni-5441-internal-sample-clock.html language=enus -->
## TOPIC 00478: NI 5441 Internal Sample Clock

- bundle_id: `ni-fgen`
- source_path: `ni-5441-internal-sample-clock.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5441-internal-sample-clock.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5441 can derive a Sample clock from its main internal timing source—the onboard Sample clock timebase. The signal generator provides a high-precision 100 MHz Voltage Controlled Crystal Oscillator (VCXO) clock source for the Sample clock timebase. As shown in the following figure, the Sample c

### NI 5441 Internal Sample Clock

The NI 5441 can derive a Sample
clock from its main internal timing source—the onboard Sample clock
timebase. The signal generator provides a high-precision
100 MHz Voltage Controlled Crystal Oscillator (VCXO) clock
source for the Sample clock timebase. As shown in the following
figure, the Sample clock timebase frequency is tuned by an Internal
Calibration DAC control voltage when the 
Reference
Clock Source property or the 
NIFGEN_ATTR_REFERENCE_CLOCK_SOURCE attribute is set to "None." The Internal Calibration DAC,
which is calibrated at the factory and which you also can
calibrate, provides for the Sample clock Timebase to maintain a
high quality frequency source.

[IMAGE alt='image' src='GUID-3FA29193-B2A4-4322-BE88-52DBA4119C65-a5.gif']

There are two methods, referred to as clock modes,
for creating an internal Sample clock from the Sample clock
timebase: Divide-Down (Divide by N) Sampling and High-Resolution Sampling.

In Divide-Down Sampling mode, the
Divide by 
N circuit uses the Sample clock timebase of 100 MHz
to create the frequency available for use as the Sample clock.
Divide-Down Sampling mode can generate any internal timebase
frequency of 100 MHz/
N, where 
N is any integer from 1 to 4,194,304. For example, the
internal timebase can run at 100 MHz, 50.0 MHz, 33.33
MHz, 25.0 MHz, 20.0 MHz, 16.666 MHz, and so on. The low
frequency limit in Divide-Down Sampling mode is
23.84185 (100 MHz/4,194,304) Hz. Divide-Down Sampling
mode provides a high-quality clock with the lowest jitter.

The High-Resolution Sampling mode also uses the
Sample clock timebase at 100 MHz to generate a frequency from
10 Hz to 100 MHz. In addition, the High-Resolution mode
uses direct digital synthesis to generate very fine resolution
increments on the order of microhertz. Refer to the 
*device
specifications* for more information about jitter.

Note

device
specifications

Parent topic:

NI 5441 Clocking Options

<!--NI_TOPIC bundle=ni-fgen path=ni-5441-iq-rate.html language=enus -->
## TOPIC 00479: NI 5441 IQ Rate

- bundle_id: `ni-fgen`
- source_path: `ni-5441-iq-rate.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5441-iq-rate.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The IQ Rate property or the NIFGEN_ATTR_OSP_IQ_RATE attribute defines the rate at which data is processed by the OSP block. If the waveform data is configured for real data points by setting the Data Processing Mode property or the NIFGEN_ATTR_OSP_DATA_PROCESSING_MODE attribute, then it is the rate

### NI 5441 IQ Rate

The IQ Rate
property or the 
NIFGEN_ATTR_OSP_IQ_RATE attribute defines the rate at which data is processed
by the OSP block. If the waveform data is configured for real data points by setting the 
Data
Processing Mode property or the 
NIFGEN_ATTR_OSP_DATA_PROCESSING_MODE attribute, then it is the
rate at which each sample from waveform memory is taken from memory
and inserted into the OSP block. If the waveform data is configured for complex data points by setting the Data Processing Mode
property or the 
NIFGEN_ATTR_OSP_DATA_PROCESSING_MODE
attribute, then it is
the rate at which each complex sample is taken from memory and
inserted into the OSP block.

The actual 
sample
rate is calculated by NI-FGEN based on the I/Q Rate. NI-FGEN
calculates the 
FIR
Interpolation Factor and 
CIC
Interpolation Factor properties or the 
NIFGEN_ATTR_OSP_FIR_FILTER_INTERPOLATION and 
NIFGEN_ATTR_OSP_CIC_FILTER_INTERPOLATION attributes unless you set them. The following formula
describes the relationship between the I/Q rate, FIR interpolation
rate, CIC interpolation rate, and sample rate:

Note

NIFGEN_ATTR_OSP_ENABLED

NIFGEN_ATTR_ARB_SAMPLE_RATE

Parent topic:

NI 5441 Basic Onboard Signal Processing Properties

<!--NI_TOPIC bundle=ni-fgen path=ni-5441-low-voltage-differential-signaling-lv.html language=enus -->
## TOPIC 00480: NI 5441 Low-Voltage Differential Signaling (LVDS)

- bundle_id: `ni-fgen`
- source_path: `ni-5441-low-voltage-differential-signaling-lv.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5441-low-voltage-differential-signaling-lv.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Low-voltage differential signaling (LVDS) is a low-noise, low-power, low-amplitude method for high-speed digital data transfer. The following figure shows a diagram of a typical LVDS circuit. As you can see in the previous figure, a current source at the driver provides approximately 3.5 mA of curre

### NI 5441 Low-Voltage Differential Signaling (LVDS)

Low-voltage differential signaling (LVDS) is a
low-noise, low-power, low-amplitude method for high-speed digital
data transfer.

The following figure shows a diagram of a typical
LVDS circuit.

[IMAGE alt='image' src='GUID-33D1EFAE-90F1-4A1C-8B90-A6B07019D4EA-a5.gif']

As you can see in the previous figure, a current
source at the driver provides approximately 3.5 mA of current.
The direction of the current across the transmission line depends
on whether the driver drives a logic high level or low level. When
the current reaches the receiver, a 100 Ω terminating
resistor connects the two ends of the differential transmission
line to provide a return path for the current. In addition, a
voltage of approximately 350 mV is established across the two
input terminals of the receiver. The differential voltage at the
receiver is either positive or negative, depending on the direction
of the current. The receiver recognizes a positive voltage signal
as a logic high level (1) and a negative voltage as a logic low
level (0).

The electrical characteristics of an LVDS signal
offers some performance improvements compared to single-ended
standards. For example, since the received voltage is a
differential between two signals, the voltage difference between
the logic high level and low level state can be smaller, allowing
for faster rise and fall times. Also, the differential transmission
scheme is less susceptible to common-mode noise than single-ended
transmission methods.

Note

Electrical Characteristics of Low-Voltage Differential
Signaling (LVDS) Interface Circuits

Parent topic:

NI 5441 DIGITAL DATA & CONTROL Connector

<!--NI_TOPIC bundle=ni-fgen path=ni-5441-memory-fragmentation.html language=enus -->
## TOPIC 00481: NI 5441 Memory Fragmentation

- bundle_id: `ni-fgen`
- source_path: `ni-5441-memory-fragmentation.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5441-memory-fragmentation.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: When storing multiple waveforms in NI 5441 memory, fragmentation can become a problem. Both waveforms and instructions are stored in NI 5441 memory in contiguous blocks. These blocks are allocated in multiples of 128 bytes, and they are written in the order that you configure them. Fragmentation occ

### NI 5441 Memory Fragmentation

When storing multiple waveforms in
NI 5441 memory, fragmentation can become a
problem. Both waveforms and instructions are stored in
NI 5441 memory in contiguous blocks. These
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

NI 5441 Onboard Memory

<!--NI_TOPIC bundle=ni-fgen path=ni-5441-ni-5441-overview.html language=enus -->
## TOPIC 00482: NI 5441 NI 5441 Overview

- bundle_id: `ni-fgen`
- source_path: `ni-5441-ni-5441-overview.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5441-ni-5441-overview.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5441 is a 100 MS/s, 16-bit arbitrary waveform generator with the following features: Onboard signal processing (OSP) One 16-bit resolution output channel Output amplitude up to 12 V [pk-pk] into a 50 Ω load Offset up to ±25% of V [pk-pk] Up to 43 MHz sine output Up to 25 MHz square Up to 5 MH

### NI 5441 NI 5441 Overview

The NI 5441 is a 100 MS/s, 16-bit arbitrary
waveform generator with the following features:

- Onboard signal processing (OSP)
- One 16-bit resolution output channel
- Output amplitude up to 12 V 
 pk-pk into a 50 Ω load
- Offset up to ±25% of V 
 pk-pk
- Up to 43 MHz sine output
- Up to 25 MHz square
- Up to 5 MHz triangle, ramp-up, and ramp-down
- Software-selectable output impedances (50 Ω or
75 Ω) and output attenuation levels from 0 dB to
51 dB
- High-Resolution, Divide by 
 N , and external clocking
- PLL synchronization to external clocks or to
PXI_CLK10
- TClk synchronization
- Sampling rate up to 100 MS/s (105 MHz with external
clock)
- Up to 512 MB of onboard waveform memory
- Waveform linking and looping for arbitrary waveform
generation
- Digital and analog filters
- Digital gain
- Four external trigger inputs
- 4 Marker events as trigger output
- 16-bit digital pattern generation with clock and LVDS
output
- PXI trigger lines

All NI 5441 devices follow industry-standard
Plug and Play specifications for the PXI bus, and offer seamless
integration with compliant systems.

Parent topic:

Devices

Related concepts:

- NI 5441 Onboard Signal Processing (OSP)

<!--NI_TOPIC bundle=ni-fgen path=ni-5441-numerically-controlled-oscillator-nco.html language=enus -->
## TOPIC 00483: NI 5441 Numerically Controlled Oscillator (NCO)

- bundle_id: `ni-fgen`
- source_path: `ni-5441-numerically-controlled-oscillator-nco.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5441-numerically-controlled-oscillator-nco.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The numerically controlled oscillator (NCO) is a digital circuit that creates two cosine waves of the same frequency with two potentially independent phases. You can use the Carrier Frequency property or the NIFGEN_ATTR_OSP_CARRIER_FREQUENCY attribute to set the carrier frequency. The I phase cosine

### NI 5441 Numerically Controlled Oscillator (NCO)

The numerically controlled oscillator (NCO) is a
digital circuit that creates two cosine waves of the same frequency
with two potentially independent phases. 
You can use the 
Carrier
Frequency property or the 
NIFGEN_ATTR_OSP_CARRIER_FREQUENCY attribute to set the carrier frequency. The I phase cosine
waveform is multiplied by the I signal path, and the Q phase cosine
waveform is multiplied by the Q data path. The I and Q phases are
programmable from -180° to 180° by setting the 
Carrier
Phase I and 
Carrier
Phase Q properties or the 
NIFGEN_ATTR_OSP_CARRIER_PHASE_I and 
NIFGEN_ATTR_OSP_CARRIER_PHASE_Q attributes. The Carrier Phase Q property or the 
NIFGEN_ATTR_OSP_CARRIER_PHASE_Q only
applies when the waveform data is configured for complex data points by setting the 
Data
Processing Mode property or the 
NIFGEN_ATTR_OSP_DATA_PROCESSING_MODE attribute. Both the
frequency and the phases can be updated during generation. For 
*quadrature
upconversion*, set the I phase to 0° and Q phase to -90°. The
Carrier Phase I/Q properties and attributes can be used to simulate
quadrature skew impairments. Change the I or Q Carrier Phase by the
required quadrature skew to simulate this impairment.

Parent topic:

NI 5441 Onboard Signal Processing Components

Related concepts:

- NI 5441 Quadrature Upconversion

<!--NI_TOPIC bundle=ni-fgen path=ni-5441-onboard-memory.html language=enus -->
## TOPIC 00484: NI 5441 Onboard Memory

- bundle_id: `ni-fgen`
- source_path: `ni-5441-onboard-memory.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5441-onboard-memory.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5441 signal generator uses an onboard memory that is 16-bits wide. The minimum standard memory size for the NI 5441 is 8 MB which translates to 8,338,608 usable bytes. With the minimum standard memory size, you can store very long waveforms on the device and obtain reliable waveform generatio

### NI 5441 Onboard Memory

The NI 5441 signal generator
uses an onboard memory that is 16-bits wide. The minimum standard
memory size for the NI 5441 is 8 MB
which translates to 8,338,608 usable bytes. With the minimum
standard memory size, you can store very long waveforms on the
device and obtain reliable waveform generation at full sample rate
of 100 MS/s. The
NI 5441 is also available with higher memory options
of 32 MB, 256 MB, and 512 MB.

The onboard memory is a single large memory area that stores both waveforms and sequence instructions to generate
the waveforms. The instructions for a complicated sequence can
occupy a significant portion of memory. The architecture of the
NI 5441 allows you to load multiple
waveforms and multiple sequence instructions into the memory. The
following diagram illustrates NI 5441
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

Parent topic:

NI 5441 Theory of Operation

<!--NI_TOPIC bundle=ni-fgen path=ni-5441-onboard-signal-processing-components.html language=enus -->
## TOPIC 00485: NI 5441 Onboard Signal Processing Components

- bundle_id: `ni-fgen`
- source_path: `ni-5441-onboard-signal-processing-components.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5441-onboard-signal-processing-components.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the block diagram of the OSP block. The OSP block includes the following components: Prefilter Gain and Prefilter Offset I/Q Rate Controller FIR (Frequency Impulse Response) CIC (Cascaded Integrator Comb) NCO (Numerically Controlled Oscillator) I/Q Combiner

### NI 5441 Onboard Signal Processing Components

The following figure shows the block diagram of the
OSP block.

[IMAGE alt='image' src='GUID-E225C2F0-CE2B-428A-A492-7D0979255359-a5.gif']

The OSP block includes the following
components:

- Prefilter Gain and
Prefilter Offset

- I/Q Rate Controller
- FIR (Frequency Impulse
Response)
- CIC (Cascaded Integrator
Comb)

- NCO (Numerically Controlled
Oscillator)
- I/Q Combiner

Parent topic:

NI 5441 Onboard Signal Processing (OSP)

Related concepts:

- NI 5441 Prefilter Gain and Offset
- NI 5441 I/Q Rate Controller
- NI 5441 FIR Filter
- NI 5441 CIC Filter
- NI 5441 Numerically Controlled Oscillator (NCO)
- NI 5441 I/Q Combiner

<!--NI_TOPIC bundle=ni-fgen path=ni-5441-onboard-signal-processing-osp.html language=enus -->
## TOPIC 00486: NI 5441 Onboard Signal Processing (OSP)

- bundle_id: `ni-fgen`
- source_path: `ni-5441-onboard-signal-processing-osp.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5441-onboard-signal-processing-osp.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The onboard signal processing (OSP) block is a general-purpose block of digital signal processing components that can be used to modify the data pulled from waveform memory during generation. The OSP block can be used for the following common applications: Arbitrary Waveform Generation Single-Tone G

### NI 5441 Onboard Signal Processing (OSP)

The onboard signal processing (OSP) block is a
general-purpose block of digital signal processing components that
can be used to modify the data pulled from waveform memory during
generation.

The OSP block can be used for the following common applications:

- Arbitrary Waveform
Generation
- Single-Tone Generation
- Quadrature
Upconversion
- Quadrature
Upconversion with Signal Impairments
- Amplitude Modulation
(AM)
- Baseband
Interpolation

Parent topic:

NI 5441 Theory of Operation

Related concepts:

- NI 5441 Arbitrary Waveform Generation
- NI 5441 Single-Tone
- NI 5441 Quadrature Upconversion
- NI 5441 Amplitude Modulation (AM) or Double Sideband
- NI 5441 Baseband Interpolation

<!--NI_TOPIC bundle=ni-fgen path=ni-5441-osp-enabled.html language=enus -->
## TOPIC 00487: NI 5441 OSP Enabled

- bundle_id: `ni-fgen`
- source_path: `ni-5441-osp-enabled.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5441-osp-enabled.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The OSP Enabled property or the NIFGEN_ATTR_OSP_ENABLED attribute activates the functionality of the OSP block. To use any of the features in the OSP block, you must enable onboard signal processing by setting this property or attribute.

### NI 5441 OSP Enabled

The 
OSP
Enabled property or the 
NIFGEN_ATTR_OSP_ENABLED attribute activates the functionality of the OSP block. To use
any of the features in the OSP block, you must enable onboard
signal processing by setting this property or attribute.

Parent topic:

NI 5441 Basic Onboard Signal Processing Properties

<!--NI_TOPIC bundle=ni-fgen path=ni-5441-output-enable.html language=enus -->
## TOPIC 00488: NI 5441 Output Enable

- bundle_id: `ni-fgen`
- source_path: `ni-5441-output-enable.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5441-output-enable.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can disable the analog output signal at the CH 0 connector by controlling the output enable relay, as shown in the following figure. When the output enable relay is disabled, the output signal is connected to ground through a 50 or 75 Ω resistance depending on the output impedance selected. The

### NI 5441 Output Enable

You can disable the analog output signal at the CH
0 connector by controlling the output enable relay, as shown in the
following figure.

[IMAGE alt='image' src='GUID-BFAEDBE6-696A-4B0B-9A41-C8FD2A49A5A8-a5.gif']

When the output enable relay is disabled, the
output signal is connected to ground through a 50 or
75 Ω resistance depending on the output impedance
selected. The output enable relay is enabled for normal waveform
generation, connecting the CH 0 SMB connector to the 
*Analog Output path*. You
can change the output enable state at any time during waveform
generation, and the generation continues on internally.

niFgen_ConfigureOutputEnabled

Note

Parent topic:

NI 5441 Analog Output

Related concepts:

- NI 5441 Analog Output

<!--NI_TOPIC bundle=ni-fgen path=ni-5441-output-impedance.html language=enus -->
## TOPIC 00489: NI 5441 Output Impedance

- bundle_id: `ni-fgen`
- source_path: `ni-5441-output-impedance.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5441-output-impedance.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5441 Analog Output path is designed to have an output impedance of 50 Ω from the Output Enable relay looking back towards the Main DAC. There is a selectable 25 Ω resistance that can be switched into the Analog Output path between the Output Enable relay and the CH 0 connector for application

### NI 5441 Output Impedance

The NI 5441 Analog Output path is
designed to have an output impedance of 50 Ω from the
*Output Enable relay* looking back towards the Main DAC. There is a
selectable 25 Ω resistance that can be switched into the
Analog Output path between the Output Enable relay and the CH
0 connector for applications requiring a 75 Ω
impedance. Most applications use a load impedance of
50 Ω, but applications such as video testing, require
75 Ω. Refer to the following figure.

[IMAGE alt='image' src='GUID-1168A294-D930-4645-8DF7-E4E6E841D015-a5.gif']

If the load impedance is a high impedance (~1
MΩ), you may see output levels up to twice the selected
output value for a matched input/output impedance. These levels can
be as high as 24 V<sub>pk-pk</sub> for the High-Gain Amplifier path. Normally, the
output levels increase as the load impedance increases. The
NI 5441 can compensate for different load impedance
values. Refer to 
*CH 0 Connector* for more
information.

niFgen_ConfigureOutputImpedance

Note

Parent topic:

NI 5441 Analog Output

Related concepts:

- NI 5441 Output Enable
- NI 5441 CH 0 Connector

<!--NI_TOPIC bundle=ni-fgen path=ni-5441-output-modes.html language=enus -->
## TOPIC 00490: NI 5441 Output Modes

- bundle_id: `ni-fgen`
- source_path: `ni-5441-output-modes.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5441-output-modes.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The output mode of your signal generator determines the type of waveforms your signal generator produces. To select an output mode, set the Output Mode parameter of the niFgen Configure Output Mode VI or the niFgen_ConfigureOutputMode function.

### NI 5441 Output Modes

The output mode of your signal generator determines the type of
waveforms your signal generator produces. To select an output mode,
set the 
Output Mode parameter of the 
niFgen
Configure Output Mode VI or the 
niFgen_ConfigureOutputMode function.

Parent topic:

NI 5441 Waveform Generation

<!--NI_TOPIC bundle=ni-fgen path=ni-5441-pfi-connectors.html language=enus -->
## TOPIC 00491: NI 5441 PFI Connectors

- bundle_id: `ni-fgen`
- source_path: `ni-5441-pfi-connectors.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5441-pfi-connectors.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: PFI 0 and PFI 1 are bidirectional connectors. As an input, the PFI terminals can accept a trigger from an external source that can start or step through waveform generation. As an output, the PFI lines route a signal out from the following sources: Marker events Start trigger PLL Reference clock sou

### NI 5441 PFI Connectors

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

device specifications

Note

Parent topic:

NI 5441 Front Panel

<!--NI_TOPIC bundle=ni-fgen path=ni-5441-phase-locked-loop-reference-clock.html language=enus -->
## TOPIC 00492: NI 5441 Phase-Locked Loop Reference Clock

- bundle_id: `ni-fgen`
- source_path: `ni-5441-phase-locked-loop-reference-clock.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5441-phase-locked-loop-reference-clock.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: A phase-locked loop (PLL) is a circuit that tunes the Sample clock timebase to phase–lock to an external Reference clock. The PLL Reference clock source controls the source of the control voltage that tunes the VCXO of the Sample clock timebase for internal clock update sources. The frequency stabil

### NI 5441 Phase-Locked Loop Reference Clock

Note

device
specifications

The following figure shows the NI 5441 Reference Clock Source path.

[IMAGE alt='image' src='GUID-928A3C7A-05C9-46C0-86CE-DCD9AFB72E85-a5.gif']

Note

NIFGEN_ATTR_REFERENCE_CLOCK_SOURCE

#### Reference Clock Sources

The NI 5441 can
phase-lock its Sample clock timebase to an external signal
that is present on the CLK IN front panel connector. PXI devices
can also phase–lock to a 10 MHz Reference clock signal
provided by the PXI bus (PXI_CLK10).

Refer to the table in 
*Clocking Options*,
for the valid NI-FGEN property value combinations that can be used
to configure the NI 5441 clock settings
for an external Reference clock.

Note

device 
specifications

Related Topics

Configuring a Reference
Clock

Parent topic:

NI 5441 Clocking Options

Related concepts:

- NI 5441 Clocking Options
- Configuring a Reference Clock

<!--NI_TOPIC bundle=ni-fgen path=ni-5441-postamplifier-attenuation.html language=enus -->
## TOPIC 00493: NI 5441 Postamplifier Attenuation

- bundle_id: `ni-fgen`
- source_path: `ni-5441-postamplifier-attenuation.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5441-postamplifier-attenuation.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The postamplifier attenuation section is after the High-Gain and Low-Gain Amplifiers in the analog path. The attenuators provide a range of attenuation from 0 dB to a maximum of 36 dB in steps of 12 dB. NI-FGEN automatically controls the value of attenuation set in the postamplifier attenuation sect

### NI 5441 Postamplifier Attenuation

The postamplifier attenuation section is after the
High-Gain and Low-Gain Amplifiers in the *analog path*. The attenuators provide a
range of attenuation from 0 dB to a maximum of 36 dB in steps
of 12 dB. NI-FGEN automatically controls the value of attenuation
set in the postamplifier attenuation section dependent on the set
gain. You can read the value NI-FGEN has selected for postamplifier
attenuation using the 
Post-Amplifier Attenuation property or the 
NIFGEN_ATTR_POST_AMPLIFIER_ATTENUATION attribute.

Parent topic:

NI 5441 Attenuation

Related concepts:

- NI 5441 Analog Output

<!--NI_TOPIC bundle=ni-fgen path=ni-5441-power-up-and-reset-conditions.html language=enus -->
## TOPIC 00494: NI 5441 Power-Up and Reset Conditions

- bundle_id: `ni-fgen`
- source_path: `ni-5441-power-up-and-reset-conditions.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5441-power-up-and-reset-conditions.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The signal generator is in the following state from the time at which the computer begins to power up until the operating system is fully booted and NI-FGEN is loaded. The CH 0 analog output connector is disabled and has 50 Ω or 75 Ω impedance to ground. This impedance is the same as its previous se

### NI 5441 Power-Up and Reset Conditions

The signal generator is in the following state from
the time at which the computer begins to power up until the operating system is
fully booted and NI-FGEN is loaded.

- The CH 0 analog output connector is disabled and has
50 Ω or 75 Ω impedance to ground. This
impedance is the same as its previous setting before the device was
powered down. The output voltage amplitude of this connector
is 0 V.
- The CLK IN connector has 50 Ω impedance to
ground.
- PFI 0 and PFI 1 are tristated and have a 1
kΩ impedance to ground.

- In devices with a DDC connector, DIGITAL DATA & CONTROL
output lines are disabled and floating; inputs have a
100 Ω differential termination.

- PXI trigger lines are tristated and floating.

After the operating system is fully booted and
NI-FGEN is loaded, or when you perform a hard reset to the device
directly from MAX or using NI-FGEN, the signal generator is in the
following state:

- CH 0 output is enabled.
- CH 0 output attenuation is set to 0 dB.
- Output impedance is set to 50 Ω.
- The Low-Gain Amplifier path is enabled in the Analog Output
path.
- The analog filter is disabled.

- The digital filter of the NI 5441
inside the DAC is disabled.

- CLK IN is disabled and has a 50 Ω
impedance to ground.
- PFI 0 and PFI 1 are tristated and have a 1
kΩ impedance to ground.

- On devices with a DDC connector, all output lines on the DIGITAL DATA
& CONTROL Connector are disabled and floating; inputs have a
100 Ω differential termination.

- PXI trigger lines are tristated and floating.
- The sample rate is set to the maximum rate, with the Sample
clock source set to the internal Sample clock timebase.
- The Sample clock timebase is tuned by the internal reference
control voltage.

Parent topic:

NI 5441 NI 5441 Overview

<!--NI_TOPIC bundle=ni-fgen path=ni-5441-preamplifier-attenuation.html language=enus -->
## TOPIC 00495: NI 5441 Preamplifier Attenuation

- bundle_id: `ni-fgen`
- source_path: `ni-5441-preamplifier-attenuation.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5441-preamplifier-attenuation.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The preamplifier attenuation section is before the Low-Gain and High-Gain amplifiers in the analog path. The attenuators provide a range of attenuation from 0 to a maximum of 12 dB in steps of 3 dB. NI-FGEN automatically controls the value of attenuation set in the preamplifier attenuation section d

### NI 5441 Preamplifier Attenuation

The preamplifier attenuation section is before the
Low-Gain and High-Gain amplifiers in the *analog path*. The attenuators provide a
range of attenuation from 0 to a maximum of 12 dB in steps of
3 dB. NI-FGEN automatically controls the value of attenuation set
in the preamplifier attenuation section depending on the set
gain. You can read the value NI-FGEN has selected for preamplifier attenuation using the 
Pre-Amplifier Attenuation property or the 
NIFGEN_ATTR_PRE_AMPLIFIER_ATTENUATION attribute.

Preamplifier attenuation improves the signal
distortion because amplifiers provide lower distortion performance
with smaller signals. However, attenuation lowers the amplitude of
both the signal and the noise in a signal as the signal-to-noise
ratio (SNR) is unchanged upon attenuation. Amplifiers also have a
fixed noise associated with them. The total noise at the amplifier
output is obtained by taking the root of the sum of squares of the
following factors:

- The input signal noise multiplied by the gain of the
amplifier
- The amplifier noise

The total noise is dominated by the larger factor.
If the signal is attenuated so that its noise when multiplied by
gain at the amplifier input is smaller than the amplifier noise,
then the output has a higher SNR. This higher SNR is a good reason
to implement some of the signal generator overall attenuation as preamplifier
attenuation.

Parent topic:

NI 5441 Attenuation

Related concepts:

- NI 5441 Analog Output

<!--NI_TOPIC bundle=ni-fgen path=ni-5441-prefilter-gain-and-offset.html language=enus -->
## TOPIC 00496: NI 5441 Prefilter Gain and Offset

- bundle_id: `ni-fgen`
- source_path: `ni-5441-prefilter-gain-and-offset.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5441-prefilter-gain-and-offset.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use the following prefiltering components to add impairments to your data and/or to eliminate overflows that occur later in the OSP block. Related Topics Prefilter Gain Prefilter Offset

### NI 5441 Prefilter Gain and Offset

You can use the following prefiltering components
to add impairments to your data and/or to eliminate overflows that
occur later in the 
*OSP* block.

#### Related Topics

- Prefilter Gain
- Prefilter
Offset

Parent topic:

NI 5441 Onboard Signal Processing Components

Related concepts:

- NI 5441 Onboard Signal Processing (OSP)
- NI 5441 Prefilter Gain
- NI 5441 Prefilter Offset

<!--NI_TOPIC bundle=ni-fgen path=ni-5441-prefilter-gain.html language=enus -->
## TOPIC 00497: NI 5441 Prefilter Gain

- bundle_id: `ni-fgen`
- source_path: `ni-5441-prefilter-gain.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5441-prefilter-gain.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Prefilter gain can change the gain of the I and Q stream during signal generation. You can change the I and Q prefilter gains independently by setting the Pre-Filter Gain I and Pre-Filter Gain Q properties or the NIFGEN_ATTR_OSP_PRE_FILTER_GAIN_I and NIFGEN_ATTR_OSP_PRE_FILTER_GAIN_Q attributes. The

### NI 5441 Prefilter Gain

Prefilter gain can change the gain of the I and Q
stream during signal generation. You can change the I and Q
prefilter gains independently by setting the 
Pre-Filter
Gain I and 
Pre-Filter
Gain Q properties or the 
NIFGEN_ATTR_OSP_PRE_FILTER_GAIN_I and 
NIFGEN_ATTR_OSP_PRE_FILTER_GAIN_Q attributes. The gain can range from 
-2.0 to +2.0 (unitless). Any
time the prefilter gain changes, the OSP block ignores all
overflows for the next 
 50 I/Q samples. If an overflow occurs during
these 
 50
 samples, the data is clipped and no error is returned. Overflows are common during the first 50
 I/Q samples after a
prefilter gain change because the abrupt change is seen as a
transient by the FIR filters. The prefilter gain can be
used to attenuate the I/Q data to eliminate overflows in later
stages of the OSP block. You can also use the prefilter gain to 
*simulate
I/Q gain imbalance impairments*.

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

NI 5441 Prefilter Gain and Offset

Related concepts:

- NI 5441 Quadrature Upconversion

<!--NI_TOPIC bundle=ni-fgen path=ni-5441-prefilter-offset.html language=enus -->
## TOPIC 00498: NI 5441 Prefilter Offset

- bundle_id: `ni-fgen`
- source_path: `ni-5441-prefilter-offset.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5441-prefilter-offset.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Prefilter offset can add offset to the I and Q stream during signal generation. Change the I and Q prefilter offsets independently by setting the Pre-Filter Offset I and Pre-Filter Offset Q properties or the NIFGEN_ATTR_OSP_PRE_FILTER_OFFSET_I and NIFGEN_ATTR_OSP_PRE_FILTER_OFFSET_Q attributes. The

### NI 5441 Prefilter Offset

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
offset changes, the OSP block ignores all overflows for the next 50
I/Q samples. If an overflow occurs during these 50 samples, the data
is clipped and no error is returned. Overflows are common
during the first 50 I/Q samples after a prefilter offset change
because the abrupt change is seen as a transient by the
interpolation filters. 
You can use the prefilter offset to 
*simulate
I/Q DC offset impairments*.

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

NI 5441 Prefilter Gain and Offset

Related concepts:

- NI 5441 Quadrature Upconversion
- NI 5441 Prefilter Gain

<!--NI_TOPIC bundle=ni-fgen path=ni-5441-quadrature-upconversion.html language=enus -->
## TOPIC 00499: NI 5441 Quadrature Upconversion

- bundle_id: `ni-fgen`
- source_path: `ni-5441-quadrature-upconversion.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5441-quadrature-upconversion.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the behavior of the OSP block during quadrature upconversion. In quadrature upconversion, you give the I and Q complex waveform data to the OSP block. This data is then pulse shaped, interpolated up to a high sample rate, and then upconverted to a programmable carrier freq

### NI 5441 Quadrature Upconversion

The following figure shows the behavior of the OSP
block during quadrature upconversion.

[IMAGE alt='image' src='GUID-8BBD6C9B-8AB5-469C-A78F-89299A58482D-a5.gif']

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
5. Set the corresponding filter parameter or download a 
 custom set of FIR
filter coefficients .
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

NI 5441 Common Onboard Signal Processing Applications

Related concepts:

- NI 5441 FIR Filter Type: Custom
- NI 5441 Prefilter Gain

<!--NI_TOPIC bundle=ni-fgen path=ni-5441-sample-clock-considerations.html language=enus -->
## TOPIC 00500: NI 5441 Sample Clock Considerations

- bundle_id: `ni-fgen`
- source_path: `ni-5441-sample-clock-considerations.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5441-sample-clock-considerations.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The performance of the signal generator that is using the OSP block can be significantly affected by the purity of its Sample clock. Sample clocks with high amounts of jitter or phase noise can create spurs in the signal generator spectrum that are not present when a pure Sample clock is used. If yo

### NI 5441 Sample Clock Considerations

The performance of the signal generator that is
using the OSP block can be significantly affected by the purity of
its Sample clock. Sample clocks with high amounts of jitter or
phase noise can create spurs in the signal generator spectrum that
are not present when a pure Sample clock is used. If you configure
the signal generator for Automatic Clock mode through the 
Clock
Mode property or the 
NIFGEN_ATTR_CLOCK_MODE attribute, NI-FGEN often selects 
*High-Resolution clocking* in
order to achieve a specific 
*I/Q rate*. Because
High-Resolution clocking has more jitter than Divide-By-N clocking,
extra spurs may occur in the signal generator output spectrum. If
you cannot tolerate these spurs, either use a pure 
*external clock*
as the Sample clock of the signal generator, or use software
resampling to change the I/Q data to an I/Q rate that works with
Divide-By-N clocking. If you are resampling, pulse shaping should
be done in software and the pulse-shaping filter type should be set to Flat by calling the
Filter
Type property or the 
NIFGEN_ATTR_OSP_FIR_FILTER_TYPE attribute.

Parent topic:

NI 5441 IQ Rate

Related concepts:

- NI 5441 Internal Sample Clock
- NI 5441 IQ Rate
- NI 5441 External Sample Clock
