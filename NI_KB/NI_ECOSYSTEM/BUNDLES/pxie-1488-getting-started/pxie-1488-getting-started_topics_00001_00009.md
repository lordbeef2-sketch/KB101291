# NI DOCUMENT BUNDLE: pxie-1488-getting-started

<!--NI_BUNDLE_CHUNK bundle=pxie-1488-getting-started start=1 end=9 -->
<!--NI_TOPIC bundle=pxie-1488-getting-started path=access-examples.html language=enus -->
## TOPIC 00001: Accessing FlexRIO with Integrated I/O Examples

- bundle_id: `pxie-1488-getting-started`
- source_path: `access-examples.html`
- source_url: https://docs-be.ni.com/bundle/pxie-1488-getting-started/raw/resource/enus/access-examples.html
- document_id: `pxie-1488-getting-started`
- page_type: `leaf`
- content_type: `task`
- source_description: The FlexRIO driver includes several example applications for LabVIEW. These examples serve as interactive tools, programming models, and as building blocks in your own applications. To access all FlexRIO with Integrated I/O getting started examples, complete the following steps. In LabVIEW, click He

Accessing FlexRIO with Integrated I/O
 Examples

Note

1. In LabVIEW, click Help»Find Examples.
2. In the NI Example Finder window that opens, click Hardware Input and Output»FlexRIO»Integrated IO»Getting Started.
3. Double click Getting Started with FlexRIO Integrated IO.vi. 
 The FlexRIO with Integrated IO Project Creator window opens.
4. Select the example that corresponds to the name of your FlexRIO module. The
 Description window includes a short description of the
 getting started example for your device. Rename the project, select a location
 for the project, and click OK. 
 The Project Explorer window for your new project
 opens.

Online examples are also available to demonstrate FlexRIO basics, such as using DRAM,
 acquiring data, and performing high throughput streaming. To access these examples, search
 FlexRIO examples in the Search the community
 field at *NI Example Programs*. For tutorial guidance on FlexRIO examples, access
 NI-maintained GitHub<sup>TM</sup> content at *PXIe-148X Programming Examples
 Explained*.

Related information:

- NI Example Programs
- PXIe-148X Programming Examples Explained

<!--NI_TOPIC bundle=pxie-1488-getting-started path=block-diagrams.html language=enus -->
## TOPIC 00002: PXIe-1488 Block Diagrams

- bundle_id: `pxie-1488-getting-started`
- source_path: `block-diagrams.html`
- source_url: https://docs-be.ni.com/bundle/pxie-1488-getting-started/raw/resource/enus/block-diagrams.html
- document_id: `pxie-1488-getting-started`
- page_type: `leaf`
- content_type: `reference`
- source_description: PXIe-1488 Module Block Diagrams Deserializer Block Diagram Serializer Block Diagram SerDes Block Diagram FPGA Carrier Block Diagram PXIe-1488 FPGA Block Diagram

PXIe-1488 Block
 Diagrams

#### PXIe-1488
 Module Block Diagrams

Figure 12.

[IMAGE alt='PXIe-1488 Deserializer Block Diagram' src='GUID-C04C72B8-1C4D-4A66-B4ED-DDD7FB45B476-a5.svg']

Figure 13.

[IMAGE alt='PXIe-1488 Serializer Block Diagram' src='GUID-7B3C0585-1F8D-4138-9479-54DEAB18DF4E-a5.svg']

Figure 14.

[IMAGE alt='PXIe-1488 SerDes Block Diagram' src='GUID-55176E84-22BF-41A4-BFB2-C0462B5338EB-a5.svg']

#### FPGA Carrier Block Diagram

Figure 15.

PXIe-1488

[IMAGE alt='1378' src='GUID-C9642DF6-B2F0-4C83-A792-734238F5D37B-a5.svg']

<!--NI_TOPIC bundle=pxie-1488-getting-started path=clip.html language=enus -->
## TOPIC 00003: Component-Level Intellectual Property (CLIP)

- bundle_id: `pxie-1488-getting-started`
- source_path: `clip.html`
- source_url: https://docs-be.ni.com/bundle/pxie-1488-getting-started/raw/resource/enus/clip.html
- document_id: `pxie-1488-getting-started`
- page_type: `leaf`
- content_type: `concept`
- source_description: The LabVIEW FPGA Module includes component-level intellectual property (CLIP) for HDL IP integration. FlexRIO devices support two types of CLIP: user-defined and socketed. User-defined CLIP allows you to insert HDL IP into an FPGA target, enabling VHDL code to communicate directly with an FPGA VI. S

Component-Level Intellectual Property (CLIP)

The LabVIEW FPGA Module includes component-level intellectual property (CLIP) for HDL IP integration. FlexRIO devices support two types of CLIP: user-defined and socketed.

- User-defined CLIP allows you to insert HDL IP into an FPGA target, enabling VHDL code to communicate directly with an FPGA VI.
- Socketed CLIP provides the same IP integration of the user-defined CLIP, but it also allows the CLIP to communicate directly with circuitry external to the FPGA. Adapter module socketed CLIP allows your IP to communicate directly with both the FPGA VI and the external adapter module connector interface.

The PXIe-1488 ships with socketed CLIP items that add module I/O to the LabVIEW project.

<!--NI_TOPIC bundle=pxie-1488-getting-started path=common-flexrio-integrated-io-examples.html language=enus -->
## TOPIC 00004: Common FlexRIO with Integrated I/O Examples

- bundle_id: `pxie-1488-getting-started`
- source_path: `common-flexrio-integrated-io-examples.html`
- source_url: https://docs-be.ni.com/bundle/pxie-1488-getting-started/raw/resource/enus/common-flexrio-integrated-io-examples.html
- document_id: `pxie-1488-getting-started`
- page_type: `leaf`
- content_type: `reference`
- source_description: In addition to the examples within the FlexRIO with Integrated IO Project Creator, NI provides several examples that apply to all FlexRIO with Integrated I/O modules to help you perform common tasks. The following examples can be found in the NI Example Finder:Show All FlexRIO with Integrated IO Har

Common FlexRIO with Integrated I/O
 Examples

In addition to the examples within the FlexRIO with Integrated IO Project Creator, NI
 provides several examples that apply to all FlexRIO with Integrated I/O modules to help you
 perform common tasks.

- Show All FlexRIO with Integrated IO Hardware.vi queries and
 displays a set of hardware properties from all FlexRIO with Integrated I/O
 devices in a chassis.
- Vivado Export Getting Started Ultrascale.lvproj demonstrates how to export
 your LabVIEW FPGA project into Vivado in order to develop your FPGA design
 in the Vivado ADE.
- Read-Write Calibration Data.vi demonstrates how to read and
 write calibration data and metadata into the storage space of FlexRIO with
 Integrated I/O devices.

Parent topic:

Accessing FlexRIO with Integrated I/O Examples

<!--NI_TOPIC bundle=pxie-1488-getting-started path=components.html language=enus -->
## TOPIC 00005: Preparing the System Components

- bundle_id: `pxie-1488-getting-started`
- source_path: `components.html`
- source_url: https://docs-be.ni.com/bundle/pxie-1488-getting-started/raw/resource/enus/components.html
- document_id: `pxie-1488-getting-started`
- page_type: `leaf`
- content_type: `topic`
- source_description: Unpacking the Kit To prevent electrostatic discharge (ESD) from damaging the device, ground yourself using a grounding strap or by holding a grounded object, such as your computer chassis. Touch the antistatic package to a metal part of the computer chassis. Remove the device from the package and in

Preparing the System Components

#### Unpacking the Kit

Notice

1. Touch the antistatic package to a metal part of the computer chassis.
2. Remove the device from the package and inspect the device for loose components or any other sign of damage. 
 org.dita.html5/xsl/topic.xsl 455Notice Never touch the exposed pins of connectors.
 org.dita.html5/xsl/topic.xsl 455Note Do not install a device if it appears damaged in any way.
3. Unpack any other items and documentation from the kit.

Store the device in the antistatic package when the device is not in use.

##### Verifying the Kit Contents

Verify that the following items are included in the PXIe-1488 kit.

- PXIe-1488 Module
- Terminal blocks
- PXIe-1488 Safety, Environmental, and Regulatory
 Information

#### System Components

The PXIe-1488 is intended for use with the following
 system components.

##### Required System Components

- PXIe chassis with slot cooling capacity ≥58 W
- Camera or serial device (for Deserializer or SerDes modules)
- Electronic control unit (for Serializer or SerDes modules)
- PXI Express embedded controller or PC with MXI controller system

##### Optional System Components

- Power source (for Deserializer or SerDes modules)
- Power sink (for Serializer or SerDes modules)
- Copper power connector wire
- HFM Female Code Z to HFM Female Code Z Cable(s)
- HFM Female Code Z to FAKRA Female Code Z Cable(s)

Note

PXIe-1488

#### Verifying the System Requirements

To use the FlexRIO instrument driver, your system must meet certain requirements.

ni.com/docs

Related information:

- FlexRIO Release Notes

<!--NI_TOPIC bundle=pxie-1488-getting-started path=flexrio-documentation-resources.html language=enus -->
## TOPIC 00006: FlexRIO Documentation and Resources

- bundle_id: `pxie-1488-getting-started`
- source_path: `flexrio-documentation-resources.html`
- source_url: https://docs-be.ni.com/bundle/pxie-1488-getting-started/raw/resource/enus/flexrio-documentation-resources.html
- document_id: `pxie-1488-getting-started`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the following resources to find more information about the PXIe-1488. All product documentation can be found at ni.com/docs or in LabVIEW by clicking Help. FlexRIO Documentation and Resources Document Contents PXIe-1488 Getting Started Guide (this document) Installation instructions Basic progra

FlexRIO Documentation and Resources

Use the following resources to find more information about the PXIe-1488.

All product documentation can be found at [ni.com/docs](https://www.ni.com/docs/en-US/) or in LabVIEW by clicking
 Help.

| Document | Contents |
| --- | --- |
| PXIe-1488 Getting Started Guide (this document) | Installation instructions Basic programming instructions |
| PXIe-1488 Specifications | Operating environment requirements IO specifications Clocking specifications Physical and mechanical specifications |
| PXIe-1488 Safety, Environmental, and Regulatory Information | Safety and compliance information Environmental information |
| LabVIEW FPGA Module Help | Basic functionality of the FPGA module Instructions for developing and debugging custom hardware logic |
| FlexRIO Readme | Minimum system requirements Supported Application Development Environments (ADEs) Known issues and bug fixes Recent updates |
| FlexRIO Help | Hardware reference information Programming instructions I/O Component Level IP (CLIP) development information |
| LabVIEW Examples | Examples showing how to run FPGA VIs on your device How showing how to run host VIs on your device |
| FlexRIO product page | Product information Data sheets |
| PXIe-148X Programming Examples Explained | Detailed tutorials that are maintained by NI in GitHubTM for FlexRIO automotive vision modules |

Parent topic:

PXIe-1488 Getting Started

Related information:

- NI Example Programs
- PXIe-148X Programming Examples Explained

<!--NI_TOPIC bundle=pxie-1488-getting-started path=front-panels-connectors.html language=enus -->
## TOPIC 00007: PXIe-1488 Front Panel and Connector Diagrams

- bundle_id: `pxie-1488-getting-started`
- source_path: `front-panels-connectors.html`
- source_url: https://docs-be.ni.com/bundle/pxie-1488-getting-started/raw/resource/enus/front-panels-connectors.html
- document_id: `pxie-1488-getting-started`
- page_type: `leaf`
- content_type: `reference`
- source_description: Deserializer Connectors Deserializer Front Panel Deserializer Front Panel Connectors Signal Descriptions Signal Name Description FlexRIO Terminal Name SI 0 Serial input to internal deserializer SI0 SI 1 Serial input to internal deserializer SI1 SI 2 Serial input to internal deserializer SI2 SI 3 Ser

PXIe-1488 Front
 Panel and Connector Diagrams

#### Deserializer Connectors

Figure 6.

[IMAGE alt='PXIe-1488 Deserializer Front Panel' src='GUID-4C425002-D3F4-435F-93BD-E0C84060F534-a5.svg']

| Signal Name | Description | FlexRIO Terminal Name |
| --- | --- | --- |
| SI 0 | Serial input to internal deserializer | SI0 |
| SI 1 | Serial input to internal deserializer | SI1 |
| SI 2 | Serial input to internal deserializer | SI2 |
| SI 3 | Serial input to internal deserializer | SI3 |
| SI 4 | Serial input to internal deserializer | SI4 |
| SI 5 | Serial input to internal deserializer | SI5 |
| SI 6 | Serial input to internal deserializer | SI6 |
| SI 7 | Serial input to internal deserializer | SI7 |

Figure 7.

[IMAGE alt='1378' src='GUID-FC272454-C619-4C76-A5D9-577C3EA89DFF-a5.svg']

| Signal Pin | Description |
| --- | --- |
| 1 | Power supply for channel SI 0 |
| 2 | Power supply for channel SI 1 |
| 3 | Digital/chassis grounding |
| 4 | Digital/chassis grounding |
| 5 | Power supply for channel SI 2 |
| 6 | Power supply for channel SI 3 |
| 7 | Power supply for channel SI 4 |
| 8 | Power supply for channel SI 5 |
| 9 | Digital/chassis grounding |
| 10 | Digital/chassis grounding |
| 11 | Power supply for channel SI 6 |
| 12 | Power supply for channel SI 7 |

Related tasks:

- Cabling the PXIe-1488

#### Serializer Connectors

Figure 8.

[IMAGE alt='PXIe-1488 Serializer Front Panel' src='GUID-BC4EE37E-AD2E-48F1-B59E-EAF69494ED21-a5.svg']

| Signal Name | Description | FlexRIO Terminal Name |
| --- | --- | --- |
| SO 0 | Serial output from internal serializer | SO0 |
| SO 1 | Serial output from internal serializer | SO1 |
| SO 2 | Serial output from internal serializer | SO2 |
| SO 3 | Serial output from internal serializer | SO3 |
| SO 4 | Serial output from internal serializer | SO4 |
| SO 5 | Serial output from internal serializer | SO5 |
| SO 6 | Serial output from internal serializer | SO6 |
| SO 7 | Serial output from internal serializer | SO7 |

Figure 9.

[IMAGE alt='1378' src='GUID-FC272454-C619-4C76-A5D9-577C3EA89DFF-a5.svg']

| Signal Pin | Description |
| --- | --- |
| 1 | Power sink for channel SO 0 |
| 2 | Power sink for channel SO 1 |
| 3 | Digital/chassis grounding |
| 4 | Digital/chassis grounding |
| 5 | Power sink for channel SO 2 |
| 6 | Power sink for channel SO 3 |
| 7 | Power sink for channel SO 4 |
| 8 | Power sink for channel SO 5 |
| 9 | Digital/chassis grounding |
| 10 | Digital/chassis grounding |
| 11 | Power sink for channel SO 6 |
| 12 | Power sink for channel SO 7 |

#### SerDes Connectors

Figure 10.

[IMAGE alt='PXIe-1488 SerDes Front Panel' src='GUID-908A6A05-0F71-407E-9FD1-93228646866A-a5.svg']

| Signal Name | Description | FlexRIO Terminal Name |
| --- | --- | --- |
| SO 0 | Serial output from internal serializer | SO0 |
| SI 0 | Serial input to internal deserializer | SI0 |
| SO 1 | Serial output from internal serializer | SO1 |
| SI 1 | Serial input to internal deserializer | SI1 |
| SO 2 | Serial output from internal serializer | SO2 |
| SI 2 | Serial input to internal deserializer | SI2 |
| SO 3 | Serial output from internal serializer | SO3 |
| SI 3 | Serial input to internal deserializer | SI3 |

Figure 11.

[IMAGE alt='1378' src='GUID-FAD5E1A6-5C04-4A1C-869B-E68522F6D9C1-a5.svg']

| Signal Pin | Description |
| --- | --- |
| 1 | Power sink for channel SO 0 |
| 2 | Power supply for channel SI 0 |
| 3 | Digital/chassis grounding |
| 4 | Digital/chassis grounding |
| 5 | Power sink for channel SO 1 |
| 6 | Power supply for channel SI 1 |
| 7 | Power sink for channel SO 2 |
| 8 | Power supply for channel SI 2 |
| 9 | Digital/chassis grounding |
| 10 | Digital/chassis grounding |
| 11 | Power sink for channel SO 3 |
| 12 | Power supply for channel SI 3 |

Related tasks:

- Cabling the PXIe-1488

<!--NI_TOPIC bundle=pxie-1488-getting-started path=install.html language=enus -->
## TOPIC 00008: Installing and Connecting

- bundle_id: `pxie-1488-getting-started`
- source_path: `install.html`
- source_url: https://docs-be.ni.com/bundle/pxie-1488-getting-started/raw/resource/enus/install.html
- document_id: `pxie-1488-getting-started`
- page_type: `leaf`
- content_type: `topic`
- source_description: Installing the Software Download the following software from ni.com/downloads. Refer to Package Manager for more information about installing, removing, and upgrading NI software using Package Manager. Installation of all NI software also automatically installs Package Manager. LabVIEW LabVIEW FPGA

Installing and Connecting

#### Installing the Software

ni.com/downloads

Note

Package Manager

- LabVIEW
- LabVIEW FPGA Module
- FlexRIO

Related information:

- Installing, Updating, Repairing, and Removing NI Software

#### Installing the PXIe-1488

Notice

PXIe-1488

1. Ensure the AC power source is connected to the chassis before installing the module. 
 The AC power cord grounds the chassis and protects it from electrical damage while you install the module.
2. Power off the chassis.
3. Inspect the slot pins on the chassis backplane for any bends or damage prior to installation. Do not install a module if the backplane is damaged.
4. Remove the black plastic covers from all the captive screws on the module front panel.
5. Identify a supported slot in the chassis. The following figure shows the symbols that indicate the slot types. 
 Figure 1.Chassis Compatibility Symbols
 
 
[IMAGE alt='1378' src='GUID-B549F540-0A70-4664-AA95-FCB16C959D1E-a5.svg'] 

 PXI Express System Controller Slot
 PXI Peripheral Slot
 PXI Express Hybrid Peripheral Slot
 PXI Express System Timing Slot
 PXI Express Peripheral Slot 
 PXIe-1488 modules can be placed in PXI Express
 peripheral slots, PXI Express hybrid peripheral slots, or PXI Express system timing slots.
6. Touch any metal part of the chassis to discharge static electricity.
7. Ensure that the ejector handle is in the downward (unlatched) position. 
 Figure 2.Module Installation
 
 
[IMAGE alt='1378' src='GUID-56F154C8-7615-4922-BFB8-ABAD4D6D9424-a5.svg'] 

 Chassis
 Hardware Module
 Ejector Handle in Downward (Unlatched) Position
8. Place the module edges into the module guides at the top and bottom of the chassis. Slide the module into the slot until it is fully inserted.
9. Latch the module in place by pulling up on the ejector handle.
10. Secure the module front panel to the chassis using the front-panel mounting screws. 
 org.dita.html5/xsl/topic.xsl 455Note Tightening the top and bottom mounting screws increases mechanical stability and also electrically connects the front panel to the chassis, which can improve the signal quality and electromagnetic performance.
11. Cover all empty slots using either filler panels (standard or EMC) or slot
 blockers with filler panels, depending on your application. 
 org.dita.html5/xsl/topic.xsl 455Note For more information about installing slot
 blockers and filler panels, go to [ni.com/r/pxiblocker](http://www.ni.com/r/pxiblocker).
12. Power on the chassis.

#### Cabling the PXIe-1488

Complete the following steps to connect your PXIe-1488 to
 other system components.

1. Connect your chassis to a power source as described in the chassis getting started
 documentation.
2. Connect serial device(s) and ECU(s) as required for your application. 
 
 org.dita.html5/xsl/topic.xsl 455Note Serial output and serial input
 coaxial connectors on the PXIe-1488 are physically
 identical. They can be differentiated by their labels. Serial output connectors are
 labeled SO and serial input connectors are labeled SI.
 org.dita.html5/xsl/topic.xsl 455Notice Do not plug or unplug
 devices while power over coax is enabled on serial channels as this may damage your
 device. Always set the power over coax to disabled and wait for the power to be fully
 disabled before plugging and unplugging devices.
  - For Deserializer or SerDes modules, use a HFM cable to connect serial device(s) to
 the PXIe-1488 serial input (SI) connector(s).
  - For Serializer or SerDes modules, use a HFM cable to connect ECU(s) to the PXIe-1488 serial output (SO) connector(s).
3. Connect the terminal blocks included in your kit to the AUX power connectors on the PXIe-1488.
4. (Optional) Connect power sink(s) or power source(s) to the AUX power connectors
 as required for your application. 
 
 org.dita.html5/xsl/topic.xsl 455Note AUX power connector pins
 map to serial input and serial output connectors one to one.
  - For Deserializer or SerDes modules, use a copper conductor wire to connect a power
 source to the serial input channel's corresponding pin on the AUX power connector. This
 allows you to supply external power. If you do not connect an external power source,
 devices connected to PXIe-1488 can be powered by the
 chassis backplane.
  - For Serializer or SerDes modules, use a copper conductor wire to connect a power
 sink to the serial output channel's corresponding pin on the AUX power connector. This
 allows you to simulate an additional load.

Figure 3.

PXIe-1488

[IMAGE alt='1378' src='GUID-27C05029-C864-4AA3-BF62-066D4411F7D8-a5.svg']

1. PXIe-1488 Deserializer Module
2. Camera or Serial Device
3. Power Source
4. HFM Female Code Z to Serial Device Connector Cable
5. Power Connector Wire, Grounding
6. Power Connector Wire, Positively Charged

Figure 4.

PXIe-1488

[IMAGE alt='1378' src='GUID-5B714F65-D7CB-447D-8672-9D1F0E7ED5AA-a5.svg']

1. PXIe-1488 Serializer Module
2. Electronic Control Unit (ECU)
3. Power Sink
4. HFM Female Code Z to HFM Female Code Z Cable or HFM Female Code Z to FAKRA Female Code
 Z Cable, depending on the ECU connector type
5. Power Connector Wire, Grounding
6. Power Connector Wire, Positively Charged

Figure 5.

PXIe-1488

[IMAGE alt='1378' src='GUID-5C5E05AF-4361-4DA5-B514-59E45C642A42-a5.svg']

1. PXIe-1488 SerDes Module
2. Electronic Control Unit (ECU)
3. HFM Female Code Z to HFM Female Code Z Cable or HFM Female Code Z to FAKRA Female Code
 Z Cable, depending on the ECU connector type
4. Camera or Serial Device
5. Power Connector Wire, Positively Charged

Note

PXIe-1488

Related reference:

- Serializer Connectors

#### Verifying the Installation in MAX

Use Measurement & Automation Explorer (MAX) to configure your NI hardware.
 MAX informs other programs about which NI hardware products are in the system and how they
 are configured. MAX is automatically installed with FlexRIO.

1. Launch MAX.
2. In the configuration tree, expand Devices and
 Interfaces to see the list of installed NI hardware. 
 Installed modules appear under the name of their associated
 chassis.
3. Expand your Chassis tree item. 
 MAX lists all modules installed in the chassis. Your default names may vary. org.dita.html5/xsl/topic.xsl 455Note If you do not see your module listed,
 press <F5> to refresh the list of installed modules. If the module is still not
 listed, power off the system, ensure the module is correctly installed, and restart.
4. Record the identifier MAX assigns to the hardware. Use this identifier when
 programming the PXIe-1488.
5. Self-test the hardware by selecting the item in the configuration tree
 and clicking Self-Test in the MAX toolbar. 
 MAX self-test performs a basic verification of hardware resources.

<!--NI_TOPIC bundle=pxie-1488-getting-started path=intro.html language=enus -->
## TOPIC 00009: PXIe-1488 Getting Started

- bundle_id: `pxie-1488-getting-started`
- source_path: `intro.html`
- source_url: https://docs-be.ni.com/bundle/pxie-1488-getting-started/raw/resource/enus/intro.html
- document_id: `pxie-1488-getting-started`
- page_type: `leaf`
- content_type: `concept`
- source_description: The PXIe-1488 FlexRIO FPD-Link Interface Module provides a high-speed digital interface for using and testing modern advanced driver assistance systems (ADAS) and autonomous drive (AD) camera sensors and electronic control units (ECUs). The PXIe-1488 includes the following variants: PXIe-1488 FlexRI

PXIe-1488 Getting Started

The PXIe-1488
 FlexRIO FPD-Link Interface Module provides a high-speed digital interface for using and
 testing modern advanced driver assistance systems (ADAS) and autonomous drive (AD) camera
 sensors and electronic control units (ECUs).

The PXIe-1488 includes the following variants:

- PXIe-1488 FlexRIO FPD-Link IV Deserializer
- PXIe-1488 FlexRIO FPD-Link IV Serializer
- PXIe-1488 FlexRIO FPD-Link IV SerDes

Install and configure the PXIe-1488 to develop a hardware and
 driver setup that allows you to design and test your software application.

Note

PXIe-1488

PXIe-1488

© 2023 National Instruments Corporation. All rights reserved. Refer to the <National Instruments>\_Legal Information directory for information about NI copyright, patents, trademarks, warranties, product warnings, and export compliance.
