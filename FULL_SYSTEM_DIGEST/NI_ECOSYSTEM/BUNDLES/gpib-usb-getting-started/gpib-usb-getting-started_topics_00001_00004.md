# NI DOCUMENT BUNDLE: gpib-usb-getting-started

<!--NI_BUNDLE_CHUNK bundle=gpib-usb-getting-started start=1 end=4 -->
<!--NI_TOPIC bundle=gpib-usb-getting-started path=installation.html language=enus -->
## TOPIC 00001: Installation

- bundle_id: `gpib-usb-getting-started`
- source_path: `installation.html`
- source_url: https://docs-be.ni.com/bundle/gpib-usb-getting-started/raw/resource/enus/installation.html
- document_id: `gpib-usb-getting-started`
- page_type: `leaf`
- content_type: `task`
- source_description: Ground loops create an electric shock hazard and can cause damage to your GPIB-USB hardware, your computer, and other system components. A ground loop can occur when your computer and one or more connected instruments do not share the same ground potential. To prevent damage to your GPIB-USB hardwar

Installation

Notice

To prevent damage to your GPIB-USB hardware and other system components, do any of the following:

- Ensure that your system and all instruments connected to it share the same ground potential. This eliminates the possibility of voltage differential running through
 your system.
- Use a GPIB-120B Bus Isolator/Expander to isolate GPIB systems and expand the GPIB interface up to 28 devices.
- Use a pair of GPIB-140A High-Speed Fiber-Optic Bus Extenders. This transforms the GPIB signals at each end into fiber optic signals, allowing each unit to reside at a different ground potential.
- Use an isolated USB hub.

Complete the following steps to install your interface:

1. Connect the USB connector from the GPIB-USB interface to an available USB Type A port on your computer.
2. Before connecting the GPIB-USB interface to GPIB devices, ensure that the computer and the GPIB devices are at the same ground potential. The GPIB-USB interface connects directly to most GPIB devices without requiring a GPIB cable.
3. If your computer is already running, the operating system automatically detects the GPIB interface. Otherwise, the GPIB interface is detected when you start your computer. 
 Figure 1.Installing the GPIB-USB Interface[IMAGE alt='1378' src='GUID-3A7DE663-6ABE-4A40-ADFB-23E069EBA6F5-a5.svg'] 

 1 Computer
 2 USB Connector
 3 GPIB-USB Interface
 4 To GPIB DevicesThe GPIB hardware installation is now complete.

Parent topic:

Overview

<!--NI_TOPIC bundle=gpib-usb-getting-started path=led-signaling.html language=enus -->
## TOPIC 00002: LED Signaling

- bundle_id: `gpib-usb-getting-started`
- source_path: `led-signaling.html`
- source_url: https://docs-be.ni.com/bundle/gpib-usb-getting-started/raw/resource/enus/led-signaling.html
- document_id: `gpib-usb-getting-started`
- page_type: `leaf`
- content_type: `concept`
- source_description: The GPIB-USB-HS controller uses two LEDs to indicate status and activity. When you connect the GPIB-USB-HS controller, the READY LED lights either green or amber once the driver is installed and detected. The following table summarizes the functionality of the LEDs on the GPIB-USB-HS hardware. GPIB-

LED Signaling

The GPIB-USB-HS controller uses two LEDs to indicate status and activity.

When you connect the GPIB-USB-HS controller, the READY LED lights either green or amber
 once the driver is installed and detected. The following table summarizes the functionality
 of the LEDs on the GPIB-USB-HS hardware.

| LED | Description |
| --- | --- |
| READY | Green indicates that the GPIB-USB-HS is plugged into a USB full-speed (USB 1.1) port.Amber indicates that the GPIB-USB-HS is plugged into a USB Hi-Speed (USB 2.0) port. |
| ACTIVE | Indicates activity on the GPIB bus. |

The GPIB-USB-HS+ controller uses a multicolored LED to indicate status and activity. The
 following table summarizes the functionality of the LEDs on the GPIB-USB-HS+ hardware.

| LED | Description |
| --- | --- |
| Alternating Amber/Green | The GPIB-USB-HS+ is not ready to use. You must install (or re-install) the NI-488.2 driver before using the GPIB-USB-HS+.Note: Windows 8 and later suspend power to a USB device that does not have a driver attached. If the LED does not light, try reinstalling the NI-488.2 driver. |
| Steady Green | Indicates that the GPIB-USB-HS+ is plugged into a USB full-speed (USB 1.1) port. |
| Steady Amber | Indicates that the GPIB-USB-HS+ is plugged into a USB Hi-Speed (USB 2.0) port. |
| Blinking Amber or Green | Indicates activity on the GPIB bus or that the GPIB Analyzer is capturing. |

Parent topic:

Installation

<!--NI_TOPIC bundle=gpib-usb-getting-started path=overview.html language=enus -->
## TOPIC 00003: Overview

- bundle_id: `gpib-usb-getting-started`
- source_path: `overview.html`
- source_url: https://docs-be.ni.com/bundle/gpib-usb-getting-started/raw/resource/enus/overview.html
- document_id: `gpib-usb-getting-started`
- page_type: `leaf`
- content_type: `reference`
- source_description: The GPIB‑USB‑HS and The GPIB‑USB‑HS+ are IEEE 488 controller devices for computers with USB slots. The GPIB‑USB‑HS and The GPIB‑USB‑HS+ achieve maximum IEEE 488.2 performance and are completely IEEE 488.2 compatible. With no GPIB cable required for instrument connection, you can use the Hi‑Speed USB

Overview

The GPIB‑USB‑HS and The GPIB‑USB‑HS+ are IEEE 488 controller devices for
 computers with USB slots. The GPIB‑USB‑HS and The GPIB‑USB‑HS+ achieve maximum
 IEEE 488.2 performance and are completely IEEE 488.2 compatible. With no GPIB cable required for
 instrument connection, you can use the Hi‑Speed USB port to control up to 14 programmable GPIB
 instruments. The device includes a license for the NI‑488.2 driver software, providing maximum
 reliability for connecting to third-party instruments with GPIB.

© 2001–2023 National Instruments Corporation. All rights reserved. Refer to the <National Instruments>\_Legal Information directory for information about NI copyright, patents, trademarks, warranties, product warnings, and export compliance.

<!--NI_TOPIC bundle=gpib-usb-getting-started path=pinout.html language=enus -->
## TOPIC 00004: GPIB Pinout

- bundle_id: `gpib-usb-getting-started`
- source_path: `pinout.html`
- source_url: https://docs-be.ni.com/bundle/gpib-usb-getting-started/raw/resource/enus/pinout.html
- document_id: `gpib-usb-getting-started`
- page_type: `leaf`
- content_type: `reference`
- source_description: Signal Descriptions Signal Terminal Description DIO1 1 Data Input/Output Bit. DIO2 2 Data Input/Output Bit. DIO3 3 Data Input/Output Bit. DIO4 4 Data Input/Output Bit. EOI 5 End-Or-Identify. DAV 6 Data Valid. NRFD 7 Not Ready For Data. NDAC 8 Not Data Accepted. IFC 9 Interface Clear. SRQ 10 Service

GPIB Pinout

[IMAGE alt='1378' src='GUID-C222BF22-4A0A-4664-AD3C-064800201A7A-a5.svg']

| Signal | Terminal | Description |
| --- | --- | --- |
| DIO1 | 1 | Data Input/Output Bit. |
| DIO2 | 2 | Data Input/Output Bit. |
| DIO3 | 3 | Data Input/Output Bit. |
| DIO4 | 4 | Data Input/Output Bit. |
| EOI | 5 | End-Or-Identify. |
| DAV | 6 | Data Valid. |
| NRFD | 7 | Not Ready For Data. |
| NDAC | 8 | Not Data Accepted. |
| IFC | 9 | Interface Clear. |
| SRQ | 10 | Service Request. |
| ATN | 11 | Attention. |
| SHIELD | 12 | Shield. |
| DIO5 | 13 | Data Input/Output Bit. |
| DIO6 | 14 | Data Input/Output Bit. |
| DIO7 | 15 | Data Input/Output Bit. |
| DIO8 | 16 | Data Input/Output Bit. |
| REN | 17 | Remote Enable. |
| GND | 18 | Ground—Wire twisted with DAV. |
| GND | 19 | Ground—Wire twisted with NRFD. |
| GND | 20 | Ground—Wire twisted with NDAC. |
| GND | 21 | Ground—Wire twisted with IFC. |
| GND | 22 | Ground—Wire twisted with SRQ. |
| GND | 23 | Ground—Wire twisted with ATN. |
| SIGNAL GROUND | 24 | Logic Ground. |

Parent topic:

Overview
