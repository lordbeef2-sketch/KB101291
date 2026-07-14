# NI DOCUMENT BUNDLE: labview-reference-design-wireless-research-ni-ettus-usrp-x410-specs

<!--NI_BUNDLE_CHUNK bundle=labview-reference-design-wireless-research-ni-ettus-usrp-x410-specs start=1 end=1 -->
<!--NI_TOPIC bundle=labview-reference-design-wireless-research-ni-ettus-usrp-x410-specs path=specs.html language=enus -->
## TOPIC 00001: LabVIEW Reference Design for Wireless Research with NI Ettus USRP X410

- bundle_id: `labview-reference-design-wireless-research-ni-ettus-usrp-x410-specs`
- source_path: `specs.html`
- source_url: https://docs-be.ni.com/bundle/labview-reference-design-wireless-research-ni-ettus-usrp-x410-specs/raw/resource/enus/specs.html
- document_id: `labview-reference-design-wireless-research-ni-ettus-usrp-x410-specs`
- page_type: `leaf`
- content_type: `topic`
- source_description: Multi-Channel Rx Recording (Single Device)-PXIe Option with PXIe-8267 Parameter X410 Only X410 + mmWave Extension Frequency Band 1 MHz - 7.2 GHz 28 GHz Channels 4 1 Digital Interface PCIe PCIe Recording IQ Rate 1 channel Up to 491 MSps Up to 491 MSps 2 channels Up to 491 MSps 4 channels Up to 245.76

LabVIEW Reference Design for Wireless
 Research with NI Ettus USRP X410

#### Multi-Channel Rx Recording (Single
 Device)-PXIe Option with PXIe-8267

| Parameter | X410 Only | X410 + mmWave Extension |  |
| --- | --- | --- | --- |
| Frequency Band | 1 MHz - 7.2 GHz | 28 GHz |  |
| Channels | 4 | 1 |  |
| Digital Interface | PCIe | PCIe |  |
| Recording IQ Rate | 1 channel | Up to 491 MSps | Up to 491 MSps |
| 2 channels | Up to 491 MSps |  |  |
| 4 channels | Up to 245.76 MSps |  |  |
| Storage | 4 TB with PXIe-8267 | 4 TB with PXIe-8267 |  |
| Software | LabVIEW 2022 Q3 (64-bit) | LabVIEW 2022 Q3 (64-bit) |  |

For more information about setting up the hardware that supports the above features, refer to
 the *LabVIEW Reference Design for Wireless Research with NI
 Ettus USRP X410 Getting Started*.

Related information:

- LabVIEW Reference Design for Wireless Research with NI Ettus USRP
 X410 Getting Started

#### Multi-Channel Tx Playback (Single
 Device)-PXIe Option with PXIe-8267

| Parameter | X410 Only |  |
| --- | --- | --- |
| Frequency Band | 1 MHz - 7.2 GHz |  |
| Channels | 4 |  |
| Digital Interface | PCIe |  |
| Tx Streaming IQ Rate | 1 channel | Up to 491 MSps |
| 2 channels | Up to 491 MSps |  |
| 4 channels | Up to 245.76 MSps |  |
| Storage | 4 TB with PXIe-8267 |  |
| Software | LabVIEW 2022 Q3 (64-bit) |  |

For more information about setting up the hardware that supports the above features, refer to
 the *LabVIEW Reference Design for Wireless Research with NI
 Ettus USRP X410 Getting Started*.

Related information:

- LabVIEW Reference Design for Wireless Research with NI Ettus USRP
 X410 Getting Started

#### 5G Signal Generating/Processing System
 Parameters

| Number of Tx Channels | 1 |
| --- | --- |
| Number of Rx Channels | 1 |
| Tx Function | 5G NR playback |
| Rx Function | 5G NR Spectrum (Burst) 5G NR EVM (Burst) One Channel Streaming (Continuous, up to 491 MSps) |
| mmWave Extension (Optional) | Support TMYTEK UD/BBox (UD Box Dual Channel, BBox One 28 G and BBox Lite 28 G) |

| Tx | Rx | Test Conditions | EVM (Typical) | Comment |
| --- | --- | --- | --- | --- |
| X410 | X410 | NR DL 100 MHz/256-QAM/30 KSCS@CHP=-29 dBm​ Frequency = 2 GHz​ | -40 dB | Refer to the X410 specifications |
| X410 | X410 | NR DL 400 M/256-QAM/120KSCS@CHP=-28 dBm​ Frequency = 2 GHz​ | -38 dB |  |
| X410 + mmWave[1]1 X410 + mmWave result is measured with TMYTEK UD/BBox for reference. | X410 + mmWave | NR DL 400 M/256-QAM/120KSCS@CHP=-xx dBm​ Frequency = 28 GHz​ | -35 dB | Adjust gain of X410, gain of BBox to achieve optimized EVM |

For more information about hardware-related parameters, refer to the X410 specifications.

For more information about 5G NR-related parameters, refer to the RFmx NR specifications.

Related information:

- Ettus USRP X410 Specifications
- RFmx NR Specifications

#### Fast Beam Steering with USRP X410

Using fast beam steering with USRP X410 requires the hardware components in the
 following table. Refer to the product documentation for these hardware components to view
 detailed specifications.

| Hardware Component | Specifications |
| --- | --- |
| Ettus USRP X410 | Refer to the Ettus USRP X410 Specifications. |
| PXIe-1092 | Refer to the PXIe-1092 Specifications. |
| PXIe-8881 | Refer to the PXIe-8881 Specifications. |
| PXIe-8394 | Refer to the PXIe-8394 (156874x-04L) Specifications. |
| MXI-Express cable | Gen 3 x8, 3 m |
| SMA cable assembly for connections between Ettus USRP X410 and TMYTEK-NI UD Box 5G Series | Coax, RG-402, 50 Ω, 1 m |
| TMYTEK-NI BBox One 5G 28GHz | Refer to the TMYTEK-NI BBox™ One 5G Datasheet. |
| TMYTEK-NI BBox Lite 5G 28GHz | Refer to the TMYTEK-NI BBox™ Lite 5G Datasheet. |
| TMYTEK-NI UD Box 5G Series | Refer to the TMYTEK-NI UD Box 5G Series Datasheet. |

Use the following connector pin assignments when you use fast beam steering with USRP
 X410.

| X410 Front Panel HDMI I/O Connector | HDMI Pin Name | USRP RIO (LV FPGA) IO Node Terminal Name | TMYTEK SPI Definition |
| --- | --- | --- | --- |
| GPIO0/GPIO1 | HDMI_Pin 1 | GPIO 0 OUT 0/GPIO 1 OUT 0 | SPI_CSB |
| HDMI_Pin 2 | GPIO 0 OUT 11/GPIO 1 OUT 11 | GND |  |
| HDMI_Pin 4 | GPIO 0 OUT 2/GPIO 1 OUT 2 | SPI_TX_EN |  |
| HDMI_Pin 6 | GPIO 0 OUT 3/GPIO 1 OUT 3 | SPI_CLK |  |
| HDMI_Pin 7 | GPIO 0 OUT 4/GPIO 1 OUT 4 | SPI_PDI |  |
| HDMI_Pin 9 | GPIO 0 OUT 5/GPIO 1 OUT 5 | SPI_SDI |  |
| HDMI_Pin 10 | GPIO 0 OUT 6/GPIO 1 OUT 6 | SPI_LDB |  |
| HDMI_Pin 12 | GPIO 0 OUT 7/GPIO 1 OUT 7 | SPI_SDO |  |
| HDMI_Pin 15 | GPIO 0 OUT 9/GPIO 1 OUT 9 | SPI_RX_EN |  |

Related information:

- Ettus USRP X410 Specifications
- PXIe-1092 Specifications
- PXIe-8881 Specifications
- PXIe-8394 (156874x-04L) Specifications
- TMYTEK-NI BBox™ One 5G Datasheet
- TMYTEK-NI BBox™ Lite 5G Datasheet
- TMYTEK-NI UD Box 5G Series Datasheet

[<sup>1</sup>](#note_ref-d470e578) X410 + mmWave
 result is measured with TMYTEK UD/BBox for
 reference.
