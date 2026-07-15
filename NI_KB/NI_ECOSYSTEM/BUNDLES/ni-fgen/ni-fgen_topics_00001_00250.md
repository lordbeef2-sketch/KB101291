# NI DOCUMENT BUNDLE: ni-fgen

<!--NI_BUNDLE_CHUNK bundle=ni-fgen start=1 end=250 -->
<!--NI_TOPIC bundle=ni-fgen path=abort-generation.html language=enus -->
## TOPIC 00001: Abort Generation

- bundle_id: `ni-fgen`
- source_path: `abort-generation.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/abort-generation.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The abort generation step aborts any signal generation that was initiated in the initiate generation step. When you abort generation, you can choose to either abort to ground or abort to a known voltage (not available in Standard Function or Frequency List output modes).

### Abort Generation

The abort generation step aborts any signal
generation that was initiated in the 
*initiate generation* step.
When you abort generation, you can choose to either 
*abort to ground* or 
*abort to a known
voltage* (not available in Standard Function or Frequency List
output modes).

Parent topic:

NI-FGEN Tutorial

Related concepts:

- Initiate Generation
- Abort to Ground
- Abort to a Known Voltage

<!--NI_TOPIC bundle=ni-fgen path=abort-to-a-known-voltage.html language=enus -->
## TOPIC 00002: Abort to a Known Voltage

- bundle_id: `ni-fgen`
- source_path: `abort-to-a-known-voltage.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/abort-to-a-known-voltage.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Arbitrary Waveform, Arbitrary Sequence, and Script output modes can abort generation to a known voltage. When waveform generation is aborted, the analog output signal remains at the voltage corresponding to the last waveform generated until the device is reconfigured for another generation. Closin

### Abort to a Known Voltage

Note

#### LabVIEW Example

To abort the generation to known voltage, complete
the following steps:

1. During your application, download a small,
constant–amplitude waveform that corresponds to the desired
output voltage. You will generate this waveform at the end of your
application.
2. Abort generation of the current waveform by calling the 
niFgen Abort
Generation VI.
3. Reconfigure the device to generate the constant–amplitude
waveform.
4. Call the 
niFgen
Initiate Generation VI to transition the device to the
Generation state.
5. Call the 
niFgen Abort
Generation VI to stop generation of the constant-amplitude
waveform.

#### C Example

To abort the generation to known voltage, complete
the following steps:

1. During your application, download a small,
constant–amplitude waveform that corresponds to the desired
output voltage. You will generate this waveform at the end of your
application.
2. Abort generation of the current waveform by calling the 
 niFgen_AbortGeneration function.
3. Reconfigure the device to generate the constant–amplitude
waveform.
4. Call the 
 niFgen_InitiateGeneration function to transition the device to the Generation
state.
5. Call the 
 niFgen_AbortGeneration function to stop generation of the constant-amplitude
waveform.

Parent topic:

Abort Generation

<!--NI_TOPIC bundle=ni-fgen path=abort-to-ground.html language=enus -->
## TOPIC 00003: Abort to Ground

- bundle_id: `ni-fgen`
- source_path: `abort-to-ground.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/abort-to-ground.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: All operation modes can abort to ground. To abort to ground you must disable the output enable relay to remove the DC voltage from the output. LabVIEW Example To abort generation to ground, complete the following steps: Call the niFgen Output Enable VI to with Output Enable set to FALSE to disable t

### Abort to Ground

All operation modes can abort to ground. To abort
to ground you must disable the output enable relay to remove the DC
voltage from the output.

#### LabVIEW Example

To abort generation to ground, complete the
following steps:

1. Call the 
niFgen Output
Enable VI to with 
 Output Enable set to FALSE to disable the analog
output and remove any DC voltage on the analog output.
2. Call the 
niFgen Abort
Generation VI to stop the waveform generation.

#### C Example

1. Call the 
 niFgen_ConfigureOutputEnabled function with the 
 enabled parameter set to 
VI_FALSE to disable the analog
output and to remove any DC voltage on the analog output.
2. Call the 
 niFgen_AbortGeneration function to stop the waveform generation.

Parent topic:

Abort Generation

<!--NI_TOPIC bundle=ni-fgen path=active-image.html language=enus -->
## TOPIC 00004: Active Image

- bundle_id: `ni-fgen`
- source_path: `active-image.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/active-image.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The active video image resulting from the scanning always has an aspect ratio (horizontal/vertical) of 4/3, independent of the video format. The color composite video signal shows that the scanning process requires some additional room on the left and right sides of each line, as well as on the top

### Active Image

The active video image resulting from the scanning always has an aspect ratio (horizontal/vertical) of 4/3, independent of the video format. The *color composite video signal* shows that the scanning process requires some additional room on the left and right sides of each line, as well as on the top and bottom of the active video image region. This additional room includes the synchronization signals, color bursts, and other format-specific information, like the ITS, which are not part of the active video image. Approximately 90% of all the lines and 80% of each line can transmit the active image information. The exact values depend on the video format, as shown in the following table.

| Video Format | Lines/Frame | Active Lines | Frame Rate | Line Duration | Active Line Duration |
| --- | --- | --- | --- | --- | --- |
| M-NTSC/M-PAL | 525 | 480/486 | 29.97 frames/sec | 63.55 µs | 52.2 µs |
| All others | 625 | 576 | 25.00 frames/sec | 64.00 µs | 52.0 µs |

Active Lines represents the number of lines that are actually used to transmit the image information. For example, only 480 lines out of 525 lines/frame transmit the image information in NTSC. Likewise, on each line, the image information is transmitted only during the active lines sequence, which is shorter than the entire line duration. For example, of 63.55 µs only 52.2 µs are the active line duration in NTSC. Frame rate is the scanning speed described in *Scanning Speed*.

Parent topic:

Video Signal Fundamentals

Related concepts:

- Generating Composite Video Signals
- Scanning Speed

<!--NI_TOPIC bundle=ni-fgen path=aliased-images.html language=enus -->
## TOPIC 00005: Aliased Images

- bundle_id: `ni-fgen`
- source_path: `aliased-images.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/aliased-images.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: An aliased image is a frequency component that appears in continuous time waveforms being recreated from discrete–time, digital waveforms. The frequencies where these extra components appear are related to both the frequency of the signals being recreated as well as the frequency of the sample rate.

### Aliased Images

An aliased image is a frequency component that appears in continuous time waveforms being recreated from discrete–time, digital waveforms. The frequencies where these extra components appear are related to both the frequency of the signals being recreated as well as the frequency of the sample rate. Looking only at positive frequencies, the two frequencies are related by the following equation:

f <sub>ai</sub>
 = | f<sub>o</sub> + nf <sub>s</sub>
|

where

f<sub>ai</sub>
 = the aliased images

f<sub>o</sub>
 = the desired waveform frequency

f<sub>s</sub>
 = the sample rate

n = an integer (either positive or negative)

As the equation indicates, there are an infinite number of these aliased images that occur. As n gets larger, however, the power content of these extra frequencies "falls off."

The following figure shows a 1 MHz sine wave generated by a 6 MS/s DAC. The dotted line represents an aliased image signal that shows up as a 5 MHz component. In this case, f<sub>o</sub>
 is 1 MHz, n is –1, and f <sub>s</sub>
 is 6 MHz; resulting in the following formula:

f<sub>ai</sub>
 = 5 MHz = |1 MHz + (–1)(6 MHz)|

The other possible frequencies of sine waves can be calculated and superimposed onto the sampling points of the image.

[IMAGE alt='image' src='GUID-3D8A62FB-61A8-4B11-9E78-311AE33FB903-a5.gif']

The following figure shows the frequency domain representation of the previous example. The vertical arrow at f<sub>o</sub> represents the frequency and signal power of the desired generated signal. The other vertical arrows represent the frequencies and signal powers of the aliased image frequency components that appear in the frequency spectrum.

[IMAGE alt='image' src='GUID-48B23A69-3157-4950-8DEE-62B5D8DE8328-a5.gif']

In systems where you want to generate accurate signals using sampled data, you must introduce an optional *lowpass filter* after the DAC to restrict the bandwidth of the output signal to meet the sampling criteria (*Shannon's Sampling theorem*).

Parent topic:

Nyquist and Shannon's Sampling Theorems

Related concepts:

- Filtering and Interpolation
- Nyquist and Shannon's Sampling Theorems

<!--NI_TOPIC bundle=ni-fgen path=arbitrary-sequence-mode.html language=enus -->
## TOPIC 00006: Arbitrary Sequence Mode

- bundle_id: `ni-fgen`
- source_path: `arbitrary-sequence-mode.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/arbitrary-sequence-mode.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Arbitrary sequence output mode allows you to load multiple waveforms in the onboard memory of the signal generator. A finite number of samples make a waveform. To generate these downloaded waveforms in a specific order, you must prepare a sequence, which contains a number of segments in a specific o

### Arbitrary Sequence Mode

Arbitrary sequence output mode allows you to load multiple waveforms in the onboard
 memory of the signal generator.

A finite number of samples make a waveform. To generate these downloaded waveforms in a specific
 order, you must prepare a sequence, which contains a number of segments in a specific order.
 Each segment specifies a downloaded waveform, a number of loops to repeat the selected
 waveform, and a numeric offset in which a marker is generated by the instrument. The timing
 and behavior of the generation of a waveform sequence is dependent on the trigger mode
 selected.

| Waveform or Segment Type | Waveform or Segment Shape | Description |
| --- | --- | --- |
| Waveform A |  | A single cycle of a sine wave that is downloaded to onboard memory |
| Waveform B |  | A single cycle of a ramp waveform that is downloaded to onboard memory |
| Waveform Segment 1 |  | A segment created using Waveform A that repeats or loops three times |
| Waveform Segment 2 |  | A segment created using Waveform B that loops twice |
| Waveform Segment 3 |  | A segment created using Waveform A that loops only once |
| Sequence List or Waveform Linking |  | The waveforms are linked in a sequence. The concept of using a sequence to generate waveforms is referred to as waveform sequencing or linking and looping waveforms. |

#### Segment Components

You create a sequence segment by segment. Each segment is made up of the following four
 components.

Waveform Handle

niFgen Create Waveform

niFgen Allocate
 Waveform

niFgen_CreateArbWaveform

niFgen_AllocateWaveform

Sample Count

Waveform Loops

Marker Offset

Marker Events

Refer to the niFgen Create Arbitrary Sequence or niFgen Create
 Advanced Arb Sequence VIs or the niFgen_CreateArbSequence or
 niFgen_CreateAdvancedArbSequence functions for more information about
 creating and configuring arbitrary sequences.

Parent topic:

Output Modes

Related concepts:

- Trigger Modes
- Marker Events

<!--NI_TOPIC bundle=ni-fgen path=arbitrary-waveform-output-mode.html language=enus -->
## TOPIC 00007: Arbitrary Waveform Output Mode

- bundle_id: `ni-fgen`
- source_path: `arbitrary-waveform-output-mode.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/arbitrary-waveform-output-mode.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: For NI signal generators, the Arbitrary Waveform output mode generates waveforms from user–created or user–provided waveform arrays of numeric data. The waveform arrays are downloaded to the onboard memory on the arbitrary waveform generator. Arbitrary Waveform output mode also uses memory for stori

### Arbitrary Waveform Output Mode

For NI signal generators, the Arbitrary Waveform output mode generates waveforms from user–created or user–provided waveform arrays of numeric data. The waveform arrays are downloaded to the onboard memory on the arbitrary waveform generator. Arbitrary Waveform output mode also uses memory for storing the instructions for generating waveform sequences in the waveform memory.

Parent topic:

Output Modes

<!--NI_TOPIC bundle=ni-fgen path=bandwidth-and-passband-flatness.html language=enus -->
## TOPIC 00008: Bandwidth and Passband Flatness

- bundle_id: `ni-fgen`
- source_path: `bandwidth-and-passband-flatness.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/bandwidth-and-passband-flatness.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The bandwidth of a signal source is defined as the frequency at which the amplitude of the frequency response is 3 dB lower than the amplitude of the frequency response at DC or a low frequency. The bandwidth of a source is limited by the output amplifier design or by filters in the analog output ci

### Bandwidth and Passband Flatness

Note

Passband flatness is a measure of the amplitude accuracy of the frequency response with respect to frequency. Passband flatness is usually specified in ±dB, and it is usually referenced to the amplitude of the frequency response at a designated frequency.

For example, a specification might be listed as ±1 dB with respect to the amplitude of the frequency response at 50 kHz. This method is used because two different metrology instruments, a digital multimeter (DMM) and a power meter, are used to measure passband flatness. The power meter is an excellent metrology instrument for measuring passband flatness, but its performance can be improved by calibrating its frequency response at a low frequency, such as 50 kHz, with a DMM. In other words, the DMM measures the amplitude of a 50 kHz tone, and the power meter measures the amplitude of all other frequencies with respect to the amplitude of the 50 kHz tone measured by the DMM.

Passband flatness is important in many applications. For example, if the sensitivity of a receiver is being tested, it is important to know the variation of the amplitude of the test tone as it is swept across the frequency band of interest. Some NI signal generators have a Direct Output analog path that has been optimized for passband flatness. Other signal generators allow you to select a frequency at which the calibrated amplitudes can be finely adjusted to achieve the best amplitude accuracy near the selected frequency.

Parent topic:

Waveform Fundamentals

<!--NI_TOPIC bundle=ni-fgen path=break.html language=enus -->
## TOPIC 00009: break

- bundle_id: `ni-fgen`
- source_path: `break.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/break.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Enable the execution of instructions to skip directly to the next instruction after the break block once the device receives a trigger. The following restrictions apply when using the break instruction: Do not use instructions that require a reaction to a trigger. These instructions include the repe

### break

Enable the execution of instructions to skip directly to
 the next instruction after the break block once the device receives a
 trigger.

The following restrictions apply when using the break instruction:

- Do not use instructions that require a reaction to a trigger. These instructions include
 the repeat until trigger , if-else , and wait until
 trigger .
- Do not nest break instructions.
- Do not use the clear instruction.
- A generate or wait <N> 
 instruction must precede the break block.
- Do not use the stream instruction.

#### Usage

Go to the next instruction following
 the break block as soon as Script trigger N is
 received.

```text
generate
break on scriptTrigger <N>
  <instructions>
end break
<instructions>
```

```text
wait <N>
break on scriptTrigger <N>
  <instructions>
end break
<instructions>
  
```

#### break Example

In the following scripts, ScriptTrigger0 is a Stop trigger. The script
 exits the repeat forever loop immediately when the device receives the
 trigger. The script does not wait for the final waveform in the loop,
 testWfm1, to be generated. Script B generates wfm 1000
 times, but stops generation as soon as the device detects the script trigger. A marker is
 placed at the start of the wfm and exported to a counter device. This setup
 helps determine how many times the wfm is generated before the specified
 condition is met.

```text
Script A
generate wfm
  break on ScriptTrigger0
    repeat forever
      generate testWfm0
      wait 12
      generate testWfm1
    end repeat
  end break
end script
    
```

```text
Script B
generate wfm
  break on ScriptTrigger0
    repeat 10000
      generate hugeTestWfm marker0(1)
    end repeat
  end Break
  generate idleStateWfm
end script
    
```

Parent topic:

Scripting Instructions

<!--NI_TOPIC bundle=ni-fgen path=clear.html language=enus -->
## TOPIC 00010: clear

- bundle_id: `ni-fgen`
- source_path: `clear.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/clear.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Clear a received Script trigger. The clear instruction is commonly used immediately before a wait or a repeat until instruction. This way, the script ignores Script triggers that are received before the wait or the repeat until instructions. Usageclear scripttrigger0 clear Examples Execute the follo

### clear

Clear a received Script trigger.

The clear instruction is commonly used immediately before a
 wait or a repeat until instruction. This way, the script
 ignores Script triggers that are received before the wait or the
 repeat until instructions.

#### Usage

```text
clear scripttrigger0
```

#### clear
 Examples

- Execute the following sequence: generate myWfmA
clear scripttrigger0
wait until scripttrigger0
generate myWfmB Without the clear instruction, any Script
 trigger received during the generation of myWfmA causes
 myWfmB to be generated after the smallest possible delay.
  1. Generate myWfmA .
  2. Clear any Script triggers.
  3. Wait for receipt of a Script trigger.
  4. Generate myWfmB .
- Continuously step between three waveforms, waiting for a Script trigger between each
 waveform. repeat forever
 clear scripttrigger0
 wait until scripttrigger0
 generate myWfmA

 clear scripttrigger0
 wait until scripttrigger0
 generate myWfmB

 clear scripttrigger0
 wait until scripttrigger0
 generate myWfmC
end repeat

clear

wait

```text
generate myWfmA
wait until scripttrigger0
wait until scripttrigger0
generate myWfmB
```

The device waits for two Script triggers to occur before
 generating myWfmB. A repeat until instruction or an
 if/else/end if instruction consumes a Script trigger in the same
 way.

Parent topic:

Scripting Instructions

<!--NI_TOPIC bundle=ni-fgen path=clocking.html language=enus -->
## TOPIC 00011: Clocking

- bundle_id: `ni-fgen`
- source_path: `clocking.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/clocking.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: NI signal generators offer a number of options for configuring the clocking of your device. Clocking is used to control the rate at which signals are generated. An internal voltage-controlled crystal oscillator (VCXO) behaves as a Sample clock timebase for the signal generator. This Sample clock tim

### Clocking

NI signal generators offer a number of options for configuring the clocking of your device. Clocking is used to control the rate at which signals are generated. An internal voltage-controlled crystal oscillator (VCXO) behaves as a Sample clock timebase for the signal generator. This Sample clock timebase is either configured or replaced by using one of the following methods:

- Internal Sample clock—The internal Sample clock timebase is used to determine clocking rates. In Arbitrary Waveform mode, you can control this timebase by choosing a clock mode for your signal generator (Divide-Down or High-Resolution).
- Reference clock—An external device is used as a Reference clock in the phase-locked loop (PLL) of the signal generator. This causes the Reference clock to phase-lock to the Sample clock timebase so that the frequency stability and accuracy of the Sample clock timebase matches that of the Reference clock.
- External Sample clock—An external Sample clock directly drives the clocking of the signal generator.

Note

#### Clock Mode

The clock mode is applicable only when using an internal Sample clock. The clock mode determines the method of deriving the Sample clock from the Sample clock timebase—the main timing component of the device. You can set the clock mode with the Clock Mode property or the NIFGEN_ATTR_CLOCK_MODE attribute.

There are three options for deriving the clock mode on the NI 5412/5421/5422/5441/5442: Divide-Down (Divide by N) Sampling, High-Resolution Sampling, and Automatic mode (the default mode for NI-FGEN).

Divide-Down Clocking Mode

Divide-Down clocking configures the Sample clock timebase. The Sample clock timebase is usually a voltage–controlled crystal oscillator (VCXO). The valid sample rates for Divide-Down clocking are integer divisions of the Sample clock timebase frequency. The sample rate is given by the formula:

SR = SCTF/n

where

SR = sample rate

n = integer from 1 to a maximum value for the specific device

SCTF = Sample clock timebase frequency for the specific device

For example, a signal generator with a Sample clock timebase frequency of 100 MS/s has available sample rates that are integer divisions of 100 MS/s, as shown in the following examples:

SCTF/1 = 100 MS/s

SCTF/2 = 50 MS/s

SCTF/3 = 33.333 MS/s

As the integer n increases, the available sample rate decreases. If you choose a sample rate other than an integer division of the Sample clock timebase, the device usually coerces the sample rate setting to the nearest sample rate or integer division of the Sample clock timebase.

Divide-Down clocking provides the lowest jitter Sample clock, and it is also referred to as /N or divide by n clocking.

High-Resolution Clocking Mode

High-Resolution clocking allows you to set the Sample clock frequency to any value from zero to the device Sample clock timebase frequency with a very fine resolution typically in the millihertz or microhertz range. This mode is useful for applications that require a precise clock source, which is not possible using the Divide-Down clocking scheme.

Automatic Clocking Mode

In Automatic clocking mode, NI-FGEN switches between Divide-Down and the High-Resolution clocking modes depending on the sample rate configured with the Sample Rate property or the NIFGEN_ATTR_ARB_SAMPLE_RATE attribute.

Parent topic:

Waveform Fundamentals

<!--NI_TOPIC bundle=ni-fgen path=closing-the-session.html language=enus -->
## TOPIC 00012: Closing the Session

- bundle_id: `ni-fgen`
- source_path: `closing-the-session.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/closing-the-session.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The closing step closes the session and deallocates any resources the session used. Closing the session is important because it releases any temporary buffers that were created to transfer data between the digitizer and the host memory. LabVIEW Example Call the niFgen Close VI to close the session.

### Closing the Session

The closing step closes the session and deallocates
any resources the session used. Closing the session is important
because it releases any temporary buffers that were created to
transfer data between the digitizer and the host memory.

#### LabVIEW Example

Call the 
niFgen Close VI to
close the session.

#### C Example

Call the 
niFgen_Close function to close the session.

Parent topic:

NI-FGEN Tutorial

<!--NI_TOPIC bundle=ni-fgen path=color-coding.html language=enus -->
## TOPIC 00013: Color Coding

- bundle_id: `ni-fgen`
- source_path: `color-coding.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/color-coding.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The color information signal C that, together with Y, forms the composite video signal is a modulated signal. The modulation type depends on the video format. For all PAL and NTSC formats, the coding is based on the quadrature-amplitude modulation (QAM) concept, where 2-color components are amplitud

### Color Coding

The color information signal C that, together with Y, forms the composite video signal is a modulated signal. The modulation type depends on the video format.

For all PAL and NTSC formats, the coding is based on the quadrature-amplitude modulation (QAM) concept, where 2-color components are amplitude modulated in quadrature and then combined. The modulation must be decoded, so to keep track of the absolute phase needed to decode the color information, a reference signal, called the color burst, is inserted at the beginning of each line, right after the horizontal synchronization pulse. The insertion signal is shown in the *Complete NTSC Frame Scan* image.

For the SECAM format, the 2-color components are frequency modulated using two different subcarrier frequencies and are sequentially distributed on alternated video lines. SECAM does not need a color burst signal.

Parent topic:

Video Signal Fundamentals

Related concepts:

- Complete NTSC Frame Scan

<!--NI_TOPIC bundle=ni-fgen path=complete-ntsc-frame-scan.html language=enus -->
## TOPIC 00014: Complete NTSC Frame Scan

- bundle_id: `ni-fgen`
- source_path: `complete-ntsc-frame-scan.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/complete-ntsc-frame-scan.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the result of scanning all 525 lines that compose a complete NTSC frame.

### Complete NTSC Frame Scan

The following figure shows the result of scanning all 525 lines that compose a complete NTSC frame.

[IMAGE alt='image' src='GUID-DE557A8D-63F3-4F75-8112-2BF5AAE7FF33-a5.gif']

Parent topic:

Interlaced Scanning

<!--NI_TOPIC bundle=ni-fgen path=configuration.html language=enus -->
## TOPIC 00015: Configuration

- bundle_id: `ni-fgen`
- source_path: `configuration.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/configuration.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Once you have opened a session to your signal generator, you need to configure the session to generate the signals you desire for your application. If you are using a multichannel device, you must configure channels immediately after initializing and before configuring any other feature of the devic

### Configuration

standard waveform

arbitrary waveform

arbitrary
sequence

frequency list

script

Features Supported

Note

Features

Parent topic:

NI-FGEN Tutorial

Related concepts:

- Configure Standard Function Mode
- Configure Arbitrary Waveform Mode
- Configure Arbitrary Sequence Mode
- Configure Frequency List Mode
- Configure Script Mode
- Features Supported on SMC Devices
- Features

<!--NI_TOPIC bundle=ni-fgen path=configure-arbitrary-sequence-mode.html language=enus -->
## TOPIC 00016: Configure Arbitrary Sequence Mode

- bundle_id: `ni-fgen`
- source_path: `configure-arbitrary-sequence-mode.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/configure-arbitrary-sequence-mode.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use Arbitrary Sequence mode to load multiple waveforms in the onboard memory of the signal generator. LabVIEW Example The procedure below provides the basic steps required to configure Arbitrary Sequence mode. For more detailed examples of the use of Arbitrary Sequence mode in LabVIEW, refer

### Configure Arbitrary Sequence Mode

You can use 
*Arbitrary Sequence*
mode to load multiple waveforms in the onboard memory of the signal
generator.

#### LabVIEW Example

The procedure below provides the basic steps
required to configure Arbitrary Sequence mode. For more detailed
examples of the use of Arbitrary Sequence mode in LabVIEW, refer to
the Fgen Basic Arb Sequence.vi or the Fgen Arbitrary Sequence.vi
examples for LabVIEW.

1. Call the 
niFgen
Configure Output Mode VI with 
 Output Mode set to Arbitrary Waveform.
2. (Optional) Call the 
niFgen
Clear Arbitrary Memory VI to clear any previously created
arbitrary waveforms, sequences, and scripts from the signal
generator memory.

Choose one of the following two options for creating your
arbitrary sequence:

Option 1—Allow NI-FGEN to configure the size
and allocated space of your waveform.

1. Call the 
niFgen
Create Waveform (poly) VI. This VI creates a waveform the size
of the data you provide.
2. Call the 
niFgen
Create Arbitrary Sequence VI or the 
niFgen
Create Advanced Arb Sequence VI.
3. Call the 
niFgen
Configure Arbitrary Sequence VI to configure the gain and
offset of the sequence of waveforms.

Option 2—Manually configure the size and
allocated space of your waveform.

1. Call the 
niFgen
Allocate Waveform VI to specify the size of the waveform to
allocate in the onboard memory of the signal generator
2. Call the 
niFgen
Write Waveform (poly) VI to write waveform data to the onboard
memory you allocated in step 3.
3. Call the 
niFgen
Create Arbitrary Sequence VI or the 
niFgen
Create Advanced Arb Sequence VI.
4. Call the 
niFgen
Configure Arbitrary Sequence VI to configure the gain and
offset of the sequence of waveforms.

#### C Example

The procedure below provides the basic steps
required to configure Arbitrary Waveform mode. For a more detailed
example of the use of Arbitrary Sequence mode in C, refer to the
BasicArbitrarySequence or the ArbitrarySequence examples for
CVI.

1. Call the 
 niFgen_ConfigureOutputMode function with 
 outputMode to 
 NIFGEN_VAL_OUTPUT_SEQ .
2. (Optional) Call the 
 niFgen_ClearArbMemory function to clear any previously created arbitrary waveforms,
sequences, and scripts from the signal generator memory.
3. Call one of the niFgen Create Waveform functions ( niFgen_CreateWaveformF64 , 
 niFgen_CreateWaveformI16 , 
 niFgen_CreateWaveformComplexF64 , or
 niFgen_CreateWaveformFromFileI16 ). The function you choose creates a waveform the size and
type of the data you choose.
4. Call the 
 niFgen_CreateArbSequence function or the 
 niFgen_CreateAdvancedArbSequence function.
5. Call the 
 niFgen_ConfigureArbSequence function to configure the gain and offset of the
waveform.

Parent topic:

Configure Output Mode

Related concepts:

- Arbitrary Sequence Mode

<!--NI_TOPIC bundle=ni-fgen path=configure-arbitrary-waveform-mode.html language=enus -->
## TOPIC 00017: Configure Arbitrary Waveform Mode

- bundle_id: `ni-fgen`
- source_path: `configure-arbitrary-waveform-mode.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/configure-arbitrary-waveform-mode.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use Arbitrary Waveform mode to generate waveforms from user–created or user–provided waveform arrays of numeric data. LabVIEW Example The procedure below provides the basic steps required to configure Arbitrary Waveform mode. For a more detailed example of the use of Arbitrary Waveform mode

### Configure Arbitrary Waveform Mode

You can use 
*Arbitrary Waveform* mode to generate
waveforms from user–created or user–provided waveform
arrays of numeric data.

#### LabVIEW Example

The procedure below provides the basic steps
required to configure Arbitrary Waveform mode. For a more detailed
example of the use of Arbitrary Waveform mode in LabVIEW, refer to
the Fgen Basic Arb Waveform.vi or the Fgen Arbitrary Waveform.vi
examples for LabVIEW.

1. Call the 
niFgen
Configure Output Mode VI with 
 Output Mode set to Arbitrary Waveform.
2. (Optional) Call the 
niFgen
Clear Arbitrary Memory VI. This clears any previously created
arbitrary waveforms, sequences, and scripts from the signal
generator memory.

Choose one of the following two options for creating your
arbitrary waveform:

Option 1—Allow NI-FGEN to configure the size
and allocated space of your waveform.

1. Call the 
niFgen
Create Waveform (poly) VI. This VI creates a waveform the size
of the data you provide.
2. Call the 
niFgen
Configure Arbitrary Waveform VI to configure the gain and
offset of the waveform.

Option 2—Manually configure the size and
allocated space of your waveform.

1. Call the 
niFgen
Allocate Waveform VI to specify the size of the waveform to
allocate in the onboard memory of the signal generator.
2. Call the 
niFgen
Write Waveform (poly) VI to write waveform data to the onboard
memory you allocated in step 3.
3. Call the 
niFgen
Configure Arbitrary Waveform VI to configure the gain and
offset of the waveform.

#### C Example

The procedure below provides the basic steps
required to configure Arbitrary Waveform mode. For a more detailed
example of the use of Arbitrary Waveform mode in C, refer to the
BasicArbitraryWaveform or the ArbitraryWaveform examples for
CVI.

1. Call the 
 niFgen_ConfigureOutputMode function with the 
 outputMode parameter to 
 NIFGEN_VAL_OUTPUT_ARB .
2. (Optional) Call the 
 niFgen_ClearArbWaveform function. This clears any previously created arbitrary
waveforms from the signal generator memory.
3. Call one of the niFgen Create Waveform functions ( niFgen_CreateWaveformF64 , 
 niFgen_CreateWaveformI16 , 
 niFgen_CreateWaveformComplexF64 , or
 niFgen_CreateWaveformFromFileI16 ). The function you choose creates a waveform the size and
type of the data you choose.
4. Call the 
 niFgen_ConfigureArbWaveform function to configure the gain and offset of the
waveform.

Parent topic:

Configure Output Mode

Related concepts:

- Arbitrary Waveform Output Mode

<!--NI_TOPIC bundle=ni-fgen path=configure-channels.html language=enus -->
## TOPIC 00018: Configure Channels

- bundle_id: `ni-fgen`
- source_path: `configure-channels.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/configure-channels.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: If you want to configure a multichannel signal generator to generate data on more than one channel, you must configure the channels to be used. If you are not using a multichannel signal generator or if you are only concerned with data generated on one channel of a multichannel signal generator, y

### Configure Channels

Note

#### LabVIEW Example

Call the 
niFgen
Configure Channels VI with 
Channels set to the channel or channels you want
to configure. Valid values are non-negative integers. For example,
0 is the only valid value on devices with one channel, while
devices with two channels support values of 0 and 1. You can
specify more than one channel by inserting commas between values
(for example, "0,1").

#### C Example

Call the 
niFgen_ConfigureChannels function with 
channels set to the channel or channels you want
to configure. Valid values are non-negative integers. For example,
0 is the only valid value on devices with one channel, while
devices with two channels support values of 0 and 1. You can
specify more than one channel by inserting commas between values
(for example, "0,1").

Parent topic:

Configuration

<!--NI_TOPIC bundle=ni-fgen path=configure-frequency-list-mode.html language=enus -->
## TOPIC 00019: Configure Frequency List Mode

- bundle_id: `ni-fgen`
- source_path: `configure-frequency-list-mode.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/configure-frequency-list-mode.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use Frequency List mode to generate a standard function using a list of frequencies you define. LabVIEW Example The procedure below provides the basic steps required to configure Frequency List mode. For an example of the use of Frequency List mode in LabVIEW, refer to the Fgen Sweep Generat

### Configure Frequency List Mode

You can use 
*Frequency List* mode to
generate a standard function using a list of frequencies you
define.

#### LabVIEW Example

The procedure below provides the basic steps
required to configure Frequency List mode. For an example of the
use of Frequency List mode in LabVIEW, refer to the Fgen Sweep
Generator.vi example.

1. Call the 
niFgen
Configure Output Mode VI with 
 Output Mode set to Frequency List.
2. (Optional) Call the 
niFgen
Clear Frequency List VI to remove any previously created
frequency lists from the signal generator memory.
3. Call the 
niFgen
Create Frequency List VI to set the function type, the
frequency list, and the duration of each step in the list..
4. Call the 
niFgen
Configure Frequency List VI to select the active frequency list
and configure the amplitude, DC offset, and start phase of the
generation.

#### C Example

The procedure below provides the basic steps
required to configure Frequency List mode. For an example of the
use of Frequency List mode in C, refer to the Fgen Sweep
SweepGenerator example for CVI.

1. Call the 
 niFgen_ConfigureOutputMode function with 
 outputMode set to 
 NIFGEN_VAL_OUTPUT_FREQ_LIST .
2. (Optional) Call the 
 niFgen_ClearFreqList function to remove a previously created frequency lists from
the signal generator memory.
3. Call the 
 niFgen_CreateFreqList function to set the function type, the frequency list, and the
duration of each step in the list..
4. Call the 
 niFgen_ConfigureFreqList function to select the active frequency list and configure the
amplitude, DC offset, and start phase of the generation.

Parent topic:

Configure Output Mode

Related concepts:

- Frequency List Mode

<!--NI_TOPIC bundle=ni-fgen path=configure-output-mode.html language=enus -->
## TOPIC 00020: Configure Output Mode

- bundle_id: `ni-fgen`
- source_path: `configure-output-mode.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/configure-output-mode.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Configure Output Mode step determines the type of waveforms that will be generated by your device. Options include standard waveforms, arbitrary waveforms, arbitrary sequences, frequency lists, and scripts. Refer to the Features Supported topic for your device for more information about the type

### Configure Output Mode

The Configure Output Mode step determines the type
of waveforms that will be generated by your device. Options include *standard
waveforms*, *arbitrary waveforms*, 
*arbitrary sequences*, 
*frequency lists*, and 
*scripts*. Refer to the 
*Features Supported* topic for
your device for more information about the type of output modes it
supports.

Parent topic:

Configuration

Related concepts:

- Configure Standard Function Mode
- Configure Arbitrary Waveform Mode
- Configure Arbitrary Sequence Mode
- Configure Frequency List Mode
- Configure Script Mode
- Devices

<!--NI_TOPIC bundle=ni-fgen path=configure-script-mode.html language=enus -->
## TOPIC 00021: Configure Script Mode

- bundle_id: `ni-fgen`
- source_path: `configure-script-mode.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/configure-script-mode.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use Script mode to use scripting to link and loop multiple waveforms in complex combinations using a script. LabVIEW Example The procedure below provides the basic steps required to configure Script mode. To see a more detailed example of the use of Script mode in LabVIEW, refer to the Fgen

### Configure Script Mode

You can use 
*Script mode* to use scripting to link
and loop multiple waveforms in complex combinations using a
script.

#### LabVIEW Example

The procedure below provides the basic steps
required to configure Script mode. To see a more detailed example
of the use of Script mode in LabVIEW, refer to the Fgen Arb
Script.vi example for LabVIEW.

1. Call the 
niFgen
Configure Output Mode VI with 
 Output Mode set to Script.
2. Write all waveforms that are referenced in the script by
calling the 
niFgen
Write Named Waveform VI and associate the proper names to
them.
3. After your waveforms are written to your device, call the 
niFgen Write
Script VI to write the script(s) containing the generation
instructions to be executed.
 The script you write can manage waveform
generation based on multiple waveforms and triggers. For example,
you could download waveforms A, B, C, and D into device memory. You
could then write a script that would wait for a trigger to initiate
generation and, upon receiving this trigger, generate waveform A
three times with a marker at position 16 each time and finally
generate waveforms B, C, and D twice (BCDBCD). The following is the
script of this example: 
 script myFirstScript 
 wait until scriptTrigger0 
 repeat 3 
 generate waveformA marker0(16) 
 end repeat 
 repeat 2 
 generate waveformB 
 generate waveformC 
 generate waveformD 
 end repeat 
 end script
4. (Optional) You can write multiple scripts that exist
simultaneously on your device. If you write multiple scripts to
your device, you must select the one you wish to execute by setting
the 
Script to
Generate property.

#### C Example

The procedure below provides the basic steps
required to configure Script mode. To see a more detailed example
of the use of Script mode in C, refer to the ArbitraryScript
example for CVI.

1. Call the 
 niFgen_configureOutputMode function with 
 outputMode set to 
 NIFGEN_VAL_OUTPUT_FUNC .
2. Write all waveforms that are referenced in the script by
calling the one of the niFgen Write Named Waveform functions ( niFgen_WriteNamedWaveformF64 , 
 niFgen_WriteNamedWaveformI16 , 
 niFgen_WriteNamedWaveformComplexF64 , 
 niFgen_WriteNamedWaveformComplexI16 ) and associate the proper names to them.
3. After your waveforms are written to your device, call the 
 niFgen_WriteScript function to write the script(s) containing the generation
instructions to be executed.
 The script you write can manage waveform
generation based on multiple waveforms and triggers. For example,
you could download waveforms A, B, C, and D into device memory. You
could then write a script that would wait for a trigger to initiate
generation and, upon receiving this trigger, generate waveform A
three times with a marker at position 16 each time and finally
generate waveforms B, C, and D twice (BCDBCD). The following is the
script of this example: 
 script myFirstScript 
 wait until scriptTrigger0 
 repeat 3 
 generate waveformA marker0(16) 
 end repeat 
 repeat 2 
 generate waveformB 
 generate waveformC 
 generate waveformD 
 end repeat 
 end script
4. (Optional) You can write multiple scripts that exist
simultaneously on your device. If you write multiple scripts to
your device, you must select the one you wish to execute by setting
the 
 NIFGEN_ATTR_SCRIPT_TO_GENERATE attribute.

Parent topic:

Configure Output Mode

Related concepts:

- Script Mode

<!--NI_TOPIC bundle=ni-fgen path=configure-standard-function-mode.html language=enus -->
## TOPIC 00022: Configure Standard Function Mode

- bundle_id: `ni-fgen`
- source_path: `configure-standard-function-mode.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/configure-standard-function-mode.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Standard Function output mode allows you to generate standard function waveforms such as sine, square, triangle, etc. LabVIEW Example The procedure below provides the basic steps required to configure Standard Function mode. For a more detailed example of the use of Standard Function mode in LabVIEW

### Configure Standard Function Mode

*Standard Function*
output mode allows you to generate standard function waveforms such
as sine, square, triangle, etc.

#### LabVIEW Example

The procedure below provides the basic steps
required to configure Standard Function mode. For a more detailed
example of the use of Standard Function mode in LabVIEW, refer to
the Fgen Basic Standard Function.vi example for LabVIEW.

1. Call the 
niFgen
Configure Output Mode VI. Set 
 Output Mode to Standard Function.
2. Choose the type of waveform you would like to generate and set
the 
 Waveform parameter of the 
niFgen
Configure Standard Waveform VI to the waveform you have
chosen.

#### C Example

The procedure below provides the basic steps
required to configure Standard Function mode. For a more detailed
example of the use of Standard Function mode in C, refer to the
BasicStandardFunction example for CVI.

1. Call the 
 niFgen_configureOutputMode function. Set 
 outputMode to 
 NIFGEN_VAL_OUTPUT_FUNC .
2. Choose the type of waveform you would like to generate and set
the 
 waveform parameter of the 
 niFgen_configureStandardWaveform function to the waveform you have chosen.

Parent topic:

Configure Output Mode

Related concepts:

- Standard Function Mode

<!--NI_TOPIC bundle=ni-fgen path=configuring-a-peer-to-peer-endpoint.html language=enus -->
## TOPIC 00023: Configuring a Peer-to-Peer Endpoint

- bundle_id: `ni-fgen`
- source_path: `configuring-a-peer-to-peer-endpoint.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/configuring-a-peer-to-peer-endpoint.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Any NI-FGEN property that is associated with an instance of an endpoint is an endpoint-based property; much like the Gain property is channel-based because it is associated with a specific channel number. The syntax FIFOEndpointN is used to tell NI-FGEN which signal generator endpoint is being speci

### Configuring a Peer-to-Peer Endpoint

Any NI-FGEN property that is associated with an instance of an endpoint is an endpoint-based property; much like the Gain property is channel-based because it is associated with a specific channel number. The syntax FIFOEndpointN is used to tell NI-FGEN which signal generator endpoint is being specified, where N is an integer starting with 0. If the signal generator supports multiple endpoints, the first is FIFOEndpoint0, the second is FIFOEndpoint1, and so on. Set the Active Channel property using this string when configuring endpoint-based properties. To determine how many endpoints your signal generator supports, query the Endpoint Count property. Use the Destination Channels property to specify which channel(s) receives the endpoint data.

The following table shows possible values for a dual-channel signal generator.

| FIFOEndpointN Destination Channels | Channel List |
| --- | --- |
| Channel 0 | 0 |
| Channel 1 | 1 |
| Channel 0 and Channel 1 (interleaved) | 0, 1 |

For devices that support multiple endpoints, physical channels cannot be contained within the destination channels for multiple endpoints.

To use NI-P2P in NI-FGEN, configure the signal generator to use *Script* output mode. Use the script command stream n, where n is an integer number of samples to stream from an endpoint to the channels specified by the Destination Channels property.

The following figure shows an NI-FGEN session configured to stream 10,240 samples received at FIFO endpoint 0 to channel 0.

[IMAGE alt='image' src='GUID-641CDB25-58FB-4229-B016-E6CCEC28B199-a5.gif']

To stream continuously until the generation is aborted from the host or by a peer, create a script that nests the stream n command in a repeat forever loop, as shown in the following script code. Refer to *Stopping a Peer-to-Peer Generation* for information about stopping this generation.

Script myScript    repeat forever      stream 10240    end repeatend script

Parent topic:

Peer-to-Peer Data Streaming

Related concepts:

- Configure Script Mode
- Stopping a Peer-to-Peer Generation

<!--NI_TOPIC bundle=ni-fgen path=configuring-a-peer-to-peer-stream.html language=enus -->
## TOPIC 00024: Configuring a Peer-to-Peer Stream

- bundle_id: `ni-fgen`
- source_path: `configuring-a-peer-to-peer-stream.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/configuring-a-peer-to-peer-stream.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: To configure a peer-to-peer stream using the NI-P2P API, a writer and reader handle for each endpoint are required. Use the niFgen Get Stream Endpoint Handle VI or the niFgen_GetStreamEndpointHandle function to get a reader endpoint handle. Refer to the Peer-to-Peer Streaming Help for more informati

### Configuring a Peer-to-Peer Stream

To configure a peer-to-peer stream using the NI-P2P API, a writer and reader handle for each endpoint are required. 
Use the niFgen Get Stream Endpoint Handle VI or the niFgen_GetStreamEndpointHandle function to get a reader endpoint handle. Refer to the Peer-to-Peer Streaming Help for more information about creating and monitoring peer-to-peer streams.

Parent topic:

Peer-to-Peer Data Streaming

<!--NI_TOPIC bundle=ni-fgen path=configuring-a-reference-clock.html language=enus -->
## TOPIC 00025: Configuring a Reference Clock

- bundle_id: `ni-fgen`
- source_path: `configuring-a-reference-clock.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/configuring-a-reference-clock.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can specify the source for the Reference clock that will be used in a phase-locked loop to tune the Sample clock timebase to the frequency stability of the Reference clock. LabVIEW Example Call the niFgen Configure Reference Clock VI with Source set to the Reference clock source. For example, se

### Configuring a Reference Clock

You can specify the source for the Reference clock
that will be used in a phase-locked loop to tune the Sample clock
timebase to the frequency stability of the Reference clock.

#### LabVIEW Example

Call the 
niFgen
Configure Reference Clock VI with 
Source set to the Reference clock source. For
example, set 
Source to "ClkIn" to obtain the Reference clock
signal from the Clk In front panel connector. Set 
Reference Clock Frequency to the frequency of the
Reference clock.

#### C Example

Call the 
niFgen_configureReferenceClock function with the 
referenceClockSource parameter set to the
Reference clock source. For example, set the 
referenceClockSource parameter to "ClkIn" to
obtain the Reference clock signal from the Clk In front panel
connector. Set 
referenceClockFrequency to the frequency of the
Reference clock.

Parent topic:

Features

<!--NI_TOPIC bundle=ni-fgen path=configuring-an-application-for-streaming.html language=enus -->
## TOPIC 00026: Configuring an Application for Streaming

- bundle_id: `ni-fgen`
- source_path: `configuring-an-application-for-streaming.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/configuring-an-application-for-streaming.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following instructions are a guide for configuring your application for streaming. For a more detailed programmatic example, refer to Fgen Arb Waveform Streaming.vi for LabVIEW or ArbitraryWaveformStreaming.prj for LabWindows/CVI. LabVIEW Example The procedure below provides the basic steps requ

### Configuring an Application for Streaming

The following instructions are a guide for
configuring your application for 
*streaming*. For a more detailed
programmatic example, refer to
Fgen Arb Waveform Streaming.vi for LabVIEW or
ArbitraryWaveformStreaming.prj for LabWindows/CVI.

#### LabVIEW Example

The procedure below provides the basic steps
required to configure streaming. For a more detailed example of the
use of streaming in LabVIEW, refer to the
Fgen Arb Waveform Streaming.vi example for
LabVIEW.

1. Call the 
niFgen
Allocate Waveform VI to specify the amount of onboard memory to
reserve for streaming.
2. Set the 
Streaming
Waveform Handle property to the waveform handle returned in
Step 1.
3. Call the 
niFgen
Write Waveform VI to write the first part of the waveform data
to the streaming waveform in onboard memory.

 Tip 

 
 When transferring large blocks of
waveform data, break the data into smaller blocks and call the
niFgen Write Waveform VI multiple times. The data is appended
sequentially. A computer can allocate smaller blocks of a large
waveform faster than allocating a single large contiguous block in
memory. Depending on the amount of RAM on the computer,
transferring ten 16 MB blocks may be faster than transferring one
160 MB block. 
 Tip 

 
 NI-FGEN requires the quotient of
the waveform size divided by the data transfer block size to be an
integer value. If the waveform size is not an integer multiple of
the block size, change either the waveform size or the block size.
A fractional number of data blocks in the waveform returns an error
message.
4. Call the 
niFgen
Initiate Generation VI to begin the waveform generation.
5. Call the 
niFgen
Write Waveform VI to write a new block of waveform data to the
streaming waveform in onboard memory.
6. Repeat step 5 until all waveform data is written.

#### C Example

The procedure below provides the basic steps
required to configure streaming. For a more detailed example of the
use of streaming in C, refer to the ArbitraryWaveformStreaming.prj
example for CVI.

1. Call the 
 niFgen_AllocateWaveform function to specify the amount of onboard memory to reserve
for streaming.
2. Set the 
 NIFGEN_ATTR_STREAMING_WAVEFORM_HANDLE attribute to the waveform handle returned in Step 1.
3. Call the 
 niFgen_WriteWaveform function to write the first part of the waveform data to the
streaming waveform in onboard memory.

 Tip 

 
 When transferring large blocks of
waveform data, break the data into smaller blocks and call the 
niFgen_WriteWaveform function
multiple times. The data is appended sequentially. A computer can
allocate smaller blocks of a large waveform faster than allocating
a single large contiguous block in memory. Depending on the amount
of RAM on the computer, transferring ten 16 MB blocks may be faster
than transferring one 160 MB block. 
 Tip 

 
 NI-FGEN requires the quotient of
the waveform size divided by the data transfer block size to be an
integer value. If the waveform size is not an integer multiple of
the block size, change either the waveform size or the block size.
A fractional number of data blocks in the waveform returns an error
message.
4. Call the 
 niFgen_InitiateGeneration function to begin the waveform generation.
5. Call the 
 niFgen_WriteWaveform function to write a new block of waveform data to the streaming waveform in onboard memory.
6. Repeat step 5 until all waveform data is written.

Parent topic:

Features

Related concepts:

- Streaming

<!--NI_TOPIC bundle=ni-fgen path=configuring-an-external-sample-clock.html language=enus -->
## TOPIC 00027: Configuring an External Sample Clock

- bundle_id: `ni-fgen`
- source_path: `configuring-an-external-sample-clock.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/configuring-an-external-sample-clock.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Some NI signal generators can accept an external clock to directly drive the Sample clock. When using an external Sample clock, the frequency stability and accuracy of the Sample clock is determined by the external Sample clock provided. LabVIEW Example Call the niFgen Configure Sample Clock Source

### Configuring an External Sample Clock

Some NI signal generators can accept an external
clock to directly drive the Sample clock. When using an external
Sample clock, the frequency stability and accuracy of the Sample
clock is determined by the external Sample clock provided.

#### LabVIEW Example

1. Call the 
niFgen
Configure Sample Clock Source VI with the 
 Source set to an external location.

Perform the following step if your application is
configured for Arbitrary Waveform, Arbitrary Sequence, or Script
output mode:

1. Call the 
niFgen Set
Sample Rate VI with the 
 Sample Rate set to the frequency of the external
device you are using as a clock source.

#### C Example

1. Call the 
 niFgen_ConfigureSampleClockSource function with the 
 sampleClockSource parameter set to an external
location.

Perform the following step if your application is
configured for Arbitrary Waveform, Arbitrary Sequence, or Script
output mode:

1. Call the 
 niFgen_ConfigureSampleRate function with the 
 sampleRate parameter set to the frequency of the
external device you are using as a clock source.

Parent topic:

Features

<!--NI_TOPIC bundle=ni-fgen path=configuring-an-internal-sample-clock.html language=enus -->
## TOPIC 00028: Configuring an Internal Sample Clock

- bundle_id: `ni-fgen`
- source_path: `configuring-an-internal-sample-clock.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/configuring-an-internal-sample-clock.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use the internal (onboard) Sample clock to control the clocking rates of your signal generator. In Arbitrary Waveform or Arbitrary Sequence mode, you can choose a clocking mode that will allow you to configure the rate at which this Sample clock runs. The onboard clock is the default Sampl

### Configuring an Internal Sample Clock

Note

#### LabVIEW Example

1. Call the 
niFgen
Configure Sample Clock Source VI with 
 Source set to "Onboard Clock".

Perform the following step only if your application
is configured for Arbitrary Waveform or Arbitrary Sequence output
mode:

1. Call the 
niFgen
Configure Clock Mode VI with 
 Clock Mode set to the clock mode required for your
application.

#### C Example

1. Call the 
 niFgen_ConfigureSampleClockSource function with the 
 sampleClockSource parameter set to
"OnboardClock".

Perform the following step only if your application
is configured for Arbitrary Waveform or Arbitrary Sequence output
mode:

1. Call the 
 niFgen_ConfigureClockMode function with the 
 clockMode parameter set to the clock mode required
for your application.

Parent topic:

Features

<!--NI_TOPIC bundle=ni-fgen path=configuring-independent-channel-waveform-gene.html language=enus -->
## TOPIC 00029: Configuring Independent-Channel Waveform Generation

- bundle_id: `ni-fgen`
- source_path: `configuring-independent-channel-waveform-gene.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/configuring-independent-channel-waveform-gene.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Multichannel waveform generators that support independent channels can be configured for multiple channel-based sessions or multichannel sessions. Some settings are only instrument-based, as opposed to channel-based. With the PXIe-5413/5423/5433, you can open multiple sessions with the same device

### Configuring Independent-Channel Waveform Generation

Note

With the PXIe-5413/5423/5433, you can open multiple sessions with the same device. This
 feature allows you to use each channel as an independent device. The following behaviors apply
 to the PXIe-5413/5423/5433:

- To output signals on multiple channels at the same time, you must create a separate
 independent session for each channel.
- You can still create multi-channel sessions. However, the PXIe-5413/5423/5433 do not allow
 writing a waveform to a single channel when in multi-channel mode. To work around this,
 consider the following options:
  - Write interleaved data for each of the channels, effectively generating a different
 waveform on each channel.
  - Create an independent session for each channel and output a different signal in each
 session.
- If a session is running a calibration procedure, no other sessions on the device can
 generate a waveform until the calibration is complete. Even though independent sessions can
 be created on the PXIe-5413/5423/5433 for each channel, the device cannot be calibrated on a
 channel-by-channel basis. Because of this, when a calibration procedure is running, no
 channels can generate signals.
- Performing a device reset on one session aborts waveform generation on all other
 sessions.

#### Configuring Multiple Channel-Based Sessions

1. Set the Channel Name parameters of two instances of the niFgen Initialize With Channels VI or niFgen_InitializeWithChannels function to different channels.
2. (Optional) If you use the Channel Name parameter in subsequent VI or function calls, set it to the same channel as specified with the niFgen Initialize With Channels VI or niFgen_InitializeWithChannels function.

All sessions open to the same waveform generator must use the same Reference Clock source and same setting for the auxiliary power pin (enabled/disabled).

Note

#### Configuring Multichannel Sessions

1. Call any niFgen Initialize VI or function. niFgen Initialize VIs and functions use all channels on multichannel waveform generators by default.
 Alternatively, you can specify multiple channels using the Channel Name parameter of the 
 niFgen Initialize With Channels VI or niFgen_InitializeWithChannels function or the Option String parameter of any
Initialize VI or function.
2. Provide interleaved data with either the niFgen Create Waveform VI or niFgen_CreateWaveform functions, the niFgen Write Waveform VI or niFgen_WriteWaveform functions, or the niFgen Write Named Waveform VI or niFgen_WriteNamedWaveform functions.

Parent topic:

Features

Related concepts:

- Initialize

<!--NI_TOPIC bundle=ni-fgen path=configuring-multichannel-i-q-signal-generator.html language=enus -->
## TOPIC 00030: Configuring Multichannel I/Q Signal Generators using Channel Name

- bundle_id: `ni-fgen`
- source_path: `configuring-multichannel-i-q-signal-generator.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/configuring-multichannel-i-q-signal-generator.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: To use onboard signal processing on supported devices, you must configure CH 0 by calling the niFgen Configure Channels VI or the niFgen_ConfigureChannels function and set the OSP Enabled property or the NIFGEN_ATTR_OSP_ENABLED attribute to True. You can use the Active Channel property or the channe

### Configuring Multichannel I/Q Signal Generators using Channel Name

To use onboard signal processing on supported devices, you must configure CH 0 by calling the niFgen Configure Channels VI or the niFgen_ConfigureChannels function and set the OSP Enabled property or the NIFGEN_ATTR_OSP_ENABLED attribute to True.

You can use the Active Channel property or the channel name parameter in the following ways:

1. When the Data
Processing Mode property or the 
 NIFGEN_ATTR_OSP_DATA_PROCESSING_MODE attribute is set to Real , you can only set the channel name to "I" . Setting the channel name as "" or "0" is equivalent to setting it to "I" .
2. When the Data Processing Mode property or the NIFGEN_ATTR_OSP_DATA_PROCESSING_MODE attribute is set to Complex , the channel name can be set to "I" or "Q" . Setting the channel name to "" or "0" is equivalent to setting it to "I, Q" .

The rules above also apply when using the channel name parameter for niFgen Create Waveform VIs and functions or niFgen Write Waveform VIs and functions. 
When the Data Processing Mode property or the NIFGEN_ATTR_OSP_DATA_PROCESSING_MODE attribute is set to Complex, you can write waveform data in the following ways:

1. Using a complex datatype, call the corresponding niFgen Create Waveform (Complex DBL) VI or the niFgen_CreateWaveformComplexF64 function.
2. Interleave the I and Q data together and call the niFgen Create Waveform (I16) VI or the niFgen Create Waveform (DBL) VI or the niFgen_CreateWaveformI16 function or the niFgen_CreateWaveformF64 function.
3. Write the data separately. Do this by specifying the channel name, "I" or "Q" , using the niFgen Write Binary 16 WaveformVI or the niFgen Write Waveform (DBL) VI or niFgen_WriteBinary16Waveform function or the niFgen_WriteWaveform function.

Parent topic:

Features

Related concepts:

- NI 5450 Interleaved Waveform Data

<!--NI_TOPIC bundle=ni-fgen path=configuring-triggers.html language=enus -->
## TOPIC 00031: Configuring Triggers

- bundle_id: `ni-fgen`
- source_path: `configuring-triggers.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/configuring-triggers.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Triggers are signals that cause the NI device to perform an action such as starting or stopping a generation operation. Triggers can be internal (software-generated) or external. External digital triggers can be several different types. When triggering your NI signal generator in Standard Function,

### Configuring Triggers

Triggers are signals that cause the NI device to
perform an action such as starting or stopping a generation
operation. Triggers can be internal (software-generated) or
external. External digital triggers can be several different 
*types*. When triggering your NI
signal generator in Standard Function, Arbitrary Waveform,
Arbitrary Sequence, Script, or Frequency List mode, you can select
the type of trigger, the trigger source, and the trigger mode that
you want to use.

#### LabVIEW Example

1. Call the 
niFgen
Configure Trigger Mode VI to select the trigger mode in which
your trigger will generate. This mode affects the behavior of the
trigger and is dependant on the output mode of the signal
generator.
2. Call the 
niFgen
Configure Trigger poly VI. Choose the instance of the VI that
corresponds to the type of trigger you wish to use.

#### C Example

1. Call the 
 niFgen_configureTriggerMode function to select the trigger mode in which your trigger will
generate. This mode affects the behavior of the trigger and is
dependant on the output mode of the signal generator.
2. Call one of the following niFgen Configure Trigger functions:
 niFgen_ConfigureDigitalEdgeStartTrigger , 
 
 niFgen_ConfigureSoftwareEdgeStartTrigger , 
 
 niFgen_ConfigureDigitalEdgeScriptTrigger , 
 
 niFgen_ConfigureDigitalLevelScriptTrigger , 
 
 niFgen_ConfigureSoftwareEdgeScriptTrigger

Parent topic:

Features

Related concepts:

- Types of Triggers

<!--NI_TOPIC bundle=ni-fgen path=configuring-your-application-for-direct-dma.html language=enus -->
## TOPIC 00032: Configuring Your Application for Direct DMA

- bundle_id: `ni-fgen`
- source_path: `configuring-your-application-for-direct-dma.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/configuring-your-application-for-direct-dma.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can achieve high rates of data transfer to the onboard memory by configuring your device for Direct DMA. Direct DMA establishes a direct connection between the signal generator onboard memory and a specialized waveform data source. The following instructions are a guide for configuring your appl

### Configuring Your Application for Direct DMA

You can achieve high rates of data transfer to the onboard memory by configuring your device for *Direct DMA*. Direct DMA establishes a direct connection between the signal generator onboard memory and a specialized waveform data source.

The following instructions are a guide for configuring your application for direct DMA.

#### LabVIEW Example

1. Enable the signal generator for direct DMA writes by setting the Direct DMA Enabled property. Once enabled, NI-FGEN monitors and reports any issues with the direct DMA transfer.
2. Identify the waveform data source and set the Direct DMA Window Address property to the address provided by your direct DMA-compatible data source.
3. Set the Direct DMA Window Size property to the size of the memory window provided by your direct DMA-compatible data source.
4. Use the niFgen Write Waveform (Direct DMA I16) VI to write blocks of data to the signal generator. For each block of data written to the signal generator, you provide the address of the direct DMA window instead of an array of samples residing in host memory. NI-FGEN detects when the address is within the direct DMA window and handles the transfer appropriately.

#### C Example

1. Enable the signal generator for direct DMA writes by setting the NIFGEN_ATTR_DIRECT_DMA_ENABLED attribute. Once enabled, NI-FGEN monitors and reports any issues with the direct DMA transfer.
2. Identify the waveform data source and set the NIFGEN_ATTR_DIRECT_DMA_WINDOW_ADDRESS attribute to the address provided by your direct DMA-compatible data source.
3. Set the NIFGEN_ATTR_DIRECT_DMA_WINDOW_SIZE attribute to the size of the memory window provided by your direct DMA-compatible data source.
4. Use the niFgen_WriteBinary16Waveform function to write blocks of data to the signal generator. For each block of data written to the signal generator, you provide the address of the direct DMA window instead of an array of samples residing in host memory. NI-FGEN detects when the address is within the direct DMA window and handles the transfer appropriately.

Parent topic:

Configuring an Application for Streaming

Related concepts:

- Direct DMA

<!--NI_TOPIC bundle=ni-fgen path=considerations-for-using-labview-real-time-module.html language=enus -->
## TOPIC 00033: Considerations for using the LabVIEW Real-Time Module

- bundle_id: `ni-fgen`
- source_path: `considerations-for-using-labview-real-time-module.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/considerations-for-using-labview-real-time-module.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Create an NI-FGEN application using NI-FGEN VIs and the LabVIEW Real-Time Module according to the standard procedure for developing applications in the LabVIEW Real-Time Module. Using NI signal generators with the LabVIEW Real-Time Module does not support external calibration.

### Considerations for using the LabVIEW Real-Time
 Module

Create an NI-FGEN application using NI-FGEN VIs and the LabVIEW Real-Time Module
 according to the standard procedure for developing applications in the LabVIEW Real-Time
 Module.

Using NI signal generators with the LabVIEW Real-Time Module does not support external
 calibration.

Parent topic:

Creating an Application with NI-FGEN and Your ADE

Related information:

- LabVIEW Real-Time Module User Manual
- NI-FGEN LabVIEW VI Reference

<!--NI_TOPIC bundle=ni-fgen path=creating-a-data-marker-event.html language=enus -->
## TOPIC 00034: Creating a Data Marker Event

- bundle_id: `ni-fgen`
- source_path: `creating-a-data-marker-event.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/creating-a-data-marker-event.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: To create and export a Data Marker event, complete the following steps: LabVIEW Example Specify the active channel as "DataMarker(0-3)". Specify a data bit number using the Data Marker Event Bit Number property. Set the output polarity of the data marker event using the Data Marker Event Level Polar

### Creating a Data Marker Event

To create and export a Data Marker event, complete the following steps:

#### LabVIEW Example

1. Specify the active channel as "DataMarker(0-3)".
2. Specify a data bit number using the Data Marker Event Bit Number property.
3. Set the output polarity of the data marker event using the Data Marker Event Level Polarity property.
4. To export the data marker, use the niFgen Export Signal VI. To determine all possible signal routes for your device, refer to the Routes topic for your device or the Device Routes tab in MAX.
 Note 

 When exporting data markers, you must specify the signal identifier for the data marker using the niFgen Export Signal VI.

#### C Example

1. Specify the active channel as "DataMarker(0-3)".
2. Specify a data bit number using the NIFGEN_ATTR_DATA_MARKER_EVENT_DATA_BIT_NUMBER attribute.
3. Set the output polarity of the data marker event using the NIFGEN_ATTR_DATA_MARKER_EVENT_LEVEL_POLARITY attribute.
4. To export the data marker, use the niFgen_ExportSignal function. To determine all possible signal routes for your device, refer to the Routes topic for your device or the the Device Routes tab in MAX. 
 
 Note 

 When exporting data markers, you must specify the signal identifier for the data marker using the niFgen_ExportSignal function.

Parent topic:

Features

<!--NI_TOPIC bundle=ni-fgen path=creating-a-marker-event-in-arbitrary-sequence.html language=enus -->
## TOPIC 00035: Creating a Marker Event in Arbitrary Sequence Mode

- bundle_id: `ni-fgen`
- source_path: `creating-a-marker-event-in-arbitrary-sequence.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/creating-a-marker-event-in-arbitrary-sequence.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can specify a marker and its location by setting an offset location value (in number of samples) from the start of the waveform. If the offset is out of range of the number of samples in that segment, NI-FGEN returns an error. LabVIEW Example Call the niFgen Create Advanced Arb Sequence VI and s

### Creating a Marker Event in Arbitrary Sequence Mode

You can specify a marker and its location by
setting an offset location value (in number of samples) from the
start of the waveform. If the offset is out of range of the number
of samples in that segment, NI-FGEN returns an error.

#### LabVIEW Example

1. Call the 
niFgen
Create Advanced Arb Sequence VI and set 
 Marker Location Array to the location at which you
would like the marker to generate.
2. Export the marker event by calling the 
niFgen Export
Signal VI and setting 
 Signal to " NIFGEN_VAL_MARKER_EVENT ".

#### C Example

1. Call the 
 niFgen_CreateAdvancedArbSequence function and set the 
 markerLocationArray parameter to the location at
which you would like the marker to generate.
2. Export the marker event by calling the 
 niFgen_ExportSignal function and setting the 
 signal parameter to " 
 NIFGEN_VAL_MARKER_EVENT ".

Parent topic:

Creating a Marker Event

<!--NI_TOPIC bundle=ni-fgen path=creating-a-marker-event-in-arbitrary-waveform.html language=enus -->
## TOPIC 00036: Creating a Marker Event in Arbitrary Waveform Mode

- bundle_id: `ni-fgen`
- source_path: `creating-a-marker-event-in-arbitrary-waveform.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/creating-a-marker-event-in-arbitrary-waveform.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can specify a marker and its location by setting an offset location value (in number of samples) from the start of the waveform. If the offset is out of range of the number of samples in that segment, NI-FGEN returns an error. NI-FGEN supports only Marker0 in arbitrary waveform mode. LabVIEW E

### Creating a Marker Event in Arbitrary Waveform Mode

Note

#### LabVIEW Example

1. Specify the active channel as "Marker0".
2. Specify the position of the Marker event by setting the 
Arbitrary
Waveform Marker Position property.
3. Export the marker event by calling the 
niFgen Export
Signal VI and setting 
 Signal to " NIFGEN_VAL_MARKER_EVENT ".

#### C Example

1. Specify the active channel as "Marker0".
2. Specify the position of the Marker event by setting the 
 NIFGEN_ATTR_ARB_MARKER_POSITION attribute.
3. Export the marker event by calling the 
 niFgen_ExportSignal function and setting the 
 signal parameter to "
 NIFGEN_VAL_MARKER_EVENT ".

Parent topic:

Creating a Marker Event

<!--NI_TOPIC bundle=ni-fgen path=creating-a-marker-event-in-script-mode.html language=enus -->
## TOPIC 00037: Creating a Marker Event in Script Mode

- bundle_id: `ni-fgen`
- source_path: `creating-a-marker-event-in-script-mode.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/creating-a-marker-event-in-script-mode.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can specify a marker and its location by setting an offset location value (in number of samples) from the start of the waveform. If the offset is out of range of the number of samples in that segment, NI-FGEN returns an error. In Script mode, you can create up to four markers for each waveform.

### Creating a Marker Event in Script Mode

You can specify a marker and its location by
setting an offset location value (in number of samples) from the
start of the waveform. If the offset is out of range of the number
of samples in that segment, NI-FGEN returns an error.

In 
*Script mode*, you can create up to
four markers for each waveform.

#### LabVIEW Example

1. To create markers in Script mode, refer to 
Common Scripting
Use Cases.
2. Export the marker event by calling the 
niFgen Export
Signal VI. Set 
 Signal to " NIFGEN_VAL_MARKER_EVENT " and set 
 Signal Identifier to the name of the marker to
export.

#### C Example

1. To create markers in Script mode, refer to 
Common Scripting
Use Cases.
2. Export the marker event by calling the 
 niFgen_ExportSignal function. Set the 
 signal parameter to " 
 NIFGEN_VAL_MARKER_EVENT " and the 
 signalIdentifier parameter to the name of the
marker to export.

Parent topic:

Creating a Marker Event

Related concepts:

- Script Mode

<!--NI_TOPIC bundle=ni-fgen path=creating-a-marker-event.html language=enus -->
## TOPIC 00038: Creating a Marker Event

- bundle_id: `ni-fgen`
- source_path: `creating-a-marker-event.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/creating-a-marker-event.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can specify a marker and its location by setting an offset location value (in number of samples) from the start of the waveform. If the offset is out of range of the number of samples in that segment, NI-FGEN returns an error. There are two rules for marker placement: A marker can be specified o

### Creating a Marker Event

You can specify a marker and its location by setting an offset location value (in number of samples) from the start of the waveform. If the offset is out of range of the number of samples in that segment, NI-FGEN returns an error.

There are two rules for marker placement:

1. A marker can be specified only at offsets that are multiples of four samples (or two complex samples).
2. A marker must be placed at least four samples from the end of the waveform. In Burst trigger mode, a marker must be placed at least eight samples from the end of the waveform.

Note

Parent topic:

Features

<!--NI_TOPIC bundle=ni-fgen path=creating-an-aplication-with-visual-basic.html language=enus -->
## TOPIC 00039: Creating an Application with Visual Basic

- bundle_id: `ni-fgen`
- source_path: `creating-an-aplication-with-visual-basic.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/creating-an-aplication-with-visual-basic.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `task`
- source_description: Develop an NI-FGEN application in Visual Basic. Open an existing or new Visual Basic project. Create the following files, which are necessary for your application, and add the files to your project: Form definition and event handling code: .frm (Optional) Visual Basic generic code module: .bas (Opti

### Creating an Application with Visual
 Basic

Develop an NI-FGEN application in Visual Basic.

1. Open an existing or new Visual Basic project.
2. Create the following files, which are necessary for your application, and add the files
 to your project: 
 Form definition and event handling code: .frm
 (Optional) Visual Basic generic code module:
 .bas
 (Optional) Visual Basic class module:
 .cls
3. Add a reference to the NI-FGEN library, which is part of
 niFgen_32.dll, by selecting Project»References»National Instruments Function Generator. 
 If the NI-FGEN library is not there, click Browse and locate
 niFgen_32.dll in your directory.
4. Press F2 to use the Object Browser to
 find function prototypes and constants.
5. Add NI-FGEN function calls to your application.
6. Run your application by clicking Run»Start.

Parent topic:

Creating an Application with NI-FGEN and Your ADE

<!--NI_TOPIC bundle=ni-fgen path=creating-an-application-with-labview.html language=enus -->
## TOPIC 00040: Creating an Application with LabVIEW

- bundle_id: `ni-fgen`
- source_path: `creating-an-application-with-labview.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/creating-an-application-with-labview.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `task`
- source_description: Develop an NI-FGEN application in LabVIEW. Open an existing or new LabVIEW VI. From the Function palette, locate the NI-FGEN VIs at Instrument I/O Instrument Drivers NI-FGEN . Click the VIs that you want to use, and drop them on the block diagram to build your application. To browse the NI-FGEN exam

### Creating an Application with LabVIEW

Develop an NI-FGEN application in LabVIEW.

1. Open an existing or new LabVIEW VI.
2. From the Function palette, locate the NI-FGEN VIs at Instrument I/O»Instrument Drivers»NI-FGEN.
3. Click the VIs that you want to use, and drop them on the block diagram to build your
 application.

To browse the NI-FGEN examples available in LabVIEW, select Find Examples»Hardware Input and Output»Modular Instruments»NI-FGEN.

Parent topic:

Creating an Application with NI-FGEN and Your ADE

Related information:

- LabVIEW User Manual
- NI-FGEN LabVIEW VI Reference

<!--NI_TOPIC bundle=ni-fgen path=creating-an-application-with-labwindows-cvi.html language=enus -->
## TOPIC 00041: Creating an Application with LabWindows/CVI

- bundle_id: `ni-fgen`
- source_path: `creating-an-application-with-labwindows-cvi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/creating-an-application-with-labwindows-cvi.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `task`
- source_description: Develop an NI-FGEN application in LabWindows/CVI. Open an exsisting or new project file. Load the NI-FGEN function tree, niFgen.fp, from VXIPnP\<WinNT|9x>\niFgen. Navigate the function hierarchy and generate function calls with the proper syntax and variable values. To browse the NI-FGEN examples av

### Creating an Application with
 LabWindows/CVI

Develop an NI-FGEN application in LabWindows/CVI.

1. Open an exsisting or new project file.
2. Load the NI-FGEN function tree, niFgen.fp, from
 VXIPnP\<WinNT|9x>\niFgen.
3. Navigate the function hierarchy and generate function calls with the proper
 syntax and variable values.

To browse the NI-FGEN examples available in LabWindows/CVI, select Help»Find Examples, and navigate to Hardware Input and Output»Modular Instruments»NIFGEN.

You can also access the examples using the Start menu, by
 selecting Start»All Programs»National Instruments»NI-FGEN»Examples.

Parent topic:

Creating an Application with NI-FGEN and Your ADE

Related information:

- NI-FGEN C Function Reference

<!--NI_TOPIC bundle=ni-fgen path=creating-an-application-with-visual-c.html language=enus -->
## TOPIC 00042: Creating an Application with Visual C++

- bundle_id: `ni-fgen`
- source_path: `creating-an-application-with-visual-c.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/creating-an-application-with-visual-c.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `task`
- source_description: develop an NI-FGEN application in Microsoft Visual C++. Open an existing or new Visual C++ project. Create and add source files to the project. C source code is .c and C++ source code is .cpp. Make sure that you include the NI-FGEN header file (niFGEN.h) in your source code files as #include "niFGEN

### Creating an Application with Visual
 C++

develop an NI-FGEN application in Microsoft Visual C++.

1. Open an existing or new Visual C++ project.
2. Create and add source files to the project. 
 C source code is .c and C++ source code is
 .cpp. Make sure that you include the NI-FGEN header
 file (niFGEN.h) in your source code files as
 #include "niFGEN.h".
3. Specify the directory that contains the NI-FGEN header file under the Preprocessor»Additional include directories settings in your compiler. For Visual C++ 6.0, these files are under Project»Settings»C/C++.
4. Add the NI-FGEN import library, niFGEN.lib, to the project
 under Link»General»Object/Library Modules.
5. Add NI-FGEN function calls to your application.
6. Build your application.

Parent topic:

Creating an Application with NI-FGEN and Your ADE

<!--NI_TOPIC bundle=ni-fgen path=creating-application-with-ni-fgen.html language=enus -->
## TOPIC 00043: Creating an Application with NI-FGEN and Your ADE

- bundle_id: `ni-fgen`
- source_path: `creating-application-with-ni-fgen.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/creating-application-with-ni-fgen.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Learn how to use NI-FGEN with your application development environment (ADE). Locate files that you need to include in your application. To successfully build your application, you need to have NI-FGEN installed, along with one of the following ADEs: LabVIEW LabVIEW Real-Time Module LabWindows/CVI M

### Creating an Application with NI-FGEN and Your
 ADE

Learn how to use NI-FGEN with your application development environment (ADE). Locate
 files that you need to include in your application.

- LabVIEW
- LabVIEW Real-Time Module
- LabWindows/CVI
- Microsoft Visual C/C++
- Microsoft Visual Basic

See the following sections for more details on creating an application.

- [Creating an Application with LabVIEW](creating-an-application-with-labview.html) Develop an NI-FGEN application in LabVIEW.
- [Considerations for using the LabVIEW Real-Time Module](considerations-for-using-labview-real-time-module.html) Create an NI-FGEN application using NI-FGEN VIs and the LabVIEW Real-Time Module according to the standard procedure for developing applications in the LabVIEW Real-Time Module.
- [Creating an Application with LabWindows/CVI](creating-an-application-with-labwindows-cvi.html) Develop an NI-FGEN application in LabWindows/CVI.
- [Creating an Application with Visual C++](creating-an-application-with-visual-c.html) develop an NI-FGEN application in Microsoft Visual C++.
- [Creating an Application with Visual Basic](creating-an-aplication-with-visual-basic.html) Develop an NI-FGEN application in Visual Basic.

Parent topic:

Programming

Related information:

- LabVIEW User Manual
- LabVIEW Real-Time Module User Manual
- NI-FGEN LabVIEW VI Reference
- NI-FGEN C Function Reference

<!--NI_TOPIC bundle=ni-fgen path=dac-resolution.html language=enus -->
## TOPIC 00044: DAC Resolution

- bundle_id: `ni-fgen`
- source_path: `dac-resolution.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/dac-resolution.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Digital-to-analog converter (DAC) resolution is a limiting factor in determining the accuracy of the re–creation of an analog waveform from digital samples. More details are present in the waveform if the DAC resolution is increased. A 3-bit DAC divides the vertical range into eight discrete levels.

### DAC Resolution

Digital-to-analog converter (DAC) resolution is a limiting factor in determining the accuracy of the re–creation of an analog waveform from digital samples. More details are present in the waveform if the DAC resolution is increased. A 3-bit DAC divides the vertical range into eight discrete levels. With a vertical range of 10 V, the 3-bit DAC cannot generate voltage differences smaller than 1.25 V. In comparison, a 16-bit DAC with 65,536 discrete levels can generate voltage differences as small as 153 µV.

The following figure shows the difference between two waveforms. The 16-bit waveform looks like a continuous sine wave, but if you were to zoom in, you would see the discrete steps of 153 µV. Both waveforms are composed of discrete voltage steps, but the 16-bit version looks much closer to a "pure" continuous–time sine waveform.

[IMAGE alt='image' src='GUID-3A37E59F-3AA3-49F0-B17C-624ADCC8251C-a5.gif']

Parent topic:

Waveform Fundamentals

<!--NI_TOPIC bundle=ni-fgen path=data-marker-events.html language=enus -->
## TOPIC 00045: Data Marker Events

- bundle_id: `ni-fgen`
- source_path: `data-marker-events.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/data-marker-events.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Data Marker events allow you to export any one of the 16 waveform data bits to any valid destination on the device. Up to four of the 16 waveform data bits can be exported at one time. Refer to Features Supported to determine if your device supports data marker events. The level of a Data Marker

### Data Marker Events

The Data Marker events allow you to export any one of the 16 waveform data bits to any valid destination on the device. Up to four of the 16 waveform data bits can be exported at one time. Refer to *Features Supported* to determine if your device supports data marker events.

The level of a Data Marker event changes at the time that a specific data bit toggles in the waveform data. If the waveform data bit toggles multiple times in a segment, the Data Marker event level changes each time. When the data bit level is high, the Data Marker event level is high. You can invert this relationship by setting the Data Marker Event Level Polarity property or the NIFGEN_ATTR_DATA_MARKER_EVENT_LEVEL_POLARITY attribute.

The following figure shows the exported data marker event shifting between low and high as the specified data bit toggles.

[IMAGE alt='image' src='GUID-450B5058-4B48-4A29-A4CF-1DED0CA1047B-a5.gif']

NI-FGEN compensates for the factors that affect the delays in the digital and analog paths in assuring that the Data Marker event appears within one Sample clock of the waveform output.

#### Data Markers as Trigger Outputs

A delay of at least 44 Sample clocks exists between the Start trigger and when the analog waveform generation appears on the output connector. Therefore, synchronizing the signal generator output signal to other devices with fast trigger response times is accomplished using the data marker event from the signal generator as the trigger source for the other device for more precise alignment to the generating waveform. You can do this using the RTSI bus, PXI trigger lines, SYNC OUT/PFI 0 and PFI 1, or PFI 4 and PFI 5.

Note

#### Related Topics

*Creating a Data Marker Event*

Parent topic:

Events

Related concepts:

- Features Supported on SMC Devices
- Creating a Data Marker Event

<!--NI_TOPIC bundle=ni-fgen path=devices.html language=enus -->
## TOPIC 00046: Devices

- bundle_id: `ni-fgen`
- source_path: `devices.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/devices.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Review the following topics for device-specific information about your NI signal generator.

### Devices

Review the following topics for device-specific information about your NI signal generator.

- [Features Supported on Non-SMC Devices](features-supported-on-non-smc-devices.html)
- [Features Supported on SMC Devices](features-supported-on-smc-devices.html)
- [Features Supported on PXIe-5413/5423/5433 Waveform Generators](features-supported-on-pxie-5413-5423-5433-wav.html)
- [NI 5402 NI 5402 Overview](ni-5402-ni-5402-overview.html)
- [NI 5404 NI PXI-5404 Overview](ni-5404-ni-pxi-5404-overview.html)
- [NI 5406 NI 5406 Overview](ni-5406-ni-5406-overview.html)
- [NI 5412 NI 5412 Overview](ni-5412-ni-5412-overview.html)
- [NI 5421 NI 5421 Overview](ni-5421-ni-5421-overview.html)
- [NI 5422 NI 5422 Overview](ni-5422-ni-5422-overview.html)
- [NI 5441 NI 5441 Overview](ni-5441-ni-5441-overview.html)
- [NI 5442 NI 5442 Overview](ni-5442-ni-5442-overview.html)
- [NI 5450 NI 5450 Overview](ni-5450-ni-5450-overview.html)
- [NI 5451 NI 5451 Overview](ni-5451-ni-5451-overview.html)

<!--NI_TOPIC bundle=ni-fgen path=different-video-formats.html language=enus -->
## TOPIC 00047: Different Video Formats

- bundle_id: `ni-fgen`
- source_path: `different-video-formats.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/different-video-formats.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The definition of the composite video signal differs from country to country. Three main video formats exist worldwide: M-NTSC—Mainly used in the USA and Japan B/G-PAL—Used in most of Europe, parts of Africa, and some other countries such as Australia SECAM—Used in France, the former Soviet Union, a

### Different Video Formats

The definition of the composite video signal differs from country to country. Three main video formats exist worldwide:

- M-NTSC—Mainly used in the USA and Japan
- B/G-PAL—Used in most of Europe, parts of Africa, and some other countries such as Australia
- SECAM—Used in France, the former Soviet Union, and parts of the Middle East

Three other formats, M-PAL, N-PAL, and Combination N-PAL, are used in some countries in South America.

Parent topic:

Video Signal Fundamentals

<!--NI_TOPIC bundle=ni-fgen path=differential-output.html language=enus -->
## TOPIC 00048: Differential Output

- bundle_id: `ni-fgen`
- source_path: `differential-output.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/differential-output.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: An NI signal generator that is configured for differential output generates waveforms using two complementary signals. Each signal is generated at a different differential output connector. When the two signals are compared at a receiver that has good rejection, any common-mode noise, that is, noise

### Differential Output

An NI signal generator that is configured for differential output generates
 waveforms using two complementary signals. Each signal is generated at a different
 differential output connector. When the two signals are compared at a
 receiver that has good rejection, any common-mode noise, that is, noise common between the
 two output terminals, and even-order distortions, for example, 2nd, 4th, 6th, ... harmonics,
 affect whether the receiving instrument can detect an accurate signal.

Parent topic:

Waveform Fundamentals

<!--NI_TOPIC bundle=ni-fgen path=digital-pattern-generation.html language=enus -->
## TOPIC 00049: Digital Pattern Generation

- bundle_id: `ni-fgen`
- source_path: `digital-pattern-generation.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/digital-pattern-generation.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Some NI signal generators support 16-bit digital pattern generation at a digital connector. The digital pattern generation provides a digital representation of the waveforms generated on the analog connector of the device at the same rates as the analog signal.

### Digital Pattern Generation

Some NI signal generators support 16-bit digital pattern generation at a digital connector. The digital pattern generation provides a digital representation of the waveforms generated on the analog connector of the device at the same rates as the analog signal.

Parent topic:

Arbitrary Waveform Output Mode

<!--NI_TOPIC bundle=ni-fgen path=direct-digital-synthesis.html language=enus -->
## TOPIC 00050: Direct Digital Synthesis

- bundle_id: `ni-fgen`
- source_path: `direct-digital-synthesis.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/direct-digital-synthesis.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: On some NI signal generators, the Standard Function output mode is implemented through direct digital synthesis (DDS). The following figure shows the building blocks for DDS-based waveform generation. You can use the lookup memory in Standard Function output mode only. You cannot use the lookup memo

### Direct Digital Synthesis

On some NI signal generators, the *Standard Function output mode* is implemented through direct digital synthesis (DDS).

The following figure shows the building blocks for DDS-based waveform generation.

[IMAGE alt='image' src='GUID-EF12101B-768D-4C7B-816E-74921623EA96-a5.gif']

You can use the lookup memory in Standard Function output mode only. You cannot use the lookup memory in *Arbitrary Waveform output mode*. You can store one cycle of a repetitive waveform—a sine, triangular, square, or arbitrary wave—in the lookup memory. Then, you can change the frequency of that waveform by sending just one instruction. You can use Standard Function output mode for very fine frequency resolution function generation. Because Standard Function output mode uses an accumulator, waveform generation loops back to the beginning of the lookup memory after passing through the end of the lookup memory.

Note

Parent topic:

Standard Function Mode

Related concepts:

- Standard Function Mode
- Arbitrary Waveform Output Mode

<!--NI_TOPIC bundle=ni-fgen path=direct-dma.html language=enus -->
## TOPIC 00051: Direct DMA

- bundle_id: `ni-fgen`
- source_path: `direct-dma.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/direct-dma.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Direct DMA can be used to transfer waveform data to the signal generator onboard memory at rates well beyond the typical 5 to 30 MB/s range in a standard PC-based architecture. To achieve such high rates, Direct DMA establishes a direct connection between the signal generator onboard memory and a sp

### Direct DMA

*Direct DMA* can be used to transfer waveform data to the signal generator onboard
 memory at rates well beyond the typical 5 to 30 MB/s
 range in a standard PC-based architecture. To achieve such high rates, Direct DMA
 establishes a direct connection between the signal generator onboard memory and a
 specialized waveform data source. Direct DMA is commonly used to stream waveform data
 from disk at data rates of greater than 100 MB/s.

In a standard PC-based architecture playback rates to the 5 to 40
 MB/s range are limited by the following factors:

- Shared data paths through the PCI controller, I/O bus, CPU, and memory that divide down bandwidth
- Latencies introduced by the operating system and application software managing data flow
- Nondeterministic operating system management of file I/O

For example, in a standard PC-based architecture, downloading a waveform to the onboard memory of your signal generator requires the following process for every 4,096 byte segment of physical memory:

1. The signal generator retrieves an address identifying the location of the data segment in the host memory.
2. The signal generator uses the address to request transfer of the data segment in the host memory.
3. The signal generator downloads the data to the onboard memory of the signal generator.
4. Steps 1-3 repeat every 4,096 bytes until the waveform data is fully downloaded.

To download a 16 MB waveform (16,777,216 bytes), this process
 repeats 4,096 times (16,777,216 bytes/4,096 bytes).

The direct connection established by Direct DMA to the data source is able to minimize or eliminate the factors that limit playback rates. To download data to the onboard memory of the signal generator with Direct DMA, the following process occurs only once:

1. The signal generator retrieves an address identifying the location of the waveform data source. This address generally refers to a large window of physically contiguous memory.
2. The signal generator uses the address to contact the waveform data source.
3. The signal generator requests the data segment and size from waveform data source. In this case,
 the size requested by the signal generator can be fairly large (for example, 16 MB ).
4. The signal generator downloads the data to the onboard memory of the signal generator from the waveform data source in one operation.

The transfer process is much faster and more efficient because an address to the waveform data is
 requested once (in this case, the address is to the waveform data source).

Parent topic:

Streaming

Related concepts:

- Streaming
- Configuring Your Application for Direct DMA

<!--NI_TOPIC bundle=ni-fgen path=edge-trigger.html language=enus -->
## TOPIC 00052: Edge Trigger

- bundle_id: `ni-fgen`
- source_path: `edge-trigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/edge-trigger.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: A digital signal has two discrete levels: a high level and a low level. When the signal transitions from high to low or from low to high, a digital edge is created. There are two types of edges: rising, which occurs when the signal transitions from low level to high level, and falling, which occurs

### Edge Trigger

A digital signal has two discrete levels: a high level and a low level. When the signal transitions from high to low or from low to high, a digital edge is created. There are two types of edges: rising, which occurs when the signal transitions from low level to high level, and falling, which occurs with a transition from high level to low level. Triggers configured to act on a rising or falling edge of a digital signal are called edge triggers.

As the following figure shows, an edge trigger could be configured to occur either at the place labeled Falling Edge of Signal or at Rising Edge of Signal.

[IMAGE alt='image' src='GUID-12A2FC9C-7966-496B-9103-C59CCE33B409-a5.gif']

Parent topic:

Types of Triggers

<!--NI_TOPIC bundle=ni-fgen path=enob.html language=enus -->
## TOPIC 00053: ENOB

- bundle_id: `ni-fgen`
- source_path: `enob.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/enob.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Effective number of bits (ENOB) is another way of specifying signal-to-noise and distortion ratio (SINAD). ENOB is calculated using the following formula: ENOB = SINAD − 1.76 6.02 This equation assumes the full scale of the DAC is utilized. The ENOB value is the value of an ideal DAC that is equival

### ENOB

Effective number of bits (ENOB) is another way of specifying signal-to-noise
 and distortion ratio (*SINAD*). ENOB is calculated using the following
 formula:

ENOB

=

SINAD

−

1.76

6.02

Note

The ENOB value is the value of an ideal DAC that is equivalent to the DAC of the
 device.

Parent topic:

Frequency Domain Fundamentals

Related concepts:

- SINAD

<!--NI_TOPIC bundle=ni-fgen path=environment.html language=enus -->
## TOPIC 00054: Environment

- bundle_id: `ni-fgen`
- source_path: `environment.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/environment.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Device performance and reliability may be limited at temperatures above the specified operating range. For best performance take the following precautions: Ensure that the ambient temperature is within the specifications for the device and is stable (±5 °C). Follow standard metrology practices. Use

### Environment

Device performance and reliability may be limited
at temperatures above the specified operating range. For best
performance take the following precautions:

- Ensure that the ambient temperature is within the
specifications for the device and is stable (±5 °C).
- Follow standard metrology practices.
- Use a PXI or PXI Express chassis with a well-designed cooling
system.

Operating NI PXI and PXI Express signal
generators outside the specified operating temperatures can
increase bias currents in the electronic components, increase
noise, accelerate drifts, and decrease product life. Beyond the
maximum specified operating temperatures, the device may perform
differently than during factory calibration, resulting in
additional measurement errors. Also, operating the device outside
of the humidity specification (>80%, >35 °C) may cause
leakages between circuit components and introduce measurement
error.

To optimize cooling and ensure best performance and
reliability the use the following guidelines:

- Chassis that provide multiple fan speed settings should always
be run with fans set on high or auto if applicable to your chassis.
Never set the fans to low or turn them off.

Note

- All empty slots in the chassis should be covered with a blank
slot filler panel.
- Remove and clean the inlet filters often to prevent buildup of
dust and other foreign material that may restrict airflow.
- The chassis should be located such that the fan inlets and
outlet vents are not obstructed. Other objects and equipment should
be kept a minimum of 3 inches from the fan inlets.

For more information about forced-air cooling,
refer to your chassis documentation.

NI PXI and PXI Express signal generators are
designed to operate at shock up to 30 g, 11 ms, half-sine. It
is specified to withstand shock up to 50 g, 11 ms, half-sine
when not operating (shipping/storage).

NI PXI and PXI Express signal generators are
designed to withstand total random vibration of 0.31 g 
<sub>rms</sub> operational and 2.46 g 
<sub>rms</sub> non operational per IEC 68-2-64.

Parent topic:

Integration and System Considerations

<!--NI_TOPIC bundle=ni-fgen path=event-delays.html language=enus -->
## TOPIC 00055: Event Delays

- bundle_id: `ni-fgen`
- source_path: `event-delays.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/event-delays.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Event delays can manually delay Marker, Started, and Done events so that they are aligned on a particular sample clock period. Delay is applied to the event with respect to the analog output of the signal generator. For example, a delay of 0 sample clocks aligns the event with the analog output sign

### Event Delays

Event delays can manually delay Marker, Started, and Done events so that they are aligned on a
 particular sample clock period.

Delay is applied to the event with respect to the analog output of the signal generator. For
 example, a delay of 0 sample clocks aligns the event with the analog output signal,
 while a delay of +2 sample clocks causes the event to appear two sample clock periods
 after the analog output appears. All event delays are adjusted in increments of sample
 clock periods, regardless of the units used to set the delay. For example, if you
 provide a value for delay with units of seconds, the delay is coerced up to the nearest
 sample clock period.

The event delay attributes must be set before waveform generation is initiated. Any changes made
 to other attributes during waveform generation may change the analog output delay.
 NI-FGEN does not compensate for this change in the analog output delay and continues to
 apply the event delay that you was originally configured.

If an event delay is applied to an event that is being exported
to multiple output terminals, NI-FGEN aligns the event on the first
terminal you specified.

You can configure event delays by calling the Marker Event Delay property or
 the NIFGEN_ATTR_MARKER_EVENT_DELAY attribute, the Started
 Event Delay property or the
 NIFGEN_ATTR_STARTED_EVENT_DELAY attribute, or the
 Done Event Delay property or the
 NIFGEN_ATTR_DONE_EVENT_DELAY attribute.

Parent topic:

Events

<!--NI_TOPIC bundle=ni-fgen path=events.html language=enus -->
## TOPIC 00056: Events

- bundle_id: `ni-fgen`
- source_path: `events.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/events.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: An event is a signal generated by the NI device at a device state. Typically, events are configured to indicate when a specific hardware condition has been met. Refer to Features Supported to determine what events your signal generator supports. Event Output Behaviors Events can have one of three ou

### Events

An event is a signal generated by the NI device at a device state. Typically, events are configured to indicate when a specific hardware condition has been met. Refer to *Features Supported* to determine what events your signal generator supports.

#### Event Output Behaviors

Events can have one of three output behaviors.

- Toggle—Each instance of the event toggles between high and low. You can set the initial state of the event.
- Pulse—Each event triggers a pulse for a specified period of time.
- Level—While the event is active, it shifts high or low depending on the active state you specify.

#### Event Status

Events can return their status in two ways.

- Live—Returns the current state of the event.
- Latched—Returns whether the event has ever been active.

The following table describes the event output behaviors and statuses supported by NI signal generators.

| Event Name | Description | Output Behavior | Status |
| --- | --- | --- | --- |
| Ready for Start | Ready For Start event indicates that the signal generator is configured and ready to receive a Start trigger. | Level | Live |
| Started | Started event indicates when the signal generator has received a Start trigger and is generating a waveform. | Level, Pulse | Latched |
| Marker | A Marker is an event that the device generates in relation to a waveform that is generated. The event is configured to occur at the time that a specific location or sample n if the waveform generates on the analog output connector. If the waveform loops multiple times in a segment, the marker generates each time the waveform loops. | Pulse, Toggle | Latched, Live |
| Data Marker | A Data Marker is an event that the signal generator generates in relation to the data bits of a waveform that is generated. Up to four bits can be configured to export to any valid destination on the signal generator. | Level | N/A |
| Done | The Done event indicates that the generation of the previous waveform is complete. | Level, Pulse | Latched |

Parent topic:

Waveform Fundamentals

Related concepts:

- Features Supported on SMC Devices
- Marker Events
- Data Marker Events

<!--NI_TOPIC bundle=ni-fgen path=extended-support-changes.html language=enus -->
## TOPIC 00057: Updates and Changes for NI-FGEN Extended Support Versions

- bundle_id: `ni-fgen`
- source_path: `extended-support-changes.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/extended-support-changes.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Browse updates and changes made in NI-FGEN versions on extended support. If you cannot find changes for your version, it might be a more recent version, documented as a new feature. Or, your version might not have included user-facing updates. You can find more information about non-visible changes,

### Updates and Changes for NI-FGEN Extended Support Versions

Browse updates and changes made in NI-FGEN versions
 on extended support.

Note

Release Notes

#### NI-FGEN 21.8 Changes

Learn about new features, behavior changes, and other updates in NI-FGEN
 21.8.

- NI-FGEN 21.8 adds support for LabVIEW 2022
- NI-FGEN 21.3 adds support for NI Linux® Real-Time
- NI-FGEN 21.3 adds support for LabVIEW 2021
- NI-FGEN 20.0 adds support for LabVIEW 2020 and LabVIEW NXG 5.0

#### NI-FGEN 21.3 Changes

Learn about new features, behavior changes, and other updates in NI-FGEN
 21.3.

- NI-FGEN 21.3 adds support for NI Linux® Real-Time.
- NI-FGEN 21.3 adds support for LabVIEW 2021.
- NI-FGEN 20.0 adds support for LabVIEW 2020 and LabVIEW NXG 5.0.
- NI-FGEN 21.3 removes support for Manual Peer-to-Peer functionality.
- NI-FGEN 21.3 removes support for NI-HWS.
- The NI-FGEN Soft Front Panel has been replaced by InstrumentStudio, which is
 automatically installed when you install the NI-FGEN driver. You can access
 InstrumentStudio in one of the following ways: Note The deprecated NI-FGEN Soft Front Panel remains available for download. Visit
 Legacy Soft Front Panels for NI-FGEN for more information.
  - From the Windows start menu, select National Instruments»InstrumentStudio [year].
 This launches InstrumentStudio and runs a soft front panel populated with devices
 detected on your system.
  - From Measurement & Automation Explorer (MAX), select a device and then click
 Test Panels.... This launches InstrumentStudio and runs a soft front panel for the
 device you selected.

#### NI-FGEN 20.0 Changes

Learn about new features, behavior changes, and other updates in NI-FGEN
 20.0.

- NI-FGEN 20.0 adds support for LabVIEW 2020 and LabVIEW NXG 5.0.

#### NI-FGEN 19.5 Changes

Learn about new features, behavior changes, and other updates in NI-FGEN
 19.5.

- NI-FGEN 19.5 adds support for LabVIEW NXG 4.0.

#### NI-FGEN 19.1 Changes

Learn about new features, behavior changes, and other updates in NI-FGEN
 19.1.

- NI-FGEN 19.1 adds support for importing and exporting configurations between NI-FGEN
 sessions.

#### NI-FGEN 19.0 Changes

Learn about new features, behavior changes, and other updates in NI-FGEN
 19.0.

- NI-FGEN 19.0 adds support for LabVIEW 2019 and LabVIEW NXG 3.1.
- NI-FGEN 19.0 drops support for Traditional DAQ (NI-DAQ) and the PCI/PXI-5401,
 PCI/PXI-5411, and PCI/PXI-5431 waveform generators.
- NI-FGEN 19.0 drops support for Express VIs in LabVIEW. Existing code created with
 earlier versions of NI-FGEN and that contains Express VIs will continue to execute, but
 the Express VI cannot be reconfigured from a dialog box. To reconfigure an Express VI,
 right-click the Express VI and select Open Front Panel»Convert. This will convert the
 Express VI to code that you can configure on the block diagram. NI recommends converting
 Express VIs to code before using the Code Conversion Utility in LabVIEW NXG to convert
 code for LabVIEW NXG.

<!--NI_TOPIC bundle=ni-fgen path=features-supported-on-non-smc-devices.html language=enus -->
## TOPIC 00058: Features Supported on Non-SMC Devices

- bundle_id: `ni-fgen`
- source_path: `features-supported-on-non-smc-devices.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/features-supported-on-non-smc-devices.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following table shows the features supported by the NI 5404 signal generators. NI 5404 Basic Operation Output Modes Standard Function (sine or square) Standard Function Output Waveform Sine and Square (both are produced) Minimum Frequency 1 µHz Maximum Frequency^1 105 MHz SYNC Duty Cycle — User-

### Features Supported on Non-SMC Devices

The following table shows the features supported by
the NI 5404 signal generators.

|  | NI 5404 |
| --- | --- |
| Basic Operation |  |
| Output Modes | Standard Function (sine or square) |
| Standard Function Output |  |
| Waveform | Sine and Square (both are produced) |
| Minimum Frequency | 1 µHz |
| Maximum Frequency1 | 105 MHz |
| SYNC Duty Cycle | — |
| User-Defined Waveform Size | 16,384 samples |
| Frequency List Output |  |
| Maximum Number of Lists | — |
| Maximum List Length | — |
| Maximum Step Duration | — |
| Minimum List Length | — |
| Minimum Step Duration | — |
| Step Duration Quantum | — |
| Arbitrary Waveform Output |  |
| Write Quantum | — |
| Waveform Quantum | — |
| Minimum Waveform Size | — |
| Maximum Waveform Size | — |
| Maximum Number of Waveforms | — |
| Streaming | — |
| Onboard Signal Processing | — |
| Arbitrary Sequence Output |  |
| Minimum Sequence Length | — |
| Maximum Sequence Length | — |
| Maximum Loop Count | — |
| Maximum Number of Sequences | — |
| Streaming | — |
| Onboard Signal Processing | — |
| Script Output |  |
| Maximum Number of Script Triggers | — |
| Maximum Number of Markers | — |
| Streaming | — |
| Output Characteristics |  |
| Output Voltage (at load equal to source impedance) | sine: 1 Vpk-pk to 2 Vpk-pk square: 5 V, 3.3 V, or 1.8 V |
| Offset (at maximum gain) | — |
| Output Impedance | 50 Ω |
| Analog Path | — |
| Analog Filter Option | — |
| Filter Correction Frequency Option | — |
| Digital Filter Option | — |
| Digital Filter Interpolation Factor | — |
| DIGITAL DATA & CONTROL CONNECTOR (DDC) or Digital Pattern | — |
| Triggering and Synchronization |  |
| Trigger Modes (Frequency List and Arbitrary Waveform Generation Modes) | — |
| Trigger Sources | Immediate, PFI 0 (External), Software, RTSI_<0..7>, PXI_STAR |
| Multiple Device Synchronization | Standard Function Mode |
| Events |  |
| Ready for Start | — |
| Started | — |
| Done | — |
| Marker | — |
| Data Marker | — |
| Clocking |  |
| Sample Rate (Update Rate) before filtering and interpolation | 300 MS/s |
| Reference Clock Source | Internal (none), External (REF IN), RTSI_<0..6>, RTSI clock, PXI 10 MHz clock |
| Reference Clock Frequency | 3 MHz to 20 MHz in 1 MHz steps |
| Clock Mode (Arbitrary Waveform Generation Mode) | — |
| Sample Clock Source (Arbitrary Waveform Generation Mode) | — |
| Calibration |  |
| Self-Calibration Functions | — |
| Calibration Utility Functions | ni54xx_ functions2 |
| External Calibration Functions3 | ni54xx_CalStart and associated functions |

<sup>1</sup>Refer to the 
*device
specifications* for conditions.

<sup>2</sup>Calibration utility
functions include
ni54xx_CalFetchDate, ni54xx_CalFetchCount, ni54xx_CalFetchMiscInfo, 
ni54xx_CalStoreMiscInfo, and ni54xx_CalChangePassword.

<sup>3</sup>External calibration functions and steps vary from
device to device. For more information about calibrating your
device, refer to the calibration procedure for your device.

Parent topic:

Devices

<!--NI_TOPIC bundle=ni-fgen path=features-supported-on-pxie-5413-5423-5433-wav.html language=enus -->
## TOPIC 00059: Features Supported on PXIe-5413/5423/5433 Waveform Generators

- bundle_id: `ni-fgen`
- source_path: `features-supported-on-pxie-5413-5423-5433-wav.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/features-supported-on-pxie-5413-5423-5433-wav.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: PXIe-5413 PXIe-5423 PXIe-5433 Basic Operation Output Modes Standard Function, Frequency List, Arbitrary Waveform, Arbitrary Sequence Standard Function, Frequency List, Arbitrary Waveform, Arbitrary Sequence, Script^5 Standard Function, Frequency List, Arbitrary Waveform, Arbitrary Sequence, Script^5

### Features Supported on PXIe-5413/5423/5433 Waveform Generators

|  | PXIe-5413 | PXIe-5423 | PXIe-5433 |
| --- | --- | --- | --- |
| Basic Operation |  |  |  |
| Output Modes | Standard Function, Frequency List, Arbitrary Waveform, Arbitrary Sequence | Standard Function, Frequency List, Arbitrary Waveform, Arbitrary Sequence, Script5 | Standard Function, Frequency List, Arbitrary Waveform, Arbitrary Sequence, Script5 |
| Independent Channels | Two-channel PXIe-5413 only6 | Two-channel PXIe-5423 only6 | Two-channel PXIe-5433 only6 |
| Spurious-Free Dynamic Range | -92 dB | -92 dB | -92 dB |
| Integrated System Jitter | 435 fs | 435 fs | 435 fs |
| Standard Function Output |  |  |  |
| Waveform | Sine, Square, Triangle, Ramp Up, Ramp Down, DC, Noise, User-Defined | Sine, Square, Triangle, Ramp Up, Ramp Down, DC, Noise, User-Defined | Sine, Square, Triangle, Ramp Up, Ramp Down, DC, Noise, User-Defined |
| Minimum Frequency | 0 Hz | 0 Hz | 0 Hz |
| Maximum Frequency3 | Sine: 20 MHz, Square: 10 MHz, Ramp and Triangle: 1 MHz, User: 20 MHz, Other: 20 MHz | Sine: 40 MHz, Square: 25 MHz, Ramp and Triangle: 5 MHz, User: 40 MHz, Other: 40 MHz | Sine: 80 MHz, Square: 50 MHz, Ramp and Triangle: 50 MHz, User: 80 MHz, Other: 80 MHz |
| SYNC Duty Cycle | — | — | — |
| User-Defined Waveform Size | 8,192 samples | 8,192 samples | 8,192 samples |
| Frequency List Output |  |  |  |
| Maximum Number of Lists* | 9,999 | 9,999 | 9,999 |
| Maximum List Length* | 1,024 | 1,024 | 1,024 |
| Maximum Step Duration* | 2,814,749 s | 2,814,749 s | 2,814,749 s |
| Minimum List Length* | 1 | 1 | 1 |
| Minimum Step Duration* | 10 ns | 10 ns | 10 ns |
| Step Duration Quantum* | 10 ns | 10 ns | 10 ns |
| Digital Gain on the Fly8 | Yes | Yes | Yes |
| Arbitrary Waveform Output |  |  |  |
| Write Quantum | 1 sample | 1 sample | 1 sample |
| Waveform Quantum* | 1 sample | 1 sample | 1 sample |
| Minimum Waveform Size* | 2 samples | 2 samples | 4 samples |
| Maximum Waveform Size* 1 | 64 M samples | 64 M samples | 256 M samples |
| Maximum Number of Waveforms* | 1,048,572 | 1,048,572 | 4,194,304 |
| Streaming | — | Yes | Yes |
| Onboard Signal Processing | — | — | — |
| Arbitrary Sequence Output |  |  |  |
| Minimum Sequence Length* | 1 | 1 | 1 |
| Maximum Sequence Length* | 65,535 | 65,535 | 65,535 |
| Maximum Loop Count* | 16,777,215 | 16,777,215 | 16,777,215 |
| Maximum Number of Sequences* | 65,535 | 65,535 | 65,535 |
| Streaming | — | Yes | Yes |
| Onboard Signal Processing | — | — | — |
| Script Output |  |  |  |
| Script Mode | No | Yes | Yes |
| Maximum Number of Script Triggers | — | 4 | 4 |
| Maximum Number of Markers | — | 4 | 4 |
| Streaming | — | Yes | Yes |
| Output Characteristics |  |  |  |
| Output Voltage (at load equal to source impedance) | up to ±6 V | up to ±6 V | up to ±6 V |
| Offset (at maximum gain) | ±3 V | ±3 V | ±3 V |
| Output Impedance | 50 Ω | 50 Ω | 50 Ω |
| Analog Path | Low-Gain, High-Gain | Low-Gain, High-Gain | Low-Gain, High-Gain |
| Analog Filter Option | — | — | — |
| Filter Correction Frequency Option | Yes | Yes | Yes |
| Digital Filter Option | Yes | Yes | Yes |
| Digital Filter Interpolation Factor | — | — | — |
| DIGITAL DATA & CONTROL CONNECTOR (DDC) or Digital Pattern | — | — | — |
| Triggering and Synchronization |  |  |  |
| Trigger Modes (Frequency List and Arbitrary Waveform Generation Modes) | Single, Continuous, Stepped, Burst | Single, Continuous, Stepped, Burst | Single, Continuous, Stepped, Burst |
| Trigger Polarity | Rising Edge9 | Rising Edge9 | Rising Edge9 |
| Trigger Sources | Immediate, Software, PXI_TRIG <0..7>, PFI <0..1>, AUX 0/PFI <0..7> | Immediate, Software, PXI_TRIG <0..7>, PFI <0..1>, AUX 0/PFI <0..7> | Immediate, Software, PXI_TRIG <0..7>, PFI <0..1>, AUX 0/PFI <0..7> |
| Multiple Device Synchronization | Using NI-TClk6 (NI-FGEN 18.1 or later) | Using NI-TClk6 (NI-FGEN 18.1 or later) | Using NI-TClk6 (NI-FGEN 18.1 or later) |
| Multiple Channel Synchronization | Automatic in the same NI-FGEN session | Automatic in the same NI-FGEN session | Automatic in the same NI-FGEN session |
| Distributed TClk | Yes7 | Yes7 | Yes7 |
| Events |  |  |  |
| Ready for Start | Yes | Yes | Yes |
| Started | Yes | Yes | Yes |
| Done | Yes | Yes | Yes |
| Marker | Yes | Yes | Yes |
| Data Marker | — | — | — |
| Marker Event Pulse Width | 200 ns | 200 ns | 200 ns10 |
| Clocking |  |  |  |
| Sample Rate (Update Rate) before filtering and interpolation | 3.125 MS/s to 200 MS/s11 | 3.125 MS/s to 200 MS/s11 | 10 S/s to 250 MS/s |
| Sample Rate (Digital Filter Enabled) | 5.6 µS/s to 200 MS/s | 5.6 µS/s to 200 MS/s | 5.6 µS/s to 400 MS/s |
| Reference Clock Source12 | Internal (none), PXI Clock (PXIe_Clk100) | Internal (none), PXI Clock (PXIe_Clk100) | Internal (none), PXI Clock (PXIe_Clk100) |
| Reference Clock Frequency | 100 MHz | 100 MHz | 100 MHz |
| Clock Mode (Arbitrary Waveform Generation Mode) | High-Resolution13 | High-Resolution13 | High-Resolution13 |
| Sample Clock Source (Arbitrary Waveform Generation Mode) | Internal | Internal | Internal |
| Calibration |  |  |  |
| Self-Calibration Functions | niFgen_SelfCal | niFgen_SelfCal | niFgen_SelfCal |
| Calibration Utility Functions | niFgen_ functions4 | niFgen_ functions4 | niFgen_ functions4 |
| External Calibration Functions2 | ni5433_ functions | ni5433_ functions | ni5433_ functions |

<sup>*</sup>You can get the value of this characteristic by calling a query function or by
 reading an attribute. NI recommends that your programs query or read the characteristic rather
 than depend on a certain value.

<sup>1</sup>Varies by waveform generator and the amount of memory. Memory use is a function
 of the number and size of waveforms and (in Arbitrary Sequence mode) the number and length of
 sequences. Typically, waveforms use most of the memory, but if you have a very large number of
 sequences, the available waveform memory is reduced.

<sup>2</sup>External calibration functions and steps vary by waveform generator. Refer to the
 *calibration procedure* for your waveform generator for more information.

<sup>3</sup>Refer to the *specifications* for your waveform generator for
 conditions.

<sup>4</sup>The niFgen Get Ext Cal Last Temp VI and niFgen Restore Last Ext Cal Constants VI
 are not supported.

<sup>5</sup>if/else/end if and break script instructions
 are not supported.

<sup>6</sup>Synchronization with NI-TClk is supported with a single NI-FGEN session per
 waveform generator. Synchronization with NI-TClk is not supported with multiple channel-based
 NI-FGEN sessions to a single multichannel waveform generator. Refer to the
 Synchronization topic for your PXIe-5413/5423/5433 waveform generator for
 more information.

<sup>7</sup>Refer to the Distributed
 TClk topic in the
 NI-TClk Synchronization Help for information about distributed TClk.

<sup>8</sup>Using digital gain on the fly, you can digitally scale a waveform while
 generating. However, you cannot change digital gain on the fly if the flatness correction
 property is enabled. This is because flatness correction requires digital correction
 coefficients to be pre-computed.

<sup>9</sup>Because the devices only use rising edge triggers, properties such as Active
 Level and Marker Initial State are no longer relevant. These properties are not supported on
 the devices.

<sup>10</sup>Starting from NI-FGEN 2026 Q2, PXIe-5433 supports configurable marker event
 pulse width with a default value of 200 ns, within a range of 20 ns to 40.959 µs, using the
 Marker Event Pulse Width and Marker Event Pulse Width Units properties.

<sup>11</sup>You can output lower frequency signals with the PXIe-5413/5423 by increasing the
 number of points in the desired waveform, which helps produce a smoother signal with faster
 slew rate.

<sup>12</sup>External clock sources are not supported.

<sup>13</sup>High-resolution clock mode uses direct digital synthesis to generate very fine
 resolution increments on the order of µHz. This provides finer control over possible sample
 rates that can be used.

Parent topic:

Devices

<!--NI_TOPIC bundle=ni-fgen path=features-supported-on-smc-devices.html language=enus -->
## TOPIC 00060: Features Supported on SMC Devices

- bundle_id: `ni-fgen`
- source_path: `features-supported-on-smc-devices.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/features-supported-on-smc-devices.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: NI 5402/5406/5412/5421/5422/5441/5442/5450/5451 The following table shows the features supported by NI signal generators based on the SMC technology. NI 5402 NI 5406 NI 5412 NI 5421 NI 5422 NI 5441 NI 5442 NI 5450 NI 5451 Basic Operation Output Modes Standard Function, Frequency List Standard Func

### Features Supported on SMC Devices

#### NI 5402/5406/5412/5421/5422/5441/5442/5450/5451

The following table shows the features supported by
NI signal generators based on the SMC
 technology.

|  | NI 5402 | NI 5406 | NI 5412 | NI 5421 | NI 5422 | NI 5441 | NI 5442 | NI 5450 | NI 5451 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Basic Operation |  |  |  |  |  |  |  |  |  |
| Output Modes | Standard Function, Frequency List | Standard Function, Frequency List | Standard Function, Arbitrary Waveform, Arbitrary Sequence | Standard Function, Arbitrary Waveform, Arbitrary Sequence, Script | Standard Function, Arbitrary Waveform, Arbitrary Sequence, Script | Standard Function, Arbitrary Waveform, Arbitrary Sequence, Script, Frequency List | Standard Function, Arbitrary Waveform, Arbitrary Sequence, Script, Frequency List | Arbitrary Waveform, Arbitrary Sequence, Script, Standard Function6 | Arbitrary Waveform, Arbitrary Sequence, Script, Standard Function |
| Standard Function Output |  |  |  |  |  |  |  |  |  |
| Waveform | Sine, Square, Triangle, Ramp Up, Ramp Down, DC, Noise, User-Defined | Sine, Square, Triangle, Ramp Up, Ramp Down, DC, Noise, User-Defined | Sine, Square, Triangle, Ramp Up, DC, Noise, User-Defined | Sine, Square, Triangle, Ramp Up, Ramp Down, DC, Noise, User-Defined | Sine, Square, Triangle, Ramp Up, Ramp Down, DC, Noise, User-Defined | Sine, Square, Triangle, Ramp Up, Ramp Down, DC, Noise, User-Defined | Sine, Square, Triangle, Ramp Up, Ramp Down, DC, Noise, User-Defined | 6 Sine, Square, Triangle, Ramp Up, Ramp Down, DC, Noise, User-Defined | Sine, Square, Triangle, Ramp Up, Ramp Down, DC, Noise, User-Defined |
| Minimum Frequency | 0 Hz | 0 Hz | <1 mHz 5 | <1 mHz 5 | <1 mHz 5 | 0 Hz | 0 Hz | 0 Hz6 | 0 Hz |
| Maximum Frequency 4 | Sine: 20 MHz, Square: 20 MHz, User-Defined: 20 MHz, Other: 1 MHz | Sine: 40 MHz, Square: 40 MHz, User-Defined: 40 MHz, Other: 5 MHz | Sine: 20 MHz, Square: 5 MHz, Other: 1 MHz | Sine: 43 MHz, Square: 25 MHz, Other: 5 MHz | Sine: 80 MHz, Square: 50 MHz, Other: 10 MHz | Sine: 43 MHz, Square: 25 MHz, User-Defined: 43 MHz, Other: 5 MHz | Sine: 43 MHz, Square: 25 MHz, User-Defined: 43 MHz, Other: 5 MHz | 6Sine: 135 MHz with filter enabled, Square: 150 MHz, Triangle: 20 MHz, 5 MHz with filter enabled, Ramp: 20 MHz User-Defined: 135 MHz | Sine: 135 MHz with filter enabled, Square: 150 MHz, Triangle: 20 MHz, 5 MHz with filter enabled, Ramp: 20 MHz User-Defined: 135 MHz |
| SYNC Duty Cycle | 20% to 80% for square, 50% for all other | 20% to 80% for square, 50% for all other | — | — | — | — | — | — | — |
| User-Defined Waveform Size | 16,384 samples | 16,384 samples | Variable 1 | Variable 1 | Variable 1 | 16,384 samples | 32,768 samples | 32,768 samples6 | 32,768 samples |
| Frequency List Output |  |  |  |  |  |  |  |  |  |
| Maximum Number of Lists * | 9,999 lists | 9,999 lists | — | — | — | 9,999 lists | 9,999 lists | — | — |
| Maximum List Length * | 58,253 steps | 58,253 steps | — | — | — | 932,066 steps | 932,066 steps | — | — |
| Maximum Step Duration * | 21 s | 21 s | — | — | — | 21 s | 21 s | — | — |
| Minimum List Length * | 1 steps | 1 steps | — | — | — | 1 steps | 1 steps | — | — |
| Minimum Step Duration * | 1.28 µs | 1.28 µs | — | — | — | 1.28 µs | 1.28 µs | — | — |
| Step Duration Quantum * | 80 ns | 80 ns | — | — | — | 80 ns | 80 ns | — | — |
| Arbitrary Waveform Output |  |  |  |  |  |  |  |  |  |
| Write Quantum | 64 samples or 32 complex samples | 64 samples or 32 complex samples | 64 samples or 32 complex samples | 64 samples or 32 complex samples | 64 samples or 32 complex samples | 64 samples or 32 complex samples | 1 sample | 1 sample | 1 sample |
| Waveform Quantum * | — | — | 4 samples | 4 samples | 4 samples | 4 samples | 1 sample | 2 samples | 2 samples |
| Minimum Waveform Write Size * | — | — | 4 samples | 4 samples | 4 samples | 4 samples | 4 samples | 4 samples | 4 samples |
| Maximum Waveform Write Size * 1 | — | — | 4 M, 16 M, 128 M samples | 4 M, 16 M, 128 M, 256 M samples | 4 M, 16 M, 128 M, 256 M samples | 16 M, 128 M, 256 M samples | 16 M, 128 M, 256 M samples | 67 M, 108 M, 352 M samples | 67 M, 108 M, 352 M samples |
| Maximum Number of Waveforms * | — | — | 2,097,151 | 2,097,151 | 2,097,151 | 2,097,151 | 2,097,151 | 2,097,151 | 2,097,151 |
| Streaming | — | — | — | Yes | Yes | Yes | Yes | Yes | Yes |
| Onboard Signal Processing | — | — | — | — | — | IF Mode | IF Mode | Baseband Mode | Baseband Mode, IF Mode |
| Arbitrary Sequence Output |  |  |  |  |  |  |  |  |  |
| Minimum Sequence Length * | — | — | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| Maximum Sequence Length * | — | — | 16,777,205 1 | 16,777,205 1 | 16,777,205 1 | 16,777,205 1 | 16,777,205 1 | 16,777,205 1 | 16,777,205 1 |
| Maximum Loop Count * | — | — | 16,777,215 | 16,777,215 | 16,777,215 | 16,777,215 | 16,777,215 | 16,777,215 | 16,777,215 |
| Maximum Number of Sequences * | — | — | 2,097,151 1 | 2,097,151 1 | 2,097,151 1 | 2,097,151 1 | 2,097,151 1 | 2,097,151 1 | 2,097,151 1 |
| Streaming | — | — | — | Yes | Yes | Yes | Yes | Yes | Yes |
| Onboard Signal Processing | — | — | — | — | — | Yes | Yes | Yes | Yes |
| Script Output |  |  |  |  |  |  |  |  |  |
| Maximum Number of Script Triggers | — | — | — | 4 | 4 | 4 | 4 | 4 | 4 |
| Maximum Number of Markers | — | — | — | 4 | 4 | 4 | 4 | 4 | 4 |
| Streaming | — | — | — | Yes | Yes | Yes | Yes | Yes | Yes |
| Output Characteristics |  |  |  |  |  |  |  |  |  |
| Output Voltage (at load equal to source impedance) | up to ±5 V | up to ±5 V | up to ±6 V | up to ±6 V | up to ±6 V | up to ±6 V | up to ±1 V | up to ±1 V | ±2.5 V single ended, ±5 V differential |
| Offset (at maximum gain) | ±5 V pk | ±5 V pk | ±3 V | ±3 V | ±6 V | ±3 V | ±0.5 V | 0 V | 1 V single ended, 2 V differential |
| Output Impedance | 50 Ω, 75 Ω | 50 Ω, 75 Ω | 50 Ω, 75 Ω | 50 Ω, 75 Ω | 50 Ω, 75 Ω | 50 Ω, 75 Ω | 50 Ω, 75 Ω | 50 Ω | 50 Ω |
| Analog Path | Main, Fixed Low-Gain, Fixed High-Gain | Main, Fixed Low-Gain, Fixed High-Gain | Main, Fixed Low-Gain, Fixed High-Gain | Main, Direct, Fixed Low-Gain, Fixed High-Gain | Main, Direct, Fixed Low-Gain, Fixed High-Gain | Main, Direct, Fixed Low-Gain, Fixed High-Gain | Main, Direct | Direct | Main, Direct |
| Analog Filter Option | Yes | Yes | No | Yes | Yes | Yes | Yes | — | Yes (Main Path only) |
| Flatness Correction for Sine Waveforms | Yes | Yes | — | — | — | — | — | Yes | Yes |
| Flatness Correction for Arbitrary Waveforms | — | — | — | — | — | — | — | Yes | Yes |
| Digital Filter Option | Yes | Yes | Yes | Yes | — | Yes | Yes | — | — |
| Digital Filter Interpolation Factor | 2 or 4 (automatic for Standard Function and Frequency List modes) | 2 or 4 (automatic for Standard Function and Frequency List modes) | 2, 4, or 8 (maximum of 400 MS/s) or automatic | 2, 4, or 8 (maximum of 400 MS/s) or automatic | — | 2, 4, or 8 (maximum of 400 MS/s) or automatic | 2, 4, or 8 (maximum of 400 MS/s) or automatic | — | — |
| DIGITAL DATA & CONTROL CONNECTOR (DDC) or Digital Pattern | — | — | — | Optional 1 | Optional 1 | Optional 1 | — | — | — |
| Triggering and Synchronization |  |  |  |  |  |  |  |  |  |
| Trigger Modes (Frequency List and Arbitrary Waveform Generation Modes) | Single, Continuous, Stepped, Burst | Single, Continuous, Stepped, Burst | Single, Continuous, Stepped, Burst | Single, Continuous, Stepped, Burst | Single, Continuous, Stepped, Burst | Single, Continuous, Stepped, Burst | Single, Continuous, Stepped, Burst | Single, Continuous, Stepped, Burst | Single, Continuous, Stepped, Burst |
| Trigger Sources | Immediate, External, Software, RTSI_<0..7>, PXI_STAR, PFI <0..1> | Immediate, External, Software, RTSI_<0..7>, PXI_STAR, PFI <0..1> | Immediate, External, Software, RTSI_<0..7>, PXI_STAR, PFI <0..1> | Immediate, External, Software, RTSI_<0..7>, PXI_STAR, PFI <0..1> | Immediate, External, Software, RTSI_<0..7>, PXI_STAR, PFI <0..1> | Immediate, External, Software, RTSI_<0..7>, PXI_STAR, PFI <0..1> | Immediate, External, Software, RTSI_<0..7>, PXI_STAR, PFI <0..1> | Immediate, External, Software, RTSI_<0..7>, PFI <0..1> | Immediate, External, Software, RTSI_<0..7>, PFI <0..1> |
| Multiple Device Synchronization | Using NI-TClk | Using NI-TClk | Using NI-TClk except for Standard Function mode | Using NI-TClk except for Standard Function mode | Using NI-TClk except for Standard Function mode | Using NI-TClk | Using NI-TClk | Using NI-TClk | Using NI-TClk |
| Events |  |  |  |  |  |  |  |  |  |
| Ready for Start | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Started | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Done | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Marker | — | — | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Data Marker | — | Yes | — | Yes | Yes | Yes | Yes | Yes | Yes |
| Clocking |  |  |  |  |  |  |  |  |  |
| Sample Rate (Update Rate) before filtering and interpolation | 100 MS/s | 100 MS/s | Internal Sample clock: 10 S/s to 100 MS/s, External Sample clock: 10 S/s to 105 MS/s | Internal Sample clock: 10 S/s to 100 MS/s, External Sample clock: 10 S/s to 105 MS/s | 5 MS/s to 200 MS/s | Internal Sample clock: 10 S/s to 100 MS/s, External Sample clock: 10 S/s to 105 MS/s | Internal Sample clock: 10 S/s to 100 MS/s, External Sample clock: 10 S/s to 105 MS/s | Internal Sample clock: 12.2 kS/s to 400 MS/s, External Sample clock: 10 MS/s, 20 MS/s to 400 MS/s | Internal Sample clock: 12.2 kS/s to 400 MS/s, External Sample clock: 10 MS/s, 20 MS/s to 400 MS/s |
| Reference Clock Source | Internal (none), External (CLK IN), PXI 10 MHz clock (PXI only), RTSI_7 (RTSI clock; PCI only), Onboard (PCI only) | Internal (none), External (CLK IN), PXI 10 MHz clock (PXI only), RTSI_7 (RTSI clock; PCI only), Onboard (PCI only) | Internal (none), External (CLK IN), PXI 10 MHz clock (PXI only), RTSI_7 (RTSI clock; PCI only), Onboard (PCI only) | Internal (none), External (CLK IN), PXI 10 MHz clock (PXI only), RTSI_7 (RTSI clock; PCI only), Onboard (PCI only) | Internal (none), External (CLK IN), PXI 10 MHz clock | Internal (none), External (CLK IN), PXI 10 MHz clock | Internal (none), External (CLK IN), PXI 10 MHz clock | Internal (none), External (CLK IN), PXI 10 MHz clock | Internal (none), External (CLK IN), PXI 10 MHz clock |
| Reference Clock Frequency | 5 MHz to 20 MHz in 1 MHz steps | 5 MHz to 20 MHz in 1 MHz steps | 5 MHz to 20 MHz in 1 MHz steps | 5 MHz to 20 MHz in 1 MHz steps | 5 MHz to 20 MHz in 1 MHz steps | 5 MHz to 20 MHz in 1 MHz steps | 5 MHz to 20 MHz in 1 MHz steps | 1 to 100 MHz in 1 MHz steps, 102 MHz to 200 MHz in 2 MHz steps, 204 MHz to 400 MHz in 4 MHz steps | 1 to 100 MHz in 1 MHz steps, 102 MHz to 200 MHz in 2 MHz steps, 204 MHz to 400 MHz in 4 MHz steps |
| Clock Mode (Arbitrary Waveform Generation Mode) | — | — | Divide-Down, High-Resolution, Automatic | Divide-Down, High-Resolution, Automatic | Divide-Down, High-Resolution, Automatic | Divide-Down, High-Resolution, Automatic | Divide-Down, High-Resolution, Automatic | High-Resolution, Automatic | High-Resolution, Automatic |
| Sample Clock Source (Arbitrary Waveform Generation Mode) | — | — | Internal, External (CLK IN), PXI_STAR (PXI only), RTSI_<0..7> | Internal, External (CLK IN), DDC CLK IN 1 , PXI_STAR (PXI only), RTSI_<0..7> | Internal, External (CLK IN), DDC CLK IN 1 , PXI_STAR | Internal, External (CLK IN), DDC CLK IN 1 , PXI_STAR | Internal, External (CLK IN), PXI_STAR | Internal, External (CLK IN) | Internal, External (CLK IN) |
| Calibration |  |  |  |  |  |  |  |  |  |
| Self-Calibration Functions | niFgen_SelfCal, niFgen_RestoreLast ExtCalConstants | niFgen_SelfCal, niFgen_RestoreLast ExtCalConstants | niFgen_SelfCal, niFgen_RestoreLast ExtCalConstants | niFgen_SelfCal, niFgen_RestoreLast ExtCalConstants | niFgen_SelfCal, niFgen_RestoreLast ExtCalConstants | niFgen_SelfCal, niFgen_RestoreLast ExtCalConstants | niFgen_SelfCal, niFgen_RestoreLast ExtCalConstants | niFgen_SelfCal, niFgen_RestoreLast ExtCalConstants | niFgen_SelfCal, niFgen_RestoreLast ExtCalConstants |
| Calibration Utility Functions 2 | niFgen_ functions | niFgen_ functions | niFgen_ functions | niFgen_ functions | niFgen_ functions | niFgen_ functions | niFgen_ functions | niFgen_ functions | niFgen_ functions |
| External Calibration Functions 3 | niFgen_InitExtCal and associated functions | niFgen_InitExtCal and associated functions | niFgen_InitExtCal and associated functions | niFgen_InitExtCal and associated functions | niFgen_InitExtCal and associated functions | niFgen_InitExtCal and associated functions | niFgen_InitExtCal and associated functions | niFgen_InitExtCal and associated functions | niFgen_InitExtCal and associated functions |

<sup>*</sup>You can get the value of this characteristic by calling
a query function or by reading an attribute. NI recommends
that your programs query or read the characteristic rather than
depend on a certain value.

<sup>1</sup>Varies with the device model or the amount of memory on
the device. Memory use is a function of the number and size of
waveforms and (in Arbitrary Sequence mode) the number and length of
sequences. Typically, waveforms use most of the memory, but if you
have a very large number of sequences, the available waveform
memory is reduced.

<sup>2</sup>Calibration utility functions include

niFgen_GetSelfCalSupported, niFgen_GetSelfCalLastDateAndTime, niFgen_GetExtCalLastDateAndTime, niFgen_GetSelfCalLastTemp, niFgen_GetExtCalLastTemp, niFgen_GetExtCalRecommendedInterval, niFgen_ChangeExtCalPassword, niFgen_SetCalUserDefinedInfo, niFgen_GetCalUserDefinedInfo, niFgen_GetCalUserDefinedInfoMaxSize, and niFgen_ReadCurrentTemperature.

<sup>3</sup>External calibration functions and steps vary from
device to device. For more information about calibrating your
device, refer to the *calibration procedure* for your device.

<sup>4</sup>Refer to the 
*device
specifications* for conditions.

<sup>5</sup>The minimum frequency available on these devices
depends on the memory size of the device, as well as the value of
the 
NIFGEN_ATTR_FUNC_MAX_BUFFER_SIZE attribute.

<sup>6</sup>This feature is only supported on the NI 5450 module revision C and later. To determine the revision letter of your NI 5450, query the Module Revision property or the NIFGEN_ATTR_MODULE_REVISION attribute.

Parent topic:

Devices

Related concepts:

- Standard Function Mode

<!--NI_TOPIC bundle=ni-fgen path=features.html language=enus -->
## TOPIC 00061: Features

- bundle_id: `ni-fgen`
- source_path: `features.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/features.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: This section provides instructions for using some of the features of NI signal generators.

### Features

This section provides instructions for using some of the features of NI signal generators.

Parent topic:

Programming

<!--NI_TOPIC bundle=ni-fgen path=filtering-and-interpolation.html language=enus -->
## TOPIC 00062: Filtering and Interpolation

- bundle_id: `ni-fgen`
- source_path: `filtering-and-interpolation.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/filtering-and-interpolation.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: All NI signal generators use a digital-to-analog converter (DAC) to generate the signals or waveforms that eventually appear at the output connector. These generated signals have a number of discrete voltage levels dependent on the number of bits in the DAC. A digital waveform must be updated at lea

### Filtering and Interpolation

All NI signal generators use a digital-to-analog converter (DAC) to generate the signals or waveforms that eventually appear at the output connector. These generated signals have a number of discrete voltage levels dependent on the number of bits in the DAC.

A digital waveform must be updated at least twice as fast as the bandwidth of the desired analog
 signal to be accurately generated (Shannon's Sampling Theorem). Even though the
 theoretical requirement for sample clock, f<sub>s</sub>, is twice that of the signal
 bandwidth, f<sub>o</sub>, images are introduced in the output signal at |f
 <sub>o</sub> ± nf<sub>s</sub>|, as shown in the following
 figure.

[IMAGE alt='image' src='GUID-48A891CF-3E91-42F6-9EC9-10D76B8D6D1B-a5.gif']

The images in the previous figure degrade the spectral purity of the signal, creating the need to
 filter these images out of the signal.

To create quality signals, all NI signal generators can lowpass filter the generated signal. A lowpass filter can smooth the raw DAC output. The filter removes high-frequency aliased components that are introduced through the digital generation of the signal. You can implement the lowpass filter through both analog and digital filters.

Designing an analog filter that rejects the images and yet gets maximum output bandwidth (0 to
 0.43f<sub>s</sub>) is difficult and is represented by the curve Analog Filter 1
 in the following figure. Analog Filter 2 represents a more practical filter. This
 filter is not as aggressive as Analog Filter 1. Analog Filter 2 does not filter out
 the images near f<sub>s</sub>, but it does reject all the others. Analog filters have
 trade-offs between the roll-off of the attenuation after the 3 dB point and the
 flatness of the attenuation before the 3 dB point.

Another aspect of the analog filter is group delay—the amount of time needed for a signal having
 finite time duration, such as a pulse, to pass through the analog filter. Ideally, in
 an analog filter with linear group delay, all frequencies present in the signal
 should have the same time delay so that the signal is not distorted.

The third filter, Analog Filter 3, has a much higher 3 dB point than the first two analog
 filters. Because of the higher 3 dB point, the filter is very nearly flat in the
 passband (0 to 0.43f<sub>s</sub>). Analog Filter 3 does not filter the images
 produced at f<sub>s</sub> and 2f<sub>s</sub> at all, but this shortcoming can be
 alleviated with a digital interpolation filter.

[IMAGE alt='image' src='GUID-F3EC51F3-0A8F-4E2E-B9E9-7A958BE38C3B-a5.gif']

To ease the requirements of the analog filter and to get more output bandwidth, NI signal
 generators use a halfband digital filter to interpolate one, three, or seven samples
 between every two waveform samples at two times, four times, and eight times the
 sample frequency, f<sub>s</sub>. Also, the DAC operates at an effective sampling rate
 that is two times (2f<sub>s</sub>), four times (4f<sub>s</sub>), and eight times
 (8f<sub>s</sub>) the sample frequency—specifically, the rate at which the data
 is clocked from the memory into the DAC.

In the following figure, the two times interpolating filter is used and the effective sample rate of the DAC is 2f<sub>s</sub>. The images at f<sub>s</sub> ± f<sub>o</sub> are no longer an issue, and the images are now at |2f<sub>s</sub> ± f<sub>o</sub>|.

[IMAGE alt='image' src='GUID-40EBCE70-98AC-40E0-B41C-0DA9897DD9F7-a5.gif']

Now, Analog Filter 2 can easily filter out all the images due to the digital generation of the
 signal. This behavior is seen in the frequency domain representation in the previous
 figure and in the time domain representation in the following figure.

[IMAGE alt='image' src='GUID-A1AF3FAC-2680-4E93-B567-EEB0B607944A-a5.gif']

Note

Using two times interpolation filtering with a DAC effective sample rate of 2f<sub>s</sub>
 eliminates images well and generates a good signal. However, increasing the
 interpolation filter to 4 further improves the output signal.

The following figure shows a signal image with four times interpolation, and the effective DAC
 sample rate at 4f<sub>s</sub>. The images are shifted up to 4f<sub>s</sub>, and well
 above the cutoff frequency of Analog Filter 3. This configuration eliminates the
 spectral images and has a filter that is maximally flat within the passband. This
 configuration approaches an ideal design in digitally generating spectrally pure
 waveforms.

[IMAGE alt='image' src='GUID-19DBE295-7AED-4C22-836D-2E7251B4F7B7-a5.gif']

To generate the most spectrally pure signals using the digital filter, use the highest interpolation factor possible.

Parent topic:

Waveform Fundamentals

Related concepts:

- Nyquist and Shannon's Sampling Theorems

<!--NI_TOPIC bundle=ni-fgen path=flow-control.html language=enus -->
## TOPIC 00063: Flow Control

- bundle_id: `ni-fgen`
- source_path: `flow-control.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/flow-control.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: When streaming data between two peers, the writer peer must have flow control credits to move data over the bus to the reader peer. The reader peer issues credits to the writer peer through control messages across the bus when space is available in the configured endpoint for the reader peer. There

### Flow Control

When streaming data between two peers, the writer peer must have flow control credits to move data over the bus to the reader peer. The reader peer issues credits to the writer peer through control messages across the bus when space is available in the configured endpoint for the reader peer. There are two methods of controlling this flow: automatic and manual.

#### Automatic Flow Control

By default, the signal generator automatically communicates with the writer peer to issue flow control credits. However, you must complete the following steps to configure your stream and begin issuing flow control credits.

1. Configure NI-P2P with information regarding each endpoint to link the endpoints into a stream, using the niP2P Create Peer to Peer Stream VI or the nip2pCreateStream function. You must specify both a reader and writer endpoint handle.
2. Use the niFgen Get Stream Endpoint Handle VI or the niFgen_GetStreamEndpointHandle function to get the signal generator reader handle and the appropriate handle from the writer peer API.
3. Enable the stream using the niP2P Enable Peer to Peer Stream VI or the nip2pEnableStream function. After you enable the stream, the signal generator begins issuing credits to the writer peer.

The signal generator issues credits in the following two ways:

- When the stream is initially enabled, the peer issues credits equal to the value of the Data Transfer Permission Initial Credits property or the NIFGEN_ATTR_P2P_DATA_TRANSFER_PERMISSION_INITIAL_CREDITS . If this property or attribute is not set, the signal generator issues a default value equal to the depth of the endpoint to the peer to minimize the chance of underflowing the signal generator. (Underflow can be caused by heavy bus traffic.)
- As data flows from the endpoint to the physical channel(s) on the signal generator, additional credits are issued to the writer peer. These credits are issued in intervals equal to the value of the Data Transfer Permission Interval property or the NIFGEN_ATTR_P2P_DATA_TRANSFER_PERMISSION_INTERVAL attribute and issued only when an amount of data greater than or equal to this value is generated at the physical channels on the signal generator.

Note

niFgen_WriteP2PEndpointI16

Parent topic:

Configuring a Peer-to-Peer Stream

<!--NI_TOPIC bundle=ni-fgen path=frequency-domain-fundamentals.html language=enus -->
## TOPIC 00064: Frequency Domain Fundamentals

- bundle_id: `ni-fgen`
- source_path: `frequency-domain-fundamentals.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/frequency-domain-fundamentals.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Expand this book to view the frequency domain topics, or click one of the following links: SFDR —Spurious–free dynamic range THD —Total harmonic distortion SINAD —Signal-to-noise-and-distortion ratio ENOB —Effective number of bits

### Frequency Domain Fundamentals

Expand this book to view the frequency domain topics, or click one of the following links:

*SFDR* —Spurious–free dynamic range

*THD* —Total harmonic distortion

*SINAD* —Signal-to-noise-and-distortion ratio

*ENOB* —Effective number of bits

Parent topic:

Waveform Fundamentals

Related concepts:

- SFDR
- THD
- SINAD
- ENOB

<!--NI_TOPIC bundle=ni-fgen path=frequency-hopping-and-sweeping.html language=enus -->
## TOPIC 00065: Frequency Hopping and Sweeping

- bundle_id: `ni-fgen`
- source_path: `frequency-hopping-and-sweeping.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/frequency-hopping-and-sweeping.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can define a staging list for performing frequency hops and sweeps. The entire staging list uses the same waveform loaded into the lookup memory. All stages are phase-continuous and differ only with the frequency generated. Frequency Sweeping A frequency sweep is the continuous generation of a s

### Frequency Hopping and Sweeping

You can define a staging list for performing frequency hops and sweeps. The entire staging list
 uses the same waveform loaded into the lookup memory. All stages are phase-continuous
 and differ only with the frequency generated.

#### Frequency Sweeping

A *frequency sweep* is the continuous generation of a single waveform with
 a frequency that changes in a linear way.

The following are the basic elements
 used to control the generation of a frequency sweep:

Start frequency

End frequency

Number of frequency steps

Frequency step duration

You can use these elements to programmatically create a frequency
 sweep.

In frequency list output mode, you can use the Fgen Sweep Generator
 example in LabVIEW or LabWindows/CVI.

A simple example of a frequency sweep is
 a chirp waveform—a sine wave produced with a linear sweep of frequency. Refer to the
 *NI Analog Waveform Editor Help* for information about creating and
 configuring a chirp waveform using the AWE.

#### Frequency Hopping

A *frequency hop* is applied in an order defined by the user. A
 *frequency hop* order differs from a *frequency sweep*,
 which the system applies in a linear succession. You can use frequency list output
 mode or arbitrary sequence output mode to implement frequency hopping.

Parent topic:

Waveform Fundamentals

<!--NI_TOPIC bundle=ni-fgen path=frequency-list-mode.html language=enus -->
## TOPIC 00066: Frequency List Mode

- bundle_id: `ni-fgen`
- source_path: `frequency-list-mode.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/frequency-list-mode.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: In Frequency List output mode, the device generates a standard function using a list of frequencies you define. A frequency list is composed of steps, each one with a frequency/duration pair. Frequency lists are commonly used for frequency sweeps and frequency-shift-keying (FSK) applications. Refer

### Frequency List Mode

Note

Features Supported

The following example shows a frequency list and the generated waveform when Single trigger mode is selected. The *trigger mode* affects the timing and behavior of the generation.

| Step | Frequency | Duration |
| --- | --- | --- |
| 0 | 3.0 Hz | 1.0 s |
| 1 | 6.0 Hz | 0.9 s |
| 2 | 0.5 Hz | 0.75 s |
| 3 | 9.0 Hz | 1.1 s |

[IMAGE alt='image' src='GUID-BFB91659-0FE2-4FC1-996D-51ABD4E07C85-a5.gif']

Related Topics

*Configuring Frequency List Mode*

Parent topic:

Output Modes

Related concepts:

- Features Supported on SMC Devices
- Trigger Modes
- Configure Frequency List Mode

<!--NI_TOPIC bundle=ni-fgen path=general-programming-flow.html language=enus -->
## TOPIC 00067: General Programming Flow

- bundle_id: `ni-fgen`
- source_path: `general-programming-flow.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/general-programming-flow.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following diagram shows the general programming flow for applications using NI-FGEN. Not all NI-FGEN VIs appear in the general programming flow as some VIs are considered utility VIs, which perform tasks such as resetting the device and returning the revision number of NI-FGEN. Refer to the NI-F

### General Programming Flow

The following diagram shows the general programming
flow for applications using NI-FGEN. Not all NI-FGEN VIs appear in
the general programming flow as some VIs are considered utility
VIs, which perform tasks such as resetting the device and returning
the revision number of NI-FGEN. Refer to the 
NI-FGEN LabVIEW
Reference or the 
NI-FGEN C Function
Reference for more information.

[IMAGE alt='image' src='GUID-7AD6831A-4983-43DD-95C8-58B52BA8238A-a5.gif']

Parent topic:

Programming

<!--NI_TOPIC bundle=ni-fgen path=generate.html language=enus -->
## TOPIC 00068: generate

- bundle_id: `ni-fgen`
- source_path: `generate.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/generate.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the generate instruction to describe which waveform to generate. Usage Generate a waveform written to the device with the Write Named Waveform VI or function for your driver.generate <waveform name> Generate a subset of the named waveform.generate <waveform name> subset (<start position>, <lengt

### generate

Use the generate instruction to describe
 which waveform to generate.

#### Usage

- Generate a waveform written to the device with the Write Named
 Waveform VI or function for your driver. generate
 <waveform name>
- Generate a subset of the named waveform. generate <waveform name> subset
 (<start position>, <length>) Specify start position and length
 in samples.
- Generate the waveform and generate a Marker event when a position within the waveform is
 generated. generate <waveform name> marker0
 (<position 1>, <position 2>, ... ,
 <position n> Specify each position in
 samples. Use the Export Signal VI or function for your driver to
 specify the destination terminal of the marker. Marker position is zero-based. For
 example, 0 refers to the first point in the waveform,
 999 refers to the 1,000th point in the waveform, and so on.
- Generate a subset of the named waveform and generate a Marker event when a position
 within the waveform is generated. generate <waveform
 name> subset(<start position>,
 <length>) marker0 (<list of
 positions>) Specify the positions and length in samples. When a subset and markers are
 specified in the same generate instruction, the marker positions are
 relative to the subset.

#### Generating Waveforms

Assume myWfm in each example has 1,024 samples.

- Generate myWfm . generate myWfm
- Generate 10 samples of myWfm starting at sample
 40. generate myWfm subset (40, 10)
- Generate myWfm and generate a marker at the start of the waveform
 (sample 0). generate myWfm marker0 (0)
- Generate myWfm and generate a marker at positions 10 and
 80. generate myWfm marker0 (10, 80)
- Generate 10 samples of myWfm starting at sample 40, and generate a
 marker at position 6 of the
 subset. generate myWfm subset (40, 10) marker0 (6)

Parent topic:

Scripting Instructions

<!--NI_TOPIC bundle=ni-fgen path=generating-composite-video-signals.html language=enus -->
## TOPIC 00069: Generating Composite Video Signals

- bundle_id: `ni-fgen`
- source_path: `generating-composite-video-signals.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/generating-composite-video-signals.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: A composite video signal embeds all the components needed to generate a video signal in a single signal. The following three main components together form a composite signal: The luma signal (or luminance)—Contains the intensity (brightness or darkness) information of the video image The chroma sign

### Generating Composite Video Signals

A composite video signal embeds all the components needed to generate a video signal in a single signal. The following three main components together form a composite signal:

- The luma signal (or luminance)—Contains the intensity (brightness or darkness) information of the video image
- The chroma signal—Contains the color information of the video image
- The synchronization signal—Controls the scanning of the signal on a display such as the TV screen

The monochrome composite signal is built of two components: luma and synchronization. The luma signal, which is usually called the Y signal, is shown in the following figure.

[IMAGE alt='image' src='GUID-11D6766E-C308-4989-98CD-A228F19E8CAB-a5.gif']

#### Monochrome Composite Video Signal (Luma Steps from White to Black)

The chroma signal by itself, which is usually called the C signal, is shown in the following figure.

[IMAGE alt='image' src='GUID-4E8CA9C6-ED6F-4477-87C5-4CCC676B6AA0-a5.gif']

#### Color Information Signal for a Color Bar Line (Including the Color Burst)

The composite color video signal, often called the Color Video, Blanking, and Sync (CVBS) signal, is the sum of Y and C.

CVBS = Y + C

[IMAGE alt='image' src='GUID-04E13F23-3148-4E9B-9D3C-360B1859209E-a5.gif']

#### Color Composite Video Signal for a Color Bar Line

The two components Y and C can also be distributed separately as two independent signals. These two signals together are called either Y/C or S-video.

Y/C = S-video

Parent topic:

Video Signal Fundamentals

<!--NI_TOPIC bundle=ni-fgen path=gray-scale-image-and-extracted-line-profile.html language=enus -->
## TOPIC 00070: Gray Scale Image and Extracted Line Profile

- bundle_id: `ni-fgen`
- source_path: `gray-scale-image-and-extracted-line-profile.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/gray-scale-image-and-extracted-line-profile.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Complete NSTC Frame Scan image simulates the video display that would appear on a television screen if the following conditions are true: The television can show the entire line instead of just the active image part. The television does not interlace the two fields to form a complete image frame

### Gray Scale Image and Extracted Line Profile

The *Complete NSTC Frame Scan* image simulates the video display that would appear on a television screen if the following conditions are true:

- The television can show the entire line instead of just the active image part.
- The television does not interlace the two fields to form a complete image frame, but instead displays a progressive scanning, line by line, of the entire frame.

The scanning starts (line-by-line from top to bottom) with a number of lines that represent the vertical synchronization pattern for the odd field. Immediately after the vertical synchronization pattern for the odd field, optional insertion test signals (ITS) are inserted. Finally, the actual odd field active image displays.

Note

The extracted line profile example at the bottom of the figure shows an actual video signal line extracted from the even field. Refer to *Video Levels* for more information about video levels.

Horizontal synchronization pulses are basically simple negative pulses, which are pulses going below the level of the luminance signal. However, the vertical synchronization signals are composed of pulse trains distributed on several lines, and the pulse trains are different for odd and even fields. The following figures show the vertical synchronization patterns for both fields and for the three main video formats.

[IMAGE alt='image' src='GUID-035E2D61-2E9D-4168-B020-A19AA21B3727-a5.gif']

#### Vertical Blanking and Synchronization Signal for NTSC

[IMAGE alt='image' src='GUID-D9E32E47-C40B-4C3A-95FE-9490207151BC-a5.gif']

#### Vertical Blanking and Synchronization Signal for PAL and SECAM

Parent topic:

Interlaced Scanning

Related concepts:

- Complete NTSC Frame Scan
- Active Image
- Video Levels

<!--NI_TOPIC bundle=ni-fgen path=how-the-ni-video-software-toolkit-filters-vid.html language=enus -->
## TOPIC 00071: How the NI Video Software Toolkit Filters Video Components

- bundle_id: `ni-fgen`
- source_path: `how-the-ni-video-software-toolkit-filters-vid.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/how-the-ni-video-software-toolkit-filters-vid.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI Video Software Toolkit has several ways to filter different video components while computing a video signal. The video formats PAL, NTSC, and SECAM require some of the filters, while other filters are optional. Three filtering modes exist: One or more of the predefined FIR filters One or more

### How the NI Video Software Toolkit Filters Video Components

The NI Video Software Toolkit has several ways to filter different video components while computing a video signal. The video formats PAL, NTSC, and SECAM require some of the filters, while other filters are optional. Three filtering modes exist:

- One or more of the predefined FIR filters
- One or more of the predefined IIR filters
- One or more user-defined FIR or IIR filters. Refer to the Advanced Color Bars from ITS with Custom Filters example.

Note

The key difference between an FIR and an IIR filter is whether the impulse response is finite (FIR) or infinite (IIR). FIR filtering is faster in computation than IIR filtering and often has a step response with less overshoot than the equivalent IIR filter. On the other hand, the frequency response of the FIR filters is not as sharp as the corresponding IIR filter.

The use of the FIR or IIR filter type depends on the application. If frequency attenuation is important, the IIR filters are recommended. If fast calculation time is a higher priority, then the FIR filters may be a better choice. If you do not specify anything, the video toolkit software uses default filters that fulfill the different requirements of the video standards.

The default filters are as follows:

- For NTSC:
  - Y (luminance component): No filter
  - Q (first chroma component): 0.4 MHz IIR filter
  - I (second chroma component): 1.3 MHz FIR filter
  - Entire composite signal: No filter
- For PAL or SECAM:
  - Y (luminance component): No filter
  - U (first chroma component): 1.3 MHz FIR filter
  - V (second chroma component): 1.3 MHz FIR filter
  - Entire composite signal: No filter

The following table lists the filter specifications.

| Filter Cut-Off | Designed for Filtering | Filter Type | Attenuation at Cut-Off | Stop-Band Frequency | Attenuation in Stop Band |
| --- | --- | --- | --- | --- | --- |
| 0.4 MHz | Q component | IIR only | < 2 dB | 0.6 MHz | > 6 dB |
| 1.3 MHz | I/U/V component | FIR/IIR | < 2 dB | 3.6 MHz | > 20 dB |
| 4.2 MHz | M-NTSC signal | FIR/IIR | 3 dB | Refer to following figures | Refer to following figures |
| 5.0 MHz | B/G-PAL signal | FIR/IIR | 3 dB | Refer to following figures | Refer to following figures |
| 5.5 MHz | I-PAL signal | FIR/IIR | 3 dB | Refer to following figures | Refer to following figures |
| 6.0 MHz | D-PAL signal | FIR/IIR | 3 dB | Refer to following figures | Refer to following figures |

The following figures show the frequency response for all the predefined FIR and IIR video filters.

[IMAGE alt='image' src='GUID-ED20D5A7-E15A-4354-8275-D5D7A32F3BB3-a5.gif']

#### Frequency Response for the Predefined FIR Filters

[IMAGE alt='image' src='GUID-06907671-100F-45E4-AFB8-0A76F3BE47F8-a5.gif']

#### Frequency Response for the Predefined IIR Filters

Parent topic:

Programming

<!--NI_TOPIC bundle=ni-fgen path=ifelseend-if.html language=enus -->
## TOPIC 00072: if/else/end if

- bundle_id: `ni-fgen`
- source_path: `ifelseend-if.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ifelseend-if.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the if/else/end if instruction to determine which sections of a script to execute. The decision depends on whether the device receives a particular Script trigger. UsageThe Script Editor automatically creates an else statement for you, though this statement is optional. This example script execu

### if/else/end if

Use the if/else/end if instruction to
 determine which sections of a script to execute. The decision depends on whether the device
 receives a particular Script trigger.

#### Usage

Note

- This example script executes a specific set of instructions when the device receives a
 Script trigger. If the device does not receive a Script trigger, the script executes a
 different set of instructions. if scriptTrigger0
 <instructions>
else
 <instructions>
end if
- This example script executes a set of instructions if the device receives a Script
 trigger. if scriptTrigger0
 <instructions>
end if
- This example script executes a set of instructions if the device does not receive a
 Script trigger. if scriptTrigger0
 else
 <instructions>
end if

Note

generate

<N>

if/else/end if

if/else/end if

if/else/end if

repeat until

<N>

#### if/else/end if
 Examples

- Generate myWfmB five times if the device receives a Script trigger.
 Otherwise, generate
 myWfmC . generate myWfmA
if scripttrigger0
 repeat 5
 generate myWfmB
 end repeat
else
 generate myWfmC
end if
- Generate myWfmA if the device receives two Script
 triggers. wait 8
if scripttrigger0
 wait 8
 if scripttrigger1
 generate myWfmA
 end if
end if
- Generate myWfmA if the device receives Script trigger 0. Or generate
 myWfmB if the device receives Script trigger 1. Otherwise, generate
 myWfmC . wait 8
if scripttrigger0
 generate myWfmA
else
 wait 8
 if scripttrigger1
 generate myWfmB
 else
 generate myWfmC
 end if
end if
- This script stops generating all subsequent waveforms after detecting a Script trigger.
 This script might be useful in the following conditions: generate myWfmA
if scripttrigger0
else 
 generate myWfmB
 if scripttrigger0
 else
 generate myWfmC
 end if
end if
  - An external digital signal serves as the Script trigger source.
  - That signal asserts when the system detects a system error condition.

Parent topic:

Scripting Instructions

<!--NI_TOPIC bundle=ni-fgen path=impedance-matching.html language=enus -->
## TOPIC 00073: Impedance Matching

- bundle_id: `ni-fgen`
- source_path: `impedance-matching.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/impedance-matching.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: When broadband signals are carried on transmission lines of any significant length, care must be taken that the transmission line is matched to its terminations. The source and load impedances should equal the characteristic impedance of the transmission line, as this minimizes signal reflections. T

### Impedance Matching

When broadband signals are carried on transmission lines of any significant length, care must
 be taken that the transmission line is matched to its terminations. The source and load
 impedances should equal the characteristic impedance of the transmission line, as this minimizes
 signal reflections. The presence of impedance discontinuities or mismatches degrade the amplitude
 and phase accuracy, as well as the temporal fidelity, of waveforms generated with a signal
 generator.

The following figure shows one of the most common mismatch errors encountered in such
 measurements.

[IMAGE alt='image' src='GUID-5352193B-2E1F-468C-AC91-5F5C9399C613-a5.gif']

In this example, selectable source impedances are provided at the signal generator outputs to
 accommodate the most popular coaxial cable characteristic impedances: 50 Ω and 75 Ω. The following figure shows what happens
 when, as in this example, a coaxial cable of the wrong characteristic impedance (50 Ω) is used with 75 Ω source and
 load impedances.

[IMAGE alt='image' src='GUID-6C4ACB99-CC3F-4039-AD18-EA7C5C261D77-a5.gif']

The pulse encounters impedance mismatches at each end of the cable, causing the pulse to be
 partially reflected. The reflected pulse traverses the cable back and forth numerous times,
 diminishing at each end by the reflection coefficient, Γ.

Γ

=

V

r

V

i

=

Z

t

−

Z

0

Z

t

+

Z

0

where

- V r = reflected voltage
- V i = incident voltage
- Z t = terminating impedance
- Z 0 = characteristic impedance

The resulting voltage waveform is distorted by the asymptotic decay of the reflected pulse as
 shown, exaggerated for visual effect. Impedance discontinuities of smaller magnitude and/or
 duration have correspondingly smaller effects. Also displayed is the waveform that results when a
 cable of matched impedance (75 Ω) is used.

#### Mismatch Uncertainty

Impedance matching is also important for preserving the absolute delivered power from an
 instrument. The accuracy with which power can be delivered is limited by mismatch error. The
 mismatch error in a z<sub>0</sub> system can be shown to be bounded by:

(

1

−

|

Γ

L

|

2

)

(

1

+

|

Γ

L

|

⋅

|

Γ

G

|

)

2

≤

mismatch

⁢

error

≤

(

1

−

|

Γ

L

|

2

)

(

1

−

|

Γ

L

|

⋅

|

Γ

G

|

)

2

where

- Γ L = load reflection coefficient
- Γ G = generator reflection coefficient

The denominator term represents mismatch uncertainty, which is a fundamental limit to the
 power transfer accuracy that can be achieved across a mismatched junction.

#### Resistive Matching

Signal generators with low/high-source impedance can be matched with a resistor placed in
 series (shunt) such that the total source impedance (admittance) is matched to the cable
 characteristic impedance (admittance). Signal generators that are not capable of driving the
 cable impedance directly can be coupled through a matching L-pad. In this case, the signal
 generator sees an approximately 500 Ω load, while the source
 impedance presented to the cable is 50 Ω, as the following figure
 shows.

[IMAGE alt='image' src='GUID-BB508423-E511-4893-BAFF-A373E13378B5-a5.gif']

High-frequency components and layout techniques should be used throughout to minimize
 parasitic effects.

Parent topic:

Waveform Fundamentals

<!--NI_TOPIC bundle=ni-fgen path=initialize.html language=enus -->
## TOPIC 00074: Initialize

- bundle_id: `ni-fgen`
- source_path: `initialize.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/initialize.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Because you can have multiple signal generators connected to your computer, you must tell NI-FGEN which signal generator to communicate with by opening a session to the signal generator. A session establishes a connection between the signal generator and your application. After this connection is es

### Initialize

Because you can have multiple signal generators
connected to your computer, you must tell NI-FGEN which signal
generator to communicate with by opening a session to the signal
generator.

A session establishes a connection between the
signal generator and your application. After this connection is
established, the signal generator can transmit data to your
application. Sessions also allow the driver to cache previous
settings, which greatly improves performance.

#### LabVIEW Example

Call the 
niFgen
Initialize VI to create a session. You can also use the niFgen Initialize with Channels VI or niFgen Initialize with Options VI as alternatives depending on the device.

- Resource Name must be set to the device identifier
assigned to the signal generator in Measurement & Automation
Explorer (MAX). You can find or set the resource name for your
signal generator by launching MAX and selecting 
 Devices and Interfaces .
- Id Query specifies whether or not to verify that
NI-FGEN supports the device you initialize. Circumstances can arise
where sending an ID query to the device is undesirable. When you
set this parameter to FALSE, the VI initializes the device without
performing an ID query.
- Reset Device allows you to reset the signal
generator during initialization.
- Instrument Handle Out returns a handle that, when
passed to subsequent VIs, allows you to communicate with the signal
generator throughout your session.

#### C Example

Call the 
niFgen_init function to create a session. You can also use the niFgen_InitializeWithChannels function or niFgen_InitWithOptions function as alternatives depending on the device.

- The 
 resourceName parameter must be set to the device
identifier assigned to the signal generator in MAX. You can find or
set the resource name for your signal generator by launching MAX
and selecting 
 Devices and Interfaces .
- The 
 idQuery parameter specifies whether or not to
verify that NI-FGEN supports the device you initialize.
Circumstances can arise where sending an ID query to the device is
undesirable. When you set this parameter to 
VI_FALSE, the function initializes
the device without performing an ID query.
- The 
 resetDevice parameter allows you to reset the
signal generator during initialization.
- The 
 vi parameter returns a handle that, when passed to
subsequent functions, allows you to communicate with the signal
generator throughout your session.

Parent topic:

NI-FGEN Tutorial

<!--NI_TOPIC bundle=ni-fgen path=initiate-generation.html language=enus -->
## TOPIC 00075: Initiate Generation

- bundle_id: `ni-fgen`
- source_path: `initiate-generation.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/initiate-generation.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Initiate Generation step transitions the device from the Committed state to the Generation state. Once this transition has been made, the device is able to begin generating waveforms. LabVIEW Example Call the niFgen Initiate Generation VI to transition the device to the Generation state. C Examp

### Initiate Generation

The Initiate Generation step transitions the device
from the Committed state to the Generation state. Once this
transition has been made, the device is able to begin generating
waveforms.

#### LabVIEW Example

Call the 
niFgen
Initiate Generation VI to transition the device to the
Generation state.

#### C Example

Call the 
niFgen_InitiateGeneration function to transition the device to the Generation state.

Parent topic:

NI-FGEN Tutorial

<!--NI_TOPIC bundle=ni-fgen path=instrumentstudio.html language=enus -->
## TOPIC 00076: InstrumentStudio

- bundle_id: `ni-fgen`
- source_path: `instrumentstudio.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/instrumentstudio.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: When you install NI‑FGEN on a system, you can monitor, control, and record measurements from supported devices using InstrumentStudio. InstrumentStudio is a software-based front panel application that allows you to perform interactive measurements on several different device types, including wavefor

### InstrumentStudio

When you install NI‑FGEN on a system, you can monitor, control, and record measurements from supported devices using InstrumentStudio. InstrumentStudio is a software-based front panel application that allows you to perform interactive measurements on several different device types, including waveform generators, in a single program.

InstrumentStudio is automatically installed when you install the NI‑FGEN driver. You can access InstrumentStudio in one of the following ways:

- From the Windows start menu, select National Instruments»InstrumentStudio [year] . This launches InstrumentStudio and runs a soft front panel populated with devices detected on your system.
- From Measurement & Automation Explorer (MAX), select a device and then click Test Panels... . This launches InstrumentStudio and runs a soft front panel for the device you selected.

For more information on using InstrumentStudio, refer to the *InstrumentStudio Manual*.

Related information:

- InstrumentStudio Manual

<!--NI_TOPIC bundle=ni-fgen path=integration-and-system-considerations.html language=enus -->
## TOPIC 00077: Integration and System Considerations

- bundle_id: `ni-fgen`
- source_path: `integration-and-system-considerations.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/integration-and-system-considerations.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: This section contains information about integrating NI signal generators into a PXI-based or a PCI-based measurement system. The PXI architecture has built-in timing and triggering features that can synchronize multiple devices over a backplane timing bus. Multiple devices in a modular instrumentati

### Integration and System Considerations

This section contains information about integrating
NI signal generators into a PXI-based or a PCI-based
measurement system.

The 
*PXI* architecture has built-in
timing and triggering features that can synchronize multiple
devices over a backplane timing bus. Multiple devices in a modular
instrumentation system can share a common Reference clock and
synchronize to triggers that are distributed over controlled signal
paths that ensure matched propagation. PC plug-ins with RTSI also
provide an internal bus that can be accessed by multiple devices.
Internal routing of these timing signals in PXI and PC plug-ins
with RTSI eliminate complicated external wiring. Standardized
timing protocols eliminate incompatibilities, giving you the best
performance when synchronizing any kind of analog, digital, or
timing measurements.

Peripheral Component Interconnect (*PCI*) is a high-performance expansion bus architecture originally developed by Intel to replace ISA and EISA. It has achieved widespread acceptance as a standard for PCs and workstations, and offers a theoretical maximum transfer rate of 132 Mbytes/s.

Related concepts:

- PXI/PXI Express Systems
- PCI Systems

<!--NI_TOPIC bundle=ni-fgen path=interlaced-scanning.html language=enus -->
## TOPIC 00078: Interlaced Scanning

- bundle_id: `ni-fgen`
- source_path: `interlaced-scanning.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/interlaced-scanning.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: All composite video systems display the video image on a TV screen using an interlaced scanning technique. The following figure illustrates the interlaced scanning concept. The analog video signal includes synchronization pulses that control the scanning line-by-line from left to right and field-by-

### Interlaced Scanning

All composite video systems display the video image on a TV screen using an interlaced scanning technique. The following figure illustrates the interlaced scanning concept.

[IMAGE alt='image' src='GUID-692C32A7-CA6C-4F30-B3B3-D72756CA9299-a5.gif']

The analog video signal includes synchronization pulses that control the scanning line-by-line from left to right and field-by-field from top to bottom. The pulses that control the line-by-line scanning are called the horizontal synchronization pulses (Hsync). The pulses that control the vertical scanning are called the vertical synchronization pulses (Vsync).

Two interlaced fields compose a *complete frame*. The first field, called the odd field, scans the odd lines of the video image. The second field, called the even field, scans the even lines of the video image. The process repeats for every frame.

Parent topic:

Video Signal Fundamentals

Related concepts:

- Complete NTSC Frame Scan

<!--NI_TOPIC bundle=ni-fgen path=level-trigger.html language=enus -->
## TOPIC 00079: Level Trigger

- bundle_id: `ni-fgen`
- source_path: `level-trigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/level-trigger.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can configure certain triggers to act when a signal goes below the defined low level or above the defined high level. Triggers configured to act in this way are known as level triggers. Not all triggers can be configured to be level triggers. Refer to Triggers Summary for information about which

### Level Trigger

You can configure certain triggers to act when a signal goes below the defined low level or above the defined high level. Triggers configured to act in this way are known as level triggers. Not all triggers can be configured to be level triggers. Refer to *Triggers Summary* for information about which triggers you can configure for level triggering.

Parent topic:

Types of Triggers

Related concepts:

- Triggers Summary

<!--NI_TOPIC bundle=ni-fgen path=marker-events.html language=enus -->
## TOPIC 00080: Marker Events

- bundle_id: `ni-fgen`
- source_path: `marker-events.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/marker-events.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: A marker is an event that the device generates in relation to a generated waveform. The event is configured to occur at the time that a specific location or sample n in the waveform generates on the analog output connector. If the waveform loops multiple times in a segment, the marker generates each

### Marker Events

A marker is an event that the device generates in relation to a generated waveform. The event is configured to occur at the time that a specific location or sample n in the waveform generates on the analog output connector. If the waveform loops multiple times in a segment, the marker generates each time the waveform loops. The following figure shows a pulse that represents a waveform sample n that is one Sample clock in width of a waveform being generated on the analog output connector. The second pulse, the Marker event, represents the pulse that generates when the corresponding waveform sample n outputs at the analog output connector. Refer to *Features Supported* to determine if your device supports markers.

[IMAGE alt='image' src='GUID-46C9E813-ABCA-4BAD-8C0F-13CA5645B8EB-a5.gif']

t<sub>m1</sub> represents the delay in time of the Marker event generated relative to the configured waveform sample n being generated.

t<sub>m2</sub> represents the Marker event pulse width in time.

NI-FGEN takes into account the factors that affect the delays in the Digital and Analog paths in assuring that the Marker event appears within one Sample clock of the waveform output. Therefore, t <sub>m1</sub> is less than one Sample clock period.

The Marker event pulse width, t<sub>m2</sub>, is at least 150 ns and can be significantly longer than 150 ns for slower Sample clocks. You can configure the pulse width by setting the Marker Event Pulse Width property or the NIFGEN_ATTR_MARKER_EVENT_PULSE_WIDTH attribute. Instruments commonly have a minimum pulse width specification for a trigger to be registered, and trigger pulses of smaller width are ignored. The signal generator ensures that a minimum pulse width exists on the Marker event by using a pulse stretching circuit. A Sample clock rate of 100 MS/s has a period of 10 ns, requiring the pulse to be lengthened for many devices to register the marker as a good trigger pulse. Refer to the *device specifications* for the timing specifications.

#### Markers as Trigger Outputs

A delay of at least 44 Sample clocks exists between the Start trigger and the analog waveform generation on the output connector. Therefore, synchronizing the signal generator output signal to other devices with fast trigger response times is accomplished using the Marker event from the signal generator as the trigger source for the other device for more precise alignment to the generating waveform. You can do this using the RTSI bus, PXI trigger lines, or PFI terminals.

#### Related Topics

Creating a Marker Event

Parent topic:

Events

Related concepts:

- Features Supported on SMC Devices
- Creating a Marker Event

<!--NI_TOPIC bundle=ni-fgen path=marker-output-signal.html language=enus -->
## TOPIC 00081: Marker Output Signal

- bundle_id: `ni-fgen`
- source_path: `marker-output-signal.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/marker-output-signal.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: A marker is a digital pulse that NI signal generators can generate at specific points within a waveform. You can route this signal to connectors on the front panel or to PXI trigger lines or RTSI trigger lines depending on the device. You can place a marker in every sequence segment. A marker can be

### Marker Output Signal

A marker is a digital pulse that NI signal generators can generate at specific points within a waveform. You can route this signal to connectors on the front panel or to PXI trigger lines or RTSI trigger lines depending on the device. You can place a marker in every sequence segment. A marker can be used as a trigger for controlling the timing of other devices in your application.

You can specify a marker by giving an offset count, in number of samples, from the start of the waveform buffer for each segment. If the waveform loops multiple times in a segment, the marker generates each time the waveform loops at the configured sample position.

If you need to generate a marker only once in a segment in which the waveform loops a number of times, break the segment up into multiple segments. For example, if you need to generate a marker on only the first iteration of a sine waveform that loops 100 times, create a segment that loops only once and generates the sine waveform with the marker at a specific sample position. Create a second segment that generates the sine waveform with no marker and loops 99 times.

This technique can be used in different combinations of segments to generate one marker every 10 of the sine waveform by creating a segment containing a marker and one loop followed by a segment with no markers that loops nine times. Repeat these two segments for as long as you need to repeat the cycle.

Parent topic:

Arbitrary Waveform Output Mode

<!--NI_TOPIC bundle=ni-fgen path=minimum-waveform-size-and-quantum.html language=enus -->
## TOPIC 00082: Minimum Waveform Size and Quantum

- bundle_id: `ni-fgen`
- source_path: `minimum-waveform-size-and-quantum.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/minimum-waveform-size-and-quantum.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The memory architecture of the NI signal generators imposes certain requirements on the waveform size and quantum. If these requirements are not met, NI-FGEN returns an error. The specific values for minimum waveform size and quantum depend on the specific NI signal generator being used. Minimum Wav

### Minimum Waveform Size and Quantum

The memory architecture of the NI signal generators imposes certain requirements on the waveform size and quantum. If these requirements are not met, NI-FGEN returns an error. The specific values for minimum waveform size and quantum depend on the specific NI signal generator being used.

#### Minimum Waveform Size

Every waveform downloaded to the device memory must be at least a minimum size in terms of the number of samples.

#### Quantum

The size in samples of the waveform downloaded to the device memory must be an
 integer multiple of a certain number or quantum.

For example, if the minimum
 waveform size for a particular signal generator is 256 samples, the quantum is eight
 samples, and you request to load a waveform of 255 samples, NI-FGEN returns an error
 because the waveform size is too small. If you request to load a waveform of 257
 samples, NI-FGEN also returns an error because even though the size is larger than
 the minimum waveform size, the waveform is not an integer multiple of the quantum
 size (8).

Waveform sizes that meet the restrictions for this example include
 256 sample, 264 samples, 272 samples, 280 samples, and others within the actual
 device memory size limit.

Parent topic:

Arbitrary Waveform Output Mode

<!--NI_TOPIC bundle=ni-fgen path=modules.html language=enus -->
## TOPIC 00083: Modules

- bundle_id: `ni-fgen`
- source_path: `modules.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/modules.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Expand this topic for information about NI signal generators available as PXI and PXI Express modules.

### Modules

Expand this topic for information about NI signal generators available as PXI and PXI Express modules.

Parent topic:

PXI/PXI Express Systems

<!--NI_TOPIC bundle=ni-fgen path=mxi-optimization-application.html language=enus -->
## TOPIC 00084: MXI Optimization Application

- bundle_id: `ni-fgen`
- source_path: `mxi-optimization-application.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/mxi-optimization-application.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: MXI-3 If you are using the MXI-3 interface to control the PXI chassis, the MXI-3 Optimization Application must be run prior to using the NI signal generator. By default, this application runs automatically when Windows starts. If you have an initialization, timeout, or performance issue with your mo

### MXI Optimization Application

#### MXI-3

If you are using the MXI-3 interface to control the
PXI chassis, the MXI-3 Optimization Application must be run prior
to using the NI signal generator. By default, this application runs
automatically when Windows starts. If you have an initialization,
timeout, or performance issue with your module, or if you are not
certain that the application ran, select 
Start»All Programs»National Instruments MXI-3»MXI-3
Optimization to run the application. If you continue to
have initialization or performance issues, refer to the MXI-3
documentation at 
Start»All Programs»National Instruments MXI-3, or
visit NI Technical Support at 
ni.com/support.

#### MXI-4 and MXI-Express Optimization

Optimization for MXI-4 and MXI Express are
performed automatically by the hardware.

Parent topic:

PXI/PXI Express Systems

<!--NI_TOPIC bundle=ni-fgen path=new-features-and-changes.html language=enus -->
## TOPIC 00085: NI-FGEN New Features and Changes

- bundle_id: `ni-fgen`
- source_path: `new-features-and-changes.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/new-features-and-changes.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Learn about updates, including new features and behavior changes, introduced in each version of NI-FGEN. Discover what is new in the latest releases of NI-FGEN.If you cannot find new features and changes for your version, it might not include user-facing updates. However, your version might include

### NI-FGEN
 New Features and Changes

Learn about updates, including new features and behavior changes, introduced in each
 version of NI-FGEN.

NI-FGEN

Note

Release Notes

Related information:

- Software and Driver Downloads

#### NI-FGEN
 2026 Q2 Changes

NI-FGEN 2026 Q2 includes support for custom marker
 pulse width in the PXIe-5433.

##### New
 Features

This version of NI-FGEN adds the
 following feature:

- Added support for custom marker pulse width for PXIe-5433.

<!--NI_TOPIC bundle=ni-fgen path=ni-5402-aborting-generation.html language=enus -->
## TOPIC 00086: NI 5402 Aborting Generation

- bundle_id: `ni-fgen`
- source_path: `ni-5402-aborting-generation.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5402-aborting-generation.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can abort the generation of the current waveform. Aborting the generation exhibits different behaviors for different waveform output modes. Whether in Standard Function mode or Frequency List mode, the NI 5402 signal generator aborts all waveforms, with the exception of the square waveform, to g

### NI 5402 Aborting Generation

You can abort the generation of the current
waveform. Aborting the generation exhibits different behaviors for
different 
*waveform output
modes*.

Whether in Standard Function mode or Frequency List mode, the NI 5402 signal generator aborts all waveforms, with the exception of the square waveform, to ground. When aborting to ground, the signal remains at the level for which the DC offset is configured. Square waveform signals drop to low when aborted.

Related Topics

*Aborting to Ground*

Parent topic:

NI 5402 Waveform Generation

Related concepts:

- NI 5402 Waveform Generation
- Abort to Ground

<!--NI_TOPIC bundle=ni-fgen path=ni-5402-access-and-active-leds.html language=enus -->
## TOPIC 00087: NI 5402 ACCESS and ACTIVE LEDs

- bundle_id: `ni-fgen`
- source_path: `ni-5402-access-and-active-leds.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5402-access-and-active-leds.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The ACCESS and ACTIVE LEDs indicate the status of the PXI module: ACCESS LED The ACCESS LED indicates basic hardware status as shown in the following table. Color Indications Off Device is not yet functional, or the device has detected a problem with a power rail. Amber The device is being accessed.

### NI 5402 ACCESS and ACTIVE LEDs

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

NI 5402 NI 5402 Overview

<!--NI_TOPIC bundle=ni-fgen path=ni-5402-accessories.html language=enus -->
## TOPIC 00088: NI 5402 Accessories

- bundle_id: `ni-fgen`
- source_path: `ni-5402-accessories.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5402-accessories.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: National Instruments offers a variety of products to use with your signal generator, including cables and other accessories. Visit ni.com for more information.

### NI 5402 Accessories

National Instruments offers a variety of products
to use with your signal generator, including cables and other
accessories. Visit 
ni.com for more
information.

Parent topic:

NI 5402 NI 5402 Overview

<!--NI_TOPIC bundle=ni-fgen path=ni-5402-analog-filter.html language=enus -->
## TOPIC 00089: NI 5402 Analog Filter

- bundle_id: `ni-fgen`
- source_path: `ni-5402-analog-filter.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5402-analog-filter.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The analog filter is a lowpass filter that is used to eliminate aliased images and artifacts due to the digital-to-analog conversion from the signal from the DAC. In general, use the analog filter for signals containing a large portion of sinusoidal content, such as AM and FM, sinc pulse, and sinuso

### NI 5402 Analog Filter

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

NI 5402 Filtering Effects

Related concepts:

- Aliased Images
- Filtering and Interpolation

<!--NI_TOPIC bundle=ni-fgen path=ni-5402-analog-output.html language=enus -->
## TOPIC 00090: NI 5402 Analog Output

- bundle_id: `ni-fgen`
- source_path: `ni-5402-analog-output.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5402-analog-output.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the NI 5402 Analog Output signal path. NI 5402 Analog waveforms are generated as follows: The digital waveform data from the Standard Function Generation Engine is passed to a digital gain circuit and then high-speed DAC. This DAC also implements a portion of the output si

### NI 5402 Analog Output

The following figure shows the NI 5402
Analog Output signal path.

[IMAGE alt='image' src='GUID-D2930CC3-8665-48B1-BD41-FAC39E240C2D-a5.gif']

NI 5402 Analog waveforms are generated as
follows:

1. The digital waveform data from the Standard Function Generation
Engine is passed to a digital gain circuit and then high-speed DAC.
This DAC also implements a portion of the output signal path
attenuation with a range of 0 dB to 3 dB. Refer to the 
 device
specifications for the exact resolution. You can adjust the
amount of attenuation by configuring the 
Amplitude
property or the 
 NIFGEN_ATTR_FUNC_AMPLITUDE attribute. NI-FGEN calculates and sets the correct amount of
attenuation required, corresponding to the gain setting.
2. Following the DAC, the signal then passes through a switchable
lowpass Analog Filter to remove 
 Aliased Images . For
User-defined waveforms created in Standard Function mode or
Frequency List mode, you can select whether to include the Analog
Filter in the Analog Output path using either the 
niFgen Configure Analog Filter VI or the 
 niFgen_EnableAnalogFilter and 
 niFgen_DisableAnalogFilter functions.
3. Either the Main path output or the Square Wave Output path is
selected based on the desired waveform which then passes through
the DC Offset Amplifier that adds the desired DC offset voltage.
For User-defined waveform created in Standard Function mode or
Frequency List mode, you can adjust the amount of DC offset added
to the signal up to ±5 V 
 pk including AC and DC components into 50 Ω
impedance. Refer to the 
DC
Offset property, or the 
 NIFGEN_ATTR_FUNC_DC_OFFSET attribute for more information.
4. The signal then passes through the Pre-Amp Attenuation section,
a set of selectable solid-state attenuators that provide 0 dB
to 12 dB of attenuation in 3 dB increments. You can adjust the
amount of attenuation by adjusting the Amplitude property, or the 
 NIFGEN_ATTR_FUNC_AMPLITUDE 
attribute. NI-FGEN calculates and sets the correct amount of
attenuation required, corresponding to the gain setting.
5. Following the Pre-Amp Attenuation section, the signal can take
one of two paths: the High-Gain or Low-Gain Amplifier path. NI-FGEN
automatically selects the best amplifier path between the High-Gain
and Low-Gain amplifiers by default based on the Amplitude property
or the 
 NIFGEN_ATTR_FUNC_AMPLITUDE attribute
setting. Alternatively, you can set the signal path to remain
constant regardless of the amplitude setting for applications
requiring one path or the other by calling the 
Analog
Path property or the 
 NIFGEN_ATTR_ANALOG_PATH attribute for more information.
  1. The High-Gain Amplifier path is used for waveform output
voltages greater than ±1.0 V (±0.83 V for sine waveforms) into
50 Ω. The amplifier has a fixed gain and is included in
the signal path to enable the signal generator to provide the
maximum V 
 pk-pk .
  2. The Low-Gain Amplifier path is used for waveforms that have all
output voltages equal to or smaller than ±1.0 V (±0.83 V for
sine waveforms) into 50 Ω. The amplifier has a fixed
gain.
6. The signal passes through the Post Amp Attenuation section, a
set of two passive attenuators 12 dB and 24 dB. You can adjust the
amount of attenuation by configuring the Amplitude property or the 
 NIFGEN_ATTR_FUNC_AMPLITUDE 
attribute. NI-FGEN calculates and sets the correct amount of
attenuation required, corresponding to the gain setting.
7. The signal then passes through the Output Enable relay. When
the Output Enable relay is disabled, ground is connected to the
output through a 50 Ω or a 75 Ω resistor.
Intentionally, Standard Function Generation continues while the
output enable relay is disabled. When the relay is enabled, the
analog waveform is seen at the CH 0 connector. You can enable
or disable the output of the analog waveform generator by calling the 
niFgen
Output Enable VI or the 
 niFgen_ConfigureOutputEnabled function for more information.
8. The signal then passes through a
50 Ω/75 Ω selector to the
CH 0 connector. You can configure the output impedance of
the analog waveform generator by calling the 
niFgen Configure Output Impedance VI or the 
 niFgen_ConfigureOutputImpedance function.

Note

Parent topic:

NI 5402 Theory of Operation

Related concepts:

- Aliased Images

<!--NI_TOPIC bundle=ni-fgen path=ni-5402-attenuation.html language=enus -->
## TOPIC 00091: NI 5402 Attenuation

- bundle_id: `ni-fgen`
- source_path: `ni-5402-attenuation.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5402-attenuation.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Analog Output path has two passive attenuation sections. Preamplifier attenuation is prior to the High-Gain and Low-Gain Amplifier paths, and postamplifier attenuation is after the High-Gain and Low-Gain Amplifier paths. The main DAC provides 0 to 3 dB of signal attenuation. Amplitude control is

### NI 5402 Attenuation

The Analog Output path has two passive attenuation
sections. *Preamplifier attenuation* is prior to the High-Gain
and Low-Gain Amplifier paths, and *postamplifier attenuation* is after the
High-Gain and Low-Gain Amplifier paths.

The main *DAC* provides 0 to 3 dB of signal attenuation. Amplitude control is implemented after the DAC. Attenuating the DAC output signal allows you to vary the signal amplitude while maintaining the dynamic range of the DAC. You do not lose any bits from the digital representation of the signal and you do not sacrifice dynamic range, as you would if you control amplitude by using smaller data ranges of the DAC.

For the Low-Gain and the High-Gain Amplifier paths, maximum attenuation is
51 dB. NI-FGEN automatically determines the correct value of attenuation in dB and configures the attenuation based on the set
amplitude. The
minimum amplitude setting for an Analog Output path configured to
High-Gain Amplifier path is .01691. The minimum allowable amplitude
setting with NI-FGEN automatically selecting the Low-Gain Amplifier
path is .005635 (gain is a unitless value).

NI-FGEN calculates and sets the correct amount of
attenuation required that corresponds to your NI-FGEN gain setting.
The correct amount of attenuation is implemented in the 
preamplifier and postamplifier attenuation blocks to best achieve
the desired output signal amplitude. You can set the amount of gain
with the Amplitude property or the 
NIFGEN_ATTR_FUNC_AMPLITUDE attribute.

Parent topic:

NI 5402 Waveform Amplitude Control

Related concepts:

- NI 5402 Preamplifier Attenuation
- NI 5402 Postamplifier Attenuation
- NI 5402 DAC Attenuation

<!--NI_TOPIC bundle=ni-fgen path=ni-5402-block-diagram.html language=enus -->
## TOPIC 00092: NI 5402 Block Diagram

- bundle_id: `ni-fgen`
- source_path: `ni-5402-block-diagram.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5402-block-diagram.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: This topic contains information about the NI 5402 top-level block diagram and descriptions of the individual blocks. If it is installed in any slot other than Slot 2 of the PXI chassis, the NI 5402 can receive a signal on the PXI_STAR line and can route a signal on the PXI_STAR line back to Slot 2

### NI 5402 Block Diagram

This topic contains information about the 
NI 5402 top-level block diagram and descriptions of the
individual blocks.

[IMAGE alt='image' src='GUID-42A6677D-182B-4580-952B-B38955E767F9-a5.gif']

Note

The following list describes the individual
blocks:

- The 
 Onboard Memory stores the 
 frequency list instructions
that you load into the device.
- Clocking allows you to phase lock the onboard Sample clock
to a Reference clock.
- The 
 Standard Function Generation Engine generates standard
functions using 
 direct digital synthesis (DDS) with a 16 k
lookup table and 48-bit accumulator using the 100 MHz Sample
clock.
- The 
 Standard Function Generation Engine retrieves the
frequency list instructions from the 
 Onboard Memory .
- The output from the 
 Standard Function Generation Engine is sent to the 
 DAC after any digital gain is applied.
- For user-defined waveforms, the 
 DAC also contains a selectable 
 Digital Filter , which interpolates and filters the
waveform data.
- The waveform data is sent from the 
 DAC to the 
 Analog Output path where the signal data is filtered and
amplified.
- The 
 Routing Matrix allows flexible routing of the PXI Trigger
lines (RTSI) and the external PFI lines.

Parent topic:

NI 5402 Theory of Operation

Related concepts:

- Frequency List Mode
- Direct Digital Synthesis

<!--NI_TOPIC bundle=ni-fgen path=ni-5402-burst-trigger-mode.html language=enus -->
## TOPIC 00093: NI 5402 Burst Trigger Mode

- bundle_id: `ni-fgen`
- source_path: `ni-5402-burst-trigger-mode.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5402-burst-trigger-mode.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: In Burst trigger mode, calling the first Start trigger begins waveform generation. The waveform then generates continually. The following table provides more information about waveform generation behavior in Frequency List output mode. Output Mode Trigger Behavior Frequency List Mode The device gene

### NI 5402 Burst Trigger Mode

In Burst trigger mode, calling the first Start
trigger begins waveform generation. The waveform then generates
continually. The
following table provides more information about
waveform generation behavior in Frequency List output mode.

| Output Mode | Trigger Behavior |
| --- | --- |
| Frequency List Mode | The device generates the next step in the active frequency list every time a Start trigger occurs. After the duration for a step elapses, the waveform generates until the next Start trigger is received. When the next Start trigger is received, the next step in the frequency list generates. If a Start trigger is received within the specified duration of the step, the Start trigger is applied after the duration elapses. Any additional Start triggers received within the duration are ignored. If the Trigger Source property or the NIFGEN_ATTR_TRIGGER_SOURCE attribute is set to NIFGEN_VAL_IMMEDIATE, the only way to advance to the next step in the frequency list is to call the niFgen Send Software Edge Trigger VI or the niFgen_SendSoftwareEdgeTrigger function. |

Parent topic:

NI 5402 Trigger Modes

<!--NI_TOPIC bundle=ni-fgen path=ni-5402-calibration.html language=enus -->
## TOPIC 00094: NI 5402 Calibration

- bundle_id: `ni-fgen`
- source_path: `ni-5402-calibration.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5402-calibration.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Before shipping your signal generator, NI calibrated your device to ensure that all features are within specifications. Calibration is a set of operations that compares the values indicated by a measuring instrument or measuring system to the corresponding values realized by external standards. You

### NI 5402 Calibration

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

NI 5402 NI 5402 Overview

<!--NI_TOPIC bundle=ni-fgen path=ni-5402-ch-0-connector.html language=enus -->
## TOPIC 00095: NI 5402 CH 0 Connector

- bundle_id: `ni-fgen`
- source_path: `ni-5402-ch-0-connector.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5402-ch-0-connector.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The CH 0 connector is the analog waveform output terminal. The maximum output levels from this connector depend on the type of load termination. For example, if the output of the device terminates into a 50 Ω load, the maximum output levels are ±5 V, while the maximum output levels are ±10 V when th

### NI 5402 CH 0 Connector

The CH 0 connector is the analog waveform
output terminal. The maximum output levels from this connector
depend on the type of load termination. For example, if the output of the device
terminates into a 50 Ω load, the maximum output levels
are ±5 V, while the maximum output levels are ±10 V when the
device terminates into a high-impedance load (HiZ). This difference
is illustrated in the following figure.

[IMAGE alt='image' src='GUID-B63A4BA1-6BFA-443C-8A58-30D1C13C1E21-a5.gif']

If the output terminates into any other load, the
levels are defined by the following formula:

V<sub>out</sub>
 = ± [ 
R<sub>L</sub>
 / ( 
R<sub>L</sub>
 + 
R<sub>O</sub>
 ) ] × 10 V

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
 or NIFGEN_ATTR_FUNC_AMPLITUDE attribute.

#### Load Impedance Compensation

The NI 5402 has the ability to configure the
output signal amplitude based on a user-configured load impedance
setting. This capability is desirable when you use the NI 5402
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
desired peak-to-peak voltage amplitude or arbitrary gain. You can configure the load impedance by calling the 
Load
Impedance property or 
NIFGEN_ATTR_LOAD_IMPEDANCE attribute.

Note

For waveform output
signal specifications, refer to the 
*device
specifications*.

Parent topic:

NI 5402 NI 5402 Overview

<!--NI_TOPIC bundle=ni-fgen path=ni-5402-clocking.html language=enus -->
## TOPIC 00096: NI 5402 Clocking

- bundle_id: `ni-fgen`
- source_path: `ni-5402-clocking.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5402-clocking.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5402 has a sample clock rate of 100 MHz. You can use the REF IN connector or the PXI_CLK10/RTSI 7 line as the source of the frequency reference for the onboard phase-locked loop. For PCI signal generators, you can also use the onboard Reference clock. The onboard Reference clock is availabl

### NI 5402 Clocking

The NI 5402 has a sample clock rate of
100 MHz. You can use the REF IN connector or the
PXI_CLK10/RTSI 7 line as the source of the frequency reference for
the onboard phase-locked loop. For PCI signal generators, you can
also use the onboard Reference clock.

[IMAGE alt='image' src='GUID-84532EF6-80F1-4F0C-A6C4-058D0C08BF61-a5.gif']

Note

Related Topics

*Phase-Locked Loop
Reference Sources*

*Exporting Clocks*

Parent topic:

NI 5402 Theory of Operation

Related concepts:

- NI 5402 Reference Clock
- NI 5402 Exporting Clocks

<!--NI_TOPIC bundle=ni-fgen path=ni-5402-continuous-trigger-mode.html language=enus -->
## TOPIC 00097: NI 5402 Continuous Trigger Mode

- bundle_id: `ni-fgen`
- source_path: `ni-5402-continuous-trigger-mode.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5402-continuous-trigger-mode.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The waveform you downloaded generates continuously after receiving one Start trigger. All Start triggers after the first Start trigger are ignored. The following table provides more information about waveform generation behavior in Frequency List output mode. Output Mode Trigger Behavior Frequency L

### NI 5402 Continuous Trigger Mode

The waveform you downloaded generates continuously
after receiving one Start trigger. All Start triggers after the
first Start trigger are ignored. The
following table provides more information about
waveform generation behavior in Frequency List output mode.

| Output Mode | Trigger Behavior |
| --- | --- |
| Frequency List Mode | The device generates the next step in the active frequency list once the duration of the step has elapsed. The frequency list repeats until generation is aborted. The frequency list generates continuously after receiving one Start trigger. All Start triggers after the first Start trigger are ignored. |

Parent topic:

NI 5402 Trigger Modes

<!--NI_TOPIC bundle=ni-fgen path=ni-5402-dac-attenuation.html language=enus -->
## TOPIC 00098: NI 5402 DAC Attenuation

- bundle_id: `ni-fgen`
- source_path: `ni-5402-dac-attenuation.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5402-dac-attenuation.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The main DAC output can be fine-tuned for attenuation, which provides 0 to 3 dB of the Analog Output path signal attenuation. This fine-tuning of the main DAC attenuation is performed by the gain DAC. Adjust the gain DAC using the Gain DAC Value property or the NIFGEN_ATTR_GAIN_DAC_VALUE attribute.

### NI 5402 DAC Attenuation

The main DAC output can be fine-tuned for
attenuation, which provides 0 to 3 dB of the Analog Output
path signal attenuation. This fine-tuning of the main DAC
attenuation is performed by the gain DAC. Adjust the gain
DAC using the 
Gain
DAC Value property or the 
NIFGEN_ATTR_GAIN_DAC_VALUE attribute. The main DAC also
provides the fine resolution for the attenuation settings.

The fine gain control of square wave signals is
controlled through the Square Wave Gain DAC. You can adjust the
Square Wave Gain DAC by setting the Gain DAC Value property or the 
NIFGEN_ATTR_GAIN_DAC_VALUE
attribute.

Parent topic:

NI 5402 Attenuation

<!--NI_TOPIC bundle=ni-fgen path=ni-5402-data-mask.html language=enus -->
## TOPIC 00099: NI 5402 Data Mask

- bundle_id: `ni-fgen`
- source_path: `ni-5402-data-mask.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5402-data-mask.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The signal generator supports analog data masks and static values. The data mask allows you to shield bits of the data to be replaced with the corresponding static value bits. For example, a mask of 0xFF00 and a static value of 0xAAAA applied to a DC waveform with a value of 0x1111 produces a DC wav

### NI 5402 Data Mask

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

NI 5402 NI 5402 Overview

<!--NI_TOPIC bundle=ni-fgen path=ni-5402-dc-offset.html language=enus -->
## TOPIC 00100: NI 5402 DC Offset

- bundle_id: `ni-fgen`
- source_path: `ni-5402-dc-offset.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5402-dc-offset.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The maximum DC Offset allowed on the signal generator depends on the output waveform being generated. For square waveforms, the maximum offset that is allowed is 50% of the amplitude setting (50% of V [pk-pk]). The maximum offset is shown in the following figure. If a sine, triangle, ramp, or user-d

### NI 5402 DC Offset

The maximum DC Offset allowed on the signal
generator depends on the output waveform being generated.

For square waveforms, the maximum offset that is
allowed is 50% of the amplitude setting (50% of V 
<sub>pk-pk</sub>). The maximum offset is shown in the following
figure.

[IMAGE alt='image' src='GUID-E3F8B57E-6A52-42D0-A3E4-F9DF811E95D2-a5.gif']

If a sine, triangle, ramp, or user-defined
waveform is generated, then any offset is allowed as long as the
waveform stays within the +10 and -10 V amplitude limit of the
board into high Z (+5 V and -5 V limit into 50 Ω load). A 2 V<sub>pk-pk</sub> sine waveform is shown in the following figure
with its maximum allowed offset setting.

[IMAGE alt='image' src='GUID-5E3A7B40-D362-4D48-90FA-1BA1203916A9-a5.gif']

Note

device specifications

Parent topic:

NI 5402 Waveform Amplitude Control

<!--NI_TOPIC bundle=ni-fgen path=ni-5402-digital-filter.html language=enus -->
## TOPIC 00101: NI 5402 Digital Filter

- bundle_id: `ni-fgen`
- source_path: `ni-5402-digital-filter.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5402-digital-filter.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The main DAC provides an internal digital filter. When digital filtering is enabled, the main DAC runs at a faster rate, referred to as the effective sample rate (ESR). The waveform data transfers to the main DAC at the configured Sample clock rate; the internal digital filter interpolates by a fact

### NI 5402 Digital Filter

The main DAC provides an internal digital filter.
When digital filtering is enabled, the main DAC runs at a faster
rate, referred to as the effective sample rate (ESR). The waveform
data transfers to the main DAC at the configured Sample clock rate;
the internal digital filter interpolates by a factor of 2x or 4x; and the DAC generates the data at the ESR.

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
without exceeding 400 MS/s.

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

NI 5402 Filtering Effects

Related concepts:

- Filtering and Interpolation
- Aliased Images

<!--NI_TOPIC bundle=ni-fgen path=ni-5402-digital-gain.html language=enus -->
## TOPIC 00102: NI 5402 Digital Gain

- bundle_id: `ni-fgen`
- source_path: `ni-5402-digital-gain.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5402-digital-gain.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Digital gain multiplies waveform data by a factor you specify in the Digital Gain property or the NIFGEN_ATTR_DIGITAL_GAIN attribute before converting the data to an analog signal in the DAC. Digital gain can be changed during generation without the glitches caused by switching that are common when

### NI 5402 Digital Gain

NIFGEN_ATTR_DIGITAL_GAIN

Note

Parent topic:

NI 5402 Waveform Amplitude Control

<!--NI_TOPIC bundle=ni-fgen path=ni-5402-events.html language=enus -->
## TOPIC 00103: NI 5402 Events

- bundle_id: `ni-fgen`
- source_path: `ni-5402-events.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5402-events.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use events to indicate when a specific hardware condition has been met on the NI 5402. An event is a signal generated by the NI device at a device state. The NI 5402 supports Ready for Start, Started, and Done events. The NI 5402 also supports the use of event delays.

### NI 5402 Events

You can use *events* to indicate when a specific
hardware condition has been met on the NI 5402. An event is a
signal generated by the NI device at a device state. The NI 5402
supports Ready for Start, Started, and Done
events. The NI 5402 also supports the use of *event delays*.

Parent topic:

NI 5402 NI 5402 Overview

Related concepts:

- Events
- Event Delays

<!--NI_TOPIC bundle=ni-fgen path=ni-5402-exporting-clocks.html language=enus -->
## TOPIC 00104: NI 5402 Exporting Clocks

- bundle_id: `ni-fgen`
- source_path: `ni-5402-exporting-clocks.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5402-exporting-clocks.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5402 provides two resources for exporting your clocks and multiple destinations to route to. The following table shows the available clock signals that can be routed to devices external to the NI 5402 and the destination options. Clock to be Exported Destination Options Sample Clock SYNC OUT/

### NI 5402 Exporting Clocks

The NI 5402 provides two resources for
exporting your clocks and multiple destinations to route to.

[IMAGE alt='image' src='GUID-60A00E20-6823-4B50-ADD4-09D750B2F25C-a5.gif']

The following table shows the available clock
signals that can be routed to devices external to the
NI 5402 and the destination options.

| Clock to be Exported | Destination Options |
| --- | --- |
| Sample Clock | SYNC OUT/PFI 0 and PFI 1 BNC connector |
| PXI_Trig<0..6> (PXI), RTSI<0..6> (PCI) |  |
| Reference Clock | SYNC OUT/PFI 0 and PFI 1 BNC connector |
| PXI_Trig<0..6> (PXI), RTSI<0..6> (PCI) |  |
| Onboard Reference Clock | RTSI7 |

#### Sample Clock

For synchronization purposes, the NI 5402 
allows you to export your Sample clock so that other devices can
have the same timing as the NI 5402. The Sample clock can
be routed to the SYNC OUT/PFI 0 and PFI 1 front panel BNC
connectors, PXI_Trig<0..6> lines on the PXI trigger bus, or
the RTSI<0..6> (PCI) lines.

Additionally, the exported clock can be divided
down by an integer value (no less than 2) before being exported to
the SYNC OUT/PFI 0 and PFI 1 BNC connectors, PXI_Trig<0..6>
lines, or the RTSI<0..6> (PCI) lines. You can configure the Sample clock divisor by calling the 
Exported Sample Clock Divisor property or the 
NIFGEN_ATTR_EXPORTED_SAMPLE_CLOCK_DIVISOR attribute.

Note

specifications

#### Reference Clock

For synchronization purposes, the NI 5402 
allows you to export your PLL Reference clock so that other devices
can lock their clock sources to the same signal. Referring to the
previous image, this clock is the actual clock that is configured
for the NI 5402 phase-locked loop circuit to use as a
reference. You must have a Reference clock configured as a PLL
Reference clock source for the signal to be available for
exporting. The Reference clock can be routed to the SYNC OUT/PFI 0
and PFI 1 BNC connectors on the front panel, the
PXI_Trig<0..6> lines on the PXI trigger bus, or the
RTSI<0..6> (PCI) lines.

Note

#### Onboard Reference Clock

The onboard Reference clock is a dedicated 10 MHz
clock for PCI modules only. The onboard Reference clock can only be
exported to RTSI7, for other modules to use, and to reimport as the
Reference clock. You can export the onboard Reference clock to
other modules on RTSI7 and then reimport it so that all devices
(including the master) can use the same Reference clock.

#### Destination Options

SYNC OUT/PFI 0 and PFI 1–The Sample clock
and the Reference clock can be exported to the SYNC OUT/PFI 0 and
PFI 1 BNC connectors on the front panel to synchronize external
devices. You must configure the device to export the desired clock
to the PFI BNC connectors.

Note

niFgen_ExportSignal

PXI_Trig<0..6>–The Sample clock and
the Reference clock can be exported to the PXI_Trig lines or RTSI
(PCI) lines. The PXI/PCI standard allows for devices to route
signals to other devices in your PXI chassis to enhance device to
device synchronization. Refer to the chassis documentation for
specifications to ensure the reference signal is within tolerance.
You must configure the device to export the desired clock to the
PXI_Trig line or RTSI line. When exporting signals,
PXI_Trig<0..6> is equivalent to RTSI_<0..6>

You can configure the
destinations for the desired clock signal by calling the 
niFgen
Export Signal VI or the 
niFgen_ExportSignal function.

Parent topic:

NI 5402 Clocking

<!--NI_TOPIC bundle=ni-fgen path=ni-5402-exporting-signals.html language=enus -->
## TOPIC 00105: NI 5402 Exporting Signals

- bundle_id: `ni-fgen`
- source_path: `ni-5402-exporting-signals.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5402-exporting-signals.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The signal generator contains seven PXI trigger lines or seven RTSI (PCI devices only) lines that are available for sending signal generator-specific information to other devices that have PXI trigger or RTSI bus connectors. The signal generator also connects to the PXI star trigger line, which you

### NI 5402 Exporting Signals

Note

ni.com/products

The signal generator has connectors on the front
panel to route signals to devices external to a PXI or PCI
chassis. The following table shows the signals available for export
and the lines they can be routed to. To determine all possible
signal routes for your device, refer to 
*Signal Routing*.

|  |  | Destination |  |
| --- | --- | --- | --- |
| PXI_Trig<0..6>, RTSI<0..6>, or PXI_STAR | SYNC OUT/PFI 0 and PFI 1 Connectors |  |  |
| Exported Clocks, Triggers, and Events | Sample Clock | Yes | Yes * |
| PLL Reference Source | Yes | Yes* |  |
| Out Start trigger | Yes | Yes |  |
| * SYNC OUT/PFI 0 is optimized for the Sample clock and PLL reference source signals and has slightly less jitter than PFI 1. SYNC OUT/PFI 0 is the recommended terminal to use for exporting clocks. |  |  |  |

Sample Clock–The clock signal that tells the
DAC when to convert the digital waveform values to an analog
voltage. The Sample clock frequency is referred to as the Sample
clock rate; the rate at which the digital waveforms from device
memory are generated. The Sample clock is also known as update
clock.

Note

PLL Reference source–A clock signal that is
only available when a PLL Reference source has been configured. The
clock is the source selected as the PLL Reference Clock source.

Out Start trigger–A signal generated by the
device upon recognizing a start condition that can be routed out
various connectors to signal other devices.

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

NI 5402 NI 5402 Overview

Related concepts:

- NI 5402 Signal Routing

<!--NI_TOPIC bundle=ni-fgen path=ni-5402-filtering-effects.html language=enus -->
## TOPIC 00106: NI 5402 Filtering Effects

- bundle_id: `ni-fgen`
- source_path: `ni-5402-filtering-effects.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5402-filtering-effects.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The delay from the time at which the device receives a trigger to the time at which the analog output signal is generated increases if the digital and/or analog filters in the Analog Output path are enabled. In the case of digital filtering, delay also increases with increase in interpolation. The

### NI 5402 Filtering Effects

Analog Output path

Note

Refer to 
*Digital
Filter* for interpolation options. Refer to the 
*device
specifications* for the delay from trigger to analog output
based on different filtering options.

Parent topic:

NI 5402 Analog Output

Related concepts:

- NI 5402 Analog Output
- NI 5402 Digital Filter

<!--NI_TOPIC bundle=ni-fgen path=ni-5402-filtering-effects_2.html language=enus -->
## TOPIC 00107: NI 5402 Filtering Effects

- bundle_id: `ni-fgen`
- source_path: `ni-5402-filtering-effects_2.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5402-filtering-effects_2.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The delay from the time at which the device receives a trigger to the time at which the analog output signal is generated increases if the digital and/or analog filters in the Analog Output path are enabled. In the case of digital filtering, delay also increases with increase in interpolation. The

### NI 5402 Filtering Effects

Analog Output path

Note

Refer to 
*Digital
Filter* for interpolation options. Refer to the 
*device
specifications* for the delay from trigger to analog output
based on different filtering options.

Parent topic:

NI 5402 Triggering

<!--NI_TOPIC bundle=ni-fgen path=ni-5402-flatness-correction.html language=enus -->
## TOPIC 00108: NI 5402 Flatness Correction

- bundle_id: `ni-fgen`
- source_path: `ni-5402-flatness-correction.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5402-flatness-correction.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5402 uses flatness correction to ensure a consistent power level when generating sine waveforms at any frequency. During external calibration, the frequency response of the Analog path in its different configurations is measured using the niFgen Initialize Flatness Calibration VI or the niFge

### NI 5402 Flatness Correction

The NI 5402 uses flatness correction to ensure
a consistent power level when generating sine waveforms at any
frequency.

During external calibration, the frequency response
of the Analog path in its different configurations is measured
using the 
niFgen Initialize Flatness Calibration VI or the 
niFgen_InitializeFlatnessCalibration function and the 
niFgen Cal Adjust Flatness
VI or the 
niFgen_CalAdjustFlatness function.

During generation, these measured values are used
to compensate for any attenuation at the requested frequency. The
compensation is applied by digitally multiplying the digital data
going into the DAC by a correction factor.

Parent topic:

NI 5402 Waveform Amplitude Control

<!--NI_TOPIC bundle=ni-fgen path=ni-5402-frequency-list-mode.html language=enus -->
## TOPIC 00109: NI 5402 Frequency List Mode

- bundle_id: `ni-fgen`
- source_path: `ni-5402-frequency-list-mode.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5402-frequency-list-mode.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Frequency List output mode allows you to configure the device to generate a standard function using a list of frequencies you define. A frequency list is composed of steps, each one with a frequency/duration pair. Frequency lists are commonly used for frequency hops and sweeps and frequency shift ke

### NI 5402 Frequency List Mode

*Frequency List output mode* allows you to configure the
device to generate a standard function using a list of frequencies
you define. A frequency list is composed of steps, each one with a
frequency/duration pair. Frequency lists are commonly used for
*frequency hops and sweeps* and frequency shift keying (FSK) applications.

Parent topic:

NI 5402 Output Modes

Related concepts:

- Frequency List Mode
- Frequency Hopping and Sweeping

<!--NI_TOPIC bundle=ni-fgen path=ni-5402-hardware-state-diagram.html language=enus -->
## TOPIC 00110: NI 5402 Hardware State Diagram

- bundle_id: `ni-fgen`
- source_path: `ni-5402-hardware-state-diagram.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5402-hardware-state-diagram.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following diagram shows the hardware states of the signal generator. The signal generator can be in one of the following six basic states during the course of operation. Idle—The device is not generating a waveform. All session properties or attributes can be programmed in the Idle state. In the

### NI 5402 Hardware State Diagram

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

NI 5402 Theory of Operation

Related concepts:

- Programming State Model

<!--NI_TOPIC bundle=ni-fgen path=ni-5402-ni-5402-overview.html language=enus -->
## TOPIC 00111: NI 5402 NI 5402 Overview

- bundle_id: `ni-fgen`
- source_path: `ni-5402-ni-5402-overview.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5402-ni-5402-overview.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5402 is a 20 MHz, 14-bit function generator with the following features: One 14-bit resolution output channel Output amplitude up to 10 V [pk-pk] into a 50 Ω load Offset up to ±5 V [pk] including AC and DC components into 50 Ω impedance Up to 20 MHz sine output Up to 20 MHz square output Up t

### NI 5402 NI 5402 Overview

The NI 5402 is a 20 MHz, 14-bit function generator with the following features:

- One 14-bit resolution output channel

- Output amplitude up to 10 V 
 pk-pk into a 50 Ω load
- Offset up to ±5 V 
 pk including AC and DC components into 50 Ω
impedance

- Up to 20 MHz sine output
- Up to 20 MHz square output
- Up to 1 MHz triangle, ramp-up, and ramp-down output

- Software-selectable output impedances (50 Ω or
75 Ω) and output attenuation levels from 0 dB to
51 dB
- PLL synchronization to external clocks or to
PXI_CLK10
- NI-TClk support for multi-module synchronization. Refer to 
 Start»All Programs»National Instruments»NI-TClk 
for more information.
- Sampling rate of 100 MS/s
- 32 MB of onboard frequency list memory
- Digital and analog filters
- Digital gain
- Two external trigger inputs
- PXI trigger/RTSI lines

All NI 5402 devices follow
industry-standard Plug and Play specifications for the PXI bus and
offer seamless integration with compliant systems.

Parent topic:

Devices

<!--NI_TOPIC bundle=ni-fgen path=ni-5402-onboard-memory.html language=enus -->
## TOPIC 00112: NI 5402 Onboard Memory

- bundle_id: `ni-fgen`
- source_path: `ni-5402-onboard-memory.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5402-onboard-memory.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5402 can store the following in onboard memory: Up to 32 MB of frequency list instructions 65,536 samples for sine, square, and triangle waveforms 16,384 samples for all other waveforms

### NI 5402 Onboard Memory

The NI 5402 can store the following in onboard
memory:

- Up to 32 MB of frequency list instructions
- 65,536 samples for sine, square, and triangle waveforms
- 16,384 samples for all other waveforms

Parent topic:

NI 5402 Theory of Operation

<!--NI_TOPIC bundle=ni-fgen path=ni-5402-output-enable.html language=enus -->
## TOPIC 00113: NI 5402 Output Enable

- bundle_id: `ni-fgen`
- source_path: `ni-5402-output-enable.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5402-output-enable.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can disable the analog output signal at the CH 0 connector by controlling the output enable relay, as shown in the following figure. When the output enable relay is disabled, the output signal is connected to ground through a 50 or 75 Ω resistance depending on the output impedance selected. The

### NI 5402 Output Enable

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

NI 5402 Analog Output

Related concepts:

- NI 5402 Analog Output

<!--NI_TOPIC bundle=ni-fgen path=ni-5402-output-impedance.html language=enus -->
## TOPIC 00114: NI 5402 Output Impedance

- bundle_id: `ni-fgen`
- source_path: `ni-5402-output-impedance.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5402-output-impedance.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5402 Analog Output path is designed to have an output impedance of 50 Ω from the Output Enable relay looking back towards the Main DAC. Most applications use a load impedance of 50 Ω, but applications such as video testing, require 75 Ω. As shown in the following figure, there is a selectable

### NI 5402 Output Impedance

The NI 5402 Analog Output path is
designed to have an output impedance of 50 Ω from the
Output Enable relay looking back towards the Main DAC. Most applications use a load impedance of
50 Ω, but applications such as video testing, require
75 Ω. As shown in the following figure, there is a
selectable 25 Ω resistance that can be switched into the
Analog Output path between the Output Enable Relay and the CH 0 connector for applications requiring a 75 Ω impedance.

[IMAGE alt='image' src='GUID-D2930CC3-8665-48B1-BD41-FAC39E240C2D-a5.gif']

If the load impedance is a high impedance (~1
MΩ), you may see output levels up to twice the selected
output value for a matched input/output impedance. These levels can
be as high as 20 V 
<sub>pk-pk</sub> for the High-Gain Amplifier path. Normally, the
output levels increase as the load impedance increases. The
NI 5402 can compensate for different load impedance
values. Refer to 
*CH 0 Connector* for more
information.

niFgen_ConfigureOutputImpedance

Note

Parent topic:

NI 5402 Analog Output

Related concepts:

- NI 5402 CH 0 Connector

<!--NI_TOPIC bundle=ni-fgen path=ni-5402-output-modes.html language=enus -->
## TOPIC 00115: NI 5402 Output Modes

- bundle_id: `ni-fgen`
- source_path: `ni-5402-output-modes.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5402-output-modes.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The output mode of your signal generator determines the type of waveforms your signal generator produces. To select an output mode, set the Output Mode parameter of the niFgen Configure Output Mode VI or the niFgen_ConfigureOutputMode function.

### NI 5402 Output Modes

The output mode of your signal generator determines the type of
waveforms your signal generator produces. To select an output mode,
set the 
Output Mode parameter of the 
niFgen
Configure Output Mode VI or the 
niFgen_ConfigureOutputMode function.

Parent topic:

NI 5402 Waveform Generation

<!--NI_TOPIC bundle=ni-fgen path=ni-5402-pci-front-panel.html language=enus -->
## TOPIC 00116: NI 5402 PCI Front Panel

- bundle_id: `ni-fgen`
- source_path: `ni-5402-pci-front-panel.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5402-pci-front-panel.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the NI PCI-5402 front panel. This front panel has four BNC connectors. The CH 0 connector is the analog output from which arbitrary waveforms are generated. The REF IN connector provides the device with an external reference or external Sample clock. The SYNC OUT/PFI 0 and

### NI 5402 PCI Front Panel

The following figure shows the
NI PCI-5402 front panel. This front panel has four BNC
connectors.

[IMAGE alt='image' src='GUID-3FB3535E-7CE2-49F9-ADEF-3718868281F2-a5.gif']

The 
*CH 0* connector is the analog output
from which arbitrary waveforms are generated.

The 
*REF IN* connector provides the
device with an external reference or external Sample clock.

The 
*SYNC OUT/PFI 0 and PFI 1*
connectors are multi-directional connections for a number of
different signals.

Parent topic:

NI 5402 NI 5402 Overview

Related concepts:

- NI 5402 CH 0 Connector
- NI 5402 REF IN Connector
- NI 5402 SYNC OUT/PFI 0 and PFI 1 Connectors

<!--NI_TOPIC bundle=ni-fgen path=ni-5402-postamplifier-attenuation.html language=enus -->
## TOPIC 00117: NI 5402 Postamplifier Attenuation

- bundle_id: `ni-fgen`
- source_path: `ni-5402-postamplifier-attenuation.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5402-postamplifier-attenuation.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The postamplifier attenuation section is after the High-Gain and Low-Gain Amplifiers in the analog path. The attenuators provide a range of attenuation from 0 dB to a maximum of 36 dB in steps of 12 dB. NI-FGEN automatically controls the value of attenuation set in the postamplifier attenuation sect

### NI 5402 Postamplifier Attenuation

The postamplifier attenuation section is after the
High-Gain and Low-Gain Amplifiers in the *analog path*. The attenuators provide a
range of attenuation from 0 dB to a maximum of 36 dB in steps
of 12 dB. NI-FGEN automatically controls the value of attenuation
set in the postamplifier attenuation section dependent on the set
amplitude. You can read the value NI-FGEN has selected for postamplifier
attenuation using the 
Post-Amplifier Attenuation property or the 
NIFGEN_ATTR_POST_AMPLIFIER_ATTENUATION attribute.

Parent topic:

NI 5402 Attenuation

Related concepts:

- NI 5402 Analog Output

<!--NI_TOPIC bundle=ni-fgen path=ni-5402-power-up-and-reset-conditions.html language=enus -->
## TOPIC 00118: NI 5402 Power-Up and Reset Conditions

- bundle_id: `ni-fgen`
- source_path: `ni-5402-power-up-and-reset-conditions.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5402-power-up-and-reset-conditions.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The signal generator is in the following state from the time at which the computer begins to power up until the operating system is fully booted and NI-FGEN is loaded. The CH 0 analog output connector is disabled and has 50 Ω or 75 Ω impedance to ground. This impedance is the same as its previous se

### NI 5402 Power-Up and Reset Conditions

The signal generator is in the following state from
the time at which the computer begins to power up until the operating system is
fully booted and NI-FGEN is loaded.

- The CH 0 analog output connector is disabled and has
50 Ω or 75 Ω impedance to ground. This
impedance is the same as its previous setting before the device was
powered down. The output voltage amplitude of this connector
is 0 V.
- The REF IN connector has 50 Ω impedance to
ground.
- SYNC OUT/PFI 0 and PFI 1 are tristated and have a 1
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

- The digital filter of the NI 5402
inside the DAC is disabled.

- REF IN is disabled and has a 50 Ω
impedance to ground.
- SYNC OUT/PFI 0 and PFI 1 are tristated and have a 1
kΩ impedance to ground.

- PXI trigger or RTSI lines are tristated and floating.
- The sample rate is set to the maximum rate, with the Sample
clock source set to the internal Sample clock timebase.
- The Sample clock timebase is tuned by the internal reference
control voltage.

Parent topic:

NI 5402 NI 5402 Overview

<!--NI_TOPIC bundle=ni-fgen path=ni-5402-preamplifier-attenuation.html language=enus -->
## TOPIC 00119: NI 5402 Preamplifier Attenuation

- bundle_id: `ni-fgen`
- source_path: `ni-5402-preamplifier-attenuation.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5402-preamplifier-attenuation.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The preamplifier attenuation section is before the Low-Gain and High-Gain amplifiers in the analog path. The attenuators provide a range of attenuation from 0 to a maximum of 12 dB in steps of 3 dB. NI-FGEN automatically controls the value of attenuation set in the preamplifier attenuation section d

### NI 5402 Preamplifier Attenuation

The preamplifier attenuation section is before the
Low-Gain and High-Gain amplifiers in the *analog path*. The attenuators provide a
range of attenuation from 0 to a maximum of 12 dB in steps of
3 dB. NI-FGEN automatically controls the value of attenuation set
in the preamplifier attenuation section depending on the set
amplitude. You can read the value NI-FGEN has selected for preamplifier attenuation using the 
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

NI 5402 Attenuation

Related concepts:

- NI 5402 Analog Output

<!--NI_TOPIC bundle=ni-fgen path=ni-5402-pxi-front-panel.html language=enus -->
## TOPIC 00120: NI 5402 PXI Front Panel

- bundle_id: `ni-fgen`
- source_path: `ni-5402-pxi-front-panel.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5402-pxi-front-panel.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the front panel of the NI 5402 for the PXI bus. This front panel has four BNC connectors. The CH 0 connector is the analog output from which waveforms are generated. The REF IN connector provides the device with an external Reference clock. The SYNC OUT/PFI 0 and PFI 1 con

### NI 5402 PXI Front Panel

The following figure shows the front panel of the
NI 5402 for the PXI bus. This front panel has four BNC
connectors.

[IMAGE alt='image' src='GUID-35F51D5E-5950-40C8-B942-078A0CE87641-a5.gif']

The 
*CH 0* connector is the analog output
from which waveforms are generated.

The 
*REF IN* connector provides the
device with an external Reference clock.

The 
*SYNC OUT/PFI 0 and PFI 1*
connectors are multidirectional connections for a number of
different signals.

Parent topic:

NI 5402 NI 5402 Overview

Related concepts:

- NI 5402 CH 0 Connector
- NI 5402 REF IN Connector
- NI 5402 SYNC OUT/PFI 0 and PFI 1 Connectors

<!--NI_TOPIC bundle=ni-fgen path=ni-5402-ref-in-connector.html language=enus -->
## TOPIC 00121: NI 5402 REF IN Connector

- bundle_id: `ni-fgen`
- source_path: `ni-5402-ref-in-connector.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5402-ref-in-connector.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The REF IN front panel connector can accept an external Reference clock You must not change the Reference clock frequency while waveform generation is in progress. Only modify the frequency of the external clock before you start the waveform generation or after you stop the waveform generation. Ex

### NI 5402 REF IN Connector

Caution

not

before

after

#### External Reference Clock Input

The REF IN connector is an input that can accept a
Reference clock from an external source and phase lock the internal
clock of the signal generator to this external Reference clock.
Refer to the 
*device
specifications* for the allowable Reference clock frequencies
and signal characteristics.

The default value for the Reference clock source is
Internal. You can configure the Reference clock source and frequency by calling the 
niFgen Configure Reference Clock VI or the 
niFgen_ConfigureReferenceClock function.

Note

PLL Reference
Sources

Parent topic:

NI 5402 NI 5402 Overview

Related concepts:

- NI 5402 Reference Clock

<!--NI_TOPIC bundle=ni-fgen path=ni-5402-reference-clock.html language=enus -->
## TOPIC 00122: NI 5402 Reference Clock

- bundle_id: `ni-fgen`
- source_path: `ni-5402-reference-clock.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5402-reference-clock.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: A phase-locked loop (PLL) is a circuit that tunes the Sample clock timebase to phase–lock to an external Reference clock. The frequency stability and accuracy of the Sample clock timebase matches that of the Reference clock when the two phase–lock. Using the PLL on your device enables you to frequen

### NI 5402 Reference Clock

Note

device
specifications

The following figure shows the NI 5402
Reference Clock Source path.

[IMAGE alt='image' src='GUID-84532EF6-80F1-4F0C-A6C4-058D0C08BF61-a5.gif']

Note

NIFGEN_ATTR_REFERENCE_CLOCK_SOURCE

#### Reference Clock Sources

The NI 5402 is capable of
phase–locking its Sample clock timebase to an external
signal on the REF IN front panel connector. PXI devices can also
phase–lock to a 10 MHz Reference clock signal provided
by the PXI bus (PXI_CLK10), while PCI devices can phase–lock
to RTSI line 7 or to the onboard Reference clock.

The following table shows the valid NI-FGEN
property or attribute values and combinations to configure the
NI 5402 clock settings for an external Reference
clock.

| Sample Clock Source | PLL Reference Clock Source |
| --- | --- |
| Internal VXCO (100 MHz) | "None" (default) |
| "PXI_CLK10" (PXI), "RTSI7" (PCI) |  |
| "RefIn" |  |
| "OnboardRefClk" (PCI) |  |

Refer to the 
*device
specifications* for information about available REF IN signal
levels.

You can set up the clock by calling the 
niFgen Configure Reference Clock VI or the 
niFgen_ConfigureReferenceClock function.

Parent topic:

NI 5402 Clocking

<!--NI_TOPIC bundle=ni-fgen path=ni-5402-sample-clock.html language=enus -->
## TOPIC 00123: NI 5402 Sample Clock

- bundle_id: `ni-fgen`
- source_path: `ni-5402-sample-clock.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5402-sample-clock.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The signal generator provides a high-precision 100 MHz Voltage Controlled Crystal Oscillator (VCXO) clock source for the Sample clock timebase. The Sample clock timebase frequency is tuned by an Internal Calibration DAC Control Voltage. This clock is used to drive the DAC and all other waveform gene

### NI 5402 Sample Clock

The signal generator provides a high-precision
100 MHz Voltage Controlled Crystal Oscillator (VCXO) clock
source for the Sample clock timebase. The Sample clock timebase
frequency is tuned by an Internal Calibration DAC Control Voltage.
This clock is used to drive the DAC and all other waveform
generation operations on the device. The Internal Calibration DAC,
which is calibrated at the factory and which you can also
calibrate, provides for the Sample clock timebase to maintain a
high quality frequency source.

Parent topic:

NI 5402 Clocking

<!--NI_TOPIC bundle=ni-fgen path=ni-5402-signal-routing.html language=enus -->
## TOPIC 00124: NI 5402 Signal Routing

- bundle_id: `ni-fgen`
- source_path: `ni-5402-signal-routing.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5402-signal-routing.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: An NI signal generator is capable of sending and receiving signals through the front panel and the PXI or RTSI trigger bus. The front panel connectors provides connectivity for the output channel as well as for control lines for sending and receiving clocks, triggers, and events. You can use the PXI

### NI 5402 Signal Routing

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

NI 5402 Theory of Operation

Related concepts:

- NI 5402 Syntax for Terminal Names

<!--NI_TOPIC bundle=ni-fgen path=ni-5402-single-trigger-mode.html language=enus -->
## TOPIC 00125: NI 5402 Single Trigger Mode

- bundle_id: `ni-fgen`
- source_path: `ni-5402-single-trigger-mode.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5402-single-trigger-mode.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: When your application is configured for Single trigger mode, only one Start trigger is required to begin waveform generation. All Start triggers after the first Start trigger are ignored. Once the waveform generation is complete, the analog output indefinitely settles at the DC value of the last sam

### NI 5402 Single Trigger Mode

When your application is configured for Single
trigger mode, only one Start trigger is required to begin waveform
generation. All Start triggers after the first Start trigger are
ignored. Once the waveform generation is complete, the analog
output indefinitely settles at the DC value of the last sample in
the waveform. The
following table provides more information about
waveform generation behavior in Frequency List output mode.

| Output Mode | Trigger Behavior |
| --- | --- |
| Frequency List Mode | The device generates each step in the active frequency list sequentially. |

Parent topic:

NI 5402 Trigger Modes

<!--NI_TOPIC bundle=ni-fgen path=ni-5402-specifications.html language=enus -->
## TOPIC 00126: NI 5402 Specifications

- bundle_id: `ni-fgen`
- source_path: `ni-5402-specifications.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5402-specifications.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: For information about the signal generator specifications, refer to the device specifications. You can access these specifications by navigating to Start»All Programs»National Instruments» NI-FGEN»Documentation»NI Signal Generators Specifications, or you can visit ni.com/manuals.

### NI 5402 Specifications

For information about the signal generator
specifications, refer to the 
*device
specifications*. You can access these specifications by
navigating to 
Start»All Programs»National Instruments»
NI-FGEN»Documentation»NI Signal Generators Specifications, or you can visit 
ni.com/manuals.

Parent topic:

NI 5402 NI 5402 Overview

<!--NI_TOPIC bundle=ni-fgen path=ni-5402-standard-function-mode.html language=enus -->
## TOPIC 00127: NI 5402 Standard Function Mode

- bundle_id: `ni-fgen`
- source_path: `ni-5402-standard-function-mode.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5402-standard-function-mode.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Standard Function output mode is used to generate standard function waveforms such as sine, square, triangle, and so on. On the NI 5402, Standard Function mode is implemented through direct digital synthesis (DDS). DDS is a technique for deriving, under digital control, an analog frequency source fr

### NI 5402 Standard Function Mode

Standard Function output mode is used to generate standard
function waveforms such as sine, square, triangle, and so on. 
On the NI 5402, *Standard Function mode* is implemented
through *direct digital synthesis* (DDS). DDS is a technique for
deriving, under digital control, an analog frequency source from a
single Reference clock frequency. This technique produces
high-frequency accuracy and resolution, temperature stability,
wideband tuning, and rapid, phase-continuous frequency
switching.

In DDS mode, a fixed–size memory (called *lookup memory*) stores one cycle of a periodic waveform. A phase accumulator indexes the lookup memory. For each cycle of the device Sample clock, the sample of the waveform in lookup memory that is addressed by the phase accumulator is returned. The accumulator is then incremented by the value in the frequency control word (FCW). By adjusting the Frequency property or the NIFGEN_ATTR_FUNC_FREQUENCY attribute, NI-FGEN calculates the corresponding FCW, and you can vary the output frequency of the waveform in lookup memory. The phase accumulator increments in smaller steps for smaller FCWs. Accordingly, you need more samples to generate one waveform cycle, so the frequency is lower. A higher FCW results in a higher frequency. In DDS mode, the Sample clock does not vary with the frequency of the generated waveform. At higher frequencies, some waveform samples in lookup memory are skipped; at lower frequencies, some samples output multiple times in succession.

Parent topic:

NI 5402 Output Modes

Related concepts:

- Standard Function Mode
- Direct Digital Synthesis

<!--NI_TOPIC bundle=ni-fgen path=ni-5402-stepped-trigger-mode.html language=enus -->
## TOPIC 00128: NI 5402 Stepped Trigger Mode

- bundle_id: `ni-fgen`
- source_path: `ni-5402-stepped-trigger-mode.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5402-stepped-trigger-mode.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The waveform you downloaded generates each time a Start trigger occurs. After a waveform finishes generating, the last sample of the waveform repeats continuously until the next Start trigger is received. When the next Start trigger is received, the waveform generates again. If a Start trigger is re

### NI 5402 Stepped Trigger Mode

The waveform you downloaded generates each time a
Start trigger occurs. After a waveform finishes generating, the
last sample of the waveform repeats continuously until the next
Start trigger is received. When the next Start trigger is received,
the waveform generates again. If a Start trigger is received while
a waveform is generating, the Start trigger is ignored and another
Start trigger is required to regenerate the waveform after the last
sample generates. The
following table provides more information about
waveform generation behavior in Frequency List output mode.

| Output Mode | Trigger Behavior |
| --- | --- |
| Frequency List Mode | The device generates the next step in the active frequency list every time a Start trigger occurs. After the duration for a step has elapsed, the signal generation stops and remains at the configured DC offset level until the next Start trigger is received. When the next Start trigger is received, the next step in the frequency list is generated. After the final step, the frequency list repeats until generation is aborted. If the Trigger Source property or the NIFGEN_ATTR_TRIGGER_SOURCE attribute is set to NIFGEN_VAL_IMMEDIATE, the only way to advance to the next step in the frequency list is to call the niFgen Send Software Edge Trigger VI or the niFgen_SendSoftwareEdgeTrigger function. |

Parent topic:

NI 5402 Trigger Modes

<!--NI_TOPIC bundle=ni-fgen path=ni-5402-sync-out-pfi-0-and-pfi-1-connectors.html language=enus -->
## TOPIC 00129: NI 5402 SYNC OUT/PFI 0 and PFI 1 Connectors

- bundle_id: `ni-fgen`
- source_path: `ni-5402-sync-out-pfi-0-and-pfi-1-connectors.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5402-sync-out-pfi-0-and-pfi-1-connectors.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: SYNC OUT/PFI 0 and PFI 1 are bidirectional connectors. As an input, SYNC OUT/PFI 0 and PFI 1 terminals can accept a trigger from an external source that can start or step through waveform generation. As an output, the SYNC OUT/PFI 0 and PFI 1 lines can route a signal out from the following sources:

### NI 5402 SYNC OUT/PFI 0 and PFI 1 Connectors

SYNC OUT/PFI 0 and PFI 1 are bidirectional
connectors.

As an input, SYNC OUT/PFI 0 and PFI 1 terminals can
accept a trigger from an external source that can start or step
through waveform generation. As an output, the SYNC OUT/PFI 0 and
PFI 1 lines can route a signal out from the following sources:

- SYNC OUT
- Out Start trigger
- PLL Reference Clock source
- Sample Clock Out (with / 
 K , where K is an integer used to divide the Sample
clock)

Exporting Signals

device
specifications

Note

niFgen_ExportSignal

Parent topic:

NI 5402 NI 5402 Overview

Related concepts:

- NI 5402 Exporting Signals

<!--NI_TOPIC bundle=ni-fgen path=ni-5402-synchronization.html language=enus -->
## TOPIC 00130: NI 5402 Synchronization

- bundle_id: `ni-fgen`
- source_path: `ni-5402-synchronization.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5402-synchronization.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Your signal generator is based on the National Instruments Synchronization and Memory Core (SMC) technology and therefore supports TClk synchronization. Refer to the NI-TClk Synchronization Help for more information about NI-TClk Synchronization.

### NI 5402 Synchronization

Your signal generator is based on the 
National Instruments
Synchronization and Memory Core (SMC) technology and therefore
supports TClk synchronization. Refer to the 
NI-TClk
Synchronization Help for more information about NI-TClk
Synchronization.

Parent topic:

NI 5402 NI 5402 Overview

<!--NI_TOPIC bundle=ni-fgen path=ni-5402-syntax-for-terminal-names.html language=enus -->
## TOPIC 00131: NI 5402 Syntax for Terminal Names

- bundle_id: `ni-fgen`
- source_path: `ni-5402-syntax-for-terminal-names.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5402-syntax-for-terminal-names.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The syntax for terminal names is a unique identifier that refers to a physical terminal in your system. To guarantee the uniqueness of a terminal name across multiple devices, terminal names begin with a forward slash, followed by the name of the device as configured in MAX, such as Dev1. A forward

### NI 5402 Syntax for Terminal Names

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

NI 5402 Signal Routing

<!--NI_TOPIC bundle=ni-fgen path=ni-5402-theory-of-operation.html language=enus -->
## TOPIC 00132: NI 5402 Theory of Operation

- bundle_id: `ni-fgen`
- source_path: `ni-5402-theory-of-operation.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5402-theory-of-operation.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Expand this topic for information about the theory of operation of your signal generator.

### NI 5402 Theory of Operation

Expand this topic for information about the theory
of operation of your signal generator.

Parent topic:

NI 5402 NI 5402 Overview

<!--NI_TOPIC bundle=ni-fgen path=ni-5402-thermal-shutdown.html language=enus -->
## TOPIC 00133: NI 5402 Thermal Shutdown

- bundle_id: `ni-fgen`
- source_path: `ni-5402-thermal-shutdown.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5402-thermal-shutdown.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: NI-FGEN supports thermal shutdown capability for the NI 5402. This capability allows the signal generator to detect when it has reached a dangerously high temperature and to then power down to prevent damage to the device. Air circulation paths, fan settings, and space allowances are several factors

### NI 5402 Thermal Shutdown

NI-FGEN supports thermal shutdown capability for
the NI 5402. This
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
example, the niFgen Commit VI or
the niFgen_commit function and the niFgen Self Cal VI or the 
 niFgen_SelfCal function.
- MAX returns an error
message if you run a self-test on your device after it exceeds the
thermal shutdown temperature.

To re-enable your device after thermal shutdown,
use one of the following methods:

- Power down the computer or chassis that contains the signal
generator.

OR

- Call the niFgen Reset
Device VI or the niFgen_ResetDevice function or perform a device reset in MAX. For more
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

NI 5402 NI 5402 Overview

<!--NI_TOPIC bundle=ni-fgen path=ni-5402-trigger-modes.html language=enus -->
## TOPIC 00134: NI 5402 Trigger Modes

- bundle_id: `ni-fgen`
- source_path: `ni-5402-trigger-modes.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5402-trigger-modes.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5402 has four trigger modes: Single, Continuous, Stepped, and Burst. These trigger modes are available for Frequency List output mode. Refer to the niFgen Configure Trigger Mode VI or the niFgen_ConfigureTriggerMode function for information about setting the trigger mode.

### NI 5402 Trigger Modes

The NI 5402 has four trigger modes: Single, Continuous, Stepped,
and Burst. These trigger modes are available for Frequency List output mode.
Refer to the 
niFgen
Configure Trigger Mode VI or the 
niFgen_ConfigureTriggerMode function for information about setting the trigger mode.

Parent topic:

NI 5402 Triggering

<!--NI_TOPIC bundle=ni-fgen path=ni-5402-trigger-sources.html language=enus -->
## TOPIC 00135: NI 5402 Trigger Sources

- bundle_id: `ni-fgen`
- source_path: `ni-5402-trigger-sources.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5402-trigger-sources.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Trigger sources are software selectable. You can use any of the following external input triggers: SYNC OUT/ PFI 0 or PFI 1 on the front panel connectors RTSI<0..7> (PCI) lines or PXI_TRIG<0..7> lines and PXI_STAR on the PXI trigger bus backplane The following figure shows the possible trigger sourc

### NI 5402 Trigger Sources

Trigger sources are software selectable. You can
use any of the following external input triggers:

- SYNC OUT/ PFI 0 or PFI 1 on the front panel connectors

- RTSI<0..7> (PCI) lines or PXI_TRIG<0..7> lines and
PXI_STAR on the PXI trigger bus backplane

The following figure shows the possible trigger
sources for the NI 5402.

[IMAGE alt='image' src='GUID-6B1565C6-1A4C-475F-B781-7F36256489B7-a5.gif']

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

NI 5402 Triggering

Related concepts:

- NI 5402 Exporting Signals
- PXI Trigger Lines
- PXI Star Trigger Line

<!--NI_TOPIC bundle=ni-fgen path=ni-5402-trigger-timing.html language=enus -->
## TOPIC 00136: NI 5402 Trigger Timing

- bundle_id: `ni-fgen`
- source_path: `ni-5402-trigger-timing.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5402-trigger-timing.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the relationship between Start trigger and the waveform output. t[s1] is the required pulse width on the Start trigger signal. t[s2] is the delay from the Start trigger to the waveform output. Refer to the NI 5402 specifications for more information about these timing para

### NI 5402 Trigger Timing

The following figure shows the relationship between
Start trigger and the waveform output. t<sub>s1</sub> is the required pulse width on the Start trigger
signal. t<sub>s2</sub> is the delay from the Start trigger to the waveform
output. Refer to the 
*NI 5402
specifications* for more information about these timing
parameters.

[IMAGE alt='image' src='GUID-9DD6A51C-2BCA-4129-9C8D-0A821181925F-a5.gif']

The NI 5402 also allows you to export
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

NI 5402 Triggering

<!--NI_TOPIC bundle=ni-fgen path=ni-5402-triggering.html language=enus -->
## TOPIC 00137: NI 5402 Triggering

- bundle_id: `ni-fgen`
- source_path: `ni-5402-triggering.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5402-triggering.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can define the signal generator functionality by using the various triggering techniques. Expand this section to learn more about using triggers with your signal generator.

### NI 5402 Triggering

You can define the signal generator functionality
by using the various triggering techniques. Expand this section to
learn more about using triggers with your signal generator.

Parent topic:

NI 5402 NI 5402 Overview

<!--NI_TOPIC bundle=ni-fgen path=ni-5402-waveform-amplitude-control.html language=enus -->
## TOPIC 00138: NI 5402 Waveform Amplitude Control

- bundle_id: `ni-fgen`
- source_path: `ni-5402-waveform-amplitude-control.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5402-waveform-amplitude-control.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5402 uses both amplifiers and attenuators to achieve needed amplitude settings. Output Paths and Amplifiers The following figure shows two gain paths: the High-Gain Amplifier path and the Low-Gain Amplifier path. The Low-Gain Amplifier path has a 2 V [pk-pk] amplifier and is used for waveform

### NI 5402 Waveform Amplitude Control

The NI 5402 uses both amplifiers and
attenuators to achieve needed amplitude settings.

#### Output Paths and Amplifiers

The following figure shows two gain paths: the
High-Gain Amplifier path and the Low-Gain Amplifier path.

[IMAGE alt='image' src='GUID-D2930CC3-8665-48B1-BD41-FAC39E240C2D-a5.gif']

The Low-Gain Amplifier path has a 2 V 
<sub>pk-pk</sub> amplifier and is used for waveforms that have
output voltages equal to or smaller than 2.00 V 
<sub>pk-pk</sub> (1.67 V 
<sub>pk-pk</sub> for sine waveforms) into matched load impedance.
The High-Gain Amplifier path has a 10 V 
<sub>pk-pk</sub> amplifier and is used for waveforms that have
output voltages greater than 2.0 V 
<sub>pk-pk</sub> (1.67 V 
<sub>pk-pk</sub> for sine waveforms) into matched load impedance.
The gains of the amplifiers are constant and can be set by calling the 
Amplitude
property or the 
NIFGEN_ATTR_FUNC_AMPLITUDE attribute.

By default, NI-FGEN automatically selects the
High-Gain and Low-Gain Amplifiers based on the amplitude setting.
You can override NI-FGEN and configure the High-Gain or the
Low-Gain Amplifier to remain in the Analog Output path regardless
of amplitude by setting the 
Analog
Path property or the 
NIFGEN_ATTR_ANALOG_PATH attribute. Configuring the Low-Gain Amplifier path to remain
constant regardless of the amplitude setting affects the maximum
output value allowable for that particular amplitude setting. The
maximum amplitude setting for an Analog Output path configured to
Low-Gain Amplifier path is 2.0 (1.67 V 
<sub>pk-pk</sub> for sine waveforms). The maximum allowable
amplitude setting with NI-FGEN automatically selecting the Gain
Amplifier path is 10.0 V with a high load impedance.

In addition, the DC Offset Amplifier for adding 
*DC offset* to the signal is in
the High-Gain and Low-Gain Amplifier paths prior to the attenuators
and amplifiers. The DC Offset Amplifier can be fine-tuned for
adding offset to your signal. This fine-tuning of the main DC
Offset Amplifier is performed by the Offset DAC.

#### Square Wave Path

The NI 5402 uses dedicated hardware to
generate low-jitter square wave functions. A comparator is fed two
signals: a sine tone from the main DAC (using the Digital Filter
and the Analog Filter to obtain a 400 MS/s signal) and a DC signal
using the Level DAC.

The output of the comparator is switched back into
the Main path in order to obtain the desired amplitude and offset.
The fine gain control of the signal is controlled through the
Square Wave Gain DAC.

When the signal generator is configured to generate
a square waveform, NI-FGEN automatically selects the Square Wave
path. When the device is idle, it generates the low state of the
square waveform.

When using the Square Wave path, the 
*DC Offset* can be ±50% of the
current Amplitude.

The SYNC OUT is generated through the same
comparator and is routed by default to the SYNC OUT/PFI 0
connector. You can unroute this route or change the output terminal
of SYNC OUT using the 
niFgen
Export Signal VI or the 
niFgen_ExportSignal function.

Parent topic:

NI 5402 Analog Output

Related concepts:

- NI 5402 DC Offset

<!--NI_TOPIC bundle=ni-fgen path=ni-5402-waveform-generation.html language=enus -->
## TOPIC 00139: NI 5402 Waveform Generation

- bundle_id: `ni-fgen`
- source_path: `ni-5402-waveform-generation.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5402-waveform-generation.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5402 supports the following output, or generation, modes: Standard Function Frequency List To select an output mode, set the Output Mode parameter of the niFgen Configure Output Mode VI or the niFgen_ConfigureOutputMode function.

### NI 5402 Waveform Generation

The NI 5402 supports the
following output, or generation, modes:

- Standard Function
- Frequency List

To select an output mode, set the 
Output Mode parameter of the 
niFgen
Configure Output Mode VI or the 
niFgen_ConfigureOutputMode function.

Parent topic:

NI 5402 NI 5402 Overview

Related concepts:

- NI 5402 Standard Function Mode
- NI 5402 Frequency List Mode

<!--NI_TOPIC bundle=ni-fgen path=ni-5404-accessories.html language=enus -->
## TOPIC 00140: NI 5404 Accessories

- bundle_id: `ni-fgen`
- source_path: `ni-5404-accessories.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5404-accessories.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: National Instruments offers a variety of probes and cables to use with NI PXI-5404 signal generators. The following table lists recommended part numbers for cables that you can use with the NI PXI-5404. Device Cable Part Number Cable Description NI 5404 SMB 110 763405-01 50 Ω SMB male to BNC male, 1

### NI 5404 Accessories

National Instruments offers a variety of probes and
cables to use with NI PXI-5404 signal generators.

The following table lists recommended part numbers
for cables that you can use with the NI PXI-5404.

| Device | Cable | Part Number | Cable Description |
| --- | --- | --- | --- |
| NI 5404 | SMB 110 | 763405-01 | 50 Ω SMB male to BNC male, 1 m coaxial cable |
| NI 5404 | SMB 300 | 763388-01 | 50 Ω SMB male to alligator clip, 1 m cable |

For more information about these products, visit 
ni.com.

Parent topic:

NI 5404 NI PXI-5404 Overview

<!--NI_TOPIC bundle=ni-fgen path=ni-5404-analog-output.html language=enus -->
## TOPIC 00141: NI 5404 Analog Output

- bundle_id: `ni-fgen`
- source_path: `ni-5404-analog-output.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5404-analog-output.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Analog waveforms are generated by the following process: The direct digital synthesis output high-speed DAC receives the 12-bit digital waveform data from the direct digital synthesis chip. A lowpass filter filters the direct digital synthesis output. This filtered signal passes through the first am

### NI 5404 Analog Output

Analog waveforms are generated by the following
process:

1. The direct digital synthesis output high-speed DAC receives the
12-bit digital waveform data from the direct digital synthesis
chip.
2. A lowpass filter filters the direct digital synthesis
output.
3. This filtered signal passes through the first amplification
stage and then passes to a comparator to generate the 
 CLOCK out on the front
panel.
4. The amplified signal also passes through another amplification
stage.
5. The final amplified signal gets AC coupled and goes to the 
 SINE out.

Refer to the 
*NI PXI-5404 Block
Diagram* for more information about analog waveform
generation.

The following figure shows the timing relationships
of the trigger input and waveform output. t<sub>d1</sub> is the pulse width on the trigger signal. t<sub>d2</sub> is the time delay from trigger to output on the 
*SINE* out.

[IMAGE alt='image' src='GUID-7B826B23-BE3D-4262-85E0-16879144C1A1-a5.gif']

Parent topic:

NI 5404 Theory of Operation

Related concepts:

- NI 5404 CLOCK Out
- NI 5404 SINE Out
- NI 5404 Block Diagram

<!--NI_TOPIC bundle=ni-fgen path=ni-5404-block-diagram.html language=enus -->
## TOPIC 00142: NI 5404 Block Diagram

- bundle_id: `ni-fgen`
- source_path: `ni-5404-block-diagram.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5404-block-diagram.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the NI 5404 block diagram.

### NI 5404 Block Diagram

The following figure shows the NI 5404
block diagram.

[IMAGE alt='image' src='GUID-CBCC94FD-6849-48D5-A55B-CA67EF311E5A-a5.gif']

Parent topic:

NI 5404 Theory of Operation

<!--NI_TOPIC bundle=ni-fgen path=ni-5404-calibration.html language=enus -->
## TOPIC 00143: NI 5404 Calibration

- bundle_id: `ni-fgen`
- source_path: `ni-5404-calibration.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5404-calibration.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Before shipping you the NI 5404, NI calibrated your device to ensure that all features are within specifications. Calibration is a set of operations that compares the values indicated by a measuring instrument or measuring system to the corresponding values realized by external standards. The result

### NI 5404 Calibration

Before shipping you the NI 5404,
NI calibrated your device to ensure that all features are
within specifications.

Calibration is a set of operations that compares
the values indicated by a measuring instrument or measuring system
to the corresponding values realized by external standards. The
result of calibration can be used to determine the measurement
error and can correct for it in the adjustment process.

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

For more information about calibrating
NI signal generators, refer to 
ni.com/calibration.

Parent topic:

NI 5404 NI PXI-5404 Overview

<!--NI_TOPIC bundle=ni-fgen path=ni-5404-clock-out.html language=enus -->
## TOPIC 00144: NI 5404 CLOCK Out

- bundle_id: `ni-fgen`
- source_path: `ni-5404-clock-out.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5404-clock-out.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: CLOCK out provides the clock output. The maximum output levels on this connector depend on the type of load termination. If the CLOCK out of the NI PXI-5404 terminates into a high-impedance load (HiZ), you can configure the output levels with the software to 5 V, 3.3 V, or 1.8 V, as shown in the fol

### NI 5404 CLOCK Out

CLOCK out provides the clock output. The maximum
output levels on this connector depend on the type of load
termination. If the CLOCK out of the NI PXI-5404 terminates
into a high-impedance load (HiZ), you can configure the output
levels with the software to 5 V, 3.3 V, or 1.8 V, as shown in
the following figure. Therefore, the maximum level is 5 V.

[IMAGE alt='image' src='GUID-1D72177A-0A3E-40E7-A058-1A6D0AA5EE72-a5.gif']

If the CLOCK out of the NI PXI-5404 terminates
into a 50 Ω load, the output levels are 2.5 V,
1.65 V, or 0.9 V. Thus, the maximum level you can obtain is
2.5 V. If the output terminates into any other load, the
levels are determined by the following formula:

V<sub>out</sub>
 = [R<sub>L</sub>
 / (R<sub>L</sub>
 + 
R<sub>O</sub>
)] × 5 V

where

V <sub>out</sub>
 is the maximum output voltage level.

R<sub>L</sub>
 is the load impedance in ohms.

R<sub>O</sub>
 is the output impedance on the NI PXI-5404
and is equal to 50 Ω.

Note

Parent topic:

NI 5404 Connecting Signals

<!--NI_TOPIC bundle=ni-fgen path=ni-5404-connecting-signals.html language=enus -->
## TOPIC 00145: NI 5404 Connecting Signals

- bundle_id: `ni-fgen`
- source_path: `ni-5404-connecting-signals.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5404-connecting-signals.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the NI PXI-5404 front panel. The front panel contains five SMB connectors. The sine output generates through the connector labeled SINE, and the clock output generates through the connector labeled CLOCK.

### NI 5404 Connecting Signals

The following figure shows the NI PXI-5404
front panel. The front panel contains five SMB connectors. The sine
output generates through the connector labeled 
*SINE*, and the clock
output generates through the connector labeled 
*CLOCK*.

[IMAGE alt='image' src='GUID-DD928E0E-CAD6-475E-BDF4-4D3570541ACC-a5.gif']

Parent topic:

NI 5404 NI PXI-5404 Overview

Related concepts:

- NI 5404 SINE Out
- NI 5404 CLOCK Out

<!--NI_TOPIC bundle=ni-fgen path=ni-5404-continuous-trigger-mode.html language=enus -->
## TOPIC 00146: NI 5404 Continuous Trigger Mode

- bundle_id: `ni-fgen`
- source_path: `ni-5404-continuous-trigger-mode.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5404-continuous-trigger-mode.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The waveform you define in the staging list generates infinitely by continually cycling through the staging list. After a trigger is received, the waveform generation starts at the first stage, continues through the last stage, and loops back to the start of the first stage, continuing until you sto

### NI 5404 Continuous Trigger Mode

The waveform you define in the staging list generates infinitely by continually cycling through the staging list. After a trigger is received, the waveform generation starts at the first stage, continues through the last stage, and loops back to the start of the first stage, continuing until you stop the waveform generation. Only one trigger is required to start the waveform generation.

You can use Continuous trigger mode with both the Arbitrary Waveform output mode and Standard Function output mode, as shown in the following figures.

#### Continuous Trigger Mode for Arbitrary Waveform Output Mode

[IMAGE alt='image' src='GUID-E5D506C0-FDB3-4D46-9E9C-1A7F1BD88AB9-a5.gif']

#### Continuous Trigger Mode for Standard Function Output Mode

[IMAGE alt='image' src='GUID-A3F423FE-8B04-4542-B451-DA27ADE8C3A4-a5.gif']

Parent topic:

NI 5404 Trigger Mode

<!--NI_TOPIC bundle=ni-fgen path=ni-5404-generating-a-clock-signal-square-wave.html language=enus -->
## TOPIC 00147: NI 5404 Generating a Clock Signal (Square Wave)

- bundle_id: `ni-fgen`
- source_path: `ni-5404-generating-a-clock-signal-square-wave.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5404-generating-a-clock-signal-square-wave.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Initialize an NI-FGEN session for the appropriate device by calling the niFgen Initialize VI or the niFgen_init function. Set the appropriate standard function properties or attributes for the desired generation. Properties Attribute Value Waveform NIFGEN_ATTR_FUNC_WAVEFORM NIFGEN_VAL_WFM_SQUARE Fre

### NI 5404 Generating a Clock Signal (Square Wave)

1. Initialize an NI-FGEN session for the appropriate device by calling the 
niFgen
Initialize VI or the 
 niFgen_init function.
2. Set the appropriate standard function properties or attributes
for the desired generation.

| Properties | Attribute | Value |
| --- | --- | --- |
| Waveform | NIFGEN_ATTR_FUNC_WAVEFORM | NIFGEN_VAL_WFM_SQUARE |
| Frequency | NIFGEN_ATTR_FUNC_FREQUENCY | the desired frequency (Hz): 0 MHz to 105 MHz |
| Amplitude | NIFGEN_ATTR_FUNC_AMPLITUDE | the desired amplitude (Vpk-pk into a high impedance load): 1.8 V, 3.3 V, or 5 V |
| Duty Cycle High | NIFGEN_ATTR_FUNC_DUTY_CYCLE_HIGH | The desired duty cycle (%). Legal values vary by the frequency. |

1. Initiate the generation (niFgen_InitiateGeneration). The square
wave should be generated at CLOCK out.
2. If you want to stop the generation, do so by disabling the
output (niFgen
Output Enable VI or niFgen_ConfigureOutputEnabled function) and/or aborting the generation (niFgen Abort Generation VI or 
 niFgen_AbortGeneration function).
3. Close the NI-FGEN session (niFgen
Close VI or niFgen_close function).

The NI-FGEN driver installs a clock signal (square wave) programming example for the 5404. For the installation locations of the example files, refer to the *NI-FGEN Instrument Driver Readme*.

Parent topic:

NI 5404 Waveform Generation

<!--NI_TOPIC bundle=ni-fgen path=ni-5404-generating-a-sine-wave.html language=enus -->
## TOPIC 00148: NI 5404 Generating a Sine Wave

- bundle_id: `ni-fgen`
- source_path: `ni-5404-generating-a-sine-wave.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5404-generating-a-sine-wave.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Complete the following steps to generate a sine wave with the NI 5404. Initialize an NI-FGEN session to the appropriate device by calling the niFgen Initialize VI or the niFgen_init function. Set the appropriate standard function properties or attributes for the desired generation. Property Attribut

### NI 5404 Generating a Sine Wave

Complete the following steps to generate a sine
wave with the NI 5404.

1. Initialize an NI-FGEN session to the appropriate device by calling the niFgen
Initialize VI or the 
 niFgen_init function.
2. Set the appropriate standard function properties or attributes
for the desired generation.

| Property | Attribute | Value |
| --- | --- | --- |
| Waveform | NIFGEN_ATTR_FUNC_WAVEFORM | NIFGEN_VAL_WFM_SINE |
| Frequency | NIFGEN_ATTR_FUNC_FREQUENCY | Desired frequency (Hz), 0 MHz to 105 MHz |
| Amplitude | NIFGEN_ATTR_FUNC_AMPLITUDE | Desired amplitude (V pk-pk into a 50 Ω load), 1V pk-pk to 2 V pk-pk |

1. Initiate the generation by calling the 
niFgen
Initiate Generation VI or the
 niFgen_InitiateGeneration function. The sine wave should be generated at the SINE Out
terminal.
2. If you want to stop the generation, do so by disabling the
output by calling the 
niFgen
Output Enable VI or the 
 niFgen_ConfigureOutputEnabled function and/or aborting the generation by calling the 
niFgen
Abort Generation VI or the 
 niFgen_AbortGeneration function.
3. Close the NI-FGEN session by calling the 
niFgen
Close VI or the 
 niFgen_close function.

The NI-FGEN driver installs a sine wave generation programming example for the 5404. For the installation locations of the example files, refer to the *NI-FGEN Instrument Driver Readme*.

Parent topic:

NI 5404 Waveform Generation

<!--NI_TOPIC bundle=ni-fgen path=ni-5404-leds.html language=enus -->
## TOPIC 00149: NI 5404 LEDs

- bundle_id: `ni-fgen`
- source_path: `ni-5404-leds.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5404-leds.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5404 has two LEDs to indicate status: ACCESS and ACTIVE. ACCESS LED The ACCESS LED indicates basic hardware status. Color Indications Off Device is not ready, not yet functional, or the device has detected a problem with a power rail. Amber Amber indicates that the device is being accessed. G

### NI 5404 LEDs

The NI 5404 has two LEDs to indicate
status: ACCESS and ACTIVE.

#### ACCESS LED

The ACCESS LED indicates basic hardware status.

| Color | Indications |
| --- | --- |
| Off | Device is not ready, not yet functional, or the device has detected a problem with a power rail. |
| Amber | Amber indicates that the device is being accessed. |
| Green | The device is ready to be programmed by a driver. |

#### ACTIVE LED

The ACTIVE LED indicates the state of the
device.

| Color | Indications |
| --- | --- |
| Off | Device is disabled or in a stopped state. |
| Amber | Indicates that the device is armed and waiting for a Start trigger. Also used to indicate that a device is paused. |
| Green | Indicates that the device is generating a waveform. |
| Red | The device has detected an error. Software must access the device to determine the cause of the error. The LED remains red until the error condition is removed. Errors might be caused by the detection of an unlocked PLL that was previously locked, a PLL that is unlocked while in reset, the device remaining in a power-up state., or an error detected by software. |

Parent topic:

NI 5404 Connecting Signals

<!--NI_TOPIC bundle=ni-fgen path=ni-5404-locking-to-a-reference-clock.html language=enus -->
## TOPIC 00150: NI 5404 Locking to a Reference Clock

- bundle_id: `ni-fgen`
- source_path: `ni-5404-locking-to-a-reference-clock.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5404-locking-to-a-reference-clock.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The onboard clock of the NI 5404 can be locked to an external reference signal. This can be used when synchronizing multiple NI 5404 signal generators or whenever the output frequency needs to be locked to some external source. If no reference source is specified, the device will use an internal ref

### NI 5404 Locking to a Reference Clock

The onboard clock of the NI 5404 can be
locked to an external reference signal. This can be used when
synchronizing multiple NI 5404 signal generators or whenever
the output frequency needs to be locked to some external source. If
no reference source is specified, the device will use an internal
reference that can be adjusted during a device calibration.

The Reference clock source can be configured using
the 
niFgen Configure Reference Clock VI or the 
niFgen_ConfigureReferenceClock function or by setting the 
Reference Clock Source property or 
NIFGEN_ATTR_REF_CLOCK_SOURCE attribute directly. In addition to specifying the source of
the Reference clock signal, you must also specify its frequency.
The Reference clock frequency can be configured using the 
niFgen Configure Reference Clock VI or the 
niFgen_ConfigureReferenceClock function or by setting the 
Reference Clock Frequency property or the 
NIFGEN_ATTR_REF_CLOCK_FREQUENCY attribute directly. The NI 5404 can lock to
3 MHz to 20 MHz frequencies (in 1 MHz steps).

| Reference Source | Description |
| --- | --- |
| NIFGEN_VAL_REF_CLOCK_INTERNAL | No external reference is used. The device uses an internal reference. |
| NIFGEN_VAL_PXI_CLK10 | 10 MHz PXI backplane clock. |
| NIFGEN_VAL_REF_IN | REF IN connector on the NI 5404 front panel. |
| NIFGEN_VAL_RTSI_<0..6> | One of the RTSI/PXI trigger lines |
| NIFGEN_VAL_REF_CLOCK_RTSI_CLOCK | RTSI clock line (RTSI_7/PXI_Trig7) |

The NI-FGEN driver installs a synchronization programming example for the 5404. For the installation locations of the example files, refer to the *NI-FGEN Instrument Driver Readme*.

Parent topic:

NI 5404 Theory of Operation

<!--NI_TOPIC bundle=ni-fgen path=ni-5404-ni-pxi-5404-overview.html language=enus -->
## TOPIC 00151: NI 5404 NI PXI-5404 Overview

- bundle_id: `ni-fgen`
- source_path: `ni-5404-ni-pxi-5404-overview.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5404-ni-pxi-5404-overview.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5404 is a 100 MHz frequency generator with the following features: A 0 MHz to 105 MHz SINE out with adjustable amplitude from 1 V[pk-pk] to 2 V[pk-pk] into a 50 Ω load The SINE amplitude begins to fall off below 9 kHz. A 0 MHz to 105 MHz CLOCK out with 5 V, 3.3 V, or 1.8 V adjustable amplit

### NI 5404 NI PXI-5404 Overview

The NI 5404 is a 100 MHz frequency generator with
the following features:

- A 0 MHz to 105 MHz 
 SINE out with adjustable
amplitude from 1 V pk-pk to 2 V pk-pk into a 50 Ω load

Note

- A 0 MHz to 105 MHz 
 CLOCK out with 5 V,
3.3 V, or 1.8 V adjustable amplitude levels into high
impedance load

Note

- Phase-locked looping to an external Reference clock
- Synchronization of board outputs to an external trigger
- External calibration to establish onboard clock frequency
accuracy, sine amplitude accuracy, and square wave duty cycle
accuracy

Parent topic:

Devices

Related concepts:

- NI 5404 SINE Out
- NI 5404 CLOCK Out

<!--NI_TOPIC bundle=ni-fgen path=ni-5404-pfi-0-connector.html language=enus -->
## TOPIC 00152: NI 5404 PFI 0 Connector

- bundle_id: `ni-fgen`
- source_path: `ni-5404-pfi-0-connector.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5404-pfi-0-connector.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The PFI 0 connector is a bidirectional connector. As an input, the PFI 0 connector can accept a trigger from an external source that can initiate waveform generation. As an output, the PFI 0 connector can route out a signal from the following sources: CLOCK out Divided-down Sample clock timebase (20

### NI 5404 PFI 0 Connector

The PFI 0 connector is a bidirectional
connector. As an input, the PFI 0 connector can accept a
trigger from an external source that can initiate waveform generation.
As an output, the PFI 0 connector can route out a signal from
the following sources:

- CLOCK out
- Divided-down Sample clock timebase (20 MHz by default,
derived from VCXO generated clock)
- REF IN connector
- PXI 10 (backplane clock)
- Software trigger
- PXI star trigger
- PXI trigger bus (RTSI) lines

An input trigger should have values of 
V<sub>IH</sub>
 = 2.0 V and of 
V<sub>IL</sub>
 = 0.8 V.

The output trigger has values of 
V<sub>OH</sub>
 = 4.07 V and of 
V<sub>OL</sub>
 = 0.44 V into HiZ.

Parent topic:

NI 5404 Connecting Signals

<!--NI_TOPIC bundle=ni-fgen path=ni-5404-phase-locked-loop-and-module-synchron.html language=enus -->
## TOPIC 00153: NI 5404 Phase-Locked Loop and Module Synchronization

- bundle_id: `ni-fgen`
- source_path: `ni-5404-phase-locked-loop-and-module-synchron.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5404-phase-locked-loop-and-module-synchron.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5404 has an onboard, voltage-controlled crystal oscillator (VCXO) with a tuning range of ±50 ppm. The VCXO generates the main clock of 60 MHz. You can lock the PLL to a Reference clock source from the external REF IN connector, from any of the PXI trigger bus (RTSI) lines or from the 10 MHz b

### NI 5404 Phase-Locked Loop and Module Synchronization

The NI 5404 has an onboard,
voltage-controlled crystal oscillator (VCXO) with a tuning range of
±50 ppm. The VCXO generates the main clock of 60 MHz. You
can lock the PLL to a Reference clock source from the external REF
IN connector, from any of the PXI trigger bus (RTSI) lines or from
the 10 MHz backplane clock.

The PLL circuitry divides both the VCXO and the
Reference clock down to 1 MHz. A phase comparator then compares the
two 1 MHz signals and sends out an error signal. This error signal
is filtered and sent to the control pin of the VCXO whose frequency
gets adjusted. To achieve phase-locked looping correctly, the
external Reference clock must be a multiple of 1 MHz and should
have a frequency error of no more than ±50 ppm. The REF IN
connector handles frequencies from 3 MHz to 20 MHz and
amplitudes from 250 mV<sub>pk-pk</sub> to 5 V<sub>pk-pk</sub>.

The following figure shows the block diagram for
the NI 5404 PLL circuit.

[IMAGE alt='image' src='GUID-1E3CA614-45F4-4295-B0DE-B5A70FDAA84A-a5.gif']

Caution

not

pk-pk

Note

Parent topic:

NI 5404 NI PXI-5404 Overview

<!--NI_TOPIC bundle=ni-fgen path=ni-5404-phase-locked-looping.html language=enus -->
## TOPIC 00154: NI 5404 Phase-Locked Looping

- bundle_id: `ni-fgen`
- source_path: `ni-5404-phase-locked-looping.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5404-phase-locked-looping.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5404 has a PLL that optionally phase-locks the device clock to a Reference clock. With the NI 5404, you can phase-lock to the PXI backplane clock, an external Reference clock that is brought in through the REF IN front panel connector, or a clock brought in from practically any other source.

### NI 5404 Phase-Locked Looping

The NI 5404 has a PLL that optionally
phase-locks the device clock to a Reference clock. With the
NI 5404, you can phase-lock to the PXI backplane clock, an
external Reference clock that is brought in through the REF IN
front panel connector, or a clock brought in from practically any
other source. If you use an external clock, the nominal value of
the frequency must be 10 MHz and the frequency must be within
100 ppm of 10 MHz. When phase-locking is disabled, the
voltage from a DAC determines the frequency of the device clock.
The value of this voltage provided by the DAC is established during
factory calibration. The following figure shows the components and
possible configurations of the phase-locking circuitry.

[IMAGE alt='image' src='GUID-532D6FF5-7795-4160-B625-1A6653D55103-a5.gif']

Parent topic:

NI 5404 NI PXI-5404 Overview

<!--NI_TOPIC bundle=ni-fgen path=ni-5404-power-up-and-reset-conditions.html language=enus -->
## TOPIC 00155: NI 5404 Power-Up and Reset Conditions

- bundle_id: `ni-fgen`
- source_path: `ni-5404-power-up-and-reset-conditions.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5404-power-up-and-reset-conditions.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: When you power up the computer, the NI 5404 is in the following state: The outputs do not have a signal. REF IN and PFI 0 connectors are not functional and do not react to any input signals. When you reset the device using NI-FGEN, the NI 5404 is in the following state: The device is stopped (not ge

### NI 5404 Power-Up and Reset Conditions

When you power up the computer, the
NI 5404 is in the following state:

- The outputs do not have a signal.
- REF IN and PFI 0 connectors are not functional and do not
react to any input signals.

When you reset the device using NI-FGEN, the
NI 5404 is in the following state:

- The device is stopped (not generating).
- The SINE and CLOCK output terminals are enabled, but no signal
is seen because the device is not generating.
- CLOCK and SINE output amplitudes are set to their maximum
values.
- CLOCK and SINE frequencies are set to 1 MHz.
- The PLL reference source is set to internal tuning (the VCXO is
not locked to an external reference signal).
- The CLOCK duty cycle is set to 50%.
- Trigger source is set to immediate.

Parent topic:

NI 5404 NI PXI-5404 Overview

<!--NI_TOPIC bundle=ni-fgen path=ni-5404-ref-in-connector.html language=enus -->
## TOPIC 00156: NI 5404 REF IN Connector

- bundle_id: `ni-fgen`
- source_path: `ni-5404-ref-in-connector.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5404-ref-in-connector.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The REF IN connector is a PLL input connector that can accept a Reference clock from an external source and frequency lock the NI 5404 internal clock to this external clock. The Reference clock can be 3 MHz to 20 MHz in 1 MHz steps. The clock should not deviate more than ±50 ppm from its nominal fre

### NI 5404 REF IN Connector

pk-pk

pk-pk

Note

If an external Reference clock is not available,
the NI 5404 automatically tunes the internal clock to the
highest accuracy possible.

Parent topic:

NI 5404 Connecting Signals

<!--NI_TOPIC bundle=ni-fgen path=ni-5404-ref-out-connector.html language=enus -->
## TOPIC 00157: NI 5404 REF OUT Connector

- bundle_id: `ni-fgen`
- source_path: `ni-5404-ref-out-connector.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5404-ref-out-connector.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The REF OUT connector is an output connector that can route out a signal from the following sources: CLOCK out Divided-down Sample clock timebase (20 MHz by default, derived from VCXO generated clock) REF IN connector PXI 10 (backplane clock) Software trigger PXI star trigger PFI 0 connector PXI tri

### NI 5404 REF OUT Connector

The REF OUT connector is an output connector that
can route out a signal from the following sources:

- CLOCK out
- Divided-down Sample clock timebase (20 MHz by default,
derived from VCXO generated clock)
- REF IN connector
- PXI 10 (backplane clock)
- Software trigger
- PXI star trigger
- PFI 0 connector
- PXI trigger bus (RTSI lines)

The output clock has values of 
V<sub>OH</sub> = 4.07 V and of 
V<sub>OL</sub> = 0.44 V into HiZ. Rise and fall time for the
output clock is 2.4 ns.

Parent topic:

NI 5404 Connecting Signals

<!--NI_TOPIC bundle=ni-fgen path=ni-5404-routing-exporting-signals.html language=enus -->
## TOPIC 00158: NI 5404 Routing/Exporting Signals

- bundle_id: `ni-fgen`
- source_path: `ni-5404-routing-exporting-signals.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5404-routing-exporting-signals.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Many different signals can be routed and exported from the NI PXI-5404. A route is made using niFgen Route Signal Out VI or the niFgen_RouteSignalOut function by specifying the desired source signal or terminal and the desired destination terminal. The following table lists the signal sources for th

### NI 5404 Routing/Exporting Signals

Many different signals can be routed and exported
from the NI PXI-5404. A route is made using 
niFgen
Route Signal Out VI or the 
niFgen_RouteSignalOut function by specifying the desired source signal or terminal
and the desired destination terminal.

The following table lists the signal sources for
the NI 5404.

| Source | Description |
| --- | --- |
| NIFGEN_VAL_NONE | Routes nothing to the destination terminal—effectively clears any routes to the terminal |
| NIFGEN_VAL_CLOCK_OUT | CLOCK out signal |
| NIFGEN_VAL_OUT_START_TRIGGER | Start trigger signal |
| NIFGEN_VAL_SOFTWARE_TRIG | Signal generated by niFgen Send Software Edge Trigger VI or niFgen_SendSoftwareEdgeTrigger function |
| NIFGEN_VAL_BOARD_CLOCK | 20 MHz signal derived from the Sample clock timebase |
| NIFGEN_VAL_REF_IN | REF IN connector on the NI 5404 front panel |
| NIFGEN_VAL_PXI_CLK10 | 10 MHz PXI backplane clock |
| NIFGEN_VAL_PXI_STAR | PXI star trigger line |
| NIFGEN_VAL_PFI_0 | PFI 0 connector on the NI 5404 front panel |
| NIFGEN_VAL_RTSI_<0..7> | One of the RTSI/PXI trigger lines |

The following table lists the destination of
signals from the NI 5404.

| Destination | Description |
| --- | --- |
| NIFGEN_VAL_REF_OUT | REF OUT connector on the NI 5404 front panel |
| NIFGEN_VAL_PFI_0 | PFI 0 connector on the NI 5404 front panel |
| NIFGEN_VAL_RTSI_<0..7> | One of the RTSI/PXI trigger lines |
| NIFGEN_VAL_REF_CLOCK_RTSI_CLOCK | RTSI_CLOCK line (RTSI/PXI_7) |

Parent topic:

NI 5404 NI PXI-5404 Overview

<!--NI_TOPIC bundle=ni-fgen path=ni-5404-rtsi-pxi-trigger-lines.html language=enus -->
## TOPIC 00159: NI 5404 RTSI/PXI Trigger Lines

- bundle_id: `ni-fgen`
- source_path: `ni-5404-rtsi-pxi-trigger-lines.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5404-rtsi-pxi-trigger-lines.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXI-5404 allows for a variety of signals to be routed to, and from, the PXI trigger (RTSI) lines. As a source, these lines can be sent to the PFI 0 connector and used to trigger other devices in the system. You can also route RTSI lines to the REF OUT connector and use them to provide a clock

### NI 5404 RTSI/PXI Trigger Lines

The NI PXI-5404 allows for a variety of
signals to be routed to, and from, the PXI trigger (RTSI)
lines.

As a source, these lines can be sent to the PFI
0 connector and used to trigger other devices in the system.
You can also route RTSI lines to the REF OUT connector and use them
to provide a clock to other devices. Additionally, any of these
lines can be routed to other RTSI lines.

The following figure shows all the routes for RTSI
lines.

[IMAGE alt='image' src='GUID-4F760416-49F9-4D7F-97DF-4C55A330D31A-a5.gif']

As a sink, RTSI lines can receive the
following:

- Start trigger
- Divided-down, onboard clock (20 MHz by default)
- Software trigger
- REF IN
- PXI 10
- PXI star
- PFI 0
- CLOCK
- Other RTSI lines

The following figure describes all the possible
routes with the RTSI lines at the sink of the route.

[IMAGE alt='image' src='GUID-7C8328EC-C555-4FF5-A63E-CDD0FBFD9AF4-a5.gif']

Note

BOARD CLOCK/N

N

N

Parent topic:

NI 5404 Trigger Sources

Related concepts:

- NI 5404 REF IN Connector
- NI 5404 CLOCK Out

<!--NI_TOPIC bundle=ni-fgen path=ni-5404-sine-out.html language=enus -->
## TOPIC 00160: NI 5404 SINE Out

- bundle_id: `ni-fgen`
- source_path: `ni-5404-sine-out.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5404-sine-out.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The SINE out provides the sine wave output. The maximum output levels on this connector depend on the type of load termination. For example, if the output of the NI PXI-5404 terminates into a 50 Ω load, the output levels are adjustable to a maximum of ±1 V, while the maximum output levels are ±2 V w

### NI 5404 SINE Out

The SINE out provides the sine wave output. The
maximum output levels on this connector depend on the type of load
termination. For example, if the output of the NI PXI-5404 terminates into
a 50 Ω load, the output levels are adjustable to a
maximum of ±1 V, while the maximum output levels are ±2 V when the device terminates into a high-impedance load (HiZ). This difference is illustrated in the following figure.

[IMAGE alt='image' src='GUID-5F52D77B-5450-45B2-9A77-9453A12D4100-a5.gif']

If the output terminates into any other
load, the levels are determined by the following formula:

V<sub>out</sub>
 = ± [ R<sub>L</sub>
 / (R<sub>L</sub>
 + R<sub>O</sub>
)] × 2 V

where

V<sub>out</sub>
 is the maximum output voltage level.

R<sub>L</sub>
 is the load impedance in ohms.

O

Note

Parent topic:

NI 5404 Connecting Signals

<!--NI_TOPIC bundle=ni-fgen path=ni-5404-specifications.html language=enus -->
## TOPIC 00161: NI 5404 Specifications

- bundle_id: `ni-fgen`
- source_path: `ni-5404-specifications.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5404-specifications.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: For information about the NI PXI-5404 specifications, refer to the NI PXI-5404 Specifications. You can access these specifications by navigating to Start»All Programs»National Instruments»NI-FGEN»Documentation»NI Signal Generators Specifications, or you can visit ni.com/manuals.

### NI 5404 Specifications

For information about the NI PXI-5404
specifications, refer to the 
*NI PXI-5404 Specifications*. You can access these specifications by
navigating to 
Start»All Programs»National
Instruments»NI-FGEN»Documentation»NI Signal Generators Specifications,
or you can visit 
ni.com/manuals.

Parent topic:

NI 5404 NI PXI-5404 Overview

<!--NI_TOPIC bundle=ni-fgen path=ni-5404-start-conditions.html language=enus -->
## TOPIC 00162: NI 5404 Start Conditions

- bundle_id: `ni-fgen`
- source_path: `ni-5404-start-conditions.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5404-start-conditions.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: SINE Out The sine waveform is configured by three parameters: frequency, amplitude, and phase. All the parameters are sent to the direct digital synthesis chip at the same time; however, because of delays within the chip, the phase and amplitude are set before the frequency. The result of these dela

### NI 5404 Start Conditions

#### SINE Out

The sine waveform is configured by three
parameters: frequency, amplitude, and phase. All the parameters are
sent to the direct digital synthesis chip at the same time;
however, because of delays within the chip, the phase and amplitude
are set before the frequency. The result of these delay differences
is a DC voltage at the SINE out before the sine signal appears. The
duration of this DC signal is about 100 ns, and its level
depends on the given phase and amplitude. You can see this start up
condition for different phase settings in the following
figures.

[IMAGE alt='image' src='GUID-86BCF973-1E41-4228-BD5F-72E567E20BDD-a5.gif']

#### Sine Output Starting for Phase Set to 45 Degrees

[IMAGE alt='image' src='GUID-2FDBA99B-5FB3-4372-8EDD-50595CF1305C-a5.gif']

#### Sine Output Starting for Phase Set to 90 Degrees

Because a phase of 0° or 180° corresponds to a
starting amplitude of 0 V, you can use one of these two phase
settings to eliminate this particular start up condition. Refer to
the following figure for an example of a start phase of 0°.

[IMAGE alt='image' src='GUID-C72C653A-6C66-4303-8B8B-05D08578D3D8-a5.gif']

#### Sine Output Starting for Phase Set to 0 Degrees

In addition, when generating higher frequencies, a
runt pulse exists upon start-up. Refer to the following figure for
an example of a runt pulse.

[IMAGE alt='image' src='GUID-D22F324F-1677-43B4-B796-FEB2DB4E175D-a5.gif']

#### Runt Pulse on SINE Output When Starting at a High Frequency for
Phase Equal to Zero

#### CLOCK Out

#### CLOCK Out

The start condition of the CLOCK out depends on the
start phase of the SINE out. Therefore, a runt pulse may occur upon
starting the clock. Refer to the following figure for an example of
a runt pulse.

[IMAGE alt='image' src='GUID-AEBED504-A90A-4F87-8FB2-4ECF8F5C93BB-a5.gif']

#### Runt Pulse on Start-up of CLOCK Output for Phase Equal to
Zero

For certain phase settings, the runt pulse does not
occur. To eliminate the runt pulse on the CLOCK out, experiment
with the starting phase setting.

Also, because of the different output paths of the
CLOCK out and SINE out, a fixed delay exists after the SINE out
initiates until the CLOCK out initiates.

Parent topic:

NI 5404 Waveform Generation

<!--NI_TOPIC bundle=ni-fgen path=ni-5404-theory-of-operation.html language=enus -->
## TOPIC 00163: NI 5404 Theory of Operation

- bundle_id: `ni-fgen`
- source_path: `ni-5404-theory-of-operation.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5404-theory-of-operation.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Expand this topic for information about the NI 5404 theory of operation.

### NI 5404 Theory of Operation

Expand this topic for information about the
NI 5404 theory of operation.

Parent topic:

NI 5404 NI PXI-5404 Overview

<!--NI_TOPIC bundle=ni-fgen path=ni-5404-trigger-mode.html language=enus -->
## TOPIC 00164: NI 5404 Trigger Mode

- bundle_id: `ni-fgen`
- source_path: `ni-5404-trigger-mode.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5404-trigger-mode.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5404 has only one trigger mode: Continuous.

### NI 5404 Trigger Mode

The NI 5404 has only one trigger mode: 
*Continuous*.

Parent topic:

NI 5404 Triggering

Related concepts:

- NI 5404 Continuous Trigger Mode

<!--NI_TOPIC bundle=ni-fgen path=ni-5404-trigger-sources.html language=enus -->
## TOPIC 00165: NI 5404 Trigger Sources

- bundle_id: `ni-fgen`
- source_path: `ni-5404-trigger-sources.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5404-trigger-sources.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: By default, the NI PXI-5404 starts immediately, after initiating a generation in software, unless a trigger is selected. When you use the Start trigger option, you can software select from one of the following sources: PXI trigger bus (RTSI) line PFI 0 (front panel connector) PXI star Software trigg

### NI 5404 Trigger Sources

By default, the NI PXI-5404 starts
immediately, after initiating a generation in software, unless a
trigger is selected. When you use the Start trigger option, you can
software select from one of the following sources:

- PXI trigger bus (RTSI) line
- PFI 0 (front panel connector)
- PXI star
- Software trigger

The following figure shows the trigger sources for
the NI 5404.

[IMAGE alt='image' src='GUID-E87FC8BA-AFF8-4987-A058-A8C4A13D5D2D-a5.gif']

#### Waveform Generation Trigger Sources

If you need to automatically trigger the waveform
generation, use software to generate the triggers. You need a
rising TTL edge for external triggering.

For external triggering, apply a rising-edge TTL
signal to the PFI 0 input. This signal should remain
de-asserted (logic low) until after the software has initialized
the waveform generation.

Parent topic:

NI 5404 Triggering

<!--NI_TOPIC bundle=ni-fgen path=ni-5404-triggering.html language=enus -->
## TOPIC 00166: NI 5404 Triggering

- bundle_id: `ni-fgen`
- source_path: `ni-5404-triggering.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5404-triggering.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: NI-FGEN allows you to start generation immediately. You can also use a software trigger or an external digital trigger. If you configure the generation to start immediately, the waveform outputs as soon as the niFgen Initiate Generation VI or the niFgen_InitiateGeneration function is called. If you

### NI 5404 Triggering

NI-FGEN allows you to start generation immediately.
You can also use a software trigger or an external digital trigger.
If you configure the generation to start immediately, the waveform
outputs as soon as the 
niFgen
Initiate Generation VI or the 
niFgen_InitiateGeneration function is called. If you specify a software trigger, the
generation does not start as soon as Initiate Generation is called;
instead the generation waits until the 
niFgen Send Software Edge Trigger VI or the 
niFgen_SendSoftwareEdgeTrigger function is called. If you specify an external trigger, the
generation does not begin until a rising edge is detected on the
specified source terminal.

You can configure the trigger source by calling the
niFgen Configure Trigger (poly) VI or the 
niFgen_ConfigureDigitalEdgeStartTrigger
niFgen_ConfigureSoftwareEdgeStartTrigger functions or by
setting the 
Trigger
Source property or the 
NIFGEN_ATTR_TRIGGER_SOURCE attribute directly. You can change standard function
properties or attributes, such as frequency, phase, and amplitude,
while generating a waveform. If you configure the generation to
trigger immediately, the change takes effect as soon as the
property or attribute is changed. If you trigger the generation
using software or an external digital trigger, the change does not
take effect until the next trigger is received. For example,
imagine that the trigger source is a software trigger and a
generation is in progress. If you change the 
Frequency
property or the 
NIFGEN_ATTR_FUNC_FREQUENCY attribute, the output frequency does not actually change until
you call the niFgen Send Software Edge Trigger VI or the 
niFgen_SendSoftwareEdgeTrigger
function again.

| Trigger | Source Description |
| --- | --- |
| NIFGEN_VAL_IMMEDIATE | No trigger is used. Generation starts and updates happen immediately. |
| NIFGEN_VAL_SOFTWARE_TRIG | The software trigger function call. |
| NIFGEN_VAL_PFI_0 | The PFI 0 connector on the NI 5404 front panel. |
| NIFGEN_VAL_RTSI_<0..7> | One of the RTSI/PXI trigger lines. |
| NIFGEN_VAL_PXI_STAR | The PXI star trigger line. |

Parent topic:

NI 5404 NI PXI-5404 Overview

<!--NI_TOPIC bundle=ni-fgen path=ni-5404-waveform-generation.html language=enus -->
## TOPIC 00167: NI 5404 Waveform Generation

- bundle_id: `ni-fgen`
- source_path: `ni-5404-waveform-generation.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5404-waveform-generation.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5404 frequency generator can generate sine or square waves at frequencies between 0 MHz and 105 MHz. NI-FGEN supports the NI 5404 in Standard Function mode only (the Output Mode property and the NIFGEN_ATTR_OUTPUT_MODE attribute can only be set to NIFGEN_VAL_OUTPUT_FUNC). In the standard func

### NI 5404 Waveform Generation

The NI 5404 frequency generator can generate
sine or square waves at frequencies between 0 MHz and
105 MHz. 
NI-FGEN supports the NI 5404 in
Standard Function mode only (the 
Output
Mode property and the 
NIFGEN_ATTR_OUTPUT_MODE attribute can only be set to 
NIFGEN_VAL_OUTPUT_FUNC). In the
standard function output mode, you can configure the following
waveform properties: 
Waveform,
Frequency,
Amplitude,
DC Offset,
Start
Phase, and 
Duty
Cycle High ( 
NIFGEN_ATTR_FUNC_WAVEFORM , 
NIFGEN_ATTR_FUNC_FREQUENCY , 
NIFGEN_ATTR_FUNC_AMPLITUDE , 
NIFGEN_ATTR_FUNC_DC_OFFSET , 
NIFGEN_ATTR_FUNC_START_PHASE , and 
NIFGEN_ATTR_FUNC_DUTY_CYCLE_HIGH attributes, respectively). You can configure many of these
properties and attributes using the 
niFgen Configure Standard Waveform VI or the 
niFgen_ConfigureStandardWaveform function.

The waveform output terminals on the NI 5404, 
*SINE* out and 
*CLOCK* out, are closely
related. The TTL signal at CLOCK out is derived from the sine
wave. Therefore, the two terminals are treated as the same channel
in NI-FGEN. Enabling and disabling the output affects both
terminals. When the frequency and phase properties or attributes
are set, both terminals are affected simultaneously. You can set
amplitude and duty cycle on each terminal independently (DC offset
can be read but not set). When you set or get one of these
properties or attributes, the result depends on the value of the
Waveform property or the 
NIFGEN_ATTR_FUNC_WAVEFORM
attribute.

The Waveform property or the 
NIFGEN_ATTR_FUNC_WAVEFORM attribute
determines which terminal is being configured when you set certain
properties or attributes. When the waveform is set to a sine wave
(the 
Waveform
property or the 
NIFGEN_ATTR_FUNC_WAVEFORM attribute is set to 
NIFGEN_VAL_WFM_SINE), setting the
amplitude configures the output of SINE out. Accordingly, if the
waveform is set to a square wave ( 
NIFGEN_VAL_WFM_SQUARE), you can
configure the amplitude and duty cycle of the TTL signal at the
CLOCK out. The settings specific to each terminal are preserved
when the Waveform property or the 
NIFGEN_ATTR_FUNC_WAVEFORM attribute
is changed, so both SINE out and CLOCK out can be configured
separately in the same session.

#### Related Topics

*Generating a Sine
Wave*

*Generating a Clock
Signal (Square Wave)*

*Locking to a Reference Clock*

*Routing/Exporting
Signals*

Parent topic:

NI 5404 NI PXI-5404 Overview

Related concepts:

- NI 5404 SINE Out
- NI 5404 CLOCK Out
- NI 5404 Generating a Sine Wave
- NI 5404 Generating a Clock Signal (Square Wave)
- NI 5404 Locking to a Reference Clock
- NI 5404 Routing/Exporting Signals

<!--NI_TOPIC bundle=ni-fgen path=ni-5406-aborting-generation.html language=enus -->
## TOPIC 00168: NI 5406 Aborting Generation

- bundle_id: `ni-fgen`
- source_path: `ni-5406-aborting-generation.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5406-aborting-generation.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can abort the generation of the current waveform. Aborting the generation exhibits different behaviors for different waveform output modes. Whether in Standard Function mode or Frequency List mode, the NI 5406 signal generator aborts all waveforms, with the exception of the square waveform, to g

### NI 5406 Aborting Generation

You can abort the generation of the current
waveform. Aborting the generation exhibits different behaviors for
different 
*waveform output
modes*.

Whether in Standard Function mode or Frequency List mode, the NI 5406 signal generator aborts all waveforms, with the exception of the square waveform, to ground. When aborting to ground, the signal remains at the level for which the DC offset is configured. Square waveform signals drop to low when aborted.

Related Topics

*Aborting to Ground*

Parent topic:

NI 5406 Waveform Generation

Related concepts:

- NI 5406 Waveform Generation
- Abort to Ground

<!--NI_TOPIC bundle=ni-fgen path=ni-5406-access-and-active-leds.html language=enus -->
## TOPIC 00169: NI 5406 ACCESS and ACTIVE LEDs

- bundle_id: `ni-fgen`
- source_path: `ni-5406-access-and-active-leds.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5406-access-and-active-leds.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The ACCESS and ACTIVE LEDs indicate the status of the PXI module: ACCESS LED The ACCESS LED indicates basic hardware status as shown in the following table. Color Indications Off Device is not yet functional, or the device has detected a problem with a power rail. Amber The device is being accessed.

### NI 5406 ACCESS and ACTIVE LEDs

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

NI 5406 NI 5406 Overview

<!--NI_TOPIC bundle=ni-fgen path=ni-5406-accessories.html language=enus -->
## TOPIC 00170: NI 5406 Accessories

- bundle_id: `ni-fgen`
- source_path: `ni-5406-accessories.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5406-accessories.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: National Instruments offers a variety of products to use with your signal generator, including cables and other accessories. Visit ni.com for more information.

### NI 5406 Accessories

National Instruments offers a variety of products
to use with your signal generator, including cables and other
accessories. Visit 
ni.com for more
information.

Parent topic:

NI 5406 NI 5406 Overview

<!--NI_TOPIC bundle=ni-fgen path=ni-5406-analog-filter.html language=enus -->
## TOPIC 00171: NI 5406 Analog Filter

- bundle_id: `ni-fgen`
- source_path: `ni-5406-analog-filter.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5406-analog-filter.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The analog filter is a lowpass filter that is used to eliminate aliased images and artifacts due to the digital-to-analog conversion from the signal from the DAC. In general, use the analog filter for signals containing a large portion of sinusoidal content, such as AM and FM, sinc pulse, and sinuso

### NI 5406 Analog Filter

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

NI 5406 Filtering Effects

Related concepts:

- Aliased Images
- Filtering and Interpolation

<!--NI_TOPIC bundle=ni-fgen path=ni-5406-analog-output.html language=enus -->
## TOPIC 00172: NI 5406 Analog Output

- bundle_id: `ni-fgen`
- source_path: `ni-5406-analog-output.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5406-analog-output.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the NI 5406 Analog Output signal path. NI 5406 Analog waveforms are generated as follows: The digital waveform data from the Standard Function Generation Engine is passed to a digital gain circuit and then high-speed DAC. This DAC also implements a portion of the output si

### NI 5406 Analog Output

The following figure shows the NI 5406
Analog Output signal path.

[IMAGE alt='image' src='GUID-D2930CC3-8665-48B1-BD41-FAC39E240C2D-a5.gif']

NI 5406 Analog waveforms are generated as
follows:

1. The digital waveform data from the Standard Function Generation
Engine is passed to a digital gain circuit and then high-speed DAC.
This DAC also implements a portion of the output signal path
attenuation with a range of 0 dB to 3 dB. Refer to the 
 NI PXI/PCI-5402/5406
Specifications for the exact resolution. You can adjust the
amount of attenuation by configuring the Amplitude property or the 
 NIFGEN_ATTR_FUNC_AMPLITUDE attribute. NI-FGEN calculates and sets the correct amount of attenuation required, corresponding to the gain setting.
2. Following the DAC, the signal then passes through a switchable
lowpass Analog Filter to remove 
 Aliased Images . For
User-defined waveforms created in Standard Function mode or
Frequency List mode, you can select whether to include the Analog
Filter in the Analog Output path using either the 
niFgen Configure Analog Filter VI or the 
 niFgen_EnableAnalogFilter and 
 niFgen_DisableAnalogFilter functions.
3. Either the Main path output or the Square Wave Output path is
selected based on the desired waveform which then passes through
the DC Offset Amplifier that adds the desired DC offset voltage.
For User-defined waveform created in Standard Function mode or
Frequency List mode, you can adjust the amount of DC offset added
to the signal up to ±5 V 
 pk including AC and DC components into 50 Ω
impedance. Refer to the 
DC
Offset property, or the 
 NIFGEN_ATTR_FUNC_DC_OFFSET attribute for more information.
4. The signal then passes through the Pre-Amp Attenuation section,
a set of selectable solid-state attenuators that provide 0 dB
to 12 dB of attenuation in 3 dB increments. You can adjust the
amount of attenuation by adjusting the Amplitude property, or the 
 NIFGEN_ATTR_FUNC_AMPLITUDE 
attribute. NI-FGEN calculates and sets the correct amount of
attenuation required, corresponding to the gain setting.
5. Following the Pre-Amp Attenuation section, the signal can take
one of two paths: the High-Gain or Low-Gain Amplifier path. NI-FGEN
automatically selects the best amplifier path between the High-Gain
and Low-Gain amplifiers by default based on the Amplitude property
or the 
 NIFGEN_ATTR_FUNC_AMPLITUDE attribute
setting. Alternatively, you can set the signal path to remain
constant regardless of the amplitude setting for applications
requiring one path or the other by calling the 
Analog
Path property or the 
 NIFGEN_ATTR_ANALOG_PATH attribute for more information.
  1. The High-Gain Amplifier path is used for waveform output
voltages greater than ±1.0 V (±0.83 V for sine waveforms) into
50 Ω. The amplifier has a fixed gain and is included in
the signal path to enable the signal generator to provide the
maximum V 
 pk-pk .
  2. The Low-Gain Amplifier path is used for waveforms that have all
output voltages equal to or smaller than ±1.0 V (±0.83 V for
sine waveforms) into 50 Ω. The amplifier has a fixed
gain.
6. The signal passes through the Post Amp Attenuation section, a
set of two passive attenuators 12 dB and 24 dB. You can adjust the
amount of attenuation by configuring the Amplitude property or the 
 NIFGEN_ATTR_FUNC_AMPLITUDE 
attribute. NI-FGEN calculates and sets the correct amount of
attenuation required, corresponding to the gain setting.
7. The signal then passes through the Output Enable relay. When
the Output Enable relay is disabled, ground is connected to the
output through a 50 Ω or a 75 Ω resistor.
Intentionally, Standard Function Generation continues while the
output enable relay is disabled. When the relay is enabled, the
analog waveform is seen at the CH 0 connector. You can enable
or disable the output of the analog waveform generator by calling the 
niFgen
Output Enable VI or the 
 niFgen_ConfigureOutputEnabled function for more information.
8. The signal then passes through a
50 Ω/75 Ω selector to the
CH 0 connector. You can configure the output impedance of
the analog waveform generator by calling the 
niFgen Configure Output Impedance VI or the 
 niFgen_ConfigureOutputImpedance function.

Note

Parent topic:

NI 5406 Theory of Operation

Related concepts:

- Aliased Images

<!--NI_TOPIC bundle=ni-fgen path=ni-5406-attenuation.html language=enus -->
## TOPIC 00173: NI 5406 Attenuation

- bundle_id: `ni-fgen`
- source_path: `ni-5406-attenuation.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5406-attenuation.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Analog Output path has two passive attenuation sections. Preamplifier attenuation is prior to the High-Gain and Low-Gain Amplifier paths, and postamplifier attenuation is after the High-Gain and Low-Gain Amplifier paths. The main DAC provides 0 to 3 dB of signal attenuation. Amplitude control is

### NI 5406 Attenuation

The Analog Output path has two passive attenuation
sections. *Preamplifier attenuation* is prior to the High-Gain
and Low-Gain Amplifier paths, and *postamplifier attenuation* is after the
High-Gain and Low-Gain Amplifier paths.

The main *DAC* provides 0 to 3 dB of signal attenuation. Amplitude control is implemented after the DAC. Attenuating the DAC output signal allows you to vary the signal amplitude while maintaining the dynamic range of the DAC. You do not lose any bits from the digital representation of the signal and you do not sacrifice dynamic range, as you would if you control amplitude by using smaller data ranges of the DAC.

For the Low-Gain and the High-Gain Amplifier paths, maximum attenuation is
51 dB. NI-FGEN automatically determines the correct value of attenuation in dB and configures the attenuation based on the set
amplitude. The
minimum amplitude setting for an Analog Output path configured to
High-Gain Amplifier path is .01691. The minimum allowable amplitude
setting with NI-FGEN automatically selecting the Low-Gain Amplifier
path is .005635 (gain is a unitless value).

NI-FGEN calculates and sets the correct amount of
attenuation required that corresponds to your NI-FGEN gain setting.
The correct amount of attenuation is implemented in the 
preamplifier and postamplifier attenuation blocks to best achieve
the desired output signal amplitude. You can set the amount of gain
with the Amplitude property or the 
NIFGEN_ATTR_FUNC_AMPLITUDE attribute.

Parent topic:

NI 5406 Waveform Amplitude Control

Related concepts:

- NI 5406 Preamplifier Attenuation
- NI 5406 Postamplifier Attenuation
- NI 5406 DAC Attenuation

<!--NI_TOPIC bundle=ni-fgen path=ni-5406-block-diagram.html language=enus -->
## TOPIC 00174: NI 5406 Block Diagram

- bundle_id: `ni-fgen`
- source_path: `ni-5406-block-diagram.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5406-block-diagram.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: This topic contains information about the NI 5406 top-level block diagram and descriptions of the individual blocks. If it is installed in any slot other than Slot 2 of the PXI chassis, the NI 5406 can receive a signal on the PXI_STAR line and can route a signal on the PXI_STAR line back to Slot 2

### NI 5406 Block Diagram

This topic contains information about the 
NI 5406 top-level block diagram and descriptions of the
individual blocks.

[IMAGE alt='image' src='GUID-42A6677D-182B-4580-952B-B38955E767F9-a5.gif']

Note

The following list describes the individual
blocks:

- The 
 Onboard Memory stores the 
 frequency list instructions
that you load into the device.
- Clocking allows you to phase lock the onboard Sample clock
to a Reference clock.
- The 
 Standard Function Generation Engine generates standard
functions using 
 direct digital synthesis (DDS) with a 16 k
lookup table and 48-bit accumulator using the 100 MHz Sample
clock.
- The 
 Standard Function Generation Engine retrieves the
frequency list instructions from the 
 Onboard Memory .
- The output from the 
 Standard Function Generation Engine is sent to the 
 DAC after any digital gain is applied.
- For user-defined waveforms, the 
 DAC also contains a selectable 
 Digital Filter , which interpolates and filters the
waveform data.
- The waveform data is sent from the 
 DAC to the 
 Analog Output path where the signal data is filtered and
amplified.
- The 
 Routing Matrix allows flexible routing of the PXI Trigger
lines (RTSI) and the external PFI lines.

Parent topic:

NI 5406 Theory of Operation

Related concepts:

- Frequency List Mode
- Direct Digital Synthesis

<!--NI_TOPIC bundle=ni-fgen path=ni-5406-burst-trigger-mode.html language=enus -->
## TOPIC 00175: NI 5406 Burst Trigger Mode

- bundle_id: `ni-fgen`
- source_path: `ni-5406-burst-trigger-mode.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5406-burst-trigger-mode.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: In Burst trigger mode, calling the first Start trigger begins waveform generation. The waveform then generates continually. The following table provides more information about waveform generation behavior in Frequency List output mode. Output Mode Trigger Behavior Frequency List Mode The device gene

### NI 5406 Burst Trigger Mode

In Burst trigger mode, calling the first Start
trigger begins waveform generation. The waveform then generates
continually. The
following table provides more information about
waveform generation behavior in Frequency List output mode.

| Output Mode | Trigger Behavior |
| --- | --- |
| Frequency List Mode | The device generates the next step in the active frequency list every time a Start trigger occurs. After the duration for a step elapses, the waveform generates until the next Start trigger is received. When the next Start trigger is received, the next step in the frequency list generates. If a Start trigger is received within the specified duration of the step, the Start trigger is applied after the duration elapses. Any additional Start triggers received within the duration are ignored. If the Trigger Source property or the NIFGEN_ATTR_TRIGGER_SOURCE attribute is set to NIFGEN_VAL_IMMEDIATE, the only way to advance to the next step in the frequency list is to call the niFgen Send Software Edge Trigger VI or the niFgen_SendSoftwareEdgeTrigger function. |

Parent topic:

NI 5406 Trigger Modes

<!--NI_TOPIC bundle=ni-fgen path=ni-5406-calibration.html language=enus -->
## TOPIC 00176: NI 5406 Calibration

- bundle_id: `ni-fgen`
- source_path: `ni-5406-calibration.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5406-calibration.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Before shipping your signal generator, NI calibrated your device to ensure that all features are within specifications. Calibration is a set of operations that compares the values indicated by a measuring instrument or measuring system to the corresponding values realized by external standards. You

### NI 5406 Calibration

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

NI 5406 NI 5406 Overview

<!--NI_TOPIC bundle=ni-fgen path=ni-5406-ch-0-connector.html language=enus -->
## TOPIC 00177: NI 5406 CH 0 Connector

- bundle_id: `ni-fgen`
- source_path: `ni-5406-ch-0-connector.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5406-ch-0-connector.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The CH 0 connector is the analog waveform output terminal. The maximum output levels from this connector depend on the type of load termination. For example, if the output of the device terminates into a 50 Ω load, the maximum output levels are ±5 V, while the maximum output levels are ±10 V when th

### NI 5406 CH 0 Connector

The CH 0 connector is the analog waveform
output terminal. The maximum output levels from this connector
depend on the type of load termination. For example, if the output of the device
terminates into a 50 Ω load, the maximum output levels
are ±5 V, while the maximum output levels are ±10 V when the
device terminates into a high-impedance load (HiZ). This difference
is illustrated in the following figure.

[IMAGE alt='image' src='GUID-B63A4BA1-6BFA-443C-8A58-30D1C13C1E21-a5.gif']

If the output terminates into any other load, the
levels are defined by the following formula:

V<sub>out</sub>
 = ± [ 
R<sub>L</sub>
 / ( 
R<sub>L</sub>
 + 
R<sub>O</sub>
 ) ] × 10 V

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
 or NIFGEN_ATTR_FUNC_AMPLITUDE attribute.

#### Load Impedance Compensation

The NI 5406 has the ability to configure the
output signal amplitude based on a user-configured load impedance
setting. This capability is desirable when you use the NI 5406
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
desired peak-to-peak voltage amplitude or arbitrary gain. You can configure the load impedance by calling the 
Load
Impedance property or 
NIFGEN_ATTR_LOAD_IMPEDANCE attribute.

Note

For waveform output
signal specifications, refer to the 
*device
specifications*.

Parent topic:

NI 5406 NI 5406 Overview

<!--NI_TOPIC bundle=ni-fgen path=ni-5406-clocking.html language=enus -->
## TOPIC 00178: NI 5406 Clocking

- bundle_id: `ni-fgen`
- source_path: `ni-5406-clocking.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5406-clocking.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5406 has a sample clock rate of 100 MHz. You can use the REF IN connector or the PXI_CLK10/RTSI 7 line as the source of the frequency reference for the onboard phase-locked loop. For PCI signal generators, you can also use the onboard Reference clock. The onboard Reference clock is availabl

### NI 5406 Clocking

The NI 5406 has a sample clock rate of
100 MHz. You can use the REF IN connector or the
PXI_CLK10/RTSI 7 line as the source of the frequency reference for
the onboard phase-locked loop. For PCI signal generators, you can
also use the onboard Reference clock.

[IMAGE alt='image' src='GUID-84532EF6-80F1-4F0C-A6C4-058D0C08BF61-a5.gif']

Note

Related Topics

*Phase-Locked Loop
Reference Sources*

*Exporting Clocks*

Parent topic:

NI 5406 Theory of Operation

Related concepts:

- NI 5406 Reference Clock
- NI 5406 Exporting Clocks

<!--NI_TOPIC bundle=ni-fgen path=ni-5406-continuous-trigger-mode.html language=enus -->
## TOPIC 00179: NI 5406 Continuous Trigger Mode

- bundle_id: `ni-fgen`
- source_path: `ni-5406-continuous-trigger-mode.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5406-continuous-trigger-mode.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The waveform you downloaded generates continuously after receiving one Start trigger. All Start triggers after the first Start trigger are ignored. The following table provides more information about waveform generation behavior in Frequency List output mode. Output Mode Trigger Behavior Frequency L

### NI 5406 Continuous Trigger Mode

The waveform you downloaded generates continuously
after receiving one Start trigger. All Start triggers after the
first Start trigger are ignored. The
following table provides more information about
waveform generation behavior in Frequency List output mode.

| Output Mode | Trigger Behavior |
| --- | --- |
| Frequency List Mode | The device generates the next step in the active frequency list once the duration of the step has elapsed. The frequency list repeats until generation is aborted. The frequency list generates continuously after receiving one Start trigger. All Start triggers after the first Start trigger are ignored. |

Parent topic:

NI 5406 Trigger Modes

<!--NI_TOPIC bundle=ni-fgen path=ni-5406-dac-attenuation.html language=enus -->
## TOPIC 00180: NI 5406 DAC Attenuation

- bundle_id: `ni-fgen`
- source_path: `ni-5406-dac-attenuation.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5406-dac-attenuation.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The main DAC output can be fine-tuned for attenuation, which provides 0 to 3 dB of the Analog Output path signal attenuation. This fine-tuning of the main DAC attenuation is performed by the gain DAC. Adjust the gain DAC using the Gain DAC Value property or the NIFGEN_ATTR_GAIN_DAC_VALUE attribute.

### NI 5406 DAC Attenuation

The main DAC output can be fine-tuned for
attenuation, which provides 0 to 3 dB of the Analog Output
path signal attenuation. This fine-tuning of the main DAC
attenuation is performed by the gain DAC. Adjust the gain
DAC using the 
Gain
DAC Value property or the 
NIFGEN_ATTR_GAIN_DAC_VALUE attribute. The main DAC also
provides the fine resolution for the attenuation settings.

The fine gain control of square wave signals is
controlled through the Square Wave Gain DAC. You can adjust the
Square Wave Gain DAC by setting the Gain DAC Value property or the 
NIFGEN_ATTR_GAIN_DAC_VALUE
attribute.

Parent topic:

NI 5406 Attenuation

<!--NI_TOPIC bundle=ni-fgen path=ni-5406-data-mask.html language=enus -->
## TOPIC 00181: NI 5406 Data Mask

- bundle_id: `ni-fgen`
- source_path: `ni-5406-data-mask.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5406-data-mask.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The signal generator supports analog data masks and static values. The data mask allows you to shield bits of the data to be replaced with the corresponding static value bits. For example, a mask of 0xFF00 and a static value of 0xAAAA applied to a DC waveform with a value of 0x1111 produces a DC wav

### NI 5406 Data Mask

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

NI 5406 NI 5406 Overview

<!--NI_TOPIC bundle=ni-fgen path=ni-5406-dc-offset.html language=enus -->
## TOPIC 00182: NI 5406 DC Offset

- bundle_id: `ni-fgen`
- source_path: `ni-5406-dc-offset.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5406-dc-offset.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The maximum DC Offset allowed on the signal generator depends on the output waveform being generated. For square waveforms, the maximum offset that is allowed is 50% of the amplitude setting (50% of V [pk-pk]). The maximum offset is shown in the following figure. If a sine, triangle, ramp, or user-d

### NI 5406 DC Offset

The maximum DC Offset allowed on the signal
generator depends on the output waveform being generated.

For square waveforms, the maximum offset that is
allowed is 50% of the amplitude setting (50% of V 
<sub>pk-pk</sub>). The maximum offset is shown in the following
figure.

[IMAGE alt='image' src='GUID-E3F8B57E-6A52-42D0-A3E4-F9DF811E95D2-a5.gif']

If a sine, triangle, ramp, or user-defined
waveform is generated, then any offset is allowed as long as the
waveform stays within the +10 and -10 V amplitude limit of the
board into high Z (+5 V and -5 V limit into 50 Ω load). A 2 V<sub>pk-pk</sub> sine waveform is shown in the following figure
with its maximum allowed offset setting.

[IMAGE alt='image' src='GUID-5E3A7B40-D362-4D48-90FA-1BA1203916A9-a5.gif']

Note

device specifications

Parent topic:

NI 5406 Waveform Amplitude Control

<!--NI_TOPIC bundle=ni-fgen path=ni-5406-digital-filter.html language=enus -->
## TOPIC 00183: NI 5406 Digital Filter

- bundle_id: `ni-fgen`
- source_path: `ni-5406-digital-filter.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5406-digital-filter.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The main DAC provides an internal digital filter. When digital filtering is enabled, the main DAC runs at a faster rate, referred to as the effective sample rate (ESR). The waveform data transfers to the main DAC at the configured Sample clock rate; the internal digital filter interpolates by a fact

### NI 5406 Digital Filter

The main DAC provides an internal digital filter.
When digital filtering is enabled, the main DAC runs at a faster
rate, referred to as the effective sample rate (ESR). The waveform
data transfers to the main DAC at the configured Sample clock rate;
the internal digital filter interpolates by a factor of 2x or 4x; and the DAC generates the data at the ESR.

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
without exceeding 400 MS/s.

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

NI 5406 Filtering Effects

Related concepts:

- Filtering and Interpolation
- Aliased Images

<!--NI_TOPIC bundle=ni-fgen path=ni-5406-digital-gain.html language=enus -->
## TOPIC 00184: NI 5406 Digital Gain

- bundle_id: `ni-fgen`
- source_path: `ni-5406-digital-gain.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5406-digital-gain.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Digital gain multiplies waveform data by a factor you specify in the Digital Gain property or the NIFGEN_ATTR_DIGITAL_GAIN attribute before converting the data to an analog signal in the DAC. Digital gain can be changed during generation without the glitches caused by switching that are common when

### NI 5406 Digital Gain

NIFGEN_ATTR_DIGITAL_GAIN

Note

Parent topic:

NI 5406 Waveform Amplitude Control

<!--NI_TOPIC bundle=ni-fgen path=ni-5406-events.html language=enus -->
## TOPIC 00185: NI 5406 Events

- bundle_id: `ni-fgen`
- source_path: `ni-5406-events.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5406-events.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use events to indicate when a specific hardware condition has been met on the NI 5406. An event is a signal generated by the NI device at a device state. The NI 5406 supports Ready for Start, Started, and Done events. The NI 5406 also supports the use of event delays.

### NI 5406 Events

You can use *events* to indicate when a specific
hardware condition has been met on the NI 5406. An event is a
signal generated by the NI device at a device state. The NI 5406
supports Ready for Start, Started, and Done
events. The NI 5406 also supports the use of *event delays*.

Parent topic:

NI 5406 NI 5406 Overview

Related concepts:

- Events
- Event Delays

<!--NI_TOPIC bundle=ni-fgen path=ni-5406-exporting-clocks.html language=enus -->
## TOPIC 00186: NI 5406 Exporting Clocks

- bundle_id: `ni-fgen`
- source_path: `ni-5406-exporting-clocks.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5406-exporting-clocks.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5406 provides two resources for exporting your clocks and multiple destinations to route to. The following table shows the available clock signals that can be routed to devices external to the NI 5406 and the destination options. Clock to be Exported Destination Options Sample Clock SYNC OUT/

### NI 5406 Exporting Clocks

The NI 5406 provides two resources for
exporting your clocks and multiple destinations to route to.

[IMAGE alt='image' src='GUID-60A00E20-6823-4B50-ADD4-09D750B2F25C-a5.gif']

The following table shows the available clock
signals that can be routed to devices external to the
NI 5406 and the destination options.

| Clock to be Exported | Destination Options |
| --- | --- |
| Sample Clock | SYNC OUT/PFI 0 and PFI 1 BNC connector |
| PXI_Trig<0..6> (PXI), RTSI<0..6> (PCI) |  |
| Reference Clock | SYNC OUT/PFI 0 and PFI 1 BNC connector |
| PXI_Trig<0..6> (PXI), RTSI<0..6> (PCI) |  |
| Onboard Reference Clock | RTSI7 |

#### Sample Clock

For synchronization purposes, the NI 5406 
allows you to export your Sample clock so that other devices can
have the same timing as the NI 5406. The Sample clock can
be routed to the SYNC OUT/PFI 0 and PFI 1 front panel BNC
connectors, PXI_Trig<0..6> lines on the PXI trigger bus, or
the RTSI<0..6> (PCI) lines.

Additionally, the exported clock can be divided
down by an integer value (no less than 2) before being exported to
the SYNC OUT/PFI 0 and PFI 1 BNC connectors, PXI_Trig<0..6>
lines, or the RTSI<0..6> (PCI) lines. You can configure the Sample clock divisor by calling the 
Exported Sample Clock Divisor property or the 
NIFGEN_ATTR_EXPORTED_SAMPLE_CLOCK_DIVISOR attribute.

Note

specifications

#### Reference Clock

For synchronization purposes, the NI 5406 
allows you to export your PLL Reference clock so that other devices
can lock their clock sources to the same signal. Referring to the
previous image, this clock is the actual clock that is configured
for the NI 5406 phase-locked loop circuit to use as a
reference. You must have a Reference clock configured as a PLL
Reference clock source for the signal to be available for
exporting. The Reference clock can be routed to the SYNC OUT/PFI 0
and PFI 1 BNC connectors on the front panel, the
PXI_Trig<0..6> lines on the PXI trigger bus, or the
RTSI<0..6> (PCI) lines.

Note

#### Onboard Reference Clock

The onboard Reference clock is a dedicated 10 MHz
clock for PCI modules only. The onboard Reference clock can only be
exported to RTSI7, for other modules to use, and to reimport as the
Reference clock. You can export the onboard Reference clock to
other modules on RTSI7 and then reimport it so that all devices
(including the master) can use the same Reference clock.

#### Destination Options

SYNC OUT/PFI 0 and PFI 1–The Sample clock
and the Reference clock can be exported to the SYNC OUT/PFI 0 and
PFI 1 BNC connectors on the front panel to synchronize external
devices. You must configure the device to export the desired clock
to the PFI BNC connectors.

Note

niFgen_ExportSignal

PXI_Trig<0..6>–The Sample clock and
the Reference clock can be exported to the PXI_Trig lines or RTSI
(PCI) lines. The PXI/PCI standard allows for devices to route
signals to other devices in your PXI chassis to enhance device to
device synchronization. Refer to the chassis documentation for
specifications to ensure the reference signal is within tolerance.
You must configure the device to export the desired clock to the
PXI_Trig line or RTSI line. When exporting signals,
PXI_Trig<0..6> is equivalent to RTSI_<0..6>

You can configure the
destinations for the desired clock signal by calling the 
niFgen
Export Signal VI or the 
niFgen_ExportSignal function.

Parent topic:

NI 5406 Clocking

<!--NI_TOPIC bundle=ni-fgen path=ni-5406-exporting-signals.html language=enus -->
## TOPIC 00187: NI 5406 Exporting Signals

- bundle_id: `ni-fgen`
- source_path: `ni-5406-exporting-signals.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5406-exporting-signals.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The signal generator contains seven PXI trigger lines or seven RTSI (PCI devices only) lines that are available for sending signal generator-specific information to other devices that have PXI trigger or RTSI bus connectors. The signal generator also connects to the PXI star trigger line, which you

### NI 5406 Exporting Signals

Note

ni.com/products

The signal generator has connectors on the front
panel to route signals to devices external to a PXI or PCI
chassis. The following table shows the signals available for export
and the lines they can be routed to. To determine all possible
signal routes for your device, refer to 
*Signal Routing*.

|  |  | Destination |  |
| --- | --- | --- | --- |
| PXI_Trig<0..6>, RTSI<0..6>, or PXI_STAR | SYNC OUT/PFI 0 and PFI 1 Connectors |  |  |
| Exported Clocks, Triggers, and Events | Sample Clock | Yes | Yes * |
| PLL Reference Source | Yes | Yes* |  |
| Out Start trigger | Yes | Yes |  |
| * SYNC OUT/PFI 0 is optimized for the Sample clock and PLL reference source signals and has slightly less jitter than PFI 1. SYNC OUT/PFI 0 is the recommended terminal to use for exporting clocks. |  |  |  |

Sample Clock–The clock signal that tells the
DAC when to convert the digital waveform values to an analog
voltage. The Sample clock frequency is referred to as the Sample
clock rate; the rate at which the digital waveforms from device
memory are generated. The Sample clock is also known as update
clock.

Note

PLL Reference source–A clock signal that is
only available when a PLL Reference source has been configured. The
clock is the source selected as the PLL Reference Clock source.

Out Start trigger–A signal generated by the
device upon recognizing a start condition that can be routed out
various connectors to signal other devices.

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

NI 5406 NI 5406 Overview

Related concepts:

- NI 5406 Signal Routing

<!--NI_TOPIC bundle=ni-fgen path=ni-5406-filtering-effects.html language=enus -->
## TOPIC 00188: NI 5406 Filtering Effects

- bundle_id: `ni-fgen`
- source_path: `ni-5406-filtering-effects.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5406-filtering-effects.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The delay from the time at which the device receives a trigger to the time at which the analog output signal is generated increases if the digital and/or analog filters in the Analog Output path are enabled. In the case of digital filtering, delay also increases with increase in interpolation. The

### NI 5406 Filtering Effects

Analog Output path

Note

Refer to 
*Digital
Filter* for interpolation options. Refer to the 
*device
specifications* for the delay from trigger to analog output
based on different filtering options.

Parent topic:

NI 5406 Analog Output

Related concepts:

- NI 5406 Analog Output
- NI 5406 Digital Filter

<!--NI_TOPIC bundle=ni-fgen path=ni-5406-filtering-effects_2.html language=enus -->
## TOPIC 00189: NI 5406 Filtering Effects

- bundle_id: `ni-fgen`
- source_path: `ni-5406-filtering-effects_2.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5406-filtering-effects_2.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The delay from the time at which the device receives a trigger to the time at which the analog output signal is generated increases if the digital and/or analog filters in the Analog Output path are enabled. In the case of digital filtering, delay also increases with increase in interpolation. The

### NI 5406 Filtering Effects

Analog Output path

Note

Refer to 
*Digital
Filter* for interpolation options. Refer to the 
*device
specifications* for the delay from trigger to analog output
based on different filtering options.

Parent topic:

NI 5406 Triggering

<!--NI_TOPIC bundle=ni-fgen path=ni-5406-flatness-correction.html language=enus -->
## TOPIC 00190: NI 5406 Flatness Correction

- bundle_id: `ni-fgen`
- source_path: `ni-5406-flatness-correction.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5406-flatness-correction.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5406 uses flatness correction to ensure a consistent power level when generating sine waveforms at any frequency. During external calibration, the frequency response of the Analog path in its different configurations is measured using the niFgen Initialize Flatness Calibration VI or the niFge

### NI 5406 Flatness Correction

The NI 5406 uses flatness correction to ensure
a consistent power level when generating sine waveforms at any
frequency.

During external calibration, the frequency response
of the Analog path in its different configurations is measured
using the 
niFgen Initialize Flatness Calibration VI or the 
niFgen_InitializeFlatnessCalibration function and the 
niFgen Cal Adjust Flatness
VI or the 
niFgen_CalAdjustFlatness function.

During generation, these measured values are used
to compensate for any attenuation at the requested frequency. The
compensation is applied by digitally multiplying the digital data
going into the DAC by a correction factor.

Parent topic:

NI 5406 Waveform Amplitude Control

<!--NI_TOPIC bundle=ni-fgen path=ni-5406-frequency-list-mode.html language=enus -->
## TOPIC 00191: NI 5406 Frequency List Mode

- bundle_id: `ni-fgen`
- source_path: `ni-5406-frequency-list-mode.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5406-frequency-list-mode.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Frequency List output mode allows you to configure the device to generate a standard function using a list of frequencies you define. A frequency list is composed of steps, each one with a frequency/duration pair. Frequency lists are commonly used for frequency hops and sweeps and frequency shift ke

### NI 5406 Frequency List Mode

*Frequency List output mode* allows you to configure the
device to generate a standard function using a list of frequencies
you define. A frequency list is composed of steps, each one with a
frequency/duration pair. Frequency lists are commonly used for
*frequency hops and sweeps* and frequency shift keying (FSK) applications.

Parent topic:

NI 5406 Output Modes

Related concepts:

- Frequency List Mode
- Frequency Hopping and Sweeping

<!--NI_TOPIC bundle=ni-fgen path=ni-5406-hardware-state-diagram.html language=enus -->
## TOPIC 00192: NI 5406 Hardware State Diagram

- bundle_id: `ni-fgen`
- source_path: `ni-5406-hardware-state-diagram.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5406-hardware-state-diagram.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following diagram shows the hardware states of the signal generator. The signal generator can be in one of the following six basic states during the course of operation. Idle—The device is not generating a waveform. All session properties or attributes can be programmed in the Idle state. In the

### NI 5406 Hardware State Diagram

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

NI 5406 Theory of Operation

Related concepts:

- Programming State Model

<!--NI_TOPIC bundle=ni-fgen path=ni-5406-ni-5406-overview.html language=enus -->
## TOPIC 00193: NI 5406 NI 5406 Overview

- bundle_id: `ni-fgen`
- source_path: `ni-5406-ni-5406-overview.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5406-ni-5406-overview.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5406 is a 40 MHz, 16-bit function generator with the following features: One 16-bit resolution output channel Output amplitude up to 10 V [pk-pk] into a 50 Ω load Offset up to ±5 V [pk] including AC and DC components into 50 Ω impedance Up to 40 MHz sine output Up to 40 MHz square output Up t

### NI 5406 NI 5406 Overview

The NI 5406 is a 40 MHz, 16-bit function generator with the following features:

- One 16-bit resolution output channel

- Output amplitude up to 10 V 
 pk-pk into a 50 Ω load
- Offset up to ±5 V 
 pk including AC and DC components into 50 Ω
impedance

- Up to 40 MHz sine output
- Up to 40 MHz square output
- Up to 5 MHz triangle, ramp-up, and ramp-down output

- Software-selectable output impedances (50 Ω or
75 Ω) and output attenuation levels from 0 dB to
51 dB
- PLL synchronization to external clocks or to
PXI_CLK10
- NI-TClk support for multi-module synchronization. Refer to 
 Start»All Programs»National Instruments»NI-TClk 
for more information.
- Sampling rate of 100 MS/s
- 32 MB of onboard frequency list memory
- Digital and analog filters
- Digital gain
- Two external trigger inputs
- PXI trigger/RTSI lines

All NI 5406 devices follow
industry-standard Plug and Play specifications for the PXI bus and
offer seamless integration with compliant systems.

Parent topic:

Devices

<!--NI_TOPIC bundle=ni-fgen path=ni-5406-onboard-memory.html language=enus -->
## TOPIC 00194: NI 5406 Onboard Memory

- bundle_id: `ni-fgen`
- source_path: `ni-5406-onboard-memory.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5406-onboard-memory.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5406 can store the following in onboard memory: Up to 32 MB of frequency list instructions 65,536 samples for sine, square, and triangle waveforms 16,384 samples for all other waveforms

### NI 5406 Onboard Memory

The NI 5406 can store the following in onboard
memory:

- Up to 32 MB of frequency list instructions
- 65,536 samples for sine, square, and triangle waveforms
- 16,384 samples for all other waveforms

Parent topic:

NI 5406 Theory of Operation

<!--NI_TOPIC bundle=ni-fgen path=ni-5406-output-enable.html language=enus -->
## TOPIC 00195: NI 5406 Output Enable

- bundle_id: `ni-fgen`
- source_path: `ni-5406-output-enable.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5406-output-enable.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can disable the analog output signal at the CH 0 connector by controlling the output enable relay, as shown in the following figure. When the output enable relay is disabled, the output signal is connected to ground through a 50 or 75 Ω resistance depending on the output impedance selected. The

### NI 5406 Output Enable

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

NI 5406 Analog Output

Related concepts:

- NI 5406 Analog Output

<!--NI_TOPIC bundle=ni-fgen path=ni-5406-output-impedance.html language=enus -->
## TOPIC 00196: NI 5406 Output Impedance

- bundle_id: `ni-fgen`
- source_path: `ni-5406-output-impedance.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5406-output-impedance.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5406 Analog Output path is designed to have an output impedance of 50 Ω from the Output Enable relay looking back towards the Main DAC. Most applications use a load impedance of 50 Ω, but applications such as video testing, require 75 Ω. As shown in the following figure, there is a selectable

### NI 5406 Output Impedance

The NI 5406 Analog Output path is
designed to have an output impedance of 50 Ω from the
Output Enable relay looking back towards the Main DAC. Most applications use a load impedance of
50 Ω, but applications such as video testing, require
75 Ω. As shown in the following figure, there is a
selectable 25 Ω resistance that can be switched into the
Analog Output path between the Output Enable Relay and the CH 0 connector for applications requiring a 75 Ω impedance.

[IMAGE alt='image' src='GUID-D2930CC3-8665-48B1-BD41-FAC39E240C2D-a5.gif']

If the load impedance is a high impedance (~1
MΩ), you may see output levels up to twice the selected
output value for a matched input/output impedance. These levels can
be as high as 20 V 
<sub>pk-pk</sub> for the High-Gain Amplifier path. Normally, the
output levels increase as the load impedance increases. The
NI 5406 can compensate for different load impedance
values. Refer to 
*CH 0 Connector* for more
information.

niFgen_ConfigureOutputImpedance

Note

Parent topic:

NI 5406 Analog Output

Related concepts:

- NI 5406 CH 0 Connector

<!--NI_TOPIC bundle=ni-fgen path=ni-5406-output-modes.html language=enus -->
## TOPIC 00197: NI 5406 Output Modes

- bundle_id: `ni-fgen`
- source_path: `ni-5406-output-modes.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5406-output-modes.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The output mode of your signal generator determines the type of waveforms your signal generator produces. To select an output mode, set the Output Mode parameter of the niFgen Configure Output Mode VI or the niFgen_ConfigureOutputMode function.

### NI 5406 Output Modes

The output mode of your signal generator determines the type of
waveforms your signal generator produces. To select an output mode,
set the 
Output Mode parameter of the 
niFgen
Configure Output Mode VI or the 
niFgen_ConfigureOutputMode function.

Parent topic:

NI 5406 Waveform Generation

<!--NI_TOPIC bundle=ni-fgen path=ni-5406-pci-front-panel.html language=enus -->
## TOPIC 00198: NI 5406 PCI Front Panel

- bundle_id: `ni-fgen`
- source_path: `ni-5406-pci-front-panel.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5406-pci-front-panel.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the NI PCI-5406 front panel. This front panel has four BNC connectors. The CH 0 connector is the analog output from which arbitrary waveforms are generated. The REF IN connector provides the device with an external reference or external Sample clock. The SYNC OUT/PFI 0 and

### NI 5406 PCI Front Panel

The following figure shows the
NI PCI-5406 front panel. This front panel has four BNC
connectors.

[IMAGE alt='image' src='GUID-3FB3535E-7CE2-49F9-ADEF-3718868281F2-a5.gif']

The 
*CH 0* connector is the analog output
from which arbitrary waveforms are generated.

The 
*REF IN* connector provides the
device with an external reference or external Sample clock.

The 
*SYNC OUT/PFI 0 and PFI 1*
connectors are multi-directional connections for a number of
different signals.

Parent topic:

NI 5406 NI 5406 Overview

Related concepts:

- NI 5406 CH 0 Connector
- NI 5406 REF IN Connector
- NI 5406 SYNC OUT/PFI 0 and PFI 1 Connectors

<!--NI_TOPIC bundle=ni-fgen path=ni-5406-postamplifier-attenuation.html language=enus -->
## TOPIC 00199: NI 5406 Postamplifier Attenuation

- bundle_id: `ni-fgen`
- source_path: `ni-5406-postamplifier-attenuation.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5406-postamplifier-attenuation.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The postamplifier attenuation section is after the High-Gain and Low-Gain Amplifiers in the analog path. The attenuators provide a range of attenuation from 0 dB to a maximum of 36 dB in steps of 12 dB. NI-FGEN automatically controls the value of attenuation set in the postamplifier attenuation sect

### NI 5406 Postamplifier Attenuation

The postamplifier attenuation section is after the
High-Gain and Low-Gain Amplifiers in the *analog path*. The attenuators provide a
range of attenuation from 0 dB to a maximum of 36 dB in steps
of 12 dB. NI-FGEN automatically controls the value of attenuation
set in the postamplifier attenuation section dependent on the set
amplitude. You can read the value NI-FGEN has selected for postamplifier
attenuation using the 
Post-Amplifier Attenuation property or the 
NIFGEN_ATTR_POST_AMPLIFIER_ATTENUATION attribute.

Parent topic:

NI 5406 Attenuation

Related concepts:

- NI 5406 Analog Output

<!--NI_TOPIC bundle=ni-fgen path=ni-5406-power-up-and-reset-conditions.html language=enus -->
## TOPIC 00200: NI 5406 Power-Up and Reset Conditions

- bundle_id: `ni-fgen`
- source_path: `ni-5406-power-up-and-reset-conditions.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5406-power-up-and-reset-conditions.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The signal generator is in the following state from the time at which the computer begins to power up until the operating system is fully booted and NI-FGEN is loaded. The CH 0 analog output connector is disabled and has 50 Ω or 75 Ω impedance to ground. This impedance is the same as its previous se

### NI 5406 Power-Up and Reset Conditions

The signal generator is in the following state from
the time at which the computer begins to power up until the operating system is
fully booted and NI-FGEN is loaded.

- The CH 0 analog output connector is disabled and has
50 Ω or 75 Ω impedance to ground. This
impedance is the same as its previous setting before the device was
powered down. The output voltage amplitude of this connector
is 0 V.
- The REF IN connector has 50 Ω impedance to
ground.
- SYNC OUT/PFI 0 and PFI 1 are tristated and have a 1
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

- The digital filter of the NI 5406
inside the DAC is disabled.

- REF IN is disabled and has a 50 Ω
impedance to ground.
- SYNC OUT/PFI 0 and PFI 1 are tristated and have a 1
kΩ impedance to ground.

- PXI trigger or RTSI lines are tristated and floating.
- The sample rate is set to the maximum rate, with the Sample
clock source set to the internal Sample clock timebase.
- The Sample clock timebase is tuned by the internal reference
control voltage.

Parent topic:

NI 5406 NI 5406 Overview

<!--NI_TOPIC bundle=ni-fgen path=ni-5406-preamplifier-attenuation.html language=enus -->
## TOPIC 00201: NI 5406 Preamplifier Attenuation

- bundle_id: `ni-fgen`
- source_path: `ni-5406-preamplifier-attenuation.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5406-preamplifier-attenuation.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The preamplifier attenuation section is before the Low-Gain and High-Gain amplifiers in the analog path. The attenuators provide a range of attenuation from 0 to a maximum of 12 dB in steps of 3 dB. NI-FGEN automatically controls the value of attenuation set in the preamplifier attenuation section d

### NI 5406 Preamplifier Attenuation

The preamplifier attenuation section is before the
Low-Gain and High-Gain amplifiers in the *analog path*. The attenuators provide a
range of attenuation from 0 to a maximum of 12 dB in steps of
3 dB. NI-FGEN automatically controls the value of attenuation set
in the preamplifier attenuation section depending on the set
amplitude. You can read the value NI-FGEN has selected for preamplifier attenuation using the 
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

NI 5406 Attenuation

Related concepts:

- NI 5406 Analog Output

<!--NI_TOPIC bundle=ni-fgen path=ni-5406-pxi-front-panel.html language=enus -->
## TOPIC 00202: NI 5406 PXI Front Panel

- bundle_id: `ni-fgen`
- source_path: `ni-5406-pxi-front-panel.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5406-pxi-front-panel.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the front panel of the NI 5406 for the PXI bus. This front panel has four BNC connectors. The CH 0 connector is the analog output from which waveforms are generated. The REF IN connector provides the device with an external Reference clock. The SYNC OUT/PFI 0 and PFI 1 con

### NI 5406 PXI Front Panel

The following figure shows the front panel of the
NI 5406 for the PXI bus. This front panel has four BNC
connectors.

[IMAGE alt='image' src='GUID-35F51D5E-5950-40C8-B942-078A0CE87641-a5.gif']

The 
*CH 0* connector is the analog output
from which waveforms are generated.

The 
*REF IN* connector provides the
device with an external Reference clock.

The 
*SYNC OUT/PFI 0 and PFI 1*
connectors are multidirectional connections for a number of
different signals.

Parent topic:

NI 5406 NI 5406 Overview

Related concepts:

- NI 5406 CH 0 Connector
- NI 5406 REF IN Connector
- NI 5406 SYNC OUT/PFI 0 and PFI 1 Connectors

<!--NI_TOPIC bundle=ni-fgen path=ni-5406-ref-in-connector.html language=enus -->
## TOPIC 00203: NI 5406 REF IN Connector

- bundle_id: `ni-fgen`
- source_path: `ni-5406-ref-in-connector.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5406-ref-in-connector.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The REF IN front panel connector can accept an external Reference clock You must not change the Reference clock frequency while waveform generation is in progress. Only modify the frequency of the external clock before you start the waveform generation or after you stop the waveform generation. Ex

### NI 5406 REF IN Connector

Caution

not

before

after

#### External Reference Clock Input

The REF IN connector is an input that can accept a
Reference clock from an external source and phase lock the internal
clock of the signal generator to this external Reference clock.
Refer to the 
*device
specifications* for the allowable Reference clock frequencies
and signal characteristics.

The default value for the Reference clock source is
Internal. You can configure the Reference clock source and frequency by calling the 
niFgen Configure Reference Clock VI or the 
niFgen_ConfigureReferenceClock function.

Note

PLL Reference
Sources

Parent topic:

NI 5406 NI 5406 Overview

Related concepts:

- NI 5406 Reference Clock

<!--NI_TOPIC bundle=ni-fgen path=ni-5406-reference-clock.html language=enus -->
## TOPIC 00204: NI 5406 Reference Clock

- bundle_id: `ni-fgen`
- source_path: `ni-5406-reference-clock.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5406-reference-clock.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: A phase-locked loop (PLL) is a circuit that tunes the Sample clock timebase to phase–lock to an external Reference clock. The frequency stability and accuracy of the Sample clock timebase matches that of the Reference clock when the two phase–lock. Using the PLL on your device enables you to frequen

### NI 5406 Reference Clock

Note

device
specifications

The following figure shows the NI 5406
Reference Clock Source path.

[IMAGE alt='image' src='GUID-84532EF6-80F1-4F0C-A6C4-058D0C08BF61-a5.gif']

Note

NIFGEN_ATTR_REFERENCE_CLOCK_SOURCE

#### Reference Clock Sources

The NI 5406 is capable of
phase–locking its Sample clock timebase to an external
signal on the REF IN front panel connector. PXI devices can also
phase–lock to a 10 MHz Reference clock signal provided
by the PXI bus (PXI_CLK10), while PCI devices can phase–lock
to RTSI line 7 or to the onboard Reference clock.

The following table shows the valid NI-FGEN
property or attribute values and combinations to configure the
NI 5406 clock settings for an external Reference
clock.

| Sample Clock Source | PLL Reference Clock Source |
| --- | --- |
| Internal VXCO (100 MHz) | "None" (default) |
| "PXI_CLK10" (PXI), "RTSI7" (PCI) |  |
| "RefIn" |  |
| "OnboardRefClk" (PCI) |  |

Refer to the 
*device
specifications* for information about available REF IN signal
levels.

You can set up the clock by calling the 
niFgen Configure Reference Clock VI or the 
niFgen_ConfigureReferenceClock function.

Parent topic:

NI 5406 Clocking

<!--NI_TOPIC bundle=ni-fgen path=ni-5406-sample-clock.html language=enus -->
## TOPIC 00205: NI 5406 Sample Clock

- bundle_id: `ni-fgen`
- source_path: `ni-5406-sample-clock.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5406-sample-clock.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The signal generator provides a high-precision 100 MHz Voltage Controlled Crystal Oscillator (VCXO) clock source for the Sample clock timebase. The Sample clock timebase frequency is tuned by an Internal Calibration DAC Control Voltage. This clock is used to drive the DAC and all other waveform gene

### NI 5406 Sample Clock

The signal generator provides a high-precision
100 MHz Voltage Controlled Crystal Oscillator (VCXO) clock
source for the Sample clock timebase. The Sample clock timebase
frequency is tuned by an Internal Calibration DAC Control Voltage.
This clock is used to drive the DAC and all other waveform
generation operations on the device. The Internal Calibration DAC,
which is calibrated at the factory and which you can also
calibrate, provides for the Sample clock timebase to maintain a
high quality frequency source.

Parent topic:

NI 5406 Clocking

<!--NI_TOPIC bundle=ni-fgen path=ni-5406-signal-routing.html language=enus -->
## TOPIC 00206: NI 5406 Signal Routing

- bundle_id: `ni-fgen`
- source_path: `ni-5406-signal-routing.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5406-signal-routing.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: An NI signal generator is capable of sending and receiving signals through the front panel and the PXI or RTSI trigger bus. The front panel connectors provides connectivity for the output channel as well as for control lines for sending and receiving clocks, triggers, and events. You can use the PXI

### NI 5406 Signal Routing

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

NI 5406 Theory of Operation

Related concepts:

- NI 5406 Syntax for Terminal Names

<!--NI_TOPIC bundle=ni-fgen path=ni-5406-single-trigger-mode.html language=enus -->
## TOPIC 00207: NI 5406 Single Trigger Mode

- bundle_id: `ni-fgen`
- source_path: `ni-5406-single-trigger-mode.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5406-single-trigger-mode.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: When your application is configured for Single trigger mode, only one Start trigger is required to begin waveform generation. All Start triggers after the first Start trigger are ignored. Once the waveform generation is complete, the analog output indefinitely settles at the DC value of the last sam

### NI 5406 Single Trigger Mode

When your application is configured for Single
trigger mode, only one Start trigger is required to begin waveform
generation. All Start triggers after the first Start trigger are
ignored. Once the waveform generation is complete, the analog
output indefinitely settles at the DC value of the last sample in
the waveform. The
following table provides more information about
waveform generation behavior in Frequency List output mode.

| Output Mode | Trigger Behavior |
| --- | --- |
| Frequency List Mode | The device generates each step in the active frequency list sequentially. |

Parent topic:

NI 5406 Trigger Modes

<!--NI_TOPIC bundle=ni-fgen path=ni-5406-specifications.html language=enus -->
## TOPIC 00208: NI 5406 Specifications

- bundle_id: `ni-fgen`
- source_path: `ni-5406-specifications.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5406-specifications.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: For information about the signal generator specifications, refer to the device specifications. You can access these specifications by navigating to Start»All Programs»National Instruments» NI-FGEN»Documentation»NI Signal Generators Specifications, or you can visit ni.com/manuals.

### NI 5406 Specifications

For information about the signal generator
specifications, refer to the 
*device
specifications*. You can access these specifications by
navigating to 
Start»All Programs»National Instruments»
NI-FGEN»Documentation»NI Signal Generators Specifications, or you can visit 
ni.com/manuals.

Parent topic:

NI 5406 NI 5406 Overview

<!--NI_TOPIC bundle=ni-fgen path=ni-5406-standard-function-mode.html language=enus -->
## TOPIC 00209: NI 5406 Standard Function Mode

- bundle_id: `ni-fgen`
- source_path: `ni-5406-standard-function-mode.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5406-standard-function-mode.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Standard Function output mode is used to generate standard function waveforms such as sine, square, triangle, and so on. On the NI 5406, Standard Function mode is implemented through direct digital synthesis (DDS). DDS is a technique for deriving, under digital control, an analog frequency source fr

### NI 5406 Standard Function Mode

Standard Function output mode is used to generate standard
function waveforms such as sine, square, triangle, and so on. 
On the NI 5406, *Standard Function mode* is implemented
through *direct digital synthesis* (DDS). DDS is a technique for
deriving, under digital control, an analog frequency source from a
single Reference clock frequency. This technique produces
high-frequency accuracy and resolution, temperature stability,
wideband tuning, and rapid, phase-continuous frequency
switching.

In DDS mode, a fixed–size memory (called *lookup memory*) stores one cycle of a periodic waveform. A phase accumulator indexes the lookup memory. For each cycle of the device Sample clock, the sample of the waveform in lookup memory that is addressed by the phase accumulator is returned. The accumulator is then incremented by the value in the frequency control word (FCW). By adjusting the Frequency property or the NIFGEN_ATTR_FUNC_FREQUENCY attribute, NI-FGEN calculates the corresponding FCW, and you can vary the output frequency of the waveform in lookup memory. The phase accumulator increments in smaller steps for smaller FCWs. Accordingly, you need more samples to generate one waveform cycle, so the frequency is lower. A higher FCW results in a higher frequency. In DDS mode, the Sample clock does not vary with the frequency of the generated waveform. At higher frequencies, some waveform samples in lookup memory are skipped; at lower frequencies, some samples output multiple times in succession.

Parent topic:

NI 5406 Output Modes

Related concepts:

- Standard Function Mode
- Direct Digital Synthesis

<!--NI_TOPIC bundle=ni-fgen path=ni-5406-stepped-trigger-mode.html language=enus -->
## TOPIC 00210: NI 5406 Stepped Trigger Mode

- bundle_id: `ni-fgen`
- source_path: `ni-5406-stepped-trigger-mode.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5406-stepped-trigger-mode.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The waveform you downloaded generates each time a Start trigger occurs. After a waveform finishes generating, the last sample of the waveform repeats continuously until the next Start trigger is received. When the next Start trigger is received, the waveform generates again. If a Start trigger is re

### NI 5406 Stepped Trigger Mode

The waveform you downloaded generates each time a
Start trigger occurs. After a waveform finishes generating, the
last sample of the waveform repeats continuously until the next
Start trigger is received. When the next Start trigger is received,
the waveform generates again. If a Start trigger is received while
a waveform is generating, the Start trigger is ignored and another
Start trigger is required to regenerate the waveform after the last
sample generates. The
following table provides more information about
waveform generation behavior in Frequency List output mode.

| Output Mode | Trigger Behavior |
| --- | --- |
| Frequency List Mode | The device generates the next step in the active frequency list every time a Start trigger occurs. After the duration for a step has elapsed, the signal generation stops and remains at the configured DC offset level until the next Start trigger is received. When the next Start trigger is received, the next step in the frequency list is generated. After the final step, the frequency list repeats until generation is aborted. If the Trigger Source property or the NIFGEN_ATTR_TRIGGER_SOURCE attribute is set to NIFGEN_VAL_IMMEDIATE, the only way to advance to the next step in the frequency list is to call the niFgen Send Software Edge Trigger VI or the niFgen_SendSoftwareEdgeTrigger function. |

Parent topic:

NI 5406 Trigger Modes

<!--NI_TOPIC bundle=ni-fgen path=ni-5406-sync-out-pfi-0-and-pfi-1-connectors.html language=enus -->
## TOPIC 00211: NI 5406 SYNC OUT/PFI 0 and PFI 1 Connectors

- bundle_id: `ni-fgen`
- source_path: `ni-5406-sync-out-pfi-0-and-pfi-1-connectors.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5406-sync-out-pfi-0-and-pfi-1-connectors.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: SYNC OUT/PFI 0 and PFI 1 are bidirectional connectors. As an input, SYNC OUT/PFI 0 and PFI 1 terminals can accept a trigger from an external source that can start or step through waveform generation. As an output, the SYNC OUT/PFI 0 and PFI 1 lines can route a signal out from the following sources:

### NI 5406 SYNC OUT/PFI 0 and PFI 1 Connectors

SYNC OUT/PFI 0 and PFI 1 are bidirectional
connectors.

As an input, SYNC OUT/PFI 0 and PFI 1 terminals can
accept a trigger from an external source that can start or step
through waveform generation. As an output, the SYNC OUT/PFI 0 and
PFI 1 lines can route a signal out from the following sources:

- SYNC OUT
- Out Start trigger
- PLL Reference Clock source
- Sample Clock Out (with / 
 K , where K is an integer used to divide the Sample
clock)

Exporting Signals

device
specifications

Note

niFgen_ExportSignal

Parent topic:

NI 5406 NI 5406 Overview

Related concepts:

- NI 5406 Exporting Signals

<!--NI_TOPIC bundle=ni-fgen path=ni-5406-synchronization.html language=enus -->
## TOPIC 00212: NI 5406 Synchronization

- bundle_id: `ni-fgen`
- source_path: `ni-5406-synchronization.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5406-synchronization.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Your signal generator is based on the National Instruments Synchronization and Memory Core (SMC) technology and therefore supports TClk synchronization. Refer to the NI-TClk Synchronization Help for more information about NI-TClk Synchronization.

### NI 5406 Synchronization

Your signal generator is based on the 
National Instruments
Synchronization and Memory Core (SMC) technology and therefore
supports TClk synchronization. Refer to the 
NI-TClk
Synchronization Help for more information about NI-TClk
Synchronization.

Parent topic:

NI 5406 NI 5406 Overview

<!--NI_TOPIC bundle=ni-fgen path=ni-5406-syntax-for-terminal-names.html language=enus -->
## TOPIC 00213: NI 5406 Syntax for Terminal Names

- bundle_id: `ni-fgen`
- source_path: `ni-5406-syntax-for-terminal-names.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5406-syntax-for-terminal-names.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The syntax for terminal names is a unique identifier that refers to a physical terminal in your system. To guarantee the uniqueness of a terminal name across multiple devices, terminal names begin with a forward slash, followed by the name of the device as configured in MAX, such as Dev1. A forward

### NI 5406 Syntax for Terminal Names

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

NI 5406 Signal Routing

<!--NI_TOPIC bundle=ni-fgen path=ni-5406-theory-of-operation.html language=enus -->
## TOPIC 00214: NI 5406 Theory of Operation

- bundle_id: `ni-fgen`
- source_path: `ni-5406-theory-of-operation.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5406-theory-of-operation.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Expand this topic for information about the theory of operation of your signal generator.

### NI 5406 Theory of Operation

Expand this topic for information about the theory
of operation of your signal generator.

Parent topic:

NI 5406 NI 5406 Overview

<!--NI_TOPIC bundle=ni-fgen path=ni-5406-thermal-shutdown.html language=enus -->
## TOPIC 00215: NI 5406 Thermal Shutdown

- bundle_id: `ni-fgen`
- source_path: `ni-5406-thermal-shutdown.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5406-thermal-shutdown.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: NI-FGEN supports thermal shutdown capability for the NI 5406. This capability allows the signal generator to detect when it has reached a dangerously high temperature and to then power down to prevent damage to the device. Air circulation paths, fan settings, and space allowances are several factors

### NI 5406 Thermal Shutdown

NI-FGEN supports thermal shutdown capability for
the NI 5406. This
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

NI 5406 NI 5406 Overview

<!--NI_TOPIC bundle=ni-fgen path=ni-5406-trigger-modes.html language=enus -->
## TOPIC 00216: NI 5406 Trigger Modes

- bundle_id: `ni-fgen`
- source_path: `ni-5406-trigger-modes.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5406-trigger-modes.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5406 has four trigger modes: Single, Continuous, Stepped, and Burst. These trigger modes are available for Frequency List output mode. Refer to the niFgen Configure Trigger Mode VI or the niFgen_ConfigureTriggerMode function for information about setting the trigger mode.

### NI 5406 Trigger Modes

The NI 5406 has four trigger modes: Single, Continuous, Stepped,
and Burst. These trigger modes are available for Frequency List output mode.
Refer to the 
niFgen
Configure Trigger Mode VI or the 
niFgen_ConfigureTriggerMode function for information about setting the trigger mode.

Parent topic:

NI 5406 Triggering

<!--NI_TOPIC bundle=ni-fgen path=ni-5406-trigger-sources.html language=enus -->
## TOPIC 00217: NI 5406 Trigger Sources

- bundle_id: `ni-fgen`
- source_path: `ni-5406-trigger-sources.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5406-trigger-sources.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Trigger sources are software selectable. You can use any of the following external input triggers: SYNC OUT/ PFI 0 or PFI 1 on the front panel connectors RTSI<0..7> (PCI) lines or PXI_TRIG<0..7> lines and PXI_STAR on the PXI trigger bus backplane The following figure shows the possible trigger sourc

### NI 5406 Trigger Sources

Trigger sources are software selectable. You can
use any of the following external input triggers:

- SYNC OUT/ PFI 0 or PFI 1 on the front panel connectors

- RTSI<0..7> (PCI) lines or PXI_TRIG<0..7> lines and
PXI_STAR on the PXI trigger bus backplane

The following figure shows the possible trigger
sources for the NI 5406.

[IMAGE alt='image' src='GUID-6B1565C6-1A4C-475F-B781-7F36256489B7-a5.gif']

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

NI 5406 Triggering

Related concepts:

- NI 5406 Exporting Signals
- PXI Trigger Lines
- PXI Star Trigger Line

<!--NI_TOPIC bundle=ni-fgen path=ni-5406-trigger-timing.html language=enus -->
## TOPIC 00218: NI 5406 Trigger Timing

- bundle_id: `ni-fgen`
- source_path: `ni-5406-trigger-timing.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5406-trigger-timing.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the relationship between Start trigger and the waveform output. t[s1] is the required pulse width on the Start trigger signal. t[s2] is the delay from the Start trigger to the waveform output. Refer to the NI PXI/PCI-5402/5406 Specifications for more information about thes

### NI 5406 Trigger Timing

The following figure shows the relationship between
Start trigger and the waveform output. t<sub>s1</sub> is the required pulse width on the Start trigger
signal. t<sub>s2</sub> is the delay from the Start trigger to the waveform
output. Refer to the 
*NI PXI/PCI-5402/5406
Specifications* for more information about these timing
parameters.

[IMAGE alt='image' src='GUID-9DD6A51C-2BCA-4129-9C8D-0A821181925F-a5.gif']

The NI 5406 also allows you to export
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

NI 5406 Triggering

<!--NI_TOPIC bundle=ni-fgen path=ni-5406-triggering.html language=enus -->
## TOPIC 00219: NI 5406 Triggering

- bundle_id: `ni-fgen`
- source_path: `ni-5406-triggering.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5406-triggering.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can define the signal generator functionality by using the various triggering techniques. Expand this section to learn more about using triggers with your signal generator.

### NI 5406 Triggering

You can define the signal generator functionality
by using the various triggering techniques. Expand this section to
learn more about using triggers with your signal generator.

Parent topic:

NI 5406 NI 5406 Overview

<!--NI_TOPIC bundle=ni-fgen path=ni-5406-waveform-amplitude-control.html language=enus -->
## TOPIC 00220: NI 5406 Waveform Amplitude Control

- bundle_id: `ni-fgen`
- source_path: `ni-5406-waveform-amplitude-control.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5406-waveform-amplitude-control.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5406 uses both amplifiers and attenuators to achieve needed amplitude settings. Output Paths and Amplifiers The following figure shows two gain paths: the High-Gain Amplifier path and the Low-Gain Amplifier path. The Low-Gain Amplifier path has a 2 V [pk-pk] amplifier and is used for waveform

### NI 5406 Waveform Amplitude Control

The NI 5406 uses both amplifiers and
attenuators to achieve needed amplitude settings.

#### Output Paths and Amplifiers

The following figure shows two gain paths: the
High-Gain Amplifier path and the Low-Gain Amplifier path.

[IMAGE alt='image' src='GUID-D2930CC3-8665-48B1-BD41-FAC39E240C2D-a5.gif']

The Low-Gain Amplifier path has a 2 V 
<sub>pk-pk</sub> amplifier and is used for waveforms that have
output voltages equal to or smaller than 2.00 V 
<sub>pk-pk</sub> (1.67 V 
<sub>pk-pk</sub> for sine waveforms) into matched load impedance.
The High-Gain Amplifier path has a 10 V 
<sub>pk-pk</sub> amplifier and is used for waveforms that have
output voltages greater than 2.0 V 
<sub>pk-pk</sub> (1.67 V 
<sub>pk-pk</sub> for sine waveforms) into matched load impedance.
The gains of the amplifiers are constant and can be set by calling the 
Amplitude
property or the 
NIFGEN_ATTR_FUNC_AMPLITUDE attribute.

By default, NI-FGEN automatically selects the
High-Gain and Low-Gain Amplifiers based on the amplitude setting.
You can override NI-FGEN and configure the High-Gain or the
Low-Gain Amplifier to remain in the Analog Output path regardless
of amplitude by setting the 
Analog
Path property or the 
NIFGEN_ATTR_ANALOG_PATH attribute. Configuring the Low-Gain Amplifier path to remain
constant regardless of the amplitude setting affects the maximum
output value allowable for that particular amplitude setting. The
maximum amplitude setting for an Analog Output path configured to
Low-Gain Amplifier path is 2.0 (1.67 V 
<sub>pk-pk</sub> for sine waveforms). The maximum allowable
amplitude setting with NI-FGEN automatically selecting the Gain
Amplifier path is 10.0 V with a high load impedance.

In addition, the DC Offset Amplifier for adding 
*DC offset* to the signal is in
the High-Gain and Low-Gain Amplifier paths prior to the attenuators
and amplifiers. The DC Offset Amplifier can be fine-tuned for
adding offset to your signal. This fine-tuning of the main DC
Offset Amplifier is performed by the Offset DAC.

#### Square Wave Path

The NI 5406 uses dedicated hardware to
generate low-jitter square wave functions. A comparator is fed two
signals: a sine tone from the main DAC (using the Digital Filter
and the Analog Filter to obtain a 400 MS/s signal) and a DC signal
using the Level DAC.

The output of the comparator is switched back into
the Main path in order to obtain the desired amplitude and offset.
The fine gain control of the signal is controlled through the
Square Wave Gain DAC.

When the signal generator is configured to generate
a square waveform, NI-FGEN automatically selects the Square Wave
path. When the device is idle, it generates the low state of the
square waveform.

When using the Square Wave path, the 
*DC Offset* can be ±50% of the
current Amplitude.

The SYNC OUT is generated through the same
comparator and is routed by default to the SYNC OUT/PFI 0
connector. You can unroute this route or change the output terminal
of SYNC OUT using the 
niFgen
Export Signal VI or the 
niFgen_ExportSignal function.

Parent topic:

NI 5406 Analog Output

Related concepts:

- NI 5406 DC Offset

<!--NI_TOPIC bundle=ni-fgen path=ni-5406-waveform-generation.html language=enus -->
## TOPIC 00221: NI 5406 Waveform Generation

- bundle_id: `ni-fgen`
- source_path: `ni-5406-waveform-generation.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5406-waveform-generation.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5406 supports the following output, or generation, modes: Standard Function Frequency List To select an output mode, set the Output Mode parameter of the niFgen Configure Output Mode VI or the niFgen_ConfigureOutputMode function.

### NI 5406 Waveform Generation

The NI 5406 supports the
following output, or generation, modes:

- Standard Function
- Frequency List

To select an output mode, set the 
Output Mode parameter of the 
niFgen
Configure Output Mode VI or the 
niFgen_ConfigureOutputMode function.

Parent topic:

NI 5406 NI 5406 Overview

Related concepts:

- NI 5406 Standard Function Mode
- NI 5406 Frequency List Mode

<!--NI_TOPIC bundle=ni-fgen path=ni-5412-aborting-generation.html language=enus -->
## TOPIC 00222: NI 5412 Aborting Generation

- bundle_id: `ni-fgen`
- source_path: `ni-5412-aborting-generation.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5412-aborting-generation.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can abort the generation of the current waveform. Aborting the generation exhibits different behaviors for different waveform output modes. Output Mode Abort Behavior Standard Function Abort to Ground—Signal remains at the level for which the DC offset is configured. Arbitrary Waveform, Arbitrar

### NI 5412 Aborting Generation

You can abort the generation of the current
waveform. Aborting the generation exhibits different behaviors for
different 
*waveform output
modes*.

| Output Mode | Abort Behavior |
| --- | --- |
| Standard Function | Abort to Ground—Signal remains at the level for which the DC offset is configured. |
| Arbitrary Waveform, Arbitrary Sequence* | Abort to a Known Voltage—Signal remains at the last sample voltage level prior to the abort. |
| * These modes can also abort to ground. |  |

Related Topics

*Aborting to Ground*

*Aborting to a
Known Voltage*

Parent topic:

NI 5412 Waveform Generation

Related concepts:

- NI 5412 Waveform Generation
- Abort to Ground
- Abort to a Known Voltage

<!--NI_TOPIC bundle=ni-fgen path=ni-5412-access-and-active-leds.html language=enus -->
## TOPIC 00223: NI 5412 ACCESS and ACTIVE LEDs

- bundle_id: `ni-fgen`
- source_path: `ni-5412-access-and-active-leds.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5412-access-and-active-leds.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The ACCESS and ACTIVE LEDs indicate the status of the PXI module: ACCESS LED The ACCESS LED indicates basic hardware status as shown in the following table. Color Indications Off Device is not yet functional, or the device has detected a problem with a power rail. Amber The device is being accessed.

### NI 5412 ACCESS and ACTIVE LEDs

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

NI 5412 NI 5412 Overview

<!--NI_TOPIC bundle=ni-fgen path=ni-5412-accessories.html language=enus -->
## TOPIC 00224: NI 5412 Accessories

- bundle_id: `ni-fgen`
- source_path: `ni-5412-accessories.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5412-accessories.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: National Instruments offers a variety of products to use with your signal generator, including cables and other accessories. Visit ni.com for more information.

### NI 5412 Accessories

National Instruments offers a variety of products
to use with your signal generator, including cables and other
accessories. Visit 
ni.com for more
information.

Parent topic:

NI 5412 NI 5412 Overview

<!--NI_TOPIC bundle=ni-fgen path=ni-5412-analog-gain-settings.html language=enus -->
## TOPIC 00225: NI 5412 Analog Gain Settings

- bundle_id: `ni-fgen`
- source_path: `ni-5412-analog-gain-settings.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5412-analog-gain-settings.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following table summarizes the maximum and minimum gain setting that you can apply for the NI-FGEN analog path options. Refer to the device specifications for more information about gain resolution. Analog Path Gain Summary (Matched Load Impedance) NI-FGEN Analog Path Maximum Gain Value Minimum

### NI 5412 Analog Gain Settings

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
| Note: Gain is unitless. |  |  |

Note

Parent topic:

NI 5412 Waveform Amplitude Control

<!--NI_TOPIC bundle=ni-fgen path=ni-5412-analog-output.html language=enus -->
## TOPIC 00226: NI 5412 Analog Output

- bundle_id: `ni-fgen`
- source_path: `ni-5412-analog-output.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5412-analog-output.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the NI 5412 Analog Output signal path. NI 5412 Analog waveforms are generated as follows: The 14-bit digital waveform data from the Waveform Generation Engine is passed to a to a digital gain circuit then a high-speed DAC. This DAC also implements a portion of the Analog O

### NI 5412 Analog Output

The following figure shows the NI 5412 Analog
Output signal path.

[IMAGE alt='image' src='GUID-6D4C36D6-D454-4961-979E-9F00D4097CE0-a5.gif']

NI 5412 Analog waveforms are generated as
follows:

1. The 14-bit digital waveform data from the Waveform Generation
Engine is passed to a to a digital gain circuit then a high-speed
DAC. This DAC also implements a portion of the Analog Output signal
path attenuation with a range of 0 dB to 3 dB. Refer to
the 
 NI PXI/PCI-5412 Specifications for the exact resolution. You can adjust the
amount of attenuation by configuring the 
Arbitrary Waveform Gain or Amplitude
properties, or the NIFGEN_ATTR_ARB_GAIN or NIFGEN_ATTR_FUNC_AMPLITUDE attributes. NI-FGEN calculates and sets the correct amount of attenuation required, corresponding to the gain setting.
2. Following the DAC are the High-Gain and Low-Gain amplifiers.
NI-FGEN selects the High-Gain or Low-Gain Amplifier paths by
default. To select the path manually, refer to the 
Analog
Path property or NIFGEN_ATTR_ANALOG_PATH attribute.
3. The signal then passes through attenuators, and
amplifiers.
4. The signal then passes through the DC Offset Amplifier that
adds the desired DC offset voltage. You can adjust the amount of DC
offset added to the signal, up to one half the value of the NI-FGEN
gain setting. For more information, refer to the Arbitrary Waveform Offset and 
DC Offset properties, or the 
 NIFGEN_ATTR_ARB_OFFSET and NIFGEN_ATTR_FUNC_DC_OFFSET attributes.
5. The signal then passes through the Pre-Amp Attenuation section,
a set of selectable solid-state attenuators that provide 0 dB
to 12 dB of attenuation in 3 dB increments. You can adjust the
amount of attenuation by adjusting 
 NIFGEN_ATTR_ARB_GAIN . NI-FGEN
calculates and sets the correct amount of attenuation required,
corresponding to the gain setting. Refer to the Arbitrary Waveform Gain and 
Amplitude properties, or the NIFGEN_ATTR_ARB_GAIN and NIFGEN_ATTR_FUNC_AMPLITUDE attributes for more information.
6. Following the Pre-Amp Attenuation section, the signal can take
one of two paths: the High-Gain or Low-Gain Amplifier path. NI-FGEN
automatically selects the best amplifier path between the High-Gain
and Low-Gain amplifiers by default based on the gain or amplitude
setting. Alternatively, you can set the signal path to remain
constant regardless of the gain setting for applications requiring
one path or the other. Refer to the Analog
Path property or the NIFGEN_ATTR_ANALOG_PATH attribute for more information.
  1. The High-Gain Amplifier path is used for waveform output
voltages greater than ±1.0 V into 50 Ω. The
amplifier has a fixed gain and is included in the signal path to
enable the AWG to provide the maximum V 
 pk-pk .
  2. The Low-Gain Amplifier path is used for waveforms that have all
output voltages equal to or smaller than ±1.0 V into
50 Ω. The amplifier has a fixed gain.
7. The signal passes through the Post Amp Attenuation section, a
set of two passive attenuators 12 dB and 24 dB. You can adjust the
amount of attenuation by configuring the Arbitrary Waveform Gain and 
Amplitude properties, or the NIFGEN_ATTR_ARB_GAIN and NIFGEN_ATTR_FUNC_AMPLITUDE attributes. NI-FGEN calculates and sets the correct amount of attenuation required, corresponding to the gain setting.
8. The signal then passes through the Output Enable relay. When
the Output Enable relay is disabled, ground is connected to the
output through a 50 Ω or a 75 Ω resistor.
Intentionally, waveform generation continues while the output
enable relay is disabled. When the relay is enabled, the analog
waveform is seen at the CH 0 connector. You can enable or
disable the output of the analog waveform generator, refer to the 
niFgen
Output Enable VI or the niFgen_ConfigureOutputEnabled function for more information.
9. The signal then passes through a 50 Ω/75 Ω selector to the
CH 0 connector. You can configure the output impedance of the analog waveform generator, refer to the niFgen Configure Output Impedance VI or the niFgen_ConfigureOutputImpedance function.

Note

Parent topic:

NI 5412 Theory of Operation

<!--NI_TOPIC bundle=ni-fgen path=ni-5412-arbitrary-sequence-mode.html language=enus -->
## TOPIC 00227: NI 5412 Arbitrary Sequence Mode

- bundle_id: `ni-fgen`
- source_path: `ni-5412-arbitrary-sequence-mode.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5412-arbitrary-sequence-mode.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Arbitrary Sequence mode allows you to load multiple waveforms in the onboard memory of the NI 5412. A finite number of samples make a waveform. To generate these downloaded waveforms in a specific order, you must prepare a sequence, which contains a number of segments in a specific order. Each segme

### NI 5412 Arbitrary Sequence Mode

*Arbitrary Sequence mode* allows you to load multiple
waveforms in the onboard memory of the NI 5412. A finite
number of samples make a waveform. To generate these downloaded
waveforms in a specific order, you must prepare a sequence, which
contains a number of segments in a specific order. Each segment
specifies a downloaded waveform, a number of loops to repeat the
selected waveform, and a numeric offset in which a marker is
generated by the device.

Parent topic:

NI 5412 Output Modes

Related concepts:

- Arbitrary Sequence Mode

<!--NI_TOPIC bundle=ni-fgen path=ni-5412-arbitrary-waveform-mode.html language=enus -->
## TOPIC 00228: NI 5412 Arbitrary Waveform Mode

- bundle_id: `ni-fgen`
- source_path: `ni-5412-arbitrary-waveform-mode.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5412-arbitrary-waveform-mode.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5412 supports Arbitrary Waveform output mode. Arbitrary Waveform mode generates waveforms from user-created/provided waveform arrays of numeric data. The waveform arrays are downloaded to the arbitrary waveform generator onboard memory. Arbitrary Waveform mode also uses memory to store the in

### NI 5412 Arbitrary Waveform Mode

The NI 5412 supports Arbitrary Waveform output mode. Arbitrary Waveform mode generates waveforms from
user-created/provided waveform arrays of numeric data. The waveform
arrays are downloaded to the arbitrary waveform generator onboard
memory. *Arbitrary Waveform mode* also uses memory to
store the instructions for generating waveform sequences in the
onboard memory.

Parent topic:

NI 5412 Output Modes

Related concepts:

- Arbitrary Waveform Output Mode

<!--NI_TOPIC bundle=ni-fgen path=ni-5412-attenuation.html language=enus -->
## TOPIC 00229: NI 5412 Attenuation

- bundle_id: `ni-fgen`
- source_path: `ni-5412-attenuation.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5412-attenuation.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Analog Output path has two passive attenuation sections. Preamplifier attenuation is prior to the High-Gain and Low-Gain Amplifier paths, and postamplifier attenuation is after the High-Gain and Low-Gain Amplifier paths. The main DAC provides 0 to 3 dB of signal attenuation. Amplitude control is

### NI 5412 Attenuation

The Analog Output path has two passive attenuation
sections. *Preamplifier attenuation* is prior to the High-Gain
and Low-Gain Amplifier paths, and *postamplifier attenuation* is after the
High-Gain and Low-Gain Amplifier paths.

The main *DAC* provides 0 to 3 dB of signal attenuation. Amplitude control is implemented after the DAC. Attenuating the DAC output signal allows you to vary the signal amplitude while maintaining the dynamic range of the DAC. You do not lose any bits from the digital representation of the signal and you do not sacrifice dynamic range, as you would if you control amplitude by using smaller data ranges of the DAC.

For the Low-Gain and the High-Gain Amplifier paths, maximum attenuation is
51 dB. NI-FGEN automatically determines the correct value of attenuation in dB and configures the attenuation based on the set
gain. The
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

NI 5412 Waveform Amplitude Control

Related concepts:

- NI 5412 Preamplifier Attenuation
- NI 5412 Postamplifier Attenuation
- NI 5412 DAC Attenuation

<!--NI_TOPIC bundle=ni-fgen path=ni-5412-burst-trigger-mode.html language=enus -->
## TOPIC 00230: NI 5412 Burst Trigger Mode

- bundle_id: `ni-fgen`
- source_path: `ni-5412-burst-trigger-mode.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5412-burst-trigger-mode.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: In Burst trigger mode, calling the first Start trigger begins waveform generation. The waveform then generates continually. Output Mode Trigger Behavior Arbitrary Waveform Mode Burst trigger mode operates the same as Continuous trigger mode when the device is operating in Arbitrary Waveform mode. Ar

### NI 5412 Burst Trigger Mode

In Burst trigger mode, calling the first Start
trigger begins waveform generation. The waveform then generates
continually.

| Output Mode | Trigger Behavior |
| --- | --- |
| Arbitrary Waveform Mode | Burst trigger mode operates the same as Continuous trigger mode when the device is operating in Arbitrary Waveform mode. |
| Arbitrary Sequence Mode | Each waveform you define in the sequence list generates continuously until another Start trigger occurs. A Start trigger causes the waveform generation to switch to the waveform defined by the next segment, after the current waveform finishes. After the sequence list is exhausted, the waveform generation returns to the waveform defined by the first segment and subsequent Start triggers will restart the process. Only the first Start trigger which signals a transition to the next segment is recognized, all subsequent Start triggers are ignored until the currently generating waveform finishes. The transition of one waveform to the next can be made amplitude continuous if waveforms in all segments start and end at the same amplitude. Alternatively, this also can be accomplished by ensuring that the waveforms from one segment to the next end and start at the same amplitude. This amplitude continuous transition is shown in the previous Arbitrary Sequence Mode examples by the transitions of Segments 1 to Segment 2, and Segment 3 to Segment 4. The transition from Segment 2 to Segment 3 shows a discontinuous transition, going from a positive value on the last sample of the ramp waveform right to a midrange value of the sine waveform. |

Parent topic:

NI 5412 Trigger Modes

Related concepts:

- NI 5412 Continuous Trigger Mode

<!--NI_TOPIC bundle=ni-fgen path=ni-5412-calibration.html language=enus -->
## TOPIC 00231: NI 5412 Calibration

- bundle_id: `ni-fgen`
- source_path: `ni-5412-calibration.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5412-calibration.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Before shipping your signal generator, NI calibrated your device to ensure that all features are within specifications. Calibration is a set of operations that compares the values indicated by a measuring instrument or measuring system to the corresponding values realized by external standards. You

### NI 5412 Calibration

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

NI 5412 NI 5412 Overview

<!--NI_TOPIC bundle=ni-fgen path=ni-5412-ch-0-connector.html language=enus -->
## TOPIC 00232: NI 5412 CH 0 Connector

- bundle_id: `ni-fgen`
- source_path: `ni-5412-ch-0-connector.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5412-ch-0-connector.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The CH 0 connector is the analog waveform output terminal. The maximum output levels from this connector depend on the type of load termination. For example, if the output of the device terminates into a 50 Ω load, the maximum output levels are ±6 V, while the maximum output levels are ±12 V when th

### NI 5412 CH 0 Connector

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

The NI 5412 has the ability to configure the
output signal amplitude based on a user-configured load impedance
setting. This capability is desirable when you use the NI 5412
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

NI 5412 NI 5412 Overview

<!--NI_TOPIC bundle=ni-fgen path=ni-5412-clk-in-connector.html language=enus -->
## TOPIC 00233: NI 5412 CLK IN Connector

- bundle_id: `ni-fgen`
- source_path: `ni-5412-clk-in-connector.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5412-clk-in-connector.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The CLK IN front panel connector can accept an external Reference clock, external Sample clock, or external Sample clock timebase. Do not change the external clocks while generating waveforms. Only modify the frequency of the external clock before you start the waveform generation or after you sto

### NI 5412 CLK IN Connector

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

NI 5412 NI 5412 Overview

Related concepts:

- NI 5412 Phase-Locked Loop Reference Clock

<!--NI_TOPIC bundle=ni-fgen path=ni-5412-clocking-options.html language=enus -->
## TOPIC 00234: NI 5412 Clocking Options

- bundle_id: `ni-fgen`
- source_path: `ni-5412-clocking-options.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5412-clocking-options.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Waveform generation is driven by the Sample clock; depending on your application, some sources may be better choices than others. You can use the following sources for the NI 5412 Sample clock: Internal Sample clock—the onboard clock is used as the Sample clock source and the Sample clock is derived

### NI 5412 Clocking Options

Waveform generation is driven by the Sample clock;
depending on your application, some sources may be better choices
than others. You can use the following sources for the
NI 5412 Sample clock:

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
configure the NI 5412 clock settings for
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

NI 5412 Theory of Operation

Related concepts:

- NI 5412 Internal Sample Clock
- NI 5412 External Sample Clock
- NI 5412 Phase-Locked Loop Reference Clock

<!--NI_TOPIC bundle=ni-fgen path=ni-5412-clocking.html language=enus -->
## TOPIC 00235: NI 5412 Clocking

- bundle_id: `ni-fgen`
- source_path: `ni-5412-clocking.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5412-clocking.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5412 has a Sample clock rate of 10 Hz to 100 MHz. The timing of the device is very flexible, and you have multiple choices for deriving the Sample clock. There are modes for deriving the Sample clock from the internal Sample clock timebase, as well as modes to provide external clocks. You als

### NI 5412 Clocking

The NI 5412 has a Sample clock
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

NI 5412 Theory of Operation

Related concepts:

- NI 5412 Clocking Options
- NI 5412 Internal Sample Clock
- NI 5412 Phase-Locked Loop Reference Clock
- NI 5412 External Sample Clock
- NI 5412 Exporting Clocks

<!--NI_TOPIC bundle=ni-fgen path=ni-5412-continuous-trigger-mode.html language=enus -->
## TOPIC 00236: NI 5412 Continuous Trigger Mode

- bundle_id: `ni-fgen`
- source_path: `ni-5412-continuous-trigger-mode.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5412-continuous-trigger-mode.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The waveform you downloaded generates continuously after receiving one Start trigger. All Start triggers after the first Start trigger are ignored. Output Mode Trigger Behavior Arbitrary Waveform Mode The waveform you downloaded generates continuously after receiving one Start trigger. All Start tri

### NI 5412 Continuous Trigger Mode

The waveform you downloaded generates continuously
after receiving one Start trigger. All Start triggers after the
first Start trigger are ignored.

| Output Mode | Trigger Behavior |
| --- | --- |
| Arbitrary Waveform Mode | The waveform you downloaded generates continuously after receiving one Start trigger. All Start triggers after the first Start trigger are ignored. |
| Arbitrary Sequence Mode | The waveform pattern you define in the sequence list generates continuously by continually cycling through the sequence list. Only one Start trigger is required to start waveform generation. After the device receives a Start trigger, the waveform generation starts at the first segment and continues through the last segment, and then loops back to the start of the first segment, continuing indefinitely. All Start triggers after the first Start trigger that starts waveform generation are ignored. |

Parent topic:

NI 5412 Trigger Modes

<!--NI_TOPIC bundle=ni-fgen path=ni-5412-dac-attenuation.html language=enus -->
## TOPIC 00237: NI 5412 DAC Attenuation

- bundle_id: `ni-fgen`
- source_path: `ni-5412-dac-attenuation.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5412-dac-attenuation.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The main DAC output can be fine-tuned for attenuation, which provides 0 to 3 dB of the Analog Output path signal attenuation. This fine-tuning of the main DAC attenuation is performed by the gain DAC. Adjust the gain DAC using the Gain DAC Value property or the NIFGEN_ATTR_GAIN_DAC_VALUE attribute.

### NI 5412 DAC Attenuation

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

NI 5412 Attenuation

<!--NI_TOPIC bundle=ni-fgen path=ni-5412-data-mask.html language=enus -->
## TOPIC 00238: NI 5412 Data Mask

- bundle_id: `ni-fgen`
- source_path: `ni-5412-data-mask.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5412-data-mask.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The signal generator supports analog data masks and static values. The data mask allows you to shield bits of the data to be replaced with the corresponding static value bits. For example, a mask of 0xFF00 and a static value of 0xAAAA applied to a DC waveform with a value of 0x1111 produces a DC wav

### NI 5412 Data Mask

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

NI 5412 NI 5412 Overview

<!--NI_TOPIC bundle=ni-fgen path=ni-5412-dc-offset.html language=enus -->
## TOPIC 00239: NI 5412 DC Offset

- bundle_id: `ni-fgen`
- source_path: `ni-5412-dc-offset.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5412-dc-offset.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5412 supports a DC offset before the attenuation chain that affects the maximum value of DC offset for a given gain setting. This preattenuation architecture requires two rules for setting the DC offset: The magnitude of the maximum value of offset can be no more than ½ of the configured gain

### NI 5412 DC Offset

The NI 5412 supports a DC offset before the attenuation chain that affects the maximum value of DC offset for a given gain setting. This preattenuation architecture requires two rules for setting the DC offset:

1. The magnitude of the maximum value of offset can be no more than ½ of the configured gain setting for the NI 5412.
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

NI 5412 Waveform Amplitude Control

<!--NI_TOPIC bundle=ni-fgen path=ni-5412-digital-filter.html language=enus -->
## TOPIC 00240: NI 5412 Digital Filter

- bundle_id: `ni-fgen`
- source_path: `ni-5412-digital-filter.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5412-digital-filter.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The main DAC provides an internal digital filter. When digital filtering is enabled, the main DAC runs at a faster rate, referred to as the effective sample rate (ESR). The waveform data transfers to the main DAC at the configured Sample clock rate; the internal digital filter interpolates by a fact

### NI 5412 Digital Filter

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

In general, use the digital filter for signals
containing large sinusoidal waveform content, such as AM and FM,
sinc, and sinusoidal chirp waveforms. The filter can be disabled
for signals that are better represented without filtering, such as
square waves or waveforms containing many pulse characteristics. If
you enable the digital filter without setting the interpolation
factor, NI-FGEN automatically uses the highest interpolation factor
possible in accordance with the above table. You can enable or disable the filter by calling the 
Configure
Digital Filter VI or the 
niFgen_EnableDigitalFilter and 
niFgen_DisableDigitalFilter functions.

#### Related Topics

*Filtering and
Interpolation*

*Aliased Images*

Parent topic:

NI 5412 Filtering Effects

Related concepts:

- Filtering and Interpolation
- Aliased Images

<!--NI_TOPIC bundle=ni-fgen path=ni-5412-digital-gain.html language=enus -->
## TOPIC 00241: NI 5412 Digital Gain

- bundle_id: `ni-fgen`
- source_path: `ni-5412-digital-gain.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5412-digital-gain.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Digital gain multiplies waveform data by a factor you specify in the Digital Gain property or the NIFGEN_ATTR_DIGITAL_GAIN attribute before converting the data to an analog signal in the DAC. Digital gain can be changed during generation without the glitches caused by switching that are common when

### NI 5412 Digital Gain

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

NI 5412 Waveform Amplitude Control

<!--NI_TOPIC bundle=ni-fgen path=ni-5412-events.html language=enus -->
## TOPIC 00242: NI 5412 Events

- bundle_id: `ni-fgen`
- source_path: `ni-5412-events.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5412-events.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use events to indicate when a specific hardware condition has been met on the NI 5412. An event is a signal generated by the NI device at a device state. The NI 5412 supports Ready for Start, Started, Marker, and Done events. The NI 5412 also supports the use of event delays. Related Topics

### NI 5412 Events

You can use *events* to indicate when a specific
hardware condition has been met on the NI 5412. An event is a
signal generated by the NI device at a device state. The NI 5412
supports Ready for Start, Started, *Marker*, and Done
events. The NI 5412 also supports the use of *event delays*.

#### Related Topics

*Creating a Marker
Event*

Parent topic:

NI 5412 NI 5412 Overview

Related concepts:

- Events
- Marker Events
- Event Delays
- Creating a Marker Event

<!--NI_TOPIC bundle=ni-fgen path=ni-5412-exporting-clocks.html language=enus -->
## TOPIC 00243: NI 5412 Exporting Clocks

- bundle_id: `ni-fgen`
- source_path: `ni-5412-exporting-clocks.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5412-exporting-clocks.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5412 provides two resources for exporting your clocks and multiple destinations to route to. The following table shows the available clock signals that can be routed to devices external to the NI 5412, the labels NI-FGEN uses to describe them and the destination options. Clock to be Exported

### NI 5412 Exporting Clocks

The NI 5412 provides two resources for
exporting your clocks and multiple destinations to route to.

[IMAGE alt='image' src='GUID-E036FAB1-22AB-4A21-8BEC-D3B45326B2D9-a5.gif']

The following table shows the available clock
signals that can be routed to devices external to the NI 5412,
the labels NI-FGEN uses to describe them and the destination
options.

| Clock to be Exported | Destination Options |
| --- | --- |
| Sample Clock | PFI<0..1> SMB connector |
| PXI_Trig<0..6> (PXI), RTSI<0..6> (PCI) |  |
| Sample clock timebase | PFI<0..1> SMB connector |
| PXI_Trig<0..6> (PXI), RTSI<0..6> (PCI) |  |
| Reference Clock | PFI<0..1> SMB connector |
| PXI_Trig<0..6> (PXI), RTSI<0..6> (PCI) |  |
| Onboard Reference Clock | RTSI7 |

#### Sample Clock

For synchronization purposes, the NI 5412
allows you to export your Sample clock so that other devices can
have the same timing as the NI 5412. The Sample clock can be
routed to the PFI<0..1> front panel SMB connectors,
PXI_Trig<0..6> lines on the PXI trigger bus, or the
RTSI<0..6> (PCI) lines.

Additionally, the exported clock can be divided
down by an integer value (no less than 2) before being exported to
the PFI<0..1> SMB connectors, PXI_Trig<0..6> lines, or
the RTSI<0..6> (PCI) lines. Refer to the 
Exported Sample Clock Divisor property or the 
NIFGEN_ATTR_EXPORTED_SAMPLE_CLOCK_DIVISOR attribute for more information about configuring the Sample
clock divisor.

#### Sample Clock Timebase

For synchronization purposes, the NI 5412
allows you to export your Sample clock timebase so that other
devices can have the same timing as the NI 5412. The Sample
clock timebase can be routed to the PFI<0..1> SMB connectors
on the front panel, the PXI_Trig<0..6> lines on the PXI
trigger bus, or the RTSI<0..6> (PCI) lines.

Additionally, the exported clock can be divided
down by an integer value before being exported to the
PFI<0..1> SMB connectors, the PXI_Trig<0..6> lines, or
the RTSI<0..6> (PCI) lines. Refer to 
Exported Sample Clock Timebase Divisor property or the 
NIFGEN_ATTR_EXPORTED_SAMPLE_CLOCK_TIMEBASE_DIVISOR attribute for more information about configuring the Sample
clock divisor.

#### Reference Clock

For synchronization purposes, the NI 5412
allows you to export your PLL Reference clock so that other devices
can lock their clock sources to the same signal. Referring to the
previous image, this clock is the actual clock that is configured
for the NI 5412 phase-locked loop circuit to use as a
reference. You must have a Reference clock configured as a PLL
Reference Clock source for the signal to be available for
exporting. The Reference clock can be routed to the PFI<0..1>
SMB connectors on the front panel, the PXI_Trig<0..6> lines
on the PXI trigger bus, or the RTSI<0..6> (PCI) lines.

Note

#### Onboard Reference Clock

The onboard Reference clock is a dedicated 10 MHz
clock for PCI modules only. The onboard Reference clock can only be
exported to RTSI7, for other modules to use, and to reimport as the
Reference clock. You can export the onboard Reference clock to
other modules on RTSI7 and then reimport it so that all devices
(including the master) can use the same Reference clock.

#### Destination Options

PFI<0..1>—The Sample clock and the
Reference clock can be exported to the PFI 0 and PFI 1 SMB
connectors on the front panel to synchronize external devices. You
must configure the device to export the desired clock to the PFI
SMB connectors.

Note

PXI_Trig<0..6>—The Sample clock and
the Reference clock can be exported to the PXI_Trig lines or RTSI
(PCI) lines. The PXI/PCI standard allows for devices to route
signals to other devices in your PXI chassis to enhance device to
device synchronization. Refer to the chassis documentation for
specifications to ensure the reference signal is within tolerance.
You must configure the device to export the desired clock to the
PXI_Trig line or RTSI line. When exporting signals,
PXI_Trig<0..6> are equivalent to RTSI_<0..6>.

Refer to the 
niFgen
Export Signal VI or the 
niFgen_ExportSignal
function for more information about configuring the destinations
for the desired clock signal.

Parent topic:

NI 5412 Theory of Operation

<!--NI_TOPIC bundle=ni-fgen path=ni-5412-exporting-signals.html language=enus -->
## TOPIC 00244: NI 5412 Exporting Signals

- bundle_id: `ni-fgen`
- source_path: `ni-5412-exporting-signals.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5412-exporting-signals.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The signal generator contains seven PXI trigger lines or seven RTSI (PCI devices only) lines that are available for sending signal generator-specific information to other devices that have PXI trigger or RTSI bus connectors. The signal generator also connects to the PXI star trigger line, which you

### NI 5412 Exporting Signals

Note

ni.com/products

The signal generator has connectors on the front
panel to route signals to devices external to a PXI or PCI
chassis. The following table shows the signals available for export
and the lines they can be routed to. To determine all possible
signal routes for your device, refer to 
*Signal Routing*.

|  |  | Destination |  |
| --- | --- | --- | --- |
| PXI_Trig<0..6>, RTSI<0..6>, or PXI_STAR | PFI 0 and PFI 1 Connectors |  |  |
| Exported Clocks, Triggers, and Events | Sample Clock | Yes | Yes * |
| Sample Clock Timebase | Yes | Yes |  |
| PLL Reference Source | Yes | Yes* |  |
| Out Start trigger | Yes | Yes |  |
| Marker Event | Yes | Yes |  |
| * SYNC OUT/PFI 0 is optimized for the Sample clock and PLL reference source signals and has slightly less jitter than PFI 1. SYNC OUT/PFI 0 is the recommended terminal to use for exporting clocks. |  |  |  |

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

NI 5412 NI 5412 Overview

Related concepts:

- NI 5412 Signal Routing

<!--NI_TOPIC bundle=ni-fgen path=ni-5412-external-sample-clock.html language=enus -->
## TOPIC 00245: NI 5412 External Sample Clock

- bundle_id: `ni-fgen`
- source_path: `ni-5412-external-sample-clock.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5412-external-sample-clock.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5412 can accept an external clock to directly drive the Sample clock. When using an external Sample clock, the frequency stability and accuracy of the Sample clock is determined by the provided external Sample clock. The following figure shows possible Sample Clock paths. You can set the cloc

### NI 5412 External Sample Clock

The NI 5412 can accept an
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

The NI 5412 incorporates
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
reprograms the NI 5412 for the new settings,
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

NI 5412 Clocking Options

<!--NI_TOPIC bundle=ni-fgen path=ni-5412-filtering-effects.html language=enus -->
## TOPIC 00246: NI 5412 Filtering Effects

- bundle_id: `ni-fgen`
- source_path: `ni-5412-filtering-effects.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5412-filtering-effects.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The delay from the time at which the device receives a trigger to the time at which the analog output signal is generated increases if the digital and/or analog filters in the Analog Output path are enabled. In the case of digital filtering, delay also increases with increase in interpolation. The

### NI 5412 Filtering Effects

Analog Output path

Note

Refer to 
*Digital
Filter* for interpolation options. Refer to the 
*device
specifications* for the delay from trigger to analog output
based on different filtering options.

Parent topic:

NI 5412 Analog Output

Related concepts:

- NI 5412 Analog Output
- NI 5412 Digital Filter

<!--NI_TOPIC bundle=ni-fgen path=ni-5412-filtering-effects_2.html language=enus -->
## TOPIC 00247: NI 5412 Filtering Effects

- bundle_id: `ni-fgen`
- source_path: `ni-5412-filtering-effects_2.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5412-filtering-effects_2.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The delay from the time at which the device receives a trigger to the time at which the analog output signal is generated increases if the digital and/or analog filters in the Analog Output path are enabled. In the case of digital filtering, delay also increases with increase in interpolation. The

### NI 5412 Filtering Effects

Analog Output path

Note

Refer to 
*Digital
Filter* for interpolation options. Refer to the 
*device
specifications* for the delay from trigger to analog output
based on different filtering options.

Parent topic:

NI 5412 Triggering

<!--NI_TOPIC bundle=ni-fgen path=ni-5412-front-panel.html language=enus -->
## TOPIC 00248: NI 5412 Front Panel

- bundle_id: `ni-fgen`
- source_path: `ni-5412-front-panel.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5412-front-panel.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the NI PXI-5412 front panel. This front panel has four SMB connectors. The ACCESS and ACTIVE LEDs indicate the status of the PXI module. The CH 0 SMB connector is the analog output from which arbitrary waveforms are generated. The CLK IN SMB connector provides the device w

### NI 5412 Front Panel

The following figure shows the NI PXI-5412 front panel. This front panel has
four SMB connectors.

[IMAGE alt='image' src='GUID-4E0F99EE-EF5F-45DA-A5A4-2BACBD38C7E8-a5.gif']

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

NI 5412 NI 5412 Overview

Related concepts:

- NI 5412 ACCESS and ACTIVE LEDs
- NI 5412 CH 0 Connector
- NI 5412 CLK IN Connector
- NI 5412 PFI Connectors

<!--NI_TOPIC bundle=ni-fgen path=ni-5412-hardware-state-diagram.html language=enus -->
## TOPIC 00249: NI 5412 Hardware State Diagram

- bundle_id: `ni-fgen`
- source_path: `ni-5412-hardware-state-diagram.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5412-hardware-state-diagram.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following diagram shows the hardware states of the signal generator. The signal generator can be in one of the following six basic states during the course of operation. Idle—The device is not generating a waveform. All session properties or attributes can be programmed in the Idle state. In the

### NI 5412 Hardware State Diagram

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

NI 5412 Theory of Operation

Related concepts:

- Programming State Model

<!--NI_TOPIC bundle=ni-fgen path=ni-5412-internal-sample-clock.html language=enus -->
## TOPIC 00250: NI 5412 Internal Sample Clock

- bundle_id: `ni-fgen`
- source_path: `ni-5412-internal-sample-clock.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen/raw/resource/enus/ni-5412-internal-sample-clock.html
- document_id: `ni-fgen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5412 can derive a Sample clock from its main internal timing source—the onboard Sample clock timebase. The signal generator provides a high-precision 100 MHz Voltage Controlled Crystal Oscillator (VCXO) clock source for the Sample clock timebase. As shown in the following figure, the Sample c

### NI 5412 Internal Sample Clock

The NI 5412 can derive a Sample
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

NI 5412 Clocking Options
