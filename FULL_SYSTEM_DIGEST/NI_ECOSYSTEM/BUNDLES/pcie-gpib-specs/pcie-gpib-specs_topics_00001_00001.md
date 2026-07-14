# NI DOCUMENT BUNDLE: pcie-gpib-specs

<!--NI_BUNDLE_CHUNK bundle=pcie-gpib-specs start=1 end=1 -->
<!--NI_TOPIC bundle=pcie-gpib-specs path=specs.html language=enus -->
## TOPIC 00001: PCIe-GPIB Specifications

- bundle_id: `pcie-gpib-specs`
- source_path: `specs.html`
- source_url: https://docs-be.ni.com/bundle/pcie-gpib-specs/raw/resource/enus/specs.html
- document_id: `pcie-gpib-specs`
- page_type: `leaf`
- content_type: `topic`
- source_description: PCIe-GPIB Specifications These specifications apply to the PCIe-GPIB. Revision History Version Date changed Description 379201B-01 December 2025 Intro topic added.Added GPIB connector version number.Clarified PCI Express connector wording. Looking For Something Else?For information not found in the

### PCIe-GPIB Specifications

#### PCIe-GPIB
 Specifications

These specifications apply to the
 PCIe-GPIB.

##### Revision History

| Version | Date changed | Description |
| --- | --- | --- |
| 379201B-01 | December 2025 | Intro topic added.Added GPIB connector version number.Clarified PCI Express connector wording. |

##### Looking For Something
 Else?

For information not found in the specifications for your product,
 such as operating instructions, browse *Related Information*.

Related information:

- PCIe-GPIB
 Getting Started
- Software and Driver Downloads
- Dimensional Drawings
- Product Certifications
- Letter of Volatility
- Discussion Forums
- NI Learning Center

#### PCIe-GPIB Specifications

#### Definitions

*Warranted* specifications describe the performance of a model under stated operating conditions and are covered by the model warranty.

*Characteristics* describe values that are relevant to the use of the model under stated operating conditions but are not covered by the model warranty.

- Typical specifications describe the performance met by a
 majority of models.
- Nominal specifications describe an attribute that is based on
 design, conformance testing, or supplemental testing.

Specifications are *Typical* unless otherwise noted.

#### PCIe-GPIB Pinout

Use the pinout to connect to terminals on the PCIe-GPIB.

Figure 1.

PCIe-GPIB

[IMAGE alt='image' src='GUID-C222BF22-4A0A-4664-AD3C-064800201A7A-a5.svg']

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

#### Performance

| GPIB 3-wireup to 1670 kbytes/s HS488up to 7980 kbytes/s |  |
| --- | --- |
| GPIB |  |
| 3-wire | up to 1670 kbytes/s |
| HS488 | up to 7980 kbytes/s |

#### Power Requirements

Note

x

Notice of Board Change—PCIe-GPIB

ni.com

| PCIe-GPIB (+3.3 V) | 320 mA, Typical; 500 mA, Maximum |
| --- | --- |

#### Physical Characteristics

| Dimensions | 9.754 cm × 6.888 cm (3.840 in. × 2.712 in.) |
| --- | --- |
| Connector GPIBIEEE 488 24-pin connector (Version 1.1) PCI Express Lanesx1 |  |
| Connector |  |
| GPIB | IEEE 488 24-pin connector (Version 1.1) |
| PCI Express Lanes | x1 |

#### Environment

| Operating ambient temperature | 0 °C to 55 °C (Tested in accordance with IEC 60068-2-1 and IEC 60068-2-2.) |
| --- | --- |
| Operating relative humidity | 10% to 90%, noncondensing (Tested in accordance with IEC 60068-2-56.) |
| Storage ambient temperature | -20 °C to 70 °C (Tested in accordance with IEC 60068-2-1 and IEC 60068-2-2.) |
| Storage relative humidity | 5% to 95%, noncondensing (Tested in accordance with IEC 60068-2-56.) |
