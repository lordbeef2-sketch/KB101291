# NI DOCUMENT BUNDLE: ni-reconfigurable-oscilloscopes

<!--NI_BUNDLE_CHUNK bundle=ni-reconfigurable-oscilloscopes start=1 end=86 -->
<!--NI_TOPIC bundle=ni-reconfigurable-oscilloscopes path=accuracy.html language=enus -->
## TOPIC 00001: Accuracy

- bundle_id: `ni-reconfigurable-oscilloscopes`
- source_path: `accuracy.html`
- source_url: https://docs-be.ni.com/bundle/ni-reconfigurable-oscilloscopes/raw/resource/enus/accuracy.html
- document_id: `ni-reconfigurable-oscilloscopes`
- page_type: `leaf`
- content_type: `concept`
- source_description: Accuracy is a measure of the ability of a device to indicate the true value of a measured signal. Accuracy is usually expressed as a percentage of the specified value, for example, 5 V ±1%. Signal CharacteristicsKnowing the characteristics of the signal under consideration helps you to choose the co

### Accuracy

Accuracy is a measure of the ability of a device to indicate the true value of a measured signal.
 Accuracy is usually expressed as a percentage of the specified value, for example, 5 V
 ±1%.

#### Signal Characteristics

Knowing the
 characteristics of the signal under consideration helps you to choose the correct settings
 to maximize measurement accuracy. Such characteristics include:

Peak-to-peak value

pk-pk

max

min

resolution

pk-pk

[IMAGE alt='image' src='GUID-A88EBD28-CAC2-4542-9E4B-66DDFD921A6F-a5.gif']

[IMAGE alt='image' src='GUID-54292011-85FC-455D-B4B5-9CC2F314BED6-a5.gif']

[IMAGE alt='image' src='GUID-585F13B8-416F-48E6-83F3-81E26ACB5520-a5.gif']

Source impedance

Input frequency

alias

Nyquist Theorem

General signal shape

[IMAGE alt='image' src='GUID-F1AF06F7-6A52-43D1-830F-808C833D2A68-a5.gif']

Input coupling

Parent topic:

Oscilloscopes Fundamentals

Related concepts:

- Resolution
- Impedance and Impedance Matching
- Aliasing
- Nyquist Theorem

<!--NI_TOPIC bundle=ni-reconfigurable-oscilloscopes path=active-image.html language=enus -->
## TOPIC 00002: Active Image

- bundle_id: `ni-reconfigurable-oscilloscopes`
- source_path: `active-image.html`
- source_url: https://docs-be.ni.com/bundle/ni-reconfigurable-oscilloscopes/raw/resource/enus/active-image.html
- document_id: `ni-reconfigurable-oscilloscopes`
- page_type: `leaf`
- content_type: `concept`
- source_description: The active video image resulting from the scanning always has an aspect ratio (horizontal/vertical) of 4/3, independent of the video format. The color composite video signal shows that the scanning process requires some additional room on the left and right sides of each line, as well as on the top

### Active Image

The active video image resulting from the scanning always has an aspect ratio
 (horizontal/vertical) of 4/3, independent of the video format. The *color composite
 video signal* shows that the scanning process requires some additional room on
 the left and right sides of each line, as well as on the top and bottom of the active
 video image region. This additional room includes the synchronization signals, color
 bursts, and other format-specific information, like the ITS, which are not part of the
 active video image. Approximately 90% of all the lines and 80% of each line can transmit
 the active image information. The exact values depend on the video format, as shown in
 the following table.

| Video Format | Lines/Frame | Active Lines | Frame Rate | Line Duration | Active Line Duration |
| --- | --- | --- | --- | --- | --- |
| NTSC | 525 | 480/486 | 29.97 frames/sec | 63.55 µs | 52.2 µs |
| PAL/SECAM | 625 | 576 | 25.00 frames/sec | 64.00 µs | 52.0 µs |

The *Active Lines* represents the number of lines that are actually used to transmit
 the image information. For example, only 480 lines out of 525 lines/frame transmit the
 image information in NTSC. Likewise, on each line, the image information is transmitted
 only during the active lines sequence, which is shorter than the entire line duration.
 For example, of 63.55 µs only 52.2 µs are the active line duration in NTSC. Frame rate
 is the scanning speed described in *Scanning Speed*.

Parent topic:

Video Fundamentals

Related concepts:

- Composite and Component Video Signals
- Scanning Speed

<!--NI_TOPIC bundle=ni-reconfigurable-oscilloscopes path=aliasing.html language=enus -->
## TOPIC 00003: Aliasing

- bundle_id: `ni-reconfigurable-oscilloscopes`
- source_path: `aliasing.html`
- source_url: https://docs-be.ni.com/bundle/ni-reconfigurable-oscilloscopes/raw/resource/enus/aliasing.html
- document_id: `ni-reconfigurable-oscilloscopes`
- page_type: `leaf`
- content_type: `concept`
- source_description: Aliasing is the misrepresentation of high frequencies as lower frequencies. An alias appears in sampled data acquired at too low a sampling rate compared to the Nyquist frequency of the signal being sampled.In systems where you want to perform accurate measurements using sampled data, the sampling r

### Aliasing

Aliasing is the misrepresentation of high frequencies as lower frequencies. An alias appears in
 sampled data acquired at too low a sampling rate compared to the *Nyquist*
 frequency of the signal being sampled.

In systems where you want to perform accurate measurements using sampled data, the sampling rate
 must be set high enough to prevent aliasing, or an optional anti-aliasing filter must be
 introduced before the A/D converter to restrict the bandwidth of the input signal to meet the
 sampling criteria. An anti-aliasing filter attenuates unwanted high-frequency signals (which
 otherwise would appear as undesired, aliased frequency components) of an analog signal prior
 to its conversion into a digital value. The actual bandwidth in which you can make correct
 measurements without aliasing is called the alias-free bandwidth. After aliasing has been
 introduced into a sampled signal, there is no general way to remove it.

In video applications, several forms of visual aliasing are possible:

Temporal aliasing

Raster scan aliasing

Stair-step aliasing

Parent topic:

Sample Rate

Related concepts:

- Nyquist Theorem

<!--NI_TOPIC bundle=ni-reconfigurable-oscilloscopes path=averaging-to-minimize-noise.html language=enus -->
## TOPIC 00004: Averaging to Minimize Noise

- bundle_id: `ni-reconfigurable-oscilloscopes`
- source_path: `averaging-to-minimize-noise.html`
- source_url: https://docs-be.ni.com/bundle/ni-reconfigurable-oscilloscopes/raw/resource/enus/averaging-to-minimize-noise.html
- document_id: `ni-reconfigurable-oscilloscopes`
- page_type: `leaf`
- content_type: `concept`
- source_description: At a minimum to complete an RIS acquisition, the number of TDC values must be equal to the oversampling factor. However, this does not guarantee a cleanly reconstructed signal. The following figures show three acquisitions of a perfectly linear edge.The following figure shows that the sample in bin

### Averaging to Minimize Noise

At a minimum to complete an *RIS* acquisition, the number of TDC values must be equal
 to the oversampling factor. However, this does not guarantee a cleanly reconstructed signal. The
 following figures show three acquisitions of a perfectly linear edge.

The following figure shows that the sample in bin number 1 is extremely close to its right-hand
 bin edge. When NI-SCOPE returns the RIS waveform, this sample is coerced to the middle of the
 bin. In similar fashion, each sample is coerced to the center of its bin.

[IMAGE alt='image' src='GUID-166DBE2D-92EC-4FFB-A312-281085C909A6-a5.gif']

The following figure shows how NI-SCOPE returns the RIS waveform, with evenly-spaced samples:

[IMAGE alt='image' src='GUID-CD82AA92-A969-4CBB-AB06-DB678A0334DF-a5.gif']

Note

The following figure shows the acquisition using two averages. Notice that twice as many
 waveforms are required now.

[IMAGE alt='image' src='GUID-EE655ECE-FB29-4AE1-B242-94E1746FCF02-a5.gif']

The following figure shows the returned waveform from the averaged RIS acquisition:

[IMAGE alt='image' src='GUID-66D4777E-7E11-4301-9386-57160D99EEC9-a5.gif']

The higher the number of averages, the smaller the effect of coercing the time of samples.
 Therefore, it is generally important to use some amount of averaging with RIS. Increasing the
 amount of averaging increases the minimum number of waveforms necessary to reconstruct the RIS
 waveform and therefore, the time it takes to complete an acquisition.

#### Randomness in RIS Acquisitions

Note

Parent topic:

Equivalent-Time Sampling and Random Interleaved Sampling

Related concepts:

- Equivalent-Time Sampling and Random Interleaved Sampling

<!--NI_TOPIC bundle=ni-reconfigurable-oscilloscopes path=bandwidth.html language=enus -->
## TOPIC 00005: Bandwidth

- bundle_id: `ni-reconfigurable-oscilloscopes`
- source_path: `bandwidth.html`
- source_url: https://docs-be.ni.com/bundle/ni-reconfigurable-oscilloscopes/raw/resource/enus/bandwidth.html
- document_id: `ni-reconfigurable-oscilloscopes`
- page_type: `leaf`
- content_type: `concept`
- source_description: Bandwidth describes the difference between limiting frequencies within which the input signal can pass through the system with minimal amplitude loss — from the input at the tip of the probe or test fixture to the output data. The limiting frequencies that determine the bandwidth include both a high

### Bandwidth

Bandwidth describes the difference between limiting frequencies within which the input signal can
 pass through the system with minimal amplitude loss — from the
 input at the tip of the probe or test fixture to the output
 data. The limiting frequencies that determine the bandwidth
 include both a high and a low frequency that are specified as
 the frequency (in Hz) at which a sinusoidal input signal is
 attenuated to 70.7% of its original amplitude. This point is
 known as the -3 dB point.

[IMAGE alt='image' src='GUID-E91C65B0-B981-4EA2-BB78-E50CBFA137EB-a5.gif']

The following figure shows the four main areas that can affect the bandwidth of a digitizer:

[IMAGE alt='image' src='GUID-0FF6834B-25E5-4138-BF3D-F365D28F0A07-a5.gif']

1. Outside world to probe
2. Probe to input connector
3. Input connector to ADC
4. ADC to software

Parent topic:

Oscilloscopes Fundamentals

<!--NI_TOPIC bundle=ni-reconfigurable-oscilloscopes path=basic-elements-fpga-vis.html language=enus -->
## TOPIC 00006: Basic Elements FPGA VIs

- bundle_id: `ni-reconfigurable-oscilloscopes`
- source_path: `basic-elements-fpga-vis.html`
- source_url: https://docs-be.ni.com/bundle/ni-reconfigurable-oscilloscopes/raw/resource/enus/basic-elements-fpga-vis.html
- document_id: `ni-reconfigurable-oscilloscopes`
- page_type: `leaf`
- content_type: `concept`
- source_description: Detect Falling Edge.viDetects a transition from TRUE to FALSE on the input signal. Use the Detect Falling Edge VI inside a single-cycle timed loop. Input parameters Signal Specifies the signal in which to detect a FALSE to TRUE transition. Output parameters Edge detected Indicates whether a TRUE to

### Basic Elements FPGA VIs

#### Detect Falling Edge.vi

Detects a transition from TRUE to
 FALSE on the input signal. Use the Detect Falling
 Edge VI inside a single-cycle timed
 loop.

[IMAGE alt='image' src='GUID-02738AE8-5C15-4C84-8034-1CD76E1FFC8D-a5.gif']

| Input parameters |
| --- |
| Signal—Specifies the signal in which to detect a FALSE to TRUE transition. |

| Output parameters |
| --- |
| Edge detected—Indicates whether a TRUE to FALSE transition is detected on the input signal. |

#### Detect Rising Edge.vi

Detects a transition from FALSE to TRUE on the
 input signal. Use the Detect Rising Edge VI inside a single-cycle
 timed loop.

[IMAGE alt='image' src='GUID-AA4A63FE-8EF6-4722-A5AE-899EA04804E6-a5.gif']

| Input parameters |
| --- |
| Signal—Specifies the signal in which to detect a FALSE to TRUE transition. |

| Output parameters |
| --- |
| Edge detected—Indicates whether a FALSE to TRUE transition is detected on the input signal. |

#### Synchronous Latch.vi

The VI stores information about the previous TRUE values of the
 signal. You can reset the VI to search for another TRUE value of
 the same signal.

If the value of the set parameter is TRUE
 and the value of the clear parameter is FALSE, the VI output is
 TRUE.

If the value of the clear parameter is
 TRUE and the value of the set parameter is
 FALSE, the VI output is FALSE.

If the
 values of both the set and the clear parameters are FALSE, the
 output of the VI remains unchanged from the previous value.

If the values of
 both the set and the clear parameters are TRUE, the VI output is
 FALSE.

The internal state of the VI is not reset when the
 owning VI stops execution. The internal state of the VI is reset to
 FALSE when the owning VI is compiled or loaded. The internal
 state is also reset when the value of the clear parameter is set to
 TRUE.

[IMAGE alt='image' src='GUID-DA275C30-05FE-4E0B-B55C-3E3F66BCC41C-a5.gif']

| Input parameters |
| --- |
| Set—Specifies that the internal state of the VI is set to TRUE. Clear—Specifies that the internal state of the VI is set to FALSE. |

| Output parameters |
| --- |
| Out—Indicates the internal state retained within the VI. |

#### Read U128 FIFO.vi

Reads data from a 128-bit FIFO. This VI is a wrapper around the LabVIEW FPGA FIFO
 Read method, and exposes handshaking signals that control when to read data from the
 FIFO.

[IMAGE alt='image' src='GUID-DA275C30-05FE-4E0B-B55C-3E3F66BCC41C-a5.gif']

| Input parameters |
| --- |
| FIFO—Specifies the reference to the FIFO from which to read data. Configure the FIFO to use a 128-bit data type. Use the following typedef of this library to configure the FIFO's data type: <instr.lib>\\_niInstr\\Basic Elements\\v1\\FPGA\\Public\\U128.ctl. Ready for output—Specifies whether the consumer of the data read from the FIFO is ready to accept new data. If you set this parameter to TRUE, the consumer is ready to accept new data and this VI is allowed to read data from the FIFO. If you set this parameter to FALSE, this VI does not return new data. |

| Output parameters |
| --- |
| Output data—Returns the data read from the FIFO. Output data.high—Returns the higher 64-bits of the 128-bit data read from the FIFO. Output data.low—Returns the lower 64-bits of the 128-bit data read from the FIFO. Output valid—Indicates whether the output data read from the FIFO is valid during the current clock cycle. |

#### Read U16 FIFO.vi

Reads data from a 16-bit FIFO. This VI is a wrapper around the LabVIEW FPGA FIFO Read
 method, and exposes handshaking signals to control when data is read from the FIFO.

[IMAGE alt='image' src='GUID-487FC679-AB4C-4AEE-8CF7-A2A50D7DE1E5-a5.gif']

| Input parameters |
| --- |
| FIFO—Specifies the reference to the FIFO from which to read data. Configure the FIFO to use the U16 datatype. Ready for output—Specifies whether the consumer of the data read from the FIFO is ready to accept new data. If you set this parameter to TRUE, the consumer is ready to accept new data and this VI is allowed to read data from the FIFO. If you set this parameter to FALSE, this VI does not return new data. |

| Output parameters |
| --- |
| Output data—Returns the data read from the FIFO. Output valid—Indicates whether the output data read from the FIFO is valid during the current clock cycle. |

#### Read U32 FIFO.vi

Reads data from a 32-bit FIFO. This VI is a wrapper around the LabVIEW FPGA FIFO Read
 method, and exposes handshaking signals to control when data is read from the
 FIFO.

[IMAGE alt='image' src='GUID-F159462F-6C59-4D0A-A022-42570B428755-a5.gif']

| Input parameters |
| --- |
| FIFO—Specifies the reference to the FIFO from which to read data. Configure the FIFO to use the U32 datatype. Ready for output—Specifies whether the consumer of the data read from the FIFO is ready to accept new data. If you set this parameter to TRUE, the consumer is ready to accept new data and this VI is allowed to read data from the FIFO. If you set this parameter to FALSE, this VI does not return new data. |

| Output parameters |
| --- |
| Output data—Returns the data read from the FIFO. Output valid—Indicates whether the output data read from the FIFO is valid during the current clock cycle. |

#### Read U64 FIFO.vi

Reads data from a 64-bit FIFO. This VI is a wrapper around the LabVIEW FPGA FIFO Read
 method, and exposes handshaking signals to control when data is read from the
 FIFO.

[IMAGE alt='image' src='GUID-6D93D7FB-B275-44CB-BA52-C732C307A00C-a5.gif']

| Input parameters |
| --- |
| FIFO—Specifies the reference to the FIFO from which to read data. Configure the FIFO to use the U64 datatype. Ready for output—Specifies whether the consumer of the data read from the FIFO is ready to accept new data. If you set this parameter to TRUE, the consumer is ready to accept new data and this VI is allowed to read data from the FIFO. If you set this parameter to FALSE, this VI does not return new data. |

| Output parameters |
| --- |
| Output data—Returns the data read from the FIFO. Output valid—Indicates whether the output data read from the FIFO is valid during the current clock cycle. |

#### Read U8 FIFO.vi

Reads data from an 8-bit FIFO. The VI is a wrapper around the LabVIEW FPGA FIFO Read
 method, and exposes handshaking signals to control when data is read from the
 FIFO.

[IMAGE alt='image' src='GUID-B4B63D7B-1547-4C1D-B815-E7D2C1A83989-a5.gif']

| Input parameters |
| --- |
| FIFO—Specifies the reference to the FIFO from which to read data. Configure the FIFO to use the U8 datatype. Ready for output—Specifies whether the consumer of the data read from the FIFO is ready to accept new data. If you set this parameter to TRUE, the consumer is ready to accept new data and this VI is allowed to read data from the FIFO. If you set this parameter to FALSE, this VI does not return new data. |

| Output parameters |
| --- |
| Output data—Returns the data read from the FIFO. Output valid—Indicates whether the output data read from the FIFO is valid during the current clock cycle. |

#### Write U128 FIFO.vi

Writes data to a 128-bit FIFO. This VI is a wrapper around the LabVIEW FPGA FIFO
 Write method, and exposes handshaking signals that inform the user when the FIFO is
 ready to accept new data.

[IMAGE alt='image' src='GUID-A5C217EB-4704-4C95-8758-5C2BC68F1BA5-a5.gif']

| Input parameters |
| --- |
| Input data—Specifies the data to write to the FIFO. Input data.high—Specifies the higher 64-bits of the data to write to the FIFO. Input data.low—Specifies the lower 64-bits of the data to be write to the FIFO. Reset—Resets the handshaking logic directly in front of the LabVIEW FPGA FIFO Write method. This parameter does not reset the entire FIFO. To reset the entire FIFO, assert the reset signal, and call the LabVIEW FPGA FIFO Clear method. No data is written to the FIFO if this parameter is set to TRUE. FIFO—Specifies the reference to the FIFO to which data must be written. Configure the FIFO to use a 128-bit data type. Use the following typedef of this library to configure the FIFO's data type: <instr.lib>\\_niInstr\\Basic Elements\\v1\\FPGA\\Public\\U128.ctl. Input valid—Specifies whether the input data parameter written to the FIFO is valid during the current clock cycle. The input data is written to the FIFO only if it is valid. |

| Output parameters |
| --- |
| Ready for input—Indicates whether this VI is ready to write new data to the FIFO in the next clock cycle. |

#### Write U16 FIFO.vi

Writes data to a 16-bit FIFO. This VI is a wrapper around the LabVIEW FPGA FIFO Write
 method, and exposes handshaking signals that inform the user when the FIFO is ready
 to accept new data.

[IMAGE alt='image' src='GUID-7C09CB0D-DD21-456A-B0FE-DE26B355E644-a5.gif']

| Input parameters |
| --- |
| Input data—Specifies the data to write to the FIFO. Reset—Resets the handshaking logic directly in front of the LabVIEW FPGA FIFO Write method. This parameter does not reset the entire FIFO. To reset the entire FIFO, assert the reset signal, and call the LabVIEW FPGA FIFO Clear method. No data is written to the FIFO if this parameter is set to TRUE. FIFO—Specifies the reference to the FIFO to which data must be written. Configure the FIFO to use the U16 datatype. Input valid—Specifies whether the input data being written to the FIFO is valid during the current clock cycle. The input data is written to the FIFO only if it is valid. |

| Output parameters |
| --- |
| Ready for input—Indicates whether this VI is ready to write new data to the FIFO in the next clock cycle. |

#### Write U32 FIFO.vi

Writes data to a 32-bit FIFO. This VI is a wrapper around the LabVIEW FPGA FIFO Write
 method and exposes handshaking signals that inform the user when the FIFO is ready
 to accept new data.

[IMAGE alt='image' src='GUID-01A704E7-AD64-4B90-8D5D-080BF3B457A2-a5.gif']

| Input parameters |
| --- |
| Input data—Specifies the data to be written to the FIFO. Reset—Resets the handshaking logic directly in front of the LabVIEW FPGA FIFO Write method. This parameter does not reset the entire FIFO. To reset the entire FIFO, assert the reset signal, and call the LabVIEW FPGA FIFO Clear method. No data is written to the FIFO if this parameter is set to TRUE. FIFO—Specifies the reference to the FIFO to which data must be written. Configure the FIFO to use the U32 datatype. Input valid—Specifies whether the input data parameter written to the FIFO is valid during the current clock cycle. The input data is written to the FIFO only if it is valid. |

| Output parameters |
| --- |
| Ready for input—Indicates whether this VI is ready to write new data to the FIFO in the next clock cycle. |

#### Write U64 FIFO.vi

Writes data to a 64-bit FIFO. This VI is a wrapper around the LabVIEW FPGA FIFO Write
 method and exposes handshaking signals that inform the user when the FIFO is ready
 to accept new data.

[IMAGE alt='image' src='GUID-EE0AB64C-3C4D-4F44-A011-0AA5968184FC-a5.gif']

| Input parameters |
| --- |
| Input data—Specifies the data to be written to the FIFO. Reset—Resets the handshaking logic directly in front of the LabVIEW FPGA FIFO Write method. This parameter does not reset the entire FIFO. To do so, assert the reset signal and call the LabVIEW FPGA FIFO Clear method. No data is written to the FIFO if this parameter is set to TRUE. FIFO—Specifies the reference to the FIFO to which data must be written. Configure the FIFO to use the U64 datatype. Input valid—Specifies whether the input data parameter written to the FIFO is valid during the current clock cycle. The input data is written to the FIFO only if it is valid. |

| Output parameters |
| --- |
| Ready for input—Indicates whether this VI is ready to write new data to the FIFO in the next clock cycle. |

#### Write U8 FIFO.vi

Writes data to an 8-bit FIFO. This VI is a wrapper around the LabVIEW FPGA FIFO Write
 method, and exposes handshaking signals that inform the user when the FIFO is ready
 to accept new data.

[IMAGE alt='image' src='GUID-1E42797E-2AEE-4517-B52F-6870F251661A-a5.gif']

| Input parameters |
| --- |
| Input data—Specifies the data to be written to the FIFO. Reset—Resets the handshaking logic directly in front of the LabVIEW FPGA FIFO Write method. This parameter does not reset the entire FIFO. To reset the entire FIFO, the reset signal must be asserted and the LabVIEW FPGA FIFO Clear method should be called. No data is written to the FIFO if this parameter is set to TRUE. FIFO—Specifies the reference to the FIFO to which data must be written. The FIFO should be configured to use the U8 datatype. Input valid—Specifies whether the input data parameter written to the FIFO is valid during the current clock cycle. The input data is written to the FIFO only if it is valid. |

| Output parameters |
| --- |
| Ready for input—Indicates whether this VI is ready to write new data to the FIFO in the next clock cycle. |

#### Read FIFO.vi

Reads data from a FIFO. This VI is a wrapper around the LabVIEW FPGA FIFO Read
 method, and exposes handshaking signals to control when data is read from the
 FIFO.

[IMAGE alt='image' src='GUID-6943F58C-9C67-4EAD-BFAE-873D1F6CF299-a5.gif']

#### Write FIFO.vi

Writes data to a FIFO. This VI is a wrapper around the LabVIEW FPGA FIFO Write
 method, and exposes handshaking signals that inform the user when the FIFO is ready
 to accept new data.

[IMAGE alt='image' src='GUID-9787B497-D019-456F-9CF0-47C7FFBCA0A4-a5.gif']

Parent topic:

Basic Elements Overview

<!--NI_TOPIC bundle=ni-reconfigurable-oscilloscopes path=basic-elements-overview.html language=enus -->
## TOPIC 00007: Basic Elements Overview

- bundle_id: `ni-reconfigurable-oscilloscopes`
- source_path: `basic-elements-overview.html`
- source_url: https://docs-be.ni.com/bundle/ni-reconfigurable-oscilloscopes/raw/resource/enus/basic-elements-overview.html
- document_id: `ni-reconfigurable-oscilloscopes`
- page_type: `leaf`
- content_type: `concept`
- source_description: This instrument design library contains several low-level elements, such as edge detectors, latches, and FIFOs. Using this library can be beneficial when developing new FPGA logic for your software-designed instrument. These basic elements are used in other instrument design libraries and the samp

### Basic Elements Overview

This instrument design library contains several low-level elements, such as edge detectors,
 latches, and FIFOs.  Using this library can be beneficial when developing new FPGA logic
 for your software-designed instrument.  These basic elements are used in other
 instrument design libraries and the sample projects for your device.

Parent topic:

LabVIEW Instrument Design Libraries for Reconfigurable Oscilloscopes

<!--NI_TOPIC bundle=ni-reconfigurable-oscilloscopes path=calibration-api-host-vis.html language=enus -->
## TOPIC 00008: Calibration API Host VIs

- bundle_id: `ni-reconfigurable-oscilloscopes`
- source_path: `calibration-api-host-vis.html`
- source_url: https://docs-be.ni.com/bundle/ni-reconfigurable-oscilloscopes/raw/resource/enus/calibration-api-host-vis.html
- document_id: `ni-reconfigurable-oscilloscopes`
- page_type: `leaf`
- content_type: `concept`
- source_description: Self-Calibrate.vi Runs self-calibration procedures for the specified device. This VI returns an error if you specify a device that is not supported by this calibration API. This VI also downloads the calibration bitstream to the device FPGA if it is not already present. Input parameters Device in Id

### Calibration API Host VIs

#### Self-Calibrate.vi

Runs self-calibration procedures for the specified device. This VI returns an error
 if you specify a device that is not supported by this calibration API. This VI also
 downloads the calibration bitstream to the device FPGA if it is not already
 present.

[IMAGE alt='image' src='GUID-43D4E255-9FE4-4297-B320-D053928793C8-a5.gif']

| Input parameters |
| --- |
| Device in—Identifies the device to self-calibrate. Error in—Describes error conditions that occur before this node runs. This input provides standard error in functionality. |

| Output parameters |
| --- |
| Device out—Passes a reference to the device to the next VI. Error out—Contains error information. This output provides standard error out functionality. |

#### Open Ext Cal Session.vi

Opens an external calibration session for the specified device. This VI returns an
 error if you specify a device that is not supported by this calibration API. This VI
 also downloads the calibration bitstream to the device FPGA if it is not already
 present.

[IMAGE alt='image' src='GUID-8F9F8D38-748B-4D07-AA76-3C8279057C44-a5.gif']

| Input parameters |
| --- |
| Device in—Identifies the device to perform external calibration on. Calibration password—The calibration password for the device. This password is required to perform external calibration, set the calibration due date, or set the date and time of verification. By default, this password is "NI". Error in—Describes error conditions that occur before this node runs. This input provides standard error in functionality. |

| Output parameters |
| --- |
| External cal session—Returns a new external calibration session reference for the device specified by device in. Use this reference as an input to other external calibration VIs in this library. Error out—Contains error information. This output provides standard error out functionality. |

#### Close Ext Cal Session.vi

Closes the specified external calibration session. You can choose to commit the
 results of this calibration session, or you can choose to disregard them.

[IMAGE alt='image' src='GUID-756526C4-717B-4BE2-A247-E7F992C4144D-a5.gif']

| Input parameters |
| --- |
| External cal session—The external calibration session to close. Action—Specifies what to do with the results of the external calibration session. Cancel (default)—Do not commit calibration results to the device. Commit—Commit calibration results to the device. Error in—Describes error conditions that occur before this node runs. This input provides standard error in functionality. |

| Output parameters |
| --- |
| Error out—Contains error information. This output provides standard error out functionality. |

#### DC Cal Initialize.vi

Initializes an external calibration session for a DC calibration step. You must
 specify which channel to calibrate. The DC Cal Configure and DC Cal Adjust VIs will
 use this channel. This VI performs any initial configuration steps, such as
 configuring clocks.

You can perform DC calibration on multiple channels using
 the same external calibration session. When you have successfully completed DC
 calibration on a channel, you can run this VI again with a different channel input
 to start the DC calibration sequence for another channel.

[IMAGE alt='image' src='GUID-2FBF1C8C-829D-482E-8866-F716AB74E767-a5.gif']

| Input parameters |
| --- |
| External cal session in—Identifies your session. This parameter is obtained from the Open Ext Cal Session VI of this library. Channel—Identifies the input channel to perform DC calibration on. Error in—Describes error conditions that occur before this node runs. This input provides standard error in functionality. |

| Output parameters |
| --- |
| External cal session out—Passes a reference to your session to the next VI. Error out—Contains error information. This output provides standard error out functionality. |

#### DC Cal Configure.vi

Configures the device for an iteration of the DC calibration step. This VI returns
 the DC voltage that you should apply to the channel being calibrated, as well as the
 current input impedance setting of the channel. Run this VI after running the DC Cal
 Initialize VI of this library.

[IMAGE alt='image' src='GUID-EC022919-D1A8-48F6-8103-1BF94A75E50D-a5.gif']

| Input parameters |
| --- |
| External cal session in—Identifies your session. This parameter is obtained from the Open Ext Cal Session VI of this library. Error in—Describes error conditions that occur before this node runs. This input provides standard error in functionality. |

| Output parameters |
| --- |
| External cal session out—Passes a reference to your session to the next VI. Voltage to generate (V)—Specifies the DC voltage to apply to the channel being calibrated. You should configure your external DC calibration source to provide this voltage. Input impedance—Returns the current input impedance setting of the channel being calibrated. Error out—Contains error information. This output provides standard error out functionality. |

#### DC Cal Adjust.vi

Measures the input voltage on a channel, compares it with the actual voltage
 generated, performs any required adjustments, and computes any calibration
 coefficients to store in the device's persistent calibration data storage. This VI
 also indicates if DC calibration is complete. Run this VI after running the
 DC Cal Initialize and DC Cal Configure VIs
 in this library.

You should continue running the DC Cal
 Configure VI and then running this VI until DC cal complete returns
 TRUE or until an error occurs.

[IMAGE alt='image' src='GUID-AEF31F81-9643-4721-ACCB-55BF92ED47E2-a5.gif']

| Input parameters |
| --- |
| External cal session in—Identifies your session. This parameter is obtained from the Open Ext Cal Session VI of this library. Actual voltage generated (V)—Specifies the actual voltage applied to the channel being calibrated. If you are calibrating the device using an inexpensive DC source in combination with a DMM, the DMM will measure the actual DC voltage input, which may vary from the voltage setting on the DC source. This value can vary slightly from the requested voltage to generate without causing an error. If the two values are too far apart, however, this VI will return an error. Error in—Describes error conditions that occur before this node runs. This input provides standard error in functionality. |

| Output parameters |
| --- |
| External cal session out—Passes a reference to your session to the next VI. DC cal complete—Returns TRUE when the DC calibration procedure is complete for this channel. You can then either initialize a new procedure or close the external calibration session. Error out—Contains error information. This output provides standard error out functionality. |

#### Timebase Cal Initialize.vi

Initializes an external calibration session for a timebase calibration step. You must
 specify which channel to calibrate. The Timebase Cal Configure
 and Timebase Cal Adjust VIs will use this channel. This VI
 performs any initial configuration steps, such as configuring clocks.

[IMAGE alt='image' src='GUID-303FFE26-96AC-468B-8141-513C36D0CC6D-a5.gif']

| Input parameters |
| --- |
| External cal session in—Identifies your session. This parameter is obtained from the Open Ext Cal Session VI of this library. Channel—Identifies the input channel to perform DC calibration on. Normally, you only need to perform timebase calibration on one channel. Error in—Describes error conditions that occur before this node runs. This input provides standard error in functionality. |

| Output parameters |
| --- |
| External cal session out—Passes a reference to your session to the next VI. Error out—Contains error information. This output provides standard error out functionality. |

#### Timebase Cal Configure.vi

Configures the device for an iteration of the timebase calibration step. This VI
 returns the frequency of a 1 V peak-to-peak sine wave that you should apply to the
 channel being calibrated. Run this VI after running the Timebase Cal
 Initialize VI of this library.

[IMAGE alt='image' src='GUID-99974ECE-9286-4467-A3A7-F19FE0BC0878-a5.gif']

| Input parameters |
| --- |
| External cal session in—Identifies your session. This parameter is obtained from the Open Ext Cal Session VI of this library. Error in—Describes error conditions that occur before this node runs. This input provides standard error in functionality. |

| Output parameters |
| --- |
| External cal session out—Passes a reference to your session to the next VI. Frequency to generate (Hz)—Specifies the frequency of the 1 V peak-to-peak sine wave to apply to the channel being calibrated. You should configure your external timebase calibration source to provide this frequency. Error out—Contains error information. This output provides standard error out functionality. |

#### Timebase Cal Adjust.vi

Measures the input frequency on a channel, compares it to the actual frequency
 generated, performs any required adjustments, and computes any calibration constants
 to store in persistent calibration data storage on the device. This VI also
 indicates if timebase calibration is complete. Run this VI after running the
 DC Cal Initialize and DC Cal Configure VIs
 in this library.

You should continue running the Timebase Cal
 Configure VI and then running this VI until timebase cal complete
 returns TRUE or until an error occurs.

[IMAGE alt='image' src='GUID-4EB83A71-8C78-458A-94CB-13BDB7BE5337-a5.gif']

| Input parameters |
| --- |
| External cal session in—Identifies your session. This parameter is obtained from the Open Ext Cal Session VI of this library. Actual frequency generated (Hz)—Specifies the actual frequency of the 1 V peak-to-peak sine wave applied to the channel input. If you are using an inexpensive frequency source in combination with a calibrated DMM to calibrate the device, this value should indicate the frequency that the DMM measured at the channel. This value may vary slightly from the requested frequency to generate without causing an error. If the two values are too far apart, however, this VI will return an error. Error in—Describes error conditions that occur before this node runs. This input provides standard error in functionality. |

| Output parameters |
| --- |
| External cal session out—Passes a reference to your session to the next VI. Timebase cal complete—Returns TRUE when the timebase calibration procedure is complete for this channel. You can then either initialize a new procedure or close the external calibration session. Error out—Contains error information. This output provides standard error out functionality. |

#### Set Misc Info.vi

Stores custom text information. After running this VI, you can retrieve this
 information using the Get Misc Info VI. The information is stored
 until you close the current calibration session. When you close the calibration
 session, you can choose to commit this information to the device. Committing this
 information to the device allows you to access it from within subsequent calibration
 sessions.

[IMAGE alt='image' src='GUID-27F37151-85A3-45B1-B8F3-A11BDDD7496A-a5.gif']

| Input parameters |
| --- |
| External cal session in—Identifies your session. This parameter is obtained from the Open Ext Cal Session VI of this library. Miscellaneous information—The text information to store. Error in—Describes error conditions that occur before this node runs. This input provides standard error in functionality. |

| Output parameters |
| --- |
| External cal session out—Passes a reference to your session to the next VI. Error out—Contains error information. This output provides standard error out functionality. |

#### Get Misc Info.vi

Returns the text information set by the Set Misc Info VI of this
 library. If you have not yet run the Set Misc Info VI during this
 calibration session, this VI will return the miscellaneous information that was last
 committed to the device.

[IMAGE alt='image' src='GUID-E5E06828-E874-46DE-BA8B-AD32D7BA1EC6-a5.gif']

| Input parameters |
| --- |
| External cal session in—Identifies your session. This parameter is obtained from the Open Ext Cal Session VI of this library. Error in—Describes error conditions that occur before this node runs. This input provides standard error in functionality. |

| Output parameters |
| --- |
| External cal session out—Passes a reference to your session to the next VI. Miscellaneous information—Returns the text information. Error out—Contains error information. This output provides standard error out functionality. |

#### Get Calibration Date and Time.vi

Returns the date and time of the last external calibration verification or
 self-calibration for a specified device.

[IMAGE alt='image' src='GUID-4C614467-97DF-4288-9F65-F0D7CEFCA347-a5.gif']

| Input parameters |
| --- |
| Device in—Identifies a device. Type of calibration—Specifies the type of calibration that the calibration date output will return a date and time for. Self -Calibration—Returns the date and time of the last self-calibration. External Calibration Verification—Returns the date and time of the last external calibration verification. Error in—Describes error conditions that occur before this node runs. This input provides standard error in functionality. |

| Output parameters |
| --- |
| Device out—Passes a reference to the device to the next VI. Calibration date—Returns the date and time that the requested calibration type was last performed. Error out—Contains error information. This output provides standard error out functionality. |

#### Get Self Cal Temp.vi

Returns the temperature of the device that was measured during the last
 self-calibration.

[IMAGE alt='image' src='GUID-FCB723B5-269E-4F8A-ADAC-125A71F7798A-a5.gif']

| Input parameters |
| --- |
| Device in—Identifies a device. Error in—Describes error conditions that occur before this node runs. This input provides standard error in functionality. |

| Output parameters |
| --- |
| Device out—Passes a reference to the device to the next VI. Temperature—Returns the device temperature, in degrees Celsius, measured during the last self-calibration. Error out—Contains error information. This output provides standard error out functionality. |

#### Get Device Temp.vi

Returns the current device temperature.

[IMAGE alt='image' src='GUID-976B8778-3607-4F4C-8B2D-4ED888E7E57A-a5.gif']

| Input parameters |
| --- |
| Device in—Identifies a device. Error in—Describes error conditions that occur before this node runs. This input provides standard error in functionality. |

| Output parameters |
| --- |
| Device out—Passes a reference to the device to the next VI. Temperature—Returns the temperature measurement. Error out—Contains error information. This output provides standard error out functionality. |

#### Change Calibration Password.vi

Changes the external calibration password for a device. This password is required to
 perform external calibration. By default, this password is "NI".

[IMAGE alt='image' src='GUID-785B510B-2496-48EC-A760-9ABBC8FE254E-a5.gif']

| Input parameters |
| --- |
| Device in—Identifies a device. Old password—The current calibration password for the device. New password—Specifies a new calibration password. Error in—Describes error conditions that occur before this node runs. This input provides standard error in functionality. |

| Output parameters |
| --- |
| Device out—Passes a reference to the device to the next VI. Error out—Contains error information. This output provides standard error out functionality. |

#### Get Calibration Recommended Interval.vi

Returns the recommended external calibration interval for a specified device.

[IMAGE alt='image' src='GUID-D959BDF5-2B44-42BF-8C21-D24772D6251F-a5.gif']

| Input parameters |
| --- |
| Device in—Identifies a device. Error in—Describes error conditions that occur before this node runs. This input provides standard error in functionality. |

| Output parameters |
| --- |
| Device out—Passes a reference to the device to the next VI. Cal interval (months)—The recommended external calibration interval. Error out—Contains error information. This output provides standard error out functionality. |

#### Get Calibration Due Date.vi

Returns the current external calibration due date for a specified device.

[IMAGE alt='image' src='GUID-BA8A708F-D7D6-4433-9ECB-2AA426D35963-a5.gif']

| Input parameters |
| --- |
| Device in—Identifies a device. Error in—Describes error conditions that occur before this node runs. This input provides standard error in functionality. |

| Output parameters |
| --- |
| Device out—Passes a reference to the device to the next VI. External cal due date—The date by which external calibration should be performed. Error out—Contains error information. This output provides standard error out functionality. |

#### Set Verification Date and Time.vi

Sets the date and time of the last external calibration verification for a specified
 device.

[IMAGE alt='image' src='GUID-F82B178B-C62C-4333-A4AC-0587A7B6DB33-a5.gif']

| Input parameters |
| --- |
| Device in—Identifies a device. Calibration password—The calibration password for the device. This password is required to perform external calibration, set the calibration due date, or set the date and time of verification. By default, this password is "NI". Verification date—Specifies the date and time that external calibration verification was last performed for the device. Error in—Describes error conditions that occur before this node runs. This input provides standard error in functionality. |

| Output parameters |
| --- |
| Device out—Passes a reference to the device to the next VI. Error out—Contains error information. This output provides standard error out functionality. |

#### Set Calibration Due Date.vi

Sets a custom due date for the next external calibration verification for a specified
 device.

[IMAGE alt='image' src='GUID-DE4882F1-2C0B-4BCB-A75F-123E892D3A63-a5.gif']

| Input parameters |
| --- |
| Device in—Identifies a device. Calibration password—The calibration password for the device. This password is required to perform external calibration, set the calibration due date, or set the date and time of verification. By default, this password is "NI". External cal due date—Specifies the new external calibration due date. Error in—Describes error conditions that occur before this node runs. This input provides standard error in functionality. |

| Output parameters |
| --- |
| Device out—Passes a reference to the device to the next VI. Error out—Contains error information. This output provides standard error out functionality. |

#### Get Self Cal Supported.vi

Checks to see if a specified device supports self-calibration.

[IMAGE alt='image' src='GUID-1BAD99BA-3C6C-437D-A527-8EF44FF463FC-a5.gif']

| Input parameters |
| --- |
| Device in—Identifies a device. Error in—Describes error conditions that occur before this node runs. This input provides standard error in functionality. |

| Output parameters |
| --- |
| Device out—Passes a reference to the device to the next VI. Self cal supported—Returns TRUE if the device supports self-calibration, and FALSE if it does not. Error out—Contains error information. This output provides standard error out functionality. |

Parent topic:

Calibration API Overview

<!--NI_TOPIC bundle=ni-reconfigurable-oscilloscopes path=calibration-api-overview.html language=enus -->
## TOPIC 00009: Calibration API Overview

- bundle_id: `ni-reconfigurable-oscilloscopes`
- source_path: `calibration-api-overview.html`
- source_url: https://docs-be.ni.com/bundle/ni-reconfigurable-oscilloscopes/raw/resource/enus/calibration-api-overview.html
- document_id: `ni-reconfigurable-oscilloscopes`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the Calibration API to perform calibration procedures on your device. To learn more about using this API in calibration, refer to the Calibration Procedure document for your device.The Calibration API includes utilities to read and write additional calibration information: Self-calibration date/

### Calibration API Overview

Use the Calibration API to perform calibration procedures on your device. To learn more about
 using this API in calibration, refer to the *Calibration
 Procedure* document for your device.

The Calibration API includes utilities to read and write additional calibration information:

- Self-calibration date/time.
- External calibration verification date/time.
- Self-calibration temperature.
- Current device temperature.
- External calibration due date.
- Recommended calibration interval.

These information functions are also available through NI MAX and the NI System Configuration
 API.

Parent topic:

LabVIEW Instrument Design Libraries for Reconfigurable Oscilloscopes

<!--NI_TOPIC bundle=ni-reconfigurable-oscilloscopes path=calibration-data-host-vis.html language=enus -->
## TOPIC 00010: Calibration Data Host VIs

- bundle_id: `ni-reconfigurable-oscilloscopes`
- source_path: `calibration-data-host-vis.html`
- source_url: https://docs-be.ni.com/bundle/ni-reconfigurable-oscilloscopes/raw/resource/enus/calibration-data-host-vis.html
- document_id: `ni-reconfigurable-oscilloscopes`
- page_type: `leaf`
- content_type: `concept`
- source_description: Open Session.vi Reads calibration data from the device and creates a Calibration Data session to allow you to access this data. Input parameters FPGA reference Specifies a reference to the FPGA target to read calibration data from. Error in Describes error conditions that occur before this node runs

### Calibration Data Host VIs

#### Open Session.vi

Reads calibration data from the device and creates a Calibration
 Data session to allow you to access this data.

[IMAGE alt='image' src='GUID-08ADC23A-0116-43BD-A161-F14643DBF944-a5.gif']

| Input parameters |
| --- |
| FPGA reference—Specifies a reference to the FPGA target to read calibration data from. Error in—Describes error conditions that occur before this node runs. This input provides standard error in functionality. Emulation model name—Specifies the model to emulate, if the FPGA reference is opened in a simulated or emulated context. |

| Output parameters |
| --- |
| Session out—Passes a reference to your session to the next VI. Session out is obtained from the Open Session VI of the Configuration library. Error out—Contains error information. This output provides standard error out functionality. |

#### Close Session.vi

Closes a specified Calibration Data session, releases resources
 used by the session, and deallocates memory used by the session.

[IMAGE alt='image' src='GUID-6B7D1F1E-9072-426E-A87C-59D1ECA45E83-a5.gif']

| Input parameters |
| --- |
| Calibration data in—Identifies the Calibration Data session to close. Error in—Describes error conditions that occur before this node runs. This input provides standard error in functionality. |

| Output parameters |
| --- |
| Error out—Contains error information. This output provides standard error out functionality. |

Parent topic:

Calibration Data Overview

<!--NI_TOPIC bundle=ni-reconfigurable-oscilloscopes path=calibration-data-overview.html language=enus -->
## TOPIC 00011: Calibration Data Overview

- bundle_id: `ni-reconfigurable-oscilloscopes`
- source_path: `calibration-data-overview.html`
- source_url: https://docs-be.ni.com/bundle/ni-reconfigurable-oscilloscopes/raw/resource/enus/calibration-data-overview.html
- document_id: `ni-reconfigurable-oscilloscopes`
- page_type: `leaf`
- content_type: `concept`
- source_description: During calibration procedures, calibration data is stored in device nonvolatile memory. Other instrument design libraries depend on the Calibration Data library. Calibration data is required to configure the device or perform synchronization measurements.

### Calibration Data Overview

During calibration procedures, calibration data is stored in device nonvolatile memory. Other
 instrument design libraries depend on the Calibration Data library. Calibration data is
 required to configure the device or perform synchronization measurements.

Parent topic:

LabVIEW Instrument Design Libraries for Reconfigurable Oscilloscopes

<!--NI_TOPIC bundle=ni-reconfigurable-oscilloscopes path=channel-fpga-vis.html language=enus -->
## TOPIC 00012: Channel FPGA VIs

- bundle_id: `ni-reconfigurable-oscilloscopes`
- source_path: `channel-fpga-vis.html`
- source_url: https://docs-be.ni.com/bundle/ni-reconfigurable-oscilloscopes/raw/resource/enus/channel-fpga-vis.html
- document_id: `ni-reconfigurable-oscilloscopes`
- page_type: `leaf`
- content_type: `concept`
- source_description: Select And Interleave.viInterleaves data from specified channels into a single array. This VI can interleave a number of channels equal to a power of 2 (1, 2, 4, ...). Triggers and channel data remain aligned with each other when passed through this VI. Input parameters Data in Specifies the data sa

### Channel FPGA VIs

#### Select And Interleave.vi

Interleaves data
 from specified channels into a single array. This VI can interleave a number of
 channels equal to a power of 2 (1, 2, 4, ...).

Triggers and channel data
 remain aligned with each other when passed through this VI.

[IMAGE alt='image' src='GUID-1F317DED-478A-4329-BAC1-1209FABB91C8-a5.gif']

| Input parameters |
| --- |
| Data in—Specifies the data samples to interleave. Each element in this array contains the data from a single channel Triggers in—Specifies the triggers to pass through the VI. Triggers remain aligned with the data in input data. This VI does not manipulate the triggers in any other way. Input valid—Specifies whether the data in input contains valid data. Channel enable mask—Specifies which channels will be interleaved. Each bit in this value represents a channel, with bit 0 representing channel 0. Number of channels to interleave—Specifies the number of channels to interleave. This value must be a power of 2. Reset—Resets the registers in the output valid path when set to TRUE, allowing for deterministic startup behavior. The registers in the channel out path are not reset. However, the output valid output returns FALSE while the reset input is asserted. |

| Output parameters |
| --- |
| Channel status—Contains information about the internal status of the VI. Channel status.next packed index—Specifies the index in interleaved data out where this VI will place the next data in input sample. Interleaved data out—Contains the interleaved channel data. Triggers out—Contains the trigger information aligned with the interleaved channel data. Sample format out—Contains information about the data in the interleaved data out output. Other VIs may require this information. Output valid —Indicates whether the interleaved data out output contains valid data. This parameter returns TRUE during clock cycles in which interleaved data out contains a valid data sample. Otherwise, this parameter returns FALSE. |

#### Select.vi

Returns the channel of data in
 at channel index. This VI has a pipeline of 1.

[IMAGE alt='image' src='GUID-94CA211C-0FCD-49EC-89F4-45AF0BA6A605-a5.gif']

| Input parameters |
| --- |
| Data in—Specifies the data samples for each channel. Each element in this array contains the data from a single channel. Input valid—Specifies whether the data in input contains valid data. Channel index—Specifies the index of the channel data to output. Each channel in the data in input corresponds to an index, starting with index 0. Reset—Resets the registers in the output valid path when set to TRUE, allowing for deterministic startup behavior. The registers in the channel out path are not reset. However, the output valid output returns FALSE while the reset input is asserted. |

| Output parameters |
| --- |
| Channel out—Returns the channel data specified by the channel index input. Output valid —Indicates whether the channel out parameter contains valid data. This parameter returns TRUE during clock cycles in which the channel out output contains a valid data sample. Otherwise, this parameter returns FALSE. |

Parent topic:

Channel Overview

<!--NI_TOPIC bundle=ni-reconfigurable-oscilloscopes path=channel-overview.html language=enus -->
## TOPIC 00013: Channel Overview

- bundle_id: `ni-reconfigurable-oscilloscopes`
- source_path: `channel-overview.html`
- source_url: https://docs-be.ni.com/bundle/ni-reconfigurable-oscilloscopes/raw/resource/enus/channel-overview.html
- document_id: `ni-reconfigurable-oscilloscopes`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use this instrument design library to manipulate channel data for use by other instrument design libraries or LabVIEW FPGA primitives. This library contains IP for interleaving channel waveforms into a single array. You can use this library to dynamically choose which channels to interleave while al

### Channel Overview

Use this instrument design library to manipulate channel data for use by other instrument design
 libraries or LabVIEW FPGA primitives. This library contains IP for interleaving channel
 waveforms into a single array. You can use this library to dynamically choose which
 channels to interleave while also maintaining a constant output array size.

This instrument design library is particularly useful when used with the Multirecord Acquisition
 instrument design library for dynamically selecting the channels to be stored into
 memory. The library can also be used to stream a single array of interleaved data.

This library supports variations in data type, number of channels, and samples per cycle.

Parent topic:

LabVIEW Instrument Design Libraries for Reconfigurable Oscilloscopes

Related concepts:

- Multirecord Acquisition Overview

<!--NI_TOPIC bundle=ni-reconfigurable-oscilloscopes path=color-coding.html language=enus -->
## TOPIC 00014: Color Coding

- bundle_id: `ni-reconfigurable-oscilloscopes`
- source_path: `color-coding.html`
- source_url: https://docs-be.ni.com/bundle/ni-reconfigurable-oscilloscopes/raw/resource/enus/color-coding.html
- document_id: `ni-reconfigurable-oscilloscopes`
- page_type: `leaf`
- content_type: `concept`
- source_description: The color information signal C, together with Y, forms the composite video signal is a modulated signal. The modulation type depends on the video format.For all PAL and NTSC formats, the coding is based on the Quadrature Amplitude Modulation (QAM) concept, where two-color components are amplitude mo

### Color Coding

The color information signal C, together with Y, forms the composite video signal is a modulated
 signal. The modulation type depends on the video format.

For all PAL and NTSC formats, the coding is based on the Quadrature Amplitude Modulation (QAM)
 concept, where two-color components are amplitude modulated in
 quadrature and then combined. The modulation must be decoded, so
 to keep track of the absolute phase needed to decode the color
 information, a reference signal, called the color burst, is
 inserted at the beginning of each line, right after the
 horizontal synchronization pulse. The insertion signal is shown
 in the *Complete NTSC Frame Scan* image.

For the SECAM format, the 2-color components are frequency modulated using two different
 subcarrier frequencies and are sequentially distributed on alternated video lines. SECAM
 does not need a color burst signal.

Parent topic:

Video Fundamentals

Related concepts:

- Complete NTSC Frame Scan

<!--NI_TOPIC bundle=ni-reconfigurable-oscilloscopes path=complete-ntsc-frame-scan.html language=enus -->
## TOPIC 00015: Complete NTSC Frame Scan

- bundle_id: `ni-reconfigurable-oscilloscopes`
- source_path: `complete-ntsc-frame-scan.html`
- source_url: https://docs-be.ni.com/bundle/ni-reconfigurable-oscilloscopes/raw/resource/enus/complete-ntsc-frame-scan.html
- document_id: `ni-reconfigurable-oscilloscopes`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the result of scanning all 525 lines that compose a complete NTSC frame.

### Complete NTSC Frame Scan

The following figure shows the result of scanning all 525 lines that compose a complete NTSC
 frame.

[IMAGE alt='image' src='GUID-8C8E4CB6-65EE-4454-BDAC-12E58B8EE869-a5.gif']

Parent topic:

Interlaced Scanning

<!--NI_TOPIC bundle=ni-reconfigurable-oscilloscopes path=composite-and-component-video-signals.html language=enus -->
## TOPIC 00016: Composite and Component Video Signals

- bundle_id: `ni-reconfigurable-oscilloscopes`
- source_path: `composite-and-component-video-signals.html`
- source_url: https://docs-be.ni.com/bundle/ni-reconfigurable-oscilloscopes/raw/resource/enus/composite-and-component-video-signals.html
- document_id: `ni-reconfigurable-oscilloscopes`
- page_type: `leaf`
- content_type: `concept`
- source_description: A composite video signal is a signal in which all the components needed to generate a video signal are embedded in a single signal. The three main components that together form a composite signal are as follows: The luma signal (or luminance) Contains the intensity (brightness or darkness) informati

### Composite and Component Video Signals

A composite video signal is a signal in which all the components needed to generate a video
 signal are embedded in a single signal. The three main components that together form a
 composite signal are as follows:

The luma signal (or luminance)

The chroma signal

The synchronization signal

The monochrome composite signal is built of two components: luma (or luminance) and
 synchronization. This signal, which is usually called the Y signal,
 is shown in the following figure:

[IMAGE alt='image' src='GUID-D0A9D27B-750A-443B-BBBA-4CE4B0E40582-a5.gif']

#### Monochrome Composite Video Signal
 (Luma Steps from White to Black)

The chroma signal by itself, which is usually called the C signal,
 is shown in the following figure:

[IMAGE alt='image' src='GUID-9A2FDCEF-7F12-493B-B5DB-83AA36A533D6-a5.gif']

#### Color Information Signal for a Color
 Bar Line (Including the Color Burst)

The composite color video signal, often called the Color Video, Blank, and Sync
 (CVBS) signal, is the sum of Y and C.

CVBS = Y + C

[IMAGE alt='image' src='GUID-795C3E62-1E14-4EF7-BF4E-D2AF31BE95D5-a5.gif']

#### Color Composite Video Signal for a
 Color Bar Line

The two components Y and C can also be
 distributed separately as two independent signals. These two signals together are
 called either Y/C or S-video.

Y/C = S-video

#### Component Video Signals

A component video
 signal is a signal in which all the color components needed to generate a video
 signal are transmitted separately. Most HDTV formats are component
 (Y-Pb-Pr).

Parent topic:

Video Fundamentals

<!--NI_TOPIC bundle=ni-reconfigurable-oscilloscopes path=configuration-fpga-vis.html language=enus -->
## TOPIC 00017: Configuration FPGA VIs

- bundle_id: `ni-reconfigurable-oscilloscopes`
- source_path: `configuration-fpga-vis.html`
- source_url: https://docs-be.ni.com/bundle/ni-reconfigurable-oscilloscopes/raw/resource/enus/configuration-fpga-vis.html
- document_id: `ni-reconfigurable-oscilloscopes`
- page_type: `leaf`
- content_type: `concept`
- source_description: Create Resources.viInstantiates the internal registers and address spaces used by this Configuration library. Output parameters Config subsystems Specifies the subsystems that were instantiated for this library. Connect this output to the Add Subsystems VI of the Instruction Framework library. This

### Configuration FPGA VIs

#### Create Resources.vi

Instantiates the internal registers and address
 spaces used by this Configuration library.

[IMAGE alt='image' src='GUID-8616E0F3-4550-4DA7-8DD0-6892F7482443-a5.gif']

| Output parameters |
| --- |
| Config subsystems—Specifies the subsystems that were instantiated for this library. Connect this output to the Add Subsystems VI of the Instruction Framework library. This allows you to use a Register Configuration object to access the resources created by this VI. Digital correction resources—Specifies resources for digital correction. Use this parameter as the digital correction resources input for the Digital Correction VI and the Validate Channel Data VI of this library. |

#### Digital Correction (4 Ch).vi

Applies digital correction gain and offset
 coefficients to the input data. If digital correction has been configured, then this
 data is scaled so that its full range corresponds to the vertical range. A
 fixed-point value of -1 corresponds to the low end of the vertical
 range, and a value nearing 1 corresponds to the high end of the vertical
 range.

This VI causes a datapath delay of 4 cycles.

[IMAGE alt='image' src='GUID-F06DE8FD-9790-4C34-8BA2-2A94C2C635C9-a5.gif']

| Input parameters |
| --- |
| Digital correction resources—The register resources that contain the correction coefficients and a cache of the channel enable state. These resources are obtained from the Create Resources VI of this library. Channel data in—Specifies the raw channel data as a cluster of arrays. Each element in the cluster contains samples from a single channel, and each element in each array contains a data sample. Input valid—Specifies whether the data from channel data in is valid. If this parameter is TRUE, output valid will return TRUE for the corresponding channel data output. |

| Output parameters |
| --- |
| Corrected channel data out—Returns channel data with digital correction applied. Output valid—Indicates that the data in corrected channel data out is valid. This parameter returns TRUE only if the input valid parameter for the corresponding channel data was TRUE. |

#### Digital Correction (8 Ch).vi

Applies digital correction gain and offset
 coefficients to the input data. If the digital correction coefficients have been
 written to the config resources, then the resulting corrected data will be scaled so
 that the full range of the fixed-point data type corresponds to the nominal vertical
 range.

This VI causes a datapath delay of 4 cycles.

[IMAGE alt='image' src='GUID-AA65B88F-35CF-424D-9974-DB6D9170C173-a5.gif']

| Input parameters |
| --- |
| Digital correction resources—The register resources that contain the correction coefficients and a cache of the channel enable state. These resources are obtained from the Create Resources VI of this library. Channel data in—Specifies the raw channel data as a cluster of arrays. Each element in the cluster contains samples from a single channel, and each element in each array contains a data sample. Input valid—Specifies whether the data from channel data in is valid. If this parameter is TRUE, output valid will return TRUE for the corresponding channel data output. |

| Output parameters |
| --- |
| Corrected channel data out—Returns channel data with digital correction applied. Output valid—Indicates that the data in corrected channel data out is valid. This parameter returns TRUE only if the input valid parameter for the corresponding channel data was TRUE. |

#### Validate 4 Channel Data.vi

output valid indicates that the data in
 corrected channel data out is valid. This parameter returns TRUE
 only if the input valid parameter for the corresponding channel data was
 TRUE.

Verifies that the channel data is valid for the
 expected channels. This VI compares the channel data valid input array against an
 internal register that tracks which channels are enabled. If the channel data valid
 value for any enabled channel I FALSE, then the expected data is
 not valid.

[IMAGE alt='image' src='GUID-E869FAAB-484F-4B9F-ABE7-AD793FDFD831-a5.gif']

| Input parameters |
| --- |
| Digital correction resources—The register resources that contain the correction coefficients and a cache of the channel enable state. These resources are obtained from the Create Resources VI of this library. Channel data valid—Specifies whether or not the data from multiple channels is valid. Each element in this boolean array represents a channel. A channel's element is TRUE if the data from that channel is valid, and FALSE if the data from that channel is invalid. Use the channel data valid I/O Node to generate this array. |

| Output parameters |
| --- |
| Expected data valid—Indicates that data from the expected enabled channels is valid. If a channel is enabled but its channel data valid value is FALSE, this parameter returns FALSE. |

#### Validate 8 Channel Data.vi

Verifies that the channel data is valid for
 the expected channels. This VI compares the channel data valid input array against
 an internal register that tracks which channels are enabled. If the channel data
 valid value for any enabled channel is FALSE, then the expected
 data is not valid.

[IMAGE alt='image' src='GUID-253A8A87-5DA5-48F4-A723-44349C14BD0B-a5.gif']

| Input parameters |
| --- |
| Digital correction resources—The register resources that contain the correction coefficients and a cache of the channel enable state. These resources are obtained from the Create Resources VI of this library. Channel data valid—Specifies whether or not the data from multiple channels is valid. Each element in this boolean array represents a channel. A channel's element is TRUE if the data from that channel is valid, and FALSE if the data from that channel is invalid. Use the channel data valid I/O Node to generate this array. |

| Output parameters |
| --- |
| Expected data valid—Indicates that data from the expected enabled channels is valid. If a channel is enabled but its channel data valid value is FALSE, this parameter returns FALSE. |

Parent topic:

Configuration Overview

<!--NI_TOPIC bundle=ni-reconfigurable-oscilloscopes path=configuration-host-vis.html language=enus -->
## TOPIC 00018: Configuration Host VIs

- bundle_id: `ni-reconfigurable-oscilloscopes`
- source_path: `configuration-host-vis.html`
- source_url: https://docs-be.ni.com/bundle/ni-reconfigurable-oscilloscopes/raw/resource/enus/configuration-host-vis.html
- document_id: `ni-reconfigurable-oscilloscopes`
- page_type: `leaf`
- content_type: `concept`
- source_description: Open Session.viOpens the instrument I/O session. Input parameters Register bus in Specifies an instruction target that interfaces to read and write registers to the device. FPGA interface in Specifies a LV FPGA interface wire to communicate with the FPGA and board driver. Subsystem map in Indicates

### Configuration Host VIs

#### Open
 Session.vi

Opens the instrument I/O session.

[IMAGE alt='image' src='GUID-BF9F5AE3-8AEF-496A-8D9B-2F80B1E77F2B-a5.gif']

| Input parameters |
| --- |
| Register bus in—Specifies an instruction target that interfaces to read and write registers to the device. FPGA interface in—Specifies a LV FPGA interface wire to communicate with the FPGA and board driver. Subsystem map in—Indicates the location for the instruction framework. Calibration data in—Specifies calibration data provided to the Configuration library. Emulation model name—Specifies a device to emulate, if emulation is enabled. Error in—Describes error conditions that occur before this node runs. This input provides standard error in functionality. |

| Output parameters |
| --- |
| Session out—Passes a reference to your session to the next VI. session out is obtained from the Open Session VI of this library. Error out—Contains error information. This output provides standard error out functionality. |

#### Configure ADC Clock.vi

Configures the device ADC to use either an onboard
 clock or an external clock.

[IMAGE alt='image' src='GUID-D322118A-FDA8-42E4-8B4A-A5C8FE1665BA-a5.gif']

| Input parameters |
| --- |
| Session in—Identifies your session. Session in is obtained from the Open Session VI of this library. Clock type—Specifies the type of clock for the device to use. Onboard—Specifies an onboard clock. External—Specifies an external clock. Reference clock source—Specifies the source of the reference clock used to generate the onboard ADC clock. None (default)—Specifies that no reference clock will be used. Clock in—Specifies that the clock source is the clock in connector on the device front panel. PXI clock—Specifies that the clock source is the clock signal from the PXI chassis. Reference clock rate (Hz)—Specifies the input reference clock rate if the reference clock source is clock in. This parameter is ignored if the reference clock source is None or PXI clock. External clock source—Specifies the source of the external clock that is divided to become the ADC clock. Clock in (default)—Specifies that the clock source is the clock in signal from the device front panel. PXIe DStar A—Specifies that the clock source is the signal from the PXIe DStar A line. External clock rate (Hz)—Specifies the frequency of the source of the ADC clock. The default value is 0. Error in—Describes error conditions that occur before this node runs. This input provides standard error in functionality. |

| Output parameters |
| --- |
| Session out—Passes a reference to your session to the next VI. session out is obtained from the Open Session VI of this library. Actual adc clock rate (Hz)—Returns the coerced value of the ADC clock rate. FPGA data clock rate (Hz)—Returns the rate of the FPGA data clock, which captures ADC samples. Actual reference clock rate (Hz)—Returns the coerced reference clock rate. Error out—Contains error information. This output provides standard error out functionality. |

#### Configure ADC Clock For Onboard.vi

Configures the device to use an
 onboard clock as the source of the ADC clock. If a reference
 clock source is specified, this VI also phase locks the device to that
 clock.

[IMAGE alt='image' src='GUID-D132FBCF-5B91-40DB-9CE2-D7582915AD43-a5.gif']

| Input parameters |
| --- |
| Session in—Identifies your session. Session in is obtained from the Open Session VI of this library. Reference clock source—Specifies the source of the reference clock used to generate the onboard ADC clock. None (default)—Specifies that no reference clock will be used. Clock in—Specifies that the clock source is the clock in connector on the device front panel. PXI clock—Specifies that the clock source is the clock signal from the PXI chassis. Reference clock rate (Hz)—Specifies the input reference clock rate if the reference clock source is clock in. This parameter is ignored if the reference clock source is None or PXI clock. Error in—Describes error conditions that occur before this node runs. This input provides standard error in functionality. |

| Output parameters |
| --- |
| Session out—Passes a reference to your session to the next VI. session out is obtained from the Open Session VI of this library. Actual adc clock rate (Hz)—Returns the coerced value of the ADC clock rate. FPGA data clock rate (Hz)—Returns the rate of the FPGA data clock, which captures ADC samples. Actual reference clock rate (Hz)—Returns the coerced reference clock rate. Error out—Contains error information. This output provides standard error out functionality. |

#### Configure ADC Clock For External.vi

Configures the device to use an
 external clock as the source of the ADC Clock. You must run
 the Disable Data Clock VI before turning off the external clock
 source.

[IMAGE alt='image' src='GUID-AB7882CE-08B5-43E8-B6AF-E06F09D50BC8-a5.gif']

| Input parameters |
| --- |
| Session in—Identifies your session. Session in is obtained from the Open Session VI of this library. External clock source—Specifies the source of the external clock that is divided to become the ADC clock. Clock in (default)—Specifies that the clock source is the Clock in signal from the device front panel. PXIe DStar A—Specifies that the clock source is the signal from the PXIe DStar A line. External clock rate (Hz)—Specifies the frequency of the source of the ADC clock. The default value is 0. Error in—Describes error conditions that occur before this node runs. This input provides standard error in functionality. |

| Output parameters |
| --- |
| Session out—Passes a reference to your session to the next VI. session out is obtained from the Open Session VI of this library. Actual ADC clock rate (Hz)—Returns the coerced value of the ADC clock rate. Fpga data clock rate (Hz)—Returns the rate of the FPGA data clock, which captures ADC samples. Error out—Contains error information. This output provides standard error out functionality. |

#### Configure Channel.vi

Configures vertical range, vertical offset,
 bandwidth, coupling, and impedance for the specified channel.

[IMAGE alt='image' src='GUID-C524847F-35AD-434B-B785-94A9CFBFD451-a5.gif']

| Input parameters |
| --- |
| Session in—Identifies your session. Session in is obtained from the Open Session VI of this library. Channel—Specifies the channel to be configured. The default channel is 0. Vertical range (V)—Specifies in volts the absolute value of the input range for the channel. The default value is 1.0. Vertical offset (V)—Specifies in volts the location of the center of the vertical range input with respect to ground. Enable channel (T)—Specifies whether the channel is enabled for acquisition. The default value is TRUE. Additional channel configuration—Specifies additional configurable properties for the channel. Additional channel configuration.Bandwidth—Specifies the difference between limiting frequencies within which the input signal can pass through the system with minimal amplitude loss. Default—The default bandwidth setting for the device. The bandwidth of the actual channel configuration will return the actual bandwidth value. Full bandwidth—No attenuation of the signal. Anti-alias filter—Attenuates unwanted high-frequency components of an analog signal prior to its conversion into a digital value. These signals would otherwise appear as undesired, aliased frequency components. Additional channel configuration.Coupling—Specifies which frequency components of a signal to pass through without attenuation. Default—The default coupling setting of the device. The coupling of the actual channel configuration will return the actual coupling setting. DC—Direct Current signal components will not be attenuated. AC—Alternating Current signal components will not be attenuated. Additional channel configuration.Impedance—Specifies the impedance for the channel. Default—The default impedance setting for the device. The impedance of the actual channel configuration will return the actual impedance value. 1 MΩ—The impedance of the channel will be configured at 1 MΩ. 50 Ω—The impedance of the channel will be configured at 50 Ω. Error in—Describes error conditions that occur before this node runs. This input provides standard error in functionality. |

| Output parameters |
| --- |
| Session out—Passes a reference to your session to the next VI. Session out is obtained from the Open Session VI of this library. Actual channel configuration—Returns the coerced configuration used to configure the channel. Actual channel configuration.Channel— The channel that was configured. Actual channel configuration.Coupling—Describes the coupling configuration applied to the channel. Default—The default coupling setting of the device. DC—Direct Current coupling. AC—Alternating Current coupling. Additional channel configuration.Impedance—Describes the impedance configuration applied to the channel Default—The channel was configured with the default impedance setting for the device. 1 MΩ—The channel was configured with 1 MΩ of impedance. 50 Ω—The channel was configured with 50 Ω of impedance. Additional channel configuration.Bandwidth—Describes the coerced bandwidth configuration applied to the channel. Default—The default bandwidth setting for the device. The bandwidth of the actual channel configuration will return the actual bandwidth value. Full bandwidth—No attenuation of the signal. Anti-alias filter—Attenuates unwanted high-frequency signals of an analog signal prior to its conversion into a digital value. These signals would otherwise appear as undesired, aliased frequency components. Actual channel configuration.Vertical range—Describes the coerced input range applied to the channel. Actual channel configuration.Vertical offset—Describes the coerced vertical offset configuration applied to the channel. Scaling coefficients—Returns coefficients without any digital correction for a scaled fetch. Scaling coefficients.Gain— Describes the gain coefficient. Scaling coefficients.Offset—Describes the offset coefficient. Error out—Contains error information. This output provides standard error out functionality. |

#### Close Session.vi

Closes the instrument I/O session.

[IMAGE alt='image' src='GUID-75D0FD02-08BA-4A7D-B0F8-72565BFF45D8-a5.gif']

| Input parameters |
| --- |
| Session in—Identifies your session. Session in is obtained from the Open Session VI of this library. Error in—Describes error conditions that occur before this node runs. This input provides standard error in functionality. |

| Output parameters |
| --- |
| Error out—Contains error information. This output provides standard error out functionality. |

#### Configure Digital Correction.vi

Digitally corrects the data on the FPGA.
 This VI applies the calibrated digital correction and passes the scaling
 coefficients used to fetch scaled data.

[IMAGE alt='image' src='GUID-B8CC5027-FAA5-42E8-97F7-31F5C83A79AA-a5.gif']

| Input parameters |
| --- |
| Session in—Identifies your session. Session in is obtained from the Open Session VI of this library. Actual channel configuration—Specifies a reference to the coerced configuration used to configure the channel. This parameter is obtained from the Configure Channel VI. Actual channel configuration.Channel—Specifies the channel that was configured. Actual channel configuration.Coupling—Specifies the coupling of the channel. Default—The default coupling setting of the device. DC—Direct Current signal. AC—Alternating Current signal. Actual channel configuration.Impedance—Specifies the impedance for the channel. Default—The default impedance setting for the device. 1 MΩ—1 MΩ of impedance. 50 Ω—50 Ω of impedance. Additional channel configuration.Bandwidth—Specifies the bandwidth of the channel. Default—The default bandwidth setting for the device. Full bandwidth—No attenuation of the signal. Anti-alias filter—Attenuates unwanted high-frequency signals of an analog signal prior to its conversion into a digital value. These signals would otherwise appear as undesired, aliased frequency components. Actual channel configuration.Vertical range—Specifies the vertical range of the channel. Actual channel configuration.Vertical offset—Specifies the vertical offset of the channel. Range adjust—Adjusts the digital corrected data using the scaling factor. This can be used to prevent clipping when the acquired data is slightly greater than the nominal range. Enable (T)—Specifies whether digital correction is enabled. The default value is TRUE. Error in—Describes error conditions that occur before this node runs. This input provides standard error in functionality. |

| Output parameters |
| --- |
| Session out—Passes a reference to your session to the next VI. Session out is obtained from the Open Session VI of this library. Scaling coefficients—Returns coefficients without any digital correction for a scaled fetch. Scaling coefficients.Gain— Describes the gain coefficient. Scaling coefficients.Offset—Describes the offset coefficient. Error out—Contains error information. This output provides standard error out functionality. |

#### Export Clock.vi

Exports the ADC clock signal or reference clock signal to
 a specified output terminal. If the clock to export has not been configured, this VI
 will return an error.

[IMAGE alt='image' src='GUID-2F3BF1CF-AC67-478E-815D-21D02246E1F0-a5.gif']

| Input parameters |
| --- |
| Session in—Identifies your session. Session in is obtained from the Open Session VI of this library. Exported clock—Specifies the clock signal to export. None—The default coupling setting of the device. ADC clock—Direct Current signal. PLL reference clock—The phase-locked reference clock signal will be exported. Output terminal—Specifies the terminal to which the clock signal will be exported. You can choose not to export any signal. Do not export—Specifies that the signal is not exported. Clock out—Specifies that the signal is exported to the CLK OUT terminal. Error in—Describes error conditions that occur before this node runs. This input provides standard error in functionality. |

| Output parameters |
| --- |
| Session out—Passes a reference to your session to the next VI. Session out is obtained from the Open Session VI of this library. Error out—Contains error information. This output provides standard error out functionality. |

#### Disable Data Clock.vi

Disables the Data Clock. You should run this VI
 before turning off the source of an external clock. The Data Clock will be
 re-enabled when you run the Configure ADC Clock VI of this
 library.

[IMAGE alt='image' src='GUID-AC1AE2E1-D549-47AA-A9B6-F367E6591878-a5.gif']

| Input parameters |
| --- |
| Session in—Identifies your session. Session in is obtained from the Open Session VI of this library. Error in—Describes error conditions that occur before this node runs. This input provides standard error in functionality. |

| Output parameters |
| --- |
| Session out—Passes a reference to your session to the next VI. Session out is obtained from the Open Session VI of this library. Error out—Contains error information. This output provides standard error out functionality. |

#### Wait Until Settled.vi

Waits until the
 input signal settles. Call this VI after configuring the channel to wait for the
 input signal to settle.

[IMAGE alt='image' src='GUID-421C2490-207C-4771-B267-D197EB001230-a5.gif']

| Input parameters |
| --- |
| Session in—Identifies your session. Session in is obtained from the Open Session VI of this library. Timeout (5000 ms)—Specifies the maximum amount of time to wait until input signal is settled. Error in—Describes error conditions that occur before this node runs. This input provides standard error in functionality. |

| Output parameters |
| --- |
| Session out—Passes a reference to your session to the next VI. Session out is obtained from the Open Session VI of this library. Error out—Contains error information. This output provides standard error out functionality. |

#### Check Channel Overload.vi

Checks all input channels on the device for
 overload conditions.

[IMAGE alt='image' src='GUID-42E40924-A3FE-4D18-A88B-F38490FDEA68-a5.gif']

| Input parameters |
| --- |
| Session in—Identifies your session. Session in is obtained from the Open Session VI of this library. Set error? (T)—Specifies whether or not to set an error if overload conditions are detected. If this parameter is TRUE, then this VI will return an error if it detects overload conditions on any channels. Error in—Describes error conditions that occur before this node runs. This input provides standard error in functionality. |

| Output parameters |
| --- |
| Session out—Passes a reference to your session to the next VI. Session out is obtained from the Open Session VI of this library. Overloaded?—Returns TRUE if one or more channels are overloaded. Error out—Contains error information. This output provides standard error out functionality. |

#### Clear Channel Overload.vi

Clears the overload condition from all device
 input channels. If this VI clears an overloaded channel, you should wait the minimum
 wait time for the channel to settle before acquiring data from on that
 channel.

[IMAGE alt='image' src='GUID-AAFBC143-C000-4393-A49D-F3B494108B00-a5.gif']

| Input parameters |
| --- |
| Session in—Identifies your session. Session in is obtained from the Open Session VI of this library. Error in—Describes error conditions that occur before this node runs. This input provides standard error in functionality. |

| Output parameters |
| --- |
| Session out—Passes a reference to your session to the next VI. Session out is obtained from the Open Session VI of this library. Min wait time (ms)—Returns the minimum amount of time you should wait after an overloaded channel has been cleared before acquiring data from that channel. if one or more channels are overloaded. Error out—Contains error information. This output provides standard error out functionality. |

#### Get Number Of Channels.vi

Returns the
 maximum number of channels supported by the device.

[IMAGE alt='image' src='GUID-31BB49F2-96EB-4029-9B6C-A448ED6A86BC-a5.gif']

| Input parameters |
| --- |
| Session in—Identifies your session. Session in is obtained from the Open Session VI of this library. Error in—Describes error conditions that occur before this node runs. This input provides standard error in functionality. |

| Output parameters |
| --- |
| Session out—Passes a reference to your session to the next VI. Session out is obtained from the Open Session VI of this library. Number of channels—Returns the maximum number of channels supported by the device. Error out—Contains error information. This output provides standard error out functionality. |

#### Check Status.vi

Checks the overall status of the device and reports
 whether it is operating correctly. This VI checks for system monitor alarms, such as
 temperature error, power error, FPGA voltage errors, clock PLL lock errors, and
 channel overload errors.

[IMAGE alt='image' src='GUID-F4E89469-0AA5-494A-9B99-103D4295C975-a5.gif']

| Input parameters |
| --- |
| Session in—Identifies your session. Session in is obtained from the Open Session VI of this library. Error in—Describes error conditions that occur before this node runs. This input provides standard error in functionality. |

| Output parameters |
| --- |
| Session out—Passes a reference to your session to the next VI. Session out is obtained from the Open Session VI of this library. Error out—Contains error information. This output provides standard error out functionality. |

#### Read
 Temperature.vi

Returns a specified temperature measurement, in degrees
 Celsius.

[IMAGE alt='image' src='GUID-74C0E84F-1485-4D1A-B9DB-A0A968D308DE-a5.gif']

| Input parameters |
| --- |
| Session in—Identifies your session. Session in is obtained from the Open Session VI of this library. Source—Specifies the source of the temperature measurement to be returned by the temperature output. Device temperature—Specifies the temperature of the analog front-end of the device as the temperature to return. Thermal shutdown margin—Specifies the temperature difference between the FPGA temperature sensor and the FPGA temperature limit as the measurement to return. FPGA temperature—Specifies the current FPGA die temperature as the measurement to return. FPGA temperature limit—Specifies the thermal shutdown limit of the FPGA sensor as the measurement to return. Error in—Describes error conditions that occur before this node runs. This input provides standard error in functionality. |

| Output parameters |
| --- |
| Session out—Passes a reference to your session to the next VI. Session out is obtained from the Open Session VI of this library. Temperature (°C)—Returns the temperature measurement in degrees Celsius. Error out—Contains error information. This output provides standard error out functionality. |

#### Read
 Power.vi

Returns a specified power measurement, in Watts.

[IMAGE alt='image' src='GUID-488814B1-4EA0-4ABC-BB54-75DA62900333-a5.gif']

| Input parameters |
| --- |
| Session in—Identifies your session. Session in is obtained from the Open Session VI of this library. Source—Describes the source of the power measurement to be returned by the power output. Device power consumption (default)—Specifies the total instantaneous power consumption of the device as the measurement source. Power shutdown margin—Specifies the difference between the power limit and the device power consumption as the measurement source. Power limit—Specifies the shutdown limit as the measurement source. Default power limit—Specifies the default power limit as the measurement source. The default power limit varies by device. Maximum power limit—Specifies the highest value accepted by the measurement source. Error in—Describes error conditions that occur before this node runs. This input provides standard error in functionality. |

| Output parameters |
| --- |
| Session out—Passes a reference to your session to the next VI. Session out is obtained from the Open Session VI of this library. Power (W)—Returns the power measurement in Watts. Error out—Contains error information. This output provides standard error out functionality. |

#### Is
 DRAM Initialized.vi

Indicates whether the DRAM is ready to be used. After
 downloading a new FPGA VI to the device, you must wait until the DRAM banks are
 initialized, before accessing the DRAM.

[IMAGE alt='image' src='GUID-4A9BD71E-2E0E-434C-875A-354182D35F03-a5.gif']

| Input parameters |
| --- |
| Session in—Identifies your session. Session in is obtained from the Open Session VI of this library. Set error? (T)—Sets an error if one or more DRAM banks are not initialized. Error in—Describes error conditions that occur before this node runs. This input provides standard error in functionality. |

| Output parameters |
| --- |
| Session out—Passes a reference to your session to the next VI. Session out is obtained from the Open Session VI of this library. DRAM initialized?—Returns TRUE if the DRAM is ready to be used, and FALSE if the DRAM is not ready to be used. Error out—Contains error information. This output provides standard error out functionality. |

#### Read
 Clocking Status.vi

Reads the status of a device to check for clock
 faults.

[IMAGE alt='image' src='GUID-0811554C-4241-4CE1-9257-F65B24EF1FD6-a5.gif']

| Input parameters |
| --- |
| FGPA interface in—Specifies a LV FPGA interface wire to communicate with the FPGA and board driver. Error in—Describes error conditions that occur before this node runs. This input provides standard error in functionality. |

| Output parameters |
| --- |
| FGPA interface out—Passes a LV FPGA interface wire to the next VI. Clock fault?—Indicates whether the data clock is in a faulty state. Error out—Contains error information. This output provides standard error out functionality. |

Parent topic:

Configuration Overview

<!--NI_TOPIC bundle=ni-reconfigurable-oscilloscopes path=configuration-overview.html language=enus -->
## TOPIC 00019: Configuration Overview

- bundle_id: `ni-reconfigurable-oscilloscopes`
- source_path: `configuration-overview.html`
- source_url: https://docs-be.ni.com/bundle/ni-reconfigurable-oscilloscopes/raw/resource/enus/configuration-overview.html
- document_id: `ni-reconfigurable-oscilloscopes`
- page_type: `leaf`
- content_type: `concept`
- source_description: This instrument design library provides functionality to configure hardware settings and to check if the hardware is operating correctly.Use this instrument design library to configure and check the status of a device. This library controls the reference and sample clocks, and ADCs. It includes host

### Configuration Overview

This instrument design library provides functionality to configure hardware settings and to check
 if the hardware is operating correctly.

Use this instrument design library to configure and check the status of a device. This library
 controls the reference and sample clocks, and ADCs. It includes host VIs and FPGA
 VIs.

#### Open Session

You must call the Open Session VI to open a Configuration
 instrument design library session before performing any device configuration. This
 VI initializes FPGA, Basecard, Clock, CPLD, ADC and Phase DAC registers.

#### Clock and ADC Configuration

Use the Configure ADC Clock VI to configure the Onboard or
 External clock. After the clock is configured, the data clock in the device FPGA is
 enabled. The Configure ADC Clock VI reads the current clock
 configuration from the device and has no effect on the hardware configuration if the
 clock and ADCs are already configured correctly.

#### Channel Configuration

You must configure the clock and ADCs before running the Channel
 Configuration VI. Use this VI to configure the channel parameters.
 After the channel is configured, the scaling coefficients are provided, which can be
 used to fetch scaled data. The Configure Channel VI exposes all
 the properties that can be configured and writes them to the hardware using the
 *Instruction Framework*.

#### Hardware Status

After configuring the channel, use the corresponding Wait Until
 Settled VI to allow the hardware to settle prior to acquiring a
 signal.

You must configure the clock and ADCs before running the Check
 Status VI. Use this VI to check the configuration status. The
 Check Status VI queries the clock PLL, ADC PLL, clock fault,
 channel overload, and power and temperature shutdown statuses.

#### Export Clock

You must configure the clock and ADC before running the Export
 Clock VI. Use this VI to export the device reference
 clock.

#### Digital Correction

Use the Digital Correction to apply compensation for DC gain and
 offset variations. Use the Configure Digital Correction host VI
 to enable digital correction. This VI will download a set of scaling coefficients to
 the FPGA for the specified input configuration. These coefficients will be applied
 to the data-path by the Digital Correction FPGA VI.

Parent topic:

LabVIEW Instrument Design Libraries for Reconfigurable Oscilloscopes

Related concepts:

- Instruction Framework Overview

<!--NI_TOPIC bundle=ni-reconfigurable-oscilloscopes path=configuring-the-hardware-in-max.html language=enus -->
## TOPIC 00020: Configuring the Hardware in MAX

- bundle_id: `ni-reconfigurable-oscilloscopes`
- source_path: `configuring-the-hardware-in-max.html`
- source_url: https://docs-be.ni.com/bundle/ni-reconfigurable-oscilloscopes/raw/resource/enus/configuring-the-hardware-in-max.html
- document_id: `ni-reconfigurable-oscilloscopes`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use Measurement & Automation Explorer (MAX) to configure your NI hardware. MAX informs other programs about which devices reside in the system and how they are configured. MAX can optionally be installed with the instrument design libraries. Launch MAX by navigating to Start»All Programs»National In

### Configuring the Hardware in MAX

Use Measurement & Automation Explorer (MAX) to configure your NI hardware. MAX informs other
 programs about which devices reside in the system and how they are configured. MAX can
 optionally be installed with the instrument design libraries.

1. Launch MAX by navigating to Start»All Programs»National Instruments»Measurement & Automation or by clicking the NI MAX desktop icon.
2. In the Configuration pane, double-click Devices and Interfaces to see the list of installed devices. Installed devices appear under the name of their associated chassis.
3. Expand your Chassis tree item. MAX lists all devices installed in the
 chassis. NI reconfigurable oscilloscopes appear as NI-RIO devices in the list. Your
 default device names may vary. Note If you do not see your hardware
 listed, refer to the *Troubleshooting* topic.
4. Record the RIO Resource Name MAX assigns to the hardware. Use this identifier when programming your reconfigurable oscilloscope.

Caution

Related concepts:

- Troubleshooting
- Creating a RIO Alias for a Reconfigurable Oscilloscope Device

<!--NI_TOPIC bundle=ni-reconfigurable-oscilloscopes path=creating-a-rio-alias-for-a-reconfigurable-osc.html language=enus -->
## TOPIC 00021: Creating a RIO Alias for a Reconfigurable Oscilloscope Device

- bundle_id: `ni-reconfigurable-oscilloscopes`
- source_path: `creating-a-rio-alias-for-a-reconfigurable-osc.html`
- source_url: https://docs-be.ni.com/bundle/ni-reconfigurable-oscilloscopes/raw/resource/enus/creating-a-rio-alias-for-a-reconfigurable-osc.html
- document_id: `ni-reconfigurable-oscilloscopes`
- page_type: `leaf`
- content_type: `concept`
- source_description: MAX allows you to create an alias for each reconfigurable oscilloscope. The alias is used in the instrument design libraries to operate the hardware resources. You are not required to create a RIO alias, but doing so can make programming easier. Reconfigurable oscilloscopes appear as NI-RIO devices

### Creating a RIO Alias for a Reconfigurable Oscilloscope Device

MAX allows you to create an alias for each reconfigurable oscilloscope. The alias is used in the
 instrument design libraries to operate the hardware resources. You are not required to
 create a RIO alias, but doing so can make programming easier. Reconfigurable
 oscilloscopes appear as NI-RIO devices in MAX. To create an alias for your device in
 MAX, complete the following steps:

1. Right-click the device name in the configuration tree.
2. Select Rename Alias from the shortcut menu.
3. Enter a new RIO alias for your NI-RIO device.
4. Press Enter .
5. Verify that the new aliases for all of your device are displayed.

Caution

<!--NI_TOPIC bundle=ni-reconfigurable-oscilloscopes path=creating-an-application-with-instrument-desig.html language=enus -->
## TOPIC 00022: Creating an Application with Instrument Design Libraries

- bundle_id: `ni-reconfigurable-oscilloscopes`
- source_path: `creating-an-application-with-instrument-desig.html`
- source_url: https://docs-be.ni.com/bundle/ni-reconfigurable-oscilloscopes/raw/resource/enus/creating-an-application-with-instrument-desig.html
- document_id: `ni-reconfigurable-oscilloscopes`
- page_type: `leaf`
- content_type: `concept`
- source_description: The instrument design libraries ship with two LabVIEW sample projects that provide functionality similar to common uses of oscilloscopes and high-speed digitizers. You can run these sample projects without any modifications or use them as starting points for creating application-specific instrument

### Creating an Application with Instrument Design Libraries

The instrument design libraries ship with two LabVIEW sample projects that provide functionality
 similar to common uses of oscilloscopes and high-speed digitizers. You can run these
 sample projects without any modifications or use them as starting points for creating
 application-specific instrument designs. Each sample project contains host VIs, which
 run on the host computer, and FPGA VIs, which run on the device itself. Block diagram
 comments describe the functionality of the VIs and indicate opportunities to customize
 the code.

<!--NI_TOPIC bundle=ni-reconfigurable-oscilloscopes path=data-manipulation-host-vis.html language=enus -->
## TOPIC 00023: Data Manipulation Host VIs

- bundle_id: `ni-reconfigurable-oscilloscopes`
- source_path: `data-manipulation-host-vis.html`
- source_url: https://docs-be.ni.com/bundle/ni-reconfigurable-oscilloscopes/raw/resource/enus/data-manipulation-host-vis.html
- document_id: `ni-reconfigurable-oscilloscopes`
- page_type: `leaf`
- content_type: `concept`
- source_description: Reshape.vi Changes the dimension size(s) of an array according to the size value(s). The elements of the array are not changed or initialized. Input parameters Array Specifies the array to be reshaped. Size or dimension size Specifies the dimension(s) of the array. Error in Describes error condition

### Data Manipulation Host VIs

#### Reshape.vi

Changes the dimension size(s) of an array according to the size value(s). The
 elements of the array are not changed or initialized.

[IMAGE alt='image' src='GUID-0357BABD-8A29-4A6A-A5E1-71E4B6618246-a5.gif']

| Input parameters |
| --- |
| Array—Specifies the array to be reshaped. Size or dimension size—Specifies the dimension(s) of the array. Error in—Describes error conditions that occur before this node runs. This input provides standard error in functionality. |

| Output parameters |
| --- |
| Reshaped array—An array of the size specified by size. If size is larger than the size of array, new uninitialized elements are added to the end. While the size of array may be changed, no elements in the array will be changed. Allocated more space—Indicates if the function resulted in new memory being allocated. Error out—Contains error information. This output provides standard error out functionality. |

#### Typecast, Deinterleave, and
 Scale.vi

Replaces portions of data in at the point you specify in data in index
 0 and data in index 1 using new data. The
 function takes new data and typecasts the array using the type specified in typecast
 type. The resulting type casted data is deinterleaved and scaled before being placed
 in data in. The deinterleaving and scaling must be specified by you in deinterleave
 factor and scaling coefficients. The resulting data is provided in data out. The
 number of elements operated on are indicated by index 0
 elements scaled and index 1 elements scaled. This VI is
 optimized to minimize buffer allocations and maximize throughput.

[IMAGE alt='image' src='GUID-4AEF3124-F993-4BB0-8893-44FA4583A6C8-a5.gif']

| Input parameters |
| --- |
| Data in—Specifies the array new data will be deinterleaved and scaled into. Deinterleave factor—Specifies the number of elements that will be deinterleaved from the 1D array new data into the 2D array data in. Each deinterleaved element from new data is placed into a different dimension of data out. If new data has a size greater than data in then the number of elements moved is truncated to the amount of space available. Scaling coefficients—Specifies the array of coefficients to be used to scale data in. Each index corresponds to a row in the 2D array data in. New data—The array that will be operated on and placed into the 2D array specified by data in. Data in index 0—Specifies the row of data in to begin replacing. Data in index 1—Specifies the column of data in to begin replacing. New data index—Specifies the index of new data to begin copying from. Typecast type—Specifies the type to cast new data to before completing the rest of the operations. Error in—Describes error conditions that occur before this node runs. This input provides standard error in functionality. |

| Output parameters |
| --- |
| Data out—The array this function returns with the updated elements. Index 0 elements scaled—Indicates the actual number of row elements updated in data out. Index 1 elements scaled—Indicates the actual number of column elements updated in data out. Error out—Contains error information. This output provides standard error out functionality. |

#### Typecast and
 Deinterleave.vi

Replaces portions of data in at the point you specify in data in index
 0 and data in index 1 using new data. The
 function takes new data and typecasts the array to the type of data out. The
 resulting type casted data is deinterleaved before being placed in data in. The
 deinterleaving must be specified by you in deinterleave factor. The resulting data
 is provided in data out. The number of elements operated on are indicated by
 index 0 elements deinterleaved and index
 1 elements deinterleaved. This VI is optimized to minimize buffer
 allocations and maximize throughput.

[IMAGE alt='image' src='GUID-06750858-3177-4A6A-9947-EE2ACD96B092-a5.gif']

| Input parameters |
| --- |
| Data in—Specifies the array new data will be deinterleaved into. Deinterleave factor—Specifies the number of elements that will be deinterleaved from the 1D array new data into the 2D array data in. Each deinterleaved element from new data is placed into a different dimension of data out. If new data has a size greater than data in then the number of elements moved is truncated to the amount of space available. New data—The array that will be operated on and placed into the 2D array specified by data in. Data in index 0—Specifies the row of data in to begin replacing. Data in index 1—Specifies the column of data in to begin replacing. New data index—Specifies the index of new data to begin copying from. Error in—Describes error conditions that occur before this node runs. This input provides standard error in functionality. |

| Output parameters |
| --- |
| Data out—The array this function returns with the updated elements. Index 0 elements deinterleaved—Indicates the actual number of row elements updated in data out. Index 1 elements deinterleaved—Indicates the actual number of column elements updated in data out. Error out—Contains error information. This output provides standard error out functionality. |

#### Deinterleave and Scale.vi

Replaces portions of data in at the point you specify in data in index
 0 and data in index 1 using new data. new
 data is deinterleaved and scaled before being placed in data in. The deinterleaving
 and scaling must be specified by you in deinterleave factor and scaling
 coefficients. The resulting data is provided in data out. The number of elements
 operated on are indicated by index 0 elements scaled and
 index 1 elements scaled. This VI is optimized to minimize
 buffer allocations and maximize throughput.

[IMAGE alt='image' src='GUID-E43C3474-6EC8-41F5-8824-E931DB28607C-a5.gif']

| Input parameters |
| --- |
| Data in—Specifies the array new data will be deinterleaved and scaled into. Deinterleave factor—Specifies the number of elements that will be deinterleaved from the 1D array new data into the 2D array data in. Each deinterleaved element from new data is placed into a different dimension of data out. If new data has a size greater than data in then the number of elements moved is truncated to the amount of space available. Scaling coefficients—Specifies the array of coefficients to be used to scale data in. Each index corresponds to a row in the 2D array data in. New data—The array that will be operated on and placed into the 2D array specified by data in. Data in index 0—Specifies the row of data in to begin replacing. Data in index 1—Specifies the column of data in to begin replacing. New data index—Specifies the index of new data to begin copying from. Error in—Describes error conditions that occur before this node runs. This input provides standard error in functionality. |

| Output parameters |
| --- |
| Data out—The array this function returns with the updated elements. Index 0 elements scaled—Indicates the actual number of row elements updated in data out. Index 1 elements scaled—Indicates the actual number of column elements updated in data out. Error out—Contains error information. This output provides standard error out functionality. |

#### Typecast and Copy.vi

Replaces portions of data in at the point you specify in data in index using new
 data. The function takes new data and typecasts the array to the type of data out
 before being placed in data in. The resulting data is provided in data out. The
 number of elements operated on is indicated by elements copied. This VI is optimized
 to minimize buffer allocations and maximize throughput.

[IMAGE alt='image' src='GUID-F6A4BD4C-BD20-47EC-860E-A829F041BCC7-a5.gif']

| Input parameters |
| --- |
| Data in—Specifies the array new data will be copied into. New data—The array that will be operated on and placed into the array specified by data in. Data in index—Specifies the index of data in to begin replacing. New data index—Specifies the index of new data to begin copying from. Error in—Describes error conditions that occur before this node runs. This input provides standard error in functionality. |

| Output parameters |
| --- |
| Data out—The array this function returns with the updated elements. Elements copied—Indicates the actual number of elements copied into data out. Error out—Contains error information. This output provides standard error out functionality. |

#### Deinterleave.vi

Replaces portions of data in at the point you specify in data in index
 0 and data in index 1 using new data. The
 function deinterleaves new data before placing the result in data in. The
 deinterleaving must be specified by you in deinterleave factor. The resulting data
 is provided in data out. The number of elements operated on are indicated by
 index 0 elements deinterleaved and index
 1 elements deinterleaved. This VI is optimized to minimize buffer
 allocations and maximize throughput.

[IMAGE alt='image' src='GUID-2C6E4383-2823-4FAE-A213-07218E8EF388-a5.gif']

| Input parameters |
| --- |
| Data in—Specifies the array new data will be deinterleaved into. Deinterleave factor—Specifies the number of elements that will be deinterleaved from the 1D array new data into the 2D array data in. Each deinterleaved element from new data is placed into a different dimension of data out. If new data has a size greater than data in then the number of elements moved is truncated to the amount of space available. New data—The array that will be operated on and placed into the 2D array specified by data in. Data in index 0—Specifies the row of data in to begin replacing. Data in index 1—Specifies the column of data in to begin replacing. New data index—Specifies the index of new data to begin copying from. Error in—Describes error conditions that occur before this node runs. This input provides standard error in functionality. |

| Output parameters |
| --- |
| Data out—The array this function returns with the updated elements. Index 0 elements deinterleaved—Indicates the actual number of row elements updated in data out. Index 1 elements deinterleaved—Indicates the actual number of column elements updated in data out. Error out—Contains error information. This output provides standard error out functionality. |

#### Scale.vi

Replaces portions of data in at the point you specify in data in index using new
 data. new data is scaled before being placed in data in. The scaling must be
 specified by you in scaling coefficients. The resulting data is provided in data
 out. The number of elements operated on is indicated by elements scaled. This VI is
 optimized to minimize buffer allocations and maximize throughput.

[IMAGE alt='image' src='GUID-17709FEB-53A2-498F-BED1-17721C9C928B-a5.gif']

| Input parameters |
| --- |
| Data in—Specifies the array new data will be scaled into. Scaling coefficients—Specifies the coefficients to be used to scale data in. New data—The array that will be operated on and placed into the array specified by data in. Data in index—Specifies the index of data in to begin replacing. New data index—Specifies the index of new data to begin copying from. Error in—Describes error conditions that occur before this node runs. This input provides standard error in functionality. |

| Output parameters |
| --- |
| Data out—The array this function returns with the updated elements. Elements scaled—Indicates the actual number of elements scaled into data out. Error out—Contains error information. This output provides standard error out functionality. |

#### Typecast and Scale.vi

Replaces portions of data in at the point you specify in data in index using new
 data. The function takes new data and typecasts the array using the type specified
 in typecast type. The resulting type casted data is scaled before being placed in
 data in. The scaling must be specified by you in scaling coefficients. The resulting
 data is provided in data out. The number of elements operated on are indicated by
 elements scaled. This VI is optimized to minimize buffer allocations and maximize
 throughput.

[IMAGE alt='image' src='GUID-F1F6B1A9-4471-4C50-9C66-7101F8E4FB9A-a5.gif']

| Input parameters |
| --- |
| Data in—Specifies the array new data will be scaled into. Scaling coefficients—Specifies the coefficients to be used to scale data in. New data—The array that will be operated on and placed into the array specified by data in. Data in index—Specifies the index of data in to begin replacing. New data index—Specifies the index of new data to begin copying from. Typecast type—Specifies the type to cast new data to before completing the rest of the operations. Error in—Describes error conditions that occur before this node runs. This input provides standard error in functionality. |

| Output parameters |
| --- |
| Data out—The array this function returns with the updated elements. Elements scaled—Indicates the actual number of elements updated in data out. Error out—Contains error information. This output provides standard error out functionality. |

Parent topic:

Data Manipulation Overview

<!--NI_TOPIC bundle=ni-reconfigurable-oscilloscopes path=data-manipulation-overview.html language=enus -->
## TOPIC 00024: Data Manipulation Overview

- bundle_id: `ni-reconfigurable-oscilloscopes`
- source_path: `data-manipulation-overview.html`
- source_url: https://docs-be.ni.com/bundle/ni-reconfigurable-oscilloscopes/raw/resource/enus/data-manipulation-overview.html
- document_id: `ni-reconfigurable-oscilloscopes`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use this instrument design library to manipulate and allocate arrays on the host. This library contains IP for deinterleaving, scaling, and copying arrays, and can optionally perform these operations after typecasting the input array to a larger data type. This typecast functionality can be useful w

### Data Manipulation Overview

Use this instrument design library to manipulate and allocate arrays on the host. This library
 contains IP for deinterleaving, scaling, and copying arrays, and
 can optionally perform these operations after typecasting the
 input array to a larger data type. This typecast functionality
 can be useful when transferring different data types through a
 single Target to Host FIFO type. For example,
 some applications will stream 16-bit or 32-bit integer array
 data through an 8-bit integer target to the host FIFO and use
 this library to typecast and scale the data to a floating point
 array. The implementation of this library is optimized to reduce
 data copies and maximize throughput.

This instrument design library is particularly useful in streaming applications that require high
 performance and efficient use of host memory.

Parent topic:

LabVIEW Instrument Design Libraries for Reconfigurable Oscilloscopes

<!--NI_TOPIC bundle=ni-reconfigurable-oscilloscopes path=data-trigger-fpga-vis.html language=enus -->
## TOPIC 00025: Data Trigger FPGA VIs

- bundle_id: `ni-reconfigurable-oscilloscopes`
- source_path: `data-trigger-fpga-vis.html`
- source_url: https://docs-be.ni.com/bundle/ni-reconfigurable-oscilloscopes/raw/resource/enus/data-trigger-fpga-vis.html
- document_id: `ni-reconfigurable-oscilloscopes`
- page_type: `leaf`
- content_type: `concept`
- source_description: Edge.viGenerates a trigger when the input data sample meets the hysteresis conditions on either a rising or falling edge of the input. You can use the configuration input to set the triggering and hysteresis conditions for this VI. Input parameters Data in It is the data sample input. This VI compar

### Data Trigger FPGA VIs

#### Edge.vi

Generates a trigger when the input data sample meets the
 hysteresis conditions on either a rising or falling edge of the input. You can use
 the configuration input to set the triggering and hysteresis conditions for this
 VI.

[IMAGE alt='image' src='GUID-BE8BA214-7315-4C97-9095-4AE844AFA9D3-a5.gif']

| Input parameters |
| --- |
| Data in—It is the data sample input. This VI compares this input to the thresholds specified in the configuration input. This parameter is either a single value or an array of values, depending on how many samples per data clock cycle your host VI sends to the FPGA. Reset—It resets the VI to its default state. Setting this value to TRUE clears the internal handshaking buffers, writes a FALSE value to the ready for output and input valid buffers, and returns FALSE for the trigger and output valid output parameters. This parameter does not affect the value of the data in input parameter. Since the outputs of this VI are buffered, it takes one FPGA clock cycle for changes to this parameter to affect the trigger and output valid output parameters. Configuration—Configuration contains trigger configuration settings. Configuration.highLevel—Specifies the value that data in must exceed in order to trigger on a positive slope after crossing the hysteresis threshold. Refer to the trigger slope element of this cluster for more information. Configuration.lowLevel—Specifies the value that data in must be less than in order to trigger on a negative slope after crossing the hysteresis threshold. Refer to the trigger slope element of this cluster for more information. Configuration.trigger slope—Specifies how the hysteresis threshold is calculated, and whether this VI should trigger when the input data is rising or falling. Positive—Configures this VI to trigger when two conditions are met. First, a sample from data in must fall below the difference between the highLevel and lowLevel values specified in this cluster. Then, a different sample from data in must rise above the highLevel value. This second sample is the data sample that causes this VI to trigger. Negative—Configures this VI to trigger when two conditions are met. First, a sample from data in must exceed the sum of the highLevel and lowLevel values specified in this cluster. Then, a different sample from data in must fall below the lowLevel value. This second sample is the data sample that causes this VI to trigger. Arm (T)—Specifies whether or not this VI should be able to trigger, regardless of the value of the data in input. Setting this value to TRUE allows this VI to trigger. Setting this value to FALSE prevents this VI from triggering. Input valid—Specifies whether the data in input contains valid data. If this value is TRUE, the data is valid and this VI can trigger. If this value is FALSE, the data is invalid and this VI will not trigger. Ready for output (T)— Indicates to the next VI whether or not the output of this VI is valid. |

| Output parameters |
| --- |
| Data out—Returns the value from the data in input. This value is pipelined and time-aligned with the trigger output. Trigger—It is the trigger signal. This output is TRUE if the sample from data in meets the trigger conditions. The default value is FALSE. Trigger index out—Returns the index of the sample in the data in input parameter that caused this VI to trigger. If multiple elements of data in caused this VI to trigger, this parameter returns the index of the first sample to meet the trigger conditions. If your data in input is a single value rather than an array, this parameter will always return 0. Output valid—Returns the value from the input valid input. This parameter indicates whether or not the data in input contains valid data. This parameter does not indicate whether or not the trigger output is valid. Datapath delay—Indicates the number of FPGA clock cycles necessary for this VI to process input data and return associated output data. This parameter has a constant value of 2. Ready for input—Indicates whether or not this VI is ready to receive input data. This output is TRUE when this VI is prepared to receive input data, and FALSE when this VI is not prepared to receive input data. |

#### Level.vi

Generates a trigger when the
 input data sample is more than or less than a specified value. You can use the
 configuration input to set the triggering conditions for this VI.

[IMAGE alt='image' src='GUID-A1A13AFC-2CB3-4EAB-A52D-52056850B210-a5.gif']

| Input parameters |
| --- |
| Data in—It is the data sample input. This VI compares this input to the level specified in the configuration input. This parameter is either a single value or an array of values, depending on how many samples per data clock cycle you acquire from the FPGA. Reset—It resets the VI to its default state. Setting this value to TRUE clears the internal handshaking buffers, writes a FALSE value to the ready for output and input valid buffers, and returns FALSE for the trigger and output valid output parameters. This parameter does not affect the value of the data in input parameter. Since the outputs of this VI are buffered, it takes one FPGA clock cycle for changes to this parameter to affect the trigger and output valid output parameters. Configuration—Configuration contains trigger configuration settings. Configuration.level—It is the value that the data in value is compared to. This parameter has the same data type as the data in input. Configuration.trigger when—Specifies whether the VI triggers when data in is more than or less than level. Trigger above—The VI will trigger if data in is more than level. Trigger below—The VI will trigger if data in is less than level. Arm (T)—Specifies whether or not this VI should be able to trigger, regardless of the value of the data in input. Setting this value to TRUE allows this VI to trigger. Setting this value to FALSE prevents this VI from triggering. Input valid—Specifies whether the data in input contains valid data. If this value is TRUE, the data is valid and this VI can trigger. If this value is FALSE, the data is invalid and this VI will not trigger. Ready for output (T)— Indicates to the next VI whether or not the output of this VI is valid. |

| Output parameters |
| --- |
| Data out—Returns the value from the data in input. This value is pipelined and time-aligned with the trigger output. Trigger—It is the trigger signal. This output is TRUE if the sample from data in meets the trigger conditions. The default value is FALSE. Trigger index out—Returns the index of the sample in the data in input parameter that caused this VI to trigger. If multiple elements of data in caused this VI to trigger, this parameter returns the index of the first sample to meet the trigger conditions. If your data in input is a single value rather than an array, this parameter will always return 0. Output valid—Returns the value from the input valid input. This parameter indicates whether or not the data in input contains valid data. This parameter does not indicate whether or not the trigger output is valid. Datapath delay—Indicates the number of FPGA clock cycles necessary for this VI to process input data and return associated output data. This parameter has a constant value of 2. Ready for input—Indicates whether or not this VI is ready to receive input data. This output is TRUE when this VI is prepared to receive input data, and FALSE when this VI is not prepared to receive input data. |

Parent topic:

Data Trigger Overview

<!--NI_TOPIC bundle=ni-reconfigurable-oscilloscopes path=data-trigger-overview.html language=enus -->
## TOPIC 00026: Data Trigger Overview

- bundle_id: `ni-reconfigurable-oscilloscopes`
- source_path: `data-trigger-overview.html`
- source_url: https://docs-be.ni.com/bundle/ni-reconfigurable-oscilloscopes/raw/resource/enus/data-trigger-overview.html
- document_id: `ni-reconfigurable-oscilloscopes`
- page_type: `leaf`
- content_type: `concept`
- source_description: This instrument design library can be used to generate a trigger on an input signal under various conditions. The triggers produced by this library are typically consumed by the acquisition block in order to determine when to start and stop acquiring data.This library supports multiple trigger types

### Data Trigger Overview

This instrument design library can be used to generate a trigger on an input signal under various
 conditions. The triggers produced by this library are typically consumed by the
 acquisition block in order to determine when to start and stop acquiring data.

This library supports multiple trigger types. For more information on supported triggers and
 their use, refer to the LabVIEW context help for the Data Trigger VIs or to *Data
 Trigger FPGA VIs*.

This library supports various data types and samples per cycle.

Parent topic:

LabVIEW Instrument Design Libraries for Reconfigurable Oscilloscopes

Related concepts:

- Data Trigger FPGA VIs

<!--NI_TOPIC bundle=ni-reconfigurable-oscilloscopes path=digital-signal-processing-dsp-overview.html language=enus -->
## TOPIC 00027: Digital Signal Processing (DSP) Overview

- bundle_id: `ni-reconfigurable-oscilloscopes`
- source_path: `digital-signal-processing-dsp-overview.html`
- source_url: https://docs-be.ni.com/bundle/ni-reconfigurable-oscilloscopes/raw/resource/enus/digital-signal-processing-dsp-overview.html
- document_id: `ni-reconfigurable-oscilloscopes`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use this instrument design library to digitally process I/Q data. This instrument design library contains LabVIEW FPGA VIs. These VIs contain functionality that is typically found in Digital Downconverters (DDCs) and Digital Upconverters (DUCs). These VIs also perform DSP for the digital correction

### Digital Signal Processing (DSP) Overview

Use this instrument design library to digitally process I/Q data. This instrument design library
 contains LabVIEW FPGA VIs. These VIs contain functionality that is typically found in
 Digital Downconverters (DDCs) and Digital Upconverters (DUCs). These VIs also perform
 DSP for the digital correction of analog imperfections in the system. For devices that
 support two samples per cycle, you can configure this instrument design library to
 process two I/Q data samples per cycle. You can use this instrument design library to
 perform the following functions:

#### DDC and DUC Functionality

Fractional decimation

Fractional interpolation

Frequency shift

#### Digital Correction Functionality

Digital gain

Digital offset

Equalization

I/Q impairments

This instrument design library also includes the Power Level
 Trigger VI and several data type conversion VIs. Data type conversion
 VIs simplify the interfacing between instrument design VIs and FPGA I/O nodes. Refer
 to the LabVIEW context help of the DSP VIs for more detailed information about the
 library interface.

Parent topic:

LabVIEW Instrument Design Libraries for Reconfigurable Oscilloscopes

<!--NI_TOPIC bundle=ni-reconfigurable-oscilloscopes path=digital-signal-processing-fpga-vis.html language=enus -->
## TOPIC 00028: Digital Signal Processing FPGA VIs

- bundle_id: `ni-reconfigurable-oscilloscopes`
- source_path: `digital-signal-processing-fpga-vis.html`
- source_url: https://docs-be.ni.com/bundle/ni-reconfigurable-oscilloscopes/raw/resource/enus/digital-signal-processing-fpga-vis.html
- document_id: `ni-reconfigurable-oscilloscopes`
- page_type: `leaf`
- content_type: `concept`
- source_description: Digital Gain - Real - 1 spc.viDigitally controls the data in signal levels. This VI must be used in a single-cycle timed loop.This VI provides the following functionality: data out ≤ data in × gain where "×" represents scalar multiplication. Data type This VI automatically adapts to real

### Digital Signal Processing FPGA VIs

#### Digital Gain - Real - 1 spc.vi

Digitally controls the data in signal
 levels. This VI must be used in a single-cycle timed
 loop.

This VI provides the following functionality:

data

out

≤

data

in

×

gain

where "×" represents scalar multiplication.

Data type

'data in'[0]

Overflows

data in.overflow

data out.overflow

Reset

TRUE

FALSE

FALSE

TRUE

Pipeline delay

timed loop

Approximate resource usage in a Xilinx Kintex 7

- Slice flip-flops: 50
- Slice LUTs: 80
- Block RAMs (18kb): 0
- DSP48E(1)s: 1

timed loop

[IMAGE alt='image' src='GUID-509D1C91-BA05-40F6-BB42-B8A62927F09C-a5.gif']

#### Digital Gain - Real - 2 spc.vi

Digitally controls the data in signal
 levels. This VI must be used in a single-cycle timed
 loop.

This VI provides the following functionality:

data

out

≤

data

in

×

gain

where "×" represents scalar multiplication.

Data type

'data in'[0]

Overflows

data in.overflow

data out.overflow

Reset

TRUE

FALSE

FALSE

TRUE

Pipeline delay

timed loop

Approximate resource usage in a Xilinx Kintex 7

- Slice flip-flops: 130
- Slice LUTs: 170
- Block RAMs (18kb): 0
- DSP48E(1)s: 2

timed loop

[IMAGE alt='image' src='GUID-41E804D5-56B3-4714-BDF7-57F991D3B0A0-a5.gif']

#### Digital Gain - Real - 4 spc.vi

Digitally controls the data in signal
 levels. This VI must be used in a single-cycle timed
 loop.

This VI provides the following functionality:

data

out

≤

data

in

×

gain

where "×" represents scalar multiplication.

Data type

'data in'[0]

Overflows

data in.overflow

data out.overflow

Reset

TRUE

FALSE

FALSE

TRUE

Pipeline delay

timed loop

Approximate resource usage in a Xilinx Kintex 7

- Slice flip-flops: 260
- Slice LUTs: 320
- Block RAMs (18kb): 0
- DSP48E(1)s: 4

timed loop

[IMAGE alt='image' src='GUID-6801A0CB-DA06-484D-84A3-86DC0159E6AA-a5.gif']

#### Digital Gain - Real - 8 spc.vi

Digitally controls the data in signal
 levels. This VI must be used in a single-cycle timed
 loop.

This VI provides the following functionality:

data

out

≤

data

in

×

gain

where "×" represents scalar multiplication.

Data type

'data in'[0]

Overflows

data in.overflow

data out.overflow

Reset

TRUE

FALSE

FALSE

TRUE

Pipeline delay

timed loop

Approximate resource usage in a Xilinx Kintex 7

- Slice flip-flops: 510
- Slice LUTs: 670
- Block RAMs (18kb): 0
- DSP48E(1)s: 8

timed loop

[IMAGE alt='image' src='GUID-A0D2131F-E887-4E84-B7C4-0C0C565BFF1E-a5.gif']

#### Digital Gain - Real - 16 spc.vi

Digitally controls the data in signal
 levels. This VI must be used in a single-cycle timed
 loop.

This VI provides the following functionality:

data

out

≤

data

in

×

gain

where "×" represents scalar multiplication.

Data type

'data in'[0]

Overflows

data in.overflow

data out.overflow

Reset

TRUE

FALSE

FALSE

TRUE

Pipeline delay

timed loop

Approximate resource usage in a Xilinx Kintex 7

- Slice flip-flops: 1360
- Slice LUTs: 1310
- Block RAMs (18kb): 0
- DSP48E(1)s: 16

timed loop

[IMAGE alt='image' src='GUID-C1AA6225-5162-4BC1-83EE-6B200CF70BBC-a5.gif']

#### Digital Gain - 1 spc.vi

Digitally controls the I and Q signal levels.
 This VI must be used in a single-cycle timed loop.

This
 VI provides the following functionality:

data

out

.

I

≤

data

in

.

I

×

gain

I

data

out

.

Q

≤

data

in

.

Q

×

gain

Q

where "×" represents scalar multiplication.

Data type

'data in'[0]

Overflows

data in.overflow

data out.overflow

Reset

TRUE

FALSE

FALSE

TRUE

Pipeline delay

timed loop

Approximate resource usage in a Xilinx Virtex-5 or Virtex-6

- Slice flip-flops: 100
- Slice LUTs: 150
- Block RAMs (18kb): 0
- DSP48E(1)s: 2

timed loop

[IMAGE alt='image' src='GUID-11821D36-7DB1-4116-9EE5-2E769C08D3C2-a5.gif']

#### Digital Gain - 2 spc.vi

Digitally controls the I and Q signal levels. This VI must be used in a single-cycle
 timed loop.

This VI provides the following functionality:

data

out

.

I

≤

data

in

.

I

×

gain

I

data

out

.

Q

≤

data

in

.

Q

×

gain

Q

where "×" represents scalar multiplication.

Data type

'data in'[0]

Overflows

data in.overflow

data out.overflow

Reset

TRUE

FALSE

FALSE

TRUE

Pipeline delay

timed loop

Approximate resource usage in a Xilinx Virtex-5 or Virtex-6

- Slice flip-flops: 250
- Slice LUTs: 325
- Block RAMs (18kb): 0
- DSP48E(1)s: 4

timed loop

[IMAGE alt='image' src='GUID-1A86BA65-861B-435E-8907-2C860BE2869C-a5.gif']

#### Digital Gain - 4 spc.vi

Digitally controls the I and Q signal levels. This VI must be used in a single-cycle
 timed loop.

This VI provides the following functionality:

data

out

.

I

≤

data

in

.

I

×

gain

I

data

out

.

Q

≤

data

in

.

Q

×

gain

Q

where "×" represents scalar multiplication.

Data type

'data in'[0]

Overflows

data in.overflow

data out.overflow

Reset

TRUE

FALSE

FALSE

TRUE

Pipeline delay

timed loop

Approximate resource usage in a Xilinx Virtex-5 or Virtex-6

- Slice flip-flops: 500
- Slice LUTs: 650
- Block RAMs (18kb): 0
- DSP48E(1)s: 8

timed loop

[IMAGE alt='image' src='GUID-9BEE221D-4E3D-4974-91DB-9B4A1FEE584F-a5.gif']

#### Digital Gain - 8 spc.vi

Digitally controls the I and Q signal levels. This VI must be used in a single-cycle
 timed loop.

This VI provides the following functionality:

data

out

.

I

≤

data

in

.

I

×

gain

I

data

out

.

Q

≤

data

in

.

Q

×

gain

Q

where "×" represents scalar multiplication.

Data type

'data in'[0]

Overflows

data in.overflow

data out.overflow

Reset

TRUE

FALSE

FALSE

TRUE

Pipeline delay

timed loop

Approximate resource usage in a Xilinx Virtex-5 or Virtex-6

- Slice flip-flops: 950
- Slice LUTs: 1275
- Block RAMs (18kb): 0
- DSP48E(1)s: 16

timed loop

[IMAGE alt='image' src='GUID-5DB05256-555E-4DFA-9C7F-8654DDAB6502-a5.gif']

#### Digital Gain - 16 spc.vi

Digitally controls the I and Q signal levels. This VI must be used in a single-cycle
 timed loop.

This VI provides the following functionality:

data

out

.

I

≤

data

in

.

I

×

gain

I

data

out

.

Q

≤

data

in

.

Q

×

gain

Q

where "×" represents scalar multiplication.

Data type

'data in'[0]

Overflows

data in.overflow

data out.overflow

Reset

TRUE

FALSE

FALSE

TRUE

Pipeline delay

timed loop

Approximate resource usage in a Xilinx Virtex-5 or Virtex-6

- Slice flip-flops: 2550
- Slice LUTs: 2550
- Block RAMs (18kb): 0
- DSP48E(1)s: 32

timed loop

[IMAGE alt='image' src='GUID-B5B2DD1E-CC94-4287-AA9F-F30D8ACA238C-a5.gif']

#### Digital Offset - Real - 1
 spc.vi

Digitally controls the data in offset. This VI must be used in a single-cycle
 timed loop.

This VI provides the following
 functionality:

data

out

≤

data

in

+

offset

Data type

'data in'[0]

Overflows

data in.overflow

data out.overflow

Reset

TRUE

FALSE

FALSE

TRUE

Pipeline delay

timed loop

Approximate resource usage in a Xilinx Kintex 7

- Slice flip-flops: 50
- Slice LUTs: 60
- Block RAMs (18kb): 0
- DSP48E(1)s: 0

timed loop

[IMAGE alt='image' src='GUID-42C42E4D-9045-4C05-93B8-A5D7D97346FA-a5.gif']

#### Digital Offset - Real - 2
 spc.vi

Digitally controls the data in offset. This VI must be used in a single-cycle
 timed loop.

This VI provides the following
 functionality:

data

out

≤

data

in

+

offset

Data type

'data in'[0]

Overflows

data in.overflow

data out.overflow

Reset

TRUE

FALSE

FALSE

TRUE

Pipeline delay

timed loop

Approximate resource usage in a Xilinx Kintex 7

- Slice flip-flops: 90
- Slice LUTs: 100
- Block RAMs (18kb): 0
- DSP48E(1)s: 0

timed loop

[IMAGE alt='image' src='GUID-29794428-8993-4656-AE3C-250952B8F374-a5.gif']

#### Digital Offset - Real - 4
 spc.vi

Digitally controls the data in offset. This VI must be used in a single-cycle
 timed loop.

This VI provides the following
 functionality:

data

out

≤

data

in

+

offset

Data type

'data in'[0]

Overflows

data in.overflow

data out.overflow

Reset

TRUE

FALSE

FALSE

TRUE

Pipeline delay

timed loop

Approximate resource usage in a Xilinx Kintex 7

- Slice flip-flops: 170
- Slice LUTs: 200
- Block RAMs (18kb): 0
- DSP48E(1)s: 0

timed loop

[IMAGE alt='image' src='GUID-B4A468AC-D86C-424C-956B-06FFD5B19EC0-a5.gif']

#### Digital Offset - Real - 8
 spc.vi

Digitally controls the data in offset. This VI must be used in a single-cycle
 timed loop.

This VI provides the following
 functionality:

data

out

≤

data

in

+

offset

Data type

'data in'[0]

Overflows

data in.overflow

data out.overflow

Reset

TRUE

FALSE

FALSE

TRUE

Pipeline delay

timed loop

Approximate resource usage in a Xilinx Kintex 7

- Slice flip-flops: 330
- Slice LUTs: 390
- Block RAMs (18kb): 0
- DSP48E(1)s: 0

timed loop

[IMAGE alt='image' src='GUID-1BFECD3E-E071-4A23-BE97-D81354B99182-a5.gif']

#### Digital Offset - Real - 16
 spc.vi

Digitally controls the data in offset. This VI must be used in a single-cycle
 timed loop.

This VI provides the following
 functionality:

data

out

≤

data

in

+

offset

Data type

'data in'[0]

Overflows

data in.overflow

data out.overflow

Reset

TRUE

FALSE

FALSE

TRUE

Pipeline delay

timed loop

Approximate resource usage in a Xilinx Kintex 7

- Slice flip-flops: 650
- Slice LUTs: 770
- Block RAMs (18kb): 0
- DSP48E(1)s: 0

timed loop

[IMAGE alt='image' src='GUID-59F3FDC9-DFC2-4D27-BCA6-690E92517C87-a5.gif']

#### Digital Offset - 1 spc.vi

Digitally controls the I and Q offset. This VI must be used in a single-cycle
 timed loop.

This VI provides the following
 functionality:

data

out

.

I

≤

data

in

.

I

+

offset

I

,

data

out

.

Q

≤

data

in

.

Q

+

offset

Q

Data type

'data in'[0]

Overflows

data in.overflow

data out.overflow

Reset

TRUE

FALSE

FALSE

TRUE

Pipeline delay

timed loop

Approximate resource usage in a Xilinx Virtex-5 or Virtex-6

- Slice flip-flops: 100
- Slice LUTs: 125
- Block RAMs (18kb): 0
- DSP48E(1)s: 0

timed loop

[IMAGE alt='image' src='GUID-6DC1BFB2-4DB9-493D-8313-7C90DD17AD63-a5.gif']

#### Digital Offset - 2 spc.vi

Digitally controls the I and Q offset. This VI must be used in a single-cycle
 timed loop.

This VI provides the following
 functionality:

data

out

.

I

≤

data

in

.

I

+

offset

I

,

data

out

.

Q

≤

data

in

.

Q

+

offset

Q

Data type

'data in'[0]

Overflows

data in.overflow

data out.overflow

Reset

TRUE

FALSE

FALSE

TRUE

Pipeline delay

timed loop

Approximate resource usage in a Xilinx Virtex-5 or Virtex-6

- Slice flip-flops: 175
- Slice LUTs: 250
- Block RAMs (18kb): 0
- DSP48E(1)s: 0

timed loop

[IMAGE alt='image' src='GUID-C7F8AAFE-A259-402C-871F-86F4449136E1-a5.gif']

#### Digital Offset - 4 spc.vi

Digitally controls the I and Q offset. This VI must be used in a single-cycle
 timed loop.

This VI provides the following
 functionality:

data

out

.

I

≤

data

in

.

I

+

offset

I

,

data

out

.

Q

≤

data

in

.

Q

+

offset

Q

Data type

'data in'[0]

Overflows

data in.overflow

data out.overflow

Reset

TRUE

FALSE

FALSE

TRUE

Pipeline delay

timed loop

Approximate resource usage

- Slice flip-flops: 325
- Slice LUTs: 450
- Block RAMs (18kb): 0
- DSP48E(1)s: 0

timed loop

[IMAGE alt='image' src='GUID-A881B00E-7361-4538-8CF3-D7B5A0B9A2E4-a5.gif']

#### Digital Offset - 8 spc.vi

Digitally controls the I and Q offset. This VI must be used in a single-cycle
 timed loop.

This VI provides the following
 functionality:

data

out

.

I

≤

data

in

.

I

+

offset

I

,

data

out

.

Q

≤

data

in

.

Q

+

offset

Q

Data type

'data in'[0]

Overflows

data in.overflow

data out.overflow

Reset

TRUE

FALSE

FALSE

TRUE

Pipeline delay

timed loop

Approximate resource usage in a Xilinx Virtex-5 or Virtex-6

- Slice flip-flops: 625
- Slice LUTs: 900
- Block RAMs (18kb): 0
- DSP48E(1)s: 0

timed loop

[IMAGE alt='image' src='GUID-7A9C64B4-F303-443D-A526-866AC31ECE46-a5.gif']

#### Digital Offset - 16 spc.vi

Digitally controls the I and Q offset. This VI must be used in a single-cycle
 timed loop.

This VI provides the following
 functionality:

data

out

.

I

≤

data

in

.

I

+

offset

I

,

data

out

.

Q

≤

data

in

.

Q

+

offset

Q

Data type

'data in'[0]

Overflows

data in.overflow

data out.overflow

Reset

TRUE

FALSE

FALSE

TRUE

Pipeline delay

timed loop

Approximate resource usage in a Xilinx Virtex-5 or Virtex-6

- Slice flip-flops: 1250
- Slice LUTs: 1800
- Block RAMs (18kb): 0
- DSP48E(1)s: 0

timed loop

[IMAGE alt='image' src='GUID-8C69FC3D-A092-476B-8E16-EE1A378588B6-a5.gif']

#### Equalization - 11 cps - 1x oc - 32
 coef.vi

Equalizes the analog response of a device. This VI implements four FIR filters as a
 matrix operation, and can also be used as a general purpose complex filter. This VI
 must be used in a single-cycle timed loop.

This VI
 provides the following functionality:

data

out

.

I

≤

data

in

.

I

×

I

Inline

-

data

in

.

Q

×

Q

Cross

,

data

out

.

Q

≤

data

in

.

Q

×

Q

Inline

+

data

in

.

I

×

I

Cross

where "×" represents convolution, and I Inline, Q Cross, Q Inline,
 and I Cross are the sets of coefficients for the four filters.

Data type

'data in'[0]

Throughput

timed loop

Overflows

data in.overflow

data out.overflow

Reset

TRUE

FALSE

FALSE

TRUE

Programming

0

For 1 sample per cycle, load the coefficients in
 natural order (0, 1, 2, 3 ...)

Complete the following steps to
 load the coefficients:

1. Select the filter to load using filter select.
2. Set coef load to TRUE and then
 FALSE , to begin the load sequence.
3. For each coefficient: write a coefficient to coef data and set coef
 write TRUE , then set coef write
 FALSE .

The new coefficients are applied automatically while they are being
 written. For the most consistent output behavior, hold the reset input
 TRUE while loading the coefficients.

You can
 use the Digital Filter Design Toolkit to calculate coefficients for your
 desired filtering application.

Pipeline delay

timed loop

Approximate resource usage in a Xilinx Virtex-6

- Slice flip-flops: 1000
- Slice LUTs: 1200
- Block RAMs (18kb): 0
- DSP48E(1)s: 12

timed loop

[IMAGE alt='image' src='GUID-052ACCA5-8F40-41B1-8BA5-0EE1D0FFE5CB-a5.gif']

#### Equalization - 1 spc - 3x oc - 33
 coef.vi

Equalizes the analog response of a device. This VI implements four FIR filters as a
 matrix operation, and can also be used as a general purpose complex filter. This VI
 must be used in a single-cycle timed loop.

This VI
 provides the following functionality:

data

out

.

I

≤

data

in

.

I

×

I

Inline

-

data

in

.

Q

×

Q

Cross

,

data

out

.

Q

≤

data

in

.

Q

×

Q

Inline

+

data

in

.

I

×

I

Cross

where "×" represents convolution, and I Inline, Q Cross, Q Inline,
 and I Cross are the sets of coefficients for the four filters.

Data type

'data in'[0]

Over-clocking

timed loop

timed loop

Overflows

data in.overflow

data out.overflow

Reset

TRUE

FALSE

FALSE

TRUE

Programming

0

For 1 sample per cycle, load the coefficients in
 natural order (0, 1, 2, 3 ...)

Complete the following steps to
 load the coefficients:

1. Select the filter to load using filter select.
2. Set coef load to TRUE and then
 FALSE , to begin the load sequence.
3. For each coefficient: write a coefficient to coef data and set coef
 write TRUE , then set coef write
 FALSE .

The new coefficients are applied automatically while they are being
 written. For the most consistent output behavior, hold the reset input
 TRUE while loading the coefficients.

You can
 use the Digital Filter Design Toolkit to calculate coefficients for your
 desired filtering application.

Pipeline delay

timed loop

Approximate resource usage in a Xilinx Virtex-6

- Slice flip-flops: 2850
- Slice LUTs: 1300
- Block RAMs (18kb): 0
- DSP48E(1)s: 52

timed loop

[IMAGE alt='image' src='GUID-052ACCA5-8F40-41B1-8BA5-0EE1D0FFE5CB-a5.gif']

#### Equalization - 2 spc - 3x oc - 48
 coef.vi

Equalizes the analog response of a device. This VI implements four FIR filters as a
 matrix operation, and can also be used as a general purpose complex filter. This VI
 must be used in a single-cycle timed loop.

This VI
 provides the following functionality:

data

out

.

I

≤

data

in

.

I

×

I

Inline

-

data

in

.

Q

×

Q

Cross

,

data

out

.

Q

≤

data

in

.

Q

×

Q

Inline

+

data

in

.

I

×

I

Cross

where "×" represents convolution, and I Inline, Q Cross, Q Inline,
 and I Cross are the sets of coefficients for the four filters.

Data type

'data in'[0]

Over-clocking

timed loop

timed loop

Overflows

data in.overflow

data out.overflow

Reset

TRUE

FALSE

FALSE

TRUE

Programming

0

For multiple samples per cycle, load the coefficients
 with an SPC step size, and wrap back to the beginning when you reach the
 end.

For example, four samples per cycle and 32 coefficients uses
 the following order: 0, 4, 8, 12, 16, 20, 24, 28, 1, 5, 9, 13, 17, 21,
 25, 29, 2, 6, 10, 14, 18, 22, 26, 30, 3, 7, 11, 15, 19, 23, 27,
 31

Complete the following steps to load the coefficients:

1. Select the filter to load using filter select.
2. Set coef load to TRUE and then
 FALSE , to begin the load sequence.
3. For each coefficient: write a coefficient to coef data and set coef
 write TRUE , then set coef write
 FALSE .

The new coefficients are applied automatically while they are being
 written. For the most consistent output behavior, hold the reset input
 TRUE while loading the coefficients.

You can
 use the Digital Filter Design Toolkit to calculate coefficients for your
 desired filtering application.

Pipeline delay

timed loop

Approximate resource usage in a Xilinx Virtex-6

- Slice flip-flops: 8100
- Slice LUTs: 3650
- Block RAMs (18kb): 0
- DSP48E(1)s: 144

timed loop

[IMAGE alt='image' src='GUID-94A20C7A-5774-458F-AED7-843D304DA2FD-a5.gif']

#### Equalization - 4 spc - 2x oc - 32
 coef.vi

Equalizes the analog response of a device. This VI implements four FIR filters as a
 matrix operation, and can also be used as a general purpose complex filter. This VI
 must be used in a single-cycle timed loop.

This VI
 provides the following functionality:

data

out

.

I

≤

data

in

.

I

×

I

Inline

-

data

in

.

Q

×

Q

Cross

,

data

out

.

Q

≤

data

in

.

Q

×

Q

Inline

+

data

in

.

I

×

I

Cross

where "×" represents convolution, and I Inline, Q Cross, Q Inline,
 and I Cross are the sets of coefficients for the four filters.

Data type

'data in'[0]

Over-clocking

timed loop

timed loop

Overflows

data in.overflow

data out.overflow

Reset

TRUE

FALSE

FALSE

TRUE

Programming

0

For multiple samples per cycle, load the coefficients
 with an SPC step size, and wrap back to the beginning when you reach the
 end.

For example, four samples per cycle and 32 coefficients uses
 the following order: 0, 4, 8, 12, 16, 20, 24, 28, 1, 5, 9, 13, 17, 21,
 25, 29, 2, 6, 10, 14, 18, 22, 26, 30, 3, 7, 11, 15, 19, 23, 27,
 31

Complete the following steps to load the coefficients:

1. Select the filter to load using filter select.
2. Set coef load to TRUE and then
 FALSE , to begin the load sequence.
3. For each coefficient: write a coefficient to coef data and set coef
 write TRUE , then set coef write
 FALSE .

The new coefficients are applied automatically while they are being
 written. For the most consistent output behavior, hold the reset input
 TRUE while loading the coefficients.

You can
 use the Digital Filter Design Toolkit to calculate coefficients for your
 desired filtering application.

Pipeline delay

timed loop

Approximate resource usage in a Xilinx Virtex-6

- Slice flip-flops: 16500
- Slice LUTs: 7550
- Block RAMs (18kb): 0
- DSP48E(1)s: 288

timed loop

[IMAGE alt='image' src='GUID-F55D86AF-5879-429D-8142-C92B01B813AE-a5.gif']

#### Equalization - 8 spc - 2x oc - 32
 coef.vi

Equalizes the analog response of a device. This VI implements four FIR filters as a
 matrix operation, and can also be used as a general purpose complex filter. This VI
 must be used in a single-cycle timed loop.

This VI
 provides the following functionality:

data

out

.

I

≤

data

in

.

I

×

I

Inline

-

data

in

.

Q

×

Q

Cross

,

data

out

.

Q

≤

data

in

.

Q

×

Q

Inline

+

data

in

.

I

×

I

Cross

where "×" represents convolution, and I Inline, Q Cross, Q Inline,
 and I Cross are the sets of coefficients for the four filters.

Data type

'data in'[0]

Over-clocking

timed loop

timed loop

Overflows

data in.overflow

data out.overflow

Reset

TRUE

FALSE

FALSE

TRUE

Programming

0

For multiple samples per cycle, load the coefficients
 with an SPC step size, and wrap back to the beginning when you reach the
 end.

For example, four samples per cycle and 32 coefficients uses
 the following order: 0, 4, 8, 12, 16, 20, 24, 28, 1, 5, 9, 13, 17, 21,
 25, 29, 2, 6, 10, 14, 18, 22, 26, 30, 3, 7, 11, 15, 19, 23, 27,
 31

Complete the following steps to load the coefficients:

1. Select the filter to load using filter select.
2. Set coef load to TRUE and then
 FALSE , to begin the load sequence.
3. For each coefficient: write a coefficient to coef data and set coef
 write TRUE , then set coef write
 FALSE .

The new coefficients are applied automatically while they are being
 written. For the most consistent output behavior, hold the reset input
 TRUE while loading the coefficients.

You can
 use the Digital Filter Design Toolkit to calculate coefficients for your
 desired filtering application.

Pipeline delay

timed loop

Approximate resource usage in a Xilinx Virtex-6

- Slice flip-flops: 35500
- Slice LUTs: 16900
- Block RAMs (18kb): 0
- DSP48E(1)s: 576

timed loop

[IMAGE alt='image' src='GUID-F55D86AF-5879-429D-8142-C92B01B813AE-a5.gif']

#### Halfband Decimator - IQ - 4 CPS -
 2x OC.vi

Decimates the input signal data in by a factor of two using a low-pass halfband FIR
 filter implementation. This VI must be used in a single-cycle timed
 loop.

Data type

'data in'[0]

Throughput

timed loop

ready for
 input

input valid

Over-clocking

timed loop

timed loop

Overflows

data in.overflow

data out.overflow

Reset

TRUE

FALSE

ready for input

output valid

FALSE

input valid

TRUE

Pipeline delay

input valid

output valid

timed
 loop

Group delay

Performance

- Decimation Factor: 2
- Anti-alias low-pass filter passband ripple (to 0.4 × output data
 rate): 0 dB to -0.01 dB
- Anti-alias low-pass filter stopband rejection (from 0.6 × output
 data rate): > 85 dB

Approximate resource usage in a Xilinx Virtex-6

- Slice flip-flops: 550
- Slice LUTs: 350
- Block RAMs (18kb): 0
- DSP48E(1)s: 2

timed loop

[IMAGE alt='image' src='GUID-08FBD5C9-57D9-45CB-9B41-D1F527E49328-a5.gif']

#### Halfband Decimator - IQ - 2 CPS -
 2x OC.vi

Decimates the input signal data in by a factor of two using a low-pass halfband FIR
 filter implementation. This VI must be used in a single-cycle timed
 loop.

Data type

'data in'[0]

Throughput

timed loop

Over-clocking

timed loop

timed loop

Overflows

data in.overflow

data out.overflow

Reset

TRUE

FALSE

FALSE

TRUE

Pipeline delay

timed loop

Group delay

Performance

- Decimation Factor: 2
- Anti-alias low-pass filter passband ripple (to 0.4 × output data
 rate): 0 dB to -0.01 dB
- Anti-alias low-pass filter stopband rejection (from 0.6 × output
 data rate): > 85 dB

Approximate resource usage in a Xilinx Virtex-6

- Slice flip-flops: 800
- Slice LUTs: 500
- Block RAMs (18kb): 0
- DSP48E(1)s: 4

timed loop

[IMAGE alt='image' src='GUID-B6B915C3-848E-475E-B02F-3B5C63E36501-a5.gif']

#### Halfband Decimator - IQ - 1 SPC -
 2x OC.vi

Decimates the input signal data in by a factor of two using a low-pass halfband FIR
 filter implementation. This VI must be used in a single-cycle timed
 loop.

Data type

'data in'[0]

Over-clocking

timed loop

timed loop

Overflows

data in.overflow

data out.overflow

Reset

TRUE

FALSE

FALSE

TRUE

Pipeline delay

timed loop

Group delay

Performance

- Decimation Factor: 2
- Anti-alias low-pass filter passband ripple (to 0.4 × output data
 rate): 0 dB to -0.01 dB
- Anti-alias low-pass filter stopband rejection (from 0.6 × output
 data rate): > 85 dB

Approximate resource usage in a Xilinx Virtex-6

- Slice flip-flops: 1200
- Slice LUTs: 800
- Block RAMs (18kb): 0
- DSP48E(1)s: 8

timed loop

[IMAGE alt='image' src='GUID-60EF3891-7FA8-4911-B62B-0999286CA57B-a5.gif']

#### Halfband Decimator - IQ - 2 spc -
 2x OC.vi

Decimates the input signal data in by a factor of two using a low-pass halfband FIR
 filter implementation. This VI must be used in a single-cycle timed
 loop.

Data type

'data in'[0]

Over-clocking

timed loop

timed loop

Overflows

data in.overflow

data out.overflow

Reset

TRUE

FALSE

FALSE

TRUE

Pipeline delay

timed loop

Group delay

Performance

- Decimation Factor: 2
- Anti-alias low-pass filter passband ripple (to 0.4 × output data
 rate): 0 dB to -0.01 dB
- Anti-alias low-pass filter stopband rejection (from 0.6 × output
 data rate): > 85 dB

Approximate resource usage in a Xilinx Virtex-6

- Slice flip-flops: 2000
- Slice LUTs: 1300
- Block RAMs (18kb): 0
- DSP48E(1)s: 16

timed loop

[IMAGE alt='image' src='GUID-54013651-AD47-41AA-BA5B-3452D681DB1B-a5.gif']

#### Halfband Decimator - IQ - 4 spc -
 2x OC.vi

Decimates the input signal data in by a factor of two using a low-pass halfband FIR
 filter implementation. This VI must be used in a single-cycle timed
 loop.

Data type

'data in'[0]

Over-clocking

timed loop

timed loop

Overflows

data in.overflow

data out.overflow

Reset

TRUE

FALSE

FALSE

TRUE

Pipeline delay

timed loop

Group delay

Performance

- Decimation Factor: 2
- Anti-alias low-pass filter passband ripple (to 0.4 × output data
 rate): 0 dB to -0.01 dB
- Anti-alias low-pass filter stopband rejection (from 0.6 × output
 data rate): > 85 dB

Approximate resource usage in a Xilinx Virtex-6

- Slice flip-flops: 3800
- Slice LUTs:: 2500
- Block RAMs (18kb): 0
- DSP48E(1)s: 32

timed loop

[IMAGE alt='image' src='GUID-4C81E270-0E42-4D97-9F77-E0E9C2DC3E55-a5.gif']

#### Halfband Decimator - IQ - 8 spc -
 2x OC.vi

Decimates the input signal data in by a factor of two using a low-pass halfband FIR
 filter implementation. This VI must be used in a single-cycle timed
 loop.

Data type

'data in'[0]

Over-clocking

timed loop

timed loop

Overflows

data in.overflow

data out.overflow

Reset

TRUE

FALSE

FALSE

TRUE

Pipeline delay

timed loop

Group delay

Performance

- Decimation Factor: 2
- Anti-alias low-pass filter passband ripple (to 0.4 × output data
 rate): 0 dB to -0.01 dB
- Anti-alias low-pass filter stopband rejection (from 0.6 × output
 data rate): > 85 dB

Approximate resource usage in a Xilinx Virtex-6

- Slice flip-flops: 7400
- Slice LUTs: 4800
- Block RAMs (18kb): 0
- DSP48E(1)s: 64

timed loop

[IMAGE alt='image' src='GUID-EB869154-4F78-42B5-9032-77105E6D65E6-a5.gif']

#### Halfband Decimator - IQ - 16 spc -
 2x OC.vi

Decimates the input signal data in by a factor of two using a low-pass halfband FIR
 filter implementation. This VI must be used in a single-cycle timed
 loop.

Data type

'data in'[0]

Over-clocking

timed loop

timed loop

Overflows

data in.overflow

data out.overflow

Reset

TRUE

FALSE

FALSE

TRUE

Pipeline delay

timed loop

Group delay

Performance

- Decimation Factor: 2
- Anti-alias low-pass filter passband ripple (to 0.4 × output data
 rate): 0 dB to -0.01 dB
- Anti-alias low-pass filter stopband rejection (from 0.6 × output
 data rate): > 85 dB

Approximate resource usage in a Xilinx Virtex-6

- Slice flip-flops: 14500
- Slice LUTs:: 9300
- Block RAMs (18kb): 0
- DSP48E(1)s: 128

timed loop

[IMAGE alt='image' src='GUID-BB73756E-02F0-4DF8-8D86-6A4DF03E3223-a5.gif']

#### Integer Decimator - real - NAP - 2
 spc.vi

Decimates the input signal data in by an integer decimation factor, without filtering
 for alias protection. This VI must be used in a single-cycle timed
 loop.

Data type

'data in'[0]

Decimation factor

0

65,535

Reset

TRUE

FALSE

FALSE

TRUE

Output calculated

FALSE

TRUE

data in[0]

Pipeline delay

timed loop

Approximate resource usage in a Xilinx Kintex 7

- Slice flip-flops: 151
- Slice LUTs: 99
- Block RAMs (18kb): 0
- DSP48E(1)s: 0

timed loop

[IMAGE alt='image' src='GUID-C4BE4C17-BEE2-4CB6-8604-E929D2700E66-a5.gif']

#### Fractional Decimator - 10 cps - 1x
 oc.vi

Decimates the input signal data in according to the output sample rate and delay
 using an FIR filter implementation. This VI must be used in a single-cycle
 timed loop.

Data type

'data in'[0]

Throughput

timed loop

Data rate

- The output sample rate input may be in the range of [1.52588E-5 to
 1.0], corresponding to decimation factors of [65,536.0 down to
 1.0].
- Decimation factor = 1 / output sample rate
- Output data rate (Hz) = input data rate (Hz) × output sample
 rate
- Input data rate = SCTL clock frequency × SPC × fraction of cycles on
 which input valid is asserted
- Example: If SCTL is clocked at 120 MHz, one SPC is used, and input
 valid is asserted every other cycle, then input data rate = 60
 MHz.

Delay

- The delay input delays the input data. Valid range: [-0.5 to
 +0.5]
- Delay (seconds) = delay / input data rate (Hz)

Overflows

data in.overflow

data out.overflow

Reset

TRUE

FALSE

FALSE

TRUE

Pipeline delay

Group delay of the anti-alias filter

- Decimation factor ≤ 16: group delay = 15 output samples
- 16 < decimation factor ≤ 128: group delay = (256 / decimation
 factor) + 15 output samples
- 128 < decimation factor ≤ 2,048: group delay = (2,056 /
 decimation factor) + 15 output samples
- 2,048 < decimation factor ≤ 32,768: group delay = (34,624 /
 decimation factor) + 15 output samples
- 32,768 < decimation factor ≤ 65,536: group delay = (65,344 /
 decimation factor) + 15 output samples

Performance

- Decimation Range: [1.0 to 65,536.0]
- Output Sample Rate Resolution: 7.11e-15 × input data rate (Hz)
- Delay Range: [-0.5 to +0.5] (corresponds to -0.5 to +0.5 input data
 rate periods)
- Delay Resolution: 1.53e-5 / input data rate (Hz)
- Anti-alias filter passband ripple (to 0.4 × output data rate): 0 dB
 to -0.01 dB
- Anti-alias filter stopband rejection (from 0.6 × output data rate):
 > 85 dB

Approximate resource usage in a Xilinx Virtex-6

- Slice flip-flops: 2800
- Slice LUTs: 6100
- Block RAMs (18kb): 25
- DSP48E(1)s: 34

timed loop

[IMAGE alt='image' src='GUID-5AFDBBEC-550F-4BBB-993A-2A9C435F15A4-a5.gif']

#### Fractional Decimator - 1 spc - 2x
 oc.vi

Decimates the input signal data in according to the output sample rate and delay
 using an FIR filter implementation. This VI must be used in a single-cycle
 timed loop.

Data type

'data in'[0]

Over-clocking

timed loop

timed loop

Data rate

- The output sample rate input may be in the range of [1.52588E-5 to
 1.0], corresponding to decimation factors of [65,536.0 down to
 1.0].
- Decimation factor = 1 / output sample rate
- Output data rate (Hz) = input data rate (Hz) × output sample
 rate
- Input data rate = SCTL clock frequency × SPC × fraction of cycles on
 which input valid is asserted
- Example: If SCTL is clocked at 120 MHz, one SPC is used, and input
 valid is asserted every other cycle, then input data rate = 60
 MHz.

Delay

- The delay input delays the input data. Valid range: [-0.5 to
 +0.5]
- Delay (seconds) = delay / input data rate (Hz)

Overflows

data in.overflow

data out.overflow

Reset

TRUE

FALSE

FALSE

TRUE

Pipeline delay

Group delay of the anti-alias filter

- Decimation factor ≤ 16: group delay = 15 output samples
- 16 < decimation factor ≤ 128: group delay = (256 / decimation
 factor) + 15 output samples
- 128 < decimation factor ≤ 2,048: group delay = (2,056 /
 decimation factor) + 15 output samples
- 2,048 < decimation factor ≤ 32,768: group delay = (34,624 /
 decimation factor) + 15 output samples
- 32,768 < decimation factor ≤ 65,536: group delay = (65,344 /
 decimation factor) + 15 output samples

Performance

- Decimation Range: [1.0 to 65,536.0]
- Output Sample Rate Resolution: 7.11e-15 × input data rate (Hz)
- Delay Range: [-0.5 to +0.5] (corresponds to -0.5 to +0.5 input data
 rate periods)
- Delay Resolution: 1.53e-5 / input data rate (Hz)
- Anti-alias filter passband ripple (to 0.4 × output data rate): 0 dB
 to -0.01 dB
- Anti-alias filter stopband rejection (from 0.6 × output data rate):
 > 85 dB

Approximate resource usage in a Xilinx Virtex-6

- Slice flip-flops: 10300
- Slice LUTs: 6100
- Block RAMs (18kb): 77
- DSP48E(1)s: 72

timed loop

[IMAGE alt='image' src='GUID-B791E3BD-ECA3-432C-81D0-FD236F4E1D32-a5.gif']

#### Fractional Decimator - 1 spc - 3x
 oc.vi

Decimates the input signal data in according to the output sample rate and delay
 using an FIR filter implementation. This VI must be used in a single-cycle
 timed loop.

Data type

'data in'[0]

Over-clocking

timed loop

timed loop

Data rate

- The output sample rate input may be in the range of [1.52588E-5 to
 1.0], corresponding to decimation factors of [65,536.0 down to
 1.0].
- Decimation factor = 1 / output sample rate
- Output data rate (Hz) = input data rate (Hz) × output sample
 rate
- Input data rate = SCTL clock frequency × SPC × fraction of cycles on
 which input valid is asserted
- Example: If SCTL is clocked at 120 MHz, one SPC is used, and input
 valid is asserted every other cycle, then input data rate = 60
 MHz.

Delay

- The delay input delays the input data. Valid range: [-0.5 to
 +0.5]
- Delay (seconds) = delay / input data rate (Hz)

Overflows

data in.overflow

data out.overflow

Reset

TRUE

FALSE

FALSE

TRUE

Pipeline delay

Group delay of the anti-alias filter

- Decimation factor ≤ 16: group delay = 15 output samples
- 16 < decimation factor ≤ 128: group delay = (256 / decimation
 factor) + 15 output samples
- 128 < decimation factor ≤ 2,048: group delay = (2,056 /
 decimation factor) + 15 output samples
- 2,048 < decimation factor ≤ 32,768: group delay = (34,624 /
 decimation factor) + 15 output samples
- 32,768 < decimation factor ≤ 65,536: group delay = (65,344 /
 decimation factor) + 15 output samples

Performance

- Decimation Range: [1.0 to 65,536.0]
- Output Sample Rate Resolution: 7.11e-15 × input data rate (Hz)
- Delay Range: [-0.5 to +0.5] (corresponds to -0.5 to +0.5 input data
 rate periods)
- Delay Resolution: 1.53e-5 / input data rate (Hz)
- Anti-alias filter passband ripple (to 0.4 × output data rate): 0 dB
 to -0.01 dB
- Anti-alias filter stopband rejection (from 0.6 × output data rate):
 > 85 dB

Approximate resource usage in a Xilinx Virtex-6

- Slice flip-flops: 7700
- Slice LUTs: 4900
- Block RAMs (18kb): 50
- DSP48E(1)s: 50

timed loop

[IMAGE alt='image' src='GUID-A48BD564-8519-49A7-9689-7FB8B880B37F-a5.gif']

#### Fractional Decimator - 2 spc - 2x
 oc.vi

Decimates the input signal data in according to the output sample rate and delay
 using an FIR filter implementation. This VI must be used in a single-cycle
 timed loop.

Data type

'data in'[0]

Over-clocking

timed loop

timed loop

Data rate

- The output sample rate input may be in the range of [1.52588E-5 to
 1.0], corresponding to decimation factors of [65,536.0 down to
 1.0].
- Decimation factor = 1 / output sample rate
- Output data rate (Hz) = input data rate (Hz) × output sample
 rate
- Input data rate = SCTL clock frequency × SPC × fraction of cycles on
 which input valid is asserted
- Example: If SCTL is clocked at 120 MHz, one SPC is used, and input
 valid is asserted every other cycle, then input data rate = 60
 MHz.

Delay

- The delay input delays the input data. Valid range: [-0.5 to
 +0.5]
- Delay (seconds) = delay / input data rate (Hz)

Output calculated

Overflows

data in.overflow

data out.overflow

Reset

TRUE

FALSE

FALSE

TRUE

Pipeline delay

Measuring pipeline delay

1. Select an output sample rate.
2. Assert and deassert reset.
3. Wait for ready for input to return TRUE.
4. Assert input valid and count the number of cycles from the first
 input valid to the first output calculated. The count is equal to
 the pipeline delay for the selected output sample rate.

Group delay of the anti-alias filter

- Decimation factor ≤ 16: group delay = 15 output samples
- 16 < decimation factor ≤ 128: group delay = (256 / decimation
 factor) + 15 output samples
- 128 < decimation factor ≤ 2,048: group delay = (2,056 /
 decimation factor) + 15 output samples
- 2,048 < decimation factor ≤ 32,768: group delay = (34,624 /
 decimation factor) + 15 output samples
- 32,768 < decimation factor ≤ 65,536: group delay = (65,344 /
 decimation factor) + 15 output samples

Performance

- Decimation Range: [1.0 to 65,536.0]
- Output Sample Rate Resolution: 7.11e-15 × input data rate (Hz)
- Delay Range: [-0.5 to +0.5] (corresponds to -0.5 to +0.5 input data
 rate periods)
- Delay Resolution: 1.53e-5 / input data rate (Hz)
- Anti-alias filter passband ripple (to 0.4 × output data rate): 0 dB
 to -0.01 dB
- Anti-alias filter stopband rejection (from 0.6 × output data rate):
 > 85 dB

Approximate resource usage in a Xilinx Virtex-6

- Slice flip-flops: 19228
- Slice LUTs: 12400
- Block RAMs (18kb): 140
- DSP48E(1)s: 140

timed loop

[IMAGE alt='image' src='GUID-92FF3F49-78BD-492A-9994-AC7B7E80DBB0-a5.gif']

#### Fractional Decimator - 2 spc - 3x
 oc.vi

Decimates the input signal data in according to the output sample rate and delay
 using an FIR filter implementation. This VI must be used in a single-cycle
 timed loop.

Data type

'data in'[0]

Over-clocking

timed loop

timed loop

Data rate

- The output sample rate input may be in the range of [1.52588E-5 to
 1.0], corresponding to decimation factors of [65,536.0 down to
 1.0].
- Decimation factor = 1 / output sample rate
- Output data rate (Hz) = input data rate (Hz) × output sample
 rate
- Input data rate = SCTL clock frequency × SPC × fraction of cycles on
 which input valid is asserted
- Example: If SCTL is clocked at 120 MHz, one SPC is used, and input
 valid is asserted every other cycle, then input data rate = 60
 MHz.

Delay

- The delay input delays the input data. Valid range: [-0.5 to
 +0.5]
- Delay (seconds) = delay / input data rate (Hz)

Output calculated

Overflows

data in.overflow

data out.overflow

Reset

TRUE

FALSE

FALSE

TRUE

Pipeline delay

Measuring pipeline delay

1. Select an output sample rate.
2. Assert and deassert reset.
3. Wait for ready for input to return TRUE .
4. Assert input valid and count the number of cycles from the first
 input valid to the first output calculated. The count is equal to
 the pipeline delay for the selected output sample rate.

Group delay of the anti-alias filter

- Decimation factor ≤ 16: group delay = 15 output samples
- 16 < decimation factor ≤ 128: group delay = (256 / decimation
 factor) + 15 output samples
- 128 < decimation factor ≤ 2,048: group delay = (2,056 /
 decimation factor) + 15 output samples
- 2,048 < decimation factor ≤ 32,768: group delay = (34,624 /
 decimation factor) + 15 output samples
- 32,768 < decimation factor ≤ 65,536: group delay = (65,344 /
 decimation factor) + 15 output samples

Performance

- Decimation Range: [1.0 to 65,536.0]
- Output Sample Rate Resolution: 7.11e-15 × input data rate (Hz)
- Delay Range: [-0.5 to +0.5] (corresponds to -0.5 to +0.5 input data
 rate periods)
- Delay Resolution: 1.53e-5 / input data rate (Hz)
- Anti-alias filter passband ripple (to 0.4 × output data rate): 0 dB
 to -0.01 dB
- Anti-alias filter stopband rejection (from 0.6 × output data rate):
 > 85 dB

Approximate resource usage in a Xilinx Virtex-6

- Slice flip-flops: 13935
- Slice LUTs: 9100
- Block RAMs (18kb): 92
- DSP48E(1)s: 96

timed loop

[IMAGE alt='image' src='GUID-DF57B34A-2E65-4C8D-84BF-5AC499BA1637-a5.gif']

#### Fractional Decimator - 4 spc - 2x
 oc.vi

Decimates the input signal data in according to the output sample rate and delay
 using an FIR filter implementation. This VI must be used in a single-cycle
 timed loop.

Data type

'data in'[0]

Over-clocking

timed loop

timed loop

Data rate

- The output sample rate input may be in the range of [1.52588E-5 to
 1.0], corresponding to decimation factors of [65,536.0 down to
 1.0].
- Decimation factor = 1 / output sample rate
- Output data rate (Hz) = input data rate (Hz) × output sample
 rate
- Input data rate = SCTL clock frequency × SPC × fraction of cycles on
 which input valid is asserted
- Example: If SCTL is clocked at 120 MHz, one SPC is used, and input
 valid is asserted every other cycle, then input data rate = 60
 MHz.

Delay

- The delay input delays the input data. Valid range: [-0.5 to
 +0.5]
- delay (seconds) = delay / input data rate (Hz)

Output calculated

Overflows

data in.overflow

data out.overflow

Reset

TRUE

FALSE

FALSE

TRUE

Pipeline delay

Measuring pipeline delay

1. Select an output sample rate.
2. Assert and deassert reset.
3. Wait for ready for input to return TRUE .
4. Assert input valid and count the number of cycles from the first
 input valid to the first output calculated. The count is equal to
 the pipeline delay for the selected output sample rate.

Group delay of the anti-alias filter

- Decimation factor ≤ 16: group delay = 15 output samples
- 16 < decimation factor ≤ 128: group delay = (256 / decimation
 factor) + 15 output samples
- 128 < decimation factor ≤ 2,048: group delay = (2,056 /
 decimation factor) + 15 output samples
- 2,048 < decimation factor ≤ 32,768: group delay = (34,624 /
 decimation factor) + 15 output samples
- 32,768 < decimation factor ≤ 65,536: group delay = (65,344 /
 decimation factor) + 15 output samples

Performance

- Decimation Range: [1.0 to 65,536.0]
- Output Sample Rate Resolution: 7.11e-15 × input data rate (Hz)
- Delay Range: [-0.5 to +0.5] (corresponds to -0.5 to +0.5 input data
 rate periods)
- Delay Resolution: 1.53e-5 / input data rate (Hz)
- Anti-alias filter passband ripple (to 0.4 × output data rate): 0 dB
 to -0.01 dB
- Anti-alias filter stopband rejection (from 0.6 × output data rate):
 > 85 dB

Approximate resource usage in a Xilinx Virtex-6

- Slice flip-flops: 39400
- Slice LUTs: 25600
- Block RAMs (18kb): 352
- DSP48E(1)s: 274

timed loop

[IMAGE alt='image' src='GUID-D66F9918-B5B2-45E3-BE27-1651DC187145-a5.gif']

#### Fractional Interpolator - 1 spc -
 2x oc.vi

Interpolates the input signal data in according to input sample rate and delay using
 an FIR filter implementation. This VI must be used in a single-cycle
 timed loop.

Data type

'data in'[0]

Over-clocking

timed loop

timed loop

Data rate

- The input sample rate input may be in the range of [1.52588E-5 to
 1.0], corresponding to interpolation factors of [65,536.0 down to
 1.0].
- Interpolation factor = 1 / input sample rate
- Output data rate (Hz) = input data rate (Hz) / input sample
 rate
- Input data rate = SCTL clock frequency × SPC × fraction of cycles on
 which input valid is asserted
- Example: If SCTL is clocked at 120 MHz, one SPC is used, and input
 valid is asserted every other cycle, then input data rate = 60
 MHz.

Delay

- The delay input delays the input data. Valid range: [-0.5 to
 +0.5]
- Delay (seconds) = delay / input data rate (Hz)

Input consumed

Overflows

data in.overflow

data out.overflow

Reset

TRUE

FALSE

FALSE

TRUE

Pipeline delay

timed loop

Group delay of the anti-image filter

Performance

- Interpolation Range: [1.0 to 65,536.0]
- Output Sample Rate Resolution: 7.11e-15 × input data rate (Hz)
- Delay Range: [-0.5 to +0.5] (corresponds to -0.5 to +0.5 input data
 rate periods)
- Delay Resolution: 3.81e-6 / input data rate (Hz)
- Anti-image filter passband ripple (to 0.4 × input data rate): 0 dB
 to -0.01 dB
- Anti-image filter stopband rejection (from 0.6 × input data rate):
 > 85 dB

Approximate resource usage in a Xilinx Virtex-6

- Slice flip-flops: 4000
- Slice LUTs: 1900
- Block RAMs (18kb): 30
- DSP48E(1)s: 46

timed loop

[IMAGE alt='image' src='GUID-E9A44B3F-8DCD-4354-8524-7E4B3AC365C9-a5.gif']

#### Fractional Interpolator - 1 spc -
 3x oc.vi

Interpolates the input signal data in according to input sample rate and delay using
 an FIR filter implementation. This VI must be used in a single-cycle
 timed loop.

Data type

'data in'[0]

Over-clocking

timed loop

timed loop

Data rate

- The input sample rate input may be in the range of [1.52588E-5 to
 1.0], corresponding to interpolation factors of [65,536.0 down to
 1.0].
- Interpolation factor = 1 / input sample rate
- Output data rate (Hz) = input data rate (Hz) / input sample
 rate
- Input data rate = SCTL clock frequency × SPC × fraction of cycles on
 which input valid is asserted
- Example: If SCTL is clocked at 120 MHz, one SPC is used, and input
 valid is asserted every other cycle, then input data rate = 60
 MHz.

Delay

- The delay input delays the input data. Valid range: [-0.5 to
 +0.5]
- Delay (seconds) = delay / input data rate (Hz)

Input consumed

Overflows

data in.overflow

data out.overflow

Reset

TRUE

FALSE

FALSE

TRUE

Pipeline delay

timed loop

Group delay of the anti-image filter

Performance

- Interpolation Range: [1.0 to 65,536.0]
- Output Sample Rate Resolution: 7.11e-15 × input data rate (Hz)
- Delay Range: [-0.5 to +0.5] (corresponds to -0.5 to +0.5 input data
 rate periods)
- Delay Resolution: 3.81e-6 / input data rate (Hz)
- Anti-image filter passband ripple (to 0.4 × input data rate): 0 dB
 to -0.01 dB
- Anti-image filter stopband rejection (from 0.6 × input data rate):
 > 85 dB

Approximate resource usage in a Xilinx Virtex-6

- Slice flip-flops: 2800
- Slice LUTs: 1400
- Block RAMs (18kb): 20
- DSP48E(1)s: 31

timed loop

[IMAGE alt='image' src='GUID-492EC004-A439-4F54-9270-73DE52792E90-a5.gif']

#### Fractional Interpolator - 1 spc -
 3x oc.vi

Interpolates the input signal data in according to input sample rate and delay using
 an FIR filter implementation. This VI must be used in a single-cycle
 timed loop.

Data type

'data in'[0]

Over-clocking

timed loop

timed loop

Data rate

- The input sample rate input may be in the range of [1.52588E-5 to
 1.0], corresponding to interpolation factors of [65,536.0 down to
 1.0].
- Interpolation factor = 1 / input sample rate
- Output data rate (Hz) = input data rate (Hz) / input sample
 rate
- Input data rate = SCTL clock frequency × SPC × fraction of cycles on
 which input valid is asserted
- Example: If SCTL is clocked at 120 MHz, one SPC is used, and input
 valid is asserted every other cycle, then input data rate = 60
 MHz.

Delay

- The delay input delays the input data. Valid range: [-0.5 to
 +0.5]
- Delay (seconds) = delay / input data rate (Hz)

Input consumed

Overflows

data in.overflow

data out.overflow

Reset

TRUE

FALSE

FALSE

TRUE

Pipeline delay

timed loop

Group delay of the anti-image filter

Performance

- Interpolation Range: [1.0 to 65,536.0]
- Output Sample Rate Resolution: 7.11e-15 × input data rate (Hz)
- Delay Range: [-0.5 to +0.5] (corresponds to -0.5 to +0.5 input data
 rate periods)
- Delay Resolution: 3.81e-6 / input data rate (Hz)
- Anti-image filter passband ripple (to 0.4 × input data rate): 0 dB
 to -0.01 dB
- Anti-image filter stopband rejection (from 0.6 × input data rate):
 > 85 dB

Approximate resource usage in a Xilinx Virtex-6

- Slice flip-flops: 2800
- Slice LUTs: 1400
- Block RAMs (18kb): 20
- DSP48E(1)s: 31

timed loop

[IMAGE alt='image' src='GUID-492EC004-A439-4F54-9270-73DE52792E90-a5.gif']

#### Fractional Interpolator - 2 spc -
 2x oc.vi

Interpolates the input signal data in according to input sample rate and delay using
 an FIR filter implementation. This VI must be used in a single-cycle
 timed loop.

Data type

'data in'[0]

Over-clocking

timed loop

timed loop

Data rate

- The input sample rate input may be in the range of [1.52588E-5 to
 1.0]. This corresponds to interpolation factors of [65,536.0 down to
 1.0]. This VI attempts to return a new data out output every cycle.
 It consumes valid data in inputs at a sample rate equal to the
 normalized input sample rate.
- Interpolation factor = 1 / input sample rate.
- Output data rate (Hz) = input data rate (Hz) / input sample
 rate.
- The input data rate is defined by the clock frequency of the
 Single-Cycle Timed Loop (SCTL), the number of Samples Per Cycle
 (SPC) in data in, and the fraction of cycles on which input valid is
 asserted.
- Example: If SCTL is clocked at 120 MHz, one SPC is used, and the
 input valid signal is asserted on every other cycle, then the input
 data rate is 60 MHz.

Delay

- The delay input delays the input data. Valid range: [-0.5 to
 +0.5]
- Delay (seconds) = delay / input data rate (Hz)

Input consumed

Overflows

data in.overflow

data out.overflow

Reset

TRUE

FALSE

FALSE

TRUE

Pipeline delay

timed loop

Group delay of the anti-image filter

Performance

- Interpolation Range: [1.0 to 65,536.0]
- Output Sample Rate Resolution: 7.11e-15 × input data rate (Hz)
- Delay Range: [-0.5 to +0.5] (corresponds to -0.5 to +0.5 input data
 rate periods)
- Delay Resolution: 3.81e-6 / input data rate (Hz)
- Anti-image filter passband ripple (to 0.4 × input data rate): 0 dB
 to -0.01 dB
- Anti-image filter stopband rejection (from 0.6 × input data rate):
 > 85 dB

Approximate resource usage in a Xilinx Virtex-6

- Slice flip-flops: 7800
- Slice LUTs: 3600
- Block RAMs (18kb): 60
- DSP48E(1)s: 92

timed loop

[IMAGE alt='image' src='GUID-BBC22181-A950-489D-A15C-3049CE7B25A3-a5.gif']

#### Fractional Interpolator - 2 spc -
 3x oc.vi

Interpolates the input signal data in according to input sample rate and delay using
 an FIR filter implementation. This VI must be used in a single-cycle
 timed loop.

Data type

'data in'[0]

Over-clocking

timed loop

timed loop

Data rate

- The input sample rate input may be in the range of [1.52588E-5 to
 1.0], corresponding to interpolation factors of [65,536.0 down to
 1.0]. This VI attempts to return a new data out output every cycle.
 It consumes valid data in inputs at a sample rate equal to the
 normalized input sample rate.
- Interpolation factor = 1 / input sample rate.
- Output data rate (Hz) = input data rate (Hz) / input sample
 rate.
- The input data rate is defined by the clock frequency of the
 Single-Cycle Timed Loop (SCTL), the number of Samples Per Cycle
 (SPC) in data in, and the fraction of cycles on which input valid is
 asserted. Input data rate = SCTL clock frequency × SPC × fraction of
 cycles on which input valid is asserted.
- For example if the SCTL is clocked at 120 MHz, one SPC is used, and
 the input valid signal is asserted on every other cycle, then the
 input data rate is 60 MHz.

Delay

- The delay input delays the input data. Valid range: [-0.5 to
 +0.5]
- Delay (seconds) = delay / input data rate (Hz)

Input consumed

Overflows

data in.overflow

data out.overflow

Reset

TRUE

FALSE

FALSE

TRUE

Pipeline delay

timed loop

Group delay of the anti-image filter

Performance

- Interpolation Range: [1.0 to 65,536.0]
- Output Sample Rate Resolution: 7.11e-15 × input data rate (Hz)
- Delay Range: [-0.5 to +0.5] (corresponds to -0.5 to +0.5 input data
 rate periods)
- Delay Resolution: 3.81e-6 / input data rate (Hz)
- Anti-image filter passband ripple (to 0.4 × input data rate): 0 dB
 to -0.01 dB
- Anti-image filter stopband rejection (from 0.6 × input data rate):
 > 85 dB

Approximate resource usage in a Xilinx Virtex-6

- Slice flip-flops: 5250
- Slice LUTs: 2500
- Block RAMs (18kb): 40
- DSP48E(1)s: 62

timed loop

[IMAGE alt='image' src='GUID-74E01DB6-E721-42FF-8E29-5C20D2C45853-a5.gif']

#### Frequency Shift - 1 spc.vi

Applies a digital frequency shift to the I/Q data. A Numerically-Controlled
 Oscillator (NCO) creates a cosine/sine pair, which is then multiplied by the I/Q
 data using a complex multiplier. The net effect is to shift the complex spectrum to
 the left or right in the frequency domain. This VI must be used in a single-cycle
 timed loop.

This VI provides the following
 functionality:

data

out

.

I

≤

data

in

.

I

×

cosine

-

data

in

.

Q

×

sine

,

data

out

.

Q

≤

data

in

.

I

×

sine

+

data

in

.

Q

×

cosine

where "×" represents scalar multiplication.

- The frequency shift input may be in the range of (-0.5 to +0.5), where
 negative values shift the complex spectrum to the left and positive values
 shift the complex spectrum to the right. The amount of frequency shift (in
 Hz) is determined by multiplying the data rate (in Hz) by the frequency
 shift input.
- Frequency Shift (Hz) = frequency shift × data rate (Hz).
- The data rate is defined by the clock frequency of the Single-Cycle Timed Loop
 (SCTL), the number of Samples Per Cycle (SPC) in data in, and the fraction of
 cycles on which input valid is asserted. Data rate = SCTL clock frequency × SPC
 × fraction of cycles on which input valid is asserted.
- For example, if the SCTL is clocked at 120 MHz, one SPC is used, and the input
 valid signal is asserted on every other cycle, then the data rate is 60
 MHz.
- The phase input may be in the range of (-0.5 to +0.5), which corresponds to
 phase shifting the sine and cosine signals -180 degrees to +180 degrees.

Data type

'data in'[0]

Overflows

data in.overflow

data out.overflow

Reset

TRUE

FALSE

FALSE

TRUE

Pipeline delay

timed loop

Performance

- Frequency Range: (-0.5 to +0.5) × data rate
- Frequency Resolution: 3.56e-15 × data rate
- Phase Range: (-0.5 to +0.5) (corresponds to -180 to +180
 degrees)
- Phase Resolution: 4.77e-7 (corresponds to 0.00017 degrees).
- Spurious Free Dynamic Range: > 105 dBFS

Approximate resource usage in a Xilinx Virtex-5 or Virtex-6

- Slice flip-flops: 375
- Slice LUTs: 600
- Block RAMs (18kb): 1
- DSP48E(1)s: 6

timed loop

[IMAGE alt='image' src='GUID-0BBD8E25-403F-4D40-9F0B-D61B9DA011A1-a5.gif']

#### Frequency Shift - 2 spc.vi

Applies a digital frequency shift to the I/Q data. A Numerically-Controlled
 Oscillator (NCO) creates a cosine/sine pair, which is then multiplied by the I/Q
 data using a complex multiplier. The net effect is to shift the complex spectrum to
 the left or right in the frequency domain. This VI must be used in a single-cycle
 timed loop.

This VI

This VI provides the
 following functionality:

data

out

.

I

≤

data

in

.

I

×

cosine

-

data

in

.

Q

×

sine

,

data

out

.

Q

≤

data

in

.

I

×

sine

+

data

in

.

Q

×

cosine

where "×" represents scalar multiplication.

- The frequency shift input may be in the range of (-0.5 to +0.5), where negative
 values shift the complex spectrum to the left and positive values shift the
 complex spectrum to the right. The amount of frequency shift (in Hz) is
 determined by multiplying the data rate (in Hz) by the frequency shift
 input.
- Frequency Shift (Hz) = frequency shift × data rate (Hz).
- The data rate is defined by the clock frequency of the Single-Cycle Timed Loop
 (SCTL), the number of Samples Per Cycle (SPC) in data in, and the fraction of
 cycles on which input valid is asserted. Data rate = SCTL clock frequency × SPC
 × fraction of cycles on which input valid is asserted.
- For example, if the SCTL is clocked at 120 MHz, one SPC is used, and the input
 valid signal is asserted on every other cycle, then the data rate is 60
 MHz.
- The phase input may be in the range of (-0.5 to +0.5), which corresponds to
 phase shifting the sine and cosine signals -180 degrees to +180 degrees.

Data type

'data in'[0]

Overflows

data in.overflow

data out.overflow

Reset

TRUE

FALSE

FALSE

TRUE

Pipeline delay

timed loop

Performance

- Frequency Range: (-0.5 to +0.5) × data rate
- Frequency Resolution: 3.56e-15 × data rate
- Phase Range: (-0.5 to +0.5) (corresponds to -180 to +180
 degrees)
- Phase Resolution: 4.77e-7 (corresponds to 0.00017 degrees).
- Spurious Free Dynamic Range: > 105 dBFS

Approximate resource usage in a Xilinx Virtex-5 or Virtex-6

- Slice flip-flops: 875
- Slice LUTs: 1110
- Block RAMs (18kb): 2
- DSP48E(1)s: 12

timed loop

[IMAGE alt='image' src='GUID-CDF0D10F-B302-469D-A6C7-2663319452E9-a5.gif']

#### Frequency Shift - 4 spc.vi

Applies a digital frequency shift to the I/Q data. A Numerically-Controlled
 Oscillator (NCO) creates a cosine/sine pair, which is then multiplied by the I/Q
 data using a complex multiplier. The net effect is to shift the complex spectrum to
 the left or right in the frequency domain. This VI must be used in a single-cycle
 timed loop.

This VI provides the following
 functionality:

data

out

.

I

≤

data

in

.

I

×

cosine

-

data

in

.

Q

×

sine

,

data

out

.

Q

≤

data

in

.

I

×

sine

+

data

in

.

Q

×

cosine

where "×" represents scalar multiplication.

- The frequency shift input may be in the range of (-0.5 to +0.5), where negative
 values shift the complex spectrum to the left and positive values shift the
 complex spectrum to the right. The amount of frequency shift (in Hz) is
 determined by multiplying the data rate (in Hz) by the frequency shift
 input.
- Frequency Shift (Hz) = frequency shift × data rate (Hz).
- The data rate is defined by the clock frequency of the Single-Cycle Timed Loop
 (SCTL), the number of Samples Per Cycle (SPC) in data in, and the fraction of
 cycles on which input valid is asserted. Data rate = SCTL clock frequency × SPC
 × fraction of cycles on which input valid is asserted.
- For example, if the SCTL is clocked at 120 MHz, one SPC is used, and the input
 valid signal is asserted on every other cycle, then the data rate is 60
 MHz.
- The phase input may be in the range of (-0.5 to +0.5), which corresponds to
 phase shifting the sine and cosine signals -180 degrees to +180 degrees.

Data type

'data in'[0]

Overflows

data in.overflow

data out.overflow

Reset

TRUE

FALSE

FALSE

TRUE

Pipeline delay

timed loop

Performance

- Frequency Range: (-0.5 to +0.5) × data rate
- Frequency Resolution: 3.56e-15 × data rate
- Phase Range: (-0.5 to +0.5) (corresponds to -180 to +180
 degrees)
- Phase Resolution: 4.77e-7 (corresponds to 0.00017 degrees).
- Spurious Free Dynamic Range: > 105 dBFS

Approximate resource usage in a Xilinx Virtex-5 or Virtex-6

- Slice flip-flops: 1650
- Slice LUTs: 2325
- Block RAMs (18kb): 4
- DSP48E(1)s: 24

timed loop

[IMAGE alt='image' src='GUID-7B4742BE-0D12-4AE2-9FEE-645890621F65-a5.gif']

#### Frequency Shift - 8 spc.vi

Applies a digital frequency shift to the I/Q data. A Numerically-Controlled
 Oscillator (NCO) creates a cosine/sine pair, which is then multiplied by the I/Q
 data using a complex multiplier. The net effect is to shift the complex spectrum to
 the left or right in the frequency domain. This VI must be used in a single-cycle
 timed loop.

This VI provides the following
 functionality:

data

out

.

I

≤

data

in

.

I

×

cosine

-

data

in

.

Q

×

sine

,

data

out

.

Q

≤

data

in

.

I

×

sine

+

data

in

.

Q

×

cosine

where "×" represents scalar multiplication.

- The frequency shift input may be in the range of (-0.5 to +0.5), where negative
 values shift the complex spectrum to the left and positive values shift the
 complex spectrum to the right. The amount of frequency shift (in Hz) is
 determined by multiplying the data rate (in Hz) by the frequency shift
 input.
- Frequency Shift (Hz) = frequency shift × data rate (Hz).
- The data rate is defined by the clock frequency of the Single-Cycle Timed Loop
 (SCTL), the number of Samples Per Cycle (SPC) in data in, and the fraction of
 cycles on which input valid is asserted. Data rate = SCTL clock frequency × SPC
 × fraction of cycles on which input valid is asserted.
- For example, if the SCTL is clocked at 120 MHz, one SPC is used, and the input
 valid signal is asserted on every other cycle, then the data rate is 60
 MHz.
- The phase input may be in the range of (-0.5 to +0.5), which corresponds to
 phase shifting the sine and cosine signals -180 degrees to +180 degrees.

Data type

'data in'[0]

Overflows

data in.overflow

data out.overflow

Reset

TRUE

FALSE

FALSE

TRUE

Pipeline delay

timed loop

Performance

- Frequency Range: (-0.5 to +0.5) × data rate
- Frequency Resolution: 3.56e-15 × data rate
- Phase Range: (-0.5 to +0.5) (corresponds to -180 to +180
 degrees)
- Phase Resolution: 4.77e-7 (corresponds to 0.00017 degrees).
- Spurious Free Dynamic Range: > 105 dBFS

Approximate resource usage in a Xilinx Virtex-5 or Virtex-6

- Slice flip-flops: 3175
- Slice LUTs: 4600
- Block RAMs (18kb): 8
- DSP48E(1)s: 48

timed loop

[IMAGE alt='image' src='GUID-FE7F0A72-DC3F-4BF0-84CE-E2879DB9F63D-a5.gif']

#### Frequency Shift - 16
 spc.vi

Applies a digital frequency shift to the I/Q data. A Numerically-Controlled
 Oscillator (NCO) creates a cosine/sine pair, which is then multiplied by the I/Q
 data using a complex multiplier. The net effect is to shift the complex spectrum to
 the left or right in the frequency domain. This VI must be used in a single-cycle
 timed loop.

This VI provides the following
 functionality:

data

out

.

I

≤

data

in

.

I

×

cosine

-

data

in

.

Q

×

sine

,

data

out

.

Q

≤

data

in

.

I

×

sine

+

data

in

.

Q

×

cosine

where "×" represents scalar multiplication.

- The frequency shift input may be in the range of (-0.5 to +0.5), where negative
 values shift the complex spectrum to the left and positive values shift the
 complex spectrum to the right. The amount of frequency shift (in Hz) is
 determined by multiplying the data rate (in Hz) by the frequency shift
 input.
- Frequency Shift (Hz) = frequency shift × data rate (Hz).
- The data rate is defined by the clock frequency of the Single-Cycle Timed Loop
 (SCTL), the number of Samples Per Cycle (SPC) in data in, and the fraction of
 cycles on which input valid is asserted. Data rate = SCTL clock frequency × SPC
 × fraction of cycles on which input valid is asserted.
- For example, if the SCTL is clocked at 120 MHz, one SPC is used, and the input
 valid signal is asserted on every other cycle, then the data rate is 60
 MHz.
- The phase input may be in the range of (-0.5 to +0.5), which corresponds to
 phase shifting the sine and cosine signals -180 degrees to +180 degrees.

Data type

'data in'[0]

Overflows

data in.overflow

data out.overflow

Reset

TRUE

FALSE

FALSE

TRUE

Pipeline delay

timed loop

Performance

- Frequency Range: [-0.5 to +0.5) × data rate
- Frequency Resolution: 3.56e-15 × data rate
- Phase Range: [-0.5 to +0.5) (corresponds to -180 to +180
 degrees)
- Phase Resolution: 4.77e-7 (corresponds to 0.00017 degrees).
- Spurious Free Dynamic Range: > 105 dBFS

Approximate resource usage in a Xilinx Virtex-5 or Virtex-6

- Slice flip-flops: 6225
- Slice LUTs: 9150
- Block RAMs (18kb): 16
- DSP48E(1)s: 96

timed loop

[IMAGE alt='image' src='GUID-4F28E29F-8BD8-43A2-995B-C79FFDF3942B-a5.gif']

#### IQ Impairments - 1 spc.vi

Modifies the I/Q data to apply signal impairments. This VI must be used in a
 single-cycle timed loop.

This VI provides the following
 functionality:

data

out

.

I

≤

(

pre

-

gain

offset

I

+

data

in

.

I

)

×

inline

gain

I

+

(

pre

-

gain

offset

Q

+

data

in

.

Q

)

×

cross

gain

Q

+

post

-

gain

offset

I

data

out

.

Q

≤

(

pre

-

gain

offset

Q

+

data

in

.

Q

)

×

inline

gain

Q

+

(

pre

-

gain

offset

I

+

data

in

.

I

)

×

cross

gain

I

+

post

-

gain

offset

Q

where "×" represents scalar multiplication.

Data type

'data in'[0]

Overflows

data in.overflow

data out.overflow

Reset

TRUE

FALSE

FALSE

TRUE

Pipeline delay

timed loop

Approximate resource usage in a Xilinx Virtex-5 or Virtex-6

- Slice flip-flops: 100
- Slice LUTs: 225
- Block RAMs (18kb): 0
- DSP48E(1)s: 4

timed loop

[IMAGE alt='image' src='GUID-F4CC8B38-7AFD-4EDA-8F88-FFA063AC1BC8-a5.gif']

#### IQ Impairments - 2 spc.vi

Modifies the I/Q data to apply signal impairments. This VI must be used in a
 single-cycle timed loop.

This VI provides the following
 functionality:

data

out

.

I

≤

(

pre

-

gain

offset

I

+

data

in

.

I

)

×

inline

gain

I

+

(

pre

-

gain

offset

Q

+

data

in

.

Q

)

×

cross

gain

Q

+

post

-

gain

offset

I

data

out

.

Q

≤

(

pre

-

gain

offset

Q

+

data

in

.

Q

)

×

inline

gain

Q

+

(

pre

-

gain

offset

I

+

data

in

.

I

)

×

cross

gain

I

+

post

-

gain

offset

Q

where "×" represents scalar multiplication.

Data type

'data in'[0]

Overflows

data in.overflow

data out.overflow

Reset

TRUE

FALSE

FALSE

TRUE

Pipeline delay

timed loop

Approximate resource usage in a Xilinx Virtex-5 or Virtex-6

- Slice flip-flops: 175
- Slice LUTs: 425
- Block RAMs (18kb): 0
- DSP48E(1)s: 8

timed loop

[IMAGE alt='image' src='GUID-9F7F81BF-7713-495A-A0B7-FC58CD625439-a5.gif']

#### IQ Impairments - 4 spc.vi

Modifies the I/Q data to apply signal impairments. This VI must be used in a
 single-cycle timed loop.

This VI provides the following
 functionality:

data

out

.

I

≤

(

pre

-

gain

offset

I

+

data

in

.

I

)

×

inline

gain

I

+

(

pre

-

gain

offset

Q

+

data

in

.

Q

)

×

cross

gain

Q

+

post

-

gain

offset

I

data

out

.

Q

≤

(

pre

-

gain

offset

Q

+

data

in

.

Q

)

×

inline

gain

Q

+

(

pre

-

gain

offset

I

+

data

in

.

I

)

×

cross

gain

I

+

post

-

gain

offset

Q

where "×" represents scalar multiplication.

Data type

'data in'[0]

Overflows

data in.overflow

data out.overflow

Reset

TRUE

FALSE

FALSE

TRUE

Pipeline delay

timed loop

Approximate resource usage in a Xilinx Virtex-5 or Virtex-6

- Slice flip-flops: 325
- Slice LUTs: 875
- Block RAMs (18kb): 0
- DSP48E(1)s: 16

timed loop

[IMAGE alt='image' src='GUID-1760CD75-B60C-4DD4-B2FD-AE20EF89AFC1-a5.gif']

#### IQ Impairments - 8 spc.vi

Modifies the I/Q data to apply signal impairments. This VI must be used in a
 single-cycle timed loop.

This VI provides the following
 functionality:

data

out

.

I

≤

(

pre

-

gain

offset

I

+

data

in

.

I

)

×

inline

gain

I

+

(

pre

-

gain

offset

Q

+

data

in

.

Q

)

×

cross

gain

Q

+

post

-

gain

offset

I

data

out

.

Q

≤

(

pre

-

gain

offset

Q

+

data

in

.

Q

)

×

inline

gain

Q

+

(

pre

-

gain

offset

I

+

data

in

.

I

)

×

cross

gain

I

+

post

-

gain

offset

Q

where "×" represents scalar multiplication.

Data type

'data in'[0]

Overflows

data in.overflow

data out.overflow

Reset

TRUE

FALSE

FALSE

TRUE

Pipeline delay

timed loop

Approximate resource usage in a Xilinx Virtex-5 or Virtex-6

- Slice flip-flops: 650
- Slice LUTs: 1725
- Block RAMs (18kb): 0
- DSP48E(1)s: 32

timed loop

[IMAGE alt='image' src='GUID-4D83BA6F-FE14-42C8-B4A4-016A0C24683D-a5.gif']

#### IQ Impairments - 16 spc.vi

Modifies the I/Q data to apply signal impairments. This VI must be used in a
 single-cycle timed loop.

This VI provides the following
 functionality:

data

out

.

I

≤

(

pre

-

gain

offset

I

+

data

in

.

I

)

×

inline

gain

I

+

(

pre

-

gain

offset

Q

+

data

in

.

Q

)

×

cross

gain

Q

+

post

-

gain

offset

I

data

out

.

Q

≤

(

pre

-

gain

offset

Q

+

data

in

.

Q

)

×

inline

gain

Q

+

(

pre

-

gain

offset

I

+

data

in

.

I

)

×

cross

gain

I

+

post

-

gain

offset

Q

where "×" represents scalar multiplication.

Data type

'data in'[0]

Overflows

data in.overflow

data out.overflow

Reset

TRUE

FALSE

FALSE

TRUE

Pipeline delay

timed loop

Approximate resource usage in a Xilinx Virtex-5 or Virtex-6

- Slice flip-flops: 2175
- Slice LUTs: 3550
- Block RAMs (18kb): 0
- DSP48E(1)s: 64

timed loop

[IMAGE alt='image' src='GUID-0439CF56-2D4A-44AC-8662-2F3E7E65A032-a5.gif']

#### IQ Power Level Trigger - 1 spc - 18 bit Legacy.vi

Creates triggers based on the trigger configuration and the power of the input
 data.

Data type

'data in'[0]

Configuration

- Trig rising edge specifies if the output trigger is
 sensitive to the increase or decrease of the input data power with
 respect to the trig level. A value of TRUE creates
 triggers when the input data power level rises above the trig level
 threshold, and a value of FALSE creates triggers
 when the input data power level falls below the trig level
 threshold.
- Min quiet time specifies the minimum quiet time of
 the input data power with respect to the trig level threshold, in
 units of valid samples. If the power of input data crosses the trig
 level threshold before the min quiet time has expired, the trigger
 is ignored and the min quiet time state is reset. The minimum
 min quiet time is one valid sample, and a
 minimum quiet time of zero is coerced to a value of one
 internally.
- Trig level specifies the threshold for the input
 data power. The power of the input data is calculated using the
 following formula: Signal power = (input data.I)^2 + (input
 data.Q)^2

Ready for trigger

FALSE

FALSE

TRUE

Reset

TRUE

FALSE

FALSE

TRUE

Pipeline delay

timed loop

Approximate resource usage in a Xilinx Virtex-5 or Virtex-6

- Slice flip-flops: 212
- Slice LUTs: 244
- Block RAMs (18kb): 0
- DSP48E(1)s: 2

timed loop

[IMAGE alt='image' src='GUID-808C79F7-7CF9-4EDF-9398-6B3A555D98C2-a5.gif']

#### IQ Power Level Trigger - 1 spc - 18 bit.vi

Creates triggers based on the trigger configuration and the power of the input
 data.

Data type

'data in'[0]

Configuration

- Trig rising edge specifies if the output trigger is
 sensitive to the increase or decrease of the input data power with
 respect to the trig level. A value of TRUE creates
 triggers when the input data power level rises above the trig level
 threshold, and a value of FALSE creates triggers
 when the input data power level falls below the trig level
 threshold.
- Min quiet time specifies the minimum quiet time of
 the input data power with respect to the trig level threshold, in
 units of valid samples. If the power of input data crosses the trig
 level threshold before the min quiet time has expired, the trigger
 is ignored and the min quiet time state is reset. The minimum
 min quiet time is one valid sample, and a
 minimum quiet time of zero is coerced to a value of one
 internally.
- Trig level specifies the threshold for the input
 data power. The power of the input data is calculated using the
 following formula:

Signal power = (input data.I)^2 + (input data.Q)^2

Ready for trigger

FALSE

FALSE

TRUE

Reset

TRUE

FALSE

FALSE

TRUE

Pipeline delay

timed loop

Approximate resource usage in a Xilinx Virtex-5 or Virtex-6

- Slice flip-flops: 37
- Slice LUTs: 142
- Block RAMs (18kb): 0
- DSP48E(1)s: 2

timed loop

[IMAGE alt='image' src='GUID-6CC2B310-DCC9-4365-9476-E83E99B2E485-a5.gif']

#### IQ Power Level Trigger - 1 spc - 25 bit.vi

Creates triggers based on the trigger configuration and the power of the input
 data.

Data type

'data in'[0]

Configuration

- Trig rising edge specifies if the output trigger is
 sensitive to the increase or decrease of the input data power with
 respect to the trig level. A value of TRUE creates
 triggers when the input data power level rises above the trig level
 threshold, and a value of FALSE creates triggers
 when the input data power level falls below the trig level
 threshold.
- Min quiet time specifies the minimum quiet time of
 the input data power with respect to the trig level threshold, in
 units of valid samples. If the power of input data crosses the trig
 level threshold before the min quiet time has expired, the trigger
 is ignored and the min quiet time state is reset. The minimum
 min quiet time is one valid sample, and a
 minimum quiet time of zero is coerced to a value of one
 internally.
- Trig level specifies the threshold for the input
 data power. The power of the input data is calculated using the
 following formula:

Signal power = (input data.I)^2 + (input data.Q)^2

Ready for trigger

FALSE

FALSE

TRUE

Reset

TRUE

FALSE

FALSE

TRUE

Pipeline delay

timed loop

Approximate resource usage in a Xilinx Virtex-5 or Virtex-6

- Slice flip-flops: 104
- Slice LUTs: 225
- Block RAMs (18kb): 0
- DSP48E(1)s: 4

timed loop

[IMAGE alt='image' src='GUID-3C5910D7-8A68-4F37-8365-58834EE58B82-a5.gif']

#### IQ Power Level Trigger - 2 spc - 18 bit.vi

Creates triggers based on the trigger configuration and the power of the input
 data.

Data type

'data in'[0]

Configuration

- Trig rising edge specifies if the output trigger is
 sensitive to the increase or decrease of the input data power with
 respect to the trig level. A value of TRUE creates
 triggers when the input data power level rises above the trig level
 threshold, and a value of FALSE creates triggers
 when the input data power level falls below the trig level
 threshold.
- Min quiet time specifies the minimum quiet time of
 the input data power with respect to the trig level threshold, in
 units of valid samples. If the power of input data crosses the trig
 level threshold before the min quiet time has expired, the trigger
 is ignored and the min quiet time state is reset. The minimum
 min quiet time is one valid sample, and a
 minimum quiet time of zero is coerced to a value of one
 internally.
- Trig level specifies the threshold for the input
 data power. The power of the input data is calculated using the
 following formula:

signal power = (input data.I)^2 + (input data.Q)^2

Ready for trigger

FALSE

FALSE

TRUE

Data index

Reset

TRUE

FALSE

FALSE

TRUE

Pipeline delay

timed loop

Approximate resource usage in a Xilinx Virtex-5 or Virtex-6

- Slice flip-flops: 48
- Slice LUTs: 212
- Block RAMs (18kb): 0
- DSP48E(1)s: 4

timed loop

[IMAGE alt='image' src='GUID-D5EB9B81-4085-4673-87AF-7CE9517D72CE-a5.gif']

#### IQ Power Level Trigger - 4 spc - 18 bit.vi

Creates triggers based on the trigger configuration and the power of the input
 data.

Data type

'data in'[0]

Configuration

- Trig rising edge specifies if the output trigger is
 sensitive to the increase or decrease of the input data power with
 respect to the trig level. A value of TRUE creates
 triggers when the input data power level rises above the trig level
 threshold, and a value of FALSE creates triggers
 when the input data power level falls below the trig level
 threshold.
- Min quiet time specifies the minimum quiet time of
 the input data power with respect to the trig level threshold, in
 units of valid samples. If the power of input data crosses the trig
 level threshold before the min quiet time has expired, the trigger
 is ignored and the min quiet time state is reset. The minimum
 min quiet time is one valid sample, and a
 minimum quiet time of zero is coerced to a value of one
 internally.
- Trig level specifies the threshold for the input
 data power. The power of the input data is calculated using the
 following formula:

Signal power = (input data.I)^2 + (input data.Q)^2

Ready for trigger

FALSE

FALSE

TRUE

Data index

Reset

TRUE

FALSE

FALSE

TRUE

Pipeline delay

timed loop

Approximate resource usage in a Xilinx Virtex-5 or Virtex-6

- Slice flip-flops: 50
- Slice LUTs: 438
- Block RAMs (18kb): 0
- DSP48E(1)s: 8

timed loop

[IMAGE alt='image' src='GUID-D9255B2E-D515-4E5A-974C-42F7DA248C21-a5.gif']

#### IQ Power Level Trigger - 8 spc - 18 bit.vi

Creates triggers based on the trigger configuration and the power of the input
 data.

Data type

'data in'[0]

Configuration

- Trig rising edge specifies if the output trigger is
 sensitive to the increase or decrease of the input data power with
 respect to the trig level. A value of TRUE creates
 triggers when the input data power level rises above the trig level
 threshold, and a value of FALSE creates triggers
 when the input data power level falls below the trig level
 threshold.
- Min quiet time specifies the minimum quiet time of
 the input data power with respect to the trig level threshold, in
 units of valid samples. If the power of input data crosses the trig
 level threshold before the min quiet time has expired, the trigger
 is ignored and the min quiet time state is reset. The minimum
 min quiet time is one valid sample, and a
 minimum quiet time of zero is coerced to a value of one
 internally.
- Trig level specifies the threshold for the input
 data power. The power of the input data is calculated using the
 following formula:

Signal power = (input data.I)^2 + (input data.Q)^2

Ready for trigger

FALSE

FALSE

TRUE

Data index

Reset

TRUE

FALSE

FALSE

TRUE

Pipeline delay

timed loop

Approximate resource usage in a Xilinx Virtex-5 or Virtex-6

- Slice flip-flops: 54
- Slice LUTs: 708
- Block RAMs (18kb): 0
- DSP48E(1)s: 16

timed loop

[IMAGE alt='image' src='GUID-4F80DD89-064E-440A-9870-BD96235DED6D-a5.gif']

#### IQ Data to U32.vi

Converts a cluster of I/Q data into separate I and Q data in the fixed-point format,
 typecasts the separate I and Q data to convert them to I16 values, and bundles the
 two I16 values into a U32. Overflows are reported from the I/Q data and fixed-point
 casts.

[IMAGE alt='image' src='GUID-52F8BE9C-73BB-4FF2-B368-01816248E9AC-a5.gif']

Input parameters

- IQ data specifies a bundle of real and imaginary
 (I/Q) data.
- IQ data.I specifies the bundled real (I) data.
- IQ data.Q specifies the bundled imaginary (Q)
 data.
- IQ data.overflow specifies whether the I/Q data has
 overflowed.

Output parameters

- U32 data returns the I/Q data that is bundled into
 U32 data, with I in the lower 16 bits and Q in the upper 16
 bits.
- Overflow indicates whether the I/Q data or any of
 the typecasts to the U32 data have overflowed.

#### U32 to IQ Data.vi

Splits the U32 data input into two I16 values and converts each I16 value into
 separate I and Q data in the fixed-point format. This VI bundles the separate I and
 Q data into an I/Q data cluster, with an option to specify an overflow.

[IMAGE alt='image' src='GUID-358BFADC-B8E1-4083-ABFD-D8029BF079FF-a5.gif']

Input parameters

- U32 data specifies the U32 I/Q data, with I in the
 lower 16 bits and Q in the upper 16 bits.
- Overflow specifies whether the I/Q data has
 overflowed.

Output parameters

- IQ data returns a bundle of real and imaginary
 (I/Q) data.
- IQ data.I returns the bundled real (I) data.
- IQ data.Q returns the bundled imaginary (Q)
 data.
- IQ data.overflow indicates whether the I/Q data has
 overflowed.

#### Complex Multiply.vi

Implements a complex multiply using DSP48E blocks.

This VI provides the
 following functionality:

IQ

Out

=

IQ

In

1

×

IQ

In

2

Pipeline delay

timed loop

[IMAGE alt='image' src='GUID-05CA201F-616C-46E4-9FC6-A7517632662F-a5.gif']

#### NCO.vi

Creates a cosine/sine pair at the specified frequency. The frequency range is -0.5 to
 0.5, and is relative to the input data rate. The spectral performance is 105 dBFS
 SFDR.

Pipeline delay

timed loop

[IMAGE alt='image' src='GUID-D6F28C10-11EA-4B48-A9E0-8B34A178AD65-a5.gif']

#### Non-symmetric FIR.vi

Implements a general purpose FIR filter. This VI must be used in a single-cycle
 timed loop, and requires an additional in-phase clock at
 three times the frequency of the single-cycle timed loop
 clock.

The filter coefficients are loaded sequentially using the filter
 coefficients input. Load the coefficients in sequential order: 0, 1, 2, ... 32.
 There are no requirements to the symmetry of the coefficients.

Complete the
 following steps to load the coefficients:

1. Set coef load high, then low to begin the load sequence.
2. For 33 times: write the coefficient to coef data and set
 coef write high, then set coef write 
 low.

The new coefficients are applied automatically as they are being
 written.

You can use the Digital Filter Design Toolkit to calculate
 coefficients for your desired filtering application.

Pipeline delay

timed loop

[IMAGE alt='image' src='GUID-BCFCD108-A9CB-45B3-BF7D-890E11BE6985-a5.gif']

Parent topic:

Digital Signal Processing (DSP) Overview

<!--NI_TOPIC bundle=ni-reconfigurable-oscilloscopes path=edge-triggers.html language=enus -->
## TOPIC 00029: Edge Triggers

- bundle_id: `ni-reconfigurable-oscilloscopes`
- source_path: `edge-triggers.html`
- source_url: https://docs-be.ni.com/bundle/ni-reconfigurable-oscilloscopes/raw/resource/enus/edge-triggers.html
- document_id: `ni-reconfigurable-oscilloscopes`
- page_type: `leaf`
- content_type: `concept`
- source_description: An edge trigger occurs when a signal crosses a trigger threshold that you specify. You can specify the slope as either positive (on the rising edge) or negative (on the falling edge) to the trigger. Edge triggering is possible on all analog trigger channels, such as 0, 1, or the external trigger cha

### Edge Triggers

An edge trigger occurs when a signal crosses a trigger threshold that you specify. You can
 specify the slope as either positive (on the rising edge) or negative (on the falling
 edge) to the trigger. Edge triggering is possible on all analog trigger channels, such
 as 0, 1, or the external trigger channel. The following figure shows edge
 triggering:

[IMAGE alt='image' src='GUID-D3204854-C2B5-40F8-B7F3-39B98B49119F-a5.gif']

Parent topic:

Triggering

<!--NI_TOPIC bundle=ni-reconfigurable-oscilloscopes path=enob.html language=enus -->
## TOPIC 00030: Effective Number of Bits (ENOB)

- bundle_id: `ni-reconfigurable-oscilloscopes`
- source_path: `enob.html`
- source_url: https://docs-be.ni.com/bundle/ni-reconfigurable-oscilloscopes/raw/resource/enus/enob.html
- document_id: `ni-reconfigurable-oscilloscopes`
- page_type: `leaf`
- content_type: `concept`
- source_description: Effective Number of Bits (ENOB) is another way of specifying signal-to-noise and distortion ratio (SINAD). ENOB is calculated using the following formula: ENOB = ( SINAD - 1 .76 ) + 20 log A V / 2 6 .02 where A is the input amplitude, V is the full scale range of the ADC.The ENOB indicates that the

### Effective Number of Bits (ENOB)

Effective Number of Bits (ENOB) is another way of specifying signal-to-noise and distortion ratio
 (*SINAD*). ENOB is calculated using the following formula:

ENOB

=

(

SINAD

-

1

.76

)

+

20

log

A

V

/

2

6

.02

where

A is the input amplitude,

V is the full scale range of the ADC.

The ENOB indicates that the ADC is equivalent to an ideal ADC of this number of bits.

Parent topic:

Frequency Domain Fundamentals

Related concepts:

- Signal-to-Noise-and-Distortion (SINAD)

<!--NI_TOPIC bundle=ni-reconfigurable-oscilloscopes path=equivalent-time-sampling-and-random-interleav.html language=enus -->
## TOPIC 00031: Equivalent-Time Sampling and Random Interleaved Sampling

- bundle_id: `ni-reconfigurable-oscilloscopes`
- source_path: `equivalent-time-sampling-and-random-interleav.html`
- source_url: https://docs-be.ni.com/bundle/ni-reconfigurable-oscilloscopes/raw/resource/enus/equivalent-time-sampling-and-random-interleav.html
- document_id: `ni-reconfigurable-oscilloscopes`
- page_type: `leaf`
- content_type: `concept`
- source_description: Equivalent-time sampling is a sampling method in which a picture of a waveform is created over time by using a series of samples taken from repetitive waveforms. Random Interleaved Sampling (RIS) is a form of equivalent-time sampling that increases apparent sample rates of repetitive signals by comb

### Equivalent-Time Sampling and Random Interleaved Sampling

Equivalent-time sampling is a sampling method in which a picture of a waveform is created over
 time by using a series of samples taken from repetitive waveforms.

Random Interleaved Sampling (RIS) is a form of equivalent-time sampling that increases apparent
 sample rates of repetitive signals by combining several triggered waveforms. Because the trigger
 time occurs randomly between two samples, the digitizer samples different points in the waveform
 on consecutive acquisitions. By combining these waveforms, you can achieve RIS sample rates that
 are up to 25 times higher than the ADC sample rate on the digitizer.

#### How RIS
 Works

Each waveform trigger occurs at some time randomly distributed between two
 samples. The digitizer can measure the time from the trigger to the next sample, commonly
 called the Time-to-Digital Conversion (TDC), extremely accurately—with hundreds of times
 more resolution than the sample period of the digitizer. With these TDC measurements,
 NI-SCOPE can combine multiple waveforms, aligned at the trigger time, to simulate a faster
 sampling rate for repetitive signals.

#### How Oversampling Factors Increase Effective Sample
 Rates

When a digitizer is in RIS mode, the legal sample rates become multiples of the
 maximum real-time sampling rate. These multiples are the oversampling factor. For example, the
 NI 5112 has a 100 MS/s maximum real-time sampling rate, so the RIS sampling rates are the
 oversampling factor times 100 MS/s, where the oversampling factor is two, three, four, and so
 on. If you specify 300 MS/s for your sampling rate, the oversampling factor is three.

Each
 TDC value is between zero and the sampling period, so a 100 MS/s digitizer has TDC values
 between 0 and 10 ns. This time span is divided into a number of bins equal to the oversampling
 factor. For example, an oversampling factor of three means there is one TDC bin from 0 to
 3.33 ns, another from 3.33 to 6.67 ns, and another from 6.67 to 10 ns. To reconstruct a
 waveform, each bin must contain at least one TDC value.

The following four figures show
 an example RIS acquisition with an oversampling factor of three. Each of the figures shows the
 aligned trigger time of the waveforms followed by the three TDC bins, where the combined width
 of the three bins is the real-time sample period of the digitizer.

1. The first waveform has a TDC value that falls in bin number 1. [IMAGE alt='image' src='GUID-166DBE2D-92EC-4FFB-A312-281085C909A6-a5.gif']
2. The succeeding waveform falls in bin number 3. [IMAGE alt='image' src='GUID-2B290811-2388-4FAB-BE5E-9108D502A230-a5.gif']
3. Because of the randomness of the TDC value, another sampled waveform falls in bin 1.
 NI-SCOPE does not fetch this waveform from the digitizer because the bin is already filled. [IMAGE alt='image' src='GUID-CEC33BB2-47A4-4189-AA62-B2251B45F044-a5.gif']
4. The next waveform falls in bin 2. [IMAGE alt='image' src='GUID-730DB83E-A15E-4939-A35B-53E80FE3973E-a5.gif']

Now all bins are full, so NI-SCOPE returns the three waveforms sampled at the maximum
 real-time rate as one evenly-sampled waveform with a sampling rate three times
 greater.

Parent topic:

Sampling Methods

<!--NI_TOPIC bundle=ni-reconfigurable-oscilloscopes path=fifo-register-bus-fpga-vis.html language=enus -->
## TOPIC 00032: FIFO Register Bus FPGA VIs

- bundle_id: `ni-reconfigurable-oscilloscopes`
- source_path: `fifo-register-bus-fpga-vis.html`
- source_url: https://docs-be.ni.com/bundle/ni-reconfigurable-oscilloscopes/raw/resource/enus/fifo-register-bus-fpga-vis.html
- document_id: `ni-reconfigurable-oscilloscopes`
- page_type: `leaf`
- content_type: `concept`
- source_description: Create Resources.vi Creates a FIFO Register Bus using an existing DMA FIFO. You must specify which FIFO is used to retrieve instructions. Input parameters Instruction FIFO Specifies the DMA FIFO used to send register instructions to the device. The DMA FIFO must meet the following requirements: The

### FIFO Register Bus FPGA VIs

#### Create Resources.vi

Creates a FIFO Register Bus using an existing DMA FIFO. You must specify which FIFO
 is used to retrieve instructions.

[IMAGE alt='image' src='GUID-420C902A-9573-4AF5-986B-7364C9ACE3EF-a5.gif']

| Input parameters |
| --- |
| Instruction FIFO—Specifies the DMA FIFO used to send register instructions to the device. The DMA FIFO must meet the following requirements: The DMA FIFO must be instantiated in the LabVIEW project and must have a pre-defined name based on the value passed to the bus instance parameter of the Open Session VI in the FIFO Register Bus Host library. The format of the name is "reg.host instruction fifo N", where N is the instance number of the FIFO Register Bus Host library and FIFO Register Bus FPGA library. For example, if the name is "reg.host instruction fifo 0", the instance number of this library is 0. The DMA FIFO type must be Host to Target. The DMA FIFO data type must be U64. |

| Output parameters |
| --- |
| FIFO Register Bus—Returns a reference to the created FIFO Register Bus. This reference may be used as an instruction producer. You must use this reference as the FIFO register bus input for the Host Interface VI of this library. |

#### Host Interface.vi

Connects required controls and indicator signals to FIFO Register Bus resources. This
 VI must be placed in a single cycle timed loop and connected
 to any FIFO Register Bus that is used as an instruction
 producer.

[IMAGE alt='image' src='GUID-32068725-8B32-499A-A382-56D44D2B83A0-a5.gif']

| Input parameters |
| --- |
| FIFO register bus—Provides the resources required to link communication between this host interface and the register configuration object. This parameter is obtained from the Create Resources VI in this library. FIFO reg bus ctrl 0—Controls this instance of the FIFO Register Bus FPGA library. This parameter must be wired to a control on the top-level FPGA VI, because it must be accessible to the FIFO Register Bus Host library from the FPGA Interface Read/Write Control function. The control must have a pre-defined name based on the value passed to the bus instance output of the Open Session VI in the FIFO Register Bus Host library. The format of the name is "fifo reg bus ctrl N", where N is the instance number of the FIFO Register Bus Host library and FIFO Register Bus FPGA library. For example, if the name is "fifo reg bus ctrl 0", the instance number of this library is 0. |

| Output parameters |
| --- |
| FIFO reg bus status 0—Indicates the status of the FIFO Register Bus FPGA library. This parameter must be wired to an indicator on the top-level FPGA VI, because it must be accessible to the FIFO Register Bus Host library from the FPGA Interface Read/Write Control function. The indicator must have a pre-defined name based on the value passed to the bus instance output of the Open Session VI in the FIFO Register Bus Host library. The format of the name is "fifo reg bus status N", where N is the instance number of the FIFO Register Bus Host library and FIFO Register Bus FPGA library. For example, if the name is "fifo reg bus status 0", the instance number of this library is 0. FIFO reg bus data 0—Returns data from a FIFO Register Bus read operation. This parameter must be wired to an indicator on the top-level FPGA VI, because it must be accessible to the FIFO Register Bus Host library from the FPGA Interface Read/Write Control function. The indicator must have a pre-defined name based on the value passed to the bus instance output of the Open Session VI in the FIFO Register Bus Host library. The format of the name is "fifo reg bus data N", where N is the instance number of the FIFO Register Bus Host library and FIFO Register Bus FPGA library. For example, if the name is "fifo reg bus data 0", the instance number of this library is 0. |

Parent topic:

FIFO Register Bus Overview

<!--NI_TOPIC bundle=ni-reconfigurable-oscilloscopes path=fifo-register-bus-host-vis.html language=enus -->
## TOPIC 00033: FIFO Register Bus Host VIs

- bundle_id: `ni-reconfigurable-oscilloscopes`
- source_path: `fifo-register-bus-host-vis.html`
- source_url: https://docs-be.ni.com/bundle/ni-reconfigurable-oscilloscopes/raw/resource/enus/fifo-register-bus-host-vis.html
- document_id: `ni-reconfigurable-oscilloscopes`
- page_type: `leaf`
- content_type: `concept`
- source_description: Open Session.viCreates an instruction target session that communicates with an FPGA target using a DMA FIFO. This session can communicate with a corresponding instance of the FIFO Register Bus library on the FPGA. Input parameters FGPA ref Specifies a reference to an FPGA VI with a FIFO Register Bus

### FIFO Register Bus Host VIs

#### Open Session.vi

Creates an instruction
 target session that communicates with an FPGA target using a DMA FIFO. This session
 can communicate with a corresponding instance of the FIFO Register Bus library on
 the FPGA.

[IMAGE alt='image' src='GUID-BDF5A541-3D04-4506-9D2F-1D2D88946FC3-a5.gif']

| Input parameters |
| --- |
| FGPA ref—Specifies a reference to an FPGA VI with a FIFO Register Bus host interface. Bus instance—Specifies which instance of the FIFO Register Bus library this VI should create. Multiple FIFO Register Bus instances may be created in an FPGA VI.Note This library supports a maximum of eight instances with bus instance values of 0 through 7. Error in—Describes error conditions that occur before this node runs. This input provides standard error in functionality. |

| Output parameters |
| --- |
| Session out—Passes a reference to your session to the next VI. Error out—Contains error information. This output provides standard error out functionality. |

#### Reset.vi

Resets the FIFO register
 bus.

[IMAGE alt='image' src='GUID-301F1A37-D17C-41A9-BFBD-9AC14D60CC5A-a5.gif']

| Input parameters |
| --- |
| Session in—Identifies your session. Session in is obtained from the Open Session VI of this library. Error in—Describes error conditions that occur before this node runs. This input provides standard error in functionality. |

| Output parameters |
| --- |
| Session out—Passes a reference to your session to the next VI. Error out—Contains error information. This output provides standard error out functionality. |

#### Close Session.vi

Closes the session and frees any allocated resources.

[IMAGE alt='image' src='GUID-BBFB1A3A-0E7A-4BD4-923F-7E06C2AF64A6-a5.gif']

| Input parameters |
| --- |
| Session in—Identifies your session. Session in is obtained from the Open Session VI of this library. Error in—Describes error conditions that occur before this node runs. This input provides standard error in functionality. |

| Output parameters |
| --- |
| Error out—Contains error information. This output provides standard error out functionality. |

#### Set Instruction FIFO Depth.vi

Sets the depth of the instruction FIFO. The depth of the FIFO affects the number of
 instructions that can be queued in the internal buffer.

[IMAGE alt='image' src='GUID-3B22AF03-FE18-4CA0-8DFB-5E19820CA7C6-a5.gif']

| Input parameters |
| --- |
| Session in—Identifies your session. Session in is obtained from the Open Session VI of this library. Instruction FIFO depth—Specifies the depth, in elements, of the host memory part of the Host to Target DMA FIFO used to transfer instructions from this instance of the FIFO Register Bus Host library to the corresponding instance of the FIFO Register Bus FPGA library. Error in—Describes error conditions that occur before this node runs. This input provides standard error in functionality. |

| Output parameters |
| --- |
| Session out—Passes a reference to your session to the next VI. Error out—Contains error information. This output provides standard error out functionality. |

#### Get Instruction FIFO Depth.vi

Returns the current depth setting of the instruction FIFO.

[IMAGE alt='image' src='GUID-B552FDEB-CD87-429D-B6A7-328163F8EBDF-a5.gif']

| Input parameters |
| --- |
| Session in—Identifies your session. Session in is obtained from the Open Session VI of this library. Error in—Describes error conditions that occur before this node runs. This input provides standard error in functionality. |

| Output parameters |
| --- |
| Session out—Passes a reference to your session to the next VI. Instruction FIFO depth—Returns the depth, in elements, of the host memory part of the Host to Target DMA FIFO used to transfer instructions from this instance of the FIFO Register Bus Host library to the corresponding instance of the FIFO Register Bus FPGA library. Error out—Contains error information. This output provides standard error out functionality. |

#### Read.vi

Returns a single value read from the target. The read instruction input specifies the
 subsystem ID and address of the data source.

[IMAGE alt='image' src='GUID-A7D931F3-B3A7-480A-8684-53767C10CD07-a5.gif']

| Input parameters |
| --- |
| Session in—Identifies your session. Session in is obtained from the Open Session VI of this library. Read instruction—Specifies the location of the data to read through a subsystem ID and an address. Read instruction.subsystem—The subsystem ID of the register to read. Read instruction.address—The address of the register to read. Timeout (1000 ms)—Specifies the minimum number of milliseconds for this VI to wait before timing out. This VI times out if the register read does not complete and data is not returned before the timeout that you specify elapses. Set this parameter to −1 if you want this VI to wait indefinitely. Error in—Describes error conditions that occur before this node runs. This input provides standard error in functionality. |

| Output parameters |
| --- |
| Session out—Passes a reference to your session to the next VI. Data—Returns the value read from the register subsystem and address specified in the read instruction input. Error out—Contains error information. This output provides standard error out functionality. |

#### Write.vi

Writes a single value to the target. The write instruction input specifies the
 subsystem ID and address of the write destination.

[IMAGE alt='image' src='GUID-F0A68069-EB32-4C99-9DCB-DDFD3A9E137D-a5.gif']

| Input parameters |
| --- |
| Session in—Identifies your session. Session in is obtained from the Open Session VI of this library. Write instruction—Specifies the data to write and the destination location. The destination is specified through a subsystem ID and an address. Write instruction.subsystem—The subsystem ID of the write destination. Write instruction.address—The address of the write destination. Write instruction.data—The data to write. Timeout (1000 ms)—Specifies the minimum number of milliseconds for this VI to wait before timing out. This VI times out if the session cannot write to the target, or if wait until committed is set to TRUE and the write is not verified before the timeout that you specify elapses. Set this parameter to −1 if you want this VI to wait indefinitely. Error in—Describes error conditions that occur before this node runs. This input provides standard error in functionality. Wait until committed (T)—Indicates whether this VI should stop running until it verifies that the target has received and processed the information in the write instruction input. This is an optional parameter. |

| Output parameters |
| --- |
| Session out—Passes a reference to your session to the next VI. Error out—Contains error information. This output provides standard error out functionality. |

#### Read Array.vi

Returns one or more values read from the target. The read instructions input
 specifies an array of subsystem IDs and addresses of data sources.

[IMAGE alt='image' src='GUID-77B1C2D7-B2AC-46C7-B8F5-3126753CB059-a5.gif']

| Input parameters |
| --- |
| Session in—Identifies your session. Session in is obtained from the Open Session VI of this library. Read instructions—Specifies an array of locations of data to read. Each element in this array contains a subsystem ID and an address. Read instructions.subsystem—The subsystem ID of the register to read. Read instructions.address—The address of the register to read. Timeout (1000 ms)—Specifies the minimum number of milliseconds for this VI to wait before timing out. This VI times out if the register read does not complete and data is not returned before the timeout that you specify elapses. Set this parameter to −1 if you want this VI to wait indefinitely. Error in—Describes error conditions that occur before this node runs. This input provides standard error in functionality. |

| Output parameters |
| --- |
| Session out—Passes a reference to your session to the next VI. Data—Returns an array of the data read from the register subsystems and addresses specified in the read instructions input array. Error out—Contains error information. This output provides standard error out functionality. |

#### Write Array.vi

Writes one or more values to the target. The write instructions input specifies an
 array of subsystem IDs and addresses of the write destinations.

[IMAGE alt='image' src='GUID-06FB0F6E-D2BC-48D9-8297-051FB5C4D495-a5.gif']

| Input parameters |
| --- |
| Session in—Identifies your session. Session in is obtained from the Open Session VI of this library. Write instructions—Specifies an array of data to write and destinations to write the data to. Each destination is specified by a subsystem ID and an address. Write instructions.subsystem—The subsystem ID of the write destination. Write instructions.address—The address of the write destination. Write instructions.data—The data to write. Timeout (1000 ms)—Specifies the minimum number of milliseconds for this VI to wait before timing out. This VI times out if the session cannot write to the target, or if wait until committed is set to TRUE and the write is not verified before the timeout that you specify elapses. Set this parameter to −1 if you want this VI to wait indefinitely. Error in—Describes error conditions that occur before this node runs. This input provides standard error in functionality. Wait until committed (T)—Indicates whether this VI should stop running until it verifies that the target has received and processed the information in the write instruction input. This is an optional parameter. |

| Output parameters |
| --- |
| Session out—Passes a reference to your session to the next VI. Error out—Contains error information. This output provides standard error out functionality. |

Parent topic:

FIFO Register Bus Overview

<!--NI_TOPIC bundle=ni-reconfigurable-oscilloscopes path=fifo-register-bus-overview.html language=enus -->
## TOPIC 00034: FIFO Register Bus Overview

- bundle_id: `ni-reconfigurable-oscilloscopes`
- source_path: `fifo-register-bus-overview.html`
- source_url: https://docs-be.ni.com/bundle/ni-reconfigurable-oscilloscopes/raw/resource/enus/fifo-register-bus-overview.html
- document_id: `ni-reconfigurable-oscilloscopes`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the FIFO Register Bus instrument design library to send register read and write instructions from your application on the host to the Instruction Framework FPGA Network. Other instrument design libraries on the FPGA can define a set of registers, which can be added as an Address Space in the Ins

### FIFO Register Bus Overview

Use the FIFO Register Bus instrument design library to send register read and write instructions
 from your application on the host to the Instruction Framework FPGA Network. Other
 instrument design libraries on the FPGA can define a set of registers, which can be
 added as an Address Space in the Instruction Framework FPGA Network. By using DMA to
 transfer data, the FIFO Register Bus library provides a significant performance benefit
 when you need to quickly issue a large number of register writes.

You can use multiple instances of the FIFO Register Bus instrument design library in your FPGA
 application. Using multiple instances of the FIFO Register Bus is useful in applications
 where independent components each send register instructions to the FPGA because each
 FIFO Register Bus instance has a separate DMA FIFO for data transfer. Different
 instances of the FIFO Register Bus can send register instructions to the same instrument
 design library on the FPGA. The Instruction Framework FPGA Network will automatically
 arbitrate among register instructions with the same destination and then route a
 completed read instruction to the instance of the FIFO Register Bus that issued it.

This instrument design library includes host VIs and FPGA VIs. For each instance of the FIFO
 Register Bus, the host writes register instructions into a Host to Target DMA FIFO. The
 FPGA reads a register instruction from the DMA FIFO, decodes it, and sends it to the
 Instruction Framework FPGA Network. The FPGA waits for the current register instruction
 to be processed before decoding and sending the next register instruction.

#### Thread Safety

Unsupported

[IMAGE alt='image' src='GUID-6F2AB728-7B00-4249-9605-A38185388964-a5.gif']

The FIFO Register Bus does not support opening multiple sessions to the same
 instance.

Supported

[IMAGE alt='image' src='GUID-6A436C0D-DDB9-4B7E-A181-2750F4E66B58-a5.gif']

You may branch the wire of a FIFO Register Bus session, and calls to the
 session will be thread-safe.

Supported

[IMAGE alt='image' src='GUID-F3EE749E-8937-4B8A-97AE-DF815AB3C1A6-a5.gif']

You may open multiple sessions if they are targeted towards different bus
 instances.

For more detailed information about the library interface, refer to
 the LabVIEW context help of the FIFO Register Bus LabVIEW VIs.

Parent topic:

LabVIEW Instrument Design Libraries for Reconfigurable Oscilloscopes

Related concepts:

- Instruction Framework Overview

<!--NI_TOPIC bundle=ni-reconfigurable-oscilloscopes path=flatness.html language=enus -->
## TOPIC 00035: Flatness

- bundle_id: `ni-reconfigurable-oscilloscopes`
- source_path: `flatness.html`
- source_url: https://docs-be.ni.com/bundle/ni-reconfigurable-oscilloscopes/raw/resource/enus/flatness.html
- document_id: `ni-reconfigurable-oscilloscopes`
- page_type: `leaf`
- content_type: `concept`
- source_description: Flatness is an effect on the acquired waveform that is frequency dependent. As the frequency rises, the amplitude slowly falls toward the 3 dB cutoff point of the bandwidth. When signals are composed entirely of frequencies below this cutoff point, the measured signal can appear slightly different t

### Flatness

Flatness is an effect on the acquired waveform that is frequency dependent. As the frequency
 rises, the amplitude slowly falls toward the 3 dB cutoff point of the bandwidth. When signals
 are composed entirely of frequencies below this cutoff point, the measured signal can appear
 slightly different than the input signal. The higher frequency components of the signal are
 attenuated more than the lower frequency components, changing the overall signal.

Flatness describes how well the analog front end passes signals of different frequencies. A
 maximally flat front end passes all frequencies with the same amount of attenuation, so the
 measured signal looks like the input signal. However, in the real world, as the frequency
 rises, the measured input signal slowly falls toward the –3 dB point.

[IMAGE alt='image' src='GUID-AE28DB71-B4E7-4AEB-8A85-B38D8A96F0A2-a5.gif']

Parent topic:

Oscilloscopes Fundamentals

<!--NI_TOPIC bundle=ni-reconfigurable-oscilloscopes path=frequency-domain-fundamentals.html language=enus -->
## TOPIC 00036: Frequency Domain Fundamentals

- bundle_id: `ni-reconfigurable-oscilloscopes`
- source_path: `frequency-domain-fundamentals.html`
- source_url: https://docs-be.ni.com/bundle/ni-reconfigurable-oscilloscopes/raw/resource/enus/frequency-domain-fundamentals.html
- document_id: `ni-reconfigurable-oscilloscopes`
- page_type: `leaf`
- content_type: `concept`

### Frequency Domain Fundamentals

- [Spurious Free Dynamic Range](spurious-free-dynamic-range.html)
- [Total Harmonic Distortion (THD)](thd.html)
- [Signal-to-Noise-and-Distortion (SINAD)](sinad.html)
- [Effective Number of Bits (ENOB)](enob.html)

Parent topic:

Oscilloscopes Fundamentals

<!--NI_TOPIC bundle=ni-reconfigurable-oscilloscopes path=gray-scale-image-and-extracted-line-profile.html language=enus -->
## TOPIC 00037: Gray Scale Image and Extracted Line Profile

- bundle_id: `ni-reconfigurable-oscilloscopes`
- source_path: `gray-scale-image-and-extracted-line-profile.html`
- source_url: https://docs-be.ni.com/bundle/ni-reconfigurable-oscilloscopes/raw/resource/enus/gray-scale-image-and-extracted-line-profile.html
- document_id: `ni-reconfigurable-oscilloscopes`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Complete NTSC Frame Scan image simulates the video display that would appear on a television screen if the following conditions were true: The television could show the entire line instead of just the active image part. The television was not interlacing the two fields to form a complete image f

### Gray Scale Image and Extracted Line Profile

The *Complete NTSC Frame Scan* image simulates the video display that would appear on
 a television screen if the following conditions were true:

- The television could show the entire line instead of just the active image part.
- The television was not interlacing the two fields to form a complete image frame, but instead was displaying a progressive scanning, line by line, of the entire frame.

The scanning starts (line-by-line from top to bottom) with a number of lines that represent the
 vertical synchronization pattern for the odd field. Immediately after the vertical
 synchronization pattern for the odd field, optional insertion test signals (ITS) are
 inserted. Finally, the actual odd field active image displays.

Note

The extracted line profile example at the bottom of the figure shows an actual video signal line
 extracted from the even field. Refer to *Video Levels* for more
 information.

Horizontal synchronization pulses are basically simple negative pulses, which are pulses going
 below the level of the luminance signal. However, the vertical synchronization signals
 are composed of pulse trains distributed on several lines, and the pulse trains are
 different for odd and even fields. The following figures show the vertical
 synchronization patterns for both fields and for several main video formats.

Figure 1.

[IMAGE alt='image' src='GUID-0D988405-F492-41D6-9CBD-5B35ABBB74FB-a5.gif']

Figure 2.

[IMAGE alt='image' src='GUID-B4FA116C-93F6-42E9-A2E4-3C13A9E17D62-a5.gif']

Figure 3.

[IMAGE alt='image' src='GUID-5A781C48-774A-4FDC-9939-93D48442D990-a5.gif']

Figure 4.

[IMAGE alt='image' src='GUID-0C5A6000-5EB1-48D3-84A2-FBDA9BAE5096-a5.gif']

Figure 5.

[IMAGE alt='image' src='GUID-A3B71B30-F15F-409F-8A4C-0DE7F72C8927-a5.gif']

Figure 6.

[IMAGE alt='image' src='GUID-3ABFE7E7-21FA-4050-9B51-EC23E5B22B1A-a5.gif']

Figure 7.

[IMAGE alt='image' src='GUID-5A3BC7BB-2F22-451F-B78E-C00517B0DA98-a5.gif']

Parent topic:

Video Fundamentals

Related concepts:

- Complete NTSC Frame Scan
- Active Image
- Video Levels

<!--NI_TOPIC bundle=ni-reconfigurable-oscilloscopes path=hysteresis-triggers.html language=enus -->
## TOPIC 00038: Hysteresis Triggers

- bundle_id: `ni-reconfigurable-oscilloscopes`
- source_path: `hysteresis-triggers.html`
- source_url: https://docs-be.ni.com/bundle/ni-reconfigurable-oscilloscopes/raw/resource/enus/hysteresis-triggers.html
- document_id: `ni-reconfigurable-oscilloscopes`
- page_type: `leaf`
- content_type: `concept`
- source_description: Hysteresis triggers eliminate incorrect triggers caused by noisy signals. For example, if your signal contains two rising edges of different amplitudes, you can use hysteresis triggering to trigger on one of the edges. Although NI-SCOPE uses a default amount of hysteresis for edge triggering, which

### Hysteresis Triggers

Hysteresis triggers eliminate incorrect triggers caused by noisy signals. For example, if your
 signal contains two rising edges of different amplitudes, you can use hysteresis triggering to
 trigger on one of the edges. Although NI-SCOPE uses a default amount of hysteresis for edge
 triggering, which is typically 2.5% of the vertical range, you can override that value by setting
 your own hysteresis values. The Configure Trigger Hysteresis function or VI
 allows you to choose the trigger coupling, trigger level, hysteresis value, and trigger
 slope.

Hysteresis triggering is possible on all analog trigger channels, such as 0, 1, or the external
 trigger input.

A positive slope hysteresis trigger is generated when the signal crosses below the voltage
 specified by the trigger level parameter minus the hysteresis value, and
 then crosses the trigger level.

[IMAGE alt='image' src='GUID-EA0DF018-9106-4B52-AFFD-59F7E6D6B0A3-a5.gif']

A negative slope hysteresis trigger is generated when a signal crosses above the voltage
 specified by the trigger level parameter plus the hysteresis value, and
 then crosses the trigger level.

[IMAGE alt='image' src='GUID-310217B2-C6FF-48FA-BF47-010B6D6D4C4C-a5.gif']

Parent topic:

Triggering

<!--NI_TOPIC bundle=ni-reconfigurable-oscilloscopes path=impedance-and-impedance-matching.html language=enus -->
## TOPIC 00039: Impedance and Impedance Matching

- bundle_id: `ni-reconfigurable-oscilloscopes`
- source_path: `impedance-and-impedance-matching.html`
- source_url: https://docs-be.ni.com/bundle/ni-reconfigurable-oscilloscopes/raw/resource/enus/impedance-and-impedance-matching.html
- document_id: `ni-reconfigurable-oscilloscopes`
- page_type: `leaf`
- content_type: `concept`
- source_description: When broadband signals are carried on transmission lines of any significant length, care must be taken that the transmission medium is matched to its terminations. The source and load impedances should equal the characteristic impedance of the transmission line, as this minimizes signal reflections.

### Impedance and Impedance Matching

When broadband signals are carried on transmission lines of any significant length, care must be
 taken that the transmission medium is matched to its terminations. The source and load impedances
 should equal the characteristic impedance of the transmission line, as this minimizes signal
 reflections. The presence of impedance discontinuities or mismatches degrades the amplitude and
 phase accuracy, as well as the temporal fidelity, of measurements made with a digitizer. The
 following example shows one of the most common mismatch errors encountered in such
 measurements.

#### Example

Selectable termination impedances are provided at the oscilloscope inputs to
 accommodate the most popular coaxial cable characteristic impedances: 50 Ω and 75 Ω. The
 following diagram illustrates what happens when a coaxial cable of the wrong characteristic
 impedance (50 Ω) is used with 75 Ω source and load impedances:

[IMAGE alt='image' src='GUID-890E4DEC-3564-4E24-BE3A-2F93ED0C2499-a5.gif']

The pulse encounters impedance mismatches at each end of the cable, whereupon it is
 partially reflected. The reflected pulse traverses the cable back and forth numerous times,
 diminishing at each end by the reflection coefficient, [IMAGE alt='image' src='GUID-BB91919B-6D69-4094-A947-C7E21E28CEB9-a5.gif'].

Γ

=

v

r

v

i

=

z

t

-

z

0

z

t

+

z

0

where

v<sub>r</sub> = reflected voltage,

v<sub>i</sub> = incident
 voltage,

z<sub>t</sub> = termination impedance,

z<sub>0</sub> = characteristic
 impedance.

The resulting voltage waveform recorded by the digitizer is distorted by the
 asymptotic decay of the reflected pulse as shown, exaggerated for visual effect. Impedance
 discontinuities of smaller magnitude and/or duration have correspondingly smaller effects. Also
 displayed is the waveform that results when a cable of matched impedance (75 Ω) is
 used.

#### Mismatch Uncertainty

Impedance matching is also
 important for preserving the absolute power measurement accuracy of an oscilloscope. The
 accuracy with which power can be measured is limited by mismatch error. The mismatch error in a
 system can be shown to be bounded by:

(

1

-

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

×

|

Γ

G

|

)

2

≤

mismatch error

≤

(

1

-

|

Γ

L

|

2

)

(

1

-

|

Γ

L

|

×

|

Γ

G

|

)

2

where

[IMAGE alt='image' src='GUID-BB91919B-6D69-4094-A947-C7E21E28CEB9-a5.gif']<sub>L</sub> =
 load reflection coefficient,

[IMAGE alt='image' src='GUID-BB91919B-6D69-4094-A947-C7E21E28CEB9-a5.gif']<sub>G</sub> = generator reflection coefficient.

The denominator
 term represents mismatch uncertainty, which is a fundamental limit to the power transfer
 accuracy that can be achieved across a mismatched junction.

#### Resistive Matching

Signal sources with low
 (high) source impedance can be matched with a resistor placed in series (shunt) such that the
 total source impedance (admittance) is matched to the cable characteristic impedance
 (admittance). Sources that are not capable of driving the cable impedance directly can be
 coupled through a matching L-pad, an example of which is shown in the following figure. In this
 case, the source sees a 500 Ω load, while the source impedance presented to the cable is 50 Ω.
 High-frequency components and layout techniques should be used throughout to minimize parasitic
 effects.

[IMAGE alt='image' src='GUID-DA221CDA-4B02-40BE-A2C3-46064844792A-a5.gif']

Parent topic:

Oscilloscopes Fundamentals

<!--NI_TOPIC bundle=ni-reconfigurable-oscilloscopes path=input-coupling.html language=enus -->
## TOPIC 00040: Input Coupling

- bundle_id: `ni-reconfigurable-oscilloscopes`
- source_path: `input-coupling.html`
- source_url: https://docs-be.ni.com/bundle/ni-reconfigurable-oscilloscopes/raw/resource/enus/input-coupling.html
- document_id: `ni-reconfigurable-oscilloscopes`
- page_type: `leaf`
- content_type: `concept`
- source_description: On many digitizers, you can configure the input channels to be DC-coupled, AC-coupled, or GND coupled. DC coupling allows DC and low-frequency components of a signal to pass through without attenuation. In contrast, AC coupling removes DC offsets and attenuates low frequency components of a signal.

### Input Coupling

On many digitizers, you can configure the input channels to be DC-coupled, AC-coupled, or GND
 coupled. DC coupling allows DC and low-frequency components of a
 signal to pass through without attenuation. In contrast, AC
 coupling removes DC offsets and attenuates low frequency
 components of a signal. This feature can be exploited to zoom in
 on AC signals with large DC offsets, such as switching noise on
 a 12 V power supply. GND coupling disconnects the input and
 internally connects the channel to ground to provide a ground,
 zero-voltage reference.

Refer to the *Specifications* for your specific digitizer for input limits that must
 be observed regardless of coupling.

Parent topic:

Oscilloscopes Fundamentals

<!--NI_TOPIC bundle=ni-reconfigurable-oscilloscopes path=instruction-framework-fpga-vis.html language=enus -->
## TOPIC 00041: Instruction Framework FPGA VIs

- bundle_id: `ni-reconfigurable-oscilloscopes`
- source_path: `instruction-framework-fpga-vis.html`
- source_url: https://docs-be.ni.com/bundle/ni-reconfigurable-oscilloscopes/raw/resource/enus/instruction-framework-fpga-vis.html
- document_id: `ni-reconfigurable-oscilloscopes`
- page_type: `leaf`
- content_type: `concept`
- source_description: Create Resources.vi Creates a register configuration object that you can use to connect instruction producers with subsystems. Use the Add Subsystems VI and Add Producer VI to connect libraries that are compatible with the Instruction Framework library. Input parameters Register clock Specifies the

### Instruction Framework FPGA VIs

#### Create Resources.vi

Creates a register configuration object that you can use to connect instruction
 producers with subsystems. Use the Add Subsystems VI and
 Add Producer VI to connect libraries that are compatible with
 the Instruction Framework library.

[IMAGE alt='image' src='GUID-5AD047DB-4FD7-406B-9725-875AD6738FEB-a5.gif']

| Input parameters |
| --- |
| Register clock—Specifies the clock source for the register configuration process. This clock source is also used for the Bus Interface VI of each address space, and the Fetch Instruction VI of each instruction producer. |

| Output parameters |
| --- |
| Register configuration—Returns the newly created register configuration object. |

#### Add Subsystems.vi

Connects address spaces to an existing register configuration object.

[IMAGE alt='image' src='GUID-EB0E21AE-300F-413A-83A1-CF5E575F85A3-a5.gif']

| Input parameters |
| --- |
| Register configuration in—Identifies the register configuration object. This parameter is obtained from the Create Resources VI of this library. Subsystems—Specifies an address space collection to add to the register configuration. Each address space contained by the collection is added as a separate subsystem. |

| Output parameters |
| --- |
| Register configuration out—Passes the modified register configuration object to the next VI. |

#### Add Producer.vi

Connects an instruction producer to an existing register configuration
 object.

[IMAGE alt='image' src='GUID-C9911908-07F8-41A4-98C3-14E691344ED8-a5.gif']

| Input parameters |
| --- |
| Register configuration in—Identifies the register configuration object. This parameter is obtained from the Create Resources VI of this library. Instruction producer—Specifies an instruction producer to add to the register configuration. |

| Output parameters |
| --- |
| Register configuration out—Passes the modified register configuration object to the next VI. |

#### Process.vi

Fetches and consumes instructions. This VI sends instructions from instruction
 producers to address spaces, then returns responses from the address spaces back to
 the instruction producers. Place this VI at the end of a configuration
 chain.

[IMAGE alt='image' src='GUID-030EF099-3E69-48CE-BDE0-D165B8FE7417-a5.gif']

| Input parameters |
| --- |
| Register configuration—Identifies the register configuration object. This parameter is obtained from the Create Resources VI. |

Parent topic:

Instruction Framework Overview

<!--NI_TOPIC bundle=ni-reconfigurable-oscilloscopes path=instruction-framework-host-vis.html language=enus -->
## TOPIC 00042: Instruction Framework Host VIs

- bundle_id: `ni-reconfigurable-oscilloscopes`
- source_path: `instruction-framework-host-vis.html`
- source_url: https://docs-be.ni.com/bundle/ni-reconfigurable-oscilloscopes/raw/resource/enus/instruction-framework-host-vis.html
- document_id: `ni-reconfigurable-oscilloscopes`
- page_type: `leaf`
- content_type: `concept`
- source_description: Context Read.vi Returns a single value read from the target. Data source is specified by context and address. Input parameters Instruction target in Identifies your session. Context in Identifies the address space to read data from. This value is obtained from the Subsystem Lookup VI of this library

### Instruction Framework Host VIs

#### Context Read.vi

Returns a single value read from the target. Data source is specified by context and
 address.

[IMAGE alt='image' src='GUID-BACD598A-F308-4BEE-99E7-D4BDA43318B8-a5.gif']

| Input parameters |
| --- |
| Instruction target in—Identifies your session. Context in—Identifies the address space to read data from. This value is obtained from the Subsystem Lookup VI of this library. Address—Specifies the address to read data from, relative to the address space associated with the context in input. Timeout (5000 ms)—Specifies the minimum number of milliseconds for this VI to wait before timing out. This VI times out if the register read does not complete and data is not returned before the timeout that you specify elapses. Set this parameter to −1 if you want this VI to wait indefinitely. Error in—Describes error conditions that occur before this node runs. This input provides standard error in functionality. |

| Output parameters |
| --- |
| Instruction target out—Passes a reference to your session to the next VI. Context out—Passes a reference to the context to the next VI. Data—Returns the data read from the address space. Error out—Contains error information. This output provides standard error out functionality. |

#### Context Write.vi

Writes a single value to the target. Destination is specified by context and
 address.

[IMAGE alt='image' src='GUID-CFAE124D-493F-459C-A01C-83A0C0223FED-a5.gif']

| Input parameters |
| --- |
| Instruction target in—Identifies your session. Context in—Identifies the address space to write data to. This value is obtained from the Subsystem Lookup VI of this library. Address—Specifies the address to write data to, relative to the address space associated with the context in input. Data—Specifies the data to write to the address space. Error in—Describes error conditions that occur before this node runs. This input provides standard error in functionality. Timeout (5000 ms)—Specifies the minimum number of milliseconds for this VI to wait before timing out. This VI times out if the session cannot write to its target, or if wait until committed is set to TRUE and the write is not verified before the timeout that you specify elapses. Set this parameter to −1 if you want this VI to wait indefinitely. Wait until committed (T)—Indicates whether this VI should stop running until it verifies that the target has received and processed the information in the data input. This is an optional parameter. |

| Output parameters |
| --- |
| Instruction target out—Passes a reference to your session to the next VI. Context out—Passes a reference to the context to the next VI. Error out—Contains error information. This output provides standard error out functionality. |

#### Context Read Array.vi

Returns one or more values read from the target. Data sources are specified by
 context and an array of addresses.

[IMAGE alt='image' src='GUID-08C32567-B97A-4BE1-86F5-EBFA1D6BDAA7-a5.gif']

| Input parameters |
| --- |
| Instruction target in—Identifies your session. Context in—Identifies the address space to read data from. This value is obtained from the Subsystem Lookup VI of this library. Addresses—Specifies a list of addresses to read data from, relative to the address space associated with the context in input. Timeout (5000 ms)—Specifies the minimum number of milliseconds for this VI to wait before timing out. This VI times out if the register read does not complete and data is not returned before the timeout that you specify elapses. Set this parameter to −1 if you want this VI to wait indefinitely. Error in—Describes error conditions that occur before this node runs. This input provides standard error in functionality. |

| Output parameters |
| --- |
| Instruction target out—Passes a reference to your session to the next VI. Context out—Passes a reference to the context to the next VI. Data—Returns an array of data read from the address space. Error out—Contains error information. This output provides standard error out functionality. |

#### Context Write Array.vi

Writes one or more values to the target. Destinations are specified by context and
 the addresses in the write instructions array.

[IMAGE alt='image' src='GUID-F575B576-44B9-4B90-A63C-344EA90CDD84-a5.gif']

| Input parameters |
| --- |
| Instruction target in—Identifies your session. Context in—Identifies the address space to write data to. This value is obtained from the Subsystem Lookup VI of this library. Write instructions—An array where each element contains data to write and the address to write the data to. Write instructions.address—The address to write to, relative to the address space associated with the context in input. Write instructions.data—The data to write. Timeout (5000 ms)—Specifies the minimum number of milliseconds for this VI to wait before timing out. This VI times out if the session cannot write to its target, or if wait until committed is set to TRUE and the write has not been verified before the timeout that you specify elapses. Set this parameter to −1 if you want this VI to wait indefinitely. Error in—Describes error conditions that occur before this node runs. This input provides standard error in functionality. Wait until committed (T)—Indicates whether this VI should stop running until it verifies that the target has received and processed the information in the data input. This is an optional parameter. |

| Output parameters |
| --- |
| Instruction target out—Passes a reference to your session to the next VI. Context out—Passes a reference to the context to the next VI. Error out—Contains error information. This output provides standard error out functionality. |

#### Read Subsystem Map.vi

Retrieves information about the subsystem map from a given target. Returns a list of
 which address spaces have been connected to the bus, and the routing context
 required to communicate with these address spaces.

[IMAGE alt='image' src='GUID-5887D8B2-128F-490A-B787-F8FC8985C325-a5.gif']

| Input parameters |
| --- |
| Instruction target in—Specifies the target to read the subsystem map from. Error in—Describes error conditions that occur before this node runs. This input provides standard error in functionality. |

| Output parameters |
| --- |
| Instruction target out—Passes a reference to your session to the next VI. Subsystem map—Contains the address space map data. Error out—Contains error information. This output provides standard error out functionality. |

#### Subsystem Lookup.vi

Returns the context for a given address space.

[IMAGE alt='image' src='GUID-45F99223-88D5-4AC2-A292-BD46E5CF0509-a5.gif']

| Input parameters |
| --- |
| Subsystem map in—The address space map data obtained from the Read Subsystem Map VI of this library. Set error if not found (T)—Specifies whether or not this VI should return an error if the lookup fails. UID—The unique identifier of the address space to look up. Instance—Specifies the instance of the address space to look up. Parent context—Specifies a context for the parent of the address space to look up. This parameter is obtained from the context output of a previous instance of this VI. Error in—Describes error conditions that occur before this node runs. This input provides standard error in functionality. |

| Output parameters |
| --- |
| Found?—TRUE if the address space lookup was successful. Subsystem map out—Passes the subsystem map to the next VI. Context—Contains lookup and routing information necessary to reference the address space found by this VI. Error out—Contains error information. This output provides standard error out functionality. |

#### Subsystem Version Check.vi

Performs a version check, comparing a potential host code version to the version
 reported by an address space on the target.

[IMAGE alt='image' src='GUID-2A0DDBBC-5ED9-43CC-89F6-ECA4F74EAF3B-a5.gif']

| Input parameters |
| --- |
| Subsystem map in—The address space map data obtained from the Read Subsystem Map VI of this library. Set error if version mismatch (T)—Specifies whether this VI should return an error if the version found is not within the range specified by the version and oldest compatible version inputs. Context—Specifies the address space to version check. Version—Specifies the version of the host code that is performing the version check. Oldest compatible version—Specifies the oldest version that the host code is backwards-compatible with. Error in—Describes error conditions that occur before this node runs. This input provides standard error in functionality. |

| Output parameters |
| --- |
| Subsystem map out—Passes the subsystem map to the next VI. Target too old—TRUE if the target address space is too old to be compatible with the specified oldest compatible version of the host code. Target too new—TRUE if the target address space is too new and is not backwards-compatible with the specified version of the host code. Error out—Contains error information. This output provides standard error out functionality. |

#### Read.vi

Returns a single value read from the target. The read instruction input specifies the
 subsystem ID and address of the data source.

[IMAGE alt='image' src='GUID-F73BFDF4-F392-4857-99E0-1ADBF691668C-a5.gif']

| Input parameters |
| --- |
| Instruction target in—Identifies your session. Read instruction—Specifies the location of the data to read through a subsystem ID and an address. Read instruction.subsystem—The subsystem ID of the register to read. Read instruction.address—The address of the register to read. Timeout—Specifies the minimum number of milliseconds for this VI to wait before timing out. This VI times out if the register read does not complete and data is not returned before the timeout that you specify elapses. Set this parameter to −1 if you want this VI to wait indefinitely. Error in—Describes error conditions that occur before this node runs. This input provides standard error in functionality. |

| Output parameters |
| --- |
| Instruction target out—Passes a reference to your session to the next VI. Data—Returns the value read from the register subsystem and address specified in the read instruction input. Error out—Contains error information. This output provides standard error out functionality. |

#### Write.vi

Writes a single value to the target. The write instruction input specifies the
 subsystem ID and address of the write destination.

[IMAGE alt='image' src='GUID-001A7CDF-3367-4F33-9FDA-D96F89DC5B1D-a5.gif']

| Input parameters |
| --- |
| Instruction target in—Identifies your session. Write instruction—Specifies the data to write and the destination location. The destination is specified through a subsystem ID and an address. Write instruction.subsystem—The subsystem ID of the write destination. Write instruction.address—The address of the write destination. Write instruction.data—The data to write. Timeout—Specifies the minimum number of milliseconds for this VI to wait before timing out. This VI times out if the session cannot write to the target, or if wait until committed is set to TRUE and the write is not verified before the timeout that you specify elapses. Set this parameter to −1 if you want this VI to wait indefinitely. Error in—Describes error conditions that occur before this node runs. This input provides standard error in functionality. Wait until committed—Indicates whether this VI should stop running until it verifies that the target has received and processed the information in the write instruction input. This is an optional parameter. |

| Output parameters |
| --- |
| Instruction target out—Passes a reference to your session to the next VI. Error out—Contains error information. This output provides standard error out functionality. |

#### Read Array.vi

Returns one or more values read from the target. The read instructions input
 specifies an array of subsystem IDs and addresses of data sources.

[IMAGE alt='image' src='GUID-805A7FA3-737C-4F31-8314-F3DA4058AF80-a5.gif']

| Input parameters |
| --- |
| Instruction target in—Identifies your session. Read instructions—Specifies an array of locations of data to read. Each element in this array contains a subsystem ID and an address. Read instructions.subsystem—The subsystem ID of the register to read. Read instructions.address—The address of the register to read. Timeout—Specifies the minimum number of milliseconds for this VI to wait before timing out. This VI times out if the register read does not complete and data is not returned before the timeout that you specify elapses. Set this parameter to −1 if you want this VI to wait indefinitely. Error in—Describes error conditions that occur before this node runs. This input provides standard error in functionality. |

| Output parameters |
| --- |
| Instruction target out—Passes a reference to your session to the next VI. Data—Returns an array of the data read from the register subsystems and addresses specified in the read instructions input array. Error out—Contains error information. This output provides standard error out functionality. |

#### Write Array.vi

Writes one or more values to the target. The write instructions input specifies an
 array of subsystem IDs and addresses of the write destinations.

[IMAGE alt='image' src='GUID-7200870B-CAFE-4624-94EE-BF391F5FAB88-a5.gif']

| Input parameters |
| --- |
| Instruction target in—Identifies your session. Write instructions—Specifies an array of data to write and destinations to write the data to. Each destination is specified by a subsystem ID and an address. Write instructions.subsystem—The subsystem ID of the write destination. Write instructions.address—The address of the write destination. Write instructions.data—The data to write. Timeout—Specifies the minimum number of milliseconds for this VI to wait before timing out. This VI times out if the session cannot write to the target, or if wait until committed is set to TRUE and the write is not verified before the timeout that you specify elapses. Set this parameter to −1 if you want this VI to wait indefinitely. Error in—Describes error conditions that occur before this node runs. This input provides standard error in functionality. Wait until committed—Indicates whether this VI should stop running until it verifies that the target has received and processed the information in the write instruction input. This is an optional parameter. |

| Output parameters |
| --- |
| Instruction target out—Passes a reference to your session to the next VI. Error out—Contains error information. This output provides standard error out functionality. |

#### Contextualize Read.vi

Applies a context to an address and returns the resulting read instruction. This
 context is used by other VIs in this library to access this address for read or
 write operations.

[IMAGE alt='image' src='GUID-0966C824-A78C-438C-B3AC-13EE839A23A4-a5.gif']

| Input parameters |
| --- |
| Context in—Specifies the address space used to create the read instruction. Address—Specifies the address to read data from. This address is relative to the address space specified by context in. Error in—Describes error conditions that occur before this node runs. This input provides standard error in functionality. |

| Output parameters |
| --- |
| Context out—Passes a reference to the context to the next VI. Read instruction—Returns the data required to read data from a register. Read instruction.subsystem—The subsystem ID of the register to read. Read instruction.address—The address of the register to read. Error out—Contains error information. This output provides standard error out functionality. |

#### Contextualize Write.vi

Applies a context to an address and returns the resulting write instruction. This
 context is used by other VIs in this library to access this address for read or
 write operations.

[IMAGE alt='image' src='GUID-9844441C-5DEE-4DED-9F59-D9BDBE6C04EA-a5.gif']

| Input parameters |
| --- |
| Context in—Specifies the address space used to create the write instruction. Address—Specifies the address to write data to. This address is relative to the address space specified by context in. Data—The data to write. Error in—Describes error conditions that occur before this node runs. This input provides standard error in functionality. |

| Output parameters |
| --- |
| Context out—Passes a reference to the context to the next VI. Write instruction—Returns the information needed to write to a location. Write instruction.subsystem—The subsystem ID of the write destination. Write instruction.address—The address of the write destination. Write instruction.data—The data to write. Error out—Contains error information. This output provides standard error out functionality. |

#### Reset.vi

Resets the specified Instruction Target.

[IMAGE alt='image' src='GUID-59D85B32-BDC2-405F-8F63-984EEF924A1C-a5.gif']

| Input parameters |
| --- |
| Instruction target in—Identifies your session. Error in—Describes error conditions that occur before this node runs. This input provides standard error in functionality. |

| Output parameters |
| --- |
| Instruction target out—Passes a reference to your session to the next VI. Error out—Contains error information. This output provides standard error out functionality. |

Parent topic:

Instruction Framework Overview

<!--NI_TOPIC bundle=ni-reconfigurable-oscilloscopes path=instruction-framework-overview.html language=enus -->
## TOPIC 00043: Instruction Framework Overview

- bundle_id: `ni-reconfigurable-oscilloscopes`
- source_path: `instruction-framework-overview.html`
- source_url: https://docs-be.ni.com/bundle/ni-reconfigurable-oscilloscopes/raw/resource/enus/instruction-framework-overview.html
- document_id: `ni-reconfigurable-oscilloscopes`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the Instruction Framework instrument design library to build a communication network in LabVIEW FPGA. The network has two types of endpoints: Instruction Producers and Address Spaces. Instruction Producers issue read and write instructions that are targeted for a particular Address Space. When t

### Instruction Framework Overview

Use the Instruction Framework instrument design library to build a communication network in
 LabVIEW FPGA. The network has two types of endpoints: *Instruction Producers*
 and *Address Spaces*. *Instruction Producers* issue read and write
 instructions that are targeted for a particular *Address Space*. When the
 destination *Address Space* completes an instruction, it provides a response
 which is routed back to the *Instruction Producer* that issued the
 instruction, as shown in the following diagram:

[IMAGE alt='image' src='GUID-1098A1B5-6FC5-48E3-8CD4-92C9E91F0336-a5.gif']

The Instruction Framework instrument design library includes some host VIs, to help with
 communication between host libraries, and FPGA address spaces. The Subsystem Map class
 provides a way to look-up the location of an *Address Space* on the host,
 using the *Address Space*'s unique identifier (UID). A context object is
 returned from this lookup function, which can be used to specify the destination for a
 read or write operation.

The Instruction Target class is intended to be used as an abstract interface for the mechanism
 used to communicate with the Instruction Framework FPGA Network. The FIFO Register Bus
 instrument design library provides an Instruction Target implementation on the host,
 which is coupled to an *Instruction Producer* implementation on the FPGA.
 This allows a host controller to send instructions to *Address Spaces* on the
 FPGA, and read the resulting responses. The instructions are sent to the FPGA using a
 uniquely named DMA FIFO, and the responses are received using a uniquely named
 indicator.

Some instrument design libraries use the Instruction Framework as a configuration mechanism.
 These libraries require a Subsystem Map object to look-up the location of corresponding
 *Address Spaces* on the FPGA. These libraries will also require an
 Instruction Target to provide the communication mechanism from the host controller to an
 *Instruction Producer* on the Instruction Framework FPGA Network. The
 corresponding *Address Spaces* must be added to the Instruction Framework
 FPGA Network in order for the host library to communicate properly with the FPGA
 library. This *Address Space* implementation provides register access through
 an *Instruction Producer*, such as the FIFO Register Bus library, instead of
 using controls and indicators on the top level of the FPGA diagram.

Parent topic:

LabVIEW Instrument Design Libraries for Reconfigurable Oscilloscopes

Related concepts:

- FIFO Register Bus Overview

<!--NI_TOPIC bundle=ni-reconfigurable-oscilloscopes path=interlaced-scanning.html language=enus -->
## TOPIC 00044: Interlaced Scanning

- bundle_id: `ni-reconfigurable-oscilloscopes`
- source_path: `interlaced-scanning.html`
- source_url: https://docs-be.ni.com/bundle/ni-reconfigurable-oscilloscopes/raw/resource/enus/interlaced-scanning.html
- document_id: `ni-reconfigurable-oscilloscopes`
- page_type: `leaf`
- content_type: `concept`
- source_description: All composite video systems display the video image on a TV screen using an interlaced scanning technique. The following figure shows the interlaced scanning concept. Interlaced Scanning Concept The analog video signal includes synchronization pulses that control the scanning line-by-line from left

### Interlaced Scanning

All composite video systems display the video image on a TV screen using an interlaced scanning
 technique. The following figure shows the interlaced scanning concept.

[IMAGE alt='image' src='GUID-D1ABBD61-1C38-4614-9956-A6861C9FF1FC-a5.gif']

#### Interlaced Scanning Concept

The analog video signal includes synchronization pulses that control the scanning line-by-line from left to right and field-by-field from top to bottom. The pulses that control the line-by-line scanning are called the horizontal synchronization pulses (Hsync). The pulses that control the vertical scanning are called the vertical synchronization pulses (Vsync).

Two interlaced fields compose a *complete frame*. The first field, called the odd field, scans the odd lines of the video image. The second field, called the even field, scans the even lines of the video image. The process repeats for every frame.

Parent topic:

Video Fundamentals

Related concepts:

- Complete NTSC Frame Scan

<!--NI_TOPIC bundle=ni-reconfigurable-oscilloscopes path=multirecord-acquisition-fpga-vis.html language=enus -->
## TOPIC 00045: Multirecord Acquisition FPGA VIs

- bundle_id: `ni-reconfigurable-oscilloscopes`
- source_path: `multirecord-acquisition-fpga-vis.html`
- source_url: https://docs-be.ni.com/bundle/ni-reconfigurable-oscilloscopes/raw/resource/enus/multirecord-acquisition-fpga-vis.html
- document_id: `ni-reconfigurable-oscilloscopes`
- page_type: `leaf`
- content_type: `concept`
- source_description: Create Status DMA FIFO Resources.viInstantiates the internal DMA status resources that the Multirecord Acquisition FPGA library uses and bundles them with the external resource that you specify. Input parameters Status DMA FIFO in Specifies the DMA FIFO, instantiated in the LabVIEW project, that the

### Multirecord Acquisition FPGA VIs

#### Create Status DMA FIFO
 Resources.vi

Instantiates the internal DMA status resources that the
 Multirecord Acquisition FPGA library uses and bundles them with the external
 resource that you specify.

[IMAGE alt='image' src='GUID-5886FAFF-6491-4B8E-AA17-A58B76B61AB2-a5.gif']

| Input parameters |
| --- |
| Status DMA FIFO in—Specifies the DMA FIFO, instantiated in the LabVIEW project, that the host uses to read status information about the acquisition state. The DMA FIFO must have a predefined name based on the value passed to the FIFO instance input. The format of the name is acq.status fifo N, where N is the FIFO instance. For example, if the name is acq.status fifo 0 the FIFO instance must be 0.The simplest method to instantiate a LabVIEW FPGA DMA FIFO is to copy and paste the FIFO from a sample project that already contains the FIFO, and update its configuration as required. Click the Create Project button on the LabVIEW Getting Started window to view the sample project. FIFO instance—Specifies the status DMA FIFO instance number. This number must match the suffix of the FIFO name passed to status DMA FIFO in. |

| Output parameters |
| --- |
| Status DMA FIFO out—Returns a reference to the status dma FIFO resource. This reference should be wired to the Create Resources VI. |

#### Create Fetch DMA FIFO
 Resources.vi

Instantiates the internal DMA fetch resources that the
 Multirecord Acquisition FPGA library uses and bundles them with the external
 resource that you specify.

[IMAGE alt='image' src='GUID-8DD74060-DCCF-45F5-9926-36E713F5337E-a5.gif']

| Input parameters |
| --- |
| Fetch DMA FIFO in—Specifies the DMA FIFO, instantiated in the LabVIEW project, that the host uses to fetch acquired waveforms from the device. The DMA FIFO must have a predefined name based on the value passed to the FIFO instance input. The format of the name is acq.fetch fifo N, where N is the FIFO instance. For example, if the name is acq.fetch fifo 0, the FIFO instance must be 0.The simplest method to instantiate a LabVIEW FPGA DMA FIFO is to copy and paste the FIFO from a sample project that already contains the FIFO, and update its configuration as required. Click the Create Project button on the LabVIEW Getting Started window to view the sample project. FIFO instance—Specifies the fetch DMA FIFO instance number. This number must match the suffix of the FIFO name passed to fetch DMA FIFO in. |

| Output parameters |
| --- |
| Fetch DMA FIFO out—Returns a reference to the fetch dma FIFO resource. This reference should be wired to the Create Resources VI. |

#### Create Resources.vi

Instantiates the
 internal memories, FIFOs, and other resources that the Multirecord Acquisition FPGA
 library uses and bundles them with the external resources that you
 specify.

Wire the acquisition output of this VI to the other Multirecord
 Acquisition FPGA VIs that are used with this acquisition library instance in your
 FPGA application.

[IMAGE alt='image' src='GUID-25426FD4-1766-4DC2-B339-4CF6D6D86060-a5.gif']

| Input parameters |
| --- |
| Memory clock—Specifies the clock domain used in the low-level read and write operations to DRAM. Use a faster clock to get better memory throughput and a slower clock to help the FPGA compilation meet timing constraints. The ideal clock rate for maximum throughput is the native DRAM clock rate of the FPGA target. The frequency of this clock can vary across different types of FPGA targets. Refer to the help file for the hardware that you use as the LabVIEW FPGA target for more information about the native DRAM clock rate. Instance—Specifies the instance number of this Multirecord Acquisition FPGA library instantiation. The value that you specify for instance must be equal to the instance number that you specify in the Open Session VI of the Multirecord Acquisition host library. Memory—Specifies the LabVIEW FPGA memory instatiated in the LabVIEW project that stores the acquired waveforms. This memory must either use DRAM or Block RAM for its implementation. DRAM is, instantiated in the LabVIEW project, while Block RAM is VI Defined. The data type of this memory must match the type specified by the instance of the VI you are using.The simplest method to instantiate a LabVIEW FPGA DRAM memory is to copy and paste an equivalent memory item from a sample project that already contains the memory item, and update its configuration as required. Click the Create Project button on the LabVIEW Getting Started window to view the sample project. Memory size (bytes)—Specifies the size in bytes of the memory specified by memory. Status DMA FIFO resource—Specifies the DMA FIFO resource that the host uses to read status information about the acquisition state. The DMA FIFO resource is created by the Create Status DMA FIFO Resources VI. Fetch DMA FIFO resource—Specifies the DMA FIFO resource that the host uses to fetch acquired waveforms from the device. The DMA FIFO resource is created by the Create Fetch DMA FIFO Resources VI. |

| Output parameters |
| --- |
| Acquisition resources—Returns the internal resources and resources that you specify, which this instance of the Multirecord Acquisition FPGA library uses. Wire this parameter to other Multirecord Acquisition VIs that you use with this instance of the Multirecord Acquisition library. Acquisition subsystem—Returns the resources used by the Multirecord Acquisition FPGA Library to communicate with the host. Connect this wire to the Instruction Framework library using the Add Subsystem VI. |

#### Set
 Input FIFO.vi

Specifies the FIFO used as the write FIFO. This FIFO accepts
 the samples that you write to the Write VI and transfers them to
 the memory clock domain to write to memory.

[IMAGE alt='image' src='GUID-E02BCF5D-4E33-42BF-9006-BDA70338970D-a5.gif']

#### Set Request FIFO.vi

Specifies the FIFO
 used to queue record read requests. This FIFO resides in the memory clock
 domain.

[IMAGE alt='image' src='GUID-A780AB56-B895-477B-9D40-1B1FF9341B6B-a5.gif']

#### Set
 Retrieve FIFO.vi

Specifies the FIFO used to retrieve record data that you
 request from memory. This FIFO accepts samples read directly from the memory and
 transfers them to the clock domain to retrieve record data using the
 Retrieve Record VI.

[IMAGE alt='image' src='GUID-B74B817D-263B-46D7-9F81-62B8A52CBC2D-a5.gif']

#### Set
 Timestamp FIFO.vi

Specifies the FIFO used to capture timestamp values.
 This FIFO accepts timestamp values that you write to the Write VI
 and transfers the timestamp values to the memory clock domain to correlate to the
 correct record data that you write to memory.

[IMAGE alt='image' src='GUID-2EDA8248-2F8E-49FF-9054-92B17A684EC7-a5.gif']

#### Process.vi

Contains the free-running
 process of the Multirecord Acquisition FPGA library. This process implements the
 various state machines and services needed to provide the core Multirecord
 Acquisition functionality. This VI also implements interaction with DRAM
 memory.

At least one instance of this VI must be present in your FPGA design
 for each instance of the Multirecord Acquisition library.

[IMAGE alt='image' src='GUID-D1932008-5754-4B54-BB01-0642A72100F0-a5.gif']

| Input parameters |
| --- |
| Acquisition resources—Specifies the resources that the current instance of the library uses. You can obtain this value from the Create Resources VI of the Multirecord Acquisition FPGA library. |

#### Retrieve Record.vi

Retrieves the record data that you previously
 requested from the device. You can request the record data using the Fetch
 Single Record VI, Fetch Multiple Records VI, or
 Request Record VI in the Multirecord Acquisition host
 library.

All samples that you retrieve from this VI are presented in the order
 in which they were fetched. You can add FPGA logic to perform FPGA-side processing
 of the record data after this VI.

[IMAGE alt='image' src='GUID-C5241ECD-EEDB-4EA3-9CFE-311981FB0847-a5.gif']

| Input parameters |
| --- |
| Acquisition resources—Specifies the resources that the current instance of the Multirecord Acquisition library uses. You can obtain this value from the Create Resources VI of the Multirecord Acquisition FPGA library. Output array size—Specifies the requested array size of data. This value must be a constant and a power of 2. If you are retrieving multiple channels, this value must be a multiple of the number of channels in the request. Ready for output—Specifies whether the logic that comes after this VI is ready to accept a new data value. |

| Output parameters |
| --- |
| Channels—Returns the number of channels contained in data. Data—Returns the data sample that the VI retrieves. If data contains multiple channels then the channels are returned in an interleaved format starting with channel 0. Retrieve data info—Returns information about the request. Retrieve data info.last sample of data request—Indicates that data contains the last sample of the current request. Wire this value to the Write to Fetch DMA FIFO VI. Retrieve data info.token—Specifies a user defined value that is specified by the host using Fetch Single Record, Fetch Multiple Records, or Request Record VIs. Output valid—Indicates whether the data output contains valid data. output valid returns TRUE for the clock cycles in which data contains a valid data sample. Otherwise, output valid returns FALSE. |

#### Write to Fetch DMA FIFO.vi

Writes data to the Fetch DMA FIFO. Use the
 Fetch FIFO to transmit record data from the FPGA to the record fetch VIs on the
 host.

Connect this VI to the Retrieve Record VI on the
 FPGA. You can add custom logic between these two VIs to perform custom FPGA
 processing on the record data.

[IMAGE alt='image' src='GUID-DC5B4E79-E2F7-44D9-94E6-A62D4F1309CD-a5.gif']

| Input parameters |
| --- |
| Data—Specifies the data sample to write to the Fetch DMA FIFO. Acquisition resources—Specifies the resources that the current instance of the Multirecord Acquisition library uses. You can obtain this value from the Create Resources VI of this library. Channels—Specifies the number of channels contained in data. Last sample of request—Specifies that data contains the last sample of the current request. Wire this value from the Retrieve Record VI. Input valid—Specifies whether the data input contains valid data. |

| Output parameters |
| --- |
| Ready for input—Indicates whether this VI is ready to accept a new data value on the next clock cycle. ready for input returns TRUE if the Write to Fetch DMA FIFO VI is ready to accept a new data value on the next clock cycle. ready for input returns FALSE if the VI is not ready to accept a new data value on the next clock cycle. |

#### Write.vi

Writes sample data into record memory, which is stored in
 DRAM/Block RAM. This VI evaluates various acquisition triggers and decides whether
 to acquire each data value into record memory. This VI organizes the stream of data
 values into discrete records based on the acquisition configuration and behavior of
 the acquisition triggers.

Whenever records are acquired, this VI also returns
 state information about the acquisition. The host application can read the acquired
 records from DRAM/Block RAM using the Fetch Single Record VI and
 the Fetch Multiple Records VI of the Multirecord Acquisition host
 library.

[IMAGE alt='image' src='GUID-997813DE-EE15-48E6-8A47-C6E64C13045F-a5.gif']

| Input parameters |
| --- |
| Data—Specifies the data sample to write to the Fetch DMA FIFO. Acquisition resources—Specifies the resources that the current instance of the Multirecord Acquisition library uses. You can obtain this value from the Create Resources VI of the Multirecord Acquisition FPGA library. Triggers—Specifies the triggers that the Write VI uses to determine when to start and stop storing samples for a record. Triggers.start trigger—specifies the acquisition start trigger. After the Initiate VI on the host initiates the acquisition, the Write VI waits for start trigger to assert prior to acquiring any record data to memory. Set start trigger to TRUE to assert the trigger. This trigger is a level-sensitive signal that is evaluated only once at the beginning of the acquisition. Triggers.advance trigger (T)—Specifies the record advance trigger. After you acquire each record fully, the Write VI waits for advance trigger input to assert prior to acquiring any data for the next record. Set advance trigger to TRUE to assert the trigger. This trigger is a level-sensitive signal that is evaluated once at the beginning of each record. The advance trigger is not evaluated prior to acquiring the first record. The advance trigger is evaluated prior to acquiring all other records.If the acquisition is configured for an infinite number of samples, this trigger is ignored. Triggers.reference trigger (T)—Specifies the record reference trigger. If you configure this acquisition for a finite number of samples, the Write VI uses the reference trigger to bind the number of samples that you write to each record. The Write VI continually acquires samples to record memory until reference trigger asserts. After reference trigger asserts, this VI acquires a finite number of samples beyond the reference trigger. The number of samples that the Write VI acquires beyond the reference trigger is based on the acquisition configuration and can be determined by the following formula:Reference trigger = (number of samples in record) - (number of pretrigger samples)Set reference trigger to TRUE to assert the trigger. This trigger is a level-sensitive signal.If you configure the acquisition for an infinite number of samples, the Write VI ignores this trigger. Triggers.start trigger index—Specifies the index of the sample that corresponds to the start trigger. Use this input when supplying more than one sample per FPGA clock cycle. Triggers.advance trigger index—Specifies the index of the sample that corresponds to the advance trigger. Use this input when supplying more than one sample per FPGA clock cycle. Triggers.reference trigger index—Specifies the index of the sample that corresponds to the reference trigger. Use this input when supplying more than one sample per FPGA clock cycle. Triggers.reference trigger correction cycle count—Specifies the number of FPGA clock cycles in the past where the reference trigger actually occurred. You can retrieve this value on the host. Use this input with synchronization. Sample format—Specifies additional information about data.Use this optional input to specify that data contains more than one channel. Typically this input is either unwired or provided by the Channel Library. Data valid—Specifies whether the data input contains valid data. Timestamp—Specifies the timestamp associated with a particular record. The number of timestamp values per record written to the Write VI must match the timestamps per record input on the Configure Acquisition VI in the Multirecord Acquisition host library.Although stored timestamp values are guaranteed to be correlated with records, they are not correlated with individual samples in those records. The application that uses the Multirecord Acquisition FPGA library must provide sample-level timestamp correlation, if required.If you do not write the required number of timestamps for each record, the record acquisition process stalls, which may eventually cause a write overflow condition. Timestamp.timestamp—Specifies the timestamp value to associated with a particular record. Timestamp.timestamp valid—Specifies whether the timestamp input contains a valid timestamp value. |

| Output parameters |
| --- |
| Status—Indicates the current status of the acquisition state machine. Status idle—Indicates whether the acquisition state machine is currently idle. If you do not initiate an acquisition, the acquisition is idle. Status.number of record acquired—Returns the number of records acquired in the current acquisition. Status.write overflow—Indicates whether a write overflow occurred. All acquired samples are written into the Write FIFO before they are stored in memory. A write overflow is treated as a non-recoverable acquisition error because the acquired data is lost.The following factors affect the likelihood of a write overflow: Memory grant time: The memory write/read grant time affects the way the FPGA arbitrates between write and read access to DRAM. Ensure that memory writes have sufficient bandwidth relative to the front-end input sample rate. Status FIFO depth: The Status FIFO reports information about acquired records to the host. If the Status FIFO is full, the acquisition FPGA logic prevents writes to memory. Eventually, this can cause the Write FIFO to fill up and overflow. Ensure that the Status FIFO is deep enough for the rate at which the host consumes this FIFO. The host consumes the entire Status FIFO each time you fetch a record or query the acquisition status. Write FIFO depth: The Write FIFO on the FPGA must be deep enough to absorb DRAM latencies. DRAM write latencies vary based on memory grant time and the inherent DRAM physical access overhead. Insufficient number of timestamps: The number of timestamps per record that are provided to the Write VI of the Multirecord Acquisition FPGA library must match the value of the timestamps per record input of the Configure Acquisition VI. If the FPGA code does not capture the correct number of timestamps per record, the record acquisition stalls. Eventually, this can cause the Write FIFO to fill up and overflow. Events—Reports various events that occur during the acquisition. Use these events to synchronize external logic with the state of the acquisition. Events.ready for start—Indicates whether the Write VI is ready to receive and react to the assertion of triggers.start trigger. Events.ready for advance—Indicates whether the Write VI is ready to receive and react to the assertion of triggers.advance trigger. Events.ready for reference—Indicates whether the Write VI is ready to receive and react to the assertion of triggers.reference trigger. Events.end of record—Indicates whether the Write VI acquired the last data sample for a record. Events.done—Indicates whether the acquisition is complete. The acquisition is complete after the last record of the acquisition is acquired to memory. Events.start trigger—Indicates whether a trigger is detected on triggers.start trigger. Events.advance trigger—Indicates whether a trigger is detected on triggers.advance trigger. Events.reference trigger—Indicates whether a trigger is detected on triggers.reference trigger. Record acquisition in progress—Indicates whether a record is currently being acquired. Acquisition of a record begins after the start trigger or advance trigger asserts. Ready for input—Indicates whether this VI is ready to accept a new data value on the next clock cycle. When set to TRUE, this VI is ready to accept a new data value on the next clock cycle. When set to FALSE, this VI is not ready to accept a new data value on the next clock cycle. |

Parent topic:

Multirecord Acquisition Overview

<!--NI_TOPIC bundle=ni-reconfigurable-oscilloscopes path=multirecord-acquisition-host-vis.html language=enus -->
## TOPIC 00046: Multirecord Acquisition Host VIs

- bundle_id: `ni-reconfigurable-oscilloscopes`
- source_path: `multirecord-acquisition-host-vis.html`
- source_url: https://docs-be.ni.com/bundle/ni-reconfigurable-oscilloscopes/raw/resource/enus/multirecord-acquisition-host-vis.html
- document_id: `ni-reconfigurable-oscilloscopes`
- page_type: `leaf`
- content_type: `concept`
- source_description: Abort.viStops the signal or record acquisition on the FPGA. The acquisition stops immediately. Therefore, after you call the Abort VI, the most recently acquired record may be incomplete. After stopping the acquisition, the Abort VI retains the acquisition state to enable you to fetch previously acq

### Multirecord Acquisition Host VIs

#### Abort.vi

Stops the signal or record acquisition on the FPGA. The
 acquisition stops immediately. Therefore, after you call the
 Abort VI, the most recently acquired record may be
 incomplete. After stopping the acquisition, the Abort VI retains
 the acquisition state to enable you to fetch previously acquired records even after
 you abort the acquisition. You cannot use this VI to abort a pending fetch.

[IMAGE alt='image' src='GUID-E9B582FD-8357-4CE5-83D1-504C86ABAE5C-a5.gif']

| Input parameters |
| --- |
| Session in—Specifies your session. Session in is obtained from the Open Session VI of the Multirecord Acquisition host library. Error in—Describes error conditions that occur before this node runs. This input provides standard error in functionality. |

| Output parameters |
| --- |
| Session out—Passes a reference to your session to the next VI. Error out—Contains error information. This output provides standard error out functionality. |

#### Check Write Overflow.vi

Checks for a Write FIFO overflow error on the
 FPGA. All acquired samples are written into the Write FIFO before they are
 eventually stored in memory. A Write FIFO overflow is treated as a non-recoverable
 acquisition error, because the acquired data is lost.

The following factors
 affect the likelihood of a write overflow:

Memory grant times

Status FIFO depth

Write FIFO depth

Insufficient number of timestamps

Configure Acquisition

[IMAGE alt='image' src='GUID-A1A824C1-57DE-467D-B1D9-36E0C4800276-a5.gif']

| Input parameters |
| --- |
| Session in—Specifies your session. Session in is obtained from the Open Session VI of the Multirecord Acquisition host library. Error in—Describes error conditions that occur before this node runs. This input provides standard error in functionality. |

| Output parameters |
| --- |
| Session out—Passes a reference to your session to the next VI. Overflow occured—Indicates whether a write overflow occurred. Error out—Contains error information. This output provides standard error out functionality. |

#### Close Session.vi

Destroys the session to the Multirecord Acquisition
 library.

Calling the Close Session VI does not abort an
 acquisition that is in progress. You cannot use this VI to abort a pending
 fetch.

[IMAGE alt='image' src='GUID-73266B35-0A49-4B4D-88CE-77812F4A92AD-a5.gif']

| Input parameters |
| --- |
| Session in—Specifies your session. Session in is obtained from the Open Session VI of the Multirecord Acquisition host library. Error in—Describes error conditions that occur before this node runs. With the following exception, this input provides standard error in functionality. This node runs normally even if an error occurred before this node runs. |

| Output parameters |
| --- |
| Error out—Contains error information. This output provides standard error out functionality. |

#### Configure Acquisition.vi

Configures the parameters for multiple records
 in an acquisition. You must run this VI before initiating an acquisition.

[IMAGE alt='image' src='GUID-A829C466-F50F-4DD1-9853-2AA4C8CEEF57-a5.gif']

| Input parameters |
| --- |
| Session in—Specifies your session. Session in is obtained from the Open Session VI of the Multirecord Acquisition host library. Number of records is finite—Specifies whether to acquire a finite number of records, or to acquire records continuously. The default value is TRUE. Number of samples is finite—Specifies whether to acquire a finite number of samples, or to acquire samples continuously. The default value is TRUE. Number of records—Specifies the number of records to acquire if number of records is finite is set to TRUE. The default value is 1. Number of samples—Specifies the number of samples per record if number of samples is finite is set to TRUE. The default value is 1,000. Pretrigger samples—Specifies the number of samples to store for each record that was acquired in the time period immediately before the reference trigger occurred. The default value is 0. Error in—Describes error conditions that occur before this node runs. With the following exception, this input provides standard error in functionality. This node runs normally even if an error occurred before this node runs. Additional acquisition configuration—Specifies additional advanced configurations. Additional acquisition configuration.record padding (samples)—Specifies additional padding to allocate for a record. This parameter can be useful in combination with adjusting the reference trigger position. The default value is 0. Additional acquisition configuration.require finite records to fit in memory—Specifies that the requested number of records and samples must fit into memory for finite acquisitions. This parameter ensures that requested data cannot be overwritten for finite acquisitions. The default is TRUE. Additional acquisition configuration.timestamps per record—Specifies the number of timestamp values the FPGA captures for each record. This value must match the number of timestamps per record provided to the Write VI of the Multirecord Acquisition FPGA library. The default value is 0. Additional acquisition configuration.status FIFO depth (records)—Sets the depth of the record status DMA FIFO. The Status FIFO reports information about the current state of the acquisition to the host. Ensure that the Status FIFO is deep enough for the rate at which the host consumes this FIFO. If the Status FIFO is full, memory writes are delayed. Eventually, this can cause the Write FIFO to fill up and overflow. The host consumes the entire Status FIFO each time you fetch a record or query acquisition status. The value is specified in units of records. The default value is 10,000 records. |

| Output parameters |
| --- |
| Session out—Passes a reference to your session to the next VI. Record allocation info—Returns information about the allocation of records in onboard memory. This information can be useful in determining maximum number of records or samples that can fit in memory. Error out—Contains error information. This output provides standard error out functionality. |

#### Fetch Multiple Records.vi

Fetches data from multiple records in an
 acquisition. The fetch operation transfers acquired waveform data from the
 DRAM/Block RAM on the device to computer memory. The data was acquired to the
 DRAM/Block RAM by the hardware after the acquisition was initiated.

If the
 number of samples specified in number of samples is not available after the time
 duration specified by timeout, the Fetch Multiple Records VI
 returns a timeout error with no data.

[IMAGE alt='image' src='GUID-5223998E-7E47-48FF-A087-EA367301E616-a5.gif']

| Input parameters |
| --- |
| Session in—Specifies your session. Session in is obtained from the Open Session VI of the Multirecord Acquisition host library. Strating record—Specifies the first record to retrieve. Record numbers are zero-based. The default value is 0. Number of records—Specifies the number of records to fetch. The default value is 1. Fetch relative to—Specifies the reference location within the acquired record from which the Fetch Multiple Records VI begins fetching data. First sample—The fetch starts at the first sample acquired by the device. If the device wraps data in its memory buffer, the first sample is no longer available. In this case, the VI returns an error if fetch offset specifies a location that is within the overwritten portion of the memory buffer. Reference trigger sample—The fetch starts relative to the reference trigger. First pretrigger sample—The fetch starts relative to the first pretrigger sample acquired. If you do not configure a reference trigger, first pretrigger sample behaves the same as first sample because there are no pretrigger samples. Most recent sample—The fetch starts relative to the most recently acquired sample. The value of fetch offset must be negative. This VI doesn't support this option. Consider using the Fetch Single Record VI instead. Current read position—The fetch starts after the last fetched sample. This VI doesn't support this option. Consider using the Fetch Single Record VI instead. Number of samples—Specifies the number of samples to fetch. The default value is 0. Timeout (ms)—Specifies the time, in milliseconds, allotted for the Fetch Multiple Records VI to complete execution of each record before returning a timeout error. A value of -1 specifies that the VI waits until all data is available. A value of 0 is not supported. The default value is 10,000. You cannot abort a pending fetch using the Abort VI or Close VI. Error in—Describes error conditions that occur before this node runs. With the following exception, this input provides standard error in functionality. This node runs normally even if an error occurred before this node runs. Fetch offset—Specifies the offset relative to the position specified by fetch relative to, from which to start fetching data. fetch offset can be a positive or negative value. The default value is 0. Token—Specifies a value that is passed with the record request. The value is returned by the Retrieve Record VI in the FPGA. You can use this information to configure FPGA processing in the retrieve loop. Scaling coefficients—Specifies scaling coefficients for instances of this VI that return double data. The VI uses the coefficients to scale the requested data. Each index of the array corresponds to a channel. The data is multiplied by the gain factor prior to adding the specified offset, using the following equation: Data— Binary hardware data * gain / maximum binary value) + offset. A gain value of 1 and an offset value of 0 has no effect on the binary data. The default behavior does not change the binary data. |

| Output parameters |
| --- |
| Session out—Passes a reference to your session to the next VI. Data—Returns the acquired records. Each waveform corresponds to a record. If the fetch contains multiple channels, all waveforms for a record are returned before proceeding to the next record. For example a two channel, two record acquisition returns four waveforms: array index 0 = Channel0 Record0 array index 1 = Channel1 Record0 array index 2 = Channel0 Record1 array index 3 = Channel1 Record1 Requested records info—Returns additional information about each record returned by data. There is one element in the requested records info array for each record. Requested records info.number of samples—Returns the number of samples in the record. Requested records info.starting sample number—Returns the sample number of the first sample in the returned record data. Sample numbers are zero-based. Sample numbers start at zero for each record and increment by one for each acquired sample. Requested records info.number of channels—Returns the number of channels in the record data. Requested records info.timestamps—Returns the timestamp values that were captured for the record. Error out—Contains error information. This output provides standard error out functionality. |

#### Fetch Single Record.vi

Fetches data from a single record in an
 acquisition. The fetch operation transfers waveform data, which is acquired by the
 hardware, from the memory on the device to the computer memory.

If the number
 of samples specified in number of samples is not available after the time duration
 specified by timeout, the Fetch Single Record VI returns a
 timeout error with no data.

[IMAGE alt='image' src='GUID-600D2CE5-6FE8-4B41-BF59-0201DAB25EDA-a5.gif']

| Input parameters |
| --- |
| Session in—Specifies your session. Session in is obtained from the Open Session VI of the Multirecord Acquisition host library. Record number—Specifies the record to retrieve. Record numbers are zero-based. The default value is 0. Fetch relative to—Specifies the reference location within the acquired record from which the Fetch Single Records VI begins fetching data. First sample—The fetch starts at the first sample acquired by the device. If the device wraps data in its memory buffer, the first sample is no longer available. In this case, the VI returns an error if fetch offset specifies a location that is within the overwritten portion of the memory buffer. Reference trigger sample—The fetch starts relative to the reference trigger. First pretrigger sample—The fetch starts relative to the first pretrigger sample acquired. If you do not configure a reference trigger, first pretrigger sample behaves the same as first sample because there are no pretrigger samples. Most recent sample—The fetch starts relative to the most recently acquired sample. The value of fetch offset must be negative. Current read position—The fetch starts after the last fetched sample. Number of samples—Specifies the number of samples to fetch. The default value is 1,000. Timeout (ms)—Specifies the time, in milliseconds, allotted for the Fetch Single Record VI to complete before returning a timeout error. A value of -1 specifies that the VI waits until all data is available. A value of 0 specifies that the VI immediately returns available data. The default value is 10,000. You cannot abort a pending fetch using the Abort VI or Close VI. Error in—Describes error conditions that occur before this node runs. This input provides standard error in functionality. Fetch offset—Specifies the offset relative to the position specified by fetch relative to, from which to start fetching data. fetch offset can be a positive or negative value. The default value is 0. Token—Specifies a value that is passed with the record request. The value is returned by the Retrieve Record VI in the FPGA. You can use this information to configure FPGA processing in the retrieve loop. Scaling coefficients—Specifies scaling coefficients for instances of this VI that return double data. The VI uses the coefficients to scale the requested data. Each index of the array corresponds to a channel. The data is multiplied by the gain factor prior to adding the specified offset, using the following equation: Data— Binary hardware data * gain / maximum binary value) + offset. A gain value of 1 and an offset value of 0 has no effect on the binary data. The default behavior does not change the binary data. |

| Output parameters |
| --- |
| Session out—Passes a reference to your session to the next VI. Data—Returns the acquired record. If more than one channel is returned, each waveform corresponds to a channel. Requested records info—Returns additional information about each record returned by data. Requested records info.number of samples—Returns the number of samples in the record. Requested records info.starting sample number—Returns the sample number of the first sample in the returned record data. Sample numbers are zero-based. Sample numbers start at zero for each record and increment by one for each acquired sample. Requested records info.number of channels—Returns the number of channels in the record data. Requested records info.timestamps—Returns the timestamp values that were captured for the record. Error out—Contains error information. This output provides standard error out functionality. |

#### Get
 Acquisition Status.vi

Checks the status of the acquisition. This VI
 determines the number of acquired records and checks the state of the record for
 which acquisition is happening. This VI also reports write overflow
 conditions.

[IMAGE alt='image' src='GUID-3AEFB501-3DBA-4B59-B7C8-EE7C9722C335-a5.gif']

| Input parameters |
| --- |
| Session in—Specifies your session. Session in is obtained from the Open Session VI of the Multirecord Acquisition host library. Error in—Describes error conditions that occur before this node runs. This input provides standard error in functionality. |

| Output parameters |
| --- |
| Overflow occured—Indicates whether a write overflow occurred. Refer to the Check Write Overflow VI for more information about write overflows. Session out—Passes a reference to your session to the next VI. Done—Indicates whether all records have been acquired. Records done—Returns the number of records that have been completely acquired. Current record status—Returns information about the record that is currently being acquired. Current record status.started—Indicates whether a record is currently being acquired. Current record status.reference trigger detected—Indicates whether the Reference Trigger has been detected for the currently acquiring record. Current record status.reference trigger sample number—Returns the sample number that corresponds to the reference trigger sample for the currently acquiring record. Sample numbers are zero-based. Sample numbers start at zero for each record and increment by one for each acquired sample. Current record status.samples written—Returns the total number of samples acquired for the currently acquiring record. This parameter returns 0 if you set query hw for number of samples written for current record to FALSE. Error out—Contains error information. This output provides standard error out functionality. |

#### Get
 Fetch Backlog.vi

Returns the number of samples that are available to be
 fetched from the specified fetch position.

The combination of fetch relative
 to and fetch offset identify a specific sample within the acquired record. This VI
 reports the number of samples that are available to fetch starting at the specified
 sample.

[IMAGE alt='image' src='GUID-A7296D03-FB1E-4532-968C-2702072C3F1C-a5.gif']

| Input parameters |
| --- |
| Session in—Specifies your session. Session in is obtained from the Open Session VI of the Multirecord Acquisition host library. Record number—Specifies the record from which to read the backlog. Record numbers are zero-based. The default value is 0. Fetch relative to—Specifies the reference location within the acquired record from which to read the backlog. First sample—The backlog calculation starts relative to the first sample acquired by the device. If the device wraps data in its memory buffer, the first sample is no longer available. In this case, the VI returns an error if fetch offset specifies a location that is within the overwritten portion of the memory buffer. Reference trigger sample—The backlog calculation starts relative to the sample that was acquired with the reference trigger. First pretrigger sample—The backlog calculation starts relative to the first pretrigger sample acquired. If you do not configure a reference trigger, first pretrigger sample behaves the same as first sample because there are no pretrigger samples. Most recent sample—The backlog calculation starts relative to the most recently acquired sample. The value of fetch offset must be negative. Current read position—The backlog calculation starts after the last fetched sample. Fetch offset—Specifies the offset relative to the position, which is specified by fetch relative to, from which to calculate the backlog. fetch offset can be a positive or negative value. The default value is 0. Error in—Describes error conditions that occur before this node runs. This input provides standard error in functionality. |

| Output parameters |
| --- |
| Session out—Passes a reference to your session to the next VI. Fetch backlog—Returns the number of samples available to be fetched. Error out—Contains error information. This output provides standard error out functionality. |

#### Get
 Number of Outstanding Record Requests.vi

Returns the number of record read
 requests that were submitted to the device but are not yet complete. A record read
 request is complete after the host retrieves the associated record data from the
 device.

Use this low-level VI primarily with the Request
 Record and Retrieve Record VIs. This VI effectively
 reports the number of times your application must call the Retrieve
 Record VI to retrieve all record data that was previously
 requested.

You do not need to use this VI when using the Fetch Single
 Record VI or Fetch Multiple Records VI. Use this VI
 with the Request Record VI and Retrieve Record
 VI to pipeline the process on the host that manages requesting and retrieving data
 from the device. The Fetch Single Record VI or Fetch
 Multiple Records VI performs these lower level record request and
 retrieval mechanisms for you.

[IMAGE alt='image' src='GUID-17EBCF48-999B-499F-8354-89576BB03192-a5.gif']

| Input parameters |
| --- |
| Session in—Specifies your session. Session in is obtained from the Open Session VI of the Multirecord Acquisition host library. Error in—Describes error conditions that occur before this node runs. This input provides standard error in functionality. |

| Output parameters |
| --- |
| Session out—Passes a reference to your session to the next VI. Number of outstanding record requests—Returns the total number of record read requests that were submitted to the device but are not yet complete. Error out—Contains error information. This output provides standard error out functionality. |

#### Get Record Status.vi

Returns detailed
 acquisition state information about a specified record.

[IMAGE alt='image' src='GUID-A90C96E2-D0D6-4B75-B8F9-27D322C55AC6-a5.gif']

| Input parameters |
| --- |
| Session in—Specifies your session. Session in is obtained from the Open Session VI of the Multirecord Acquisition host library. Record number—Specifies the record number for which to obtain status information. Record numbers are zero-based. The default value is 0. Error in—Describes error conditions that occur before this node runs. This input provides standard error in functionality. |

| Output parameters |
| --- |
| Session out—Passes a reference to your session to the next VI. Record status—Returns status information about the specified record. Record status.state—Returns the acquisition state of the record. Not started—The first sample has not yet been acquired for this record. Being acquired—The record is currently being acquired into device memory. Completed—The last sample for the record has been acquired into the memory. The record is available to fetch from the device. Overwritten—The record was previously acquired, but it was overwritten in memory. The record is not available to fetch. Record status.reference trigger detected—Indicates whether the Write VI of the Multirecord Acquisition FPGA library detected the reference trigger for the specified record. Record status.reference trigger sample number—Returns the sample number that corresponds to the reference trigger sample for the specified record. Sample numbers are zero-based. Sample numbers always start at zero for each record and increment by one for each acquired sample. Record status.first pretrigger sample number—Returns the sample number that corresponds to the first pretrigger sample for the specified record. Sample numbers are zero-based. Sample numbers start at zero for each record and increment by one for each acquired sample. Record status.samples written—Returns the total number of samples acquired for the specified record. Record status.current read position—Returns the sample number of the current read position within the record. This parameter denotes the current position of the record read pointer when fetching records relative to current read position. Sample numbers are zero-based. Sample numbers start at zero for each record and increment by one for each acquired sample. Record status.first valid sample—Returns the sample number of the oldest sample that is available to be fetched from the device. Sample numbers are zero-based. Sample numbers always start at zero for each record and increment by one for each acquired sample. Record status.last valid sample to request—Returns the sample number of the newest sample that can be fetched. Sample numbers are zero-based. Sample numbers always start at zero for each record and increment by one for each acquired sample. Record status.timestamps—Returns the timestamp values that were captured for the record. Error out—Contains error information. This output provides standard error out functionality. |

#### Initiate.vi

Starts a new acquisition on the FPGA. You must configure the
 acquisition using the Configure Acquisition VI prior to calling
 the Initiate VI. Only call the Initiate VI
 when there is no acquisition in progress, otherwise subsequent fetches will not
 return samples.

After calling this VI, the FPGA is sensitive to the various
 acquisition triggers such as start, reference, and advance triggers. After
 triggering conditions are satisfied, the FPGA immediately begins acquiring data into
 record memory in the DRAM or Block RAM.

[IMAGE alt='image' src='GUID-A7AB6857-7133-42DA-9931-0872DB81CE0D-a5.gif']

| Input parameters |
| --- |
| Session in—Specifies your session. Session in is obtained from the Open Session VI of the Multirecord Acquisition host library. Error in—Describes error conditions that occur before this node runs. This input provides standard error in functionality. |

| Output parameters |
| --- |
| Session out—Passes a reference to your session to the next VI. Error out—Contains error information. This output provides standard error out functionality. |

#### Open
 Session.vi

Opens a session to the instance of the Multirecord Acquisition
 library on the device that is connected to the instance of register bus session in.
 Use session out to identify the Multirecord Acquisition library in all subsequent
 Multirecord Acquisition VIs.

[IMAGE alt='image' src='GUID-FFA690CC-9FDD-48B6-AF56-CB350FE31725-a5.gif']

| Input parameters |
| --- |
| Register bus—Specifies a reference to the Register Bus session, which identifies the instance of the Register Bus library to which this instance of the Multirecord Acquisition library is connected in the FPGA. FGPA interface—Specifies the reference to the FPGA interface. Subsystem map—Specifies the reference to the subsystem map. This reference is provided by calling the Read Subsystem Map VI from the Instruction Framework host library. Instance—Specifies the instance number of the Multirecord Acquisition FPGA library for which to open a session. This value must match the value of instance of the Create Resources VI in the Multirecord Acquisition FPGA library. Error in—Describes error conditions that occur before this node runs. This input provides standard error in functionality. |

| Output parameters |
| --- |
| Session out—Passes a reference to your session to the next VI. Error out—Contains error information. This output provides standard error out functionality. |

#### Request Record.vi

Submits a request to read a particular record from the
 device. This VI does not wait for the record data to be retrieved from the device.
 This VI completes execution immediately after submitting the record read
 request.

Use this low-level VI primarily with the Retrieve
 Record VI. You do not need to use the Request
 Record VI when using the Fetch Single Record VI or
 Fetch Multiple Records VI. Use the Request
 Record VI along with the Retrieve Record VI to
 pipeline the process on the host that manages requesting and retrieving data from
 the device. The Fetch Single Record VI or Fetch Multiple
 Records VI performs these lower level record request and retrieval
 mechanisms for you.

[IMAGE alt='image' src='GUID-4D320EE9-0DD8-4653-80A3-54DDB4F1BBB5-a5.gif']

| Input parameters |
| --- |
| Session in—specifies your session. Session in is obtained from the Open Session VI of the Multirecord Acquisition host library. Record number—Specifies the record number to request. Record numbers are zero-based. The default value is 0. Starting sample number—Specifies the first sample number of the block of record samples to request. Sample numbers are zero-based. Sample numbers start at zero for each record and increment by one for each acquired sample. Number of samples—Specifies the number of samples to request. The default value is 1,000. Token—Specifies a value that is passed with the record request. The value is returned by the Retrieve Record VI in the FPGA. You can use this information to configure FPGA processing in the retrieve loop. Error in—Describes error conditions that occur before this node runs. This input provides standard error in functionality. |

| Output parameters |
| --- |
| Session out—Passes a reference to your session to the next VI. Error out—Contains error information. This output provides standard error out functionality. |

#### Reset.vi

Resets the host session and the instance of the Multirecord
 Acquisition FPGA library to which this session is connected.

This VI aborts
 any active acquisition on the device. This VI does not change the current settings
 for Read Memory Grant Time, Write Memory Grant
 Time, Fetch FIFO Depth, or Status FIFO
 Depth.

[IMAGE alt='image' src='GUID-EEE7A9F4-5D1E-4C42-A10C-517D0BFF52AE-a5.gif']

| Input parameters |
| --- |
| Session in—Specifies your session. Session in is obtained from the Open Session VI of the Multirecord Acquisition host library. Error in—Describes error conditions that occur before this node runs. This input provides standard error in functionality. |

| Output parameters |
| --- |
| Session out—Passes a reference to your session to the next VI. Error out—Contains error information. This output provides standard error out functionality. |

#### Retrieve Record.vi

Retrieves record data that you requested using the
 Request Record VI. The Retrieve Record VI
 retrieves samples in the same order in which they were originally requested. When
 returning multiple channels, this VI returns the data interleaved with channel 0
 starting at array index 0. Use the Get Number of
 Outstanding Record Requests VI to determine the number of pending
 record requests.

This is a low-level VI that is used primarily with the
 Request Record VI. You do not need to use this VI when using
 the Fetch Single Record VI or Fetch Multiple
 Records VI. The Retrieve Record VI, along with the
 Request Record VI, is useful if you want to pipeline the
 process on the host that manages requesting and retrieving data from the device. The
 Fetch Single Record VI or Fetch Multiple
 Records VI effectively wraps these lower level record request and
 retrieval mechanisms.

[IMAGE alt='image' src='GUID-CD2FEAB9-A51D-41EB-89A4-9700F95154B3-a5.gif']

| Input parameters |
| --- |
| Session in—Specifies your session. Session in is obtained from the Open Session VI of the Multirecord Acquisition host library. Samples to retrieve (-1)—Specifies the number of samples that the VI must retrieve. A value of -1 specifies that this VI must retrieve all samples that were specified in the original Request Record VI call. National Instruments recommends that you set samples to retrieve to -1. However, you can adjust samples to retrieve to retrieve partial samples of a record request. The default value is -1. Timeout (ms)—Specifies the time, in milliseconds, allotted for the Retrieve Record VI to complete before returning a timeout error. A value of -1 specifies that the VI waits until all data is available. The default value is 10,000. You cannot abort a pending fetch using the Abort VI or Close VI. Error in—Describes error conditions that occur before this node runs. This input provides standard error in functionality. |

| Output parameters |
| --- |
| Session out—Passes a reference to your session to the next VI. Data—Returns the record data that was retrieved from the device. When returning multiple channels, the data is returned interleaved with channel 0 starting at array index 0. Requested record info—Returns information about the original record request. Requested record info.number of samples—Returns the number of samples that were retrieved. Requested record info.starting sample number—Returns the sample number of the first sample in the retrieved data. Sample numbers are zero-based. Sample numbers start at zero for each record and increment by one for each sample that is acquired. Requested record info.number of channels—Returns the number of channels in the record data. Requested record info.timestamps—Returns the timestamp values that were captured for this record. Done with retrieve—Indicates when all requested samples have been retrieved. EDVR instances of this VI must be called in a loop until this parameter returns TRUE. You can use EDVR instances of this VI to optimize performance by allowing access to the low-level data buffer. Error out—Contains error information. This output provides standard error out functionality. |

#### Set Fetch FIFO Depth.vi

Sets the depth of
 the DMA FIFO that fetches record data from the device. When deciding the depth of
 the DMA FIFO, you must consider the size of the fetched records and the number of
 record requests to queue up simultaneously. For optimal performance, the DMA FIFO
 must be large enough to satisfy each of these constraints.

[IMAGE alt='image' src='GUID-EF87931D-A4CD-44E0-894E-128B5D70AE59-a5.gif']

| Input parameters |
| --- |
| Session in—Specifies your session. Session in is obtained from the Open Session VI of the Multirecord Acquisition host library. FIFO depth (bytes)—Specifies the depth, in bytes, of the DMA FIFO. Error in—Describes error conditions that occur before this node runs. This input provides standard error in functionality. |

| Output parameters |
| --- |
| Session out—Passes a reference to your session to the next VI. Error out—Contains error information. This output provides standard error out functionality. |

#### Set Memory Read Grant Time.vi

Configures
 the read grant time setting of the time-slot arbiter that controls DRAM access on
 the device.

[IMAGE alt='image' src='GUID-0DDE019F-2DDE-4D4C-963D-EE9B81AB38CD-a5.gif']

| Input parameters |
| --- |
| Session in—Specifies your session. Session in is obtained from the Open Session VI of the Multirecord Acquisition host library. Grant time (clocks)—Specifies the number of back-to-back clock cycles to allocate for memory read operations. These are clock cycles of the process clock that is wired to the Create Resources VI of the Multirecord Acquisition FPGA instance of the Multirecord Acquisition library. The default value is 0. Error in—Describes error conditions that occur before this node runs. This input provides standard error in functionality. |

| Output parameters |
| --- |
| Session out—Passes a reference to your session to the next VI. Error out—Contains error information. This output provides standard error out functionality. |

#### Set Memory Write Grant Time.vi

Configures
 the write grant time setting of the time-slot arbiter that controls DRAM access on
 the device.

[IMAGE alt='image' src='GUID-8CEFF799-2587-41D7-BA0D-F16F9B993FAB-a5.gif']

| Input parameters |
| --- |
| Session in—Specifies your session. Session in is obtained from the Open Session VI of the Multirecord Acquisition host library. Grant time (clocks)—Specifies the number of back-to-back clock cycles to allocate for memory write operations. These are clock cycles of the process clock that is wired to the Create Resources VI of the Multirecord Acquisition FPGA instance of the Multirecord Acquisition library. The default value is 0. Error in—Describes error conditions that occur before this node runs. This input provides standard error in functionality. |

| Output parameters |
| --- |
| Session out—Passes a reference to your session to the next VI. Error out—Contains error information. This output provides standard error out functionality. |

#### Wait
 for Samples.vi

Waits for the requested number of samples to be available.
 The VI returns the starting sample number of the request. You can use starting
 sample number with the Request Record VI. You must run this VI
 after initiating an acquisition.

[IMAGE alt='image' src='GUID-EDCA2662-E886-4E80-922D-287B3DFABEAE-a5.gif']

| Input parameters |
| --- |
| Session in—specifies your session. Session in is obtained from the Open Session VI of the Multirecord Acquisition host library. Record number—Specifies the record number to request. Record numbers are zero-based. Fetch relative to—Specifies the reference location within the acquired record for this VI to wait for before returning. Number of samples—Specifies the number of samples to request. Timeout (ms)—Specifies the time, in milliseconds, allotted for the Fetch Multiple Records VI to complete execution before returning a timeout error. A value of -1 specifies that the VI waits until all data is available. A value of 0 specifies that the VI immediately returns available data. The default value is 10,000. A pending wait can not be aborted using the Abort VI or Close VI. Fetch offset—Specifies the offset relative to the position specified by the fetch relative to input, from which to start fetching data. Offset can be a positive or negative value. The default value is 0. Error in—Describes error conditions that occur before this node runs. This input provides standard error in functionality. |

| Output parameters |
| --- |
| Session out—Passes a reference to your session to the next VI. Starting sample number—Indicates the first sample number of the block of record samples. Sample numbers are zero based. Sample numbers start at zero for each record and increment by one for each sample that is acquired. Number of samples (coerced)—Indicates the actual number of samples the function waited for. This value may be coerced depending on the configured acquisition settings. Error out—Contains error information. This output provides standard error out functionality. |

Parent topic:

Multirecord Acquisition Overview

<!--NI_TOPIC bundle=ni-reconfigurable-oscilloscopes path=multirecord-acquisition-overview.html language=enus -->
## TOPIC 00047: Multirecord Acquisition Overview

- bundle_id: `ni-reconfigurable-oscilloscopes`
- source_path: `multirecord-acquisition-overview.html`
- source_url: https://docs-be.ni.com/bundle/ni-reconfigurable-oscilloscopes/raw/resource/enus/multirecord-acquisition-overview.html
- document_id: `ni-reconfigurable-oscilloscopes`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the Multirecord Acquisition instrument design library to acquire a series of waveforms that are aligned with various triggering conditions. The FPGA uses triggering conditions to determine when to start and stop acquiring each waveform. Each acquired waveform is stored in DRAM on the device in a

### Multirecord Acquisition Overview

Use the Multirecord Acquisition instrument design library to acquire a series of waveforms that are aligned with various triggering conditions. The FPGA uses triggering conditions to determine when to start and stop acquiring each waveform. Each acquired waveform is stored in DRAM on the device in a region of memory called a record. Your application can retrieve those records from DRAM for further processing and analysis. You can perform this custom processing on the FPGA or host. Each data sample of a record is 32 bits wide. For devices that receive two samples per cycle, you can configure this instrument design library to acquire two samples per cycle.

This instrument design library is particularly useful when you need to capture a finite amount of data that is correlated with external events. For example, you can use this instrument design library in RF applications to capture multiple bursts of RF data and align those acquisitions to the start of each burst signal. Each RF burst might be stored in a single record. However, this is one specific example, and there are many other kinds of applications in which you can use this library.

In general, records are denoted by the assertion of a reference trigger.
 After the FPGA starts acquiring a record, the FPGA continues acquiring data into that
 record until the reference trigger asserts. After the
 reference trigger asserts, the FPGA acquires the specified
 number of post-trigger samples into that record before marking the record as complete
 and advancing to the next record. This behavior allows you to capture a specified number
 of samples both before and after the assertion of the reference
 trigger.

This library supports the following types of triggers:

Start trigger

Reference trigger

Advance trigger

You can also use this instrument design library to store one or more 64-bit timestamps that are
 correlated with each record. For example, you could store the time when the
 reference trigger asserts for each record. This technique can
 be useful if your application needs to track when each record was acquired.

This instrument design library includes host VIs and FPGA VIs. The following figure is a
 high-level block diagram of the LabVIEW FPGA design of the Multirecord Acquisition
 library.

[IMAGE alt='image' src='GUID-D47E63A9-27E6-4418-8D6D-A993548A9A47-a5.gif']

The FPGA writes sample data into this instrument design library from the Sample Clock domain. You
 can retrieve the acquired records from memory and transfer them to the host through the
 Fetch DMA FIFO VI. You can insert custom FPGA processing code either before samples are
 written to memory or after you retrieve records from memory. Where you decide to perform
 the processing generally depends on the nature of the signal processing algorithm.

Refer to the LabVIEW context help for the Multirecord Acquisition LabVIEW VIs for more detailed
 information about the library interface.

Parent topic:

LabVIEW Instrument Design Libraries for Reconfigurable Oscilloscopes

<!--NI_TOPIC bundle=ni-reconfigurable-oscilloscopes path=multirecord-acquisition-sample-project.html language=enus -->
## TOPIC 00048: Multirecord Acquisition Sample Project

- bundle_id: `ni-reconfigurable-oscilloscopes`
- source_path: `multirecord-acquisition-sample-project.html`
- source_url: https://docs-be.ni.com/bundle/ni-reconfigurable-oscilloscopes/raw/resource/enus/multirecord-acquisition-sample-project.html
- document_id: `ni-reconfigurable-oscilloscopes`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Multirecord Acquisition sample project provides a host interface that is similar to other digitizer APIs. To get started with the Multirecord Acquisition sample project, complete the following steps: Launch LabVIEW. Select File»Create Project. On the left side of the Create Project window, selec

### Multirecord Acquisition Sample Project

The Multirecord Acquisition sample project provides a host interface that is similar to other digitizer APIs.

To get started with the Multirecord Acquisition sample project, complete the following steps:

1. Launch LabVIEW.
2. Select File » Create Project .
3. On the left side of the Create Project window, select Oscilloscopes .
4. On the right side of the Create Project window, select the
 Multirecord Acquisition sample project and click
 Next .
5. Specify a name, location, and device target for the project in the Create Project window and click Finish .
LabVIEW creates, configures, and opens a new Multirecord Acquisition project.
6. In the project tree, navigate to My Computer » Project Documentation , open Multirecord Acquisition Documentation.html , and navigate to the Running this Sample Project section of the documentation.
7. Follow the instructions in the project documentation and VI block diagram comments to use and customize the sample project.

Parent topic:

Creating an Application with Instrument Design Libraries

<!--NI_TOPIC bundle=ni-reconfigurable-oscilloscopes path=ni-labview-instrument-design-libraries-for-re.html language=enus -->
## TOPIC 00049: LabVIEW Instrument Design Libraries for Reconfigurable Oscilloscopes

- bundle_id: `ni-reconfigurable-oscilloscopes`
- source_path: `ni-labview-instrument-design-libraries-for-re.html`
- source_url: https://docs-be.ni.com/bundle/ni-reconfigurable-oscilloscopes/raw/resource/enus/ni-labview-instrument-design-libraries-for-re.html
- document_id: `ni-reconfigurable-oscilloscopes`
- page_type: `leaf`
- content_type: `concept`
- source_description: This section describes the instrument design libraries that you can use to create application-specific instrumentation.

### LabVIEW Instrument Design Libraries for
 Reconfigurable Oscilloscopes

This section describes the instrument design libraries that you can use to *create
 application-specific instrumentation*.

Parent topic:

Programming

Related concepts:

- Creating an Application with Instrument Design Libraries

<!--NI_TOPIC bundle=ni-reconfigurable-oscilloscopes path=ni-oscilloscopes-fundamentals-help.html language=enus -->
## TOPIC 00050: Oscilloscopes Fundamentals

- bundle_id: `ni-reconfigurable-oscilloscopes`
- source_path: `ni-oscilloscopes-fundamentals-help.html`
- source_url: https://docs-be.ni.com/bundle/ni-reconfigurable-oscilloscopes/raw/resource/enus/ni-oscilloscopes-fundamentals-help.html
- document_id: `ni-reconfigurable-oscilloscopes`
- page_type: `leaf`
- content_type: `concept`

### Oscilloscopes Fundamentals

- [Bandwidth](bandwidth.html)
- [Flatness](flatness.html)
- [Resolution](resolution.html)
- [Sample Rate](sample-rate.html)
- [Record Length](record-length.html)
- [Vertical Range and Offset](vertical-range-and-offset.html)
- [Input Coupling](input-coupling.html)
- [Impedance and Impedance Matching](impedance-and-impedance-matching.html)
- [Probes and Their Effects](probes-and-their-effects.html)
- [Accuracy](accuracy.html)
- [Noise](noise.html)
- [Triggering](triggering.html)
- [Sample Clock](sample-clock.html)
- [Reference Clock/Phase-Lock Loop](reference-clock-phase-lock-loop.html)
- [Time-to-Digital Converter (TDC)](tdc.html)
- [Sampling Methods](sampling-methods.html)
- [Frequency Domain Fundamentals](frequency-domain-fundamentals.html)
- [Video Fundamentals](video-fundamentals.html)

<!--NI_TOPIC bundle=ni-reconfigurable-oscilloscopes path=noise.html language=enus -->
## TOPIC 00051: Noise

- bundle_id: `ni-reconfigurable-oscilloscopes`
- source_path: `noise.html`
- source_url: https://docs-be.ni.com/bundle/ni-reconfigurable-oscilloscopes/raw/resource/enus/noise.html
- document_id: `ni-reconfigurable-oscilloscopes`
- page_type: `leaf`
- content_type: `concept`
- source_description: Noise is any unwanted signal that appears in your sampled data. Noise comes from both external and internal sources. The following external noise sources might appear: AC power line Motors Generators Transformers Fluorescent lights Soldering irons and welders CRT displays Computers Electrical storms

### Noise

Noise is any unwanted signal that appears in your sampled data. Noise comes from both external
 and internal sources.

The following external noise sources might appear:

- AC power line
- Motors
- Generators
- Transformers
- Fluorescent lights
- Soldering irons and welders
- CRT displays
- Computers
- Electrical storms
- Radio transmitters

The following internal noise sources might appear:

- Digital clocks
- Microprocessors
- Switched mode power supplies

Noise can be transient in nature, have fixed frequencies such as harmonic or mixer products, or
 be broadband random noise.

Parent topic:

Oscilloscopes Fundamentals

<!--NI_TOPIC bundle=ni-reconfigurable-oscilloscopes path=nyquist-theorem.html language=enus -->
## TOPIC 00052: Nyquist Theorem

- bundle_id: `ni-reconfigurable-oscilloscopes`
- source_path: `nyquist-theorem.html`
- source_url: https://docs-be.ni.com/bundle/ni-reconfigurable-oscilloscopes/raw/resource/enus/nyquist-theorem.html
- document_id: `ni-reconfigurable-oscilloscopes`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Nyquist theorem states that a signal must be sampled at least twice as fast as the highest frequency component of the signal to accurately reconstruct the waveform. Frequency components higher than half the sample rate are mistakenly interpreted as low-frequency components, a phenomenon known as

### Nyquist Theorem

The Nyquist theorem states that a signal must be sampled at least twice as fast as the highest
 frequency component of the signal to accurately reconstruct the waveform. Frequency
 components higher than half the sample rate are mistakenly interpreted as low-frequency
 components, a phenomenon known as *aliasing*.

The following figure shows a 5 MHz sine wave digitized by a 6 MS/s ADC. The dotted line
 indicates the aliased signal recorded by the ADC at that sample rate. The 5 MHz
 frequency aliases back into the passband, falsely appearing as a 1 MHz sine wave.
 Inserting a lowpass filter with a cutoff at the Nyquist rate prevents aliasing in the
 passband.

[IMAGE alt='image' src='GUID-05E2BC75-4E2D-42F6-89BC-600115FBB048-a5.gif']

The following figure shows the frequency view of the same example:

[IMAGE alt='image' src='GUID-AF3DF760-FC29-4B8A-B1D4-22C1B8C37511-a5.gif']

where

fs = 6 MS/s fN = 3 MHz (the Nyquist frequency) fa = 1 MHz (1fs - 5 MHz).

Parent topic:

Sample Rate

Related concepts:

- Aliasing
- Undersampling
- Oversampling

<!--NI_TOPIC bundle=ni-reconfigurable-oscilloscopes path=oversampling.html language=enus -->
## TOPIC 00053: Oversampling

- bundle_id: `ni-reconfigurable-oscilloscopes`
- source_path: `oversampling.html`
- source_url: https://docs-be.ni.com/bundle/ni-reconfigurable-oscilloscopes/raw/resource/enus/oversampling.html
- document_id: `ni-reconfigurable-oscilloscopes`
- page_type: `leaf`
- content_type: `concept`
- source_description: Oversampling is sampling at a rate beyond twice the highest frequency component of interest in the signal. Because real-world signals are not perfectly filtered and often contain frequency components greater than the Nyquist frequency, oversampling can be used to increase the foldover frequency so t

### Oversampling

Oversampling is sampling at a rate beyond twice the highest frequency component of interest in
 the signal. Because real-world signals are not perfectly filtered and often contain frequency
 components greater than the *Nyquist* frequency, oversampling can be used to increase
 the foldover frequency so that these unwanted components of the signal do not alias into the
 passband. Oversampling is also necessary when trying to capture fast edges, transients, and
 one-time events.

Parent topic:

Sample Rate

Related concepts:

- Nyquist Theorem

<!--NI_TOPIC bundle=ni-reconfigurable-oscilloscopes path=overview.html language=enus -->
## TOPIC 00054: Reconfigurable Oscilloscopes Overview

- bundle_id: `ni-reconfigurable-oscilloscopes`
- source_path: `overview.html`
- source_url: https://docs-be.ni.com/bundle/ni-reconfigurable-oscilloscopes/raw/resource/enus/overview.html
- document_id: `ni-reconfigurable-oscilloscopes`
- page_type: `leaf`
- content_type: `concept`
- source_description: This manual contains hardware and programming support for LabVIEW Instrument Design Libraries for Reconfigurable Oscilloscopes and the following reconfigurable oscilloscopes: PXIe-5164 PXIe-5170R PXIe-5171R This file assumes that you have already followed the software and hardware installation instr

### Reconfigurable Oscilloscopes
 Overview

This manual contains hardware and programming support for LabVIEW Instrument Design
 Libraries for Reconfigurable Oscilloscopes and the following reconfigurable
 oscilloscopes:

- PXIe-5164
- PXIe-5170R
- PXIe-5171R

This file assumes that you have already followed the software and hardware installation
 instructions in the *Calibration Procedure* for your device.

Note

<!--NI_TOPIC bundle=ni-reconfigurable-oscilloscopes path=pci-and-pxi-ground-loop-noise.html language=enus -->
## TOPIC 00055: PCI and PXI Ground Loop Noise

- bundle_id: `ni-reconfigurable-oscilloscopes`
- source_path: `pci-and-pxi-ground-loop-noise.html`
- source_url: https://docs-be.ni.com/bundle/ni-reconfigurable-oscilloscopes/raw/resource/enus/pci-and-pxi-ground-loop-noise.html
- document_id: `ni-reconfigurable-oscilloscopes`
- page_type: `leaf`
- content_type: `concept`
- source_description: Some computer chassis can induce ground loop noise in measurements taken with instruments having grounded input connectors. Spurious DC and low-frequency content can result. The cause is usually power supply return currents from the motherboard that partially flow through the computer chassis to the

### PCI and PXI Ground Loop Noise

Some computer chassis can induce ground loop noise in measurements taken with instruments having
 grounded input connectors. Spurious DC and low-frequency content can result. The cause is usually
 power supply return currents from the motherboard that partially flow through the computer
 chassis to the power supply housing rather than entirely through the power supply cabling.

The following guidelines help mitigate ground loop noise for PCI devices:

- Ensure that the motherboard is tightly screwed down to the chassis so that chassis return
 currents will flow though the chassis under the motherboard and not in the vicinity of the PCI
 boards.
- Ensure that the power supply cable is well seated on the motherboard.
- Locate analog input cards in slots furthest away from the power supply.
- Locate video cards and other high power PCI boards in slots furthest removed from the analog
 input cards.

The following guidelines help mitigate ground loop noise for PXI devices:

- Ensure that the screws on the front panel of the device are tightened down.
- Ensure that any external equipment that is providing a signal, and is not floating with
 respect to ground (for example, it is not a passive sensor or a battery-operated device), is
 connected to the same ground as the chassis.
- On rack mounted systems, ground the chassis to the metal rack mount to reduce ground loop
 currents.

Parent topic:

Noise

<!--NI_TOPIC bundle=ni-reconfigurable-oscilloscopes path=peer-to-peer-streaming.html language=enus -->
## TOPIC 00056: Peer-to-Peer Streaming

- bundle_id: `ni-reconfigurable-oscilloscopes`
- source_path: `peer-to-peer-streaming.html`
- source_url: https://docs-be.ni.com/bundle/ni-reconfigurable-oscilloscopes/raw/resource/enus/peer-to-peer-streaming.html
- document_id: `ni-reconfigurable-oscilloscopes`
- page_type: `leaf`
- content_type: `concept`
- source_description: This device supports peer-to-peer data streaming. Use LabVIEW FPGA to configure your device to set up a peer-to-peer streaming session. Peer-to-Peer Resource AvailabilityReconfigurable oscilloscopes support both Peer-to-Peer Reader and Peer-to-Peer Writer streams. You can configure a total of 16 str

### Peer-to-Peer Streaming

This device supports peer-to-peer data streaming. Use LabVIEW FPGA to configure your device to
 set up a peer-to-peer streaming session.

#### Peer-to-Peer Resource
 Availability

Reconfigurable oscilloscopes support both Peer-to-Peer Reader
 and Peer-to-Peer Writer streams. You can configure a total of 16 streams. The
 following table lists the stream types available for the VSTs.

| FIFO Type | Description |
| --- | --- |
| DMA input | Reads data into the FIFO from the VI. |
| DMA output | Writes data from the FIFO into the VI. |
| P2P writer | Writes data to the peer-to-peer reader device. |
| P2P reader | Reads data from the peer-to-peer writer device. |

Parent topic:

Programming

<!--NI_TOPIC bundle=ni-reconfigurable-oscilloscopes path=probe-compensation.html language=enus -->
## TOPIC 00057: Probe Compensation

- bundle_id: `ni-reconfigurable-oscilloscopes`
- source_path: `probe-compensation.html`
- source_url: https://docs-be.ni.com/bundle/ni-reconfigurable-oscilloscopes/raw/resource/enus/probe-compensation.html
- document_id: `ni-reconfigurable-oscilloscopes`
- page_type: `leaf`
- content_type: `concept`
- source_description: Adjusting the tunable probe capacitor to get a flat frequency response is called probe compensation. Probe compensation balances the electrical properties of the probe to the particular digitizer you are using. The following figure illustrates that an undercompensated probe attenuates higher frequen

### Probe Compensation

Adjusting the tunable probe capacitor to get a flat frequency response is called probe
 compensation. Probe compensation balances the electrical properties of the probe to the
 particular digitizer you are using. The following figure illustrates that an undercompensated
 probe attenuates higher frequency signals, whereas an overcompensated probe amplifies higher
 frequencies.

[IMAGE alt='image' src='GUID-CA94273C-B40A-4ABC-950F-3B1B2C75F370-a5.gif']

Tip

#### How to Compensate a Probe

To compensate a
 probe, complete the following steps:

1. Connect the BNC end of the probe to an input channel of the digitizer, either CH 0 or CH 1,
 and select X10 attenuation on the body of the probe tip.
2. Attach the BNC adapter (probe accessory) to the tip of the probe.
3. Connect the SMB100 probe-compensation cable to PFI1.
4. Attach the probe with the BNC adapter to the BNC female end of the SMB100 cable.
5. Enable the probe compensation signal on PFI1.
6. Digitize data on the input channel. Adjust the vertical range on the input channel until the
 signal starts to clip. Then increase the vertical range one step so that it no longer clips to
 ensure that you use the main dynamic range of the ADC.
7. Adjust the tunable capacitor to make the waveform look as square as possible.
8. For the most accurate measurements, compensate probes for each channel (CH 0 and CH 1) and
 use them on that channel only. Recompensate when using the probe on a different channel.

Parent topic:

Probes and Their Effects

<!--NI_TOPIC bundle=ni-reconfigurable-oscilloscopes path=probes-and-their-effects.html language=enus -->
## TOPIC 00058: Probes and Their Effects

- bundle_id: `ni-reconfigurable-oscilloscopes`
- source_path: `probes-and-their-effects.html`
- source_url: https://docs-be.ni.com/bundle/ni-reconfigurable-oscilloscopes/raw/resource/enus/probes-and-their-effects.html
- document_id: `ni-reconfigurable-oscilloscopes`
- page_type: `leaf`
- content_type: `concept`
- source_description: Probes work with digitizers as part of your measurement system. Signals travel from the tip of the probe to the input amplifier and are then digitized by the ADC. This signal path makes the probe an important electrical system component that can affect the accuracy of the measurement. A probe can po

### Probes and Their Effects

Probes work with digitizers as part of your measurement system. Signals travel from the tip of
 the probe to the input amplifier and are then digitized by the ADC. This signal path
 makes the probe an important electrical system component that can affect the accuracy of
 the measurement. A probe can potentially influence measured amplitude and phase, and the
 signal can pick up additional noise on its way to the input stage. Although NI
 high-speed digitizers do not ship with probes, several types of probes are available,
 including passive, active, and current probes.

#### Passive Probes

The passive probe is the most widely used general-purpose
 probe. Passive probes are specified by bandwidth (or rise time), attenuation ratio,
 compensation range, and mechanical design aspects. Probes with attenuation, X10,
 X100, or X1000, have a tunable capacitor that can reduce capacitive effects at the
 input. The ability to cancel or minimize effective capacitance improves the probe's
 bandwidth and rise time. The following figure shows a typical X10 probe
 model:

[IMAGE alt='image' src='GUID-3D306B9F-FFBC-420A-9922-2189F2A6AF91-a5.gif']

Adjust the tunable capacitor, C<sub>p</sub>, to obtain a flat frequency
 response. C<sub>p</sub> is the probe capacitance, R<sub>p</sub> is the probe
 resistance, C<sub>in</sub> is the input capacitance, R<sub>in</sub> is the input
 resistance of the digitizer.

Analytically, obtaining a flat frequency response
 means that

R

in

R

in

+

R

p

=

C

p

C

p

+

C

in

+

C

c

When tuned for flat response, it can be shown that

R

in

C

in

+

C

p

=

C

p

R

p

or the time constant of the probe equals the time constant of the digitizer
 input.

#### Active Probes

Active probes, such as differential and Field-Effect
 Transistor (FET) probes, contain active circuitry in the probe itself to reject
 noise and amplify the signal. FET probes are useful for low-voltage measurements at
 high frequencies and differential probes are noted for their high Common-Mode
 Rejection Ratio (CMRR) and nongrounded reference.

#### Current Probes

Current probes magnetically measure AC and DC current
 flowing in a conductor instead of using a series resistance in the loop to measure
 current. This lack of series resistance causes very little interference in the
 circuit being tested.

Parent topic:

Oscilloscopes Fundamentals

Related concepts:

- Probe Compensation

<!--NI_TOPIC bundle=ni-reconfigurable-oscilloscopes path=programming.html language=enus -->
## TOPIC 00059: Programming

- bundle_id: `ni-reconfigurable-oscilloscopes`
- source_path: `programming.html`
- source_url: https://docs-be.ni.com/bundle/ni-reconfigurable-oscilloscopes/raw/resource/enus/programming.html
- document_id: `ni-reconfigurable-oscilloscopes`
- page_type: `leaf`
- content_type: `concept`
- source_description: This section provides reference information for using instrument design libraries to create application-specific instrumentation designs for reconfigurable oscilloscopes. The manufacturer recommends that you have 8 GB or more of system memory and requires a 64-bit operating system for compiling LabV

### Programming

Note

<!--NI_TOPIC bundle=ni-reconfigurable-oscilloscopes path=real-time-sampling.html language=enus -->
## TOPIC 00060: Real-Time Sampling

- bundle_id: `ni-reconfigurable-oscilloscopes`
- source_path: `real-time-sampling.html`
- source_url: https://docs-be.ni.com/bundle/ni-reconfigurable-oscilloscopes/raw/resource/enus/real-time-sampling.html
- document_id: `ni-reconfigurable-oscilloscopes`
- page_type: `leaf`
- content_type: `concept`
- source_description: Real-time sampling is the default sampling method used by NI high-speed digitizers. In real-time sampling, the digitizer gathers all the samples for a waveform in one acquisition with one trigger event.

### Real-Time Sampling

Real-time sampling is the default sampling method used by NI high-speed digitizers. In real-time
 sampling, the digitizer gathers all the samples for a waveform in one acquisition with one
 trigger event.

Parent topic:

Sampling Methods

Related concepts:

- Equivalent-Time Sampling and Random Interleaved Sampling
- Time Interleaved Sampling

<!--NI_TOPIC bundle=ni-reconfigurable-oscilloscopes path=record-length.html language=enus -->
## TOPIC 00061: Record Length

- bundle_id: `ni-reconfigurable-oscilloscopes`
- source_path: `record-length.html`
- source_url: https://docs-be.ni.com/bundle/ni-reconfigurable-oscilloscopes/raw/resource/enus/record-length.html
- document_id: `ni-reconfigurable-oscilloscopes`
- page_type: `leaf`
- content_type: `concept`
- source_description: Record length refers to the number of samples, or data points, the digitizer acquires for each channel in a single acquisition. Maximum DurationRecord length limits the maximum duration of a single-shot acquisition. For example, with a 1,000-sample record and a sample rate of 20 MS/s, the duration o

### Record Length

Record length refers to the number of samples, or data points, the digitizer acquires for each
 channel in a single acquisition.

#### Maximum Duration

Record length limits the
 maximum duration of a single-shot acquisition. For example, with a 1,000-sample record and a
 sample rate of 20 MS/s, the duration of acquisition is 50 µs (the number of points multiplied by
 the acquisition time per sample, or 1,000 x 50 ns. With a 100,000-sample record and a sample
 rate of 20 MS/s, the duration of the acquisition is 5 ms (100,000 x 50 ns).

Parent topic:

Oscilloscopes Fundamentals

<!--NI_TOPIC bundle=ni-reconfigurable-oscilloscopes path=reference-clock-phase-lock-loop.html language=enus -->
## TOPIC 00062: Reference Clock/Phase-Lock Loop

- bundle_id: `ni-reconfigurable-oscilloscopes`
- source_path: `reference-clock-phase-lock-loop.html`
- source_url: https://docs-be.ni.com/bundle/ni-reconfigurable-oscilloscopes/raw/resource/enus/reference-clock-phase-lock-loop.html
- document_id: `ni-reconfigurable-oscilloscopes`
- page_type: `leaf`
- content_type: `concept`
- source_description: The reference clock is used in the Phase-Locked Loop (PLL) circuit of a digitizer to synchronize the internal oscillator to the reference clock. The frequency stability of the internal oscillator matches that of the PLL reference clock when the two are phase locked. In turn, phase locking synchroniz

### Reference Clock/Phase-Lock Loop

The reference clock is used in the Phase-Locked Loop (PLL) circuit of a digitizer to synchronize
 the internal oscillator to the reference clock. The frequency stability of the internal
 oscillator matches that of the PLL reference clock when the two are phase locked. In turn, phase
 locking synchronizes clocks of multiple devices that are phase locked to the same reference
 clock. The most common frequency for a reference clock is 10 MHz because a clock of that
 frequency can generally be shared over a cable without much attenuation or loss. However, the
 frequency range of reference clocks can vary anywhere from 1 MHz to 20 MHz. The following figure
 shows a block diagram of a basic PLL:

[IMAGE alt='image' src='GUID-1D3A76C8-0E6F-4143-9EA5-E6F24AAF207C-a5.gif']

The operation of this circuit is typical of all PLLs. A PLL is a feedback control system that
 controls the frequency and phase of a Voltage Controlled Oscillator (VCO). The input signal is
 applied to a phase detector. The output of the VCO connects to the other input. As shown in the
 previous diagram, the frequencies of both signals are the same. The output of the phase detector
 develops a voltage proportional to the phase difference between the two input signals. The
 lowpass filter receives this signal from the phase detector. The lowpass filter determines the
 dynamic characteristics of the PLL. The filtered signal controls the VCO.

Parent topic:

Oscilloscopes Fundamentals

<!--NI_TOPIC bundle=ni-reconfigurable-oscilloscopes path=resolution.html language=enus -->
## TOPIC 00063: Resolution

- bundle_id: `ni-reconfigurable-oscilloscopes`
- source_path: `resolution.html`
- source_url: https://docs-be.ni.com/bundle/ni-reconfigurable-oscilloscopes/raw/resource/enus/resolution.html
- document_id: `ni-reconfigurable-oscilloscopes`
- page_type: `leaf`
- content_type: `concept`
- source_description: Resolution is the smallest input voltage change a digitizer can capture. Resolution can be expressed in bits (LSB), in proportions, or in percent of full scale. For example, a system has 12-bit resolution, one part in 4,096 resolution, and 0.0244% of full scale.Resolution limits the precision of a m

### Resolution

Resolution is the smallest input voltage change a digitizer can capture. Resolution can be
 expressed in bits (LSB), in proportions, or in percent of full scale. For example, a system has
 12-bit resolution, one part in 4,096 resolution, and 0.0244% of full scale.

Resolution limits the precision of a measurement. The higher the resolution (number of bits), the
 more precise the measurement. An 8-bit ADC divides the vertical range of the input amplifier into
 256 discrete levels. With a vertical range of 10 V, the 8-bit ADC cannot ideally resolve voltage
 differences smaller than 39 mV. In comparison, a 14-bit ADC with 16,384 discrete levels can
 ideally resolve voltage differences as small as 610 µV.

| Bits | Resolution | % FS |
| --- | --- | --- |
| 8 | 1/256 | .390 |
| 10 | 1/1024 | .0976 |
| 12 | 1/4096 | .0244 |
| 14 | 1/16384 | .0061 |
| 16 | 1/65536 | .0015 |

The following figure shows the transfer function of a 3-bit ADC with a vertical range of 5 V
 having an ideal resolution of 5/8 V/LSB:

[IMAGE alt='image' src='GUID-EFF80BFD-FF83-4CE5-9785-AB151BB12371-a5.gif']

Parent topic:

Oscilloscopes Fundamentals

<!--NI_TOPIC bundle=ni-reconfigurable-oscilloscopes path=sample-clock.html language=enus -->
## TOPIC 00064: Sample Clock

- bundle_id: `ni-reconfigurable-oscilloscopes`
- source_path: `sample-clock.html`
- source_url: https://docs-be.ni.com/bundle/ni-reconfigurable-oscilloscopes/raw/resource/enus/sample-clock.html
- document_id: `ni-reconfigurable-oscilloscopes`
- page_type: `leaf`
- content_type: `concept`
- source_description: The sample clock is sent to the ADC of each channel and to the acquisition engine to control the sampling rate of a device. The sample clock sources are as follows. Internal Sample ClockHigh-speed digitizers and oscilloscopes have an onboard (internal) clock that controls the sampling rate as well a

### Sample Clock

The sample clock is sent to the ADC of each channel and to the acquisition engine to control the
 sampling rate of a device. The sample clock sources are as follows.

#### Internal Sample Clock

High-speed digitizers and
 oscilloscopes have an onboard (internal) clock that controls the sampling rate as well as other
 timing functionality of the device. In most cases, the onboard oscillator is a Voltage
 Controlled Crystal Oscillator (VCXO). Typically, an onboard DAC (digital to analog converter) is
 used to calibrate the VCXO to exactly the desired clock rate. This DAC can also be used to
 adjust the frequency of the VCXO to phase lock it to a *reference clock*. The maximum
 sampling rate of a device is usually determined by the speed of the onboard clock. However,
 other sampling rates can be achieved by two methods; decimation of the data or dividing down the
 onboard clock.

#### Decimation Method

In the decimation method, the ADC samples at the rate of the onboard clock and then sends its
 digital data to a decimator that essentially discards samples at a specific interval to achieve
 slower effective sampling rates. The valid sampling rates are always an integer divisor of the
 onboard clock. For example, if the onboard clock is 100 MHz but you want to sample at 25 MS/s,
 you must use decimation. The decimation method would discard all data except for every fourth
 datapoint to achieve exactly 1/4 of the maximum sample rate (or onboard clock rate).

#### Divide Down Clock Method

Some oscilloscopes use the divide down clock method. In this method the onboard clock is
 sent through a series of clock dividers, and then that clock is sent to the ADC. Typically,
 the decimation method is preferred over the divide down clock method.

Note

#### External
 Sample Clock

Some digitizers and oscilloscopes can accept an external sample
 clock. This external sample clock is used to replace the onboard clock (the VCXO) for
 synchronization or to achieve a sampling rate that cannot be specified by using the onboard
 clock. Some devices can also decimate the external sample clock to achieve a sampling rate
 that is an integer divisor of the external sample clock. For example, if the external sample
 clock is 70 MHz, you could decimate the clock by a factor of 2 and achieve a 35 MS/s
 sampling rate.

Note

reference clock

Parent topic:

Oscilloscopes Fundamentals

Related concepts:

- Reference Clock/Phase-Lock Loop

<!--NI_TOPIC bundle=ni-reconfigurable-oscilloscopes path=sample-rate.html language=enus -->
## TOPIC 00065: Sample Rate

- bundle_id: `ni-reconfigurable-oscilloscopes`
- source_path: `sample-rate.html`
- source_url: https://docs-be.ni.com/bundle/ni-reconfigurable-oscilloscopes/raw/resource/enus/sample-rate.html
- document_id: `ni-reconfigurable-oscilloscopes`
- page_type: `leaf`
- content_type: `concept`
- source_description: Sample rate, specified in samples per second (S/s), is the rate at which a signal is sampled and digitized by an Analog-to-Digital Converter (ADC). According to the Nyquist theorem, a sample rate at least twice the highest frequency of the signal produces accurate measurements if the analog bandwidt

### Sample Rate

Sample rate, specified in samples per second (S/s), is the rate at which a signal is sampled and
 digitized by an Analog-to-Digital Converter (ADC).

According to the *Nyquist theorem*, a sample rate at least twice the highest
 frequency of the signal produces accurate measurements if the *analog bandwidth* is
 wide enough to let the signal pass through without attenuation. A higher sample rate captures
 more waveform details for the time domain measurements.

The following figure illustrates a 1 MHz sine wave sampled by a 2 MS/s ADC and a 20 MS/s ADC.
 The faster ADC digitizes 20 points per cycle of the input signal compared with 2 points per
 cycle with the slower ADC. In this example, the higher sample rate more accurately captures
 the waveform shape:

[IMAGE alt='image' src='GUID-3CC40B3E-E133-477D-8BE1-8E0D541956B5-a5.gif']

Parent topic:

Oscilloscopes Fundamentals

Related concepts:

- Nyquist Theorem
- Bandwidth
- Undersampling
- Oversampling

<!--NI_TOPIC bundle=ni-reconfigurable-oscilloscopes path=sampling-methods.html language=enus -->
## TOPIC 00066: Sampling Methods

- bundle_id: `ni-reconfigurable-oscilloscopes`
- source_path: `sampling-methods.html`
- source_url: https://docs-be.ni.com/bundle/ni-reconfigurable-oscilloscopes/raw/resource/enus/sampling-methods.html
- document_id: `ni-reconfigurable-oscilloscopes`
- page_type: `leaf`
- content_type: `concept`
- source_description: The sampling method you use determines how the digitizer collects sample points. Depending on whether the signal is changing slowly or quickly, you can choose one of the following methods described in Related concepts.

### Sampling Methods

The sampling method you use determines how the digitizer collects sample points. Depending on
 whether the signal is changing slowly or quickly, you can choose
 one of the following methods described in *Related
 concepts*.

Parent topic:

Oscilloscopes Fundamentals

Related concepts:

- Real-Time Sampling
- Equivalent-Time Sampling and Random Interleaved Sampling
- Time Interleaved Sampling

<!--NI_TOPIC bundle=ni-reconfigurable-oscilloscopes path=scanning-speed.html language=enus -->
## TOPIC 00067: Scanning Speed

- bundle_id: `ni-reconfigurable-oscilloscopes`
- source_path: `scanning-speed.html`
- source_url: https://docs-be.ni.com/bundle/ni-reconfigurable-oscilloscopes/raw/resource/enus/scanning-speed.html
- document_id: `ni-reconfigurable-oscilloscopes`
- page_type: `leaf`
- content_type: `concept`
- source_description: The scanning speed is the number of video frames generated per second. The scanning speed and the number of lines per frame depend on the video format. NTSC specifies a scanning speed of approximately 30 frames per seconds and 525 lines per frame while PAL and SECAM specify a rate of 25 frames per s

### Scanning Speed

The scanning speed is the number of video frames generated per second. The scanning speed and the
 number of lines per frame depend on the video format. NTSC specifies a scanning speed of
 approximately 30 frames per seconds and 525 lines per frame while PAL and SECAM specify
 a rate of 25 frames per second and 625 lines per frame.

Parent topic:

Video Fundamentals

<!--NI_TOPIC bundle=ni-reconfigurable-oscilloscopes path=self-calibrating-a-reconfigurable-oscilloscop.html language=enus -->
## TOPIC 00068: Self-Calibrating a Reconfigurable Oscilloscope

- bundle_id: `ni-reconfigurable-oscilloscopes`
- source_path: `self-calibrating-a-reconfigurable-oscilloscop.html`
- source_url: https://docs-be.ni.com/bundle/ni-reconfigurable-oscilloscopes/raw/resource/enus/self-calibrating-a-reconfigurable-oscilloscop.html
- document_id: `ni-reconfigurable-oscilloscopes`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can self-calibrate your device in MAX by selecting your device under Devices and Interfaces in MAX and selecting Self-Calibrate at the top of the device window.Reconfigurable oscilloscopes are externally calibrated at the factory; however, you should perform a self-calibration in any of the foll

### Self-Calibrating a Reconfigurable Oscilloscope

You can self-calibrate your device in MAX by selecting your device under Devices and
 Interfaces in MAX and selecting Self-Calibrate at
 the top of the device window.

Reconfigurable oscilloscopes are externally calibrated at the factory; however, you should
 perform a self-calibration in any of the following situations:

- After first installing the device into your chassis and allowing the device to warm up.
- After any module in the chassis is installed, uninstalled, or moved.
- When the system is in an environment where the ambient temperature varies or the module
 temperature has drifted more than ±5 °C from the temperature at the last
 self-calibration.
- To periodically adjust for small performance drifts that occur with product aging.

Note

Self-Calibration

When using LabVIEW, you can self-calibrate your device using the Self Calibrate VI, located on
 the Functions»Software-Designed
 Instruments»Oscilloscopes»your
 device»Calibration palette.

For more information about self-calibrating your device, refer to the
 *Self-Calibration* topic for your device.

<!--NI_TOPIC bundle=ni-reconfigurable-oscilloscopes path=sinad.html language=enus -->
## TOPIC 00069: Signal-to-Noise-and-Distortion (SINAD)

- bundle_id: `ni-reconfigurable-oscilloscopes`
- source_path: `sinad.html`
- source_url: https://docs-be.ni.com/bundle/ni-reconfigurable-oscilloscopes/raw/resource/enus/sinad.html
- document_id: `ni-reconfigurable-oscilloscopes`
- page_type: `leaf`
- content_type: `concept`
- source_description: Signal-to-Noise-and-Distortion (SINAD) is the ratio of the rms signal amplitude (set to 1 dB below Full Scale) to the rms sum of all other spectral components, including the harmonics but excluding DC. SINAD is usually expressed in dB.

### Signal-to-Noise-and-Distortion (SINAD)

Signal-to-Noise-and-Distortion (SINAD) is the ratio of the rms signal amplitude (set to 1 dB
 below Full Scale) to the rms sum of all other spectral components, including the harmonics but
 excluding DC. SINAD is usually expressed in dB.

Parent topic:

Frequency Domain Fundamentals

<!--NI_TOPIC bundle=ni-reconfigurable-oscilloscopes path=spurious-free-dynamic-range.html language=enus -->
## TOPIC 00070: Spurious Free Dynamic Range

- bundle_id: `ni-reconfigurable-oscilloscopes`
- source_path: `spurious-free-dynamic-range.html`
- source_url: https://docs-be.ni.com/bundle/ni-reconfigurable-oscilloscopes/raw/resource/enus/spurious-free-dynamic-range.html
- document_id: `ni-reconfigurable-oscilloscopes`
- page_type: `leaf`
- content_type: `concept`
- source_description: Spurious Free Dynamic Range (SFDR) is the usable dynamic range before spurious noise interferes with or distorts the fundamental signal. The amplitude of the fundamental signal is usually -1 dBFS. SFDR is the measure of the ratio in amplitude between the fundamental signal and the largest harmonical

### Spurious Free Dynamic Range

Spurious Free Dynamic Range (SFDR) is the usable dynamic range before spurious noise interferes
 with or distorts the fundamental signal. The amplitude of the fundamental signal is
 usually -1 dBFS. SFDR is the measure of the ratio in amplitude between the fundamental
 signal and the largest harmonically or non-harmonically related spur from DC to the full
 Nyquist bandwidth (half the sampling rate). A spur is any frequency bin on a spectrum
 analyzer, or from a Fourier transform, of the analog signal. SFDR is expressed
 in dBc.

The following figure illustrates how SFDR is measured:

[IMAGE alt='image' src='GUID-861BAC5D-2ADD-4F80-AC3F-FCCC6937774C-a5.gif']

Parent topic:

Frequency Domain Fundamentals

<!--NI_TOPIC bundle=ni-reconfigurable-oscilloscopes path=stream-to-host-sample-project.html language=enus -->
## TOPIC 00071: Stream to Host Sample Project

- bundle_id: `ni-reconfigurable-oscilloscopes`
- source_path: `stream-to-host-sample-project.html`
- source_url: https://docs-be.ni.com/bundle/ni-reconfigurable-oscilloscopes/raw/resource/enus/stream-to-host-sample-project.html
- document_id: `ni-reconfigurable-oscilloscopes`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Stream to Host sample project provides a host interface that is similar to other digitizer APIs.To get started with the Stream to Host sample project, complete the following steps: Launch LabVIEW. Select File»Create Project. On the left side of the Create Project window, select Oscilloscopes. On

### Stream to Host Sample Project

The Stream to Host sample project provides a host interface that is similar to other digitizer
 APIs.

To get started with the Stream to Host sample project, complete the following steps:

1. Launch LabVIEW.
2. Select File » Create Project .
3. On the left side of the Create Project window, select Oscilloscopes .
4. On the right side of the Create Project window, select the
 Stream to Host sample project and click
 Next .
5. Specify a name, location, and device target for the project in the Create Project window and click Finish .
LabVIEW creates, configures, and opens a new Stream to Host project.
6. In the project tree, navigate to My Computer » Project Documentation , open Stream to Host Documentation.html , and navigate to the Running this Sample Project section of the documentation.
7. Follow the instructions in the project documentation and VI block diagram comments to use and customize the sample project.

Parent topic:

Creating an Application with Instrument Design Libraries

<!--NI_TOPIC bundle=ni-reconfigurable-oscilloscopes path=tdc.html language=enus -->
## TOPIC 00072: Time-to-Digital Converter (TDC)

- bundle_id: `ni-reconfigurable-oscilloscopes`
- source_path: `tdc.html`
- source_url: https://docs-be.ni.com/bundle/ni-reconfigurable-oscilloscopes/raw/resource/enus/tdc.html
- document_id: `ni-reconfigurable-oscilloscopes`
- page_type: `leaf`
- content_type: `concept`
- source_description: A Time-to-Digital Converter (TDC) is a circuit that is used to measure the time between two events. For digitizers, the TDC measures the time elapsed from when a trigger is received by the digitizer to the time the first sample is taken.

### Time-to-Digital Converter (TDC)

A Time-to-Digital Converter (TDC) is a circuit that is used to measure the time between two
 events. For digitizers, the TDC measures the time elapsed from when a trigger is received by the
 digitizer to the time the first sample is taken.

[IMAGE alt='image' src='GUID-140C29F1-F454-40BD-AE90-066983DFA4EF-a5.gif']

Parent topic:

Oscilloscopes Fundamentals

<!--NI_TOPIC bundle=ni-reconfigurable-oscilloscopes path=thd.html language=enus -->
## TOPIC 00073: Total Harmonic Distortion (THD)

- bundle_id: `ni-reconfigurable-oscilloscopes`
- source_path: `thd.html`
- source_url: https://docs-be.ni.com/bundle/ni-reconfigurable-oscilloscopes/raw/resource/enus/thd.html
- document_id: `ni-reconfigurable-oscilloscopes`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Total Harmonic Distortion (THD) of a signal is the ratio of the sum of the powers of the first five harmonics above the measured fundamental frequency to the power of the fundamental frequency. THD is usually expressed in dB or dBc. Measurements for calculating the THD are made at the output of

### Total Harmonic Distortion (THD)

The Total Harmonic Distortion (THD) of a signal is the ratio of the sum of the powers of the
 first five harmonics above the measured fundamental frequency to
 the power of the fundamental frequency. THD is usually expressed
 in dB or dBc. Measurements for calculating the THD are made at
 the output of a device under specified conditions.

Parent topic:

Frequency Domain Fundamentals

<!--NI_TOPIC bundle=ni-reconfigurable-oscilloscopes path=time-interleaved-sampling.html language=enus -->
## TOPIC 00074: Time Interleaved Sampling

- bundle_id: `ni-reconfigurable-oscilloscopes`
- source_path: `time-interleaved-sampling.html`
- source_url: https://docs-be.ni.com/bundle/ni-reconfigurable-oscilloscopes/raw/resource/enus/time-interleaved-sampling.html
- document_id: `ni-reconfigurable-oscilloscopes`
- page_type: `leaf`
- content_type: `concept`
- source_description: Time Interleaved Sampling (TIS) is a technique to increase the real-time sample rate of a device. TIS uses multiple Analog-to-Digital Converters (ADCs) to sample the same input waveform, but at different relative phases. The hardware then interleaves these samples to create the waveform as if only o

### Time Interleaved Sampling

Time Interleaved Sampling (TIS) is a technique to increase the real-time sample rate of a device.
 TIS uses multiple Analog-to-Digital Converters (ADCs) to sample the same input waveform, but
 at different relative phases. The hardware then interleaves these samples to create the
 waveform as if only one ADC were sampling the waveform at a higher sample rate.

#### How TIS Works

When you enable TIS on a channel,
 the device samples the input signal of that channel using more than one ADC. The clocks of these
 ADCs are shifted to a phase that reflects the time when an ADC of a higher sample rate would
 acquire a point. An example is shown in the following figure.

[IMAGE alt='image' src='GUID-5F8C9A23-89CB-42ED-8F34-DE5A6BCAB1A6-a5.gif']

To obtain a 2 G/s TIS rate using two ADCs, each operated at 1 G/s, the 1 GHz clock of
 one ADC is shifted 180 degrees with respect to the 1 GHz clock of the other ADC.

The data
 returned is in order and is acquired in real time. Therefore, the input signal is not required
 to be repetitive.

#### How TIS Affects Measurements

Because multiple
 ADCs are used in TIS, it is possible for mismatch between ADCs and phase offset between clocks
 to cause small changes in the spectral performance of the device. NI digitizers calibrate most
 of these changes out, but some small residual changes may persist. It may be important,
 particularly in frequency domain applications, to understand the following effects.

Offset Mismatch

Gain Mismatch

Phase Offset

Parent topic:

Sampling Methods

<!--NI_TOPIC bundle=ni-reconfigurable-oscilloscopes path=triggering.html language=enus -->
## TOPIC 00075: Triggering

- bundle_id: `ni-reconfigurable-oscilloscopes`
- source_path: `triggering.html`
- source_url: https://docs-be.ni.com/bundle/ni-reconfigurable-oscilloscopes/raw/resource/enus/triggering.html
- document_id: `ni-reconfigurable-oscilloscopes`
- page_type: `leaf`
- content_type: `concept`
- source_description: A trigger is an external stimulus that initiates one or more instrument functions. Trigger stimuli include digital edges, software functions, and analog levels. The trigger can be derived from attributes of the signal to be acquired, such as the level and slope of the signal. You can use several kin

### Triggering

A trigger is an external stimulus that initiates one or more instrument functions. Trigger
 stimuli include digital edges, software functions, and analog levels. The trigger can be
 derived from attributes of the signal to be acquired, such as the level and slope of the
 signal.

You can use several kinds of triggering with high-speed digitizers,
 including *hysteresis*, *edge*, and
 *window triggering*.

Parent topic:

Oscilloscopes Fundamentals

Related concepts:

- Hysteresis Triggers
- Edge Triggers
- Window Triggers

<!--NI_TOPIC bundle=ni-reconfigurable-oscilloscopes path=troubleshooting.html language=enus -->
## TOPIC 00076: Troubleshooting

- bundle_id: `ni-reconfigurable-oscilloscopes`
- source_path: `troubleshooting.html`
- source_url: https://docs-be.ni.com/bundle/ni-reconfigurable-oscilloscopes/raw/resource/enus/troubleshooting.html
- document_id: `ni-reconfigurable-oscilloscopes`
- page_type: `leaf`
- content_type: `concept`
- source_description: If your device does not appear in MAX, complete the following steps: Verify that you have followed the software installation steps properly. In the MAX Configuration pane, click Devices and Interfaces. Expand the Chassis tree to see the list of installed devices, and press F5 to refresh the list. If

### Troubleshooting

If your device does not appear in MAX, complete the following steps:

1. Verify that you have followed the software installation steps properly.
2. In the MAX Configuration pane, click Devices and Interfaces .
3. Expand the Chassis tree to see the list of installed devices, and press
 F5 to refresh the list.
4. If the module is still not listed, disconnect all external signals from the hardware, power off
 the system, ensure that all hardware is correctly installed, and restart the system.
 Caution Disconnect
 or disable any external connections to the module front panel before powering
 off the device. Applying external signals while the device is powered off may
 cause damage.
5. In Windows, navigate to the Device Manager .
6. If you are using a PXI controller, verify that a NI entry appears in the
 system device list. If error conditions appear in the list, right-click the
 NI-RIO FPGA Device node and your device node and select
 Update Driver . If you are using a MXI controller,
 right-click PCI-to-PCI Bridge and select
 Properties from the shortcut menu to verify that the
 bridge is enabled.
7. Restart your computer.
8. If the device still fails to appear in MAX, contact NI technical support or visit
 ni.com/support .

<!--NI_TOPIC bundle=ni-reconfigurable-oscilloscopes path=undersampling.html language=enus -->
## TOPIC 00077: Undersampling

- bundle_id: `ni-reconfigurable-oscilloscopes`
- source_path: `undersampling.html`
- source_url: https://docs-be.ni.com/bundle/ni-reconfigurable-oscilloscopes/raw/resource/enus/undersampling.html
- document_id: `ni-reconfigurable-oscilloscopes`
- page_type: `leaf`
- content_type: `concept`
- source_description: Undersampling is essentially sampling too slowly, or sampling at a rate below the Nyquist frequency for a particular signal of interest. Undersampling leads to aliasing and the original signal cannot be properly reconstructed. However, undersampling also requires less memory, so it may be useful in

### Undersampling

Undersampling is essentially sampling too slowly, or sampling at a rate below the
 *Nyquist* frequency for a particular signal of interest. Undersampling
 leads to *aliasing* and the original signal cannot be properly reconstructed.
 However, undersampling also requires less memory, so it may be useful in certain
 applications.

Parent topic:

Sample Rate

Related concepts:

- Nyquist Theorem
- Aliasing

<!--NI_TOPIC bundle=ni-reconfigurable-oscilloscopes path=user-manual-welcome.html language=enus -->
## TOPIC 00078: Reconfigurable Oscilloscopes User Manual

- bundle_id: `ni-reconfigurable-oscilloscopes`
- source_path: `user-manual-welcome.html`
- source_url: https://docs-be.ni.com/bundle/ni-reconfigurable-oscilloscopes/raw/resource/enus/user-manual-welcome.html
- document_id: `ni-reconfigurable-oscilloscopes`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Reconfigurable Oscilloscopes User Manual provides detailed descriptions of the product functionality and the step by step processes for use. Looking for Something Else?For information not found in the User Manual for your product, such as specifications and API reference, browse Related Informat

### Reconfigurable Oscilloscopes
 User Manual

The Reconfigurable Oscilloscopes User Manual provides detailed
 descriptions of the product functionality and the step by step processes for use.

#### Looking for Something Else?

For information not found in the User Manual
 for your product, such as specifications and API reference, browse *Related
 Information*.

Related information:

- Hardware and Software Operating System
 Compatibility
- License Setup and Activation

<!--NI_TOPIC bundle=ni-reconfigurable-oscilloscopes path=using-the-labview-fpga-module.html language=enus -->
## TOPIC 00079: Using the LabVIEW FPGA Module

- bundle_id: `ni-reconfigurable-oscilloscopes`
- source_path: `using-the-labview-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/ni-reconfigurable-oscilloscopes/raw/resource/enus/using-the-labview-fpga-module.html
- document_id: `ni-reconfigurable-oscilloscopes`
- page_type: `leaf`
- content_type: `concept`
- source_description: The LabVIEW FPGA Module enables you to use LabVIEW to create VIs that run on the device. The LabVIEW FPGA Module includes a Functions palette with VIs that can control the I/O, timing, and logic of the device. The LabVIEW FPGA Module synthesizes your custom VI into a form that can be downloaded to t

### Using the LabVIEW FPGA Module

The LabVIEW FPGA Module enables you to use LabVIEW to create VIs that run on the device. The
 LabVIEW FPGA Module includes a Functions palette with VIs that can control the I/O,
 timing, and logic of the device. The LabVIEW FPGA Module synthesizes your custom VI into
 a form that can be downloaded to the FPGA on the device.

When programming LabVIEW host code in Windows, the FPGA module allows you to communicate with the
 FPGA VI on the FPGA. Use read and write methods on the host to write to and read from
 controls and indicators on the FPGA VI. Use DMA methods on the host to transfer data to
 and from the FPGA VI.

Parent topic:

Programming

<!--NI_TOPIC bundle=ni-reconfigurable-oscilloscopes path=using-the-standard-functionality-for-error-in.html language=enus -->
## TOPIC 00080: Using the Standard Functionality for error in Parameters

- bundle_id: `ni-reconfigurable-oscilloscopes`
- source_path: `using-the-standard-functionality-for-error-in.html`
- source_url: https://docs-be.ni.com/bundle/ni-reconfigurable-oscilloscopes/raw/resource/enus/using-the-standard-functionality-for-error-in.html
- document_id: `ni-reconfigurable-oscilloscopes`
- page_type: `leaf`
- content_type: `concept`
- source_description: Many LabVIEW VIs contain error in parameters you can use to manage errors. These parameters typically provide the same, standard functionality. When a node exhibits different parameter functionality, the exceptions are documented in the reference material for that node. Standard error in behavior is

### Using the Standard Functionality for error in Parameters

error in

error in

Note

error in

error in

|  | Error in describes error conditions that occur before this node runs. The default is no error. If an error occurred before this node runs, the node passes the error in value to error out. This node runs normally only if no error occurred before this node runs. If an error occurs while this node runs, it runs normally and sets its own error status in error out. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. |
| --- | --- |

The error in cluster contains the following cluster elements:

|  | Status is TRUE (X) if an error occurred before this node ran or FALSE (✓) to indicate a warning or that no error occurred before this node ran. The default is FALSE. |
| --- | --- |
|  | Code is the error or warning code. The default is 0. If status is TRUE, code is an error code. If status is FALSE, code is 0 or a warning code. |
|  | Source specifies the origin of the error or warning and is, in most cases, the name of the node that produced the error or warning. The default is an empty string. |

Parent topic:

Programming

<!--NI_TOPIC bundle=ni-reconfigurable-oscilloscopes path=using-the-standard-functionality-for-error-ou.html language=enus -->
## TOPIC 00081: Using the Standard Functionality for error out Parameters

- bundle_id: `ni-reconfigurable-oscilloscopes`
- source_path: `using-the-standard-functionality-for-error-ou.html`
- source_url: https://docs-be.ni.com/bundle/ni-reconfigurable-oscilloscopes/raw/resource/enus/using-the-standard-functionality-for-error-ou.html
- document_id: `ni-reconfigurable-oscilloscopes`
- page_type: `leaf`
- content_type: `concept`
- source_description: Many LabVIEW VIs contain an error out parameter you can use to manage errors. These parameters typically provide the same, standard functionality. When a node exhibits different parameter functionality, the exceptions are documented in the reference material for that node.Standard error out function

### Using the Standard Functionality for error out Parameters

Many LabVIEW VIs contain an error out parameter you can use to manage
 errors. These parameters typically provide the same, standard functionality. When a node
 exhibits different parameter functionality, the exceptions are documented in the
 reference material for that node.

Standard error out functionality is as follows:

|  | Error out contains error information. If error in indicates that an error occurred before this VI ran, error out contains the same error information. Otherwise, it describes the error status that this VI produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- | --- |

The error out contains the following cluster elements:

|  | Status is TRUE (X) if an error occurred or FALSE (✓) to indicate a warning or that no error occurred. |
| --- | --- |
|  | Code is the error or warning code. If status is TRUE, code is an error code. If status is FALSE, code is 0 or a warning code. |
|  | Source specifies the origin of the error or warning and is, in most cases, the name of the node that produced the error or warning. |

Parent topic:

Programming

<!--NI_TOPIC bundle=ni-reconfigurable-oscilloscopes path=vertical-range-and-offset.html language=enus -->
## TOPIC 00082: Vertical Range and Offset

- bundle_id: `ni-reconfigurable-oscilloscopes`
- source_path: `vertical-range-and-offset.html`
- source_url: https://docs-be.ni.com/bundle/ni-reconfigurable-oscilloscopes/raw/resource/enus/vertical-range-and-offset.html
- document_id: `ni-reconfigurable-oscilloscopes`
- page_type: `leaf`
- content_type: `concept`
- source_description: Vertical range is the peak-to-peak voltage span that a digitizer can measure at the input connector. Most digitizers have several choices for vertical range.Vertical offset is the voltage the vertical range is centered on. Vertical offset positions the vertical range around an arbitrary DC value. Us

### Vertical Range and Offset

Vertical range is the peak-to-peak voltage span that a digitizer can measure at the input
 connector. Most digitizers have several choices for vertical range.

Vertical offset is the voltage the vertical range is centered on. Vertical offset positions the
 vertical range around an arbitrary DC value. Using this offset allows you to examine small
 changes in the input signal, which can improve the accuracy of your measurement.

For example, imagine that you are acquiring the waveform shown in the following figure that
 outputs 0.75 V to 1.25 V. Without using vertical offset, you would need to specify a range of
 2.5 V (±1.25 V) to capture the waveform.

[IMAGE alt='image' src='GUID-6BC9A3E5-32BD-4859-AB36-435DABE16199-a5.gif']

Parent topic:

Oscilloscopes Fundamentals

<!--NI_TOPIC bundle=ni-reconfigurable-oscilloscopes path=video-format-naming.html language=enus -->
## TOPIC 00083: Video Format Naming

- bundle_id: `ni-reconfigurable-oscilloscopes`
- source_path: `video-format-naming.html`
- source_url: https://docs-be.ni.com/bundle/ni-reconfigurable-oscilloscopes/raw/resource/enus/video-format-naming.html
- document_id: `ni-reconfigurable-oscilloscopes`
- page_type: `leaf`
- content_type: `concept`
- source_description: The most common standard video formats (NTSC, PAL, and SECAM) are known by acronyms. Sometimes extra letters are appended to the front of the names to indicate the refresh rate. For example, M-PAL and M-NTSC have a refresh rate of 59.94 fields per second. Standard Definition (SDTV) FormatsThe defini

### Video Format Naming

The most common standard video formats (NTSC, PAL, and SECAM) are known by acronyms. Sometimes
 extra letters are appended to the front of the names to indicate the refresh rate. For
 example, M-PAL and M-NTSC have a refresh rate of 59.94 fields per second.

#### Standard Definition (SDTV) Formats

The
 definition of standard composite video signal formats differs from country to
 country.

M-NTSC

B/G-PAL

SECAM

M-PAL

#### EDTV
 and HDTV Video Formats

Note

#### EDTV Formats

- 480i/59.94 fps
- 480i/60 fps
- 480p/59.94 Fps
- 480p/60 Fps
- 576i/50 fps
- 576p/50 Fps

#### HDTV Signal Formats

- 720p/30 Fps (not supported by NI-SCOPE)
- 720p/50 Fps
- 720p/59.94 Fps
- 720p/60 Fps
- 1080i/50 fps
- 1080i/59.94 fps
- 1080i/60 fps
- 1080p/24 Fps

Parent topic:

Video Fundamentals

<!--NI_TOPIC bundle=ni-reconfigurable-oscilloscopes path=video-fundamentals.html language=enus -->
## TOPIC 00084: Video Fundamentals

- bundle_id: `ni-reconfigurable-oscilloscopes`
- source_path: `video-fundamentals.html`
- source_url: https://docs-be.ni.com/bundle/ni-reconfigurable-oscilloscopes/raw/resource/enus/video-fundamentals.html
- document_id: `ni-reconfigurable-oscilloscopes`
- page_type: `leaf`
- content_type: `concept`

### Video Fundamentals

- [Composite and Component Video Signals](composite-and-component-video-signals.html)
- [Video Format Naming](video-format-naming.html)
- [Scanning Speed](scanning-speed.html)
- [Color Coding](color-coding.html)
- [Interlaced Scanning](interlaced-scanning.html)
- [Gray Scale Image and Extracted Line Profile](gray-scale-image-and-extracted-line-profile.html)
- [Active Image](active-image.html)
- [Video Levels](video-levels.html)

Parent topic:

Oscilloscopes Fundamentals

<!--NI_TOPIC bundle=ni-reconfigurable-oscilloscopes path=video-levels.html language=enus -->
## TOPIC 00085: Video Levels

- bundle_id: `ni-reconfigurable-oscilloscopes`
- source_path: `video-levels.html`
- source_url: https://docs-be.ni.com/bundle/ni-reconfigurable-oscilloscopes/raw/resource/enus/video-levels.html
- document_id: `ni-reconfigurable-oscilloscopes`
- page_type: `leaf`
- content_type: `concept`
- source_description: The video levels define the levels and ranges for the different parts of the video signal. The unit used to define video levels is the IRE (Institute of Radio Engineers). The blanking level refers to 0 IRE and the white level refers to +100 IRE. The blanking level, which is the reference level for t

### Video Levels

The video levels define the levels and ranges for the different parts of the video signal. The
 unit used to define video levels is the IRE (Institute of Radio Engineers). The blanking
 level refers to 0 IRE and the white level refers to +100 IRE. The blanking level, which
 is the reference level for the video signal (usually 0 V), is different from the black
 level if a setup is applied to the signal as shown in the following figure:

[IMAGE alt='image' src='GUID-7DC387DD-CFE5-4605-962C-E247A51DD154-a5.gif']

For NTSC, a setup of 7.5 IRE is usually applied, moving the black level to +7.5 IRE. For PAL and
 SECAM, the black level is aligned with the blanking level at 0 IRE.

The following table shows the different video levels depending on the video format:

| Video Format | Sync Level | Blanking Level | Black Level | White Level | Peak Level | Burst Amplitude |
| --- | --- | --- | --- | --- | --- | --- |
| NTSC | –40 IRE | 0 IRE | +7.5 IRE | +100 IRE | +120 IRE | 20.0 IRE |
| PAL | –43 IRE | 0 IRE | 0 IRE | +100 IRE | +133 IRE | 21.5 IRE |
| SECAM | –43 IRE | 0 IRE | 0 IRE | +100 IRE | +130 IRE | N/A |

The analog composite video signal is defined as a voltage source with an output impedance of
 75 Ω. The sync-to-white level is normally 1 V<sub>pk-pk</sub> when loaded with a 75 Ω
 resistance. Therefore, the unloaded signal is nominally 2 V<sub>pk-pk</sub>.

Parent topic:

Video Fundamentals

<!--NI_TOPIC bundle=ni-reconfigurable-oscilloscopes path=window-triggers.html language=enus -->
## TOPIC 00086: Window Triggers

- bundle_id: `ni-reconfigurable-oscilloscopes`
- source_path: `window-triggers.html`
- source_url: https://docs-be.ni.com/bundle/ni-reconfigurable-oscilloscopes/raw/resource/enus/window-triggers.html
- document_id: `ni-reconfigurable-oscilloscopes`
- page_type: `leaf`
- content_type: `concept`
- source_description: A window trigger occurs when a signal either enters or leaves a window you specify with the window mode parameters in the Configure Trigger Window function. Window triggering is possible on all analog trigger channels, such as 0, 1, or the external trigger input.The following figure shows an enterin

### Window Triggers

A window trigger occurs when a signal either enters or leaves a window you specify with the
 window mode parameters in the Configure Trigger Window function. Window
 triggering is possible on all analog trigger channels, such as 0, 1, or the external
 trigger input.

The following figure shows an entering window trigger.:

[IMAGE alt='image' src='GUID-9BE50463-293B-4B4B-A632-1F595E334E4A-a5.gif']

The following figure shows a leaving window trigger:

[IMAGE alt='image' src='GUID-43DB27D1-0908-4EF6-8482-8B44182B8E0F-a5.gif']

Parent topic:

Triggering
