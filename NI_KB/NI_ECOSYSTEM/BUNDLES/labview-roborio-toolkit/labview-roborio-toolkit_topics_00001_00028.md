# NI DOCUMENT BUNDLE: labview-roborio-toolkit

<!--NI_BUNDLE_CHUNK bundle=labview-roborio-toolkit start=1 end=28 -->
<!--NI_TOPIC bundle=labview-roborio-toolkit path=roboriohelp/roborio_comm_rt.html language=enus -->
## TOPIC 00001: Communicating with RT Targets from a Host Computer (roboRIO Toolkit)

- bundle_id: `labview-roborio-toolkit`
- source_path: `roboriohelp/roborio_comm_rt.html`
- source_url: https://docs-be.ni.com/bundle/labview-roborio-toolkit/raw/resource/enus/roboriohelp/roborio_comm_rt.html
- document_id: `labview-roborio-toolkit`
- page_type: `leaf`
- content_type: ``

### Communicating with RT Targets from a Host Computer (roboRIO Toolkit)

Use the following table to learn about the methods that you can use to communicate with roboRIO targets from a host computer.

|  | Network Communication | Front Panel Communication |
| --- | --- | --- |
| Description | A host VI runs on the host computer and communicates with the VI running on the RT target using specific network communication programmatic controls. | LabVIEW and the RT Engine execute different parts of the same VI. LabVIEW on the host computer displays the front panel of the VI while the RT Engine executes the block diagram. |
| Use Case | Customizing the code of the VIs respectively running on the host computer and on the RT target. Controlling the data that the host computer and the RT target send to each other. | Monitoring the VIs running on an RT target. |
| Example | Refer to the Network Communication sample project for examples of creating different types of network communication systems using the roboRIO. Access this sample project by selecting File»Create Project in LabVIEW and selecting Sample Projects»roboRIO. | None. |

**Related Information**

[Real-Time System Components](/csh?topicname=lvrtconcepts/real-time_system_components.html)

<!--NI_TOPIC bundle=labview-roborio-toolkit path=roboriohelp/roborio_configuring.html language=enus -->
## TOPIC 00002: Configuring roboRIO (roboRIO Toolkit)

- bundle_id: `labview-roborio-toolkit`
- source_path: `roboriohelp/roborio_configuring.html`
- source_url: https://docs-be.ni.com/bundle/labview-roborio-toolkit/raw/resource/enus/roboriohelp/roborio_configuring.html
- document_id: `labview-roborio-toolkit`
- page_type: `leaf`
- content_type: ``

### Configuring roboRIO (roboRIO Toolkit)

Use the following topics to learn about connecting the roboRIO to a host computer and installing software on the roboRIO:

- Connecting roboRIO to a Host Computer
- Installing Software on roboRIO

|  | To view related topics, click the Locate button, shown at left, in the toolbar at the top of this window. The LabVIEW Help highlights this topic in the Contents tab so you can navigate the related topics. |
| --- | --- |

<!--NI_TOPIC bundle=labview-roborio-toolkit path=roboriohelp/roborio_connector_pinouts.html language=enus -->
## TOPIC 00003: I/O Connectors (roboRIO Toolkit)

- bundle_id: `labview-roborio-toolkit`
- source_path: `roboriohelp/roborio_connector_pinouts.html`
- source_url: https://docs-be.ni.com/bundle/labview-roborio-toolkit/raw/resource/enus/roboriohelp/roborio_connector_pinouts.html
- document_id: `labview-roborio-toolkit`
- page_type: `leaf`
- content_type: ``

### I/O Connectors (roboRIO Toolkit)

The following table lists the pinouts of the I/O connectors on the roboRIO.

| Port | Pinout |
| --- | --- |
| myRIO Expansion Port (MXP) |  |
| CAN |  |
| I2C |  |
| RS-232 |  |
| DIO |  |
| RSL |  |
| RELAY |  |
| ANALOG IN |  |
| PWM |  |
| SPI |  |

<!--NI_TOPIC bundle=labview-roborio-toolkit path=roboriohelp/roborio_create_applications.html language=enus -->
## TOPIC 00004: Creating roboRIO Applications (roboRIO Toolkit)

- bundle_id: `labview-roborio-toolkit`
- source_path: `roboriohelp/roborio_create_applications.html`
- source_url: https://docs-be.ni.com/bundle/labview-roborio-toolkit/raw/resource/enus/roboriohelp/roborio_create_applications.html
- document_id: `labview-roborio-toolkit`
- page_type: `leaf`
- content_type: ``

### Creating roboRIO Applications (roboRIO Toolkit)

Use the following topics to learn about the roboRIO programming concepts that are helpful for creating a roboRIO application:

- Choosing between Express VIs and Low Level VIs
- Communicating with RT Targets from a Host Computer
- Deploying Real-Time Applications
- Generating FPGA Clocks
- Understanding FPGA Personalities
- Understanding Hysteresis
- Using Callback VIs to Handle Interrupts
- Using the Project Explorer Window

|  | To view related topics, click the Locate button, shown at left, in the toolbar at the top of this window. The LabVIEW Help highlights this topic in the Contents tab so you can navigate the related topics. |
| --- | --- |

<!--NI_TOPIC bundle=labview-roborio-toolkit path=roboriohelp/roborio_datadb_apps.html language=enus -->
## TOPIC 00005: Visualizing Data on a Mobile Device (roboRIO Toolkit)

- bundle_id: `labview-roborio-toolkit`
- source_path: `roboriohelp/roborio_datadb_apps.html`
- source_url: https://docs-be.ni.com/bundle/labview-roborio-toolkit/raw/resource/enus/roboriohelp/roborio_datadb_apps.html
- document_id: `labview-roborio-toolkit`
- page_type: `leaf`
- content_type: ``

### Visualizing Data on a Mobile Device (roboRIO Toolkit)

You can install the Data Dashboard for LabVIEW app on an iPad or Android device to visualize the data that you acquire on the roboRIO. Use this app to create a custom dashboard to control and monitor your LabVIEW application remotely. You can access data using secure LabVIEW web services and share dashboards with others from your iPad or Android device.

Visit ni.com/info and enter the Info Code ext3du to learn more about Data Dashboard for LabVIEW.

<!--NI_TOPIC bundle=labview-roborio-toolkit path=roboriohelp/roborio_dio_lines.html language=enus -->
## TOPIC 00006: DIO Lines (roboRIO Toolkit)

- bundle_id: `labview-roborio-toolkit`
- source_path: `roboriohelp/roborio_dio_lines.html`
- source_url: https://docs-be.ni.com/bundle/labview-roborio-toolkit/raw/resource/enus/roboriohelp/roborio_dio_lines.html
- document_id: `labview-roborio-toolkit`
- page_type: `leaf`
- content_type: ``

### DIO Lines (roboRIO Toolkit)

The lines for the digital inputs and outputs on the roboRIO are not limited to those on the DIO port. Multiple ports contain DIO lines and use different voltages. The following table lists the voltages on the DIO lines for different ports.

| Voltage | Ports |
| --- | --- |
| 3.3 V | DIO, I2C, SPI, and MXP |
| 5 V | PWM and RELAY |

<!--NI_TOPIC bundle=labview-roborio-toolkit path=roboriohelp/roborio_evi_avi.html language=enus -->
## TOPIC 00007: Choosing between Express VIs and Low Level VIs (roboRIO Toolkit)

- bundle_id: `labview-roborio-toolkit`
- source_path: `roboriohelp/roborio_evi_avi.html`
- source_url: https://docs-be.ni.com/bundle/labview-roborio-toolkit/raw/resource/enus/roboriohelp/roborio_evi_avi.html
- document_id: `labview-roborio-toolkit`
- page_type: `leaf`
- content_type: ``

### Choosing between Express VIs and Low Level VIs (roboRIO Toolkit)

The LabVIEW roboRIO Toolkit provides the following types of VIs for creating roboRIO applications:

- Express VIs —Use the Express VIs to interactively configure the settings for the I/O channels. When you place an Express VI on the block diagram or double-click an Express VI, a configuration dialog box appears. Use this configuration dialog box to configure the Express VI. You can also configure the Express VI by wiring values to the terminals of the Express VI on the block diagram.
- Low Level VIs —Use the Low Level VIs to have more control over allocating and releasing I/O channels.

#### Understanding the Underlying Code of Express VIs

In the configuration dialog box of an Express VI, click the **View Code** tab to view the underlying code of the Express VI. This code consists of the Low Level VIs and other LabVIEW VIs.

The code of the Express VIs uses Smart Open VIs instead of the Open VIs to open references to I/O channels. Smart Open VIs can open an I/O reference the first time they run and then save the reference in memory. The use of Smart Open VIs ensures that the Express VIs can run efficiently in loops because you do not need to open references to I/O channels for each iteration.

You can copy the code of an Express VI to a new block diagram and start programming with the Low Level VIs. After you copy the code, replace the Smart Open VI with an Open VI because the Open VIs open an I/O reference and pass the reference around to all other places where you need to access the I/O channel. You also need to add a Close VI to close I/O references after data operation. The following figure shows an example of modifying the code copied from the Analog Input Express VI.

[IMAGE alt='image' src='noloc_bd_myrioexpresscode.gif']

**Related Information**

[Express VIs](/csh?topicname=lvconcepts/expressvis.html)

<!--NI_TOPIC bundle=labview-roborio-toolkit path=roboriohelp/roborio_fpga_clock.html language=enus -->
## TOPIC 00008: Generating FPGA Clocks (roboRIO Toolkit)

- bundle_id: `labview-roborio-toolkit`
- source_path: `roboriohelp/roborio_fpga_clock.html`
- source_url: https://docs-be.ni.com/bundle/labview-roborio-toolkit/raw/resource/enus/roboriohelp/roborio_fpga_clock.html
- document_id: `labview-roborio-toolkit`
- page_type: `leaf`
- content_type: ``

### Generating FPGA Clocks (roboRIO Toolkit)

The FPGA target on the hardware has a clock rate of 40 MHz, which means the clock cycle is 25 ns. To generate a frequency that is less than 40 MHz, you can change a signal on every *x* number of rising edges of the clock signal. The following figure shows an example of changing a 40 MHz clock signal on rising edges to generate 20 MHz and 10 MHz clock signals, respectively.

[IMAGE alt='image' src='noloc_eps_fpgaclockfrequency.gif']

In the previous figure, you toggle the clock signal on every rising edge to generate the 20 MHz clock signal and toggle the clock signal on every other rising edge to generate the 10 MHz clock signal.

The frequency to generate on the hardware must meet the following requirements:

- The frequency must be divisible by 25 ns because the clock cycle is 25 ns and you count the number of rising edges to make changes. For example, you cannot generate a frequency of 25 MHz. The first achievable frequency below 40 MHz is 20 MHz.
- The frequency must be within the range of approximately 610.35 Hz to 40 MHz. The hardware uses a 16-bit counter that counts from 0 to 65,535. You can calculate the lowest achievable frequency by the equation 1/(25 ns * 65536) ≈ 610.35 Hz.

You can use clock divisors to generate even lower frequencies for different I/O types. You can divide the base frequency by even numbers and use the generated clock to increment the counter. For example, with a clock divisor of 2, the lowest achievable frequency is 1/(50 ns * 65536) ≈ 305.17 Hz.

The following equation calculates frequencies that you can generate for pulse width modulation (PWM) I/O.

*f*
 <sub>PWM</sub> = *f*
 <sub>clk</sub> / (*N* * [*X* + 1])

| where | fPWM is the desired PWM frequency |
| --- | --- |
|  | fclk is the base clock frequency |
|  | N is the clock divisor |
|  | X is the number of counts before changing the signal |

The following equation calculates frequencies that you can generate for serial peripheral interface (SPI) I/O.

*f*
 <sub>SPI</sub> = *f*
 <sub>clk</sub> / (2 * *N* * [*X* + 1])

| where | fSPI is the desired SPI frequency |
| --- | --- |
|  | fclk is the base clock frequency |
|  | N is the clock divisor |
|  | X is the number of counts before changing the signal |

Some Express VIs include a **Validate** button for validating whether these Express VIs can generate the frequency that you specify. If you specify an invalid value for **Frequency**, the Express VIs coerce the specified value to the nearest valid value when you click the **Validate** button.

<!--NI_TOPIC bundle=labview-roborio-toolkit path=roboriohelp/roborio_fpga_personalities.html language=enus -->
## TOPIC 00009: Understanding FPGA Personalities (roboRIO Toolkit)

- bundle_id: `labview-roborio-toolkit`
- source_path: `roboriohelp/roborio_fpga_personalities.html`
- source_url: https://docs-be.ni.com/bundle/labview-roborio-toolkit/raw/resource/enus/roboriohelp/roborio_fpga_personalities.html
- document_id: `labview-roborio-toolkit`
- page_type: `leaf`
- content_type: ``

### Understanding FPGA Personalities (roboRIO Toolkit)

FPGA personalities consist of predefined FPGA bitfiles for you to program with roboRIO. The LabVIEW roboRIO Toolkit provides a default FPGA personality. The default FPGA personality supports general I/O, protocols, and interrupt. Use the default personality for control applications.

|  | Note You can also create customized FPGA personality to fit your application needs. |
| --- | --- |

The following table lists the functionalities, channels names, and channel numbers that the default FPGA personality supports.

| Supported Functionalities | Number of Supported Channels | Name of Supported Channels |
| --- | --- | --- |
| Analog Input | 8 | B/AI0~B/AI3AI/AI0~AI/AI3 |
| Analog Output | 2 | B/AO0, B/AO1 |
| Digital Input | 30 | B/DIO0~B/DIO15DIO/DIO0~DIO/DIO9SPI/CS0~SPI/CS3 |
| Digital Output | 30 | B/DIO0~B/DIO15DIO/DIO0~DIO/DIO9SPI/CS0~SPI/CS3 |
| RSL | 1 | RSL |
| Relay | 4 | RELAY/RELAY0~RELAY/RELAY3 |
| Button | 1 | Button |
| LED | 6 | RADIO (Green), RADIO (Red)COMM (Green), COMM (Red)MODE (Green), MODE (Red) |
| Accelerometer | 3 | X-Axis, Y-Axis, Z-Axis |
| PWM | 13 | B/PWM0~B/PWM2PWM/PWM0~PWM/PWM9 |
| Encoder | 6 | B/ENCDIO/ENC0~DIO/ENC4 |
| SPI | 2 | B/SPISPI/SPI |
| I2C | 2 | B/I2CI2C/I2C |
| UART | 2 | B/UARTRS-232 |
| CAN | 1 | CAN |
| Interrupt | 8 | B/AI0 (Interrupt)~B/AI1 (Interrupt)B/DIO0 (Interrupt)~B/DIO3 (Interrupt)Button0 (Interrupt)Timer (Interrupt) |

**Related Information**

roboRIO Shipping Personality Reference

roboRIO User Manual

roboRIO Specifications

[I/O Connectors](../roboriohelp/roborio_connector_pinouts.html)

<!--NI_TOPIC bundle=labview-roborio-toolkit path=roboriohelp/roborio_get_started.html language=enus -->
## TOPIC 00010: Getting Started with the roboRIO Toolkit (roboRIO Toolkit)

- bundle_id: `labview-roborio-toolkit`
- source_path: `roboriohelp/roborio_get_started.html`
- source_url: https://docs-be.ni.com/bundle/labview-roborio-toolkit/raw/resource/enus/roboriohelp/roborio_get_started.html
- document_id: `labview-roborio-toolkit`
- page_type: `leaf`
- content_type: ``

### Getting Started with the roboRIO Toolkit (roboRIO Toolkit)

Use the following steps to get started using the roboRIO with the roboRIO Toolkit for developing your roboRIO applications. Select a topic in each step to help you get started.

1. Install Software and Drivers for Your roboRIO Application
  - LabVIEW roboRIO Toolkit Readme
  - LabVIEW roboRIO Software Bundle Readme
  - Using roboRIO with Other NI Software
2. Connect and Set Up the roboRIO
  - Wiring Power to the roboRIO
  - Connecting roboRIO to a Host Computer
  - Using the Getting Started with roboRIO Wizard
  - Installing Software on roboRIO
  - Using the roboRIO I/O Monitor
3. Learn roboRIO Programming
  - Tutorials on Getting Started with roboRIO Programming
  - Concepts in roboRIO Programming
4. Create Your roboRIO Application
  - Using roboRIO Templates and Sample Projects
  - Using roboRIO Examples
  - Using roboRIO VIs
  - Creating roboRIO Applications
  - Using roboRIO with Other NI Software

<!--NI_TOPIC bundle=labview-roborio-toolkit path=roboriohelp/roborio_hardware_bd.html language=enus -->
## TOPIC 00011: Block Diagram (roboRIO Toolkit)

- bundle_id: `labview-roborio-toolkit`
- source_path: `roboriohelp/roborio_hardware_bd.html`
- source_url: https://docs-be.ni.com/bundle/labview-roborio-toolkit/raw/resource/enus/roboriohelp/roborio_hardware_bd.html
- document_id: `labview-roborio-toolkit`
- page_type: `leaf`
- content_type: ``

### Block Diagram (roboRIO Toolkit)

The following figure shows the hardware block diagram of the roboRIO.

[IMAGE alt='image' src='noloc_eps_roborio_bd.gif']

<!--NI_TOPIC bundle=labview-roborio-toolkit path=roboriohelp/roborio_hardware_overview.html language=enus -->
## TOPIC 00012: roboRIO Hardware Overview (roboRIO Toolkit)

- bundle_id: `labview-roborio-toolkit`
- source_path: `roboriohelp/roborio_hardware_overview.html`
- source_url: https://docs-be.ni.com/bundle/labview-roborio-toolkit/raw/resource/enus/roboriohelp/roborio_hardware_overview.html
- document_id: `labview-roborio-toolkit`
- page_type: `leaf`
- content_type: ``

### roboRIO Hardware Overview (roboRIO Toolkit)

Use the following topics to understand basic information about the roboRIO hardware:

- Block Diagram
- DIO Lines
- I/O Connectors
- Power Supply

|  | To view related topics, click the Locate button, shown at left, in the toolbar at the top of this window. The LabVIEW Help highlights this topic in the Contents tab so you can navigate the related topics. |
| --- | --- |

<!--NI_TOPIC bundle=labview-roborio-toolkit path=roboriohelp/roborio_hysteresis.html language=enus -->
## TOPIC 00013: Understanding Hysteresis (roboRIO Toolkit)

- bundle_id: `labview-roborio-toolkit`
- source_path: `roboriohelp/roborio_hysteresis.html`
- source_url: https://docs-be.ni.com/bundle/labview-roborio-toolkit/raw/resource/enus/roboriohelp/roborio_hysteresis.html
- document_id: `labview-roborio-toolkit`
- page_type: `leaf`
- content_type: ``

### Understanding Hysteresis (roboRIO Toolkit)

Hysteresis, also known as window size, adds a window above or below the trigger level. Hysteresis reduces false triggering due to noise or jitter in the signal.

When you use the Register Analog Input Interrupt VI or the Interrupt Express VI to generate analog input interrupts, both of these VIs use a 0.02 V hysteresis to avoid false interrupt registration. The way this hysteresis works depends on whether you register an interrupt on the falling edge or rising edge of the analog input signal, as described in the following table.

| Type | Description |
| --- | --- |
| Analog Falling Edge | The VI registers an interrupt when the signal starts or rises above Threshold plus hysteresis and then drops below Threshold. |
| Analog Rising Edge | The VI registers an interrupt when the signal starts below Threshold minus hysteresis and then crosses above Threshold. |

Use the following figure to understand when the VI registers analog-falling-edge interrupts.

[IMAGE alt='image' src='noloc_fp_interrupt_hysteresis_falling_edge.gif']

The following list describes important details about the previous figure:

|  | The signal rises above Threshold plus hysteresis. When the signal value drops below Threshold, the VI registers an interrupt. |
| --- | --- |
|  | The VI does not register any interrupt, because the signal stays below Threshold plus hysteresis since the VI last registered an interrupt. |
|  | The signal rises above Threshold plus hysteresis. When the signal drops below Threshold, the VI registers another interrupt. |

Use the following figure to understand when the VI registers analog-rising-edge interrupts.

[IMAGE alt='image' src='noloc_fp_interrupt_hysteresis_rising_edge.gif']

The following list describes important details about the previous figure:

|  | The VI registers an interrupt when the signal value rises above Threshold. |
| --- | --- |
|  | The VI does not register any interrupt, because the signal stays above Threshold minus hysteresis since the VI last registered an interrupt. |
|  | The signal drops below Threshold minus hysteresis. When the signal crosses above Threshold, the VI registers another interrupt. |

**Related Information**

[Interrupt Express VI](/csh?topicname=myrioreference/myrioref_exp_irq.html)

[Register Analog Input Interrupt VI](/csh?topicname=myrioreference/myrioref_register_ai_irq.html)

<!--NI_TOPIC bundle=labview-roborio-toolkit path=roboriohelp/roborio_install_sw.html language=enus -->
## TOPIC 00014: Installing Software on roboRIO (roboRIO Toolkit)

- bundle_id: `labview-roborio-toolkit`
- source_path: `roboriohelp/roborio_install_sw.html`
- source_url: https://docs-be.ni.com/bundle/labview-roborio-toolkit/raw/resource/enus/roboriohelp/roborio_install_sw.html
- document_id: `labview-roborio-toolkit`
- page_type: `leaf`
- content_type: ``

### Installing Software on roboRIO (roboRIO Toolkit)

When you run the **Getting Started with roboRIO** wizard, LabVIEW installs the recommended software set on the roboRIO. You can also use Measurement & Automation Explorer (MAX) to manually install software on the roboRIO.

Complete the following steps to install software on the roboRIO using MAX:

1. In MAX, expand Remote Systems in the configuration tree and then expand your roboRIO target.
2. Right-click Software and click Add/Remove Software to launch LabVIEW Real-Time Software Wizard .
3. Select the recommended software set for the roboRIO.
4. Click Next .
5. Click roboRIO 
 *x* , where x matches the version of the LabVIEW roboRIO Toolkit.
6. Click Next to view a summary of your selection.
7. Click Next to start installing the software. When the installation completes, the wizard restarts the roboRIO.
8. Click Finish to close the wizard.

**Related Information**

[Getting Started with roboRIO Wizard](../roboriohelp/roboriohelp.html)

<!--NI_TOPIC bundle=labview-roborio-toolkit path=roboriohelp/roborio_interactive_headless.html language=enus -->
## TOPIC 00015: Deploying Real-Time Applications (roboRIO Toolkit)

- bundle_id: `labview-roborio-toolkit`
- source_path: `roboriohelp/roborio_interactive_headless.html`
- source_url: https://docs-be.ni.com/bundle/labview-roborio-toolkit/raw/resource/enus/roboriohelp/roborio_interactive_headless.html
- document_id: `labview-roborio-toolkit`
- page_type: `leaf`
- content_type: ``

### Deploying Real-Time Applications (roboRIO Toolkit)

After you build a real-time application for the roboRIO, you need to deploy the application to the RT target on the roboRIO. Use one of the following methods to deploy real-time applications:

- Interactive Deployment —Deploys real-time applications from the Project Explorer window. Interactive deployment requires that the RT target stays connected to the LabVIEW development environment. In the Project Explorer window, you can run VIs on the RT target by clicking Run . LabVIEW compiles the VIs and their dependencies and deploys the application to the RT target.
- Headless Deployment —Deploys real-time applications from outside of the LabVIEW development environment, such as C programming. Use this method to programmatically deploy to targets or when you do not have access to LabVIEW.

**Related Information**

[Building and Deploying a Stand-Alone Real-Time Application](/csh?topicname=lvrthowto/rt_building_rt_app.html)

<!--NI_TOPIC bundle=labview-roborio-toolkit path=roboriohelp/roborio_mathscript_apps.html language=enus -->
## TOPIC 00016: Performing Textual Mathematics and Algorithm Design (roboRIO Toolkit)

- bundle_id: `labview-roborio-toolkit`
- source_path: `roboriohelp/roborio_mathscript_apps.html`
- source_url: https://docs-be.ni.com/bundle/labview-roborio-toolkit/raw/resource/enus/roboriohelp/roborio_mathscript_apps.html
- document_id: `labview-roborio-toolkit`
- page_type: `leaf`
- content_type: ``

### Performing Textual Mathematics and Algorithm Design (roboRIO Toolkit)

You can use the LabVIEW MathScript RT Module to develop .m files with an interactive command-line interface and deploy .m files to the RT target on the roboRIO. When you integrate this module with the LabVIEW Control Design and Simulation Module, you can perform textual mathematics and algorithm design in LabVIEW using the .m file syntax.

Visit ni.com/info and enter the Info Code exccik to learn more about the MathScript RT Module. Visit ni.com/info and enter the Info Code exu7rq to learn more about the Control Design and Simulation Module.

<!--NI_TOPIC bundle=labview-roborio-toolkit path=roboriohelp/roborio_ni_software.html language=enus -->
## TOPIC 00017: Using roboRIO with Other NI Software (roboRIO Toolkit)

- bundle_id: `labview-roborio-toolkit`
- source_path: `roboriohelp/roborio_ni_software.html`
- source_url: https://docs-be.ni.com/bundle/labview-roborio-toolkit/raw/resource/enus/roboriohelp/roborio_ni_software.html
- document_id: `labview-roborio-toolkit`
- page_type: `leaf`
- content_type: ``

### Using roboRIO with Other NI Software (roboRIO Toolkit)

Use the following topics to learn about creating applications on the roboRIO with the LabVIEW roboRIO Toolkit and other NI software:

- Acquiring and Processing Images
- Communicating with Serial Devices Using VISA
- Creating Feedback Control Systems
- Creating Robotics Applications
- Performing Textual Mathematics and Algorithm Design
- Simulating Dynamic Systems
- Visualizing Data on a Mobile Device

|  | To view related topics, click the Locate button, shown at left, in the toolbar at the top of this window. The LabVIEW Help highlights this topic in the Contents tab so you can navigate the related topics. |
| --- | --- |

<!--NI_TOPIC bundle=labview-roborio-toolkit path=roboriohelp/roborio_pid_apps.html language=enus -->
## TOPIC 00018: Creating Feedback Control Systems (roboRIO Toolkit)

- bundle_id: `labview-roborio-toolkit`
- source_path: `roboriohelp/roborio_pid_apps.html`
- source_url: https://docs-be.ni.com/bundle/labview-roborio-toolkit/raw/resource/enus/roboriohelp/roborio_pid_apps.html
- document_id: `labview-roborio-toolkit`
- page_type: `leaf`
- content_type: ``

### Creating Feedback Control Systems (roboRIO Toolkit)

You can use the roboRIO with the PID VIs to create feedback control systems to control motors, temperature, pressure, and so on. To access the PID VIs, select **Control & Simulation»PID** from the Functions palette in LabVIEW.

**Related Information**

[PID VIs](/csh?topicname=lvpid/pidtitle.html)

[Functions Palette](/csh?topicname=glang/functions_palette.html)

<!--NI_TOPIC bundle=labview-roborio-toolkit path=roboriohelp/roborio_power_supply.html language=enus -->
## TOPIC 00019: Power Supply (roboRIO Toolkit)

- bundle_id: `labview-roborio-toolkit`
- source_path: `roboriohelp/roborio_power_supply.html`
- source_url: https://docs-be.ni.com/bundle/labview-roborio-toolkit/raw/resource/enus/roboriohelp/roborio_power_supply.html
- document_id: `labview-roborio-toolkit`
- page_type: `leaf`
- content_type: ``

### Power Supply (roboRIO Toolkit)

The following types of power supplies are necessary for using the roboRIO:

- Power supply for the roboRIO
- Power supply for peripheral devices

#### Power Supply for the roboRIO

You need to connect an external power supply to the roboRIO. The power supply provides the power for the roboRIO I/O channels and the onboard devices.

|  | Note The power supply voltage for the roboRIO to properly work ranges from 7 V to 16 V. |
| --- | --- |

Use the COMBICON power connector that ships with the roboRIO to connect the power supply to the roboRIO. The following figure shows the COMBICON power connector.

[IMAGE alt='image' src='noloc_eps_power_9075.gif']

The following list describes important details about the previous figure:

|  | The terminal screws secure the wires in the screw terminals. |
| --- | --- |
|  | The connector screws secure the power connector on the front panel of the roboRIO. |

##### Wiring Power to the roboRIO

Complete the following steps to connect a power supply to the roboRIO:

|  | Caution Turn off the power supply before you install or remove the power connector from the roboRIO. |
| --- | --- |

1. Connect the positive lead of the power supply to the V terminal of the power connector and tighten the terminal screw.
2. Connect the negative lead of the power supply to the C terminal of the power connector and tighten the terminal screw.
3. Install the power connector on the front panel of the roboRIO and tighten the connector screws.
4. Turn on the power supply.

#### Power Supply for Peripheral Devices

When you connect peripheral devices to the roboRIO, the roboRIO works as the master device and supplies power to the peripheral devices.

The roboRIO contains multiple voltage rails because different ports require different power supplies for the peripheral devices. The following table lists the roboRIO voltage rails for powering the peripheral devices.

| Voltage Rail | Usage |
| --- | --- |
| 6 V | Power from the PWM port for use with servos. |
| 5 V | Power from the SPI port. Power from DIO and ANALOG IN ports for sensors. Power from the MXP port for powering expansion circuits. |
| 3.3 V | Power from SPI, I2C, and MXP ports. |

<!--NI_TOPIC bundle=labview-roborio-toolkit path=roboriohelp/roborio_project_explorer.html language=enus -->
## TOPIC 00020: Using the Project Explorer Window (roboRIO Toolkit)

- bundle_id: `labview-roborio-toolkit`
- source_path: `roboriohelp/roborio_project_explorer.html`
- source_url: https://docs-be.ni.com/bundle/labview-roborio-toolkit/raw/resource/enus/roboriohelp/roborio_project_explorer.html
- document_id: `labview-roborio-toolkit`
- page_type: `leaf`
- content_type: ``

### Using the Project Explorer Window (roboRIO Toolkit)

Use the **Project Explorer** window to manage LabVIEW projects for the following tasks:

- Managing the targets, VIs, and other support files of a project from one location.
- Connecting the host computer to roboRIO targets, setting target properties, and deploying VIs to targets.

The following figure shows the **Project Explorer** window when you add a roboRIO target to a LabVIEW project.

[IMAGE alt='image' src='roborioprojectexplorer.gif']

The **Project Explorer** window includes the following sections:

- Project root —Contains the host computer and the roboRIO target you add to the current project. The label on the project root includes the filename for the project. To add more roboRIO targets to the project, right-click the project root and select New»Targets and Devices from the shortcut menu.
  - My Computer —Represents the local or host computer as a target in the project.
    - Build Specifications —Includes build configurations for source distributions and other types of builds available in LabVIEW toolkits and modules.
  - RT Target —Represents the roboRIO target you add to the project. VIs and libraries that you add to a roboRIO target appear under this target in the Project Explorer window. 
 
 To configure the settings of a roboRIO target, right-click the target and select Properties from the shortcut menu to launch the roboRIO Properties dialog box. You can also right-click the roboRIO target and select different options to accomplish the following tasks: creating a callback VI from templates, launching the Getting Started with roboRIO wizard, and launching the roboRIO I/O Monitor .
    - FPGA Target —Represents the FPGA target on the roboRIO. To add the FPGA target under the RT target, right-click the chassis under the roboRIO target and select New»FPGA Target from the shortcut menu.
 [IMAGE alt='image' src='note.gif']
**Note** Once you add an FPGA target under the chassis, you must use an FPGA bitfile with the roboRIO VIs.
    - Build Specifications —Includes specifications for building source distributions, stand-alone real-time applications, and zip files. If you have the LabVIEW Professional Development System or the Application Builder installed, right-click Build Specifications and select New»Real-Time Application from the shortcut menu to create a build specification that defines how to build stand-alone real-time applications.

**Related Information**

[Managing a Project in LabVIEW](/csh?topicname=lvconcepts/using_labview_projects.html)

[Adding RT Targets to a LabVIEW Project](/csh?topicname=lvrtconcepts/adding_targets_project_rt.html)

[Creating Stand-Alone Real-Time Applications](/csh?topicname=lvrtconcepts/building_rtapplications.html)

[Real-Time Target](/csh?topicname=lvrthelp/rt_computing_devices.html)

[Using Callback VIs to Handle Interrupts](../roboriohelp/roborio_use_callback_vi.html)

[Getting Started with roboRIO Wizard](../roboriohelp/roboriohelp.html)

[roboRIO I/O Monitor](../roboriohelp/roboriohelp.html)

<!--NI_TOPIC bundle=labview-roborio-toolkit path=roboriohelp/roborio_related_doc.html language=enus -->
## TOPIC 00021: Related Documentation (roboRIO Toolkit)

- bundle_id: `labview-roborio-toolkit`
- source_path: `roboriohelp/roborio_related_doc.html`
- source_url: https://docs-be.ni.com/bundle/labview-roborio-toolkit/raw/resource/enus/roboriohelp/roborio_related_doc.html
- document_id: `labview-roborio-toolkit`
- page_type: `leaf`
- content_type: ``

### Related Documentation (roboRIO Toolkit)

The following documents contain information that you may find helpful as you use the LabVIEW roboRIO Toolkit:

- Getting Started with roboRIO Programming —Use these tutorials to learn about creating your first roboRIO application and configuring Ethernet on the roboRIO. To access these tutorials, launch LabVIEW, click the Set Up and Explore link in LabVIEW, and select Access Getting Started Tutorials .
- roboRIO I/O Monitor Help —Use this help to learn about how to test and monitor data from each I/O channel on the roboRIO. You can access this help by clicking the Help button in the roboRIO I/O Monitor dialog box.
- roboRIO User Manual and roboRIO Specifications—Use these manuals to learn about the roboRIO hardware, specifications, and other helpful resources, such as dimensions, pin assignments, and connectivity information. You must have Adobe Reader installed to view the PDFs. Refer to the Adobe Systems Incorporated website at www.adobe.com to download the latest version of Adobe Reader. Refer to ni.com/manuals for updated documentation resources.
- LabVIEW roboRIO Toolkit Readme —Use this file to obtain introductory information about the LabVIEW roboRIO Toolkit, such as the product overview, system requirements, installation instructions, and known issues. Access this readme by navigating to the labview\readme directory and opening readme_roboRIO.html .
- LabVIEW roboRIO Software Bundle Readme —Use this file to obtain introductory information about the LabVIEW roboRIO Software Bundle, such as included software, system requirements, installation instructions, and known issues. To access this readme, insert the LabVIEW roboRIO Software Bundle DVD 1 and open readme_roboRIOBundle.html .
- Additional LabVIEW documentation for LabVIEW add-ons such as the Real-Time Module and the FPGA Module.

<!--NI_TOPIC bundle=labview-roborio-toolkit path=roboriohelp/roborio_robo_apps.html language=enus -->
## TOPIC 00022: Creating Robotics Applications (roboRIO Toolkit)

- bundle_id: `labview-roborio-toolkit`
- source_path: `roboriohelp/roborio_robo_apps.html`
- source_url: https://docs-be.ni.com/bundle/labview-roborio-toolkit/raw/resource/enus/roboriohelp/roborio_robo_apps.html
- document_id: `labview-roborio-toolkit`
- page_type: `leaf`
- content_type: ``

### Creating Robotics Applications (roboRIO Toolkit)

The LabVIEW Robotics Module for myRIO and roboRIO provides you with select functionality from the LabVIEW Robotics Module to use with the myRIO or the roboRIO. You can use the roboRIO with the Robotics Module for myRIO and roboRIO to develop and deploy robotics applications, such as steering, path planning, obstacle avoidance, and inverse kinematics.

To install the Robotics Module for myRIO and roboRIO, insert the LabVIEW roboRIO Software Bundle DVD 1 and select **Robotics Module for myRIO and roboRIO** from the product list. After you install the Robotics Module for myRIO and roboRIO, you can find the Robotics Algorithms VIs by selecting **roboRIO»Robotics Algorithms** from the Functions palette in LabVIEW.

Visit ni.com/info and enter the Info Code exb9ig to learn more about the Robotics Module for myRIO and roboRIO.

**Related Information**

[LabVIEW roboRIO Software Bundle Readme](../roboriohelp/roborio_related_doc.html)

[Functions Palette](/csh?topicname=glang/functions_palette.html)

<!--NI_TOPIC bundle=labview-roborio-toolkit path=roboriohelp/roborio_simulation_apps.html language=enus -->
## TOPIC 00023: Simulating Dynamic Systems (roboRIO Toolkit)

- bundle_id: `labview-roborio-toolkit`
- source_path: `roboriohelp/roborio_simulation_apps.html`
- source_url: https://docs-be.ni.com/bundle/labview-roborio-toolkit/raw/resource/enus/roboriohelp/roborio_simulation_apps.html
- document_id: `labview-roborio-toolkit`
- page_type: `leaf`
- content_type: ``

### Simulating Dynamic Systems (roboRIO Toolkit)

You can use the roboRIO with the LabVIEW Control Design and Simulation Module to simulate dynamic systems, design sophisticated controllers, and use both classical and state-space approaches to design controllers and estimators.

After you install the Control Design and Simulation Module, you can find the Control Design and Simulation VIs and functions by selecting **Control & Simulation** from the Functions palette in LabVIEW.

Visit ni.com/info and enter the Info Code exu7rq to learn more about the Control Design and Simulation Module.

**Related Information**

[Functions Palette](/csh?topicname=glang/functions_palette.html)

<!--NI_TOPIC bundle=labview-roborio-toolkit path=roboriohelp/roborio_usb_ethernet_config.html language=enus -->
## TOPIC 00024: Connecting roboRIO to a Host Computer (roboRIO Toolkit)

- bundle_id: `labview-roborio-toolkit`
- source_path: `roboriohelp/roborio_usb_ethernet_config.html`
- source_url: https://docs-be.ni.com/bundle/labview-roborio-toolkit/raw/resource/enus/roboriohelp/roborio_usb_ethernet_config.html
- document_id: `labview-roborio-toolkit`
- page_type: `leaf`
- content_type: ``

### Connecting roboRIO to a Host Computer (roboRIO Toolkit)

You can connect the roboRIO to a host computer by using one of the following methods:

- USB device connection —When you use a USB cable to connect the roboRIO from the USB device port to a host computer, the LabVIEW roboRIO Toolkit installs a USB driver on the host computer. The USB driver then creates a virtual network interface card and assigns an IP address to the roboRIO in the format 172.22.11. x .
- Ethernet connection —When you use an Ethernet cable to connect the roboRIO to a host computer, you can control the roboRIO and deploy VIs to the roboRIO through an Ethernet network. To learn about configuring Ethernet on the roboRIO, launch LabVIEW, click the Set Up and Explore link, and select Configure Ethernet .

<!--NI_TOPIC bundle=labview-roborio-toolkit path=roboriohelp/roborio_use_callback_vi.html language=enus -->
## TOPIC 00025: Using Callback VIs to Handle Interrupts (roboRIO Toolkit)

- bundle_id: `labview-roborio-toolkit`
- source_path: `roboriohelp/roborio_use_callback_vi.html`
- source_url: https://docs-be.ni.com/bundle/labview-roborio-toolkit/raw/resource/enus/roboriohelp/roborio_use_callback_vi.html
- document_id: `labview-roborio-toolkit`
- page_type: `leaf`
- content_type: ``

### Using Callback VIs to Handle Interrupts (roboRIO Toolkit)

An interrupt is a signal indicating an event that needs immediate attention. You can use interrupts to alert the target to a high-priority condition that requires the interruption of the current block diagram code that the target is executing. To trigger an interrupt, you can use the Interrupt Express VI or Interrupt Low Level VIs.

You must use callback VIs to handle interrupts. The Callback VI contains code that handles interrupts and runs when the interrupt triggering occurs.

#### Considerations for Callback VIs

When you create or use a callback VI, take the following factors into consideration:

- Callback VIs are of a time-critical priority, which is the highest priority in block diagram code on RT targets. This means that the priority of callback VIs is higher than that of any Timed Loops on RT targets. To avoid unexpected timing behavior, do not add a Timed Loop to the block diagram of callback VIs.
- You can use callback VIs to unregister or destroy interrupts. When you unregister or destroy an interrupt, the interrupt triggering stops. Destroying an interrupt also releases the resources associated with the interrupt.
- To communicate between a callback VI and a non-callback VI, you must use global variables or function global variables, which help access and pass data among VIs.
- A callback VI can use one or two CPUs, as described in the following table.

| Scenario | Use Case | Note |
| --- | --- | --- |
| One CPU Used | The block diagram of the callback VI includes only one While Loop. This loop does not contain pieces of code running in parallel. | The non-callback code keeps executing when the callback VI runs. |
| Two CPUs Used | The block diagram of the callback VI includes two While Loops. Each CPU executes the code running in one While Loop. The block diagram code of the callback VI contains one While Loop. This loop contains two pieces of code that execute in parallel. | The non-callback code stops executing until the callback VI finishes running and frees up one CPU. Using two CPUs for a long time can cause a disconnection between the host computer and the target, because keeping this connection requires using the CPU of the target. Note National Instruments recommends that you use callback VIs to execute short code that handles emergent events. |
|  | Note National Instruments recommends that you use callback VIs to execute short code that handles emergent events. |  |

#### Creating a Callback VI

To create a callback VI, you must ensure the connector pane of the VI meets the following requirements:

- The connector pane uses the 4 x 2 x 2 x 4 pattern.
- The data type of the top-left terminal is unsigned 8-bit integer.
- The top-left terminal is a recommended terminal.

You can also create callback VIs from templates by completing the following steps:

1. In LabVIEW, select File»Create Project to launch the Create Project dialog box and create a new roboRIO project.
2. In the Project Explorer window, right-click the roboRIO target, select Create Callback VI , and select one of the following options:
  - IO IRQ —Creates a callback VI that handles I/O interrupts, such as analog and digital input interrupts.
  - Timer IRQ —Creates a callback VI that handles timer interrupts.
3. In the Specify a name for the callback VI dialog box, specify a name for the VI and click Save .
4. Click OK when LabVIEW finishes creating the VI and adding this VI to the roboRIO target. You can find the callback VI when you expand the roboRIO target.

#### Opening a Callback VI

In the **Project Explorer** window, you can always double-click a callback VI under the target to open and edit this VI. When you add multiple callback VIs under the target, use one of the following methods to locate the callback VI that a VI uses:

- Double-click the Callback VI reference that you wire to the Register Analog Input Interrupt VI or the Register Digital Input Interrupt VI to open the callback VI that a Low Level VI uses.
- Right-click the Interrupt Express VI and select Open Callback VI from the shortcut menu to open the callback VI that the Express VI uses.

**Related Information**

[Building the Connector Pane](/csh?topicname=lvconcepts/building_connector_pane.html)

[Create Project Dialog Box](/csh?topicname=lvdialog/create_project_db.html)

[Global Variables](/csh?topicname=lvconcepts/glob_variables.html)

[Interrupt Express VI](/csh?topicname=myrioreference/myrioref_exp_irq.html)

[Interrupt VIs](/csh?topicname=myrioreference/myrioref_irqvis.html)

<!--NI_TOPIC bundle=labview-roborio-toolkit path=roboriohelp/roborio_visa_apps.html language=enus -->
## TOPIC 00026: Communicating with Serial Devices Using VISA (roboRIO Toolkit)

- bundle_id: `labview-roborio-toolkit`
- source_path: `roboriohelp/roborio_visa_apps.html`
- source_url: https://docs-be.ni.com/bundle/labview-roborio-toolkit/raw/resource/enus/roboriohelp/roborio_visa_apps.html
- document_id: `labview-roborio-toolkit`
- page_type: `leaf`
- content_type: ``

### Communicating with Serial Devices Using VISA (roboRIO Toolkit)

You can install NI-VISA to communicate with serial devices that you connect to the roboRIO. NI-VISA is the National Instruments implementation of the VISA I/O standard. NI-VISA includes software libraries, interactive utilities, and configuration programs through Measurement & Automation Explorer (MAX) for various development needs.

**Related Information**

[VISA VIs and Functions](/csh?topicname=lvinstio/visa_lib_ref_func_descr.html)

<!--NI_TOPIC bundle=labview-roborio-toolkit path=roboriohelp/roborio_vision_apps.html language=enus -->
## TOPIC 00027: Acquiring and Processing Images (roboRIO Toolkit)

- bundle_id: `labview-roborio-toolkit`
- source_path: `roboriohelp/roborio_vision_apps.html`
- source_url: https://docs-be.ni.com/bundle/labview-roborio-toolkit/raw/resource/enus/roboriohelp/roborio_vision_apps.html
- document_id: `labview-roborio-toolkit`
- page_type: `leaf`
- content_type: ``

### Acquiring and Processing Images (roboRIO Toolkit)

You can connect a USB camera to the USB host port on the roboRIO to acquire and process images. You must install the following NI software to create image applications:

- NI Vision Acquisition Software —Allows you to acquire images from USB cameras that you connect to the roboRIO.
- NI Vision Development Module —Helps you develop image processing applications, such as image pattern recognition, color sensing, light sensing, and object tracking.

After you connect a USB camera to the roboRIO and install the software, select **Tools»Vision Assistant** in LabVIEW to launch the **Vision Assistant** to start acquiring and processing images.

Visit ni.com/info and enter the Info Code exwj7a to learn more about the Vision Acquisition Software and the Vision Development Module.

<!--NI_TOPIC bundle=labview-roborio-toolkit path=roboriohelp/roboriohelp.html language=enus -->
## TOPIC 00028: roboRIO Toolkit

- bundle_id: `labview-roborio-toolkit`
- source_path: `roboriohelp/roboriohelp.html`
- source_url: https://docs-be.ni.com/bundle/labview-roborio-toolkit/raw/resource/enus/roboriohelp/roboriohelp.html
- document_id: `labview-roborio-toolkit`
- page_type: `leaf`
- content_type: ``

### roboRIO Toolkit

June 2015, 374999A-01

The LabVIEW roboRIO Toolkit provides you with tools for creating and deploying applications on the roboRIO. The roboRIO Toolkit contains the following components:

- roboRIO VIs —The roboRIO VIs provide functionality that you use to interface with the roboRIO I/O channels and onboard devices.
- roboRIO USB Monitor —This USB monitor shows basic information about the roboRIO that you connect to your computer and provides options for you to work with the roboRIO. This USB monitor appears when you use a USB cable to connect the roboRIO to your computer.
- Getting Started with roboRIO —This wizard helps you set up a new roboRIO and test the onboard devices. To launch this wizard, launch LabVIEW, click the Set Up and Explore link, and select Launch the Getting Started Wizard . You can also access this wizard through the roboRIO USB Monitor .
- roboRIO I/O Monitor —This dialog box helps you test and monitor data from different I/O channels on the roboRIO. To launch this dialog box, launch LabVIEW, click the Set Up and Explore link, and select Launch the I/O Monitor . You can also access this dialog box through the roboRIO USB Monitor .
- Templates and sample projects —Templates demonstrate useful design patterns and serve as starting points for your applications. Sample projects demonstrate working applications based on the templates. You can customize the templates and sample projects according to the needs of your application. Select File»Create Project to display the Create Project dialog box, which lists templates and sample projects.
- Examples —Example VIs demonstrate common applications that you can create by using the roboRIO Toolkit. You can modify an example VI to fit an application, or you can copy and paste from one or more example VIs into a VI that you create. Refer to the labview\examples\roboRIO directory for example VIs installed with the roboRIO Toolkit. You can also access these VIs by selecting Help»Find Examples and then selecting Toolkits and Modules»roboRIO in the NI Example Finder.

|  | To view related topics, click the Locate button, shown at left, in the toolbar at the top of this window. The LabVIEW Help highlights this topic in the Contents tab so you can navigate the related topics. |
| --- | --- |

© 2015 National Instruments. All rights reserved.
