# NI DOCUMENT BUNDLE: rfmxinstr-c-api-ref

<!--NI_BUNDLE_CHUNK bundle=rfmxinstr-c-api-ref start=1 end=103 -->
<!--NI_TOPIC bundle=rfmxinstr-c-api-ref path=group____root__ni_r_fmx_instr__attributes__advanced_1ga93b93a49fbae9c9bab209202e49eb2a4.html language=enus -->
## TOPIC 00001: RFMXINSTR_ATTR_CLEANER_SPECTRUM

- bundle_id: `rfmxinstr-c-api-ref`
- source_path: `group____root__ni_r_fmx_instr__attributes__advanced_1ga93b93a49fbae9c9bab209202e49eb2a4.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_instr__attributes__advanced_1ga93b93a49fbae9c9bab209202e49eb2a4.html
- document_id: `rfmxinstr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies how to obtain the lowest noise floor or faster measurement speed. SyntaxRFMXINSTR_ATTR_CLEANER_SPECTRUMNumeric ValueData TypeAccessApplies To37int32Read/WriteN/ARemarksName (value)DescriptionPXIe-5665Sets the FFT Width attribute to take narrower bandwidth acquisitions and avoid digitizer s

### RFMXINSTR_ATTR_CLEANER_SPECTRUM

Specifies how to obtain the lowest noise floor or faster measurement speed.

#### Syntax

RFMXINSTR_ATTR_CLEANER_SPECTRUM

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 37 | int32 | Read/Write | N/A |

#### Remarks

| Name (value) | Description |
| --- | --- |
| PXIe-5665 | Sets the FFT Width attribute to take narrower bandwidth acquisitions and avoid digitizer spurs. Uses IF filters to reduce the noise floor for frequencies below 80 MHz. |
| PXIe-5644/5645/5646, PXIe-5840/5841/5842 | Returns the best possible spectrum. |
| PXIe-5668 | Returns the best possible spectrum. To provide the best spectrum measurement, the acquisition is reduced to 100 MHz segments for any center frequency. |
| Other devices | This attribute is ignored. |

Note

Some measurements, such as Spurious Emissions enable the Cleaner Spectrum attribute by default. You can speed up those measurements by disabling the Cleaner Spectrum attribute.

You do not need to use a selector string if you want to configure this attribute for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax.

The default value is **Disabled**.

**Supported devices**: PXIe-5665, PXIe-5668, PXIe-5644/5645/5646, PXIe-5840/5841/5842/5860

| Name | Value | Description |
| --- | --- | --- |
| RFMXINSTR_VAL_CLEANER_SPECTRUM_DISABLED | 0 (0x0) | Disable this attribute to get faster measurement speed. |
| RFMXINSTR_VAL_CLEANER_SPECTRUM_ENABLED | 1 (0x1) | Enable this attribute to get the lowest noise floor and avoid digitizer spurs. |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxinstr-c-api-ref path=group____root__ni_r_fmx_instr__attributes__advanced_1ga992836b9a606ebec9d6addfa291f8030.html language=enus -->
## TOPIC 00002: RFMXINSTR_ATTR_SUBSPAN_OVERLAP

- bundle_id: `rfmxinstr-c-api-ref`
- source_path: `group____root__ni_r_fmx_instr__attributes__advanced_1ga992836b9a606ebec9d6addfa291f8030.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_instr__attributes__advanced_1ga992836b9a606ebec9d6addfa291f8030.html
- document_id: `rfmxinstr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use subspan overlap process to eliminate or reduce analyzer spurs. To enable this feature, specify a non-zero percentage overlap between consecutive subspans in a spectrum acquisition. SyntaxRFMXINSTR_ATTR_SUBSPAN_OVERLAPNumeric ValueData TypeAccessApplies To50float64Read/WriteN/ARemarks If a value

### RFMXINSTR_ATTR_SUBSPAN_OVERLAP

Use subspan overlap process to eliminate or reduce analyzer spurs. To enable this feature, specify a non-zero percentage overlap between consecutive subspans in a spectrum acquisition.

#### Syntax

RFMXINSTR_ATTR_SUBSPAN_OVERLAP

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 50 | float64 | Read/Write | N/A |

#### Remarks

If a value greater than 0 is specified, then for each spectral line in the resulting spectrum, the driver acquires data twice with slightly different hardware settings, so that the analyzer spurs, if any, are present at different frequencies in the two acquisitions. Typically, LO frequency is shifted between the acquisitions causing analyzer spurs that are relative to the LO frequency, to move from one frequency to another. Those spurs, which are present in only one of the acquisitions for each spectral line, get removed.

Note

Subspan overlap process effectively is performing minimum averaging, which might reduce the measured noise floor level. RFmx Spectrum Averaging can be enabled to minimize the effect of subspan overlap on the noise floor.

Note

RFmx may apply further shifts to the specified value to accommodate fixed-frequency edges of components such as preselectors.

You do not need to use a selector string if you want to configure this attribute for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax.

The default value is 0.

**Valid values**

| Name (value) | Description |
| --- | --- |
| PXIe-5820/5830/5831/5832/5840/5841/5860 | 0 |
| PXIe-5842 | 0, 50 |
| PXIe-5665/5668 | 0 to <100 |

**Supported devices**: PXIe-5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxinstr-c-api-ref path=group____root__ni_r_fmx_instr__attributes__advanced_1ga9b0cb3fc627953463ac0025c7b8e0f97.html language=enus -->
## TOPIC 00003: RFMXINSTR_ATTR_TEMPERATURE_READ_INTERVAL

- bundle_id: `rfmxinstr-c-api-ref`
- source_path: `group____root__ni_r_fmx_instr__attributes__advanced_1ga9b0cb3fc627953463ac0025c7b8e0f97.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_instr__attributes__advanced_1ga9b0cb3fc627953463ac0025c7b8e0f97.html
- document_id: `rfmxinstr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the minimum time difference between temperature sensor readings. This value is expressed in seconds. SyntaxRFMXINSTR_ATTR_TEMPERATURE_READ_INTERVALNumeric ValueData TypeAccessApplies To119float64Read/WriteN/ARemarks When you call the RFmx Initiate function, RFmx checks if the amount of tim

### RFMXINSTR_ATTR_TEMPERATURE_READ_INTERVAL

Specifies the minimum time difference between temperature sensor readings. This value is expressed in seconds.

#### Syntax

RFMXINSTR_ATTR_TEMPERATURE_READ_INTERVAL

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 119 | float64 | Read/Write | N/A |

#### Remarks

When you call the RFmx Initiate function, RFmx checks if the amount of time specified by this attribute has elapsed before reading the hardware temperature.

Note

RFmx ignores Temperature Read Interval attribute if you read the [RFMXINSTR_ATTR_DOWNCONVERTER_GAIN](group____root__ni_r_fmx_instr__attributes__advanced_1ga085790ced7f69901469f2a45963d61cb.html) attribute.

You do not need to use a selector string if you want to configure this attribute for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax.

The default value is 30 seconds.

**Supported devices**: PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxinstr-c-api-ref path=group____root__ni_r_fmx_instr__attributes__advanced_1ga9d5505b27d225cc16509ca572d8aa47a.html language=enus -->
## TOPIC 00004: RFMXINSTR_ATTR_SMU_CHANNEL

- bundle_id: `rfmxinstr-c-api-ref`
- source_path: `group____root__ni_r_fmx_instr__attributes__advanced_1ga9d5505b27d225cc16509ca572d8aa47a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_instr__attributes__advanced_1ga9d5505b27d225cc16509ca572d8aa47a.html
- document_id: `rfmxinstr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the output channel to be used for noise figure (NF) measurement in RFmx. SyntaxRFMXINSTR_ATTR_SMU_CHANNELNumeric ValueData TypeAccessApplies To72char[]Read/WriteN/ARemarks The default value is 0.

### RFMXINSTR_ATTR_SMU_CHANNEL

Specifies the output channel to be used for noise figure (NF) measurement in RFmx.

#### Syntax

RFMXINSTR_ATTR_SMU_CHANNEL

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 72 | char[] | Read/Write | N/A |

#### Remarks

The default value is 0.

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxinstr-c-api-ref path=group____root__ni_r_fmx_instr__attributes__advanced_1gaa1f18676fa0a7d6584572cc9ab82762c.html language=enus -->
## TOPIC 00005: RFMXINSTR_ATTR_OPTIMIZE_PATH_FOR_SIGNAL_BANDWIDTH

- bundle_id: `rfmxinstr-c-api-ref`
- source_path: `group____root__ni_r_fmx_instr__attributes__advanced_1gaa1f18676fa0a7d6584572cc9ab82762c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_instr__attributes__advanced_1gaa1f18676fa0a7d6584572cc9ab82762c.html
- document_id: `rfmxinstr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Optimizes RF path for the signal bandwidth that is centered on the IQ carrier frequency. SyntaxRFMXINSTR_ATTR_OPTIMIZE_PATH_FOR_SIGNAL_BANDWIDTHNumeric ValueData TypeAccessApplies To91int32Read/WriteN/ARemarks You can disable this attribute to avoid changes to the RF path when changing the signal ba

### RFMXINSTR_ATTR_OPTIMIZE_PATH_FOR_SIGNAL_BANDWIDTH

Optimizes RF path for the signal bandwidth that is centered on the IQ carrier frequency.

#### Syntax

RFMXINSTR_ATTR_OPTIMIZE_PATH_FOR_SIGNAL_BANDWIDTH

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 91 | int32 | Read/Write | N/A |

#### Remarks

You can disable this attribute to avoid changes to the RF path when changing the signal bandwidth.

You do not need to use a selector string if you want to configure this attribute for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax.

The default value is **Automatic**.

**Supported devices**: PXIe-5830/5831/5832/5841/5842

| Name | Value | Description |
| --- | --- | --- |
| RFMXINSTR_VAL_OPTIMIZE_PATH_FOR_SIGNAL_BANDWIDTH_DISABLED | 0 (0x0) | Disables the optimized path for signal bandwidth. |
| RFMXINSTR_VAL_OPTIMIZE_PATH_FOR_SIGNAL_BANDWIDTH_ENABLED | 1 (0x1) | Enables the optimized path for signal bandwidth. |
| RFMXINSTR_VAL_OPTIMIZE_PATH_FOR_SIGNAL_BANDWIDTH_AUTOMATIC | 2 (0x2) | Automatically enables the optimized path based on other configurations. |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxinstr-c-api-ref path=group____root__ni_r_fmx_instr__attributes__advanced_1gaa3bafc1d089210bd395ae6bbdd5f7d7a.html language=enus -->
## TOPIC 00006: RFMXINSTR_ATTR_THERMAL_CORRECTION_TEMPERATURE_RESOLUTION

- bundle_id: `rfmxinstr-c-api-ref`
- source_path: `group____root__ni_r_fmx_instr__attributes__advanced_1gaa3bafc1d089210bd395ae6bbdd5f7d7a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_instr__attributes__advanced_1gaa3bafc1d089210bd395ae6bbdd5f7d7a.html
- document_id: `rfmxinstr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the temperature change required before RFmx recalculates the thermal correction settings when entering the running state. This value is expressed in degree Celsius. SyntaxRFMXINSTR_ATTR_THERMAL_CORRECTION_TEMPERATURE_RESOLUTIONNumeric ValueData TypeAccessApplies To120float64Read/WriteN/ARe

### RFMXINSTR_ATTR_THERMAL_CORRECTION_TEMPERATURE_RESOLUTION

Specifies the temperature change required before RFmx recalculates the thermal correction settings when entering the running state. This value is expressed in degree Celsius.

#### Syntax

RFMXINSTR_ATTR_THERMAL_CORRECTION_TEMPERATURE_RESOLUTION

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 120 | float64 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string if you want to configure this attribute for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax.

**Default value**

| Name (value) | Description |
| --- | --- |
| PXIe-5830/5831/5832/5842/5860 | 0.2 |
| PXIe-5840/5841 | 1.0 |

**Supported devices**: PXIe-5830/5831/5832/5840/5841/5842/5860

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxinstr-c-api-ref path=group____root__ni_r_fmx_instr__attributes__advanced_1gaae5331f67477d745b2e6fad519ff1f92.html language=enus -->
## TOPIC 00007: RFMXINSTR_ATTR_IF_FILTER_BANDWIDTH

- bundle_id: `rfmxinstr-c-api-ref`
- source_path: `group____root__ni_r_fmx_instr__attributes__advanced_1gaae5331f67477d745b2e6fad519ff1f92.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_instr__attributes__advanced_1gaae5331f67477d745b2e6fad519ff1f92.html
- document_id: `rfmxinstr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the IF filter path bandwidth for your device configuration. SyntaxRFMXINSTR_ATTR_IF_FILTER_BANDWIDTHNumeric ValueData TypeAccessApplies To48float64Read/WriteN/ARemarksName (value)Description-Note For composite devices, such as the PXIe-5665/5668, the IF filter path bandwidth includes all I

### RFMXINSTR_ATTR_IF_FILTER_BANDWIDTH

Specifies the IF filter path bandwidth for your device configuration.

#### Syntax

RFMXINSTR_ATTR_IF_FILTER_BANDWIDTH

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 48 | float64 | Read/Write | N/A |

#### Remarks

| Name (value) | Description |
| --- | --- |
| - | Note For composite devices, such as the PXIe-5665/5668, the IF filter path bandwidth includes all IF filters across the component modules of a composite device. |

RFmx chooses an appropriate IF filter as default IF Filter based on measurement configuration, center frequency, cleaner spectrum and downconverter preselector.

You do not need to use a selector string if you want to configure this attribute for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax.

**Supported devices**: PXIe-5665/5668

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxinstr-c-api-ref path=group____root__ni_r_fmx_instr__attributes__advanced_1gad3b194d7b38850f4886ef57534dfa335.html language=enus -->
## TOPIC 00008: RFMXINSTR_ATTR_MIXER_LEVEL_OFFSET

- bundle_id: `rfmxinstr-c-api-ref`
- source_path: `group____root__ni_r_fmx_instr__attributes__advanced_1gad3b194d7b38850f4886ef57534dfa335.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_instr__attributes__advanced_1gad3b194d7b38850f4886ef57534dfa335.html
- document_id: `rfmxinstr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of dB by which to adjust the device mixer level. SyntaxRFMXINSTR_ATTR_MIXER_LEVEL_OFFSETNumeric ValueData TypeAccessApplies To15float64Read/WriteN/ARemarks Specifying a positive value for this attribute configures the device for moderate distortion and low noise, and specifying

### RFMXINSTR_ATTR_MIXER_LEVEL_OFFSET

Specifies the number of dB by which to adjust the device mixer level.

#### Syntax

RFMXINSTR_ATTR_MIXER_LEVEL_OFFSET

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 15 | float64 | Read/Write | N/A |

#### Remarks

Specifying a positive value for this attribute configures the device for moderate distortion and low noise, and specifying a negative value results in low distortion and higher noise. You cannot set the [RFMXINSTR_ATTR_MIXER_LEVEL_OFFSET](group____root__ni_r_fmx_instr__attributes__advanced_1gad3b194d7b38850f4886ef57534dfa335.html) and [RFMXINSTR_ATTR_MIXER_LEVEL](group____root__ni_r_fmx_instr__attributes__advanced_1ga9c3c02fd682285746697d30891b3d4f9.html) attributes at the same time.

You do not need to use a selector string if you want to configure this attribute for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax.

The default value is 0. The default value specifies device settings that are the best compromise between distortion and noise.

**Supported devices**: PXIe-5663/5663E/5665/5668

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxinstr-c-api-ref path=group____root__ni_r_fmx_instr__attributes__advanced_1gafa3f7f972764fba0440c8ea890a6158d.html language=enus -->
## TOPIC 00009: RFMXINSTR_ATTR_FREQUENCY_SETTLING

- bundle_id: `rfmxinstr-c-api-ref`
- source_path: `group____root__ni_r_fmx_instr__attributes__advanced_1gafa3f7f972764fba0440c8ea890a6158d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_instr__attributes__advanced_1gafa3f7f972764fba0440c8ea890a6158d.html
- document_id: `rfmxinstr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the value used for LO frequency settling. SyntaxRFMXINSTR_ATTR_FREQUENCY_SETTLINGNumeric ValueData TypeAccessApplies To10float64Read/WriteN/ARemarks Specify the units and interpretation for this scalar value using the RFMXINSTR_ATTR_FREQUENCY_SETTLING_UNITS attribute.Valid valuesFrequency

### RFMXINSTR_ATTR_FREQUENCY_SETTLING

Specifies the value used for LO frequency settling.

#### Syntax

RFMXINSTR_ATTR_FREQUENCY_SETTLING

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 10 | float64 | Read/Write | N/A |

#### Remarks

Specify the units and interpretation for this scalar value using the [RFMXINSTR_ATTR_FREQUENCY_SETTLING_UNITS](group____root__ni_r_fmx_instr__attributes__advanced_1ga6a7eaf94ca4f5fba6344796855f3ca9b.html) attribute.

**Valid values**

| Frequency Settling Units Property Value | PXIe-5663/5663E | PXIe-5665/5668 | PXIe-5644/5645/5646 | PXIe-5830/5831/5832/5840/5841/5842, PXIe-5831 with PXIe-5653 (using PXIe-3622 LO), PXIe-5832 with PXIe-5653 (using PXIe-3623 LO) | PXIe-5831 with PXIe-5653 (using PXIe-5653 LO) and PXIe-5832 with PXIe-5653 (using PXIe-5653 LO) |
| --- | --- | --- | --- | --- | --- |
| Seconds After Lock | 2 µs to 80 ms, resolution of approximately 2 µs | 4 µs to 80 ms, resolution of approximately 4 µs | 1 µs to 65 ms, resolution of 1 µs | 1 µs to 10s, resolution of 1 µs | 4 µs to 80 ms, resolution of approximately 4 µs |
| Seconds After I/O | 0 µs to 80 ms, resolution of 1 µs | 0 µs to 80 ms, resolution of 1 µs | 1 µs to 65 ms, resolution of 1 µs | 0 µs to 10s, resolution of 1 µs | 0 µs to 80 ms, resolution of 1 µs |
| PPM | 1.0, 0.1, 0.01 | 1.0, 0.1, 0.01, 0.001 | 1.0, 0.1, 0.01 | 1.0 to 0.01 | 1.0 to 0.01 |

| Name (value) | Description |
| --- | --- |
| - | Note This attribute is not supported if you are using an external LO. |

You do not need to use a selector string if you want to configure this attribute for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax.

The default value is 0.1.

**Supported devices**: PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5668, PXIe-5830/5831/5832/5840/5841/5842

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxinstr-c-api-ref path=group____root__ni_r_fmx_instr__attributes__advanced_1gafcb0f28fc8cb6268f8efea17ce1aa37e.html language=enus -->
## TOPIC 00010: RFMXINSTR_ATTR_AMPLITUDE_SETTLING

- bundle_id: `rfmxinstr-c-api-ref`
- source_path: `group____root__ni_r_fmx_instr__attributes__advanced_1gafcb0f28fc8cb6268f8efea17ce1aa37e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_instr__attributes__advanced_1gafcb0f28fc8cb6268f8efea17ce1aa37e.html
- document_id: `rfmxinstr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the amplitude settling accuracy value. This value is expressed in decibels. RFmx waits until the RF power attains the specified accuracy level after calling the RFmx Initiate function. SyntaxRFMXINSTR_ATTR_AMPLITUDE_SETTLINGNumeric ValueData TypeAccessApplies To56float64Read/WriteN/ARemark

### RFMXINSTR_ATTR_AMPLITUDE_SETTLING

Specifies the amplitude settling accuracy value. This value is expressed in decibels. RFmx waits until the RF power attains the specified accuracy level after calling the RFmx Initiate function.

#### Syntax

RFMXINSTR_ATTR_AMPLITUDE_SETTLING

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 56 | float64 | Read/Write | N/A |

#### Remarks

Any specified amplitude settling value that is above the acceptable minimum value is coerced down to the closest valid value.

You do not need to use a selector string if you want to configure this attribute for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax.

**Supported Devices:** PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxinstr-c-api-ref path=group____root__ni_r_fmx_instr__attributes__advanced__self__calibration.html language=enus -->
## TOPIC 00011: Self Calibration

- bundle_id: `rfmxinstr-c-api-ref`
- source_path: `group____root__ni_r_fmx_instr__attributes__advanced__self__calibration.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_instr__attributes__advanced__self__calibration.html
- document_id: `rfmxinstr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXINSTR_ATTR_SELF_CALIBRATION_VALIDITY_CHECKSpecifies whether the RFmx driver validates the self-calibration data. RFMXINSTR_ATTR_SELF_CALIBRATION_VALIDITY_CHECK_TIME_INTERVALSpecifies the minimum time between two self calibration validity checks. This value i

### Self Calibration

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXINSTR_ATTR_SELF_CALIBRATION_VALIDITY_CHECK | Specifies whether the RFmx driver validates the self-calibration data. |
| RFMXINSTR_ATTR_SELF_CALIBRATION_VALIDITY_CHECK_TIME_INTERVAL | Specifies the minimum time between two self calibration validity checks. This value is expressed in seconds. |

#### Attachments

None

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxinstr-c-api-ref path=group____root__ni_r_fmx_instr__attributes__advanced__self__calibration_1gae8381a4c96015451c877d27cd9687327.html language=enus -->
## TOPIC 00012: RFMXINSTR_ATTR_SELF_CALIBRATION_VALIDITY_CHECK

- bundle_id: `rfmxinstr-c-api-ref`
- source_path: `group____root__ni_r_fmx_instr__attributes__advanced__self__calibration_1gae8381a4c96015451c877d27cd9687327.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_instr__attributes__advanced__self__calibration_1gae8381a4c96015451c877d27cd9687327.html
- document_id: `rfmxinstr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the RFmx driver validates the self-calibration data. SyntaxRFMXINSTR_ATTR_SELF_CALIBRATION_VALIDITY_CHECKNumeric ValueData TypeAccessApplies To117int32Read/WriteN/ARemarks You can specify the time interval required to perform the check using the RFMXINSTR_ATTR_SELF_CALIBRATION_VALI

### RFMXINSTR_ATTR_SELF_CALIBRATION_VALIDITY_CHECK

Specifies whether the RFmx driver validates the self-calibration data.

#### Syntax

RFMXINSTR_ATTR_SELF_CALIBRATION_VALIDITY_CHECK

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 117 | int32 | Read/Write | N/A |

#### Remarks

You can specify the time interval required to perform the check using the [RFMXINSTR_ATTR_SELF_CALIBRATION_VALIDITY_CHECK_TIME_INTERVAL](group____root__ni_r_fmx_instr__attributes__advanced__self__calibration_1gaae86ea0b2bb0dcee34d41a450ec7872a.html) attribute.

RFmxInstr_SelfCalibrate

Note

The RFmx driver does not consider self-calibration range data during self calibration validity check.

The default value is **Off**.

**Supported devices**: PXIe-5663/5663E/5665/5668, PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5833/5840/5841/5842/5860

| Name | Value | Description |
| --- | --- | --- |
| RFMXINSTR_VAL_SELF_CALIBRATION_VALIDITY_CHECK_OFF | 0 (0x0) | Indicates that RFmx does not check whether device self-calibration data is valid. |
| RFMXINSTR_VAL_SELF_CALIBRATION_VALIDITY_CHECK_ENABLED | 1 (0x1) | Indicates that RFmx checks whether device self-calibration data is valid and reports a warning from the RFmx Commit and RFmx Initiate functions when the data is invalid. |

Parent topic:

Self Calibration

<!--NI_TOPIC bundle=rfmxinstr-c-api-ref path=group____root__ni_r_fmx_instr__attributes__device__information.html language=enus -->
## TOPIC 00013: Device Information

- bundle_id: `rfmxinstr-c-api-ref`
- source_path: `group____root__ni_r_fmx_instr__attributes__device__information.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_instr__attributes__device__information.html
- document_id: `rfmxinstr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXINSTR_ATTR_DEVICE_TEMPERATUREReturns the current temperature of the module. This value is expressed in degrees Celsius. RFMXINSTR_ATTR_DIGITIZER_TEMPERATUREReturns the current temperature of the digitizer module. This value is expressed in degrees Celsius. R

### Device Information

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXINSTR_ATTR_DEVICE_TEMPERATURE | Returns the current temperature of the module. This value is expressed in degrees Celsius. |
| RFMXINSTR_ATTR_DIGITIZER_TEMPERATURE | Returns the current temperature of the digitizer module. This value is expressed in degrees Celsius. |
| RFMXINSTR_ATTR_INSTRUMENT_FIRMWARE_REVISION | Returns a string containing the firmware revision information of the RF downconverter for the composite device you are currently using. |
| RFMXINSTR_ATTR_INSTRUMENT_MODEL | Returns a string that contains the model number or name of the RF device that you are currently using. |
| RFMXINSTR_ATTR_LO_TEMPERATURE | Returns the current temperature of the LO module associated with the device. This value is expressed in degrees Celsius. |
| RFMXINSTR_ATTR_MODULE_REVISION | Returns the revision of the RF downconverter module. |
| RFMXINSTR_ATTR_PRESELECTOR_PRESENT | Indicates whether a preselector is available on the RF downconverter module. |
| RFMXINSTR_ATTR_RF_PREAMP_PRESENT | Indicates whether an RF preamplifier is available on the RF downconverter module. |
| RFMXINSTR_ATTR_SERIAL_NUMBER | Returns the serial number of the RF downconverter module. |

#### Attachments

None

Parent topic:

Attributes

<!--NI_TOPIC bundle=rfmxinstr-c-api-ref path=group____root__ni_r_fmx_instr__attributes__device__information_1ga49f6cd0199eaa444f056ddd529f40578.html language=enus -->
## TOPIC 00014: RFMXINSTR_ATTR_MODULE_REVISION

- bundle_id: `rfmxinstr-c-api-ref`
- source_path: `group____root__ni_r_fmx_instr__attributes__device__information_1ga49f6cd0199eaa444f056ddd529f40578.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_instr__attributes__device__information_1ga49f6cd0199eaa444f056ddd529f40578.html
- document_id: `rfmxinstr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the revision of the RF downconverter module. SyntaxRFMXINSTR_ATTR_MODULE_REVISIONNumeric ValueData TypeAccessApplies To29char[]Read-OnlyPortRemarks On a MIMO session, use "port::<deviceName>/<channelNumber>" as the Selector String to read this attribute. You can use the RFmxInstr Build Port

### RFMXINSTR_ATTR_MODULE_REVISION

Returns the revision of the RF downconverter module.

#### Syntax

RFMXINSTR_ATTR_MODULE_REVISION

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 29 | char[] | Read-Only | Port |

#### Remarks

Selector String

RFmxInstr Build Port String

Note

For PXIe-5644/5645/5646 and PXIe-5820/5830/5831/5832/5840/5841/5842/5860, this attribute returns the revision of the VST module.

**Supported devices**: PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

Parent topic:

Device Information

<!--NI_TOPIC bundle=rfmxinstr-c-api-ref path=group____root__ni_r_fmx_instr__attributes__device__information_1gadd3d805ad73e676cad19a70a8bf5485e.html language=enus -->
## TOPIC 00015: RFMXINSTR_ATTR_RF_PREAMP_PRESENT

- bundle_id: `rfmxinstr-c-api-ref`
- source_path: `group____root__ni_r_fmx_instr__attributes__device__information_1gadd3d805ad73e676cad19a70a8bf5485e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_instr__attributes__device__information_1gadd3d805ad73e676cad19a70a8bf5485e.html
- document_id: `rfmxinstr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates whether an RF preamplifier is available on the RF downconverter module. SyntaxRFMXINSTR_ATTR_RF_PREAMP_PRESENTNumeric ValueData TypeAccessApplies To32int32Read-OnlyPortRemarksName (value)DescriptionTRUEA preamplifier is available on the downconverter.FALSENo preamplifier is available on th

### RFMXINSTR_ATTR_RF_PREAMP_PRESENT

Indicates whether an RF preamplifier is available on the RF downconverter module.

#### Syntax

RFMXINSTR_ATTR_RF_PREAMP_PRESENT

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 32 | int32 | Read-Only | Port |

#### Remarks

| Name (value) | Description |
| --- | --- |
| TRUE | A preamplifier is available on the downconverter. |
| FALSE | No preamplifier is available on the downconverter. |

On a MIMO session, use "port::<deviceName>/<channelNumber>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this attribute. You can use the [RFmxInstr Build Port String](/csh?context=rfmxinstr_rfmxinstrcref_function_build_port_string_2) function to build the selector string.

**Supported devices**: PXIe-5663/5663E/5665/5668, PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842

Parent topic:

Device Information

<!--NI_TOPIC bundle=rfmxinstr-c-api-ref path=group____root__ni_r_fmx_instr__attributes__device__information_1gaeeeb67ffc73f7dc95fb5756118e40663.html language=enus -->
## TOPIC 00016: RFMXINSTR_ATTR_LO_TEMPERATURE

- bundle_id: `rfmxinstr-c-api-ref`
- source_path: `group____root__ni_r_fmx_instr__attributes__device__information_1gaeeeb67ffc73f7dc95fb5756118e40663.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_instr__attributes__device__information_1gaeeeb67ffc73f7dc95fb5756118e40663.html
- document_id: `rfmxinstr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the current temperature of the LO module associated with the device. This value is expressed in degrees Celsius. SyntaxRFMXINSTR_ATTR_LO_TEMPERATURENumeric ValueData TypeAccessApplies To26float64Read-OnlyPortRemarks On a MIMO session, use "port::<deviceName>/<channelNumber>" as the Selector

### RFMXINSTR_ATTR_LO_TEMPERATURE

Returns the current temperature of the LO module associated with the device. This value is expressed in degrees Celsius.

#### Syntax

RFMXINSTR_ATTR_LO_TEMPERATURE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 26 | float64 | Read-Only | Port |

#### Remarks

Selector String

RFmxInstr Build Port String

Note

This attribute is not supported if you are using an external LO.

**Supported devices**: PXIe-5663/5663E/5665/5668, PXIe-5840/5841/5842

Parent topic:

Device Information

<!--NI_TOPIC bundle=rfmxinstr-c-api-ref path=group____root__ni_r_fmx_instr__attributes__event__ready__for__advance.html language=enus -->
## TOPIC 00017: Ready For Advance

- bundle_id: `rfmxinstr-c-api-ref`
- source_path: `group____root__ni_r_fmx_instr__attributes__event__ready__for__advance.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_instr__attributes__event__ready__for__advance.html
- document_id: `rfmxinstr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXINSTR_ATTR_READY_FOR_ADVANCE_EVENT_OUTPUT_TERMINALSpecifies the destination terminal for the Ready for Advance event. RFMXINSTR_ATTR_READY_FOR_ADVANCE_EVENT_TERMINAL_NAMEReturns the fully qualified signal name as a string. AttachmentsNone

### Ready For Advance

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXINSTR_ATTR_READY_FOR_ADVANCE_EVENT_OUTPUT_TERMINAL | Specifies the destination terminal for the Ready for Advance event. |
| RFMXINSTR_ATTR_READY_FOR_ADVANCE_EVENT_TERMINAL_NAME | Returns the fully qualified signal name as a string. |

#### Attachments

None

Parent topic:

Event

<!--NI_TOPIC bundle=rfmxinstr-c-api-ref path=group____root__ni_r_fmx_instr__attributes__event__ready__for__advance_1ga52220cedd9d4699bb154a56a66e28c41.html language=enus -->
## TOPIC 00018: RFMXINSTR_ATTR_READY_FOR_ADVANCE_EVENT_OUTPUT_TERMINAL

- bundle_id: `rfmxinstr-c-api-ref`
- source_path: `group____root__ni_r_fmx_instr__attributes__event__ready__for__advance_1ga52220cedd9d4699bb154a56a66e28c41.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_instr__attributes__event__ready__for__advance_1ga52220cedd9d4699bb154a56a66e28c41.html
- document_id: `rfmxinstr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the destination terminal for the Ready for Advance event. SyntaxRFMXINSTR_ATTR_READY_FOR_ADVANCE_EVENT_OUTPUT_TERMINALNumeric ValueData TypeAccessApplies To109char[]Read/WriteN/ARemarksThis attribute is not supported on a MIMO session.You do not need to use a selector string if you want to

### RFMXINSTR_ATTR_READY_FOR_ADVANCE_EVENT_OUTPUT_TERMINAL

Specifies the destination terminal for the Ready for Advance event.

#### Syntax

RFMXINSTR_ATTR_READY_FOR_ADVANCE_EVENT_OUTPUT_TERMINAL

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 109 | char[] | Read/Write | N/A |

#### Remarks

Note

This attribute is not supported on a MIMO session.

You do not need to use a selector string if you want to configure this attribute for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax.

The default value is **Do not export signal**.

**Supported devices**: PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

| Name | Value | Description |
| --- | --- | --- |
| RFMXINSTR_VAL_NONE_STR |  | Does not export the signal. |
| RFMXINSTR_VAL_CLK_OUT_STR | ClkOut | Exports the signal to the CLK OUT connector on the PXIe-5622/5624 front panel. |
| RFMXINSTR_VAL_REF_OUT_STR | RefOut | Exports the signal to the REF IN/OUT terminal on the PXIe-5652, and the REF OUT terminal on the PXIe-5644/5645/5646 and PXIe-5820/5830/5831/5832/5840/5841/5842/5860. |
| RFMXINSTR_VAL_REF_OUT2_STR | RefOut2 | Exports the signal to the REF OUT2 terminal on the LO. This connector exists only on PXIe-5652. |
| RFMXINSTR_VAL_PFI0_STR | PFI0 | Exports the signal to the PFI 0 connector. For the PXIe-5841 with PXIe-5655, the signal is exported to the PXIe-5841 PFI 0. |
| RFMXINSTR_VAL_PFI1_STR | PFI1 | Exports the signal to the PFI 1 connector on PXIe-5142 and PXIe-5622. |
| RFMXINSTR_VAL_PXI_TRIG0_STR | PXI_Trig0 | Exports the signal to the PXI trigger line 0. |
| RFMXINSTR_VAL_PXI_TRIG1_STR | PXI_Trig1 | Exports the signal to the PXI trigger line 1. |
| RFMXINSTR_VAL_PXI_TRIG2_STR | PXI_Trig2 | Exports the signal to the PXI trigger line 2. |
| RFMXINSTR_VAL_PXI_TRIG3_STR | PXI_Trig3 | Exports the signal to the PXI trigger line 3. |
| RFMXINSTR_VAL_PXI_TRIG4_STR | PXI_Trig4 | Exports the signal to the PXI trigger line 4. |
| RFMXINSTR_VAL_PXI_TRIG5_STR | PXI_Trig5 | Exports the signal to the PXI trigger line 5. |
| RFMXINSTR_VAL_PXI_TRIG6_STR | PXI_Trig6 | Exports the signal to the PXI trigger line 6. |
| RFMXINSTR_VAL_PXI_TRIG7_STR | PXI_Trig7 | Exports the signal to the PXI trigger line 7. |
| RFMXINSTR_VAL_PXI_STAR_STR | PXI_STAR | Exports the signal to the PXI star trigger line. This value is not valid for PXIe-5644/5645/5646. |
| RFMXINSTR_VAL_PXIE_DSTARC_STR | PXIe_DStarC | Exports the signal to the PXIe DStar C trigger line. This value is valid only for PXIe-5820/5830/5831/5832/5840/5841/5842/5860. |
| RFMXINSTR_VAL_DIO_PFI0_STR | DIO/PFI0 | Exports the signal to the PFI 0 on the DIO front panel connector. |
| RFMXINSTR_VAL_DIO_PFI1_STR | DIO/PFI1 | Exports the signal to the PFI 1 on the DIO front panel connector. |
| RFMXINSTR_VAL_DIO_PFI2_STR | DIO/PFI2 | Exports the signal to the PFI 2 on the DIO front panel connector. |
| RFMXINSTR_VAL_DIO_PFI3_STR | DIO/PFI3 | Exports the signal to the PFI 3 on the DIO front panel connector. |
| RFMXINSTR_VAL_DIO_PFI4_STR | DIO/PFI4 | Exports the signal to the PFI 4 on the DIO front panel connector. |
| RFMXINSTR_VAL_DIO_PFI5_STR | DIO/PFI5 | Exports the signal to the PFI 5 on the DIO front panel connector. |
| RFMXINSTR_VAL_DIO_PFI6_STR | DIO/PFI6 | Exports the signal to the PFI 6 on the DIO front panel connector. |
| RFMXINSTR_VAL_DIO_PFI7_STR | DIO/PFI7 | Exports the signal to the PFI 7 on the DIO front panel connector. |

Parent topic:

Ready For Advance

<!--NI_TOPIC bundle=rfmxinstr-c-api-ref path=group____root__ni_r_fmx_instr__attributes__event__ready__for__advance_1ga6ab4495090e73064bcdfbbb066303ae2.html language=enus -->
## TOPIC 00019: RFMXINSTR_ATTR_READY_FOR_ADVANCE_EVENT_TERMINAL_NAME

- bundle_id: `rfmxinstr-c-api-ref`
- source_path: `group____root__ni_r_fmx_instr__attributes__event__ready__for__advance_1ga6ab4495090e73064bcdfbbb066303ae2.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_instr__attributes__event__ready__for__advance_1ga6ab4495090e73064bcdfbbb066303ae2.html
- document_id: `rfmxinstr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the fully qualified signal name as a string. SyntaxRFMXINSTR_ATTR_READY_FOR_ADVANCE_EVENT_TERMINAL_NAMENumeric ValueData TypeAccessApplies To110char[]Read-OnlyN/ARemarks The standard format is as follows: PXIe-5820/5840/5841/5842: /ModuleName/ai/0/ReadyForAdvanceEvent, where ModuleName is th

### RFMXINSTR_ATTR_READY_FOR_ADVANCE_EVENT_TERMINAL_NAME

Returns the fully qualified signal name as a string.

#### Syntax

RFMXINSTR_ATTR_READY_FOR_ADVANCE_EVENT_TERMINAL_NAME

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 110 | char[] | Read-Only | N/A |

#### Remarks

- **PXIe-5820/5840/5841/5842**: */ModuleName/ai/0/ReadyForAdvanceEvent*, where *ModuleName* is the name of your device in MAX.
- **PXIe-5830/5831/5832**: */BasebandModule/ai/0/ReadyForAdvanceEvent*, where *BasebandModule* is the name of your device in MAX.
- **PXIe-5860**: */ModuleName/ai/ChannelNumber/ReadyForAdvanceEvent*, where *ModuleName* is the name of your device in MAX and ChannelNumber is the channel number (0 or 1)
- **All other devices**: */DigitizerName/ReadyForAdvanceEvent*, where *DigitizerName* is the name of your associated digitizer module in MAX.

Note

This attribute is not supported on a MIMO session.

**Supported devices**: PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

Parent topic:

Ready For Advance

<!--NI_TOPIC bundle=rfmxinstr-c-api-ref path=group____root__ni_r_fmx_instr__attributes__event__ready__for__reference.html language=enus -->
## TOPIC 00020: Ready For Reference

- bundle_id: `rfmxinstr-c-api-ref`
- source_path: `group____root__ni_r_fmx_instr__attributes__event__ready__for__reference.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_instr__attributes__event__ready__for__reference.html
- document_id: `rfmxinstr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXINSTR_ATTR_READY_FOR_REFERENCE_EVENT_OUTPUT_TERMINALSpecifies the destination terminal for the Ready for Reference event. RFMXINSTR_ATTR_READY_FOR_REFERENCE_EVENT_TERMINAL_NAMEReturns the fully qualified signal name as a string. AttachmentsNone

### Ready For Reference

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXINSTR_ATTR_READY_FOR_REFERENCE_EVENT_OUTPUT_TERMINAL | Specifies the destination terminal for the Ready for Reference event. |
| RFMXINSTR_ATTR_READY_FOR_REFERENCE_EVENT_TERMINAL_NAME | Returns the fully qualified signal name as a string. |

#### Attachments

None

Parent topic:

Event

<!--NI_TOPIC bundle=rfmxinstr-c-api-ref path=group____root__ni_r_fmx_instr__attributes__event__ready__for__reference_1ga04ee8f6dd8a90ca826d938c2d96dcb69.html language=enus -->
## TOPIC 00021: RFMXINSTR_ATTR_READY_FOR_REFERENCE_EVENT_TERMINAL_NAME

- bundle_id: `rfmxinstr-c-api-ref`
- source_path: `group____root__ni_r_fmx_instr__attributes__event__ready__for__reference_1ga04ee8f6dd8a90ca826d938c2d96dcb69.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_instr__attributes__event__ready__for__reference_1ga04ee8f6dd8a90ca826d938c2d96dcb69.html
- document_id: `rfmxinstr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the fully qualified signal name as a string. SyntaxRFMXINSTR_ATTR_READY_FOR_REFERENCE_EVENT_TERMINAL_NAMENumeric ValueData TypeAccessApplies To112char[]Read-OnlyN/ARemarks The standard format is as follows: PXIe-5820/5840/5841/5842: /ModuleName/ai/0/ReadyForReferenceEvent, where ModuleName i

### RFMXINSTR_ATTR_READY_FOR_REFERENCE_EVENT_TERMINAL_NAME

Returns the fully qualified signal name as a string.

#### Syntax

RFMXINSTR_ATTR_READY_FOR_REFERENCE_EVENT_TERMINAL_NAME

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 112 | char[] | Read-Only | N/A |

#### Remarks

- **PXIe-5820/5840/5841/5842**: */ModuleName/ai/0/ReadyForReferenceEvent*, where *ModuleName* is the name of your device in MAX.
- **PXIe-5830/5831/5832**: */BasebandModule/ai/0/ReadyForReferenceEvent*, where *BasebandModule* is the name of your device in MAX.
- **PXIe-5860**: */ModuleName/ai/ChannelNumber/ReadyForReferenceEvent*, where *BasebandModule*is the name of your device in MAX and ChannelNumber is the channel number (0 or 1).
- **All other devices**: */DigitizerName/ReadyForReferenceEvent*, where *DigitizerName* is the name of your associated digitizer module in MAX.

Note

This attribute is not supported on a MIMO session.

**Supported devices**: PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

Parent topic:

Ready For Reference

<!--NI_TOPIC bundle=rfmxinstr-c-api-ref path=group____root__ni_r_fmx_instr__attributes__event__ready__for__reference_1gad896d106ca25099cc36bdb18fc44179f.html language=enus -->
## TOPIC 00022: RFMXINSTR_ATTR_READY_FOR_REFERENCE_EVENT_OUTPUT_TERMINAL

- bundle_id: `rfmxinstr-c-api-ref`
- source_path: `group____root__ni_r_fmx_instr__attributes__event__ready__for__reference_1gad896d106ca25099cc36bdb18fc44179f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_instr__attributes__event__ready__for__reference_1gad896d106ca25099cc36bdb18fc44179f.html
- document_id: `rfmxinstr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the destination terminal for the Ready for Reference event. SyntaxRFMXINSTR_ATTR_READY_FOR_REFERENCE_EVENT_OUTPUT_TERMINALNumeric ValueData TypeAccessApplies To111char[]Read/WriteN/ARemarksThis attribute is not supported on a MIMO session.You do not need to use a selector string if you wan

### RFMXINSTR_ATTR_READY_FOR_REFERENCE_EVENT_OUTPUT_TERMINAL

Specifies the destination terminal for the Ready for Reference event.

#### Syntax

RFMXINSTR_ATTR_READY_FOR_REFERENCE_EVENT_OUTPUT_TERMINAL

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 111 | char[] | Read/Write | N/A |

#### Remarks

Note

This attribute is not supported on a MIMO session.

You do not need to use a selector string if you want to configure this attribute for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax.

The default value is **Do not export signal**.

**Supported devices**: PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

| Name | Value | Description |
| --- | --- | --- |
| RFMXINSTR_VAL_NONE_STR |  | Does not export the signal. |
| RFMXINSTR_VAL_CLK_OUT_STR | ClkOut | Exports the signal to the CLK OUT connector on the PXIe-5622/5624 front panel. |
| RFMXINSTR_VAL_REF_OUT_STR | RefOut | Exports the signal to the REF IN/OUT terminal on the PXIe-5652, and the REF OUT terminal on the PXIe-5644/5645/5646 and PXIe-5820/5830/5831/5832/5840/5841/5842/5860. |
| RFMXINSTR_VAL_REF_OUT2_STR | RefOut2 | Exports the signal to the REF OUT2 terminal on the LO. This connector exists only on PXIe-5652. |
| RFMXINSTR_VAL_PFI0_STR | PFI0 | Exports the signal to the PFI 0 connector. For the PXIe-5841 with PXIe-5655, the signal is exported to the PXIe-5841 PFI 0. |
| RFMXINSTR_VAL_PFI1_STR | PFI1 | Exports the signal to the PFI 1 connector on PXIe-5142 and PXIe-5622. |
| RFMXINSTR_VAL_PXI_TRIG0_STR | PXI_Trig0 | Exports the signal to the PXI trigger line 0. |
| RFMXINSTR_VAL_PXI_TRIG1_STR | PXI_Trig1 | Exports the signal to the PXI trigger line 1. |
| RFMXINSTR_VAL_PXI_TRIG2_STR | PXI_Trig2 | Exports the signal to the PXI trigger line 2. |
| RFMXINSTR_VAL_PXI_TRIG3_STR | PXI_Trig3 | Exports the signal to the PXI trigger line 3. |
| RFMXINSTR_VAL_PXI_TRIG4_STR | PXI_Trig4 | Exports the signal to the PXI trigger line 4. |
| RFMXINSTR_VAL_PXI_TRIG5_STR | PXI_Trig5 | Exports the signal to the PXI trigger line 5. |
| RFMXINSTR_VAL_PXI_TRIG6_STR | PXI_Trig6 | Exports the signal to the PXI trigger line 6. |
| RFMXINSTR_VAL_PXI_TRIG7_STR | PXI_Trig7 | Exports the signal to the PXI trigger line 7. |
| RFMXINSTR_VAL_PXI_STAR_STR | PXI_STAR | Exports the signal to the PXI star trigger line. This value is not valid for PXIe-5644/5645/5646. |
| RFMXINSTR_VAL_PXIE_DSTARC_STR | PXIe_DStarC | Exports the signal to the PXIe DStar C trigger line. This value is valid only for PXIe-5820/5830/5831/5832/5840/5841/5842/5860. |
| RFMXINSTR_VAL_DIO_PFI0_STR | DIO/PFI0 | Exports the signal to the PFI 0 on the DIO front panel connector. |
| RFMXINSTR_VAL_DIO_PFI1_STR | DIO/PFI1 | Exports the signal to the PFI 1 on the DIO front panel connector. |
| RFMXINSTR_VAL_DIO_PFI2_STR | DIO/PFI2 | Exports the signal to the PFI 2 on the DIO front panel connector. |
| RFMXINSTR_VAL_DIO_PFI3_STR | DIO/PFI3 | Exports the signal to the PFI 3 on the DIO front panel connector. |
| RFMXINSTR_VAL_DIO_PFI4_STR | DIO/PFI4 | Exports the signal to the PFI 4 on the DIO front panel connector. |
| RFMXINSTR_VAL_DIO_PFI5_STR | DIO/PFI5 | Exports the signal to the PFI 5 on the DIO front panel connector. |
| RFMXINSTR_VAL_DIO_PFI6_STR | DIO/PFI6 | Exports the signal to the PFI 6 on the DIO front panel connector. |
| RFMXINSTR_VAL_DIO_PFI7_STR | DIO/PFI7 | Exports the signal to the PFI 7 on the DIO front panel connector. |

Parent topic:

Ready For Reference

<!--NI_TOPIC bundle=rfmxinstr-c-api-ref path=group____root__ni_r_fmx_instr__attributes__frequency__reference_1gaea274433cbeb49ff24b3dde5515d2656.html language=enus -->
## TOPIC 00023: RFMXINSTR_ATTR_FREQUENCY_REFERENCE_EXPORTED_TERMINAL

- bundle_id: `rfmxinstr-c-api-ref`
- source_path: `group____root__ni_r_fmx_instr__attributes__frequency__reference_1gaea274433cbeb49ff24b3dde5515d2656.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_instr__attributes__frequency__reference_1gaea274433cbeb49ff24b3dde5515d2656.html
- document_id: `rfmxinstr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies a comma-separated list of the terminals at which to export the frequency reference. SyntaxRFMXINSTR_ATTR_FREQUENCY_REFERENCE_EXPORTED_TERMINALNumeric ValueData TypeAccessApplies To34char[]Read/WriteN/ARemarksThis attribute is not supported on a MIMO session.You do not need to use a selecto

### RFMXINSTR_ATTR_FREQUENCY_REFERENCE_EXPORTED_TERMINAL

Specifies a comma-separated list of the terminals at which to export the frequency reference.

#### Syntax

RFMXINSTR_ATTR_FREQUENCY_REFERENCE_EXPORTED_TERMINAL

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 34 | char[] | Read/Write | N/A |

#### Remarks

Note

This attribute is not supported on a MIMO session.

You do not need to use a selector string if you want to configure this attribute for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax.

The default value is **None**.

**Supported devices**: PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

| Name | Value | Description |
| --- | --- | --- |
| RFMXINSTR_VAL_NONE_STR |  | The Reference Clock is not exported. This value is not valid for the PXIe-5644/5645/5646. |
| RFMXINSTR_VAL_REF_OUT_STR | RefOut | Export the clock on the REF IN/OUT terminal on the PXIe-5652, the REF OUT terminals on the PXIe-5653, or the REF OUT terminal on the PXIe-5694, PXIe-5644/5645/5646, or PXIe-5820/5830/5831/5832/5840/5841/5860. |
| RFMXINSTR_VAL_REF_OUT2_STR | RefOut2 | Export the clock on the REF OUT2 terminal on the PXIe-5652. This value is valid only for the PXIe-5663E. |
| RFMXINSTR_VAL_CLK_OUT_STR | ClkOut | Export the Reference Clock on the CLK OUT terminal on the Digitizer. This value is not valid for the PXIe-5644/5645/5646 or PXIe-5820/5830/5831/5832/5840/5841/5842/5860. |

Parent topic:

Frequency Reference

<!--NI_TOPIC bundle=rfmxinstr-c-api-ref path=group____root__ni_r_fmx_instr__attributes__lo.html language=enus -->
## TOPIC 00024: LO

- bundle_id: `rfmxinstr-c-api-ref`
- source_path: `group____root__ni_r_fmx_instr__attributes__lo.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_instr__attributes__lo.html
- document_id: `rfmxinstr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXINSTR_ATTR_DOWNCONVERTER_CENTER_FREQUENCYEnables in-band retuning and specifies the current frequency of the RF downconverter. This value is expressed in Hz. RFMXINSTR_ATTR_DOWNCONVERTER_FREQUENCY_OFFSETSpecifies an offset from the center frequency value for

### LO

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXINSTR_ATTR_DOWNCONVERTER_CENTER_FREQUENCY | Enables in-band retuning and specifies the current frequency of the RF downconverter. This value is expressed in Hz. |
| RFMXINSTR_ATTR_DOWNCONVERTER_FREQUENCY_OFFSET | Specifies an offset from the center frequency value for the downconverter. Use this attribute to offset the measurement away from the LO leakage or DC Offset of analyzers that use a direct conversion architecture. You must set this attribute to half the bandwidth or span of the measurement + guardband. The guardband is needed to ensure that the LO leakage is not inside the analog or digital filter rolloffs. This value is expressed in Hz. |
| RFMXINSTR_ATTR_LO2_EXPORT_ENABLED | Specifies whether to enable the LO2 OUT terminals in the installed devices. |
| RFMXINSTR_ATTR_LO_EXPORT_ENABLED | Specifies whether to enable the LO OUT terminals on the installed devices. |
| RFMXINSTR_ATTR_LO_FREQUENCY | Specifies the LO signal frequency for the configured center frequency. This value is expressed in Hz. |
| RFMXINSTR_ATTR_LO_FREQUENCY_STEP_SIZE | Specifies the step size for tuning the LO phase-locked loop (PLL). |
| RFMXINSTR_ATTR_LO_INJECTION_SIDE | Specifies the LO injection side. |
| RFMXINSTR_ATTR_LO_IN_POWER | Specifies the power level expected at the LO IN terminal when the RFMXINSTR_ATTR_LO_SOURCE attribute is set to LO_In. This value is expressed in dBm. |
| RFMXINSTR_ATTR_LO_LEAKAGE_AVOIDANCE_ENABLED | Specifies whether to reduce the effects of the instrument leakage by placing the LO outside the band of acquisition. |
| RFMXINSTR_ATTR_LO_OUT_POWER | Specifies the power level of the signal at the LO OUT terminal when the RFMXINSTR_ATTR_LO_EXPORT_ENABLED attribute is set to TRUE. This value is expressed in dBm. |
| RFMXINSTR_ATTR_LO_PLL_FRACTIONAL_MODE | Specifies whether to use fractional mode for the LO phase-locked loop (PLL). |
| RFMXINSTR_ATTR_LO_SOURCE | Specifies the local oscillator (LO) signal source used to downconvert the RF input signal. |
| RFMXINSTR_ATTR_LO_VCO_FREQUENCY_STEP_SIZE | Specifies the step size for tuning the internal voltage-controlled oscillator (VCO) used to generate the LO signal. The valid values for LO1 include 1 Hz to 50 MHz and for LO2 include 1 Hz to 100 MHz. |
| RFMXINSTR_ATTR_TUNING_SPEED | Makes tradeoffs between tuning speed and phase noise. |

#### Attachments

None

Parent topic:

Attributes

<!--NI_TOPIC bundle=rfmxinstr-c-api-ref path=group____root__ni_r_fmx_instr__attributes__lo_1ga5845b2a8558f1736170eed2f223e0959.html language=enus -->
## TOPIC 00025: RFMXINSTR_ATTR_LO_PLL_FRACTIONAL_MODE

- bundle_id: `rfmxinstr-c-api-ref`
- source_path: `group____root__ni_r_fmx_instr__attributes__lo_1ga5845b2a8558f1736170eed2f223e0959.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_instr__attributes__lo_1ga5845b2a8558f1736170eed2f223e0959.html
- document_id: `rfmxinstr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to use fractional mode for the LO phase-locked loop (PLL). SyntaxRFMXINSTR_ATTR_LO_PLL_FRACTIONAL_MODENumeric ValueData TypeAccessApplies To90int32Read/WriteLoRemarks Fractional mode provides a finer frequency step resolution, but may result in non harmonic spurs. Refer to the spec

### RFMXINSTR_ATTR_LO_PLL_FRACTIONAL_MODE

Specifies whether to use fractional mode for the LO phase-locked loop (PLL).

#### Syntax

RFMXINSTR_ATTR_LO_PLL_FRACTIONAL_MODE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 90 | int32 | Read/Write | Lo |

#### Remarks

Fractional mode provides a finer frequency step resolution, but may result in non harmonic spurs. Refer to the specifications document of your device for more information about fractional mode and non harmonic spurs.

RFmxInstr_BuildLOString

Note

This attribute is not supported on a MIMO session.

Selector String

Note

The LO PLL Fractional Mode attribute is applicable only when using the internal LO.

Note

For PXIe-5831 with PXIe-5653, PXIe-5832 with PXIe-5653, this attribute is ignored if the PXIe-5653 is used as the LO source.

The default value is **Enabled**.

**Supported devices**: PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842

| Name | Value | Description |
| --- | --- | --- |
| RFMXINSTR_VAL_LO_PLL_FRACTIONAL_MODE_DISABLED | 0 (0x0) | Indicates that the attribute is disabled. |
| RFMXINSTR_VAL_LO_PLL_FRACTIONAL_MODE_ENABLED | 1 (0x1) | Indicates that the attribute is enabled. |

Parent topic:

LO

<!--NI_TOPIC bundle=rfmxinstr-c-api-ref path=group____root__ni_r_fmx_instr__attributes__lo_1ga6b2d2e20bb4132c2cc72ea968a17de13.html language=enus -->
## TOPIC 00026: RFMXINSTR_ATTR_LO_VCO_FREQUENCY_STEP_SIZE

- bundle_id: `rfmxinstr-c-api-ref`
- source_path: `group____root__ni_r_fmx_instr__attributes__lo_1ga6b2d2e20bb4132c2cc72ea968a17de13.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_instr__attributes__lo_1ga6b2d2e20bb4132c2cc72ea968a17de13.html
- document_id: `rfmxinstr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the step size for tuning the internal voltage-controlled oscillator (VCO) used to generate the LO signal. The valid values for LO1 include 1 Hz to 50 MHz and for LO2 include 1 Hz to 100 MHz. SyntaxRFMXINSTR_ATTR_LO_VCO_FREQUENCY_STEP_SIZENumeric ValueData TypeAccessApplies To80float64Read/

### RFMXINSTR_ATTR_LO_VCO_FREQUENCY_STEP_SIZE

Specifies the step size for tuning the internal voltage-controlled oscillator (VCO) used to generate the LO signal. The valid values for LO1 include 1 Hz to 50 MHz and for LO2 include 1 Hz to 100 MHz.

#### Syntax

RFMXINSTR_ATTR_LO_VCO_FREQUENCY_STEP_SIZE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 80 | float64 | Read/Write | N/A |

#### Remarks

Note

Do not set this attribute with the [RFMXINSTR_ATTR_LO_FREQUENCY_STEP_SIZE](group____root__ni_r_fmx_instr__attributes__lo_1ga55ac8cc764bff368e7ec37650c51d485.html) attribute.

Note

This attribute is not supported on a MIMO session.

You do not need to use a selector string if you want to configure this attribute for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax.

The default value is 1 MHz.

**Supported devices**: PXIe-5830/5831/5832

Parent topic:

LO

<!--NI_TOPIC bundle=rfmxinstr-c-api-ref path=group____root__ni_r_fmx_instr__attributes__lo_1gab27e8fed60485b1ba2d4d520eed5edf1.html language=enus -->
## TOPIC 00027: RFMXINSTR_ATTR_LO_LEAKAGE_AVOIDANCE_ENABLED

- bundle_id: `rfmxinstr-c-api-ref`
- source_path: `group____root__ni_r_fmx_instr__attributes__lo_1gab27e8fed60485b1ba2d4d520eed5edf1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_instr__attributes__lo_1gab27e8fed60485b1ba2d4d520eed5edf1.html
- document_id: `rfmxinstr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to reduce the effects of the instrument leakage by placing the LO outside the band of acquisition. SyntaxRFMXINSTR_ATTR_LO_LEAKAGE_AVOIDANCE_ENABLEDNumeric ValueData TypeAccessApplies To55int32Read/WriteN/ARemarks This attribute is ignored if: the bandwidth required by the measurem

### RFMXINSTR_ATTR_LO_LEAKAGE_AVOIDANCE_ENABLED

Specifies whether to reduce the effects of the instrument leakage by placing the LO outside the band of acquisition.

#### Syntax

RFMXINSTR_ATTR_LO_LEAKAGE_AVOIDANCE_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 55 | int32 | Read/Write | N/A |

#### Remarks

- the bandwidth required by the measurement is more than the available instrument bandwidth after offsetting the LO.
- you set the [RFMXINSTR_ATTR_DOWNCONVERTER_CENTER_FREQUENCY](group____root__ni_r_fmx_instr__attributes__lo_1ga3088d5b93368b82d226b3d97a3055aa9.html) or [RFMXINSTR_ATTR_DOWNCONVERTER_FREQUENCY_OFFSET](group____root__ni_r_fmx_instr__attributes__lo_1gac9c30b5f30f8d67e6f65ba32007197b9.html) attributes.

Note

When using a DPD applied signal for performing measurements like ModAcc, PvT, or TXP, you must set this attribute to **False** when the [RFMXINSTR_ATTR_LO_SOURCE](group____root__ni_r_fmx_instr__attributes__lo_1ga3c19249b0d47a9d489c57baef1219d9f.html) attribute is set to **Automatic_SG_SA_Shared**.

You do not need to use a selector string if you want to configure this attribute for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax.

The default value for PXIe-5830/5831/5832/5840/5841/5842 is **True**, else the default value is **False**.

**Supported devices**: PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842

| Name | Value | Description |
| --- | --- | --- |
| RFMXINSTR_VAL_LO_LEAKAGE_AVOIDANCE_ENABLED_FALSE | 0 (0x0) | RFmx does not modify the Downconverter Frequency Offset attribute. |
| RFMXINSTR_VAL_LO_LEAKAGE_AVOIDANCE_ENABLED_TRUE | 1 (0x1) | RFmx calculates the required LO offset based on the measurement configuration and appropriately sets the Downconverter Frequency Offset attribute. |

Parent topic:

LO

<!--NI_TOPIC bundle=rfmxinstr-c-api-ref path=group____root__ni_r_fmx_instr__attributes__lo_1gac9c30b5f30f8d67e6f65ba32007197b9.html language=enus -->
## TOPIC 00028: RFMXINSTR_ATTR_DOWNCONVERTER_FREQUENCY_OFFSET

- bundle_id: `rfmxinstr-c-api-ref`
- source_path: `group____root__ni_r_fmx_instr__attributes__lo_1gac9c30b5f30f8d67e6f65ba32007197b9.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_instr__attributes__lo_1gac9c30b5f30f8d67e6f65ba32007197b9.html
- document_id: `rfmxinstr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies an offset from the center frequency value for the downconverter. Use this attribute to offset the measurement away from the LO leakage or DC Offset of analyzers that use a direct conversion architecture. You must set this attribute to half the bandwidth or span of the measurement + guardba

### RFMXINSTR_ATTR_DOWNCONVERTER_FREQUENCY_OFFSET

Specifies an offset from the center frequency value for the downconverter. Use this attribute to offset the measurement away from the LO leakage or DC Offset of analyzers that use a direct conversion architecture. You must set this attribute to half the bandwidth or span of the measurement + guardband. The guardband is needed to ensure that the LO leakage is not inside the analog or digital filter rolloffs. This value is expressed in Hz.

#### Syntax

RFMXINSTR_ATTR_DOWNCONVERTER_FREQUENCY_OFFSET

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 53 | float64 | Read/Write | N/A |

#### Remarks

RFMXINSTR_ATTR_LO_LEAKAGE_AVOIDANCE_ENABLED

Note

This attribute is not supported on a MIMO session.

You do not need to use a selector string if you want to configure this attribute for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax.

**Default values:** For spectrum acquisition types, the RFmx driver automatically calculates the default value to avoid residual LO power. For I/Q acquisition types, the default value is 0 Hz. If the center frequency is set to a non-multiple of [RFMXINSTR_ATTR_LO_FREQUENCY_STEP_SIZE](group____root__ni_r_fmx_instr__attributes__lo_1ga55ac8cc764bff368e7ec37650c51d485.html) attribute, this attribute is set to compensate for the difference.

The following valid values correspond to their respective devices:

| Name (value) | Description |
| --- | --- |
| PXIe-5646 | -100 MHz to +100 MHz |
| PXIe-5830/5831/5832/5840 | -500 MHz to +500 MHz |
| PXIe-5841 (200MHz Bandwidth) | -100 MHz to +100 MHz |
| PXIe-5841 (1GHz Bandwidth) | -500 MHz to +500 MHz |
| PXIe-5842 (500MHz Bandwidth) | -250 MHz to +250 MHz |
| PXIe-5842 (1GHz Bandwidth) | -500 MHz to +500 MHz |
| PXIe-5842 (2GHz Bandwidth) | -1 GHz to +1 GHz |
| PXIe-5842 (4GHz Bandwidth) using Standard personality | -1 GHz to +1 GHz |
| PXIe-5842 (4GHz Bandwidth) using the 4GHz Bandwidth personality | -2 GHz to +2 GHz |
| Other devices | -42 MHz to +42 MHz |

**Supported Devices:** PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842

Parent topic:

LO

<!--NI_TOPIC bundle=rfmxinstr-c-api-ref path=group____root__ni_r_fmx_instr__attributes__lo_1gada989f64302c37c7c46e83b6c07db2cb.html language=enus -->
## TOPIC 00029: RFMXINSTR_ATTR_LO2_EXPORT_ENABLED

- bundle_id: `rfmxinstr-c-api-ref`
- source_path: `group____root__ni_r_fmx_instr__attributes__lo_1gada989f64302c37c7c46e83b6c07db2cb.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_instr__attributes__lo_1gada989f64302c37c7c46e83b6c07db2cb.html
- document_id: `rfmxinstr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the LO2 OUT terminals in the installed devices. SyntaxRFMXINSTR_ATTR_LO2_EXPORT_ENABLEDNumeric ValueData TypeAccessApplies To58int32Read/WriteN/ARemarks Set this attribute to Enabled to export the 4 GHz LO signal from the LO2 IN terminal to the LO2 OUT terminal. You can a

### RFMXINSTR_ATTR_LO2_EXPORT_ENABLED

Specifies whether to enable the LO2 OUT terminals in the installed devices.

#### Syntax

RFMXINSTR_ATTR_LO2_EXPORT_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 58 | int32 | Read/Write | N/A |

#### Remarks

Enabled

RFMXINSTR_ATTR_LO_EXPORT_ENABLED

Note

This attribute is not supported on a MIMO session.

You do not need to use a selector string if you want to configure this attribute for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax.

The default value is **Disabled**.

**Supported Devices:** PXIe-5665/5668

| Name | Value | Description |
| --- | --- | --- |
| RFMXINSTR_VAL_LO2_EXPORT_DISABLED | 0 (0x0) | Disables the LO2 OUT terminals. |
| RFMXINSTR_VAL_LO2_EXPORT_ENABLED | 1 (0x1) | Enables the LO2 OUT terminals. |

Parent topic:

LO

<!--NI_TOPIC bundle=rfmxinstr-c-api-ref path=group____root__ni_r_fmx_instr__attributes__mechanical__attenuation.html language=enus -->
## TOPIC 00030: Mechanical Attenuation

- bundle_id: `rfmxinstr-c-api-ref`
- source_path: `group____root__ni_r_fmx_instr__attributes__mechanical__attenuation.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_instr__attributes__mechanical__attenuation.html
- document_id: `rfmxinstr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXINSTR_ATTR_MECHANICAL_ATTENUATION_AUTOSpecifies whether the RFmx driver chooses an attenuation setting based on the hardware settings. RFMXINSTR_ATTR_MECHANICAL_ATTENUATION_VALUESpecifies the level of mechanical attenuation for the RF path. This value is exp

### Mechanical Attenuation

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXINSTR_ATTR_MECHANICAL_ATTENUATION_AUTO | Specifies whether the RFmx driver chooses an attenuation setting based on the hardware settings. |
| RFMXINSTR_ATTR_MECHANICAL_ATTENUATION_VALUE | Specifies the level of mechanical attenuation for the RF path. This value is expressed in dB. |

#### Attachments

None

Parent topic:

Attributes

<!--NI_TOPIC bundle=rfmxinstr-c-api-ref path=group____root__ni_r_fmx_instr__attributes__mechanical__attenuation_1gad6fcb4d44a4f861f7c63c18a39e2a9cc.html language=enus -->
## TOPIC 00031: RFMXINSTR_ATTR_MECHANICAL_ATTENUATION_VALUE

- bundle_id: `rfmxinstr-c-api-ref`
- source_path: `group____root__ni_r_fmx_instr__attributes__mechanical__attenuation_1gad6fcb4d44a4f861f7c63c18a39e2a9cc.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_instr__attributes__mechanical__attenuation_1gad6fcb4d44a4f861f7c63c18a39e2a9cc.html
- document_id: `rfmxinstr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the level of mechanical attenuation for the RF path. This value is expressed in dB. SyntaxRFMXINSTR_ATTR_MECHANICAL_ATTENUATION_VALUENumeric ValueData TypeAccessApplies To7float64Read/WriteN/ARemarks The RFmx driver uses the value of this attribute as the attenuation setting when you set t

### RFMXINSTR_ATTR_MECHANICAL_ATTENUATION_VALUE

Specifies the level of mechanical attenuation for the RF path. This value is expressed in dB.

#### Syntax

RFMXINSTR_ATTR_MECHANICAL_ATTENUATION_VALUE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 7 | float64 | Read/Write | N/A |

#### Remarks

The RFmx driver uses the value of this attribute as the attenuation setting when you set the [RFMXINSTR_ATTR_MECHANICAL_ATTENUATION_AUTO](group____root__ni_r_fmx_instr__attributes__mechanical__attenuation_1gaf9d7cc5be1c02e162b1451859bffc4ca.html) attribute to **False**.

You do not need to use a selector string if you want to configure this attribute for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax.

**Valid values**

| Name (value) | Description |
| --- | --- |
| PXIe-5663/5663E | 0, 16 |
| PXIe-5665 (3.6 GHz) | 0, 10, 20, 30 |
| PXIe-5665 (14 GHz), PXIe-5668 | 0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75 |

**Supported devices**: PXIe-5663/5663E, PXIe-5665, PXIe-5668

Parent topic:

Mechanical Attenuation

<!--NI_TOPIC bundle=rfmxinstr-c-api-ref path=group____root__ni_r_fmx_instr__attributes__mechanical__attenuation_1gaf9d7cc5be1c02e162b1451859bffc4ca.html language=enus -->
## TOPIC 00032: RFMXINSTR_ATTR_MECHANICAL_ATTENUATION_AUTO

- bundle_id: `rfmxinstr-c-api-ref`
- source_path: `group____root__ni_r_fmx_instr__attributes__mechanical__attenuation_1gaf9d7cc5be1c02e162b1451859bffc4ca.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_instr__attributes__mechanical__attenuation_1gaf9d7cc5be1c02e162b1451859bffc4ca.html
- document_id: `rfmxinstr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the RFmx driver chooses an attenuation setting based on the hardware settings. SyntaxRFMXINSTR_ATTR_MECHANICAL_ATTENUATION_AUTONumeric ValueData TypeAccessApplies To6int32Read/WriteN/ARemarks You do not need to use a selector string if you want to configure this attribute for all s

### RFMXINSTR_ATTR_MECHANICAL_ATTENUATION_AUTO

Specifies whether the RFmx driver chooses an attenuation setting based on the hardware settings.

#### Syntax

RFMXINSTR_ATTR_MECHANICAL_ATTENUATION_AUTO

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string if you want to configure this attribute for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax.

The default value is **True**.

**Supported devices**: PXIe-5663/5663E/5665/5668

| Name | Value | Description |
| --- | --- | --- |
| RFMXINSTR_VAL_MECHANICAL_ATTENUATION_AUTO_FALSE | 0 (0x0) | Specifies that the RFmx driver uses the value configured in the RFMXINSTR_ATTR_MECHANICAL_ATTENUATION_VALUE attribute. |
| RFMXINSTR_VAL_MECHANICAL_ATTENUATION_AUTO_TRUE | 1 (0x1) | Specifies that the measurement computes the mechanical attenuation. |

Parent topic:

Mechanical Attenuation

<!--NI_TOPIC bundle=rfmxinstr-c-api-ref path=group____root__ni_r_fmx_instr__attributes__mimo__lo__splitter.html language=enus -->
## TOPIC 00033: LO Splitter

- bundle_id: `rfmxinstr-c-api-ref`
- source_path: `group____root__ni_r_fmx_instr__attributes__mimo__lo__splitter.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_instr__attributes__mimo__lo__splitter.html
- document_id: `rfmxinstr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsLossGroup membersNoneAttachmentsNone

### LO Splitter

#### Groups

- Loss

#### Group members

None

#### Attachments

None

Parent topic:

MIMO

<!--NI_TOPIC bundle=rfmxinstr-c-api-ref path=group____root__ni_r_fmx_instr__attributes__recommended__settings_1ga86b6e26d33c8cdd54db85839cb4107f1.html language=enus -->
## TOPIC 00034: RFMXINSTR_ATTR_RECOMMENDED_CENTER_FREQUENCY

- bundle_id: `rfmxinstr-c-api-ref`
- source_path: `group____root__ni_r_fmx_instr__attributes__recommended__settings_1ga86b6e26d33c8cdd54db85839cb4107f1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_instr__attributes__recommended__settings_1ga86b6e26d33c8cdd54db85839cb4107f1.html
- document_id: `rfmxinstr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the recommended center frequency of the RF signal. This value is expressed in Hz. SyntaxRFMXINSTR_ATTR_RECOMMENDED_CENTER_FREQUENCYNumeric ValueData TypeAccessApplies To57float64Read-OnlyInstrumentRemarksThis attribute is supported only when: RFmxInstr_Initialize function or the RFmxInstr_In

### RFMXINSTR_ATTR_RECOMMENDED_CENTER_FREQUENCY

Returns the recommended center frequency of the RF signal. This value is expressed in Hz.

#### Syntax

RFMXINSTR_ATTR_RECOMMENDED_CENTER_FREQUENCY

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 57 | float64 | Read-Only | Instrument |

#### Remarks

Note

- [RFmxInstr_Initialize](/csh?context=rfmxinstr_rfmxinstrcref_function_initialize) function or the [RFmxInstr_Initialize](group____root__ni_r_fmx_instr__functions__utility_1gaa7511a012338cb4316fda5c7289b15d8.html) function is called with option string "AnalysisOnly=1", or
- [RFmxInstr_InitializeFromNIRFSASessionArray](/csh?context=rfmxinstr_rfmxinstrcref_function_initialize_from_nirfsa_session_array) function is called with option string "AnalysisOnly=1;MaxNumWfms:<n>". Use "<i>instr<n></i>" as the selector string to read this attribute.

Parent topic:

Recommended Settings

<!--NI_TOPIC bundle=rfmxinstr-c-api-ref path=group____root__ni_r_fmx_instr__attributes__recommended__settings_1gac96ffe58c0c279d4f9c29f497ae46ab2.html language=enus -->
## TOPIC 00035: RFMXINSTR_ATTR_RECOMMENDED_ACQUISITION_TYPE

- bundle_id: `rfmxinstr-c-api-ref`
- source_path: `group____root__ni_r_fmx_instr__attributes__recommended__settings_1gac96ffe58c0c279d4f9c29f497ae46ab2.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_instr__attributes__recommended__settings_1gac96ffe58c0c279d4f9c29f497ae46ab2.html
- document_id: `rfmxinstr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the recommended acquisition type for the last committed measurement configuration. SyntaxRFMXINSTR_ATTR_RECOMMENDED_ACQUISITION_TYPENumeric ValueData TypeAccessApplies To39int32Read-OnlyInstrumentRemarksThis attribute is supported only when: RFmxInstr_Initialize function or the RFmxInstr_Ini

### RFMXINSTR_ATTR_RECOMMENDED_ACQUISITION_TYPE

Returns the recommended acquisition type for the last committed measurement configuration.

#### Syntax

RFMXINSTR_ATTR_RECOMMENDED_ACQUISITION_TYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 39 | int32 | Read-Only | Instrument |

#### Remarks

Note

- [RFmxInstr_Initialize](/csh?context=rfmxinstr_rfmxinstrcref_function_initialize) function or the [RFmxInstr_Initialize](group____root__ni_r_fmx_instr__functions__utility_1gaa7511a012338cb4316fda5c7289b15d8.html) function is called with option string "AnalysisOnly=1", or
- [RFmxInstr_InitializeFromNIRFSASessionArray](/csh?context=rfmxinstr_rfmxinstrcref_function_initialize_from_nirfsa_session_array) function is called with option string "AnalysisOnly=1;MaxNumWfms:<n>". Use "<i>instr<n></i>" as the selector string to read this attribute.

| Name | Value | Description |
| --- | --- | --- |
| RFMXINSTR_VAL_RECOMMENDED_ACQUISITION_TYPE_IQ | 0 (0x0) | Indicates that the recommended acquisition type is I/Q. Use the Analyze (IQ) function to perform the measurement. |
| RFMXINSTR_VAL_RECOMMENDED_ACQUISITION_TYPE_SPECTRAL | 1 (0x1) | Indicates that the recommended acquisition type is Spectral. Use Analyze (Spectrum) function to perform the measurement. |
| RFMXINSTR_VAL_RECOMMENDED_ACQUISITION_TYPE_IQ_OR_SPECTRAL | 2 (0x2) | Indicates that the recommended acquisition type is I/Q or Spectral. Use either Analyze (IQ) or Analyze (Spectrum) function to perform the measurement. |

Parent topic:

Recommended Settings

<!--NI_TOPIC bundle=rfmxinstr-c-api-ref path=group____root__ni_r_fmx_instr__attributes__recommended__settings__iq_1ga0bd0bb9f65501efe9281a63b47cf1389.html language=enus -->
## TOPIC 00036: RFMXINSTR_ATTR_RECOMMENDED_IQ_PRE_TRIGGER_TIME

- bundle_id: `rfmxinstr-c-api-ref`
- source_path: `group____root__ni_r_fmx_instr__attributes__recommended__settings__iq_1ga0bd0bb9f65501efe9281a63b47cf1389.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_instr__attributes__recommended__settings__iq_1ga0bd0bb9f65501efe9281a63b47cf1389.html
- document_id: `rfmxinstr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the recommended pretrigger time for I/Q acquisition. This value is expressed in seconds. SyntaxRFMXINSTR_ATTR_RECOMMENDED_IQ_PRE_TRIGGER_TIMENumeric ValueData TypeAccessApplies To44float64Read-OnlyInstrumentRemarksThis attribute is supported only when: RFmxInstr_Initialize function or the RF

### RFMXINSTR_ATTR_RECOMMENDED_IQ_PRE_TRIGGER_TIME

Returns the recommended pretrigger time for I/Q acquisition. This value is expressed in seconds.

#### Syntax

RFMXINSTR_ATTR_RECOMMENDED_IQ_PRE_TRIGGER_TIME

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 44 | float64 | Read-Only | Instrument |

#### Remarks

Note

- [RFmxInstr_Initialize](/csh?context=rfmxinstr_rfmxinstrcref_function_initialize) function or the [RFmxInstr_Initialize](group____root__ni_r_fmx_instr__functions__utility_1gaa7511a012338cb4316fda5c7289b15d8.html) function is called with option string "AnalysisOnly=1", or
- [RFmxInstr_InitializeFromNIRFSASessionArray](/csh?context=rfmxinstr_rfmxinstrcref_function_initialize_from_nirfsa_session_array) function is called with option string "AnalysisOnly=1;MaxNumWfms:<n>". Use "<i>instr<n></i>" as the selector string to read this attribute.

Parent topic:

IQ

<!--NI_TOPIC bundle=rfmxinstr-c-api-ref path=group____root__ni_r_fmx_instr__attributes__recommended__settings__iq_1ga1a4000419451466b1fec4ff6dee69a07.html language=enus -->
## TOPIC 00037: RFMXINSTR_ATTR_RECOMMENDED_IQ_MINIMUM_SAMPLE_RATE

- bundle_id: `rfmxinstr-c-api-ref`
- source_path: `group____root__ni_r_fmx_instr__attributes__recommended__settings__iq_1ga1a4000419451466b1fec4ff6dee69a07.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_instr__attributes__recommended__settings__iq_1ga1a4000419451466b1fec4ff6dee69a07.html
- document_id: `rfmxinstr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the recommended minimum sample rate for I/Q acquisition. This value is expressed in Hz. SyntaxRFMXINSTR_ATTR_RECOMMENDED_IQ_MINIMUM_SAMPLE_RATENumeric ValueData TypeAccessApplies To43float64Read-OnlyInstrumentRemarksThis attribute is supported only when: RFmxInstr_Initialize function or the

### RFMXINSTR_ATTR_RECOMMENDED_IQ_MINIMUM_SAMPLE_RATE

Returns the recommended minimum sample rate for I/Q acquisition. This value is expressed in Hz.

#### Syntax

RFMXINSTR_ATTR_RECOMMENDED_IQ_MINIMUM_SAMPLE_RATE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 43 | float64 | Read-Only | Instrument |

#### Remarks

Note

- [RFmxInstr_Initialize](/csh?context=rfmxinstr_rfmxinstrcref_function_initialize) function or the [RFmxInstr_Initialize](group____root__ni_r_fmx_instr__functions__utility_1gaa7511a012338cb4316fda5c7289b15d8.html) function is called with option string "AnalysisOnly=1", or
- [RFmxInstr_InitializeFromNIRFSASessionArray](/csh?context=rfmxinstr_rfmxinstrcref_function_initialize_from_nirfsa_session_array) function is called with option string "AnalysisOnly=1;MaxNumWfms:<n>". Use "<i>instr<n></i>" as the selector string to read this attribute.

Parent topic:

IQ

<!--NI_TOPIC bundle=rfmxinstr-c-api-ref path=group____root__ni_r_fmx_instr__attributes__recommended__settings__iq_1ga5cac01c9c4fe58331be9f440a28b7f89.html language=enus -->
## TOPIC 00038: RFMXINSTR_ATTR_RECOMMENDED_IQ_ACQUISITION_TIME

- bundle_id: `rfmxinstr-c-api-ref`
- source_path: `group____root__ni_r_fmx_instr__attributes__recommended__settings__iq_1ga5cac01c9c4fe58331be9f440a28b7f89.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_instr__attributes__recommended__settings__iq_1ga5cac01c9c4fe58331be9f440a28b7f89.html
- document_id: `rfmxinstr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the recommended acquisition time for I/Q acquisition. This value is expressed in seconds. SyntaxRFMXINSTR_ATTR_RECOMMENDED_IQ_ACQUISITION_TIMENumeric ValueData TypeAccessApplies To42float64Read-OnlyInstrumentRemarksThis attribute is supported only when: RFmxInstr_Initialize function or the R

### RFMXINSTR_ATTR_RECOMMENDED_IQ_ACQUISITION_TIME

Returns the recommended acquisition time for I/Q acquisition. This value is expressed in seconds.

#### Syntax

RFMXINSTR_ATTR_RECOMMENDED_IQ_ACQUISITION_TIME

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 42 | float64 | Read-Only | Instrument |

#### Remarks

Note

- [RFmxInstr_Initialize](/csh?context=rfmxinstr_rfmxinstrcref_function_initialize) function or the [RFmxInstr_Initialize](group____root__ni_r_fmx_instr__functions__utility_1gaa7511a012338cb4316fda5c7289b15d8.html) function is called with option string "AnalysisOnly=1", or
- [RFmxInstr_InitializeFromNIRFSASessionArray](/csh?context=rfmxinstr_rfmxinstrcref_function_initialize_from_nirfsa_session_array) function is called with option string "AnalysisOnly=1;MaxNumWfms:<n>". Use "<i>instr<n></i>" as the selector string to read this attribute.

Parent topic:

IQ

<!--NI_TOPIC bundle=rfmxinstr-c-api-ref path=group____root__ni_r_fmx_instr__attributes__recommended__settings__spectral.html language=enus -->
## TOPIC 00039: Spectral

- bundle_id: `rfmxinstr-c-api-ref`
- source_path: `group____root__ni_r_fmx_instr__attributes__recommended__settings__spectral.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_instr__attributes__recommended__settings__spectral.html
- document_id: `rfmxinstr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXINSTR_ATTR_RECOMMENDED_SPECTRAL_ACQUISITION_SPANReturns the recommended acquisition span for spectral acquisition. This value is expressed in Hz. RFMXINSTR_ATTR_RECOMMENDED_SPECTRAL_FFT_WINDOWReturns the recommended FFT window type for spectral acquisition.

### Spectral

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXINSTR_ATTR_RECOMMENDED_SPECTRAL_ACQUISITION_SPAN | Returns the recommended acquisition span for spectral acquisition. This value is expressed in Hz. |
| RFMXINSTR_ATTR_RECOMMENDED_SPECTRAL_FFT_WINDOW | Returns the recommended FFT window type for spectral acquisition. |
| RFMXINSTR_ATTR_RECOMMENDED_SPECTRAL_RESOLUTION_BANDWIDTH | Returns the recommended FFT bin width for spectral acquisition. This value is expressed in Hz. |

#### Attachments

None

Parent topic:

Recommended Settings

<!--NI_TOPIC bundle=rfmxinstr-c-api-ref path=group____root__ni_r_fmx_instr__attributes__rf__attenuation_1ga79366f122abccf48cb87573d9329c336.html language=enus -->
## TOPIC 00040: RFMXINSTR_ATTR_RF_ATTENUATION_VALUE

- bundle_id: `rfmxinstr-c-api-ref`
- source_path: `group____root__ni_r_fmx_instr__attributes__rf__attenuation_1ga79366f122abccf48cb87573d9329c336.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_instr__attributes__rf__attenuation_1ga79366f122abccf48cb87573d9329c336.html
- document_id: `rfmxinstr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the nominal attenuation setting for all attenuators before the first mixer in the RF signal chain. This value is expressed in dB. SyntaxRFMXINSTR_ATTR_RF_ATTENUATION_VALUENumeric ValueData TypeAccessApplies To5float64Read/WriteN/ARemarks The RFmx driver uses the value of this attribute as

### RFMXINSTR_ATTR_RF_ATTENUATION_VALUE

Specifies the nominal attenuation setting for all attenuators before the first mixer in the RF signal chain. This value is expressed in dB.

#### Syntax

RFMXINSTR_ATTR_RF_ATTENUATION_VALUE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5 | float64 | Read/Write | N/A |

#### Remarks

The RFmx driver uses the value of this attribute as the attenuation setting when you set the [RFMXINSTR_ATTR_RF_ATTENUATION_AUTO](group____root__ni_r_fmx_instr__attributes__rf__attenuation_1gadfcdc90ac16ece2ebb2baed8dcb77efb.html) attribute to **False**.

| Name (value) | Description |
| --- | --- |
| PXIe-5663/5663E | You can change the attenuation value to modify the amount of noise and distortion. Higher attenuation levels increase the noise level but decreases distortion; lower attenuation levels decrease the noise level but increases distortion. |
| PXIe-5603/5605/5665/5668 | Refer to the PXIe-5665 or the PXIe-5668 RF Attenuation and Signal Levels topic in the NI RF Vector Signal Analyzers Help for more information about configuring attenuation. |

You do not need to use a selector string if you want to configure this attribute for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax.

The valid values for this attribute depend on the device configuration.

**Supported devices**: PXIe-5663/5663E/5603/5605/5665/5668

Parent topic:

RF Attenuation

<!--NI_TOPIC bundle=rfmxinstr-c-api-ref path=group____root__ni_r_fmx_instr__attributes__rf__attenuation_1gadfcdc90ac16ece2ebb2baed8dcb77efb.html language=enus -->
## TOPIC 00041: RFMXINSTR_ATTR_RF_ATTENUATION_AUTO

- bundle_id: `rfmxinstr-c-api-ref`
- source_path: `group____root__ni_r_fmx_instr__attributes__rf__attenuation_1gadfcdc90ac16ece2ebb2baed8dcb77efb.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_instr__attributes__rf__attenuation_1gadfcdc90ac16ece2ebb2baed8dcb77efb.html
- document_id: `rfmxinstr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the RFmx driver computes the RF attenuation. SyntaxRFMXINSTR_ATTR_RF_ATTENUATION_AUTONumeric ValueData TypeAccessApplies To4int32Read/WriteN/ARemarks If you set this attribute to True, the RFmx driver chooses an attenuation setting based on the reference level configured on the per

### RFMXINSTR_ATTR_RF_ATTENUATION_AUTO

Specifies whether the RFmx driver computes the RF attenuation.

#### Syntax

RFMXINSTR_ATTR_RF_ATTENUATION_AUTO

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 4 | int32 | Read/Write | N/A |

#### Remarks

If you set this attribute to **True**, the RFmx driver chooses an attenuation setting based on the reference level configured on the personality.

You do not need to use a selector string if you want to configure this attribute for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax.

The default value is **True**.

**Supported devices**: PXIe-5663/5663E, PXIe-5665/5668

| Name | Value | Description |
| --- | --- | --- |
| RFMXINSTR_VAL_RF_ATTENUATION_AUTO_FALSE | 0 (0x0) | Specifies that the RFmx driver uses the value configured using RFMXINSTR_ATTR_RF_ATTENUATION_VALUE attribute. |
| RFMXINSTR_VAL_RF_ATTENUATION_AUTO_TRUE | 1 (0x1) | Specifies that the RFmx driver computes the RF attenuation. |

Parent topic:

RF Attenuation

<!--NI_TOPIC bundle=rfmxinstr-c-api-ref path=group____root__ni_r_fmx_instr__attributes__trigger.html language=enus -->
## TOPIC 00042: Trigger

- bundle_id: `rfmxinstr-c-api-ref`
- source_path: `group____root__ni_r_fmx_instr__attributes__trigger.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_instr__attributes__trigger.html
- document_id: `rfmxinstr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsAdvanceStartGroup membersNameDescriptionRFMXINSTR_ATTR_TRIGGER_EXPORT_OUTPUT_TERMINALSpecifies the destination terminal for the exported Reference Trigger. You can also choose not to export any signal. RFMXINSTR_ATTR_TRIGGER_TERMINAL_NAMEReturns the fully qualified signal name as a string. Att

### Trigger

#### Groups

- Advance
- Start

#### Group members

| Name | Description |
| --- | --- |
| RFMXINSTR_ATTR_TRIGGER_EXPORT_OUTPUT_TERMINAL | Specifies the destination terminal for the exported Reference Trigger. You can also choose not to export any signal. |
| RFMXINSTR_ATTR_TRIGGER_TERMINAL_NAME | Returns the fully qualified signal name as a string. |

#### Attachments

None

Parent topic:

Attributes

<!--NI_TOPIC bundle=rfmxinstr-c-api-ref path=group____root__ni_r_fmx_instr__attributes__trigger__advance_1ga231744d78012ef76ac4c0faa28508063.html language=enus -->
## TOPIC 00043: RFMXINSTR_ATTR_ADVANCE_TRIGGER_TYPE

- bundle_id: `rfmxinstr-c-api-ref`
- source_path: `group____root__ni_r_fmx_instr__attributes__trigger__advance_1ga231744d78012ef76ac4c0faa28508063.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_instr__attributes__trigger__advance_1ga231744d78012ef76ac4c0faa28508063.html
- document_id: `rfmxinstr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the advance trigger is a digital edge or a software trigger. SyntaxRFMXINSTR_ATTR_ADVANCE_TRIGGER_TYPENumeric ValueData TypeAccessApplies To103int32Read/WriteN/ARemarks You do not need to use a selector string if you want to configure this attribute for all signal instances. Specif

### RFMXINSTR_ATTR_ADVANCE_TRIGGER_TYPE

Specifies whether the advance trigger is a digital edge or a software trigger.

#### Syntax

RFMXINSTR_ATTR_ADVANCE_TRIGGER_TYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 103 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string if you want to configure this attribute for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax.

The default value is **None**.

**Supported devices**: PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

| Name | Value | Description |
| --- | --- | --- |
| RFMXINSTR_VAL_ADVANCE_TRIGGER_TYPE_NONE | 0 (0x0) | No advance trigger is configured. |
| RFMXINSTR_VAL_ADVANCE_TRIGGER_TYPE_DIGITAL_EDGE | 1 (0x1) | The advance trigger is not asserted until a digital edge is detected. The source of the digital edge is specified with the RFMXINSTR_ATTR_ADVANCE_TRIGGER_DIGITAL_EDGE_SOURCE attribute. |
| RFMXINSTR_VAL_ADVANCE_TRIGGER_TYPE_SOFTWARE | 3 (0x3) | The advance trigger is not asserted until a software trigger occurs. You can assert the software trigger by calling the RFmxInstr Send Software Edge Trigger function. |

Parent topic:

Advance

<!--NI_TOPIC bundle=rfmxinstr-c-api-ref path=group____root__ni_r_fmx_instr__attributes__trigger__advance__digital__edge_1gac4c25213cb6d61ebaf0b3210742e81dc.html language=enus -->
## TOPIC 00044: RFMXINSTR_ATTR_ADVANCE_TRIGGER_DIGITAL_EDGE_SOURCE

- bundle_id: `rfmxinstr-c-api-ref`
- source_path: `group____root__ni_r_fmx_instr__attributes__trigger__advance__digital__edge_1gac4c25213cb6d61ebaf0b3210742e81dc.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_instr__attributes__trigger__advance__digital__edge_1gac4c25213cb6d61ebaf0b3210742e81dc.html
- document_id: `rfmxinstr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the source terminal for the advance trigger. SyntaxRFMXINSTR_ATTR_ADVANCE_TRIGGER_DIGITAL_EDGE_SOURCENumeric ValueData TypeAccessApplies To104char[]Read/WriteN/ARemarks This attribute is used only when the RFMXINSTR_ATTR_ADVANCE_TRIGGER_TYPE attribute is set to Digital Edge.You do not need

### RFMXINSTR_ATTR_ADVANCE_TRIGGER_DIGITAL_EDGE_SOURCE

Specifies the source terminal for the advance trigger.

#### Syntax

RFMXINSTR_ATTR_ADVANCE_TRIGGER_DIGITAL_EDGE_SOURCE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 104 | char[] | Read/Write | N/A |

#### Remarks

This attribute is used only when the [RFMXINSTR_ATTR_ADVANCE_TRIGGER_TYPE](group____root__ni_r_fmx_instr__attributes__trigger__advance_1ga231744d78012ef76ac4c0faa28508063.html) attribute is set to **Digital Edge**.

You do not need to use a selector string if you want to configure this attribute for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax.

The default value of this attribute is "" (empty string).

**Supported devices**: PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

| Name | Value | Description |
| --- | --- | --- |
| RFMXINSTR_VAL_PFI0_STR | PFI0 | The trigger is received on PFI 0. For the PXIe-5841 with PXIe-5655, the trigger is received on the PXIe-5841 PFI 0. |
| RFMXINSTR_VAL_PFI1_STR | PFI1 | The trigger is received on PFI 1. |
| RFMXINSTR_VAL_PXI_TRIG0_STR | PXI_Trig0 | The trigger is received on PXI trigger line 0. |
| RFMXINSTR_VAL_PXI_TRIG1_STR | PXI_Trig1 | The trigger is received on PXI trigger line 1. |
| RFMXINSTR_VAL_PXI_TRIG2_STR | PXI_Trig2 | The trigger is received on PXI trigger line 2. |
| RFMXINSTR_VAL_PXI_TRIG3_STR | PXI_Trig3 | The trigger is received on PXI trigger line 3. |
| RFMXINSTR_VAL_PXI_TRIG4_STR | PXI_Trig4 | The trigger is received on PXI trigger line 4. |
| RFMXINSTR_VAL_PXI_TRIG5_STR | PXI_Trig5 | The trigger is received on PXI trigger line 5. |
| RFMXINSTR_VAL_PXI_TRIG6_STR | PXI_Trig6 | The trigger is received on PXI trigger line 6. |
| RFMXINSTR_VAL_PXI_TRIG7_STR | PXI_Trig7 | The trigger is received on PXI trigger line 7. |
| RFMXINSTR_VAL_PXI_STAR_STR | PXI_STAR | The trigger is received on the PXI star trigger line. This value is not valid for PXIe-5644/5645/5646. |
| RFMXINSTR_VAL_PXIE_DSTARB_STR | PXIe_DStarB | The trigger is received on the PXIe DStar B trigger line. This value is valid only for PXIe-5820/5830/5831/5832/5840/5841/5842/5860. |
| RFMXINSTR_VAL_TIMER_EVENT_STR | TimerEvent | The trigger is received from the timer event. This value is valid only for PXIe-5820/5840/5841/5842/5860 and for digital edge advance triggers on PXIe-5663E/5665. |
| RFMXINSTR_VAL_DIO_PFI0_STR | DIO/PFI0 | The trigger is received on PFI 0 of the DIO front panel connector. |
| RFMXINSTR_VAL_DIO_PFI1_STR | DIO/PFI1 | The trigger is received on PFI 1 of the DIO front panel connector. |
| RFMXINSTR_VAL_DIO_PFI2_STR | DIO/PFI2 | The trigger is received on PFI 2 of the DIO front panel connector. |
| RFMXINSTR_VAL_DIO_PFI3_STR | DIO/PFI3 | The trigger is received on PFI 3 of the DIO front panel connector. |
| RFMXINSTR_VAL_DIO_PFI4_STR | DIO/PFI4 | The trigger is received on PFI 4 of the DIO front panel connector. |
| RFMXINSTR_VAL_DIO_PFI5_STR | DIO/PFI5 | The trigger is received on PFI 5 of the DIO front panel connector. |
| RFMXINSTR_VAL_DIO_PFI6_STR | DIO/PFI6 | The trigger is received on PFI 6 of the DIO front panel connector. |
| RFMXINSTR_VAL_DIO_PFI7_STR | DIO/PFI7 | The trigger is received on PFI 7 of the DIO front panel connector. |

Parent topic:

Digital Edge

<!--NI_TOPIC bundle=rfmxinstr-c-api-ref path=group____root__ni_r_fmx_instr__attributes__trigger__start.html language=enus -->
## TOPIC 00045: Start

- bundle_id: `rfmxinstr-c-api-ref`
- source_path: `group____root__ni_r_fmx_instr__attributes__trigger__start.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_instr__attributes__trigger__start.html
- document_id: `rfmxinstr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsDigital EdgeGroup membersNameDescriptionRFMXINSTR_ATTR_START_TRIGGER_EXPORT_OUTPUT_TERMINALSpecifies the destination terminal for the exported start trigger. RFMXINSTR_ATTR_START_TRIGGER_TERMINAL_NAMEReturns the fully qualified signal name as a string. RFMXINSTR_ATTR_START_TRIGGER_TYPESpecifie

### Start

#### Groups

- Digital Edge

#### Group members

| Name | Description |
| --- | --- |
| RFMXINSTR_ATTR_START_TRIGGER_EXPORT_OUTPUT_TERMINAL | Specifies the destination terminal for the exported start trigger. |
| RFMXINSTR_ATTR_START_TRIGGER_TERMINAL_NAME | Returns the fully qualified signal name as a string. |
| RFMXINSTR_ATTR_START_TRIGGER_TYPE | Specifies whether the start trigger is a digital edge or a software trigger. |

#### Attachments

None

Parent topic:

Trigger

<!--NI_TOPIC bundle=rfmxinstr-c-api-ref path=group____root__ni_r_fmx_instr__attributes__trigger__start_1ga15ddd69a1b87723433e865f457d9b46d.html language=enus -->
## TOPIC 00046: RFMXINSTR_ATTR_START_TRIGGER_EXPORT_OUTPUT_TERMINAL

- bundle_id: `rfmxinstr-c-api-ref`
- source_path: `group____root__ni_r_fmx_instr__attributes__trigger__start_1ga15ddd69a1b87723433e865f457d9b46d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_instr__attributes__trigger__start_1ga15ddd69a1b87723433e865f457d9b46d.html
- document_id: `rfmxinstr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the destination terminal for the exported start trigger. SyntaxRFMXINSTR_ATTR_START_TRIGGER_EXPORT_OUTPUT_TERMINALNumeric ValueData TypeAccessApplies To101char[]Read/WriteN/ARemarks You can also choose not to export any signal. This attribute is not supported on a MIMO session.You do not n

### RFMXINSTR_ATTR_START_TRIGGER_EXPORT_OUTPUT_TERMINAL

Specifies the destination terminal for the exported start trigger.

#### Syntax

RFMXINSTR_ATTR_START_TRIGGER_EXPORT_OUTPUT_TERMINAL

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 101 | char[] | Read/Write | N/A |

#### Remarks

Note

This attribute is not supported on a MIMO session.

You do not need to use a selector string if you want to configure this attribute for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax.

The default value is **Do not export signal**.

**Supported devices**: PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

| Name | Value | Description |
| --- | --- | --- |
| RFMXINSTR_VAL_NONE_STR |  | Does not export the signal. |
| RFMXINSTR_VAL_CLK_OUT_STR | ClkOut | Exports the signal to the CLK OUT connector on the PXIe-5622/5624 front panel. |
| RFMXINSTR_VAL_REF_OUT_STR | RefOut | Exports the signal to the REF IN/OUT terminal on PXIe-5652, and the REF OUT terminal on PXIe-5644/5645/5646 and PXIe-5820/5830/5831/5832/5840/5841/5842/5860. |
| RFMXINSTR_VAL_REF_OUT2_STR | RefOut2 | Exports the signal to the REF OUT2 terminal on the LO. This connector exists only on PXIe-5652. |
| RFMXINSTR_VAL_PFI0_STR | PFI0 | Exports the signal to the PFI 0 connector. For the PXIe-5841 with PXIe-5655, the signal is exported to the PXIe-5841 PFI 0. |
| RFMXINSTR_VAL_PFI1_STR | PFI1 | Exports the signal to the PFI 1 connector on PXIe-5142 and PXIe-5622. |
| RFMXINSTR_VAL_PXI_TRIG0_STR | PXI_Trig0 | Exports the signal to the PXI trigger line 0. |
| RFMXINSTR_VAL_PXI_TRIG1_STR | PXI_Trig1 | Exports the signal to the PXI trigger line 1. |
| RFMXINSTR_VAL_PXI_TRIG2_STR | PXI_Trig2 | Exports the signal to the PXI trigger line 2. |
| RFMXINSTR_VAL_PXI_TRIG3_STR | PXI_Trig3 | Exports the signal to the PXI trigger line 3. |
| RFMXINSTR_VAL_PXI_TRIG4_STR | PXI_Trig4 | Exports the signal to the PXI trigger line 4. |
| RFMXINSTR_VAL_PXI_TRIG5_STR | PXI_Trig5 | Exports the signal to the PXI trigger line 5. |
| RFMXINSTR_VAL_PXI_TRIG6_STR | PXI_Trig6 | Exports the signal to the PXI trigger line 6. |
| RFMXINSTR_VAL_PXI_TRIG7_STR | PXI_Trig7 | Exports the signal to the PXI trigger line 7. |
| RFMXINSTR_VAL_PXI_STAR_STR | PXI_STAR | Exports the signal to the PXI star trigger line. This value is not valid for PXIe-5644/5645/5646. |
| RFMXINSTR_VAL_PXIE_DSTARC_STR | PXIe_DStarC | Exports the signal to the PXIe DStar C trigger line. This value is valid only for PXIe-5820/5830/5831/5832/5840/5841/5842/5860. |
| RFMXINSTR_VAL_DIO_PFI0_STR | DIO/PFI0 | Exports the signal to the PFI 0 on the DIO front panel connector. |
| RFMXINSTR_VAL_DIO_PFI1_STR | DIO/PFI1 | Exports the signal to the PFI 1 on the DIO front panel connector. |
| RFMXINSTR_VAL_DIO_PFI2_STR | DIO/PFI2 | Exports the signal to the PFI 2 on the DIO front panel connector. |
| RFMXINSTR_VAL_DIO_PFI3_STR | DIO/PFI3 | Exports the signal to the PFI 3 on the DIO front panel connector. |
| RFMXINSTR_VAL_DIO_PFI4_STR | DIO/PFI4 | Exports the signal to the PFI 4 on the DIO front panel connector. |
| RFMXINSTR_VAL_DIO_PFI5_STR | DIO/PFI5 | Exports the signal to the PFI 5 on the DIO front panel connector. |
| RFMXINSTR_VAL_DIO_PFI6_STR | DIO/PFI6 | Exports the signal to the PFI 6 on the DIO front panel connector. |
| RFMXINSTR_VAL_DIO_PFI7_STR | DIO/PFI7 | Exports the signal to the PFI 7 on the DIO front panel connector. |

Parent topic:

Start

<!--NI_TOPIC bundle=rfmxinstr-c-api-ref path=group____root__ni_r_fmx_instr__attributes__trigger__start_1gaa60f016353a84268e926bfded4ba7935.html language=enus -->
## TOPIC 00047: RFMXINSTR_ATTR_START_TRIGGER_TERMINAL_NAME

- bundle_id: `rfmxinstr-c-api-ref`
- source_path: `group____root__ni_r_fmx_instr__attributes__trigger__start_1gaa60f016353a84268e926bfded4ba7935.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_instr__attributes__trigger__start_1gaa60f016353a84268e926bfded4ba7935.html
- document_id: `rfmxinstr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the fully qualified signal name as a string. SyntaxRFMXINSTR_ATTR_START_TRIGGER_TERMINAL_NAMENumeric ValueData TypeAccessApplies To102char[]Read-OnlyN/ARemarks The standard format is as follows: PXIe-5820/5840/5841/5842: /ModuleName/ai/0/StartTrigger, where ModuleName is the name of your dev

### RFMXINSTR_ATTR_START_TRIGGER_TERMINAL_NAME

Returns the fully qualified signal name as a string.

#### Syntax

RFMXINSTR_ATTR_START_TRIGGER_TERMINAL_NAME

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 102 | char[] | Read-Only | N/A |

#### Remarks

- **PXIe-5820/5840/5841/5842**: */ModuleName/ai/0/StartTrigger*, where *ModuleName* is the name of your device in MAX.
- **PXIe-5830/5831/5832**: */BasebandModule/ai/0/StartTrigger*, where *BasebandModule* is the name of your device in MAX.
- **PXIe-5860**: */ModuleName/ai/ChannelNumber/StartTrigger,*, where *ModuleName*is the name of your device in MAX and ChannelNumber is the channel number (0 or 1).
- **All other devices**: */DigitizerName/StartTrigger*, where *DigitizerName* is the name of your associated digitizer module in MAX.

Note

This attribute is not supported on a MIMO session.

**Supported devices**: PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

Parent topic:

Start

<!--NI_TOPIC bundle=rfmxinstr-c-api-ref path=group____root__ni_r_fmx_instr__attributes__trigger__start__digital__edge.html language=enus -->
## TOPIC 00048: Digital Edge

- bundle_id: `rfmxinstr-c-api-ref`
- source_path: `group____root__ni_r_fmx_instr__attributes__trigger__start__digital__edge.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_instr__attributes__trigger__start__digital__edge.html
- document_id: `rfmxinstr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXINSTR_ATTR_START_TRIGGER_DIGITAL_EDGESpecifies the active edge for the start trigger. This attribute is used only when you set the RFMXINSTR_ATTR_START_TRIGGER_TYPE attribute to Digital Edge. RFMXINSTR_ATTR_START_TRIGGER_DIGITAL_EDGE_SOURCESpecifies the sour

### Digital Edge

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXINSTR_ATTR_START_TRIGGER_DIGITAL_EDGE | Specifies the active edge for the start trigger. This attribute is used only when you set the RFMXINSTR_ATTR_START_TRIGGER_TYPE attribute to Digital Edge. |
| RFMXINSTR_ATTR_START_TRIGGER_DIGITAL_EDGE_SOURCE | Specifies the source terminal for the start trigger. This attribute is used only when you set the RFMXINSTR_ATTR_START_TRIGGER_TYPE attribute to Digital Edge. |

#### Attachments

None

Parent topic:

Start

<!--NI_TOPIC bundle=rfmxinstr-c-api-ref path=group____root__ni_r_fmx_instr__functions.html language=enus -->
## TOPIC 00049: Functions

- bundle_id: `rfmxinstr-c-api-ref`
- source_path: `group____root__ni_r_fmx_instr__functions.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_instr__functions.html
- document_id: `rfmxinstr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsBuild StringCalibrationConfigurationSet and Get AttributesUtilityGroup membersNameDescriptionRFmxInstr_CfgSParameterExternalAttenuationPowerCompensationEnabledRFmxInstr_CloseCloses the RFmx session. RFmxInstr_GetErrorRetrieves and then clears the error information for the session or the curren

### Functions

#### Groups

- Build String
- Calibration
- Configuration
- Set and Get Attributes
- Utility

#### Group members

| Name | Description |
| --- | --- |
| RFmxInstr_CfgSParameterExternalAttenuationPowerCompensationEnabled |  |
| RFmxInstr_Close | Closes the RFmx session. |
| RFmxInstr_GetError | Retrieves and then clears the error information for the session or the current execution thread. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the errorDescriptionBufferSize parameter. |
| RFmxInstr_GetErrorString | Converts a status code returned by an RFmxInstr function into a user-readable string. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the errorDescriptionBufferSize parameter. |
| RFmxInstr_RegisterExternalRFSubsystemCallbacks |  |
| RFmxInstr_UnregisterExternalRFSubsystemCallbacks |  |

#### Attachments

None

Parent topic:

niRFmxInstr.h

<!--NI_TOPIC bundle=rfmxinstr-c-api-ref path=group____root__ni_r_fmx_instr__functions_1ga47912fb504106aadfbff53469b6051e5.html language=enus -->
## TOPIC 00050: RFmxInstr_GetErrorString

- bundle_id: `rfmxinstr-c-api-ref`
- source_path: `group____root__ni_r_fmx_instr__functions_1ga47912fb504106aadfbff53469b6051e5.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_instr__functions_1ga47912fb504106aadfbff53469b6051e5.html
- document_id: `rfmxinstr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts a status code returned by an RFmxInstr function into a user-readable string. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the errorDescriptionBufferSize parameter. Syntaxint32 __stdcall RFmxInstr_GetErrorString(niRFmxInstrHandle

### RFmxInstr_GetErrorString

Converts a status code returned by an RFmxInstr function into a user-readable string. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **errorDescriptionBufferSize** parameter.

#### Syntax

int32 __stdcall RFmxInstr_GetErrorString(niRFmxInstrHandle instrumentHandle, int32 errorCode, int32 errorDescriptionBufferSize, char errorDescription[])

#### Remarks

If the error description, including the terminating NULL byte, is larger than the size you indicate in the **errorDescriptionBufferSize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

If you want to call this function just to get the required buffer size, you must pass 0 for **errorDescriptionBufferSize** and NULL for the **errorDescription** buffer.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxInstr_Initialize function. |
| errorCode | [in] | int32 | Passes the statusOrRequiredSize parameter that is returned from any RFmxInstr function. |
| errorDescriptionBufferSize | [in] | int32 | Passes the number of bytes in the char array you specify in errorDescription.If the error description, including the terminating NULL byte, contains more bytes than you indicate in this parameter, the function copies errorDescriptionBufferSize - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the size of the buffer that you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7. |
| errorDescription | [out] | char[] | Returns the user-readable message string that corresponds to the status code you specify.If you pass 0 for errorDescriptionBufferSize, you can pass NULL for the errorDescription buffer parameter to get the size of error description message. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

When the **statusOrRequiredSize** return value returns the buffer size, the status code is not returned.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxInstr_GetError](group____root__ni_r_fmx_instr__functions_1ga3c9efe926e0a627b12a3ba6c33e22657.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxinstr-c-api-ref path=group____root__ni_r_fmx_instr__functions_1gae3951a740bc8f51ed2b0425c28d1980d.html language=enus -->
## TOPIC 00051: RFmxInstr_Close

- bundle_id: `rfmxinstr-c-api-ref`
- source_path: `group____root__ni_r_fmx_instr__functions_1gae3951a740bc8f51ed2b0425c28d1980d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_instr__functions_1gae3951a740bc8f51ed2b0425c28d1980d.html
- document_id: `rfmxinstr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Closes the RFmx session. Syntaxint32 __stdcall RFmxInstr_Close(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 forceDestroy)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter identifies the instrument session. This parameter is obtained from th

### RFmxInstr_Close

Closes the RFmx session.

#### Syntax

int32 __stdcall RFmxInstr_Close(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 forceDestroy)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter identifies the instrument session. This parameter is obtained from the RFmxInstr_Initialize function or the RFmxInstr_InitializeFromNIRFSASessionArray function. |
| selectorString | [in] | char[] | Specifies a selector string. Pass an empty string. |
| forceDestroy | [in] | int32 | This parameter indicates whether to forcefully destroy the RFmx session.The default value is FALSE.Name (value)DescriptionTRUEForcefully destroys the RFmx session. You do not have to call the RFmxInstr Close function multiple times. Destroying the RFmx session invalidates all references to the session.FALSEDestroys the RFmx session only if you call the RFmxInstr Close function a number of times equal to the number of times you obtained a reference to the RFmx session. |
| Name (value) | Description |  |  |
| TRUE | Forcefully destroys the RFmx session. You do not have to call the RFmxInstr Close function multiple times. Destroying the RFmx session invalidates all references to the session. |  |  |
| FALSE | Destroys the RFmx session only if you call the RFmxInstr Close function a number of times equal to the number of times you obtained a reference to the RFmx session. |  |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxInstr_GetError](group____root__ni_r_fmx_instr__functions_1ga3c9efe926e0a627b12a3ba6c33e22657.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxinstr-c-api-ref path=group____root__ni_r_fmx_instr__functions__build__string_1ga401b235acd0b4f352213f8098ae34796.html language=enus -->
## TOPIC 00052: RFmxInstr_BuildInstrumentString

- bundle_id: `rfmxinstr-c-api-ref`
- source_path: `group____root__ni_r_fmx_instr__functions__build__string_1ga401b235acd0b4f352213f8098ae34796.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_instr__functions__build__string_1ga401b235acd0b4f352213f8098ae34796.html
- document_id: `rfmxinstr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates the instrument string to use as the Selector String for reading the recommended settings. Syntaxint32 __stdcall RFmxInstr_BuildInstrumentString(char selectorString[], int32 selectorStringOutLength, char selectorStringOut[], int32 instrNumber)ParametersNameDirectionTypeDescriptionselectorStri

### RFmxInstr_BuildInstrumentString

Creates the instrument string to use as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) for reading the recommended settings.

#### Syntax

int32 __stdcall RFmxInstr_BuildInstrumentString(char selectorString[], int32 selectorStringOutLength, char selectorStringOut[], int32 instrNumber)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| selectorString | [in] | char[] | This parameter specifies the selector string. The default value is "" (empty string).Example:"" |
| selectorStringOutLength | [out] | int32 | Specifies the length of the string that is returned by the selectorStringOut parameter. To get the minimum buffer size required to build the selector string, set the selectorStringOutLength parameter to 0. |
| selectorStringOut | [out] | char[] | This parameter returns the selector string created by this function. |
| instrNumber | [in] | int32 | This parameter specifies the instrument number for which you want the recommended settings to be read. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxInstr_GetError](group____root__ni_r_fmx_instr__functions_1ga3c9efe926e0a627b12a3ba6c33e22657.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Build String

<!--NI_TOPIC bundle=rfmxinstr-c-api-ref path=group____root__ni_r_fmx_instr__functions__build__string_1ga8cb251d4a6b8dbb4a85a4f2fb524d865.html language=enus -->
## TOPIC 00053: RFmxInstr_BuildCalibrationPlaneString

- bundle_id: `rfmxinstr-c-api-ref`
- source_path: `group____root__ni_r_fmx_instr__functions__build__string_1ga8cb251d4a6b8dbb4a85a4f2fb524d865.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_instr__functions__build__string_1ga8cb251d4a6b8dbb4a85a4f2fb524d865.html
- document_id: `rfmxinstr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates the selector string to use with external attenuation table functions. Syntaxint32 __stdcall RFmxInstr_BuildCalibrationPlaneString(char selectorString[], int32 selectorStringOutLength, char calibrationPlaneName)ParametersNameDirectionTypeDescriptionselectorString[in]char[]This parameter retur

### RFmxInstr_BuildCalibrationPlaneString

Creates the selector string to use with external attenuation table functions.

#### Syntax

int32 __stdcall RFmxInstr_BuildCalibrationPlaneString(char selectorString[], int32 selectorStringOutLength, char calibrationPlaneName)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| selectorString | [in] | char[] | This parameter returns the selector string created by this function. |
| selectorStringOutLength | [out] | int32 | Specifies the length of the string that is returned by the selectorStringOut parameter. To get the minimum buffer size required to build the selector string, set the selectorStringOutLength parameter to 0. |
| calibrationPlaneName | [in] | char | This parameter specifies the calibration plane name for building the selector string. This input accepts the calibration plane name with or without the "calplane::" prefix. The default value is "" (empty string).Example:"""calplane::plane0""plane0" |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxInstr_GetError](group____root__ni_r_fmx_instr__functions_1ga3c9efe926e0a627b12a3ba6c33e22657.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Build String

<!--NI_TOPIC bundle=rfmxinstr-c-api-ref path=group____root__ni_r_fmx_instr__functions__build__string_1gab1425a445e08b9ec23b5011f7d6509d7.html language=enus -->
## TOPIC 00054: RFmxInstr_BuildPortString2

- bundle_id: `rfmxinstr-c-api-ref`
- source_path: `group____root__ni_r_fmx_instr__functions__build__string_1gab1425a445e08b9ec23b5011f7d6509d7.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_instr__functions__build__string_1gab1425a445e08b9ec23b5011f7d6509d7.html
- document_id: `rfmxinstr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates the port string to use as the selector string with External Attenuation Table functions. On a MIMO session, this function can be used to build port string to use as a selector string for configuring or reading port-specific properties and external attenuation table functions. Syntaxint32 __s

### RFmxInstr_BuildPortString2

Creates the port string to use as the selector string with External Attenuation Table functions. On a MIMO session, this function can be used to build port string to use as a selector string for configuring or reading port-specific properties and external attenuation table functions.

#### Syntax

int32 __stdcall RFmxInstr_BuildPortString2(char selectorString[], char portName[], char deviceName[], int32 channelNumber, int32 selectorStringOutLength, char selectorStringOut[])

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| selectorString | [in] | char[] | Specifies the calibration plane string when used for building port string for the external attenuation table functions. If you do not specify the calibration plane string, the default calibration plane instance is used.Example:"""calplane::plane0"You can use the RFmxInstr_BuildCalibrationPlaneString to build the selector string. |
| portName | [in] | char[] | Specifies the port for building the selector string. |
| deviceName | [in] | char[] | Specifies the device name for building the selector string. |
| channelNumber | [in] | int32 | Specifies the channel number for building the selector string. |
| selectorStringOutLength | [in] | int32 | Specifies the length of the string that is returned by the selectorStringOut parameter. To get the minimum buffer size required to build the selector string, set the selectorStringOutLength parameter to 0. |
| selectorStringOut | [out] | char[] | Returns the selector string created by this function. You can pass NULL for this parameter if selectorStringLength is set to 0, which will return the minimum buffer size required to create the signal string. If the selectorString buffer is not large enough to build the signal string, the function returns an error. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxInstr_GetError](group____root__ni_r_fmx_instr__functions_1ga3c9efe926e0a627b12a3ba6c33e22657.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Build String

<!--NI_TOPIC bundle=rfmxinstr-c-api-ref path=group____root__ni_r_fmx_instr__functions__calibration.html language=enus -->
## TOPIC 00055: Calibration

- bundle_id: `rfmxinstr-c-api-ref`
- source_path: `group____root__ni_r_fmx_instr__functions__calibration.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_instr__functions__calibration.html
- document_id: `rfmxinstr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsUtilityGroup membersNameDescriptionRFmxInstr_IsSelfCalibrateValidReturns an array to indicate which calibration steps contain valid calibration data. To omit steps with the valid calibration data from self-calibration, you can pass the Valid Steps parameter to the Steps To Omit parameter of th

### Calibration

#### Groups

- Utility

#### Group members

| Name | Description |
| --- | --- |
| RFmxInstr_IsSelfCalibrateValid | Returns an array to indicate which calibration steps contain valid calibration data. To omit steps with the valid calibration data from self-calibration, you can pass the Valid Steps parameter to the Steps To Omit parameter of the RFmxInstr_SelfCalibrate function. On a MIMO session, use the Selector String parameter to get the self-calibration validity for a specific MIMO port. |
| RFmxInstr_SelfCalibrate | Self-calibrates the NI-RFSA device and associated modules that support self-calibration. If self-calibration completes successfully, the new calibration constants are stored immediately in the nonvolatile memory of the module. On a MIMO session, this function self-calibrates all NI-RFSA devices and associated modules that support self-calibration. |
| RFmxInstr_SelfCalibrateRange | Self-calibrates all configurations within the specified frequency and reference level limits. If there is an open session for NI-RFSG for your device, it may remain open but cannot be used while this function runs. NI recommends that no external signals are present on the RF In port while the calibration is taking place. For more information about Self Calibrate Range, refer to the niRFSA Self Calibrate Range function topic for your device in the NI RF Vector Signal Analyzers Help. On a MIMO session, this function self-calibrates all NI-RFSA devices and associated modules that support self-calibration. |

#### Attachments

None

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxinstr-c-api-ref path=group____root__ni_r_fmx_instr__functions__calibration_1ga31cb18802e9bc58b926769dbbe87a197.html language=enus -->
## TOPIC 00056: RFmxInstr_SelfCalibrate

- bundle_id: `rfmxinstr-c-api-ref`
- source_path: `group____root__ni_r_fmx_instr__functions__calibration_1ga31cb18802e9bc58b926769dbbe87a197.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_instr__functions__calibration_1ga31cb18802e9bc58b926769dbbe87a197.html
- document_id: `rfmxinstr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Self-calibrates the NI-RFSA device and associated modules that support self-calibration. If self-calibration completes successfully, the new calibration constants are stored immediately in the nonvolatile memory of the module. On a MIMO session, this function self-calibrates all NI-RFSA devices and

### RFmxInstr_SelfCalibrate

Self-calibrates the NI-RFSA device and associated modules that support self-calibration. If self-calibration completes successfully, the new calibration constants are stored immediately in the nonvolatile memory of the module. On a MIMO session, this function self-calibrates all NI-RFSA devices and associated modules that support self-calibration.

#### Syntax

int32 __stdcall RFmxInstr_SelfCalibrate(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 stepsToOmit)

#### Remarks

Refer to the specifications document for your device for more information about how often to self-calibrate. For more information about Self Calibrate, refer to the *niRFSA Self Cal VI* topic for your device in the *NI RF Vector Signal Analyzers Help*.

Note

RFmxInstr_GetNIRFSASession

**Supported devices**: PXIe-5663/5663E/5665/5668, PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter identifies the instrument session. This parameter is obtained from the RFmxInstr_Initialize function or the RFmxInstr_InitializeFromNIRFSASessionArray function. |
| selectorString | [in] | char[] | Specifies a selector string. Pass an empty string. |
| stepsToOmit | [in] | int32 | This parameter specifies which calibration steps to skip during the self-calibration process. The default value is an empty array, which indicates that all calibration steps are performed. The only valid value for PXIe-5820/5830/5831/5832/5840/5841/5842/5860 is an empty array.Name (Value)DescriptionPreselector Alignment (1)Omits the Preselector Alignment step. If you omit this step and the niRFSA Is Self Cal Valid function indicates the calibration data for this step is invalid, the preselector alignment specifications are not guaranteed. This step applies only to the PXIe-5605/5606.Gain Reference (2)Omits the Gain Reference step. If you omit this step and the niRFSA Is Self Cal Valid function indicates the calibration data for this step is invalid, the absolute accuracy of the device is not guaranteed.IF Flatness (4)Omits the IF Flatness step. If you omit this step and the niRFSA Is Self Cal, valid function indicates the calibration data for this step is invalid, the IF flatness specifications are not guaranteed.Digitizer Self Cal (8)Omits the Digitizer Self Cal step. If you omit this step and the niRFSA Is Self Cal Valid function indicates the calibration data for this step is invalid, the absolute accuracy of the device is not guaranteed.LO Self Cal (10)Omits the LO Self Cal step. If you omit this step and the niRFSA Is Self Cal Valid function indicates the calibration data for this step is invalid, the LO PLL may fail to lock.Amplitude Accuracy (20)Not used by this function.Residual LO Power (40)Not used by this function.Image Suppression (80)Not used by this function.Synthesizer Alignment (100)Not used by this function.DC Offset (200)Not used by this function. |
| Name (Value) | Description |  |  |
| Preselector Alignment (1) | Omits the Preselector Alignment step. If you omit this step and the niRFSA Is Self Cal Valid function indicates the calibration data for this step is invalid, the preselector alignment specifications are not guaranteed. This step applies only to the PXIe-5605/5606. |  |  |
| Gain Reference (2) | Omits the Gain Reference step. If you omit this step and the niRFSA Is Self Cal Valid function indicates the calibration data for this step is invalid, the absolute accuracy of the device is not guaranteed. |  |  |
| IF Flatness (4) | Omits the IF Flatness step. If you omit this step and the niRFSA Is Self Cal, valid function indicates the calibration data for this step is invalid, the IF flatness specifications are not guaranteed. |  |  |
| Digitizer Self Cal (8) | Omits the Digitizer Self Cal step. If you omit this step and the niRFSA Is Self Cal Valid function indicates the calibration data for this step is invalid, the absolute accuracy of the device is not guaranteed. |  |  |
| LO Self Cal (10) | Omits the LO Self Cal step. If you omit this step and the niRFSA Is Self Cal Valid function indicates the calibration data for this step is invalid, the LO PLL may fail to lock. |  |  |
| Amplitude Accuracy (20) | Not used by this function. |  |  |
| Residual LO Power (40) | Not used by this function. |  |  |
| Image Suppression (80) | Not used by this function. |  |  |
| Synthesizer Alignment (100) | Not used by this function. |  |  |
| DC Offset (200) | Not used by this function. |  |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxInstr_GetError](group____root__ni_r_fmx_instr__functions_1ga3c9efe926e0a627b12a3ba6c33e22657.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Calibration

<!--NI_TOPIC bundle=rfmxinstr-c-api-ref path=group____root__ni_r_fmx_instr__functions__calibration_1ga605d7591dd0998e708da83f54b928bb1.html language=enus -->
## TOPIC 00057: RFmxInstr_SelfCalibrateRange

- bundle_id: `rfmxinstr-c-api-ref`
- source_path: `group____root__ni_r_fmx_instr__functions__calibration_1ga605d7591dd0998e708da83f54b928bb1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_instr__functions__calibration_1ga605d7591dd0998e708da83f54b928bb1.html
- document_id: `rfmxinstr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Self-calibrates all configurations within the specified frequency and reference level limits. If there is an open session for NI-RFSG for your device, it may remain open but cannot be used while this function runs. NI recommends that no external signals are present on the RF In port while the calibr

### RFmxInstr_SelfCalibrateRange

Self-calibrates all configurations within the specified frequency and reference level limits. If there is an open session for NI-RFSG for your device, it may remain open but cannot be used while this function runs. NI recommends that no external signals are present on the RF In port while the calibration is taking place. For more information about Self Calibrate Range, refer to the *niRFSA Self Calibrate Range* function topic for your device in the *NI RF Vector Signal Analyzers Help*. On a MIMO session, this function self-calibrates all NI-RFSA devices and associated modules that support self-calibration.

#### Syntax

int32 __stdcall RFmxInstr_SelfCalibrateRange(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 stepsToOmit, float64 minimumFrequency, float64 maximumFrequency, float64 minimumReferenceLevel, float64 maximumReferenceLevel)

#### Remarks

Supported devices:

Note

This function does not update self-calibration date and temperature. Self-calibration range data is not saved to your device if you restart the system.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter identifies the instrument session. This parameter is obtained from the RFmxInstr_Initialize function or the RFmxInstr_InitializeFromNIRFSASessionArray function. |
| selectorString | [in] | char[] | Specifies a selector string. Pass an empty string. |
| stepsToOmit | [in] | int32 | This parameter specifies which calibration steps to skip during the self-calibration process. The default value is an empty array, which indicates that all calibration steps are performed. The only valid value for the PXIe-5820/5830/5831/5832/5840/5841/5842 is an empty array.Name (Value)DescriptionPreselector Alignment (1)Not used by this function.Gain Reference (2)Not used by this function.IF Flatness (4)Not used by this function.Digitizer Self Cal (8)Not used by this function.LO Self Cal (10)Omits the LO Self Cal step. If you omit this step and the niRFSA Is Self Cal Valid function indicates the calibration data for this step is invalid, the LO PLL may fail to lock.Amplitude Accuracy (20)Omits the Amplitude Accuracy step. If you omit this step, the absolute accuracy ofthe device is not adjusted.Residual LO Power (40)Omits the Residual LO Power step. If you omit this step, the Residual LO Powerperformance is not adjusted.Image Suppression (80)Omits the Image Suppression step. If you omit this step, the Residual SidebandImage performance is not adjusted.Synthesizer Alignment (100)Omits the VCO Alignment step. If you omit this step, the LO PLL will not getadjusted.DC Offset (200)Omits the DC Offset step. |
| Name (Value) | Description |  |  |
| Preselector Alignment (1) | Not used by this function. |  |  |
| Gain Reference (2) | Not used by this function. |  |  |
| IF Flatness (4) | Not used by this function. |  |  |
| Digitizer Self Cal (8) | Not used by this function. |  |  |
| LO Self Cal (10) | Omits the LO Self Cal step. If you omit this step and the niRFSA Is Self Cal Valid function indicates the calibration data for this step is invalid, the LO PLL may fail to lock. |  |  |
| Amplitude Accuracy (20) | Omits the Amplitude Accuracy step. If you omit this step, the absolute accuracy ofthe device is not adjusted. |  |  |
| Residual LO Power (40) | Omits the Residual LO Power step. If you omit this step, the Residual LO Powerperformance is not adjusted. |  |  |
| Image Suppression (80) | Omits the Image Suppression step. If you omit this step, the Residual SidebandImage performance is not adjusted. |  |  |
| Synthesizer Alignment (100) | Omits the VCO Alignment step. If you omit this step, the LO PLL will not getadjusted. |  |  |
| DC Offset (200) | Omits the DC Offset step. |  |  |
| minimumFrequency | [in] | float64 | This parameter specifies the minimum frequency for the custom self calibration range. This value is expressed in Hz. Note For PXIe-5830/5831/5832, only the applicable ports within the specified frequency range are calibrated. |
| maximumFrequency | [in] | float64 | This parameter specifies the maximum frequency for the custom self calibration range. This value is expressed in Hz. |
| minimumReferenceLevel | [in] | float64 | This parameter specifies the minimum reference level for the custom self calibration range. This value is expressed in dBm. |
| maximumReferenceLevel | [in] | float64 | This parameter specifies the maximum reference level for the custom self calibration range. This value is expressed dBm. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxInstr_GetError](group____root__ni_r_fmx_instr__functions_1ga3c9efe926e0a627b12a3ba6c33e22657.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Calibration

<!--NI_TOPIC bundle=rfmxinstr-c-api-ref path=group____root__ni_r_fmx_instr__functions__calibration__utility.html language=enus -->
## TOPIC 00058: Utility

- bundle_id: `rfmxinstr-c-api-ref`
- source_path: `group____root__ni_r_fmx_instr__functions__calibration__utility.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_instr__functions__calibration__utility.html
- document_id: `rfmxinstr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxInstr_GetSelfCalibrateLastDateAndTimeReturns the date and time of the last successful self-calibration. On a MIMO session, use the Selector String parameter to get the last successful self-calibration date and time for a specific MIMO port. RFmxInstr_GetSelf

### Utility

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxInstr_GetSelfCalibrateLastDateAndTime | Returns the date and time of the last successful self-calibration. On a MIMO session, use the Selector String parameter to get the last successful self-calibration date and time for a specific MIMO port. |
| RFmxInstr_GetSelfCalibrateLastTemperature | Returns the temperature at the last successful self-calibration. On a MIMO session, use the Selector String parameter to get the last successful self-calibration temperature for a specific MIMO port. |

#### Attachments

None

Parent topic:

Calibration

<!--NI_TOPIC bundle=rfmxinstr-c-api-ref path=group____root__ni_r_fmx_instr__functions__calibration__utility_1ga932a2130b1b455bd593a963c3f72f47b.html language=enus -->
## TOPIC 00059: RFmxInstr_GetSelfCalibrateLastTemperature

- bundle_id: `rfmxinstr-c-api-ref`
- source_path: `group____root__ni_r_fmx_instr__functions__calibration__utility_1ga932a2130b1b455bd593a963c3f72f47b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_instr__functions__calibration__utility_1ga932a2130b1b455bd593a963c3f72f47b.html
- document_id: `rfmxinstr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the temperature at the last successful self-calibration. On a MIMO session, use the Selector String parameter to get the last successful self-calibration temperature for a specific MIMO port. Syntaxint32 __stdcall RFmxInstr_GetSelfCalibrateLastTemperature(niRFmxInstrHandle instrumentHandle,

### RFmxInstr_GetSelfCalibrateLastTemperature

Returns the temperature at the last successful self-calibration. On a MIMO session, use the **Selector String** parameter to get the last successful self-calibration temperature for a specific MIMO port.

#### Syntax

int32 __stdcall RFmxInstr_GetSelfCalibrateLastTemperature(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 *temperature, int64 selfCalibrateStep)

#### Remarks

**Supported Devices:** PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831 (IF only)/5832 (IF only)/5840/5841/5842/5860

Note

For PXIe-5644/5645/5646 devices, you must select **Image Suppression** for the **Self Calibrate Step** parameter.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter identifies the instrument session. This parameter is obtained from the RFmxInstr_Initialize function or the RFmxInstr_InitializeFromNIRFSASessionArray function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of a MIMO port on a MIMO session. The default value is "" (empty string).Example:"""port::myrfsa1/0"You can use the RFmxInstr Build Port String function to build the selector string. |
| temperature | [out] | float64 * | This parameter returns the temperature at the last self-calibration. This value is expressed in degree Celsius. |
| selfCalibrateStep | [in] | int64 | This parameter specifies the self-calibration step to query for the last successful self-calibration temperature data. The default value is Preselector Alignment.Name (Value)DescriptionPreselector Alignment (1)Selects the Preselector Alignment self-calibration step.Gain Reference (2)Selects the Gain Reference self-calibration step.IF Flatness (4)Selects the IF Flatness self-calibration step.Digitizer Self Cal (8)Selects the Digitizer Self Cal self-calibration step.LO Self Cal (10)Selects the LO Self Cal self-calibration step.Amplitude Accuracy (20)Selects the Amplitude Accuracy self-calibration step.Residual LO Power (40)Selects the Residual LO Power self-calibration step.Image Suppression (80)Selects the Image Suppression self-calibration step.Synthesizer Alignment (100)Selects the Synthesizer Alignment self-calibration step.DC Offset (200)Selects the DC Offset self-calibration step. |
| Name (Value) | Description |  |  |
| Preselector Alignment (1) | Selects the Preselector Alignment self-calibration step. |  |  |
| Gain Reference (2) | Selects the Gain Reference self-calibration step. |  |  |
| IF Flatness (4) | Selects the IF Flatness self-calibration step. |  |  |
| Digitizer Self Cal (8) | Selects the Digitizer Self Cal self-calibration step. |  |  |
| LO Self Cal (10) | Selects the LO Self Cal self-calibration step. |  |  |
| Amplitude Accuracy (20) | Selects the Amplitude Accuracy self-calibration step. |  |  |
| Residual LO Power (40) | Selects the Residual LO Power self-calibration step. |  |  |
| Image Suppression (80) | Selects the Image Suppression self-calibration step. |  |  |
| Synthesizer Alignment (100) | Selects the Synthesizer Alignment self-calibration step. |  |  |
| DC Offset (200) | Selects the DC Offset self-calibration step. |  |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxInstr_GetError](group____root__ni_r_fmx_instr__functions_1ga3c9efe926e0a627b12a3ba6c33e22657.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfmxinstr-c-api-ref path=group____root__ni_r_fmx_instr__functions__configuration.html language=enus -->
## TOPIC 00060: Configuration

- bundle_id: `rfmxinstr-c-api-ref`
- source_path: `group____root__ni_r_fmx_instr__functions__configuration.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_instr__functions__configuration.html
- document_id: `rfmxinstr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsExternalattntableSend Software Edge TriggerGroup membersNameDescriptionRFmxInstr_CfgFrequencyReferenceConfigures the Reference Clock and the frequency reference source. RFmxInstr_CfgMechanicalAttenuationConfigures the mechanical attenuation and the RFmx driver attenuation hardware settings. RF

### Configuration

#### Groups

- Externalattntable
- Send Software Edge Trigger

#### Group members

| Name | Description |
| --- | --- |
| RFmxInstr_CfgFrequencyReference | Configures the Reference Clock and the frequency reference source. |
| RFmxInstr_CfgMechanicalAttenuation | Configures the mechanical attenuation and the RFmx driver attenuation hardware settings. |
| RFmxInstr_CfgRFAttenuation | Configures the nominal attenuation and the RFmx driver setting. |
| RFmxInstr_ExportSignal | Routes signals (triggers, clocks, and events) to the specified output terminal. |

#### Attachments

None

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxinstr-c-api-ref path=group____root__ni_r_fmx_instr__functions__configuration__externalattntable.html language=enus -->
## TOPIC 00061: Externalattntable

- bundle_id: `rfmxinstr-c-api-ref`
- source_path: `group____root__ni_r_fmx_instr__functions__configuration__externalattntable.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_instr__functions__configuration__externalattntable.html
- document_id: `rfmxinstr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsExternal Attenuation InterpolationGroup membersNameDescriptionRFmxInstr_CfgExternalAttenuationTableStores the external attenuation table in the calibration plane specified by the Selector String parameter. On a MIMO session, the external attenuation table is stored for each MIMO port in the sp

### Externalattntable

#### Groups

- External Attenuation Interpolation

#### Group members

| Name | Description |
| --- | --- |
| RFmxInstr_CfgExternalAttenuationTable | Stores the external attenuation table in the calibration plane specified by the Selector String parameter. On a MIMO session, the external attenuation table is stored for each MIMO port in the specified calibration plane. |
| RFmxInstr_CfgSParameterExternalAttenuationTable | Stores the S-parameter table in the calibration plane specified by the Selector String parameter. On a MIMO session, the S-parameter table is stored for each MIMO port in the specified calibration plane. |
| RFmxInstr_CfgSParameterExternalAttenuationTableSplit | Stores the S-parameter table in the calibration plane specified by the Selector String parameter. On a MIMO session, the S-parameter table is stored for each MIMO port in the specified calibration plane. |
| RFmxInstr_CfgSParameterExternalAttenuationType | Configures the type of S-parameter to apply to measurements on the specified port for a Calplane. You can use the Selector String input to specify the name of the Calplane and port to configure for S-parameter. |
| RFmxInstr_DeleteAllExternalAttenuationTables | Deletes all the external attenuation tables in the calibration plane specified by the Selector String parameter. On a MIMO session, this function deletes all the external attenuation tables for the specified MIMO port. |
| RFmxInstr_DeleteExternalAttenuationTable | Deletes the external attenuation table set by the Table Name parameter in the calibration plane specified by the Selector String parameter. On a MIMO session, this function deletes the external attenuation table for the specified MIMO port. |
| RFmxInstr_DisableCalibrationPlane | Disables the calibration plane specified by the Selector String parameter for amplitude correction. |
| RFmxInstr_EnableCalibrationPlane | Enables the calibration plane specified by the Selector String parameter for amplitude correction. |
| RFmxInstr_GetExternalAttenuationTableActualValue | Returns the external attenuation table actual value that is applied to the measurements for a specified signal and calibration plane. |
| RFmxInstr_GetSParameterExternalAttenuationType | Returns the type of S-parameter that is applied to the measurements on the specified port on a Calplane. You can use the Selector String input to specify the name of the Calplane and port to configure for S-parameter. |
| RFmxInstr_LoadSParameterExternalAttenuationTableFromS2PFile | Stores the S-parameter table from the S2P file in the calibration plane specified by the Selector String parameter. S-parameter tables are used for fixture de-embedding. On a MIMO session, the S-parameter table is stored for each MIMO port in the specified calibration plane. |
| RFmxInstr_SelectActiveExternalAttenuationTable | Activates the external attenuation table set by the Table Name parameter in the calibration plane specified by the Selector String parameter. On a MIMO session, this function selects the active external attenuation table for the specified MIMO port. The specified table will be used for amplitude correction during measurement. |

#### Attachments

None

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxinstr-c-api-ref path=group____root__ni_r_fmx_instr__functions__configuration__externalattntable_1ga084bc4ab0abf606ece87589ddf496f6e.html language=enus -->
## TOPIC 00062: RFmxInstr_GetSParameterExternalAttenuationType

- bundle_id: `rfmxinstr-c-api-ref`
- source_path: `group____root__ni_r_fmx_instr__functions__configuration__externalattntable_1ga084bc4ab0abf606ece87589ddf496f6e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_instr__functions__configuration__externalattntable_1ga084bc4ab0abf606ece87589ddf496f6e.html
- document_id: `rfmxinstr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the type of S-parameter that is applied to the measurements on the specified port on a Calplane. You can use the Selector String input to specify the name of the Calplane and port to configure for S-parameter. Syntaxint32 __stdcall RFmxInstr_GetSParameterExternalAttenuationType(niRFmxInstrHa

### RFmxInstr_GetSParameterExternalAttenuationType

Returns the type of S-parameter that is applied to the measurements on the specified port on a Calplane. You can use the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) input to specify the name of the Calplane and port to configure for S-parameter.

#### Syntax

int32 __stdcall RFmxInstr_GetSParameterExternalAttenuationType(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 *sParameterType)

#### Remarks

**Supported devices**: PXIe-5830/5831/5832/5840/5841/5842/5860

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter identifies the instrument session. This parameter is obtained from the RFmxInstr_Initialize function or the RFmxInstr_InitializeFromNIRFSASessionArray function. |
| selectorString | [in] | char[] | This parameter specifies the calibration plane name in which either S-parameter or external attenuation table is stored. This input accepts the calibration plane name with the "calplane::" prefix. If you do not specify the calibration plane name, the default calibration plane instance is used. The default value is "" (empty string).On a MIMO session if you do not specify the port name, this function will return an error. To get S-parameter external attenuation type from a specific MIMO port, use the port specifier with or without the calplane name. Example: "calplane::plane1/port::myrfsa1/0".Note For PXIe-5830/5831/5832 devices, port names should also be specified along with Calplane names. Hence, the valid selector string is "calplane::<calplaneName>/port::<portName>". For a MIMO port, the valid selector string is "calplane::<calplaneName>/port::<deviceName>/<channelNumber>/<portName>". Use RFmxInstr_GetAvailablePorts function to get the valid port names.Example:"""calplane::plane0""calplane::plane0/port::if0""port::if0""calplane::plane0/port::myrfsa1/0""calplane::plane0/port::myrfsa1/0/if0" |
| sParameterType | [out] | int32 * | This parameter returns the type of S-parameter which is applied to measurements on the specified port of a Calplane. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxInstr_GetError](group____root__ni_r_fmx_instr__functions_1ga3c9efe926e0a627b12a3ba6c33e22657.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Externalattntable

<!--NI_TOPIC bundle=rfmxinstr-c-api-ref path=group____root__ni_r_fmx_instr__functions__configuration__externalattntable_1ga4748205e9762ba357e9edda33a6e65ff.html language=enus -->
## TOPIC 00063: RFmxInstr_SelectActiveExternalAttenuationTable

- bundle_id: `rfmxinstr-c-api-ref`
- source_path: `group____root__ni_r_fmx_instr__functions__configuration__externalattntable_1ga4748205e9762ba357e9edda33a6e65ff.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_instr__functions__configuration__externalattntable_1ga4748205e9762ba357e9edda33a6e65ff.html
- document_id: `rfmxinstr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Activates the external attenuation table set by the Table Name parameter in the calibration plane specified by the Selector String parameter. On a MIMO session, this function selects the active external attenuation table for the specified MIMO port. The specified table will be used for amplitude cor

### RFmxInstr_SelectActiveExternalAttenuationTable

Activates the external attenuation table set by the **Table Name** parameter in the calibration plane specified by the **Selector String** parameter. On a MIMO session, this function selects the active external attenuation table for the specified MIMO port. The specified table will be used for amplitude correction during measurement.

#### Syntax

int32 __stdcall RFmxInstr_SelectActiveExternalAttenuationTable(niRFmxInstrHandle instrumentHandle, char selectorString[], char tableName)

#### Remarks

**Supported devices**: PXIe-5663/5663E, PXIe-5665, PXIe-5668, PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842/5860

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter identifies the instrument session. This parameter is obtained from the RFmxInstr_Initialize function or the RFmxInstr_InitializeFromNIRFSASessionArray function. |
| selectorString | [in] | char[] | This parameter specifies the calibration plane name in which either S-parameter or external attenuation table is stored. This input accepts the calibration plane name with the "calplane::" prefix. If you do not specify the calibration plane name, the default calibration plane instance is used. The default value is "" (empty string).On a MIMO session, the default "" (empty string) selects the active external attenuation table for all the MIMO Ports. To configure external attenuation type for a specific MIMO port, use the port specifier with or without the calplane name. Example: "calplane::plane1/port::myrfsa1/0".Note For PXIe-5830/5831/5832 devices, port names should also be specified along with Calplane names. Hence, the valid selector string is "calplane::<calplaneName>/port::<portName>". If you specify "port::all", all ports are considered configured. For a MIMO port, the valid selector string is "calplane::<calplaneName>/port::<deviceName>/<channelNumber>/<portName>". If you specify "port::all", all ports are considered configured. Use RFmxInstr_GetAvailablePorts function to get the valid port names.Example:"""calplane::plane0""calplane::plane0/port::if0""port::if0""calplane::plane0/port::all""calplane::plane0/port::myrfsa1/0""calplane::plane0/port::myrfsa1/0, port::myrfsa2/0""calplane::plane0/port::myrfsa1/0/if0" |
| tableName | [in] | char | This parameter specifies the name to be associated with external attenuation table within a calibration plane. Provide a unique name, such as "table1" to configure the table. The default value is "" (empty string).Example:"""table1" |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxInstr_GetError](group____root__ni_r_fmx_instr__functions_1ga3c9efe926e0a627b12a3ba6c33e22657.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Externalattntable

<!--NI_TOPIC bundle=rfmxinstr-c-api-ref path=group____root__ni_r_fmx_instr__functions__configuration__externalattntable_1ga4e135e6c348922b7c1471ebf467ee8df.html language=enus -->
## TOPIC 00064: RFmxInstr_DeleteAllExternalAttenuationTables

- bundle_id: `rfmxinstr-c-api-ref`
- source_path: `group____root__ni_r_fmx_instr__functions__configuration__externalattntable_1ga4e135e6c348922b7c1471ebf467ee8df.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_instr__functions__configuration__externalattntable_1ga4e135e6c348922b7c1471ebf467ee8df.html
- document_id: `rfmxinstr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Deletes all the external attenuation tables in the calibration plane specified by the Selector String parameter. On a MIMO session, this function deletes all the external attenuation tables for the specified MIMO port. Syntaxint32 __stdcall RFmxInstr_DeleteAllExternalAttenuationTables(niRFmxInstrHan

### RFmxInstr_DeleteAllExternalAttenuationTables

Deletes all the external attenuation tables in the calibration plane specified by the **Selector String** parameter. On a MIMO session, this function deletes all the external attenuation tables for the specified MIMO port.

#### Syntax

int32 __stdcall RFmxInstr_DeleteAllExternalAttenuationTables(niRFmxInstrHandle instrumentHandle, char selectorString[])

#### Remarks

**Supported devices**: PXIe-5663/5663E, PXIe-5665, PXIe-5668, PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842/5860

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter identifies the instrument session. This parameter is obtained from the RFmxInstr_Initialize function or the RFmxInstr_InitializeFromNIRFSASessionArray function. |
| selectorString | [in] | char[] | This parameter specifies the calibration plane name in which either S-parameter or external attenuation table is stored. This input accepts the calibration plane name with the "calplane::" prefix. If you do not specify the calibration plane name, the default calibration plane instance is used. The default value is "" (empty string). If you specify "calplane::all", all the calibration planes are deleted.On a MIMO session, the default "" (empty string) deletes all the external attenuation tables for all MIMO Ports. To delete an external attenuation type for a specific MIMO port, use the port specifier with or without the calplane name. Example: "calplane::plane1/port::myrfsa1/0".Note For PXIe-5830/5831/5832 devices, port names should also be specified along with Calplane names. Hence, the valid selector string is "calplane::<calplaneName>/port::<portName>". If you specify "port::all", all ports are considered configured. For a MIMO port, the valid selector string is "calplane::<calplaneName>/port::<deviceName>/<channelNumber>/<portName>". If you specify "port::all", all MIMO ports are considered configured. Use RFmxInstr_GetAvailablePorts function to get the valid port names.Example:"""calplane::plane0""calplane::all""calplane::plane0/port::if0""port::if0""calplane::plane0/port::all""calplane::all/port::all""calplane::plane0/port::myrfsa1/0""calplane::plane0/port::myrfsa1/0, port::myrfsa2/0""calplane::plane0/port::myrfsa1/0/if0" |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxInstr_GetError](group____root__ni_r_fmx_instr__functions_1ga3c9efe926e0a627b12a3ba6c33e22657.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Externalattntable

<!--NI_TOPIC bundle=rfmxinstr-c-api-ref path=group____root__ni_r_fmx_instr__functions__configuration__externalattntable_1ga5f53d7bd6b717ad8452443b1951cbd84.html language=enus -->
## TOPIC 00065: RFmxInstr_CfgSParameterExternalAttenuationType

- bundle_id: `rfmxinstr-c-api-ref`
- source_path: `group____root__ni_r_fmx_instr__functions__configuration__externalattntable_1ga5f53d7bd6b717ad8452443b1951cbd84.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_instr__functions__configuration__externalattntable_1ga5f53d7bd6b717ad8452443b1951cbd84.html
- document_id: `rfmxinstr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the type of S-parameter to apply to measurements on the specified port for a Calplane. You can use the Selector String input to specify the name of the Calplane and port to configure for S-parameter. Syntaxint32 __stdcall RFmxInstr_CfgSParameterExternalAttenuationType(niRFmxInstrHandle in

### RFmxInstr_CfgSParameterExternalAttenuationType

Configures the type of S-parameter to apply to measurements on the specified port for a Calplane. You can use the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) input to specify the name of the Calplane and port to configure for S-parameter.

#### Syntax

int32 __stdcall RFmxInstr_CfgSParameterExternalAttenuationType(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 sParameterType)

#### Remarks

**Supported devices**: PXIe-5830/5831/5832/5840/5841/5842/5860

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter identifies the instrument session. This parameter is obtained from the RFmxInstr_Initialize function or the RFmxInstr_InitializeFromNIRFSASessionArray function. |
| selectorString | [in] | char[] | This parameter specifies the calibration plane name in which either S-parameter or external attenuation table is stored. This input accepts the calibration plane name with the "calplane::" prefix. If you do not specify the calibration plane name, the default calibration plane instance is used. The default value is "" (empty string).On a MIMO session if you do not specify the port name, this configuration is applied to all MIMO ports in the session for the default calibration plane instance. To configure S-parameter external attenuation type for a specific MIMO port, use the port specifier with or without the calplane name. Example: "calplane::plane1/port::myrfsa1/0".Note For PXIe-5830/5831/5832 devices, port names should also be specified along with Calplane names. Hence, the valid selector string is "calplane::<calplaneName>/port::<portName>". If you specify "port::all", all ports are considered configured. Use RFmxInstr_GetAvailablePorts function to get the valid port names. For a MIMO port, the valid selector string is "calplane::<calplaneName>/port::<deviceName>/<channelNumber>/<portName>". If you specify "port::all", all MIMO ports are considered configured. Example:"""calplane::plane0""calplane::plane0/port::if0""port::if0""calplane::plane0/port::all""calplane::plane0/port::myrfsa1/0""calplane::plane0/port::myrfsa1/0, port::myrfsa2/0""calplane::plane0/port::myrfsa1/0/if0" |
| sParameterType | [in] | int32 | This parameter specifies the type of S-parameter which applies to measurements on the specified port for a Calplane. If you set this parameter to Scalar or Vector, RFmx adjusts the instrument settings and the returned data to remove the effects of the external network between the instrument and the DUT.PXIe-5831/5832: Valid values for this parameter are Scalar and Vector. Vector is only supported for TRX ports in a semiconductor test system (STS).PXIe-5840/5841/5842/5860: The only valid value for this parameter is Scalar.The default value is Scalar.Name (Value)DescriptionScalar (1)De-embeds the measurement using the gain term.Vector (2)De-embeds the measurement using the gain term and the reflection term. |
| Name (Value) | Description |  |  |
| Scalar (1) | De-embeds the measurement using the gain term. |  |  |
| Vector (2) | De-embeds the measurement using the gain term and the reflection term. |  |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxInstr_GetError](group____root__ni_r_fmx_instr__functions_1ga3c9efe926e0a627b12a3ba6c33e22657.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Externalattntable

<!--NI_TOPIC bundle=rfmxinstr-c-api-ref path=group____root__ni_r_fmx_instr__functions__configuration__externalattntable_1ga88c866daf6e986cea006e11832dc717d.html language=enus -->
## TOPIC 00066: RFmxInstr_GetExternalAttenuationTableActualValue

- bundle_id: `rfmxinstr-c-api-ref`
- source_path: `group____root__ni_r_fmx_instr__functions__configuration__externalattntable_1ga88c866daf6e986cea006e11832dc717d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_instr__functions__configuration__externalattntable_1ga88c866daf6e986cea006e11832dc717d.html
- document_id: `rfmxinstr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the external attenuation table actual value that is applied to the measurements for a specified signal and calibration plane. Syntaxint32 __stdcall RFmxInstr_GetExternalAttenuationTableActualValue(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 *externalAttenuation)Remarks

### RFmxInstr_GetExternalAttenuationTableActualValue

Returns the external attenuation table actual value that is applied to the measurements for a specified signal and calibration plane.

#### Syntax

int32 __stdcall RFmxInstr_GetExternalAttenuationTableActualValue(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 *externalAttenuation)

#### Remarks

On a MIMO session, this function returns the external attenuation table actual value for a specified port. You can use the **Selector String** parameter to specify the name of the signal, calibration plane, and MIMO port to return the external attenuation table actual value.

**Supported devices**: PXIe-5663/5663E, PXIe-5665, PXIe-5668, PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842/5860

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter identifies the instrument session. This parameter is obtained from the RFmxInstr_Initialize function or the RFmxInstr_InitializeFromNIRFSASessionArray function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and calibration plane name. This input accepts the calibration plane name with the "calplane::" prefix. If you do not specify the calibration plane name, the default calibration plane instance is used. The default value is "" (empty string). On a MIMO session, you must use "port::<deviceName>/<channelNumber>" as part of the selector string to read the external attenuation table actual value for the specified port. If you do not specify the signal name, the value is returned for the last committed signal instance.Example:"""signal::sig1""calplane::plane0""signal::sig1/calplane::plane0""port::rfsa1/0""signal::sig1/port::rfsa1/0""calplane::plane0/port::rfsa1/0""signal::sig1/calplane::plane0/port::rfsa1/0" |
| externalAttenuation | [out] | float64 * | This parameter returns the external attenuation table actual value applied to the measurements for a specified signal and calibration plane. This further includes interpolation of the external attenuation table based on the specified signal. On a MIMO session, this value corresponds to a specified port. This value is expressed in dB. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxInstr_GetError](group____root__ni_r_fmx_instr__functions_1ga3c9efe926e0a627b12a3ba6c33e22657.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Externalattntable

<!--NI_TOPIC bundle=rfmxinstr-c-api-ref path=group____root__ni_r_fmx_instr__functions__configuration__externalattntable_1gaa1f3dcd73cecc6fc02def213cb336847.html language=enus -->
## TOPIC 00067: RFmxInstr_DisableCalibrationPlane

- bundle_id: `rfmxinstr-c-api-ref`
- source_path: `group____root__ni_r_fmx_instr__functions__configuration__externalattntable_1gaa1f3dcd73cecc6fc02def213cb336847.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_instr__functions__configuration__externalattntable_1gaa1f3dcd73cecc6fc02def213cb336847.html
- document_id: `rfmxinstr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Disables the calibration plane specified by the Selector String parameter for amplitude correction. Syntaxint32 __stdcall RFmxInstr_DisableCalibrationPlane(niRFmxInstrHandle instrumentHandle, char selectorString[])RemarksSupported devices: PXIe-5663/5663E, PXIe-5665, PXIe-5668, PXIe-5644/5645/5646,

### RFmxInstr_DisableCalibrationPlane

Disables the calibration plane specified by the **Selector String** parameter for amplitude correction.

#### Syntax

int32 __stdcall RFmxInstr_DisableCalibrationPlane(niRFmxInstrHandle instrumentHandle, char selectorString[])

#### Remarks

**Supported devices**: PXIe-5663/5663E, PXIe-5665, PXIe-5668, PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842/5860

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter identifies the instrument session. This parameter is obtained from the RFmxInstr_Initialize function or the RFmxInstr_InitializeFromNIRFSASessionArray function. |
| selectorString | [in] | char[] | This parameter specifies the calibration plane name in which the external attenuation table is stored. This input accepts the calibration plane name with the "calplane::" prefix. If you do not specify the calibration plane name, the default calibration plane instance is used. The default value is "" (empty string). If you specify "calplane::all", all the calibration planes are disabled.Example:"""calplane::plane0""calplane::all" |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxInstr_GetError](group____root__ni_r_fmx_instr__functions_1ga3c9efe926e0a627b12a3ba6c33e22657.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Externalattntable

<!--NI_TOPIC bundle=rfmxinstr-c-api-ref path=group____root__ni_r_fmx_instr__functions__configuration__externalattntable_1gabe564a278922e17e36eb986f7b0d9d3e.html language=enus -->
## TOPIC 00068: RFmxInstr_LoadSParameterExternalAttenuationTableFromS2PFile

- bundle_id: `rfmxinstr-c-api-ref`
- source_path: `group____root__ni_r_fmx_instr__functions__configuration__externalattntable_1gabe564a278922e17e36eb986f7b0d9d3e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_instr__functions__configuration__externalattntable_1gabe564a278922e17e36eb986f7b0d9d3e.html
- document_id: `rfmxinstr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Stores the S-parameter table from the S2P file in the calibration plane specified by the Selector String parameter. S-parameter tables are used for fixture de-embedding. On a MIMO session, the S-parameter table is stored for each MIMO port in the specified calibration plane. Syntaxint32 __stdcall RF

### RFmxInstr_LoadSParameterExternalAttenuationTableFromS2PFile

Stores the S-parameter table from the S2P file in the calibration plane specified by the **Selector String** parameter. S-parameter tables are used for fixture de-embedding. On a MIMO session, the S-parameter table is stored for each MIMO port in the specified calibration plane.

#### Syntax

int32 __stdcall RFmxInstr_LoadSParameterExternalAttenuationTableFromS2PFile(niRFmxInstrHandle instrumentHandle, char selectorString[], char tableName, char s2PFilePath, int32 sParameterOrientation)

#### Remarks

Note

If there is only one table configured in any calibration plane, it is automatically selected as the active table.

**Supported devices**: PXIe-5830/5831/5832/5840/5841/5842/5860

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter identifies the instrument session. This parameter is obtained from the RFmxInstr_Initialize function or the RFmxInstr_InitializeFromNIRFSASessionArray function. |
| selectorString | [in] | char[] | This parameter specifies the calibration plane name in which the external attenuation table is stored. This input accepts the calibration plane name with the "calplane::" prefix. If you do not specify the calibration plane name, the default calibration plane instance is used. The default value is "" (empty string). Note For PXIe-5830/5831/5832 devices, port names should also be specified along with Calplane names. Hence, the valid selector string is "calplane::<calplaneName>/port::<portName>". If you specify "port::all", all ports are considered configured. For a MIMO port, the valid selector string is "calplane::<calplaneName>/port::<deviceName>/<channelNumber>/<portName>". If you specify "port::all", all MIMO ports are considered configured. Use RFmxInstr_GetAvailablePorts function to get the valid port names. Example:"""calplane::plane0""calplane::plane0/port::if0""port::if0""calplane::plane0/port::all""calplane::plane0/port::myrfsa1/0""calplane::plane0/port::myrfsa1/0, port::myrfsa2/0""calplane::plane0/port::myrfsa1/0/if0" |
| tableName | [in] | char | This parameter specifies the name to be associated with S-parameter table within a calibration plane. Provide a unique name, such as "table1" to configure the table. The default value is "" (empty string).Example:"""table1" |
| s2PFilePath | [in] | char | This parameter specifies the path to the S2P file that contains S-parameter table information for the specified port. |
| sParameterOrientation | [in] | int32 | This parameter specifies the orientation of the data in the S-parameter table relative to the port you specify. The default value is Port2 Towards DUT.Name (Value)DescriptionPort1 Towards DUT (0)Port 1 of the S2P is oriented towards the DUT.Port2 Towards DUT (1)Port 2 of the S2P is oriented towards the DUT. |
| Name (Value) | Description |  |  |
| Port1 Towards DUT (0) | Port 1 of the S2P is oriented towards the DUT. |  |  |
| Port2 Towards DUT (1) | Port 2 of the S2P is oriented towards the DUT. |  |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxInstr_GetError](group____root__ni_r_fmx_instr__functions_1ga3c9efe926e0a627b12a3ba6c33e22657.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Externalattntable

<!--NI_TOPIC bundle=rfmxinstr-c-api-ref path=group____root__ni_r_fmx_instr__functions__configuration__externalattntable_1gadbd8823d4d340191c4dc3953ced4bcf5.html language=enus -->
## TOPIC 00069: RFmxInstr_DeleteExternalAttenuationTable

- bundle_id: `rfmxinstr-c-api-ref`
- source_path: `group____root__ni_r_fmx_instr__functions__configuration__externalattntable_1gadbd8823d4d340191c4dc3953ced4bcf5.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_instr__functions__configuration__externalattntable_1gadbd8823d4d340191c4dc3953ced4bcf5.html
- document_id: `rfmxinstr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Deletes the external attenuation table set by the Table Name parameter in the calibration plane specified by the Selector String parameter. On a MIMO session, this function deletes the external attenuation table for the specified MIMO port. Syntaxint32 __stdcall RFmxInstr_DeleteExternalAttenuationTa

### RFmxInstr_DeleteExternalAttenuationTable

Deletes the external attenuation table set by the **Table Name** parameter in the calibration plane specified by the **Selector String** parameter. On a MIMO session, this function deletes the external attenuation table for the specified MIMO port.

#### Syntax

int32 __stdcall RFmxInstr_DeleteExternalAttenuationTable(niRFmxInstrHandle instrumentHandle, char selectorString[], char tableName)

#### Remarks

**Supported devices**: PXIe-5663/5663E, PXIe-5665, PXIe-5668, PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842/5860

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter identifies the instrument session. This parameter is obtained from the RFmxInstr_Initialize function or the RFmxInstr_InitializeFromNIRFSASessionArray function. |
| selectorString | [in] | char[] | This parameter specifies the calibration plane name in which the external attenuation table is stored. This input accepts the calibration plane name with the "calplane::" prefix. If you do not specify the calibration plane name, the default calibration plane instance is used. The default value is "" (empty string).On a MIMO session, the default "" (empty string) deletes the active external attenuation table for all the MIMO Ports. To delete an external attenuation type for a specific MIMO port, use the port specifier with or without the calplane name. Example: "calplane::plane1/port::myrfsa1/0".Note For PXIe-5830/5831/5832 devices, port names should also be specified along with Calplane names. Hence, the valid selector string is "calplane::<calplaneName>/port::<portName>". If you specify "port::all", all ports are considered configured. For a MIMO port, the valid selector string is "calplane::<calplaneName>/port::<deviceName>/<channelNumber>/<portName>". If you specify "port::all", all MIMO ports are considered configured. Use RFmxInstr_GetAvailablePorts function to get the valid port names. Example:"""calplane::plane0""calplane::plane0/port::if0""port::if0""calplane::plane0/port::all""calplane::plane0/port::myrfsa1/0""calplane::plane0/port::myrfsa1/0, port::myrfsa2/0""calplane::plane0/port::myrfsa1/0/if0" |
| tableName | [in] | char | This parameter specifies the name to be associated with external attenuation table within a calibration plane. Provide a unique name, such as "table1" to configure the table. The default value is "" (empty string).Example:"""table1" |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxInstr_GetError](group____root__ni_r_fmx_instr__functions_1ga3c9efe926e0a627b12a3ba6c33e22657.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Externalattntable

<!--NI_TOPIC bundle=rfmxinstr-c-api-ref path=group____root__ni_r_fmx_instr__functions__configuration__externalattntable_1gaed39f4ad48d0413270e33072c7b00c1a.html language=enus -->
## TOPIC 00070: RFmxInstr_CfgExternalAttenuationTable

- bundle_id: `rfmxinstr-c-api-ref`
- source_path: `group____root__ni_r_fmx_instr__functions__configuration__externalattntable_1gaed39f4ad48d0413270e33072c7b00c1a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_instr__functions__configuration__externalattntable_1gaed39f4ad48d0413270e33072c7b00c1a.html
- document_id: `rfmxinstr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Stores the external attenuation table in the calibration plane specified by the Selector String parameter. On a MIMO session, the external attenuation table is stored for each MIMO port in the specified calibration plane. Syntaxint32 __stdcall RFmxInstr_CfgExternalAttenuationTable(niRFmxInstrHandle

### RFmxInstr_CfgExternalAttenuationTable

Stores the external attenuation table in the calibration plane specified by the **Selector String** parameter. On a MIMO session, the external attenuation table is stored for each MIMO port in the specified calibration plane.

#### Syntax

int32 __stdcall RFmxInstr_CfgExternalAttenuationTable(niRFmxInstrHandle instrumentHandle, char selectorString[], char tableName, float64 frequency[], float64 externalAttenuation[], int32 arraySize)

#### Remarks

If there is only one table configured in any calibration plane, it is automatically selected as the active table.

**Supported devices**: PXIe-5663/5663E, PXIe-5665, PXIe-5668, PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842/5860

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter identifies the instrument session. This parameter is obtained from the RFmxInstr_Initialize function or the RFmxInstr_InitializeFromNIRFSASessionArray function. |
| selectorString | [in] | char[] | This parameter specifies the calibration plane name in which the external attenuation table is stored. This input accepts the calibration plane name with the "calplane::" prefix. If you do not specify the calibration plane name, the default calibration plane instance is used. The default value is "" (empty string).On a MIMO session if you do not specify the port name, this configuration is applied to all MIMO ports in the session for the default calibration plane instance. To configure external attenuation table for a specific MIMO port, use the port specifier with or without the calplane name. Example: "calplane::plane1/port::myrfsa1/0".Note For PXIe-5830/5831/5832 devices, port names should also be specified along with Calplane names. Hence, the valid selector string is "calplane::<calplaneName>/port::<portName>". If you specify "port::all", all ports are considered configured. For a MIMO port, the valid selector string is "calplane::<calplaneName>/port::<deviceName>/<channelNumber>/<portName>". If you specify "port::all", all MIMO ports are considered configured. Use RFmxInstr_GetAvailablePorts function to get the valid port names.Example:"""calplane::plane0""calplane::plane0/port::if0""port::if0""calplane::plane0/port::all""calplane::plane0/port::myrfsa1/0""calplane::plane0/port::myrfsa1/0, port::myrfsa2/0""calplane::plane0/port::myrfsa1/0/if0" |
| tableName | [in] | char | This parameter specifies the name to be associated with external attenuation table within a calibration plane. Provide a unique name, such as "table1" to configure the table. The default value is "" (empty string).Example:"""table1" |
| frequency | [in] | float64[] | This parameter specifies an array of frequencies in the external attenuation table. This value is expressed in Hz. |
| externalAttenuation | [in] | float64[] | This parameter specifies an array of attenuations corresponding to the frequency specified by the Frequency parameter. This value is expressed in dB. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxInstr_GetError](group____root__ni_r_fmx_instr__functions_1ga3c9efe926e0a627b12a3ba6c33e22657.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Externalattntable

<!--NI_TOPIC bundle=rfmxinstr-c-api-ref path=group____root__ni_r_fmx_instr__functions__configuration__externalattntable_1gaee297adae3daa59779666ccf22b16a68.html language=enus -->
## TOPIC 00071: RFmxInstr_EnableCalibrationPlane

- bundle_id: `rfmxinstr-c-api-ref`
- source_path: `group____root__ni_r_fmx_instr__functions__configuration__externalattntable_1gaee297adae3daa59779666ccf22b16a68.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_instr__functions__configuration__externalattntable_1gaee297adae3daa59779666ccf22b16a68.html
- document_id: `rfmxinstr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enables the calibration plane specified by the Selector String parameter for amplitude correction. Syntaxint32 __stdcall RFmxInstr_EnableCalibrationPlane(niRFmxInstrHandle instrumentHandle, char selectorString[])RemarksSupported devices: PXIe-5663/5663E, PXIe-5665, PXIe-5668, PXIe-5644/5645/5646, PX

### RFmxInstr_EnableCalibrationPlane

Enables the calibration plane specified by the **Selector String** parameter for amplitude correction.

#### Syntax

int32 __stdcall RFmxInstr_EnableCalibrationPlane(niRFmxInstrHandle instrumentHandle, char selectorString[])

#### Remarks

**Supported devices**: PXIe-5663/5663E, PXIe-5665, PXIe-5668, PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842/5860

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter identifies the instrument session. This parameter is obtained from the RFmxInstr_Initialize function or the RFmxInstr_InitializeFromNIRFSASessionArray function. |
| selectorString | [in] | char[] | This parameter specifies the calibration plane name in which the external attenuation table or S-parameter is stored. This input accepts the calibration plane name with the "calplane::" prefix. If you do not specify the calibration plane name, the default calibration plane instance is used. The default value is "" (empty string). If "calplane::all" is specified, all the calibration planes are enabled.Example:"""calplane::plane0""calplane::all" |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxInstr_GetError](group____root__ni_r_fmx_instr__functions_1ga3c9efe926e0a627b12a3ba6c33e22657.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Externalattntable

<!--NI_TOPIC bundle=rfmxinstr-c-api-ref path=group____root__ni_r_fmx_instr__functions__configuration__externalattntable__external__attenuation__interpolation.html language=enus -->
## TOPIC 00072: External Attenuation Interpolation

- bundle_id: `rfmxinstr-c-api-ref`
- source_path: `group____root__ni_r_fmx_instr__functions__configuration__externalattntable__external__attenuation__interpolation.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_instr__functions__configuration__externalattntable__external__attenuation__interpolation.html
- document_id: `rfmxinstr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxInstr_CfgExternalAttenuationInterpolationLinearSelects the linear interpolation method when interpolating S-parameters for the specified table. If the carrier frequency does not match a row in the S-parameter table, this function performs a linear interpolat

### External Attenuation Interpolation

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxInstr_CfgExternalAttenuationInterpolationLinear | Selects the linear interpolation method when interpolating S-parameters for the specified table. If the carrier frequency does not match a row in the S-parameter table, this function performs a linear interpolation based on the entries above and below the row in the table. Note Currently interpolation is supported only for S-parameter tables. |
| RFmxInstr_CfgExternalAttenuationInterpolationNearest | Selects the nearest interpolation method when interpolating S-parameters for a specified table. The parameters of the table nearest to the carrier frequency are used. Note Currently interpolation is supported only for S-parameter tables. |
| RFmxInstr_CfgExternalAttenuationInterpolationSpline | Selects the spline interpolation method when interpolating parameters for the specified table. If the carrier frequency does not match a row in the S-parameter table, this function performs a spline interpolation based on the entries above and below the row in the table. Note Currently interpolation is supported only for S-parameter tables. |

#### Attachments

None

Parent topic:

Externalattntable

<!--NI_TOPIC bundle=rfmxinstr-c-api-ref path=group____root__ni_r_fmx_instr__functions__configuration__externalattntable__external__attenuation__interpolation_1ga8cc68818d1e2cd7d89f1ec9181d63a39.html language=enus -->
## TOPIC 00073: RFmxInstr_CfgExternalAttenuationInterpolationSpline

- bundle_id: `rfmxinstr-c-api-ref`
- source_path: `group____root__ni_r_fmx_instr__functions__configuration__externalattntable__external__attenuation__interpolation_1ga8cc68818d1e2cd7d89f1ec9181d63a39.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_instr__functions__configuration__externalattntable__external__attenuation__interpolation_1ga8cc68818d1e2cd7d89f1ec9181d63a39.html
- document_id: `rfmxinstr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Selects the spline interpolation method when interpolating parameters for the specified table. If the carrier frequency does not match a row in the S-parameter table, this function performs a spline interpolation based on the entries above and below the row in the table. Currently interpolation is s

### RFmxInstr_CfgExternalAttenuationInterpolationSpline

Selects the spline interpolation method when interpolating parameters for the specified table. If the carrier frequency does not match a row in the S-parameter table, this function performs a spline interpolation based on the entries above and below the row in the table.

Note

Currently interpolation is supported only for S-parameter tables.

#### Syntax

int32 __stdcall RFmxInstr_CfgExternalAttenuationInterpolationSpline(niRFmxInstrHandle instrumentHandle, char selectorString[], char tableName)

#### Remarks

**Supported devices**: PXIe-5663/5663E, PXIe-5665, PXIe-5668, PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842/5860

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter identifies the instrument session. This parameter is obtained from the RFmxInstr_Initialize function or the RFmxInstr_InitializeFromNIRFSASessionArray function. |
| selectorString | [in] | char[] | This parameter specifies the calibration plane name in which either S-parameter or external attenuation table is stored. This input accepts the calibration plane name with the "calplane::" prefix. If you do not specify the calibration plane name, the default calibration plane instance is used. The default value is "" (empty string). Note For PXIe-5830/5831/5832 devices, port names should also be specified along with Calplane names. Hence, the valid selector string is "calplane::<calplaneName>/port::<portName>". If you specify "port::all", all ports are considered configured. Use RFmxInstr_GetAvailablePorts function to get the valid port names.Example:"""calplane::plane0""calplane::plane0/port::if0""port::if0""calplane::plane0/port::all" |
| tableName | [in] | char | This parameter specifies the name to be associated with either the S-parameter table or the external attenuation table within a calibration plane. Provide a unique name, such as "table1" to configure the table. The default value is "" (empty string).Example:"""table1" |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxInstr_GetError](group____root__ni_r_fmx_instr__functions_1ga3c9efe926e0a627b12a3ba6c33e22657.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

External Attenuation Interpolation

<!--NI_TOPIC bundle=rfmxinstr-c-api-ref path=group____root__ni_r_fmx_instr__functions__configuration__externalattntable__external__attenuation__interpolation_1ga92ac3c606821d1fc0b45b850f81fb93e.html language=enus -->
## TOPIC 00074: RFmxInstr_CfgExternalAttenuationInterpolationNearest

- bundle_id: `rfmxinstr-c-api-ref`
- source_path: `group____root__ni_r_fmx_instr__functions__configuration__externalattntable__external__attenuation__interpolation_1ga92ac3c606821d1fc0b45b850f81fb93e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_instr__functions__configuration__externalattntable__external__attenuation__interpolation_1ga92ac3c606821d1fc0b45b850f81fb93e.html
- document_id: `rfmxinstr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Selects the nearest interpolation method when interpolating S-parameters for a specified table. The parameters of the table nearest to the carrier frequency are used. Currently interpolation is supported only for S-parameter tables.Syntaxint32 __stdcall RFmxInstr_CfgExternalAttenuationInterpolationN

### RFmxInstr_CfgExternalAttenuationInterpolationNearest

Selects the nearest interpolation method when interpolating S-parameters for a specified table. The parameters of the table nearest to the carrier frequency are used.

Note

Currently interpolation is supported only for S-parameter tables.

#### Syntax

int32 __stdcall RFmxInstr_CfgExternalAttenuationInterpolationNearest(niRFmxInstrHandle instrumentHandle, char selectorString[], char tableName)

#### Remarks

**Supported devices**: PXIe-5663/5663E, PXIe-5665, PXIe-5668, PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842/5860

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter identifies the instrument session. This parameter is obtained from the RFmxInstr_Initialize function or the RFmxInstr_InitializeFromNIRFSASessionArray function. |
| selectorString | [in] | char[] | This parameter specifies the calibration plane name in which either S-parameter or external attenuation table is stored. This input accepts the calibration plane name with the "calplane::" prefix. If you do not specify the calibration plane name, the default calibration plane instance is used. The default value is "" (empty string). Note For PXIe-5830/5831/5832 devices, port names should also be specified along with Calplane names. Hence, the valid selector string is "calplane::<calplaneName>/port::<portName>". If you specify "port::all", all ports are considered configured. Use RFmxInstr_GetAvailablePorts function to get the valid port names.Example:"""calplane::plane0""calplane::plane0/port::if0""port::if0""calplane::plane0/port::all" |
| tableName | [in] | char | This parameter specifies the name to be associated with either the S-parameter table or the external attenuation table within a calibration plane. Provide a unique name, such as "table1" to configure the table. The default value is "" (empty string).Example:"""table1" |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxInstr_GetError](group____root__ni_r_fmx_instr__functions_1ga3c9efe926e0a627b12a3ba6c33e22657.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

External Attenuation Interpolation

<!--NI_TOPIC bundle=rfmxinstr-c-api-ref path=group____root__ni_r_fmx_instr__functions__configuration__externalattntable__external__attenuation__interpolation_1gacd1b9c9a8b06fd83394826724181a5f0.html language=enus -->
## TOPIC 00075: RFmxInstr_CfgExternalAttenuationInterpolationLinear

- bundle_id: `rfmxinstr-c-api-ref`
- source_path: `group____root__ni_r_fmx_instr__functions__configuration__externalattntable__external__attenuation__interpolation_1gacd1b9c9a8b06fd83394826724181a5f0.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_instr__functions__configuration__externalattntable__external__attenuation__interpolation_1gacd1b9c9a8b06fd83394826724181a5f0.html
- document_id: `rfmxinstr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Selects the linear interpolation method when interpolating S-parameters for the specified table. If the carrier frequency does not match a row in the S-parameter table, this function performs a linear interpolation based on the entries above and below the row in the table. Currently interpolation is

### RFmxInstr_CfgExternalAttenuationInterpolationLinear

Selects the linear interpolation method when interpolating S-parameters for the specified table. If the carrier frequency does not match a row in the S-parameter table, this function performs a linear interpolation based on the entries above and below the row in the table.

Note

Currently interpolation is supported only for S-parameter tables.

#### Syntax

int32 __stdcall RFmxInstr_CfgExternalAttenuationInterpolationLinear(niRFmxInstrHandle instrumentHandle, char selectorString[], char tableName, int32 format)

#### Remarks

**Supported devices**: PXIe-5663/5663E, PXIe-5665, PXIe-5668, PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842/5860

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter identifies the instrument session. This parameter is obtained from the RFmxInstr_Initialize function or the RFmxInstr_InitializeFromNIRFSASessionArray function. |
| selectorString | [in] | char[] | This parameter specifies the calibration plane name in which either S-parameter or external attenuation table is stored. This input accepts the calibration plane name with the "calplane::" prefix. If you do not specify the calibration plane name, the default calibration plane instance is used. The default value is "" (empty string). Note For PXIe-5830/5831/5832 devices, port names should also be specified along with Calplane names. Hence, the valid selector string is "calplane::<calplaneName>/port::<portName>". If you specify "port::all", all ports are considered configured. Use RFmxInstr_GetAvailablePorts function to get the valid port names.Example:"""calplane::plane0""calplane::plane0/port::if0""port::if0""calplane::plane0/port::all" |
| tableName | [in] | char | This parameter specifies the name to be associated with either the S-parameter table or the external attenuation table within a calibration plane. Provide a unique name, such as "table1" to configure the table. The default value is "" (empty string).Example:"""table1" |
| format | [in] | int32 | This parameter specifies the format of parameters to interpolate. The default value is Real and Imaginary.Name (Value)DescriptionReal and Imaginary (0)Results in a linear interpolation of the real portion of the complex number and a separate linear interpolation of the complex portion.Magnitude and Phase (1)Results in a linear interpolation.Magnitude and Phase (dB) (2)Results in a linear interpolation. |
| Name (Value) | Description |  |  |
| Real and Imaginary (0) | Results in a linear interpolation of the real portion of the complex number and a separate linear interpolation of the complex portion. |  |  |
| Magnitude and Phase (1) | Results in a linear interpolation. |  |  |
| Magnitude and Phase (dB) (2) | Results in a linear interpolation. |  |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxInstr_GetError](group____root__ni_r_fmx_instr__functions_1ga3c9efe926e0a627b12a3ba6c33e22657.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

External Attenuation Interpolation

<!--NI_TOPIC bundle=rfmxinstr-c-api-ref path=group____root__ni_r_fmx_instr__functions__configuration__send__software__edge__trigger.html language=enus -->
## TOPIC 00076: Send Software Edge Trigger

- bundle_id: `rfmxinstr-c-api-ref`
- source_path: `group____root__ni_r_fmx_instr__functions__configuration__send__software__edge__trigger.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_instr__functions__configuration__send__software__edge__trigger.html
- document_id: `rfmxinstr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxInstr_SendSoftwareEdgeAdvanceTriggerSends a trigger to the waiting device when you choose a software version of the Advance trigger. You can also use this function to override a hardware trigger. RFmxInstr_SendSoftwareEdgeStartTriggerSends a trigger to the w

### Send Software Edge Trigger

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxInstr_SendSoftwareEdgeAdvanceTrigger | Sends a trigger to the waiting device when you choose a software version of the Advance trigger. You can also use this function to override a hardware trigger. |
| RFmxInstr_SendSoftwareEdgeStartTrigger | Sends a trigger to the waiting device when you choose a software version of Start trigger. You can also use this function to override a hardware trigger. |

#### Attachments

None

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxinstr-c-api-ref path=group____root__ni_r_fmx_instr__functions__set__and__get__attributes__get__attributes.html language=enus -->
## TOPIC 00077: Get Attributes

- bundle_id: `rfmxinstr-c-api-ref`
- source_path: `group____root__ni_r_fmx_instr__functions__set__and__get__attributes__get__attributes.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_instr__functions__set__and__get__attributes__get__attributes.html
- document_id: `rfmxinstr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxInstr_GetAttributeF32Queries the value of an RFmx 32-bit floating point number (float32) attribute. RFmxInstr_GetAttributeF32ArrayQueries the value of an RFmx 32-bit floating point number (float32) attribute. You must provide a char array to serve as a buffe

### Get Attributes

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxInstr_GetAttributeF32 | Queries the value of an RFmx 32-bit floating point number (float32) attribute. |
| RFmxInstr_GetAttributeF32Array | Queries the value of an RFmx 32-bit floating point number (float32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL for the attrVal buffer. |
| RFmxInstr_GetAttributeF64 | Queries the value of an RFmx 64-bit floating point number (float64) attribute. |
| RFmxInstr_GetAttributeF64Array | Queries the value of an RFmx 64-bit floating point number (float64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL for the attrVal buffer. |
| RFmxInstr_GetAttributeI16 | Queries the value of an RFmx 16-bit integer (int16) attribute. |
| RFmxInstr_GetAttributeI32 | Queries the value of an RFmx 32-bit integer (int32) attribute. |
| RFmxInstr_GetAttributeI32Array | Queries the value of an RFmx 32-bit integer (int32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL for the attrVal buffer. |
| RFmxInstr_GetAttributeI64 | Queries the value of an RFmx 64-bit integer (int64) attribute. |
| RFmxInstr_GetAttributeI64Array | Queries the value of an RFmx 64-bit integer (int64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL for the attrVal buffer. |
| RFmxInstr_GetAttributeI8 | Queries the value of an RFmx 8-bit integer (int8) attribute. |
| RFmxInstr_GetAttributeI8Array | Queries the value of an RFmx 8-bit integer (int8) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL for the attrVal buffer. |
| RFmxInstr_GetAttributeNIComplexDoubleArray | Queries the value of an RFmx NIComplexDouble attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL for the attrVal buffer. |
| RFmxInstr_GetAttributeNIComplexSingleArray | Queries the value of an RFmx NIComplexSingle attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL for the attrVal buffer. |
| RFmxInstr_GetAttributeString | Queries the value of an RFmx string attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL for the attrVal buffer. |
| RFmxInstr_GetAttributeU16 | Queries the value of an RFmx 16-bit unsigned integer (uInt16) attribute. |
| RFmxInstr_GetAttributeU32 | Queries the value of an RFmx 32-bit unsigned integer (uInt32) attribute. |
| RFmxInstr_GetAttributeU32Array | Queries the value of an RFmx 32-bit unsigned integer (uInt32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL for the attrVal buffer. |
| RFmxInstr_GetAttributeU64Array | Queries the value of an RFmx 64-bit unsigned integer (uInt64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL for the attrVal buffer. |
| RFmxInstr_GetAttributeU8 | Queries the value of an RFmx 8-bit unsigned integer (uInt8) attribute. |
| RFmxInstr_GetAttributeU8Array | Queries the value of an RFmx 8-bit unsigned integer (uInt8) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL for the attrVal buffer. |

#### Attachments

None

Parent topic:

Set and Get Attributes

<!--NI_TOPIC bundle=rfmxinstr-c-api-ref path=group____root__ni_r_fmx_instr__functions__set__and__get__attributes__get__attributes_1ga30ed84ebac9892d6980033b2df6c8901.html language=enus -->
## TOPIC 00078: RFmxInstr_GetAttributeI32

- bundle_id: `rfmxinstr-c-api-ref`
- source_path: `group____root__ni_r_fmx_instr__functions__set__and__get__attributes__get__attributes_1ga30ed84ebac9892d6980033b2df6c8901.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_instr__functions__set__and__get__attributes__get__attributes_1ga30ed84ebac9892d6980033b2df6c8901.html
- document_id: `rfmxinstr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 32-bit integer (int32) attribute. Syntaxint32 __stdcall RFmxInstr_GetAttributeI32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int32 *attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies the RFmx s

### RFmxInstr_GetAttributeI32

Queries the value of an RFmx 32-bit integer (int32) attribute.

#### Syntax

int32 __stdcall RFmxInstr_GetAttributeI32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int32 *attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | int32 * | Returns the current value of the attribute. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxInstr_GetError](group____root__ni_r_fmx_instr__functions_1ga3c9efe926e0a627b12a3ba6c33e22657.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxinstr-c-api-ref path=group____root__ni_r_fmx_instr__functions__set__and__get__attributes__get__attributes_1ga34bd0295b94aa2d3f225c70d1740dbc3.html language=enus -->
## TOPIC 00079: RFmxInstr_GetAttributeU64Array

- bundle_id: `rfmxinstr-c-api-ref`
- source_path: `group____root__ni_r_fmx_instr__functions__set__and__get__attributes__get__attributes_1ga34bd0295b94aa2d3f225c70d1740dbc3.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_instr__functions__set__and__get__attributes__get__attributes_1ga34bd0295b94aa2d3f225c70d1740dbc3.html
- document_id: `rfmxinstr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 64-bit unsigned integer (uInt64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for ar

### RFmxInstr_GetAttributeU64Array

Queries the value of an RFmx 64-bit unsigned integer (uInt64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer.

#### Syntax

int32 __stdcall RFmxInstr_GetAttributeU64Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt64 attrVal[], int32 arraySize, int32 *actualArraySize)

#### Remarks

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | uInt64[] | Returns the current value of the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxInstr_GetError](group____root__ni_r_fmx_instr__functions_1ga3c9efe926e0a627b12a3ba6c33e22657.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxinstr-c-api-ref path=group____root__ni_r_fmx_instr__functions__set__and__get__attributes__get__attributes_1ga3f14c18597521e85118ea2d80e93fed0.html language=enus -->
## TOPIC 00080: RFmxInstr_GetAttributeU32

- bundle_id: `rfmxinstr-c-api-ref`
- source_path: `group____root__ni_r_fmx_instr__functions__set__and__get__attributes__get__attributes_1ga3f14c18597521e85118ea2d80e93fed0.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_instr__functions__set__and__get__attributes__get__attributes_1ga3f14c18597521e85118ea2d80e93fed0.html
- document_id: `rfmxinstr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 32-bit unsigned integer (uInt32) attribute. Syntaxint32 __stdcall RFmxInstr_GetAttributeU32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt32 *attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies

### RFmxInstr_GetAttributeU32

Queries the value of an RFmx 32-bit unsigned integer (uInt32) attribute.

#### Syntax

int32 __stdcall RFmxInstr_GetAttributeU32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt32 *attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | uInt32 * | Returns the current value of the attribute. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxInstr_GetError](group____root__ni_r_fmx_instr__functions_1ga3c9efe926e0a627b12a3ba6c33e22657.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxinstr-c-api-ref path=group____root__ni_r_fmx_instr__functions__set__and__get__attributes__get__attributes_1ga4350826e3babb7d80ec32e3ff7bd33cf.html language=enus -->
## TOPIC 00081: RFmxInstr_GetAttributeF32

- bundle_id: `rfmxinstr-c-api-ref`
- source_path: `group____root__ni_r_fmx_instr__functions__set__and__get__attributes__get__attributes_1ga4350826e3babb7d80ec32e3ff7bd33cf.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_instr__functions__set__and__get__attributes__get__attributes_1ga4350826e3babb7d80ec32e3ff7bd33cf.html
- document_id: `rfmxinstr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 32-bit floating point number (float32) attribute. Syntaxint32 __stdcall RFmxInstr_GetAttributeF32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, float32 *attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIde

### RFmxInstr_GetAttributeF32

Queries the value of an RFmx 32-bit floating point number (float32) attribute.

#### Syntax

int32 __stdcall RFmxInstr_GetAttributeF32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, float32 *attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | float32 * | Returns the current value of the attribute. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxInstr_GetError](group____root__ni_r_fmx_instr__functions_1ga3c9efe926e0a627b12a3ba6c33e22657.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxinstr-c-api-ref path=group____root__ni_r_fmx_instr__functions__set__and__get__attributes__get__attributes_1ga7b88078831abdaa8f39c2b2b640a8736.html language=enus -->
## TOPIC 00082: RFmxInstr_GetAttributeF32Array

- bundle_id: `rfmxinstr-c-api-ref`
- source_path: `group____root__ni_r_fmx_instr__functions__set__and__get__attributes__get__attributes_1ga7b88078831abdaa8f39c2b2b640a8736.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_instr__functions__set__and__get__attributes__get__attributes_1ga7b88078831abdaa8f39c2b2b640a8736.html
- document_id: `rfmxinstr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 32-bit floating point number (float32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0

### RFmxInstr_GetAttributeF32Array

Queries the value of an RFmx 32-bit floating point number (float32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer.

#### Syntax

int32 __stdcall RFmxInstr_GetAttributeF32Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, float32 attrVal[], int32 arraySize, int32 *actualArraySize)

#### Remarks

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | float32[] | Returns the current value of the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxInstr_GetError](group____root__ni_r_fmx_instr__functions_1ga3c9efe926e0a627b12a3ba6c33e22657.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxinstr-c-api-ref path=group____root__ni_r_fmx_instr__functions__set__and__get__attributes__get__attributes_1ga7c0b69a555e898258b038666d1201947.html language=enus -->
## TOPIC 00083: RFmxInstr_GetAttributeI32Array

- bundle_id: `rfmxinstr-c-api-ref`
- source_path: `group____root__ni_r_fmx_instr__functions__set__and__get__attributes__get__attributes_1ga7c0b69a555e898258b038666d1201947.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_instr__functions__set__and__get__attributes__get__attributes_1ga7c0b69a555e898258b038666d1201947.html
- document_id: `rfmxinstr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 32-bit integer (int32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize an

### RFmxInstr_GetAttributeI32Array

Queries the value of an RFmx 32-bit integer (int32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer.

#### Syntax

int32 __stdcall RFmxInstr_GetAttributeI32Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int32 attrVal[], int32 arraySize, int32 *actualArraySize)

#### Remarks

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | int32[] | Returns the current value of the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxInstr_GetError](group____root__ni_r_fmx_instr__functions_1ga3c9efe926e0a627b12a3ba6c33e22657.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxinstr-c-api-ref path=group____root__ni_r_fmx_instr__functions__set__and__get__attributes__get__attributes_1ga7f2570e94cefe57976d0a49300943e68.html language=enus -->
## TOPIC 00084: RFmxInstr_GetAttributeI64Array

- bundle_id: `rfmxinstr-c-api-ref`
- source_path: `group____root__ni_r_fmx_instr__functions__set__and__get__attributes__get__attributes_1ga7f2570e94cefe57976d0a49300943e68.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_instr__functions__set__and__get__attributes__get__attributes_1ga7f2570e94cefe57976d0a49300943e68.html
- document_id: `rfmxinstr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 64-bit integer (int64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize an

### RFmxInstr_GetAttributeI64Array

Queries the value of an RFmx 64-bit integer (int64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer.

#### Syntax

int32 __stdcall RFmxInstr_GetAttributeI64Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int64 attrVal[], int32 arraySize, int32 *actualArraySize)

#### Remarks

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | int64[] | Returns the current value of the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxInstr_GetError](group____root__ni_r_fmx_instr__functions_1ga3c9efe926e0a627b12a3ba6c33e22657.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxinstr-c-api-ref path=group____root__ni_r_fmx_instr__functions__set__and__get__attributes__get__attributes_1ga807301a79413b8d738bc81841a9541c3.html language=enus -->
## TOPIC 00085: RFmxInstr_GetAttributeNIComplexSingleArray

- bundle_id: `rfmxinstr-c-api-ref`
- source_path: `group____root__ni_r_fmx_instr__functions__set__and__get__attributes__get__attributes_1ga807301a79413b8d738bc81841a9541c3.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_instr__functions__set__and__get__attributes__get__attributes_1ga807301a79413b8d738bc81841a9541c3.html
- document_id: `rfmxinstr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx NIComplexSingle attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL

### RFmxInstr_GetAttributeNIComplexSingleArray

Queries the value of an RFmx NIComplexSingle attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer.

#### Syntax

int32 __stdcall RFmxInstr_GetAttributeNIComplexSingleArray(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, NIComplexSingle attrVal[], int32 arraySize, int32 *actualArraySize)

#### Remarks

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | NIComplexSingle[] | Returns the current value of the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxInstr_GetError](group____root__ni_r_fmx_instr__functions_1ga3c9efe926e0a627b12a3ba6c33e22657.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxinstr-c-api-ref path=group____root__ni_r_fmx_instr__functions__set__and__get__attributes__get__attributes_1ga9f8af0cd61cb6aabf2caf71aae955907.html language=enus -->
## TOPIC 00086: RFmxInstr_GetAttributeString

- bundle_id: `rfmxinstr-c-api-ref`
- source_path: `group____root__ni_r_fmx_instr__functions__set__and__get__attributes__get__attributes_1ga9f8af0cd61cb6aabf2caf71aae955907.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_instr__functions__set__and__get__attributes__get__attributes_1ga9f8af0cd61cb6aabf2caf71aae955907.html
- document_id: `rfmxinstr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx string attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL for the a

### RFmxInstr_GetAttributeString

Queries the value of an RFmx string attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer.

#### Syntax

int32 __stdcall RFmxInstr_GetAttributeString(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int32 arraySize, char attrVal[])

#### Remarks

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | Specifies the selector string for the attribute being read. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. Pass the number of bytes in the char buffer you specify for the attrVal parameter. If you pass 0, you can pass NULL for the attrVal parameter. |
| attrVal | [out] | char[] | Returns the current value of the attribute. This parameter must have at least as many bytes as indicated in the arraySize parameter. If you specify 0 for the arraySize parameter, you can pass NULL for this parameter. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

When the **statusOrRequiredSize** return value returns the buffer size, the status code is not returned.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxInstr_GetError](group____root__ni_r_fmx_instr__functions_1ga3c9efe926e0a627b12a3ba6c33e22657.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxinstr-c-api-ref path=group____root__ni_r_fmx_instr__functions__set__and__get__attributes__get__attributes_1gaa49b736661b07960f56e00de20ed5e80.html language=enus -->
## TOPIC 00087: RFmxInstr_GetAttributeU16

- bundle_id: `rfmxinstr-c-api-ref`
- source_path: `group____root__ni_r_fmx_instr__functions__set__and__get__attributes__get__attributes_1gaa49b736661b07960f56e00de20ed5e80.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_instr__functions__set__and__get__attributes__get__attributes_1gaa49b736661b07960f56e00de20ed5e80.html
- document_id: `rfmxinstr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 16-bit unsigned integer (uInt16) attribute. Syntaxint32 __stdcall RFmxInstr_GetAttributeU16(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt16 *attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies

### RFmxInstr_GetAttributeU16

Queries the value of an RFmx 16-bit unsigned integer (uInt16) attribute.

#### Syntax

int32 __stdcall RFmxInstr_GetAttributeU16(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt16 *attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | uInt16 * | Returns the current value of the attribute. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxInstr_GetError](group____root__ni_r_fmx_instr__functions_1ga3c9efe926e0a627b12a3ba6c33e22657.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxinstr-c-api-ref path=group____root__ni_r_fmx_instr__functions__set__and__get__attributes__get__attributes_1gad4440946780830a06af8f673a4860b53.html language=enus -->
## TOPIC 00088: RFmxInstr_GetAttributeF64Array

- bundle_id: `rfmxinstr-c-api-ref`
- source_path: `group____root__ni_r_fmx_instr__functions__set__and__get__attributes__get__attributes_1gad4440946780830a06af8f673a4860b53.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_instr__functions__set__and__get__attributes__get__attributes_1gad4440946780830a06af8f673a4860b53.html
- document_id: `rfmxinstr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 64-bit floating point number (float64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0

### RFmxInstr_GetAttributeF64Array

Queries the value of an RFmx 64-bit floating point number (float64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer.

#### Syntax

int32 __stdcall RFmxInstr_GetAttributeF64Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, float64 attrVal[], int32 arraySize, int32 *actualArraySize)

#### Remarks

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | float64[] | Returns the current value of the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxInstr_GetError](group____root__ni_r_fmx_instr__functions_1ga3c9efe926e0a627b12a3ba6c33e22657.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxinstr-c-api-ref path=group____root__ni_r_fmx_instr__functions__set__and__get__attributes__get__attributes_1gaf1294efc04c814fb86c1579168b1d330.html language=enus -->
## TOPIC 00089: RFmxInstr_GetAttributeI64

- bundle_id: `rfmxinstr-c-api-ref`
- source_path: `group____root__ni_r_fmx_instr__functions__set__and__get__attributes__get__attributes_1gaf1294efc04c814fb86c1579168b1d330.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_instr__functions__set__and__get__attributes__get__attributes_1gaf1294efc04c814fb86c1579168b1d330.html
- document_id: `rfmxinstr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 64-bit integer (int64) attribute. Syntaxint32 __stdcall RFmxInstr_GetAttributeI64(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int64 *attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies the RFmx s

### RFmxInstr_GetAttributeI64

Queries the value of an RFmx 64-bit integer (int64) attribute.

#### Syntax

int32 __stdcall RFmxInstr_GetAttributeI64(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int64 *attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | int64 * | Returns the current value of the attribute. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxInstr_GetError](group____root__ni_r_fmx_instr__functions_1ga3c9efe926e0a627b12a3ba6c33e22657.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxinstr-c-api-ref path=group____root__ni_r_fmx_instr__functions__set__and__get__attributes__get__attributes_1gafb2dd7033252bf63acf5e6857e96698c.html language=enus -->
## TOPIC 00090: RFmxInstr_GetAttributeF64

- bundle_id: `rfmxinstr-c-api-ref`
- source_path: `group____root__ni_r_fmx_instr__functions__set__and__get__attributes__get__attributes_1gafb2dd7033252bf63acf5e6857e96698c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_instr__functions__set__and__get__attributes__get__attributes_1gafb2dd7033252bf63acf5e6857e96698c.html
- document_id: `rfmxinstr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 64-bit floating point number (float64) attribute. Syntaxint32 __stdcall RFmxInstr_GetAttributeF64(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, float64 *attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIde

### RFmxInstr_GetAttributeF64

Queries the value of an RFmx 64-bit floating point number (float64) attribute.

#### Syntax

int32 __stdcall RFmxInstr_GetAttributeF64(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, float64 *attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | float64 * | Returns the current value of the attribute. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxInstr_GetError](group____root__ni_r_fmx_instr__functions_1ga3c9efe926e0a627b12a3ba6c33e22657.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxinstr-c-api-ref path=group____root__ni_r_fmx_instr__functions__set__and__get__attributes__set__attributes.html language=enus -->
## TOPIC 00091: Set Attributes

- bundle_id: `rfmxinstr-c-api-ref`
- source_path: `group____root__ni_r_fmx_instr__functions__set__and__get__attributes__set__attributes.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_instr__functions__set__and__get__attributes__set__attributes.html
- document_id: `rfmxinstr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxInstr_SetAttributeF32Sets the value of an RFmx 32-bit floating point number (float32) attribute. RFmxInstr_SetAttributeF32ArraySets the value of an RFmx 32-bit floating point number (float32) attribute. You must provide a char array to serve as a buffer for

### Set Attributes

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxInstr_SetAttributeF32 | Sets the value of an RFmx 32-bit floating point number (float32) attribute. |
| RFmxInstr_SetAttributeF32Array | Sets the value of an RFmx 32-bit floating point number (float32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. |
| RFmxInstr_SetAttributeF64 | Sets the value of an RFmx 64-bit floating point number (float64) attribute. |
| RFmxInstr_SetAttributeF64Array | Sets the value of an RFmx 64-bit floating point number (float64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. |
| RFmxInstr_SetAttributeI16 | Sets the value of an RFmx 16-bit integer (int16) attribute. |
| RFmxInstr_SetAttributeI32 | Sets the value of an RFmx 32-bit integer (int32) attribute. |
| RFmxInstr_SetAttributeI32Array | Sets the value of an RFmx 32-bit integer (int32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. |
| RFmxInstr_SetAttributeI64 | Sets the value of an RFmx 64-bit integer (int64) attribute. |
| RFmxInstr_SetAttributeI64Array | Sets the value of an RFmx 64-bit integer (int64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. |
| RFmxInstr_SetAttributeI8 | Sets the value of an RFmx 8-bit integer (int8) attribute. |
| RFmxInstr_SetAttributeI8Array | Sets the value of an RFmx 8-bit integer (int8) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. |
| RFmxInstr_SetAttributeNIComplexDoubleArray | Sets the value of an RFmx NIComplexDouble attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. |
| RFmxInstr_SetAttributeNIComplexSingleArray | Sets the value of an RFmx NIComplexSingle attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. |
| RFmxInstr_SetAttributeString | Sets the value of an RFmx string attribute. |
| RFmxInstr_SetAttributeU16 | Sets the value of an RFmx 16-bit unsigned integer (uInt16) attribute. |
| RFmxInstr_SetAttributeU32 | Sets the value of an RFmx 32-bit unsigned integer (uInt32) attribute. |
| RFmxInstr_SetAttributeU32Array | Sets the value of an RFmx 32-bit unsigned integer (uInt32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. |
| RFmxInstr_SetAttributeU64Array | Sets the value of an RFmx 64-bit unsigned integer (uInt64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. |
| RFmxInstr_SetAttributeU8 | Sets the value of an RFmx 8-bit unsigned integer (uInt8) attribute. |
| RFmxInstr_SetAttributeU8Array | Sets the value of an RFmx 8-bit unsigned integer (uInt8) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. |

#### Attachments

None

Parent topic:

Set and Get Attributes

<!--NI_TOPIC bundle=rfmxinstr-c-api-ref path=group____root__ni_r_fmx_instr__functions__set__and__get__attributes__set__attributes_1ga0fa1d37011d6d8a85e426d3dbf500b40.html language=enus -->
## TOPIC 00092: RFmxInstr_SetAttributeI8

- bundle_id: `rfmxinstr-c-api-ref`
- source_path: `group____root__ni_r_fmx_instr__functions__set__and__get__attributes__set__attributes_1ga0fa1d37011d6d8a85e426d3dbf500b40.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_instr__functions__set__and__get__attributes__set__attributes_1ga0fa1d37011d6d8a85e426d3dbf500b40.html
- document_id: `rfmxinstr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 8-bit integer (int8) attribute. Syntaxint32 __stdcall RFmxInstr_SetAttributeI8(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int8 attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies the RFmx session.

### RFmxInstr_SetAttributeI8

Sets the value of an RFmx 8-bit integer (int8) attribute.

#### Syntax

int32 __stdcall RFmxInstr_SetAttributeI8(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int8 attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | int8 | Pass the value to which you want to set the attribute |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxInstr_GetError](group____root__ni_r_fmx_instr__functions_1ga3c9efe926e0a627b12a3ba6c33e22657.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxinstr-c-api-ref path=group____root__ni_r_fmx_instr__functions__set__and__get__attributes__set__attributes_1ga1f628e654cf0818b0a6be94bf7179120.html language=enus -->
## TOPIC 00093: RFmxInstr_SetAttributeF64

- bundle_id: `rfmxinstr-c-api-ref`
- source_path: `group____root__ni_r_fmx_instr__functions__set__and__get__attributes__set__attributes_1ga1f628e654cf0818b0a6be94bf7179120.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_instr__functions__set__and__get__attributes__set__attributes_1ga1f628e654cf0818b0a6be94bf7179120.html
- document_id: `rfmxinstr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 64-bit floating point number (float64) attribute. Syntaxint32 __stdcall RFmxInstr_SetAttributeF64(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, float64 attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentif

### RFmxInstr_SetAttributeF64

Sets the value of an RFmx 64-bit floating point number (float64) attribute.

#### Syntax

int32 __stdcall RFmxInstr_SetAttributeF64(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, float64 attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | float64 | Pass the value to which you want to set the attribute |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxInstr_GetError](group____root__ni_r_fmx_instr__functions_1ga3c9efe926e0a627b12a3ba6c33e22657.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxinstr-c-api-ref path=group____root__ni_r_fmx_instr__functions__set__and__get__attributes__set__attributes_1ga1f8c014524843c319fb720a17df0ce88.html language=enus -->
## TOPIC 00094: RFmxInstr_SetAttributeU8Array

- bundle_id: `rfmxinstr-c-api-ref`
- source_path: `group____root__ni_r_fmx_instr__functions__set__and__get__attributes__set__attributes_1ga1f8c014524843c319fb720a17df0ce88.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_instr__functions__set__and__get__attributes__set__attributes_1ga1f8c014524843c319fb720a17df0ce88.html
- document_id: `rfmxinstr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 8-bit unsigned integer (uInt8) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. Syntaxint32 __stdcall RFmxInstr_SetAttributeU8Array(niRFmxInstrHandle instrumentHandle, char select

### RFmxInstr_SetAttributeU8Array

Sets the value of an RFmx 8-bit unsigned integer (uInt8) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter.

#### Syntax

int32 __stdcall RFmxInstr_SetAttributeU8Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt8 attrVal[], int32 arraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | uInt8[] | Pass the value to which you want to set the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxInstr_GetError](group____root__ni_r_fmx_instr__functions_1ga3c9efe926e0a627b12a3ba6c33e22657.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxinstr-c-api-ref path=group____root__ni_r_fmx_instr__functions__set__and__get__attributes__set__attributes_1ga3afceed675ea81ab9b4f982009d9cd8b.html language=enus -->
## TOPIC 00095: RFmxInstr_SetAttributeI8Array

- bundle_id: `rfmxinstr-c-api-ref`
- source_path: `group____root__ni_r_fmx_instr__functions__set__and__get__attributes__set__attributes_1ga3afceed675ea81ab9b4f982009d9cd8b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_instr__functions__set__and__get__attributes__set__attributes_1ga3afceed675ea81ab9b4f982009d9cd8b.html
- document_id: `rfmxinstr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 8-bit integer (int8) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. Syntaxint32 __stdcall RFmxInstr_SetAttributeI8Array(niRFmxInstrHandle instrumentHandle, char selectorString[]

### RFmxInstr_SetAttributeI8Array

Sets the value of an RFmx 8-bit integer (int8) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter.

#### Syntax

int32 __stdcall RFmxInstr_SetAttributeI8Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int8 attrVal[], int32 arraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | int8[] | Pass the value to which you want to set the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxInstr_GetError](group____root__ni_r_fmx_instr__functions_1ga3c9efe926e0a627b12a3ba6c33e22657.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxinstr-c-api-ref path=group____root__ni_r_fmx_instr__functions__set__and__get__attributes__set__attributes_1ga575f075405488af9d1fd120e4f26ef10.html language=enus -->
## TOPIC 00096: RFmxInstr_SetAttributeI64Array

- bundle_id: `rfmxinstr-c-api-ref`
- source_path: `group____root__ni_r_fmx_instr__functions__set__and__get__attributes__set__attributes_1ga575f075405488af9d1fd120e4f26ef10.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_instr__functions__set__and__get__attributes__set__attributes_1ga575f075405488af9d1fd120e4f26ef10.html
- document_id: `rfmxinstr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 64-bit integer (int64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. Syntaxint32 __stdcall RFmxInstr_SetAttributeI64Array(niRFmxInstrHandle instrumentHandle, char selectorStrin

### RFmxInstr_SetAttributeI64Array

Sets the value of an RFmx 64-bit integer (int64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter.

#### Syntax

int32 __stdcall RFmxInstr_SetAttributeI64Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int64 attrVal[], int32 arraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | int64[] | Pass the value to which you want to set the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxInstr_GetError](group____root__ni_r_fmx_instr__functions_1ga3c9efe926e0a627b12a3ba6c33e22657.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxinstr-c-api-ref path=group____root__ni_r_fmx_instr__functions__set__and__get__attributes__set__attributes_1ga590b53c888e7fc87c83a9612b0d54c33.html language=enus -->
## TOPIC 00097: RFmxInstr_SetAttributeU16

- bundle_id: `rfmxinstr-c-api-ref`
- source_path: `group____root__ni_r_fmx_instr__functions__set__and__get__attributes__set__attributes_1ga590b53c888e7fc87c83a9612b0d54c33.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_instr__functions__set__and__get__attributes__set__attributes_1ga590b53c888e7fc87c83a9612b0d54c33.html
- document_id: `rfmxinstr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 16-bit unsigned integer (uInt16) attribute. Syntaxint32 __stdcall RFmxInstr_SetAttributeU16(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt16 attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies the

### RFmxInstr_SetAttributeU16

Sets the value of an RFmx 16-bit unsigned integer (uInt16) attribute.

#### Syntax

int32 __stdcall RFmxInstr_SetAttributeU16(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt16 attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | uInt16 | Pass the value to which you want to set the attribute |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxInstr_GetError](group____root__ni_r_fmx_instr__functions_1ga3c9efe926e0a627b12a3ba6c33e22657.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxinstr-c-api-ref path=group____root__ni_r_fmx_instr__functions__set__and__get__attributes__set__attributes_1ga5ebd927a0ff91ffc2f1fef90bf38683d.html language=enus -->
## TOPIC 00098: RFmxInstr_SetAttributeU64Array

- bundle_id: `rfmxinstr-c-api-ref`
- source_path: `group____root__ni_r_fmx_instr__functions__set__and__get__attributes__set__attributes_1ga5ebd927a0ff91ffc2f1fef90bf38683d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_instr__functions__set__and__get__attributes__set__attributes_1ga5ebd927a0ff91ffc2f1fef90bf38683d.html
- document_id: `rfmxinstr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 64-bit unsigned integer (uInt64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. Syntaxint32 __stdcall RFmxInstr_SetAttributeU64Array(niRFmxInstrHandle instrumentHandle, char sel

### RFmxInstr_SetAttributeU64Array

Sets the value of an RFmx 64-bit unsigned integer (uInt64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter.

#### Syntax

int32 __stdcall RFmxInstr_SetAttributeU64Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt64 attrVal[], int32 arraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | uInt64[] | Pass the value to which you want to set the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxInstr_GetError](group____root__ni_r_fmx_instr__functions_1ga3c9efe926e0a627b12a3ba6c33e22657.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxinstr-c-api-ref path=group____root__ni_r_fmx_instr__functions__set__and__get__attributes__set__attributes_1ga8f8cbc7ef301c069cc29ae7a91ac562c.html language=enus -->
## TOPIC 00099: RFmxInstr_SetAttributeU32Array

- bundle_id: `rfmxinstr-c-api-ref`
- source_path: `group____root__ni_r_fmx_instr__functions__set__and__get__attributes__set__attributes_1ga8f8cbc7ef301c069cc29ae7a91ac562c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_instr__functions__set__and__get__attributes__set__attributes_1ga8f8cbc7ef301c069cc29ae7a91ac562c.html
- document_id: `rfmxinstr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 32-bit unsigned integer (uInt32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. Syntaxint32 __stdcall RFmxInstr_SetAttributeU32Array(niRFmxInstrHandle instrumentHandle, char sel

### RFmxInstr_SetAttributeU32Array

Sets the value of an RFmx 32-bit unsigned integer (uInt32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter.

#### Syntax

int32 __stdcall RFmxInstr_SetAttributeU32Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt32 attrVal[], int32 arraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | uInt32[] | Pass the value to which you want to set the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxInstr_GetError](group____root__ni_r_fmx_instr__functions_1ga3c9efe926e0a627b12a3ba6c33e22657.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxinstr-c-api-ref path=group____root__ni_r_fmx_instr__functions__set__and__get__attributes__set__attributes_1gac673101da59959978d3ac4ebab6154ef.html language=enus -->
## TOPIC 00100: RFmxInstr_SetAttributeF64Array

- bundle_id: `rfmxinstr-c-api-ref`
- source_path: `group____root__ni_r_fmx_instr__functions__set__and__get__attributes__set__attributes_1gac673101da59959978d3ac4ebab6154ef.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_instr__functions__set__and__get__attributes__set__attributes_1gac673101da59959978d3ac4ebab6154ef.html
- document_id: `rfmxinstr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 64-bit floating point number (float64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. Syntaxint32 __stdcall RFmxInstr_SetAttributeF64Array(niRFmxInstrHandle instrumentHandle, ch

### RFmxInstr_SetAttributeF64Array

Sets the value of an RFmx 64-bit floating point number (float64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter.

#### Syntax

int32 __stdcall RFmxInstr_SetAttributeF64Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, float64 attrVal[], int32 arraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | float64[] | Pass the value to which you want to set the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxInstr_GetError](group____root__ni_r_fmx_instr__functions_1ga3c9efe926e0a627b12a3ba6c33e22657.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxinstr-c-api-ref path=group____root__ni_r_fmx_instr__functions__set__and__get__attributes__set__attributes_1gadbab4e792222dae1333994247755f595.html language=enus -->
## TOPIC 00101: RFmxInstr_SetAttributeI32Array

- bundle_id: `rfmxinstr-c-api-ref`
- source_path: `group____root__ni_r_fmx_instr__functions__set__and__get__attributes__set__attributes_1gadbab4e792222dae1333994247755f595.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_instr__functions__set__and__get__attributes__set__attributes_1gadbab4e792222dae1333994247755f595.html
- document_id: `rfmxinstr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 32-bit integer (int32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. Syntaxint32 __stdcall RFmxInstr_SetAttributeI32Array(niRFmxInstrHandle instrumentHandle, char selectorStrin

### RFmxInstr_SetAttributeI32Array

Sets the value of an RFmx 32-bit integer (int32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter.

#### Syntax

int32 __stdcall RFmxInstr_SetAttributeI32Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int32 attrVal[], int32 arraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | int32[] | Pass the value to which you want to set the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxInstr_GetError](group____root__ni_r_fmx_instr__functions_1ga3c9efe926e0a627b12a3ba6c33e22657.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxinstr-c-api-ref path=group____root__ni_r_fmx_instr__functions__set__and__get__attributes__set__attributes_1gae6c13aff40e656541aca7d8ccea2fc3d.html language=enus -->
## TOPIC 00102: RFmxInstr_SetAttributeNIComplexSingleArray

- bundle_id: `rfmxinstr-c-api-ref`
- source_path: `group____root__ni_r_fmx_instr__functions__set__and__get__attributes__set__attributes_1gae6c13aff40e656541aca7d8ccea2fc3d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_instr__functions__set__and__get__attributes__set__attributes_1gae6c13aff40e656541aca7d8ccea2fc3d.html
- document_id: `rfmxinstr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx NIComplexSingle attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. Syntaxint32 __stdcall RFmxInstr_SetAttributeNIComplexSingleArray(niRFmxInstrHandle instrumentHandle, char selector

### RFmxInstr_SetAttributeNIComplexSingleArray

Sets the value of an RFmx NIComplexSingle attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter.

#### Syntax

int32 __stdcall RFmxInstr_SetAttributeNIComplexSingleArray(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, NIComplexSingle attrVal[], int32 arraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | NIComplexSingle[] | Pass the value to which you want to set the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxInstr_GetError](group____root__ni_r_fmx_instr__functions_1ga3c9efe926e0a627b12a3ba6c33e22657.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxinstr-c-api-ref path=group____root__ni_r_fmx_instr__functions__set__and__get__attributes__set__attributes_1gae7ae3322a98933987a0cd26cbff11d91.html language=enus -->
## TOPIC 00103: RFmxInstr_SetAttributeNIComplexDoubleArray

- bundle_id: `rfmxinstr-c-api-ref`
- source_path: `group____root__ni_r_fmx_instr__functions__set__and__get__attributes__set__attributes_1gae7ae3322a98933987a0cd26cbff11d91.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_instr__functions__set__and__get__attributes__set__attributes_1gae7ae3322a98933987a0cd26cbff11d91.html
- document_id: `rfmxinstr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx NIComplexDouble attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. Syntaxint32 __stdcall RFmxInstr_SetAttributeNIComplexDoubleArray(niRFmxInstrHandle instrumentHandle, char selector

### RFmxInstr_SetAttributeNIComplexDoubleArray

Sets the value of an RFmx NIComplexDouble attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter.

#### Syntax

int32 __stdcall RFmxInstr_SetAttributeNIComplexDoubleArray(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, NIComplexDouble attrVal[], int32 arraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | NIComplexDouble[] | Pass the value to which you want to set the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxInstr_GetError](group____root__ni_r_fmx_instr__functions_1ga3c9efe926e0a627b12a3ba6c33e22657.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes
