# NI DOCUMENT BUNDLE: digital-audio-acquisition-generation

<!--NI_BUNDLE_CHUNK bundle=digital-audio-acquisition-generation start=1 end=22 -->
<!--NI_TOPIC bundle=digital-audio-acquisition-generation path=acquire-generate-signal-different-interface.html language=enus -->
## TOPIC 00001: Acquiring and Generating PCM Signals of Different Serial Audio Interface Types

- bundle_id: `digital-audio-acquisition-generation`
- source_path: `acquire-generate-signal-different-interface.html`
- source_url: https://docs-be.ni.com/bundle/digital-audio-acquisition-generation/raw/resource/enus/acquire-generate-signal-different-interface.html
- document_id: `digital-audio-acquisition-generation`
- page_type: `leaf`
- content_type: `reference`
- source_description: You must complete specific API configurations to acquire and generate PCM signals of each serial audio interface type that has unique timing logic. You can use the following example API configurations or modify API controls based on your test needs. Introduced in Digital Audio Acquisition and Genera

Acquiring and Generating PCM Signals of
 Different Serial Audio Interface Types

You must complete specific API configurations to acquire and generate PCM signals of
 each serial audio interface type that has unique timing logic. You can use the following
 example API configurations or modify API controls based on your test needs.

Introduced in Digital Audio Acquisition and Generation Toolkit 2023 Q3

#### I2S

| API Control | Value |  |
| --- | --- | --- |
| PCM Data Configuration | Frame Sync Edge for Channel 0 | Falling |
| Channel Count Per Frame | 2 |  |
| Channel Length | 32 |  |
| Bit Depth | 24 |  |
| Channel 0 Offset | 1 |  |
| Endianness | MSB First |  |
| Data Justification | Left Justified |  |
| Frame Sync Clock Control | Frame Length | 64 |
| Frame Sync Pulse Width | 32 |  |
| Bit Clock Edge Sync | Falling |  |

The following figure demonstrates the timing logic of I2S when you configure
 API controls as the previous table shows.

[IMAGE alt='Timing Logic of I2S' src='GUID-0ED2F531-F9A1-4EBC-8E45-D945AEE6F94B-a5.svg']

#### Left-Justified

| API Control | Value |  |
| --- | --- | --- |
| PCM Data Configuration | Frame Sync Edge for Channel 0 | Rising |
| Channel Count Per Frame | 2 |  |
| Channel Length | 32 |  |
| Bit Depth | 24 |  |
| Channel 0 Offset | 0 |  |
| Endianness | MSB First |  |
| Data Justification | Left Justified |  |
| Frame Sync Clock Control | Frame Length | 64 |
| Frame Sync Pulse Width | 32 |  |
| Bit Clock Edge Sync | Falling |  |

The following figure demonstrates the timing logic of left-justified when you
 configure API controls as the previous table shows.

[IMAGE alt='Timing Logic of Left-Justified' src='GUID-A78EF0F6-85F9-4988-B3EE-0FF9F3510230-a5.svg']

#### Right-Justified

| API Control | Value |  |
| --- | --- | --- |
| PCM Data Configuration | Frame Sync Edge for Channel 0 | Rising |
| Channel Count Per Frame | 2 |  |
| Channel Length | 32 |  |
| Bit Depth | 24 |  |
| Channel 0 Offset | 0 |  |
| Endianness | MSB First |  |
| Data Justification | Right Justified |  |
| Frame Sync Clock Control | Frame Length | 64 |
| Frame Sync Pulse Width | 32 |  |
| Bit Clock Edge Sync | Falling |  |

The following figure demonstrates the timing logic of right-justified when
 you configure API controls as the previous table shows.

[IMAGE alt='Timing Logic of Right-Justified' src='GUID-8A3521AA-2F64-411B-B3AE-2A89E9748DCF-a5.svg']

#### 4-Channel TDM

| API Control | Value |  |
| --- | --- | --- |
| PCM Data Configuration | Frame Sync Edge for Channel 0 | Rising |
| Channel Count Per Frame | 4 |  |
| Channel Length | 32 |  |
| Bit Depth | 24 |  |
| Channel 0 Offset | 0 |  |
| Endianness | MSB First |  |
| Data Justification | Left Justified |  |
| Frame Sync Clock Control | Frame Length | 128 |
| Frame Sync Pulse Width | 64 |  |
| Bit Clock Edge Sync | Falling |  |

The following figure demonstrates the timing logic of 4-Channel TDM when you
 configure API controls as the previous table shows.

[IMAGE alt='Timing Logic of 4-Channel TDM' src='GUID-D81DA4FE-7437-4B1A-BB24-ACF5575BF834-a5.svg']

#### 6-Channel TDM

| API Control | Value |  |
| --- | --- | --- |
| PCM Data Configuration | Frame Sync Edge for Channel 0 | Falling |
| Channel Count Per Frame | 6 |  |
| Channel Length | 32 |  |
| Bit Depth | 32 |  |
| Channel 0 Offset | 0 |  |
| Endianness | MSB First |  |
| Data Justification | Left Justified |  |
| Frame Sync Clock Control | Frame Length | 192 |
| Frame Sync Pulse Width | 96 |  |
| Bit Clock Edge Sync | Falling |  |

#### 8-Channel TDM

| API Control | Value |  |
| --- | --- | --- |
| PCM Data Configuration | Frame Sync Edge for Channel 0 | Falling |
| Channel Count Per Frame | 8 |  |
| Channel Length | 32 |  |
| Bit Depth | 24 |  |
| Channel 0 Offset | 0 |  |
| Endianness | MSB First |  |
| Data Justification | Left Justified |  |
| Frame Sync Clock Control | Frame Length | 256 |
| Frame Sync Pulse Width | 128 |  |
| Bit Clock Edge Sync | Falling |  |

#### S/PDIF

| API Control | Value |  |
| --- | --- | --- |
| PCM Data Configuration | Frame Sync Edge for Channel 0 | Depending on test needs |
| Channel Count Per Frame | Depending on test needs |  |
| Channel Length | Depending on test needs |  |
| Bit Depth | 16 |  |
| Channel 0 Offset | 4 |  |
| Endianness | MSB First |  |
| Data Justification | Left Justified |  |
| Frame Sync Clock Control | Frame Length | Depending on test needs |
| Frame Sync Pulse Width | Depending on test needs |  |
| Bit Clock Edge Sync | Depending on test needs |  |

The following figure demonstrates the timing logic of S/PDIF when you
 configure API controls as the previous table shows.

[IMAGE alt='Timing Logic of S/PDIF' src='GUID-BEA063A3-CAB4-4AE5-BC43-6AB94F92D6B3-a5.svg']

If you set Channel 0 Offset to 0 and Bit
 Depth to 24, the timing logic of S/PDIF changes as the following
 figure shows.

[IMAGE alt='Timing Logic of S/PDIF' src='GUID-E1F472B2-832D-46D7-BF1E-710AD919FA7F-a5.svg']

Note

Bit Clock rate

Clock Mode

frequency

gain

phase

microphone sensitivity

Related reference:

- Digital Audio Acquisition and Generation Toolkit 2023 Q3 New Features and Changes

<!--NI_TOPIC bundle=digital-audio-acquisition-generation path=changes.html language=enus -->
## TOPIC 00002: New Features and Changes

- bundle_id: `digital-audio-acquisition-generation`
- source_path: `changes.html`
- source_url: https://docs-be.ni.com/bundle/digital-audio-acquisition-generation/raw/resource/enus/changes.html
- document_id: `digital-audio-acquisition-generation`
- page_type: `leaf`
- content_type: `concept`
- source_description: Learn about updates—including new features and behavior changes—introduced in each version of the Digital Audio Acquisition and Generation Toolkit. Digital Audio Acquisition and Generation Toolkit 2023 Q3 New Features and Changes Introduces PCM acquisition and generation APIs which you can configure

New Features and Changes

Learn about updates—including new features and behavior changes—introduced in each
 version of the Digital Audio Acquisition and Generation Toolkit.

#### Digital Audio Acquisition and Generation Toolkit
 2023 Q3 New Features and Changes

- Introduces PCM acquisition and generation APIs which you can configure to acquire and
 generate PCM signals of different serial audio interface types. I2S acquisition and
 generation APIs are obsolete as of Digital Audio Acquisition and Generation Toolkit 2023 Q3.
- Allows the same hardware device to synchronously acquire and generate PCM signals of the
 same or different serial audio interface types.
- Increases the maximum number of timing engines to 4 when synchronously acquiring and
 generating or only acquiring PCM signals with the PXIe-7820/7821 . The maximum number of timing engines for PCM generation is 2 whenever synchronously
 acquiring and generating or only generating PCM signals.
- Changes the toolkit name from LabVIEW PDM Acquisition Toolkit to Digital Audio Acquisition and Generation Toolkit .
- Adds support for LabVIEW 2022 and removes support for LabVIEW 2018 SP1 Patch.

Related reference:

- Acquiring and Generating PCM Signals of Different Serial Audio Interface Types
- PCM Bus Specifications

#### Digital Audio Acquisition and Generation Toolkit
 2022 Q4 New Features and Changes

- Adds support for 64-bit LabVIEW 2018 SP1 Patch, 2019, 2020, and 2021.
- Provides C# APIs and examples.

Related reference:

- Finding the Examples

#### Digital Audio Acquisition and Generation Toolkit
 2021 Q4 New Features and Changes

- Adds support for acquiring, converting, and generating I2S signals.

Related reference:

- PCM Bus Specifications

#### Digital Audio Acquisition and Generation Toolkit
 2021 Q2 New Features and Changes

- Adds support for generating PDM signals.
- Adds support for different rates and decimation factors.
- Adds support for PXIe-7821 and USB-7845/7846 .

Related reference:

- PDM Acquisition and Generation Specifications for PXIe-7820/7821
- PDM Acquisition and Generation Specifications for USB-7845/7846
- Function Generator Specifications
- Modulator Specifications
- Linear Chirp Specifications
- Logarithmic Chirp Specifications

<!--NI_TOPIC bundle=digital-audio-acquisition-generation path=component.html language=enus -->
## TOPIC 00003: Digital Audio Acquisition and Generation System Components

- bundle_id: `digital-audio-acquisition-generation`
- source_path: `component.html`
- source_url: https://docs-be.ni.com/bundle/digital-audio-acquisition-generation/raw/resource/enus/component.html
- document_id: `digital-audio-acquisition-generation`
- page_type: `leaf`
- content_type: `concept`
- source_description: A digital audio acquisition and generation system is a system of hardware and software that you configure to acquire and generate digital audio signals. Use the following table of typical system components as a starting point for building your digital audio acquisition and generation system. Compone

Digital Audio Acquisition and Generation
 System Components

A digital audio acquisition and generation system is a system of hardware and software
 that you configure to acquire and generate digital audio signals. Use the following table of
 typical system components as a starting point for building your digital audio acquisition
 and generation system.

| Component | Note |
| --- | --- |
| Digital Audio Acquisition and Generation Toolkit | Install Digital Audio Acquisition and Generation Toolkit using NI Package Manager. |
| Use one or multiple hardware components in the following list: PXIe-7820 PXIe-7821 USB-7845 USB-7846 | N/A |
| NI R Series Multifunction RIO 20.0 or a later version | NI recommends using the latest version. |

<!--NI_TOPIC bundle=digital-audio-acquisition-generation path=connector-pin-pxie-7820-7821-pcm-acq-gen.html language=enus -->
## TOPIC 00004: Connector Pin Assignments for PXIe-7820/7821 PCM Acquisition or Generation

- bundle_id: `digital-audio-acquisition-generation`
- source_path: `connector-pin-pxie-7820-7821-pcm-acq-gen.html`
- source_url: https://docs-be.ni.com/bundle/digital-audio-acquisition-generation/raw/resource/enus/connector-pin-pxie-7820-7821-pcm-acq-gen.html
- document_id: `digital-audio-acquisition-generation`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the following connector pin assignments when you configure pin functions for PCM acquisition or generation using the PXIe-7820/7821. Connector 0 Pin Assignments Terminal Function Assignment 1 DIO31 PCM IO 15 2 GND GND 3 DIO29 Frame sync clock 3 4 GND GND 5 DIO27 GPIO 6 6 GND GND 7 DIO25 PCM IO 1

Connector Pin Assignments for PXIe-7820/7821 PCM Acquisition or Generation

Use the following connector pin assignments when you configure pin functions for PCM
 acquisition or generation using the PXIe-7820/7821.

#### Connector 0 Pin Assignments

| Terminal | Function | Assignment |
| --- | --- | --- |
| 1 | DIO31 | PCM IO 15 |
| 2 | GND | GND |
| 3 | DIO29 | Frame sync clock 3 |
| 4 | GND | GND |
| 5 | DIO27 | GPIO 6 |
| 6 | GND | GND |
| 7 | DIO25 | PCM IO 13 |
| 8 | GND | GND |
| 9 | DIO23 | PCM IO 11 |
| 10 | GND | GND |
| 11 | DIO21 | PCM IO 9 |
| 12 | GND | GND |
| 13 | DIO19 | Bit clock 3 |
| 14 | GND | GND |
| 15 | DIO17 | GPIO 5 |
| 16 | GND | GND |
| 17 | DIO15 | GPIO 3 |
| 18 | GND | GND |
| 19 | DIO13 | Bit clock 1 |
| 20 | GND | GND |
| 21 | DIO11 | PCM IO 7 |
| 22 | GND | GND |
| 23 | DIO9 | PCM IO 5 |
| 24 | GND | GND |
| 25 | DIO7 | PCM IO 3 |
| 26 | GND | GND |
| 27 | DIO5 | Frame sync clock 0 |
| 28 | GND | GND |
| 29 | DIO3 | GPIO 1 |
| 30 | GND | GND |
| 31 | DIO1 | PCM IO 1 |
| 32 | GND | GND |
| 33 | GND | GND |
| 34 | GND | GND |
| 35 | DIO30 | Bit clock 2 |
| 36 | GND | GND |
| 37 | DIO28 | PCM IO 14 |
| 38 | GND | GND |
| 39 | DIO26 | PCM IO 12 |
| 40 | GND | GND |
| 41 | DIO24 | PCM IO 10 |
| 42 | GND | GND |
| 43 | DIO22 | GPIO 7 |
| 44 | GND | GND |
| 45 | DIO20 | Frame sync clock 2 |
| 46 | GND | GND |
| 47 | DIO18 | GPIO 4 |
| 48 | GND | GND |
| 49 | DIO16 | PCM IO 8 |
| 50 | GND | GND |
| 51 | DIO14 | PCM IO 6 |
| 52 | GND | GND |
| 53 | DIO12 | GPIO 2 |
| 54 | GND | GND |
| 55 | DIO10 | Frame sync clock 1 |
| 56 | GND | GND |
| 57 | DIO8 | GPIO 0 |
| 58 | GND | GND |
| 59 | DIO6 | PCM IO 4 |
| 60 | GND | GND |
| 61 | DIO4 | PCM IO 2 |
| 62 | GND | GND |
| 63 | DIO2 | PCM IO 0 |
| 64 | GND | GND |
| 65 | DIO0 | Bit clock 0 |
| 66 | GND | GND |
| 67 | External Clock x (an input only, x is the connector number) | Reserved |
| 68 | GND | GND |

#### Connector 1 Pin Assignments

| Terminal | Function | Assignment |
| --- | --- | --- |
| 1 | DIO31 | PCM IO 31 |
| 2 | GND | GND |
| 3 | DIO29 | Frame sync clock 7 |
| 4 | GND | GND |
| 5 | DIO27 | GPIO 14 |
| 6 | GND | GND |
| 7 | DIO25 | PCM IO 29 |
| 8 | GND | GND |
| 9 | DIO23 | PCM IO 27 |
| 10 | GND | GND |
| 11 | DIO21 | PCM IO 25 |
| 12 | GND | GND |
| 13 | DIO19 | Bit clock 7 |
| 14 | GND | GND |
| 15 | DIO17 | GPIO 13 |
| 16 | GND | GND |
| 17 | DIO15 | GPIO 11 |
| 18 | GND | GND |
| 19 | DIO13 | Bit clock 5 |
| 20 | GND | GND |
| 21 | DIO11 | PCM IO 23 |
| 22 | GND | GND |
| 23 | DIO9 | PCM IO 21 |
| 24 | GND | GND |
| 25 | DIO7 | PCM IO 19 |
| 26 | GND | GND |
| 27 | DIO5 | Frame sync clock 4 |
| 28 | GND | GND |
| 29 | DIO3 | GPIO 9 |
| 30 | GND | GND |
| 31 | DIO1 | PCM IO 17 |
| 32 | GND | GND |
| 33 | GND | GND |
| 34 | GND | GND |
| 35 | DIO30 | Bit clock 6 |
| 36 | GND | GND |
| 37 | DIO28 | PCM IO 30 |
| 38 | GND | GND |
| 39 | DIO26 | PCM IO 28 |
| 40 | GND | GND |
| 41 | DIO24 | PCM IO 26 |
| 42 | GND | GND |
| 43 | DIO22 | GPIO 15 |
| 44 | GND | GND |
| 45 | DIO20 | Frame sync clock 6 |
| 46 | GND | GND |
| 47 | DIO18 | GPIO 12 |
| 48 | GND | GND |
| 49 | DIO16 | PCM IO 24 |
| 50 | GND | GND |
| 51 | DIO14 | PCM IO 22 |
| 52 | GND | GND |
| 53 | DIO12 | GPIO 10 |
| 54 | GND | GND |
| 55 | DIO10 | Frame sync clock 5 |
| 56 | GND | GND |
| 57 | DIO8 | GPIO 8 |
| 58 | GND | GND |
| 59 | DIO6 | PCM IO 20 |
| 60 | GND | GND |
| 61 | DIO4 | PCM IO 18 |
| 62 | GND | GND |
| 63 | DIO2 | PCM IO 16 |
| 64 | GND | GND |
| 65 | DIO0 | Bit clock 4 |
| 66 | GND | GND |
| 67 | External Clock x (an input only, x is the connector number) | Reserved |
| 68 | GND | GND |

Parent topic:

PCM Bus Specifications

<!--NI_TOPIC bundle=digital-audio-acquisition-generation path=connector-pin-usb-7845-7846-pcm-acq-gen.html language=enus -->
## TOPIC 00005: Connector Pin Assignments for USB-7845/7846 PCM Acquisition or Generation

- bundle_id: `digital-audio-acquisition-generation`
- source_path: `connector-pin-usb-7845-7846-pcm-acq-gen.html`
- source_url: https://docs-be.ni.com/bundle/digital-audio-acquisition-generation/raw/resource/enus/connector-pin-usb-7845-7846-pcm-acq-gen.html
- document_id: `digital-audio-acquisition-generation`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the following connector pin assignments when you configure pin functions for PCM acquisition or generation using the USB-7845/7846. Connector 0 Pin Assignments Terminal Function Assignment 1 DIO31 PCM IO 15 2 GND GND 3 DIO29 Frame sync clock 3 4 GND GND 5 DIO27 GPIO 6 6 GND GND 7 DIO25 PCM IO 13

Connector Pin Assignments for USB-7845/7846 PCM Acquisition or Generation

Use the following connector pin assignments when you configure pin functions for PCM
 acquisition or generation using the USB-7845/7846.

#### Connector 0 Pin Assignments

| Terminal | Function | Assignment |
| --- | --- | --- |
| 1 | DIO31 | PCM IO 15 |
| 2 | GND | GND |
| 3 | DIO29 | Frame sync clock 3 |
| 4 | GND | GND |
| 5 | DIO27 | GPIO 6 |
| 6 | GND | GND |
| 7 | DIO25 | PCM IO 13 |
| 8 | GND | GND |
| 9 | DIO23 | PCM IO 11 |
| 10 | GND | GND |
| 11 | DIO21 | PCM IO 9 |
| 12 | GND | GND |
| 13 | DIO19 | Bit clock 3 |
| 14 | GND | GND |
| 15 | DIO17 | GPIO 5 |
| 16 | GND | GND |
| 17 | DIO15 | GPIO 3 |
| 18 | GND | GND |
| 19 | DIO13 | Bit clock 1 |
| 20 | GND | GND |
| 21 | DIO11 | PCM IO 7 |
| 22 | GND | GND |
| 23 | DIO9 | PCM IO 5 |
| 24 | GND | GND |
| 25 | DIO7 | PCM IO 3 |
| 26 | GND | GND |
| 27 | DIO5 | Frame sync clock 0 |
| 28 | GND | GND |
| 29 | DIO3 | GPIO 1 |
| 30 | GND | GND |
| 31 | DIO1 | PCM IO 1 |
| 32 | GND | GND |
| 33 | GND | GND |
| 34 | GND | GND |
| 35 | DIO30 | Bit clock 2 |
| 36 | GND | GND |
| 37 | DIO28 | PCM IO 14 |
| 38 | GND | GND |
| 39 | DIO26 | PCM IO 12 |
| 40 | GND | GND |
| 41 | DIO24 | PCM IO 10 |
| 42 | GND | GND |
| 43 | DIO22 | GPIO 7 |
| 44 | GND | GND |
| 45 | DIO20 | Frame sync clock 2 |
| 46 | GND | GND |
| 47 | DIO18 | GPIO 4 |
| 48 | GND | GND |
| 49 | DIO16 | PCM IO 8 |
| 50 | GND | GND |
| 51 | DIO14 | PCM IO 6 |
| 52 | GND | GND |
| 53 | DIO12 | GPIO 2 |
| 54 | GND | GND |
| 55 | DIO10 | Frame sync clock 1 |
| 56 | GND | GND |
| 57 | DIO8 | GPIO 0 |
| 58 | GND | GND |
| 59 | DIO6 | PCM IO 4 |
| 60 | GND | GND |
| 61 | DIO4 | PCM IO 2 |
| 62 | GND | GND |
| 63 | DIO2 | PCM IO 0 |
| 64 | GND | GND |
| 65 | DIO0 | Bit clock 0 |
| 66 | GND | GND |
| 67 | External Clock x (an input only, x is the connector number) | Reserved |
| 68 | GND | GND |

Parent topic:

PCM Bus Specifications

<!--NI_TOPIC bundle=digital-audio-acquisition-generation path=digital-audio-acquisition-generation.html language=enus -->
## TOPIC 00006: What Is Digital Audio Acquisition and Generation Toolkit and Who Is It For?

- bundle_id: `digital-audio-acquisition-generation`
- source_path: `digital-audio-acquisition-generation.html`
- source_url: https://docs-be.ni.com/bundle/digital-audio-acquisition-generation/raw/resource/enus/digital-audio-acquisition-generation.html
- document_id: `digital-audio-acquisition-generation`
- page_type: `leaf`
- content_type: `reference`
- source_description: The Digital Audio Acquisition and Generation Toolkit is a software add-on that helps production test engineers acquire and generate pulse-density modulation (PDM) and pulse-code modulation (PCM) signals to assess the performance of digital audio devices. Use PDM APIs to acquire and generate PDM sign

What Is Digital Audio Acquisition and Generation Toolkit and Who Is It For?

The Digital Audio Acquisition and Generation Toolkit is a software add-on that helps
 production test engineers acquire and generate pulse-density modulation (PDM) and pulse-code
 modulation (PCM) signals to assess the performance of digital audio devices. Use PDM APIs to
 acquire and generate PDM signals or configure PCM APIs to acquire and generate PCM signals of
 different serial audio interface types, such as inter-IC sound (I2S or I²S), left-justified,
 right-justified, time-division multiplexing (TDM), and Sony/Philips Digital Interface Format
 (S/PDIF).

#### Key Features

The features that set the Digital Audio Acquisition and Generation Toolkit apart.

- Acquiring PDM and PCM signals and converting signals to audio waveforms for
 testing.
- Generating PDM and PCM signals for device performance assessment.
- Supporting different rates and decimation factors.
- Supporting different PCM serial audio interface types.
- Synchronously acquiring and generating PCM signals with the PXIe-7820/7821 .

#### Basic Concepts

Understand the following basic concepts before using the Digital Audio Acquisition and Generation Toolkit.

Task

task

Bank

bank

Data Line

data line

Refer to the *PDM Acquisition and Generation Specifications* and *PCM
 Bus Specifications* for the supported number of channels and data lines
 and for the layout of banks to channels.

The Digital Audio Acquisition and Generation Toolkit supports multiple concurrent tasks with
 the following limitations:

- The same channel cannot be in more than one task at the same time.
- Channels from the same bank cannot be in different tasks at the same time.
- The number of concurrent tasks is limited to the number of timing engines
 supported.
- (PDM only) The same hardware device cannot support an input task and an output
 task at the same time.

Related reference:

- PDM Acquisition and Generation Specifications
- PCM Bus Specifications

<!--NI_TOPIC bundle=digital-audio-acquisition-generation path=distort-signal-bit-shift.html language=enus -->
## TOPIC 00007: What Should I Do If Signals Are Distorted with a Bit Shift?

- bundle_id: `digital-audio-acquisition-generation`
- source_path: `distort-signal-bit-shift.html`
- source_url: https://docs-be.ni.com/bundle/digital-audio-acquisition-generation/raw/resource/enus/distort-signal-bit-shift.html
- document_id: `digital-audio-acquisition-generation`
- page_type: `leaf`
- content_type: `reference`
- source_description: SymptomDuring PCM acquisition, when the receiver (FPGA) in master mode generates the bit clock and the frame sync clock, the signals that the receiver acquires are distorted or have incorrect amplitude with a bit shift, as the following figures show. This issue also occurs during PCM generation when

What Should I Do If Signals Are Distorted
 with a Bit Shift?

#### Symptom

During PCM acquisition, when the receiver (FPGA) in master mode
 generates the bit clock and the frame sync clock, the signals that the receiver
 acquires are distorted or have incorrect amplitude with a bit shift, as the
 following figures show. This issue also occurs during PCM generation when the
 receiver (DUT) in master mode generates clocks.

Figure 4.

[IMAGE alt='Distorted Signal with a Bit Shift (Endianness Set to LSB First)' src='GUID-74B4E19C-B1CB-43E9-A6E7-8B95AB8326DE-a5.svg']

Figure 5.

[IMAGE alt='Distorted Signal with a Bit Shift (Endianness Set to MSB First)' src='GUID-759A09F1-2165-4E10-981E-6F0FBAAE12EF-a5.svg']

Figure 6.

[IMAGE alt='Bit-Shifted Signal with Incorrect Amplitude' src='GUID-A8CB2B30-B601-4B09-AE32-FED581B282AC-a5.svg']

Note

100 ns

#### Root Cause

Cables
 cause propagation delays.

#### Solution

To compensate
 for cable propagation delays during PCM acquisition, set Latch
 Delay in the PCM input task to delay data latching by the FPGA. NI
 recommends a 50 ns delay at 12 MHz bit clock for 1 m
 cables.

To compensate for cable propagation delays during PCM generation, set
 Generation Timing Offset to advance data generation. NI
 recommends a 50 ns generation offset at 12 MHz bit
 clock for 1 m cables.

The following figure shows a correct signal after you
 set Latch Delay or Generation Timing
 Offset.

[IMAGE alt='Correct Signal' src='GUID-B38B47C1-7127-4FF7-8C1D-516E1F4A2F09-a5.svg']

Parent topic:

Troubleshooting

<!--NI_TOPIC bundle=digital-audio-acquisition-generation path=dma-fifo-overflow.html language=enus -->
## TOPIC 00008: What Should I Do If I Encounter DMA FIFO Overflow?

- bundle_id: `digital-audio-acquisition-generation`
- source_path: `dma-fifo-overflow.html`
- source_url: https://docs-be.ni.com/bundle/digital-audio-acquisition-generation/raw/resource/enus/dma-fifo-overflow.html
- document_id: `digital-audio-acquisition-generation`
- page_type: `leaf`
- content_type: `reference`
- source_description: SymptomI receive a "DMA FIFO overflow" error message when using the USB-7845/7846 to acquire PCM signals. Root CauseThe USB-7845/7846 has bus speed and bandwidth limitations. SolutionSet the bit clock rate and the number of channels within limits. Use the following formulas to calculate the maximum

What Should I Do If I Encounter DMA FIFO
 Overflow?

#### Symptom

I receive a "DMA FIFO overflow" error message when using the USB-7845/7846 to acquire PCM signals.

#### Root Cause

The USB-7845/7846 has bus speed and bandwidth
 limitations.

#### Solution

Set the bit
 clock rate and the number of channels within limits. Use the following formulas to
 calculate the maximum bit clock rate and number of channels that apply in most
 cases:

N

Fs

Bit clock rate

Frame
 length

N

Fs

The previous formulas use a rough
 estimate of the maximum DMA throughput from the USB-7845/7846 to the host system. To avoid overflow, you
 must also consider the number of samples to read for each channel and other system
 configurations that affect the DMA throughput. For example, if you want more samples
 at higher sampling rates, NI recommends you configure fewer channels per
 task.

Parent topic:

Troubleshooting

<!--NI_TOPIC bundle=digital-audio-acquisition-generation path=example.html language=enus -->
## TOPIC 00009: Finding the Examples

- bundle_id: `digital-audio-acquisition-generation`
- source_path: `example.html`
- source_url: https://docs-be.ni.com/bundle/digital-audio-acquisition-generation/raw/resource/enus/example.html
- document_id: `digital-audio-acquisition-generation`
- page_type: `leaf`
- content_type: `reference`
- source_description: Acquire or generate different types of digital audio signals by running the LabVIEW and C# examples that the Digital Audio Acquisition and Generation Toolkit provides. LabVIEW examples are in the following directory: LabVIEW version\examples\Digital Audio Acquisition and Generation Toolkit. C# dynam

Finding the Examples

Acquire or generate different types of digital audio signals by running the LabVIEW and
 C# examples that the Digital Audio Acquisition and Generation Toolkit provides.

LabVIEW examples are in the following directory: LabVIEW
 version\examples\Digital Audio Acquisition and Generation
 Toolkit.

- DLL: C:\Program Files\National Instruments\PDM Acquisition
 Toolkit\NationalInstruments.PDMToolkit.Task.dll
- Examples: C:\Users\Public\Documents\National Instruments\PDM
 Acquisition Toolkit\Examples\DotNET

You can use C# DLL and examples to acquire and generate only PDM and I2S signals.

Note

Digital Audio Acquisition and Generation Toolkit

Related reference:

- Digital Audio Acquisition and Generation Toolkit 2022 Q4 New Features and Changes

<!--NI_TOPIC bundle=digital-audio-acquisition-generation path=pcm-specs.html language=enus -->
## TOPIC 00010: PCM Bus Specifications

- bundle_id: `digital-audio-acquisition-generation`
- source_path: `pcm-specs.html`
- source_url: https://docs-be.ni.com/bundle/digital-audio-acquisition-generation/raw/resource/enus/pcm-specs.html
- document_id: `digital-audio-acquisition-generation`
- page_type: `leaf`
- content_type: `reference`
- source_description: Refer to these specifications when using the Digital Audio Acquisition and Generation Toolkit with the PXIe-7820/7821 and USB-7845/7846 to acquire and generate pulse-code modulation (PCM) signals. I2S bus specifications are introduced in Digital Audio Acquisition and Generation Toolkit 2021 Q4 and u

PCM Bus Specifications

Refer to these specifications when using the Digital Audio Acquisition and Generation Toolkit
 with the PXIe-7820/7821 and USB-7845/7846
 to acquire and generate pulse-code modulation (PCM) signals.

Note

Digital Audio Acquisition and Generation Toolkit

Digital Audio Acquisition and Generation Toolkit

Related reference:

- Digital Audio Acquisition and Generation Toolkit 2021 Q4 New Features and Changes
- Digital Audio Acquisition and Generation Toolkit 2023 Q3 New Features and Changes

<!--NI_TOPIC bundle=digital-audio-acquisition-generation path=specs-function-generator.html language=enus -->
## TOPIC 00011: Function Generator Specifications

- bundle_id: `digital-audio-acquisition-generation`
- source_path: `specs-function-generator.html`
- source_url: https://docs-be.ni.com/bundle/digital-audio-acquisition-generation/raw/resource/enus/specs-function-generator.html
- document_id: `digital-audio-acquisition-generation`
- page_type: `leaf`
- content_type: `reference`
- source_description: Refer to the following specifications and examples when generating signals using the Digital Audio Acquisition and Generation Toolkit. Introduced in Digital Audio Acquisition and Generation Toolkit 2021 Q2 Dynamic Range and Distortion Specifications Measurement Conditions PDM rate 3.072 MHz Modulato

Function Generator Specifications

Refer to the following specifications and examples when generating signals using the
 Digital Audio Acquisition and Generation Toolkit.

Introduced in Digital Audio Acquisition and Generation Toolkit 2021 Q2

Parent topic:

PDM Acquisition and Generation Specifications

Related reference:

- Digital Audio Acquisition and Generation Toolkit 2021 Q2 New Features and Changes

#### Dynamic Range and Distortion
 Specifications

| Measurement Conditions PDM rate3.072 MHz Modulator bandwidth20 kHz Test signal1 kHz sine wave Measurement bandwidthModulator bandwidth |  |
| --- | --- |
| Measurement Conditions |  |
| PDM rate | 3.072 MHz |
| Modulator bandwidth | 20 kHz |
| Test signal | 1 kHz sine wave |
| Measurement bandwidth | Modulator bandwidth |
| SINAD, where test amplitude is 0.5 relative digital full scale Fourth order modulator>98 dB Fifth order modulator>124 dB |  |
| SINAD, where test amplitude is 0.5 relative digital full scale |  |
| Fourth order modulator | >98 dB |
| Fifth order modulator | >124 dB |
| Dynamic Range, where test amplitude is 0.0005 relative digital full scale Fourth order modulator>100 dB Fifth order modulator>126 dB |  |
| Dynamic Range, where test amplitude is 0.0005 relative digital full scale |  |
| Fourth order modulator | >100 dB |
| Fifth order modulator | >126 dB |

#### Modulator Bandwidth

##### SINAD as a Function of Modulator
 Bandwidth

| Measurement Conditions PDM rate3.072 MHz Modulator bandwidth3 kHz to 46 kHz Test frequency1 kHz Test amplitude0.5 FS |  |
| --- | --- |
| Measurement Conditions |  |
| PDM rate | 3.072 MHz |
| Modulator bandwidth | 3 kHz to 46 kHz |
| Test frequency | 1 kHz |
| Test amplitude | 0.5 FS |

The following figure demonstrates the signal-to-noise and distortion ratio
 (SINAD) as a function of modulator bandwidth when the modulator order is 4
 and 5.

Figure 1.

[IMAGE alt='SINAD as Function of Modulator Bandwidth' src='GUID-642C1EBE-56C1-4597-87BE-AFE015663C60-a5.svg']

##### Modulator Flatness as a Function of
 Modulator Bandwidth

| Measurement Conditions PDM rate3.072 MHz Fourth Order Modulator Modulator bandwidth ≤40 kHzRipple DC to modulation bandwidth < ±0.004 dB Modulator bandwidth >40 kHz and ≤46 kHzRipple DC to modulation bandwidth < ±0.01 dB Fifth Order Modulator Modulator bandwidth ≤40 kHzRipple DC to modulation bandwidth < ±0.001 dB Modulator bandwidth >40 kHz and ≤46 kHzRipple DC to modulation bandwidth < ±0.002 dB |  |
| --- | --- |
| Measurement Conditions |  |
| PDM rate | 3.072 MHz |
| Fourth Order Modulator Modulator bandwidth ≤40 kHzRipple DC to modulation bandwidth < ±0.004 dB Modulator bandwidth >40 kHz and ≤46 kHzRipple DC to modulation bandwidth < ±0.01 dB |  |
| Fourth Order Modulator |  |
| Modulator bandwidth ≤40 kHz | Ripple DC to modulation bandwidth < ±0.004 dB |
| Modulator bandwidth >40 kHz and ≤46 kHz | Ripple DC to modulation bandwidth < ±0.01 dB |
| Fifth Order Modulator Modulator bandwidth ≤40 kHzRipple DC to modulation bandwidth < ±0.001 dB Modulator bandwidth >40 kHz and ≤46 kHzRipple DC to modulation bandwidth < ±0.002 dB |  |
| Fifth Order Modulator |  |
| Modulator bandwidth ≤40 kHz | Ripple DC to modulation bandwidth < ±0.001 dB |
| Modulator bandwidth >40 kHz and ≤46 kHz | Ripple DC to modulation bandwidth < ±0.002 dB |

#### Spectral Characteristics

| Measurement Conditions PDM rate3.072 MHz Modulator bandwidth20 kHz Test frequency1 kHz Test amplitude0.5 FS Spectral resolution10 Hz Window typeHanning Number of RMS averaging64 |  |
| --- | --- |
| Measurement Conditions |  |
| PDM rate | 3.072 MHz |
| Modulator bandwidth | 20 kHz |
| Test frequency | 1 kHz |
| Test amplitude | 0.5 FS |
| Spectral resolution | 10 Hz |
| Window type | Hanning |
| Number of RMS averaging | 64 |

The following figures demonstrate the averaged power spectrum when the modulator
 order is 4 and 5, respectively.

Figure 2.

[IMAGE alt='Averaged Power Spectrum for Fourth Order Modulator' src='GUID-992559D5-370C-42B0-A322-83D0501E0022-a5.svg']

Figure 3.

[IMAGE alt='Averaged Power Spectrum for Fifth Order Modulator' src='GUID-9497E710-DA8F-4F81-B557-69355A218930-a5.svg']

<!--NI_TOPIC bundle=digital-audio-acquisition-generation path=specs-linear-chirp.html language=enus -->
## TOPIC 00012: Linear Chirp Specifications

- bundle_id: `digital-audio-acquisition-generation`
- source_path: `specs-linear-chirp.html`
- source_url: https://docs-be.ni.com/bundle/digital-audio-acquisition-generation/raw/resource/enus/specs-linear-chirp.html
- document_id: `digital-audio-acquisition-generation`
- page_type: `leaf`
- content_type: `reference`
- source_description: Introduced in Digital Audio Acquisition and Generation Toolkit 2021 Q2 The following specifications apply to the Configure Chirp (N Ch) VI when configuring a linear chirp signal. Start frequency range 0 to PDM rate/2 Stop frequency range 0 to PDM rate/2 Pre-chirp duration range 0 to 2^32 − 1 PDM sam

Linear Chirp Specifications

Introduced in Digital Audio Acquisition and Generation Toolkit 2021 Q2

The following specifications apply to the Configure Chirp (N Ch) VI when
 configuring a linear chirp signal.

| Start frequency range | 0 to PDM rate/2 |
| --- | --- |
| Stop frequency range | 0 to PDM rate/2 |
| Pre-chirp duration range | 0 to 232 − 1 PDM samples, or approximately 23 minutes at PDM rate of 3.072 MHz |
| Chirp duration range | 0 to 232 − 1 − Pre-chirp duration samples |

The linear chirp rate range, in seconds, is defined by the following equation:

Linear chirp rate range

=

±

(

Stop freq - Start freq

)

/

Chirp duration

Refer to the following table for maximum chirp rates at different PDM rates.

| Maximum Linear Chirp Rate | PDM Rate = 600 kHz | PDM Rate = 800 kHz | PDM Rate = 2.4 MHz | PDM Rate = 3.072 MHz | PDM Rate = 4.8 MHz |
| --- | --- | --- | --- | --- | --- |
| Range | ±1.37 MHz/s | ±2.44 MHz/s | ±21.9 MHz/s | ±35.9 MHz/s | ±87.8 MHz/s |
| Minimum Time DC to PDM rate/2 | 7 ms | 5 ms | 2 ms | 2 ms | 1 ms |

Parent topic:

PDM Acquisition and Generation Specifications

Related reference:

- Digital Audio Acquisition and Generation Toolkit 2021 Q2 New Features and Changes

<!--NI_TOPIC bundle=digital-audio-acquisition-generation path=specs-logarithmic-chirp.html language=enus -->
## TOPIC 00013: Logarithmic Chirp Specifications

- bundle_id: `digital-audio-acquisition-generation`
- source_path: `specs-logarithmic-chirp.html`
- source_url: https://docs-be.ni.com/bundle/digital-audio-acquisition-generation/raw/resource/enus/specs-logarithmic-chirp.html
- document_id: `digital-audio-acquisition-generation`
- page_type: `leaf`
- content_type: `reference`
- source_description: Introduced in Digital Audio Acquisition and Generation Toolkit 2021 Q2 The following specifications apply to the Configure Chirp (N Ch) VI when configuring a logarithmic chirp signal. Start frequency range ≤PDM rate/32, corresponding to 96 kHz at 3.072 MHz PDM rate Stop frequency range ≤PDM rate/32

Logarithmic Chirp Specifications

Introduced in Digital Audio Acquisition and Generation Toolkit 2021 Q2

The following specifications apply to the Configure Chirp (N Ch) VI when
 configuring a logarithmic chirp signal.

| Start frequency range | ≤PDM rate/32, corresponding to 96 kHz at 3.072 MHz PDM rate |
| --- | --- |
| Stop frequency range | ≤PDM rate/32 |
| Pre-chirp duration range | 0 to 232 − 1 PDM samples, or approximately 23 minutes at PDM rate of 3.072 MHz |
| Chirp duration range | 0 to 232 − 1 − Pre-chirp duration samples |

The logarithmic chirp rate range, in seconds, is defined by the following equation:

Logarithmic chirp rate range

=

±

(

Stop freq / Start freq

)

/

Chirp duration

Refer to the following table for maximum chirp rates at different PDM rates.

| Maximum Logarithmic Chirp Rate | PDM Rate = 600 kHz | PDM Rate = 800 kHz | PDM Rate = 2.4 MHz | PDM Rate = 3.072 MHz | PDM Rate = 4.8 MHz |
| --- | --- | --- | --- | --- | --- |
| Range | ±105 octave/s | ±140 octave/s | ±422 octave/s | ±541 octave/s | ±845 octave/s |
| Minimum chirp time for 10 octaves | 95 ms | 71 ms | 24 ms | 18.5 ms | 12 ms |

Parent topic:

PDM Acquisition and Generation Specifications

Related reference:

- Digital Audio Acquisition and Generation Toolkit 2021 Q2 New Features and Changes

<!--NI_TOPIC bundle=digital-audio-acquisition-generation path=specs-modulator.html language=enus -->
## TOPIC 00014: Modulator Specifications

- bundle_id: `digital-audio-acquisition-generation`
- source_path: `specs-modulator.html`
- source_url: https://docs-be.ni.com/bundle/digital-audio-acquisition-generation/raw/resource/enus/specs-modulator.html
- document_id: `digital-audio-acquisition-generation`
- page_type: `leaf`
- content_type: `reference`
- source_description: Introduced in Digital Audio Acquisition and Generation Toolkit 2021 Q2 PDM modulator order 4 and 5. Use the Configure Modulator VI to select the modulator order. PDM modulator bandwidth DC to 0.015 * PCM rate. The bandwidth is DC to 46 kHz for PDM rate of 3.072 MHz. The default is 22 kHz at PDM rate

Modulator Specifications

Introduced in Digital Audio Acquisition and Generation Toolkit 2021 Q2

| PDM modulator order | 4 and 5. Use the Configure Modulator VI to select the modulator order. |
| --- | --- |
| PDM modulator bandwidth | DC to 0.015 * PCM rate. The bandwidth is DC to 46 kHz for PDM rate of 3.072 MHz. The default is 22 kHz at PDM rate of 3.072 MHz. |
| Recommended maximum output signal amplitude Fourth order modulator0.707 relative digital full scale Fifth order modulator0.500 relative digital full scale |  |
| Recommended maximum output signal amplitude |  |
| Fourth order modulator | 0.707 relative digital full scale |
| Fifth order modulator | 0.500 relative digital full scale |

Parent topic:

PDM Acquisition and Generation Specifications

Related reference:

- Digital Audio Acquisition and Generation Toolkit 2021 Q2 New Features and Changes

<!--NI_TOPIC bundle=digital-audio-acquisition-generation path=specs-pcm-acq-gen.html language=enus -->
## TOPIC 00015: PCM Acquisition and Generation Specifications

- bundle_id: `digital-audio-acquisition-generation`
- source_path: `specs-pcm-acq-gen.html`
- source_url: https://docs-be.ni.com/bundle/digital-audio-acquisition-generation/raw/resource/enus/specs-pcm-acq-gen.html
- document_id: `digital-audio-acquisition-generation`
- page_type: `leaf`
- content_type: `reference`
- source_description: Toolkit Characteristics for PXIe-7820/7821 Number of PCM data lines 32, consisting of 4 banks of 8 data lines, 2 bit clock (serial clock) lines, and 2 frame sync clock (word select clock or L/R clock) lines Number of PCM channels 1 channel to 16 channels per frame or data line depending on API confi

PCM Acquisition and Generation
 Specifications

#### Toolkit Characteristics for PXIe-7820/7821

| Number of PCM data lines | 32, consisting of 4 banks of 8 data lines, 2 bit clock (serial clock) lines, and 2 frame sync clock (word select clock or L/R clock) lines |
| --- | --- |
| Number of PCM channels | 1 channel to 16 channels per frame or data line depending on API configurations |
| Clock input/output | Master and slave |
| Data, clock, and GPIO logic level | Single-ended logic 1.2 V, 1.8 V, and 3.3 V |
| Frame length | 8 bits to 512 bits depending on API configurations |
| Channel length | 8 bits to 32 bits depending on API configurations |
| Data word format | 2's complement with configurable justification and endianness |
| Timebase reference source | 40 MHz Onboard Clock |
| Divided clock | <2%, 250 ps peak-peak jitter |
| DDS clock | <100 ppm, 8.3 ns peak-peak jitter |
| General purpose digital I/O (GPIO) | 16 static GPIO lines that can be configured independently as input or output lines |
| Generation signal types | Custom periodic signals |
| Data output format | 24 bits/channel |
| Number of timing engines Per target for synchronous acquisition and generation4 Acquisition4 Generation2 |  |
| Number of timing engines |  |
| Per target for synchronous acquisition and generation | 4 |
| Acquisition | 4 |
| Generation | 2 |
| PCM clock rate Bit clock (Master or Slave)160 kHz to 25 MHz Frame sync clock (Master or Slave)10 kHz to 192 kHz |  |
| PCM clock rate |  |
| Bit clock (Master or Slave) | 160 kHz to 25 MHz |
| Frame sync clock (Master or Slave) | 10 kHz to 192 kHz |
| Bit clock (serial clock) master and slave Master clockOne master bit clock shared across the data lines configured in a timing engine Slave clockOne slave clock on the first bit clock line in the bank: bit clock 0 in bank 0, bit clock 2 in bank 1, bit clock 4 in bank 2, and bit clock 6 in bank 3 |  |
| Bit clock (serial clock) master and slave |  |
| Master clock | One master bit clock shared across the data lines configured in a timing engine |
| Slave clock | One slave clock on the first bit clock line in the bank: bit clock 0 in bank 0, bit clock 2 in bank 1, bit clock 4 in bank 2, and bit clock 6 in bank 3 |
| Frame sync clock (word select clock) master and slave Master clockOne derived clock (from master bit clock) shared across the data lines configured in a timing engine Slave clockOne slave clock on the first frame sync clock line in the bank: frame sync clock 0 in bank 0, frame sync clock 2 in bank 1, frame sync clock 4 in bank 2, and frame sync clock 6 in bank 3 |  |
| Frame sync clock (word select clock) master and slave |  |
| Master clock | One derived clock (from master bit clock) shared across the data lines configured in a timing engine |
| Slave clock | One slave clock on the first frame sync clock line in the bank: frame sync clock 0 in bank 0, frame sync clock 2 in bank 1, frame sync clock 4 in bank 2, and frame sync clock 6 in bank 3 |
| Bit depth (audio depth) Acquisition8 bits to 32 bits depending on API configurations Generation8 bits to 24 bits depending on API configurations |  |
| Bit depth (audio depth) |  |
| Acquisition | 8 bits to 32 bits depending on API configurations |
| Generation | 8 bits to 24 bits depending on API configurations |
| Phase/Synchronization AcquisitionAll channels within a bank of 8 data lines are sampled synchronously from a common clock (internal clock or input clock). Phase relationship between channels is fully maintained. Channels within a task are synchronized. In slave mode, all channels within a bank are synchronized based on the input clock for the bank. GenerationAll channels within a task are generated synchronously from the internal clock or input clock. Phase relationship between channels is fully maintained. In slave mode, all channels within a bank are synchronized based on the input clock for the bank. |  |
| Phase/Synchronization |  |
| Acquisition | All channels within a bank of 8 data lines are sampled synchronously from a common clock (internal clock or input clock). Phase relationship between channels is fully maintained. Channels within a task are synchronized. In slave mode, all channels within a bank are synchronized based on the input clock for the bank. |
| Generation | All channels within a task are generated synchronously from the internal clock or input clock. Phase relationship between channels is fully maintained. In slave mode, all channels within a bank are synchronized based on the input clock for the bank. |

#### Toolkit Characteristics for USB-7845/7846

| Number of PCM data lines | 16, consisting of 2 banks of 8 data lines, 2 bit clock (serial clock) lines, and 2 frame sync clock (word select clock or L/R clock) lines |
| --- | --- |
| Number of PCM channels | 1 channel to 16 channels per data line depending on API configurations |
| Data, clock, and GPIO logic level | Single-ended logic 1.2 V, 1.8 V, and 3.3 V |
| Frame length | 8 bits to 512 bits depending on API configurations |
| Channel length | 8 bits to 32 bits depending on API configurations |
| Data word format | 2's complement with configurable justification and endianness |
| Timebase reference source | 40 MHz Onboard Clock |
| Divided clock | <2%, 250 ps peak-peak jitter |
| DDS clock | <100 ppm, 8.3 ns peak-peak jitter |
| General purpose digital I/O (GPIO) | 8 static GPIO lines that can be configured independently as input or output lines |
| Data output format | 24 bits/channel |
| Number of timing engines Acquisition2 Generation1 |  |
| Number of timing engines |  |
| Acquisition | 2 |
| Generation | 1 |
| Bit clock (serial clock) master and slave Master clockOne master bit clock shared across the data lines configured in a timing engine Slave clockOne slave clock on the first bit clock line in the bank: bit clock 0 in bank 0 and bit clock 2 in bank 1 |  |
| Bit clock (serial clock) master and slave |  |
| Master clock | One master bit clock shared across the data lines configured in a timing engine |
| Slave clock | One slave clock on the first bit clock line in the bank: bit clock 0 in bank 0 and bit clock 2 in bank 1 |
| Frame sync clock (word select clock) master and slave Master clockOne derived clock (from master bit clock) shared across the data lines configured in a timing engine Slave clockOne slave clock on the first frame sync clock line in the bank: frame sync clock 0 in bank 0 and frame sync clock 2 in bank 1 |  |
| Frame sync clock (word select clock) master and slave |  |
| Master clock | One derived clock (from master bit clock) shared across the data lines configured in a timing engine |
| Slave clock | One slave clock on the first frame sync clock line in the bank: frame sync clock 0 in bank 0 and frame sync clock 2 in bank 1 |
| Bit depth (audio depth) Acquisition8 bits to 32 bits depending on API configurations Generation8 bits to 24 bits depending on API configurations |  |
| Bit depth (audio depth) |  |
| Acquisition | 8 bits to 32 bits depending on API configurations |
| Generation | 8 bits to 24 bits depending on API configurations |
| Phase/Synchronization AcquisitionAll channels within a bank of 8 data lines are sampled synchronously from a common clock (internal clock or input clock). Phase relationship between channels is fully maintained. Channels within a task are synchronized. In slave mode, all channels within a bank are synchronized based on the input clock for the bank. GenerationAll channels within a task are generated synchronously from the internal clock or input clock. Phase relationship between channels is fully maintained. In slave mode, all channels within a bank are synchronized based on the input clock for the bank. |  |
| Phase/Synchronization |  |
| Acquisition | All channels within a bank of 8 data lines are sampled synchronously from a common clock (internal clock or input clock). Phase relationship between channels is fully maintained. Channels within a task are synchronized. In slave mode, all channels within a bank are synchronized based on the input clock for the bank. |
| Generation | All channels within a task are generated synchronously from the internal clock or input clock. Phase relationship between channels is fully maintained. In slave mode, all channels within a bank are synchronized based on the input clock for the bank. |

#### Acquisition and Generation Control
 Characteristics

| Acquisition mode | Finite or Continuous |
| --- | --- |
| Generation mode | Continuous |
| Acquisition trigger options | Immediate or PXI-Trigger. Independent triggering on each task |
| Generation trigger options | Immediate or PXI-Trigger |
| Generation export signal options | None |
| Acquisition PXI trigger | PXI-Trig [0..7]. Rising or Falling edge |
| Generation PXI trigger | PXI-Trig [0..7]. Rising or Falling edge |
| Acquisition trigger options for USB targets | Immediate |
| Generation trigger options for USB targets | Immediate |
| Acquisition Data Latch Delay[1]1 By default, the latch point is at the acquisition edge of the bit clock (serial clock) period which is at the half period edge of the clock. To compensate for cable delays, especially at the higher clock rates, you can delay the latch point until after the acquisition edge. | Time in ns to delay the latch point |
| Generation Timing Offset[2]2 By default, data generation happens at the start of the bit clock. When the receiver in master mode generates clocks, the generated data is not available at the receiver side at the expected time due to cable delays. To compensate for cable delays, you can advance data generation ahead of the start of the bit clock. | Time in ns to advance data generation |

#### Timing Specifications (Master
 Mode)

| Master Mode | Minimum | Maximum | Conditions |
| --- | --- | --- | --- |
| Bit clock (serial clock) frequency | 160 kHz | 25 MHz |  |
| Clock high | 0.35 T |  |  |
| Clock low | 0.35 T |  |  |
| Delay |  | 0.80 T |  |
| Hold time | 0 |  |  |
| Clock rise-time |  |  | 0.15 T |

#### Timing Specifications (Slave
 Mode)

| Slave Mode[3]3 The receiver specifications must match the performance of the transmitter. | Minimum | Maximum | Conditions |
| --- | --- | --- | --- |
| Bit clock (serial clock) frequency | 160 kHz | 25 MHz |  |
| Clock high | 0.35 T |  |  |
| Clock low | 0.35 T |  |  |
| Setup time | 0.5 T | 1.40 T | Depending on the input Latch Delay |
| Hold time |  |  |  |

#### Voltage Output Levels

| Logic Level4 Logic levels are the same as the logic levels of the FPGA target.[4] | Output Low Voltage Maximum | Output High Voltage Minimum |
| --- | --- | --- |
| 1.2 V | 0.20 V | 1.00 V |
| 1.8 V | 0.20 V | 1.54 V |
| 3.3 V | 0.20 V | 2.40 V |

#### Voltage Input Levels

| Logic Level[4] | Input Low Voltage Maximum | Input High Voltage Minimum |
| --- | --- | --- |
| 1.2 V | 0.42 V | 0.84 V |
| 1.8 V | 0.61 V | 1.21 V |
| 3.3 V | 0.80 V | 2.00 V |

Parent topic:

PCM Bus Specifications

[<sup>1</sup>](#note_ref-d3170e774) By default, the latch point is at the
 acquisition edge of the bit clock (serial clock) period which is at the half period
 edge of the clock. To compensate for cable delays, especially at the higher clock
 rates, you can delay the latch point until after the acquisition
 edge.

[<sup>2</sup>](#note_ref-d3170e786) By default, data generation happens at the start
 of the bit clock. When the receiver in master mode generates clocks, the generated
 data is not available at the receiver side at the expected time due to cable delays.
 To compensate for cable delays, you can advance data generation ahead of the start of
 the bit clock.

[<sup>3</sup>](#note_ref-d3170e958) The receiver specifications must match the
 performance of the transmitter.

<sup>4</sup> Logic levels are the same as the
 logic levels of the FPGA target.

<!--NI_TOPIC bundle=digital-audio-acquisition-generation path=specs-pcm-bank-map-pxie-7820-7821.html language=enus -->
## TOPIC 00016: PCM Bank to Channel Mapping for PXIe-7820/7821

- bundle_id: `digital-audio-acquisition-generation`
- source_path: `specs-pcm-bank-map-pxie-7820-7821.html`
- source_url: https://docs-be.ni.com/bundle/digital-audio-acquisition-generation/raw/resource/enus/specs-pcm-bank-map-pxie-7820-7821.html
- document_id: `digital-audio-acquisition-generation`
- page_type: `leaf`
- content_type: `reference`
- source_description: Bank 0 PCM Data Line 0 PCM Channel 0.0 Bank 2 PCM Data Line 16 PCM Channel 16.0 PCM Channel 0.1 PCM Channel 16.1 … … PCM Channel 0.15 PCM Channel 16.15 … … PCM Data Line 7 PCM Channel 7.0 PCM Data Line 23 PCM Channel 23.0 PCM Channel 7.1 PCM Channel 23.1 … … PCM Channel 7.15 PCM Channel 23.15 Bit Cl

PCM Bank to Channel Mapping for PXIe-7820/7821

| Bank 0 | PCM Data Line 0 | PCM Channel 0.0 | Bank 2 | PCM Data Line 16 | PCM Channel 16.0 |
| --- | --- | --- | --- | --- | --- |
| PCM Channel 0.1 | PCM Channel 16.1 |  |  |  |  |
| … | … |  |  |  |  |
| PCM Channel 0.15 | PCM Channel 16.15 |  |  |  |  |
| … | … |  |  |  |  |
| PCM Data Line 7 | PCM Channel 7.0 | PCM Data Line 23 | PCM Channel 23.0 |  |  |
| PCM Channel 7.1 | PCM Channel 23.1 |  |  |  |  |
| … | … |  |  |  |  |
| PCM Channel 7.15 | PCM Channel 23.15 |  |  |  |  |
| Bit Clock (Serial Clock) 0,1 and Frame Sync Clock (Word Select Clock) 0,1 | Bit Clock (Serial Clock) 4,5 and Frame Sync Clock (Word Select Clock) 4,5 |  |  |  |  |
| Bank 1 | PCM Data Line 8 | PCM Channel 8.0 | Bank 3 | PCM Data Line 24 | PCM Channel 24.0 |
| PCM Channel 8.1 | PCM Channel 24.1 |  |  |  |  |
| … | … |  |  |  |  |
| PCM Channel 8.15 | PCM Channel 24.15 |  |  |  |  |
| … | … |  |  |  |  |
| PCM Data Line 15 | PCM Channel 15.0 | PCM Data Line 31 | PCM Channel 31.0 |  |  |
| PCM Channel 15.1 | PCM Channel 31.1 |  |  |  |  |
| … | … |  |  |  |  |
| PCM Channel 15.15 | PCM Channel 31.15 |  |  |  |  |
| Bit Clock (Serial Clock) 2,3 and Frame Sync Clock (Word Select Clock) 2,3 | Bit Clock (Serial Clock) 6,7 and Frame Sync Clock (Word Select Clock) 6,7 |  |  |  |  |

Parent topic:

PCM Bus Specifications

<!--NI_TOPIC bundle=digital-audio-acquisition-generation path=specs-pcm-bank-map-usb-7845-7846.html language=enus -->
## TOPIC 00017: PCM Bank to Channel Mapping for USB-7845/7846

- bundle_id: `digital-audio-acquisition-generation`
- source_path: `specs-pcm-bank-map-usb-7845-7846.html`
- source_url: https://docs-be.ni.com/bundle/digital-audio-acquisition-generation/raw/resource/enus/specs-pcm-bank-map-usb-7845-7846.html
- document_id: `digital-audio-acquisition-generation`
- page_type: `leaf`
- content_type: `reference`
- source_description: Bank 0 PCM Data Line 0 PCM Channel 0.0 PCM Channel 0.1 … PCM Channel 0.15 … PCM Data Line 7 PCM Channel 7.0 PCM Channel 7.1 … PCM Channel 7.15 Bit Clock (Serial Clock) 0,1 and Frame Sync Clock (Word Select Clock) 0,1 Bank 1 PCM Data Line 8 PCM Channel 8.0 PCM Channel 8.1 … PCM Channel 8.15 … PCM Dat

PCM Bank to Channel Mapping for USB-7845/7846

| Bank 0 | PCM Data Line 0 | PCM Channel 0.0 |
| --- | --- | --- |
| PCM Channel 0.1 |  |  |
| … |  |  |
| PCM Channel 0.15 |  |  |
| … |  |  |
| PCM Data Line 7 | PCM Channel 7.0 |  |
| PCM Channel 7.1 |  |  |
| … |  |  |
| PCM Channel 7.15 |  |  |
| Bit Clock (Serial Clock) 0,1 and Frame Sync Clock (Word Select Clock) 0,1 |  |  |
| Bank 1 | PCM Data Line 8 | PCM Channel 8.0 |
| PCM Channel 8.1 |  |  |
| … |  |  |
| PCM Channel 8.15 |  |  |
| … |  |  |
| PCM Data Line 15 | PCM Channel 15.0 |  |
| PCM Channel 15.1 |  |  |
| … |  |  |
| PCM Channel 15.15 |  |  |
| Bit Clock (Serial Clock) 2,3 and Frame Sync Clock (Word Select Clock) 2,3 |  |  |

Parent topic:

PCM Bus Specifications

<!--NI_TOPIC bundle=digital-audio-acquisition-generation path=specs-pdm-acq-gen.html language=enus -->
## TOPIC 00018: PDM Acquisition and Generation Specifications

- bundle_id: `digital-audio-acquisition-generation`
- source_path: `specs-pdm-acq-gen.html`
- source_url: https://docs-be.ni.com/bundle/digital-audio-acquisition-generation/raw/resource/enus/specs-pdm-acq-gen.html
- document_id: `digital-audio-acquisition-generation`
- page_type: `leaf`
- content_type: `reference`
- source_description: The Digital Audio Acquisition and Generation Toolkit supports the PXIe-7820/7821 and USB-7845/7846.

PDM Acquisition and Generation
 Specifications

The Digital Audio Acquisition and Generation Toolkit supports the PXIe-7820/7821 and USB-7845/7846.

<!--NI_TOPIC bundle=digital-audio-acquisition-generation path=specs-pxie-7820.html language=enus -->
## TOPIC 00019: PDM Acquisition and Generation Specifications for PXIe-7820/7821

- bundle_id: `digital-audio-acquisition-generation`
- source_path: `specs-pxie-7820.html`
- source_url: https://docs-be.ni.com/bundle/digital-audio-acquisition-generation/raw/resource/enus/specs-pxie-7820.html
- document_id: `digital-audio-acquisition-generation`
- page_type: `leaf`
- content_type: `reference`
- source_description: Refer to these specifications when using the Digital Audio Acquisition and Generation Toolkit with the PXIe-7820/7821. PDM generation specifications are introduced in Digital Audio Acquisition and Generation Toolkit 2021 Q2. Specifications for the PXIe-7821 are introduced in Digital Audio Acquisitio

PDM Acquisition and Generation
 Specifications for PXIe-7820/7821

Refer to these specifications when using the Digital Audio Acquisition and Generation Toolkit
 with the PXIe-7820/7821.

Note

Digital Audio Acquisition and Generation Toolkit

Note

Digital Audio Acquisition and Generation Toolkit

Parent topic:

PDM Acquisition and Generation Specifications

Related reference:

- Digital Audio Acquisition and Generation Toolkit 2021 Q2 New Features and Changes

#### Toolkit Characteristics

| Number of PDM data lines Acquisition32, consisting of 4 banks of 8 data lines and 2 clock lines Generation16 |  |
| --- | --- |
| Number of PDM data lines |  |
| Acquisition | 32, consisting of 4 banks of 8 data lines and 2 clock lines |
| Generation | 16 |
| Number of PDM channels Acquisition64, consisting of 4 banks of 16 channels Generation32 |  |
| Number of PDM channels |  |
| Acquisition | 64, consisting of 4 banks of 16 channels |
| Generation | 32 |
| Number of timing engines Acquisition2 Generation1 |  |
| Number of timing engines |  |
| Acquisition | 2 |
| Generation | 1 |
| Clock input/output AcquisitionClock output—One master bit clock shared across 8 data lines (16 channels) GenerationClock input—One input shared across all output channels |  |
| Clock input/output |  |
| Acquisition | Clock output—One master bit clock shared across 8 data lines (16 channels) |
| Generation | Clock input—One input shared across all output channels |
| Data, clock, and GPIO logical level AcquisitionSingle-ended logic 1.2 V, 1.8 V, and 3.3 V GenerationSingle-ended logic 1.2 V, 1.8 V, and 3.3 V |  |
| Data, clock, and GPIO logical level |  |
| Acquisition | Single-ended logic 1.2 V, 1.8 V, and 3.3 V |
| Generation | Single-ended logic 1.2 V, 1.8 V, and 3.3 V |
| PDM clock rate Acquisition10 kb/s to 4800 kb/s, master mode only Generation10 kb/s to 4800 kb/s, slave mode only |  |
| PDM clock rate |  |
| Acquisition | 10 kb/s to 4800 kb/s, master mode only |
| Generation | 10 kb/s to 4800 kb/s, slave mode only |
| Timebase reference source AcquisitionPXI Express 100 MHz GenerationN/A |  |
| Timebase reference source |  |
| Acquisition | PXI Express 100 MHz |
| Generation | N/A |
| Divided clock chosen based on timebase accuracy errors Acquisition<2%, 250 ps peak-peak jitter GenerationN/A |  |
| Divided clock chosen based on timebase accuracy errors |  |
| Acquisition | <2%, 250 ps peak-peak jitter |
| Generation | N/A |
| DDS clock chosen based on timebase accuracy errors Acquisition<100 ppm, 8.3 ns peak-peak jitter GenerationN/A |  |
| DDS clock chosen based on timebase accuracy errors |  |
| Acquisition | <100 ppm, 8.3 ns peak-peak jitter |
| Generation | N/A |
| Phase/Synchronization AcquisitionAll channels within a bank of 8 data lines are sampled synchronously from a common clock. Phase relationship between channels is fully maintained. Channels within a task are synchronized. GenerationAll channels are generated synchronously from the input clock. Phase relationship between channels is fully maintained. |  |
| Phase/Synchronization |  |
| Acquisition | All channels within a bank of 8 data lines are sampled synchronously from a common clock. Phase relationship between channels is fully maintained. Channels within a task are synchronized. |
| Generation | All channels are generated synchronously from the input clock. Phase relationship between channels is fully maintained. |
| Generation signal types AcquisitionN/A GenerationSine, chirp (linear or logarithmic), white noise, and custom periodic signals |  |
| Generation signal types |  |
| Acquisition | N/A |
| Generation | Sine, chirp (linear or logarithmic), white noise, and custom periodic signals |
| General purpose digital I/O (GPIO) Acquisition24 static GPIO lines that can be configured independently as input or output lines Generation8 static GPIO lines that can be configured independently as input or output lines |  |
| General purpose digital I/O (GPIO) |  |
| Acquisition | 24 static GPIO lines that can be configured independently as input or output lines |
| Generation | 8 static GPIO lines that can be configured independently as input or output lines |

Refer to the *Bank to Channel Mapping for PXIe-7820/7821* section for the layout of banks, data lines, channels, and clock lines.

#### Decimation Filters Specifications

| Decimation factor options | 24, 32, 48, 64, 96, and 128. Select the option by task. |
| --- | --- |

| Decimation Factor | 24 and 48 | 32 and 64 | 96 and 128 |
| --- | --- | --- | --- |
| Normalized passband frequency (Hz) | 0.4275 | 0.438 | 0.45 |
| Passband ripple (dB) | ±0.0025 | ±0.001 | ±0.0004 |
| Normalized stopband frequency (Hz) | 0.5725 | 0.562 | 0.55 |
| Stopband attenuation (dB) | >110 | >120 | >123 |
| Filter output delay (samples) | 23 | 30 | 38 |

#### Acquisition and Generation Control
 Characteristics

| Acquisition options | Raw PDM and/or PCM (decimated) data |
| --- | --- |
| Acquisition mode | Finite or Continuous |
| Generation mode | Continuous |
| Acquisition trigger options | Immediate or PXI-Trigger. Independent triggering on each task |
| Generation trigger options | Immediate or PXI-Trigger |
| Generation export signal options | Start trigger to a PXI trigger line |
| Acquisition PXI trigger | PXI-Trig [0..7]. Rising or Falling edge |
| Generation PXI trigger | PXI-Trig [0..7]. Rising or Falling edge |
| Acquisition pre-delay | Common pre-delay for each task applied to both PDM and PCM data |
| Acquisition pre-delay resolution | 1 PDM bitrate period |
| Acquisition pre-delay range | 0 to 16383 bitrate periods |
| Acquisition post-delay | Common post-delay for each task and applied to decimated data |
| Acquisition post-delay resolution | 1 decimated data period |
| Acquisition post-delay range | 0 to 227-2 (134,217,726) decimated data periods |

#### Simulation Mode Characteristics

| PDM simulation signal type | Sine tone with a PDM amplitude of ±0.7071 FS (0.500 RMS) |
| --- | --- |
| Tone start phase | 0 degree for all tones when using the Configure PDM Trigger (None) VI |
| Tone frequencies at 3.072 MHz for all 64 PDM channel inputs PDM Channel Input 0L1 kHz PDM Channel Input 0R2 kHz ...... PDM Channel Input 7L15 kHz PDM Channel Input 7R16 kHz PDM Channel Input 8L1 kHz PDM Channel Input 8R2 kHz ...... PDM Channel Input 31L15 kHz PDM Channel Input 31R16 kHz |  |
| Tone frequencies at 3.072 MHz for all 64 PDM channel inputs |  |
| PDM Channel Input 0L | 1 kHz |
| PDM Channel Input 0R | 2 kHz |
| ... | ... |
| PDM Channel Input 7L | 15 kHz |
| PDM Channel Input 7R | 16 kHz |
| PDM Channel Input 8L | 1 kHz |
| PDM Channel Input 8R | 2 kHz |
| ... | ... |
| PDM Channel Input 31L | 15 kHz |
| PDM Channel Input 31R | 16 kHz |

Tone frequency is proportional to the selected PDM rate and repeats for every group of 16
 PDM channel inputs. For a PDM rate of 3.072 MHz, tone frequency is 1 kHz for the first PDM
 channel input, increments by 1 kHz for each PDM channel input, and repeats this sequence for
 every group of 16 PDM channel inputs.

Refer to the *Bank to Channel Mapping for PXIe-7820/7821* section for the layout of banks, data lines, channels, and clock lines.

#### Bank to Channel Mapping for PXIe-7820/7821

| Bank 0 | PDM Data Input 0 | PDM Channel Input 0L | Bank 2 | PDM Data Input 16 | PDM Channel Input 16L |
| --- | --- | --- | --- | --- | --- |
| PDM Channel Input 0R | PDM Channel Input 16R |  |  |  |  |
| … | … |  |  |  |  |
| PDM Data Input 7 | PDM Channel Input 7L | PDM Data Input 23 | PDM Channel Input 23L |  |  |
| PDM Channel Input 7R | PDM Channel Input 23R |  |  |  |  |
| Clock 0,1 | Clock 4,5 |  |  |  |  |
| Bank 1 | PDM Data Input 8 | PDM Channel Input 8L | Bank 3 | PDM Data Input 24 | PDM Channel Input 24L |
| PDM Channel Input 8R | PDM Channel Input 24R |  |  |  |  |
| … | … |  |  |  |  |
| PDM Data Input 15 | PDM Channel Input 15L | PDM Data Input 31 | PDM Channel Input 31L |  |  |
| PDM Channel Input 15R | PDM Channel Input 31R |  |  |  |  |
| Clock 2,3 | Clock 6,7 |  |  |  |  |

#### Connector Pin Assignments for PXIe-7820/7821 PDM Acquisition

Use the following connector pin assignments when you configure pin functions for PDM
 acquisition using the PXIe-7820/7821.

##### Connector 0 Pin Assignments

| Terminal | Function | Assignment |
| --- | --- | --- |
| 1 | DIO31 | PDM Input 15 |
| 2 | GND | GND |
| 3 | DIO29 | GPIO 11 |
| 4 | GND | GND |
| 5 | DIO27 | GPIO 9 |
| 6 | GND | GND |
| 7 | DIO25 | PDM Input 13 |
| 8 | GND | GND |
| 9 | DIO23 | PDM Input 11 |
| 10 | GND | GND |
| 11 | DIO21 | PDM Input 9 |
| 12 | GND | GND |
| 13 | DIO19 | PDM Clock Output 3 |
| 14 | GND | GND |
| 15 | DIO17 | GPIO 7 |
| 16 | GND | GND |
| 17 | DIO15 | GPIO 5 |
| 18 | GND | GND |
| 19 | DIO13 | PDM Clock Output 1 |
| 20 | GND | GND |
| 21 | DIO11 | PDM Input 7 |
| 22 | GND | GND |
| 23 | DIO9 | PDM Input 5 |
| 24 | GND | GND |
| 25 | DIO7 | PDM Input 3 |
| 26 | GND | GND |
| 27 | DIO5 | GPIO 3 |
| 28 | GND | GND |
| 29 | DIO3 | GPIO 1 |
| 30 | GND | GND |
| 31 | DIO1 | PDM Input 1 |
| 32 | GND | GND |
| 33 | GND | GND |
| 34 | GND | GND |
| 35 | DIO30 | PDM Clock Output 2 |
| 36 | GND | GND |
| 37 | DIO28 | PDM Input 14 |
| 38 | GND | GND |
| 39 | DIO26 | PDM Input 12 |
| 40 | GND | GND |
| 41 | DIO24 | PDM Input 10 |
| 42 | GND | GND |
| 43 | DIO22 | GPIO 10 |
| 44 | GND | GND |
| 45 | DIO20 | GPIO 8 |
| 46 | GND | GND |
| 47 | DIO18 | GPIO 6 |
| 48 | GND | GND |
| 49 | DIO16 | PDM Input 8 |
| 50 | GND | GND |
| 51 | DIO14 | PDM Input 6 |
| 52 | GND | GND |
| 53 | DIO12 | GPIO 4 |
| 54 | GND | GND |
| 55 | DIO10 | GPIO 2 |
| 56 | GND | GND |
| 57 | DIO8 | GPIO 0 |
| 58 | GND | GND |
| 59 | DIO6 | PDM Input 4 |
| 60 | GND | GND |
| 61 | DIO4 | PDM Input 2 |
| 62 | GND | GND |
| 63 | DIO2 | PDM Input 0 |
| 64 | GND | GND |
| 65 | DIO0 | PDM Clock Output 0 |
| 66 | GND | GND |
| 67 | External Clock x (an input only, x is the connector number) | Reserved |
| 68 | GND | GND |

##### Connector 1 Pin Assignments

| Terminal | Function | Assignment |
| --- | --- | --- |
| 1 | DIO31 | PDM Input 31 |
| 2 | GND | GND |
| 3 | DIO29 | GPIO 23 |
| 4 | GND | GND |
| 5 | DIO27 | GPIO 21 |
| 6 | GND | GND |
| 7 | DIO25 | PDM Input 29 |
| 8 | GND | GND |
| 9 | DIO23 | PDM Input 27 |
| 10 | GND | GND |
| 11 | DIO21 | PDM Input 25 |
| 12 | GND | GND |
| 13 | DIO19 | PDM Clock Output 7 |
| 14 | GND | GND |
| 15 | DIO17 | GPIO 19 |
| 16 | GND | GND |
| 17 | DIO15 | GPIO 17 |
| 18 | GND | GND |
| 19 | DIO13 | PDM Clock Output 5 |
| 20 | GND | GND |
| 21 | DIO11 | PDM Input 23 |
| 22 | GND | GND |
| 23 | DIO9 | PDM Input 21 |
| 24 | GND | GND |
| 25 | DIO7 | PDM Input 19 |
| 26 | GND | GND |
| 27 | DIO5 | GPIO 15 |
| 28 | GND | GND |
| 29 | DIO3 | GPIO 13 |
| 30 | GND | GND |
| 31 | DIO1 | PDM Input 17 |
| 32 | GND | GND |
| 33 | GND | GND |
| 34 | GND | GND |
| 35 | DIO30 | PDM Clock Output 6 |
| 36 | GND | GND |
| 37 | DIO28 | PDM Input 30 |
| 38 | GND | GND |
| 39 | DIO26 | PDM Input 28 |
| 40 | GND | GND |
| 41 | DIO24 | PDM Input 26 |
| 42 | GND | GND |
| 43 | DIO22 | GPIO 22 |
| 44 | GND | GND |
| 45 | DIO20 | GPIO 20 |
| 46 | GND | GND |
| 47 | DIO18 | GPIO 18 |
| 48 | GND | GND |
| 49 | DIO16 | PDM Input 24 |
| 50 | GND | GND |
| 51 | DIO14 | PDM Input 22 |
| 52 | GND | GND |
| 53 | DIO12 | GPIO 16 |
| 54 | GND | GND |
| 55 | DIO10 | GPIO 14 |
| 56 | GND | GND |
| 57 | DIO8 | GPIO 12 |
| 58 | GND | GND |
| 59 | DIO6 | PDM Input 20 |
| 60 | GND | GND |
| 61 | DIO4 | PDM Input 18 |
| 62 | GND | GND |
| 63 | DIO2 | PDM Input 16 |
| 64 | GND | GND |
| 65 | DIO0 | PDM Clock Output 4 |
| 66 | GND | GND |
| 67 | External Clock x (an input only, x is the connector number) | Reserved |
| 68 | GND | GND |

#### Connector Pin Assignments for PXIe-7820/7821 PDM Generation

Use the following connector pin assignments when you configure pin functions for PDM
 generation using the PXIe-7820/7821.

Introduced in Digital Audio Acquisition and Generation Toolkit 2021 Q2

##### Connector 0 Pin Assignments

| Terminal | Function | Assignment |
| --- | --- | --- |
| 1 | DIO31 | PDM Output 15 |
| 2 | GND | GND |
| 3 | DIO29 | Not connected |
| 4 | GND | GND |
| 5 | DIO27 | Not connected |
| 6 | GND | GND |
| 7 | DIO25 | PDM Output 13 |
| 8 | GND | GND |
| 9 | DIO23 | PDM Output 11 |
| 10 | GND | GND |
| 11 | DIO21 | PDM Output 9 |
| 12 | GND | GND |
| 13 | DIO19 | Not connected |
| 14 | GND | GND |
| 15 | DIO17 | GPIO 7 |
| 16 | GND | GND |
| 17 | DIO15 | GPIO 5 |
| 18 | GND | GND |
| 19 | DIO13 | Not connected |
| 20 | GND | GND |
| 21 | DIO11 | PDM Output 7 |
| 22 | GND | GND |
| 23 | DIO9 | PDM Output 5 |
| 24 | GND | GND |
| 25 | DIO7 | PDM Output 3 |
| 26 | GND | GND |
| 27 | DIO5 | GPIO 3 |
| 28 | GND | GND |
| 29 | DIO3 | GPIO 1 |
| 30 | GND | GND |
| 31 | DIO1 | PDM Output 1 |
| 32 | GND | GND |
| 33 | GND | GND |
| 34 | GND | GND |
| 35 | DIO30 | Not connected |
| 36 | GND | GND |
| 37 | DIO28 | PDM Output 14 |
| 38 | GND | GND |
| 39 | DIO26 | PDM Output 12 |
| 40 | GND | GND |
| 41 | DIO24 | PDM Output 10 |
| 42 | GND | GND |
| 43 | DIO22 | Not connected |
| 44 | GND | GND |
| 45 | DIO20 | Not connected |
| 46 | GND | GND |
| 47 | DIO18 | GPIO 6 |
| 48 | GND | GND |
| 49 | DIO16 | PDM Output 8 |
| 50 | GND | GND |
| 51 | DIO14 | PDM Output 6 |
| 52 | GND | GND |
| 53 | DIO12 | GPIO 4 |
| 54 | GND | GND |
| 55 | DIO10 | GPIO 2 |
| 56 | GND | GND |
| 57 | DIO8 | GPIO 0 |
| 58 | GND | GND |
| 59 | DIO6 | PDM Output 4 |
| 60 | GND | GND |
| 61 | DIO4 | PDM Output 2 |
| 62 | GND | GND |
| 63 | DIO2 | PDM Output 0 |
| 64 | GND | GND |
| 65 | DIO0 | PDM Clock 0 |
| 66 | GND | GND |
| 67 | External Clock x (an input only, x is the connector number) | Reserved |
| 68 | GND | GND |

<!--NI_TOPIC bundle=digital-audio-acquisition-generation path=specs-usb-7845-7846.html language=enus -->
## TOPIC 00020: PDM Acquisition and Generation Specifications for USB-7845/7846

- bundle_id: `digital-audio-acquisition-generation`
- source_path: `specs-usb-7845-7846.html`
- source_url: https://docs-be.ni.com/bundle/digital-audio-acquisition-generation/raw/resource/enus/specs-usb-7845-7846.html
- document_id: `digital-audio-acquisition-generation`
- page_type: `leaf`
- content_type: `reference`
- source_description: Refer to these specifications when using the Digital Audio Acquisition and Generation Toolkit with the USB-7845/7846. Introduced in Digital Audio Acquisition and Generation Toolkit 2021 Q2 Toolkit Characteristics Number of PDM data lines Acquisition 8, consisting of 1 bank of 8 data lines and 2 cloc

PDM Acquisition and Generation
 Specifications for USB-7845/7846

Refer to these specifications when using the Digital Audio Acquisition and Generation Toolkit
 with the USB-7845/7846.

Introduced in Digital Audio Acquisition and Generation Toolkit 2021 Q2

Parent topic:

PDM Acquisition and Generation Specifications

Related reference:

- Digital Audio Acquisition and Generation Toolkit 2021 Q2 New Features and Changes

#### Toolkit Characteristics

| Number of PDM data lines Acquisition8, consisting of 1 bank of 8 data lines and 2 clock lines Generation8 |  |
| --- | --- |
| Number of PDM data lines |  |
| Acquisition | 8, consisting of 1 bank of 8 data lines and 2 clock lines |
| Generation | 8 |
| Number of PDM channels Acquisition16 Generation16 |  |
| Number of PDM channels |  |
| Acquisition | 16 |
| Generation | 16 |
| Number of timing engines Acquisition1 Generation1 |  |
| Number of timing engines |  |
| Acquisition | 1 |
| Generation | 1 |
| Clock input/output AcquisitionClock output—One master bit clock shared across 8 data lines (16 channels) GenerationClock input—One input shared across all output channels |  |
| Clock input/output |  |
| Acquisition | Clock output—One master bit clock shared across 8 data lines (16 channels) |
| Generation | Clock input—One input shared across all output channels |
| Data, clock, and GPIO logical level AcquisitionSingle-ended logic 1.2 V, 1.8 V, and 3.3 V GenerationSingle-ended logic 1.2 V, 1.8 V, and 3.3 V |  |
| Data, clock, and GPIO logical level |  |
| Acquisition | Single-ended logic 1.2 V, 1.8 V, and 3.3 V |
| Generation | Single-ended logic 1.2 V, 1.8 V, and 3.3 V |
| PDM clock rate Acquisition10 kb/s to 4800 kb/s, master mode only Generation10 kb/s to 4800 kb/s, slave mode only |  |
| PDM clock rate |  |
| Acquisition | 10 kb/s to 4800 kb/s, master mode only |
| Generation | 10 kb/s to 4800 kb/s, slave mode only |
| Timebase reference source AcquisitionPXI Express 100 MHz GenerationN/A |  |
| Timebase reference source |  |
| Acquisition | PXI Express 100 MHz |
| Generation | N/A |
| Divided clock chosen based on timebase accuracy errors Acquisition<2%, 250 ps peak-peak jitter GenerationN/A |  |
| Divided clock chosen based on timebase accuracy errors |  |
| Acquisition | <2%, 250 ps peak-peak jitter |
| Generation | N/A |
| DDS clock chosen based on timebase accuracy errors Acquisition<100 ppm, 8.3 ns peak-peak jitter GenerationN/A |  |
| DDS clock chosen based on timebase accuracy errors |  |
| Acquisition | <100 ppm, 8.3 ns peak-peak jitter |
| Generation | N/A |
| Phase/Synchronization AcquisitionAll channels within a bank of 8 data lines are sampled synchronously from a common clock. Phase relationship between channels is fully maintained. Channels within a task are synchronized. GenerationAll channels are generated synchronously from the input clock. Phase relationship between channels is fully maintained. |  |
| Phase/Synchronization |  |
| Acquisition | All channels within a bank of 8 data lines are sampled synchronously from a common clock. Phase relationship between channels is fully maintained. Channels within a task are synchronized. |
| Generation | All channels are generated synchronously from the input clock. Phase relationship between channels is fully maintained. |
| Generation signal types AcquisitionN/A GenerationSine, chirp (linear or logarithmic), white noise, and custom periodic signals |  |
| Generation signal types |  |
| Acquisition | N/A |
| Generation | Sine, chirp (linear or logarithmic), white noise, and custom periodic signals |
| General purpose digital I/O (GPIO) Acquisition8 static GPIO lines that can be configured independently as input or output lines Generation8 static GPIO lines that can be configured independently as input or output lines |  |
| General purpose digital I/O (GPIO) |  |
| Acquisition | 8 static GPIO lines that can be configured independently as input or output lines |
| Generation | 8 static GPIO lines that can be configured independently as input or output lines |

Refer to the *Bank to Channel Mapping for USB-7845/7846* section for the layout of banks, data lines, channels, and clock lines.

#### Decimation Filters Specifications

| Decimation factor options | 24, 32, 48, 64, 96, and 128. Select the option by task. |
| --- | --- |

| Decimation Factor | 24 and 48 | 32 and 64 | 96 and 128 |
| --- | --- | --- | --- |
| Normalized passband frequency (Hz) | 0.4275 | 0.438 | 0.45 |
| Passband ripple (dB) | ±0.0025 | ±0.001 | ±0.0004 |
| Normalized stopband frequency (Hz) | 0.5725 | 0.562 | 0.55 |
| Stopband attenuation (dB) | >110 | >120 | >123 |
| Filter output delay (samples) | 23 | 30 | 38 |

#### Acquisition and Generation Control
 Characteristics

| Acquisition options | Raw PDM and/or PCM (decimated) data |
| --- | --- |
| Acquisition mode | Finite or Continuous |
| Generation mode | Continuous |
| Acquisition trigger options | Immediate only |
| Generation trigger options | Immediate only |
| Generation export signal options | None |
| Acquisition pre-delay | Common pre-delay for each task applied to both PDM and PCM data |
| Acquisition pre-delay resolution | 1 PDM bitrate period |
| Acquisition pre-delay range | 0 to 16383 bitrate periods |
| Acquisition post-delay | Common post-delay for each task and applied to decimated data |
| Acquisition post-delay resolution | 1 decimated data period |
| Acquisition post-delay range | 0 to 227-2 (134,217,726) decimated data periods |

#### Simulation Mode Characteristics

| PDM simulation signal type | Sine tone with a PDM amplitude of ±0.7071 FS (0.500 RMS) |
| --- | --- |
| Tone start phase | 0 degree for all tones when using the Configure PDM Trigger (None) VI |
| Tone frequencies at 3.072 MHz for all 16 PDM channel inputs PDM Channel Input 0L1 kHz PDM Channel Input 0R2 kHz ...... PDM Channel Input 7L15 kHz PDM Channel Input 7R16 kHz |  |
| Tone frequencies at 3.072 MHz for all 16 PDM channel inputs |  |
| PDM Channel Input 0L | 1 kHz |
| PDM Channel Input 0R | 2 kHz |
| ... | ... |
| PDM Channel Input 7L | 15 kHz |
| PDM Channel Input 7R | 16 kHz |

Tone frequency is proportional to the selected PDM rate. For a PDM rate of 3.072 MHz, tone
 frequency is 1 kHz for the first PDM channel input and increments by 1 kHz for each PDM
 channel input.

Refer to the *Bank to Channel Mapping for USB-7845/7846* section for the layout of banks, data lines, channels, and clock lines.

#### Bank to Channel Mapping for USB-7845/7846

| Bank 0 | PDM Data Input 0 | PDM Channel Input 0L |
| --- | --- | --- |
| PDM Channel Input 0R |  |  |
| … |  |  |
| PDM Data Input 7 | PDM Channel Input 7L |  |
| PDM Channel Input 7R |  |  |
| Clock 0,1 |  |  |

#### Connector Pin Assignments for USB-7845/7846 PDM Acquisition

Use the following connector pin assignments when you configure pin functions for PDM
 acquisition using the USB-7845/7846.

##### Connector 0 Pin Assignments

| Terminal | Function | Assignment |
| --- | --- | --- |
| 1 | DIO31 | Not connected |
| 2 | GND | GND |
| 3 | DIO29 | Not connected |
| 4 | GND | GND |
| 5 | DIO27 | Not connected |
| 6 | GND | GND |
| 7 | DIO25 | Not connected |
| 8 | GND | GND |
| 9 | DIO23 | Not connected |
| 10 | GND | GND |
| 11 | DIO21 | Not connected |
| 12 | GND | GND |
| 13 | DIO19 | Not connected |
| 14 | GND | GND |
| 15 | DIO17 | GPIO 7 |
| 16 | GND | GND |
| 17 | DIO15 | GPIO 5 |
| 18 | GND | GND |
| 19 | DIO13 | PDM Clock Output 1 |
| 20 | GND | GND |
| 21 | DIO11 | PDM Input 7 |
| 22 | GND | GND |
| 23 | DIO9 | PDM Input 5 |
| 24 | GND | GND |
| 25 | DIO7 | PDM Input 3 |
| 26 | GND | GND |
| 27 | DIO5 | GPIO 3 |
| 28 | GND | GND |
| 29 | DIO3 | GPIO 1 |
| 30 | GND | GND |
| 31 | DIO1 | PDM Input 1 |
| 32 | GND | GND |
| 33 | GND | GND |
| 34 | GND | GND |
| 35 | DIO30 | Not connected |
| 36 | GND | GND |
| 37 | DIO28 | Not connected |
| 38 | GND | GND |
| 39 | DIO26 | Not connected |
| 40 | GND | GND |
| 41 | DIO24 | Not connected |
| 42 | GND | GND |
| 43 | DIO22 | Not connected |
| 44 | GND | GND |
| 45 | DIO20 | Not connected |
| 46 | GND | GND |
| 47 | DIO18 | GPIO 6 |
| 48 | GND | GND |
| 49 | DIO16 | Not connected |
| 50 | GND | GND |
| 51 | DIO14 | PDM Input 6 |
| 52 | GND | GND |
| 53 | DIO12 | GPIO 4 |
| 54 | GND | GND |
| 55 | DIO10 | GPIO 2 |
| 56 | GND | GND |
| 57 | DIO8 | GPIO 0 |
| 58 | GND | GND |
| 59 | DIO6 | PDM Input 4 |
| 60 | GND | GND |
| 61 | DIO4 | PDM Input 2 |
| 62 | GND | GND |
| 63 | DIO2 | PDM Input 0 |
| 64 | GND | GND |
| 65 | DIO0 | PDM Clock Output 0 |
| 66 | GND | GND |
| 67 | External Clock x (an input only, x is the connector number) | Reserved |
| 68 | GND | GND |

#### Connector Pin Assignments for USB-7845/7846 PDM Generation

Use the following connector pin assignments when you configure pin functions for PDM
 generation using the USB-7845/7846.

##### Connector 0 Pin Assignments

| Terminal | Function | Assignment |
| --- | --- | --- |
| 1 | DIO31 | Not connected |
| 2 | GND | GND |
| 3 | DIO29 | Not connected |
| 4 | GND | GND |
| 5 | DIO27 | Not connected |
| 6 | GND | GND |
| 7 | DIO25 | Not connected |
| 8 | GND | GND |
| 9 | DIO23 | Not connected |
| 10 | GND | GND |
| 11 | DIO21 | Not connected |
| 12 | GND | GND |
| 13 | DIO19 | Not connected |
| 14 | GND | GND |
| 15 | DIO17 | GPIO 7 |
| 16 | GND | GND |
| 17 | DIO15 | GPIO 5 |
| 18 | GND | GND |
| 19 | DIO13 | Not connected |
| 20 | GND | GND |
| 21 | DIO11 | PDM Output 7 |
| 22 | GND | GND |
| 23 | DIO9 | PDM Output 5 |
| 24 | GND | GND |
| 25 | DIO7 | PDM Output 3 |
| 26 | GND | GND |
| 27 | DIO5 | GPIO 3 |
| 28 | GND | GND |
| 29 | DIO3 | GPIO 1 |
| 30 | GND | GND |
| 31 | DIO1 | PDM Output 1 |
| 32 | GND | GND |
| 33 | GND | GND |
| 34 | GND | GND |
| 35 | DIO30 | Not connected |
| 36 | GND | GND |
| 37 | DIO28 | Not connected |
| 38 | GND | GND |
| 39 | DIO26 | Not connected |
| 40 | GND | GND |
| 41 | DIO24 | Not connected |
| 42 | GND | GND |
| 43 | DIO22 | Not connected |
| 44 | GND | GND |
| 45 | DIO20 | Not connected |
| 46 | GND | GND |
| 47 | DIO18 | GPIO 6 |
| 48 | GND | GND |
| 49 | DIO16 | Not connected |
| 50 | GND | GND |
| 51 | DIO14 | PDM Output 6 |
| 52 | GND | GND |
| 53 | DIO12 | GPIO 4 |
| 54 | GND | GND |
| 55 | DIO10 | GPIO 2 |
| 56 | GND | GND |
| 57 | DIO8 | GPIO 0 |
| 58 | GND | GND |
| 59 | DIO6 | PDM Output 4 |
| 60 | GND | GND |
| 61 | DIO4 | PDM Output 2 |
| 62 | GND | GND |
| 63 | DIO2 | PDM Output 0 |
| 64 | GND | GND |
| 65 | DIO0 | PDM Clock Output 0 |
| 66 | GND | GND |
| 67 | External Clock x (an input only, x is the connector number) | Reserved |
| 68 | GND | GND |

<!--NI_TOPIC bundle=digital-audio-acquisition-generation path=troubleshoot.html language=enus -->
## TOPIC 00021: Troubleshooting

- bundle_id: `digital-audio-acquisition-generation`
- source_path: `troubleshoot.html`
- source_url: https://docs-be.ni.com/bundle/digital-audio-acquisition-generation/raw/resource/enus/troubleshoot.html
- document_id: `digital-audio-acquisition-generation`
- page_type: `leaf`
- content_type: `reference`
- source_description: Troubleshoot the following known issues you may encounter when using the Digital Audio Acquisition and Generation Toolkit.

Troubleshooting

Troubleshoot the following known issues you may encounter when using the Digital Audio Acquisition and Generation Toolkit.

- [What Should I Do If I Encounter DMA FIFO Overflow?](dma-fifo-overflow.html)
- [What Should I Do If Signals Are Distorted with a Bit Shift?](distort-signal-bit-shift.html)

<!--NI_TOPIC bundle=digital-audio-acquisition-generation path=user-manual-welcome.html language=enus -->
## TOPIC 00022: Welcome to the Digital Audio Acquisition and Generation Toolkit User Manual

- bundle_id: `digital-audio-acquisition-generation`
- source_path: `user-manual-welcome.html`
- source_url: https://docs-be.ni.com/bundle/digital-audio-acquisition-generation/raw/resource/enus/user-manual-welcome.html
- document_id: `digital-audio-acquisition-generation`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Digital Audio Acquisition and Generation Toolkit User Manual provides detailed descriptions of product functionality and step-by-step processes for use. Looking for something else?For information not found in the User Manual for your product, like specifications or API reference, browse Related

Welcome to the Digital Audio Acquisition and Generation
 Toolkit User Manual

The Digital Audio Acquisition and Generation
 Toolkit User Manual provides detailed
 descriptions of product functionality and step-by-step processes for use.

#### Looking for something else?

For
 information not found in the User Manual for your product, like specifications or
 API reference, browse Related Information.

Related information:

- Download Digital Audio Acquisition and Generation Toolkit
- Digital Audio Acquisition and Generation Toolkit Release Notes
- PXIe-7820 Specifications
- PXIe-7821 Specifications
- USB-7845 Specifications
- USB-7846 Specifications
- PXIe-7820 Getting Started
- PXIe-7821 Getting Started
- USB-7845 Getting Started
- USB-7846 Getting Started
