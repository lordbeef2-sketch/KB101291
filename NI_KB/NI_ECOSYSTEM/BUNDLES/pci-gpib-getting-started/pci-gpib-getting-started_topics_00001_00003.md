# NI DOCUMENT BUNDLE: pci-gpib-getting-started

<!--NI_BUNDLE_CHUNK bundle=pci-gpib-getting-started start=1 end=3 -->
<!--NI_TOPIC bundle=pci-gpib-getting-started path=installation.html language=enus -->
## TOPIC 00001: Installation

- bundle_id: `pci-gpib-getting-started`
- source_path: `installation.html`
- source_url: https://docs-be.ni.com/bundle/pci-gpib-getting-started/raw/resource/enus/installation.html
- document_id: `pci-gpib-getting-started`
- page_type: `leaf`
- content_type: `task`
- source_description: Electrostatic discharge can damage several components on your GPIB board. To avoid such damage in handling your board, touch the antistatic plastic package to a metal part of your computer chassis before removing the board from the package. Complete the following steps to install your interface: Mak

Installation

Notice

1. Make sure that your computer is powered off. Keep the computer plugged in so that it remains grounded while you install the GPIB hardware.
2. Remove the top cover (or other access panels) to gain access to the computer expansion slots.
3. Find an unused expansion slot in your computer. Your PCI board can be plugged into
 either a 3.3 V or 5 V, 32- or 64-bit PCI slot.
4. Remove the corresponding slot cover on the back panel of the computer.
5. Insert the GPIB board into the slot with the GPIB connector sticking out of the
 opening on the back panel, as shown in the following figure. It might be a tight fit,
 but do not force the board into place. 
 [IMAGE alt='1378' src='GUID-1D37E770-E72A-4002-AE05-A117144A2F08-a5.svg'] 

 1 PCI Express Board
 2 PCI Express Slot
 3 Computer
6. Screw the mounting bracket of the GPIB board to the back panel rail of the computer.
7. Replace the top cover (or the access panel to the expansion slot).
8. Power on your computer. 
 The GPIB hardware installation is now complete.

Parent topic:

PCI-GPIB

<!--NI_TOPIC bundle=pci-gpib-getting-started path=overview.html language=enus -->
## TOPIC 00002: PCI-GPIB

- bundle_id: `pci-gpib-getting-started`
- source_path: `overview.html`
- source_url: https://docs-be.ni.com/bundle/pci-gpib-getting-started/raw/resource/enus/overview.html
- document_id: `pci-gpib-getting-started`
- page_type: `leaf`
- content_type: `reference`
- source_description: The PCI‑GPIB is a plug‑and‑play IEEE 488 interface for PCs and workstations with PCI expansion slots. The PCI‑GPIB can sustain data transfer rates of more than 1.5 MB/s using the IEEE 488.1 three‑wire interlocked handshake. It also implements the high-speed IEEE 488.1 noninterlocked handshake (HS488

PCI-GPIB

The PCI‑GPIB is a plug‑and‑play IEEE 488 interface for PCs and workstations
 with PCI expansion slots. The PCI‑GPIB can sustain data transfer rates of more
 than 1.5 MB/s using the IEEE 488.1 three‑wire interlocked handshake. It also implements the
 high-speed IEEE 488.1 noninterlocked handshake (HS488) for benchmarked data transfers at more
 than 7.7 MB/s. The onboard bus master DMA controller means that there are no microprocessor
 interruptions in data transfer.

© 2001–2023 National Instruments Corporation. All rights reserved. Refer to the <National Instruments>\_Legal Information directory for information about NI copyright, patents, trademarks, warranties, product warnings, and export compliance.

<!--NI_TOPIC bundle=pci-gpib-getting-started path=pinout.html language=enus -->
## TOPIC 00003: GPIB Pinout

- bundle_id: `pci-gpib-getting-started`
- source_path: `pinout.html`
- source_url: https://docs-be.ni.com/bundle/pci-gpib-getting-started/raw/resource/enus/pinout.html
- document_id: `pci-gpib-getting-started`
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

PCI-GPIB
