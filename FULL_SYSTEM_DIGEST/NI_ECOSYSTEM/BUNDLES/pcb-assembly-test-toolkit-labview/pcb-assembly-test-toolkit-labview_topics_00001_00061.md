# NI DOCUMENT BUNDLE: pcb-assembly-test-toolkit-labview

<!--NI_BUNDLE_CHUNK bundle=pcb-assembly-test-toolkit-labview start=1 end=61 -->
<!--NI_TOPIC bundle=pcb-assembly-test-toolkit-labview path=action-button-test-seq.html language=enus -->
## TOPIC 00001: Action Button Test Sequence

- bundle_id: `pcb-assembly-test-toolkit-labview`
- source_path: `action-button-test-seq.html`
- source_url: https://docs-be.ni.com/bundle/pcb-assembly-test-toolkit-labview/raw/resource/enus/action-button-test-seq.html
- document_id: `pcb-assembly-test-toolkit-labview`
- page_type: `leaf`
- content_type: `reference`
- source_description: The Action Button Test sequence generates DC voltages to simulate button actions that demonstrate DC-RMS voltage measurements simultaneously on specific PCB test points. This TestStand sequence uses the LabVIEW measurement libraries. By default, the test sequence is installed to the following locati

### Action Button Test Sequence

The Action Button Test sequence generates DC voltages to simulate button actions
 that demonstrate DC-RMS voltage measurements simultaneously on specific PCB test points.

This TestStand sequence uses the LabVIEW measurement libraries. By default, the test
 sequence is installed to the following location: C:\Users\Public\Documents\National Instruments\PCB Assembly Test
 Toolkit for LabVIEW\TestStand\Automation\Action Button
 Tests

#### Required Driver Application Software

#### Highlighted Features

Action Button Test

- DAQ_DC Voltage Generation
- DAQ_DC-RMS Voltage Measurement

Turn Off all AO Channels

#### Hardware Configuration

[IMAGE alt='image' src='GUID-328C86DD-8928-40B4-B6EA-DC5666B12B6A-a5.png']

#### Using the Sequence with Physical Hardware

1. Run the sequence once in simulation mode. Running the sequence
 in simulation mode creates the required global virtual channels in NI MAX that
 you must modify. Note In this
 example, physical and global virtual channels are used to configure the
 terminal or pin to perform the instrument actions. Global virtual channels
 are software entities that encapsulate the physical channel along with other
 channel specific information such as range, terminal configuration, and
 custom scaling. You can create global channels in NI MAX and call them from
 measurement libraries.
2. Right click the Import Hardware Config step and select Run Mode»Skip to skip the step.
3. Configure the remaining sequences. Open each sequence and
 examine the Note to run with Hardware entry.
4. Step into the Action Button Test sequence.
  1. Select the DC Voltage Generation - Action
 Button ON State and DC Voltage Generation -
 Action Button OFF State steps and update the generated
 static digital states based on Action Button ON and OFF conditions. In
 the example, the Action Button ON condition is achieved by supplying 3.3
 V to TS_BUTTONENABLE0 and the Action Button OFF
 condition is achieved by supplying 0 V to
 TS_BUTTONENABLE0 . Review and modify the digital
 states based on your use case. Note The maximum current
 drive per channel is specific to each device. For the PXIe-6363, the
 maximum current drive per channel is ±5 mA. For the TS-15110 analog
 output module, the maximum current drive per channel is ±1 mA. If
 you are using another device, consult the applicable device
 specifications. Consider the specified limit when configuring button
 states.
  2. Review analog output and analog input pin configurations for your
 intended use case.
5. Configure the Turn Off all AO Channels 
 sequence.
  1. Open the DC Voltage Generation - Initialize AO
 Channels step and update the Physical
 Channels input to use your analog output channel.
  2. Review the analog output pin configurations for your use case.
  3. Save the sequence.

Parent topic:

Automation Test Sequences

<!--NI_TOPIC bundle=pcb-assembly-test-toolkit-labview path=audio-test-sequence.html language=enus -->
## TOPIC 00002: Audio Test Sequence

- bundle_id: `pcb-assembly-test-toolkit-labview`
- source_path: `audio-test-sequence.html`
- source_url: https://docs-be.ni.com/bundle/pcb-assembly-test-toolkit-labview/raw/resource/enus/audio-test-sequence.html
- document_id: `pcb-assembly-test-toolkit-labview`
- page_type: `leaf`
- content_type: `reference`
- source_description: The Audio Test sequence demonstrates frequency domain measurements of audio tones captured from the audio amplifier path. This TestStand sequence uses the LabVIEW measurement libraries. By default, the test sequence is installed to the following location: C:\Users\Public\Documents\National Instrumen

### Audio Test Sequence

The Audio Test sequence demonstrates frequency domain measurements of audio tones
 captured from the audio amplifier path.

This TestStand sequence uses the LabVIEW measurement libraries. By default, the test
 sequence is installed to the following location: C:\Users\Public\Documents\National Instruments\PCB Assembly Test
 Toolkit for LabVIEW\TestStand\Automation\Audio Tests

#### Required Driver Application Software

#### Highlighted Features

Audio Line Check

- DAQ_DC Signal Voltage Generation
- DAQ_Frequency Domain Measurement

Audio Filter Check

- DAQ_DC Signal Voltage Generation
- DAQ_Frequency Domain Measurement

Turn Off all AO Channels

#### Hardware Configuration

[IMAGE alt='image' src='GUID-FEF68370-AFE8-43CA-9E98-F1FBE08EB43D-a5.png']

#### Using the Sequence with Physical Hardware

1. Run the sequence once in simulation mode. Running the sequence
 in simulation mode creates the required global virtual channels in NI MAX that
 you must modify. Note In this
 example, physical and global virtual channels are used to configure the
 terminal or pin to perform the instrument actions. Global virtual channels
 are software entities that encapsulate the physical channel along with other
 channel specific information such as range, terminal configuration, and
 custom scaling. You can create global channels in NI MAX and call them from
 measurement libraries.
2. Right click the Import Hardware Config step and select Run Mode»Skip to skip the step.
3. Configure the remaining sequences. Open each sequence and
 examine the Note to run with Hardware entry.
4. Configure the Audio Line Check sequence.
  1. Open NI-MAX and update the physical channel linked to the global virtual
 channels used in the Signal Voltage Generation and Frequency Domain
 Measurement initialize steps: TS_AudioLineIn0 and
 TP_AudioLineOut0 . Refer to Creating and
 Modifying Global Virtual Channels for more information.
  2. Open the Frequency Domain Measurement – Configure
 TP step and update the Digital Trigger
 Source .
  3. Review the analog output and analog input pin configurations for your
 use case.
  4. Save the sequence.
5. Configure the Audio Filter Check sequence.
  1. Open NI-MAX and update the physical channel linked to the global virtual
 channels used in the Signal Voltage Generation and Frequency Domain
 Measurement initialize steps: TS_AudioLineIn0 and
 TP_AudioLineOut0 . Refer to Creating and
 Modifying Global Virtual Channels for more information.
  2. Open the Frequency Domain Measurement – Configure
 TP step and update the Digital Trigger
 Source .
  3. Review the analog output and analog input pin configurations for your
 use case.
  4. Save the sequence.
6. Configure the Turn Off all AO Channels 
 sequence.
  1. Open the DC Voltage Generation - Initialize AO
 Channels step and update the Physical
 Channels input to use your analog output channel.
  2. Review the analog output pin configurations for your use case.
  3. Save the sequence.

Parent topic:

Automation Test Sequences

Related tasks:

- Creating and Modifying Global Virtual Channels

<!--NI_TOPIC bundle=pcb-assembly-test-toolkit-labview path=comm-apis.html language=enus -->
## TOPIC 00003: Communication APIs Library

- bundle_id: `pcb-assembly-test-toolkit-labview`
- source_path: `comm-apis.html`
- source_url: https://docs-be.ni.com/bundle/pcb-assembly-test-toolkit-labview/raw/resource/enus/comm-apis.html
- document_id: `pcb-assembly-test-toolkit-labview`
- page_type: `leaf`
- content_type: `reference`
- source_description: The Communication APIs Library contains simple read and write VIs for I^2C, SPI, and serial communication modes. This library is applicable for the USB-8452, USB-232, and corresponding driver application software. The library provides separate VI for each supported communication mode (I^2C, SPI, or

### Communication APIs Library

The Communication APIs Library contains simple read and write VIs for I<sup>2</sup>C,
 SPI, and serial communication modes. This library is applicable for the USB-8452, USB-232,
 and corresponding driver application software.

- The library provides separate VI for each supported communication mode (I 2 C, SPI,
 or serial). Each VI performs equivalent read and write functions.
- Refer to the existing LabVIEW examples for additional information.
  - The 845x_I2C and 845x_SPI read and write VIs for
 NI-845x devices are based on the existing NI-845x LabVIEW example. Refer
 to Location of NI-845x Example for information about
 locating the installed example.
  - The VISA_Simple Serial VI is based on the LabVIEW example for serial
 communication. The LabVIEW example performs read and write operations.
 In LabVIEW, select Help»Find Examples and use the LabVIEW Example Finder to locate serial
 communcation examples.

Figure 41.

2

[IMAGE alt='image' src='GUID-337D2EC4-B15B-42BA-826F-E8CFE1BF1115-a5.png']

Figure 42.

[IMAGE alt='image' src='GUID-517DF36A-EBAD-4BDE-8BB7-6C937D35BEAB-a5.png']

Figure 43.

[IMAGE alt='image' src='GUID-E5EC0193-B2CE-4A9B-830E-688150B40255-a5.png']

Parent topic:

Measurement Libraries

Related information:

- I2C/SPI NI-845x Hardware and Software Manual
- Archived: NI-845x Software and Hardware Installation Guide (May
 2011)
- Location of NI-845x Example
- Serial Installation Guide for PCI/PCIe, PXI/PXIe, USB, ENET,
 ExpressCard, and PCMCIA Hardware
- Set Up Communication with Serial Instruments in LabVIEW using
 NI-VISA

<!--NI_TOPIC bundle=pcb-assembly-test-toolkit-labview path=communication-test-seq.html language=enus -->
## TOPIC 00004: Communication Test Sequence

- bundle_id: `pcb-assembly-test-toolkit-labview`
- source_path: `communication-test-seq.html`
- source_url: https://docs-be.ni.com/bundle/pcb-assembly-test-toolkit-labview/raw/resource/enus/communication-test-seq.html
- document_id: `pcb-assembly-test-toolkit-labview`
- page_type: `leaf`
- content_type: `reference`
- source_description: The Communication Test sequence demonstrates data read and write operations through I^2C, SPI, and serial communication using a USB-845x or USB-232 device. This TestStand sequence uses the LabVIEW measurement libraries. By default, the test sequence is installed to the following location: C:\Users\P

### Communication Test Sequence

The Communication Test sequence demonstrates data read and write operations
 through I<sup>2</sup>C, SPI, and serial communication using a USB-845x or USB-232
 device.

This TestStand sequence uses the LabVIEW measurement libraries.
 By default, the test sequence is installed to the following location: C:\Users\Public\Documents\National Instruments\PCB Assembly Test
 Toolkit for LabVIEW\TestStand\Automation\Communication
 Tests

Refer to the *Communications APIs Library* topic for
 information about related examples on which the Communication APIs are based.

#### Required Driver Application Software

- NI-DAQmx
- NI-845x
- NI-Serial

#### Highlighted Features

I2C Comm Test

2

SPI Comm Test

Serial Comm Test

#### Hardware Configuration

Figure 7.

2

[IMAGE alt='image' src='GUID-5AD7EBA0-461E-40F7-95BE-CAE027E8F7ED-a5.png']

Figure 8.

[IMAGE alt='image' src='GUID-A69F1754-B5BC-455D-9C3E-208FE304FC7A-a5.png']

Figure 9.

[IMAGE alt='image' src='GUID-2D20B1BF-7650-406A-A52D-37C0E08A1671-a5.png']

#### Using the Sequence with Physical
 Hardware

- Update the I2C Comm Test sequence.
  1. Update the DeviceID variable with the connected
 USB-845x device ID in the Update I2C Interface Device
 ID step. Copy this step and associated variables if you
 create a custom sequence.
  2. Review and update step settings for the I2C Read – Read
 Register Data and I2C Write – Write Register
 Data steps based on the relevant I 2 C
 specifications. These settings are used in read and write
 operations.
  3. Review the configurations of USB-845x I 2 C pins for your
 intended use case.

- Update the SPI Comm Test sequence.
  1. Update the DeviceID variable with the connected
 USB-845x device ID in the Update SPI Interface Device
 ID step. Copy this step and associated variables if you
 create a custom sequence.
  2. Review and update step settings for the SPI Read – Read
 Register Data and SPI Write – Write Register
 Data steps based on the relevant SPI specifications.
 These settings are used in read and write operations.
  3. Review the configurations of USB-845x SPI pins for your intended use
 case.

- Update the Serial Comm Test sequence.
  1. Update the Serial VISA variable with the targeted
 serial COM VISA address in the Update Serial VISA 
 step. Copy this step and associated variables if you create a
 custom sequence.
  2. Review and update step settings for the Simple Serial
 Comm step based on the relevant serial port
 specifications. These settings are used in read and write operations
 over the serial COM port.
  3. Review the connections between the serial com ports for your intended
 use case.

Parent topic:

Automation Test Sequences

Related tasks:

- Creating and Modifying Global Virtual Channels

Related reference:

- Communication APIs Library

Related information:

- Set Up Communication with Serial Instruments in LabVIEW using
 NI-VISA
- Serial Installation Guide for PCI/PCIe, PXI/PXIe, USB, ENET,
 ExpressCard, and PCMCIA Hardware
- Archived: NI-845x Software and Hardware Installation Guide (May
 2011)
- Location of NI-845x Example

<!--NI_TOPIC bundle=pcb-assembly-test-toolkit-labview path=creating-sequences.html language=enus -->
## TOPIC 00005: Creating a Sequence in TestStand with LabVIEW APIs

- bundle_id: `pcb-assembly-test-toolkit-labview`
- source_path: `creating-sequences.html`
- source_url: https://docs-be.ni.com/bundle/pcb-assembly-test-toolkit-labview/raw/resource/enus/creating-sequences.html
- document_id: `pcb-assembly-test-toolkit-labview`
- page_type: `leaf`
- content_type: `task`
- source_description: Before you begin, you must create a PCBATT LabVIEW project. Refer to Launching the Toolkit in LabVIEW for details. You will use the path to your project in the following procedure. Launch TestStand. Select File New Sequence File to create an empty sequence file. Insert LabVIEW VIs in the sequence. R

### Creating a Sequence in TestStand with LabVIEW
 APIs

Note

Launching the Toolkit in LabVIEW

1. Launch TestStand.
2. Select File»New»Sequence File to create an empty sequence file.
3. Insert LabVIEW VIs in the sequence. Refer to the PCB Assembly Test
 Toolkit for LabVIEW sequence templates as you implement
 your test sequence. Note You can use both
 physical and virtual channels. Refer to the *Automation Test
 Sequences* topic to understand naming conventions for virtual
 channels.
  - You can access PCB Assembly Test
 Toolkit for LabVIEW LabVIEW VIs
 from your PCBATT LabVIEW project.
  - PCB Assembly Test
 Toolkit for LabVIEW sequence templates are
 available in the following location: C:\Users\Public\Documents\National Instruments\PCB Assembly Test
 Toolkit for LabVIEW\TestStand\Automation
4. Use test steps to perform limit checks on measured values for your test cases.
 Use flow control steps to control the execution of test steps according to your
 test needs.
5. Select File»Save As to save your sequence file.

#### Running Your TestStand Sequence

Complete the following steps to run a test sequence that is open in TestStand.

1. Select Execute»Single Pass to run the test sequence.
2. When the execution completes, click review the report in
 the Report pane.
3. (Optional) select Execute»Restart to run the sequence again.

Parent topic:

Using the PCB Assembly Test Toolkit for LabVIEW

Related reference:

- Launching the Toolkit in LabVIEW
- Automation Test Sequences

<!--NI_TOPIC bundle=pcb-assembly-test-toolkit-labview path=dc-rms-current-measure-library.html language=enus -->
## TOPIC 00006: DAQ_DC-RMS Current Measurement Library

- bundle_id: `pcb-assembly-test-toolkit-labview`
- source_path: `dc-rms-current-measure-library.html`
- source_url: https://docs-be.ni.com/bundle/pcb-assembly-test-toolkit-labview/raw/resource/enus/dc-rms-current-measure-library.html
- document_id: `pcb-assembly-test-toolkit-labview`
- page_type: `leaf`
- content_type: `reference`
- source_description: DAQ_DC-RMS Current Measurement library VIs initialize, configure, measure, and close user-configurable analog input pins for current measurements. This library is applicable for analog input channels and modules. Use the DAQ_DC-RMS Current Meas Initialize VI to initialize hardware and create a DAQmx

### DAQ_DC-RMS Current Measurement
 Library

DAQ_DC-RMS Current Measurement library VIs initialize, configure, measure, and close
 user-configurable analog input pins for current measurements. This library is applicable for
 analog input channels and modules.

1. Use the DAQ_DC-RMS Current Meas Initialize VI to initialize hardware
 and create a DAQmx Task for current measurement. Note If you use a Global channel,
 declare it as current.
2. Pass the current measurement DAQmx Task to the DAQ_DC-RMS Current Meas Configure
 and Measure VI.
3. Configure the DAQ_DC-RMS Current Meas Configure and Measure VI.
  - 
  - Execution Settings —By default, the Configure and Measure VI also executes the
 measurement. If you are using a trigger for your
 measurement, choose the Configure Only or Measure Only
 execution option to avoid automatic execution. Use the
 Skip Analysis? setting to select whether to perform
 post-analysis on the measured data. Use post-analysis to
 derive the average and RMS current.
  - Configuration Settings —Configure the channel settings. You can configure all analog input channels or
 configure individual settings for only active channels. The
 channel settings include the maximum and minimum current
 range, terminal configuration, shunt resistor location,
 shunt resistor value and active channels. To configure
 active channels click the Channel Setting
 Type tab. Configure the timing related
 parameters for the DC-RMS current measurement. The
 Timing setting configures sample clock source input,
 sampling rate, number of samples, and the sample timing
 engine used for the DAQmx Task.Acquisition Time = Number of Samples/Sample Rate
 Specify a value of Auto to automatically select
 the timing engine. Note For NI
 63xx (X Series) and other DAQ devices, use Auto mode
 only. The sample timing engine is only used for cDAQ and
 TestScale platforms, which support multiple timing
 engines. Note Refer to
 the relevant specifications document to identify the
 maximum sampling rate for your device. Values that
 exceed the maximum sampling rate generate errors. Configure triggers to start the source or
 measurement based on various trigger events. Trigger
 options include no trigger or digital start
 triggers.
  - Output Data —The VI outputs the following data.
  - Current Waveforms —Displays the captured DC waveforms.
  - DC-RMS Current Measurements —Provides the derived post-analyzed data from the
 captured DC waveforms.
  - Acquisition Time —The calculated acquisition time for the
 measurement.
4. Wire the updated current measurement task from DAQmx Task Out.
5. Close the current measurement task using DAQ_DC-RMS Current Meas Close 
 VI.

#### Execution Option Settings

Configure and Measure

Configure Only

Measure Only

#### Best Practices

- For faster measurements, set the maximum sampling rate possible for the given
 Sample Clock Source input and assign a smaller Number of Samples to
 capture.
- To access this VI in a software-based timing setting, set the sampling rate for
 the sample clock source and set the number of samples to two (the minimum
 samples supported by DAQmx). Invoke this VI multiple times in a software loop to
 get the actual required number of samples.
- For better resolution, increase the number of samples (for example, 1000
 samples).

Figure 20.

[IMAGE alt='image' src='GUID-0F19C2E8-DD48-417D-8344-986959A3AEFF-a5.png']

Parent topic:

Measurement Libraries

<!--NI_TOPIC bundle=pcb-assembly-test-toolkit-labview path=dc-rms-voltage-measure-library.html language=enus -->
## TOPIC 00007: DAQ DC-RMS Voltage Measurement Library

- bundle_id: `pcb-assembly-test-toolkit-labview`
- source_path: `dc-rms-voltage-measure-library.html`
- source_url: https://docs-be.ni.com/bundle/pcb-assembly-test-toolkit-labview/raw/resource/enus/dc-rms-voltage-measure-library.html
- document_id: `pcb-assembly-test-toolkit-labview`
- page_type: `leaf`
- content_type: `reference`
- source_description: DAQ DC-RMS Voltage Measurement Library VIs initialize, configure, measure, and close user-configurable analog input pins. This library is applicable for analog input channels and modules. Use the DAQ_DC-RMS Voltage Meas Initialize VI to initialize hardware and create a DAQmx Task for voltage measure

### DAQ DC-RMS Voltage Measurement
 Library

DAQ DC-RMS Voltage Measurement Library VIs initialize, configure, measure, and close
 user-configurable analog input pins. This library is applicable for analog input channels
 and modules.

1. Use the DAQ_DC-RMS Voltage Meas Initialize VI to initialize hardware
 and create a DAQmx Task for voltage measurement.
2. Pass the voltage measurement DAQmx Task to the DAQ_DC-RMS Voltage Meas Configure
 and Measure VI.
3. Configure the DAQ_DC-RMS Voltage Meas Configure and Measure VI.
  - 
  - Execution Settings —By default, the Configure and Measure VI also executes the
 measurement. If you are using a trigger for your
 measurement, choose the Configure Only or Measure Only
 execution option to avoid automatic execution. Use the
 Skip Analysis? setting to select whether to perform post
 analysis on the measured data. Use post-analysis to
 derive the average and RMS voltage.
  - Configuration Settings —Configure the range and terminal settings. Global settings are applied to any channel
 without channel-specific settings. Use the Specific Channel
 Settings to configure a channel, including physical analog
 input voltage channels, to a specific limit. Configure
 the timing related parameters for DAQ_DC-RMS voltage
 measurement. The Timing setting configures sample clock
 source input, sampling rate, number of samples, and the
 sample timing engine used for the DAQmx Task.Acquisition Time = Number of Samples/Sample Rate
 Specify a value of Auto to automatically select
 the timing engine. Note For NI
 63xx (X Series) and other DAQ devices, use Auto mode
 only. The sample timing engine is only used for cDAQ and
 TestScale platforms, which support multiple timing
 engines. Note Refer to
 the relevant specifications document to identify the
 maximum sampling rate for your device. Values that
 exceed the maximum sampling rate generate errors. Configure triggers to start the source or
 measurement based on various trigger events. Trigger
 options include no trigger or digital start
 triggers.
  - Output Data —The VI outputs the following data.
  - Voltage Waveforms —Displays the captured voltage waveforms.
  - DC-RMS Voltage Measurements —Provides the derived post-analyzed data from the
 captured DC waveforms.
  - Acquisition Time —The calculated acquisition time for the
 measurement.
4. Wire the updated voltage measurement task from DAQmx Task Out.
5. Close the voltage measurement task using DAQ_DC-RMS Voltage Meas Close 
 VI.

#### Execution Option Settings

Configure and Measure

Configure Only

Measure Only

#### Best Practices

- For faster measurements, set the maximum sampling rate possible for the given
 Sample Clock Source input and assign a smaller Number of Samples to
 capture.
- For better resolution, increase the number of samples (for example, 1000
 samples).

Figure 17.

[IMAGE alt='image' src='GUID-C1492AE3-92B8-43F4-B882-66F4634EE385-a5.png']

Parent topic:

Measurement Libraries

<!--NI_TOPIC bundle=pcb-assembly-test-toolkit-labview path=dc-voltage-gen-library.html language=enus -->
## TOPIC 00008: DAQ_DC Voltage Generation Library

- bundle_id: `pcb-assembly-test-toolkit-labview`
- source_path: `dc-voltage-gen-library.html`
- source_url: https://docs-be.ni.com/bundle/pcb-assembly-test-toolkit-labview/raw/resource/enus/dc-voltage-gen-library.html
- document_id: `pcb-assembly-test-toolkit-labview`
- page_type: `leaf`
- content_type: `reference`
- source_description: DAQ_DC Voltage Generation Library VIs initialize, configure, generate, and close user-configurable analog output pins for DC voltage generation. This library is applicable for analog output channels and modules. Use the DAQ_DC Voltage Gen Initialize VI to initialize hardware and create a DAQmx Task

### DAQ_DC Voltage Generation Library

DAQ_DC Voltage Generation Library VIs initialize, configure, generate, and close
 user-configurable analog output pins for DC voltage generation. This library is applicable
 for analog output channels and modules.

1. Use the DAQ_DC Voltage Gen Initialize VI to initialize hardware and
 create a DAQmx Task for DC voltage generation. Notice To avoid equipment damage or
 measurement degradation, configure the device to generate 0 V before calling
 the DAQ_DC Voltage Gen Close VI. Voltage is generated
 until you configure the device to generate 0 V or until device power is
 disabled during a reboot.
2. Pass the DAQmx Task to the DAQ_DC Voltage Gen Configure and Measure 
 VI.
3. Configure the DAQ_DC Voltage Gen Configure and Measure VI.
  - 
  - Range Settings —Specifies the minimum and maximum range settings for the
 analog output voltage channels.
  - Output Voltage —Specifies the output voltage to generate on the selected
 channels.
4. Wire the updated DC voltage generation task from DAQmx Task Out.
5. Close the DC voltage generation task using DAQ_DC Voltage Gen Close 
 VI.

Figure 16.

[IMAGE alt='image' src='GUID-7FCF5754-0C09-4914-8878-8841555B05D2-a5.png']

Parent topic:

Measurement Libraries

<!--NI_TOPIC bundle=pcb-assembly-test-toolkit-labview path=digital-clock-gen.html language=enus -->
## TOPIC 00009: DAQ_Digital Clock Generation Library

- bundle_id: `pcb-assembly-test-toolkit-labview`
- source_path: `digital-clock-gen.html`
- source_url: https://docs-be.ni.com/bundle/pcb-assembly-test-toolkit-labview/raw/resource/enus/digital-clock-gen.html
- document_id: `pcb-assembly-test-toolkit-labview`
- page_type: `leaf`
- content_type: `reference`
- source_description: DAQ_Digital Clock Generation Library VIs initialize, configure, generate, and close user-configurable terminals using counters. This library is applicable for digital I/O channels and modules that support timing output signals with PFI channels or other connections. Use the DAQ_Digital Clk Gen Initi

### DAQ_Digital Clock Generation Library

DAQ_Digital Clock Generation Library VIs initialize, configure, generate, and close
 user-configurable terminals using counters. This library is applicable for digital I/O
 channels and modules that support timing output signals with PFI channels or other
 connections.

1. Use the DAQ_Digital Clk Gen Initialize VI to initialize hardware and
 create a DAQmx Task for dynamic digital clock generation.
2. Specify the physical channel input to use for the counter. Only one counter can
 be used for a task. Use separate tasks for each counter if multiple counters are
 required. Note TestScale
 devices do not support frequency generation because the generation time and
 duty cycle cannot be controlled. Refer to *Using the Frequency
 Generator* in the *TestScale Features* manual for
 details.
3. Provide the output terminal on which to generate the signal. Refer to the NI-DAQmx
 Device Terminals Help table. To access the table in NI MAX, select
 your device and right-click Device Pinout . Use the table
 to view the default PFI terminals of each counter for your device.
4. If necessary, configure PFI lines. Note For the TestScale TS-15050
 module only, P0.DIO<0:7> channels map to
 PFI<0:7> terminals. Refer to the
 *TS-15050 Specifications* for more information.
5. Pass the digital clock generation DAQmx Task to the DAQ_Digital Clk
 Gen Configure and Measure VI.
6. Configure the DAQ_Digital Clk Gen Configure and Measure 
 VI.
  - 
  - Frequency (Hz) —Specifies the frequency to generate pulses.
  - Duty cycle (%) —Specifies the duty cycle to generate pulses.
  - Generation Time —Specifies the time for the generation of the digital clock
 signal. Set generation times as an integral multiple of the
 time period (1/Frequency (Hz)) to generate complete
 cycles.
  - Actual Pulse Settings —Returns the frequency, duty cycle and generation time of the
 generated digital signal from the instrument.
7. Wire the updated digital clock generation task from DAQmx Task Out.
8. Close the digital clock generation task using DAQ_Digital Clk Gen
 Close VI.

Figure 32.

[IMAGE alt='image' src='GUID-E6F54070-7489-4F5E-9DDD-7C31206B21E3-a5.png']

Parent topic:

Measurement Libraries

Related information:

- Using the Frequency Generator

<!--NI_TOPIC bundle=pcb-assembly-test-toolkit-labview path=digital-edge-count-measure.html language=enus -->
## TOPIC 00010: DAQ_Digital Edge Count Measurement Library

- bundle_id: `pcb-assembly-test-toolkit-labview`
- source_path: `digital-edge-count-measure.html`
- source_url: https://docs-be.ni.com/bundle/pcb-assembly-test-toolkit-labview/raw/resource/enus/digital-edge-count-measure.html
- document_id: `pcb-assembly-test-toolkit-labview`
- page_type: `leaf`
- content_type: `reference`
- source_description: DAQ_Digital Edge Count Measurement Library VIs initialize, configure, measure, and close user-configurable PFI lines using selected counters for digital events or edge counting. This library is applicable for digital I/O channels and modules that support timing input signals with PFI channels or oth

### DAQ_Digital Edge Count Measurement Library

DAQ_Digital Edge Count Measurement Library VIs initialize, configure, measure, and close
 user-configurable PFI lines using selected counters for digital events or edge counting.
 This library is applicable for digital I/O channels and modules that support timing
 input signals with PFI channels or other connections.

1. Use the DAQ_DECM Initialize VI to initialize hardware and create DAQmx
 Tasks for digital edge count measurement. The Count Digital Events library
 requires two DAQmx tasks: a counter task for edge counting and a timer task
 used for hardware-timed wait types to precisely control measurement time.
2. For the timer task, provide a counter resource to generate the measurement
 window for a hardware-timed wait type. No external physical connections are
 required. The counter task uses the generated pulse internally. For
 software-timed wait types, leave the Counter – Timer input empty.
3. For the counter task, provide a counter resource and input terminal to listen for digital
 events or edges. Refer to the NI-DAQmx Device Terminals Help table.
 To access the table in NI MAX, select your device and right-click
 Device Pinout . Use the table to view the default PFI
 terminals of each counter for your device.
4. If necessary, configure PFI lines. Note For
 the TestScale TS-15050 module only, P0.DIO<0:7>
 channels map to PFI<0:7> terminals. Refer to
 the *TS-15050 Specifications* for more information.
5. Pass the digital edge count measurement DAQmx Task to the DAQ_DECM Configure and
 Measure VI. Refer to the following sections for more information
 about configuration settings.
  - 
  - Execution Settings —By default, the Configure and Measure VI also executes the
 measurement. If you are using a trigger for your
 measurement, choose the Configure Only or Measure Only
 execution option to avoid automatic execution. Note For
 software-timed wait types, a Measure Only operation
 returns the current counter value immediately. It does
 not wait for the specified duration.
  - Counter Settings —These setting specify the active edge to count, the count
 duration, and the wait type (either software-timed or
 hardware-timed).
  - Timer - Trigger Settings —These settings control the start of the hardware-timed
 counting with a digital start trigger.
  - Output Data —The VI returns the number of edge counts at the end of
 measurement duration.
6. Close the digital edge count measurement task using DAQ_DECM Close 
 VI.

#### Execution Option Settings

Configure and Measure

Configure Only

Measure Only

#### Hardware Timed Digital Edge Counting

With hardware-timed digital edge counting, a timer task precisely controls the count
 measurement time by generating a single pulse of the specified duration that starts
 or stops the counting process. This is suitable for high-frequency inputs that
 require precise a measurement time for edge counting.

The following timing diagram illustrates hardware-timed digital edge counting. In this case,
 the timer task controls the measurement time by generating a pulse signal of the
 specified duration.

Calling the Configure and Measure VI starts the edge counting, waits for the
 specified measurement duration (counting happens until the timer pulse signal goes
 low) and finally measures the counter value.

Figure 36.

[IMAGE alt='image' src='GUID-70792D03-CEF4-4BE9-80DF-734CBCD08258-a5.png']

The following timing diagram illustrates hardware-timed digital edge counting with a
 trigger. In this case, the digital start trigger source controls the timer start.

The Configure Only call configures the trigger, starts the task and wait for the
 trigger to start the timer and edge counting. At that point, you can send the
 trigger and perform additional actions. The Measure Only call waits for the
 specified measurement duration and then reads the counter value.

Figure 37.

[IMAGE alt='image' src='GUID-C82F46DB-69B6-4BEB-99B9-6AE4709E79E8-a5.png']

#### Software Timed Digital Edge Counting

With software-timed digital edge counting, counting starts as soon as the task
 starts. After an internal or external software-timed wait, the edges are
 counted.

The following timing diagram illustrates software-timed digital edge counting that
 uses the library VI to add the wait internally.

The Configure and Measure call starts the edge counting, waits for the specified
 measurement duration, and finally measures the counter value. With this method,
 software delays can affect the counting process to produce measurements that are
 less precise.

This method is suitable for low-frequency inputs that do not require a precise
 measurement time for edge counting.

Figure 38.

[IMAGE alt='image' src='GUID-8D4EA389-5332-455B-9C1C-95BDB5D0DE42-a5.png']

The following timing diagram illustrates software-timed digital edge counting that
 uses an external, user-defined software wait. The library VI does not wait during
 the measurement.

The Configure Only call starts the edge counting. During the measurement duration you
 can wait in the test layer or perform other actions before using a Measure Only call
 to read and return the counter value.

This method is suitable for low-frequency inputs with long measurement times that during which
 you can perform other operations. You can also wait and measure in a separate
 thread.

Figure 39.

[IMAGE alt='image' src='GUID-8335E988-392E-42F0-A07F-FC3F3AE72FC1-a5.png']

Figure 40.

[IMAGE alt='image' src='GUID-191FB767-9DFA-4F7F-B7C8-432471A47F0F-a5.png']

Parent topic:

Measurement Libraries

<!--NI_TOPIC bundle=pcb-assembly-test-toolkit-labview path=digital-frequency-measure.html language=enus -->
## TOPIC 00011: DAQ_Digital Frequency Measurement Library

- bundle_id: `pcb-assembly-test-toolkit-labview`
- source_path: `digital-frequency-measure.html`
- source_url: https://docs-be.ni.com/bundle/pcb-assembly-test-toolkit-labview/raw/resource/enus/digital-frequency-measure.html
- document_id: `pcb-assembly-test-toolkit-labview`
- page_type: `leaf`
- content_type: `reference`
- source_description: DAQ_Digital Frequency Measurement Library VIs initialize, configure, measure, and close user-configurable PFI lines using selected counter for digital frequency measurement. This library is applicable for digital I/O channels and modules that support timing input signals with PFI channels or other c

### DAQ_Digital Frequency Measurement
 Library

DAQ_Digital Frequency Measurement Library VIs initialize, configure, measure, and
 close user-configurable PFI lines using selected counter for digital frequency
 measurement. This library is applicable for digital I/O channels and modules that
 support timing input signals with PFI channels or other connections. This
 measurement uses the large range (two-counter) measurement method. This method uses one
 counter to divide the frequency of the input signal by the specified divisor, creating a
 lower-frequency signal that is measured using second counter. Refer to the following topics
 for detailed information about this measurement method.

- Large-Range Two Counters Measurement Method in the NI-DAQmx User
 Manual manual
- Large Range of Frequencies with Two Counters in the TestScale
 Features manual

1. Use the DAQ_Dig Freq Meas Initialize VI to initialize hardware and
 create a DAQmx Task for digital frequency measurement.
2. Specify the physical or global channel input to use for the counter. Only one counter can be
 used for a task. Use separate tasks for each counter if multiple counters are
 required. Note Counter 0 is always paired with
 Counter 1. Counter 2 is
 always paired with Counter 3 for the large range (two
 counter) method used by this library. Paired counters cannot be used in
 other tasks.
3. Provide the output terminal on which to measure the signal. Refer to the NI-DAQmx
 Device Terminals Help table. To access the table in NI MAX, select
 your device and right-click Device Pinout . Use the table
 to view the default PFI terminals of each counter for your device.
4. If necessary, configure PFI lines. Note For
 the TestScale TS-15050 module only, P0.DIO<0:7>
 channels map to PFI<0:7> terminals. Refer to
 the *TS-15050 Specifications* for more information.
5. Pass the digital frequency measurement DAQmx Task to the DAQ_Dig Freq Meas
 Configure and Measure VI.
6. Configure the DAQ_Dig Freq Meas Configure and Measure VI.
  - 
  - Range —These settings include the frequency range for the
 measurement. Based on this setting, the internal time base
 is selected to obtain the highest resolution.
  - Measurement Settings —These settings include the divisor value for the large range
 (two counter) measurement method. The default value (4) is
 appropriate for most use cases. Update the divisor value
 only if necessary. Larger values increase measurement
 accuracy but a value that is too large causes the count
 register to roll over. Refer to Large-Range Two
 Counter Measurement Method in the NI-DAQmx
 User Manual for the frequency range calculation
 based on divisor value. Note For very
 low frequencies, the measurement may require multiple
 input cycles.
  - Output Data —Returns the detected frequency on the specified input
 terminal.
7. Wire the updated digital frequency measurement task from DAQmx Task Out.
8. Close the digital frequency measurement task with the DAQ_Dig Freq Meas
 Close VI.

Figure 34.

[IMAGE alt='image' src='GUID-191FB767-9DFA-4F7F-B7C8-432471A47F0F-a5.png']

Parent topic:

Measurement Libraries

Related information:

- Large-Range Two Counter Measurement Method
- Large Range of Frequencies with Two Counters

<!--NI_TOPIC bundle=pcb-assembly-test-toolkit-labview path=digital-io-sequence.html language=enus -->
## TOPIC 00012: Digital I/O Test Sequence

- bundle_id: `pcb-assembly-test-toolkit-labview`
- source_path: `digital-io-sequence.html`
- source_url: https://docs-be.ni.com/bundle/pcb-assembly-test-toolkit-labview/raw/resource/enus/digital-io-sequence.html
- document_id: `pcb-assembly-test-toolkit-labview`
- page_type: `leaf`
- content_type: `reference`
- source_description: The Digital I/O Tests sequence simulates digital I/O channels or modules to demonstrate generation and measurement of digital state, digital pattern, clock, digital pulse, and PWM signals. This TestStand sequence uses the LabVIEW measurement libraries. By default, the test sequence is installed to t

### Digital I/O Test Sequence

The Digital I/O Tests sequence simulates digital I/O channels or modules to
 demonstrate generation and measurement of digital state, digital pattern, clock, digital
 pulse, and PWM signals.

This TestStand sequence uses the LabVIEW measurement libraries. By default, the test
 sequence is installed to the following location: C:\Users\Public\Documents\National Instruments\PCB Assembly Test
 Toolkit for LabVIEW\TestStand\Automation\Digital IO Tests

#### Highlighted Features

Digital State Test

- DAQ_Static Digital State Generation
- DAQ_Static Digital State Measurement

Digital Pattern Test (with trigger)

- DAQ_Dynamic Digital Pattern Generation
- DAQ_Dynamic Digital Pattern Measurement

Digital Clock Tests

- DAQ_Digital Clock Generation
- DAQ_Digital Frequency Measurement

Digital PWM Test

- DAQ_Digital Pulse Generation
- DAQ_Digital PWM Measurement

Digital Count Event Tests - SW Timed (External Wait)

- DAQ_Digital Pulse Generation
- DAQ_Digital Edge Count Measurement

Digital Count Event Tests - HW Timed (With Trigger)

- DAQ_Digital Pattern Generation
- DAQ_Digital Edge Count Measurement

Turn Off all DO Channels

#### Hardware Configuration

[IMAGE alt='image' src='GUID-90E1F675-FB70-4CC3-9304-BFB697B10F52-a5.png']

#### Using the Sequence with Physical
 Hardware

1. Run the sequence once in simulation mode. Running the sequence
 in simulation mode creates the required global virtual channels in NI MAX that
 you must modify. Note In this
 example, physical and global virtual channels are used to configure the
 terminal or pin to perform the instrument actions. Global virtual channels
 are software entities that encapsulate the physical channel along with other
 channel specific information such as range, terminal configuration, and
 custom scaling. You can create global channels in NI MAX and call them from
 measurement libraries.
2. Right click the Import Hardware Config step and select Run Mode»Skip to skip the step.
3. Configure the remaining sequences. Open each sequence and
 examine the Note to run with Hardware entry.
4. Configure the Digital State Test sequence.
  1. Open NI-MAX and update the physical channel linked to the global virtual
 channels used in the Static Digital State Generation and Measurement
 initialize steps: TS_Din0, TS_Din1, TP_DOut0,
 TP_DOut1 . Refer to Creating and Modifying Global
 Virtual Channels for more information.
  2. Review the digital input and digital output pin configurations for your
 application use case.
  3. Save the sequence.
5. Configure the Digital Pattern Test (With Trigger) 
 sequence.
  1. Open NI-MAX and update the physical channel linked to the global virtual
 channels used in the Static Digital State Generation and Measurement
 initialize steps: TS_Din0, TS_Din1, TP_DOut0,
 TP_DOut1 . Refer to Creating and Modifying Global
 Virtual Channels for more information.
  2. Update the trigger as appropriate for your hardware configuration in
 Dynamic Digital Pattern Measurement - Configure
 TP step.
  3. Update parameters in the Generate Port Digital Data 
 step based on the desired digital pattern. This step can also be
 replaced entirely with any other step to generate any custom digital
 pattern.
  4. Verify that the sampling rate at measurement end should be the same as
 the sampling rate at generation end. Use the onboard clock devices on
 the same backplane or use external PFI signals.
  5. Review the pin configurations for your application use case.
  6. Save the sequence.
6. Configure the Digital Clock Test sequence.
  1. Update the terminal and counter channels used in the initialize step.
    - Physical Counter: Simulated_DAQ/ctr1,
 Simulated_DAQ/ctr3
    - Terminals: /Simulated_DAQ/PFI3,
 /Simulated_DAQ/PFI7
  2. Update the digital clock settings in the Digital Clock
 Generation - Configure and generate Digital clock step
 based on the generated digital clock signal.
  3. Review the pin configurations for your application use case.
  4. Save the sequence.
7. Configure the Digital PWM Test sequence.
  1. Update the terminal and counter channels used in the initialize step.
    - Physical Counter: Simulated_DAQ/ctr1,
 Simulated_DAQ/ctr3
    - Terminals: /Simulated_DAQ/PFI3,
 /Simulated_DAQ/PFI7
  2. Update the cycles to capture in the Digital PWM Measurement -
 Configure only step.
  3. Update the digital pulse settings in the Digital Pulse
 Generation - Generate Digital pulse signals step based on
 the generated digital pulse signal.
  4. Review the pin configurations for your application use case.
  5. Save the sequence.
8. Configure the Digital Count Event Tests - SW Timed (External
 Wait) sequence.
  1. Update the terminal and counter channels used in the initialize step.
    - Physical Counter: Simulated_DAQ/ctr1,
 Simulated_DAQ/ctr3
    - Terminals: /Simulated_DAQ/PFI3,
 /Simulated_DAQ/PFI7
  2. Update the digital pulse settings in the Digital Pulse
 Generation - Configure & Generate Digital pulse
 signals step.
  3. Update the external software wait time in the External
 Software Wait step based on the measurement window
 required to capture the entire digital pulse signal.
  4. Review the pin configurations for your application use case.
  5. Save the sequence.
9. Configure the Digital Count Event Tests - HW Timed (With
 Trigger) sequence.
  1. Update the terminal and counter channels used in the initialize step.
    - Physical Counter: Simulated_DAQ/ctr0,
 Simulated_DAQ/ctr1
    - Terminals: /Simulated_DAQ/PFI0
    - Global Channel: TS_Din0
  2. Update the trigger as appropriate for your hardware configuration in
 Digital Edge Count Measurement - Configure TP 
 step.
  3. Update parameters in the Generate Port Digital Data 
 step based on the desired digital pattern. This step can also be
 replaced entirely with any other step to generate any custom digital
 pattern.
  4. Review the pin configurations for your application use case.
  5. Save the sequence.
10. Configure the Turn Off all DO Channels sequence.
  1. Open the Initialize step and update the Global
 Channels input to use yourdigital output channel.
  2. Review the digital output pin configurations for your use case.
  3. Save the sequence.

#### Physical Hardware
 Considerations

Ensure a common ground connection is provided between digital input and digital
 output resources.

In digital pattern measurement, make sure to use the same sample clock rate in both
 digital input and digital output for precise data extraction from the testpoint.

Digital states are provided as True or
 False Boolean values to the VIs. The corresponding
 voltage level, for example, a digital HIGH state, depends on individual
 resources.

(TestScale only) TS-15050 DIO channels use 3.3 V TTL, single-ended I/O. The TS-15120
 DIO voltage level is controlled by manual jumper connections. TS-15130 DO channels
 are current sinking outputs. Refer to the individual product documentation for
 additional details.

Parent topic:

Automation Test Sequences

Related tasks:

- Creating and Modifying Global Virtual Channels

<!--NI_TOPIC bundle=pcb-assembly-test-toolkit-labview path=digital-pulse-gen.html language=enus -->
## TOPIC 00013: DAQ_Digital Pulse Generation Library

- bundle_id: `pcb-assembly-test-toolkit-labview`
- source_path: `digital-pulse-gen.html`
- source_url: https://docs-be.ni.com/bundle/pcb-assembly-test-toolkit-labview/raw/resource/enus/digital-pulse-gen.html
- document_id: `pcb-assembly-test-toolkit-labview`
- page_type: `leaf`
- content_type: `reference`
- source_description: DAQ_Digital Pulse Generation Library VIs initialize, configure, generate, and close user-configurable terminals using counters. This library is applicable for digital I/O channels and modules that support timing output signals with PFI channels or other connections.The supported frequency range for

### DAQ_Digital Pulse Generation Library

DAQ_Digital Pulse Generation Library VIs initialize, configure, generate, and close
 user-configurable terminals using counters. This library is applicable for digital I/O
 channels and modules that support timing output signals with PFI channels or other
 connections.

Note

1. Use the DAQ_Digital Pulse Gen Initialize VI to initialize hardware and create a
 DAQmx Task for digital pulse generation.
2. Specify the physical or global channel input to use for the counter. Only one counter can be
 used for a task. Use separate tasks for each counter if multiple counters are
 required.
3. Provide the output terminal on which to generate the signal. Refer to the NI-DAQmx
 Device Terminals Help table. To access the table in NI MAX, select
 your device and right-click Device Pinout . Use the table
 to view the default PFI terminals of each counter for your device.
4. If necessary, configure PFI lines. Note For
 the TestScale TS-15050 module only, P0.DIO<0:7> channels map to
 PFI<0:7> terminals. Refer to the *TS-15050 Specifications*
 for more information.
5. Pass the digital pulse generation DAQmx Task to the DAQ_Digital Pulse Gen Configure and
 Measure VI.
6. Configure the DAQ_Digital Pulse Gen Configure and Measure VI.
  - 
  - High time (s) —Specifies the high time of the pulse.
  - Low time (s) —Specifies the low time of the pulse.
  - Number of Pulses —Specifies the number of pulses to generate.
  - Actual Pulse Settings —Returns the actual high time, low time and generation time
 of the generated digital signal.
7. Wire the updated digital pulse generation task from DAQmx Task Out.
8. Close the digital pulse generation task using DAQ_Digital Pulse Gen Close VI.

Figure 33.

[IMAGE alt='image' src='GUID-E6F54070-7489-4F5E-9DDD-7C31206B21E3-a5.png']

Parent topic:

Measurement Libraries

<!--NI_TOPIC bundle=pcb-assembly-test-toolkit-labview path=digital-pwm-measure.html language=enus -->
## TOPIC 00014: DAQ_Digital PWM Measurement Library

- bundle_id: `pcb-assembly-test-toolkit-labview`
- source_path: `digital-pwm-measure.html`
- source_url: https://docs-be.ni.com/bundle/pcb-assembly-test-toolkit-labview/raw/resource/enus/digital-pwm-measure.html
- document_id: `pcb-assembly-test-toolkit-labview`
- page_type: `leaf`
- content_type: `reference`
- source_description: DAQ_Digital PWM Measurement Library VIs initialize, configure, measure, and close counter input tasks with an assigned input terminal. This library is applicable for digital I/O channels and modules that support timing input signals with PFI channels or other connections. Use the DAQ Digital Frequen

### DAQ_Digital PWM Measurement Library

DAQ_Digital PWM Measurement Library VIs initialize, configure, measure, and close counter
 input tasks with an assigned input terminal. This library is applicable for digital I/O
 channels and modules that support timing input signals with PFI channels or other
 connections.

Note

1. Use the DAQ_Dig PWM Meas Initialize VI to initialize hardware and create a DAQmx
 Task for digital PWM measurement.
2. Specify the physical or global channel input to use for the counter. Only one counter can
 be used for a task. Only one counter can be
 used for a task. Use separate tasks for each counter if multiple counters are
 required. Note The Global Channel (Counter) input terminal supports
 only Semi-Period Counter Input global channels from NI MAX. The VI returns
 an error for other invalid global channels.
3. Provide the output terminal on which to measure the signal. Refer to the NI-DAQmx
 Device Terminals Help table. To access the table in NI MAX, select
 your device and right-click Device Pinout . Use the table
 to view the default PFI terminals of each counter for your device.
4. If necessary, configure PFI lines. Note For
 the TestScale TS-15050 module only, P0.DIO<0:7> channels map to
 PFI<0:7> terminals. Refer to the *TS-15050 Specifications*
 for more information.
5. During initialization, counters are reserved with the default timebase. for NI 63xx (X
 Series) DAQ devices, the default timebase is 100 MHz. The TestScale timebase
 uses a maximum value of 80 MHz. The following table shows the relation between
 each timebase and the PWM semi-period duration in DAQ NI 63xx (X Series) and
 TestScale devices. Timebase Clock
 Minimum Semi-Period
 Maximum Semi-Period100 MHz (default)
 20 ns
 42.949673 s
 80 MHz (TestScale maximum)
 25 ns
 53.687091 s
 20 MHz
 100 ns
 214.748365 s
 100 kHz
 20 µs
 42949.673 s To determine the timebase clocks assigned to the counter, update the
 minimum and maximum semi-period values in the DAQ_Dig PWM Meas
 Initialize VI block diagram. A semi-period is the time
 between either a rising and falling edge, or a falling and rising edge in a
 PWM signal. 
[IMAGE alt='image' src='GUID-66B03623-4BCE-44FF-AB36-25ADFC180D03-a5.png'] For
 details about TestScale Counter Timebase behavior, visit *Clock
 Routing* in the *TestScale Features* manual.
6. Pass the digital PWM measurement DAQmx Task to the DAQ_Dig PWM Meas Configure and Measure
 VI.
  - 
  - Execution Settings —By default, the Configure and Measure VI also executes the
 measurement. If you are using a trigger for your
 measurement, choose the Configure Only or Measure Only
 execution option to avoid automatic execution. Tip To
 capture the entire signal, use Configure Only mode to
 set the channel to wait for the first rising edge of the
 input signal. After capturing the cycles, use Measure
 Only mode to read the measured data.
  - Measurement Settings —Configure the number of PWM cycles to capture. Captured
 cycles are averaged to derive Digital PWM Measurements. A
 PWM cycle represents a complete PWM wave measured from the
 rising edge to next consecutive rising edge. At least two
 cycles are required for PWM measurements. Otherwise, the low
 time for a single pulse will not have a clear end to enable
 low time calculation. Configure the timeout. The default
 timeout is 10 seconds. The VI returns an error if the
 specified time elapses before the requested cycles are
 captured. Customize the timeout value as necessary based
 on the captured PWM signal frequency and number of
 cycles to capture.
  - Output Data —The VI returns the detected High Time(s), Low Time(s), Duty
 Cycle (%) and Frequency (Hz) on the specified input
 terminal. These measurements are the averaged results from
 the captured PWM cycles. The output measurements also return
 the actual number of cycles captured during the
 measurement.
7. Wire the updated digital PWM measurement task from DAQmx Task Out and perform any
 additional operations.
8. Close the digital PWM measurement task using DAQ_Dig PWM Meas Close VI.

#### Execution Option Settings

Configure and Measure

Configure Only

Measure Only

Figure 35.

[IMAGE alt='image' src='GUID-191FB767-9DFA-4F7F-B7C8-432471A47F0F-a5.png']

Parent topic:

Measurement Libraries

Related information:

- Clock Routing

<!--NI_TOPIC bundle=pcb-assembly-test-toolkit-labview path=dmm-dc-rms-current-measure-library.html language=enus -->
## TOPIC 00015: DMM_DC-RMS Current Measurement Library

- bundle_id: `pcb-assembly-test-toolkit-labview`
- source_path: `dmm-dc-rms-current-measure-library.html`
- source_url: https://docs-be.ni.com/bundle/pcb-assembly-test-toolkit-labview/raw/resource/enus/dmm-dc-rms-current-measure-library.html
- document_id: `pcb-assembly-test-toolkit-labview`
- page_type: `leaf`
- content_type: `reference`
- source_description: DMM_DC-RMS Current Measurement Library VIs initialize, configure, measure and and close a DC Current or AC RMS Current measurement on an NI-DMM instrument. The DMM_DC-RMS Current Meas Initialize VI creates a new NI-DMM driver session on the device specified by the DMM Resource Name control. The devi

### DMM_DC-RMS Current Measurement
 Library

DMM_DC-RMS Current Measurement Library VIs initialize, configure, measure and and close
 a DC Current or AC RMS Current measurement on an NI-DMM instrument.

The DMM_DC-RMS Current Meas Initialize VI creates a new NI-DMM
 driver session on the device specified by the DMM Resource Name control. The device
 uses the specified powerline frequency value to select a timebase for setting the
 Aperture Time property in powerline cycles (PLCs).

Note

50 Hz

60 Hz

The DMM_DC-RMS Current Meas Configure and Measure VI configures
 the NI-DMM DC or AC RMS current measurement on the resource provided by the DMM
 Handle In control.

Note

The DMM_DC-RMS Current Meas Configure and Measure VI configures
 the measurement based on the following settings.

Function Settings

Default Values and Automatic Range
 Coercion

Execution Option Settings

Configure and Measure

Configure Only

Measure Only

If repeated, a DMM Measure Only operation uses the most recent DMM
 Configure Only configuration.

Timing & Trigger Settings

- AC Min Frequency configures the minimum frequency properties the DMM
 uses for AC measurements that affect aperture settings.
- Aperture Time specifies the length of time for the ADC to read the
 signal.
- Settle Time is the time required for a measurement system to
 stabilize to a specified accuracy limit.

The DMM_DC-RMS Current Meas Configure and Measure VI returns the
 following information.

Measurement

DMM execution settings

The DMM_DC-RMS Voltage Meas Close VI closes the NI-DMM session
 specified by DMM Handle In and releases the resource.

#### Examples

Figure 21.

[IMAGE alt='image' src='GUID-F3372885-7530-419A-8E70-9998BB015CDE-a5.png']

If repeated, a DMM Measure Only operation uses the most recent DMM
 Configure Only configuration.

Figure 22.

[IMAGE alt='image' src='GUID-BA89B964-DCC1-4105-92B6-2704D284CB5E-a5.png']

#### Default Values and Automatic Range
 Coercion

Use the VI context help and block diagram comments to understand the impact of
 each parameter. Adjust the default values only when necessary for your
 application.

| Parameter Name | Default Value |
| --- | --- |
| Power Frequency | 50 Hz |
| Range and Function | First main function in Auto Range for each physical quantity |
| Resolution in Digits | 5 1/2 |
| Execution Option | Configure and Measure |
| Aperture Time (s) | -1 (Auto) |
| Settle Time (s) | -1 (Auto) |
| AC Min Frequency | 40 Hz |
| Enable Trigger? | False |
| Trigger Source | Immediate |
| Trigger Delay (s) | -1 (Auto) |
| Slope | Rising |

The listed range for each function include all possible ranges for all
 NI-DMM instruments. If you select a range that is not supported for your DMM, the
 upper supported range is automatically selected. Use the DMM»Execution Setting output to verify the actual execution values.

#### DMM Trigger Methods

If the physical signal is already active, a DMM can begin a measurement immediately
 when the read function executes within a Config and Measure VI when the Measure Only
 execution option is specified. Use the NI-DMM driver software to add software delays
 or specify a trigger delay to insert a user-defined delay before the measurement
 starts.

The following figure illustrates a block diagram configured for immediate measurement
 with a delay based on a DAQ analog output signal.

Note

[IMAGE alt='image' src='GUID-77165859-FEA5-4255-8F44-4AFD9A9FE81F-a5.png']

The DMM can start measurements using an external signal or internal TTL
 (X) channel configured as the HW Trigger
 Source. On a PXIe system, TTL (X) is connected
 to the PXI_Trigger(X) internal signal. For example, you can use
 a DAQ_6363/PXI_Trig0 as a start trigger by linking it to
 TTL 0 as the trigger source. When the read function
 executes inside the Configure and Measure VI, the DMM waits for the external signal
 and then waits for the duration of any specified trigger delay.

This configuration uses only a parallel physical signal.

The following figure illustrates a block diagram configured to use an hardware
 trigger source asynchronously.

[IMAGE alt='image' src='GUID-1A9D0640-CFB8-48F7-A9A0-82D56867EB76-a5.png']

Parent topic:

Measurement Libraries

<!--NI_TOPIC bundle=pcb-assembly-test-toolkit-labview path=dmm-dc-rms-voltage-measure-library.html language=enus -->
## TOPIC 00016: DMM_DC-RMS Voltage Measurement Library

- bundle_id: `pcb-assembly-test-toolkit-labview`
- source_path: `dmm-dc-rms-voltage-measure-library.html`
- source_url: https://docs-be.ni.com/bundle/pcb-assembly-test-toolkit-labview/raw/resource/enus/dmm-dc-rms-voltage-measure-library.html
- document_id: `pcb-assembly-test-toolkit-labview`
- page_type: `leaf`
- content_type: `reference`
- source_description: DMM_DC-RMS Voltage Measurement Library VIs initialize, configure, measure and close a DC voltage or AC RMS voltage measurement on a NI-DMM instrument. The DMM_DC-RMS Voltage Meas Initialize VI creates a new NI-DMM driver session on the device specified by the DMM Resource Name control. The device us

### DMM_DC-RMS Voltage Measurement
 Library

DMM_DC-RMS Voltage Measurement Library VIs initialize, configure, measure and close a DC
 voltage or AC RMS voltage measurement on a NI-DMM instrument.

The DMM_DC-RMS Voltage Meas Initialize VI creates a new NI-DMM driver
 session on the device specified by the DMM Resource Name control. The device uses
 the specified powerline frequency value to select a timebase for setting the
 Aperture Time property in powerline cycles (PLCs).

Note

50 Hz

60 Hz

The DMM_DC-RMS Voltage Meas Configure and Measure VI configures the
 NI-DMM DC or AC RMS voltage measurement on the resource provided by the DMM Handle
 In control.

Note

The DMM_DC-RMS Voltage Meas Configure and Measure VI configures
 the measurement based on the following settings.

Function Settings

Default Values and Automatic Range
 Coercion

Execution Option Settings

Configure and Measure

Configure Only

Measure Only

If repeated, a DMM Measure Only operation uses the most recent DMM
 Configure Only configuration.

Timing & Trigger Settings

- AC Min Frequency configures the minimum frequency properties the DMM
 uses for AC measurements that affect aperture settings.
- Aperture Time specifies the length of time for the ADC to read the
 signal.
- Settle Time is the time required for a measurement system to
 stabilize to a specified accuracy limit.

The DMM_DC-RMS Voltage Meas Configure and Measure VI returns the
 following information.

Measurement

DMM execution settings

The DMM_DC-RMS Voltage Meas Close VI closes the NI-DMM session specified
 by DMM Handle In and releases the resource.

#### Examples

Figure 18.

[IMAGE alt='image' src='GUID-FD609A1B-AE08-4BFC-B0C5-F47337E28028-a5.png']

If repeated, a DMM Measure Only operation uses the most recent DMM
 Configure Only configuration.

Figure 19.

[IMAGE alt='image' src='GUID-2F218CF0-60A5-446E-81B7-23ACAB59E39E-a5.png']

#### Default Values and Automatic Range
 Coercion

Use the VI context help and block diagram comments to understand the impact of
 each parameter. Adjust the default values only when necessary for your
 application.

| Parameter Name | Default Value |
| --- | --- |
| Power Frequency | 50 Hz |
| Range and Function | First main function in Auto Range for each physical quantity |
| Resolution in Digits | 5 1/2 |
| Execution Option | Configure and Measure |
| Aperture Time (s) | -1 (Auto) |
| Settle Time (s) | -1 (Auto) |
| AC Min Frequency | 40 Hz |
| Enable Trigger? | False |
| Trigger Source | Immediate |
| Trigger Delay (s) | -1 (Auto) |
| Slope | Rising |

The listed range for each function include all possible ranges for all
 NI-DMM instruments. If you select a range that is not supported for your DMM, the
 upper supported range is automatically selected. Use the DMM»Execution Setting output to verify the actual execution values.

#### DMM Trigger Methods

If the physical signal is already active, a DMM can begin a measurement immediately
 when the read function executes within a Config and Measure VI when the Measure Only
 execution option is specified. Use the NI-DMM driver software to add software delays
 or specify a trigger delay to insert a user-defined delay before the measurement
 starts.

The following figure illustrates a block diagram configured for immediate measurement
 with a delay based on a DAQ analog output signal.

Note

[IMAGE alt='image' src='GUID-77165859-FEA5-4255-8F44-4AFD9A9FE81F-a5.png']

The DMM can start measurements using an external signal or internal TTL
 (X) channel configured as the HW Trigger
 Source. On a PXIe system, TTL (X) is connected
 to the PXI_Trigger(X) internal signal. For example, you can use
 a DAQ_6363/PXI_Trig0 as a start trigger by linking it to
 TTL 0 as the trigger source. When the read function
 executes inside the Configure and Measure VI, the DMM waits for the external signal
 and then waits for the duration of any specified trigger delay.

This configuration uses only a parallel physical signal.

The following figure illustrates a block diagram configured to use an hardware
 trigger source asynchronously.

[IMAGE alt='image' src='GUID-1A9D0640-CFB8-48F7-A9A0-82D56867EB76-a5.png']

Parent topic:

Measurement Libraries

<!--NI_TOPIC bundle=pcb-assembly-test-toolkit-labview path=dmm-freq-measure-library.html language=enus -->
## TOPIC 00017: DMM_Frequency Domain Measurement Library

- bundle_id: `pcb-assembly-test-toolkit-labview`
- source_path: `dmm-freq-measure-library.html`
- source_url: https://docs-be.ni.com/bundle/pcb-assembly-test-toolkit-labview/raw/resource/enus/dmm-freq-measure-library.html
- document_id: `pcb-assembly-test-toolkit-labview`
- page_type: `leaf`
- content_type: `reference`
- source_description: DMM_Frequency Domain Measurement Library VIs initialize, configure, measure and close user-configurable analog input pins and derive frequency domain measurements for the measured waveforms. The DMM_Frequency Domain Meas Initialize VI creates a new NI-DMM driver session on the device specified by th

### DMM_Frequency Domain Measurement
 Library

DMM_Frequency Domain Measurement Library VIs initialize, configure, measure and close
 user-configurable analog input pins and derive frequency domain measurements for the
 measured waveforms.

The DMM_Frequency Domain Meas Initialize VI creates a new NI-DMM
 driver session on the device specified by the DMM Resource Name control. The device
 uses the specified powerline frequency value to select a timebase for setting the
 Aperture Time property in powerline cycles (PLCs).

Note

50 Hz

60 Hz

The DMM_Frequency Domain Meas Configure and Measure VI
 configures the NI-DMM frequency or period measurement on the resource provided by
 the DMM Handle In control.

Note

The DMM_Frequency Domain Meas Configure and Measure VI
 configures the measurement based on the following settings.

Function Settings

Default Values and Automatic Range
 Coercion

Note

Execution Option Settings

Configure and Measure

Configure Only

Measure Only

If repeated, a DMM Measure Only operation uses the most recent DMM
 Configure Only configuration.

Timing & Trigger Settings

The DMM_Frequency Domain Meas Configure and Measure VI returns
 the following information.

Measurement

DMM execution settings

The DMM_Frequency Domain Meas Close VI closes the NI-DMM session
 specified by DMM Handle In and releases the resource.

#### Examples

Figure 26.

[IMAGE alt='image' src='GUID-C11E93A0-405B-4CAE-99DB-AB5898D50B6E-a5.png']

This example uses the DAQ Signal Voltage Generation library to generate voltage
 from an analog output device.

Note

Figure 27.

[IMAGE alt='image' src='GUID-3E775FAF-0583-4611-A22C-3AABBC60D607-a5.png']

#### Default Values and Automatic Range
 Coercion

Use the VI context help and block diagram comments to understand the impact of
 each parameter. Adjust the default values only when necessary for your
 application.

| Parameter Name | Default Value |
| --- | --- |
| Power Frequency | 50 Hz |
| Range and Function | First main function in Auto Range for each physical quantity |
| Resolution in Digits | 5 1/2 |
| Execution Option | Configure and Measure |
| Aperture Time (s) | -1 (Auto) |
| Settle Time (s) | -1 (Auto) |
| AC Min Frequency | 40 Hz |
| Enable Trigger? | False |
| Trigger Source | Immediate |
| Trigger Delay (s) | -1 (Auto) |
| Slope | Rising |

The listed range for each function include all possible ranges for all
 NI-DMM instruments. If you select a range that is not supported for your DMM, the
 upper supported range is automatically selected. Use the DMM»Execution Setting output to verify the actual execution values.

#### DMM Trigger Methods

If the physical signal is already active, a DMM can begin a measurement immediately
 when the read function executes within a Config and Measure VI when the Measure Only
 execution option is specified. Use the NI-DMM driver software to add software delays
 or specify a trigger delay to insert a user-defined delay before the measurement
 starts.

The following figure illustrates a block diagram configured for immediate measurement
 with a delay based on a DAQ analog output signal.

Note

[IMAGE alt='image' src='GUID-77165859-FEA5-4255-8F44-4AFD9A9FE81F-a5.png']

The DMM can start measurements using an external signal or internal TTL
 (X) channel configured as the HW Trigger
 Source. On a PXIe system, TTL (X) is connected
 to the PXI_Trigger(X) internal signal. For example, you can use
 a DAQ_6363/PXI_Trig0 as a start trigger by linking it to
 TTL 0 as the trigger source. When the read function
 executes inside the Configure and Measure VI, the DMM waits for the external signal
 and then waits for the duration of any specified trigger delay.

This configuration uses only a parallel physical signal.

The following figure illustrates a block diagram configured to use an hardware
 trigger source asynchronously.

[IMAGE alt='image' src='GUID-1A9D0640-CFB8-48F7-A9A0-82D56867EB76-a5.png']

Parent topic:

Measurement Libraries

Related information:

- Frequency/Period

<!--NI_TOPIC bundle=pcb-assembly-test-toolkit-labview path=dmm-mixed-measure-library.html language=enus -->
## TOPIC 00018: DMM_Mixed Measurement Library (for DMM Scan)

- bundle_id: `pcb-assembly-test-toolkit-labview`
- source_path: `dmm-mixed-measure-library.html`
- source_url: https://docs-be.ni.com/bundle/pcb-assembly-test-toolkit-labview/raw/resource/enus/dmm-mixed-measure-library.html
- document_id: `pcb-assembly-test-toolkit-labview`
- page_type: `leaf`
- content_type: `reference`
- source_description: DMM Mixed Measurement Library VIs can be used to initialize, configure, measure, and close the following measurement types on a NI-DMM instrument: DC and AC voltage, DC and AC current, resistance (2-wire only), frequency, or period. ExamplesThe structure of this library is identical to the individua

### DMM_Mixed Measurement Library (for DMM
 Scan)

DMM Mixed Measurement Library VIs can be used to initialize, configure, measure, and
 close the following measurement types on a NI-DMM instrument: DC and AC voltage, DC and AC
 current, resistance (2-wire only), frequency, or period.

#### Examples

The following figure illustrates the minimum useful
 block diagram for this library.

Figure 49.

[IMAGE alt='image' src='GUID-495BAF1A-AA85-4972-8DA7-610EA2D28773-a5.png']

#### Default Values and Automatic Range
 Coercion

Use the VI context help and block diagram comments to understand the impact of
 each parameter. Adjust the default values only when necessary for your
 application.

| Parameter Name | Default Value |
| --- | --- |
| Power Frequency | 50 Hz |
| Range and Function | First main function in Auto Range for each physical quantity |
| Resolution in Digits | 5 1/2 |
| Execution Option | Configure and Measure |
| Aperture Time (s) | -1 (Auto) |
| Settle Time (s) | -1 (Auto) |
| AC Min Frequency | 40 Hz |
| Enable Trigger? | False |
| Trigger Source | Immediate |
| Trigger Delay (s) | -1 (Auto) |
| Slope | Rising |

The listed range for each function include all possible ranges for all
 NI-DMM instruments. If you select a range that is not supported for your DMM, the
 upper supported range is automatically selected. Use the DMM»Execution Setting output to verify the actual execution values.

#### DMM Trigger Methods

If the physical signal is already active, a DMM can begin a measurement immediately
 when the read function executes within a Config and Measure VI when the Measure Only
 execution option is specified. Use the NI-DMM driver software to add software delays
 or specify a trigger delay to insert a user-defined delay before the measurement
 starts.

The following figure illustrates a block diagram configured for immediate measurement
 with a delay based on a DAQ analog output signal.

Note

[IMAGE alt='image' src='GUID-77165859-FEA5-4255-8F44-4AFD9A9FE81F-a5.png']

The DMM can start measurements using an external signal or internal TTL
 (X) channel configured as the HW Trigger
 Source. On a PXIe system, TTL (X) is connected
 to the PXI_Trigger(X) internal signal. For example, you can use
 a DAQ_6363/PXI_Trig0 as a start trigger by linking it to
 TTL 0 as the trigger source. When the read function
 executes inside the Configure and Measure VI, the DMM waits for the external signal
 and then waits for the duration of any specified trigger delay.

This configuration uses only a parallel physical signal.

The following figure illustrates a block diagram configured to use an hardware
 trigger source asynchronously.

[IMAGE alt='image' src='GUID-1A9D0640-CFB8-48F7-A9A0-82D56867EB76-a5.png']

Parent topic:

Measurement Libraries

<!--NI_TOPIC bundle=pcb-assembly-test-toolkit-labview path=dmm-resistance-measure-library.html language=enus -->
## TOPIC 00019: DMM_Resistance Measurement Library (2-Wire and 4-Wire)

- bundle_id: `pcb-assembly-test-toolkit-labview`
- source_path: `dmm-resistance-measure-library.html`
- source_url: https://docs-be.ni.com/bundle/pcb-assembly-test-toolkit-labview/raw/resource/enus/dmm-resistance-measure-library.html
- document_id: `pcb-assembly-test-toolkit-labview`
- page_type: `leaf`
- content_type: `reference`
- source_description: DMM_Resistance Measurement Library VIs initialize, configure, and close 2-Wire and 4-Wire resistance measurements. The DMM_Resistance Meas Initialize VI creates a new NI-DMM driver session on the device specified by the DMM Resource Name control. The device uses the specified powerline frequency val

### DMM_Resistance Measurement Library (2-Wire
 and 4-Wire)

DMM_Resistance Measurement Library VIs initialize, configure, and close 2-Wire and
 4-Wire resistance measurements.

The DMM_Resistance Meas Initialize VI creates a new NI-DMM
 driver session on the device specified by the DMM Resource Name control. The device
 uses the specified powerline frequency value to select a timebase for setting the
 Aperture Time property in powerline cycles (PLCs).

Note

50 Hz

60 Hz

The DMM_Resistance Meas Configure and Measure VI configures the
 NI-DMM frequency or period measurement on the resource provided by the DMM Handle In
 control.

Note

The DMM_Resistance Meas Configure and Measure VI configures the
 measurement based on the following settings.

- 
- Function Settings —Specifies the desired 2-wire or 4-wire function and range, and the
 resolution in digits for the measurement. Refer to Default
 Values and Automatic Range Coercion for more information
 about listed ranges.
- Execution Option Settings —By default, the Configure and Measure VI also executes the
 measurement. If you are using a trigger for your measurement, choose
 the Configure Only or Measure Only execution option to avoid
 automatic execution.
- Configure and Measure —Configures the DMM according to the values provided on the front panel and
 executes the measurement.
- Configure Only —Sets the configuration of the DMM but does not execute the measurement. This option can be
 useful to prepare a trigger and wait for a software or hardware event. This
 operation must be followed by a Measure Only operation.
- Measure Only —Skips configuration to perform a DMM read. Formats the result into a string and outputs the
 effective execution settings to an output cluster. A Measure Only operation
 must be preceded by a Configure Only operation. If repeated, a DMM Measure Only operation uses the most recent DMM
 Configure Only configuration.

Timing & Trigger Settings

The DMM_Resistance Meas Configure and Measure VI returns the
 following information.

Measurement

DMM execution settings

The DMM_Resistance Meas Close VI closes the NI-DMM session
 specified by DMM Handle In and releases the resource.

#### Examples

Figure 44.

[IMAGE alt='image' src='GUID-7FCB0976-FF81-4104-80D2-F32589083480-a5.png']

If repeated, a DMM Measure Only operation uses the most recent DMM
 Configure Only configuration.

Figure 45.

[IMAGE alt='image' src='GUID-9F7474DD-8BE7-4E1D-B9C3-5D7F7D71660C-a5.png']

#### Default Values and Automatic Range
 Coercion

Use the VI context help and block diagram comments to understand the impact of
 each parameter. Adjust the default values only when necessary for your
 application.

| Parameter Name | Default Value |
| --- | --- |
| Power Frequency | 50 Hz |
| Range and Function | First main function in Auto Range for each physical quantity |
| Resolution in Digits | 5 1/2 |
| Execution Option | Configure and Measure |
| Aperture Time (s) | -1 (Auto) |
| Settle Time (s) | -1 (Auto) |
| AC Min Frequency | 40 Hz |
| Enable Trigger? | False |
| Trigger Source | Immediate |
| Trigger Delay (s) | -1 (Auto) |
| Slope | Rising |

The listed range for each function include all possible ranges for all
 NI-DMM instruments. If you select a range that is not supported for your DMM, the
 upper supported range is automatically selected. Use the DMM»Execution Setting output to verify the actual execution values.

#### DMM Trigger Methods

If the physical signal is already active, a DMM can begin a measurement immediately
 when the read function executes within a Config and Measure VI when the Measure Only
 execution option is specified. Use the NI-DMM driver software to add software delays
 or specify a trigger delay to insert a user-defined delay before the measurement
 starts.

The following figure illustrates a block diagram configured for immediate measurement
 with a delay based on a DAQ analog output signal.

Note

[IMAGE alt='image' src='GUID-77165859-FEA5-4255-8F44-4AFD9A9FE81F-a5.png']

The DMM can start measurements using an external signal or internal TTL
 (X) channel configured as the HW Trigger
 Source. On a PXIe system, TTL (X) is connected
 to the PXI_Trigger(X) internal signal. For example, you can use
 a DAQ_6363/PXI_Trig0 as a start trigger by linking it to
 TTL 0 as the trigger source. When the read function
 executes inside the Configure and Measure VI, the DMM waits for the external signal
 and then waits for the duration of any specified trigger delay.

This configuration uses only a parallel physical signal.

The following figure illustrates a block diagram configured to use an hardware
 trigger source asynchronously.

[IMAGE alt='image' src='GUID-1A9D0640-CFB8-48F7-A9A0-82D56867EB76-a5.png']

Parent topic:

Measurement Libraries

Related information:

- System Considerations for Resistance Measurements

<!--NI_TOPIC bundle=pcb-assembly-test-toolkit-labview path=dmm-scan-16v-15c-library.html language=enus -->
## TOPIC 00020: DMM_Scan PXI Mux PXI Shunt 16V-15C Library

- bundle_id: `pcb-assembly-test-toolkit-labview`
- source_path: `dmm-scan-16v-15c-library.html`
- source_url: https://docs-be.ni.com/bundle/pcb-assembly-test-toolkit-labview/raw/resource/enus/dmm-scan-16v-15c-library.html
- document_id: `pcb-assembly-test-toolkit-labview`
- page_type: `leaf`
- content_type: `reference`
- source_description: The DMM_Scan PXI Mux PXI Shunt 16V-15C Library VIs initialize, configure, scan, and measure a list of channels from multiple DMM functions, as well as close the scan on the NI-DMM, SWITCH MUX, or SWITCH shunt relay instrument. This library performs a specific scan configuration that is assigned in a

### DMM_Scan PXI Mux PXI Shunt 16V-15C
 Library

The DMM_Scan PXI Mux PXI Shunt 16V-15C Library VIs initialize, configure,
 scan, and measure a list of channels from multiple DMM functions, as well as close the
 scan on the NI-DMM, SWITCH MUX, or SWITCH shunt relay instrument.

This
 library performs a specific scan configuration that is assigned in a random order to a
 combination of 16 voltage type (maximum) and 15 current type (maximum) measurements in a
 2-wire (differential) configuration.

This library supports 16 voltage type
 differential measurements, 15 current differential measurements, and 15 free SPST
 relays.

#### Recommended Hardware

- PXI chassis (hybrid) and controller
- PXI-4065 or PXIe-408x DMM
- PXIe-2527 (or similar multiplexer switch module) with TB-2627 terminal block
- HV6-BAN4 cable to connect the DMM to the TB-2627 terminal block
- PXI-2568 or similar relay module with individual SPST relays for the current
 shunt continuity function

#### Recommended Hardware
 Configuration

This section outlines the recommended connections, using the PXIe-2527 or similar multiplexer
 switch module configured in a dual topology:

- 16 voltage-based 2-wire measurements ( ch0 to
 ch15 ) connected to the DMM HI/LO
- 15 current-based 2-wire measurements ( ch16 to
 ch30 ) connected to the same DMM to CURRENT/LO

[IMAGE alt='image' src='GUID-7138D6EA-A50B-4531-9B9F-DA579A7D43C2-a5.svg']

The following figure depicts the connections for the PXI-2568 or similar relay
 module, as shunt, dedicated to 15 current-based 2-wire measurements
 (ch16 to ch30). Use a configuration in
 parallel with the current channels to simplify connections and maintain continuity
 of DUT power during all measurements.

[IMAGE alt='image' src='GUID-79D15AA9-AF2B-4216-B9D4-8A1A25C9B9A5-a5.svg']

The following figures illustrate example PXI Mux PXI Shunt connections for a DMM SCAN using
 the PXIe-2527 and PXI-2568.

[IMAGE alt='image' src='GUID-3CD2AF62-F975-4B86-B3EE-157EF27E5B18-a5.png']

#### Software Recommendations

For voltage and current measurements, you must individually declare, in any order,
 the channels, functions and ranges, and digits in the scan list.

For timing optimization, the software removes the configuration phase between
 multiplexer scans when sequential channels in the scan list use the same
 configuration.

By default, all shunt relays are closed by the Initialize VI. This behavior can be
 disabled with the Close All Shunts control.

To measure only a list of resistances, disable the Close All
 Shunts control Initialize VI. The DUT does not receive power because
 all shunt relays are open.

#### Library VI Descriptions

The DMM_Scan PMPS 16V-15C Initialize VI creates a NI-DMM Scan
 driver session on each device specified by the Scan Resource Names control. The
 device uses the specified powerline frequency value to select a timebase for setting
 the Aperture Time property in powerline cycles (PLCs).

Note

50 Hz

60 Hz

By default, the DMM_Scan PMPS 16V-15C Initialize VI randomly defines a
 specific switch topology with a fixed channel mapping for the 16 (maximum) voltage
 and 15 (maximum) current measurement configuration. Each current channel number is
 linked to the equivalent channel shunt number. For example, Current
 ch16 is linked to Shunt ch16.

Enable the Close all Shunts control to close all shunt relays
 from channels 16 to 30 in a fixed channel topology mapping and allow continuous
 power to the DUT during all measurements. disable the control for a
 2-Wire Resistance measurement function without any
 current through the DUT.

The DMM_Scan PMPS 16V-15C Initialize VI returns the maximum
 voltage and current characteristics from each multiplexer and shunt relay.

DMM_Scan PMPS 16V-15C Configure and Measure

Scan Configuration

chX

The DMM_Scan PMPS 16V-15C Configure and Measure VI returns the
 following information.

Formatted Measurements

Raw Measurements

Total Scan Time (s)

The DMM_Scan PMPS 16V-15C Close VI disconnects all multiplexer and shunt
 relays, closes the NI-DMM and NI-SWITCH scan sessions associated with the scan
 resources, and releases all resources.

The following figure illustrates the minimum usage block diagram, with a loop, for this
 library.

[IMAGE alt='image' src='GUID-EC4B98CA-9D05-43D0-B2EC-460D361D8C2B-a5.png']

The following figure illustrates two sequential DMM scans that use different
 configurations:

[IMAGE alt='image' src='GUID-58F0FCC4-C49B-40B6-A6FB-092B6863B8ED-a5.png']

Parent topic:

DMM_Scan Libraries

<!--NI_TOPIC bundle=pcb-assembly-test-toolkit-labview path=dmm-scan-daq-ext-relay.html language=enus -->
## TOPIC 00021: DMM_Scan DAQ External Relay

- bundle_id: `pcb-assembly-test-toolkit-labview`
- source_path: `dmm-scan-daq-ext-relay.html`
- source_url: https://docs-be.ni.com/bundle/pcb-assembly-test-toolkit-labview/raw/resource/enus/dmm-scan-daq-ext-relay.html
- document_id: `pcb-assembly-test-toolkit-labview`
- page_type: `leaf`
- content_type: `reference`
- source_description: The DMM_Scan DAQ Ext RLY Library VIs initialize, configure, scan, and measure a list of channels from multiple DMM functions, as well as close the scan on the NI-DMM and NI-DAQmx digital outputs used to control individual external relays to perform both MUX and SWITCH shunt relay functions. This lib

### DMM_Scan DAQ External Relay

The DMM_Scan DAQ Ext RLY Library VIs initialize, configure, scan, and measure a
 list of channels from multiple DMM functions, as well as close the scan on the NI-DMM
 and NI-DAQmx digital outputs used to control individual external relays to perform both
 MUX and SWITCH shunt relay functions.

This library uses custom mapping and topology configurations to support any DAQ device and port
 structure, including C Series relay driver modules or DIO TTL devices with external
 amplification. You must use dual-pole external relays (DPST) for differential
 measurements attached to any DO line channel. The hardware mapping has a fixed
 declaration priority that lists voltage channels first, followed by current channels,
 and then shunt channels.

This library supports the measurement of any number and combination of voltage or current
 type functions based on DAQ digital output channels.

#### Recommended Hardware

Choose one of the following recommended hardware configurations.

- PXI chassis (hybrid) and controller
- PXI-4065 or PXIe-408x DMM
- PXIe-6363 or other NI 63xx (X Series) DAQ device to execute both multiplexer
 and current shunt functions using dual-pole external relays

- PC-based controller system
- USB cDAQ-917x chassis
- USB-4065 DMM
- NI-947x C Series digital output module to execute both multiplexer and
 current shunt functions using dual-pole external relays

#### Recommended Hardware Configuration

This recommended configuration uses the 48-channel PXIe-6363 in a mixed voltage and current
 2-wire (differential) scan configuration. The topology maps a custom number of
 2-wire voltage-based measurements connected to HI/LO on the DMM, followed by a
 custom number of 2-wire current based measurements to CURRENT/LO on the same DMM.

The following figures illustrate example custom channel connections for a DMM SCAN
 with DAQ external relays using the PXIe-6363.

[IMAGE alt='image' src='GUID-E7D6C4AD-A741-4856-B3C4-0384C983149C-a5.png']

[IMAGE alt='image' src='GUID-B03F1B8D-AE18-4D0C-B4D2-C0549EC9BA26-a5.png']

The following figure illustrates a custom topology mapping.

Figure 50.

[IMAGE alt='image' src='GUID-989AC730-B2E6-41DE-B51A-08B64984C6C7-a5.png']

The Initialize VI returns a topology mapping to simplify connections and
 maintenance.

[IMAGE alt='image' src='GUID-69105D47-2ADE-479F-B88A-A4FE26260A08-a5.png']

#### Software Recommendations

For voltage and current measurements, you must individually declare, in any order,
 the channels, functions and ranges, and digits in the scan list.

For timing optimization, the software removes the configuration phase between
 multiplexer scans when sequential channels in the scan list use the same
 configuration.

By default, all shunt relays are closed by the Initialize VI. This behavior can be
 disabled with the Close All Shunts control.

To measure only a list of resistances, disable the Close All
 Shunts control for the Initialize VI. The DUT does not receive power
 because all shunt relays are open.

#### Library VI Descriptions

The DMM_Scan DER 32V-16C Initialize VI creates a NI-DMM Scan
 driver session on each device specified by the Scan Resource Names control. The
 device uses the specified powerline frequency value to select a timebase for setting
 the Aperture Time property in powerline cycles (PLCs).

Note

50 Hz

60 Hz

You must make hardware mapping declarations in the following order:

1. Declare your custom hardware mapping and topology configuration. You can use any
 DAQ device and port structure, including cDAQ relay driver modules and DIO TTL
 devices with external amplification.
2. Declare the positions for the voltage type channels.
3. Declare the list of current type channels.
4. Declare the numeric difference, or shift, between the first current channel and
 the first current shunt.

You can scan all channels randomly with each measurement type in a 2-wire
 (differential) configuration. You must use dual-pole external relays (DPST) for
 differential measurements attached to any DO line channel.

By default, the DMM_Scan DER 32V-16C Initialize VI randomly
 defines a specific switch topology with a fixed channel mapping for the 32 voltage
 (maximum) and 15 current (maximum) measurement configuration. Each current channel
 is linked to the shunt channel according to the following pattern: shunt
 channel number = current measurement channel number + 16. For
 example, current ch32 is linked to shunt
 ch48.

Enable the Close all Shunts control to close all DAQ DO lines
 attached to declared shunt relays and allow continuous power to the DUT during all
 measurements. disable the control for a 2-Wire Resistance
 measurement function without any current through the DUT.

Use the Relays Debounce Time (ms) control to define the
 debounce timing specifications for external relays. The typical default value is 5
 ms. Adjust the value for your specific external relay. Values that are too small
 introduce errors in measurements accuracy.

The DMM_Scan DER 32V-16C Initialize VI returns a Topology
 Mapping Output. Use this output to check your mapping declaration and simplify
 connecting the appropriate channels for your device. The output can also simplify
 maintenance and later hardware modifications. For shunt channels, the VI returns the
 link to the current measurement channel.

DMM_Scan DER 32V-16C Configure and Measure

Scan Configuration

chX

Default Values and
 Automatic Range Coercion

The DMM_Scan DER 32V-16C Configure and Measure VI returns the
 following information.

Formatted Measurements

Raw Measurements

Total Scan Time (s)

The DMM_Scan DER 32V-16C Close VI opens all relays, closes the
 NI-DAQmx and NI-DMM Scan sessions associated with the specified scan resource DMM
 handles, and releases all resources.

The following figure illustrates the minimum usage block diagram, with a loop, for this
 library.

[IMAGE alt='image' src='GUID-C6975717-B09A-45CB-98A6-225BDBD2B05C-a5.png']

The following figure illustrates two sequential DMM scans that use different
 configurations:

[IMAGE alt='image' src='GUID-B2BBB896-0AFC-4DE2-9951-94231131941F-a5.png']

Parent topic:

DMM_Scan Libraries

<!--NI_TOPIC bundle=pcb-assembly-test-toolkit-labview path=dmm-scan-libraries.html language=enus -->
## TOPIC 00022: DMM_Scan Libraries

- bundle_id: `pcb-assembly-test-toolkit-labview`
- source_path: `dmm-scan-libraries.html`
- source_url: https://docs-be.ni.com/bundle/pcb-assembly-test-toolkit-labview/raw/resource/enus/dmm-scan-libraries.html
- document_id: `pcb-assembly-test-toolkit-labview`
- page_type: `leaf`
- content_type: `reference`
- source_description: The PCB Assembly Test Toolkit for LabVIEW includes three DMM Scan libraries to support a broad range of hardware configurations. The following figure describes the general software structure and configuration used for all DMM_Scan libraries. By default, during the initialize function, all shunt chan

### DMM_Scan Libraries

The PCB Assembly Test
 Toolkit for LabVIEW includes three DMM Scan libraries to
 support a broad range of hardware configurations.

[IMAGE alt='image' src='GUID-DADE8C34-360C-4C1F-98AF-FCB4F9B4C0A7-a5.svg']

1. By default, during the initialize function, all shunt channels are closed to
 maintain continuity of current to power the DUT.
2. Each element (channel, function, range, digits) from the scan list is
 selected sequentially in the main loop.
3. The mux channels for voltage-type functions are closed based on the
 corresponding path.
4. If the channel is a current-type, the shunt channel is open to enable DMM
 current measurement.
5. The shunt channel is closed to maintain continuity between scans.
6. The mux channel is open.

- Do not open or close the shunt channel relay for voltage-only functions.
- Do not reconfigure the DMM if the next channel configuration is the
 same. Execute the measurement using the existing configuration
 parameters.

Parent topic:

Measurement Libraries

<!--NI_TOPIC bundle=pcb-assembly-test-toolkit-labview path=dmm-scan-pxi-relay.html language=enus -->
## TOPIC 00023: DMM_Scan PXI Relay Driver 32V-16C Library

- bundle_id: `pcb-assembly-test-toolkit-labview`
- source_path: `dmm-scan-pxi-relay.html`
- source_url: https://docs-be.ni.com/bundle/pcb-assembly-test-toolkit-labview/raw/resource/enus/dmm-scan-pxi-relay.html
- document_id: `pcb-assembly-test-toolkit-labview`
- page_type: `leaf`
- content_type: `reference`
- source_description: The DMM_Scan PXI RLY Driver 32V-16C library VIs initialize, configure, scan, and measure a list of channels from multiple DMM functions, as well as close the scan on the NI-DMM combined with a single SWITCH individual relay driver used to execute both MUX and SWITCH Shunt Relay functions.This librar

### DMM_Scan PXI Relay Driver 32V-16C
 Library

The DMM_Scan PXI RLY Driver 32V-16C library VIs initialize, configure, scan,
 and measure a list of channels from multiple DMM functions, as well as close the scan on
 the NI-DMM combined with a single SWITCH individual relay driver used to execute both
 MUX and SWITCH Shunt Relay functions.

This library is intended to perform
 a specific scan configuration in random order for a combined maximum of 32 voltage type
 and 16 current type measurements in a 2-wire (differential) configuration.

This
 library supports 32 voltage type differential measurements and 16 current differential
 measurements.

#### Recommended Hardware

- PXI chassis (hybrid) and controller
- PXI-4065 or PXIe-408x DMM
- PXI-2567 (or similar relay driver module) to execute both multiplexer and current shunt
 functions using dual-pole external relays.

#### Recommended Hardware
 Configuration

This section outlines the recommended connections, using the recommended PXI-2567 or
 similar relay driver module configured in a mapped topology:

- 32 voltage-based 2-wire measurements ( ch0 to
 ch31 ) connected to the DMM HI/LO
- 15 current-based 2-wire measurements ( ch32 to
 ch47 ) connected to the same DMM to CURRENT/LO
- Current shunt channels on the remaining channels ( ch48 to
 ch63 ) of the switch relay driver. Note To simplify connections and
 ensure DUT power continuity through all measurements, map the shunt channels
 in the same order as the current measurement channels. With this mapping,
 the shunt channel number is always equivalent to the current
 measurement channel number + 16.

[IMAGE alt='image' src='GUID-FB112B73-4BDC-4A53-87C1-EB23F4931D0A-a5.svg']

Notice

The following figures illustrate example connections for a DMM SCAN using the
 PXI-2567.

[IMAGE alt='image' src='GUID-52B00EAD-A4F2-4391-BA8A-69FE246980B5-a5.png']

[IMAGE alt='image' src='GUID-4422A5F2-85BF-48D4-AEB9-672CF20D2220-a5.png']

#### Software Recommendations

For voltage and current measurements, you must individually declare, in any order,
 the channels, functions and ranges, and digits in the scan list.

For timing optimization, the software removes the configuration phase between
 multiplexer scans when sequential channels in the scan list use the same
 configuration.

By default, all shunt relays are closed by the Initialize VI. This behavior can be
 disabled with the Close All Shunts control.

To measure only a list of resistances, disable the Close All
 Shunts control for the Initialize VI. The DUT does not receive power
 because all shunt relays are open.

#### Library VI Descriptions

The DMM_Scan PRD 32V-16C Initialize VI creates a NI-DMM Scan
 driver session on each device specified by the Scan Resource Names control. The
 device uses the specified powerline frequency value to select a timebase for setting
 the Aperture Time property in powerline cycles (PLCs).

Note

50 Hz

60 Hz

By default, the DMM_Scan PRD 32V-16C Initialize VI randomly
 defines a specific switch topology with a fixed channel mapping for the 32 (maximum)
 voltage and 16 (maximum) current measurement configuration. Each current channel is
 linked to the shunt channel according to the following pattern: shunt
 channel number = current measurement channel number + 16. For
 example, current ch32 is linked to shunt
 ch48.

Enable the Close all Shunts control to close all shunt relays
 from channels 48 to 63 in a fixed channel topology mapping and allow continuous
 power to the DUT during all measurements. disable the control for a
 2-Wire Resistance measurement function without any
 current through the DUT.

Use the Relays Debounce Time (ms) control to define the
 debounce timing specifications for external relays. The typical default value is 5
 ms. Adjust the value for your specific external relay. Values that are too small
 introduce errors in measurements accuracy.

If the NI multiplexer uses embedded relays the DMM_Scan PRD 32V-16C
 Initialize VI returns the switch maximum voltage and current
 characteristics from each multiplexer and shunt relay. For external custom relays
 and the NI 2567 Relay Driver, the return values are 0.

DMM_Scan PRD 32V-16C Configure and Measure

Scan Configuration

chX

Default Values and
 Automatic Range Coercion

The DMM_Scan PRD 32V-16C Configure and Measure VI returns the
 following information.

Formatted Measurements

Raw Measurements

Total Scan Time (s)

The DMM_Scan PRD 32V-16C Close VI disconnects all multiplexer
 and shunt relays, closes the NI-DMM and NI-SWITCH Scan sessions associated with the
 scan resources, and releases all resources.

The following figure illustrates the minimum usage block diagram, with a loop, for this
 library.

[IMAGE alt='image' src='GUID-A02249A1-0B95-42F7-AE50-37042350D6A8-a5.png']

The following figure illustrates two sequential DMM scans that use different
 configurations:

[IMAGE alt='image' src='GUID-4DDE690C-9D9D-481D-A923-1FD6A9135C50-a5.png']

Parent topic:

DMM_Scan Libraries

<!--NI_TOPIC bundle=pcb-assembly-test-toolkit-labview path=dynamic-digital-pattern-gen.html language=enus -->
## TOPIC 00024: DAQ_Dynamic Digital Pattern Generation Library

- bundle_id: `pcb-assembly-test-toolkit-labview`
- source_path: `dynamic-digital-pattern-gen.html`
- source_url: https://docs-be.ni.com/bundle/pcb-assembly-test-toolkit-labview/raw/resource/enus/dynamic-digital-pattern-gen.html
- document_id: `pcb-assembly-test-toolkit-labview`
- page_type: `leaf`
- content_type: `reference`
- source_description: DAQ_Dynamic Digital Pattern Generation Library VIs initialize, configure, generate, and close user-configurable digital output pins. This library is applicable for digital output modules and channels that support hardware-timed digital waveform characteristics. This library supports both Port and Di

### DAQ_Dynamic Digital Pattern Generation
 Library

DAQ_Dynamic Digital Pattern Generation Library VIs initialize, configure, generate, and
 close user-configurable digital output pins. This library is applicable for digital
 output modules and channels that support hardware-timed digital waveform
 characteristics.

Note

1. Use the DAQ_Dyn Dig Gen Initialize VI to initialize hardware and create a DAQmx
 Task for dynamic digital pattern generation.
2. Pass the dynamic digital pattern generation DAQmx Task to the DAQ_Dyn Dig Gen Configure
 and Measure VI.
3. Configure the DAQ_Dyn Dig Gen Configure and Measure VI.
  - 
  - Configuration Settings —Configure the timing related parameters for dynamic digital pattern generation. The
 Timing setting configures sample clock source input,
 sampling rate, number of samples, and the sample timing
 engine used for the dynamic digital pattern generation
 task. Note For NI
 63xx (X Series) and other DAQ devices, use Auto mode
 only. The sample timing engine is only used for cDAQ and
 TestScale platforms, which support multiple timing
 engines. Note Refer to the relevant specifications document to
 identify the maximum sampling rate for your device.
 Values that exceed the maximum sampling rate generate
 errors. Configure triggers to start the source
 or measurement based on various trigger events. Trigger
 options include no trigger or digital start
 triggers. Note Triggers
 are not supported for serial modules including C Series
 and TestScale TS-15120 and TS-15130 devices. Refer to
 the *Timed digital input/output restrictions*
 section of *Digital I/O Considerations for C Series
 and TestScale Devices* for a list of
 limitations to consider for hardware-timed digital
 tasks. Configure the Port Digital Data to
 specify the integer data for the port used. Note DAQmx
 does not evaluate the size of the port and internally
 ignores the other bits.
    - Acquisition Time = Number of Samples/Sample Rate
    - Specify Auto to automatically select the timing
 engine.
  - Output Data —The VI outputs the total generation time in seconds.
4. Wire the updated dynamic digital pattern generation task from DAQmx Task Out.
5. Close the dynamic digital pattern generation task using DAQ_Dyn Dig Gen Close VI.

Figure 31.

[IMAGE alt='image' src='GUID-11601CE5-DFEE-43F9-BB69-DEA69A3E4CE9-a5.png']

Parent topic:

Measurement Libraries

Related information:

- Digital I/O Considerations for C Series and TestScale
 Devices

<!--NI_TOPIC bundle=pcb-assembly-test-toolkit-labview path=dynamic-digital-pattern-measure.html language=enus -->
## TOPIC 00025: DAQ_Dynamic Digital Pattern Measurement Library

- bundle_id: `pcb-assembly-test-toolkit-labview`
- source_path: `dynamic-digital-pattern-measure.html`
- source_url: https://docs-be.ni.com/bundle/pcb-assembly-test-toolkit-labview/raw/resource/enus/dynamic-digital-pattern-measure.html
- document_id: `pcb-assembly-test-toolkit-labview`
- page_type: `leaf`
- content_type: `reference`
- source_description: DAQ_Dynamic Digital Pattern Measurement Library VIs enable dynamic digital measurements on one or more digital channel lines or on an entire port in a digital module. This library is applicable for TestScale digital input modules or channels that support hardware-timed digital waveform characteristi

### DAQ_Dynamic Digital Pattern Measurement
 Library

DAQ_Dynamic Digital Pattern Measurement Library VIs enable dynamic digital measurements
 on one or more digital channel lines or on an entire port in a digital module. This
 library is applicable for TestScale digital input modules or channels that support
 hardware-timed digital waveform characteristics.

Note

1. Use the DAQ_Dyn Dig Meas Initialize VI to initialize hardware and create a DAQmx
 Task for dynamic digital pattern measurement.
2. Pass the dynamic digital pattern measurement DAQmx Task to the DAQ_Dyn Dig Meas Configure
 and Measure VI.
3. Configure the DAQ_Dyn Dig Meas Configure and Measure VI.
  - 
  - Configuration Settings —Configure the timing related parameters for dynamic digital pattern measurement. The
 Timing setting configures sample clock source input,
 sampling rate, number of samples, and the sample timing
 engine used for the DAQmx Task. Note For NI
 63xx (X Series) and other DAQ devices, use Auto mode
 only. The sample timing engine is only used for cDAQ and
 TestScale platforms, which support multiple timing
 engines. Note Refer to the relevant specifications document to
 identify the maximum sampling rate for your device.
 Values that exceed the maximum sampling rate generate
 errors. Configure triggers to start the source
 or measurement based on various trigger events. Trigger
 options include no trigger or digital start
 triggers.
    - Acquisition Time = Number of Samples/Sample Rate
    - Specify Auto to automatically select the timing
 engine.
  - Output Data —The VI outputs the following data.
  - Measured Digital Pattern —Displays the captured digital voltage
 waveforms.
  - Port Digital Data —Provides the derived post-analyzed port digital
 data in U32 format from the captured digital
 patterns.
4. Wire the updated dynamic digital pattern measurement task from DAQmx Task Out.
5. Close the dynamic digital pattern measurement task using DAQ_Dyn Dig Meas Close VI.

#### Best Practices

- For faster measurements, set the maximum sampling rate possible for the given
 Sample Clock Source input and assign a smaller Number of Samples to
 capture.
- For better resolution, increase the number of samples (for example, 1000
 samples).

Figure 30.

[IMAGE alt='image' src='GUID-060C9D57-9555-4B18-9F0B-63DBB068EA0D-a5.png']

Parent topic:

Measurement Libraries

<!--NI_TOPIC bundle=pcb-assembly-test-toolkit-labview path=freq-measure-library.html language=enus -->
## TOPIC 00026: DAQ_Frequency Domain Measurement Library

- bundle_id: `pcb-assembly-test-toolkit-labview`
- source_path: `freq-measure-library.html`
- source_url: https://docs-be.ni.com/bundle/pcb-assembly-test-toolkit-labview/raw/resource/enus/freq-measure-library.html
- document_id: `pcb-assembly-test-toolkit-labview`
- page_type: `leaf`
- content_type: `reference`
- source_description: DAQ_Frequency Domain Measurement Library VIs initialize, configure, measure, and close user-configurable analog input pins and derive frequency domain measurements for the measured waveforms. This library is applicable for analog input channels and modules. Use the DAQ_FDV Meas Initialize VI to init

### DAQ_Frequency Domain Measurement
 Library

DAQ_Frequency Domain Measurement Library VIs initialize, configure, measure, and close
 user-configurable analog input pins and derive frequency domain measurements for the
 measured waveforms. This library is applicable for analog input channels and
 modules.

1. Use the DAQ_FDV Meas Initialize VI to initialize hardware and create a DAQmx Task for
 frequency domain measurement.
2. Pass the frequency domain measurement DAQmx Task to the DAQ_FDV Meas Configure and Measure
 VI.
3. Configure the DAQ_FDV Meas Configure and Measure VI.
  - 
  - Execution Settings —By default, the Configure and Measure VI also executes the
 measurement. If you are using a trigger for your
 measurement, choose the Configure Only or Measure Only
 execution option to avoid automatic execution. Use the
 Skip Analysis? setting to select whether to perform
 post-analysis on the measured data. Use post analysis to
 derive maximum voltage, current, power, and average
 power.
  - Configuration Settings —Configure the range and terminal settings. Global settings are applied to any channel
 without channel-specific settings. Use the Specific Channel
 Settings to configure a channel, including physical analog
 input voltage channels, to a specific limit. Configure
 the timing related parameters for frequency domain
 measurement. The Timing setting configures sample clock
 source input, sampling rate, number of samples, and the
 sample timing engine used for the DAQmx Task.Acquisition Time = Number of Samples/Sample Rate
 Specify Auto to automatically select the timing
 engine. Note For NI
 63xx (X Series) and other DAQ devices, use Auto mode
 only. The sample timing engine is only used for cDAQ and
 TestScale platforms, which support multiple timing
 engines. Note Refer to
 the relevant specifications document to identify the
 maximum sampling rate for your device. Values that
 exceed the maximum sampling rate generate errors. Configure triggers to start the source or
 measurement based on various trigger events. Trigger
 options include no trigger or digital start
 triggers.
  - Measurement Settings —Choose whether to perform periodic waveform measurements. To
 capture periodic waveforms you must capture multiple
 cycles. Configure the Voltage Frequency (Hz), Voltage
 Waveform Period (s) and Voltage Waveform duty cycle (%)
 values.
  - Output Data —The VI outputs the following data.
  - Voltage Waveforms —Displays the captured voltage waveforms.
  - Frequency Domain Measurements —Provides the derived post-analyzed data from the
 captured frequency domain waveforms.
  - Acquisition Time —Calculated acquisition time for the measurement.
4. Wire the updated frequency domain measurement task from DAQmx Task Out.
5. Close the frequency domain measurement task using DAQ_FDV Meas Close VI.

#### Execution Option Settings

Configure and Measure

Configure Only

Measure Only

#### Best Practices

- For faster measurements, set the maximum sampling rate possible for the given
 Sample Clock Source input and assign a smaller Number of Samples to
 capture.
- For better resolution, increase the number of samples (for example, 1000
 samples).

Figure 25.

[IMAGE alt='image' src='GUID-C1492AE3-92B8-43F4-B882-66F4634EE385-a5.png']

Parent topic:

Measurement Libraries

<!--NI_TOPIC bundle=pcb-assembly-test-toolkit-labview path=full-test-vi.html language=enus -->
## TOPIC 00027: PCB Assembly Test Toolkit for LabVIEW: Creating a Full Test LabVIEW VI

- bundle_id: `pcb-assembly-test-toolkit-labview`
- source_path: `full-test-vi.html`
- source_url: https://docs-be.ni.com/bundle/pcb-assembly-test-toolkit-labview/raw/resource/enus/full-test-vi.html
- document_id: `pcb-assembly-test-toolkit-labview`
- page_type: `leaf`
- content_type: `task`
- source_description: Before you begin, you must create a PCBATT LabVIEW project. Refer to Launching the Toolkit in LabVIEW for details. You will use the path to your project in the following procedure. Launch LabVIEW and open a new VI. Add required VIs to the block diagram. You can access PCB Assembly Test Toolkit for L

### Creating a Full Test LabVIEW VI

Note

Launching the Toolkit in LabVIEW

1. Launch LabVIEW and open a new VI.
2. Add required VIs to the block diagram. You can access PCB Assembly Test
 Toolkit for LabVIEW LabVIEW VIs from your PCBATT LabVIEW
 project.
3. Wire the VIs and create any necessary controls in the front panel. The
 following image illustrates wiring for a simple block diagram. [IMAGE alt='image' src='GUID-E28ADD71-B9D3-4D8F-B3AE-0ED711D4433D-a5.png']
4. Click File»Save As to save the VI.
5. Configure the front panel and run the VI to test your functionality.

The following image depicts an example of a full test VI that uses the timing engine
 from the power supply as a trigger to synchronize the analog input and make a
 measurement.

[IMAGE alt='image' src='GUID-AEC1E8CA-F263-4FA2-823F-4EB8A7DCF916-a5.png']

Parent topic:

Using the PCB Assembly Test Toolkit for LabVIEW

Related reference:

- Launching the Toolkit in LabVIEW

<!--NI_TOPIC bundle=pcb-assembly-test-toolkit-labview path=installing-pcba-toolkit-package.html language=enus -->
## TOPIC 00028: Installing the PCB Assembly Test Toolkit for LabVIEW

- bundle_id: `pcb-assembly-test-toolkit-labview`
- source_path: `installing-pcba-toolkit-package.html`
- source_url: https://docs-be.ni.com/bundle/pcb-assembly-test-toolkit-labview/raw/resource/enus/installing-pcba-toolkit-package.html
- document_id: `pcb-assembly-test-toolkit-labview`
- page_type: `leaf`
- content_type: `task`
- source_description: Follow these steps to install the PCB Assembly Test Toolkit for LabVIEW with NI Package Manager. Install any related software, including LabVIEW, TestStand, and driver application software, before you install the PCB Assembly Test Toolkit for LabVIEW. Refer to the Software Components topic for a lis

### Installing the PCB Assembly Test
 Toolkit for LabVIEW

Follow these steps to install the PCB Assembly Test
 Toolkit for LabVIEW with NI
 Package Manager.

Note

PCB Assembly Test
 Toolkit for LabVIEW

Software Components

1. Launch NI Package Manager and search for PCB Assembly Test
 Toolkit for LabVIEW .
2. Click the search result for PCB Assembly Test
 Toolkit for LabVIEW . The product page
 appears with the latest available version is automatically selected.
3. Click Install .
4. Review the prompts and complete the installation process.
  - Do not deselect all recommended packages without review. You must install packages
 related to PCB assembly testing, including the following packages, if they are
 recommended: You may accept or reject other recommended software packages based on your
 needs.
    1. NI Certificates Installer
    2. PCB Assembly Test Toolkit LabVIEW Support
    3. PCB Assembly Test Toolkit LabVIEW 2021 32-bit Support
    4. PCB Assembly Test Toolkit LabVIEW 2021 64-bit Support
  - The installer reminds you of the LabVIEW, TestStand, and driver application software
 requirements. If LabVIEW, TestStand, or required drivers are not installed, cancel the
 PCB Assembly Test Toolkit installation and install the required software.
  - You must accept the required license agreements to continue with software
 installation.
5. Restart the computer when installation is complete.

Related reference:

- Software Components

<!--NI_TOPIC bundle=pcb-assembly-test-toolkit-labview path=labview-adapter.html language=enus -->
## TOPIC 00029: Configuring the LabVIEW Adapter in TestStand

- bundle_id: `pcb-assembly-test-toolkit-labview`
- source_path: `labview-adapter.html`
- source_url: https://docs-be.ni.com/bundle/pcb-assembly-test-toolkit-labview/raw/resource/enus/labview-adapter.html
- document_id: `pcb-assembly-test-toolkit-labview`
- page_type: `leaf`
- content_type: `task`
- source_description: PCB Assembly Test Toolkit for LabVIEW Measurement Library VIs require the LabVIEW Development System as the active LabVIEW adapter in TestStand. Launch TestStand. Select Configure Adapters . The Adapter Configuration window appears. Select LabVIEW in the list of adapters and click Configure. The Lab

### Configuring the LabVIEW Adapter in
 TestStand

PCB Assembly Test
 Toolkit for LabVIEW Measurement
 Library VIs require the LabVIEW Development System as the active LabVIEW adapter in
 TestStand.

1. Launch TestStand.
2. Select Configure»Adapters . The Adapter Configuration window appears. [IMAGE alt='image' src='GUID-D397796F-3990-4C5C-806A-CF9F929B7970-a5.png']
3. Select LabVIEW in the list of adapters and click
 Configure . The LabVIEW Adapter Configuration dialog
 appears. [IMAGE alt='image' src='GUID-842E66F4-92BA-4A1F-9DB0-2A54A41A1D4E-a5.png']
4. Select LabVIEW Development System .
5. Click OK . You are prompted to unload modules.
6. Click OK to unload and to reload modules.

Repeat these steps to verify the specified LabVIEW adapter any time you reinstall
 TestStand.

<!--NI_TOPIC bundle=pcb-assembly-test-toolkit-labview path=launch-in-labview.html language=enus -->
## TOPIC 00030: Launching the PCB Assembly Test Toolkit for LabVIEW in LabVIEW

- bundle_id: `pcb-assembly-test-toolkit-labview`
- source_path: `launch-in-labview.html`
- source_url: https://docs-be.ni.com/bundle/pcb-assembly-test-toolkit-labview/raw/resource/enus/launch-in-labview.html
- document_id: `pcb-assembly-test-toolkit-labview`
- page_type: `leaf`
- content_type: `reference`
- source_description: PCB Assembly Test Toolkit for LabVIEW provides measurement and generation libraries to enable common actions performed in PCB assembly electrical functional test. Use these libraries to create or extend your LabVIEW sequencer application. The toolkit also provides LabVIEW examples to help you unders

### Launching the Toolkit in LabVIEW

PCB Assembly Test
 Toolkit for LabVIEW provides measurement and generation libraries
 to enable common actions performed in PCB assembly electrical functional
 test.

Use these libraries to create or extend your LabVIEW sequencer application. The toolkit
 also provides LabVIEW examples to help you understand the toolkit libraries and
 accelerate your own application development.

#### Accessing Toolkit Libraries and Examples

To access
 toolkit libraries and LabVIEW examples, create a new LabVIEW project using the
 included PCBATT sample project template. The project template is organized into
 folders for toolkit functions that contain the relevant library VIs, followed by
 folders for LabVIEW-based examples.

1. Launch LabVIEW.
2. Open the Create Project window.
  - On the LabVIEW welcome screen, click Create
 Project .
  - If LabVIEW is already open, navigate to Project»Create Project .
3. In the Create Project window, select Sample Projects»PCBATT . The PCB Assembly Test
 Toolkit for LabVIEW project type is
 automatically selected. [IMAGE alt='image' src='GUID-56E92D42-CD7A-4D1F-890A-8B060BB522EE-a5.png']
4. Click Next .
5. Enter a Project Name .
6. Optionally, specify a custom Project Root path.
7. Click Finish . LabVIEW generates and displays your new
 project.
8. Click File»Save to save your example project.

Figure 1.

[IMAGE alt='image' src='GUID-E246D6EE-834B-4263-8B24-88041A085CBD-a5.png']

#### LabVIEW Examples

To access LabVIEW examples, create and open a new LabVIEW project using the PCBATT
 Sample Project template. The template includes the toolkit libraries and LabVIEW
 examples.

The provided examples are configured with default values for quick testing. Most
 examples use two toolkit libraries to accomplish generation and measurement in a
 loopback configuration.

Use the DMM examples to explore the methods to use the DMM individual functions or by
 using the DMM Scan library.

Note

Channel Topology Mapping Tester Tool

<!--NI_TOPIC bundle=pcb-assembly-test-toolkit-labview path=launch-in-teststand.html language=enus -->
## TOPIC 00031: Launching the PCB Assembly Test Toolkit for LabVIEW in TestStand

- bundle_id: `pcb-assembly-test-toolkit-labview`
- source_path: `launch-in-teststand.html`
- source_url: https://docs-be.ni.com/bundle/pcb-assembly-test-toolkit-labview/raw/resource/enus/launch-in-teststand.html
- document_id: `pcb-assembly-test-toolkit-labview`
- page_type: `leaf`
- content_type: `task`
- source_description: Use the included TestStand workspace to explore PCB Assembly Test Toolkit for LabVIEW example sequences that you can adapt for your own application. For LabVIEW development, open the included project as described in the LabVIEW Project, Libraries, and Examples section of the Components of a PCB Asse

### Launching the Toolkit in TestStand

Use the included TestStand workspace to explore PCB Assembly Test
 Toolkit for LabVIEW example sequences that you can adapt for your
 own application.

Note

LabVIEW
 Project, Libraries, and Examples

PCB Assembly Test
 Toolkit for LabVIEW

1. In Windows Explorer, navigate to the following location: C:\Users\Public\Documents\National Instruments\PCB Assembly Test
 Toolkit for LabVIEW
2. Within the PCB Assembly Test Toolkit for LabVIEW directory,
 navigate to the TestStand directory.
3. Double-click PCBA TestStand Workspace.tsw to launch a
 workspace that includes the toolkit libraries and test templates. You can also
 copy the file path and open the workspace in TestStand.
4. In TestStand, navigate to PCBA TestStand Project\PCBA FT Demo\PCBA FT
 Demo.seq in the PCBA TestStand Workspace.
5. Double-click PCBA FT Demo.seq to open the sequence in
 TestStand. A dialog box appears that describes the requirements and purpose of
 the demo sequence. Click OK to close the dialog box.
6. Click Execute»Single Pass 
 to run the sequence in simulation mode.

Related tasks:

- Running Demo Test Sequences with Simulated Hardware
- Running the PCBA FT Demo Test Sequence

Related reference:

- Components of a PCB Assembly Test Toolkit for LabVIEW System

<!--NI_TOPIC bundle=pcb-assembly-test-toolkit-labview path=led-test-sequence.html language=enus -->
## TOPIC 00032: LED Test Sequence

- bundle_id: `pcb-assembly-test-toolkit-labview`
- source_path: `led-test-sequence.html`
- source_url: https://docs-be.ni.com/bundle/pcb-assembly-test-toolkit-labview/raw/resource/enus/led-test-sequence.html
- document_id: `pcb-assembly-test-toolkit-labview`
- page_type: `leaf`
- content_type: `reference`
- source_description: The LED Test sequence demonstrates measuring differential voltage across the anode and the cathode of the LED. The sequence also demonstrates the validation of a PWM signal with an analog buffer. The sequence simulates analog input and analog output channels or modules. This TestStand sequence uses

### LED Test Sequence

The LED Test sequence demonstrates measuring differential voltage across the
 anode and the cathode of the LED. The sequence also demonstrates the validation of a PWM
 signal with an analog buffer. The sequence simulates analog input and analog output
 channels or modules.

This TestStand sequence uses the LabVIEW measurement libraries. By default, the test
 sequence is installed to the following location: C:\Users\Public\Documents\National Instruments\PCB Assembly Test
 Toolkit for LabVIEW\TestStand\Automation\LED Tests

#### Required Driver Application Software

#### Highlighted Features

Validate DC Level

Send and Validate PWM (Analog Buffer)

- DAQ_Signal Voltage Generation
- DAQ_Time Domain Measurement

Turn Off all AO Channels

#### Hardware Configuration

[IMAGE alt='image' src='GUID-67C6AF8A-71A5-4D56-AD02-E7D738C3B86F-a5.png']

#### Using the Sequence with Physical
 Hardware

1. Run the sequence once in simulation mode. Running the sequence
 in simulation mode creates the required global virtual channels in NI MAX that
 you must modify. Note In this
 example, physical and global virtual channels are used to configure the
 terminal or pin to perform the instrument actions. Global virtual channels
 are software entities that encapsulate the physical channel along with other
 channel specific information such as range, terminal configuration, and
 custom scaling. You can create global channels in NI MAX and call them from
 measurement libraries.
2. Right click the Import Hardware Config step and select Run Mode»Skip to skip the step.
3. Configure the remaining sequences. Open each sequence and
 examine the Note to run with Hardware entry.
4. Configure the Validate DC Level Sequence sequence.
  1. Open NI-MAX and update the physical channel linked to the global virtual
 channels used in the DC-RMS Voltage Measurement initialize steps:
 TP_LED0 . Refer to Creating and
 Modifying Global Virtual Channels for more information.
  2. Review the power and analog input pin configurations for your use
 case.
  3. Save the sequence.
5. Configure the Send and Validate PWM(Analog Buffer) sequence.
  1. Open NI-MAX and update the physical channel linked to the global virtual
 channels used in the Signal Voltage Generation and Time Domain
 Measurement initialize steps: TS_PWM_LED0 and
 TP_PWM_LED0 . Refer to Creating and
 Modifying Global Virtual Channels for more information.
  2. Open the Time Domain Measurement - Configure capture settings
 for LED Measure step and update the Digital
 Trigger Source .
  3. Set Periodic waveform to
 True to perform time domain analysis in the
 measured data in the Time Domain Measurement - Fetch capture
 settings for LED Measure step.
  4. Review the power and analog input pin configurations for your use
 case.
  5. Save the sequence.
6. Configure the Turn Off all AO Channels 
 sequence.
  1. Open the DC Voltage Generation - Initialize AO
 Channels step and update the Physical
 Channels input to use your analog output channel.
  2. Review the analog output pin configurations for your use case.
  3. Save the sequence.

Parent topic:

Automation Test Sequences

Related tasks:

- Creating and Modifying Global Virtual Channels

<!--NI_TOPIC bundle=pcb-assembly-test-toolkit-labview path=library-list.html language=enus -->
## TOPIC 00033: PCB Assembly Test Toolkit for LabVIEW Measurement Libraries

- bundle_id: `pcb-assembly-test-toolkit-labview`
- source_path: `library-list.html`
- source_url: https://docs-be.ni.com/bundle/pcb-assembly-test-toolkit-labview/raw/resource/enus/library-list.html
- document_id: `pcb-assembly-test-toolkit-labview`
- page_type: `leaf`
- content_type: `reference`
- source_description: PCB Assembly Test Toolkit for LabVIEW provides measurement and generation libraries to enable common actions performed in PCB assembly electrical functional test. You can access PCB Assembly Test Toolkit for LabVIEW LabVIEW VIs from your PCBATT LabVIEW project. Refer to Launching the Toolkit in LabV

### Measurement Libraries

PCB Assembly Test
 Toolkit for LabVIEW provides measurement and
 generation libraries to enable common actions performed in PCB assembly electrical
 functional test. You can access PCB Assembly Test
 Toolkit for LabVIEW
 LabVIEW VIs from your PCBATT LabVIEW project. Refer to *Launching the Toolkit in
 LabVIEW* for details.

Note

Help

»

PCBA Measurement Library Help

- [DAQ_Power Supply Library](ps-source-measure-library.html) DAQ_Power Supply Library VIs initialize, configure, source, measure, and close user-configurable power supply pins. This library is applicable for the TestScale TS-15200 power supply module.
- [DAQ_DC Voltage Generation Library](dc-voltage-gen-library.html) DAQ_DC Voltage Generation Library VIs initialize, configure, generate, and close user-configurable analog output pins for DC voltage generation. This library is applicable for analog output channels and modules.
- [DAQ DC-RMS Voltage Measurement Library](dc-rms-voltage-measure-library.html) DAQ DC-RMS Voltage Measurement Library VIs initialize, configure, measure, and close user-configurable analog input pins. This library is applicable for analog input channels and modules.
- [DMM_DC-RMS Voltage Measurement Library](dmm-dc-rms-voltage-measure-library.html) DMM_DC-RMS Voltage Measurement Library VIs initialize, configure, measure and close a DC voltage or AC RMS voltage measurement on a NI-DMM instrument.
- [DAQ_DC-RMS Current Measurement Library](dc-rms-current-measure-library.html) DAQ_DC-RMS Current Measurement library VIs initialize, configure, measure, and close user-configurable analog input pins for current measurements. This library is applicable for analog input channels and modules.
- [DMM_DC-RMS Current Measurement Library](dmm-dc-rms-current-measure-library.html) DMM_DC-RMS Current Measurement Library VIs initialize, configure, measure and and close a DC Current or AC RMS Current measurement on an NI-DMM instrument.
- [DAQ_Signal Voltage Generation Library](sig-voltage-gen-library.html) DAQ_Signal Voltage Generation Library VIs provides options to generate various waveform voltage signal tones (single/multi) over one or more given generation times on analog output terminals of DAQmx. This library is applicable for analog output channels and modules.
- [DAQ_Time Domain Measurement Library](time-measure-library.html) DAQ_Time Domain Measurement Library VIs initialize, configure, measure, and close user-configurable analog input pins and derive time domain measurements for the measured waveforms. This library is applicable for analog input channels and modules.
- [DAQ_Frequency Domain Measurement Library](freq-measure-library.html) DAQ_Frequency Domain Measurement Library VIs initialize, configure, measure, and close user-configurable analog input pins and derive frequency domain measurements for the measured waveforms. This library is applicable for analog input channels and modules.
- [DMM_Frequency Domain Measurement Library](dmm-freq-measure-library.html) DMM_Frequency Domain Measurement Library VIs initialize, configure, measure and close user-configurable analog input pins and derive frequency domain measurements for the measured waveforms.
- [DAQ_Static Digital State Measurement Library](static-digital-state-measure.html) DAQ_Static Digital State Measurement Library VIs measure the static digital data on all configured digital channel lines in the DAQmx task. This library is applicable for digital input channels and modules.
- [DAQ_Static Digital State Generation Library](static-digital-state-gen.html) DAQ_Static Digital State Generation Library VIs generate static digital data on all configured digital channel lines in the DAQmx task. This library is applicable for digital output channels and modules.
- [DAQ_Dynamic Digital Pattern Measurement Library](dynamic-digital-pattern-measure.html) DAQ_Dynamic Digital Pattern Measurement Library VIs enable dynamic digital measurements on one or more digital channel lines or on an entire port in a digital module. This library is applicable for TestScale digital input modules or channels that support hardware-timed digital waveform characteristics.
- [DAQ_Dynamic Digital Pattern Generation Library](dynamic-digital-pattern-gen.html) DAQ_Dynamic Digital Pattern Generation Library VIs initialize, configure, generate, and close user-configurable digital output pins. This library is applicable for digital output modules and channels that support hardware-timed digital waveform characteristics.
- [DAQ_Digital Clock Generation Library](digital-clock-gen.html) DAQ_Digital Clock Generation Library VIs initialize, configure, generate, and close user-configurable terminals using counters. This library is applicable for digital I/O channels and modules that support timing output signals with PFI channels or other connections.
- [DAQ_Digital Pulse Generation Library](digital-pulse-gen.html) DAQ_Digital Pulse Generation Library VIs initialize, configure, generate, and close user-configurable terminals using counters. This library is applicable for digital I/O channels and modules that support timing output signals with PFI channels or other connections.
- [DAQ_Digital Frequency Measurement Library](digital-frequency-measure.html) DAQ_Digital Frequency Measurement Library VIs initialize, configure, measure, and close user-configurable PFI lines using selected counter for digital frequency measurement. This library is applicable for digital I/O channels and modules that support timing input signals with PFI channels or other connections.
- [DAQ_Digital PWM Measurement Library](digital-pwm-measure.html) DAQ_Digital PWM Measurement Library VIs initialize, configure, measure, and close counter input tasks with an assigned input terminal. This library is applicable for digital I/O channels and modules that support timing input signals with PFI channels or other connections.
- [DAQ_Digital Edge Count Measurement Library](digital-edge-count-measure.html) DAQ_Digital Edge Count Measurement Library VIs initialize, configure, measure, and close user-configurable PFI lines using selected counters for digital events or edge counting. This library is applicable for digital I/O channels and modules that support timing input signals with PFI channels or other connections.
- [Communication APIs Library](comm-apis.html) The Communication APIs Library contains simple read and write VIs for I 2 C, SPI, and serial communication modes. This library is applicable for the USB-8452, USB-232, and corresponding driver application software.
- [DAQ_Synchronization Library](sync-library.html) DAQ_Synchronization Library VIs route signals between specified source signals and output terminals for the given DAQmx Task.
- [DMM_Resistance Measurement Library (2-Wire and 4-Wire)](dmm-resistance-measure-library.html) DMM_Resistance Measurement Library VIs initialize, configure, and close 2-Wire and 4-Wire resistance measurements.
- [DAQ_Temperature RTD Measurement Library](temperature-rtd-measure.html) DAQ_Temperature RTD Measurement Library VIs initialize, configure, measure, and close user configurable analog input pins to derive temperature measurements from resistance temperature detectors (RTDs). This library is applicable for C Series temperature input modules.
- [DAQ_Temperature Thermistor Measurement Library](thermistor-measure.html) DAQ_Temperature Thermistor Measurement Library VIs initialize, configure, measure, and close user-configurable analog input pins to derive temperature measurements from voltage excited NTC-typed thermistor devices. This library is applicable for NI-63xx (X Series) analog input channels, TestScale analog input modules, and C Series voltage input modules.
- [DAQ_Temperature Thermocouple Measurement Library](thermocouple-measure.html) DAQ_Temperature Thermocouple Measurement Library VIs initialize, configure, measure, and close user configurable analog input pins to derive temperature measurements from thermocouples. This library is applicable for C Series temperature input modules.
- [DMM_Mixed Measurement Library (for DMM Scan)](dmm-mixed-measure-library.html) DMM Mixed Measurement Library VIs can be used to initialize, configure, measure, and close the following measurement types on a NI-DMM instrument: DC and AC voltage, DC and AC current, resistance (2-wire only), frequency, or period.
- [DMM_Scan Libraries](dmm-scan-libraries.html) The PCB Assembly Test Toolkit for LabVIEW includes three DMM Scan libraries to support a broad range of hardware configurations.

Related reference:

- Launching the Toolkit in LabVIEW

<!--NI_TOPIC bundle=pcb-assembly-test-toolkit-labview path=mic-test-sequence.html language=enus -->
## TOPIC 00034: Microphone Test Sequence

- bundle_id: `pcb-assembly-test-toolkit-labview`
- source_path: `mic-test-sequence.html`
- source_url: https://docs-be.ni.com/bundle/pcb-assembly-test-toolkit-labview/raw/resource/enus/mic-test-sequence.html
- document_id: `pcb-assembly-test-toolkit-labview`
- page_type: `leaf`
- content_type: `reference`
- source_description: The Microphone Test sequence uses analog output channels or modules and analog input channels or modules to demonstrate frequency domain measurements of a captured audio signal. This TestStand sequence uses the LabVIEW measurement libraries. By default, the test sequence is installed to the followin

### Microphone Test Sequence

The Microphone Test sequence uses analog output channels or modules and analog
 input channels or modules to demonstrate frequency domain measurements of a captured
 audio signal.

This TestStand sequence uses the LabVIEW measurement libraries. By default, the test
 sequence is installed to the following location: C:\Users\Public\Documents\National Instruments\PCB Assembly Test
 Toolkit for LabVIEW\TestStand\Automation\Microphone Tests

#### Required Driver Application Software

#### Highlighted Features

Microphone Test (with Trigger)

- DAQ_DC Signal Voltage Generation
- DAQ_Frequency Domain Measurement

Turn Off all AO Channels

#### Hardware Configuration

[IMAGE alt='image' src='GUID-E2949E56-3472-47B5-B46B-900897950637-a5.png']

#### Using the Sequence with Physical
 Hardware

1. Run the sequence once in simulation mode. Running the sequence
 in simulation mode creates the required global virtual channels in NI MAX that
 you must modify. Note In this
 example, physical and global virtual channels are used to configure the
 terminal or pin to perform the instrument actions. Global virtual channels
 are software entities that encapsulate the physical channel along with other
 channel specific information such as range, terminal configuration, and
 custom scaling. You can create global channels in NI MAX and call them from
 measurement libraries.
2. Right click the Import Hardware Config step and select Run Mode»Skip to skip the step.
3. Configure the remaining sequences. Open each sequence and
 examine the Note to run with Hardware entry.
4. Configure the Microphone Test (with Trigger) sequence.
  1. Open NI-MAX and update the physical channel linked to the global virtual
 channels used in the Signal Voltage Generation and Frequency Domain
 Measurement initialize steps: TS_Speaker0 ,
 TP_Mic0 , TP_Mic1 , and
 TP_Mic2 . Refer to Creating and
 Modifying Global Virtual Channels for more information.
  2. Open the Frequency Domain Measurement – Configure
 TP step and update the Digital Trigger
 Source .
  3. Review the analog output and analog input pin configurations for your
 use case.
  4. Save the sequence.
5. Configure the Turn Off all AO Channels 
 sequence.
  1. Open the DC Voltage Generation - Initialize AO
 Channels step and update the Physical
 Channels input to use your analog output channel.
  2. Review the analog output pin configurations for your use case.
  3. Save the sequence.

Parent topic:

Automation Test Sequences

Related tasks:

- Creating and Modifying Global Virtual Channels

<!--NI_TOPIC bundle=pcb-assembly-test-toolkit-labview path=new-features-and-changes.html language=enus -->
## TOPIC 00035: PCB Assembly Test Toolkit for LabVIEW New Features and Changes

- bundle_id: `pcb-assembly-test-toolkit-labview`
- source_path: `new-features-and-changes.html`
- source_url: https://docs-be.ni.com/bundle/pcb-assembly-test-toolkit-labview/raw/resource/enus/new-features-and-changes.html
- document_id: `pcb-assembly-test-toolkit-labview`
- page_type: `leaf`
- content_type: `concept`
- source_description: Learn about updates, including new features and behavior changes, introduced in each version of PCB Assembly Test Toolkit for LabVIEW. Discover what is new in the latest releases of PCB Assembly Test Toolkit for LabVIEW.If you cannot find new features and changes for your version, it might not inclu

### PCB Assembly Test
 Toolkit for LabVIEW
 New Features and Changes

Learn about updates, including new features and behavior changes, introduced in each
 version of PCB Assembly Test
 Toolkit for LabVIEW.

PCB Assembly Test
 Toolkit for LabVIEW

Note

#### PCB Assembly Test Toolkit 2025 Q2 for
 LabVIEW Changes

Learn about new features, behavior changes, and other updates in PCB Assembly Test
 Toolkit 2025 Q2 for LabVIEW.

##### New Features

This version of the PCB Assembly Test
 Toolkit for LabVIEW provides support for the
 following features:

- Updated DAQ functions to support PCIe, PXIe, and USB devices, emphasizing support for NI
 63xx (X Series) devices. Updated icons colors and library names (existing libraries now
 have a DAQ_ prefix) to distinguish new hardware and mixed signal support.
- Added new individual simple DMM functions to measure AC/DC voltage and current,
 frequency and period, and 2-wire or 4-wire resistance. A new DMM mixed measurement library
 integrates all measurements while using the same Initialize, Configure and Measure, and
 Close function pattern used in other PCB Assembly Test Toolkit libraries.
- Added new simple switch function to support NI multiplexers and all topologies using a
 path method to connect and disconnect internal relays (for example,
 ch1 , com0 ).
- Added new simple functions to support DMM Scan using three different hardware methods.
 Supported hardware methods correspond to the following NI bundles: PXI DMM Switches, PXI
 DMM with Switch Relay Driver and External Relays, and PXI DAQ DO with Custom External
 Relays).
- Added a new list of examples for DAQ, DMM, DMM Scan methods in LabVIEW.
- Updated TestStand automation sequences using PC-based devices, such as NI 63xx (X
 Series) devices.

<!--NI_TOPIC bundle=pcb-assembly-test-toolkit-labview path=numeric-limit-test.html language=enus -->
## TOPIC 00036: Creating a Multiple Numeric Limit Test in TestStand

- bundle_id: `pcb-assembly-test-toolkit-labview`
- source_path: `numeric-limit-test.html`
- source_url: https://docs-be.ni.com/bundle/pcb-assembly-test-toolkit-labview/raw/resource/enus/numeric-limit-test.html
- document_id: `pcb-assembly-test-toolkit-labview`
- page_type: `leaf`
- content_type: `task`
- source_description: Use the Tests step type to perform limit checks the measured data. Complete the following steps to add a multiple numeric limit test to your sequence. Open or create a PCB Assembly Test sequence in TestStand. In the list of steps, expand the Tests folder. Add the Multiple Numeric Limit Test step to

### Creating a Multiple Numeric Limit Test in
 TestStand

Use the Tests step type to perform limit checks the measured data.
 Complete the following steps to add a multiple numeric limit test to your sequence.

1. Open or create a PCB Assembly Test sequence in TestStand.
2. In the list of steps, expand the Tests folder. [IMAGE alt='image' src='GUID-CF002080-06BF-4E7A-854C-4DE3F4E40948-a5.png']
3. Add the Multiple Numeric Limit Test step to your
 sequence.
4. Click the Module tab in the step settings.
5. Select the VI path. The VI loads.
6. Reference the data types returned by the VI to create the TestStand variables
 that represent your measurement data.
  - For simple data types (for example, number, string, boolean or array),
 create named TestStand variables with the corresponding type.
  - For container data types, click the Create/Update Custom Data
 Type 
 button to create
 a custom data type. You can then create a TestStand variable using this
 custom data type. [IMAGE alt='image' src='GUID-4131589B-38EC-4C11-8E9B-FDC8EC93772A-a5.png']
7. Assign each VI return value to the corresponding TestStand variable.
8. Click the Limits tab in the step settings. Use this tab
 to define limits. [IMAGE alt='image' src='GUID-C6525AA8-7615-43EF-A500-48B84AB0D97C-a5.png'] Add additional limits as necessary.
  1. Specify a Measurement Name for each limit.
  2. Select the desired Comparison Type .
  3. Update the Low and High 
 limits.
9. Click the Data Source tab in the step settings. Set the
 desired TestStand variable as the Data Source to evaluate
 for each limit check.
10. Return to the Module tab and declare any other required
 output variables.

Tip

Functional Demo Sequences

Parent topic:

Using the PCB Assembly Test Toolkit for LabVIEW

<!--NI_TOPIC bundle=pcb-assembly-test-toolkit-labview path=overview.html language=enus -->
## TOPIC 00037: PCB Assembly Test Toolkit for LabVIEW Overview

- bundle_id: `pcb-assembly-test-toolkit-labview`
- source_path: `overview.html`
- source_url: https://docs-be.ni.com/bundle/pcb-assembly-test-toolkit-labview/raw/resource/enus/overview.html
- document_id: `pcb-assembly-test-toolkit-labview`
- page_type: `leaf`
- content_type: `concept`
- source_description: The PCB Assembly Test Toolkit for LabVIEW includes a measurement library, automation examples, a test demo example, and documentation for electrical functional testing of PCB assemblies. The PCB Assembly Test Toolkit for LabVIEW provides library examples and automation-ready TestStand sequence templ

### PCB Assembly Test
 Toolkit for LabVIEW
 Overview

The PCB Assembly Test
 Toolkit for LabVIEW includes a measurement library,
 automation examples, a test demo example, and documentation for electrical functional
 testing of PCB assemblies.

The PCB Assembly Test
 Toolkit for LabVIEW provides library examples and
 automation-ready TestStand sequence templates that you can use for production testing of
 printed-circuit board assembly (PCBA) with data acquisition systems, DMM and switch
 instruments, CompactDAQ hardware, TestScale devices, or any device supported by
 NI-DAQmx. The add-on includes example measurements for DC/RMS voltage, idle power,
 frequency, digital counting, DMM scanning with different hardware configurations, and
 more. Additionally, the PCB Assembly Test Toolkit provides example tests for interface
 buttons and LED, power diagnostics, and more.

<!--NI_TOPIC bundle=pcb-assembly-test-toolkit-labview path=pcb-assembly-functional-test-run.html language=enus -->
## TOPIC 00038: Running the PCBA FT Demo Test Sequence

- bundle_id: `pcb-assembly-test-toolkit-labview`
- source_path: `pcb-assembly-functional-test-run.html`
- source_url: https://docs-be.ni.com/bundle/pcb-assembly-test-toolkit-labview/raw/resource/enus/pcb-assembly-functional-test-run.html
- document_id: `pcb-assembly-test-toolkit-labview`
- page_type: `leaf`
- content_type: `task`
- source_description: Locate the Steps:MainSequence pane. Review the steps in the Setup step group. Review the steps and instrument configurations in the Main step group. The Power Diagnostics step demonstrates the Power Supply Source and DC-RMS Voltage Measurements without triggers. The test performs the following steps

### Running the PCBA FT Demo Test Sequence

1. Locate the Steps:MainSequence pane. Review the steps in the Setup step
 group.
2. Review the steps and instrument configurations in the Main step group.
  - The Power Diagnostics step demonstrates the Power Supply Source and
 DC-RMS Voltage Measurements without triggers. The test performs the
 following steps:
    1. Initializes the Power Supply and DC-RMS Voltage Measurement
 libraries.
    2. Configures the power supply source and begins sourcing. Supply
 voltage is sourced in the output even after closing the task.
 Here the example supplies 5 V with a 3 A current setpoint.
    3. Measures the start-up transition maximum current, idle power
 consumption from the power source.
    4. Measures the DC voltages on DC regulators with the DC-RMS
 Voltage Measurement library. To validate the measurement, thet
 test compares the limits with the expected nominal values of the
 regulators (1 V, 3.3 V, and 5 V, with tolerance).
  - The battery or charger voltage and current sleep mode step demonstrates
 the DMM_Scan PXI Mux PXI Shunt 16V-15C function. The test performs the
 following steps:
    1. Initializes the DMM_Scan PXI Mux PXI Shunt 16V-15C library.
    2. Configures the scan channels of the PMPS topology (voltages ch0,
 ch1 and current ch16, ch17) for the active mode of the PCBA
 charger. All shunt switches are closed to keep the continuity of
 the full circuit.
    3. Measures the voltages and current from the input charger and
 output to the lithium-ion battery. Checks the limits of the
 battery range and charger (2.5V to 4.25 V and 0 to 500 mA for
 the battery and 4.75 V to 5.25 V and 0 to 500 mA for the charger
 input).
    4. Waits for the PCBA to enter sleep mode after 2 seconds of
 inactivity.
    5. Configures the scan channels (ch1, ch17) for the battery voltage
 and current output in sleep mode. Note For microampere
 accuracy, change the configuration to specify a current
 range of 100 µA and set digits to
 6 1/2.
    6. Measures the voltages and current from the output lithium-ion
 battery and checks the following limits:
      - Voltage: 2.5 V to 4.25 V
      - Current: 5 µA to 15 µA
  - The Reset and Self-Test step demonstrates DC-RMS voltage measurements by
 performing button actions to generate DC states on specific test points.
 The test performs the following steps:
    1. Initializes the Static Digital State Generation and DC-RMS
 Voltage Measurement libraries.
    2. Configures static digital state generation to generate digital
 HIGH/LOW states that perform action button reset ON/OFF
 conditions. In this example, the digital HIGH state is set for
 0.1 seconds by the wait function followed by the Digital LOW
 state and a 5 second wait for the UUT to reboot.
    3. Measures DC-RMS voltage measurement on the Power and Status LEDs
 for the expected button action states. In this example, the ON
 state of the Power and Status LED are validated with DC-RMS
 Voltage measurements. The expected limit values, with tolerance,
 are 2 V for the red LED and 2.9 V for the green LED.
  - The Animation and Sound User Input Test demonstrates time domain
 measurements by generating DC Voltages to perform button actions on
 specific test points with Hardware Trigger. The test performs the
 following steps: Note Running this example in simulation mode produces non-periodic
 waveforms. Perform the remaining steps to ignore errors in
 simulation mode.
    1. Initializes the DC Voltage Generation and Time Domain
 Measurement libraries.
    2. Configures DC voltage generation to generate DC voltage and
 perform action button OFF/ON conditions. In this example,
 setting the test point to 3.3 V, representing the ON state, and
 0 V, representing the OFF state.
    3. Measures time domain measurements on the Animation Action LED
 and the Tone Action sound check line for the expected Button
 action states. This time domain measurement is only valid for
 periodic waveform signals and will produce errors for other
 signals. The expected limits, with tolerance, are 30% of duty
 cycle and a 1 kHz sine wave tone.
  - The Audio Filter Test demonstrates frequency domain measurements of a
 captured multi-tone analog signal representing audio. The analog signal
 is generated by an analog output module with a hardware trigger. The
 test performs the following steps:
    1. Initializes the Signal Voltage Generation and Frequency Domain
 Measurement libraries.
    2. Configures frequency domain measurement to wait for a signal
 voltage generation start trigger.
    3. Configures signal voltage generation to start sourcing the sine
 wave with multiple tones. The example generates a multi-tone
 sine wave of 10 Hz, 100 Hz, 1 kHz, and 10 kHz with an amplitude
 of 1 V. The signal voltage generation module sends the trigger
 through the backplane when sourcing starts, triggering the
 measurement start with the analog input module.
    4. Fetches the measured voltage waveformsand returns the detected
 frequency and amplitude of each tone.
    5. Validates the frequency and amplitudes limits are within ±10% of
 the nominal value.
  - Turn Off all AO Channels disables power for all analog ouput channels by
 configuring them to 0 V. The step performs the following actions:
    1. Initializes the DC Voltage Generation library.
    2. Configures DC voltage generation to source 0 V for the specified
 analog ouput channels.
    3. Closes the DAQmx task.
  - Power Down Supply disables power supply output. The step performs the
 following actions:
    1. Initializes the Power Supply Source and Measure library.
    2. Configures the voltage setpoint to source 0 V and configures the
 output status to Disable Output when Task
 stopped for the specified power channels.
    3. Closes the DAQmx task.
3. In simulation mode, configure the Animation and Sound User Input
 Test to run without errors:
  1. Open the Animation and Sound User Input Test 
 sequence.
  2. Click the Time Domain Measurement - Fetch Volume LED Dutycycle
 and Tweeter Frequency step. On the step settings tab,
 select Properties»Run Options .
  3. On the Run Options tab, enable the Ignore Run-Time
 Errors checkbox to ignore all run-time errors for this
 step. [IMAGE alt='image' src='GUID-DB813B8A-8E6A-4E66-B203-E5B8CC726F3A-a5.png']
  4. Save the sequence.
4. Select Execute»Single Pass to run the sequence.
5. When the execution completes, review the report on the report pane. Verify the
 measurement and the data formats returned by the measurement libraries.
  - The report includes the configurations and measurement values captured
 from the simulation.
  - The report indicates a Failed status because the simulated measurements
 do not satisfy the limit checks.
6. Select Execute»Restart to run the sequence again.

Parent topic:

PCBA Functional Test Demo Test Sequence

<!--NI_TOPIC bundle=pcb-assembly-test-toolkit-labview path=pcb-assembly-functional-test-seq.html language=enus -->
## TOPIC 00039: PCBA Functional Test Demo Test Sequence

- bundle_id: `pcb-assembly-test-toolkit-labview`
- source_path: `pcb-assembly-functional-test-seq.html`
- source_url: https://docs-be.ni.com/bundle/pcb-assembly-test-toolkit-labview/raw/resource/enus/pcb-assembly-functional-test-seq.html
- document_id: `pcb-assembly-test-toolkit-labview`
- page_type: `leaf`
- content_type: `reference`
- source_description: The PCBA FT Demo test sequence demonstrates testing PCBA DUTs in TestStand using the PCB Assembly Test Toolkit measurement libraries built in LabVIEW. Refer to the individual library documentation for more information about how to use each library in your own application. Highlighted FeaturesThe PCB

### PCBA Functional Test Demo Test
 Sequence

The PCBA FT Demo test sequence demonstrates testing PCBA DUTs in TestStand
 using the PCB Assembly Test Toolkit measurement libraries built in LabVIEW.
 Refer to the individual library documentation for more information about how to use each
 library in your own application.

#### Highlighted Features

Power Diagnostics

- DAQ_Power Supply Source and Measure
- DAQ_DC-RMS Voltage Measurement

Battery or charger voltage and current sleep mode

Reset and Self-Test

- DAQ_Static Digital State Generation
- DAQ_DC-RMS Voltage Measurement

Animation and Sound User Input Test

- DAQ_DC Voltage Generation
- DAQ_Time Domain Measurement

Audio Filter Test

- DAQ_Signal Voltage Generation
- DAQ_Frequency Domain Measurement

Turn Off All AO Channels

Power Down Supply

#### Setup Diagram

The following figures represent the simulated hardware setup used in this example
 sequence. Refer to individual device specifications for pinouts and relevant
 specifications.

Figure 2.

[IMAGE alt='image' src='GUID-82098016-F659-46DC-838E-DEDF2B2EA639-a5.png']

Figure 3.

[IMAGE alt='image' src='GUID-7EA0244F-0EE0-484E-8DDF-21821CF35521-a5.png']

Figure 4.

[IMAGE alt='image' src='GUID-33D553EE-5F3C-4B23-B382-048E8DB801DD-a5.png']

Figure 5.

[IMAGE alt='image' src='GUID-EF814CA5-7F57-494A-9CA7-2385EE42CDA0-a5.png']

Figure 6.

[IMAGE alt='image' src='GUID-DB3C60E2-EF77-4A46-BECE-CC45D36208E3-a5.png']

The following table provides a detailed summary of the functional demo sequence test
 scenario.

| PCBA Functional Test Demo | LSL | USL | Units | Timing (s) | Test Points | V Mode | Analysis Value | Trigger | Procedure/Condition | Measurement Library |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Power Diagnostics |  |  |  |  |  |  |  |  |  |  |
| To power up and measure start-up transition max pic current, idle power consumption, and DC regulators. |  |  |  |  |  |  |  |  |  |  |
| Start-up transition max pic current | 0 | 1 | A | 0.1 | TP_POWER0 | Ref | Max Current | Maintain existing value | Set Power On Voltage to 5 V, 3 A, Maintain Existing Value, Measure TP_Max Current (Pic Transition) | Power supply source and measure |
| Idle power consumption | 4.5 | 5.5 | W | 0.1 | TP_POWER0 | Ref | Idle Watt | Maintain existing value | Measure idle watt, Power voltage already On | Power supply source and measure |
| DC Regulators | 0.9 | 1.1 | V | 0.1 | TP_REG0 | Ref | Average DC Voltage | No | Measure regulator voltage around 1 V | DC-RMS voltage measurement |
| - | 3.1 | 3.4 | V | - | TP_REG1 | Ref | Average DC Voltage | No | Measure regulator voltage around 3.3 V | - |
| - | 4.8 | 5.2 | V | - | TP_REG2 | Ref | Average DC Voltage | No | Measure regulator voltage around 5 V | - |
| Battery or charger voltage and current sleep mode |  |  |  |  |  |  |  |  |  |  |
| USB Voltage | 4.75 | 5.25 | V | DMM 5.5 Dig | ch0 | Diff | DMM | No | Close all Current Shunts to Power the DUT, Scan ch0 | DMM Scan PXI MUX SHUNT Topology |
| Li-ion Battery Voltage | 2.5 | 4.25 | V | DMM 5.5 Dig | ch1 | Diff | DMM | No | Scan ch1, SOC dependent | - |
| USB Current | 0 | 500 | mA | DMM 5.5 Dig | ch16 | Diff | DMM | No | Scan ch16, SOC dependent | - |
| Li-ion Battery Current | 0 | 500 | mA | DMM 5.5 Dig | ch17 | Diff | DMM | No | Scan ch17, SOC dependent | - |
| Battery Voltage Sleep Mode | 2.5 | 4.25 | V | DMM 5.5 Dig | ch1 | Diff | DMM | No | Wait inactivity for 2 sec, Scan ch1 | New Scan |
| Battery Current Sleep Mode | 5 | 15 | µA | DMM 6.5 Dig | ch17 | Diff | DMM | No | Scan ch17 | - |
| Reset and self-test |  |  |  |  |  |  |  |  |  |  |
| To simulate Push Reset Button On/Off condition for 0.1 sec followed by a 5 sec wait for reboot to check voltage values on power and status LEDs. |  |  |  |  |  |  |  |  |  |  |
| Push button reset |  |  | V | Wait for 0.1 sec followed by a 5 sec wait for reboot | TP_RESET0 | Ref |  |  | Switch ON 0.1 sec then switch OFF with digital output (DO Module switch), Wait Reboot for 5 sec | Static digital state generation |
| Power LED0 RED | 1.8 | 2.2 | V | 0.1 | TP_LED0 | Diff | Average DC Voltage | No | Measure value for state (LED Power) | DC-RMS voltage measurement |
| Status LED1 GREEN | 2.6 | 3.2 | V | - | TP_LED1 | Diff | Average DC Voltage | No | Measure value for state (LED Status) | - |
| Animation and sound user input test |  |  |  |  |  |  |  |  |  |  |
| To simulate the push on a volume button to generate a sound and a light animation to the LED. |  |  |  |  |  |  |  |  |  |  |
| Push action button |  |  |  | 0.5 | TS_Button0 | Ref |  | No | Generate DC 3.3 V to simulate Button On | DC voltage generation |
| Animation action LED | 25% | 35% | Duty cycle | 0.5 | TP_VOL_LED0 | Ref | TDM Voltage Duty Cycle | Trigger on button | Measure PWM square signal On Volume LED | Time domain measurement |
| Tone action sound check | 990 | 1010 | Hz | 0.5 | TP_TWEET0 | Ref | TDM Voltage Frequency | - | Measure 1 kHz frequency on Tweeter | - |
| Audio filter test |  |  |  |  |  |  |  |  |  |  |
| To test if measured tones frequency are within ±10% of tolerance |  |  |  |  |  |  |  |  |  |  |
| Send multi-tone audio |  |  |  | 0.1 | TP_LineIn | Ref |  |  | Send 4 tones: 10 Hz, 100 Hz, 1 kHz, 10 kHz, 1 V sine signal | Signal voltage generation |
| Measure tone | -10% | +10% | Hz | 0.1 | TP_LineOut | Ref | Detected Tones Frequencies (0, 1, 2, 3) | Trigger from signal generation | Measure 4 tones: 10 Hz, 100 Hz, 1 kHz, 10 kHz | Frequency domain measurement |
| - | -10% | +10% | V | 0.1 | - | Ref | Detected Tones Amplitudes (0, 1, 2, 3) | - | Measure 4 voltage amplitudes | - |

<!--NI_TOPIC bundle=pcb-assembly-test-toolkit-labview path=pcb-assembly-test-toolkit-enable-hw.html language=enus -->
## TOPIC 00040: Enabling Physical Hardware for PCB Assembly Test Toolkit for LabVIEW Steps

- bundle_id: `pcb-assembly-test-toolkit-labview`
- source_path: `pcb-assembly-test-toolkit-enable-hw.html`
- source_url: https://docs-be.ni.com/bundle/pcb-assembly-test-toolkit-labview/raw/resource/enus/pcb-assembly-test-toolkit-enable-hw.html
- document_id: `pcb-assembly-test-toolkit-labview`
- page_type: `leaf`
- content_type: `task`
- source_description: The PCBA FT Demo Test sequence uses simulated hardware by default. Complete the following steps to modify the sequence to use physical hardware. Run the sequence once in simulation mode. Running the sequence in simulation mode creates the required global virtual channels in NI MAX that you must modi

### Enabling Physical Hardware

The PCBA FT Demo Test sequence uses simulated hardware by default. Complete the following
 steps to modify the sequence to use physical hardware.

1. Run the sequence once in simulation mode. Running the sequence
 in simulation mode creates the required global virtual channels in NI MAX that
 you must modify. Note In this
 example, physical and global virtual channels are used to configure the
 terminal or pin to perform the instrument actions. Global virtual channels
 are software entities that encapsulate the physical channel along with other
 channel specific information such as range, terminal configuration, and
 custom scaling. You can create global channels in NI MAX and call them from
 measurement libraries.
2. In the Main sequence, locate the Import Hardware Config
 step.
3. Right click the Import Hardware Config step and select Run Mode»Skip to skip the step. [IMAGE alt='image' src='GUID-5C866446-C501-4656-BEB5-036581B9F9D1-a5.png']
4. Configure the remaining sequences. Open each sequence and
 examine the Note to run with Hardware entry.
5. Configure the Power Diagnostics sequence:
  1. Step into the Power Diagnostics sequence and open the Power
 Supply Source and Measure - Initialize Power Supply step.
  2. Update the Physical Channels input with the
 Power Module Channel in the initialize step
 of Power Supply Source and Measure.
  3. Open NI-MAX and update the physical channel linked to the global virtual
 channels used in the DC-RMS Voltage Measurement initialize step:
 TP_REG0 , TP_REG1 ,
 TP_REG2 . Refer to Creating and
 Modifying Global Virtual Channels for more information.
  4. Review the power and analog input pin configurations for your use
 case.
  5. Save the sequence.
6. Configure the Reset and Self-Test sequence:
  1. Open NI-MAX and update the physical channel linked to the global virtual
 channels used in the Static Digital State Generation and DC-RMS Voltage
 Measurement initialize steps: TS_RESET0 ,
 TP_LED0 , and TP_LED1 .
 Refer to Creating and Modifying Global Virtual Channels for
 more information.
  2. Select the Static Digital State Generation - Turn ON Push
 Reset Button and Static Digital State
 Generation - Turn OFF Push Reset Button steps and update
 the generated static digital states based on Action Button ON and OFF
 conditions. In the example, the Action Button ON condition is achieved
 by setting digital HIGH to TS_RESET0 and the Action Button OFF condition
 is achieved by setting digital LOW to TS_RESET0. Review and modify the
 digital states based on your use case.
  3. Review the analog output and analog input pin configurations for your
 use case.
  4. Save the sequence.
7. Configure the Animation and Sound User Input Test sequence:
  1. Open NI-MAX and update the physical channel linked to the global virtual
 channels used in the DC Voltage Generation and Time Domain Measurement
 initialize steps: TS_Button0 ,
 TP_VOL_LED0 , and
 TP_TWEET0 . Refer to Creating and
 Modifying Global Virtual Channels for more information.
  2. Select the DC Voltage Generation - Action
 Button ON State and DC Voltage Generation -
 Action Button OFF State steps and update the generated
 static digital states based on Action Button ON and OFF conditions. In
 the example, the Action Button ON condition is achieved by supplying 3.3
 V to TS_BUTTON0 and the Action Button OFF condition is achieved by
 supplying 0 V to TS_BUTTON0. Review and modify the digital states based
 on your use case. Note The maximum current drive per channel is specific to each device.
 For the PXIe-6363, the maximum current drive per channel is ±5 mA.
 For the TS-15110 analog output module, the maximum current drive per
 channel is ±1 mA. If you are using another device, consult the
 applicable device specifications. Consider the specified limit when
 configuring button states.
  3. Select the Time Domain Measurement - Fetch Volume LED
 Dutycycle and Tweeter Frequency step.
  4. Select the Properties tab in the Step Settings and click Run
 Options .
  5. Verify that the Ignore Run-Time Errors checkbox
 is disabled. The sequence requires a periodic waveform signal. The Time
 Domain Measurements produce run-time errors for other waveform signals,
 but these errors can be ignored when running the sequence with simulated
 hardware.
  6. Review the analog output and analog input pin configurations for your
 use case.
  7. Save the sequence.
8. Configure the Audio Filter Test sequence.
  1. Open NI-MAX and update the physical channel linked to the global virtual
 channels used in the Signal Voltage Generation and Frequency Domain
 Measurement initialize steps: TS_LineIn and
 TP_LineOut . Refer to Creating and
 Modifying Global Virtual Channels for more information.
  2. Open the Frequency Domain Measurement – Configure
 TP step and update the Digital Trigger
 Source .
  3. Review the analog output and analog input pin configurations for your
 use case.
  4. Save the sequence.
9. Configure the Turn Off all AO Channels 
 sequence.
  1. Open the DC Voltage Generation - Initialize AO
 Channels step and update the Physical
 Channels input to use your analog output channel.
  2. Review the analog output pin configurations for your use case.
  3. Save the sequence.
10. Configure the Power Down Supply 
 sequence.
  1. Open the Power Supply Source and Measure -
 Initialize step and update the Physical
 Channels input to use your power module channel.
  2. Review the power configurations for your use case.
  3. Save the sequence.

Parent topic:

PCBA Functional Test Demo Test Sequence

Related tasks:

- Creating and Modifying Global Virtual Channels

<!--NI_TOPIC bundle=pcb-assembly-test-toolkit-labview path=pcba-global-virtual-channels.html language=enus -->
## TOPIC 00041: Creating and Modifying Global Virtual Channels

- bundle_id: `pcb-assembly-test-toolkit-labview`
- source_path: `pcba-global-virtual-channels.html`
- source_url: https://docs-be.ni.com/bundle/pcb-assembly-test-toolkit-labview/raw/resource/enus/pcba-global-virtual-channels.html
- document_id: `pcb-assembly-test-toolkit-labview`
- page_type: `leaf`
- content_type: `task`
- source_description: A virtual channel is a collection of settings such as a name, a physical channel, input terminal connections, the type of measurement or generation, and scaling information. A virtual channel that is created outside a task is a global virtual channel. Refer to Creating a Virtual Channel in NI-DAQmx

### Creating and Modifying Global Virtual
 Channels

A virtual channel is a collection of settings such as a name, a physical
 channel, input terminal connections, the type of measurement or generation, and scaling
 information. A virtual channel that is created outside a task is a global virtual
 channel. Refer to *Creating a Virtual Channel in NI-DAQmx and Using it
 in LabVIEW* for detailed definitions and examples.

#### Creating Global Virtual Channels in NI MAX

1. Launch NI MAX.
2. In NI MAX, right-click Data Neighborhood and select Create
 New .
3. In the Create New window, select NI-DAQmx Global Virtual
 Channel .
4. Click Next . The DAQ Assistant opens.
5. Select an I/O type, such as analog input.
6. Select the physical channel of the hardware.
7. Type the global virtual channel name.
8. Click Finish .
9. Save your configuration.

#### Modifying Global Virtual Channels in NI MAX

1. Launch NI MAX.
2. In NI MAX, navigate to Data Neighborhood»NI-DAQmx Global Virtual Channel .
3. Select the global channel to modify. The Configuration window opens.
4. Click the Details 
 
 button to view the physical channel. [IMAGE alt='image' src='GUID-CD698D43-5996-4BDD-8F58-8DF0B6519944-a5.png']
5. Right-click the physical channel and select Change Physical Channel to update the physical channel. [IMAGE alt='image' src='GUID-177C8545-2F80-4E20-860C-59131AB02284-a5.png']
6. Select the desired physical channel and click OK .
7. Click Save .

Parent topic:

Enabling Physical Hardware

Related information:

- NI-DAQmx User Manual: Naming Channels, Tasks, and
 Scales
- Creating a Virtual Channel in NI-DAQmx and Using It in LabVIEW
- Performing DAQmx Channel Calibration in MAX Using
 Wizard

<!--NI_TOPIC bundle=pcb-assembly-test-toolkit-labview path=power-supply-test-sequence.html language=enus -->
## TOPIC 00042: Power Supply Test Sequence

- bundle_id: `pcb-assembly-test-toolkit-labview`
- source_path: `power-supply-test-sequence.html`
- source_url: https://docs-be.ni.com/bundle/pcb-assembly-test-toolkit-labview/raw/resource/enus/power-supply-test-sequence.html
- document_id: `pcb-assembly-test-toolkit-labview`
- page_type: `leaf`
- content_type: `reference`
- source_description: The Power Supply Test sequences sources voltage from a power module and measures all test points on the PCB simultaneously with an analog input module. This TestStand sequence uses the LabVIEW measurement libraries. By default, the test sequence is installed to the following location: C:\Users\Publi

### Power Supply Test Sequence

The Power Supply Test sequences sources voltage from a power module and measures
 all test points on the PCB simultaneously with an analog input module.

This TestStand sequence uses the LabVIEW measurement libraries. By default, the test
 sequence is installed to the following location: C:\Users\Public\Documents\National Instruments\PCB Assembly Test
 Toolkit for LabVIEW\TestStand\Automation\Power Supply
 Tests

#### Required Driver Application Software

#### Highlighted Features

Power Supply Test (with Trigger)

- DAQ_Power Supply Source and Measure
- DAQ_Time Domain Measurement

Power Supply Test (without Trigger)

- DAQ_Power Supply Source and Measure
- DAQ_DC-RMS Voltage Measurement

Power down all Power Supplies

#### Hardware Configuration

[IMAGE alt='image' src='GUID-DE8C7275-5B51-48ED-9B14-E00BF727742E-a5.png']

#### Using the Sequence with
 Physical Hardware

1. Run the sequence once in simulation mode. Running the sequence
 in simulation mode creates the required global virtual channels in NI MAX that
 you must modify. Note In this
 example, physical and global virtual channels are used to configure the
 terminal or pin to perform the instrument actions. Global virtual channels
 are software entities that encapsulate the physical channel along with other
 channel specific information such as range, terminal configuration, and
 custom scaling. You can create global channels in NI MAX and call them from
 measurement libraries.
2. Right click the Import Hardware Config step and select Run Mode»Skip to skip the step.
3. Configure the remaining sequences. Open each sequence and
 examine the Note to run with Hardware entry.
4. Configure the Power Supply and Measure (with Trigger)
 Sequence sequence.
  1. Update the Physical Channels input to use your
 power module channel in the Power Supply Source and Measure initialize
 step.
  2. Open NI-MAX and update the physical channel linked to the global virtual
 channels used in the Time Domain Measurement initialize steps:
 TP_Power0 , TP_Power1 
 and TP_Power2 . Refer to Creating and
 Modifying Global Virtual Channels for more information.
  3. Open the Time Domain Measurement – Configure TP 
 step and update the Digital Trigger Source .
  4. Update the Timing Engine to use your trigger line
 in the Power Supply Configure and Measure step.
  5. Set the Periodic waveform input to
 True to perform time domain analysis in the
 measured data in the Time Domain Measurement - Fetch
 TP step.
  6. Review the power and analog input pin configurations for your use
 case.
  7. Save the sequence.
5. Configure the Power Supply and Measure (without Trigger) 
 sequence.
  1. Update the Physical Channels input to use your
 power module channel in the Power Supply Source and Measure initialize
 step.
  2. Open NI-MAX and update the physical channel linked to the global virtual
 channels used in the Time Domain Measurement initialize steps:
 TP_Power0 , TP_Power1 
 and TP_Power2 . Refer to Creating and
 Modifying Global Virtual Channels for more information.
  3. Review the power and analog input pin configurations for your use
 case.
  4. Save the sequence.
6. Configure the Power down all Power Supplies 
 sequence.
  1. Open the Power Supply Source and Measure -
 Initialize step and update the Physical
 Channels input to use your power module channel.
  2. Review the power configurations for your use case.
  3. Save the sequence.

Parent topic:

Automation Test Sequences

Related tasks:

- Creating and Modifying Global Virtual Channels

<!--NI_TOPIC bundle=pcb-assembly-test-toolkit-labview path=ps-source-measure-library.html language=enus -->
## TOPIC 00043: DAQ_Power Supply Library

- bundle_id: `pcb-assembly-test-toolkit-labview`
- source_path: `ps-source-measure-library.html`
- source_url: https://docs-be.ni.com/bundle/pcb-assembly-test-toolkit-labview/raw/resource/enus/ps-source-measure-library.html
- document_id: `pcb-assembly-test-toolkit-labview`
- page_type: `leaf`
- content_type: `reference`
- source_description: DAQ_Power Supply Library VIs initialize, configure, source, measure, and close user-configurable power supply pins. This library is applicable for the TestScale TS-15200 power supply module. Use the PS Initialize VI to initialize hardware and create a DAQmx Task for power supply measurement. Pass th

### DAQ_Power Supply Library

DAQ_Power Supply Library VIs initialize, configure, source, measure, and close
 user-configurable power supply pins. This library is applicable for the TestScale TS-15200
 power supply module.

1. Use the PS Initialize VI to initialize hardware and create a DAQmx Task for power supply
 measurement.
2. Pass the power supply measurement DAQmx Task to the DAQ_PS Configure and Measure VI.
3. Configure the DAQ_PS Configure and Measure VI.
  - 
  - Execution Settings —By default, the Configure and Measure VI also executes the
 measurement. If you are using a trigger for your
 measurement, choose the Configure Only or Measure Only
 execution option to avoid automatic execution. Use the
 Skip Analysis? setting to select whether to perform post
 analysis on the measured data. Use post analysis to
 derive maximum voltage, current, power, and average
 power.
  - Configuration Settings —Configure the required power channel settings. The channel settings include output
 voltage, output current, sensing methods, idle output
 behavior and output enabled state. Configure the timing
 related parameters for power supply generation and
 measurement. The Timing setting configures sample clock
 source input, sampling rate, number of samples, and the
 sample timing engine used for the power supply task.Acquisition Time = Number of Samples/Sample Rate
 Specify Auto to automatically select the timing
 engine. Note The
 maximum sampling rate for the TS-15200 is 10 kS/s.
 Values that exceed the maximum sampling rate generate
 errors. Note Refer to
 the relevant specifications document to identify the
 maximum sampling rate for your device. Values that
 exceed the maximum sampling rate generate errors. Configure triggers to start the source or
 measurement based on various trigger events. Trigger
 options include no trigger or digital start
 triggers.
  - Output Data —The VI outputs the following data.
  - Voltage and Current Waveforms —Displays the captured voltage and current
 waveform during sourcing power supply
  - Power Measurements —Provides the derived post-analyzed data from the
 captured waveforms.
  - Acquisition Time —Calculated acquisition time for the measurement.
4. Wire the updated power supply task from DAQmx Task Out.
5. Close the power supply measurement task using DAQ_PS Close VI.

#### Execution Option Settings

Configure and Measure

Configure Only

Measure Only

#### Best Practices

- For faster measurements, set the maximum sampling rate possible for the given
 Sample Clock Source input and assign a smaller Number of Samples to
 capture.
- To access this VI in a software-based timing setting, set the sampling rate for
 the sample clock source and set the number of samples to two (the minimum
 samples supported by DAQmx). Invoke this VI multiple times in a software loop to
 get the actual required number of samples.
- For better resolution, increase the number of samples (for example, 1000
 samples).

Figure 15.

[IMAGE alt='image' src='GUID-831B0991-A722-4FAE-A624-BF4DC5976B4E-a5.png']

Parent topic:

Measurement Libraries

<!--NI_TOPIC bundle=pcb-assembly-test-toolkit-labview path=run-demo.html language=enus -->
## TOPIC 00044: Running Demo Test Sequences with Simulated Hardware

- bundle_id: `pcb-assembly-test-toolkit-labview`
- source_path: `run-demo.html`
- source_url: https://docs-be.ni.com/bundle/pcb-assembly-test-toolkit-labview/raw/resource/enus/run-demo.html
- document_id: `pcb-assembly-test-toolkit-labview`
- page_type: `leaf`
- content_type: `task`
- source_description: PCB Assembly Test Toolkit for LabVIEW includes demo test sequences that use simulated hardware by default. Complete the following steps to open a test sequence in TestStand and run the sequence in simulation mode. To modify a test sequence to use physical hardware, refer to the PDF documentation in

### Running Demo Test Sequences with Simulated
 Hardware

PCB Assembly Test
 Toolkit for LabVIEW includes demo test sequences that use
 simulated hardware by default.

Complete the following steps to open a test sequence in TestStand and run the
 sequence in simulation mode. To modify a test sequence to use physical hardware,
 refer to the PDF documentation in the test sequence folder.

1. Navigate to C:\Users\Public\Documents\National Instruments\PCB Assembly Test
 Toolkit for LabVIEW\TestStand\Automation .
2. Locate and double-click the desired test sequence. The test sequence opens in
 TestStand.
3. Select Execute»Single Pass to run the test sequence.
4. When execution completes, click review the report in the
 Report pane.
5. (Optional) select Execute»Restart to run the sequence again.

<!--NI_TOPIC bundle=pcb-assembly-test-toolkit-labview path=sensor-test-sequence.html language=enus -->
## TOPIC 00045: Sensor Test Sequence

- bundle_id: `pcb-assembly-test-toolkit-labview`
- source_path: `sensor-test-sequence.html`
- source_url: https://docs-be.ni.com/bundle/pcb-assembly-test-toolkit-labview/raw/resource/enus/sensor-test-sequence.html
- document_id: `pcb-assembly-test-toolkit-labview`
- page_type: `leaf`
- content_type: `reference`
- source_description: The Sensor Test sequence demonstrates temperature measurements captured with a thermistor, RTD, and thermocouple sensing devices using C Series temperature input modules (NI-9211, NI-9217), C Series voltage input modules (NI-9215), and analog input modules (TS-15100, TS-15200). This TestStand sequen

### Sensor Test Sequence

The Sensor Test sequence demonstrates temperature measurements captured with a
 thermistor, RTD, and thermocouple sensing devices using C Series temperature input
 modules (NI-9211, NI-9217), C Series voltage input modules (NI-9215), and analog input
 modules (TS-15100, TS-15200).

This TestStand sequence uses the LabVIEW measurement libraries. By default, the test
 sequence is installed to the following location: C:\Users\Public\Documents\National Instruments\PCB Assembly Test
 Toolkit for LabVIEW\TestStand\Automation\Sensor Tests

#### Required Driver Application Software

#### Highlighted Features

Thermistor Test - cDAQ

- DAQ_DC Voltage Generation
- DAQ_Temperature Thermistor Measurement

Thermistor Test - TestScale

- DAQ_Power Supply Source and Measure
- DAQ_Temperature Thermistor Measurement

RTD Test

Thermocouple Test

Turn Off all AO Channels

Power down all Power Supplies

#### Hardware Configuration

The following figure illustrates the hardware connections for this example
 sequence.

Figure 10.

[IMAGE alt='image' src='GUID-A177B631-38F2-4A57-83A7-B667026D5797-a5.png']

For cDAQ thermistor measurements, the analog input terminal configuration is
 differential and floating. To avoid common mode voltage errors, connect a direct
 wire or bias resistor between AIx- to
 COM based on the ground differences between the sensing
 and the measurement device. The possible bias resistor values range from 1 kΩ to 10
 kΩ. Refer to *Measurement System Types and Signal Sources* for more
 information.

Figure 11.

[IMAGE alt='image' src='GUID-91AFFDB7-173E-4214-8BEC-357E77522F52-a5.png']

For the TestScale thermistor measurement, the default analog input terminal
 configuration is RSE.

Refer to the documentation for your specific device for pinouts and other
 information necessary to adapt this example sequence to your application.

For shielded thermocouple measurements, connect the COM
 terminal of your device to the shield. Connect the shield to a common-mode voltage
 reference for the thermocouple. A common-mode voltage reference is a voltage that is
 within ±1.2 V of the common-mode voltage of the thermocouple. If you are using a
 floating thermocouple or a thermocouple within ±1.2 V of earth ground, connect
 COM and the shield to earth ground. The shield grounding
 methodology varies depending on the application. Refer to the following for an
 illustration of a typical shielding configuration.

[IMAGE alt='image' src='GUID-1668D059-FD32-4FCF-B1C6-4CA809838BC3-a5.png']

Refer to *Taking a Thermocouple Measurement in LabVIEW* for details about
 thermocouple measurements using NI DAQ devices.

#### Using the Sequence with Physical
 Hardware

1. Run the sequence once in simulation mode. Running the sequence
 in simulation mode creates the required global virtual channels in NI MAX that
 you must modify. Note In this
 example, physical and global virtual channels are used to configure the
 terminal or pin to perform the instrument actions. Global virtual channels
 are software entities that encapsulate the physical channel along with other
 channel specific information such as range, terminal configuration, and
 custom scaling. You can create global channels in NI MAX and call them from
 measurement libraries.
2. Right click the Import Hardware Config step and select Run Mode»Skip to skip the step.
3. Configure the remaining sequences. Open each sequence and
 examine the Note to run with Hardware entry.
4. Configure the Thermistor Test - cDAQ sequence.
  1. Open NI-MAX and update the physical channel linked to the global virtual
 channels used in the DC Voltage Generation and Temperature Thermistor
 Measurement initialize steps: TS_THEX and
 TP_TH0 . Refer to Creating and Modifying
 Global Virtual Channels for more information.
  2. Update the Thermistor Parameter and Terminal Configuration based on your
 thermistor settings to ensure accurate temperature measurements.
  3. Review the analog output and analog input pin configurations for your
 use case.
  4. Save the sequence.
5. Configure the Thermistor Test - TestScale sequence.
  1. Open NI-MAX and update the physical channel linked to the global virtual
 channels used in the Temperature Thermistor Measurement initialize step:
 TS_TH1 . Refer to Creating and Modifying
 Global Virtual Channels for more information.
  2. Open the PS – Initialize step and update the
 Physical Channels input to use the TestScale power module pin.
  3. Update the Thermistor Parameter and Terminal Configuration based on your
 thermistor settings to ensure accurate temperature measurements.
  4. Review the analog output and analog input pin configurations for your
 use case.
  5. Save the sequence.
6. Configure the RTD Test sequence.
  1. Open NI-MAX and update the physical channel linked to the global virtual
 channels used in the Temperature RTD Measurement initialize step:
 TP_RTD . Refer to Creating and Modifying
 Global Virtual Channels for more information.
  2. Update the RTD Type, Sensor Resistance at 0 deg C (ohm), Resistance
 Configuration, Current Excitation Source, Current Excitation (A), and
 ADC Timing Mode parameters based on your RTD settings to ensure accurate
 temperature measurements.
  3. Save the sequence.
7. Configure the Thermocouple Test sequence.
  1. Open NI-MAX and update the physical channel linked to the global virtual
 channels used in the Temperature Thermocouple Measurement initialize
 step: TP_TC . Refer to Creating and
 Modifying Global Virtual Channels for more information.
  2. Update the Thermocouple Type, CJC Temp (deg C), Enable Autozero, and
 Auto Zero Mode parameters based on your RTD settings to ensure accurate
 temperature measurements.
  3. Save the sequence.
8. Configure the Turn Off all AO Channels 
 sequence.
  1. Open the DC Voltage Generation - Initialize AO
 Channels step and update the Physical
 Channels input to use your analog output channel.
  2. Review the analog output pin configurations for your use case.
  3. Save the sequence.
9. Configure the Turn Off Power Channel sequence.
  1. Open the Initialize step and update the
 Physical Channels input to use your power
 channel.
  2. Review the analog output configurations for your use case.
  3. Save the sequence.
  4. 

Parent topic:

Automation Test Sequences

Related tasks:

- Creating and Modifying Global Virtual Channels

Related information:

- Measurement System Types and Signal Sources
- Taking a Thermocouple Measurement in LabVIEW

<!--NI_TOPIC bundle=pcb-assembly-test-toolkit-labview path=sig-voltage-gen-library.html language=enus -->
## TOPIC 00046: DAQ_Signal Voltage Generation Library

- bundle_id: `pcb-assembly-test-toolkit-labview`
- source_path: `sig-voltage-gen-library.html`
- source_url: https://docs-be.ni.com/bundle/pcb-assembly-test-toolkit-labview/raw/resource/enus/sig-voltage-gen-library.html
- document_id: `pcb-assembly-test-toolkit-labview`
- page_type: `leaf`
- content_type: `reference`
- source_description: DAQ_Signal Voltage Generation Library VIs provides options to generate various waveform voltage signal tones (single/multi) over one or more given generation times on analog output terminals of DAQmx. This library is applicable for analog output channels and modules. Use the DAQ_SV Gen Initialize VI

### DAQ_Signal Voltage Generation Library

DAQ_Signal Voltage Generation Library VIs provides options to generate various waveform
 voltage signal tones (single/multi) over one or more given generation times on analog output
 terminals of DAQmx. This library is applicable for analog output channels and
 modules.

1. Use the DAQ_SV Gen Initialize VI to initialize hardware and create a DAQmx Task for signal
 voltage generation.
2. Pass the signal voltage generation DAQmx Task to the DAQ_SV Gen Configure and Measure
 VI.
3. Configure the DAQ_SV Gen Configure and Measure VI.
  - 
  - Configuration Settings —Configure the range and terminal settings. Global settings are applied to any channel
 without channel-specific settings. Use the Specific Channel
 Settings to configure a channel, including physical analog
 input voltage channels, to a specific limit. Configure
 the signal generator settings for single tone sine
 waves, single tone square waves, or multi-tone
 signals. Configure the timing related parameters
 for signal voltage generation. The Timing setting
 configures sample clock source input, sampling rate,
 number of samples, and the sample timing engine used for
 the DAQmx Task.Acquisition Time = Number of Samples/Sample Rate
 Specify Auto to automatically select the timing
 engine. Note For NI
 63xx (X Series) and other DAQ devices, use Auto mode
 only. The sample timing engine is only used for cDAQ and
 TestScale platforms, which support multiple timing
 engines. Note Refer to
 the relevant specifications document to identify the
 maximum sampling rate for your device. Values that
 exceed the maximum sampling rate generate errors. Configure triggers to start the source or
 measurement based on various trigger events. Trigger
 options include no trigger or digital start
 triggers.
  - Output Data —The VI outputs the following data.
  - Voltage Waveforms —Displays the captured signal voltage
 waveforms.
  - Generation Time —Returns the actual generation time by the
 instrument in seconds, based on the coerced value
 of the sample clock rate and input generation
 time.
4. Wire the updated signal voltage generation task from DAQmx Task Out.
5. Close the signal voltage generation task using DAQ_SV Gen Close VI.

#### Best Practices

Figure 23.

[IMAGE alt='image' src='GUID-7FCF5754-0C09-4914-8878-8841555B05D2-a5.png']

Parent topic:

Measurement Libraries

<!--NI_TOPIC bundle=pcb-assembly-test-toolkit-labview path=static-digital-state-gen.html language=enus -->
## TOPIC 00047: DAQ_Static Digital State Generation Library

- bundle_id: `pcb-assembly-test-toolkit-labview`
- source_path: `static-digital-state-gen.html`
- source_url: https://docs-be.ni.com/bundle/pcb-assembly-test-toolkit-labview/raw/resource/enus/static-digital-state-gen.html
- document_id: `pcb-assembly-test-toolkit-labview`
- page_type: `leaf`
- content_type: `reference`
- source_description: DAQ_Static Digital State Generation Library VIs generate static digital data on all configured digital channel lines in the DAQmx task. This library is applicable for digital output channels and modules.This library does not support digital ports and returns an error. Specify the ports in line-based

### DAQ_Static Digital State Generation
 Library

DAQ_Static Digital State Generation Library VIs generate static digital data on all
 configured digital channel lines in the DAQmx task. This library is applicable for
 digital output channels and modules.

Note

DIO/port0/line0:31

1. Use the DAQ_Static Dig Gen Initialize VI to initialize hardware and create a
 DAQmx Task for static digital state generation.
2. Pass the static digital state generation DAQmx Task to the DAQ_Static Dig Gen Configure and
 Measure VI.
3. Configure the DAQ_Static Dig Gen Configure and Measure VI.
  - 
  - Data to Write —Represents the digital data to output. Each element in the
 array corresponds to a line in your task. The number of
 elements in the array must match the number of lines in the
 task.
  - Channel Identifiers —Returns the corresponding digital output channels lines to
 which the generation data is mapped linearly.
4. Wire the updated static digital state generation task from DAQmx Task Out and perform any
 additional operations.
5. Close the static digital state generation task using DAQ_Static Dig Gen Close VI.

Figure 29.

[IMAGE alt='image' src='GUID-11601CE5-DFEE-43F9-BB69-DEA69A3E4CE9-a5.png']

Parent topic:

Measurement Libraries

<!--NI_TOPIC bundle=pcb-assembly-test-toolkit-labview path=static-digital-state-measure.html language=enus -->
## TOPIC 00048: DAQ_Static Digital State Measurement Library

- bundle_id: `pcb-assembly-test-toolkit-labview`
- source_path: `static-digital-state-measure.html`
- source_url: https://docs-be.ni.com/bundle/pcb-assembly-test-toolkit-labview/raw/resource/enus/static-digital-state-measure.html
- document_id: `pcb-assembly-test-toolkit-labview`
- page_type: `leaf`
- content_type: `reference`
- source_description: DAQ_Static Digital State Measurement Library VIs measure the static digital data on all configured digital channel lines in the DAQmx task. This library is applicable for digital input channels and modules. This library does not support digital ports and returns an error. Specify the ports in line-b

### DAQ_Static Digital State Measurement
 Library

DAQ_Static Digital State Measurement Library VIs measure the static digital data on all
 configured digital channel lines in the DAQmx task. This library is applicable for
 digital input channels and modules.

Note

DIO/port0/line0:31

1. Use the DAQ_Static Dig Meas Initialize VI to initialize hardware and create a
 DAQmx Task for static digital state measurement.
2. Pass the static digital state measurement DAQmx Task to the DAQ_Static Dig Meas Configure
 and Measure VI.
3. Obtain the following outputs:
  - 
  - Channel Line Identifiers —Returns the digital channels lines in the task.
  - Line States —Outputs the acquired states of digital lines configured in
 the DAQmx Task. Each element in this array maps linearly to
 a line in the task which is returned in the channel line
 identifier array.
4. Wire the updated static digital state measurement task from DAQmx Task Out and perform any
 additional operations.
5. Close the static digital state measurement task using DAQ_Static Dig Meas Close VI.

#### Best Practices

To ensure complete cycles are generated for each tone, select a generation time (in
 seconds) that is an integral multiple of the time period (1/Frequency (Hz)). For
 multi-tone generation, the generation time must be an integral multiple of the time
 period for all tones.

Figure 28.

[IMAGE alt='image' src='GUID-060C9D57-9555-4B18-9F0B-63DBB068EA0D-a5.png']

Parent topic:

Measurement Libraries

<!--NI_TOPIC bundle=pcb-assembly-test-toolkit-labview path=sync-example-seq.html language=enus -->
## TOPIC 00049: Synchronization Example Sequence

- bundle_id: `pcb-assembly-test-toolkit-labview`
- source_path: `sync-example-seq.html`
- source_url: https://docs-be.ni.com/bundle/pcb-assembly-test-toolkit-labview/raw/resource/enus/sync-example-seq.html
- document_id: `pcb-assembly-test-toolkit-labview`
- page_type: `leaf`
- content_type: `reference`
- source_description: The Synchronization example sequence demonstrates synchronization of multiple DAQ devices or multiple chassis using generation and measurement libraries that target analog digital I/O channels and modules. This TestStand sequence uses the LabVIEW measurement libraries. By default, the test sequence

### Synchronization Example Sequence

The Synchronization example sequence demonstrates synchronization of multiple DAQ
 devices or multiple chassis using generation and measurement libraries that target
 analog digital I/O channels and modules.

This TestStand sequence uses the LabVIEW measurement libraries. By default, the test
 sequence is installed to the following location: C:\Users\Public\Documents\National Instruments\PCB Assembly Test
 Toolkit for LabVIEW\TestStand\Automation\Synchronization
 Example

#### Required Driver Application Software

#### Highlighted Features

SignalVoltageGeneration and TimeDomainMeasurement

- DAQ_Synchronization
- DAQ_Signal Voltage Generation
- DAQ_Time Domain Measurement

DynamicDigitalPatternGeneration and DynamicDigitalPatternMeasurement

- DAQ_Synchronization
- DAQ_Dynamic Digital Pattern Generation
- DAQ_Dynamic Digital Pattern Measurement

DigitalClockGeneration and DigitalPWMMeasurement

- DAQ_Digital Clock Generation
- DAQ_Digital PWM Measurement

Turn Off all AO Channels

Turn Off all DO Channels

#### Hardware Configuration

The following figures illustrates the specific hardware connections for this example
 sequence using TestScale backplanes and core modules. For NI 63xx (X Series) DAQ
 instruments, PFI signals are routed directly using the PFI resources available on
 the instrument connector. Refer to your hardware specifications to understand the
 available PFI routing signals for clocks and triggers.

In the first figure,
 PFI0 routes the sample clock and
 PFI1 routes the start trigger.

Figure 12.

[IMAGE alt='image' src='GUID-0576E6CA-80DA-47EA-A9B6-B70CA625DB1F-a5.png']

PFI0

PFI1

Figure 13.

[IMAGE alt='image' src='GUID-8F332035-DBC3-46BA-AF36-3B8E999B7EB0-a5.png']

Figure 14.

[IMAGE alt='image' src='GUID-BB8B4FCF-7A0A-4AA3-A3CD-CF8AEE054A22-a5.png']

Refer to the documentation for your specific device for pinouts and other
 information necessary to adapt this example sequence to your application.

#### Using the Sequence with Physical
 Hardware

1. Run the sequence once in simulation mode. Running the sequence
 in simulation mode creates the required global virtual channels in NI MAX that
 you must modify. Note In this
 example, physical and global virtual channels are used to configure the
 terminal or pin to perform the instrument actions. Global virtual channels
 are software entities that encapsulate the physical channel along with other
 channel specific information such as range, terminal configuration, and
 custom scaling. You can create global channels in NI MAX and call them from
 measurement libraries.
2. Right click the Import Hardware Config step and select Run Mode»Skip to skip the step.
3. Configure the remaining sequences. Open each sequence and
 examine the Note to run with Hardware entry.
4. Configure the SignalVoltageGeneration and
 TimeDomainMeasurement sequence.
  1. Open NI-MAX and update the physical channel linked to the global virtual
 channels used in the Signal Voltage Generation and Time Domain
 Measurement initialize steps: TS_Analog0 and
 TP_Analog0 . Refer to Creating and
 Modifying Global Virtual Channels for more information.
  2. Update the routing path in the Route
 Synchronization Signals step for the chassis where the
 signal originates to export the sample clock and start trigger of the
 Signal Voltage Generation task to the target PFI lines.
  3. Open the Time Domain Measurement – Configure TP 
 step and update the Sample Clock Source and
 Digital Trigger Source to use external PFI
 lines.
  4. Set the Periodic Waveform input to
 True to enable all time domain measurements
 in the Time Domain Measurement - Read Captured
 Waveform step.
  5. Review the analog output and analog input pin configurations for your
 use case.
  6. Save the sequence.
5. Configure the DynamicDigitalPatternGeneration and
 DynamicDigitalPatternMeasurement sequence.
  1. Open NI-MAX and update the physical channel linked to the global virtual
 channels used in the Dynamic Digital Pattern Generation and Dynamic
 Digital Pattern Measurement initialize steps:
 TS_Digital0:1 and
 TP_Digital0:1 . Refer to Creating and
 Modifying Global Virtual Channels for more information.
  2. Update the routing path in the Route Synchronization
 Signals step for the DAQ instrument or chassis where the
 signal originates to export the sample clock and start trigger of the
 Dynamic Digital Pattern Generation task to the target PFI lines.
  3. Update the Sample Clock Source and
 Digital Trigger Source to use external PFI
 lines in the Dynamic Digital Measurement – Configure
 TP step.
  4. Update the Number of Digital Lines configured for
 signal generation in the Generate Port Digital Data 
 step.
  5. Review the digital output and digital input pin configurations for your
 use case.
  6. Save the sequence.
6. Configure the DigitalClockGeneration and
 DigitalPWMMeasurement sequence.
  1. Update the Output Terminal and Physical
 Channel (Counter) used in the Digital Clock Generation
 and Digital PWM Measurement initialize steps.
  2. Review the digital output and digital input pin configurations for your
 use case.
  3. Save the sequence.
7. Configure the Turn Off all AO Channels sequence.
  1. Open the DC Voltage Generation - Initialize AO
 Channels step and update the Global
 Channels input to use your analog output channel.
  2. Update Number of Analog Lines to be configured to
 0 V in the Assign AO
 Voltages step.
  3. Review the analog output pin configurations for your use case.
  4. Save the sequence.
8. Configure the Turn Off all DO Channels sequence.
  1. Open the DC Voltage Generation - Initialize DO
 Channels step and update the Global
 Channels input to use your digital output channel.
  2. Update Number of Digital Lines to be configured
 to a digital LOW state in the Assign
 Digital States step.
  3. Review the digital output pin configurations for your use case.
  4. Save the sequence.

#### Physical Hardware
 Considerations

Ensure a common ground connection is provided between digital input and digital
 output resources.

In digital pattern measurement, make sure to use the same sample clock rate in both
 digital input and digital output for precise data extraction from the testpoint.

Digital states are provided as True or
 False Boolean values to the VIs. The corresponding
 voltage level, for example, a digital HIGH state, depends on individual
 resources.

(TestScale only) TS-15050 DIO channels use 3.3 V TTL, single-ended I/O. The TS-15120
 DIO voltage level is controlled by manual jumper connections. TS-15130 DO channels
 are current sinking outputs. Refer to the individual product documentation for
 additional details.

Parent topic:

Automation Test Sequences

Related concepts:

- Achieving Synchronization

Related tasks:

- Creating and Modifying Global Virtual Channels

Related information:

- Channels: Physical, Virtual, Local Virtual, and Global Virtual
- NI-DAQmx Synchronization of PXI Express Modules
- Choosing a CompactDAQ Synchronization Technology

<!--NI_TOPIC bundle=pcb-assembly-test-toolkit-labview path=sync-library.html language=enus -->
## TOPIC 00050: DAQ_Synchronization Library

- bundle_id: `pcb-assembly-test-toolkit-labview`
- source_path: `sync-library.html`
- source_url: https://docs-be.ni.com/bundle/pcb-assembly-test-toolkit-labview/raw/resource/enus/sync-library.html
- document_id: `pcb-assembly-test-toolkit-labview`
- page_type: `leaf`
- content_type: `reference`
- source_description: DAQ_Synchronization Library VIs route signals between specified source signals and output terminals for the given DAQmx Task. For synchronization examples that use the Synchronization Library, refer to the Backplane Synchronization Example sequence included with the PCB Assembly Test Toolkit for Lab

### DAQ_Synchronization Library

DAQ_Synchronization Library VIs route signals between specified source signals and
 output terminals for the given DAQmx Task.

Note

PCB Assembly Test Toolkit for LabVIEW

1. Retrieve the DAQmx Task from any PCB Assembly Test Toolkit DAQ library Initialize VI.
2. Pass the DAQmx Task to the DAQ_Route synchronization signals VI.
3. Configure the Routing paths input, which specifies the list of paths
 between exported signals and output terminals where routing actions are
 performed. Refer to the Device Routes table in NI Measurement &
 Automation Explorer to determine eligible signals to route for the target
 device. In TestScale, certain internal signals can be routed and
 exposed to external PFI Lines. For more details refer to *Digital
 Routing* in the *TestScale Features* manual. Note The routes created by this VI
 are embedded in a task. Once the DAQmx task is committed, the route is
 committed to the targeted device. When the task is cleared, the route is
 unreserved. Refer to *Task-Based Routing* in the *NI-DAQmx
 User Manual* for more information and refer to *Signal
 Routing* for general information. Note The source signal and output
 terminal can be on different devices as long as a public bus, such as PXIe
 backplane slots or the TestScale backplane, connects the
 devices.
4. Wire the updated task from DAQmx Task Out.
5. Perform additional task configuration using any PCB Assembly Test Toolkit
 library Configure VI.
6. Close the task using any PCB Assembly Test Toolkit for LabVIEW library Close VI.

#### Best Practices

- For faster measurements, set the maximum sampling rate possible for the given
 Sample Clock Source input and assign a smaller Number of Samples to
 capture.
- For better resolution, increase the number of samples (for example, 1000
 samples).

Parent topic:

Measurement Libraries

Related information:

- Task-Based Routing
- Signal Routing
- Digital Routing
- Analog and Digital Input Timing Signals
- Analog and Digital Output Timing Signals

<!--NI_TOPIC bundle=pcb-assembly-test-toolkit-labview path=sync-practices.html language=enus -->
## TOPIC 00051: PCB Assembly Test Toolkit for LabVIEW: Achieving Synchronization

- bundle_id: `pcb-assembly-test-toolkit-labview`
- source_path: `sync-practices.html`
- source_url: https://docs-be.ni.com/bundle/pcb-assembly-test-toolkit-labview/raw/resource/enus/sync-practices.html
- document_id: `pcb-assembly-test-toolkit-labview`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use these best practices to synchronize multiple chassis. Length-match external cables used to route signals like start trigger and sample clock between chassis. Length-matching prevents signal skew between trigger and clock. Configure the generation and measurement cable ends to function at the sam

### Achieving Synchronization

Use these best practices to synchronize multiple chassis.

- Length-match external cables used to route signals like start trigger and sample
 clock between chassis. Length-matching prevents signal skew between trigger and
 clock.
- Configure the generation and measurement cable ends to function at the same sample
 clock rate. Note TestScale modules do
 not divide down external sample clock signals. You must provide the actual
 sample rate input for correct timing details in the measurement
 results.

For multi-chassis synchronization of digital signals that involves data generation in a
 T1 chassis and data measurement in a T2 chassis with a shared clock signal, setup time
 and hold time violations might produce incorrect data measurements. Take the following
 steps to add an offset equivalent to half of the sampling time period at the end of the
 measurement that prevents setup time and hold time violations.

- For the signal measurement system, select Falling Edge as
 the Active Edge parameter in Timing settings.
- For the signal generation system, select Rising Edge as the
 Active Edge parameter in Timing settings.

Refer to the *Related Information*section for more information about
 synchronization at ni.com.

Parent topic:

Creating a Synchronization VI

Related reference:

- Launching the Toolkit in LabVIEW

Related information:

- NI-DAQmx Synchronization of PXI Express Modules
- Choosing a CompactDAQ Synchronization Technology

<!--NI_TOPIC bundle=pcb-assembly-test-toolkit-labview path=sync-vi.html language=enus -->
## TOPIC 00052: PCB Assembly Test Toolkit for LabVIEW: Creating a Synchronization VI

- bundle_id: `pcb-assembly-test-toolkit-labview`
- source_path: `sync-vi.html`
- source_url: https://docs-be.ni.com/bundle/pcb-assembly-test-toolkit-labview/raw/resource/enus/sync-vi.html
- document_id: `pcb-assembly-test-toolkit-labview`
- page_type: `leaf`
- content_type: `task`
- source_description: This example uses the Signal Voltage Generation VI to generate an analog waveform from TestScale Backplane 1. The example uses the Time Domain Measurement Library to measure the waveform with TestScale Backplane 2. To synchronize multiple TestScale chassis you must use a Clock or Trigger SYNC signal

### Creating a Synchronization VI

This example uses the Signal Voltage Generation VI to
 generate an analog waveform from TestScale Backplane 1. The example uses the Time Domain
 Measurement Library to measure the waveform with TestScale Backplane 2. To synchronize
 multiple TestScale chassis you must use a Clock or Trigger SYNC signal over PFI lines
 between chassis. In this example, the analog output module in TestScale
 Backplane 1 exports the sample clock and start trigger through core module PFI lines to the
 analog input module in TestScale Backplane 2.

Note

Launching the Toolkit in LabVIEW

1. Launch LabVIEW and open a new VI.
2. Add the required VIs from the generation, measurement, and synchronization
 libraries to your block diagram. You can access PCB Assembly Test
 Toolkit for LabVIEW LabVIEW VIs from your PCBATT LabVIEW
 project.
3. Wire the VIs and create any necessary controls in the front panel.
  - Ensure that the Route Synchronization Signal VI from the Synchronization
 Library follows the Initialize VI from the Generation Library.
  - Export the clock and trigger signals to external PFI lines.
  - In the Measurement VI use the relevant PFI lines as source inputs for
 the clock and trigger signals.
4. Click File»Save As to save the VI.
5. Configure the front panel and run the VI to test your functionality.

The following image depicts an example of a complete synchronization block
 diagram.

[IMAGE alt='image' src='GUID-920DA275-9228-4644-A644-66E5136BF010-a5.png']

Parent topic:

Using the PCB Assembly Test Toolkit for LabVIEW

<!--NI_TOPIC bundle=pcb-assembly-test-toolkit-labview path=system-components.html language=enus -->
## TOPIC 00053: Components of a PCB Assembly Test Toolkit for LabVIEW System

- bundle_id: `pcb-assembly-test-toolkit-labview`
- source_path: `system-components.html`
- source_url: https://docs-be.ni.com/bundle/pcb-assembly-test-toolkit-labview/raw/resource/enus/system-components.html
- document_id: `pcb-assembly-test-toolkit-labview`
- page_type: `leaf`
- content_type: `reference`
- source_description: PCB Assembly Test Toolkit for LabVIEW is designed for use in a system that might require hardware, drivers, and software to optimize your application. Use the minimum required system components as a starting point for building your system. A system and the surrounding environment must meet any requi

### Components of a 
 PCB Assembly Test Toolkit for LabVIEW System

PCB Assembly Test Toolkit for LabVIEW is designed for use in a system that might
 require hardware, drivers, and software to optimize your application. Use the minimum
 required system components as a starting point for building your system.

Note

#### Supported Hardware

The PCB Assembly Test
 Toolkit for LabVIEW supports all
 devices supported by the following driver application software: NI-845x, NI-DAQmx,
 NI-DMM, NI-Serial, and NI-SWITCH. The PCB Assembly Test
 Toolkit for LabVIEW provides specific support for the following NI
 hardware:

- PXIe, PCIe, and USB DAQ devices
- PXIe and USB DMM instruments
- PXI and PXIe switches
- CompactDAQ (cDAQ) chassis and modules, emphasizing support for temperature measurement
- TestScale chassis and modules
- NI USB-8452 (I 2 C/SPI) modules
- NI USB-232 or PXI-843x serial modules

#### Software Components

PCB Assembly Test
 Toolkit for LabVIEW requires minimum versions of LabVIEW,
 TestStand, and NI driver application software.

| Dependency | Required Version |
| --- | --- |
| LabVIEW | 2021 SP1 or later (32-bit, 64 bit) |
| TestStand | 2021 SP1 or later (32 bit, 64-bit) |
| NI-DAQmx | 2022 Q4 or later |
| NI-DMM | 2022 Q3 or later |
| NI-SWITCH | 2022 Q4 or later |
| NI-Serial | 21.3 or later |
| NI-VISA | 21.5 or later |
| NI-845x | 21.3 or later |

#### LabVIEW Project, Libraries, and
 Examples

PCB Assembly Test
 Toolkit for LabVIEW provides measurement and generation libraries
 to enable common actions performed in PCB assembly electrical functional
 test.

Use these libraries to create or extend your LabVIEW sequencer application. The toolkit
 also provides LabVIEW examples to help you understand the toolkit libraries and
 accelerate your own application development.

Related reference:

- Launching the Toolkit in LabVIEW

#### TestStand Functional Demo and Automated Test
 Sequences

PCB Assembly Test
 Toolkit for LabVIEW includes test sequences to demonstrate how to
 accomplish common tasks such as extracting test data or determining pass/fail test
 results.

Launch C:\Users\Public\Documents\National Instruments\PCB Assembly Test
 Toolkit for LabVIEW\TestStand\PCBA TestStand WorkSpace.tsw to open a TestStand workspace that
 includes all PCB Assembly Test
 Toolkit for LabVIEW functional test sequences and
 measurement libraries.

The Functional Demo TestStand sequence can be found at the following location: C:\Users\Public\Documents\National Instruments\PCB
 Assembly Test Toolkit for LabVIEW\TestStand\PCBA FT Demo\PCBA FT
 Demo.seq

Automated test sequences are located in the following directory: C:\Users\Public\Documents\National Instruments\PCB Assembly Test
 Toolkit for LabVIEW\TestStand\Automation

Related tasks:

- Launching the Toolkit in TestStand
- Running the PCBA FT Demo Test Sequence

Related reference:

- Automation Test Sequences

<!--NI_TOPIC bundle=pcb-assembly-test-toolkit-labview path=temperature-rtd-measure.html language=enus -->
## TOPIC 00054: DAQ_Temperature RTD Measurement Library

- bundle_id: `pcb-assembly-test-toolkit-labview`
- source_path: `temperature-rtd-measure.html`
- source_url: https://docs-be.ni.com/bundle/pcb-assembly-test-toolkit-labview/raw/resource/enus/temperature-rtd-measure.html
- document_id: `pcb-assembly-test-toolkit-labview`
- page_type: `leaf`
- content_type: `reference`
- source_description: DAQ_Temperature RTD Measurement Library VIs initialize, configure, measure, and close user configurable analog input pins to derive temperature measurements from resistance temperature detectors (RTDs). This library is applicable for C Series temperature input modules. The Temperature RTD Measuremen

### DAQ_Temperature RTD Measurement
 Library

DAQ_Temperature RTD Measurement Library VIs initialize, configure, measure, and close
 user configurable analog input pins to derive temperature measurements from resistance
 temperature detectors (RTDs). This library is applicable for C Series temperature input
 modules.

Note

For more details on RTD measurements refer to *Making an RTD or Thermistor
 Measurement in NI-MAX*

1. Use the DAQ_TRTD Meas Initialize VI to initialize hardware and create DAQmx
 Tasks for temperature RTD measurement.
2. Pass the temperature RTD measurement DAQmx Task to the DAQ_TRTD Meas Configure and Measure
 VI.
3. Configure the DAQ_TRTD Meas Configure and Measure VI. Note For more accurate
 measurements, you can use NI MAX to calibrate any global channels specified
 in the Initialize VI.
  - 
  - Execution Settings —By default, the Configure and Measure VI also executes the
 measurement. If you are using a trigger for your
 measurement, choose the Configure Only or Measure Only
 execution option to avoid automatic execution. Use the
 Skip Analysis? setting to select whether to perform
 post-analysis on the measured data. Use post analysis to
 derive maximum voltage, current, power, and average
 power.
  - Configuration Settings —Configure the range and terminal settings. Global settings are applied to any channel
 without channel-specific settings. Use the Specific Channel
 Settings to configure a channel, including physical analog
 input temperature channels, to a specific limit. Note Voltage
 excitation is not supported. The Temperature RTD
 measurement library supports only external or internal
 current excitation. Configure the timing
 related parameters for the measurement. The Timing
 setting configures sample clock source input, sampling
 rate, number of samples, and the sample timing engine
 used for the DAQmx Task.Acquisition Time = Number of Samples/Sample Rate
 Specify Auto to automatically select the timing
 engine. Note For NI
 63xx (X Series) and other DAQ devices, use Auto mode
 only. The sample timing engine is only used for cDAQ and
 TestScale platforms, which support multiple timing
 engines. Note Timing
 engine configurations are identical for the TestScale
 and cDAQ chassis. Refer to *cDAQ-91xx and TestScale
 Chassis Timing Engines* for more
 information. Note The
 maximum aggregate sampling rate for the NI-9217 is 400
 kS/s. Values that exceed the maximum aggregate sampling
 rate generate errors. Note Refer to
 the relevant specifications document to identify the
 maximum sampling rate for your device. Values that
 exceed the maximum sampling rate generate errors. Configure triggers to start the source or
 measurement based on various trigger events. Trigger
 options include no trigger or digital start
 triggers.
  - Output Data —The VI outputs the following data.
  - Temperature Waveforms —Displays the captured temperature
 waveforms.
  - Temperature Measurements —Provides the derived post-analyzed data from the
 captured temperature waveforms, which is output as
 an averaged temperature represented in degrees
 Celsius or degrees Kelvin.
  - Acquisition Time —Calculated acquisition time for the measurement.
4. Wire the updated temperature RTD measurement task from DAQmx Task Out.
5. Close the temperature RTD measurement task using DAQ_TRTD Meas Close VI.

#### Execution Option Settings

Configure and Measure

Configure Only

Measure Only

#### Best Practices

- For faster measurements, set the maximum sampling rate possible for the given
 Sample Clock Source input and assign a smaller Number of Samples to
 capture.
- For better resolution, increase the number of samples (for example, 1000
 samples).

Figure 46.

[IMAGE alt='image' src='GUID-1DC594CA-F804-4738-A292-993DCABA9498-a5.png']

Parent topic:

Measurement Libraries

Related information:

- Making an RTD or Thermistor Measurement in NI-MAX
- cDAQ-91xx and TestScale Chassis Timing Engines

<!--NI_TOPIC bundle=pcb-assembly-test-toolkit-labview path=test-sequence-list.html language=enus -->
## TOPIC 00055: PCB Assembly Test Toolkit for LabVIEW Automation Test Sequences

- bundle_id: `pcb-assembly-test-toolkit-labview`
- source_path: `test-sequence-list.html`
- source_url: https://docs-be.ni.com/bundle/pcb-assembly-test-toolkit-labview/raw/resource/enus/test-sequence-list.html
- document_id: `pcb-assembly-test-toolkit-labview`
- page_type: `leaf`
- content_type: `reference`
- source_description: PCB Assembly Test Toolkit for LabVIEW provides test sequences built in TestStand using toolkit measurement libraries. These test sequences demonstrate basic electrical functional testing. Reuse or modify these test sequence to meet the requirements of your own application. Automation Test Sequences

### Automation Test Sequences

PCB Assembly Test
 Toolkit for LabVIEW provides test sequences built in
 TestStand using toolkit measurement libraries. These test sequences demonstrate basic
 electrical functional testing. Reuse or modify these test sequence to meet the
 requirements of your own application.

Automation Test Sequences are
 located in the following directory: C:\Users\Public\Documents\National Instruments\PCB Assembly Test
 Toolkit for LabVIEW\TestStand\Automation.

Launch C:\Users\Public\Documents\National Instruments\PCB Assembly Test
 Toolkit for LabVIEW\TestStand\PCBA TestStand WorkSpace.tsw to open a TestStand workspace that
 includes all PCB Assembly Test
 Toolkit for LabVIEW automated test sequences and
 measurement libraries.

| Naming Convention | Configuration Feature |
| --- | --- |
| TS_ prefix | Sourcing points in the PCBA board |
| TP_ prefix | Test points in the PCBA board |
| Number (zero-based) suffix | Multiple channels |

<TS_DIn0, TS_DIn1>

<TP_DOut0, TP_DOut1>

The PCB Assembly Test Toolkit for LabVIEW provides the following automated test sequences
 which demonstrate working with various measurements and hardware configurations.

- [Action Button Test Sequence](action-button-test-seq.html) The Action Button Test sequence generates DC voltages to simulate button actions that demonstrate DC-RMS voltage measurements simultaneously on specific PCB test points.
- [Audio Test Sequence](audio-test-sequence.html) The Audio Test sequence demonstrates frequency domain measurements of audio tones captured from the audio amplifier path.
- [Communication Test Sequence](communication-test-seq.html) The Communication Test sequence demonstrates data read and write operations through I 2 C, SPI, and serial communication using a USB-845x or USB-232 device.
- [Digital I/O Test Sequence](digital-io-sequence.html) The Digital I/O Tests sequence simulates digital I/O channels or modules to demonstrate generation and measurement of digital state, digital pattern, clock, digital pulse, and PWM signals.
- [LED Test Sequence](led-test-sequence.html) The LED Test sequence demonstrates measuring differential voltage across the anode and the cathode of the LED. The sequence also demonstrates the validation of a PWM signal with an analog buffer. The sequence simulates analog input and analog output channels or modules.
- [Microphone Test Sequence](mic-test-sequence.html) The Microphone Test sequence uses analog output channels or modules and analog input channels or modules to demonstrate frequency domain measurements of a captured audio signal.
- [Power Supply Test Sequence](power-supply-test-sequence.html) The Power Supply Test sequences sources voltage from a power module and measures all test points on the PCB simultaneously with an analog input module.
- [Sensor Test Sequence](sensor-test-sequence.html) The Sensor Test sequence demonstrates temperature measurements captured with a thermistor, RTD, and thermocouple sensing devices using C Series temperature input modules (NI-9211, NI-9217), C Series voltage input modules (NI-9215), and analog input modules (TS-15100, TS-15200).
- [Synchronization Example Sequence](sync-example-seq.html) The Synchronization example sequence demonstrates synchronization of multiple DAQ devices or multiple chassis using generation and measurement libraries that target analog digital I/O channels and modules.

<!--NI_TOPIC bundle=pcb-assembly-test-toolkit-labview path=teststand-search-dirs.html language=enus -->
## TOPIC 00056: Configuring Search Directories in TestStand

- bundle_id: `pcb-assembly-test-toolkit-labview`
- source_path: `teststand-search-dirs.html`
- source_url: https://docs-be.ni.com/bundle/pcb-assembly-test-toolkit-labview/raw/resource/enus/teststand-search-dirs.html
- document_id: `pcb-assembly-test-toolkit-labview`
- page_type: `leaf`
- content_type: `task`
- source_description: Configure TestStand Search Directories to include the base folder for the PCB Assembly Test Toolkit for LabVIEW libraries. Before you begin, you must create a PCBATT LabVIEW project. Refer to Launching the Toolkit in LabVIEW for details. You will use the path to your project in the following procedu

### Configuring Search Directories in
 TestStand

Configure TestStand Search Directories to include the base folder for the PCB Assembly Test
 Toolkit for LabVIEW libraries.

Note

Launching the Toolkit in LabVIEW

1. Launch TestStand.
2. Select Configure»Search Directories . The Edit Search Directories window appears.
3. Click Add .
4. Navigate to your PCBATT project folder. For example, a typical path is
 C:\Users\<Profile>\Documents\LabVIEW Data\<PCBATT Project
 Name>\ , where <Profile> is your Windows
 profile and <PCBATT Project Name>\ is the name of your
 project.
5. Click OK . In the Edit Search Directories window, the new
 path appears at the top of the Search Directories list.
6. Select the new path and ensure that the Search
 Subdirectories checkbox is enabled. [IMAGE alt='image' src='GUID-84844E44-6CD5-4860-B6C8-1BF42914B4A4-a5.png'] Note You must enable the Search
 Subdirectories option to allow TestStand to locate the individual LabVIEW
 libraries.
7. Click OK .
8. If you are prompted to reload libraries, click OK .

TestStand can now locate the relevant toolkit LabVIEW libraries.

Related reference:

- Launching the Toolkit in LabVIEW
- Software Components

<!--NI_TOPIC bundle=pcb-assembly-test-toolkit-labview path=thermistor-measure.html language=enus -->
## TOPIC 00057: DAQ_Temperature Thermistor Measurement Library

- bundle_id: `pcb-assembly-test-toolkit-labview`
- source_path: `thermistor-measure.html`
- source_url: https://docs-be.ni.com/bundle/pcb-assembly-test-toolkit-labview/raw/resource/enus/thermistor-measure.html
- document_id: `pcb-assembly-test-toolkit-labview`
- page_type: `leaf`
- content_type: `reference`
- source_description: DAQ_Temperature Thermistor Measurement Library VIs initialize, configure, measure, and close user-configurable analog input pins to derive temperature measurements from voltage excited NTC-typed thermistor devices. This library is applicable for NI-63xx (X Series) analog input channels, TestScale an

### DAQ_Temperature Thermistor Measurement
 Library

DAQ_Temperature Thermistor Measurement Library VIs initialize, configure, measure, and
 close user-configurable analog input pins to derive temperature measurements from
 voltage excited NTC-typed thermistor devices. This library is applicable for NI-63xx (X
 Series) analog input channels, TestScale analog input modules, and C Series voltage
 input modules.

Note

For more details on Thermistor measurements, refer to *Making an RTD or Thermistor
 Measurement in NI-MAX*.

1. Use the DAQ_TTR Meas Initialize VI to initialize hardware and create DAQmx Tasks
 for temperature thermistor measurement.
2. Pass the temperature thermistor measurement DAQmx Task to the DAQ_TTR Meas Configure and
 Measure VI.
3. Configure the DAQ_TTR Meas Configure and Measure VI. Note For more accurate
 measurements, you can use NI MAX to calibrate any global channels specified
 in the Initialize VI.
  - 
  - Execution Settings —By default, the Configure and Measure VI also executes the
 measurement. If you are using a trigger for your
 measurement, choose the Configure Only or Measure Only
 execution option to avoid automatic execution.
  - Configuration Settings —Configure the range and terminal settings. Global settings
 are applied to any channel without channel-specific
 settings. Use the Specific Channel Settings to configure a
 channel, including physical analog input temperature
 channels. Note Current
 excitation is not supported. The Temperature Thermistor
 measurement library supports only external voltage
 excitation. Note The
 Temperature Thermistor measurement library provides
 A B C parameter and
 Beta parameter support. Refer
 to the *Measurement Details* section for more
 information. Configure the timing related
 parameters for temperature measurement. The Timing
 setting configures sample clock source input, sampling
 rate, number of samples, and the sample timing engine
 used for the DAQmx Task.Acquisition Time = Number of Samples/Sample Rate
 Specify Auto to automatically select the timing
 engine. Note For NI
 63xx (X Series) and other DAQ devices, use Auto mode
 only. The sample timing engine is only used for cDAQ and
 TestScale platforms, which support multiple timing
 engines. Note Timing
 engine configurations are identical for the TestScale
 and cDAQ chassis. Refer to *cDAQ-91xx and TestScale
 Chassis Timing Engines* for more
 information. Note Refer to
 the relevant specifications document to identify the
 maximum sampling rate for your device. Values that
 exceed the maximum sampling rate generate errors. Configure triggers to start the source or
 measurement based on various trigger events. Trigger
 options include no trigger or digital start
 triggers.
  - Output Data —The VI outputs the following data.
  - Temperature Waveforms —Displays the captured temperature
 waveforms.
  - Temperature Measurements —Provides the derived post-analyzed data from the
 captured temperature waveforms, which is output as
 an averaged temperature represented in degrees
 Celsius or degrees Kelvin.
  - Acquisition Time —Calculated acquisition time for the measurement.
4. Wire the updated temperature thermistor measurement task from DAQmx Task Out.
5. Close the temperature thermistor measurement task using DAQ_TTR Meas Close VI.

#### Execution Option Settings

Configure and Measure

Configure Only

Measure Only

#### Best Practices

- For faster measurements, set the maximum sampling rate possible for the given
 Sample Clock Source input and assign a smaller Number of Samples to
 capture.
- For better resolution, increase the number of samples (for example, 1000
 samples).

- You can use any other external source for voltage excitation in thermistor
 measurements.
- Use a remote sensing method with power supply modules for more reliable voltage
 excitation values.

Figure 47.

[IMAGE alt='image' src='GUID-2C6096BB-4C91-441D-AB5B-86261827EA4A-a5.png']

#### Measurement Details

The Temperature Thermistor measurement library derives temperature measurements from
 thermistor parameters using the following methods. A B C parameter-based temperature
 measurements provides more accurate results than beta parameter-based measurements
 because the beta parameter calculation effectively substitutes zero for the C
 parameter during Steinhart-Hart equation conversion.

A B C Type

1

T

=

A

+

B

ln

⁡

R

+

C

(

ln

⁡

R

)

3

Where 
T = temperature in degrees Kelvin 
R = measured thermistor resistance in Ohms 
A, B, C = constants provided by the thermistor manufacturer

Beta Parameter Type

0

0

A

=

1

T

0

-

1

β

ln

⁡

R

0

B

=

1

β

C

=

0

Substituting these values in a Steinhart-Hart equation gives the following beta
 parameter equation:

1

T

=

1

T

0

+

1

β

ln

⁡

(

R

R

0

)

Where 
T = temperature in degrees Kelvin 
R = measured thermistor resistance in Ohms 
 β = beta parameter provided by thermistor manufacturer in Kelvin 
R<sub>0</sub> = thermistor resistance (in Ohms) in temperature T<sub>0</sub> 
T<sub>0</sub> = 298.15 Kelvin (equivalent to 25 °C)

Parent topic:

Measurement Libraries

Related information:

- Making an RTD or Thermistor Measurement in NI-MAX

<!--NI_TOPIC bundle=pcb-assembly-test-toolkit-labview path=thermocouple-measure.html language=enus -->
## TOPIC 00058: DAQ_Temperature Thermocouple Measurement Library

- bundle_id: `pcb-assembly-test-toolkit-labview`
- source_path: `thermocouple-measure.html`
- source_url: https://docs-be.ni.com/bundle/pcb-assembly-test-toolkit-labview/raw/resource/enus/thermocouple-measure.html
- document_id: `pcb-assembly-test-toolkit-labview`
- page_type: `leaf`
- content_type: `reference`
- source_description: DAQ_Temperature Thermocouple Measurement Library VIs initialize, configure, measure, and close user configurable analog input pins to derive temperature measurements from thermocouples. This library is applicable for C Series temperature input modules. The Temperature Thermocouple measurement librar

### DAQ_Temperature Thermocouple Measurement
 Library

DAQ_Temperature Thermocouple Measurement Library VIs initialize, configure, measure, and
 close user configurable analog input pins to derive temperature measurements from
 thermocouples. This library is applicable for C Series temperature input
 modules.

Note

1. Use the DAQ_TTC Meas Initialize VI to initialize hardware and create DAQmx Tasks
 for temperature thermocouple measurement. The Initialize VI requires cold
 junction compensation (CJC) details for accurate temperature measurements.
 You can use built-in, constant, or channel based CJC input. For information
 about setting up external channel-based CJC measurements, refer to
 *Cold Junction Compensation (CJC) on DAQ Hardware Without Built in
 CJC*. Note For
 more accurate measurements, you can use NI MAX to calibrate any global
 channels specified in the Initialize VI.
2. Pass the temperature thermocouple measurement DAQmx Task to the DAQ_TTC Meas Configure and
 Measure VI.
3. Configure the DAQ_TTC Meas Configure and Measure VI.
  - 
  - Execution Settings —By default, the Configure and Measure VI also executes the
 measurement. If you are using a trigger for your
 measurement, choose the Configure Only or Measure Only
 execution option to avoid automatic execution. Use the
 Skip Analysis? setting to select whether to perform
 post-analysis on the measured data. Use post analysis to
 derive maximum voltage, current, power, and average
 power.
  - Configuration Settings —Configure the range and terminal settings. Global settings are applied to any channel
 without channel-specific settings. Use the Specific Channel
 Settings to configure a channel, including physical analog
 input temperature channels, to a specific limit. Configure the timing related parameters for the
 measurement. The Timing setting configures sample clock
 source input, sampling rate, number of samples, and the
 sample timing engine used for the temperature
 thermocouple measurement task.Acquisition Time = Number of Samples/Sample Rate
 Specify Auto to automatically select the timing
 engine. Note For NI
 63xx (X Series) and other DAQ devices, use Auto mode
 only. The sample timing engine is only used for cDAQ and
 TestScale platforms, which support multiple timing
 engines. Note Timing
 engine configurations are identical for the TestScale
 and cDAQ chassis. Refer to *cDAQ-91xx and TestScale
 Chassis Timing Engines* for more
 information. Note The
 maximum aggregate sampling rate for the NI-9211 is 14
 S/s. Values that exceed the maximum aggregate sampling
 rate generate errors. Note Refer to
 the relevant specifications document to identify the
 maximum sampling rate for your device. Values that
 exceed the maximum sampling rate generate errors. Configure triggers to start the source or
 measurement based on various trigger events. Trigger
 options include no trigger or digital start
 triggers.
    - Specify a CJC Source and CJC Channel.
    - Autozero compensates for internal offsets during
 temperature measurements to increase measurement
 accuracy.
  - Measurement Settings —Choose whether to perform periodic waveform measurements. To capture periodic waveforms
 you must capture multiple cycles. Configure the Voltage
 Frequency (Hz), Voltage Waveform Period (s), and Voltage
 Waveform duty cycle (%) values.
  - Output Data —The VI outputs the following data.
  - Temperature Waveforms —Displays the captured temperature
 waveforms.
  - Temperature Measurements —Provides the derived post-analyzed data from the
 captured temperature waveforms, which is output as
 an averaged temperature represented in degrees
 Celsius or degrees Kelvin.
  - Acquisition Time —Calculated acquisition time for the measurement.
4. Wire the updated temperature thermocouple measurement task from DAQmx Task Out.
5. Close the temperature thermocouple measurement task using DAQ_TTC Meas Close VI.

#### Execution Option Settings

Configure and Measure

Configure Only

Measure Only

#### Best Practices

- For faster measurements, set the maximum sampling rate possible for the given
 Sample Clock Source input and assign a smaller Number of Samples to capture. The
 minimum supported number is 2.
- For better resolution, increase the number of samples (for example, 10 samples). Requesting
 more samples increases the measurement acquisition time.
- NI recommends signal conditioning for accurate temperature measurements from
 thermocouple devices. For more information refer to Signal Conditioning
 Requirements for Thermocouples .
- Refer to Taking a Thermocouple Measurement in LabVIEW for more
 information about thermocouple measurements using NI DAQ devices.

Figure 48.

[IMAGE alt='image' src='GUID-11310DC5-08DC-4A8E-B8B6-1F9EEB24D534-a5.png']

Parent topic:

Measurement Libraries

Related information:

- Cold Junction Compensation (CJC) on DAQ Hardware Without Built in
 CJC
- Taking a Thermocouple Measurement in LabVIEW
- Signal Conditioning Requirements for Thermocouples

<!--NI_TOPIC bundle=pcb-assembly-test-toolkit-labview path=time-measure-library.html language=enus -->
## TOPIC 00059: DAQ_Time Domain Measurement Library

- bundle_id: `pcb-assembly-test-toolkit-labview`
- source_path: `time-measure-library.html`
- source_url: https://docs-be.ni.com/bundle/pcb-assembly-test-toolkit-labview/raw/resource/enus/time-measure-library.html
- document_id: `pcb-assembly-test-toolkit-labview`
- page_type: `leaf`
- content_type: `reference`
- source_description: DAQ_Time Domain Measurement Library VIs initialize, configure, measure, and close user-configurable analog input pins and derive time domain measurements for the measured waveforms. This library is applicable for analog input channels and modules. Use the DAQ_TDV Meas Initialize VI to initialize har

### DAQ_Time Domain Measurement Library

DAQ_Time Domain Measurement Library VIs initialize, configure, measure, and close
 user-configurable analog input pins and derive time domain measurements for the measured
 waveforms. This library is applicable for analog input channels and modules.

1. Use the DAQ_TDV Meas Initialize VI to initialize hardware and create a DAQmx Task
 for time domain measurement.
2. Pass the time domain measurement DAQmx Task to the DAQ_TDV Meas Configure and Measure
 VI.
3. Configure the DAQ_TDV Meas Configure and Measure VI.
  - 
  - Execution Settings —By default, the Configure and Measure VI also executes the
 measurement. If you are using a trigger for your
 measurement, choose the Configure Only or Measure Only
 execution option to avoid automatic execution. Use the
 Skip Analysis? setting to select whether to perform
 post-analysis on the measured data. Use post analysis to
 derive maximum voltage, current, power, and average
 power.
  - Configuration Settings —Configure the range and terminal settings. Global settings are applied to any channel
 without channel-specific settings. Use the Specific Channel
 Settings to configure a channel, including physical analog
 input voltage channels, to a specific limit. Configure
 the timing related parameters for the TDV measurement.
 The Timing setting configures sample clock source input,
 sampling rate, number of samples, and the sample timing
 engine used for the DAQmx Task.Acquisition Time = Number of Samples/Sample Rate
 Specify Auto to automatically select the timing
 engine. Note For NI
 63xx (X Series) and other DAQ devices, use Auto mode
 only. The sample timing engine is only used for cDAQ and
 TestScale platforms, which support multiple timing
 engines. The sample timing engine method is used to
 share a trigger with the TestScale power supply module
 task. Note Refer to
 the relevant specifications document to identify the
 maximum sampling rate for your device. Values that
 exceed the maximum sampling rate generate errors. Configure triggers to start the source or
 measurement based on various trigger events. Trigger
 options include no trigger or digital start
 triggers.
  - Measurement Settings —Choose whether to perform periodic waveform measurements. To
 capture periodic waveforms you must capture multiple
 cycles. Configure the Voltage Frequency (Hz), Voltage
 Waveform Period (s) and Voltage Waveform duty cycle (%)
 values.
  - Output Data —The VI outputs the following data.
  - Voltage Waveforms —Displays the captured voltage waveforms.
  - Time Domain Measurements —Provides the derived post-analyzed data from the
 captured time domain waveforms.
  - Acquisition Time —Calculated acquisition time for the measurement.
4. Wire the updated time domain measurement task from DAQmx Task Out.
5. Close the time domain measurement task using DAQ_TDV Meas Close VI.

#### Execution Option Settings

Configure and Measure

Configure Only

Measure Only

#### Best Practices

- For faster measurements, set the maximum sampling rate possible for the given
 Sample Clock Source input and assign a smaller Number of Samples to
 capture.
- For better resolution, increase the number of samples (for example, 1000
 samples).

Figure 24.

[IMAGE alt='image' src='GUID-C1492AE3-92B8-43F4-B882-66F4634EE385-a5.png']

Parent topic:

Measurement Libraries

<!--NI_TOPIC bundle=pcb-assembly-test-toolkit-labview path=usage.html language=enus -->
## TOPIC 00060: Using the PCB Assembly Test Toolkit for LabVIEW

- bundle_id: `pcb-assembly-test-toolkit-labview`
- source_path: `usage.html`
- source_url: https://docs-be.ni.com/bundle/pcb-assembly-test-toolkit-labview/raw/resource/enus/usage.html
- document_id: `pcb-assembly-test-toolkit-labview`
- page_type: `leaf`
- content_type: `reference`
- source_description: Refer to the following procedures for help with developing your own application.

### Using the PCB Assembly Test
 Toolkit for LabVIEW

Refer to the following procedures for help with developing your own
 application.

<!--NI_TOPIC bundle=pcb-assembly-test-toolkit-labview path=user-manual-welcome.html language=enus -->
## TOPIC 00061: PCB Assembly Test Toolkit for LabVIEW User Manual

- bundle_id: `pcb-assembly-test-toolkit-labview`
- source_path: `user-manual-welcome.html`
- source_url: https://docs-be.ni.com/bundle/pcb-assembly-test-toolkit-labview/raw/resource/enus/user-manual-welcome.html
- document_id: `pcb-assembly-test-toolkit-labview`
- page_type: `leaf`
- content_type: `concept`
- source_description: The PCB Assembly Test Toolkit for LabVIEW User Manual provides detailed descriptions of the product functionality and the step by step processes for use. Looking for Something Else?For information not found in the User Manual for your product, such as specifications and API reference, browse Related

### PCB Assembly Test Toolkit for LabVIEW
 User Manual

The PCB Assembly Test Toolkit for LabVIEW User Manual provides detailed
 descriptions of the product functionality and the step by step processes for use.

#### Looking for Something Else?

For information not found in the User Manual
 for your product, such as specifications and API reference, browse *Related
 Information*.

Related information:

- Software and Driver Downloads
- Release Notes
- License Setup and Activation
- Discussion Forums
- NI Learning Center
