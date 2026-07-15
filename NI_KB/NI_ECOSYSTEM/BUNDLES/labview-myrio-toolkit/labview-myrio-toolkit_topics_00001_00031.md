# NI DOCUMENT BUNDLE: labview-myrio-toolkit

<!--NI_BUNDLE_CHUNK bundle=labview-myrio-toolkit start=1 end=31 -->
<!--NI_TOPIC bundle=labview-myrio-toolkit path=1-sample-versus-n-samples-modes.html language=enus -->
## TOPIC 00001: LabVIEW myRIO Toolkit 1 Sample Versus N Samples Modes

- bundle_id: `labview-myrio-toolkit`
- source_path: `1-sample-versus-n-samples-modes.html`
- source_url: https://docs-be.ni.com/bundle/labview-myrio-toolkit/raw/resource/enus/1-sample-versus-n-samples-modes.html
- document_id: `labview-myrio-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The LabVIEW myRIO Toolkit provides VIs to perform signal acquisition and generation using the 1 sample and n samples I/O modes. The following table explains the operation and application of the two I/O modes: 1 Signal Acquisition and Generation I/O Modes Operation I/O Mode Description Use Case Signa

### LabVIEW myRIO Toolkit 1
 Sample Versus N Samples Modes

The LabVIEW myRIO Toolkit provides VIs to
 perform signal acquisition and generation using the 1 sample and
 n samples I/O modes.

The following table explains the operation and application of the two I/O modes:

| Operation | I/O Mode | Description | Use Case |
| --- | --- | --- | --- |
| Signal Acquisition | 1 Sample | The myRIO device acquires one sample each time for a single channel or multiple channels. This mode uses software-timed acquisition. The sample rate of acquisition depends on the software loop rate on the real-time processor. Various factors affect the loop rate, such as simultaneous running of multiple programs on the myRIO target. | Acquiring the most recent value or periodically monitoring low-frequency signals, such as the temperature. |
| Signal Acquisition | N Samples | The myRIO device acquires multiple samples at the same time for a single channel or multiple channels. This mode has the following characteristics: Hardware-timed acquisition—The Field Programmable Gate Array (FPGA) target on the myRIO device has a 40 MHz clock rate, which controls the rate of acquisition. The sample rate depends on the hardware clock, which is faster and more accurate than a software loop. Therefore, you can have accurate control over the time between each sample. Buffered acquisition—The FPGA transfers the samples from the FPGA target to an intermediate memory buffer using direct memory access (DMA). LabVIEW then reads these samples on the real-time processor. | Acquiring finite high-frequency signals, such as an audio signal. |
| Signal Generation | 1 Sample | The myRIO device generates one sample each time for a single channel or multiple channels. This mode uses software-timed generation. The sample rate of generation depends on the software loop rate on the real-time side. Various factors affect the loop rate, such as the simultaneous running of multiple programs on the myRIO target. | Generating the most recent value or generating low-frequency signals. For example, generating a known voltage to stimulate a device. |
| Signal Generation | N Samples | The myRIO device generates multiple samples at the same time for a single channel or multiple channels. This mode has the following characteristics: Hardware-timed generation—The FPGA target on the myRIO device has a 40 MHz clock rate, which controls the rate of generation. The sample rate depends on the hardware clock, which is faster and more accurate than a software loop. Therefore, you can have accurate control over the time between each sample. Buffered generation—The real-time processor collects samples from LabVIEW and stores them in an intermediate memory buffer using DMA. Then, the FPGA retrieves the samples from the buffer. | Generating finite time-varying signals, such as an AC sine wave. |

Note

n

High
 Throughput Add-On for myRIO

High
 Throughput Add-On for myRIO

High Throughput Add-on for
 myRIO

After installing the High Throughput Add-On for myRIO, see
 High Frequency Sampling.lvproj in the
 labview\examples\myRIO\High Frequency Sampling directory. This
 example compares the 1 sample mode with the n
 samples mode using the myRIO Express VIs.

Parent topic:

Creating myRIO Applications with the LabVIEW myRIO Toolkit

Related information:

- High Throughput Add-on for myRIO

<!--NI_TOPIC bundle=labview-myrio-toolkit path=acquiring-and-processing-images.html language=enus -->
## TOPIC 00002: Acquiring and Processing Images with the LabVIEW myRIO Toolkit

- bundle_id: `labview-myrio-toolkit`
- source_path: `acquiring-and-processing-images.html`
- source_url: https://docs-be.ni.com/bundle/labview-myrio-toolkit/raw/resource/enus/acquiring-and-processing-images.html
- document_id: `labview-myrio-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Connect a USB camera to the USB host port on the myRIO to acquire and process images. Install the following NI software to create image applications: Vision Acquisition Software Acquires images from USB cameras that you connect to the myRIO. Vision Development Module Develops image processing applic

### Acquiring and Processing Images with the LabVIEW myRIO Toolkit

Connect a USB camera to the USB host port on the myRIO to acquire and process
 images.

Install the following NI software to create image applications:

Vision Acquisition Software

Vision Development Module

After you connect a USB camera to the myRIO and install the software, open LabVIEW.
 Select Tools»Vision Assistant to start acquiring and processing images.

Note

Machine Vision

Parent topic:

LabVIEW myRIO Toolkit Using myRIO with Other NI Software

Related information:

- Machine Vision

<!--NI_TOPIC bundle=labview-myrio-toolkit path=choosing-between-express-vis-and-low-level-vi.html language=enus -->
## TOPIC 00003: Choosing Between Express VIs and Low Level VIs with LabVIEW myRIO Toolkit

- bundle_id: `labview-myrio-toolkit`
- source_path: `choosing-between-express-vis-and-low-level-vi.html`
- source_url: https://docs-be.ni.com/bundle/labview-myrio-toolkit/raw/resource/enus/choosing-between-express-vis-and-low-level-vi.html
- document_id: `labview-myrio-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use Express VIs and Low Level VIs in the LabVIEW myRIO Toolkit to optimize I/O channel configuration and control.The LabVIEW myRIO Toolkit provides the following types of VIs for creating myRIO applications: Express VIs Use Express VIs to interactively configure the I/O channel settings. When you pl

### Choosing Between Express VIs and Low Level VIs
 with LabVIEW myRIO Toolkit

Use Express VIs and Low Level VIs in the LabVIEW myRIO Toolkit to optimize I/O channel configuration and control.

The LabVIEW myRIO Toolkit provides the following types of
 VIs for creating myRIO applications:

Express VIs

Low Level VIs

#### Understanding the Underlying Code of Express VIs

Open the configuration
 dialog box of an Express VI. Select the View Code tab to see
 the underlying code of the Express VI. This code consists of the Low Level VIs and
 other LabVIEW VIs.

The code of the Express VIs uses Smart
 Open VIs instead of Open VIs to open references to
 I/O channels. Smart Open VIs open an I/O reference the first time
 they run and then save the reference in memory. The use of Smart
 Open VIs ensures that the Express VIs run efficiently in loops. This
 efficiency occurs because the system does not open references to I/O channels for
 each iteration.

You can copy the code of an Express VI to a new block diagram
 and start programming with the Low Level VIs. After you copy the code, replace the
 Smart Open VI with an Open VI. The
 Open VIs open an I/O reference and pass the reference to all
 places that require access to the I/O channel. You also must add a
 Close VI to close I/O references after data operation. The
 following figure shows an example of modifying the code copied from the
 Analog Input Express VI.

Figure 5.

[IMAGE alt='Diagram showing code modification from Smart Open VI to Open VI and Close VI.' src='GUID-DD7394F2-8025-465D-8E63-349AB5D97FA1-a5.gif']

Parent topic:

Creating myRIO Applications with the LabVIEW myRIO Toolkit

Related information:

- Express VIs

<!--NI_TOPIC bundle=labview-myrio-toolkit path=choosing-fpga-personalities.html language=enus -->
## TOPIC 00004: Choosing FPGA Personalities with the LabVIEW myRIO Toolkit

- bundle_id: `labview-myrio-toolkit`
- source_path: `choosing-fpga-personalities.html`
- source_url: https://docs-be.ni.com/bundle/labview-myrio-toolkit/raw/resource/enus/choosing-fpga-personalities.html
- document_id: `labview-myrio-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Select a Field Programmable Gate Array (FPGA) personality when programming with myRIO. Each personality allows you to implement specific functionalities and use different channels on the myRIO device.FPGA personalities consist of predefined FPGA bitfiles used for programming with myRIO. The LabVIEW

### Choosing FPGA Personalities with the LabVIEW myRIO Toolkit

Select a Field Programmable Gate Array (FPGA) personality when programming with
 myRIO. Each personality allows you to implement specific functionalities and use different
 channels on the myRIO device.

FPGA personalities consist of predefined FPGA bitfiles used for programming with myRIO. The LabVIEW myRIO Toolkit provides the following
 FPGA personalities:

Default

High Throughput

Note

High Throughput Add-On for myRIO

High Throughput Add-On for myRIO

High Throughput Add-on for myRIO

Select a personality when you create a myRIO project.

1. Right-click a myRIO target in the Project Explorer 
 window.
2. Select Switch FPGA Personality .
3. Choose an available personality from the shortcut menu.

Note

The following table lists the functionalities and channel numbers that each personality
 supports:

| Supported Functionalities | Number of Supported Channels |  |  |  |
| --- | --- | --- | --- | --- |
| Default | High Throughput |  |  |  |
| myRIO-1900 | myRIO-1950 | myRIO-1900 | myRIO-1950 |  |
| Analog Input (1 Sample) | 12 | 8 | 12 | 8 |
| Analog Output (1 Sample) | 8 | 4 | 8 | 4 |
| Digital Input | 40 | 32 | 40 | 32 |
| Digital Output | 40 | 32 | 40 | 32 |
| Button | 1 | 1 | 1 | 1 |
| LED | 4 | 4 | 4 | 4 |
| Accelerometer | 3 | 3 | 3 | 3 |
| PWM | 8 | 6 | N/A | N/A |
| Encoder | 4 | 2 | N/A | N/A |
| SPI | 2 | 2 | N/A | N/A |
| I2C | 2 | 2 | N/A | N/A |
| UART | 2 | 2 | 2 | 2 |
| Interrupt | 8 | 8 | N/A | N/A |
| Analog Input (N Samples) | N/A | N/A | 1 | 1 |
| Analog Output (N Samples) | N/A | N/A | 1 | 1 |
| Audio Input (N Samples) | N/A | N/A | 2 | N/A |
| Audio Output (N Samples) | N/A | N/A | 2 | N/A |
| Digital Input (N Samples) | N/A | N/A | 1 | 1 |
| Digital Output (N Samples) | N/A | N/A | 1 | 1 |
| Input Device (Joystick) | 1 | 1 | 1 | 1 |

#### Supported Channels

The default FPGA personality supports the following channels of the I/O connectors on
 the myRIO device:

| Supported Functionalities | Supported Channels |  |
| --- | --- | --- |
| myRIO-1900 | myRIO-1950 |  |
| Analog Input | A/AI0~A/AI3B/AI0~B/AI3C/AI0, C/AI1AudioIn/Left, AudioIn/Right | A/AI0~A/AI3B/AI0~B/AI3 |
| Analog Output | A/AO0, A/AO1B/AO0, B/AO1C/AO0, C/AO1AudioOut/Left, AudioOut/Right | A/AO0, A/AO1B/AO0, B/AO1 |
| Digital Input | A/DIO0~A/AI15B/DIO0~B/DIO15C/DIO0~C/DIO7 | A/DIO0~A/AI15B/DIO0~B/DIO15 |
| Digital Output | A/DIO0~A/AI15B/DIO0~B/DIO15C/DIO0~C/DIO7 | A/DIO0~A/AI15B/DIO0~B/DIO15 |
| Button | Button0 | Button0 |
| LED | LED0~3 | LED0~3 |
| Accelerometer | X-Axis, Y-Axis, Z-Axis | X-Axis, Y-Axis, Z-Axis |
| PWM | A/PWM0~A/PWM2B/PWM0~B/PWM2C/PWM0, C/PWM1 | A/PWM0~A/PWM2B/PWM0~B/PWM2 |
| Encoder | A/ENCB/ENCC/ENC0, C/ENC1 | A/ENCB/ENC |
| SPI | A/SPIB/SPI | A/SPIB/SPI |
| I2C | A/I2CB/I2C | A/I2CB/I2C |
| UART | A/UARTB/UART | A/UARTB/UART |
| Interrupt | A/AI0 (Interrupt), A/AI1 (Interrupt),A/DIO0 (Interrupt)~A/DIO3(Interrupt), Button0 (Interrupt) | A/AI0 (Interrupt), A/AI1 (Interrupt),A/DIO0 (Interrupt)~A/DIO3(Interrupt), Button0 (Interrupt) |
| Input Device (Joystick) | USB | USB |

Note

A/

B/

C/

The High Throughput FPGA personality
 supports the following channels of the I/O connectors on the myRIO:

| Supported Functionalities | Supported Channels |  |
| --- | --- | --- |
| myRIO-1900 | myRIO-1950 |  |
| Analog Input | A/AI0~A/AI3B/AI0~B/AI3 C/AI0, C/AI1AudioIn/Left, AudioIn/Right | A/AI0~A/AI3B/AI0~B/AI3 |
| Analog Output | A/AO0, A/AO1B/AO0, B/AO1 C/AO0, C/AO1AudioOut/Left, AudioOut/Right | A/AO0, A/AO1B/AO0, B/AO1 |
| Analog Input (N Samples) | A/AI0 (N Samples) | A/AI0 (N Samples) |
| Analog Output (N Samples) | A/AO0 (N Samples) | A/AO0 (N Samples) |
| Audio Input (N Samples) | AudioIn/Left (N Samples), AudioIn/Right (N Samples) | N/A |
| Audio Output (N Samples) | AudioOut/Left (N Samples), AudioOut/Right (N Samples) | N/A |
| Digital Input | A/DIO0~A/AI15B/DIO0~B/DIO15 C/DIO0~C/DIO7 | A/DIO0~A/AI15B/DIO0~B/DIO15 |
| Digital Output | A/DIO0~A/AI15B/DIO0~B/DIO15 C/DIO0~C/DIO7 | A/DIO0~A/AI15B/DIO0~B/DIO15 |
| Digital Input (N Samples) | A/DI0 (N Samples) | A/DI0 (N Samples) |
| Digital Output (N Samples) | A/DO0 (N Samples) | A/DO0 (N Samples) |
| Button | Button0 | Button0 |
| LED | LED0~3 | LED0~3 |
| Accelerometer | X-Axis, Y-Axis, Z-Axis | X-Axis, Y-Axis, Z-Axis |
| UART | A/UARTB/UART | A/UARTB/UART |
| Input Device (Joystick) | USB | USB |

Parent topic:

Creating myRIO Applications with the LabVIEW myRIO Toolkit

Related concepts:

- LabVIEW myRIO Toolkit myRIO I/O Connectors

Related information:

- High Throughput Add-on for myRIO

<!--NI_TOPIC bundle=labview-myrio-toolkit path=communicating-with-rt-targets-from-a-host-com.html language=enus -->
## TOPIC 00005: LabVIEW myRIO Toolkit Communicating with RT Targets from a Host Computer

- bundle_id: `labview-myrio-toolkit`
- source_path: `communicating-with-rt-targets-from-a-host-com.html`
- source_url: https://docs-be.ni.com/bundle/labview-myrio-toolkit/raw/resource/enus/communicating-with-rt-targets-from-a-host-com.html
- document_id: `labview-myrio-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use network or front panel communication methods for communicating with myRIO targets from a host computer.5 RT Targets Communication Methods Network Communication Front Panel Communication Description A host VI runs on the host computer. The host VI communicates with the VI running on the RT target

### LabVIEW myRIO Toolkit
 Communicating with RT Targets from a Host Computer

Use network or front panel communication methods for communicating with myRIO targets
 from a host computer.

|  | Network Communication | Front Panel Communication |
| --- | --- | --- |
| Description | A host VI runs on the host computer. The host VI communicates with the VI running on the RT target using specific network communication programmatic controls. | LabVIEW and the RT Engine execute different parts of the same VI. LabVIEW on the host computer displays the front panel of the VI while the RT Engine executes the block diagram. |
| Use Case | Customizing the code of the VIs running on the host computer and on the RT target. Controlling the data that the host computer and the RT target send to each other. | Monitoring the VIs running on an RT target. |
| Example | For examples of creating different network communication systems using the myRIO, see the Network Communication sample project. To access this sample project, perform the following steps: Select File » Create Project in LabVIEW. Select Sample Projects » myRIO. | None. |

Parent topic:

Creating myRIO Applications with the LabVIEW myRIO Toolkit

Related information:

- Real-Time System Components

<!--NI_TOPIC bundle=labview-myrio-toolkit path=communicating-with-serial-devices-using-visa.html language=enus -->
## TOPIC 00006: LabVIEW myRIO Toolkit Communicating with Serial Devices Using VISA

- bundle_id: `labview-myrio-toolkit`
- source_path: `communicating-with-serial-devices-using-visa.html`
- source_url: https://docs-be.ni.com/bundle/labview-myrio-toolkit/raw/resource/enus/communicating-with-serial-devices-using-visa.html
- document_id: `labview-myrio-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Install NI-VISA to communicate with serial devices that you connect to the myRIO device.NI-VISA is the NI implementation of the VISA I/O standard. NI-VISA provides software libraries, interactive utilities, and configuration programs through Measurement & Automation Explorer (MAX) for various develo

### LabVIEW myRIO Toolkit
 Communicating with Serial Devices Using VISA

Install NI-VISA to communicate with serial devices that you connect to the myRIO
 device.

NI-VISA is the NI implementation of the VISA I/O standard. NI-VISA provides software libraries,
 interactive utilities, and configuration programs through Measurement & Automation
 Explorer (MAX) for various development needs.

Parent topic:

LabVIEW myRIO Toolkit Using myRIO with Other NI Software

Related information:

- VISA VIs and Functions

<!--NI_TOPIC bundle=labview-myrio-toolkit path=configuring-myrio.html language=enus -->
## TOPIC 00007: Configuring the myRIO Device with the LabVIEW myRIO Toolkit

- bundle_id: `labview-myrio-toolkit`
- source_path: `configuring-myrio.html`
- source_url: https://docs-be.ni.com/bundle/labview-myrio-toolkit/raw/resource/enus/configuring-myrio.html
- document_id: `labview-myrio-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following sections contain information about connecting the myRIO device to a host computer and installing software on the myRIO device.

### Configuring the myRIO Device with the LabVIEW myRIO Toolkit

The following sections contain information about connecting the myRIO device to a
 host computer and installing software on the myRIO device.

- [Connecting myRIO to a Host Computer Through USB with LabVIEW myRIO Toolkit](connecting-myrio-to-a-host-computer-through-usb.html) Perform the following steps to connect the myRIO device to a host computer using a USB connection.
- [Connecting myRIO to a Host Computer Through Wireless Connection with LabVIEW myRIO Toolkit](connecting-myrio-to-a-host-computer-through-wireless.html) Perform the following steps to connect the myRIO device to a host computer using a wireless network.
- [Installing Software on the myRIO Device](installing-software-on-myrio.html) When you run the Getting Started with myRIO wizard, LabVIEW installs the recommended software set on the myRIO device. You can also use Measurement & Automation Explorer (MAX) to manually install software on the myRIO device.

<!--NI_TOPIC bundle=labview-myrio-toolkit path=connecting-myrio-to-a-host-computer-through-usb.html language=enus -->
## TOPIC 00008: Connecting myRIO to a Host Computer Through USB with LabVIEW myRIO Toolkit

- bundle_id: `labview-myrio-toolkit`
- source_path: `connecting-myrio-to-a-host-computer-through-usb.html`
- source_url: https://docs-be.ni.com/bundle/labview-myrio-toolkit/raw/resource/enus/connecting-myrio-to-a-host-computer-through-usb.html
- document_id: `labview-myrio-toolkit`
- page_type: `leaf`
- content_type: `task`
- source_description: Perform the following steps to connect the myRIO device to a host computer using a USB connection. Connect the myRIO device to a host computer using a USB cable from the USB device port. The LabVIEW myRIO Toolkit installs a USB driver on the host computer. The USB driver creates a virtual network in

### Connecting myRIO to a Host Computer Through USB with LabVIEW myRIO Toolkit

Perform the following steps to connect the myRIO device to a host computer using a
 USB connection.

1. Connect the myRIO device to a host computer using a USB cable from the USB
 device port.
2. The LabVIEW myRIO Toolkit installs a
 USB driver on the host computer.
3. The USB driver creates a virtual network interface card on the host
 computer.
4. The USB driver assigns the 172.22.11.x IP address to the myRIO
 device.

Parent topic:

Configuring the myRIO Device with the LabVIEW myRIO Toolkit

<!--NI_TOPIC bundle=labview-myrio-toolkit path=connecting-myrio-to-a-host-computer-through-wireless.html language=enus -->
## TOPIC 00009: Connecting myRIO to a Host Computer Through Wireless Connection with LabVIEW myRIO Toolkit

- bundle_id: `labview-myrio-toolkit`
- source_path: `connecting-myrio-to-a-host-computer-through-wireless.html`
- source_url: https://docs-be.ni.com/bundle/labview-myrio-toolkit/raw/resource/enus/connecting-myrio-to-a-host-computer-through-wireless.html
- document_id: `labview-myrio-toolkit`
- page_type: `leaf`
- content_type: `task`
- source_description: Perform the following steps to connect the myRIO device to a host computer using a wireless network. Connect the myRIO device to the host computer through USB. Launch LabVIEW. Click the Set Up and Explore link. Select Configure WiFi. By connecting the myRIO device to a host computer through a wirele

### Connecting myRIO to a Host Computer
 Through Wireless Connection with LabVIEW myRIO Toolkit

Perform the following steps to connect the myRIO device to a host computer using a
 wireless network.

1. Connect the myRIO device to the host computer through USB.
2. Launch LabVIEW.
3. Click the Set Up and Explore link.
4. Select Configure WiFi.

By connecting the myRIO device to a host computer through a wireless network, you can
 perform the following tasks:

- Wirelessly detect the myRIO device
- Deploy applications
- Use shared variables to transfer data between the myRIO device and the host
 computer

Parent topic:

Configuring the myRIO Device with the LabVIEW myRIO Toolkit

<!--NI_TOPIC bundle=labview-myrio-toolkit path=creating-a-callback-vi.html language=enus -->
## TOPIC 00010: Creating a Callback VI with the LabVIEW myRIO Toolkit

- bundle_id: `labview-myrio-toolkit`
- source_path: `creating-a-callback-vi.html`
- source_url: https://docs-be.ni.com/bundle/labview-myrio-toolkit/raw/resource/enus/creating-a-callback-vi.html
- document_id: `labview-myrio-toolkit`
- page_type: `leaf`
- content_type: `task`
- source_description: Learn how to create a callback VI using LabVIEW for myRIO projects by configuring the connector pane and selecting appropriate options for handling interrupts. To create a callback VI, make sure the connector pane of the VI meets the following requirements: The connector pane uses the 4x2x2x4 patter

### Creating a Callback VI with the LabVIEW myRIO Toolkit

Learn how to create a callback VI using LabVIEW for myRIO projects by configuring the
 connector pane and selecting appropriate options for handling interrupts.

To create a callback VI, make sure the connector pane of the VI meets the following
 requirements:

- The connector pane uses the 4x2x2x4 pattern.
- The data type of the top-left terminal is unsigned 8-bit integer.
- The top-left terminal is a recommended terminal.

Perform the following steps to create callback VIs from templates:

1. Select File»Create Project in LabVIEW to create a new myRIO project.
2. Right-click the myRIO target in the Project Explorer
 window and select Create Callback VI from the shortcut
 menu.
3. Select one of the following options:
  - IO IRQ to create a callback VI that handles I/O
 interrupts, such as analog and digital input interrupts.
  - Timer IRQ to create a callback VI that handles
 timer interrupts.
4. Specify a name for the VI in the Specify a name for the callback
 VI dialog box and click Save.
5. Click OK when LabVIEW finishes creating and adding this
 VI to the myRIO target. 
 Note Expand the myRIO target to display the callback
 VI.

Parent topic:

Using Callback VIs to Handle Interrupts with the LabVIEW myRIO Toolkit

Related information:

- Building the Connector Pane
- Create Project Dialog Box

<!--NI_TOPIC bundle=labview-myrio-toolkit path=creating-audio-applications.html language=enus -->
## TOPIC 00011: Creating Audio Applications with the LabVIEW myRIO Toolkit

- bundle_id: `labview-myrio-toolkit`
- source_path: `creating-audio-applications.html`
- source_url: https://docs-be.ni.com/bundle/labview-myrio-toolkit/raw/resource/enus/creating-audio-applications.html
- document_id: `labview-myrio-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Access the audio input and output channels of myRIO using Express VIs, low‑level VIs, and FPGA interface nodes to create audio applications.The myRIO-1900 model provides audio input and output channels. Use the audio channels to perform audio acquisition and playback.The following table shows the me

### Creating Audio Applications with the LabVIEW myRIO Toolkit

Access the audio input and output channels of myRIO using Express VIs, low‑level VIs,
 and FPGA interface nodes to create audio applications.

The myRIO-1900 model provides audio input and output channels. Use the audio channels to perform
 audio acquisition and playback.

The following table shows the methods used for accessing the audio input and output channels:

| Audio Channel | Audio Input | Audio Input | Audio Output | Audio Output |
| --- | --- | --- | --- | --- |
| Method | Default | High Throughput | Default | High Throughput |
| myRIO Express VIs | Use the Audio Input Express VI and select the AudioIn/Left or the AudioIn/Right channel in the configuration dialog box. | Use the Audio Input Express VI and select the AudioIn/Left (N Samples) or the AudioIn/Right (N Samples) channel in the configuration dialog box. | Use the Audio Output Express VI and select the AudioOut/Left or the AudioOut/Right channel in the configuration dialog box. | Use the Audio Output Express VI and select the AudioOut/Left (N Samples) or the AudioOut/Right (N Samples) channel in the configuration dialog box. |
| myRIO Low Level VIs | Use the Open VI on the Analog Input 1 Sample palette to open a reference to the audio input channels. | Use the Open VI on the Audio Input N Samples palette to open a reference to the audio input channels. | Use the Open VI on the Analog Output 1 Sample palette to open a reference to the audio output channels. | Use the Open VI on the Audio Output N Samples palette to open a reference to the audio output channels. |
| FPGA Interface Nodes | Use the Open FPGA VI Reference function to open a reference to the default FPGA personality. Wire the output reference to the Read/Write Control function to access the audio input channels. | Use the Open FPGA VI Reference function to open a reference to the high-throughput FPGA personality. Wire the output reference to the Read/Write Control function and the Invoke Method function to access the audio input channels. | Use the Open FPGA VI Reference function to open a reference to the default FPGA personality. Wire the output reference to the Read/Write Control function to access the audio output channels. | Use the Open FPGA VI Reference function to open a reference to the high-throughput FPGA personality. Wire the output reference to the Read/Write Control function and the Invoke Method function to access the audio output channels. |

Clap
 Sensor

Voice Recorder

1. Select File»Create Project in LabVIEW.
2. Select Sample Projects»myRIO .

Note

Voice
 Recorder

High Throughput Add-On for myRIO

High Throughput Add-On for myRIO

High Throughput
 Add-on for myRIO

Note

Parent topic:

Creating myRIO Applications with the LabVIEW myRIO Toolkit

Related concepts:

- Choosing FPGA Personalities with the LabVIEW myRIO Toolkit

Related information:

- High Throughput Add-on for myRIO

<!--NI_TOPIC bundle=labview-myrio-toolkit path=creating-feedback-control-systems.html language=enus -->
## TOPIC 00012: Creating Feedback Control Systems with the LabVIEW myRIO Toolkit

- bundle_id: `labview-myrio-toolkit`
- source_path: `creating-feedback-control-systems.html`
- source_url: https://docs-be.ni.com/bundle/labview-myrio-toolkit/raw/resource/enus/creating-feedback-control-systems.html
- document_id: `labview-myrio-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use myRIO with the PID VIs to create feedback control systems to control, for example, motors, temperature, and pressure.To access the PID VIs, select Control & Simulation PID from the Functions palette in LabVIEW.

### Creating Feedback Control Systems with the LabVIEW myRIO Toolkit

Use myRIO with the PID VIs to create feedback control systems to control, for
 example, motors, temperature, and pressure.

To access the PID VIs, select Control & Simulation»PID from the Functions palette in LabVIEW.

Parent topic:

LabVIEW myRIO Toolkit Using myRIO with Other NI Software

Related information:

- PID VIs
- Functions Palette

<!--NI_TOPIC bundle=labview-myrio-toolkit path=creating-myrio-applications.html language=enus -->
## TOPIC 00013: Creating myRIO Applications with the LabVIEW myRIO Toolkit

- bundle_id: `labview-myrio-toolkit`
- source_path: `creating-myrio-applications.html`
- source_url: https://docs-be.ni.com/bundle/labview-myrio-toolkit/raw/resource/enus/creating-myrio-applications.html
- document_id: `labview-myrio-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following sections contain information about the myRIO programming concepts that are helpful for creating a myRIO application.

### Creating myRIO Applications with the LabVIEW myRIO Toolkit

The following sections contain information about the myRIO programming concepts that
 are helpful for creating a myRIO application.

- [LabVIEW myRIO Toolkit 1 Sample Versus N Samples Modes](1-sample-versus-n-samples-modes.html) The LabVIEW myRIO Toolkit provides VIs to perform signal acquisition and generation using the 1 sample and n samples I/O modes.
- [Choosing Between Express VIs and Low Level VIs with LabVIEW myRIO Toolkit](choosing-between-express-vis-and-low-level-vi.html) Use Express VIs and Low Level VIs in the LabVIEW myRIO Toolkit to optimize I/O channel configuration and control.
- [Choosing FPGA Personalities with the LabVIEW myRIO Toolkit](choosing-fpga-personalities.html) Select a Field Programmable Gate Array (FPGA) personality when programming with myRIO. Each personality allows you to implement specific functionalities and use different channels on the myRIO device.
- [LabVIEW myRIO Toolkit Communicating with RT Targets from a Host Computer](communicating-with-rt-targets-from-a-host-com.html) Use network or front panel communication methods for communicating with myRIO targets from a host computer.
- [Creating Audio Applications with the LabVIEW myRIO Toolkit](creating-audio-applications.html) Access the audio input and output channels of myRIO using Express VIs, low‑level VIs, and FPGA interface nodes to create audio applications.
- [Deploying Real-Time Applications with the LabVIEW myRIO Toolkit](deploying-real-time-applications.html) After building a real-time application for myRIO, deploy the application to the RT target on the myRIO device.
- [Generating FPGA Clocks with the LabVIEW myRIO Toolkit](generating-fpga-clocks.html) Generate FPGA clock signals with frequencies lower than 40 MHz by modifying rising edges, using clock divisors, and calculating frequencies for PWM and SPI I/O.
- [LabVIEW myRIO Toolkit Understanding Hysteresis](understanding-hysteresis.html) Hysteresis, also known as window size, adds a window above or below the trigger level. Hysteresis reduces false triggering due to noise or jitter in the signal.
- [LabVIEW myRIO Toolkit Understanding Latency](understanding-latency.html) Latency is the time required to complete an operation. When you use the myRIO Express VIs to acquire or generate signals, latency has different meanings.
- [Using Callback VIs to Handle Interrupts with the LabVIEW myRIO Toolkit](using-callback-vis-to-handle-interrupts.html) Create and edit callback VIs for interrupt handling, considering their characteristics.
- [Using the Project Explorer Window with the LabVIEW myRIO Toolkit](using-the-project-explorer-window.html) Use the Project Explorer window to manage targets, VIs, and support files in LabVIEW projects. Connect myRIO targets to the host computer, set target properties, and deploy VIs to targets in Project Explorer .

<!--NI_TOPIC bundle=labview-myrio-toolkit path=creating-robotics-applications.html language=enus -->
## TOPIC 00014: LabVIEW myRIO Toolkit Creating Robotics Applications

- bundle_id: `labview-myrio-toolkit`
- source_path: `creating-robotics-applications.html`
- source_url: https://docs-be.ni.com/bundle/labview-myrio-toolkit/raw/resource/enus/creating-robotics-applications.html
- document_id: `labview-myrio-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use myRIO with the Robotics Module for LabRIO to develop and deploy robotics applications, such as steering, path planning, obstacle avoidance, and inverse kinematics.The LabVIEW Robotics Module for LabRIO provides select functionality from the LabVIEW Robotics Module to use with myRIO or roboRIO. A

### LabVIEW myRIO Toolkit
 Creating Robotics Applications

Use myRIO with the Robotics Module for LabRIO to develop and deploy robotics
 applications, such as steering, path planning, obstacle avoidance, and inverse
 kinematics.

The LabVIEW Robotics Module for LabRIO provides select functionality from the LabVIEW Robotics
 Module to use with myRIO or roboRIO.

After installing the Robotics Module for LabRIO, you have access to the Robotics
 Algorithms VIs. Select myRIO»Robotics Algorithms from the Functions palette in LabVIEW.

Note

Required and Optional Software to Program myRIO

Parent topic:

LabVIEW myRIO Toolkit Using myRIO with Other NI Software

Related information:

- Functions Palette
- Required and Optional Software to Program myRIO

<!--NI_TOPIC bundle=labview-myrio-toolkit path=deploying-real-time-applications.html language=enus -->
## TOPIC 00015: Deploying Real-Time Applications with the LabVIEW myRIO Toolkit

- bundle_id: `labview-myrio-toolkit`
- source_path: `deploying-real-time-applications.html`
- source_url: https://docs-be.ni.com/bundle/labview-myrio-toolkit/raw/resource/enus/deploying-real-time-applications.html
- document_id: `labview-myrio-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: After building a real-time application for myRIO, deploy the application to the RT target on the myRIO device.Use one of the following methods to deploy real-time applications: Interactive Deployment Deploys real-time applications from the Project Explorer window. Interactive deployment requires tha

### Deploying Real-Time Applications with the LabVIEW myRIO Toolkit

After building a real-time application for myRIO, deploy the application to the RT
 target on the myRIO device.

Use one of the following methods to deploy real-time applications:

Interactive Deployment

Project Explorer

Run

Project Explorer

Headless Deployment

Parent topic:

Creating myRIO Applications with the LabVIEW myRIO Toolkit

Related information:

- Building and Deploying a Stand-Alone Real-Time
 Application

<!--NI_TOPIC bundle=labview-myrio-toolkit path=generating-fpga-clocks.html language=enus -->
## TOPIC 00016: Generating FPGA Clocks with the LabVIEW myRIO Toolkit

- bundle_id: `labview-myrio-toolkit`
- source_path: `generating-fpga-clocks.html`
- source_url: https://docs-be.ni.com/bundle/labview-myrio-toolkit/raw/resource/enus/generating-fpga-clocks.html
- document_id: `labview-myrio-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Generate FPGA clock signals with frequencies lower than 40 MHz by modifying rising edges, using clock divisors, and calculating frequencies for PWM and SPI I/O. The FPGA target on the hardware operates at a clock rate of 40 MHz. Therefore, the clock cycle is 25 ns. To generate a frequency lower than

### Generating FPGA Clocks with the LabVIEW myRIO Toolkit

Generate FPGA clock signals with frequencies lower than 40 MHz by modifying rising
 edges, using clock divisors, and calculating frequencies for PWM and SPI I/O.

The FPGA target on the hardware operates at a clock rate of 40
 MHz. Therefore, the clock cycle is 25 ns. To
 generate a frequency lower than 40 MHz, you can change a
 signal on every x-th rising edges of the clock signal.

[Figure 6.Modifying a 40 MHz Clock
 Signal](generating-fpga-clocks.html#GUID-48D4A133-6F8E-4A9C-9284-EB9DB4712637__FIG_KCN_3VM_PJC) shows an example of modifying a 40
 MHz clock signal on rising edges. The modification generates 20 MHz and 10 MHz clock
 signals. Toggling the clock signal on each rising edge generates the 20 MHz clock signal. Toggling the clock signal on every
 other rising edge produces the 10 MHz clock signal.

Figure 6.

[IMAGE alt='Waveforms showing 40 MHz, 20 MHz, and 10 MHz clock signals.' src='GUID-A19DB609-70D7-42EF-9B54-B68A89558F01-a5.gif']

The frequency to be generated on the hardware must meet the following requirements:

- The frequency must be divisible by 25 ns because the
 clock cycle is 25 ns . The system counts the number of
 rising edges to make changes. For example, you cannot generate a frequency of 25 MHz . The first achievable frequency below 40 MHz is 20 MHz .
- The frequency must be between 610.35 Hz and 40 MHz . The hardware uses a 16-bit counter that
 counts from 0 to 65,535. You can calculate the lowest frequency with the following equation: 1
 25
 
 n
 s
 ·
 65536
 ≈
 610
 .
 35
 
 H
 z

Use clock divisors to generate even lower frequencies for different I/O types. Divide the
 base frequency by even numbers and use the generated clock to increment the counter. For
 example, with a clock divisor of 2, the lowest achievable frequency is:

1

50

n

s

·

65536

≈

305

.

17

H

z

The following equation calculates frequencies that you can generate for the Pulse Width
 Modulation (PWM) I/O:

f

P

W

M

=

f

c

l

k

N

·

X

+

1

Where

- f PWM is the desired PWM frequency.
- f clk is the base clock frequency.
- N is the clock divisor.
- X is the number of counts before changing the signal.

The following equation calculates frequencies that you can generate for Serial Peripheral
 Interface (SPI) I/O:

f

S

P

I

=

f

c

l

k

2

·

N

·

X

+

1

Where

- f SPI is the desired SPI frequency.
- f clk is the base clock frequency.
- N is the clock divisor.
- X is the number of counts before changing the signal.

Some Express VIs have a Validate button. Use this button to check
 if the Express VIs can generate the frequency you specify. If you specify an invalid
 frequency value, the Express VIs adjust it to the nearest valid value when you click
 Validate.

Parent topic:

Creating myRIO Applications with the LabVIEW myRIO Toolkit

<!--NI_TOPIC bundle=labview-myrio-toolkit path=i-o-connectors.html language=enus -->
## TOPIC 00017: LabVIEW myRIO Toolkit myRIO I/O Connectors

- bundle_id: `labview-myrio-toolkit`
- source_path: `i-o-connectors.html`
- source_url: https://docs-be.ni.com/bundle/labview-myrio-toolkit/raw/resource/enus/i-o-connectors.html
- document_id: `labview-myrio-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figures show the pinouts of the I/O connectors on the myRIO device. 1 Mini System Port (MSP) Connectors Diagram of myRIO MSP connectors with pin labels and audio ports. 2 myRIO Expansion Port (MXP) Connectors Diagram of myRIO MXP connectors with pin labels and functions.

### LabVIEW myRIO Toolkit myRIO
 I/O Connectors

The following figures show the pinouts of the I/O connectors on the myRIO
 device.

Figure 1.

[IMAGE alt='Diagram of myRIO MSP connectors with pin labels and audio ports.' src='GUID-A436AD8B-48A0-4C1F-95AC-F973D75DA5AA-a5.gif']

Figure 2.

[IMAGE alt='Diagram of myRIO MXP connectors with pin labels and functions.' src='GUID-CCC82AF2-22EF-41C9-A1B8-2C1AAB415282-a5.gif']

Parent topic:

LabVIEW myRIO Toolkit myRIO Hardware Overview

<!--NI_TOPIC bundle=labview-myrio-toolkit path=installing-software-on-myrio.html language=enus -->
## TOPIC 00018: Installing Software on the myRIO Device

- bundle_id: `labview-myrio-toolkit`
- source_path: `installing-software-on-myrio.html`
- source_url: https://docs-be.ni.com/bundle/labview-myrio-toolkit/raw/resource/enus/installing-software-on-myrio.html
- document_id: `labview-myrio-toolkit`
- page_type: `leaf`
- content_type: `task`
- source_description: When you run the Getting Started with myRIO wizard, LabVIEW installs the recommended software set on the myRIO device. You can also use Measurement & Automation Explorer (MAX) to manually install software on the myRIO device. Complete the following steps to install software on the myRIO using MAX: E

### Installing Software on the myRIO
 Device

When you run the Getting Started with myRIO wizard, LabVIEW
 installs the recommended software set on the myRIO device. You can also use
 Measurement & Automation Explorer (MAX) to manually install
 software on the myRIO device.

Complete the following steps to install software on the myRIO using
 MAX:

1. Expand Remote Systems in the configuration tree in
 MAX and then expand your myRIO target.
2. Right-click Software and select Add/Remove
 Software to launch LabVIEW Real-Time Software
 Wizard.
3. Select the recommended software set for the myRIO device.
4. Click Next.
5. Click myRIO
 x, where x matches
 the version of the LabVIEW myRIO Toolkit.
6. Click Next to view a summary of your selection.
7. Click Next to start installing the software. 
 When the installation completes, the wizard restarts the myRIO
 device.
8. Click Finish to close the wizard.

Parent topic:

Configuring the myRIO Device with the LabVIEW myRIO Toolkit

<!--NI_TOPIC bundle=labview-myrio-toolkit path=myrio-1900-hardware-block-diagram.html language=enus -->
## TOPIC 00019: LabVIEW myRIO Toolkit myRIO-1900 Hardware Block Diagram

- bundle_id: `labview-myrio-toolkit`
- source_path: `myrio-1900-hardware-block-diagram.html`
- source_url: https://docs-be.ni.com/bundle/labview-myrio-toolkit/raw/resource/enus/myrio-1900-hardware-block-diagram.html
- document_id: `labview-myrio-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the hardware block diagram of the myRIO-1900. 3 myRIO-1900 Hardware Block Diagram Block diagram of myRIO-1900 hardware components and connections.

### LabVIEW myRIO Toolkit
 myRIO-1900 Hardware Block Diagram

The following figure shows the hardware block diagram of the myRIO-1900.

Figure 3.

[IMAGE alt='Block diagram of myRIO-1900 hardware components and connections.' src='GUID-5D396E42-E2B1-4FB4-BBAC-E7B3ECDA2DD7-a5.gif']

Parent topic:

LabVIEW myRIO Toolkit myRIO Hardware Overview

<!--NI_TOPIC bundle=labview-myrio-toolkit path=myrio-1950-hardware-block-diagram.html language=enus -->
## TOPIC 00020: LabVIEW myRIO Toolkit myRIO-1950 Hardware Block Diagram

- bundle_id: `labview-myrio-toolkit`
- source_path: `myrio-1950-hardware-block-diagram.html`
- source_url: https://docs-be.ni.com/bundle/labview-myrio-toolkit/raw/resource/enus/myrio-1950-hardware-block-diagram.html
- document_id: `labview-myrio-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the hardware block diagram of the myRIO-1950. 4 myRIO-1950 Hardware Block Diagram Block diagram of myRIO-1950 hardware components and connections.

### LabVIEW myRIO Toolkit
 myRIO-1950 Hardware Block Diagram

The following figure shows the hardware block diagram of the myRIO-1950.

Figure 4.

[IMAGE alt='Block diagram of myRIO-1950 hardware components and connections.' src='GUID-06BE8AEF-491B-4254-95D6-0662382D5745-a5.gif']

Parent topic:

LabVIEW myRIO Toolkit myRIO Hardware Overview

<!--NI_TOPIC bundle=labview-myrio-toolkit path=myrio-hardware-overview.html language=enus -->
## TOPIC 00021: LabVIEW myRIO Toolkit myRIO Hardware Overview

- bundle_id: `labview-myrio-toolkit`
- source_path: `myrio-hardware-overview.html`
- source_url: https://docs-be.ni.com/bundle/labview-myrio-toolkit/raw/resource/enus/myrio-hardware-overview.html
- document_id: `labview-myrio-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following sections contain basic information about the myRIO hardware.

### LabVIEW myRIO Toolkit myRIO
 Hardware Overview

The following sections contain basic information about the myRIO
 hardware.

- [LabVIEW myRIO Toolkit myRIO I/O Connectors](i-o-connectors.html) The following figures show the pinouts of the I/O connectors on the myRIO device.
- [LabVIEW myRIO Toolkit myRIO-1900 Hardware Block Diagram](myrio-1900-hardware-block-diagram.html) The following figure shows the hardware block diagram of the myRIO-1900.
- [LabVIEW myRIO Toolkit myRIO-1950 Hardware Block Diagram](myrio-1950-hardware-block-diagram.html) The following figure shows the hardware block diagram of the myRIO-1950.

<!--NI_TOPIC bundle=labview-myrio-toolkit path=opening-a-callback-vi.html language=enus -->
## TOPIC 00022: Opening a Callback VI with the LabVIEW myRIO Toolkit

- bundle_id: `labview-myrio-toolkit`
- source_path: `opening-a-callback-vi.html`
- source_url: https://docs-be.ni.com/bundle/labview-myrio-toolkit/raw/resource/enus/opening-a-callback-vi.html
- document_id: `labview-myrio-toolkit`
- page_type: `leaf`
- content_type: `task`
- source_description: Learn how to open and edit a callback VI in the Project Explorer window, and locate specific callback VIs used by other VIs. Double-click a callback VI under the target in the Project Explorer window to open and edit this VI. There might be multiple callback VIs under the target. Use one of the foll

### Opening a Callback VI with the LabVIEW myRIO Toolkit

Learn how to open and edit a callback VI in the Project Explorer window, and locate
 specific callback VIs used by other VIs.

Project
 Explorer

Note

- Double-click the callback VI reference that you wire to the
 Register Analog Input Interrupt VI or the
 Register Digital Input Interrupt VI.
- Right-click the Interrupt Express VI and select
 Open Callback VI from the shortcut menu.

Parent topic:

Using Callback VIs to Handle Interrupts with the LabVIEW myRIO Toolkit

<!--NI_TOPIC bundle=labview-myrio-toolkit path=overview.html language=enus -->
## TOPIC 00023: LabVIEW myRIO Toolkit Overview

- bundle_id: `labview-myrio-toolkit`
- source_path: `overview.html`
- source_url: https://docs-be.ni.com/bundle/labview-myrio-toolkit/raw/resource/enus/overview.html
- document_id: `labview-myrio-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The LabVIEW myRIO Toolkit provides tools for creating applications and deploying applications on the myRIO Student Embedded Device. The LabVIEW myRIO Toolkit is a software add-on for LabVIEW. The toolkit provides the necessary driver and the tools to quickly develop and deploy applications to the my

### LabVIEW myRIO Toolkit
 Overview

The LabVIEW myRIO Toolkit provides tools for
 creating applications and deploying applications on the myRIO Student Embedded
 Device.

The LabVIEW myRIO Toolkit is a software add-on
 for LabVIEW. The toolkit provides the necessary driver and the tools to quickly develop
 and deploy applications to the myRIO Student Embedded Device. The toolkit includes
 configuration-based Express and Advanced I/O VIs for each I/O type on the myRIO device.
 These VIs help students quickly prototype ideas and create stand-alone applications.

LabVIEW myRIO Toolkit

myRIO VIs

myRIO USB Monitor

Getting Started with myRIO

1. Launch LabVIEW.
2. Click the Set Up and Explore link.
3. Select Launch the Getting Started
 Wizard .

myRIO USB
 Monitor

myRIO I/O Monitor

1. Launch LabVIEW.
2. Click the Set Up and Explore link.
3. Select Launch the I/O Monitor .

myRIO USB
 Monitor

Templates and sample projects

File

»

Create Project

Create Project

Examples

LabVIEW myRIO Toolkit

labview\examples\myRIO

LabVIEW myRIO Toolkit

1. Select Help»Find Examples in LabVIEW.
2. Select Toolkits and Modules»myRIO in the Example Finder .

<!--NI_TOPIC bundle=labview-myrio-toolkit path=performing-textual-mathematics-and-algorithm.html language=enus -->
## TOPIC 00024: Performing Textual Mathematics and Algorithm Design with the LabVIEW myRIO Toolkit

- bundle_id: `labview-myrio-toolkit`
- source_path: `performing-textual-mathematics-and-algorithm.html`
- source_url: https://docs-be.ni.com/bundle/labview-myrio-toolkit/raw/resource/enus/performing-textual-mathematics-and-algorithm.html
- document_id: `labview-myrio-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The MathScript RT Module provides textual mathematics and algorithm design functionality in LabVIEW.Use the LabVIEW MathScript RT Module to develop .m files with an interactive command-line interface. You can deploy these .m files to the RT target on the myRIO. Integrate the MathScript RT Module mod

### Performing Textual Mathematics and Algorithm
 Design with the LabVIEW myRIO Toolkit

The MathScript RT Module provides textual mathematics and algorithm design
 functionality in LabVIEW.

Use the LabVIEW MathScript RT Module to develop .m files with an interactive
 command-line interface. You can deploy these .m files to the RT
 target on the myRIO.

Integrate the MathScript RT Module module with the LabVIEW Control Design and Simulation
 Module. This integration allows for textual mathematics and algorithm design in LabVIEW
 using the .m file syntax.

Parent topic:

LabVIEW myRIO Toolkit Using myRIO with Other NI Software

<!--NI_TOPIC bundle=labview-myrio-toolkit path=simulating-dynamic-systems.html language=enus -->
## TOPIC 00025: Simulating Dynamic Systems with the LabVIEW myRIO Toolkit

- bundle_id: `labview-myrio-toolkit`
- source_path: `simulating-dynamic-systems.html`
- source_url: https://docs-be.ni.com/bundle/labview-myrio-toolkit/raw/resource/enus/simulating-dynamic-systems.html
- document_id: `labview-myrio-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use myRIO with the LabVIEW Control Design and Simulation Module to simulate dynamic systems and design advanced controllers. Design controllers and estimators using both classical and state-space methods.To use the Control Design and Simulation VIs and functions, install the LabVIEW Control Design a

### Simulating Dynamic Systems with the LabVIEW myRIO Toolkit

Use myRIO with the LabVIEW Control Design and Simulation Module to simulate dynamic
 systems and design advanced controllers. Design controllers and estimators using both
 classical and state-space methods.

To use the Control Design and Simulation VIs and functions, install the LabVIEW Control Design
 and Simulation Module. After installation, select Control &
 Simulation from the Functions palette in
 LabVIEW.

Parent topic:

LabVIEW myRIO Toolkit Using myRIO with Other NI Software

Related information:

- Functions Palette

<!--NI_TOPIC bundle=labview-myrio-toolkit path=understanding-hysteresis.html language=enus -->
## TOPIC 00026: LabVIEW myRIO Toolkit Understanding Hysteresis

- bundle_id: `labview-myrio-toolkit`
- source_path: `understanding-hysteresis.html`
- source_url: https://docs-be.ni.com/bundle/labview-myrio-toolkit/raw/resource/enus/understanding-hysteresis.html
- document_id: `labview-myrio-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Hysteresis, also known as window size, adds a window above or below the trigger level. Hysteresis reduces false triggering due to noise or jitter in the signal.Use the Register Analog Input Interrupt VI or the Interrupt Express VI to generate analog input interrupts. Both VIs use a 0.02 V hysteresis

### LabVIEW myRIO Toolkit
 Understanding Hysteresis

Hysteresis, also known as window size, adds a window above or below the
 trigger level. Hysteresis reduces false triggering due to noise or jitter in the
 signal.

Use the Register Analog Input Interrupt VI or the Interrupt
 Express VI to generate analog input interrupts. Both VIs use a
 0.02 V hysteresis to
 prevent false interrupt registration. The hysteresis behavior
 depends on how you register the interrupt. You might register
 the interrupt on the falling edge or rising edge of the analog
 input signal. The following table describes the differences
 between the two methods:

| Type | Description |
| --- | --- |
| Analog Falling Edge | The signal starts or rises above the threshold plus hysteresis. The VI registers an interrupt when the signal drops below the threshold. |
| Analog Rising Edge | The signal starts below the threshold minus hysteresis. The VI registers an interrupt when the signal rises above the threshold. |

The following figure shows how the VI registers analog falling-edge interrupts:

Figure 7.

[IMAGE alt='Graph showing analog-falling-edge interrupts at trigger points.' src='GUID-36A5BE85-4D01-4D78-B2BC-794A7832D84D-a5.gif']

1. The signal rises above the threshold plus hysteresis. When the signal value drops below
 the threshold, the VI registers an interrupt.
2. The signal stays below the threshold plus hysteresis since the VI last registered an
 interrupt. The VI does not register any interrupts.
3. The signal rises above the threshold plus hysteresis. When the signal drops below the
 threshold, the VI registers another interrupt.

The following figure shows how the VI registers analog rising-edge interrupts:

Figure 8.

[IMAGE alt='Graph showing analog rising-edge interrupts with threshold and trigger points.' src='GUID-3DE5841C-8641-42EE-B46F-E63496A01F04-a5.gif']

1. The VI registers an interrupt when the signal value rises above the threshold.
2. The signal stays above the threshold minus hysteresis since the VI last registered an
 interrupt. The VI does not register any interrupts.
3. The signal drops below the threshold minus hysteresis. When the signal crosses above the
 threshold, the VI registers another interrupt.

Parent topic:

Creating myRIO Applications with the LabVIEW myRIO Toolkit

<!--NI_TOPIC bundle=labview-myrio-toolkit path=understanding-latency.html language=enus -->
## TOPIC 00027: LabVIEW myRIO Toolkit Understanding Latency

- bundle_id: `labview-myrio-toolkit`
- source_path: `understanding-latency.html`
- source_url: https://docs-be.ni.com/bundle/labview-myrio-toolkit/raw/resource/enus/understanding-latency.html
- document_id: `labview-myrio-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Latency is the time required to complete an operation. When you use the myRIO Express VIs to acquire or generate signals, latency has different meanings. Latency in Signal AcquisitionLatency in signal acquisition is the time myRIO needs to transfer the acquired signal to the real-time processor. In

### LabVIEW myRIO Toolkit
 Understanding Latency

Latency is the time required to complete an operation. When you use the myRIO
 Express VIs to acquire or generate signals, latency has different meanings.

#### Latency in Signal
 Acquisition

Latency in signal acquisition is the time myRIO needs to transfer the
 acquired signal to the real-time processor. In the n samples mode,
 latency includes the software or memory transfer that places the signal into the correct
 memory. Latency also includes the transfer required to deliver the signal to the
 algorithm.

When using myRIO Express VIs for signal acquisition in the
 n samples mode, latency is the time required to complete the following
 tasks:

DMA read operation

Data copying

Note

#### Latency in Signal
 Generation

Latency in signal generation is the time myRIO needs to export the
 acquired signal to another Data Acquisition (DAQ) device. In the n
 samples mode, latency includes the software or memory transfer that gets the signal from the
 algorithm. Latency also includes the transfer required to deliver the signal into the
 correct memory.

When using myRIO Express VIs to perform signal generation in the
 n samples mode, the following processes result in latency:

Data copying

DMA write operation

Interrupt processing

n

n

The actual latency depends on whether you check the Wait until
 done? checkbox on the Express VIs, as follows:

- The following figure shows the latency in signal generation when you check the
 Wait until done? checkbox: Figure 9.Latency in Signal Generation with
 Wait until done checked
 
 [IMAGE alt='Diagram showing latency in signal generation with Wait until done? checked.' src='GUID-FE600CC0-2F5E-41BF-B7EE-DC5F377D55C1-a5.gif'] In this case, latency is the time needed to complete the data copying, DMA write
 operation, and interrupt processing.
- The following figures show the latency in signal generation when you do not check the
 Wait until done? checkbox: Figure 10.Latency in Signal Generation
 Without Wait until done checked
 
 [IMAGE alt='Diagram of latency in signal generation without Wait until done? checked.' src='GUID-8D790D83-B85A-4218-A6DF-73C657BFF462-a5.gif'] In this case, RT continuously writes signal values from the algorithm to the
 real-time buffer. At the same time, RT transfers the values from the real-time buffer to
 the FPGA buffer in another loop. Therefore, latency refers to the time required to
 complete the DMA write operation and interrupt processing. This latency is typically 400 µs .

Parent topic:

Creating myRIO Applications with the LabVIEW myRIO Toolkit

Related concepts:

- LabVIEW myRIO Toolkit 1 Sample Versus N Samples Modes

<!--NI_TOPIC bundle=labview-myrio-toolkit path=user-manual-welcome.html language=enus -->
## TOPIC 00028: LabVIEW myRIO Toolkit User Manual

- bundle_id: `labview-myrio-toolkit`
- source_path: `user-manual-welcome.html`
- source_url: https://docs-be.ni.com/bundle/labview-myrio-toolkit/raw/resource/enus/user-manual-welcome.html
- document_id: `labview-myrio-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The LabVIEW myRIO Toolkit User Manual provides detailed descriptions of the product functionality and the step by step processes for use. Looking for Something Else?For information not found in the User Manual for your product, such as specifications and API reference, browse Related Information.

### LabVIEW myRIO Toolkit
 User Manual

The LabVIEW myRIO Toolkit User Manual provides detailed
 descriptions of the product functionality and the step by step processes for use.

#### Looking for Something Else?

For information not found in the User Manual
 for your product, such as specifications and API reference, browse *Related
 Information*.

Related information:

- Hardware and Software Operating System Compatibility
- Interactive Activation Guide
- Software and Driver Downloads
- Release Notes
- Learning Center
- Discussion Forums

<!--NI_TOPIC bundle=labview-myrio-toolkit path=using-callback-vis-to-handle-interrupts.html language=enus -->
## TOPIC 00029: Using Callback VIs to Handle Interrupts with the LabVIEW myRIO Toolkit

- bundle_id: `labview-myrio-toolkit`
- source_path: `using-callback-vis-to-handle-interrupts.html`
- source_url: https://docs-be.ni.com/bundle/labview-myrio-toolkit/raw/resource/enus/using-callback-vis-to-handle-interrupts.html
- document_id: `labview-myrio-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Create and edit callback VIs for interrupt handling, considering their characteristics.An interrupt is a signal that indicates an event requiring immediate attention. Use interrupts to notify the target of a high-priority condition requiring the interruption of the currently executing block diagram

### Using Callback VIs to Handle Interrupts with
 the LabVIEW myRIO Toolkit

Create and edit callback VIs for interrupt handling, considering their
 characteristics.

An interrupt is a signal that indicates an event requiring immediate attention. Use interrupts to
 notify the target of a high-priority condition requiring the interruption of the
 currently executing block diagram code. To trigger an interrupt, use the
 Interrupt Express VI or Interrupt Low Level
 VIs.

Use callback VIs to handle interrupts. The Callback VI contains code that
 handles interrupts and runs when the interrupt triggering occurs.

#### Features
 of Callback VIs

Callback VIs have the following features:

- Callback VIs have a time-critical priority, which is the highest priority in
 block diagram code on RT targets. The priority of callback VIs is higher than
 any Timed Loops on RT targets. To prevent unexpected
 timing behavior, do not add a Timed Loop to the block
 diagram of callback VIs.
- Use callback VIs to unregister or disable interrupts. When you unregister or
 disable an interrupt, the interrupt triggering stops. Disabling an interrupt
 also releases the resources associated with the interrupt.
- Use global variables or function global variables to communicate between a
 callback VI and a non-callback VI. These variables help access and pass data
 among VIs.
- A callback VI can use one or two CPUs, as described in the following table:

| Scenario | Use Case | Note |
| --- | --- | --- |
| One CPU Used | The block diagram of the callback VI includes only one While Loop. This loop does not contain pieces of code running in parallel. | The non-callback code keeps executing when the callback VI runs. |
| Two CPUs Used | The following cases exist: The block diagram of the callback VI includes two While Loops. Each CPU executes the code running in one While Loop. The block diagram code of the callback VI contains one While Loop. This loop contains two pieces of code that execute in parallel. | The non-callback code stops execution until the callback VI completes and frees up one CPU.Using two CPUs for an extended period might disconnect the host computer from the target. Maintaining this connection requires using the CPU of the target. Note The manufacturer recommends the use of callback VIs to execute short code that handles emergent events. |

Parent topic:

Creating myRIO Applications with the LabVIEW myRIO Toolkit

Related tasks:

- Creating a Callback VI with the LabVIEW myRIO Toolkit
- Opening a Callback VI with the LabVIEW myRIO Toolkit

Related information:

- Global Variables

<!--NI_TOPIC bundle=labview-myrio-toolkit path=using-myrio-with-other-ni-software.html language=enus -->
## TOPIC 00030: LabVIEW myRIO Toolkit Using myRIO with Other NI Software

- bundle_id: `labview-myrio-toolkit`
- source_path: `using-myrio-with-other-ni-software.html`
- source_url: https://docs-be.ni.com/bundle/labview-myrio-toolkit/raw/resource/enus/using-myrio-with-other-ni-software.html
- document_id: `labview-myrio-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following sections contain information about creating applications on the myRIO with the LabVIEW myRIO Toolkit and other NI software.

### LabVIEW myRIO Toolkit Using
 myRIO with Other NI Software

The following sections contain information about creating applications on the myRIO
 with the LabVIEW myRIO Toolkit and other NI
 software.

- [Acquiring and Processing Images with the LabVIEW myRIO Toolkit](acquiring-and-processing-images.html) Connect a USB camera to the USB host port on the myRIO to acquire and process images.
- [LabVIEW myRIO Toolkit Communicating with Serial Devices Using VISA](communicating-with-serial-devices-using-visa.html) Install NI-VISA to communicate with serial devices that you connect to the myRIO device.
- [Creating Feedback Control Systems with the LabVIEW myRIO Toolkit](creating-feedback-control-systems.html) Use myRIO with the PID VIs to create feedback control systems to control, for example, motors, temperature, and pressure.
- [LabVIEW myRIO Toolkit Creating Robotics Applications](creating-robotics-applications.html) Use myRIO with the Robotics Module for LabRIO to develop and deploy robotics applications, such as steering, path planning, obstacle avoidance, and inverse kinematics.
- [Performing Textual Mathematics and Algorithm Design with the LabVIEW myRIO Toolkit](performing-textual-mathematics-and-algorithm.html) The MathScript RT Module provides textual mathematics and algorithm design functionality in LabVIEW.
- [Simulating Dynamic Systems with the LabVIEW myRIO Toolkit](simulating-dynamic-systems.html) Use myRIO with the LabVIEW Control Design and Simulation Module to simulate dynamic systems and design advanced controllers. Design controllers and estimators using both classical and state-space methods.

<!--NI_TOPIC bundle=labview-myrio-toolkit path=using-the-project-explorer-window.html language=enus -->
## TOPIC 00031: Using the Project Explorer Window with the LabVIEW myRIO Toolkit

- bundle_id: `labview-myrio-toolkit`
- source_path: `using-the-project-explorer-window.html`
- source_url: https://docs-be.ni.com/bundle/labview-myrio-toolkit/raw/resource/enus/using-the-project-explorer-window.html
- document_id: `labview-myrio-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the Project Explorer window to manage targets, VIs, and support files in LabVIEW projects. Connect myRIO targets to the host computer, set target properties, and deploy VIs to targets in Project Explorer.The following figure shows the Project Explorer window after you add a myRIO target to a Lab

### Using the Project Explorer Window with the LabVIEW myRIO Toolkit

Use the Project Explorer window to manage targets, VIs, and
 support files in LabVIEW projects. Connect myRIO targets to the host computer, set target
 properties, and deploy VIs to targets in Project
 Explorer.

The following figure shows the Project Explorer window after you add a
 myRIO target to a LabVIEW project:

Figure 11.

[IMAGE alt='LabVIEW Project Explorer window with a myRIO target added.' src='GUID-43BC09A8-3890-4199-A36B-52DD9EE24BA5-a5.svg']

1. Project Root —Contains the host computer and the myRIO target
 you added to the current project. The label on the project root includes the
 filename for the project. To add more myRIO targets to the project, right-click
 the project root and select New»Targets and Devices from the shortcut menu.
2. My Computer —Represents the local or host computer as a target
 in the project.
3. Build Specifications —Includes build configurations for source
 distributions and other types of builds available in LabVIEW toolkits and
 modules.
4. RT Target —Represents the myRIO target you added to the project. VIs
 and libraries that you add to a myRIO target display under this target. To
 configure the settings of a myRIO target, right-click the target and select
 Properties from the shortcut menu. Right-click
 the myRIO target and select different options to perform the following tasks:
 Switch between FPGA personalities
 Create a callback VI from templates
 Launch the Getting Started with myRIO wizard
 Launch the myRIO I/O Monitor
5. FPGA Target —Represents the FPGA target on the myRIO. To add the FPGA
 target under the RT target, right-click the chassis under the myRIO target. Then,
 select New»FPGA Target from the shortcut menu. Note 
 After adding an FPGA target under the chassis, you must use an FPGA bitfile with
 the myRIO VIs.
6. Build Specifications —Includes specifications for building
 source distributions, stand-alone real-time applications, and zip files. If you
 have LabVIEW Professional Development System or
 Application Builder installed, you can create a build
 specification here. Right-click Build Specifications and
 select New»Real-Time Application from the shortcut menu to create a build specification. The build
 specification defines how to build stand-alone real-time applications.

Parent topic:

Creating myRIO Applications with the LabVIEW myRIO Toolkit

Related concepts:

- Choosing FPGA Personalities with the LabVIEW myRIO Toolkit
- Using Callback VIs to Handle Interrupts with the LabVIEW myRIO Toolkit

Related information:

- Managing a Project in LabVIEW
- Adding RT Targets to a LabVIEW Project
- Creating Stand-Alone Real-Time Applications
- Real-Time Target
