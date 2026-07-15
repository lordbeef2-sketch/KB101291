# NI DOCUMENT BUNDLE: gpib-usb-hs-specs

<!--NI_BUNDLE_CHUNK bundle=gpib-usb-hs-specs start=1 end=1 -->
<!--NI_TOPIC bundle=gpib-usb-hs-specs path=specs.html language=enus -->
## TOPIC 00001: GPIB-USB-HS Specifications

- bundle_id: `gpib-usb-hs-specs`
- source_path: `specs.html`
- source_url: https://docs-be.ni.com/bundle/gpib-usb-hs-specs/raw/resource/enus/specs.html
- document_id: `gpib-usb-hs-specs`
- page_type: `leaf`
- content_type: `topic`
- source_description: GPIB-USB-HS Specifications Definitions Warranted specifications describe the performance of a model under stated operating conditions and are covered by the model warranty. Characteristics describe values that are relevant to the use of the model under stated operating conditions but are not covered

### GPIB-USB-HS
 Specifications

#### GPIB-USB-HS Specifications

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

#### Bus Interface

| Bus Connector | USB 3.0/2.0 hi-speed or 1.1 full-speed[1]1 The module READY LED lights amber when connected to a USB 3.0 or 2.0 port, and green when connected to a USB 1.1 port. |
| --- | --- |

#### Power Requirements

USB bus-powered device

| +5 V (VBUS) | 140 mA, Typical; 500 mA, Maximum |
| --- | --- |

#### GPIB-USB-HS Pinout

Use the pinout to connect to terminals on the GPIB-USB-HS.

Figure 1.

GPIB-USB-HS

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

| Dimensions | 10.7 cm × 6.6 cm × 2.6 cm (4.2 in. × 2.6 in. × 1.0 in.) |
| --- | --- |
| Weight | 180 g (6.3 oz), includes USB cable weight |
| Connector GPIBIEEE 488 24-pin connector USBUSB standard Type A plug |  |
| Connector |  |
| GPIB | IEEE 488 24-pin connector |
| USB | USB standard Type A plug |
| Jackscrew ThreadM3.5 × 0.6 Torque0.56 N · m (5.0 lb · in.), maximum |  |
| Jackscrew |  |
| Thread | M3.5 × 0.6 |
| Torque | 0.56 N · m (5.0 lb · in.), maximum |

#### Environment

| Operating ambient temperature | 0 °C to 55 °C (Tested in accordance with IEC 60068-2-1 and IEC 60068-2-2.) |
| --- | --- |
| Operating relative humidity | 10% to 90%, noncondensing (Tested in accordance with IEC 60068-2-56.) |
| Storage ambient temperature | -20 °C to 70 °C (Tested in accordance with IEC 60068-2-1 and IEC 60068-2-2.) |
| Storage relative humidity | 5% to 95%, noncondensing (Tested in accordance with IEC 60068-2-56.) |

[<sup>1</sup>](#note_ref-d266e185) The module
 READY LED lights amber when connected to a USB 3.0 or 2.0
 port, and green when connected to a USB 1.1 port.
