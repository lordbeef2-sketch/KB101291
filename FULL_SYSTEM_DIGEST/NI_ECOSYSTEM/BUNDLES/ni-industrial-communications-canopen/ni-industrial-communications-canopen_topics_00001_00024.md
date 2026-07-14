# NI DOCUMENT BUNDLE: ni-industrial-communications-canopen

<!--NI_BUNDLE_CHUNK bundle=ni-industrial-communications-canopen start=1 end=24 -->
<!--NI_TOPIC bundle=ni-industrial-communications-canopen path=basic-programming-model.html language=enus -->
## TOPIC 00001: Basic Programming Model

- bundle_id: `ni-industrial-communications-canopen`
- source_path: `basic-programming-model.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-canopen/raw/resource/enus/basic-programming-model.html
- document_id: `ni-industrial-communications-canopen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The basic programming model is a general guideline for creating and executing a typical LabVIEW application for CANopen. Creating the ApplicationThe first step of any CANopen application is creating an interface object. An interface object corresponds to a CAN port on a CANopen board. Use the CANope

### Basic Programming Model

The basic programming model is a general guideline for creating and executing a
 typical LabVIEW application for CANopen.

#### Creating the Application

The first step
 of any CANopen application is creating an interface object. An interface object
 corresponds to a CAN port on a CANopen board. Use the CANopen Interface
 Create VI to create interface objects. Use Measurement & Automation
 Explorer to view the mapping relationship between each interface name and specific
 hardware model.

CANopen Create

- Device-specific objects
- Bus-wide objects

For example, to use a process data object (PDO) for
 a specific device, create a PDO for this device. To use a PDO for another device,
 create another PDO. You can create up to 355 objects, maximum.

After creating
 objects for communication, you can implement the algorithm of the application. For
 more information about creating a LabVIEW application, refer to the *LabVIEW
 User Manual*.

#### Starting Devices and Objects

You must
 start devices and objects before executing the application.

To start devices,
 use network management (NMT) commands. LabVIEW automatically
 starts all objects when you start an application.

To start objects, use the
 proper instance of the CANopen Start VI.

#### Starting Devices

start remote node

CANopen NMT Write

start remote node

0

(Optional) Configuring Devices

CANopen
 SDO Write

CANopen SDO Batch
 Write

(Optional) Monitoring Objects

node guarding

heartbeat

CANopen Node Guarding Start

CANopen Heartbeat
 Start

#### Executing the Application

You may execute applications after the previous steps. Devices transmit and receive
 PDOs during the execution. Use the CANopen RPDO Write VI to transmit
 data to devices. Use the CANopen TPDO Read VI to read the data that
 devices send.

#### Stopping and Closing Objects

LabVIEW stops and closes all objects when the application terminates. You can also
 manually stop and close objects before the application terminates. Use the
 corresponding instance of the CANopen Stop VI to stop objects, such as
 PDOs, heartbeat objects, and node guarding objects. Use the corresponding instance
 of the CANopen Close VI to close objects.

If you close an object
 without stopping this object, the CANopen Close VI stops the object automatically
 and closes the object. If you stop an object without closing this object, LabVIEW
 closes this object when the application terminates.

Parent topic:

Configuring CANopen

Related concepts:

- Process Data Object
- Network Management
- Heartbeat Protocol and Node Guarding Protocol

<!--NI_TOPIC bundle=ni-industrial-communications-canopen path=cabling.html language=enus -->
## TOPIC 00002: Cabling

- bundle_id: `ni-industrial-communications-canopen`
- source_path: `cabling.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-canopen/raw/resource/enus/cabling.html
- document_id: `ni-industrial-communications-canopen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Cabling RequirementsCables must meet the physical medium requirements specified in ISO 11898, as shown in the following table. 11 ISO 11898 Cable Requirements Characteristic Value Impedance 108 Ω minimum 120 Ω nominal 132 Ω maximum Length-related resistance 70 mΩ /m nominal Specific line delay 5 ns/

### Cabling

#### Cabling Requirements

Cables must meet the
 physical medium requirements specified in ISO 11898, as shown in the following
 table.

| Characteristic | Value |
| --- | --- |
| Impedance | 108 Ω minimum 120 Ω nominal 132 Ω maximum |
| Length-related resistance | 70 mΩ /m nominal |
| Specific line delay | 5 ns/m nominal |

Belden cable (3084A) is suitable for most applications.

#### Cable Length

The cabling characteristics
 and desired bit transmission rate affect the allowable cable length. Detailed cable
 length recommendations are in the ISO 11898 and CiA DS 102 specifications. ISO 11898
 specifies 40 m total cable length with a maximum stub
 length of 0.3 m for a bit rate of 1 Mbps. The ISO 11898 specification says that
 significantly longer cable lengths may be allowed at lower bit rates, but each node
 should be analyzed for signal integrity problems.

#### Maximum Number of Devices

The maximum number of devices that you can
 connect to a CANopen port depends on the electrical characteristics of the devices
 on the network. If all of the devices on the network meet the CANopen
 specifications, 64 devices may be connected to the network.

#### Connectors

CANopen hardware has a 9-Pin D-Sub terminal connector.

Figure 1.

[IMAGE alt='9-Pin D-Sub Connector' src='GUID-6BC02CE2-AE9D-4650-95F6-79B9E4BB95E3-a5.gif']

| Signal Name | Description |
| --- | --- |
| NC | No connection. |
| CAN_L | CAN_L bus line. |
| V— | CAN reference ground. |
| NC | No connection. |
| (SHLD) | Optional CAN shield. |
| (COM) | Optional CAN reference ground. |
| CAN_H | CAN_H bus line. |
| NC | No connection. |
| (V+) | Also referred to as Ext_Vbat, this is an optional CAN power supply if bus power/external VBAT is required. |

Some CANopen devices may use a Combicon-style pluggable screw terminal
 connector. The 5-pin Combicon-style pluggable screw terminal follows the pinout
 required by the CANopen Specification. The following figure shows
 the pinout for this connector.

Figure 2.

[IMAGE alt='5-Pin Combicon Connector' src='GUID-110BD4E4-7DD1-4BEC-873E-197790D12B96-a5.gif']

1. V—
2. CAN_L
3. GND
4. CAN_H
5. V+

| Signal Name | Description |
| --- | --- |
| V— | CAN reference ground. |
| CAN_L | CAN_L bus line. |
| GND | Ground |
| CAN_H | CAN_H bus line. |
| (V+) | Also referred to as Ext_Vbat, this is an optional CAN power supply if bus power/external VBAT is required. |

#### Bus Power Requirements

The physical layer
 on the PXI and PCI CANopen interfaces is internally powered. You do not need to
 supply bus power. The COM pin serves as the reference ground for
 the bus signals.

The physical layer on C-Series NI-9881 requires external power supply of +9
 V to +30 V to operate. Connect the external
 power supply to the Vsup pin on the module. The COM pins are for reference
 ground.

#### Termination

The pair of signal wires
 (CAN_H and CAN_L) constitutes a transmission
 line. If the transmission line is not terminated, each signal change on the line
 causes reflections that may cause communication failures.

Because
 communication flows both ways on the CANopen bus, CANopen requires that both ends of
 the cable be terminated. However, this requirement does not mean that every device
 should have a termination resistor. If multiple devices are placed along the cable,
 only the devices on the ends of the cable should have termination
 resistors.

The termination resistors on a cable should match the nominal
 impedance of the cable. CANopen requires a cable with a nominal impedance of 120 Ω; therefore, a 120
 Ω resistor should be used at each end of the cable. Each termination
 resistor should be capable of dissipating at least 0.25
 W of power.

#### Cabling Examples

The following figure shows a cable connecting two CANopen devices.

Figure 3.

[IMAGE alt='Cable Connecting Two CANopen Devices' src='GUID-4D5EEABF-081F-4EC2-9696-0D0602E768B0-a5.gif']

The following figure shows where to install termination resistors in a system with
 more than two devices.

Figure 4.

[IMAGE alt='Termination Resistors Location' src='GUID-3F99475C-E412-4842-BA9A-58AD51C8D2C4-a5.gif']

Parent topic:

CANopen Hardware

<!--NI_TOPIC bundle=ni-industrial-communications-canopen path=canopen-hardware.html language=enus -->
## TOPIC 00003: CANopen Hardware

- bundle_id: `ni-industrial-communications-canopen`
- source_path: `canopen-hardware.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-canopen/raw/resource/enus/canopen-hardware.html
- document_id: `ni-industrial-communications-canopen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Supported Hardware Products NI-Industrial Communications for CANopen supports the following CANopen hardware. The CANopen products are fully compliant with the CANopen Specification. NI-9881 A C-Series CANopen module used for NI CompactRIO platform. This hardware allows you to use your CompactRIO ch

### CANopen Hardware

#### Supported Hardware Products

NI-Industrial Communications for
 CANopen
 supports the following CANopen hardware. The CANopen products are fully compliant
 with the *CANopen Specification*.

NI-9881

PCI-8531

PCI Local Bus Specification

PXI-8531

PXI Specification

CompactPCI Specification

#### Isolation

All NI CANopen products protect your equipment from being
 damaged by high-voltage spikes on the target bus. Bus ports on PXI and PCI CANopen
 products support channel-to-channel and channel-to-bus isolation, and are
 galvanically isolated up to 500 Vrms (5 s max withstand). Bus ports on C-Series CANopen
 products support channel-to-bus isolation, and are galvanically isolated up to 1000 Vrms (5 s max
 withstand).

#### Transceiver

All of the supported CANopen products use the NXP PCA82C251
 High-Speed CAN transceiver. The NXP PCA82C251 is fully compatible with the ISO 11898
 standard and supports all the CANopen baud rates (10
 kbps, 20 kbps, 50
 kbps, 125 kbps, 250 kbps, 500 kbps, 800 kbps, and 1 Mbps).

#### LED
 Indicator

NI CANopen boards include two LEDs to help you monitor hardware
 and bus status.

Note

The PCI-8351 and the PXI-8531 feature four LEDs on the front panel but only LED 1
 and LED 2 are currently active. LED 3 and LED 4 are reserved for future use.

LED 1

LED 2

The following table lists hardware status LED states.

| LED 1 Status Indicator | Hardware Status |
| --- | --- |
| (Off) | No application uses the CANopen hardware port. The CANopen port is disconnected from the CANopen network. |
| Solid Green | The CANopen hardware port is opened in a normal condition. |
| Blink Green | The CANopen hardware port is stopped. |

The following table lists error status LED states.

| LED 2 Status Indicator | Error Status |
| --- | --- |
| (Off) | No errors are detected. |
| Solid Red | CAN network bus is off. You can clear the bus off error physically and reopen the CANopen interface. |
| Blink Red | Error occurs when initializing the firmware. The hardware may be problematic. |

Related concepts:

- Cabling
- Troubleshooting CANopen Applications

Related information:

- PCI/PXI-8531 Specifications
- NI-9881 and sbRIO-9881 Specifications

<!--NI_TOPIC bundle=ni-industrial-communications-canopen path=canopen-object-dictionary.html language=enus -->
## TOPIC 00004: CANopen Object Dictionary

- bundle_id: `ni-industrial-communications-canopen`
- source_path: `canopen-object-dictionary.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-canopen/raw/resource/enus/canopen-object-dictionary.html
- document_id: `ni-industrial-communications-canopen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The CANopen object dictionary describes all communication objects of a device, including application data and configuration parameters. The core of a CANopen device is an object dictionary. The object dictionary contains a look-up table with a 16-bit index and an 8-bit sub-index. Each entry is a com

### CANopen Object Dictionary

The CANopen object dictionary describes all communication objects of a device,
 including application data and configuration parameters.

- The object dictionary contains a look-up table with a 16-bit index and an 8-bit sub-index.
- Each entry is a communication object.
- A communication object contains a variable of any type.

(EDS)

.ini

Note

The CANopen object dictionary contains the following common objects:

- [Device Profiles](device-profiles.html) The device profile defines the behavior and objects of a CANopen device.
- [Process Data Object](process-data-object.html) A process data object (PDO) provides access to application objects stored within a device.
- [Service Data Object](service-data-object.html) A service data object (SDO) allows a device to read from or write to the CANopen object dictionary.
- [Synchronization](synchronization.html) A synchronization (SYNC) object provides synchronous communication on a CANopen network.
- [Emergency](emergency.html) A CANopen device generates an emergency (EMCY) message when a device-internal error occurs.
- [Heartbeat Protocol and Node Guarding Protocol](heartbeat-and-node-guarding.html) Use the heartbeat protocol or the node guarding protocol to detect device failures on a CANopen network.
- [Network Management](network-management.html) Use the network management (NMT) service to control NMT states of CANopen devices.

Parent topic:

CANopen Protocol Overview

<!--NI_TOPIC bundle=ni-industrial-communications-canopen path=configuring-attributes-of-canopen-objects.html language=enus -->
## TOPIC 00005: Configuring Attributes of CANopen Objects

- bundle_id: `ni-industrial-communications-canopen`
- source_path: `configuring-attributes-of-canopen-objects.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-canopen/raw/resource/enus/configuring-attributes-of-canopen-objects.html
- document_id: `ni-industrial-communications-canopen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Create property nodes of attributes to configure a CANopen object. Before performing this procedure, create CANopen objects with the CANopen Create VI.To configure the attributes of the CANopen object, create a property node for each attribute. Complete the following steps to create a property node

### Configuring Attributes of CANopen Objects

Create property nodes of attributes to configure a CANopen object.

Before performing this procedure, create CANopen objects with the CANopen
 Create VI.

To configure the attributes of the CANopen object, create a property node for each attribute.

Complete the following steps to create a property node of an attribute.

1. Right-click a refnum terminal of an object to display the shortcut menu.
2. Browse to Create»Property for CANopen Object Class and
 select the attribute to configure. LabVIEW creates a property node for this
 attribute.
3. (Optional) Right-click the property node and select Change All To Write from the shortcut menu. This menu item is available for writable attributes only.

The following table lists all attributes of CANopen objects that you can configure.

| Object Name | Attribute Name | Data Type | Access | Description |
| --- | --- | --- | --- | --- |
| Interface | Baud rate | Enum | Read only | The baud rate of the CANopen interface. |
| TPDO | Node-ID | U8 | Read only | The node-ID of the device that sends the TPDO. |
| TPDO | COB-ID | U32 | Read/write | The COB-ID of the TPDO. |
| TPDO | Data size | U8 | Read/write | The size, in number of bytes, of the data contained in the TPDO. |
| TPDO | Buffer size | U16 | Read only | The maximum number of CANopen frames that the TPDO receive buffer saves. |
| TPDO | Auto start | Boolean | Read/write | The option that indicates whether the device starts the TPDO automatically in reading operations. |
| RPDO | Node-ID | U8 | Read only | The node-ID of the device that receives the RPDO. |
| RPDO | COB-ID | U32 | Read/write | The COB-ID of the RPDO. |
| RPDO | Data size | U8 | Read/write | The size, in number of bytes, of the data contained in the RPDO. |
| RPDO | Data padding | U8 | Read/write | The padding value of the RPDO. When you use the CANopen RPDO Write VI to write an array that is shorter than data size, this VI uses the data padding value to complement the rest data bytes. |
| RPDO | Inhibit time | U8 | Read/write | The minimum interval for event-driven PDO transmissions. |
| RPDO | Event time | U8 | Read/write | The maximum interval for event-driven PDO transmissions. |
| RPDO | Auto start | Boolean | Read/write | The option that indicates whether the device starts the RPDO automatically in writing operations. |
| SDO | Node-ID | U8 | Read only | The node-ID of the device that the SDO communicates with. |
| SDO | Server COB-ID | U32 | Read/write | The COB-ID of the SDO server. |
| SDO | Client COB-ID | U32 | Read/write | The COB-ID of the SDO client. |
| SYNC | COB-ID | U32 | Read/write | The COB-ID of the SYNC object. |
| SYNC | Counter overflow value | U8 | Read/write | The value of the synchronous counter overflow object. The valid range of counter overflow value is 0 and 2 to 240. |
| SYNC | Auto start | Boolean | Read/write | The option that indicates whether the device starts the SYNC object automatically in sending SYNC message operations. |
| Heartbeat | Node-ID | U8 | Read only | The node-ID of the producer device of the heartbeat object. |
| Heartbeat | COB-ID | U32 | Read/write | The COB-ID of the heartbeat message. |
| Heartbeat | Consumer time | U16 | Read/write | The maximum time, in milliseconds, between the transmission of two subsequent heartbeat messages. |
| Heartbeat | Factor | U8 | Read/write | The tolerance factor of consumer time. LabVIEW multiplies consumer time by factor and uses the product as the timeout of consumer devices. |
| Heartbeat | Auto start | Boolean | Read/write | The option that indicates whether the device starts the heartbeat object automatically in reading operations. |
| Node guarding | Node-ID | U8 | Read only | The node-ID of the device that the node guarding object monitors. |
| Node guarding | COB-ID | U32 | Read/write | The COB-ID of the node guarding message. |
| Node guarding | Guard time | U16 | Read/write | The time interval, in milliseconds, that the node guarding master sends requests to slave devices. |
| Node guarding | Life time factor | U8 | Read/write | An index that LabVIEW uses to calculate the timeout value for the device to respond. LabVIEW calculates the timeout value by multiplying guard time by life time factor. |
| Node guarding | Auto start | Boolean | Read/write | The option that indicates whether the device starts the node guarding object automatically in reading operations. |
| Emergency | Node-ID | U8 | Read only | The node-ID of the device of the EMCY object. |
| Emergency | COB-ID | U32 | Read/write | The COB-ID of the EMCY message. |
| Emergency | Buffer size | U16 | Read only | The maximum number of EMCY messages that the buffer saves. |
| Emergency | Auto start | Boolean | Read/write | The option that indicates whether the device starts the EMCY object automatically in reading operations. |
| CAN frame read | Buffer size | U16 | Read only | The maximum number of CAN frames that the buffer saves. |
| CAN frame read | Auto start | Boolean | Read/write | The option that indicates whether the device starts the CAN frame read object automatically in reading operations. |

Parent topic:

Configuring CANopen

Related concepts:

- Synchronization

Related information:

- CANopen Create VI

<!--NI_TOPIC bundle=ni-industrial-communications-canopen path=configuring-canopen.html language=enus -->
## TOPIC 00006: Configuring CANopen

- bundle_id: `ni-industrial-communications-canopen`
- source_path: `configuring-canopen.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-canopen/raw/resource/enus/configuring-canopen.html
- document_id: `ni-industrial-communications-canopen`
- page_type: `leaf`
- content_type: `concept`

### Configuring CANopen

- [Basic Programming Model](basic-programming-model.html) The basic programming model is a general guideline for creating and executing a typical LabVIEW application for CANopen.
- [Configuring Attributes of CANopen Objects](configuring-attributes-of-canopen-objects.html) Create property nodes of attributes to configure a CANopen object.
- [Creating Batch SDOs](creating-batch-sdos.html) A batch SDO is a group of service data objects (SDOs) that you can configure together.
- [Previewing and Validating Batch SDOs](previewing-and-validating-batch-sdos.html) You can preview and validate batch SDOs before deploying.
- [Troubleshooting CANopen Applications](troubleshooting-canopen-applications.html) Guidelines to troubleshoot common issues with CANopen applications.

<!--NI_TOPIC bundle=ni-industrial-communications-canopen path=creating-batch-sdos.html language=enus -->
## TOPIC 00007: Creating Batch SDOs

- bundle_id: `ni-industrial-communications-canopen`
- source_path: `creating-batch-sdos.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-canopen/raw/resource/enus/creating-batch-sdos.html
- document_id: `ni-industrial-communications-canopen`
- page_type: `leaf`
- content_type: `concept`
- source_description: A batch SDO is a group of service data objects (SDOs) that you can configure together. Complete the following steps to create a batch SDO: Right-click a target in the Project Explorer window and select New»CANopen Batch SDO from the shortcut menu. The Batch SDO General Settings dialog box appears. E

### Creating Batch SDOs

A batch SDO is a group of service data objects (SDOs) that you can configure together.

Complete the following steps to create a batch SDO:

1. Right-click a target in the Project Explorer window and select
 New»CANopen Batch SDO from
 the shortcut menu. The Batch SDO General
 Settings dialog box appears.
2. Enter a name for the batch SDO that you want to create in the Name text box.
3. (Optional) Specify an electronic data sheet (EDS) file in the EDS
 File field. EDS files are stored in the CANopen Object Dictionary.
4. Click the OK button to display the Batch SDO dialog
 box.
5. Select Object Dictionary from the Category list to
 display the Batch SDO - Object Dictionary page.
6. Select an object from the list and click the Add to Batch button to add this object to the Batch SDO list. You can also double-click a CANopen object to add this object to the Batch SDO list.
7. (Optional) Adjust the order of the object by using the Move Up and Move Down buttons.
8. (Optional) Preview and validate the batch SDO.
9. Click the OK button to close this dialog box and create the batch SDO.

CANopen SDO Batch Write

Note

CANopen SDO Batch Write

Project Explorer

To deploy a batch SDO on the localhost, enable the NI Scan Engine on the computer.

#### Enabling the NI Scan
 Engine

Complete the following steps to enable the NI Scan Engine.

1. In the Project Explorer window, right-click My
 Computer and select Properties from the shortcut menu
 to display the My Computer Properties dialog box.
2. In the My Computer Properties dialog box, select Scan
 Engine from the left pane to display the Scan Engine 
 page.
3. To enable the NI Scan Engine, enable the Start Scan Engine on
 Deploy checkbox.

Note

Parent topic:

Configuring CANopen

Related concepts:

- Service Data Object
- CANopen Object Dictionary

Related tasks:

- Previewing and Validating Batch SDOs

Related information:

- Batch SDO General Settings Dialog Box
- Batch SDO Dialog Box
- Batch SDO - Object Dictionary Page
- CANopen SDO Batch Write VI

<!--NI_TOPIC bundle=ni-industrial-communications-canopen path=device-profiles.html language=enus -->
## TOPIC 00008: Device Profiles

- bundle_id: `ni-industrial-communications-canopen`
- source_path: `device-profiles.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-canopen/raw/resource/enus/device-profiles.html
- document_id: `ni-industrial-communications-canopen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The device profile defines the behavior and objects of a CANopen device. Device manufacturers provide standard device profiles for each type of CANopen devices. The following table lists common device types and standard device profiles. 4 Common Device Types and Standard Device Profiles Device Type

### Device Profiles

The device profile defines the behavior and objects of a CANopen device.

Device manufacturers provide standard device profiles for each type of CANopen devices. The
 following table lists common device types and standard device profiles.

| Device Type | Standard Device Profile |
| --- | --- |
| Generic I/O Modules | CiA 401 |
| Drives and Motion Control | CiA 402 |
| Measuring Devices and Closed Loop Controllers | CiA 404 |
| IEC 61131-3 Programmable Devices | CiA 405 |
| Rotating and Linear Encoders | CiA 406 |
| Hydraulic Drives and Proportional Valves | CiA 408 |
| Inclinometers | CiA 410 |
| Medical Devices | CiA 412 |
| Truck Gateways | CiA 413 |
| Yarn Feeding Units | CiA 414 |
| Road Construction Machinery | CiA 415 |

You can configure device profiles or use customized device profiles to support additional objects in the *object dictionary*. Ensure CANopen devices support the following objects to use these devices:

Identity Object

Error Object

Parent topic:

CANopen Object Dictionary

<!--NI_TOPIC bundle=ni-industrial-communications-canopen path=emergency.html language=enus -->
## TOPIC 00009: Emergency

- bundle_id: `ni-industrial-communications-canopen`
- source_path: `emergency.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-canopen/raw/resource/enus/emergency.html
- document_id: `ni-industrial-communications-canopen`
- page_type: `leaf`
- content_type: `concept`
- source_description: A CANopen device generates an emergency (EMCY) message when a device-internal error occurs. The CANopen device reports the EMCY message only once. If no new errors occur on the device, the device does not report further EMCY messages.The CAN identifier of an EMCY is 80[h] plus a node-ID. An EMCY alw

### Emergency

A CANopen device generates an emergency (EMCY) message when a device-internal error
 occurs.

The CANopen device reports the EMCY message only once. If no new errors occur on the device, the
 device does not report further EMCY messages.

The CAN identifier of an EMCY is 80<sub>h</sub> plus a node-ID. An EMCY always contains 8 data
 bytes. The first 2 bytes are CANopen-specific error codes. The third byte contains an
 error register, and the remaining 5 bytes are manufacturer-specific error codes.

#### CANopen Error Codes

The CANopen protocol provides CANopen-specific error
 codes to indicate device-internal errors. Each error code indicates a general
 category of errors. Device manufacturers may provide detailed error codes and
 information for devices. The following table lists the CANopen-specific error codes
 and types.

| Error Code | Description |
| --- | --- |
| 0000h | Error reset or no error |
| 1000h | Generic error |
| 2000h | Current |
| 2100h | Current, CANopen device input side |
| 2200h | Current inside the CANopen device |
| 2300h | Current, CANopen device output side |
| 3000h | Voltage |
| 3100h | Mains voltage |
| 3200h | Voltage inside the CANopen device |
| 3300h | Output voltage |
| 4000h | Temperature |
| 4100h | Ambient temperature |
| 4200h | Device temperature |
| 5000h | CANopen device hardware |
| 6000h | CANopen device software |
| 6100h | Internal software |
| 6200h | User software |
| 6300h | Data set |
| 7000h | Additional modules |
| 8000h | Monitoring |
| 8100h | Communication |
| 8110h | CAN overrun (objects lost) |
| 8120h | CAN in error passive mode |
| 8130h | Life guard error or heartbeat error |
| 8140h | Recovered from bus off |
| 8150h | CAN-ID collision |
| 8200h | Protocol error |
| 8210h | PDO not processed due to length error |
| 8220h | PDO length exceeded |
| 8230h | DAM MPDO not processed, destination object not available |
| 9000h | External error |
| F000h | Additional functions |
| FF00h | Device specific |

#### Error Registers

An error register object
 is a bit field of 8 bits. This object reflects the internal error status of a
 device. Each bit indicates an error status. The index of the error register object
 is 1001<sub>h</sub> in the object dictionary.

The following table lists the
 error statuses of the bits.

| Bit | Error Status |
| --- | --- |
| 0 | Generic error |
| 1 | Current error |
| 2 | Voltage error |
| 3 | Temperature error |
| 4 | Communication error (overrun, error state) |
| 5 | Device profile specific error |
| 6 | Reserved (always 0) |
| 7 | Manufacturer-specific error |

When an error occurs, the device sets the generic error bit and the
 corresponding bit to 1<sub>b</sub>. For example, if a temperature error occurs, the
 device sets both bit 0 and bit 3 to 1<sub>b</sub>. The manufacturer-specific error
 field contains additional error information from manufacturers. Once you resolve all
 internal errors, the device sends an EMCY message with an error code of
 0000<sub>h</sub>.

Parent topic:

CANopen Object Dictionary

<!--NI_TOPIC bundle=ni-industrial-communications-canopen path=extended-support-changes.html language=enus -->
## TOPIC 00010: Updates and Changes for NI-Industrial Communications for CANopen Extended Support Versions

- bundle_id: `ni-industrial-communications-canopen`
- source_path: `extended-support-changes.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-canopen/raw/resource/enus/extended-support-changes.html
- document_id: `ni-industrial-communications-canopen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Browse updates and changes made in NI-Industrial Communications for CANopen versions on extended support. If you cannot find changes for your version, it might be a more recent version, documented as a new feature. Or, your version might not have included user-facing updates. You can find more infor

### Updates and Changes for NI-Industrial Communications for
 CANopen Extended Support Versions

Browse updates and changes made in NI-Industrial Communications for
 CANopen versions
 on extended support.

Note

Release Notes

#### NI-Industrial Communications for
 CANopen
 20.0 Changes

Learn about new features, behavior changes, and other updates in NI-Industrial Communications for
 CANopen 20.0.

- Added support for LabVIEW 2020 (32-bit).

#### NI-Industrial Communications for
 CANopen
 19.0 Changes

Learn about new features, behavior changes, and other updates in NI-Industrial Communications for
 CANopen 19.0.

- Added support for LabVIEW 2019 (32-bit).

<!--NI_TOPIC bundle=ni-industrial-communications-canopen path=getting-started-with-compactrio.html language=enus -->
## TOPIC 00011: Getting Started with CompactRIO

- bundle_id: `ni-industrial-communications-canopen`
- source_path: `getting-started-with-compactrio.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-canopen/raw/resource/enus/getting-started-with-compactrio.html
- document_id: `ni-industrial-communications-canopen`
- page_type: `leaf`
- content_type: `concept`
- source_description: When you use a C Series NI-Industrial Communications for CANopen module in a CompactRIO chassis, the NI-IndCom for CANopen features on the LabVIEW Real-Time Module are the same as other RT targets, such as PXI. The communication between the NI-IndCom for CANopen RT driver and the module does not exi

### Getting Started with CompactRIO

When you use a C Series NI-Industrial Communications for CANopen module in a CompactRIO
 chassis, the NI-IndCom for CANopen features on the LabVIEW Real-Time Module are the same
 as other RT targets, such as PXI. The communication between the NI-IndCom for CANopen RT
 driver and the module does not exist in the default FPGA VI that ships with CompactRIO.
 Prior to using NI-IndCom for CANopen features, you must use the LabVIEW FPGA Module to
 compile and run an FPGA VI that contains the required communication logic.

Complete the following steps to use a C Series NI-IndCom for CANopen module in a
 CompactRIO chassis from the out-of-box configuration.

#### Step 1. Install the Required Software

Install the required software to the host computer in the following
 order:

1. LabVIEW
2. LabVIEW Real-Time Module
3. LabVIEW FPGA Module
4. NI-RIO
5. NI-IndCom for CANopen

#### Step 2. Install NI-IndCom for CANopen to the
 CompactRIO RT Controller

Use MAX to locate your CompactRIO controller
 under Remote Systems in the left pane. Right-click the
 Software item and select Add/Remove
 Software to launch the installer. You can install the required
 components in the following two methods:

- NI-RIO with NI Scan Engine support —After selecting this
 item, the next page displays a list of add-ons. Scroll down to the bottom of the
 add-on list to check NI-IndCom for CANopen. If this selection is dimmed, refer
 to the explanation on the right pane to resolve the problem, or use custom
 installation.
- Custom software installation —Custom installation can be
 useful on controllers with small memory because this method enables you to avoid
 installation of unused components. Select the NI-IndCom for CANopen item. The
 installer selects the required dependencies, such as NI-RIO IO Scan.

#### Step 3. Add Modules to a
 LabVIEW Project

To compile an FPGA VI with the required communication logic, you must add NI-IndCom
 for CANopen modules to a LabVIEW project.

1. Add the controller to the LabVIEW project. If the controller is online, you can
 right-click on the project item and select New»Targets and
 Devices»Existing target or device , then select the controller
 under Real-Time CompactRIO . If the controller is offline,
 you can add the controller by selecting New target or
 device .
2. Select programming mode for the chassis. When you add the controller, a dialog
 box appears and asks you to select the programming mode for the chassis.
 Although NI-IndCom for CANopen uses the NI Scan Engine components, you must
 select LabVIEW FPGA Interface as the chassis mode. This
 configures the chassis to support compilation of an FPGA VI. Note If the Discover
 C Series Modules dialog box appears, select the
 Do Not Discover button and proceed to step 5.
3. Ignore errors for discovered NI-IndCom for CANopen modules. LabVIEW may report
 an error for NI-IndCom for CANopen modules, stating that LabVIEW FPGA is not
 supported. Do not change the chassis to Scan Interface
 mode . Ignore this error message and select
 Continue .
4. Add the FPGA target. Right-click the chassis item under the controller, and
 select New»FPGA Target .
5. Add the NI-IndCom for CANopen modules. Right-click the chassis item under the
 controller (not FPGA), and select New»C Series Modules»Existing
 target or device . Select the plus sign to discover, and then
 hold the <Shift> key to select all NI-IndCom for CANopen modules in the
 list. Select OK to add the modules to the project. You
 can also add NI-IndCom for CANopen modules offline by selecting New
 target or device , then select C Series
 Module , and in the next dialog select the appropriate
 Module Type , such as NI 9881. When using an NI-IndCom
 for CANopen module in a project, you do not need to have that module installed
 physically. For NI-IndCom for CANopen, the module in a project is simply a
 signal to the FPGA VI that NI-IndCom for CANopen communication is required for
 the slot.

#### Step 4. Compile and run the
 FPGA VI

If you are new to CompactRIO, you can use an empty FPGA VI in
 order to quickly get started with NI-IndCom for CANopen tools and examples. Select
 the FPGA target in LabVIEW project, and then select New»VI.
 When the front panel opens, select the LabVIEW run button (arrow) to compile and run
 the VI. Even though the VI is empty, it will load the required NI-IndCom for CANopen
 support. When compilation completes and the VI runs the first time, you can close
 the front-panel and proceed to the next step.

If you have an existing FPGA VI
 in your project, you must re-compile the FPGA VI in order to incorporate NI-IndCom
 for CANopen support for the configured slots. Once the FPGA VI is re-compiled, you
 run it using the same methods that you used previously. This is typically done using
 the Open FPGA VI Reference from a host VI.

The
 following tables provide a detailed list of actions that cause NI-IndCom for CANopen
 to load and unload. NI-IndCom for CANopen must be loaded in order for its hardware
 to be detected. Within the tables, the term CANopen-enabled FPGA VI refers to an
 FPGA VI compiled with a project that contains at least one NI-IndCom for CANopen
 module. The term CANopen-disabled FPGA VI refers to an FPGA VI compiled with no
 NI-IndCom for CANopen modules.

| Action | Comment |
| --- | --- |
| Invoke Open FPGA VI Reference with a CANOPEN-enabled FPGA VI. | NI-IndCom for CANopen loads regardless of whether Run the FPGA VI is checked in the configuration dialog. |
| Run CANOPEN-enabled FPGA VI using Interactive Front Panel Communication |  |

Note

| Action | Comment |
| --- | --- |
| Invoke Close FPGA VI Reference with shortcut option Close and Reset if Last Reference (default). | If the reference is not the last to close, NI-IndCom for CANopen remains loaded. Shortcut options Close and Close and Abort without Reference Counting do not unload NI-IndCom for CANopen. |
| Power down CompactRIO |  |
| Run CANopen-disabled FPGA VI. | This applies to Open FPGA VI Reference or Interactive Front Panel Communication. |
| Invoke Reset using the Invoke Method node of the FPGA Interface. | Reset of an open FPGA reference causes NI-IndCom for CANopen to unload, and then immediately load again. If you are using NI-IndCom for CANopen interfaces during the reset, the interfaces will be invalidated. Other methods such as Abort do not unload NI-IndCom for CANopen. |
| Run a different CANopen-enabled FPGA VI from the CANopen-enabled FPGA VI currently loaded. | When you change FPGA VIs, the effect is the same as the reset method. NI-IndCom for CANopen unloads, and then immediately loads again. |

Note

#### Step 5. Wait for Interfaces to be Detected

After the FPGA runs with NI-IndCom for CANopen support, it may take a few seconds for
 the new FPGA features to be detected, appropriate RT drivers to load, and NI-IndCom
 for CANopen modules to be detected. This delay occurs only after the action from
 Table X-1 is performed.

In this loading process, after you use the Open FPGA
 VI Reference function to load the CANopen module, you must wait for a few seconds to
 use the *CANopen Create* VI and any other application based on the
 real-time CompactRIO controller. If you start an application on the real-time
 CompactRIO controller immediately after using the Open FPGA VI Reference function,
 an error occurs and NI-IndCom for CANopen fails to run this application. Wait for a
 few seconds and create the CANopen interface.

Note

You can use the options to detect
 NI-IndCom for CANopen hardware:

- MAX Devices & Interfaces —You can detect the
 interfaces visually by opening the Devices &
 Interfaces tree under the RT controller in MAX. Once the
 hardware is detected, you can see CANopen hardware information.
- System API —If you need to detect interfaces
 programmatically within a running RT VI, National Instruments provides APIs for
 this purpose. The NI System Configuration API can detect any NI hardware
 product, including NI-IndCom for CANopen interfaces. NI-IndCom for CANopen also
 provides a System API with properties specific to NI-IndCom for CANopen
 hardware.

#### Step 6. Use NI-IndCom for CANopen

Once the interfaces are detected, you are ready to use these interfaces. Within your
 RT VI, you can use the *NI-IndCom for CANopen VIs* to read and write
 data.

Parent topic:

Getting Started with NI-Industrial Communications for CANopen

<!--NI_TOPIC bundle=ni-industrial-communications-canopen path=getting-started-with-ni-industrial-communicat.html language=enus -->
## TOPIC 00012: Getting Started with NI-Industrial Communications for CANopen

- bundle_id: `ni-industrial-communications-canopen`
- source_path: `getting-started-with-ni-industrial-communicat.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-canopen/raw/resource/enus/getting-started-with-ni-industrial-communicat.html
- document_id: `ni-industrial-communications-canopen`
- page_type: `leaf`
- content_type: `concept`
- source_description: LabVIEW Project Use NI-Industrial Communications for CANopen in a LabVIEW project to interact with batch service data objects (SDO), device baud rates, device node-IDs, and electronic data sheet (EDS) files. NI-Industrial Communications for CANopen introduces the following menus and menu items to th

### Getting Started with NI-Industrial Communications for CANopen

#### LabVIEW Project

Use NI-Industrial Communications for
 CANopen in a LabVIEW project to interact with
 batch service data objects (SDO), device baud rates, device
 node-IDs, and electronic data sheet (EDS) files. NI-Industrial Communications for
 CANopen introduces the following menus and menu
 items to the Project Explorer window.

CANopen Batch SDO

Batch SDO General
 Settings

Project Explorer

New»CANopen Batch SDO

Batch SDO shortcut menu

CANopen Utilities

Online Test
 Panel

Change Device Baud Rate

Change Node-ID

Project Explorer

CANopen Utilities

CANopen EDS File Paths

EDS File Path

Tools»CANopen EDS File
 Paths

#### CANopen VIs

Use the CANopen VIs to
 create CANopen applications. Use the basic programming model to
 create CANopen applications. Access the CANopen VIs from the Industrial
 Communications»CANopen palette.

#### Examples

NI-Industrial Communications for
 CANopen includes LabVIEW examples that demonstrate
 a wide variety of use cases. The examples build on the basic concepts to demonstrate
 more in-depth use cases. To view these examples, select Help»Find
 Examples in LabVIEW. To browse examples by task, locate NI-Industrial Communications for
 CANopen examples under Hardware Input
 and Output»NI-Industrial Communications

Related concepts:

- Creating Batch SDOs
- Basic Programming Model

<!--NI_TOPIC bundle=ni-industrial-communications-canopen path=heartbeat-and-node-guarding.html language=enus -->
## TOPIC 00013: Heartbeat Protocol and Node Guarding Protocol

- bundle_id: `ni-industrial-communications-canopen`
- source_path: `heartbeat-and-node-guarding.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-canopen/raw/resource/enus/heartbeat-and-node-guarding.html
- document_id: `ni-industrial-communications-canopen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the heartbeat protocol or the node guarding protocol to detect device failures on a CANopen network. Heartbeat ProtocolThe heartbeat protocol allows a device to indicate the current network management (NMT) state. This protocol is a producer/consumer protocol. A producer device autonomously tran

### Heartbeat Protocol and Node Guarding
 Protocol

Use the heartbeat protocol or the node guarding protocol to detect device failures
 on a CANopen network.

#### Heartbeat Protocol

The heartbeat protocol
 allows a device to indicate the current *network management* (NMT) state.
 This protocol is a producer/consumer protocol. A producer device autonomously
 transmits a heartbeat message at a specified interval. The heartbeat message
 indicates the NMT state of the device. One or multiple consumer devices receive the
 message. The consumer devices generate heartbeat events if these devices do not
 receive any heartbeat message within a specified time.

Note

h

#### Node Guarding Protocol

The node guarding
 protocol monitors the NMT state of a device. This protocol is a master/slave
 protocol. A master device transmits requests to a slave device. The slave device
 answers each request with a message indicating the NMT state and a toggle bit that
 varies at each response. The master device generates a node guarding event in the
 following cases:

- The slave device switches between different states.
- The slave device does not respond within a specified time.
- The toggle bit does not vary between two subsequent responses.

Parent topic:

CANopen Object Dictionary

Related concepts:

- Network Management

<!--NI_TOPIC bundle=ni-industrial-communications-canopen path=measurement-automation-explorer-help-for-cano.html language=enus -->
## TOPIC 00014: Hardware Information when Using MAX

- bundle_id: `ni-industrial-communications-canopen`
- source_path: `measurement-automation-explorer-help-for-cano.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-canopen/raw/resource/enus/measurement-automation-explorer-help-for-cano.html
- document_id: `ni-industrial-communications-canopen`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use Measurement & Automation Explorer (MAX) to configure and test CANopen hardware. CANopen Hardware Information Product The product name of the NI CANopen device. Serial Number The serial number of the NI CANopen device. Interface The (logical) name of the NI CANopen device. Slot The slot w

### Hardware Information when Using MAX

You can use Measurement & Automation Explorer (MAX) to configure and test CANopen
 hardware.

#### CANopen Hardware Information

Product

Serial Number

Interface

Slot

Note

Note

Parent topic:

CANopen Hardware

<!--NI_TOPIC bundle=ni-industrial-communications-canopen path=network-management.html language=enus -->
## TOPIC 00015: Network Management

- bundle_id: `ni-industrial-communications-canopen`
- source_path: `network-management.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-canopen/raw/resource/enus/network-management.html
- document_id: `ni-industrial-communications-canopen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the network management (NMT) service to control NMT states of CANopen devices. An NMT message forces a target device to transition from one NMT state to another. An NMT message is a 2-byte CAN frame with an identifier of 0 (000[h]). The first byte contains a command specifier which indicates an

### Network Management

Use the network management (NMT) service to control NMT states of CANopen devices.

An NMT message forces a target device to transition from one NMT state to another.

h

- The first byte contains a command specifier which indicates an NMT command.
- The second byte contains a node-ID of a target device. If the node-ID is 0, all
 devices on the CANopen network are the target devices of the NMT command.

#### Device NMT States

A CANopen device has
 the following NMT states:

Initialization

- Initializing —The device performs basic
 initialization and enters the next sub-state.
- Reset application —The device initializes
 parameters in the following two areas of the object
 dictionary : The device sets the parameter values to power-on values. The
 device profile defines the power-on values. The device then enters
 the next sub-state.
  - Manufacturer specific profile area
  - Standardized device profile area
- Reset communication —The device initializes
 parameters in the communication profile area of the object
 dictionary. The device sets the parameter values to power-on values.
 The device profile defines the power-on values.

Pre-operational

Operational

Stopped

heartbeat

node guarding

To trigger state transitions, use the following methods:

- NMT messages
- Hardware resetting
- Device specific events

The following table shows the communication objects that each state supports:

| State | PDO | SDO | SYNC | Emergency | Boot-up | Network Management |
| --- | --- | --- | --- | --- | --- | --- |
| Initialization |  |  |  |  | X |  |
| Pre-operational |  | X | X | X |  | X |
| Operational | X | X | X | X |  | X |
| Stopped |  |  |  |  |  | X |

#### NMT Commands

CANopen has the following
 NMT commands:

- Start remote node —This command switches target devices
 into the operational state.
- Stop remote node —This command switches target devices
 into the stopped state.
- Enter pre-operational —This command switches target
 devices into the pre-operational state.
- Reset node —This command switches target devices into the
 reset application sub-state of the initialization state. The devices initialize
 application and communication parameters and enter the pre-operational
 state.
- Reset communication —This command switches target devices
 into the reset communication sub-state of the initialization state. The devices
 reset communication parameters and enter the pre-operational state.

Parent topic:

CANopen Object Dictionary

Related concepts:

- Heartbeat Protocol and Node Guarding Protocol

<!--NI_TOPIC bundle=ni-industrial-communications-canopen path=new-features-and-changes.html language=enus -->
## TOPIC 00016: NI-Industrial Communications for CANopen New Features and Changes

- bundle_id: `ni-industrial-communications-canopen`
- source_path: `new-features-and-changes.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-canopen/raw/resource/enus/new-features-and-changes.html
- document_id: `ni-industrial-communications-canopen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Learn about updates, including new features and behavior changes, introduced in each version of NI-Industrial Communications for CANopen. Discover what is new in the latest releases of NI-Industrial Communications for CANopen.If you cannot find new features and changes for your version, it might not

### NI-Industrial Communications for
 CANopen
 New Features and Changes

Learn about updates, including new features and behavior changes, introduced in each
 version of NI-Industrial Communications for
 CANopen.

NI-Industrial Communications for
 CANopen

Note

Release Notes

Related information:

- Software and Driver Downloads

#### NI-Industrial Communications for
 CANopen
 2022 Q4 Changes

Learn about new features, behavior changes, and other updates in NI-Industrial Communications for
 CANopen 2022 Q4.

##### New Features

This version of NI-Industrial Communications for
 CANopen provides support for the following features:

- Added support for LabVIEW 2022 (32-bit).
- Extended the LabVIEW version support with NI Linux RealTime to include LabVIEW 2020 and
 later.

#### NI-Industrial Communications for
 CANopen
 21.5 Changes

Learn about new features, behavior changes, and other updates in NI-Industrial Communications for
 CANopen 21.5.

##### New Features

This
 version of NI-Industrial Communications for
 CANopen provides support for the following
 features:

- Added support for LabVIEW 2021 (32-bit).
- Added support for PXI and PXIe controllers with NI Linux RealTime through
 .ipk installation.

<!--NI_TOPIC bundle=ni-industrial-communications-canopen path=previewing-and-validating-batch-sdos.html language=enus -->
## TOPIC 00017: Previewing and Validating Batch SDOs

- bundle_id: `ni-industrial-communications-canopen`
- source_path: `previewing-and-validating-batch-sdos.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-canopen/raw/resource/enus/previewing-and-validating-batch-sdos.html
- document_id: `ni-industrial-communications-canopen`
- page_type: `leaf`
- content_type: `task`
- source_description: You can preview and validate batch SDOs before deploying.If you notice issues when you preview or validate the batch SDOs, modify the batch SDOs in the Batch SDO - Object Dictionary page of the Batch SDO dialog box.Complete the following steps to preview and validate a batch SDO. Right-click an exis

### Previewing and Validating Batch SDOs

You can preview and validate batch SDOs before deploying.

If you notice issues when you preview or validate the batch SDOs, modify the batch SDOs in the
 Batch SDO - Object Dictionary page of the Batch SDO
 dialog box.

Complete the following steps to preview and validate a batch SDO.

1. Right-click an existing batch SDO in the Project Explorer window
 and select Edit from the shortcut menu. The Batch
 SDO dialog box appears.
2. Select Batch SDO - Batch SDO Preview from the
 Category list to display the Batch SDO - Batch SDO
 Preview page.
3. Click the Generate Batch SDO Preview button. LabVIEW generates a preview of this batch SDO.
4. (Optional) Check whether the batch SDO contains all SDOs that you need.
5. Select Batch SDO - Online Validation from the
 Category list to display the Batch SDO - Online
 Validation page.
6. Configure the following settings on this page for local CANopen network: 
 Interface name/location
 Interface baud rate
 Device node-ID
 Timeout
7. Click the Send Batch SDO button to validate the batch SDO. 
 LabVIEW validates the batch SDO by using the settings you specified in the previous
 step. The Status field returns the validation result.

Parent topic:

Configuring CANopen

Related concepts:

- Creating Batch SDOs

Related information:

- Batch SDO - Object Dictionary Page
- Batch SDO Dialog Box
- Batch SDO - Preview Page
- Batch SDO - Online Verification Page

<!--NI_TOPIC bundle=ni-industrial-communications-canopen path=process-data-object.html language=enus -->
## TOPIC 00018: Process Data Object

- bundle_id: `ni-industrial-communications-canopen`
- source_path: `process-data-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-canopen/raw/resource/enus/process-data-object.html
- document_id: `ni-industrial-communications-canopen`
- page_type: `leaf`
- content_type: `concept`
- source_description: A process data object (PDO) provides access to application objects stored within a device. A PDO transfers short blocks of high priority data in real time. A PDO consists of a header containing a COB-ID and a number of data bytes. A PDO may contain a maximum of eight data bytes. The device PDO confi

### Process Data Object

A process data object (PDO) provides access to application objects stored within a
 device.

COB-ID

Note

- When a device sends a PDO, this device is a PDO producer. The PDO
 is a transmit-PDO (TPDO) of this device.
- When a device receives a PDO, this device is a PDO consumer. The
 PDO is a receive-PDO (RPDO) of this device.

Parent topic:

CANopen Object Dictionary

<!--NI_TOPIC bundle=ni-industrial-communications-canopen path=protocol-overview.html language=enus -->
## TOPIC 00019: CANopen Protocol Overview

- bundle_id: `ni-industrial-communications-canopen`
- source_path: `protocol-overview.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-canopen/raw/resource/enus/protocol-overview.html
- document_id: `ni-industrial-communications-canopen`
- page_type: `leaf`
- content_type: `concept`
- source_description: A controller area network (CAN) is a low-cost real-time network of devices. Use CAN to connect devices such as controllers, sensors, and actuators on a common serial bus. Each device on a CAN network communicates with another device by using a common pair of wires. The International Organization for

### CANopen Protocol Overview

A *controller area network* (CAN) is a low-cost real-time network of devices. Use CAN
 to connect devices such as controllers, sensors, and actuators on a common serial bus.
 Each device on a CAN network communicates with another device by using a common pair of
 wires. The *International Organization for Standardization* (ISO)
 standardizes the CAN protocol as ISO 11898.

*CANopen* is a CAN-based higher layer protocol with flexible configuration
 capabilities. Each CANopen device contains a *device profile*. To configure
 the device, modify the device profile. You can use CANopen in various fields, such as
 medical equipment, vehicles, public transportation, and building automation.

#### CANopen Communication Objects

CANopen provides the following standard communication objects:

- Process data object (PDO)
- Service data object (SDO)
- Synchronization object (SYNC)
- Emergency object (EMCY)
- Network Management object (NMT)
- Heartbeat object
- Node guarding object

CANopen object dictionary

Note

CANopen Object
 Dictionary

#### Node-IDs
 and COB-IDs

A *node-ID* is an address that identifies a device on a
 CANopen network. A node-ID ranges from 1 to 127. Devices use CANopen messages to communicate
 with each other.

- Message ID. The message ID is a communication object identifier 
 (COB-ID).
- Remote transmit request (RTR) bit.
- Length indication.

CANopen uses 11-bit COB-IDs and supports 29-bit COB-IDs.

- The sequence of the first four bits is a function code of the CANopen message.
- The sequence of the remaining seven bits is a node-ID.

The following table shows the distribution of COB-IDs:

| Communication Object | Function Code (Binary) | Resulting COB-ID |
| --- | --- | --- |
| NMT | 0000 | 0 |
| SYNC | 0001 | 128 (80h) |
| EMCY | 0001 | 129 (81h) - 255 (FFh), 80h + node-ID |
| PDO1 (TPDO) | 0011 | 385 (181h) - 511 (1FFh), 180h + node-ID |
| PDO1 (RPDO) | 0100 | 513 (201h) - 639 (27Fh), 200h + node-ID |
| PDO2 (TPDO) | 0101 | 641 (281h) - 767 (2FFh), 280h + node-ID |
| PDO2 (RPDO) | 0110 | 769 (301h) - 895 (37Fh), 300h + node-ID |
| PDO3 (TPDO) | 0111 | 897 (381h) - 1023 (3FFh), 380h + node-ID |
| PDO3 (RPDO) | 1000 | 1025 (401h) - 1151 (47Fh), 400h + node-ID |
| PDO4 (TPDO) | 1001 | 1153 (481h) - 1279 (4FFh), 480h + node-ID |
| PDO4 (RPDO) | 1010 | 1281 (501h) - 1407 (57Fh), 500h + node-ID |
| SDO (TSDO) | 1011 | 1409 (581h) - 1535 (5FFh), 580h + node-ID |
| SDO (RSDO) | 1100 | 1537 (601h) - 1663 (67Fh), 600h + node-ID |
| Error control | 1110 | 1793 (701h) - 1919 (77Fh), 700h + node-ID |

Most devices comply with this connection set. The device profile defines which
 communication objects the device supports.

For more information about CANopen, refer
 to the *CAN in Automation (CiA)* website.

Related concepts:

- Device Profiles
- CANopen Object Dictionary

Related information:

- CAN in Automation (CiA)

<!--NI_TOPIC bundle=ni-industrial-communications-canopen path=service-data-object.html language=enus -->
## TOPIC 00020: Service Data Object

- bundle_id: `ni-industrial-communications-canopen`
- source_path: `service-data-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-canopen/raw/resource/enus/service-data-object.html
- document_id: `ni-industrial-communications-canopen`
- page_type: `leaf`
- content_type: `concept`
- source_description: A service data object (SDO) allows a device to read from or write to the CANopen object dictionary. An SDO reads from entries or writes to entries in the object dictionary. An SDO contains two CAN frames with different COB-IDs. The operation of SDOs is on the basis of client/server relationship. The

### Service Data Object

A service data object (SDO) allows a device to read from or write to the CANopen
 object dictionary.

An SDO reads from entries or writes to entries in the object dictionary. An SDO contains two CAN
 frames with different COB-IDs. The operation of SDOs is on the basis of client/server
 relationship. The SDO communication is peer-to-peer communication. The client sends
 requests and the server responds to those requests.

If an error occurs, for instance an entry does not exist, the device returns a message containing a completion code that represents the error.

Parent topic:

CANopen Object Dictionary

<!--NI_TOPIC bundle=ni-industrial-communications-canopen path=synchronization.html language=enus -->
## TOPIC 00021: Synchronization

- bundle_id: `ni-industrial-communications-canopen`
- source_path: `synchronization.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-canopen/raw/resource/enus/synchronization.html
- document_id: `ni-industrial-communications-canopen`
- page_type: `leaf`
- content_type: `concept`
- source_description: A synchronization (SYNC) object provides synchronous communication on a CANopen network. An SYNC producer broadcasts SYNC messages in the network periodically. An SYNC message is a single CAN frame with an identifier 128 (080[h]) by default. Configure devices to transmit synchronous PDOs when the de

### Synchronization

A synchronization (SYNC) object provides synchronous communication on a
 CANopen network.

An SYNC producer broadcasts SYNC messages in the network periodically. An SYNC message is a
 single CAN frame with an identifier 128
 (080<sub>h</sub>) by default. Configure devices to
 transmit synchronous PDOs when the devices receive
 an SYNC message. Each device may have a time jitter
 in transmission when other objects have higher
 priority identifiers or transmitting orders. The
 maximum time jitter indicates the quality of the
 synchronization.

The time period between SYNC messages depends on the communication cycle period parameter. You
 may configure this parameter during the boot-up
 process. Synchronous Counter Overflow

The synchronous counter overflow object is an *object dictionary* entry that defines the maximum value of the SYNC counter. The SYNC counter is an optional part of an SYNC message. You can enable the SYNC counter by specifying a non-zero value to the synchronous counter overflow object.

The SYNC counter value starts from 1 and increases by 1 with each SYNC message. An SYNC cycle is
 the time period between the time when the SYNC
 counter value is 1 and the time when the SYNC
 counter value reaches the synchronous counter
 overflow value. At the end of an SYNC cycle, the
 device sends out the SYNC message with a counter
 value that equals the synchronous counter overflow
 value. The device then resets the SYNC counter value
 to 1 for the next SYNC message. The next SYNC
 message starts another SYNC cycle.

Use the synchronous counter overflow object to ensure periodic SYNC events occur in SYNC cycles with the same SYNC counter value. You can use specific SYNC counter values to trigger multiple periodic SYNC events. For example, you can set the periods of event A and event B to 3 and the period of event C to 4. You then set the synchronous counter overflow to 12. When you execute the application, event A and event B occur when the SYNC counter is 3, 6, 9, and 12. Event C occurs when the SYNC counter is 4, 8, and 12.

| Value | Description |
| --- | --- |
| 0 | The SYNC message is a CAN message containing 0 data bytes. The SYNC message does not contain an SYNC counter. |
| 1 | Reserved. |
| 2 to 240 | The SYNC message is a CAN message containing 1 data byte. The data byte is an SYNC counter. |
| 241 to 255 | Reserved. |

Parent topic:

CANopen Object Dictionary

<!--NI_TOPIC bundle=ni-industrial-communications-canopen path=troubleshooting-canopen-applications.html language=enus -->
## TOPIC 00022: Troubleshooting CANopen Applications

- bundle_id: `ni-industrial-communications-canopen`
- source_path: `troubleshooting-canopen-applications.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-canopen/raw/resource/enus/troubleshooting-canopen-applications.html
- document_id: `ni-industrial-communications-canopen`
- page_type: `leaf`
- content_type: `concept`
- source_description: Guidelines to troubleshoot common issues with CANopen applications.Use the following guidelines to troubleshoot common issues when creating or executing CANopen applications. All CANopen operations return failures A possible reason is that the CANopen devices use inconsistent baud rates. All CANopen

### Troubleshooting CANopen Applications

Guidelines to troubleshoot common issues with CANopen applications.

Use the following guidelines to troubleshoot common issues when creating or executing CANopen
 applications.

All CANopen operations return failures

All CANopen devices must use the same baud rate on a CANopen network.

Ensure all operations use the same baud rate. For example, if the
 baud rate of a device is 1 Mbps, the baud
 rate of the CANopen interface must be 1
 Mbps.

LabVIEW fails to change node-IDs or baud rates of some devices

If a device does not support LSS, you cannot change the node-ID or
 baud rate by using LabVIEW dialog boxes or VIs. You can change the node-ID
 or baud rate by using switches on the device.

Some devices support LSS
 in the stopped state only. You can use the CANopen NMT
 Write VI to switch the device into the stopped state before
 changing the node-ID or baud rate.

After LabVIEW changes a node-ID or a baud rate, the change does not take
 effect

CANopen NMT Write

For example, after you
 change the node-ID from 2 to 3, reset the device with the original
 node-ID 2. The device switches into the new
 node-ID 3 after the reset.

The device does not change states when receiving a network management (NMT)
 message

For example, if you
 send out a reset command, a device may need five seconds to reset all the
 parameters and enter the pre-operational state.

service data objects

Switch a device into either of these states to use SDOs.

process data objects

Switch a device into the
 operational state to use PDOs.

Online Test Panel

Online Test Panel

Ensure the device is in the pre-operational state
 and re-scan devices in the Online Test Panel.

If the device is not in the pre-operational state, send an Enter
 pre-operational command to switch the device into the pre-operational state.
 You can send the command by using the NMT status page
 of the Online Test Panel dialog box or the
 CANopen NMT Write VI.

Online Test Panel

Online Test Panel

Online Test Panel

For example, if
 the original baud rate is 10 kbps, you can
 change the baud rate to 1 Mbps to improve the
 performance.

Change Device Baud Rate

Try all baud rates

You can
 disable the detection to improve the performance. You may disable the
 detection by removing the checkmark from the checkbox and specifying the
 current baud rate manually.

CANopen CAN Frame Read

CANopen CAN Frame
 Write

You must assign another interface to
 the CANopen CAN Frame Read VI to read the CANopen frame.
 Otherwise, the CANopen CAN Frame Read VI cannot read the
 message.

Devices may need some time to transmit and receive CANopen
 frames.

In Measurement & Automation Explorer (MAX), a PXI device does not display
 the slot number.

To
 re-identify the PXI device, right-click the PXI device in MAX and select
 Identify As»Device_model. To re-identify the
 chassis, perform the same steps.

The error status LED of the device is solid red

To change device
 baud rates to the same baud rate, use the Online Test
 Panel dialog box. To clear the error, re-open the CANopen
 interface with the new baud rate.

The baud rate that you use to
 communicate with this device does not match the device baud rate. Ensure you
 use the correct baud rate and re-open the CANopen interface to clear the
 error.

Parent topic:

Configuring CANopen

Related concepts:

- Service Data Object
- Process Data Object

Related information:

- CANopen VIs
- Online Test Panel Dialog Box
- Online Test Panel Dialog Box

<!--NI_TOPIC bundle=ni-industrial-communications-canopen path=user-manual-welcome.html language=enus -->
## TOPIC 00023: NI-Industrial Communications for CANopen User Manual

- bundle_id: `ni-industrial-communications-canopen`
- source_path: `user-manual-welcome.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-canopen/raw/resource/enus/user-manual-welcome.html
- document_id: `ni-industrial-communications-canopen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI-Industrial Communications for CANopen User Manual provides detailed descriptions of the product functionality and the step by step processes for use. Looking for Something Else?For information not found in the User Manual for your product, such as specifications and API reference, browse Rela

### NI-Industrial Communications for
 CANopen
 User Manual

The NI-Industrial Communications for
 CANopen User Manual provides detailed
 descriptions of the product functionality and the step by step processes for use.

#### Looking for Something Else?

For information not found in the User Manual
 for your product, such as specifications and API reference, browse *Related
 Information*.

Related information:

- Download NI-Industrial Communications for CANopen
- NI-Industrial Communications for CANopen Release Notes
- NI-Industrial Communications for CANopen Programming Reference
 Manual
- The Basics of CANopen
- PCI/PXI-8531 Specifications
- NI-9881 and sbRIO-9881 Specifications

<!--NI_TOPIC bundle=ni-industrial-communications-canopen path=using-the-labview-real-time-module.html language=enus -->
## TOPIC 00024: Using the LabVIEW Real-Time Module

- bundle_id: `ni-industrial-communications-canopen`
- source_path: `using-the-labview-real-time-module.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-canopen/raw/resource/enus/using-the-labview-real-time-module.html
- document_id: `ni-industrial-communications-canopen`
- page_type: `leaf`
- content_type: `concept`
- source_description: The LabVIEW Real-Time (RT) Module combines LabVIEW graphical programming with the power of a real-time operating system, enabling you to build real-time applications. The NI-Industrial Communications for CANopen provides features and performance specifically designed for the LabVIEW Real-Time Module

### Using the LabVIEW Real-Time Module

The LabVIEW Real-Time (RT) Module combines LabVIEW graphical programming with the power of a real-time operating system, enabling you to build real-time applications. The NI-Industrial Communications for CANopen provides features and performance specifically designed for the LabVIEW Real-Time Module.
High Priority Loops

Many real-time applications contain at least one loop that must execute at the highest priority. This high-priority loop typically contains code to read inputs, execute a control algorithm, and then write outputs. The high-priority loop executes at a fast period, such as 500 µs (2 kHz). To ensure that the loop diagram executes within the period, the node must meet the following two requirements:

- Low cost—The average execution time of the node, such as read and write VIs, must be low.
- Low jitter—The execution time also must be consistent from one loop iteration to another.

Most of the read and write VIs, except the *CANopen SDO Read* VI and *CANopen SDO Write* VI in the *CANopen* VIs provide fast and consistent execution time, and these VIs avoid access to shared resources. When these VIs execute for the first loop iteration, these VIs often perform tasks such as auto-start of the session, and so on. These tasks result in high cost for the first iteration compared to any subsequent iteration. When you measure performance of the VIs, discard the first iteration from the measurement.

For VIs or property nodes other than the read and write VIs, you must assume the nodes do not support high priority loops. The property nodes are designed for configuration purposes. VIs that change state, such as the *CANopen Start* VI, require time for hardware or software configuration. However, certain properties and VIs support high-priority use.

Refer to the help for the specific node you want to use for information about whether this node supports a high priority loop.

Parent topic:

Getting Started with NI-Industrial Communications for CANopen
