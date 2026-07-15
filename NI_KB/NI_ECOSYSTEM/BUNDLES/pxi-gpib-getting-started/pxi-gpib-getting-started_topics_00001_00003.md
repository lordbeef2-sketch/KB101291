# NI DOCUMENT BUNDLE: pxi-gpib-getting-started

<!--NI_BUNDLE_CHUNK bundle=pxi-gpib-getting-started start=1 end=3 -->
<!--NI_TOPIC bundle=pxi-gpib-getting-started path=installation.html language=enus -->
## TOPIC 00001: PXI-GPIB and PXI-8232 Installation

- bundle_id: `pxi-gpib-getting-started`
- source_path: `installation.html`
- source_url: https://docs-be.ni.com/bundle/pxi-gpib-getting-started/raw/resource/enus/installation.html
- document_id: `pxi-gpib-getting-started`
- page_type: `leaf`
- content_type: `task`
- source_description: Electrostatic discharge can damage several components on your GPIB board. To avoid electrostatic damage when you handle the board, touch the antistatic plastic package to a metal part of your system chassis before removing the board from the package. Complete the following steps to install your PXI

PXI-GPIB and PXI-8232 Installation

Notice

1. Make sure that your PXI or CompactPCI chassis is powered off. Keep the PXI or
 CompactPCI chassis plugged in so that it remains grounded while you install your PXI
 card.
2. Choose an unused PXI or CompactPCI 5 V peripheral slot. For maximum performance, your PXI card has an onboard DMA controller that can only be used if the board is installed in a slot that supports bus arbitration, or bus master cards. National Instruments recommends installing your PXI card in such a slot. If you install the board in a non-master slot, you must disable your PXI card’s onboard DMA controller using the board-level call ibdma. Refer to the NI-488.2 Help for a complete description of ibdma.
3. Remove the filler panel for the peripheral slot you have chosen.
4. Touch a metal part on your chassis to discharge any static electricity that might be on your clothes or body.
5. Insert your PXI card into the selected 5 V slot. Use the injector/ejector handle to
 fully inject the device into place. The following figure shows how to install your PXI card into a PXI or CompactPCI chassis. 
 Figure 1.Installing Your PXI Card
 
 
 
[IMAGE alt='1378' src='GUID-FC7E16A0-5551-4C89-8896-7CABF73A58DD-a5.svg'] 

 1 Injector/Ejector Handle (In Down Position)2 Your PXI Card
 3 PXI Chassis4 Injector/Ejector Rail
6. Screw the front panel of the PXI card to the front panel mounting rail of the PXI or CompactPCI chassis.
7. Power on your PXI or CompactPCI chassis. 
 The PXI card installation is now complete.

Parent topic:

PXI-GPIB

<!--NI_TOPIC bundle=pxi-gpib-getting-started path=overview.html language=enus -->
## TOPIC 00002: PXI-GPIB

- bundle_id: `pxi-gpib-getting-started`
- source_path: `overview.html`
- source_url: https://docs-be.ni.com/bundle/pxi-gpib-getting-started/raw/resource/enus/overview.html
- document_id: `pxi-gpib-getting-started`
- page_type: `leaf`
- content_type: `reference`
- source_description: The PXI‑GPIB is an IEEE 488 controller module for PXI systems. You can use this module to integrate non-PXI instruments into your PXI system using GPIB. The PXI‑GPIB achieves maximum IEEE 488.2 transfer rates. This module includes a license for the NI‑488.2 driver software, which provides maximum re

PXI-GPIB

The PXI‑GPIB is an IEEE 488 controller module for PXI systems.
 You can use this module to integrate non-PXI instruments into your PXI system using
 GPIB. The PXI‑GPIB achieves maximum IEEE 488.2 transfer rates. This module includes a license
 for the NI‑488.2 driver software, which provides maximum reliability for connecting to
 third-party instruments with GPIB.

© 2001–2023 National Instruments Corporation. All rights reserved. Refer to the <National Instruments>\_Legal Information directory for information about NI copyright, patents, trademarks, warranties, product warnings, and export compliance.

<!--NI_TOPIC bundle=pxi-gpib-getting-started path=pinout.html language=enus -->
## TOPIC 00003: GPIB Pinout

- bundle_id: `pxi-gpib-getting-started`
- source_path: `pinout.html`
- source_url: https://docs-be.ni.com/bundle/pxi-gpib-getting-started/raw/resource/enus/pinout.html
- document_id: `pxi-gpib-getting-started`
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

PXI-GPIB
