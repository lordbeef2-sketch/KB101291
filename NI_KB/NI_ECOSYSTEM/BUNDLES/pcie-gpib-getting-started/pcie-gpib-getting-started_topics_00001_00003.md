# NI DOCUMENT BUNDLE: pcie-gpib-getting-started

<!--NI_BUNDLE_CHUNK bundle=pcie-gpib-getting-started start=1 end=3 -->
<!--NI_TOPIC bundle=pcie-gpib-getting-started path=installing.html language=enus -->
## TOPIC 00001: Installation

- bundle_id: `pcie-gpib-getting-started`
- source_path: `installing.html`
- source_url: https://docs-be.ni.com/bundle/pcie-gpib-getting-started/raw/resource/enus/installing.html
- document_id: `pcie-gpib-getting-started`
- page_type: `leaf`
- content_type: `task`
- source_description: Electrostatic discharge can damage several components on your GPIB board. To avoid such damage in handling your board, touch the antistatic plastic package to a metal part of your computer chassis before removing the board from the package. Complete the following steps to install your interface: Mak

Installation

Notice

1. Make sure that your computer is powered off. Keep the computer plugged in so that
 it remains grounded while you install the GPIB hardware.
2. Remove the top cover (or other access panels) to gain access to the computer
 expansion slots.
3. Your PCI Express card can be plugged into a x1, x4, x8, or x16 PCI Express
 slot.
4. Remove the corresponding slot cover on the back panel of the computer.
5. Insert the GPIB board into the slot with the GPIB connector sticking out of the
 opening on the back panel, as shown in the following figure. It might be a tight fit,
 but do not force the board into place. 
 Figure 1.Installing Your PCI Express Board
 
 
[IMAGE alt='1378' src='GUID-9C2EB02A-8FC2-4CEC-8DC1-3F7E13222914-a5.svg']
 1 PCI Express Board
 2 PCI Express Slot
 3 Computer
 org.dita.html5/xsl/topic.xsl 455Note Your PCI Express
 board may be larger than the one shown in the figure.
6. Screw the mounting bracket of the GPIB board to the back panel rail of the
 computer.
7. Replace the top cover (or the access panel to the expansion slot).
8. Power on your computer. 
 The GPIB hardware installation is now complete.

Parent topic:

PCIe-GPIB

<!--NI_TOPIC bundle=pcie-gpib-getting-started path=overview.html language=enus -->
## TOPIC 00002: PCIe-GPIB

- bundle_id: `pcie-gpib-getting-started`
- source_path: `overview.html`
- source_url: https://docs-be.ni.com/bundle/pcie-gpib-getting-started/raw/resource/enus/overview.html
- document_id: `pcie-gpib-getting-started`
- page_type: `leaf`
- content_type: `reference`
- source_description: The PCIe‑GPIB is an IEEE 488 controller device for computers with PCI Express slots. You can use this device to integrate an instrument into your system using GPIB. The PCIe‑GPIB achieves maximum IEEE 488.2 transfer rates. With an onboard bus master DMA controller, there is no microprocessor interru

PCIe-GPIB

The PCIe‑GPIB is an IEEE 488 controller device for computers with PCI Express
 slots. You can use this device to integrate an instrument into your system using
 GPIB. The PCIe‑GPIB achieves maximum IEEE 488.2 transfer rates. With an onboard bus master DMA
 controller, there is no microprocessor interruption in data transfers. The device includes a
 license for the NI‑488.2 driver software, providing maximum reliability for connecting to
 third-party instruments with GPIB.

© 2001–2023 National Instruments Corporation. All rights reserved. Refer to the <National Instruments>\_Legal Information directory for information about NI copyright, patents, trademarks, warranties, product warnings, and export compliance.

<!--NI_TOPIC bundle=pcie-gpib-getting-started path=pinout.html language=enus -->
## TOPIC 00003: GPIB Pinout

- bundle_id: `pcie-gpib-getting-started`
- source_path: `pinout.html`
- source_url: https://docs-be.ni.com/bundle/pcie-gpib-getting-started/raw/resource/enus/pinout.html
- document_id: `pcie-gpib-getting-started`
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

PCIe-GPIB
