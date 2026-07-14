# NI DOCUMENT BUNDLE: pxie-1488-specs

<!--NI_BUNDLE_CHUNK bundle=pxie-1488-specs start=1 end=1 -->
<!--NI_TOPIC bundle=pxie-1488-specs path=specs.html language=enus -->
## TOPIC 00001: PXIe-1488 Specifications

- bundle_id: `pxie-1488-specs`
- source_path: `specs.html`
- source_url: https://docs-be.ni.com/bundle/pxie-1488-specs/raw/resource/enus/specs.html
- document_id: `pxie-1488-specs`
- page_type: `leaf`
- content_type: `topic`
- source_description: Introduction This document lists the specifications for the following variants of the PXIe-1488: PXIe-1488 FlexRIO FPD-Link IV Deserializer PXIe-1488 FlexRIO FPD-Link IV Serializer PXIe-1488 FlexRIO FPD-Link IV SerDes If you purchased the PXIe-1488 as part of an NI system, refer to your system docum

### PXIe-1488
 Specifications

#### Introduction

This document lists the specifications for the following variants of the PXIe-1488:

- PXIe-1488 FlexRIO FPD-Link IV Deserializer
- PXIe-1488 FlexRIO FPD-Link IV Serializer
- PXIe-1488 FlexRIO FPD-Link IV SerDes

Note

PXIe-1488

#### Definitions

*Warranted* specifications describe the performance of a model under stated operating conditions and are covered by the model warranty.

*Characteristics* describe values that are relevant to the use of the model under stated operating conditions but are not covered by the model warranty.

- Typical specifications describe the performance met by a
 majority of models.
- Nominal specifications describe an attribute that is based on
 design, conformance testing, or supplemental testing.
- Measured specifications describe the measured performance of a
 representative model.

Specifications are *Typical* unless otherwise noted.

#### Conditions

Specifications are valid under the following conditions unless otherwise noted.

- Ambient temperature of 23 °C 
 ±5 °C
- Installed in chassis with slot cooling capacity ≥58 W [[1]](#note-d288e161) [<sup>1</sup>](#fnsrc_1-d288e161) The
 PXIe-1488 SerDes module can operate in a
 chassis with a slot cooling capacity of <58
 W in a restricted user mode.

#### PXIe-1488 Pinout

##### Deserializer Pinout

Figure 1.

[IMAGE alt='PXIe-1488 Deserializer Front Panel' src='GUID-4C425002-D3F4-435F-93BD-E0C84060F534-a5.svg']

| Signal Name | Description | FlexRIO Terminal Name |
| --- | --- | --- |
| SI 0 | Serial input to internal deserializer | SI0 |
| SI 1 | Serial input to internal deserializer | SI1 |
| SI 2 | Serial input to internal deserializer | SI2 |
| SI 3 | Serial input to internal deserializer | SI3 |
| SI 4 | Serial input to internal deserializer | SI4 |
| SI 5 | Serial input to internal deserializer | SI5 |
| SI 6 | Serial input to internal deserializer | SI6 |
| SI 7 | Serial input to internal deserializer | SI7 |

Figure 2.

[IMAGE alt='image' src='GUID-FC272454-C619-4C76-A5D9-577C3EA89DFF-a5.svg']

| Signal Pin | Description |
| --- | --- |
| 1 | Power supply for channel SI 0 |
| 2 | Power supply for channel SI 1 |
| 3 | Digital/chassis grounding |
| 4 | Digital/chassis grounding |
| 5 | Power supply for channel SI 2 |
| 6 | Power supply for channel SI 3 |
| 7 | Power supply for channel SI 4 |
| 8 | Power supply for channel SI 5 |
| 9 | Digital/chassis grounding |
| 10 | Digital/chassis grounding |
| 11 | Power supply for channel SI 6 |
| 12 | Power supply for channel SI 7 |

##### Serializer Pinout

Figure 3.

[IMAGE alt='PXIe-1488 Serializer Front Panel' src='GUID-BC4EE37E-AD2E-48F1-B59E-EAF69494ED21-a5.svg']

| Signal Name | Description | FlexRIO Terminal Name |
| --- | --- | --- |
| SO 0 | Serial output from internal serializer | SO0 |
| SO 1 | Serial output from internal serializer | SO1 |
| SO 2 | Serial output from internal serializer | SO2 |
| SO 3 | Serial output from internal serializer | SO3 |
| SO 4 | Serial output from internal serializer | SO4 |
| SO 5 | Serial output from internal serializer | SO5 |
| SO 6 | Serial output from internal serializer | SO6 |
| SO 7 | Serial output from internal serializer | SO7 |

Figure 4.

[IMAGE alt='image' src='GUID-FC272454-C619-4C76-A5D9-577C3EA89DFF-a5.svg']

| Signal Pin | Description |
| --- | --- |
| 1 | Power sink for channel SO 0 |
| 2 | Power sink for channel SO 1 |
| 3 | Digital/chassis grounding |
| 4 | Digital/chassis grounding |
| 5 | Power sink for channel SO 2 |
| 6 | Power sink for channel SO 3 |
| 7 | Power sink for channel SO 4 |
| 8 | Power sink for channel SO 5 |
| 9 | Digital/chassis grounding |
| 10 | Digital/chassis grounding |
| 11 | Power sink for channel SO 6 |
| 12 | Power sink for channel SO 7 |

##### SerDes Pinout

Figure 5.

[IMAGE alt='PXIe-1488 SerDes Front Panel' src='GUID-908A6A05-0F71-407E-9FD1-93228646866A-a5.svg']

| Signal Name | Description | FlexRIO Terminal Name |
| --- | --- | --- |
| SO 0 | Serial output from internal serializer | SO0 |
| SI 0 | Serial input to internal deserializer | SI0 |
| SO 1 | Serial output from internal serializer | SO1 |
| SI 1 | Serial input to internal deserializer | SI1 |
| SO 2 | Serial output from internal serializer | SO2 |
| SI 2 | Serial input to internal deserializer | SI2 |
| SO 3 | Serial output from internal serializer | SO3 |
| SI 3 | Serial input to internal deserializer | SI3 |

Figure 6.

[IMAGE alt='image' src='GUID-FAD5E1A6-5C04-4A1C-869B-E68522F6D9C1-a5.svg']

| Signal Pin | Description |
| --- | --- |
| 1 | Power sink for channel SO 0 |
| 2 | Power supply for channel SI 0 |
| 3 | Digital/chassis grounding |
| 4 | Digital/chassis grounding |
| 5 | Power sink for channel SO 1 |
| 6 | Power supply for channel SI 1 |
| 7 | Power sink for channel SO 2 |
| 8 | Power supply for channel SI 2 |
| 9 | Digital/chassis grounding |
| 10 | Digital/chassis grounding |
| 11 | Power sink for channel SO 3 |
| 12 | Power supply for channel SI 3 |

#### Serial Device Compatibility

Refer to the following information to verify that the PXIe-1488 module chip set is compatible with your serial
 device or camera.

| Chip set brand | Texas Instruments |
| --- | --- |
| Module deserializer | DS90UB9702 |
| Module serializer | DS90UB971 |
| Supported mated SerDes | Input channel: DS90UB971, DS90UB953, DS90UB951, DS90UB935 Output channel: DS90UB9702, DS90UB954, DS90UB960, DS90UB962, DS90UB936 |
| Supported clock modes | Synchronous mode, Non-synchronous mode |
| Support Data Formats | CSI-2 only, no DVP (digital video port) |
| Supported FPD-Link modes | FPD-Link III, FPD-Link IV |

Note

Note

PXIe-1488

#### Bus Interface

| Form factor | PCI Express Gen-3 x8 |
| --- | --- |

#### Reconfigurable FPGA

The following table lists the specifications for the PXIe-1488
 FPGA.

| FPGA | KU11P |
| --- | --- |
| LUTs | 298,560 |
| DSP48 slices (25 × 18 multiplier) | 2,928 |
| Embedded Block RAM | 21 Mb |
| Timebase reference sources | PXI Express 100 MHz (PXIe_CLK100) |
| Data transfers | DMA, interrupts, programmed I/O |
| Embedded UltraRAM™ | 22 Mb |
| Number of DMA channels | 60 |

Note

##### Onboard DRAM

| Memory size | 4 GB (2 banks of 2 GB) |
| --- | --- |
| DRAM clock rate | 1064 MHz |
| Physical bus width | 32 bit |
| LabVIEW FPGA DRAM clock rate | 267 MHz |
| LabVIEW FPGA DRAM bus width | 256 bit per bank |
| Maximum theoretical data rate | 17 GB/s (8.5 GB/s per bank) |

#### Serial I/O Characteristics

##### Input Channels

| Connector label | SI |
| --- | --- |
| Connector type | HFM Male Code Z, coaxial |
| Power over Coax (PoC) output range, AUX power maximum | 6 V to 32 V, 800 mA per channel |

##### PoC Output Range, Internal Power
 Supply

| Nominal voltage | 12 V |
| --- | --- |
| Maximum current | 400 mA per channel, 2 A total |

| I/O standard | FPD-Link IV with PoC |
| --- | --- |
| Maximum data rate | 7.55 Gb/s |
| Reference clock speed | 25 MHz |

##### Output Channels

| Connector label | SO |
| --- | --- |
| Connector type | HFM Male Code Z, coaxial |

##### PoC Input Range

| Nominal voltage | 6 V to 32 V |
| --- | --- |
| Maximum current | 800 mA per channel |

| I/O standard | FPD-Link IV with PoC |
| --- | --- |
| Maximum data rate | 7.55 Gb/s |
| Reference clock speed | 23.59275 MHz to 26 MHz |

##### AUX Power Channels

| Power sink or source maximum voltage | 6 V to 32 V |
| --- | --- |
| Power sink or source maximum current | 800 mA per channel |
| Power connector type | Conn Terminal Block, Weidmuller part number 2439690000 |

##### Power Connector Wiring

| Gauge | 0.08 mm2 to 0.5 mm2 (28 AWG to 20 AWG) |
| --- | --- |
| Wire strip length | 8 mm |
| Terminal connection type | Tension clamp |
| Retention | External strain relief of AUX power connections recommended |

##### PXIe-1488
 Deserializer

| Input channels | 8 |
| --- | --- |
| Communication | I2C, GPIO, CSI-2 |
| CSI-2 interface | D-PHY, 1, 2, or 4 lanes, 600 Mb/s to 1,500 Mb/s per lane, no lane swaps or inversions |

##### PXIe-1488
 Serializer

| Output channels | 8 |
| --- | --- |
| Communication | I2C, GPIO, CSI-2 |
| CSI-2 interface | D-PHY, 1, 2, or 4 lanes, 600 Mb/s to 1,500 Mb/s per lane, no lane swaps or inversions |

##### PXIe-1488
 SerDes

| Input channels | 4 |
| --- | --- |
| Output channels | 4 |
| Maximum Tap pairs per module | 4 |
| Communication | I2C, GPIO, CSI-2 |
| CSI-2 interface | D-PHY, 1, 2, or 4 lanes, 600 Mb/s to 1,500 Mb/s per lane, no lane swaps or inversions |

#### Power Requirements

Note

Note

Note

PXIe-1488

##### Backplane Power Source

| 3.3 V | 3.0 A, maximum |
| --- | --- |
| 12 V | 6.0 A, maximum |

##### Backplane Power

| Total power | 82 W, maximum |
| --- | --- |

##### Power over Coax (PoC) Source, External
 Power Supply

| Voltage range | 6 V to 32 V |
| --- | --- |
| Maximum current | 800 mA per channel, up to 8 channels |

##### Power over Coax (PoC) Source, Internal
 Power Supply

| Nominal voltage | 12 V |
| --- | --- |
| Maximum current | 400 mA per channel, up to 2 A total |

##### Diagnostic PoC Current
 Measurement

| Current measurement range | 50 mA to 800 mA |
| --- | --- |
| Current measurement accuracy | 50 mA to 100 mA: ±20% 100 mA to 800 mA: ±15% |

##### Diagnostic PoC Voltage Measurement

| Voltage measurement range | 6 V to 32 V |
| --- | --- |
| Voltage measurement accuracy[2]2 Due to resistive (IR drop) losses in the circuit, actual voltage measurement accuracy depends on the load of the PoC circuit. | ±2.5% |

#### Environmental Characteristics

| Operating temperature | 0 °C to 55 °C[3]3 The PXIe-1488 requires a chassis with slot cooling capacity ≥58 W. Not all chassis with slot cooling capacity ≥58 W can achieve this ambient temperature range. Refer to the chassis specifications at ni.com/docs to determine the ambient temperature ranges your chassis can achieve. |
| --- | --- |
| Storage temperature | -40 °C to 71 °C |
| Operating humidity | 10% to 90%, noncondensing |
| Storage humidity | 5% to 95%, noncondensing |

| Pollution degree | 2 |
| --- | --- |
| Maximum altitude | 2,000 m (800 mbar) (at 25 °C ambient temperature) |

| Operating vibration | 5 Hz to 500 Hz, 0.3 g RMS |
| --- | --- |
| Non-operating vibration | 5 Hz to 500 Hz, 2.4 g RMS |
| Operating shock | 30 g, half-sine, 11 ms pulse |

#### Physical

| Dimensions | 3U, two-slot PXI Express module, 21.6 cm × 4.1 cm × 13.0 cm (8.5 in. × 1.6 in. × 5.1 in.) |
| --- | --- |
| Weight | 650 g (22.93 oz) |

#### Timing and Synchronization

| Timebase | 100 MHz, shared by all ports, disciplined by PXI_Clk100 |
| --- | --- |
| Trigger I/O source | PXI_Trig <0:7> |

[<sup>1</sup>](#note_ref-d288e161) The
 PXIe-1488 SerDes module can operate in a
 chassis with a slot cooling capacity of <58
 W in a restricted user mode.

[<sup>2</sup>](#note_ref-d288e2271) Due to resistive (IR drop) losses in the
 circuit, actual voltage measurement accuracy depends on the load of the PoC
 circuit.

[<sup>3</sup>](#note_ref-d288e2320) The
 PXIe-1488 requires a chassis with slot cooling
 capacity ≥58 W. Not all chassis with slot cooling
 capacity ≥58 W can achieve this ambient temperature range. Refer to the
 chassis specifications at [ni.com/docs](https://ni.com/docs) to determine the ambient temperature
 ranges your chassis can achieve.
