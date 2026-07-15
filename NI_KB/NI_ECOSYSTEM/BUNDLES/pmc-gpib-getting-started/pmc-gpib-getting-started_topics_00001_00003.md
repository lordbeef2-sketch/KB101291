# NI DOCUMENT BUNDLE: pmc-gpib-getting-started

<!--NI_BUNDLE_CHUNK bundle=pmc-gpib-getting-started start=1 end=3 -->
<!--NI_TOPIC bundle=pmc-gpib-getting-started path=installation.html language=enus -->
## TOPIC 00001: PMC-GPIB Installation

- bundle_id: `pmc-gpib-getting-started`
- source_path: `installation.html`
- source_url: https://docs-be.ni.com/bundle/pmc-gpib-getting-started/raw/resource/enus/installation.html
- document_id: `pmc-gpib-getting-started`
- page_type: `leaf`
- content_type: `task`
- source_description: Electrostatic discharge can damage several components on your GPIB board. To avoid electrostatic damage when you handle the board, touch the antistatic plastic package to a metal part of your system chassis before removing the board from the package. Complete the following steps to install your PMC-

PMC-GPIB Installation

Notice

1. Power off your system.
2. Find an unused PMC slot in your system. You may need to remove the host from the system to access the PMC slot.
3. Remove the corresponding slot filler panel from the host.
4. Insert the PMC-GPIB into the slot as shown in the following figure. It might be a
 tight fit, but do not force the board into place. 
 Figure 1.Installing the PMC-GPIB
 [IMAGE alt='1378' src='GUID-8646F128-A778-4E53-953D-550AFCCFBA98-a5.svg'] 

 1 Host Face Plate
 2 3.3 V Keying Hole
 3.5 V Keying Hole
 4 PMC-GPIB Board
 5 Mounting Screws
5. Use the mounting hardware provided to fasten the PMC-GPIB to the host.
6. Reinstall the host, if you removed it to install the PMC-GPIB.
7. Power on your system. 
 The PMC-GPIB hardware installation is now complete.

Parent topic:

PMC-GPIB

<!--NI_TOPIC bundle=pmc-gpib-getting-started path=overview.html language=enus -->
## TOPIC 00002: PMC-GPIB

- bundle_id: `pmc-gpib-getting-started`
- source_path: `overview.html`
- source_url: https://docs-be.ni.com/bundle/pmc-gpib-getting-started/raw/resource/enus/overview.html
- document_id: `pmc-gpib-getting-started`
- page_type: `leaf`
- content_type: `reference`
- source_description: The PMC‑GPIB is an IEEE 488 controller device for the PCI Mezzanine Card (PMC) standard (IEEE P1386.1).You can use this device to integrate an instrument into your system using GPIB. The PMC‑GPIB achieves maximum IEEE 488.2 transfer rates and plug‑and‑play compatibility for easy hardware installatio

PMC-GPIB

The PMC‑GPIB is an IEEE 488 controller device for the PCI Mezzanine Card
 (PMC) standard (IEEE P1386.1).You can use this device to integrate an instrument
 into your system using GPIB. The PMC‑GPIB achieves maximum IEEE 488.2 transfer rates and
 plug‑and‑play compatibility for easy hardware installation. The device includes a license for
 the NI‑488.2 driver software, providing maximum reliability for connecting to third-party
 instruments with GPIB.

© 2001–2023 National Instruments Corporation. All rights reserved. Refer to the <National Instruments>\_Legal Information directory for information about NI copyright, patents, trademarks, warranties, product warnings, and export compliance.

<!--NI_TOPIC bundle=pmc-gpib-getting-started path=pinout.html language=enus -->
## TOPIC 00003: PMC-GPIB Pinout

- bundle_id: `pmc-gpib-getting-started`
- source_path: `pinout.html`
- source_url: https://docs-be.ni.com/bundle/pmc-gpib-getting-started/raw/resource/enus/pinout.html
- document_id: `pmc-gpib-getting-started`
- page_type: `leaf`
- content_type: `reference`
- source_description: Signal Descriptions Signal Terminal Description DIO1 1 Data Input/Output Bit. DIO2 2 Data Input/Output Bit. DIO3 3 Data Input/Output Bit. DIO4 4 Data Input/Output Bit. EOI 5 End-Or-Identify. DAV 6 Data Valid. NRFD 7 Not Ready For Data. NDAC 8 Not Data Accepted. IFC 9 Interface Clear. SRQ 10 Service

PMC-GPIB Pinout

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

PMC-GPIB
