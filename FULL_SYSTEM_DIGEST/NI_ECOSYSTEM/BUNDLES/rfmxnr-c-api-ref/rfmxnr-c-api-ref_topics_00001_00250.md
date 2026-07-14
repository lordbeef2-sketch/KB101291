# NI DOCUMENT BUNDLE: rfmxnr-c-api-ref

<!--NI_BUNDLE_CHUNK bundle=rfmxnr-c-api-ref start=1 end=250 -->
<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes_1ga4c0aac1915808889c896b7e20f8f941e.html language=enus -->
## TOPIC 00001: RFMXNR_ATTR_TRANSMIT_ANTENNA_TO_ANALYZE

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes_1ga4c0aac1915808889c896b7e20f8f941e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes_1ga4c0aac1915808889c896b7e20f8f941e.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the physical antenna that is currently connected to the analyzer. SyntaxRFMXNR_ATTR_TRANSMIT_ANTENNA_TO_ANALYZENumeric ValueData TypeAccessApplies To9437339int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance

### RFMXNR_ATTR_TRANSMIT_ANTENNA_TO_ANALYZE

Specifies the physical antenna that is currently connected to the analyzer.

#### Syntax

RFMXNR_ATTR_TRANSMIT_ANTENNA_TO_ANALYZE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9437339 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 0.

Parent topic:

Attributes

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes_1ga6da4371b0ef40ccba30cf63941844ec5.html language=enus -->
## TOPIC 00002: RFMXNR_ATTR_COMPONENT_CARRIER_AT_CENTER_FREQUENCY

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes_1ga6da4371b0ef40ccba30cf63941844ec5.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes_1ga6da4371b0ef40ccba30cf63941844ec5.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the index of the component carrier having its center at the user-configured center frequency. The measurement uses this attribute along with RFMXNR_ATTR_COMPONENT_CARRIER_SPACING_TYPE attribute to calculate the value of the RFMXNR_ATTR_COMPONENT_CARRIER_FREQUENCY. This attribute is ignored

### RFMXNR_ATTR_COMPONENT_CARRIER_AT_CENTER_FREQUENCY

Specifies the index of the component carrier having its center at the user-configured center frequency. The measurement uses this attribute along with [RFMXNR_ATTR_COMPONENT_CARRIER_SPACING_TYPE](group____root__ni_r_fmx_n_r__attributes_1gab1e230ce452437bc639579d0cbc15105.html) attribute to calculate the value of the [RFMXNR_ATTR_COMPONENT_CARRIER_FREQUENCY](group____root__ni_r_fmx_n_r__attributes__component__carrier_1gaf0410d126734d3ae540e80f844c1f873.html). This attribute is ignored if you set the CC Spacing Type attribute to **User**.

#### Syntax

RFMXNR_ATTR_COMPONENT_CARRIER_AT_CENTER_FREQUENCY

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9437204 | int32 | Read/Write | Subblock |

#### Remarks

Use "subblock<n>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute.

Valid values are -1, 0, 1 ... n - 1, inclusive, where n is the number of component carriers in the subblock.

The default value is -1. If the value is -1, the component carrier frequency values are calculated such that the center of the subcarrier(with maximum subcarrier spacing for a frequency range), which is closest to the center of the aggregated channel bandwidth, lies at the center frequency.

Parent topic:

Attributes

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes_1ga883d34b87186d052cf470032999088b1.html language=enus -->
## TOPIC 00003: RFMXNR_ATTR_PIBY2BPSK_POWER_BOOST_ENABLED

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes_1ga883d34b87186d052cf470032999088b1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes_1ga883d34b87186d052cf470032999088b1.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the power boost for PI/2 BPSK signal when you set the RFMXNR_ATTR_FREQUENCY_RANGE attribute to Range 1. This attribute is valid only for uplink direction. SyntaxRFMXNR_ATTR_PIBY2BPSK_POWER_BOOST_ENABLEDNumeric ValueData TypeAccessApplies To9437342int32Read/WriteN/ARemarks For PI/2 BPSK mod

### RFMXNR_ATTR_PIBY2BPSK_POWER_BOOST_ENABLED

Specifies the power boost for PI/2 BPSK signal when you set the [RFMXNR_ATTR_FREQUENCY_RANGE](group____root__ni_r_fmx_n_r__attributes_1ga2d7a755e490f4f0475f463b6e1c649e7.html) attribute to **Range 1**. This attribute is valid only for uplink direction.

#### Syntax

RFMXNR_ATTR_PIBY2BPSK_POWER_BOOST_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9437342 | int32 | Read/Write | N/A |

#### Remarks

For PI/2 BPSK modulation, if this attribute is set to True, [RFMXNR_ATTR_POWER_CLASS](group____root__ni_r_fmx_n_r__attributes_1ga8998a73bba41b05c44f369148f64687a.html) attribute to **3**,[RFMXNR_ATTR_BAND](group____root__ni_r_fmx_n_r__attributes_1ga6ced4b997d00b18f70d4b2f96dfee4cf.html) attribute to 40, 41, 77, 78, or 79, and the [RFMXNR_ATTR_PUSCH_SLOT_ALLOCATION](group____root__ni_r_fmx_n_r__attributes__component__carrier__bandwidth__part__user__pusch_1ga1399a80960797440c033b296f71d2067.html) attribute is set such that, at most 40% of the radio frame is active, then the EVM Equalizer spectral flatness mask specified in section 6.4.2.4.1 of 3GPP 38.101-1 is used. Otherwise the EVM Equalizer spectral flatness mask specified in section 6.4.2.4 of 3GPP 38.101-1 is used.

When you set the Frequency Range attribute to **Range 2-1** or **Range 2-2**, the measurement ignores the PIby2BPSK Pwr Boost Enabled attribute. In this case, when you set the [RFMXNR_ATTR_MODACC_SPECTRAL_FLATNESS_CONDITION](group____root__ni_r_fmx_n_r__attributes__modacc_1ga281f8f1b87901d8a5701ff4772ab930f.html) attribute to **Normal**, the equalizer spectral flatness mask as specified in section 6.4.2.5 of *3GPP TS 38.101-2* is used for the PI/2 BPSK signal. Otherwise, the equalizer spectral flatness mask as specified in section 6.4.2.4 of *3GPP 38.101-2* is used.

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **False**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXNR_VAL_PIBY2BPSK_POWER_BOOST_ENABLED_FALSE | 0 (0x0) | Power boost for PI/2 BPSK modulation is not enabled. |
| RFMXNR_VAL_PIBY2BPSK_POWER_BOOST_ENABLED_TRUE | 1 (0x1) | Power boost for PI/2 BPSK modulation is enabled. |

Parent topic:

Attributes

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes_1ga8998a73bba41b05c44f369148f64687a.html language=enus -->
## TOPIC 00004: RFMXNR_ATTR_POWER_CLASS

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes_1ga8998a73bba41b05c44f369148f64687a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes_1ga8998a73bba41b05c44f369148f64687a.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the power class for the UE as specified in section 6.2 of 3GPP 38.101-1/2/3 specification. SyntaxRFMXNR_ATTR_POWER_CLASSNumeric ValueData TypeAccessApplies To9437340int32Read/WriteN/ARemarks This attribute impacts the spectral flatness mask for uplink.You do not need to use a selector stri

### RFMXNR_ATTR_POWER_CLASS

Specifies the power class for the UE as specified in section 6.2 of *3GPP 38.101-1/2/3* specification.

#### Syntax

RFMXNR_ATTR_POWER_CLASS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9437340 | int32 | Read/Write | N/A |

#### Remarks

This attribute impacts the spectral flatness mask for uplink.

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **3**.

Parent topic:

Attributes

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes_1ga9a4cd858e44d0aa98af4c0999f0de213.html language=enus -->
## TOPIC 00005: RFMXNR_ATTR_NUMBER_OF_RECEIVE_CHAINS

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes_1ga9a4cd858e44d0aa98af4c0999f0de213.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes_1ga9a4cd858e44d0aa98af4c0999f0de213.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of receive chains. SyntaxRFMXNR_ATTR_NUMBER_OF_RECEIVE_CHAINSNumeric ValueData TypeAccessApplies To9490435int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector String topic fo

### RFMXNR_ATTR_NUMBER_OF_RECEIVE_CHAINS

Specifies the number of receive chains.

#### Syntax

RFMXNR_ATTR_NUMBER_OF_RECEIVE_CHAINS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9490435 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 1.

Parent topic:

Attributes

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes_1gaaf87d21cdf2a65944f96a20c4b150abc.html language=enus -->
## TOPIC 00006: RFMXNR_ATTR_PHASE_COMPENSATION_FREQUENCY

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes_1gaaf87d21cdf2a65944f96a20c4b150abc.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes_1gaaf87d21cdf2a65944f96a20c4b150abc.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the frequency used for phase compensation of the signal when you set the RFMXNR_ATTR_PHASE_COMPENSATION attribute to User Defined. This value is expressed in Hz. SyntaxRFMXNR_ATTR_PHASE_COMPENSATION_FREQUENCYNumeric ValueData TypeAccessApplies To9437281float64Read/WriteSubblockRemarks Use

### RFMXNR_ATTR_PHASE_COMPENSATION_FREQUENCY

Specifies the frequency used for phase compensation of the signal when you set the [RFMXNR_ATTR_PHASE_COMPENSATION](group____root__ni_r_fmx_n_r__attributes__advanced_1ga095e654b5090dc7934dc2e445efa1898.html) attribute to **User Defined**. This value is expressed in Hz.

#### Syntax

RFMXNR_ATTR_PHASE_COMPENSATION_FREQUENCY

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9437281 | float64 | Read/Write | Subblock |

#### Remarks

Use "subblock<n>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute.

The default value is 0.

Parent topic:

Attributes

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__acp_1ga3845a89b69aafe3b25f748101a1e1b7e.html language=enus -->
## TOPIC 00007: RFMXNR_ATTR_ACP_ALL_TRACES_ENABLED

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__acp_1ga3845a89b69aafe3b25f748101a1e1b7e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__acp_1ga3845a89b69aafe3b25f748101a1e1b7e.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the traces to be stored and retrieved after performing the ACP measurement. SyntaxRFMXNR_ATTR_ACP_ALL_TRACES_ENABLEDNumeric ValueData TypeAccessApplies To9441321int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the

### RFMXNR_ATTR_ACP_ALL_TRACES_ENABLED

Specifies whether to enable the traces to be stored and retrieved after performing the ACP measurement.

#### Syntax

RFMXNR_ATTR_ACP_ALL_TRACES_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9441321 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is FALSE.

Parent topic:

ACP

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__acp_1ga8db50c3d64b1483ab4750a020cc856d6.html language=enus -->
## TOPIC 00008: RFMXNR_ATTR_ACP_POWER_UNITS

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__acp_1ga8db50c3d64b1483ab4750a020cc856d6.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__acp_1ga8db50c3d64b1483ab4750a020cc856d6.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the unit for absolute power. SyntaxRFMXNR_ATTR_ACP_POWER_UNITSNumeric ValueData TypeAccessApplies To9441307int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector String topic for informat

### RFMXNR_ATTR_ACP_POWER_UNITS

Specifies the unit for absolute power.

#### Syntax

RFMXNR_ATTR_ACP_POWER_UNITS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9441307 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **dBm**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXNR_VAL_ACP_POWER_UNITS_DBM | 0 (0x0) | Indicates that the absolute power is expressed in dBm. |
| RFMXNR_VAL_ACP_POWER_UNITS_DBM_BY_HZ | 1 (0x1) | Indicates that the absolute power is expressed in dBm/Hz. |

Parent topic:

ACP

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__acp_1gaed5b57a9d4d049c700102d12507354a1.html language=enus -->
## TOPIC 00009: RFMXNR_ATTR_ACP_MEASUREMENT_MODE

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__acp_1gaed5b57a9d4d049c700102d12507354a1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__acp_1gaed5b57a9d4d049c700102d12507354a1.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement calibrates the noise floor of analyzer or performs the ACP measurement. SyntaxRFMXNR_ATTR_ACP_MEASUREMENT_MODENumeric ValueData TypeAccessApplies To9441352int32Read/WriteN/ARemarks Refer to the measurement guidelines section in the Noise Compensation Algorithm topic

### RFMXNR_ATTR_ACP_MEASUREMENT_MODE

Specifies whether the measurement calibrates the noise floor of analyzer or performs the ACP measurement.

#### Syntax

RFMXNR_ATTR_ACP_MEASUREMENT_MODE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9441352 | int32 | Read/Write | N/A |

#### Remarks

Refer to the measurement guidelines section in the [Noise Compensation Algorithm](https://www.ni.com/docs/en-US/bundle/rfmx-nr/page/noise-compensation-algorithm.html) topic for more information.

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **Measure**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXNR_VAL_ACP_MEASUREMENT_MODE_MEASURE | 0 (0x0) | Performs the ACP measurement on the acquired signal. |
| RFMXNR_VAL_ACP_MEASUREMENT_MODE_CALIBRATE_NOISE_FLOOR | 1 (0x1) | Performs manual noise calibration of the signal analyzer for the ACP measurement. |

Parent topic:

ACP

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__acp__advanced.html language=enus -->
## TOPIC 00010: Advanced

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__acp__advanced.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__acp__advanced.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXNR_ATTR_ACP_FAR_IF_OUTPUT_POWER_OFFSETSpecifies the offset that is needed to adjust the IF output power levels for the offset channels that are far from the carrier channel to improve the dynamic range. This value is expressed in dB. This attribute is applic

### Advanced

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXNR_ATTR_ACP_FAR_IF_OUTPUT_POWER_OFFSET | Specifies the offset that is needed to adjust the IF output power levels for the offset channels that are far from the carrier channel to improve the dynamic range. This value is expressed in dB. This attribute is applicable only when you set the RFMXNR_ATTR_ACP_IF_OUTPUT_POWER_OFFSET_AUTO attribute to False and RFMXNR_ATTR_ACP_MEASUREMENT_METHOD attribute to Dynamic Range. |
| RFMXNR_ATTR_ACP_IF_OUTPUT_POWER_OFFSET_AUTO | Specifies whether the measurement computes an appropriate IF output power level offset for the offset channels to improve the dynamic range of the ACP measurement. This attribute is applicable only when you set the RFMXNR_ATTR_ACP_MEASUREMENT_METHOD attribute to Dynamic Range. |
| RFMXNR_ATTR_ACP_NEAR_IF_OUTPUT_POWER_OFFSET | Specifies the offset that is needed to adjust the IF output power levels for the offset channels that are near the carrier channel to improve the dynamic range. This value is expressed in dB. This attribute is applicable only when you set the RFMXNR_ATTR_ACP_IF_OUTPUT_POWER_OFFSET_AUTO attribute to False and RFMXNR_ATTR_ACP_MEASUREMENT_METHOD attribute to Dynamic Range. |
| RFMXNR_ATTR_ACP_SEQUENTIAL_FFT_SIZE | Specifies the number of bins to be used for FFT computation, when you set the RFMXNR_ATTR_ACP_MEASUREMENT_METHOD attribute to Sequential FFT. |

#### Attachments

None

Parent topic:

ACP

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__acp__advanced_1ga41f202e33d96a2e9f522bc80a5070b22.html language=enus -->
## TOPIC 00011: RFMXNR_ATTR_ACP_NEAR_IF_OUTPUT_POWER_OFFSET

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__acp__advanced_1ga41f202e33d96a2e9f522bc80a5070b22.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__acp__advanced_1ga41f202e33d96a2e9f522bc80a5070b22.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the offset that is needed to adjust the IF output power levels for the offset channels that are near the carrier channel to improve the dynamic range. This value is expressed in dB. This attribute is applicable only when you set the RFMXNR_ATTR_ACP_IF_OUTPUT_POWER_OFFSET_AUTO attribute to

### RFMXNR_ATTR_ACP_NEAR_IF_OUTPUT_POWER_OFFSET

Specifies the offset that is needed to adjust the IF output power levels for the offset channels that are near the carrier channel to improve the dynamic range. This value is expressed in dB. This attribute is applicable only when you set the [RFMXNR_ATTR_ACP_IF_OUTPUT_POWER_OFFSET_AUTO](group____root__ni_r_fmx_n_r__attributes__acp__advanced_1ga4269b1746b06ec1f52e8875b6bd08cb6.html) attribute to **False** and [RFMXNR_ATTR_ACP_MEASUREMENT_METHOD](group____root__ni_r_fmx_n_r__attributes__acp_1ga1a9171aa71a1698014457eff87927f79.html) attribute to **Dynamic Range**.

#### Syntax

RFMXNR_ATTR_ACP_NEAR_IF_OUTPUT_POWER_OFFSET

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9441317 | float64 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 10.

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__acp__averaging.html language=enus -->
## TOPIC 00012: Averaging

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__acp__averaging.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__acp__averaging.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXNR_ATTR_ACP_AVERAGING_COUNTSpecifies the number of acquisitions used for averaging when you set the RFMXNR_ATTR_ACP_AVERAGING_ENABLED attribute to True. RFMXNR_ATTR_ACP_AVERAGING_ENABLEDSpecifies whether to enable averaging for the ACP measurement. RFMXNR_AT

### Averaging

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXNR_ATTR_ACP_AVERAGING_COUNT | Specifies the number of acquisitions used for averaging when you set the RFMXNR_ATTR_ACP_AVERAGING_ENABLED attribute to True. |
| RFMXNR_ATTR_ACP_AVERAGING_ENABLED | Specifies whether to enable averaging for the ACP measurement. |
| RFMXNR_ATTR_ACP_AVERAGING_TYPE | Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for ACP measurement. |

#### Attachments

None

Parent topic:

ACP

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__acp__component__carrier.html language=enus -->
## TOPIC 00013: Component Carrier

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__acp__component__carrier.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__acp__component__carrier.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXNR_ATTR_ACP_COMPONENT_CARRIER_INTEGRATION_BANDWIDTHSpecifies the integration bandwidth of the component carrier (CC). This value is expressed in Hz. AttachmentsNone

### Component Carrier

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXNR_ATTR_ACP_COMPONENT_CARRIER_INTEGRATION_BANDWIDTH | Specifies the integration bandwidth of the component carrier (CC). This value is expressed in Hz. |

#### Attachments

None

Parent topic:

ACP

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__acp__noise__calibration__averaging_1gaa42f87e371597000f995d2e1aa0499ee.html language=enus -->
## TOPIC 00014: RFMXNR_ATTR_ACP_NOISE_CALIBRATION_AVERAGING_COUNT

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__acp__noise__calibration__averaging_1gaa42f87e371597000f995d2e1aa0499ee.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__acp__noise__calibration__averaging_1gaa42f87e371597000f995d2e1aa0499ee.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the averaging count used for noise calibration when you set the RFMXNR_ATTR_ACP_NOISE_CALIBRATION_AVERAGING_AUTO attribute to False. SyntaxRFMXNR_ATTR_ACP_NOISE_CALIBRATION_AVERAGING_COUNTNumeric ValueData TypeAccessApplies To9441354Int32Read/WriteN/ARemarks You do not need to use a select

### RFMXNR_ATTR_ACP_NOISE_CALIBRATION_AVERAGING_COUNT

Specifies the averaging count used for noise calibration when you set the [RFMXNR_ATTR_ACP_NOISE_CALIBRATION_AVERAGING_AUTO](group____root__ni_r_fmx_n_r__attributes__acp__noise__calibration__averaging_1gaf1637cb9fac1957fa03b2a92bbac75ab.html) attribute to **False**.

#### Syntax

RFMXNR_ATTR_ACP_NOISE_CALIBRATION_AVERAGING_COUNT

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9441354 | Int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 32.

Parent topic:

Averaging

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__acp__noise__calibration__averaging_1gaf1637cb9fac1957fa03b2a92bbac75ab.html language=enus -->
## TOPIC 00015: RFMXNR_ATTR_ACP_NOISE_CALIBRATION_AVERAGING_AUTO

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__acp__noise__calibration__averaging_1gaf1637cb9fac1957fa03b2a92bbac75ab.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__acp__noise__calibration__averaging_1gaf1637cb9fac1957fa03b2a92bbac75ab.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether RFmx automatically computes the averaging count used for instrument noise calibration. SyntaxRFMXNR_ATTR_ACP_NOISE_CALIBRATION_AVERAGING_AUTONumeric ValueData TypeAccessApplies To9441355Int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this att

### RFMXNR_ATTR_ACP_NOISE_CALIBRATION_AVERAGING_AUTO

Specifies whether RFmx automatically computes the averaging count used for instrument noise calibration.

#### Syntax

RFMXNR_ATTR_ACP_NOISE_CALIBRATION_AVERAGING_AUTO

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9441355 | Int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **True**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXNR_VAL_ACP_NOISE_CALIBRATION_AVERAGING_AUTO_FALSE | 0 (0x0) | RFmx uses the averaging count that you set for the RFMXNR_ATTR_ACP_NOISE_CALIBRATION_AVERAGING_COUNT attribute. |
| RFMXNR_VAL_ACP_NOISE_CALIBRATION_AVERAGING_AUTO_TRUE | 1 (0x1) | When you set the RFMXNR_ATTR_ACP_MEASUREMENT_METHOD attribute to Normal or Sequential FFT, RFmx uses a noise calibration averaging count of 32. When you set the ACP Meas Method attribute to Dynamic Range and the sweep time is less than 5 ms, RFmx uses a noise calibration averaging count of 15. When you set the ACP Meas Method to Dynamic Range and the sweep time is greater than or equal to 5 ms, RFmx uses a noise calibration averaging count of 5. |

Parent topic:

Averaging

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__acp__offset_1ga0399291d3cebb301b48d50066e202a9c.html language=enus -->
## TOPIC 00016: RFMXNR_ATTR_ACP_NUMBER_OF_NR_OFFSETS

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__acp__offset_1ga0399291d3cebb301b48d50066e202a9c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__acp__offset_1ga0399291d3cebb301b48d50066e202a9c.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of NR adjacent channel offsets to be configured at offset positions when the RFMXNR_ATTR_ACP_CHANNEL_CONFIGURATION_TYPE attribute is set to Standard or NS_29 or Standard Rel 16 or Standard Rel 18. SyntaxRFMXNR_ATTR_ACP_NUMBER_OF_NR_OFFSETSNumeric ValueData TypeAccessApplies To94

### RFMXNR_ATTR_ACP_NUMBER_OF_NR_OFFSETS

Specifies the number of NR adjacent channel offsets to be configured at offset positions when the [RFMXNR_ATTR_ACP_CHANNEL_CONFIGURATION_TYPE](group____root__ni_r_fmx_n_r__attributes__acp_1ga4b2770c01ebd62c48bcaa588e4e452e5.html) attribute is set to **Standard** or **NS_29** or **Standard Rel 16** or **Standard Rel 18**.

#### Syntax

RFMXNR_ATTR_ACP_NUMBER_OF_NR_OFFSETS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9441291 | int32 | Read/Write | Subblock |

#### Remarks

Use "subblock<n>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute.

The default value is dependent on 3GPP specification.

Parent topic:

Offset

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__acp__offset_1ga127fde8f29d032217d636a8ab1f9b902.html language=enus -->
## TOPIC 00017: RFMXNR_ATTR_ACP_NUMBER_OF_EUTRA_OFFSETS

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__acp__offset_1ga127fde8f29d032217d636a8ab1f9b902.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__acp__offset_1ga127fde8f29d032217d636a8ab1f9b902.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of evolved universal terrestrial radio access (E-UTRA) adjacent channel offsets to be configured at offset positions when the RFMXNR_ATTR_ACP_CHANNEL_CONFIGURATION_TYPE attribute is set to Standard or NS_29 or Standard Rel 16 or Standard Rel 18. For uplink ACP measurement, and f

### RFMXNR_ATTR_ACP_NUMBER_OF_EUTRA_OFFSETS

Specifies the number of evolved universal terrestrial radio access (E-UTRA) adjacent channel offsets to be configured at offset positions when the [RFMXNR_ATTR_ACP_CHANNEL_CONFIGURATION_TYPE](group____root__ni_r_fmx_n_r__attributes__acp_1ga4b2770c01ebd62c48bcaa588e4e452e5.html) attribute is set to **Standard** or **NS_29** or **Standard Rel 16** or **Standard Rel 18**. For uplink ACP measurement, and for downlink ACP measurement in frequency range 2-1 and frequency range 2-2, this attribute has to be 0.

#### Syntax

RFMXNR_ATTR_ACP_NUMBER_OF_EUTRA_OFFSETS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9441290 | int32 | Read/Write | Subblock |

#### Remarks

Use "subblock<n>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute.

The default value is dependent on 3GPP specification.

Parent topic:

Offset

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__acp__offset_1ga58d1edc84e7678d68bddb22c396a6c1d.html language=enus -->
## TOPIC 00018: RFMXNR_ATTR_ACP_OFFSET_FREQUENCY

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__acp__offset_1ga58d1edc84e7678d68bddb22c396a6c1d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__acp__offset_1ga58d1edc84e7678d68bddb22c396a6c1d.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the offset frequency of an offset channel. This value is expressed in Hz. The offset frequency is computed from the center of a reference component carrier/subblock to the center of the nearest RBW filter of the offset channel. SyntaxRFMXNR_ATTR_ACP_OFFSET_FREQUENCYNumeric ValueData TypeAc

### RFMXNR_ATTR_ACP_OFFSET_FREQUENCY

Specifies the offset frequency of an offset channel. This value is expressed in Hz. The offset frequency is computed from the center of a reference component carrier/subblock to the center of the nearest RBW filter of the offset channel.

#### Syntax

RFMXNR_ATTR_ACP_OFFSET_FREQUENCY

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9441294 | float64 | Read/Write | Offset |

#### Remarks

Use "offset<k>" or "subblock<n>" or "subblock<n>/offset<k>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result.

The default value is 10 MHz.

Parent topic:

Offset

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__acp__offset_1ga5dbe65aa37b4c41d372f2b23ce0c3b0d.html language=enus -->
## TOPIC 00019: RFMXNR_ATTR_ACP_NUMBER_OF_OFFSETS

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__acp__offset_1ga5dbe65aa37b4c41d372f2b23ce0c3b0d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__acp__offset_1ga5dbe65aa37b4c41d372f2b23ce0c3b0d.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of configured offset channels when the RFMXNR_ATTR_ACP_CHANNEL_CONFIGURATION_TYPE attribute is set to CustomSyntaxRFMXNR_ATTR_ACP_NUMBER_OF_OFFSETSNumeric ValueData TypeAccessApplies To9441292int32Read/WriteSubblockRemarks Use "subblock<n>" as the selector string to configure or

### RFMXNR_ATTR_ACP_NUMBER_OF_OFFSETS

Specifies the number of configured offset channels when the [RFMXNR_ATTR_ACP_CHANNEL_CONFIGURATION_TYPE](group____root__ni_r_fmx_n_r__attributes__acp_1ga4b2770c01ebd62c48bcaa588e4e452e5.html) attribute is set to **Custom**

#### Syntax

RFMXNR_ATTR_ACP_NUMBER_OF_OFFSETS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9441292 | int32 | Read/Write | Subblock |

#### Remarks

Use "subblock<n>" as the selector string to configure or read this attribute.

The default value is 1.

Parent topic:

Offset

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__acp__offset_1ga68dda861a96f87933ff77e27209c19ac.html language=enus -->
## TOPIC 00020: RFMXNR_ATTR_ACP_OFFSET_INTEGRATION_BANDWIDTH

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__acp__offset_1ga68dda861a96f87933ff77e27209c19ac.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__acp__offset_1ga68dda861a96f87933ff77e27209c19ac.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the integration bandwidth of an offset channel. This value is expressed in Hz. SyntaxRFMXNR_ATTR_ACP_OFFSET_INTEGRATION_BANDWIDTHNumeric ValueData TypeAccessApplies To9441298float64Read/WriteOffsetRemarks Use "offset<k>" or "subblock<n>" or "subblock<n>/offset<k>" as the Selector String to

### RFMXNR_ATTR_ACP_OFFSET_INTEGRATION_BANDWIDTH

Specifies the integration bandwidth of an offset channel. This value is expressed in Hz.

#### Syntax

RFMXNR_ATTR_ACP_OFFSET_INTEGRATION_BANDWIDTH

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9441298 | float64 | Read/Write | Offset |

#### Remarks

Use "offset<k>" or "subblock<n>" or "subblock<n>/offset<k>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result.

The default value is 9 MHz.

Parent topic:

Offset

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__acp__offset_1gadf866a94d08e1b799bbfe2f8e07d99ae.html language=enus -->
## TOPIC 00021: RFMXNR_ATTR_ACP_NUMBER_OF_ENDC_OFFSETS

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__acp__offset_1gadf866a94d08e1b799bbfe2f8e07d99ae.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__acp__offset_1gadf866a94d08e1b799bbfe2f8e07d99ae.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of ENDC adjacent channel offsets to be configured at offset positions when the RFMXNR_ATTR_ACP_CHANNEL_CONFIGURATION_TYPE attribute is set to Standard or NS_29 or Standard Rel 16 or Standard Rel 18SyntaxRFMXNR_ATTR_ACP_NUMBER_OF_ENDC_OFFSETSNumeric ValueData TypeAccessApplies To

### RFMXNR_ATTR_ACP_NUMBER_OF_ENDC_OFFSETS

Specifies the number of ENDC adjacent channel offsets to be configured at offset positions when the [RFMXNR_ATTR_ACP_CHANNEL_CONFIGURATION_TYPE](group____root__ni_r_fmx_n_r__attributes__acp_1ga4b2770c01ebd62c48bcaa588e4e452e5.html) attribute is set to **Standard** or **NS_29** or **Standard Rel 16** or **Standard Rel 18**

#### Syntax

RFMXNR_ATTR_ACP_NUMBER_OF_ENDC_OFFSETS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9441347 | int32 | Read/Write | Subblock |

#### Remarks

Use "subblock<n>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute.

The default value is dependent on 3GPP specification.

Parent topic:

Offset

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__acp__rbw__filter.html language=enus -->
## TOPIC 00022: RBW Filter

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__acp__rbw__filter.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__acp__rbw__filter.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXNR_ATTR_ACP_RBW_FILTER_AUTO_BANDWIDTHSpecifies whether the measurement computes the RBW. RFMXNR_ATTR_ACP_RBW_FILTER_BANDWIDTHSpecifies the bandwidth of the RBW filter, used to sweep the acquired signal, when you set the RFMXNR_ATTR_ACP_RBW_FILTER_AUTO_BANDWI

### RBW Filter

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXNR_ATTR_ACP_RBW_FILTER_AUTO_BANDWIDTH | Specifies whether the measurement computes the RBW. |
| RFMXNR_ATTR_ACP_RBW_FILTER_BANDWIDTH | Specifies the bandwidth of the RBW filter, used to sweep the acquired signal, when you set the RFMXNR_ATTR_ACP_RBW_FILTER_AUTO_BANDWIDTH attribute to False. This value is expressed in Hz. |
| RFMXNR_ATTR_ACP_RBW_FILTER_TYPE | Specifies the shape of the RBW filter. |

#### Attachments

None

Parent topic:

ACP

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__acp__rbw__filter_1gad5294ceec9901ea21af02d36eb1ab6bc.html language=enus -->
## TOPIC 00023: RFMXNR_ATTR_ACP_RBW_FILTER_BANDWIDTH

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__acp__rbw__filter_1gad5294ceec9901ea21af02d36eb1ab6bc.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__acp__rbw__filter_1gad5294ceec9901ea21af02d36eb1ab6bc.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the bandwidth of the RBW filter, used to sweep the acquired signal, when you set the RFMXNR_ATTR_ACP_RBW_FILTER_AUTO_BANDWIDTH attribute to False. This value is expressed in Hz. SyntaxRFMXNR_ATTR_ACP_RBW_FILTER_BANDWIDTHNumeric ValueData TypeAccessApplies To9441303float64Read/WriteN/ARemar

### RFMXNR_ATTR_ACP_RBW_FILTER_BANDWIDTH

Specifies the bandwidth of the RBW filter, used to sweep the acquired signal, when you set the [RFMXNR_ATTR_ACP_RBW_FILTER_AUTO_BANDWIDTH](group____root__ni_r_fmx_n_r__attributes__acp__rbw__filter_1ga06a34739240c3757843ab44df416d088.html) attribute to **False**. This value is expressed in Hz.

#### Syntax

RFMXNR_ATTR_ACP_RBW_FILTER_BANDWIDTH

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9441303 | float64 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 30 kHz.

Parent topic:

RBW Filter

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__acp__results__lower__offset.html language=enus -->
## TOPIC 00024: Lower Offset

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__acp__results__lower__offset.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__acp__results__lower__offset.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXNR_ATTR_ACP_RESULTS_LOWER_OFFSET_ABSOLUTE_POWERReturns the lower (negative) offset channel power. The carrier power is reported in dBm when you set the RFMXNR_ATTR_ACP_POWER_UNITS attribute to dBm, and in dBm/Hz when you set the ACP Pwr Units attribute to dB

### Lower Offset

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXNR_ATTR_ACP_RESULTS_LOWER_OFFSET_ABSOLUTE_POWER | Returns the lower (negative) offset channel power. The carrier power is reported in dBm when you set the RFMXNR_ATTR_ACP_POWER_UNITS attribute to dBm, and in dBm/Hz when you set the ACP Pwr Units attribute to dBm/Hz. |
| RFMXNR_ATTR_ACP_RESULTS_LOWER_OFFSET_RELATIVE_POWER | Returns the power in lower (negative) offset channel relative to the total aggregated power. This value is expressed in dB. |

#### Attachments

None

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__acp__results__upper__offset_1ga3b823921ff81acc57bd238e2aeaa3088.html language=enus -->
## TOPIC 00025: RFMXNR_ATTR_ACP_RESULTS_UPPER_OFFSET_RELATIVE_POWER

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__acp__results__upper__offset_1ga3b823921ff81acc57bd238e2aeaa3088.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__acp__results__upper__offset_1ga3b823921ff81acc57bd238e2aeaa3088.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the power in the upper (positive) offset channel relative to the total aggregated power. This value is expressed in dB. SyntaxRFMXNR_ATTR_ACP_RESULTS_UPPER_OFFSET_RELATIVE_POWERNumeric ValueData TypeAccessApplies To9441346float64Read-OnlyOffsetRemarks Use "offset<k>" or "subblock<n>" or "sub

### RFMXNR_ATTR_ACP_RESULTS_UPPER_OFFSET_RELATIVE_POWER

Returns the power in the upper (positive) offset channel relative to the total aggregated power. This value is expressed in dB.

#### Syntax

RFMXNR_ATTR_ACP_RESULTS_UPPER_OFFSET_RELATIVE_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9441346 | float64 | Read-Only | Offset |

#### Remarks

Use "offset<k>" or "subblock<n>" or "subblock<n>/offset<k>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result.

Parent topic:

Upper Offset

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__advanced_1gaa090211e5557a12a06071b5f2fb6b227.html language=enus -->
## TOPIC 00026: RFMXNR_ATTR_ACQUISITION_BANDWIDTH_OPTIMIZATION_ENABLED

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__advanced_1gaa090211e5557a12a06071b5f2fb6b227.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__advanced_1gaa090211e5557a12a06071b5f2fb6b227.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether RFmx optimizes the acquisition bandwidth. This may cause acquisition center frequency or local oscillator (LO) to be placed at different position than you configured. SyntaxRFMXNR_ATTR_ACQUISITION_BANDWIDTH_OPTIMIZATION_ENABLEDNumeric ValueData TypeAccessApplies To9490433int32Read/

### RFMXNR_ATTR_ACQUISITION_BANDWIDTH_OPTIMIZATION_ENABLED

Specifies whether RFmx optimizes the acquisition bandwidth. This may cause acquisition center frequency or local oscillator (LO) to be placed at different position than you configured.

#### Syntax

RFMXNR_ATTR_ACQUISITION_BANDWIDTH_OPTIMIZATION_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9490433 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **False**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXNR_VAL_ACQUISITION_BANDWIDTH_OPTIMIZATION_ENABLED_FALSE | 0 (0x0) | RFmx does not optimize acquisition bandwidth and will be based on the Nyquist criterion. The value of the acquisition center frequency is the same as the value of the RFMXNR_ATTR_CENTER_FREQUENCY that you configure. |
| RFMXNR_VAL_ACQUISITION_BANDWIDTH_OPTIMIZATION_ENABLED_TRUE | 1 (0x1) | RFmx positions the acquisition center frequency to acquire the least bandwidth based on the configuration and span needed for the measurement. This helps in reducing the amount of data to process for the measurement, thus improving the speed. However this might cause the LO to be positioned at a non-dc subcarrier position, hence the measurement sensitive to it should have this attribute disabled. |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__advanced_1gaf653fc9b49c5ce185301fbb77d612665.html language=enus -->
## TOPIC 00027: RFMXNR_ATTR_GRID_SIZE_MODE

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__advanced_1gaf653fc9b49c5ce185301fbb77d612665.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__advanced_1gaf653fc9b49c5ce185301fbb77d612665.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to set the grid size of all BWPs and SSB in a component carrier automatically or manually. SyntaxRFMXNR_ATTR_GRID_SIZE_MODENumeric ValueData TypeAccessApplies To9437468int32Read/WriteN/ARemarks When you set this attribute to Auto, the grid size is set equal to the maximum transmiss

### RFMXNR_ATTR_GRID_SIZE_MODE

Specifies whether to set the grid size of all BWPs and SSB in a component carrier automatically or manually.

#### Syntax

RFMXNR_ATTR_GRID_SIZE_MODE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9437468 | int32 | Read/Write | N/A |

#### Remarks

When you set this attribute to **Auto**, the grid size is set equal to the maximum transmission bandwidth specified in the 3GPP specification.

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for the named signals.

The default value is **Auto**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXNR_VAL_GRID_SIZE_MODE_MANUAL | 0 (0x0) | The grid size is user specified. |
| RFMXNR_VAL_GRID_SIZE_MODE_AUTO | 1 (0x1) | The grid size is set equal to the maximum transmission bandwidth specified by the 3GPP specification. |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__chp.html language=enus -->
## TOPIC 00028: CHP

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__chp.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__chp.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsAveragingComponent CarrierFFTNoise CalibrationNoise CompensationRBW FilterResultsSweep TimeGroup membersNameDescriptionRFMXNR_ATTR_CHP_ALL_TRACES_ENABLEDSpecifies whether to enable the traces to be stored and retrieved after performing the CHP measurement. RFMXNR_ATTR_CHP_AMPLITUDE_CORRECTION_

### CHP

#### Groups

- Averaging
- Component Carrier
- FFT
- Noise Calibration
- Noise Compensation
- RBW Filter
- Results
- Sweep Time

#### Group members

| Name | Description |
| --- | --- |
| RFMXNR_ATTR_CHP_ALL_TRACES_ENABLED | Specifies whether to enable the traces to be stored and retrieved after performing the CHP measurement. |
| RFMXNR_ATTR_CHP_AMPLITUDE_CORRECTION_TYPE | Specifies whether the amplitude of frequency bins in the spectrum used by the measurement is corrected for external attenuation at RF center frequency or corrected for external attenuation at individual frequency bins Use the RFmxInstr Configure External Attenuation Table function to configure the external attenuation table. |
| RFMXNR_ATTR_CHP_INTEGRATION_BANDWIDTH_TYPE | Specifies the integration bandwidth (IBW) type used to measure the power of the acquired signal. Integration bandwidth is the frequency interval over which the power in each frequency bin is added to measure the total power in that interval. |
| RFMXNR_ATTR_CHP_MEASUREMENT_ENABLED | Specifies whether to enable the channel power measurement. |
| RFMXNR_ATTR_CHP_MEASUREMENT_MODE | Specifies whether the measurement calibrates the noise floor of analyzer or performs the CHP measurement. |
| RFMXNR_ATTR_CHP_NUMBER_OF_ANALYSIS_THREADS | Specifies the maximum number of threads used for parallelism for the CHP measurement. |
| RFMXNR_ATTR_CHP_SUBBLOCK_INTEGRATION_BANDWIDTH | Specifies the integration bandwidth of the subblock. This value is expressed in Hz. It is the span from left edge of the integration bandwidth of the leftmost carrier to the right edge of the integration bandwidth of the rightmost carrier within a subblock. |

#### Attachments

None

Parent topic:

Attributes

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__chp_1ga0cad84a936d11bdf87c7d5a3e0615e32.html language=enus -->
## TOPIC 00029: RFMXNR_ATTR_CHP_MEASUREMENT_MODE

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__chp_1ga0cad84a936d11bdf87c7d5a3e0615e32.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__chp_1ga0cad84a936d11bdf87c7d5a3e0615e32.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement calibrates the noise floor of analyzer or performs the CHP measurement. SyntaxRFMXNR_ATTR_CHP_MEASUREMENT_MODENumeric ValueData TypeAccessApplies To9449505int32Read/WriteN/ARemarks Refer to the measurement guidelines section in the Noise Compensation Algorithm topic

### RFMXNR_ATTR_CHP_MEASUREMENT_MODE

Specifies whether the measurement calibrates the noise floor of analyzer or performs the CHP measurement.

#### Syntax

RFMXNR_ATTR_CHP_MEASUREMENT_MODE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9449505 | int32 | Read/Write | N/A |

#### Remarks

Refer to the measurement guidelines section in the [Noise Compensation Algorithm](https://www.ni.com/docs/en-US/bundle/rfmx-nr/page/noise-compensation-algorithm.html) topic for more information.

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **Measure**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXNR_VAL_CHP_MEASUREMENT_MODE_MEASURE | 0 (0x0) | Performs the CHP measurement on the acquired signal. |
| RFMXNR_VAL_CHP_MEASUREMENT_MODE_CALIBRATE_NOISE_FLOOR | 1 (0x1) | Performs manual noise calibration of the signal analyzer for the CHP measurement. |

Parent topic:

CHP

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__chp__sweep__time_1ga1cd8f7d79c060a6dd5c698a8217bce3d.html language=enus -->
## TOPIC 00030: RFMXNR_ATTR_CHP_SWEEP_TIME_AUTO

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__chp__sweep__time_1ga1cd8f7d79c060a6dd5c698a8217bce3d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__chp__sweep__time_1ga1cd8f7d79c060a6dd5c698a8217bce3d.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement sets the sweep time. SyntaxRFMXNR_ATTR_CHP_SWEEP_TIME_AUTONumeric ValueData TypeAccessApplies To9449474int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strin

### RFMXNR_ATTR_CHP_SWEEP_TIME_AUTO

Specifies whether the measurement sets the sweep time.

#### Syntax

RFMXNR_ATTR_CHP_SWEEP_TIME_AUTO

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9449474 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **True**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXNR_VAL_CHP_SWEEP_TIME_AUTO_FALSE | 0 (0x0) | The measurement uses the sweep time that you specify in the RFMXNR_ATTR_CHP_SWEEP_TIME_INTERVAL attribute. |
| RFMXNR_VAL_CHP_SWEEP_TIME_AUTO_TRUE | 1 (0x1) | The measurement uses the sweep time based on the resolution bandwidth. |

Parent topic:

Sweep Time

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__component__carrier_1ga50cbfb29808c47ba32dfca52a6bf3743.html language=enus -->
## TOPIC 00031: RFMXNR_ATTR_RATED_TRP

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__component__carrier_1ga50cbfb29808c47ba32dfca52a6bf3743.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__component__carrier_1ga50cbfb29808c47ba32dfca52a6bf3743.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the rated carrier TRP output power. This value is expressed in dBm. SyntaxRFMXNR_ATTR_RATED_TRPNumeric ValueData TypeAccessApplies To9437345float64Read/WriteCarrierRemarks Use "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>" as the Selector String to configure or read this attribu

### RFMXNR_ATTR_RATED_TRP

Specifies the rated carrier TRP output power. This value is expressed in dBm.

#### Syntax

RFMXNR_ATTR_RATED_TRP

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9437345 | float64 | Read/Write | Carrier |

#### Remarks

Use "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute.

The default value is 0.

Parent topic:

Component Carrier

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__component__carrier_1gabd8c62f5d7e5236f26eb46c60f3a8c33.html language=enus -->
## TOPIC 00032: RFMXNR_ATTR_SUB_BAND_ALLOCATION

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__component__carrier_1gabd8c62f5d7e5236f26eb46c60f3a8c33.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__component__carrier_1gabd8c62f5d7e5236f26eb46c60f3a8c33.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the sub-band allocation in the NR-U wideband channel. Sub-band is the set of RBs with approximately 20 MHz bandwidth, where the wideband channel is uniformly divided into an integer number of 20 MHz sub-bands. SyntaxRFMXNR_ATTR_SUB_BAND_ALLOCATIONNumeric ValueData TypeAccessApplies To94372

### RFMXNR_ATTR_SUB_BAND_ALLOCATION

Specifies the sub-band allocation in the NR-U wideband channel. Sub-band is the set of RBs with approximately 20 MHz bandwidth, where the wideband channel is uniformly divided into an integer number of 20 MHz sub-bands.

#### Syntax

RFMXNR_ATTR_SUB_BAND_ALLOCATION

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9437244 | char[] | Read/Write | Carrier |

#### Remarks

This attribute is valid only for the bands n46, n96, n102 as defined in the 3GPP TS 37.213 for the shared spectrum channel access.

- Single unsigned integer values or last
- A range of single unsigned integer values given as i0:i1, where i0 represents the first and i1 the last value in the range, with i0 <= i1. The keyword last expands to the largest allowed value, depending on the context of the range specification.

Examples: 0,2 will expand to {0,2}

0:2,3 will expand to {0,1,2,3}.

Use "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute.

The default value is 0-Last, where

Last = 0 for 20 MHz

1 for 40 MHz

2 for 60 MHz

3 for 80 MHz

4 for 100 MHz

Parent topic:

Component Carrier

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__component__carrier__bandwidth__part_1gabb70036c7695dc63deea90a3fe4a0392.html language=enus -->
## TOPIC 00033: RFMXNR_ATTR_NUMBER_OF_BANDWIDTH_PARTS

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__component__carrier__bandwidth__part_1gabb70036c7695dc63deea90a3fe4a0392.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__component__carrier__bandwidth__part_1gabb70036c7695dc63deea90a3fe4a0392.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of bandwidth parts present in the component carrier. SyntaxRFMXNR_ATTR_NUMBER_OF_BANDWIDTH_PARTSNumeric ValueData TypeAccessApplies To9437245int32Read/WriteCarrierRemarks Use "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>" as the Selector String to configure or read th

### RFMXNR_ATTR_NUMBER_OF_BANDWIDTH_PARTS

Specifies the number of bandwidth parts present in the component carrier.

#### Syntax

RFMXNR_ATTR_NUMBER_OF_BANDWIDTH_PARTS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9437245 | int32 | Read/Write | Carrier |

#### Remarks

Use "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute.

The default value is 1.

Parent topic:

Bandwidth Part

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__component__carrier__bandwidth__part__coreset_1ga4e81aa462a2cf17aed6635d35aeb244e.html language=enus -->
## TOPIC 00034: RFMXNR_ATTR_CORESET_RESOURCE_BLOCK_OFFSET

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__component__carrier__bandwidth__part__coreset_1ga4e81aa462a2cf17aed6635d35aeb244e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__component__carrier__bandwidth__part__coreset_1ga4e81aa462a2cf17aed6635d35aeb244e.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the starting resource block of a CORESET cluster. SyntaxRFMXNR_ATTR_CORESET_RESOURCE_BLOCK_OFFSETNumeric ValueData TypeAccessApplies To9437450int32Read/WriteCoresetclusterRemarks Use "coresetcluster<<i>j</i>>" or "coreset<k>" or "bwp<<i>l</i>>" or "carrier<<i>m</i>>" or "subblock<n>" or "s

### RFMXNR_ATTR_CORESET_RESOURCE_BLOCK_OFFSET

Specifies the starting resource block of a CORESET cluster.

#### Syntax

RFMXNR_ATTR_CORESET_RESOURCE_BLOCK_OFFSET

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9437450 | int32 | Read/Write | Coresetcluster |

#### Remarks

Use "coresetcluster<<i>j</i>>" or "coreset<k>" or "bwp<<i>l</i>>" or "carrier<<i>m</i>>" or "subblock<n>" or "subblock<n>/carrier<<i>m</i>>/bwp<<i>l</i>>/coreset<k>"/coresetcluster<*j*> as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute.

Valid values should be a multiple of 6. The default value is 0.

Parent topic:

CORESET

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__component__carrier__bandwidth__part__coreset__pdcch_1ga8a5ab70af72a6ccf39c7b1a4c207c64d.html language=enus -->
## TOPIC 00035: RFMXNR_ATTR_NUMBER_OF_PDCCH_CONFIGURATIONS

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__component__carrier__bandwidth__part__coreset__pdcch_1ga8a5ab70af72a6ccf39c7b1a4c207c64d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__component__carrier__bandwidth__part__coreset__pdcch_1ga8a5ab70af72a6ccf39c7b1a4c207c64d.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of PDCCH Configurations for a CORESET. SyntaxRFMXNR_ATTR_NUMBER_OF_PDCCH_CONFIGURATIONSNumeric ValueData TypeAccessApplies To9437458int32Read/WriteCoresetRemarks Use "coreset<<i>l</i>>" or "bwp<<i>m</i>>" or "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>/bwp<<i>m</i>>/

### RFMXNR_ATTR_NUMBER_OF_PDCCH_CONFIGURATIONS

Specifies the number of PDCCH Configurations for a CORESET.

#### Syntax

RFMXNR_ATTR_NUMBER_OF_PDCCH_CONFIGURATIONS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9437458 | int32 | Read/Write | Coreset |

#### Remarks

Use "coreset<<i>l</i>>" or "bwp<<i>m</i>>" or "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>/bwp<<i>m</i>>/coreset<<i>l</i>>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute.

The default value is 0.

Parent topic:

PDCCH

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__component__carrier__bandwidth__part__coreset__pdcch_1gaddb281b96b6af9a18b20a1389f2b3cf0.html language=enus -->
## TOPIC 00036: RFMXNR_ATTR_PDCCH_CCE_OFFSET

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__component__carrier__bandwidth__part__coreset__pdcch_1gaddb281b96b6af9a18b20a1389f2b3cf0.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__component__carrier__bandwidth__part__coreset__pdcch_1gaddb281b96b6af9a18b20a1389f2b3cf0.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the PDCCH CCE offset. SyntaxRFMXNR_ATTR_PDCCH_CCE_OFFSETNumeric ValueData TypeAccessApplies To9437460int32Read/WritePDCCHRemarks Use " pdcch <<i>j</i>>" or "coreset<k>" or "bwp<<i>l</i>>" or "carrier<<i>m</i>>" or "subblock<n>" or "subblock<n>/carrier<<i>m</i>>/bwp<<i>l</i>>/coreset<k>"/pd

### RFMXNR_ATTR_PDCCH_CCE_OFFSET

Specifies the PDCCH CCE offset.

#### Syntax

RFMXNR_ATTR_PDCCH_CCE_OFFSET

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9437460 | int32 | Read/Write | PDCCH |

#### Remarks

Use " pdcch <<i>j</i>>" or "coreset<k>" or "bwp<<i>l</i>>" or "carrier<<i>m</i>>" or "subblock<n>" or "subblock<n>/carrier<<i>m</i>>/bwp<<i>l</i>>/coreset<k>"/pdcch<*j*> as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute.

It is used when the PDCCH Candidate Index is set to -1. The default value is 0.

Parent topic:

PDCCH

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__component__carrier__bandwidth__part__user.html language=enus -->
## TOPIC 00037: User

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__component__carrier__bandwidth__part__user.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__component__carrier__bandwidth__part__user.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsPDSCHPUSCHGroup membersNameDescriptionRFMXNR_ATTR_NUMBER_OF_USERSSpecifies the number of users present in the bandwidth part. RFMXNR_ATTR_RNTISpecifies the RNTI. AttachmentsNone

### User

#### Groups

- PDSCH
- PUSCH

#### Group members

| Name | Description |
| --- | --- |
| RFMXNR_ATTR_NUMBER_OF_USERS | Specifies the number of users present in the bandwidth part. |
| RFMXNR_ATTR_RNTI | Specifies the RNTI. |

#### Attachments

None

Parent topic:

Bandwidth Part

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__component__carrier__bandwidth__part__user_1ga46360467f94622fd074201448f142cf5.html language=enus -->
## TOPIC 00038: RFMXNR_ATTR_NUMBER_OF_USERS

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__component__carrier__bandwidth__part__user_1ga46360467f94622fd074201448f142cf5.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__component__carrier__bandwidth__part__user_1ga46360467f94622fd074201448f142cf5.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of users present in the bandwidth part. SyntaxRFMXNR_ATTR_NUMBER_OF_USERSNumeric ValueData TypeAccessApplies To9437284int32Read/WriteBandwidthpartRemarks Use "bwp<<i>m</i>>" or "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>/bwp<<i>m</i>>" as the Selector String to conf

### RFMXNR_ATTR_NUMBER_OF_USERS

Specifies the number of users present in the bandwidth part.

#### Syntax

RFMXNR_ATTR_NUMBER_OF_USERS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9437284 | int32 | Read/Write | Bandwidthpart |

#### Remarks

Use "bwp<<i>m</i>>" or "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>/bwp<<i>m</i>>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute.

The default value is 1.

Parent topic:

User

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__component__carrier__bandwidth__part__user_1ga9e2ae70a0aabcca7ce31b17c339117bc.html language=enus -->
## TOPIC 00039: RFMXNR_ATTR_RNTI

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__component__carrier__bandwidth__part__user_1ga9e2ae70a0aabcca7ce31b17c339117bc.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__component__carrier__bandwidth__part__user_1ga9e2ae70a0aabcca7ce31b17c339117bc.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the RNTI. SyntaxRFMXNR_ATTR_RNTINumeric ValueData TypeAccessApplies To9437285int32Read/WriteUserRemarks Use "user<<i>l</i>>" or "bwp<<i>m</i>>" or "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>/bwp<<i>m</i>>/user<<i>l</i>>" as the Selector String to configure or read this attribu

### RFMXNR_ATTR_RNTI

Specifies the RNTI.

#### Syntax

RFMXNR_ATTR_RNTI

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9437285 | int32 | Read/Write | User |

#### Remarks

Use "user<<i>l</i>>" or "bwp<<i>m</i>>" or "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>/bwp<<i>m</i>>/user<<i>l</i>>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute.

The default value is 1.

Parent topic:

User

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__component__carrier__bandwidth__part__user__pdsch_1ga0da7e5b0bb971612e66e599061e1c922.html language=enus -->
## TOPIC 00040: RFMXNR_ATTR_PDSCH_SLOT_ALLOCATION

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__component__carrier__bandwidth__part__user__pdsch_1ga0da7e5b0bb971612e66e599061e1c922.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__component__carrier__bandwidth__part__user__pdsch_1ga0da7e5b0bb971612e66e599061e1c922.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the slot allocation in NR Frame. This defines the indices of the allocated slots. SyntaxRFMXNR_ATTR_PDSCH_SLOT_ALLOCATIONNumeric ValueData TypeAccessApplies To9437312char[]Read/WritePDSCHRemarks The format is defined by range format specifiers. The range format specifier is a comma separat

### RFMXNR_ATTR_PDSCH_SLOT_ALLOCATION

Specifies the slot allocation in NR Frame. This defines the indices of the allocated slots.

#### Syntax

RFMXNR_ATTR_PDSCH_SLOT_ALLOCATION

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9437312 | char[] | Read/Write | PDSCH |

#### Remarks

- Single unsigned integer values or last
- A range of single unsigned integer values given as i0:i1, where i0 represents the first and i1 the last value in the range, with i0 <= i1. The keyword last expands to the largest allowed value, depending on the context of the range specification.

Examples: 2,5 will expand to {2,5}

1:3,7 will expand to {1,2,3,7}.

Use "pdsch<<i>r</i>>" or "user<<i>l</i>>" or "bwp<<i>m</i>>" or "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>/bwp<<i>m</i>>/user<<i>l</i>>/pdsch<<i>r</i>>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute.

The default value is 0-Last. Valid values are from 0 to (Maximum number of slots in frame - 1), inclusive.

Parent topic:

PDSCH

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__component__carrier__bandwidth__part__user__pdsch_1ga728a820fdb90acee98dc089c219e3e0c.html language=enus -->
## TOPIC 00041: RFMXNR_ATTR_PDSCH_NUMBER_OF_RESOURCE_BLOCKS

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__component__carrier__bandwidth__part__user__pdsch_1ga728a820fdb90acee98dc089c219e3e0c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__component__carrier__bandwidth__part__user__pdsch_1ga728a820fdb90acee98dc089c219e3e0c.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of consecutive resource blocks in a PDSCH cluster. SyntaxRFMXNR_ATTR_PDSCH_NUMBER_OF_RESOURCE_BLOCKSNumeric ValueData TypeAccessApplies To9437289int32Read/WritePdschclusterRemarks Use "pdschcluster<<i>s</i>>" or "pdsch<<i>r</i>>" or "user<<i>l</i>>" or "bwp<<i>m</i>>" or "carrie

### RFMXNR_ATTR_PDSCH_NUMBER_OF_RESOURCE_BLOCKS

Specifies the number of consecutive resource blocks in a PDSCH cluster.

#### Syntax

RFMXNR_ATTR_PDSCH_NUMBER_OF_RESOURCE_BLOCKS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9437289 | int32 | Read/Write | Pdschcluster |

#### Remarks

Use "pdschcluster<<i>s</i>>" or "pdsch<<i>r</i>>" or "user<<i>l</i>>" or "bwp<<i>m</i>>" or "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>/bwp<<i>m</i>>/user<<i>l</i>>/pdsch<<i>r</i>>/pdschcluster<<i>s</i>>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute.

The default value is -1. If you set this attribute to -1, all available resource blocks within the bandwidth part are configured.

Parent topic:

PDSCH

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__component__carrier__bandwidth__part__user__pdsch__dmrs_1ga1fe84d82315dba6812aef88ef86de0d5.html language=enus -->
## TOPIC 00042: RFMXNR_ATTR_PDSCH_DMRS_ANTENNA_PORTS

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__component__carrier__bandwidth__part__user__pdsch__dmrs_1ga1fe84d82315dba6812aef88ef86de0d5.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__component__carrier__bandwidth__part__user__pdsch__dmrs_1ga1fe84d82315dba6812aef88ef86de0d5.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the antenna ports used for DMRS transmission. SyntaxRFMXNR_ATTR_PDSCH_DMRS_ANTENNA_PORTSNumeric ValueData TypeAccessApplies To9437291char[]Read/WritePDSCHRemarks Use "pdsch<<i>r</i>>" or "user<<i>l</i>>" or "bwp<<i>m</i>>" or "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>/bwp<<i>

### RFMXNR_ATTR_PDSCH_DMRS_ANTENNA_PORTS

Specifies the antenna ports used for DMRS transmission.

#### Syntax

RFMXNR_ATTR_PDSCH_DMRS_ANTENNA_PORTS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9437291 | char[] | Read/Write | PDSCH |

#### Remarks

Use "pdsch<<i>r</i>>" or "user<<i>l</i>>" or "bwp<<i>m</i>>" or "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>/bwp<<i>m</i>>/user<<i>l</i>>/pdsch<<i>r</i>>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute.

The default value is 1000.

Parent topic:

DMRS

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__component__carrier__bandwidth__part__user__pdsch__ptrs.html language=enus -->
## TOPIC 00043: PTRS

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__component__carrier__bandwidth__part__user__pdsch__ptrs.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__component__carrier__bandwidth__part__user__pdsch__ptrs.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsMappingGroup membersNameDescriptionRFMXNR_ATTR_EPRE_RATIO_PORTSpecifies the EPRE Ratio Port used to determine the PDSCH PT-RS RE power scaling as defined in the Table 4.1-2 of 3GPP TS 38.214 specification when you set the RFMXNR_ATTR_PDSCH_PTRS_POWER_MODE attribute to Standard. RFMXNR_ATTR_PDS

### PTRS

#### Groups

- Mapping

#### Group members

| Name | Description |
| --- | --- |
| RFMXNR_ATTR_EPRE_RATIO_PORT | Specifies the EPRE Ratio Port used to determine the PDSCH PT-RS RE power scaling as defined in the Table 4.1-2 of 3GPP TS 38.214 specification when you set the RFMXNR_ATTR_PDSCH_PTRS_POWER_MODE attribute to Standard. |
| RFMXNR_ATTR_PDSCH_PTRS_ANTENNA_PORTS | Specifies the DMRS Antenna Ports associated with PTRS transmission. |
| RFMXNR_ATTR_PDSCH_PTRS_ENABLED | Specifies whether PT-RS is present in the transmitted signal. |
| RFMXNR_ATTR_PDSCH_PTRS_POWER | Specifies the factor by which the PDSCH PTRS REs are boosted, compared to PDSCH REs. This value is expressed in dB. The value of this attribute is taken as an input when you set the RFMXNR_ATTR_PDSCH_PTRS_POWER_MODE attribute to User Defined. If you set the PDSCH PTRS Pwr Mode attribute to Standard, the value is computed from other parameters. |
| RFMXNR_ATTR_PDSCH_PTRS_POWER_MODE | Specifies whether the configured RFMXNR_ATTR_PDSCH_PTRS_POWER is calculated as defined in 3GPP specification or configured by you. |

#### Attachments

None

Parent topic:

PDSCH

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__component__carrier__bandwidth__part__user__pdsch__ptrs_1ga250b1b645a47fff3e150547e4de4c698.html language=enus -->
## TOPIC 00044: RFMXNR_ATTR_PDSCH_PTRS_ANTENNA_PORTS

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__component__carrier__bandwidth__part__user__pdsch__ptrs_1ga250b1b645a47fff3e150547e4de4c698.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__component__carrier__bandwidth__part__user__pdsch__ptrs_1ga250b1b645a47fff3e150547e4de4c698.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the DMRS Antenna Ports associated with PTRS transmission. SyntaxRFMXNR_ATTR_PDSCH_PTRS_ANTENNA_PORTSNumeric ValueData TypeAccessApplies To9437306char[]Read/WritePDSCHRemarks Use "pdsch<<i>r</i>>" or "user<<i>l</i>>" or "bwp<<i>m</i>>" or "carrier<k>" or "subblock<n>" or "subblock<n>/carrie

### RFMXNR_ATTR_PDSCH_PTRS_ANTENNA_PORTS

Specifies the DMRS Antenna Ports associated with PTRS transmission.

#### Syntax

RFMXNR_ATTR_PDSCH_PTRS_ANTENNA_PORTS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9437306 | char[] | Read/Write | PDSCH |

#### Remarks

Use "pdsch<<i>r</i>>" or "user<<i>l</i>>" or "bwp<<i>m</i>>" or "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>/bwp<<i>m</i>>/user<<i>l</i>>/pdsch<<i>r</i>>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute.

The default value is 0.

Parent topic:

PTRS

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__component__carrier__bandwidth__part__user__pdsch__ptrs_1ga51f647dca025b0c0d395a59fb6e2af87.html language=enus -->
## TOPIC 00045: RFMXNR_ATTR_EPRE_RATIO_PORT

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__component__carrier__bandwidth__part__user__pdsch__ptrs_1ga51f647dca025b0c0d395a59fb6e2af87.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__component__carrier__bandwidth__part__user__pdsch__ptrs_1ga51f647dca025b0c0d395a59fb6e2af87.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the EPRE Ratio Port used to determine the PDSCH PT-RS RE power scaling as defined in the Table 4.1-2 of 3GPP TS 38.214 specification when you set the RFMXNR_ATTR_PDSCH_PTRS_POWER_MODE attribute to Standard. SyntaxRFMXNR_ATTR_EPRE_RATIO_PORTNumeric ValueData TypeAccessApplies To9437330int32

### RFMXNR_ATTR_EPRE_RATIO_PORT

Specifies the EPRE Ratio Port used to determine the PDSCH PT-RS RE power scaling as defined in the Table 4.1-2 of *3GPP TS 38.214* specification when you set the [RFMXNR_ATTR_PDSCH_PTRS_POWER_MODE](group____root__ni_r_fmx_n_r__attributes__component__carrier__bandwidth__part__user__pdsch__ptrs_1ga00549a2c6327fa16e447c8594d361dad.html) attribute to **Standard**.

#### Syntax

RFMXNR_ATTR_EPRE_RATIO_PORT

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9437330 | int32 | Read/Write | PDSCH |

#### Remarks

Use "pdsch<<i>r</i>>" or "user<<i>l</i>>" or "bwp<<i>m</i>>" or "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>/bwp<<i>m</i>>/user<<i>l</i>>/pdsch<<i>r</i>>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute.

The default value is 0.

Parent topic:

PTRS

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__component__carrier__bandwidth__part__user__pdsch__ptrs__mapping.html language=enus -->
## TOPIC 00046: Mapping

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__component__carrier__bandwidth__part__user__pdsch__ptrs__mapping.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__component__carrier__bandwidth__part__user__pdsch__ptrs__mapping.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXNR_ATTR_PDSCH_PTRS_FREQUENCY_DENSITYSpecifies the density of PTRS in frequency domain. RFMXNR_ATTR_PDSCH_PTRS_RE_OFFSETSpecifies the RE Offset to be used for transmission of PTRS as defined in Table 7.4.1.2.2-1 of 3GPP 38.211 specification. RFMXNR_ATTR_PDSCH

### Mapping

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXNR_ATTR_PDSCH_PTRS_FREQUENCY_DENSITY | Specifies the density of PTRS in frequency domain. |
| RFMXNR_ATTR_PDSCH_PTRS_RE_OFFSET | Specifies the RE Offset to be used for transmission of PTRS as defined in Table 7.4.1.2.2-1 of 3GPP 38.211 specification. |
| RFMXNR_ATTR_PDSCH_PTRS_TIME_DENSITY | Specifies the density of PTRS in time domain. |

#### Attachments

None

Parent topic:

PTRS

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__component__carrier__bandwidth__part__user__pusch_1ga4c3ebe4bf323ef8fbd1a7c703c122be3.html language=enus -->
## TOPIC 00047: RFMXNR_ATTR_PUSCH_NUMBER_OF_RESOURCE_BLOCKS

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__component__carrier__bandwidth__part__user__pusch_1ga4c3ebe4bf323ef8fbd1a7c703c122be3.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__component__carrier__bandwidth__part__user__pusch_1ga4c3ebe4bf323ef8fbd1a7c703c122be3.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of consecutive resource blocks in a physical uplink shared channel (PUSCH) cluster. This attribute is ignored if you set the RFMXNR_ATTR_AUTO_RESOURCE_BLOCK_DETECTION_ENABLED attribute to True. SyntaxRFMXNR_ATTR_PUSCH_NUMBER_OF_RESOURCE_BLOCKSNumeric ValueData TypeAccessApplies

### RFMXNR_ATTR_PUSCH_NUMBER_OF_RESOURCE_BLOCKS

Specifies the number of consecutive resource blocks in a physical uplink shared channel (PUSCH) cluster. This attribute is ignored if you set the [RFMXNR_ATTR_AUTO_RESOURCE_BLOCK_DETECTION_ENABLED](group____root__ni_r_fmx_n_r__attributes__signal__detection_1gabe8a913090c18dc6d4736335e76b2019.html) attribute to **True**.

#### Syntax

RFMXNR_ATTR_PUSCH_NUMBER_OF_RESOURCE_BLOCKS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9437225 | int32 | Read/Write | Puschcluster |

#### Remarks

Use "puschcluster<<i>s</i>>" or "pusch<<i>r</i>>" or "user<<i>l</i>>" or "bwp<<i>m</i>>" or "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>/bwp<<i>m</i>>/user<<i>l</i>>/pusch<<i>r</i>>/puschcluster<<i>s</i>>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute.

The default value is -1. If you set this attribute to -1, all available resource blocks for the specified bandwidth are configured.

Parent topic:

PUSCH

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__component__carrier__bandwidth__part__user__pusch_1ga50b5b690f3b121e8b10aa2ca9f8ecb31.html language=enus -->
## TOPIC 00048: RFMXNR_ATTR_PUSCH_NUMBER_OF_RESOURCE_BLOCK_CLUSTERS

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__component__carrier__bandwidth__part__user__pusch_1ga50b5b690f3b121e8b10aa2ca9f8ecb31.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__component__carrier__bandwidth__part__user__pusch_1ga50b5b690f3b121e8b10aa2ca9f8ecb31.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of clusters of resource allocations with each cluster including one or more consecutive resource blocks. This attribute is ignored if you set the RFMXNR_ATTR_AUTO_RESOURCE_BLOCK_DETECTION_ENABLED attribute to True. SyntaxRFMXNR_ATTR_PUSCH_NUMBER_OF_RESOURCE_BLOCK_CLUSTERSNumeric

### RFMXNR_ATTR_PUSCH_NUMBER_OF_RESOURCE_BLOCK_CLUSTERS

Specifies the number of clusters of resource allocations with each cluster including one or more consecutive resource blocks. This attribute is ignored if you set the [RFMXNR_ATTR_AUTO_RESOURCE_BLOCK_DETECTION_ENABLED](group____root__ni_r_fmx_n_r__attributes__signal__detection_1gabe8a913090c18dc6d4736335e76b2019.html) attribute to **True**.

#### Syntax

RFMXNR_ATTR_PUSCH_NUMBER_OF_RESOURCE_BLOCK_CLUSTERS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9437223 | int32 | Read/Write | PUSCH |

#### Remarks

Use "pusch<<i>r</i>>" or "user<<i>l</i>>" or "bwp<<i>m</i>>" or "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>/bwp<<i>m</i>>/user<<i>l</i>>/pusch<<i>r</i>>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute.

The default value is 1.

Parent topic:

PUSCH

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__component__carrier__bandwidth__part__user__pusch_1gaa5edf179d689daa3d9c72c7c31574562.html language=enus -->
## TOPIC 00049: RFMXNR_ATTR_PUSCH_RESOURCE_BLOCK_OFFSET

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__component__carrier__bandwidth__part__user__pusch_1gaa5edf179d689daa3d9c72c7c31574562.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__component__carrier__bandwidth__part__user__pusch_1gaa5edf179d689daa3d9c72c7c31574562.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the starting resource block number of a PUSCH cluster. This attribute is ignored if you set the RFMXNR_ATTR_AUTO_RESOURCE_BLOCK_DETECTION_ENABLED attribute to True. SyntaxRFMXNR_ATTR_PUSCH_RESOURCE_BLOCK_OFFSETNumeric ValueData TypeAccessApplies To9437224int32Read/WritePuschclusterRemarks

### RFMXNR_ATTR_PUSCH_RESOURCE_BLOCK_OFFSET

Specifies the starting resource block number of a PUSCH cluster. This attribute is ignored if you set the [RFMXNR_ATTR_AUTO_RESOURCE_BLOCK_DETECTION_ENABLED](group____root__ni_r_fmx_n_r__attributes__signal__detection_1gabe8a913090c18dc6d4736335e76b2019.html) attribute to **True**.

#### Syntax

RFMXNR_ATTR_PUSCH_RESOURCE_BLOCK_OFFSET

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9437224 | int32 | Read/Write | Puschcluster |

#### Remarks

Use "puschcluster<<i>s</i>>" or "pusch<<i>r</i>>" or "user<<i>l</i>>" or "bwp<<i>m</i>>" or "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>/bwp<<i>m</i>>/user<<i>l</i>>/pusch<<i>r</i>>/puschcluster<<i>s</i>>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute.

The default value is 0.

Parent topic:

PUSCH

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__component__carrier__bandwidth__part__user__pusch_1gab875e771c4b44f5cfb281808273c9d4a.html language=enus -->
## TOPIC 00050: RFMXNR_ATTR_PUSCH_SYMBOL_ALLOCATION

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__component__carrier__bandwidth__part__user__pusch_1gab875e771c4b44f5cfb281808273c9d4a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__component__carrier__bandwidth__part__user__pusch_1gab875e771c4b44f5cfb281808273c9d4a.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the symbol allocation of each slot allocation. SyntaxRFMXNR_ATTR_PUSCH_SYMBOL_ALLOCATIONNumeric ValueData TypeAccessApplies To9437261char[]Read/WritePUSCHRemarks The format is defined by range format specifiers. The range format specifier is a comma separated list of entries in the followi

### RFMXNR_ATTR_PUSCH_SYMBOL_ALLOCATION

Specifies the symbol allocation of each slot allocation.

#### Syntax

RFMXNR_ATTR_PUSCH_SYMBOL_ALLOCATION

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9437261 | char[] | Read/Write | PUSCH |

#### Remarks

- Single unsigned integer values or last
- A range of single unsigned integer values given as i0:i1, where i0 represents the first and i1 the last value in the range, with i0 <= i1. The keyword last expands to the largest allowed value, depending on the context of the range specification.

Examples: 2,5 will expand to {2,5}

1:3,7 will expand to {1,2,3,7}.

Use "pusch<<i>r</i>>" or "user<<i>l</i>>" or "bwp<<i>m</i>>" or "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>/bwp<<i>m</i>>/user<<i>l</i>>/pusch<<i>r</i>>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute.

The default value is 0-Last. Valid values are from 0 to 13, inclusive.

Parent topic:

PUSCH

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__component__carrier__bandwidth__part__user__pusch_1gacb0ce9f0c979ceb54e0c961ed7101ee8.html language=enus -->
## TOPIC 00051: RFMXNR_ATTR_NUMBER_OF_PUSCH_CONFIGURATIONS

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__component__carrier__bandwidth__part__user__pusch_1gacb0ce9f0c979ceb54e0c961ed7101ee8.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__component__carrier__bandwidth__part__user__pusch_1gacb0ce9f0c979ceb54e0c961ed7101ee8.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of PUSCH slot configurations. SyntaxRFMXNR_ATTR_NUMBER_OF_PUSCH_CONFIGURATIONSNumeric ValueData TypeAccessApplies To9437259int32Read/WriteUserRemarks Use "user<<i>l</i>>" or "bwp<<i>m</i>>" or "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>/bwp<<i>m</i>>/user<<i>l</i>>"

### RFMXNR_ATTR_NUMBER_OF_PUSCH_CONFIGURATIONS

Specifies the number of PUSCH slot configurations.

#### Syntax

RFMXNR_ATTR_NUMBER_OF_PUSCH_CONFIGURATIONS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9437259 | int32 | Read/Write | User |

#### Remarks

Use "user<<i>l</i>>" or "bwp<<i>m</i>>" or "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>/bwp<<i>m</i>>/user<<i>l</i>>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute.

The default value is 1.

Parent topic:

PUSCH

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__component__carrier__bandwidth__part__user__pusch_1gad7ce4fee08509163f2d28d1b44a2d42b.html language=enus -->
## TOPIC 00052: RFMXNR_ATTR_PUSCH_TRANSFORM_PRECODING_ENABLED

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__component__carrier__bandwidth__part__user__pusch_1gad7ce4fee08509163f2d28d1b44a2d42b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__component__carrier__bandwidth__part__user__pusch_1gad7ce4fee08509163f2d28d1b44a2d42b.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether transform precoding is enabled. Enable transform precoding when analyzing a DFT-s-OFDM waveform. SyntaxRFMXNR_ATTR_PUSCH_TRANSFORM_PRECODING_ENABLEDNumeric ValueData TypeAccessApplies To9437214int32Read/WritePUSCHRemarks Use "pusch<<i>r</i>>" or "user<<i>l</i>>" or "bwp<<i>m</i>>"

### RFMXNR_ATTR_PUSCH_TRANSFORM_PRECODING_ENABLED

Specifies whether transform precoding is enabled. Enable transform precoding when analyzing a DFT-s-OFDM waveform.

#### Syntax

RFMXNR_ATTR_PUSCH_TRANSFORM_PRECODING_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9437214 | int32 | Read/Write | PUSCH |

#### Remarks

Use "pusch<<i>r</i>>" or "user<<i>l</i>>" or "bwp<<i>m</i>>" or "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>/bwp<<i>m</i>>/user<<i>l</i>>/pusch<<i>r</i>>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute.

The default value is **False**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXNR_VAL_PUSCH_TRANSFORM_PRECODING_ENABLED_FALSE | 0 (0x0) | Transform precoding is disabled. |
| RFMXNR_VAL_PUSCH_TRANSFORM_PRECODING_ENABLED_TRUE | 1 (0x1) | Transform precoding is enabled. |

Parent topic:

PUSCH

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__component__carrier__bandwidth__part__user__pusch__dmrs_1ga186d069830d77f7389f48a2d06369bef.html language=enus -->
## TOPIC 00053: RFMXNR_ATTR_PUSCH_DMRS_ANTENNA_PORTS

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__component__carrier__bandwidth__part__user__pusch__dmrs_1ga186d069830d77f7389f48a2d06369bef.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__component__carrier__bandwidth__part__user__pusch__dmrs_1ga186d069830d77f7389f48a2d06369bef.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the antenna ports used for DMRS transmission. SyntaxRFMXNR_ATTR_PUSCH_DMRS_ANTENNA_PORTSNumeric ValueData TypeAccessApplies To9437249char[]Read/WritePUSCHRemarks Use "pusch<<i>r</i>>" or "user<<i>l</i>>" or "bwp<<i>m</i>>" or "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>/bwp<<i>

### RFMXNR_ATTR_PUSCH_DMRS_ANTENNA_PORTS

Specifies the antenna ports used for DMRS transmission.

#### Syntax

RFMXNR_ATTR_PUSCH_DMRS_ANTENNA_PORTS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9437249 | char[] | Read/Write | PUSCH |

#### Remarks

Use "pusch<<i>r</i>>" or "user<<i>l</i>>" or "bwp<<i>m</i>>" or "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>/bwp<<i>m</i>>/user<<i>l</i>>/pusch<<i>r</i>>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute.

The default value is 0. Valid values depend on [RFMXNR_ATTR_PUSCH_MAPPING_TYPE](group____root__ni_r_fmx_n_r__attributes__component__carrier__bandwidth__part__user__pusch__dmrs__mapping_1ga21763224f339a941dfc4bd599cecdaca.html) and [RFMXNR_ATTR_PUSCH_DMRS_NUMBER_OF_CDM_GROUPS](group____root__ni_r_fmx_n_r__attributes__component__carrier__bandwidth__part__user__pusch__dmrs_1gacec3e668dc6b86d6f2693c7303441de1.html) attributes.

Parent topic:

DMRS

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__component__carrier__bandwidth__part__user__pusch__dmrs_1ga229879636586d2ddfa52b1cac13f4c60.html language=enus -->
## TOPIC 00054: RFMXNR_ATTR_PUSCH_DMRS_POWER_MODE

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__component__carrier__bandwidth__part__user__pusch__dmrs_1ga229879636586d2ddfa52b1cac13f4c60.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__component__carrier__bandwidth__part__user__pusch__dmrs_1ga229879636586d2ddfa52b1cac13f4c60.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the value of RFMXNR_ATTR_PUSCH_DMRS_POWER attribute is calculated based on the RFMXNR_ATTR_PUSCH_DMRS_NUMBER_OF_CDM_GROUPS attribute or specified by you. SyntaxRFMXNR_ATTR_PUSCH_DMRS_POWER_MODENumeric ValueData TypeAccessApplies To9437265int32Read/WritePUSCHRemarks Use "pusch<<i>r<

### RFMXNR_ATTR_PUSCH_DMRS_POWER_MODE

Specifies whether the value of [RFMXNR_ATTR_PUSCH_DMRS_POWER](group____root__ni_r_fmx_n_r__attributes__component__carrier__bandwidth__part__user__pusch__dmrs_1ga6461f44bb05b88576494f02fb0a8d00a.html) attribute is calculated based on the [RFMXNR_ATTR_PUSCH_DMRS_NUMBER_OF_CDM_GROUPS](group____root__ni_r_fmx_n_r__attributes__component__carrier__bandwidth__part__user__pusch__dmrs_1gacec3e668dc6b86d6f2693c7303441de1.html) attribute or specified by you.

#### Syntax

RFMXNR_ATTR_PUSCH_DMRS_POWER_MODE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9437265 | int32 | Read/Write | PUSCH |

#### Remarks

Use "pusch<<i>r</i>>" or "user<<i>l</i>>" or "bwp<<i>m</i>>" or "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>/bwp<<i>m</i>>/user<<i>l</i>>/pusch<<i>r</i>>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute.

The default value is **CDM Groups**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXNR_VAL_PUSCH_DMRS_POWER_MODE_CDM_GROUPS | 0 (0x0) | The value of PUSCH DMRS Pwr is calculated based on PDSCH DMRS Num CDM Groups attribute. |
| RFMXNR_VAL_PUSCH_DMRS_POWER_MODE_USER_DEFINED | 1 (0x1) | The value of PUSCH DMRS Pwr is specified by you. |

Parent topic:

DMRS

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__component__carrier__bandwidth__part__user__pusch__dmrs_1gafc432af735c028340f29f35e5c7e41f8.html language=enus -->
## TOPIC 00055: RFMXNR_ATTR_PUSCH_DMRS_RELEASE_VERSION

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__component__carrier__bandwidth__part__user__pusch__dmrs_1gafc432af735c028340f29f35e5c7e41f8.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__component__carrier__bandwidth__part__user__pusch__dmrs_1gafc432af735c028340f29f35e5c7e41f8.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the 3GGP release version for PUSCH DMRS. SyntaxRFMXNR_ATTR_PUSCH_DMRS_RELEASE_VERSIONNumeric ValueData TypeAccessApplies To9437462int32Read/WritePUSCHRemarks Use "pusch<<i>r</i>>" or "user<<i>l</i>>" or "bwp<<i>m</i>>" or "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>/bwp<<i>m</i

### RFMXNR_ATTR_PUSCH_DMRS_RELEASE_VERSION

Specifies the 3GGP release version for PUSCH DMRS.

#### Syntax

RFMXNR_ATTR_PUSCH_DMRS_RELEASE_VERSION

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9437462 | int32 | Read/Write | PUSCH |

#### Remarks

Use "pusch<<i>r</i>>" or "user<<i>l</i>>" or "bwp<<i>m</i>>" or "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>/bwp<<i>m</i>>/user<<i>l</i>>/pusch<<i>r</i>>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute.

The default value is 0.

| Name | Value | Description |
| --- | --- | --- |
| RFMXNR_VAL_PUSCH_DMRS_RELEASE_VERSION_RELEASE15 | 0 (0x0) | Specifies a 3GGP release version of 15 for PUSCH DMRS. |
| RFMXNR_VAL_PUSCH_DMRS_RELEASE_VERSION_RELEASE16 | 1 (0x1) | Specifies a 3GGP release version of 16 or later for PUSCH DMRS. |

Parent topic:

DMRS

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__component__carrier__bandwidth__part__user__pusch__dmrs__low__papr__sequence_1gaa3bf2f3dca3609bc36707ff15206e0b7.html language=enus -->
## TOPIC 00056: RFMXNR_ATTR_PUSCH_DMRS_GROUP_HOPPING_ENABLED

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__component__carrier__bandwidth__part__user__pusch__dmrs__low__papr__sequence_1gaa3bf2f3dca3609bc36707ff15206e0b7.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__component__carrier__bandwidth__part__user__pusch__dmrs__low__papr__sequence_1gaa3bf2f3dca3609bc36707ff15206e0b7.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the group hopping is enabled. This attribute is valid only when you set the RFMXNR_ATTR_PUSCH_TRANSFORM_PRECODING_ENABLED attribute to True. SyntaxRFMXNR_ATTR_PUSCH_DMRS_GROUP_HOPPING_ENABLEDNumeric ValueData TypeAccessApplies To9437217int32Read/WritePUSCHRemarks Use "pusch<<i>r</i

### RFMXNR_ATTR_PUSCH_DMRS_GROUP_HOPPING_ENABLED

Specifies whether the group hopping is enabled. This attribute is valid only when you set the [RFMXNR_ATTR_PUSCH_TRANSFORM_PRECODING_ENABLED](group____root__ni_r_fmx_n_r__attributes__component__carrier__bandwidth__part__user__pusch_1gad7ce4fee08509163f2d28d1b44a2d42b.html) attribute to **True**.

#### Syntax

RFMXNR_ATTR_PUSCH_DMRS_GROUP_HOPPING_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9437217 | int32 | Read/Write | PUSCH |

#### Remarks

Use "pusch<<i>r</i>>" or "user<<i>l</i>>" or "bwp<<i>m</i>>" or "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>/bwp<<i>m</i>>/user<<i>l</i>>/pusch<<i>r</i>>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute.

The default value is **False**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXNR_VAL_PUSCH_DMRS_GROUP_HOPPING_ENABLED_FALSE | 0 (0x0) | Group hopping is disabled. |
| RFMXNR_VAL_PUSCH_DMRS_GROUP_HOPPING_ENABLED_TRUE | 1 (0x1) | Group hopping is enabled. |

Parent topic:

Low PAPR Sequence

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__component__carrier__bandwidth__part__user__pusch__ptrs_1gaceed56ed8534b4242e0c7bdd31b36ab6.html language=enus -->
## TOPIC 00057: RFMXNR_ATTR_PUSCH_PTRS_ANTENNA_PORTS

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__component__carrier__bandwidth__part__user__pusch__ptrs_1gaceed56ed8534b4242e0c7bdd31b36ab6.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__component__carrier__bandwidth__part__user__pusch__ptrs_1gaceed56ed8534b4242e0c7bdd31b36ab6.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the DMRS antenna ports associated with PTRS transmission. This attribute is valid only if you set the RFMXNR_ATTR_PUSCH_PTRS_ENABLED attribute to True. SyntaxRFMXNR_ATTR_PUSCH_PTRS_ANTENNA_PORTSNumeric ValueData TypeAccessApplies To9437270char[]Read/WritePUSCHRemarks Use "pusch<<i>r</i>>"

### RFMXNR_ATTR_PUSCH_PTRS_ANTENNA_PORTS

Specifies the DMRS antenna ports associated with PTRS transmission. This attribute is valid only if you set the [RFMXNR_ATTR_PUSCH_PTRS_ENABLED](group____root__ni_r_fmx_n_r__attributes__component__carrier__bandwidth__part__user__pusch__ptrs_1gab9934b34bd136fc1a96b3d0b4a78f73c.html) attribute to **True**.

#### Syntax

RFMXNR_ATTR_PUSCH_PTRS_ANTENNA_PORTS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9437270 | char[] | Read/Write | PUSCH |

#### Remarks

Use "pusch<<i>r</i>>" or "user<<i>l</i>>" or "bwp<<i>m</i>>" or "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>/bwp<<i>m</i>>/user<<i>l</i>>/pusch<<i>r</i>>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute.

The default value is 0.

Parent topic:

PTRS

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__component__carrier__bandwidth__part__user__pusch__ptrs_1gae8fb331d8d9972935618c086fc717a74.html language=enus -->
## TOPIC 00058: RFMXNR_ATTR_PUSCH_PTRS_POWER

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__component__carrier__bandwidth__part__user__pusch__ptrs_1gae8fb331d8d9972935618c086fc717a74.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__component__carrier__bandwidth__part__user__pusch__ptrs_1gae8fb331d8d9972935618c086fc717a74.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the factor by which the PUSCH PTRS REs are boosted. This value is expressed in dB. This attribute is valid only if you set the RFMXNR_ATTR_PUSCH_PTRS_ENABLED attribute to True. SyntaxRFMXNR_ATTR_PUSCH_PTRS_POWERNumeric ValueData TypeAccessApplies To9437272float64Read/WritePUSCHRemarks Use

### RFMXNR_ATTR_PUSCH_PTRS_POWER

Specifies the factor by which the PUSCH PTRS REs are boosted. This value is expressed in dB. This attribute is valid only if you set the [RFMXNR_ATTR_PUSCH_PTRS_ENABLED](group____root__ni_r_fmx_n_r__attributes__component__carrier__bandwidth__part__user__pusch__ptrs_1gab9934b34bd136fc1a96b3d0b4a78f73c.html) attribute to **True**.

#### Syntax

RFMXNR_ATTR_PUSCH_PTRS_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9437272 | float64 | Read/Write | PUSCH |

#### Remarks

Use "pusch<<i>r</i>>" or "user<<i>l</i>>" or "bwp<<i>m</i>>" or "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>/bwp<<i>m</i>>/user<<i>l</i>>/pusch<<i>r</i>>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute.

The default value is 0.

Parent topic:

PTRS

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__component__carrier__bandwidth__part__user__pusch__ptrs__mapping.html language=enus -->
## TOPIC 00059: Mapping

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__component__carrier__bandwidth__part__user__pusch__ptrs__mapping.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__component__carrier__bandwidth__part__user__pusch__ptrs__mapping.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXNR_ATTR_PUSCH_PTRS_FREQUENCY_DENSITYSpecifies the density of PTRS in frequency domain. This attribute is valid only if you set the RFMXNR_ATTR_PUSCH_PTRS_ENABLED attribute to True and RFMXNR_ATTR_PUSCH_TRANSFORM_PRECODING_ENABLED attribute to False. RFMXNR_A

### Mapping

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXNR_ATTR_PUSCH_PTRS_FREQUENCY_DENSITY | Specifies the density of PTRS in frequency domain. This attribute is valid only if you set the RFMXNR_ATTR_PUSCH_PTRS_ENABLED attribute to True and RFMXNR_ATTR_PUSCH_TRANSFORM_PRECODING_ENABLED attribute to False. |
| RFMXNR_ATTR_PUSCH_PTRS_RE_OFFSET | Specifies the RE offset to be used for transmission of PTRS as defined in the Table 6.4.1.2.2.1-1 of 3GPP 38.211 specification. This attribute is valid only if you set the RFMXNR_ATTR_PUSCH_PTRS_ENABLED attribute to True and RFMXNR_ATTR_PUSCH_TRANSFORM_PRECODING_ENABLED attribute to False. |
| RFMXNR_ATTR_PUSCH_PTRS_TIME_DENSITY | Specifies the density of PTRS in time domain. This attribute is valid only if you set the RFMXNR_ATTR_PUSCH_PTRS_ENABLED attribute to True. |

#### Attachments

None

Parent topic:

PTRS

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__component__carrier__bandwidth__part__user__pusch__ptrs__mapping_1gaedd477dde46232ec3f86d9905266b25e.html language=enus -->
## TOPIC 00060: RFMXNR_ATTR_PUSCH_PTRS_TIME_DENSITY

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__component__carrier__bandwidth__part__user__pusch__ptrs__mapping_1gaedd477dde46232ec3f86d9905266b25e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__component__carrier__bandwidth__part__user__pusch__ptrs__mapping_1gaedd477dde46232ec3f86d9905266b25e.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the density of PTRS in time domain. This attribute is valid only if you set the RFMXNR_ATTR_PUSCH_PTRS_ENABLED attribute to True. SyntaxRFMXNR_ATTR_PUSCH_PTRS_TIME_DENSITYNumeric ValueData TypeAccessApplies To9437276int32Read/WritePUSCHRemarks Use "pusch<<i>r</i>>" or "user<<i>l</i>>" or "

### RFMXNR_ATTR_PUSCH_PTRS_TIME_DENSITY

Specifies the density of PTRS in time domain. This attribute is valid only if you set the [RFMXNR_ATTR_PUSCH_PTRS_ENABLED](group____root__ni_r_fmx_n_r__attributes__component__carrier__bandwidth__part__user__pusch__ptrs_1gab9934b34bd136fc1a96b3d0b4a78f73c.html) attribute to **True**.

#### Syntax

RFMXNR_ATTR_PUSCH_PTRS_TIME_DENSITY

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9437276 | int32 | Read/Write | PUSCH |

#### Remarks

Use "pusch<<i>r</i>>" or "user<<i>l</i>>" or "bwp<<i>m</i>>" or "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>/bwp<<i>m</i>>/user<<i>l</i>>/pusch<<i>r</i>>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute.

The default value is **1**.

Parent topic:

Mapping

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__component__carrier__bandwidth__part__user__pusch__ptrs__transform__precoding__sequence.html language=enus -->
## TOPIC 00061: Transform Precoding Sequence

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__component__carrier__bandwidth__part__user__pusch__ptrs__transform__precoding__sequence.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__component__carrier__bandwidth__part__user__pusch__ptrs__transform__precoding__sequence.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXNR_ATTR_NUMBER_OF_PTRS_GROUPSSpecifies the number of PTRS groups per OFDM symbol. This attribute is valid only if you set the RFMXNR_ATTR_PUSCH_PTRS_ENABLED attribute to True and RFMXNR_ATTR_PUSCH_TRANSFORM_PRECODING_ENABLED attribute to True. RFMXNR_ATTR_SA

### Transform Precoding Sequence

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXNR_ATTR_NUMBER_OF_PTRS_GROUPS | Specifies the number of PTRS groups per OFDM symbol. This attribute is valid only if you set the RFMXNR_ATTR_PUSCH_PTRS_ENABLED attribute to True and RFMXNR_ATTR_PUSCH_TRANSFORM_PRECODING_ENABLED attribute to True. |
| RFMXNR_ATTR_SAMPLES_PER_PTRS_GROUP | Specifies the number of samples per each PTRS group. This attribute is valid only if you set the RFMXNR_ATTR_PUSCH_PTRS_ENABLED attribute to True and RFMXNR_ATTR_PUSCH_TRANSFORM_PRECODING_ENABLED attribute to True. |

#### Attachments

None

Parent topic:

PTRS

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__component__carrier__bandwidth__part__user__pusch__ptrs__transform__precoding__sequence_1ga92820ee5863c9a9626d641c707c110ef.html language=enus -->
## TOPIC 00062: RFMXNR_ATTR_NUMBER_OF_PTRS_GROUPS

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__component__carrier__bandwidth__part__user__pusch__ptrs__transform__precoding__sequence_1ga92820ee5863c9a9626d641c707c110ef.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__component__carrier__bandwidth__part__user__pusch__ptrs__transform__precoding__sequence_1ga92820ee5863c9a9626d641c707c110ef.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of PTRS groups per OFDM symbol. This attribute is valid only if you set the RFMXNR_ATTR_PUSCH_PTRS_ENABLED attribute to True and RFMXNR_ATTR_PUSCH_TRANSFORM_PRECODING_ENABLED attribute to True. SyntaxRFMXNR_ATTR_NUMBER_OF_PTRS_GROUPSNumeric ValueData TypeAccessApplies To9437274i

### RFMXNR_ATTR_NUMBER_OF_PTRS_GROUPS

Specifies the number of PTRS groups per OFDM symbol. This attribute is valid only if you set the [RFMXNR_ATTR_PUSCH_PTRS_ENABLED](group____root__ni_r_fmx_n_r__attributes__component__carrier__bandwidth__part__user__pusch__ptrs_1gab9934b34bd136fc1a96b3d0b4a78f73c.html) attribute to **True** and [RFMXNR_ATTR_PUSCH_TRANSFORM_PRECODING_ENABLED](group____root__ni_r_fmx_n_r__attributes__component__carrier__bandwidth__part__user__pusch_1gad7ce4fee08509163f2d28d1b44a2d42b.html) attribute to **True**.

#### Syntax

RFMXNR_ATTR_NUMBER_OF_PTRS_GROUPS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9437274 | int32 | Read/Write | PUSCH |

#### Remarks

Use "pusch<<i>r</i>>" or "user<<i>l</i>>" or "bwp<<i>m</i>>" or "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>/bwp<<i>m</i>>/user<<i>l</i>>/pusch<<i>r</i>>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute.

The default value is **2**.

Parent topic:

Transform Precoding Sequence

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__component__carrier__ssb_1ga04d6683f8233fc505f13a16615df00d4.html language=enus -->
## TOPIC 00063: RFMXNR_ATTR_PBCH_DMRS_POWER

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__component__carrier__ssb_1ga04d6683f8233fc505f13a16615df00d4.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__component__carrier__ssb_1ga04d6683f8233fc505f13a16615df00d4.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the power scaling value for the PBCH DMRS symbols in the SS/PBCH block. This value is expressed in dB. SyntaxRFMXNR_ATTR_PBCH_DMRS_POWERNumeric ValueData TypeAccessApplies To9437321float64Read/WriteCarrierRemarks Use "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>" as the Selector

### RFMXNR_ATTR_PBCH_DMRS_POWER

Specifies the power scaling value for the PBCH DMRS symbols in the SS/PBCH block. This value is expressed in dB.

#### Syntax

RFMXNR_ATTR_PBCH_DMRS_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9437321 | float64 | Read/Write | Carrier |

#### Remarks

Use "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute.

The default value is 0.

Parent topic:

SSB

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__component__carrier__ssb_1gadf7f1f63744ab8691d1cc471aab78021.html language=enus -->
## TOPIC 00064: RFMXNR_ATTR_SSB_GRID_SIZE

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__component__carrier__ssb_1gadf7f1f63744ab8691d1cc471aab78021.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__component__carrier__ssb_1gadf7f1f63744ab8691d1cc471aab78021.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the SSB resource grid size when you set the RFMXNR_ATTR_GRID_SIZE_MODE attribute to Manual. SyntaxRFMXNR_ATTR_SSB_GRID_SIZENumeric ValueData TypeAccessApplies To9437467int32Read/WriteCarrierRemarks Use "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>" as the Selector String to conf

### RFMXNR_ATTR_SSB_GRID_SIZE

Specifies the SSB resource grid size when you set the [RFMXNR_ATTR_GRID_SIZE_MODE](group____root__ni_r_fmx_n_r__attributes__advanced_1gaf653fc9b49c5ce185301fbb77d612665.html) attribute to **Manual**.

#### Syntax

RFMXNR_ATTR_SSB_GRID_SIZE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9437467 | int32 | Read/Write | Carrier |

#### Remarks

Use "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute.

Parent topic:

SSB

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__component__carrier__ssb_1gae624c04c50b29ef61f115bfbcac7e570.html language=enus -->
## TOPIC 00065: RFMXNR_ATTR_SSS_POWER

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__component__carrier__ssb_1gae624c04c50b29ef61f115bfbcac7e570.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__component__carrier__ssb_1gae624c04c50b29ef61f115bfbcac7e570.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the power scaling value for the secondary synchronization symbol in the SS/PBCH block. This value is expressed in dB. SyntaxRFMXNR_ATTR_SSS_POWERNumeric ValueData TypeAccessApplies To9437319float64Read/WriteCarrierRemarks Use "carrier<k>" or "subblock<n>carrier<k>" as the Selector String t

### RFMXNR_ATTR_SSS_POWER

Specifies the power scaling value for the secondary synchronization symbol in the SS/PBCH block. This value is expressed in dB.

#### Syntax

RFMXNR_ATTR_SSS_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9437319 | float64 | Read/Write | Carrier |

#### Remarks

Use "carrier<k>" or "subblock<n>carrier<k>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute.

The default value is 0.

Parent topic:

SSB

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__component__carrier__ssb_1gafab3a9dc203c72c6b503eb5a63934f3a.html language=enus -->
## TOPIC 00066: RFMXNR_ATTR_SSB_ACTIVE_BLOCKS

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__component__carrier__ssb_1gafab3a9dc203c72c6b503eb5a63934f3a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__component__carrier__ssb_1gafab3a9dc203c72c6b503eb5a63934f3a.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the SSB burst(s) indices for the SSB pattern that needs to be transmitted. SyntaxRFMXNR_ATTR_SSB_ACTIVE_BLOCKSNumeric ValueData TypeAccessApplies To9437333char[]Read/WriteCarrierRemarks Use "carrier<k>" or "subblock<n>carrier<k>" as the Selector String to configure or read this attribute.T

### RFMXNR_ATTR_SSB_ACTIVE_BLOCKS

Specifies the SSB burst(s) indices for the SSB pattern that needs to be transmitted.

#### Syntax

RFMXNR_ATTR_SSB_ACTIVE_BLOCKS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9437333 | char[] | Read/Write | Carrier |

#### Remarks

Use "carrier<k>" or "subblock<n>carrier<k>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute.

The default value is 0 - Last.

Parent topic:

SSB

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__list.html language=enus -->
## TOPIC 00067: List

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__list.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__list.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsStepGroup membersNameDescriptionRFMXNR_ATTR_NUMBER_OF_STEPSSpecifies the number of active steps in the list. AttachmentsNone

### List

#### Groups

- Step

#### Group members

| Name | Description |
| --- | --- |
| RFMXNR_ATTR_NUMBER_OF_STEPS | Specifies the number of active steps in the list. |

#### Attachments

None

Parent topic:

Attributes

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__list_1gaf5b94026c7b223102557ade33e0f604d.html language=enus -->
## TOPIC 00068: RFMXNR_ATTR_NUMBER_OF_STEPS

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__list_1gaf5b94026c7b223102557ade33e0f604d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__list_1gaf5b94026c7b223102557ade33e0f604d.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of active steps in the list. SyntaxRFMXNR_ATTR_NUMBER_OF_STEPSNumeric ValueData TypeAccessApplies To9441272int32Read/WriteN/ARemarks You need to use a selector string to configure or read this attribute for the list instance.The default value is 0.

### RFMXNR_ATTR_NUMBER_OF_STEPS

Specifies the number of active steps in the list.

#### Syntax

RFMXNR_ATTR_NUMBER_OF_STEPS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9441272 | int32 | Read/Write | N/A |

#### Remarks

You need to use a selector string to configure or read this attribute for the list instance.

The default value is 0.

Parent topic:

List

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__list__step_1ga981610188d5315472002608814be3bf1.html language=enus -->
## TOPIC 00069: RFMXNR_ATTR_LIST_STEP_TIMER_DURATION

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__list__step_1ga981610188d5315472002608814be3bf1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__list__step_1ga981610188d5315472002608814be3bf1.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the duration of a given list step in units specified by RFMXNR_ATTR_LIST_STEP_TIMER_UNIT. SyntaxRFMXNR_ATTR_LIST_STEP_TIMER_DURATIONNumeric ValueData TypeAccessApplies To9441273float64Read/WriteN/ARemarks You need to use a selector string to configure or read this attribute for the list st

### RFMXNR_ATTR_LIST_STEP_TIMER_DURATION

Specifies the duration of a given list step in units specified by [RFMXNR_ATTR_LIST_STEP_TIMER_UNIT](group____root__ni_r_fmx_n_r__attributes__list__step_1gafaddd41da6ff8920f155b07ba0f3d04e.html).

#### Syntax

RFMXNR_ATTR_LIST_STEP_TIMER_DURATION

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9441273 | float64 | Read/Write | N/A |

#### Remarks

You need to use a selector string to configure or read this attribute for the list step instance.

The default value is 0.

Parent topic:

Step

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__list__step_1ga9cf9a8501bcd23e8d9ff4d54addb95c9.html language=enus -->
## TOPIC 00070: RFMXNR_ATTR_LIST_STEP_TIMER_OFFSET

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__list__step_1ga9cf9a8501bcd23e8d9ff4d54addb95c9.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__list__step_1ga9cf9a8501bcd23e8d9ff4d54addb95c9.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the offset from the start of the step for which the measurements are computed. The unit for this attribute is specified by RFMXNR_ATTR_LIST_STEP_TIMER_UNIT. This attribute is valid only when you set the RFMXNR_ATTR_DIGITAL_EDGE_TRIGGER_SOURCE attribute to TimerEvent. SyntaxRFMXNR_ATTR_LIST

### RFMXNR_ATTR_LIST_STEP_TIMER_OFFSET

Specifies the offset from the start of the step for which the measurements are computed. The unit for this attribute is specified by [RFMXNR_ATTR_LIST_STEP_TIMER_UNIT](group____root__ni_r_fmx_n_r__attributes__list__step_1gafaddd41da6ff8920f155b07ba0f3d04e.html). This attribute is valid only when you set the [RFMXNR_ATTR_DIGITAL_EDGE_TRIGGER_SOURCE](group____root__ni_r_fmx_n_r__attributes__trigger__digital__edge_1ga5f52176056e8261e00a5ed6c8338b698.html) attribute to **TimerEvent**.

#### Syntax

RFMXNR_ATTR_LIST_STEP_TIMER_OFFSET

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9441271 | float64 | Read/Write | N/A |

#### Remarks

You need to use a selector string to configure or read this attribute for the list step instance.

The default value is 0.

Parent topic:

Step

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__list__step_1gafaddd41da6ff8920f155b07ba0f3d04e.html language=enus -->
## TOPIC 00071: RFMXNR_ATTR_LIST_STEP_TIMER_UNIT

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__list__step_1gafaddd41da6ff8920f155b07ba0f3d04e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__list__step_1gafaddd41da6ff8920f155b07ba0f3d04e.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the units in which RFMXNR_ATTR_LIST_STEP_TIMER_DURATION and RFMXNR_ATTR_LIST_STEP_TIMER_OFFSET are specified. SyntaxRFMXNR_ATTR_LIST_STEP_TIMER_UNITNumeric ValueData TypeAccessApplies To9441270int32Read/WriteN/ARemarks You need to use a selector string to configure or read this attribute f

### RFMXNR_ATTR_LIST_STEP_TIMER_UNIT

Specifies the units in which [RFMXNR_ATTR_LIST_STEP_TIMER_DURATION](group____root__ni_r_fmx_n_r__attributes__list__step_1ga981610188d5315472002608814be3bf1.html) and [RFMXNR_ATTR_LIST_STEP_TIMER_OFFSET](group____root__ni_r_fmx_n_r__attributes__list__step_1ga9cf9a8501bcd23e8d9ff4d54addb95c9.html) are specified.

#### Syntax

RFMXNR_ATTR_LIST_STEP_TIMER_UNIT

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9441270 | int32 | Read/Write | N/A |

#### Remarks

You need to use a selector string to configure or read this attribute for the list step instance.

The default value is **Slot**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXNR_VAL_LIST_STEP_TIMER_UNIT_SLOT | 1 (0x1) | List Step Timer Duration and List Step Timer Offset are specified in units of slots. |
| RFMXNR_VAL_LIST_STEP_TIMER_UNIT_TIME | 6 (0x6) | List Step Timer Duration and List Step Timer Offset are specified in seconds. Specify the List Step Timer Duration and List Step Timer Offset in multiples of 1 ms * (15 kHz/minimum subcarrier spacing of all carriers). All slots within this notional time duration are analysed. |

Parent topic:

Step

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__modacc.html language=enus -->
## TOPIC 00072: ModAcc

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__modacc.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__modacc.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsAuto LevelAveragingComposite ResultsIQ ImpairmentsNoise CompensationResultsShort FrameTransientGroup membersNameDescriptionRFMXNR_ATTR_MODACC_ALL_TRACES_ENABLEDSpecifies whether to enable the traces to be stored and retrieved after performing the ModAcc measurement. RFMXNR_ATTR_MODACC_CHANNEL_

### ModAcc

#### Groups

- Auto Level
- Averaging
- Composite Results
- IQ Impairments
- Noise Compensation
- Results
- Short Frame
- Transient

#### Group members

| Name | Description |
| --- | --- |
| RFMXNR_ATTR_MODACC_ALL_TRACES_ENABLED | Specifies whether to enable the traces to be stored and retrieved after performing the ModAcc measurement. |
| RFMXNR_ATTR_MODACC_CHANNEL_ESTIMATION_TYPE | Specifies the method used for channel estimation. |
| RFMXNR_ATTR_MODACC_COMMON_CLOCK_SOURCE_ENABLED | Specifies whether same reference clock is used for local oscillator and digital-to-analog converter. When same reference clock is used the Carrier Frequency Offset is proportional to Sample Clock Error. |
| RFMXNR_ATTR_MODACC_DC_SUBCARRIER_REMOVAL_ENABLED | Specifies whether the DC subcarrier is removed from the EVM results. |
| RFMXNR_ATTR_MODACC_EVM_REFERENCE_DATA_SYMBOLS_MODE | Specifies whether to either use a reference waveform or an acquired waveform to create reference data symbols for EVM computation. |
| RFMXNR_ATTR_MODACC_EVM_UNIT | Specifies the units of the EVM results. |
| RFMXNR_ATTR_MODACC_FFT_WINDOW_LENGTH | Specifies the FFT window length (W). This value is expressed as a percentage of the cyclic prefix length. This attribute is used when you set the RFMXNR_ATTR_MODACC_FFT_WINDOW_TYPE attribute to 3GPP, where it is needed to calculate the EVM using two different FFT window positions, Delta_C-W/2, and Delta_C+W/2. |
| RFMXNR_ATTR_MODACC_FFT_WINDOW_OFFSET | Specifies the position of the FFT window used to calculate the EVM when RFMXNR_ATTR_MODACC_FFT_WINDOW_TYPE attribute is set to Custom. The offset is expressed as a percentage of the cyclic prefix length. If you set this attribute to 0, the EVM window starts at the end of cyclic prefix. If you set this attribute to 100, the EVM window starts at the beginning of cyclic prefix. |
| RFMXNR_ATTR_MODACC_FFT_WINDOW_TYPE | Specifies the FFT window type used for EVM calculation. |
| RFMXNR_ATTR_MODACC_FREQUENCY_ERROR_ESTIMATION | Specifies the operation mode of frequency error estimation. |
| RFMXNR_ATTR_MODACC_MAGNITUDE_AND_PHASE_ERROR_ENABLED | Specifies whether to measure the magnitude and the phase error. |
| RFMXNR_ATTR_MODACC_MEASUREMENT_ENABLED | Specifies whether to enable the ModAcc measurement. |
| RFMXNR_ATTR_MODACC_MEASUREMENT_LENGTH | Specifies the measurement length in units specified by RFMXNR_ATTR_MODACC_MEASUREMENT_LENGTH_UNIT attribute. |
| RFMXNR_ATTR_MODACC_MEASUREMENT_LENGTH_UNIT | Specifies the units in which measurement offset and measurement length are specified. |
| RFMXNR_ATTR_MODACC_MEASUREMENT_MODE | Specifies whether the measurement should calibrate the noise floor of the analyzer or perform the ModAcc measurement. |
| RFMXNR_ATTR_MODACC_MEASUREMENT_OFFSET | Specifies the measurement offset to skip from the synchronization boundary. The synchronization boundary is specified by the RFMXNR_ATTR_MODACC_SYNCHRONIZATION_MODE attribute. The unit for this is specified by RFMXNR_ATTR_MODACC_MEASUREMENT_LENGTH_UNIT. |
| RFMXNR_ATTR_MODACC_MULTICARRIER_FILTER_ENABLED | Specifies whether to use the filter in single carrier configurations to minimize leakage into the carrier. Measurement ignores this attribute, if number of carriers is set to more than 1 or if you set the RFMXNR_ATTR_ACQUISITION_BANDWIDTH_OPTIMIZATION_ENABLED attribute to False, where in the multi carrier filter will always be used. |
| RFMXNR_ATTR_MODACC_NUMBER_OF_ANALYSIS_THREADS | Specifies the maximum number of threads used for parallelism for the ModAcc measurement. |
| RFMXNR_ATTR_MODACC_PHASE_TRACKING_MODE | Specifies the method used for phase tracking. |
| RFMXNR_ATTR_MODACC_PRE_FFT_ERROR_ESTIMATION_INTERVAL | Specifies the interval used for Pre-FFT error estimation. |
| RFMXNR_ATTR_MODACC_SPECTRAL_FLATNESS_CONDITION | Specifies the test condition for Spectral Flatness measurement. |
| RFMXNR_ATTR_MODACC_SPECTRUM_INVERTED | Specifies whether the spectrum of the signal being measured is inverted. This happens when I and Q component of the baseband complex signal is swapped. |
| RFMXNR_ATTR_MODACC_SYMBOL_CLOCK_ERROR_ESTIMATION_ENABLED | Specifies whether to estimate symbol clock error. |
| RFMXNR_ATTR_MODACC_SYNCHRONIZATION_MODE | Specifies whether the measurement is performed from slot or frame boundary. |
| RFMXNR_ATTR_MODACC_TIMING_TRACKING_MODE | Specifies the method used for timing tracking. |

#### Attachments

None

Parent topic:

Attributes

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__modacc_1ga192f71ad472ccc9c027d313ee757f6dc.html language=enus -->
## TOPIC 00073: RFMXNR_ATTR_MODACC_MAGNITUDE_AND_PHASE_ERROR_ENABLED

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__modacc_1ga192f71ad472ccc9c027d313ee757f6dc.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__modacc_1ga192f71ad472ccc9c027d313ee757f6dc.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to measure the magnitude and the phase error. SyntaxRFMXNR_ATTR_MODACC_MAGNITUDE_AND_PHASE_ERROR_ENABLEDNumeric ValueData TypeAccessApplies To9453688int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instanc

### RFMXNR_ATTR_MODACC_MAGNITUDE_AND_PHASE_ERROR_ENABLED

Specifies whether to measure the magnitude and the phase error.

#### Syntax

RFMXNR_ATTR_MODACC_MAGNITUDE_AND_PHASE_ERROR_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9453688 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **True**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXNR_VAL_MODACC_MAGNITUDE_AND_PHASE_ERROR_ENABLED_FALSE | 0 (0x0) | Indicates that magnitude error and phase error results computation is disabled. |
| RFMXNR_VAL_MODACC_MAGNITUDE_AND_PHASE_ERROR_ENABLED_TRUE | 1 (0x1) | Indicates that magnitude error and phase error results computation is enabled. |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__modacc_1ga281f8f1b87901d8a5701ff4772ab930f.html language=enus -->
## TOPIC 00074: RFMXNR_ATTR_MODACC_SPECTRAL_FLATNESS_CONDITION

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__modacc_1ga281f8f1b87901d8a5701ff4772ab930f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__modacc_1ga281f8f1b87901d8a5701ff4772ab930f.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the test condition for Spectral Flatness measurement. SyntaxRFMXNR_ATTR_MODACC_SPECTRAL_FLATNESS_CONDITIONNumeric ValueData TypeAccessApplies To9453584int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Ref

### RFMXNR_ATTR_MODACC_SPECTRAL_FLATNESS_CONDITION

Specifies the test condition for Spectral Flatness measurement.

#### Syntax

RFMXNR_ATTR_MODACC_SPECTRAL_FLATNESS_CONDITION

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9453584 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **Normal**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXNR_VAL_MODACC_SPECTRAL_FLATNESS_CONDITION_NORMAL | 0 (0x0) | Frequency range and maximum ripple defined in the section 6.4.2.4.1, Table 6.4.2.4.1-1 of 3GPP 38.101-1 and section 6.4.2.4.1, Table 6.4.2.4.1-1 of 3GPP 38.101-2 are used. |
| RFMXNR_VAL_MODACC_SPECTRAL_FLATNESS_CONDITION_EXTREME | 1 (0x1) | Frequency range and maximum ripple defined in the section 6.4.2.4.1, Table 6.4.2.4.1-2 of 3GPP 38.101-1 and section 6.4.2.4.1, Table 6.4.2.4.1-2 of 3GPP 38.101-2 are used. |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__modacc_1ga2ae3e936bf56a93cdfbec5bc42b352b3.html language=enus -->
## TOPIC 00075: RFMXNR_ATTR_MODACC_MEASUREMENT_LENGTH_UNIT

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__modacc_1ga2ae3e936bf56a93cdfbec5bc42b352b3.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__modacc_1ga2ae3e936bf56a93cdfbec5bc42b352b3.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the units in which measurement offset and measurement length are specified. SyntaxRFMXNR_ATTR_MODACC_MEASUREMENT_LENGTH_UNITNumeric ValueData TypeAccessApplies To9453573int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default si

### RFMXNR_ATTR_MODACC_MEASUREMENT_LENGTH_UNIT

Specifies the units in which measurement offset and measurement length are specified.

#### Syntax

RFMXNR_ATTR_MODACC_MEASUREMENT_LENGTH_UNIT

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9453573 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **Slot**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXNR_VAL_MODACC_MEASUREMENT_LENGTH_UNIT_SLOT | 1 (0x1) | Measurement offset and measurement length are specified in units of slots. |
| RFMXNR_VAL_MODACC_MEASUREMENT_LENGTH_UNIT_SUBFRAME | 3 (0x3) | Measurement offset and measurement length are specified in units of subframes. |
| RFMXNR_VAL_MODACC_MEASUREMENT_LENGTH_UNIT_TIME | 6 (0x6) | Measurement offset and measurement length are specified in seconds. Specify the measurement offset and length in multiples of 1 ms * (15 kHz/minimum subcarrier spacing of all carriers). All slots within this notional time duration are analysed. |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__modacc_1ga2b041f0c7f1a3eaca3b857f4317a4801.html language=enus -->
## TOPIC 00076: RFMXNR_ATTR_MODACC_DC_SUBCARRIER_REMOVAL_ENABLED

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__modacc_1ga2b041f0c7f1a3eaca3b857f4317a4801.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__modacc_1ga2b041f0c7f1a3eaca3b857f4317a4801.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the DC subcarrier is removed from the EVM results. SyntaxRFMXNR_ATTR_MODACC_DC_SUBCARRIER_REMOVAL_ENABLEDNumeric ValueData TypeAccessApplies To9437231int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instan

### RFMXNR_ATTR_MODACC_DC_SUBCARRIER_REMOVAL_ENABLED

Specifies whether the DC subcarrier is removed from the EVM results.

#### Syntax

RFMXNR_ATTR_MODACC_DC_SUBCARRIER_REMOVAL_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9437231 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **True**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXNR_VAL_MODACC_DC_SUBCARRIER_REMOVAL_ENABLED_FALSE | 0 (0x0) | The DC subcarrier is present in the EVM results. |
| RFMXNR_VAL_MODACC_DC_SUBCARRIER_REMOVAL_ENABLED_TRUE | 1 (0x1) | The DC subcarrier is removed from the EVM results. |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__modacc_1ga2de06b4f0e480e69fdbfd0d719128c6d.html language=enus -->
## TOPIC 00077: RFMXNR_ATTR_MODACC_EVM_REFERENCE_DATA_SYMBOLS_MODE

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__modacc_1ga2de06b4f0e480e69fdbfd0d719128c6d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__modacc_1ga2de06b4f0e480e69fdbfd0d719128c6d.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to either use a reference waveform or an acquired waveform to create reference data symbols for EVM computation. SyntaxRFMXNR_ATTR_MODACC_EVM_REFERENCE_DATA_SYMBOLS_MODENumeric ValueData TypeAccessApplies To9453697int32Read/WriteN/ARemarks You do not need to use a selector string t

### RFMXNR_ATTR_MODACC_EVM_REFERENCE_DATA_SYMBOLS_MODE

Specifies whether to either use a reference waveform or an acquired waveform to create reference data symbols for EVM computation.

#### Syntax

RFMXNR_ATTR_MODACC_EVM_REFERENCE_DATA_SYMBOLS_MODE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9453697 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **Acquired Waveform**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXNR_VAL_MODACC_EVM_REFERENCE_DATA_SYMBOLS_MODE_ACQUIRED_WAVEFORM | 0 (0x0) | Indicates that reference data symbols for EVM computation are created using the acquired waveform. |
| RFMXNR_VAL_MODACC_EVM_REFERENCE_DATA_SYMBOLS_MODE_REFERENCE_WAVEFORM | 1 (0x1) | Indicates that reference data symbols for EVM computation are created using the reference waveform. |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__modacc_1ga405c4854ffabe66c4536d00694ab9f99.html language=enus -->
## TOPIC 00078: RFMXNR_ATTR_MODACC_SYMBOL_CLOCK_ERROR_ESTIMATION_ENABLED

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__modacc_1ga405c4854ffabe66c4536d00694ab9f99.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__modacc_1ga405c4854ffabe66c4536d00694ab9f99.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to estimate symbol clock error. SyntaxRFMXNR_ATTR_MODACC_SYMBOL_CLOCK_ERROR_ESTIMATION_ENABLEDNumeric ValueData TypeAccessApplies To9453685int32Read/WriteN/ARemarks This attribute is ignored when the RFMXNR_ATTR_MODACC_COMMON_CLOCK_SOURCE_ENABLED attribute is True and the RFMXNR_AT

### RFMXNR_ATTR_MODACC_SYMBOL_CLOCK_ERROR_ESTIMATION_ENABLED

Specifies whether to estimate symbol clock error.

#### Syntax

RFMXNR_ATTR_MODACC_SYMBOL_CLOCK_ERROR_ESTIMATION_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9453685 | int32 | Read/Write | N/A |

#### Remarks

This attribute is ignored when the [RFMXNR_ATTR_MODACC_COMMON_CLOCK_SOURCE_ENABLED](group____root__ni_r_fmx_n_r__attributes__modacc_1gaeb60ebea5098df95681f13ffa8e066bd.html) attribute is **True** and the [RFMXNR_ATTR_MODACC_FREQUENCY_ERROR_ESTIMATION](group____root__ni_r_fmx_n_r__attributes__modacc_1gab93ba7fc3550a369c1d8e7275eae6922.html) attribute is **Disabled**, in which case, symbol clock error is not estimated.

If symbol clock error is absent in the signal to be analyzed, you may disable symbol clock error estimation to reduce measurement time or to avoid measurement inaccuracy due to error in symbol clock error estimation.

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **True**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXNR_VAL_MODACC_SYMBOL_CLOCK_ERROR_ESTIMATION_ENABLED_FALSE | 0 (0x0) | Indicates that symbol clock error estimation and correction is disabled. |
| RFMXNR_VAL_MODACC_SYMBOL_CLOCK_ERROR_ESTIMATION_ENABLED_TRUE | 1 (0x1) | Indicates that symbol clock error estimation and correction is enabled. |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__modacc_1ga446b1f8a384f6d9cbe087eb4a230256f.html language=enus -->
## TOPIC 00079: RFMXNR_ATTR_MODACC_MEASUREMENT_LENGTH

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__modacc_1ga446b1f8a384f6d9cbe087eb4a230256f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__modacc_1ga446b1f8a384f6d9cbe087eb4a230256f.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the measurement length in units specified by RFMXNR_ATTR_MODACC_MEASUREMENT_LENGTH_UNIT attribute. SyntaxRFMXNR_ATTR_MODACC_MEASUREMENT_LENGTHNumeric ValueData TypeAccessApplies To9453575float64Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribut

### RFMXNR_ATTR_MODACC_MEASUREMENT_LENGTH

Specifies the measurement length in units specified by [RFMXNR_ATTR_MODACC_MEASUREMENT_LENGTH_UNIT](group____root__ni_r_fmx_n_r__attributes__modacc_1ga2ae3e936bf56a93cdfbec5bc42b352b3.html) attribute.

#### Syntax

RFMXNR_ATTR_MODACC_MEASUREMENT_LENGTH

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9453575 | float64 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 1.

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__modacc_1ga55c49142f4bf31826c88c276655ae98e.html language=enus -->
## TOPIC 00080: RFMXNR_ATTR_MODACC_MEASUREMENT_OFFSET

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__modacc_1ga55c49142f4bf31826c88c276655ae98e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__modacc_1ga55c49142f4bf31826c88c276655ae98e.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the measurement offset to skip from the synchronization boundary. The synchronization boundary is specified by the RFMXNR_ATTR_MODACC_SYNCHRONIZATION_MODE attribute. The unit for this is specified by RFMXNR_ATTR_MODACC_MEASUREMENT_LENGTH_UNIT. SyntaxRFMXNR_ATTR_MODACC_MEASUREMENT_OFFSETNum

### RFMXNR_ATTR_MODACC_MEASUREMENT_OFFSET

Specifies the measurement offset to skip from the synchronization boundary. The synchronization boundary is specified by the [RFMXNR_ATTR_MODACC_SYNCHRONIZATION_MODE](group____root__ni_r_fmx_n_r__attributes__modacc_1gaf8a074716a9c49e6962eaf1b2e78ba50.html) attribute. The unit for this is specified by [RFMXNR_ATTR_MODACC_MEASUREMENT_LENGTH_UNIT](group____root__ni_r_fmx_n_r__attributes__modacc_1ga2ae3e936bf56a93cdfbec5bc42b352b3.html).

#### Syntax

RFMXNR_ATTR_MODACC_MEASUREMENT_OFFSET

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9453574 | float64 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 0.

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__modacc_1ga5c5effdf31eec2bad0c512f37adcab57.html language=enus -->
## TOPIC 00081: RFMXNR_ATTR_MODACC_CHANNEL_ESTIMATION_TYPE

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__modacc_1ga5c5effdf31eec2bad0c512f37adcab57.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__modacc_1ga5c5effdf31eec2bad0c512f37adcab57.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the method used for channel estimation. SyntaxRFMXNR_ATTR_MODACC_CHANNEL_ESTIMATION_TYPENumeric ValueData TypeAccessApplies To9453577int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector

### RFMXNR_ATTR_MODACC_CHANNEL_ESTIMATION_TYPE

Specifies the method used for channel estimation.

#### Syntax

RFMXNR_ATTR_MODACC_CHANNEL_ESTIMATION_TYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9453577 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **Reference+Data**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXNR_VAL_MODACC_CHANNEL_ESTIMATION_TYPE_REFERENCE | 0 (0x0) | Only demodulation reference (DMRS) symbol is used to calculate channel coefficients. |
| RFMXNR_VAL_MODACC_CHANNEL_ESTIMATION_TYPE_REFERENCE_AND_DATA | 1 (0x1) | Both demodulation reference (DMRS) and data symbols are used to calculate channel coefficients. This method is as per definition of 3GPP NR specification. |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__modacc_1ga5def43a36b5c6e0217eabeae9a7b55bd.html language=enus -->
## TOPIC 00082: RFMXNR_ATTR_MODACC_MULTICARRIER_FILTER_ENABLED

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__modacc_1ga5def43a36b5c6e0217eabeae9a7b55bd.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__modacc_1ga5def43a36b5c6e0217eabeae9a7b55bd.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to use the filter in single carrier configurations to minimize leakage into the carrier. Measurement ignores this attribute, if number of carriers is set to more than 1 or if you set the RFMXNR_ATTR_ACQUISITION_BANDWIDTH_OPTIMIZATION_ENABLED attribute to False, where in the multi c

### RFMXNR_ATTR_MODACC_MULTICARRIER_FILTER_ENABLED

Specifies whether to use the filter in single carrier configurations to minimize leakage into the carrier. Measurement ignores this attribute, if number of carriers is set to more than 1 or if you set the [RFMXNR_ATTR_ACQUISITION_BANDWIDTH_OPTIMIZATION_ENABLED](group____root__ni_r_fmx_n_r__attributes__advanced_1gaa090211e5557a12a06071b5f2fb6b227.html) attribute to **False**, where in the multi carrier filter will always be used.

#### Syntax

RFMXNR_ATTR_MODACC_MULTICARRIER_FILTER_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9453570 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **False**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXNR_VAL_MODACC_MULTICARRIER_FILTER_ENABLED_FALSE | 0 (0x0) | Measurement doesn't use the filter. |
| RFMXNR_VAL_MODACC_MULTICARRIER_FILTER_ENABLED_TRUE | 1 (0x1) | Measurement filters out unwanted emissions. |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__modacc_1ga99869aa8b87a1e8bb2d5bf45288560c9.html language=enus -->
## TOPIC 00083: RFMXNR_ATTR_MODACC_EVM_UNIT

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__modacc_1ga99869aa8b87a1e8bb2d5bf45288560c9.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__modacc_1ga99869aa8b87a1e8bb2d5bf45288560c9.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the units of the EVM results. SyntaxRFMXNR_ATTR_MODACC_EVM_UNITNumeric ValueData TypeAccessApplies To9453578int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector String topic for informa

### RFMXNR_ATTR_MODACC_EVM_UNIT

Specifies the units of the EVM results.

#### Syntax

RFMXNR_ATTR_MODACC_EVM_UNIT

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9453578 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **Percentage**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXNR_VAL_MODACC_EVM_UNIT_PERCENTAGE | 0 (0x0) | The EVM is reported as a percentage. |
| RFMXNR_VAL_MODACC_EVM_UNIT_DB | 1 (0x1) | The EVM is reported in dB. |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__modacc_1gab93ba7fc3550a369c1d8e7275eae6922.html language=enus -->
## TOPIC 00084: RFMXNR_ATTR_MODACC_FREQUENCY_ERROR_ESTIMATION

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__modacc_1gab93ba7fc3550a369c1d8e7275eae6922.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__modacc_1gab93ba7fc3550a369c1d8e7275eae6922.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the operation mode of frequency error estimation. SyntaxRFMXNR_ATTR_MODACC_FREQUENCY_ERROR_ESTIMATIONNumeric ValueData TypeAccessApplies To9453681int32Read/WriteN/ARemarks If frequency error is absent in the signal to be analyzed, you may disable frequency estimation to reduce measurement

### RFMXNR_ATTR_MODACC_FREQUENCY_ERROR_ESTIMATION

Specifies the operation mode of frequency error estimation.

#### Syntax

RFMXNR_ATTR_MODACC_FREQUENCY_ERROR_ESTIMATION

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9453681 | int32 | Read/Write | N/A |

#### Remarks

If frequency error is absent in the signal to be analyzed, you may disable frequency estimation to reduce measurement time or to avoid measurement inaccuracy due to error in frequency error estimation.

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **Normal**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXNR_VAL_MODACC_FREQUENCY_ERROR_ESTIMATION_DISABLED | 0 (0x0) | Frequency error estimation and correction is disabled. |
| RFMXNR_VAL_MODACC_FREQUENCY_ERROR_ESTIMATION_NORMAL | 1 (0x1) | Estimate and correct frequency error of range +/- half subcarrier spacing. |
| RFMXNR_VAL_MODACC_FREQUENCY_ERROR_ESTIMATION_WIDE | 2 (0x2) | Estimate and correct frequency error of range +/- half resource block when RFMXNR_ATTR_AUTO_RESOURCE_BLOCK_DETECTION_ENABLED is True, or range +/- number of guard subcarrier when RFMXNR_ATTR_AUTO_RESOURCE_BLOCK_DETECTION_ENABLED is False. |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__modacc_1gabf76b716ebc7f51e70635c0b3c8f2784.html language=enus -->
## TOPIC 00085: RFMXNR_ATTR_MODACC_TIMING_TRACKING_MODE

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__modacc_1gabf76b716ebc7f51e70635c0b3c8f2784.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__modacc_1gabf76b716ebc7f51e70635c0b3c8f2784.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the method used for timing tracking. SyntaxRFMXNR_ATTR_MODACC_TIMING_TRACKING_MODENumeric ValueData TypeAccessApplies To9453650int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strin

### RFMXNR_ATTR_MODACC_TIMING_TRACKING_MODE

Specifies the method used for timing tracking.

#### Syntax

RFMXNR_ATTR_MODACC_TIMING_TRACKING_MODE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9453650 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **Reference+Data**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXNR_VAL_MODACC_TIMING_TRACKING_MODE_DISABLED | 0 (0x0) | Disables the timing tracking. |
| RFMXNR_VAL_MODACC_TIMING_TRACKING_MODE_REFERENCE_AND_DATA | 1 (0x1) | All reference and data symbols are used for timing tracking. |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__modacc_1gac53fdbca54dd8d3d705e193239f9805b.html language=enus -->
## TOPIC 00086: RFMXNR_ATTR_MODACC_PHASE_TRACKING_MODE

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__modacc_1gac53fdbca54dd8d3d705e193239f9805b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__modacc_1gac53fdbca54dd8d3d705e193239f9805b.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the method used for phase tracking. SyntaxRFMXNR_ATTR_MODACC_PHASE_TRACKING_MODENumeric ValueData TypeAccessApplies To9453649int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector String

### RFMXNR_ATTR_MODACC_PHASE_TRACKING_MODE

Specifies the method used for phase tracking.

#### Syntax

RFMXNR_ATTR_MODACC_PHASE_TRACKING_MODE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9453649 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **Reference+Data**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXNR_VAL_MODACC_PHASE_TRACKING_MODE_DISABLED | 0 (0x0) | Disables the phase tracking. |
| RFMXNR_VAL_MODACC_PHASE_TRACKING_MODE_REFERENCE_AND_DATA | 1 (0x1) | All reference and data symbols are used for phase tracking. |
| RFMXNR_VAL_MODACC_PHASE_TRACKING_MODE_PTRS | 2 (0x2) | Only PTRS symbols are used for phase tracking. |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__modacc_1gaeb60ebea5098df95681f13ffa8e066bd.html language=enus -->
## TOPIC 00087: RFMXNR_ATTR_MODACC_COMMON_CLOCK_SOURCE_ENABLED

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__modacc_1gaeb60ebea5098df95681f13ffa8e066bd.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__modacc_1gaeb60ebea5098df95681f13ffa8e066bd.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether same reference clock is used for local oscillator and digital-to-analog converter. When same reference clock is used the Carrier Frequency Offset is proportional to Sample Clock Error. SyntaxRFMXNR_ATTR_MODACC_COMMON_CLOCK_SOURCE_ENABLEDNumeric ValueData TypeAccessApplies To9453582

### RFMXNR_ATTR_MODACC_COMMON_CLOCK_SOURCE_ENABLED

Specifies whether same reference clock is used for local oscillator and digital-to-analog converter. When same reference clock is used the Carrier Frequency Offset is proportional to Sample Clock Error.

#### Syntax

RFMXNR_ATTR_MODACC_COMMON_CLOCK_SOURCE_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9453582 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **True**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXNR_VAL_MODACC_COMMON_CLOCK_SOURCE_ENABLED_FALSE | 0 (0x0) | The Sample Clock error is estimated independently. |
| RFMXNR_VAL_MODACC_COMMON_CLOCK_SOURCE_ENABLED_TRUE | 1 (0x1) | The Sample Clock error is estimated from carrier frequency offset. |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__modacc_1gaf7d4eab3b86bece122845fbff14ca19f.html language=enus -->
## TOPIC 00088: RFMXNR_ATTR_MODACC_FFT_WINDOW_TYPE

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__modacc_1gaf7d4eab3b86bece122845fbff14ca19f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__modacc_1gaf7d4eab3b86bece122845fbff14ca19f.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the FFT window type used for EVM calculation. SyntaxRFMXNR_ATTR_MODACC_FFT_WINDOW_TYPENumeric ValueData TypeAccessApplies To9453579int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector S

### RFMXNR_ATTR_MODACC_FFT_WINDOW_TYPE

Specifies the FFT window type used for EVM calculation.

#### Syntax

RFMXNR_ATTR_MODACC_FFT_WINDOW_TYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9453579 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **Custom**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXNR_VAL_MODACC_FFT_WINDOW_TYPE_3GPP | 0 (0x0) | The maximum EVM between the start window position and the end window position is returned according to the 3GPP specification. The FFT window positions are specified by the RFMXNR_ATTR_MODACC_MEASUREMENT_LENGTH_UNIT attribute. |
| RFMXNR_VAL_MODACC_FFT_WINDOW_TYPE_CUSTOM | 1 (0x1) | Only one FFT window position is used for the EVM calculation. FFT window position is specified by RFMXNR_ATTR_MODACC_FFT_WINDOW_OFFSET attribute. |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__modacc__iq__impairments_1ga7de4bd71792ecc7eb25c2a84e6c2ca01.html language=enus -->
## TOPIC 00089: RFMXNR_ATTR_MODACC_IQ_QUADRATURE_ERROR_CORRECTION_ENABLED

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__modacc__iq__impairments_1ga7de4bd71792ecc7eb25c2a84e6c2ca01.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__modacc__iq__impairments_1ga7de4bd71792ecc7eb25c2a84e6c2ca01.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable IQ quadrature error correction. SyntaxRFMXNR_ATTR_MODACC_IQ_QUADRATURE_ERROR_CORRECTION_ENABLEDNumeric ValueData TypeAccessApplies To9453700int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instan

### RFMXNR_ATTR_MODACC_IQ_QUADRATURE_ERROR_CORRECTION_ENABLED

Specifies whether to enable IQ quadrature error correction.

#### Syntax

RFMXNR_ATTR_MODACC_IQ_QUADRATURE_ERROR_CORRECTION_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9453700 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **False**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXNR_VAL_MODACC_IQ_QUADRATURE_ERROR_CORRECTION_ENABLED_FALSE | 0 (0x0) | IQ quadrature error correction is disabled. |
| RFMXNR_VAL_MODACC_IQ_QUADRATURE_ERROR_CORRECTION_ENABLED_TRUE | 1 (0x1) | IQ quadrature error correction is enabled. |

Parent topic:

IQ Impairments

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__modacc__noise__compensation_1ga9aeef23b856f22c437389bafa3e82a2e.html language=enus -->
## TOPIC 00090: RFMXNR_ATTR_MODACC_NOISE_COMPENSATION_ENABLED

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__modacc__noise__compensation_1ga9aeef23b856f22c437389bafa3e82a2e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__modacc__noise__compensation_1ga9aeef23b856f22c437389bafa3e82a2e.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the contribution of the instrument noise is compensated for EVM computation. SyntaxRFMXNR_ATTR_MODACC_NOISE_COMPENSATION_ENABLEDNumeric ValueData TypeAccessApplies To9453714int32Read/WriteN/ARemarks You must measure the noise floor before applying the noise compensation. The instru

### RFMXNR_ATTR_MODACC_NOISE_COMPENSATION_ENABLED

Specifies whether the contribution of the instrument noise is compensated for EVM computation.

#### Syntax

RFMXNR_ATTR_MODACC_NOISE_COMPENSATION_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9453714 | int32 | Read/Write | N/A |

#### Remarks

You must measure the noise floor before applying the noise compensation. The instrument noise floor is measured for the RF path used by the ModAcc measurement and cached for future use.

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

Supported devices are NI 5831 and NI 5840/41. The default value is **False**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXNR_VAL_MODACC_NOISE_COMPENSATION_ENABLED_FALSE | 0 (0x0) | Noise compensation is disabled for the measurement. |
| RFMXNR_VAL_MODACC_NOISE_COMPENSATION_ENABLED_TRUE | 1 (0x1) | Noise compensation is enabled for the measurement. |

Parent topic:

Noise Compensation

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__modacc__results_1ga02b5c4537c6eb93cd29368f28acda7e1.html language=enus -->
## TOPIC 00091: RFMXNR_ATTR_MODACC_RESULTS_COMPONENT_CARRIER_SYMBOL_CLOCK_ERROR_MEAN

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__modacc__results_1ga02b5c4537c6eb93cd29368f28acda7e1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__modacc__results_1ga02b5c4537c6eb93cd29368f28acda7e1.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the estimated sample clock error averaged over measurement length. This value is expressed in ppm. SyntaxRFMXNR_ATTR_MODACC_RESULTS_COMPONENT_CARRIER_SYMBOL_CLOCK_ERROR_MEANNumeric ValueData TypeAccessApplies To9453619float64Read-OnlyChainRemarks Use "carrier<k>" or "subblock<n>" or "subbloc

### RFMXNR_ATTR_MODACC_RESULTS_COMPONENT_CARRIER_SYMBOL_CLOCK_ERROR_MEAN

Returns the estimated sample clock error averaged over measurement length. This value is expressed in ppm.

#### Syntax

RFMXNR_ATTR_MODACC_RESULTS_COMPONENT_CARRIER_SYMBOL_CLOCK_ERROR_MEAN

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9453619 | float64 | Read-Only | Chain |

#### Remarks

Use "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>" or "subblock<n>/carrier<k>/chain<<i>r</i>>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__modacc__results_1ga1080009af1475a8bb30ab8195258046d.html language=enus -->
## TOPIC 00092: RFMXNR_ATTR_MODACC_RESULTS_COMPONENT_CARRIER_TIME_OFFSET_MEAN

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__modacc__results_1ga1080009af1475a8bb30ab8195258046d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__modacc__results_1ga1080009af1475a8bb30ab8195258046d.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the time difference between the detected slot or frame boundary depending on the sync mode and reference trigger location. This value is expressed in seconds. SyntaxRFMXNR_ATTR_MODACC_RESULTS_COMPONENT_CARRIER_TIME_OFFSET_MEANNumeric ValueData TypeAccessApplies To9453618float64Read-OnlyChain

### RFMXNR_ATTR_MODACC_RESULTS_COMPONENT_CARRIER_TIME_OFFSET_MEAN

Returns the time difference between the detected slot or frame boundary depending on the sync mode and reference trigger location. This value is expressed in seconds.

#### Syntax

RFMXNR_ATTR_MODACC_RESULTS_COMPONENT_CARRIER_TIME_OFFSET_MEAN

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9453618 | float64 | Read-Only | Chain |

#### Remarks

Use "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>" or "subblock<n>/carrier<k>/chain<<i>r</i>>"as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__modacc__results_1ga4e72892feb88ac486b5feb319080e9eb.html language=enus -->
## TOPIC 00093: RFMXNR_ATTR_MODACC_RESULTS_COMPONENT_CARRIER_CROSS_POWER_MEAN

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__modacc__results_1ga4e72892feb88ac486b5feb319080e9eb.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__modacc__results_1ga4e72892feb88ac486b5feb319080e9eb.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the cross power. The cross power for chain x is the power contribution from layers other than layer x in the chain. This value is expressed in dB. SyntaxRFMXNR_ATTR_MODACC_RESULTS_COMPONENT_CARRIER_CROSS_POWER_MEANNumeric ValueData TypeAccessApplies To9453743float64Read-OnlyChainRemarks Use

### RFMXNR_ATTR_MODACC_RESULTS_COMPONENT_CARRIER_CROSS_POWER_MEAN

Returns the cross power. The cross power for chain x is the power contribution from layers other than layer x in the chain. This value is expressed in dB.

#### Syntax

RFMXNR_ATTR_MODACC_RESULTS_COMPONENT_CARRIER_CROSS_POWER_MEAN

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9453743 | float64 | Read-Only | Chain |

#### Remarks

Use "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>" or "subblock<n>/carrier<k>/chain<<i>r</i>>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__modacc__results_1ga5b3f98afc30e6983510fb255e1eda2b0.html language=enus -->
## TOPIC 00094: RFMXNR_ATTR_MODACC_RESULTS_COMPOSITE_PEAK_EVM_SYMBOL_INDEX

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__modacc__results_1ga5b3f98afc30e6983510fb255e1eda2b0.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__modacc__results_1ga5b3f98afc30e6983510fb255e1eda2b0.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the symbol index where ModAcc Results Max Pk Composite EVM occurs. SyntaxRFMXNR_ATTR_MODACC_RESULTS_COMPOSITE_PEAK_EVM_SYMBOL_INDEXNumeric ValueData TypeAccessApplies To9453597int32Read-OnlyLayerRemarks Use "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>" or "subblock<n>/carrier<k>/

### RFMXNR_ATTR_MODACC_RESULTS_COMPOSITE_PEAK_EVM_SYMBOL_INDEX

Returns the symbol index where ModAcc Results Max Pk Composite EVM occurs.

#### Syntax

RFMXNR_ATTR_MODACC_RESULTS_COMPOSITE_PEAK_EVM_SYMBOL_INDEX

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9453597 | int32 | Read-Only | Layer |

#### Remarks

Use "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>" or "subblock<n>/carrier<k>/layer<<i>q</i>>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__modacc__results_1ga66fd09de637b3666748dac1d229d2598.html language=enus -->
## TOPIC 00095: RFMXNR_ATTR_MODACC_RESULTS_SUBBLOCK_LO_COMPONENT_CARRIER_INDEX

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__modacc__results_1ga66fd09de637b3666748dac1d229d2598.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__modacc__results_1ga66fd09de637b3666748dac1d229d2598.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the index of the component carrier that includes the LO of the transmitter according to the RFMXNR_ATTR_SUBBLOCK_FREQUENCY and RFMXNR_ATTR_SUBBLOCK_TRANSMIT_LO_FREQUENCY attributes. If the LO of the transmitter doesn't fall into any component carrier of the subblock, the attribute returns -1

### RFMXNR_ATTR_MODACC_RESULTS_SUBBLOCK_LO_COMPONENT_CARRIER_INDEX

Returns the index of the component carrier that includes the LO of the transmitter according to the [RFMXNR_ATTR_SUBBLOCK_FREQUENCY](group____root__ni_r_fmx_n_r__attributes_1gaaf94c225d4835cedc981c7acf991814f.html) and [RFMXNR_ATTR_SUBBLOCK_TRANSMIT_LO_FREQUENCY](group____root__ni_r_fmx_n_r__attributes_1ga740a5de3b345a05259f2e5cefd35c781.html) attributes. If the LO of the transmitter doesn't fall into any component carrier of the subblock, the attribute returns -1. This result is valid only when you set the [RFMXNR_ATTR_TRANSMITTER_ARCHITECTURE](group____root__ni_r_fmx_n_r__attributes__advanced_1ga43f68610b348ca835a0dc5b0f042958e.html) attribute to **LO per Subblock**.

#### Syntax

RFMXNR_ATTR_MODACC_RESULTS_SUBBLOCK_LO_COMPONENT_CARRIER_INDEX

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9453666 | Int32 | Read-Only | Chain |

#### Remarks

Use "subblock<n>"or "subblock<n>/chain<<i>r</i>>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__modacc__results_1gaa3ff2991b84e3c9bf1cc16e6c01acab8.html language=enus -->
## TOPIC 00096: RFMXNR_ATTR_MODACC_RESULTS_COMPONENT_CARRIER_TIME_ALIGNMENT_ERROR_MEAN

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__modacc__results_1gaa3ff2991b84e3c9bf1cc16e6c01acab8.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__modacc__results_1gaa3ff2991b84e3c9bf1cc16e6c01acab8.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the difference in the timing error, in seconds, of a CC with respect to the reference CC. The reference CC is fixed to Subblock0/ComponentCarrier0. The timing error reported is a frame timing error when the synchronization mode is set to 'Frame' and is slot timing error when the synchronizat

### RFMXNR_ATTR_MODACC_RESULTS_COMPONENT_CARRIER_TIME_ALIGNMENT_ERROR_MEAN

Returns the difference in the timing error, in seconds, of a CC with respect to the reference CC. The reference CC is fixed to Subblock0/ComponentCarrier0. The timing error reported is a frame timing error when the synchronization mode is set to 'Frame' and is slot timing error when the synchronization mode is set to 'Slot'.

#### Syntax

RFMXNR_ATTR_MODACC_RESULTS_COMPONENT_CARRIER_TIME_ALIGNMENT_ERROR_MEAN

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9453744 | float64 | Read-Only | Chain |

#### Remarks

Use "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>" or "subblock<n>/carrier<k>/chain<<i>r</i>>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__modacc__results_1gab2060d8f51f879ffa3a3627ac9b3ca31.html language=enus -->
## TOPIC 00097: RFMXNR_ATTR_MODACC_RESULTS_SUBBLOCK_LO_SUBCARRIER_INDEX

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__modacc__results_1gab2060d8f51f879ffa3a3627ac9b3ca31.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__modacc__results_1gab2060d8f51f879ffa3a3627ac9b3ca31.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the subcarrier index within the respective component carrier where the transmitter LO is located. Due to its dependence on RFMXNR_ATTR_SUBBLOCK_FREQUENCY and RFMXNR_ATTR_SUBBLOCK_TRANSMIT_LO_FREQUENCY properties, the value can be fractional, and the LO might reside in between subcarriers of

### RFMXNR_ATTR_MODACC_RESULTS_SUBBLOCK_LO_SUBCARRIER_INDEX

Returns the subcarrier index within the respective component carrier where the transmitter LO is located. Due to its dependence on [RFMXNR_ATTR_SUBBLOCK_FREQUENCY](group____root__ni_r_fmx_n_r__attributes_1gaaf94c225d4835cedc981c7acf991814f.html) and [RFMXNR_ATTR_SUBBLOCK_TRANSMIT_LO_FREQUENCY](group____root__ni_r_fmx_n_r__attributes_1ga740a5de3b345a05259f2e5cefd35c781.html) properties, the value can be fractional, and the LO might reside in between subcarriers of a component carrier. This result is valid only when you set the [RFMXNR_ATTR_TRANSMITTER_ARCHITECTURE](group____root__ni_r_fmx_n_r__attributes__advanced_1ga43f68610b348ca835a0dc5b0f042958e.html) attribute to **LO per Subblock**.

#### Syntax

RFMXNR_ATTR_MODACC_RESULTS_SUBBLOCK_LO_SUBCARRIER_INDEX

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9453667 | Int32 | Read-Only | Chain |

#### Remarks

Use "subblock<n>" or "subblock<n>/chain<<i>r</i>>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__modacc__results__pdsch_1ga69d4aa5ac87c7dbcf60f72d3e1b7ba15.html language=enus -->
## TOPIC 00098: RFMXNR_ATTR_MODACC_RESULTS_PDSCH_4096QAM_RMS_EVM_MEAN

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__modacc__results__pdsch_1ga69d4aa5ac87c7dbcf60f72d3e1b7ba15.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__modacc__results__pdsch_1ga69d4aa5ac87c7dbcf60f72d3e1b7ba15.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean value of RMS EVMs calculated over measurement length on all 4096 QAM modulated PDSCH data symbols. SyntaxRFMXNR_ATTR_MODACC_RESULTS_PDSCH_4096QAM_RMS_EVM_MEANNumeric ValueData TypeAccessApplies To9453746float64Read-OnlyBandwidthpartRemarks When you set the RFMXNR_ATTR_MODACC_EVM_UNI

### RFMXNR_ATTR_MODACC_RESULTS_PDSCH_4096QAM_RMS_EVM_MEAN

Returns the mean value of RMS EVMs calculated over measurement length on all 4096 QAM modulated PDSCH data symbols.

#### Syntax

RFMXNR_ATTR_MODACC_RESULTS_PDSCH_4096QAM_RMS_EVM_MEAN

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9453746 | float64 | Read-Only | Bandwidthpart |

#### Remarks

When you set the [RFMXNR_ATTR_MODACC_EVM_UNIT](group____root__ni_r_fmx_n_r__attributes__modacc_1ga99869aa8b87a1e8bb2d5bf45288560c9.html) attribute to **Percentage**, the measurement returns this result as a percentage. When you set the ModAcc EVM Unit attribute to **dB**, the measurement returns this result in dB.

Use "bwp<<i>m</i>>" or "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>/bwp<<i>m</i>>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result.

Parent topic:

PDSCH

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__modacc__results__pdsch_1gabb52933ba48921e643b7c739b3b50969.html language=enus -->
## TOPIC 00099: RFMXNR_ATTR_MODACC_RESULTS_PDSCH_64QAM_RMS_EVM_MEAN

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__modacc__results__pdsch_1gabb52933ba48921e643b7c739b3b50969.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__modacc__results__pdsch_1gabb52933ba48921e643b7c739b3b50969.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean value of RMS EVMs calculated over measurement length on all 64 QAM modulated PDSCH data symbols. SyntaxRFMXNR_ATTR_MODACC_RESULTS_PDSCH_64QAM_RMS_EVM_MEANNumeric ValueData TypeAccessApplies To9453655float64Read-OnlyBandwidthpartRemarks When you set the RFMXNR_ATTR_MODACC_EVM_UNIT at

### RFMXNR_ATTR_MODACC_RESULTS_PDSCH_64QAM_RMS_EVM_MEAN

Returns the mean value of RMS EVMs calculated over measurement length on all 64 QAM modulated PDSCH data symbols.

#### Syntax

RFMXNR_ATTR_MODACC_RESULTS_PDSCH_64QAM_RMS_EVM_MEAN

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9453655 | float64 | Read-Only | Bandwidthpart |

#### Remarks

When you set the [RFMXNR_ATTR_MODACC_EVM_UNIT](group____root__ni_r_fmx_n_r__attributes__modacc_1ga99869aa8b87a1e8bb2d5bf45288560c9.html) attribute to **Percentage**, the measurement returns this result as a percentage. When you set the ModAcc EVM Unit attribute to **dB**, the measurement returns this result in dB.

Use "bwp<<i>m</i>>" or "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>/bwp<<i>m</i>>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result.

Parent topic:

PDSCH

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__modacc__results__pdsch_1gac8e91958cba44857818119ab0e20b557.html language=enus -->
## TOPIC 00100: RFMXNR_ATTR_MODACC_RESULTS_PDSCH_QPSK_RMS_EVM_MEAN

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__modacc__results__pdsch_1gac8e91958cba44857818119ab0e20b557.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__modacc__results__pdsch_1gac8e91958cba44857818119ab0e20b557.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean value of RMS EVMs calculated over measurement length on all QPSK modulated PDSCH data symbols. SyntaxRFMXNR_ATTR_MODACC_RESULTS_PDSCH_QPSK_RMS_EVM_MEANNumeric ValueData TypeAccessApplies To9453653float64Read-OnlyBandwidthpartRemarks When you set the RFMXNR_ATTR_MODACC_EVM_UNIT attri

### RFMXNR_ATTR_MODACC_RESULTS_PDSCH_QPSK_RMS_EVM_MEAN

Returns the mean value of RMS EVMs calculated over measurement length on all QPSK modulated PDSCH data symbols.

#### Syntax

RFMXNR_ATTR_MODACC_RESULTS_PDSCH_QPSK_RMS_EVM_MEAN

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9453653 | float64 | Read-Only | Bandwidthpart |

#### Remarks

When you set the [RFMXNR_ATTR_MODACC_EVM_UNIT](group____root__ni_r_fmx_n_r__attributes__modacc_1ga99869aa8b87a1e8bb2d5bf45288560c9.html) attribute to **Percentage**, the measurement returns this result as a percentage. When you set the ModAcc EVM Unit attribute to **dB**, the measurement returns this result in dB.

Use "bwp<<i>m</i>>" or "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>/bwp<<i>m</i>>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result.

Parent topic:

PDSCH

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__modacc__results__pdsch_1gad86ce03dee3a97a105e9e6e7820a0c3f.html language=enus -->
## TOPIC 00101: RFMXNR_ATTR_MODACC_RESULTS_PDSCH_DATA_RMS_EVM_MEAN

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__modacc__results__pdsch_1gad86ce03dee3a97a105e9e6e7820a0c3f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__modacc__results__pdsch_1gad86ce03dee3a97a105e9e6e7820a0c3f.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean value of RMS EVMs calculated over measurement length on PDSCH data symbols. SyntaxRFMXNR_ATTR_MODACC_RESULTS_PDSCH_DATA_RMS_EVM_MEANNumeric ValueData TypeAccessApplies To9453657float64Read-OnlyLayerRemarks When you set the RFMXNR_ATTR_MODACC_EVM_UNIT attribute to Percentage, the mea

### RFMXNR_ATTR_MODACC_RESULTS_PDSCH_DATA_RMS_EVM_MEAN

Returns the mean value of RMS EVMs calculated over measurement length on PDSCH data symbols.

#### Syntax

RFMXNR_ATTR_MODACC_RESULTS_PDSCH_DATA_RMS_EVM_MEAN

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9453657 | float64 | Read-Only | Layer |

#### Remarks

When you set the [RFMXNR_ATTR_MODACC_EVM_UNIT](group____root__ni_r_fmx_n_r__attributes__modacc_1ga99869aa8b87a1e8bb2d5bf45288560c9.html) attribute to **Percentage**, the measurement returns this result as a percentage. When you set the ModAcc EVM Unit attribute to **dB**, the measurement returns this result in dB.

Use "user<<i>l</i>>" or "bwp<<i>m</i>>" or "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>/bwp<<i>m</i>>/user<<i>l</i>>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result.

Parent topic:

PDSCH

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__modacc__results__pusch.html language=enus -->
## TOPIC 00102: PUSCH

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__modacc__results__pusch.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__modacc__results__pusch.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXNR_ATTR_MODACC_RESULTS_PUSCH_DATA_PEAK_EVM_MAXIMUMReturns the maximum value of peak EVMs calculated over measurement length on PUSCH data symbols. RFMXNR_ATTR_MODACC_RESULTS_PUSCH_DATA_RE_POWER_MEANReturns the mean value (over Meas Length) of power calculate

### PUSCH

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXNR_ATTR_MODACC_RESULTS_PUSCH_DATA_PEAK_EVM_MAXIMUM | Returns the maximum value of peak EVMs calculated over measurement length on PUSCH data symbols. |
| RFMXNR_ATTR_MODACC_RESULTS_PUSCH_DATA_RE_POWER_MEAN | Returns the mean value (over Meas Length) of power calculated on PUSCH data REs. |
| RFMXNR_ATTR_MODACC_RESULTS_PUSCH_DATA_RMS_EVM_MEAN | Returns the mean value of RMS EVMs calculated over measurement length on PUSCH data symbols. |
| RFMXNR_ATTR_MODACC_RESULTS_PUSCH_DATA_TRANSIENT_RMS_EVM_MEAN | Returns the mean value of RMS EVMs calulated over measurement interval for the PUSCH symbols where the transient occurs. |
| RFMXNR_ATTR_MODACC_RESULTS_PUSCH_DMRS_PEAK_EVM_MAXIMUM | Returns the maximum value of peak EVMs calculated over measurement length on PUSCH DMRS. |
| RFMXNR_ATTR_MODACC_RESULTS_PUSCH_DMRS_RE_POWER_MEAN | Returns the mean value (over Meas Length) of power calculated on PUSCH DMRS REs. |
| RFMXNR_ATTR_MODACC_RESULTS_PUSCH_DMRS_RMS_EVM_MEAN | Returns the mean value of RMS EVMs calculated over measurement length on PUSCH DMRS. |
| RFMXNR_ATTR_MODACC_RESULTS_PUSCH_PEAK_PHASE_OFFSET_MAXIMUM | Returns the maximum value over Meas Length of peak phase offsets between the reference and measurement slots. |
| RFMXNR_ATTR_MODACC_RESULTS_PUSCH_PEAK_PHASE_OFFSET_SLOT_INDEX | Returns the slot index where ModAcc Results PUSCH Pk Phase Offset Max occurs. |
| RFMXNR_ATTR_MODACC_RESULTS_PUSCH_PTRS_PEAK_EVM_MAXIMUM | Returns the maximum value of peak EVMs calculated over measurement length on PUSCH PTRS. |
| RFMXNR_ATTR_MODACC_RESULTS_PUSCH_PTRS_RE_POWER_MEAN | Returns the mean value (over Meas Length) of power calculated on PUSCH PTRS REs. |
| RFMXNR_ATTR_MODACC_RESULTS_PUSCH_PTRS_RMS_EVM_MEAN | Returns the mean value of RMS EVMs calculated over measurement length on PUSCH PTRS. |

#### Attachments

None

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__modacc__results__pusch_1ga06600597d548a94bf5a62ce1adf27eab.html language=enus -->
## TOPIC 00103: RFMXNR_ATTR_MODACC_RESULTS_PUSCH_DMRS_PEAK_EVM_MAXIMUM

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__modacc__results__pusch_1ga06600597d548a94bf5a62ce1adf27eab.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__modacc__results__pusch_1ga06600597d548a94bf5a62ce1adf27eab.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum value of peak EVMs calculated over measurement length on PUSCH DMRS. SyntaxRFMXNR_ATTR_MODACC_RESULTS_PUSCH_DMRS_PEAK_EVM_MAXIMUMNumeric ValueData TypeAccessApplies To9453604float64Read-OnlyLayerRemarks When you set the RFMXNR_ATTR_MODACC_EVM_UNIT attribute to Percentage, the mea

### RFMXNR_ATTR_MODACC_RESULTS_PUSCH_DMRS_PEAK_EVM_MAXIMUM

Returns the maximum value of peak EVMs calculated over measurement length on PUSCH DMRS.

#### Syntax

RFMXNR_ATTR_MODACC_RESULTS_PUSCH_DMRS_PEAK_EVM_MAXIMUM

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9453604 | float64 | Read-Only | Layer |

#### Remarks

When you set the [RFMXNR_ATTR_MODACC_EVM_UNIT](group____root__ni_r_fmx_n_r__attributes__modacc_1ga99869aa8b87a1e8bb2d5bf45288560c9.html) attribute to **Percentage**, the measurement returns this result as a percentage. When you set the ModAcc EVM Unit attribute to **dB**, the measurement returns this result in dB.

Use "user<<i>l</i>>" or "bwp<<i>m</i>>" or "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>/bwp<<i>m</i>>/user<<i>l</i>>" or "subblock<n>/carrier<k>/bwp<<i>m</i>>/user<<i>l</i>>/layer<<i>q</i>>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result.

Parent topic:

PUSCH

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__modacc__results__pusch_1ga0e8400a6b9811e50b38e45e871a9f416.html language=enus -->
## TOPIC 00104: RFMXNR_ATTR_MODACC_RESULTS_PUSCH_PTRS_RE_POWER_MEAN

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__modacc__results__pusch_1ga0e8400a6b9811e50b38e45e871a9f416.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__modacc__results__pusch_1ga0e8400a6b9811e50b38e45e871a9f416.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean value (over Meas Length) of power calculated on PUSCH PTRS REs. SyntaxRFMXNR_ATTR_MODACC_RESULTS_PUSCH_PTRS_RE_POWER_MEANNumeric ValueData TypeAccessApplies To9453739float64Read-OnlyLayerRemarks Use "user<<i>l</i>>" or "bwp<<i>m</i>>" or "carrier<k>" or "subblock<n>" or "subblock<n>

### RFMXNR_ATTR_MODACC_RESULTS_PUSCH_PTRS_RE_POWER_MEAN

Returns the mean value (over Meas Length) of power calculated on PUSCH PTRS REs.

#### Syntax

RFMXNR_ATTR_MODACC_RESULTS_PUSCH_PTRS_RE_POWER_MEAN

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9453739 | float64 | Read-Only | Layer |

#### Remarks

Use "user<<i>l</i>>" or "bwp<<i>m</i>>" or "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>/bwp<<i>m</i>>/user<<i>l</i>>" or "subblock<n>/carrier<k>/bwp<<i>m</i>>/user<<i>l</i>>/layer<<i>q</i>>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result.

Parent topic:

PUSCH

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__modacc__results__pusch_1ga18906d1ac38a83435dc5dc43a19811e6.html language=enus -->
## TOPIC 00105: RFMXNR_ATTR_MODACC_RESULTS_PUSCH_DATA_RMS_EVM_MEAN

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__modacc__results__pusch_1ga18906d1ac38a83435dc5dc43a19811e6.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__modacc__results__pusch_1ga18906d1ac38a83435dc5dc43a19811e6.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean value of RMS EVMs calculated over measurement length on PUSCH data symbols. SyntaxRFMXNR_ATTR_MODACC_RESULTS_PUSCH_DATA_RMS_EVM_MEANNumeric ValueData TypeAccessApplies To9453599float64Read-OnlyLayerRemarks When you set the RFMXNR_ATTR_MODACC_EVM_UNIT attribute to Percentage, the mea

### RFMXNR_ATTR_MODACC_RESULTS_PUSCH_DATA_RMS_EVM_MEAN

Returns the mean value of RMS EVMs calculated over measurement length on PUSCH data symbols.

#### Syntax

RFMXNR_ATTR_MODACC_RESULTS_PUSCH_DATA_RMS_EVM_MEAN

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9453599 | float64 | Read-Only | Layer |

#### Remarks

When you set the [RFMXNR_ATTR_MODACC_EVM_UNIT](group____root__ni_r_fmx_n_r__attributes__modacc_1ga99869aa8b87a1e8bb2d5bf45288560c9.html) attribute to **Percentage**, the measurement returns this result as a percentage. When you set the ModAcc EVM Unit attribute to **dB**, the measurement returns this result in dB.

Use "user<<i>l</i>>" or "bwp<<i>m</i>>" or "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>/bwp<<i>m</i>>/user<<i>l</i>>" or "subblock<n>/carrier<k>/bwp<<i>m</i>>/user<<i>l</i>>/layer<<i>q</i>>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result.

Parent topic:

PUSCH

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__modacc__results__pusch_1ga2b4daaf1ff28bd6f6c2631f0fa9b0cdb.html language=enus -->
## TOPIC 00106: RFMXNR_ATTR_MODACC_RESULTS_PUSCH_DATA_RE_POWER_MEAN

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__modacc__results__pusch_1ga2b4daaf1ff28bd6f6c2631f0fa9b0cdb.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__modacc__results__pusch_1ga2b4daaf1ff28bd6f6c2631f0fa9b0cdb.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean value (over Meas Length) of power calculated on PUSCH data REs. SyntaxRFMXNR_ATTR_MODACC_RESULTS_PUSCH_DATA_RE_POWER_MEANNumeric ValueData TypeAccessApplies To9453737float64Read-OnlyLayerRemarks Use "user<<i>l</i>>" or "bwp<<i>m</i>>" or "carrier<k>" or "subblock<n>" or "subblock<n>

### RFMXNR_ATTR_MODACC_RESULTS_PUSCH_DATA_RE_POWER_MEAN

Returns the mean value (over Meas Length) of power calculated on PUSCH data REs.

#### Syntax

RFMXNR_ATTR_MODACC_RESULTS_PUSCH_DATA_RE_POWER_MEAN

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9453737 | float64 | Read-Only | Layer |

#### Remarks

Use "user<<i>l</i>>" or "bwp<<i>m</i>>" or "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>/bwp<<i>m</i>>/user<<i>l</i>>" or "subblock<n>/carrier<k>/bwp<<i>m</i>>/user<<i>l</i>>/layer<<i>q</i>>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result.

Parent topic:

PUSCH

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__modacc__results__pusch_1gab5efc912a0231b3658d63ce34b2e4b3a.html language=enus -->
## TOPIC 00107: RFMXNR_ATTR_MODACC_RESULTS_PUSCH_DATA_TRANSIENT_RMS_EVM_MEAN

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__modacc__results__pusch_1gab5efc912a0231b3658d63ce34b2e4b3a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__modacc__results__pusch_1gab5efc912a0231b3658d63ce34b2e4b3a.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean value of RMS EVMs calulated over measurement interval for the PUSCH symbols where the transient occurs. SyntaxRFMXNR_ATTR_MODACC_RESULTS_PUSCH_DATA_TRANSIENT_RMS_EVM_MEANNumeric ValueData TypeAccessApplies To9453734float64Read-OnlyLayerRemarks When you set the RFMXNR_ATTR_MODACC_EVM

### RFMXNR_ATTR_MODACC_RESULTS_PUSCH_DATA_TRANSIENT_RMS_EVM_MEAN

Returns the mean value of RMS EVMs calulated over measurement interval for the PUSCH symbols where the transient occurs.

#### Syntax

RFMXNR_ATTR_MODACC_RESULTS_PUSCH_DATA_TRANSIENT_RMS_EVM_MEAN

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9453734 | float64 | Read-Only | Layer |

#### Remarks

When you set the [RFMXNR_ATTR_MODACC_EVM_UNIT](group____root__ni_r_fmx_n_r__attributes__modacc_1ga99869aa8b87a1e8bb2d5bf45288560c9.html) attribute to **Percentage**, the measurement returns this result as a percentage. When you set the ModAcc EVM Unit attribute to **dB**, the measurement returns this result in dB.

Use "user<<i>l</i>>" or "bwp<<i>m</i>>" or "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>/bwp<<i>m</i>>/user<<i>l</i>>" or "subblock<n>/carrier<k>/bwp<<i>m</i>>/user<<i>l</i>>/layer<<i>q</i>>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result.

Parent topic:

PUSCH

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__modacc__results__pusch_1gac9c98194dd50df0a0a777c38919a5d07.html language=enus -->
## TOPIC 00108: RFMXNR_ATTR_MODACC_RESULTS_PUSCH_PEAK_PHASE_OFFSET_MAXIMUM

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__modacc__results__pusch_1gac9c98194dd50df0a0a777c38919a5d07.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__modacc__results__pusch_1gac9c98194dd50df0a0a777c38919a5d07.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum value over Meas Length of peak phase offsets between the reference and measurement slots. SyntaxRFMXNR_ATTR_MODACC_RESULTS_PUSCH_PEAK_PHASE_OFFSET_MAXIMUMNumeric ValueData TypeAccessApplies To9453735float64Read-OnlyLayerRemarks Use "user<<i>l</i>>" or "bwp<<i>m</i>>" or "carrier<

### RFMXNR_ATTR_MODACC_RESULTS_PUSCH_PEAK_PHASE_OFFSET_MAXIMUM

Returns the maximum value over Meas Length of peak phase offsets between the reference and measurement slots.

#### Syntax

RFMXNR_ATTR_MODACC_RESULTS_PUSCH_PEAK_PHASE_OFFSET_MAXIMUM

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9453735 | float64 | Read-Only | Layer |

#### Remarks

Use "user<<i>l</i>>" or "bwp<<i>m</i>>" or "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>/bwp<<i>m</i>>/user<<i>l</i>>" or "subblock<n>/carrier<k>/bwp<<i>m</i>>/user<<i>l</i>>/layer<<i>q</i>>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result.

Parent topic:

PUSCH

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__modacc__results__pusch_1gaf201b338fd6b94859efffd74ed23dbd2.html language=enus -->
## TOPIC 00109: RFMXNR_ATTR_MODACC_RESULTS_PUSCH_DMRS_RMS_EVM_MEAN

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__modacc__results__pusch_1gaf201b338fd6b94859efffd74ed23dbd2.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__modacc__results__pusch_1gaf201b338fd6b94859efffd74ed23dbd2.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean value of RMS EVMs calculated over measurement length on PUSCH DMRS. SyntaxRFMXNR_ATTR_MODACC_RESULTS_PUSCH_DMRS_RMS_EVM_MEANNumeric ValueData TypeAccessApplies To9453603float64Read-OnlyLayerRemarks When you set the RFMXNR_ATTR_MODACC_EVM_UNIT attribute to Percentage, the measurement

### RFMXNR_ATTR_MODACC_RESULTS_PUSCH_DMRS_RMS_EVM_MEAN

Returns the mean value of RMS EVMs calculated over measurement length on PUSCH DMRS.

#### Syntax

RFMXNR_ATTR_MODACC_RESULTS_PUSCH_DMRS_RMS_EVM_MEAN

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9453603 | float64 | Read-Only | Layer |

#### Remarks

When you set the [RFMXNR_ATTR_MODACC_EVM_UNIT](group____root__ni_r_fmx_n_r__attributes__modacc_1ga99869aa8b87a1e8bb2d5bf45288560c9.html) attribute to **Percentage**, the measurement returns this result as a percentage. When you set the ModAcc EVM Unit attribute to **dB**, the measurement returns this result in dB.

Use "user<<i>l</i>>" or "bwp<<i>m</i>>" or "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>/bwp<<i>m</i>>/user<<i>l</i>>" or "subblock<n>/carrier<k>/bwp<<i>m</i>>/user<<i>l</i>>/layer<<i>q</i>>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result.

Parent topic:

PUSCH

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__modacc__results__spectral__flatness_1ga1d8d034fff8261c9eccce7e4e72a133f.html language=enus -->
## TOPIC 00110: RFMXNR_ATTR_MODACC_RESULTS_SPECTRAL_FLATNESS_RANGE1_MAXIMUM_SUBCARRIER_INDEX

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__modacc__results__spectral__flatness_1ga1d8d034fff8261c9eccce7e4e72a133f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__modacc__results__spectral__flatness_1ga1d8d034fff8261c9eccce7e4e72a133f.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum subcarrier index magnitude of EVM equalizer coefficients within Range1 for the measurement unit with the worst ripple margin among all four ripple results defined in section 6.4.2.4.1 of 3GPP 38.101-1 specification and section 6.4.2.4.1 of 3GPP 38.101-2 specification. SyntaxRFMXN

### RFMXNR_ATTR_MODACC_RESULTS_SPECTRAL_FLATNESS_RANGE1_MAXIMUM_SUBCARRIER_INDEX

Returns the maximum subcarrier index magnitude of EVM equalizer coefficients within Range1 for the measurement unit with the worst ripple margin among all four ripple results defined in section 6.4.2.4.1 of *3GPP 38.101-1* specification and section 6.4.2.4.1 of *3GPP 38.101-2* specification.

#### Syntax

RFMXNR_ATTR_MODACC_RESULTS_SPECTRAL_FLATNESS_RANGE1_MAXIMUM_SUBCARRIER_INDEX

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9453709 | int32 | Read-Only | Layer |

#### Remarks

Use "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>" or "subblock<n>/carrier<k>/layer<<i>q</i>>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result.

Parent topic:

Spectral Flatness

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__modacc__results__spectral__flatness_1ga7abe0cbaa137e6becdbe9d17f8c0fe73.html language=enus -->
## TOPIC 00111: RFMXNR_ATTR_MODACC_RESULTS_SPECTRAL_FLATNESS_RANGE1_MAXIMUM_TO_RANGE1_MINIMUM

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__modacc__results__spectral__flatness_1ga7abe0cbaa137e6becdbe9d17f8c0fe73.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__modacc__results__spectral__flatness_1ga7abe0cbaa137e6becdbe9d17f8c0fe73.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the peak-to-peak ripple of the magnitude of EVM equalizer coefficients within Range1 for the measurement unit, that has the worst ripple margin among all four ripple results defined in section 6.4.2.4.1 of 3GPP 38.101-1 specification and section 6.4.2.4.1 of 3GPP 38.101-2 specification. This

### RFMXNR_ATTR_MODACC_RESULTS_SPECTRAL_FLATNESS_RANGE1_MAXIMUM_TO_RANGE1_MINIMUM

Returns the peak-to-peak ripple of the magnitude of EVM equalizer coefficients within Range1 for the measurement unit, that has the worst ripple margin among all four ripple results defined in section 6.4.2.4.1 of *3GPP 38.101-1* specification and section 6.4.2.4.1 of *3GPP 38.101-2* specification. This value is expressed in dB.

#### Syntax

RFMXNR_ATTR_MODACC_RESULTS_SPECTRAL_FLATNESS_RANGE1_MAXIMUM_TO_RANGE1_MINIMUM

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9453608 | float64 | Read-Only | Layer |

#### Remarks

Use "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>" or "subblock<n>/carrier<k>/layer<<i>q</i>>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result.

Parent topic:

Spectral Flatness

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__modacc__results__spectral__flatness_1ga9d4cb4c470b5178033582a14cbf3218a.html language=enus -->
## TOPIC 00112: RFMXNR_ATTR_MODACC_RESULTS_SPECTRAL_FLATNESS_MARGIN_SLOT_INDEX

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__modacc__results__spectral__flatness_1ga9d4cb4c470b5178033582a14cbf3218a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__modacc__results__spectral__flatness_1ga9d4cb4c470b5178033582a14cbf3218a.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the slot index with the worst ripple margin among all four ripple results defined in section 6.4.2.4.1 of 3GPP 38.101-1 specification and section 6.4.2.4.1 of 3GPP 38.101-2. SyntaxRFMXNR_ATTR_MODACC_RESULTS_SPECTRAL_FLATNESS_MARGIN_SLOT_INDEXNumeric ValueData TypeAccessApplies To9453704int32

### RFMXNR_ATTR_MODACC_RESULTS_SPECTRAL_FLATNESS_MARGIN_SLOT_INDEX

Returns the slot index with the worst ripple margin among all four ripple results defined in section 6.4.2.4.1 of *3GPP 38.101-1* specification and section 6.4.2.4.1 of *3GPP 38.101-2*.

#### Syntax

RFMXNR_ATTR_MODACC_RESULTS_SPECTRAL_FLATNESS_MARGIN_SLOT_INDEX

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9453704 | int32 | Read-Only | Layer |

#### Remarks

Use "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>" or "subblock<n>/carrier<k>/layer<<i>q</i>>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result.

Parent topic:

Spectral Flatness

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__modacc__results__spectral__flatness_1gab6c1d53de625b401f4d86ceb2d29940e.html language=enus -->
## TOPIC 00113: RFMXNR_ATTR_MODACC_RESULTS_SPECTRAL_FLATNESS_RANGE2_MINIMUM

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__modacc__results__spectral__flatness_1gab6c1d53de625b401f4d86ceb2d29940e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__modacc__results__spectral__flatness_1gab6c1d53de625b401f4d86ceb2d29940e.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the minimum magnitude of EVM equalizer coefficients within Range2 for the measurement unit with the worst ripple margin among all four ripple results defined in section 6.4.2.4.1 of 3GPP 38.101-1 specification and section 6.4.2.4.1 of 3GPP 38.101-2 specification. The value is expressed in dB

### RFMXNR_ATTR_MODACC_RESULTS_SPECTRAL_FLATNESS_RANGE2_MINIMUM

Returns the minimum magnitude of EVM equalizer coefficients within Range2 for the measurement unit with the worst ripple margin among all four ripple results defined in section 6.4.2.4.1 of *3GPP 38.101-1* specification and section 6.4.2.4.1 of *3GPP 38.101-2* specification. The value is expressed in dB.

#### Syntax

RFMXNR_ATTR_MODACC_RESULTS_SPECTRAL_FLATNESS_RANGE2_MINIMUM

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9453708 | float64 | Read-Only | Layer |

#### Remarks

Use "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>" or "subblock<n>/carrier<k>/layer<<i>q</i>>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result.

Parent topic:

Spectral Flatness

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__modacc__results__spectral__flatness_1gac7249ce74d91170ecace15a88968e30d.html language=enus -->
## TOPIC 00114: RFMXNR_ATTR_MODACC_RESULTS_SPECTRAL_FLATNESS_RANGE2_MAXIMUM_TO_RANGE2_MINIMUM

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__modacc__results__spectral__flatness_1gac7249ce74d91170ecace15a88968e30d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__modacc__results__spectral__flatness_1gac7249ce74d91170ecace15a88968e30d.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the peak-to-peak ripple of the magnitude of EVM equalizer coefficients within Range2 for the Measurement unit, that has the worst ripple margin among all four ripple results defined in section 6.4.2.4.1 of 3GPP 38.101-1 specification and section 6.4.2.4.1 of 3GPP 38.101-2 specification. This

### RFMXNR_ATTR_MODACC_RESULTS_SPECTRAL_FLATNESS_RANGE2_MAXIMUM_TO_RANGE2_MINIMUM

Returns the peak-to-peak ripple of the magnitude of EVM equalizer coefficients within Range2 for the Measurement unit, that has the worst ripple margin among all four ripple results defined in section 6.4.2.4.1 of *3GPP 38.101-1* specification and section 6.4.2.4.1 of *3GPP 38.101-2* specification. This value is expressed in dB.

#### Syntax

RFMXNR_ATTR_MODACC_RESULTS_SPECTRAL_FLATNESS_RANGE2_MAXIMUM_TO_RANGE2_MINIMUM

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9453609 | float64 | Read-Only | Layer |

#### Remarks

Use "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>" or "subblock<n>/carrier<k>/layer<<i>q</i>>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result.

Parent topic:

Spectral Flatness

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__modacc__results__spectral__flatness_1gad0f069b7d84d727c110f2c910bff60c2.html language=enus -->
## TOPIC 00115: RFMXNR_ATTR_MODACC_RESULTS_SPECTRAL_FLATNESS_RANGE2_MAXIMUM

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__modacc__results__spectral__flatness_1gad0f069b7d84d727c110f2c910bff60c2.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__modacc__results__spectral__flatness_1gad0f069b7d84d727c110f2c910bff60c2.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum magnitude of EVM equalizer coefficients within Range2 for the measurement unit with the worst ripple margin among all four ripple results defined in section 6.4.2.4.1 of 3GPP 38.101-1 specification and section 6.4.2.4.1 of 3GPP 38.101-2 specification. The value is expressed in dB

### RFMXNR_ATTR_MODACC_RESULTS_SPECTRAL_FLATNESS_RANGE2_MAXIMUM

Returns the maximum magnitude of EVM equalizer coefficients within Range2 for the measurement unit with the worst ripple margin among all four ripple results defined in section 6.4.2.4.1 of *3GPP 38.101-1* specification and section 6.4.2.4.1 of *3GPP 38.101-2* specification. The value is expressed in dB.

#### Syntax

RFMXNR_ATTR_MODACC_RESULTS_SPECTRAL_FLATNESS_RANGE2_MAXIMUM

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9453707 | float64 | Read-Only | Layer |

#### Remarks

Use "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>" or "subblock<n>/carrier<k>/layer<<i>q</i>>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result.

Parent topic:

Spectral Flatness

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__modacc__results__spectral__flatness_1gad686ee6ab14d31af8442ec367f07a983.html language=enus -->
## TOPIC 00116: RFMXNR_ATTR_MODACC_RESULTS_SPECTRAL_FLATNESS_RANGE1_MINIMUM

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__modacc__results__spectral__flatness_1gad686ee6ab14d31af8442ec367f07a983.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__modacc__results__spectral__flatness_1gad686ee6ab14d31af8442ec367f07a983.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the minimum magnitude of EVM equalizer coefficients within Range1 for the measurement unit with the worst ripple margin among all four ripple results defined in section 6.4.2.4.1 of 3GPP 38.101-1 specification and section 6.4.2.4.1 of 3GPP 38.101-2 specification. The value is expressed in dB

### RFMXNR_ATTR_MODACC_RESULTS_SPECTRAL_FLATNESS_RANGE1_MINIMUM

Returns the minimum magnitude of EVM equalizer coefficients within Range1 for the measurement unit with the worst ripple margin among all four ripple results defined in section 6.4.2.4.1 of *3GPP 38.101-1* specification and section 6.4.2.4.1 of *3GPP 38.101-2* specification. The value is expressed in dB.

#### Syntax

RFMXNR_ATTR_MODACC_RESULTS_SPECTRAL_FLATNESS_RANGE1_MINIMUM

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9453706 | float64 | Read-Only | Layer |

#### Remarks

Use "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>" or "subblock<n>/carrier<k>/layer<<i>q</i>>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result.

Parent topic:

Spectral Flatness

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__modacc__results__ssb_1ga7868cb0a46115785241b0d4cb59f1a38.html language=enus -->
## TOPIC 00117: RFMXNR_ATTR_MODACC_RESULTS_PBCH_DATA_PEAK_EVM_MAXIMUM

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__modacc__results__ssb_1ga7868cb0a46115785241b0d4cb59f1a38.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__modacc__results__ssb_1ga7868cb0a46115785241b0d4cb59f1a38.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum value calculated over measurement length of peak EVMs calculated on PBCH data symbols. SyntaxRFMXNR_ATTR_MODACC_RESULTS_PBCH_DATA_PEAK_EVM_MAXIMUMNumeric ValueData TypeAccessApplies To9453694float64Read-OnlyCarrierRemarks When you set the RFMXNR_ATTR_MODACC_EVM_UNIT attribute to

### RFMXNR_ATTR_MODACC_RESULTS_PBCH_DATA_PEAK_EVM_MAXIMUM

Returns the maximum value calculated over measurement length of peak EVMs calculated on PBCH data symbols.

#### Syntax

RFMXNR_ATTR_MODACC_RESULTS_PBCH_DATA_PEAK_EVM_MAXIMUM

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9453694 | float64 | Read-Only | Carrier |

#### Remarks

When you set the [RFMXNR_ATTR_MODACC_EVM_UNIT](group____root__ni_r_fmx_n_r__attributes__modacc_1ga99869aa8b87a1e8bb2d5bf45288560c9.html) attribute to **Percentage**, the measurement returns this result as a percentage. When you set the ModAcc EVM Unit attribute to **dB**, the measurement returns this result in dB.

Use "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result.

Parent topic:

SSB

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__obw__span.html language=enus -->
## TOPIC 00118: Span

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__obw__span.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__obw__span.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXNR_ATTR_OBW_SPANSpecifies the frequency range around the subblock center frequency, which is used to find the RFMXNR_ATTR_OBW_RESULTS_OCCUPIED_BANDWIDTH. When RFMXNR_ATTR_OBW_SPAN_AUTO is set to False, the configured span value is used by the measurement. Th

### Span

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXNR_ATTR_OBW_SPAN | Specifies the frequency range around the subblock center frequency, which is used to find the RFMXNR_ATTR_OBW_RESULTS_OCCUPIED_BANDWIDTH. When RFMXNR_ATTR_OBW_SPAN_AUTO is set to False, the configured span value is used by the measurement. This value is expressed in Hz. |
| RFMXNR_ATTR_OBW_SPAN_AUTO | Specifies whether the frequency range of the spectrum used for the OBW measurement is auto computed or configured by the user. |

#### Attachments

None

Parent topic:

OBW

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__obw__sweep__time.html language=enus -->
## TOPIC 00119: Sweep Time

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__obw__sweep__time.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__obw__sweep__time.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXNR_ATTR_OBW_SWEEP_TIME_AUTOSpecifies whether the measurement sets the sweep time. RFMXNR_ATTR_OBW_SWEEP_TIME_INTERVALSpecifies the sweep time when you set the RFMXNR_ATTR_OBW_SWEEP_TIME_AUTO attribute to False. This value is expressed in seconds. Attachments

### Sweep Time

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXNR_ATTR_OBW_SWEEP_TIME_AUTO | Specifies whether the measurement sets the sweep time. |
| RFMXNR_ATTR_OBW_SWEEP_TIME_INTERVAL | Specifies the sweep time when you set the RFMXNR_ATTR_OBW_SWEEP_TIME_AUTO attribute to False. This value is expressed in seconds. |

#### Attachments

None

Parent topic:

OBW

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__pvt_1ga26ec69883eda8141dfebbe07936ab0ed.html language=enus -->
## TOPIC 00120: RFMXNR_ATTR_PVT_MEASUREMENT_ENABLED

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__pvt_1ga26ec69883eda8141dfebbe07936ab0ed.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__pvt_1ga26ec69883eda8141dfebbe07936ab0ed.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the PVT measurement. SyntaxRFMXNR_ATTR_PVT_MEASUREMENT_ENABLEDNumeric ValueData TypeAccessApplies To9474048int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector String

### RFMXNR_ATTR_PVT_MEASUREMENT_ENABLED

Specifies whether to enable the PVT measurement.

#### Syntax

RFMXNR_ATTR_PVT_MEASUREMENT_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9474048 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is FALSE.

Parent topic:

PVT

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__pvt__averaging_1ga56253b2e7260d62d2d6a3255ab7f7cdd.html language=enus -->
## TOPIC 00121: RFMXNR_ATTR_PVT_AVERAGING_ENABLED

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__pvt__averaging_1ga56253b2e7260d62d2d6a3255ab7f7cdd.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__pvt__averaging_1ga56253b2e7260d62d2d6a3255ab7f7cdd.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable averaging for the power versus time (PVT) measurement. SyntaxRFMXNR_ATTR_PVT_AVERAGING_ENABLEDNumeric ValueData TypeAccessApplies To9474051int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instanc

### RFMXNR_ATTR_PVT_AVERAGING_ENABLED

Specifies whether to enable averaging for the power versus time (PVT) measurement.

#### Syntax

RFMXNR_ATTR_PVT_AVERAGING_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9474051 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **False**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXNR_VAL_PVT_AVERAGING_ENABLED_FALSE | 0 (0x0) | The measurement is performed on a single acquisition. |
| RFMXNR_VAL_PVT_AVERAGING_ENABLED_TRUE | 1 (0x1) | The measurement uses the value of the RFMXNR_ATTR_PVT_AVERAGING_COUNT attribute as the number of acquisitions over which the PVT measurement is averaged. |

Parent topic:

Averaging

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__sem_1ga6449ad472919ef7a422d47894378ac87.html language=enus -->
## TOPIC 00122: RFMXNR_ATTR_SEM_SUBBLOCK_INTEGRATION_BANDWIDTH

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__sem_1ga6449ad472919ef7a422d47894378ac87.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__sem_1ga6449ad472919ef7a422d47894378ac87.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the integration bandwidth of a subblock. This value is expressed in Hz. Integration bandwidth is the span from the left edge of the leftmost carrier to the right edge of the rightmost carrier within the subblock. SyntaxRFMXNR_ATTR_SEM_SUBBLOCK_INTEGRATION_BANDWIDTHNumeric ValueData TypeAcces

### RFMXNR_ATTR_SEM_SUBBLOCK_INTEGRATION_BANDWIDTH

Returns the integration bandwidth of a subblock. This value is expressed in Hz. Integration bandwidth is the span from the left edge of the leftmost carrier to the right edge of the rightmost carrier within the subblock.

#### Syntax

RFMXNR_ATTR_SEM_SUBBLOCK_INTEGRATION_BANDWIDTH

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9469955 | float64 | Read-Only | Subblock |

#### Remarks

Use "subblock<n>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result.

The default value is 0.

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__sem_1gac03b387ac66bae8d30624deca3f07edb.html language=enus -->
## TOPIC 00123: RFMXNR_ATTR_SEM_AMPLITUDE_CORRECTION_TYPE

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__sem_1gac03b387ac66bae8d30624deca3f07edb.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__sem_1gac03b387ac66bae8d30624deca3f07edb.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the amplitude of the frequency bins, used in measurements, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the RFmxInstr Configure External Attenuation Table function to configure the external attenuation table. SyntaxRFMXN

### RFMXNR_ATTR_SEM_AMPLITUDE_CORRECTION_TYPE

Specifies whether the amplitude of the frequency bins, used in measurements, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the [RFmxInstr Configure External Attenuation Table](/csh?context=rfmxinstr_rfmxinstrcref_function_cfg_external_attenuation_table) function to configure the external attenuation table.

#### Syntax

RFMXNR_ATTR_SEM_AMPLITUDE_CORRECTION_TYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9469975 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **RF Center Frequency**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXNR_VAL_SEM_AMPLITUDE_CORRECTION_TYPE_RF_CENTER_FREQUENCY | 0 (0x0) | All the frequency bins in the spectrum are compensated with a single external attenuation value that corresponds to the RF center frequency. |
| RFMXNR_VAL_SEM_AMPLITUDE_CORRECTION_TYPE_SPECTRUM_FREQUENCY_BIN | 1 (0x1) | An individual frequency bin in the spectrum is compensated with the external attenuation value corresponding to that frequency. |

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__sem__offset_1ga227b1f4b75e7517ce78bbc1878a72f3b.html language=enus -->
## TOPIC 00124: RFMXNR_ATTR_SEM_NUMBER_OF_OFFSETS

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__sem__offset_1ga227b1f4b75e7517ce78bbc1878a72f3b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__sem__offset_1ga227b1f4b75e7517ce78bbc1878a72f3b.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of SEM offset segments. SyntaxRFMXNR_ATTR_SEM_NUMBER_OF_OFFSETSNumeric ValueData TypeAccessApplies To9469958int32Read/WriteSubblockRemarks Use "subblock<n>" as the Selector String to configure or read this attribute.The default value is 1.

### RFMXNR_ATTR_SEM_NUMBER_OF_OFFSETS

Specifies the number of SEM offset segments.

#### Syntax

RFMXNR_ATTR_SEM_NUMBER_OF_OFFSETS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9469958 | int32 | Read/Write | Subblock |

#### Remarks

Use "subblock<n>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute.

The default value is 1.

Parent topic:

Offset

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__sem__offset_1gaebd3cb959d6b014150380c534b1c977f.html language=enus -->
## TOPIC 00125: RFMXNR_ATTR_SEM_OFFSET_FREQUENCY_DEFINITION

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__sem__offset_1gaebd3cb959d6b014150380c534b1c977f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__sem__offset_1gaebd3cb959d6b014150380c534b1c977f.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the definition of the the start frequency and stop frequency of the offset segments. SyntaxRFMXNR_ATTR_SEM_OFFSET_FREQUENCY_DEFINITIONNumeric ValueData TypeAccessApplies To9470018int32Read/WriteOffsetRemarks If this attribute is not configured, the following values are used based on other

### RFMXNR_ATTR_SEM_OFFSET_FREQUENCY_DEFINITION

Specifies the definition of the the start frequency and stop frequency of the offset segments.

#### Syntax

RFMXNR_ATTR_SEM_OFFSET_FREQUENCY_DEFINITION

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9470018 | int32 | Read/Write | Offset |

#### Remarks

If this attribute is not configured, the following values are used based on other configurations - Carrier Edge to Meas BW Center for a single-carrier configuration, Subblock Edge to Meas BW Center for a multi-carrier configuration, and Carrier Center to Meas BW Center for a single-carrier configuration in the bands n46, n96, and n102 as defined in the 3GPP TS 37.213 for the shared spectrum channel access.

Use "offset<k>" or "subblock<n>" or "subblock<n>/offset<k>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute.

| Name | Value | Description |
| --- | --- | --- |
| RFMXNR_VAL_SEM_OFFSET_FREQUENCY_DEFINITION_CARRIER_CENTER_TO_MEAS_BW_CENTER | 0 (0x0) | The start frequency and stop frequency are defined from the center of the closest carrier channel bandwidth to the center of the offset segment measurement bandwidth. |
| RFMXNR_VAL_SEM_OFFSET_FREQUENCY_DEFINITION_CARRIER_EDGE_TO_MEAS_BW_CENTER | 2 (0x2) | The start frequency and stop frequency are defined from the nearest edge of the closest carrier channel bandwidth to the center of the offset segment measurement bandwidth. |
| RFMXNR_VAL_SEM_OFFSET_FREQUENCY_DEFINITION_SUBBLOCK_EDGE_TO_MEAS_BW_CENTER | 6 (0x6) | The start frequency and stop frequency are defined from the subblock edge of the closest subblock bandwidth to the center of the offset segment measurement bandwidth. |

Parent topic:

Offset

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__sem__results__component__carrier_1ga35f34b44c99fce477b62174a11f4d518.html language=enus -->
## TOPIC 00126: RFMXNR_ATTR_SEM_RESULTS_COMPONENT_CARRIER_ABSOLUTE_PEAK_POWER

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__sem__results__component__carrier_1ga35f34b44c99fce477b62174a11f4d518.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__sem__results__component__carrier_1ga35f34b44c99fce477b62174a11f4d518.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the peak power in the component carrier. This value is expressed in dBm. SyntaxRFMXNR_ATTR_SEM_RESULTS_COMPONENT_CARRIER_ABSOLUTE_PEAK_POWERNumeric ValueData TypeAccessApplies To9469986float64Read-OnlyCarrierRemarks Use "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>" as the Selecto

### RFMXNR_ATTR_SEM_RESULTS_COMPONENT_CARRIER_ABSOLUTE_PEAK_POWER

Returns the peak power in the component carrier. This value is expressed in dBm.

#### Syntax

RFMXNR_ATTR_SEM_RESULTS_COMPONENT_CARRIER_ABSOLUTE_PEAK_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9469986 | float64 | Read-Only | Carrier |

#### Remarks

Use "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result.

Parent topic:

Component Carrier

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__sem__results__component__carrier_1gabd54444bdc4a8549a8b22e6b24e7f0e9.html language=enus -->
## TOPIC 00127: RFMXNR_ATTR_SEM_RESULTS_COMPONENT_CARRIER_PEAK_FREQUENCY

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__sem__results__component__carrier_1gabd54444bdc4a8549a8b22e6b24e7f0e9.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__sem__results__component__carrier_1gabd54444bdc4a8549a8b22e6b24e7f0e9.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the frequency at which peak power occurs in the component carrier. This value is expressed in Hz. SyntaxRFMXNR_ATTR_SEM_RESULTS_COMPONENT_CARRIER_PEAK_FREQUENCYNumeric ValueData TypeAccessApplies To9469987float64Read-OnlyCarrierRemarks Use "carrier<k>" or "subblock<n>" or "subblock<n>/carrie

### RFMXNR_ATTR_SEM_RESULTS_COMPONENT_CARRIER_PEAK_FREQUENCY

Returns the frequency at which peak power occurs in the component carrier. This value is expressed in Hz.

#### Syntax

RFMXNR_ATTR_SEM_RESULTS_COMPONENT_CARRIER_PEAK_FREQUENCY

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9469987 | float64 | Read-Only | Carrier |

#### Remarks

Use "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result.

Parent topic:

Component Carrier

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__sem__results__component__carrier_1gabffaf057a2afc720cc576c113d27aca5.html language=enus -->
## TOPIC 00128: RFMXNR_ATTR_SEM_RESULTS_COMPONENT_CARRIER_RELATIVE_INTEGRATED_POWER

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__sem__results__component__carrier_1gabffaf057a2afc720cc576c113d27aca5.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__sem__results__component__carrier_1gabffaf057a2afc720cc576c113d27aca5.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the component carrier power relative to RFMXNR_ATTR_SEM_RESULTS_SUBBLOCK_POWER. This value is expressed in dB. SyntaxRFMXNR_ATTR_SEM_RESULTS_COMPONENT_CARRIER_RELATIVE_INTEGRATED_POWERNumeric ValueData TypeAccessApplies To9469985float64Read-OnlyCarrierRemarks Use "carrier<k>" or "subblock<n>

### RFMXNR_ATTR_SEM_RESULTS_COMPONENT_CARRIER_RELATIVE_INTEGRATED_POWER

Returns the component carrier power relative to [RFMXNR_ATTR_SEM_RESULTS_SUBBLOCK_POWER](group____root__ni_r_fmx_n_r__attributes__sem__results_1ga0516aad05dceee009e17fcaefc9c1c20.html). This value is expressed in dB.

#### Syntax

RFMXNR_ATTR_SEM_RESULTS_COMPONENT_CARRIER_RELATIVE_INTEGRATED_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9469985 | float64 | Read-Only | Carrier |

#### Remarks

Use "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result.

Parent topic:

Component Carrier

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__sem__results__component__carrier_1gaf018c0d2fcc6ef2abce07a52115e9da7.html language=enus -->
## TOPIC 00129: RFMXNR_ATTR_SEM_RESULTS_COMPONENT_CARRIER_ABSOLUTE_INTEGRATED_POWER

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__sem__results__component__carrier_1gaf018c0d2fcc6ef2abce07a52115e9da7.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__sem__results__component__carrier_1gaf018c0d2fcc6ef2abce07a52115e9da7.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the power measured over the RFMXNR_ATTR_SEM_COMPONENT_CARRIER_INTEGRATION_BANDWIDTH attribute. This value is expressed in dBm. SyntaxRFMXNR_ATTR_SEM_RESULTS_COMPONENT_CARRIER_ABSOLUTE_INTEGRATED_POWERNumeric ValueData TypeAccessApplies To9469984float64Read-OnlyCarrierRemarks Use "carrier<k>"

### RFMXNR_ATTR_SEM_RESULTS_COMPONENT_CARRIER_ABSOLUTE_INTEGRATED_POWER

Returns the power measured over the [RFMXNR_ATTR_SEM_COMPONENT_CARRIER_INTEGRATION_BANDWIDTH](group____root__ni_r_fmx_n_r__attributes__sem__component__carrier_1gaab7e32d262f07cd95c00b6cf75e50e63.html) attribute. This value is expressed in dBm.

#### Syntax

RFMXNR_ATTR_SEM_RESULTS_COMPONENT_CARRIER_ABSOLUTE_INTEGRATED_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9469984 | float64 | Read-Only | Carrier |

#### Remarks

Use "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result.

Parent topic:

Component Carrier

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__sem__results__lower__offset.html language=enus -->
## TOPIC 00130: Lower Offset

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__sem__results__lower__offset.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__sem__results__lower__offset.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXNR_ATTR_SEM_RESULTS_LOWER_OFFSET_ABSOLUTE_INTEGRATED_POWERReturns the lower (negative) offset segment power. This value is expressed in dBm. RFMXNR_ATTR_SEM_RESULTS_LOWER_OFFSET_ABSOLUTE_PEAK_POWERReturns the peak power in the lower (negative) offset segment

### Lower Offset

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXNR_ATTR_SEM_RESULTS_LOWER_OFFSET_ABSOLUTE_INTEGRATED_POWER | Returns the lower (negative) offset segment power. This value is expressed in dBm. |
| RFMXNR_ATTR_SEM_RESULTS_LOWER_OFFSET_ABSOLUTE_PEAK_POWER | Returns the peak power in the lower (negative) offset segment. This value is expressed in dBm. |
| RFMXNR_ATTR_SEM_RESULTS_LOWER_OFFSET_MARGIN | Returns the margin from the absolute limit mask for lower (negative) offset. Margin is defined as the minimum difference between the spectrum and the limit mask. This value is expressed in dB. |
| RFMXNR_ATTR_SEM_RESULTS_LOWER_OFFSET_MARGIN_ABSOLUTE_POWER | Returns the power at which the Margin occurs in the lower (negative) offset segment. This value is expressed in dBm. |
| RFMXNR_ATTR_SEM_RESULTS_LOWER_OFFSET_MARGIN_FREQUENCY | Returns the frequency at which the Margin occurs in the lower (negative) offset. This value is expressed in Hz. |
| RFMXNR_ATTR_SEM_RESULTS_LOWER_OFFSET_MARGIN_RELATIVE_POWER | Returns the power at which the Margin occurs in the lower (negative) offset segment relative to RFMXNR_ATTR_SEM_RESULTS_TOTAL_AGGREGATED_POWER attribute. This value is expressed in dB. |
| RFMXNR_ATTR_SEM_RESULTS_LOWER_OFFSET_MEASUREMENT_STATUS | Returns the measurement status based on the spectrum emission limits defined by the standard mask type that you configure in the RFMXNR_ATTR_SEM_UPLINK_MASK_TYPE attribute. |
| RFMXNR_ATTR_SEM_RESULTS_LOWER_OFFSET_PEAK_FREQUENCY | Returns the frequency at which the peak power occurs in the lower (negative) offset segment. This value is expressed in Hz. |
| RFMXNR_ATTR_SEM_RESULTS_LOWER_OFFSET_RELATIVE_INTEGRATED_POWER | Returns the power in the lower (negative) offset segment relative to RFMXNR_ATTR_SEM_RESULTS_TOTAL_AGGREGATED_POWER attribute. This value is expressed in dB. |
| RFMXNR_ATTR_SEM_RESULTS_LOWER_OFFSET_RELATIVE_PEAK_POWER | Returns the peak power in the lower (negative) offset segment relative to RFMXNR_ATTR_SEM_RESULTS_TOTAL_AGGREGATED_POWER attribute. This value is expressed in dB. |

#### Attachments

None

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__sem__results__lower__offset_1ga1359e4d333557261b9b090bb6fd5c86f.html language=enus -->
## TOPIC 00131: RFMXNR_ATTR_SEM_RESULTS_LOWER_OFFSET_PEAK_FREQUENCY

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__sem__results__lower__offset_1ga1359e4d333557261b9b090bb6fd5c86f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__sem__results__lower__offset_1ga1359e4d333557261b9b090bb6fd5c86f.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the frequency at which the peak power occurs in the lower (negative) offset segment. This value is expressed in Hz. SyntaxRFMXNR_ATTR_SEM_RESULTS_LOWER_OFFSET_PEAK_FREQUENCYNumeric ValueData TypeAccessApplies To9469993float64Read-OnlyOffsetRemarks Use "offset<k>" or "subblock<n>" or "subbloc

### RFMXNR_ATTR_SEM_RESULTS_LOWER_OFFSET_PEAK_FREQUENCY

Returns the frequency at which the peak power occurs in the lower (negative) offset segment. This value is expressed in Hz.

#### Syntax

RFMXNR_ATTR_SEM_RESULTS_LOWER_OFFSET_PEAK_FREQUENCY

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9469993 | float64 | Read-Only | Offset |

#### Remarks

Use "offset<k>" or "subblock<n>" or "subblock<n>/offset<k>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result.

Parent topic:

Lower Offset

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__sem__results__lower__offset_1ga28c9035fbedd9a616b7ce00aedb08785.html language=enus -->
## TOPIC 00132: RFMXNR_ATTR_SEM_RESULTS_LOWER_OFFSET_RELATIVE_PEAK_POWER

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__sem__results__lower__offset_1ga28c9035fbedd9a616b7ce00aedb08785.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__sem__results__lower__offset_1ga28c9035fbedd9a616b7ce00aedb08785.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the peak power in the lower (negative) offset segment relative to RFMXNR_ATTR_SEM_RESULTS_TOTAL_AGGREGATED_POWER attribute. This value is expressed in dB. SyntaxRFMXNR_ATTR_SEM_RESULTS_LOWER_OFFSET_RELATIVE_PEAK_POWERNumeric ValueData TypeAccessApplies To9469992float64Read-OnlyOffsetRemarks

### RFMXNR_ATTR_SEM_RESULTS_LOWER_OFFSET_RELATIVE_PEAK_POWER

Returns the peak power in the lower (negative) offset segment relative to [RFMXNR_ATTR_SEM_RESULTS_TOTAL_AGGREGATED_POWER](group____root__ni_r_fmx_n_r__attributes__sem__results_1gaba5fe7c25650ebb85322fd66f2410030.html) attribute. This value is expressed in dB.

#### Syntax

RFMXNR_ATTR_SEM_RESULTS_LOWER_OFFSET_RELATIVE_PEAK_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9469992 | float64 | Read-Only | Offset |

#### Remarks

Use "offset<k>" or "subblock<n>" or "subblock<n>/offset<k>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result.

Parent topic:

Lower Offset

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__sem__results__lower__offset_1ga7eb51d3847d573d44247101f3e1d5f9c.html language=enus -->
## TOPIC 00133: RFMXNR_ATTR_SEM_RESULTS_LOWER_OFFSET_MARGIN

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__sem__results__lower__offset_1ga7eb51d3847d573d44247101f3e1d5f9c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__sem__results__lower__offset_1ga7eb51d3847d573d44247101f3e1d5f9c.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the margin from the absolute limit mask for lower (negative) offset. Margin is defined as the minimum difference between the spectrum and the limit mask. This value is expressed in dB. SyntaxRFMXNR_ATTR_SEM_RESULTS_LOWER_OFFSET_MARGINNumeric ValueData TypeAccessApplies To9469994float64Read-O

### RFMXNR_ATTR_SEM_RESULTS_LOWER_OFFSET_MARGIN

Returns the margin from the absolute limit mask for lower (negative) offset. Margin is defined as the minimum difference between the spectrum and the limit mask. This value is expressed in dB.

#### Syntax

RFMXNR_ATTR_SEM_RESULTS_LOWER_OFFSET_MARGIN

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9469994 | float64 | Read-Only | Offset |

#### Remarks

Use "offset<k>" or "subblock<n>" or "subblock<n>/offset<k>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result.

Parent topic:

Lower Offset

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__sem__results__lower__offset_1gaa2edfcaf54a3f3b79f0cf4fe4892599b.html language=enus -->
## TOPIC 00134: RFMXNR_ATTR_SEM_RESULTS_LOWER_OFFSET_MARGIN_FREQUENCY

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__sem__results__lower__offset_1gaa2edfcaf54a3f3b79f0cf4fe4892599b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__sem__results__lower__offset_1gaa2edfcaf54a3f3b79f0cf4fe4892599b.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the frequency at which the Margin occurs in the lower (negative) offset. This value is expressed in Hz. SyntaxRFMXNR_ATTR_SEM_RESULTS_LOWER_OFFSET_MARGIN_FREQUENCYNumeric ValueData TypeAccessApplies To9469997float64Read-OnlyOffsetRemarks Use "offset<k>" or "subblock<n>" or "subblock<n>/offse

### RFMXNR_ATTR_SEM_RESULTS_LOWER_OFFSET_MARGIN_FREQUENCY

Returns the frequency at which the Margin occurs in the lower (negative) offset. This value is expressed in Hz.

#### Syntax

RFMXNR_ATTR_SEM_RESULTS_LOWER_OFFSET_MARGIN_FREQUENCY

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9469997 | float64 | Read-Only | Offset |

#### Remarks

Use "offset<k>" or "subblock<n>" or "subblock<n>/offset<k>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result.

Parent topic:

Lower Offset

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__sem__results__lower__offset_1gaa4a8d5163414f4e208eb90a5c80f8b58.html language=enus -->
## TOPIC 00135: RFMXNR_ATTR_SEM_RESULTS_LOWER_OFFSET_ABSOLUTE_INTEGRATED_POWER

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__sem__results__lower__offset_1gaa4a8d5163414f4e208eb90a5c80f8b58.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__sem__results__lower__offset_1gaa4a8d5163414f4e208eb90a5c80f8b58.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the lower (negative) offset segment power. This value is expressed in dBm. SyntaxRFMXNR_ATTR_SEM_RESULTS_LOWER_OFFSET_ABSOLUTE_INTEGRATED_POWERNumeric ValueData TypeAccessApplies To9469989float64Read-OnlyOffsetRemarks Use "offset<k>" or "subblock<n>" or "subblock<n>/offset<k>" as the Selecto

### RFMXNR_ATTR_SEM_RESULTS_LOWER_OFFSET_ABSOLUTE_INTEGRATED_POWER

Returns the lower (negative) offset segment power. This value is expressed in dBm.

#### Syntax

RFMXNR_ATTR_SEM_RESULTS_LOWER_OFFSET_ABSOLUTE_INTEGRATED_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9469989 | float64 | Read-Only | Offset |

#### Remarks

Use "offset<k>" or "subblock<n>" or "subblock<n>/offset<k>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result.

Parent topic:

Lower Offset

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__sem__results__lower__offset_1gaa8fd9f10b39a7e536fb42ceaf803fcaa.html language=enus -->
## TOPIC 00136: RFMXNR_ATTR_SEM_RESULTS_LOWER_OFFSET_MEASUREMENT_STATUS

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__sem__results__lower__offset_1gaa8fd9f10b39a7e536fb42ceaf803fcaa.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__sem__results__lower__offset_1gaa8fd9f10b39a7e536fb42ceaf803fcaa.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the measurement status based on the spectrum emission limits defined by the standard mask type that you configure in the RFMXNR_ATTR_SEM_UPLINK_MASK_TYPE attribute. SyntaxRFMXNR_ATTR_SEM_RESULTS_LOWER_OFFSET_MEASUREMENT_STATUSNumeric ValueData TypeAccessApplies To9469988int32Read-OnlyOffsetR

### RFMXNR_ATTR_SEM_RESULTS_LOWER_OFFSET_MEASUREMENT_STATUS

Returns the measurement status based on the spectrum emission limits defined by the standard mask type that you configure in the [RFMXNR_ATTR_SEM_UPLINK_MASK_TYPE](group____root__ni_r_fmx_n_r__attributes__sem_1ga3089148cb82acc2035c66bd9ad5d93d6.html) attribute.

#### Syntax

RFMXNR_ATTR_SEM_RESULTS_LOWER_OFFSET_MEASUREMENT_STATUS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9469988 | int32 | Read-Only | Offset |

#### Remarks

Use "offset<k>" or "subblock<n>" or "subblock<n>/offset<k>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result.

| Name | Value | Description |
| --- | --- | --- |
| RFMXNR_VAL_SEM_LOWER_OFFSET_MEASUREMENT_STATUS_FAIL | 0 (0x0) | Indicates that the measurement has failed. |
| RFMXNR_VAL_SEM_LOWER_OFFSET_MEASUREMENT_STATUS_PASS | 1 (0x1) | Indicates that the measurement has passed. |

Parent topic:

Lower Offset

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__sem__results__lower__offset_1gaca2f62180efbbd3120b90eb828112259.html language=enus -->
## TOPIC 00137: RFMXNR_ATTR_SEM_RESULTS_LOWER_OFFSET_MARGIN_ABSOLUTE_POWER

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__sem__results__lower__offset_1gaca2f62180efbbd3120b90eb828112259.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__sem__results__lower__offset_1gaca2f62180efbbd3120b90eb828112259.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the power at which the Margin occurs in the lower (negative) offset segment. This value is expressed in dBm. SyntaxRFMXNR_ATTR_SEM_RESULTS_LOWER_OFFSET_MARGIN_ABSOLUTE_POWERNumeric ValueData TypeAccessApplies To9469995float64Read-OnlyOffsetRemarks Use "offset<k>" or "subblock<n>" or "subbloc

### RFMXNR_ATTR_SEM_RESULTS_LOWER_OFFSET_MARGIN_ABSOLUTE_POWER

Returns the power at which the Margin occurs in the lower (negative) offset segment. This value is expressed in dBm.

#### Syntax

RFMXNR_ATTR_SEM_RESULTS_LOWER_OFFSET_MARGIN_ABSOLUTE_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9469995 | float64 | Read-Only | Offset |

#### Remarks

Use "offset<k>" or "subblock<n>" or "subblock<n>/offset<k>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result.

Parent topic:

Lower Offset

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__sem__results__lower__offset_1gacdf8add4afdb3d0e0af1c91724d3c2a9.html language=enus -->
## TOPIC 00138: RFMXNR_ATTR_SEM_RESULTS_LOWER_OFFSET_ABSOLUTE_PEAK_POWER

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__sem__results__lower__offset_1gacdf8add4afdb3d0e0af1c91724d3c2a9.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__sem__results__lower__offset_1gacdf8add4afdb3d0e0af1c91724d3c2a9.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the peak power in the lower (negative) offset segment. This value is expressed in dBm. SyntaxRFMXNR_ATTR_SEM_RESULTS_LOWER_OFFSET_ABSOLUTE_PEAK_POWERNumeric ValueData TypeAccessApplies To9469991float64Read-OnlyOffsetRemarks Use "offset<k>" or "subblock<n>" or "subblock<n>/offset<k>" as the S

### RFMXNR_ATTR_SEM_RESULTS_LOWER_OFFSET_ABSOLUTE_PEAK_POWER

Returns the peak power in the lower (negative) offset segment. This value is expressed in dBm.

#### Syntax

RFMXNR_ATTR_SEM_RESULTS_LOWER_OFFSET_ABSOLUTE_PEAK_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9469991 | float64 | Read-Only | Offset |

#### Remarks

Use "offset<k>" or "subblock<n>" or "subblock<n>/offset<k>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result.

Parent topic:

Lower Offset

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__sem__results__upper__offset.html language=enus -->
## TOPIC 00139: Upper Offset

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__sem__results__upper__offset.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__sem__results__upper__offset.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXNR_ATTR_SEM_RESULTS_UPPER_OFFSET_ABSOLUTE_INTEGRATED_POWERReturns the upper (positive) offset segment power. This value is expressed in dBm. RFMXNR_ATTR_SEM_RESULTS_UPPER_OFFSET_ABSOLUTE_PEAK_POWERReturns the peak power in the upper (positive) offset segment

### Upper Offset

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXNR_ATTR_SEM_RESULTS_UPPER_OFFSET_ABSOLUTE_INTEGRATED_POWER | Returns the upper (positive) offset segment power. This value is expressed in dBm. |
| RFMXNR_ATTR_SEM_RESULTS_UPPER_OFFSET_ABSOLUTE_PEAK_POWER | Returns the peak power in the upper (positive) offset segment. This value is expressed in dBm. |
| RFMXNR_ATTR_SEM_RESULTS_UPPER_OFFSET_MARGIN | Returns the margin from the absolute limit mask for upper (positive) offset. Margin is defined as the minimum difference between the spectrum and the limit mask. This value is expressed in dB. |
| RFMXNR_ATTR_SEM_RESULTS_UPPER_OFFSET_MARGIN_ABSOLUTE_POWER | Returns the power at which the Margin occurs in the upper (positive) offset segment. This value is expressed in dBm. |
| RFMXNR_ATTR_SEM_RESULTS_UPPER_OFFSET_MARGIN_FREQUENCY | Returns the frequency at which the Margin occurs in the upper (positive) offset. This value is expressed in Hz. |
| RFMXNR_ATTR_SEM_RESULTS_UPPER_OFFSET_MARGIN_RELATIVE_POWER | Returns the power at which the Margin occurs in the upper (positive) offset segment relative to RFMXNR_ATTR_SEM_RESULTS_TOTAL_AGGREGATED_POWER attribute. This value is expressed in dB. |
| RFMXNR_ATTR_SEM_RESULTS_UPPER_OFFSET_MEASUREMENT_STATUS | Returns the measurement status based on the user-configured standard measurement limits. Spectrum emission limits can be defined by setting RFMXNR_ATTR_SEM_UPLINK_MASK_TYPE attribute. |
| RFMXNR_ATTR_SEM_RESULTS_UPPER_OFFSET_PEAK_FREQUENCY | Returns the frequency at which the peak power occurs in the upper (positive)offset segment. This value is expressed in Hz. |
| RFMXNR_ATTR_SEM_RESULTS_UPPER_OFFSET_RELATIVE_INTEGRATED_POWER | Returns the power in the upper (positive) offset segment relative to RFMXNR_ATTR_SEM_RESULTS_TOTAL_AGGREGATED_POWER attribute. This value is expressed in dB. |
| RFMXNR_ATTR_SEM_RESULTS_UPPER_OFFSET_RELATIVE_PEAK_POWER | Returns the peak power in the upper (positive) offset segment relative to RFMXNR_ATTR_SEM_RESULTS_TOTAL_AGGREGATED_POWER attribute. This value is expressed in dB. |

#### Attachments

None

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__sem__results__upper__offset_1ga34eb288000b615265bc36c43e23072af.html language=enus -->
## TOPIC 00140: RFMXNR_ATTR_SEM_RESULTS_UPPER_OFFSET_RELATIVE_INTEGRATED_POWER

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__sem__results__upper__offset_1ga34eb288000b615265bc36c43e23072af.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__sem__results__upper__offset_1ga34eb288000b615265bc36c43e23072af.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the power in the upper (positive) offset segment relative to RFMXNR_ATTR_SEM_RESULTS_TOTAL_AGGREGATED_POWER attribute. This value is expressed in dB. SyntaxRFMXNR_ATTR_SEM_RESULTS_UPPER_OFFSET_RELATIVE_INTEGRATED_POWERNumeric ValueData TypeAccessApplies To9470000float64Read-OnlyOffsetRemarks

### RFMXNR_ATTR_SEM_RESULTS_UPPER_OFFSET_RELATIVE_INTEGRATED_POWER

Returns the power in the upper (positive) offset segment relative to [RFMXNR_ATTR_SEM_RESULTS_TOTAL_AGGREGATED_POWER](group____root__ni_r_fmx_n_r__attributes__sem__results_1gaba5fe7c25650ebb85322fd66f2410030.html) attribute. This value is expressed in dB.

#### Syntax

RFMXNR_ATTR_SEM_RESULTS_UPPER_OFFSET_RELATIVE_INTEGRATED_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9470000 | float64 | Read-Only | Offset |

#### Remarks

Use "offset<k>" or "subblock<n>" or "subblock<n>/offset<k>" as the selector string to read this result.

Parent topic:

Upper Offset

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__sem__results__upper__offset_1ga9f6aa295f4897f9b691f8caa53e3d51b.html language=enus -->
## TOPIC 00141: RFMXNR_ATTR_SEM_RESULTS_UPPER_OFFSET_PEAK_FREQUENCY

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__sem__results__upper__offset_1ga9f6aa295f4897f9b691f8caa53e3d51b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__sem__results__upper__offset_1ga9f6aa295f4897f9b691f8caa53e3d51b.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the frequency at which the peak power occurs in the upper (positive)offset segment. This value is expressed in Hz. SyntaxRFMXNR_ATTR_SEM_RESULTS_UPPER_OFFSET_PEAK_FREQUENCYNumeric ValueData TypeAccessApplies To9470003float64Read-OnlyOffsetRemarks Use "offset<k>" or "subblock<n>" or "subblock

### RFMXNR_ATTR_SEM_RESULTS_UPPER_OFFSET_PEAK_FREQUENCY

Returns the frequency at which the peak power occurs in the upper (positive)offset segment. This value is expressed in Hz.

#### Syntax

RFMXNR_ATTR_SEM_RESULTS_UPPER_OFFSET_PEAK_FREQUENCY

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9470003 | float64 | Read-Only | Offset |

#### Remarks

Use "offset<k>" or "subblock<n>" or "subblock<n>/offset<k>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result.

Parent topic:

Upper Offset

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__sem__results__upper__offset_1gae3df6cb6ede20b7a253b34ce281021f6.html language=enus -->
## TOPIC 00142: RFMXNR_ATTR_SEM_RESULTS_UPPER_OFFSET_ABSOLUTE_PEAK_POWER

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__sem__results__upper__offset_1gae3df6cb6ede20b7a253b34ce281021f6.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__sem__results__upper__offset_1gae3df6cb6ede20b7a253b34ce281021f6.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the peak power in the upper (positive) offset segment. This value is expressed in dBm. SyntaxRFMXNR_ATTR_SEM_RESULTS_UPPER_OFFSET_ABSOLUTE_PEAK_POWERNumeric ValueData TypeAccessApplies To9470001float64Read-OnlyOffsetRemarks Use "offset<k>" or "subblock<n>" or "subblock<n>/offset<k>" as the S

### RFMXNR_ATTR_SEM_RESULTS_UPPER_OFFSET_ABSOLUTE_PEAK_POWER

Returns the peak power in the upper (positive) offset segment. This value is expressed in dBm.

#### Syntax

RFMXNR_ATTR_SEM_RESULTS_UPPER_OFFSET_ABSOLUTE_PEAK_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9470001 | float64 | Read-Only | Offset |

#### Remarks

Use "offset<k>" or "subblock<n>" or "subblock<n>/offset<k>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result.

Parent topic:

Upper Offset

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__sem__results__upper__offset_1gaff83d3c960fc7cdca6249a9a09aef889.html language=enus -->
## TOPIC 00143: RFMXNR_ATTR_SEM_RESULTS_UPPER_OFFSET_MARGIN_FREQUENCY

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__sem__results__upper__offset_1gaff83d3c960fc7cdca6249a9a09aef889.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__sem__results__upper__offset_1gaff83d3c960fc7cdca6249a9a09aef889.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the frequency at which the Margin occurs in the upper (positive) offset. This value is expressed in Hz. SyntaxRFMXNR_ATTR_SEM_RESULTS_UPPER_OFFSET_MARGIN_FREQUENCYNumeric ValueData TypeAccessApplies To9470007float64Read-OnlyOffsetRemarks Use "offset<k>" or "subblock<n>" or "subblock<n>/offse

### RFMXNR_ATTR_SEM_RESULTS_UPPER_OFFSET_MARGIN_FREQUENCY

Returns the frequency at which the Margin occurs in the upper (positive) offset. This value is expressed in Hz.

#### Syntax

RFMXNR_ATTR_SEM_RESULTS_UPPER_OFFSET_MARGIN_FREQUENCY

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9470007 | float64 | Read-Only | Offset |

#### Remarks

Use "offset<k>" or "subblock<n>" or "subblock<n>/offset<k>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result.

Parent topic:

Upper Offset

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__sem__sweep__time.html language=enus -->
## TOPIC 00144: Sweep Time

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__sem__sweep__time.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__sem__sweep__time.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXNR_ATTR_SEM_SWEEP_TIME_AUTOSpecifies whether the measurement sets the sweep time. RFMXNR_ATTR_SEM_SWEEP_TIME_INTERVALSpecifies the sweep time when you set the RFMXNR_ATTR_SEM_SWEEP_TIME_AUTO attribute to False. This value is expressed in seconds. Attachments

### Sweep Time

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXNR_ATTR_SEM_SWEEP_TIME_AUTO | Specifies whether the measurement sets the sweep time. |
| RFMXNR_ATTR_SEM_SWEEP_TIME_INTERVAL | Specifies the sweep time when you set the RFMXNR_ATTR_SEM_SWEEP_TIME_AUTO attribute to False. This value is expressed in seconds. |

#### Attachments

None

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__sem__sweep__time_1ga69249b131f22e440e80402dca0b00c20.html language=enus -->
## TOPIC 00145: RFMXNR_ATTR_SEM_SWEEP_TIME_INTERVAL

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__sem__sweep__time_1ga69249b131f22e440e80402dca0b00c20.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__sem__sweep__time_1ga69249b131f22e440e80402dca0b00c20.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the sweep time when you set the RFMXNR_ATTR_SEM_SWEEP_TIME_AUTO attribute to False. This value is expressed in seconds. SyntaxRFMXNR_ATTR_SEM_SWEEP_TIME_INTERVALNumeric ValueData TypeAccessApplies To9469971float64Read/WriteN/ARemarks You do not need to use a selector string to configure or

### RFMXNR_ATTR_SEM_SWEEP_TIME_INTERVAL

Specifies the sweep time when you set the [RFMXNR_ATTR_SEM_SWEEP_TIME_AUTO](group____root__ni_r_fmx_n_r__attributes__sem__sweep__time_1gac0403cad2659429f952350c3304918b3.html) attribute to **False**. This value is expressed in seconds.

#### Syntax

RFMXNR_ATTR_SEM_SWEEP_TIME_INTERVAL

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9469971 | float64 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 1 ms.

Parent topic:

Sweep Time

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__trigger__iq__power__edge_1ga358594bab97f2bed9be795d08a60f3c0.html language=enus -->
## TOPIC 00146: RFMXNR_ATTR_IQ_POWER_EDGE_TRIGGER_SOURCE

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__trigger__iq__power__edge_1ga358594bab97f2bed9be795d08a60f3c0.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__trigger__iq__power__edge_1ga358594bab97f2bed9be795d08a60f3c0.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the channel from which the device monitors the trigger. SyntaxRFMXNR_ATTR_IQ_POWER_EDGE_TRIGGER_SOURCENumeric ValueData TypeAccessApplies To9437191char[]Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer

### RFMXNR_ATTR_IQ_POWER_EDGE_TRIGGER_SOURCE

Specifies the channel from which the device monitors the trigger.

#### Syntax

RFMXNR_ATTR_IQ_POWER_EDGE_TRIGGER_SOURCE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9437191 | char[] | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value of this attribute is hardware dependent.

Parent topic:

IQ Power Edge

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__trigger__iq__power__edge_1ga9567fc3a6ffa985698e86a844721e06d.html language=enus -->
## TOPIC 00147: RFMXNR_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__trigger__iq__power__edge_1ga9567fc3a6ffa985698e86a844721e06d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__trigger__iq__power__edge_1ga9567fc3a6ffa985698e86a844721e06d.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the reference for the RFMXNR_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL attribute. The IQ Power Edge Level Type attribute is used only when you set the RFMXNR_ATTR_TRIGGER_TYPE attribute to IQ Power Edge. SyntaxRFMXNR_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPENumeric ValueData TypeAccessApplies To9441279

### RFMXNR_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE

Specifies the reference for the [RFMXNR_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL](group____root__ni_r_fmx_n_r__attributes__trigger__iq__power__edge_1gab2caf9541118577461d6f693280f55b8.html) attribute. The IQ Power Edge Level Type attribute is used only when you set the [RFMXNR_ATTR_TRIGGER_TYPE](group____root__ni_r_fmx_n_r__attributes__trigger_1gaf64fe2d3e807b4f3196f811c352537ca.html) attribute to **IQ Power Edge**.

#### Syntax

RFMXNR_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9441279 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **Relative**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXNR_VAL_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_RELATIVE | 0 (0x0) | The IQ Power Edge Level attribute is relative to the value of the RFMXNR_ATTR_REFERENCE_LEVEL attribute. |
| RFMXNR_VAL_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_ABSOLUTE | 1 (0x1) | The IQ Power Edge Level attribute specifies the absolute power. |

Parent topic:

IQ Power Edge

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__trigger__minimum__quiet__time.html language=enus -->
## TOPIC 00148: Minimum Quiet Time

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__trigger__minimum__quiet__time.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__trigger__minimum__quiet__time.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXNR_ATTR_TRIGGER_MINIMUM_QUIET_TIME_DURATIONSpecifies the time duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. This value is expressed in seconds. If you set the RFMXNR_ATTR_IQ_POWER_EDGE_TRIGGER_SLOPE a

### Minimum Quiet Time

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXNR_ATTR_TRIGGER_MINIMUM_QUIET_TIME_DURATION | Specifies the time duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. This value is expressed in seconds. If you set the RFMXNR_ATTR_IQ_POWER_EDGE_TRIGGER_SLOPE attribute to Rising Slope, the signal is quiet below the trigger level. If you set the IQ Power Edge Slope attribute to Falling Slope, the signal is quiet above the trigger level. |
| RFMXNR_ATTR_TRIGGER_MINIMUM_QUIET_TIME_MODE | Specifies whether the measurement computes the minimum quiet time used for triggering. |

#### Attachments

None

Parent topic:

Trigger

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__trigger__minimum__quiet__time_1gacd11ce7a14b011e5a249b81366c38260.html language=enus -->
## TOPIC 00149: RFMXNR_ATTR_TRIGGER_MINIMUM_QUIET_TIME_MODE

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__trigger__minimum__quiet__time_1gacd11ce7a14b011e5a249b81366c38260.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__trigger__minimum__quiet__time_1gacd11ce7a14b011e5a249b81366c38260.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement computes the minimum quiet time used for triggering. SyntaxRFMXNR_ATTR_TRIGGER_MINIMUM_QUIET_TIME_MODENumeric ValueData TypeAccessApplies To9437195int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default

### RFMXNR_ATTR_TRIGGER_MINIMUM_QUIET_TIME_MODE

Specifies whether the measurement computes the minimum quiet time used for triggering.

#### Syntax

RFMXNR_ATTR_TRIGGER_MINIMUM_QUIET_TIME_MODE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9437195 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **Auto**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXNR_VAL_TRIGGER_MINIMUM_QUIET_TIME_MODE_MANUAL | 0 (0x0) | The minimum quiet time for triggering is the value of the RFMXNR_ATTR_TRIGGER_MINIMUM_QUIET_TIME_DURATION attribute. |
| RFMXNR_VAL_TRIGGER_MINIMUM_QUIET_TIME_MODE_AUTO | 1 (0x1) | The measurement computes the minimum quiet time used for triggering. |

Parent topic:

Minimum Quiet Time

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__trigger__minimum__quiet__time_1gae44559d941c55f8a6e835ed912869ae7.html language=enus -->
## TOPIC 00150: RFMXNR_ATTR_TRIGGER_MINIMUM_QUIET_TIME_DURATION

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__trigger__minimum__quiet__time_1gae44559d941c55f8a6e835ed912869ae7.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__trigger__minimum__quiet__time_1gae44559d941c55f8a6e835ed912869ae7.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the time duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. This value is expressed in seconds. If you set the RFMXNR_ATTR_IQ_POWER_EDGE_TRIGGER_SLOPE attribute to Rising Slope, the signal is quiet below the trigger level. If you set the

### RFMXNR_ATTR_TRIGGER_MINIMUM_QUIET_TIME_DURATION

Specifies the time duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. This value is expressed in seconds. If you set the [RFMXNR_ATTR_IQ_POWER_EDGE_TRIGGER_SLOPE](group____root__ni_r_fmx_n_r__attributes__trigger__iq__power__edge_1gaf89d49201d5996877fc4c8483638612b.html) attribute to **Rising Slope**, the signal is quiet below the trigger level. If you set the IQ Power Edge Slope attribute to **Falling Slope**, the signal is quiet above the trigger level.

#### Syntax

RFMXNR_ATTR_TRIGGER_MINIMUM_QUIET_TIME_DURATION

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9437196 | float64 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default of this attribute is hardware dependent.

Parent topic:

Minimum Quiet Time

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__txp_1gabdc76402d800def1dfff469373d84ada.html language=enus -->
## TOPIC 00151: RFMXNR_ATTR_TXP_ALL_TRACES_ENABLED

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__txp_1gabdc76402d800def1dfff469373d84ada.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__txp_1gabdc76402d800def1dfff469373d84ada.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enables the traces to be stored and retrieved after the TXP measurement is performed. SyntaxRFMXNR_ATTR_TXP_ALL_TRACES_ENABLEDNumeric ValueData TypeAccessApplies To9465863int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal ins

### RFMXNR_ATTR_TXP_ALL_TRACES_ENABLED

Enables the traces to be stored and retrieved after the TXP measurement is performed.

#### Syntax

RFMXNR_ATTR_TXP_ALL_TRACES_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9465863 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is False.

Parent topic:

TXP

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__txp_1gad8c194b9c481d8c3122c925c37925f9d.html language=enus -->
## TOPIC 00152: RFMXNR_ATTR_TXP_MEASUREMENT_INTERVAL

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__txp_1gad8c194b9c481d8c3122c925c37925f9d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__txp_1gad8c194b9c481d8c3122c925c37925f9d.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the measurement interval. This value is expressed in seconds. SyntaxRFMXNR_ATTR_TXP_MEASUREMENT_INTERVALNumeric ValueData TypeAccessApplies To9465859float64Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Ref

### RFMXNR_ATTR_TXP_MEASUREMENT_INTERVAL

Specifies the measurement interval. This value is expressed in seconds.

#### Syntax

RFMXNR_ATTR_TXP_MEASUREMENT_INTERVAL

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9465859 | float64 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 1 ms.

Parent topic:

TXP

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__txp__averaging.html language=enus -->
## TOPIC 00153: Averaging

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__txp__averaging.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__txp__averaging.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXNR_ATTR_TXP_AVERAGING_COUNTSpecifies the number of acquisitions used for averaging when RFMXNR_ATTR_TXP_AVERAGING_ENABLED is True. RFMXNR_ATTR_TXP_AVERAGING_ENABLEDSpecifies whether to enable averaging for TXP measurement. AttachmentsNone

### Averaging

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXNR_ATTR_TXP_AVERAGING_COUNT | Specifies the number of acquisitions used for averaging when RFMXNR_ATTR_TXP_AVERAGING_ENABLED is True. |
| RFMXNR_ATTR_TXP_AVERAGING_ENABLED | Specifies whether to enable averaging for TXP measurement. |

#### Attachments

None

Parent topic:

TXP

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__txp__averaging_1ga27036b667b3b290e922855121909476d.html language=enus -->
## TOPIC 00154: RFMXNR_ATTR_TXP_AVERAGING_ENABLED

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__txp__averaging_1ga27036b667b3b290e922855121909476d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__txp__averaging_1ga27036b667b3b290e922855121909476d.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable averaging for TXP measurement. SyntaxRFMXNR_ATTR_TXP_AVERAGING_ENABLEDNumeric ValueData TypeAccessApplies To9465860int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector

### RFMXNR_ATTR_TXP_AVERAGING_ENABLED

Specifies whether to enable averaging for TXP measurement.

#### Syntax

RFMXNR_ATTR_TXP_AVERAGING_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9465860 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **False**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXNR_VAL_TXP_AVERAGING_ENABLED_FALSE | 0 (0x0) | The number of acquisitions is 1. |
| RFMXNR_VAL_TXP_AVERAGING_ENABLED_TRUE | 1 (0x1) | The measurement uses the RFMXNR_ATTR_TXP_AVERAGING_COUNT for the number of acquisitions over which the measurement is averaged. |

Parent topic:

Averaging

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__txp__averaging_1ga3c4dd9fc4f152d2e346a0cadf51efdae.html language=enus -->
## TOPIC 00155: RFMXNR_ATTR_TXP_AVERAGING_COUNT

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__txp__averaging_1ga3c4dd9fc4f152d2e346a0cadf51efdae.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__txp__averaging_1ga3c4dd9fc4f152d2e346a0cadf51efdae.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of acquisitions used for averaging when RFMXNR_ATTR_TXP_AVERAGING_ENABLED is True. SyntaxRFMXNR_ATTR_TXP_AVERAGING_COUNTNumeric ValueData TypeAccessApplies To9465861int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the def

### RFMXNR_ATTR_TXP_AVERAGING_COUNT

Specifies the number of acquisitions used for averaging when [RFMXNR_ATTR_TXP_AVERAGING_ENABLED](group____root__ni_r_fmx_n_r__attributes__txp__averaging_1ga27036b667b3b290e922855121909476d.html) is **True**.

#### Syntax

RFMXNR_ATTR_TXP_AVERAGING_COUNT

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9465861 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 10.

Parent topic:

Averaging

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__txp__results.html language=enus -->
## TOPIC 00156: Results

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__txp__results.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__txp__results.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXNR_ATTR_TXP_RESULTS_AVERAGE_POWER_MEANReturns the average power of the acquired signal. RFMXNR_ATTR_TXP_RESULTS_PEAK_POWER_MAXIMUMReturns the peak power of the acquired signal. AttachmentsNone

### Results

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXNR_ATTR_TXP_RESULTS_AVERAGE_POWER_MEAN | Returns the average power of the acquired signal. |
| RFMXNR_ATTR_TXP_RESULTS_PEAK_POWER_MAXIMUM | Returns the peak power of the acquired signal. |

#### Attachments

None

Parent topic:

TXP

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__attributes__txp__results_1ga2c3b2475b9ac4bfe6a3cca972e5f56f1.html language=enus -->
## TOPIC 00157: RFMXNR_ATTR_TXP_RESULTS_AVERAGE_POWER_MEAN

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__attributes__txp__results_1ga2c3b2475b9ac4bfe6a3cca972e5f56f1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__attributes__txp__results_1ga2c3b2475b9ac4bfe6a3cca972e5f56f1.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the average power of the acquired signal. SyntaxRFMXNR_ATTR_TXP_RESULTS_AVERAGE_POWER_MEANNumeric ValueData TypeAccessApplies To9465866float64Read-OnlyN/ARemarks When you set the RFMXNR_ATTR_TXP_AVERAGING_ENABLED attribute to True, it returns the max of the peak power computed for each avera

### RFMXNR_ATTR_TXP_RESULTS_AVERAGE_POWER_MEAN

Returns the average power of the acquired signal.

#### Syntax

RFMXNR_ATTR_TXP_RESULTS_AVERAGE_POWER_MEAN

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9465866 | float64 | Read-Only | N/A |

#### Remarks

When you set the [RFMXNR_ATTR_TXP_AVERAGING_ENABLED](group____root__ni_r_fmx_n_r__attributes__txp__averaging_1ga27036b667b3b290e922855121909476d.html) attribute to **True**, it returns the max of the peak power computed for each averaging count.

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **dBm**.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions.html language=enus -->
## TOPIC 00158: Functions

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsAdvancedBuild StringConfigurationFetchSelect MeasurementSet and Get AttributesUtilityGroup membersNameDescriptionRFmxNR_CloseCloses the session to the device. RFmxNR_GetErrorRetrieves and then clears the error information for the session or the current execution thread. You must provide a char

### Functions

#### Groups

- Advanced
- Build String
- Configuration
- Fetch
- Select Measurement
- Set and Get Attributes
- Utility

#### Group members

| Name | Description |
| --- | --- |
| RFmxNR_Close | Closes the session to the device. |
| RFmxNR_GetError | Retrieves and then clears the error information for the session or the current execution thread. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the errorDescriptionBufferSize parameter. |
| RFmxNR_GetErrorString | Converts a status code returned by an RFmxNR function into a user-readable string. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the errorDescriptionBufferSize parameter. |
| RFmxNR_Initialize | Creates an RFmx session to the device you specify through the resourceName parameter, and returns a handleOut that identifies this device in all subsequent RFmx functions. |
| RFmxNR_Initiate | Initiates all enabled measurements. Call this function after configuring the signal and measurement. This function asynchronously launches measurements in the background and immediately returns to the caller program. You can fetch measurement results using the Fetch functions or result attributes in the attribute node. To get the status of measurements, use the RFmxNR_WaitForMeasurementComplete function or RFmxNR_CheckMeasurementStatus function. |
| RFmxNR_ModAccFetchPDSCH4096QAMConstellationTrace |  |
| RFmxNR_ModAccFetchPDSCH4096QAMConstellationTraceSplit |  |

#### Attachments

None

Parent topic:

niRFmxNR.h

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions_1ga1feff952d2974304538c63402d9188e6.html language=enus -->
## TOPIC 00159: RFmxNR_Initiate

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions_1ga1feff952d2974304538c63402d9188e6.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions_1ga1feff952d2974304538c63402d9188e6.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initiates all enabled measurements. Call this function after configuring the signal and measurement. This function asynchronously launches measurements in the background and immediately returns to the caller program. You can fetch measurement results using the Fetch functions or result attributes in

### RFmxNR_Initiate

Initiates all enabled measurements. Call this function after configuring the signal and measurement. This function asynchronously launches measurements in the background and immediately returns to the caller program. You can fetch measurement results using the Fetch functions or result attributes in the attribute node. To get the status of measurements, use the [RFmxNR_WaitForMeasurementComplete](group____root__ni_r_fmx_n_r__functions__utility_1ga6663f492337a1cecdf2ad4ffe6705c7b.html) function or [RFmxNR_CheckMeasurementStatus](group____root__ni_r_fmx_n_r__functions__utility_1ga6de3d436bd9e3410c3478ea4531388f1.html) function.

#### Syntax

int32 __stdcall RFmxNR_Initiate(niRFmxInstrHandle instrumentHandle, char selectorString[], char resultName[])

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies the signal name and result name. The result name can either be specified through this input or the Result Name parameter. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name in this parameter, either the result name specified by the Result Name parameter or the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxNR_BuildSignalString function to build the Selector String. |
| resultName | [in] | char[] | This parameter specifies the name to be associated with measurement results. Provide a unique name, such as "r1" to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. The default value is "" (empty string) which refers to default result instance.Example:"result::r1""r1" |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html language=enus -->
## TOPIC 00160: RFmxNR_GetError

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Retrieves and then clears the error information for the session or the current execution thread. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the errorDescriptionBufferSize parameter. Syntaxint32 __stdcall RFmxNR_GetError(niRFmxInstrHand

### RFmxNR_GetError

Retrieves and then clears the error information for the session or the current execution thread. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **errorDescriptionBufferSize** parameter.

#### Syntax

int32 __stdcall RFmxNR_GetError(niRFmxInstrHandle instrumentHandle, int32 *errorCode, int32 errorDescriptionBufferSize, char errorDescription[])

#### Remarks

If the error description, including the terminating NULL byte, is larger than the size you indicate in the **errorDescriptionBufferSize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

If you want to call this function just to get the required buffer size, you must pass 0 for **errorDescriptionBufferSize** and NULL for the errorDescription buffer.

Note

Use the [RFmxNR_GetErrorString](group____root__ni_r_fmx_n_r__functions_1gab957e4198104d70ea490563b4bdc65c9.html) function if the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function does not return an error message.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Specifies the RFmx session. If a valid session handle is passed, the last error stored in that session is retrieved. You can pass NULL to retrieve the last error stored in the current execution thread. |
| errorCode | [out] | int32 * | Returns the error code for the session or execution thread. If you pass 0 for the errorDescriptionBufferSize parameter, you can pass NULL for the errorCode parameter. |
| errorDescriptionBufferSize | [in] | int32 | Passes the number of bytes in the char array you specify in errorDescriptionIf the error description, including the terminating NULL byte, contains more bytes than you indicate in this parameter, the function copies errorDescriptionBufferSize - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the size of the buffer that you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7. |
| errorDescription | [out] | char[] | Returns the error description for the session or execution thread. If there is no description, this function returns an empty string.The buffer must contain at least as many elements as the value you specify with the errorDescriptionBufferSize parameter. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

When the **statusOrRequiredSize** return value returns the buffer size, the status code is not returned.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions_1gab957e4198104d70ea490563b4bdc65c9.html language=enus -->
## TOPIC 00161: RFmxNR_GetErrorString

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions_1gab957e4198104d70ea490563b4bdc65c9.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions_1gab957e4198104d70ea490563b4bdc65c9.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts a status code returned by an RFmxNR function into a user-readable string. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the errorDescriptionBufferSize parameter. Syntaxint32 __stdcall RFmxNR_GetErrorString(niRFmxInstrHandle instr

### RFmxNR_GetErrorString

Converts a status code returned by an RFmxNR function into a user-readable string. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **errorDescriptionBufferSize** parameter.

#### Syntax

int32 __stdcall RFmxNR_GetErrorString(niRFmxInstrHandle instrumentHandle, int32 errorCode, int32 errorDescriptionBufferSize, char errorDescription[])

#### Remarks

If the error description, including the terminating NULL byte, is larger than the size you indicate in the **errorDescriptionBufferSize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

If you want to call this function just to get the required buffer size, you must pass 0 for **errorDescriptionBufferSize** and NULL for the **errorDescription** buffer.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxNR_Initialize function. |
| errorCode | [in] | int32 | Passes the statusOrRequiredSize parameter that is returned from any RFmxNR function. |
| errorDescriptionBufferSize | [in] | int32 | Passes the number of bytes in the char array you specify in errorDescription.If the error description, including the terminating NULL byte, contains more bytes than you indicate in this parameter, the function copies errorDescriptionBufferSize - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the size of the buffer that you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7. |
| errorDescription | [out] | char[] | Returns the user-readable message string that corresponds to the status code you specify.If you pass 0 for errorDescriptionBufferSize, you can pass NULL for the errorDescription buffer parameter to get the size of error description message. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

When the **statusOrRequiredSize** return value returns the buffer size, the status code is not returned.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions_1gacef673c10614868d18b20236577ead50.html language=enus -->
## TOPIC 00162: RFmxNR_Close

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions_1gacef673c10614868d18b20236577ead50.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions_1gacef673c10614868d18b20236577ead50.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Closes the session to the device. Syntaxint32 __stdcall RFmxNR_Close(niRFmxInstrHandle instrumentHandle, int32 forceDestroy)RemarksThis function is a wrapper over the RFmx Instruments API, and calls the RFmxInstr_Close function.Enabling the SFP (Soft Front Panel) debug has a performance impact. For

### RFmxNR_Close

Closes the session to the device.

#### Syntax

int32 __stdcall RFmxNR_Close(niRFmxInstrHandle instrumentHandle, int32 forceDestroy)

#### Remarks

This function is a wrapper over the RFmx Instruments API, and calls the [RFmxInstr_Close](/csh?context=rfmxinstr_rfmxinstrcref_function_close) function.

Note

Enabling the SFP (Soft Front Panel) debug has a performance impact. For best performance, NI recommends disabling SFP debug. SFP debug can be enabled/disabled from either the RF Signal Analyzer panel in InstrumentStudio, the RFSA Soft Front Panel, or the RFmx Debug Configuration Utility.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxNR_Initialize function. |
| forceDestroy | [in] | int32 | Specifies whether to destroy the RFmx session.ValueDescriptionRFMXNR_VAL_FALSE (0)Destroys the RFmx session. Call the RFmxNR_Close function a number of times equal to the number of times you obtained a reference to the RFmx session.RFMXNR_VAL_TRUE (1)Destroys the RFmx session. You do not have to call the RFmxNR_Close function multiple times. Destroying the RFmx session invalidates all references to the session. |
| Value | Description |  |  |
| RFMXNR_VAL_FALSE (0) | Destroys the RFmx session. Call the RFmxNR_Close function a number of times equal to the number of times you obtained a reference to the RFmx session. |  |  |
| RFMXNR_VAL_TRUE (1) | Destroys the RFmx session. You do not have to call the RFmxNR_Close function multiple times. Destroying the RFmx session invalidates all references to the session. |  |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions_1gaf3a0417fc49db1defa718bd11df5f975.html language=enus -->
## TOPIC 00163: RFmxNR_Initialize

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions_1gaf3a0417fc49db1defa718bd11df5f975.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions_1gaf3a0417fc49db1defa718bd11df5f975.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an RFmx session to the device you specify through the resourceName parameter, and returns a handleOut that identifies this device in all subsequent RFmx functions. Syntaxint32 __stdcall RFmxNR_Initialize(char resourceName[], char optionString[], niRFmxInstrHandle *handleOut, int32 *isNewSess

### RFmxNR_Initialize

Creates an RFmx session to the device you specify through the **resourceName** parameter, and returns a **handleOut** that identifies this device in all subsequent RFmx functions.

#### Syntax

int32 __stdcall RFmxNR_Initialize(char resourceName[], char optionString[], niRFmxInstrHandle *handleOut, int32 *isNewSession)

#### Remarks

This function is a wrapper over the RFmx Instruments API, and calls the [RFmxInstr_Initialize](/csh?context=rfmxinstr_rfmxinstrcref_function_initialize) function.

Note

Enabling the SFP (Soft Front Panel) debug has a performance impact. For best performance, NI recommends disabling SFP debug. SFP debug can be enabled/disabled from either the RF Signal Analyzer panel in InstrumentStudio, the RFSA Soft Front Panel, or the RFmx Debug Configuration Utility.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| resourceName | [in] | char[] | Specifies the resource name of the device to initialize.The following table shows examples of how to specify the resource name.Example #Device TypeSyntax1myRFmxDeviceRFmx device, device name is "myRFmxDevice"2myLogicalNameIVI logical name or virtual instrument, name is "myLogicalName"For NI-DAQmx devices, the syntax is the device name specified in MAX, as shown in Example 1. Typical default names for NI-DAQmx devices in MAX are Dev1 or PXI1Slot2. You can rename an NI-DAQmx device by right-clicking the name in MAX, selecting Rename from the pull-down menu, and entering a new name. You can also pass the name of an IVI logical name configured with the IVI Configuration utility. For additional information about IVI, refer to the IVI section of the Measurement & Automation Explorer Help. |
| Example # | Device Type | Syntax |  |
| 1 | myRFmxDevice | RFmx device, device name is "myRFmxDevice" |  |
| 2 | myLogicalName | IVI logical name or virtual instrument, name is "myLogicalName" |  |
| optionString | [in] | char[] | Sets the initial value of certain attributes for the session.The following attributes are used in this parameter:RFmxSetupSimulateAnalysisOnlyFor more information about attributes used in this parameter, refer to the NI RF Vector Signal Analyzers Help.The format of this string is "AttributeName=Value", where AttributeName is the name of the attribute and Value is the value to which the attribute is set. For example, you can simulate an PXIe-5663E using either of the following strings:"Simulate=1, RFmxSetup=Model:5663E""Simulate=1, RFmxSetup=Model:5601; Digitizer:5622; LO:5652; LOBoardType:PXIe"To set multiple attributes, separate their assignments with a comma.To use FPGA extensions, specify the custom LabVIEW FPGA bitfile to use with the bitfile specifier within the RFmxSetup string. For example, "RFmxSetup=bitfile:yourbitfile.lvbitx" specifies that RFmx uses yourbitfile.lvbitx as the LabVIEW FPGA bitfile for the session.To use AnalysisOnly mode, specify the string as "AnalysisOnly=1". In this mode, user is responsible for waveform acquisition and RFmx driver will perform analysis on user specified IQ waveform or Spectrum. Use personality specific Analyze functions to perform measurements.Note To simulate a device using the PXIe-5622 (25 MHz) digitizer, set the Digitizer field to 5622_25MHz_DDC and the Simulate field to 1. You can set the Digitizer field to 5622_25MHz_DDC only when using the PXIe-5665.To use external NI Source Measure Units (SMU) as the noise source power supply for the noise figure (NF) measurement, use the "NoiseSourcePowerSupply" specifier within the RFmxSetup string. For example, "RFmxSetup= NoiseSourcePowerSupply:myDCPower[0]" configures RFmx to use channel 0 on myDCPower SMU device for powering the noise source. You should allocate a dedicated SMU channel for RFmx.Note RFmx supports PXIe-4138, PXIe-4139, and PXIe-4139 (40 W) SMUs. |
| handleOut | [out] | niRFmxInstrHandle * | Identifies your instrument session. |
| isNewSession | [out] | int32 * | Returns RFMXNR_VAL_TRUE if the function created a new session, or RFMXNR_VAL_FALSE if the function returned a reference to an existing session. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__advanced.html language=enus -->
## TOPIC 00164: Advanced

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__advanced.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__advanced.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsAnalyze2ListGroup membersNameDescriptionRFmxNR_AbortMeasurementsStops acquisition and measurements associated with signal instance that you specify in the Selector String parameter, which were previously initiated by the RFmxNR_Initiate function or measurement read functions. Calling this func

### Advanced

#### Groups

- Analyze2
- List

#### Group members

| Name | Description |
| --- | --- |
| RFmxNR_AbortMeasurements | Stops acquisition and measurements associated with signal instance that you specify in the Selector String parameter, which were previously initiated by the RFmxNR_Initiate function or measurement read functions. Calling this function is optional, unless you want to stop a measurement before it is complete. This function executes even if there is an incoming error. |
| RFmxNR_ClearAllNamedResults | Clears all results for the signal that you specify in the Selector String parameter. |
| RFmxNR_ClearNamedResult | Clears a result instance specified by the result name in the Selector String parameter. |
| RFmxNR_ClearNoiseCalibrationDatabase | Clears the noise calibration database used for noise compensation. |
| RFmxNR_CloneSignalConfiguration | Creates a new instance of a signal by copying all the attribute values from an existing signal instance. |
| RFmxNR_CreateSignalConfiguration | Creates a new instance of a signal. |
| RFmxNR_DeleteSignalConfiguration | Deletes an instance of a signal that you specify in the Signal Name parameter. |
| RFmxNR_GetAllNamedResultNames | Returns the named result names of the signal that you specify in the Selector String parameter. |

#### Attachments

None

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__advanced_1ga2468519bd3b952f4bf511a488fa5a9c5.html language=enus -->
## TOPIC 00165: RFmxNR_ClearNoiseCalibrationDatabase

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__advanced_1ga2468519bd3b952f4bf511a488fa5a9c5.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__advanced_1ga2468519bd3b952f4bf511a488fa5a9c5.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Clears the noise calibration database used for noise compensation. Syntaxint32 __stdcall RFmxNR_ClearNoiseCalibrationDatabase(niRFmxInstrHandle instrumentHandle, char selectorString[])ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifies the RFmx session

### RFmxNR_ClearNoiseCalibrationDatabase

Clears the noise calibration database used for noise compensation.

#### Syntax

int32 __stdcall RFmxNR_ClearNoiseCalibrationDatabase(niRFmxInstrHandle instrumentHandle, char selectorString[])

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string).Example:"signal::sig1"You can use the RFmxNR_BuildSignalString function to build the selector string. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__advanced_1ga42ad87a820381748ce88b1443ef6d1aa.html language=enus -->
## TOPIC 00166: RFmxNR_ClearNamedResult

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__advanced_1ga42ad87a820381748ce88b1443ef6d1aa.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__advanced_1ga42ad87a820381748ce88b1443ef6d1aa.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Clears a result instance specified by the result name in the Selector String parameter. Syntaxint32 __stdcall RFmxNR_ClearNamedResult(niRFmxInstrHandle instrumentHandle, char selectorString[])ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifies the RFmx

### RFmxNR_ClearNamedResult

Clears a result instance specified by the result name in the **Selector String** parameter.

#### Syntax

int32 __stdcall RFmxNR_ClearNamedResult(niRFmxInstrHandle instrumentHandle, char selectorString[])

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default is "" (empty string).Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxNR_BuildSignalString function to build the selector string. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__advanced_1ga5aeaeb106731e707eb3696a65be19b1e.html language=enus -->
## TOPIC 00167: RFmxNR_GetAllNamedResultNames

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__advanced_1ga5aeaeb106731e707eb3696a65be19b1e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__advanced_1ga5aeaeb106731e707eb3696a65be19b1e.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the named result names of the signal that you specify in the Selector String parameter. Syntaxint32 __stdcall RFmxNR_GetAllNamedResultNames(niRFmxInstrHandle instrumentHandle, char selectorString[], char resultNames[], int32 resultNamesBufferSize, int32 *actualResultNamesSize, int32 *default

### RFmxNR_GetAllNamedResultNames

Returns the named result names of the signal that you specify in the **Selector String** parameter.

#### Syntax

int32 __stdcall RFmxNR_GetAllNamedResultNames(niRFmxInstrHandle instrumentHandle, char selectorString[], char resultNames[], int32 resultNamesBufferSize, int32 *actualResultNamesSize, int32 *defaultResultExists)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string).Example:"signal::sig1"You can use the RFmxNR_BuildSignalString function to build the selector string. |
| resultNames | [out] | char[] | This parameter returns an array of result names. |
| resultNamesBufferSize | [in] | int32 | Specifies the size of the resultNames array. Set the resultNamesBufferSize parameter to 0 to get the size of the resultNames array in the return value. |
| actualResultNamesSize | [out] | int32 * | Returns the actual size of the resultNames array, if you pass NULL to resultNames array parameter and set the resultNamesBufferSize parameter to 0. |
| defaultResultExists | [out] | int32 * | This parameter indicates whether the default result exists. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__advanced_1ga712ee17c73a689276a5877cea6f1e998.html language=enus -->
## TOPIC 00168: RFmxNR_CreateSignalConfiguration

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__advanced_1ga712ee17c73a689276a5877cea6f1e998.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__advanced_1ga712ee17c73a689276a5877cea6f1e998.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a new instance of a signal. Syntaxint32 __stdcall RFmxNR_CreateSignalConfiguration(niRFmxInstrHandle instrumentHandle, char signalName[])ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifies the RFmx session refnum. Instrument Handle In is obtain

### RFmxNR_CreateSignalConfiguration

Creates a new instance of a signal.

#### Syntax

int32 __stdcall RFmxNR_CreateSignalConfiguration(niRFmxInstrHandle instrumentHandle, char signalName[])

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| signalName | [in] | char[] | This parameter specifies the name of the signal. This parameter accepts the signal name with or without the "signal::" prefix.Example:"signal::sig1""sig1" |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__advanced_1ga7f8fab3ce1d341ae244e090598a12b2b.html language=enus -->
## TOPIC 00169: RFmxNR_DeleteSignalConfiguration

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__advanced_1ga7f8fab3ce1d341ae244e090598a12b2b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__advanced_1ga7f8fab3ce1d341ae244e090598a12b2b.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Deletes an instance of a signal that you specify in the Signal Name parameter. Syntaxint32 __stdcall RFmxNR_DeleteSignalConfiguration(niRFmxInstrHandle instrumentHandle, char signalName[])ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifies the RFmx ses

### RFmxNR_DeleteSignalConfiguration

Deletes an instance of a signal that you specify in the **Signal Name** parameter.

#### Syntax

int32 __stdcall RFmxNR_DeleteSignalConfiguration(niRFmxInstrHandle instrumentHandle, char signalName[])

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| signalName | [in] | char[] | This parameter specifies the name of the signal. This parameter accepts the signal name with or without the "signal::" prefix.Example:"signal::sig1""sig1" |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__advanced_1gac448a8e544c0dd91587cd6b185e83ed0.html language=enus -->
## TOPIC 00170: RFmxNR_CloneSignalConfiguration

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__advanced_1gac448a8e544c0dd91587cd6b185e83ed0.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__advanced_1gac448a8e544c0dd91587cd6b185e83ed0.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a new instance of a signal by copying all the attribute values from an existing signal instance. Syntaxint32 __stdcall RFmxNR_CloneSignalConfiguration(niRFmxInstrHandle instrumentHandle, char oldSignalName[], char newSignalName[])ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRF

### RFmxNR_CloneSignalConfiguration

Creates a new instance of a signal by copying all the attribute values from an existing signal instance.

#### Syntax

int32 __stdcall RFmxNR_CloneSignalConfiguration(niRFmxInstrHandle instrumentHandle, char oldSignalName[], char newSignalName[])

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| oldSignalName | [in] | char[] | This parameter specifies the name of the existing signal. This parameter accepts the signal name with or without the "signal::" prefix.Example:"signal::OldSigName""OldSigName" |
| newSignalName | [in] | char[] | This parameter specifies the name of the new signal. This parameter accepts the signal name with or without the "signal::" prefix.Example:"signal::NewSigName""NewSigName" |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__advanced_1gad2c7ae74096171d55c98c337f9819079.html language=enus -->
## TOPIC 00171: RFmxNR_AbortMeasurements

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__advanced_1gad2c7ae74096171d55c98c337f9819079.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__advanced_1gad2c7ae74096171d55c98c337f9819079.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Stops acquisition and measurements associated with signal instance that you specify in the Selector String parameter, which were previously initiated by the RFmxNR_Initiate function or measurement read functions. Calling this function is optional, unless you want to stop a measurement before it is c

### RFmxNR_AbortMeasurements

Stops acquisition and measurements associated with signal instance that you specify in the **Selector String** parameter, which were previously initiated by the [RFmxNR_Initiate](group____root__ni_r_fmx_n_r__functions_1ga1feff952d2974304538c63402d9188e6.html) function or measurement read functions. Calling this function is optional, unless you want to stop a measurement before it is complete. This function executes even if there is an incoming error.

#### Syntax

int32 __stdcall RFmxNR_AbortMeasurements(niRFmxInstrHandle instrumentHandle, char selectorString[])

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string).Example:"signal::sig1"You can use the RFmxNR_BuildSignalString function to build the selector string. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__advanced_1gaeb949b5a8be0b4be02ffdc94a0448634.html language=enus -->
## TOPIC 00172: RFmxNR_ClearAllNamedResults

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__advanced_1gaeb949b5a8be0b4be02ffdc94a0448634.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__advanced_1gaeb949b5a8be0b4be02ffdc94a0448634.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Clears all results for the signal that you specify in the Selector String parameter. Syntaxint32 __stdcall RFmxNR_ClearAllNamedResults(niRFmxInstrHandle instrumentHandle, char selectorString[])ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifies the RFm

### RFmxNR_ClearAllNamedResults

Clears all results for the signal that you specify in the **Selector String** parameter.

#### Syntax

int32 __stdcall RFmxNR_ClearAllNamedResults(niRFmxInstrHandle instrumentHandle, char selectorString[])

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string).Example:"signal::sig1"You can use the RFmxNR_BuildSignalString function to build the selector string. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__advanced__analyze2.html language=enus -->
## TOPIC 00173: Analyze2

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__advanced__analyze2.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__advanced__analyze2.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxNR_AnalyzeIQ1WaveformPerforms the enabled measurements on the I/Q complex waveform that you specify in IQ parameter. Call this function after you configure the signal and measurement attributes. You can fetch measurement results using the Fetch functions or

### Analyze2

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxNR_AnalyzeIQ1Waveform | Performs the enabled measurements on the I/Q complex waveform that you specify in IQ parameter. Call this function after you configure the signal and measurement attributes. You can fetch measurement results using the Fetch functions or result attributes in the attribute node. Use this function only if the RFMXINSTR_ATTR_RECOMMENDED_ACQUISITION_TYPE attribute value is either IQ or IQ or Spectral. |
| RFmxNR_AnalyzeIQ1WaveformSplit | Performs the enabled measurements on the I/Q complex waveform that you specify in IQ parameter. Call this function after you configure the signal and measurement attributes. You can fetch measurement results using the Fetch functions or result attributes in the attribute node. Use this function only if the RFMXINSTR_ATTR_RECOMMENDED_ACQUISITION_TYPE attribute value is either IQ or IQ or Spectral. |
| RFmxNR_AnalyzeNWaveformsIQ | Performs the enabled measurements on the I/Q complex waveform(s) that you specify in IQ parameter. Call this function after you configure the signal and measurement attributes. You can fetch measurement results using the Fetch functions or result attributes in the attribute node. Use this function only if the RFMXINSTR_ATTR_RECOMMENDED_ACQUISITION_TYPE attribute value is either IQ or IQ or Spectral. |
| RFmxNR_AnalyzeNWaveformsIQSplit | Performs the enabled measurements on the I/Q complex waveform(s) that you specify in IQ parameter. Call this function after you configure the signal and measurement attributes. You can fetch measurement results using the Fetch functions or result attributes in the attribute node. Use this function only if the RFMXINSTR_ATTR_RECOMMENDED_ACQUISITION_TYPE attribute value is either IQ or IQ or Spectral. |
| RFmxNR_AnalyzeNWaveformsSpectrum | Performs the enabled measurements on the spectrum(s) that you specify in the Spectrum parameter. Call this function after you configure the signal and measurement attributes. You can fetch measurement results using the Fetch functions or result attributes in the attribute node. Use this function only if the RFMXINSTR_ATTR_RECOMMENDED_ACQUISITION_TYPE attribute value is either Spectral or IQ or Spectral. |
| RFmxNR_AnalyzeSpectrum1Waveform | Performs the enabled measurements on the spectrum that you specify in the Spectrum parameter. Call this function after you configure the signal and measurement attributes. You can fetch measurement results using the Fetch functions or result attributes in the attribute node. Use this function only if the RFMXINSTR_ATTR_RECOMMENDED_ACQUISITION_TYPE attribute value is either Spectral or IQ or Spectral. |

#### Attachments

None

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__advanced__analyze2_1ga35a3b150af802cb3ed70238166f73db6.html language=enus -->
## TOPIC 00174: RFmxNR_AnalyzeNWaveformsIQSplit

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__advanced__analyze2_1ga35a3b150af802cb3ed70238166f73db6.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__advanced__analyze2_1ga35a3b150af802cb3ed70238166f73db6.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs the enabled measurements on the I/Q complex waveform(s) that you specify in IQ parameter. Call this function after you configure the signal and measurement attributes. You can fetch measurement results using the Fetch functions or result attributes in the attribute node. Use this function o

### RFmxNR_AnalyzeNWaveformsIQSplit

Performs the enabled measurements on the I/Q complex waveform(s) that you specify in **IQ** parameter. Call this function after you configure the signal and measurement attributes. You can fetch measurement results using the Fetch functions or result attributes in the attribute node. Use this function only if the [RFMXINSTR_ATTR_RECOMMENDED_ACQUISITION_TYPE](/csh?context=rfmxinstr_rfmxinstrcref_attribute_recommended_acquisition_type) attribute value is either **IQ** or **IQ or Spectral**.

#### Syntax

int32 __stdcall RFmxNR_AnalyzeNWaveformsIQSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], char resultName[], float64 x0[], float64 dx[], float32 iqI[], float32 iqQ[], int32 iqSize[], int32 arraySize, int32 reset)

#### Remarks

When using the Analysis-Only mode in RFmxNR, the RFmx driver ignores the RFmx hardware settings such as reference level and attenuation. The only RF hardware settings that are not ignored are the center frequency and trigger type, since it is needed for spectral measurement traces as well as some measurements such as ModAcc, ACP, and SEM.

Note

Query the Recommended Acquisition Type attribute from the RFmxInstr Attribute after calling the [RFmxNR_Commit](group____root__ni_r_fmx_n_r__functions__utility_1ga1c37b93c6e45121252305b57e7bf81d8.html) function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function or the RFmxInstr_InitializeFromNIRFSASessionArray function. |
| selectorString | [in] | char[] | This parameter specifies the signal name and result name. The result name can either be specified through this input or the Result Name parameter. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name in this parameter, either the result name specified by the Result Name parameter or the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxNR_BuildSignalString function to build the Selector String. |
| resultName | [in] | char[] | This parameter specifies the name to be associated with measurement results. Provide a unique name, such as "r1" to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. The default value is "" (empty string) which refers to default result instance.Example:"result::r1""r1" |
| x0 | [in] | float64[] | This parameter specifies the start time of the input y array. This value is expressed in seconds. |
| dx | [in] | float64[] | This parameter specifies the time interval between the samples in the input y array. This value is expressed in seconds. The reciprocal of dx indicates the I/Q rate of the input signal. |
| iqI | [in] | float32[] | This parameter specifies an array of complex-valued time domain data. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively. |
| iqQ | [in] | float32[] | This parameter specifies an array of complex-valued time domain data. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively. |
| iqSize | [in] | int32[] | Specifies the size of n waveforms |
| arraySize | [in] | int32 | Specifies the size of the array. |
| reset | [in] | int32 | This parameter resets measurement averaging. If you enable averaging, set this parameter to TRUE for first record and FALSE for subsequent records. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Analyze2

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__advanced__analyze2_1ga3cd83ea509647ee0c377d1e8e58078a3.html language=enus -->
## TOPIC 00175: RFmxNR_AnalyzeNWaveformsIQ

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__advanced__analyze2_1ga3cd83ea509647ee0c377d1e8e58078a3.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__advanced__analyze2_1ga3cd83ea509647ee0c377d1e8e58078a3.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs the enabled measurements on the I/Q complex waveform(s) that you specify in IQ parameter. Call this function after you configure the signal and measurement attributes. You can fetch measurement results using the Fetch functions or result attributes in the attribute node. Use this function o

### RFmxNR_AnalyzeNWaveformsIQ

Performs the enabled measurements on the I/Q complex waveform(s) that you specify in **IQ** parameter. Call this function after you configure the signal and measurement attributes. You can fetch measurement results using the Fetch functions or result attributes in the attribute node. Use this function only if the [RFMXINSTR_ATTR_RECOMMENDED_ACQUISITION_TYPE](/csh?context=rfmxinstr_rfmxinstrcref_attribute_recommended_acquisition_type) attribute value is either **IQ** or **IQ or Spectral**.

#### Syntax

int32 __stdcall RFmxNR_AnalyzeNWaveformsIQ(niRFmxInstrHandle instrumentHandle, char selectorString[], char resultName[], float64 x0[], float64 dx[], NIComplexSingle iq[], int32 iqSize[], int32 arraySize, int32 reset)

#### Remarks

When using the Analysis-Only mode in RFmxNR, the RFmx driver ignores the RFmx hardware settings such as reference level and attenuation. The only RF hardware settings that are not ignored are the center frequency and trigger type, since it is needed for spectral measurement traces as well as some measurements such as ModAcc, ACP, and SEM.

Note

Query the Recommended Acquisition Type attribute from the RFmxInstr Attribute after calling the [RFmxNR_Commit](group____root__ni_r_fmx_n_r__functions__utility_1ga1c37b93c6e45121252305b57e7bf81d8.html) function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function or the RFmxInstr_InitializeFromNIRFSASessionArray function. |
| selectorString | [in] | char[] | This parameter specifies the signal name and result name. The result name can either be specified through this input or the Result Name parameter. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name in this parameter, either the result name specified by the Result Name parameter or the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxNR_BuildSignalString function to build the Selector String. |
| resultName | [in] | char[] | This parameter specifies the name to be associated with measurement results. Provide a unique name, such as "r1" to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. The default value is "" (empty string) which refers to default result instance.Example:"result::r1""r1" |
| x0 | [in] | float64[] | This parameter specifies the start time of the input y array. This value is expressed in seconds. |
| dx | [in] | float64[] | This parameter specifies the time interval between the samples in the input y array. This value is expressed in seconds. The reciprocal of dx indicates the I/Q rate of the input signal. |
| iq | [in] | NIComplexSingle[] | This parameter specifies an array of complex-valued time domain data. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively. |
| iqSize | [in] | int32[] | Specifies the size of n waveforms |
| arraySize | [in] | int32 | Specifies the size of the array. |
| reset | [in] | int32 | This parameter resets measurement averaging. If you enable averaging, set this parameter to TRUE for first record and FALSE for subsequent records. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Analyze2

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__advanced__analyze2_1ga4bd2fb39dfd6a1ab7d53814350c717fa.html language=enus -->
## TOPIC 00176: RFmxNR_AnalyzeSpectrum1Waveform

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__advanced__analyze2_1ga4bd2fb39dfd6a1ab7d53814350c717fa.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__advanced__analyze2_1ga4bd2fb39dfd6a1ab7d53814350c717fa.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs the enabled measurements on the spectrum that you specify in the Spectrum parameter. Call this function after you configure the signal and measurement attributes. You can fetch measurement results using the Fetch functions or result attributes in the attribute node. Use this function only i

### RFmxNR_AnalyzeSpectrum1Waveform

Performs the enabled measurements on the spectrum that you specify in the **Spectrum** parameter. Call this function after you configure the signal and measurement attributes. You can fetch measurement results using the Fetch functions or result attributes in the attribute node. Use this function only if the [RFMXINSTR_ATTR_RECOMMENDED_ACQUISITION_TYPE](/csh?context=rfmxinstr_rfmxinstrcref_attribute_recommended_acquisition_type) attribute value is either **Spectral** or **IQ or Spectral**.

#### Syntax

int32 __stdcall RFmxNR_AnalyzeSpectrum1Waveform(niRFmxInstrHandle instrumentHandle, char selectorString[], char resultName[], float64 x0, float64 dx, float32 spectrum[], int32 arraySize, int32 reset, int64 reserved)

#### Remarks

When using the Analysis-Only mode in RFmxNR, the RFmx driver ignores the RFmx hardware settings such as reference level and attenuation. The only RF hardware settings that are not ignored are the center frequency and trigger type, since it is needed for spectral measurement traces as well as some measurements such as ModAcc, ACP, and SEM.

Note

Query the Recommended Acquisition Type attribute from the RFmxInstr Attribute after calling the [RFmxNR_Commit](group____root__ni_r_fmx_n_r__functions__utility_1ga1c37b93c6e45121252305b57e7bf81d8.html) function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies the signal name and result name. The result name can either be specified through this input or the Result Name parameter. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name in this parameter, either the result name specified by the Result Name parameter or the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxNR_BuildSignalString function to build the Selector String. |
| resultName | [in] | char[] | This parameter specifies the name to be associated with measurement results. Provide a unique name, such as "r1" to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. The default value is "" (empty string) which refers to default result instance.Example:"result::r1""r1" |
| x0 | [in] | float64 | This parameter specifies the start frequency of the spectrum. This value is expressed in Hz. |
| dx | [in] | float64 | This parameter specifies the frequency interval between data points in the spectrum. |
| spectrum | [in] | float32[] | This parameter contains the real-value power spectrum. |
| arraySize | [in] | int32 | Specifies the size of the array. |
| reset | [in] | int32 | This parameter resets measurement averaging. If you enable averaging, set this parameter to TRUE for first record and FALSE for subsequent records. |
| reserved | [in] | int64 | Reserved for future use. Any value passed to this parameter will be ignored. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Analyze2

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__advanced__analyze2_1ga83d5bab197fdaa72584389242a936aab.html language=enus -->
## TOPIC 00177: RFmxNR_AnalyzeNWaveformsSpectrum

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__advanced__analyze2_1ga83d5bab197fdaa72584389242a936aab.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__advanced__analyze2_1ga83d5bab197fdaa72584389242a936aab.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs the enabled measurements on the spectrum(s) that you specify in the Spectrum parameter. Call this function after you configure the signal and measurement attributes. You can fetch measurement results using the Fetch functions or result attributes in the attribute node. Use this function onl

### RFmxNR_AnalyzeNWaveformsSpectrum

Performs the enabled measurements on the spectrum(s) that you specify in the **Spectrum** parameter. Call this function after you configure the signal and measurement attributes. You can fetch measurement results using the Fetch functions or result attributes in the attribute node. Use this function only if the [RFMXINSTR_ATTR_RECOMMENDED_ACQUISITION_TYPE](/csh?context=rfmxinstr_rfmxinstrcref_attribute_recommended_acquisition_type) attribute value is either **Spectral** or **IQ or Spectral**.

#### Syntax

int32 __stdcall RFmxNR_AnalyzeNWaveformsSpectrum(niRFmxInstrHandle instrumentHandle, char selectorString[], char resultName[], float64 x0[], float64 dx[], float32 spectrum[], int32 spectrumSize[], int32 arraySize, int32 reset)

#### Remarks

Note

Query the Recommended Acquisition Type attribute from the RFmxInstr Attribute after calling the [RFmxNR_Commit](group____root__ni_r_fmx_n_r__functions__utility_1ga1c37b93c6e45121252305b57e7bf81d8.html) function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function or the RFmxInstr_InitializeFromNIRFSASessionArray function. |
| selectorString | [in] | char[] | This parameter specifies the signal name and result name. The result name can either be specified through this input or the Result Name parameter. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name in this parameter, either the result name specified by the Result Name parameter or the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxNR_BuildSignalString function to build the Selector String. |
| resultName | [in] | char[] | This parameter specifies the name to be associated with measurement results. Provide a unique name, such as "r1" to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. The default value is "" (empty string) which refers to default result instance.Example:"result::r1""r1" |
| x0 | [in] | float64[] | This parameter specifies the start frequency of the spectrum. This value is expressed in Hz. |
| dx | [in] | float64[] | This parameter specifies the frequency interval between data points in the spectrum. |
| spectrum | [in] | float32[] | This parameter specifies the array of real-value power spectrum. |
| spectrumSize | [in] | int32[] | Specifies the size of n waveforms. |
| arraySize | [in] | int32 | Specifies the size of the array. |
| reset | [in] | int32 | This parameter resets measurement averaging. If you enable averaging, set this parameter to TRUE for first record and FALSE for subsequent records. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Analyze2

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__advanced__analyze2_1gaace3a3941b21411b756d5fa9ece58cb6.html language=enus -->
## TOPIC 00178: RFmxNR_AnalyzeIQ1Waveform

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__advanced__analyze2_1gaace3a3941b21411b756d5fa9ece58cb6.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__advanced__analyze2_1gaace3a3941b21411b756d5fa9ece58cb6.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs the enabled measurements on the I/Q complex waveform that you specify in IQ parameter. Call this function after you configure the signal and measurement attributes. You can fetch measurement results using the Fetch functions or result attributes in the attribute node. Use this function only

### RFmxNR_AnalyzeIQ1Waveform

Performs the enabled measurements on the I/Q complex waveform that you specify in **IQ** parameter. Call this function after you configure the signal and measurement attributes. You can fetch measurement results using the Fetch functions or result attributes in the attribute node. Use this function only if the [RFMXINSTR_ATTR_RECOMMENDED_ACQUISITION_TYPE](/csh?context=rfmxinstr_rfmxinstrcref_attribute_recommended_acquisition_type) attribute value is either **IQ** or **IQ or Spectral**.

#### Syntax

int32 __stdcall RFmxNR_AnalyzeIQ1Waveform(niRFmxInstrHandle instrumentHandle, char selectorString[], char resultName[], float64 x0, float64 dx, NIComplexSingle iq[], int32 arraySize, int32 reset, int64 reserved)

#### Remarks

When using the Analysis-Only mode in RFmxNR, the RFmx driver ignores the RFmx hardware settings such as reference level and attenuation. The only RF hardware settings that are not ignored are the center frequency and trigger type, since it is needed for spectral measurement traces as well as some measurements such as ModAcc, ACP, and SEM.

Note

Query the Recommended Acquisition Type attribute from the RFmxInstr Attribute after calling the [RFmxNR_Commit](group____root__ni_r_fmx_n_r__functions__utility_1ga1c37b93c6e45121252305b57e7bf81d8.html) function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies the signal name and result name. The result name can either be specified through this input or the Result Name parameter. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name in this parameter, either the result name specified by the Result Name parameter or the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxNR_BuildSignalString function to build the Selector String. |
| resultName | [in] | char[] | This parameter specifies the name to be associated with measurement results. Provide a unique name, such as "r1" to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. The default value is "" (empty string) which refers to default result instance.Example:"result::r1""r1" |
| x0 | [in] | float64 | This parameter specifies the start time of the input y array. This value is expressed in seconds. |
| dx | [in] | float64 | This parameter specifies the time interval between the samples in the input y array. This value is expressed in seconds. The reciprocal of dx indicates the I/Q rate of the input signal. |
| iq | [in] | NIComplexSingle[] | This parameter specifies an array of complex-valued time domain data. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively. |
| arraySize | [in] | int32 | Specifies the size of the array. |
| reset | [in] | int32 | This parameter resets measurement averaging. If you enable averaging, set this parameter to TRUE for first record and FALSE for subsequent records. |
| reserved | [in] | int64 | Reserved for future use. Any value passed to this parameter will be ignored. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Analyze2

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__advanced__list.html language=enus -->
## TOPIC 00179: List

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__advanced__list.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__advanced__list.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxNR_BuildListStepStringCreates the list step string. RFmxNR_BuildListStringCreates the list string. RFmxNR_CreateListCreates a new list instance. Call the RFmxNR_CreateListStep function to add steps to the list. Alternatively, you can also specify the number

### List

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxNR_BuildListStepString | Creates the list step string. |
| RFmxNR_BuildListString | Creates the list string. |
| RFmxNR_CreateList | Creates a new list instance. Call the RFmxNR_CreateListStep function to add steps to the list. Alternatively, you can also specify the number of list steps using the RFMXNR_ATTR_NUMBER_OF_STEPS attribute. |
| RFmxNR_CreateListStep | Creates a new list step instance in a list. |
| RFmxNR_DeleteList | Deletes the list instance and all the list steps that you specify in the List Name parameter. When a list step is deleted, all the instances of attributes associated with the list step are also removed. |

#### Attachments

None

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__advanced__list_1ga072318dbe747c52862d490dd4be5bb73.html language=enus -->
## TOPIC 00180: RFmxNR_BuildListString

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__advanced__list_1ga072318dbe747c52862d490dd4be5bb73.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__advanced__list_1ga072318dbe747c52862d490dd4be5bb73.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates the list string. Syntaxint32 __stdcall RFmxNR_BuildListString(char listName[], char resultName[], int32 selectorStringOutLength, char selectorStringOut[])ParametersNameDirectionTypeDescriptionlistName[in]char[]This parameter specifies the name of the list. This parameter accepts the list nam

### RFmxNR_BuildListString

Creates the list string.

#### Syntax

int32 __stdcall RFmxNR_BuildListString(char listName[], char resultName[], int32 selectorStringOutLength, char selectorStringOut[])

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| listName | [in] | char[] | This parameter specifies the name of the list. This parameter accepts the list name with or without the "list::" prefix. The default value is "" (empty string).Example:"list::samplelist1""samplelist1" |
| resultName | [in] | char[] | This parameter specifies the name to be associated with measurement results. Provide a unique name, such as "r1" to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. The default value is "" (empty string) for the default result instance.Example:"result::r1""r1" |
| selectorStringOutLength | [out] | int32 | Specifies the length of the string that is returned by the selectorStringOut parameter. To get the minimum buffer size required to build the selector string, set the selectorStringOutLength parameter to 0. |
| selectorStringOut | [out] | char[] | This parameter returns the selector string created by this function. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

List

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__advanced__list_1ga4ed499a2c5101479b5f85622776efff6.html language=enus -->
## TOPIC 00181: RFmxNR_CreateListStep

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__advanced__list_1ga4ed499a2c5101479b5f85622776efff6.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__advanced__list_1ga4ed499a2c5101479b5f85622776efff6.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a new list step instance in a list. Syntaxint32 __stdcall RFmxNR_CreateListStep(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 *createdStepIndex)RemarksSupported devices:PXIe-5840/5841/5842/5860ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis

### RFmxNR_CreateListStep

Creates a new list step instance in a list.

#### Syntax

int32 __stdcall RFmxNR_CreateListStep(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 *createdStepIndex)

#### Remarks

**Supported devices:**PXIe-5840/5841/5842/5860

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies the name of the list. This parameter accepts the list name with or without the "list::" prefix.Example:"list::samplelist1""samplelist1"You can use the RFmxNR_BuildListString function to build the selector string or use the Selector String Out parameter from the RFmxNR_CreateList function. |
| createdStepIndex | [out] | int32 * | Returns the created list step index. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

List

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__advanced__list_1ga5e7ee686de8f99249a3710b03601d643.html language=enus -->
## TOPIC 00182: RFmxNR_CreateList

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__advanced__list_1ga5e7ee686de8f99249a3710b03601d643.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__advanced__list_1ga5e7ee686de8f99249a3710b03601d643.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a new list instance. Call the RFmxNR_CreateListStep function to add steps to the list. Alternatively, you can also specify the number of list steps using the RFMXNR_ATTR_NUMBER_OF_STEPS attribute. Syntaxint32 __stdcall RFmxNR_CreateList(niRFmxInstrHandle instrumentHandle, char listName[])Rem

### RFmxNR_CreateList

Creates a new list instance. Call the [RFmxNR_CreateListStep](group____root__ni_r_fmx_n_r__functions__advanced__list_1ga4ed499a2c5101479b5f85622776efff6.html) function to add steps to the list. Alternatively, you can also specify the number of list steps using the [RFMXNR_ATTR_NUMBER_OF_STEPS](group____root__ni_r_fmx_n_r__attributes__list_1gaf5b94026c7b223102557ade33e0f604d.html) attribute.

#### Syntax

int32 __stdcall RFmxNR_CreateList(niRFmxInstrHandle instrumentHandle, char listName[])

#### Remarks

**Supported devices:**PXIe-5840/5841/5842/5860

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| listName | [in] | char[] | This parameter specifies the name of the list. This parameter accepts the list name with or without the "list::" prefix.Example:"list::samplelist1""samplelist1"You can use the RFmxNR_BuildListString function to build the list name. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

List

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__advanced__list_1gabe9fc3a020ca8bcf7a726cdd508c9ea1.html language=enus -->
## TOPIC 00183: RFmxNR_DeleteList

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__advanced__list_1gabe9fc3a020ca8bcf7a726cdd508c9ea1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__advanced__list_1gabe9fc3a020ca8bcf7a726cdd508c9ea1.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Deletes the list instance and all the list steps that you specify in the List Name parameter. When a list step is deleted, all the instances of attributes associated with the list step are also removed. Syntaxint32 __stdcall RFmxNR_DeleteList(niRFmxInstrHandle instrumentHandle, char listName[])Remar

### RFmxNR_DeleteList

Deletes the list instance and all the list steps that you specify in the **List Name** parameter. When a list step is deleted, all the instances of attributes associated with the list step are also removed.

#### Syntax

int32 __stdcall RFmxNR_DeleteList(niRFmxInstrHandle instrumentHandle, char listName[])

#### Remarks

**Supported devices:**PXIe-5840/5841/5860

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| listName | [in] | char[] | This parameter specifies the name of the list. This parameter accepts the list name with or without the "list::" prefix.Example:"list::samplelist1""samplelist1"You can use the RFmxNR_BuildListString function to build the list name. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

List

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__advanced__list_1gaef653ef101748bde6b90f479eee9e614.html language=enus -->
## TOPIC 00184: RFmxNR_BuildListStepString

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__advanced__list_1gaef653ef101748bde6b90f479eee9e614.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__advanced__list_1gaef653ef101748bde6b90f479eee9e614.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates the list step string. Syntaxint32 __stdcall RFmxNR_BuildListStepString(char listName[], char resultName[], int32 stepNumber, int32 selectorStringOutLength, char selectorStringOut[])ParametersNameDirectionTypeDescriptionlistName[in]char[]This parameter specifies the list name. This input acce

### RFmxNR_BuildListStepString

Creates the list step string.

#### Syntax

int32 __stdcall RFmxNR_BuildListStepString(char listName[], char resultName[], int32 stepNumber, int32 selectorStringOutLength, char selectorStringOut[])

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| listName | [in] | char[] | This parameter specifies the list name. This input accepts the list name with or without the "list::" prefix. The default value is "" (empty string).Example:"list::samplelist1""samplelist1" |
| resultName | [in] | char[] | This parameter specifies the name to be associated with measurement results. Provide a unique name, such as "r1" to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. The default value is "" (empty string) for the default result instance.Example:"result::r1""r1" |
| stepNumber | [in] | int32 | This parameter specifies the step number for building the selector string. The default value is 0, which corresponds to the first step. When you use -1 as the step number, all steps are considered. |
| selectorStringOutLength | [out] | int32 | Specifies the length of the string that is returned by the selectorStringOut parameter. To get the minimum buffer size required to build the selector string, set the selectorStringOutLength parameter to 0. |
| selectorStringOut | [out] | char[] | This parameter returns the selector string created by this function. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

List

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__build__string.html language=enus -->
## TOPIC 00185: Build String

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__build__string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__build__string.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxNR_BuildBandwidthPartStringCreates the bandwidth part string. RFmxNR_BuildCORESETClusterStringCreates the coreset cluster string. RFmxNR_BuildCORESETStringCreates the coreset string. RFmxNR_BuildCarrierStringCreates the carrier string. RFmxNR_BuildChainStrin

### Build String

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxNR_BuildBandwidthPartString | Creates the bandwidth part string. |
| RFmxNR_BuildCORESETClusterString | Creates the coreset cluster string. |
| RFmxNR_BuildCORESETString | Creates the coreset string. |
| RFmxNR_BuildCarrierString | Creates the carrier string. |
| RFmxNR_BuildChainString | Creates a chain string. |
| RFmxNR_BuildLayerString | Creates a layer string. |
| RFmxNR_BuildOffsetString | Creates the offset string. |
| RFmxNR_BuildPDCCHString | Creates the PDCCH string. |
| RFmxNR_BuildPDSCHClusterString | Creates a PDSCH Cluster string. |
| RFmxNR_BuildPDSCHString | Creates the PDSCH string. |
| RFmxNR_BuildPUSCHClusterString | Creates a PUSCH Cluster string. |
| RFmxNR_BuildPUSCHString | Creates the PUSCH string. |
| RFmxNR_BuildSignalString | Creates selector string. |
| RFmxNR_BuildSubblockString | Creates the subblock string. |
| RFmxNR_BuildUserString | Creates the user number string. |

#### Attachments

None

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__build__string_1ga04c3180ada4c117fd89beac8c0b4f25b.html language=enus -->
## TOPIC 00186: RFmxNR_BuildPUSCHClusterString

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__build__string_1ga04c3180ada4c117fd89beac8c0b4f25b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__build__string_1ga04c3180ada4c117fd89beac8c0b4f25b.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a PUSCH Cluster string. Syntaxint32 __stdcall RFmxNR_BuildPUSCHClusterString(char selectorString[], int32 selectorStringOutLength, char selectorStringOut[], int32 puschClusterNumber)ParametersNameDirectionTypeDescriptionselectorString[in]char[]This parameter specifies a Selector String compr

### RFmxNR_BuildPUSCHClusterString

Creates a PUSCH Cluster string.

#### Syntax

int32 __stdcall RFmxNR_BuildPUSCHClusterString(char selectorString[], int32 selectorStringOutLength, char selectorStringOut[], int32 puschClusterNumber)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, subblock number, bandwidth part number, user number, and pusch number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"subblock0/carrier0/bwp0/user0/pusch0""signal::sig1/subblock0/carrier0/bwp0/user0/pusch0""signal::sig1/result::r1/subblock0/carrier0/bwp/user0/pusch0""result::r1/subblock0/carrier0/bwp0/user0/pusch0"You can use the RFmxNR_BuildPUSCHString function to build the selector string. |
| selectorStringOutLength | [out] | int32 | Specifies the length of the string that is returned by the selectorStringOut parameter. To get the minimum buffer size required to build the selector string, set the selectorStringOutLength parameter to 0. |
| selectorStringOut | [out] | char[] | This parameter returns the selector string created by this function. |
| puschClusterNumber | [in] | int32 | This parameter specifies the PUSCH cluster number for building the selector string. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Build String

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__build__string_1ga0bec6d8c27ca57127311bc1dd425ae15.html language=enus -->
## TOPIC 00187: RFmxNR_BuildLayerString

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__build__string_1ga0bec6d8c27ca57127311bc1dd425ae15.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__build__string_1ga0bec6d8c27ca57127311bc1dd425ae15.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a layer string. Syntaxint32 __stdcall RFmxNR_BuildLayerString(char selectorString[], int32 layerNumber, int32 selectorStringOutLength, char selectorStringOut[])ParametersNameDirectionTypeDescriptionselectorString[in]char[]This parameter specifies a Selector String comprising of the signal na

### RFmxNR_BuildLayerString

Creates a layer string.

#### Syntax

int32 __stdcall RFmxNR_BuildLayerString(char selectorString[], int32 layerNumber, int32 selectorStringOutLength, char selectorStringOut[])

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, subblock number, carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0".Example:"subblock0/carrier0""signal::sig1/subblock0/carrier0""signal::sig1/result::r1/subblock0/carrier0""result::r1/subblock0/carrier0"You can use the RFmxNR_BuildSubblockString function to build the selector string. |
| layerNumber | [in] | int32 | This parameter specifies the layer number for building the selector string. |
| selectorStringOutLength | [out] | int32 | Specifies the length of the string that is returned by the selectorStringOut parameter. To get the minimum buffer size required to build the selector string, set the selectorStringOutLength parameter to 0. |
| selectorStringOut | [out] | char[] | This parameter returns the selector string created by this function. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Build String

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__build__string_1ga12b9e1a4e7788c74c714343dbfeb7ac7.html language=enus -->
## TOPIC 00188: RFmxNR_BuildBandwidthPartString

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__build__string_1ga12b9e1a4e7788c74c714343dbfeb7ac7.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__build__string_1ga12b9e1a4e7788c74c714343dbfeb7ac7.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates the bandwidth part string. Syntaxint32 __stdcall RFmxNR_BuildBandwidthPartString(char selectorString[], int32 selectorStringOutLength, char selectorStringOut[], int32 bandwidthPartNumber)ParametersNameDirectionTypeDescriptionselectorString[in]char[]This parameter specifies a Selector String

### RFmxNR_BuildBandwidthPartString

Creates the bandwidth part string.

#### Syntax

int32 __stdcall RFmxNR_BuildBandwidthPartString(char selectorString[], int32 selectorStringOutLength, char selectorStringOut[], int32 bandwidthPartNumber)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0".Example:"subblock0/carrier0""signal::sig1/subblock0/carrier0""result::r1/subblock0/carrier0""signal::sig1/result::r1/subblock0/carrier0"You can use the RFmxNR_BuildCarrierString function to build the selector string. |
| selectorStringOutLength | [out] | int32 | Specifies the length of the string that is returned by the selectorStringOut parameter. To get the minimum buffer size required to build the selector string, set the selectorStringOutLength parameter to 0. |
| selectorStringOut | [out] | char[] | This parameter returns the selector string created by this function. |
| bandwidthPartNumber | [in] | int32 | This parameter specifies the bandwidth part number for building the selector string. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Build String

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__build__string_1ga1346c3b1daecaa20e14d57e578da2041.html language=enus -->
## TOPIC 00189: RFmxNR_BuildPDCCHString

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__build__string_1ga1346c3b1daecaa20e14d57e578da2041.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__build__string_1ga1346c3b1daecaa20e14d57e578da2041.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates the PDCCH string. Syntaxint32 __stdcall RFmxNR_BuildPDCCHString(char selectorString[], int32 pdcchNumber, int32 selectorStringOutLength, char selectorStringOut[])ParametersNameDirectionTypeDescriptionselectorString[in]char[]This parameter specifies a Selector String comprising of the signal

### RFmxNR_BuildPDCCHString

Creates the PDCCH string.

#### Syntax

int32 __stdcall RFmxNR_BuildPDCCHString(char selectorString[], int32 pdcchNumber, int32 selectorStringOutLength, char selectorStringOut[])

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, subblock number, carrier number, bandwidth part number, and coreset number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"subblock0/carrier0/bwp0/coreset0""signal::sig1/subblock0/carrier0/bwp0/coreset0""result::r1/subblock0/carrier0/bwp0/coreset0""signal::sig1/result::r1/subblock0/carrier0/bwp0/coreset0"You can use the RFmxNR_BuildCORESETString function to build the selector string. |
| pdcchNumber | [in] | int32 | This parameter specifies the PDCCH number for building the selector string. |
| selectorStringOutLength | [out] | int32 | Specifies the length of the string that is returned by the selectorStringOut parameter. To get the minimum buffer size required to build the selector string, set the selectorStringOutLength parameter to 0. |
| selectorStringOut | [out] | char[] | This parameter returns the selector string created by this function. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Build String

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__build__string_1ga134da1029633969651925756c24e6ef5.html language=enus -->
## TOPIC 00190: RFmxNR_BuildSignalString

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__build__string_1ga134da1029633969651925756c24e6ef5.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__build__string_1ga134da1029633969651925756c24e6ef5.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates selector string. Syntaxint32 __stdcall RFmxNR_BuildSignalString(char signalName[], char resultName[], int32 selectorStringLength, char selectorString[])ParametersNameDirectionTypeDescriptionsignalName[in]char[]This parameter specifies the signal name for building the selector string. This in

### RFmxNR_BuildSignalString

Creates selector string.

#### Syntax

int32 __stdcall RFmxNR_BuildSignalString(char signalName[], char resultName[], int32 selectorStringLength, char selectorString[])

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| signalName | [in] | char[] | This parameter specifies the signal name for building the selector string. This input accepts the signal name with or without the "signal::" prefix. The default value is "" (empty string).Example:"signal::sig1""sig1" |
| resultName | [in] | char[] | This parameter specifies the name to be associated with measurement results. Provide a unique name, such as "r1" to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. The default value is "" (empty string) which refers to default result instance.Example:"result::r1""r1" |
| selectorStringLength | [in] | int32 | Specifies the length of the selector string. Set this parameter to 0 to get the minimum buffer size required to build the selector string. |
| selectorString | [in] | char[] | This parameter returns the selector string. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Build String

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__build__string_1ga233d4e7860fde419970f2346d1e08df3.html language=enus -->
## TOPIC 00191: RFmxNR_BuildPDSCHString

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__build__string_1ga233d4e7860fde419970f2346d1e08df3.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__build__string_1ga233d4e7860fde419970f2346d1e08df3.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates the PDSCH string. Syntaxint32 __stdcall RFmxNR_BuildPDSCHString(char selectorString[], int32 pdschNumber, int32 selectorStringOutLength, char selectorStringOut[])ParametersNameDirectionTypeDescriptionselectorString[in]char[]This parameter specifies a Selector String comprising of the signal

### RFmxNR_BuildPDSCHString

Creates the PDSCH string.

#### Syntax

int32 __stdcall RFmxNR_BuildPDSCHString(char selectorString[], int32 pdschNumber, int32 selectorStringOutLength, char selectorStringOut[])

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, subblock number, bandwidth part number, and user number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"subblock0/carrier0/bwp0/user0""signal::sig1/subblock0/carrier0/bwp0/user0""signal::sig1/result::r1/subblock0/carrier0/bwp/user0""result::r1/subblock0/carrier0/bwp0/user0"You can use the RFmxNR_BuildUserString function to build the selector string. |
| pdschNumber | [in] | int32 | This parameter specifies the PDSCH number for building the selector string. |
| selectorStringOutLength | [out] | int32 | Specifies the length of the string that is returned by the selectorStringOut parameter. To get the minimum buffer size required to build the selector string, set the selectorStringOutLength parameter to 0. |
| selectorStringOut | [out] | char[] | This parameter returns the selector string created by this function. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Build String

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__build__string_1ga47c05ca51011618cf11c8a8c7fac2bb2.html language=enus -->
## TOPIC 00192: RFmxNR_BuildPUSCHString

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__build__string_1ga47c05ca51011618cf11c8a8c7fac2bb2.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__build__string_1ga47c05ca51011618cf11c8a8c7fac2bb2.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates the PUSCH string. Syntaxint32 __stdcall RFmxNR_BuildPUSCHString(char selectorString[], int32 puschNumber, int32 selectorStringOutLength, char selectorStringOut[])ParametersNameDirectionTypeDescriptionselectorString[in]char[]This parameter specifies a Selector String comprising of the signal

### RFmxNR_BuildPUSCHString

Creates the PUSCH string.

#### Syntax

int32 __stdcall RFmxNR_BuildPUSCHString(char selectorString[], int32 puschNumber, int32 selectorStringOutLength, char selectorStringOut[])

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, subblock number, bandwidth part number, and user number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"subblock0/carrier0/bwp0/user0""signal::sig1/subblock0/carrier0/bwp0/user0""signal::sig1/result::r1/subblock0/carrier0/bwp/user0""result::r1/subblock0/carrier0/bwp0/user0"You can use the RFmxNR_BuildUserString function to build the selector string. |
| puschNumber | [in] | int32 | This parameter specifies the PUSCH number for building the selector string. |
| selectorStringOutLength | [out] | int32 | Specifies the length of the string that is returned by the selectorStringOut parameter. To get the minimum buffer size required to build the selector string, set the selectorStringOutLength parameter to 0. |
| selectorStringOut | [out] | char[] | This parameter returns the selector string created by this function. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Build String

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__build__string_1ga5cc0b5f18eec80d8785ac7ec67f61208.html language=enus -->
## TOPIC 00193: RFmxNR_BuildSubblockString

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__build__string_1ga5cc0b5f18eec80d8785ac7ec67f61208.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__build__string_1ga5cc0b5f18eec80d8785ac7ec67f61208.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates the subblock string. Syntaxint32 __stdcall RFmxNR_BuildSubblockString(char selectorString[], int32 subblockNumber, int32 selectorStringOutLength, char selectorStringOut[])ParametersNameDirectionTypeDescriptionselectorString[in]char[]This parameter specifies a Selector String comprising of th

### RFmxNR_BuildSubblockString

Creates the subblock string.

#### Syntax

int32 __stdcall RFmxNR_BuildSubblockString(char selectorString[], int32 subblockNumber, int32 selectorStringOutLength, char selectorStringOut[])

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default is "" (empty string).Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxNR_BuildSignalString function to build the selector string. |
| subblockNumber | [in] | int32 | This parameter specifies the number of subblocks that are configured in the non-contiguous carrier aggregation. Set this parameter to 1, which is the default, for single carrier and intra-band contiguous carrier aggregation. |
| selectorStringOutLength | [out] | int32 | Specifies the length of the string that is returned by the selectorStringOut parameter. To get the minimum buffer size required to build the selector string, set the selectorStringOutLength parameter to 0. |
| selectorStringOut | [out] | char[] | This parameter returns the selector string created by this function. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Build String

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__build__string_1ga6a99e59ac70377d79981f0eb947ecd74.html language=enus -->
## TOPIC 00194: RFmxNR_BuildUserString

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__build__string_1ga6a99e59ac70377d79981f0eb947ecd74.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__build__string_1ga6a99e59ac70377d79981f0eb947ecd74.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates the user number string. Syntaxint32 __stdcall RFmxNR_BuildUserString(char selectorString[], int32 userNumber, int32 selectorStringOutLength, char selectorStringOut[])ParametersNameDirectionTypeDescriptionselectorString[in]char[]This parameter specifies a Selector String comprising of the sig

### RFmxNR_BuildUserString

Creates the user number string.

#### Syntax

int32 __stdcall RFmxNR_BuildUserString(char selectorString[], int32 userNumber, int32 selectorStringOutLength, char selectorStringOut[])

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, subblock number, and bandwidth part number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"subblock0/carrier0/bwp0""signal::sig1/subblock0/carrier0/bwp0""result::r1/subblock0/carrier0/bwp0""signal::sig1/result::r1/subblock0/carrier0/bwp0"You can use the RFmxNR_BuildBandwidthPartString function to build the selector string. |
| userNumber | [in] | int32 | This parameter specifies the user number for building the selector string. |
| selectorStringOutLength | [out] | int32 | Specifies the length of the string that is returned by the selectorStringOut parameter. To get the minimum buffer size required to build the selector string, set the selectorStringOutLength parameter to 0. |
| selectorStringOut | [out] | char[] | This parameter returns the selector string created by this function. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Build String

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__configuration.html language=enus -->
## TOPIC 00195: Configuration

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__configuration.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__configuration.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsACPCHPModAccOBWPVTSelected PortsSEMTriggerGroup membersNameDescriptionRFmxNR_AutoLevelExamines the input signal to calculate the peak power level and sets it as the value of the RFMXNR_ATTR_REFERENCE_LEVEL attribute. Use this function to calculate an approximate setting for the reference level

### Configuration

#### Groups

- ACP
- CHP
- ModAcc
- OBW
- PVT
- Selected Ports
- SEM
- Trigger

#### Group members

| Name | Description |
| --- | --- |
| RFmxNR_AutoLevel | Examines the input signal to calculate the peak power level and sets it as the value of the RFMXNR_ATTR_REFERENCE_LEVEL attribute. Use this function to calculate an approximate setting for the reference level. |
| RFmxNR_CfgExternalAttenuation | Specifies the attenuation of a switch or cable connected to the RF IN connector of the signal analyzer. |
| RFmxNR_CfgFrequency | Configures the expected carrier frequency of the RF signal to acquire. The signal analyzer tunes to this frequency. |
| RFmxNR_CfgFrequencyReference | Configures the Reference Clock and the frequency reference source. |
| RFmxNR_CfgMechanicalAttenuation | Configures the mechanical attenuation and the RFmx driver attenuation hardware settings. |
| RFmxNR_CfgRF | Configures the RF attributes of the signal specified by the selector string. |
| RFmxNR_CfgRFAttenuation | Configures the nominal attenuation and the RFmx driver setting. |
| RFmxNR_CfgReferenceLevel | Configures the reference level which represents the maximum expected power of an RF input signal. |
| RFmxNR_CfggNodeBCategory | Configures the gNodeB Category of the signal being measured. |
| RFmxNR_SendSoftwareEdgeTrigger | Sends a trigger to the device when you use the RFmxNR Configure Trigger function to choose a software version of a trigger and the device is waiting for the trigger to be sent. You can also use this function to override a hardware trigger. |

#### Attachments

None

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__configuration_1ga0980ee4fa2eb024100413da9d2d85a99.html language=enus -->
## TOPIC 00196: RFmxNR_CfggNodeBCategory

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__configuration_1ga0980ee4fa2eb024100413da9d2d85a99.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__configuration_1ga0980ee4fa2eb024100413da9d2d85a99.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the gNodeB Category of the signal being measured. Syntaxint32 __stdcall RFmxNR_CfggNodeBCategory(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 gNodeBCategory)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifies the RFmx ses

### RFmxNR_CfggNodeBCategory

Configures the gNodeB Category of the signal being measured.

#### Syntax

int32 __stdcall RFmxNR_CfggNodeBCategory(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 gNodeBCategory)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string).Example:"signal::sig1"You can use the RFmxNR_BuildSignalString function to build the selector string. |
| gNodeBCategory | [in] | int32 | This parameter specifies the downlink gNodeB (Base station) category. Refer to 3GPP 38.104 specification for more information about gNodeB Category. The default value is Wide Area Base Station - Category A.NameValueDescriptionRFMXNR_VAL_GNODEB_CATEGORY_WIDE_AREA_BASE_STATION_CATEGORY_A0 (0x0)Specifies that the gNodeB type is Wide Area Base Station - Category A.RFMXNR_VAL_GNODEB_CATEGORY_WIDE_AREA_BASE_STATION_CATEGORY_B_OPTION11 (0x1)Specifies that the gNodeB type is Wide Area Base Station - Category B Option1.RFMXNR_VAL_GNODEB_CATEGORY_WIDE_AREA_BASE_STATION_CATEGORY_B_OPTION22 (0x2)Specifies that the gNodeB type is Wide Area Base Station - Category B Option2.RFMXNR_VAL_GNODEB_CATEGORY_LOCAL_AREA_BASE_STATION3 (0x3)Specifies that the gNodeB type is Local Area Base Station.RFMXNR_VAL_GNODEB_CATEGORY_MEDIUM_RANGE_BASE_STATION5 (0x5)Specifies that the gNodeB type is Medium Range Base Station.RFMXNR_VAL_GNODEB_CATEGORY_FR2_CATEGORY_A6 (0x6)Specifies that the gNodeB type is FR2 Category A.RFMXNR_VAL_GNODEB_CATEGORY_FR2_CATEGORY_B7 (0x7)Specifies that the gNodeB type is FR2 Category B. |
| Name | Value | Description |  |
| RFMXNR_VAL_GNODEB_CATEGORY_WIDE_AREA_BASE_STATION_CATEGORY_A | 0 (0x0) | Specifies that the gNodeB type is Wide Area Base Station - Category A. |  |
| RFMXNR_VAL_GNODEB_CATEGORY_WIDE_AREA_BASE_STATION_CATEGORY_B_OPTION1 | 1 (0x1) | Specifies that the gNodeB type is Wide Area Base Station - Category B Option1. |  |
| RFMXNR_VAL_GNODEB_CATEGORY_WIDE_AREA_BASE_STATION_CATEGORY_B_OPTION2 | 2 (0x2) | Specifies that the gNodeB type is Wide Area Base Station - Category B Option2. |  |
| RFMXNR_VAL_GNODEB_CATEGORY_LOCAL_AREA_BASE_STATION | 3 (0x3) | Specifies that the gNodeB type is Local Area Base Station. |  |
| RFMXNR_VAL_GNODEB_CATEGORY_MEDIUM_RANGE_BASE_STATION | 5 (0x5) | Specifies that the gNodeB type is Medium Range Base Station. |  |
| RFMXNR_VAL_GNODEB_CATEGORY_FR2_CATEGORY_A | 6 (0x6) | Specifies that the gNodeB type is FR2 Category A. |  |
| RFMXNR_VAL_GNODEB_CATEGORY_FR2_CATEGORY_B | 7 (0x7) | Specifies that the gNodeB type is FR2 Category B. |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__configuration_1ga21ff3bca4675060ced902ba463c92cc3.html language=enus -->
## TOPIC 00197: RFmxNR_CfgReferenceLevel

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__configuration_1ga21ff3bca4675060ced902ba463c92cc3.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__configuration_1ga21ff3bca4675060ced902ba463c92cc3.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the reference level which represents the maximum expected power of an RF input signal. Syntaxint32 __stdcall RFmxNR_CfgReferenceLevel(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 referenceLevel)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHand

### RFmxNR_CfgReferenceLevel

Configures the reference level which represents the maximum expected power of an RF input signal.

#### Syntax

int32 __stdcall RFmxNR_CfgReferenceLevel(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 referenceLevel)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string).Example:"signal::sig1"You can use the RFmxNR_BuildSignalString function to build the selector string. |
| referenceLevel | [in] | float64 | This parameter specifies the reference level which represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices. The default value of this parameter is hardware dependent. |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__configuration_1ga497c6979f40795a75ac7547732f11ec2.html language=enus -->
## TOPIC 00198: RFmxNR_SendSoftwareEdgeTrigger

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__configuration_1ga497c6979f40795a75ac7547732f11ec2.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__configuration_1ga497c6979f40795a75ac7547732f11ec2.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sends a trigger to the device when you use the RFmxNR Configure Trigger function to choose a software version of a trigger and the device is waiting for the trigger to be sent. You can also use this function to override a hardware trigger. Syntaxint32 __stdcall RFmxNR_SendSoftwareEdgeTrigger(niRFmxI

### RFmxNR_SendSoftwareEdgeTrigger

Sends a trigger to the device when you use the RFmxNR Configure Trigger function to choose a software version of a trigger and the device is waiting for the trigger to be sent. You can also use this function to override a hardware trigger.

#### Syntax

int32 __stdcall RFmxNR_SendSoftwareEdgeTrigger(niRFmxInstrHandle instrumentHandle)

#### Remarks

- You configure an invalid trigger.
- You have not previously called the [RFmxNR_Initiate](group____root__ni_r_fmx_n_r__functions_1ga1feff952d2974304538c63402d9188e6.html) function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__configuration_1ga59b3d46ea5e6e5539f1c551046d1d6c0.html language=enus -->
## TOPIC 00199: RFmxNR_AutoLevel

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__configuration_1ga59b3d46ea5e6e5539f1c551046d1d6c0.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__configuration_1ga59b3d46ea5e6e5539f1c551046d1d6c0.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Examines the input signal to calculate the peak power level and sets it as the value of the RFMXNR_ATTR_REFERENCE_LEVEL attribute. Use this function to calculate an approximate setting for the reference level. Syntaxint32 __stdcall RFmxNR_AutoLevel(niRFmxInstrHandle instrumentHandle, char selectorSt

### RFmxNR_AutoLevel

Examines the input signal to calculate the peak power level and sets it as the value of the [RFMXNR_ATTR_REFERENCE_LEVEL](group____root__ni_r_fmx_n_r__attributes_1ga404847dba9dba752bde4bc9939581d3a.html) attribute. Use this function to calculate an approximate setting for the reference level.

#### Syntax

int32 __stdcall RFmxNR_AutoLevel(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 measurementInterval, float64 *referenceLevel)

#### Remarks

1. Resets the mixer level, mixer level offset, and IF output power offset.
2. Sets the starting reference level to the maximum reference level supported by the device based on the current RF attenuation, mechanical attenuation, and preamplifier enabled settings.
3. Iterates to adjust the reference level based on the input signal peak power.
4. Uses immediate triggering and restores the trigger settings back to user setting after the execution.

When using NI-PXIe 5663, NI-PXIe 5665, or NI-PXIe 5668R device, NI recommends that you set an appropriate value for mechanical attenuation before calling the RFmxNR Auto Level function. Setting an appropriate value for mechanical attenuation reduces the number of times the attenuator settings are changed by this function; thus reducing wear and tear, and maximizing the life time of the attenuator.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string).Example:"signal::sig1"You can use the RFmxNR_BuildSignalString function to build the selector string. |
| measurementInterval | [in] | float64 | This parameter specifies the acquisition length. This value is expressed in seconds. Use this value to compute the number of samples to acquire from the signal analyzer. The default value is 10 ms.Auto Level function does not use any trigger for acquisition. It ignores the user-configured trigger attributes. NI recommends that you set a sufficiently high measurement interval to ensure that the acquired waveform is at least as long as one period of the signal. |
| referenceLevel | [out] | float64 * | This parameter returns the estimated peak power level of the input signal. This value is expressed in dBm. The default value of this parameter is hardware dependent. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__configuration_1ga6ef67e7d632a4a0c9e00ceb6982864d5.html language=enus -->
## TOPIC 00200: RFmxNR_CfgMechanicalAttenuation

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__configuration_1ga6ef67e7d632a4a0c9e00ceb6982864d5.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__configuration_1ga6ef67e7d632a4a0c9e00ceb6982864d5.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the mechanical attenuation and the RFmx driver attenuation hardware settings. Syntaxint32 __stdcall RFmxNR_CfgMechanicalAttenuation(niRFmxInstrHandle instrumentHandle, char channelName[], int32 mechanicalAttenuationAuto, float64 mechanicalAttenuationValue)RemarksThis function is a wrapper

### RFmxNR_CfgMechanicalAttenuation

Configures the mechanical attenuation and the RFmx driver attenuation hardware settings.

#### Syntax

int32 __stdcall RFmxNR_CfgMechanicalAttenuation(niRFmxInstrHandle instrumentHandle, char channelName[], int32 mechanicalAttenuationAuto, float64 mechanicalAttenuationValue)

#### Remarks

This function is a wrapper over the RFmx Instruments API, and calls the [RFmxInstr_CfgMechanicalAttenuation](/csh?context=rfmxinstr_rfmxinstrcref_function_cfg_mechanical_attenuation) function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxNR_Initialize function. |
| channelName | [in] | char[] | Set this parameter to "" (empty string) or NULL. |
| mechanicalAttenuationAuto | [in] | int32 | Specifies whether the RFmx driver automatically chooses an attenuation setting based on the hardware settings.ValueDescriptionRFMXNR_VAL_MECHANICAL_ATTENUATION_AUTO_FALSE (0)Specifies that the RFmx driver uses the value configured in the mechanicalAttenuationValue parameter.RFMXNR_VAL_MECHANICAL_ATTENUATION_AUTO_TRUE (1)Specifies that the measurement computes the mechanical attenuation. |
| Value | Description |  |  |
| RFMXNR_VAL_MECHANICAL_ATTENUATION_AUTO_FALSE (0) | Specifies that the RFmx driver uses the value configured in the mechanicalAttenuationValue parameter. |  |  |
| RFMXNR_VAL_MECHANICAL_ATTENUATION_AUTO_TRUE (1) | Specifies that the measurement computes the mechanical attenuation. |  |  |
| mechanicalAttenuationValue | [in] | float64 | Specifies the level of mechanical attenuation, in dB, for the RF path when the mechanicalAttenuationAuto is set to RFMXNR_VAL_MECHANICAL_ATTENUATION_AUTO_FALSE. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__configuration_1ga7ed125fbe9b025767b30840e66c9d539.html language=enus -->
## TOPIC 00201: RFmxNR_CfgFrequencyReference

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__configuration_1ga7ed125fbe9b025767b30840e66c9d539.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__configuration_1ga7ed125fbe9b025767b30840e66c9d539.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the Reference Clock and the frequency reference source. Syntaxint32 __stdcall RFmxNR_CfgFrequencyReference(niRFmxInstrHandle instrumentHandle, char channelName[], char frequencyReferenceSource[], float64 frequencyReferenceFrequency)RemarksThis function is a wrapper over the RFmx Instrumen

### RFmxNR_CfgFrequencyReference

Configures the Reference Clock and the frequency reference source.

#### Syntax

int32 __stdcall RFmxNR_CfgFrequencyReference(niRFmxInstrHandle instrumentHandle, char channelName[], char frequencyReferenceSource[], float64 frequencyReferenceFrequency)

#### Remarks

This function is a wrapper over the RFmx Instruments API, and calls the [RFmxInstr_CfgFrequencyReference](/csh?context=rfmxinstr_rfmxinstrcref_function_cfg_frequency_reference) function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxNR_Initialize function. |
| channelName | [in] | char[] | Set this parameter to "" (empty string) or NULL. |
| frequencyReferenceSource | [in] | char[] | Specifies the frequency reference source.ValueDescriptionRFMXNR_VAL_ONBOARD_CLOCK_STR ("Onboard Clock")PXIe-5663/5663E: The RFmx driver locks the PXIe-5663/5663E to the PXIe-5652 LO source onboard clock. Connect the REF OUT2 connector (if it exists) on the PXIe-5652 to the PXIe-5622 CLK IN terminal. On versions of the PXIe-5663/5663E that lack a REF OUT2 connector on the PXIe-5652, connect the REF IN/OUT connector on the PXIe-5652 to the PXIe-5622 CLK IN terminal.PXIe-5665: The RFmx driver locks the PXIe-5665 to the PXIe-5653 LO source onboard clock. Connect the 100 MHz REF OUT terminal on the PXIe-5653 to the PXIe-5622 CLK IN terminal.PXIe-5644R/5645R/5646R, PXIe-5840: The RFmx driver locks the device to its onboard clock.RFMXNR_VAL_REF_IN_STR ("RefIn")PXIe-5663/5663E: Connect the external signal to the PXIe-5652 REF IN/OUT connector. Connect the REF OUT2 connector (if it exists) on the PXIe-5652 to the PXIe-5622 CLK IN terminal.PXIe-5665: Connect the external signal to the PXIe-5653 REF IN connector. Connect the 100 MHz REF OUT terminal on the PXIe-5653 to the PXIe-5622 CLK IN connector. If your external clock signal frequency is set to a frequency other than 10 MHz, set the frequencyReferenceFrequency parameter according to the frequency of your external clock signal.PXIe-5644R/5645R/5646R, PXIe-5840: The RFmx driver locks the device to the signal at the external REF IN connector.RFMXNR_VAL_PXI_CLK_STR ("PXI_Clk")PXIe-5644R/5645R/5646R, PXIe-5663/5663E/5665, PXIe-5840: The RFmx driver locks the PXIe-5644R/5645R/5646R, PXIe-5663/5663E/5665 to the PXI backplane clock.RFMXNR_VAL_CLK_IN_STR ("ClkIn")PXIe-5663/5663E: The RFmx driver locks the PXIe-5663/5663E to an external 10 MHz signal. Connect the external signal to the PXIe-5622 CLK IN connector, and connect the PXIe-5622 CLK OUT connector to the FREQ REF IN connector on the PXIe-5652.PXIe-5665: The RFmx driver locks the PXIe-5665 to an external 100 MHz signal. Connect the external signal to the PXIe-5622 CLK IN connector, and connect the PXIe-5622 CLK OUT connector to the REF IN connector on the PXIe-5653. Set the frequencyReferenceFrequency parameter to 100 MHz.PXIe-5644R/5645R/5646R, PXIe-5840: This configuration does not apply to the PXIe-5644R/5645R/5646R. |
| Value | Description |  |  |
| RFMXNR_VAL_ONBOARD_CLOCK_STR ("Onboard Clock") | PXIe-5663/5663E: The RFmx driver locks the PXIe-5663/5663E to the PXIe-5652 LO source onboard clock. Connect the REF OUT2 connector (if it exists) on the PXIe-5652 to the PXIe-5622 CLK IN terminal. On versions of the PXIe-5663/5663E that lack a REF OUT2 connector on the PXIe-5652, connect the REF IN/OUT connector on the PXIe-5652 to the PXIe-5622 CLK IN terminal.PXIe-5665: The RFmx driver locks the PXIe-5665 to the PXIe-5653 LO source onboard clock. Connect the 100 MHz REF OUT terminal on the PXIe-5653 to the PXIe-5622 CLK IN terminal.PXIe-5644R/5645R/5646R, PXIe-5840: The RFmx driver locks the device to its onboard clock. |  |  |
| RFMXNR_VAL_REF_IN_STR ("RefIn") | PXIe-5663/5663E: Connect the external signal to the PXIe-5652 REF IN/OUT connector. Connect the REF OUT2 connector (if it exists) on the PXIe-5652 to the PXIe-5622 CLK IN terminal.PXIe-5665: Connect the external signal to the PXIe-5653 REF IN connector. Connect the 100 MHz REF OUT terminal on the PXIe-5653 to the PXIe-5622 CLK IN connector. If your external clock signal frequency is set to a frequency other than 10 MHz, set the frequencyReferenceFrequency parameter according to the frequency of your external clock signal.PXIe-5644R/5645R/5646R, PXIe-5840: The RFmx driver locks the device to the signal at the external REF IN connector. |  |  |
| RFMXNR_VAL_PXI_CLK_STR ("PXI_Clk") | PXIe-5644R/5645R/5646R, PXIe-5663/5663E/5665, PXIe-5840: The RFmx driver locks the PXIe-5644R/5645R/5646R, PXIe-5663/5663E/5665 to the PXI backplane clock. |  |  |
| RFMXNR_VAL_CLK_IN_STR ("ClkIn") | PXIe-5663/5663E: The RFmx driver locks the PXIe-5663/5663E to an external 10 MHz signal. Connect the external signal to the PXIe-5622 CLK IN connector, and connect the PXIe-5622 CLK OUT connector to the FREQ REF IN connector on the PXIe-5652.PXIe-5665: The RFmx driver locks the PXIe-5665 to an external 100 MHz signal. Connect the external signal to the PXIe-5622 CLK IN connector, and connect the PXIe-5622 CLK OUT connector to the REF IN connector on the PXIe-5653. Set the frequencyReferenceFrequency parameter to 100 MHz.PXIe-5644R/5645R/5646R, PXIe-5840: This configuration does not apply to the PXIe-5644R/5645R/5646R. |  |  |
| frequencyReferenceFrequency | [in] | float64 | Specifies the Reference Clock rate, in Hz, when the frequencyReferenceSource parameter is set to RFMXNR_VAL_CLK_IN_STR or RFMXNR_VAL_REF_IN_STR. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__configuration_1gae3cfd32818a9cf1d4dc308eb33ae618a.html language=enus -->
## TOPIC 00202: RFmxNR_CfgExternalAttenuation

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__configuration_1gae3cfd32818a9cf1d4dc308eb33ae618a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__configuration_1gae3cfd32818a9cf1d4dc308eb33ae618a.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the attenuation of a switch or cable connected to the RF IN connector of the signal analyzer. Syntaxint32 __stdcall RFmxNR_CfgExternalAttenuation(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 externalAttenuation)ParametersNameDirectionTypeDescriptioninstrumentHandle[in

### RFmxNR_CfgExternalAttenuation

Specifies the attenuation of a switch or cable connected to the RF IN connector of the signal analyzer.

#### Syntax

int32 __stdcall RFmxNR_CfgExternalAttenuation(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 externalAttenuation)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string).Example:"signal::sig1"You can use the RFmxNR_BuildSignalString function to build the selector string. |
| externalAttenuation | [in] | float64 | This parameter specifies the attenuation of a switch or cable connected to the RF IN connector of the signal analyzer. This value is expressed in dB. For more information about attenuation, refer to the RF Attenuation and Signal Levels topic for your device in the NI RF Vector Signal Analyzers Help. The default value is 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__configuration_1gafdf134b66e88b3ad5b79539fa55d2f0b.html language=enus -->
## TOPIC 00203: RFmxNR_CfgFrequency

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__configuration_1gafdf134b66e88b3ad5b79539fa55d2f0b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__configuration_1gafdf134b66e88b3ad5b79539fa55d2f0b.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the expected carrier frequency of the RF signal to acquire. The signal analyzer tunes to this frequency. Syntaxint32 __stdcall RFmxNR_CfgFrequency(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 centerFrequency)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]n

### RFmxNR_CfgFrequency

Configures the expected carrier frequency of the RF signal to acquire. The signal analyzer tunes to this frequency.

#### Syntax

int32 __stdcall RFmxNR_CfgFrequency(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 centerFrequency)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and the subblock number. If you do not specify the signal name, the default signal instance is used. The default value is "subblock0".Example:"subblock0""signal::sig1/subblock0"You can use the RFmxNR_BuildSignalString function to build the selector string. |
| centerFrequency | [in] | float64 | This parameter specifies the expected carrier frequency, in Hz, of the RF signal to acquire. The signal analyzer tunes to this frequency. The default of this attribute is hardware dependent. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__configuration__acp.html language=enus -->
## TOPIC 00204: ACP

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__configuration__acp.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__configuration__acp.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxNR_ACPCfgAveragingConfigures averaging for the ACP measurement. RFmxNR_ACPCfgMeasurementMethodConfigures the method for performing the ACP measurement. RFmxNR_ACPCfgNoiseCompensationEnabledConfigures compensation of the channel powers for the inherent noise

### ACP

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxNR_ACPCfgAveraging | Configures averaging for the ACP measurement. |
| RFmxNR_ACPCfgMeasurementMethod | Configures the method for performing the ACP measurement. |
| RFmxNR_ACPCfgNoiseCompensationEnabled | Configures compensation of the channel powers for the inherent noise floor of the signal analyzer. |
| RFmxNR_ACPCfgNumberOfENDCOffsets | Configures the number of ENDC adjacent channels of the subblock. |
| RFmxNR_ACPCfgNumberOfEUTRAOffsets | Configures the number of E-UTRA adjacent channels of the subblock. |
| RFmxNR_ACPCfgNumberOfNROffsets | Configures the number of NR adjacent channels of the subblock. |
| RFmxNR_ACPCfgNumberOfUTRAOffsets | Configures the number of UTRA adjacent channels of the subblock. |
| RFmxNR_ACPCfgPowerUnits | Configures the unit for absolute power. |
| RFmxNR_ACPCfgRBWFilter | Configures the resolution bandwidth (RBW) filter. |
| RFmxNR_ACPCfgSweepTime | Configures the sweep time. |
| RFmxNR_ACPValidateNoiseCalibrationData | Indicates whether the ACP noise calibration data is valid for the configuration specified by the signal name in the Selector String parameter. |

#### Attachments

None

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__configuration__acp_1ga2924924a28ce97bfbec303e1509e6cf8.html language=enus -->
## TOPIC 00205: RFmxNR_ACPCfgNumberOfUTRAOffsets

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__configuration__acp_1ga2924924a28ce97bfbec303e1509e6cf8.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__configuration__acp_1ga2924924a28ce97bfbec303e1509e6cf8.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the number of UTRA adjacent channels of the subblock. Syntaxint32 __stdcall RFmxNR_ACPCfgNumberOfUTRAOffsets(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 numberOfUTRAOffsets)RemarksUse "subblock<n>" as the selector string to configure this function.ParametersNameDirect

### RFmxNR_ACPCfgNumberOfUTRAOffsets

Configures the number of UTRA adjacent channels of the subblock.

#### Syntax

int32 __stdcall RFmxNR_ACPCfgNumberOfUTRAOffsets(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 numberOfUTRAOffsets)

#### Remarks

Use "subblock<n>" as the selector string to configure this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and the subblock number. If you do not specify the signal name, the default signal instance is used. The default value is "subblock0".Example:"subblock0""signal::sig1/subblock0"You can use the RFmxNR_BuildSignalString function to build the selector string. |
| numberOfUTRAOffsets | [in] | int32 | This parameter specifies the number of UTRA adjacent channel offsets to be configured at offset positions. For uplink ACP measurement in frequency range 2, and for downlink ACP measurement, this parameter has to be 0. The default value is dependent on 3GPP specification. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ACP

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__configuration__acp_1ga2d8021010b8c0540eae1ee67b6c636fa.html language=enus -->
## TOPIC 00206: RFmxNR_ACPCfgRBWFilter

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__configuration__acp_1ga2d8021010b8c0540eae1ee67b6c636fa.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__configuration__acp_1ga2d8021010b8c0540eae1ee67b6c636fa.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the resolution bandwidth (RBW) filter. Syntaxint32 __stdcall RFmxNR_ACPCfgRBWFilter(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 rbwAuto, float64 rbw, int32 rbwFilterType)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifie

### RFmxNR_ACPCfgRBWFilter

Configures the resolution bandwidth (RBW) filter.

#### Syntax

int32 __stdcall RFmxNR_ACPCfgRBWFilter(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 rbwAuto, float64 rbw, int32 rbwFilterType)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string).Example:"signal::sig1"You can use the RFmxNR_BuildSignalString function to build the selector string. |
| rbwAuto | [in] | int32 | This parameter specifies whether the measurement computes the RBW. The default value is True.NameValueDescriptionRFMXNR_VAL_ACP_RBW_FILTER_AUTO_BANDWIDTH_FALSE0 (0x0)The measurement uses the RBW that you specify in the RFMXNR_ATTR_ACP_RBW_FILTER_BANDWIDTH attribute.RFMXNR_VAL_ACP_RBW_FILTER_AUTO_BANDWIDTH_TRUE1 (0x1)The measurement computes the RBW. |
| Name | Value | Description |  |
| RFMXNR_VAL_ACP_RBW_FILTER_AUTO_BANDWIDTH_FALSE | 0 (0x0) | The measurement uses the RBW that you specify in the RFMXNR_ATTR_ACP_RBW_FILTER_BANDWIDTH attribute. |  |
| RFMXNR_VAL_ACP_RBW_FILTER_AUTO_BANDWIDTH_TRUE | 1 (0x1) | The measurement computes the RBW. |  |
| rbw | [in] | float64 | This parameter specifies the bandwidth of the RBW filter, used to sweep the acquired signal, when you set the RBW Auto parameter to False. This value is expressed in Hz. The default value is 30 kHz. |
| rbwFilterType | [in] | int32 | This parameter specifies the shape of the RBW filter. The default value is FFT Based.NameValueDescriptionRFMXNR_VAL_ACP_RBW_FILTER_TYPE_FFT_BASED0 (0x0)No RBW filtering is performed.RFMXNR_VAL_ACP_RBW_FILTER_TYPE_GAUSSIAN1 (0x1)An RBW filter with a Gaussian response is applied.RFMXNR_VAL_ACP_RBW_FILTER_TYPE_FLAT2 (0x2)An RBW filter with a flat response is applied. |
| Name | Value | Description |  |
| RFMXNR_VAL_ACP_RBW_FILTER_TYPE_FFT_BASED | 0 (0x0) | No RBW filtering is performed. |  |
| RFMXNR_VAL_ACP_RBW_FILTER_TYPE_GAUSSIAN | 1 (0x1) | An RBW filter with a Gaussian response is applied. |  |
| RFMXNR_VAL_ACP_RBW_FILTER_TYPE_FLAT | 2 (0x2) | An RBW filter with a flat response is applied. |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ACP

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__configuration__acp_1ga4c7a6ff21f7efba753a2fea58232dff0.html language=enus -->
## TOPIC 00207: RFmxNR_ACPCfgAveraging

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__configuration__acp_1ga4c7a6ff21f7efba753a2fea58232dff0.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__configuration__acp_1ga4c7a6ff21f7efba753a2fea58232dff0.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures averaging for the ACP measurement. Syntaxint32 __stdcall RFmxNR_ACPCfgAveraging(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 averagingEnabled, int32 averagingCount, int32 averagingType)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis para

### RFmxNR_ACPCfgAveraging

Configures averaging for the ACP measurement.

#### Syntax

int32 __stdcall RFmxNR_ACPCfgAveraging(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 averagingEnabled, int32 averagingCount, int32 averagingType)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string).Example:"signal::sig1"You can use the RFmxNR_BuildSignalString function to build the selector string. |
| averagingEnabled | [in] | int32 | This parameter specifies whether to enable averaging for the measurement. The default value is False.NameValueDescriptionRFMXNR_VAL_ACP_AVERAGING_ENABLED_FALSE0 (0x0)The measurement is performed on a single acquisition.RFMXNR_VAL_ACP_AVERAGING_ENABLED_TRUE1 (0x1)The ACP measurement uses the value of the RFMXNR_ATTR_ACP_AVERAGING_COUNT attribute as the number of acquisitions over which the ACP measurement is averaged. |
| Name | Value | Description |  |
| RFMXNR_VAL_ACP_AVERAGING_ENABLED_FALSE | 0 (0x0) | The measurement is performed on a single acquisition. |  |
| RFMXNR_VAL_ACP_AVERAGING_ENABLED_TRUE | 1 (0x1) | The ACP measurement uses the value of the RFMXNR_ATTR_ACP_AVERAGING_COUNT attribute as the number of acquisitions over which the ACP measurement is averaged. |  |
| averagingCount | [in] | int32 | This parameter specifies the number of acquisitions used for averaging when you set the Averaging Enabled parameter to True. The default value is 10. |
| averagingType | [in] | int32 | This parameter specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the measurement. The default value is RMS.NameValueDescriptionRFMXNR_VAL_ACP_AVERAGING_TYPE_RMS0 (0x0)The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations, but not the noise floor.RFMXNR_VAL_ACP_AVERAGING_TYPE_LOG1 (0x1)The power spectrum is averaged in a logarithmic scale.RFMXNR_VAL_ACP_AVERAGING_TYPE_SCALAR2 (0x2)The square root of the power spectrum is averaged.RFMXNR_VAL_ACP_AVERAGING_TYPE_MAXIMUM3 (0x3)The peak power in the spectrum at each frequency bin is retained from one acquisition to the next.RFMXNR_VAL_ACP_AVERAGING_TYPE_MINIMUM4 (0x4)The lowest power in the spectrum at each frequency bin is retained from one acquisition to the next. |
| Name | Value | Description |  |
| RFMXNR_VAL_ACP_AVERAGING_TYPE_RMS | 0 (0x0) | The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations, but not the noise floor. |  |
| RFMXNR_VAL_ACP_AVERAGING_TYPE_LOG | 1 (0x1) | The power spectrum is averaged in a logarithmic scale. |  |
| RFMXNR_VAL_ACP_AVERAGING_TYPE_SCALAR | 2 (0x2) | The square root of the power spectrum is averaged. |  |
| RFMXNR_VAL_ACP_AVERAGING_TYPE_MAXIMUM | 3 (0x3) | The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. |  |
| RFMXNR_VAL_ACP_AVERAGING_TYPE_MINIMUM | 4 (0x4) | The lowest power in the spectrum at each frequency bin is retained from one acquisition to the next. |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ACP

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__configuration__acp_1ga5930a930c50413b7e65f5a3b7a89378c.html language=enus -->
## TOPIC 00208: RFmxNR_ACPCfgMeasurementMethod

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__configuration__acp_1ga5930a930c50413b7e65f5a3b7a89378c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__configuration__acp_1ga5930a930c50413b7e65f5a3b7a89378c.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the method for performing the ACP measurement. Syntaxint32 __stdcall RFmxNR_ACPCfgMeasurementMethod(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 measurementMethod)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifies the RF

### RFmxNR_ACPCfgMeasurementMethod

Configures the method for performing the ACP measurement.

#### Syntax

int32 __stdcall RFmxNR_ACPCfgMeasurementMethod(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 measurementMethod)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string).Example:"signal::sig1"You can use the RFmxNR_BuildSignalString function to build the selector string. |
| measurementMethod | [in] | int32 | This parameter specifies the method for performing the ACP measurement. The default value is Normal.NameValueDescriptionRFMXNR_VAL_ACP_MEASUREMENT_METHOD_NORMAL0 (0x0)The ACP measurement acquires the spectrum using the same signal analyzer setting across frequency bands. Use this method when measurement speed is desirable over higher dynamic range.RFMXNR_VAL_ACP_MEASUREMENT_METHOD_DYNAMIC_RANGE1 (0x1)The ACP measurement acquires the spectrum using the hardware-specific optimizations for different frequency bands. Use this method to get the best dynamic range. Supported Devices: PXIe 5665/5668R\| RFMXNR_VAL_ACP_MEASUREMENT_METHOD_SEQUENTIAL_FFT \| 2 (0x2) \| The ACP measurement acquires I/Q samples for a duration specified by the RFMXNR_ATTR_ACP_SWEEP_TIME_INTERVAL attribute. These samples are divided into smaller chunks. The size of each chunk is defined by the RFMXNR_ATTR_ACP_SEQUENTIAL_FFT_SIZE attribute, and the FFT is computed on each of these chunks. The resultant FFTs are averaged to get the spectrum and is used to compute the ACP. If the total acquired samples is not an integer multiple of the FFT size, the remaining samples at the end of the acquisition are not used for the measurement. Use this method to optimize ACP Measurement speed. The accuracy of results may be reduced when using this measurement method. For accurate power measurements when the power characteristics of the signal vary over time, averaging is allowed. The following attributes have limited support when you set the RFMXNR_ATTR_ACP_MEASUREMENT_METHOD to Sequential FFT.\| Property \| Supported Value \|\|-----------------------------------------—\|------------------—\|\| RFMXNR_ATTR_ACP_RBW_FILTER_AUTO_BANDWIDTH \| True \|\| RFMXNR_ATTR_ACP_RBW_FILTER_TYPE \| FFT Based \|\| RFMXNR_ATTR_ACP_AVERAGING_COUNT \| >=1 \|\| RFMXNR_ATTR_ACP_NUMBER_OF_ANALYSIS_THREADS \| >=1 \|\| RFMXNR_ATTR_ACP_AMPLITUDE_CORRECTION_TYPE \| RF Center Frequency \| \| |
| Name | Value | Description |  |
| RFMXNR_VAL_ACP_MEASUREMENT_METHOD_NORMAL | 0 (0x0) | The ACP measurement acquires the spectrum using the same signal analyzer setting across frequency bands. Use this method when measurement speed is desirable over higher dynamic range. |  |
| RFMXNR_VAL_ACP_MEASUREMENT_METHOD_DYNAMIC_RANGE | 1 (0x1) | The ACP measurement acquires the spectrum using the hardware-specific optimizations for different frequency bands. Use this method to get the best dynamic range. Supported Devices: PXIe 5665/5668R |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ACP

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__configuration__acp_1gab455506e6ee6d50cb719cfa1f3ee1c06.html language=enus -->
## TOPIC 00209: RFmxNR_ACPCfgNumberOfEUTRAOffsets

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__configuration__acp_1gab455506e6ee6d50cb719cfa1f3ee1c06.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__configuration__acp_1gab455506e6ee6d50cb719cfa1f3ee1c06.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the number of E-UTRA adjacent channels of the subblock. Syntaxint32 __stdcall RFmxNR_ACPCfgNumberOfEUTRAOffsets(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 numberOfEUTRAOffsets)RemarksUse "subblock<n>" as the selector string to configure this function.ParametersNameDi

### RFmxNR_ACPCfgNumberOfEUTRAOffsets

Configures the number of E-UTRA adjacent channels of the subblock.

#### Syntax

int32 __stdcall RFmxNR_ACPCfgNumberOfEUTRAOffsets(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 numberOfEUTRAOffsets)

#### Remarks

Use "subblock<n>" as the selector string to configure this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and the subblock number. If you do not specify the signal name, the default signal instance is used. The default value is "subblock0".Example:"subblock0""signal::sig1/subblock0"You can use the RFmxNR_BuildSignalString function to build the selector string. |
| numberOfEUTRAOffsets | [in] | int32 | This parameter specifies the number of E-UTRA adjacent channel offsets to be configured at offset positions. For downlink ACP measurement in frequency range 2, and for uplink ACP measurement, this parameter has to be 0. The default value is dependent on 3GPP specification. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ACP

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__configuration__acp_1gac047193510eb85c4c778873dea50b1bc.html language=enus -->
## TOPIC 00210: RFmxNR_ACPCfgNumberOfNROffsets

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__configuration__acp_1gac047193510eb85c4c778873dea50b1bc.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__configuration__acp_1gac047193510eb85c4c778873dea50b1bc.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the number of NR adjacent channels of the subblock. Syntaxint32 __stdcall RFmxNR_ACPCfgNumberOfNROffsets(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 numberOfNrOffsets)RemarksUse "subblock<n>" as the selector string to configure this function.ParametersNameDirectionTyp

### RFmxNR_ACPCfgNumberOfNROffsets

Configures the number of NR adjacent channels of the subblock.

#### Syntax

int32 __stdcall RFmxNR_ACPCfgNumberOfNROffsets(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 numberOfNrOffsets)

#### Remarks

Use "subblock<n>" as the selector string to configure this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and the subblock number. If you do not specify the signal name, the default signal instance is used. The default value is "subblock0".Example:"subblock0""signal::sig1/subblock0"You can use the RFmxNR_BuildSignalString function to build the selector string. |
| numberOfNrOffsets | [in] | int32 | This parameter specifies the number of NR adjacent channel offsets to be configured at offset positions. The default value is dependent on 3GPP specification. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ACP

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__configuration__acp_1gaccae004d1e82987ee6f18b33b4f0650b.html language=enus -->
## TOPIC 00211: RFmxNR_ACPCfgNoiseCompensationEnabled

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__configuration__acp_1gaccae004d1e82987ee6f18b33b4f0650b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__configuration__acp_1gaccae004d1e82987ee6f18b33b4f0650b.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures compensation of the channel powers for the inherent noise floor of the signal analyzer. Syntaxint32 __stdcall RFmxNR_ACPCfgNoiseCompensationEnabled(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 noiseCompensationEnabled)ParametersNameDirectionTypeDescriptioninstrumentHan

### RFmxNR_ACPCfgNoiseCompensationEnabled

Configures compensation of the channel powers for the inherent noise floor of the signal analyzer.

#### Syntax

int32 __stdcall RFmxNR_ACPCfgNoiseCompensationEnabled(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 noiseCompensationEnabled)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string).Example:"signal::sig1"You can use the RFmxNR_BuildSignalString function to build the selector string. |
| noiseCompensationEnabled | [in] | int32 | This parameter specifies whether to enable compensation of the channel powers for the inherent noise floor of the signal analyzer. The default value is False.NameValueDescriptionRFMXNR_VAL_ACP_NOISE_COMPENSATION_ENABLED_FALSE0 (0x0)Disables noise compensation.RFMXNR_VAL_ACP_NOISE_COMPENSATION_ENABLED_TRUE1 (0x1)Enables noise compensation.Supported Devices: PXIe-5663/5665/5668R, PXIe-5830/5831/5832/5842/5860 |
| Name | Value | Description |  |
| RFMXNR_VAL_ACP_NOISE_COMPENSATION_ENABLED_FALSE | 0 (0x0) | Disables noise compensation. |  |
| RFMXNR_VAL_ACP_NOISE_COMPENSATION_ENABLED_TRUE | 1 (0x1) | Enables noise compensation.Supported Devices: PXIe-5663/5665/5668R, PXIe-5830/5831/5832/5842/5860 |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ACP

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__configuration__acp_1gae51c20f0608575b4139b3a05715aa1a4.html language=enus -->
## TOPIC 00212: RFmxNR_ACPCfgSweepTime

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__configuration__acp_1gae51c20f0608575b4139b3a05715aa1a4.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__configuration__acp_1gae51c20f0608575b4139b3a05715aa1a4.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the sweep time. Syntaxint32 __stdcall RFmxNR_ACPCfgSweepTime(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 sweepTimeAuto, float64 sweepTimeInterval)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifies the RFmx session refnu

### RFmxNR_ACPCfgSweepTime

Configures the sweep time.

#### Syntax

int32 __stdcall RFmxNR_ACPCfgSweepTime(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 sweepTimeAuto, float64 sweepTimeInterval)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string).Example:"signal::sig1"You can use the RFmxNR_BuildSignalString function to build the selector string. |
| sweepTimeAuto | [in] | int32 | This parameter specifies whether the measurement sets the sweep time. The default value is True.NameValueDescriptionRFMXNR_VAL_ACP_SWEEP_TIME_AUTO_FALSE0 (0x0)The measurement uses the sweep time that you specify in the RFMXNR_ATTR_ACP_SWEEP_TIME_INTERVAL attribute.RFMXNR_VAL_ACP_SWEEP_TIME_AUTO_TRUE1 (0x1)The measurement uses a sweep time of 1 ms. |
| Name | Value | Description |  |
| RFMXNR_VAL_ACP_SWEEP_TIME_AUTO_FALSE | 0 (0x0) | The measurement uses the sweep time that you specify in the RFMXNR_ATTR_ACP_SWEEP_TIME_INTERVAL attribute. |  |
| RFMXNR_VAL_ACP_SWEEP_TIME_AUTO_TRUE | 1 (0x1) | The measurement uses a sweep time of 1 ms. |  |
| sweepTimeInterval | [in] | float64 | This parameter specifies the sweep time when you set the Sweep Time Auto parameter to False. This value is expressed in seconds. The default value is 1 ms. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ACP

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__configuration__chp.html language=enus -->
## TOPIC 00213: CHP

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__configuration__chp.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__configuration__chp.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxNR_CHPCfgAveragingConfigures averaging for the CHP measurement. RFmxNR_CHPCfgRBWFilterConfigures the resolution bandwidth (RBW) filter. RFmxNR_CHPCfgSweepTimeConfigures the sweep time. RFmxNR_CHPValidateNoiseCalibrationDataIndicates whether the CHP noise cal

### CHP

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxNR_CHPCfgAveraging | Configures averaging for the CHP measurement. |
| RFmxNR_CHPCfgRBWFilter | Configures the resolution bandwidth (RBW) filter. |
| RFmxNR_CHPCfgSweepTime | Configures the sweep time. |
| RFmxNR_CHPValidateNoiseCalibrationData | Indicates whether the CHP noise calibration data is valid for the configuration specified by the signal name in the Selector String parameter. |

#### Attachments

None

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__configuration__chp_1ga106a818e61e5cb4cedd4116e951f19cb.html language=enus -->
## TOPIC 00214: RFmxNR_CHPCfgSweepTime

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__configuration__chp_1ga106a818e61e5cb4cedd4116e951f19cb.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__configuration__chp_1ga106a818e61e5cb4cedd4116e951f19cb.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the sweep time. Syntaxint32 __stdcall RFmxNR_CHPCfgSweepTime(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 sweepTimeAuto, float64 sweepTimeInterval)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifies the RFmx session refnu

### RFmxNR_CHPCfgSweepTime

Configures the sweep time.

#### Syntax

int32 __stdcall RFmxNR_CHPCfgSweepTime(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 sweepTimeAuto, float64 sweepTimeInterval)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string).Example:"signal::sig1"You can use the RFmxNR_BuildSignalString function to build the selector string. |
| sweepTimeAuto | [in] | int32 | This parameter specifies whether the measurement sets the sweep time. The default value is True.NameValueDescriptionRFMXNR_VAL_CHP_SWEEP_TIME_AUTO_FALSE0 (0x0)The measurement uses the sweep time that you specify in the RFMXNR_ATTR_CHP_SWEEP_TIME_INTERVAL attribute.RFMXNR_VAL_CHP_SWEEP_TIME_AUTO_TRUE1 (0x1)The measurement uses the sweep time based on the resolution bandwidth. |
| Name | Value | Description |  |
| RFMXNR_VAL_CHP_SWEEP_TIME_AUTO_FALSE | 0 (0x0) | The measurement uses the sweep time that you specify in the RFMXNR_ATTR_CHP_SWEEP_TIME_INTERVAL attribute. |  |
| RFMXNR_VAL_CHP_SWEEP_TIME_AUTO_TRUE | 1 (0x1) | The measurement uses the sweep time based on the resolution bandwidth. |  |
| sweepTimeInterval | [in] | float64 | This parameter specifies the sweep time when you set the Sweep Time Auto parameter to False. This value is expressed in seconds. The default value is 1 ms. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

CHP

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__configuration__chp_1ga230f4cc1e490fbf798b7664facceb5e6.html language=enus -->
## TOPIC 00215: RFmxNR_CHPCfgRBWFilter

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__configuration__chp_1ga230f4cc1e490fbf798b7664facceb5e6.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__configuration__chp_1ga230f4cc1e490fbf798b7664facceb5e6.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the resolution bandwidth (RBW) filter. Syntaxint32 __stdcall RFmxNR_CHPCfgRBWFilter(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 rbwAuto, float64 rbw, int32 rbwFilterType)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifie

### RFmxNR_CHPCfgRBWFilter

Configures the resolution bandwidth (RBW) filter.

#### Syntax

int32 __stdcall RFmxNR_CHPCfgRBWFilter(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 rbwAuto, float64 rbw, int32 rbwFilterType)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string).Example:"signal::sig1"You can use the RFmxNR_BuildSignalString function to build the selector string. |
| rbwAuto | [in] | int32 | This parameter specifies whether the measurement computes the RBW. The default value is True.NameValueDescriptionRFMXNR_VAL_CHP_RBW_FILTER_AUTO_BANDWIDTH_FALSE0 (0x0)The measurement uses the RBW that you specify in the RFMXNR_ATTR_CHP_RBW_FILTER_BANDWIDTH attribute.RFMXNR_VAL_CHP_RBW_FILTER_AUTO_BANDWIDTH_TRUE1 (0x1)The measurement computes the RBW. |
| Name | Value | Description |  |
| RFMXNR_VAL_CHP_RBW_FILTER_AUTO_BANDWIDTH_FALSE | 0 (0x0) | The measurement uses the RBW that you specify in the RFMXNR_ATTR_CHP_RBW_FILTER_BANDWIDTH attribute. |  |
| RFMXNR_VAL_CHP_RBW_FILTER_AUTO_BANDWIDTH_TRUE | 1 (0x1) | The measurement computes the RBW. |  |
| rbw | [in] | float64 | This parameter specifies the bandwidth of the RBW filter, used to sweep the acquired signal, when you set the RBW Auto parameter to False. This value is expressed in Hz. The default value is 30 kHz. |
| rbwFilterType | [in] | int32 | This parameter specifies the shape of the RBW filter. The default value is FFT Based.NameValueDescriptionRFMXNR_VAL_CHP_RBW_FILTER_TYPE_FFT_BASED0 (0x0)No RBW filtering is performed.RFMXNR_VAL_CHP_RBW_FILTER_TYPE_GAUSSIAN1 (0x1)An RBW filter with a Gaussian response is applied.RFMXNR_VAL_CHP_RBW_FILTER_TYPE_FLAT2 (0x2)An RBW filter with a flat response is applied. |
| Name | Value | Description |  |
| RFMXNR_VAL_CHP_RBW_FILTER_TYPE_FFT_BASED | 0 (0x0) | No RBW filtering is performed. |  |
| RFMXNR_VAL_CHP_RBW_FILTER_TYPE_GAUSSIAN | 1 (0x1) | An RBW filter with a Gaussian response is applied. |  |
| RFMXNR_VAL_CHP_RBW_FILTER_TYPE_FLAT | 2 (0x2) | An RBW filter with a flat response is applied. |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

CHP

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__configuration__chp_1ga62abe7fec67160ac98c0fca0527344c2.html language=enus -->
## TOPIC 00216: RFmxNR_CHPValidateNoiseCalibrationData

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__configuration__chp_1ga62abe7fec67160ac98c0fca0527344c2.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__configuration__chp_1ga62abe7fec67160ac98c0fca0527344c2.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates whether the CHP noise calibration data is valid for the configuration specified by the signal name in the Selector String parameter. Syntaxint32 __stdcall RFmxNR_CHPValidateNoiseCalibrationData(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 *noiseCalibrationDataValid)Para

### RFmxNR_CHPValidateNoiseCalibrationData

Indicates whether the CHP noise calibration data is valid for the configuration specified by the signal name in the **Selector String** parameter.

#### Syntax

int32 __stdcall RFmxNR_CHPValidateNoiseCalibrationData(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 *noiseCalibrationDataValid)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string).Example:"signal::sig1"You can use the RFmxNR_BuildSignalString function to build the selector string. |
| noiseCalibrationDataValid | [out] | int32 * | This parameter returns whether the calibration data is valid.Name (Value)DescriptionFalse (0)Returns false if the calibration data is not present for the specified configuration or if the difference between the current device temperature and the calibration temperature exceeds the [-5 °C, 5 °C] range.True (1)Returns true if the calibration data is present for the configuration specified by the signal name in the Selector String parameter. |
| Name (Value) | Description |  |  |
| False (0) | Returns false if the calibration data is not present for the specified configuration or if the difference between the current device temperature and the calibration temperature exceeds the [-5 °C, 5 °C] range. |  |  |
| True (1) | Returns true if the calibration data is present for the configuration specified by the signal name in the Selector String parameter. |  |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

CHP

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__configuration__modacc.html language=enus -->
## TOPIC 00217: ModAcc

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__configuration__modacc.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__configuration__modacc.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxNR_ModAccAutoLevelPerforms the user-configured ModAcc measurement at multiple reference levels relative to the user-configured RFMXNR_ATTR_REFERENCE_LEVEL attribute and configures the reference level corresponding to the lowest RFMXNR_ATTR_MODACC_RESULTS_COM

### ModAcc

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxNR_ModAccAutoLevel | Performs the user-configured ModAcc measurement at multiple reference levels relative to the user-configured RFMXNR_ATTR_REFERENCE_LEVEL attribute and configures the reference level corresponding to the lowest RFMXNR_ATTR_MODACC_RESULTS_COMPOSITE_RMS_EVM_MEAN result. |
| RFmxNR_ModAccCfgMeasurementMode | Configures the measurement mode for the ModAcc measurement. |
| RFmxNR_ModAccCfgNoiseCompensationEnabled | Configures whether to enable EVM noise compensation for the ModAcc measurement. |
| RFmxNR_ModAccCfgReferenceWaveform | Configures the reference waveform for the creation of reference data symbols for EVM computation. |
| RFmxNR_ModAccCfgReferenceWaveformSplit | Configures the reference waveform for the creation of reference data symbols for EVM computation. |
| RFmxNR_ModAccClearNoiseCalibrationDatabase | Clears the noise calibration database used for EVM noise compensation. |
| RFmxNR_ModAccValidateCalibrationData | Specifies whether calibration data is valid for the configuration specified by the signal name in the Selector String parameter. |

#### Attachments

None

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__configuration__modacc_1ga07e95556b4a77896f5d60077e7513fd6.html language=enus -->
## TOPIC 00218: RFmxNR_ModAccCfgReferenceWaveformSplit

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__configuration__modacc_1ga07e95556b4a77896f5d60077e7513fd6.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__configuration__modacc_1ga07e95556b4a77896f5d60077e7513fd6.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the reference waveform for the creation of reference data symbols for EVM computation. Syntaxint32 __stdcall RFmxNR_ModAccCfgReferenceWaveformSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 x0, float64 dx, float32 referenceWaveformI[], float32 referenceWaveformQ[]

### RFmxNR_ModAccCfgReferenceWaveformSplit

Configures the reference waveform for the creation of reference data symbols for EVM computation.

#### Syntax

int32 __stdcall RFmxNR_ModAccCfgReferenceWaveformSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 x0, float64 dx, float32 referenceWaveformI[], float32 referenceWaveformQ[], int32 arraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string).Example:"signal::sig1"You can use the RFmxNR_BuildSignalString function to build the selector string. |
| x0 | [in] | float64 | This parameter specifies the start time, in seconds. |
| dx | [in] | float64 | This parameter specifies the sample duration, in seconds. |
| referenceWaveformI | [in] | float32[] | This parameter Specifies the real part of complex baseband samples, in volts. |
| referenceWaveformQ | [in] | float32[] | This parameter Specifies the imaginary part of complex baseband samples, in volts. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__configuration__modacc_1ga0a8e62edf2e5355cbda7c2d6612eff4a.html language=enus -->
## TOPIC 00219: RFmxNR_ModAccCfgMeasurementMode

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__configuration__modacc_1ga0a8e62edf2e5355cbda7c2d6612eff4a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__configuration__modacc_1ga0a8e62edf2e5355cbda7c2d6612eff4a.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the measurement mode for the ModAcc measurement. Syntaxint32 __stdcall RFmxNR_ModAccCfgMeasurementMode(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 measurementMode)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifies the R

### RFmxNR_ModAccCfgMeasurementMode

Configures the measurement mode for the ModAcc measurement.

#### Syntax

int32 __stdcall RFmxNR_ModAccCfgMeasurementMode(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 measurementMode)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string).Example:"signal::sig1"You can use the RFmxNR_BuildSignalString function to build the selector string. |
| measurementMode | [in] | int32 | This parameter specifies whether the measurement should calibrate the noise floor of the analyzer or perform the ModAcc measurement. The default value is Measure.NameValueDescriptionRFMXNR_VAL_MODACC_MEASUREMENT_MODE_MEASURE0 (0x0)The ModAcc measurement is performed on the acquired signal.RFMXNR_VAL_MODACC_MEASUREMENT_MODE_CALIBRATE_NOISE_FLOOR1 (0x1)The ModAcc measurement measures the noise floor of the instrument across the frequency determined by the carrier frequency and the channel bandwidth. In this mode, the measurement expects the signal generator to be turned off and checks if there is any signal power detected at RFIn port of the analyzer beyond a certain threshold. All scalar results and traces are invalid in this mode. Even if the instrument noise floor is already calibrated, the measurement performs all the required acquisitions and overwrites any pre-existing noise floor calibration data. |
| Name | Value | Description |  |
| RFMXNR_VAL_MODACC_MEASUREMENT_MODE_MEASURE | 0 (0x0) | The ModAcc measurement is performed on the acquired signal. |  |
| RFMXNR_VAL_MODACC_MEASUREMENT_MODE_CALIBRATE_NOISE_FLOOR | 1 (0x1) | The ModAcc measurement measures the noise floor of the instrument across the frequency determined by the carrier frequency and the channel bandwidth. In this mode, the measurement expects the signal generator to be turned off and checks if there is any signal power detected at RFIn port of the analyzer beyond a certain threshold. All scalar results and traces are invalid in this mode. Even if the instrument noise floor is already calibrated, the measurement performs all the required acquisitions and overwrites any pre-existing noise floor calibration data. |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__configuration__pvt_1gaf9b1120f8898a9bf2b4d8857ab10cff5.html language=enus -->
## TOPIC 00220: RFmxNR_PVTCfgAveraging

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__configuration__pvt_1gaf9b1120f8898a9bf2b4d8857ab10cff5.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__configuration__pvt_1gaf9b1120f8898a9bf2b4d8857ab10cff5.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures averaging for the PVT measurement. Syntaxint32 __stdcall RFmxNR_PVTCfgAveraging(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 averagingEnabled, int32 averagingCount, int32 averagingType)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis para

### RFmxNR_PVTCfgAveraging

Configures averaging for the PVT measurement.

#### Syntax

int32 __stdcall RFmxNR_PVTCfgAveraging(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 averagingEnabled, int32 averagingCount, int32 averagingType)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string).Example:"signal::sig1"You can use the RFmxNR_BuildSignalString function to build the selector string. |
| averagingEnabled | [in] | int32 | This parameter specifies whether to enable averaging for the measurement. The default value is False.NameValueDescriptionRFMXNR_VAL_PVT_AVERAGING_ENABLED_FALSE0 (0x0)The measurement is performed on a single acquisition.RFMXNR_VAL_PVT_AVERAGING_ENABLED_TRUE1 (0x1)The measurement uses the value of the RFMXNR_ATTR_PVT_AVERAGING_COUNT attribute as the number of acquisitions over which the PVT measurement is averaged. |
| Name | Value | Description |  |
| RFMXNR_VAL_PVT_AVERAGING_ENABLED_FALSE | 0 (0x0) | The measurement is performed on a single acquisition. |  |
| RFMXNR_VAL_PVT_AVERAGING_ENABLED_TRUE | 1 (0x1) | The measurement uses the value of the RFMXNR_ATTR_PVT_AVERAGING_COUNT attribute as the number of acquisitions over which the PVT measurement is averaged. |  |
| averagingCount | [in] | int32 | This parameter specifies the number of acquisitions used for averaging when you set the Averaging Enabled parameter to True. The default value is 10. |
| averagingType | [in] | int32 | This parameter specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the measurement. The default value is RMS.NameValueDescriptionRFMXNR_VAL_PVT_AVERAGING_TYPE_RMS0 (0x0)The power spectrum is linearly averaged.RFMXNR_VAL_PVT_AVERAGING_TYPE_LOG1 (0x1)The power spectrum is averaged in a logarithmic scale. |
| Name | Value | Description |  |
| RFMXNR_VAL_PVT_AVERAGING_TYPE_RMS | 0 (0x0) | The power spectrum is linearly averaged. |  |
| RFMXNR_VAL_PVT_AVERAGING_TYPE_LOG | 1 (0x1) | The power spectrum is averaged in a logarithmic scale. |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

PVT

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__configuration__selected__ports_1ga5fcd63ff9813fd36b9f344dca4aae37c.html language=enus -->
## TOPIC 00221: RFmxNR_CfgSelectedPortsMultiple

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__configuration__selected__ports_1ga5fcd63ff9813fd36b9f344dca4aae37c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__configuration__selected__ports_1ga5fcd63ff9813fd36b9f344dca4aae37c.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the selected ports to each chain based on the values you set in RFMXNR_ATTR_NUMBER_OF_RECEIVE_CHAINS attribute. Syntaxint32 __stdcall RFmxNR_CfgSelectedPortsMultiple(niRFmxInstrHandle instrumentHandle, char selectorString[], char selectedPorts[])ParametersNameDirectionTypeDescriptioninstr

### RFmxNR_CfgSelectedPortsMultiple

Configures the selected ports to each chain based on the values you set in [RFMXNR_ATTR_NUMBER_OF_RECEIVE_CHAINS](group____root__ni_r_fmx_n_r__attributes_1ga9a4cd858e44d0aa98af4c0999f0de213.html) attribute.

#### Syntax

int32 __stdcall RFmxNR_CfgSelectedPortsMultiple(niRFmxInstrHandle instrumentHandle, char selectorString[], char selectedPorts[])

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function or the RFmxInstr_InitializeFromNIRFSASessionArray function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"""signal::sig1"You can use the RFmxNR_BuildSignalString function to build the selector string. |
| selectedPorts | [in] | char[] | This parameter specifies the list of MIMO ports to be configured. Use "port::<deviceName>/<channelNumber>" as the format for the selected port.For PXIe-5830/5831/5832 devices on a MIMO session, the selected port includes the instrument port in the format "port::<deviceName>/<channelNumber>/<instrPort>".Example:port::myrfsa1/0/if1You can use the RFmxInstr Build Port String function to build the selected port. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Selected Ports

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__configuration__sem_1ga7a6352c923edda7846b478bbcc1d4730.html language=enus -->
## TOPIC 00222: RFmxNR_SEMCfgOffsetFrequency

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__configuration__sem_1ga7a6352c923edda7846b478bbcc1d4730.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__configuration__sem_1ga7a6352c923edda7846b478bbcc1d4730.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the start and stop frequencies and the sideband of an offset segment. Syntaxint32 __stdcall RFmxNR_SEMCfgOffsetFrequency(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 offsetStartFrequency, float64 offsetStopFrequency, int32 offsetSideband)RemarksUse "offset<k>" or "su

### RFmxNR_SEMCfgOffsetFrequency

Configures the start and stop frequencies and the sideband of an offset segment.

#### Syntax

int32 __stdcall RFmxNR_SEMCfgOffsetFrequency(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 offsetStartFrequency, float64 offsetStopFrequency, int32 offsetSideband)

#### Remarks

Use "offset<k>" or "subblock<n>" or "subblock<n>/offset<k>" as the selector string to configure or read this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, subblock number, and offset number. If you do not specify the signal name, the default signal instance is used.Example:"subblock0/offset0""signal::sig1/subblock0/offset0"You can use the RFmxNR_BuildOffsetString function to build the selector string. |
| offsetStartFrequency | [in] | float64 | This parameter specifies the start frequency of an offset segment relative to the component carrier bandwidth edge (single carrier) or subblock aggregated channel bandwidth edge (multi-carrier). This value is expressed in Hz. The default value is 0. |
| offsetStopFrequency | [in] | float64 | This parameter specifies the stop frequency of an offset segment relative to the component carrier bandwidth edge (single carrier) or subblock aggregated channel bandwidth edge (multi-carrier). This value is expressed in Hz. The default value is 1 MHz. |
| offsetSideband | [in] | int32 | This parameter specifies whether the offset segment is present either on one side or on both sides of a carrier. The default value is Both.NameValueDescriptionRFMXNR_VAL_SEM_OFFSET_SIDEBAND_NEGATIVE0 (0x0)Configures a lower offset segment to the left of the leftmost carrier.RFMXNR_VAL_SEM_OFFSET_SIDEBAND_POSITIVE1 (0x1)Configures an upper offset segment to the right of the rightmost carrier.RFMXNR_VAL_SEM_OFFSET_SIDEBAND_BOTH2 (0x2)Configures both the negative and the positive offset segments. |
| Name | Value | Description |  |
| RFMXNR_VAL_SEM_OFFSET_SIDEBAND_NEGATIVE | 0 (0x0) | Configures a lower offset segment to the left of the leftmost carrier. |  |
| RFMXNR_VAL_SEM_OFFSET_SIDEBAND_POSITIVE | 1 (0x1) | Configures an upper offset segment to the right of the rightmost carrier. |  |
| RFMXNR_VAL_SEM_OFFSET_SIDEBAND_BOTH | 2 (0x2) | Configures both the negative and the positive offset segments. |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__configuration__sem_1ga92f572d968e98dc9298488b5df5b4045.html language=enus -->
## TOPIC 00223: RFmxNR_SEMCfgOffsetRelativeLimit

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__configuration__sem_1ga92f572d968e98dc9298488b5df5b4045.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__configuration__sem_1ga92f572d968e98dc9298488b5df5b4045.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the start and stop relative limit of the offset segment. Syntaxint32 __stdcall RFmxNR_SEMCfgOffsetRelativeLimit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 relativeLimitStart, float64 relativeLimitStop)RemarksUse "offset<n>" or "subblock<n>" or "subblock<n>/offset<n

### RFmxNR_SEMCfgOffsetRelativeLimit

Configures the start and stop relative limit of the offset segment.

#### Syntax

int32 __stdcall RFmxNR_SEMCfgOffsetRelativeLimit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 relativeLimitStart, float64 relativeLimitStop)

#### Remarks

Note

This function is considered only when you set the [RFMXNR_ATTR_LINK_DIRECTION](group____root__ni_r_fmx_n_r__attributes_1ga7af3c52ecb58e04851f84033f0b69bcc.html) attribute to **Downlink** and [RFMXNR_ATTR_SEM_DOWNLINK_MASK_TYPE](group____root__ni_r_fmx_n_r__attributes__sem_1ga731315e97fdae8db96e1adaaa5142594.html) attribute to **Custom**.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, subblock number, and offset number. If you do not specify the signal name, the default signal instance is used.Example:"subblock0/offset0""signal::sig1/subblock0/offset0"You can use the RFmxNR_BuildOffsetString function to build the selector string. |
| relativeLimitStart | [in] | float64 | This parameter specifies the relative power limit corresponding to the beginning of the offset segment. This value is expressed in dB. The default value is -53. |
| relativeLimitStop | [in] | float64 | This parameter specifies the relative power limit corresponding to the end of the offset segment. This value is expressed in dB. The default value is -60. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__configuration__sem_1gaa1d88c022bf4822de75a7daeb6fb8068.html language=enus -->
## TOPIC 00224: RFmxNR_SEMCfgComponentCarrierRatedOutputPower

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__configuration__sem_1gaa1d88c022bf4822de75a7daeb6fb8068.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__configuration__sem_1gaa1d88c022bf4822de75a7daeb6fb8068.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the rated output power (P[rated], x) of the component carrier. Syntaxint32 __stdcall RFmxNR_SEMCfgComponentCarrierRatedOutputPower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 componentCarrierRatedOutputPower)RemarksUse "carrier<k>" or "subblock<n>/carrier<k>" as the

### RFmxNR_SEMCfgComponentCarrierRatedOutputPower

Configures the rated output power (P<sub>rated</sub>, x) of the component carrier.

#### Syntax

int32 __stdcall RFmxNR_SEMCfgComponentCarrierRatedOutputPower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 componentCarrierRatedOutputPower)

#### Remarks

Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to configure this function.

Note

This function is valid when you set the [RFMXNR_ATTR_LINK_DIRECTION](group____root__ni_r_fmx_n_r__attributes_1ga7af3c52ecb58e04851f84033f0b69bcc.html) attribute to **Downlink**, [RFMXNR_ATTR_SEM_DOWNLINK_MASK_TYPE](group____root__ni_r_fmx_n_r__attributes__sem_1ga731315e97fdae8db96e1adaaa5142594.html) attribute to **Standard**, and [RFMXNR_ATTR_GNODEB_CATEGORY](group____root__ni_r_fmx_n_r__attributes_1ga6c2b5ba86dc41543a9ddeb12a4dbd943.html) attribute to **Medium Range Base Station**. For more details please refer to section 6.6.4 of *3GPP 38.104* specification.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, subblock number and carrier number. If you do not specify the signal name, the default signal instance is used.Example:"subblock0/carrier0""signal::sig1/subblock0/carrier0"You can use the RFmxNR_BuildCarrierString function to build the selector string. |
| componentCarrierRatedOutputPower | [in] | float64 | This parameter specifies the rated output power (Prated, x), which is used only to choose the limit table for medium range base station, FR2 Category A and FR2 Category B. This value is expressed in dBm. This parameter will be considered when you set the RFMXNR_ATTR_LINK_DIRECTION attribute to Downlink, RFMXNR_ATTR_SEM_DOWNLINK_MASK_TYPE attribute to Standard, and RFMXNR_ATTR_GNODEB_CATEGORY attribute to Medium Range Base Station or FR2 Category A or FR2 Category B. For more details please refer to section 6.6.4 and section 9.7.4 of 3GPP 38.104 specification. The default value is 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__configuration__sem_1gabebb8b15e81ba2147fa6c0d95c4d70b8.html language=enus -->
## TOPIC 00225: RFmxNR_SEMCfgOffsetLimitFailMask

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__configuration__sem_1gabebb8b15e81ba2147fa6c0d95c4d70b8.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__configuration__sem_1gabebb8b15e81ba2147fa6c0d95c4d70b8.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the limit fail mask of the offset segments that specify the criteria to determine the measurement fail status. Syntaxint32 __stdcall RFmxNR_SEMCfgOffsetLimitFailMask(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 limitFailMask)RemarksUse "offset<n>" or "subblock<n>/"offs

### RFmxNR_SEMCfgOffsetLimitFailMask

Configures the limit fail mask of the offset segments that specify the criteria to determine the measurement fail status.

#### Syntax

int32 __stdcall RFmxNR_SEMCfgOffsetLimitFailMask(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 limitFailMask)

#### Remarks

Use "offset<n>" or "subblock<n>/"offset<n>" as the selector string to configure or read this function. 
 
@param [in] instrumentHandle 
@parblock 
This parameter specifies the RFmx session refnum. <b>Instrument Handle In</b> is obtained from the <a href="[https://ni.com/docs/en-US/csh?context=rfmxinstr_rfmxinstrcref_function_initialize](/csh?context=rfmxinstr_rfmxinstrcref_function_initialize)" >RFmxInstr_Initialize</a> function. 
@endparblock 
@param [in] selectorString 
@parblock 
This parameter specifies a <a href="[https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html)" >Selector String</a> comprising of the signal name, subblock number, and offset number. If you do not specify the signal name, the default signal instance is used. 
 
Example: 
 
"subblock0/offset0" 
 
"signal::sig1/subblock0/offset0" 
 
You can use the @ref RFmxNR_BuildOffsetString function to build the selector string. 
@endparblock 
@param [in] limitFailMask 
@parblock 
This parameter specifies the criteria to determine the measurement fail status. The default value is <b>Absolute</b>. 
 
<table class="markdownTable"> 
  <tr class="markdownTableHead">    <th class="markdownTableHeadNone"> Name

Value

Description

RFMXNR_VAL_SEM_OFFSET_LIMIT_FAIL_MASK_ABS_AND_REL

0 (0x0)

Specifies that the measurement fails if the power in the segment exceeds both the absolute and relative masks.

RFMXNR_VAL_SEM_OFFSET_LIMIT_FAIL_MASK_ABS_OR_REL

1 (0x1)

Specifies that the measurement fails if the power in the segment exceeds either the absolute or relative mask.

RFMXNR_VAL_SEM_OFFSET_LIMIT_FAIL_MASK_ABSOLUTE

2 (0x2)

Specifies that the measurement fails if the power in the segment exceeds the absolute mask.

RFMXNR_VAL_SEM_OFFSET_LIMIT_FAIL_MASK_RELATIVE

3 (0x3)

Specifies that the measurement fails if the power in the segment exceeds the relative mask.

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__configuration__sem_1gac4ce8d30aa9ae951c1269165ef504521.html language=enus -->
## TOPIC 00226: RFmxNR_SEMCfgOffsetBandwidthIntegral

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__configuration__sem_1gac4ce8d30aa9ae951c1269165ef504521.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__configuration__sem_1gac4ce8d30aa9ae951c1269165ef504521.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the bandwidth integral of the offset segments. Syntaxint32 __stdcall RFmxNR_SEMCfgOffsetBandwidthIntegral(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 bandwidthIntegral)RemarksUse "offset<k>" or "subblock<n>" or "subblock<n>/offset<k>" as the selector string to configu

### RFmxNR_SEMCfgOffsetBandwidthIntegral

Configures the bandwidth integral of the offset segments.

#### Syntax

int32 __stdcall RFmxNR_SEMCfgOffsetBandwidthIntegral(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 bandwidthIntegral)

#### Remarks

Use "offset<k>" or "subblock<n>" or "subblock<n>/offset<k>" as the selector string to configure or read this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, subblock number, carrier number, and offset number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"subblock0/offset0""signal::sig1/subblock0/offset0""signal::sig1/result::r1/subblock0/offset0""result::r1/subblock0/offset0"You can use the RFmxNR_BuildOffsetString function to build the selector string. |
| bandwidthIntegral | [in] | int32 | This parameter specifies the resolution of a spectrum to compare with the spectral mask limits as an integer multiple of the RBW. When you set this parameter to a value greater than 1, the measurement acquires the spectrum with a narrow resolution and then processes it digitally to get a wider resolution that is equal to the product of a bandwidth integral and a RBW. The default value is 1. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__configuration__sem_1gacf3470535092bdc522528fe28aaabc9d.html language=enus -->
## TOPIC 00227: RFmxNR_SEMCfgAveraging

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__configuration__sem_1gacf3470535092bdc522528fe28aaabc9d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__configuration__sem_1gacf3470535092bdc522528fe28aaabc9d.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures averaging for the SEM measurement. Syntaxint32 __stdcall RFmxNR_SEMCfgAveraging(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 averagingEnabled, int32 averagingCount, int32 averagingType)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis para

### RFmxNR_SEMCfgAveraging

Configures averaging for the SEM measurement.

#### Syntax

int32 __stdcall RFmxNR_SEMCfgAveraging(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 averagingEnabled, int32 averagingCount, int32 averagingType)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string).Example:"signal::sig1"You can use the RFmxNR_BuildSignalString function to build the selector string. |
| averagingEnabled | [in] | int32 | This parameter specifies whether to enable averaging for the measurement. The default value is False.NameValueDescriptionRFMXNR_VAL_SEM_AVERAGING_ENABLED_FALSE0 (0x0)The measurement is performed on a single acquisition.RFMXNR_VAL_SEM_AVERAGING_ENABLED_TRUE1 (0x1)The SEM measurement uses the value of the RFMXNR_ATTR_SEM_AVERAGING_COUNT attribute as the number of acquisitions over which the SEM measurement is averaged. |
| Name | Value | Description |  |
| RFMXNR_VAL_SEM_AVERAGING_ENABLED_FALSE | 0 (0x0) | The measurement is performed on a single acquisition. |  |
| RFMXNR_VAL_SEM_AVERAGING_ENABLED_TRUE | 1 (0x1) | The SEM measurement uses the value of the RFMXNR_ATTR_SEM_AVERAGING_COUNT attribute as the number of acquisitions over which the SEM measurement is averaged. |  |
| averagingCount | [in] | int32 | This parameter specifies the number of acquisitions used for averaging when you set the Averaging Enabled parameter to True. The default value is 10. |
| averagingType | [in] | int32 | This parameter specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the measurement. The default value is RMS.NameValueDescriptionRFMXNR_VAL_SEM_AVERAGING_TYPE_RMS0 (0x0)The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor.RFMXNR_VAL_SEM_AVERAGING_TYPE_LOG1 (0x1)The power spectrum is averaged in a logarithmic scale.RFMXNR_VAL_SEM_AVERAGING_TYPE_SCALAR2 (0x2)The square root of the power spectrum is averaged.RFMXNR_VAL_SEM_AVERAGING_TYPE_MAXIMUM3 (0x3)The peak power in the spectrum at each frequency bin is retained from one acquisition to the next.RFMXNR_VAL_SEM_AVERAGING_TYPE_MINIMUM4 (0x4)The lowest power in the spectrum at each frequency bin is retained from one acquisition to the next. |
| Name | Value | Description |  |
| RFMXNR_VAL_SEM_AVERAGING_TYPE_RMS | 0 (0x0) | The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. |  |
| RFMXNR_VAL_SEM_AVERAGING_TYPE_LOG | 1 (0x1) | The power spectrum is averaged in a logarithmic scale. |  |
| RFMXNR_VAL_SEM_AVERAGING_TYPE_SCALAR | 2 (0x2) | The square root of the power spectrum is averaged. |  |
| RFMXNR_VAL_SEM_AVERAGING_TYPE_MAXIMUM | 3 (0x3) | The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. |  |
| RFMXNR_VAL_SEM_AVERAGING_TYPE_MINIMUM | 4 (0x4) | The lowest power in the spectrum at each frequency bin is retained from one acquisition to the next. |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__configuration__sem__array.html language=enus -->
## TOPIC 00228: Array

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__configuration__sem__array.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__configuration__sem__array.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxNR_SEMCfgComponentCarrierRatedOutputPowerArrayConfigures an array of the rated output power (P[rated], x) of the component carrier. RFmxNR_SEMCfgOffsetAbsoluteLimitArrayConfigures an array of the start limit and the stop limit of the offset segments. RFmxNR_

### Array

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxNR_SEMCfgComponentCarrierRatedOutputPowerArray | Configures an array of the rated output power (Prated, x) of the component carrier. |
| RFmxNR_SEMCfgOffsetAbsoluteLimitArray | Configures an array of the start limit and the stop limit of the offset segments. |
| RFmxNR_SEMCfgOffsetBandwidthIntegralArray | Configures an array of the bandwidth integral of the offset segments. |
| RFmxNR_SEMCfgOffsetFrequencyArray | Configures an array of the start and stop frequencies and the sideband of an offset segment. |
| RFmxNR_SEMCfgOffsetLimitFailMaskArray | Configures an array of the limit fail mask of the offset segments that specifies the criteria to determine the measurement fail status. |
| RFmxNR_SEMCfgOffsetRBWFilterArray | Configures the offset RBW and the offset RBW filter type array. |
| RFmxNR_SEMCfgOffsetRelativeLimitArray | Configures an array of the start and stop relative limit of the offset segment. |

#### Attachments

None

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__configuration__sem__array_1ga2d67566a475f5347d0347bbe85f092f0.html language=enus -->
## TOPIC 00229: RFmxNR_SEMCfgOffsetAbsoluteLimitArray

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__configuration__sem__array_1ga2d67566a475f5347d0347bbe85f092f0.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__configuration__sem__array_1ga2d67566a475f5347d0347bbe85f092f0.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures an array of the start limit and the stop limit of the offset segments. Syntaxint32 __stdcall RFmxNR_SEMCfgOffsetAbsoluteLimitArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 absoluteLimitStart[], float64 absoluteLimitStop[], int32 numberOfElements)RemarksUse "subbl

### RFmxNR_SEMCfgOffsetAbsoluteLimitArray

Configures an array of the start limit and the stop limit of the offset segments.

#### Syntax

int32 __stdcall RFmxNR_SEMCfgOffsetAbsoluteLimitArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 absoluteLimitStart[], float64 absoluteLimitStop[], int32 numberOfElements)

#### Remarks

Use "subblock<n>" as the selector string to configure this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and the subblock number. If you do not specify the signal name, the default signal instance is used. The default value is "subblock0".Example:"subblock0""signal::sig1/subblock0"You can use the RFmxNR_BuildSignalString function to build the selector string. |
| absoluteLimitStart | [in] | float64[] | This parameter specifies an array of the absolute power limit corresponding to the beginning of an offset segment. This value is expressed in dBm. The default value is -21. |
| absoluteLimitStop | [in] | float64[] | This parameter specifies an array of the absolute power limit corresponding to the end of an offset segment. This value is expressed in dBm. The default value is -21. |
| numberOfElements | [in] | int32 | Specifies the number of elements in each array. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Array

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__configuration__sem__array_1gab1e3d81801f38cdad9c7d9707d0a8e2e.html language=enus -->
## TOPIC 00230: RFmxNR_SEMCfgComponentCarrierRatedOutputPowerArray

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__configuration__sem__array_1gab1e3d81801f38cdad9c7d9707d0a8e2e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__configuration__sem__array_1gab1e3d81801f38cdad9c7d9707d0a8e2e.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures an array of the rated output power (P[rated], x) of the component carrier. Syntaxint32 __stdcall RFmxNR_SEMCfgComponentCarrierRatedOutputPowerArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 componentCarrierRatedOutputPower[], int32 numberOfElements)RemarksUse "sub

### RFmxNR_SEMCfgComponentCarrierRatedOutputPowerArray

Configures an array of the rated output power (P<sub>rated</sub>, x) of the component carrier.

#### Syntax

int32 __stdcall RFmxNR_SEMCfgComponentCarrierRatedOutputPowerArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 componentCarrierRatedOutputPower[], int32 numberOfElements)

#### Remarks

Use "subblock<n>" as the selector string to read results from this function.

Note

This function is valid when you set the [RFMXNR_ATTR_LINK_DIRECTION](group____root__ni_r_fmx_n_r__attributes_1ga7af3c52ecb58e04851f84033f0b69bcc.html) attribute to **Downlink**, [RFMXNR_ATTR_SEM_DOWNLINK_MASK_TYPE](group____root__ni_r_fmx_n_r__attributes__sem_1ga731315e97fdae8db96e1adaaa5142594.html) attribute to **Standard**, and [RFMXNR_ATTR_GNODEB_CATEGORY](group____root__ni_r_fmx_n_r__attributes_1ga6c2b5ba86dc41543a9ddeb12a4dbd943.html) attribute to **Medium Range Base Station**. For more details please refer to section 6.6.4 of *3GPP 38.104* specification.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and the subblock number. If you do not specify the signal name, the default signal instance is used. The default value is "subblock0".Example:"subblock0""signal::sig1/subblock0"You can use the RFmxNR_BuildSignalString function to build the selector string. |
| componentCarrierRatedOutputPower | [in] | float64[] | This parameter specifies an array of the rated output power (Prated, x), which is used only to choose the limit table for medium range base station, FR2 Category A and FR2 Category B. This value is expressed in dBm. This parameter will be considered when you set the RFMXNR_ATTR_LINK_DIRECTION attribute to Downlink, RFMXNR_ATTR_SEM_DOWNLINK_MASK_TYPE attribute to Standard, and RFMXNR_ATTR_GNODEB_CATEGORY attribute to Medium Range Base Station or FR2 Category A or FR2 Category B. For more details please refer to section 6.6.4 of 3GPP 38.104 specification. The default value is 0. |
| numberOfElements | [in] | int32 | Specifies the number of elements in each array. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Array

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__configuration__trigger.html language=enus -->
## TOPIC 00231: Trigger

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__configuration__trigger.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__configuration__trigger.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxNR_CfgDigitalEdgeTriggerConfigures the device to wait for a digital edge trigger and then marks a reference point within the record. RFmxNR_CfgIQPowerEdgeTriggerConfigures the device to wait for the complex power of the I/Q data to cross the specified thresh

### Trigger

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxNR_CfgDigitalEdgeTrigger | Configures the device to wait for a digital edge trigger and then marks a reference point within the record. |
| RFmxNR_CfgIQPowerEdgeTrigger | Configures the device to wait for the complex power of the I/Q data to cross the specified threshold and then marks a reference point within the record. |
| RFmxNR_CfgSoftwareEdgeTrigger | Configures the device to wait for a software trigger and then marks a reference point within the record. |
| RFmxNR_DisableTrigger | Configures the device to not wait for a trigger to mark a reference point within a record. This function defines the signal triggering as immediate. |

#### Attachments

None

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__configuration__trigger_1ga8cbdfcdd3ac787e8f1f672941e0e8b20.html language=enus -->
## TOPIC 00232: RFmxNR_CfgSoftwareEdgeTrigger

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__configuration__trigger_1ga8cbdfcdd3ac787e8f1f672941e0e8b20.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__configuration__trigger_1ga8cbdfcdd3ac787e8f1f672941e0e8b20.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the device to wait for a software trigger and then marks a reference point within the record. Syntaxint32 __stdcall RFmxNR_CfgSoftwareEdgeTrigger(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 triggerDelay, int32 enableTrigger)ParametersNameDirectionTypeDescriptioninst

### RFmxNR_CfgSoftwareEdgeTrigger

Configures the device to wait for a software trigger and then marks a reference point within the record.

#### Syntax

int32 __stdcall RFmxNR_CfgSoftwareEdgeTrigger(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 triggerDelay, int32 enableTrigger)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string).Example:"signal::sig1"You can use the RFmxNR_BuildSignalString function to build the selector string. |
| triggerDelay | [in] | float64 | This parameter specifies the trigger delay time. This value is expressed in seconds. If the delay is negative, the measurement acquires pretrigger samples. If the delay is positive, the measurement acquires post-trigger samples. The default value is 0. |
| enableTrigger | [in] | int32 | This parameter specifies whether to enable the trigger. The default value is TRUE. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Trigger

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__fetch.html language=enus -->
## TOPIC 00233: Fetch

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__fetch.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__fetch.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsACPCHPModAccOBWPVTSEMTXPGroup membersNoneAttachmentsNone

### Fetch

#### Groups

- ACP
- CHP
- ModAcc
- OBW
- PVT
- SEM
- TXP

#### Group members

None

#### Attachments

None

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__fetch__acp.html language=enus -->
## TOPIC 00234: ACP

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__fetch__acp.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__fetch__acp.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxNR_ACPFetchAbsolutePowersTraceFetches the absolute powers trace for ACP measurement. RFmxNR_ACPFetchComponentCarrierMeasurementReturns the absolute and relative powers measured in the component carriers. RFmxNR_ACPFetchComponentCarrierMeasurementArrayReturns

### ACP

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxNR_ACPFetchAbsolutePowersTrace | Fetches the absolute powers trace for ACP measurement. |
| RFmxNR_ACPFetchComponentCarrierMeasurement | Returns the absolute and relative powers measured in the component carriers. |
| RFmxNR_ACPFetchComponentCarrierMeasurementArray | Returns an array of the absolute and relative powers measured in the component carriers. |
| RFmxNR_ACPFetchOffsetMeasurement | Returns the absolute and relative power of the lower and upper offset channel. The relative power is relative to subblock power. |
| RFmxNR_ACPFetchOffsetMeasurementArray | Returns an array of the absolute and relative power of the lower and upper offset channel. |
| RFmxNR_ACPFetchRelativePowersTrace | Fetches the relative powers trace for ACP measurement. |
| RFmxNR_ACPFetchSpectrum | Fetches the spectrum used for ACP measurements. |
| RFmxNR_ACPFetchSubblockMeasurement | Fetches the power, integration bandwidth, and center frequency of the subblock. |
| RFmxNR_ACPFetchTotalAggregatedPower | Returns the sum of powers in all the subblocks. |

#### Attachments

None

Parent topic:

Fetch

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__fetch__acp_1ga0452afb1b40405e9a8bcf2452cdf5024.html language=enus -->
## TOPIC 00235: RFmxNR_ACPFetchTotalAggregatedPower

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__fetch__acp_1ga0452afb1b40405e9a8bcf2452cdf5024.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__fetch__acp_1ga0452afb1b40405e9a8bcf2452cdf5024.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the sum of powers in all the subblocks. Syntaxint32 __stdcall RFmxNR_ACPFetchTotalAggregatedPower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *totalAggregatedPower)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis paramete

### RFmxNR_ACPFetchTotalAggregatedPower

Returns the sum of powers in all the subblocks.

#### Syntax

int32 __stdcall RFmxNR_ACPFetchTotalAggregatedPower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *totalAggregatedPower)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default is "" (empty string).Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxNR_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| totalAggregatedPower | [out] | float64 * | This parameter returns the total power of all the subblocks. The power in each subblock is the sum of powers of all the frequency bins over the integration bandwidth of the subblocks. This value includes the power in the inter-carrier gaps within a subblock, but it does not include the power within the subblock gaps. The carrier power is reported in dBm when you set the RFMXNR_ATTR_ACP_POWER_UNITS attribute to dBm, and in dBm/Hz when you set the ACP Pwr Units attribute to dBm/Hz. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ACP

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__fetch__acp_1ga1c827d3a9179aa144fa90f9a7cfd9d5d.html language=enus -->
## TOPIC 00236: RFmxNR_ACPFetchOffsetMeasurement

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__fetch__acp_1ga1c827d3a9179aa144fa90f9a7cfd9d5d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__fetch__acp_1ga1c827d3a9179aa144fa90f9a7cfd9d5d.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the absolute and relative power of the lower and upper offset channel. The relative power is relative to subblock power. Syntaxint32 __stdcall RFmxNR_ACPFetchOffsetMeasurement(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *lowerRelativePower, float64 *up

### RFmxNR_ACPFetchOffsetMeasurement

Returns the absolute and relative power of the lower and upper offset channel. The relative power is relative to subblock power.

#### Syntax

int32 __stdcall RFmxNR_ACPFetchOffsetMeasurement(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *lowerRelativePower, float64 *upperRelativePower, float64 *lowerAbsolutePower, float64 *upperAbsolutePower)

#### Remarks

Use "offset<k>" or "subblock<n>" or "subblock<n>/offset<k>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, subblock number, carrier number, and offset number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"subblock0/offset0""signal::sig1/subblock0/offset0""signal::sig1/result::r1/subblock0/offset0""result::r1/subblock0/offset0"You can use the RFmxNR_BuildOffsetString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| lowerRelativePower | [out] | float64 * | This parameter returns the power in lower (negative) offset channel relative to the total aggregated power. This value is expressed in dB. |
| upperRelativePower | [out] | float64 * | This parameter returns the power in the upper (positive) offset channel relative to the total aggregated power. This value is expressed in dB. |
| lowerAbsolutePower | [out] | float64 * | This parameter returns the lower offset channel power. The carrier power is reported in dBm when you set the RFMXNR_ATTR_ACP_POWER_UNITS attribute to dBm, and in dBm/Hz when you set the ACP Pwr Units attribute to dBm/Hz. |
| upperAbsolutePower | [out] | float64 * | This parameter returns the upper offset channel power. The carrier power is reported in dBm when you set the RFMXNR_ATTR_ACP_POWER_UNITS attribute to dBm, and in dBm/Hz when you set the ACP Pwr Units attribute to dBm/Hz. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ACP

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__fetch__acp_1ga77e96ad8f5cbb0ec0c68ae9f7fc7ba6b.html language=enus -->
## TOPIC 00237: RFmxNR_ACPFetchRelativePowersTrace

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__fetch__acp_1ga77e96ad8f5cbb0ec0c68ae9f7fc7ba6b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__fetch__acp_1ga77e96ad8f5cbb0ec0c68ae9f7fc7ba6b.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the relative powers trace for ACP measurement. Syntaxint32 __stdcall RFmxNR_ACPFetchRelativePowersTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 traceIndex, float64 *x0, float64 *dx, float32 relativePowersTrace[], int32 arraySize, int32 *actualArraySi

### RFmxNR_ACPFetchRelativePowersTrace

Fetches the relative powers trace for ACP measurement.

#### Syntax

int32 __stdcall RFmxNR_ACPFetchRelativePowersTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 traceIndex, float64 *x0, float64 *dx, float32 relativePowersTrace[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default is "" (empty string).Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxNR_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| traceIndex | [in] | int32 | Specifies the index of the trace to fetch. The traceIndex can range from 0 to (Number of carriers + 2*Number of offsets). |
| x0 | [out] | float64 * | This parameter returns the start frequency of the channel. This value is expressed in Hz. |
| dx | [out] | float64 * | This parameter returns the frequency bin spacing. This value is expressed in Hz. |
| relativePowersTrace | [out] | float32[] | This parameter returns an array of the relative power measured in each channel relative to total aggregated power. This value is expressed in dB. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ACP

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__fetch__acp_1gaaf317064d3294acefa96298dad102682.html language=enus -->
## TOPIC 00238: RFmxNR_ACPFetchSubblockMeasurement

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__fetch__acp_1gaaf317064d3294acefa96298dad102682.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__fetch__acp_1gaaf317064d3294acefa96298dad102682.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the power, integration bandwidth, and center frequency of the subblock. Syntaxint32 __stdcall RFmxNR_ACPFetchSubblockMeasurement(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *subblockPower, float64 *integrationBandwidth, float64 *frequency)ParametersNam

### RFmxNR_ACPFetchSubblockMeasurement

Fetches the power, integration bandwidth, and center frequency of the subblock.

#### Syntax

int32 __stdcall RFmxNR_ACPFetchSubblockMeasurement(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *subblockPower, float64 *integrationBandwidth, float64 *frequency)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, and subblock number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0".Example:"subblock0""signal::sig1/subblock0""result::r1/subblock0""signal::sig1/result::r1/subblock0"You can use the RFmxNR_BuildSubblockString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| subblockPower | [out] | float64 * | This parameter returns the sum of powers of all the frequency bins over the integration bandwidth of the subblock. This includes the power in inter-carrier gaps within a subblock. The carrier power is reported in dBm when you set the RFMXNR_ATTR_ACP_POWER_UNITS attribute to dBm, and in dBm/Hz when you set the ACP Pwr Units attribute to dBm/Hz. |
| integrationBandwidth | [out] | float64 * | This parameter returns the integration bandwidth used in calculating the power of the subblock. Integration bandwidth is the span from left edge of the leftmost carrier to the right edge of the rightmost carrier within a subblock. This value is expressed in Hz. |
| frequency | [out] | float64 * | This parameter returns the absolute center frequency of the subblock. This value is the center of the subblock integration bandwidth. This value is expressed in Hz. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ACP

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__fetch__acp_1gab4cfa72611ae9185ae142e90969e4f98.html language=enus -->
## TOPIC 00239: RFmxNR_ACPFetchSpectrum

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__fetch__acp_1gab4cfa72611ae9185ae142e90969e4f98.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__fetch__acp_1gab4cfa72611ae9185ae142e90969e4f98.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the spectrum used for ACP measurements. Syntaxint32 __stdcall RFmxNR_ACPFetchSpectrum(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 spectrum[], int32 arraySize, int32 *actualArraySize)ParametersNameDirectionTypeDescriptioninstru

### RFmxNR_ACPFetchSpectrum

Fetches the spectrum used for ACP measurements.

#### Syntax

int32 __stdcall RFmxNR_ACPFetchSpectrum(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 spectrum[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default is "" (empty string).Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxNR_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| x0 | [out] | float64 * | This parameter returns the start frequency of the channel. This value is expressed in Hz. |
| dx | [out] | float64 * | This parameter returns the frequency bin spacing. This value is expressed in Hz. |
| spectrum | [out] | float32[] | This parameter returns the array of averaged power measured at each frequency bin. The carrier power is reported in dBm when you set the RFMXNR_ATTR_ACP_POWER_UNITS attribute to dBm, and in dBm/Hz when you set the ACP Pwr Units attribute to dBm/Hz. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ACP

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__fetch__acp_1gacbd00678027ec774a3eaf0036b345b1a.html language=enus -->
## TOPIC 00240: RFmxNR_ACPFetchAbsolutePowersTrace

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__fetch__acp_1gacbd00678027ec774a3eaf0036b345b1a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__fetch__acp_1gacbd00678027ec774a3eaf0036b345b1a.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the absolute powers trace for ACP measurement. Syntaxint32 __stdcall RFmxNR_ACPFetchAbsolutePowersTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 traceIndex, float64 *x0, float64 *dx, float32 absolutePowersTrace[], int32 arraySize, int32 *actualArraySi

### RFmxNR_ACPFetchAbsolutePowersTrace

Fetches the absolute powers trace for ACP measurement.

#### Syntax

int32 __stdcall RFmxNR_ACPFetchAbsolutePowersTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 traceIndex, float64 *x0, float64 *dx, float32 absolutePowersTrace[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default is "" (empty string).Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxNR_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| traceIndex | [in] | int32 | Specifies the index of the trace to fetch. The traceIndex can range from 0 to (Number of carriers + 2*Number of offsets). |
| x0 | [out] | float64 * | This parameter returns the start frequency of the channel. This value is expressed in Hz. |
| dx | [out] | float64 * | This parameter returns the frequency bin spacing. This value is expressed in Hz. |
| absolutePowersTrace | [out] | float32[] | This parameter returns an array the power measured in each channel. The carrier power is reported in dBm when you set the RFMXNR_ATTR_ACP_POWER_UNITS attribute to dBm, and in dBm/Hz when you set the ACP Pwr Units attribute to dBm/Hz. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ACP

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__fetch__acp_1gafc9fc47696b034c9726d260b90f54da5.html language=enus -->
## TOPIC 00241: RFmxNR_ACPFetchComponentCarrierMeasurementArray

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__fetch__acp_1gafc9fc47696b034c9726d260b90f54da5.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__fetch__acp_1gafc9fc47696b034c9726d260b90f54da5.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns an array of the absolute and relative powers measured in the component carriers. Syntaxint32 __stdcall RFmxNR_ACPFetchComponentCarrierMeasurementArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 absolutePower[], float64 relativePower[], int32 arraySize

### RFmxNR_ACPFetchComponentCarrierMeasurementArray

Returns an array of the absolute and relative powers measured in the component carriers.

#### Syntax

int32 __stdcall RFmxNR_ACPFetchComponentCarrierMeasurementArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 absolutePower[], float64 relativePower[], int32 arraySize, int32 *actualArraySize)

#### Remarks

Use "subblock<n>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, and subblock number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"subblock0""signal::sig1/subblock0""result::r1/subblock0""signal::sig1/result::r1/subblock0"You can use the RFmxNR_BuildSubblockString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| absolutePower | [out] | float64[] | This parameter returns an array of the power measured over the integration bandwidth of the component carrier. This value is expressed in dBm. The carrier power is reported in dBm when you set the RFMXNR_ATTR_ACP_POWER_UNITS attribute to dBm, and in dBm/Hz when you set the ACP Pwr Units attribute to dBm/Hz. |
| relativePower | [out] | float64[] | This parameter returns an array of the component carrier power relative to its subblock power. This value is expressed in dB. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ACP

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__fetch__chp.html language=enus -->
## TOPIC 00242: CHP

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__fetch__chp.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__fetch__chp.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxNR_CHPFetchComponentCarrierMeasurementReturns the absolute and relative powers measured in the component carriers. RFmxNR_CHPFetchComponentCarrierMeasurementArrayReturns an array of the absolute and relative powers measured in the component carriers. RFmxNR_

### CHP

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxNR_CHPFetchComponentCarrierMeasurement | Returns the absolute and relative powers measured in the component carriers. |
| RFmxNR_CHPFetchComponentCarrierMeasurementArray | Returns an array of the absolute and relative powers measured in the component carriers. |
| RFmxNR_CHPFetchSpectrum | Fetches the spectrum used for CHP measurements. |
| RFmxNR_CHPFetchSubblockPower | Returns the power of subblock. |
| RFmxNR_CHPFetchTotalAggregatedPower | Returns the sum of powers in all the subblocks. |

#### Attachments

None

Parent topic:

Fetch

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__fetch__chp_1gae2fb17b6671191f49e1cc2243b0cf3dc.html language=enus -->
## TOPIC 00243: RFmxNR_CHPFetchTotalAggregatedPower

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__fetch__chp_1gae2fb17b6671191f49e1cc2243b0cf3dc.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__fetch__chp_1gae2fb17b6671191f49e1cc2243b0cf3dc.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the sum of powers in all the subblocks. Syntaxint32 __stdcall RFmxNR_CHPFetchTotalAggregatedPower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *totalAggregatedPower)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis paramete

### RFmxNR_CHPFetchTotalAggregatedPower

Returns the sum of powers in all the subblocks.

#### Syntax

int32 __stdcall RFmxNR_CHPFetchTotalAggregatedPower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *totalAggregatedPower)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default is "" (empty string).Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxNR_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| totalAggregatedPower | [out] | float64 * | This parameter returns the total power of all the subblocks. The power in each subblock is the sum of powers of all the frequency bins over the integration bandwidth of the subblocks. This value includes the power in the inter-carrier gaps within a subblock, but it does not include the power within the subblock gaps. This value is expressed in dBm. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

CHP

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__fetch__modacc_1ga026a967fd053bb9df6ff66a823d0cae7.html language=enus -->
## TOPIC 00244: RFmxNR_ModAccFetchPDSCH256QAMConstellationTrace

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__fetch__modacc_1ga026a967fd053bb9df6ff66a823d0cae7.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__fetch__modacc_1ga026a967fd053bb9df6ff66a823d0cae7.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches PDSCH 256 QAM trace. Syntaxint32 __stdcall RFmxNR_ModAccFetchPDSCH256QAMConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle qam256Constellation[], int32 arraySize, int32 *actualArraySize)RemarksUse "carrier<k>" or "subblock<n>" or "s

### RFmxNR_ModAccFetchPDSCH256QAMConstellationTrace

Fetches PDSCH 256 QAM trace.

#### Syntax

int32 __stdcall RFmxNR_ModAccFetchPDSCH256QAMConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle qam256Constellation[], int32 arraySize, int32 *actualArraySize)

#### Remarks

Use "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0".Example:"subblock0/carrier0""signal::sig1/subblock0/carrier0""result::r1/subblock0/carrier0""signal::sig1/result::r1/subblock0/carrier0"You can use the RFmxNR_BuildCarrierString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| qam256Constellation | [out] | NIComplexSingle[] | This parameter returns the 256 QAM constellation trace. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__fetch__modacc_1ga298bad93979701840f8d50cd52b4a67d.html language=enus -->
## TOPIC 00245: RFmxNR_ModAccFetchSpectralFlatnessTrace

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__fetch__modacc_1ga298bad93979701840f8d50cd52b4a67d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__fetch__modacc_1ga298bad93979701840f8d50cd52b4a67d.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the spectral flatness, upper mask, and lower mask traces. Spectral flatness is the magnitude of equalizer coefficients at each allocated subcarrier. Lower and upper masks are derived from section 6.5.2.4.5 of 3GPP TS 38.521-1 specification. Syntaxint32 __stdcall RFmxNR_ModAccFetchSpectralFla

### RFmxNR_ModAccFetchSpectralFlatnessTrace

Returns the spectral flatness, upper mask, and lower mask traces. Spectral flatness is the magnitude of equalizer coefficients at each allocated subcarrier. Lower and upper masks are derived from section 6.5.2.4.5 of *3GPP TS 38.521-1* specification.

#### Syntax

int32 __stdcall RFmxNR_ModAccFetchSpectralFlatnessTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 spectralFlatness[], float32 spectralFlatnessLowerMask[], float32 spectralFlatnessUpperMask[], int32 arraySize, int32 *actualArraySize)

#### Remarks

Use "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>" or "subblock<n>/carrier<k>/layer<<i>q</i>>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, subblock number, carrier number and layer number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0/layer0".Example:"subblock0/carrier0/layer0""signal::sig1/subblock0/carrier0/layer0""result::r1/subblock0/carrier0/layer0""signal::sig1/result::r1/subblock0/carrier0/layer0"You can use the RFmxNR_BuildCarrierString and RFmxNR_BuildLayerString functions to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| x0 | [out] | float64 * | This parameter returns the start point of the of the resource block. |
| dx | [out] | float64 * | This parameter returns the subcarrier spacing. |
| spectralFlatness | [out] | float32[] | This parameter returns an array of the spectral flatness values at each allocated subcarrier. |
| spectralFlatnessLowerMask | [out] | float32[] | This parameter returns an array of the spectral flatness values at each allocated subcarrier. |
| spectralFlatnessUpperMask | [out] | float32[] | This parameter returns an array of the spectral flatness values at each allocated subcarrier. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__fetch__modacc_1ga4e5b2f6a1585f9bc171ae087e8cbc792.html language=enus -->
## TOPIC 00246: RFmxNR_ModAccFetchPDSCH1024QAMConstellationTrace

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__fetch__modacc_1ga4e5b2f6a1585f9bc171ae087e8cbc792.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__fetch__modacc_1ga4e5b2f6a1585f9bc171ae087e8cbc792.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the PDSCH 1024 QAM constellation trace. Syntaxint32 __stdcall RFmxNR_ModAccFetchPDSCH1024QAMConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle qam1024Constellation[], int32 arraySize, int32 *actualArraySize)RemarksUse "carrier<k>" o

### RFmxNR_ModAccFetchPDSCH1024QAMConstellationTrace

Fetches the PDSCH 1024 QAM constellation trace.

#### Syntax

int32 __stdcall RFmxNR_ModAccFetchPDSCH1024QAMConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle qam1024Constellation[], int32 arraySize, int32 *actualArraySize)

#### Remarks

Use "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0".Example:"subblock0/carrier0""signal::sig1/subblock0/carrier0""result::r1/subblock0/carrier0""signal::sig1/result::r1/subblock0/carrier0"You can use the RFmxNR_BuildCarrierString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| qam1024Constellation | [out] | NIComplexSingle[] | This parameter returns the 1024 QAM constellation trace. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__fetch__modacc_1ga5c39dd65479aec3de62a94def89120dc.html language=enus -->
## TOPIC 00247: RFmxNR_ModAccFetchPUSCHPTRSConstellationTraceSplit

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__fetch__modacc_1ga5c39dd65479aec3de62a94def89120dc.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__fetch__modacc_1ga5c39dd65479aec3de62a94def89120dc.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches PUSCH PTRS trace. The constellation points of different slots in the measurement length is concatenated. Syntaxint32 __stdcall RFmxNR_ModAccFetchPUSCHPTRSConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 puschPTRSConstellationI[], flo

### RFmxNR_ModAccFetchPUSCHPTRSConstellationTraceSplit

Fetches PUSCH PTRS trace. The constellation points of different slots in the measurement length is concatenated.

#### Syntax

int32 __stdcall RFmxNR_ModAccFetchPUSCHPTRSConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 puschPTRSConstellationI[], float32 puschPTRSConstellationQ[], int32 arraySize, int32 *actualArraySize)

#### Remarks

Use "user<k>" or "carrier<<i>l</i>>" or "subblock<n>" or "subblock<n>/carrier<<i>l</i>>/user<k>" or "subblock<n>/carrier<k>/user<k>/layer<<i>q</i>>" as the selector string to read this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, subblock number, user number and layer number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0/user0/layer0".Example:"subblock0/carrier0/user0/layer0""signal::sig1/subblock0/carrier0/user0/layer0""result::r1/subblock0/carrier0/user0/layer0""signal::sig1/result::r1/subblock0/carrier0/user0/layer0"You can use the RFmxNR_BuildUserString and RFmxNR_BuildLayerString functions to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| puschPTRSConstellationI | [out] | float32[] | This parameter Returns the real part of PUSCH PTRS constellation trace. |
| puschPTRSConstellationQ | [out] | float32[] | This parameter Returns the imaginary part of PUSCH PTRS constellation trace. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__fetch__modacc_1ga5d5fd0fcbad2be8e9c993db5cbeb1f83.html language=enus -->
## TOPIC 00248: RFmxNR_ModAccFetchPSSRMSEVMPerSymbolMeanTrace

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__fetch__modacc_1ga5d5fd0fcbad2be8e9c993db5cbeb1f83.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__fetch__modacc_1ga5d5fd0fcbad2be8e9c993db5cbeb1f83.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the mean PSS RMS EVM of each symbol. Syntaxint32 __stdcall RFmxNR_ModAccFetchPSSRMSEVMPerSymbolMeanTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 pssRMSEVMPerSymbolMean[], int32 arraySize, int32 *actualArraySize)RemarksUse

### RFmxNR_ModAccFetchPSSRMSEVMPerSymbolMeanTrace

Fetches the mean PSS RMS EVM of each symbol.

#### Syntax

int32 __stdcall RFmxNR_ModAccFetchPSSRMSEVMPerSymbolMeanTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 pssRMSEVMPerSymbolMean[], int32 arraySize, int32 *actualArraySize)

#### Remarks

Use "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0".Example:"subblock0/carrier0""signal::sig1/subblock0/carrier0""result::r1/subblock0/carrier0""signal::sig1/result::r1/subblock0/carrier0"You can use the RFmxNR_BuildCarrierString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| x0 | [out] | float64 * | This parameter returns the start symbol index from the frame start in terms of SSB numerology. |
| dx | [out] | float64 * | This parameter returns the width in terms of symbols. |
| pssRMSEVMPerSymbolMean | [out] | float32[] | This parameter returns an array which the EVM of each symbol averaged across all the allocated subcarriers allocated with PSS within symbol. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__fetch__modacc_1ga5f62c6592e7df59cdd67bb045f0be5ab.html language=enus -->
## TOPIC 00249: RFmxNR_ModAccFetchSSSRMSEVMPerSubcarrierMeanTrace

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__fetch__modacc_1ga5f62c6592e7df59cdd67bb045f0be5ab.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__fetch__modacc_1ga5f62c6592e7df59cdd67bb045f0be5ab.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the mean SSS RMS EVM of each subcarrier. Syntaxint32 __stdcall RFmxNR_ModAccFetchSSSRMSEVMPerSubcarrierMeanTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 sssRMSEVMPerSubcarrierMean[], int32 arraySize, int32 *actualArraySize

### RFmxNR_ModAccFetchSSSRMSEVMPerSubcarrierMeanTrace

Fetches the mean SSS RMS EVM of each subcarrier.

#### Syntax

int32 __stdcall RFmxNR_ModAccFetchSSSRMSEVMPerSubcarrierMeanTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 sssRMSEVMPerSubcarrierMean[], int32 arraySize, int32 *actualArraySize)

#### Remarks

Use "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0".Example:"subblock0/carrier0""signal::sig1/subblock0/carrier0""result::r1/subblock0/carrier0""signal::sig1/result::r1/subblock0/carrier0"You can use the RFmxNR_BuildCarrierString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| x0 | [out] | float64 * | This parameter returns the start point of the of the resource grid. |
| dx | [out] | float64 * | This parameter returns the subcarrier spacing of SSB. |
| sssRMSEVMPerSubcarrierMean | [out] | float32[] | This parameter returns an array which the EVM of each allocated subcarrier averaged across all the symbols allocated with SSS within the measurement length. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__fetch__modacc_1ga6101247d5ae51bb75d9bdcc84381a1c0.html language=enus -->
## TOPIC 00250: RFmxNR_ModAccFetchPUSCHDMRSConstellationTrace

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__fetch__modacc_1ga6101247d5ae51bb75d9bdcc84381a1c0.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__fetch__modacc_1ga6101247d5ae51bb75d9bdcc84381a1c0.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches PUSCH DMRS trace. The constellation points of different slots in the measurement length is concatenated. Syntaxint32 __stdcall RFmxNR_ModAccFetchPUSCHDMRSConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle puschDMRSConstellation[], i

### RFmxNR_ModAccFetchPUSCHDMRSConstellationTrace

Fetches PUSCH DMRS trace. The constellation points of different slots in the measurement length is concatenated.

#### Syntax

int32 __stdcall RFmxNR_ModAccFetchPUSCHDMRSConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle puschDMRSConstellation[], int32 arraySize, int32 *actualArraySize)

#### Remarks

Use "user<k>" or "carrier<<i>l</i>>" or "subblock<n>" or "subblock<n>/carrier<<i>l</i>>/user<k>" or "subblock<n>/carrier<k>/user<k>/layer<<i>q</i>>" as the selector string to read this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, subblock number, user number and layer number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0/user0/layer0".Example:"subblock0/carrier0/user0/layer0""signal::sig1/subblock0/carrier0/user0/layer0""result::r1/subblock0/carrier0/user0/layer0""signal::sig1/result::r1/subblock0/carrier0/user0/layer0"You can use the RFmxNR_BuildUserString and RFmxNR_BuildLayerString functions to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| puschDMRSConstellation | [out] | NIComplexSingle[] | This parameter returns the PDSCH DMRS constellation trace. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc
