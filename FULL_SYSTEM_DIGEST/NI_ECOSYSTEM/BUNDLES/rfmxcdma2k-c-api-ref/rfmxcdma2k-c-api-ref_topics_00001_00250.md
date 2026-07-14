# NI DOCUMENT BUNDLE: rfmxcdma2k-c-api-ref

<!--NI_BUNDLE_CHUNK bundle=rfmxcdma2k-c-api-ref start=1 end=250 -->
<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes_1ga17a45f6c7504637a7d5015650b67699d.html language=enus -->
## TOPIC 00001: RFMXCDMA2K_ATTR_BAND_CLASS

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes_1ga17a45f6c7504637a7d5015650b67699d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes_1ga17a45f6c7504637a7d5015650b67699d.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the band in which the channel is located as defined in Section: 1.5, Table 1.5- Band Class List, of the 3GPP2 C.S0057-F specification v1.0. SyntaxRFMXCDMA2K_ATTR_BAND_CLASSNumeric ValueData TypeAccessApplies To6291472int32Read/WriteN/ARemarks You do not need to use a selector string to con

### RFMXCDMA2K_ATTR_BAND_CLASS

Specifies the band in which the channel is located as defined in Section: 1.5, Table 1.5- Band Class List, of the 3GPP2 C.S0057-F specification v1.0.

#### Syntax

RFMXCDMA2K_ATTR_BAND_CLASS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6291472 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **0**. Valid values are 0 to 12, 14 and 15.

Parent topic:

Attributes

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes_1ga3d1c8b4fef596c9b779aab8a4b248f58.html language=enus -->
## TOPIC 00002: RFMXCDMA2K_ATTR_RESULT_FETCH_TIMEOUT

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes_1ga3d1c8b4fef596c9b779aab8a4b248f58.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes_1ga3d1c8b4fef596c9b779aab8a4b248f58.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the time to wait before results are available in the RFmxCDMA2k Attribute. This value is expressed in seconds. SyntaxRFMXCDMA2K_ATTR_RESULT_FETCH_TIMEOUTNumeric ValueData TypeAccessApplies To6340608float64Read/WriteN/ARemarks Set this value to a time longer than expected for fetching the m

### RFMXCDMA2K_ATTR_RESULT_FETCH_TIMEOUT

Specifies the time to wait before results are available in the RFmxCDMA2k Attribute. This value is expressed in seconds.

#### Syntax

RFMXCDMA2K_ATTR_RESULT_FETCH_TIMEOUT

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6340608 | float64 | Read/Write | N/A |

#### Remarks

Set this value to a time longer than expected for fetching the measurement. A value of -1 specifies that the RFmxCDMA2k Attribute waits until the measurement is complete before fetching the measurement.

The default value is 10 seconds.

Parent topic:

Attributes

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes_1ga43dccf09ab795d9ee5a438ed0921dc50.html language=enus -->
## TOPIC 00003: RFMXCDMA2K_ATTR_REFERENCE_LEVEL_HEADROOM

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes_1ga43dccf09ab795d9ee5a438ed0921dc50.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes_1ga43dccf09ab795d9ee5a438ed0921dc50.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the margin RFmx adds to the RFMXCDMA2K_ATTR_REFERENCE_LEVEL attribute. The margin avoids clipping and overflow warnings if the input signal exceeds the configured reference level. SyntaxRFMXCDMA2K_ATTR_REFERENCE_LEVEL_HEADROOMNumeric ValueData TypeAccessApplies To6295548float64Read/WriteN/

### RFMXCDMA2K_ATTR_REFERENCE_LEVEL_HEADROOM

Specifies the margin RFmx adds to the [RFMXCDMA2K_ATTR_REFERENCE_LEVEL](group____root__ni_r_fmx_c_d_m_a2k__attributes_1ga96e417de6d5f3b1936d0a24b4bc8e0d2.html) attribute. The margin avoids clipping and overflow warnings if the input signal exceeds the configured reference level.

#### Syntax

RFMXCDMA2K_ATTR_REFERENCE_LEVEL_HEADROOM

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6295548 | float64 | Read/Write | N/A |

#### Remarks

RFmx configures the input gain to avoid clipping and associated overflow warnings provided the instantaneous power of the input signal remains within the Reference Level plus the Reference Level Headroom. If you know the input power of the signal precisely or previously included the margin in the Reference Level, you could improve the signal-to-noise ratio by reducing the Reference Level Headroom.

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

**Supported devices**: PXIe-5668R, PXIe-5830/5831/5832/5840/5841/5842/5860.

**Default values**

| Name (value) | Description |
| --- | --- |
| PXIe-5668 | 6 dB |
| PXIe-5830/5831/5832/5841/5842/5860 | 1 dB |
| PXIe-5840 | 0 dB |

Parent topic:

Attributes

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes_1ga96e417de6d5f3b1936d0a24b4bc8e0d2.html language=enus -->
## TOPIC 00004: RFMXCDMA2K_ATTR_REFERENCE_LEVEL

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes_1ga96e417de6d5f3b1936d0a24b4bc8e0d2.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes_1ga96e417de6d5f3b1936d0a24b4bc8e0d2.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the reference level, which represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and V[pk-pk] for baseband devices. SyntaxRFMXCDMA2K_ATTR_REFERENCE_LEVELNumeric ValueData TypeAccessApplies To6291458float64Read/WriteN/ARemarks You do not

### RFMXCDMA2K_ATTR_REFERENCE_LEVEL

Specifies the reference level, which represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and V<sub>pk-pk</sub> for baseband devices.

#### Syntax

RFMXCDMA2K_ATTR_REFERENCE_LEVEL

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6291458 | float64 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value of this attribute is hardware dependent.

Parent topic:

Attributes

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__acp.html language=enus -->
## TOPIC 00005: ACP

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__acp.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__acp.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsAdvancedAveragingCarrierFFTOffsetRBW FilterResultsSweep TimeGroup membersNameDescriptionRFMXCDMA2K_ATTR_ACP_ALL_TRACES_ENABLEDSpecifies whether to enable the traces to be stored and retrieved after performing the ACP measurement. RFMXCDMA2K_ATTR_ACP_MEASUREMENT_ENABLEDSpecifies whether to enab

### ACP

#### Groups

- Advanced
- Averaging
- Carrier
- FFT
- Offset
- RBW Filter
- Results
- Sweep Time

#### Group members

| Name | Description |
| --- | --- |
| RFMXCDMA2K_ATTR_ACP_ALL_TRACES_ENABLED | Specifies whether to enable the traces to be stored and retrieved after performing the ACP measurement. |
| RFMXCDMA2K_ATTR_ACP_MEASUREMENT_ENABLED | Specifies whether to enable the ACP measurement. |
| RFMXCDMA2K_ATTR_ACP_MEASUREMENT_METHOD | Specifies the method for performing the ACP measurement. |
| RFMXCDMA2K_ATTR_ACP_NOISE_COMPENSATION_ENABLED | Specifies whether to enable compensation of the channel powers for the inherent noise floor of the signal analyzer. |
| RFMXCDMA2K_ATTR_ACP_NUMBER_OF_ANALYSIS_THREADS | Specifies the maximum number of threads used for parallelism for the ACP measurement. |

#### Attachments

None

Parent topic:

Attributes

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__acp_1gacd47a38ba0c82719ed418f034c93f97d.html language=enus -->
## TOPIC 00006: RFMXCDMA2K_ATTR_ACP_MEASUREMENT_ENABLED

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__acp_1gacd47a38ba0c82719ed418f034c93f97d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__acp_1gacd47a38ba0c82719ed418f034c93f97d.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the ACP measurement. SyntaxRFMXCDMA2K_ATTR_ACP_MEASUREMENT_ENABLEDNumeric ValueData TypeAccessApplies To6295552int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Str

### RFMXCDMA2K_ATTR_ACP_MEASUREMENT_ENABLED

Specifies whether to enable the ACP measurement.

#### Syntax

RFMXCDMA2K_ATTR_ACP_MEASUREMENT_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6295552 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is FALSE.

Parent topic:

ACP

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__acp__advanced.html language=enus -->
## TOPIC 00007: Advanced

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__acp__advanced.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__acp__advanced.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXCDMA2K_ATTR_ACP_FAR_IF_OUTPUT_POWER_OFFSETSpecifies the offset by which to adjust the IF output power level for offset channels that are far from the carrier channel to improve the dynamic range. This value is expressed in dB. This attribute is used only if

### Advanced

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXCDMA2K_ATTR_ACP_FAR_IF_OUTPUT_POWER_OFFSET | Specifies the offset by which to adjust the IF output power level for offset channels that are far from the carrier channel to improve the dynamic range. This value is expressed in dB. This attribute is used only if you set the RFMXCDMA2K_ATTR_ACP_MEASUREMENT_METHOD attribute to Dynamic Range and set the RFMXCDMA2K_ATTR_ACP_IF_OUTPUT_POWER_OFFSET_AUTO attribute to False. |
| RFMXCDMA2K_ATTR_ACP_IF_OUTPUT_POWER_OFFSET_AUTO | Specifies whether the measurement computes an IF output power level offset for the offset channels to improve the dynamic range of the ACP measurement. This attribute is used only if you set the RFMXCDMA2K_ATTR_ACP_MEASUREMENT_METHOD attribute to Dynamic Range. |
| RFMXCDMA2K_ATTR_ACP_NEAR_IF_OUTPUT_POWER_OFFSET | Specifies the offset by which to adjust the IF output power level for offset channels that are near the carrier channel to improve the dynamic range. This value is expressed in dB. This attribute is used only if you set the RFMXCDMA2K_ATTR_ACP_MEASUREMENT_METHOD attribute to Dynamic Range and set the RFMXCDMA2K_ATTR_ACP_IF_OUTPUT_POWER_OFFSET_AUTO attribute to False. |
| RFMXCDMA2K_ATTR_ACP_SEQUENTIAL_FFT_SIZE | Specifies the FFT size, when you set the RFMXCDMA2K_ATTR_ACP_MEASUREMENT_METHOD attribute to Sequential FFT. |

#### Attachments

None

Parent topic:

ACP

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__acp__advanced_1ga15c502242d75dcb0dc258c08e37dd65f.html language=enus -->
## TOPIC 00008: RFMXCDMA2K_ATTR_ACP_IF_OUTPUT_POWER_OFFSET_AUTO

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__acp__advanced_1ga15c502242d75dcb0dc258c08e37dd65f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__acp__advanced_1ga15c502242d75dcb0dc258c08e37dd65f.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement computes an IF output power level offset for the offset channels to improve the dynamic range of the ACP measurement. This attribute is used only if you set the RFMXCDMA2K_ATTR_ACP_MEASUREMENT_METHOD attribute to Dynamic Range. SyntaxRFMXCDMA2K_ATTR_ACP_IF_OUTPUT_PO

### RFMXCDMA2K_ATTR_ACP_IF_OUTPUT_POWER_OFFSET_AUTO

Specifies whether the measurement computes an IF output power level offset for the offset channels to improve the dynamic range of the ACP measurement. This attribute is used only if you set the [RFMXCDMA2K_ATTR_ACP_MEASUREMENT_METHOD](group____root__ni_r_fmx_c_d_m_a2k__attributes__acp_1gad6606efe7c2551cbda9cad17b3f53efc.html) attribute to **Dynamic Range**.

#### Syntax

RFMXCDMA2K_ATTR_ACP_IF_OUTPUT_POWER_OFFSET_AUTO

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6295604 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **True**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXCDMA2K_VAL_ACP_IF_OUTPUT_POWER_OFFSET_AUTO_FALSE | 0 (0x0) | The measurement does not compute an IF output power level offset for the offset channels. |
| RFMXCDMA2K_VAL_ACP_IF_OUTPUT_POWER_OFFSET_AUTO_TRUE | 1 (0x1) | The measurement computes an IF output power level offset for the offset channels. |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__acp__advanced_1gaa944a5f889e1f03e6745223dff12f3a7.html language=enus -->
## TOPIC 00009: RFMXCDMA2K_ATTR_ACP_SEQUENTIAL_FFT_SIZE

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__acp__advanced_1gaa944a5f889e1f03e6745223dff12f3a7.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__acp__advanced_1gaa944a5f889e1f03e6745223dff12f3a7.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the FFT size, when you set the RFMXCDMA2K_ATTR_ACP_MEASUREMENT_METHOD attribute to Sequential FFT. SyntaxRFMXCDMA2K_ATTR_ACP_SEQUENTIAL_FFT_SIZENumeric ValueData TypeAccessApplies To6295608int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribut

### RFMXCDMA2K_ATTR_ACP_SEQUENTIAL_FFT_SIZE

Specifies the FFT size, when you set the [RFMXCDMA2K_ATTR_ACP_MEASUREMENT_METHOD](group____root__ni_r_fmx_c_d_m_a2k__attributes__acp_1gad6606efe7c2551cbda9cad17b3f53efc.html) attribute to **Sequential FFT**.

#### Syntax

RFMXCDMA2K_ATTR_ACP_SEQUENTIAL_FFT_SIZE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6295608 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 512.

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__acp__averaging_1gad82d7bb8a0d0c0ea1b592546af4b7293.html language=enus -->
## TOPIC 00010: RFMXCDMA2K_ATTR_ACP_AVERAGING_TYPE

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__acp__averaging_1gad82d7bb8a0d0c0ea1b592546af4b7293.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__acp__averaging_1gad82d7bb8a0d0c0ea1b592546af4b7293.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for ACP measurement. SyntaxRFMXCDMA2K_ATTR_ACP_AVERAGING_TYPENumeric ValueData TypeAccessApplies To6295576int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read t

### RFMXCDMA2K_ATTR_ACP_AVERAGING_TYPE

Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for ACP measurement.

#### Syntax

RFMXCDMA2K_ATTR_ACP_AVERAGING_TYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6295576 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **RMS**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXCDMA2K_VAL_ACP_AVERAGING_TYPE_RMS | 0 (0x0) | The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. |
| RFMXCDMA2K_VAL_ACP_AVERAGING_TYPE_LOG | 1 (0x1) | The power spectrum is averaged in a logarithmic scale. |
| RFMXCDMA2K_VAL_ACP_AVERAGING_TYPE_SCALAR | 2 (0x2) | The square root of the power spectrum is averaged. |
| RFMXCDMA2K_VAL_ACP_AVERAGING_TYPE_MAXIMUM | 3 (0x3) | The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. |
| RFMXCDMA2K_VAL_ACP_AVERAGING_TYPE_MINIMUM | 4 (0x4) | The lowest power in the spectrum at each frequency bin is retained from one acquisition to the next. |

Parent topic:

Averaging

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__acp__fft_1ga1ecada4f1c0ea42cc524046bd31b9d39.html language=enus -->
## TOPIC 00011: RFMXCDMA2K_ATTR_ACP_FFT_OVERLAP

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__acp__fft_1ga1ecada4f1c0ea42cc524046bd31b9d39.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__acp__fft_1ga1ecada4f1c0ea42cc524046bd31b9d39.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the number of samples to overlap between consecutive chunks while performing FFT. SyntaxRFMXCDMA2K_ATTR_ACP_FFT_OVERLAPNumeric ValueData TypeAccessApplies To6295610float64Read-OnlyN/ARemarks This value is expressed as a percentage of RFMXCDMA2K_ATTR_ACP_SEQUENTIAL_FFT_SIZE attribute when you

### RFMXCDMA2K_ATTR_ACP_FFT_OVERLAP

Returns the number of samples to overlap between consecutive chunks while performing FFT.

#### Syntax

RFMXCDMA2K_ATTR_ACP_FFT_OVERLAP

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6295610 | float64 | Read-Only | N/A |

#### Remarks

This value is expressed as a percentage of [RFMXCDMA2K_ATTR_ACP_SEQUENTIAL_FFT_SIZE](group____root__ni_r_fmx_c_d_m_a2k__attributes__acp__advanced_1gaa944a5f889e1f03e6745223dff12f3a7.html) attribute when you set the [RFMXCDMA2K_ATTR_ACP_MEASUREMENT_METHOD](group____root__ni_r_fmx_c_d_m_a2k__attributes__acp_1gad6606efe7c2551cbda9cad17b3f53efc.html) attribute to **Sequential FFT**.

You do not need to use a selector string to read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

Parent topic:

FFT

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__acp__offset.html language=enus -->
## TOPIC 00012: Offset

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__acp__offset.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__acp__offset.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXCDMA2K_ATTR_ACP_NUMBER_OF_OFFSETSSpecifies the number of offset channels. RFMXCDMA2K_ATTR_ACP_OFFSET_FREQUENCYReturns the frequency of an ACP offset channel relative to the carrier frequency. This value is expressed in Hz. RFMXCDMA2K_ATTR_ACP_OFFSET_INTEGRAT

### Offset

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXCDMA2K_ATTR_ACP_NUMBER_OF_OFFSETS | Specifies the number of offset channels. |
| RFMXCDMA2K_ATTR_ACP_OFFSET_FREQUENCY | Returns the frequency of an ACP offset channel relative to the carrier frequency. This value is expressed in Hz. |
| RFMXCDMA2K_ATTR_ACP_OFFSET_INTEGRATION_BANDWIDTH | Returns the integration bandwidth of an ACP offset channel. This value is expressed in Hz. |

#### Attachments

None

Parent topic:

ACP

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__acp__offset_1ga69ec86c6793aca888ce7f88c7cccef03.html language=enus -->
## TOPIC 00013: RFMXCDMA2K_ATTR_ACP_OFFSET_FREQUENCY

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__acp__offset_1ga69ec86c6793aca888ce7f88c7cccef03.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__acp__offset_1ga69ec86c6793aca888ce7f88c7cccef03.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the frequency of an ACP offset channel relative to the carrier frequency. This value is expressed in Hz. SyntaxRFMXCDMA2K_ATTR_ACP_OFFSET_FREQUENCYNumeric ValueData TypeAccessApplies To6295562float64Read-OnlyOffsetRemarks Use "offset< <format type="monospace-italic">n</format> >" as the Sele

### RFMXCDMA2K_ATTR_ACP_OFFSET_FREQUENCY

Returns the frequency of an ACP offset channel relative to the carrier frequency. This value is expressed in Hz.

#### Syntax

RFMXCDMA2K_ATTR_ACP_OFFSET_FREQUENCY

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6295562 | float64 | Read-Only | Offset |

#### Remarks

Use "offset< 
<format type="monospace-italic">n</format> 
>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result.

Parent topic:

Offset

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__acp__offset_1ga924572f516d34352ed557b1818fc77fd.html language=enus -->
## TOPIC 00014: RFMXCDMA2K_ATTR_ACP_NUMBER_OF_OFFSETS

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__acp__offset_1ga924572f516d34352ed557b1818fc77fd.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__acp__offset_1ga924572f516d34352ed557b1818fc77fd.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of offset channels. SyntaxRFMXCDMA2K_ATTR_ACP_NUMBER_OF_OFFSETSNumeric ValueData TypeAccessApplies To6295560int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector String topic

### RFMXCDMA2K_ATTR_ACP_NUMBER_OF_OFFSETS

Specifies the number of offset channels.

#### Syntax

RFMXCDMA2K_ATTR_ACP_NUMBER_OF_OFFSETS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6295560 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 2.

Parent topic:

Offset

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__acp__offset_1gab39cc1148b15b135123657aeccab948c.html language=enus -->
## TOPIC 00015: RFMXCDMA2K_ATTR_ACP_OFFSET_INTEGRATION_BANDWIDTH

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__acp__offset_1gab39cc1148b15b135123657aeccab948c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__acp__offset_1gab39cc1148b15b135123657aeccab948c.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the integration bandwidth of an ACP offset channel. This value is expressed in Hz. SyntaxRFMXCDMA2K_ATTR_ACP_OFFSET_INTEGRATION_BANDWIDTHNumeric ValueData TypeAccessApplies To6295566float64Read-OnlyOffsetRemarks Use "offset< <format type="monospace-italic">n</format> >" as the Selector Strin

### RFMXCDMA2K_ATTR_ACP_OFFSET_INTEGRATION_BANDWIDTH

Returns the integration bandwidth of an ACP offset channel. This value is expressed in Hz.

#### Syntax

RFMXCDMA2K_ATTR_ACP_OFFSET_INTEGRATION_BANDWIDTH

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6295566 | float64 | Read-Only | Offset |

#### Remarks

Use "offset< 
<format type="monospace-italic">n</format> 
>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result.

Parent topic:

Offset

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__acp__rbw__filter.html language=enus -->
## TOPIC 00016: RBW Filter

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__acp__rbw__filter.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__acp__rbw__filter.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXCDMA2K_ATTR_ACP_RBW_FILTER_AUTO_BANDWIDTHSpecifies whether the measurement computes the RBW. RFMXCDMA2K_ATTR_ACP_RBW_FILTER_BANDWIDTHSpecifies the bandwidth of the RBW filter used to sweep the acquired signal when you set the RFMXCDMA2K_ATTR_ACP_RBW_FILTER_A

### RBW Filter

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXCDMA2K_ATTR_ACP_RBW_FILTER_AUTO_BANDWIDTH | Specifies whether the measurement computes the RBW. |
| RFMXCDMA2K_ATTR_ACP_RBW_FILTER_BANDWIDTH | Specifies the bandwidth of the RBW filter used to sweep the acquired signal when you set the RFMXCDMA2K_ATTR_ACP_RBW_FILTER_AUTO_BANDWIDTH attribute to False. This value is expressed in Hz. |
| RFMXCDMA2K_ATTR_ACP_RBW_FILTER_TYPE | Specifies the shape of the digital RBW filter. |

#### Attachments

None

Parent topic:

ACP

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__acp__rbw__filter_1ga4dab4e356ee7955f3b5dc826f9d0784d.html language=enus -->
## TOPIC 00017: RFMXCDMA2K_ATTR_ACP_RBW_FILTER_TYPE

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__acp__rbw__filter_1ga4dab4e356ee7955f3b5dc826f9d0784d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__acp__rbw__filter_1ga4dab4e356ee7955f3b5dc826f9d0784d.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the shape of the digital RBW filter. SyntaxRFMXCDMA2K_ATTR_ACP_RBW_FILTER_TYPENumeric ValueData TypeAccessApplies To6295581int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector String to

### RFMXCDMA2K_ATTR_ACP_RBW_FILTER_TYPE

Specifies the shape of the digital RBW filter.

#### Syntax

RFMXCDMA2K_ATTR_ACP_RBW_FILTER_TYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6295581 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **Gaussian**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXCDMA2K_VAL_ACP_RBW_FILTER_TYPE_FFT_BASED | 0 (0x0) | An RBW filter with an FFT-based response is applied. |
| RFMXCDMA2K_VAL_ACP_RBW_FILTER_TYPE_GAUSSIAN | 1 (0x1) | An RBW filter with a Gaussian response is applied. |
| RFMXCDMA2K_VAL_ACP_RBW_FILTER_TYPE_FLAT | 2 (0x2) | An RBW filter with a flat response is applied. |

Parent topic:

RBW Filter

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__acp__rbw__filter_1gadccaa22d1b6991fb4ae46f499a58fd21.html language=enus -->
## TOPIC 00018: RFMXCDMA2K_ATTR_ACP_RBW_FILTER_AUTO_BANDWIDTH

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__acp__rbw__filter_1gadccaa22d1b6991fb4ae46f499a58fd21.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__acp__rbw__filter_1gadccaa22d1b6991fb4ae46f499a58fd21.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement computes the RBW. SyntaxRFMXCDMA2K_ATTR_ACP_RBW_FILTER_AUTO_BANDWIDTHNumeric ValueData TypeAccessApplies To6295579int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Sel

### RFMXCDMA2K_ATTR_ACP_RBW_FILTER_AUTO_BANDWIDTH

Specifies whether the measurement computes the RBW.

#### Syntax

RFMXCDMA2K_ATTR_ACP_RBW_FILTER_AUTO_BANDWIDTH

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6295579 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **True**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXCDMA2K_VAL_ACP_RBW_AUTO_FALSE | 0 (0x0) | The measurement uses the RBW that you specify in the RFMXCDMA2K_ATTR_ACP_RBW_FILTER_BANDWIDTH attribute. |
| RFMXCDMA2K_VAL_ACP_RBW_AUTO_TRUE | 1 (0x1) | The measurement computes the RBW. |

Parent topic:

RBW Filter

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__acp__results__carrier.html language=enus -->
## TOPIC 00019: Carrier

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__acp__results__carrier.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__acp__results__carrier.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXCDMA2K_ATTR_ACP_RESULTS_CARRIER_ABSOLUTE_POWERReturns the absolute measured carrier power. This value is expressed in dBm. AttachmentsNone

### Carrier

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXCDMA2K_ATTR_ACP_RESULTS_CARRIER_ABSOLUTE_POWER | Returns the absolute measured carrier power. This value is expressed in dBm. |

#### Attachments

None

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__acp__results__carrier_1ga0114ab15e898672f7c1e14c8c29a78d2.html language=enus -->
## TOPIC 00020: RFMXCDMA2K_ATTR_ACP_RESULTS_CARRIER_ABSOLUTE_POWER

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__acp__results__carrier_1ga0114ab15e898672f7c1e14c8c29a78d2.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__acp__results__carrier_1ga0114ab15e898672f7c1e14c8c29a78d2.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the absolute measured carrier power. This value is expressed in dBm. SyntaxRFMXCDMA2K_ATTR_ACP_RESULTS_CARRIER_ABSOLUTE_POWERNumeric ValueData TypeAccessApplies To6295590float64Read-OnlyN/ARemarks You do not need to use a selector string to read this result for the default signal and result

### RFMXCDMA2K_ATTR_ACP_RESULTS_CARRIER_ABSOLUTE_POWER

Returns the absolute measured carrier power. This value is expressed in dBm.

#### Syntax

RFMXCDMA2K_ATTR_ACP_RESULTS_CARRIER_ABSOLUTE_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6295590 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and named results.

Parent topic:

Carrier

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__acp__results__lower__offset.html language=enus -->
## TOPIC 00021: Lower Offset

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__acp__results__lower__offset.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__acp__results__lower__offset.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXCDMA2K_ATTR_ACP_RESULTS_LOWER_OFFSET_ABSOLUTE_POWERReturns the absolute measured lower offset channel power. This value is expressed in dBm. RFMXCDMA2K_ATTR_ACP_RESULTS_LOWER_OFFSET_RELATIVE_POWERReturns the lower offset channel power measured relative to th

### Lower Offset

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXCDMA2K_ATTR_ACP_RESULTS_LOWER_OFFSET_ABSOLUTE_POWER | Returns the absolute measured lower offset channel power. This value is expressed in dBm. |
| RFMXCDMA2K_ATTR_ACP_RESULTS_LOWER_OFFSET_RELATIVE_POWER | Returns the lower offset channel power measured relative to the carrier absolute integrated power. This value is expressed in dB. |

#### Attachments

None

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__acp__results__lower__offset_1ga11f41c5644a9a7cebb4c5b08b832e120.html language=enus -->
## TOPIC 00022: RFMXCDMA2K_ATTR_ACP_RESULTS_LOWER_OFFSET_ABSOLUTE_POWER

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__acp__results__lower__offset_1ga11f41c5644a9a7cebb4c5b08b832e120.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__acp__results__lower__offset_1ga11f41c5644a9a7cebb4c5b08b832e120.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the absolute measured lower offset channel power. This value is expressed in dBm. SyntaxRFMXCDMA2K_ATTR_ACP_RESULTS_LOWER_OFFSET_ABSOLUTE_POWERNumeric ValueData TypeAccessApplies To6295596float64Read-OnlyOffsetRemarks Use "offset< <format type="monospace-italic">n</format> >" as the Selector

### RFMXCDMA2K_ATTR_ACP_RESULTS_LOWER_OFFSET_ABSOLUTE_POWER

Returns the absolute measured lower offset channel power. This value is expressed in dBm.

#### Syntax

RFMXCDMA2K_ATTR_ACP_RESULTS_LOWER_OFFSET_ABSOLUTE_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6295596 | float64 | Read-Only | Offset |

#### Remarks

Use "offset< 
<format type="monospace-italic">n</format> 
>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result.

Parent topic:

Lower Offset

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__acp__results__upper__offset.html language=enus -->
## TOPIC 00023: Upper Offset

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__acp__results__upper__offset.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__acp__results__upper__offset.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXCDMA2K_ATTR_ACP_RESULTS_UPPER_OFFSET_ABSOLUTE_POWERReturns the absolute measured upper offset channel power. This value is expressed in dBm. RFMXCDMA2K_ATTR_ACP_RESULTS_UPPER_OFFSET_RELATIVE_POWERReturns the upper offset channel power measured relative to th

### Upper Offset

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXCDMA2K_ATTR_ACP_RESULTS_UPPER_OFFSET_ABSOLUTE_POWER | Returns the absolute measured upper offset channel power. This value is expressed in dBm. |
| RFMXCDMA2K_ATTR_ACP_RESULTS_UPPER_OFFSET_RELATIVE_POWER | Returns the upper offset channel power measured relative to the carrier absolute integrated power. This value is expressed in dB. |

#### Attachments

None

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__acp__results__upper__offset_1gae381711f3eb57bc174c910c9b85f5670.html language=enus -->
## TOPIC 00024: RFMXCDMA2K_ATTR_ACP_RESULTS_UPPER_OFFSET_RELATIVE_POWER

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__acp__results__upper__offset_1gae381711f3eb57bc174c910c9b85f5670.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__acp__results__upper__offset_1gae381711f3eb57bc174c910c9b85f5670.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the upper offset channel power measured relative to the carrier absolute integrated power. This value is expressed in dB. SyntaxRFMXCDMA2K_ATTR_ACP_RESULTS_UPPER_OFFSET_RELATIVE_POWERNumeric ValueData TypeAccessApplies To6295603float64Read-OnlyOffsetRemarks Use "offset< <format type="monospa

### RFMXCDMA2K_ATTR_ACP_RESULTS_UPPER_OFFSET_RELATIVE_POWER

Returns the upper offset channel power measured relative to the carrier absolute integrated power. This value is expressed in dB.

#### Syntax

RFMXCDMA2K_ATTR_ACP_RESULTS_UPPER_OFFSET_RELATIVE_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6295603 | float64 | Read-Only | Offset |

#### Remarks

Use "offset< 
<format type="monospace-italic">n</format> 
>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result.

Parent topic:

Upper Offset

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__acp__sweep__time_1ga97ce318c8205895bc4f2e2bc2336a2aa.html language=enus -->
## TOPIC 00025: RFMXCDMA2K_ATTR_ACP_SWEEP_TIME_INTERVAL

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__acp__sweep__time_1ga97ce318c8205895bc4f2e2bc2336a2aa.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__acp__sweep__time_1ga97ce318c8205895bc4f2e2bc2336a2aa.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the sweep time when you set the RFMXCDMA2K_ATTR_ACP_SWEEP_TIME_AUTO attribute to False. This value is expressed in seconds. SyntaxRFMXCDMA2K_ATTR_ACP_SWEEP_TIME_INTERVALNumeric ValueData TypeAccessApplies To6295583float64Read/WriteN/ARemarks You do not need to use a selector string to conf

### RFMXCDMA2K_ATTR_ACP_SWEEP_TIME_INTERVAL

Specifies the sweep time when you set the [RFMXCDMA2K_ATTR_ACP_SWEEP_TIME_AUTO](group____root__ni_r_fmx_c_d_m_a2k__attributes__acp__sweep__time_1gaf9c55f80f8811f9e5fc67a5fc5e66d5c.html) attribute to **False**. This value is expressed in seconds.

#### Syntax

RFMXCDMA2K_ATTR_ACP_SWEEP_TIME_INTERVAL

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6295583 | float64 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 0.0016667 seconds.

Parent topic:

Sweep Time

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__advanced.html language=enus -->
## TOPIC 00026: Advanced

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__advanced.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__advanced.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXCDMA2K_ATTR_AUTO_LEVEL_INITIAL_REFERENCE_LEVELSpecifies the initial reference level that the RFmxCDMA2k Auto Level function uses to estimate the peak power of the input signal. This value is expressed in dBm. RFMXCDMA2K_ATTR_LIMITED_CONFIGURATION_CHANGESpeci

### Advanced

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXCDMA2K_ATTR_AUTO_LEVEL_INITIAL_REFERENCE_LEVEL | Specifies the initial reference level that the RFmxCDMA2k Auto Level function uses to estimate the peak power of the input signal. This value is expressed in dBm. |
| RFMXCDMA2K_ATTR_LIMITED_CONFIGURATION_CHANGE | Specifies the set of attributes that are considered by RFmx in the locked signal configuration state. |

#### Attachments

None

Parent topic:

Attributes

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__advanced_1ga00a6493004675ee05bbe391f976827a8.html language=enus -->
## TOPIC 00027: RFMXCDMA2K_ATTR_LIMITED_CONFIGURATION_CHANGE

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__advanced_1ga00a6493004675ee05bbe391f976827a8.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__advanced_1ga00a6493004675ee05bbe391f976827a8.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the set of attributes that are considered by RFmx in the locked signal configuration state. SyntaxRFMXCDMA2K_ATTR_LIMITED_CONFIGURATION_CHANGENumeric ValueData TypeAccessApplies To6344707int32Read/WriteN/ARemarks If your test system performs the same measurement at different selected ports

### RFMXCDMA2K_ATTR_LIMITED_CONFIGURATION_CHANGE

Specifies the set of attributes that are considered by RFmx in the locked signal configuration state.

#### Syntax

RFMXCDMA2K_ATTR_LIMITED_CONFIGURATION_CHANGE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6344707 | int32 | Read/Write | N/A |

#### Remarks

If your test system performs the same measurement at different selected ports, multiple frequencies and/or power levels repeatedly, enabling this attribute can help achieve faster measurements. When you set this attribute to a value other than **Disabled**, the RFmx driver will use an optimized code path and skip some checks. Because RFmx skips some checks when you use this attribute, you need to be aware of the limitations of this feature, which are listed in the [Limitations of the Limited Configuration Change Property](https://www.ni.com/docs/en-US/bundle/rfmx-wcdma-prop/page/rfmxwcdmaprop/limitations.html) topic.

You can also use this attribute to lock a specific instrument configuration for a signal so that every time that you initiate the signal, RFmx applies the RFmxInstr attributes from a locked configuration.

NI recommends you use this attribute in conjunction with named signal configurations. Create named signal configurations for each measurement configuration in your test program and set this attribute to a value other than **Disabled** for one or more of the named signal configurations. This allows RFmx to precompute the acquisition settings for your measurement configurations and re-use the precomputed settings each time you initiate the measurement. You do not need to use this attribute if you create named signals for all the measurement configurations in your test program during test sequence initialization and do not change any RFInstr or personality attributes while testing each device under test. RFmx automatically optimizes that use case.

Specify the named signal configuration you are setting this attribute in the selector string input. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default value is **Disabled**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXCDMA2K_VAL_LIMITED_CONFIGURATION_CHANGE_DISABLED | 0 (0x0) | This is the normal mode of RFmx operation. All configuration changes in RFmxInstr attributes or in personality attributes will be applied during RFmx Commit. |
| RFMXCDMA2K_VAL_LIMITED_CONFIGURATION_CHANGE_NO_CHANGE | 1 (0x1) | Signal configuration is locked after the first Commit of the named signal configuration. Any configuration change thereafter either in RFmxInstr attributes or personality attributes will not be considered by subsequent RFmx Commits or Initiates of this signal. Use No Change if you have created named signal configurations for all measurement configurations but are setting some RFmxInstr attributes. Refer to the Limitations of the Limited Configuration Change Property topic for more details about the limitations of using this mode. |
| RFMXCDMA2K_VAL_LIMITED_CONFIGURATION_CHANGE_FREQUENCY | 2 (0x2) | Signal configuration, other than center frequency and external attenuation, is locked after first Commit of the named signal configuration. Thereafter, only the RFMXCDMA2K_ATTR_CENTER_FREQUENCY and RFMXCDMA2K_ATTR_EXTERNAL_ATTENUATION attribute value changes will be considered by subsequent driver Commits or Initiates of this signal. Refer to the Limitations of the Limited Configuration Change Property topic for more details about the limitations of using this mode. |
| RFMXCDMA2K_VAL_LIMITED_CONFIGURATION_CHANGE_REFERENCE_LEVEL | 3 (0x3) | Signal configuration, other than the reference level, is locked after first Commit of the named signal configuration. Thereafter only the RFMXCDMA2K_ATTR_REFERENCE_LEVEL attribute value change will be considered by subsequent driver Commits or Initiates of this signal. If you have configured this signal to use an IQ Power Edge Trigger, NI recommends that you set the RFMXCDMA2K_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE to Relative so that the trigger level is automatically adjusted as you adjust the reference level. Refer to the Limitations of the Limited Configuration Change Property topic for more details about the limitations of using this mode. |
| RFMXCDMA2K_VAL_LIMITED_CONFIGURATION_CHANGE_FREQUENCY_AND_REFERENCE_LEVEL | 4 (0x4) | Signal configuration, other than center frequency, reference level, and external attenuation, is locked after first Commit of the named signal configuration. Thereafter only Center Frequency, Reference Level, and External Attenuation attribute value changes will be considered by subsequent driver Commits or Initiates of this signal. If you have configured this signal to use an IQ Power Edge Trigger, NI recommends you set the IQ Power Edge Level Type to Relative so that the trigger level is automatically adjusted as you adjust the reference level. Refer to the Limitations of the Limited Configuration Change Property topic for more details about the limitations of using this mode. |
| RFMXCDMA2K_VAL_LIMITED_CONFIGURATION_CHANGE_SELECTED_PORTS_FREQUENCY_AND_REFERENCE_LEVEL | 5 (0x5) | Signal configuration, other than selected ports, center frequency, reference level, external attenuation, and RFInstr configuration, is locked after first Commit or Initiate of the named signal configuration. Thereafter only Selected Ports, Center Frequency, Reference Level, and External Attenuation attribute value changes will be considered by subsequent driver Commits or Initiates of this signal. If you have configured this signal to use an IQ Power Edge Trigger, NI recommends you set the IQ Power Edge Level Type to Relative so that the trigger level is automatically adjusted as you adjust the reference level. Refer to the Limitations of the Limited Configuration Change Property topic for more details about the limitations of using this mode. |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__advanced_1gaf9047215e61aa886ad8bd07021049d44.html language=enus -->
## TOPIC 00028: RFMXCDMA2K_ATTR_AUTO_LEVEL_INITIAL_REFERENCE_LEVEL

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__advanced_1gaf9047215e61aa886ad8bd07021049d44.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__advanced_1gaf9047215e61aa886ad8bd07021049d44.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the initial reference level that the RFmxCDMA2k Auto Level function uses to estimate the peak power of the input signal. This value is expressed in dBm. SyntaxRFMXCDMA2K_ATTR_AUTO_LEVEL_INITIAL_REFERENCE_LEVELNumeric ValueData TypeAccessApplies To6344704float64Read/WriteN/ARemarks The defa

### RFMXCDMA2K_ATTR_AUTO_LEVEL_INITIAL_REFERENCE_LEVEL

Specifies the initial reference level that the [RFmxCDMA2k Auto Level](/csh?context=rfmxcdma2k_rfmxcdma2kcref_function_auto_level) function uses to estimate the peak power of the input signal. This value is expressed in dBm.

#### Syntax

RFMXCDMA2K_ATTR_AUTO_LEVEL_INITIAL_REFERENCE_LEVEL

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6344704 | float64 | Read/Write | N/A |

#### Remarks

The default value is 30 dBm.

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__cda.html language=enus -->
## TOPIC 00029: CDA

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__cda.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__cda.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsMeasurement ChannelResultsGroup membersNameDescriptionRFMXCDMA2K_ATTR_CDA_ALL_TRACES_ENABLEDSpecifies whether to enable the traces to be stored and retrieved after performing the code domain analysis (CDA). RFMXCDMA2K_ATTR_CDA_BASE_SPREADING_FACTORSpecifies the base spreading factor used to ca

### CDA

#### Groups

- Measurement Channel
- Results

#### Group members

| Name | Description |
| --- | --- |
| RFMXCDMA2K_ATTR_CDA_ALL_TRACES_ENABLED | Specifies whether to enable the traces to be stored and retrieved after performing the code domain analysis (CDA). |
| RFMXCDMA2K_ATTR_CDA_BASE_SPREADING_FACTOR | Specifies the base spreading factor used to calculate the code domain power traces. |
| RFMXCDMA2K_ATTR_CDA_IQ_GAIN_IMBALANCE_REMOVAL_ENABLED | Specifies whether to remove the I/Q gain imbalance before the code domain analysis (CDA) measurement. |
| RFMXCDMA2K_ATTR_CDA_IQ_OFFSET_REMOVAL_ENABLED | Specifies whether to remove I/Q offset before the code domain analysis (CDA) measurement. |
| RFMXCDMA2K_ATTR_CDA_IQ_QUADRATURE_ERROR_REMOVAL_ENABLED | Specifies whether to remove the I/Q quadrature error before the code domain analysis (CDA) measurement. |
| RFMXCDMA2K_ATTR_CDA_MEASUREMENT_ENABLED | Specifies whether to enable the code domain analysis (CDA) measurement. |
| RFMXCDMA2K_ATTR_CDA_MEASUREMENT_LENGTH | Specifies the duration of code domain measurement. This value is expressed in slots. |
| RFMXCDMA2K_ATTR_CDA_MEASUREMENT_OFFSET | Specifies the measurement offset to skip from the synchronization boundary. The synchronization boundary is specified by the RFMXCDMA2K_ATTR_CDA_SYNCHRONIZATION_MODE attribute. This value is expressed in slots. |
| RFMXCDMA2K_ATTR_CDA_POWER_UNIT | Specifies the measurement unit of the measured code domain power results. |
| RFMXCDMA2K_ATTR_CDA_RECEIVE_FILTER_ENABLED | Specifies whether to enable the received filter for the code domain analysis (CDA) measurement. Use this attribute to disable the filter, if the received signal is already filtered. |
| RFMXCDMA2K_ATTR_CDA_SPECTRUM_INVERTED | Specifies whether the spectrum of the signal is inverted. |
| RFMXCDMA2K_ATTR_CDA_SYNCHRONIZATION_MODE | Specifies whether the measurement is performed from the frame, slot, or symbol boundary. |

#### Attachments

None

Parent topic:

Attributes

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__cda_1ga6a25a5e8184b27ae1031ea67431bbf75.html language=enus -->
## TOPIC 00030: RFMXCDMA2K_ATTR_CDA_IQ_GAIN_IMBALANCE_REMOVAL_ENABLED

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__cda_1ga6a25a5e8184b27ae1031ea67431bbf75.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__cda_1ga6a25a5e8184b27ae1031ea67431bbf75.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to remove the I/Q gain imbalance before the code domain analysis (CDA) measurement. SyntaxRFMXCDMA2K_ATTR_CDA_IQ_GAIN_IMBALANCE_REMOVAL_ENABLEDNumeric ValueData TypeAccessApplies To6369292int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this a

### RFMXCDMA2K_ATTR_CDA_IQ_GAIN_IMBALANCE_REMOVAL_ENABLED

Specifies whether to remove the I/Q gain imbalance before the code domain analysis (CDA) measurement.

#### Syntax

RFMXCDMA2K_ATTR_CDA_IQ_GAIN_IMBALANCE_REMOVAL_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6369292 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **False**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXCDMA2K_VAL_CDA_IQ_GAIN_IMBALANCE_REMOVAL_ENABLED_FALSE | 0 (0x0) | I/Q gain imbalance is not removed before the CDA measurement. |
| RFMXCDMA2K_VAL_CDA_IQ_GAIN_IMBALANCE_REMOVAL_ENABLED_TRUE | 1 (0x1) | I/Q gain imbalance is removed before the CDA measurement. |

Parent topic:

CDA

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__cda_1gade3a391bd31088871a4398a80d4e43ad.html language=enus -->
## TOPIC 00031: RFMXCDMA2K_ATTR_CDA_IQ_QUADRATURE_ERROR_REMOVAL_ENABLED

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__cda_1gade3a391bd31088871a4398a80d4e43ad.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__cda_1gade3a391bd31088871a4398a80d4e43ad.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to remove the I/Q quadrature error before the code domain analysis (CDA) measurement. SyntaxRFMXCDMA2K_ATTR_CDA_IQ_QUADRATURE_ERROR_REMOVAL_ENABLEDNumeric ValueData TypeAccessApplies To6369293int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read th

### RFMXCDMA2K_ATTR_CDA_IQ_QUADRATURE_ERROR_REMOVAL_ENABLED

Specifies whether to remove the I/Q quadrature error before the code domain analysis (CDA) measurement.

#### Syntax

RFMXCDMA2K_ATTR_CDA_IQ_QUADRATURE_ERROR_REMOVAL_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6369293 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **False**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXCDMA2K_VAL_CDA_IQ_QUADRATURE_ERROR_REMOVAL_ENABLED_FALSE | 0 (0x0) | I/Q quadrature error is not removed before the CDA measurement. |
| RFMXCDMA2K_VAL_CDA_IQ_QUADRATURE_ERROR_REMOVAL_ENABLED_TRUE | 1 (0x1) | I/Q quadrature error is removed before the CDA measurement. |

Parent topic:

CDA

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__cda_1gae2656380c8cee750c120a9ffdc88f539.html language=enus -->
## TOPIC 00032: RFMXCDMA2K_ATTR_CDA_BASE_SPREADING_FACTOR

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__cda_1gae2656380c8cee750c120a9ffdc88f539.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__cda_1gae2656380c8cee750c120a9ffdc88f539.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the base spreading factor used to calculate the code domain power traces. SyntaxRFMXCDMA2K_ATTR_CDA_BASE_SPREADING_FACTORNumeric ValueData TypeAccessApplies To6369285int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signa

### RFMXCDMA2K_ATTR_CDA_BASE_SPREADING_FACTOR

Specifies the base spreading factor used to calculate the code domain power traces.

#### Syntax

RFMXCDMA2K_ATTR_CDA_BASE_SPREADING_FACTOR

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6369285 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 64. The valid values are 2, 4, 8, 16, 32, and 64.

Parent topic:

CDA

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__cda__measurement__channel.html language=enus -->
## TOPIC 00033: Measurement Channel

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__cda__measurement__channel.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__cda__measurement__channel.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXCDMA2K_ATTR_CDA_MEASUREMENT_CHANNEL_BRANCHSpecifies the branch of a channel subject to channel specific analysis. RFMXCDMA2K_ATTR_CDA_MEASUREMENT_CHANNEL_WALSH_CODE_LENGTHSpecifies the Walsh code length of a channel subject to channel specific analysis. RFMX

### Measurement Channel

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXCDMA2K_ATTR_CDA_MEASUREMENT_CHANNEL_BRANCH | Specifies the branch of a channel subject to channel specific analysis. |
| RFMXCDMA2K_ATTR_CDA_MEASUREMENT_CHANNEL_WALSH_CODE_LENGTH | Specifies the Walsh code length of a channel subject to channel specific analysis. |
| RFMXCDMA2K_ATTR_CDA_MEASUREMENT_CHANNEL_WALSH_CODE_NUMBER | Specifies the Walsh code number of a channel subject to channel specific analysis. |

#### Attachments

None

Parent topic:

CDA

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__cda__measurement__channel_1gaa6b5636bcbab259c12ca359463da0a93.html language=enus -->
## TOPIC 00034: RFMXCDMA2K_ATTR_CDA_MEASUREMENT_CHANNEL_BRANCH

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__cda__measurement__channel_1gaa6b5636bcbab259c12ca359463da0a93.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__cda__measurement__channel_1gaa6b5636bcbab259c12ca359463da0a93.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the branch of a channel subject to channel specific analysis. SyntaxRFMXCDMA2K_ATTR_CDA_MEASUREMENT_CHANNEL_BRANCHNumeric ValueData TypeAccessApplies To6369288int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal insta

### RFMXCDMA2K_ATTR_CDA_MEASUREMENT_CHANNEL_BRANCH

Specifies the branch of a channel subject to channel specific analysis.

#### Syntax

RFMXCDMA2K_ATTR_CDA_MEASUREMENT_CHANNEL_BRANCH

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6369288 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **I**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXCDMA2K_VAL_CDA_MEASUREMENT_CHANNEL_BRANCH_I | 0 (0x0) | Specifies the in-phase branch. |
| RFMXCDMA2K_VAL_CDA_MEASUREMENT_CHANNEL_BRANCH_Q | 1 (0x1) | Specifies the quadrature branch. |

Parent topic:

Measurement Channel

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__cda__results.html language=enus -->
## TOPIC 00035: Results

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__cda__results.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__cda__results.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXCDMA2K_ATTR_CDA_RESULTS_CHIP_RATE_ERRORReturns the chip rate error. This value is expressed in parts per million (ppm). RFMXCDMA2K_ATTR_CDA_RESULTS_FREQUENCY_ERRORReturns the frequency error. This value is expressed in Hz. RFMXCDMA2K_ATTR_CDA_RESULTS_IQ_GAIN

### Results

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXCDMA2K_ATTR_CDA_RESULTS_CHIP_RATE_ERROR | Returns the chip rate error. This value is expressed in parts per million (ppm). |
| RFMXCDMA2K_ATTR_CDA_RESULTS_FREQUENCY_ERROR | Returns the frequency error. This value is expressed in Hz. |
| RFMXCDMA2K_ATTR_CDA_RESULTS_IQ_GAIN_IMBALANCE | Returns the I/Q gain imbalance of the composite signal averaged over all measured slots. This value is expressed in dB. |
| RFMXCDMA2K_ATTR_CDA_RESULTS_IQ_ORIGIN_OFFSET | Returns the I/Q origin offset of the composite signal averaged over all measured slots. This value is expressed in dB. |
| RFMXCDMA2K_ATTR_CDA_RESULTS_IQ_QUADRATURE_ERROR | Returns the I/Q quadrature error of the composite signal averaged over all measured slots. This value is expressed in degrees. |
| RFMXCDMA2K_ATTR_CDA_RESULTS_I_MEAN_ACTIVE_POWER | Returns the average power of all active code channels measured on the I-branch. If you set the RFMXCDMA2K_ATTR_CDA_POWER_UNIT attribute to dBm, this measurement returns the absolute measured power; otherwise, this measurement returns a value relative to the RFMXCDMA2K_ATTR_CDA_RESULTS_TOTAL_POWER attribute. |
| RFMXCDMA2K_ATTR_CDA_RESULTS_I_PEAK_INACTIVE_POWER | Returns the maximum measured code power among the set of inactive channels on the I-branch and in the code domain of the base spreading factor. If you set the RFMXCDMA2K_ATTR_CDA_POWER_UNIT attribute to dBm, this measurement returns the absolute measured power; otherwise, this measurement returns a value relative to the RFMXCDMA2K_ATTR_CDA_RESULTS_TOTAL_POWER attribute. |
| RFMXCDMA2K_ATTR_CDA_RESULTS_MEAN_ACTIVE_POWER | Returns the average power of all active code channels. If you set the RFMXCDMA2K_ATTR_CDA_POWER_UNIT attribute to dBm, this measurement returns the absolute measured power; otherwise, this measurement returns a value relative to the RFMXCDMA2K_ATTR_CDA_RESULTS_TOTAL_POWER attribute. |
| RFMXCDMA2K_ATTR_CDA_RESULTS_MEAN_INACTIVE_POWER | Returns the average code power, measured among the set of inactive channels, in the code domain of the base spreading factor. If you set the RFMXCDMA2K_ATTR_CDA_POWER_UNIT attribute to dBm, this measurement returns the absolute measured power; otherwise, this measurement returns a value relative to the RFMXCDMA2K_ATTR_CDA_RESULTS_TOTAL_POWER attribute. |
| RFMXCDMA2K_ATTR_CDA_RESULTS_MEAN_PILOT_POWER | Returns the mean power of the R-PICH. |
| RFMXCDMA2K_ATTR_CDA_RESULTS_MEAN_SYMBOL_POWER | Returns the mean symbol power of the configured measurement channel. This value is expressed in dB, when you set the RFMXCDMA2K_ATTR_CDA_POWER_UNIT attribute to dB, and in dBm, when you set the CDA Pwr Unit attribute to dBm. |
| RFMXCDMA2K_ATTR_CDA_RESULTS_PEAK_ACTIVE_POWER | Returns the maximum power among all active code channels. If you set the RFMXCDMA2K_ATTR_CDA_POWER_UNIT attribute to dBm, this measurement returns the absolute measured power; otherwise, this measurement returns a value relative to the RFMXCDMA2K_ATTR_CDA_RESULTS_TOTAL_POWER attribute. |
| RFMXCDMA2K_ATTR_CDA_RESULTS_PEAK_INACTIVE_POWER | Returns the maximum measured code power, measured among the set of inactive channels, in the code domain of the base spreading factor. If you set the RFMXCDMA2K_ATTR_CDA_POWER_UNIT attribute to dBm, this measurement returns the absolute measured power; otherwise, this measurement returns a value relative to the RFMXCDMA2K_ATTR_CDA_RESULTS_TOTAL_POWER attribute. |
| RFMXCDMA2K_ATTR_CDA_RESULTS_PEAK_SYMBOL_EVM | Returns the peak symbol EVM of the configured measurement channel. This value is expressed as a percentage. |
| RFMXCDMA2K_ATTR_CDA_RESULTS_Q_MEAN_ACTIVE_POWER | Returns the average power of all active code channels measured on the Q-branch. If you set the RFMXCDMA2K_ATTR_CDA_POWER_UNIT attribute to dBm, this measurement returns the absolute measured power; otherwise, this measurement returns a value relative to the RFMXCDMA2K_ATTR_CDA_RESULTS_TOTAL_POWER attribute. |
| RFMXCDMA2K_ATTR_CDA_RESULTS_Q_PEAK_INACTIVE_POWER | Returns the maximum measured code power among the set of inactive channels on the Q-branch and in the code domain of the base spreading factor. If you set the RFMXCDMA2K_ATTR_CDA_POWER_UNIT attribute to dBm, this measurement returns the absolute measured power; otherwise, this measurement returns a value relative to the RFMXCDMA2K_ATTR_CDA_RESULTS_TOTAL_POWER attribute. |
| RFMXCDMA2K_ATTR_CDA_RESULTS_RMS_SYMBOL_EVM | Returns the RMS symbol EVM of the configured measurement channel. This value is expressed as a percentage. |
| RFMXCDMA2K_ATTR_CDA_RESULTS_RMS_SYMBOL_MAGNITUDE_ERROR | Returns the RMS symbol magnitude error of the configured measurement channel. This value is expressed as a percentage. |
| RFMXCDMA2K_ATTR_CDA_RESULTS_RMS_SYMBOL_PHASE_ERROR | Returns the RMS symbol phase error of the configured measurement channel. This value is expressed in degrees. |
| RFMXCDMA2K_ATTR_CDA_RESULTS_TOTAL_ACTIVE_POWER | Returns the sum of the powers of all active code channels. If you set the RFMXCDMA2K_ATTR_CDA_POWER_UNIT attribute to dBm, this measurement returns the absolute measured power; otherwise, this measurement returns a value relative to the RFMXCDMA2K_ATTR_CDA_RESULTS_TOTAL_POWER attribute. |
| RFMXCDMA2K_ATTR_CDA_RESULTS_TOTAL_POWER | Returns the mean power of the received signal. This value is expressed in dBm. |

#### Attachments

None

Parent topic:

CDA

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__cda__results_1ga02f78c187cac3f60e8ddd27e4dfbd49b.html language=enus -->
## TOPIC 00036: RFMXCDMA2K_ATTR_CDA_RESULTS_TOTAL_ACTIVE_POWER

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__cda__results_1ga02f78c187cac3f60e8ddd27e4dfbd49b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__cda__results_1ga02f78c187cac3f60e8ddd27e4dfbd49b.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the sum of the powers of all active code channels. If you set the RFMXCDMA2K_ATTR_CDA_POWER_UNIT attribute to dBm, this measurement returns the absolute measured power; otherwise, this measurement returns a value relative to the RFMXCDMA2K_ATTR_CDA_RESULTS_TOTAL_POWER attribute. SyntaxRFMXCD

### RFMXCDMA2K_ATTR_CDA_RESULTS_TOTAL_ACTIVE_POWER

Returns the sum of the powers of all active code channels. If you set the [RFMXCDMA2K_ATTR_CDA_POWER_UNIT](group____root__ni_r_fmx_c_d_m_a2k__attributes__cda_1ga19478b846aca6fda9fa5966c6b20f4af.html) attribute to **dBm**, this measurement returns the absolute measured power; otherwise, this measurement returns a value relative to the [RFMXCDMA2K_ATTR_CDA_RESULTS_TOTAL_POWER](group____root__ni_r_fmx_c_d_m_a2k__attributes__cda__results_1ga4caee61e88c05bffe087004448b5a4a9.html) attribute.

#### Syntax

RFMXCDMA2K_ATTR_CDA_RESULTS_TOTAL_ACTIVE_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6369304 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and named results.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__cda__results_1ga0c8605e5fc49718462febeb842d2d034.html language=enus -->
## TOPIC 00037: RFMXCDMA2K_ATTR_CDA_RESULTS_I_MEAN_ACTIVE_POWER

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__cda__results_1ga0c8605e5fc49718462febeb842d2d034.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__cda__results_1ga0c8605e5fc49718462febeb842d2d034.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the average power of all active code channels measured on the I-branch. If you set the RFMXCDMA2K_ATTR_CDA_POWER_UNIT attribute to dBm, this measurement returns the absolute measured power; otherwise, this measurement returns a value relative to the RFMXCDMA2K_ATTR_CDA_RESULTS_TOTAL_POWER at

### RFMXCDMA2K_ATTR_CDA_RESULTS_I_MEAN_ACTIVE_POWER

Returns the average power of all active code channels measured on the I-branch. If you set the [RFMXCDMA2K_ATTR_CDA_POWER_UNIT](group____root__ni_r_fmx_c_d_m_a2k__attributes__cda_1ga19478b846aca6fda9fa5966c6b20f4af.html) attribute to **dBm**, this measurement returns the absolute measured power; otherwise, this measurement returns a value relative to the [RFMXCDMA2K_ATTR_CDA_RESULTS_TOTAL_POWER](group____root__ni_r_fmx_c_d_m_a2k__attributes__cda__results_1ga4caee61e88c05bffe087004448b5a4a9.html) attribute.

#### Syntax

RFMXCDMA2K_ATTR_CDA_RESULTS_I_MEAN_ACTIVE_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6369309 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and named results.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__cda__results_1ga193e38ddfe03b6ffcc257b43767e1ac6.html language=enus -->
## TOPIC 00038: RFMXCDMA2K_ATTR_CDA_RESULTS_I_PEAK_INACTIVE_POWER

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__cda__results_1ga193e38ddfe03b6ffcc257b43767e1ac6.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__cda__results_1ga193e38ddfe03b6ffcc257b43767e1ac6.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum measured code power among the set of inactive channels on the I-branch and in the code domain of the base spreading factor. If you set the RFMXCDMA2K_ATTR_CDA_POWER_UNIT attribute to dBm, this measurement returns the absolute measured power; otherwise, this measurement returns a

### RFMXCDMA2K_ATTR_CDA_RESULTS_I_PEAK_INACTIVE_POWER

Returns the maximum measured code power among the set of inactive channels on the I-branch and in the code domain of the base spreading factor. If you set the [RFMXCDMA2K_ATTR_CDA_POWER_UNIT](group____root__ni_r_fmx_c_d_m_a2k__attributes__cda_1ga19478b846aca6fda9fa5966c6b20f4af.html) attribute to **dBm**, this measurement returns the absolute measured power; otherwise, this measurement returns a value relative to the [RFMXCDMA2K_ATTR_CDA_RESULTS_TOTAL_POWER](group____root__ni_r_fmx_c_d_m_a2k__attributes__cda__results_1ga4caee61e88c05bffe087004448b5a4a9.html) attribute.

#### Syntax

RFMXCDMA2K_ATTR_CDA_RESULTS_I_PEAK_INACTIVE_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6369310 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and named results.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__cda__results_1ga3d27d841027d7ffe8a9dc5290f252986.html language=enus -->
## TOPIC 00039: RFMXCDMA2K_ATTR_CDA_RESULTS_Q_PEAK_INACTIVE_POWER

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__cda__results_1ga3d27d841027d7ffe8a9dc5290f252986.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__cda__results_1ga3d27d841027d7ffe8a9dc5290f252986.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum measured code power among the set of inactive channels on the Q-branch and in the code domain of the base spreading factor. If you set the RFMXCDMA2K_ATTR_CDA_POWER_UNIT attribute to dBm, this measurement returns the absolute measured power; otherwise, this measurement returns a

### RFMXCDMA2K_ATTR_CDA_RESULTS_Q_PEAK_INACTIVE_POWER

Returns the maximum measured code power among the set of inactive channels on the Q-branch and in the code domain of the base spreading factor. If you set the [RFMXCDMA2K_ATTR_CDA_POWER_UNIT](group____root__ni_r_fmx_c_d_m_a2k__attributes__cda_1ga19478b846aca6fda9fa5966c6b20f4af.html) attribute to **dBm**, this measurement returns the absolute measured power; otherwise, this measurement returns a value relative to the [RFMXCDMA2K_ATTR_CDA_RESULTS_TOTAL_POWER](group____root__ni_r_fmx_c_d_m_a2k__attributes__cda__results_1ga4caee61e88c05bffe087004448b5a4a9.html) attribute.

#### Syntax

RFMXCDMA2K_ATTR_CDA_RESULTS_Q_PEAK_INACTIVE_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6369312 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and named results.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__cda__results_1ga4caee61e88c05bffe087004448b5a4a9.html language=enus -->
## TOPIC 00040: RFMXCDMA2K_ATTR_CDA_RESULTS_TOTAL_POWER

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__cda__results_1ga4caee61e88c05bffe087004448b5a4a9.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__cda__results_1ga4caee61e88c05bffe087004448b5a4a9.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean power of the received signal. This value is expressed in dBm. SyntaxRFMXCDMA2K_ATTR_CDA_RESULTS_TOTAL_POWERNumeric ValueData TypeAccessApplies To6369303float64Read-OnlyN/ARemarks You do not need to use a selector string to read this result for the default signal and result instance.

### RFMXCDMA2K_ATTR_CDA_RESULTS_TOTAL_POWER

Returns the mean power of the received signal. This value is expressed in dBm.

#### Syntax

RFMXCDMA2K_ATTR_CDA_RESULTS_TOTAL_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6369303 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and named results.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__cda__results_1ga58063938321b41338a903017d84a8260.html language=enus -->
## TOPIC 00041: RFMXCDMA2K_ATTR_CDA_RESULTS_PEAK_SYMBOL_EVM

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__cda__results_1ga58063938321b41338a903017d84a8260.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__cda__results_1ga58063938321b41338a903017d84a8260.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the peak symbol EVM of the configured measurement channel. This value is expressed as a percentage. SyntaxRFMXCDMA2K_ATTR_CDA_RESULTS_PEAK_SYMBOL_EVMNumeric ValueData TypeAccessApplies To6369299float64Read-OnlyN/ARemarks You do not need to use a selector string to read this result for the de

### RFMXCDMA2K_ATTR_CDA_RESULTS_PEAK_SYMBOL_EVM

Returns the peak symbol EVM of the configured measurement channel. This value is expressed as a percentage.

#### Syntax

RFMXCDMA2K_ATTR_CDA_RESULTS_PEAK_SYMBOL_EVM

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6369299 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and named results.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__cda__results_1ga78bf016c5bcaa0c6f0c5ce8a0e3733bd.html language=enus -->
## TOPIC 00042: RFMXCDMA2K_ATTR_CDA_RESULTS_IQ_QUADRATURE_ERROR

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__cda__results_1ga78bf016c5bcaa0c6f0c5ce8a0e3733bd.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__cda__results_1ga78bf016c5bcaa0c6f0c5ce8a0e3733bd.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the I/Q quadrature error of the composite signal averaged over all measured slots. This value is expressed in degrees. SyntaxRFMXCDMA2K_ATTR_CDA_RESULTS_IQ_QUADRATURE_ERRORNumeric ValueData TypeAccessApplies To6369316float64Read-OnlyN/ARemarks You do not need to use a selector string to read

### RFMXCDMA2K_ATTR_CDA_RESULTS_IQ_QUADRATURE_ERROR

Returns the I/Q quadrature error of the composite signal averaged over all measured slots. This value is expressed in degrees.

#### Syntax

RFMXCDMA2K_ATTR_CDA_RESULTS_IQ_QUADRATURE_ERROR

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6369316 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and named results.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__cda__results_1ga78f16e39ead7a928a0bfebd2265ebb6f.html language=enus -->
## TOPIC 00043: RFMXCDMA2K_ATTR_CDA_RESULTS_MEAN_INACTIVE_POWER

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__cda__results_1ga78f16e39ead7a928a0bfebd2265ebb6f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__cda__results_1ga78f16e39ead7a928a0bfebd2265ebb6f.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the average code power, measured among the set of inactive channels, in the code domain of the base spreading factor. If you set the RFMXCDMA2K_ATTR_CDA_POWER_UNIT attribute to dBm, this measurement returns the absolute measured power; otherwise, this measurement returns a value relative to

### RFMXCDMA2K_ATTR_CDA_RESULTS_MEAN_INACTIVE_POWER

Returns the average code power, measured among the set of inactive channels, in the code domain of the base spreading factor. If you set the [RFMXCDMA2K_ATTR_CDA_POWER_UNIT](group____root__ni_r_fmx_c_d_m_a2k__attributes__cda_1ga19478b846aca6fda9fa5966c6b20f4af.html) attribute to **dBm**, this measurement returns the absolute measured power; otherwise, this measurement returns a value relative to the [RFMXCDMA2K_ATTR_CDA_RESULTS_TOTAL_POWER](group____root__ni_r_fmx_c_d_m_a2k__attributes__cda__results_1ga4caee61e88c05bffe087004448b5a4a9.html) attribute.

#### Syntax

RFMXCDMA2K_ATTR_CDA_RESULTS_MEAN_INACTIVE_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6369307 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and named results.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__cda__results_1ga8640ad3032569dce943f1737d8472021.html language=enus -->
## TOPIC 00044: RFMXCDMA2K_ATTR_CDA_RESULTS_MEAN_PILOT_POWER

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__cda__results_1ga8640ad3032569dce943f1737d8472021.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__cda__results_1ga8640ad3032569dce943f1737d8472021.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean power of the R-PICH. SyntaxRFMXCDMA2K_ATTR_CDA_RESULTS_MEAN_PILOT_POWERNumeric ValueData TypeAccessApplies To6369313float64Read-OnlyN/ARemarks Returns the mean power value in dB, when you set the RFMXCDMA2K_ATTR_CDA_POWER_UNIT attribute to dB.Returns the mean power value in dBm, whe

### RFMXCDMA2K_ATTR_CDA_RESULTS_MEAN_PILOT_POWER

Returns the mean power of the R-PICH.

#### Syntax

RFMXCDMA2K_ATTR_CDA_RESULTS_MEAN_PILOT_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6369313 | float64 | Read-Only | N/A |

#### Remarks

Returns the mean power value in dB, when you set the [RFMXCDMA2K_ATTR_CDA_POWER_UNIT](group____root__ni_r_fmx_c_d_m_a2k__attributes__cda_1ga19478b846aca6fda9fa5966c6b20f4af.html) attribute to **dB**.

Returns the mean power value in dBm, when you set the CDA Pwr Unit attribute to **dBm**.

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and named results.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__cda__results_1ga8ce061c68d78763af0787d49bfed9b65.html language=enus -->
## TOPIC 00045: RFMXCDMA2K_ATTR_CDA_RESULTS_IQ_GAIN_IMBALANCE

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__cda__results_1ga8ce061c68d78763af0787d49bfed9b65.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__cda__results_1ga8ce061c68d78763af0787d49bfed9b65.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the I/Q gain imbalance of the composite signal averaged over all measured slots. This value is expressed in dB. SyntaxRFMXCDMA2K_ATTR_CDA_RESULTS_IQ_GAIN_IMBALANCENumeric ValueData TypeAccessApplies To6369315float64Read-OnlyN/ARemarks You do not need to use a selector string to read this res

### RFMXCDMA2K_ATTR_CDA_RESULTS_IQ_GAIN_IMBALANCE

Returns the I/Q gain imbalance of the composite signal averaged over all measured slots. This value is expressed in dB.

#### Syntax

RFMXCDMA2K_ATTR_CDA_RESULTS_IQ_GAIN_IMBALANCE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6369315 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and named results.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__cda__results_1ga9a4a93beffe747748221859dd5d108ed.html language=enus -->
## TOPIC 00046: RFMXCDMA2K_ATTR_CDA_RESULTS_PEAK_INACTIVE_POWER

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__cda__results_1ga9a4a93beffe747748221859dd5d108ed.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__cda__results_1ga9a4a93beffe747748221859dd5d108ed.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum measured code power, measured among the set of inactive channels, in the code domain of the base spreading factor. If you set the RFMXCDMA2K_ATTR_CDA_POWER_UNIT attribute to dBm, this measurement returns the absolute measured power; otherwise, this measurement returns a value rel

### RFMXCDMA2K_ATTR_CDA_RESULTS_PEAK_INACTIVE_POWER

Returns the maximum measured code power, measured among the set of inactive channels, in the code domain of the base spreading factor. If you set the [RFMXCDMA2K_ATTR_CDA_POWER_UNIT](group____root__ni_r_fmx_c_d_m_a2k__attributes__cda_1ga19478b846aca6fda9fa5966c6b20f4af.html) attribute to **dBm**, this measurement returns the absolute measured power; otherwise, this measurement returns a value relative to the [RFMXCDMA2K_ATTR_CDA_RESULTS_TOTAL_POWER](group____root__ni_r_fmx_c_d_m_a2k__attributes__cda__results_1ga4caee61e88c05bffe087004448b5a4a9.html) attribute.

#### Syntax

RFMXCDMA2K_ATTR_CDA_RESULTS_PEAK_INACTIVE_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6369308 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and named results.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__cda__results_1ga9c2e3c111b8135208edd4638ae3e6760.html language=enus -->
## TOPIC 00047: RFMXCDMA2K_ATTR_CDA_RESULTS_PEAK_ACTIVE_POWER

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__cda__results_1ga9c2e3c111b8135208edd4638ae3e6760.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__cda__results_1ga9c2e3c111b8135208edd4638ae3e6760.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum power among all active code channels. If you set the RFMXCDMA2K_ATTR_CDA_POWER_UNIT attribute to dBm, this measurement returns the absolute measured power; otherwise, this measurement returns a value relative to the RFMXCDMA2K_ATTR_CDA_RESULTS_TOTAL_POWER attribute. SyntaxRFMXCDM

### RFMXCDMA2K_ATTR_CDA_RESULTS_PEAK_ACTIVE_POWER

Returns the maximum power among all active code channels. If you set the [RFMXCDMA2K_ATTR_CDA_POWER_UNIT](group____root__ni_r_fmx_c_d_m_a2k__attributes__cda_1ga19478b846aca6fda9fa5966c6b20f4af.html) attribute to **dBm**, this measurement returns the absolute measured power; otherwise, this measurement returns a value relative to the [RFMXCDMA2K_ATTR_CDA_RESULTS_TOTAL_POWER](group____root__ni_r_fmx_c_d_m_a2k__attributes__cda__results_1ga4caee61e88c05bffe087004448b5a4a9.html) attribute.

#### Syntax

RFMXCDMA2K_ATTR_CDA_RESULTS_PEAK_ACTIVE_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6369306 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and named results.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__cda__results_1ga9e763767e84aa184e3c4cbc80394dbd2.html language=enus -->
## TOPIC 00048: RFMXCDMA2K_ATTR_CDA_RESULTS_IQ_ORIGIN_OFFSET

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__cda__results_1ga9e763767e84aa184e3c4cbc80394dbd2.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__cda__results_1ga9e763767e84aa184e3c4cbc80394dbd2.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the I/Q origin offset of the composite signal averaged over all measured slots. This value is expressed in dB. SyntaxRFMXCDMA2K_ATTR_CDA_RESULTS_IQ_ORIGIN_OFFSETNumeric ValueData TypeAccessApplies To6369314float64Read-OnlyN/ARemarks You do not need to use a selector string to read this resul

### RFMXCDMA2K_ATTR_CDA_RESULTS_IQ_ORIGIN_OFFSET

Returns the I/Q origin offset of the composite signal averaged over all measured slots. This value is expressed in dB.

#### Syntax

RFMXCDMA2K_ATTR_CDA_RESULTS_IQ_ORIGIN_OFFSET

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6369314 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and named results.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__cda__results_1gaa6cfacd593c14f7ee727aaaa4a0737f8.html language=enus -->
## TOPIC 00049: RFMXCDMA2K_ATTR_CDA_RESULTS_RMS_SYMBOL_EVM

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__cda__results_1gaa6cfacd593c14f7ee727aaaa4a0737f8.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__cda__results_1gaa6cfacd593c14f7ee727aaaa4a0737f8.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the RMS symbol EVM of the configured measurement channel. This value is expressed as a percentage. SyntaxRFMXCDMA2K_ATTR_CDA_RESULTS_RMS_SYMBOL_EVMNumeric ValueData TypeAccessApplies To6369298float64Read-OnlyN/ARemarks You do not need to use a selector string to read this result for the defa

### RFMXCDMA2K_ATTR_CDA_RESULTS_RMS_SYMBOL_EVM

Returns the RMS symbol EVM of the configured measurement channel. This value is expressed as a percentage.

#### Syntax

RFMXCDMA2K_ATTR_CDA_RESULTS_RMS_SYMBOL_EVM

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6369298 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and named results.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__cda__results_1gaabf7b7d47d4892dd1857e87644604f43.html language=enus -->
## TOPIC 00050: RFMXCDMA2K_ATTR_CDA_RESULTS_CHIP_RATE_ERROR

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__cda__results_1gaabf7b7d47d4892dd1857e87644604f43.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__cda__results_1gaabf7b7d47d4892dd1857e87644604f43.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the chip rate error. This value is expressed in parts per million (ppm). SyntaxRFMXCDMA2K_ATTR_CDA_RESULTS_CHIP_RATE_ERRORNumeric ValueData TypeAccessApplies To6369318float64Read-OnlyN/ARemarks You do not need to use a selector string to read this result for the default signal and result ins

### RFMXCDMA2K_ATTR_CDA_RESULTS_CHIP_RATE_ERROR

Returns the chip rate error. This value is expressed in parts per million (ppm).

#### Syntax

RFMXCDMA2K_ATTR_CDA_RESULTS_CHIP_RATE_ERROR

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6369318 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and named results.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__cda__results_1gab9faf9cd4d6f8d96b55ac8c19eadad44.html language=enus -->
## TOPIC 00051: RFMXCDMA2K_ATTR_CDA_RESULTS_RMS_SYMBOL_MAGNITUDE_ERROR

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__cda__results_1gab9faf9cd4d6f8d96b55ac8c19eadad44.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__cda__results_1gab9faf9cd4d6f8d96b55ac8c19eadad44.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the RMS symbol magnitude error of the configured measurement channel. This value is expressed as a percentage. SyntaxRFMXCDMA2K_ATTR_CDA_RESULTS_RMS_SYMBOL_MAGNITUDE_ERRORNumeric ValueData TypeAccessApplies To6369300float64Read-OnlyN/ARemarks You do not need to use a selector string to read

### RFMXCDMA2K_ATTR_CDA_RESULTS_RMS_SYMBOL_MAGNITUDE_ERROR

Returns the RMS symbol magnitude error of the configured measurement channel. This value is expressed as a percentage.

#### Syntax

RFMXCDMA2K_ATTR_CDA_RESULTS_RMS_SYMBOL_MAGNITUDE_ERROR

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6369300 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and named results.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__cda__results_1gae55b131fb6e81a93d1493de20e5f84bb.html language=enus -->
## TOPIC 00052: RFMXCDMA2K_ATTR_CDA_RESULTS_FREQUENCY_ERROR

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__cda__results_1gae55b131fb6e81a93d1493de20e5f84bb.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__cda__results_1gae55b131fb6e81a93d1493de20e5f84bb.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the frequency error. This value is expressed in Hz. SyntaxRFMXCDMA2K_ATTR_CDA_RESULTS_FREQUENCY_ERRORNumeric ValueData TypeAccessApplies To6369317float64Read-OnlyN/ARemarks You do not need to use a selector string to read this result for the default signal and result instance. Refer to the S

### RFMXCDMA2K_ATTR_CDA_RESULTS_FREQUENCY_ERROR

Returns the frequency error. This value is expressed in Hz.

#### Syntax

RFMXCDMA2K_ATTR_CDA_RESULTS_FREQUENCY_ERROR

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6369317 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and named results.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__cda__results_1gae9dc48d5bfa30761562f1ab4c7e532ca.html language=enus -->
## TOPIC 00053: RFMXCDMA2K_ATTR_CDA_RESULTS_MEAN_SYMBOL_POWER

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__cda__results_1gae9dc48d5bfa30761562f1ab4c7e532ca.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__cda__results_1gae9dc48d5bfa30761562f1ab4c7e532ca.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean symbol power of the configured measurement channel. This value is expressed in dB, when you set the RFMXCDMA2K_ATTR_CDA_POWER_UNIT attribute to dB, and in dBm, when you set the CDA Pwr Unit attribute to dBm. SyntaxRFMXCDMA2K_ATTR_CDA_RESULTS_MEAN_SYMBOL_POWERNumeric ValueData TypeAc

### RFMXCDMA2K_ATTR_CDA_RESULTS_MEAN_SYMBOL_POWER

Returns the mean symbol power of the configured measurement channel. This value is expressed in dB, when you set the [RFMXCDMA2K_ATTR_CDA_POWER_UNIT](group____root__ni_r_fmx_c_d_m_a2k__attributes__cda_1ga19478b846aca6fda9fa5966c6b20f4af.html) attribute to **dB**, and in dBm, when you set the CDA Pwr Unit attribute to **dBm**.

#### Syntax

RFMXCDMA2K_ATTR_CDA_RESULTS_MEAN_SYMBOL_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6369302 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and named results.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__cda__results_1gaf4c216803708d215e72f786d82aae444.html language=enus -->
## TOPIC 00054: RFMXCDMA2K_ATTR_CDA_RESULTS_MEAN_ACTIVE_POWER

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__cda__results_1gaf4c216803708d215e72f786d82aae444.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__cda__results_1gaf4c216803708d215e72f786d82aae444.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the average power of all active code channels. If you set the RFMXCDMA2K_ATTR_CDA_POWER_UNIT attribute to dBm, this measurement returns the absolute measured power; otherwise, this measurement returns a value relative to the RFMXCDMA2K_ATTR_CDA_RESULTS_TOTAL_POWER attribute. SyntaxRFMXCDMA2K

### RFMXCDMA2K_ATTR_CDA_RESULTS_MEAN_ACTIVE_POWER

Returns the average power of all active code channels. If you set the [RFMXCDMA2K_ATTR_CDA_POWER_UNIT](group____root__ni_r_fmx_c_d_m_a2k__attributes__cda_1ga19478b846aca6fda9fa5966c6b20f4af.html) attribute to **dBm**, this measurement returns the absolute measured power; otherwise, this measurement returns a value relative to the [RFMXCDMA2K_ATTR_CDA_RESULTS_TOTAL_POWER](group____root__ni_r_fmx_c_d_m_a2k__attributes__cda__results_1ga4caee61e88c05bffe087004448b5a4a9.html) attribute.

#### Syntax

RFMXCDMA2K_ATTR_CDA_RESULTS_MEAN_ACTIVE_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6369305 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and named results.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__cda__results_1gaf97fdc01981205b3fb750e3e8e4d8411.html language=enus -->
## TOPIC 00055: RFMXCDMA2K_ATTR_CDA_RESULTS_Q_MEAN_ACTIVE_POWER

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__cda__results_1gaf97fdc01981205b3fb750e3e8e4d8411.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__cda__results_1gaf97fdc01981205b3fb750e3e8e4d8411.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the average power of all active code channels measured on the Q-branch. If you set the RFMXCDMA2K_ATTR_CDA_POWER_UNIT attribute to dBm, this measurement returns the absolute measured power; otherwise, this measurement returns a value relative to the RFMXCDMA2K_ATTR_CDA_RESULTS_TOTAL_POWER at

### RFMXCDMA2K_ATTR_CDA_RESULTS_Q_MEAN_ACTIVE_POWER

Returns the average power of all active code channels measured on the Q-branch. If you set the [RFMXCDMA2K_ATTR_CDA_POWER_UNIT](group____root__ni_r_fmx_c_d_m_a2k__attributes__cda_1ga19478b846aca6fda9fa5966c6b20f4af.html) attribute to **dBm**, this measurement returns the absolute measured power; otherwise, this measurement returns a value relative to the [RFMXCDMA2K_ATTR_CDA_RESULTS_TOTAL_POWER](group____root__ni_r_fmx_c_d_m_a2k__attributes__cda__results_1ga4caee61e88c05bffe087004448b5a4a9.html) attribute.

#### Syntax

RFMXCDMA2K_ATTR_CDA_RESULTS_Q_MEAN_ACTIVE_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6369311 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and named results.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__channel.html language=enus -->
## TOPIC 00056: Channel

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__channel.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__channel.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsUser DefinedGroup membersNameDescriptionRFMXCDMA2K_ATTR_CHANNEL_CONFIGURATION_MODESpecifies whether to detect the channels automatically or to use a specified channel configuration. AttachmentsNone

### Channel

#### Groups

- User Defined

#### Group members

| Name | Description |
| --- | --- |
| RFMXCDMA2K_ATTR_CHANNEL_CONFIGURATION_MODE | Specifies whether to detect the channels automatically or to use a specified channel configuration. |

#### Attachments

None

Parent topic:

Attributes

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__channel_1ga3c88eb1dedd8333791a4fdde39fcdb76.html language=enus -->
## TOPIC 00057: RFMXCDMA2K_ATTR_CHANNEL_CONFIGURATION_MODE

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__channel_1ga3c88eb1dedd8333791a4fdde39fcdb76.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__channel_1ga3c88eb1dedd8333791a4fdde39fcdb76.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to detect the channels automatically or to use a specified channel configuration. SyntaxRFMXCDMA2K_ATTR_CHANNEL_CONFIGURATION_MODENumeric ValueData TypeAccessApplies To6291474int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for

### RFMXCDMA2K_ATTR_CHANNEL_CONFIGURATION_MODE

Specifies whether to detect the channels automatically or to use a specified channel configuration.

#### Syntax

RFMXCDMA2K_ATTR_CHANNEL_CONFIGURATION_MODE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6291474 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **Auto Detect**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXCDMA2K_VAL_CHANNEL_CONFIGURATION_MODE_AUTO_DETECT | 0 (0x0) | Specifies that the system automatically detects the channels. |
| RFMXCDMA2K_VAL_CHANNEL_CONFIGURATION_MODE_USER_DEFINED | 1 (0x1) | Specifies that the system uses a specific channel configuration. |

Parent topic:

Channel

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__channel__user__defined.html language=enus -->
## TOPIC 00058: User Defined

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__channel__user__defined.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__channel__user__defined.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXCDMA2K_ATTR_BRANCHSpecifies the branch on which a specific user-defined channel is mapped. This attribute is used only when you set the RFMXCDMA2K_ATTR_CHANNEL_CONFIGURATION_MODE attribute to User Defined. RFMXCDMA2K_ATTR_NUMBER_OF_CHANNELSSpecifies the numb

### User Defined

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXCDMA2K_ATTR_BRANCH | Specifies the branch on which a specific user-defined channel is mapped. This attribute is used only when you set the RFMXCDMA2K_ATTR_CHANNEL_CONFIGURATION_MODE attribute to User Defined. |
| RFMXCDMA2K_ATTR_NUMBER_OF_CHANNELS | Specifies the number of user-defined channels. This attribute is used only when you set the RFMXCDMA2K_ATTR_CHANNEL_CONFIGURATION_MODE attribute to User Defined. |
| RFMXCDMA2K_ATTR_WALSH_CODE_LENGTH | Specifies the Walsh code length of a specific user-defined channel. This value is expressed in chips. This attribute is used only when you set the RFMXCDMA2K_ATTR_CHANNEL_CONFIGURATION_MODE attribute to User Defined. |
| RFMXCDMA2K_ATTR_WALSH_CODE_NUMBER | Specifies the Walsh code number of a specific user-defined channel. This attribute is used only when you set the RFMXCDMA2K_ATTR_CHANNEL_CONFIGURATION_MODE attribute to User Defined. |

#### Attachments

None

Parent topic:

Channel

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__channel__user__defined_1ga64cad65a1ef747d4f191a01c18ea7d92.html language=enus -->
## TOPIC 00059: RFMXCDMA2K_ATTR_WALSH_CODE_NUMBER

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__channel__user__defined_1ga64cad65a1ef747d4f191a01c18ea7d92.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__channel__user__defined_1ga64cad65a1ef747d4f191a01c18ea7d92.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the Walsh code number of a specific user-defined channel. This attribute is used only when you set the RFMXCDMA2K_ATTR_CHANNEL_CONFIGURATION_MODE attribute to User Defined. SyntaxRFMXCDMA2K_ATTR_WALSH_CODE_NUMBERNumeric ValueData TypeAccessApplies To6291480int32Read/WriteChannelRemarks Use

### RFMXCDMA2K_ATTR_WALSH_CODE_NUMBER

Specifies the Walsh code number of a specific user-defined channel. This attribute is used only when you set the [RFMXCDMA2K_ATTR_CHANNEL_CONFIGURATION_MODE](group____root__ni_r_fmx_c_d_m_a2k__attributes__channel_1ga3c88eb1dedd8333791a4fdde39fcdb76.html) attribute to **User Defined**.

#### Syntax

RFMXCDMA2K_ATTR_WALSH_CODE_NUMBER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6291480 | int32 | Read/Write | Channel |

#### Remarks

Use "channel< 
<format type="monospace-italic">n</format> 
>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute.

The default value is 0.

Parent topic:

User Defined

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__channel__user__defined_1gab475c1da29b878465c465e734bb9d801.html language=enus -->
## TOPIC 00060: RFMXCDMA2K_ATTR_BRANCH

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__channel__user__defined_1gab475c1da29b878465c465e734bb9d801.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__channel__user__defined_1gab475c1da29b878465c465e734bb9d801.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the branch on which a specific user-defined channel is mapped. This attribute is used only when you set the RFMXCDMA2K_ATTR_CHANNEL_CONFIGURATION_MODE attribute to User Defined. SyntaxRFMXCDMA2K_ATTR_BRANCHNumeric ValueData TypeAccessApplies To6291481int32Read/WriteChannelRemarks Use "chan

### RFMXCDMA2K_ATTR_BRANCH

Specifies the branch on which a specific user-defined channel is mapped. This attribute is used only when you set the [RFMXCDMA2K_ATTR_CHANNEL_CONFIGURATION_MODE](group____root__ni_r_fmx_c_d_m_a2k__attributes__channel_1ga3c88eb1dedd8333791a4fdde39fcdb76.html) attribute to **User Defined**.

#### Syntax

RFMXCDMA2K_ATTR_BRANCH

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6291481 | int32 | Read/Write | Channel |

#### Remarks

Use "channel< 
<format type="monospace-italic">n</format> 
>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute.

The default value is **I**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXCDMA2K_VAL_BRANCH_I | 0 (0x0) | Specifies the in-phase branch. |
| RFMXCDMA2K_VAL_BRANCH_Q | 1 (0x1) | Specifies the quadrature branch. |
| RFMXCDMA2K_VAL_BRANCH_I_AND_Q | 2 (0x2) | Specifies the in-phase and quadrature branch. |

Parent topic:

User Defined

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__channel__user__defined_1gac5eb7b8f150ac4a7dc978d48e713eeca.html language=enus -->
## TOPIC 00061: RFMXCDMA2K_ATTR_WALSH_CODE_LENGTH

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__channel__user__defined_1gac5eb7b8f150ac4a7dc978d48e713eeca.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__channel__user__defined_1gac5eb7b8f150ac4a7dc978d48e713eeca.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the Walsh code length of a specific user-defined channel. This value is expressed in chips. This attribute is used only when you set the RFMXCDMA2K_ATTR_CHANNEL_CONFIGURATION_MODE attribute to User Defined. SyntaxRFMXCDMA2K_ATTR_WALSH_CODE_LENGTHNumeric ValueData TypeAccessApplies To629147

### RFMXCDMA2K_ATTR_WALSH_CODE_LENGTH

Specifies the Walsh code length of a specific user-defined channel. This value is expressed in chips. This attribute is used only when you set the [RFMXCDMA2K_ATTR_CHANNEL_CONFIGURATION_MODE](group____root__ni_r_fmx_c_d_m_a2k__attributes__channel_1ga3c88eb1dedd8333791a4fdde39fcdb76.html) attribute to **User Defined**.

#### Syntax

RFMXCDMA2K_ATTR_WALSH_CODE_LENGTH

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6291479 | int32 | Read/Write | Channel |

#### Remarks

Use "channel< 
<format type="monospace-italic">n</format> 
>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute.

The default value is 64.

Parent topic:

User Defined

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__channel__user__defined_1gad734fb6771b31563a4dd28ba6f76d91c.html language=enus -->
## TOPIC 00062: RFMXCDMA2K_ATTR_NUMBER_OF_CHANNELS

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__channel__user__defined_1gad734fb6771b31563a4dd28ba6f76d91c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__channel__user__defined_1gad734fb6771b31563a4dd28ba6f76d91c.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of user-defined channels. This attribute is used only when you set the RFMXCDMA2K_ATTR_CHANNEL_CONFIGURATION_MODE attribute to User Defined. SyntaxRFMXCDMA2K_ATTR_NUMBER_OF_CHANNELSNumeric ValueData TypeAccessApplies To6291478int32Read/WriteN/ARemarks You do not need to use a se

### RFMXCDMA2K_ATTR_NUMBER_OF_CHANNELS

Specifies the number of user-defined channels. This attribute is used only when you set the [RFMXCDMA2K_ATTR_CHANNEL_CONFIGURATION_MODE](group____root__ni_r_fmx_c_d_m_a2k__attributes__channel_1ga3c88eb1dedd8333791a4fdde39fcdb76.html) attribute to **User Defined**.

#### Syntax

RFMXCDMA2K_ATTR_NUMBER_OF_CHANNELS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6291478 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 0.

Parent topic:

User Defined

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__chp.html language=enus -->
## TOPIC 00063: CHP

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__chp.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__chp.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsAveragingRBW FilterResultsSweep TimeGroup membersNameDescriptionRFMXCDMA2K_ATTR_CHP_ALL_TRACES_ENABLEDSpecifies whether to enable the traces to be stored and retrieved after performing the CHP measurement. RFMXCDMA2K_ATTR_CHP_INTEGRATION_BANDWIDTHReturns the CHP carrier integration bandwidth.

### CHP

#### Groups

- Averaging
- RBW Filter
- Results
- Sweep Time

#### Group members

| Name | Description |
| --- | --- |
| RFMXCDMA2K_ATTR_CHP_ALL_TRACES_ENABLED | Specifies whether to enable the traces to be stored and retrieved after performing the CHP measurement. |
| RFMXCDMA2K_ATTR_CHP_INTEGRATION_BANDWIDTH | Returns the CHP carrier integration bandwidth. This value is expressed in Hz. |
| RFMXCDMA2K_ATTR_CHP_MEASUREMENT_ENABLED | Specifies whether to enable the CHP measurement. |
| RFMXCDMA2K_ATTR_CHP_NUMBER_OF_ANALYSIS_THREADS | Specifies the maximum number of threads used for parallelism for the CHP measurement. |

#### Attachments

None

Parent topic:

Attributes

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__chp_1ga2743b472eaf0a48218d40b54e5eb541e.html language=enus -->
## TOPIC 00064: RFMXCDMA2K_ATTR_CHP_MEASUREMENT_ENABLED

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__chp_1ga2743b472eaf0a48218d40b54e5eb541e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__chp_1ga2743b472eaf0a48218d40b54e5eb541e.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the CHP measurement. SyntaxRFMXCDMA2K_ATTR_CHP_MEASUREMENT_ENABLEDNumeric ValueData TypeAccessApplies To6303744int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Str

### RFMXCDMA2K_ATTR_CHP_MEASUREMENT_ENABLED

Specifies whether to enable the CHP measurement.

#### Syntax

RFMXCDMA2K_ATTR_CHP_MEASUREMENT_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6303744 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is FALSE.

Parent topic:

CHP

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__chp_1ga47c02bf6143169c09260c4550bc583ef.html language=enus -->
## TOPIC 00065: RFMXCDMA2K_ATTR_CHP_INTEGRATION_BANDWIDTH

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__chp_1ga47c02bf6143169c09260c4550bc583ef.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__chp_1ga47c02bf6143169c09260c4550bc583ef.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the CHP carrier integration bandwidth. This value is expressed in Hz. SyntaxRFMXCDMA2K_ATTR_CHP_INTEGRATION_BANDWIDTHNumeric ValueData TypeAccessApplies To6303746float64Read-OnlyN/ARemarks You do not need to use a selector string to read this attribute for the default signal instance. Refer

### RFMXCDMA2K_ATTR_CHP_INTEGRATION_BANDWIDTH

Returns the CHP carrier integration bandwidth. This value is expressed in Hz.

#### Syntax

RFMXCDMA2K_ATTR_CHP_INTEGRATION_BANDWIDTH

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6303746 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

Parent topic:

CHP

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__chp_1gacccb45dff425df12222b6d56362d0f98.html language=enus -->
## TOPIC 00066: RFMXCDMA2K_ATTR_CHP_NUMBER_OF_ANALYSIS_THREADS

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__chp_1gacccb45dff425df12222b6d56362d0f98.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__chp_1gacccb45dff425df12222b6d56362d0f98.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the maximum number of threads used for parallelism for the CHP measurement. SyntaxRFMXCDMA2K_ATTR_CHP_NUMBER_OF_ANALYSIS_THREADSNumeric ValueData TypeAccessApplies To6303747int32Read/WriteN/ARemarks The number of threads can range from 1 to the number of physical cores. The number of threa

### RFMXCDMA2K_ATTR_CHP_NUMBER_OF_ANALYSIS_THREADS

Specifies the maximum number of threads used for parallelism for the CHP measurement.

#### Syntax

RFMXCDMA2K_ATTR_CHP_NUMBER_OF_ANALYSIS_THREADS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6303747 | int32 | Read/Write | N/A |

#### Remarks

The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations.

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 1.

Parent topic:

CHP

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__chp__averaging.html language=enus -->
## TOPIC 00067: Averaging

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__chp__averaging.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__chp__averaging.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXCDMA2K_ATTR_CHP_AVERAGING_COUNTSpecifies the number of acquisitions used for averaging when you set the RFMXCDMA2K_ATTR_CHP_AVERAGING_ENABLED attribute to True. RFMXCDMA2K_ATTR_CHP_AVERAGING_ENABLEDSpecifies whether to enable averaging for the CHP measuremen

### Averaging

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXCDMA2K_ATTR_CHP_AVERAGING_COUNT | Specifies the number of acquisitions used for averaging when you set the RFMXCDMA2K_ATTR_CHP_AVERAGING_ENABLED attribute to True. |
| RFMXCDMA2K_ATTR_CHP_AVERAGING_ENABLED | Specifies whether to enable averaging for the CHP measurement. |
| RFMXCDMA2K_ATTR_CHP_AVERAGING_TYPE | Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the CHP measurement. |

#### Attachments

None

Parent topic:

CHP

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__chp__averaging_1gadb9ff8d7f8724912dd7f4095292e4d87.html language=enus -->
## TOPIC 00068: RFMXCDMA2K_ATTR_CHP_AVERAGING_COUNT

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__chp__averaging_1gadb9ff8d7f8724912dd7f4095292e4d87.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__chp__averaging_1gadb9ff8d7f8724912dd7f4095292e4d87.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of acquisitions used for averaging when you set the RFMXCDMA2K_ATTR_CHP_AVERAGING_ENABLED attribute to True. SyntaxRFMXCDMA2K_ATTR_CHP_AVERAGING_COUNTNumeric ValueData TypeAccessApplies To6303750int32Read/WriteN/ARemarks You do not need to use a selector string to configure or r

### RFMXCDMA2K_ATTR_CHP_AVERAGING_COUNT

Specifies the number of acquisitions used for averaging when you set the [RFMXCDMA2K_ATTR_CHP_AVERAGING_ENABLED](group____root__ni_r_fmx_c_d_m_a2k__attributes__chp__averaging_1gaf9fcb9377f3f83f0436ba17254e0e730.html) attribute to **True**.

#### Syntax

RFMXCDMA2K_ATTR_CHP_AVERAGING_COUNT

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6303750 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 10.

Parent topic:

Averaging

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__chp__averaging_1gaf4de088a5d3eaa34a210b43d5285c8d8.html language=enus -->
## TOPIC 00069: RFMXCDMA2K_ATTR_CHP_AVERAGING_TYPE

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__chp__averaging_1gaf4de088a5d3eaa34a210b43d5285c8d8.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__chp__averaging_1gaf4de088a5d3eaa34a210b43d5285c8d8.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the CHP measurement. SyntaxRFMXCDMA2K_ATTR_CHP_AVERAGING_TYPENumeric ValueData TypeAccessApplies To6303753int32Read/WriteN/ARemarks You do not need to use a selector string to configure or re

### RFMXCDMA2K_ATTR_CHP_AVERAGING_TYPE

Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the CHP measurement.

#### Syntax

RFMXCDMA2K_ATTR_CHP_AVERAGING_TYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6303753 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **RMS**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXCDMA2K_VAL_CHP_AVERAGING_TYPE_RMS | 0 (0x0) | The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. |
| RFMXCDMA2K_VAL_CHP_AVERAGING_TYPE_LOG | 1 (0x1) | The power spectrum is averaged on a logarithmic scale. |
| RFMXCDMA2K_VAL_CHP_AVERAGING_TYPE_SCALAR | 2 (0x2) | The square root of the power spectrum is averaged. |
| RFMXCDMA2K_VAL_CHP_AVERAGING_TYPE_MAXIMUM | 3 (0x3) | The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. |
| RFMXCDMA2K_VAL_CHP_AVERAGING_TYPE_MINIMUM | 4 (0x4) | The lowest power in the spectrum at each frequency bin is retained from one acquisition to the next. |

Parent topic:

Averaging

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__chp__rbw__filter.html language=enus -->
## TOPIC 00070: RBW Filter

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__chp__rbw__filter.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__chp__rbw__filter.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXCDMA2K_ATTR_CHP_RBW_FILTER_AUTO_BANDWIDTHSpecifies whether the measurement computes the RBW. RFMXCDMA2K_ATTR_CHP_RBW_FILTER_BANDWIDTHSpecifies the bandwidth of the RBW filter used to sweep the acquired signal when you set the RFMXCDMA2K_ATTR_CHP_RBW_FILTER_A

### RBW Filter

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXCDMA2K_ATTR_CHP_RBW_FILTER_AUTO_BANDWIDTH | Specifies whether the measurement computes the RBW. |
| RFMXCDMA2K_ATTR_CHP_RBW_FILTER_BANDWIDTH | Specifies the bandwidth of the RBW filter used to sweep the acquired signal when you set the RFMXCDMA2K_ATTR_CHP_RBW_FILTER_AUTO_BANDWIDTH attribute to False. This value is expressed in Hz. |
| RFMXCDMA2K_ATTR_CHP_RBW_FILTER_TYPE | Specifies the shape of the digital RBW filter. |

#### Attachments

None

Parent topic:

CHP

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__chp__rbw__filter_1ga062d87befc548aa0733ed2f09702e70d.html language=enus -->
## TOPIC 00071: RFMXCDMA2K_ATTR_CHP_RBW_FILTER_AUTO_BANDWIDTH

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__chp__rbw__filter_1ga062d87befc548aa0733ed2f09702e70d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__chp__rbw__filter_1ga062d87befc548aa0733ed2f09702e70d.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement computes the RBW. SyntaxRFMXCDMA2K_ATTR_CHP_RBW_FILTER_AUTO_BANDWIDTHNumeric ValueData TypeAccessApplies To6303756int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Sel

### RFMXCDMA2K_ATTR_CHP_RBW_FILTER_AUTO_BANDWIDTH

Specifies whether the measurement computes the RBW.

#### Syntax

RFMXCDMA2K_ATTR_CHP_RBW_FILTER_AUTO_BANDWIDTH

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6303756 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **True**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXCDMA2K_VAL_CHP_RBW_AUTO_FALSE | 0 (0x0) | The measurement uses the RBW that you specify in the RFMXCDMA2K_ATTR_CHP_RBW_FILTER_BANDWIDTH attribute. |
| RFMXCDMA2K_VAL_CHP_RBW_AUTO_TRUE | 1 (0x1) | The measurement computes the RBW. |

Parent topic:

RBW Filter

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__chp__rbw__filter_1ga23782e1a6b31fb709bef302b6374c287.html language=enus -->
## TOPIC 00072: RFMXCDMA2K_ATTR_CHP_RBW_FILTER_TYPE

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__chp__rbw__filter_1ga23782e1a6b31fb709bef302b6374c287.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__chp__rbw__filter_1ga23782e1a6b31fb709bef302b6374c287.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the shape of the digital RBW filter. SyntaxRFMXCDMA2K_ATTR_CHP_RBW_FILTER_TYPENumeric ValueData TypeAccessApplies To6303758int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector String to

### RFMXCDMA2K_ATTR_CHP_RBW_FILTER_TYPE

Specifies the shape of the digital RBW filter.

#### Syntax

RFMXCDMA2K_ATTR_CHP_RBW_FILTER_TYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6303758 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **Gaussian**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXCDMA2K_VAL_CHP_RBW_FILTER_TYPE_FFT_BASED | 0 (0x0) | No RBW filtering is performed. |
| RFMXCDMA2K_VAL_CHP_RBW_FILTER_TYPE_GAUSSIAN | 1 (0x1) | An RBW filter with a Gaussian response is applied. |
| RFMXCDMA2K_VAL_CHP_RBW_FILTER_TYPE_FLAT | 2 (0x2) | An RBW filter with a flat response is applied. |

Parent topic:

RBW Filter

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__chp__rbw__filter_1ga81ca2646938ab1e226ca768a5f85d804.html language=enus -->
## TOPIC 00073: RFMXCDMA2K_ATTR_CHP_RBW_FILTER_BANDWIDTH

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__chp__rbw__filter_1ga81ca2646938ab1e226ca768a5f85d804.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__chp__rbw__filter_1ga81ca2646938ab1e226ca768a5f85d804.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the bandwidth of the RBW filter used to sweep the acquired signal when you set the RFMXCDMA2K_ATTR_CHP_RBW_FILTER_AUTO_BANDWIDTH attribute to False. This value is expressed in Hz. SyntaxRFMXCDMA2K_ATTR_CHP_RBW_FILTER_BANDWIDTHNumeric ValueData TypeAccessApplies To6303757float64Read/WriteN/

### RFMXCDMA2K_ATTR_CHP_RBW_FILTER_BANDWIDTH

Specifies the bandwidth of the RBW filter used to sweep the acquired signal when you set the [RFMXCDMA2K_ATTR_CHP_RBW_FILTER_AUTO_BANDWIDTH](group____root__ni_r_fmx_c_d_m_a2k__attributes__chp__rbw__filter_1ga062d87befc548aa0733ed2f09702e70d.html) attribute to **False**. This value is expressed in Hz.

#### Syntax

RFMXCDMA2K_ATTR_CHP_RBW_FILTER_BANDWIDTH

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6303757 | float64 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 10 kHz.

Parent topic:

RBW Filter

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__chp__results.html language=enus -->
## TOPIC 00074: Results

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__chp__results.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__chp__results.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsCarrierGroup membersNoneAttachmentsNone

### Results

#### Groups

- Carrier

#### Group members

None

#### Attachments

None

Parent topic:

CHP

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__chp__results__carrier.html language=enus -->
## TOPIC 00075: Carrier

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__chp__results__carrier.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__chp__results__carrier.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXCDMA2K_ATTR_CHP_RESULTS_CARRIER_ABSOLUTE_POWERReturns the averaged CHP measured in the specified integration bandwidth. This value is expressed in dBm. AttachmentsNone

### Carrier

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXCDMA2K_ATTR_CHP_RESULTS_CARRIER_ABSOLUTE_POWER | Returns the averaged CHP measured in the specified integration bandwidth. This value is expressed in dBm. |

#### Attachments

None

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__chp__results__carrier_1gaf28d0a8ea01862cefdb68f843892649f.html language=enus -->
## TOPIC 00076: RFMXCDMA2K_ATTR_CHP_RESULTS_CARRIER_ABSOLUTE_POWER

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__chp__results__carrier_1gaf28d0a8ea01862cefdb68f843892649f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__chp__results__carrier_1gaf28d0a8ea01862cefdb68f843892649f.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the averaged CHP measured in the specified integration bandwidth. This value is expressed in dBm. SyntaxRFMXCDMA2K_ATTR_CHP_RESULTS_CARRIER_ABSOLUTE_POWERNumeric ValueData TypeAccessApplies To6303765float64Read-OnlyN/ARemarks You do not need to use a selector string to read this result for t

### RFMXCDMA2K_ATTR_CHP_RESULTS_CARRIER_ABSOLUTE_POWER

Returns the averaged CHP measured in the specified integration bandwidth. This value is expressed in dBm.

#### Syntax

RFMXCDMA2K_ATTR_CHP_RESULTS_CARRIER_ABSOLUTE_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6303765 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and named results.

Parent topic:

Carrier

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__chp__sweep__time_1ga07355cd7c4aea628eb2ee7f45233c318.html language=enus -->
## TOPIC 00077: RFMXCDMA2K_ATTR_CHP_SWEEP_TIME_INTERVAL

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__chp__sweep__time_1ga07355cd7c4aea628eb2ee7f45233c318.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__chp__sweep__time_1ga07355cd7c4aea628eb2ee7f45233c318.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the sweep time when you set the RFMXCDMA2K_ATTR_CHP_SWEEP_TIME_AUTO attribute to False. This value is expressed in seconds. SyntaxRFMXCDMA2K_ATTR_CHP_SWEEP_TIME_INTERVALNumeric ValueData TypeAccessApplies To6303762float64Read/WriteN/ARemarks You do not need to use a selector string to conf

### RFMXCDMA2K_ATTR_CHP_SWEEP_TIME_INTERVAL

Specifies the sweep time when you set the [RFMXCDMA2K_ATTR_CHP_SWEEP_TIME_AUTO](group____root__ni_r_fmx_c_d_m_a2k__attributes__chp__sweep__time_1ga1232416e27cbbe1588442a1f5c1af14e.html) attribute to **False**. This value is expressed in seconds.

#### Syntax

RFMXCDMA2K_ATTR_CHP_SWEEP_TIME_INTERVAL

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6303762 | float64 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 0.001667 seconds.

Parent topic:

Sweep Time

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__chp__sweep__time_1ga1232416e27cbbe1588442a1f5c1af14e.html language=enus -->
## TOPIC 00078: RFMXCDMA2K_ATTR_CHP_SWEEP_TIME_AUTO

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__chp__sweep__time_1ga1232416e27cbbe1588442a1f5c1af14e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__chp__sweep__time_1ga1232416e27cbbe1588442a1f5c1af14e.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement computes the sweep time. SyntaxRFMXCDMA2K_ATTR_CHP_SWEEP_TIME_AUTONumeric ValueData TypeAccessApplies To6303761int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Select

### RFMXCDMA2K_ATTR_CHP_SWEEP_TIME_AUTO

Specifies whether the measurement computes the sweep time.

#### Syntax

RFMXCDMA2K_ATTR_CHP_SWEEP_TIME_AUTO

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6303761 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **True**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXCDMA2K_VAL_CHP_SWEEP_TIME_AUTO_FALSE | 0 (0x0) | The measurement uses the sweep time that you specify in the RFMXCDMA2K_ATTR_CHP_SWEEP_TIME_INTERVAL attribute. |
| RFMXCDMA2K_VAL_CHP_SWEEP_TIME_AUTO_TRUE | 1 (0x1) | The measurement uses the default sweep time of 0.001667 seconds. |

Parent topic:

Sweep Time

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__modacc.html language=enus -->
## TOPIC 00079: ModAcc

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__modacc.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__modacc.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsMulti Carrier FilterResultsGroup membersNameDescriptionRFMXCDMA2K_ATTR_MODACC_ALL_TRACES_ENABLEDSpecifies whether to enable the traces to be stored and retrieved after performing the modulation accuracy (ModAcc) measurement. RFMXCDMA2K_ATTR_MODACC_IQ_GAIN_IMBALANCE_REMOVAL_ENABLEDSpecifies whe

### ModAcc

#### Groups

- Multi Carrier Filter
- Results

#### Group members

| Name | Description |
| --- | --- |
| RFMXCDMA2K_ATTR_MODACC_ALL_TRACES_ENABLED | Specifies whether to enable the traces to be stored and retrieved after performing the modulation accuracy (ModAcc) measurement. |
| RFMXCDMA2K_ATTR_MODACC_IQ_GAIN_IMBALANCE_REMOVAL_ENABLED | Specifies whether to remove the I/Q gain imbalance before an EVM measurement. |
| RFMXCDMA2K_ATTR_MODACC_IQ_OFFSET_REMOVAL_ENABLED | Specifies whether to remove the I/Q offset before an EVM measurement. |
| RFMXCDMA2K_ATTR_MODACC_IQ_QUADRATURE_ERROR_REMOVAL_ENABLED | Specifies whether to remove the I/Q quadrature error before an EVM measurement. |
| RFMXCDMA2K_ATTR_MODACC_MEASUREMENT_ENABLED | Specifies whether to enable the modulation accuracy (ModAcc) measurement. |
| RFMXCDMA2K_ATTR_MODACC_MEASUREMENT_LENGTH | Specifies the duration of the modulation accuracy (ModAcc) measurement. This value is expressed in slots. |
| RFMXCDMA2K_ATTR_MODACC_MEASUREMENT_OFFSET | Specifies the measurement offset to skip from the synchronization boundary. The synchronization boundary is specified by the RFMXCDMA2K_ATTR_MODACC_SYNCHRONIZATION_MODE attribute. This value is expressed in slots. |
| RFMXCDMA2K_ATTR_MODACC_RECEIVE_FILTER_ENABLED | Specifies whether to enable the received filter for the ModAcc measurement. For RC1/2, this attribute refers to the band-limiting filter specified in the Chapter 6.4.2.1 of 3GPP2 C.S0011-E. |
| RFMXCDMA2K_ATTR_MODACC_SPECTRUM_INVERTED | Specifies whether the spectrum of the signal is inverted. |
| RFMXCDMA2K_ATTR_MODACC_SYNCHRONIZATION_MODE | Specifies whether the measurement is performed from the frame, slot, or symbol boundary. |

#### Attachments

None

Parent topic:

Attributes

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__modacc_1ga63c0b3bdd92756c566aec883ddc41fe8.html language=enus -->
## TOPIC 00080: RFMXCDMA2K_ATTR_MODACC_SPECTRUM_INVERTED

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__modacc_1ga63c0b3bdd92756c566aec883ddc41fe8.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__modacc_1ga63c0b3bdd92756c566aec883ddc41fe8.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the spectrum of the signal is inverted. SyntaxRFMXCDMA2K_ATTR_MODACC_SPECTRUM_INVERTEDNumeric ValueData TypeAccessApplies To6361097int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Se

### RFMXCDMA2K_ATTR_MODACC_SPECTRUM_INVERTED

Specifies whether the spectrum of the signal is inverted.

#### Syntax

RFMXCDMA2K_ATTR_MODACC_SPECTRUM_INVERTED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6361097 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **False**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXCDMA2K_VAL_MODACC_SPECTRUM_INVERTED_FALSE | 0 (0x0) | The measured spectrum is not inverted. |
| RFMXCDMA2K_VAL_MODACC_SPECTRUM_INVERTED_TRUE | 1 (0x1) | The measured spectrum is inverted. |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__modacc_1ga67d71ee11543ff4ba24d07e177785381.html language=enus -->
## TOPIC 00081: RFMXCDMA2K_ATTR_MODACC_SYNCHRONIZATION_MODE

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__modacc_1ga67d71ee11543ff4ba24d07e177785381.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__modacc_1ga67d71ee11543ff4ba24d07e177785381.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement is performed from the frame, slot, or symbol boundary. SyntaxRFMXCDMA2K_ATTR_MODACC_SYNCHRONIZATION_MODENumeric ValueData TypeAccessApplies To6361093int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the defaul

### RFMXCDMA2K_ATTR_MODACC_SYNCHRONIZATION_MODE

Specifies whether the measurement is performed from the frame, slot, or symbol boundary.

#### Syntax

RFMXCDMA2K_ATTR_MODACC_SYNCHRONIZATION_MODE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6361093 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **Slot**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXCDMA2K_VAL_MODACC_SYNCHRONIZATION_MODE_FRAME | 0 (0x0) | The frame boundary is detected, and the measurement is performed over the RFMXCDMA2K_ATTR_MODACC_MEASUREMENT_LENGTH attribute starting at the RFMXCDMA2K_ATTR_MODACC_MEASUREMENT_OFFSET attribute from the frame boundary. |
| RFMXCDMA2K_VAL_MODACC_SYNCHRONIZATION_MODE_SLOT | 1 (0x1) | The slot boundary is detected, and the measurement is performed over the ModAcc Meas Length attribute starting at the ModAcc Meas Offset attribute from the slot boundary. |
| RFMXCDMA2K_VAL_MODACC_SYNCHRONIZATION_MODE_ARBITRARY | 2 (0x2) | The symbol boundary is detected, and the measurement is performed over the ModAcc Meas Length attribute starting at the ModAcc Meas Offset attribute from the slot boundary. |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__modacc_1ga7c395b31f794f31b0fbe5eb1e36b355d.html language=enus -->
## TOPIC 00082: RFMXCDMA2K_ATTR_MODACC_MEASUREMENT_LENGTH

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__modacc_1ga7c395b31f794f31b0fbe5eb1e36b355d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__modacc_1ga7c395b31f794f31b0fbe5eb1e36b355d.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the duration of the modulation accuracy (ModAcc) measurement. This value is expressed in slots. SyntaxRFMXCDMA2K_ATTR_MODACC_MEASUREMENT_LENGTHNumeric ValueData TypeAccessApplies To6361095int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute

### RFMXCDMA2K_ATTR_MODACC_MEASUREMENT_LENGTH

Specifies the duration of the modulation accuracy (ModAcc) measurement. This value is expressed in slots.

#### Syntax

RFMXCDMA2K_ATTR_MODACC_MEASUREMENT_LENGTH

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6361095 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 1. The valid values are 1 to 16, inclusive. The sum of the ModAcc measurement offset and the ModAcc measurement length must be less than or equal to 16.

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__modacc_1ga7df72a952eab1aa3730151e8f10261fd.html language=enus -->
## TOPIC 00083: RFMXCDMA2K_ATTR_MODACC_IQ_GAIN_IMBALANCE_REMOVAL_ENABLED

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__modacc_1ga7df72a952eab1aa3730151e8f10261fd.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__modacc_1ga7df72a952eab1aa3730151e8f10261fd.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to remove the I/Q gain imbalance before an EVM measurement. SyntaxRFMXCDMA2K_ATTR_MODACC_IQ_GAIN_IMBALANCE_REMOVAL_ENABLEDNumeric ValueData TypeAccessApplies To6361249int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the defa

### RFMXCDMA2K_ATTR_MODACC_IQ_GAIN_IMBALANCE_REMOVAL_ENABLED

Specifies whether to remove the I/Q gain imbalance before an EVM measurement.

#### Syntax

RFMXCDMA2K_ATTR_MODACC_IQ_GAIN_IMBALANCE_REMOVAL_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6361249 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **False**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXCDMA2K_VAL_MODACC_IQ_GAIN_IMBALANCE_REMOVAL_ENABLED_FALSE | 0 (0x0) | I/Q gain imbalance is not removed before the EVM measurement. |
| RFMXCDMA2K_VAL_MODACC_IQ_GAIN_IMBALANCE_REMOVAL_ENABLED_TRUE | 1 (0x1) | I/Q gain imbalance is removed before the EVM measurement. |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__modacc_1gadbb8d589b555218a4ddf7534f6540b4a.html language=enus -->
## TOPIC 00084: RFMXCDMA2K_ATTR_MODACC_RECEIVE_FILTER_ENABLED

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__modacc_1gadbb8d589b555218a4ddf7534f6540b4a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__modacc_1gadbb8d589b555218a4ddf7534f6540b4a.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the received filter for the ModAcc measurement. For RC1/2, this attribute refers to the band-limiting filter specified in the Chapter 6.4.2.1 of 3GPP2 C.S0011-E. SyntaxRFMXCDMA2K_ATTR_MODACC_RECEIVE_FILTER_ENABLEDNumeric ValueData TypeAccessApplies To6361251int32Read/Writ

### RFMXCDMA2K_ATTR_MODACC_RECEIVE_FILTER_ENABLED

Specifies whether to enable the received filter for the ModAcc measurement. For RC1/2, this attribute refers to the band-limiting filter specified in the Chapter 6.4.2.1 of *3GPP2 C.S0011-E*.

#### Syntax

RFMXCDMA2K_ATTR_MODACC_RECEIVE_FILTER_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6361251 | int32 | Read/Write | N/A |

#### Remarks

For RC3/4, this attribute refers to the complementary filter specified in the Chapter 6.4.2.2 of *3GPP2 C.S0011-E*.

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **True**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXCDMA2K_VAL_MODACC_RECEIVE_FILTER_ENABLED_FALSE | 0 (0x0) | Disables received filtering for the ModAcc measurement. |
| RFMXCDMA2K_VAL_MODACC_RECEIVE_FILTER_ENABLED_TRUE | 1 (0x1) | Enables received filtering for the ModAcc measurement. |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__modacc_1gae360f6495983b7abf33ced23cf1f3dc3.html language=enus -->
## TOPIC 00085: RFMXCDMA2K_ATTR_MODACC_IQ_OFFSET_REMOVAL_ENABLED

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__modacc_1gae360f6495983b7abf33ced23cf1f3dc3.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__modacc_1gae360f6495983b7abf33ced23cf1f3dc3.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to remove the I/Q offset before an EVM measurement. SyntaxRFMXCDMA2K_ATTR_MODACC_IQ_OFFSET_REMOVAL_ENABLEDNumeric ValueData TypeAccessApplies To6361096int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal insta

### RFMXCDMA2K_ATTR_MODACC_IQ_OFFSET_REMOVAL_ENABLED

Specifies whether to remove the I/Q offset before an EVM measurement.

#### Syntax

RFMXCDMA2K_ATTR_MODACC_IQ_OFFSET_REMOVAL_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6361096 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **False**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXCDMA2K_VAL_MODACC_IQ_OFFSET_REMOVAL_ENABLED_FALSE | 0 (0x0) | I/Q offset is not removed before the EVM measurement. |
| RFMXCDMA2K_VAL_MODACC_IQ_OFFSET_REMOVAL_ENABLED_TRUE | 1 (0x1) | I/Q offset is removed before the EVM measurement. |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__modacc_1gaf1460466fce67a919e2bce97a87cea3a.html language=enus -->
## TOPIC 00086: RFMXCDMA2K_ATTR_MODACC_ALL_TRACES_ENABLED

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__modacc_1gaf1460466fce67a919e2bce97a87cea3a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__modacc_1gaf1460466fce67a919e2bce97a87cea3a.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the traces to be stored and retrieved after performing the modulation accuracy (ModAcc) measurement. SyntaxRFMXCDMA2K_ATTR_MODACC_ALL_TRACES_ENABLEDNumeric ValueData TypeAccessApplies To6361109int32Read/WriteN/ARemarks You do not need to use a selector string to configure

### RFMXCDMA2K_ATTR_MODACC_ALL_TRACES_ENABLED

Specifies whether to enable the traces to be stored and retrieved after performing the modulation accuracy (ModAcc) measurement.

#### Syntax

RFMXCDMA2K_ATTR_MODACC_ALL_TRACES_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6361109 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is FALSE.

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__modacc_1gaf36ed4ae9db2fd48cdd8022244e2f0fc.html language=enus -->
## TOPIC 00087: RFMXCDMA2K_ATTR_MODACC_MEASUREMENT_OFFSET

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__modacc_1gaf36ed4ae9db2fd48cdd8022244e2f0fc.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__modacc_1gaf36ed4ae9db2fd48cdd8022244e2f0fc.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the measurement offset to skip from the synchronization boundary. The synchronization boundary is specified by the RFMXCDMA2K_ATTR_MODACC_SYNCHRONIZATION_MODE attribute. This value is expressed in slots. SyntaxRFMXCDMA2K_ATTR_MODACC_MEASUREMENT_OFFSETNumeric ValueData TypeAccessApplies To6

### RFMXCDMA2K_ATTR_MODACC_MEASUREMENT_OFFSET

Specifies the measurement offset to skip from the synchronization boundary. The synchronization boundary is specified by the [RFMXCDMA2K_ATTR_MODACC_SYNCHRONIZATION_MODE](group____root__ni_r_fmx_c_d_m_a2k__attributes__modacc_1ga67d71ee11543ff4ba24d07e177785381.html) attribute. This value is expressed in slots.

#### Syntax

RFMXCDMA2K_ATTR_MODACC_MEASUREMENT_OFFSET

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6361094 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 0. The valid values are 1 to 16, inclusive. The sum of the ModAcc measurement offset and the ModAcc measurement length must be less than or equal to 16.

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__modacc__multi__carrier__filter.html language=enus -->
## TOPIC 00088: Multi Carrier Filter

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__modacc__multi__carrier__filter.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__modacc__multi__carrier__filter.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXCDMA2K_ATTR_MODACC_MULTI_CARRIER_FILTER_ENABLEDSpecifies whether to enable the multi carrier filter which can be used to improve ModAcc measurement quality in presence of neighboring carriers. AttachmentsNone

### Multi Carrier Filter

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXCDMA2K_ATTR_MODACC_MULTI_CARRIER_FILTER_ENABLED | Specifies whether to enable the multi carrier filter which can be used to improve ModAcc measurement quality in presence of neighboring carriers. |

#### Attachments

None

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__modacc__multi__carrier__filter_1ga9b26c5184034faec2638d546bb632860.html language=enus -->
## TOPIC 00089: RFMXCDMA2K_ATTR_MODACC_MULTI_CARRIER_FILTER_ENABLED

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__modacc__multi__carrier__filter_1ga9b26c5184034faec2638d546bb632860.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__modacc__multi__carrier__filter_1ga9b26c5184034faec2638d546bb632860.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the multi carrier filter which can be used to improve ModAcc measurement quality in presence of neighboring carriers. SyntaxRFMXCDMA2K_ATTR_MODACC_MULTI_CARRIER_FILTER_ENABLEDNumeric ValueData TypeAccessApplies To6361104int32Read/WriteN/ARemarks You do not need to use a s

### RFMXCDMA2K_ATTR_MODACC_MULTI_CARRIER_FILTER_ENABLED

Specifies whether to enable the multi carrier filter which can be used to improve ModAcc measurement quality in presence of neighboring carriers.

#### Syntax

RFMXCDMA2K_ATTR_MODACC_MULTI_CARRIER_FILTER_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6361104 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **False**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXCDMA2K_VAL_MODACC_MULTI_CARRIER_FILTER_ENABLED_FALSE | 0 (0x0) | Disables multi carrier filter for ModAcc measurement. |
| RFMXCDMA2K_VAL_MODACC_MULTI_CARRIER_FILTER_ENABLED_TRUE | 1 (0x1) | Enables multi carrier filter for ModAcc measurement. |

Parent topic:

Multi Carrier Filter

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__modacc__results_1ga1240b4a2212fcecc1113af77b61bcd5d.html language=enus -->
## TOPIC 00090: RFMXCDMA2K_ATTR_MODACC_RESULTS_RMS_MAGNITUDE_ERROR

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__modacc__results_1ga1240b4a2212fcecc1113af77b61bcd5d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__modacc__results_1ga1240b4a2212fcecc1113af77b61bcd5d.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the RMS magnitude error of the composite signal. This value is expressed as a percentage. SyntaxRFMXCDMA2K_ATTR_MODACC_RESULTS_RMS_MAGNITUDE_ERRORNumeric ValueData TypeAccessApplies To6361122float64Read-OnlyN/ARemarks You do not need to use a selector string to read this result for the defau

### RFMXCDMA2K_ATTR_MODACC_RESULTS_RMS_MAGNITUDE_ERROR

Returns the RMS magnitude error of the composite signal. This value is expressed as a percentage.

#### Syntax

RFMXCDMA2K_ATTR_MODACC_RESULTS_RMS_MAGNITUDE_ERROR

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6361122 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and named results.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__modacc__results_1ga3216e163294dcfa3dad1bdd5cd69b424.html language=enus -->
## TOPIC 00091: RFMXCDMA2K_ATTR_MODACC_RESULTS_IQ_GAIN_IMBALANCE

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__modacc__results_1ga3216e163294dcfa3dad1bdd5cd69b424.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__modacc__results_1ga3216e163294dcfa3dad1bdd5cd69b424.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the I/Q gain imbalance of the composite signal averaged over all measured slots. This value is expressed in dB. SyntaxRFMXCDMA2K_ATTR_MODACC_RESULTS_IQ_GAIN_IMBALANCENumeric ValueData TypeAccessApplies To6361125float64Read-OnlyN/ARemarks You do not need to use a selector string to read this

### RFMXCDMA2K_ATTR_MODACC_RESULTS_IQ_GAIN_IMBALANCE

Returns the I/Q gain imbalance of the composite signal averaged over all measured slots. This value is expressed in dB.

#### Syntax

RFMXCDMA2K_ATTR_MODACC_RESULTS_IQ_GAIN_IMBALANCE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6361125 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and named results.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__modacc__results_1ga41249c7a638f5cc85d421e1d26e0a92c.html language=enus -->
## TOPIC 00092: RFMXCDMA2K_ATTR_MODACC_RESULTS_PEAK_CDE

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__modacc__results_1ga41249c7a638f5cc85d421e1d26e0a92c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__modacc__results_1ga41249c7a638f5cc85d421e1d26e0a92c.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum value among the code domain errors (CDEs). This value is expressed in dB. The CDEs are computed by projecting the descrambled error vector onto the code domain at a specific spreading factor. The CDE for every code with a specific spreading factor is defined as the ratio of the m

### RFMXCDMA2K_ATTR_MODACC_RESULTS_PEAK_CDE

Returns the maximum value among the code domain errors (CDEs). This value is expressed in dB. The CDEs are computed by projecting the descrambled error vector onto the code domain at a specific spreading factor. The CDE for every code with a specific spreading factor is defined as the ratio of the mean power of the projection onto that code to the mean power of the composite reference waveform. A fixed spreading factor of 16 is used. The CDEs are computed separately for I and Q branches.

#### Syntax

RFMXCDMA2K_ATTR_MODACC_RESULTS_PEAK_CDE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6361129 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and named results.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__modacc__results_1ga858e868c8a82d7aed67ae31978741ee1.html language=enus -->
## TOPIC 00093: RFMXCDMA2K_ATTR_MODACC_RESULTS_FREQUENCY_ERROR

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__modacc__results_1ga858e868c8a82d7aed67ae31978741ee1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__modacc__results_1ga858e868c8a82d7aed67ae31978741ee1.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the frequency error averaged over all measured slots. This value is expressed in Hz. SyntaxRFMXCDMA2K_ATTR_MODACC_RESULTS_FREQUENCY_ERRORNumeric ValueData TypeAccessApplies To6361127float64Read-OnlyN/ARemarks You do not need to use a selector string to read this result for the default signal

### RFMXCDMA2K_ATTR_MODACC_RESULTS_FREQUENCY_ERROR

Returns the frequency error averaged over all measured slots. This value is expressed in Hz.

#### Syntax

RFMXCDMA2K_ATTR_MODACC_RESULTS_FREQUENCY_ERROR

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6361127 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and named results.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__modacc__results_1ga8f0816f08d063c0b2c15739d4b2240ca.html language=enus -->
## TOPIC 00094: RFMXCDMA2K_ATTR_MODACC_RESULTS_PEAK_ACTIVE_CDE_WALSH_CODE_NUMBER

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__modacc__results_1ga8f0816f08d063c0b2c15739d4b2240ca.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__modacc__results_1ga8f0816f08d063c0b2c15739d4b2240ca.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the Walsh code number of the channel corresponding to the value that the RFMXCDMA2K_ATTR_MODACC_RESULTS_PEAK_ACTIVE_CDE attribute returns. SyntaxRFMXCDMA2K_ATTR_MODACC_RESULTS_PEAK_ACTIVE_CDE_WALSH_CODE_NUMBERNumeric ValueData TypeAccessApplies To6361135int32Read-OnlyN/ARemarks You do not ne

### RFMXCDMA2K_ATTR_MODACC_RESULTS_PEAK_ACTIVE_CDE_WALSH_CODE_NUMBER

Returns the Walsh code number of the channel corresponding to the value that the [RFMXCDMA2K_ATTR_MODACC_RESULTS_PEAK_ACTIVE_CDE](group____root__ni_r_fmx_c_d_m_a2k__attributes__modacc__results_1gab19f8c12e5a1f6c6d135d827b4338fff.html) attribute returns.

#### Syntax

RFMXCDMA2K_ATTR_MODACC_RESULTS_PEAK_ACTIVE_CDE_WALSH_CODE_NUMBER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6361135 | int32 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and named results.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__modacc__results_1gaa6e029e8f7f88d49135410dc730bd261.html language=enus -->
## TOPIC 00095: RFMXCDMA2K_ATTR_MODACC_RESULTS_CHIP_RATE_ERROR

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__modacc__results_1gaa6e029e8f7f88d49135410dc730bd261.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__modacc__results_1gaa6e029e8f7f88d49135410dc730bd261.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the chip rate error. This value is expressed in parts per million (ppm). SyntaxRFMXCDMA2K_ATTR_MODACC_RESULTS_CHIP_RATE_ERRORNumeric ValueData TypeAccessApplies To6361139float64Read-OnlyN/ARemarks You do not need to use a selector string to read this result for the default signal and result

### RFMXCDMA2K_ATTR_MODACC_RESULTS_CHIP_RATE_ERROR

Returns the chip rate error. This value is expressed in parts per million (ppm).

#### Syntax

RFMXCDMA2K_ATTR_MODACC_RESULTS_CHIP_RATE_ERROR

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6361139 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and named results.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__modacc__results_1gab604e44c7d98eb898a69a4f768c5d076.html language=enus -->
## TOPIC 00096: RFMXCDMA2K_ATTR_MODACC_RESULTS_IQ_QUADRATURE_ERROR

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__modacc__results_1gab604e44c7d98eb898a69a4f768c5d076.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__modacc__results_1gab604e44c7d98eb898a69a4f768c5d076.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the I/Q quadrature error of the composite signal, averaged over all measured slots. This value is expressed in degrees. SyntaxRFMXCDMA2K_ATTR_MODACC_RESULTS_IQ_QUADRATURE_ERRORNumeric ValueData TypeAccessApplies To6361126float64Read-OnlyN/ARemarks You do not need to use a selector string to

### RFMXCDMA2K_ATTR_MODACC_RESULTS_IQ_QUADRATURE_ERROR

Returns the I/Q quadrature error of the composite signal, averaged over all measured slots. This value is expressed in degrees.

#### Syntax

RFMXCDMA2K_ATTR_MODACC_RESULTS_IQ_QUADRATURE_ERROR

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6361126 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and named results.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__modacc__results_1gabda83a17cba3774d3ac70fc3ac88fd29.html language=enus -->
## TOPIC 00097: RFMXCDMA2K_ATTR_MODACC_RESULTS_IQ_ORIGIN_OFFSET

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__modacc__results_1gabda83a17cba3774d3ac70fc3ac88fd29.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__modacc__results_1gabda83a17cba3774d3ac70fc3ac88fd29.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the I/Q origin offset of the composite signal averaged over all measured slots. This value is expressed in dB. SyntaxRFMXCDMA2K_ATTR_MODACC_RESULTS_IQ_ORIGIN_OFFSETNumeric ValueData TypeAccessApplies To6361124float64Read-OnlyN/ARemarks You do not need to use a selector string to read this re

### RFMXCDMA2K_ATTR_MODACC_RESULTS_IQ_ORIGIN_OFFSET

Returns the I/Q origin offset of the composite signal averaged over all measured slots. This value is expressed in dB.

#### Syntax

RFMXCDMA2K_ATTR_MODACC_RESULTS_IQ_ORIGIN_OFFSET

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6361124 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and named results.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__modacc__results_1gac6233d849d9b75cf6daf691281e65b39.html language=enus -->
## TOPIC 00098: RFMXCDMA2K_ATTR_MODACC_RESULTS_RHO

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__modacc__results_1gac6233d849d9b75cf6daf691281e65b39.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__modacc__results_1gac6233d849d9b75cf6daf691281e65b39.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the correlation of the received signal with the reference signal normalized by the signal power. The value of Rho is between 0 and 1.0, inclusive. A value of 1.0 indicates that the received signal and the reference signal are perfectly correlated. SyntaxRFMXCDMA2K_ATTR_MODACC_RESULTS_RHONume

### RFMXCDMA2K_ATTR_MODACC_RESULTS_RHO

Returns the correlation of the received signal with the reference signal normalized by the signal power. The value of Rho is between 0 and 1.0, inclusive. A value of 1.0 indicates that the received signal and the reference signal are perfectly correlated.

#### Syntax

RFMXCDMA2K_ATTR_MODACC_RESULTS_RHO

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6361128 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and named results.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__modacc__results_1gac8e944a59ca8b08c052bb08f8fe69d99.html language=enus -->
## TOPIC 00099: RFMXCDMA2K_ATTR_MODACC_RESULTS_PEAK_CDE_BRANCH

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__modacc__results_1gac8e944a59ca8b08c052bb08f8fe69d99.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__modacc__results_1gac8e944a59ca8b08c052bb08f8fe69d99.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the branch corresponding to the value that the RFMXCDMA2K_ATTR_MODACC_RESULTS_PEAK_ACTIVE_CDE attribute returns. SyntaxRFMXCDMA2K_ATTR_MODACC_RESULTS_PEAK_CDE_BRANCHNumeric ValueData TypeAccessApplies To6361144int32Read-OnlyN/ARemarks You do not need to use a selector string to read this res

### RFMXCDMA2K_ATTR_MODACC_RESULTS_PEAK_CDE_BRANCH

Returns the branch corresponding to the value that the [RFMXCDMA2K_ATTR_MODACC_RESULTS_PEAK_ACTIVE_CDE](group____root__ni_r_fmx_c_d_m_a2k__attributes__modacc__results_1gab19f8c12e5a1f6c6d135d827b4338fff.html) attribute returns.

#### Syntax

RFMXCDMA2K_ATTR_MODACC_RESULTS_PEAK_CDE_BRANCH

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6361144 | int32 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and named results.

| Name | Value | Description |
| --- | --- | --- |
| RFMXCDMA2K_VAL_MODACC_PEAK_CDE_BRANCH_I | 0 (0x0) | The signal is modulated on the in-phase branch. |
| RFMXCDMA2K_VAL_MODACC_PEAK_CDE_BRANCH_Q | 1 (0x1) | The signal is modulated on the quadrature branch. |
| RFMXCDMA2K_VAL_MODACC_PEAK_CDE_BRANCH_I_AND_Q | 2 (0x2) | Complex modulated signal. |

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__modacc__results_1gaf34f74b35e91465d613ac3bc4046918e.html language=enus -->
## TOPIC 00100: RFMXCDMA2K_ATTR_MODACC_RESULTS_PEAK_EVM

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__modacc__results_1gaf34f74b35e91465d613ac3bc4046918e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__modacc__results_1gaf34f74b35e91465d613ac3bc4046918e.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the peak EVM of the composite signal. This value is expressed as a percentage. SyntaxRFMXCDMA2K_ATTR_MODACC_RESULTS_PEAK_EVMNumeric ValueData TypeAccessApplies To6361121float64Read-OnlyN/ARemarks You do not need to use a selector string to read this result for the default signal and result i

### RFMXCDMA2K_ATTR_MODACC_RESULTS_PEAK_EVM

Returns the peak EVM of the composite signal. This value is expressed as a percentage.

#### Syntax

RFMXCDMA2K_ATTR_MODACC_RESULTS_PEAK_EVM

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6361121 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and named results.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__modacc__results__detected__channel.html language=enus -->
## TOPIC 00101: Detected Channel

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__modacc__results__detected__channel.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__modacc__results__detected__channel.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXCDMA2K_ATTR_MODACC_RESULTS_DETECTED_BRANCHReturns the branch of the detected channel. If you set the RFMXCDMA2K_ATTR_CHANNEL_CONFIGURATION_MODE attribute to User Defined, the attribute returns the branch of the configured channel. RFMXCDMA2K_ATTR_MODACC_RESU

### Detected Channel

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXCDMA2K_ATTR_MODACC_RESULTS_DETECTED_BRANCH | Returns the branch of the detected channel. If you set the RFMXCDMA2K_ATTR_CHANNEL_CONFIGURATION_MODE attribute to User Defined, the attribute returns the branch of the configured channel. |
| RFMXCDMA2K_ATTR_MODACC_RESULTS_DETECTED_WALSH_CODE_LENGTH | Returns the Walsh code length of the detected channel. If you set the RFMXCDMA2K_ATTR_CHANNEL_CONFIGURATION_MODE attribute to User Defined, the attribute returns the Walsh code length of the configured channel. |
| RFMXCDMA2K_ATTR_MODACC_RESULTS_DETECTED_WALSH_CODE_NUMBER | Returns the Walsh code number of the detected channel. If you set the RFMXCDMA2K_ATTR_CHANNEL_CONFIGURATION_MODE attribute to User Defined, the attribute returns the Walsh code number of the configured channel. |
| RFMXCDMA2K_ATTR_MODACC_RESULTS_NUMBER_OF_DETECTED_CHANNELS | Returns the total number of detected channels. If you set the RFMXCDMA2K_ATTR_CHANNEL_CONFIGURATION_MODE attribute to User Defined, the attribute returns the number of configured channels. |

#### Attachments

None

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__modacc__results__detected__channel_1ga4921a48c0a224170fc765cd45331377a.html language=enus -->
## TOPIC 00102: RFMXCDMA2K_ATTR_MODACC_RESULTS_NUMBER_OF_DETECTED_CHANNELS

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__modacc__results__detected__channel_1ga4921a48c0a224170fc765cd45331377a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__modacc__results__detected__channel_1ga4921a48c0a224170fc765cd45331377a.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the total number of detected channels. If you set the RFMXCDMA2K_ATTR_CHANNEL_CONFIGURATION_MODE attribute to User Defined, the attribute returns the number of configured channels. SyntaxRFMXCDMA2K_ATTR_MODACC_RESULTS_NUMBER_OF_DETECTED_CHANNELSNumeric ValueData TypeAccessApplies To6361140in

### RFMXCDMA2K_ATTR_MODACC_RESULTS_NUMBER_OF_DETECTED_CHANNELS

Returns the total number of detected channels. If you set the [RFMXCDMA2K_ATTR_CHANNEL_CONFIGURATION_MODE](group____root__ni_r_fmx_c_d_m_a2k__attributes__channel_1ga3c88eb1dedd8333791a4fdde39fcdb76.html) attribute to **User Defined**, the attribute returns the number of configured channels.

#### Syntax

RFMXCDMA2K_ATTR_MODACC_RESULTS_NUMBER_OF_DETECTED_CHANNELS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6361140 | int32 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and named results.

Parent topic:

Detected Channel

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__modacc__results__detected__channel_1ga6291c8c3ff45145e1e7a1ee035b85e61.html language=enus -->
## TOPIC 00103: RFMXCDMA2K_ATTR_MODACC_RESULTS_DETECTED_WALSH_CODE_NUMBER

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__modacc__results__detected__channel_1ga6291c8c3ff45145e1e7a1ee035b85e61.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__modacc__results__detected__channel_1ga6291c8c3ff45145e1e7a1ee035b85e61.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the Walsh code number of the detected channel. If you set the RFMXCDMA2K_ATTR_CHANNEL_CONFIGURATION_MODE attribute to User Defined, the attribute returns the Walsh code number of the configured channel. SyntaxRFMXCDMA2K_ATTR_MODACC_RESULTS_DETECTED_WALSH_CODE_NUMBERNumeric ValueData TypeAcce

### RFMXCDMA2K_ATTR_MODACC_RESULTS_DETECTED_WALSH_CODE_NUMBER

Returns the Walsh code number of the detected channel. If you set the [RFMXCDMA2K_ATTR_CHANNEL_CONFIGURATION_MODE](group____root__ni_r_fmx_c_d_m_a2k__attributes__channel_1ga3c88eb1dedd8333791a4fdde39fcdb76.html) attribute to **User Defined**, the attribute returns the Walsh code number of the configured channel.

#### Syntax

RFMXCDMA2K_ATTR_MODACC_RESULTS_DETECTED_WALSH_CODE_NUMBER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6361142 | int32 | Read-Only | Channel |

#### Remarks

Use "channel< 
<format type="monospace-italic">n</format> 
>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this attribute.

Parent topic:

Detected Channel

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__modacc__results__detected__channel_1ga78e8b5202e307e2900c3d957a2af4f11.html language=enus -->
## TOPIC 00104: RFMXCDMA2K_ATTR_MODACC_RESULTS_DETECTED_BRANCH

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__modacc__results__detected__channel_1ga78e8b5202e307e2900c3d957a2af4f11.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__modacc__results__detected__channel_1ga78e8b5202e307e2900c3d957a2af4f11.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the branch of the detected channel. If you set the RFMXCDMA2K_ATTR_CHANNEL_CONFIGURATION_MODE attribute to User Defined, the attribute returns the branch of the configured channel. SyntaxRFMXCDMA2K_ATTR_MODACC_RESULTS_DETECTED_BRANCHNumeric ValueData TypeAccessApplies To6361143int32Read-Only

### RFMXCDMA2K_ATTR_MODACC_RESULTS_DETECTED_BRANCH

Returns the branch of the detected channel. If you set the [RFMXCDMA2K_ATTR_CHANNEL_CONFIGURATION_MODE](group____root__ni_r_fmx_c_d_m_a2k__attributes__channel_1ga3c88eb1dedd8333791a4fdde39fcdb76.html) attribute to **User Defined**, the attribute returns the branch of the configured channel.

#### Syntax

RFMXCDMA2K_ATTR_MODACC_RESULTS_DETECTED_BRANCH

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6361143 | int32 | Read-Only | Channel |

#### Remarks

Use "channel< 
<format type="monospace-italic">n</format> 
>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this attribute.

| Name | Value | Description |
| --- | --- | --- |
| RFMXCDMA2K_VAL_MODACC_DETECTED_BRANCH_I | 0 (0x0) | The signal modulated on the in-phase branch. |
| RFMXCDMA2K_VAL_MODACC_DETECTED_BRANCH_Q | 1 (0x1) | The signal modulated on the quadrature branch. |
| RFMXCDMA2K_VAL_MODACC_DETECTED_BRANCH_I_AND_Q | 2 (0x2) | The signal modulated on the in-phase branch and quadrature branch. |

Parent topic:

Detected Channel

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__modacc__results__detected__channel_1ga8ac46ab811421f5e85ea421cd919730c.html language=enus -->
## TOPIC 00105: RFMXCDMA2K_ATTR_MODACC_RESULTS_DETECTED_WALSH_CODE_LENGTH

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__modacc__results__detected__channel_1ga8ac46ab811421f5e85ea421cd919730c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__modacc__results__detected__channel_1ga8ac46ab811421f5e85ea421cd919730c.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the Walsh code length of the detected channel. If you set the RFMXCDMA2K_ATTR_CHANNEL_CONFIGURATION_MODE attribute to User Defined, the attribute returns the Walsh code length of the configured channel. SyntaxRFMXCDMA2K_ATTR_MODACC_RESULTS_DETECTED_WALSH_CODE_LENGTHNumeric ValueData TypeAcce

### RFMXCDMA2K_ATTR_MODACC_RESULTS_DETECTED_WALSH_CODE_LENGTH

Returns the Walsh code length of the detected channel. If you set the [RFMXCDMA2K_ATTR_CHANNEL_CONFIGURATION_MODE](group____root__ni_r_fmx_c_d_m_a2k__attributes__channel_1ga3c88eb1dedd8333791a4fdde39fcdb76.html) attribute to **User Defined**, the attribute returns the Walsh code length of the configured channel.

#### Syntax

RFMXCDMA2K_ATTR_MODACC_RESULTS_DETECTED_WALSH_CODE_LENGTH

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6361141 | int32 | Read-Only | Channel |

#### Remarks

Use "channel< 
<format type="monospace-italic">n</format> 
>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this attribute.

Parent topic:

Detected Channel

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__obw.html language=enus -->
## TOPIC 00106: OBW

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__obw.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__obw.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsAveragingRBW FilterResultsSweep TimeGroup membersNameDescriptionRFMXCDMA2K_ATTR_OBW_ALL_TRACES_ENABLEDSpecifies whether to enable the traces to be stored and retrieved after performing the OBW. RFMXCDMA2K_ATTR_OBW_MEASUREMENT_ENABLEDSpecifies whether to enable the OBW measurement. RFMXCDMA2K_A

### OBW

#### Groups

- Averaging
- RBW Filter
- Results
- Sweep Time

#### Group members

| Name | Description |
| --- | --- |
| RFMXCDMA2K_ATTR_OBW_ALL_TRACES_ENABLED | Specifies whether to enable the traces to be stored and retrieved after performing the OBW. |
| RFMXCDMA2K_ATTR_OBW_MEASUREMENT_ENABLED | Specifies whether to enable the OBW measurement. |
| RFMXCDMA2K_ATTR_OBW_NUMBER_OF_ANALYSIS_THREADS | Specifies the maximum number of threads used for parallelism for the OBW measurement. |
| RFMXCDMA2K_ATTR_OBW_SPAN | Returns the frequency span of the OBW measurement. This value is expressed in Hz. |

#### Attachments

None

Parent topic:

Attributes

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__obw_1ga18adb5528e1dcd687c8cd933a9bbee59.html language=enus -->
## TOPIC 00107: RFMXCDMA2K_ATTR_OBW_MEASUREMENT_ENABLED

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__obw_1ga18adb5528e1dcd687c8cd933a9bbee59.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__obw_1ga18adb5528e1dcd687c8cd933a9bbee59.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the OBW measurement. SyntaxRFMXCDMA2K_ATTR_OBW_MEASUREMENT_ENABLEDNumeric ValueData TypeAccessApplies To6316032int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Str

### RFMXCDMA2K_ATTR_OBW_MEASUREMENT_ENABLED

Specifies whether to enable the OBW measurement.

#### Syntax

RFMXCDMA2K_ATTR_OBW_MEASUREMENT_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6316032 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is FALSE.

Parent topic:

OBW

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__obw_1ga695355cd308bb0ca16d9395256967a58.html language=enus -->
## TOPIC 00108: RFMXCDMA2K_ATTR_OBW_ALL_TRACES_ENABLED

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__obw_1ga695355cd308bb0ca16d9395256967a58.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__obw_1ga695355cd308bb0ca16d9395256967a58.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the traces to be stored and retrieved after performing the OBW. SyntaxRFMXCDMA2K_ATTR_OBW_ALL_TRACES_ENABLEDNumeric ValueData TypeAccessApplies To6316050int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default

### RFMXCDMA2K_ATTR_OBW_ALL_TRACES_ENABLED

Specifies whether to enable the traces to be stored and retrieved after performing the OBW.

#### Syntax

RFMXCDMA2K_ATTR_OBW_ALL_TRACES_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6316050 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is FALSE.

Parent topic:

OBW

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__obw_1ga9287a25fd1ba9db3cfa614072eb7d658.html language=enus -->
## TOPIC 00109: RFMXCDMA2K_ATTR_OBW_NUMBER_OF_ANALYSIS_THREADS

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__obw_1ga9287a25fd1ba9db3cfa614072eb7d658.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__obw_1ga9287a25fd1ba9db3cfa614072eb7d658.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the maximum number of threads used for parallelism for the OBW measurement. SyntaxRFMXCDMA2K_ATTR_OBW_NUMBER_OF_ANALYSIS_THREADSNumeric ValueData TypeAccessApplies To6316035int32Read/WriteN/ARemarks The number of threads can range from 1 to the number of physical cores. The number of threa

### RFMXCDMA2K_ATTR_OBW_NUMBER_OF_ANALYSIS_THREADS

Specifies the maximum number of threads used for parallelism for the OBW measurement.

#### Syntax

RFMXCDMA2K_ATTR_OBW_NUMBER_OF_ANALYSIS_THREADS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6316035 | int32 | Read/Write | N/A |

#### Remarks

The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations.

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 1.

Parent topic:

OBW

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__obw_1gadfc3fbb04554ed129971b9e2d893ba00.html language=enus -->
## TOPIC 00110: RFMXCDMA2K_ATTR_OBW_SPAN

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__obw_1gadfc3fbb04554ed129971b9e2d893ba00.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__obw_1gadfc3fbb04554ed129971b9e2d893ba00.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the frequency span of the OBW measurement. This value is expressed in Hz. SyntaxRFMXCDMA2K_ATTR_OBW_SPANNumeric ValueData TypeAccessApplies To6316036float64Read-OnlyN/ARemarks You do not need to use a selector string to read this attribute for the default signal instance. Refer to the Select

### RFMXCDMA2K_ATTR_OBW_SPAN

Returns the frequency span of the OBW measurement. This value is expressed in Hz.

#### Syntax

RFMXCDMA2K_ATTR_OBW_SPAN

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6316036 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

Parent topic:

OBW

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__obw__averaging.html language=enus -->
## TOPIC 00111: Averaging

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__obw__averaging.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__obw__averaging.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXCDMA2K_ATTR_OBW_AVERAGING_COUNTSpecifies the number of acquisitions used for averaging when you set the RFMXCDMA2K_ATTR_OBW_AVERAGING_ENABLED attribute to True. RFMXCDMA2K_ATTR_OBW_AVERAGING_ENABLEDSpecifies whether to enable averaging for the OBW measuremen

### Averaging

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXCDMA2K_ATTR_OBW_AVERAGING_COUNT | Specifies the number of acquisitions used for averaging when you set the RFMXCDMA2K_ATTR_OBW_AVERAGING_ENABLED attribute to True. |
| RFMXCDMA2K_ATTR_OBW_AVERAGING_ENABLED | Specifies whether to enable averaging for the OBW measurement. |
| RFMXCDMA2K_ATTR_OBW_AVERAGING_TYPE | Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the OBW measurement. |

#### Attachments

None

Parent topic:

OBW

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__obw__averaging_1ga0d96929ebb03cbb0313fdfbc1a48bcbc.html language=enus -->
## TOPIC 00112: RFMXCDMA2K_ATTR_OBW_AVERAGING_COUNT

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__obw__averaging_1ga0d96929ebb03cbb0313fdfbc1a48bcbc.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__obw__averaging_1ga0d96929ebb03cbb0313fdfbc1a48bcbc.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of acquisitions used for averaging when you set the RFMXCDMA2K_ATTR_OBW_AVERAGING_ENABLED attribute to True. SyntaxRFMXCDMA2K_ATTR_OBW_AVERAGING_COUNTNumeric ValueData TypeAccessApplies To6316038int32Read/WriteN/ARemarks You do not need to use a selector string to configure or r

### RFMXCDMA2K_ATTR_OBW_AVERAGING_COUNT

Specifies the number of acquisitions used for averaging when you set the [RFMXCDMA2K_ATTR_OBW_AVERAGING_ENABLED](group____root__ni_r_fmx_c_d_m_a2k__attributes__obw__averaging_1ga6d782943ca47c2b6ecb647e7977fd1f5.html) attribute to **True**.

#### Syntax

RFMXCDMA2K_ATTR_OBW_AVERAGING_COUNT

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6316038 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 10.

Parent topic:

Averaging

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__obw__averaging_1ga5bb6740fe7f321f0b8be70ef31b1ef31.html language=enus -->
## TOPIC 00113: RFMXCDMA2K_ATTR_OBW_AVERAGING_TYPE

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__obw__averaging_1ga5bb6740fe7f321f0b8be70ef31b1ef31.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__obw__averaging_1ga5bb6740fe7f321f0b8be70ef31b1ef31.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the OBW measurement. SyntaxRFMXCDMA2K_ATTR_OBW_AVERAGING_TYPENumeric ValueData TypeAccessApplies To6316041int32Read/WriteN/ARemarks You do not need to use a selector string to configure or re

### RFMXCDMA2K_ATTR_OBW_AVERAGING_TYPE

Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the OBW measurement.

#### Syntax

RFMXCDMA2K_ATTR_OBW_AVERAGING_TYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6316041 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **RMS**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXCDMA2K_VAL_OBW_AVERAGING_TYPE_RMS | 0 (0x0) | The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. |
| RFMXCDMA2K_VAL_OBW_AVERAGING_TYPE_LOG | 1 (0x1) | The power spectrum is averaged in a logarithmic scale. |
| RFMXCDMA2K_VAL_OBW_AVERAGING_TYPE_SCALAR | 2 (0x2) | The square root of the power spectrum is averaged. |
| RFMXCDMA2K_VAL_OBW_AVERAGING_TYPE_MAXIMUM | 3 (0x3) | The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. |
| RFMXCDMA2K_VAL_OBW_AVERAGING_TYPE_MINIMUM | 4 (0x4) | The lowest power in the spectrum at each frequency bin is retained from one acquisition to the next. |

Parent topic:

Averaging

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__obw__averaging_1ga6d782943ca47c2b6ecb647e7977fd1f5.html language=enus -->
## TOPIC 00114: RFMXCDMA2K_ATTR_OBW_AVERAGING_ENABLED

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__obw__averaging_1ga6d782943ca47c2b6ecb647e7977fd1f5.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__obw__averaging_1ga6d782943ca47c2b6ecb647e7977fd1f5.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable averaging for the OBW measurement. SyntaxRFMXCDMA2K_ATTR_OBW_AVERAGING_ENABLEDNumeric ValueData TypeAccessApplies To6316039int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the

### RFMXCDMA2K_ATTR_OBW_AVERAGING_ENABLED

Specifies whether to enable averaging for the OBW measurement.

#### Syntax

RFMXCDMA2K_ATTR_OBW_AVERAGING_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6316039 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **False**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXCDMA2K_VAL_OBW_AVERAGING_ENABLED_FALSE | 0 (0x0) | The measurement is performed on a single acquisition. |
| RFMXCDMA2K_VAL_OBW_AVERAGING_ENABLED_TRUE | 1 (0x1) | The OBW measurement uses the value of the RFMXCDMA2K_ATTR_OBW_AVERAGING_COUNT attribute as the number of acquisitions over which the OBW measurement is averaged. |

Parent topic:

Averaging

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__obw__rbw__filter.html language=enus -->
## TOPIC 00115: RBW Filter

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__obw__rbw__filter.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__obw__rbw__filter.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXCDMA2K_ATTR_OBW_RBW_FILTER_AUTO_BANDWIDTHSpecifies whether the measurement computes the RBW. RFMXCDMA2K_ATTR_OBW_RBW_FILTER_BANDWIDTHSpecifies the bandwidth of the RBW filter used to sweep the acquired signal when you set the RFMXCDMA2K_ATTR_OBW_RBW_FILTER_A

### RBW Filter

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXCDMA2K_ATTR_OBW_RBW_FILTER_AUTO_BANDWIDTH | Specifies whether the measurement computes the RBW. |
| RFMXCDMA2K_ATTR_OBW_RBW_FILTER_BANDWIDTH | Specifies the bandwidth of the RBW filter used to sweep the acquired signal when you set the RFMXCDMA2K_ATTR_OBW_RBW_FILTER_AUTO_BANDWIDTH attribute to False. This value is expressed in Hz. |
| RFMXCDMA2K_ATTR_OBW_RBW_FILTER_TYPE | Specifies the shape of the digital RBW filter. |

#### Attachments

None

Parent topic:

OBW

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__obw__rbw__filter_1ga226fc1a392e1ff33d4f8bfd8157059e1.html language=enus -->
## TOPIC 00116: RFMXCDMA2K_ATTR_OBW_RBW_FILTER_AUTO_BANDWIDTH

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__obw__rbw__filter_1ga226fc1a392e1ff33d4f8bfd8157059e1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__obw__rbw__filter_1ga226fc1a392e1ff33d4f8bfd8157059e1.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement computes the RBW. SyntaxRFMXCDMA2K_ATTR_OBW_RBW_FILTER_AUTO_BANDWIDTHNumeric ValueData TypeAccessApplies To6316044int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Sel

### RFMXCDMA2K_ATTR_OBW_RBW_FILTER_AUTO_BANDWIDTH

Specifies whether the measurement computes the RBW.

#### Syntax

RFMXCDMA2K_ATTR_OBW_RBW_FILTER_AUTO_BANDWIDTH

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6316044 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **True**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXCDMA2K_VAL_OBW_RBW_AUTO_FALSE | 0 (0x0) | The measurement uses the RBW that you specify in the RFMXCDMA2K_ATTR_OBW_RBW_FILTER_BANDWIDTH attribute. |
| RFMXCDMA2K_VAL_OBW_RBW_AUTO_TRUE | 1 (0x1) | The measurement computes the RBW. |

Parent topic:

RBW Filter

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__obw__rbw__filter_1ga3a822f54d7ebc9f8f484cd93a162c05f.html language=enus -->
## TOPIC 00117: RFMXCDMA2K_ATTR_OBW_RBW_FILTER_TYPE

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__obw__rbw__filter_1ga3a822f54d7ebc9f8f484cd93a162c05f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__obw__rbw__filter_1ga3a822f54d7ebc9f8f484cd93a162c05f.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the shape of the digital RBW filter. SyntaxRFMXCDMA2K_ATTR_OBW_RBW_FILTER_TYPENumeric ValueData TypeAccessApplies To6316046int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector String to

### RFMXCDMA2K_ATTR_OBW_RBW_FILTER_TYPE

Specifies the shape of the digital RBW filter.

#### Syntax

RFMXCDMA2K_ATTR_OBW_RBW_FILTER_TYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6316046 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **Gaussian**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXCDMA2K_VAL_OBW_RBW_FILTER_TYPE_FFT_BASED | 0 (0x0) | No RBW filtering is performed. |
| RFMXCDMA2K_VAL_OBW_RBW_FILTER_TYPE_GAUSSIAN | 1 (0x1) | An RBW filter with a Gaussian response is applied. |
| RFMXCDMA2K_VAL_OBW_RBW_FILTER_TYPE_FLAT | 2 (0x2) | An RBW filter with a Flat response is applied. |

Parent topic:

RBW Filter

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__obw__rbw__filter_1gaa056c632a85b17ddb55d910f8e2eb7f2.html language=enus -->
## TOPIC 00118: RFMXCDMA2K_ATTR_OBW_RBW_FILTER_BANDWIDTH

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__obw__rbw__filter_1gaa056c632a85b17ddb55d910f8e2eb7f2.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__obw__rbw__filter_1gaa056c632a85b17ddb55d910f8e2eb7f2.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the bandwidth of the RBW filter used to sweep the acquired signal when you set the RFMXCDMA2K_ATTR_OBW_RBW_FILTER_AUTO_BANDWIDTH attribute to False. This value is expressed in Hz. SyntaxRFMXCDMA2K_ATTR_OBW_RBW_FILTER_BANDWIDTHNumeric ValueData TypeAccessApplies To6316045float64Read/WriteN/

### RFMXCDMA2K_ATTR_OBW_RBW_FILTER_BANDWIDTH

Specifies the bandwidth of the RBW filter used to sweep the acquired signal when you set the [RFMXCDMA2K_ATTR_OBW_RBW_FILTER_AUTO_BANDWIDTH](group____root__ni_r_fmx_c_d_m_a2k__attributes__obw__rbw__filter_1ga226fc1a392e1ff33d4f8bfd8157059e1.html) attribute to **False**. This value is expressed in Hz.

#### Syntax

RFMXCDMA2K_ATTR_OBW_RBW_FILTER_BANDWIDTH

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6316045 | float64 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 30 kHz.

Parent topic:

RBW Filter

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__obw__results.html language=enus -->
## TOPIC 00119: Results

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__obw__results.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__obw__results.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXCDMA2K_ATTR_OBW_RESULTS_ABSOLUTE_POWERReturns the absolute power measured in the OBW. This value is expressed in dBm. RFMXCDMA2K_ATTR_OBW_RESULTS_OCCUPIED_BANDWIDTHReturns the bandwidth that occupies 99% of the total signal power. This value is expressed in

### Results

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXCDMA2K_ATTR_OBW_RESULTS_ABSOLUTE_POWER | Returns the absolute power measured in the OBW. This value is expressed in dBm. |
| RFMXCDMA2K_ATTR_OBW_RESULTS_OCCUPIED_BANDWIDTH | Returns the bandwidth that occupies 99% of the total signal power. This value is expressed in Hz. |
| RFMXCDMA2K_ATTR_OBW_RESULTS_START_FREQUENCY | Returns the start frequency of the OBW. This value is expressed in Hz. |
| RFMXCDMA2K_ATTR_OBW_RESULTS_STOP_FREQUENCY | Returns the stop frequency of the OBW. This value is expressed in Hz. |

#### Attachments

None

Parent topic:

OBW

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__obw__results_1ga017522ebfbdb629522801c52447e63f8.html language=enus -->
## TOPIC 00120: RFMXCDMA2K_ATTR_OBW_RESULTS_ABSOLUTE_POWER

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__obw__results_1ga017522ebfbdb629522801c52447e63f8.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__obw__results_1ga017522ebfbdb629522801c52447e63f8.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the absolute power measured in the OBW. This value is expressed in dBm. SyntaxRFMXCDMA2K_ATTR_OBW_RESULTS_ABSOLUTE_POWERNumeric ValueData TypeAccessApplies To6316052float64Read-OnlyN/ARemarks You do not need to use a selector string to read this result for the default signal and result insta

### RFMXCDMA2K_ATTR_OBW_RESULTS_ABSOLUTE_POWER

Returns the absolute power measured in the OBW. This value is expressed in dBm.

#### Syntax

RFMXCDMA2K_ATTR_OBW_RESULTS_ABSOLUTE_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6316052 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and named results.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__obw__results_1ga8333142798a62a307e34a36208ba1aa2.html language=enus -->
## TOPIC 00121: RFMXCDMA2K_ATTR_OBW_RESULTS_START_FREQUENCY

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__obw__results_1ga8333142798a62a307e34a36208ba1aa2.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__obw__results_1ga8333142798a62a307e34a36208ba1aa2.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the start frequency of the OBW. This value is expressed in Hz. SyntaxRFMXCDMA2K_ATTR_OBW_RESULTS_START_FREQUENCYNumeric ValueData TypeAccessApplies To6316053float64Read-OnlyN/ARemarks The OBW is calculated using the following formula: OBW = Stop Frequency - Start FrequencyYou do not need to

### RFMXCDMA2K_ATTR_OBW_RESULTS_START_FREQUENCY

Returns the start frequency of the OBW. This value is expressed in Hz.

#### Syntax

RFMXCDMA2K_ATTR_OBW_RESULTS_START_FREQUENCY

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6316053 | float64 | Read-Only | N/A |

#### Remarks

The OBW is calculated using the following formula: *OBW = Stop Frequency - Start Frequency*

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and named results.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__obw__results_1gaaca357f93d3b0d87a5c85b56b2c9b84f.html language=enus -->
## TOPIC 00122: RFMXCDMA2K_ATTR_OBW_RESULTS_STOP_FREQUENCY

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__obw__results_1gaaca357f93d3b0d87a5c85b56b2c9b84f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__obw__results_1gaaca357f93d3b0d87a5c85b56b2c9b84f.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the stop frequency of the OBW. This value is expressed in Hz. SyntaxRFMXCDMA2K_ATTR_OBW_RESULTS_STOP_FREQUENCYNumeric ValueData TypeAccessApplies To6316054float64Read-OnlyN/ARemarks The OBW is calculated using the following formula: OBW = Stop Frequency - Start FrequencyYou do not need to us

### RFMXCDMA2K_ATTR_OBW_RESULTS_STOP_FREQUENCY

Returns the stop frequency of the OBW. This value is expressed in Hz.

#### Syntax

RFMXCDMA2K_ATTR_OBW_RESULTS_STOP_FREQUENCY

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6316054 | float64 | Read-Only | N/A |

#### Remarks

The OBW is calculated using the following formula: *OBW = Stop Frequency - Start Frequency*

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and named results.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__obw__results_1gac6dd5493db44349915c8490a8435de5b.html language=enus -->
## TOPIC 00123: RFMXCDMA2K_ATTR_OBW_RESULTS_OCCUPIED_BANDWIDTH

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__obw__results_1gac6dd5493db44349915c8490a8435de5b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__obw__results_1gac6dd5493db44349915c8490a8435de5b.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the bandwidth that occupies 99% of the total signal power. This value is expressed in Hz. SyntaxRFMXCDMA2K_ATTR_OBW_RESULTS_OCCUPIED_BANDWIDTHNumeric ValueData TypeAccessApplies To6316051float64Read-OnlyN/ARemarks You do not need to use a selector string to read this result for the default s

### RFMXCDMA2K_ATTR_OBW_RESULTS_OCCUPIED_BANDWIDTH

Returns the bandwidth that occupies 99% of the total signal power. This value is expressed in Hz.

#### Syntax

RFMXCDMA2K_ATTR_OBW_RESULTS_OCCUPIED_BANDWIDTH

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6316051 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and named results.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__obw__sweep__time.html language=enus -->
## TOPIC 00124: Sweep Time

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__obw__sweep__time.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__obw__sweep__time.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXCDMA2K_ATTR_OBW_SWEEP_TIME_AUTOSpecifies whether the measurement computes the sweep time. RFMXCDMA2K_ATTR_OBW_SWEEP_TIME_INTERVALSpecifies the sweep time when you set the RFMXCDMA2K_ATTR_OBW_SWEEP_TIME_AUTO attribute to False. This value is expressed in seco

### Sweep Time

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXCDMA2K_ATTR_OBW_SWEEP_TIME_AUTO | Specifies whether the measurement computes the sweep time. |
| RFMXCDMA2K_ATTR_OBW_SWEEP_TIME_INTERVAL | Specifies the sweep time when you set the RFMXCDMA2K_ATTR_OBW_SWEEP_TIME_AUTO attribute to False. This value is expressed in seconds. |

#### Attachments

None

Parent topic:

OBW

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__obw__sweep__time_1ga390b8305b55451a4cc268b87d3e20c34.html language=enus -->
## TOPIC 00125: RFMXCDMA2K_ATTR_OBW_SWEEP_TIME_INTERVAL

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__obw__sweep__time_1ga390b8305b55451a4cc268b87d3e20c34.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__obw__sweep__time_1ga390b8305b55451a4cc268b87d3e20c34.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the sweep time when you set the RFMXCDMA2K_ATTR_OBW_SWEEP_TIME_AUTO attribute to False. This value is expressed in seconds. SyntaxRFMXCDMA2K_ATTR_OBW_SWEEP_TIME_INTERVALNumeric ValueData TypeAccessApplies To6316048float64Read/WriteN/ARemarks You do not need to use a selector string to conf

### RFMXCDMA2K_ATTR_OBW_SWEEP_TIME_INTERVAL

Specifies the sweep time when you set the [RFMXCDMA2K_ATTR_OBW_SWEEP_TIME_AUTO](group____root__ni_r_fmx_c_d_m_a2k__attributes__obw__sweep__time_1ga3d6b9d030a0485734b81e8bd0f5f7de6.html) attribute to **False**. This value is expressed in seconds.

#### Syntax

RFMXCDMA2K_ATTR_OBW_SWEEP_TIME_INTERVAL

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6316048 | float64 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 0.001667 seconds.

Parent topic:

Sweep Time

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__obw__sweep__time_1ga3d6b9d030a0485734b81e8bd0f5f7de6.html language=enus -->
## TOPIC 00126: RFMXCDMA2K_ATTR_OBW_SWEEP_TIME_AUTO

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__obw__sweep__time_1ga3d6b9d030a0485734b81e8bd0f5f7de6.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__obw__sweep__time_1ga3d6b9d030a0485734b81e8bd0f5f7de6.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement computes the sweep time. SyntaxRFMXCDMA2K_ATTR_OBW_SWEEP_TIME_AUTONumeric ValueData TypeAccessApplies To6316047int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Select

### RFMXCDMA2K_ATTR_OBW_SWEEP_TIME_AUTO

Specifies whether the measurement computes the sweep time.

#### Syntax

RFMXCDMA2K_ATTR_OBW_SWEEP_TIME_AUTO

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6316047 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **True**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXCDMA2K_VAL_OBW_SWEEP_TIME_AUTO_FALSE | 0 (0x0) | The measurement uses the sweep time that you specify in the RFMXCDMA2K_ATTR_OBW_SWEEP_TIME_INTERVAL attribute. |
| RFMXCDMA2K_VAL_OBW_SWEEP_TIME_AUTO_TRUE | 1 (0x1) | The measurement uses the default sweep time of 0.001667 seconds. |

Parent topic:

Sweep Time

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__qevm.html language=enus -->
## TOPIC 00127: QEVM

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__qevm.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__qevm.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsAveragingResultsGroup membersNameDescriptionRFMXCDMA2K_ATTR_QEVM_ALL_TRACES_ENABLEDSpecifies whether to enable the traces to be stored and retrieved after performing the QEVM measurement. RFMXCDMA2K_ATTR_QEVM_IQ_GAIN_IMBALANCE_REMOVAL_ENABLEDSpecifies whether to remove I/Q gain imbalance befor

### QEVM

#### Groups

- Averaging
- Results

#### Group members

| Name | Description |
| --- | --- |
| RFMXCDMA2K_ATTR_QEVM_ALL_TRACES_ENABLED | Specifies whether to enable the traces to be stored and retrieved after performing the QEVM measurement. |
| RFMXCDMA2K_ATTR_QEVM_IQ_GAIN_IMBALANCE_REMOVAL_ENABLED | Specifies whether to remove I/Q gain imbalance before QEVM measurement. |
| RFMXCDMA2K_ATTR_QEVM_IQ_OFFSET_REMOVAL_ENABLED | Specifies whether to remove I/Q offset before QEVM measurement. |
| RFMXCDMA2K_ATTR_QEVM_IQ_QUADRATURE_ERROR_REMOVAL_ENABLED | Specifies whether to remove I/Q quadrature error before QEVM measurement. |
| RFMXCDMA2K_ATTR_QEVM_MEASUREMENT_ENABLED | Specifies whether to enable the QEVM measurement. |
| RFMXCDMA2K_ATTR_QEVM_MEASUREMENT_LENGTH | Specifies the number of chips used for a single measurement. |
| RFMXCDMA2K_ATTR_QEVM_NUMBER_OF_ANALYSIS_THREADS | Specifies the maximum number of threads used for parallelism for the QEVM measurement. |
| RFMXCDMA2K_ATTR_QEVM_RECEIVE_FILTER_ENABLED | Specifies whether to enable the received filter for the QEVM measurement. |
| RFMXCDMA2K_ATTR_QEVM_SPECTRUM_INVERTED | Specifies whether the spectrum of the signal is inverted. |

#### Attachments

None

Parent topic:

Attributes

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__qevm_1ga0a9855d94605aaf87da4f21903aa5887.html language=enus -->
## TOPIC 00128: RFMXCDMA2K_ATTR_QEVM_SPECTRUM_INVERTED

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__qevm_1ga0a9855d94605aaf87da4f21903aa5887.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__qevm_1ga0a9855d94605aaf87da4f21903aa5887.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the spectrum of the signal is inverted. SyntaxRFMXCDMA2K_ATTR_QEVM_SPECTRUM_INVERTEDNumeric ValueData TypeAccessApplies To6365189int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Sele

### RFMXCDMA2K_ATTR_QEVM_SPECTRUM_INVERTED

Specifies whether the spectrum of the signal is inverted.

#### Syntax

RFMXCDMA2K_ATTR_QEVM_SPECTRUM_INVERTED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6365189 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **False**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXCDMA2K_VAL_QEVM_SPECTRUM_INVERTED_FALSE | 0 (0x0) | The measurement spectrum is normal. |
| RFMXCDMA2K_VAL_QEVM_SPECTRUM_INVERTED_TRUE | 1 (0x1) | The measurement spectrum is inverted. |

Parent topic:

QEVM

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__qevm_1ga0ce48977490d26833a31656d75cc17e2.html language=enus -->
## TOPIC 00129: RFMXCDMA2K_ATTR_QEVM_ALL_TRACES_ENABLED

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__qevm_1ga0ce48977490d26833a31656d75cc17e2.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__qevm_1ga0ce48977490d26833a31656d75cc17e2.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the traces to be stored and retrieved after performing the QEVM measurement. SyntaxRFMXCDMA2K_ATTR_QEVM_ALL_TRACES_ENABLEDNumeric ValueData TypeAccessApplies To6365194int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute fo

### RFMXCDMA2K_ATTR_QEVM_ALL_TRACES_ENABLED

Specifies whether to enable the traces to be stored and retrieved after performing the QEVM measurement.

#### Syntax

RFMXCDMA2K_ATTR_QEVM_ALL_TRACES_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6365194 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is FALSE.

Parent topic:

QEVM

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__qevm_1ga300248def7fab6398b1f61dc8f33ecb7.html language=enus -->
## TOPIC 00130: RFMXCDMA2K_ATTR_QEVM_IQ_GAIN_IMBALANCE_REMOVAL_ENABLED

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__qevm_1ga300248def7fab6398b1f61dc8f33ecb7.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__qevm_1ga300248def7fab6398b1f61dc8f33ecb7.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to remove I/Q gain imbalance before QEVM measurement. SyntaxRFMXCDMA2K_ATTR_QEVM_IQ_GAIN_IMBALANCE_REMOVAL_ENABLEDNumeric ValueData TypeAccessApplies To6365191int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default sign

### RFMXCDMA2K_ATTR_QEVM_IQ_GAIN_IMBALANCE_REMOVAL_ENABLED

Specifies whether to remove I/Q gain imbalance before QEVM measurement.

#### Syntax

RFMXCDMA2K_ATTR_QEVM_IQ_GAIN_IMBALANCE_REMOVAL_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6365191 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **False**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXCDMA2K_VAL_QEVM_IQ_GAIN_IMBALANCE_REMOVAL_ENABLED_FALSE | 0 (0x0) | I/Q gain imbalance is not removed before the QEVM measurement. |
| RFMXCDMA2K_VAL_QEVM_IQ_GAIN_IMBALANCE_REMOVAL_ENABLED_TRUE | 1 (0x1) | I/Q gain imbalance is removed before the QEVM measurement. |

Parent topic:

QEVM

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__qevm_1ga30116fafa806de755f5d1653eac1a879.html language=enus -->
## TOPIC 00131: RFMXCDMA2K_ATTR_QEVM_MEASUREMENT_LENGTH

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__qevm_1ga30116fafa806de755f5d1653eac1a879.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__qevm_1ga30116fafa806de755f5d1653eac1a879.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of chips used for a single measurement. SyntaxRFMXCDMA2K_ATTR_QEVM_MEASUREMENT_LENGTHNumeric ValueData TypeAccessApplies To6365186int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the

### RFMXCDMA2K_ATTR_QEVM_MEASUREMENT_LENGTH

Specifies the number of chips used for a single measurement.

#### Syntax

RFMXCDMA2K_ATTR_QEVM_MEASUREMENT_LENGTH

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6365186 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 1536. The valid values are 700 to 2500, inclusive.

Parent topic:

QEVM

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__qevm_1ga4278858c28e94fb755a5c023f066c7fa.html language=enus -->
## TOPIC 00132: RFMXCDMA2K_ATTR_QEVM_RECEIVE_FILTER_ENABLED

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__qevm_1ga4278858c28e94fb755a5c023f066c7fa.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__qevm_1ga4278858c28e94fb755a5c023f066c7fa.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the received filter for the QEVM measurement. SyntaxRFMXCDMA2K_ATTR_QEVM_RECEIVE_FILTER_ENABLEDNumeric ValueData TypeAccessApplies To6365193int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instan

### RFMXCDMA2K_ATTR_QEVM_RECEIVE_FILTER_ENABLED

Specifies whether to enable the received filter for the QEVM measurement.

#### Syntax

RFMXCDMA2K_ATTR_QEVM_RECEIVE_FILTER_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6365193 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **True**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXCDMA2K_VAL_QEVM_RECEIVE_FILTER_ENABLED_FALSE | 0 (0x0) | Disables received filtering for the QEVM measurement. |
| RFMXCDMA2K_VAL_QEVM_RECEIVE_FILTER_ENABLED_TRUE | 1 (0x1) | Enables received filtering for the QEVM measurement. |

Parent topic:

QEVM

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__qevm_1ga6b852fd8738fa419029a84e0d1e13926.html language=enus -->
## TOPIC 00133: RFMXCDMA2K_ATTR_QEVM_NUMBER_OF_ANALYSIS_THREADS

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__qevm_1ga6b852fd8738fa419029a84e0d1e13926.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__qevm_1ga6b852fd8738fa419029a84e0d1e13926.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the maximum number of threads used for parallelism for the QEVM measurement. SyntaxRFMXCDMA2K_ATTR_QEVM_NUMBER_OF_ANALYSIS_THREADSNumeric ValueData TypeAccessApplies To6365195int32Read/WriteN/ARemarks The number of threads can range from 1 to the number of physical cores. The number of thr

### RFMXCDMA2K_ATTR_QEVM_NUMBER_OF_ANALYSIS_THREADS

Specifies the maximum number of threads used for parallelism for the QEVM measurement.

#### Syntax

RFMXCDMA2K_ATTR_QEVM_NUMBER_OF_ANALYSIS_THREADS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6365195 | int32 | Read/Write | N/A |

#### Remarks

The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations.

The default value is 1. Valid values range from 0 to 10, inclusive.

Parent topic:

QEVM

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__qevm_1ga81f287d502275b00834f7efe885ebe44.html language=enus -->
## TOPIC 00134: RFMXCDMA2K_ATTR_QEVM_IQ_OFFSET_REMOVAL_ENABLED

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__qevm_1ga81f287d502275b00834f7efe885ebe44.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__qevm_1ga81f287d502275b00834f7efe885ebe44.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to remove I/Q offset before QEVM measurement. SyntaxRFMXCDMA2K_ATTR_QEVM_IQ_OFFSET_REMOVAL_ENABLEDNumeric ValueData TypeAccessApplies To6365190int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Ref

### RFMXCDMA2K_ATTR_QEVM_IQ_OFFSET_REMOVAL_ENABLED

Specifies whether to remove I/Q offset before QEVM measurement.

#### Syntax

RFMXCDMA2K_ATTR_QEVM_IQ_OFFSET_REMOVAL_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6365190 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **False**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXCDMA2K_VAL_QEVM_IQ_OFFSET_REMOVAL_ENABLED_FALSE | 0 (0x0) | I/Q offset is not removed before the QEVM measurement. |
| RFMXCDMA2K_VAL_QEVM_IQ_OFFSET_REMOVAL_ENABLED_TRUE | 1 (0x1) | I/Q offset is removed before the QEVM measurement. |

Parent topic:

QEVM

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__qevm_1ga982651b0a933414def324f5393558bd7.html language=enus -->
## TOPIC 00135: RFMXCDMA2K_ATTR_QEVM_IQ_QUADRATURE_ERROR_REMOVAL_ENABLED

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__qevm_1ga982651b0a933414def324f5393558bd7.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__qevm_1ga982651b0a933414def324f5393558bd7.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to remove I/Q quadrature error before QEVM measurement. SyntaxRFMXCDMA2K_ATTR_QEVM_IQ_QUADRATURE_ERROR_REMOVAL_ENABLEDNumeric ValueData TypeAccessApplies To6365192int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default

### RFMXCDMA2K_ATTR_QEVM_IQ_QUADRATURE_ERROR_REMOVAL_ENABLED

Specifies whether to remove I/Q quadrature error before QEVM measurement.

#### Syntax

RFMXCDMA2K_ATTR_QEVM_IQ_QUADRATURE_ERROR_REMOVAL_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6365192 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **False**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXCDMA2K_VAL_QEVM_IQ_QUADRATURE_ERROR_REMOVAL_ENABLED_FALSE | 0 (0x0) | I/Q quadrature error is not removed before the QEVM measurement. |
| RFMXCDMA2K_VAL_QEVM_IQ_QUADRATURE_ERROR_REMOVAL_ENABLED_TRUE | 1 (0x1) | I/Q quadrature error is removed before the QEVM measurement. |

Parent topic:

QEVM

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__qevm_1gafeb2b633ef64848dacfb365271329fe4.html language=enus -->
## TOPIC 00136: RFMXCDMA2K_ATTR_QEVM_MEASUREMENT_ENABLED

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__qevm_1gafeb2b633ef64848dacfb365271329fe4.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__qevm_1gafeb2b633ef64848dacfb365271329fe4.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the QEVM measurement. SyntaxRFMXCDMA2K_ATTR_QEVM_MEASUREMENT_ENABLEDNumeric ValueData TypeAccessApplies To6365184int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector S

### RFMXCDMA2K_ATTR_QEVM_MEASUREMENT_ENABLED

Specifies whether to enable the QEVM measurement.

#### Syntax

RFMXCDMA2K_ATTR_QEVM_MEASUREMENT_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6365184 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is FALSE.

Parent topic:

QEVM

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__qevm__averaging.html language=enus -->
## TOPIC 00137: Averaging

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__qevm__averaging.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__qevm__averaging.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXCDMA2K_ATTR_QEVM_AVERAGING_COUNTSpecifies the number of measurements used for averaging when you set the RFMXCDMA2K_ATTR_QEVM_AVERAGING_ENABLED attribute to True. RFMXCDMA2K_ATTR_QEVM_AVERAGING_ENABLEDSpecifies whether to enable averaging for the QEVM measur

### Averaging

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXCDMA2K_ATTR_QEVM_AVERAGING_COUNT | Specifies the number of measurements used for averaging when you set the RFMXCDMA2K_ATTR_QEVM_AVERAGING_ENABLED attribute to True. |
| RFMXCDMA2K_ATTR_QEVM_AVERAGING_ENABLED | Specifies whether to enable averaging for the QEVM measurement. |

#### Attachments

None

Parent topic:

QEVM

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__qevm__averaging_1ga6941be8a54fa25ac0dc9f10374f09100.html language=enus -->
## TOPIC 00138: RFMXCDMA2K_ATTR_QEVM_AVERAGING_ENABLED

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__qevm__averaging_1ga6941be8a54fa25ac0dc9f10374f09100.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__qevm__averaging_1ga6941be8a54fa25ac0dc9f10374f09100.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable averaging for the QEVM measurement. SyntaxRFMXCDMA2K_ATTR_QEVM_AVERAGING_ENABLEDNumeric ValueData TypeAccessApplies To6365187int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to th

### RFMXCDMA2K_ATTR_QEVM_AVERAGING_ENABLED

Specifies whether to enable averaging for the QEVM measurement.

#### Syntax

RFMXCDMA2K_ATTR_QEVM_AVERAGING_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6365187 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **False**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXCDMA2K_VAL_QEVM_AVERAGING_ENABLED_FALSE | 0 (0x0) | The averaging is disabled for the measurement. |
| RFMXCDMA2K_VAL_QEVM_AVERAGING_ENABLED_TRUE | 1 (0x1) | The averaging is enabled for the measurement. |

Parent topic:

Averaging

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__qevm__averaging_1ga84235707dd7d604744dd6881a6b13698.html language=enus -->
## TOPIC 00139: RFMXCDMA2K_ATTR_QEVM_AVERAGING_COUNT

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__qevm__averaging_1ga84235707dd7d604744dd6881a6b13698.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__qevm__averaging_1ga84235707dd7d604744dd6881a6b13698.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of measurements used for averaging when you set the RFMXCDMA2K_ATTR_QEVM_AVERAGING_ENABLED attribute to True. SyntaxRFMXCDMA2K_ATTR_QEVM_AVERAGING_COUNTNumeric ValueData TypeAccessApplies To6365188int32Read/WriteN/ARemarks You do not need to use a selector string to configure or

### RFMXCDMA2K_ATTR_QEVM_AVERAGING_COUNT

Specifies the number of measurements used for averaging when you set the [RFMXCDMA2K_ATTR_QEVM_AVERAGING_ENABLED](group____root__ni_r_fmx_c_d_m_a2k__attributes__qevm__averaging_1ga6941be8a54fa25ac0dc9f10374f09100.html) attribute to **True**.

#### Syntax

RFMXCDMA2K_ATTR_QEVM_AVERAGING_COUNT

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6365188 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default values is 10. The valid values are 1 to 10000, inclusive.

Parent topic:

Averaging

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__qevm__results.html language=enus -->
## TOPIC 00140: Results

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__qevm__results.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__qevm__results.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXCDMA2K_ATTR_QEVM_RESULTS_MAXIMUM_CHIP_RATE_ERRORReturns the maximum chip rate error. This value is expressed in parts per million (ppm). RFMXCDMA2K_ATTR_QEVM_RESULTS_MAXIMUM_FREQUENCY_ERRORReturns the maximum frequency error of the received signal. This valu

### Results

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXCDMA2K_ATTR_QEVM_RESULTS_MAXIMUM_CHIP_RATE_ERROR | Returns the maximum chip rate error. This value is expressed in parts per million (ppm). |
| RFMXCDMA2K_ATTR_QEVM_RESULTS_MAXIMUM_FREQUENCY_ERROR | Returns the maximum frequency error of the received signal. This value is expressed in Hz. |
| RFMXCDMA2K_ATTR_QEVM_RESULTS_MAXIMUM_IQ_GAIN_IMBALANCE | Returns the maximum I/Q gain imbalance of the received signal. This value is expressed in dB. |
| RFMXCDMA2K_ATTR_QEVM_RESULTS_MAXIMUM_IQ_ORIGIN_OFFSET | Returns the maximum origin offset of the received signal. This value is expressed in dB. |
| RFMXCDMA2K_ATTR_QEVM_RESULTS_MAXIMUM_IQ_QUADRATURE_ERROR | Returns the maximum I/Q quadrature error (phase imbalance) of the received signal. This value is expressed in degrees. |
| RFMXCDMA2K_ATTR_QEVM_RESULTS_MAXIMUM_MAGNITUDE_ERROR | Returns the maximum magnitude error of the received signal. This value is expressed as a percentage. |
| RFMXCDMA2K_ATTR_QEVM_RESULTS_MAXIMUM_PEAK_EVM | Returns the maximum peak EVM of the received signal. This value is expressed as a percentage. |
| RFMXCDMA2K_ATTR_QEVM_RESULTS_MAXIMUM_PHASE_ERROR | Returns the maximum phase error of the received signal. This value is expressed in degrees. |
| RFMXCDMA2K_ATTR_QEVM_RESULTS_MAXIMUM_RMS_EVM | Returns the maximum RMS EVM of the received signal. This value is expressed as a percentage. |
| RFMXCDMA2K_ATTR_QEVM_RESULTS_MEAN_CHIP_RATE_ERROR | Returns the mean chip rate error. This value is expressed in parts per million (ppm). |
| RFMXCDMA2K_ATTR_QEVM_RESULTS_MEAN_FREQUENCY_ERROR | Returns the mean averaged frequency error of the received signal. This value is expressed in Hz. |
| RFMXCDMA2K_ATTR_QEVM_RESULTS_MEAN_IQ_GAIN_IMBALANCE | Returns the mean I/Q gain imbalance of the received signal. This value is expressed in dB. |
| RFMXCDMA2K_ATTR_QEVM_RESULTS_MEAN_IQ_ORIGIN_OFFSET | Returns the mean averaged origin offset of the received signal. This value is expressed in dB. |
| RFMXCDMA2K_ATTR_QEVM_RESULTS_MEAN_IQ_QUADRATURE_ERROR | Returns the mean I/Q quadrature error (phase imbalance) of the received signal. This value is expressed in degrees. |
| RFMXCDMA2K_ATTR_QEVM_RESULTS_MEAN_MAGNITUDE_ERROR | Returns the mean averaged magnitude error of the received signal. This value is expressed as a percentage. |
| RFMXCDMA2K_ATTR_QEVM_RESULTS_MEAN_PEAK_EVM | Returns the mean averaged peak EVM of the received signal. This value is expressed as a percentage. |
| RFMXCDMA2K_ATTR_QEVM_RESULTS_MEAN_PHASE_ERROR | Returns the mean averaged phase error of the received signal. This value is expressed in degrees. |
| RFMXCDMA2K_ATTR_QEVM_RESULTS_MEAN_RMS_EVM | Returns the mean averaged RMS EVM of the received signal. This value is expressed as a percentage. |

#### Attachments

None

Parent topic:

QEVM

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__qevm__results_1ga02e20821ad3e798ea994b80dbcfebfab.html language=enus -->
## TOPIC 00141: RFMXCDMA2K_ATTR_QEVM_RESULTS_MEAN_MAGNITUDE_ERROR

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__qevm__results_1ga02e20821ad3e798ea994b80dbcfebfab.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__qevm__results_1ga02e20821ad3e798ea994b80dbcfebfab.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean averaged magnitude error of the received signal. This value is expressed as a percentage. SyntaxRFMXCDMA2K_ATTR_QEVM_RESULTS_MEAN_MAGNITUDE_ERRORNumeric ValueData TypeAccessApplies To6365201float64Read-OnlyN/ARemarks You do not need to use a selector string to read this attribute fo

### RFMXCDMA2K_ATTR_QEVM_RESULTS_MEAN_MAGNITUDE_ERROR

Returns the mean averaged magnitude error of the received signal. This value is expressed as a percentage.

#### Syntax

RFMXCDMA2K_ATTR_QEVM_RESULTS_MEAN_MAGNITUDE_ERROR

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6365201 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this attribute for the default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__qevm__results_1ga055a68a1a299402633dae47ed8c05660.html language=enus -->
## TOPIC 00142: RFMXCDMA2K_ATTR_QEVM_RESULTS_MAXIMUM_PHASE_ERROR

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__qevm__results_1ga055a68a1a299402633dae47ed8c05660.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__qevm__results_1ga055a68a1a299402633dae47ed8c05660.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum phase error of the received signal. This value is expressed in degrees. SyntaxRFMXCDMA2K_ATTR_QEVM_RESULTS_MAXIMUM_PHASE_ERRORNumeric ValueData TypeAccessApplies To6365204float64Read-OnlyN/ARemarks You do not need to use a selector string to read this attribute for the default si

### RFMXCDMA2K_ATTR_QEVM_RESULTS_MAXIMUM_PHASE_ERROR

Returns the maximum phase error of the received signal. This value is expressed in degrees.

#### Syntax

RFMXCDMA2K_ATTR_QEVM_RESULTS_MAXIMUM_PHASE_ERROR

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6365204 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this attribute for the default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__qevm__results_1ga3438c49715e7c9ef6b9d444a13e87fa5.html language=enus -->
## TOPIC 00143: RFMXCDMA2K_ATTR_QEVM_RESULTS_MEAN_PEAK_EVM

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__qevm__results_1ga3438c49715e7c9ef6b9d444a13e87fa5.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__qevm__results_1ga3438c49715e7c9ef6b9d444a13e87fa5.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean averaged peak EVM of the received signal. This value is expressed as a percentage. SyntaxRFMXCDMA2K_ATTR_QEVM_RESULTS_MEAN_PEAK_EVMNumeric ValueData TypeAccessApplies To6365199float64Read-OnlyN/ARemarks You do not need to use a selector string to read this attribute for the default

### RFMXCDMA2K_ATTR_QEVM_RESULTS_MEAN_PEAK_EVM

Returns the mean averaged peak EVM of the received signal. This value is expressed as a percentage.

#### Syntax

RFMXCDMA2K_ATTR_QEVM_RESULTS_MEAN_PEAK_EVM

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6365199 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this attribute for the default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__qevm__results_1ga3473b63ba81c95b8c29d20a8369e8f51.html language=enus -->
## TOPIC 00144: RFMXCDMA2K_ATTR_QEVM_RESULTS_MAXIMUM_IQ_QUADRATURE_ERROR

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__qevm__results_1ga3473b63ba81c95b8c29d20a8369e8f51.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__qevm__results_1ga3473b63ba81c95b8c29d20a8369e8f51.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum I/Q quadrature error (phase imbalance) of the received signal. This value is expressed in degrees. SyntaxRFMXCDMA2K_ATTR_QEVM_RESULTS_MAXIMUM_IQ_QUADRATURE_ERRORNumeric ValueData TypeAccessApplies To6365212float64Read-OnlyN/ARemarks You do not need to use a selector string to rea

### RFMXCDMA2K_ATTR_QEVM_RESULTS_MAXIMUM_IQ_QUADRATURE_ERROR

Returns the maximum I/Q quadrature error (phase imbalance) of the received signal. This value is expressed in degrees.

#### Syntax

RFMXCDMA2K_ATTR_QEVM_RESULTS_MAXIMUM_IQ_QUADRATURE_ERROR

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6365212 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this attribute for the default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__qevm__results_1ga35418cee9211f78919bbfce266132374.html language=enus -->
## TOPIC 00145: RFMXCDMA2K_ATTR_QEVM_RESULTS_MEAN_PHASE_ERROR

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__qevm__results_1ga35418cee9211f78919bbfce266132374.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__qevm__results_1ga35418cee9211f78919bbfce266132374.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean averaged phase error of the received signal. This value is expressed in degrees. SyntaxRFMXCDMA2K_ATTR_QEVM_RESULTS_MEAN_PHASE_ERRORNumeric ValueData TypeAccessApplies To6365203float64Read-OnlyN/ARemarks You do not need to use a selector string to read this attribute for the default

### RFMXCDMA2K_ATTR_QEVM_RESULTS_MEAN_PHASE_ERROR

Returns the mean averaged phase error of the received signal. This value is expressed in degrees.

#### Syntax

RFMXCDMA2K_ATTR_QEVM_RESULTS_MEAN_PHASE_ERROR

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6365203 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this attribute for the default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html)s topic for information about the string syntax for named signals.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__qevm__results_1ga380bbb22813e09eedbfce02d24934380.html language=enus -->
## TOPIC 00146: RFMXCDMA2K_ATTR_QEVM_RESULTS_MEAN_IQ_ORIGIN_OFFSET

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__qevm__results_1ga380bbb22813e09eedbfce02d24934380.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__qevm__results_1ga380bbb22813e09eedbfce02d24934380.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean averaged origin offset of the received signal. This value is expressed in dB. SyntaxRFMXCDMA2K_ATTR_QEVM_RESULTS_MEAN_IQ_ORIGIN_OFFSETNumeric ValueData TypeAccessApplies To6365207float64Read-OnlyN/ARemarks You do not need to use a selector string to read this attribute for the defau

### RFMXCDMA2K_ATTR_QEVM_RESULTS_MEAN_IQ_ORIGIN_OFFSET

Returns the mean averaged origin offset of the received signal. This value is expressed in dB.

#### Syntax

RFMXCDMA2K_ATTR_QEVM_RESULTS_MEAN_IQ_ORIGIN_OFFSET

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6365207 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this attribute for the default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__qevm__results_1ga518a9c3e298ba02d03c8c3a5d68bb098.html language=enus -->
## TOPIC 00147: RFMXCDMA2K_ATTR_QEVM_RESULTS_MAXIMUM_IQ_GAIN_IMBALANCE

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__qevm__results_1ga518a9c3e298ba02d03c8c3a5d68bb098.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__qevm__results_1ga518a9c3e298ba02d03c8c3a5d68bb098.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum I/Q gain imbalance of the received signal. This value is expressed in dB. SyntaxRFMXCDMA2K_ATTR_QEVM_RESULTS_MAXIMUM_IQ_GAIN_IMBALANCENumeric ValueData TypeAccessApplies To6365210float64Read-OnlyN/ARemarks You do not need to use a selector string to read this attribute for the de

### RFMXCDMA2K_ATTR_QEVM_RESULTS_MAXIMUM_IQ_GAIN_IMBALANCE

Returns the maximum I/Q gain imbalance of the received signal. This value is expressed in dB.

#### Syntax

RFMXCDMA2K_ATTR_QEVM_RESULTS_MAXIMUM_IQ_GAIN_IMBALANCE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6365210 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this attribute for the default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__qevm__results_1ga53558c135c1d54f12f352ccf01efcacc.html language=enus -->
## TOPIC 00148: RFMXCDMA2K_ATTR_QEVM_RESULTS_MAXIMUM_MAGNITUDE_ERROR

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__qevm__results_1ga53558c135c1d54f12f352ccf01efcacc.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__qevm__results_1ga53558c135c1d54f12f352ccf01efcacc.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum magnitude error of the received signal. This value is expressed as a percentage. SyntaxRFMXCDMA2K_ATTR_QEVM_RESULTS_MAXIMUM_MAGNITUDE_ERRORNumeric ValueData TypeAccessApplies To6365202float64Read-OnlyN/ARemarks You do not need to use a selector string to read this attribute for t

### RFMXCDMA2K_ATTR_QEVM_RESULTS_MAXIMUM_MAGNITUDE_ERROR

Returns the maximum magnitude error of the received signal. This value is expressed as a percentage.

#### Syntax

RFMXCDMA2K_ATTR_QEVM_RESULTS_MAXIMUM_MAGNITUDE_ERROR

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6365202 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this attribute for the default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__qevm__results_1ga5a76a5fa470627e4c3fb691a398f342e.html language=enus -->
## TOPIC 00149: RFMXCDMA2K_ATTR_QEVM_RESULTS_MEAN_CHIP_RATE_ERROR

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__qevm__results_1ga5a76a5fa470627e4c3fb691a398f342e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__qevm__results_1ga5a76a5fa470627e4c3fb691a398f342e.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean chip rate error. This value is expressed in parts per million (ppm). SyntaxRFMXCDMA2K_ATTR_QEVM_RESULTS_MEAN_CHIP_RATE_ERRORNumeric ValueData TypeAccessApplies To6365213float64Read-OnlyN/ARemarks You do not need to use a selector string to read this attribute for the default signal

### RFMXCDMA2K_ATTR_QEVM_RESULTS_MEAN_CHIP_RATE_ERROR

Returns the mean chip rate error. This value is expressed in parts per million (ppm).

#### Syntax

RFMXCDMA2K_ATTR_QEVM_RESULTS_MEAN_CHIP_RATE_ERROR

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6365213 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this attribute for the default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__qevm__results_1ga5d88507a741d7aabe53e95118afe83de.html language=enus -->
## TOPIC 00150: RFMXCDMA2K_ATTR_QEVM_RESULTS_MEAN_IQ_GAIN_IMBALANCE

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__qevm__results_1ga5d88507a741d7aabe53e95118afe83de.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__qevm__results_1ga5d88507a741d7aabe53e95118afe83de.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean I/Q gain imbalance of the received signal. This value is expressed in dB. SyntaxRFMXCDMA2K_ATTR_QEVM_RESULTS_MEAN_IQ_GAIN_IMBALANCENumeric ValueData TypeAccessApplies To6365209float64Read-OnlyN/ARemarks You do not need to use a selector string to read this attribute for the default

### RFMXCDMA2K_ATTR_QEVM_RESULTS_MEAN_IQ_GAIN_IMBALANCE

Returns the mean I/Q gain imbalance of the received signal. This value is expressed in dB.

#### Syntax

RFMXCDMA2K_ATTR_QEVM_RESULTS_MEAN_IQ_GAIN_IMBALANCE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6365209 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this attribute for the default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__qevm__results_1ga6e3917403a420681d8eea040ed08fc9a.html language=enus -->
## TOPIC 00151: RFMXCDMA2K_ATTR_QEVM_RESULTS_MEAN_FREQUENCY_ERROR

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__qevm__results_1ga6e3917403a420681d8eea040ed08fc9a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__qevm__results_1ga6e3917403a420681d8eea040ed08fc9a.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean averaged frequency error of the received signal. This value is expressed in Hz. SyntaxRFMXCDMA2K_ATTR_QEVM_RESULTS_MEAN_FREQUENCY_ERRORNumeric ValueData TypeAccessApplies To6365205float64Read-OnlyN/ARemarks You do not need to use a selector string to read this attribute for the defa

### RFMXCDMA2K_ATTR_QEVM_RESULTS_MEAN_FREQUENCY_ERROR

Returns the mean averaged frequency error of the received signal. This value is expressed in Hz.

#### Syntax

RFMXCDMA2K_ATTR_QEVM_RESULTS_MEAN_FREQUENCY_ERROR

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6365205 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this attribute for the default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__qevm__results_1ga6fd710d4630f55e2666a701b1ac55bf3.html language=enus -->
## TOPIC 00152: RFMXCDMA2K_ATTR_QEVM_RESULTS_MEAN_IQ_QUADRATURE_ERROR

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__qevm__results_1ga6fd710d4630f55e2666a701b1ac55bf3.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__qevm__results_1ga6fd710d4630f55e2666a701b1ac55bf3.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean I/Q quadrature error (phase imbalance) of the received signal. This value is expressed in degrees. SyntaxRFMXCDMA2K_ATTR_QEVM_RESULTS_MEAN_IQ_QUADRATURE_ERRORNumeric ValueData TypeAccessApplies To6365211float64Read-OnlyN/ARemarks You do not need to use a selector string to read this

### RFMXCDMA2K_ATTR_QEVM_RESULTS_MEAN_IQ_QUADRATURE_ERROR

Returns the mean I/Q quadrature error (phase imbalance) of the received signal. This value is expressed in degrees.

#### Syntax

RFMXCDMA2K_ATTR_QEVM_RESULTS_MEAN_IQ_QUADRATURE_ERROR

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6365211 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this attribute for the default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__qevm__results_1ga8e53bcb190ce6d31c46000f91954cee7.html language=enus -->
## TOPIC 00153: RFMXCDMA2K_ATTR_QEVM_RESULTS_MAXIMUM_IQ_ORIGIN_OFFSET

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__qevm__results_1ga8e53bcb190ce6d31c46000f91954cee7.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__qevm__results_1ga8e53bcb190ce6d31c46000f91954cee7.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum origin offset of the received signal. This value is expressed in dB. SyntaxRFMXCDMA2K_ATTR_QEVM_RESULTS_MAXIMUM_IQ_ORIGIN_OFFSETNumeric ValueData TypeAccessApplies To6365208float64Read-OnlyN/ARemarks You do not need to use a selector string to read this attribute for the default

### RFMXCDMA2K_ATTR_QEVM_RESULTS_MAXIMUM_IQ_ORIGIN_OFFSET

Returns the maximum origin offset of the received signal. This value is expressed in dB.

#### Syntax

RFMXCDMA2K_ATTR_QEVM_RESULTS_MAXIMUM_IQ_ORIGIN_OFFSET

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6365208 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this attribute for the default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__qevm__results_1ga8f01a4511c476c849f7474c26ead7771.html language=enus -->
## TOPIC 00154: RFMXCDMA2K_ATTR_QEVM_RESULTS_MAXIMUM_CHIP_RATE_ERROR

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__qevm__results_1ga8f01a4511c476c849f7474c26ead7771.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__qevm__results_1ga8f01a4511c476c849f7474c26ead7771.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum chip rate error. This value is expressed in parts per million (ppm). SyntaxRFMXCDMA2K_ATTR_QEVM_RESULTS_MAXIMUM_CHIP_RATE_ERRORNumeric ValueData TypeAccessApplies To6365214float64Read-OnlyN/ARemarks You do not need to use a selector string to read this attribute for the default s

### RFMXCDMA2K_ATTR_QEVM_RESULTS_MAXIMUM_CHIP_RATE_ERROR

Returns the maximum chip rate error. This value is expressed in parts per million (ppm).

#### Syntax

RFMXCDMA2K_ATTR_QEVM_RESULTS_MAXIMUM_CHIP_RATE_ERROR

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6365214 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this attribute for the default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__sem.html language=enus -->
## TOPIC 00155: SEM

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__sem.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__sem.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsAveragingCarrierOffsetResultsSweep TimeGroup membersNameDescriptionRFMXCDMA2K_ATTR_SEM_ALL_TRACES_ENABLEDSpecifies whether to enable the traces to be stored and retrieved after performing the SEM measurement. RFMXCDMA2K_ATTR_SEM_MEASUREMENT_ENABLEDSpecifies whether to enable the SEM measuremen

### SEM

#### Groups

- Averaging
- Carrier
- Offset
- Results
- Sweep Time

#### Group members

| Name | Description |
| --- | --- |
| RFMXCDMA2K_ATTR_SEM_ALL_TRACES_ENABLED | Specifies whether to enable the traces to be stored and retrieved after performing the SEM measurement. |
| RFMXCDMA2K_ATTR_SEM_MEASUREMENT_ENABLED | Specifies whether to enable the SEM measurement. |
| RFMXCDMA2K_ATTR_SEM_NUMBER_OF_ANALYSIS_THREADS | Specifies the maximum number of threads used for parallelism for the SEM measurement. |

#### Attachments

None

Parent topic:

Attributes

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__sem_1ga1c9b8381838342b379856fb329154518.html language=enus -->
## TOPIC 00156: RFMXCDMA2K_ATTR_SEM_ALL_TRACES_ENABLED

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__sem_1ga1c9b8381838342b379856fb329154518.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__sem_1ga1c9b8381838342b379856fb329154518.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the traces to be stored and retrieved after performing the SEM measurement. SyntaxRFMXCDMA2K_ATTR_SEM_ALL_TRACES_ENABLEDNumeric ValueData TypeAccessApplies To6324263int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for

### RFMXCDMA2K_ATTR_SEM_ALL_TRACES_ENABLED

Specifies whether to enable the traces to be stored and retrieved after performing the SEM measurement.

#### Syntax

RFMXCDMA2K_ATTR_SEM_ALL_TRACES_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6324263 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is FALSE.

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__sem_1ga3fb1fbd58ff55b24b5c751945701d7c5.html language=enus -->
## TOPIC 00157: RFMXCDMA2K_ATTR_SEM_NUMBER_OF_ANALYSIS_THREADS

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__sem_1ga3fb1fbd58ff55b24b5c751945701d7c5.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__sem_1ga3fb1fbd58ff55b24b5c751945701d7c5.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the maximum number of threads used for parallelism for the SEM measurement. SyntaxRFMXCDMA2K_ATTR_SEM_NUMBER_OF_ANALYSIS_THREADSNumeric ValueData TypeAccessApplies To6324253int32Read/WriteN/ARemarks The number of threads can range from 1 to the number of physical cores. The number of threa

### RFMXCDMA2K_ATTR_SEM_NUMBER_OF_ANALYSIS_THREADS

Specifies the maximum number of threads used for parallelism for the SEM measurement.

#### Syntax

RFMXCDMA2K_ATTR_SEM_NUMBER_OF_ANALYSIS_THREADS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6324253 | int32 | Read/Write | N/A |

#### Remarks

The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations.

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 1.

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__sem__averaging.html language=enus -->
## TOPIC 00158: Averaging

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__sem__averaging.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__sem__averaging.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXCDMA2K_ATTR_SEM_AVERAGING_COUNTSpecifies the number of acquisitions used for averaging when you set the RFMXCDMA2K_ATTR_SEM_AVERAGING_ENABLED attribute to True. RFMXCDMA2K_ATTR_SEM_AVERAGING_ENABLEDSpecifies whether to enable averaging for the SEM measuremen

### Averaging

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXCDMA2K_ATTR_SEM_AVERAGING_COUNT | Specifies the number of acquisitions used for averaging when you set the RFMXCDMA2K_ATTR_SEM_AVERAGING_ENABLED attribute to True. |
| RFMXCDMA2K_ATTR_SEM_AVERAGING_ENABLED | Specifies whether to enable averaging for the SEM measurement. |
| RFMXCDMA2K_ATTR_SEM_AVERAGING_TYPE | Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the SEM measurement. |

#### Attachments

None

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__sem__averaging_1ga328213598ac728bdf691df4e35b627c4.html language=enus -->
## TOPIC 00159: RFMXCDMA2K_ATTR_SEM_AVERAGING_ENABLED

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__sem__averaging_1ga328213598ac728bdf691df4e35b627c4.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__sem__averaging_1ga328213598ac728bdf691df4e35b627c4.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable averaging for the SEM measurement. SyntaxRFMXCDMA2K_ATTR_SEM_AVERAGING_ENABLEDNumeric ValueData TypeAccessApplies To6324255int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the

### RFMXCDMA2K_ATTR_SEM_AVERAGING_ENABLED

Specifies whether to enable averaging for the SEM measurement.

#### Syntax

RFMXCDMA2K_ATTR_SEM_AVERAGING_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6324255 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **False**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXCDMA2K_VAL_SEM_AVERAGING_ENABLED_FALSE | 0 (0x0) | The measurement is performed on a single acquisition. |
| RFMXCDMA2K_VAL_SEM_AVERAGING_ENABLED_TRUE | 1 (0x1) | The SEM measurement uses the value of the RFMXCDMA2K_ATTR_SEM_AVERAGING_COUNT attribute as the number of acquisitions over which the SEM measurement is averaged. |

Parent topic:

Averaging

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__sem__averaging_1ga54491c92f8689b8c4550d0c89bc917a4.html language=enus -->
## TOPIC 00160: RFMXCDMA2K_ATTR_SEM_AVERAGING_TYPE

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__sem__averaging_1ga54491c92f8689b8c4550d0c89bc917a4.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__sem__averaging_1ga54491c92f8689b8c4550d0c89bc917a4.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the SEM measurement. SyntaxRFMXCDMA2K_ATTR_SEM_AVERAGING_TYPENumeric ValueData TypeAccessApplies To6324257int32Read/WriteN/ARemarks You do not need to use a selector string to configure or re

### RFMXCDMA2K_ATTR_SEM_AVERAGING_TYPE

Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the SEM measurement.

#### Syntax

RFMXCDMA2K_ATTR_SEM_AVERAGING_TYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6324257 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **RMS**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXCDMA2K_VAL_SEM_AVERAGING_TYPE_RMS | 0 (0x0) | The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. |
| RFMXCDMA2K_VAL_SEM_AVERAGING_TYPE_LOG | 1 (0x1) | The power spectrum is averaged in a logarithmic scale. |
| RFMXCDMA2K_VAL_SEM_AVERAGING_TYPE_SCALAR | 2 (0x2) | The square root of the power spectrum is averaged. |
| RFMXCDMA2K_VAL_SEM_AVERAGING_TYPE_MAXIMUM | 3 (0x3) | The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. |
| RFMXCDMA2K_VAL_SEM_AVERAGING_TYPE_MINIMUM | 4 (0x4) | The least power in the spectrum at each frequency bin is retained from one acquisition to the next. |

Parent topic:

Averaging

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__sem__carrier.html language=enus -->
## TOPIC 00161: Carrier

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__sem__carrier.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__sem__carrier.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXCDMA2K_ATTR_SEM_CARRIER_INTEGRATION_BANDWIDTHReturns the SEM carrier integration bandwidth. This value is expressed in Hz. AttachmentsNone

### Carrier

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXCDMA2K_ATTR_SEM_CARRIER_INTEGRATION_BANDWIDTH | Returns the SEM carrier integration bandwidth. This value is expressed in Hz. |

#### Attachments

None

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__sem__carrier_1ga4201e31163aaf51485e4d20915ac39ad.html language=enus -->
## TOPIC 00162: RFMXCDMA2K_ATTR_SEM_CARRIER_INTEGRATION_BANDWIDTH

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__sem__carrier_1ga4201e31163aaf51485e4d20915ac39ad.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__sem__carrier_1ga4201e31163aaf51485e4d20915ac39ad.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the SEM carrier integration bandwidth. This value is expressed in Hz. SyntaxRFMXCDMA2K_ATTR_SEM_CARRIER_INTEGRATION_BANDWIDTHNumeric ValueData TypeAccessApplies To6324229float64Read-OnlyN/ARemarks You do not need to use a selector string to read this attribute for the default signal instance

### RFMXCDMA2K_ATTR_SEM_CARRIER_INTEGRATION_BANDWIDTH

Returns the SEM carrier integration bandwidth. This value is expressed in Hz.

#### Syntax

RFMXCDMA2K_ATTR_SEM_CARRIER_INTEGRATION_BANDWIDTH

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6324229 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

Parent topic:

Carrier

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__sem__offset.html language=enus -->
## TOPIC 00163: Offset

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__sem__offset.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__sem__offset.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsRBW FilterGroup membersNameDescriptionRFMXCDMA2K_ATTR_SEM_NUMBER_OF_OFFSETSReturns the number of SEM offset segments. RFMXCDMA2K_ATTR_SEM_OFFSET_BANDWIDTH_INTEGRALReturns the bandwidth integral for a specific offset segment. RFMXCDMA2K_ATTR_SEM_OFFSET_START_FREQUENCYReturns the start frequency

### Offset

#### Groups

- RBW Filter

#### Group members

| Name | Description |
| --- | --- |
| RFMXCDMA2K_ATTR_SEM_NUMBER_OF_OFFSETS | Returns the number of SEM offset segments. |
| RFMXCDMA2K_ATTR_SEM_OFFSET_BANDWIDTH_INTEGRAL | Returns the bandwidth integral for a specific offset segment. |
| RFMXCDMA2K_ATTR_SEM_OFFSET_START_FREQUENCY | Returns the start frequency of an SEM offset segment relative to the carrier frequency. This value is expressed in Hz. |
| RFMXCDMA2K_ATTR_SEM_OFFSET_STOP_FREQUENCY | Returns the stop frequency of an SEM offset segment relative to the carrier frequency. This value is expressed in Hz. |

#### Attachments

None

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__sem__offset_1ga528c8652ccd2204b1f7ed420e3aa221b.html language=enus -->
## TOPIC 00164: RFMXCDMA2K_ATTR_SEM_OFFSET_STOP_FREQUENCY

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__sem__offset_1ga528c8652ccd2204b1f7ed420e3aa221b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__sem__offset_1ga528c8652ccd2204b1f7ed420e3aa221b.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the stop frequency of an SEM offset segment relative to the carrier frequency. This value is expressed in Hz. SyntaxRFMXCDMA2K_ATTR_SEM_OFFSET_STOP_FREQUENCYNumeric ValueData TypeAccessApplies To6324245float64Read-OnlyOffsetRemarks Use "offset< <format type="monospace-italic">n</format> >" a

### RFMXCDMA2K_ATTR_SEM_OFFSET_STOP_FREQUENCY

Returns the stop frequency of an SEM offset segment relative to the carrier frequency. This value is expressed in Hz.

#### Syntax

RFMXCDMA2K_ATTR_SEM_OFFSET_STOP_FREQUENCY

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6324245 | float64 | Read-Only | Offset |

#### Remarks

Use "offset< 
<format type="monospace-italic">n</format> 
>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result.

Parent topic:

Offset

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__sem__offset_1gaad5b5cba04b2340f1e48c0ff4ee4afe5.html language=enus -->
## TOPIC 00165: RFMXCDMA2K_ATTR_SEM_OFFSET_START_FREQUENCY

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__sem__offset_1gaad5b5cba04b2340f1e48c0ff4ee4afe5.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__sem__offset_1gaad5b5cba04b2340f1e48c0ff4ee4afe5.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the start frequency of an SEM offset segment relative to the carrier frequency. This value is expressed in Hz. SyntaxRFMXCDMA2K_ATTR_SEM_OFFSET_START_FREQUENCYNumeric ValueData TypeAccessApplies To6324244float64Read-OnlyOffsetRemarks Use "offset< <format type="monospace-italic">n</format> >"

### RFMXCDMA2K_ATTR_SEM_OFFSET_START_FREQUENCY

Returns the start frequency of an SEM offset segment relative to the carrier frequency. This value is expressed in Hz.

#### Syntax

RFMXCDMA2K_ATTR_SEM_OFFSET_START_FREQUENCY

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6324244 | float64 | Read-Only | Offset |

#### Remarks

Use "offset< 
<format type="monospace-italic">n</format> 
>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result.

Parent topic:

Offset

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__sem__offset_1gae82feacc5719f873886bfe799949e69e.html language=enus -->
## TOPIC 00166: RFMXCDMA2K_ATTR_SEM_OFFSET_BANDWIDTH_INTEGRAL

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__sem__offset_1gae82feacc5719f873886bfe799949e69e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__sem__offset_1gae82feacc5719f873886bfe799949e69e.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the bandwidth integral for a specific offset segment. SyntaxRFMXCDMA2K_ATTR_SEM_OFFSET_BANDWIDTH_INTEGRALNumeric ValueData TypeAccessApplies To6324236int32Read-OnlyOffsetRemarks A bandwidth integral greater than 1 indicates a RBW filter of a narrower bandwidth is used for the offset segment

### RFMXCDMA2K_ATTR_SEM_OFFSET_BANDWIDTH_INTEGRAL

Returns the bandwidth integral for a specific offset segment.

#### Syntax

RFMXCDMA2K_ATTR_SEM_OFFSET_BANDWIDTH_INTEGRAL

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6324236 | int32 | Read-Only | Offset |

#### Remarks

A bandwidth integral greater than 1 indicates a RBW filter of a narrower bandwidth is used for the offset segment measurement, and digital processing is used to achieve the RBW defined for the offset segment.

Use the following equation to calculate the value of the offset segment RBW: *offset segment RBW* = *RBW* * *BW integral*

Use "offset< 
<format type="monospace-italic">n</format> 
>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result.

Parent topic:

Offset

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__sem__results.html language=enus -->
## TOPIC 00167: Results

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__sem__results.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__sem__results.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsCarrierLower OffsetUpper OffsetGroup membersNameDescriptionRFMXCDMA2K_ATTR_SEM_RESULTS_MEASUREMENT_STATUSIndicates the overall measurement status based on the measurement limits, which are specified by the standard for each offset segment. AttachmentsNone

### Results

#### Groups

- Carrier
- Lower Offset
- Upper Offset

#### Group members

| Name | Description |
| --- | --- |
| RFMXCDMA2K_ATTR_SEM_RESULTS_MEASUREMENT_STATUS | Indicates the overall measurement status based on the measurement limits, which are specified by the standard for each offset segment. |

#### Attachments

None

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__sem__results__carrier.html language=enus -->
## TOPIC 00168: Carrier

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__sem__results__carrier.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__sem__results__carrier.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXCDMA2K_ATTR_SEM_RESULTS_CARRIER_ABSOLUTE_INTEGRATED_POWERReturns the carrier power. The carrier power is the power centered at the center frequency and integrated over the carrier bandwidth of 1.23 MHz. This value is expressed in dBm. AttachmentsNone

### Carrier

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXCDMA2K_ATTR_SEM_RESULTS_CARRIER_ABSOLUTE_INTEGRATED_POWER | Returns the carrier power. The carrier power is the power centered at the center frequency and integrated over the carrier bandwidth of 1.23 MHz. This value is expressed in dBm. |

#### Attachments

None

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__sem__results__carrier_1ga4423940bd99c695c25dab95c66e14c33.html language=enus -->
## TOPIC 00169: RFMXCDMA2K_ATTR_SEM_RESULTS_CARRIER_ABSOLUTE_INTEGRATED_POWER

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__sem__results__carrier_1ga4423940bd99c695c25dab95c66e14c33.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__sem__results__carrier_1ga4423940bd99c695c25dab95c66e14c33.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the carrier power. The carrier power is the power centered at the center frequency and integrated over the carrier bandwidth of 1.23 MHz. This value is expressed in dBm. SyntaxRFMXCDMA2K_ATTR_SEM_RESULTS_CARRIER_ABSOLUTE_INTEGRATED_POWERNumeric ValueData TypeAccessApplies To6324269float64Rea

### RFMXCDMA2K_ATTR_SEM_RESULTS_CARRIER_ABSOLUTE_INTEGRATED_POWER

Returns the carrier power. The carrier power is the power centered at the center frequency and integrated over the carrier bandwidth of 1.23 MHz. This value is expressed in dBm.

#### Syntax

RFMXCDMA2K_ATTR_SEM_RESULTS_CARRIER_ABSOLUTE_INTEGRATED_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6324269 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and named results.

Parent topic:

Carrier

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__sem__results__lower__offset.html language=enus -->
## TOPIC 00170: Lower Offset

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__sem__results__lower__offset.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__sem__results__lower__offset.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXCDMA2K_ATTR_SEM_RESULTS_LOWER_OFFSET_ABSOLUTE_INTEGRATED_POWERReturns the absolute power measured in the lower (negative) offset segment. This value is expressed in dBm. RFMXCDMA2K_ATTR_SEM_RESULTS_LOWER_OFFSET_ABSOLUTE_PEAK_POWERReturns the peak power measu

### Lower Offset

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXCDMA2K_ATTR_SEM_RESULTS_LOWER_OFFSET_ABSOLUTE_INTEGRATED_POWER | Returns the absolute power measured in the lower (negative) offset segment. This value is expressed in dBm. |
| RFMXCDMA2K_ATTR_SEM_RESULTS_LOWER_OFFSET_ABSOLUTE_PEAK_POWER | Returns the peak power measured in the lower (negative) offset segment. This value is expressed in dBm. |
| RFMXCDMA2K_ATTR_SEM_RESULTS_LOWER_OFFSET_MARGIN | Returns the margin from the limit mask value specified by the standard. This value is expressed in dB. Margin is defined as the minimum difference between the spectrum and the closest limit mask, which can be absolute or relative. |
| RFMXCDMA2K_ATTR_SEM_RESULTS_LOWER_OFFSET_MARGIN_ABSOLUTE_POWER | Returns the absolute power at which the margin occurred in the lower (negative) offset segment. This value is expressed in dBm. |
| RFMXCDMA2K_ATTR_SEM_RESULTS_LOWER_OFFSET_MARGIN_FREQUENCY | Returns the frequency at which the margin occurred in the lower (negative) offset segment. This value is expressed in Hz. |
| RFMXCDMA2K_ATTR_SEM_RESULTS_LOWER_OFFSET_MARGIN_RELATIVE_POWER | Returns the power at which the margin occurred in the lower (negative) offset segment relative to the carrier absolute integrated power. This value is expressed in dB. |
| RFMXCDMA2K_ATTR_SEM_RESULTS_LOWER_OFFSET_MEASUREMENT_STATUS | Indicates the lower offset segment measurement status based on measurement limits specified by the standard. |
| RFMXCDMA2K_ATTR_SEM_RESULTS_LOWER_OFFSET_PEAK_FREQUENCY | Returns the frequency at which the peak power occurred in the lower offset segment. This value is expressed in Hz. |
| RFMXCDMA2K_ATTR_SEM_RESULTS_LOWER_OFFSET_RELATIVE_INTEGRATED_POWER | Returns the power measured in the lower (negative) offset segment relative to the carrier absolute integrated power. This value is expressed in dB. |
| RFMXCDMA2K_ATTR_SEM_RESULTS_LOWER_OFFSET_RELATIVE_PEAK_POWER | Returns the peak power measured in the lower (negative) offset segment relative to the carrier absolute integrated power. This value is expressed in dB. |

#### Attachments

None

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__sem__results__lower__offset_1ga43c7c0092b5f0ccbe435d0fa30b14dbc.html language=enus -->
## TOPIC 00171: RFMXCDMA2K_ATTR_SEM_RESULTS_LOWER_OFFSET_RELATIVE_INTEGRATED_POWER

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__sem__results__lower__offset_1ga43c7c0092b5f0ccbe435d0fa30b14dbc.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__sem__results__lower__offset_1ga43c7c0092b5f0ccbe435d0fa30b14dbc.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the power measured in the lower (negative) offset segment relative to the carrier absolute integrated power. This value is expressed in dB. SyntaxRFMXCDMA2K_ATTR_SEM_RESULTS_LOWER_OFFSET_RELATIVE_INTEGRATED_POWERNumeric ValueData TypeAccessApplies To6324277float64Read-OnlyOffsetRemarks Use "

### RFMXCDMA2K_ATTR_SEM_RESULTS_LOWER_OFFSET_RELATIVE_INTEGRATED_POWER

Returns the power measured in the lower (negative) offset segment relative to the carrier absolute integrated power. This value is expressed in dB.

#### Syntax

RFMXCDMA2K_ATTR_SEM_RESULTS_LOWER_OFFSET_RELATIVE_INTEGRATED_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6324277 | float64 | Read-Only | Offset |

#### Remarks

Use "offset< 
<format type="monospace-italic">n</format> 
>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result.

Parent topic:

Lower Offset

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__sem__results__lower__offset_1ga72519fc965e408b18b29430e211116d0.html language=enus -->
## TOPIC 00172: RFMXCDMA2K_ATTR_SEM_RESULTS_LOWER_OFFSET_MARGIN_FREQUENCY

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__sem__results__lower__offset_1ga72519fc965e408b18b29430e211116d0.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__sem__results__lower__offset_1ga72519fc965e408b18b29430e211116d0.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the frequency at which the margin occurred in the lower (negative) offset segment. This value is expressed in Hz. SyntaxRFMXCDMA2K_ATTR_SEM_RESULTS_LOWER_OFFSET_MARGIN_FREQUENCYNumeric ValueData TypeAccessApplies To6324284float64Read-OnlyOffsetRemarks Use "offset< <format type="monospace-ita

### RFMXCDMA2K_ATTR_SEM_RESULTS_LOWER_OFFSET_MARGIN_FREQUENCY

Returns the frequency at which the margin occurred in the lower (negative) offset segment. This value is expressed in Hz.

#### Syntax

RFMXCDMA2K_ATTR_SEM_RESULTS_LOWER_OFFSET_MARGIN_FREQUENCY

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6324284 | float64 | Read-Only | Offset |

#### Remarks

Use "offset< 
<format type="monospace-italic">n</format> 
>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result.

Parent topic:

Lower Offset

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__sem__results__lower__offset_1ga799b681b7fc82f829f436cf6798f2a6b.html language=enus -->
## TOPIC 00173: RFMXCDMA2K_ATTR_SEM_RESULTS_LOWER_OFFSET_RELATIVE_PEAK_POWER

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__sem__results__lower__offset_1ga799b681b7fc82f829f436cf6798f2a6b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__sem__results__lower__offset_1ga799b681b7fc82f829f436cf6798f2a6b.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the peak power measured in the lower (negative) offset segment relative to the carrier absolute integrated power. This value is expressed in dB. SyntaxRFMXCDMA2K_ATTR_SEM_RESULTS_LOWER_OFFSET_RELATIVE_PEAK_POWERNumeric ValueData TypeAccessApplies To6324279float64Read-OnlyOffsetRemarks Use "o

### RFMXCDMA2K_ATTR_SEM_RESULTS_LOWER_OFFSET_RELATIVE_PEAK_POWER

Returns the peak power measured in the lower (negative) offset segment relative to the carrier absolute integrated power. This value is expressed in dB.

#### Syntax

RFMXCDMA2K_ATTR_SEM_RESULTS_LOWER_OFFSET_RELATIVE_PEAK_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6324279 | float64 | Read-Only | Offset |

#### Remarks

Use "offset< 
<format type="monospace-italic">n</format> 
>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result.

Parent topic:

Lower Offset

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__sem__results__lower__offset_1ga94f8742cb84af11a286ea2570be56f56.html language=enus -->
## TOPIC 00174: RFMXCDMA2K_ATTR_SEM_RESULTS_LOWER_OFFSET_PEAK_FREQUENCY

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__sem__results__lower__offset_1ga94f8742cb84af11a286ea2570be56f56.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__sem__results__lower__offset_1ga94f8742cb84af11a286ea2570be56f56.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the frequency at which the peak power occurred in the lower offset segment. This value is expressed in Hz. SyntaxRFMXCDMA2K_ATTR_SEM_RESULTS_LOWER_OFFSET_PEAK_FREQUENCYNumeric ValueData TypeAccessApplies To6324280float64Read-OnlyOffsetRemarks Use "offset< <format type="monospace-italic">n</f

### RFMXCDMA2K_ATTR_SEM_RESULTS_LOWER_OFFSET_PEAK_FREQUENCY

Returns the frequency at which the peak power occurred in the lower offset segment. This value is expressed in Hz.

#### Syntax

RFMXCDMA2K_ATTR_SEM_RESULTS_LOWER_OFFSET_PEAK_FREQUENCY

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6324280 | float64 | Read-Only | Offset |

#### Remarks

Use "offset< 
<format type="monospace-italic">n</format> 
>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result.

Parent topic:

Lower Offset

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__sem__results__lower__offset_1ga9a56daa8936b03d0305fec9a60cfb02a.html language=enus -->
## TOPIC 00175: RFMXCDMA2K_ATTR_SEM_RESULTS_LOWER_OFFSET_ABSOLUTE_INTEGRATED_POWER

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__sem__results__lower__offset_1ga9a56daa8936b03d0305fec9a60cfb02a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__sem__results__lower__offset_1ga9a56daa8936b03d0305fec9a60cfb02a.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the absolute power measured in the lower (negative) offset segment. This value is expressed in dBm. SyntaxRFMXCDMA2K_ATTR_SEM_RESULTS_LOWER_OFFSET_ABSOLUTE_INTEGRATED_POWERNumeric ValueData TypeAccessApplies To6324276float64Read-OnlyOffsetRemarks Use "offset< <format type="monospace-italic">

### RFMXCDMA2K_ATTR_SEM_RESULTS_LOWER_OFFSET_ABSOLUTE_INTEGRATED_POWER

Returns the absolute power measured in the lower (negative) offset segment. This value is expressed in dBm.

#### Syntax

RFMXCDMA2K_ATTR_SEM_RESULTS_LOWER_OFFSET_ABSOLUTE_INTEGRATED_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6324276 | float64 | Read-Only | Offset |

#### Remarks

Use "offset< 
<format type="monospace-italic">n</format> 
>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result.

Parent topic:

Lower Offset

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__sem__results__upper__offset_1ga40591e8b50b1f0cc88cf81f17e83119d.html language=enus -->
## TOPIC 00176: RFMXCDMA2K_ATTR_SEM_RESULTS_UPPER_OFFSET_MARGIN_FREQUENCY

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__sem__results__upper__offset_1ga40591e8b50b1f0cc88cf81f17e83119d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__sem__results__upper__offset_1ga40591e8b50b1f0cc88cf81f17e83119d.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the frequency at which the margin occurred in the upper (positive) offset. This value is expressed in Hz. SyntaxRFMXCDMA2K_ATTR_SEM_RESULTS_UPPER_OFFSET_MARGIN_FREQUENCYNumeric ValueData TypeAccessApplies To6324297float64Read-OnlyOffsetRemarks Use "offset< <format type="monospace-italic">n</

### RFMXCDMA2K_ATTR_SEM_RESULTS_UPPER_OFFSET_MARGIN_FREQUENCY

Returns the frequency at which the margin occurred in the upper (positive) offset. This value is expressed in Hz.

#### Syntax

RFMXCDMA2K_ATTR_SEM_RESULTS_UPPER_OFFSET_MARGIN_FREQUENCY

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6324297 | float64 | Read-Only | Offset |

#### Remarks

Use "offset< 
<format type="monospace-italic">n</format> 
>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result.

Parent topic:

Upper Offset

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__sem__results__upper__offset_1ga55b1d2ef31135c9c0357d7dd1ba51f11.html language=enus -->
## TOPIC 00177: RFMXCDMA2K_ATTR_SEM_RESULTS_UPPER_OFFSET_RELATIVE_PEAK_POWER

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__sem__results__upper__offset_1ga55b1d2ef31135c9c0357d7dd1ba51f11.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__sem__results__upper__offset_1ga55b1d2ef31135c9c0357d7dd1ba51f11.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the peak power measured in the upper (positive) offset segment relative to the carrier absolute integrated power. This value is expressed in dB. SyntaxRFMXCDMA2K_ATTR_SEM_RESULTS_UPPER_OFFSET_RELATIVE_PEAK_POWERNumeric ValueData TypeAccessApplies To6324292float64Read-OnlyOffsetRemarks Use "o

### RFMXCDMA2K_ATTR_SEM_RESULTS_UPPER_OFFSET_RELATIVE_PEAK_POWER

Returns the peak power measured in the upper (positive) offset segment relative to the carrier absolute integrated power. This value is expressed in dB.

#### Syntax

RFMXCDMA2K_ATTR_SEM_RESULTS_UPPER_OFFSET_RELATIVE_PEAK_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6324292 | float64 | Read-Only | Offset |

#### Remarks

Use "offset< 
<format type="monospace-italic">n</format> 
>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result.

Parent topic:

Upper Offset

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__sem__results__upper__offset_1ga8eb64461100150b2056880206dad9158.html language=enus -->
## TOPIC 00178: RFMXCDMA2K_ATTR_SEM_RESULTS_UPPER_OFFSET_ABSOLUTE_PEAK_POWER

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__sem__results__upper__offset_1ga8eb64461100150b2056880206dad9158.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__sem__results__upper__offset_1ga8eb64461100150b2056880206dad9158.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the peak power measured in the upper (positive) offset segment. This value is expressed in dBm. SyntaxRFMXCDMA2K_ATTR_SEM_RESULTS_UPPER_OFFSET_ABSOLUTE_PEAK_POWERNumeric ValueData TypeAccessApplies To6324291float64Read-OnlyOffsetRemarks Use "offset< <format type="monospace-italic">n</format>

### RFMXCDMA2K_ATTR_SEM_RESULTS_UPPER_OFFSET_ABSOLUTE_PEAK_POWER

Returns the peak power measured in the upper (positive) offset segment. This value is expressed in dBm.

#### Syntax

RFMXCDMA2K_ATTR_SEM_RESULTS_UPPER_OFFSET_ABSOLUTE_PEAK_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6324291 | float64 | Read-Only | Offset |

#### Remarks

Use "offset< 
<format type="monospace-italic">n</format> 
>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result.

Parent topic:

Upper Offset

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__sem__results__upper__offset_1gaf61960a4b4c0bc3afae3c8fd8f0f71f4.html language=enus -->
## TOPIC 00179: RFMXCDMA2K_ATTR_SEM_RESULTS_UPPER_OFFSET_RELATIVE_INTEGRATED_POWER

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__sem__results__upper__offset_1gaf61960a4b4c0bc3afae3c8fd8f0f71f4.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__sem__results__upper__offset_1gaf61960a4b4c0bc3afae3c8fd8f0f71f4.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the power measured in the upper (positive) offset segment relative to the carrier absolute integrated power. This value is expressed in dB. SyntaxRFMXCDMA2K_ATTR_SEM_RESULTS_UPPER_OFFSET_RELATIVE_INTEGRATED_POWERNumeric ValueData TypeAccessApplies To6324290float64Read-OnlyOffsetRemarks Use "

### RFMXCDMA2K_ATTR_SEM_RESULTS_UPPER_OFFSET_RELATIVE_INTEGRATED_POWER

Returns the power measured in the upper (positive) offset segment relative to the carrier absolute integrated power. This value is expressed in dB.

#### Syntax

RFMXCDMA2K_ATTR_SEM_RESULTS_UPPER_OFFSET_RELATIVE_INTEGRATED_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6324290 | float64 | Read-Only | Offset |

#### Remarks

Use "offset< 
<format type="monospace-italic">n</format> 
>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result.

Parent topic:

Upper Offset

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__sem__sweep__time_1ga04b670943106110d0522c3d59cc9a1ed.html language=enus -->
## TOPIC 00180: RFMXCDMA2K_ATTR_SEM_SWEEP_TIME_AUTO

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__sem__sweep__time_1ga04b670943106110d0522c3d59cc9a1ed.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__sem__sweep__time_1ga04b670943106110d0522c3d59cc9a1ed.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement computes the sweep time. SyntaxRFMXCDMA2K_ATTR_SEM_SWEEP_TIME_AUTONumeric ValueData TypeAccessApplies To6324261int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Select

### RFMXCDMA2K_ATTR_SEM_SWEEP_TIME_AUTO

Specifies whether the measurement computes the sweep time.

#### Syntax

RFMXCDMA2K_ATTR_SEM_SWEEP_TIME_AUTO

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6324261 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **True**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXCDMA2K_VAL_SEM_SWEEP_TIME_AUTO_FALSE | 0 (0x0) | The measurement uses the sweep time that you specify in the RFMXCDMA2K_ATTR_SEM_SWEEP_TIME_INTERVAL attribute. |
| RFMXCDMA2K_VAL_SEM_SWEEP_TIME_AUTO_TRUE | 1 (0x1) | The measurement uses the default sweep time, 0.001667 seconds. |

Parent topic:

Sweep Time

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__slotphase.html language=enus -->
## TOPIC 00181: SlotPhase

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__slotphase.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__slotphase.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsResultsGroup membersNameDescriptionRFMXCDMA2K_ATTR_SLOTPHASE_ALL_TRACES_ENABLEDSpecifies whether to enable the traces to be stored and retrieved after performing the SlotPhase measurement. RFMXCDMA2K_ATTR_SLOTPHASE_MEASUREMENT_ENABLEDSpecifies whether to enable the SlotPhase measurement. RFMXC

### SlotPhase

#### Groups

- Results

#### Group members

| Name | Description |
| --- | --- |
| RFMXCDMA2K_ATTR_SLOTPHASE_ALL_TRACES_ENABLED | Specifies whether to enable the traces to be stored and retrieved after performing the SlotPhase measurement. |
| RFMXCDMA2K_ATTR_SLOTPHASE_MEASUREMENT_ENABLED | Specifies whether to enable the SlotPhase measurement. |
| RFMXCDMA2K_ATTR_SLOTPHASE_MEASUREMENT_LENGTH | Specifies the duration of the SlotPhase measurement. This value is expressed in slots. |
| RFMXCDMA2K_ATTR_SLOTPHASE_MEASUREMENT_OFFSET | Specifies the measurement offset to skip from the synchronization boundary. The synchronization boundary is specified by the RFMXCDMA2K_ATTR_SLOTPHASE_SYNCHRONIZATION_MODE attribute. This value is expressed in slots. |
| RFMXCDMA2K_ATTR_SLOTPHASE_RECEIVE_FILTER_ENABLED | Specifies whether to enable the received filter for the SlotPhase measurement. Use this attribute to disable the filter, if the received signal is already filtered. |
| RFMXCDMA2K_ATTR_SLOTPHASE_SPECTRUM_INVERTED | Specifies whether the spectrum of the signal is inverted. |
| RFMXCDMA2K_ATTR_SLOTPHASE_SYNCHRONIZATION_MODE | Specifies whether the measurement is performed from the frame or slot boundary. |
| RFMXCDMA2K_ATTR_SLOTPHASE_TRANSIENT_DURATION | Specifies the region to exclude for computing the individual slot phase discontinuity values. This value is expressed in seconds. |

#### Attachments

None

Parent topic:

Attributes

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__slotphase_1gaaff807906e77a16412f9f124020143b5.html language=enus -->
## TOPIC 00182: RFMXCDMA2K_ATTR_SLOTPHASE_SYNCHRONIZATION_MODE

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__slotphase_1gaaff807906e77a16412f9f124020143b5.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__slotphase_1gaaff807906e77a16412f9f124020143b5.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement is performed from the frame or slot boundary. SyntaxRFMXCDMA2K_ATTR_SLOTPHASE_SYNCHRONIZATION_MODENumeric ValueData TypeAccessApplies To6377474int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default sign

### RFMXCDMA2K_ATTR_SLOTPHASE_SYNCHRONIZATION_MODE

Specifies whether the measurement is performed from the frame or slot boundary.

#### Syntax

RFMXCDMA2K_ATTR_SLOTPHASE_SYNCHRONIZATION_MODE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6377474 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **Slot**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXCDMA2K_VAL_SLOTPHASE_SYNCHRONIZATION_MODE_FRAME | 0 (0x0) | The frame boundary is detected, and the measurement is performed over the number of slots specified by the RFMXCDMA2K_ATTR_SLOTPHASE_MEASUREMENT_LENGTH attribute starting at the RFMXCDMA2K_ATTR_SLOTPHASE_MEASUREMENT_LENGTH slots from the frame boundary. |
| RFMXCDMA2K_VAL_SLOTPHASE_SYNCHRONIZATION_MODE_SLOT | 1 (0x1) | The slot boundary is detected, and the measurement is performed over the number of slots specified by the SlotPhase Meas Length attribute starting at the SlotPhase measurement offset slots from the slot boundary. |

Parent topic:

SlotPhase

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__slotphase__results.html language=enus -->
## TOPIC 00183: Results

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__slotphase__results.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__slotphase__results.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXCDMA2K_ATTR_SLOTPHASE_RESULTS_MAXIMUM_PHASE_DISCONTINUITYReturns the maximum slot phase discontinuity value observed in the measurement interval. This value is expressed in degrees. AttachmentsNone

### Results

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXCDMA2K_ATTR_SLOTPHASE_RESULTS_MAXIMUM_PHASE_DISCONTINUITY | Returns the maximum slot phase discontinuity value observed in the measurement interval. This value is expressed in degrees. |

#### Attachments

None

Parent topic:

SlotPhase

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__slotphase__results_1ga08492d5b70364c8470aa20b631e646ee.html language=enus -->
## TOPIC 00184: RFMXCDMA2K_ATTR_SLOTPHASE_RESULTS_MAXIMUM_PHASE_DISCONTINUITY

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__slotphase__results_1ga08492d5b70364c8470aa20b631e646ee.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__slotphase__results_1ga08492d5b70364c8470aa20b631e646ee.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum slot phase discontinuity value observed in the measurement interval. This value is expressed in degrees. SyntaxRFMXCDMA2K_ATTR_SLOTPHASE_RESULTS_MAXIMUM_PHASE_DISCONTINUITYNumeric ValueData TypeAccessApplies To6377483float64Read-OnlyN/ARemarks You do not need to use a selector st

### RFMXCDMA2K_ATTR_SLOTPHASE_RESULTS_MAXIMUM_PHASE_DISCONTINUITY

Returns the maximum slot phase discontinuity value observed in the measurement interval. This value is expressed in degrees.

#### Syntax

RFMXCDMA2K_ATTR_SLOTPHASE_RESULTS_MAXIMUM_PHASE_DISCONTINUITY

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6377483 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and named results.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__slotpower.html language=enus -->
## TOPIC 00185: SlotPower

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__slotpower.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__slotpower.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXCDMA2K_ATTR_SLOTPOWER_MEASUREMENT_ENABLEDSpecifies whether to enable the SlotPower measurement. RFMXCDMA2K_ATTR_SLOTPOWER_MEASUREMENT_LENGTHSpecifies the duration of the SlotPower measurement. This value is expressed in slots. RFMXCDMA2K_ATTR_SLOTPOWER_MEASU

### SlotPower

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXCDMA2K_ATTR_SLOTPOWER_MEASUREMENT_ENABLED | Specifies whether to enable the SlotPower measurement. |
| RFMXCDMA2K_ATTR_SLOTPOWER_MEASUREMENT_LENGTH | Specifies the duration of the SlotPower measurement. This value is expressed in slots. |
| RFMXCDMA2K_ATTR_SLOTPOWER_MEASUREMENT_OFFSET | Specifies the measurement offset to skip from the synchronization boundary. The synchronization boundary is specified by the RFMXCDMA2K_ATTR_SLOTPOWER_SYNCHRONIZATION_MODE attribute. This value is expressed in slots. |
| RFMXCDMA2K_ATTR_SLOTPOWER_RECEIVE_FILTER_ENABLED | Specifies whether to enable the received filter for the SlotPower measurement. Use this attribute to disable the filter, if the received signal is already filtered. |
| RFMXCDMA2K_ATTR_SLOTPOWER_SPECTRUM_INVERTED | Specifies whether the spectrum of the signal is inverted. |
| RFMXCDMA2K_ATTR_SLOTPOWER_SYNCHRONIZATION_MODE | Specifies whether the measurement is performed from the frame or slot boundary. |

#### Attachments

None

Parent topic:

Attributes

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__slotpower_1ga005afe457d45f494d34f494a1af3a9bf.html language=enus -->
## TOPIC 00186: RFMXCDMA2K_ATTR_SLOTPOWER_RECEIVE_FILTER_ENABLED

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__slotpower_1ga005afe457d45f494d34f494a1af3a9bf.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__slotpower_1ga005afe457d45f494d34f494a1af3a9bf.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the received filter for the SlotPower measurement. Use this attribute to disable the filter, if the received signal is already filtered. SyntaxRFMXCDMA2K_ATTR_SLOTPOWER_RECEIVE_FILTER_ENABLEDNumeric ValueData TypeAccessApplies To6373382int32Read/WriteN/ARemarks You do not

### RFMXCDMA2K_ATTR_SLOTPOWER_RECEIVE_FILTER_ENABLED

Specifies whether to enable the received filter for the SlotPower measurement. Use this attribute to disable the filter, if the received signal is already filtered.

#### Syntax

RFMXCDMA2K_ATTR_SLOTPOWER_RECEIVE_FILTER_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6373382 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **True**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXCDMA2K_VAL_SLOTPOWER_RECEIVE_FILTER_ENABLED_FALSE | 0 (0x0) | Disables received filtering for the SlotPower measurement. |
| RFMXCDMA2K_VAL_SLOTPOWER_RECEIVE_FILTER_ENABLED_TRUE | 1 (0x1) | Enables received filtering for the SlotPower measurement. |

Parent topic:

SlotPower

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__slotpower_1ga042a75da6dc6de99537dc418286a3f00.html language=enus -->
## TOPIC 00187: RFMXCDMA2K_ATTR_SLOTPOWER_SPECTRUM_INVERTED

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__slotpower_1ga042a75da6dc6de99537dc418286a3f00.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__slotpower_1ga042a75da6dc6de99537dc418286a3f00.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the spectrum of the signal is inverted. SyntaxRFMXCDMA2K_ATTR_SLOTPOWER_SPECTRUM_INVERTEDNumeric ValueData TypeAccessApplies To6373381int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the

### RFMXCDMA2K_ATTR_SLOTPOWER_SPECTRUM_INVERTED

Specifies whether the spectrum of the signal is inverted.

#### Syntax

RFMXCDMA2K_ATTR_SLOTPOWER_SPECTRUM_INVERTED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6373381 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **False**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXCDMA2K_VAL_SLOTPOWER_SPECTRUM_INVERTED_FALSE | 0 (0x0) | The measurement spectrum is normal. |
| RFMXCDMA2K_VAL_SLOTPOWER_SPECTRUM_INVERTED_TRUE | 1 (0x1) | The measurement spectrum is inverted. |

Parent topic:

SlotPower

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__slotpower_1ga19ec24aa342ba7801fed4d616f97a3d0.html language=enus -->
## TOPIC 00188: RFMXCDMA2K_ATTR_SLOTPOWER_MEASUREMENT_OFFSET

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__slotpower_1ga19ec24aa342ba7801fed4d616f97a3d0.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__slotpower_1ga19ec24aa342ba7801fed4d616f97a3d0.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the measurement offset to skip from the synchronization boundary. The synchronization boundary is specified by the RFMXCDMA2K_ATTR_SLOTPOWER_SYNCHRONIZATION_MODE attribute. This value is expressed in slots. SyntaxRFMXCDMA2K_ATTR_SLOTPOWER_MEASUREMENT_OFFSETNumeric ValueData TypeAccessAppli

### RFMXCDMA2K_ATTR_SLOTPOWER_MEASUREMENT_OFFSET

Specifies the measurement offset to skip from the synchronization boundary. The synchronization boundary is specified by the [RFMXCDMA2K_ATTR_SLOTPOWER_SYNCHRONIZATION_MODE](group____root__ni_r_fmx_c_d_m_a2k__attributes__slotpower_1gac0647687d6347f516064a68b82538b1a.html) attribute. This value is expressed in slots.

#### Syntax

RFMXCDMA2K_ATTR_SLOTPOWER_MEASUREMENT_OFFSET

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6373379 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 0.

Parent topic:

SlotPower

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__slotpower_1ga3bf68d4dacf3b2f9f0c1e323375b2fe2.html language=enus -->
## TOPIC 00189: RFMXCDMA2K_ATTR_SLOTPOWER_MEASUREMENT_ENABLED

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__slotpower_1ga3bf68d4dacf3b2f9f0c1e323375b2fe2.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__slotpower_1ga3bf68d4dacf3b2f9f0c1e323375b2fe2.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the SlotPower measurement. SyntaxRFMXCDMA2K_ATTR_SLOTPOWER_MEASUREMENT_ENABLEDNumeric ValueData TypeAccessApplies To6373376int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the

### RFMXCDMA2K_ATTR_SLOTPOWER_MEASUREMENT_ENABLED

Specifies whether to enable the SlotPower measurement.

#### Syntax

RFMXCDMA2K_ATTR_SLOTPOWER_MEASUREMENT_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6373376 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is FALSE.

Parent topic:

SlotPower

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__slotpower_1gac0647687d6347f516064a68b82538b1a.html language=enus -->
## TOPIC 00190: RFMXCDMA2K_ATTR_SLOTPOWER_SYNCHRONIZATION_MODE

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__slotpower_1gac0647687d6347f516064a68b82538b1a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__slotpower_1gac0647687d6347f516064a68b82538b1a.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement is performed from the frame or slot boundary. SyntaxRFMXCDMA2K_ATTR_SLOTPOWER_SYNCHRONIZATION_MODENumeric ValueData TypeAccessApplies To6373378int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default sign

### RFMXCDMA2K_ATTR_SLOTPOWER_SYNCHRONIZATION_MODE

Specifies whether the measurement is performed from the frame or slot boundary.

#### Syntax

RFMXCDMA2K_ATTR_SLOTPOWER_SYNCHRONIZATION_MODE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6373378 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **Slot**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXCDMA2K_VAL_SLOTPOWER_SYNCHRONIZATION_MODE_FRAME | 0 (0x0) | The frame boundary is detected, and the measurement is performed over the number of slots specified by the RFMXCDMA2K_ATTR_SLOTPOWER_MEASUREMENT_LENGTH attribute starting at the RFMXCDMA2K_ATTR_SLOTPOWER_MEASUREMENT_OFFSET slots from the frame boundary. |
| RFMXCDMA2K_VAL_SLOTPOWER_SYNCHRONIZATION_MODE_SLOT | 1 (0x1) | The slot boundary is detected, and the measurement is performed over the number of slots specified by the SlotPower Meas Length attribute starting at the SlotPower measurement offset slots from the slot boundary. |

Parent topic:

SlotPower

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__slotpower_1gae4a3d9ef2bdeb2e2a2fc1b9a82b4a2f5.html language=enus -->
## TOPIC 00191: RFMXCDMA2K_ATTR_SLOTPOWER_MEASUREMENT_LENGTH

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__slotpower_1gae4a3d9ef2bdeb2e2a2fc1b9a82b4a2f5.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__slotpower_1gae4a3d9ef2bdeb2e2a2fc1b9a82b4a2f5.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the duration of the SlotPower measurement. This value is expressed in slots. SyntaxRFMXCDMA2K_ATTR_SLOTPOWER_MEASUREMENT_LENGTHNumeric ValueData TypeAccessApplies To6373380int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default

### RFMXCDMA2K_ATTR_SLOTPOWER_MEASUREMENT_LENGTH

Specifies the duration of the SlotPower measurement. This value is expressed in slots.

#### Syntax

RFMXCDMA2K_ATTR_SLOTPOWER_MEASUREMENT_LENGTH

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6373380 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 16.

Parent topic:

SlotPower

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__spreading.html language=enus -->
## TOPIC 00192: Spreading

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__spreading.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__spreading.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsDownlinkUplinkGroup membersNoneAttachmentsNone

### Spreading

#### Groups

- Downlink
- Uplink

#### Group members

None

#### Attachments

None

Parent topic:

Attributes

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__spreading__uplink.html language=enus -->
## TOPIC 00193: Uplink

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__spreading__uplink.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__spreading__uplink.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXCDMA2K_ATTR_UPLINK_SPREADING_LONG_CODE_MASKSpecifies the long code mask for reverse link spreading. AttachmentsNone

### Uplink

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXCDMA2K_ATTR_UPLINK_SPREADING_LONG_CODE_MASK | Specifies the long code mask for reverse link spreading. |

#### Attachments

None

Parent topic:

Spreading

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__spreading__uplink_1ga9e88619e6c692e6bddad5ed2b995bbad.html language=enus -->
## TOPIC 00194: RFMXCDMA2K_ATTR_UPLINK_SPREADING_LONG_CODE_MASK

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__spreading__uplink_1ga9e88619e6c692e6bddad5ed2b995bbad.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__spreading__uplink_1ga9e88619e6c692e6bddad5ed2b995bbad.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the long code mask for reverse link spreading. SyntaxRFMXCDMA2K_ATTR_UPLINK_SPREADING_LONG_CODE_MASKNumeric ValueData TypeAccessApplies To6291486int64Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to

### RFMXCDMA2K_ATTR_UPLINK_SPREADING_LONG_CODE_MASK

Specifies the long code mask for reverse link spreading.

#### Syntax

RFMXCDMA2K_ATTR_UPLINK_SPREADING_LONG_CODE_MASK

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6291486 | int64 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 0.

Parent topic:

Uplink

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__trigger.html language=enus -->
## TOPIC 00195: Trigger

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__trigger.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__trigger.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsDigital EdgeIQ Power EdgeMinimum Quiet TimeGroup membersNameDescriptionRFMXCDMA2K_ATTR_TRIGGER_DELAYSpecifies the trigger delay time. This value is expressed in seconds. RFMXCDMA2K_ATTR_TRIGGER_TYPESpecifies the trigger type. AttachmentsNone

### Trigger

#### Groups

- Digital Edge
- IQ Power Edge
- Minimum Quiet Time

#### Group members

| Name | Description |
| --- | --- |
| RFMXCDMA2K_ATTR_TRIGGER_DELAY | Specifies the trigger delay time. This value is expressed in seconds. |
| RFMXCDMA2K_ATTR_TRIGGER_TYPE | Specifies the trigger type. |

#### Attachments

None

Parent topic:

Attributes

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__trigger_1ga6f52e58e343b8c62003deede9ee7f6ff.html language=enus -->
## TOPIC 00196: RFMXCDMA2K_ATTR_TRIGGER_DELAY

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__trigger_1ga6f52e58e343b8c62003deede9ee7f6ff.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__trigger_1ga6f52e58e343b8c62003deede9ee7f6ff.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the trigger delay time. This value is expressed in seconds. SyntaxRFMXCDMA2K_ATTR_TRIGGER_DELAYNumeric ValueData TypeAccessApplies To6291466float64Read/WriteN/ARemarks If the delay is negative, the measurement acquires pretrigger samples. If the delay is positive, the measurement acquires

### RFMXCDMA2K_ATTR_TRIGGER_DELAY

Specifies the trigger delay time. This value is expressed in seconds.

#### Syntax

RFMXCDMA2K_ATTR_TRIGGER_DELAY

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6291466 | float64 | Read/Write | N/A |

#### Remarks

If the delay is negative, the measurement acquires pretrigger samples. If the delay is positive, the measurement acquires post-trigger samples.

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 0 seconds.

Parent topic:

Trigger

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__trigger__digital__edge_1gadbbbbbbf750cf1522c65160a61ad4612.html language=enus -->
## TOPIC 00197: RFMXCDMA2K_ATTR_DIGITAL_EDGE_TRIGGER_EDGE

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__trigger__digital__edge_1gadbbbbbbf750cf1522c65160a61ad4612.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__trigger__digital__edge_1gadbbbbbbf750cf1522c65160a61ad4612.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the active edge for the trigger. This attribute is used only when you set the RFMXCDMA2K_ATTR_TRIGGER_TYPE attribute to Digital Edge. SyntaxRFMXCDMA2K_ATTR_DIGITAL_EDGE_TRIGGER_EDGENumeric ValueData TypeAccessApplies To6291462int32Read/WriteN/ARemarks You do not need to use a selector stri

### RFMXCDMA2K_ATTR_DIGITAL_EDGE_TRIGGER_EDGE

Specifies the active edge for the trigger. This attribute is used only when you set the [RFMXCDMA2K_ATTR_TRIGGER_TYPE](group____root__ni_r_fmx_c_d_m_a2k__attributes__trigger_1gabbabe67a8b1ecc6de63a784879646439.html) attribute to **Digital Edge**.

#### Syntax

RFMXCDMA2K_ATTR_DIGITAL_EDGE_TRIGGER_EDGE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6291462 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **Rising Edge**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXCDMA2K_VAL_DIGITAL_EDGE_RISING_EDGE | 0 (0x0) | The trigger asserts on the rising edge of the signal. |
| RFMXCDMA2K_VAL_DIGITAL_EDGE_FALLING_EDGE | 1 (0x1) | The trigger asserts on the falling edge of the signal. |

Parent topic:

Digital Edge

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__trigger__iq__power__edge_1ga689f9244b7d6a21b40579255289dc02a.html language=enus -->
## TOPIC 00198: RFMXCDMA2K_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__trigger__iq__power__edge_1ga689f9244b7d6a21b40579255289dc02a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__trigger__iq__power__edge_1ga689f9244b7d6a21b40579255289dc02a.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the reference for the IQ Power Edge Level Type attribute. This attribute is used only when you set the RFMXCDMA2K_ATTR_TRIGGER_TYPE attribute to IQ Power Edge. SyntaxRFMXCDMA2K_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPENumeric ValueData TypeAccessApplies To6295551int32Read/WriteN/ARemarks You d

### RFMXCDMA2K_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE

Specifies the reference for the IQ Power Edge Level Type attribute. This attribute is used only when you set the [RFMXCDMA2K_ATTR_TRIGGER_TYPE](group____root__ni_r_fmx_c_d_m_a2k__attributes__trigger_1gabbabe67a8b1ecc6de63a784879646439.html) attribute to **IQ Power Edge**.

#### Syntax

RFMXCDMA2K_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6295551 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **Relative**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXCDMA2K_VAL_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_RELATIVE | 0 (0x0) | The IQ Power Edge Level attribute is relative to the value of the RFMXCDMA2K_ATTR_REFERENCE_LEVEL attribute. |
| RFMXCDMA2K_VAL_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_ABSOLUTE | 1 (0x1) | The IQ Power Edge Level attribute specifies the absolute power. |

Parent topic:

IQ Power Edge

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__trigger__iq__power__edge_1gaafcdbf8469e1e2ba02a9f895886f1a3f.html language=enus -->
## TOPIC 00199: RFMXCDMA2K_ATTR_IQ_POWER_EDGE_TRIGGER_SOURCE

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__trigger__iq__power__edge_1gaafcdbf8469e1e2ba02a9f895886f1a3f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__trigger__iq__power__edge_1gaafcdbf8469e1e2ba02a9f895886f1a3f.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the channel from which the device monitors the trigger. This attribute is used only when you set the RFMXCDMA2K_ATTR_TRIGGER_TYPE attribute to IQ Power Edge. SyntaxRFMXCDMA2K_ATTR_IQ_POWER_EDGE_TRIGGER_SOURCENumeric ValueData TypeAccessApplies To6291463char[]Read/WriteN/ARemarks You do not

### RFMXCDMA2K_ATTR_IQ_POWER_EDGE_TRIGGER_SOURCE

Specifies the channel from which the device monitors the trigger. This attribute is used only when you set the [RFMXCDMA2K_ATTR_TRIGGER_TYPE](group____root__ni_r_fmx_c_d_m_a2k__attributes__trigger_1gabbabe67a8b1ecc6de63a784879646439.html) attribute to **IQ Power Edge**.

#### Syntax

RFMXCDMA2K_ATTR_IQ_POWER_EDGE_TRIGGER_SOURCE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6291463 | char[] | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value of this attribute is hardware dependent.

Parent topic:

IQ Power Edge

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__trigger__minimum__quiet__time.html language=enus -->
## TOPIC 00200: Minimum Quiet Time

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__trigger__minimum__quiet__time.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__trigger__minimum__quiet__time.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXCDMA2K_ATTR_TRIGGER_MINIMUM_QUIET_TIME_DURATIONSpecifies the time duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. This value is expressed in seconds. RFMXCDMA2K_ATTR_TRIGGER_MINIMUM_QUIET_TIME_MODESpeci

### Minimum Quiet Time

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXCDMA2K_ATTR_TRIGGER_MINIMUM_QUIET_TIME_DURATION | Specifies the time duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. This value is expressed in seconds. |
| RFMXCDMA2K_ATTR_TRIGGER_MINIMUM_QUIET_TIME_MODE | Specifies whether the measurement computes the minimum quiet time used for triggering. |

#### Attachments

None

Parent topic:

Trigger

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__trigger__minimum__quiet__time_1gacb45e2cd75c0f81fa2e92d4f81e96ccf.html language=enus -->
## TOPIC 00201: RFMXCDMA2K_ATTR_TRIGGER_MINIMUM_QUIET_TIME_DURATION

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__trigger__minimum__quiet__time_1gacb45e2cd75c0f81fa2e92d4f81e96ccf.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__trigger__minimum__quiet__time_1gacb45e2cd75c0f81fa2e92d4f81e96ccf.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the time duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. This value is expressed in seconds. SyntaxRFMXCDMA2K_ATTR_TRIGGER_MINIMUM_QUIET_TIME_DURATIONNumeric ValueData TypeAccessApplies To6291468float64Read/WriteN/ARemarks If you set

### RFMXCDMA2K_ATTR_TRIGGER_MINIMUM_QUIET_TIME_DURATION

Specifies the time duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. This value is expressed in seconds.

#### Syntax

RFMXCDMA2K_ATTR_TRIGGER_MINIMUM_QUIET_TIME_DURATION

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6291468 | float64 | Read/Write | N/A |

#### Remarks

If you set the [RFMXCDMA2K_ATTR_IQ_POWER_EDGE_TRIGGER_SLOPE](group____root__ni_r_fmx_c_d_m_a2k__attributes__trigger__iq__power__edge_1ga5b4d80a07c74c371dedf7d3d7c8d5dcd.html) attribute to **Rising Slope**, the signal is quiet below the trigger level. If you set the IQ Power Edge Slope attribute to **Falling Slope**, the signal is quiet above the trigger level.

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value of this attribute is hardware dependent.

Parent topic:

Minimum Quiet Time

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__attributes__trigger__minimum__quiet__time_1gaec006b3b609f69d03d534ba25fe47e7d.html language=enus -->
## TOPIC 00202: RFMXCDMA2K_ATTR_TRIGGER_MINIMUM_QUIET_TIME_MODE

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__attributes__trigger__minimum__quiet__time_1gaec006b3b609f69d03d534ba25fe47e7d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__attributes__trigger__minimum__quiet__time_1gaec006b3b609f69d03d534ba25fe47e7d.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement computes the minimum quiet time used for triggering. SyntaxRFMXCDMA2K_ATTR_TRIGGER_MINIMUM_QUIET_TIME_MODENumeric ValueData TypeAccessApplies To6291467int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the defa

### RFMXCDMA2K_ATTR_TRIGGER_MINIMUM_QUIET_TIME_MODE

Specifies whether the measurement computes the minimum quiet time used for triggering.

#### Syntax

RFMXCDMA2K_ATTR_TRIGGER_MINIMUM_QUIET_TIME_MODE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 6291467 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **Auto**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXCDMA2K_VAL_TRIGGER_MINIMUM_QUIET_TIME_MODE_MANUAL | 0 (0x0) | The minimum quiet time for triggering is the value of the RFMXCDMA2K_ATTR_TRIGGER_MINIMUM_QUIET_TIME_DURATION attribute. |
| RFMXCDMA2K_VAL_TRIGGER_MINIMUM_QUIET_TIME_MODE_AUTO | 1 (0x1) | The measurement computes the minimum quiet time used for triggering. |

Parent topic:

Minimum Quiet Time

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions.html language=enus -->
## TOPIC 00203: Functions

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsAdvancedBuild StringConfigurationFetchSelect MeasurementSet and Get AttributesUtilityGroup membersNameDescriptionRFmxCDMA2k_CloseCloses the session to the device. RFmxCDMA2k_GetErrorRetrieves and then clears the error information for the session or the current execution thread. You must provid

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
| RFmxCDMA2k_Close | Closes the session to the device. |
| RFmxCDMA2k_GetError | Retrieves and then clears the error information for the session or the current execution thread. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the errorDescriptionBufferSize parameter. |
| RFmxCDMA2k_GetErrorString | Converts a status code returned by an RFmxCDMA2k function into a user-readable string. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the errorDescriptionBufferSize parameter. |
| RFmxCDMA2k_Initialize | Creates an RFmx session to the device you specify through the resourceName parameter, and returns a handleOut that identifies this device in all subsequent RFmx functions. |
| RFmxCDMA2k_Initiate | Initiates all enabled measurements. Call this function after configuring the signal and measurement. |

#### Attachments

None

Parent topic:

niRFmxCDMA2k.h

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions_1ga0879efb64e5c57089d2bef12a3c0c3f1.html language=enus -->
## TOPIC 00204: RFmxCDMA2k_GetErrorString

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions_1ga0879efb64e5c57089d2bef12a3c0c3f1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions_1ga0879efb64e5c57089d2bef12a3c0c3f1.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts a status code returned by an RFmxCDMA2k function into a user-readable string. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the errorDescriptionBufferSize parameter. Syntaxint32 __stdcall RFmxCDMA2k_GetErrorString(niRFmxInstrHand

### RFmxCDMA2k_GetErrorString

Converts a status code returned by an RFmxCDMA2k function into a user-readable string. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **errorDescriptionBufferSize** parameter.

#### Syntax

int32 __stdcall RFmxCDMA2k_GetErrorString(niRFmxInstrHandle instrumentHandle, int32 errorCode, int32 errorDescriptionBufferSize, char errorDescription[])

#### Remarks

If the error description, including the terminating NULL byte, is larger than the size you indicate in the **errorDescriptionBufferSize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

If you want to call this function just to get the required buffer size, you must pass 0 for **errorDescriptionBufferSize** and NULL for the **errorDescription** buffer.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxCDMA2k_Initialize function. |
| errorCode | [in] | int32 | Passes the statusOrRequiredSize parameter that is returned from any RFmxCDMA2k function. |
| errorDescriptionBufferSize | [in] | int32 | Passes the number of bytes in the char array you specify in errorDescription.If the error description, including the terminating NULL byte, contains more bytes than you indicate in this parameter, the function copies errorDescriptionBufferSize - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the size of the buffer that you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7. |
| errorDescription | [out] | char[] | Returns the user-readable message string that corresponds to the status code you specify.If you pass 0 for errorDescriptionBufferSize, you can pass NULL for the errorDescription buffer parameter to get the size of error description message. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

When the **statusOrRequiredSize** return value returns the buffer size, the status code is not returned.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions_1ga6a74144a3c40488e8cdacbf36b7778d9.html language=enus -->
## TOPIC 00205: RFmxCDMA2k_Initialize

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions_1ga6a74144a3c40488e8cdacbf36b7778d9.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions_1ga6a74144a3c40488e8cdacbf36b7778d9.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an RFmx session to the device you specify through the resourceName parameter, and returns a handleOut that identifies this device in all subsequent RFmx functions. Syntaxint32 __stdcall RFmxCDMA2k_Initialize(char resourceName[], char optionString[], niRFmxInstrHandle *handleOut, int32 *isNew

### RFmxCDMA2k_Initialize

Creates an RFmx session to the device you specify through the **resourceName** parameter, and returns a **handleOut** that identifies this device in all subsequent RFmx functions.

#### Syntax

int32 __stdcall RFmxCDMA2k_Initialize(char resourceName[], char optionString[], niRFmxInstrHandle *handleOut, int32 *isNewSession)

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
| isNewSession | [out] | int32 * | Returns RFMXCDMA2K_VAL_TRUE if the function created a new session, or RFMXCDMA2K_VAL_FALSE if the function returned a reference to an existing session. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html language=enus -->
## TOPIC 00206: RFmxCDMA2k_GetError

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Retrieves and then clears the error information for the session or the current execution thread. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the errorDescriptionBufferSize parameter. Syntaxint32 __stdcall RFmxCDMA2k_GetError(niRFmxInstr

### RFmxCDMA2k_GetError

Retrieves and then clears the error information for the session or the current execution thread. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **errorDescriptionBufferSize** parameter.

#### Syntax

int32 __stdcall RFmxCDMA2k_GetError(niRFmxInstrHandle instrumentHandle, int32 *errorCode, int32 errorDescriptionBufferSize, char errorDescription[])

#### Remarks

If the error description, including the terminating NULL byte, is larger than the size you indicate in the **errorDescriptionBufferSize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

If you want to call this function just to get the required buffer size, you must pass 0 for **errorDescriptionBufferSize** and NULL for the errorDescription buffer.

Note

Use the [RFmxCDMA2k_GetErrorString](group____root__ni_r_fmx_c_d_m_a2k__functions_1ga0879efb64e5c57089d2bef12a3c0c3f1.html) function if the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function does not return an error message.

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

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions_1gafb56460158bf0121f9bf319265307435.html language=enus -->
## TOPIC 00207: RFmxCDMA2k_Initiate

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions_1gafb56460158bf0121f9bf319265307435.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions_1gafb56460158bf0121f9bf319265307435.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initiates all enabled measurements. Call this function after configuring the signal and measurement. Syntaxint32 __stdcall RFmxCDMA2k_Initiate(niRFmxInstrHandle instrumentHandle, char selectorString[], char resultName[])RemarksThis function asynchronously launches measurements in the background and

### RFmxCDMA2k_Initiate

Initiates all enabled measurements. Call this function after configuring the signal and measurement.

#### Syntax

int32 __stdcall RFmxCDMA2k_Initiate(niRFmxInstrHandle instrumentHandle, char selectorString[], char resultName[])

#### Remarks

This function asynchronously launches measurements in the background and immediately returns to the caller program. You can fetch measurement results using the Fetch functions or result attributes in the attribute node. To get the status of measurements, use the [RFmxCDMA2k_WaitForMeasurementComplete](group____root__ni_r_fmx_c_d_m_a2k__functions__utility_1gacf7c9fdf6aef0565293dd90ab944fd89.html) function or [RFmxCDMA2k_CheckMeasurementStatus](group____root__ni_r_fmx_c_d_m_a2k__functions__utility_1gadb7605431716089d5430cd2bad652414.html) function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising the signal name and the result name. The result name can either by specified through this input or the Result Name input. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name in this input, either the result name specified by the Result Name input or the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| resultName | [in] | char[] | This parameter specifies the name to be associated with measurement results. Provide a unique name, such as "r1" to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result:" prefix. The default value is "" (empty string), which refers to the default result instance.Examples:"""result::r1""r1" |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__advanced.html language=enus -->
## TOPIC 00208: Advanced

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__advanced.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__advanced.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsAnalyze2Group membersNameDescriptionRFmxCDMA2k_AbortMeasurementsStops acquisition and measurements associated with the signal instance that you specify in the Selector String parameter. The acquisition and measurements were previously initiated by the RFmxCDMA2k_Initiate function or measuremen

### Advanced

#### Groups

- Analyze2

#### Group members

| Name | Description |
| --- | --- |
| RFmxCDMA2k_AbortMeasurements | Stops acquisition and measurements associated with the signal instance that you specify in the Selector String parameter. The acquisition and measurements were previously initiated by the RFmxCDMA2k_Initiate function or measurement read functions. |
| RFmxCDMA2k_ClearAllNamedResults | Clears all results for the signal that you specify in the Selector String parameter. |
| RFmxCDMA2k_ClearNamedResult | Clears a result instance specified by the result name in the Selector String parameter. |
| RFmxCDMA2k_CloneSignalConfiguration | Creates a new instance of a signal by copying all the attribute values from an existing signal instance. |
| RFmxCDMA2k_CreateSignalConfiguration | Creates a new instance of a signal. |
| RFmxCDMA2k_DeleteSignalConfiguration | Deletes an instance of a signal that you specify in the Signal Name parameter. |
| RFmxCDMA2k_GetAllNamedResultNames | Returns the named result names of the signal that you specify in the Selector String parameter. |

#### Attachments

None

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__advanced_1ga7582b54d8653dba9439f01320b0203bd.html language=enus -->
## TOPIC 00209: RFmxCDMA2k_CreateSignalConfiguration

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__advanced_1ga7582b54d8653dba9439f01320b0203bd.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__advanced_1ga7582b54d8653dba9439f01320b0203bd.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a new instance of a signal. Syntaxint32 __stdcall RFmxCDMA2k_CreateSignalConfiguration(niRFmxInstrHandle instrumentHandle, char signalName[])ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifies the RFmx session refnum. This parameter is obtained

### RFmxCDMA2k_CreateSignalConfiguration

Creates a new instance of a signal.

#### Syntax

int32 __stdcall RFmxCDMA2k_CreateSignalConfiguration(niRFmxInstrHandle instrumentHandle, char signalName[])

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| signalName | [in] | char[] | This parameter specifies the name of the signal. This input accepts the signal name with or without the "signal::" prefix.Examples:"signal::sig1""sig1" |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__advanced_1ga858e07e8d9334aec5e6645d46fd0eb36.html language=enus -->
## TOPIC 00210: RFmxCDMA2k_CloneSignalConfiguration

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__advanced_1ga858e07e8d9334aec5e6645d46fd0eb36.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__advanced_1ga858e07e8d9334aec5e6645d46fd0eb36.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a new instance of a signal by copying all the attribute values from an existing signal instance. Syntaxint32 __stdcall RFmxCDMA2k_CloneSignalConfiguration(niRFmxInstrHandle instrumentHandle, char oldSignalName[], char newSignalName[])ParametersNameDirectionTypeDescriptioninstrumentHandle[in]

### RFmxCDMA2k_CloneSignalConfiguration

Creates a new instance of a signal by copying all the attribute values from an existing signal instance.

#### Syntax

int32 __stdcall RFmxCDMA2k_CloneSignalConfiguration(niRFmxInstrHandle instrumentHandle, char oldSignalName[], char newSignalName[])

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| oldSignalName | [in] | char[] | This parameter specifies the name of an existing signal. This input accepts the signal name with or without the "signal::" prefix.Examples:"signal::OldSigName""OldSigName" |
| newSignalName | [in] | char[] | This parameter specifies the name of the new signal. This input accepts the signal name with or without the "signal::" prefix.Examples:"signal::NewSigName""NewSigName" |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__advanced_1gacdd4eaf60255a00e6a6a40fa95f590f6.html language=enus -->
## TOPIC 00211: RFmxCDMA2k_GetAllNamedResultNames

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__advanced_1gacdd4eaf60255a00e6a6a40fa95f590f6.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__advanced_1gacdd4eaf60255a00e6a6a40fa95f590f6.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the named result names of the signal that you specify in the Selector String parameter. Syntaxint32 __stdcall RFmxCDMA2k_GetAllNamedResultNames(niRFmxInstrHandle instrumentHandle, char selectorString[], char resultNames[], int32 resultNamesBufferSize, int32 *actualResultNamesSize, int32 *def

### RFmxCDMA2k_GetAllNamedResultNames

Returns the named result names of the signal that you specify in the **Selector String** parameter.

#### Syntax

int32 __stdcall RFmxCDMA2k_GetAllNamedResultNames(niRFmxInstrHandle instrumentHandle, char selectorString[], char resultNames[], int32 resultNamesBufferSize, int32 *actualResultNamesSize, int32 *defaultResultExists)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Examples:"""signal::sig1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| resultNames | [out] | char[] | This parameter returns an array of result names. |
| resultNamesBufferSize | [in] | int32 | Specifies the size of the resultNames array. Set the resultNamesBufferSize parameter to 0 to get the size of the resultNames array in the return value. |
| actualResultNamesSize | [out] | int32 * | Returns the actual size of the resultNames array, if you pass NULL to resultNames array parameter and set the resultNamesBufferSize parameter to 0. |
| defaultResultExists | [out] | int32 * | This parameter indicates whether the default result exists. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__advanced_1gad0c0f9dcba808e9c2f3a5c53920245ea.html language=enus -->
## TOPIC 00212: RFmxCDMA2k_AbortMeasurements

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__advanced_1gad0c0f9dcba808e9c2f3a5c53920245ea.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__advanced_1gad0c0f9dcba808e9c2f3a5c53920245ea.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Stops acquisition and measurements associated with the signal instance that you specify in the Selector String parameter. The acquisition and measurements were previously initiated by the RFmxCDMA2k_Initiate function or measurement read functions. Syntaxint32 __stdcall RFmxCDMA2k_AbortMeasurements(n

### RFmxCDMA2k_AbortMeasurements

Stops acquisition and measurements associated with the signal instance that you specify in the **Selector String** parameter. The acquisition and measurements were previously initiated by the [RFmxCDMA2k_Initiate](group____root__ni_r_fmx_c_d_m_a2k__functions_1gafb56460158bf0121f9bf319265307435.html) function or measurement read functions.

#### Syntax

int32 __stdcall RFmxCDMA2k_AbortMeasurements(niRFmxInstrHandle instrumentHandle, char selectorString[])

#### Remarks

Calling this function is optional, unless you want to stop a measurement before it is complete. This function executes even if there is an incoming error.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Examples:"""signal::sig1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__advanced_1gae542973d75f6e1cbb6c202f25b47f2ef.html language=enus -->
## TOPIC 00213: RFmxCDMA2k_ClearNamedResult

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__advanced_1gae542973d75f6e1cbb6c202f25b47f2ef.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__advanced_1gae542973d75f6e1cbb6c202f25b47f2ef.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Clears a result instance specified by the result name in the Selector String parameter. Syntaxint32 __stdcall RFmxCDMA2k_ClearNamedResult(niRFmxInstrHandle instrumentHandle, char selectorString[])ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifies the

### RFmxCDMA2k_ClearNamedResult

Clears a result instance specified by the result name in the **Selector String** parameter.

#### Syntax

int32 __stdcall RFmxCDMA2k_ClearNamedResult(niRFmxInstrHandle instrumentHandle, char selectorString[])

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__advanced__analyze2.html language=enus -->
## TOPIC 00214: Analyze2

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__advanced__analyze2.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__advanced__analyze2.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxCDMA2k_AnalyzeIQ1WaveformPerforms the enabled measurements on the I/Q complex waveform that you specify in IQ parameter. Call this function after you configure the signal and measurement attributes. You can fetch measurement results using the Fetch functions

### Analyze2

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxCDMA2k_AnalyzeIQ1Waveform | Performs the enabled measurements on the I/Q complex waveform that you specify in IQ parameter. Call this function after you configure the signal and measurement attributes. You can fetch measurement results using the Fetch functions or result attributes in the attribute node. Use this function only if the RFMXINSTR_ATTR_RECOMMENDED_ACQUISITION_TYPE attribute value is either IQ or IQ or Spectral. Note Query the Recommended Acquisition Type attribute from the RFmxInstr Attribute after calling the RFmxCDMA2k_Commit function. |
| RFmxCDMA2k_AnalyzeIQ1WaveformSplit | Performs the enabled measurements on the I/Q complex waveform that you specify in IQ parameter. Call this function after you configure the signal and measurement attributes. You can fetch measurement results using the Fetch functions or result attributes in the attribute node. Use this function only if the RFMXINSTR_ATTR_RECOMMENDED_ACQUISITION_TYPE attribute value is either IQ or IQ or Spectral. Note Query the Recommended Acquisition Type attribute from the RFmxInstr Attribute after calling the RFmxCDMA2k_Commit function. |
| RFmxCDMA2k_AnalyzeSpectrum1Waveform | Performs the enabled measurements on the spectrum waveform that you specify in Spectrum parameter. Call this function after you configure the signal and measurement attributes. You can fetch measurement results using the Fetch functions or result attributes in the attribute node. Use this function only if the RFMXINSTR_ATTR_RECOMMENDED_ACQUISITION_TYPE attribute value is either Spectral or IQ or Spectral. |

#### Attachments

None

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__advanced__analyze2_1ga281fe7c4850d4f2f6aaf7b9b22839c41.html language=enus -->
## TOPIC 00215: RFmxCDMA2k_AnalyzeIQ1Waveform

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__advanced__analyze2_1ga281fe7c4850d4f2f6aaf7b9b22839c41.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__advanced__analyze2_1ga281fe7c4850d4f2f6aaf7b9b22839c41.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs the enabled measurements on the I/Q complex waveform that you specify in IQ parameter. Call this function after you configure the signal and measurement attributes. You can fetch measurement results using the Fetch functions or result attributes in the attribute node. Use this function only

### RFmxCDMA2k_AnalyzeIQ1Waveform

Performs the enabled measurements on the I/Q complex waveform that you specify in **IQ** parameter. Call this function after you configure the signal and measurement attributes. You can fetch measurement results using the Fetch functions or result attributes in the attribute node. Use this function only if the [RFMXINSTR_ATTR_RECOMMENDED_ACQUISITION_TYPE](/csh?context=rfmxinstr_rfmxinstrcref_attribute_recommended_acquisition_type) attribute value is either **IQ** or **IQ or Spectral**.

Note

Query the Recommended Acquisition Type attribute from the RFmxInstr Attribute after calling the [RFmxCDMA2k_Commit](group____root__ni_r_fmx_c_d_m_a2k__functions__utility_1gadc861bbb47d7f5e708244d9a66cded29.html) function.

#### Syntax

int32 __stdcall RFmxCDMA2k_AnalyzeIQ1Waveform(niRFmxInstrHandle instrumentHandle, char selectorString[], char resultName[], float64 x0, float64 dx, NIComplexSingle iq[], int32 arraySize, int32 reset, int64 reserved)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function or the RFmxInstr Initialize function with option string as "AnalysisOnly=1". |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. The result name can either be specified through this input or the Result Name parameter. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name in this input, either the result name specified by Result Name parameter or the default result instance is used. The default is "" (empty string).Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxCDMA2k Build Signal String function to build the selector string. |
| resultName | [in] | char[] | This parameter specifies the name to be associated with measurement results. Provide a unique name, such as "r1" to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. The default value is "" (empty string) which refers to default result instance.Example:"result::r1""r1" |
| x0 | [in] | float64 | This parameter specifies the start time of the input Y array. This value is expressed in seconds. |
| dx | [in] | float64 | This parameter specifies the time interval between the samples in the input Y array. This value is expressed in seconds. The reciprocal of dx indicates the I/Q rate of the input signal. |
| iq | [in] | NIComplexSingle[] | This parameter specifies the array of complex-valued time domain data. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively. |
| arraySize | [in] | int32 | Specifies the size of the array. |
| reset | [in] | int32 | This parameter resets measurement averaging. If you enable averaging, set this parameter to TRUE for first record and FALSE for subsequent records. |
| reserved | [in] | int64 | Reserved for future use. Any value passed to this parameter will be ignored. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Analyze2

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__advanced__analyze2_1gaa869a5e8eee9bb97eff4bb90464e8052.html language=enus -->
## TOPIC 00216: RFmxCDMA2k_AnalyzeSpectrum1Waveform

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__advanced__analyze2_1gaa869a5e8eee9bb97eff4bb90464e8052.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__advanced__analyze2_1gaa869a5e8eee9bb97eff4bb90464e8052.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs the enabled measurements on the spectrum waveform that you specify in Spectrum parameter. Call this function after you configure the signal and measurement attributes. You can fetch measurement results using the Fetch functions or result attributes in the attribute node. Use this function o

### RFmxCDMA2k_AnalyzeSpectrum1Waveform

Performs the enabled measurements on the spectrum waveform that you specify in **Spectrum** parameter. Call this function after you configure the signal and measurement attributes. You can fetch measurement results using the Fetch functions or result attributes in the attribute node. Use this function only if the [RFMXINSTR_ATTR_RECOMMENDED_ACQUISITION_TYPE](/csh?context=rfmxinstr_rfmxinstrcref_attribute_recommended_acquisition_type) attribute value is either **Spectral** or **IQ or Spectral**.

#### Syntax

int32 __stdcall RFmxCDMA2k_AnalyzeSpectrum1Waveform(niRFmxInstrHandle instrumentHandle, char selectorString[], char resultName[], float64 x0, float64 dx, float32 spectrum[], int32 arraySize, int32 reset, int64 reserved)

#### Remarks

Note

Query the Recommended Acquisition Type attribute from the RFmxInstr Attribute after calling the [RFmx CDMA2k Commit](/csh?context=rfmxcdma2k_rfmxcdma2kcref_function_commit) function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function or the RFmxInstr Initialize function with option string as "AnalysisOnly=1". |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. The result name can either be specified through this input or the Result Name parameter. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name in this input, either the result name specified by Result Name parameter or the default result instance is used. The default is "" (empty string).Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxCDMA2k Build Signal String function to build the selector string. |
| resultName | [in] | char[] | This parameter specifies the name to be associated with measurement results. Provide a unique name, such as "r1" to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. The default value is "" (empty string) which refers to default result instance.Example:"result::r1""r1" |
| x0 | [in] | float64 | This parameter specifies the start frequency of the spectrum. This value is expressed in Hz. |
| dx | [in] | float64 | This parameter specifies the frequency interval between data points in the spectrum. |
| spectrum | [in] | float32[] | This parameter contains the real-value power spectrum. |
| arraySize | [in] | int32 | Specifies the size of the array. |
| reset | [in] | int32 | This parameter resets measurement averaging. If you enable averaging, set this parameter to TRUE for first record and FALSE for subsequent records. |
| reserved | [in] | int64 | Reserved for future use. Any value passed to this parameter will be ignored. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Analyze2

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__advanced__analyze2_1gab88998eb5135a136a579fc43e6d9aacf.html language=enus -->
## TOPIC 00217: RFmxCDMA2k_AnalyzeIQ1WaveformSplit

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__advanced__analyze2_1gab88998eb5135a136a579fc43e6d9aacf.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__advanced__analyze2_1gab88998eb5135a136a579fc43e6d9aacf.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs the enabled measurements on the I/Q complex waveform that you specify in IQ parameter. Call this function after you configure the signal and measurement attributes. You can fetch measurement results using the Fetch functions or result attributes in the attribute node. Use this function only

### RFmxCDMA2k_AnalyzeIQ1WaveformSplit

Performs the enabled measurements on the I/Q complex waveform that you specify in **IQ** parameter. Call this function after you configure the signal and measurement attributes. You can fetch measurement results using the Fetch functions or result attributes in the attribute node. Use this function only if the [RFMXINSTR_ATTR_RECOMMENDED_ACQUISITION_TYPE](/csh?context=rfmxinstr_rfmxinstrcref_attribute_recommended_acquisition_type) attribute value is either **IQ** or **IQ or Spectral**.

Note

Query the Recommended Acquisition Type attribute from the RFmxInstr Attribute after calling the [RFmxCDMA2k_Commit](group____root__ni_r_fmx_c_d_m_a2k__functions__utility_1gadc861bbb47d7f5e708244d9a66cded29.html) function.

#### Syntax

int32 __stdcall RFmxCDMA2k_AnalyzeIQ1WaveformSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], char resultName[], float64 x0, float64 dx, float32 iqI[], float32 iqQ[], int32 arraySize, int32 reset, int64 reserved)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function or the RFmxInstr Initialize function with option string as "AnalysisOnly=1". |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. The result name can either be specified through this input or the Result Name parameter. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name in this input, either the result name specified by Result Name parameter or the default result instance is used. The default is "" (empty string).Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxCDMA2k Build Signal String function to build the selector string. |
| resultName | [in] | char[] | This parameter specifies the name to be associated with measurement results. Provide a unique name, such as "r1" to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. The default value is "" (empty string) which refers to default result instance.Example:"result::r1""r1" |
| x0 | [in] | float64 | This parameter specifies the start time of the input Y array. This value is expressed in seconds. |
| dx | [in] | float64 | This parameter specifies the time interval between the samples in the input Y array. This value is expressed in seconds. The reciprocal of dx indicates the I/Q rate of the input signal. |
| iqI | [in] | float32[] | This parameter Specifies the real part of array of complex-valued time domain data. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively. |
| iqQ | [in] | float32[] | This parameter Specifies the imaginary part of array of complex-valued time domain data. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively. |
| arraySize | [in] | int32 | Specifies the size of the array. |
| reset | [in] | int32 | This parameter resets measurement averaging. If you enable averaging, set this parameter to TRUE for first record and FALSE for subsequent records. |
| reserved | [in] | int64 | Reserved for future use. Any value passed to this parameter will be ignored. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Analyze2

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__build__string.html language=enus -->
## TOPIC 00218: Build String

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__build__string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__build__string.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxCDMA2k_BuildChannelStringCreates a selector string to use with channel configuration. RFmxCDMA2k_BuildOffsetStringCreates the offset string to use as the selector string with the SEM and ACP offset configuration for fetch attributes and functions. RFmxCDMA2k

### Build String

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxCDMA2k_BuildChannelString | Creates a selector string to use with channel configuration. |
| RFmxCDMA2k_BuildOffsetString | Creates the offset string to use as the selector string with the SEM and ACP offset configuration for fetch attributes and functions. |
| RFmxCDMA2k_BuildSignalString | Creates a selector string to use with configuration or fetch attributes and functions. |

#### Attachments

None

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__build__string_1ga1d1ad5f9d781c46152742e98f83efebc.html language=enus -->
## TOPIC 00219: RFmxCDMA2k_BuildOffsetString

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__build__string_1ga1d1ad5f9d781c46152742e98f83efebc.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__build__string_1ga1d1ad5f9d781c46152742e98f83efebc.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates the offset string to use as the selector string with the SEM and ACP offset configuration for fetch attributes and functions. Syntaxint32 __stdcall RFmxCDMA2k_BuildOffsetString(char selectorString[], int32 offsetNumber, int32 selectorStringOutLength, char selectorStringOut[])RemarksRefer to

### RFmxCDMA2k_BuildOffsetString

Creates the offset string to use as the selector string with the SEM and ACP offset configuration for fetch attributes and functions.

#### Syntax

int32 __stdcall RFmxCDMA2k_BuildOffsetString(char selectorString[], int32 offsetNumber, int32 selectorStringOutLength, char selectorStringOut[])

#### Remarks

Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| offsetNumber | [in] | int32 | This parameter specifies the offset number used to build the selector string. |
| selectorStringOutLength | [out] | int32 | Specifies the length of the string that is returned by the selectorStringOut parameter. To get the minimum buffer size required to build the selector string, set the selectorStringOutLength parameter to 0. |
| selectorStringOut | [out] | char[] | This parameter returns the Selector String that can be passed to the Selector String input on Configure functions, Initiate functions, and Fetch functions. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Build String

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__build__string_1ga2427b9fd7402268c6da7c38f56a7a3b5.html language=enus -->
## TOPIC 00220: RFmxCDMA2k_BuildSignalString

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__build__string_1ga2427b9fd7402268c6da7c38f56a7a3b5.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__build__string_1ga2427b9fd7402268c6da7c38f56a7a3b5.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a selector string to use with configuration or fetch attributes and functions. Syntaxint32 __stdcall RFmxCDMA2k_BuildSignalString(char signalName[], char resultName[], int32 selectorStringLength, char selectorString[])RemarksRefer to the Selector String topic for information about the string

### RFmxCDMA2k_BuildSignalString

Creates a selector string to use with configuration or fetch attributes and functions.

#### Syntax

int32 __stdcall RFmxCDMA2k_BuildSignalString(char signalName[], char resultName[], int32 selectorStringLength, char selectorString[])

#### Remarks

Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| signalName | [in] | char[] | This parameter specifies the name of the signal when using named signal configurations. This input accepts the signal name with or without the "signal::" prefix. The default value is "" (empty string).Examples:"""signal::sig1""sig1" |
| resultName | [in] | char[] | This parameter specifies the name of the result when performing overlapped measurements. This input accepts the result name with or without the "result::" prefix. The default value is "" (empty string).Examples:"""result::r1""r1" |
| selectorStringLength | [in] | int32 | Specifies the length of the selector string. Set this parameter to 0 to get the minimum buffer size required to build the selector string. |
| selectorString | [in] | char[] | This parameter returns the selector string you can use in the input to Configuration functions, Fetch functions, or other functions that build selector strings. This string contains the signal and/or result names with their appropriate prefixes.Examples:"signal::sig1""result::r1""signal::sig1/result::r1" |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Build String

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__build__string_1ga28fd6b0e3405ee5ba91fc1df4011fe5f.html language=enus -->
## TOPIC 00221: RFmxCDMA2k_BuildChannelString

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__build__string_1ga28fd6b0e3405ee5ba91fc1df4011fe5f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__build__string_1ga28fd6b0e3405ee5ba91fc1df4011fe5f.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a selector string to use with channel configuration. Syntaxint32 __stdcall RFmxCDMA2k_BuildChannelString(char selectorString[], int32 channelNumber, int32 selectorStringOutLength, char selectorStringOut[])RemarksRefer to the Selector String topic for information about the string syntax for n

### RFmxCDMA2k_BuildChannelString

Creates a selector string to use with channel configuration.

#### Syntax

int32 __stdcall RFmxCDMA2k_BuildChannelString(char selectorString[], int32 channelNumber, int32 selectorStringOutLength, char selectorStringOut[])

#### Remarks

Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| channelNumber | [in] | int32 | This parameter specifies the channel number used to build the selector string. |
| selectorStringOutLength | [out] | int32 | Specifies the length of the string that is returned by the selectorStringOut parameter. To get the minimum buffer size required to build the selector string, set the selectorStringOutLength parameter to 0. |
| selectorStringOut | [out] | char[] | This parameter returns the Selector String that can be passed to the Selector String input on Configure functions, Initiate functions, and Fetch functions. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Build String

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__configuration.html language=enus -->
## TOPIC 00222: Configuration

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__configuration.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__configuration.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsACPCDACHPFrequencyModAccOBWQEVMSEMSlotPhaseSlotPowerTriggerGroup membersNameDescriptionRFmxCDMA2k_AutoLevelExamines the input signal to calculate the peak power level and sets it as the value of the RFMXCDMA2K_ATTR_REFERENCE_LEVEL attribute. Use this function to calculate an approximate settin

### Configuration

#### Groups

- ACP
- CDA
- CHP
- Frequency
- ModAcc
- OBW
- QEVM
- SEM
- SlotPhase
- SlotPower
- Trigger

#### Group members

| Name | Description |
| --- | --- |
| RFmxCDMA2k_AutoLevel | Examines the input signal to calculate the peak power level and sets it as the value of the RFMXCDMA2K_ATTR_REFERENCE_LEVEL attribute. Use this function to calculate an approximate setting for the reference level. |
| RFmxCDMA2k_CfgBandClass | Configures the band class used for the measurement. |
| RFmxCDMA2k_CfgChannelConfigurationMode | Configures RFmx CDMA2k to detect the channels automatically or to use a specified channel configuration. |
| RFmxCDMA2k_CfgExternalAttenuation | Specifies any external attenuation to be considered by RFmx CDMA2k measurements, such as the attenuation of a switch or cable connected to the signal analyzer RF IN connector. |
| RFmxCDMA2k_CfgFrequencyReference | Configures the Reference Clock and the frequency reference source. |
| RFmxCDMA2k_CfgMechanicalAttenuation | Configures the mechanical attenuation and the RFmx driver attenuation hardware settings. |
| RFmxCDMA2k_CfgNumberOfChannels | Configures the number of channels for the user-defined channel configuration when you set the RFMXCDMA2K_ATTR_CHANNEL_CONFIGURATION_MODE attribute to User Defined. |
| RFmxCDMA2k_CfgRF | Configures the RF attributes of the signal specified by the Selector String parameter. |
| RFmxCDMA2k_CfgRFAttenuation | Configures the nominal attenuation and the RFmx driver setting. |
| RFmxCDMA2k_CfgRadioConfiguration | Configures the radio configuration of the CDMA2k signal. |
| RFmxCDMA2k_CfgReferenceLevel | Configures the reference level. The reference level represents the maximum expected power of an input RF signal. |
| RFmxCDMA2k_CfgUplinkSpreading | Configures the scrambling code used for the uplink transmission. |
| RFmxCDMA2k_CfgUserDefinedChannel | Configures an individual user-defined channel when the channel configuration mode is set to User Defined. |
| RFmxCDMA2k_CfgUserDefinedChannelArray | Configures all user-defined channels when you set the RFMXCDMA2K_ATTR_CHANNEL_CONFIGURATION_MODE attribute to User Defined. |
| RFmxCDMA2k_SendSoftwareEdgeTrigger | Sends a trigger to the device when you use the RFmxCDMA2k Configure Trigger function to choose a software version of a trigger and the device is waiting for the trigger to be sent. You can also use this function to override a hardware trigger. |

#### Attachments

None

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__configuration_1ga07d0c7b1e4c74100c1921a9cd14e9876.html language=enus -->
## TOPIC 00223: RFmxCDMA2k_CfgRFAttenuation

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__configuration_1ga07d0c7b1e4c74100c1921a9cd14e9876.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__configuration_1ga07d0c7b1e4c74100c1921a9cd14e9876.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the nominal attenuation and the RFmx driver setting. Syntaxint32 __stdcall RFmxCDMA2k_CfgRFAttenuation(niRFmxInstrHandle instrumentHandle, char channelName[], int32 rfAttenuationAuto, float64 rfAttenuationValue)RemarksThis function is a wrapper over the RFmx Instruments API, and calls the

### RFmxCDMA2k_CfgRFAttenuation

Configures the nominal attenuation and the RFmx driver setting.

#### Syntax

int32 __stdcall RFmxCDMA2k_CfgRFAttenuation(niRFmxInstrHandle instrumentHandle, char channelName[], int32 rfAttenuationAuto, float64 rfAttenuationValue)

#### Remarks

This function is a wrapper over the RFmx Instruments API, and calls the [RFmxInstr_CfgRFAttenuation](/csh?context=rfmxinstr_rfmxinstrcref_function_cfg_rf_attenuation) function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxCDMA2k_Initialize function. |
| channelName | [in] | char[] | Set this parameter to "" (empty string) or NULL. |
| rfAttenuationAuto | [in] | int32 | Specifies whether the RFmx driver computes the RF attenuation.ValueDescriptionRFMXCDMA2K_VAL_RF_ATTENUATION_AUTO_FALSE (0)Specifies that the RFmx driver uses the value configured using the rfAttenuationValue parameter.RFMXCDMA2K_VAL_RF_ATTENUATION_AUTO_TRUE (1)Specifies that the RFmx driver computes the RF attenuation automatically. |
| Value | Description |  |  |
| RFMXCDMA2K_VAL_RF_ATTENUATION_AUTO_FALSE (0) | Specifies that the RFmx driver uses the value configured using the rfAttenuationValue parameter. |  |  |
| RFMXCDMA2K_VAL_RF_ATTENUATION_AUTO_TRUE (1) | Specifies that the RFmx driver computes the RF attenuation automatically. |  |  |
| rfAttenuationValue | [in] | float64 | Specifies the nominal attenuation setting, in dB, for all attenuators before the first mixer in the RF signal chain when the rfAttenuationAuto parameter is set to RFMXCDMA2K_VAL_RF_ATTENUATION_AUTO_FALSE. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__configuration_1ga175ba0cb1f69fa57acc314d537f76756.html language=enus -->
## TOPIC 00224: RFmxCDMA2k_CfgUserDefinedChannelArray

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__configuration_1ga175ba0cb1f69fa57acc314d537f76756.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__configuration_1ga175ba0cb1f69fa57acc314d537f76756.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures all user-defined channels when you set the RFMXCDMA2K_ATTR_CHANNEL_CONFIGURATION_MODE attribute to User Defined. Syntaxint32 __stdcall RFmxCDMA2k_CfgUserDefinedChannelArray(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 walshCodeLength[], int32 walshCodeNumber[], int32 b

### RFmxCDMA2k_CfgUserDefinedChannelArray

Configures all user-defined channels when you set the [RFMXCDMA2K_ATTR_CHANNEL_CONFIGURATION_MODE](group____root__ni_r_fmx_c_d_m_a2k__attributes__channel_1ga3c88eb1dedd8333791a4fdde39fcdb76.html) attribute to **User Defined**.

#### Syntax

int32 __stdcall RFmxCDMA2k_CfgUserDefinedChannelArray(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 walshCodeLength[], int32 walshCodeNumber[], int32 branch[], int32 numberOfElements)

#### Remarks

Use equal-sized arrays for **Walsh Code Length**, **Walsh Code Number**, and **Branch**.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Examples:"""signal::sig1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| walshCodeLength | [in] | int32[] | This parameter specifies an array of the Walsh code length of the CDMA2k signal. The default value is 64. |
| walshCodeNumber | [in] | int32[] | This parameter specifies an array of the Walsh code number of the CDMA2k signal. The default value is 0. |
| branch | [in] | int32[] | This parameter specifies an array of the branch on which a specific user-defined channel is mapped. The default value is I.Name (value)DescriptionI (0)Specifies the in-phase branch.Q (1)Specifies the quadrature branch.I and Q (2)Specifies the in-phase and quadrature branch. |
| Name (value) | Description |  |  |
| I (0) | Specifies the in-phase branch. |  |  |
| Q (1) | Specifies the quadrature branch. |  |  |
| I and Q (2) | Specifies the in-phase and quadrature branch. |  |  |
| numberOfElements | [in] | int32 | Specifies the number of elements in each array. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__configuration_1ga1e8bf06cc148d69589a80c969789c9ac.html language=enus -->
## TOPIC 00225: RFmxCDMA2k_CfgRadioConfiguration

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__configuration_1ga1e8bf06cc148d69589a80c969789c9ac.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__configuration_1ga1e8bf06cc148d69589a80c969789c9ac.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the radio configuration of the CDMA2k signal. Syntaxint32 __stdcall RFmxCDMA2k_CfgRadioConfiguration(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 radioConfiguration)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifies the

### RFmxCDMA2k_CfgRadioConfiguration

Configures the radio configuration of the CDMA2k signal.

#### Syntax

int32 __stdcall RFmxCDMA2k_CfgRadioConfiguration(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 radioConfiguration)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Examples:"""signal::sig1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| radioConfiguration | [in] | int32 | This parameter specifies the radio configuration of the CDMA2k signal to be analyzed. The default value is RC3.Name (value)DescriptionRC1 (0)For Uplink, Radio configuration 1 includes 64-ary orthogonal modulation, reverse fundamental channel (R-FCH) and reverse supplemental code channels (R-SCCHs). For Downlink, Radio Configuration 1 includes binary phase-shift keying (BPSK), forward fundamental channels (F-FCHs) and forward supplemental channels (F-SCHs).RC2 (1)For Uplink, Radio configuration 2 includes 64-ary orthogonal modulation, R-FCH and R-SCCHs. For Downlink, Radio Configuration 2 includes BPSKs, F-FCHs and F-SCHs.RC3 (2)For Uplink, Radio configuration 3 includes binary phase shift keying (BPSK), R-FCH and reverse supplemental channels (R-SCHs). For Downlink, Radio Configuration 3 includes quadrature phase-shift keying (QPSK), F-FCHs and F-SCHs.RC4 (3)For Uplink, Radio configuration 4 includes BPSK, R-FCH and R-SCHs. For Downlink, Radio Configuration 4 includes QPSK, F-FCHs and F-SCHs.RC5 (4)For Uplink, Radio configuration 5 is not supported. For Downlink, Radio Configuration 5 includes QPSK, F-FCHs and F-SCHs. |
| Name (value) | Description |  |  |
| RC1 (0) | For Uplink, Radio configuration 1 includes 64-ary orthogonal modulation, reverse fundamental channel (R-FCH) and reverse supplemental code channels (R-SCCHs). For Downlink, Radio Configuration 1 includes binary phase-shift keying (BPSK), forward fundamental channels (F-FCHs) and forward supplemental channels (F-SCHs). |  |  |
| RC2 (1) | For Uplink, Radio configuration 2 includes 64-ary orthogonal modulation, R-FCH and R-SCCHs. For Downlink, Radio Configuration 2 includes BPSKs, F-FCHs and F-SCHs. |  |  |
| RC3 (2) | For Uplink, Radio configuration 3 includes binary phase shift keying (BPSK), R-FCH and reverse supplemental channels (R-SCHs). For Downlink, Radio Configuration 3 includes quadrature phase-shift keying (QPSK), F-FCHs and F-SCHs. |  |  |
| RC4 (3) | For Uplink, Radio configuration 4 includes BPSK, R-FCH and R-SCHs. For Downlink, Radio Configuration 4 includes QPSK, F-FCHs and F-SCHs. |  |  |
| RC5 (4) | For Uplink, Radio configuration 5 is not supported. For Downlink, Radio Configuration 5 includes QPSK, F-FCHs and F-SCHs. |  |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__configuration_1ga2e24e1b9bb79e4f44b457d1c1810cc89.html language=enus -->
## TOPIC 00226: RFmxCDMA2k_CfgChannelConfigurationMode

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__configuration_1ga2e24e1b9bb79e4f44b457d1c1810cc89.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__configuration_1ga2e24e1b9bb79e4f44b457d1c1810cc89.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures RFmx CDMA2k to detect the channels automatically or to use a specified channel configuration. Syntaxint32 __stdcall RFmxCDMA2k_CfgChannelConfigurationMode(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 channelConfigurationMode)ParametersNameDirectionTypeDescriptioninstru

### RFmxCDMA2k_CfgChannelConfigurationMode

Configures RFmx CDMA2k to detect the channels automatically or to use a specified channel configuration.

#### Syntax

int32 __stdcall RFmxCDMA2k_CfgChannelConfigurationMode(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 channelConfigurationMode)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Examples:"""signal::sig1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| channelConfigurationMode | [in] | int32 | This parameter specifies whether to detect the channels automatically or to use a specified channel configuration.This parameter has no effect if radio configuration 1 or 2 (RC1 or RC2) is configured, as RC1 and RC2 always use a single 64-ary Walsh-modulated channel.Name (value)DescriptionAuto Detect (0)Specifies that the system automatically detects the channels.User Defined (1)Specifies that the system uses a specific channel configuration. This mode increases measurement speed because no time is spent on channel detection. |
| Name (value) | Description |  |  |
| Auto Detect (0) | Specifies that the system automatically detects the channels. |  |  |
| User Defined (1) | Specifies that the system uses a specific channel configuration. This mode increases measurement speed because no time is spent on channel detection. |  |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__configuration_1ga478bc83a1edf2e0a3cf560e224680a27.html language=enus -->
## TOPIC 00227: RFmxCDMA2k_CfgExternalAttenuation

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__configuration_1ga478bc83a1edf2e0a3cf560e224680a27.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__configuration_1ga478bc83a1edf2e0a3cf560e224680a27.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies any external attenuation to be considered by RFmx CDMA2k measurements, such as the attenuation of a switch or cable connected to the signal analyzer RF IN connector. Syntaxint32 __stdcall RFmxCDMA2k_CfgExternalAttenuation(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 e

### RFmxCDMA2k_CfgExternalAttenuation

Specifies any external attenuation to be considered by RFmx CDMA2k measurements, such as the attenuation of a switch or cable connected to the signal analyzer RF IN connector.

#### Syntax

int32 __stdcall RFmxCDMA2k_CfgExternalAttenuation(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 externalAttenuation)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Examples:"""signal::sig1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| externalAttenuation | [in] | float64 | This parameter specifies the attenuation of a switch or cable connected to the signal analyzer RF IN connector. This value is expressed in dB. The default value is 0 dB.For more information about attenuation, refer to the RF Attenuation and Signal Levels topic for your device in the NI RF Vector Signal Analyzers Help. The default value is 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__configuration_1ga47a079b10aa72fc08394f2233d59aad0.html language=enus -->
## TOPIC 00228: RFmxCDMA2k_SendSoftwareEdgeTrigger

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__configuration_1ga47a079b10aa72fc08394f2233d59aad0.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__configuration_1ga47a079b10aa72fc08394f2233d59aad0.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sends a trigger to the device when you use the RFmxCDMA2k Configure Trigger function to choose a software version of a trigger and the device is waiting for the trigger to be sent. You can also use this function to override a hardware trigger. Syntaxint32 __stdcall RFmxCDMA2k_SendSoftwareEdgeTrigger

### RFmxCDMA2k_SendSoftwareEdgeTrigger

Sends a trigger to the device when you use the RFmxCDMA2k Configure Trigger function to choose a software version of a trigger and the device is waiting for the trigger to be sent. You can also use this function to override a hardware trigger.

#### Syntax

int32 __stdcall RFmxCDMA2k_SendSoftwareEdgeTrigger(niRFmxInstrHandle instrumentHandle)

#### Remarks

- You configure an invalid trigger.
- You have not previously called the [RFmxCDMA2k_Initiate](group____root__ni_r_fmx_c_d_m_a2k__functions_1gafb56460158bf0121f9bf319265307435.html) function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__configuration_1ga502f9b0bcefe42b9f6b9692ced74319d.html language=enus -->
## TOPIC 00229: RFmxCDMA2k_CfgUplinkSpreading

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__configuration_1ga502f9b0bcefe42b9f6b9692ced74319d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__configuration_1ga502f9b0bcefe42b9f6b9692ced74319d.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the scrambling code used for the uplink transmission. Syntaxint32 __stdcall RFmxCDMA2k_CfgUplinkSpreading(niRFmxInstrHandle instrumentHandle, char selectorString[], int64 uplinkSpreadingLongCodeMask)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter

### RFmxCDMA2k_CfgUplinkSpreading

Configures the scrambling code used for the uplink transmission.

#### Syntax

int32 __stdcall RFmxCDMA2k_CfgUplinkSpreading(niRFmxInstrHandle instrumentHandle, char selectorString[], int64 uplinkSpreadingLongCodeMask)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Examples:"""signal::sig1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| uplinkSpreadingLongCodeMask | [in] | int64 | This parameter specifies the long code mask for uplink spreading. This number is a 42-bit binary number, represented as a 64-bit integer. The default value is 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__configuration_1gaa3b35a1146f4f0a19d8fabd435a9f2e6.html language=enus -->
## TOPIC 00230: RFmxCDMA2k_CfgNumberOfChannels

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__configuration_1gaa3b35a1146f4f0a19d8fabd435a9f2e6.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__configuration_1gaa3b35a1146f4f0a19d8fabd435a9f2e6.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the number of channels for the user-defined channel configuration when you set the RFMXCDMA2K_ATTR_CHANNEL_CONFIGURATION_MODE attribute to User Defined. Syntaxint32 __stdcall RFmxCDMA2k_CfgNumberOfChannels(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 numberOfChannels)P

### RFmxCDMA2k_CfgNumberOfChannels

Configures the number of channels for the user-defined channel configuration when you set the [RFMXCDMA2K_ATTR_CHANNEL_CONFIGURATION_MODE](group____root__ni_r_fmx_c_d_m_a2k__attributes__channel_1ga3c88eb1dedd8333791a4fdde39fcdb76.html) attribute to **User Defined**.

#### Syntax

int32 __stdcall RFmxCDMA2k_CfgNumberOfChannels(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 numberOfChannels)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Examples:"""signal::sig1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| numberOfChannels | [in] | int32 | This parameter specifies the number of user-defined channels. The default value is 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__configuration_1gaa5b823e8de80410c79ed1a96a846140a.html language=enus -->
## TOPIC 00231: RFmxCDMA2k_CfgBandClass

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__configuration_1gaa5b823e8de80410c79ed1a96a846140a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__configuration_1gaa5b823e8de80410c79ed1a96a846140a.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the band class used for the measurement. Syntaxint32 __stdcall RFmxCDMA2k_CfgBandClass(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 bandClass)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifies the RFmx session refnum. Th

### RFmxCDMA2k_CfgBandClass

Configures the band class used for the measurement.

#### Syntax

int32 __stdcall RFmxCDMA2k_CfgBandClass(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 bandClass)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Examples:"""signal::sig1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| bandClass | [in] | int32 | This parameter specifies the band in which the channel is located as defined in Section: 1.5, Table 1.5-1: Band Class List, of the 3GPP2 C.S0057-F specification v1.0. The default value is 0.Name (value)Description0 (0)Specifies the 800 MHz cellular band.1 (1)Specifies the 1.8 GHz to 2.0 GHz PCS band.2 (2)Specifies the 872 MHz to 960 MHz TACS band.3 (3)Specifies the 832 MHz to 925 MHZ JTACS band.4 (4)Specifies the 1.75 GHz to 1.87 GHz Korean PCS band.5 (5)Specifies the 450 MHz NMT band.6 (6)Specifies the 2 GHz IMT-2000 band.7 (7)Specifies the upper 700 MHz PARMR band.8 (8)Specifies the 1,800 MHz to 2 GHz band.9 (9)Specifies the 900 MHz band.10 (10)Specifies the secondary 1,800 MHz band.11 (11)Specifies the 400 MHz European PAMR band.12 (12)Specifies the 800 MHz PAMR band.14 (14)Specifies the US PCS 1.9 GHz band.15 (15)Specifies the AWS band. |
| Name (value) | Description |  |  |
| 0 (0) | Specifies the 800 MHz cellular band. |  |  |
| 1 (1) | Specifies the 1.8 GHz to 2.0 GHz PCS band. |  |  |
| 2 (2) | Specifies the 872 MHz to 960 MHz TACS band. |  |  |
| 3 (3) | Specifies the 832 MHz to 925 MHZ JTACS band. |  |  |
| 4 (4) | Specifies the 1.75 GHz to 1.87 GHz Korean PCS band. |  |  |
| 5 (5) | Specifies the 450 MHz NMT band. |  |  |
| 6 (6) | Specifies the 2 GHz IMT-2000 band. |  |  |
| 7 (7) | Specifies the upper 700 MHz PARMR band. |  |  |
| 8 (8) | Specifies the 1,800 MHz to 2 GHz band. |  |  |
| 9 (9) | Specifies the 900 MHz band. |  |  |
| 10 (10) | Specifies the secondary 1,800 MHz band. |  |  |
| 11 (11) | Specifies the 400 MHz European PAMR band. |  |  |
| 12 (12) | Specifies the 800 MHz PAMR band. |  |  |
| 14 (14) | Specifies the US PCS 1.9 GHz band. |  |  |
| 15 (15) | Specifies the AWS band. |  |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__configuration_1gab86378a0c04fa5c6a251d8c6d388e337.html language=enus -->
## TOPIC 00232: RFmxCDMA2k_CfgUserDefinedChannel

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__configuration_1gab86378a0c04fa5c6a251d8c6d388e337.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__configuration_1gab86378a0c04fa5c6a251d8c6d388e337.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures an individual user-defined channel when the channel configuration mode is set to User Defined. Syntaxint32 __stdcall RFmxCDMA2k_CfgUserDefinedChannel(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 walshCodeLength, int32 walshCodeNumber, int32 branch)RemarksUse "channel<n

### RFmxCDMA2k_CfgUserDefinedChannel

Configures an individual user-defined channel when the channel configuration mode is set to **User Defined**.

#### Syntax

int32 __stdcall RFmxCDMA2k_CfgUserDefinedChannel(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 walshCodeLength, int32 walshCodeNumber, int32 branch)

#### Remarks

Use "channel<n>" as the selector string to configure this function.

A channel is defined by the Walsh code length and number and the quadrature branch on which it is mapped.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and channel number. If you do not specify the signal name, the default signal instance is used. The default value is "channel0".Examples:"channel0""signal::sig1/channel0"You can use the RFmxCDMA2k_BuildChannelString function to build the selector string. |
| walshCodeLength | [in] | int32 | This parameter specifies the Walsh code length of a specific user-defined channel. The default value is 64. |
| walshCodeNumber | [in] | int32 | This parameter specifies the Walsh code number of a specific user-defined channel. The default value is 0. |
| branch | [in] | int32 | This parameter specifies the branch on which a specific user-defined channel is mapped. The default value is I.Name (value)DescriptionI (0)Specifies the in-phase branch.Q (1)Specifies the quadrature branch.I and Q (2)Specifies the in-phase and quadrature branch. |
| Name (value) | Description |  |  |
| I (0) | Specifies the in-phase branch. |  |  |
| Q (1) | Specifies the quadrature branch. |  |  |
| I and Q (2) | Specifies the in-phase and quadrature branch. |  |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__configuration_1gabafcdbd86d097e777fdb212a893dce31.html language=enus -->
## TOPIC 00233: RFmxCDMA2k_CfgReferenceLevel

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__configuration_1gabafcdbd86d097e777fdb212a893dce31.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__configuration_1gabafcdbd86d097e777fdb212a893dce31.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the reference level. The reference level represents the maximum expected power of an input RF signal. Syntaxint32 __stdcall RFmxCDMA2k_CfgReferenceLevel(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 referenceLevel)ParametersNameDirectionTypeDescriptioninstrumentHandle

### RFmxCDMA2k_CfgReferenceLevel

Configures the reference level. The reference level represents the maximum expected power of an input RF signal.

#### Syntax

int32 __stdcall RFmxCDMA2k_CfgReferenceLevel(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 referenceLevel)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Examples:"""signal::sig1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| referenceLevel | [in] | float64 | This parameter specifies the reference level, which represents the maximum expected power of an RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices. The default value of this parameter is hardware dependent. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__configuration_1gabfbb17d885d9b441503f0f43f28ce80c.html language=enus -->
## TOPIC 00234: RFmxCDMA2k_CfgMechanicalAttenuation

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__configuration_1gabfbb17d885d9b441503f0f43f28ce80c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__configuration_1gabfbb17d885d9b441503f0f43f28ce80c.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the mechanical attenuation and the RFmx driver attenuation hardware settings. Syntaxint32 __stdcall RFmxCDMA2k_CfgMechanicalAttenuation(niRFmxInstrHandle instrumentHandle, char channelName[], int32 mechanicalAttenuationAuto, float64 mechanicalAttenuationValue)RemarksThis function is a wra

### RFmxCDMA2k_CfgMechanicalAttenuation

Configures the mechanical attenuation and the RFmx driver attenuation hardware settings.

#### Syntax

int32 __stdcall RFmxCDMA2k_CfgMechanicalAttenuation(niRFmxInstrHandle instrumentHandle, char channelName[], int32 mechanicalAttenuationAuto, float64 mechanicalAttenuationValue)

#### Remarks

This function is a wrapper over the RFmx Instruments API, and calls the [RFmxInstr_CfgMechanicalAttenuation](/csh?context=rfmxinstr_rfmxinstrcref_function_cfg_mechanical_attenuation) function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxCDMA2k_Initialize function. |
| channelName | [in] | char[] | Set this parameter to "" (empty string) or NULL. |
| mechanicalAttenuationAuto | [in] | int32 | Specifies whether the RFmx driver automatically chooses an attenuation setting based on the hardware settings.ValueDescriptionRFMXCDMA2K_VAL_MECHANICAL_ATTENUATION_AUTO_FALSE (0)Specifies that the RFmx driver uses the value configured in the mechanicalAttenuationValue parameter.RFMXCDMA2K_VAL_MECHANICAL_ATTENUATION_AUTO_TRUE (1)Specifies that the measurement computes the mechanical attenuation. |
| Value | Description |  |  |
| RFMXCDMA2K_VAL_MECHANICAL_ATTENUATION_AUTO_FALSE (0) | Specifies that the RFmx driver uses the value configured in the mechanicalAttenuationValue parameter. |  |  |
| RFMXCDMA2K_VAL_MECHANICAL_ATTENUATION_AUTO_TRUE (1) | Specifies that the measurement computes the mechanical attenuation. |  |  |
| mechanicalAttenuationValue | [in] | float64 | Specifies the level of mechanical attenuation, in dB, for the RF path when the mechanicalAttenuationAuto is set to RFMXCDMA2K_VAL_MECHANICAL_ATTENUATION_AUTO_FALSE. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__configuration_1gacb3193c31cf119c88743b31295d9b4fe.html language=enus -->
## TOPIC 00235: RFmxCDMA2k_AutoLevel

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__configuration_1gacb3193c31cf119c88743b31295d9b4fe.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__configuration_1gacb3193c31cf119c88743b31295d9b4fe.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Examines the input signal to calculate the peak power level and sets it as the value of the RFMXCDMA2K_ATTR_REFERENCE_LEVEL attribute. Use this function to calculate an approximate setting for the reference level. Syntaxint32 __stdcall RFmxCDMA2k_AutoLevel(niRFmxInstrHandle instrumentHandle, char se

### RFmxCDMA2k_AutoLevel

Examines the input signal to calculate the peak power level and sets it as the value of the [RFMXCDMA2K_ATTR_REFERENCE_LEVEL](group____root__ni_r_fmx_c_d_m_a2k__attributes_1ga96e417de6d5f3b1936d0a24b4bc8e0d2.html) attribute. Use this function to calculate an approximate setting for the reference level.

#### Syntax

int32 __stdcall RFmxCDMA2k_AutoLevel(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 measurementInterval, float64 *referenceLevel)

#### Remarks

1. Resets the mixer level, mixer level offset, and IF output power offset.
2. Sets the starting reference level to the maximum reference level supported by the device based on the current RF attenuation, mechanical attenuation, and preamplifier enabled settings.
3. Iterates to adjust the reference level based on the input signal peak power.
4. Uses immediate triggering and restores the trigger settings back to user setting after the execution.

You can also specify the starting reference level using the [RFMXCDMA2K_ATTR_AUTO_LEVEL_INITIAL_REFERENCE_LEVEL](group____root__ni_r_fmx_c_d_m_a2k__attributes__advanced_1gaf9047215e61aa886ad8bd07021049d44.html) attribute.

When using NI 5663, 5665, or 5668R devices, NI recommends that you set an appropriate value for mechanical attenuation before calling the RFmxCDMA2k Auto Level function. Setting an appropriate value for mechanical attenuation reduces the number of times the attenuator settings are changed by this function; thus reducing wear and tear, and maximizing the life time of the attenuator.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Examples:"""signal::sig1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| measurementInterval | [in] | float64 | This parameter specifies the acquisition length. This value is expressed in seconds. Use this value to compute the number of samples to acquire from the signal analyzer.Auto Level function does not use any trigger for acquisition. It ignores the user-configured trigger attributes. NI recommends that you set a sufficiently high measurement interval to ensure that the acquired waveform is at least as long as one period of the signal. |
| referenceLevel | [out] | float64 * | This parameter returns the estimated peak power level of the input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices. The default value of this parameter is hardware dependent. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__configuration_1gae30dfe0c1de44193a39b2c15db841767.html language=enus -->
## TOPIC 00236: RFmxCDMA2k_CfgRF

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__configuration_1gae30dfe0c1de44193a39b2c15db841767.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__configuration_1gae30dfe0c1de44193a39b2c15db841767.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the RF attributes of the signal specified by the Selector String parameter. Syntaxint32 __stdcall RFmxCDMA2k_CfgRF(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 centerFrequency, float64 referenceLevel, float64 externalAttenuation)ParametersNameDirectionTypeDescription

### RFmxCDMA2k_CfgRF

Configures the RF attributes of the signal specified by the **Selector String** parameter.

#### Syntax

int32 __stdcall RFmxCDMA2k_CfgRF(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 centerFrequency, float64 referenceLevel, float64 externalAttenuation)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Examples:"""signal::sig1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| centerFrequency | [in] | float64 | This parameter specifies the carrier frequency of the RF signal to acquire. This value is expressed in Hz. The signal analyzer tunes to this frequency. The default value of this parameter is hardware dependent. Refer to the 3GPP2 standard C.S0057-E v1.0 for more information about bands. |
| referenceLevel | [in] | float64 | This parameter specifies the reference level, which represents the maximum expected power of an RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices. The default value of this parameter is hardware dependent. |
| externalAttenuation | [in] | float64 | This parameter specifies the attenuation of a switch or cable connected to the RF IN connector of the signal analyzer. This value is expressed in dB.For more information about attenuation, refer to the RF Attenuation and Signal Levels topic for your device in the NI RF Vector Signal Analyzers Help. The default value is 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__configuration_1gae9abf4b87a0bba6aa1c922c01e2989bc.html language=enus -->
## TOPIC 00237: RFmxCDMA2k_CfgFrequencyReference

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__configuration_1gae9abf4b87a0bba6aa1c922c01e2989bc.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__configuration_1gae9abf4b87a0bba6aa1c922c01e2989bc.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the Reference Clock and the frequency reference source. Syntaxint32 __stdcall RFmxCDMA2k_CfgFrequencyReference(niRFmxInstrHandle instrumentHandle, char channelName[], char frequencyReferenceSource[], float64 frequencyReferenceFrequency)RemarksThis function is a wrapper over the RFmx Instr

### RFmxCDMA2k_CfgFrequencyReference

Configures the Reference Clock and the frequency reference source.

#### Syntax

int32 __stdcall RFmxCDMA2k_CfgFrequencyReference(niRFmxInstrHandle instrumentHandle, char channelName[], char frequencyReferenceSource[], float64 frequencyReferenceFrequency)

#### Remarks

This function is a wrapper over the RFmx Instruments API, and calls the [RFmxInstr_CfgFrequencyReference](/csh?context=rfmxinstr_rfmxinstrcref_function_cfg_frequency_reference) function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxCDMA2k_Initialize function. |
| channelName | [in] | char[] | Set this parameter to "" (empty string) or NULL. |
| frequencyReferenceSource | [in] | char[] | Specifies the frequency reference source.ValueDescriptionRFMXCDMA2K_VAL_ONBOARD_CLOCK_STR ("Onboard Clock")PXIe-5663/5663E: The RFmx driver locks the PXIe-5663/5663E to the PXIe-5652 LO source onboard clock. Connect the REF OUT2 connector (if it exists) on the PXIe-5652 to the PXIe-5622 CLK IN terminal. On versions of the PXIe-5663/5663E that lack a REF OUT2 connector on the PXIe-5652, connect the REF IN/OUT connector on the PXIe-5652 to the PXIe-5622 CLK IN terminal.PXIe-5665: The RFmx driver locks the PXIe-5665 to the PXIe-5653 LO source onboard clock. Connect the 100 MHz REF OUT terminal on the PXIe-5653 to the PXIe-5622 CLK IN terminal.PXIe-5644R/5645R/5646R, PXIe-5840: The RFmx driver locks the device to its onboard clock.RFMXCDMA2K_VAL_REF_IN_STR ("RefIn")PXIe-5663/5663E: Connect the external signal to the PXIe-5652 REF IN/OUT connector. Connect the REF OUT2 connector (if it exists) on the PXIe-5652 to the PXIe-5622 CLK IN terminal.PXIe-5665: Connect the external signal to the PXIe-5653 REF IN connector. Connect the 100 MHz REF OUT terminal on the PXIe-5653 to the PXIe-5622 CLK IN connector. If your external clock signal frequency is set to a frequency other than 10 MHz, set the frequencyReferenceFrequency parameter according to the frequency of your external clock signal.PXIe-5644R/5645R/5646R, PXIe-5840: The RFmx driver locks the device to the signal at the external REF IN connector.RFMXCDMA2K_VAL_PXI_CLK_STR ("PXI_Clk")PXIe-5644R/5645R/5646R, PXIe-5663/5663E/5665, PXIe-5840: The RFmx driver locks the PXIe-5644R/5645R/5646R, PXIe-5663/5663E/5665 to the PXI backplane clock.RFMXCDMA2K_VAL_CLK_IN_STR ("ClkIn")PXIe-5663/5663E: The RFmx driver locks the PXIe-5663/5663E to an external 10 MHz signal. Connect the external signal to the PXIe-5622 CLK IN connector, and connect the PXIe-5622 CLK OUT connector to the FREQ REF IN connector on the PXIe-5652.PXIe-5665: The RFmx driver locks the PXIe-5665 to an external 100 MHz signal. Connect the external signal to the PXIe-5622 CLK IN connector, and connect the PXIe-5622 CLK OUT connector to the REF IN connector on the PXIe-5653. Set the frequencyReferenceFrequency parameter to 100 MHz.PXIe-5644R/5645R/5646R, PXIe-5840: This configuration does not apply to the PXIe-5644R/5645R/5646R. |
| Value | Description |  |  |
| RFMXCDMA2K_VAL_ONBOARD_CLOCK_STR ("Onboard Clock") | PXIe-5663/5663E: The RFmx driver locks the PXIe-5663/5663E to the PXIe-5652 LO source onboard clock. Connect the REF OUT2 connector (if it exists) on the PXIe-5652 to the PXIe-5622 CLK IN terminal. On versions of the PXIe-5663/5663E that lack a REF OUT2 connector on the PXIe-5652, connect the REF IN/OUT connector on the PXIe-5652 to the PXIe-5622 CLK IN terminal.PXIe-5665: The RFmx driver locks the PXIe-5665 to the PXIe-5653 LO source onboard clock. Connect the 100 MHz REF OUT terminal on the PXIe-5653 to the PXIe-5622 CLK IN terminal.PXIe-5644R/5645R/5646R, PXIe-5840: The RFmx driver locks the device to its onboard clock. |  |  |
| RFMXCDMA2K_VAL_REF_IN_STR ("RefIn") | PXIe-5663/5663E: Connect the external signal to the PXIe-5652 REF IN/OUT connector. Connect the REF OUT2 connector (if it exists) on the PXIe-5652 to the PXIe-5622 CLK IN terminal.PXIe-5665: Connect the external signal to the PXIe-5653 REF IN connector. Connect the 100 MHz REF OUT terminal on the PXIe-5653 to the PXIe-5622 CLK IN connector. If your external clock signal frequency is set to a frequency other than 10 MHz, set the frequencyReferenceFrequency parameter according to the frequency of your external clock signal.PXIe-5644R/5645R/5646R, PXIe-5840: The RFmx driver locks the device to the signal at the external REF IN connector. |  |  |
| RFMXCDMA2K_VAL_PXI_CLK_STR ("PXI_Clk") | PXIe-5644R/5645R/5646R, PXIe-5663/5663E/5665, PXIe-5840: The RFmx driver locks the PXIe-5644R/5645R/5646R, PXIe-5663/5663E/5665 to the PXI backplane clock. |  |  |
| RFMXCDMA2K_VAL_CLK_IN_STR ("ClkIn") | PXIe-5663/5663E: The RFmx driver locks the PXIe-5663/5663E to an external 10 MHz signal. Connect the external signal to the PXIe-5622 CLK IN connector, and connect the PXIe-5622 CLK OUT connector to the FREQ REF IN connector on the PXIe-5652.PXIe-5665: The RFmx driver locks the PXIe-5665 to an external 100 MHz signal. Connect the external signal to the PXIe-5622 CLK IN connector, and connect the PXIe-5622 CLK OUT connector to the REF IN connector on the PXIe-5653. Set the frequencyReferenceFrequency parameter to 100 MHz.PXIe-5644R/5645R/5646R, PXIe-5840: This configuration does not apply to the PXIe-5644R/5645R/5646R. |  |  |
| frequencyReferenceFrequency | [in] | float64 | Specifies the Reference Clock rate, in Hz, when the frequencyReferenceSource parameter is set to RFMXCDMA2K_VAL_CLK_IN_STR or RFMXCDMA2K_VAL_REF_IN_STR. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__configuration__acp.html language=enus -->
## TOPIC 00238: ACP

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__configuration__acp.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__configuration__acp.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxCDMA2k_ACPCfgAveragingConfigures averaging for the ACP measurement. RFmxCDMA2k_ACPCfgMeasurementMethodConfigures the method for performing the ACP measurement. RFmxCDMA2k_ACPCfgNoiseCompensationEnabledConfigures channel power compensation for the inherent no

### ACP

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxCDMA2k_ACPCfgAveraging | Configures averaging for the ACP measurement. |
| RFmxCDMA2k_ACPCfgMeasurementMethod | Configures the method for performing the ACP measurement. |
| RFmxCDMA2k_ACPCfgNoiseCompensationEnabled | Configures channel power compensation for the inherent noise floor of the signal analyzer. |
| RFmxCDMA2k_ACPCfgNumberOfOffsets | Configures the number of offsets for the ACP measurement. |
| RFmxCDMA2k_ACPCfgRBWFilter | Configures the RBW filter. |
| RFmxCDMA2k_ACPCfgSweepTime | Configures the sweep time. |

#### Attachments

None

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__configuration__acp_1ga0aeed905e2a38c1bad6996d721597edf.html language=enus -->
## TOPIC 00239: RFmxCDMA2k_ACPCfgAveraging

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__configuration__acp_1ga0aeed905e2a38c1bad6996d721597edf.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__configuration__acp_1ga0aeed905e2a38c1bad6996d721597edf.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures averaging for the ACP measurement. Syntaxint32 __stdcall RFmxCDMA2k_ACPCfgAveraging(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 averagingEnabled, int32 averagingCount, int32 averagingType)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis

### RFmxCDMA2k_ACPCfgAveraging

Configures averaging for the ACP measurement.

#### Syntax

int32 __stdcall RFmxCDMA2k_ACPCfgAveraging(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 averagingEnabled, int32 averagingCount, int32 averagingType)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Examples:"""signal::sig1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| averagingEnabled | [in] | int32 | This parameter specifies whether to enable averaging for the measurement. The default value is False.Name (value)DescriptionFalse (0)The measurement is performed on a single acquisition.True (1)The ACP measurement uses the Averaging Count parameter to calculate the number of acquisitions over which the ACP measurement is averaged. |
| Name (value) | Description |  |  |
| False (0) | The measurement is performed on a single acquisition. |  |  |
| True (1) | The ACP measurement uses the Averaging Count parameter to calculate the number of acquisitions over which the ACP measurement is averaged. |  |  |
| averagingCount | [in] | int32 | This parameter specifies the number of acquisitions used for averaging when you set the Averaging Enabled parameter to True. The default value is 10. |
| averagingType | [in] | int32 | This parameter specifies the averaging type for averaging multiple spectrum acquisitions. RFmx uses the averaged spectrum for the measurement.The default value is RMS.Name (value)DescriptionRMS (0)The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor.Log (1)The power spectrum is averaged in a logarithmic scale.Scalar (2)The square root of the power spectrum is averaged.Max (3)The peak power in the spectrum at each frequency bin is retained from one acquisition to the next.Min (4)The least power in the spectrum at each frequency bin is retained from one acquisition to the next.Refer to the Averaging section of the Spectrum topic for more information about averaging types. |
| Name (value) | Description |  |  |
| RMS (0) | The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. |  |  |
| Log (1) | The power spectrum is averaged in a logarithmic scale. |  |  |
| Scalar (2) | The square root of the power spectrum is averaged. |  |  |
| Max (3) | The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. |  |  |
| Min (4) | The least power in the spectrum at each frequency bin is retained from one acquisition to the next. |  |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ACP

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__configuration__acp_1ga2ba74f3b03bd59d3378bd4c57ef6fb42.html language=enus -->
## TOPIC 00240: RFmxCDMA2k_ACPCfgSweepTime

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__configuration__acp_1ga2ba74f3b03bd59d3378bd4c57ef6fb42.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__configuration__acp_1ga2ba74f3b03bd59d3378bd4c57ef6fb42.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the sweep time. Syntaxint32 __stdcall RFmxCDMA2k_ACPCfgSweepTime(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 sweepTimeAuto, float64 sweepTimeInterval)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifies the RFmx session r

### RFmxCDMA2k_ACPCfgSweepTime

Configures the sweep time.

#### Syntax

int32 __stdcall RFmxCDMA2k_ACPCfgSweepTime(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 sweepTimeAuto, float64 sweepTimeInterval)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Examples:"""signal::sig1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| sweepTimeAuto | [in] | int32 | This parameter specifies whether the measurement computes the sweep time.Name (value)DescriptionFalse (0)The measurement uses the sweep time that you specify using the Sweep Time Interval parameter.True (1)The measurement uses the default sweep time of 0.001667 seconds. |
| Name (value) | Description |  |  |
| False (0) | The measurement uses the sweep time that you specify using the Sweep Time Interval parameter. |  |  |
| True (1) | The measurement uses the default sweep time of 0.001667 seconds. |  |  |
| sweepTimeInterval | [in] | float64 | This parameter specifies the sweep time if you set the Sweep Time Auto parameter to False. This value is expressed in seconds. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ACP

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__configuration__acp_1ga525be413a6db397a22fe74b85d97976c.html language=enus -->
## TOPIC 00241: RFmxCDMA2k_ACPCfgRBWFilter

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__configuration__acp_1ga525be413a6db397a22fe74b85d97976c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__configuration__acp_1ga525be413a6db397a22fe74b85d97976c.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the RBW filter. Syntaxint32 __stdcall RFmxCDMA2k_ACPCfgRBWFilter(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 rbwAuto, float64 rbw, int32 rbwFilterType)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifies the RFmx session

### RFmxCDMA2k_ACPCfgRBWFilter

Configures the RBW filter.

#### Syntax

int32 __stdcall RFmxCDMA2k_ACPCfgRBWFilter(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 rbwAuto, float64 rbw, int32 rbwFilterType)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Examples:"""signal::sig1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| rbwAuto | [in] | int32 | This parameter specifies whether the measurement computes the RBW.Refer to the RBW and Sweep Time section in the ACP topic for more information about RBW and sweep time.Name (value)DescriptionFalse (0)The measurement uses the RBW that you specify in the RBW parameter.True (1)The measurement computes the RBW.The default value is True. |
| Name (value) | Description |  |  |
| False (0) | The measurement uses the RBW that you specify in the RBW parameter. |  |  |
| True (1) | The measurement computes the RBW. |  |  |
| rbw | [in] | float64 | This parameter specifies the bandwidth of the RBW filter used to sweep the acquired signal if you set the RBW Auto parameter to False. This value is expressed in Hz. The default value is 10 kHz. |
| rbwFilterType | [in] | int32 | This parameter specifies the shape of the digital RBW filter. The default value is Gaussian.Name (value)DescriptionFFT Based (0)No RBW filtering is performed.Gaussian (1)An RBW filter with a Gaussian response is applied.Flat (2)An RBW filter with a flat response is applied. |
| Name (value) | Description |  |  |
| FFT Based (0) | No RBW filtering is performed. |  |  |
| Gaussian (1) | An RBW filter with a Gaussian response is applied. |  |  |
| Flat (2) | An RBW filter with a flat response is applied. |  |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ACP

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__configuration__acp_1ga73c15d2a137ee0c0bbd744f020344fa8.html language=enus -->
## TOPIC 00242: RFmxCDMA2k_ACPCfgNoiseCompensationEnabled

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__configuration__acp_1ga73c15d2a137ee0c0bbd744f020344fa8.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__configuration__acp_1ga73c15d2a137ee0c0bbd744f020344fa8.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures channel power compensation for the inherent noise floor of the signal analyzer. Syntaxint32 __stdcall RFmxCDMA2k_ACPCfgNoiseCompensationEnabled(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 noiseCompensationEnabled)ParametersNameDirectionTypeDescriptioninstrumentHandle[

### RFmxCDMA2k_ACPCfgNoiseCompensationEnabled

Configures channel power compensation for the inherent noise floor of the signal analyzer.

#### Syntax

int32 __stdcall RFmxCDMA2k_ACPCfgNoiseCompensationEnabled(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 noiseCompensationEnabled)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Examples:"""signal::sig1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| noiseCompensationEnabled | [in] | int32 | This parameter specifies whether to enable compensation of the channel powers for the inherent noise floor of the signal analyzer. The default value is False.Name (value)DescriptionFalse (0)Disables compensation of the channel powers for the noise floor of the signal analyzer.True (1)Enables compensation of the channel powers for the noise floor of the signal analyzer. The noise floor of the signal analyzer is measured for the RF path used by the ACP measurement and cached for future use. If the signal analyzer or measurement parameters change, noise floors are measured again. Supported Devices: PXIe-5663/5665/5668R, PXIe-5830/5831/5832/5842/5860 |
| Name (value) | Description |  |  |
| False (0) | Disables compensation of the channel powers for the noise floor of the signal analyzer. |  |  |
| True (1) | Enables compensation of the channel powers for the noise floor of the signal analyzer. The noise floor of the signal analyzer is measured for the RF path used by the ACP measurement and cached for future use. If the signal analyzer or measurement parameters change, noise floors are measured again. Supported Devices: PXIe-5663/5665/5668R, PXIe-5830/5831/5832/5842/5860 |  |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ACP

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__configuration__acp_1gab1cf376cf33cf3bc84d0445106267031.html language=enus -->
## TOPIC 00243: RFmxCDMA2k_ACPCfgNumberOfOffsets

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__configuration__acp_1gab1cf376cf33cf3bc84d0445106267031.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__configuration__acp_1gab1cf376cf33cf3bc84d0445106267031.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the number of offsets for the ACP measurement. Syntaxint32 __stdcall RFmxCDMA2k_ACPCfgNumberOfOffsets(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 numberOfOffsets)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifies the RF

### RFmxCDMA2k_ACPCfgNumberOfOffsets

Configures the number of offsets for the ACP measurement.

#### Syntax

int32 __stdcall RFmxCDMA2k_ACPCfgNumberOfOffsets(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 numberOfOffsets)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Examples:"""signal::sig1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| numberOfOffsets | [in] | int32 | This parameter specifies the number of offset channels. The default value is 2. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ACP

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__configuration__acp_1gad936b9914a6b955b06c62f23140a6078.html language=enus -->
## TOPIC 00244: RFmxCDMA2k_ACPCfgMeasurementMethod

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__configuration__acp_1gad936b9914a6b955b06c62f23140a6078.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__configuration__acp_1gad936b9914a6b955b06c62f23140a6078.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the method for performing the ACP measurement. Syntaxint32 __stdcall RFmxCDMA2k_ACPCfgMeasurementMethod(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 measurementMethod)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifies th

### RFmxCDMA2k_ACPCfgMeasurementMethod

Configures the method for performing the ACP measurement.

#### Syntax

int32 __stdcall RFmxCDMA2k_ACPCfgMeasurementMethod(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 measurementMethod)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Examples:"""signal::sig1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| measurementMethod | [in] | int32 | This parameter specifies the method for performing the ACP measurement. The default value is Normal.NameValueDescriptionRFMXCDMA2K_VAL_ACP_MEASUREMENT_METHOD_NORMAL0 (0x0)The ACP measurement acquires the spectrum using the same signal analyzer setting across frequency bands. Use this method when measurement speed is desirable over higher dynamic range.RFMXCDMA2K_VAL_ACP_MEASUREMENT_METHOD_DYNAMIC_RANGE1 (0x1)The ACP measurement acquires the spectrum using the hardware-specific optimizations for different frequency bands. Use this method to get the best dynamic range. Supported Devices: PXIe-5665/5668R.\| RFMXCDMA2K_VAL_ACP_MEASUREMENT_METHOD_SEQUENTIAL_FFT \| 2 (0x2) \| The ACP measurement acquires I/Q the samples specified by the RFMXCDMA2K_ATTR_ACP_SWEEP_TIME_INTERVAL. These samples are divided into smaller chunks. The size of each chunk is defined by the RFMXCDMA2K_ATTR_ACP_SEQUENTIAL_FFT_SIZE attribute, and FFT is computed for each these chunks. The resultant FFTs are averaged to get the spectrum used to compute the ACP. If the total acquired samples is not an integer multiple of the FFT size, the remaining samples at the end of the acquisition are not used. Use this method to optimize the ACP Measurement speed. The accuracy of results may be reduced when using this measurement method. For accurate power measurements when the power characteristics of the signal vary over time, averaging is allowed. The following attributes have limited support when you set the ACP Measurement Method attribute to Sequential FFT.\| Properties \| Supported Values \|\|-----------------------------------------—\|---------------—\|\| RFMXCDMA2K_ATTR_ACP_RBW_FILTER_AUTO_BANDWIDTH \| True \|\| RFMXCDMA2K_ATTR_ACP_RBW_FILTER_TYPE \| FFT Based \|\| RFMXCDMA2K_ATTR_ACP_AVERAGING_COUNT \| >=1 \|\| RFMXCDMA2K_ATTR_ACP_NUMBER_OF_ANALYSIS_THREADS \| >=1 \|Note For multi-span FFT, the averaging count should be 1.\| |
| Name | Value | Description |  |
| RFMXCDMA2K_VAL_ACP_MEASUREMENT_METHOD_NORMAL | 0 (0x0) | The ACP measurement acquires the spectrum using the same signal analyzer setting across frequency bands. Use this method when measurement speed is desirable over higher dynamic range. |  |
| RFMXCDMA2K_VAL_ACP_MEASUREMENT_METHOD_DYNAMIC_RANGE | 1 (0x1) | The ACP measurement acquires the spectrum using the hardware-specific optimizations for different frequency bands. Use this method to get the best dynamic range. Supported Devices: PXIe-5665/5668R. |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ACP

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__configuration__cda.html language=enus -->
## TOPIC 00245: CDA

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__configuration__cda.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__configuration__cda.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxCDMA2k_CDACfgMeasurementChannelConfigures the spreading factor, spreading code, modulation type, and branch of the channel to be measured. RFmxCDMA2k_CDACfgPowerUnitConfigures the Power Unit parameter for the code domain power results, except for the Total P

### CDA

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxCDMA2k_CDACfgMeasurementChannel | Configures the spreading factor, spreading code, modulation type, and branch of the channel to be measured. |
| RFmxCDMA2k_CDACfgPowerUnit | Configures the Power Unit parameter for the code domain power results, except for the Total Power parameter. |
| RFmxCDMA2k_CDACfgSynchronizationModeAndInterval | Configures the Synchronization Mode, Measurement Offset, and Measurement Length parameters for the code domain analysis (CDA) measurement. |

#### Attachments

None

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__configuration__cda_1ga275879b4f1a84744fe9b4efa0d36718a.html language=enus -->
## TOPIC 00246: RFmxCDMA2k_CDACfgSynchronizationModeAndInterval

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__configuration__cda_1ga275879b4f1a84744fe9b4efa0d36718a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__configuration__cda_1ga275879b4f1a84744fe9b4efa0d36718a.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the Synchronization Mode, Measurement Offset, and Measurement Length parameters for the code domain analysis (CDA) measurement. Syntaxint32 __stdcall RFmxCDMA2k_CDACfgSynchronizationModeAndInterval(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 synchronizationMode, int32

### RFmxCDMA2k_CDACfgSynchronizationModeAndInterval

Configures the **Synchronization Mode**, **Measurement Offset**, and **Measurement Length** parameters for the code domain analysis (CDA) measurement.

#### Syntax

int32 __stdcall RFmxCDMA2k_CDACfgSynchronizationModeAndInterval(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 synchronizationMode, int32 measurementOffset, int32 measurementLength)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Examples:"""signal::sig1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| synchronizationMode | [in] | int32 | This parameter specifies whether the measurement is performed from the frame, slot, or symbol boundary.The default value is Slot.Name (value)DescriptionFrame (0)The frame boundary is detected, and the measurement is performed over the number of slots specified by the Measurement Length parameter starting at the Measurement Offset slots from the frame boundary.Slot (1)The slot boundary is detected, and the measurement is performed over the number of slots specified by the Measurement Length parameter starting at the Measurement Offset slots from the slot boundary.Arbitrary (2)The symbol boundary is detected, and the measurement is performed over the number of slots specified by the Measurement Length parameter starting at the Measurement Offset slots from the symbol boundary. |
| Name (value) | Description |  |  |
| Frame (0) | The frame boundary is detected, and the measurement is performed over the number of slots specified by the Measurement Length parameter starting at the Measurement Offset slots from the frame boundary. |  |  |
| Slot (1) | The slot boundary is detected, and the measurement is performed over the number of slots specified by the Measurement Length parameter starting at the Measurement Offset slots from the slot boundary. |  |  |
| Arbitrary (2) | The symbol boundary is detected, and the measurement is performed over the number of slots specified by the Measurement Length parameter starting at the Measurement Offset slots from the symbol boundary. |  |  |
| measurementOffset | [in] | int32 | This parameter specifies the measurement offset to skip from the synchronization boundary. The synchronization boundary is specified by the Synchronization Mode parameter. This value is expressed in slots. |
| measurementLength | [in] | int32 | This parameter specifies the duration of code domain measurement. This value is expressed in slots.The default value is 0. The valid values are 1 to 16, inclusive. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

CDA

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__configuration__cda_1ga5a9acc19c11b99eeec94173dc8af85e9.html language=enus -->
## TOPIC 00247: RFmxCDMA2k_CDACfgMeasurementChannel

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__configuration__cda_1ga5a9acc19c11b99eeec94173dc8af85e9.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__configuration__cda_1ga5a9acc19c11b99eeec94173dc8af85e9.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the spreading factor, spreading code, modulation type, and branch of the channel to be measured. Syntaxint32 __stdcall RFmxCDMA2k_CDACfgMeasurementChannel(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 walshCodeLength, int32 walshCodeNumber, int32 branch)ParametersNameDi

### RFmxCDMA2k_CDACfgMeasurementChannel

Configures the spreading factor, spreading code, modulation type, and branch of the channel to be measured.

#### Syntax

int32 __stdcall RFmxCDMA2k_CDACfgMeasurementChannel(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 walshCodeLength, int32 walshCodeNumber, int32 branch)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Examples:"""signal::sig1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| walshCodeLength | [in] | int32 | This parameter specifies the Walsh code length of a channel subject to channel specific analysis. The default value is 64. The valid values are 2, 4, 8, 16, 32, and 64. |
| walshCodeNumber | [in] | int32 | This parameter specifies the Walsh code number of a channel subject to channel specific analysis. |
| branch | [in] | int32 | This parameter specifies the Walsh branch of a channel subject to channel specific analysis. The default value is I.Name (value)DescriptionI (0)Specifies the in-phase branch.Q (1)Specifies the quadrature branch. |
| Name (value) | Description |  |  |
| I (0) | Specifies the in-phase branch. |  |  |
| Q (1) | Specifies the quadrature branch. |  |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

CDA

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__configuration__cda_1ga8c4a11309f617e6d612d8f9265d23e85.html language=enus -->
## TOPIC 00248: RFmxCDMA2k_CDACfgPowerUnit

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__configuration__cda_1ga8c4a11309f617e6d612d8f9265d23e85.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__configuration__cda_1ga8c4a11309f617e6d612d8f9265d23e85.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the Power Unit parameter for the code domain power results, except for the Total Power parameter. Syntaxint32 __stdcall RFmxCDMA2k_CDACfgPowerUnit(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 powerUnit)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxIns

### RFmxCDMA2k_CDACfgPowerUnit

Configures the **Power Unit** parameter for the code domain power results, except for the **Total Power** parameter.

#### Syntax

int32 __stdcall RFmxCDMA2k_CDACfgPowerUnit(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 powerUnit)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Examples:"""signal::sig1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| powerUnit | [in] | int32 | This parameter specifies the measurement unit of the measured code domain power results. This value is expressed in dB/dBm. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

CDA

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__configuration__chp.html language=enus -->
## TOPIC 00249: CHP

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__configuration__chp.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__configuration__chp.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxCDMA2k_CHPCfgAveragingConfigures averaging for the CHP measurement. RFmxCDMA2k_CHPCfgRBWFilterConfigures the RBW filter. RFmxCDMA2k_CHPCfgSweepTimeConfigures the sweep time. AttachmentsNone

### CHP

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxCDMA2k_CHPCfgAveraging | Configures averaging for the CHP measurement. |
| RFmxCDMA2k_CHPCfgRBWFilter | Configures the RBW filter. |
| RFmxCDMA2k_CHPCfgSweepTime | Configures the sweep time. |

#### Attachments

None

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__configuration__chp_1ga0b86c964b810bbf5fd0dc53073eb9bcb.html language=enus -->
## TOPIC 00250: RFmxCDMA2k_CHPCfgSweepTime

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__configuration__chp_1ga0b86c964b810bbf5fd0dc53073eb9bcb.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__configuration__chp_1ga0b86c964b810bbf5fd0dc53073eb9bcb.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the sweep time. Syntaxint32 __stdcall RFmxCDMA2k_CHPCfgSweepTime(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 sweepTimeAuto, float64 sweepTimeInterval)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifies the RFmx session r

### RFmxCDMA2k_CHPCfgSweepTime

Configures the sweep time.

#### Syntax

int32 __stdcall RFmxCDMA2k_CHPCfgSweepTime(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 sweepTimeAuto, float64 sweepTimeInterval)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Examples:"""signal::sig1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| sweepTimeAuto | [in] | int32 | This parameter specifies whether the measurement computes the sweep time.The default value is True .Name (value)DescriptionFalse (0)The measurement uses the sweep time that you specify using the Sweep Time Interval parameter.True (1)The measurement uses the default sweep time of 0.001667 seconds.Refer to the RBW and Sweep Time section in the CHP topic for more information about RBW and sweep time. |
| Name (value) | Description |  |  |
| False (0) | The measurement uses the sweep time that you specify using the Sweep Time Interval parameter. |  |  |
| True (1) | The measurement uses the default sweep time of 0.001667 seconds. |  |  |
| sweepTimeInterval | [in] | float64 | This parameter specifies the sweep time if you set the Sweep Time Auto parameter to False. This value is expressed in seconds.The default value is 0.00167 seconds. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

CHP
