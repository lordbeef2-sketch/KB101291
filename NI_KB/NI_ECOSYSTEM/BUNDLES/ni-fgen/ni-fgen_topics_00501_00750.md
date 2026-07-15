# NI DOCUMENT BUNDLE: ni-fgen

<!--NI_BUNDLE_CHUNK bundle=ni-fgen start=501 end=750 -->
<!--NI_TOPIC bundle=ni-fgen path=ni-5441-sample-size-and-resolution.html language=enus -->
## TOPIC 00501: NI 5441 Sample Size and Resolution

- bundle_id: `ni-fgen`
- source_path: `ni-5441-sample-size-and-resolution.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5441-sample-size-and-resolution.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5441 stores arbitrary waveforms in memory as signed 16-bit digital words. On the NI 5441, the entire 16 bits are sent to the digital gain circuit, the digital filter, and the DAC. The NI 5441 stores arbitrary complex waveforms in memory as interleaved real/imaginary 16-bit digital words. Each

### NI 5441 Sample Size and Resolution

The NI 5441 stores arbitrary
waveforms in memory as signed 16-bit digital words. On the
NI 5441, the entire 16 bits are sent to the digital
gain circuit, the digital filter, and the DAC.

The NI 5441 stores arbitrary 
complex waveforms in memory as interleaved real/imaginary
16-bit digital words. Each real/imaginary pair is processed by the
OSP block before it is sent to the digital gain circuit, the
digital filter, and the DAC.

Related Topics

*Onboard Memory*

*Waveform Sizes*

Parent topic:

NI 5441 Waveform Generation

Related concepts:

- NI 5441 Onboard Memory
- NI 5441 Waveform Size and Quantum

<!--NI_TOPIC bundle=ni-fgen path=ni-5441-script-mode.html language=enus -->
## TOPIC 00502: NI 5441 Script Mode

- bundle_id: `ni-fgen`
- source_path: `ni-5441-script-mode.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5441-script-mode.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Script Mode allows you to use scripting to link and loop multiple waveforms in complex combinations using a script. A script is a series of instructions that indicates how waveforms saved in the onboard memory should be sent to the DUT. Scripts have many different uses, including specifying the orde

### NI 5441 Script Mode

*Script Mode* allows you to use scripting to link and
loop multiple waveforms in complex combinations using a 
script. A script is a series of instructions that
indicates how waveforms saved in the onboard memory should be sent
to the DUT. Scripts have many different uses, including specifying the order in which the waveforms
are generated, the number of times they are generated, and the
triggers and markers associated with the generation.

Parent topic:

NI 5441 Output Modes

Related concepts:

- Script Mode

<!--NI_TOPIC bundle=ni-fgen path=ni-5441-signal-routing.html language=enus -->
## TOPIC 00503: NI 5441 Signal Routing

- bundle_id: `ni-fgen`
- source_path: `ni-5441-signal-routing.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5441-signal-routing.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: An NI signal generator is capable of sending and receiving signals through the front panel and the PXI or RTSI trigger bus. The front panel connectors provides connectivity for the output channel as well as for control lines for sending and receiving clocks, triggers, and events. You can use the PXI

### NI 5441 Signal Routing

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

NI 5441 Theory of Operation

Related concepts:

- NI 5441 Syntax for Terminal Names

<!--NI_TOPIC bundle=ni-fgen path=ni-5441-single-tone.html language=enus -->
## TOPIC 00504: NI 5441 Single-Tone

- bundle_id: `ni-fgen`
- source_path: `ni-5441-single-tone.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5441-single-tone.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the behavior of the OSP block during single–tone generation. Use the Standard Function output mode to generate a single-tone. During single-tone generation, the NCO is used to create the output signal.

### NI 5441 Single-Tone

The following figure shows the behavior of the OSP
block during single–tone generation.

[IMAGE alt='image' src='GUID-A9C5CFE7-B5B9-4B98-A8F6-7ED157B865F7-a5.gif']

Use the 
*Standard Function output
mode* to generate a single-tone. During single-tone generation,
the 
*NCO* is used to create the
output signal.

Parent topic:

NI 5441 Common Onboard Signal Processing Applications

Related concepts:

- Standard Function Mode
- NI 5441 Numerically Controlled Oscillator (NCO)

<!--NI_TOPIC bundle=ni-fgen path=ni-5441-single-trigger-mode.html language=enus -->
## TOPIC 00505: NI 5441 Single Trigger Mode

- bundle_id: `ni-fgen`
- source_path: `ni-5441-single-trigger-mode.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5441-single-trigger-mode.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: When your application is configured for Single trigger mode, only one Start trigger is required to begin waveform generation. All Start triggers after the first Start trigger are ignored. Once the waveform generation is complete, the analog output indefinitely settles at the DC value of the last sam

### NI 5441 Single Trigger Mode

When your application is configured for Single
trigger mode, only one Start trigger is required to begin waveform
generation. All Start triggers after the first Start trigger are
ignored. Once the waveform generation is complete, the analog
output indefinitely settles at the DC value of the last sample in
the waveform. The
following table provides more information about
waveform generation behavior in Arbitrary Waveform, Arbitrary
Sequence, and Frequency List output modes.

| Output Mode | Trigger Behavior |
| --- | --- |
| Arbitrary Waveform Mode | The waveform you downloaded generates only once and waveform generation halts, unless the Arbitrary Waveform Repeat Count property or the NIFGEN_ATTR_ARB_REPEAT_COUNT attribute is set, in which case the waveform generates the specified number of times. |
| Arbitrary Sequence Mode | The waveform pattern you define in the sequence list generates only once. When a Start trigger is received, generation begins at the first segment and continues through the last segment, after which the waveform generation halts. You can determine the DC value at which waveform generation ends by configuring the last point in the final segment as the desired DC value, or you can add an extra segment filled with the same DC value. |
| Frequency List Mode | The device generates each step in the active frequency list sequentially. |

Parent topic:

NI 5441 Trigger Modes

<!--NI_TOPIC bundle=ni-fgen path=ni-5441-specifications.html language=enus -->
## TOPIC 00506: NI 5441 Specifications

- bundle_id: `ni-fgen`
- source_path: `ni-5441-specifications.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5441-specifications.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: For information about the signal generator specifications, refer to the device specifications. You can access these specifications by navigating to Start»All Programs»National Instruments» NI-FGEN»Documentation»NI Signal Generators Specifications, or you can visit ni.com/manuals.

### NI 5441 Specifications

For information about the signal generator
specifications, refer to the 
*device
specifications*. You can access these specifications by
navigating to 
Start»All Programs»National Instruments»
NI-FGEN»Documentation»NI Signal Generators Specifications, or you can visit 
ni.com/manuals.

Parent topic:

NI 5441 NI 5441 Overview

<!--NI_TOPIC bundle=ni-fgen path=ni-5441-standard-function-mode.html language=enus -->
## TOPIC 00507: NI 5441 Standard Function Mode

- bundle_id: `ni-fgen`
- source_path: `ni-5441-standard-function-mode.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5441-standard-function-mode.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Standard Function output mode is used to generate standard function waveforms such as sine, square, triangle, and so on. On the NI 5441, Standard Function mode is implemented through direct digital synthesis (DDS). DDS is a technique for deriving, under digital control, an analog frequency source fr

### NI 5441 Standard Function Mode

Standard Function output mode is used to generate standard
function waveforms such as sine, square, triangle, and so on. 
On the NI 5441, *Standard Function mode* is implemented
through *direct digital synthesis* (DDS). DDS is a technique for
deriving, under digital control, an analog frequency source from a
single Reference clock frequency. This technique produces
high-frequency accuracy and resolution, temperature stability,
wideband tuning, and rapid, phase-continuous frequency
switching.

In DDS mode, a fixed–size memory (called *lookup memory*) stores one cycle of a periodic waveform. A phase accumulator indexes the lookup memory. For each cycle of the device Sample clock, the sample of the waveform in lookup memory that is addressed by the phase accumulator is returned. The accumulator is then incremented by the value in the frequency control word (FCW). By adjusting the Frequency property or the NIFGEN_ATTR_FUNC_FREQUENCY attribute, NI-FGEN calculates the corresponding FCW, and you can vary the output frequency of the waveform in lookup memory. The phase accumulator increments in smaller steps for smaller FCWs. Accordingly, you need more samples to generate one waveform cycle, so the frequency is lower. A higher FCW results in a higher frequency. In DDS mode, the Sample clock does not vary with the frequency of the generated waveform. At higher frequencies, some waveform samples in lookup memory are skipped; at lower frequencies, some samples output multiple times in succession.

Parent topic:

NI 5441 Output Modes

Related concepts:

- Standard Function Mode
- Direct Digital Synthesis

<!--NI_TOPIC bundle=ni-fgen path=ni-5441-stepped-trigger-mode.html language=enus -->
## TOPIC 00508: NI 5441 Stepped Trigger Mode

- bundle_id: `ni-fgen`
- source_path: `ni-5441-stepped-trigger-mode.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5441-stepped-trigger-mode.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The waveform you downloaded generates each time a Start trigger occurs. After a waveform finishes generating, the last sample of the waveform repeats continuously until the next Start trigger is received. When the next Start trigger is received, the waveform generates again. If a Start trigger is re

### NI 5441 Stepped Trigger Mode

The waveform you downloaded generates each time a
Start trigger occurs. After a waveform finishes generating, the
last sample of the waveform repeats continuously until the next
Start trigger is received. When the next Start trigger is received,
the waveform generates again. If a Start trigger is received while
a waveform is generating, the Start trigger is ignored and another
Start trigger is required to regenerate the waveform after the last
sample generates. The
following table provides more information about
waveform generation behavior in Arbitrary Waveform, Arbitrary
Sequence, and Frequency List output modes.

| Output Mode | Trigger Behavior |
| --- | --- |
| Arbitrary Waveform Mode | If the Arbitrary Waveform Repeat Count property or the NIFGEN_ATTR_ARB_REPEAT_COUNT attribute is set, the waveform generates the specified number of times instead of just once. |
| Arbitrary Sequence Mode | The waveforms you define in the sequence list generate one segment at a time, each time a Start trigger occurs. The waveform loops as many times as has been configured for that particular segment. After the generation of a segment has halted, the last sample of the waveform repeats continuously until the next Start trigger is received. After the sequence list is exhausted, the waveform generation returns to the first segment and subsequent Start triggers restart the process. |
| Frequency List Mode | The device generates the next step in the active frequency list every time a Start trigger occurs. After the duration for a step has elapsed, the signal generation stops and remains at the configured DC offset level until the next Start trigger is received. When the next Start trigger is received, the next step in the frequency list is generated. After the final step, the frequency list repeats until generation is aborted. If the Trigger Source property or the NIFGEN_ATTR_TRIGGER_SOURCE attribute is set to NIFGEN_VAL_IMMEDIATE, the only way to advance to the next step in the frequency list is to call the niFgen Send Software Edge Trigger VI or the niFgen_SendSoftwareEdgeTrigger function. |

Parent topic:

NI 5441 Trigger Modes

<!--NI_TOPIC bundle=ni-fgen path=ni-5441-streaming.html language=enus -->
## TOPIC 00509: NI 5441 Streaming

- bundle_id: `ni-fgen`
- source_path: `ni-5441-streaming.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5441-streaming.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Streaming is a way to generate waveforms that are too large to fit in the onboard memory of the signal generator. Streaming can be used in Arbitrary Waveform, Arbitrary Sequence, or Script output modes. To stream waveform data, allocate and identify all or a portion of the signal generator onboard m

### NI 5441 Streaming

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

NI 5441 Waveform Generation

Related concepts:

- Arbitrary Waveform Output Mode
- Arbitrary Sequence Mode
- Script Mode
- Direct DMA

<!--NI_TOPIC bundle=ni-fgen path=ni-5441-synchronization.html language=enus -->
## TOPIC 00510: NI 5441 Synchronization

- bundle_id: `ni-fgen`
- source_path: `ni-5441-synchronization.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5441-synchronization.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Your signal generator is based on the National Instruments Synchronization and Memory Core (SMC) technology and therefore supports TClk synchronization. Refer to the NI-TClk Synchronization Help for more information about NI-TClk Synchronization.

### NI 5441 Synchronization

Your signal generator is based on the 
National Instruments
Synchronization and Memory Core (SMC) technology and therefore
supports TClk synchronization. Refer to the 
NI-TClk
Synchronization Help for more information about NI-TClk
Synchronization.

Parent topic:

NI 5441 NI 5441 Overview

<!--NI_TOPIC bundle=ni-fgen path=ni-5441-syntax-for-terminal-names.html language=enus -->
## TOPIC 00511: NI 5441 Syntax for Terminal Names

- bundle_id: `ni-fgen`
- source_path: `ni-5441-syntax-for-terminal-names.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5441-syntax-for-terminal-names.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The syntax for terminal names is a unique identifier that refers to a physical terminal in your system. To guarantee the uniqueness of a terminal name across multiple devices, terminal names begin with a forward slash, followed by the name of the device as configured in MAX, such as Dev1. A forward

### NI 5441 Syntax for Terminal Names

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

NI 5441 Signal Routing

<!--NI_TOPIC bundle=ni-fgen path=ni-5441-theory-of-operation.html language=enus -->
## TOPIC 00512: NI 5441 Theory of Operation

- bundle_id: `ni-fgen`
- source_path: `ni-5441-theory-of-operation.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5441-theory-of-operation.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Expand this topic for information about the theory of operation of your signal generator.

### NI 5441 Theory of Operation

Expand this topic for information about the theory
of operation of your signal generator.

Parent topic:

NI 5441 NI 5441 Overview

<!--NI_TOPIC bundle=ni-fgen path=ni-5441-thermal-shutdown.html language=enus -->
## TOPIC 00513: NI 5441 Thermal Shutdown

- bundle_id: `ni-fgen`
- source_path: `ni-5441-thermal-shutdown.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5441-thermal-shutdown.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: NI-FGEN supports thermal shutdown capability for the NI 5441. This capability allows the signal generator to detect when it has reached a dangerously high temperature and to then power down to prevent damage to the device. Air circulation paths, fan settings, and space allowances are several factors

### NI 5441 Thermal Shutdown

NI-FGEN supports thermal shutdown capability for
the NI 5441. This
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

NI 5441 NI 5441 Overview

<!--NI_TOPIC bundle=ni-fgen path=ni-5441-trigger-modes.html language=enus -->
## TOPIC 00514: NI 5441 Trigger Modes

- bundle_id: `ni-fgen`
- source_path: `ni-5441-trigger-modes.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5441-trigger-modes.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5441 has four trigger modes: Single, Continuous, Stepped, and Burst. These trigger modes are available for Arbitrary Waveform, Arbitrary Sequence, and Frequency List output mode. Refer to the niFgen Configure Trigger Mode VI or the niFgen_ConfigureTriggerMode function for information about se

### NI 5441 Trigger Modes

The NI 5441 has four trigger modes: Single, Continuous, Stepped,
and Burst. These trigger modes are available for Arbitrary
Waveform, Arbitrary Sequence, and Frequency List output mode.
Refer to the 
niFgen
Configure Trigger Mode VI or the 
niFgen_ConfigureTriggerMode function for information about setting the trigger mode.

Parent topic:

NI 5441 Triggering

<!--NI_TOPIC bundle=ni-fgen path=ni-5441-trigger-sources.html language=enus -->
## TOPIC 00515: NI 5441 Trigger Sources

- bundle_id: `ni-fgen`
- source_path: `ni-5441-trigger-sources.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5441-trigger-sources.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Trigger sources are software selectable. You can use any of the following external input triggers: PFI 0 or PFI 1 on the front panel connectors PFI 2 or PFI 3 on the DIGITAL DATA & CONTROL front panel connector PXI_TRIG<0..7> lines and PXI_STAR on the PXI trigger bus backplane The following figure s

### NI 5441 Trigger Sources

Trigger sources are software selectable. You can
use any of the following external input triggers:

- PFI 0 or PFI 1 on the front panel connectors

- PFI 2 or PFI 3 on the DIGITAL DATA & CONTROL front panel
connector

- PXI_TRIG<0..7> lines and
PXI_STAR on the PXI trigger bus backplane

The following figure shows the possible trigger
sources for the NI 5441.

[IMAGE alt='image' src='GUID-3D9E272C-29DC-41E1-8DF1-6E390A3EE66C-a5.gif']

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

NI 5441 Triggering

Related concepts:

- NI 5441 Exporting Signals
- PXI Trigger Lines
- PXI Star Trigger Line

<!--NI_TOPIC bundle=ni-fgen path=ni-5441-trigger-timing.html language=enus -->
## TOPIC 00516: NI 5441 Trigger Timing

- bundle_id: `ni-fgen`
- source_path: `ni-5441-trigger-timing.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5441-trigger-timing.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the relationship between Start trigger and the waveform output. t[s1] is the required pulse width on the Start trigger signal. t[s2] is the delay from the Start trigger to the waveform output. Refer to the NI PXI-5441 Specifications for more information about these timing

### NI 5441 Trigger Timing

The following figure shows the relationship between
Start trigger and the waveform output. t<sub>s1</sub> is the required pulse width on the Start trigger
signal. t<sub>s2</sub> is the delay from the Start trigger to the waveform
output. Refer to the 
*NI PXI-5441 Specifications* for more information about these timing
parameters.

[IMAGE alt='image' src='GUID-9DD6A51C-2BCA-4129-9C8D-0A821181925F-a5.gif']

The NI 5441 also allows you to export
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

NI 5441 Triggering

<!--NI_TOPIC bundle=ni-fgen path=ni-5441-triggering.html language=enus -->
## TOPIC 00517: NI 5441 Triggering

- bundle_id: `ni-fgen`
- source_path: `ni-5441-triggering.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5441-triggering.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can define the signal generator functionality by using the various triggering techniques. Expand this section to learn more about using triggers with your signal generator.

### NI 5441 Triggering

You can define the signal generator functionality
by using the various triggering techniques. Expand this section to
learn more about using triggers with your signal generator.

Parent topic:

NI 5441 NI 5441 Overview

<!--NI_TOPIC bundle=ni-fgen path=ni-5441-using-an-external-clock-with-the-osp.html language=enus -->
## TOPIC 00518: NI 5441 Using an External Clock with the OSP Block

- bundle_id: `ni-fgen`
- source_path: `ni-5441-using-an-external-clock-with-the-osp.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5441-using-an-external-clock-with-the-osp.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Some applications may require lower jitter or phase noise than is provided by the onboard High-Resolution clock. You can use an external clock source to achieve spectral purity at any arbitrary I/Q rate. To determine the frequency of the sample rate for the external clock source, complete the follow

### NI 5441 Using an External Clock with the OSP Block

Some applications may require lower jitter or phase
noise than is provided by the onboard High-Resolution clock. You can use an
external clock source to achieve spectral purity at any arbitrary
I/Q rate. To determine the frequency of the sample rate for the
external clock source, complete the following steps.

1. Set the 
Sample
Clock Source property or the 
 NIFGEN_ATTR_SAMPLE_CLOCK_SOURCE attribute to the external 
 clock source 
you are using.
2. Set the 
IQ Rate
property or the 
 NIFGEN_ATTR_OSP_IQ_RATE attribute.

1. (Optional) Set the EM 
FIR
Interpolation Factor property or the 
 NIFGEN_ATTR_OSP_FIR_FILTER_INTERPOLATION attribute.
2. (Optional) Set the 
CIC
Interpolation Factor property or the 
 NIFGEN_ATTR_OSP_CIC_FILTER_INTERPOLATION attribute.
3. Read the value of the 
Sample
Rate property or the 
 NIFGEN_ATTR_ARB_SAMPLE_RATE attribute.
4. Set the external clock source sample rate to the EM frequency
of the Sample Rate property you just read.
5. Validate that the external Sample clock source is connected to
the NI 5441 connector specified in the Sample Clock Source property
or the 
 NIFGEN_ATTR_SAMPLE_CLOCK_SOURCE 
attribute and generating a clock before you continue configuring
the NI 5441.

For more information about using external clocks, refer to 
*External Sample
Clock Sources*.

Parent topic:

NI 5441 IQ Rate

Related concepts:

- NI 5441 External Sample Clock

<!--NI_TOPIC bundle=ni-fgen path=ni-5441-waveform-amplitude-control.html language=enus -->
## TOPIC 00519: NI 5441 Waveform Amplitude Control

- bundle_id: `ni-fgen`
- source_path: `ni-5441-waveform-amplitude-control.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5441-waveform-amplitude-control.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5441 uses both amplifiers and attenuators to achieve required amplitude settings. Output Paths and Amplifiers The following figure shows two different gain paths: the Direct path and the Main path with High-Gain and Low-Gain amplifiers. The Direct path provides the output of the main DAC to t

### NI 5441 Waveform Amplitude Control

The NI 5441 uses both amplifiers and
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

NI 5441 Analog Output

Related concepts:

- NI 5441 DC Offset

<!--NI_TOPIC bundle=ni-fgen path=ni-5441-waveform-and-generation-instruction-m.html language=enus -->
## TOPIC 00520: NI 5441 Waveform and Generation Instruction Memory Size

- bundle_id: `ni-fgen`
- source_path: `ni-5441-waveform-and-generation-instruction-m.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5441-waveform-and-generation-instruction-m.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Waveform Memory Size Waveforms are stored in the NI 5441 onboard memory in contiguous blocks. These blocks are allocated in multiples of 128 bytes. This allocation style means that while waveform sizes may be multiples of four samples (eight bytes) on the NI 5441 , the amount of onboard memory alloc

### NI 5441 Waveform and Generation Instruction Memory Size

#### Waveform Memory Size

Waveforms are stored in the
NI 5441 onboard memory in contiguous
blocks. These blocks are allocated in multiples of 128 bytes. This
allocation style means that while waveform sizes may be multiples
of four samples (eight bytes) on the NI 5441
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

The NI 5441 uses a
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

NI 5441 Onboard Memory

<!--NI_TOPIC bundle=ni-fgen path=ni-5441-waveform-generation.html language=enus -->
## TOPIC 00521: NI 5441 Waveform Generation

- bundle_id: `ni-fgen`
- source_path: `ni-5441-waveform-generation.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5441-waveform-generation.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5441 supports the following output, or generation, modes: Standard Function Arbitrary Waveform Arbitrary Sequence Frequency List Script To select an output mode, set the Output Mode parameter of the niFgen Configure Output Mode VI or the niFgen_ConfigureOutputMode function.

### NI 5441 Waveform Generation

The NI 5441 supports the
following output, or generation, modes:

- Standard Function
- Arbitrary Waveform
- Arbitrary Sequence
- Frequency List
- Script

To select an output mode, set the 
Output Mode parameter of the 
niFgen
Configure Output Mode VI or the 
niFgen_ConfigureOutputMode function.

Parent topic:

NI 5441 NI 5441 Overview

Related concepts:

- NI 5441 Standard Function Mode
- NI 5441 Arbitrary Waveform Mode
- NI 5441 Arbitrary Sequence Mode
- NI 5441 Frequency List Mode
- NI 5441 Script Mode

<!--NI_TOPIC bundle=ni-fgen path=ni-5441-waveform-quantum.html language=enus -->
## TOPIC 00522: NI 5441 Waveform Quantum

- bundle_id: `ni-fgen`
- source_path: `ni-5441-waveform-quantum.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5441-waveform-quantum.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Quantum is the increment in samples that waveform sizes must adhere to. Waveforms must be downloaded in integer multiples of the four samples (or two for complex samples), the quantum for the NI 5441. For example, if while in Arbitrary Waveform mode, you request to load a waveform of seven samples,

### NI 5441 Waveform Quantum

Quantum is the increment in samples that waveform
sizes must adhere to. Waveforms must be downloaded in integer multiples of the four samples (or two for complex samples), the quantum for the NI 5441.

For example, if while in Arbitrary Waveform mode, you request to load a waveform of seven samples, the task will not complete successfully because the waveform is not an integer multiple of the quantum size. Waveform sizes that meet the conditions include 4, 8, 12, 16, 20, and so on, up to maximum allowable waveform size.

Parent topic:

NI 5441 Waveform Size and Quantum

<!--NI_TOPIC bundle=ni-fgen path=ni-5441-waveform-size-and-quantum.html language=enus -->
## TOPIC 00523: NI 5441 Waveform Size and Quantum

- bundle_id: `ni-fgen`
- source_path: `ni-5441-waveform-size-and-quantum.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5441-waveform-size-and-quantum.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5441 onboard memory architecture imposes certain requirements on the waveform size and quantum.

### NI 5441 Waveform Size and Quantum

The NI 5441 onboard memory architecture
imposes certain requirements on the waveform *size* and *quantum*.

Parent topic:

NI 5441 Waveform Generation

Related concepts:

- NI 5441 Waveform Size
- NI 5441 Waveform Quantum

<!--NI_TOPIC bundle=ni-fgen path=ni-5441-waveform-size.html language=enus -->
## TOPIC 00524: NI 5441 Waveform Size

- bundle_id: `ni-fgen`
- source_path: `ni-5441-waveform-size.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5441-waveform-size.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Minimum Waveform Size The minimum waveform size on the NI 5441 depends on the output mode and the trigger mode. Refer to the device specifications for the minimum waveform size values for the different modes. To provide greater programming flexibility, NI-FGEN does not strictly enforce the minimum

### NI 5441 Waveform Size

#### Minimum Waveform Size

The
minimum waveform size on the NI 5441 depends on the output mode and the 
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

NI 5441 Waveform Size and Quantum

Related concepts:

- NI 5441 Trigger Modes
- NI 5441 Waveform and Generation Instruction Memory Size

<!--NI_TOPIC bundle=ni-fgen path=ni-5442-aborting-generation.html language=enus -->
## TOPIC 00525: NI 5442 Aborting Generation

- bundle_id: `ni-fgen`
- source_path: `ni-5442-aborting-generation.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5442-aborting-generation.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can abort the generation of the current waveform. Aborting the generation exhibits different behaviors for different waveform output modes. Output Mode Abort Behavior Standard Function, Frequency List Abort to Ground—Signal remains at the level for which the DC offset is configured. Arbitrary Wa

### NI 5442 Aborting Generation

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

NI 5442 Waveform Generation

Related concepts:

- NI 5442 Waveform Generation
- Abort to Ground
- Abort to a Known Voltage

<!--NI_TOPIC bundle=ni-fgen path=ni-5442-access-and-active-leds.html language=enus -->
## TOPIC 00526: NI 5442 ACCESS and ACTIVE LEDs

- bundle_id: `ni-fgen`
- source_path: `ni-5442-access-and-active-leds.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5442-access-and-active-leds.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The ACCESS and ACTIVE LEDs indicate the status of the PXIe module: ACCESS LED The ACCESS LED indicates basic hardware status as shown in the following table. Color Indications Off Device is not yet functional, or the device has detected a problem with a power rail. Amber The device is being accessed

### NI 5442 ACCESS and ACTIVE LEDs

The ACCESS and ACTIVE LEDs indicate the status of
the PXIe module:

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

NI 5442 Front Panel

<!--NI_TOPIC bundle=ni-fgen path=ni-5442-accessories.html language=enus -->
## TOPIC 00527: NI 5442 Accessories

- bundle_id: `ni-fgen`
- source_path: `ni-5442-accessories.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5442-accessories.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: National Instruments offers a variety of products to use with your signal generator, including cables and other accessories. Visit ni.com for more information.

### NI 5442 Accessories

National Instruments offers a variety of products
to use with your signal generator, including cables and other
accessories. Visit 
ni.com for more
information.

Parent topic:

NI 5442 NI 5442 Overview

<!--NI_TOPIC bundle=ni-fgen path=ni-5442-amplitude-modulation-am-or-double-sid.html language=enus -->
## TOPIC 00528: NI 5442 Amplitude Modulation (AM) or Double Sideband

- bundle_id: `ni-fgen`
- source_path: `ni-5442-amplitude-modulation-am-or-double-sid.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5442-amplitude-modulation-am-or-double-sid.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can generate an AM radio signal with the OSP block. To generate an AM signal, complete the following steps. Enable onboard signal processing by setting the OSP Enabled property or the NIFGEN_ATTR_OSP_ENABLED attribute. Specify the use of real numbers for the waveform data by setting the Data Pro

### NI 5442 Amplitude Modulation (AM) or Double Sideband

[IMAGE alt='image' src='GUID-F01501B2-890D-4D3D-A326-C8ED6307C0C6-a5.gif']

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

NI 5442 Common Onboard Signal Processing Applications

<!--NI_TOPIC bundle=ni-fgen path=ni-5442-analog-filter.html language=enus -->
## TOPIC 00529: NI 5442 Analog Filter

- bundle_id: `ni-fgen`
- source_path: `ni-5442-analog-filter.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5442-analog-filter.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The analog filter is a lowpass filter that is used to eliminate aliased images and artifacts due to the digital-to-analog conversion from the signal from the DAC. In general, use the analog filter for signals containing a large portion of sinusoidal content, such as AM and FM, sinc pulse, and sinuso

### NI 5442 Analog Filter

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

NI 5442 Filtering Effects

Related concepts:

- Aliased Images
- Filtering and Interpolation

<!--NI_TOPIC bundle=ni-fgen path=ni-5442-analog-gain-settings.html language=enus -->
## TOPIC 00530: NI 5442 Analog Gain Settings

- bundle_id: `ni-fgen`
- source_path: `ni-5442-analog-gain-settings.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5442-analog-gain-settings.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following table summarizes the maximum and minimum gain setting that you can apply for the NI-FGEN analog path options. Refer to the device specifications for more information about gain resolution. Analog Path Gain Summary (Matched Load Impedance) NI-FGEN Analog Path Maximum Gain Value Minimum

### NI 5442 Analog Gain Settings

The following table summarizes the maximum and
minimum gain setting that you can apply for the NI-FGEN analog path
options. Refer to the 
*device
specifications* for more information about gain resolution.

| Analog Path Gain Summary (Matched Load Impedance) |  |  |
| --- | --- | --- |
| NI-FGEN Analog Path | Maximum Gain Value | Minimum Gain Value |
| Main Path (default) | 1.027 | 2.817 m |
| Direct Path | 0.527 | 0.354 |
| Note: Gain is unitless. |  |  |

Note

Parent topic:

NI 5442 Waveform Amplitude Control

<!--NI_TOPIC bundle=ni-fgen path=ni-5442-analog-output.html language=enus -->
## TOPIC 00531: NI 5442 Analog Output

- bundle_id: `ni-fgen`
- source_path: `ni-5442-analog-output.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5442-analog-output.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the NI 5442 Analog Output signal path. NI 5442 analog waveforms are generated as follows: The 16-bit digital waveform data from the Waveform Generation Engine or OSP is passed to a digital gain circuit and then high-speed DAC. This DAC also implements a portion of the Anal

### NI 5442 Analog Output

The following figure shows the NI 5442 Analog Output signal path.

[IMAGE alt='image' src='GUID-235B4D87-8DC7-40D4-BF4D-44312DF3D738-a5.gif']

NI 5442 analog waveforms are
generated as follows:

1. The 16-bit digital waveform data from the Waveform Generation
Engine or OSP is passed to a digital gain circuit and then
high-speed DAC. This DAC also implements a portion of the Analog
Output signal path attenuation with a range of 0 dB to
3 dB. Refer to the NI PXIe-5442
Specifications for the exact resolution. You can adjust the amount
of attenuation by configuring the 
Arbitrary
Waveform Gain or 
Amplitude
properties or the 
 NIFGEN_ATTR_ARB_GAIN or 
 NIFGEN_ATTR_FUNC_AMPLITUDE attributes. NI-FGEN calculates and sets the correct amount of
attenuation required, corresponding to the gain setting.
2. Following the DAC, the signal can take one of two paths: the
Direct path or the Main path. NI-FGEN selects the Main path by default. To select the
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
6. Following the Preamplifier Attenuation section, the signal passes through an amplifier with a fixed gain.
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

NI 5442 Theory of Operation

Related concepts:

- Aliased Images

<!--NI_TOPIC bundle=ni-fgen path=ni-5442-arbitrary-sequence-mode.html language=enus -->
## TOPIC 00532: NI 5442 Arbitrary Sequence Mode

- bundle_id: `ni-fgen`
- source_path: `ni-5442-arbitrary-sequence-mode.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5442-arbitrary-sequence-mode.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Arbitrary Sequence mode allows you to load multiple waveforms in the onboard memory of the NI 5442. A finite number of samples make a waveform. To generate these downloaded waveforms in a specific order, you must prepare a sequence, which contains a number of segments in a specific order. Each segme

### NI 5442 Arbitrary Sequence Mode

*Arbitrary Sequence mode* allows you to load multiple
waveforms in the onboard memory of the NI 5442. A finite
number of samples make a waveform. To generate these downloaded
waveforms in a specific order, you must prepare a sequence, which
contains a number of segments in a specific order. Each segment
specifies a downloaded waveform, a number of loops to repeat the
selected waveform, and a numeric offset in which a marker is
generated by the device.

Parent topic:

NI 5442 Output Modes

Related concepts:

- Arbitrary Sequence Mode

<!--NI_TOPIC bundle=ni-fgen path=ni-5442-arbitrary-waveform-generation.html language=enus -->
## TOPIC 00533: NI 5442 Arbitrary Waveform Generation

- bundle_id: `ni-fgen`
- source_path: `ni-5442-arbitrary-waveform-generation.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5442-arbitrary-waveform-generation.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the behavior of the OSP block during basic arbitrary waveform generation . For basic arbitrary waveform generation, disable onboard signal processing by setting the OSP Enabled property or the NIFGEN_ATTR_OSP_ENABLED attribute.

### NI 5442 Arbitrary Waveform Generation

The following figure shows the behavior of the OSP
block during basic arbitrary waveform generation .

[IMAGE alt='image' src='GUID-43D36FE5-31A6-47BB-AC1B-B87EFB58A3A1-a5.gif']

For basic arbitrary waveform generation, disable
onboard signal processing by setting the 
OSP
Enabled property or the 
NIFGEN_ATTR_OSP_ENABLED attribute.

Parent topic:

NI 5442 Common Onboard Signal Processing Applications

<!--NI_TOPIC bundle=ni-fgen path=ni-5442-arbitrary-waveform-mode.html language=enus -->
## TOPIC 00534: NI 5442 Arbitrary Waveform Mode

- bundle_id: `ni-fgen`
- source_path: `ni-5442-arbitrary-waveform-mode.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5442-arbitrary-waveform-mode.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5442 supports Arbitrary Waveform output mode. Arbitrary Waveform mode generates waveforms from user-created/provided waveform arrays of numeric data. The waveform arrays are downloaded to the arbitrary waveform generator onboard memory. Arbitrary Waveform mode also uses memory to store the in

### NI 5442 Arbitrary Waveform Mode

The NI 5442 supports Arbitrary Waveform output mode. Arbitrary Waveform mode generates waveforms from
user-created/provided waveform arrays of numeric data. The waveform
arrays are downloaded to the arbitrary waveform generator onboard
memory. *Arbitrary Waveform mode* also uses memory to
store the instructions for generating waveform sequences in the
onboard memory.

Parent topic:

NI 5442 Output Modes

Related concepts:

- Arbitrary Waveform Output Mode

<!--NI_TOPIC bundle=ni-fgen path=ni-5442-attenuation.html language=enus -->
## TOPIC 00535: NI 5442 Attenuation

- bundle_id: `ni-fgen`
- source_path: `ni-5442-attenuation.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5442-attenuation.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Analog Output path has two passive attenuation sections. Preamplifier attenuation occurs prior to the amplifier, and postamplifier attenuation occurs after the amplifier. The main DAC provides 0 to 3 dB of signal attenuation. Amplitude control is implemented after the DAC. Attenuating the DAC ou

### NI 5442 Attenuation

The Analog Output path has two passive attenuation
sections. *Preamplifier attenuation* occurs prior to the amplifier, and
*postamplifier attenuation* occurs after the amplifier.

The main *DAC* provides 0 to 3 dB of signal attenuation. Amplitude control is implemented after the DAC. Attenuating the DAC output signal allows you to vary the signal amplitude while maintaining the dynamic range of the DAC. You do not lose any bits from the digital representation of the signal and you do not sacrifice dynamic range, as you would if you control amplitude by using smaller data ranges of the DAC. Passive attenuation by preamplifier and postamplifier attenuation is not available if the Direct path is selected.

For the Main path, maximum attenuation is
51 dB. For the Direct path, maximum output attenuation is 3
dB. NI-FGEN automatically determines the correct value of attenuation in dB and configures the attenuation based on the set
gain. The minimum gain setting for the Direct path is 0.354. The
minimum allowable gain setting with NI-FGEN automatically selecting
the Main path is .00282 (gain is a unitless value).

NI-FGEN calculates and sets the correct amount of
attenuation required that corresponds to your NI-FGEN gain setting.
The correct amount of attenuation is implemented in the 
preamplifier and postamplifier attenuation blocks to best achieve
the desired output signal amplitude. You can set the amount of gain
with the Arbitrary Waveform Gain property or the 
NIFGEN_ATTR_ARB_GAIN attribute.

Parent topic:

NI 5442 Waveform Amplitude Control

Related concepts:

- NI 5442 Preamplifier Attenuation
- NI 5442 Postamplifier Attenuation
- NI 5442 DAC Attenuation

<!--NI_TOPIC bundle=ni-fgen path=ni-5442-baseband-interpolation.html language=enus -->
## TOPIC 00536: NI 5442 Baseband Interpolation

- bundle_id: `ni-fgen`
- source_path: `ni-5442-baseband-interpolation.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5442-baseband-interpolation.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the behavior of the OSP block during baseband interpolation. Baseband interpolation allows the OSP block to interpolate signals at a low sample rate up to a high sample rate. Arbitrary pulse shaping of the data can also be done in the FIR filter. For baseband interpolation

### NI 5442 Baseband Interpolation

The following figure shows the behavior of the OSP
block during baseband interpolation.

[IMAGE alt='image' src='GUID-53BB8088-2711-43FD-9CD5-9445611C5FA0-a5.gif']

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
5. Set the corresponding filter parameter.
6. Disable the carrier by setting the 
Carrier
Enabled property or the 
 NIFGEN_ATTR_OSP_CARRIER_ENABLED attribute.
7. Download the low sample rate waveform(s) to the signal
generator.

Parent topic:

NI 5442 Common Onboard Signal Processing Applications

<!--NI_TOPIC bundle=ni-fgen path=ni-5442-basic-onboard-signal-processing-prope.html language=enus -->
## TOPIC 00537: NI 5442 Basic Onboard Signal Processing Properties

- bundle_id: `ni-fgen`
- source_path: `ni-5442-basic-onboard-signal-processing-prope.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5442-basic-onboard-signal-processing-prope.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following properties configure the OSP block: OSP Enabled Data Processing Mode IQ Rate Carrier Enabled Carrier Frequency FIR Filter Type

### NI 5442 Basic Onboard Signal Processing Properties

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

NI 5442 Onboard Signal Processing (OSP)

Related concepts:

- NI 5442 OSP Enabled
- NI 5442 Data Processing Mode
- NI 5442 IQ Rate
- NI 5442 Carrier Frequency
- NI 5442 FIR Filter Type

<!--NI_TOPIC bundle=ni-fgen path=ni-5442-block-diagram.html language=enus -->
## TOPIC 00538: NI 5442 Block Diagram

- bundle_id: `ni-fgen`
- source_path: `ni-5442-block-diagram.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5442-block-diagram.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: This topic contains information about the NI 5442 top-level block diagram and descriptions of the individual blocks. If the device is installed in any slot other than system timing slot of the PXI Express chassis, the NI 5442 can import clocks on the PXI_STAR line. However, PXI Express signal gene

### NI 5442 Block Diagram

This topic contains information about the
NI 5442 top-level block diagram and descriptions of the
individual blocks.

[IMAGE alt='image' src='GUID-900F88F3-7CB0-467A-99DA-19560D6CEEE8-a5.gif']

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
 DAC device after any digital gain or onboard signal
processing is applied.

- The 
 DAC also contains a selectable 
 Digital Filter , which interpolates and filters the
waveform data.
- The waveform data is sent from the 
 DAC to the 
 Analog Output path where the waveform data is filtered and
amplified.

Parent topic:

NI 5442 Theory of Operation

<!--NI_TOPIC bundle=ni-fgen path=ni-5442-burst-trigger-mode.html language=enus -->
## TOPIC 00539: NI 5442 Burst Trigger Mode

- bundle_id: `ni-fgen`
- source_path: `ni-5442-burst-trigger-mode.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5442-burst-trigger-mode.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: In Burst trigger mode, calling the first Start trigger begins waveform generation. The waveform then generates continually. The following table provides more information about waveform generation behavior in Arbitrary Waveform, Arbitrary Sequence, and Frequency List output modes. Output Mode Trigger

### NI 5442 Burst Trigger Mode

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

NI 5442 Trigger Modes

Related concepts:

- NI 5442 Continuous Trigger Mode

<!--NI_TOPIC bundle=ni-fgen path=ni-5442-calibration.html language=enus -->
## TOPIC 00540: NI 5442 Calibration

- bundle_id: `ni-fgen`
- source_path: `ni-5442-calibration.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5442-calibration.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Before shipping your signal generator, NI calibrated your device to ensure that all features are within specifications. Calibration is a set of operations that compares the values indicated by a measuring instrument or measuring system to the corresponding values realized by external standards. You

### NI 5442 Calibration

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

NI 5442 NI 5442 Overview

<!--NI_TOPIC bundle=ni-fgen path=ni-5442-carrier-frequency.html language=enus -->
## TOPIC 00541: NI 5442 Carrier Frequency

- bundle_id: `ni-fgen`
- source_path: `ni-5442-carrier-frequency.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5442-carrier-frequency.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The carrier frequency determines the frequency of the cosine waves (both I and Q) exported from the NCO . You can use the Carrier Frequency property or the NIFGEN_ATTR_OSP_CARRIER_FREQUENCY attribute to set the carrier frequency. This frequency is programmable during signal generation. For I/Q Rates

### NI 5442 Carrier Frequency

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
lower sample rates translate to lower valid carrier rates.

Parent topic:

NI 5442 Basic Onboard Signal Processing Properties

Related concepts:

- NI 5442 Numerically Controlled Oscillator (NCO)
- NI 5442 IQ Rate

<!--NI_TOPIC bundle=ni-fgen path=ni-5442-ch-0-connector.html language=enus -->
## TOPIC 00542: NI 5442 CH 0 Connector

- bundle_id: `ni-fgen`
- source_path: `ni-5442-ch-0-connector.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5442-ch-0-connector.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The CH 0 connector is the analog waveform output terminal. The maximum output levels from this connector depend on the type of load termination. For example, if the output of the device terminates into a 50 Ω load, the maximum output levels are ±1 V, while the maximum output levels are ±2 V when the

### NI 5442 CH 0 Connector

The CH 0 connector is the analog waveform
output terminal. The maximum output levels from this connector
depend on the type of load termination. For example, if the output of the device
terminates into a 50 Ω load, the maximum output levels
are ±1 V, while the maximum output levels are ±2 V when the
device terminates into a high-impedance load (HiZ). This difference
is illustrated in the following figure.

[IMAGE alt='image' src='GUID-FFF99B8B-0FCB-4CBE-AC60-7A642D717D9A-a5.gif']

If the output terminates into any other load, the
levels are defined by the following formula:

V<sub>out</sub>
 = ± [ 
R<sub>L</sub>
 / ( 
R<sub>L</sub>
 + 
R<sub>O</sub>
 ) ] × 2 V

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

The NI 5442 has the ability to configure the
output signal amplitude based on a user-configured load impedance
setting. This capability is desirable when you use the NI 5442
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

NI 5442 Front Panel

<!--NI_TOPIC bundle=ni-fgen path=ni-5442-clk-in-connector.html language=enus -->
## TOPIC 00543: NI 5442 CLK IN Connector

- bundle_id: `ni-fgen`
- source_path: `ni-5442-clk-in-connector.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5442-clk-in-connector.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The CLK IN front panel connector can accept an external Reference clock, external Sample clock, or external Sample clock timebase. Do not change the external clocks while generating waveforms. Only modify the frequency of the external clock before you start the waveform generation or after you sto

### NI 5442 CLK IN Connector

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

NI 5442 Front Panel

Related concepts:

- NI 5442 Phase-Locked Loop Reference Clock

<!--NI_TOPIC bundle=ni-fgen path=ni-5442-clocking-options.html language=enus -->
## TOPIC 00544: NI 5442 Clocking Options

- bundle_id: `ni-fgen`
- source_path: `ni-5442-clocking-options.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5442-clocking-options.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Waveform generation is driven by the Sample clock; depending on your application, some sources may be better choices than others. You can use the following sources for the NI 5442 Sample clock: Internal Sample clock—the onboard clock is used as the Sample clock source and the Sample clock is derived

### NI 5442 Clocking Options

Waveform generation is driven by the Sample clock;
depending on your application, some sources may be better choices
than others. You can use the following sources for the
NI 5442 Sample clock:

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
configure the NI 5442 clock settings for
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

NI 5442 Clocking

Related concepts:

- NI 5442 Internal Sample Clock
- NI 5442 External Sample Clock
- NI 5442 Phase-Locked Loop Reference Clock

<!--NI_TOPIC bundle=ni-fgen path=ni-5442-clocking.html language=enus -->
## TOPIC 00545: NI 5442 Clocking

- bundle_id: `ni-fgen`
- source_path: `ni-5442-clocking.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5442-clocking.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5442 has a Sample clock rate of 10 Hz to 100 MHz. The timing of the device is very flexible, and you have multiple choices for deriving the Sample clock. There are modes for deriving the Sample clock from the internal Sample clock timebase, as well as modes to provide external clocks. You als

### NI 5442 Clocking

The NI 5442 has a Sample clock
rate of 10 Hz to 100 MHz. The timing of the device
is very flexible, and you have multiple choices for deriving the
Sample clock. There are modes for deriving the Sample clock from
the internal Sample clock timebase, as well as modes to provide
external clocks. You also have several choices for providing the
frequency reference for the onboard phase-locked loop.

[IMAGE alt='image' src='GUID-480B4092-E26D-4D74-9435-2573C3898389-a5.gif']

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

NI 5442 Theory of Operation

Related concepts:

- NI 5442 Clocking Options
- NI 5442 Internal Sample Clock
- NI 5442 Phase-Locked Loop Reference Clock
- NI 5442 External Sample Clock
- NI 5442 Exporting Clocks

<!--NI_TOPIC bundle=ni-fgen path=ni-5442-common-onboard-signal-processing-appl.html language=enus -->
## TOPIC 00546: NI 5442 Common Onboard Signal Processing Applications

- bundle_id: `ni-fgen`
- source_path: `ni-5442-common-onboard-signal-processing-appl.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5442-common-onboard-signal-processing-appl.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The OSP block is particularly useful for the following common applications: Arbitrary Waveform Generation Single-Tone Generation Quadrature Upconversion Amplitude Modulation (AM) or Double Sideband Baseband Interpolation

### NI 5442 Common Onboard Signal Processing Applications

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

NI 5442 Onboard Signal Processing (OSP)

Related concepts:

- NI 5442 Arbitrary Waveform Generation
- NI 5442 Single-Tone
- NI 5442 Quadrature Upconversion
- NI 5442 Amplitude Modulation (AM) or Double Sideband
- NI 5442 Baseband Interpolation

<!--NI_TOPIC bundle=ni-fgen path=ni-5442-continuous-trigger-mode.html language=enus -->
## TOPIC 00547: NI 5442 Continuous Trigger Mode

- bundle_id: `ni-fgen`
- source_path: `ni-5442-continuous-trigger-mode.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5442-continuous-trigger-mode.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The waveform you downloaded generates continuously after receiving one Start trigger. All Start triggers after the first Start trigger are ignored. The following table provides more information about waveform generation behavior in Arbitrary Waveform, Arbitrary Sequence, and Frequency List output mo

### NI 5442 Continuous Trigger Mode

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

NI 5442 Trigger Modes

<!--NI_TOPIC bundle=ni-fgen path=ni-5442-dac-attenuation.html language=enus -->
## TOPIC 00548: NI 5442 DAC Attenuation

- bundle_id: `ni-fgen`
- source_path: `ni-5442-dac-attenuation.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5442-dac-attenuation.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The main DAC output can be fine-tuned for attenuation, which provides 0 to 3 dB of the Analog Output path signal attenuation. This fine-tuning of the main DAC attenuation is performed by the gain DAC. Adjust the gain DAC using the Gain DAC Value property or the NIFGEN_ATTR_GAIN_DAC_VALUE attribute.

### NI 5442 DAC Attenuation

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

NI 5442 Attenuation

<!--NI_TOPIC bundle=ni-fgen path=ni-5442-data-mask.html language=enus -->
## TOPIC 00549: NI 5442 Data Mask

- bundle_id: `ni-fgen`
- source_path: `ni-5442-data-mask.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5442-data-mask.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The signal generator supports analog data masks and static values. The data mask allows you to shield bits of the data to be replaced with the corresponding static value bits. For example, a mask of 0xFF00 and a static value of 0xAAAA applied to a DC waveform with a value of 0x1111 produces a DC wav

### NI 5442 Data Mask

The signal generator supports analog
data masks and static values. The data mask allows you to shield
bits of the data to be replaced with the corresponding static value
bits. For example, a mask of 0xFF00 and a static value of 0xAAAA
applied to a DC waveform with a value of 0x1111 produces a DC
waveform with a value of 0x11AA.

NI-FGEN supports separate and independent analog
and digital data masks and static values. The analog data mask and
analog static value apply to the digital data applied to the DAC,
and ultimately to the signal on the analog output terminal. You can configure an analog data mask by calling the 
Analog Data
Mask or 
Analog
Static Value properties or the 
NIFGEN_ATTR_ANALOG_DATA_MASK and 
NIFGEN_ATTR_ANALOG_STATIC_VALUE attributes.

Parent topic:

NI 5442 NI 5442 Overview

<!--NI_TOPIC bundle=ni-fgen path=ni-5442-data-processing-mode.html language=enus -->
## TOPIC 00550: NI 5442 Data Processing Mode

- bundle_id: `ni-fgen`
- source_path: `ni-5442-data-processing-mode.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5442-data-processing-mode.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Data Processing mode determines whether the OSP block uses only the I signal path to generate waveforms or uses the I and Q signal paths to generate complex waveforms. If the waveform data is configured for real data points by setting the Data Processing Mode property or the NIFGEN_ATTR_OSP_DATA_PRO

### NI 5442 Data Processing Mode

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

NI 5442 Basic Onboard Signal Processing Properties

<!--NI_TOPIC bundle=ni-fgen path=ni-5442-dc-offset.html language=enus -->
## TOPIC 00551: NI 5442 DC Offset

- bundle_id: `ni-fgen`
- source_path: `ni-5442-dc-offset.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5442-dc-offset.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5442 supports a DC offset before the attenuation chain that affects the maximum value of DC offset for a given gain setting. This preattenuation architecture requires two rules for setting the DC offset: The magnitude of the maximum value of offset can be no more than ½ of the configured gain

### NI 5442 DC Offset

The NI 5442 supports a DC offset before the attenuation chain that affects the maximum value of DC offset for a given gain setting. This preattenuation architecture requires two rules for setting the DC offset:

1. The magnitude of the maximum value of offset can be no more than ½ of the configured gain setting for the NI 5442.
2. The waveform maximum plus the offset must not exceed ±1 V
 into 50 Ω; if it does, the waveform is clipped. For example, if you have set a gain of .75
 , which corresponds to an amplitude of .75 V
 , and the waveform is a sine wave using the full range of the DAC, the maximum DC offset you can apply without clipping the sine wave is ±.25 V
 . At this point, output voltages of the sine waveform have reached the maximum amplitude that the device supports. If you increase the DC offset further, the top portion of the waveform at 1 V
 is clipped.

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

NI 5442 Waveform Amplitude Control

<!--NI_TOPIC bundle=ni-fgen path=ni-5442-digital-filter.html language=enus -->
## TOPIC 00552: NI 5442 Digital Filter

- bundle_id: `ni-fgen`
- source_path: `ni-5442-digital-filter.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5442-digital-filter.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The main DAC provides an internal digital filter. When digital filtering is enabled, the main DAC runs at a faster rate, referred to as the effective sample rate (ESR). The waveform data transfers to the main DAC at the configured Sample clock rate; the internal digital filter interpolates by a fact

### NI 5442 Digital Filter

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

NI 5442 Filtering Effects

Related concepts:

- NI 5442 Onboard Signal Processing (OSP)
- NI 5442 IQ Rate
- Filtering and Interpolation
- Aliased Images

<!--NI_TOPIC bundle=ni-fgen path=ni-5442-digital-gain.html language=enus -->
## TOPIC 00553: NI 5442 Digital Gain

- bundle_id: `ni-fgen`
- source_path: `ni-5442-digital-gain.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5442-digital-gain.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Digital gain multiplies waveform data by a factor you specify in the Digital Gain property or the NIFGEN_ATTR_DIGITAL_GAIN attribute before converting the data to an analog signal in the DAC. Digital gain can be changed during generation without the glitches caused by switching that are common when

### NI 5442 Digital Gain

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

NI 5442 Waveform Amplitude Control

<!--NI_TOPIC bundle=ni-fgen path=ni-5442-direct-dma.html language=enus -->
## TOPIC 00554: NI 5442 Direct DMA

- bundle_id: `ni-fgen`
- source_path: `ni-5442-direct-dma.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5442-direct-dma.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Direct DMA can transfer waveform data to the signal generator onboard memory at rates well beyond the typical 5 to 30 MB/s range in a standard PC-based architecture. To achieve such high rates, direct DMA establishes a direct connection between the signal generator onboard memory and a specialized w

### NI 5442 Direct DMA

*Direct DMA* can transfer waveform data to the signal generator onboard memory at rates well beyond the typical 5 to 30 MB/s range in a standard PC-based architecture. To achieve such high rates, direct DMA establishes a direct connection between the signal generator onboard memory and a specialized waveform data source. Direct DMA is commonly used to *stream* waveform data from disk at data rates of 100+ MB/sec. Conduant's StreamStor™ products are one example of direct DMA-compatible data sources.

#### Related Topics

*Configuring an Application for Direct DMA*

*DMA Fundamentals*

Parent topic:

NI 5442 Streaming

Related concepts:

- Direct DMA
- Streaming
- Configuring Your Application for Direct DMA

<!--NI_TOPIC bundle=ni-fgen path=ni-5442-events.html language=enus -->
## TOPIC 00555: NI 5442 Events

- bundle_id: `ni-fgen`
- source_path: `ni-5442-events.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5442-events.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use events to indicate when a specific hardware condition has been met on the NI 5442. An event is a signal generated by the NI device at a device state. The NI 5442 supports Ready for Start, Started, Data Marker, Marker, and Done events. The NI 5442 also supports the use of event delays. Re

### NI 5442 Events

You can use *events* to indicate when a specific
hardware condition has been met on the NI 5442. An event is a
signal generated by the NI device at a device state. The NI 5442
supports Ready for Start, Started, *Data Marker*, *Marker*, and Done
events. The NI 5442 also supports the use of *event delays*.

#### Related Topics

*Creating a Marker
Event*

*Creating a Data Marker
Event*

Parent topic:

NI 5442 NI 5442 Overview

Related concepts:

- Events
- Data Marker Events
- Marker Events
- Event Delays
- Creating a Marker Event
- Creating a Data Marker Event

<!--NI_TOPIC bundle=ni-fgen path=ni-5442-exporting-clocks.html language=enus -->
## TOPIC 00556: NI 5442 Exporting Clocks

- bundle_id: `ni-fgen`
- source_path: `ni-5442-exporting-clocks.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5442-exporting-clocks.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5442 provides resources for exporting your clocks and multiple destinations for routing. The following table shows the available clock signals that can be routed to devices external to the signal generator and the destination options. Clock to be Exported Destination Options Sample Clock PFI

### NI 5442 Exporting Clocks

The NI 5442 provides resources for exporting your clocks and multiple destinations for
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
NI 5442 allows you to export your clocks 
so that other devices can share the timing of the NI 5442. The following sections describe the possible clock routing configurations.

#### Sample Clock

The Sample clock can be routed to the
PFI <0..1> front panel SMB connectors, PXI_Trig<0..6>
lines on the PXI trigger bus, or the RTSI<0..6> lines.

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
RTSI<0..6> lines.

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

NI 5442 Clocking

<!--NI_TOPIC bundle=ni-fgen path=ni-5442-exporting-signals.html language=enus -->
## TOPIC 00557: NI 5442 Exporting Signals

- bundle_id: `ni-fgen`
- source_path: `ni-5442-exporting-signals.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5442-exporting-signals.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The signal generator contains seven PXI trigger lines that are available for sending signal generator-specific information to other devices that have PXI trigger bus connectors. The signal generator has connectors on the front panel to route signals to devices external to the PXI Express chassis. Th

### NI 5442 Exporting Signals

The signal generator contains seven PXI trigger
lines that are available for sending signal generator-specific
information to other devices that have PXI trigger bus
connectors.

The signal generator has connectors on the front
panel to route signals to devices external to the PXI Express
chassis. The following table shows the signals available for export
and the lines they can be routed to. To determine all possible
signal routes for your device, refer to 
*Signal Routing*.

|  |  | Destination |  |
| --- | --- | --- | --- |
| PXI_TRIG<0..6> | PFI 0 andPFI 1 Connectors |  |  |
| Exported Clocks,Triggers, and Events | Sample Clock | Yes | Yes |
| Sample Clock Timebase | Yes | Yes |  |
| PLL Reference Source | Yes | Yes |  |
| Out Start trigger | Yes | Yes |  |
| Marker Event | Yes | Yes |  |

Sample Clock

Note

Sample Clock Timebase

Note

Reference clock–A clock signal
that is only available when a Reference clock source for the PLLs has been
configured. The clock is the source selected as the PLL Reference
clock source.

Start trigger out–A signal generated by the
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
Generation mode waveform generation to any of the PXI trigger lines
or front panel connectors.
- The signal generator Start trigger output signal to other
devices through any of the PXI trigger lines or front panel
connectors.
- The signal generator Sample clock signal to other devices
through any of the PXI trigger lines or front panel
connectors.
- The PLL Reference clock source to other devices through any of
the PXI trigger lines or front panel connectors.

In NI-FGEN, the PXI trigger lines are referred to
as RTSI<0..6>. The correlation between PXI_TRIG< 
x> and RTSI< 
x> is one to one. For more information about
configuring and routing the device internal signals, refer to the 
niFgen Export Signal VI
or the 
niFgen_ExportSignal function.

Parent topic:

NI 5442 NI 5442 Overview

Related concepts:

- NI 5442 Signal Routing

<!--NI_TOPIC bundle=ni-fgen path=ni-5442-external-sample-clock.html language=enus -->
## TOPIC 00558: NI 5442 External Sample Clock

- bundle_id: `ni-fgen`
- source_path: `ni-5442-external-sample-clock.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5442-external-sample-clock.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5442 can accept an external clock to directly drive the Sample clock. When using an external Sample clock, the frequency stability and accuracy of the Sample clock is determined by the provided external Sample clock. The following figure shows possible Sample Clock paths. You can set the cloc

### NI 5442 External Sample Clock

The NI 5442 can accept an
external clock to directly drive the Sample clock. When using an
external Sample clock, the frequency stability and accuracy of the
Sample clock is determined by the provided external Sample
clock.

The following figure shows possible Sample
Clock paths.

[IMAGE alt='image' src='GUID-FB8AB24C-DDB8-4156-9B5E-33D383DC03F4-a5.gif']

You can set the clock source by calling the
niFgen
Configure Sample Clock Source VI or the 
niFgen_ConfigureSampleClockSource function.

niFgen_ConfigureSampleRate

Note

device specifications

#### External Sample Clock Considerations

The NI 5442 incorporates
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
reprograms the NI 5442 for the new settings,
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

NI 5442 Clocking Options

Related concepts:

- NI 5442 Sample Clock Considerations

<!--NI_TOPIC bundle=ni-fgen path=ni-5442-filtering-and-interpolation.html language=enus -->
## TOPIC 00559: NI 5442 Filtering and Interpolation

- bundle_id: `ni-fgen`
- source_path: `ni-5442-filtering-and-interpolation.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5442-filtering-and-interpolation.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The filtering and interpolation stage of the OSP block increases the effective sample rate of the signal generator while protecting the frequency spectrum of the interpolated data from images. This protection occurs when the data passes through a lowpass filter after zero stuffing. The frequency res

### NI 5442 Filtering and Interpolation

The filtering and interpolation stage of the 
*OSP* block increases the effective
sample rate of the signal generator while protecting the frequency
spectrum of the interpolated data from images. This protection
occurs when the data passes through a lowpass filter after zero
stuffing. The frequency response of the low pass filter can be
changed with the 
Filter
Type property or the 
NIFGEN_ATTR_OSP_FIR_FILTER_TYPE attribute.

[IMAGE alt='image' src='GUID-C1BDF7AF-B534-458E-A2A9-BA1D9A6DD7BE-a5.gif']

Parent topic:

NI 5442 Onboard Signal Processing Components

Related concepts:

- NI 5442 Onboard Signal Processing (OSP)

<!--NI_TOPIC bundle=ni-fgen path=ni-5442-filtering-effects.html language=enus -->
## TOPIC 00560: NI 5442 Filtering Effects

- bundle_id: `ni-fgen`
- source_path: `ni-5442-filtering-effects.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5442-filtering-effects.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The delay from the time at which the device receives a trigger to the time at which the analog output signal is generated increases if the digital and/or analog filters in the Analog Output path are enabled. In the case of digital filtering, delay also increases with increase in interpolation. Enabl

### NI 5442 Filtering Effects

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

NI 5442 Analog Output

Related concepts:

- NI 5442 Analog Output
- NI 5442 Onboard Signal Processing (OSP)
- NI 5442 Digital Filter

<!--NI_TOPIC bundle=ni-fgen path=ni-5442-filtering-effects_2.html language=enus -->
## TOPIC 00561: NI 5442 Filtering Effects

- bundle_id: `ni-fgen`
- source_path: `ni-5442-filtering-effects_2.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5442-filtering-effects_2.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The delay from the time at which the device receives a trigger to the time at which the analog output signal is generated increases if the digital and/or analog filters in the Analog Output path are enabled. In the case of digital filtering, delay also increases with increase in interpolation. Enabl

### NI 5442 Filtering Effects

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

NI 5442 Triggering

<!--NI_TOPIC bundle=ni-fgen path=ni-5442-fir-filter-type-flat.html language=enus -->
## TOPIC 00562: NI 5442 FIR Filter Type: Flat

- bundle_id: `ni-fgen`
- source_path: `ni-5442-fir-filter-type-flat.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5442-fir-filter-type-flat.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Passband Value: 0.40 This lowpass filter is designed to give a flat response until the passband value. The passband value is a fraction of the I/Q Rate coming into the FIR filter. Use the Flat Filter Passband property or the NIFGEN_ATTR_OSP_FIR_FILTER_FLAT_PASSBAND attribute to set the passband valu

### NI 5442 FIR Filter Type: Flat

Passband Value: 0.40

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

[IMAGE alt='image' src='GUID-1343D8E2-F83F-4310-A25D-36DA2801503C-a5.gif']

Parent topic:

NI 5442 FIR Filter Types

Related concepts:

- NI 5442 I/Q Rate Controller

<!--NI_TOPIC bundle=ni-fgen path=ni-5442-fir-filter-type-raised-cosine.html language=enus -->
## TOPIC 00563: NI 5442 FIR Filter Type: Raised Cosine

- bundle_id: `ni-fgen`
- source_path: `ni-5442-fir-filter-type-raised-cosine.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5442-fir-filter-type-raised-cosine.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Alpha Values: 0.1 to 0.4 This lowpass filter is commonly used in communications applications. The passband of the raised cosine filter with the roll-off factor, α, stops at 0.5 × (1 − α) times the I/Q Rate. The stopband of the raised cosine filter begins at 0.5 × (1 + α) times the I/Q Rate. The tran

### NI 5442 FIR Filter Type: Raised Cosine

Alpha Values: 0.1 to 0.4

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

Parent topic:

NI 5442 FIR Filter Types

Related concepts:

- NI 5442 I/Q Rate Controller

<!--NI_TOPIC bundle=ni-fgen path=ni-5442-fir-filter-type-root-raised-cosine.html language=enus -->
## TOPIC 00564: NI 5442 FIR Filter Type: Root Raised Cosine

- bundle_id: `ni-fgen`
- source_path: `ni-5442-fir-filter-type-root-raised-cosine.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5442-fir-filter-type-root-raised-cosine.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Alpha Values: 0.1 to 0.4 This lowpass filter is commonly used in communications applications. The passband of the root raised cosine filter with the roll-off factor, α, stops at 0.5 × (1 − α) times the I/Q Rate. The stopband of the root raised cosine filter begins at 0.5 × (1 + α) times the I/Q Rate

### NI 5442 FIR Filter Type: Root Raised Cosine

Alpha Values: 0.1 to 0.4

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
Raised Cosine Filter Alpha property or the 
NIFGEN_ATTR_OSP_FIR_FILTER_RAISED_COSINE_ALPHA attribute to set the 
α value.

The following diagram shows an ideal root raised
cosine filter response with an 
α of 0.5. The frequency
axis is scaled as a fraction of the 
I/Q
Rate.

[IMAGE alt='image' src='GUID-AAD8865C-5B03-4E67-8E39-2FD2389E6EBA-a5.gif']

Parent topic:

NI 5442 FIR Filter Types

Related concepts:

- NI 5442 I/Q Rate Controller

<!--NI_TOPIC bundle=ni-fgen path=ni-5442-fir-filter-type.html language=enus -->
## TOPIC 00565: NI 5442 FIR Filter Type

- bundle_id: `ni-fgen`
- source_path: `ni-5442-fir-filter-type.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5442-fir-filter-type.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The FIR Filter type determines the spectral shaping of the data done in the FIR filter. Use the FIR Filter Type property or the NIFGEN_ATTR_OSP_FIR_FILTER_TYPE attribute to set the FIR filter type. The following filter types are supported: Flat Raised Cosine Root Raised Cosine

### NI 5442 FIR Filter Type

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

Parent topic:

NI 5442 Basic Onboard Signal Processing Properties

Related concepts:

- NI 5442 FIR Filter Types
- NI 5442 FIR Filter Type: Flat
- NI 5442 FIR Filter Type: Raised Cosine
- NI 5442 FIR Filter Type: Root Raised Cosine

<!--NI_TOPIC bundle=ni-fgen path=ni-5442-fir-filter-types.html language=enus -->
## TOPIC 00566: NI 5442 FIR Filter Types

- bundle_id: `ni-fgen`
- source_path: `ni-5442-fir-filter-types.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5442-fir-filter-types.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: There are a number of built-in low-pass pulse-shaping filters available in NI-FGEN. Because the coefficients are scaled for unity-gain, the filters may overflow if transients (such as step response) are presented at the input of the filter. Use the Filter Type property or the NIFGEN_ATTR_OSP_FIR_FIL

### NI 5442 FIR Filter Types

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

Parent topic:

NI 5442 Onboard Signal Processing Components

Related concepts:

- NI 5442 FIR Filter Type
- NI 5442 FIR Filter Type: Flat
- NI 5442 FIR Filter Type: Raised Cosine
- NI 5442 FIR Filter Type: Root Raised Cosine

<!--NI_TOPIC bundle=ni-fgen path=ni-5442-frequency-list-mode.html language=enus -->
## TOPIC 00567: NI 5442 Frequency List Mode

- bundle_id: `ni-fgen`
- source_path: `ni-5442-frequency-list-mode.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5442-frequency-list-mode.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Frequency List output mode allows you to configure the device to generate a standard function using a list of frequencies you define. A frequency list is composed of steps, each one with a frequency/duration pair. Frequency lists are commonly used for frequency hops and sweeps and frequency shift ke

### NI 5442 Frequency List Mode

*Frequency List output mode* allows you to configure the
device to generate a standard function using a list of frequencies
you define. A frequency list is composed of steps, each one with a
frequency/duration pair. Frequency lists are commonly used for
*frequency hops and sweeps* and frequency shift keying (FSK) applications.

Parent topic:

NI 5442 Output Modes

Related concepts:

- Frequency List Mode
- Frequency Hopping and Sweeping

<!--NI_TOPIC bundle=ni-fgen path=ni-5442-front-panel.html language=enus -->
## TOPIC 00568: NI 5442 Front Panel

- bundle_id: `ni-fgen`
- source_path: `ni-5442-front-panel.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5442-front-panel.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the NI PXIe-5442 front panel. This front panel has four SMB connectors. The ACCESS and ACTIVE LEDs indicate the status of the PXI module. The CH 0 SMB connector is the analog output from which arbitrary waveforms are generated. The CLK IN SMB connector provides the device

### NI 5442 Front Panel

The following figure shows the NI PXIe-5442 front panel. This front panel has
four SMB connectors.

[IMAGE alt='image' src='GUID-3C56D9FA-4227-40AF-99DE-7CF8CB177EFE-a5.gif']

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

Parent topic:

NI 5442 NI 5442 Overview

Related concepts:

- NI 5442 ACCESS and ACTIVE LEDs
- NI 5442 CH 0 Connector
- NI 5442 CLK IN Connector
- NI 5442 PFI Connectors

<!--NI_TOPIC bundle=ni-fgen path=ni-5442-hardware-state-diagram.html language=enus -->
## TOPIC 00569: NI 5442 Hardware State Diagram

- bundle_id: `ni-fgen`
- source_path: `ni-5442-hardware-state-diagram.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5442-hardware-state-diagram.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following diagram shows the hardware states of the signal generator. The signal generator can be in one of the following six basic states during the course of operation. Idle—The device is not generating a waveform. All session properties or attributes can be programmed in the Idle state. In the

### NI 5442 Hardware State Diagram

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

NI 5442 Theory of Operation

Related concepts:

- Programming State Model

<!--NI_TOPIC bundle=ni-fgen path=ni-5442-i-q-combiner.html language=enus -->
## TOPIC 00570: NI 5442 I/Q Combiner

- bundle_id: `ni-fgen`
- source_path: `ni-5442-i-q-combiner.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5442-i-q-combiner.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: When the waveform data is configured for complex data points by setting the Data Processing Mode property or the NIFGEN_ATTR_OSP_DATA_PROCESSING_MODE attribute, the I and Q data streams are combined after they are multiplied with the carriers. The I/Q combiner is implemented as I [p] − Q [p]. The co

### NI 5442 I/Q Combiner

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

NI 5442 Onboard Signal Processing Components

Related concepts:

- NI 5442 Quadrature Upconversion

<!--NI_TOPIC bundle=ni-fgen path=ni-5442-i-q-rate-controller.html language=enus -->
## TOPIC 00571: NI 5442 I/Q Rate Controller

- bundle_id: `ni-fgen`
- source_path: `ni-5442-i-q-rate-controller.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5442-i-q-rate-controller.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The I/Q rate component pulls the data from the generation engine such that a new sample is returned once every Total_OSP_Interpolation Sample clocks. The Total_OSP_Interpolation is the amount of interpolation applied within the Filtering and Interpolation component, and does not include the DAC in

### NI 5442 I/Q Rate Controller

Note

Parent topic:

NI 5442 Onboard Signal Processing Components

<!--NI_TOPIC bundle=ni-fgen path=ni-5442-internal-sample-clock.html language=enus -->
## TOPIC 00572: NI 5442 Internal Sample Clock

- bundle_id: `ni-fgen`
- source_path: `ni-5442-internal-sample-clock.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5442-internal-sample-clock.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5442 can derive a Sample clock from its main internal timing source—the onboard Sample clock timebase. The signal generator provides a high-precision 100 MHz Voltage Controlled Crystal Oscillator (VCXO) clock source for the Sample clock timebase. As shown in the following figure, the Sample c

### NI 5442 Internal Sample Clock

The NI 5442 can derive a Sample
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

NI 5442 Clocking Options

<!--NI_TOPIC bundle=ni-fgen path=ni-5442-iq-rate.html language=enus -->
## TOPIC 00573: NI 5442 IQ Rate

- bundle_id: `ni-fgen`
- source_path: `ni-5442-iq-rate.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5442-iq-rate.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The IQ Rate property or the NIFGEN_ATTR_OSP_IQ_RATE attribute defines the rate at which data is processed by the OSP block. If the waveform data is configured for real data points by setting the Data Processing Mode property or the NIFGEN_ATTR_OSP_DATA_PROCESSING_MODE attribute, then it is the rate

### NI 5442 IQ Rate

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

NIFGEN_ATTR_ARB_SAMPLE_RATE

Note

NIFGEN_ATTR_OSP_ENABLED

NIFGEN_ATTR_ARB_SAMPLE_RATE

Parent topic:

NI 5442 Basic Onboard Signal Processing Properties

<!--NI_TOPIC bundle=ni-fgen path=ni-5442-memory-fragmentation.html language=enus -->
## TOPIC 00574: NI 5442 Memory Fragmentation

- bundle_id: `ni-fgen`
- source_path: `ni-5442-memory-fragmentation.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5442-memory-fragmentation.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: When storing multiple waveforms in NI 5442 memory, fragmentation can become a problem. Both waveforms and instructions are stored in NI 5442 memory in contiguous blocks. These blocks are allocated in multiples of 128 bytes, and they are written in the order that you configure them. Fragmentation occ

### NI 5442 Memory Fragmentation

When storing multiple waveforms in
NI 5442 memory, fragmentation can become a
problem. Both waveforms and instructions are stored in
NI 5442 memory in contiguous blocks. These
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

NI 5442 Onboard Memory

<!--NI_TOPIC bundle=ni-fgen path=ni-5442-ni-5442-overview.html language=enus -->
## TOPIC 00575: NI 5442 NI 5442 Overview

- bundle_id: `ni-fgen`
- source_path: `ni-5442-ni-5442-overview.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5442-ni-5442-overview.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5442 is a 100 MS/s, 16-bit arbitrary waveform generator for the PXI Express platform with the following features: Onboard signal processing (OSP) with 40 MHz of digital upconverter bandwidth One 16-bit resolution output channel Output amplitude with a maximum of 2 V[pk-pk] into a 50 Ω load Of

### NI 5442 NI 5442 Overview

The NI 5442 is a 100 MS/s, 16-bit arbitrary
waveform generator for the PXI Express platform with the following
features:

- Onboard signal processing (OSP)
with 40 MHz of digital upconverter bandwidth
- One 16-bit resolution output channel
- Output amplitude with a maximum of 2 V pk-pk into a 50 Ω load
- Offset up to ±25% of V pk-pk
- Up to 43 MHz sine waveform output
- Up to 25 MHz square waveform output
- Up to 5 MHz triangle, ramp-up, and ramp-down waveform
output
- Software-selectable output impedances (50 or
75 Ω) and output attenuation levels from 0 to
51 dB
- High-Resolution and Divide by 
 N internal clocking modes, as well as external clocking
options
- PLL synchronization to external clocks or to
PXI_CLK10
- TClk synchronization
- Sample rate up to 100 MS/s (105 MHz with external
clock)
- Up to 512 MB of onboard waveform memory
- Waveform linking and looping for arbitrary waveform
generation
- Digital and analog filters
- Digital gain
- Four external trigger inputs
- Four Marker events as trigger output
- PXI trigger lines

All NI 5442 devices follow industry-standard
Plug and Play specifications for the PXI Express bus and offer
seamless integration with compliant systems.

Parent topic:

Devices

Related concepts:

- NI 5442 Onboard Signal Processing (OSP)

<!--NI_TOPIC bundle=ni-fgen path=ni-5442-numerically-controlled-oscillator-nco.html language=enus -->
## TOPIC 00576: NI 5442 Numerically Controlled Oscillator (NCO)

- bundle_id: `ni-fgen`
- source_path: `ni-5442-numerically-controlled-oscillator-nco.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5442-numerically-controlled-oscillator-nco.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The numerically controlled oscillator (NCO) is a digital circuit that creates two cosine waves of the same frequency with two potentially independent phases. You can use the Carrier Frequency property or the NIFGEN_ATTR_OSP_CARRIER_FREQUENCY attribute to set the carrier frequency. The I phase cosine

### NI 5442 Numerically Controlled Oscillator (NCO)

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

NI 5442 Onboard Signal Processing Components

Related concepts:

- NI 5442 Quadrature Upconversion

<!--NI_TOPIC bundle=ni-fgen path=ni-5442-onboard-memory.html language=enus -->
## TOPIC 00577: NI 5442 Onboard Memory

- bundle_id: `ni-fgen`
- source_path: `ni-5442-onboard-memory.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5442-onboard-memory.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5442 signal generator uses an onboard memory that is 16-bits wide. The minimum standard memory size for the NI 5442 is 8 MB which translates to 8,338,608 usable bytes. With the minimum standard memory size, you can store very long waveforms on the device and obtain reliable waveform generatio

### NI 5442 Onboard Memory

The NI 5442 signal generator
uses an onboard memory that is 16-bits wide. The minimum standard
memory size for the NI 5442 is 8 MB
which translates to 8,338,608 usable bytes. With the minimum
standard memory size, you can store very long waveforms on the
device and obtain reliable waveform generation at full sample rate
of 100 MS/s. The
NI 5442 is also available with higher memory options
of 32 MB, 256 MB, and 512 MB.

The onboard memory is a single large memory area that stores both waveforms and sequence instructions to generate
the waveforms. The instructions for a complicated sequence can
occupy a significant portion of memory. The architecture of the
NI 5442 allows you to load multiple
waveforms and multiple sequence instructions into the memory. The
following diagram illustrates NI 5442
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

NI 5442 Theory of Operation

<!--NI_TOPIC bundle=ni-fgen path=ni-5442-onboard-signal-processing-components.html language=enus -->
## TOPIC 00578: NI 5442 Onboard Signal Processing Components

- bundle_id: `ni-fgen`
- source_path: `ni-5442-onboard-signal-processing-components.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5442-onboard-signal-processing-components.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the block diagram of the OSP block. The OSP block includes the following components: Prefilter Gain and Prefilter Offset I/Q Rate Controller Filtering and Interpolation NCO (Numerically Controlled Oscillator) I/Q Combiner

### NI 5442 Onboard Signal Processing Components

The following figure shows the block diagram of the
OSP block.

[IMAGE alt='image' src='GUID-5F7AC982-603C-4F76-9F6B-E06811383E85-a5.gif']

The OSP block includes the following
components:

- Prefilter Gain and
Prefilter Offset

- I/Q Rate Controller
- Filtering and
Interpolation

- NCO (Numerically Controlled
Oscillator)
- I/Q Combiner

Parent topic:

NI 5442 Onboard Signal Processing (OSP)

Related concepts:

- NI 5442 Prefilter Gain and Offset
- NI 5442 I/Q Rate Controller
- NI 5442 Filtering and Interpolation
- NI 5442 Numerically Controlled Oscillator (NCO)
- NI 5442 I/Q Combiner

<!--NI_TOPIC bundle=ni-fgen path=ni-5442-onboard-signal-processing-osp.html language=enus -->
## TOPIC 00579: NI 5442 Onboard Signal Processing (OSP)

- bundle_id: `ni-fgen`
- source_path: `ni-5442-onboard-signal-processing-osp.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5442-onboard-signal-processing-osp.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The onboard signal processing (OSP) block is a general-purpose block of digital signal processing components that can be used to modify the data pulled from waveform memory during generation. The OSP block can be used for the following common applications: Arbitrary Waveform Generation Single-Tone G

### NI 5442 Onboard Signal Processing (OSP)

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

NI 5442 Theory of Operation

Related concepts:

- NI 5442 Arbitrary Waveform Generation
- NI 5442 Single-Tone
- NI 5442 Quadrature Upconversion
- NI 5442 Amplitude Modulation (AM) or Double Sideband
- NI 5442 Baseband Interpolation

<!--NI_TOPIC bundle=ni-fgen path=ni-5442-osp-enabled.html language=enus -->
## TOPIC 00580: NI 5442 OSP Enabled

- bundle_id: `ni-fgen`
- source_path: `ni-5442-osp-enabled.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5442-osp-enabled.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The OSP Enabled property or the NIFGEN_ATTR_OSP_ENABLED attribute activates the functionality of the OSP block. To use any of the features in the OSP block, you must enable onboard signal processing by setting this property or attribute.

### NI 5442 OSP Enabled

The 
OSP
Enabled property or the 
NIFGEN_ATTR_OSP_ENABLED attribute activates the functionality of the OSP block. To use
any of the features in the OSP block, you must enable onboard
signal processing by setting this property or attribute.

Parent topic:

NI 5442 Basic Onboard Signal Processing Properties

<!--NI_TOPIC bundle=ni-fgen path=ni-5442-output-enable.html language=enus -->
## TOPIC 00581: NI 5442 Output Enable

- bundle_id: `ni-fgen`
- source_path: `ni-5442-output-enable.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5442-output-enable.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can disable the analog output signal at the CH 0 connector by controlling the output enable relay, as shown in the following figure. When the output enable relay is disabled, the output signal is connected to ground through a 50 or 75 Ω resistance depending on the output impedance selected. The

### NI 5442 Output Enable

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

NI 5442 Analog Output

Related concepts:

- NI 5442 Analog Output

<!--NI_TOPIC bundle=ni-fgen path=ni-5442-output-impedance.html language=enus -->
## TOPIC 00582: NI 5442 Output Impedance

- bundle_id: `ni-fgen`
- source_path: `ni-5442-output-impedance.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5442-output-impedance.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5442 Analog Output path is designed to have an output impedance of 50 Ω from the Output Enable relay looking back towards the Main DAC. There is a selectable 25 Ω resistance that can be switched into the Analog Output path between the Output Enable relay and the CH 0 connector for application

### NI 5442 Output Impedance

The NI 5442 Analog Output path is
designed to have an output impedance of 50 Ω from the
*Output Enable relay* looking back towards the Main DAC. There is a
selectable 25 Ω resistance that can be switched into the
Analog Output path between the Output Enable relay and the CH
0 connector for applications requiring a 75 Ω
impedance. Most applications use a load impedance of
50 Ω, but applications such as video testing, require
75 Ω. Refer to the following figure.

[IMAGE alt='image' src='GUID-235B4D87-8DC7-40D4-BF4D-44312DF3D738-a5.gif']

If the load impedance is a high impedance (~1
MΩ), you may see output levels up to twice the selected
output value for a matched input/output impedance. These levels can
be as high as 4 V<sub>pk-pk</sub> for the Main path. Normally, the
output levels increase as the load impedance increases. The
NI 5442 can compensate for different load impedance
values. Refer to 
*CH 0 Connector* for more
information.

niFgen_ConfigureOutputImpedance

Note

Parent topic:

NI 5442 Analog Output

Related concepts:

- NI 5442 Output Enable
- NI 5442 CH 0 Connector

<!--NI_TOPIC bundle=ni-fgen path=ni-5442-output-modes.html language=enus -->
## TOPIC 00583: NI 5442 Output Modes

- bundle_id: `ni-fgen`
- source_path: `ni-5442-output-modes.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5442-output-modes.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The output mode of your signal generator determines the type of waveforms your signal generator produces. To select an output mode, set the Output Mode parameter of the niFgen Configure Output Mode VI or the niFgen_ConfigureOutputMode function.

### NI 5442 Output Modes

The output mode of your signal generator determines the type of
waveforms your signal generator produces. To select an output mode,
set the 
Output Mode parameter of the 
niFgen
Configure Output Mode VI or the 
niFgen_ConfigureOutputMode function.

Parent topic:

NI 5442 Waveform Generation

<!--NI_TOPIC bundle=ni-fgen path=ni-5442-pfi-connectors.html language=enus -->
## TOPIC 00584: NI 5442 PFI Connectors

- bundle_id: `ni-fgen`
- source_path: `ni-5442-pfi-connectors.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5442-pfi-connectors.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: PFI 0 and PFI 1 are bidirectional connectors. As an input, the PFI terminals can accept a trigger from an external source that can start or step through waveform generation. As an output, the PFI lines route a signal out from the following sources: Marker events Start trigger PLL Reference clock sou

### NI 5442 PFI Connectors

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

NI 5442 Front Panel

<!--NI_TOPIC bundle=ni-fgen path=ni-5442-phase-locked-loop-reference-clock.html language=enus -->
## TOPIC 00585: NI 5442 Phase-Locked Loop Reference Clock

- bundle_id: `ni-fgen`
- source_path: `ni-5442-phase-locked-loop-reference-clock.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5442-phase-locked-loop-reference-clock.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: A phase-locked loop (PLL) is a circuit that tunes the Sample clock timebase to phase–lock to an external Reference clock. The PLL Reference clock source controls the source of the control voltage that tunes the VCXO of the Sample clock timebase for internal clock update sources. The frequency stabil

### NI 5442 Phase-Locked Loop Reference Clock

Note

device
specifications

The following figure shows the NI 5442 Reference Clock Source path.

[IMAGE alt='image' src='GUID-928A3C7A-05C9-46C0-86CE-DCD9AFB72E85-a5.gif']

Note

NIFGEN_ATTR_REFERENCE_CLOCK_SOURCE

#### Reference Clock Sources

The NI 5442 can
phase-lock its Sample clock timebase to an external signal
that is present on the CLK IN front panel connector. PXI devices
can also phase–lock to a 10 MHz Reference clock signal
provided by the PXI bus (PXI_CLK10).

Refer to the table in 
*Clocking Options*,
for the valid NI-FGEN property value combinations that can be used
to configure the NI 5442 clock settings
for an external Reference clock.

Note

device 
specifications

Related Topics

Configuring a Reference
Clock

Parent topic:

NI 5442 Clocking Options

Related concepts:

- NI 5442 Clocking Options
- Configuring a Reference Clock

<!--NI_TOPIC bundle=ni-fgen path=ni-5442-postamplifier-attenuation.html language=enus -->
## TOPIC 00586: NI 5442 Postamplifier Attenuation

- bundle_id: `ni-fgen`
- source_path: `ni-5442-postamplifier-attenuation.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5442-postamplifier-attenuation.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The postamplifier attenuation section is located after the amplifier in the Main path. The attenuators provide a range of attenuation from 0 dB to a maximum of 36 dB in steps of 12 dB. NI-FGEN automatically controls the value of attenuation set in the postamplifier attenuation section dependent on t

### NI 5442 Postamplifier Attenuation

The postamplifier attenuation section is located
after the amplifier in the Main path. The attenuators provide a
range of attenuation from 0 dB to a maximum of 36 dB in steps
of 12 dB. NI-FGEN automatically controls the value of attenuation
set in the postamplifier attenuation section dependent on the set
gain. You can read the value NI-FGEN has selected for postamplifier
attenuation using the 
Post-Amplifier Attenuation property or the 
NIFGEN_ATTR_POST_AMPLIFIER_ATTENUATION attribute.

Parent topic:

NI 5442 Attenuation

<!--NI_TOPIC bundle=ni-fgen path=ni-5442-power-up-and-reset-conditions.html language=enus -->
## TOPIC 00587: NI 5442 Power-Up and Reset Conditions

- bundle_id: `ni-fgen`
- source_path: `ni-5442-power-up-and-reset-conditions.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5442-power-up-and-reset-conditions.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The signal generator is in the following state from the time at which the computer begins to power up until the operating system is fully booted and NI-FGEN is loaded. The CH 0 analog output connector is disabled and has 50 Ω or 75 Ω impedance to ground. This impedance is the same as its previous se

### NI 5442 Power-Up and Reset Conditions

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

- The digital filter of the NI 5442
inside the DAC is disabled.

- CLK IN is disabled and has a 50 Ω
impedance to ground.
- PFI 0 and PFI 1 are tristated and have a 1
kΩ impedance to ground.

- PXI trigger lines are tristated and floating.
- The sample rate is set to the maximum rate, with the Sample
clock source set to the internal Sample clock timebase.
- The Sample clock timebase is tuned by the internal reference
control voltage.

Parent topic:

NI 5442 NI 5442 Overview

<!--NI_TOPIC bundle=ni-fgen path=ni-5442-preamplifier-attenuation.html language=enus -->
## TOPIC 00588: NI 5442 Preamplifier Attenuation

- bundle_id: `ni-fgen`
- source_path: `ni-5442-preamplifier-attenuation.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5442-preamplifier-attenuation.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The preamplifier attenuation section is located before the amplifier in the Main path. The attenuators provide a range of attenuation from 0 to a maximum of 12 dB in steps of 3 dB. NI-FGEN automatically controls the value of attenuation set in the preamplifier attenuation section depending on the se

### NI 5442 Preamplifier Attenuation

The preamplifier attenuation section is located
before the amplifier in the Main path. The attenuators provide a
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

NI 5442 Attenuation

<!--NI_TOPIC bundle=ni-fgen path=ni-5442-prefilter-gain-and-offset.html language=enus -->
## TOPIC 00589: NI 5442 Prefilter Gain and Offset

- bundle_id: `ni-fgen`
- source_path: `ni-5442-prefilter-gain-and-offset.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5442-prefilter-gain-and-offset.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use the following prefiltering components to add impairments to your data and/or to eliminate overflows that occur later in the OSP block. Related Topics Prefilter Gain Prefilter Offset

### NI 5442 Prefilter Gain and Offset

You can use the following prefiltering components
to add impairments to your data and/or to eliminate overflows that
occur later in the 
*OSP* block.

#### Related Topics

- Prefilter Gain
- Prefilter
Offset

Parent topic:

NI 5442 Onboard Signal Processing Components

Related concepts:

- NI 5442 Onboard Signal Processing (OSP)
- NI 5442 Prefilter Gain
- NI 5442 Prefilter Offset

<!--NI_TOPIC bundle=ni-fgen path=ni-5442-prefilter-gain.html language=enus -->
## TOPIC 00590: NI 5442 Prefilter Gain

- bundle_id: `ni-fgen`
- source_path: `ni-5442-prefilter-gain.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5442-prefilter-gain.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Prefilter gain can change the gain of the I and Q stream during signal generation. You can change the I and Q prefilter gains independently by setting the Pre-Filter Gain I and Pre-Filter Gain Q properties or the NIFGEN_ATTR_OSP_PRE_FILTER_GAIN_I and NIFGEN_ATTR_OSP_PRE_FILTER_GAIN_Q attributes. The

### NI 5442 Prefilter Gain

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
overflows for the next 71
 I/Q samples. If an overflow occurs during
these 71
 
 samples, the data is clipped and no error is returned. Overflows are common during the first 71
 I/Q samples after a
prefilter gain change because the abrupt change is seen as a
transient by the interpolation filters. The prefilter gain can be
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

NI 5442 Prefilter Gain and Offset

Related concepts:

- NI 5442 Quadrature Upconversion

<!--NI_TOPIC bundle=ni-fgen path=ni-5442-prefilter-offset.html language=enus -->
## TOPIC 00591: NI 5442 Prefilter Offset

- bundle_id: `ni-fgen`
- source_path: `ni-5442-prefilter-offset.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5442-prefilter-offset.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Prefilter offset can add offset to the I and Q stream during signal generation. Change the I and Q prefilter offsets independently by setting the Pre-Filter Offset I and Pre-Filter Offset Q properties or the NIFGEN_ATTR_OSP_PRE_FILTER_OFFSET_I and NIFGEN_ATTR_OSP_PRE_FILTER_OFFSET_Q attributes. The

### NI 5442 Prefilter Offset

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
offset changes, the OSP block ignores all overflows for the next 71
I/Q samples. If an overflow occurs during these 71 samples, the data
is clipped and no error is returned. 
Overflows are common
during the first 71 I/Q samples after a prefilter offset change
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

NI 5442 Prefilter Gain and Offset

Related concepts:

- NI 5442 Quadrature Upconversion
- NI 5442 Prefilter Gain

<!--NI_TOPIC bundle=ni-fgen path=ni-5442-pxi-express-bandwidth-considerations.html language=enus -->
## TOPIC 00592: NI 5442 PXI Express Bandwidth Considerations

- bundle_id: `ni-fgen`
- source_path: `ni-5442-pxi-express-bandwidth-considerations.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5442-pxi-express-bandwidth-considerations.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: National Instruments PXI Express signal generators use PCI Express as the interface to the computer. The physical connection between a PXI Express signal generator and a computer is called a PCI Express link. When a signal generator generates a waveform, it can saturate this link. Saturation occurs

### NI 5442 PXI Express Bandwidth Considerations

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

NI 5442 Streaming

<!--NI_TOPIC bundle=ni-fgen path=ni-5442-quadrature-upconversion.html language=enus -->
## TOPIC 00593: NI 5442 Quadrature Upconversion

- bundle_id: `ni-fgen`
- source_path: `ni-5442-quadrature-upconversion.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5442-quadrature-upconversion.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the behavior of the OSP block during quadrature upconversion. In quadrature upconversion, you give the I and Q complex waveform data to the OSP block. This data is then pulse shaped, interpolated up to a high sample rate, and then upconverted to a programmable carrier freq

### NI 5442 Quadrature Upconversion

The following figure shows the behavior of the OSP
block during quadrature upconversion.

[IMAGE alt='image' src='GUID-66E7A0A6-916D-4EB7-98C5-D6254DCD359D-a5.gif']

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

NI 5442 Common Onboard Signal Processing Applications

Related concepts:

- NI 5442 Prefilter Gain

<!--NI_TOPIC bundle=ni-fgen path=ni-5442-sample-clock-considerations.html language=enus -->
## TOPIC 00594: NI 5442 Sample Clock Considerations

- bundle_id: `ni-fgen`
- source_path: `ni-5442-sample-clock-considerations.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5442-sample-clock-considerations.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The performance of the signal generator that is using the OSP block can be significantly affected by the purity of its Sample clock. Sample clocks with high amounts of jitter or phase noise can create spurs in the signal generator spectrum that are not present when a pure Sample clock is used. If yo

### NI 5442 Sample Clock Considerations

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

NI 5442 IQ Rate

Related concepts:

- NI 5442 Internal Sample Clock
- NI 5442 IQ Rate
- NI 5442 External Sample Clock

<!--NI_TOPIC bundle=ni-fgen path=ni-5442-sample-size-and-resolution.html language=enus -->
## TOPIC 00595: NI 5442 Sample Size and Resolution

- bundle_id: `ni-fgen`
- source_path: `ni-5442-sample-size-and-resolution.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5442-sample-size-and-resolution.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5442 stores arbitrary waveforms in memory as signed 16-bit digital words. On the NI 5442, the entire 16 bits are sent to the digital gain circuit, the digital filter, and the DAC. Related Topics Onboard Memory Waveform Sizes

### NI 5442 Sample Size and Resolution

The NI 5442 stores arbitrary
waveforms in memory as signed 16-bit digital words. On the
NI 5442, the entire 16 bits are sent to the digital
gain circuit, the digital filter, and the DAC.

Related Topics

*Onboard Memory*

*Waveform Sizes*

Parent topic:

NI 5442 Waveform Generation

Related concepts:

- NI 5442 Onboard Memory
- NI 5442 Waveform Size and Quantum

<!--NI_TOPIC bundle=ni-fgen path=ni-5442-script-mode.html language=enus -->
## TOPIC 00596: NI 5442 Script Mode

- bundle_id: `ni-fgen`
- source_path: `ni-5442-script-mode.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5442-script-mode.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Script Mode allows you to use scripting to link and loop multiple waveforms in complex combinations using a script. A script is a series of instructions that indicates how waveforms saved in the onboard memory should be sent to the DUT. Scripts have many different uses, including specifying the orde

### NI 5442 Script Mode

*Script Mode* allows you to use scripting to link and
loop multiple waveforms in complex combinations using a 
script. A script is a series of instructions that
indicates how waveforms saved in the onboard memory should be sent
to the DUT. Scripts have many different uses, including specifying the order in which the waveforms
are generated, the number of times they are generated, and the
triggers and markers associated with the generation.

Parent topic:

NI 5442 Output Modes

Related concepts:

- Script Mode

<!--NI_TOPIC bundle=ni-fgen path=ni-5442-signal-routing.html language=enus -->
## TOPIC 00597: NI 5442 Signal Routing

- bundle_id: `ni-fgen`
- source_path: `ni-5442-signal-routing.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5442-signal-routing.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: An NI signal generator is capable of sending and receiving signals through the front panel and the PXI or RTSI trigger bus. The front panel connectors provides connectivity for the output channel as well as for control lines for sending and receiving clocks, triggers, and events. You can use the PXI

### NI 5442 Signal Routing

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

NI 5442 Theory of Operation

Related concepts:

- NI 5442 Syntax for Terminal Names

<!--NI_TOPIC bundle=ni-fgen path=ni-5442-single-tone.html language=enus -->
## TOPIC 00598: NI 5442 Single-Tone

- bundle_id: `ni-fgen`
- source_path: `ni-5442-single-tone.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5442-single-tone.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the behavior of the OSP block during single–tone generation. Use the Standard Function output mode to generate a single-tone. During single-tone generation, the NCO is used to create the output signal.

### NI 5442 Single-Tone

The following figure shows the behavior of the OSP
block during single–tone generation.

[IMAGE alt='image' src='GUID-A9C5CFE7-B5B9-4B98-A8F6-7ED157B865F7-a5.gif']

Use the 
*Standard Function output
mode* to generate a single-tone. During single-tone generation,
the 
*NCO* is used to create the
output signal.

Parent topic:

NI 5442 Common Onboard Signal Processing Applications

Related concepts:

- Standard Function Mode
- NI 5442 Numerically Controlled Oscillator (NCO)

<!--NI_TOPIC bundle=ni-fgen path=ni-5442-single-trigger-mode.html language=enus -->
## TOPIC 00599: NI 5442 Single Trigger Mode

- bundle_id: `ni-fgen`
- source_path: `ni-5442-single-trigger-mode.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5442-single-trigger-mode.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: When your application is configured for Single trigger mode, only one Start trigger is required to begin waveform generation. All Start triggers after the first Start trigger are ignored. Once the waveform generation is complete, the analog output indefinitely settles at the DC value of the last sam

### NI 5442 Single Trigger Mode

When your application is configured for Single
trigger mode, only one Start trigger is required to begin waveform
generation. All Start triggers after the first Start trigger are
ignored. Once the waveform generation is complete, the analog
output indefinitely settles at the DC value of the last sample in
the waveform. The
following table provides more information about
waveform generation behavior in Arbitrary Waveform, Arbitrary
Sequence, and Frequency List output modes.

| Output Mode | Trigger Behavior |
| --- | --- |
| Arbitrary Waveform Mode | The waveform you downloaded generates only once and waveform generation halts, unless the Arbitrary Waveform Repeat Count property or the NIFGEN_ATTR_ARB_REPEAT_COUNT attribute is set, in which case the waveform generates the specified number of times. |
| Arbitrary Sequence Mode | The waveform pattern you define in the sequence list generates only once. When a Start trigger is received, generation begins at the first segment and continues through the last segment, after which the waveform generation halts. You can determine the DC value at which waveform generation ends by configuring the last point in the final segment as the desired DC value, or you can add an extra segment filled with the same DC value. |
| Frequency List Mode | The device generates each step in the active frequency list sequentially. |

Parent topic:

NI 5442 Trigger Modes

<!--NI_TOPIC bundle=ni-fgen path=ni-5442-specifications.html language=enus -->
## TOPIC 00600: NI 5442 Specifications

- bundle_id: `ni-fgen`
- source_path: `ni-5442-specifications.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5442-specifications.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: For information about the signal generator specifications, refer to the device specifications. You can access these specifications by navigating to Start»All Programs»National Instruments» NI-FGEN»Documentation»NI Signal Generators Specifications, or you can visit ni.com/manuals.

### NI 5442 Specifications

For information about the signal generator
specifications, refer to the 
*device
specifications*. You can access these specifications by
navigating to 
Start»All Programs»National Instruments»
NI-FGEN»Documentation»NI Signal Generators Specifications, or you can visit 
ni.com/manuals.

Parent topic:

NI 5442 NI 5442 Overview

<!--NI_TOPIC bundle=ni-fgen path=ni-5442-standard-function-mode.html language=enus -->
## TOPIC 00601: NI 5442 Standard Function Mode

- bundle_id: `ni-fgen`
- source_path: `ni-5442-standard-function-mode.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5442-standard-function-mode.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Standard Function output mode is used to generate standard function waveforms such as sine, square, triangle, and so on. On the NI 5442, Standard Function mode is implemented through direct digital synthesis (DDS). DDS is a technique for deriving, under digital control, an analog frequency source fr

### NI 5442 Standard Function Mode

Standard Function output mode is used to generate standard
function waveforms such as sine, square, triangle, and so on. 
On the NI 5442, *Standard Function mode* is implemented
through *direct digital synthesis* (DDS). DDS is a technique for
deriving, under digital control, an analog frequency source from a
single Reference clock frequency. This technique produces
high-frequency accuracy and resolution, temperature stability,
wideband tuning, and rapid, phase-continuous frequency
switching.

In DDS mode, a fixed–size memory (called *lookup memory*) stores one cycle of a periodic waveform. A phase accumulator indexes the lookup memory. For each cycle of the device Sample clock, the sample of the waveform in lookup memory that is addressed by the phase accumulator is returned. The accumulator is then incremented by the value in the frequency control word (FCW). By adjusting the Frequency property or the NIFGEN_ATTR_FUNC_FREQUENCY attribute, NI-FGEN calculates the corresponding FCW, and you can vary the output frequency of the waveform in lookup memory. The phase accumulator increments in smaller steps for smaller FCWs. Accordingly, you need more samples to generate one waveform cycle, so the frequency is lower. A higher FCW results in a higher frequency. In DDS mode, the Sample clock does not vary with the frequency of the generated waveform. At higher frequencies, some waveform samples in lookup memory are skipped; at lower frequencies, some samples output multiple times in succession.

Parent topic:

NI 5442 Output Modes

Related concepts:

- Standard Function Mode
- Direct Digital Synthesis

<!--NI_TOPIC bundle=ni-fgen path=ni-5442-stepped-trigger-mode.html language=enus -->
## TOPIC 00602: NI 5442 Stepped Trigger Mode

- bundle_id: `ni-fgen`
- source_path: `ni-5442-stepped-trigger-mode.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5442-stepped-trigger-mode.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The waveform you downloaded generates each time a Start trigger occurs. After a waveform finishes generating, the last sample of the waveform repeats continuously until the next Start trigger is received. When the next Start trigger is received, the waveform generates again. If a Start trigger is re

### NI 5442 Stepped Trigger Mode

The waveform you downloaded generates each time a
Start trigger occurs. After a waveform finishes generating, the
last sample of the waveform repeats continuously until the next
Start trigger is received. When the next Start trigger is received,
the waveform generates again. If a Start trigger is received while
a waveform is generating, the Start trigger is ignored and another
Start trigger is required to regenerate the waveform after the last
sample generates. The
following table provides more information about
waveform generation behavior in Arbitrary Waveform, Arbitrary
Sequence, and Frequency List output modes.

| Output Mode | Trigger Behavior |
| --- | --- |
| Arbitrary Waveform Mode | If the Arbitrary Waveform Repeat Count property or the NIFGEN_ATTR_ARB_REPEAT_COUNT attribute is set, the waveform generates the specified number of times instead of just once. |
| Arbitrary Sequence Mode | The waveforms you define in the sequence list generate one segment at a time, each time a Start trigger occurs. The waveform loops as many times as has been configured for that particular segment. After the generation of a segment has halted, the last sample of the waveform repeats continuously until the next Start trigger is received. After the sequence list is exhausted, the waveform generation returns to the first segment and subsequent Start triggers restart the process. |
| Frequency List Mode | The device generates the next step in the active frequency list every time a Start trigger occurs. After the duration for a step has elapsed, the signal generation stops and remains at the configured DC offset level until the next Start trigger is received. When the next Start trigger is received, the next step in the frequency list is generated. After the final step, the frequency list repeats until generation is aborted. If the Trigger Source property or the NIFGEN_ATTR_TRIGGER_SOURCE attribute is set to NIFGEN_VAL_IMMEDIATE, the only way to advance to the next step in the frequency list is to call the niFgen Send Software Edge Trigger VI or the niFgen_SendSoftwareEdgeTrigger function. |

Parent topic:

NI 5442 Trigger Modes

<!--NI_TOPIC bundle=ni-fgen path=ni-5442-streaming.html language=enus -->
## TOPIC 00603: NI 5442 Streaming

- bundle_id: `ni-fgen`
- source_path: `ni-5442-streaming.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5442-streaming.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Streaming is a way to generate waveforms that are too large to fit in the onboard memory of the signal generator. Streaming can be used in Arbitrary Waveform, Arbitrary Sequence, or Script output modes. To stream waveform data, allocate and identify all or a portion of the signal generator onboard m

### NI 5442 Streaming

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

NI 5442 Waveform Generation

Related concepts:

- Arbitrary Waveform Output Mode
- Arbitrary Sequence Mode
- Script Mode
- Direct DMA

<!--NI_TOPIC bundle=ni-fgen path=ni-5442-synchronization.html language=enus -->
## TOPIC 00604: NI 5442 Synchronization

- bundle_id: `ni-fgen`
- source_path: `ni-5442-synchronization.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5442-synchronization.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Your signal generator is based on the National Instruments Synchronization and Memory Core (SMC) technology and therefore supports TClk synchronization. Refer to the NI-TClk Synchronization Help for more information about NI-TClk Synchronization.

### NI 5442 Synchronization

Your signal generator is based on the 
National Instruments
Synchronization and Memory Core (SMC) technology and therefore
supports TClk synchronization. Refer to the 
NI-TClk
Synchronization Help for more information about NI-TClk
Synchronization.

Parent topic:

NI 5442 NI 5442 Overview

<!--NI_TOPIC bundle=ni-fgen path=ni-5442-syntax-for-terminal-names.html language=enus -->
## TOPIC 00605: NI 5442 Syntax for Terminal Names

- bundle_id: `ni-fgen`
- source_path: `ni-5442-syntax-for-terminal-names.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5442-syntax-for-terminal-names.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The syntax for terminal names is a unique identifier that refers to a physical terminal in your system. To guarantee the uniqueness of a terminal name across multiple devices, terminal names begin with a forward slash, followed by the name of the device as configured in MAX, such as Dev1. A forward

### NI 5442 Syntax for Terminal Names

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

NI 5442 Signal Routing

<!--NI_TOPIC bundle=ni-fgen path=ni-5442-theory-of-operation.html language=enus -->
## TOPIC 00606: NI 5442 Theory of Operation

- bundle_id: `ni-fgen`
- source_path: `ni-5442-theory-of-operation.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5442-theory-of-operation.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Expand this topic for information about the theory of operation of your signal generator.

### NI 5442 Theory of Operation

Expand this topic for information about the theory
of operation of your signal generator.

Parent topic:

NI 5442 NI 5442 Overview

<!--NI_TOPIC bundle=ni-fgen path=ni-5442-thermal-shutdown.html language=enus -->
## TOPIC 00607: NI 5442 Thermal Shutdown

- bundle_id: `ni-fgen`
- source_path: `ni-5442-thermal-shutdown.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5442-thermal-shutdown.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: NI-FGEN supports thermal shutdown capability for the NI 5442. This capability allows the signal generator to detect when it has reached a dangerously high temperature and to then power down to prevent damage to the device. Air circulation paths, fan settings, and space allowances are several factors

### NI 5442 Thermal Shutdown

NI-FGEN supports thermal shutdown capability for
the NI 5442. This
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

NI 5442 NI 5442 Overview

<!--NI_TOPIC bundle=ni-fgen path=ni-5442-trigger-modes.html language=enus -->
## TOPIC 00608: NI 5442 Trigger Modes

- bundle_id: `ni-fgen`
- source_path: `ni-5442-trigger-modes.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5442-trigger-modes.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5442 has four trigger modes: Single, Continuous, Stepped, and Burst. These trigger modes are available for Arbitrary Waveform, Arbitrary Sequence, and Frequency List output mode. Refer to the niFgen Configure Trigger Mode VI or the niFgen_ConfigureTriggerMode function for information about se

### NI 5442 Trigger Modes

The NI 5442 has four trigger modes: Single, Continuous, Stepped,
and Burst. These trigger modes are available for Arbitrary
Waveform, Arbitrary Sequence, and Frequency List output mode.
Refer to the 
niFgen
Configure Trigger Mode VI or the 
niFgen_ConfigureTriggerMode function for information about setting the trigger mode.

Parent topic:

NI 5442 Triggering

<!--NI_TOPIC bundle=ni-fgen path=ni-5442-trigger-sources.html language=enus -->
## TOPIC 00609: NI 5442 Trigger Sources

- bundle_id: `ni-fgen`
- source_path: `ni-5442-trigger-sources.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5442-trigger-sources.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Trigger sources are software selectable. You can use any of the following external input triggers: PFI 0 or PFI 1 on the front panel connectors PXI_TRIG<0..7> lines on the PXI trigger bus backplane The following figure shows the possible trigger sources for the NI 5442. ^ § Refer to Exporting Signal

### NI 5442 Trigger Sources

Trigger sources are software selectable. You can
use any of the following external input triggers:

- PFI 0 or PFI 1 on the front panel connectors

- PXI_TRIG<0..7> lines on the PXI trigger bus backplane

The following figure shows the possible trigger
sources for the NI 5442.

[IMAGE alt='image' src='GUID-1C4628B0-B1AB-4165-B6B6-0E91EB739FBA-a5.gif']

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

NI 5442 Triggering

Related concepts:

- NI 5442 Exporting Signals
- PXI Trigger Lines
- PXI Star Trigger Line

<!--NI_TOPIC bundle=ni-fgen path=ni-5442-trigger-timing.html language=enus -->
## TOPIC 00610: NI 5442 Trigger Timing

- bundle_id: `ni-fgen`
- source_path: `ni-5442-trigger-timing.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5442-trigger-timing.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the relationship between Start trigger and the waveform output. t[s1] is the required pulse width on the Start trigger signal. t[s2] is the delay from the Start trigger to the waveform output. Refer to the NI PXIe-5442 Specifications for more information about these timing

### NI 5442 Trigger Timing

The following figure shows the relationship between
Start trigger and the waveform output. t<sub>s1</sub> is the required pulse width on the Start trigger
signal. t<sub>s2</sub> is the delay from the Start trigger to the waveform
output. Refer to the 
*NI PXIe-5442
Specifications* for more information about these timing
parameters.

[IMAGE alt='image' src='GUID-9DD6A51C-2BCA-4129-9C8D-0A821181925F-a5.gif']

The NI 5442 also allows you to export
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

NI 5442 Triggering

<!--NI_TOPIC bundle=ni-fgen path=ni-5442-triggering.html language=enus -->
## TOPIC 00611: NI 5442 Triggering

- bundle_id: `ni-fgen`
- source_path: `ni-5442-triggering.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5442-triggering.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can define the signal generator functionality by using the various triggering techniques. Expand this section to learn more about using triggers with your signal generator.

### NI 5442 Triggering

You can define the signal generator functionality
by using the various triggering techniques. Expand this section to
learn more about using triggers with your signal generator.

Parent topic:

NI 5442 NI 5442 Overview

<!--NI_TOPIC bundle=ni-fgen path=ni-5442-using-an-external-clock-with-the-osp.html language=enus -->
## TOPIC 00612: NI 5442 Using an External Clock with the OSP Block

- bundle_id: `ni-fgen`
- source_path: `ni-5442-using-an-external-clock-with-the-osp.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5442-using-an-external-clock-with-the-osp.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Some applications may require lower jitter or phase noise than is provided by the onboard High-Resolution clock. You can use an external clock source to achieve spectral purity at any arbitrary I/Q rate. To determine the frequency of the sample rate for the external clock source, complete the follow

### NI 5442 Using an External Clock with the OSP Block

Some applications may require lower jitter or phase
noise than is provided by the onboard High-Resolution clock. You can use an
external clock source to achieve spectral purity at any arbitrary
I/Q rate. To determine the frequency of the sample rate for the
external clock source, complete the following steps.

1. Set the 
Sample
Clock Source property or the 
 NIFGEN_ATTR_SAMPLE_CLOCK_SOURCE attribute to the external 
 clock source 
you are using.
2. Set the 
IQ Rate
property or the 
 NIFGEN_ATTR_OSP_IQ_RATE attribute.

1. Read the value of the 
Sample
Rate property or the 
 NIFGEN_ATTR_ARB_SAMPLE_RATE attribute.
2. Set the external clock source sample rate to the frequency of
the Sample Rate property or the 
 NIFGEN_ATTR_ARB_SAMPLE_RATE 
attribute that you just read.
3. Validate that the external Sample clock source is connected to
the NI 5442 connector specified in the 
Sample
Clock Source property or the 
 NIFGEN_ATTR_SAMPLE_CLOCK_SOURCE attribute and is generating a clock before you continue
configuring the 
NI 5442.

For more information about using external clocks, refer to 
*External Sample
Clock Sources*.

Parent topic:

NI 5442 IQ Rate

Related concepts:

- NI 5442 External Sample Clock

<!--NI_TOPIC bundle=ni-fgen path=ni-5442-waveform-amplitude-control.html language=enus -->
## TOPIC 00613: NI 5442 Waveform Amplitude Control

- bundle_id: `ni-fgen`
- source_path: `ni-5442-waveform-amplitude-control.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5442-waveform-amplitude-control.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5442 uses both amplifiers and attenuators to achieve required amplitude settings. Output Paths and Amplifiers The following figure shows two different gain paths: the Direct path and the Main path with High-Gain and Low-Gain amplifiers. The Direct path provides the output of the main DAC to t

### NI 5442 Waveform Amplitude Control

The NI 5442 uses both amplifiers and
attenuators to achieve required amplitude settings.

#### Output Paths and Amplifiers

The following figure shows two different gain
paths: the Direct path and the Main path with High-Gain and Low-Gain amplifiers.

[IMAGE alt='image' src='GUID-235B4D87-8DC7-40D4-BF4D-44312DF3D738-a5.gif']

The Direct path provides the output of the main DAC
to the CH 0 connector with the fewest electronic components in the path.
There are no programmable amplifiers and there is no method for adding DC
offset to the waveform. The Direct path can generate a maximum of 
1 V<sub>pk-pk</sub> at the CH 0 output into matched load
impedance. The maximum gain setting for an Analog Output path
configured to the Direct path is 0.527 (gain is a unitless
value).

The Main path
 has a 
2 V<sub>pk-pk</sub> amplifier and is used for waveforms that
have all output voltages equal to or smaller than 
2.0 V<sub>pk-pk</sub> into matched load impedance.
 You can configure the gain by calling the 
Arbitrary Waveform Gain or 
Amplitude
property or the 
NIFGEN_ATTR_ARB_GAIN or
NIFGEN_ATTR_FUNC_AMPLITUDE attribute.

In addition, the DC offset amplifier, which adds 
*DC offset* to the signal, is
located in the High-Gain and Low-Gain Amplifier paths prior to the
attenuators and amplifiers. The DC offset amplifier can be
fine-tuned to add offset to your signal. This fine-tuning of the
main DC offset amplifier is performed by the offset DAC.

Parent topic:

NI 5442 Analog Output

Related concepts:

- NI 5442 DC Offset

<!--NI_TOPIC bundle=ni-fgen path=ni-5442-waveform-and-generation-instruction-m.html language=enus -->
## TOPIC 00614: NI 5442 Waveform and Generation Instruction Memory Size

- bundle_id: `ni-fgen`
- source_path: `ni-5442-waveform-and-generation-instruction-m.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5442-waveform-and-generation-instruction-m.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Waveform Memory Size Waveforms are stored in the NI 5442 onboard memory in contiguous blocks. These blocks are allocated in multiples of 128 bytes. This allocation style means that while waveform sizes may be multiples of one sample (two bytes) on the NI 5442, the amount of onboard memory allocated

### NI 5442 Waveform and Generation Instruction Memory Size

#### Waveform Memory Size

Waveforms are stored in the
NI 5442 onboard memory in contiguous
blocks. These blocks are allocated in multiples of 128 bytes. This
allocation style means that while waveform sizes may be multiples
of 
one sample (two bytes) on the NI 5442, the amount of
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
2. Memory is written to in blocks of 2 bytes.

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

The NI 5442 uses a
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

NI 5442 Onboard Memory

<!--NI_TOPIC bundle=ni-fgen path=ni-5442-waveform-generation.html language=enus -->
## TOPIC 00615: NI 5442 Waveform Generation

- bundle_id: `ni-fgen`
- source_path: `ni-5442-waveform-generation.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5442-waveform-generation.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5442 supports the following output, or generation, modes: Standard Function Arbitrary Waveform Arbitrary Sequence Frequency List Script To select an output mode, set the Output Mode parameter of the niFgen Configure Output Mode VI or the niFgen_ConfigureOutputMode function.

### NI 5442 Waveform Generation

The NI 5442 supports the
following output, or generation, modes:

- Standard Function
- Arbitrary Waveform
- Arbitrary Sequence
- Frequency List
- Script

To select an output mode, set the 
Output Mode parameter of the 
niFgen
Configure Output Mode VI or the 
niFgen_ConfigureOutputMode function.

Parent topic:

NI 5442 NI 5442 Overview

Related concepts:

- NI 5442 Standard Function Mode
- NI 5442 Arbitrary Waveform Mode
- NI 5442 Arbitrary Sequence Mode
- NI 5442 Frequency List Mode
- NI 5442 Script Mode

<!--NI_TOPIC bundle=ni-fgen path=ni-5442-waveform-quantum.html language=enus -->
## TOPIC 00616: NI 5442 Waveform Quantum

- bundle_id: `ni-fgen`
- source_path: `ni-5442-waveform-quantum.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5442-waveform-quantum.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Quantum is the increment in samples that waveform sizes must adhere to. The NI 5442 has a sample quantum of one, allowing waveforms of any size (between the maximum and minimum waveform sizes) to be downloaded.

### NI 5442 Waveform Quantum

Quantum is the increment in samples that waveform
sizes must adhere to. The NI 5442 has a sample quantum of one, allowing
waveforms of any size (between the maximum and minimum waveform
sizes) to be downloaded.

Parent topic:

NI 5442 Waveform Size and Quantum

<!--NI_TOPIC bundle=ni-fgen path=ni-5442-waveform-size-and-quantum.html language=enus -->
## TOPIC 00617: NI 5442 Waveform Size and Quantum

- bundle_id: `ni-fgen`
- source_path: `ni-5442-waveform-size-and-quantum.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5442-waveform-size-and-quantum.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5442 onboard memory architecture imposes certain requirements on the waveform size and quantum.

### NI 5442 Waveform Size and Quantum

The NI 5442 onboard memory architecture
imposes certain requirements on the waveform *size* and *quantum*.

Parent topic:

NI 5442 Waveform Generation

Related concepts:

- NI 5442 Waveform Size
- NI 5442 Waveform Quantum

<!--NI_TOPIC bundle=ni-fgen path=ni-5442-waveform-size.html language=enus -->
## TOPIC 00618: NI 5442 Waveform Size

- bundle_id: `ni-fgen`
- source_path: `ni-5442-waveform-size.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5442-waveform-size.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Minimum Waveform Size The minimum waveform size on the NI 5442 depends on the output mode and the trigger mode. Refer to the device specifications for the minimum waveform size values for the different modes. To provide greater programming flexibility, NI-FGEN does not strictly enforce the minimum

### NI 5442 Waveform Size

#### Minimum Waveform Size

The
minimum waveform size on the NI 5442 depends on the output mode and the 
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

NI 5442 Waveform Size and Quantum

Related concepts:

- NI 5442 Trigger Modes
- NI 5442 Waveform and Generation Instruction Memory Size

<!--NI_TOPIC bundle=ni-fgen path=ni-5450-aborting-generation.html language=enus -->
## TOPIC 00619: NI 5450 Aborting Generation

- bundle_id: `ni-fgen`
- source_path: `ni-5450-aborting-generation.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5450-aborting-generation.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can abort the generation of the current waveform. Aborting the generation exhibits different behaviors for different waveform output modes. Related Topics Aborting to Ground

### NI 5450 Aborting Generation

You can abort the generation of the current
waveform. Aborting the generation exhibits different behaviors for
different 
*waveform output
modes*.

Related Topics

*Aborting to Ground*

Parent topic:

NI 5450 Waveform Generation

Related concepts:

- NI 5450 Waveform Generation
- Abort to Ground

<!--NI_TOPIC bundle=ni-fgen path=ni-5450-access-and-active-leds.html language=enus -->
## TOPIC 00620: NI 5450 ACCESS and ACTIVE LEDs

- bundle_id: `ni-fgen`
- source_path: `ni-5450-access-and-active-leds.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5450-access-and-active-leds.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The ACCESS and ACTIVE LEDs indicate the status of the PXIe module: ACCESS LED The ACCESS LED indicates basic hardware status as shown in the following table. Color Indications Off Device is not yet functional, or the device has detected a problem with a power rail. Amber The device is being accessed

### NI 5450 ACCESS and ACTIVE LEDs

The ACCESS and ACTIVE LEDs indicate the status of
the PXIe module:

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

NI 5450 Front Panel

<!--NI_TOPIC bundle=ni-fgen path=ni-5450-accessories.html language=enus -->
## TOPIC 00621: NI 5450 Accessories

- bundle_id: `ni-fgen`
- source_path: `ni-5450-accessories.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5450-accessories.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: National Instruments offers a variety of products to use with your signal generator, including cables and other accessories. Visit ni.com for more information.

### NI 5450 Accessories

National Instruments offers a variety of products
to use with your signal generator, including cables and other
accessories. Visit 
ni.com for more
information.

Parent topic:

NI 5450 NI 5450 Overview

<!--NI_TOPIC bundle=ni-fgen path=ni-5450-adjusting-skew.html language=enus -->
## TOPIC 00622: NI 5450 Adjusting Skew

- bundle_id: `ni-fgen`
- source_path: `ni-5450-adjusting-skew.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5450-adjusting-skew.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Using the NI 5450, you can fine-tune the skew in your TClk application by dynamically adjusting the oscillator phase DAC value. You can only adjust the value in External Sample Clock mode, but you can use the PXI 10 MHz backplane clock with an External Sample Clock Multiplier as your external clock

### NI 5450 Adjusting Skew

Using the NI 5450, you can fine-tune the skew in your TClk application by dynamically adjusting the oscillator phase DAC value.
You can only adjust the value in *External Sample Clock* mode, but you can use the PXI 10 MHz backplane clock with an External Sample Clock Multiplier as your external clock if you are not supplying your own clock source.

Complete the following steps to manually adjust TClk:

1. Configure the devices for acquisition or generation synchronized with NI-TClk.
2. Read the oscillator phase DAC value after performing TClk synchronization and save the value while the program is still running.
3. Manually adjust the oscillator phase DAC value until optimal alignment is achieved, starting from the value saved in step 2.

Complete the following steps to optimize synchronization repeatability:

1. After the acquisition or generation is completed, but before you close the session, read the Oscillator Phase DAC Value property.
2. Store the value.
3. Before running the program again, set the oscillator phase DAC value to the stored value.

Parent topic:

NI 5450 Synchronization

Related concepts:

- NI 5450 External Sample Clock

<!--NI_TOPIC bundle=ni-fgen path=ni-5450-analog-gain-settings.html language=enus -->
## TOPIC 00623: NI 5450 Analog Gain Settings

- bundle_id: `ni-fgen`
- source_path: `ni-5450-analog-gain-settings.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5450-analog-gain-settings.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following table summarizes the maximum and minimum gain setting that you can apply for the NI-FGEN analog path options. Refer to the device specifications for more information about gain resolution. Analog Path Gain Summary (Matched Load Impedance) NI-FGEN Analog Path Maximum Gain Value Minimum

### NI 5450 Analog Gain Settings

The following table summarizes the maximum and
minimum gain setting that you can apply for the NI-FGEN analog path
options. Refer to the 
*device
specifications* for more information about gain resolution.

| Analog Path Gain Summary (Matched Load Impedance) |  |  |
| --- | --- | --- |
| NI-FGEN Analog Path | Maximum Gain Value | Minimum Gain Value |
| Direct Path without flatness correction | 0.5 | 0.354 |
| Direct Path with flatness correction | 0.4 | 0.284 |
| Note: Gain is unitless. |  |  |

Note

Parent topic:

NI 5450 Waveform Amplitude Control

<!--NI_TOPIC bundle=ni-fgen path=ni-5450-analog-output.html language=enus -->
## TOPIC 00624: NI 5450 Analog Output

- bundle_id: `ni-fgen`
- source_path: `ni-5450-analog-output.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5450-analog-output.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the NI 5450 Analog Output signal path. NI 5450 analog waveforms are generated as follows: The 16-bit digital waveform data from the Waveform Generation Engine or OSP is passed to a digital gain circuit and then to the high-speed DAC. This DAC also implements a portion of t

### NI 5450 Analog Output

The following figure shows the NI 5450 Analog Output signal path.

[IMAGE alt='image' src='GUID-99847B23-D9A8-4ADE-853D-434DB360B9E4-a5.gif']

NI 5450 analog waveforms are
generated as follows:

1. The 16-bit digital waveform data from the Waveform Generation
Engine or OSP is passed to a digital gain circuit and then to the 
high-speed DAC. This DAC also implements a portion of the Analog
Output signal path attenuation with a range of 0 dB to 3 dB. Refer to the NI PXIe-5450 Specifications for the exact resolution. You can adjust the amount
of attenuation by configuring the Arbitrary
Waveform Gain property or the NIFGEN_ATTR_ARB_GAIN attribute. NI-FGEN calculates and sets the correct amount of attenuation required, corresponding to the gain setting.
2. Following the DAC, the signal follows the
Direct path. The Direct path can provide a maximum of 1.0 V pk-pk differential output into matched impedance with a
maximum of 3 dB attenuation.
3. The signal then passes through the Output Enable relay. When
the Output Enable relay is disabled, ground is connected to the
output through a 50 Ω resistor.
Waveform generation continues while the output
enable relay is disabled. When the relay is enabled, the analog
waveform is seen at the connector. Enable or
disable the output of the analog waveform generator by using the 
niFgen Output
Enable VI or the 
 niFgen_ConfigureOutputEnabled function.
4. The signal then passes to the
differential channel connector.

Note

Parent topic:

NI 5450 Theory of Operation

<!--NI_TOPIC bundle=ni-fgen path=ni-5450-arbitrary-sequence-mode.html language=enus -->
## TOPIC 00625: NI 5450 Arbitrary Sequence Mode

- bundle_id: `ni-fgen`
- source_path: `ni-5450-arbitrary-sequence-mode.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5450-arbitrary-sequence-mode.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Arbitrary Sequence mode allows you to load multiple waveforms in the onboard memory of the NI 5450. A finite number of samples make a waveform. To generate these downloaded waveforms in a specific order, you must prepare a sequence, which contains a number of segments in a specific order. Each segme

### NI 5450 Arbitrary Sequence Mode

*Arbitrary Sequence mode* allows you to load multiple
waveforms in the onboard memory of the NI 5450. A finite
number of samples make a waveform. To generate these downloaded
waveforms in a specific order, you must prepare a sequence, which
contains a number of segments in a specific order. Each segment
specifies a downloaded waveform, a number of loops to repeat the
selected waveform, and a numeric offset in which a marker is
generated by the device.

Parent topic:

NI 5450 Output Modes

Related concepts:

- Arbitrary Sequence Mode

<!--NI_TOPIC bundle=ni-fgen path=ni-5450-arbitrary-waveform-generation.html language=enus -->
## TOPIC 00626: NI 5450 Arbitrary Waveform Generation

- bundle_id: `ni-fgen`
- source_path: `ni-5450-arbitrary-waveform-generation.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5450-arbitrary-waveform-generation.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the behavior of the OSP block during basic arbitrary waveform generation without OSP for each channel. For basic arbitrary waveform generation, disable onboard signal processing by setting the OSP Enabled property or the NIFGEN_ATTR_OSP_ENABLED attribute.

### NI 5450 Arbitrary Waveform Generation

The following figure shows the behavior of the OSP
block during basic arbitrary waveform generation without OSP for each channel.

[IMAGE alt='image' src='GUID-8DFB67DA-9114-4DD7-8C94-B2D93AED936C-a5.gif']

For basic arbitrary waveform generation, disable
onboard signal processing by setting the 
OSP
Enabled property or the 
NIFGEN_ATTR_OSP_ENABLED attribute.

Parent topic:

NI 5450 Common Onboard Signal Processing Applications

<!--NI_TOPIC bundle=ni-fgen path=ni-5450-arbitrary-waveform-mode.html language=enus -->
## TOPIC 00627: NI 5450 Arbitrary Waveform Mode

- bundle_id: `ni-fgen`
- source_path: `ni-5450-arbitrary-waveform-mode.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5450-arbitrary-waveform-mode.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5450 supports Arbitrary Waveform output mode. Arbitrary Waveform mode generates waveforms from user-created/provided waveform arrays of numeric data. The waveform arrays are downloaded to the arbitrary waveform generator onboard memory. Arbitrary Waveform mode also uses memory to store the in

### NI 5450 Arbitrary Waveform Mode

The NI 5450 supports Arbitrary Waveform output mode. Arbitrary Waveform mode generates waveforms from
user-created/provided waveform arrays of numeric data. The waveform
arrays are downloaded to the arbitrary waveform generator onboard
memory. *Arbitrary Waveform mode* also uses memory to
store the instructions for generating waveform sequences in the
onboard memory.

Parent topic:

NI 5450 Output Modes

Related concepts:

- Arbitrary Waveform Output Mode

<!--NI_TOPIC bundle=ni-fgen path=ni-5450-attenuation.html language=enus -->
## TOPIC 00628: NI 5450 Attenuation

- bundle_id: `ni-fgen`
- source_path: `ni-5450-attenuation.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5450-attenuation.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The main DAC output can be fine-tuned for attenuation, which provides 0 to 3 dB of the Analog Output path signal attenuation. Attenuating the DAC output signal allows you to vary the signal amplitude while maintaining the dynamic range of the DAC. You do not lose any bits from the digital representa

### NI 5450 Attenuation

The main DAC output can be fine-tuned for attenuation, which provides 0 to 3 dB of the Analog Output path signal attenuation. Attenuating the DAC output signal allows you to vary the signal amplitude while maintaining the dynamic range of the DAC. You do not lose any bits from the digital representation of the signal and you do not sacrifice dynamic range, as you would if you control amplitude by using smaller data ranges of the DAC. The main DAC also provides the fine resolution for the attenuation settings.

Fine-tuning of the main DAC attenuation is performed by the gain DAC. Adjust the gain DAC using the Gain DAC Value property or the NIFGEN_ATTR_GAIN_DAC_VALUE attribute.

Parent topic:

NI 5450 Waveform Amplitude Control

<!--NI_TOPIC bundle=ni-fgen path=ni-5450-baseband-i-q-interpolation.html language=enus -->
## TOPIC 00629: NI 5450 Baseband I/Q Interpolation

- bundle_id: `ni-fgen`
- source_path: `ni-5450-baseband-i-q-interpolation.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5450-baseband-i-q-interpolation.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the behavior of the OSP block during baseband I/Q interpolation. Baseband I/Q interpolation allows the OSP block to interpolate complex data signals at a low sample rate up to a high sample rate. Arbitrary pulse shaping of the data can also be done in the FIR filter. For b

### NI 5450 Baseband I/Q Interpolation

The following figure shows the behavior of the OSP
block during baseband I/Q interpolation.

[IMAGE alt='image' src='GUID-B7D4B7BA-723C-4923-B5CE-6BE234092194-a5.gif']

Baseband I/Q interpolation allows the OSP block to
interpolate complex data signals at a low sample rate up to a high sample rate.
Arbitrary pulse shaping of the data can also be done in the FIR
filter. For baseband I/Q interpolation, complete the following
steps.

1. Enable onboard signal processing by setting the 
OSP
Enabled property or the 
 NIFGEN_ATTR_OSP_ENABLED attribute.
2. Set the OSP mode to Baseband by calling the OSP Mode
property or the 
 NIFGEN_ATTR_OSP_MODE attribute.
3. Specify the use of complex numbers for the waveform data by
setting the 
Data
Processing Mode property or the 
 NIFGEN_ATTR_OSP_DATA_PROCESSING_MODE attribute.
4. Set the 
IQ Rate
property or the 
 NIFGEN_ATTR_OSP_IQ_RATE attribute to the low sample rate of the waveform data.
5. Set the 
FIR Filter
Type property or the 
 NIFGEN_ATTR_OSP_FIR_FILTER_TYPE attribute.
6. Set the corresponding filter parameter.
7. (Optional) Shift the frequency by calling the Frequency Shift property or the 
 NIFGEN_ATTR_OSP_FREQUENCY_SHIFT attribute.
8. Download the low sample rate waveform(s) to the signal
generator.
9. Read the sample rate by calling the Sample Rate property or the NIFGEN_ATTR_ARB_SAMPLE_RATE attribute.

Parent topic:

NI 5450 Baseband Interpolation Considerations

<!--NI_TOPIC bundle=ni-fgen path=ni-5450-baseband-interpolation-considerations.html language=enus -->
## TOPIC 00630: NI 5450 Baseband Interpolation Considerations

- bundle_id: `ni-fgen`
- source_path: `ni-5450-baseband-interpolation-considerations.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5450-baseband-interpolation-considerations.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5450 implements baseband interpolation in order to reduce the power of aliased images. Interpolation is a process that effectively turns a lower sample rate into a higher sample rate. Because the signal is now at a higher sample rate, images are moved to higher frequencies, where they fall in

### NI 5450 Baseband Interpolation Considerations

The NI 5450 implements baseband interpolation in order to reduce the power of *aliased images*. Interpolation is a process that effectively turns a lower sample rate into a higher sample rate. Because the signal is now at a higher sample rate, images are moved to higher frequencies, where they fall in the rejection band of the image rejection filter and are suppressed.

NIFGEN_ATTR_ARB_SAMPLE_RATE

Note

NI PXIe-5450 specifications

#### Interpolation Settings

To determine the total interpolation and interpolated sample rate, divide 400 MS/s by your desired I/Q rate and round down to the nearest step, as noted in the Interpolation table for your total interpolation value. Then, consult the following table for settings that will allow you to achieve your desired interpolated sample rate.

Note

Example: At a desired I/Q rate of 4.5 MS/s, the total interpolation will be determined by the following calculations:

400 MS/s ÷ 4.45 MS/s = 89.88x total interpolation.

A total interpolation rate of 89.88x falls in the 24-8192 Total Interpolation range in the Interpolation table. As this range is measured in steps of 8, you must round down to the nearest multiple of 8, yielding a total interpolation rate of 88x. This value corresponds to a sample rate of 391.6 MS/s and a worst case image at or below -100 dB .

| I/Q Rate (S/s) | Total Interpolation | I or Q Bandwidth (Hz) 1 Sample /symbol | Interpolated Sample Rate* (MS/s) | Theoretical Worst Case Image Feed-through (dB), 20 MHz at Baseband Bandwidth Signal, Direct Path | Theoretical Worst Case Image Feed-through† (dB), Maximum I/Q Bandwidth, Direct Path |
| --- | --- | --- | --- | --- | --- |
| 12—24 k | 16384—32768 in steps of 32 | 4.8—9.6 k | 370—400 | N/A | <–100 |
| 24—48 k | 8192—16384 in steps of 16 | 9.6—19.2 k | 370—400 | N/A | <–100 |
| 48k—16.66 M | 24—8192 in steps of 8 | 19.2 k—6.664 M | 310—400 | N/A | –100 |
| 16.66—33.33 M | 12—24 in steps of 4 | 6.664—13.332 M | 300—400 | N/A | –88 |
| 33.33—50 M | 8 | 13.332—20 M | 267—400 | N/A | –61 |
| 50—67.5 M | 4 | 20—27 M | 200—270 | –31 | –23 |
| 67.5—100 M | 4 | 27—40 M | 270—400 | –62 | –45 |
| 100—135 M | 2 | 40—54 M | 200—270 | –31 | –31 |
| 135—200 M | 2 | 54—80 M | 270—400 | –62 | –28 |
| — | 1 | 80—108 M | 200—270 | –31 | –8 |
| — | 1 | 108—159.6 M | 270—399 | –62 | –8 |
| — | 1 | 120 M | 400 | –82 | –52 |
| Assumptions: Internal Sample clock. Desired I/Q and sample rate ranges do not include the lower limit, for example, an I/Q rate of 50 MS/s yields 8x total interpolation. *If your interpolated sample rate falls within an undesirable band, you can use the Modulation Toolkit to provide fractional resampling that will adjust the sample rate to achieve better image rejection. †Calculated from sinc response and typical filter rejection for the NI 5450. Refer to the NI PXIe-5450 specifications for more information about the expected performance of the NI 5450. |  |  |  |  |  |

Parent topic:

NI 5450 Common Onboard Signal Processing Applications

Related concepts:

- Aliased Images

<!--NI_TOPIC bundle=ni-fgen path=ni-5450-baseband-interpolation.html language=enus -->
## TOPIC 00631: NI 5450 Baseband Interpolation

- bundle_id: `ni-fgen`
- source_path: `ni-5450-baseband-interpolation.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5450-baseband-interpolation.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the behavior of the OSP block during baseband interpolation. Baseband interpolation allows the OSP block to interpolate real data signals at a low sample rate up to a high sample rate. Arbitrary pulse shaping of the data can also be done in the FIR filter. For baseband int

### NI 5450 Baseband Interpolation

The following figure shows the behavior of the OSP
block during baseband interpolation.

[IMAGE alt='image' src='GUID-9827881A-BA49-45BC-B6B6-B6BA45DA7862-a5.gif']

Baseband interpolation allows the OSP block to
interpolate real data signals at a low sample rate up to a high sample rate.
Arbitrary pulse shaping of the data can also be done in the FIR
filter. For baseband interpolation, complete the following
steps.

1. Enable onboard signal processing by setting the 
OSP
Enabled property or the 
 NIFGEN_ATTR_OSP_ENABLED attribute.
2. Set the OSP mode to Baseband by calling the OSP Mode
property or the 
 NIFGEN_ATTR_OSP_MODE attribute
3. Specify the use of real numbers for the waveform data by
setting the 
Data
Processing Mode property or the 
 NIFGEN_ATTR_OSP_DATA_PROCESSING_MODE attribute.
4. Set the 
IQ Rate
property or the 
 NIFGEN_ATTR_OSP_IQ_RATE attribute to the low sample rate of the waveform data.
5. Set the 
FIR Filter
Type property or the 
 NIFGEN_ATTR_OSP_FIR_FILTER_TYPE attribute.
6. Set the corresponding filter parameter.
7. Download the low sample rate waveform(s) to the signal
generator.
8. Read the sample rate by calling the Sample Rate property or the NIFGEN_ATTR_ARB_SAMPLE_RATE attribute.

Parent topic:

NI 5450 Baseband Interpolation Considerations

<!--NI_TOPIC bundle=ni-fgen path=ni-5450-basic-onboard-signal-processing-prope.html language=enus -->
## TOPIC 00632: NI 5450 Basic Onboard Signal Processing Properties

- bundle_id: `ni-fgen`
- source_path: `ni-5450-basic-onboard-signal-processing-prope.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5450-basic-onboard-signal-processing-prope.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following properties configure the OSP block: OSP Mode OSP Enabled Data Processing Mode IQ Rate Frequency Shift FIR Filter Type

### NI 5450 Basic Onboard Signal Processing Properties

The following properties configure the OSP block:

- OSP Mode

- OSP Enabled
- Data Processing
Mode
- IQ Rate

- Frequency Shift

- FIR Filter Type

Parent topic:

NI 5450 Onboard Signal Processing (OSP)

Related concepts:

- NI 5450 OSP Mode
- NI 5450 OSP Enabled
- NI 5450 Data Processing Mode
- NI 5450 IQ Rate
- NI 5450 Frequency Shift
- NI 5450 FIR Filter Type

<!--NI_TOPIC bundle=ni-fgen path=ni-5450-block-diagram.html language=enus -->
## TOPIC 00633: NI 5450 Block Diagram

- bundle_id: `ni-fgen`
- source_path: `ni-5450-block-diagram.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5450-block-diagram.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: This topic contains information about the NI 5450 top-level block diagram and descriptions of the individual blocks. The following list describes the individual blocks: Onboard Memory stores the waveform data and generation instructions that you load into the device. Clocking allows you to create yo

### NI 5450 Block Diagram

This topic contains information about the
NI 5450 top-level block diagram and descriptions of the
individual blocks.

[IMAGE alt='image' src='GUID-57DF8895-2C12-44F0-B9AD-2A1A920274D4-a5.gif']

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
 DAC device after any digital gain or onboard signal
processing is applied.

- The waveform data is sent from the 
 DAC to the 
 Analog Output path where the waveform data can be filtered.

- The Routing Matrix allows flexible routing of the PXI Trigger
lines and the external PFI lines.
- The Flatness Correction filter ensures consistent power level across all frequencies. Flatness Correction is disabled by default in NI-FGEN.

Parent topic:

NI 5450 Theory of Operation

<!--NI_TOPIC bundle=ni-fgen path=ni-5450-burst-trigger-mode.html language=enus -->
## TOPIC 00634: NI 5450 Burst Trigger Mode

- bundle_id: `ni-fgen`
- source_path: `ni-5450-burst-trigger-mode.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5450-burst-trigger-mode.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: In Burst trigger mode, calling the first Start trigger begins waveform generation. The waveform then generates continually. The following table provides more information about waveform generation behavior in Arbitrary Waveform and Arbitrary Sequence output modes. Output Mode Trigger Behavior Arbitra

### NI 5450 Burst Trigger Mode

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

NI 5450 Trigger Modes

Related concepts:

- NI 5450 Continuous Trigger Mode

<!--NI_TOPIC bundle=ni-fgen path=ni-5450-calibration.html language=enus -->
## TOPIC 00635: NI 5450 Calibration

- bundle_id: `ni-fgen`
- source_path: `ni-5450-calibration.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5450-calibration.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Before shipping your signal generator, NI calibrated your device to ensure that all features are within specifications. Calibration is a set of operations that compares the values indicated by a measuring instrument or measuring system to the corresponding values realized by external standards. You

### NI 5450 Calibration

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

NI 5450 NI 5450 Overview

<!--NI_TOPIC bundle=ni-fgen path=ni-5450-clk-in-connector.html language=enus -->
## TOPIC 00636: NI 5450 CLK IN Connector

- bundle_id: `ni-fgen`
- source_path: `ni-5450-clk-in-connector.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5450-clk-in-connector.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The CLK IN front panel connector can accept an external Reference clock, external Sample clock, or external Sample clock timebase. Do not change the external clocks while generating waveforms. Only modify the frequency of the external clock before you start the waveform generation or after you sto

### NI 5450 CLK IN Connector

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

Reference
Clock

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

#### External Sample Clock Timebase Input

The CLK IN connector
also can receive an external Sample clock timebase. Refer to the 
*device
specifications* for the allowable external Sample clock timebase
frequencies and signal characteristics.

Configure the Sample clock timebase source with the 
Sample Clock Timebase Source and Sample Clock Timebase Rate properties or the 
NIFGEN_ATTR_SAMPLE_CLOCK_TIMEBASE_SOURCE and NIFGEN_ATTR_SAMPLE_CLOCK_TIMEBASE_RATE attributes. The device uses the internal sample clock timebase by
default.

Parent topic:

NI 5450 Front Panel

Related concepts:

- NI 5450 Reference Clock

<!--NI_TOPIC bundle=ni-fgen path=ni-5450-clk-out-connector.html language=enus -->
## TOPIC 00637: NI 5450 CLK OUT Connector

- bundle_id: `ni-fgen`
- source_path: `ni-5450-clk-out-connector.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5450-clk-out-connector.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The CLK OUT connector is typically used as an output terminal to provide a clock signal that can be shared by other devices. The CLK OUT connector is designed to allow the NI 5450 to generate high speed clock signals with very low jitter. As an output, the CLK OUT line routes a signal out from the f

### NI 5450 CLK OUT Connector

The CLK OUT connector is typically used as an output terminal to provide a clock signal that can be shared by other devices. The CLK OUT connector is designed to allow the NI 5450 to generate high speed clock signals with very low jitter.

As an output, the CLK OUT line routes a signal out
from the following sources:

- PLL Reference clock source
- Sample Clock Out (with / K where K is an integer used to divide the Sample
clock)
- Sample clock timebase (with / M where M is an integer used to divide the Sample clock
timebase frequency)

Refer to the 
*device specifications* for information about the signal
characteristics for the CLK OUT connector.

Parent topic:

NI 5450 Front Panel

<!--NI_TOPIC bundle=ni-fgen path=ni-5450-clocking-options.html language=enus -->
## TOPIC 00638: NI 5450 Clocking Options

- bundle_id: `ni-fgen`
- source_path: `ni-5450-clocking-options.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5450-clocking-options.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5450 uses a sample clock to generate data. In conjunction with the sample clock, you can also use a reference clock, or less commonly, a sample clock timebase. These clocks are defined as follows: Sample clock: The clock that drives new output data to the DACs. It runs at the sample rate. In

### NI 5450 Clocking Options

The NI 5450 uses a sample clock to generate data. In conjunction with the sample clock, you can also use a reference clock, or less commonly, a sample clock timebase. These clocks are defined as follows:

- Sample clock: The clock that drives new output data to the DACs. It runs at the sample rate. In I/Q generation, the sample rate is an interpolated multiple of the I/Q rate.
- Reference clock — An external clock source used to regulate the frequency and stability of an internally generated sample clock. The NI 5450 onboard PLLs lock to the reference clock.
- Sample Clock Timebase: A high-speed multiple of the sample clock used internally. In general, NI-FGEN manages this clock for you, except in advanced cases where you import or export a sample clock timebase.

The NI 5450 can generate all necessary clocks internally, or you can provide any one of the three clocks as an input. Therefore, there are four main clocking scenarios:

- Internal Sample clock —The onboard clock is used as the
sample clock. The NI 5450 onboard clock combines the low jitter of a divide-down clock with the high resolution of a DDS-based clock. Therefore, there is no difference between the divide down, high resolution, and automatic clock modes for the NI 5450.
- Reference clock— This case is identical to the internal sample clock case, except that the internal sample clock is phase-locked to an external reference clock input. This can facilitate synchronization among devices or can allow you to improve the specifications of the sample clock by training it to a high-quality external clock.
- External Sample clock — An external clock input is used as the sample clock. The external clock passes through a PLL and may optionally be multiplied by the PLL.
- External Sample clock timebase — A high-speed external clock input is used as the basis for the sample clock. The sample clock runs at the rate of the input clock or at an integer division. An external sample clock timebase is an advanced clocking case that allows you to bypass onboard PLLs to preserve the specifications of your input clock.

The following table shows the valid NI-FGEN
property or attribute value combinations that can be used to
configure the clock settings for
an internal Sample clock, an external Sample clock, or a Reference
clock. The term 
Update clock is synonymous with 
Sample clock.

| Sample Clock Source* | Reference Clock* |
| --- | --- |
| "OnboardClk" (default) | "None" (default) |
| "PXI_CLK10" |  |
| "ClkIn" |  |
| "ClkIn" | Not Applicable |
| *These column headings refer to NI-FGEN properties. The attributes that correspond to these properties are NIFGEN_ATTR_SAMPLE_CLOCK_SOURCE and NIFGEN_ATTR_REFERENCE_CLOCK_SOURCE. The values in the columns represent the values that can be set on these properties or attributes. Settings that line up horizontally show valid combinations of the NI-FGEN settings. |  |

Parent topic:

NI 5450 Clocking

Related concepts:

- NI 5450 Reference Clock
- NI 5450 Internal Sample Clock
- NI 5450 External Sample Clock
- NI 5450 External Sample Clock Timebase

<!--NI_TOPIC bundle=ni-fgen path=ni-5450-clocking.html language=enus -->
## TOPIC 00639: NI 5450 Clocking

- bundle_id: `ni-fgen`
- source_path: `ni-5450-clocking.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5450-clocking.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5450 has a Sample clock rate of 12.2 kHz to 400 MHz. The timing of the device is very flexible, and you have multiple choices for deriving the Sample clock. There are modes for deriving the Sample clock from the internal Sample clock timebase, as well as modes to provide external clocks. You

### NI 5450 Clocking

The NI 5450 has a Sample clock
rate of 12.2 kHz to 400 MHz. The timing of the device
is very flexible, and you have multiple choices for deriving the
Sample clock. There are modes for deriving the Sample clock from
the internal Sample clock timebase, as well as modes to provide
external clocks. You also have several choices for providing the
frequency reference for the onboard phase-locked loop.

[IMAGE alt='image' src='GUID-9F461095-5466-4410-9491-3E0E691C11D6-a5.gif']

Related Topics

*Clocking Options*

*Internal Sample Clock
Sources*

*Reference Clock*

*External Sample
Clock Sources*
*External Sample Clock Timebase*

*Exporting Clocks*

Parent topic:

NI 5450 Theory of Operation

Related concepts:

- NI 5450 Clocking Options
- NI 5450 Internal Sample Clock
- NI 5450 Reference Clock
- NI 5450 External Sample Clock
- NI 5450 External Sample Clock Timebase
- NI 5450 Exporting Clocks

<!--NI_TOPIC bundle=ni-fgen path=ni-5450-common-onboard-signal-processing-appl.html language=enus -->
## TOPIC 00640: NI 5450 Common Onboard Signal Processing Applications

- bundle_id: `ni-fgen`
- source_path: `ni-5450-common-onboard-signal-processing-appl.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5450-common-onboard-signal-processing-appl.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The OSP block is particularly useful for the following common applications: Baseband Interpolation Baseband I/Q Interpolation

### NI 5450 Common Onboard Signal Processing Applications

The OSP block is particularly useful for the
following common applications:

- Baseband
Interpolation
- Baseband I/Q
Interpolation

Parent topic:

NI 5450 Onboard Signal Processing (OSP)

Related concepts:

- NI 5450 Baseband Interpolation
- NI 5450 Baseband I/Q Interpolation

<!--NI_TOPIC bundle=ni-fgen path=ni-5450-continuous-trigger-mode.html language=enus -->
## TOPIC 00641: NI 5450 Continuous Trigger Mode

- bundle_id: `ni-fgen`
- source_path: `ni-5450-continuous-trigger-mode.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5450-continuous-trigger-mode.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The waveform you downloaded generates continuously after receiving one Start trigger. All Start triggers after the first Start trigger are ignored. The following table provides more information about waveform generation behavior in Arbitrary Waveform and Arbitrary Sequence output modes. Output Mode

### NI 5450 Continuous Trigger Mode

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

NI 5450 Trigger Modes

<!--NI_TOPIC bundle=ni-fgen path=ni-5450-data-mask.html language=enus -->
## TOPIC 00642: NI 5450 Data Mask

- bundle_id: `ni-fgen`
- source_path: `ni-5450-data-mask.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5450-data-mask.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The signal generator supports analog data masks and static values. The data mask allows you to shield bits of the data to be replaced with the corresponding static value bits. For example, a mask of 0xFF00 and a static value of 0xAAAA applied to a DC waveform with a value of 0x1111 produces a DC wav

### NI 5450 Data Mask

The signal generator supports analog
data masks and static values. The data mask allows you to shield
bits of the data to be replaced with the corresponding static value
bits. For example, a mask of 0xFF00 and a static value of 0xAAAA
applied to a DC waveform with a value of 0x1111 produces a DC
waveform with a value of 0x11AA.

NI-FGEN supports separate and independent analog
and digital data masks and static values. The analog data mask and
analog static value apply to the digital data applied to the DAC,
and ultimately to the signal on the analog output terminal. You can configure an analog data mask by calling the 
Analog Data
Mask or 
Analog
Static Value properties or the 
NIFGEN_ATTR_ANALOG_DATA_MASK and 
NIFGEN_ATTR_ANALOG_STATIC_VALUE attributes.

Parent topic:

NI 5450 NI 5450 Overview

<!--NI_TOPIC bundle=ni-fgen path=ni-5450-data-processing-mode.html language=enus -->
## TOPIC 00643: NI 5450 Data Processing Mode

- bundle_id: `ni-fgen`
- source_path: `ni-5450-data-processing-mode.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5450-data-processing-mode.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Data Processing mode determines whether the OSP block uses only the I signal path to generate waveforms or uses the I and Q signal paths to generate complex waveforms. If the waveform data is configured for real data points by setting the Data Processing Mode property or the NIFGEN_ATTR_OSP_DATA_PRO

### NI 5450 Data Processing Mode

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

NI 5450 Basic Onboard Signal Processing Properties

<!--NI_TOPIC bundle=ni-fgen path=ni-5450-differential-channel-connectors.html language=enus -->
## TOPIC 00644: NI 5450 Differential Channel Connectors

- bundle_id: `ni-fgen`
- source_path: `ni-5450-differential-channel-connectors.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5450-differential-channel-connectors.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The CH 0+/− and CH 1+/− connectors are the analog waveform output terminals. These connectors provide differential waveform output; they cannot be used for single-ended operation. The connectors must terminate into balanced loads. The maximum output levels from these connectors depend on the type of

### NI 5450 Differential Channel Connectors

The CH 0+/− and CH 1+/− connectors are the analog waveform
output terminals. These connectors provide differential waveform output; they cannot be used for single-ended operation. The connectors must terminate into balanced loads. The maximum output levels from these connectors
depend on the type of load termination. For example, if the output of the device
terminates into a balanced 50 Ω load with *flatness correction* disabled, the maximum output levels
are ±0.5 V, while the maximum output levels are ±1.0  when the
device terminates into a high-impedance load (HiZ). This difference
is illustrated in the following figure.

[IMAGE alt='image' src='GUID-F84E7C28-AF33-4B6D-B08D-C46EED58DE0A-a5.gif']

If the output terminates into any other load, the
levels are defined by the following formula:

V<sub>out</sub>
 = ± [ 
R<sub>L</sub>
 / ( 
R<sub>L</sub>
 + 
R<sub>O</sub>
 ) ] × 2 V

where

V<sub>out</sub>
 is the maximum peak output voltage level

R<sub>L</sub>
 is the load impedance in ohms

O

Note

out

Set the amplitude of the generated output
signal in terms of peak voltage by setting the gain value. NI-FGEN
calculates and sets the correct amount of attenuation required for
the desired gain value. Configure the output signal amplitude by calling the
 
Arbitrary Waveform Gain property or
NIFGEN_ATTR_ARB_GAIN attribute.

#### Load Impedance Compensation

The NI 5450 has the ability to configure the
output signal amplitude based on a user-configured load impedance
setting. This capability is desirable when you use the NI 5450
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

NI 5450 Front Panel

Related concepts:

- NI 5450 Flatness Correction

<!--NI_TOPIC bundle=ni-fgen path=ni-5450-digital-gain.html language=enus -->
## TOPIC 00645: NI 5450 Digital Gain

- bundle_id: `ni-fgen`
- source_path: `ni-5450-digital-gain.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5450-digital-gain.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Digital gain multiplies waveform data by a factor you specify in the Digital Gain property or the NIFGEN_ATTR_DIGITAL_GAIN attribute before converting the data to an analog signal in the DAC. Digital gain can be changed during generation without the glitches caused by switching that are common when

### NI 5450 Digital Gain

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

NI 5450 Waveform Amplitude Control

<!--NI_TOPIC bundle=ni-fgen path=ni-5450-events.html language=enus -->
## TOPIC 00646: NI 5450 Events

- bundle_id: `ni-fgen`
- source_path: `ni-5450-events.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5450-events.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use events to indicate when a specific hardware condition has been met on the NI 5450. An event is a signal generated by the NI device at a device state. The NI 5450 supports Ready for Start, Started, Data Marker, Marker, and Done events. The NI 5450 also supports the use of event delays. Re

### NI 5450 Events

You can use *events* to indicate when a specific
hardware condition has been met on the NI 5450. An event is a
signal generated by the NI device at a device state. The NI 5450
supports Ready for Start, Started, *Data Marker*, *Marker*, and Done
events. The NI 5450 also supports the use of *event delays*.

#### Related Topics

*Creating a Marker
Event*

*Creating a Data Marker
Event*

Parent topic:

NI 5450 NI 5450 Overview

Related concepts:

- Events
- Data Marker Events
- Marker Events
- Event Delays
- Creating a Marker Event
- Creating a Data Marker Event

<!--NI_TOPIC bundle=ni-fgen path=ni-5450-exporting-clocks.html language=enus -->
## TOPIC 00647: NI 5450 Exporting Clocks

- bundle_id: `ni-fgen`
- source_path: `ni-5450-exporting-clocks.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5450-exporting-clocks.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5450 provides resources for exporting your clocks and multiple destinations for routing. The following table shows the available clock signals that can be routed to devices external to the signal generator and the destination options. The PFI outputs have a bandwidth of 200 MHz. The PXI Trigg

### NI 5450 Exporting Clocks

The NI 5450 provides resources for exporting your clocks and multiple destinations for
routing.

[IMAGE alt='image' src='GUID-A16BC157-0B86-4AD7-9DBA-FA1CACD04629-a5.gif']

Note

| Clock to be Exported | Destination Options |  |  |
| --- | --- | --- | --- |
|  | CLK OUT | PFI<0..1> | PXI_Trig<0..6> |
| Sample Clock/K | K ≥1 | K ≥2 | K ≥2 |
| SCTB/M | M ≥1 | M ≥2 | M ≥2 |
| Reference Clock | Always | Always | Always |
| Note: All divisors have a default value of 1. If a divisor is greater than 1, the divided clock output is not phase aligned with waveform generation. Refer to the Exporting Signals topic for more information. |  |  |  |

For synchronization purposes, the
NI 5450 allows you to export your clocks 
so that other devices can share the timing of the NI 5450. The following sections describe the possible clock routing configurations.

#### Sample Clock

The Sample clock can be routed to the CLK OUT front panel SMA connector.

Additionally, the exported clock can be divided
down by an integer value (no less than 2) and exported to
the PFI <0..1> connectors, the CLK OUT connector, or the PXI_Trig<0..6>
lines. Refer to the 
Exported Sample Clock Divisor property or the 
NIFGEN_ATTR_EXPORTED_SAMPLE_CLOCK_DIVISOR attribute for more information about configuring the Sample
clock divisor.

#### Sample Clock Timebase

The Sample clock timebase can be routed to the CLK OUT front panel SMA connector.

Additionally, the exported clock can be divided
down by an integer value and exported to the
PFI <0..1> connectors, the CLK OUT connector, or the PXI_Trig<0..6>
lines. You can configure the Sample clock divisor by calling the 
Exported Sample Clock Timebase Divisor property or the 
NIFGEN_ATTR_EXPORTED_SAMPLE_CLOCK_TIMEBASE_DIVISOR attribute.

#### Reference Clock

The Reference clock is the
clock that is configured for the signal generator
phase-locked loop circuit to use as a reference. A clock configured as a PLL Reference clock source is available for exporting. The Reference clock can be routed to
the PFI <0..1> front panel SMB connectors, the CLK OUT front panel SMA connector, or the PXI_Trig<0..6>
lines on the PXI trigger bus.

Note

#### Destination Options

The following sections define the destinations for
exported clocks.

PFI <0..1>—The Sample clock (when K ≥2), the Sample clock timebase (when M ≥2), and the
Reference clock can be exported to the PFI 0 and PFI 1 SMB
connectors on the front panel to synchronize external devices. You
must configure the device to export the desired clock to the PFI SMB connectors.

CLK OUT—The Sample clock, the Sample clock timebase, and the
Reference clock can be exported to the CLK OUT SMA
connectors on the front panel to synchronize external devices. You
must configure the device to export the desired clock to the CLK OUT SMA connector.

PXI_Trig<0..6>—Sample clock (when K ≥2), the Sample clock timebase (when M ≥2), and the
Reference clock can be exported to the PXI_Trig lines. The PXI standards allow for devices to route signals
to other devices in your PXI Express chassis to enhance device-to-device
synchronization. Refer to the chassis documentation for
specifications to ensure the reference signal is within tolerance.
You must configure the device to export the desired clock to the
PXI_Trig line.

Refer to 
niFgen Export
Signal VI or the 
niFgen_ExportSignal function for more information about configuring the
destinations for the desired clock signal.

Parent topic:

NI 5450 Clocking

Related concepts:

- NI 5450 Exporting Signals

<!--NI_TOPIC bundle=ni-fgen path=ni-5450-exporting-signals.html language=enus -->
## TOPIC 00648: NI 5450 Exporting Signals

- bundle_id: `ni-fgen`
- source_path: `ni-5450-exporting-signals.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5450-exporting-signals.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The signal generator contains seven PXI trigger lines that are available for sending signal generator-specific information to other devices that have PXI trigger bus connectors. The signal generator has connectors on the front panel to route signals to devices external to the PXI Express chassis. Th

### NI 5450 Exporting Signals

The signal generator contains seven PXI trigger
lines that are available for sending signal generator-specific
information to other devices that have PXI trigger bus
connectors.

Signal Routing

Note

|  |  | Destination |  |  |
| --- | --- | --- | --- | --- |
| PXI_TRIG<0..6> | PFI 0 and PFI 1 Connectors | CLK OUT |  |  |
| Exported Clocks, Triggers, and Events | Sample Clock | Yes (when /K with K ≥2) | Yes (when /K with K ≥2) | Yes |
| Sample Clock Timebase | Yes (when /M with M ≥2) | Yes (when /M with M ≥2) | Yes |  |
| PLL Reference Source | Yes | Yes | Yes |  |
| Out Start trigger | Yes | Yes | No |  |
| Marker Event | Yes | Yes | No |  |

Sample Clock

Note

Sample Clock Timebase

Note

Reference clock–A clock signal
that is only available when a Reference clock source for the PLLs has been
configured. The clock is the source selected as the PLL Reference
clock source.

Start trigger out–A signal generated by the
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
Generation mode waveform generation to any of the PXI trigger lines
or the PFI 0 and PFI 1 connectors.
- The signal generator Start trigger output signal to other
devices through any of the PXI trigger lines
or the PFI 0 and PFI 1 connectors.
- The signal generator Sample clock signal to other devices
through any of the PXI trigger lines or front panel
connectors.
- The signal generator Sample clock timebase signal to other devices
through any of the PXI trigger lines or front panel
connectors.
- The PLL Reference clock source to other devices through any of
the PXI trigger lines or front panel connectors.

In NI-FGEN, the PXI trigger lines are referred to
as RTSI<0..6>. The correlation between PXI_TRIG< 
x> and RTSI< 
x> is one to one. For more information about
configuring and routing the device internal signals, refer to the 
niFgen Export Signal VI
or the 
niFgen_ExportSignal function.

Parent topic:

NI 5450 NI 5450 Overview

Related concepts:

- NI 5450 Signal Routing

<!--NI_TOPIC bundle=ni-fgen path=ni-5450-external-sample-clock-timebase.html language=enus -->
## TOPIC 00649: NI 5450 External Sample Clock Timebase

- bundle_id: `ni-fgen`
- source_path: `ni-5450-external-sample-clock-timebase.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5450-external-sample-clock-timebase.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: An external sample clock timebase is an external source that drives the output DACs almost directly. The sample clock rate can equal the sample clock timebase rate or be an integer division. You can set the Sample clock timebase source by calling the Sample Clock Timebase Source property or the NIFG

### NI 5450 External Sample Clock Timebase

An external sample clock timebase is an external
source that drives the output DACs almost directly. The sample clock rate can equal the sample clock timebase rate or be an integer division.

[IMAGE alt='image' src='GUID-398511A7-043F-4E7A-ABDC-8946FB579C2F-a5.gif']

NIFGEN_ATTR_SAMPLE_CLOCK_TIMEBASE_SOURCE

NIFGEN_ATTR_SAMPLE_CLOCK_TIMEBASE_RATE

Caution

NIFGEN_ATTR_EXPORTED_SAMPLE_CLOCK_TIMEBASE_OUTPUT_TERMINAL

Note

device specifications

Parent topic:

NI 5450 Clocking Options

<!--NI_TOPIC bundle=ni-fgen path=ni-5450-external-sample-clock.html language=enus -->
## TOPIC 00650: NI 5450 External Sample Clock

- bundle_id: `ni-fgen`
- source_path: `ni-5450-external-sample-clock.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5450-external-sample-clock.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5450 can accept an external clock to directly drive the Sample clock. When using an external Sample clock, the frequency stability and accuracy of the Sample clock is determined by the provided external Sample clock. The following figure shows possible Sample Clock paths. You can set the cloc

### NI 5450 External Sample Clock

The NI 5450 can accept an
external clock to directly drive the Sample clock. When using an
external Sample clock, the frequency stability and accuracy of the
Sample clock is determined by the provided external Sample
clock.

The following figure shows possible Sample
Clock paths.

[IMAGE alt='image' src='GUID-87D5D904-8A0D-42AD-AA11-DA16314DAA98-a5.gif']

You can set the clock source by calling the
niFgen
Configure Sample Clock Source VI or the 
niFgen_ConfigureSampleClockSource function.

If the external sample clock differs from the desired sample rate, you can multiply the clock by calling the
External Sample Clock Multiplier property or the 
NIFGEN_ATTR_EXTERNAL_SAMPLE_CLOCK_MULTIPLIER attribute.

niFgen_ConfigureSampleRate

Note

device specifications

#### External Sample Clock Considerations

The NI 5450 incorporates
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
reprograms the NI 5450 for the new settings,
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

NI 5450 Clocking Options

<!--NI_TOPIC bundle=ni-fgen path=ni-5450-filtering-and-interpolation.html language=enus -->
## TOPIC 00651: NI 5450 Filtering and Interpolation

- bundle_id: `ni-fgen`
- source_path: `ni-5450-filtering-and-interpolation.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5450-filtering-and-interpolation.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The filtering and interpolation stage of the OSP block increases the effective sample rate of the signal generator while protecting the frequency spectrum of the interpolated data from images. This protection occurs when the data passes through a lowpass filter after zero stuffing. The frequency res

### NI 5450 Filtering and Interpolation

The filtering and interpolation stage of the 
*OSP* block increases the effective
sample rate of the signal generator while protecting the frequency
spectrum of the interpolated data from images. This protection
occurs when the data passes through a lowpass filter after zero
stuffing. The frequency response of the low pass filter can be
changed with the 
Filter
Type property or the 
NIFGEN_ATTR_OSP_FIR_FILTER_TYPE attribute.

[IMAGE alt='image' src='GUID-C1BDF7AF-B534-458E-A2A9-BA1D9A6DD7BE-a5.gif']

Parent topic:

NI 5450 Onboard Signal Processing Components

Related concepts:

- NI 5450 Onboard Signal Processing (OSP)

<!--NI_TOPIC bundle=ni-fgen path=ni-5450-filtering-effects.html language=enus -->
## TOPIC 00652: NI 5450 Filtering Effects

- bundle_id: `ni-fgen`
- source_path: `ni-5450-filtering-effects.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5450-filtering-effects.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The delay from the time at which the device receives a trigger to the time at which the analog output signal is generated increases if the digital and/or analog filters in the Analog Output path are enabled. In the case of digital filtering, delay also increases with increase in interpolation. Enabl

### NI 5450 Filtering Effects

Analog Output path

onboard signal processing block

Note

Refer to the 
*device
specifications* for the delay from trigger to analog output
based on different filtering options.

Parent topic:

NI 5450 Analog Output

Related concepts:

- NI 5450 Analog Output
- NI 5450 Onboard Signal Processing (OSP)

<!--NI_TOPIC bundle=ni-fgen path=ni-5450-filtering-effects_2.html language=enus -->
## TOPIC 00653: NI 5450 Filtering Effects

- bundle_id: `ni-fgen`
- source_path: `ni-5450-filtering-effects_2.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5450-filtering-effects_2.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The delay from the time at which the device receives a trigger to the time at which the analog output signal is generated increases if the digital and/or analog filters in the Analog Output path are enabled. In the case of digital filtering, delay also increases with increase in interpolation. Enabl

### NI 5450 Filtering Effects

Analog Output path

onboard signal processing block

Note

Refer to the 
*device
specifications* for the delay from trigger to analog output
based on different filtering options.

Parent topic:

NI 5450 Triggering

<!--NI_TOPIC bundle=ni-fgen path=ni-5450-fir-filter-type-flat.html language=enus -->
## TOPIC 00654: NI 5450 FIR Filter Type: Flat

- bundle_id: `ni-fgen`
- source_path: `ni-5450-fir-filter-type-flat.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5450-fir-filter-type-flat.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Passband Value: 0.40 This lowpass filter is designed to give a flat response until the passband value. The passband value is a fraction of the I/Q Rate coming into the FIR filter. Use the Flat Filter Passband property or the NIFGEN_ATTR_OSP_FIR_FILTER_FLAT_PASSBAND attribute to set the passband valu

### NI 5450 FIR Filter Type: Flat

Passband Value: 0.40

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

[IMAGE alt='image' src='GUID-1343D8E2-F83F-4310-A25D-36DA2801503C-a5.gif']

Parent topic:

NI 5450 FIR Filter Types

Related concepts:

- NI 5450 I/Q Rate Controller

<!--NI_TOPIC bundle=ni-fgen path=ni-5450-fir-filter-type-raised-cosine.html language=enus -->
## TOPIC 00655: NI 5450 FIR Filter Type: Raised Cosine

- bundle_id: `ni-fgen`
- source_path: `ni-5450-fir-filter-type-raised-cosine.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5450-fir-filter-type-raised-cosine.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Alpha Values: 0.1 to 0.4 This lowpass filter is commonly used in communications applications. The passband of the raised cosine filter with the roll-off factor, α, stops at 0.5 × (1 − α) times the I/Q Rate. The stopband of the raised cosine filter begins at 0.5 × (1 + α) times the I/Q Rate. The tran

### NI 5450 FIR Filter Type: Raised Cosine

Alpha Values: 0.1 to 0.4

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

Parent topic:

NI 5450 FIR Filter Types

Related concepts:

- NI 5450 I/Q Rate Controller

<!--NI_TOPIC bundle=ni-fgen path=ni-5450-fir-filter-type-root-raised-cosine.html language=enus -->
## TOPIC 00656: NI 5450 FIR Filter Type: Root Raised Cosine

- bundle_id: `ni-fgen`
- source_path: `ni-5450-fir-filter-type-root-raised-cosine.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5450-fir-filter-type-root-raised-cosine.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Alpha Values: 0.1 to 0.4 This lowpass filter is commonly used in communications applications. The passband of the root raised cosine filter with the roll-off factor, α, stops at 0.5 × (1 − α) times the I/Q Rate. The stopband of the root raised cosine filter begins at 0.5 × (1 + α) times the I/Q Rate

### NI 5450 FIR Filter Type: Root Raised Cosine

Alpha Values: 0.1 to 0.4

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
Raised Cosine Filter Alpha property or the 
NIFGEN_ATTR_OSP_FIR_FILTER_RAISED_COSINE_ALPHA attribute to set the 
α value.

The following diagram shows an ideal root raised
cosine filter response with an 
α of 0.5. The frequency
axis is scaled as a fraction of the 
I/Q
Rate.

[IMAGE alt='image' src='GUID-AAD8865C-5B03-4E67-8E39-2FD2389E6EBA-a5.gif']

Parent topic:

NI 5450 FIR Filter Types

Related concepts:

- NI 5450 I/Q Rate Controller

<!--NI_TOPIC bundle=ni-fgen path=ni-5450-fir-filter-type.html language=enus -->
## TOPIC 00657: NI 5450 FIR Filter Type

- bundle_id: `ni-fgen`
- source_path: `ni-5450-fir-filter-type.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5450-fir-filter-type.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the FIR Filter Type property or the NIFGEN_ATTR_OSP_FIR_FILTER_TYPE attribute to set the FIR filter type. The following filter types are supported: Flat Raised Cosine Root Raised Cosine

### NI 5450 FIR Filter Type

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

NI 5450 Basic Onboard Signal Processing Properties

Related concepts:

- NI 5450 FIR Filter Type: Flat
- NI 5450 FIR Filter Type: Raised Cosine
- NI 5450 FIR Filter Type: Root Raised Cosine

<!--NI_TOPIC bundle=ni-fgen path=ni-5450-fir-filter-types.html language=enus -->
## TOPIC 00658: NI 5450 FIR Filter Types

- bundle_id: `ni-fgen`
- source_path: `ni-5450-fir-filter-types.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5450-fir-filter-types.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: There are a number of built-in low-pass pulse-shaping filters available in NI-FGEN. Because the coefficients are scaled for unity-gain, the filters may overflow if transients (such as step response) are presented at the input of the filter. Use the Filter Type property or the NIFGEN_ATTR_OSP_FIR_FIL

### NI 5450 FIR Filter Types

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

#### Digital Filter Overflow

FIR filters may overflow. If an overflow occurs, data is clipped and NI-FGEN returns an error.

Digital filter overflows can be caused by transients. Transients can occur as an abrupt jump at the beginning of a waveform or they may be present in the data you supply. NI-FGEN ignores overflows that are caused by transients at the beginning of a waveform. You can choose to ignore overflow errors caused by transients present in your data with the 
OSP Overflow Error Reporting property or the 
NIFGEN_ATTR_OSP_OVERFLOW_ERROR_REPORTING attribute.

Parent topic:

NI 5450 Onboard Signal Processing Components

Related concepts:

- NI 5450 FIR Filter Type
- NI 5450 FIR Filter Type: Flat
- NI 5450 FIR Filter Type: Raised Cosine
- NI 5450 FIR Filter Type: Root Raised Cosine

<!--NI_TOPIC bundle=ni-fgen path=ni-5450-flatness-correction.html language=enus -->
## TOPIC 00659: NI 5450 Flatness Correction

- bundle_id: `ni-fgen`
- source_path: `ni-5450-flatness-correction.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5450-flatness-correction.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5450 can use flatness correction to ensure a consistent power level across frequencies when generating arbitrary waveforms or I/Q data. Flatness correction is disabled by default in NI-FGEN. You can enable or disable flatness correction by setting the Flatness Correction Enabled property or t

### NI 5450 Flatness Correction

The NI 5450 can use flatness correction to ensure
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

NI 5450 Waveform Amplitude Control

Related concepts:

- NI 5450 Analog Gain Settings

<!--NI_TOPIC bundle=ni-fgen path=ni-5450-frequency-shift.html language=enus -->
## TOPIC 00660: NI 5450 Frequency Shift

- bundle_id: `ni-fgen`
- source_path: `ni-5450-frequency-shift.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5450-frequency-shift.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Frequency Shift property or the NIFGEN_ATTR_OSP_FREQUENCY_SHIFT attribute can be used to shift the frequency of a baseband signal. This property can only be used when the OSP mode has been configured for baseband by setting the OSP Mode property or the NIFGEN_ATTR_OSP_MODE attribute. When you ar

### NI 5450 Frequency Shift

The Frequency Shift property or the NIFGEN_ATTR_OSP_FREQUENCY_SHIFT attribute can be used to shift the frequency of a baseband signal. This property can only be used when the OSP mode has been configured for baseband by setting the OSP Mode property or the NIFGEN_ATTR_OSP_MODE attribute.

NIFGEN_ATTR_OSP_FREQUENCY_SHIFT

Note

Parent topic:

NI 5450 Basic Onboard Signal Processing Properties

<!--NI_TOPIC bundle=ni-fgen path=ni-5450-front-panel.html language=enus -->
## TOPIC 00661: NI 5450 Front Panel

- bundle_id: `ni-fgen`
- source_path: `ni-5450-front-panel.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5450-front-panel.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the NI PXIe-5450 front panel. This front panel has two SMB connectors and six SMA connectors. The CLK IN SMA connector accepts an external clock that can be used as a Reference clock, a Sample clock, or a Sample clock timebase. The CLK OUT SMA connector provides a clock si

### NI 5450 Front Panel

The following figure shows the NI PXIe-5450 front panel. This front panel has
two SMB connectors and six SMA connectors.

[IMAGE alt='image' src='GUID-CA14E7B8-82FC-45C1-B020-B2C89171B28A-a5.gif']

The 
*CLK IN* SMA connector accepts an external clock that can be used as a Reference clock, a Sample clock, or a Sample clock timebase.

The 
*CLK OUT* SMA connector provides a clock signal that can be shared by other devices.

The 
*PFI 0 and PFI 1* SMB
connectors are bidirectional connections that can accept a trigger from an external source and can start or step through waveform generation or route signals from several clock, event, and trigger sources.

The 
*CH 0+/I+* SMA connector provides differential waveform output for channel 0.

The 
*CH 0−/I−* SMA connector provides complementary differential waveform output for channel 0.

The 
*CH 1+/Q+* SMA connector provides differential waveform output for channel 1.

The 
*CH 1−/Q−* SMA connector provides complementary differential waveform output for channel 1.

Parent topic:

NI 5450 NI 5450 Overview

Related concepts:

- NI 5450 CLK IN Connector
- NI 5450 CLK OUT Connector
- NI 5450 PFI Connectors
- NI 5450 Differential Channel Connectors

<!--NI_TOPIC bundle=ni-fgen path=ni-5450-hardware-state-diagram.html language=enus -->
## TOPIC 00662: NI 5450 Hardware State Diagram

- bundle_id: `ni-fgen`
- source_path: `ni-5450-hardware-state-diagram.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5450-hardware-state-diagram.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following diagram shows the hardware states of the signal generator. The signal generator can be in one of the following six basic states during the course of operation. Idle—The device is not generating a waveform. All session properties or attributes can be programmed in the Idle state. In the

### NI 5450 Hardware State Diagram

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

NI 5450 Theory of Operation

Related concepts:

- Programming State Model

<!--NI_TOPIC bundle=ni-fgen path=ni-5450-i-q-rate-controller.html language=enus -->
## TOPIC 00663: NI 5450 I/Q Rate Controller

- bundle_id: `ni-fgen`
- source_path: `ni-5450-i-q-rate-controller.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5450-i-q-rate-controller.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The I/Q rate component pulls the data from the generation engine such that a new sample is returned once every Total_OSP_Interpolation Sample clocks. The Total_OSP_Interpolation is the amount of interpolation applied within the Filtering and Interpolation component, and does not include the DAC in

### NI 5450 I/Q Rate Controller

Note

Parent topic:

NI 5450 Onboard Signal Processing Components

<!--NI_TOPIC bundle=ni-fgen path=ni-5450-identifying-module-revision.html language=enus -->
## TOPIC 00664: NI 5450 Identifying Module Revision

- bundle_id: `ni-fgen`
- source_path: `ni-5450-identifying-module-revision.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5450-identifying-module-revision.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: NI PXIe-5450 Specifications and features may vary according to the revision letter of the module. To determine the revision letter of your NI 5450, query the Module Revision property or the NIFGEN_ATTR_MODULE_REVISION attribute.

### NI 5450 Identifying Module Revision

*NI PXIe-5450 Specifications* and features may vary according to the revision letter of the module. To determine the revision letter of your NI 5450, query the Module Revision property or the NIFGEN_ATTR_MODULE_REVISION attribute.

Parent topic:

NI 5450 NI 5450 Overview

<!--NI_TOPIC bundle=ni-fgen path=ni-5450-interleaved-waveform-data.html language=enus -->
## TOPIC 00665: NI 5450 Interleaved Waveform Data

- bundle_id: `ni-fgen`
- source_path: `ni-5450-interleaved-waveform-data.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5450-interleaved-waveform-data.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: In order to write data to multiple channels on the same device simultaneously, the data must be interleaved. Interleaved samples prioritize samples before channels, such that the array lists the first sample from every channel in the task, then the second sample from every channel, up to the last sa

### NI 5450 Interleaved Waveform Data

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

NI 5450 Multichannel Configuration

<!--NI_TOPIC bundle=ni-fgen path=ni-5450-internal-sample-clock.html language=enus -->
## TOPIC 00666: NI 5450 Internal Sample Clock

- bundle_id: `ni-fgen`
- source_path: `ni-5450-internal-sample-clock.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5450-internal-sample-clock.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5450 can derive a Sample clock from its main internal timing source—the Sample clock timebase. The signal generator provides a high-precision 400 MHz oscillator clock source for the Sample clock timebase. The NI 5450 has a high-resolution internal clock. You can change the frequency of this c

### NI 5450 Internal Sample Clock

The NI 5450 can derive a Sample
clock from its main internal timing source—the Sample clock
timebase. The signal generator provides a high-precision
400 MHz oscillator clock
source for the Sample clock timebase.

[IMAGE alt='image' src='GUID-B9DD67D6-16F7-4555-9B06-9E6AB1B3F51A-a5.gif']

The NI 5450 has a high-resolution internal clock. You can change the frequency of this clock by calling the niFgen Set Sample Rate VI or the niFgen_ConfigureSampleRate function. When you set a desired sample rate, NI-FGEN will internally determine and apply appropriate divide-down factors.

Parent topic:

NI 5450 Clocking Options

<!--NI_TOPIC bundle=ni-fgen path=ni-5450-iq-rate.html language=enus -->
## TOPIC 00667: NI 5450 IQ Rate

- bundle_id: `ni-fgen`
- source_path: `ni-5450-iq-rate.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5450-iq-rate.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The IQ Rate property or the NIFGEN_ATTR_OSP_IQ_RATE attribute defines the rate at which data is processed by the OSP block. If the waveform data is configured for real data points by setting the Data Processing Mode property or the NIFGEN_ATTR_OSP_DATA_PROCESSING_MODE attribute, then it is the rate

### NI 5450 IQ Rate

NIFGEN_ATTR_OSP_IQ_RATE

NIFGEN_ATTR_OSP_DATA_PROCESSING_MODE

NIFGEN_ATTR_OSP_DATA_PROCESSING_MODE

Note

NIFGEN_ATTR_OSP_ENABLED

NIFGEN_ATTR_ARB_SAMPLE_RATE

Parent topic:

NI 5450 Basic Onboard Signal Processing Properties

<!--NI_TOPIC bundle=ni-fgen path=ni-5450-memory-fragmentation.html language=enus -->
## TOPIC 00668: NI 5450 Memory Fragmentation

- bundle_id: `ni-fgen`
- source_path: `ni-5450-memory-fragmentation.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5450-memory-fragmentation.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: When storing multiple waveforms in NI 5450 memory, fragmentation can become a problem. Both waveforms and instructions are stored in NI 5450 memory in contiguous blocks. These blocks are allocated in multiples of 128 bytes, and they are written in the order that you configure them. Fragmentation occ

### NI 5450 Memory Fragmentation

When storing multiple waveforms in
NI 5450 memory, fragmentation can become a
problem. Both waveforms and instructions are stored in
NI 5450 memory in contiguous blocks. These
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

NI 5450 Onboard Memory

<!--NI_TOPIC bundle=ni-fgen path=ni-5450-multichannel-configuration.html language=enus -->
## TOPIC 00669: NI 5450 Multichannel Configuration

- bundle_id: `ni-fgen`
- source_path: `ni-5450-multichannel-configuration.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5450-multichannel-configuration.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5450 has two channels. By default, both are active. You can configure one or both channels as active by calling the niFgen Configure Channels VI or the niFgen_ConfigureChannels function immediately after calling the niFgen Initialize VI or the niFgen_init function. The niFgen Configure Channe

### NI 5450 Multichannel Configuration

The NI 5450 has two channels. By default, both are active. You can configure one or both channels as active by calling the niFgen Configure Channels VI or the niFgen_ConfigureChannels function immediately after calling the niFgen Initialize VI or the niFgen_init function. The niFgen Configure Channels VI or the niFgen_ConfigureChannels function cannot be called after the session has been committed. If a channel is inactive, it will maintain its output voltage and state until it is made active again or until the device is reset.

The NI 5450 has two memory banks, one for each channel. When the niFgen Configure Channels VI or the niFgen_ConfigureChannels function is called to configure only one channel as active, both channel memory banks will be configured. This allows you to use the entire onboard memory for one channel of generation.

#### Configuring Channels for OSP

The NI 5450 supports one channel of real or complex baseband OSP generation. When the OSP is enabled, only one channel may be configured as active. Individual OSP properties can be configured using the I and Q channel strings ("I" and "Q", respectively).

Parent topic:

NI 5450 Theory of Operation

<!--NI_TOPIC bundle=ni-fgen path=ni-5450-multichannel-waveform-allocation.html language=enus -->
## TOPIC 00670: NI 5450 Multichannel Waveform Allocation

- bundle_id: `ni-fgen`
- source_path: `ni-5450-multichannel-waveform-allocation.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5450-multichannel-waveform-allocation.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: A waveform consists of all of the data to be generated on all active channels of a device. A waveform is allocated on a per–device basis, and when waveform allocation occurs, space is allocated on the device onboard memory for each channel. Waveform data must therefore be the same size for each chan

### NI 5450 Multichannel Waveform Allocation

A waveform consists of all of the data to be generated on all active channels of a device. A waveform is allocated on a per–device basis, and when waveform allocation occurs, space is allocated on the device onboard memory for each channel. Waveform data must therefore be the same size for each channel.

Because waveforms contain data for all channels, you can only generate one script, sequence, or arbitrary waveform at a time for all active channels of the device; you cannot generate separate scripts, sequences, or arbitrary waveforms on different channels at the same time.

#### Writing Data

On the NI 5450, data can be written to channel 0 and 1 independently, to I and Q independently, or to both channels simultaneously.

Tip

I/Q generation

To write waveform data to an individual channel, begin by allocating space for waveform data by calling the niFgen Allocate Waveform or niFgen Allocate Named Waveform VI or the niFgen_AllocateWaveform or niFgen_AllocateNamedWaveform function. Once you have allocated the waveform data, call the appropriate niFgen Write Waveform (poly) VI or one of the niFgen Write Waveform functions with the Channel Name parameter set to "0" or "1" and the Waveform Name or waveformHandle parameter set to the name of the waveform previously allocated. You can repeat these steps to write waveform data to another channel.

To write waveform data to both channels at once, you must first *interleave* the data. Once the data is interleaved, call the niFgen Write Waveform (poly) VI or one of the niFgen Write Waveform functions with the Channel parameter set to "0,1".

Parent topic:

NI 5450 Multichannel Configuration

Related concepts:

- NI 5450 Writing I/Q Data
- NI 5450 Interleaved Waveform Data

<!--NI_TOPIC bundle=ni-fgen path=ni-5450-ni-5450-overview.html language=enus -->
## TOPIC 00671: NI 5450 NI 5450 Overview

- bundle_id: `ni-fgen`
- source_path: `ni-5450-ni-5450-overview.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5450-ni-5450-overview.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5450 is a 400 MS/s, 16-bit differential I/Q generator for the PXI Express platform with the following features: Onboard signal processing (OSP) with 120 MHz of baseband I/Q bandwidth, flatness correction, and interpolation 16-bit resolution output, two channels, differential output Differenti

### NI 5450 NI 5450 Overview

The NI 5450 is a 400 MS/s, 16-bit differential I/Q generator for the PXI Express platform with the following
features:

- Onboard signal processing (OSP)
with 120 MHz of baseband I/Q bandwidth, flatness correction, and interpolation
- 16-bit resolution output, two channels, differential output
- Differential output amplitude with a maximum of 1.0 V pk-pk into a 100 Ω differential load
- 50 Ω output impedance (100 Ω differential output impedance), and output attenuation levels from 0 to
3 dB
- High-Resolution internal clocking
- External clocking options
- PLL synchronization to external clocks or to
PXI clock
- TClk synchronization
- Sample rate up to 400 MS/s
- Up to 2 GB of onboard waveform memory
- Waveform linking and looping for arbitrary waveform
generation
- Digital gain
- 2 bidirectional PFI lines for importing triggers and exporting events
- PXI trigger lines

All NI 5450 devices follow industry-standard
Plug and Play specifications for the PXI Express bus and offer
seamless integration with compliant systems.

Parent topic:

Devices

Related concepts:

- NI 5450 Onboard Signal Processing (OSP)

<!--NI_TOPIC bundle=ni-fgen path=ni-5450-onboard-memory.html language=enus -->
## TOPIC 00672: NI 5450 Onboard Memory

- bundle_id: `ni-fgen`
- source_path: `ni-5450-onboard-memory.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5450-onboard-memory.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5450 signal generator uses an onboard memory that is 16-bits wide. The minimum standard memory size for the NI 5450 is 128 MB. With the minimum standard memory size, you can store very long waveforms on the device and obtain reliable waveform generation at full sample rate of 400 MS/s. The NI

### NI 5450 Onboard Memory

The NI 5450 signal generator
uses an onboard memory that is 16-bits wide. The minimum standard
memory size for the NI 5450 is 128 MB. With the minimum
standard memory size, you can store very long waveforms on the
device and obtain reliable waveform generation at full sample rate
of 400 MS/s. The
NI 5450 is also available with higher memory options of 512 MB or 2 GB.

The onboard memory is a single large memory area per channel that stores both waveforms and sequence instructions to generate
the waveforms. The instructions for a complicated sequence can
occupy a significant portion of memory. The architecture of the
NI 5450 allows you to load multiple
waveforms and multiple sequence instructions into the memory. The
following diagram illustrates NI 5450
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

NI 5450 Theory of Operation

<!--NI_TOPIC bundle=ni-fgen path=ni-5450-onboard-signal-processing-components.html language=enus -->
## TOPIC 00673: NI 5450 Onboard Signal Processing Components

- bundle_id: `ni-fgen`
- source_path: `ni-5450-onboard-signal-processing-components.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5450-onboard-signal-processing-components.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the block diagram of the OSP block. The OSP block includes the following components: Prefilter Gain and Prefilter Offset FIR filters Filtering and Interpolation Writing I/Q Data

### NI 5450 Onboard Signal Processing Components

The following figure shows the block diagram of the
OSP block.

[IMAGE alt='image' src='GUID-B7D4B7BA-723C-4923-B5CE-6BE234092194-a5.gif']

The OSP block includes the following
components:

- Prefilter Gain and
Prefilter Offset

- FIR filters
- Filtering and Interpolation
- Writing I/Q Data

Parent topic:

NI 5450 Onboard Signal Processing (OSP)

Related concepts:

- NI 5450 Prefilter Gain and Offset
- NI 5450 FIR Filter Types
- NI 5450 Filtering and Interpolation
- NI 5450 Writing I/Q Data

<!--NI_TOPIC bundle=ni-fgen path=ni-5450-onboard-signal-processing-osp.html language=enus -->
## TOPIC 00674: NI 5450 Onboard Signal Processing (OSP)

- bundle_id: `ni-fgen`
- source_path: `ni-5450-onboard-signal-processing-osp.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5450-onboard-signal-processing-osp.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The onboard signal processing (OSP) block is a general-purpose block of digital signal processing components that can be used to modify the data pulled from waveform memory during generation. The OSP block can be used for the following common applications: Arbitrary Waveform Generation Baseband Inte

### NI 5450 Onboard Signal Processing (OSP)

The onboard signal processing (OSP) block is a
general-purpose block of digital signal processing components that
can be used to modify the data pulled from waveform memory during
generation.

The OSP block can be used for the following common applications:

- Arbitrary Waveform
Generation
- Baseband Interpolation
- Baseband I/Q
Interpolation

Parent topic:

NI 5450 Theory of Operation

Related concepts:

- NI 5450 Arbitrary Waveform Generation
- NI 5450 Baseband Interpolation
- NI 5450 Baseband I/Q Interpolation

<!--NI_TOPIC bundle=ni-fgen path=ni-5450-osp-enabled.html language=enus -->
## TOPIC 00675: NI 5450 OSP Enabled

- bundle_id: `ni-fgen`
- source_path: `ni-5450-osp-enabled.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5450-osp-enabled.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The OSP Enabled property or the NIFGEN_ATTR_OSP_ENABLED attribute activates the functionality of the OSP block. To use any of the features in the OSP block, you must enable onboard signal processing by setting this property or attribute.

### NI 5450 OSP Enabled

The 
OSP
Enabled property or the 
NIFGEN_ATTR_OSP_ENABLED attribute activates the functionality of the OSP block. To use
any of the features in the OSP block, you must enable onboard
signal processing by setting this property or attribute.

Parent topic:

NI 5450 Basic Onboard Signal Processing Properties

<!--NI_TOPIC bundle=ni-fgen path=ni-5450-osp-mode.html language=enus -->
## TOPIC 00676: NI 5450 OSP Mode

- bundle_id: `ni-fgen`
- source_path: `ni-5450-osp-mode.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5450-osp-mode.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The OSP Mode property or the NIFGEN_ATTR_OSP_MODE attribute specifies the generation mode implemented by the OSP block. The OSP block can operate in IF or Baseband mode. On the NI 5450, the default OSP mode is Baseband generation. In baseband mode, I/Q data is filtered, interpolated, and scaled in t

### NI 5450 OSP Mode

The 
OSP
Mode property or the 
NIFGEN_ATTR_OSP_MODE attribute specifies the generation mode implemented by the OSP block. The OSP block can operate in IF or Baseband mode. 
 On the NI 5450, the default OSP mode is Baseband generation.

In baseband mode, I/Q data is filtered, interpolated, and scaled in the device OSP. The device generates I data on the CH 0+ and CH 0− differential output terminals and Q data on the CH 1+ and CH 1− differential output terminals.

Parent topic:

NI 5450 Basic Onboard Signal Processing Properties

<!--NI_TOPIC bundle=ni-fgen path=ni-5450-output-enable.html language=enus -->
## TOPIC 00677: NI 5450 Output Enable

- bundle_id: `ni-fgen`
- source_path: `ni-5450-output-enable.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5450-output-enable.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can disable the analog output signal at the differential channel connectors by controlling the output enable relay, as shown in the following figure. When the output enable relay is disabled, the output signal is connected to ground through a 50 Ω resistance. The output enable relay is enabled f

### NI 5450 Output Enable

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

NI 5450 Analog Output

Related concepts:

- NI 5450 Analog Output

<!--NI_TOPIC bundle=ni-fgen path=ni-5450-output-modes.html language=enus -->
## TOPIC 00678: NI 5450 Output Modes

- bundle_id: `ni-fgen`
- source_path: `ni-5450-output-modes.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5450-output-modes.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The output mode of your signal generator determines the type of waveforms your signal generator produces. To select an output mode, set the Output Mode parameter of the niFgen Configure Output Mode VI or the niFgen_ConfigureOutputMode function.

### NI 5450 Output Modes

The output mode of your signal generator determines the type of
waveforms your signal generator produces. To select an output mode,
set the 
Output Mode parameter of the 
niFgen
Configure Output Mode VI or the 
niFgen_ConfigureOutputMode function.

Parent topic:

NI 5450 Waveform Generation

<!--NI_TOPIC bundle=ni-fgen path=ni-5450-pfi-connectors.html language=enus -->
## TOPIC 00679: NI 5450 PFI Connectors

- bundle_id: `ni-fgen`
- source_path: `ni-5450-pfi-connectors.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5450-pfi-connectors.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: PFI 0 and PFI 1 are bidirectional connectors. As an input, the PFI terminals can accept a trigger from an external source that can start or step through waveform generation. As an output, the PFI lines route a signal out from the following sources: Marker events Start trigger PLL Reference clock sou

### NI 5450 PFI Connectors

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

NI 5450 Front Panel

<!--NI_TOPIC bundle=ni-fgen path=ni-5450-power-up-and-reset-conditions.html language=enus -->
## TOPIC 00680: NI 5450 Power-Up and Reset Conditions

- bundle_id: `ni-fgen`
- source_path: `ni-5450-power-up-and-reset-conditions.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5450-power-up-and-reset-conditions.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The signal generator is in the following state from the time at which the computer begins to power up until the operating system is fully booted and NI-FGEN is loaded. The CH 0+/− and CH 1+/− differential output connectors are disabled and each has 50 Ω impedance to ground. This impedance is the sam

### NI 5450 Power-Up and Reset Conditions

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

NI 5450 NI 5450 Overview

<!--NI_TOPIC bundle=ni-fgen path=ni-5450-prefilter-gain-and-offset.html language=enus -->
## TOPIC 00681: NI 5450 Prefilter Gain and Offset

- bundle_id: `ni-fgen`
- source_path: `ni-5450-prefilter-gain-and-offset.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5450-prefilter-gain-and-offset.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use the following prefiltering components to add impairments to your data and/or to eliminate overflows that occur later in the OSP block. Related Topics Prefilter Gain Prefilter Offset

### NI 5450 Prefilter Gain and Offset

You can use the following prefiltering components
to add impairments to your data and/or to eliminate overflows that
occur later in the 
*OSP* block.

#### Related Topics

- Prefilter Gain
- Prefilter
Offset

Parent topic:

NI 5450 Onboard Signal Processing Components

Related concepts:

- NI 5450 Onboard Signal Processing (OSP)
- NI 5450 Prefilter Gain
- NI 5450 Prefilter Offset

<!--NI_TOPIC bundle=ni-fgen path=ni-5450-prefilter-gain.html language=enus -->
## TOPIC 00682: NI 5450 Prefilter Gain

- bundle_id: `ni-fgen`
- source_path: `ni-5450-prefilter-gain.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5450-prefilter-gain.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Prefilter gain can change the gain of the I and Q stream during signal generation. You can change the I and Q prefilter gains independently by setting the Pre-Filter Gain I and Pre-Filter Gain Q properties or the NIFGEN_ATTR_OSP_PRE_FILTER_GAIN_I and NIFGEN_ATTR_OSP_PRE_FILTER_GAIN_Q attributes. The

### NI 5450 Prefilter Gain

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

NI 5450 Prefilter Gain and Offset

<!--NI_TOPIC bundle=ni-fgen path=ni-5450-prefilter-offset.html language=enus -->
## TOPIC 00683: NI 5450 Prefilter Offset

- bundle_id: `ni-fgen`
- source_path: `ni-5450-prefilter-offset.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5450-prefilter-offset.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Prefilter offset can add offset to the I and Q stream during signal generation. Change the I and Q prefilter offsets independently by setting the Pre-Filter Offset I and Pre-Filter Offset Q properties or the NIFGEN_ATTR_OSP_PRE_FILTER_OFFSET_I and NIFGEN_ATTR_OSP_PRE_FILTER_OFFSET_Q attributes. The

### NI 5450 Prefilter Offset

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

NI 5450 Prefilter Gain and Offset

Related concepts:

- NI 5450 Prefilter Gain

<!--NI_TOPIC bundle=ni-fgen path=ni-5450-pxi-express-bandwidth-considerations.html language=enus -->
## TOPIC 00684: NI 5450 PXI Express Bandwidth Considerations

- bundle_id: `ni-fgen`
- source_path: `ni-5450-pxi-express-bandwidth-considerations.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5450-pxi-express-bandwidth-considerations.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: National Instruments PXI Express signal generators use PCI Express as the interface to the computer. The physical connection between a PXI Express signal generator and a computer is called a PCI Express link. When a signal generator generates a waveform, it can saturate this link. Saturation occurs

### NI 5450 PXI Express Bandwidth Considerations

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

NI 5450 Streaming

<!--NI_TOPIC bundle=ni-fgen path=ni-5450-reference-clock.html language=enus -->
## TOPIC 00685: NI 5450 Reference Clock

- bundle_id: `ni-fgen`
- source_path: `ni-5450-reference-clock.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5450-reference-clock.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the NI 5450 Reference Clock Source path. The NI 5450 can phase-lock its Sample clock to an external signal that is present on the CLK IN front panel connector. PXI devices can also phase–lock to a 10 MHz Reference clock signal provided by the PXI bus (PXI_CLK10). Refer to

### NI 5450 Reference Clock

The following figure shows the NI 5450 Reference Clock Source path.

[IMAGE alt='image' src='GUID-B8EBE8BF-FC7F-45E7-8DCB-EEE72D0F4218-a5.gif']

The NI 5450 can
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

NI 5450 Clocking Options

Related concepts:

- NI 5450 Clocking Options
- Configuring a Reference Clock

<!--NI_TOPIC bundle=ni-fgen path=ni-5450-sample-size-and-resolution.html language=enus -->
## TOPIC 00686: NI 5450 Sample Size and Resolution

- bundle_id: `ni-fgen`
- source_path: `ni-5450-sample-size-and-resolution.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5450-sample-size-and-resolution.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5450 stores arbitrary waveforms in memory as signed 16-bit digital words. On the NI 5450, the entire 16 bits are sent to the digital gain circuit, the OSP and the DAC. Related Topics Onboard Memory Waveform Sizes

### NI 5450 Sample Size and Resolution

The NI 5450 stores arbitrary
waveforms in memory as signed 16-bit digital words. On the
NI 5450, the entire 16 bits are sent to the digital
gain circuit, the OSP and the DAC.

Related Topics

*Onboard Memory*

*Waveform Sizes*

Parent topic:

NI 5450 Waveform Generation

Related concepts:

- NI 5450 Onboard Memory
- NI 5450 Waveform Size and Quantum

<!--NI_TOPIC bundle=ni-fgen path=ni-5450-script-mode.html language=enus -->
## TOPIC 00687: NI 5450 Script Mode

- bundle_id: `ni-fgen`
- source_path: `ni-5450-script-mode.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5450-script-mode.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Script Mode allows you to use scripting to link and loop multiple waveforms in complex combinations using a script. A script is a series of instructions that indicates how waveforms saved in the onboard memory should be sent to the DUT. Scripts have many different uses, including specifying the orde

### NI 5450 Script Mode

*Script Mode* allows you to use scripting to link and
loop multiple waveforms in complex combinations using a 
script. A script is a series of instructions that
indicates how waveforms saved in the onboard memory should be sent
to the DUT. Scripts have many different uses, including specifying the order in which the waveforms
are generated, the number of times they are generated, and the
triggers and markers associated with the generation.

Parent topic:

NI 5450 Output Modes

Related concepts:

- Script Mode

<!--NI_TOPIC bundle=ni-fgen path=ni-5450-signal-routing.html language=enus -->
## TOPIC 00688: NI 5450 Signal Routing

- bundle_id: `ni-fgen`
- source_path: `ni-5450-signal-routing.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5450-signal-routing.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: An NI signal generator is capable of sending and receiving signals through the front panel and the PXI or RTSI trigger bus. The front panel connectors provides connectivity for the output channel as well as for control lines for sending and receiving clocks, triggers, and events. You can use the PXI

### NI 5450 Signal Routing

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

NI 5450 Theory of Operation

Related concepts:

- NI 5450 Syntax for Terminal Names

<!--NI_TOPIC bundle=ni-fgen path=ni-5450-single-trigger-mode.html language=enus -->
## TOPIC 00689: NI 5450 Single Trigger Mode

- bundle_id: `ni-fgen`
- source_path: `ni-5450-single-trigger-mode.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5450-single-trigger-mode.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: When your application is configured for Single trigger mode, only one Start trigger is required to begin waveform generation. All Start triggers after the first Start trigger are ignored. Once the waveform generation is complete, the analog output indefinitely settles at the DC value of the last sam

### NI 5450 Single Trigger Mode

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

NI 5450 Trigger Modes

<!--NI_TOPIC bundle=ni-fgen path=ni-5450-specifications.html language=enus -->
## TOPIC 00690: NI 5450 Specifications

- bundle_id: `ni-fgen`
- source_path: `ni-5450-specifications.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5450-specifications.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: For information about the signal generator specifications, refer to the device specifications. You can access these specifications by navigating to Start»All Programs»National Instruments» NI-FGEN»Documentation»NI Signal Generators Specifications, or you can visit ni.com/manuals.

### NI 5450 Specifications

For information about the signal generator
specifications, refer to the 
*device
specifications*. You can access these specifications by
navigating to 
Start»All Programs»National Instruments»
NI-FGEN»Documentation»NI Signal Generators Specifications, or you can visit 
ni.com/manuals.

Parent topic:

NI 5450 NI 5450 Overview

<!--NI_TOPIC bundle=ni-fgen path=ni-5450-standard-function-mode.html language=enus -->
## TOPIC 00691: NI 5450 Standard Function Mode

- bundle_id: `ni-fgen`
- source_path: `ni-5450-standard-function-mode.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5450-standard-function-mode.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Standard Function output mode is used to generate standard function waveforms such as sine, square, triangle, and so on. On the NI 5450, Standard Function mode is implemented through direct digital synthesis (DDS). DDS is a technique for deriving, under digital control, an analog frequency source fr

### NI 5450 Standard Function Mode

Standard Function output mode is used to generate standard
function waveforms such as sine, square, triangle, and so on. 
On the NI 5450, *Standard Function mode* is implemented
through *direct digital synthesis* (DDS). DDS is a technique for
deriving, under digital control, an analog frequency source from a
single Reference clock frequency. This technique produces
high-frequency accuracy and resolution, temperature stability,
wideband tuning, and rapid, phase-continuous frequency
switching.

In DDS mode, a fixed–size memory (called *lookup memory*) stores one cycle of a periodic waveform. A phase accumulator indexes the lookup memory. For each cycle of the device Sample clock, the sample of the waveform in lookup memory that is addressed by the phase accumulator is returned. The accumulator is then incremented by the value in the frequency control word (FCW). By adjusting the Frequency property or the NIFGEN_ATTR_FUNC_FREQUENCY attribute, NI-FGEN calculates the corresponding FCW, and you can vary the output frequency of the waveform in lookup memory. The phase accumulator increments in smaller steps for smaller FCWs. Accordingly, you need more samples to generate one waveform cycle, so the frequency is lower. A higher FCW results in a higher frequency. In DDS mode, the Sample clock does not vary with the frequency of the generated waveform. At higher frequencies, some waveform samples in lookup memory are skipped; at lower frequencies, some samples output multiple times in succession.

This feature is only supported on module revision C and later. Refer to the *Identifying Module Revision* topic for more information.

Parent topic:

NI 5450 Output Modes

Related concepts:

- Standard Function Mode
- Direct Digital Synthesis
- NI 5450 Identifying Module Revision

<!--NI_TOPIC bundle=ni-fgen path=ni-5450-stepped-trigger-mode.html language=enus -->
## TOPIC 00692: NI 5450 Stepped Trigger Mode

- bundle_id: `ni-fgen`
- source_path: `ni-5450-stepped-trigger-mode.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5450-stepped-trigger-mode.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The waveform you downloaded generates each time a Start trigger occurs. After a waveform finishes generating, the last sample of the waveform repeats continuously until the next Start trigger is received. When the next Start trigger is received, the waveform generates again. If a Start trigger is re

### NI 5450 Stepped Trigger Mode

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

NI 5450 Trigger Modes

<!--NI_TOPIC bundle=ni-fgen path=ni-5450-streaming.html language=enus -->
## TOPIC 00693: NI 5450 Streaming

- bundle_id: `ni-fgen`
- source_path: `ni-5450-streaming.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5450-streaming.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Streaming is a way to generate waveforms that are too large to fit in the onboard memory of the signal generator. Streaming can be used in Arbitrary Waveform, Arbitrary Sequence, or Script output modes. To stream waveform data, allocate and identify all or a portion of the signal generator onboard m

### NI 5450 Streaming

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

NI 5450 Waveform Generation

Related concepts:

- Arbitrary Waveform Output Mode
- Arbitrary Sequence Mode
- Script Mode
- Direct DMA

<!--NI_TOPIC bundle=ni-fgen path=ni-5450-synchronization.html language=enus -->
## TOPIC 00694: NI 5450 Synchronization

- bundle_id: `ni-fgen`
- source_path: `ni-5450-synchronization.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5450-synchronization.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Your signal generator is based on the National Instruments Synchronization and Memory Core (SMC) technology and therefore supports TClk synchronization. Refer to the NI-TClk Synchronization Help for more information about NI-TClk Synchronization.

### NI 5450 Synchronization

Your signal generator is based on the 
National Instruments
Synchronization and Memory Core (SMC) technology and therefore
supports TClk synchronization. Refer to the 
NI-TClk
Synchronization Help for more information about NI-TClk
Synchronization.

Parent topic:

NI 5450 NI 5450 Overview

<!--NI_TOPIC bundle=ni-fgen path=ni-5450-syntax-for-terminal-names.html language=enus -->
## TOPIC 00695: NI 5450 Syntax for Terminal Names

- bundle_id: `ni-fgen`
- source_path: `ni-5450-syntax-for-terminal-names.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5450-syntax-for-terminal-names.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The syntax for terminal names is a unique identifier that refers to a physical terminal in your system. To guarantee the uniqueness of a terminal name across multiple devices, terminal names begin with a forward slash, followed by the name of the device as configured in MAX, such as Dev1. A forward

### NI 5450 Syntax for Terminal Names

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

NI 5450 Signal Routing

<!--NI_TOPIC bundle=ni-fgen path=ni-5450-theory-of-operation.html language=enus -->
## TOPIC 00696: NI 5450 Theory of Operation

- bundle_id: `ni-fgen`
- source_path: `ni-5450-theory-of-operation.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5450-theory-of-operation.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Expand this topic for information about the theory of operation of your signal generator.

### NI 5450 Theory of Operation

Expand this topic for information about the theory
of operation of your signal generator.

Parent topic:

NI 5450 NI 5450 Overview

<!--NI_TOPIC bundle=ni-fgen path=ni-5450-thermal-shutdown.html language=enus -->
## TOPIC 00697: NI 5450 Thermal Shutdown

- bundle_id: `ni-fgen`
- source_path: `ni-5450-thermal-shutdown.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5450-thermal-shutdown.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: NI-FGEN supports thermal shutdown capability for the NI 5450. This capability allows the signal generator to detect when it has reached a dangerously high temperature and to then power down to prevent damage to the device. Air circulation paths, fan settings, and space allowances are several factors

### NI 5450 Thermal Shutdown

NI-FGEN supports thermal shutdown capability for
the NI 5450. This
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

NI 5450 NI 5450 Overview

<!--NI_TOPIC bundle=ni-fgen path=ni-5450-trigger-modes.html language=enus -->
## TOPIC 00698: NI 5450 Trigger Modes

- bundle_id: `ni-fgen`
- source_path: `ni-5450-trigger-modes.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5450-trigger-modes.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5450 has four trigger modes: Single, Continuous, Stepped, and Burst. These trigger modes are available for Arbitrary Waveform, and Arbitrary Sequence output modes. Refer to the niFgen Configure Trigger Mode VI or the niFgen_ConfigureTriggerMode function for information about setting the trigg

### NI 5450 Trigger Modes

The NI 5450 has four trigger modes: Single, Continuous, Stepped,
and Burst. These trigger modes are available for Arbitrary
Waveform, and Arbitrary Sequence output modes.
Refer to the 
niFgen
Configure Trigger Mode VI or the 
niFgen_ConfigureTriggerMode function for information about setting the trigger mode.

Parent topic:

NI 5450 Triggering

<!--NI_TOPIC bundle=ni-fgen path=ni-5450-trigger-sources.html language=enus -->
## TOPIC 00699: NI 5450 Trigger Sources

- bundle_id: `ni-fgen`
- source_path: `ni-5450-trigger-sources.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5450-trigger-sources.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Trigger sources are software selectable. You can use any of the following external input triggers: PFI 0 or PFI 1 on the front panel connectors PXI_TRIG<0..7> lines on the PXI trigger bus backplane The following figure shows the possible trigger sources for the NI 5450. ^ § Refer to Exporting Signal

### NI 5450 Trigger Sources

Trigger sources are software selectable. You can
use any of the following external input triggers:

- PFI 0 or PFI 1 on the front panel connectors

- PXI_TRIG<0..7> lines on the PXI trigger bus backplane

The following figure shows the possible trigger
sources for the NI 5450.

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

NI 5450 Triggering

Related concepts:

- NI 5450 Exporting Signals
- PXI Trigger Lines

<!--NI_TOPIC bundle=ni-fgen path=ni-5450-trigger-timing.html language=enus -->
## TOPIC 00700: NI 5450 Trigger Timing

- bundle_id: `ni-fgen`
- source_path: `ni-5450-trigger-timing.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5450-trigger-timing.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the relationship between Start trigger and the waveform output. t[s1] is the required pulse width on the Start trigger signal. t[s2] is the delay from the Start trigger to the waveform output. Refer to the NI 5450 specifications for more information about these timing para

### NI 5450 Trigger Timing

The following figure shows the relationship between
Start trigger and the waveform output. t<sub>s1</sub> is the required pulse width on the Start trigger
signal. t<sub>s2</sub> is the delay from the Start trigger to the waveform
output. Refer to the 
*NI 5450
specifications* for more information about these timing
parameters.

[IMAGE alt='image' src='GUID-9DD6A51C-2BCA-4129-9C8D-0A821181925F-a5.gif']

The NI 5450 also allows you to export
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

NI 5450 Triggering

<!--NI_TOPIC bundle=ni-fgen path=ni-5450-triggering.html language=enus -->
## TOPIC 00701: NI 5450 Triggering

- bundle_id: `ni-fgen`
- source_path: `ni-5450-triggering.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5450-triggering.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can define the signal generator functionality by using the various triggering techniques. Expand this section to learn more about using triggers with your signal generator.

### NI 5450 Triggering

You can define the signal generator functionality
by using the various triggering techniques. Expand this section to
learn more about using triggers with your signal generator.

Parent topic:

NI 5450 NI 5450 Overview

<!--NI_TOPIC bundle=ni-fgen path=ni-5450-using-an-external-clock-with-the-osp.html language=enus -->
## TOPIC 00702: NI 5450 Using an External Clock with the OSP Block

- bundle_id: `ni-fgen`
- source_path: `ni-5450-using-an-external-clock-with-the-osp.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5450-using-an-external-clock-with-the-osp.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Some applications may require lower jitter or phase noise than is provided by the onboard High-Resolution clock. You can use an external clock source to achieve spectral purity at any arbitrary I/Q rate. To determine the frequency of the sample rate for the external clock source, complete the follow

### NI 5450 Using an External Clock with the OSP Block

Some applications may require lower jitter or phase
noise than is provided by the onboard High-Resolution clock. You can use an
external clock source to achieve spectral purity at any arbitrary
I/Q rate. To determine the frequency of the sample rate for the
external clock source, complete the following steps.

1. Set the 
Sample
Clock Source property or the 
 NIFGEN_ATTR_SAMPLE_CLOCK_SOURCE attribute to the external 
 clock source 
you are using.
2. Set the 
IQ Rate
property or the 
 NIFGEN_ATTR_OSP_IQ_RATE attribute.

1. Read the value of the 
Sample
Rate property or the 
 NIFGEN_ATTR_ARB_SAMPLE_RATE attribute.
2. Set the external clock source sample rate to the frequency of
the Sample Rate property or the 
 NIFGEN_ATTR_ARB_SAMPLE_RATE 
attribute that you just read.
3. Validate that the external Sample clock source is connected to
the NI 5450 connector specified in the 
Sample
Clock Source property or the 
 NIFGEN_ATTR_SAMPLE_CLOCK_SOURCE attribute and is generating a clock before you continue
configuring the 
NI 5450.

For more information about using external clocks, refer to 
*External Sample
Clock Sources*.

Parent topic:

NI 5450 IQ Rate

Related concepts:

- NI 5450 External Sample Clock

<!--NI_TOPIC bundle=ni-fgen path=ni-5450-waveform-amplitude-control.html language=enus -->
## TOPIC 00703: NI 5450 Waveform Amplitude Control

- bundle_id: `ni-fgen`
- source_path: `ni-5450-waveform-amplitude-control.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5450-waveform-amplitude-control.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5450 can be configured to achieve required amplitude settings. Output Paths and Amplifiers The following figure shows the Direct path. The Direct path provides the output of the main DAC to the CH 0+/− connectors with the fewest electronic components in the path. There are no programmable amp

### NI 5450 Waveform Amplitude Control

The NI 5450 can be configured to achieve required amplitude settings.

#### Output Paths and Amplifiers

The following figure shows the Direct path.

[IMAGE alt='image' src='GUID-99847B23-D9A8-4ADE-853D-434DB360B9E4-a5.gif']

The Direct path provides the output of the main DAC
to the CH 0+/− connectors with the fewest electronic components in the path.
There are no programmable amplifiers and there is no method for adding DC
offset to the waveform. The Direct path can generate a maximum of 
1.0 V<sub>pk-pk</sub> at the CH 0+/− output into 50 Ω. The maximum gain setting for an Analog Output path
configured to the Direct path is 0.5 (gain is a unitless
value).

Parent topic:

NI 5450 Analog Output

<!--NI_TOPIC bundle=ni-fgen path=ni-5450-waveform-and-generation-instruction-m.html language=enus -->
## TOPIC 00704: NI 5450 Waveform and Generation Instruction Memory Size

- bundle_id: `ni-fgen`
- source_path: `ni-5450-waveform-and-generation-instruction-m.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5450-waveform-and-generation-instruction-m.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Waveform Memory Size Waveforms are stored in the NI 5450 onboard memory in contiguous blocks. These blocks are allocated in multiples of 128 bytes. This allocation style means that while waveform sizes may be multiples of two samples (four bytes) on the NI 5450, the amount of onboard memory allocate

### NI 5450 Waveform and Generation Instruction Memory Size

#### Waveform Memory Size

Waveforms are stored in the
NI 5450 onboard memory in contiguous
blocks. These blocks are allocated in multiples of 128 bytes. This
allocation style means that while waveform sizes may be multiples
of 
two samples (four bytes) on the NI 5450, the amount of
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

NI 5450 Onboard Memory

<!--NI_TOPIC bundle=ni-fgen path=ni-5450-waveform-generation.html language=enus -->
## TOPIC 00705: NI 5450 Waveform Generation

- bundle_id: `ni-fgen`
- source_path: `ni-5450-waveform-generation.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5450-waveform-generation.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5450 supports the following output, or generation, modes: Arbitrary Waveform Arbitrary Sequence Script To select an output mode, set the Output Mode parameter of the niFgen Configure Output Mode VI or the niFgen_ConfigureOutputMode function.

### NI 5450 Waveform Generation

The NI 5450 supports the
following output, or generation, modes:

- Arbitrary Waveform
- Arbitrary Sequence
- Script

To select an output mode, set the 
Output Mode parameter of the 
niFgen
Configure Output Mode VI or the 
niFgen_ConfigureOutputMode function.

Parent topic:

NI 5450 NI 5450 Overview

Related concepts:

- NI 5450 Arbitrary Waveform Mode
- NI 5450 Arbitrary Sequence Mode
- NI 5450 Script Mode

<!--NI_TOPIC bundle=ni-fgen path=ni-5450-waveform-quantum.html language=enus -->
## TOPIC 00706: NI 5450 Waveform Quantum

- bundle_id: `ni-fgen`
- source_path: `ni-5450-waveform-quantum.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5450-waveform-quantum.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Quantum is the increment in samples that waveform sizes must adhere to. The NI 5450 has a sample quantum of two, allowing waveforms of any even numbered size (between the maximum and minimum waveform sizes) to be downloaded. For example, if while in Arbitrary Waveform mode, you request to load a wav

### NI 5450 Waveform Quantum

Quantum is the increment in samples that waveform
sizes must adhere to. The NI 5450 has a sample quantum of two, allowing waveforms of any even numbered size (between the maximum and minimum waveform
sizes) to be downloaded.

For example, if while in Arbitrary Waveform mode, you request to load a waveform of seven samples, the task will not complete successfully because the waveform is not an integer multiple of the quantum size. Waveform sizes that meet the conditions include 2, 4, 8, 10, 12, and so on, up to maximum allowable waveform size.

Parent topic:

NI 5450 Waveform Size and Quantum

<!--NI_TOPIC bundle=ni-fgen path=ni-5450-waveform-size-and-quantum.html language=enus -->
## TOPIC 00707: NI 5450 Waveform Size and Quantum

- bundle_id: `ni-fgen`
- source_path: `ni-5450-waveform-size-and-quantum.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5450-waveform-size-and-quantum.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5450 onboard memory architecture imposes certain requirements on the waveform size and quantum.

### NI 5450 Waveform Size and Quantum

The NI 5450 onboard memory architecture
imposes certain requirements on the waveform *size* and *quantum*.

Parent topic:

NI 5450 Waveform Generation

Related concepts:

- NI 5450 Waveform Size
- NI 5450 Waveform Quantum

<!--NI_TOPIC bundle=ni-fgen path=ni-5450-waveform-size.html language=enus -->
## TOPIC 00708: NI 5450 Waveform Size

- bundle_id: `ni-fgen`
- source_path: `ni-5450-waveform-size.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5450-waveform-size.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Minimum Waveform Size The minimum waveform size on the NI 5450 depends on the output mode and the trigger mode. Refer to the device specifications for the minimum waveform size values for the different modes. To provide greater programming flexibility, NI-FGEN does not strictly enforce the minimum

### NI 5450 Waveform Size

#### Minimum Waveform Size

The
minimum waveform size on the NI 5450 depends on the output mode and the 
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

NI 5450 Waveform Size and Quantum

Related concepts:

- NI 5450 Trigger Modes
- NI 5450 Waveform and Generation Instruction Memory Size

<!--NI_TOPIC bundle=ni-fgen path=ni-5450-writing-i-q-data.html language=enus -->
## TOPIC 00709: NI 5450 Writing I/Q Data

- bundle_id: `ni-fgen`
- source_path: `ni-5450-writing-i-q-data.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5450-writing-i-q-data.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: On multichannel devices, I/Q data can either be written to individual channels (for example, designating one channel for I data and one channel for Q data) or to both channels of the device at once when following the multichannel waveform allocation guidelines.

### NI 5450 Writing I/Q Data

On multichannel devices, I/Q data can either be written to individual channels (for example, designating one channel for I data and one channel for Q data) or to both channels of the device at once when following the *multichannel waveform allocation* guidelines.

Parent topic:

NI 5450 Onboard Signal Processing Components

Related concepts:

- NI 5450 Multichannel Waveform Allocation

<!--NI_TOPIC bundle=ni-fgen path=ni-5451-aborting-generation.html language=enus -->
## TOPIC 00710: NI 5451 Aborting Generation

- bundle_id: `ni-fgen`
- source_path: `ni-5451-aborting-generation.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5451-aborting-generation.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can abort the generation of the current waveform. Aborting the generation exhibits different behaviors for different waveform output modes. Related Topics Aborting to Ground

### NI 5451 Aborting Generation

You can abort the generation of the current
waveform. Aborting the generation exhibits different behaviors for
different 
*waveform output
modes*.

Related Topics

*Aborting to Ground*

Parent topic:

NI 5451 Waveform Generation

Related concepts:

- NI 5451 Waveform Generation
- Abort to Ground

<!--NI_TOPIC bundle=ni-fgen path=ni-5451-access-and-active-leds.html language=enus -->
## TOPIC 00711: NI 5451 ACCESS and ACTIVE LEDs

- bundle_id: `ni-fgen`
- source_path: `ni-5451-access-and-active-leds.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5451-access-and-active-leds.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The ACCESS and ACTIVE LEDs indicate the status of the PXIe module: ACCESS LED The ACCESS LED indicates basic hardware status as shown in the following table. Color Indications Off Device is not yet functional, or the device has detected a problem with a power rail. Amber The device is being accessed

### NI 5451 ACCESS and ACTIVE LEDs

The ACCESS and ACTIVE LEDs indicate the status of
the PXIe module:

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

NI 5451 Front Panel

<!--NI_TOPIC bundle=ni-fgen path=ni-5451-accessories.html language=enus -->
## TOPIC 00712: NI 5451 Accessories

- bundle_id: `ni-fgen`
- source_path: `ni-5451-accessories.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5451-accessories.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: National Instruments offers a variety of products to use with your signal generator, including cables and other accessories. Visit ni.com for more information.

### NI 5451 Accessories

National Instruments offers a variety of products
to use with your signal generator, including cables and other
accessories. Visit 
ni.com for more
information.

Parent topic:

NI 5451 NI 5451 Overview

<!--NI_TOPIC bundle=ni-fgen path=ni-5451-adjusting-skew.html language=enus -->
## TOPIC 00713: NI 5451 Adjusting Skew

- bundle_id: `ni-fgen`
- source_path: `ni-5451-adjusting-skew.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5451-adjusting-skew.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Using the NI 5451, you can fine-tune the skew in your TClk application by dynamically adjusting the oscillator phase DAC value. You can only adjust the value in External Sample Clock mode, but you can use the PXI 10 MHz backplane clock with an External Sample Clock Multiplier as your external clock

### NI 5451 Adjusting Skew

Using the NI 5451, you can fine-tune the skew in your TClk application by dynamically adjusting the oscillator phase DAC value.
You can only adjust the value in *External Sample Clock* mode, but you can use the PXI 10 MHz backplane clock with an External Sample Clock Multiplier as your external clock if you are not supplying your own clock source.

Complete the following steps to manually adjust TClk:

1. Configure the devices for acquisition or generation synchronized with NI-TClk.
2. Read the oscillator phase DAC value after performing TClk synchronization and save the value while the program is still running.
3. Manually adjust the oscillator phase DAC value until optimal alignment is achieved, starting from the value saved in step 2.

Complete the following steps to optimize synchronization repeatability:

1. After the acquisition or generation is completed, but before you close the session, read the Oscillator Phase DAC Value property.
2. Store the value.
3. Before running the program again, set the oscillator phase DAC value to the stored value.

Parent topic:

NI 5451 Synchronization

Related concepts:

- NI 5451 External Sample Clock

<!--NI_TOPIC bundle=ni-fgen path=ni-5451-amplitude-modulation-am-or-double-sid.html language=enus -->
## TOPIC 00714: NI 5451 Amplitude Modulation (AM) or Double Sideband

- bundle_id: `ni-fgen`
- source_path: `ni-5451-amplitude-modulation-am-or-double-sid.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5451-amplitude-modulation-am-or-double-sid.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can generate an AM radio signal with the OSP block. To generate an AM signal, complete the following steps. Enable onboard signal processing by setting the OSP Enabled property or the NIFGEN_ATTR_OSP_ENABLED attribute. Set the OSP Mode property or the NIFGEN_ATTR_OSP_MODE attribute to IF. Specif

### NI 5451 Amplitude Modulation (AM) or Double Sideband

[IMAGE alt='image' src='GUID-332DF7B0-090E-4535-83BC-E7A319506DEA-a5.gif']

You can generate an AM radio signal with the OSP
block. To generate an AM signal, complete the following steps.

1. Enable onboard signal processing by setting the 
OSP
Enabled property or the 
 NIFGEN_ATTR_OSP_ENABLED attribute.
2. Set the OSP Mode property or the NIFGEN_ATTR_OSP_MODE attribute to IF .
3. Specify the use of real numbers for the waveform data by
setting the 
Data
Processing Mode property or the 
 NIFGEN_ATTR_OSP_DATA_PROCESSING_MODE attribute.
4. Set the 
IQ Rate
property or the 
 NIFGEN_ATTR_OSP_IQ_RATE attribute to the sample rate of the baseband data.
5. Set the 
Pre-Filter
Gain I property or the 
 NIFGEN_ATTR_OSP_PRE_FILTER_GAIN_I attribute to 0.5.
6. Set the 
Pre-Filter
Offset I property or the 
 NIFGEN_ATTR_OSP_PRE_FILTER_OFFSET_I attribute to 0.5. Steps 4 and 5 ensure that all interpolated
data is positive when it is mixed with the carrier.
7. Enable the carrier by setting the 
Carrier
Enabled property or the 
 NIFGEN_ATTR_OSP_CARRIER_ENABLED attribute.
8. Set the 
Carrier
Frequency property or the 
 NIFGEN_ATTR_OSP_CARRIER_FREQUENCY attribute to the station frequency.
9. Specify a flat FIR filter by setting the 
FIR Filter
Type property or the 
 NIFGEN_ATTR_OSP_FIR_FILTER_TYPE attribute.
10. Set the 
Flat
Filter Passband property or the 
 NIFGEN_ATTR_OSP_FIR_FILTER_FLAT_PASSBAND attribute to 0.4.
11. Download the waveform data to the signal generator.

Parent topic:

NI 5451 Common Onboard Signal Processing Applications

<!--NI_TOPIC bundle=ni-fgen path=ni-5451-analog-gain-settings.html language=enus -->
## TOPIC 00715: NI 5451 Analog Gain Settings

- bundle_id: `ni-fgen`
- source_path: `ni-5451-analog-gain-settings.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5451-analog-gain-settings.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following table summarizes the maximum and minimum gain setting that you can apply for the NI-FGEN analog path options. Refer to the device specifications for more information about gain resolution. Analog Path Gain Summary (50 Ω, Differential) NI-FGEN Analog Path Maximum Gain Value Minimum Gain

### NI 5451 Analog Gain Settings

The following table summarizes the maximum and
minimum gain setting that you can apply for the NI-FGEN analog path
options. Refer to the 
*device
specifications* for more information about gain resolution.

| Analog Path Gain Summary (50 Ω, Differential) |  |  |
| --- | --- | --- |
| NI-FGEN Analog Path | Maximum Gain Value | Minimum Gain Value |
| Main Path without flatness correction | 2.5 | 1.77e-3 |
| Main Path with flatness correction | 1.75 | 1.24e-3 |
| Direct Path without flatness correction | 0.5 | 0.354 |
| Direct Path with flatness correction | 0.4 | 0.284 |
| Note: Gain is unitless. |  |  |

Note

Parent topic:

NI 5451 Waveform Amplitude Control

<!--NI_TOPIC bundle=ni-fgen path=ni-5451-analog-output.html language=enus -->
## TOPIC 00716: NI 5451 Analog Output

- bundle_id: `ni-fgen`
- source_path: `ni-5451-analog-output.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5451-analog-output.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the NI 5451 Analog Output signal path. NI 5451 analog waveforms are generated as follows: The 16-bit digital waveform data from the Waveform Generation Engine or OSP is passed to a digital gain circuit and then to the high-speed DAC. This DAC also implements a portion of t

### NI 5451 Analog Output

The following figure shows the NI 5451 Analog Output signal path.

[IMAGE alt='image' src='GUID-C075BAAC-CFF8-4A9C-A767-0BEB86BCFCEF-a5.gif']

NI 5451 analog waveforms are
generated as follows:

1. The 16-bit digital waveform data from the Waveform Generation
Engine or OSP is passed to a digital gain circuit and then to the
high-speed DAC. This DAC also implements a portion of the Analog
Output signal path attenuation with a range of 0 dB to
3 dB. Refer to the NI PXIe-5451 Specifications for the exact resolution. You can adjust the amount
of attenuation by configuring the 
Arbitrary
Waveform Gain property or the 
 NIFGEN_ATTR_ARB_GAIN attribute. NI-FGEN calculates and sets the correct amount of
attenuation required, corresponding to the gain setting.
2. Following the DAC, the signal is routed through either the Direct path or the Main path. The Direct path has a fixed lowpass filter and no additional signal conditioning. The Direct path can provide a maximum of 1.0 V pk-pk DC differential output into 50 Ω with a maximum of 3 dB attenuation. The Main path has a selectable lowpass filter and a bank of attenuators that are automatically selected based on the requested gain setting. The Main path can provide a maximum of 5.0 V pk-pk DC differential output into 50 Ω.
3. The signal then passes through the Output Enable relay. When
the Output Enable relay is disabled, ground is connected to the
output through a 50 Ω resistor.
Waveform generation continues while the output
enable relay is disabled. When the relay is enabled, the analog
waveform is seen at the connector. Enable or
disable the output of the analog waveform generator by using the 
niFgen Output
Enable VI or the 
 niFgen_ConfigureOutputEnabled function.
4. The signal then passes to the
differential channel connector. The terminal must be configured for differential output using the Terminal Configuration property or the NIFGEN_ATTR_TERMINAL_CONFIGURATION attribute when using the Direct path. The terminal for the Main path can be configured for differential or single-ended output.

Note

Parent topic:

NI 5451 Theory of Operation

<!--NI_TOPIC bundle=ni-fgen path=ni-5451-arbitrary-sequence-mode.html language=enus -->
## TOPIC 00717: NI 5451 Arbitrary Sequence Mode

- bundle_id: `ni-fgen`
- source_path: `ni-5451-arbitrary-sequence-mode.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5451-arbitrary-sequence-mode.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Arbitrary Sequence mode allows you to load multiple waveforms in the onboard memory of the NI 5451. A finite number of samples make a waveform. To generate these downloaded waveforms in a specific order, you must prepare a sequence, which contains a number of segments in a specific order. Each segme

### NI 5451 Arbitrary Sequence Mode

*Arbitrary Sequence mode* allows you to load multiple
waveforms in the onboard memory of the NI 5451. A finite
number of samples make a waveform. To generate these downloaded
waveforms in a specific order, you must prepare a sequence, which
contains a number of segments in a specific order. Each segment
specifies a downloaded waveform, a number of loops to repeat the
selected waveform, and a numeric offset in which a marker is
generated by the device.

Parent topic:

NI 5451 Output Modes

Related concepts:

- Arbitrary Sequence Mode

<!--NI_TOPIC bundle=ni-fgen path=ni-5451-arbitrary-waveform-mode.html language=enus -->
## TOPIC 00718: NI 5451 Arbitrary Waveform Mode

- bundle_id: `ni-fgen`
- source_path: `ni-5451-arbitrary-waveform-mode.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5451-arbitrary-waveform-mode.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5451 supports Arbitrary Waveform output mode. Arbitrary Waveform mode generates waveforms from user-created/provided waveform arrays of numeric data. The waveform arrays are downloaded to the arbitrary waveform generator onboard memory. Arbitrary Waveform mode also uses memory to store the in

### NI 5451 Arbitrary Waveform Mode

The NI 5451 supports Arbitrary Waveform output mode. Arbitrary Waveform mode generates waveforms from
user-created/provided waveform arrays of numeric data. The waveform
arrays are downloaded to the arbitrary waveform generator onboard
memory. *Arbitrary Waveform mode* also uses memory to
store the instructions for generating waveform sequences in the
onboard memory.

Parent topic:

NI 5451 Output Modes

Related concepts:

- Arbitrary Waveform Output Mode

<!--NI_TOPIC bundle=ni-fgen path=ni-5451-attenuation.html language=enus -->
## TOPIC 00719: NI 5451 Attenuation

- bundle_id: `ni-fgen`
- source_path: `ni-5451-attenuation.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5451-attenuation.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Attenuation in the NI 5451 is achieved in 3 dB steps in the selectable attenuator bank. Fine resolution attenuation in between each 3 dB step is achieved by the Gain DAC. Attenuating the DAC output signal allows you to vary the signal amplitude while maintaining the dynamic range of the DAC. No bits

### NI 5451 Attenuation

Attenuation in the NI 5451 is achieved in 3 dB steps in the selectable attenuator bank. Fine resolution attenuation in between each 3 dB step is achieved by the Gain DAC.

Attenuating the DAC output signal allows you to vary the signal amplitude while maintaining the dynamic range of the DAC. No bits are lost from the digital representation of the signal and dynamic range is not sacrificed, as would happen if you 
control amplitude by using smaller data ranges of the DAC. Only the gain DAC's 0 dB to 3 dB attenuation is available if the Direct path is selected. For the Main path, the maximum attenuation is 63 dB.

NI-FGEN calculates and sets the correct amount of
attenuation required that corresponds to your NI-FGEN gain setting.
The correct amount of attenuation is implemented in the preamplifier attenuation block to best achieve
the desired output signal amplitude. You can set the amount of gain
with the Arbitrary Waveform Gain property or the 
NIFGEN_ATTR_ARB_GAIN attribute.

Parent topic:

NI 5451 Waveform Amplitude Control

<!--NI_TOPIC bundle=ni-fgen path=ni-5451-baseband-i-q-interpolation.html language=enus -->
## TOPIC 00720: NI 5451 Baseband I/Q Interpolation

- bundle_id: `ni-fgen`
- source_path: `ni-5451-baseband-i-q-interpolation.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5451-baseband-i-q-interpolation.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the behavior of the OSP block during baseband I/Q interpolation. Baseband I/Q interpolation allows the OSP block to interpolate complex data signals at a low sample rate up to a high sample rate. Arbitrary pulse shaping of the data can also be done in the FIR filter. For b

### NI 5451 Baseband I/Q Interpolation

The following figure shows the behavior of the OSP
block during baseband I/Q interpolation.

[IMAGE alt='image' src='GUID-B7D4B7BA-723C-4923-B5CE-6BE234092194-a5.gif']

Baseband I/Q interpolation allows the OSP block to
interpolate complex data signals at a low sample rate up to a high sample rate.
Arbitrary pulse shaping of the data can also be done in the FIR
filter. For baseband I/Q interpolation, complete the following
steps.

1. Enable onboard signal processing by setting the 
OSP
Enabled property or the 
 NIFGEN_ATTR_OSP_ENABLED attribute.
2. Set the OSP mode to Baseband by calling the OSP Mode
property or the 
 NIFGEN_ATTR_OSP_MODE attribute.
3. Specify the use of complex numbers for the waveform data by
setting the 
Data
Processing Mode property or the 
 NIFGEN_ATTR_OSP_DATA_PROCESSING_MODE attribute.
4. Set the 
IQ Rate
property or the 
 NIFGEN_ATTR_OSP_IQ_RATE attribute to the low sample rate of the waveform data.
5. Set the 
FIR Filter
Type property or the 
 NIFGEN_ATTR_OSP_FIR_FILTER_TYPE attribute.
6. Set the corresponding filter parameter.
7. (Optional) Shift the frequency by calling the Frequency Shift property or the 
 NIFGEN_ATTR_OSP_FREQUENCY_SHIFT attribute.
8. Download the low sample rate waveform(s) to the signal
generator.
9. Read the sample rate by calling the Sample Rate property or the NIFGEN_ATTR_ARB_SAMPLE_RATE attribute.

Parent topic:

NI 5451 Common Onboard Signal Processing Applications

<!--NI_TOPIC bundle=ni-fgen path=ni-5451-baseband-interpolation-considerations.html language=enus -->
## TOPIC 00721: NI 5451 Baseband Interpolation Considerations

- bundle_id: `ni-fgen`
- source_path: `ni-5451-baseband-interpolation-considerations.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5451-baseband-interpolation-considerations.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5451 implements baseband interpolation in order to reduce the power of aliased images. Interpolation is a process that effectively turns a lower sample rate into a higher sample rate. Because the signal is now at a higher sample rate, images are moved to higher frequencies, where they fall in

### NI 5451 Baseband Interpolation Considerations

The NI 5451 implements baseband interpolation in order to reduce the power of *aliased images*. Interpolation is a process that effectively turns a lower sample rate into a higher sample rate. Because the signal is now at a higher sample rate, images are moved to higher frequencies, where they fall in the rejection band of the image rejection filter and are suppressed.

NIFGEN_ATTR_ARB_SAMPLE_RATE

Note

NI PXIe-5451 Specifications

#### Interpolation Settings

To determine the total interpolation and interpolated sample rate, divide 400 MS/s by your desired I/Q rate and round down to the nearest step, as noted in the Interpolation table for your total interpolation value. Then, consult the following table for settings that will allow you to achieve your desired interpolated sample rate.

Note

Example: At a desired I/Q rate of 4.5 MS/s, the total interpolation will be determined by the following calculations:

400 MS/s ÷ 4.45 MS/s = 89.88x total interpolation.

A total interpolation rate of 89.88x falls in the 24-8192 Total Interpolation range in the Interpolation table. As this range is measured in steps of 8, you must round down to the nearest multiple of 8, yielding a total interpolation rate of 88x. This value corresponds to a sample rate of 391.6 MS/s and a worst case image at or below -100 dB for the Direct path.

| I/Q Rate (S/s) | Total Interpolation | I or Q Bandwidth (Hz) 1 Sample /symbol | Interpolated Sample Rate* (MS/s) | Theoretical Worst Case Image Feed-through (dB), 20 MHz at Baseband Bandwidth Signal, Main Path | Theoretical Worst Case Image Feed-through† (dB), Maximum I/Q Bandwidth, Main Path | Theoretical Worst Case Image Feed-through (dB), 20 MHz at Baseband Bandwidth Signal, Direct Path | Theoretical Worst Case Image Feed-through† (dB), Maximum I/Q Bandwidth, Direct Path |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 12—24 k | 16384—32768 in steps of 32 | 4.8—9.6 k | 370—400 | N/A | –152 | N/A | <–100 |
| 24—48 k | 8192—16384 in steps of 16 | 9.6—19.2 k | 370—400 | N/A | –152 | N/A | <–100 |
| 48k—16.66 M | 24—8192 in steps of 8 | 19.2 k—6.664 M | 310—400 | N/A | –96 | N/A | –100 |
| 16.66—33.33 M | 12—24 in steps of 4 | 6.664—13.332 M | 300—400 | N/A | –89 | N/A | –88 |
| 33.33—50 M | 8 | 13.332—20 M | 267—400 | N/A | –63 | N/A | –61 |
| 50—67.5 M | 4 | 20—27 M | 200—270 | –22 | –22 | –31 | –23 |
| 67.5—100 M | 4 | 27—40 M | 270—400 | –57 | –50 | –62 | –45 |
| 100—135 M | 2 | 40—54 M | 200—270 | –22 | –27 | –31 | –31 |
| 135—200 M | 2 | 54—80 M | 270—400 | –57 | –27 | –62 | –28 |
| — | 1 | 80—108 M | 200—270 | –22 | –7 | –31 | –8 |
| — | 1 | 108—159.6 M | 270—399 | –57 | –8 | –62 | –8 |
| — | 1 | 120 M | 400 | –87 | –64 | –82 | –52 |
| Assumptions: Internal Sample clock. Desired I/Q and sample rate ranges do not include the lower limit, for example, an I/Q rate of 50 MS/s yields 8x total interpolation. *If your interpolated sample rate falls within an undesirable band, you can use the Modulation Toolkit to provide fractional resampling that will adjust the sample rate to achieve better image rejection. †Calculated from sinc response and typical filter rejection for the NI 5451. Refer to the NI PXIe-5451 Specifications for more information about the expected performance of the NI 5451. |  |  |  |  |  |  |  |

Parent topic:

NI 5451 Onboard Signal Processing (OSP)

Related concepts:

- Aliased Images

<!--NI_TOPIC bundle=ni-fgen path=ni-5451-basic-onboard-signal-processing-prope.html language=enus -->
## TOPIC 00722: NI 5451 Basic Onboard Signal Processing Properties

- bundle_id: `ni-fgen`
- source_path: `ni-5451-basic-onboard-signal-processing-prope.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5451-basic-onboard-signal-processing-prope.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following properties configure the OSP block: OSP Mode OSP Enabled Data Processing Mode IQ Rate Carrier Frequency Frequency Shift FIR Filter Type

### NI 5451 Basic Onboard Signal Processing Properties

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

NI 5451 Onboard Signal Processing (OSP)

Related concepts:

- NI 5451 OSP Mode
- NI 5451 OSP Enabled
- NI 5451 Data Processing Mode
- NI 5451 IQ Rate
- NI 5451 Carrier Frequency Property
- NI 5451 Frequency Shift Property
- NI 5451 FIR Filter Type

<!--NI_TOPIC bundle=ni-fgen path=ni-5451-block-diagram.html language=enus -->
## TOPIC 00723: NI 5451 Block Diagram

- bundle_id: `ni-fgen`
- source_path: `ni-5451-block-diagram.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5451-block-diagram.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: This topic contains information about the NI 5451 top-level block diagram and descriptions of the individual blocks. The following list describes the individual blocks: Onboard Memory stores the waveform data and generation instructions that you load into the device. Clocking allows you to create yo

### NI 5451 Block Diagram

This topic contains information about the
NI 5451 top-level block diagram and descriptions of the
individual blocks.

[IMAGE alt='image' src='GUID-ECC1EF6B-F805-4003-B095-FAD97AB03C6B-a5.gif']

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
 DAC device after any digital gain or onboard signal
processing is applied.

- The waveform data is sent from the 
 DAC to the 
 Analog Output path where the waveform data can be filtered.

- The Routing Matrix allows flexible routing of the PXI Trigger
lines and the external PFI lines.
- The Flatness Correction filter ensures consistent power level across all frequencies. Flatness Correction is disabled by default in NI-FGEN.

Parent topic:

NI 5451 Theory of Operation

<!--NI_TOPIC bundle=ni-fgen path=ni-5451-burst-trigger-mode.html language=enus -->
## TOPIC 00724: NI 5451 Burst Trigger Mode

- bundle_id: `ni-fgen`
- source_path: `ni-5451-burst-trigger-mode.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5451-burst-trigger-mode.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: In Burst trigger mode, calling the first Start trigger begins waveform generation. The waveform then generates continually. The following table provides more information about waveform generation behavior in Arbitrary Waveform and Arbitrary Sequence output modes. Output Mode Trigger Behavior Arbitra

### NI 5451 Burst Trigger Mode

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

NI 5451 Trigger Modes

Related concepts:

- NI 5451 Continuous Trigger Mode

<!--NI_TOPIC bundle=ni-fgen path=ni-5451-calibration.html language=enus -->
## TOPIC 00725: NI 5451 Calibration

- bundle_id: `ni-fgen`
- source_path: `ni-5451-calibration.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5451-calibration.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Before shipping your signal generator, NI calibrated your device to ensure that all features are within specifications. Calibration is a set of operations that compares the values indicated by a measuring instrument or measuring system to the corresponding values realized by external standards. You

### NI 5451 Calibration

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

NI 5451 NI 5451 Overview

<!--NI_TOPIC bundle=ni-fgen path=ni-5451-carrier-frequency-property.html language=enus -->
## TOPIC 00726: NI 5451 Carrier Frequency Property

- bundle_id: `ni-fgen`
- source_path: `ni-5451-carrier-frequency-property.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5451-carrier-frequency-property.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The carrier frequency determines the frequency of the cosine waves (both I and Q) exported from the NCO when the OSP Mode is set to IF. You can use the Carrier Frequency property or the NIFGEN_ATTR_OSP_CARRIER_FREQUENCY attribute to set the carrier frequency. This frequency is programmable during si

### NI 5451 Carrier Frequency Property

The carrier frequency determines the frequency of
the cosine waves (both I and Q) exported from the 
*NCO* when the OSP Mode is set to IF. You can use the 
Carrier
Frequency property or the 
NIFGEN_ATTR_OSP_CARRIER_FREQUENCY attribute to set the carrier frequency. This frequency is
programmable during signal generation.For the NI 5451, the carrier frequency can only be set in IF mode.

For 
*I/Q Rates* below the
interpolation range of the OSP block, NI-FGEN selects a lower
Sample clock rate in order to achieve the requested I/Q Rate.
Because the carrier cannot be more than 0.4 × Sample Rate, these
lower sample rates translate to lower valid carrier rates.

Related Topics

*Carrier Frequency* component

Parent topic:

NI 5451 Basic Onboard Signal Processing Properties

Related concepts:

- NI 5451 Numerically Controlled Oscillator (NCO)
- NI 5451 IQ Rate
- NI 5451 Carrier Frequency

<!--NI_TOPIC bundle=ni-fgen path=ni-5451-carrier-frequency.html language=enus -->
## TOPIC 00727: NI 5451 Carrier Frequency

- bundle_id: `ni-fgen`
- source_path: `ni-5451-carrier-frequency.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5451-carrier-frequency.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The carrier frequency capability is used to modulate complex baseband data up in frequency for direct generation. Applying the carrier frequency capability performs a quadrature upconversion process when the I phase of the NCO leads the Q phase of the NCO by 90 degrees, as shown below. The phases of

### NI 5451 Carrier Frequency

The carrier frequency capability is used to modulate complex baseband data up in frequency for direct generation. Applying the carrier frequency capability performs a quadrature upconversion process when the I phase of the NCO leads the Q phase of the NCO by 90 degrees, as shown below. The phases of either I and/or Q can also be modified to add I/Q impairments to the signal.

[IMAGE alt='image' src='GUID-5AD8ED7A-8B8D-48D3-8442-E4EA5C8487CB-a5.gif']

Note

The Carrier Frequency property or the NIFGEN_ATTR_OSP_CARRIER_FREQUENCY attribute can be used to set the frequency of the NCO Frequency and can be updated during generation. The phase for the two cosine waves are set using the Carrier
Phase I and Carrier
Phase Q properties or the NIFGEN_ATTR_OSP_CARRIER_PHASE_I and NIFGEN_ATTR_OSP_CARRIER_PHASE_Q attributes. Carrier Frequency and Phase can be applied only when the OSP Enabled property is set to True or the NIFGEN_ATTR_OSP_ENABLED attribute is set to VI_TRUE, and the OSP Mode property is set to IF or the NIFGEN_ATTR_OSP_MODE attribute is set to NIFGEN_VAL_OSP_IF. When the Data Processing Mode property is set to Complex or the NIFGEN_ATTR_OSP_DATA_PROCESSING_MODE attribute is set to NIFGEN_VAL_OSP_COMPLEX, the Carrier Frequency performs quadrature upconversion. When the data processing mode is set to Real or NIFGEN_VAL_OSP_REAL, double side band amplitude modulation (AM) occurs at the output of the NI 5451, centered at the carrier frequency.

Parent topic:

NI 5451 Numerically Controlled Oscillator (NCO)

<!--NI_TOPIC bundle=ni-fgen path=ni-5451-clk-in-connector.html language=enus -->
## TOPIC 00728: NI 5451 CLK IN Connector

- bundle_id: `ni-fgen`
- source_path: `ni-5451-clk-in-connector.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5451-clk-in-connector.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The CLK IN front panel connector can accept an external Reference clock, external Sample clock, or external Sample clock timebase. Do not change the external clocks while generating waveforms. Only modify the frequency of the external clock before you start the waveform generation or after you sto

### NI 5451 CLK IN Connector

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

Reference
Clock

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

#### External Sample Clock Timebase Input

The CLK IN connector
also can receive an external Sample clock timebase. Refer to the 
*device
specifications* for the allowable external Sample clock timebase
frequencies and signal characteristics.

Configure the Sample clock timebase source with the 
Sample Clock Timebase Source and Sample Clock Timebase Rate properties or the 
NIFGEN_ATTR_SAMPLE_CLOCK_TIMEBASE_SOURCE and NIFGEN_ATTR_SAMPLE_CLOCK_TIMEBASE_RATE attributes. The device uses the internal sample clock timebase by
default.

Parent topic:

NI 5451 Front Panel

Related concepts:

- NI 5451 Reference Clock

<!--NI_TOPIC bundle=ni-fgen path=ni-5451-clk-out-connector.html language=enus -->
## TOPIC 00729: NI 5451 CLK OUT Connector

- bundle_id: `ni-fgen`
- source_path: `ni-5451-clk-out-connector.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5451-clk-out-connector.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The CLK OUT connector is typically used as an output terminal to provide a clock signal that can be shared by other devices. The CLK OUT connector is designed to allow the NI 5451 to generate high speed clock signals with very low jitter. As an output, the CLK OUT line routes a signal out from the f

### NI 5451 CLK OUT Connector

The CLK OUT connector is typically used as an output terminal to provide a clock signal that can be shared by other devices. The CLK OUT connector is designed to allow the NI 5451 to generate high speed clock signals with very low jitter.

As an output, the CLK OUT line routes a signal out
from the following sources:

- PLL Reference clock source
- Sample Clock Out (with / K where K is an integer used to divide the Sample
clock)
- Sample clock timebase (with / M where M is an integer used to divide the Sample clock
timebase frequency)

Refer to the 
*device specifications* for information about the signal
characteristics for the CLK OUT connector.

Parent topic:

NI 5451 Front Panel

<!--NI_TOPIC bundle=ni-fgen path=ni-5451-clocking-options.html language=enus -->
## TOPIC 00730: NI 5451 Clocking Options

- bundle_id: `ni-fgen`
- source_path: `ni-5451-clocking-options.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5451-clocking-options.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5451 uses a sample clock to generate data. In conjunction with the sample clock, you can also use a reference clock, or less commonly, a sample clock timebase. These clocks are defined as follows: Sample clock: The clock that drives new output data to the DACs. It runs at the sample rate. In

### NI 5451 Clocking Options

The NI 5451 uses a sample clock to generate data. In conjunction with the sample clock, you can also use a reference clock, or less commonly, a sample clock timebase. These clocks are defined as follows:

- Sample clock: The clock that drives new output data to the DACs. It runs at the sample rate. In I/Q generation, the sample rate is an interpolated multiple of the I/Q rate.
- Reference clock — An external clock source used to regulate the frequency and stability of an internally generated sample clock. The NI 5451 onboard PLLs lock to the reference clock.
- Sample Clock Timebase: A high-speed multiple of the sample clock used internally. In general, NI-FGEN manages this clock for you, except in advanced cases where you import or export a sample clock timebase.

The NI 5451 can generate all necessary clocks internally, or you can provide any one of the three clocks as an input. Therefore, there are four main clocking scenarios:

- Internal Sample clock —The onboard clock is used as the
sample clock. The NI 5451 onboard clock combines the low jitter of a divide-down clock with the high resolution of a DDS-based clock. Therefore, there is no difference between the divide down, high resolution, and automatic clock modes for the NI 5451.
- Reference clock— This case is identical to the internal sample clock case, except that the internal sample clock is phase-locked to an external reference clock input. This can facilitate synchronization among devices or can allow you to improve the specifications of the sample clock by training it to a high-quality external clock.
- External Sample clock — An external clock input is used as the sample clock. The external clock passes through a PLL and may optionally be multiplied by the PLL.
- External Sample clock timebase — A high-speed external clock input is used as the basis for the sample clock. The sample clock runs at the rate of the input clock or at an integer division. An external sample clock timebase is an advanced clocking case that allows you to bypass onboard PLLs to preserve the specifications of your input clock.

The following table shows the valid NI-FGEN
property or attribute value combinations that can be used to
configure the clock settings for
an internal Sample clock, an external Sample clock, or a Reference
clock. The term 
Update clock is synonymous with 
Sample clock.

| Sample Clock Source* | Reference Clock* |
| --- | --- |
| "OnboardClk" (default) | "None" (default) |
| "PXI_CLK10" |  |
| "ClkIn" |  |
| "ClkIn" | Not Applicable |
| *These column headings refer to NI-FGEN properties. The attributes that correspond to these properties are NIFGEN_ATTR_SAMPLE_CLOCK_SOURCE and NIFGEN_ATTR_REFERENCE_CLOCK_SOURCE. The values in the columns represent the values that can be set on these properties or attributes. Settings that line up horizontally show valid combinations of the NI-FGEN settings. |  |

Parent topic:

NI 5451 Clocking

Related concepts:

- NI 5451 Reference Clock
- NI 5451 Internal Sample Clock
- NI 5451 External Sample Clock
- NI 5451 External Sample Clock Timebase

<!--NI_TOPIC bundle=ni-fgen path=ni-5451-clocking.html language=enus -->
## TOPIC 00731: NI 5451 Clocking

- bundle_id: `ni-fgen`
- source_path: `ni-5451-clocking.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5451-clocking.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5451 has a Sample clock rate of 12.2 kHz to 400 MHz. The timing of the device is very flexible, and you have multiple choices for deriving the Sample clock. There are modes for deriving the Sample clock from the internal Sample clock timebase, as well as modes to provide external clocks. You

### NI 5451 Clocking

The NI 5451 has a Sample clock
rate of 12.2 kHz to 400 MHz. The timing of the device
is very flexible, and you have multiple choices for deriving the
Sample clock. There are modes for deriving the Sample clock from
the internal Sample clock timebase, as well as modes to provide
external clocks. You also have several choices for providing the
frequency reference for the onboard phase-locked loop.

[IMAGE alt='image' src='GUID-9F461095-5466-4410-9491-3E0E691C11D6-a5.gif']

Related Topics

*Clocking Options*

*Internal Sample Clock
Sources*

*Reference Clock*

*External Sample
Clock Sources*
*External Sample Clock Timebase*

*Exporting Clocks*

Parent topic:

NI 5451 Theory of Operation

Related concepts:

- NI 5451 Clocking Options
- NI 5451 Internal Sample Clock
- NI 5451 Reference Clock
- NI 5451 External Sample Clock
- NI 5451 External Sample Clock Timebase
- NI 5451 Exporting Clocks

<!--NI_TOPIC bundle=ni-fgen path=ni-5451-common-mode-offset-and-differential-l.html language=enus -->
## TOPIC 00732: NI 5451 Common-Mode Offset and Differential Loads

- bundle_id: `ni-fgen`
- source_path: `ni-5451-common-mode-offset-and-differential-l.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5451-common-mode-offset-and-differential-l.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: This assumption does not hold when a differential load is applied between CH 0/1+ and CH 0/1- and a common mode offset is added. To compensate for the discrepancy between software settings and actual signal output, use the following formula to determine the settings necessary to achieve the desired

### NI 5451 Common-Mode Offset and Differential Loads

[IMAGE alt='image' src='GUID-D00AE7E1-92EB-41CE-81B1-F5C2CEDB3B1A-a5.gif']

This assumption does not hold when a differential load is applied between CH 0/1+ and CH 0/1- and a common mode offset is added. To compensate for the discrepancy between software settings and actual signal output, use the following formula to determine the settings necessary to achieve the desired output.

[IMAGE alt='image' src='GUID-E4CA44DE-60E7-41CC-BA91-BEFC454939CB-a5.gif']

[IMAGE alt='image' src='GUID-A029F0CE-CE0E-40E1-A2E1-AE92639D6299-a5.gif']

where

V<sub>cmo set</sub>
 is the value to set for the Common Mode Offset property or NIFGEN_ATTR_COMMON_MODE_OFFSET attribute to achieve V<sub>cmo desired</sub>

R<sub>L</sub>
 is the load impedance in ohms

R<sub>Lset</sub>
 is the load impedance specified by the user

R<sub>D</sub>
 is the differential load impedance

R<sub>S</sub>
 is the single-ended load impedance

Set the load impedance, R<sub>Lset</sub>, to half of the differential load in parallel with the single-ended load on one terminal, to allow the software to correctly scale differential gain and differential offset.

To avoid clipping in differential mode, the waveform maximum multiplied by the gain plus half of the user-specified differential offset plus the common-mode offset should not exceed the maximum output voltage.

Parent topic:

NI 5451 Offset

<!--NI_TOPIC bundle=ni-fgen path=ni-5451-common-onboard-signal-processing-appl.html language=enus -->
## TOPIC 00733: NI 5451 Common Onboard Signal Processing Applications

- bundle_id: `ni-fgen`
- source_path: `ni-5451-common-onboard-signal-processing-appl.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5451-common-onboard-signal-processing-appl.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The OSP block is particularly useful for the following common applications: Baseband I/Q Interpolation Quadrature Upconversion Amplitude Modulation (AM) or Double Sideband Tone Generation

### NI 5451 Common Onboard Signal Processing Applications

The OSP block is particularly useful for the
following common applications:

- Baseband I/Q
Interpolation
- Quadrature
Upconversion
- Amplitude Modulation
(AM) or Double Sideband
- Tone
Generation

Parent topic:

NI 5451 Onboard Signal Processing (OSP)

Related concepts:

- NI 5451 Baseband I/Q Interpolation
- NI 5451 Quadrature Upconversion
- NI 5451 Amplitude Modulation (AM) or Double Sideband
- NI 5451 Tone

<!--NI_TOPIC bundle=ni-fgen path=ni-5451-continuous-trigger-mode.html language=enus -->
## TOPIC 00734: NI 5451 Continuous Trigger Mode

- bundle_id: `ni-fgen`
- source_path: `ni-5451-continuous-trigger-mode.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5451-continuous-trigger-mode.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The waveform you downloaded generates continuously after receiving one Start trigger. All Start triggers after the first Start trigger are ignored. The following table provides more information about waveform generation behavior in Arbitrary Waveform and Arbitrary Sequence output modes. Output Mode

### NI 5451 Continuous Trigger Mode

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

NI 5451 Trigger Modes

<!--NI_TOPIC bundle=ni-fgen path=ni-5451-data-mask.html language=enus -->
## TOPIC 00735: NI 5451 Data Mask

- bundle_id: `ni-fgen`
- source_path: `ni-5451-data-mask.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5451-data-mask.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The signal generator supports analog data masks and static values. The data mask allows you to shield bits of the data to be replaced with the corresponding static value bits. For example, a mask of 0xFF00 and a static value of 0xAAAA applied to a DC waveform with a value of 0x1111 produces a DC wav

### NI 5451 Data Mask

The signal generator supports analog
data masks and static values. The data mask allows you to shield
bits of the data to be replaced with the corresponding static value
bits. For example, a mask of 0xFF00 and a static value of 0xAAAA
applied to a DC waveform with a value of 0x1111 produces a DC
waveform with a value of 0x11AA.

NI-FGEN supports separate and independent analog
and digital data masks and static values. The analog data mask and
analog static value apply to the digital data applied to the DAC,
and ultimately to the signal on the analog output terminal. You can configure an analog data mask by calling the 
Analog Data
Mask or 
Analog
Static Value properties or the 
NIFGEN_ATTR_ANALOG_DATA_MASK and 
NIFGEN_ATTR_ANALOG_STATIC_VALUE attributes.

Parent topic:

NI 5451 NI 5451 Overview

<!--NI_TOPIC bundle=ni-fgen path=ni-5451-data-processing-mode.html language=enus -->
## TOPIC 00736: NI 5451 Data Processing Mode

- bundle_id: `ni-fgen`
- source_path: `ni-5451-data-processing-mode.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5451-data-processing-mode.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Data Processing mode determines whether the OSP block uses only the I signal path to generate waveforms or uses the I and Q signal paths to generate complex waveforms. If the waveform data is configured for real data points by setting the Data Processing Mode property or the NIFGEN_ATTR_OSP_DATA_PRO

### NI 5451 Data Processing Mode

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

NI 5451 Basic Onboard Signal Processing Properties

<!--NI_TOPIC bundle=ni-fgen path=ni-5451-dc-offset.html language=enus -->
## TOPIC 00737: NI 5451 DC Offset

- bundle_id: `ni-fgen`
- source_path: `ni-5451-dc-offset.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5451-dc-offset.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The waveform maximum plus the offset must not exceed the maximum output voltage. If it does, the waveform is clipped. Refer to the device specifications for the NI 5451 maximum output voltage. For example, if you have set a gain of 1.5 in single-ended mode, which corresponds to an amplitude of 3 V[p

### NI 5451 DC Offset

The waveform maximum plus the offset must not exceed the maximum output voltage. If it does, the waveform is clipped. Refer to the *device specifications* for the NI 5451 maximum output voltage. For example, if you have set a gain of 1.5 in single-ended mode, which corresponds to an amplitude of 3 V<sub>pk-pk</sub> DC when the waveform is a sine wave using the full range of the DAC, the maximum DC offset you can apply without clipping the sine wave is ±1 V. At this point, output voltages of the sine waveform have reached the maximum amplitude that the device supports. If you increase the DC offset further, the top/bottom portion of the waveform at ±2.5 V is clipped.

The DC offset can be changed at any time during waveform generation by calling the 
Arbitrary Waveform Offset property or the 
NIFGEN_ATTR_ARB_OFFSET attribute.

The DC offset cannot be set if you selected the
Direct path. The Direct path offset is near zero. Refer to the 
*device
specifications* for information about the maximum value of the
DC offset.

In differential mode, use the 
Arbitrary Waveform Offset property or the 
NIFGEN_ATTR_ARB_OFFSET attribute to control the differential offset. Use the Common Mode Offset property or NIFGEN_ATTR_COMMON_MODE_OFFSET attribute to control the common-mode offset.

Parent topic:

NI 5451 Offset

<!--NI_TOPIC bundle=ni-fgen path=ni-5451-differential-and-single-ended-channel.html language=enus -->
## TOPIC 00738: NI 5451 Differential and Single-Ended Channel Connectors

- bundle_id: `ni-fgen`
- source_path: `ni-5451-differential-and-single-ended-channel.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5451-differential-and-single-ended-channel.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The CH 0+/− and CH 1+/− connectors are the analog waveform output terminals. These connectors provide differential waveform output. CH 0+ and CH 1+ also provide single-ended waveform output. When in differential, direct path mode, the connectors must terminate into balanced loads. The maximum output

### NI 5451 Differential and Single-Ended Channel Connectors

The CH 0+/− and CH 1+/− connectors are the analog waveform
output terminals. These connectors provide differential waveform output. CH 0+ and CH 1+ also provide single-ended waveform output. When in differential, direct path mode, the connectors must terminate into balanced loads. The maximum output levels from these connectors depend on the type of load termination. For example, if the output of the device terminates into a balanced 50 Ω load to ground with *flatness correction* disabled, the maximum output level is ±1.25 V. If the output of the device terminates into a high-impedance load (HiZ), the maximum output level is ±2.5 V. This difference is illustrated in the following figure. The maximum levels can be exclusively offset or gain, or a combination of offset and gain.

[IMAGE alt='image' src='GUID-EF35AE9D-3E8A-4B04-B1FB-0B709C919D44-a5.gif']

If the output terminates into any other load, the maximum output levels for gain or offset are defined by the following formula:

V<sub>out</sub>
 = ± [ 
R<sub>L</sub>
 / ( 
R<sub>L</sub>
 + 
R<sub>S</sub>
 ) ] × 2.5 V

where

V<sub>out</sub>
 is the maximum peak output voltage level

R<sub>L</sub>
 is the load impedance in ohms

S

Note

out

Set the amplitude of the generated output
signal in terms of peak voltage by setting the gain value. NI-FGEN
calculates and sets the correct amount of attenuation required for
the desired gain value. Configure the output signal amplitude by calling the
 
Arbitrary Waveform Gain property or
NIFGEN_ATTR_ARB_GAIN attribute.

#### Load Impedance Compensation

The NI 5451 has the ability to configure the
output signal amplitude and offset based on a user-configured load impedance
setting. This capability is desirable when you use the NI 5451
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

Note

Common-Mode Offset

For waveform output
signal specifications, refer to the 
*device
specifications*.

Parent topic:

NI 5451 Front Panel

Related concepts:

- NI 5451 Flatness Correction
- NI 5451 Common-Mode Offset and Differential Loads

<!--NI_TOPIC bundle=ni-fgen path=ni-5451-digital-gain.html language=enus -->
## TOPIC 00739: NI 5451 Digital Gain

- bundle_id: `ni-fgen`
- source_path: `ni-5451-digital-gain.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5451-digital-gain.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Digital gain multiplies waveform data by a factor you specify in the Digital Gain property or the NIFGEN_ATTR_DIGITAL_GAIN attribute before converting the data to an analog signal in the DAC. Digital gain can be changed during generation without the glitches caused by switching that are common when

### NI 5451 Digital Gain

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

NI 5451 Waveform Amplitude Control

<!--NI_TOPIC bundle=ni-fgen path=ni-5451-events.html language=enus -->
## TOPIC 00740: NI 5451 Events

- bundle_id: `ni-fgen`
- source_path: `ni-5451-events.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5451-events.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use events to indicate when a specific hardware condition has been met on the NI 5451. An event is a signal generated by the NI device at a device state. The NI 5451 supports Ready for Start, Started, Data Marker, Marker, and Done events. The NI 5451 also supports the use of event delays. Re

### NI 5451 Events

You can use *events* to indicate when a specific
hardware condition has been met on the NI 5451. An event is a
signal generated by the NI device at a device state. The NI 5451
supports Ready for Start, Started, *Data Marker*, *Marker*, and Done
events. The NI 5451 also supports the use of *event delays*.

#### Related Topics

*Creating a Marker
Event*

*Creating a Data Marker
Event*

Parent topic:

NI 5451 NI 5451 Overview

Related concepts:

- Events
- Data Marker Events
- Marker Events
- Event Delays
- Creating a Marker Event
- Creating a Data Marker Event

<!--NI_TOPIC bundle=ni-fgen path=ni-5451-exporting-clocks.html language=enus -->
## TOPIC 00741: NI 5451 Exporting Clocks

- bundle_id: `ni-fgen`
- source_path: `ni-5451-exporting-clocks.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5451-exporting-clocks.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5451 provides resources for exporting your clocks and multiple destinations for routing. The following table shows the available clock signals that can be routed to devices external to the signal generator and the destination options. The PFI outputs have a bandwidth of 200 MHz. The PXI Trigg

### NI 5451 Exporting Clocks

The NI 5451 provides resources for exporting your clocks and multiple destinations for
routing.

[IMAGE alt='image' src='GUID-A16BC157-0B86-4AD7-9DBA-FA1CACD04629-a5.gif']

Note

| Clock to be Exported | Destination Options |  |  |
| --- | --- | --- | --- |
|  | CLK OUT | PFI<0..1> | PXI_Trig<0..6> |
| Sample Clock/K | K ≥1 | K ≥2 | K ≥2 |
| SCTB/M | M ≥1 | M ≥2 | M ≥2 |
| Reference Clock | Always | Always | Always |
| Note: All divisors have a default value of 1. If a divisor is greater than 1, the divided clock output is not phase aligned with waveform generation. Refer to the Exporting Signals topic for more information. |  |  |  |

For synchronization purposes, the
NI 5451 allows you to export your clocks 
so that other devices can share the timing of the NI 5451. The following sections describe the possible clock routing configurations.

#### Sample Clock

The Sample clock can be routed to the CLK OUT front panel SMA connector.

Additionally, the exported clock can be divided
down by an integer value (no less than 2) and exported to
the PFI <0..1> connectors, the CLK OUT connector, or the PXI_Trig<0..6>
lines. Refer to the 
Exported Sample Clock Divisor property or the 
NIFGEN_ATTR_EXPORTED_SAMPLE_CLOCK_DIVISOR attribute for more information about configuring the Sample
clock divisor.

#### Sample Clock Timebase

The Sample clock timebase can be routed to the CLK OUT front panel SMA connector.

Additionally, the exported clock can be divided
down by an integer value and exported to the
PFI <0..1> connectors, the CLK OUT connector, or the PXI_Trig<0..6>
lines. You can configure the Sample clock divisor by calling the 
Exported Sample Clock Timebase Divisor property or the 
NIFGEN_ATTR_EXPORTED_SAMPLE_CLOCK_TIMEBASE_DIVISOR attribute.

#### Reference Clock

The Reference clock is the
clock that is configured for the signal generator
phase-locked loop circuit to use as a reference. A clock configured as a PLL Reference clock source is available for exporting. The Reference clock can be routed to
the PFI <0..1> front panel SMB connectors, the CLK OUT front panel SMA connector, or the PXI_Trig<0..6>
lines on the PXI trigger bus.

Note

#### Destination Options

The following sections define the destinations for
exported clocks.

PFI <0..1>—The Sample clock (when K ≥2), the Sample clock timebase (when M ≥2), and the
Reference clock can be exported to the PFI 0 and PFI 1 SMB
connectors on the front panel to synchronize external devices. You
must configure the device to export the desired clock to the PFI SMB connectors.

CLK OUT—The Sample clock, the Sample clock timebase, and the
Reference clock can be exported to the CLK OUT SMA
connectors on the front panel to synchronize external devices. You
must configure the device to export the desired clock to the CLK OUT SMA connector.

PXI_Trig<0..6>—Sample clock (when K ≥2), the Sample clock timebase (when M ≥2), and the
Reference clock can be exported to the PXI_Trig lines. The PXI standards allow for devices to route signals
to other devices in your PXI Express chassis to enhance device-to-device
synchronization. Refer to the chassis documentation for
specifications to ensure the reference signal is within tolerance.
You must configure the device to export the desired clock to the
PXI_Trig line.

Refer to 
niFgen Export
Signal VI or the 
niFgen_ExportSignal function for more information about configuring the
destinations for the desired clock signal.

Parent topic:

NI 5451 Clocking

Related concepts:

- NI 5451 Exporting Signals

<!--NI_TOPIC bundle=ni-fgen path=ni-5451-exporting-signals.html language=enus -->
## TOPIC 00742: NI 5451 Exporting Signals

- bundle_id: `ni-fgen`
- source_path: `ni-5451-exporting-signals.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5451-exporting-signals.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The signal generator contains seven PXI trigger lines that are available for sending signal generator-specific information to other devices that have PXI trigger bus connectors. The signal generator has connectors on the front panel to route signals to devices external to the PXI Express chassis. Th

### NI 5451 Exporting Signals

The signal generator contains seven PXI trigger
lines that are available for sending signal generator-specific
information to other devices that have PXI trigger bus
connectors.

Signal Routing

Note

|  |  | Destination |  |  |
| --- | --- | --- | --- | --- |
| PXI_TRIG<0..6> | PFI 0 and PFI 1 Connectors | CLK OUT |  |  |
| Exported Clocks, Triggers, and Events | Sample Clock | Yes (when /K with K ≥2) | Yes (when /K with K ≥2) | Yes |
| Sample Clock Timebase | Yes (when /M with M ≥2) | Yes (when /M with M ≥2) | Yes |  |
| PLL Reference Source | Yes | Yes | Yes |  |
| Out Start trigger | Yes | Yes | No |  |
| Marker Event | Yes | Yes | No |  |

Sample Clock

Note

Sample Clock Timebase

Note

Reference clock–A clock signal
that is only available when a Reference clock source for the PLLs has been
configured. The clock is the source selected as the PLL Reference
clock source.

Start trigger out–A signal generated by the
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
Generation mode waveform generation to any of the PXI trigger lines
or the PFI 0 and PFI 1 connectors.
- The signal generator Start trigger output signal to other
devices through any of the PXI trigger lines
or the PFI 0 and PFI 1 connectors.
- The signal generator Sample clock signal to other devices
through any of the PXI trigger lines or front panel
connectors.
- The signal generator Sample clock timebase signal to other devices
through any of the PXI trigger lines or front panel
connectors.
- The PLL Reference clock source to other devices through any of
the PXI trigger lines or front panel connectors.

In NI-FGEN, the PXI trigger lines are referred to
as RTSI<0..6>. The correlation between PXI_TRIG< 
x> and RTSI< 
x> is one to one. For more information about
configuring and routing the device internal signals, refer to the 
niFgen Export Signal VI
or the 
niFgen_ExportSignal function.

Parent topic:

NI 5451 NI 5451 Overview

Related concepts:

- NI 5451 Signal Routing

<!--NI_TOPIC bundle=ni-fgen path=ni-5451-external-sample-clock-timebase.html language=enus -->
## TOPIC 00743: NI 5451 External Sample Clock Timebase

- bundle_id: `ni-fgen`
- source_path: `ni-5451-external-sample-clock-timebase.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5451-external-sample-clock-timebase.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: An external sample clock timebase is an external source that drives the output DACs almost directly. The sample clock rate can equal the sample clock timebase rate or be an integer division. You can set the Sample clock timebase source by calling the Sample Clock Timebase Source property or the NIFG

### NI 5451 External Sample Clock Timebase

An external sample clock timebase is an external
source that drives the output DACs almost directly. The sample clock rate can equal the sample clock timebase rate or be an integer division.

[IMAGE alt='image' src='GUID-398511A7-043F-4E7A-ABDC-8946FB579C2F-a5.gif']

NIFGEN_ATTR_SAMPLE_CLOCK_TIMEBASE_SOURCE

NIFGEN_ATTR_SAMPLE_CLOCK_TIMEBASE_RATE

Caution

NIFGEN_ATTR_EXPORTED_SAMPLE_CLOCK_TIMEBASE_OUTPUT_TERMINAL

Note

device specifications

Parent topic:

NI 5451 Clocking Options

<!--NI_TOPIC bundle=ni-fgen path=ni-5451-external-sample-clock.html language=enus -->
## TOPIC 00744: NI 5451 External Sample Clock

- bundle_id: `ni-fgen`
- source_path: `ni-5451-external-sample-clock.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5451-external-sample-clock.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5451 can accept an external clock to directly drive the Sample clock. When using an external Sample clock, the frequency stability and accuracy of the Sample clock is determined by the provided external Sample clock. The following figure shows possible Sample Clock paths. You can set the cloc

### NI 5451 External Sample Clock

The NI 5451 can accept an
external clock to directly drive the Sample clock. When using an
external Sample clock, the frequency stability and accuracy of the
Sample clock is determined by the provided external Sample
clock.

The following figure shows possible Sample
Clock paths.

[IMAGE alt='image' src='GUID-87D5D904-8A0D-42AD-AA11-DA16314DAA98-a5.gif']

You can set the clock source by calling the
niFgen
Configure Sample Clock Source VI or the 
niFgen_ConfigureSampleClockSource function.

If the external sample clock differs from the desired sample rate, you can multiply the clock by calling the
External Sample Clock Multiplier property or the 
NIFGEN_ATTR_EXTERNAL_SAMPLE_CLOCK_MULTIPLIER attribute.

niFgen_ConfigureSampleRate

Note

device specifications

#### External Sample Clock Considerations

The NI 5451 incorporates
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
reprograms the NI 5451 for the new settings,
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

NI 5451 Clocking Options

<!--NI_TOPIC bundle=ni-fgen path=ni-5451-filtering-and-interpolation.html language=enus -->
## TOPIC 00745: NI 5451 Filtering and Interpolation

- bundle_id: `ni-fgen`
- source_path: `ni-5451-filtering-and-interpolation.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5451-filtering-and-interpolation.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The filtering and interpolation stage of the OSP block increases the effective sample rate of the signal generator while protecting the frequency spectrum of the interpolated data from images. This protection occurs when the data passes through a lowpass filter after zero stuffing. The frequency res

### NI 5451 Filtering and Interpolation

The filtering and interpolation stage of the 
*OSP* block increases the effective
sample rate of the signal generator while protecting the frequency
spectrum of the interpolated data from images. This protection
occurs when the data passes through a lowpass filter after zero
stuffing. The frequency response of the low pass filter can be
changed with the 
Filter
Type property or the 
NIFGEN_ATTR_OSP_FIR_FILTER_TYPE attribute.

[IMAGE alt='image' src='GUID-C1BDF7AF-B534-458E-A2A9-BA1D9A6DD7BE-a5.gif']

Parent topic:

NI 5451 Onboard Signal Processing Components

Related concepts:

- NI 5451 Onboard Signal Processing (OSP)

<!--NI_TOPIC bundle=ni-fgen path=ni-5451-filtering-effects.html language=enus -->
## TOPIC 00746: NI 5451 Filtering Effects

- bundle_id: `ni-fgen`
- source_path: `ni-5451-filtering-effects.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5451-filtering-effects.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The delay from the time at which the device receives a trigger to the time at which the analog output signal is generated increases if the digital and/or analog filters in the Analog Output path are enabled. In the case of digital filtering, delay also increases with increase in interpolation. Enabl

### NI 5451 Filtering Effects

Analog Output path

onboard signal processing block

Note

Refer to the 
*device
specifications* for the delay from trigger to analog output
based on different filtering options.

Parent topic:

NI 5451 Analog Output

Related concepts:

- NI 5451 Analog Output
- NI 5451 Onboard Signal Processing (OSP)

<!--NI_TOPIC bundle=ni-fgen path=ni-5451-filtering-effects_2.html language=enus -->
## TOPIC 00747: NI 5451 Filtering Effects

- bundle_id: `ni-fgen`
- source_path: `ni-5451-filtering-effects_2.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5451-filtering-effects_2.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The delay from the time at which the device receives a trigger to the time at which the analog output signal is generated increases if the digital and/or analog filters in the Analog Output path are enabled. In the case of digital filtering, delay also increases with increase in interpolation. Enabl

### NI 5451 Filtering Effects

Analog Output path

onboard signal processing block

Note

Refer to the 
*device
specifications* for the delay from trigger to analog output
based on different filtering options.

Parent topic:

NI 5451 Triggering

<!--NI_TOPIC bundle=ni-fgen path=ni-5451-fir-filter-type-flat.html language=enus -->
## TOPIC 00748: NI 5451 FIR Filter Type: Flat

- bundle_id: `ni-fgen`
- source_path: `ni-5451-fir-filter-type-flat.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5451-fir-filter-type-flat.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Passband Value: 0.40 This lowpass filter is designed to give a flat response until the passband value. The passband value is a fraction of the I/Q Rate coming into the FIR filter. Use the Flat Filter Passband property or the NIFGEN_ATTR_OSP_FIR_FILTER_FLAT_PASSBAND attribute to set the passband valu

### NI 5451 FIR Filter Type: Flat

Passband Value: 0.40

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

[IMAGE alt='image' src='GUID-1343D8E2-F83F-4310-A25D-36DA2801503C-a5.gif']

Parent topic:

NI 5451 FIR Filter Types

Related concepts:

- NI 5451 I/Q Rate Controller

<!--NI_TOPIC bundle=ni-fgen path=ni-5451-fir-filter-type-raised-cosine.html language=enus -->
## TOPIC 00749: NI 5451 FIR Filter Type: Raised Cosine

- bundle_id: `ni-fgen`
- source_path: `ni-5451-fir-filter-type-raised-cosine.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5451-fir-filter-type-raised-cosine.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Alpha Values: 0.1 to 0.4 This lowpass filter is commonly used in communications applications. The passband of the raised cosine filter with the roll-off factor, α, stops at 0.5 × (1 − α) times the I/Q Rate. The stopband of the raised cosine filter begins at 0.5 × (1 + α) times the I/Q Rate. The tran

### NI 5451 FIR Filter Type: Raised Cosine

Alpha Values: 0.1 to 0.4

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

Parent topic:

NI 5451 FIR Filter Types

Related concepts:

- NI 5451 I/Q Rate Controller

<!--NI_TOPIC bundle=ni-fgen path=ni-5451-fir-filter-type-root-raised-cosine.html language=enus -->
## TOPIC 00750: NI 5451 FIR Filter Type: Root Raised Cosine

- bundle_id: `ni-fgen`
- source_path: `ni-5451-fir-filter-type-root-raised-cosine.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5451-fir-filter-type-root-raised-cosine.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Alpha Values: 0.1 to 0.4 This lowpass filter is commonly used in communications applications. The passband of the root raised cosine filter with the roll-off factor, α, stops at 0.5 × (1 − α) times the I/Q Rate. The stopband of the root raised cosine filter begins at 0.5 × (1 + α) times the I/Q Rate

### NI 5451 FIR Filter Type: Root Raised Cosine

Alpha Values: 0.1 to 0.4

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
Raised Cosine Filter Alpha property or the 
NIFGEN_ATTR_OSP_FIR_FILTER_RAISED_COSINE_ALPHA attribute to set the 
α value.

The following diagram shows an ideal root raised
cosine filter response with an 
α of 0.5. The frequency
axis is scaled as a fraction of the 
I/Q
Rate.

[IMAGE alt='image' src='GUID-AAD8865C-5B03-4E67-8E39-2FD2389E6EBA-a5.gif']

Parent topic:

NI 5451 FIR Filter Types

Related concepts:

- NI 5451 I/Q Rate Controller
