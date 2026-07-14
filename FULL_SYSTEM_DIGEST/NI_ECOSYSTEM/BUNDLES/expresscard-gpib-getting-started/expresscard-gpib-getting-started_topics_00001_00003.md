# NI DOCUMENT BUNDLE: expresscard-gpib-getting-started

<!--NI_BUNDLE_CHUNK bundle=expresscard-gpib-getting-started start=1 end=3 -->
<!--NI_TOPIC bundle=expresscard-gpib-getting-started path=installation.html language=enus -->
## TOPIC 00001: ExpressCard-GPIB Installation

- bundle_id: `expresscard-gpib-getting-started`
- source_path: `installation.html`
- source_url: https://docs-be.ni.com/bundle/expresscard-gpib-getting-started/raw/resource/enus/installation.html
- document_id: `expresscard-gpib-getting-started`
- page_type: `leaf`
- content_type: `task`
- source_description: Ground loops create an electric shock hazard and can cause damage to your ExpressCard-GPIB hardware, your computer, and other system components. A ground loop can occur when your computer and one or more connected instruments do not share the same ground potential. To prevent damage to your ExpressC

ExpressCard-GPIB Installation

Notice

To prevent damage to your ExpressCard-GPIB hardware and other system components, do any
 of the following:

- Ensure that your system and all instruments connected to it share the same ground
 potential. This eliminates the possibility of voltage differential running through
 your system.
- Use a GPIB-120B Bus Isolator/Expander to isolate GPIB systems and expand the GPIB
 interface up to 28 devices.
- Use a pair of GPIB-140A High-Speed Fiber-Optic Bus Extenders. This transforms the
 GPIB signals at each end into fiber optic signals, allowing each unit to reside at a
 different ground potential.

Complete the following steps to install the ExpressCard-GPIB interface:

1. Plug the card into an available ExpressCard slot on your computer.
2. Before connecting the ExpressCard-GPIB interface to GPIB devices, ensure that the computer and the GPIB devices are at the same ground potential.
3. If your computer is already running, the operating system automatically detects the GPIB interface. Otherwise, the GPIB interface is detected when you start your computer. 
 The following figure shows how to insert the ExpressCard-GPIB and connect the cable.Figure 1.Inserting the ExpressCard-GPIB[IMAGE alt='1378' src='GUID-601F5C2F-F02C-426F-BF87-A995A6A66C3D-a5.svg']
 1 Notebook Computer
 2 ExpressCard Slot
 3 ExpressCard-GPIB CableThe GPIB hardware installation is now complete.

Parent topic:

ExpressCard-GPIB Getting Started

<!--NI_TOPIC bundle=expresscard-gpib-getting-started path=overview.html language=enus -->
## TOPIC 00002: ExpressCard-GPIB Getting Started

- bundle_id: `expresscard-gpib-getting-started`
- source_path: `overview.html`
- source_url: https://docs-be.ni.com/bundle/expresscard-gpib-getting-started/raw/resource/enus/overview.html
- document_id: `expresscard-gpib-getting-started`
- page_type: `leaf`
- content_type: `reference`
- source_description: The ExpressCard‑GPIB is an IEEE 488 controller device for laptop computers with ExpressCard slots. TYou can use this device to integrate an instrument into your system using GPIB. The ExpressCard‑GPIB provides a maximum-performance GPIB controller. It implements the IEEE 488.1 high‑speed handshake (

ExpressCard-GPIB Getting Started

The ExpressCard‑GPIB is an IEEE 488 controller device for laptop computers with
 ExpressCard slots.

TYou can use this device to integrate an instrument into your system using GPIB. The
 ExpressCard‑GPIB provides a maximum-performance GPIB controller. It implements the IEEE 488.1
 high‑speed handshake (HS488). The device includes a license for the NI‑488.2 driver software,
 providing maximum reliability for connecting to third-party instruments with GPIB.

© 2001–2023 National Instruments Corporation. All rights reserved. Refer to the <National Instruments>\_Legal Information directory for information about NI copyright, patents, trademarks, warranties, product warnings, and export compliance.

<!--NI_TOPIC bundle=expresscard-gpib-getting-started path=pinout.html language=enus -->
## TOPIC 00003: GPIB Pinout

- bundle_id: `expresscard-gpib-getting-started`
- source_path: `pinout.html`
- source_url: https://docs-be.ni.com/bundle/expresscard-gpib-getting-started/raw/resource/enus/pinout.html
- document_id: `expresscard-gpib-getting-started`
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

ExpressCard-GPIB Getting Started
