# NI DOCUMENT BUNDLE: expresscard-gpib-specs

<!--NI_BUNDLE_CHUNK bundle=expresscard-gpib-specs start=1 end=1 -->
<!--NI_TOPIC bundle=expresscard-gpib-specs path=specs.html language=enus -->
## TOPIC 00001: ExpressCard-GPIB Specifications

- bundle_id: `expresscard-gpib-specs`
- source_path: `specs.html`
- source_url: https://docs-be.ni.com/bundle/expresscard-gpib-specs/raw/resource/enus/specs.html
- document_id: `expresscard-gpib-specs`
- page_type: `leaf`
- content_type: `topic`
- source_description: ExpressCard-GPIB Specifications Definitions Warranted specifications describe the performance of a model under stated operating conditions and are covered by the model warranty. Characteristics describe values that are relevant to the use of the model under stated operating conditions but are not co

### ExpressCard-GPIB Specifications

#### ExpressCard-GPIB Specifications

#### Definitions

*Warranted* specifications describe the performance of a model under stated operating conditions and are covered by the model warranty.

*Characteristics* describe values that are relevant to the use of the model under stated operating conditions but are not covered by the model warranty.

- Typical specifications describe the performance met by a
 majority of models.
- Nominal specifications describe an attribute that is based on
 design, conformance testing, or supplemental testing.

Specifications are *Typical* unless otherwise noted.

#### Performance

| GPIB 3-wireup to 1830 kbytes/s HS488up to 7230 kbytes/s |  |
| --- | --- |
| GPIB |  |
| 3-wire | up to 1830 kbytes/s |
| HS488 | up to 7230 kbytes/s |

#### Power Requirements

Device is powered by ExpressCard USB interface.

| +3.3 V | 140 mA, Typical; 500 mA, Maximum |
| --- | --- |

#### ExpressCard-GPIB Pinout

Use the pinout to connect to terminals on the ExpressCard-GPIB.

Figure 1.

ExpressCard-GPIB

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

#### Physical Characteristics

| Dimensions | 3.4 cm × 7.5 cm × 0.5 cm (1.34 in. × 2.95 in. × 0.2 in.) |
| --- | --- |
| Connector GPIB26-position latching connector with cable to IEEE 488 24-pin connector included in shipping kit ExpressCardExpressCard/34 standard connector interface |  |
| Connector |  |
| GPIB | 26-position latching connector with cable to IEEE 488 24-pin connector included in shipping kit |
| ExpressCard | ExpressCard/34 standard connector interface |

#### Environment

| Operating ambient temperature | 0 °C to 65 °C (Tested in accordance with IEC 60068-2-1 and IEC 60068-2-2.) |
| --- | --- |
| Operating relative humidity | 5% to 95%, noncondensing (Tested in accordance with IEC 60068-2-56.) |
| Storage ambient temperature | -20 °C to 65 °C (Tested in accordance with IEC 60068-2-1 and IEC 60068-2-2.) |
| Nonoperating thermal shock | -20 °C to 65 °C, 5 shocks |
