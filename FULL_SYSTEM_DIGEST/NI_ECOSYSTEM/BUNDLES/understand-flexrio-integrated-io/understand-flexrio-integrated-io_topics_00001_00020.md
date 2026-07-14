# NI DOCUMENT BUNDLE: understand-flexrio-integrated-io

<!--NI_BUNDLE_CHUNK bundle=understand-flexrio-integrated-io start=1 end=20 -->
<!--NI_TOPIC bundle=understand-flexrio-integrated-io path=clip-by-module.html language=enus -->
## TOPIC 00001: Socketed Component-Level IP (CLIP) by Module Name

- bundle_id: `understand-flexrio-integrated-io`
- source_path: `clip-by-module.html`
- source_url: https://docs-be.ni.com/bundle/understand-flexrio-integrated-io/raw/resource/enus/clip-by-module.html
- document_id: `understand-flexrio-integrated-io`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following tables provide the Socketed CLIP signals for your FlexRIO Integrated I/O Module.You can create custom CLIP items for your FlexRIO Integrated I/O module. If you choose to develop a custom CLIP item for your application, NI recommends using the CLIP provided with in the LabVIEW example f

### Socketed Component-Level IP (CLIP) by Module
 Name

Notice

- [PXIe-5745 Socketed CLIP Signals](pxie-5745-socketed-clip.html)
- [PXIe-5785 Socketed CLIP Signals](pxie-5785-socketed-clip.html)
- [PXIe-5763 Socketed CLIP Signals](pxie-5763-socketed-clip.html)
- [PXIe-5764 Socketed CLIP Signals](pxie-5764-socketed-clip.html)
- [PXIe-5774 Socketed CLIP Signals](pxie-5774-socketed-clip.html)
- [PXIe-5775 Socketed CLIP Signals](pxie-5775-socketed-clip.html)

<!--NI_TOPIC bundle=understand-flexrio-integrated-io path=clip-file-adapter-module-configuration.html language=enus -->
## TOPIC 00002: CLIP File and Adapter Module Configuration File Locations

- bundle_id: `understand-flexrio-integrated-io`
- source_path: `clip-file-adapter-module-configuration.html`
- source_url: https://docs-be.ni.com/bundle/understand-flexrio-integrated-io/raw/resource/enus/clip-file-adapter-module-configuration.html
- document_id: `understand-flexrio-integrated-io`
- page_type: `leaf`
- content_type: `reference`
- source_description: To access CLIP files and adapter module configuation files, open <NISharedDir>/FlexRIO IO Sockets/FlexRIOIoSocketType1/<Device name>/.All FlexRIO with Integrated I/O targets parse only the .fam files in the subdirectory determined by their target name independent of their bus type or FPGA variant. F

### CLIP File and Adapter Module Configuration
 File Locations

<NISharedDir>/FlexRIO IO Sockets/FlexRIOIoSocketType1/<Device
 name>/

Note

NI-5763

<!--NI_TOPIC bundle=understand-flexrio-integrated-io path=configuring-dio-voltage.html language=enus -->
## TOPIC 00003: Configuring the DIO Voltage

- bundle_id: `understand-flexrio-integrated-io`
- source_path: `configuring-dio-voltage.html`
- source_url: https://docs-be.ni.com/bundle/understand-flexrio-integrated-io/raw/resource/enus/configuring-dio-voltage.html
- document_id: `understand-flexrio-integrated-io`
- page_type: `leaf`
- content_type: `task`
- source_description: In the DIO Voltage Properties dialog box, select General from the Category list to display the DIO Voltage General Properties page. Specify the DIO Voltage. The default DIO Voltage is 3.3 V. To enable DIO voltage configuration through the DIO Voltage API property, select Software Controlled.

### Configuring the DIO Voltage

1. In the DIO Voltage Properties dialog box, select
 General from the Category list
 to display the DIO Voltage General Properties page.
2. Specify the DIO Voltage. 
 Note The default DIO Voltage is
 3.3 V. To enable DIO voltage configuration through the DIO
 Voltage API property, select Software
 Controlled.

<!--NI_TOPIC bundle=understand-flexrio-integrated-io path=configuring-dram-fpga-memory-items.html language=enus -->
## TOPIC 00004: Configuring DRAM with FPGA Memory Items

- bundle_id: `understand-flexrio-integrated-io`
- source_path: `configuring-dram-fpga-memory-items.html`
- source_url: https://docs-be.ni.com/bundle/understand-flexrio-integrated-io/raw/resource/enus/configuring-dram-fpga-memory-items.html
- document_id: `understand-flexrio-integrated-io`
- page_type: `leaf`
- content_type: `task`
- source_description: Use the FPGA memory item interface to use DRAM in the same way that you use block memory and look-up tables (LUT). DRAM memory items appear in the Project Explorer window under the FPGA target. The FPGA memory item interface allows you to partition the physical DRAM banks into multiple memory items.

### Configuring DRAM with FPGA Memory
 Items

Project Explorer

Note

Figure 2.

[IMAGE alt='image' src='GUID-6E553802-276B-49EC-AB39-0CBEB615F757-a5.png']

To configure DRAM with FPGA memory items, complete the following steps.

1. Determine whether you want to create a target-scoped memory item or a VI-defined memory item. 
 To create a target-scoped memory item, which you can access in the entire FPGA VI hierarchy,
 right-click the FPGA target in the Project Explorerwindow and
 select New»Memory from the shortcut menu. The Memory Properties
 dialog box appears.
 To create a VI-defined memory item, place a VI-defined Memory Configuration node on the block
 diagram, right-click the node, and select Configure from the shortcut menu. The Memory
 Properties dialog box appears.Figure 3.Memory Properties Window
 
[IMAGE alt='image' src='GUID-3ED84D21-3A82-4EF7-A392-200F49BA9FEF-a5.png']
2. Configure the memory item in the Memory Properties dialog box.
 Click OK. The memory item is now populated in the Project
 Explorer window under the target. 
 Note If you use a Memory Method Node in a
 single-cycle Timed Loop, make sure the corresponding arbitration option is Arbitrate if
 Multiple Requestors Only or Never Arbitrate.
3. Use the memory item in an FPGA VI.

<!--NI_TOPIC bundle=understand-flexrio-integrated-io path=configuring-flexrio-io-labview.html language=enus -->
## TOPIC 00005: Configuring FlexRIO I/O in LabVIEW

- bundle_id: `understand-flexrio-integrated-io`
- source_path: `configuring-flexrio-io-labview.html`
- source_url: https://docs-be.ni.com/bundle/understand-flexrio-integrated-io/raw/resource/enus/configuring-flexrio-io-labview.html
- document_id: `understand-flexrio-integrated-io`
- page_type: `leaf`
- content_type: `task`
- source_description: The FlexRIO I/O module provides the interface to the physical I/O signals in your system. Right-click the target and select Properties to configure the type of I/O module used in your system. In the IO Module Properties window, select the General heading under the Category column. Check the Enable I

### Configuring FlexRIO I/O in LabVIEW

The FlexRIO I/O module provides the
 interface to the physical I/O signals in your system.

1. Right-click the target and select Properties to
 configure the type of I/O module used in your system.
2. In the IO Module Properties window, select the
 General heading under the
 Category column.
3. Check the Enable IO Modulebox to enable the use of an
 I/O module with your device.
4. Select your I/O module from theIO Modules list, then
 select the I/O module's CLIP from the Component Level IP
 list.
5. Click OK.
6. Select Clock Selections from the
 Category column.
7. Select Clocks and click Create Necessary
 Clocks.
8. Click OK. 
 Note Select Details from the Category list for more
 information about the I/O module in your system.

<!--NI_TOPIC bundle=understand-flexrio-integrated-io path=flexrio-iio-dio-connector.html language=enus -->
## TOPIC 00006: FlexRIO Integrated I/O DIO Connector

- bundle_id: `understand-flexrio-integrated-io`
- source_path: `flexrio-iio-dio-connector.html`
- source_url: https://docs-be.ni.com/bundle/understand-flexrio-integrated-io/raw/resource/enus/flexrio-iio-dio-connector.html
- document_id: `understand-flexrio-integrated-io`
- page_type: `leaf`
- content_type: `concept`
- source_description: The DIO front panel connector includes 8 general purpose digital lines and 4 MGT lanes. You can connect to these resources using a supported cable and accessory, such as the NI SCB-19 (NI part number 156053A-01). These signals are 3.3V LVCMOS bidirectional digital signals and may be used in a variet

### FlexRIO Integrated I/O DIO Connector

The DIO front panel connector includes 8 general purpose digital lines and 4 MGT lanes.
 You can connect to these resources using a supported cable and accessory, such as the NI
 SCB-19 (NI part number 156053A-01). These signals are 3.3V LVCMOS bidirectional digital
 signals and may be used in a variety of applications. Direction is controlled
 independently for each channel through the LabVIEW FPGA Module diagram.

The PFI signals are connected to the FPGA through 3.3 V LVCMOS buffers. These buffers
 allow for direction control, isolation to protect the FPGA from overvoltage conditions,
 and excellent signal quality through the matched 50 Ω output impedance. For exact I/O
 levels and input and output impedances, refer to the device specifications.

The digital lines are protected against overvoltage conditions. The device provides this
 protection through a combination of diode clamps to the +3.3 V and GND lines and a
 positive temperature coefficient resistor for impedance matching.

[IMAGE alt='image' src='GUID-693462A1-8364-46E5-920A-71D6844235D7-a5.gif']

Note

Note

<!--NI_TOPIC bundle=understand-flexrio-integrated-io path=flexrio-mgt-dio-properties.html language=enus -->
## TOPIC 00007: FlexRIO MGT DIO General Properties Page

- bundle_id: `understand-flexrio-integrated-io`
- source_path: `flexrio-mgt-dio-properties.html`
- source_url: https://docs-be.ni.com/bundle/understand-flexrio-integrated-io/raw/resource/enus/flexrio-mgt-dio-properties.html
- document_id: `understand-flexrio-integrated-io`
- page_type: `leaf`
- content_type: `concept`
- source_description: Enter a short description of your concept here (optional). This socket connects the user diagram with the DIO MGTs, Reference Clocks, and support signals. Reference Clock IBUFGTs are already instantiated and should not be added in the CLIP. This page includes the following components: Socketed Compo

### FlexRIO MGT DIO General Properties
 Page

Enter a short description of your concept here (optional).

This socket connects the user diagram with the DIO MGTs, Reference Clocks, and support
 signals. Reference Clock IBUFGTs are already instantiated and should not be added in the
 CLIP.

This page includes the following components:

- Socketed Component-Level IP Declaration —Specifies the socketed CLIP to use.
 Socketed CLIP allows your IP to communicate with both the FPGA VI and the I/O module
 connector interface.

<!--NI_TOPIC bundle=understand-flexrio-integrated-io path=fpga-base-clock-resources-flexrio-iio.html language=enus -->
## TOPIC 00008: FPGA Base Clock Resources for FlexRIO with Integrated I/O

- bundle_id: `understand-flexrio-integrated-io`
- source_path: `fpga-base-clock-resources-flexrio-iio.html`
- source_url: https://docs-be.ni.com/bundle/understand-flexrio-integrated-io/raw/resource/enus/fpga-base-clock-resources-flexrio-iio.html
- document_id: `understand-flexrio-integrated-io`
- page_type: `leaf`
- content_type: `concept`
- source_description: A base clock is a digital signal existing in hardware that you can use as a clock for an FPGA application. You can use the following base clock resources for FlexRIO with Integrated I/O devices: 80 MHz Clock The 80 MHz Onboard Clock is the default clock in your LabVIEW FPGA project. This clock can b

### FPGA Base Clock Resources for FlexRIO with
 Integrated I/O

A base clock is a digital signal existing in hardware that you can use as a clock for an
 FPGA application.

You can use the following base clock resources for FlexRIO with Integrated I/O
 devices:

#### 80
 MHz Clock

The 80 MHz Onboard Clock is the default clock in your LabVIEW
 FPGA project. This clock can be used as a top-level clock for running your LabVIEW
 FPGA VI. The top-level clock on an FPGA target determines the execution time of the
 individual functions and VIs on the FPGA VI block diagram. If you change the
 frequency of the top-level clock, you also change the execution speed of functions
 on the block diagram and the execution rate of the FPGA VI.

#### PXIe_Clk100

PXIe_Clk100 can be used as a source for running your LabVIEW
 FPGA VI.

#### 300
 MHz Clock

The 300 MHz Clock can be used as a source for running your
 LabVIEW FPGA VI. Refer to the FPGA Base Clock Properties Dialog Box topic of the
 *LabVIEW FPGA Module Help* for more information about configuring
 base clocks on your FPGA target.

#### DRAM Clock

LabVIEW FPGA Module Help

Note

<!--NI_TOPIC bundle=understand-flexrio-integrated-io path=pxi-express-fpga-module-functions.html language=enus -->
## TOPIC 00009: PXI Express FPGA Module Functions Supported by FlexRIO Integrated I/O Devices

- bundle_id: `understand-flexrio-integrated-io`
- source_path: `pxi-express-fpga-module-functions.html`
- source_url: https://docs-be.ni.com/bundle/understand-flexrio-integrated-io/raw/resource/enus/pxi-express-fpga-module-functions.html
- document_id: `understand-flexrio-integrated-io`
- page_type: `leaf`
- content_type: `reference`
- source_description: Your FlexRIO Integrated I/O device supports the following LabVIEW FPGA functions: Arbitration Determines which object can access the resource if multiple objects request access at the same time. Configure the arbitration settings for the channels of this device in the FPGA I/O Properties dialog box

### PXI Express FPGA Module Functions Supported
 by FlexRIO Integrated I/O Devices

Your FlexRIO Integrated I/O device supports the following LabVIEW FPGA functions:

#### Arbitration

Determines which object can access the resource if multiple
 objects request access at the same time. Configure the arbitration settings for the
 channels of this device in the FPGA I/O Properties dialog box
 for the FPGA I/O item you are using.

#### FPGA Base
 Clocks

Refer to the FPGA Target Properties Dialog Box topic in the LabVIEW
 FPGA Help for more information about configuring base clocks.

#### Single-Cycle Timed Loop

Enables implementation of multiple clock domains
 in an FPGA VI.

#### Peer-to-Peer Streaming

Enables peer-to-peer data streaming. Use LabVIEW
 FPGA to configure your FlexRIO with Integrated I/O device to set up a peer-to-peer
 streaming session.

#### FlexRIO
 Peer-to-Peer Resource Availability

Enables Peer to Peer Reader and Peer to
 Peer Writer streams. The following table lists the stream types available for
 FlexRIO PXI Express devices.

| FIFO Type | Description |
| --- | --- |
| DMA input | Reads data into the FIFO from the VI. |
| DMA output | Writes data from the FIFO into the VI. |
| P2P Writer | Writes data to the peer-to-peer reader device. |
| P2P Reader | Reads data from the peer-to-peer writer device. |

<!--NI_TOPIC bundle=understand-flexrio-integrated-io path=pxi-pxie-fpga-io-items.html language=enus -->
## TOPIC 00010: PXI/PXIe FPGA I/O Items

- bundle_id: `understand-flexrio-integrated-io`
- source_path: `pxi-pxie-fpga-io-items.html`
- source_url: https://docs-be.ni.com/bundle/understand-flexrio-integrated-io/raw/resource/enus/pxi-pxie-fpga-io-items.html
- document_id: `understand-flexrio-integrated-io`
- page_type: `leaf`
- content_type: `reference`
- source_description: 1 FPGA I/O Node You can use an FPGA I/O Node, configured for reading and writing, with your FlexRIO Integrated I/O device. The FPGA I/O Node is located on the FPGA I/O Functions palette and performs specific FPGA I/O operations on your FPGA target. You can select the following PXI/PXI Express FPGA I

### PXI/PXIe FPGA I/O Items

Figure 1.

[IMAGE alt='image' src='GUID-0DDF3D0F-C0A5-401D-93CF-0DDDDDEEBCC5-a5.gif']

You can use an FPGA I/O Node, configured for reading and writing, with your FlexRIO Integrated
 I/O device. The FPGA I/O Node is located on the FPGA I/O
 Functions palette and performs specific FPGA I/O operations on your
 FPGA target.

You can select the following PXI/PXI Express FPGA I/O items for the FlexRIO with Integrated
 I/O devices.

| FPGA I/O Item | Description |
| --- | --- |
| PXI_Clk10 | Controls the 10 MHz clock on the PXI backplane. You can use this clock to synchronize multiple PXI modules. Use an FPGA I/O Node configured for reading across this channel. |

| Terminal | Description |
| --- | --- |
| PXIe_DStarB | Controls the differential star trigger that creates connections between a PXI Express system timing module and a peripheral device. PXIe_DStarB distributes trigger signals from the system timing slot to the peripherals (input). Use an FPGA I/O Node configured for reading to access this channel. |
| PXIe_DStarC | Controls the differential star trigger that creates connections between a PXI Express system timing module and a peripheral device. PXIe_DStarC sends trigger or clock signals from the peripherals to the system timing slot (output). Use an FPGA I/O Node configured for writing to access this channel. |
| PXIe_Sync100 | Controls the reference signal that is synchronous to the rising edge of PXIe_CLK100. Use PXIe_Sync100 to synchronize multiple modules in a PXI Express system. Use an FPGA I/O Node configured for reading to access this channel. |

<!--NI_TOPIC bundle=understand-flexrio-integrated-io path=pxie-5745-socketed-clip.html language=enus -->
## TOPIC 00011: PXIe-5745 Socketed CLIP Signals

- bundle_id: `understand-flexrio-integrated-io`
- source_path: `pxie-5745-socketed-clip.html`
- source_url: https://docs-be.ni.com/bundle/understand-flexrio-integrated-io/raw/resource/enus/pxie-5745-socketed-clip.html
- document_id: `understand-flexrio-integrated-io`
- page_type: `leaf`
- content_type: `reference`
- source_description: The PXIe-5745 CLIP provides access to two AC-coupled 12-bit 3.2 GS/s analog input channels and eight bidirectional DIO channels. CLIP Signal NameDirectionData TypeDescriptionData ClockFrom CLIPBooleanFPGA clock used to sample analog input data.Data Clock 2xFrom CLIPBooleanFPGA clock that samples ana

### PXIe-5745 Socketed CLIP Signals

| CLIP Signal Name | Direction | Data Type | Description |
| --- | --- | --- | --- |
| Data Clock | From CLIP | Boolean | FPGA clock used to sample analog input data. |
| Data Clock 2x | From CLIP | Boolean | FPGA clock that samples analog input data at twice the rate of Data Clock. |
| AO Ready for Input | From CLIP | Boolean | Indicates whether the AO link is ready for data. |
| AO 0 Data N | To CLIP | fixed-point <±12,1> | Sends analog output samples through the AO 0 front panel connector. |
| AO 0 Data N-1 | To CLIP | fixed-point <±12,1> | Sends analog output samples through the AO 0 front panel connector. |
| AO 0 Data N-2 | To CLIP | fixed-point <±12,1> | Sends analog output samples through the AO 0 front panel connector. |
| AO 0 Data N-3 | To CLIP | fixed-point <±12,1> | Sends analog output samples through the AO 0 front panel connector. |
| AO 0 Data N-4 | To CLIP | fixed-point <±12,1> | Sends analog output samples through the AO 0 front panel connector. |
| AO 0 Data N-5 | To CLIP | fixed-point <±12,1> | Sends analog output samples through the AO 0 front panel connector. |
| AO 0 Data N-6 | To CLIP | fixed-point <±12,1> | Sends analog output samples through the AO 0 front panel connector. |
| AO 0 Data N-7 | To CLIP | fixed-point <±12,1> | Sends analog output samples through the AO 0 front panel connector. |
| AO 0 Data N-8 | To CLIP | fixed-point <±12,1> | Sends analog output samples through the AO 0 front panel connector. |
| AO 0 Data N-9 | To CLIP | fixed-point <±12,1> | Sends analog output samples through the AO 0 front panel connector. |
| AO 0 Data N-10 | To CLIP | fixed-point <±12,1> | Sends analog output samples through the AO 0 front panel connector. |
| AO 0 Data N-11 | To CLIP | fixed-point <±12,1> | Sends analog output samples through the AO 0 front panel connector. |
| AO 0 Data N-12 | To CLIP | fixed-point <±12,1> | Sends analog output samples through the AO 0 front panel connector. |
| AO 0 Data N-13 | To CLIP | fixed-point <±12,1> | Sends analog output samples through the AO 0 front panel connector. |
| AO 0 Data N-14 | To CLIP | fixed-point <±12,1> | Sends analog output samples through the AO 0 front panel connector. |
| AO 0 Data N-15 | To CLIP | fixed-point <±12,1> | Sends analog output samples through the AO 0 front panel connector. |
| Ao 1 Data N | To CLIP | fixed-point <±12,1> | Sends analog output samples through the AO 1 front panel connector. |
| AO 1 Data N-1 | To CLIP | fixed-point <±12,1> | Sends analog output samples through the AO 1 front panel connector. |
| AO 1 Data N-2 | To CLIP | fixed-point <±12,1> | Sends analog output samples through the AO 1 front panel connector. |
| AO 1 Data N-3 | To CLIP | fixed-point <±12,1> | Sends analog output samples through the AO 1 front panel connector. |
| AO 1 Data N-4 | To CLIP | fixed-point <±12,1> | Sends analog output samples through the AO 1 front panel connector. |
| AO 1 Data N-5 | To CLIP | fixed-point <±12,1> | Sends analog output samples through the AO 1 front panel connector. |
| AO 1 Data N-6 | To CLIP | fixed-point <±12,1> | Sends analog output samples through the AO 1 front panel connector. |
| AO 1 Data N-7 | To CLIP | fixed-point <±12,1> | Sends analog output samples through the AO 1 front panel connector. |
| AO 1 Data N-8 | To CLIP | fixed-point <±12,1> | Sends analog output samples through the AO 1 front panel connector. |
| AO 1 Data N-9 | To CLIP | fixed-point <±12,1> | Sends analog output samples through the AO 1 front panel connector. |
| AO 1 Data N-10 | To CLIP | fixed-point <±12,1> | Sends analog output samples through the AO 1 front panel connector. |
| AO 1 Data N-11 | To CLIP | fixed-point <±12,1> | Sends analog output samples through the AO 1 front panel connector. |
| AO 1 Data N-12 | To CLIP | fixed-point <±12,1> | Sends analog output samples through the AO 1 front panel connector. |
| AO 1 Data N-13 | To CLIP | fixed-point <±12,1> | Sends analog output samples through the AO 1 front panel connector. |
| AO 1 Data N-14 | To CLIP | fixed-point <±12,1> | Sends analog output samples through the AO 1 front panel connector. |
| AO 1 Data N-15 | To CLIP | fixed-point <±12,1> | Sends analog output samples through the AO 1 front panel connector. |
| IO Error | From CLIP | I32 | Returns IO module errors, to be reported by the driver. |
| IO Ready | From CLIP | Boolean | Indicates successful configuration of the IO module devices with the current clocking mode settings. |

Parent topic:

Socketed Component-Level IP (CLIP) by Module Name

<!--NI_TOPIC bundle=understand-flexrio-integrated-io path=pxie-5763-socketed-clip.html language=enus -->
## TOPIC 00012: PXIe-5763 Socketed CLIP Signals

- bundle_id: `understand-flexrio-integrated-io`
- source_path: `pxie-5763-socketed-clip.html`
- source_url: https://docs-be.ni.com/bundle/understand-flexrio-integrated-io/raw/resource/enus/pxie-5763-socketed-clip.html
- document_id: `understand-flexrio-integrated-io`
- page_type: `leaf`
- content_type: `reference`
- source_description: The PXIe-5763 CLIP provides access to four AC-coupled and DC-coupled 16-bit 500 MS/s analog input channels and eight bidirectional DIO channels. CLIP Signal NameDirectionData TypeDescriptionData ClockFrom CLIPBooleanFPGA clock used to sample analog input data.Data Clock 2xFrom CLIPBooleanFPGA clock

### PXIe-5763 Socketed CLIP Signals

| CLIP Signal Name | Direction | Data Type | Description |
| --- | --- | --- | --- |
| Data Clock | From CLIP | Boolean | FPGA clock used to sample analog input data. |
| Data Clock 2x | From CLIP | Boolean | FPGA clock that samples analog input data at twice the rate of Data Clock. |
| AI 0 Data N | From CLIP | fixed-point <±16,1> | Returns analog input data through the AI 0 front panel connector. Each sample is a left-justified I16 data type. |
| AI 0 Data N-1 | From CLIP | fixed-point <±16,1> | Returns analog input data through the AI 0 front panel connector. Each sample is a left-justified I16 data type. |
| AI 0 Data N-2 | From CLIP | fixed-point <±16,1> | Returns analog input data through the AI 0 front panel connector. Each sample is a left-justified I16 data type. |
| AI 0 Data N-3 | From CLIP | fixed-point <±16,1> | Returns analog input data through the AI 0 front panel connector. Each sample is a left-justified I16 data type. |
| AI 1 Data N | From CLIP | fixed-point <±16,1> | Returns analog input data through the AI 1 front panel connector. Each sample is a left-justified I16 data type. |
| AI 1 Data N-1 | From CLIP | fixed-point <±16,1> | Returns analog input data through the AI 1 front panel connector. Each sample is a left-justified I16 data type. |
| AI 1 Data N-2 | From CLIP | fixed-point <±16,1> | Returns analog input data through the AI 1 front panel connector. Each sample is a left-justified I16 data type. |
| AI 1 Data N-3 | From CLIP | fixed-point <±16,1> | Returns analog input data through the AI 1 front panel connector. Each sample is a left-justified I16 data type. |
| AI 2 Data N | From CLIP | fixed-point <±16,1> | Returns analog input data through the AI 2 front panel connector. Each sample is a left-justified I16 data type. |
| AI 2 Data N-1 | From CLIP | fixed-point <±16,1> | Returns analog input data through the AI 2 front panel connector. Each sample is a left-justified I16 data type. |
| AI 2 Data N-2 | From CLIP | fixed-point <±16,1> | Returns analog input data through the AI 2 front panel connector. Each sample is a left-justified I16 data type. |
| AI 2 Data N-3 | From CLIP | fixed-point <±16,1> | Returns analog input data through the AI 2 front panel connector. Each sample is a left-justified I16 data type. |
| AI 3 Data N | From CLIP | fixed-point <±16,1> | Returns analog input data through the AI 3 front panel connector. Each sample is a left-justified I16 data type. |
| AI 3 Data N-1 | From CLIP | fixed-point <±16,1> | Returns analog input data through the AI 3 front panel connector. Each sample is a left-justified I16 data type. |
| AI 3 Data N-2 | From CLIP | fixed-point <±16,1> | Returns analog input data through the AI 3 front panel connector. Each sample is a left-justified I16 data type. |
| AI 3 Data N-3 | From CLIP | fixed-point <±16,1> | Returns analog input data through the AI 3 front panel connector. Each sample is a left-justified I16 data type. |

Parent topic:

Socketed Component-Level IP (CLIP) by Module Name

<!--NI_TOPIC bundle=understand-flexrio-integrated-io path=pxie-5764-socketed-clip.html language=enus -->
## TOPIC 00013: PXIe-5764 Socketed CLIP Signals

- bundle_id: `understand-flexrio-integrated-io`
- source_path: `pxie-5764-socketed-clip.html`
- source_url: https://docs-be.ni.com/bundle/understand-flexrio-integrated-io/raw/resource/enus/pxie-5764-socketed-clip.html
- document_id: `understand-flexrio-integrated-io`
- page_type: `leaf`
- content_type: `reference`
- source_description: The PXIe-5764 CLIP provides access to four AC-coupled and DC-coupled 14-bit 1 GS/s analog input channels and eight bidirectional DIO channels. CLIP Signal NameDirectionData TypeDescriptionData ClockFrom CLIPBooleanFPGA clock used to sample analog input data.Data Clock 2xFrom CLIPBooleanFPGA clock th

### PXIe-5764 Socketed CLIP Signals

| CLIP Signal Name | Direction | Data Type | Description |
| --- | --- | --- | --- |
| Data Clock | From CLIP | Boolean | FPGA clock used to sample analog input data. |
| Data Clock 2x | From CLIP | Boolean | FPGA clock that samples analog input data at twice the rate of Data Clock. |
| AI 0 Data N | From CLIP | fixed-point <±16,1> | Returns analog input data through the AI 0 front panel connector. Each sample is a left-justified I16 data type. |
| AI 0 Data N-1 | From CLIP | fixed-point <±16,1> | Returns analog input data through the AI 0 front panel connector. Each sample is a left-justified I16 data type. |
| AI 0 Data N-2 | From CLIP | fixed-point <±16,1> | Returns analog input data through the AI 0 front panel connector. Each sample is a left-justified I16 data type. |
| AI 0 Data N-3 | From CLIP | fixed-point <±16,1> | Returns analog input data through the AI 0 front panel connector. Each sample is a left-justified I16 data type. |
| AI 0 Data N-4 | From CLIP | fixed-point <±16,1> | Returns analog input data through the AI 0 front panel connector. Each sample is a left-justified I16 data type. |
| AI 0 Data N-5 | From CLIP | fixed-point <±16,1> | Returns analog input data through the AI 0 front panel connector. Each sample is a left-justified I16 data type. |
| AI 0 Data N-6 | From CLIP | fixed-point <±16,1> | Returns analog input data through the AI 0 front panel connector. Each sample is a left-justified I16 data type. |
| AI 0 Data N-7 | From CLIP | fixed-point <±16,1> | Returns analog input data through the AI 0 front panel connector. Each sample is a left-justified I16 data type. |
| AI 1 Data N | From CLIP | fixed-point <±16,1> | Returns analog input data through the AI 1 front panel connector. Each sample is a left-justified I16 data type. |
| AI 1 Data N-1 | From CLIP | fixed-point <±16,1> | Returns analog input data through the AI 1 front panel connector. Each sample is a left-justified I16 data type. |
| AI 1 Data N-2 | From CLIP | fixed-point <±16,1> | Returns analog input data through the AI 1 front panel connector. Each sample is a left-justified I16 data type. |
| AI 1 Data N-3 | From CLIP | fixed-point <±16,1> | Returns analog input data through the AI 1 front panel connector. Each sample is a left-justified I16 data type. |
| AI 1 Data N-4 | From CLIP | fixed-point <±16,1> | Returns analog input data through the AI 1 front panel connector. Each sample is a left-justified I16 data type. |
| AI 1 Data N-5 | From CLIP | fixed-point <±16,1> | Returns analog input data through the AI 1 front panel connector. Each sample is a left-justified I16 data type. |
| AI 1 Data N-6 | From CLIP | fixed-point <±16,1> | Returns analog input data through the AI 1 front panel connector. Each sample is a left-justified I16 data type. |
| AI 1 Data N-7 | From CLIP | fixed-point <±16,1> | Returns analog input data through the AI 1 front panel connector. Each sample is a left-justified I16 data type. |
| AI 2 Data N | From CLIP | fixed-point <±16,1> | Returns analog input data through the AI 2 front panel connector. Each sample is a left-justified I16 data type |
| AI 2 Data N-1 | From CLIP | fixed-point <±16,1> | Returns analog input data through the AI 2 front panel connector. Each sample is a left-justified I16 data type |
| AI 2 Data N-2 | From CLIP | fixed-point <±16,1> | Returns analog input data through the AI 2 front panel connector. Each sample is a left-justified I16 data type |
| AI 2 Data N-3 | From CLIP | fixed-point <±16,1> | Returns analog input data through the AI 2 front panel connector. Each sample is a left-justified I16 data type |
| AI 2 Data N-4 | From CLIP | fixed-point <±16,1> | Returns analog input data through the AI 2 front panel connector. Each sample is a left-justified I16 data type |
| AI 2 Data N-5 | From CLIP | fixed-point <±16,1> | Returns analog input data through the AI 2 front panel connector. Each sample is a left-justified I16 data type |
| AI 2 Data N-6 | From CLIP | fixed-point <±16,1> | Returns analog input data through the AI 2 front panel connector. Each sample is a left-justified I16 data type |
| AI 2 Data N-7 | From CLIP | fixed-point <±16,1> | Returns analog input data through the AI 2 front panel connector. Each sample is a left-justified I16 data type |
| AI 3 Data N | From CLIP | fixed-point <±16,1> | Returns analog input data through the AI 3 front panel connector. Each sample is a left-justified I16 data type |
| AI 3 Data N-1 | From CLIP | fixed-point <±16,1> | Returns analog input data through the AI 3 front panel connector. Each sample is a left-justified I16 data type |
| AI 3 Data N-2 | From CLIP | fixed-point <±16,1> | Returns analog input data through the AI 3 front panel connector. Each sample is a left-justified I16 data type |
| AI 3 Data N-3 | From CLIP | fixed-point <±16,1> | Returns analog input data through the AI 3 front panel connector. Each sample is a left-justified I16 data type |
| AI 3 Data N-4 | From CLIP | fixed-point <±16,1> | Returns analog input data through the AI 3 front panel connector. Each sample is a left-justified I16 data type |
| AI 3 Data N-5 | From CLIP | fixed-point <±16,1> | Returns analog input data through the AI 3 front panel connector. Each sample is a left-justified I16 data type |
| AI 3 Data N-6 | From CLIP | fixed-point <±16,1> | Returns analog input data through the AI 3 front panel connector. Each sample is a left-justified I16 data type |
| AI 3 Data N-7 | From CLIP | fixed-point <±16,1> | Returns analog input data through the AI 3 front panel connector. Each sample is a left-justified I16 data type |

Parent topic:

Socketed Component-Level IP (CLIP) by Module Name

<!--NI_TOPIC bundle=understand-flexrio-integrated-io path=pxie-5774-socketed-clip.html language=enus -->
## TOPIC 00014: PXIe-5774 Socketed CLIP Signals

- bundle_id: `understand-flexrio-integrated-io`
- source_path: `pxie-5774-socketed-clip.html`
- source_url: https://docs-be.ni.com/bundle/understand-flexrio-integrated-io/raw/resource/enus/pxie-5774-socketed-clip.html
- document_id: `understand-flexrio-integrated-io`
- page_type: `leaf`
- content_type: `reference`
- source_description: The PXIe-5774 CLIP provides access to two DC-coupled 12-bit 6.4 GS/s analog input channels and eight bidirectional DIO channels. CLIP Signal Name Direction Data Type Description Data Clock From CLIP Boolean FPGA clock used to sample analog input data. Data Clock 2x From CLIP Boolean FPGA clock that

### PXIe-5774 Socketed CLIP Signals

6.4 GS/s

| CLIP Signal Name | Direction | Data Type | Description |
| --- | --- | --- | --- |
| Data Clock | From CLIP | Boolean | FPGA clock used to sample analog input data. |
| Data Clock 2x | From CLIP | Boolean | FPGA clock that samples analog input data at twice the rate of Data Clock. |
| AI Data Valid | From CLIP | Boolean | Indicates whether AI sample data is vaild. |
| AI 0 Data N | From CLIP | fixed-point <±12,1> | Returns analog input data through the AI 0 front panel connector. |
| AI 0 Data N-1 | From CLIP | fixed-point <±12,1> | Returns analog input data through the AI 0 front panel connector. |
| AI 0 Data N-2 | From CLIP | fixed-point <±12,1> | Returns analog input data through the AI 0 front panel connector. |
| AI 0 Data N-3 | From CLIP | fixed-point <±12,1> | Returns analog input data through the AI 0 front panel connector. |
| AI 0 Data N-4 | From CLIP | fixed-point <±12,1> | Returns analog input data through the AI 0 front panel connector. |
| AI 0 Data N-5 | From CLIP | fixed-point <±12,1> | Returns analog input data through the AI 0 front panel connector. |
| AI 0 Data N-6 | From CLIP | fixed-point <±12,1> | Returns analog input data through the AI 0 front panel connector. |
| AI 0 Data N-7 | From CLIP | fixed-point <±12,1> | Returns analog input data through the AI 0 front panel connector. |
| AI 0 Data N-8 | From CLIP | fixed-point <±12,1> | Returns analog input data through the AI 0 front panel connector. |
| AI 0 Data N-9 | From CLIP | fixed-point <±12,1> | Returns analog input data through the AI 0 front panel connector. |
| AI 0 Data N-10 | From CLIP | fixed-point <±12,1> | Returns analog input data through the AI 0 front panel connector. |
| AI 0 Data N-11 | From CLIP | fixed-point <±12,1> | Returns analog input data through the AI 0 front panel connector. |
| AI 0 Data N-12 | From CLIP | fixed-point <±12,1> | Returns analog input data through the AI 0 front panel connector. |
| AI 0 Data N-13 | From CLIP | fixed-point <±12,1> | Returns analog input data through the AI 0 front panel connector. |
| AI 0 Data N-14 | From CLIP | fixed-point <±12,1> | Returns analog input data through the AI 0 front panel connector. |
| AI 0 Data N-15 | From CLIP | fixed-point <±12,1> | Returns analog input data through the AI 0 front panel connector. |
| AI 1 Data N | From CLIP | fixed-point <±12,1> | Returns analog input data through the AI 1 front panel connector. |
| AI 1 Data N-1 | From CLIP | fixed-point <±12,1> | Returns analog input data through the AI 1 front panel connector. |
| AI 1 Data N-2 | From CLIP | fixed-point <±12,1> | Returns analog input data through the AI 1 front panel connector. |
| AI 1 Data N-3 | From CLIP | fixed-point <±12,1> | Returns analog input data through the AI 1 front panel connector. |
| AI 1 Data N-4 | From CLIP | fixed-point <±12,1> | Returns analog input data through the AI 1 front panel connector. |
| AI 1 Data N-5 | From CLIP | fixed-point <±12,1> | Returns analog input data through the AI 1 front panel connector. |
| AI 1 Data N-6 | From CLIP | fixed-point <±12,1> | Returns analog input data through the AI 1 front panel connector. |
| AI 1 Data N-7 | From CLIP | fixed-point <±12,1> | Returns analog input data through the AI 1 front panel connector. |
| AI 1 Data N-8 | From CLIP | fixed-point <±12,1> | Returns analog input data through the AI 1 front panel connector. |
| AI 1 Data N-9 | From CLIP | fixed-point <±12,1> | Returns analog input data through the AI 1 front panel connector. |
| AI 1 Data N-10 | From CLIP | fixed-point <±12,1> | Returns analog input data through the AI 1 front panel connector. |
| AI 1 Data N-11 | From CLIP | fixed-point <±12,1> | Returns analog input data through the AI 1 front panel connector. |
| AI 1 Data N-12 | From CLIP | fixed-point <±12,1> | Returns analog input data through the AI 1 front panel connector. |
| AI 1 Data N-13 | From CLIP | fixed-point <±12,1> | Returns analog input data through the AI 1 front panel connector. |
| AI 1 Data N-14 | From CLIP | fixed-point <±12,1> | Returns analog input data through the AI 1 front panel connector. |
| AI 1 Data N-15 | From CLIP | fixed-point <±12,1> | Returns analog input data through the AI 1 front panel connector. |
| IO Error | From CLIP | I32 | Returns IO module errors, to be reported by the driver. |
| IO Ready | From CLIP | Boolean | Indicates successful configuration of the IO module devices with the current clocking mode settings. |
| TriggerIn | From CLIP | Boolean | Returns state of TRIG IN port on front panel. |
| TriggerOut | To CLIP | Boolean | Sets state of TRIG OUT port on front panel. |
| TdcExpandedPulseSample1 | From CLIP | Boolean | Reserved for future use |
| TdcExpandedPulseSample2 | From CLIP | Boolean | Reserved for future use |

Parent topic:

Socketed Component-Level IP (CLIP) by Module Name

<!--NI_TOPIC bundle=understand-flexrio-integrated-io path=pxie-5775-socketed-clip.html language=enus -->
## TOPIC 00015: PXIe-5775 Socketed CLIP Signals

- bundle_id: `understand-flexrio-integrated-io`
- source_path: `pxie-5775-socketed-clip.html`
- source_url: https://docs-be.ni.com/bundle/understand-flexrio-integrated-io/raw/resource/enus/pxie-5775-socketed-clip.html
- document_id: `understand-flexrio-integrated-io`
- page_type: `leaf`
- content_type: `reference`
- source_description: The PXIe-5775 CLIP provides access to two AC-coupled 12-bit 3.2 GS/s analog input channels and eight bidirectional DIO channels. CLIP Signal NameDirectionData TypeDescriptionData ClockFrom CLIPBooleanFPGA clock used to sample analog input data.Data Clock 2xFrom CLIPBooleanFPGA clock that samples ana

### PXIe-5775 Socketed CLIP Signals

| CLIP Signal Name | Direction | Data Type | Description |
| --- | --- | --- | --- |
| Data Clock | From CLIP | Boolean | FPGA clock used to sample analog input data. |
| Data Clock 2x | From CLIP | Boolean | FPGA clock that samples analog input data at twice the rate of Data Clock. |
| AI Data Valid | From CLIP | Boolean | Indicates whether AI sample data is vaild. |
| AI 0 Data N | From CLIP | fixed-point <±12,1> | Returns analog input data through the AI 0 front panel connector. |
| AI 0 Data N-1 | From CLIP | fixed-point <±12,1> | Returns analog input data through the AI 0 front panel connector. |
| AI 0 Data N-2 | From CLIP | fixed-point <±12,1> | Returns analog input data through the AI 0 front panel connector. |
| AI 0 Data N-3 | From CLIP | fixed-point <±12,1> | Returns analog input data through the AI 0 front panel connector. |
| AI 0 Data N-4 | From CLIP | fixed-point <±12,1> | Returns analog input data through the AI 0 front panel connector. |
| AI 0 Data N-5 | From CLIP | fixed-point <±12,1> | Returns analog input data through the AI 0 front panel connector. |
| AI 0 Data N-6 | From CLIP | fixed-point <±12,1> | Returns analog input data through the AI 0 front panel connector. |
| AI 0 Data N-7 | From CLIP | fixed-point <±12,1> | Returns analog input data through the AI 0 front panel connector. |
| AI 0 Data N-8 | From CLIP | fixed-point <±12,1> | Returns analog input data through the AI 0 front panel connector. |
| AI 0 Data N-9 | From CLIP | fixed-point <±12,1> | Returns analog input data through the AI 0 front panel connector. |
| AI 0 Data N-10 | From CLIP | fixed-point <±12,1> | Returns analog input data through the AI 0 front panel connector. |
| AI 0 Data N-11 | From CLIP | fixed-point <±12,1> | Returns analog input data through the AI 0 front panel connector. |
| AI 0 Data N-12 | From CLIP | fixed-point <±12,1> | Returns analog input data through the AI 0 front panel connector. |
| AI 0 Data N-13 | From CLIP | fixed-point <±12,1> | Returns analog input data through the AI 0 front panel connector. |
| AI 0 Data N-14 | From CLIP | fixed-point <±12,1> | Returns analog input data through the AI 0 front panel connector. |
| AI 0 Data N-15 | From CLIP | fixed-point <±12,1> | Returns analog input data through the AI 0 front panel connector. |
| AI 1 Data N | From CLIP | fixed-point <±12,1> | Returns analog input data through the AI 1 front panel connector. |
| AI 1 Data N-1 | From CLIP | fixed-point <±12,1> | Returns analog input data through the AI 1 front panel connector. |
| AI 1 Data N-2 | From CLIP | fixed-point <±12,1> | Returns analog input data through the AI 1 front panel connector. |
| AI 1 Data N-3 | From CLIP | fixed-point <±12,1> | Returns analog input data through the AI 1 front panel connector. |
| AI 1 Data N-4 | From CLIP | fixed-point <±12,1> | Returns analog input data through the AI 1 front panel connector. |
| AI 1 Data N-5 | From CLIP | fixed-point <±12,1> | Returns analog input data through the AI 1 front panel connector. |
| AI 1 Data N-6 | From CLIP | fixed-point <±12,1> | Returns analog input data through the AI 1 front panel connector. |
| AI 1 Data N-7 | From CLIP | fixed-point <±12,1> | Returns analog input data through the AI 1 front panel connector. |
| AI 1 Data N-8 | From CLIP | fixed-point <±12,1> | Returns analog input data through the AI 1 front panel connector. |
| AI 1 Data N-9 | From CLIP | fixed-point <±12,1> | Returns analog input data through the AI 1 front panel connector. |
| AI 1 Data N-10 | From CLIP | fixed-point <±12,1> | Returns analog input data through the AI 1 front panel connector. |
| AI 1 Data N-11 | From CLIP | fixed-point <±12,1> | Returns analog input data through the AI 1 front panel connector. |
| AI 1 Data N-12 | From CLIP | fixed-point <±12,1> | Returns analog input data through the AI 1 front panel connector. |
| AI 1 Data N-13 | From CLIP | fixed-point <±12,1> | Returns analog input data through the AI 1 front panel connector. |
| AI 1 Data N-14 | From CLIP | fixed-point <±12,1> | Returns analog input data through the AI 1 front panel connector. |
| AI 1 Data N-15 | From CLIP | fixed-point <±12,1> | Returns analog input data through the AI 1 front panel connector. |
| IO Error | From CLIP | I32 | Returns IO module errors, to be reported by the driver. |
| IO Ready | From CLIP | Boolean | Indicates successful configuration of the IO module devices with the current clocking mode settings. |

Parent topic:

Socketed Component-Level IP (CLIP) by Module Name

<!--NI_TOPIC bundle=understand-flexrio-integrated-io path=pxie-5785-socketed-clip.html language=enus -->
## TOPIC 00016: PXIe-5785 Socketed CLIP Signals

- bundle_id: `understand-flexrio-integrated-io`
- source_path: `pxie-5785-socketed-clip.html`
- source_url: https://docs-be.ni.com/bundle/understand-flexrio-integrated-io/raw/resource/enus/pxie-5785-socketed-clip.html
- document_id: `understand-flexrio-integrated-io`
- page_type: `leaf`
- content_type: `reference`
- source_description: The PXIe-5785 CLIP provides access to two AC-coupled 12-bit 3.2 GS/s analog input channels, two AC-coupled 12 bit 3.2 GS/s analog output channels, and eight bidirectional DIO channels. CLIP Signal NameDirectionData TypeDescriptionData ClockFrom CLIPBooleanFPGA clock used to sample analog input data.

### PXIe-5785 Socketed CLIP Signals

| CLIP Signal Name | Direction | Data Type | Description |
| --- | --- | --- | --- |
| Data Clock | From CLIP | Boolean | FPGA clock used to sample analog input data. |
| Data Clock 2x | From CLIP | Boolean | FPGA clock that samples analog input data at twice the rate of Data Clock. |
| AI Data Valid | From CLIP | Boolean | Indicates whether AI sample data is vaild. |
| AI 0 Data N | From CLIP | fixed-point <±12,1> | Returns analog input data through the AI 0 front panel connector. |
| AI 0 Data N-1 | From CLIP | fixed-point <±12,1> | Returns analog input data through the AI 0 front panel connector. |
| AI 0 Data N-2 | From CLIP | fixed-point <±12,1> | Returns analog input data through the AI 0 front panel connector. |
| AI 0 Data N-3 | From CLIP | fixed-point <±12,1> | Returns analog input data through the AI 0 front panel connector. |
| AI 0 Data N-4 | From CLIP | fixed-point <±12,1> | Returns analog input data through the AI 0 front panel connector. |
| AI 0 Data N-5 | From CLIP | fixed-point <±12,1> | Returns analog input data through the AI 0 front panel connector. |
| AI 0 Data N-6 | From CLIP | fixed-point <±12,1> | Returns analog input data through the AI 0 front panel connector. |
| AI 0 Data N-7 | From CLIP | fixed-point <±12,1> | Returns analog input data through the AI 0 front panel connector. |
| AI 0 Data N-8 | From CLIP | fixed-point <±12,1> | Returns analog input data through the AI 0 front panel connector. |
| AI 0 Data N-9 | From CLIP | fixed-point <±12,1> | Returns analog input data through the AI 0 front panel connector. |
| AI 0 Data N-10 | From CLIP | fixed-point <±12,1> | Returns analog input data through the AI 0 front panel connector. |
| AI 0 Data N-11 | From CLIP | fixed-point <±12,1> | Returns analog input data through the AI 0 front panel connector. |
| AI 0 Data N-12 | From CLIP | fixed-point <±12,1> | Returns analog input data through the AI 0 front panel connector. |
| AI 0 Data N-13 | From CLIP | fixed-point <±12,1> | Returns analog input data through the AI 0 front panel connector. |
| AI 0 Data N-14 | From CLIP | fixed-point <±12,1> | Returns analog input data through the AI 0 front panel connector. |
| AI 0 Data N-15 | From CLIP | fixed-point <±12,1> | Returns analog input data through the AI 0 front panel connector. |
| AI 1 Data N | From CLIP | fixed-point <±12,1> | Returns analog input data through the AI 1 front panel connector. |
| AI 1 Data N-1 | From CLIP | fixed-point <±12,1> | Returns analog input data through the AI 1 front panel connector. |
| AI 1 Data N-2 | From CLIP | fixed-point <±12,1> | Returns analog input data through the AI 1 front panel connector. |
| AI 1 Data N-3 | From CLIP | fixed-point <±12,1> | Returns analog input data through the AI 1 front panel connector. |
| AI 1 Data N-4 | From CLIP | fixed-point <±12,1> | Returns analog input data through the AI 1 front panel connector. |
| AI 1 Data N-5 | From CLIP | fixed-point <±12,1> | Returns analog input data through the AI 1 front panel connector. |
| AI 1 Data N-6 | From CLIP | fixed-point <±12,1> | Returns analog input data through the AI 1 front panel connector. |
| AI 1 Data N-7 | From CLIP | fixed-point <±12,1> | Returns analog input data through the AI 1 front panel connector. |
| AI 1 Data N-8 | From CLIP | fixed-point <±12,1> | Returns analog input data through the AI 1 front panel connector. |
| AI 1 Data N-9 | From CLIP | fixed-point <±12,1> | Returns analog input data through the AI 1 front panel connector. |
| AI 1 Data N-10 | From CLIP | fixed-point <±12,1> | Returns analog input data through the AI 1 front panel connector. |
| AI 1 Data N-11 | From CLIP | fixed-point <±12,1> | Returns analog input data through the AI 1 front panel connector. |
| AI 1 Data N-12 | From CLIP | fixed-point <±12,1> | Returns analog input data through the AI 1 front panel connector. |
| AI 1 Data N-13 | From CLIP | fixed-point <±12,1> | Returns analog input data through the AI 1 front panel connector. |
| AI 1 Data N-14 | From CLIP | fixed-point <±12,1> | Returns analog input data through the AI 1 front panel connector. |
| AI 1 Data N-15 | From CLIP | fixed-point <±12,1> | Returns analog input data through the AI 1 front panel connector. |
| AO Ready for Input | From CLIP | Boolean | Indicates whether the AO link is ready for data. |
| AO 0 Data N | To CLIP | fixed-point <±12,1> | Sends anaolg output samples through the AO 0 front panel connector. |
| AO 0 Data N-1 | To CLIP | fixed-point <±12,1> | Sends anaolg output samples through the AO 0 front panel connector. |
| AO 0 Data N-2 | To CLIP | fixed-point <±12,1> | Sends anaolg output samples through the AO 0 front panel connector. |
| AO 0 Data N-3 | To CLIP | fixed-point <±12,1> | Sends anaolg output samples through the AO 0 front panel connector. |
| AO 0 Data N-4 | To CLIP | fixed-point <±12,1> | Sends anaolg output samples through the AO 0 front panel connector. |
| AO 0 Data N-5 | To CLIP | fixed-point <±12,1> | Sends anaolg output samples through the AO 0 front panel connector. |
| AO 0 Data N-6 | To CLIP | fixed-point <±12,1> | Sends anaolg output samples through the AO 0 front panel connector. |
| AO 0 Data N-7 | To CLIP | fixed-point <±12,1> | Sends anaolg output samples through the AO 0 front panel connector. |
| AO 0 Data N-8 | To CLIP | fixed-point <±12,1> | Sends anaolg output samples through the AO 0 front panel connector. |
| AO 0 Data N-9 | To CLIP | fixed-point <±12,1> | Sends anaolg output samples through the AO 0 front panel connector. |
| AO 0 Data N-10 | To CLIP | fixed-point <±12,1> | Sends anaolg output samples through the AO 0 front panel connector. |
| AO 0 Data N-11 | To CLIP | fixed-point <±12,1> | Sends anaolg output samples through the AO 0 front panel connector. |
| AO 0 Data N-12 | To CLIP | fixed-point <±12,1> | Sends anaolg output samples through the AO 0 front panel connector. |
| AO 0 Data N-13 | To CLIP | fixed-point <±12,1> | Sends anaolg output samples through the AO 0 front panel connector. |
| AO 0 Data N-14 | To CLIP | fixed-point <±12,1> | Sends anaolg output samples through the AO 0 front panel connector. |
| AO 0 Data N-15 | To CLIP | fixed-point <±12,1> | Sends anaolg output samples through the AO 0 front panel connector. |
| AO 1 Data N | To CLIP | fixed-point <±12,1> | Sends anaolg output samples through the AO 1 front panel connector. |
| AO 1 Data N-1 | To CLIP | fixed-point <±12,1> | Sends anaolg output samples through the AO 1 front panel connector. |
| AO 1 Data N-2 | To CLIP | fixed-point <±12,1> | Sends anaolg output samples through the AO 1 front panel connector. |
| AO 1 Data N-3 | To CLIP | fixed-point <±12,1> | Sends anaolg output samples through the AO 1 front panel connector. |
| AO 1 Data N-4 | To CLIP | fixed-point <±12,1> | Sends anaolg output samples through the AO 1 front panel connector. |
| AO 1 Data N-5 | To CLIP | fixed-point <±12,1> | Sends anaolg output samples through the AO 1 front panel connector. |
| AO 1 Data N-6 | To CLIP | fixed-point <±12,1> | Sends anaolg output samples through the AO 1 front panel connector. |
| AO 1 Data N-7 | To CLIP | fixed-point <±12,1> | Sends anaolg output samples through the AO 1 front panel connector. |
| AO 1 Data N-8 | To CLIP | fixed-point <±12,1> | Sends anaolg output samples through the AO 1 front panel connector. |
| AO 1 Data N-9 | To CLIP | fixed-point <±12,1> | Sends anaolg output samples through the AO 1 front panel connector. |
| AO 1 Data N-10 | To CLIP | fixed-point <±12,1> | Sends anaolg output samples through the AO 1 front panel connector. |
| AO 1 Data N-11 | To CLIP | fixed-point <±12,1> | Sends anaolg output samples through the AO 1 front panel connector. |
| AO 1 Data N-12 | To CLIP | fixed-point <±12,1> | Sends anaolg output samples through the AO 1 front panel connector. |
| AO 1 Data N-13 | To CLIP | fixed-point <±12,1> | Sends anaolg output samples through the AO 1 front panel connector. |
| AO 1 Data N-14 | To CLIP | fixed-point <±12,1> | Sends anaolg output samples through the AO 1 front panel connector. |
| AO 1 Data N-15 | To CLIP | fixed-point <±12,1> | Sends anaolg output samples through the AO 1 front panel connector. |
| IO Error | From CLIP | I32 | Returns IO module errors, to be reported by the driver. |
| IO Ready | From CLIP | Boolean | Indicates successful configuration of the IO module devices with the current clocking mode settings. |

Parent topic:

Socketed Component-Level IP (CLIP) by Module Name

<!--NI_TOPIC bundle=understand-flexrio-integrated-io path=reset-conditions.html language=enus -->
## TOPIC 00017: Power On, Download, and Reset Conditions

- bundle_id: `understand-flexrio-integrated-io`
- source_path: `reset-conditions.html`
- source_url: https://docs-be.ni.com/bundle/understand-flexrio-integrated-io/raw/resource/enus/reset-conditions.html
- document_id: `understand-flexrio-integrated-io`
- page_type: `leaf`
- content_type: `concept`
- source_description: Your FlexRIO with Integrated I/O device applies default conditions after powering on the device, restarting the device, or downloading a new FPGA VI to the device. Find the default conditions for your module listed below. PXIe-5763, PXIe-5764, PXIe-5775 ADC resets to its default operating mode. Cloc

### Power On, Download, and Reset
 Conditions

Your FlexRIO with Integrated I/O device applies default conditions after powering on the
 device, restarting the device, or downloading a new FPGA VI to the device. Find the
 default conditions for your module listed below.

#### PXIe-5763, PXIe-5764, PXIe-5775

- ADC resets to its default operating mode.
- Clocking is reset to the internal clock and backplane reference.
- Phase DAC value resets to minimum.

#### PXIe-5745

- DAC resets to its default operating mode: 3.2 GS/s dual-channel, inverse sinc filter
 disabled
- Clocking is reset to the internal clock and backplane reference.
- Phase DAC value resets to minimum.

#### PXIe-5785

- ADC resets to its default operating mode: 3.2 GS/s dual-channel
- DAC resets to its default operating mode: 3.2 GS/s dual-channel, inverse sinc filter
 disabled
- Clocking is reset to the internal clock and backplane reference.
- Phase DAC value resets to minimum.

<!--NI_TOPIC bundle=understand-flexrio-integrated-io path=signal-trigger-routing.html language=enus -->
## TOPIC 00018: Signal and Trigger Routing

- bundle_id: `understand-flexrio-integrated-io`
- source_path: `signal-trigger-routing.html`
- source_url: https://docs-be.ni.com/bundle/understand-flexrio-integrated-io/raw/resource/enus/signal-trigger-routing.html
- document_id: `understand-flexrio-integrated-io`
- page_type: `leaf`
- content_type: `concept`
- source_description: Enter a short description of your concept here (optional). FlexRIO devices with integrated I/O can send and receive signals through the front panel connectors and the PXI trigger bus. The front panel connectors provide connectivity for the input and output signals and for the control lines that send

### Signal and Trigger Routing

Enter a short description of your concept here (optional).

FlexRIO devices with integrated I/O can send and receive signals through the front panel
 connectors and the PXI trigger bus. The front panel connectors provide connectivity for
 the input and output signals and for the control lines that send and receive clocks,
 triggers, and events. You can use the PXI trigger bus to send and receive events and
 triggers.

#### PXI Trigger Lines

FlexRIO devices with integrated I/O support sharing signals with other devices via the PXI
 trigger bus. Host software connects a logical device terminal to a specific PXI Trigger line
 or to a terminal on another device. An FPGA I/O Node can then read or write the logical
 signal from the FPGA diagram. FlexRIO devices with integrated I/O provide 32 logical sources
 (Source0 through Source31) that can drive signals on the PXI trigger bus, and 32 logical
 destinations (Destination0 through Destination31) that can receive signals from the PXI
 trigger bus. Use FPGA I/O nodes to write to and read from these sources and destinations.
 These logical sources and destinations are not connected to the PXI trigger bus until host
 software creates an appropriate route. You can create a route by using
 niFlexRIO_RouteSignal or by providing a terminal name as a routing
 property.

#### Terminal Names and Aliasing

A terminal
 name is a unique identifier that refers to a physical terminal in your system. To
 guarantee the uniqueness of a terminal name across multiple devices, terminal names
 begin with a forward slash, followed by the name of the device as configured in MAX,
 such as Dev1. A forward slash and the name of the terminal, such as PFI1, follow the
 device identifier. For example, the fully qualified terminal name for PFI1 on Dev1
 is /Dev1/PFI1.

Each of the routing matrix's 32 Source signals and 32
 Destination signals can be assigned an alias by renaming the I/O item in the LabVIEW
 FPGA Project. These aliases become valid terminal names once the bitfile has been
 opened on the device, and can be used wherever a terminal name is
 expected.

Related information:

- niFlexRIO_RouteSignal

<!--NI_TOPIC bundle=understand-flexrio-integrated-io path=time-digital-converter.html language=enus -->
## TOPIC 00019: Time-to-Digital Converter

- bundle_id: `understand-flexrio-integrated-io`
- source_path: `time-digital-converter.html`
- source_url: https://docs-be.ni.com/bundle/understand-flexrio-integrated-io/raw/resource/enus/time-digital-converter.html
- document_id: `understand-flexrio-integrated-io`
- page_type: `leaf`
- content_type: `reference`
- source_description: The FlexRIO Integrated I/O devices have a Time-to-Digital Converter (TDC) subsystem that allows the device to measure time between an event asserted in the Sample Clock domain and an event asserted on the PXIe_Clk100 domain. This measurement may be useful for evaluating the relative timing between s

### Time-to-Digital Converter

[IMAGE alt='image' src='GUID-4E1E6D38-870B-4136-9843-EEE10DADC11B-a5.gif']

<!--NI_TOPIC bundle=understand-flexrio-integrated-io path=viewing-fpga-target-vi-dependencies.html language=enus -->
## TOPIC 00020: Viewing FPGA Target VI Dependencies

- bundle_id: `understand-flexrio-integrated-io`
- source_path: `viewing-fpga-target-vi-dependencies.html`
- source_url: https://docs-be.ni.com/bundle/understand-flexrio-integrated-io/raw/resource/enus/viewing-fpga-target-vi-dependencies.html
- document_id: `understand-flexrio-integrated-io`
- page_type: `leaf`
- content_type: `task`
- source_description: Right-click Dependencies. Select Refresh from the shortcut menu. Refer to Managing Dependencies in LabVIEW Projects in the LabVIEW Help for more information about using dependencies.

### Viewing FPGA Target VI Dependencies

1. Right-click Dependencies.
2. Select Refresh from the shortcut menu.

LabVIEW Help
