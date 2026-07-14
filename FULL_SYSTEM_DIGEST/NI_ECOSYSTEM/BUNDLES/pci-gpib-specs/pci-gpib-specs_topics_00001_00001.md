# NI DOCUMENT BUNDLE: pci-gpib-specs

<!--NI_BUNDLE_CHUNK bundle=pci-gpib-specs start=1 end=1 -->
<!--NI_TOPIC bundle=pci-gpib-specs path=specs.html language=enus -->
## TOPIC 00001: PCI-GPIB Specifications

- bundle_id: `pci-gpib-specs`
- source_path: `specs.html`
- source_url: https://docs-be.ni.com/bundle/pci-gpib-specs/raw/resource/enus/specs.html
- document_id: `pci-gpib-specs`
- page_type: `leaf`
- content_type: `reference`
- source_description: Definitions Warranted specifications describe the performance of a model under stated operating conditions and are covered by the model warranty. Characteristics describe values that are relevant to the use of the model under stated operating conditions but are not covered by the model warranty. Typ

PCI-GPIB Specifications

#### Definitions

*Warranted* specifications describe the performance of a model under stated operating conditions and are covered by the model warranty.

*Characteristics* describe values that are relevant to the use of the model under stated operating conditions but are not covered by the model warranty.

- Typical specifications describe the performance met by a
 majority of models.
- Nominal specifications describe an attribute that is based on
 design, conformance testing, or supplemental testing.

Specifications are *Typical* unless otherwise noted.

#### Performance

| GPIB 3-wireup to 1536 kbytes/s HS488up to 7885 kbytes/s |  |
| --- | --- |
| GPIB |  |
| 3-wire | up to 1536 kbytes/s |
| HS488 | up to 7885 kbytes/s |

#### Power Requirements

| PCI-GPIB/TNT4882C[1] +3.3 V121 mA, Typical; 182 mA, Maximum +5 V300 mA, Typical; 450 mA, Maximum |  |
| --- | --- |
| PCI-GPIB/TNT4882C[1] |  |
| +3.3 V | 121 mA, Typical; 182 mA, Maximum |
| +5 V | 300 mA, Typical; 450 mA, Maximum |
| PCI-GPIB/TNT5004[2] +5 V150 mA, Maximum VIO5 mA, Maximum |  |
| PCI-GPIB/TNT5004[2] |  |
| +5 V | 150 mA, Maximum |
| VIO | 5 mA, Maximum |
| PCI-GPIB/LP (Low Profile)[3] +5 V300 mA, Typical; 450 mA, Maximum |  |
| PCI-GPIB/LP (Low Profile)[3] |  |
| +5 V | 300 mA, Typical; 450 mA, Maximum |

#### Physical Characteristics

| Dimensions PCI-GPIB/TNT4882C13.3 cm × 10.7 cm (5.25 in. × 4.20 in.) PCI-GPIB/TNT500412 cm × 6.44 cm (4.72 in. × 2.54 in.) PCI-GPIB/LP12 cm × 6.44 cm (4.87 in. × 2.54 in.) |  |
| --- | --- |
| Dimensions |  |
| PCI-GPIB/TNT4882C | 13.3 cm × 10.7 cm (5.25 in. × 4.20 in.) |
| PCI-GPIB/TNT5004 | 12 cm × 6.44 cm (4.72 in. × 2.54 in.) |
| PCI-GPIB/LP | 12 cm × 6.44 cm (4.87 in. × 2.54 in.) |
| Connector GPIBIEEE 488 24-pin connector (The PCI-GPIB/LP uses a special cable to convert between the Micro D-Sub connector of the board and the GPIB connector.) PCIUniversal |  |
| Connector |  |
| GPIB | IEEE 488 24-pin connector (The PCI-GPIB/LP uses a special cable to convert between the Micro D-Sub connector of the board and the GPIB connector.) |
| PCI | Universal |

#### Environment

| Operating ambient temperature | 0 °C to 55 °C (Tested in accordance with IEC 60068-2-1 and IEC 60068-2-2.) |
| --- | --- |
| Operating relative humidity | 10% to 90%, noncondensing (Tested in accordance with IEC 60068-2-56.) |
| Storage ambient temperature | -20 °C to 70 °C (Tested in accordance with IEC 60068-2-1 and IEC 60068-2-2.) |
| Storage relative humidity | 5% to 95%, noncondensing (Tested in accordance with IEC 60068-2-56.) |

[<sup>1</sup>](#note_ref-d233e173) PCI-GPIB boards manufactured before 2003 use the TNT4882C controller. The assembly number printed on these boards is 183617*x*-01.

[<sup>2</sup>](#note_ref-d233e205) A later revision of PCI-GPIB boards uses the TNT5004 controller. The assembly number printed on these boards is 188513*x*-01.

[<sup>3</sup>](#note_ref-d233e237) PCI-GPIB/LP is a low-profile PCI-GPIB board designed to fit in low-profile machines. It uses a special cable to convert between the micro-DSub connector of the board and the GPIB connector.
