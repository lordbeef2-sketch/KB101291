# NI DOCUMENT BUNDLE: ni-serial

<!--NI_BUNDLE_CHUNK bundle=ni-serial start=1 end=67 -->
<!--NI_TOPIC bundle=ni-serial path=advanced-features.html language=enus -->
## TOPIC 00001: Advanced Features

- bundle_id: `ni-serial`
- source_path: `advanced-features.html`
- source_url: https://docs-be.ni.com/bundle/ni-serial/raw/resource/enus/advanced-features.html
- document_id: `ni-serial`
- page_type: `leaf`
- content_type: `concept`
- source_description: In addition to supporting standard 16550-compatible UART functionality, some NI serial hardware supports additional advanced features: Adjustable FIFO levels RS-485 transceiver control RS-485 socketed bias resistors RS-485 programmatically controlled bias resistors RS-232 transceiver state RS-232 DT

### Advanced Features

In addition to supporting standard 16550-compatible UART functionality, some NI serial
 hardware supports additional advanced features:

- Adjustable FIFO levels
- RS-485 transceiver control
- RS-485 socketed bias resistors
- RS-485 programmatically controlled bias resistors
- RS-232 transceiver state
- RS-232 DTE/DCE transceiver control
- Hardware implemented flow control

To determine which features your product supports, refer to the following table.

#### Serial Hardware Features

| Hardware | Adjustable FIFO Settings | Get Interface Type | RS-485 Transceiver Control | RS-485 Socketed Bias Resistors | RS-485 Programmatically Controlled Bias Resistors | RS-232 Transceiver State | RS-232 DTE/DCE Transceiver Control | Hardware Implemented Flow Control - RTS/CTS | Hardware Implemented Flow Control - DTR/DSR | Hardware Implemented Flow Control - Xon/Xoff |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PCI/NI PCIe/PXI/NI PXIe-8430, PCI/PXI-8432 | X | X |  |  |  | X |  | X | X | X |
| PCI-232, PXI-8420, PXI-8422 | X | X |  |  |  |  |  | X |  | X |
| PCI/NI PCIe/PXI/NI PXIe-8431 eight port, NI PCIe-8431 16 port, PCI-485 eight port, PXI-8421 eight port | X | X | X |  |  |  |  | X |  | X |
| All other PCI/PXI-8431, PCI/PXI-8433, PCI-485, PXI-8421, and PXI-8423 | X | X | X | X |  |  |  | X |  | X |
| USB-232 one port |  | X |  |  |  | X |  | X | X | X |
| USB-232 two and four port |  | X |  |  |  | X | X | X | X | X |
| USB-485 one port |  | X | X |  | X |  |  | X |  | X |
| USB-485 two and four port |  | X | X | X | X |  |  | X |  | X |
| ENET-232 |  |  |  |  |  |  |  | X | X | X |
| ENET-485 |  |  | X | X |  |  |  | X |  | X |
| NI ExpressCard-8420 |  | X |  |  |  | X |  | X | X | X |
| NI ExpressCard-8421 |  | X | X |  | X |  |  | X |  | X |

Related concepts:

- FIFO Buffers
- Retrieving the Serial Interface Type
- RS-485 Transceiver Control
- Bias Resistors
- USB-485 Programmatically Controlled Bias Resistors
- Retrieving the RS-232 Transceiver State
- RS-232 DTE versus DCE
- Hardware Implemented Flow Control

<!--NI_TOPIC bundle=ni-serial path=baud-rates.html language=enus -->
## TOPIC 00002: Baud Rates

- bundle_id: `ni-serial`
- source_path: `baud-rates.html`
- source_url: https://docs-be.ni.com/bundle/ni-serial/raw/resource/enus/baud-rates.html
- document_id: `ni-serial`
- page_type: `leaf`
- content_type: `concept`
- source_description: The maximum baud rates supported are listed in the table below. HardwarePlatform Maximum Baud Rate RS-232 RS-485 PCI/NI PCIe-843x 1000 kbits/s 3000 kbits/s^1 PCI-232/485 115.2 kbits/s 460.8 kbits/s PXI/NI PXIe-843x 1000 kbits/s 3000 kbits/s^1, 2 PXI-842x 115.2 kbits/s 460.8 kbits/s USB 230.4 kbits/s

### Baud Rates

The maximum baud rates supported are listed in the table below.

| HardwarePlatform | Maximum Baud Rate |  |
| --- | --- | --- |
| RS-232 | RS-485 |  |
| PCI/NI PCIe-843x | 1000 kbits/s | 3000 kbits/s1 |
| PCI-232/485 | 115.2 kbits/s | 460.8 kbits/s |
| PXI/NI PXIe-843x | 1000 kbits/s | 3000 kbits/s1, 2 |
| PXI-842x | 115.2 kbits/s | 460.8 kbits/s |
| USB | 230.4 kbits/s | 460.8 kbits/s |
| ENET | 230.4 kbits/s | 460.8 kbits/s |
| ExpressCard | 230.4 kbits/s | 460.8 kbits/s |

All NI serial hardware supports standard baud rates. In addition, the PCI/NI
 PCIe/PXI-843x family of hardware supports any baud rate between 2
 bits/s and the maximum supported baud rate for that interface.

National Instruments considers the following baud rates to be standard. NI serial
 hardware supports these rates up to the maximum rate specified. Your device may also
 support additional baud rates not listed below:

| 300 | 19200 |
| --- | --- |
| 600 | 38400 |
| 1200 | 57600 |
| 2400 | 115200 |
| 4800 | 230400 |
| 9600 | 460800 |
| 14400 |  |

To set the baud rate, set the VISA Baud attribute or use the Windows SetCommState
 function and pass the actual value of the baud rate in the
 BaudRate field of the DCB
 structure.

<sup>1</sup>The two-wire auto control mode for the RS-485 transceiver has a maximum baud
 rate of 2000 kbits/s.

<sup>2</sup>For possible use with higher baud rates, refer to ni.com/kb
 and search for KnowledgeBase 58KEI82F.

<!--NI_TOPIC bundle=ni-serial path=bias-resistors.html language=enus -->
## TOPIC 00003: Bias Resistors

- bundle_id: `ni-serial`
- source_path: `bias-resistors.html`
- source_url: https://docs-be.ni.com/bundle/ni-serial/raw/resource/enus/bias-resistors.html
- document_id: `ni-serial`
- page_type: `leaf`
- content_type: `concept`
- source_description: An RS-485 transmission line enters an indeterminate state if no nodes are transmitting on it. This indeterminate state can cause the receivers to receive invalid data bits from noise picked up on the cable. To prevent a line from receiving these data bits, the transmission line can be forced into a

### Bias Resistors

An RS-485 transmission line enters an indeterminate state if no nodes are transmitting on
 it. This indeterminate state can cause the receivers to receive invalid data bits from
 noise picked up on the cable. To prevent a line from receiving these data bits, the
 transmission line can be forced into a known state by installing two bias resistors at
 one node on the transmission line. Doing so creates a voltage divider that forces the
 voltage between the differential pair to be greater than 200 mV, the threshold voltage
 for the receiver.

The following figure shows a transmission line using bias resistors.

[IMAGE alt='image' src='GUID-092DAEB6-21DC-4E92-8961-AC7A3069030D-a5.gif']

#### Transmission Line Using Bias Resistors

On the PCI RS-485 two and four-port serial cards, PXI RS-485 two and four-port serial
 cards, and ENET RS-485 two and four-port serial cards, there are four
 user-configurable bias resistors in front of each connector. These resistors are
 socketed and pre-loaded with 620 [IMAGE alt='image' src='GUID-3D97CC5D-839F-4675-B3BF-F1B240D4C49D-a5.gif'] resistors. They are connected to the receive signals of each
 port to maintain a known state when the bus is idle. The connections are made as
 follows:

- RXD+ and CTS– are pulled up to +5 V
- RXD– and CTS+ are pulled down to GND

Rather than using two 620 [IMAGE alt='image' src='GUID-3D97CC5D-839F-4675-B3BF-F1B240D4C49D-a5.gif'] resistors at one node, you can increase the value of the
 resistors and put them at every node. For instance, if there are eight nodes in a
 system, you can use 4.7 k[IMAGE alt='image' src='GUID-3D97CC5D-839F-4675-B3BF-F1B240D4C49D-a5.gif'] resistors at each node to effectively achieve the same
 result.

[IMAGE alt='image' src='GUID-3D97CC5D-839F-4675-B3BF-F1B240D4C49D-a5.gif']

<!--NI_TOPIC bundle=ni-serial path=can-i-use-ni-serial-hardware-with-a-non-windows.html language=enus -->
## TOPIC 00004: Can I use NI serial hardware with a non-Windows platform?

- bundle_id: `ni-serial`
- source_path: `can-i-use-ni-serial-hardware-with-a-non-windows.html`
- source_url: https://docs-be.ni.com/bundle/ni-serial/raw/resource/enus/can-i-use-ni-serial-hardware-with-a-non-windows.html
- document_id: `ni-serial`
- page_type: `leaf`
- content_type: `concept`
- source_description: Refer to the following table for operating system support for NI serial hardware. NI-Serial Hardware Operating System Support Bus Windows 7 32 Windows 7 64 Windows Vista 32 Windows Vista 64 Windows XP Windows 2000 Windows 2003 Server R2 32-bit Windows 2008 Server R2 64-bit Linux LabVIEW Real-Time Ma

### Can I use NI serial hardware with a non-Windows platform?

Refer to the following table for operating system support for NI serial hardware.

#### NI-Serial Hardware Operating System Support

| Bus | Windows 7 32 | Windows 7 64 | Windows Vista 32 | Windows Vista 64 | Windows XP | Windows 2000 | Windows 2003 Server R2 32-bit | Windows 2008 Server R2 64-bit | Linux | LabVIEW Real-Time | Mac OS X |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PCI/NI PCIe-843x | ●▲ | ●▲ | ●▲ | ●▲ | ●▲ | ●▲3 | ●▲ | ●▲ | ▲2 | ●▲ |  |
| PCI-232/485 | ●▲ | ●▲ | ●▲ | ●▲ | ●▲ | ●▲3 | ●▲ | ●▲ | ●▲ | ●▲ |  |
| PXI-843x/NI PXIe-843x | ●▲ | ●▲ | ●▲ | ●▲ | ●▲ | ●▲3 | ●▲ | ●▲ | ▲2 | ●▲ |  |
| PXI-842x | ●▲ | ●▲ | ●▲ | ●▲ | ●▲ | ●▲3 | ●▲ | ●▲ |  | ●▲ |  |
| USB | ●▲ | ●▲ | ●▲ | ●▲ | ●▲ | ●▲3 | ●▲ | ●▲ |  |  |  |
| ENET | ●▲ | ● | ●▲ | ● | ●▲ | ●▲3 | ●▲ | ●▲ | ● | ● | ● |
| ExpressCard | ●▲ | ●▲ | ●▲ | ●▲ | ●▲ | ●▲3 | ●▲ | ●▲ |  |  |  |
| PCMCIA |  |  | ●▲1 |  | ●▲1 | ●▲1 |  |  | ●▲ |  |  |

● NI-VISA Support

▲ Native OS Support

For more information about using NI serial hardware in Linux, refer to
 ni.com/kb and search for 1PJDDEV8.

<sup>1</sup>Supported by NI-Serial versions 3.5.0 and earlier.

<sup>2</sup>Supported with Linux kernel 2.6.30 and later
 (PCI/PXI-843x and RS-232 only).

<sup>3</sup>Windows 2000 supported by NI-Serial versions 3.5.1 and earlier.

<!--NI_TOPIC bundle=ni-serial path=can-i-use-usb-serial-hardware-ethernet-serial.html language=enus -->
## TOPIC 00005: Can I use USB serial hardware, Ethernet serial hardware, and plug-in serial hardware in the same computer at the same time?

- bundle_id: `ni-serial`
- source_path: `can-i-use-usb-serial-hardware-ethernet-serial.html`
- source_url: https://docs-be.ni.com/bundle/ni-serial/raw/resource/enus/can-i-use-usb-serial-hardware-ethernet-serial.html
- document_id: `ni-serial`
- page_type: `leaf`
- content_type: `concept`
- source_description: As long as your operating system supports all your NI serial hardware, you can mix different types of serial interfaces in your computer. All NI serial hardware and software is designed and tested for interoperability.

### Can I use USB serial hardware, Ethernet serial hardware, and plug-in serial hardware in
 the same computer at the same time?

As long as your operating system supports all your NI serial hardware, you can mix
 different types of serial interfaces in your computer. All NI serial hardware and
 software is designed and tested for interoperability.

<!--NI_TOPIC bundle=ni-serial path=delete-a-serial-interface.html language=enus -->
## TOPIC 00006: Delete a Serial Interface

- bundle_id: `ni-serial`
- source_path: `delete-a-serial-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-serial/raw/resource/enus/delete-a-serial-interface.html
- document_id: `ni-serial`
- page_type: `leaf`
- content_type: `concept`
- source_description: Before you physically remove a serial interface from your Windows system, follow these steps to remove the hardware information: Launch MAX. Expand the My System directory by clicking the + next to the folder. Expand the Devices and Interfaces directory by clicking the + next to the folder. Right-cl

### Delete a Serial Interface

Before you physically remove a serial interface from your Windows system, follow these
 steps to remove the hardware information:

1. Launch MAX.
2. Expand the My System directory by clicking the
 + next to the folder.
3. Expand the Devices and Interfaces directory by clicking the +
 next to the folder.
4. Right-click on your serial interface and select Delete from
 the drop-down menu that appears.
5. When prompted, click the Yes button to confirm the removal of
 your interface.
6. MAX automatically updates the list of installed serial interfaces. You can also
 select View»Refresh to update the list.

On LabVIEW RT, it is not necessary to programmatically delete hardware from the system.
 Simply power down your RT controller and remove the hardware. When you power on your RT
 controller again, the ports are automatically removed from the system. You may need to
 refresh MAX to see the changes.

<!--NI_TOPIC bundle=ni-serial path=does-the-serial-hardware-have-built-in-suppor.html language=enus -->
## TOPIC 00007: Does the serial hardware have built-in support for protocols such as SDLC and ModBus?

- bundle_id: `ni-serial`
- source_path: `does-the-serial-hardware-have-built-in-suppor.html`
- source_url: https://docs-be.ni.com/bundle/ni-serial/raw/resource/enus/does-the-serial-hardware-have-built-in-suppor.html
- document_id: `ni-serial`
- page_type: `leaf`
- content_type: `concept`
- source_description: Because the serial hardware uses UARTs for communication, protocols such as SDLC and ModBus are not supported in hardware. However, these protocols (or their derivatives) can be supported by software applications that handle the protocol translation.

### Does the serial hardware have built-in support for protocols such as SDLC and
 ModBus?

Because the serial hardware uses UARTs for communication, protocols such as SDLC and
 ModBus are not supported in hardware. However, these protocols (or their derivatives)
 can be supported by software applications that handle the protocol translation.

<!--NI_TOPIC bundle=ni-serial path=duplex-architectures.html language=enus -->
## TOPIC 00008: Duplex Architectures

- bundle_id: `ni-serial`
- source_path: `duplex-architectures.html`
- source_url: https://docs-be.ni.com/bundle/ni-serial/raw/resource/enus/duplex-architectures.html
- document_id: `ni-serial`
- page_type: `leaf`
- content_type: `concept`
- source_description: Duplex refers to the means of bandwidth usage in a serial system. The two common means of bi-directional serial communication are full duplex and half duplex. Half-duplex communication involves a transmitter and a receiver connected to each end of the same wire or pair of wires. Because the same tra

### Duplex Architectures

Duplex refers to the means of bandwidth usage in a serial system. The
 two common means of bi-directional serial communication are full duplex and half duplex.
 Half-duplex communication involves a transmitter and a receiver connected to each end of
 the same wire or pair of wires. Because the same transmission line both sends and
 receives data, devices cannot send data in both directions at the same time. First, one
 device transmits over the wire(s) to the receiver of the second device. When the first
 device finishes transmitting, both devices switch the connections from their transmitter
 to their receiver, or vice versa. The device that was receiving data can then transmit
 over the line.

In full-duplex communication, the devices use a separate wire (or pair of wires) for
 simultaneous transmission in each direction. Thus, the devices do not switch between
 transmitting and receiving.

In a differential serial bus (such as RS-422 or RS-485), a half-duplex system transmits
 and receives over the same twisted pair of wires. Thus, half-duplex communication is
 often referred to as two-wire communication. Likewise, full-duplex
 communication is often referred to as four-wire communication,
 because the full-duplex system uses a separate pair of wires for communication in each
 direction.

Parent topic:

Serial Communication Issues

<!--NI_TOPIC bundle=ni-serial path=expresscard-hardware-installation.html language=enus -->
## TOPIC 00009: ExpressCard Hardware Installation

- bundle_id: `ni-serial`
- source_path: `expresscard-hardware-installation.html`
- source_url: https://docs-be.ni.com/bundle/ni-serial/raw/resource/enus/expresscard-hardware-installation.html
- document_id: `ni-serial`
- page_type: `leaf`
- content_type: `concept`
- source_description: Before installing your hardware, follow the NI-Serial Software Installation instructions. To install the ExpressCard serial board in your computer, insert the card into a free ExpressCard socket. The card has no jumpers or switches to set, and you do not need to shut down the system before you inser

### ExpressCard Hardware Installation

Before installing your hardware, follow the NI-Serial Software Installation
 instructions.

To install the ExpressCard serial board in your computer, insert the card into a free
 ExpressCard socket. The card has no jumpers or switches to set, and you do not need to
 shut down the system before you insert it.

Windows will automatically detect your hardware.

The serial hardware installation is complete. Continue to Verify the Installation.

<!--NI_TOPIC bundle=ni-serial path=fifo-buffers.html language=enus -->
## TOPIC 00010: FIFO Buffers

- bundle_id: `ni-serial`
- source_path: `fifo-buffers.html`
- source_url: https://docs-be.ni.com/bundle/ni-serial/raw/resource/enus/fifo-buffers.html
- document_id: `ni-serial`
- page_type: `leaf`
- content_type: `concept`
- source_description: FIFO buffers are present on the 16550-compatible UARTs—one for the transmitter and one for the receiver. The Receive Buffer control sets the number of characters received in the FIFO before the PC is interrupted to read the data. The Transmit Buffer control sets the maximum number of bytes written t

### FIFO Buffers

FIFO buffers are present on the 16550-compatible UARTs—one for the transmitter and one
 for the receiver. The Receive Buffer control sets the number of characters received in
 the FIFO before the PC is interrupted to read the data. The Transmit Buffer control sets
 the maximum number of bytes written to the FIFO when the PC is interrupted to write the
 data.

The built-in ports on PXI RT controllers and the PCI, PCI Express, PXI, and PXI Express
 plug-in serial boards have configurable FIFO settings. Use the
 Advanced tab in Measurement & Automation Explorer to
 configure your FIFO settings. When you configure FIFO settings, consider the following
 points:

- You can select larger FIFO buffer sizes to reduce the number of interrupts your PC
 receives and thereby minimize system overhead.
- If transfer rates are high, you can lower the Receive Buffer value to prevent
 overrun errors due to interrupt latency.
- If your data transfer sizes are small, and your Receive Buffer value is above your
 data sizes, your system is less efficient. For maximum efficiency, set your Receive
 Buffer value such that your data transfer size is a multiple of that value.
- Using flow control minimizes the chance of FIFO overrun errors. For best results,
 use a flow control method implemented in hardware according to the Advanced Features table.

Related concepts:

- Advanced Features

<!--NI_TOPIC bundle=ni-serial path=full-duplex.html language=enus -->
## TOPIC 00011: Full Duplex

- bundle_id: `ni-serial`
- source_path: `full-duplex.html`
- source_url: https://docs-be.ni.com/bundle/ni-serial/raw/resource/enus/full-duplex.html
- document_id: `ni-serial`
- page_type: `leaf`
- content_type: `concept`
- source_description: A typical full-duplex multidrop bus architecture involves a master-slave protocol. Only one device, the master, can control access to the bus. All other devices are slaves. Slave devices must wait for the master to give them access to the bus. In a typical full-duplex system, one transmission line c

### Full Duplex

A typical full-duplex multidrop bus architecture involves a master-slave protocol. Only
 one device, the master, can control access to the bus. All other devices are slaves.
 Slave devices must wait for the master to give them access to the bus. In a typical
 full-duplex system, one transmission line connects the bus master transmitter to all of
 the slave receivers. A second transmission line connects all of the slave transmitters
 to the bus master receiver. Because each transmission line has two separate wires, a
 full-duplex system is often referred to as a four-wire system. The master uses four-wire
 mode, and the slaves use two-wire mode. The following figure shows a typical full-duplex
 system.

[IMAGE alt='image' src='GUID-08CF5FC1-96C0-4815-8080-ED03AF3CAFA4-a5.gif']

#### Typical Full-Duplex System

Parent topic:

Duplex Architectures

<!--NI_TOPIC bundle=ni-serial path=general-programming-requirements.html language=enus -->
## TOPIC 00012: General Programming Requirements

- bundle_id: `ni-serial`
- source_path: `general-programming-requirements.html`
- source_url: https://docs-be.ni.com/bundle/ni-serial/raw/resource/enus/general-programming-requirements.html
- document_id: `ni-serial`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI-Serial software for Windows is fully integrated into the standard Windows communications software. NI serial ports are used like any other Windows communications (COM) port. Windows has standard communication functions for use within Windows applications. When you develop your application, re

### General Programming Requirements

The NI-Serial software for Windows is fully integrated into the standard Windows
 communications software. NI serial ports are used like any other Windows communications
 (COM) port. Windows has standard communication functions for use within Windows
 applications.

When you develop your application, remember that you must use the standard Windows serial
 communication functions or any API that uses the standard Windows serial communication
 functions such as NI-VISA. For more information about NI-VISA, see
 ni.com/VISA. For information about Microsoft Windows serial
 communication functions, refer to the Platform Software Development
 Kit.

If you have LabVIEW, LabWindows/CVI, or VISA and want to use it with your serial
 hardware, refer to your LabVIEW, LabWindows/CVI, or VISA documentation for information
 about serial I/O functions.

<!--NI_TOPIC bundle=ni-serial path=half-duplex.html language=enus -->
## TOPIC 00013: Half Duplex

- bundle_id: `ni-serial`
- source_path: `half-duplex.html`
- source_url: https://docs-be.ni.com/bundle/ni-serial/raw/resource/enus/half-duplex.html
- document_id: `ni-serial`
- page_type: `leaf`
- content_type: `concept`
- source_description: A typical half-duplex multidrop bus architecture also involves a master-slave protocol. However, in a half-duplex system, all transmitters and receivers are connected to the same transmission line. A half-duplex system is often referred to as a two-wire system. The following figure shows a typical h

### Half Duplex

A typical half-duplex multidrop bus architecture also involves a master-slave protocol.
 However, in a half-duplex system, all transmitters and receivers are connected to the
 same transmission line. A half-duplex system is often referred to as a two-wire system.
 The following figure shows a typical half-duplex system.

[IMAGE alt='image' src='GUID-EDF36C60-DEF6-44ED-9A04-A03291B39A4B-a5.gif']

#### Typical Half-Duplex System

Parent topic:

Duplex Architectures

<!--NI_TOPIC bundle=ni-serial path=hardware-implemented-flow-control.html language=enus -->
## TOPIC 00014: Hardware Implemented Flow Control

- bundle_id: `ni-serial`
- source_path: `hardware-implemented-flow-control.html`
- source_url: https://docs-be.ni.com/bundle/ni-serial/raw/resource/enus/hardware-implemented-flow-control.html
- document_id: `ni-serial`
- page_type: `leaf`
- content_type: `concept`
- source_description: Serial flow control mechanisms are described with varying terminology. Flow control can be in band, meaning that special characters are sent across the serial line to control the flow, or out of band, meaning that extra physical wires are used for flow control. Typically, in-band flow control is ref

### Hardware Implemented Flow Control

Serial flow control mechanisms are described with varying terminology. Flow control can
 be in band, meaning that special characters are sent across the
 serial line to control the flow, or out of band, meaning that extra
 physical wires are used for flow control. Typically, in-band flow control is referred to
 as software flow control, and out-of-band flow control is referred to
 as hardware flow control.

Although in-band and out-of-band flow control are often referred to as software and
 hardware flow control, you can implement them either by driver software or directly in
 the serial hardware. NI-Serial implements flow control in both the driver and hardware,
 depending on the hardware capabilities.

#### Driver Implemented Flow Control

Driver implemented flow control relies on the driver software to detect flow control
 events and signal for the other end of the connection to halt the flow of data. The
 performance of driver implemented flow control varies with the speed and CPU load of
 the system being used, and in some cases the driver cannot prevent hardware FIFO
 overruns.

#### Hardware Implemented Flow Control

Hardware implemented flow control performs all flow control functionality in the
 serial hardware, without the latency of waiting for action from the serial driver.
 This allows for more reliable flow control operation, even on busy systems.

<!--NI_TOPIC bundle=ni-serial path=how-can-i-change-the-com-numbers-of-my-nation.html language=enus -->
## TOPIC 00015: How can I change the COM numbers of my National Instruments serial ports?

- bundle_id: `ni-serial`
- source_path: `how-can-i-change-the-com-numbers-of-my-nation.html`
- source_url: https://docs-be.ni.com/bundle/ni-serial/raw/resource/enus/how-can-i-change-the-com-numbers-of-my-nation.html
- document_id: `ni-serial`
- page_type: `leaf`
- content_type: `concept`
- source_description: Select a new COM number from the COM Port Number control of the Advanced MAX tab and click Save.

### How can I change the COM numbers of my National Instruments serial ports?

Select a new COM number from the COM Port Number control of the Advanced MAX tab and click Save.

Related concepts:

- Serial Port Settings

<!--NI_TOPIC bundle=ni-serial path=how-can-i-determine-whether-my-hardware-and-s.html language=enus -->
## TOPIC 00016: How can I determine whether my hardware and software are installed properly?

- bundle_id: `ni-serial`
- source_path: `how-can-i-determine-whether-my-hardware-and-s.html`
- source_url: https://docs-be.ni.com/bundle/ni-serial/raw/resource/enus/how-can-i-determine-whether-my-hardware-and-s.html
- document_id: `ni-serial`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the NI-Serial Troubleshooting Wizard. This wizard verifies that your serial hardware and the NI-Serial software are installed correctly and working properly.

### How can I determine whether my hardware and software are installed properly?

Use the NI-Serial Troubleshooting Wizard. This wizard verifies that your serial hardware
 and the NI-Serial software are installed correctly and working properly.

<!--NI_TOPIC bundle=ni-serial path=how-can-i-determine-which-port-is-associated.html language=enus -->
## TOPIC 00017: How can I determine which port is associated with COMx?

- bundle_id: `ni-serial`
- source_path: `how-can-i-determine-which-port-is-associated.html`
- source_url: https://docs-be.ni.com/bundle/ni-serial/raw/resource/enus/how-can-i-determine-which-port-is-associated.html
- document_id: `ni-serial`
- page_type: `leaf`
- content_type: `concept`
- source_description: To determine which physical port is associated with COMx, complete the following steps: Launch MAX. Expand the My System directory by clicking the + next to the folder. Expand the Devices and Interfaces directory by clicking on the + next to the folder. MAX lists your installed serial hardware under

### How can I determine which port is associated with COMx?

To determine which physical port is associated with COMx, complete the
 following steps:

1. Launch MAX.
2. Expand the My System directory by clicking the
 + next to the folder.
3. Expand the Devices and Interfaces directory by clicking on
 the + next to the folder. MAX lists your installed serial hardware under
 Devices and Interfaces .
4. Click your serial interface in the device tree. The right window displays
 information on what COM number is associated with each physical port on your serial
 interface.

<!--NI_TOPIC bundle=ni-serial path=how-can-i-determine-which-type-of-serial-hard.html language=enus -->
## TOPIC 00018: How can I determine which type of serial hardware I have installed?

- bundle_id: `ni-serial`
- source_path: `how-can-i-determine-which-type-of-serial-hard.html`
- source_url: https://docs-be.ni.com/bundle/ni-serial/raw/resource/enus/how-can-i-determine-which-type-of-serial-hard.html
- document_id: `ni-serial`
- page_type: `leaf`
- content_type: `concept`
- source_description: To view the serial hardware installed on your Windows system, complete the following steps: Launch MAX. Expand the My System directory by clicking the + next to the folder. Expand the Devices and Interfaces directory by clicking on the + next to the folder. MAX lists your installed serial hardware u

### How can I determine which type of serial hardware I have installed?

To view the serial hardware installed on your Windows system, complete the following
 steps:

1. Launch MAX.
2. Expand the My System directory by clicking the
 + next to the folder.
3. Expand the Devices and Interfaces directory by clicking on
 the + next to the folder. MAX lists your installed serial hardware under
 Devices and Interfaces .

To view the serial hardware installed on your LabVIEW Real-Time controller, complete the
 following steps:

1. Launch MAX.
2. Expand Remote Systems by clicking the
 + next to the folder.
3. Find your RT controller in the list and expand it.
4. Expand the Devices and Interfaces directory.
5. Expand the Serial entry. MAX lists your installed serial
 hardware under Serial .

<!--NI_TOPIC bundle=ni-serial path=how-can-i-determine-which-version-of-the-ni-serial-installed.html language=enus -->
## TOPIC 00019: How can I determine which version of the NI-Serial software I have installed?

- bundle_id: `ni-serial`
- source_path: `how-can-i-determine-which-version-of-the-ni-serial-installed.html`
- source_url: https://docs-be.ni.com/bundle/ni-serial/raw/resource/enus/how-can-i-determine-which-version-of-the-ni-serial-installed.html
- document_id: `ni-serial`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use MAX to view your NI-Serial software version.

### How can I determine which version of the NI-Serial software I have installed?

You can use MAX to view your NI-Serial software version.

Related concepts:

- View NI-Serial Software Version

<!--NI_TOPIC bundle=ni-serial path=how-can-i-repair-my-ni-serial-software.html language=enus -->
## TOPIC 00020: How can I repair my NI-Serial software?

- bundle_id: `ni-serial`
- source_path: `how-can-i-repair-my-ni-serial-software.html`
- source_url: https://docs-be.ni.com/bundle/ni-serial/raw/resource/enus/how-can-i-repair-my-ni-serial-software.html
- document_id: `ni-serial`
- page_type: `leaf`
- content_type: `concept`
- source_description: To repair the NI-Serial software, complete the following steps: Select Start»Control Panel. On Windows XP/Server 2003, double-click the Add/Remove Programs icon. On Windows Vista, double-click the Programs and Features icon. On Windows 7/Server 2008, click Uninstall a Program. Select National Instru

### How can I repair my NI-Serial software?

To repair the NI-Serial software, complete the following steps:

1. Select Start»Control Panel .
2. On Windows XP/Server 2003, double-click the Add/Remove
 Programs icon. On Windows Vista, double-click the
 Programs and Features icon. On Windows 7/Server 2008,
 click Uninstall a Program .
3. Select National Instruments Software in the list and click
 the Change/Remove button on Windows XP/Server 2003 or the
 Uninstall/Change button on Windows 7/Vista/Server
 2008.
4. Select the software components you want to repair and click the
 Repair button. The repair checks all utilities and
 registry entries associated with the NI-Serial software and repairs or replaces
 files as necessary.
5. Restart the computer to complete the repair process.
6. Use the NI-Serial Troubleshooting Wizard to verify that your software has been
 repaired and is working properly.

<!--NI_TOPIC bundle=ni-serial path=how-do-i-force-windows-to-detect-my-pci.html language=enus -->
## TOPIC 00021: How do I force Windows to detect my PCI, PCI Express, PXI, or PXI Express hardware?

- bundle_id: `ni-serial`
- source_path: `how-do-i-force-windows-to-detect-my-pci.html`
- source_url: https://docs-be.ni.com/bundle/ni-serial/raw/resource/enus/how-do-i-force-windows-to-detect-my-pci.html
- document_id: `ni-serial`
- page_type: `leaf`
- content_type: `concept`
- source_description: If the ports on your hardware do not show up in MAX or the Windows Device Manager, complete the following steps: Select Start»Control Panel and double-click the System icon. Select the Hardware tab and click the Device Manager button. Double-click the NI-Serial Peripherals icon. From the NI-Serial P

### How do I force Windows to detect my PCI, PCI Express, PXI, or PXI Express
 hardware?

If the ports on your hardware do not show up in MAX or the Windows Device Manager,
 complete the following steps:

1. Select Start»Control Panel and double-click the
 System icon.
2. Select the Hardware tab and click the Device
 Manager button.
3. Double-click the NI-Serial Peripherals icon.
4. From the NI-Serial Peripherals list, right-click any National
 Instruments interface that was not properly detected.
5. Choose the Uninstall option.
6. In the Confirm Device Removal dialog box, click the
 OK button to remove the hardware information.
7. Click the Scan for Hardware Changes icon at the top of the
 Device Manager window.
8. Windows should automatically detect your hardware.

<!--NI_TOPIC bundle=ni-serial path=how-do-i-force-windows-to-detect-my-usb-or-ex.html language=enus -->
## TOPIC 00022: How do I force Windows to detect my USB or ExpressCard hardware?

- bundle_id: `ni-serial`
- source_path: `how-do-i-force-windows-to-detect-my-usb-or-ex.html`
- source_url: https://docs-be.ni.com/bundle/ni-serial/raw/resource/enus/how-do-i-force-windows-to-detect-my-usb-or-ex.html
- document_id: `ni-serial`
- page_type: `leaf`
- content_type: `concept`
- source_description: If the ports on your hardware do not show up in MAX or the Windows Device Manager, complete the following steps: Select Start»Control Panel and double-click the System icon. Select the Hardware tab and click the Device Manager button. The Device Manager window should appear as shown below. Double-cl

### How do I force Windows to detect my USB or ExpressCard hardware?

If the ports on your hardware do not show up in MAX or the Windows Device Manager,
 complete the following steps:

1. Select Start»Control Panel and double-click the
 System icon.
2. Select the Hardware tab and click the Device
 Manager button. The Device Manager window should appear as shown
 below.
3. Double-click the Ports (COM & LPT) icon. Verify that all
 USB and ExpressCard serial communication ports are displayed without exclamation
 marks (!). If any USB or ExpressCard serial port has an exclamation mark,
 right-click the port and select Uninstall .
4. In the Device Manager menu bar, select
 View . In the View menu, select
 Show Hidden Devices .
5. A new device category named NI-Serial USB/ExpressCard perf 
 should now be present. Expand this entry and verify that no devices in this list
 have exclamation marks (!). If one or more devices has an exclamation mark,
 right-click the device and select Uninstall .
6. Click the Scan for Hardware Changes icon at the top of the
 Device Manager window.
7. Windows should automatically detect your hardware.
8. If any of your serial ports are still not visible, disconnect and reconnect the USB
 or ExpressCard serial hardware to a different USB port and return to step 2.

<!--NI_TOPIC bundle=ni-serial path=how-do-i-resolve-serial-usb-power-conflicts.html language=enus -->
## TOPIC 00023: How do I resolve serial USB power conflicts?

- bundle_id: `ni-serial`
- source_path: `how-do-i-resolve-serial-usb-power-conflicts.html`
- source_url: https://docs-be.ni.com/bundle/ni-serial/raw/resource/enus/how-do-i-resolve-serial-usb-power-conflicts.html
- document_id: `ni-serial`
- page_type: `leaf`
- content_type: `concept`
- source_description: The USB-232, USB-232/2, USB-232/4, USB-485, and USB-485/2 are high- power bus-powered devices that require more than 100 mA during normal operation. Thus, they must be plugged into an externally powered hub that can deliver up to 500 mA per USB port. If the USB network does not have enough power to

### How do I resolve serial USB power conflicts?

The USB-232, USB-232/2, USB-232/4, USB-485, and USB-485/2 are high-
 power bus-powered devices that require more than 100 mA during normal
 operation. Thus, they must be plugged into an externally powered hub that can deliver up
 to 500 mA per USB port. If the USB network does not have enough power to support the USB
 serial hardware, and a system dialog box informs you that there is not enough power for
 the device, reconnect the hardware to an externally powered hub.

The USB-485/4 is a self-powered device that requires external power. If the device is
 plugged into a USB port, and the device does not have power, it will not enumerate and
 the ports will not show in the Device Manager. To ensure proper port enumeration, always
 make sure the USB-485/4 has external power before connecting it to the USB network.

<!--NI_TOPIC bundle=ni-serial path=how-do-i-troubleshoot-problems.html language=enus -->
## TOPIC 00024: How do I troubleshoot problems?

- bundle_id: `ni-serial`
- source_path: `how-do-i-troubleshoot-problems.html`
- source_url: https://docs-be.ni.com/bundle/ni-serial/raw/resource/enus/how-do-i-troubleshoot-problems.html
- document_id: `ni-serial`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the NI-Serial Troubleshooting Wizard. This wizard verifies that your serial hardware and the NI-Serial software are installed correctly and working properly.

### How do I troubleshoot problems?

Use the NI-Serial Troubleshooting Wizard. This wizard verifies that your serial hardware
 and the NI-Serial software are installed correctly and working properly.

<!--NI_TOPIC bundle=ni-serial path=how-do-i-use-9-data-bit-framing.html language=enus -->
## TOPIC 00025: How do I use 9 data bit framing?

- bundle_id: `ni-serial`
- source_path: `how-do-i-use-9-data-bit-framing.html`
- source_url: https://docs-be.ni.com/bundle/ni-serial/raw/resource/enus/how-do-i-use-9-data-bit-framing.html
- document_id: `ni-serial`
- page_type: `leaf`
- content_type: `concept`
- source_description: While NI-Serial software and hardware directly supports only 5, 6, 7, and 8 data bits, it may be possible to use the parity function to create a ninth data bit, depending on your application. To create and control a ninth data bit, enable parity and set parity mark or parity space for a ninth bit of

### How do I use 9 data bit framing?

While NI-Serial software and hardware directly supports only 5, 6, 7, and 8 data bits, it
 may be possible to use the parity function to create a ninth data bit, depending on your
 application. To create and control a ninth data bit, enable parity and set parity mark
 or parity space for a ninth bit of either a 1 or 0, respectively. However, you must do
 this every time the ninth bit changes state, and thus it may not work for
 high-throughput applications.

<!--NI_TOPIC bundle=ni-serial path=how-many-interrupts-are-required-for-my-seria.html language=enus -->
## TOPIC 00026: How many interrupts are required for my serial interface?

- bundle_id: `ni-serial`
- source_path: `how-many-interrupts-are-required-for-my-seria.html`
- source_url: https://docs-be.ni.com/bundle/ni-serial/raw/resource/enus/how-many-interrupts-are-required-for-my-seria.html
- document_id: `ni-serial`
- page_type: `leaf`
- content_type: `concept`
- source_description: If you have a shared IRQ board or an isolated board, you need one interrupt per board. Serial ENET and serial USB interfaces do not require interrupts.

### How many interrupts are required for my serial interface?

If you have a shared IRQ board or an isolated board, you need one interrupt per
 board.

Serial ENET and serial USB interfaces do not require interrupts.

<!--NI_TOPIC bundle=ni-serial path=how-many-serial-ports-can-i-have-on-my-machine.html language=enus -->
## TOPIC 00027: How many serial ports can I have on my machine?

- bundle_id: `ni-serial`
- source_path: `how-many-serial-ports-can-i-have-on-my-machine.html`
- source_url: https://docs-be.ni.com/bundle/ni-serial/raw/resource/enus/how-many-serial-ports-can-i-have-on-my-machine.html
- document_id: `ni-serial`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can have up to 256 serial ports.

### How many serial ports can I have on my machine?

You can have up to 256 serial ports.

<!--NI_TOPIC bundle=ni-serial path=launching-max.html language=enus -->
## TOPIC 00028: Launching MAX

- bundle_id: `ni-serial`
- source_path: `launching-max.html`
- source_url: https://docs-be.ni.com/bundle/ni-serial/raw/resource/enus/launching-max.html
- document_id: `ni-serial`
- page_type: `leaf`
- content_type: `concept`
- source_description: To start MAX, double-click the MAX icon on the desktop or select Start >> NI MAX. (Windows 8). Click NI Launcher and select Measurement > Automation. To make changes to serial port settings, you must launch MAX with administrative privileges. To launch MAX with administrative privileges, right-click

### Launching MAX

To start MAX, double-click the MAX icon on the desktop or select Start >>
 NI MAX. (Windows 8). Click NI Launcher and select
 Measurement > Automation.

To make changes to serial port settings, you must launch MAX with administrative
 privileges. To launch MAX with administrative privileges, right-click the MAX icon on
 the desktop or the Start menu and select More >>
 Run as administrator. You must enter an administrative password if you
 are not an administrator.

<!--NI_TOPIC bundle=ni-serial path=max-overview.html language=enus -->
## TOPIC 00029: MAX Overview

- bundle_id: `ni-serial`
- source_path: `max-overview.html`
- source_url: https://docs-be.ni.com/bundle/ni-serial/raw/resource/enus/max-overview.html
- document_id: `ni-serial`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can perform the following serial-related tasks in MAX: Establish basic communication with your serial devices. Launch the NI-Serial Troubleshooter to verify installation and troubleshoot serial problems (Windows only). Launch NI I/O Trace to monitor NI-VISA API calls to serial interfaces(Windows

### MAX Overview

- Establish basic communication with your serial devices.
- Launch the NI-Serial Troubleshooter to verify installation and troubleshoot
 serial problems (Windows only).
- Launch NI I/O Trace to monitor NI-VISA API calls to serial interfaces(Windows
 only).
- View information about your serial hardware and NI-Serial software.
- Reconfigure the serial interface settings.
- Locate additional help resources for NI-Serial.

<!--NI_TOPIC bundle=ni-serial path=monitor-record-and-display-ni-visa.html language=enus -->
## TOPIC 00030: NI I/O Trace

- bundle_id: `ni-serial`
- source_path: `monitor-record-and-display-ni-visa.html`
- source_url: https://docs-be.ni.com/bundle/ni-serial/raw/resource/enus/monitor-record-and-display-ni-visa.html
- document_id: `ni-serial`
- page_type: `leaf`
- content_type: `concept`
- source_description: NI I/O Trace is used to monitor, record, and display NI-VISA API calls. NI I/O Trace is available only on Windows. To monitor NI-VISA calls, use NI I/O Trace as follows: Launch MAX. Expand the My System directory by clicking the + next to the folder. Expand the Devices and Interfaces directory by cl

### NI I/O Trace

NI I/O Trace is used to monitor, record, and display NI-VISA API calls. NI I/O Trace is
 available only on Windows.

1. Launch MAX .
2. Expand the My System directory by clicking the
 + next to the folder.
3. Expand the Devices and Interfaces directory by clicking
 the + next to the folder.
4. Right-click on your serial interface and select NI I/O
 Trace from the drop-down menu that appears.
5. On the NI I/O Trace toolbar, click the green arrow button to start a
 capture.
6. Start the NI-VISA application you want to monitor.

NI I/O Trace records and displays all NI-VISA calls.

For more information about using NI I/O Trace, select Help >> Help
 Topics in NI I/O Trace.

<!--NI_TOPIC bundle=ni-serial path=new-features-and-changes.html language=enus -->
## TOPIC 00031: NI-Serial New Features and Changes

- bundle_id: `ni-serial`
- source_path: `new-features-and-changes.html`
- source_url: https://docs-be.ni.com/bundle/ni-serial/raw/resource/enus/new-features-and-changes.html
- document_id: `ni-serial`
- page_type: `leaf`
- content_type: `concept`
- source_description: Learn about updates, including new features and behavior changes, introduced in each version of NI-Serial. Discover what is new in the latest releases of NI-Serial.If you cannot find new features and changes for your version, it might not include user-facing updates. However, your version might incl

### NI-Serial
 New Features and Changes

Learn about updates, including new features and behavior changes, introduced in each
 version of NI-Serial.

NI-Serial

Note

Release Notes

Related information:

- Software and Driver Downloads

#### NI-Serial
 2025 Q4 Changes

Learn about new features, behavior changes, and other updates in NI-Serial 2025 Q4.

##### New
 Features and Changes

This version of NI-Serial
 provides support for the following features:

- Added support for Red Hat Enterprise Linux 9.6.
- Ended support for Red Hat Enterprise Linux 9.4.
- Ended support for Windows Server 2019.

#### NI-Serial
 2023 Q4 Changes

Learn about new features, behavior changes, and other updates in NI-Serial 2023 Q4.

##### New
 Features

This version of the NI-Serial
 provides support for the following features:

- NI Hardware Configuration Utility is now installed as a part of NI-Serial.
- Bug fixes for NI Linux Real-Time to address issues and improve overall
 performance.
- Incorporation of an extra configuration file designed to house default settings
 for NI-Serial, which will be utilized when integrating new hardware.
- In the Windows Device Manager, the identified serial ports will not display the
 serial number that is linked to the corresponding NI-Serial device. Similarly,
 when using the NI-Serial Troubleshooter, the list of verified serial ports will
 not exhibit the serial number within the Port Description. Nevertheless, users
 can utilize NI-MAX for the purpose of associating COM port numbers with their
 respective NI-Serial devices.
- Starting from kernel version 5.15.79, the following RS-485 transceiver modes are
 no longer maintained:
  1. 2-Wire DTR
  2. 2-Wire DTR with echo

<!--NI_TOPIC bundle=ni-serial path=pci-and-pci-express-hardware-installation.html language=enus -->
## TOPIC 00032: PCI and PCI Express Hardware Installation

- bundle_id: `ni-serial`
- source_path: `pci-and-pci-express-hardware-installation.html`
- source_url: https://docs-be.ni.com/bundle/ni-serial/raw/resource/enus/pci-and-pci-express-hardware-installation.html
- document_id: `ni-serial`
- page_type: `leaf`
- content_type: `concept`
- source_description: If you are installing a PCI or PCI Express RS-485 interface, you might need to adjust the value of the bias resistors, depending on your application. Bias resistors are not available on eight-port or 16-port PCI hardware. For more information, refer to Bias Resistors. Before you remove your boar

### PCI and PCI Express Hardware Installation

Note

Caution

Before installing your hardware, follow the NI-Serial Software Installation
 instructions.

To install your PCI or PCI Express serial board, complete the following steps:

1. Turn off your computer. Keep the computer plugged in so that it remains grounded
 while you install the PCI or PCI Express serial board.
2. Remove the top or side cover of the computer.
3. Find an unused PCI or PCI Express expansion slot in your computer.
4. Remove the corresponding expansion slot cover on the back panel of the
 computer.
5. Touch a metal part on your chassis to discharge any static electricity.
6. Insert the PCI or PCI Express serial board into the slot with the serial connectors
 toward the opening on the back panel. Make sure that you insert the board all the
 way into the slot. The following figures show how to install the PCI or PCI Express
 serial board into an expansion slot. [IMAGE alt='image' src='GUID-8948A131-1265-45C2-852A-923CBD5A229A-a5.gif']

[IMAGE alt='image' src='GUID-A0EC0E2B-78E1-477A-AD7A-8E2261BBCE33-a5.gif']
1 PCI Serial Board2 PCI Slot3 PC

1 PCI Express Serial Board2 PCI Express Slot3 PC

#### PCI and PCI Express Serial Board Installation

1. Screw the PCI or PCI Express serial board mounting bracket to the back panel
 
 mounting rail of the computer.
2. Replace the cover.
3. Turn on your computer.
4. The operating system will automatically detect your hardware.

The serial hardware installation is complete. Continue to Verify the Installation.

Related concepts:

- Bias Resistors

<!--NI_TOPIC bundle=ni-serial path=performance-on-labview-real-time.html language=enus -->
## TOPIC 00033: Performance on LabVIEW Real-Time

- bundle_id: `ni-serial`
- source_path: `performance-on-labview-real-time.html`
- source_url: https://docs-be.ni.com/bundle/ni-serial/raw/resource/enus/performance-on-labview-real-time.html
- document_id: `ni-serial`
- page_type: `leaf`
- content_type: `concept`
- source_description: NI-Serial users on LabVIEW Real-Time have control over whether secondary interrupt handling is enabled. When secondary interrupt handling is enabled, I/O is processed at a priority lower than time-critical. Using secondary interrupt handling reduces jitter for time-critical loops and makes serial ha

### Performance on LabVIEW Real-Time

NI-Serial users on LabVIEW Real-Time have control over whether secondary interrupt
 handling is enabled. When secondary interrupt handling is enabled, I/O is processed at a
 priority lower than time-critical. Using secondary interrupt handling reduces jitter for
 time-critical loops and makes serial hardware interrupts more deterministic. However, it
 may also reduce I/O performance and can increase the possibility of overflowing the RX
 FIFO buffer. Secondary interrupt handling is a setting at the system-wide level and is
 enabled by default.

To enable or disable this feature, complete the following steps:

1. Copy to your host the niserial.dbs file in the
 /ni-rt/system directory on the RT target.
2. In the niserial.dbs file, find the entry
 SecondaryInterrupts and modify it accordingly:
  - To enable secondary interrupt handling, set
 SecondaryInterrupts to 1.
  - To disable secondary interrupt handling, set
 SecondaryInterrupts to 0.
3. Download the updated niserial.dbs file to the target, overwriting
 the existing file in the /ni-rt/system directory.
4. Reboot your RT target.

<!--NI_TOPIC bundle=ni-serial path=pxi-and-pxi-express-hardware-installation.html language=enus -->
## TOPIC 00034: PXI and PXI Express Hardware Installation

- bundle_id: `ni-serial`
- source_path: `pxi-and-pxi-express-hardware-installation.html`
- source_url: https://docs-be.ni.com/bundle/ni-serial/raw/resource/enus/pxi-and-pxi-express-hardware-installation.html
- document_id: `ni-serial`
- page_type: `leaf`
- content_type: `concept`
- source_description: A PXI Express card can be installed in the same way as a PXI card. A mechanical key will prevent the insertion of a PXI Express card into an incompatible slot. Before you remove your board from the package, touch the antistatic plastic package to a metal part of your system chassis to discharge el

### PXI and PXI Express Hardware Installation

|  | A PXI Express card can be installed in the same way as a PXI card. A mechanical key will prevent the insertion of a PXI Express card into an incompatible slot. |
| --- | --- |

Caution

Before installing your hardware, follow the NI-Serial Software Installation
 instructions.

To install your PXI or PXI Express serial board, complete the following steps:

1. Turn off your PXI, PXI Express, or CompactPCI chassis. Keep the chassis plugged in
 so that it remains grounded while you install the PXI or PXI Express serial
 board.
2. Find an unused PXI, PXI Express, or CompactPCI peripheral slot.
3. Remove the corresponding filler panel.
4. Touch a metal part on your chassis to discharge any static electricity.
5. Insert the PXI or PXI Express serial board into the slot. Use the injector/ejector
 handle to fully inject the device into place. The following figure shows how to
 install a PXI serial board into a PXI or CompactPCI chassis. A PXI Express card
 would be installed into a PXI Express chassis in the same way. [IMAGE alt='image' src='GUID-BBC4BF3E-5EB8-434F-8F81-F871723468D9-a5.gif'] 
 1
Injector/Ejector Handle (In Down Position)
2
PXI Serial Board
3
PXI Chassis
4
Injector/Ejector Rail

#### Installing the PXI Serial Board

1. Screw the PXI or PXI Express serial board front panel to the front panel mounting
 rail of the PXI, PXI Express, or CompactPCI chassis.
2. Turn on your PXI, PXI Express, or CompactPCI chassis.
3. The operating system will automatically detect your hardware.

The serial hardware installation is complete. Continue to Verify the Installation.

<!--NI_TOPIC bundle=ni-serial path=recover-unused-com-numbers.html language=enus -->
## TOPIC 00035: Recover Unused COM Numbers

- bundle_id: `ni-serial`
- source_path: `recover-unused-com-numbers.html`
- source_url: https://docs-be.ni.com/bundle/ni-serial/raw/resource/enus/recover-unused-com-numbers.html
- document_id: `ni-serial`
- page_type: `leaf`
- content_type: `concept`
- source_description: When serial hardware is physically removed from a Windows system without first being deleted from the operating system, Windows continues to mark the COM numbers associated with that hardware as in use. This allows you to reinsert the hardware and have those ports keep their original COM numbers. To

### Recover Unused COM Numbers

When serial hardware is physically removed from a Windows system without first being
 deleted from the operating system, Windows continues to mark the COM numbers associated
 with that hardware as in use. This allows you to reinsert the
 hardware and have those ports keep their original COM numbers.

1. Launch MAX .
2. Select Tool>>NI-Serial>>Recover Unused COM
 Numbers .

<!--NI_TOPIC bundle=ni-serial path=retrieving-the-rs-232-transceiver-state.html language=enus -->
## TOPIC 00036: Retrieving the RS-232 Transceiver State

- bundle_id: `ni-serial`
- source_path: `retrieving-the-rs-232-transceiver-state.html`
- source_url: https://docs-be.ni.com/bundle/ni-serial/raw/resource/enus/retrieving-the-rs-232-transceiver-state.html
- document_id: `ni-serial`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI-Serial software returns which mode the RS-232 transceivers are currently operating in, and whether the serial connection is valid. Transceiver mode refers to the programmed mode. Transceiver state refers to the physical state of the transceivers (actual operating mode and whether valid or i

### Retrieving the RS-232 Transceiver State

The NI-Serial software returns which mode the RS-232 transceivers are currently operating
 in, and whether the serial connection is valid.

Note

Transceiver mode

Transceiver state

There are two ways to retrieve the RS-232 transceiver state and tranceiver mode:

- Read the NI-VISA wire mode attribute to retrieve the transceiver state and the NI-VISA
 IsPortConnected attribute to retrieve the transceiver mode.
- The NI-Serial software uses programmatic control codes and the DeviceIoControl Windows
 function to retrieve the RS-232 transceiver state and transceiver mode.

To retrieve the RS-232 transceiver state using the DeviceIoControl Windows function,
 complete the following steps:

1. Add the following lines to your source code: #include <winioctl.h>
#include <NiSerial.h> 
 Note The header file NiSerial.h is included on your
 NI-Serial software CD. You also can find it in the NI-Serial folder
 where you installed your National Instruments software (typically, C:\Program
 Files\National Instruments\NI-Serial).
2. The RS-232 transceiver state attribute is contained within a struct of type
 SERIAL_RS232_STATE . The struct members and possible values are shown
 below: Member Name
Values
PortMode
RS232_MODE_DTE RS232_MODE_DCE RS232_MODE_AUTO
Connection
SERIAL_CONNECTION_INVALID SERIAL_CONNECTION_VALID
3. To retrieve the current RS-232 transceiver state, use
 NISERIAL_GET_RS232_STATE and DeviceIoControl with the following
 code:
 SERIAL_RS232_STATE l_SerialRs232State;
DWORD l_ByteCount;
DeviceIoControl (
 PortHandle,
 NISERIAL_GET_RS232_STATE,
 (LPVOID) NULL,
 0,
 (LPVOID) &l_SerialRs232State,
 sizeof (l_SerialRs232State),
 (LPDWORD) &l_ByteCount,
 NULL
 );

<!--NI_TOPIC bundle=ni-serial path=retrieving-the-serial-interface-type.html language=enus -->
## TOPIC 00037: Retrieving the Serial Interface Type

- bundle_id: `ni-serial`
- source_path: `retrieving-the-serial-interface-type.html`
- source_url: https://docs-be.ni.com/bundle/ni-serial/raw/resource/enus/retrieving-the-serial-interface-type.html
- document_id: `ni-serial`
- page_type: `leaf`
- content_type: `concept`
- source_description: There are two ways to retrieve the serial interface type (RS-232 or RS-485): Read the NI-VISA wire mode attribute. The NI-Serial software uses programmatic control codes and the DeviceIoControl Windows function to retrieve the serial interface type. To retrieve the serial interface type using the De

### Retrieving the Serial Interface Type

There are two ways to retrieve the serial interface type (RS-232 or RS-485):

- Read the NI-VISA wire mode attribute.
- The NI-Serial software uses programmatic control codes and the DeviceIoControl Windows
 function to retrieve the serial interface type.

To retrieve the serial interface type using the DeviceIoControl Windows function, complete
 the following steps:

1. Add the following lines to your source code: #include <winioctl.h>
#include <NiSerial.h> 
 Note The header file NiSerial.h is included on your
 NI-Serial software CD. You also can find it in the NI-Serial folder
 where you installed your National Instruments software (typically, C:\Program
 Files\National Instruments\NI-Serial).
2. The SERIAL_INTERFACE attribute can have the following values:
  - RS485_INTERFACE
  - RS232_INTERFACE
3. To retrieve the serial interface type, use NISERIAL_GET_INTERFACE_TYPE 
 and DeviceIoControl with the following code:
 SERIAL_INTERFACE l_SerialInterface;
DWORD l_ByteCount;
DeviceIoControl (
 PortHandle,
 NISERIAL_GET_INTERFACE_TYPE,
 (LPVOID) NULL,
 0,
 (LPVOID) &l_SerialInterface,
 sizeof (l_SerialInterface),
 (LPDWORD) &l_ByteCount,
 NULL
 );

<!--NI_TOPIC bundle=ni-serial path=rs-232-dte-versus-dce.html language=enus -->
## TOPIC 00038: RS-232 DTE versus DCE

- bundle_id: `ni-serial`
- source_path: `rs-232-dte-versus-dce.html`
- source_url: https://docs-be.ni.com/bundle/ni-serial/raw/resource/enus/rs-232-dte-versus-dce.html
- document_id: `ni-serial`
- page_type: `leaf`
- content_type: `concept`
- source_description: In the RS-232 specification, DTE (Data Terminal Equipment) and DCE (Data Communications Equipment) refer to the types of equipment on either end of a serial connection. In general, DTE and DCE refer to computer equipment and modems, respectively. Because the RS-232 specification mainly involves conn

### RS-232 DTE versus DCE

In the RS-232 specification, DTE (Data Terminal Equipment) and DCE (Data Communications
 Equipment) refer to the types of equipment on either end of a serial connection. In
 general, DTE and DCE refer to computer equipment and modems, respectively. Because the
 RS-232 specification mainly involves connecting a DTE directly to a DCE and vice versa,
 the pinouts are defined so that cabling is simple. That is, a cable connected a computer
 to a modem by wiring pin 1 to pin 1, pin 2 to pin 2, and so on. This method is known as
 straight-through cabling.

The following figure shows straight-through cabling in a DTE-to-DCE interface.

[IMAGE alt='image' src='GUID-531C80D7-4CD4-4546-8EA5-E8C5300BE893-a5.svg']

#### Straight-Through Cabling in a DTE-to-DCE Interface

Straight-through cabling is still the standard method to connect a modem to your PC.
 However, because many applications use serial communication to connect two or more
 DTEs without modems, the cabling becomes more complicated. If two DTEs are wired
 together using a straight-through cable, one transmitter is connected to the other
 transmitter, and one receiver is connected to the other receiver. In this setup, no
 transmissions can occur. Thus, these applications must use a cabling scheme that
 connects the transmitter on one device to the receiver on the other device and vice
 versa. This method is known as null-modem cabling, because it
 replaces the two modems that traditional RS-232 applications would require between
 the two DTEs. To communicate from one DTE serial port to another, use a null-modem
 cable.

The following figure shows null-modem cabling in a DTE-to-DTE interface.

[IMAGE alt='image' src='GUID-DC826CA1-8642-4500-8CAF-DFA255010A3A-a5.svg']

#### Null-Modem Cabling in a DTE-to-DTE Interface

PCI, PCI Express, PXI, PXI Express, USB (one port only), ENET, and ExpressCard RS-232
 ports are DTE serial ports.

USB-232 (two and four port only) can be configured to DTE or DCE. Refer to USB-232 Transceiver Control for more information.

Parent topic:

Serial Communication Issues

Related concepts:

- USB-232 Transceiver Control

<!--NI_TOPIC bundle=ni-serial path=rs-232.html language=enus -->
## TOPIC 00039: RS-232

- bundle_id: `ni-serial`
- source_path: `rs-232.html`
- source_url: https://docs-be.ni.com/bundle/ni-serial/raw/resource/enus/rs-232.html
- document_id: `ni-serial`
- page_type: `leaf`
- content_type: `concept`
- source_description: As specified in the ANSI/EIA-232-D Standard, Interface Between Data Terminal Equipment and Data Circuit-Terminating Equipment Employing Serial Binary Data Interchange, RS-232 standardizes serial communication between computers and between computer terminals and modems. Many applications use the RS-2

### RS-232

As specified in the ANSI/EIA-232-D Standard, Interface Between Data Terminal
 Equipment and Data Circuit-Terminating Equipment Employing Serial Binary Data
 Interchange, RS-232 standardizes serial communication between computers
 and between computer terminals and modems. Many applications use the RS-232 standard to
 interface peripherals to personal computers. RS-232 uses transmission lines in which the
 state of each signal is represented by referencing the voltage level of a single line to
 ground. RS-232 was designed for serial communication up to distances of 50 ft and with
 data rates up to 20 kbytes/s. However, because of improvements in line drivers and
 cabling, it is possible to increase the actual performance of the bus past the
 limitations on speed and distance recommended in the specification.

Parent topic:

Serial Port Information Overview

<!--NI_TOPIC bundle=ni-serial path=rs-422.html language=enus -->
## TOPIC 00040: RS-422

- bundle_id: `ni-serial`
- source_path: `rs-422.html`
- source_url: https://docs-be.ni.com/bundle/ni-serial/raw/resource/enus/rs-422.html
- document_id: `ni-serial`
- page_type: `leaf`
- content_type: `concept`
- source_description: As specified in the EIA/RS-422-A Standard, Electrical Characteristics of Balanced Voltage Digital Interface Circuits, RS-422 defines a serial interface much like RS-232. However, RS-422 uses balanced (or differential) transmission lines. Balanced transmission lines use two transmission lines for eac

### RS-422

As specified in the EIA/RS-422-A Standard, Electrical Characteristics of
 Balanced Voltage Digital Interface Circuits, RS-422 defines a serial
 interface much like RS-232. However, RS-422 uses balanced (or differential) transmission
 lines. Balanced transmission lines use two transmission lines for each signal. The state
 of each signal is represented, not by a voltage level on one line referenced to ground
 as in RS-232, but rather by the relative voltage of the two lines to each other. For
 example, the TX signal is carried on two wires, wire A and wire B. A logical 1 is
 represented by the voltage on line A being greater than the voltage on line B. A logical
 0 is represented by the voltage on line A being less than the voltage on line B.
 Differential voltage transmission creates a signal that is more immune to noise as well
 as voltage loss due to transmission line effects. Thus, you can use RS-422 for longer
 distances (up to 4,000 ft) and greater transmission speeds (up to 10 Mbytes/s) than
 RS-232.

Parent topic:

Serial Port Information Overview

<!--NI_TOPIC bundle=ni-serial path=rs-485-termination.html language=enus -->
## TOPIC 00041: RS-485 Termination

- bundle_id: `ni-serial`
- source_path: `rs-485-termination.html`
- source_url: https://docs-be.ni.com/bundle/ni-serial/raw/resource/enus/rs-485-termination.html
- document_id: `ni-serial`
- page_type: `leaf`
- content_type: `concept`
- source_description: Because each differential pair of wires is a transmission line, you must properly terminate the line to prevent reflections. A common method of terminating a two-wire multidrop RS-485 network is to install terminating resistors at each end of the multidrop network. If you daisy-chained multiple inst

### RS-485 Termination

Because each differential pair of wires is a transmission line, you must properly
 terminate the line to prevent reflections. A common method of terminating a two-wire
 multidrop RS-485 network is to install terminating resistors at each end of the
 multidrop network. If you daisy-chained multiple instruments together, you need a
 terminating resistor at only the first and last instruments. The terminating resistor
 should match the characteristic impedance of the transmission line (typically 100 to 120
 [IMAGE alt='image' src='GUID-3D97CC5D-839F-4675-B3BF-F1B240D4C49D-a5.gif']). You can order an optional DB-9 RS-485 termination connector that
 contains embedded terminating resistors for easy termination from National Instruments.
 For ordering information, contact National Instruments.

The following figure shows a multidrop network using terminating resistors.

[IMAGE alt='image' src='GUID-BE50E346-0AD5-490E-888F-DE7BC203C61F-a5.gif']

#### Multidrop Network Using Terminating Resistors

The following figure shows a full-duplex network using terminating resistors.

[IMAGE alt='image' src='GUID-9366583E-C967-4BF4-BF52-4140DBA7B971-a5.gif']

#### Full-Duplex Network Using Terminating Resistors

Parent topic:

Serial Communication Issues

<!--NI_TOPIC bundle=ni-serial path=rs-485-transceiver-control.html language=enus -->
## TOPIC 00042: RS-485 Transceiver Control

- bundle_id: `ni-serial`
- source_path: `rs-485-transceiver-control.html`
- source_url: https://docs-be.ni.com/bundle/ni-serial/raw/resource/enus/rs-485-transceiver-control.html
- document_id: `ni-serial`
- page_type: `leaf`
- content_type: `concept`
- source_description: The RS-485 hardware supports four modes of hardware transceiver control. You can use hardware transceiver control to enable and disable your transmitters and receivers so that they function on different bus topologies. The following table lists the status of the transmitters and receivers under each

### RS-485 Transceiver Control

The RS-485 hardware supports four modes of hardware transceiver control. You can use
 hardware transceiver control to enable and disable your transmitters and receivers so
 that they function on different bus topologies. The following table lists the status of
 the transmitters and receivers under each transceiver control mode.

#### RS-485 Transceiver Control Modes

| Mode | Transmitter | Receiver |
| --- | --- | --- |
| Four-wire mode | Always enabled | Always enabled |
| Two-wire mode: DTR controlled with echo | Enabled when DTR asserted | Always enabled |
| Two-wire mode: DTR controlled | Enabled when DTR asserted | Enabled when DTR unasserted |
| Two-wire mode: Auto Control | Enabled when transmitting data | Enabled when not transmitting data |

#### Four-Wire Mode

Use the four-wire mode for most full-duplex systems. In this mode, the transmitter
 and receiver are always enabled. This mode is the default.

#### Two-Wire Mode: DTR Controlled with Echo

You can use this mode in half-duplex systems where you need to control the
 transmitter programmatically. In the DTR-with-echo mode, the transmitter is
 tri-stated when the DTR signal of the UART (Universal Asynchronous
 Receiver/Transmitter) is unasserted. To transmit, your application first must enable
 the transmitter by asserting DTR. After the data is fully transmitted, your
 application unasserts DTR to disable the transmitter. Because the receiver is always
 enabled in this mode, you receive packets not only from other devices, but also your
 transmitter. Thus, your receiver echoes all data you transmit.

#### Two-Wire Mode: DTR Controlled

This mode is similar to the two-wire, DTR-with-echo mode. Although this mode uses the
 same method as the DTR-with-echo mode to control the transmitter, the hardware
 automatically disables the receiver whenever the transmitter is enabled. Thus, you
 do not receive the packets sent from your transmitter.

#### Two-Wire Mode: Auto Control

In this mode, the serial hardware transparently enables the transmitter and receiver
 in a two-wire system. Use this mode to remove the burden of transceiver control from
 your application. The hardware automatically enables the transmitter for each byte
 to be transmitted. Also, the hardware disables the receiver whenever the transmitter
 is enabled, so you do not receive the packets sent from your transmitter.

Note

Related concepts:

- Serial Communication Issues

<!--NI_TOPIC bundle=ni-serial path=rs-485.html language=enus -->
## TOPIC 00043: RS-485

- bundle_id: `ni-serial`
- source_path: `rs-485.html`
- source_url: https://docs-be.ni.com/bundle/ni-serial/raw/resource/enus/rs-485.html
- document_id: `ni-serial`
- page_type: `leaf`
- content_type: `concept`
- source_description: As specified in the EIA-485 Standard, Standard for Electrical Characteristics of Generators and Receivers for Use in Balanced Digital Multipoint Systems, RS-485 expands on the RS-422 standard by increasing the number of devices you can use from 10 to 32 and by working with half-duplex bus architectu

### RS-485

As specified in the EIA-485 Standard, Standard for Electrical Characteristics of
 Generators and Receivers for Use in Balanced Digital Multipoint Systems,
 RS-485 expands on the RS-422 standard by increasing the number of devices you can use
 from 10 to 32 and by working with half-duplex bus architectures. Unlike the RS-422
 standard, RS-485 addresses the issue of using multiple transmitters on the same line.
 RS-485 defines the electrical characteristics necessary to ensure adequate signal
 voltages under maximum load, as well as short-circuit protection. RS-485 can also
 withstand multiple drivers driving conflicting signals at the same time.

Parent topic:

Serial Port Information Overview

<!--NI_TOPIC bundle=ni-serial path=serial-communication-issues.html language=enus -->
## TOPIC 00044: Serial Communication Issues

- bundle_id: `ni-serial`
- source_path: `serial-communication-issues.html`
- source_url: https://docs-be.ni.com/bundle/ni-serial/raw/resource/enus/serial-communication-issues.html
- document_id: `ni-serial`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following topics explain some serial communication issues, including duplex architectures, termination methods, bias resistors, and types of connecting equipment. Duplex Architectures Full Duplex Half Duplex RS-485 Termination Bias Resistors RS-232 DTE versus DCE

### Serial Communication Issues

The following topics explain some serial communication issues, including duplex
 architectures, termination methods, bias resistors, and types of connecting
 equipment.

Duplex Architectures

Full Duplex

Half Duplex

RS-485 Termination

Bias Resistors

RS-232 DTE versus DCE

Parent topic:

Serial Port Information Overview

Related concepts:

- Duplex Architectures
- Full Duplex
- Half Duplex
- RS-485 Termination
- Bias Resistors
- RS-232 DTE versus DCE

<!--NI_TOPIC bundle=ni-serial path=serial-port-information.html language=enus -->
## TOPIC 00045: Serial Port Information Overview

- bundle_id: `ni-serial`
- source_path: `serial-port-information.html`
- source_url: https://docs-be.ni.com/bundle/ni-serial/raw/resource/enus/serial-port-information.html
- document_id: `ni-serial`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following topics describe the RS-232, RS-422, and RS-485 standards and explain some of the issues involved with these types of serial communication. RS-232 RS-422 RS-485 Serial Communication Issues Duplex Architectures Full Duplex Half Duplex RS-485 Termination Bias Resistors RS-232 DTE versus D

### Serial Port Information Overview

The following topics describe the RS-232, RS-422, and RS-485 standards and explain some
 of the issues involved with these types of serial communication.

RS-232

RS-422

RS-485

Serial Communication Issues

Duplex Architectures

Full Duplex

Half Duplex

RS-485 Termination

Bias Resistors

RS-232 DTE versus DCE

The following table lists the features of the RS-232, RS-422, and RS-485 standards.

#### RS-232, RS-422, and RS-485 Features

| Feature | RS-232 | RS-422 | RS-485 |
| --- | --- | --- | --- |
| Type of transmission lines | Single ended | Differential | Differential |
| Maximum number of drivers | 1 | 1 | 32 |
| Maximum number of receivers | 1 | 10 | 32 |
| Maximum cable length | 50 ft | 4,000 ft | 4,000 ft |
| Maximum data rate | 20 kbytes/s | 10 Mbytes/s | 10 Mbytes/s |
| Maximum CMV | ± 25 V | ±7 V | +12 to –7 V |
| Driver output | 5 to 25 V | 2 to 6 V | 1.5 to 6 V |
| Driver load | <3 k | 100 | 60 |

Related concepts:

- RS-232
- RS-422
- RS-485
- Serial Communication Issues
- Duplex Architectures
- Full Duplex
- Half Duplex
- RS-485 Termination
- Bias Resistors
- RS-232 DTE versus DCE

<!--NI_TOPIC bundle=ni-serial path=serial-port-settings.html language=enus -->
## TOPIC 00046: Serial Port Settings

- bundle_id: `ni-serial`
- source_path: `serial-port-settings.html`
- source_url: https://docs-be.ni.com/bundle/ni-serial/raw/resource/enus/serial-port-settings.html
- document_id: `ni-serial`
- page_type: `leaf`
- content_type: `concept`
- source_description: Viewing Serial Port Settings To view your Windows serial port settings, follow these steps: Launch MAX. Expand the desired system. This is My System for the local machine, or can be found under Remote Systems for a LabVIEW Real-Time controller. Expand the Devices and Interfaces folder. Browse the ha

### Serial Port Settings

#### Viewing Serial Port Settings

1. Launch MAX .
2. Expand the desired system. This is My System for the
 local machine, or can be found under Remote Systems 
 for a LabVIEW Real-Time controller.
3. Expand the Devices and Interfaces folder.
4. Browse the hardware tree to locate the desired serial port.

#### Port Settings Tab

The Port Settings tab contains the general serial port
 settings such as baud rate, parity, etc. In the Port Settings
 tab, you can change any setting by clicking the arrow button to the right of a
 field. When you click the arrow button, a list of valid values for that field
 appears, and you can select the desired setting from the list. For boards that
 support nonstandard baud rates, in addition to selecting default baud rates from the
 drop-down list, you may also enter a value directly.

#### Advanced Settings Tab

The Advanced Settings tab contains settings specific to your
 hardware, such as the transceiver mode, enabling or disabling the FIFOs, or enabling
 or disabling the bias resistors on the USB-485. The available settings may change
 depending on what serial interface you are configuring. Click Show
 Help in the upper right corner of the MAX window for information
 about specific advanced settings.

Note

#### Save Pending Changes

To save your changes to this item, click Save.

#### Discard Pending Changes

To discard your changes to the current port, click Revert.
 Revert is available only if you have made at least one change to the port. It undoes
 any changes you have made and restores the port to the most recently saved
 state.

#### Restore Defaults

To reset all fields for a port to their default values at any time (not including the
 COM port number), click the Defaults button.

<!--NI_TOPIC bundle=ni-serial path=setting-ring-indicate-and-dcd-with-deviceioco.html language=enus -->
## TOPIC 00047: Setting Ring Indicate and DCD with DeviceIoControl

- bundle_id: `ni-serial`
- source_path: `setting-ring-indicate-and-dcd-with-deviceioco.html`
- source_url: https://docs-be.ni.com/bundle/ni-serial/raw/resource/enus/setting-ring-indicate-and-dcd-with-deviceioco.html
- document_id: `ni-serial`
- page_type: `leaf`
- content_type: `concept`
- source_description: There are two ways to set and retrieve these RS-232 signals: Set and read the NI-VISA Line RI State and Line DCD State attributes. The NI-Serial software uses programmatic control codes and the DeviceIoControl Windows function to retrieve these RS-232 signals. To retrieve these RS-232 signals using

### Setting Ring Indicate and DCD with DeviceIoControl

There are two ways to set and retrieve these RS-232 signals:

- Set and read the NI-VISA Line RI State and Line DCD State attributes.
- The NI-Serial software uses programmatic control codes and the DeviceIoControl Windows
 function to retrieve these RS-232 signals.

To retrieve these RS-232 signals using the DeviceIoControl Windows function, complete the
 following steps:

1. Add the following lines to your source code: #include <winioctl.h>
#include <NiSerial.h> 
 Note The header file NiSerial.h is included on your
 NI-Serial software CD. You also can find it in the NI-Serial folder
 where you installed your National Instruments software (typically, C:\Program
 Files\National Instruments\NI-Serial).
2. The SERIAL_RI_OUT attribute can have the following values:
  - SERIAL_RI_ON
  - SERIAL_RI_OFF
3. To set the RS-232 signal RI when the transceiver is in DCE mode, use the following
 code:
 DWORD l_ByteCount;
DeviceIoControl (
 PortHandle,
 NISERIAL_SET_RI,
 (LPVOID) NULL,
 0,
 (LPVOID) NULL,
 0,
 (LPDWORD) &l_ByteCount,
 NULL
 );
4. To clear the RS-232 signal RI when the transceiver is in DCE mode, use the following
 code:
 DWORD l_ByteCount;
DeviceIoControl (
 PortHandle,
 NISERIAL_CLR_RI,
 (LPVOID) NULL,
 0,
 (LPVOID) NULL,
 0,
 (LPDWORD) &l_ByteCount,
 NULL
 );
5. To retrieve the current state of the RS-232 signal RI when the transceiver is in DCE
 mode, use the following code:
 SERIAL_RI_OUT l_SerialRiOut;
DWORD l_ByteCount;
DeviceIoControl (
 PortHandle,
 NISERIAL_GET_RI,
 (LPVOID) NULL,
 0,
 (LPVOID) &l_SerialRiOut,
 sizeof (l_SerialRiOut),
 (LPDWORD) &l_ByteCount,
 NULL
 );
6. The SERIAL_DCD_OUT attribute can have the following values:
  - SERIAL_DCD_ON
  - SERIAL_DCD_OFF
7. To set the RS-232 signal DCD when the transceiver is in DCE mode, use the following
 code:
 DWORD l_ByteCount;
DeviceIoControl (
 PortHandle,
 NISERIAL_SET_DCD,
 (LPVOID) NULL,
 0,
 (LPVOID) NULL,
 0,
 (LPDWORD) &l_ByteCount,
 NULL
 );
8. To clear the RS-232 signal DCD when the transceiver is in DCE mode, use the following
 code:
 DWORD l_ByteCount;
DeviceIoControl (
 PortHandle,
 NISERIAL_CLR_DCD,
 (LPVOID) NULL,
 0,
 (LPVOID) NULL,
 0,
 (LPDWORD) &l_ByteCount,
 NULL
 );
9. To retrieve the current state of the RS-232 signal DCD when the transceiver is in DCE
 mode, use the following code:
 SERIAL_DCD_OUT l_SerialDcdOut;
DWORD l_ByteCount;
DeviceIoControl (
 PortHandle,
 NISERIAL_GET_DCD,
 (LPVOID) NULL,
 0,
 (LPVOID) &l_SerialDcdOut,
 sizeof (l_SerialDcdOut),
 (LPDWORD) &l_ByteCount,
 NULL
 );

Parent topic:

USB-232 Transceiver Control

<!--NI_TOPIC bundle=ni-serial path=setting-the-rs-232-transceiver-mode-with-device.html language=enus -->
## TOPIC 00048: Setting the RS-232 Transceiver Mode with DeviceIoControl

- bundle_id: `ni-serial`
- source_path: `setting-the-rs-232-transceiver-mode-with-device.html`
- source_url: https://docs-be.ni.com/bundle/ni-serial/raw/resource/enus/setting-the-rs-232-transceiver-mode-with-device.html
- document_id: `ni-serial`
- page_type: `leaf`
- content_type: `concept`
- source_description: There are two ways to set and retrieve the RS-232 transceiver state: Set and read the NI-VISA wire mode attribute. The NI-Serial software uses programmatic control codes and the DeviceIoControl Windows function to retrieve the RS-232 transceiver state. To set and retrieve the RS-232 transceiver stat

### Setting the RS-232 Transceiver Mode with DeviceIoControl

There are two ways to set and retrieve the RS-232 transceiver state:

- Set and read the NI-VISA wire mode attribute.
- The NI-Serial software uses programmatic control codes and the DeviceIoControl Windows
 function to retrieve the RS-232 transceiver state.

To set and retrieve the RS-232 transceiver state using the DeviceIoControl Windows
 function, complete the following steps:

1. Add the following lines to your source code: #include <winioctl.h>
#include <NiSerial.h> 
 Note The header file NiSerial.h is included on your
 NI-Serial software CD. You also can find it in the NI-Serial folder
 where you installed your National Instruments software (typically, C:\Program
 Files\National Instruments\NI-Serial).
2. The TRANSCEIVER_MODE attribute can have the following values:
  - RS232_MODE_DTE
  - RS232_MODE_DCE
  - RS232_MODE_AUTO
3. To set the RS-232 transceiver, use NISERIAL_SET_RS232_MODE and
 DeviceIoControl. For example, to set to Force DCE mode, use the following code:
 TRANSCEIVER_MODE l_TransceiverMode = RS232_MODE_DCE;
DWORD l_ByteCount;
DeviceIoControl (
 PortHandle,
 NISERIAL_SET_RS232_MODE,
 (LPVOID) &l_TransceiverMode,
 sizeof (l_TransceiverMode),
 (LPVOID) NULL,
 0,
 (LPDWORD) &l_ByteCount,
 NULL
 );
4. To retrieve the current RS-232 transceiver mode, you can use
 NISERIAL_GET_RS232_MODE and DeviceIoControl with the following code:
 TRANSCEIVER_MODE l_TransceiverMode;
DWORD l_ByteCount;
DeviceIoControl (
 PortHandle,
 NISERIAL_GET_RS232_MODE,
 (LPVOID) NULL,
 0,
 (LPVOID) &l_TransceiverMode,
 sizeof (l_TransceiverMode),
 (LPDWORD) &l_ByteCount,
 NULL
 );

Parent topic:

USB-232 Transceiver Control

<!--NI_TOPIC bundle=ni-serial path=setting-the-rs-485-transceiver-control-mode-labview.html language=enus -->
## TOPIC 00049: Setting the RS-485 Transceiver Control Mode in LabVIEW Real-Time

- bundle_id: `ni-serial`
- source_path: `setting-the-rs-485-transceiver-control-mode-labview.html`
- source_url: https://docs-be.ni.com/bundle/ni-serial/raw/resource/enus/setting-the-rs-485-transceiver-control-mode-labview.html
- document_id: `ni-serial`
- page_type: `leaf`
- content_type: `concept`
- source_description: Setting the Default Mode of Operation To set the default mode of operation: For PCI, PCI Express, PXI, and PXI Express: Use the Advanced tab in Measurement & Automation Explorer (MAX) to define the default transceiver control mode. For FieldPoint devices supporting multiple transceiver control modes

### Setting the RS-485 Transceiver Control Mode in LabVIEW Real-Time

#### Setting the Default Mode of Operation

To set the default mode of operation:

- For PCI, PCI Express, PXI, and PXI Express: Use the
 Advanced tab in Measurement & Automation Explorer
 (MAX) to define the default transceiver control mode.
- For FieldPoint devices supporting multiple transceiver control modes, follow
 these steps: Note Without modification, the default mode is set
 to four-wire.
  1. Using an FTP client, download the
 /ni-rt/system/niserial.dbs file from the LabVIEW
 Real-Time target.
  2. Locate the entry in the niserial.dbs file that says
 SerialPortName = "COMx" , where
 COMx corresponds to the port you want to
 modify.
  3. In the next line, add the following entry to the
 niserial.dbs file: TransceiverMode =
 <Transceiver Mode> where
 <Transceiver Mode> is: <Transceiver Mode>
Description128
Four-wire mode
129
Two-wire mode: DTR controlled with echo
130
Two-wire mode: DTR controlled
131
Two-wire mode: Auto Control
  4. Copy the file back to its original location on the LabVIEW Real-Time
 target, replacing the original file. Reboot your LabVIEW Real-Time
 target for your changes to take effect. For example, to configure COM4
 to use two-wire Auto Control mode, the following would appear in the
 niserial.dbs file: SerialPortName = "COM4"
 TransceiverMode = 131

#### Modifying the Transceiver Control Mode Programmatically

To modify the transceiver control mode programmatically:

- In LabVIEW Real-Time, you must use the VISA wire mode attribute to change the
 RS-485 transceiver control mode programmatically.

Parent topic:

RS-485 Transceiver Control

<!--NI_TOPIC bundle=ni-serial path=setting-the-rs-485-transceiver-control-mode-windows.html language=enus -->
## TOPIC 00050: Setting the RS-485 Transceiver Control Mode in Windows

- bundle_id: `ni-serial`
- source_path: `setting-the-rs-485-transceiver-control-mode-windows.html`
- source_url: https://docs-be.ni.com/bundle/ni-serial/raw/resource/enus/setting-the-rs-485-transceiver-control-mode-windows.html
- document_id: `ni-serial`
- page_type: `leaf`
- content_type: `concept`
- source_description: Setting the Default Mode of Operation To set the default mode of operation: Use the Advanced tab in Measurement & Automation Explorer (MAX). Modifying the RS-485 Transceiver Mode Programmatically To modify the RS-485 transceiver mode programmatically: Change the NI-VISA wire mode attribute. The NI-S

### Setting the RS-485 Transceiver Control Mode in Windows

#### Setting the Default Mode of Operation

- Use the Advanced tab in Measurement & Automation Explorer
 (MAX).

#### Modifying the RS-485 Transceiver Mode Programmatically

- Change the NI-VISA wire mode attribute.
- The NI-Serial software uses programmatic control codes and the DeviceIoControl Windows
 function for programming the RS-485 transceiver control mode.

#### Setting the RS-485 Transceiver Control Mode on PCI, PCI Express, PXI, PXI Express, USB,
 and ExpressCard Hardware

1. Add the following lines to your source code: #include <winioctl.h>
#include <NiSerial.h> 
 Note You can find the header file NiSerial.h
 in the NI-Serial folder where you installed your National
 Instruments software (typically, C:\Program Files\National
 Instruments\NI-Serial). It is also included on your NI-Serial
 software CD.
2. The TRANSCEIVER_MODE attribute can have the following values:
  - RS485_MODE_4WIRE
  - RS485_MODE_2W_ECHO
  - RS485_MODE_2W_DTR
  - RS485_MODE_2W_AUTO
3. To set the RS-485 transceiver control mode, use
 NISERIAL_SET_RS485_MODE and DeviceIoControl. For example,
 to set to two-wire Auto Control mode, use the following code:
 TRANSCEIVER_MODE l_TransceiverMode = RS485_MODE_2W_AUTO;
DWORD l_ByteCount;
DeviceIoControl (
 PortHandle,
 NISERIAL_SET_RS485_MODE,
 (LPVOID) &l_TransceiverMode,
 sizeof (l_TransceiverMode),
 (LPVOID) NULL,
 0,
 (LPDWORD) &l_ByteCount,
 NULL
 );
4. To retrieve the current RS-485 transceiver control mode, you can use
 NISERIAL_GET_RS485_MODE and DeviceIoControl with the
 following code:
 TRANSCEIVER_MODE l_TransceiverMode;
DWORD l_ByteCount;
DeviceIoControl (
 PortHandle,
 NISERIAL_GET_RS485_MODE,
 (LPVOID) NULL,
 0,
 (LPVOID) &l_TransceiverMode,
 sizeof (l_TransceiverMode),
 (LPDWORD) &l_ByteCount,
 NULL
 );

#### Setting the RS-485 Transceiver Control Mode on ENET
 Hardware

1. Add the following lines to your source code:
 #include <winioctl.h>
#define SERIAL_TM_4WIRE 0x80
#define SERIAL_TM_2W_ECHO 0x81
#define SERIAL_TM_2W_DTR 0x82
#define SERIAL_TM_2W_AUTO 0x83
#define IOCTL_SERIAL_SET_TRANSCEIVER_MODE
 CTL_CODE(FILE_DEVICE_SERIAL_PORT,37,METHOD_BUFFERED,FILE_ANY_ACCESS)
2. To set the RS-485 transceiver control mode, use
 IOCTL_SERIAL_SET_TRANSCEIVER_MODE and DeviceIoControl. For
 example, to set to two-wire Auto Control mode, use the following code:
 ULONG bytecount;
TRANSCEIVER_MODE transceiver_mode = SERIAL_TM_2W_AUTO;
DeviceIoControl(
 comhandle,
 IOCTL_SERIAL_SET_TRANSCEIVER_MODE,
 (PVOID) &transceiver_mode,
 sizeof(transceiver_mode),
 (PVOID) NULL, 0,
 &bytecount,
 NULL
);

Parent topic:

RS-485 Transceiver Control

<!--NI_TOPIC bundle=ni-serial path=setting-the-usb-485-programmatically-controll.html language=enus -->
## TOPIC 00051: Setting the USB-485 Programmatically Controlled Bias Resistor Mode

- bundle_id: `ni-serial`
- source_path: `setting-the-usb-485-programmatically-controll.html`
- source_url: https://docs-be.ni.com/bundle/ni-serial/raw/resource/enus/setting-the-usb-485-programmatically-controll.html
- document_id: `ni-serial`
- page_type: `leaf`
- content_type: `concept`
- source_description: The USB-485 hardware can programmatically control the onboard (nonsocketed) bias resistors. By default, these resistors are enabled during normal device operation and disabled during USB suspend. There are two ways to control these resistors: Use the Advanced tab in MAX. If the Enable Dynamic Bias R

### Setting the USB-485 Programmatically Controlled Bias Resistor Mode

The USB-485 hardware can programmatically control the onboard (nonsocketed) bias resistors.
 By default, these resistors are enabled during normal device operation and disabled during
 USB suspend. There are two ways to control these resistors:

- Use the Advanced tab in MAX. If the Enable Dynamic
 Bias Resistors box is checked, the resistors are enabled automatically
 whenever a serial port is open during normal operation. If the box is not checked, the
 resistors are disabled.
- Your software can enable or disable the bias resistors programmatically by making
 DeviceIoControl calls to the serial driver.

#### Setting the RS-485 Programmatically Controlled Bias Resistors with
 DeviceIoControl

The NI-Serial software uses programmatic control codes and the DeviceIoControl Windows
 function for programming the RS-485 bias resistor mode. To set and retrieve the RS-485
 bias resistor mode, complete the following steps:

1. Add the following lines to your source code: #include <winioctl.h>
#include <NiSerial.h> 
 Note The header file NiSerial.h is included on your
 NI-Serial software CD. You also can find it in the NI-Serial
 folder where you installed your National Instruments software (typically,
 C:\Program Files\National Instruments\NI-Serial).
2. The SERIAL_RS485_BIAS attribute can have the following values:
  - RS485_BIAS_OFF
  - RS485_BIAS_ON
3. To set the RS-485 bias resistor mode, use NISERIAL_SET_RS485_BIAS 
 and DeviceIoControl. For example, to enable programmatically controlled RS-485 bias
 resistors, use the following code:
 SERIAL_RS485_BIAS l_SerialRs485Bias = RS485_BIAS_ON;
DWORD l_ByteCount;
DeviceIoControl (
 PortHandle,
 NISERIAL_SET_RS485_BIAS,
 (LPVOID) &l_SerialRs485Bias,
 sizeof (l_SerialRs485Bias),
 (LPVOID) NULL,
 0,
 (LPDWORD) &l_ByteCount,
 NULL
 );
4. To retrieve the current RS-485 bias resistor mode, you can use
 NISERIAL_GET_RS485_BIAS and DeviceIoControl with the following
 code:
 SERIAL_RS485_BIAS l_SerialRs485Bias;
DWORD l_ByteCount;
DeviceIoControl (
 PortHandle,
 NISERIAL_GET_RS485_BIAS,
 (LPVOID) NULL,
 0,
 (LPVOID) &l_SerialRs485Bias,
 sizeof (l_SerialRs485Bias),
 (LPDWORD) &l_ByteCount,
 NULL
 );

Parent topic:

Bias Resistors

<!--NI_TOPIC bundle=ni-serial path=uninstall-software-from-your-labview-rt-target.html language=enus -->
## TOPIC 00052: Uninstall Software from Your LabVIEW RT Target

- bundle_id: `ni-serial`
- source_path: `uninstall-software-from-your-labview-rt-target.html`
- source_url: https://docs-be.ni.com/bundle/ni-serial/raw/resource/enus/uninstall-software-from-your-labview-rt-target.html
- document_id: `ni-serial`
- page_type: `leaf`
- content_type: `concept`
- source_description: To uninstall the NI-Serial software from your LabVIEW RT target, complete the following steps: Launch MAX. Expand Remote Systems by clicking the + next to it. Find your remote system in the list and expand it. Right-click Software and select Add/Remove Software. In the Add/Remove Software window, cl

### Uninstall Software from Your LabVIEW RT Target

To uninstall the NI-Serial software from your LabVIEW RT target, complete the following
 steps:

1. Launch MAX.
2. Expand Remote Systems by clicking the
 + next to it.
3. Find your remote system in the list and expand it.
4. Right-click Software and select Add/Remove
 Software .
5. In the Add/Remove Software window, click
 NI-Serial and select Uninstall the
 Feature .
6. Click Next to start the software download. Click
 Finish when the download is complete.

<!--NI_TOPIC bundle=ni-serial path=uninstall-the-windows-software.html language=enus -->
## TOPIC 00053: Uninstall the Windows Software

- bundle_id: `ni-serial`
- source_path: `uninstall-the-windows-software.html`
- source_url: https://docs-be.ni.com/bundle/ni-serial/raw/resource/enus/uninstall-the-windows-software.html
- document_id: `ni-serial`
- page_type: `leaf`
- content_type: `concept`
- source_description: To uninstall the NI-Serial software, complete the following steps: Select Start»Control Panel. On Windows XP/Server 2003, double-click the Add/Remove Programs icon. On Windows Vista, double-click the Programs and Features icon. On Windows 7/Server 2008, click Uninstall a Program. Select National Ins

### Uninstall the Windows Software

To uninstall the NI-Serial software, complete the following steps:

1. Select Start»Control Panel .
2. On Windows XP/Server 2003, double-click the Add/Remove
 Programs icon. On Windows Vista, double-click the
 Programs and Features icon. On Windows 7/Server 2008,
 click Uninstall a Program .
3. Select National Instruments Software in the list and click
 the Change/Remove button on Windows XP/Server 2003 or the
 Uninstall/Change button on Windows 7/Vista/Server
 2008.
4. Select the software components you want to remove and click the
 Remove button.
5. For PCI, PCI Express, PXI, and PXI Express devices, shut down Windows, power off
 your computer, and physically remove the serial interfaces from your system. For USB
 and ExpressCard hardware, simply unplug the device from your system.

The uninstallation program removes only items that the setup wizard installed. If you
 added anything to a directory that the setup wizard created, the uninstallation program
 does not delete that directory. You must remove any remaining components yourself.

To reinstall the hardware and software, refer to Install the Hardware and NI-Serial
 Software Installation.

<!--NI_TOPIC bundle=ni-serial path=usb-232-transceiver-control.html language=enus -->
## TOPIC 00054: USB-232 Transceiver Control

- bundle_id: `ni-serial`
- source_path: `usb-232-transceiver-control.html`
- source_url: https://docs-be.ni.com/bundle/ni-serial/raw/resource/enus/usb-232-transceiver-control.html
- document_id: `ni-serial`
- page_type: `leaf`
- content_type: `concept`
- source_description: The USB-232 two and four-port hardware supports both DTE and DCE transceiver modes. By default, the RS-232 transceiver mode is forced to DTE, but you can adjust this in two ways: Use the Advanced tab in MAX. To set the transceiver mode to be used whenever a port is opened, select the desired mode fr

### USB-232 Transceiver Control

The USB-232 two and four-port hardware supports both DTE and DCE transceiver modes. By
 default, the RS-232 transceiver mode is forced to DTE, but you can adjust this in two
 ways:

- Use the Advanced tab in MAX. To set the transceiver mode to
 be used whenever a port is opened, select the desired mode from the transceiver mode
 pull-down menu.
- Change the transceiver mode programmatically by making a DeviceIoControl function
 call to the serial driver.

The following table describes the RS-232 modes.

#### RS-232 Modes

| RS-232 Mode | Description |
| --- | --- |
| Force DTE (Default) | The transceiver is forced into DTE mode |
| Force DCE | The transceiver is forced into DCE mode |
| Auto 232 | The transceiver automatically switches between DTE and DCE modes about four times a second until a valid RS-232 signal is detected |

Note

Note

The USB-232 hardware also allows you to set and retrieve the state of the Ring
 Indicate (RI) and Data Carrier Detect (DCD) lines along with the Transceiver
 Mode.

Setting the RS-232 Transceiver Mode with DeviceIoControl

Setting Ring Indicate (RI) and Data Carrier Detect (DCD) with
 DeviceIoControl

Related concepts:

- Setting the RS-232 Transceiver Mode with DeviceIoControl
- Setting Ring Indicate and DCD with DeviceIoControl

<!--NI_TOPIC bundle=ni-serial path=usb-485-programmatically-controlled-bias-resi.html language=enus -->
## TOPIC 00055: USB-485 Programmatically Controlled Bias Resistors

- bundle_id: `ni-serial`
- source_path: `usb-485-programmatically-controlled-bias-resi.html`
- source_url: https://docs-be.ni.com/bundle/ni-serial/raw/resource/enus/usb-485-programmatically-controlled-bias-resi.html
- document_id: `ni-serial`
- page_type: `leaf`
- content_type: `concept`
- source_description: On the USB-485 hardware, there are programmatically controlled onboard bias resistors. In addition, the USB-485 two and four-port hardware has user-configurable socketed bias resistors. By default, the USB-485 hardware uses the programmatically controlled bias resistors, which are connected to the r

### USB-485 Programmatically Controlled Bias Resistors

On the USB-485 hardware, there are programmatically controlled onboard bias resistors. In
 addition, the USB-485 two and four-port hardware has user-configurable socketed bias
 resistors. By default, the USB-485 hardware uses the programmatically controlled bias
 resistors, which are connected to the receive signals of each port to maintain a known
 state when the bus is idle. The connections are made as follows:

- RXD+ and CTS– are pulled up to +3.3 V
- RXD– and CTS+ are pulled down to GND

The follwing figure shows a USB transmission line using bias resistors.

[IMAGE alt='image' src='GUID-E4127892-5447-475F-9FDF-700AEB0F895C-a5.gif']

#### USB-485 Transmission Line Using Bias Resistors

The values of the programmatically controlled bias resistors have been calculated
 such that there is a voltage of at least 200 mV between the differential pair.
 Rather than using the programmatically controlled bias resistors, you can load
 custom values of resistors into the sockets in front of each connector or use
 external bias resistors. If these resistors are installed, make sure the
 programmatically controlled bias resistors are disabled.

Note

Note

[IMAGE alt='image' src='GUID-3D97CC5D-839F-4675-B3BF-F1B240D4C49D-a5.gif']

Parent topic:

Bias Resistors

<!--NI_TOPIC bundle=ni-serial path=usb-hardware-installation.html language=enus -->
## TOPIC 00056: USB Hardware Installation

- bundle_id: `ni-serial`
- source_path: `usb-hardware-installation.html`
- source_url: https://docs-be.ni.com/bundle/ni-serial/raw/resource/enus/usb-hardware-installation.html
- document_id: `ni-serial`
- page_type: `leaf`
- content_type: `concept`
- source_description: If you are installing a USB-485/2 or USB-485/4, you might need to adjust the value of the bias resistors, depending on your application. For more information, refer to Bias Resistors. Before installing your hardware, follow the NI-Serial Software Installation instructions. To install your USB seri

### USB Hardware Installation

Note

Before installing your hardware, follow the NI-Serial Software Installation
 instructions.

To install your USB serial hardware, complete the following steps:

1. If you are installing a USB-485/4, connect the external power supply.
2. Connect the USB cable from the USB hardware to an available USB port on your
 computer or USB hub.
3. If your computer is not already on, turn it on.
4. Windows will automatically detect your hardware.

The serial hardware installation is complete. Continue to Verify the Installation.

Related concepts:

- Bias Resistors

<!--NI_TOPIC bundle=ni-serial path=user-manual-welcome.html language=enus -->
## TOPIC 00057: NI-Serial User Manual

- bundle_id: `ni-serial`
- source_path: `user-manual-welcome.html`
- source_url: https://docs-be.ni.com/bundle/ni-serial/raw/resource/enus/user-manual-welcome.html
- document_id: `ni-serial`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI-Serial User Manual provides detailed descriptions of the product functionality and the step by step processes for use. Looking for Something Else?For information not found in the User Manual for your product, such as specifications and API reference, browse Related Information.

### NI-Serial
 User Manual

The NI-Serial User Manual provides detailed
 descriptions of the product functionality and the step by step processes for use.

#### Looking for Something Else?

For information not found in the User Manual
 for your product, such as specifications and API reference, browse *Related
 Information*.

Related information:

- Download NI-Serial
- Interactive Activation Guide
- NI-Serial Release Notes
- NI-Serial Troubleshooter User Manual
- Hardware Configuration Utility User Manual

<!--NI_TOPIC bundle=ni-serial path=verify-installation-and-troubleshoot-ni-serial.html language=enus -->
## TOPIC 00058: Verify Installation and Troubleshoot NI-Serial Problems

- bundle_id: `ni-serial`
- source_path: `verify-installation-and-troubleshoot-ni-serial.html`
- source_url: https://docs-be.ni.com/bundle/ni-serial/raw/resource/enus/verify-installation-and-troubleshoot-ni-serial.html
- document_id: `ni-serial`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI-Serial Troubleshooting Wizard supports ports only on your local Windows system. It does not test your LabVIEW Real-Time serial ports. To verify the hardware and software installation and troubleshoot NI-Serial problems, follow these steps to run the Troubleshooting Wizard: Launch MAX. Select

### Verify Installation and Troubleshoot NI-Serial Problems

The NI-Serial Troubleshooting Wizard supports ports only on your local Windows system. It
 does not test your LabVIEW Real-Time serial ports.

To verify the hardware and software installation and troubleshoot NI-Serial problems,
 follow these steps to run the Troubleshooting Wizard:

1. Launch MAX.
2. Select Help»Troubleshooting»NI-Serial Troubleshooting Wizard .
 The Troubleshooting Wizard tests your serial interface and displays the results as
 shown below.

[IMAGE alt='image' src='GUID-20AB2087-8AA2-4E95-859C-D135136A807F-a5.gif']

#### NI-Serial Troubleshooting Wizard

The Troubleshooting Wizard verifies that your serial driver is installed properly,
 that the configuration of your hardware does not conflict with anything else in your
 system, and that the serial driver can communicate with your hardware correctly.

To view online help for the Troubleshooting Wizard, click the
 Help button.

<!--NI_TOPIC bundle=ni-serial path=verify-installation-and-troubleshoot.html language=enus -->
## TOPIC 00059: NI-Serial Troubleshooter

- bundle_id: `ni-serial`
- source_path: `verify-installation-and-troubleshoot.html`
- source_url: https://docs-be.ni.com/bundle/ni-serial/raw/resource/enus/verify-installation-and-troubleshoot.html
- document_id: `ni-serial`
- page_type: `leaf`
- content_type: `concept`
- source_description: NI-Serial Troubleshooter is used to verify installation and troubleshoot issues. The NI-Serial Troubleshooter supports ports only on your local Windows system. It does not test your LabVIEW Real-Time serial ports. To verify the hardware and software installation and troubleshoot NI-Serial problems,

### NI-Serial Troubleshooter

NI-Serial Troubleshooter is used to verify installation and troubleshoot issues. The NI-Serial Troubleshooter supports ports only on your local Windows system.
 It does not test your LabVIEW Real-Time serial ports.

1. Launch MAX .
2. Select Help >> Troubleshootin >> NI-Serial
 Troubleshooter .

The Troubleshooter verifies that your serial driver is installed properly, that the
 configuration of your hardware does not conflict with anything else in your system, and
 that the serial driver can communicate with your hardware correctly.

To view online help for the Troubleshooter, click the Help
 button.

<!--NI_TOPIC bundle=ni-serial path=view-ni-serial-software-version.html language=enus -->
## TOPIC 00060: View NI-Serial Software Version

- bundle_id: `ni-serial`
- source_path: `view-ni-serial-software-version.html`
- source_url: https://docs-be.ni.com/bundle/ni-serial/raw/resource/enus/view-ni-serial-software-version.html
- document_id: `ni-serial`
- page_type: `leaf`
- content_type: `concept`
- source_description: To view the NI-Serial software version for Windows, follow these steps: Launch MAX. Expand the My System directory by clicking the + next to the folder. Expand the Software directory by clicking the + next to the folder. Click NI-Serial. MAX displays the NI-Serial software version number in the righ

### View NI-Serial Software Version

1. Launch MAX .
2. Expand the My System directory by clicking the
 + next to the folder.
3. Expand the Software directory by clicking the
 + next to the folder.
4. Click NI-Serial .

MAX displays the NI-Serial software version number in the right pane.

1. Launch MAX .
2. Expand Remote Systems by clicking the
 + next to it.
3. Find your RT controller in the list and expand it.
4. Expand the Software directory.
5. Click NI-Serial .

MAX displays the NI-Serial software version number in the right pane.

<!--NI_TOPIC bundle=ni-serial path=what-happens-to-data-sent-to-a-closed-serial.html language=enus -->
## TOPIC 00061: What happens to data sent to a closed serial port?

- bundle_id: `ni-serial`
- source_path: `what-happens-to-data-sent-to-a-closed-serial.html`
- source_url: https://docs-be.ni.com/bundle/ni-serial/raw/resource/enus/what-happens-to-data-sent-to-a-closed-serial.html
- document_id: `ni-serial`
- page_type: `leaf`
- content_type: `concept`
- source_description: Because serial communication ports are active only when the port is open (for example, by using CreateFile), data may be received and made available only when the port is open. Assume that any data received by a closed com port may be lost or corrupted.

### What happens to data sent to a closed serial port?

Because serial communication ports are active only when the port is open (for example, by
 using CreateFile), data may be received and made available only when the port is open.
 Assume that any data received by a closed com port may be lost or corrupted.

<!--NI_TOPIC bundle=ni-serial path=what-is-the-difference-between-usb-20-and-usb.html language=enus -->
## TOPIC 00062: What is the difference between USB 2.0 and USB 1.1?

- bundle_id: `ni-serial`
- source_path: `what-is-the-difference-between-usb-20-and-usb.html`
- source_url: https://docs-be.ni.com/bundle/ni-serial/raw/resource/enus/what-is-the-difference-between-usb-20-and-usb.html
- document_id: `ni-serial`
- page_type: `leaf`
- content_type: `concept`
- source_description: The USB 2.0 specification replaces the USB 1.1 specification and adds a high-speed mode of operation (480 Mbit/s) to the previously existing full-speed (12 Mbit/s) and low-speed (1.5 Mbit/s) modes of operation. Because USB 2.0 expands on the features of USB 1.1 while preserving backward device compa

### What is the difference between USB 2.0 and USB 1.1?

The USB 2.0 specification replaces the USB 1.1 specification and adds a high-speed mode
 of operation (480 Mbit/s) to the previously existing full-speed (12 Mbit/s) and
 low-speed (1.5 Mbit/s) modes of operation. Because USB 2.0 expands on the features of
 USB 1.1 while preserving backward device compatibility, you can use most full-speed and
 low-speed devices with either USB 2.0 high-speed networks or USB 1.1 full-speed
 networks.

USB-232/485 devices are USB 2.0 full-speed compliant, so you can use them in either
 high-speed (USB 2.0 hubs) or full-speed (USB 1.1 hubs) networks.

<!--NI_TOPIC bundle=ni-serial path=what-is-the-relationship-between-bits-per-second.html language=enus -->
## TOPIC 00063: What is the relationship between bits per second, throughput, and bus utilization?

- bundle_id: `ni-serial`
- source_path: `what-is-the-relationship-between-bits-per-second.html`
- source_url: https://docs-be.ni.com/bundle/ni-serial/raw/resource/enus/what-is-the-relationship-between-bits-per-second.html
- document_id: `ni-serial`
- page_type: `leaf`
- content_type: `concept`
- source_description: The term bits per second (bps) refers to the bit rate of data transfer, with 1/bps being the length of time in seconds required to transmit one bit. Throughput is the actual data transfer measured by amount of data transmitted time required to transmit Bus utilization is the percentage of time that

### What is the relationship between bits per second, throughput, and bus
 utilization?

The term bits per second (bps) refers to the bit rate of data
 transfer, with 1/bps being the length of time in seconds required to transmit one
 bit.

Throughput is the actual data transfer measured by

amount of data transmitted
time required to transmit

Bus utilization is the percentage of time that the serial bus is
 actively transmitting data. Because a wide range of factors such as flow control,
 processor latency, and device architecture can affect serial performance, bus
 utilization often is not 100 percent. In addition, there is overhead associated with
 serial communication in the form of start bits, stop bits, and parity bits. This
 overhead reduces the throughput by 20–30 percent. Thus, the actual data throughput can
 be considerably less than the bits per second setting.

<!--NI_TOPIC bundle=ni-serial path=why-cant-i-make-changes-to-my-settings-in-measurement.html language=enus -->
## TOPIC 00064: Why can't I make changes to my settings in Measurement Automation Explorer (MAX)?

- bundle_id: `ni-serial`
- source_path: `why-cant-i-make-changes-to-my-settings-in-measurement.html`
- source_url: https://docs-be.ni.com/bundle/ni-serial/raw/resource/enus/why-cant-i-make-changes-to-my-settings-in-measurement.html
- document_id: `ni-serial`
- page_type: `leaf`
- content_type: `concept`
- source_description: To make changes in MAX on Windows XP/Server 2003, you must be a user with Administrator privileges. To make changes in MAX on Windows 7/Vista/Server 2008, follow these steps to launch MAX with administrative privileges: If MAX is open, close it. Find the MAX icon on the desktop or by going to Start»

### Why can't I make changes to my settings in Measurement Automation Explorer (MAX)?

To make changes in MAX on Windows XP/Server 2003, you must be a user with Administrator
 privileges. To make changes in MAX on Windows 7/Vista/Server 2008, follow these steps to
 launch MAX with administrative privileges:

1. If MAX is open, close it.
2. Find the MAX icon on the desktop or by going to Start»All
 Programs»National Instruments»Measurement Automation .
3. Right-click on the MAX icon and select Run as administrator .
 You must enter an administrative password if you are not an administrator.

You should now be able to modify and save settings in MAX.

<!--NI_TOPIC bundle=ni-serial path=why-do-loopback-tests-of-large-data-transfers.html language=enus -->
## TOPIC 00065: Why do loopback tests of large data transfers sometimes have problems?

- bundle_id: `ni-serial`
- source_path: `why-do-loopback-tests-of-large-data-transfers.html`
- source_url: https://docs-be.ni.com/bundle/ni-serial/raw/resource/enus/why-do-loopback-tests-of-large-data-transfers.html
- document_id: `ni-serial`
- page_type: `leaf`
- content_type: `concept`
- source_description: In a typical loopback test, an external wrap plug is used to loop back transmit signals to receive signals. In this configuration, data transmitted is read back on the same serial port to test port communication. Loopback programs often perform this data transfer using a single write followed by a s

### Why do loopback tests of large data transfers sometimes have problems?

In a typical loopback test, an external wrap plug is used to loop back transmit signals
 to receive signals. In this configuration, data transmitted is read back on the same
 serial port to test port communication. Loopback programs often perform this data
 transfer using a single write followed by a single read, and thus rely on driver
 software and serial hardware buffering to hold the data between the two function calls.
 However, these buffers are of finite size, and thus any data transfer that exceeds the
 buffer size either times out, blocks (due to flow control), or drops data. This behavior
 is a result of the test design and does not represent a hardware or driver error. Buffer
 sizes vary between operating systems and hardware, but typically range from 4–8 KB in
 size.

<!--NI_TOPIC bundle=ni-serial path=why-does-my-pcipci-expresspxipxi-express-serial.html language=enus -->
## TOPIC 00066: Why does my PCI/PCI Express/PXI/PXI Express serial card display the wrong serial number?

- bundle_id: `ni-serial`
- source_path: `why-does-my-pcipci-expresspxipxi-express-serial.html`
- source_url: https://docs-be.ni.com/bundle/ni-serial/raw/resource/enus/why-does-my-pcipci-expresspxipxi-express-serial.html
- document_id: `ni-serial`
- page_type: `leaf`
- content_type: `concept`
- source_description: If you swap one PCI/PCI Express/PXI/PXI Express serial card for another of the exact same type, the serial number shown in the device manager and MAX may not change. This happens because Windows cannot distinguish the old hardware from the new. To fix this problem, delete the interface from the syst

### Why does my PCI/PCI Express/PXI/PXI Express serial card display the wrong serial
 number?

If you swap one PCI/PCI Express/PXI/PXI Express serial card for another of the exact same
 type, the serial number shown in the device manager and MAX may not change. This happens
 because Windows cannot distinguish the old hardware from the new. To fix this problem,
 delete the interface from the system and either scan for new hardware in the device
 manager or restart your computer. This forces Windows to reinstall your hardware, and
 the correct serial number should be displayed.

<!--NI_TOPIC bundle=ni-serial path=why-isnt-the-auto232-transceiver-mode-on-my-u.html language=enus -->
## TOPIC 00067: Why isn't the Auto232 transceiver mode on my USB-232 working?

- bundle_id: `ni-serial`
- source_path: `why-isnt-the-auto232-transceiver-mode-on-my-u.html`
- source_url: https://docs-be.ni.com/bundle/ni-serial/raw/resource/enus/why-isnt-the-auto232-transceiver-mode-on-my-u.html
- document_id: `ni-serial`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Auto232 mode of operation allows you to connect to either a RS-232 DTE or DCE device using either a null-modem or straight-through cable. The USB-232 port will automatically switch approximately every 250 ms between DTE and DCE operating modes until at least one RS-232 receiver line (RX, CTS, DS

### Why isn't the Auto232 transceiver mode on my USB-232 working?

The Auto232 mode of operation allows you to connect to either a RS-232 DTE or DCE device
 using either a null-modem or straight-through cable. The USB-232 port will automatically
 switch approximately every 250 ms between DTE and DCE operating modes until at least one
 RS-232 receiver line (RX, CTS, DSR, RI, or DCD) has a valid voltage. Auto232 is
 available on the USB-232/2 and USB-232/4, and is not available on the USB-232 (single
 port).

Not all devices and applications can take advantage of this feature:

- Some devices can generate valid voltages on receive lines for both modes, even
 though the device itself is only DTE or DCE. Thus, these devices may not operate
 correctly when using Auto232 mode.
- Some applications immediately start communicating after a COM port is open, thus not
 allowing enough time for the proper operating mode to be selected.
- Some cabling schemes short RI, DCD, and DSR together. While this does not present a
 problem in DTE mode, these signals are driven when in DCE mode. Thus, by shorting
 the signals together, the outputs will be double (or triple) driven which may cause
 signal noise or other artifacts. Use a straight-through cable instead.

If problems with Auto232 can not be resolved, set the USB-232 to the correct mode (DTE or
 DCE) for your device and application. By default, the USB-232 ports are set to DTE
 mode.
