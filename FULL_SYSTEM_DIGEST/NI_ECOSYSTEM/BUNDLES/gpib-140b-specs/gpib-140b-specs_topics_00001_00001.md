# NI DOCUMENT BUNDLE: gpib-140b-specs

<!--NI_BUNDLE_CHUNK bundle=gpib-140b-specs start=1 end=1 -->
<!--NI_TOPIC bundle=gpib-140b-specs path=gpib-140b-specs.html language=enus -->
## TOPIC 00001: GPIB-140B Specifications

- bundle_id: `gpib-140b-specs`
- source_path: `gpib-140b-specs.html`
- source_url: https://docs-be.ni.com/bundle/gpib-140b-specs/raw/resource/enus/gpib-140b-specs.html
- document_id: `gpib-140b-specs`
- page_type: `leaf`
- content_type: `topic`
- source_description: GPIB-140B Specifications Definitions Warranted specifications describe the performance of a model under stated operating conditions and are covered by the model warranty. Characteristics describe values that are relevant to the use of the model under stated operating conditions but are not covered b

### GPIB-140B Specifications

#### GPIB-140B Specifications

#### Definitions

*Warranted* specifications describe the performance of a model under stated operating conditions and are covered by the model warranty.

*Characteristics* describe values that are relevant to the use of the model under stated operating conditions but are not covered by the model warranty.

- Typical specifications describe the performance
 met by a majority of models.
- Nominal specifications describe an attribute that
 is based on design, conformance testing, or supplemental testing.

Specifications are 
 *Typical* unless otherwise noted.

#### Conditions

Specifications are valid for 0 °C to 55 °C unless otherwise noted.

#### Cleaning Statement

Notice

GPIB-140B

#### System Configuration

| Distance per extension | Up to 1 km |
| --- | --- |
| Loading per extension | Up to 13 additional devices (28 total devices in the extension system, including the extenders) |
| Multiple extension | Permitted in any pattern of star or linear pattern |

#### Device Characteristics

| Transmission interface unit | Optical transmitter and receiver (HFBR1414, HFBR2416, or equivalent) with ST-style optical cable connectors |
| --- | --- |
| GPIB interface load | Two standard loads, AC and DC |

#### Performance Characteristics

| Maximum transfer rate Buffered mode, non-HS488>1.1 MBytes/s HS488 handshake>2.8 MBytes/s Unbuffered mode>200 kBytes/s |  |
| --- | --- |
| Maximum transfer rate |  |
| Buffered mode, non-HS488 | >1.1 MBytes/s |
| HS488 handshake | >2.8 MBytes/s |
| Unbuffered mode | >200 kBytes/s |
| Functionality | Transparent GPIB operation except for latched parallel polls |
| Interlocked IEEE 488 handshake | Maintained across the extension in unbuffered mode |
| IEEE 488 capability identification codes SH1Complete Source Handshake AH1Complete Acceptor Handshake T5, TE5Complete Talker L3, LE3Complete Listener SR1Complete Service Request RL1Complete Remote Local PP1, 2Complete Parallel Poll DC1Complete Device Clear DT1Complete Device Trigger C1-5Complete Controller E2Tri-state GPIB driver |  |
| IEEE 488 capability identification codes |  |
| SH1 | Complete Source Handshake |
| AH1 | Complete Acceptor Handshake |
| T5, TE5 | Complete Talker |
| L3, LE3 | Complete Listener |
| SR1 | Complete Service Request |
| RL1 | Complete Remote Local |
| PP1, 2 | Complete Parallel Poll |
| DC1 | Complete Device Clear |
| DT1 | Complete Device Trigger |
| C1-5 | Complete Controller |
| E2 | Tri-state GPIB driver |
| HS488 capability identification codes SHEHS-488 Source Handshake AHEHS-488 Acceptor Handshake |  |
| HS488 capability identification codes |  |
| SHE | HS-488 Source Handshake |
| AHE | HS-488 Acceptor Handshake |

#### Operational Characteristics

| Architecture | Point-to-point (not multi-drop) transmission |
| --- | --- |
| Operating modes | Buffered or unbuffered (interlocked) mode |
| HS488 modes | Enabled HS488 or disabled HS488 mode |
| Parallel Poll Response modes | Immediate Parallel Poll Response mode or latched Parallel Poll Response mode |

#### Power Requirements

| Input voltage range | 9 V DC to 15 V DC |
| --- | --- |
| Maximum power consumption | 3.0 W (250 mA @ 12 V) |
| 12 V DC Power Supply (NI PN 723595-02; shipped with the GPIB-140B) Input voltage range100 V AC to 240 V AC, 47 Hz to 63 Hz |  |
| 12 V DC Power Supply (NI PN 723595-02; shipped with the GPIB-140B) |  |
| Input voltage range | 100 V AC to 240 V AC, 47 Hz to 63 Hz |

#### GPIB-140B Pinout

Use the pinout to connect to terminals on the GPIB-140B.

Figure 1.

GPIB-140B

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

##### Dimensions and Weight

| Overall case size (dimensions) | 93.67 × 133.88 × 28.80 mm (3.69 × 5.27 × 1.13 in.) |
| --- | --- |
| Enclosure material | Aluminum |
| Weight | 323 g (11.4 oz) |

##### Field Wiring Specifications

| GPIB cable | Type X2 shielded |
| --- | --- |
| Transmission cable | 3.0 × 6.5 mm cable diameter62.5/125 micron core/clad with NA = 0.275850 nm operating wavelength​ 3.0 dB/km attenuation Duplex style, terminated with ST-style connectors; multi-mode |

#### Environmental Guidelines

Notice

GPIB-140B

Notice

##### Environmental Characteristics

| Operating | 0 °C to 55 °C |
| --- | --- |
| Storage | -20 °C to 70 °C |

| Operating | 10% RH to 90% RH, noncondensing |
| --- | --- |
| Storage | 5% RH to 95% RH, noncondensing |

| Pollution degree | 2 |
| --- | --- |

| Maximum altitude | 2,000 m (800 mbar), at 25 °C ambient temperature |
| --- | --- |

| Operating vibration | 5 Hz to 500 Hz, 0.3 g RMS |
| --- | --- |
| Non-operating vibration | 5 Hz to 500 Hz, 2.4 g RMS |
| Operating shock | 30 g, half-sine, 11 ms pulse |

#### Environmental Management

NI is committed to designing and manufacturing products in an environmentally responsible manner. NI recognizes that eliminating certain hazardous substances from our products is beneficial to the environment and to NI customers.

For additional environmental information, refer to the
 *Engineering a Healthy Planet* web page at [ni.com/environment](http://www.ni.com/en-us/about-ni/corporate-responsibility/environment.html). This page contains the environmental regulations
 and directives with which NI complies, as well as other environmental information not included
 in this document.

##### EU and UK Customers

[IMAGE alt='image' src='GUID-BB5A9EE4-1FE3-43AB-8ED8-E47DAFD24494-a5.svg']

ni.com/environment/weee

##### 电子信息产品污染控制管理办法（中国RoHS）

[IMAGE alt='image' src='GUID-C4CF8885-365B-494D-88C1-341E092C1FA0-a5.svg']

ni.com/environment/rohs_china

ni.com/environment/rohs_china

#### Product Certifications and Declarations

Refer to the product Declaration of Conformity (DoC)
 for additional regulatory compliance information. To obtain product certifications and the
 DoC for NI products, visit [ni.com/product-certifications](https://www.ni.com/en-us/support/documentation/product-certifications.html), search by model number, and click
 the appropriate link.

#### NI Services

Visit [ni.com/support](https://www.ni.com/en-us/support.html) to find support resources including documentation,
 downloads, and troubleshooting and application development self-help such as tutorials and
 examples.

Visit [ni.com/services](https://www.ni.com/en-us/shop/services.html) to learn about NI service offerings such as
 calibration options, repair, and replacement.

Visit [ni.com/register](https://www.ni.com/myni/products/en/) to register your NI product. Product registration facilitates
 technical support and ensures that you receive important information updates from NI.

NI corporate headquarters is located at 11500 N Mopac Expwy, Austin, TX, 78759-3504,
 USA.
