# NI DOCUMENT BUNDLE: rfmxevdo-c-api-ref

<!--NI_BUNDLE_CHUNK bundle=rfmxevdo-c-api-ref start=1 end=167 -->
<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__attributes__acp_1gae8d5a1393c98269f528071fd6d834c04.html language=enus -->
## TOPIC 00001: RFMXEVDO_ATTR_ACP_MEASUREMENT_ENABLED

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__attributes__acp_1gae8d5a1393c98269f528071fd6d834c04.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__attributes__acp_1gae8d5a1393c98269f528071fd6d834c04.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the ACP measurement. SyntaxRFMXEVDO_ATTR_ACP_MEASUREMENT_ENABLEDNumeric ValueData TypeAccessApplies To8392704int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strin

### RFMXEVDO_ATTR_ACP_MEASUREMENT_ENABLED

Specifies whether to enable the ACP measurement.

#### Syntax

RFMXEVDO_ATTR_ACP_MEASUREMENT_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 8392704 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is FALSE.

Parent topic:

ACP

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__attributes__acp_1gaeb0104302ee37be0a0e494578194c0e5.html language=enus -->
## TOPIC 00002: RFMXEVDO_ATTR_ACP_ALL_TRACES_ENABLED

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__attributes__acp_1gaeb0104302ee37be0a0e494578194c0e5.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__attributes__acp_1gaeb0104302ee37be0a0e494578194c0e5.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the traces to be stored and retrieved after performing the ACP measurement. SyntaxRFMXEVDO_ATTR_ACP_ALL_TRACES_ENABLEDNumeric ValueData TypeAccessApplies To8392737int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for th

### RFMXEVDO_ATTR_ACP_ALL_TRACES_ENABLED

Specifies whether to enable the traces to be stored and retrieved after performing the ACP measurement.

#### Syntax

RFMXEVDO_ATTR_ACP_ALL_TRACES_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 8392737 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is FALSE.

Parent topic:

ACP

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__attributes__acp_1gaee2ce2e9ea4ae152b0064a45c7b10a52.html language=enus -->
## TOPIC 00003: RFMXEVDO_ATTR_ACP_NOISE_COMPENSATION_ENABLED

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__attributes__acp_1gaee2ce2e9ea4ae152b0064a45c7b10a52.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__attributes__acp_1gaee2ce2e9ea4ae152b0064a45c7b10a52.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable compensation of the channel powers for the inherent noise floor of the signal analyzer. SyntaxRFMXEVDO_ATTR_ACP_NOISE_COMPENSATION_ENABLEDNumeric ValueData TypeAccessApplies To8392736int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read t

### RFMXEVDO_ATTR_ACP_NOISE_COMPENSATION_ENABLED

Specifies whether to enable compensation of the channel powers for the inherent noise floor of the signal analyzer.

#### Syntax

RFMXEVDO_ATTR_ACP_NOISE_COMPENSATION_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 8392736 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **False**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXEVDO_VAL_ACP_NOISE_COMPENSATION_ENABLED_FALSE | 0 (0x0) | Disables compensation of the channel powers for the noise floor of the signal analyzer. |
| RFMXEVDO_VAL_ACP_NOISE_COMPENSATION_ENABLED_TRUE | 1 (0x1) | Enables compensation of the channel powers for the noise floor of the signal analyzer. The noise floor of the signal analyzer is measured for the RF path used by the ACP measurement and cached for future use. If signal analyzer or measurement parameters change, noise floors are remeasured.Supported Devices: PXIe-5663/5665/5668R, PXIe-5830/5831/5832/5842/5860 |

Parent topic:

ACP

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__attributes__acp__carrier_1gaa755c208db9d3a35daa19ce76f6892be.html language=enus -->
## TOPIC 00004: RFMXEVDO_ATTR_ACP_CARRIER_INTEGRATION_BANDWIDTH

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__attributes__acp__carrier_1gaa755c208db9d3a35daa19ce76f6892be.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__attributes__acp__carrier_1gaa755c208db9d3a35daa19ce76f6892be.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the ACP carrier integration bandwidth. This value is expressed in Hz. SyntaxRFMXEVDO_ATTR_ACP_CARRIER_INTEGRATION_BANDWIDTHNumeric ValueData TypeAccessApplies To8392709float64Read-OnlyCarrierRemarks Use "carrier<k>" as the selector string to read this result.

### RFMXEVDO_ATTR_ACP_CARRIER_INTEGRATION_BANDWIDTH

Returns the ACP carrier integration bandwidth. This value is expressed in Hz.

#### Syntax

RFMXEVDO_ATTR_ACP_CARRIER_INTEGRATION_BANDWIDTH

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 8392709 | float64 | Read-Only | Carrier |

#### Remarks

Use "carrier<k>" as the selector string to read this result.

Parent topic:

Carrier

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__attributes__acp__fft.html language=enus -->
## TOPIC 00005: FFT

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__attributes__acp__fft.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__attributes__acp__fft.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXEVDO_ATTR_ACP_FFT_OVERLAPReturns the number of samples to overlap between consecutive chunks while performing FFT. RFMXEVDO_ATTR_ACP_FFT_OVERLAP_MODESpecifies how the FFT overlap is applied to the acquired samples. AttachmentsNone

### FFT

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXEVDO_ATTR_ACP_FFT_OVERLAP | Returns the number of samples to overlap between consecutive chunks while performing FFT. |
| RFMXEVDO_ATTR_ACP_FFT_OVERLAP_MODE | Specifies how the FFT overlap is applied to the acquired samples. |

#### Attachments

None

Parent topic:

ACP

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__attributes__acp__fft_1ga878831d4dd2f4792cd237c7450147bfe.html language=enus -->
## TOPIC 00006: RFMXEVDO_ATTR_ACP_FFT_OVERLAP

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__attributes__acp__fft_1ga878831d4dd2f4792cd237c7450147bfe.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__attributes__acp__fft_1ga878831d4dd2f4792cd237c7450147bfe.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the number of samples to overlap between consecutive chunks while performing FFT. SyntaxRFMXEVDO_ATTR_ACP_FFT_OVERLAPNumeric ValueData TypeAccessApplies To8392762float64Read-OnlyN/ARemarks This value is expressed as a percentage of RFMXEVDO_ATTR_ACP_SEQUENTIAL_FFT_SIZE attribute when you set

### RFMXEVDO_ATTR_ACP_FFT_OVERLAP

Returns the number of samples to overlap between consecutive chunks while performing FFT.

#### Syntax

RFMXEVDO_ATTR_ACP_FFT_OVERLAP

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 8392762 | float64 | Read-Only | N/A |

#### Remarks

This value is expressed as a percentage of [RFMXEVDO_ATTR_ACP_SEQUENTIAL_FFT_SIZE](group____root__ni_r_fmx_e_v_d_o__attributes__acp__advanced_1ga33ef8090458cfdd964bfdf1b810b7c3f.html) attribute when you set the [RFMXEVDO_ATTR_ACP_MEASUREMENT_METHOD](group____root__ni_r_fmx_e_v_d_o__attributes__acp_1ga1069975b9ee84365f99d91df43fea556.html) attribute to **Sequential FFT**.

You do not need to use a selector string to read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

Parent topic:

FFT

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__attributes__acp__offset__power__reference_1gabb4baf3e620fb41cba9b2768a775bc8b.html language=enus -->
## TOPIC 00007: RFMXEVDO_ATTR_ACP_OFFSET_POWER_REFERENCE_SPECIFIC

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__attributes__acp__offset__power__reference_1gabb4baf3e620fb41cba9b2768a775bc8b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__attributes__acp__offset__power__reference_1gabb4baf3e620fb41cba9b2768a775bc8b.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the index of the carrier used as the reference carrier. The power measured in this carrier is used as the power reference for measuring the offset channel relative power when you set the RFMXEVDO_ATTR_ACP_OFFSET_POWER_REFERENCE_CARRIER attribute to Specific. SyntaxRFMXEVDO_ATTR_ACP_OFFSET_

### RFMXEVDO_ATTR_ACP_OFFSET_POWER_REFERENCE_SPECIFIC

Specifies the index of the carrier used as the reference carrier. The power measured in this carrier is used as the power reference for measuring the offset channel relative power when you set the [RFMXEVDO_ATTR_ACP_OFFSET_POWER_REFERENCE_CARRIER](group____root__ni_r_fmx_e_v_d_o__attributes__acp__offset__power__reference_1ga7895fa74f3a5cc96441bf3608ca21700.html) attribute to **Specific**.

#### Syntax

RFMXEVDO_ATTR_ACP_OFFSET_POWER_REFERENCE_SPECIFIC

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 8392717 | int32 | Read/Write | N/A |

#### Remarks

The default value is 0.

Parent topic:

Power Reference

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__attributes__acp__rbw__filter_1ga01e07bc65629e06f42b056d2104f4918.html language=enus -->
## TOPIC 00008: RFMXEVDO_ATTR_ACP_RBW_FILTER_BANDWIDTH

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__attributes__acp__rbw__filter_1ga01e07bc65629e06f42b056d2104f4918.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__attributes__acp__rbw__filter_1ga01e07bc65629e06f42b056d2104f4918.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the bandwidth of the RBW filter, used to sweep the acquired signal, when you set the RFMXEVDO_ATTR_ACP_RBW_FILTER_AUTO_BANDWIDTH attribute to False. This value is expressed in Hz. SyntaxRFMXEVDO_ATTR_ACP_RBW_FILTER_BANDWIDTHNumeric ValueData TypeAccessApplies To8392732float64Read/WriteN/AR

### RFMXEVDO_ATTR_ACP_RBW_FILTER_BANDWIDTH

Specifies the bandwidth of the RBW filter, used to sweep the acquired signal, when you set the [RFMXEVDO_ATTR_ACP_RBW_FILTER_AUTO_BANDWIDTH](group____root__ni_r_fmx_e_v_d_o__attributes__acp__rbw__filter_1gae66eba543326101515426bec467adf08.html) attribute to **False**. This value is expressed in Hz.

#### Syntax

RFMXEVDO_ATTR_ACP_RBW_FILTER_BANDWIDTH

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 8392732 | float64 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 30 kHz.

Parent topic:

RBW Filter

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__attributes__acp__rbw__filter_1ga33712765da833bb7b91049563daebde9.html language=enus -->
## TOPIC 00009: RFMXEVDO_ATTR_ACP_RBW_FILTER_TYPE

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__attributes__acp__rbw__filter_1ga33712765da833bb7b91049563daebde9.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__attributes__acp__rbw__filter_1ga33712765da833bb7b91049563daebde9.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the shape of the digital RBW filter. SyntaxRFMXEVDO_ATTR_ACP_RBW_FILTER_TYPENumeric ValueData TypeAccessApplies To8392733int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector String topi

### RFMXEVDO_ATTR_ACP_RBW_FILTER_TYPE

Specifies the shape of the digital RBW filter.

#### Syntax

RFMXEVDO_ATTR_ACP_RBW_FILTER_TYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 8392733 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **Gaussian**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXEVDO_VAL_ACP_RBW_FILTER_TYPE_FFT_BASED | 0 (0x0) | An RBW with an FFT-based response is applied. |
| RFMXEVDO_VAL_ACP_RBW_FILTER_TYPE_GAUSSIAN | 1 (0x1) | An RBW filter with a Gaussian response is applied. |
| RFMXEVDO_VAL_ACP_RBW_FILTER_TYPE_FLAT | 2 (0x2) | An RBW filter with a flat response is applied. |

Parent topic:

RBW Filter

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__attributes__acp__results_1ga818281ceeec20e7e281762a0ef8ee329.html language=enus -->
## TOPIC 00010: RFMXEVDO_ATTR_ACP_RESULTS_TOTAL_CARRIER_POWER

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__attributes__acp__results_1ga818281ceeec20e7e281762a0ef8ee329.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__attributes__acp__results_1ga818281ceeec20e7e281762a0ef8ee329.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the total carrier power measured by the adjacent channel power (ACP) measurement. This value is expressed in dBm. SyntaxRFMXEVDO_ATTR_ACP_RESULTS_TOTAL_CARRIER_POWERNumeric ValueData TypeAccessApplies To8392738float64Read-OnlyN/ARemarks You do not need to use a selector string to configure o

### RFMXEVDO_ATTR_ACP_RESULTS_TOTAL_CARRIER_POWER

Returns the total carrier power measured by the adjacent channel power (ACP) measurement. This value is expressed in dBm.

#### Syntax

RFMXEVDO_ATTR_ACP_RESULTS_TOTAL_CARRIER_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 8392738 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal and result instances. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__attributes__acp__results__carrier_1gab03323bbdd99dca639f30da529faf373.html language=enus -->
## TOPIC 00011: RFMXEVDO_ATTR_ACP_RESULTS_CARRIER_RELATIVE_POWER

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__attributes__acp__results__carrier_1gab03323bbdd99dca639f30da529faf373.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__attributes__acp__results__carrier_1gab03323bbdd99dca639f30da529faf373.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the relative measured carrier power. This value is expressed in dB. SyntaxRFMXEVDO_ATTR_ACP_RESULTS_CARRIER_RELATIVE_POWERNumeric ValueData TypeAccessApplies To8392743float64Read-OnlyCarrierRemarks Use "carrier<i><n></i>" as the Selector String to read this attribute.

### RFMXEVDO_ATTR_ACP_RESULTS_CARRIER_RELATIVE_POWER

Returns the relative measured carrier power. This value is expressed in dB.

#### Syntax

RFMXEVDO_ATTR_ACP_RESULTS_CARRIER_RELATIVE_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 8392743 | float64 | Read-Only | Carrier |

#### Remarks

Use "carrier<i><n></i>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this attribute.

Parent topic:

Carrier

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__attributes__acp__results__upper__offset.html language=enus -->
## TOPIC 00012: Upper Offset

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__attributes__acp__results__upper__offset.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__attributes__acp__results__upper__offset.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXEVDO_ATTR_ACP_RESULTS_UPPER_OFFSET_ABSOLUTE_POWERReturns the absolute measured upper offset channel power. This value is expressed in dBm. RFMXEVDO_ATTR_ACP_RESULTS_UPPER_OFFSET_RELATIVE_POWERReturns the upper offset channel power measured relative to the in

### Upper Offset

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXEVDO_ATTR_ACP_RESULTS_UPPER_OFFSET_ABSOLUTE_POWER | Returns the absolute measured upper offset channel power. This value is expressed in dBm. |
| RFMXEVDO_ATTR_ACP_RESULTS_UPPER_OFFSET_RELATIVE_POWER | Returns the upper offset channel power measured relative to the integrated power of the power reference carrier. This value is expressed in dB. |

#### Attachments

None

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__attributes__acp__results__upper__offset_1gade4dde28d953d055ec54169a7f31815a.html language=enus -->
## TOPIC 00013: RFMXEVDO_ATTR_ACP_RESULTS_UPPER_OFFSET_ABSOLUTE_POWER

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__attributes__acp__results__upper__offset_1gade4dde28d953d055ec54169a7f31815a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__attributes__acp__results__upper__offset_1gade4dde28d953d055ec54169a7f31815a.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the absolute measured upper offset channel power. This value is expressed in dBm. SyntaxRFMXEVDO_ATTR_ACP_RESULTS_UPPER_OFFSET_ABSOLUTE_POWERNumeric ValueData TypeAccessApplies To8392754float64Read-OnlyOffsetRemarks Use "offset<i><n></i>" as the Selector String to read this attribute.

### RFMXEVDO_ATTR_ACP_RESULTS_UPPER_OFFSET_ABSOLUTE_POWER

Returns the absolute measured upper offset channel power. This value is expressed in dBm.

#### Syntax

RFMXEVDO_ATTR_ACP_RESULTS_UPPER_OFFSET_ABSOLUTE_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 8392754 | float64 | Read-Only | Offset |

#### Remarks

Use "offset<i><n></i>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this attribute.

Parent topic:

Upper Offset

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__attributes__advanced_1gaf0a188ce9d27ffa7cfa57370349bbb8e.html language=enus -->
## TOPIC 00014: RFMXEVDO_ATTR_LIMITED_CONFIGURATION_CHANGE

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__attributes__advanced_1gaf0a188ce9d27ffa7cfa57370349bbb8e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__attributes__advanced_1gaf0a188ce9d27ffa7cfa57370349bbb8e.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the set of attributes that are considered by RFmx in the locked signal configuration state. SyntaxRFMXEVDO_ATTR_LIMITED_CONFIGURATION_CHANGENumeric ValueData TypeAccessApplies To8441859int32Read/WriteN/ARemarks If your test system performs the same measurement at different selected ports,

### RFMXEVDO_ATTR_LIMITED_CONFIGURATION_CHANGE

Specifies the set of attributes that are considered by RFmx in the locked signal configuration state.

#### Syntax

RFMXEVDO_ATTR_LIMITED_CONFIGURATION_CHANGE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 8441859 | int32 | Read/Write | N/A |

#### Remarks

If your test system performs the same measurement at different selected ports, multiple frequencies and/or power levels repeatedly, enabling this attribute can help achieve faster measurements. When you set this attribute to a value other than **Disabled**, the RFmx driver will use an optimized code path and skip some checks. Because RFmx skips some checks when you use this attribute, you need to be aware of the limitations of this feature, which are listed in the [Limitations of the Limited Configuration Change Property](https://www.ni.com/docs/en-US/bundle/rfmx-wcdma-prop/page/rfmxwcdmaprop/limitations.html) topic.

You can also use this attribute to lock a specific instrument configuration for a signal so that every time that you initiate the signal, RFmx applies the RFmxInstr attributes from a locked configuration.

NI recommends you use this attribute in conjunction with named signal configurations. Create named signal configurations for each measurement configuration in your test program and set this attribute to a value other than **Disabled** for one or more of the named signal configurations. This allows RFmx to precompute the acquisition settings for your measurement configurations and re-use the precomputed settings each time you initiate the measurement. You do not need to use this attribute if you create named signals for all the measurement configurations in your test program during test sequence initialization and do not change any RFInstr or personality attributes while testing each device under test. RFmx automatically optimizes that use case.

Specify the named signal configuration you are setting this attribute in the selector string input. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default value is **Disabled**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXEVDO_VAL_LIMITED_CONFIGURATION_CHANGE_DISABLED | 0 (0x0) | This is the normal mode of RFmx operation. All configuration changes in RFmxInstr attributes or in personality attributes will be applied during RFmx Commit. |
| RFMXEVDO_VAL_LIMITED_CONFIGURATION_CHANGE_NO_CHANGE | 1 (0x1) | Signal configuration is locked after the first Commit of the named signal configuration. Any configuration change thereafter either in RFmxInstr attributes or personality attributes will not be considered by subsequent RFmx Commits or Initiates of this signal. Use No Change if you have created named signal configurations for all measurement configurations but are setting some RFmxInstr attributes. Refer to the Limitations of the Limited Configuration Change Property topic for more details about the limitations of using this mode. |
| RFMXEVDO_VAL_LIMITED_CONFIGURATION_CHANGE_FREQUENCY | 2 (0x2) | Signal configuration, other than center frequency and external attenuation, is locked after first Commit of the named signal configuration. Thereafter, only the RFMXEVDO_ATTR_CENTER_FREQUENCY and RFMXEVDO_ATTR_EXTERNAL_ATTENUATION attribute value changes will be considered by subsequent driver Commits or Initiates of this signal. Refer to the Limitations of the Limited Configuration Change Property topic for more details about the limitations of using this mode. |
| RFMXEVDO_VAL_LIMITED_CONFIGURATION_CHANGE_REFERENCE_LEVEL | 3 (0x3) | Signal configuration, other than the reference level, is locked after first Commit of the named signal configuration. Thereafter only the RFMXEVDO_ATTR_REFERENCE_LEVEL attribute value change will be considered by subsequent driver Commits or Initiates of this signal. If you have configured this signal to use an IQ Power Edge Trigger, NI recommends that you set the RFMXEVDO_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE to Relative so that the trigger level is automatically adjusted as you adjust the reference level. Refer to the Limitations of the Limited Configuration Change Property topic for more details about the limitations of using this mode. |
| RFMXEVDO_VAL_LIMITED_CONFIGURATION_CHANGE_FREQUENCY_AND_REFERENCE_LEVEL | 4 (0x4) | Signal configuration, other than center frequency, reference level, and external attenuation, is locked after first Commit of the named signal configuration. Thereafter only Center Frequency, Reference Level, and External Attenuation attribute value changes will be considered by subsequent driver Commits or Initiates of this signal. If you have configured this signal to use an IQ Power Edge Trigger, NI recommends you set the IQ Power Edge Trigger Level Type to Relative so that the trigger level is automatically adjusted as you adjust the reference level. Refer to the Limitations of the Limited Configuration Change Property topic for more details about the limitations of using this mode. |
| RFMXEVDO_VAL_LIMITED_CONFIGURATION_CHANGE_SELECTED_PORTS_FREQUENCY_AND_REFERENCE_LEVEL | 5 (0x5) | Signal configuration, other than selected ports, center frequency, reference level, external attenuation, and RFInstr configuration, is locked after first Commit or Initiate of the named signal configuration. Thereafter only Selected Ports, Center Frequency, Reference Level, and External Attenuation attribute value changes will be considered by subsequent driver Commits or Initiates of this signal. If you have configured this signal to use an IQ Power Edge Trigger, NI recommends you set the IQ Power Edge Level Type to Relative so that the trigger level is automatically adjusted as you adjust the reference level. Refer to the Limitations of the Limited Configuration Change Property topic for more details about the limitations of using this mode. |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__attributes__carrier.html language=enus -->
## TOPIC 00015: Carrier

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__attributes__carrier.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__attributes__carrier.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsChannelSpreadingGroup membersNameDescriptionRFMXEVDO_ATTR_CARRIER_FREQUENCYSpecifies the carrier frequency of the RF signal to acquire. This value is expressed in Hz. The signal analyzer tunes to this frequency. RFMXEVDO_ATTR_NUMBER_OF_CARRIERSSpecifies the number of carriers in the signal. RF

### Carrier

#### Groups

- Channel
- Spreading

#### Group members

| Name | Description |
| --- | --- |
| RFMXEVDO_ATTR_CARRIER_FREQUENCY | Specifies the carrier frequency of the RF signal to acquire. This value is expressed in Hz. The signal analyzer tunes to this frequency. |
| RFMXEVDO_ATTR_NUMBER_OF_CARRIERS | Specifies the number of carriers in the signal. |
| RFMXEVDO_ATTR_PHYSICAL_LAYER_SUBTYPE | Selects the EV-DO physical layer subtype. |

#### Attachments

None

Parent topic:

Attributes

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__attributes__carrier_1ga2ee386bf429adda789b090a59bd05403.html language=enus -->
## TOPIC 00016: RFMXEVDO_ATTR_PHYSICAL_LAYER_SUBTYPE

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__attributes__carrier_1ga2ee386bf429adda789b090a59bd05403.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__attributes__carrier_1ga2ee386bf429adda789b090a59bd05403.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Selects the EV-DO physical layer subtype. SyntaxRFMXEVDO_ATTR_PHYSICAL_LAYER_SUBTYPENumeric ValueData TypeAccessApplies To8388625int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector String topic

### RFMXEVDO_ATTR_PHYSICAL_LAYER_SUBTYPE

Selects the EV-DO physical layer subtype.

#### Syntax

RFMXEVDO_ATTR_PHYSICAL_LAYER_SUBTYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 8388625 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **0,1**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXEVDO_VAL_PHYSICAL_LAYER_SUBTYPE_0_1 | 0 (0x0) | Specifies subtype 0, 1. 3GPP2 C.S0024-B v3.0 defines this subtype in 10 DEFAULT (SUBTYPE 0) AND SUBTYPE 1 PHYSICAL LAYER PROTOCOL. |
| RFMXEVDO_VAL_PHYSICAL_LAYER_SUBTYPE_2 | 1 (0x1) | Specifies subtype 2. 3GPP2 C.S0024-B v3.0 defines this subtype in 11 SUBTYPE 2 PHYSICAL LAYER. |
| RFMXEVDO_VAL_PHYSICAL_LAYER_SUBTYPE_3 | 2 (0x2) | Specifies subtype 3. 3GPP2 C.S0024-B v3.0 defines this subtype in 12 SUBTYPE 3 PHYSICAL LAYER. |

Parent topic:

Carrier

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__attributes__carrier__channel.html language=enus -->
## TOPIC 00017: Channel

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__attributes__carrier__channel.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__attributes__carrier__channel.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsUser DefinedGroup membersNameDescriptionRFMXEVDO_ATTR_CHANNEL_CONFIGURATION_MODESpecifies whether to detect the channels automatically or to use a specified channel configuration. AttachmentsNone

### Channel

#### Groups

- User Defined

#### Group members

| Name | Description |
| --- | --- |
| RFMXEVDO_ATTR_CHANNEL_CONFIGURATION_MODE | Specifies whether to detect the channels automatically or to use a specified channel configuration. |

#### Attachments

None

Parent topic:

Carrier

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__attributes__carrier__spreading__uplink_1ga26bd1057ae097484079a057463933c51.html language=enus -->
## TOPIC 00018: RFMXEVDO_ATTR_UPLINK_SPREADING_I_MASK

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__attributes__carrier__spreading__uplink_1ga26bd1057ae097484079a057463933c51.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__attributes__carrier__spreading__uplink_1ga26bd1057ae097484079a057463933c51.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the long code mask of the in-phase (I) channel. SyntaxRFMXEVDO_ATTR_UPLINK_SPREADING_I_MASKNumeric ValueData TypeAccessApplies To8388649int64Read/WriteN/ARemarks The default value is 0x0.

### RFMXEVDO_ATTR_UPLINK_SPREADING_I_MASK

Specifies the long code mask of the in-phase (I) channel.

#### Syntax

RFMXEVDO_ATTR_UPLINK_SPREADING_I_MASK

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 8388649 | int64 | Read/Write | N/A |

#### Remarks

The default value is 0x0.

Parent topic:

Uplink

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__attributes__carrier__spreading__uplink_1ga52f9328597b1042bd388ed4e8d0df8a6.html language=enus -->
## TOPIC 00019: RFMXEVDO_ATTR_UPLINK_SPREADING_Q_MASK

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__attributes__carrier__spreading__uplink_1ga52f9328597b1042bd388ed4e8d0df8a6.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__attributes__carrier__spreading__uplink_1ga52f9328597b1042bd388ed4e8d0df8a6.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the long code mask of the quadrature (Q) channel. SyntaxRFMXEVDO_ATTR_UPLINK_SPREADING_Q_MASKNumeric ValueData TypeAccessApplies To8388650int64Read/WriteN/ARemarks The default value is 0x0.

### RFMXEVDO_ATTR_UPLINK_SPREADING_Q_MASK

Specifies the long code mask of the quadrature (Q) channel.

#### Syntax

RFMXEVDO_ATTR_UPLINK_SPREADING_Q_MASK

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 8388650 | int64 | Read/Write | N/A |

#### Remarks

The default value is 0x0.

Parent topic:

Uplink

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__attributes__cda.html language=enus -->
## TOPIC 00020: CDA

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__attributes__cda.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__attributes__cda.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsMeasurement ChannelResultsGroup membersNameDescriptionRFMXEVDO_ATTR_CDA_ALL_TRACES_ENABLEDSpecifies whether to enable the traces after performing the CDA measurement. RFMXEVDO_ATTR_CDA_IQ_GAIN_IMBALANCE_REMOVAL_ENABLEDSpecifies whether to remove the I/Q gain imbalance before the CDA measuremen

### CDA

#### Groups

- Measurement Channel
- Results

#### Group members

| Name | Description |
| --- | --- |
| RFMXEVDO_ATTR_CDA_ALL_TRACES_ENABLED | Specifies whether to enable the traces after performing the CDA measurement. |
| RFMXEVDO_ATTR_CDA_IQ_GAIN_IMBALANCE_REMOVAL_ENABLED | Specifies whether to remove the I/Q gain imbalance before the CDA measurement. |
| RFMXEVDO_ATTR_CDA_IQ_OFFSET_REMOVAL_ENABLED | Specifies whether to remove the I/Q offset before the CDA measurement. |
| RFMXEVDO_ATTR_CDA_IQ_QUADRATURE_ERROR_REMOVAL_ENABLED | Specifies whether to remove the I/Q quadrature error before the CDA measurement. |
| RFMXEVDO_ATTR_CDA_MEASUREMENT_ENABLED | Specifies whether to enable the CDA measurement. |
| RFMXEVDO_ATTR_CDA_MEASUREMENT_LENGTH | Specifies the duration of the CDA measurement. This value is expressed in slots. |
| RFMXEVDO_ATTR_CDA_MEASUREMENT_OFFSET | Specifies the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the RFMXEVDO_ATTR_CDA_SYNCHRONIZATION_MODE attribute. |
| RFMXEVDO_ATTR_CDA_POWER_UNIT | Specifies the measurement unit of the code domain power results. |
| RFMXEVDO_ATTR_CDA_RECEIVE_FILTER_ENABLED | Specifies whether to enable receive filtering. |
| RFMXEVDO_ATTR_CDA_SPECTRUM_INVERTED | Specifies whether the signal spectrum is inverted. |
| RFMXEVDO_ATTR_CDA_SYNCHRONIZATION_MODE | Specifies whether the measurement is performed from the frame, slot, or symbol boundary. |

#### Attachments

None

Parent topic:

Attributes

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__attributes__cda_1ga05cd9bcb2dbe234d7af1a61b6af47869.html language=enus -->
## TOPIC 00021: RFMXEVDO_ATTR_CDA_POWER_UNIT

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__attributes__cda_1ga05cd9bcb2dbe234d7af1a61b6af47869.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__attributes__cda_1ga05cd9bcb2dbe234d7af1a61b6af47869.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the measurement unit of the code domain power results. SyntaxRFMXEVDO_ATTR_CDA_POWER_UNITNumeric ValueData TypeAccessApplies To8466440int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selecto

### RFMXEVDO_ATTR_CDA_POWER_UNIT

Specifies the measurement unit of the code domain power results.

#### Syntax

RFMXEVDO_ATTR_CDA_POWER_UNIT

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 8466440 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **dB**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXEVDO_VAL_CDA_POWER_UNIT_DB | 0 (0x0) | Specifies that the measurement unit is dB. |
| RFMXEVDO_VAL_CDA_POWER_UNIT_DBM | 1 (0x1) | Specifies that the measurement unit is dBm. |

Parent topic:

CDA

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__attributes__cda_1ga16c13add721f3b8dc1be5993341bfc52.html language=enus -->
## TOPIC 00022: RFMXEVDO_ATTR_CDA_MEASUREMENT_OFFSET

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__attributes__cda_1ga16c13add721f3b8dc1be5993341bfc52.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__attributes__cda_1ga16c13add721f3b8dc1be5993341bfc52.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the RFMXEVDO_ATTR_CDA_SYNCHRONIZATION_MODE attribute. SyntaxRFMXEVDO_ATTR_CDA_MEASUREMENT_OFFSETNumeric ValueData TypeAccessApplies To8466435int3

### RFMXEVDO_ATTR_CDA_MEASUREMENT_OFFSET

Specifies the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the [RFMXEVDO_ATTR_CDA_SYNCHRONIZATION_MODE](group____root__ni_r_fmx_e_v_d_o__attributes__cda_1ga3879358376bae21442b30af14a6884c6.html) attribute.

#### Syntax

RFMXEVDO_ATTR_CDA_MEASUREMENT_OFFSET

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 8466435 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 0. Valid values are [0,15]. The sum of CDA Meas Offset and CDA Meas Length is less than or equal to 16.

Parent topic:

CDA

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__attributes__cda_1ga1f154aa90c553b6bc479a08f9989d94d.html language=enus -->
## TOPIC 00023: RFMXEVDO_ATTR_CDA_IQ_QUADRATURE_ERROR_REMOVAL_ENABLED

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__attributes__cda_1ga1f154aa90c553b6bc479a08f9989d94d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__attributes__cda_1ga1f154aa90c553b6bc479a08f9989d94d.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to remove the I/Q quadrature error before the CDA measurement. SyntaxRFMXEVDO_ATTR_CDA_IQ_QUADRATURE_ERROR_REMOVAL_ENABLEDNumeric ValueData TypeAccessApplies To8466444int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the defa

### RFMXEVDO_ATTR_CDA_IQ_QUADRATURE_ERROR_REMOVAL_ENABLED

Specifies whether to remove the I/Q quadrature error before the CDA measurement.

#### Syntax

RFMXEVDO_ATTR_CDA_IQ_QUADRATURE_ERROR_REMOVAL_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 8466444 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **False**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXEVDO_VAL_CDA_IQ_QUADRATURE_ERROR_REMOVAL_ENABLED_FALSE | 0 (0x0) | The I/Q quadrature error is not removed before the CDA measurement. |
| RFMXEVDO_VAL_CDA_IQ_QUADRATURE_ERROR_REMOVAL_ENABLED_TRUE | 1 (0x1) | The I/Q quadrature error is removed before the CDA measurement. |

Parent topic:

CDA

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__attributes__cda__results_1ga220b441357e11ce33769e6a6b5600aa7.html language=enus -->
## TOPIC 00024: RFMXEVDO_ATTR_CDA_RESULTS_CHIP_RATE_ERROR

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__attributes__cda__results_1ga220b441357e11ce33769e6a6b5600aa7.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__attributes__cda__results_1ga220b441357e11ce33769e6a6b5600aa7.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the chip rate error. This value is expressed in ppm. SyntaxRFMXEVDO_ATTR_CDA_RESULTS_CHIP_RATE_ERRORNumeric ValueData TypeAccessApplies To8466450float64Read-OnlyN/ARemarks You do not need to use a selector string to read this result for the default signal and result instances. Refer to the S

### RFMXEVDO_ATTR_CDA_RESULTS_CHIP_RATE_ERROR

Returns the chip rate error. This value is expressed in ppm.

#### Syntax

RFMXEVDO_ATTR_CDA_RESULTS_CHIP_RATE_ERROR

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 8466450 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for the default signal and result instances. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and named results.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__attributes__cda__results_1gadc6acea77fe5c310a31296f980a6c88e.html language=enus -->
## TOPIC 00025: RFMXEVDO_ATTR_CDA_RESULTS_FREQUENCY_ERROR

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__attributes__cda__results_1gadc6acea77fe5c310a31296f980a6c88e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__attributes__cda__results_1gadc6acea77fe5c310a31296f980a6c88e.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the frequency error. This value is expressed in Hz. SyntaxRFMXEVDO_ATTR_CDA_RESULTS_FREQUENCY_ERRORNumeric ValueData TypeAccessApplies To8466449float64Read-OnlyN/ARemarks You do not need to use a selector string to read this result for the default signal and result instances. Refer to the Se

### RFMXEVDO_ATTR_CDA_RESULTS_FREQUENCY_ERROR

Returns the frequency error. This value is expressed in Hz.

#### Syntax

RFMXEVDO_ATTR_CDA_RESULTS_FREQUENCY_ERROR

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 8466449 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for the default signal and result instances. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and named results.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__attributes__cda__results_1gae4afe8aad2e7334b7e64fd2a29e4b0a0.html language=enus -->
## TOPIC 00026: RFMXEVDO_ATTR_CDA_RESULTS_IQ_QUADRATURE_ERROR

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__attributes__cda__results_1gae4afe8aad2e7334b7e64fd2a29e4b0a0.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__attributes__cda__results_1gae4afe8aad2e7334b7e64fd2a29e4b0a0.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the I/Q quadrature error. This value is expressed in degrees. SyntaxRFMXEVDO_ATTR_CDA_RESULTS_IQ_QUADRATURE_ERRORNumeric ValueData TypeAccessApplies To8466453float64Read-OnlyN/ARemarks You do not need to use a selector string to read this result for the default signal and result instances. R

### RFMXEVDO_ATTR_CDA_RESULTS_IQ_QUADRATURE_ERROR

Returns the I/Q quadrature error. This value is expressed in degrees.

#### Syntax

RFMXEVDO_ATTR_CDA_RESULTS_IQ_QUADRATURE_ERROR

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 8466453 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for the default signal and result instances. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and named results.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__attributes__cda__results__uplink_1ga08600046c545995c4f61ced27a2a1850.html language=enus -->
## TOPIC 00027: RFMXEVDO_ATTR_CDA_RESULTS_UPLINK_RMS_SYMBOL_PHASE_ERROR

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__attributes__cda__results__uplink_1ga08600046c545995c4f61ced27a2a1850.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__attributes__cda__results__uplink_1ga08600046c545995c4f61ced27a2a1850.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the RMS symbol phase error of the configured measurement channel. This value is expressed in degrees. SyntaxRFMXEVDO_ATTR_CDA_RESULTS_UPLINK_RMS_SYMBOL_PHASE_ERRORNumeric ValueData TypeAccessApplies To8466457float64Read-OnlyN/ARemarks You do not need to use a selector string to read this res

### RFMXEVDO_ATTR_CDA_RESULTS_UPLINK_RMS_SYMBOL_PHASE_ERROR

Returns the RMS symbol phase error of the configured measurement channel. This value is expressed in degrees.

#### Syntax

RFMXEVDO_ATTR_CDA_RESULTS_UPLINK_RMS_SYMBOL_PHASE_ERROR

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 8466457 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for the default signal and result instances. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and named results.

Parent topic:

Uplink

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__attributes__cda__results__uplink_1ga0f5c030e4c08a30f28376cac70a29392.html language=enus -->
## TOPIC 00028: RFMXEVDO_ATTR_CDA_RESULTS_UPLINK_MEAN_INACTIVE_POWER

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__attributes__cda__results__uplink_1ga0f5c030e4c08a30f28376cac70a29392.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__attributes__cda__results__uplink_1ga0f5c030e4c08a30f28376cac70a29392.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the average code power measured among the set of inactive channels in the code domain of the base spreading factor. The base spreading factor depends on the configured physical layer subtype and is 16 for subtype 0/1; 32 otherwise. SyntaxRFMXEVDO_ATTR_CDA_RESULTS_UPLINK_MEAN_INACTIVE_POWERNu

### RFMXEVDO_ATTR_CDA_RESULTS_UPLINK_MEAN_INACTIVE_POWER

Returns the average code power measured among the set of inactive channels in the code domain of the base spreading factor. The base spreading factor depends on the configured physical layer subtype and is 16 for subtype 0/1; 32 otherwise.

#### Syntax

RFMXEVDO_ATTR_CDA_RESULTS_UPLINK_MEAN_INACTIVE_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 8466463 | float64 | Read-Only | N/A |

#### Remarks

If you set the [RFMXEVDO_ATTR_CDA_POWER_UNIT](group____root__ni_r_fmx_e_v_d_o__attributes__cda_1ga05cd9bcb2dbe234d7af1a61b6af47869.html) attribute to **dBm**, the measurement returns the absolute measured power in dBm. Otherwise, the measurement returns the value relative to the total power in dB.

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

Parent topic:

Uplink

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__attributes__sem__averaging.html language=enus -->
## TOPIC 00029: Averaging

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__attributes__sem__averaging.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__attributes__sem__averaging.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXEVDO_ATTR_SEM_AVERAGING_COUNTSpecifies the number of acquisitions used for averaging when you set the RFMXEVDO_ATTR_SEM_AVERAGING_ENABLED attribute to True. RFMXEVDO_ATTR_SEM_AVERAGING_ENABLEDSpecifies whether to enable averaging for the spectral emissions m

### Averaging

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXEVDO_ATTR_SEM_AVERAGING_COUNT | Specifies the number of acquisitions used for averaging when you set the RFMXEVDO_ATTR_SEM_AVERAGING_ENABLED attribute to True. |
| RFMXEVDO_ATTR_SEM_AVERAGING_ENABLED | Specifies whether to enable averaging for the spectral emissions mask (SEM) measurement. |
| RFMXEVDO_ATTR_SEM_AVERAGING_TYPE | Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the spectral emissions mask (SEM) measurement. |

#### Attachments

None

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__attributes__sem__carrier.html language=enus -->
## TOPIC 00030: Carrier

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__attributes__sem__carrier.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__attributes__sem__carrier.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXEVDO_ATTR_SEM_CARRIER_INTEGRATION_BANDWIDTHReturns the SEM carrier integration bandwidth. This value is expressed in Hz. AttachmentsNone

### Carrier

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXEVDO_ATTR_SEM_CARRIER_INTEGRATION_BANDWIDTH | Returns the SEM carrier integration bandwidth. This value is expressed in Hz. |

#### Attachments

None

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__attributes__sem__carrier_1ga47341302c81bff3f7532deaea4265ae4.html language=enus -->
## TOPIC 00031: RFMXEVDO_ATTR_SEM_CARRIER_INTEGRATION_BANDWIDTH

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__attributes__sem__carrier_1ga47341302c81bff3f7532deaea4265ae4.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__attributes__sem__carrier_1ga47341302c81bff3f7532deaea4265ae4.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the SEM carrier integration bandwidth. This value is expressed in Hz. SyntaxRFMXEVDO_ATTR_SEM_CARRIER_INTEGRATION_BANDWIDTHNumeric ValueData TypeAccessApplies To8421381float64Read-OnlyCarrierRemarks Use "carrier<k>" as the selector string to read this result.

### RFMXEVDO_ATTR_SEM_CARRIER_INTEGRATION_BANDWIDTH

Returns the SEM carrier integration bandwidth. This value is expressed in Hz.

#### Syntax

RFMXEVDO_ATTR_SEM_CARRIER_INTEGRATION_BANDWIDTH

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 8421381 | float64 | Read-Only | Carrier |

#### Remarks

Use "carrier<k>" as the selector string to read this result.

Parent topic:

Carrier

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__attributes__sem__offset_1ga712a7be6e4c3d11b5cc3a16bfa1abc0d.html language=enus -->
## TOPIC 00032: RFMXEVDO_ATTR_SEM_OFFSET_STOP_FREQUENCY

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__attributes__sem__offset_1ga712a7be6e4c3d11b5cc3a16bfa1abc0d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__attributes__sem__offset_1ga712a7be6e4c3d11b5cc3a16bfa1abc0d.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the stop frequency of an SEM offset segment relative to the carrier frequency. This value is expressed in Hz. SyntaxRFMXEVDO_ATTR_SEM_OFFSET_STOP_FREQUENCYNumeric ValueData TypeAccessApplies To8421397float64Read-OnlyOffsetRemarks Use "offset<n>" as the selector string to read this result.

### RFMXEVDO_ATTR_SEM_OFFSET_STOP_FREQUENCY

Returns the stop frequency of an SEM offset segment relative to the carrier frequency. This value is expressed in Hz.

#### Syntax

RFMXEVDO_ATTR_SEM_OFFSET_STOP_FREQUENCY

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 8421397 | float64 | Read-Only | Offset |

#### Remarks

Use "offset<n>" as the selector string to read this result.

Parent topic:

Offset

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__attributes__sem__results.html language=enus -->
## TOPIC 00033: Results

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__attributes__sem__results.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__attributes__sem__results.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsCarrierLower OffsetUpper OffsetGroup membersNameDescriptionRFMXEVDO_ATTR_SEM_RESULTS_COMPOSITE_MEASUREMENT_STATUSIndicates the overall measurement status based on the measurement limits and the failure criteria specified by the standard for each offset segment. RFMXEVDO_ATTR_SEM_RESULTS_TOTAL_

### Results

#### Groups

- Carrier
- Lower Offset
- Upper Offset

#### Group members

| Name | Description |
| --- | --- |
| RFMXEVDO_ATTR_SEM_RESULTS_COMPOSITE_MEASUREMENT_STATUS | Indicates the overall measurement status based on the measurement limits and the failure criteria specified by the standard for each offset segment. |
| RFMXEVDO_ATTR_SEM_RESULTS_TOTAL_CARRIER_POWER | Returns the total carrier power of the selected carrier. This value is expressed in dBm. |

#### Attachments

None

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__attributes__sem__results_1ga1480402ffc5007a669499d24cbab01f5.html language=enus -->
## TOPIC 00034: RFMXEVDO_ATTR_SEM_RESULTS_TOTAL_CARRIER_POWER

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__attributes__sem__results_1ga1480402ffc5007a669499d24cbab01f5.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__attributes__sem__results_1ga1480402ffc5007a669499d24cbab01f5.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the total carrier power of the selected carrier. This value is expressed in dBm. SyntaxRFMXEVDO_ATTR_SEM_RESULTS_TOTAL_CARRIER_POWERNumeric ValueData TypeAccessApplies To8421416float64Read-OnlyN/ARemarks You do not need to use a selector string to configure or read this attribute for the def

### RFMXEVDO_ATTR_SEM_RESULTS_TOTAL_CARRIER_POWER

Returns the total carrier power of the selected carrier. This value is expressed in dBm.

#### Syntax

RFMXEVDO_ATTR_SEM_RESULTS_TOTAL_CARRIER_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 8421416 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal and result instances. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__attributes__sem__results__carrier.html language=enus -->
## TOPIC 00035: Carrier

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__attributes__sem__results__carrier.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__attributes__sem__results__carrier.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXEVDO_ATTR_SEM_RESULTS_CARRIER_ABSOLUTE_INTEGRATED_POWERReturns the absolute carrier power measurement. This value is expressed in dBm. RFMXEVDO_ATTR_SEM_RESULTS_CARRIER_ABSOLUTE_PEAK_POWERReturns the peak absolute carrier power. This value is expressed in dB

### Carrier

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXEVDO_ATTR_SEM_RESULTS_CARRIER_ABSOLUTE_INTEGRATED_POWER | Returns the absolute carrier power measurement. This value is expressed in dBm. |
| RFMXEVDO_ATTR_SEM_RESULTS_CARRIER_ABSOLUTE_PEAK_POWER | Returns the peak absolute carrier power. This value is expressed in dBm. |
| RFMXEVDO_ATTR_SEM_RESULTS_CARRIER_PEAK_FREQUENCY | Returns the frequency at which the peak power occurs in the carrier channel. This value is expressed in Hz. |
| RFMXEVDO_ATTR_SEM_RESULTS_CARRIER_RELATIVE_INTEGRATED_POWER | Returns the relative carrier power measurement. This value is expressed in dB. |

#### Attachments

None

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__attributes__sem__results__lower__offset_1ga84705407be4a38271bef509550848149.html language=enus -->
## TOPIC 00036: RFMXEVDO_ATTR_SEM_RESULTS_LOWER_OFFSET_RELATIVE_INTEGRATED_POWER

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__attributes__sem__results__lower__offset_1ga84705407be4a38271bef509550848149.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__attributes__sem__results__lower__offset_1ga84705407be4a38271bef509550848149.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the power measured in the lower (negative) offset segment relative to the integrated power of the reference carrier. SyntaxRFMXEVDO_ATTR_SEM_RESULTS_LOWER_OFFSET_RELATIVE_INTEGRATED_POWERNumeric ValueData TypeAccessApplies To8421429float64Read-OnlyOffsetRemarks Use "offset<i><n></i>" as the

### RFMXEVDO_ATTR_SEM_RESULTS_LOWER_OFFSET_RELATIVE_INTEGRATED_POWER

Returns the power measured in the lower (negative) offset segment relative to the integrated power of the reference carrier.

#### Syntax

RFMXEVDO_ATTR_SEM_RESULTS_LOWER_OFFSET_RELATIVE_INTEGRATED_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 8421429 | float64 | Read-Only | Offset |

#### Remarks

Use "offset<i><n></i>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this attribute.

Parent topic:

Lower Offset

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__attributes__sem__results__lower__offset_1gab269a3534f8834efa3eb5bf4d606c93a.html language=enus -->
## TOPIC 00037: RFMXEVDO_ATTR_SEM_RESULTS_LOWER_OFFSET_ABSOLUTE_PEAK_POWER

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__attributes__sem__results__lower__offset_1gab269a3534f8834efa3eb5bf4d606c93a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__attributes__sem__results__lower__offset_1gab269a3534f8834efa3eb5bf4d606c93a.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the peak absolute power measured in the lower (negative) offset segment. This value is expressed in dBm. SyntaxRFMXEVDO_ATTR_SEM_RESULTS_LOWER_OFFSET_ABSOLUTE_PEAK_POWERNumeric ValueData TypeAccessApplies To8421430float64Read-OnlyOffsetRemarks Use "offset<i><n></i>" as the Selector String to

### RFMXEVDO_ATTR_SEM_RESULTS_LOWER_OFFSET_ABSOLUTE_PEAK_POWER

Returns the peak absolute power measured in the lower (negative) offset segment. This value is expressed in dBm.

#### Syntax

RFMXEVDO_ATTR_SEM_RESULTS_LOWER_OFFSET_ABSOLUTE_PEAK_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 8421430 | float64 | Read-Only | Offset |

#### Remarks

Use "offset<i><n></i>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this attribute.

Parent topic:

Lower Offset

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__attributes__sem__results__upper__offset_1gabfdd78f94e7882ad3d639ec6795d410d.html language=enus -->
## TOPIC 00038: RFMXEVDO_ATTR_SEM_RESULTS_UPPER_OFFSET_RELATIVE_PEAK_POWER

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__attributes__sem__results__upper__offset_1gabfdd78f94e7882ad3d639ec6795d410d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__attributes__sem__results__upper__offset_1gabfdd78f94e7882ad3d639ec6795d410d.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the peak power measured in the upper (positive) offset segment relative to the integrated power of the reference carrier. This value is expressed in dB. SyntaxRFMXEVDO_ATTR_SEM_RESULTS_UPPER_OFFSET_RELATIVE_PEAK_POWERNumeric ValueData TypeAccessApplies To8421444float64Read-OnlyOffsetRemarks

### RFMXEVDO_ATTR_SEM_RESULTS_UPPER_OFFSET_RELATIVE_PEAK_POWER

Returns the peak power measured in the upper (positive) offset segment relative to the integrated power of the reference carrier. This value is expressed in dB.

#### Syntax

RFMXEVDO_ATTR_SEM_RESULTS_UPPER_OFFSET_RELATIVE_PEAK_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 8421444 | float64 | Read-Only | Offset |

#### Remarks

Use "offset<i><n></i>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this attribute.

Parent topic:

Upper Offset

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__attributes__sem__results__upper__offset_1gad7179dc6efc6a130ea230e78517fa295.html language=enus -->
## TOPIC 00039: RFMXEVDO_ATTR_SEM_RESULTS_UPPER_OFFSET_MEASUREMENT_STATUS

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__attributes__sem__results__upper__offset_1gad7179dc6efc6a130ea230e78517fa295.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__attributes__sem__results__upper__offset_1gad7179dc6efc6a130ea230e78517fa295.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the upper offset measurement status based on measurement limits and the failure criteria specified by the standard. SyntaxRFMXEVDO_ATTR_SEM_RESULTS_UPPER_OFFSET_MEASUREMENT_STATUSNumeric ValueData TypeAccessApplies To8421450int32Read-OnlyOffsetRemarks Use "offset<i><n></i>" as the Selector

### RFMXEVDO_ATTR_SEM_RESULTS_UPPER_OFFSET_MEASUREMENT_STATUS

Indicates the upper offset measurement status based on measurement limits and the failure criteria specified by the standard.

#### Syntax

RFMXEVDO_ATTR_SEM_RESULTS_UPPER_OFFSET_MEASUREMENT_STATUS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 8421450 | int32 | Read-Only | Offset |

#### Remarks

Use "offset<i><n></i>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this attribute.

| Name | Value | Description |
| --- | --- | --- |
| RFMXEVDO_VAL_SEM_UPPER_OFFSET_MEASUREMENT_STATUS_FAIL | 0 (0x0) | The measurement fails. |
| RFMXEVDO_VAL_SEM_UPPER_OFFSET_MEASUREMENT_STATUS_PASS | 1 (0x1) | The measurement passes. |

Parent topic:

Upper Offset

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__attributes__sem__sweep__time_1ga2becb34d0663cf91fcdfb2ecce805e80.html language=enus -->
## TOPIC 00040: RFMXEVDO_ATTR_SEM_SWEEP_TIME_INTERVAL

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__attributes__sem__sweep__time_1ga2becb34d0663cf91fcdfb2ecce805e80.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__attributes__sem__sweep__time_1ga2becb34d0663cf91fcdfb2ecce805e80.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the sweep time when you set the RFMXEVDO_ATTR_SEM_SWEEP_TIME_AUTO attribute to False. This value is expressed in seconds. SyntaxRFMXEVDO_ATTR_SEM_SWEEP_TIME_INTERVALNumeric ValueData TypeAccessApplies To8421414float64Read/WriteN/ARemarks You do not need to use a selector string to configur

### RFMXEVDO_ATTR_SEM_SWEEP_TIME_INTERVAL

Specifies the sweep time when you set the [RFMXEVDO_ATTR_SEM_SWEEP_TIME_AUTO](group____root__ni_r_fmx_e_v_d_o__attributes__sem__sweep__time_1ga69a79ae2b626e2e14dea890936733023.html) attribute to **False**. This value is expressed in seconds.

#### Syntax

RFMXEVDO_ATTR_SEM_SWEEP_TIME_INTERVAL

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 8421414 | float64 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 0.00167 seconds.

Parent topic:

Sweep Time

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__attributes__sem__sweep__time_1ga69a79ae2b626e2e14dea890936733023.html language=enus -->
## TOPIC 00041: RFMXEVDO_ATTR_SEM_SWEEP_TIME_AUTO

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__attributes__sem__sweep__time_1ga69a79ae2b626e2e14dea890936733023.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__attributes__sem__sweep__time_1ga69a79ae2b626e2e14dea890936733023.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement computes the sweep time. SyntaxRFMXEVDO_ATTR_SEM_SWEEP_TIME_AUTONumeric ValueData TypeAccessApplies To8421413int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector

### RFMXEVDO_ATTR_SEM_SWEEP_TIME_AUTO

Specifies whether the measurement computes the sweep time.

#### Syntax

RFMXEVDO_ATTR_SEM_SWEEP_TIME_AUTO

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 8421413 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **True**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXEVDO_VAL_SEM_SWEEP_TIME_AUTO_FALSE | 0 (0x0) | The measurement uses the default sweep time of 1.67 ms. |
| RFMXEVDO_VAL_SEM_SWEEP_TIME_AUTO_TRUE | 1 (0x1) | The measurement calculates the sweep time using a default value. |

Parent topic:

Sweep Time

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__attributes__slotphase.html language=enus -->
## TOPIC 00042: SlotPhase

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__attributes__slotphase.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__attributes__slotphase.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsResultsGroup membersNameDescriptionRFMXEVDO_ATTR_SLOTPHASE_ALL_TRACES_ENABLEDSpecifies whether to enable the traces after performing the SlotPhase measurement. RFMXEVDO_ATTR_SLOTPHASE_MEASUREMENT_ENABLEDSpecifies whether to enable the SlotPhase measurement. RFMXEVDO_ATTR_SLOTPHASE_MEASUREMENT_

### SlotPhase

#### Groups

- Results

#### Group members

| Name | Description |
| --- | --- |
| RFMXEVDO_ATTR_SLOTPHASE_ALL_TRACES_ENABLED | Specifies whether to enable the traces after performing the SlotPhase measurement. |
| RFMXEVDO_ATTR_SLOTPHASE_MEASUREMENT_ENABLED | Specifies whether to enable the SlotPhase measurement. |
| RFMXEVDO_ATTR_SLOTPHASE_MEASUREMENT_LENGTH | Specifies the duration of the SlotPhase measurement. This value is expressed in slots. |
| RFMXEVDO_ATTR_SLOTPHASE_MEASUREMENT_OFFSET | Specifies the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the RFMXEVDO_ATTR_SLOTPHASE_SYNCHRONIZATION_MODEproperty. |
| RFMXEVDO_ATTR_SLOTPHASE_RECEIVE_FILTER_ENABLED | Specifies whether to enable receive filtering. |
| RFMXEVDO_ATTR_SLOTPHASE_SPECTRUM_INVERTED | Specifies whether the signal spectrum is inverted. |
| RFMXEVDO_ATTR_SLOTPHASE_SYNCHRONIZATION_MODE | Specifies whether the measurement is performed from the frame or the slot boundary. |
| RFMXEVDO_ATTR_SLOTPHASE_TRANSIENT_DURATION | Specifies the transient duration for the SlotPhase measurement. This value is expressed in seconds. |

#### Attachments

None

Parent topic:

Attributes

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__attributes__slotphase_1ga8b4df7fdaf93a94a32fe84f4d09591fb.html language=enus -->
## TOPIC 00043: RFMXEVDO_ATTR_SLOTPHASE_RECEIVE_FILTER_ENABLED

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__attributes__slotphase_1ga8b4df7fdaf93a94a32fe84f4d09591fb.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__attributes__slotphase_1ga8b4df7fdaf93a94a32fe84f4d09591fb.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable receive filtering. SyntaxRFMXEVDO_ATTR_SLOTPHASE_RECEIVE_FILTER_ENABLEDNumeric ValueData TypeAccessApplies To8474630int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selecto

### RFMXEVDO_ATTR_SLOTPHASE_RECEIVE_FILTER_ENABLED

Specifies whether to enable receive filtering.

#### Syntax

RFMXEVDO_ATTR_SLOTPHASE_RECEIVE_FILTER_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 8474630 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **True**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXEVDO_VAL_SLOTPHASE_RECEIVE_FILTER_ENABLED_FALSE | 0 (0x0) | Receive filtering is disabled. |
| RFMXEVDO_VAL_SLOTPHASE_RECEIVE_FILTER_ENABLED_TRUE | 1 (0x1) | Receive filtering is enabled. |

Parent topic:

SlotPhase

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__attributes__slotphase_1gab1f784ee502be23e3d7b17e9753911dc.html language=enus -->
## TOPIC 00044: RFMXEVDO_ATTR_SLOTPHASE_MEASUREMENT_LENGTH

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__attributes__slotphase_1gab1f784ee502be23e3d7b17e9753911dc.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__attributes__slotphase_1gab1f784ee502be23e3d7b17e9753911dc.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the duration of the SlotPhase measurement. This value is expressed in slots. SyntaxRFMXEVDO_ATTR_SLOTPHASE_MEASUREMENT_LENGTHNumeric ValueData TypeAccessApplies To8474628int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default s

### RFMXEVDO_ATTR_SLOTPHASE_MEASUREMENT_LENGTH

Specifies the duration of the SlotPhase measurement. This value is expressed in slots.

#### Syntax

RFMXEVDO_ATTR_SLOTPHASE_MEASUREMENT_LENGTH

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 8474628 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 16.

Parent topic:

SlotPhase

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__attributes__slotphase_1gac4b822c51493bc1beea8f0f7088bfd6f.html language=enus -->
## TOPIC 00045: RFMXEVDO_ATTR_SLOTPHASE_MEASUREMENT_ENABLED

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__attributes__slotphase_1gac4b822c51493bc1beea8f0f7088bfd6f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__attributes__slotphase_1gac4b822c51493bc1beea8f0f7088bfd6f.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the SlotPhase measurement. SyntaxRFMXEVDO_ATTR_SLOTPHASE_MEASUREMENT_ENABLEDNumeric ValueData TypeAccessApplies To8474624int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Se

### RFMXEVDO_ATTR_SLOTPHASE_MEASUREMENT_ENABLED

Specifies whether to enable the SlotPhase measurement.

#### Syntax

RFMXEVDO_ATTR_SLOTPHASE_MEASUREMENT_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 8474624 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is FALSE.

Parent topic:

SlotPhase

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__attributes__slotphase__results_1ga68f1ce31d4efa2f14d28b8020021b3b0.html language=enus -->
## TOPIC 00046: RFMXEVDO_ATTR_SLOTPHASE_RESULTS_MAXIMUM_HALF_SLOT_PHASE_DISCONTINUITY

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__attributes__slotphase__results_1ga68f1ce31d4efa2f14d28b8020021b3b0.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__attributes__slotphase__results_1ga68f1ce31d4efa2f14d28b8020021b3b0.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum slot phase discontinuity value observed in the measurement interval. This value is expressed in degrees. SyntaxRFMXEVDO_ATTR_SLOTPHASE_RESULTS_MAXIMUM_HALF_SLOT_PHASE_DISCONTINUITYNumeric ValueData TypeAccessApplies To8474635float64Read-OnlyN/ARemarks You do not need to use a sel

### RFMXEVDO_ATTR_SLOTPHASE_RESULTS_MAXIMUM_HALF_SLOT_PHASE_DISCONTINUITY

Returns the maximum slot phase discontinuity value observed in the measurement interval. This value is expressed in degrees.

#### Syntax

RFMXEVDO_ATTR_SLOTPHASE_RESULTS_MAXIMUM_HALF_SLOT_PHASE_DISCONTINUITY

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 8474635 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for the default signal and result instances. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and named results.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__attributes__slotpower_1ga41456b49cd52201a52f8d06aa566a55b.html language=enus -->
## TOPIC 00047: RFMXEVDO_ATTR_SLOTPOWER_MEASUREMENT_OFFSET

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__attributes__slotpower_1ga41456b49cd52201a52f8d06aa566a55b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__attributes__slotpower_1ga41456b49cd52201a52f8d06aa566a55b.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the RFMXEVDO_ATTR_SLOTPOWER_SYNCHRONIZATION_MODE attribute. SyntaxRFMXEVDO_ATTR_SLOTPOWER_MEASUREMENT_OFFSETNumeric ValueData TypeAccessApplies T

### RFMXEVDO_ATTR_SLOTPOWER_MEASUREMENT_OFFSET

Specifies the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the [RFMXEVDO_ATTR_SLOTPOWER_SYNCHRONIZATION_MODE](group____root__ni_r_fmx_e_v_d_o__attributes__slotpower_1gacc02f7cfcc2d84a293c0ea3c7edf45ea.html) attribute.

#### Syntax

RFMXEVDO_ATTR_SLOTPOWER_MEASUREMENT_OFFSET

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 8470531 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 0.

Parent topic:

SlotPower

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__attributes__slotpower_1ga934744542fe4566bf698878ef8501843.html language=enus -->
## TOPIC 00048: RFMXEVDO_ATTR_SLOTPOWER_MEASUREMENT_LENGTH

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__attributes__slotpower_1ga934744542fe4566bf698878ef8501843.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__attributes__slotpower_1ga934744542fe4566bf698878ef8501843.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the duration of the SlotPower measurement. This value is expressed in slots. SyntaxRFMXEVDO_ATTR_SLOTPOWER_MEASUREMENT_LENGTHNumeric ValueData TypeAccessApplies To8470532int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default s

### RFMXEVDO_ATTR_SLOTPOWER_MEASUREMENT_LENGTH

Specifies the duration of the SlotPower measurement. This value is expressed in slots.

#### Syntax

RFMXEVDO_ATTR_SLOTPOWER_MEASUREMENT_LENGTH

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 8470532 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 16.

Parent topic:

SlotPower

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__attributes__slotpower_1gab66d2ab8d2828be401e01511fcc34cd7.html language=enus -->
## TOPIC 00049: RFMXEVDO_ATTR_SLOTPOWER_SPECTRUM_INVERTED

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__attributes__slotpower_1gab66d2ab8d2828be401e01511fcc34cd7.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__attributes__slotpower_1gab66d2ab8d2828be401e01511fcc34cd7.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the signal spectrum is inverted. SyntaxRFMXEVDO_ATTR_SLOTPOWER_SPECTRUM_INVERTEDNumeric ValueData TypeAccessApplies To8470533int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector

### RFMXEVDO_ATTR_SLOTPOWER_SPECTRUM_INVERTED

Specifies whether the signal spectrum is inverted.

#### Syntax

RFMXEVDO_ATTR_SLOTPOWER_SPECTRUM_INVERTED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 8470533 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **False**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXEVDO_VAL_SLOTPOWER_SPECTRUM_INVERTED_FALSE | 0 (0x0) | The spectrum is not inverted. |
| RFMXEVDO_VAL_SLOTPOWER_SPECTRUM_INVERTED_TRUE | 1 (0x1) | The spectrum is inverted. |

Parent topic:

SlotPower

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__attributes__slotpower_1gacc02f7cfcc2d84a293c0ea3c7edf45ea.html language=enus -->
## TOPIC 00050: RFMXEVDO_ATTR_SLOTPOWER_SYNCHRONIZATION_MODE

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__attributes__slotpower_1gacc02f7cfcc2d84a293c0ea3c7edf45ea.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__attributes__slotpower_1gacc02f7cfcc2d84a293c0ea3c7edf45ea.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement is performed from the frame or the slot boundary. SyntaxRFMXEVDO_ATTR_SLOTPOWER_SYNCHRONIZATION_MODENumeric ValueData TypeAccessApplies To8470530int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default si

### RFMXEVDO_ATTR_SLOTPOWER_SYNCHRONIZATION_MODE

Specifies whether the measurement is performed from the frame or the slot boundary.

#### Syntax

RFMXEVDO_ATTR_SLOTPOWER_SYNCHRONIZATION_MODE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 8470530 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **Slot**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXEVDO_VAL_SLOTPOWER_SYNCHRONIZATION_MODE_FRAME | 0 (0x0) | The frame boundary is detected, and the measurement is performed over the number of slots specified by the RFMXEVDO_ATTR_SLOTPOWER_MEASUREMENT_LENGTH attribute starting at RFMXEVDO_ATTR_SLOTPOWER_MEASUREMENT_OFFSET slots from the frame boundary. |
| RFMXEVDO_VAL_SLOTPOWER_SYNCHRONIZATION_MODE_SLOT | 1 (0x1) | The slot boundary is detected and the measurement is performed over the number of slots specified by the SlotPower Meas Length attribute starting at SlotPower Meas Offset slots from the slot boundary. |

Parent topic:

SlotPower

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__attributes__trigger.html language=enus -->
## TOPIC 00051: Trigger

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__attributes__trigger.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__attributes__trigger.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsDigital EdgeIQ Power EdgeMinimum Quiet TimeGroup membersNameDescriptionRFMXEVDO_ATTR_TRIGGER_DELAYSpecifies the trigger delay time. This value is expressed in seconds. RFMXEVDO_ATTR_TRIGGER_TYPESpecifies the trigger type. AttachmentsNone

### Trigger

#### Groups

- Digital Edge
- IQ Power Edge
- Minimum Quiet Time

#### Group members

| Name | Description |
| --- | --- |
| RFMXEVDO_ATTR_TRIGGER_DELAY | Specifies the trigger delay time. This value is expressed in seconds. |
| RFMXEVDO_ATTR_TRIGGER_TYPE | Specifies the trigger type. |

#### Attachments

None

Parent topic:

Attributes

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__attributes__trigger_1ga0c861b704b4021434e0f4e9fe90d89f5.html language=enus -->
## TOPIC 00052: RFMXEVDO_ATTR_TRIGGER_TYPE

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__attributes__trigger_1ga0c861b704b4021434e0f4e9fe90d89f5.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__attributes__trigger_1ga0c861b704b4021434e0f4e9fe90d89f5.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the trigger type. SyntaxRFMXEVDO_ATTR_TRIGGER_TYPENumeric ValueData TypeAccessApplies To8388612int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information about th

### RFMXEVDO_ATTR_TRIGGER_TYPE

Specifies the trigger type.

#### Syntax

RFMXEVDO_ATTR_TRIGGER_TYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 8388612 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **None**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXEVDO_VAL_TRIGGER_TYPE_NONE | 0 (0x0) | No Reference Trigger is configured. |
| RFMXEVDO_VAL_TRIGGER_TYPE_DIGITAL_EDGE | 1 (0x1) | The Reference Trigger is not asserted until a digital edge is detected. The source of the digital edge is specified using the RFMXEVDO_ATTR_DIGITAL_EDGE_TRIGGER_SOURCE attribute. |
| RFMXEVDO_VAL_TRIGGER_TYPE_IQ_POWER_EDGE | 2 (0x2) | The Reference Trigger is asserted when the signal changes past the level specified by the slope (rising or falling), which is configured using the RFMXEVDO_ATTR_IQ_POWER_EDGE_TRIGGER_SLOPE attribute. |
| RFMXEVDO_VAL_TRIGGER_TYPE_SOFTWARE | 3 (0x3) | The Reference Trigger is not asserted until a software trigger occurs. |

Parent topic:

Trigger

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__attributes__trigger__iq__power__edge.html language=enus -->
## TOPIC 00053: IQ Power Edge

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__attributes__trigger__iq__power__edge.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__attributes__trigger__iq__power__edge.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXEVDO_ATTR_IQ_POWER_EDGE_TRIGGER_LEVELSpecifies the power level at which the device triggers. This value is expressed in dB when the RFMXEVDO_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE attribute is set to Relative and in dBm when the IQ Power Edge Level Type attri

### IQ Power Edge

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXEVDO_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL | Specifies the power level at which the device triggers. This value is expressed in dB when the RFMXEVDO_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE attribute is set to Relative and in dBm when the IQ Power Edge Level Type attribute is set to Absolute. The device asserts the trigger when the signal exceeds the level specified by the value of this attribute, taking into consideration the specified slope. This attribute is used only when you set the RFMXEVDO_ATTR_TRIGGER_TYPE attribute to IQ Power Edge. |
| RFMXEVDO_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE | Specifies the reference for the RFMXEVDO_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL attribute. This attribute is used only when you set the RFMXEVDO_ATTR_TRIGGER_TYPE attribute to IQ Power Edge. |
| RFMXEVDO_ATTR_IQ_POWER_EDGE_TRIGGER_SLOPE | Specifies whether the device asserts the trigger when the signal power is rising or when it is falling. The device asserts the trigger when the signal power exceeds the specified level with the slope you specify. This attribute is used only when you set the RFMXEVDO_ATTR_TRIGGER_TYPE attribute to IQ Power Edge. |
| RFMXEVDO_ATTR_IQ_POWER_EDGE_TRIGGER_SOURCE | Specifies the channel from which the device monitors the trigger. This attribute is used only when you set the RFMXEVDO_ATTR_TRIGGER_TYPE attribute to IQ Power Edge. |

#### Attachments

None

Parent topic:

Trigger

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__attributes__trigger__iq__power__edge_1ga0bf05a95afa24d6627a13bb63f2ef88a.html language=enus -->
## TOPIC 00054: RFMXEVDO_ATTR_IQ_POWER_EDGE_TRIGGER_SOURCE

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__attributes__trigger__iq__power__edge_1ga0bf05a95afa24d6627a13bb63f2ef88a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__attributes__trigger__iq__power__edge_1ga0bf05a95afa24d6627a13bb63f2ef88a.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the channel from which the device monitors the trigger. This attribute is used only when you set the RFMXEVDO_ATTR_TRIGGER_TYPE attribute to IQ Power Edge. SyntaxRFMXEVDO_ATTR_IQ_POWER_EDGE_TRIGGER_SOURCENumeric ValueData TypeAccessApplies To8388615char[]Read/WriteN/ARemarks You do not nee

### RFMXEVDO_ATTR_IQ_POWER_EDGE_TRIGGER_SOURCE

Specifies the channel from which the device monitors the trigger. This attribute is used only when you set the [RFMXEVDO_ATTR_TRIGGER_TYPE](group____root__ni_r_fmx_e_v_d_o__attributes__trigger_1ga0c861b704b4021434e0f4e9fe90d89f5.html) attribute to **IQ Power Edge**.

#### Syntax

RFMXEVDO_ATTR_IQ_POWER_EDGE_TRIGGER_SOURCE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 8388615 | char[] | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default of this attribute is hardware dependent.

Parent topic:

IQ Power Edge

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__functions_1gaccaec841794030fe0dda93eb76bb7e60.html language=enus -->
## TOPIC 00055: RFmxEVDO_GetError

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__functions_1gaccaec841794030fe0dda93eb76bb7e60.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__functions_1gaccaec841794030fe0dda93eb76bb7e60.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Retrieves and then clears the error information for the session or the current execution thread. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the errorDescriptionBufferSize parameter. Syntaxint32 __stdcall RFmxEVDO_GetError(niRFmxInstrHa

### RFmxEVDO_GetError

Retrieves and then clears the error information for the session or the current execution thread. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **errorDescriptionBufferSize** parameter.

#### Syntax

int32 __stdcall RFmxEVDO_GetError(niRFmxInstrHandle instrumentHandle, int32 *errorCode, int32 errorDescriptionBufferSize, char errorDescription[])

#### Remarks

If the error description, including the terminating NULL byte, is larger than the size you indicate in the **errorDescriptionBufferSize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

If you want to call this function just to get the required buffer size, you must pass 0 for **errorDescriptionBufferSize** and NULL for the errorDescription buffer.

Note

Use the [RFmxEVDO_GetErrorString](group____root__ni_r_fmx_e_v_d_o__functions_1ga909486601d1a4de4a51c005671a1cf61.html) function if the [RFmxEVDO_GetError](group____root__ni_r_fmx_e_v_d_o__functions_1gaccaec841794030fe0dda93eb76bb7e60.html) function does not return an error message.

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

To obtain a text description of the status code and additional information about the error condition, call the [RFmxEVDO_GetError](group____root__ni_r_fmx_e_v_d_o__functions_1gaccaec841794030fe0dda93eb76bb7e60.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__functions__advanced.html language=enus -->
## TOPIC 00056: Advanced

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__functions__advanced.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__functions__advanced.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsAnalyze2Group membersNameDescriptionRFmxEVDO_AbortMeasurementsStops acquisition and measurements associated with the signal instance that you specify in the Selector String parameter. These measurements were previously initiated by the RFmxEVDO_Initiate function or measurement read functions.

### Advanced

#### Groups

- Analyze2

#### Group members

| Name | Description |
| --- | --- |
| RFmxEVDO_AbortMeasurements | Stops acquisition and measurements associated with the signal instance that you specify in the Selector String parameter. These measurements were previously initiated by the RFmxEVDO_Initiate function or measurement read functions. Calling this function is optional, unless you want to stop a measurement before it is complete. This function executes even if there is an incoming error. |
| RFmxEVDO_ClearAllNamedResults | Clears all results for the signal that you specify in the Selector String parameter. |
| RFmxEVDO_ClearNamedResult | Clears a result instance specified by the result name in the Selector String parameter. |
| RFmxEVDO_CloneSignalConfiguration | Creates a new instance of a signal by copying all the attribute values from an existing signal instance. |
| RFmxEVDO_CreateSignalConfiguration | Creates a new instance of a signal. |
| RFmxEVDO_DeleteSignalConfiguration | Deletes an instance of a signal that you specify in the Signal Name parameter. |
| RFmxEVDO_GetAllNamedResultNames | Returns the named result names of the signal that you specify in the Selector String parameter. |

#### Attachments

None

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__functions__advanced_1ga1115d2975d7ff031265219a6922bc987.html language=enus -->
## TOPIC 00057: RFmxEVDO_DeleteSignalConfiguration

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__functions__advanced_1ga1115d2975d7ff031265219a6922bc987.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__functions__advanced_1ga1115d2975d7ff031265219a6922bc987.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Deletes an instance of a signal that you specify in the Signal Name parameter. Syntaxint32 __stdcall RFmxEVDO_DeleteSignalConfiguration(niRFmxInstrHandle instrumentHandle, char signalName[])ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifies the RFmx s

### RFmxEVDO_DeleteSignalConfiguration

Deletes an instance of a signal that you specify in the **Signal Name** parameter.

#### Syntax

int32 __stdcall RFmxEVDO_DeleteSignalConfiguration(niRFmxInstrHandle instrumentHandle, char signalName[])

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| signalName | [in] | char[] | This parameter specifies the name of the signal. This input accepts the signal name with or without the "signal::" prefix.Example:"signal::sig1""sig1" |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxEVDO_GetError](group____root__ni_r_fmx_e_v_d_o__functions_1gaccaec841794030fe0dda93eb76bb7e60.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__functions__advanced_1ga5db209e6849b998a3d9f4eafd15c63ee.html language=enus -->
## TOPIC 00058: RFmxEVDO_AbortMeasurements

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__functions__advanced_1ga5db209e6849b998a3d9f4eafd15c63ee.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__functions__advanced_1ga5db209e6849b998a3d9f4eafd15c63ee.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Stops acquisition and measurements associated with the signal instance that you specify in the Selector String parameter. These measurements were previously initiated by the RFmxEVDO_Initiate function or measurement read functions. Calling this function is optional, unless you want to stop a measure

### RFmxEVDO_AbortMeasurements

Stops acquisition and measurements associated with the signal instance that you specify in the **Selector String** parameter. These measurements were previously initiated by the [RFmxEVDO_Initiate](group____root__ni_r_fmx_e_v_d_o__functions_1ga2f3a9ce0c3ea8d1cfbd59d3140ed2725.html) function or measurement read functions. Calling this function is optional, unless you want to stop a measurement before it is complete. This function executes even if there is an incoming error.

#### Syntax

int32 __stdcall RFmxEVDO_AbortMeasurements(niRFmxInstrHandle instrumentHandle, char selectorString[])

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Examples:"""signal::sig1"You can use the RFmxEVDO_BuildSignalString function to build the selector string. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxEVDO_GetError](group____root__ni_r_fmx_e_v_d_o__functions_1gaccaec841794030fe0dda93eb76bb7e60.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__functions__advanced_1ga803c447cabb510bd23b6f045e41cd17f.html language=enus -->
## TOPIC 00059: RFmxEVDO_CreateSignalConfiguration

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__functions__advanced_1ga803c447cabb510bd23b6f045e41cd17f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__functions__advanced_1ga803c447cabb510bd23b6f045e41cd17f.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a new instance of a signal. Syntaxint32 __stdcall RFmxEVDO_CreateSignalConfiguration(niRFmxInstrHandle instrumentHandle, char signalName[])ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifies the RFmx session refnum. This parameter is obtained f

### RFmxEVDO_CreateSignalConfiguration

Creates a new instance of a signal.

#### Syntax

int32 __stdcall RFmxEVDO_CreateSignalConfiguration(niRFmxInstrHandle instrumentHandle, char signalName[])

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| signalName | [in] | char[] | This parameter specifies the name of the signal. This input accepts the signal name with or without the "signal::" prefix.Example:"signal::sig1""sig1" |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxEVDO_GetError](group____root__ni_r_fmx_e_v_d_o__functions_1gaccaec841794030fe0dda93eb76bb7e60.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__functions__advanced_1gacfcbde64b074027180b193c53b8c4e65.html language=enus -->
## TOPIC 00060: RFmxEVDO_GetAllNamedResultNames

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__functions__advanced_1gacfcbde64b074027180b193c53b8c4e65.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__functions__advanced_1gacfcbde64b074027180b193c53b8c4e65.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the named result names of the signal that you specify in the Selector String parameter. Syntaxint32 __stdcall RFmxEVDO_GetAllNamedResultNames(niRFmxInstrHandle instrumentHandle, char selectorString[], char resultNames[], int32 resultNamesBufferSize, int32 *actualResultNamesSize, int32 *defau

### RFmxEVDO_GetAllNamedResultNames

Returns the named result names of the signal that you specify in the **Selector String** parameter.

#### Syntax

int32 __stdcall RFmxEVDO_GetAllNamedResultNames(niRFmxInstrHandle instrumentHandle, char selectorString[], char resultNames[], int32 resultNamesBufferSize, int32 *actualResultNamesSize, int32 *defaultResultExists)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Examples:"""signal::sig1"You can use the RFmxEVDO_BuildSignalString function to build the selector string. |
| resultNames | [out] | char[] | This parameter returns an array of result names. |
| resultNamesBufferSize | [in] | int32 | Specifies the size of the resultNames array. Set the resultNamesBufferSize parameter to 0 to get the size of the resultNames array in the return value. |
| actualResultNamesSize | [out] | int32 * | Returns the actual size of the resultNames array, if you pass NULL to resultNames array parameter and set the resultNamesBufferSize parameter to 0. |
| defaultResultExists | [out] | int32 * | This parameter indicates whether the default result exists. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxEVDO_GetError](group____root__ni_r_fmx_e_v_d_o__functions_1gaccaec841794030fe0dda93eb76bb7e60.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__functions__advanced__analyze2.html language=enus -->
## TOPIC 00061: Analyze2

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__functions__advanced__analyze2.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__functions__advanced__analyze2.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxEVDO_AnalyzeIQ1WaveformPerforms the enabled measurements on the I/Q complex waveform that you specify in IQ parameter. Call this function after you configure the signal and measurement attributes. You can fetch measurement results using the Fetch functions o

### Analyze2

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxEVDO_AnalyzeIQ1Waveform | Performs the enabled measurements on the I/Q complex waveform that you specify in IQ parameter. Call this function after you configure the signal and measurement attributes. You can fetch measurement results using the Fetch functions or result attributes in the attribute node. Use this function only if the RFMXINSTR_ATTR_RECOMMENDED_ACQUISITION_TYPE attribute value is either IQ or IQ or Spectral. |
| RFmxEVDO_AnalyzeIQ1WaveformSplit | Performs the enabled measurements on the I/Q complex waveform that you specify in IQ parameter. Call this function after you configure the signal and measurement attributes. You can fetch measurement results using the Fetch functions or result attributes in the attribute node. Use this function only if the RFMXINSTR_ATTR_RECOMMENDED_ACQUISITION_TYPE attribute value is either IQ or IQ or Spectral. |
| RFmxEVDO_AnalyzeSpectrum1Waveform | Performs the enabled measurements on the spectrum waveform that you specify in the Spectrum parameter. Call this function after you configure the signal and measurement attributes. You can fetch measurement results using the Fetch functions or result attributes in the attribute node. Use this function only if the RFMXINSTR_ATTR_RECOMMENDED_ACQUISITION_TYPE attribute value is either Spectral or IQ or Spectral. |

#### Attachments

None

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__functions__advanced__analyze2_1ga74a7762f04c2a512f20cf83b023acab2.html language=enus -->
## TOPIC 00062: RFmxEVDO_AnalyzeIQ1WaveformSplit

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__functions__advanced__analyze2_1ga74a7762f04c2a512f20cf83b023acab2.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__functions__advanced__analyze2_1ga74a7762f04c2a512f20cf83b023acab2.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs the enabled measurements on the I/Q complex waveform that you specify in IQ parameter. Call this function after you configure the signal and measurement attributes. You can fetch measurement results using the Fetch functions or result attributes in the attribute node. Use this function only

### RFmxEVDO_AnalyzeIQ1WaveformSplit

Performs the enabled measurements on the I/Q complex waveform that you specify in **IQ** parameter. Call this function after you configure the signal and measurement attributes. You can fetch measurement results using the Fetch functions or result attributes in the attribute node. Use this function only if the [RFMXINSTR_ATTR_RECOMMENDED_ACQUISITION_TYPE](/csh?context=rfmxinstr_rfmxinstrcref_attribute_recommended_acquisition_type) attribute value is either **IQ** or **IQ or Spectral**.

#### Syntax

int32 __stdcall RFmxEVDO_AnalyzeIQ1WaveformSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], char resultName[], float64 x0, float64 dx, float32 iqI[], float32 iqQ[], int32 arraySize, int32 reset, int64 reserved)

#### Remarks

Note

Query the Recommended Acquisition Type attribute from the RFmxInstr Attribute after calling the [RFmxEVDO_Commit](group____root__ni_r_fmx_e_v_d_o__functions__utility_1gaeb5ed8f7c156dcb1332a2f45ca0576aa.html) function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function or the RFmxInstr Initialize function with option string as "AnalysisOnly=1". |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and the result name. The result name can be specified either through this input or through the Result Name parameter. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name in this parameter, either the result name specified by the Result Name parameter or the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxEVDO_BuildSignalString function to build the selector string. |
| resultName | [in] | char[] | This parameter specifies the name to be associated with measurement results. Provide a unique name, such as "r1", to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. The default value is "" (empty string), which refers to default result instance.Example:"""result::r1""r1" |
| x0 | [in] | float64 | This parameter specifies the start time of the input Y array. This value is expressed in seconds. |
| dx | [in] | float64 | This parameter specifies the time interval between the samples in the input Y array. This value is expressed in seconds. The reciprocal of dx indicates the I/Q rate of the input signal. |
| iqI | [in] | float32[] | This parameter specifies an array of complex-valued time domain data. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively. |
| iqQ | [in] | float32[] | This parameter specifies an array of complex-valued time domain data. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively. |
| arraySize | [in] | int32 | Specifies the size of the array. |
| reset | [in] | int32 | This parameter resets measurement averaging. If you enable averaging, set this parameter to TRUE for first record and FALSE for subsequent records. |
| reserved | [in] | int64 | Reserved for future use. Any value passed to this parameter will be ignored. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxEVDO_GetError](group____root__ni_r_fmx_e_v_d_o__functions_1gaccaec841794030fe0dda93eb76bb7e60.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Analyze2

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__functions__advanced__analyze2_1gaa4d139084dd9f458fc8ebb02f0c20345.html language=enus -->
## TOPIC 00063: RFmxEVDO_AnalyzeSpectrum1Waveform

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__functions__advanced__analyze2_1gaa4d139084dd9f458fc8ebb02f0c20345.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__functions__advanced__analyze2_1gaa4d139084dd9f458fc8ebb02f0c20345.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs the enabled measurements on the spectrum waveform that you specify in the Spectrum parameter. Call this function after you configure the signal and measurement attributes. You can fetch measurement results using the Fetch functions or result attributes in the attribute node. Use this functi

### RFmxEVDO_AnalyzeSpectrum1Waveform

Performs the enabled measurements on the spectrum waveform that you specify in the **Spectrum** parameter. Call this function after you configure the signal and measurement attributes. You can fetch measurement results using the Fetch functions or result attributes in the attribute node. Use this function only if the [RFMXINSTR_ATTR_RECOMMENDED_ACQUISITION_TYPE](/csh?context=rfmxinstr_rfmxinstrcref_attribute_recommended_acquisition_type) attribute value is either **Spectral** or **IQ or Spectral**.

#### Syntax

int32 __stdcall RFmxEVDO_AnalyzeSpectrum1Waveform(niRFmxInstrHandle instrumentHandle, char selectorString[], char resultName[], float64 x0, float64 dx, float32 spectrum[], int32 arraySize, int32 reset, int64 reserved)

#### Remarks

Note

Query the Recommended Acquisition Type attribute from the RFmxInstr Attribute after calling the [RFmxEVDO_Commit](group____root__ni_r_fmx_e_v_d_o__functions__utility_1gaeb5ed8f7c156dcb1332a2f45ca0576aa.html) function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function or the RFmxInstr Initialize function with option string as "AnalysisOnly=1". |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and the result name. The result name can be specified either through this input or through the Result Name parameter. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name in this parameter, either the result name specified by the Result Name parameter or the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxEVDO_BuildSignalString function to build the selector string. |
| resultName | [in] | char[] | This parameter specifies the name to be associated with measurement results. Provide a unique name, such as "r1", to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. The default value is "" (empty string), which refers to default result instance.Example:"""result::r1""r1" |
| x0 | [in] | float64 | This parameter specifies the start frequency of the spectrum. This value is expressed in Hz. |
| dx | [in] | float64 | This parameter specifies the frequency interval between data points in the spectrum. |
| spectrum | [in] | float32[] | This parameter contains the real-value power spectrum. |
| arraySize | [in] | int32 | Specifies the size of the array. |
| reset | [in] | int32 | This parameter resets measurement averaging. If you enable averaging, set this parameter to TRUE for first record and FALSE for subsequent records. |
| reserved | [in] | int64 | Reserved for future use. Any value passed to this parameter will be ignored. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxEVDO_GetError](group____root__ni_r_fmx_e_v_d_o__functions_1gaccaec841794030fe0dda93eb76bb7e60.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Analyze2

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__functions__build__string.html language=enus -->
## TOPIC 00064: Build String

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__functions__build__string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__functions__build__string.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxEVDO_BuildCarrierStringCreates the carrier string to use as the selector string with the adjacent channel power (ACP), channel power (CHP), and spectral emission mask (SEM) carrier configuration or fetch attributes and functions. RFmxEVDO_BuildChannelStringC

### Build String

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxEVDO_BuildCarrierString | Creates the carrier string to use as the selector string with the adjacent channel power (ACP), channel power (CHP), and spectral emission mask (SEM) carrier configuration or fetch attributes and functions. |
| RFmxEVDO_BuildChannelString | Creates the channel string to use as the selector string with the modulation accuracy (ModAcc) channel configuration or fetch attributes and functions. |
| RFmxEVDO_BuildOffsetString | Creates the offset string to use as the selector string with adjacent channel power (ACP) and spectral emission mask (SEM) offset configuration or fetch attributes and functions. |
| RFmxEVDO_BuildSignalString | Creates a selector string for use with configuration or fetch attributes and functions. |

#### Attachments

None

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__functions__build__string_1ga18049cc166f081a5ed4a6783b0cee89d.html language=enus -->
## TOPIC 00065: RFmxEVDO_BuildSignalString

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__functions__build__string_1ga18049cc166f081a5ed4a6783b0cee89d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__functions__build__string_1ga18049cc166f081a5ed4a6783b0cee89d.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a selector string for use with configuration or fetch attributes and functions. Syntaxint32 __stdcall RFmxEVDO_BuildSignalString(char signalName[], char resultName[], int32 selectorStringLength, char selectorString[])RemarksRefer to the Selector String topic for information about the string

### RFmxEVDO_BuildSignalString

Creates a selector string for use with configuration or fetch attributes and functions.

#### Syntax

int32 __stdcall RFmxEVDO_BuildSignalString(char signalName[], char resultName[], int32 selectorStringLength, char selectorString[])

#### Remarks

Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| signalName | [in] | char[] | This parameter specifies the name of the signal when using named signal configurations. This input accepts the signal name with or without the "signal::" prefix. The default value is "" (empty string).Examples:"""signal::sig1""sig1" |
| resultName | [in] | char[] | This parameter specifies the name of the result when performing Named Results. This input accepts the result name with or without the "result::" prefix. The default value is "" (empty string).Examples:"""result::r1""r1" |
| selectorStringLength | [in] | int32 | Specifies the length of the selector string. Set this parameter to 0 to get the minimum buffer size required to build the selector string. |
| selectorString | [in] | char[] | This parameter returns the selector string you can use in the Selector String input parameter for Configuration functions, Fetch functions, or other functions that build selector strings. This string contains the signal and/or result names with their appropriate prefixes.Examples:"""signal::sig1""result::r1""signal::sig1/result::r1" |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxEVDO_GetError](group____root__ni_r_fmx_e_v_d_o__functions_1gaccaec841794030fe0dda93eb76bb7e60.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Build String

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__functions__build__string_1ga7d371ab81cc8ee7e99d715fe2dbbfc72.html language=enus -->
## TOPIC 00066: RFmxEVDO_BuildCarrierString

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__functions__build__string_1ga7d371ab81cc8ee7e99d715fe2dbbfc72.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__functions__build__string_1ga7d371ab81cc8ee7e99d715fe2dbbfc72.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates the carrier string to use as the selector string with the adjacent channel power (ACP), channel power (CHP), and spectral emission mask (SEM) carrier configuration or fetch attributes and functions. Syntaxint32 __stdcall RFmxEVDO_BuildCarrierString(char selectorString[], int32 carrierNumber,

### RFmxEVDO_BuildCarrierString

Creates the carrier string to use as the selector string with the adjacent channel power (ACP), channel power (CHP), and spectral emission mask (SEM) carrier configuration or fetch attributes and functions.

#### Syntax

int32 __stdcall RFmxEVDO_BuildCarrierString(char selectorString[], int32 carrierNumber, int32 selectorStringOutLength, char selectorStringOut[])

#### Remarks

Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxEVDO_BuildSignalString function to build the selector string. |
| carrierNumber | [in] | int32 | This parameter specifies the carrier number for building the selector string. |
| selectorStringOutLength | [out] | int32 | Specifies the length of the string that is returned by the selectorStringOut parameter. To get the minimum buffer size required to build the selector string, set the selectorStringOutLength parameter to 0. |
| selectorStringOut | [out] | char[] | This parameter returns the selector string you can use in the Selector String input parameter for Configuration functions, Fetch functions, or the RFmxEVDO_Initiate function. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxEVDO_GetError](group____root__ni_r_fmx_e_v_d_o__functions_1gaccaec841794030fe0dda93eb76bb7e60.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Build String

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__functions__configuration_1ga8c4ab14e7bfbfa98828e21a2ec4df391.html language=enus -->
## TOPIC 00067: RFmxEVDO_CfgUplinkNumberOfChannels

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__functions__configuration_1ga8c4ab14e7bfbfa98828e21a2ec4df391.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__functions__configuration_1ga8c4ab14e7bfbfa98828e21a2ec4df391.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the number of channels in the EV-DO uplink. Syntaxint32 __stdcall RFmxEVDO_CfgUplinkNumberOfChannels(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 uplinkNumberOfChannels)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifies

### RFmxEVDO_CfgUplinkNumberOfChannels

Configures the number of channels in the EV-DO uplink.

#### Syntax

int32 __stdcall RFmxEVDO_CfgUplinkNumberOfChannels(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 uplinkNumberOfChannels)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Examples:"""signal::sig1"You can use the RFmxEVDO_BuildSignalString function to build the selector string. |
| uplinkNumberOfChannels | [in] | int32 | This parameter specifies the number of user-defined channels. The default value is 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxEVDO_GetError](group____root__ni_r_fmx_e_v_d_o__functions_1gaccaec841794030fe0dda93eb76bb7e60.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__functions__configuration_1ga9f61121c152d44b97d7542193fed6b4b.html language=enus -->
## TOPIC 00068: RFmxEVDO_CfgNumberOfCarriers

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__functions__configuration_1ga9f61121c152d44b97d7542193fed6b4b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__functions__configuration_1ga9f61121c152d44b97d7542193fed6b4b.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the number of carriers for the analysis of the EV-DO signal. Syntaxint32 __stdcall RFmxEVDO_CfgNumberOfCarriers(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 numberOfCarriers)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter speci

### RFmxEVDO_CfgNumberOfCarriers

Configures the number of carriers for the analysis of the EV-DO signal.

#### Syntax

int32 __stdcall RFmxEVDO_CfgNumberOfCarriers(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 numberOfCarriers)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Examples:"""signal::sig1"You can use the RFmxEVDO_BuildSignalString function to build the selector string. |
| numberOfCarriers | [in] | int32 | This parameter specifies the number of carriers in the signal. The default value is 1. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxEVDO_GetError](group____root__ni_r_fmx_e_v_d_o__functions_1gaccaec841794030fe0dda93eb76bb7e60.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__functions__configuration_1gae7012ea61ae08e52382cbda92568333a.html language=enus -->
## TOPIC 00069: RFmxEVDO_CfgExternalAttenuation

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__functions__configuration_1gae7012ea61ae08e52382cbda92568333a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__functions__configuration_1gae7012ea61ae08e52382cbda92568333a.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies external attenuation to be considered by RFmx EV-DO measurements, such as the attenuation of a switch or cable connected to the signal analyzer RF IN connector. Syntaxint32 __stdcall RFmxEVDO_CfgExternalAttenuation(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 external

### RFmxEVDO_CfgExternalAttenuation

Specifies external attenuation to be considered by RFmx EV-DO measurements, such as the attenuation of a switch or cable connected to the signal analyzer RF IN connector.

#### Syntax

int32 __stdcall RFmxEVDO_CfgExternalAttenuation(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 externalAttenuation)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Examples:"""signal::sig1"You can use the RFmxEVDO_BuildSignalString function to build the selector string. |
| externalAttenuation | [in] | float64 | This parameter specifies external attenuation to be considered by RFmx EV-DO measurements, such as the attenuation of a switch or cable connected to the RF signal analyzer RF IN connector.For more information about attenuation, refer to the Attenuation and Signal Levels topic for your device in the NI RF Vector Signal Analyzers Help. The default value is 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxEVDO_GetError](group____root__ni_r_fmx_e_v_d_o__functions_1gaccaec841794030fe0dda93eb76bb7e60.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__functions__configuration__acp.html language=enus -->
## TOPIC 00070: ACP

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__functions__configuration__acp.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__functions__configuration__acp.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxEVDO_ACPCfgAveragingConfigures averaging for the adjacent channel power (ACP) measurement. RFmxEVDO_ACPCfgMeasurementMethodConfigures the method for performing the adjacent channel power (ACP) measurement. RFmxEVDO_ACPCfgNoiseCompensationEnabledConfigures co

### ACP

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxEVDO_ACPCfgAveraging | Configures averaging for the adjacent channel power (ACP) measurement. |
| RFmxEVDO_ACPCfgMeasurementMethod | Configures the method for performing the adjacent channel power (ACP) measurement. |
| RFmxEVDO_ACPCfgNoiseCompensationEnabled | Configures compensation of the channel powers for the inherent noise floor of the signal analyzer. |
| RFmxEVDO_ACPCfgNumberOfOffsets | Configures the number of offset channel pairs for the adjacent channel power (ACP) measurement. Channel pairs consist of upper and lower offset channels. |
| RFmxEVDO_ACPCfgOffsetPowerReference | Configures the power reference of the offset channels in multi-carrier setups. |
| RFmxEVDO_ACPCfgRBWFilter | Configures the resolution bandwidth (RBW) filter. |
| RFmxEVDO_ACPCfgSweepTime | Configures the sweep time. |

#### Attachments

None

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__functions__configuration__cda_1ga3e512433c0290a4f3c903ba185317b17.html language=enus -->
## TOPIC 00071: RFmxEVDO_CDACfgUplinkMeasurementChannel

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__functions__configuration__cda_1ga3e512433c0290a4f3c903ba185317b17.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__functions__configuration__cda_1ga3e512433c0290a4f3c903ba185317b17.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the spreading factor, spreading code, modulation type, and branch of the channel to be measured. Syntaxint32 __stdcall RFmxEVDO_CDACfgUplinkMeasurementChannel(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 walshCodeLength, int32 walshCodeNumber, int32 branch)ParametersNa

### RFmxEVDO_CDACfgUplinkMeasurementChannel

Configures the spreading factor, spreading code, modulation type, and branch of the channel to be measured.

#### Syntax

int32 __stdcall RFmxEVDO_CDACfgUplinkMeasurementChannel(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 walshCodeLength, int32 walshCodeNumber, int32 branch)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Examples:"""signal::sig1"You can use the RFmxEVDO_BuildSignalString function to build the selector string. |
| walshCodeLength | [in] | int32 | This parameter specifies the Walsh code length of the channel, subject to channel-specific analysis. The default value is 16. Valid values are 2, 4, 8, 16, and 32. |
| walshCodeNumber | [in] | int32 | This parameter specifies the Walsh code number of the channel, subject to channel-specific analysis. The default value is 0. The maximum value is 31. |
| branch | [in] | int32 | This parameter specifies the Walsh branch of the channel, subject to channel-specific analysis. The default value is I.NameValueDescriptionRFMXEVDO_VAL_CDA_UPLINK_BRANCH_I0 (0x0)Specifies the in-phase branch.RFMXEVDO_VAL_CDA_UPLINK_BRANCH_Q1 (0x1)Specifies the quadrature branch.RFMXEVDO_VAL_CDA_UPLINK_BRANCH_I_AND_Q2 (0x2)Specifies the in-phase and quadrature branch. |
| Name | Value | Description |  |
| RFMXEVDO_VAL_CDA_UPLINK_BRANCH_I | 0 (0x0) | Specifies the in-phase branch. |  |
| RFMXEVDO_VAL_CDA_UPLINK_BRANCH_Q | 1 (0x1) | Specifies the quadrature branch. |  |
| RFMXEVDO_VAL_CDA_UPLINK_BRANCH_I_AND_Q | 2 (0x2) | Specifies the in-phase and quadrature branch. |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxEVDO_GetError](group____root__ni_r_fmx_e_v_d_o__functions_1gaccaec841794030fe0dda93eb76bb7e60.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

CDA

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__functions__configuration__chp_1gac2912e24711a74be0112dfea166bd784.html language=enus -->
## TOPIC 00072: RFmxEVDO_CHPCfgSweepTime

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__functions__configuration__chp_1gac2912e24711a74be0112dfea166bd784.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__functions__configuration__chp_1gac2912e24711a74be0112dfea166bd784.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the sweep time. Syntaxint32 __stdcall RFmxEVDO_CHPCfgSweepTime(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 sweepTimeAuto, float64 sweepTimeInterval)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifies the RFmx session ref

### RFmxEVDO_CHPCfgSweepTime

Configures the sweep time.

#### Syntax

int32 __stdcall RFmxEVDO_CHPCfgSweepTime(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 sweepTimeAuto, float64 sweepTimeInterval)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Examples:"""signal::sig1"You can use the RFmxEVDO_BuildSignalString function to build the selector string. |
| sweepTimeAuto | [in] | int32 | This parameter specifies whether the measurement calculates the sweep time. The default value is True.Name (value)DescriptionFalse (0)The measurement uses the sweep time that you specify using the Sweep Time Interval parameter.True (1)The measurement uses the default sweep time of 1.67 ms. |
| Name (value) | Description |  |  |
| False (0) | The measurement uses the sweep time that you specify using the Sweep Time Interval parameter. |  |  |
| True (1) | The measurement uses the default sweep time of 1.67 ms. |  |  |
| sweepTimeInterval | [in] | float64 | This parameter specifies the sweep time when you set the Sweep Time Auto parameter to False. This value is expressed in seconds. The default value is 1.67 ms. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxEVDO_GetError](group____root__ni_r_fmx_e_v_d_o__functions_1gaccaec841794030fe0dda93eb76bb7e60.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

CHP

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__functions__configuration__frequency.html language=enus -->
## TOPIC 00073: Frequency

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__functions__configuration__frequency.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__functions__configuration__frequency.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxEVDO_CfgFrequencyConfigures the expected carrier frequency of the RF signal to acquire. The signal analyzer tunes to this frequency. RFmxEVDO_CfgFrequencyChannelNumberConfigures the expected carrier frequency of the RF signal to acquire according to the give

### Frequency

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxEVDO_CfgFrequency | Configures the expected carrier frequency of the RF signal to acquire. The signal analyzer tunes to this frequency. |
| RFmxEVDO_CfgFrequencyChannelNumber | Configures the expected carrier frequency of the RF signal to acquire according to the given channel number. The signal analyzer tunes to this frequency. |

#### Attachments

None

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__functions__configuration__frequency_1gaefc5670e5f1cfd000118f58392c5743d.html language=enus -->
## TOPIC 00074: RFmxEVDO_CfgFrequency

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__functions__configuration__frequency_1gaefc5670e5f1cfd000118f58392c5743d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__functions__configuration__frequency_1gaefc5670e5f1cfd000118f58392c5743d.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the expected carrier frequency of the RF signal to acquire. The signal analyzer tunes to this frequency. Syntaxint32 __stdcall RFmxEVDO_CfgFrequency(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 centerFrequency)ParametersNameDirectionTypeDescriptioninstrumentHandle[in

### RFmxEVDO_CfgFrequency

Configures the expected carrier frequency of the RF signal to acquire. The signal analyzer tunes to this frequency.

#### Syntax

int32 __stdcall RFmxEVDO_CfgFrequency(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 centerFrequency)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Examples:"""signal::sig1"You can use the RFmxEVDO_BuildSignalString function to build the selector string. |
| centerFrequency | [in] | float64 | This parameter specifies the expected carrier frequency of the RF signal to acquire. This value is expressed in Hz. The RF signal analyzer tunes to this frequency. The default of this parameter is hardware dependent. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxEVDO_GetError](group____root__ni_r_fmx_e_v_d_o__functions_1gaccaec841794030fe0dda93eb76bb7e60.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Frequency

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__functions__configuration__frequency_1gaefeaab4392ea48ad4583b71438034e89.html language=enus -->
## TOPIC 00075: RFmxEVDO_CfgFrequencyChannelNumber

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__functions__configuration__frequency_1gaefeaab4392ea48ad4583b71438034e89.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__functions__configuration__frequency_1gaefeaab4392ea48ad4583b71438034e89.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the expected carrier frequency of the RF signal to acquire according to the given channel number. The signal analyzer tunes to this frequency. Syntaxint32 __stdcall RFmxEVDO_CfgFrequencyChannelNumber(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 linkDirection, int32 ban

### RFmxEVDO_CfgFrequencyChannelNumber

Configures the expected carrier frequency of the RF signal to acquire according to the given channel number. The signal analyzer tunes to this frequency.

#### Syntax

int32 __stdcall RFmxEVDO_CfgFrequencyChannelNumber(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 linkDirection, int32 bandClass, int32 channelNumber)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Examples:"""signal::sig1"You can use the RFmxEVDO_BuildSignalString function to build the selector string. |
| linkDirection | [in] | int32 | This parameter specifies which direction the frequency is calculated. Currently, only Uplink is supported.Name (value)DescriptionUplink (1)The frequency is calculated in the reverse link direction, also know as the uplink direction. |
| Name (value) | Description |  |  |
| Uplink (1) | The frequency is calculated in the reverse link direction, also know as the uplink direction. |  |  |
| bandClass | [in] | int32 | This parameter specifies the band in which the channel is located as defined in Section: 1.5, Table 1.5-1: Band Class List, of the 3GPP2 C.S0057-F specification v1.0. Valid values range between 0 and 15, inclusive. |
| channelNumber | [in] | int32 | This parameter is the absolute RF channel number. The valid range for this parameter depends on the value you specify for the Band parameter. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxEVDO_GetError](group____root__ni_r_fmx_e_v_d_o__functions_1gaccaec841794030fe0dda93eb76bb7e60.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Frequency

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__functions__configuration__modacc.html language=enus -->
## TOPIC 00076: ModAcc

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__functions__configuration__modacc.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__functions__configuration__modacc.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxEVDO_ModAccCfgMultiCarrierFilterEnabledEnables or disables the multicarrier filter. In multicarrier setups, EVM values are higher than in single carrier setups. The multicarrier filter attempts to minimize interferences from neighboring carriers by applying

### ModAcc

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxEVDO_ModAccCfgMultiCarrierFilterEnabled | Enables or disables the multicarrier filter. In multicarrier setups, EVM values are higher than in single carrier setups. The multicarrier filter attempts to minimize interferences from neighboring carriers by applying sharp edges. |
| RFmxEVDO_ModAccCfgSynchronizationModeAndInterval | Configures how the modulation accuracy (ModAcc) measurement synchronizes to the signal and the synchronization interval length. |

#### Attachments

None

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__functions__configuration__obw.html language=enus -->
## TOPIC 00077: OBW

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__functions__configuration__obw.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__functions__configuration__obw.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxEVDO_OBWCfgAveragingConfigures averaging for the occupied bandwidth (OBW) measurement. RFmxEVDO_OBWCfgRBWFilterConfigures the resolution bandwidth (RBW) filter. RFmxEVDO_OBWCfgSweepTimeConfigures sweep time. AttachmentsNone

### OBW

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxEVDO_OBWCfgAveraging | Configures averaging for the occupied bandwidth (OBW) measurement. |
| RFmxEVDO_OBWCfgRBWFilter | Configures the resolution bandwidth (RBW) filter. |
| RFmxEVDO_OBWCfgSweepTime | Configures sweep time. |

#### Attachments

None

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__functions__configuration__obw_1ga201b9d66f0749e3b841a63243b15e5ab.html language=enus -->
## TOPIC 00078: RFmxEVDO_OBWCfgSweepTime

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__functions__configuration__obw_1ga201b9d66f0749e3b841a63243b15e5ab.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__functions__configuration__obw_1ga201b9d66f0749e3b841a63243b15e5ab.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures sweep time. Syntaxint32 __stdcall RFmxEVDO_OBWCfgSweepTime(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 sweepTimeAuto, float64 sweepTimeInterval)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifies the RFmx session refnum.

### RFmxEVDO_OBWCfgSweepTime

Configures sweep time.

#### Syntax

int32 __stdcall RFmxEVDO_OBWCfgSweepTime(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 sweepTimeAuto, float64 sweepTimeInterval)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Examples:"""signal::sig1"You can use the RFmxEVDO_BuildSignalString function to build the selector string. |
| sweepTimeAuto | [in] | int32 | This parameter specifies whether the measurement calculates the sweep time. The default value is True.Name (value)DescriptionFalse (0)The measurement uses the sweep time that you specify using the Sweep Time Interval parameter.True (1)The measurement uses the default sweep time of 1.67 ms. |
| Name (value) | Description |  |  |
| False (0) | The measurement uses the sweep time that you specify using the Sweep Time Interval parameter. |  |  |
| True (1) | The measurement uses the default sweep time of 1.67 ms. |  |  |
| sweepTimeInterval | [in] | float64 | This parameter specifies the sweep time when you set the Sweep Time Auto parameter to False. This value is expressed in seconds. The default value is 1.67 ms. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxEVDO_GetError](group____root__ni_r_fmx_e_v_d_o__functions_1gaccaec841794030fe0dda93eb76bb7e60.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

OBW

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__functions__configuration__obw_1ga4ad895efe2ee28a31e0559622b7ba99e.html language=enus -->
## TOPIC 00079: RFmxEVDO_OBWCfgAveraging

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__functions__configuration__obw_1ga4ad895efe2ee28a31e0559622b7ba99e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__functions__configuration__obw_1ga4ad895efe2ee28a31e0559622b7ba99e.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures averaging for the occupied bandwidth (OBW) measurement. Syntaxint32 __stdcall RFmxEVDO_OBWCfgAveraging(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 averagingEnabled, int32 averagingCount, int32 averagingType)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niR

### RFmxEVDO_OBWCfgAveraging

Configures averaging for the occupied bandwidth (OBW) measurement.

#### Syntax

int32 __stdcall RFmxEVDO_OBWCfgAveraging(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 averagingEnabled, int32 averagingCount, int32 averagingType)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Examples:"""signal::sig1"You can use the RFmxEVDO_BuildSignalString function to build the selector string. |
| averagingEnabled | [in] | int32 | This parameter specifies whether to enable averaging for the measurement. The default value is False.Name (value)DescriptionFalse (0)Averaging is not enabled.True (1)Averaging is enabled. |
| Name (value) | Description |  |  |
| False (0) | Averaging is not enabled. |  |  |
| True (1) | Averaging is enabled. |  |  |
| averagingCount | [in] | int32 | This parameter specifies the number of acquisitions used for averaging when you set the Averaging Enabled parameter to True. The default value is 10. |
| averagingType | [in] | int32 | This parameter specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the measurement.Refer to the Averaging section of the Spectrum topic for more information about averaging types. The default value is RMS.Name (value)DescriptionRMS (0)The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor.Log (1)The power spectrum is averaged in a logarithmic scale.Scalar (2)The square root of the power spectrum is averaged.Max (3)The peak power in the spectrum at each frequency bin is retained from one acquisition to the next.Min (4)The least power in the spectrum at each frequency bin is retained from one acquisition to the next. |
| Name (value) | Description |  |  |
| RMS (0) | The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. |  |  |
| Log (1) | The power spectrum is averaged in a logarithmic scale. |  |  |
| Scalar (2) | The square root of the power spectrum is averaged. |  |  |
| Max (3) | The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. |  |  |
| Min (4) | The least power in the spectrum at each frequency bin is retained from one acquisition to the next. |  |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxEVDO_GetError](group____root__ni_r_fmx_e_v_d_o__functions_1gaccaec841794030fe0dda93eb76bb7e60.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

OBW

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__functions__configuration__obw_1gaad2a63e87b36d54c936ed5168c7653bb.html language=enus -->
## TOPIC 00080: RFmxEVDO_OBWCfgRBWFilter

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__functions__configuration__obw_1gaad2a63e87b36d54c936ed5168c7653bb.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__functions__configuration__obw_1gaad2a63e87b36d54c936ed5168c7653bb.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the resolution bandwidth (RBW) filter. Syntaxint32 __stdcall RFmxEVDO_OBWCfgRBWFilter(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 rbwAuto, float64 rbw, int32 rbwFilterType)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specif

### RFmxEVDO_OBWCfgRBWFilter

Configures the resolution bandwidth (RBW) filter.

#### Syntax

int32 __stdcall RFmxEVDO_OBWCfgRBWFilter(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 rbwAuto, float64 rbw, int32 rbwFilterType)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Examples:"""signal::sig1"You can use the RFmxEVDO_BuildSignalString function to build the selector string. |
| rbwAuto | [in] | int32 | This parameter specifies whether the measurement calculates the RBW. The default value is True.Name (value)DescriptionTrue (1)RFmx EV-DO automatically computes the RBW.False (0)The measurement uses the RBW you specify.Refer to the RBW and Sweep Time section in the Spectrum topic for more details on RBW and sweep time. |
| Name (value) | Description |  |  |
| True (1) | RFmx EV-DO automatically computes the RBW. |  |  |
| False (0) | The measurement uses the RBW you specify. |  |  |
| rbw | [in] | float64 | This parameter specifies the bandwidth of the RBW filter used to sweep the acquired signal, when you set the RBW Auto parameter to False. This value is expressed in Hz. The default value is 30 kHz. |
| rbwFilterType | [in] | int32 | This parameter specifies the shape of the digital RBW filter. The default value is Gaussian.Name (value)DescriptionFFT Based (0)No RBW filtering is performed.Gaussian (1)An RBW filter with a Gaussian response is applied.Flat (2)An RBW filter with a flat response is applied. |
| Name (value) | Description |  |  |
| FFT Based (0) | No RBW filtering is performed. |  |  |
| Gaussian (1) | An RBW filter with a Gaussian response is applied. |  |  |
| Flat (2) | An RBW filter with a flat response is applied. |  |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxEVDO_GetError](group____root__ni_r_fmx_e_v_d_o__functions_1gaccaec841794030fe0dda93eb76bb7e60.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

OBW

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__functions__configuration__sem.html language=enus -->
## TOPIC 00081: SEM

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__functions__configuration__sem.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__functions__configuration__sem.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxEVDO_SEMCfgAveragingConfigures averaging for the spectral emission mask (SEM) measurement. RFmxEVDO_SEMCfgSweepTimeConfigures the sweep time. AttachmentsNone

### SEM

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxEVDO_SEMCfgAveraging | Configures averaging for the spectral emission mask (SEM) measurement. |
| RFmxEVDO_SEMCfgSweepTime | Configures the sweep time. |

#### Attachments

None

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__functions__configuration__sem_1ga7336584faf64d8146ab6d8cebfd7eda6.html language=enus -->
## TOPIC 00082: RFmxEVDO_SEMCfgAveraging

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__functions__configuration__sem_1ga7336584faf64d8146ab6d8cebfd7eda6.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__functions__configuration__sem_1ga7336584faf64d8146ab6d8cebfd7eda6.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures averaging for the spectral emission mask (SEM) measurement. Syntaxint32 __stdcall RFmxEVDO_SEMCfgAveraging(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 averagingEnabled, int32 averagingCount, int32 averagingType)ParametersNameDirectionTypeDescriptioninstrumentHandle[in

### RFmxEVDO_SEMCfgAveraging

Configures averaging for the spectral emission mask (SEM) measurement.

#### Syntax

int32 __stdcall RFmxEVDO_SEMCfgAveraging(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 averagingEnabled, int32 averagingCount, int32 averagingType)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Examples:"""signal::sig1"You can use the RFmxEVDO_BuildSignalString function to build the selector string. |
| averagingEnabled | [in] | int32 | This parameter specifies whether to enable averaging for the measurement. The default value is False.Name (value)DescriptionFalse (0)Averaging is not enabled.True (1)Averaging is enabled. |
| Name (value) | Description |  |  |
| False (0) | Averaging is not enabled. |  |  |
| True (1) | Averaging is enabled. |  |  |
| averagingCount | [in] | int32 | This parameter specifies the number of acquisitions used for averaging when you set the Averaging Enabled parameter to True. The default value is 10. |
| averagingType | [in] | int32 | This parameter specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the measurement.Refer to the Averaging section of the Spectrum topic for more information about averaging types. The default value is RMS.Name (value)DescriptionRMS (0)The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor.Log (1)The power spectrum is averaged in a logarithmic scale.Scalar (2)The square root of the power spectrum is averaged.Max (3)The peak power in the spectrum at each frequency bin is retained from one acquisition to the next.Min (4)The least power in the spectrum at each frequency bin is retained from one acquisition to the next. |
| Name (value) | Description |  |  |
| RMS (0) | The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. |  |  |
| Log (1) | The power spectrum is averaged in a logarithmic scale. |  |  |
| Scalar (2) | The square root of the power spectrum is averaged. |  |  |
| Max (3) | The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. |  |  |
| Min (4) | The least power in the spectrum at each frequency bin is retained from one acquisition to the next. |  |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxEVDO_GetError](group____root__ni_r_fmx_e_v_d_o__functions_1gaccaec841794030fe0dda93eb76bb7e60.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__functions__configuration__sem_1gaf698eee51ec6916540a8dddade68dab0.html language=enus -->
## TOPIC 00083: RFmxEVDO_SEMCfgSweepTime

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__functions__configuration__sem_1gaf698eee51ec6916540a8dddade68dab0.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__functions__configuration__sem_1gaf698eee51ec6916540a8dddade68dab0.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the sweep time. Syntaxint32 __stdcall RFmxEVDO_SEMCfgSweepTime(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 sweepTimeAuto, float64 sweepTimeInterval)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifies the RFmx session ref

### RFmxEVDO_SEMCfgSweepTime

Configures the sweep time.

#### Syntax

int32 __stdcall RFmxEVDO_SEMCfgSweepTime(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 sweepTimeAuto, float64 sweepTimeInterval)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Examples:"""signal::sig1"You can use the RFmxEVDO_BuildSignalString function to build the selector string. |
| sweepTimeAuto | [in] | int32 | This parameter specifies whether the measurement calculates the sweep time. The default value is True.Name (value)DescriptionFalse (0)The measurement uses the sweep time that you specify using the Sweep Time Interval parameter.True (1)The measurement uses the default sweep time of 1.67 ms. |
| Name (value) | Description |  |  |
| False (0) | The measurement uses the sweep time that you specify using the Sweep Time Interval parameter. |  |  |
| True (1) | The measurement uses the default sweep time of 1.67 ms. |  |  |
| sweepTimeInterval | [in] | float64 | This parameter specifies the sweep time when you set the Sweep Time Auto parameter to False. This value is expressed in seconds. The default value is 1.67 ms. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxEVDO_GetError](group____root__ni_r_fmx_e_v_d_o__functions_1gaccaec841794030fe0dda93eb76bb7e60.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__functions__configuration__slotphase.html language=enus -->
## TOPIC 00084: SlotPhase

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__functions__configuration__slotphase.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__functions__configuration__slotphase.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxEVDO_SlotPhaseCfgSynchronizationModeAndIntervalConfigures the synchronization mode, measurement offset, and measurement length. AttachmentsNone

### SlotPhase

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxEVDO_SlotPhaseCfgSynchronizationModeAndInterval | Configures the synchronization mode, measurement offset, and measurement length. |

#### Attachments

None

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__functions__configuration__slotphase_1ga0a83e98f17aadf4d3865c729c0795924.html language=enus -->
## TOPIC 00085: RFmxEVDO_SlotPhaseCfgSynchronizationModeAndInterval

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__functions__configuration__slotphase_1ga0a83e98f17aadf4d3865c729c0795924.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__functions__configuration__slotphase_1ga0a83e98f17aadf4d3865c729c0795924.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the synchronization mode, measurement offset, and measurement length. Syntaxint32 __stdcall RFmxEVDO_SlotPhaseCfgSynchronizationModeAndInterval(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 synchronizationMode, int32 measurementOffset, int32 measurementLength)Parameters

### RFmxEVDO_SlotPhaseCfgSynchronizationModeAndInterval

Configures the synchronization mode, measurement offset, and measurement length.

#### Syntax

int32 __stdcall RFmxEVDO_SlotPhaseCfgSynchronizationModeAndInterval(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 synchronizationMode, int32 measurementOffset, int32 measurementLength)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Examples:"""signal::sig1"You can use the RFmxEVDO_BuildSignalString function to build the selector string. |
| synchronizationMode | [in] | int32 | This parameter specifies whether the measurement is performed from the frame or the slot boundary. The default value is Slot.NameValueDescriptionRFMXEVDO_VAL_SLOTPHASE_SYNCHRONIZATION_MODE_FRAME0 (0x0)The frame boundary is detected, and the measurement is performed over the number of slots specified by the RFMXEVDO_ATTR_SLOTPHASE_MEASUREMENT_LENGTH attribute starting at RFMXEVDO_ATTR_SLOTPHASE_MEASUREMENT_OFFSET slots from the frame boundary.RFMXEVDO_VAL_SLOTPHASE_SYNCHRONIZATION_MODE_SLOT1 (0x1)The slot boundary is detected and the measurement is performed over the number of slots specified by the SlotPhase Meas Length attribute starting at SlotPhase Meas Offset slots from the slot boundary. |
| Name | Value | Description |  |
| RFMXEVDO_VAL_SLOTPHASE_SYNCHRONIZATION_MODE_FRAME | 0 (0x0) | The frame boundary is detected, and the measurement is performed over the number of slots specified by the RFMXEVDO_ATTR_SLOTPHASE_MEASUREMENT_LENGTH attribute starting at RFMXEVDO_ATTR_SLOTPHASE_MEASUREMENT_OFFSET slots from the frame boundary. |  |
| RFMXEVDO_VAL_SLOTPHASE_SYNCHRONIZATION_MODE_SLOT | 1 (0x1) | The slot boundary is detected and the measurement is performed over the number of slots specified by the SlotPhase Meas Length attribute starting at SlotPhase Meas Offset slots from the slot boundary. |  |
| measurementOffset | [in] | int32 | This parameter specifies the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the SlotPhase Sync Mode attribute. The default value is 0. |
| measurementLength | [in] | int32 | This parameter specifies the duration of the SlotPhase measurement. This value is expressed in slots. The default value is 16. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxEVDO_GetError](group____root__ni_r_fmx_e_v_d_o__functions_1gaccaec841794030fe0dda93eb76bb7e60.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SlotPhase

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__functions__configuration__slotpower.html language=enus -->
## TOPIC 00086: SlotPower

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__functions__configuration__slotpower.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__functions__configuration__slotpower.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxEVDO_SlotPowerCfgSynchronizationModeAndIntervalConfigures the synchronization mode, measurement offset, and measurement length. AttachmentsNone

### SlotPower

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxEVDO_SlotPowerCfgSynchronizationModeAndInterval | Configures the synchronization mode, measurement offset, and measurement length. |

#### Attachments

None

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__functions__configuration__slotpower_1ga266bbafdabfd91c17d69a5e0a2cbe075.html language=enus -->
## TOPIC 00087: RFmxEVDO_SlotPowerCfgSynchronizationModeAndInterval

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__functions__configuration__slotpower_1ga266bbafdabfd91c17d69a5e0a2cbe075.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__functions__configuration__slotpower_1ga266bbafdabfd91c17d69a5e0a2cbe075.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the synchronization mode, measurement offset, and measurement length. Syntaxint32 __stdcall RFmxEVDO_SlotPowerCfgSynchronizationModeAndInterval(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 synchronizationMode, int32 measurementOffset, int32 measurementLength)Parameters

### RFmxEVDO_SlotPowerCfgSynchronizationModeAndInterval

Configures the synchronization mode, measurement offset, and measurement length.

#### Syntax

int32 __stdcall RFmxEVDO_SlotPowerCfgSynchronizationModeAndInterval(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 synchronizationMode, int32 measurementOffset, int32 measurementLength)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Examples:"""signal::sig1"You can use the RFmxEVDO_BuildSignalString function to build the selector string. |
| synchronizationMode | [in] | int32 | This parameter specifies whether the measurement is performed from the frame or the slot boundary. The default value is Slot.NameValueDescriptionRFMXEVDO_VAL_SLOTPOWER_SYNCHRONIZATION_MODE_FRAME0 (0x0)The frame boundary is detected, and the measurement is performed over the number of slots specified by the RFMXEVDO_ATTR_SLOTPOWER_MEASUREMENT_LENGTH attribute starting at RFMXEVDO_ATTR_SLOTPOWER_MEASUREMENT_OFFSET slots from the frame boundary.RFMXEVDO_VAL_SLOTPOWER_SYNCHRONIZATION_MODE_SLOT1 (0x1)The slot boundary is detected and the measurement is performed over the number of slots specified by the SlotPower Meas Length attribute starting at SlotPower Meas Offset slots from the slot boundary. |
| Name | Value | Description |  |
| RFMXEVDO_VAL_SLOTPOWER_SYNCHRONIZATION_MODE_FRAME | 0 (0x0) | The frame boundary is detected, and the measurement is performed over the number of slots specified by the RFMXEVDO_ATTR_SLOTPOWER_MEASUREMENT_LENGTH attribute starting at RFMXEVDO_ATTR_SLOTPOWER_MEASUREMENT_OFFSET slots from the frame boundary. |  |
| RFMXEVDO_VAL_SLOTPOWER_SYNCHRONIZATION_MODE_SLOT | 1 (0x1) | The slot boundary is detected and the measurement is performed over the number of slots specified by the SlotPower Meas Length attribute starting at SlotPower Meas Offset slots from the slot boundary. |  |
| measurementOffset | [in] | int32 | This parameter specifies the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the SlotPower Sync Mode attribute. The default value is 0. |
| measurementLength | [in] | int32 | This parameter specifies the duration of the SlotPower measurement. This value is expressed in slots. The default value is 16. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxEVDO_GetError](group____root__ni_r_fmx_e_v_d_o__functions_1gaccaec841794030fe0dda93eb76bb7e60.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SlotPower

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__functions__configuration__trigger.html language=enus -->
## TOPIC 00088: Trigger

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__functions__configuration__trigger.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__functions__configuration__trigger.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxEVDO_CfgDigitalEdgeTriggerConfigures the device to wait for a software trigger to mark a reference point within the record. RFmxEVDO_CfgIQPowerEdgeTriggerConfigures the device to wait for the complex power of the I/Q data to cross the specified threshold to

### Trigger

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxEVDO_CfgDigitalEdgeTrigger | Configures the device to wait for a software trigger to mark a reference point within the record. |
| RFmxEVDO_CfgIQPowerEdgeTrigger | Configures the device to wait for the complex power of the I/Q data to cross the specified threshold to mark a reference point within the record. |
| RFmxEVDO_CfgSoftwareEdgeTrigger | Configures the device to wait for a software trigger to mark a reference point within the record. |
| RFmxEVDO_DisableTrigger | Configures the device to not wait for a trigger to mark a reference point within a record. This function defines the signal triggering as immediate. |

#### Attachments

None

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__functions__configuration__trigger_1ga1642365e90a04fcc275e46a0e305d766.html language=enus -->
## TOPIC 00089: RFmxEVDO_CfgDigitalEdgeTrigger

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__functions__configuration__trigger_1ga1642365e90a04fcc275e46a0e305d766.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__functions__configuration__trigger_1ga1642365e90a04fcc275e46a0e305d766.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the device to wait for a software trigger to mark a reference point within the record. Syntaxint32 __stdcall RFmxEVDO_CfgDigitalEdgeTrigger(niRFmxInstrHandle instrumentHandle, char selectorString[], char digitalEdgeSource[], int32 digitalEdge, float64 triggerDelay, int32 enableTrigger)Par

### RFmxEVDO_CfgDigitalEdgeTrigger

Configures the device to wait for a software trigger to mark a reference point within the record.

#### Syntax

int32 __stdcall RFmxEVDO_CfgDigitalEdgeTrigger(niRFmxInstrHandle instrumentHandle, char selectorString[], char digitalEdgeSource[], int32 digitalEdge, float64 triggerDelay, int32 enableTrigger)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Examples:"""signal::sig1"You can use the RFmxEVDO_BuildSignalString function to build the selector string. |
| digitalEdgeSource | [in] | char[] | This parameter specifies the source terminal for the digital edge trigger. The default of this parameter is hardware dependent.Name (value)DescriptionPFI0(PFI0)The trigger is received on PFI 0.PFI1(PFI1)The trigger is received on PFI 1.PXI_Trig0(PXI_Trig0)The trigger is received on PXI trigger line 0.PXI_Trig1(PXI_Trig1)The trigger is received on PXI trigger line 1.PXI_Trig2(PXI_Trig2)The trigger is received on PXI trigger line 2.PXI_Trig3(PXI_Trig3)The trigger is received on PXI trigger line 3.PXI_Trig4(PXI_Trig4)The trigger is received on PXI trigger line 4.PXI_Trig5(PXI_Trig5)The trigger is received on PXI trigger line 5.PXI_Trig6(PXI_Trig6)The trigger is received on PXI trigger line 6.PXI_Trig7(PXI_Trig7)The trigger is received on PXI trigger line 7.PXI_STAR(PXI_STAR)The trigger is received on the PXI star trigger line. |
| Name (value) | Description |  |  |
| PFI0(PFI0) | The trigger is received on PFI 0. |  |  |
| PFI1(PFI1) | The trigger is received on PFI 1. |  |  |
| PXI_Trig0(PXI_Trig0) | The trigger is received on PXI trigger line 0. |  |  |
| PXI_Trig1(PXI_Trig1) | The trigger is received on PXI trigger line 1. |  |  |
| PXI_Trig2(PXI_Trig2) | The trigger is received on PXI trigger line 2. |  |  |
| PXI_Trig3(PXI_Trig3) | The trigger is received on PXI trigger line 3. |  |  |
| PXI_Trig4(PXI_Trig4) | The trigger is received on PXI trigger line 4. |  |  |
| PXI_Trig5(PXI_Trig5) | The trigger is received on PXI trigger line 5. |  |  |
| PXI_Trig6(PXI_Trig6) | The trigger is received on PXI trigger line 6. |  |  |
| PXI_Trig7(PXI_Trig7) | The trigger is received on PXI trigger line 7. |  |  |
| PXI_STAR(PXI_STAR) | The trigger is received on the PXI star trigger line. |  |  |
| digitalEdge | [in] | int32 | This parameter specifies the trigger edge to detect. The default value is Rising Edge.Name (value)DescriptionRising Edge (0)RFmx EV-DO detects a rising edge.Falling Edge (1)RFmx EV-DO detects a falling edge. |
| Name (value) | Description |  |  |
| Rising Edge (0) | RFmx EV-DO detects a rising edge. |  |  |
| Falling Edge (1) | RFmx EV-DO detects a falling edge. |  |  |
| triggerDelay | [in] | float64 | This parameter specifies the trigger delay time. This value is expressed in seconds. The default value is 0. |
| enableTrigger | [in] | int32 | This parameter specifies whether to enable the trigger. The default value is TRUE. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxEVDO_GetError](group____root__ni_r_fmx_e_v_d_o__functions_1gaccaec841794030fe0dda93eb76bb7e60.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Trigger

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__functions__configuration__trigger_1ga2c86d06bf0538f633fe955cc532fb513.html language=enus -->
## TOPIC 00090: RFmxEVDO_CfgIQPowerEdgeTrigger

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__functions__configuration__trigger_1ga2c86d06bf0538f633fe955cc532fb513.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__functions__configuration__trigger_1ga2c86d06bf0538f633fe955cc532fb513.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the device to wait for the complex power of the I/Q data to cross the specified threshold to mark a reference point within the record. Syntaxint32 __stdcall RFmxEVDO_CfgIQPowerEdgeTrigger(niRFmxInstrHandle instrumentHandle, char selectorString[], char iqPowerEdgeSource[], int32 iqPowerEdg

### RFmxEVDO_CfgIQPowerEdgeTrigger

Configures the device to wait for the complex power of the I/Q data to cross the specified threshold to mark a reference point within the record.

#### Syntax

int32 __stdcall RFmxEVDO_CfgIQPowerEdgeTrigger(niRFmxInstrHandle instrumentHandle, char selectorString[], char iqPowerEdgeSource[], int32 iqPowerEdgeSlope, float64 iqPowerEdgeLevel, float64 triggerDelay, int32 minimumQuietTimeMode, float64 minimumQuietTime, int32 iqPowerEdgeLevelType, int32 enableTrigger)

#### Remarks

To trigger on burst signals, specify a minimum quiet time, which ensures that the trigger does not occur in the middle of the burst signal. The quiet time must be set to a value smaller than the time between bursts but large enough to ignore power changes within a burst.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Examples:"""signal::sig1"You can use the RFmxEVDO_BuildSignalString function to build the selector string. |
| iqPowerEdgeSource | [in] | char[] | This parameter specifies the channel from which the device monitors the trigger. The default of this parameter is hardware dependent. |
| iqPowerEdgeSlope | [in] | int32 | This parameter specifies whether the device asserts the trigger when the signal power is rising or when it is falling. The device asserts the trigger when the signal power exceeds the specified level with the slope you specify. The default value is Rising Slope.Name (value)DescriptionRising Slope (0)The trigger asserts when the signal power is rising.Falling Slope (1)The trigger asserts when the signal power is falling. |
| Name (value) | Description |  |  |
| Rising Slope (0) | The trigger asserts when the signal power is rising. |  |  |
| Falling Slope (1) | The trigger asserts when the signal power is falling. |  |  |
| iqPowerEdgeLevel | [in] | float64 | This parameter specifies the threshold above or below which the RF signal analyzer triggers. The value is expressed in dB if IQ Power Edge Level Type is set to Relative; and is expressed in dBm if IQ Power Edge Level Type is set to Absolute. The device asserts the trigger when the signal exceeds the level specified by the value of this parameter, taking into consideration the specified slope. The default of this parameter is hardware dependent. |
| triggerDelay | [in] | float64 | This parameter specifies the trigger delay time. This value is expressed in seconds. The default value is 0. |
| minimumQuietTimeMode | [in] | int32 | This parameter specifies the duration for which the signal must be quiet before the RF signal analyzer arms the I/Q power edge trigger. This value is expressed in seconds. If you set the IQ Power Edge Slope parameter to Rising Slope, the signal is quiet when it is below the trigger level. If you set the IQ Power Edge Slope parameter to Falling Slope, the signal is quiet when it is above the trigger level. The default of this parameter is hardware dependent. |
| minimumQuietTime | [in] | float64 | This parameter specifies whether the measurement calculates the minimum quiet time used for triggering. The default value is Auto.Name (value)DescriptionManual (0)The measurement uses the minimum quiet time value you specify.Auto (1)The measurement calculates the minimum quiet time used for triggering. |
| Name (value) | Description |  |  |
| Manual (0) | The measurement uses the minimum quiet time value you specify. |  |  |
| Auto (1) | The measurement calculates the minimum quiet time used for triggering. |  |  |
| iqPowerEdgeLevelType | [in] | int32 | This parameter specifies the reference for the IQ Power Edge Level parameter.The IQ Power Edge Level Type parameter is used only when you set the RFMXEVDO_ATTR_TRIGGER_TYPE attribute to IQ Power Edge.Name (value)DescriptionRelative (0)The IQ Power Edge Level is relative to the reference level.Absolute (1)The IQ Power Edge Level specifies the absolute power. |
| Name (value) | Description |  |  |
| Relative (0) | The IQ Power Edge Level is relative to the reference level. |  |  |
| Absolute (1) | The IQ Power Edge Level specifies the absolute power. |  |  |
| enableTrigger | [in] | int32 | This parameter specifies whether to enable the trigger. The default value is TRUE. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxEVDO_GetError](group____root__ni_r_fmx_e_v_d_o__functions_1gaccaec841794030fe0dda93eb76bb7e60.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Trigger

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__functions__configuration__trigger_1ga488b04112916271156ae88028f791963.html language=enus -->
## TOPIC 00091: RFmxEVDO_DisableTrigger

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__functions__configuration__trigger_1ga488b04112916271156ae88028f791963.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__functions__configuration__trigger_1ga488b04112916271156ae88028f791963.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the device to not wait for a trigger to mark a reference point within a record. This function defines the signal triggering as immediate. Syntaxint32 __stdcall RFmxEVDO_DisableTrigger(niRFmxInstrHandle instrumentHandle, char selectorString[])ParametersNameDirectionTypeDescriptioninstrumen

### RFmxEVDO_DisableTrigger

Configures the device to not wait for a trigger to mark a reference point within a record. This function defines the signal triggering as immediate.

#### Syntax

int32 __stdcall RFmxEVDO_DisableTrigger(niRFmxInstrHandle instrumentHandle, char selectorString[])

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Examples:"""signal::sig1"You can use the RFmxEVDO_BuildSignalString function to build the selector string. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxEVDO_GetError](group____root__ni_r_fmx_e_v_d_o__functions_1gaccaec841794030fe0dda93eb76bb7e60.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Trigger

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__functions__configuration__trigger_1ga88f2584072403b88793bbbf2b9204098.html language=enus -->
## TOPIC 00092: RFmxEVDO_CfgSoftwareEdgeTrigger

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__functions__configuration__trigger_1ga88f2584072403b88793bbbf2b9204098.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__functions__configuration__trigger_1ga88f2584072403b88793bbbf2b9204098.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the device to wait for a software trigger to mark a reference point within the record. Syntaxint32 __stdcall RFmxEVDO_CfgSoftwareEdgeTrigger(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 triggerDelay, int32 enableTrigger)ParametersNameDirectionTypeDescriptioninstrumen

### RFmxEVDO_CfgSoftwareEdgeTrigger

Configures the device to wait for a software trigger to mark a reference point within the record.

#### Syntax

int32 __stdcall RFmxEVDO_CfgSoftwareEdgeTrigger(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 triggerDelay, int32 enableTrigger)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Examples:"""signal::sig1"You can use the RFmxEVDO_BuildSignalString function to build the selector string. |
| triggerDelay | [in] | float64 | This parameter specifies the trigger delay time. This value is expressed in seconds. The default value is 0. |
| enableTrigger | [in] | int32 | This parameter specifies whether to enable the trigger. The default value is TRUE. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxEVDO_GetError](group____root__ni_r_fmx_e_v_d_o__functions_1gaccaec841794030fe0dda93eb76bb7e60.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Trigger

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__functions__fetch.html language=enus -->
## TOPIC 00093: Fetch

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__functions__fetch.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__functions__fetch.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsACPCDACHPModAccOBWSEMSlotPhaseSlotPowerGroup membersNoneAttachmentsNone

### Fetch

#### Groups

- ACP
- CDA
- CHP
- ModAcc
- OBW
- SEM
- SlotPhase
- SlotPower

#### Group members

None

#### Attachments

None

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__functions__fetch__acp.html language=enus -->
## TOPIC 00094: ACP

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__functions__fetch__acp.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__functions__fetch__acp.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxEVDO_ACPFetchAbsolutePowersTraceFetches the absolute powers trace for the adjacent channel power (ACP) measurement. RFmxEVDO_ACPFetchCarrierMeasurementReturns the absolute and relative powers measured in the carriers. The relative powers are measured relativ

### ACP

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxEVDO_ACPFetchAbsolutePowersTrace | Fetches the absolute powers trace for the adjacent channel power (ACP) measurement. |
| RFmxEVDO_ACPFetchCarrierMeasurement | Returns the absolute and relative powers measured in the carriers. The relative powers are measured relative to the integrated power of the power reference carrier. |
| RFmxEVDO_ACPFetchCarrierMeasurementArray | Returns the absolute and relative powers measured in the carrier channels. The relative powers are measured relative to the integrated power of the power reference carrier. |
| RFmxEVDO_ACPFetchOffsetMeasurement | Returns the absolute and relative powers measured in the offset channel. The relative powers are measured relative to the integrated power of the power reference carrier. |
| RFmxEVDO_ACPFetchOffsetMeasurementArray | Returns the absolute and relative powers measured in the offset channel. The relative powers are measured relative to the integrated power of the power reference carrier. |
| RFmxEVDO_ACPFetchRelativePowersTrace | Fetches the relative powers trace for adjacent channel power (ACP) measurement. |
| RFmxEVDO_ACPFetchSpectrum | Fetches the spectrum used for the adjacent channel power (ACP) measurement. |
| RFmxEVDO_ACPFetchTotalCarrierPower | Fetches the total carrier power measured by the adjacent channel power (ACP) measurement. |

#### Attachments

None

Parent topic:

Fetch

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__functions__fetch__acp_1ga3cda2884fc521cad4d53d63620a53484.html language=enus -->
## TOPIC 00095: RFmxEVDO_ACPFetchCarrierMeasurement

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__functions__fetch__acp_1ga3cda2884fc521cad4d53d63620a53484.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__functions__fetch__acp_1ga3cda2884fc521cad4d53d63620a53484.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the absolute and relative powers measured in the carriers. The relative powers are measured relative to the integrated power of the power reference carrier. Syntaxint32 __stdcall RFmxEVDO_ACPFetchCarrierMeasurement(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, f

### RFmxEVDO_ACPFetchCarrierMeasurement

Returns the absolute and relative powers measured in the carriers. The relative powers are measured relative to the integrated power of the power reference carrier.

#### Syntax

int32 __stdcall RFmxEVDO_ACPFetchCarrierMeasurement(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *absolutePower, float64 *relativePower)

#### Remarks

Use "carrier<n>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used.Examples:"carrier0""signal::sig1/carrier0""result::r1/carrier0""signal::sig1/result::r1/carrier0"You can use the RFmxEVDO_BuildCarrierString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| absolutePower | [out] | float64 * | This parameter returns the absolute carrier power. This value is expressed in dBm. |
| relativePower | [out] | float64 * | This parameter returns the relative carrier power. This value is expressed in dB. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxEVDO_GetError](group____root__ni_r_fmx_e_v_d_o__functions_1gaccaec841794030fe0dda93eb76bb7e60.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ACP

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__functions__fetch__acp_1ga5936848424617312f2c88280b7b5022d.html language=enus -->
## TOPIC 00096: RFmxEVDO_ACPFetchOffsetMeasurementArray

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__functions__fetch__acp_1ga5936848424617312f2c88280b7b5022d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__functions__fetch__acp_1ga5936848424617312f2c88280b7b5022d.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the absolute and relative powers measured in the offset channel. The relative powers are measured relative to the integrated power of the power reference carrier. Syntaxint32 __stdcall RFmxEVDO_ACPFetchOffsetMeasurementArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64

### RFmxEVDO_ACPFetchOffsetMeasurementArray

Returns the absolute and relative powers measured in the offset channel. The relative powers are measured relative to the integrated power of the power reference carrier.

#### Syntax

int32 __stdcall RFmxEVDO_ACPFetchOffsetMeasurementArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 lowerRelativePower[], float64 upperRelativePower[], float64 lowerAbsolutePower[], float64 upperAbsolutePower[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxEVDO_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| lowerRelativePower | [out] | float64[] | This parameter returns the array of lower offset channel powers measured relative to the power of the carrier specified by the RFMXEVDO_ATTR_ACP_OFFSET_POWER_REFERENCE_CARRIER attribute. This value is expressed in dB. |
| upperRelativePower | [out] | float64[] | This parameter returns the array of upper offset channel powers measured relative to the power of the carrier specified by the RFMXEVDO_ATTR_ACP_OFFSET_POWER_REFERENCE_CARRIER attribute. This value is expressed in dB. |
| lowerAbsolutePower | [out] | float64[] | This parameter returns the array of lower offset channel powers. |
| upperAbsolutePower | [out] | float64[] | This parameter returns the array of upper offset channel powers. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxEVDO_GetError](group____root__ni_r_fmx_e_v_d_o__functions_1gaccaec841794030fe0dda93eb76bb7e60.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ACP

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__functions__fetch__acp_1ga8a51e25f523b1fc4be6a26b49fe13b87.html language=enus -->
## TOPIC 00097: RFmxEVDO_ACPFetchCarrierMeasurementArray

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__functions__fetch__acp_1ga8a51e25f523b1fc4be6a26b49fe13b87.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__functions__fetch__acp_1ga8a51e25f523b1fc4be6a26b49fe13b87.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the absolute and relative powers measured in the carrier channels. The relative powers are measured relative to the integrated power of the power reference carrier. Syntaxint32 __stdcall RFmxEVDO_ACPFetchCarrierMeasurementArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float

### RFmxEVDO_ACPFetchCarrierMeasurementArray

Returns the absolute and relative powers measured in the carrier channels. The relative powers are measured relative to the integrated power of the power reference carrier.

#### Syntax

int32 __stdcall RFmxEVDO_ACPFetchCarrierMeasurementArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 absolutePower[], float64 relativePower[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxEVDO_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| absolutePower | [out] | float64[] | This parameter returns the array of absolute carrier powers. This value is expressed in dBm. |
| relativePower | [out] | float64[] | This parameter returns the array of relative carrier powers. This value is expressed in dB. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxEVDO_GetError](group____root__ni_r_fmx_e_v_d_o__functions_1gaccaec841794030fe0dda93eb76bb7e60.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ACP

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__functions__fetch__acp_1gabac0ffefcb77206f8d29d7ec7d4ef045.html language=enus -->
## TOPIC 00098: RFmxEVDO_ACPFetchSpectrum

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__functions__fetch__acp_1gabac0ffefcb77206f8d29d7ec7d4ef045.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__functions__fetch__acp_1gabac0ffefcb77206f8d29d7ec7d4ef045.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the spectrum used for the adjacent channel power (ACP) measurement. Syntaxint32 __stdcall RFmxEVDO_ACPFetchSpectrum(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 spectrum[], int32 arraySize, int32 *actualArraySize)ParametersName

### RFmxEVDO_ACPFetchSpectrum

Fetches the spectrum used for the adjacent channel power (ACP) measurement.

#### Syntax

int32 __stdcall RFmxEVDO_ACPFetchSpectrum(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 spectrum[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxEVDO_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| x0 | [out] | float64 * | This parameter returns the start frequency. This value is expressed in Hz. |
| dx | [out] | float64 * | This parameter returns the frequency bin spacing. This value is expressed in Hz. |
| spectrum | [out] | float32[] | This parameter returns the averaged power measured at each frequency bin. This value is expressed in dBm or dBm/Hz. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxEVDO_GetError](group____root__ni_r_fmx_e_v_d_o__functions_1gaccaec841794030fe0dda93eb76bb7e60.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ACP

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__functions__fetch__acp_1gac6c5460980ce5a76fbe306b9d6d9e9cd.html language=enus -->
## TOPIC 00099: RFmxEVDO_ACPFetchTotalCarrierPower

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__functions__fetch__acp_1gac6c5460980ce5a76fbe306b9d6d9e9cd.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__functions__fetch__acp_1gac6c5460980ce5a76fbe306b9d6d9e9cd.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the total carrier power measured by the adjacent channel power (ACP) measurement. Syntaxint32 __stdcall RFmxEVDO_ACPFetchTotalCarrierPower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *totalCarrierPower)ParametersNameDirectionTypeDescriptioninstrumentHa

### RFmxEVDO_ACPFetchTotalCarrierPower

Fetches the total carrier power measured by the adjacent channel power (ACP) measurement.

#### Syntax

int32 __stdcall RFmxEVDO_ACPFetchTotalCarrierPower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *totalCarrierPower)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxEVDO_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| totalCarrierPower | [out] | float64 * | This parameter returns the total carrier power. This value is expressed in dBm. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxEVDO_GetError](group____root__ni_r_fmx_e_v_d_o__functions_1gaccaec841794030fe0dda93eb76bb7e60.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ACP

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__functions__fetch__acp_1gad1c860c0f6c5a3ff504eb859bd760b98.html language=enus -->
## TOPIC 00100: RFmxEVDO_ACPFetchRelativePowersTrace

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__functions__fetch__acp_1gad1c860c0f6c5a3ff504eb859bd760b98.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__functions__fetch__acp_1gad1c860c0f6c5a3ff504eb859bd760b98.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the relative powers trace for adjacent channel power (ACP) measurement. Syntaxint32 __stdcall RFmxEVDO_ACPFetchRelativePowersTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 traceIndex, float64 *x0, float64 *dx, float32 relativePowersTrace[], int32 arra

### RFmxEVDO_ACPFetchRelativePowersTrace

Fetches the relative powers trace for adjacent channel power (ACP) measurement.

#### Syntax

int32 __stdcall RFmxEVDO_ACPFetchRelativePowersTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 traceIndex, float64 *x0, float64 *dx, float32 relativePowersTrace[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxEVDO_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| traceIndex | [in] | int32 | Specifies the index of the trace to fetch. The traceIndex can range from 0 to (Number of carriers + 2*Number of offsets). |
| x0 | [out] | float64 * | This parameter returns the start frequency of the channel. This value is expressed in Hz. |
| dx | [out] | float64 * | This parameter returns the frequency bin spacing. This value is expressed in Hz. |
| relativePowersTrace | [out] | float32[] | This parameter returns the relative power measured in each channel relative to power reference carrier. This value is expressed in dB. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxEVDO_GetError](group____root__ni_r_fmx_e_v_d_o__functions_1gaccaec841794030fe0dda93eb76bb7e60.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ACP

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__functions__fetch__acp_1gad7920493f9990e41aa03c9ab6dfc9138.html language=enus -->
## TOPIC 00101: RFmxEVDO_ACPFetchAbsolutePowersTrace

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__functions__fetch__acp_1gad7920493f9990e41aa03c9ab6dfc9138.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__functions__fetch__acp_1gad7920493f9990e41aa03c9ab6dfc9138.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the absolute powers trace for the adjacent channel power (ACP) measurement. Syntaxint32 __stdcall RFmxEVDO_ACPFetchAbsolutePowersTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 traceIndex, float64 *x0, float64 *dx, float32 absolutePowersTrace[], int32

### RFmxEVDO_ACPFetchAbsolutePowersTrace

Fetches the absolute powers trace for the adjacent channel power (ACP) measurement.

#### Syntax

int32 __stdcall RFmxEVDO_ACPFetchAbsolutePowersTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 traceIndex, float64 *x0, float64 *dx, float32 absolutePowersTrace[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxEVDO_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| traceIndex | [in] | int32 | Specifies the index of the trace to fetch. The traceIndex can range from 0 to (Number of carriers + 2*Number of offsets). |
| x0 | [out] | float64 * | This parameter is the start parameter. |
| dx | [out] | float64 * | This parameter is the delta parameter. |
| absolutePowersTrace | [out] | float32[] | This parameter returns the real signal values stored in an array. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxEVDO_GetError](group____root__ni_r_fmx_e_v_d_o__functions_1gaccaec841794030fe0dda93eb76bb7e60.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ACP

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__functions__fetch__acp_1gafdf95943c2f326d8ab4c97c6f50f9662.html language=enus -->
## TOPIC 00102: RFmxEVDO_ACPFetchOffsetMeasurement

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__functions__fetch__acp_1gafdf95943c2f326d8ab4c97c6f50f9662.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__functions__fetch__acp_1gafdf95943c2f326d8ab4c97c6f50f9662.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the absolute and relative powers measured in the offset channel. The relative powers are measured relative to the integrated power of the power reference carrier. Syntaxint32 __stdcall RFmxEVDO_ACPFetchOffsetMeasurement(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeo

### RFmxEVDO_ACPFetchOffsetMeasurement

Returns the absolute and relative powers measured in the offset channel. The relative powers are measured relative to the integrated power of the power reference carrier.

#### Syntax

int32 __stdcall RFmxEVDO_ACPFetchOffsetMeasurement(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *lowerRelativePower, float64 *upperRelativePower, float64 *lowerAbsolutePower, float64 *upperAbsolutePower)

#### Remarks

Use "offset<n>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, and offset number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used.Examples:"offset0""signal::sig1/offset0""result::r1/offset0""signal::sig1/result::r1/offset0"You can use the RFmxEVDO_BuildOffsetString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| lowerRelativePower | [out] | float64 * | This parameter returns the lower offset channel power measured relative to the power of the carrier specified by the RFMXEVDO_ATTR_ACP_OFFSET_POWER_REFERENCE_CARRIER attribute. This value is expressed in dB. |
| upperRelativePower | [out] | float64 * | This parameter returns the upper offset channel power measured relative to the power of the carrier specified by the RFMXEVDO_ATTR_ACP_OFFSET_POWER_REFERENCE_CARRIER attribute. This value is expressed in dB. |
| lowerAbsolutePower | [out] | float64 * | This parameter returns the lower offset channel power. This value is expressed in dBm. |
| upperAbsolutePower | [out] | float64 * | This parameter returns the upper offset channel power. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxEVDO_GetError](group____root__ni_r_fmx_e_v_d_o__functions_1gaccaec841794030fe0dda93eb76bb7e60.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ACP

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__functions__fetch__cda.html language=enus -->
## TOPIC 00103: CDA

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__functions__fetch__cda.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__functions__fetch__cda.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxEVDO_CDAFetchIQImpairmentsFetches the measured I/Q impairments. RFmxEVDO_CDAFetchUplinkCodeDomainIAndQPowerFetches the I and Q mean active powers and the I and Q peak inactive powers. RFmxEVDO_CDAFetchUplinkCodeDomainIAndQPowerTraceFetches the I and Q code p

### CDA

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxEVDO_CDAFetchIQImpairments | Fetches the measured I/Q impairments. |
| RFmxEVDO_CDAFetchUplinkCodeDomainIAndQPower | Fetches the I and Q mean active powers and the I and Q peak inactive powers. |
| RFmxEVDO_CDAFetchUplinkCodeDomainIAndQPowerTrace | Fetches the I and Q code power traces measured in the code domain of the base spreading factor. |
| RFmxEVDO_CDAFetchUplinkCodeDomainPower | Fetches the scalar code domain power results. |
| RFmxEVDO_CDAFetchUplinkSymbolConstellationTrace | Fetches the symbol constellation trace of the configured measurement channel. |
| RFmxEVDO_CDAFetchUplinkSymbolConstellationTraceSplit | Fetches the symbol constellation trace of the configured measurement channel. |
| RFmxEVDO_CDAFetchUplinkSymbolEVM | Fetches the modulation accuracy related measures for the configured measurement channel. |
| RFmxEVDO_CDAFetchUplinkSymbolEVMTrace | Returns the symbol EVM trace of the configured measurement channel. |
| RFmxEVDO_CDAFetchUplinkSymbolMagnitudeErrorTrace | Returns the symbol magnitude error trace of the configured measurement channel. |
| RFmxEVDO_CDAFetchUplinkSymbolPhaseErrorTrace | Fetches the symbol phase error trace of the configured measurement channel. |
| RFmxEVDO_CDAFetchUplinkSymbolPowerTrace | Returns the symbol power trace of the configured measurement channel. |

#### Attachments

None

Parent topic:

Fetch

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__functions__fetch__cda_1ga1b6bc2d8d2044f0cb76b298f3ccd31f9.html language=enus -->
## TOPIC 00104: RFmxEVDO_CDAFetchUplinkCodeDomainIAndQPower

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__functions__fetch__cda_1ga1b6bc2d8d2044f0cb76b298f3ccd31f9.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__functions__fetch__cda_1ga1b6bc2d8d2044f0cb76b298f3ccd31f9.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the I and Q mean active powers and the I and Q peak inactive powers. Syntaxint32 __stdcall RFmxEVDO_CDAFetchUplinkCodeDomainIAndQPower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *imEanActivePower, float64 *qMeanActivePower, float64 *iPeakInactivePower

### RFmxEVDO_CDAFetchUplinkCodeDomainIAndQPower

Fetches the I and Q mean active powers and the I and Q peak inactive powers.

#### Syntax

int32 __stdcall RFmxEVDO_CDAFetchUplinkCodeDomainIAndQPower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *imEanActivePower, float64 *qMeanActivePower, float64 *iPeakInactivePower, float64 *qPeakInactivePower)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxEVDO_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| imEanActivePower | [out] | float64 * | This parameter returns the average power of all active code channels measured on the I-branch. If you set the CDA Power Unit attribute to dBm, the measurement returns the absolute measured power in dBm. Otherwise, the measurement returns the value relative to the total power in dB. |
| qMeanActivePower | [out] | float64 * | This parameter returns the average power of all active code channels measured on the Q-branch. If you set the CDA Power Unit attribute to dBm, the measurement returns the absolute measured power in dBm. Otherwise, the measurement returns the value relative to the total power in dB. |
| iPeakInactivePower | [out] | float64 * | This parameter returns the largest measured code power among the set of inactive channels on the I-branch, and in the code domain of the base spreading factor. The base spreading factor depends on the configured physical layer subtype, and is 16 for subtype 0/1; 32 otherwise. If you set the CDA Power Unit attribute to dBm, the measurement returns the absolute measured power in dBm. Otherwise, the measurement returns the value relative to the total power in dB. |
| qPeakInactivePower | [out] | float64 * | This parameter returns the largest measured code power among the set of inactive channels on the Q-branch, and in the code domain of the base spreading factor. The base spreading factor depends on the configured physical layer subtype, and is 16 for subtype 0/1; 32 otherwise. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxEVDO_GetError](group____root__ni_r_fmx_e_v_d_o__functions_1gaccaec841794030fe0dda93eb76bb7e60.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

CDA

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__functions__fetch__cda_1ga22f0053eff0b05bf9c8d395705d183d8.html language=enus -->
## TOPIC 00105: RFmxEVDO_CDAFetchUplinkSymbolConstellationTrace

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__functions__fetch__cda_1ga22f0053eff0b05bf9c8d395705d183d8.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__functions__fetch__cda_1ga22f0053eff0b05bf9c8d395705d183d8.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the symbol constellation trace of the configured measurement channel. Syntaxint32 __stdcall RFmxEVDO_CDAFetchUplinkSymbolConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle symbolConstellation[], int32 arraySize, int32 *actualArraySi

### RFmxEVDO_CDAFetchUplinkSymbolConstellationTrace

Fetches the symbol constellation trace of the configured measurement channel.

#### Syntax

int32 __stdcall RFmxEVDO_CDAFetchUplinkSymbolConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle symbolConstellation[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxEVDO_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| symbolConstellation | [out] | NIComplexSingle[] | This parameter returns the complex signal values stored in an array. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxEVDO_GetError](group____root__ni_r_fmx_e_v_d_o__functions_1gaccaec841794030fe0dda93eb76bb7e60.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

CDA

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__functions__fetch__cda_1ga35f8d16465402bfccd703f59d176543e.html language=enus -->
## TOPIC 00106: RFmxEVDO_CDAFetchIQImpairments

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__functions__fetch__cda_1ga35f8d16465402bfccd703f59d176543e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__functions__fetch__cda_1ga35f8d16465402bfccd703f59d176543e.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the measured I/Q impairments. Syntaxint32 __stdcall RFmxEVDO_CDAFetchIQImpairments(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *iqOriginOffset, float64 *iqGainImbalance, float64 *iqQuadratureError)ParametersNameDirectionTypeDescriptioninstrumentHandle[

### RFmxEVDO_CDAFetchIQImpairments

Fetches the measured I/Q impairments.

#### Syntax

int32 __stdcall RFmxEVDO_CDAFetchIQImpairments(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *iqOriginOffset, float64 *iqGainImbalance, float64 *iqQuadratureError)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxEVDO_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| iqOriginOffset | [out] | float64 * | This parameter returns the I/Q origin offset. This value is expressed in dB. |
| iqGainImbalance | [out] | float64 * | This parameter returns the I/Q gain imbalance. This value is expressed in dB. |
| iqQuadratureError | [out] | float64 * | This parameter returns the I/Q quadrature error. This value is expressed in degrees. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxEVDO_GetError](group____root__ni_r_fmx_e_v_d_o__functions_1gaccaec841794030fe0dda93eb76bb7e60.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

CDA

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__functions__fetch__cda_1ga3d1e0b92bdd8801c9fc0e959ca79bd9f.html language=enus -->
## TOPIC 00107: RFmxEVDO_CDAFetchUplinkCodeDomainPower

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__functions__fetch__cda_1ga3d1e0b92bdd8801c9fc0e959ca79bd9f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__functions__fetch__cda_1ga3d1e0b92bdd8801c9fc0e959ca79bd9f.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the scalar code domain power results. Syntaxint32 __stdcall RFmxEVDO_CDAFetchUplinkCodeDomainPower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *totalPower, float64 *totalActivePower, float64 *meanActivePower, float64 *peakActivePower, float64 *meanInac

### RFmxEVDO_CDAFetchUplinkCodeDomainPower

Fetches the scalar code domain power results.

#### Syntax

int32 __stdcall RFmxEVDO_CDAFetchUplinkCodeDomainPower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *totalPower, float64 *totalActivePower, float64 *meanActivePower, float64 *peakActivePower, float64 *meanInactivePower, float64 *peakInactivePower)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxEVDO_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| totalPower | [out] | float64 * | This parameter returns the mean power of the received signal. This value is expressed in dBm. |
| totalActivePower | [out] | float64 * | This parameter returns the sum of the powers of all active code channels. If you set the CDA Power Unit attribute to dBm, the measurement returns the absolute measured power in dBm. Otherwise, the measurement returns the value relative to the total power in dB. |
| meanActivePower | [out] | float64 * | This parameter returns the average power of all active code channels. If you set the CDA Power Unit attribute to dBm, the measurement returns the absolute measured power in dBm. Otherwise, the measurement returns the value relative to the total power in dB. |
| peakActivePower | [out] | float64 * | This parameter returns the maximum power among all active code channels. If you set the CDA Power Unit attribute to dBm, the measurement returns the absolute measured power in dBm. Otherwise, the measurement returns the value relative to the total power in dB. |
| meanInactivePower | [out] | float64 * | This parameter returns the average code power measured among the set of inactive channels in the code domain of the base spreading factor. The base spreading factor depends on the configured physical layer subtype and is 16 for subtype 0/1; 32 otherwise. If you set the CDA Power Unit attribute to dBm, the measurement returns the absolute measured power in dBm. Otherwise, the measurement returns the value relative to the total power in dB. The default value is 0. |
| peakInactivePower | [out] | float64 * | This parameter returns the largest measured code power among the set of inactive channels in the code domain of the base spreading factor. The base spreading factor depends on the configured physical layer subtype, and is 16 for subtype 0/1; 32 otherwise. If you set the CDA Power Unit attribute to dBm, the measurement returns the absolute measured power in dBm. Otherwise, the measurement returns the value relative to the total power in dB. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxEVDO_GetError](group____root__ni_r_fmx_e_v_d_o__functions_1gaccaec841794030fe0dda93eb76bb7e60.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

CDA

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__functions__fetch__cda_1ga46aecf71b553bb2753dcc3483ce20159.html language=enus -->
## TOPIC 00108: RFmxEVDO_CDAFetchUplinkSymbolPhaseErrorTrace

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__functions__fetch__cda_1ga46aecf71b553bb2753dcc3483ce20159.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__functions__fetch__cda_1ga46aecf71b553bb2753dcc3483ce20159.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the symbol phase error trace of the configured measurement channel. Syntaxint32 __stdcall RFmxEVDO_CDAFetchUplinkSymbolPhaseErrorTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 symbolPhaseError[], int32 arraySize, int32 *actualArraySize)ParametersNam

### RFmxEVDO_CDAFetchUplinkSymbolPhaseErrorTrace

Fetches the symbol phase error trace of the configured measurement channel.

#### Syntax

int32 __stdcall RFmxEVDO_CDAFetchUplinkSymbolPhaseErrorTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 symbolPhaseError[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxEVDO_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| symbolPhaseError | [out] | float32[] | This parameter returns the array of RMS symbol phase errors of the configured measurement channel. This value is expressed in degrees. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxEVDO_GetError](group____root__ni_r_fmx_e_v_d_o__functions_1gaccaec841794030fe0dda93eb76bb7e60.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

CDA

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__functions__fetch__cda_1ga5e575e6358fef568e98c52c927bad5ef.html language=enus -->
## TOPIC 00109: RFmxEVDO_CDAFetchUplinkSymbolPowerTrace

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__functions__fetch__cda_1ga5e575e6358fef568e98c52c927bad5ef.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__functions__fetch__cda_1ga5e575e6358fef568e98c52c927bad5ef.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the symbol power trace of the configured measurement channel. Syntaxint32 __stdcall RFmxEVDO_CDAFetchUplinkSymbolPowerTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 symbolPowers[], int32 arraySize, int32 *actualArraySize)ParametersNameDirectionTypeD

### RFmxEVDO_CDAFetchUplinkSymbolPowerTrace

Returns the symbol power trace of the configured measurement channel.

#### Syntax

int32 __stdcall RFmxEVDO_CDAFetchUplinkSymbolPowerTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 symbolPowers[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxEVDO_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| symbolPowers | [out] | float32[] | This parameter returns the trace of measured symbol powers. This value is expressed in dBm. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxEVDO_GetError](group____root__ni_r_fmx_e_v_d_o__functions_1gaccaec841794030fe0dda93eb76bb7e60.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

CDA

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__functions__fetch__cda_1ga5e6659ffec79e931b5abd27939ee71fb.html language=enus -->
## TOPIC 00110: RFmxEVDO_CDAFetchUplinkSymbolEVMTrace

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__functions__fetch__cda_1ga5e6659ffec79e931b5abd27939ee71fb.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__functions__fetch__cda_1ga5e6659ffec79e931b5abd27939ee71fb.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the symbol EVM trace of the configured measurement channel. Syntaxint32 __stdcall RFmxEVDO_CDAFetchUplinkSymbolEVMTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 symbolEVM[], int32 arraySize, int32 *actualArraySize)ParametersNameDirectionTypeDescript

### RFmxEVDO_CDAFetchUplinkSymbolEVMTrace

Returns the symbol EVM trace of the configured measurement channel.

#### Syntax

int32 __stdcall RFmxEVDO_CDAFetchUplinkSymbolEVMTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 symbolEVM[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxEVDO_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| symbolEVM | [out] | float32[] | This parameter This parameter returns the trace of symbol EVM. This value is expressed as a percentage. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxEVDO_GetError](group____root__ni_r_fmx_e_v_d_o__functions_1gaccaec841794030fe0dda93eb76bb7e60.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

CDA

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__functions__fetch__cda_1ga6704a4fc109c6b2f9a16575742719b58.html language=enus -->
## TOPIC 00111: RFmxEVDO_CDAFetchUplinkCodeDomainIAndQPowerTrace

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__functions__fetch__cda_1ga6704a4fc109c6b2f9a16575742719b58.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__functions__fetch__cda_1ga6704a4fc109c6b2f9a16575742719b58.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the I and Q code power traces measured in the code domain of the base spreading factor. Syntaxint32 __stdcall RFmxEVDO_CDAFetchUplinkCodeDomainIAndQPowerTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 iCodeDomainPowers[], float32 qCodeDomainPowers[],

### RFmxEVDO_CDAFetchUplinkCodeDomainIAndQPowerTrace

Fetches the I and Q code power traces measured in the code domain of the base spreading factor.

#### Syntax

int32 __stdcall RFmxEVDO_CDAFetchUplinkCodeDomainIAndQPowerTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 iCodeDomainPowers[], float32 qCodeDomainPowers[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxEVDO_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| iCodeDomainPowers | [out] | float32[] | This parameter returns the I code domain power traces. This value is expressed in dB or dBm. |
| qCodeDomainPowers | [out] | float32[] | This parameter returns the Q code domain power traces. This value is expressed in dB or dBm. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxEVDO_GetError](group____root__ni_r_fmx_e_v_d_o__functions_1gaccaec841794030fe0dda93eb76bb7e60.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

CDA

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__functions__fetch__cda_1ga720cdeac567f5f777ccf6d4456bd7130.html language=enus -->
## TOPIC 00112: RFmxEVDO_CDAFetchUplinkSymbolEVM

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__functions__fetch__cda_1ga720cdeac567f5f777ccf6d4456bd7130.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__functions__fetch__cda_1ga720cdeac567f5f777ccf6d4456bd7130.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the modulation accuracy related measures for the configured measurement channel. Syntaxint32 __stdcall RFmxEVDO_CDAFetchUplinkSymbolEVM(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *rmsSymbolEVM, float64 *peakSymbolEVM, float64 *rmsSymbolMagnitudeError,

### RFmxEVDO_CDAFetchUplinkSymbolEVM

Fetches the modulation accuracy related measures for the configured measurement channel.

#### Syntax

int32 __stdcall RFmxEVDO_CDAFetchUplinkSymbolEVM(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *rmsSymbolEVM, float64 *peakSymbolEVM, float64 *rmsSymbolMagnitudeError, float64 *rmsSymbolPhaseError, float64 *meanSymbolPower, float64 *frequencyError, float64 *chipRateError)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxEVDO_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| rmsSymbolEVM | [out] | float64 * | This parameter returns the RMS ymbol EVM of the configured measurement channel. This value is expressed as a percentage. |
| peakSymbolEVM | [out] | float64 * | This parameter returns the peak symbol EVM of the configured measurement channel. This value is expressed as a percentage. |
| rmsSymbolMagnitudeError | [out] | float64 * | This parameter returns the RMS symbol magnitude error of the configured measurement channel. This value is expressed as a percentage. |
| rmsSymbolPhaseError | [out] | float64 * | This parameter returns the RMS symbol phase error of the configured measurement channel. This value is expressed in degrees. |
| meanSymbolPower | [out] | float64 * | This parameter returns the mean symbol power of the configured measurement channel. This value is expressed in dB or dBm. |
| frequencyError | [out] | float64 * | This parameter returns the frequency error. This value is expressed in Hz. |
| chipRateError | [out] | float64 * | This parameter returns the chip rate error. This value is expressed in ppm. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxEVDO_GetError](group____root__ni_r_fmx_e_v_d_o__functions_1gaccaec841794030fe0dda93eb76bb7e60.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

CDA

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__functions__fetch__cda_1gaa0ca51530bd9f53ed41e0f1900656fb3.html language=enus -->
## TOPIC 00113: RFmxEVDO_CDAFetchUplinkSymbolConstellationTraceSplit

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__functions__fetch__cda_1gaa0ca51530bd9f53ed41e0f1900656fb3.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__functions__fetch__cda_1gaa0ca51530bd9f53ed41e0f1900656fb3.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the symbol constellation trace of the configured measurement channel. Syntaxint32 __stdcall RFmxEVDO_CDAFetchUplinkSymbolConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 symbolConstellationI[], float32 symbolConstellationQ[], int32 a

### RFmxEVDO_CDAFetchUplinkSymbolConstellationTraceSplit

Fetches the symbol constellation trace of the configured measurement channel.

#### Syntax

int32 __stdcall RFmxEVDO_CDAFetchUplinkSymbolConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 symbolConstellationI[], float32 symbolConstellationQ[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxEVDO_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| symbolConstellationI | [out] | float32[] | This parameter Returns the real part of complex signal values stored in an array. |
| symbolConstellationQ | [out] | float32[] | This parameter Returns the imaginary part of complex signal values stored in an array. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxEVDO_GetError](group____root__ni_r_fmx_e_v_d_o__functions_1gaccaec841794030fe0dda93eb76bb7e60.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

CDA

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__functions__fetch__cda_1gaeaa79b9b35c1b165975c84c283506eee.html language=enus -->
## TOPIC 00114: RFmxEVDO_CDAFetchUplinkSymbolMagnitudeErrorTrace

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__functions__fetch__cda_1gaeaa79b9b35c1b165975c84c283506eee.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__functions__fetch__cda_1gaeaa79b9b35c1b165975c84c283506eee.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the symbol magnitude error trace of the configured measurement channel. Syntaxint32 __stdcall RFmxEVDO_CDAFetchUplinkSymbolMagnitudeErrorTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 symbolMagnitudeError[], int32 arraySize, int32 *actualArraySize)P

### RFmxEVDO_CDAFetchUplinkSymbolMagnitudeErrorTrace

Returns the symbol magnitude error trace of the configured measurement channel.

#### Syntax

int32 __stdcall RFmxEVDO_CDAFetchUplinkSymbolMagnitudeErrorTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 symbolMagnitudeError[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxEVDO_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| symbolMagnitudeError | [out] | float32[] | This parameter returns the trace of symbol magnitude error.. This value is expressed as a percentage. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxEVDO_GetError](group____root__ni_r_fmx_e_v_d_o__functions_1gaccaec841794030fe0dda93eb76bb7e60.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

CDA

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__functions__fetch__chp.html language=enus -->
## TOPIC 00115: CHP

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__functions__fetch__chp.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__functions__fetch__chp.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxEVDO_CHPFetchCarrierMeasurementReturns the absolute and relative powers measured in the carriers. The relative powers are measured relative to the integrated power of the power reference carrier. Use "carrier<n>" as the selector string to read results from t

### CHP

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxEVDO_CHPFetchCarrierMeasurement | Returns the absolute and relative powers measured in the carriers. The relative powers are measured relative to the integrated power of the power reference carrier. Use "carrier<n>" as the selector string to read results from this function. |
| RFmxEVDO_CHPFetchCarrierMeasurementArray | Returns the array of carrier measurements of the channel power (CHP) measurement. |
| RFmxEVDO_CHPFetchSpectrum | Fetches the spectrum used for the channel power (CHP) measurement. |
| RFmxEVDO_CHPFetchTotalCarrierPower | Fetches the total carrier power measured by the channel power (CHP) measurement. |

#### Attachments

None

Parent topic:

Fetch

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__functions__fetch__chp_1ga3cd5c164a22e976cb6f88b2faf76470b.html language=enus -->
## TOPIC 00116: RFmxEVDO_CHPFetchSpectrum

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__functions__fetch__chp_1ga3cd5c164a22e976cb6f88b2faf76470b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__functions__fetch__chp_1ga3cd5c164a22e976cb6f88b2faf76470b.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the spectrum used for the channel power (CHP) measurement. Syntaxint32 __stdcall RFmxEVDO_CHPFetchSpectrum(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 spectrum[], int32 arraySize, int32 *actualArraySize)ParametersNameDirection

### RFmxEVDO_CHPFetchSpectrum

Fetches the spectrum used for the channel power (CHP) measurement.

#### Syntax

int32 __stdcall RFmxEVDO_CHPFetchSpectrum(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 spectrum[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxEVDO_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| x0 | [out] | float64 * | This parameter returns the start frequency. This value is expressed in Hz. |
| dx | [out] | float64 * | This parameter returns the frequency bin spacing. This value is expressed in Hz. |
| spectrum | [out] | float32[] | This parameter returns the averaged power measured at each frequency bin. This value is expressed in dBm or dBm/Hz. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxEVDO_GetError](group____root__ni_r_fmx_e_v_d_o__functions_1gaccaec841794030fe0dda93eb76bb7e60.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

CHP

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__functions__fetch__chp_1ga3ee489dc42e35da16691eb39a0aea470.html language=enus -->
## TOPIC 00117: RFmxEVDO_CHPFetchCarrierMeasurement

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__functions__fetch__chp_1ga3ee489dc42e35da16691eb39a0aea470.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__functions__fetch__chp_1ga3ee489dc42e35da16691eb39a0aea470.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the absolute and relative powers measured in the carriers. The relative powers are measured relative to the integrated power of the power reference carrier. Use "carrier<n>" as the selector string to read results from this function. Syntaxint32 __stdcall RFmxEVDO_CHPFetchCarrierMeasurement(n

### RFmxEVDO_CHPFetchCarrierMeasurement

Returns the absolute and relative powers measured in the carriers. The relative powers are measured relative to the integrated power of the power reference carrier. Use "carrier<n>" as the selector string to read results from this function.

#### Syntax

int32 __stdcall RFmxEVDO_CHPFetchCarrierMeasurement(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *carrierAbsolutePower, float64 *carrierRelativePower)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used.Examples:"carrier0""signal::sig1/carrier0""result::r1/carrier0""signal::sig1/result::r1/carrier0"You can use the RFmxEVDO_BuildCarrierString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| carrierAbsolutePower | [out] | float64 * | This parameter returns the absolute carrier power of the selected carrier. This value is expressed in dBm. |
| carrierRelativePower | [out] | float64 * | This parameter returns the relative carrier power of the selected carrier. This value is expressed in dBm. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxEVDO_GetError](group____root__ni_r_fmx_e_v_d_o__functions_1gaccaec841794030fe0dda93eb76bb7e60.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

CHP

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__functions__fetch__chp_1ga4efb3714a7bfbffe05d98137c0289465.html language=enus -->
## TOPIC 00118: RFmxEVDO_CHPFetchTotalCarrierPower

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__functions__fetch__chp_1ga4efb3714a7bfbffe05d98137c0289465.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__functions__fetch__chp_1ga4efb3714a7bfbffe05d98137c0289465.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the total carrier power measured by the channel power (CHP) measurement. Syntaxint32 __stdcall RFmxEVDO_CHPFetchTotalCarrierPower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *totalCarrierPower)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]n

### RFmxEVDO_CHPFetchTotalCarrierPower

Fetches the total carrier power measured by the channel power (CHP) measurement.

#### Syntax

int32 __stdcall RFmxEVDO_CHPFetchTotalCarrierPower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *totalCarrierPower)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxEVDO_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| totalCarrierPower | [out] | float64 * | This parameter returns the total carrier power. This value is expressed in dBm. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxEVDO_GetError](group____root__ni_r_fmx_e_v_d_o__functions_1gaccaec841794030fe0dda93eb76bb7e60.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

CHP

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__functions__fetch__chp_1gac9de12ce77cc471a7d7ecd5cb8dd29d6.html language=enus -->
## TOPIC 00119: RFmxEVDO_CHPFetchCarrierMeasurementArray

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__functions__fetch__chp_1gac9de12ce77cc471a7d7ecd5cb8dd29d6.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__functions__fetch__chp_1gac9de12ce77cc471a7d7ecd5cb8dd29d6.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the array of carrier measurements of the channel power (CHP) measurement. Syntaxint32 __stdcall RFmxEVDO_CHPFetchCarrierMeasurementArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 carrierAbsolutePower[], float64 carrierRelativePower[], int32 arraySize

### RFmxEVDO_CHPFetchCarrierMeasurementArray

Returns the array of carrier measurements of the channel power (CHP) measurement.

#### Syntax

int32 __stdcall RFmxEVDO_CHPFetchCarrierMeasurementArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 carrierAbsolutePower[], float64 carrierRelativePower[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxEVDO_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| carrierAbsolutePower | [out] | float64[] | This parameter returns the array of absolute carrier powers. This value is expressed in dBm. |
| carrierRelativePower | [out] | float64[] | This parameter returns the array of relative carrier powers. This value is expressed in dB. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxEVDO_GetError](group____root__ni_r_fmx_e_v_d_o__functions_1gaccaec841794030fe0dda93eb76bb7e60.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

CHP

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__functions__fetch__modacc.html language=enus -->
## TOPIC 00120: ModAcc

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__functions__fetch__modacc.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__functions__fetch__modacc.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxEVDO_ModAccFetchConstellationTraceReturns the constellation trace of the EV-DO measurement. RFmxEVDO_ModAccFetchConstellationTraceSplitReturns the constellation trace of the EV-DO measurement. RFmxEVDO_ModAccFetchEVMTraceReturns the EVM trace of the ModAcc m

### ModAcc

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxEVDO_ModAccFetchConstellationTrace | Returns the constellation trace of the EV-DO measurement. |
| RFmxEVDO_ModAccFetchConstellationTraceSplit | Returns the constellation trace of the EV-DO measurement. |
| RFmxEVDO_ModAccFetchEVMTrace | Returns the EVM trace of the ModAcc measurement. |
| RFmxEVDO_ModAccFetchIQImpairments | Returns the origin offset, gain imbalance, and quadrature error. |
| RFmxEVDO_ModAccFetchMagnitudeErrorTrace | Returns the magnitude error trace for the modulation accuracy (ModAcc) measurement. |
| RFmxEVDO_ModAccFetchPhaseErrorTrace | Returns the phase error trace of the ModAcc measurement. |
| RFmxEVDO_ModAccFetchUplinkDetectedChannel | Returns the detected channel selected by the selector string. |
| RFmxEVDO_ModAccFetchUplinkDetectedChannelArray | Returns the array of detected channels in the EV-DO uplink. |
| RFmxEVDO_ModAccFetchUplinkDetectedDataModulationType | Returns the modulation type of the uplink data channel. |
| RFmxEVDO_ModAccFetchUplinkEVM | Returns the EVM and related values of the EV-DO uplink. |
| RFmxEVDO_ModAccFetchUplinkNumberOfDetectedChannels | Returns the number of channels detected by the modulation accuracy (ModAcc) measurement. |
| RFmxEVDO_ModAccFetchUplinkPeakActiveCDE | Returns the peak value among the code domain errors of the active channels, along with the code number and the code length. |
| RFmxEVDO_ModAccFetchUplinkPeakCDE | Returns the maximum value among the code domain errors (CDEs), in dB. |

#### Attachments

None

Parent topic:

Fetch

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__functions__fetch__modacc_1ga06961ca486df1b9647ce4f49b8a75f1c.html language=enus -->
## TOPIC 00121: RFmxEVDO_ModAccFetchMagnitudeErrorTrace

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__functions__fetch__modacc_1ga06961ca486df1b9647ce4f49b8a75f1c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__functions__fetch__modacc_1ga06961ca486df1b9647ce4f49b8a75f1c.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the magnitude error trace for the modulation accuracy (ModAcc) measurement. Syntaxint32 __stdcall RFmxEVDO_ModAccFetchMagnitudeErrorTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 magnitudeError[], int32 arraySize, int32 *ac

### RFmxEVDO_ModAccFetchMagnitudeErrorTrace

Returns the magnitude error trace for the modulation accuracy (ModAcc) measurement.

#### Syntax

int32 __stdcall RFmxEVDO_ModAccFetchMagnitudeErrorTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 magnitudeError[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxEVDO_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| x0 | [out] | float64 * | This parameter is the start parameter. |
| dx | [out] | float64 * | This parameter is the delta parameter. |
| magnitudeError | [out] | float32[] | This parameter returns the real signal values stored in an array. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxEVDO_GetError](group____root__ni_r_fmx_e_v_d_o__functions_1gaccaec841794030fe0dda93eb76bb7e60.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__functions__fetch__modacc_1ga3953c37883482e65acf3102302cbc5da.html language=enus -->
## TOPIC 00122: RFmxEVDO_ModAccFetchIQImpairments

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__functions__fetch__modacc_1ga3953c37883482e65acf3102302cbc5da.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__functions__fetch__modacc_1ga3953c37883482e65acf3102302cbc5da.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the origin offset, gain imbalance, and quadrature error. Syntaxint32 __stdcall RFmxEVDO_ModAccFetchIQImpairments(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *iqOriginOffset, float64 *iqGainImbalance, float64 *iqQuadratureError)ParametersNameDirectionTy

### RFmxEVDO_ModAccFetchIQImpairments

Returns the origin offset, gain imbalance, and quadrature error.

#### Syntax

int32 __stdcall RFmxEVDO_ModAccFetchIQImpairments(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *iqOriginOffset, float64 *iqGainImbalance, float64 *iqQuadratureError)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxEVDO_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| iqOriginOffset | [out] | float64 * | This parameter returns the I/Q origin offset of the composite signal. This value is expressed in dB. |
| iqGainImbalance | [out] | float64 * | This parameter returns the I/Q gain imbalance of the composite signal. This value is expressed in dB. |
| iqQuadratureError | [out] | float64 * | This parameter returns the I/Q quadrature error of the composite signal. This value is expressed in degrees. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxEVDO_GetError](group____root__ni_r_fmx_e_v_d_o__functions_1gaccaec841794030fe0dda93eb76bb7e60.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__functions__fetch__modacc_1ga51a5ffb68cdf97943fe46df1714b3eb9.html language=enus -->
## TOPIC 00123: RFmxEVDO_ModAccFetchUplinkPeakActiveCDE

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__functions__fetch__modacc_1ga51a5ffb68cdf97943fe46df1714b3eb9.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__functions__fetch__modacc_1ga51a5ffb68cdf97943fe46df1714b3eb9.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the peak value among the code domain errors of the active channels, along with the code number and the code length. Syntaxint32 __stdcall RFmxEVDO_ModAccFetchUplinkPeakActiveCDE(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *uplinkPeakActiveCDE, int32 *u

### RFmxEVDO_ModAccFetchUplinkPeakActiveCDE

Returns the peak value among the code domain errors of the active channels, along with the code number and the code length.

#### Syntax

int32 __stdcall RFmxEVDO_ModAccFetchUplinkPeakActiveCDE(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *uplinkPeakActiveCDE, int32 *uplinkPeakActiveCDEWalshCodeLength, int32 *uplinkPeakActiveCDEWalshCodeNumber, int32 *uplinkPeakActiveCDEBranch)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxEVDO_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| uplinkPeakActiveCDE | [out] | float64 * | This parameter returns the peak value of all CDEs of the active channels. This value is expressed in dB. |
| uplinkPeakActiveCDEWalshCodeLength | [out] | int32 * | This parameter returns the Walsh code length of the channel corresponding to the Uplink Peak Active CDE (dB) result. |
| uplinkPeakActiveCDEWalshCodeNumber | [out] | int32 * | This parameter returns the Walsh code number of the channel corresponding to the Uplink Peak Active CDE (dB) result. |
| uplinkPeakActiveCDEBranch | [out] | int32 * | This parameter returns the branch of the channel corresponding to the Peak Active CDE (dB) result.Name (value)DescriptionI(0)The peak active CDE corresponds to the in-phase branch.Q(1)The peak active CDE corresponds to the quadrature branch.I and Q(2)The peak active CDE corresponds to the in-phase branch and the quadrature branch. |
| Name (value) | Description |  |  |
| I(0) | The peak active CDE corresponds to the in-phase branch. |  |  |
| Q(1) | The peak active CDE corresponds to the quadrature branch. |  |  |
| I and Q(2) | The peak active CDE corresponds to the in-phase branch and the quadrature branch. |  |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxEVDO_GetError](group____root__ni_r_fmx_e_v_d_o__functions_1gaccaec841794030fe0dda93eb76bb7e60.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__functions__fetch__modacc_1ga54fb2b17e79289f757167d4620d17c12.html language=enus -->
## TOPIC 00124: RFmxEVDO_ModAccFetchUplinkDetectedChannelArray

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__functions__fetch__modacc_1ga54fb2b17e79289f757167d4620d17c12.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__functions__fetch__modacc_1ga54fb2b17e79289f757167d4620d17c12.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the array of detected channels in the EV-DO uplink. Syntaxint32 __stdcall RFmxEVDO_ModAccFetchUplinkDetectedChannelArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 uplinkDetectedWalshCodeLength[], int32 uplinkDetectedWalshCodeNumber[], int32 uplinkDetec

### RFmxEVDO_ModAccFetchUplinkDetectedChannelArray

Returns the array of detected channels in the EV-DO uplink.

#### Syntax

int32 __stdcall RFmxEVDO_ModAccFetchUplinkDetectedChannelArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 uplinkDetectedWalshCodeLength[], int32 uplinkDetectedWalshCodeNumber[], int32 uplinkDetectedBranch[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxEVDO_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| uplinkDetectedWalshCodeLength | [out] | int32[] | This parameter returns an array of detected Walsh code length values. |
| uplinkDetectedWalshCodeNumber | [out] | int32[] | This parameter returns an array of detected Walsh code number values. |
| uplinkDetectedBranch | [out] | int32[] | This parameter returns an array of detected branch values.Name (value)DescriptionI(0)The detected channel occupies the in-phase branch.Q(1)The detected channel occupies the quadrature branch.I and Q(2)The detected channel occupies the in-phase branch and the quadrature branch. |
| Name (value) | Description |  |  |
| I(0) | The detected channel occupies the in-phase branch. |  |  |
| Q(1) | The detected channel occupies the quadrature branch. |  |  |
| I and Q(2) | The detected channel occupies the in-phase branch and the quadrature branch. |  |  |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxEVDO_GetError](group____root__ni_r_fmx_e_v_d_o__functions_1gaccaec841794030fe0dda93eb76bb7e60.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__functions__fetch__modacc_1ga5ca8d05562403df49f19f31c30de1611.html language=enus -->
## TOPIC 00125: RFmxEVDO_ModAccFetchUplinkDetectedChannel

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__functions__fetch__modacc_1ga5ca8d05562403df49f19f31c30de1611.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__functions__fetch__modacc_1ga5ca8d05562403df49f19f31c30de1611.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the detected channel selected by the selector string. Syntaxint32 __stdcall RFmxEVDO_ModAccFetchUplinkDetectedChannel(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 *uplinkDetectedWalshCodeLength, int32 *uplinkDetectedWalshCodeNumber, int32 *uplinkDetectedB

### RFmxEVDO_ModAccFetchUplinkDetectedChannel

Returns the detected channel selected by the selector string.

#### Syntax

int32 __stdcall RFmxEVDO_ModAccFetchUplinkDetectedChannel(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 *uplinkDetectedWalshCodeLength, int32 *uplinkDetectedWalshCodeNumber, int32 *uplinkDetectedBranch)

#### Remarks

Use "channel<n>" as the selector string to configure this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, and channel number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used.Examples:"channel0""signal::sig1/channel0""result::r1/channel0""signal::sig1/result::r1/channel0"You can use the RFmxEVDO_BuildChannelString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| uplinkDetectedWalshCodeLength | [out] | int32 * | This parameter returns the detected Walsh code length. |
| uplinkDetectedWalshCodeNumber | [out] | int32 * | This parameter returns the detected Walsh code number. |
| uplinkDetectedBranch | [out] | int32 * | This parameter returns the detected branch.Name (value)DescriptionI(0)The detected channel occupies the in-phase branch.Q(1)The detected channel occupies the quadrature branch.I and Q(2)The detected channel occupies the in-phase branch and the quadrature branch. |
| Name (value) | Description |  |  |
| I(0) | The detected channel occupies the in-phase branch. |  |  |
| Q(1) | The detected channel occupies the quadrature branch. |  |  |
| I and Q(2) | The detected channel occupies the in-phase branch and the quadrature branch. |  |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxEVDO_GetError](group____root__ni_r_fmx_e_v_d_o__functions_1gaccaec841794030fe0dda93eb76bb7e60.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__functions__fetch__modacc_1ga631eea8b46747abac17321417ea1e8f3.html language=enus -->
## TOPIC 00126: RFmxEVDO_ModAccFetchPhaseErrorTrace

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__functions__fetch__modacc_1ga631eea8b46747abac17321417ea1e8f3.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__functions__fetch__modacc_1ga631eea8b46747abac17321417ea1e8f3.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the phase error trace of the ModAcc measurement. Syntaxint32 __stdcall RFmxEVDO_ModAccFetchPhaseErrorTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 phaseError[], int32 arraySize, int32 *actualArraySize)ParametersNameDirecti

### RFmxEVDO_ModAccFetchPhaseErrorTrace

Returns the phase error trace of the ModAcc measurement.

#### Syntax

int32 __stdcall RFmxEVDO_ModAccFetchPhaseErrorTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 phaseError[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxEVDO_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| x0 | [out] | float64 * | This parameter is the start parameter. |
| dx | [out] | float64 * | This parameter is the delta parameter. |
| phaseError | [out] | float32[] | This parameter returns the real signal values stored in an array. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxEVDO_GetError](group____root__ni_r_fmx_e_v_d_o__functions_1gaccaec841794030fe0dda93eb76bb7e60.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__functions__fetch__modacc_1ga769063f4ce9f2f741ab7b4db3292b791.html language=enus -->
## TOPIC 00127: RFmxEVDO_ModAccFetchEVMTrace

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__functions__fetch__modacc_1ga769063f4ce9f2f741ab7b4db3292b791.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__functions__fetch__modacc_1ga769063f4ce9f2f741ab7b4db3292b791.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the EVM trace of the ModAcc measurement. Syntaxint32 __stdcall RFmxEVDO_ModAccFetchEVMTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 evm[], int32 arraySize, int32 *actualArraySize)ParametersNameDirectionTypeDescriptioninstr

### RFmxEVDO_ModAccFetchEVMTrace

Returns the EVM trace of the ModAcc measurement.

#### Syntax

int32 __stdcall RFmxEVDO_ModAccFetchEVMTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 evm[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxEVDO_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| x0 | [out] | float64 * | This parameter is the start parameter. |
| dx | [out] | float64 * | This parameter is the delta parameter. |
| evm | [out] | float32[] | This parameter returns the real signal values stored in an array. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxEVDO_GetError](group____root__ni_r_fmx_e_v_d_o__functions_1gaccaec841794030fe0dda93eb76bb7e60.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__functions__fetch__modacc_1ga96ab88393b2f022b648ade57c9ce3691.html language=enus -->
## TOPIC 00128: RFmxEVDO_ModAccFetchConstellationTrace

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__functions__fetch__modacc_1ga96ab88393b2f022b648ade57c9ce3691.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__functions__fetch__modacc_1ga96ab88393b2f022b648ade57c9ce3691.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the constellation trace of the EV-DO measurement. Syntaxint32 __stdcall RFmxEVDO_ModAccFetchConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle constellation[], int32 arraySize, int32 *actualArraySize)ParametersNameDirectionTypeDescr

### RFmxEVDO_ModAccFetchConstellationTrace

Returns the constellation trace of the EV-DO measurement.

#### Syntax

int32 __stdcall RFmxEVDO_ModAccFetchConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle constellation[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxEVDO_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| constellation | [out] | NIComplexSingle[] | This parameter returns an array of complex chips of the corrected signal on which the ModAcc measurements are done. These chips can be used to obtain the constellation diagram. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxEVDO_GetError](group____root__ni_r_fmx_e_v_d_o__functions_1gaccaec841794030fe0dda93eb76bb7e60.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__functions__fetch__modacc_1ga9b41f4d6425c7f16371414d4d054a7d7.html language=enus -->
## TOPIC 00129: RFmxEVDO_ModAccFetchUplinkPeakCDE

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__functions__fetch__modacc_1ga9b41f4d6425c7f16371414d4d054a7d7.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__functions__fetch__modacc_1ga9b41f4d6425c7f16371414d4d054a7d7.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum value among the code domain errors (CDEs), in dB. Syntaxint32 __stdcall RFmxEVDO_ModAccFetchUplinkPeakCDE(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *uplinkPeakCDE, int32 *uplinkPeakCDEWalshCodeNumber, int32 *uplinkPeakCDEBranch)RemarksThe

### RFmxEVDO_ModAccFetchUplinkPeakCDE

Returns the maximum value among the code domain errors (CDEs), in dB.

#### Syntax

int32 __stdcall RFmxEVDO_ModAccFetchUplinkPeakCDE(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *uplinkPeakCDE, int32 *uplinkPeakCDEWalshCodeNumber, int32 *uplinkPeakCDEBranch)

#### Remarks

The CDEs are calculated by projecting the descrambled error vector onto the code domain at a specific spreading factor.

The CDE for every code with a specific spreading factor is defined as the ratio of the mean power of the projection onto that code to the mean power of the composite reference waveform.

A fixed spreading factor of 16 is used.

The CDEs are calculated separately for I and Q branches.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxEVDO_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| uplinkPeakCDE | [out] | float64 * | This parameter returns the maximum value among the CDEs. This value is expressed in dB. |
| uplinkPeakCDEWalshCodeNumber | [out] | int32 * | This parameter returns the code number of the channel corresponding to the Uplink Peak CDE (dB) result. |
| uplinkPeakCDEBranch | [out] | int32 * | This parameter returns the quadrature branch of the peak CDE.Name (value)DescriptionI(0)Returns the channel with peak CDE detected on the in-phase branch.Q(1)Returns the channel with peak CDE detected on the quadrature branch. |
| Name (value) | Description |  |  |
| I(0) | Returns the channel with peak CDE detected on the in-phase branch. |  |  |
| Q(1) | Returns the channel with peak CDE detected on the quadrature branch. |  |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxEVDO_GetError](group____root__ni_r_fmx_e_v_d_o__functions_1gaccaec841794030fe0dda93eb76bb7e60.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__functions__fetch__modacc_1ga9c39ee46fe6a0d82a8f0c5b2a1a2047c.html language=enus -->
## TOPIC 00130: RFmxEVDO_ModAccFetchConstellationTraceSplit

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__functions__fetch__modacc_1ga9c39ee46fe6a0d82a8f0c5b2a1a2047c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__functions__fetch__modacc_1ga9c39ee46fe6a0d82a8f0c5b2a1a2047c.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the constellation trace of the EV-DO measurement. Syntaxint32 __stdcall RFmxEVDO_ModAccFetchConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 constellationI[], float32 constellationQ[], int32 arraySize, int32 *actualArraySize)Paramete

### RFmxEVDO_ModAccFetchConstellationTraceSplit

Returns the constellation trace of the EV-DO measurement.

#### Syntax

int32 __stdcall RFmxEVDO_ModAccFetchConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 constellationI[], float32 constellationQ[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxEVDO_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| constellationI | [out] | float32[] | This parameter returns an array of complex chips of the corrected signal on which the ModAcc measurements are done. These chips can be used to obtain the constellation diagram. |
| constellationQ | [out] | float32[] | This parameter returns an array of complex chips of the corrected signal on which the ModAcc measurements are done. These chips can be used to obtain the constellation diagram. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxEVDO_GetError](group____root__ni_r_fmx_e_v_d_o__functions_1gaccaec841794030fe0dda93eb76bb7e60.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__functions__fetch__modacc_1gab5ab9f7404ac1d7347a6bcc77aa1f2cb.html language=enus -->
## TOPIC 00131: RFmxEVDO_ModAccFetchUplinkNumberOfDetectedChannels

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__functions__fetch__modacc_1gab5ab9f7404ac1d7347a6bcc77aa1f2cb.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__functions__fetch__modacc_1gab5ab9f7404ac1d7347a6bcc77aa1f2cb.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the number of channels detected by the modulation accuracy (ModAcc) measurement. Syntaxint32 __stdcall RFmxEVDO_ModAccFetchUplinkNumberOfDetectedChannels(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 *uplinkNumberOfDetectedChannels)ParametersNameDirectionT

### RFmxEVDO_ModAccFetchUplinkNumberOfDetectedChannels

Returns the number of channels detected by the modulation accuracy (ModAcc) measurement.

#### Syntax

int32 __stdcall RFmxEVDO_ModAccFetchUplinkNumberOfDetectedChannels(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 *uplinkNumberOfDetectedChannels)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxEVDO_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| uplinkNumberOfDetectedChannels | [out] | int32 * | This parameter returns the number of channels detected by the ModAcc. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxEVDO_GetError](group____root__ni_r_fmx_e_v_d_o__functions_1gaccaec841794030fe0dda93eb76bb7e60.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__functions__fetch__modacc_1gad521f1bb324a5e4410e29937a07d6212.html language=enus -->
## TOPIC 00132: RFmxEVDO_ModAccFetchUplinkDetectedDataModulationType

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__functions__fetch__modacc_1gad521f1bb324a5e4410e29937a07d6212.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__functions__fetch__modacc_1gad521f1bb324a5e4410e29937a07d6212.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the modulation type of the uplink data channel. Syntaxint32 __stdcall RFmxEVDO_ModAccFetchUplinkDetectedDataModulationType(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 *uplinkDetectedDataModulationType)ParametersNameDirectionTypeDescriptioninstrumentHandl

### RFmxEVDO_ModAccFetchUplinkDetectedDataModulationType

Returns the modulation type of the uplink data channel.

#### Syntax

int32 __stdcall RFmxEVDO_ModAccFetchUplinkDetectedDataModulationType(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 *uplinkDetectedDataModulationType)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxEVDO_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| uplinkDetectedDataModulationType | [out] | int32 * | This parameter returns the detected modulation type of the uplink data channel.Name (value)DescriptionData Channel Absent(1)The uplink data channel is absent.B4(2)The uplink data channel uses binary phase shift keying (BPSK) with the Walsh function W(4,2).Q4(3)The uplink data channel uses quadrature phase shift keying (QPSK) with the Walsh function W(4,2).Q2(4)The uplink data channel uses QPSK with the Walsh function W(2,1).Q4Q2(5)The uplink data channel uses QPSK with the Walsh functions W(4,2) and W(2,1).E4E2(6)The uplink data channel uses 8-bit phase shift keying (8-PSK) with the Walsh functions W(4,2) and W(2,1). |
| Name (value) | Description |  |  |
| Data Channel Absent(1) | The uplink data channel is absent. |  |  |
| B4(2) | The uplink data channel uses binary phase shift keying (BPSK) with the Walsh function W(4,2). |  |  |
| Q4(3) | The uplink data channel uses quadrature phase shift keying (QPSK) with the Walsh function W(4,2). |  |  |
| Q2(4) | The uplink data channel uses QPSK with the Walsh function W(2,1). |  |  |
| Q4Q2(5) | The uplink data channel uses QPSK with the Walsh functions W(4,2) and W(2,1). |  |  |
| E4E2(6) | The uplink data channel uses 8-bit phase shift keying (8-PSK) with the Walsh functions W(4,2) and W(2,1). |  |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxEVDO_GetError](group____root__ni_r_fmx_e_v_d_o__functions_1gaccaec841794030fe0dda93eb76bb7e60.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__functions__fetch__modacc_1gaeaca2466398ecd16c8a3674e0eecd7a5.html language=enus -->
## TOPIC 00133: RFmxEVDO_ModAccFetchUplinkEVM

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__functions__fetch__modacc_1gaeaca2466398ecd16c8a3674e0eecd7a5.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__functions__fetch__modacc_1gaeaca2466398ecd16c8a3674e0eecd7a5.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the EVM and related values of the EV-DO uplink. Syntaxint32 __stdcall RFmxEVDO_ModAccFetchUplinkEVM(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *uplinkRMSEVM, float64 *uplinkPeakEVM, float64 *uplinkRho, float64 *frequencyError, float64 *chipRateError,

### RFmxEVDO_ModAccFetchUplinkEVM

Returns the EVM and related values of the EV-DO uplink.

#### Syntax

int32 __stdcall RFmxEVDO_ModAccFetchUplinkEVM(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *uplinkRMSEVM, float64 *uplinkPeakEVM, float64 *uplinkRho, float64 *frequencyError, float64 *chipRateError, float64 *uplinkRMSMagnitudeError, float64 *uplinkRMSPhaseError)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxEVDO_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| uplinkRMSEVM | [out] | float64 * | This parameter returns the RMS of the EVM, as a percentage. |
| uplinkPeakEVM | [out] | float64 * | This parameter returns the peak value of the uplink EVM, as a percentage. |
| uplinkRho | [out] | float64 * | This parameter returns the Rho value. |
| frequencyError | [out] | float64 * | This parameter returns the detected frequency error in Hz. |
| chipRateError | [out] | float64 * | This parameter returns the chip rate error in parts per million (ppm). |
| uplinkRMSMagnitudeError | [out] | float64 * | This parameter returns the RMS of the magnitude error, as a percentage. |
| uplinkRMSPhaseError | [out] | float64 * | This parameter returns the RMS of the phase error in degrees. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxEVDO_GetError](group____root__ni_r_fmx_e_v_d_o__functions_1gaccaec841794030fe0dda93eb76bb7e60.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__functions__fetch__obw.html language=enus -->
## TOPIC 00134: OBW

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__functions__fetch__obw.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__functions__fetch__obw.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxEVDO_OBWFetchMeasurementReturns the occupied bandwidth (OBW) measurement. RFmxEVDO_OBWFetchSpectrumFetches the spectrum trace used for the OBW measurement. AttachmentsNone

### OBW

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxEVDO_OBWFetchMeasurement | Returns the occupied bandwidth (OBW) measurement. |
| RFmxEVDO_OBWFetchSpectrum | Fetches the spectrum trace used for the OBW measurement. |

#### Attachments

None

Parent topic:

Fetch

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__functions__fetch__obw_1gaf8882a3fc3cdf54d37ed59b53b5faf6e.html language=enus -->
## TOPIC 00135: RFmxEVDO_OBWFetchSpectrum

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__functions__fetch__obw_1gaf8882a3fc3cdf54d37ed59b53b5faf6e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__functions__fetch__obw_1gaf8882a3fc3cdf54d37ed59b53b5faf6e.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the spectrum trace used for the OBW measurement. Syntaxint32 __stdcall RFmxEVDO_OBWFetchSpectrum(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 spectrum[], int32 arraySize, int32 *actualArraySize)ParametersNameDirectionTypeDescri

### RFmxEVDO_OBWFetchSpectrum

Fetches the spectrum trace used for the OBW measurement.

#### Syntax

int32 __stdcall RFmxEVDO_OBWFetchSpectrum(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 spectrum[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxEVDO_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| x0 | [out] | float64 * | This parameter returns the start frequency. This value is expressed in Hz. |
| dx | [out] | float64 * | This parameter returns the frequency bin spacing. This value is expressed in Hz. |
| spectrum | [out] | float32[] | This parameter returns the averaged power measured at each frequency bin. This value is expressed in dBm. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxEVDO_GetError](group____root__ni_r_fmx_e_v_d_o__functions_1gaccaec841794030fe0dda93eb76bb7e60.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

OBW

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__functions__fetch__obw_1gafb361489d480433662f55e9794693bbf.html language=enus -->
## TOPIC 00136: RFmxEVDO_OBWFetchMeasurement

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__functions__fetch__obw_1gafb361489d480433662f55e9794693bbf.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__functions__fetch__obw_1gafb361489d480433662f55e9794693bbf.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the occupied bandwidth (OBW) measurement. Syntaxint32 __stdcall RFmxEVDO_OBWFetchMeasurement(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *occupiedBandwidth, float64 *absolutePower, float64 *startFrequency, float64 *stopFrequency)ParametersNameDirection

### RFmxEVDO_OBWFetchMeasurement

Returns the occupied bandwidth (OBW) measurement.

#### Syntax

int32 __stdcall RFmxEVDO_OBWFetchMeasurement(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *occupiedBandwidth, float64 *absolutePower, float64 *startFrequency, float64 *stopFrequency)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxEVDO_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| occupiedBandwidth | [out] | float64 * | This parameter returns the occupied bandwidth. This value is expressed in Hz. |
| absolutePower | [out] | float64 * | This parameter returns the total integrated power of the averaged spectrum acquired by the OBW measurement. This value is expressed in dBm. |
| startFrequency | [out] | float64 * | This parameter returns the start frequency of the OBW. This value is expressed in Hz.The OBW is calculated using the following formula: OBW = stop frequency - start frequency |
| stopFrequency | [out] | float64 * | This parameter returns the stop frequency of the OBW. This value is expressed in Hz. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxEVDO_GetError](group____root__ni_r_fmx_e_v_d_o__functions_1gaccaec841794030fe0dda93eb76bb7e60.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

OBW

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__functions__fetch__sem.html language=enus -->
## TOPIC 00137: SEM

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__functions__fetch__sem.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__functions__fetch__sem.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxEVDO_SEMFetchCarrierMeasurementReturns the carrier measurements for the carrier selected by the selector string. Use "carrier<n>" as the selector string to read parameters from this function. RFmxEVDO_SEMFetchCarrierMeasurementArrayReturns the array of carri

### SEM

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxEVDO_SEMFetchCarrierMeasurement | Returns the carrier measurements for the carrier selected by the selector string. Use "carrier<n>" as the selector string to read parameters from this function. |
| RFmxEVDO_SEMFetchCarrierMeasurementArray | Returns the array of carrier measurements. |
| RFmxEVDO_SEMFetchLowerOffsetMargin | Returns the measurement status and margin from the limit line measured in the lower offset segment. |
| RFmxEVDO_SEMFetchLowerOffsetMarginArray | Returns the array of measurement statuses and margins from the limit line measured in the lower offset segments. |
| RFmxEVDO_SEMFetchLowerOffsetPower | Returns the lower offset segment power measurements. Use "offset<n>" as the selector string to read parameters from this function. |
| RFmxEVDO_SEMFetchLowerOffsetPowerArray | Returns the arrays of lower offset segment power measurements. |
| RFmxEVDO_SEMFetchMeasurementStatus | Fetches the SEM measurement status. |
| RFmxEVDO_SEMFetchSpectrum | Fetches the spectrum used for the spectral emission mask (SEM) measurement. |
| RFmxEVDO_SEMFetchTotalCarrierPower | Returns the total carrier power of the selected carrier. |
| RFmxEVDO_SEMFetchUpperOffsetMargin | Returns the measurement status and margin from the limit line measured in the upper offset segment. |
| RFmxEVDO_SEMFetchUpperOffsetMarginArray | Returns the measurement status and margin from the limit line measured in the upper offset segments. |
| RFmxEVDO_SEMFetchUpperOffsetPower | Returns the upper offset segment power measurements. |
| RFmxEVDO_SEMFetchUpperOffsetPowerArray | Returns the arrays of upper offset segment power measurements. |

#### Attachments

None

Parent topic:

Fetch

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__functions__fetch__sem_1ga236a42d92c21db630bc8737d3117bcd9.html language=enus -->
## TOPIC 00138: RFmxEVDO_SEMFetchLowerOffsetPowerArray

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__functions__fetch__sem_1ga236a42d92c21db630bc8737d3117bcd9.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__functions__fetch__sem_1ga236a42d92c21db630bc8737d3117bcd9.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the arrays of lower offset segment power measurements. Syntaxint32 __stdcall RFmxEVDO_SEMFetchLowerOffsetPowerArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 absoluteIntegratedPower[], float64 relativeIntegratedPower[], float64 absolutePeakPower[], f

### RFmxEVDO_SEMFetchLowerOffsetPowerArray

Returns the arrays of lower offset segment power measurements.

#### Syntax

int32 __stdcall RFmxEVDO_SEMFetchLowerOffsetPowerArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 absoluteIntegratedPower[], float64 relativeIntegratedPower[], float64 absolutePeakPower[], float64 peakFrequency[], float64 relativePeakPower[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxEVDO_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| absoluteIntegratedPower | [out] | float64[] | This parameter returns the array of lower (negative) offset segment powers measured. This value is expressed in dBm. |
| relativeIntegratedPower | [out] | float64[] | This parameter returns the array of powers in each lower (negative) offset segment relative to the integrated power of the reference carrier. This value is expressed in dB. |
| absolutePeakPower | [out] | float64[] | This parameter returns the array of peak powers measured in each lower (negative) offset segment. |
| peakFrequency | [out] | float64[] | This parameter returns the array of frequencies at which the peak power occurred in each offset segment. This value is expressed in Hz. |
| relativePeakPower | [out] | float64[] | This parameter returns the array of peak powers in the lower (negative) offset segment relative to the integrated power of the reference carrier. This value is expressed in dB. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxEVDO_GetError](group____root__ni_r_fmx_e_v_d_o__functions_1gaccaec841794030fe0dda93eb76bb7e60.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__functions__fetch__sem_1ga26d807741a0ca2687dedcd11f311941e.html language=enus -->
## TOPIC 00139: RFmxEVDO_SEMFetchUpperOffsetMargin

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__functions__fetch__sem_1ga26d807741a0ca2687dedcd11f311941e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__functions__fetch__sem_1ga26d807741a0ca2687dedcd11f311941e.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the measurement status and margin from the limit line measured in the upper offset segment. Syntaxint32 __stdcall RFmxEVDO_SEMFetchUpperOffsetMargin(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 *measurementStatus, float64 *margin, float64 *marginFrequency

### RFmxEVDO_SEMFetchUpperOffsetMargin

Returns the measurement status and margin from the limit line measured in the upper offset segment.

#### Syntax

int32 __stdcall RFmxEVDO_SEMFetchUpperOffsetMargin(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 *measurementStatus, float64 *margin, float64 *marginFrequency, float64 *marginAbsolutePower, float64 *marginRelativePower)

#### Remarks

Use "offset<n>" as the selector string to read parameters from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, and offset number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used.Examples:"offset0""signal::sig1/offset0""result::r1/offset0""signal::sig1/result::r1/offset0"You can use the RFmxEVDO_BuildOffsetString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| measurementStatus | [out] | int32 * | This parameter indicates the upper offset measurement status. |
| margin | [out] | float64 * | This parameter returns the power at which the margin occurred in the upper (positive) offset segment. This value is expressed in dBm. |
| marginFrequency | [out] | float64 * | This parameter returns the frequency at which the margin occurred in the upper (positive) offset. This value is expressed in Hz. |
| marginAbsolutePower | [out] | float64 * | This parameter returns the margin from the limit mask value. This value is expressed in dB. Margin is defined as the minimum distance between the spectrum and the limit mask. |
| marginRelativePower | [out] | float64 * | This parameter returns the power at which the margin occurred in the upper (positive) offset segment relative to the integrated power of the reference carrier. This value is expressed in dB. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxEVDO_GetError](group____root__ni_r_fmx_e_v_d_o__functions_1gaccaec841794030fe0dda93eb76bb7e60.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__functions__fetch__sem_1ga2b7c722fa4961baefe1993f86bd9a599.html language=enus -->
## TOPIC 00140: RFmxEVDO_SEMFetchUpperOffsetPowerArray

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__functions__fetch__sem_1ga2b7c722fa4961baefe1993f86bd9a599.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__functions__fetch__sem_1ga2b7c722fa4961baefe1993f86bd9a599.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the arrays of upper offset segment power measurements. Syntaxint32 __stdcall RFmxEVDO_SEMFetchUpperOffsetPowerArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 absoluteIntegratedPower[], float64 relativeIntegratedPower[], float64 absolutePeakPower[], f

### RFmxEVDO_SEMFetchUpperOffsetPowerArray

Returns the arrays of upper offset segment power measurements.

#### Syntax

int32 __stdcall RFmxEVDO_SEMFetchUpperOffsetPowerArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 absoluteIntegratedPower[], float64 relativeIntegratedPower[], float64 absolutePeakPower[], float64 peakFrequency[], float64 relativePeakPower[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxEVDO_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| absoluteIntegratedPower | [out] | float64[] | This parameter returns the array of upper (positive) offset segment powers measured. This value is expressed in dBm. |
| relativeIntegratedPower | [out] | float64[] | This parameter returns the array of powers measured in each upper (positive) offset segment relative to the integrated power of the reference carrier. This value is expressed in dB. |
| absolutePeakPower | [out] | float64[] | This parameter returns the array of peak powers measured in each upper (positive) offset segment. The power is measured in dBm. |
| peakFrequency | [out] | float64[] | This parameter returns the array of frequencies at which the peak power occurred in each offset segment. This value is expressed in Hz. |
| relativePeakPower | [out] | float64[] | This parameter returns the array of peak powers measured in each upper (positive) offset segment relative to the integrated power of the reference carrier. This value is expressed in dB. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxEVDO_GetError](group____root__ni_r_fmx_e_v_d_o__functions_1gaccaec841794030fe0dda93eb76bb7e60.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__functions__fetch__sem_1ga48e9ae49225ba9851d7c1a8feb85e4ee.html language=enus -->
## TOPIC 00141: RFmxEVDO_SEMFetchMeasurementStatus

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__functions__fetch__sem_1ga48e9ae49225ba9851d7c1a8feb85e4ee.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__functions__fetch__sem_1ga48e9ae49225ba9851d7c1a8feb85e4ee.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the SEM measurement status. Syntaxint32 __stdcall RFmxEVDO_SEMFetchMeasurementStatus(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 *measurementStatus)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifies the RF

### RFmxEVDO_SEMFetchMeasurementStatus

Fetches the SEM measurement status.

#### Syntax

int32 __stdcall RFmxEVDO_SEMFetchMeasurementStatus(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 *measurementStatus)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxEVDO_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| measurementStatus | [out] | int32 * | This parameter returns the status of the measurement.Name (value)DescriptionFail (0)the signal exceeds the limits given by 3GPP2 C.S0033-D v2.0 tables 4.4.1.3-1 ff.Pass (1)The signal did not exceed the spectrum emission limits. |
| Name (value) | Description |  |  |
| Fail (0) | the signal exceeds the limits given by 3GPP2 C.S0033-D v2.0 tables 4.4.1.3-1 ff. |  |  |
| Pass (1) | The signal did not exceed the spectrum emission limits. |  |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxEVDO_GetError](group____root__ni_r_fmx_e_v_d_o__functions_1gaccaec841794030fe0dda93eb76bb7e60.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__functions__fetch__sem_1ga6f237c4edde382c75c2ae8e1eae0f59d.html language=enus -->
## TOPIC 00142: RFmxEVDO_SEMFetchUpperOffsetMarginArray

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__functions__fetch__sem_1ga6f237c4edde382c75c2ae8e1eae0f59d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__functions__fetch__sem_1ga6f237c4edde382c75c2ae8e1eae0f59d.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the measurement status and margin from the limit line measured in the upper offset segments. Syntaxint32 __stdcall RFmxEVDO_SEMFetchUpperOffsetMarginArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 measurementStatus[], float64 margin[], float64 marginFr

### RFmxEVDO_SEMFetchUpperOffsetMarginArray

Returns the measurement status and margin from the limit line measured in the upper offset segments.

#### Syntax

int32 __stdcall RFmxEVDO_SEMFetchUpperOffsetMarginArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 measurementStatus[], float64 margin[], float64 marginFrequency[], float64 marginAbsolutePower[], float64 marginRelativePower[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxEVDO_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| measurementStatus | [out] | int32[] | This parameter returns the array of upper offset measurement statuses.Name (value)DescriptionFail (0)the signal exceeds the limits given by 3GPP2 C.S0033-D v2.0 tables 4.4.1.3-1 ff.Pass (1)The signal did not exceed the spectrum emission limits. |
| Name (value) | Description |  |  |
| Fail (0) | the signal exceeds the limits given by 3GPP2 C.S0033-D v2.0 tables 4.4.1.3-1 ff. |  |  |
| Pass (1) | The signal did not exceed the spectrum emission limits. |  |  |
| margin | [out] | float64[] | This parameter returns the array of powers at which the margin occurred in each upper (positive) offset segment. This value is expressed in dBm. |
| marginFrequency | [out] | float64[] | This parameter returns the array of frequencies at which the margin occurred in each upper (positive) offset. This value is expressed in Hz. |
| marginAbsolutePower | [out] | float64[] | This parameter returns the array of margins. This value is expressed in dB. Margin is defined as the minimum distance between the spectrum and the limit mask. |
| marginRelativePower | [out] | float64[] | This parameter returns the array of powers at which the margin occurred in each upper (positive) offset segment relative to the integrated power of the reference carrier. This value is expressed in dB. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxEVDO_GetError](group____root__ni_r_fmx_e_v_d_o__functions_1gaccaec841794030fe0dda93eb76bb7e60.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__functions__fetch__sem_1ga7153b0a77c90ececdfdcab9bcb2d5454.html language=enus -->
## TOPIC 00143: RFmxEVDO_SEMFetchUpperOffsetPower

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__functions__fetch__sem_1ga7153b0a77c90ececdfdcab9bcb2d5454.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__functions__fetch__sem_1ga7153b0a77c90ececdfdcab9bcb2d5454.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the upper offset segment power measurements. Syntaxint32 __stdcall RFmxEVDO_SEMFetchUpperOffsetPower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *absoluteIntegratedPower, float64 *relativeIntegratedPower, float64 *absolutePeakPower, float64 *peakFreque

### RFmxEVDO_SEMFetchUpperOffsetPower

Returns the upper offset segment power measurements.

#### Syntax

int32 __stdcall RFmxEVDO_SEMFetchUpperOffsetPower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *absoluteIntegratedPower, float64 *relativeIntegratedPower, float64 *absolutePeakPower, float64 *peakFrequency, float64 *relativePeakPower)

#### Remarks

Use "offset<n>" as the selector string to read parameters from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, and offset number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used.Examples:"offset0""signal::sig1/offset0""result::r1/offset0""signal::sig1/result::r1/offset0"You can use the RFmxEVDO_BuildOffsetString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| absoluteIntegratedPower | [out] | float64 * | This parameter returns the upper (positive) offset segment power measured. This value is expressed in dBm. |
| relativeIntegratedPower | [out] | float64 * | This parameter returns the power in the upper (positive) offset segment relative to the integrated power of the reference carrier. This value is expressed in dB. |
| absolutePeakPower | [out] | float64 * | This parameter returns the peak power measured in the upper (positive) offset segment. The power is measured in dBm. |
| peakFrequency | [out] | float64 * | This parameter returns the frequency at which the peak power occurred in the offset segment. This value is expressed in Hz. |
| relativePeakPower | [out] | float64 * | This parameter returns the peak power in the upper (positive) offset segment relative to the integrated power of the reference carrier. This value is expressed in dB. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxEVDO_GetError](group____root__ni_r_fmx_e_v_d_o__functions_1gaccaec841794030fe0dda93eb76bb7e60.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__functions__fetch__sem_1ga7fe9417538638ffcebf0d513ce836e6c.html language=enus -->
## TOPIC 00144: RFmxEVDO_SEMFetchCarrierMeasurement

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__functions__fetch__sem_1ga7fe9417538638ffcebf0d513ce836e6c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__functions__fetch__sem_1ga7fe9417538638ffcebf0d513ce836e6c.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the carrier measurements for the carrier selected by the selector string. Use "carrier<n>" as the selector string to read parameters from this function. Syntaxint32 __stdcall RFmxEVDO_SEMFetchCarrierMeasurement(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float

### RFmxEVDO_SEMFetchCarrierMeasurement

Returns the carrier measurements for the carrier selected by the selector string. Use "carrier<n>" as the selector string to read parameters from this function.

#### Syntax

int32 __stdcall RFmxEVDO_SEMFetchCarrierMeasurement(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *absoluteIntegratedPower, float64 *relativeIntegratedPower)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used.Examples:"carrier0""signal::sig1/carrier0""result::r1/carrier0""signal::sig1/result::r1/carrier0"You can use the RFmxEVDO_BuildCarrierString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| absoluteIntegratedPower | [out] | float64 * | This parameter returns absolute power of the selected carrier. This value is expressed in dBm. |
| relativeIntegratedPower | [out] | float64 * | This parameter returns the relative power of the selected carrier. This value is expressed in dB. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxEVDO_GetError](group____root__ni_r_fmx_e_v_d_o__functions_1gaccaec841794030fe0dda93eb76bb7e60.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__functions__fetch__sem_1gaee8c84cbffe98b14886ec7ef4b3e1b23.html language=enus -->
## TOPIC 00145: RFmxEVDO_SEMFetchCarrierMeasurementArray

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__functions__fetch__sem_1gaee8c84cbffe98b14886ec7ef4b3e1b23.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__functions__fetch__sem_1gaee8c84cbffe98b14886ec7ef4b3e1b23.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the array of carrier measurements. Syntaxint32 __stdcall RFmxEVDO_SEMFetchCarrierMeasurementArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 absoluteIntegratedPower[], float64 relativeIntegratedPower[], int32 arraySize, int32 *actualArraySize)Paramete

### RFmxEVDO_SEMFetchCarrierMeasurementArray

Returns the array of carrier measurements.

#### Syntax

int32 __stdcall RFmxEVDO_SEMFetchCarrierMeasurementArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 absoluteIntegratedPower[], float64 relativeIntegratedPower[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxEVDO_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| absoluteIntegratedPower | [out] | float64[] | This parameter returns the array of absolute carrier powers. This value is expressed in dBm. |
| relativeIntegratedPower | [out] | float64[] | This parameter returns the array of relative carrier powers. This value is expressed in dB. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxEVDO_GetError](group____root__ni_r_fmx_e_v_d_o__functions_1gaccaec841794030fe0dda93eb76bb7e60.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__functions__fetch__sem_1gafc407e03829ea971fb0613e00da31dfb.html language=enus -->
## TOPIC 00146: RFmxEVDO_SEMFetchTotalCarrierPower

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__functions__fetch__sem_1gafc407e03829ea971fb0613e00da31dfb.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__functions__fetch__sem_1gafc407e03829ea971fb0613e00da31dfb.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the total carrier power of the selected carrier. Syntaxint32 __stdcall RFmxEVDO_SEMFetchTotalCarrierPower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *totalCarrierPower)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis par

### RFmxEVDO_SEMFetchTotalCarrierPower

Returns the total carrier power of the selected carrier.

#### Syntax

int32 __stdcall RFmxEVDO_SEMFetchTotalCarrierPower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *totalCarrierPower)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxEVDO_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| totalCarrierPower | [out] | float64 * | This parameter returns the total carrier power of the selected carrier. This value is expressed in dBm. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxEVDO_GetError](group____root__ni_r_fmx_e_v_d_o__functions_1gaccaec841794030fe0dda93eb76bb7e60.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__functions__fetch__slotphase_1ga37e947b949746c3bac5e2cf97668a221.html language=enus -->
## TOPIC 00147: RFmxEVDO_SlotPhaseFetchPhaseDiscontinuities

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__functions__fetch__slotphase_1ga37e947b949746c3bac5e2cf97668a221.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__functions__fetch__slotphase_1ga37e947b949746c3bac5e2cf97668a221.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the phase discontinuity value for the half-slot boundaries in the measurement interval. Syntaxint32 __stdcall RFmxEVDO_SlotPhaseFetchPhaseDiscontinuities(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 halfSlotphaseDiscontinuity[], int32 arraySize, int32 *

### RFmxEVDO_SlotPhaseFetchPhaseDiscontinuities

Fetches the phase discontinuity value for the half-slot boundaries in the measurement interval.

#### Syntax

int32 __stdcall RFmxEVDO_SlotPhaseFetchPhaseDiscontinuities(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 halfSlotphaseDiscontinuity[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxEVDO_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| halfSlotphaseDiscontinuity | [out] | float64[] | This parameter returns the array of slot phase discontinuity value observed in the measurement interval. This value is expressed in degrees. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxEVDO_GetError](group____root__ni_r_fmx_e_v_d_o__functions_1gaccaec841794030fe0dda93eb76bb7e60.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SlotPhase

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__functions__fetch__slotphase_1gae129ad9cdf0d84def1c0812cbd0eb4c2.html language=enus -->
## TOPIC 00148: RFmxEVDO_SlotPhaseFetchMaximumHalfSlotPhaseDiscontinuity

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__functions__fetch__slotphase_1gae129ad9cdf0d84def1c0812cbd0eb4c2.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__functions__fetch__slotphase_1gae129ad9cdf0d84def1c0812cbd0eb4c2.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the maximum phase discontinuity observed at half-slot boundaries in the measurement interval. Syntaxint32 __stdcall RFmxEVDO_SlotPhaseFetchMaximumHalfSlotPhaseDiscontinuity(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *maximumHalfSlotphaseDiscontinuity)

### RFmxEVDO_SlotPhaseFetchMaximumHalfSlotPhaseDiscontinuity

Fetches the maximum phase discontinuity observed at half-slot boundaries in the measurement interval.

#### Syntax

int32 __stdcall RFmxEVDO_SlotPhaseFetchMaximumHalfSlotPhaseDiscontinuity(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *maximumHalfSlotphaseDiscontinuity)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxEVDO_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| maximumHalfSlotphaseDiscontinuity | [out] | float64 * | This parameter returns the maximum slot phase discontinuity value observed in the measurement interval. This value is expressed in degrees. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxEVDO_GetError](group____root__ni_r_fmx_e_v_d_o__functions_1gaccaec841794030fe0dda93eb76bb7e60.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SlotPhase

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__functions__fetch__slotpower_1ga46690e1387186b8aa9600d894cbcb32c.html language=enus -->
## TOPIC 00149: RFmxEVDO_SlotPowerFetchPowers

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__functions__fetch__slotpower_1ga46690e1387186b8aa9600d894cbcb32c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__functions__fetch__slotpower_1ga46690e1387186b8aa9600d894cbcb32c.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the slot power and slot power delta for all half-slots in the measurement length. The slot power delta is the difference in power between adjacent half-slots. Syntaxint32 __stdcall RFmxEVDO_SlotPowerFetchPowers(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float

### RFmxEVDO_SlotPowerFetchPowers

Fetches the slot power and slot power delta for all half-slots in the measurement length. The slot power delta is the difference in power between adjacent half-slots.

#### Syntax

int32 __stdcall RFmxEVDO_SlotPowerFetchPowers(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 halfSlotpower[], float64 halfSlotpowerDelta[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxEVDO_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| halfSlotpower | [out] | float64[] | This parameter returns the array of half slot powers. This value is expressed in dBm. |
| halfSlotpowerDelta | [out] | float64[] | This parameter returns the array of half slot power delta powers. This value is expressed in dB. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxEVDO_GetError](group____root__ni_r_fmx_e_v_d_o__functions_1gaccaec841794030fe0dda93eb76bb7e60.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SlotPower

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__functions__select__measurement_1gabcf5f6a3521062bd22d99be7e13eb1e6.html language=enus -->
## TOPIC 00150: RFmxEVDO_SelectMeasurements

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__functions__select__measurement_1gabcf5f6a3521062bd22d99be7e13eb1e6.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__functions__select__measurement_1gabcf5f6a3521062bd22d99be7e13eb1e6.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enables all the measurements that you specify in the Measurements parameter and disables all other measurements. Syntaxint32 __stdcall RFmxEVDO_SelectMeasurements(niRFmxInstrHandle instrumentHandle, char selectorString[], uInt32 measurements, int32 enableAllTraces)ParametersNameDirectionTypeDescript

### RFmxEVDO_SelectMeasurements

Enables all the measurements that you specify in the **Measurements** parameter and disables all other measurements.

#### Syntax

int32 __stdcall RFmxEVDO_SelectMeasurements(niRFmxInstrHandle instrumentHandle, char selectorString[], uInt32 measurements, int32 enableAllTraces)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Examples:"""signal::sig1"You can use the RFmxEVDO_BuildSignalString function to build the selector string. |
| measurements | [in] | uInt32 | This parameter specifies the measurements to perform.Name (value)DescriptionModAcc (0)Enables the ModAcc measurement.ACP (1)Enables the ACP measurement.CHP (2)Enables the CHP measurement.OBW (3)Enables the OBW measurement.SEM (4)Enables the SEM measurement.CDA (5)Enables the CDA measurement.SlotPhase (6)Enables the SlotPhase measurement.SlotPower (7)Enables the SlotPower measurement.The default is an empty array. |
| Name (value) | Description |  |  |
| ModAcc (0) | Enables the ModAcc measurement. |  |  |
| ACP (1) | Enables the ACP measurement. |  |  |
| CHP (2) | Enables the CHP measurement. |  |  |
| OBW (3) | Enables the OBW measurement. |  |  |
| SEM (4) | Enables the SEM measurement. |  |  |
| CDA (5) | Enables the CDA measurement. |  |  |
| SlotPhase (6) | Enables the SlotPhase measurement. |  |  |
| SlotPower (7) | Enables the SlotPower measurement. |  |  |
| enableAllTraces | [in] | int32 | This parameter specifies whether to enable all traces for the selected measurement. The default value is FALSE. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxEVDO_GetError](group____root__ni_r_fmx_e_v_d_o__functions_1gaccaec841794030fe0dda93eb76bb7e60.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Select Measurement

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__functions__set__and__get__attributes.html language=enus -->
## TOPIC 00151: Set and Get Attributes

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__functions__set__and__get__attributes.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__functions__set__and__get__attributes.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsGet AttributesSet AttributesGroup membersNoneAttachmentsNone

### Set and Get Attributes

#### Groups

- Get Attributes
- Set Attributes

#### Group members

None

#### Attachments

None

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__functions__set__and__get__attributes__get__attributes_1ga05b3e701322057200569e9eb2e8d89a5.html language=enus -->
## TOPIC 00152: RFmxEVDO_GetAttributeF64

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__functions__set__and__get__attributes__get__attributes_1ga05b3e701322057200569e9eb2e8d89a5.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__functions__set__and__get__attributes__get__attributes_1ga05b3e701322057200569e9eb2e8d89a5.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 64-bit floating point number (float64) attribute. Syntaxint32 __stdcall RFmxEVDO_GetAttributeF64(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, float64 *attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIden

### RFmxEVDO_GetAttributeF64

Queries the value of an RFmx 64-bit floating point number (float64) attribute.

#### Syntax

int32 __stdcall RFmxEVDO_GetAttributeF64(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, float64 *attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxEVDO_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxEVDO_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | float64 * | Returns the current value of the attribute. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxEVDO_GetError](group____root__ni_r_fmx_e_v_d_o__functions_1gaccaec841794030fe0dda93eb76bb7e60.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__functions__set__and__get__attributes__get__attributes_1ga0ea0aa6f6e7fda543728ee68a2317ce9.html language=enus -->
## TOPIC 00153: RFmxEVDO_GetAttributeU32Array

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__functions__set__and__get__attributes__get__attributes_1ga0ea0aa6f6e7fda543728ee68a2317ce9.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__functions__set__and__get__attributes__get__attributes_1ga0ea0aa6f6e7fda543728ee68a2317ce9.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 32-bit unsigned integer (uInt32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for ar

### RFmxEVDO_GetAttributeU32Array

Queries the value of an RFmx 32-bit unsigned integer (uInt32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer.

#### Syntax

int32 __stdcall RFmxEVDO_GetAttributeU32Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt32 attrVal[], int32 arraySize, int32 *actualArraySize)

#### Remarks

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxEVDO_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxEVDO_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | uInt32[] | Returns the current value of the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxEVDO_GetError](group____root__ni_r_fmx_e_v_d_o__functions_1gaccaec841794030fe0dda93eb76bb7e60.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__functions__set__and__get__attributes__get__attributes_1ga386725ead604a77d2ce105f64d60c009.html language=enus -->
## TOPIC 00154: RFmxEVDO_GetAttributeI8Array

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__functions__set__and__get__attributes__get__attributes_1ga386725ead604a77d2ce105f64d60c009.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__functions__set__and__get__attributes__get__attributes_1ga386725ead604a77d2ce105f64d60c009.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 8-bit integer (int8) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and

### RFmxEVDO_GetAttributeI8Array

Queries the value of an RFmx 8-bit integer (int8) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer.

#### Syntax

int32 __stdcall RFmxEVDO_GetAttributeI8Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int8 attrVal[], int32 arraySize, int32 *actualArraySize)

#### Remarks

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxEVDO_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxEVDO_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | int8[] | Returns the current value of the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxEVDO_GetError](group____root__ni_r_fmx_e_v_d_o__functions_1gaccaec841794030fe0dda93eb76bb7e60.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__functions__set__and__get__attributes__get__attributes_1ga3c36b7e39e6298cc9c13b1b2c07d60c4.html language=enus -->
## TOPIC 00155: RFmxEVDO_GetAttributeI16

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__functions__set__and__get__attributes__get__attributes_1ga3c36b7e39e6298cc9c13b1b2c07d60c4.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__functions__set__and__get__attributes__get__attributes_1ga3c36b7e39e6298cc9c13b1b2c07d60c4.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 16-bit integer (int16) attribute. Syntaxint32 __stdcall RFmxEVDO_GetAttributeI16(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int16 *attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies the RFmx se

### RFmxEVDO_GetAttributeI16

Queries the value of an RFmx 16-bit integer (int16) attribute.

#### Syntax

int32 __stdcall RFmxEVDO_GetAttributeI16(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int16 *attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxEVDO_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxEVDO_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | int16 * | Returns the current value of the attribute. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxEVDO_GetError](group____root__ni_r_fmx_e_v_d_o__functions_1gaccaec841794030fe0dda93eb76bb7e60.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__functions__set__and__get__attributes__get__attributes_1gafb2c3479fecc933ecb11d210f56c646d.html language=enus -->
## TOPIC 00156: RFmxEVDO_GetAttributeU8Array

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__functions__set__and__get__attributes__get__attributes_1gafb2c3479fecc933ecb11d210f56c646d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__functions__set__and__get__attributes__get__attributes_1gafb2c3479fecc933ecb11d210f56c646d.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 8-bit unsigned integer (uInt8) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arra

### RFmxEVDO_GetAttributeU8Array

Queries the value of an RFmx 8-bit unsigned integer (uInt8) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer.

#### Syntax

int32 __stdcall RFmxEVDO_GetAttributeU8Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt8 attrVal[], int32 arraySize, int32 *actualArraySize)

#### Remarks

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxEVDO_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxEVDO_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | uInt8[] | Returns the current value of the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxEVDO_GetError](group____root__ni_r_fmx_e_v_d_o__functions_1gaccaec841794030fe0dda93eb76bb7e60.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__functions__set__and__get__attributes__set__attributes.html language=enus -->
## TOPIC 00157: Set Attributes

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__functions__set__and__get__attributes__set__attributes.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__functions__set__and__get__attributes__set__attributes.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxEVDO_SetAttributeF32Sets the value of an RFmx 32-bit floating point number (float32) attribute. RFmxEVDO_SetAttributeF32ArraySets the value of an RFmx 32-bit floating point number (float32) attribute. You must provide a char array to serve as a buffer for th

### Set Attributes

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxEVDO_SetAttributeF32 | Sets the value of an RFmx 32-bit floating point number (float32) attribute. |
| RFmxEVDO_SetAttributeF32Array | Sets the value of an RFmx 32-bit floating point number (float32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. |
| RFmxEVDO_SetAttributeF64 | Sets the value of an RFmx 64-bit floating point number (float64) attribute. |
| RFmxEVDO_SetAttributeF64Array | Sets the value of an RFmx 64-bit floating point number (float64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. |
| RFmxEVDO_SetAttributeI16 | Sets the value of an RFmx 16-bit integer (int16) attribute. |
| RFmxEVDO_SetAttributeI32 | Sets the value of an RFmx 32-bit integer (int32) attribute. |
| RFmxEVDO_SetAttributeI32Array | Sets the value of an RFmx 32-bit integer (int32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. |
| RFmxEVDO_SetAttributeI64 | Sets the value of an RFmx 64-bit integer (int64) attribute. |
| RFmxEVDO_SetAttributeI64Array | Sets the value of an RFmx 64-bit integer (int64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. |
| RFmxEVDO_SetAttributeI8 | Sets the value of an RFmx 8-bit integer (int8) attribute. |
| RFmxEVDO_SetAttributeI8Array | Sets the value of an RFmx 8-bit integer (int8) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. |
| RFmxEVDO_SetAttributeNIComplexDoubleArray | Sets the value of an RFmx NIComplexDouble attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. |
| RFmxEVDO_SetAttributeNIComplexSingleArray | Sets the value of an RFmx NIComplexSingle attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. |
| RFmxEVDO_SetAttributeString | Sets the value of an RFmx string attribute. |
| RFmxEVDO_SetAttributeU16 | Sets the value of an RFmx 16-bit unsigned integer (uInt16) attribute. |
| RFmxEVDO_SetAttributeU32 | Sets the value of an RFmx 32-bit unsigned integer (uInt32) attribute. |
| RFmxEVDO_SetAttributeU32Array | Sets the value of an RFmx 32-bit unsigned integer (uInt32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. |
| RFmxEVDO_SetAttributeU64Array | Sets the value of an RFmx 64-bit unsigned integer (uInt64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. |
| RFmxEVDO_SetAttributeU8 | Sets the value of an RFmx 8-bit unsigned integer (uInt8) attribute. |
| RFmxEVDO_SetAttributeU8Array | Sets the value of an RFmx 8-bit unsigned integer (uInt8) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. |

#### Attachments

None

Parent topic:

Set and Get Attributes

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__functions__set__and__get__attributes__set__attributes_1ga59b8cd9c436306c1717b968c414f7db4.html language=enus -->
## TOPIC 00158: RFmxEVDO_SetAttributeI8

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__functions__set__and__get__attributes__set__attributes_1ga59b8cd9c436306c1717b968c414f7db4.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__functions__set__and__get__attributes__set__attributes_1ga59b8cd9c436306c1717b968c414f7db4.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 8-bit integer (int8) attribute. Syntaxint32 __stdcall RFmxEVDO_SetAttributeI8(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int8 attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies the RFmx session. Y

### RFmxEVDO_SetAttributeI8

Sets the value of an RFmx 8-bit integer (int8) attribute.

#### Syntax

int32 __stdcall RFmxEVDO_SetAttributeI8(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int8 attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxEVDO_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxEVDO_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | int8 | Pass the value to which you want to set the attribute |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxEVDO_GetError](group____root__ni_r_fmx_e_v_d_o__functions_1gaccaec841794030fe0dda93eb76bb7e60.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__functions__set__and__get__attributes__set__attributes_1ga8d48bc2367a9c3b2729e15d1eb3a0964.html language=enus -->
## TOPIC 00159: RFmxEVDO_SetAttributeI64Array

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__functions__set__and__get__attributes__set__attributes_1ga8d48bc2367a9c3b2729e15d1eb3a0964.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__functions__set__and__get__attributes__set__attributes_1ga8d48bc2367a9c3b2729e15d1eb3a0964.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 64-bit integer (int64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. Syntaxint32 __stdcall RFmxEVDO_SetAttributeI64Array(niRFmxInstrHandle instrumentHandle, char selectorString

### RFmxEVDO_SetAttributeI64Array

Sets the value of an RFmx 64-bit integer (int64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter.

#### Syntax

int32 __stdcall RFmxEVDO_SetAttributeI64Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int64 attrVal[], int32 arraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxEVDO_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxEVDO_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | int64[] | Pass the value to which you want to set the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxEVDO_GetError](group____root__ni_r_fmx_e_v_d_o__functions_1gaccaec841794030fe0dda93eb76bb7e60.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__functions__set__and__get__attributes__set__attributes_1ga9245b6dd5a2df136aefa2648bc00139b.html language=enus -->
## TOPIC 00160: RFmxEVDO_SetAttributeI8Array

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__functions__set__and__get__attributes__set__attributes_1ga9245b6dd5a2df136aefa2648bc00139b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__functions__set__and__get__attributes__set__attributes_1ga9245b6dd5a2df136aefa2648bc00139b.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 8-bit integer (int8) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. Syntaxint32 __stdcall RFmxEVDO_SetAttributeI8Array(niRFmxInstrHandle instrumentHandle, char selectorString[],

### RFmxEVDO_SetAttributeI8Array

Sets the value of an RFmx 8-bit integer (int8) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter.

#### Syntax

int32 __stdcall RFmxEVDO_SetAttributeI8Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int8 attrVal[], int32 arraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxEVDO_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxEVDO_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | int8[] | Pass the value to which you want to set the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxEVDO_GetError](group____root__ni_r_fmx_e_v_d_o__functions_1gaccaec841794030fe0dda93eb76bb7e60.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__functions__set__and__get__attributes__set__attributes_1gaa3788e340a74272e8fe2e7d16348054b.html language=enus -->
## TOPIC 00161: RFmxEVDO_SetAttributeF32

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__functions__set__and__get__attributes__set__attributes_1gaa3788e340a74272e8fe2e7d16348054b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__functions__set__and__get__attributes__set__attributes_1gaa3788e340a74272e8fe2e7d16348054b.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 32-bit floating point number (float32) attribute. Syntaxint32 __stdcall RFmxEVDO_SetAttributeF32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, float32 attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifi

### RFmxEVDO_SetAttributeF32

Sets the value of an RFmx 32-bit floating point number (float32) attribute.

#### Syntax

int32 __stdcall RFmxEVDO_SetAttributeF32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, float32 attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxEVDO_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxEVDO_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | float32 | Pass the value to which you want to set the attribute |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxEVDO_GetError](group____root__ni_r_fmx_e_v_d_o__functions_1gaccaec841794030fe0dda93eb76bb7e60.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__functions__set__and__get__attributes__set__attributes_1gafd234af5f562bbc7c764a4e036c3ce5c.html language=enus -->
## TOPIC 00162: RFmxEVDO_SetAttributeI32Array

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__functions__set__and__get__attributes__set__attributes_1gafd234af5f562bbc7c764a4e036c3ce5c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__functions__set__and__get__attributes__set__attributes_1gafd234af5f562bbc7c764a4e036c3ce5c.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 32-bit integer (int32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. Syntaxint32 __stdcall RFmxEVDO_SetAttributeI32Array(niRFmxInstrHandle instrumentHandle, char selectorString

### RFmxEVDO_SetAttributeI32Array

Sets the value of an RFmx 32-bit integer (int32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter.

#### Syntax

int32 __stdcall RFmxEVDO_SetAttributeI32Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int32 attrVal[], int32 arraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxEVDO_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxEVDO_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | int32[] | Pass the value to which you want to set the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxEVDO_GetError](group____root__ni_r_fmx_e_v_d_o__functions_1gaccaec841794030fe0dda93eb76bb7e60.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__functions__utility.html language=enus -->
## TOPIC 00163: Utility

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__functions__utility.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__functions__utility.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxEVDO_CheckMeasurementStatusChecks the status of the measurement. Use this function to check for any errors that may occur during measurement or to check whether the measurement is complete and results are available. RFmxEVDO_CommitCommits settings to the har

### Utility

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxEVDO_CheckMeasurementStatus | Checks the status of the measurement. Use this function to check for any errors that may occur during measurement or to check whether the measurement is complete and results are available. |
| RFmxEVDO_Commit | Commits settings to the hardware. Calling this function is optional. RFmxEVDO commits settings to the hardware when you call the RFmxEVDO_Initiate function. |
| RFmxEVDO_InitializeFromNIRFSASession | Creates an RFmx session from an existing NI-RFSA session. This function resets all the NI-RFSA attributes to their default values and stops export of all external signals and events. This function takes in an active NI-RFSA instrument handle and returns an RFmx Handle Out that identifies the device in all the subsequent RFmx functions. |
| RFmxEVDO_ResetAttribute | Resets an attribute that you specify in the attributeID parameter to default values. |
| RFmxEVDO_ResetToDefault | Resets a signal to the default values. |
| RFmxEVDO_WaitForAcquisitionComplete | Waits and blocks the data flow until the acquisition is done. This function is typically called after the specific Initiate function. |
| RFmxEVDO_WaitForMeasurementComplete | Waits for the specified number for seconds for all the measurements to complete. |

#### Attachments

None

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__functions__utility_1ga174968af11dc7ed988cc3d783b780a2a.html language=enus -->
## TOPIC 00164: RFmxEVDO_WaitForAcquisitionComplete

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__functions__utility_1ga174968af11dc7ed988cc3d783b780a2a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__functions__utility_1ga174968af11dc7ed988cc3d783b780a2a.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Waits and blocks the data flow until the acquisition is done. This function is typically called after the specific Initiate function. Syntaxint32 __stdcall RFmxEVDO_WaitForAcquisitionComplete(niRFmxInstrHandle instrumentHandle, float64 timeout)RemarksThis function is a wrapper over the RFmx Instrume

### RFmxEVDO_WaitForAcquisitionComplete

Waits and blocks the data flow until the acquisition is done. This function is typically called after the specific Initiate function.

#### Syntax

int32 __stdcall RFmxEVDO_WaitForAcquisitionComplete(niRFmxInstrHandle instrumentHandle, float64 timeout)

#### Remarks

This function is a wrapper over the RFmx Instruments API, and calls the [RFmxInstr_WaitForAcquisitionComplete](/csh?context=rfmxinstr_rfmxinstrcref_function_wait_for_acquisition_complete) function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxEVDO_Initialize function. |
| timeout | [in] | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxEVDO_GetError](group____root__ni_r_fmx_e_v_d_o__functions_1gaccaec841794030fe0dda93eb76bb7e60.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__functions__utility_1gaac9262e86124d28615e1f82e571f9af4.html language=enus -->
## TOPIC 00165: RFmxEVDO_InitializeFromNIRFSASession

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__functions__utility_1gaac9262e86124d28615e1f82e571f9af4.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__functions__utility_1gaac9262e86124d28615e1f82e571f9af4.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an RFmx session from an existing NI-RFSA session. This function resets all the NI-RFSA attributes to their default values and stops export of all external signals and events. This function takes in an active NI-RFSA instrument handle and returns an RFmx Handle Out that identifies the device

### RFmxEVDO_InitializeFromNIRFSASession

Creates an RFmx session from an existing NI-RFSA session. This function resets all the NI-RFSA attributes to their default values and stops export of all external signals and events. This function takes in an active NI-RFSA instrument handle and returns an RFmx Handle Out that identifies the device in all the subsequent RFmx functions.

#### Syntax

int32 __stdcall RFmxEVDO_InitializeFromNIRFSASession(uInt32 nirfsaSession, niRFmxInstrHandle *handleOut)

#### Remarks

This function is a wrapper over the RFmx Instruments API, and calls the [RFmxInstr_InitializeFromNIRFSASession](/csh?context=rfmxinstr_rfmxinstrcref_function_initialize_from_nirfsa_session) function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| nirfsaSession | [in] | uInt32 | Specifies the NIRFSA session handle of the device to initialize. |
| handleOut | [out] | niRFmxInstrHandle * | Returns an RFmx instrument session. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxEVDO_GetError](group____root__ni_r_fmx_e_v_d_o__functions_1gaccaec841794030fe0dda93eb76bb7e60.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group____root__ni_r_fmx_e_v_d_o__functions__utility_1gaf07fd26d34b15b8466fbc409d0a88a3a.html language=enus -->
## TOPIC 00166: RFmxEVDO_ResetToDefault

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group____root__ni_r_fmx_e_v_d_o__functions__utility_1gaf07fd26d34b15b8466fbc409d0a88a3a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_e_v_d_o__functions__utility_1gaf07fd26d34b15b8466fbc409d0a88a3a.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Resets a signal to the default values. Syntaxint32 __stdcall RFmxEVDO_ResetToDefault(niRFmxInstrHandle instrumentHandle, char selectorString[])ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifies the RFmx session refnum. This parameter is obtained from

### RFmxEVDO_ResetToDefault

Resets a signal to the default values.

#### Syntax

int32 __stdcall RFmxEVDO_ResetToDefault(niRFmxInstrHandle instrumentHandle, char selectorString[])

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Examples:"""signal::sig1"You can use the RFmxEVDO_BuildSignalString function to build the selector string. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxEVDO_GetError](group____root__ni_r_fmx_e_v_d_o__functions_1gaccaec841794030fe0dda93eb76bb7e60.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfmxevdo-c-api-ref path=group__root__ni_r_fmx_e_v_d_o.html language=enus -->
## TOPIC 00167: niRFmxEVDO.h

- bundle_id: `rfmxevdo-c-api-ref`
- source_path: `group__root__ni_r_fmx_e_v_d_o.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-c-api-ref/raw/resource/enus/group__root__ni_r_fmx_e_v_d_o.html
- document_id: `rfmxevdo-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsAttributesFunctionsGroup membersNoneAttachmentsNone

### niRFmxEVDO.h

#### Groups

- Attributes
- Functions

#### Group members

None

#### Attachments

None
