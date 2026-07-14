# NI DOCUMENT BUNDLE: rfmxtdscdma-c-api-ref

<!--NI_BUNDLE_CHUNK bundle=rfmxtdscdma-c-api-ref start=1 end=250 -->
<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes_1ga1afd6943023218b92cb76d0fc38f67d2.html language=enus -->
## TOPIC 00001: RFMXTDSCDMA_ATTR_REFERENCE_LEVEL_HEADROOM

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes_1ga1afd6943023218b92cb76d0fc38f67d2.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes_1ga1afd6943023218b92cb76d0fc38f67d2.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the margin RFmx adds to the RFMXTDSCDMA_ATTR_REFERENCE_LEVEL attribute. The margin avoids clipping and overflow warnings if the input signal exceeds the configured reference level. SyntaxRFMXTDSCDMA_ATTR_REFERENCE_LEVEL_HEADROOMNumeric ValueData TypeAccessApplies To7344124float64Read/Write

### RFMXTDSCDMA_ATTR_REFERENCE_LEVEL_HEADROOM

Specifies the margin RFmx adds to the [RFMXTDSCDMA_ATTR_REFERENCE_LEVEL](group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes_1gaac5d004ce9cfe0cb454fb88d54568936.html) attribute. The margin avoids clipping and overflow warnings if the input signal exceeds the configured reference level.

#### Syntax

RFMXTDSCDMA_ATTR_REFERENCE_LEVEL_HEADROOM

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 7344124 | float64 | Read/Write | N/A |

#### Remarks

RFmx configures the input gain to avoid clipping and associated overflow warnings provided the instantaneous power of the input signal remains within the Reference Level plus the Reference Level Headroom. If you know the input power of the signal precisely or previously included the margin in the Reference Level, you could improve the signal-to-noise ratio by reducing the Reference Level Headroom.

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

**Supported devices:**PXIe-5668R, PXIe-5830/5831/5832/5840/5841/5842/5860.

**Default values**

| Name (value) | Description |
| --- | --- |
| PXIe-5668 | 6 dB |
| PXIe-5830/5831/5832/5841/5842/5860 | 1 dB |
| PXIe-5840 | 0 dB |

Parent topic:

Attributes

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes_1ga229ac7e01d10bd5a32dade82d189e3cb.html language=enus -->
## TOPIC 00002: RFMXTDSCDMA_ATTR_PILOT_CODE

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes_1ga229ac7e01d10bd5a32dade82d189e3cb.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes_1ga229ac7e01d10bd5a32dade82d189e3cb.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the SYNC-UL code used by the uplink pilot time slot (UpPTS). This attribute is used when the RFMXTDSCDMA_ATTR_MODACC_SYNCHRONIZATION_MODE attribute is set to Subframe, or the RFMXTDSCDMA_ATTR_MODACC_SLOT_TYPE attribute is set to Pilot. SyntaxRFMXTDSCDMA_ATTR_PILOT_CODENumeric ValueData Typ

### RFMXTDSCDMA_ATTR_PILOT_CODE

Specifies the SYNC-UL code used by the uplink pilot time slot (UpPTS). This attribute is used when the [RFMXTDSCDMA_ATTR_MODACC_SYNCHRONIZATION_MODE](group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc_1ga1c3cfa23ee9d0c4afbd2eab70d1918cc.html) attribute is set to **Subframe**, or the [RFMXTDSCDMA_ATTR_MODACC_SLOT_TYPE](group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc_1ga017698cba60ec880f222ea6ae36eb13d.html) attribute is set to **Pilot**.

#### Syntax

RFMXTDSCDMA_ATTR_PILOT_CODE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 7340060 | int32 | Read/Write | N/A |

#### Remarks

The Code Group of the attribute is determined by the following formula:

*Code Group* = *floor (Pilot Code / 8)*

The code group of the attribute should match the code group of the [RFMXTDSCDMA_ATTR_UPLINK_SCRAMBLING_CODE](group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__scrambling__uplink_1ga3287a316f961cf947f017bfa505b987d.html) attribute. For more information on code allocations, refer to the *Code Allocation* in Section 8.3 of *3GPP TS 25.223*, v.11.0.0 Release 11.

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 0.

Parent topic:

Attributes

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes_1ga6bad390963053209a1ff5e00441683e1.html language=enus -->
## TOPIC 00003: RFMXTDSCDMA_ATTR_EXTERNAL_ATTENUATION

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes_1ga6bad390963053209a1ff5e00441683e1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes_1ga6bad390963053209a1ff5e00441683e1.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the level of external attenuation that is considered by the selected measurement. This value is expressed in dB. SyntaxRFMXTDSCDMA_ATTR_EXTERNAL_ATTENUATIONNumeric ValueData TypeAccessApplies To7340035float64Read/WriteN/ARemarks For more information about attenuation, refer to the RF Atten

### RFMXTDSCDMA_ATTR_EXTERNAL_ATTENUATION

Specifies the level of external attenuation that is considered by the selected measurement. This value is expressed in dB.

#### Syntax

RFMXTDSCDMA_ATTR_EXTERNAL_ATTENUATION

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 7340035 | float64 | Read/Write | N/A |

#### Remarks

For more information about attenuation, refer to the *RF Attenuation and Signal Levels* topic for your device in the *NI RF Vector Signal Analyzers Help*.

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 0 dB.

Parent topic:

Attributes

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes_1gaac5d004ce9cfe0cb454fb88d54568936.html language=enus -->
## TOPIC 00004: RFMXTDSCDMA_ATTR_REFERENCE_LEVEL

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes_1gaac5d004ce9cfe0cb454fb88d54568936.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes_1gaac5d004ce9cfe0cb454fb88d54568936.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the reference level that represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and V[pk-pk] for baseband devices. SyntaxRFMXTDSCDMA_ATTR_REFERENCE_LEVELNumeric ValueData TypeAccessApplies To7340034float64Read/WriteN/ARemarks You do not

### RFMXTDSCDMA_ATTR_REFERENCE_LEVEL

Specifies the reference level that represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and V<sub>pk-pk</sub> for baseband devices.

#### Syntax

RFMXTDSCDMA_ATTR_REFERENCE_LEVEL

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 7340034 | float64 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default of this attribute is hardware dependent.

Parent topic:

Attributes

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__acp.html language=enus -->
## TOPIC 00005: ACP

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__acp.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__acp.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsAdvancedAveragingCarrierFFTOffsetRBW FilterResultsSweep TimeGroup membersNameDescriptionRFMXTDSCDMA_ATTR_ACP_ALL_TRACES_ENABLEDSpecifies whether to enable the traces to be stored and retrieved after performing the ACP measurement. RFMXTDSCDMA_ATTR_ACP_MEASUREMENT_ENABLEDSpecifies whether to en

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
| RFMXTDSCDMA_ATTR_ACP_ALL_TRACES_ENABLED | Specifies whether to enable the traces to be stored and retrieved after performing the ACP measurement. |
| RFMXTDSCDMA_ATTR_ACP_MEASUREMENT_ENABLED | Specifies whether to enable the ACP measurement. |
| RFMXTDSCDMA_ATTR_ACP_MEASUREMENT_METHOD | Specifies the method for performing the ACP measurement. |
| RFMXTDSCDMA_ATTR_ACP_NOISE_COMPENSATION_ENABLED | Specifies whether to enable compensation of the channel powers for the inherent noise floor of the signal analyzer. |
| RFMXTDSCDMA_ATTR_ACP_NUMBER_OF_ANALYSIS_THREADS | Specifies the maximum number of threads used for parallelism for the ACP measurement. |

#### Attachments

None

Parent topic:

Attributes

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__acp_1gaee8b7712ed9e1da45f80eeb6e6ebc550.html language=enus -->
## TOPIC 00006: RFMXTDSCDMA_ATTR_ACP_ALL_TRACES_ENABLED

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__acp_1gaee8b7712ed9e1da45f80eeb6e6ebc550.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__acp_1gaee8b7712ed9e1da45f80eeb6e6ebc550.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the traces to be stored and retrieved after performing the ACP measurement. SyntaxRFMXTDSCDMA_ATTR_ACP_ALL_TRACES_ENABLEDNumeric ValueData TypeAccessApplies To7344161int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for

### RFMXTDSCDMA_ATTR_ACP_ALL_TRACES_ENABLED

Specifies whether to enable the traces to be stored and retrieved after performing the ACP measurement.

#### Syntax

RFMXTDSCDMA_ATTR_ACP_ALL_TRACES_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 7344161 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is FALSE.

Parent topic:

ACP

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__acp__advanced.html language=enus -->
## TOPIC 00007: Advanced

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__acp__advanced.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__acp__advanced.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXTDSCDMA_ATTR_ACP_FAR_IF_OUTPUT_POWER_OFFSETSpecifies the offset by which to adjust the IF output power level for offset channels that are far from the carrier channel to improve the dynamic range. This value is expressed in dB. This attribute is used only if

### Advanced

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXTDSCDMA_ATTR_ACP_FAR_IF_OUTPUT_POWER_OFFSET | Specifies the offset by which to adjust the IF output power level for offset channels that are far from the carrier channel to improve the dynamic range. This value is expressed in dB. This attribute is used only if you set the RFMXTDSCDMA_ATTR_ACP_MEASUREMENT_METHOD attribute to Dynamic Range and set the RFMXTDSCDMA_ATTR_ACP_IF_OUTPUT_POWER_OFFSET_AUTO attribute to False. |
| RFMXTDSCDMA_ATTR_ACP_IF_OUTPUT_POWER_OFFSET_AUTO | Specifies whether the measurement calculates an IF output power level offset for the offset channels to improve the dynamic range of the ACP measurement. This attribute is used only if you set the RFMXTDSCDMA_ATTR_ACP_MEASUREMENT_METHOD attribute to Dynamic Range. |
| RFMXTDSCDMA_ATTR_ACP_NEAR_IF_OUTPUT_POWER_OFFSET | Specifies the offset by which to adjust the IF output power level for offset channels that are near the carrier channel to improve the dynamic range. This value is expressed in dB. This attribute is used only if you set the RFMXTDSCDMA_ATTR_ACP_MEASUREMENT_METHOD attribute to Dynamic Range and set the RFMXTDSCDMA_ATTR_ACP_IF_OUTPUT_POWER_OFFSET_AUTO attribute to False. |
| RFMXTDSCDMA_ATTR_ACP_SEQUENTIAL_FFT_SIZE | Specifies the FFT size when you set the RFMXTDSCDMA_ATTR_ACP_MEASUREMENT_METHOD attribute to Sequential FFT. |

#### Attachments

None

Parent topic:

ACP

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__acp__advanced_1ga18f4817d084aa7d7294c8f850c0629b6.html language=enus -->
## TOPIC 00008: RFMXTDSCDMA_ATTR_ACP_SEQUENTIAL_FFT_SIZE

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__acp__advanced_1ga18f4817d084aa7d7294c8f850c0629b6.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__acp__advanced_1ga18f4817d084aa7d7294c8f850c0629b6.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the FFT size when you set the RFMXTDSCDMA_ATTR_ACP_MEASUREMENT_METHOD attribute to Sequential FFT. SyntaxRFMXTDSCDMA_ATTR_ACP_SEQUENTIAL_FFT_SIZENumeric ValueData TypeAccessApplies To7344184int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribu

### RFMXTDSCDMA_ATTR_ACP_SEQUENTIAL_FFT_SIZE

Specifies the FFT size when you set the [RFMXTDSCDMA_ATTR_ACP_MEASUREMENT_METHOD](group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__acp_1ga81fb63a44994187460a01bc3dddd31ea.html) attribute to **Sequential FFT**.

#### Syntax

RFMXTDSCDMA_ATTR_ACP_SEQUENTIAL_FFT_SIZE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 7344184 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) Strings topic for information about the string syntax for named signals.

The default value is 512.

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__acp__rbw__filter_1ga48279b8e65f9ab0cf927a3d0b741a141.html language=enus -->
## TOPIC 00009: RFMXTDSCDMA_ATTR_ACP_RBW_FILTER_TYPE

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__acp__rbw__filter_1ga48279b8e65f9ab0cf927a3d0b741a141.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__acp__rbw__filter_1ga48279b8e65f9ab0cf927a3d0b741a141.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the shape of the digital RBW filter. SyntaxRFMXTDSCDMA_ATTR_ACP_RBW_FILTER_TYPENumeric ValueData TypeAccessApplies To7344157int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector String t

### RFMXTDSCDMA_ATTR_ACP_RBW_FILTER_TYPE

Specifies the shape of the digital RBW filter.

#### Syntax

RFMXTDSCDMA_ATTR_ACP_RBW_FILTER_TYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 7344157 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **FFT Based**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXTDSCDMA_VAL_ACP_RBW_FILTER_TYPE_FFT_BASED | 0 (0x0) | An RBW filter with a fast Fourier transform (FFT)-based response is applied. |
| RFMXTDSCDMA_VAL_ACP_RBW_FILTER_TYPE_GAUSSIAN | 1 (0x1) | An RBW filter with a Gaussian response is applied. |
| RFMXTDSCDMA_VAL_ACP_RBW_FILTER_TYPE_FLAT | 2 (0x2) | An RBW filter with a flat response is applied. |

Parent topic:

RBW Filter

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__acp__rbw__filter_1gab0939f1d423e602f9640ca9f5fe5e41f.html language=enus -->
## TOPIC 00010: RFMXTDSCDMA_ATTR_ACP_RBW_FILTER_AUTO_BANDWIDTH

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__acp__rbw__filter_1gab0939f1d423e602f9640ca9f5fe5e41f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__acp__rbw__filter_1gab0939f1d423e602f9640ca9f5fe5e41f.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement calculates the RBW. SyntaxRFMXTDSCDMA_ATTR_ACP_RBW_FILTER_AUTO_BANDWIDTHNumeric ValueData TypeAccessApplies To7344155int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the

### RFMXTDSCDMA_ATTR_ACP_RBW_FILTER_AUTO_BANDWIDTH

Specifies whether the measurement calculates the RBW.

#### Syntax

RFMXTDSCDMA_ATTR_ACP_RBW_FILTER_AUTO_BANDWIDTH

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 7344155 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **True**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXTDSCDMA_VAL_ACP_RBW_AUTO_FALSE | 0 (0x0) | The measurement uses the RBW that you specify in the RFMXTDSCDMA_ATTR_ACP_RBW_FILTER_BANDWIDTH attribute. |
| RFMXTDSCDMA_VAL_ACP_RBW_AUTO_TRUE | 1 (0x1) | The measurement calculates the RBW. |

Parent topic:

RBW Filter

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__acp__results__carrier.html language=enus -->
## TOPIC 00011: Carrier

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__acp__results__carrier.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__acp__results__carrier.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXTDSCDMA_ATTR_ACP_RESULTS_CARRIER_ABSOLUTE_POWERReturns the absolute measured carrier power. This value is expressed in dBm. AttachmentsNone

### Carrier

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXTDSCDMA_ATTR_ACP_RESULTS_CARRIER_ABSOLUTE_POWER | Returns the absolute measured carrier power. This value is expressed in dBm. |

#### Attachments

None

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__acp__results__lower__offset.html language=enus -->
## TOPIC 00012: Lower Offset

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__acp__results__lower__offset.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__acp__results__lower__offset.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXTDSCDMA_ATTR_ACP_RESULTS_LOWER_OFFSET_ABSOLUTE_POWERReturns the absolute measured lower offset channel power. This value is expressed in dBm. RFMXTDSCDMA_ATTR_ACP_RESULTS_LOWER_OFFSET_RELATIVE_POWERReturns the lower offset channel power measured relative to

### Lower Offset

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXTDSCDMA_ATTR_ACP_RESULTS_LOWER_OFFSET_ABSOLUTE_POWER | Returns the absolute measured lower offset channel power. This value is expressed in dBm. |
| RFMXTDSCDMA_ATTR_ACP_RESULTS_LOWER_OFFSET_RELATIVE_POWER | Returns the lower offset channel power measured relative to the integrated power of the power reference carrier. This value is expressed in dB. |

#### Attachments

None

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__acp__results__lower__offset_1ga9c66487b359896e11dc7912fd5aa70a4.html language=enus -->
## TOPIC 00013: RFMXTDSCDMA_ATTR_ACP_RESULTS_LOWER_OFFSET_ABSOLUTE_POWER

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__acp__results__lower__offset_1ga9c66487b359896e11dc7912fd5aa70a4.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__acp__results__lower__offset_1ga9c66487b359896e11dc7912fd5aa70a4.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the absolute measured lower offset channel power. This value is expressed in dBm. SyntaxRFMXTDSCDMA_ATTR_ACP_RESULTS_LOWER_OFFSET_ABSOLUTE_POWERNumeric ValueData TypeAccessApplies To7344172float64Read-OnlyOffsetRemarks Use "offset<i><n></i>" as the Selector String to read this result.

### RFMXTDSCDMA_ATTR_ACP_RESULTS_LOWER_OFFSET_ABSOLUTE_POWER

Returns the absolute measured lower offset channel power. This value is expressed in dBm.

#### Syntax

RFMXTDSCDMA_ATTR_ACP_RESULTS_LOWER_OFFSET_ABSOLUTE_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 7344172 | float64 | Read-Only | Offset |

#### Remarks

Use "offset<i><n></i>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result.

Parent topic:

Lower Offset

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__acp__results__upper__offset.html language=enus -->
## TOPIC 00014: Upper Offset

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__acp__results__upper__offset.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__acp__results__upper__offset.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXTDSCDMA_ATTR_ACP_RESULTS_UPPER_OFFSET_ABSOLUTE_POWERReturns the absolute measured upper offset channel power. This value is expressed in dBm. RFMXTDSCDMA_ATTR_ACP_RESULTS_UPPER_OFFSET_RELATIVE_POWERReturns the upper offset channel power measured relative to

### Upper Offset

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXTDSCDMA_ATTR_ACP_RESULTS_UPPER_OFFSET_ABSOLUTE_POWER | Returns the absolute measured upper offset channel power. This value is expressed in dBm. |
| RFMXTDSCDMA_ATTR_ACP_RESULTS_UPPER_OFFSET_RELATIVE_POWER | Returns the upper offset channel power measured relative to the integrated power of the power reference carrier. This value is expressed in dB. |

#### Attachments

None

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__acp__sweep__time_1ga880fd89d68e0b816841bf51b3705796a.html language=enus -->
## TOPIC 00015: RFMXTDSCDMA_ATTR_ACP_SWEEP_TIME_INTERVAL

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__acp__sweep__time_1ga880fd89d68e0b816841bf51b3705796a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__acp__sweep__time_1ga880fd89d68e0b816841bf51b3705796a.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the sweep time when you set the RFMXTDSCDMA_ATTR_ACP_SWEEP_TIME_AUTO attribute to False. This value is expressed in seconds. SyntaxRFMXTDSCDMA_ATTR_ACP_SWEEP_TIME_INTERVALNumeric ValueData TypeAccessApplies To7344159float64Read/WriteN/ARemarks You do not need to use a selector string to co

### RFMXTDSCDMA_ATTR_ACP_SWEEP_TIME_INTERVAL

Specifies the sweep time when you set the [RFMXTDSCDMA_ATTR_ACP_SWEEP_TIME_AUTO](group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__acp__sweep__time_1ga7c4a253c56ba71d92f3de9138f04f9df.html) attribute to **False**. This value is expressed in seconds.

#### Syntax

RFMXTDSCDMA_ATTR_ACP_SWEEP_TIME_INTERVAL

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 7344159 | float64 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 0.00066 s.

Parent topic:

Sweep Time

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__advanced_1ga65a2aa43f1dc8ac6c093418c8fd6a81e.html language=enus -->
## TOPIC 00016: RFMXTDSCDMA_ATTR_LIMITED_CONFIGURATION_CHANGE

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__advanced_1ga65a2aa43f1dc8ac6c093418c8fd6a81e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__advanced_1ga65a2aa43f1dc8ac6c093418c8fd6a81e.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the set of attributes that are considered by RFmx in the locked signal configuration state. SyntaxRFMXTDSCDMA_ATTR_LIMITED_CONFIGURATION_CHANGENumeric ValueData TypeAccessApplies To7393283int32Read/WriteN/ARemarks If your test system performs the same measurement at different selected port

### RFMXTDSCDMA_ATTR_LIMITED_CONFIGURATION_CHANGE

Specifies the set of attributes that are considered by RFmx in the locked signal configuration state.

#### Syntax

RFMXTDSCDMA_ATTR_LIMITED_CONFIGURATION_CHANGE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 7393283 | int32 | Read/Write | N/A |

#### Remarks

If your test system performs the same measurement at different selected ports, multiple frequencies, and/or power levels repeatedly, you can enable this attribute to help achieve faster measurements. When you set this attribute to a value other than **Disabled**, the RFmx driver will use an optimized code path and skip some checks. Because RFmx skips some checks when you use this attribute, you need to be aware of the limitations of this feature, which are listed in the [Limitations of the Limited Configuration Change Property](https://www.ni.com/docs/en-US/bundle/rfmx-wcdma-prop/page/rfmxwcdmaprop/limitations.html) topic.

You can also use this attribute to lock a specific instrument configuration for a signal so that every time that you initiate the signal, RFmx applies the RFmxInstr attributes from a locked configuration.

NI recommends you use this attribute in conjunction with named signal configurations. Create named signal configurations for each measurement configuration in your test program and set this attribute to a value other than **Disabled** for one or more of the named signal configurations. This allows RFmx to precompute the acquisition settings for your measurement configurations and re-use the precomputed settings each time you initiate the measurement. You do not need to use this attribute if you create named signals for all the measurement configurations in your test program during test sequence initialization and do not change any RFmxInstr or personality attributes while testing each device under test. RFmx automatically optimizes that use case.

Specify the named signal configuration you are setting this attribute in the selector string input. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default value is **Disabled**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXTDSCDMA_VAL_LIMITED_CONFIGURATION_CHANGE_DISABLED | 0 (0x0) | This is the normal mode of RFmx operation. All configuration changes in RFmxInstr attributes or in personality attributes will be applied during RFmx Commit. |
| RFMXTDSCDMA_VAL_LIMITED_CONFIGURATION_CHANGE_NO_CHANGE | 1 (0x1) | Signal configuration is locked after the first Commit of the named signal configuration. Any configuration change thereafter either in RFmxInstr attributes or personality attributes will not be considered by subsequent RFmx Commits or Initiates of this signal. Use No Change if you have created named signal configurations for all measurement configurations but are setting some RFmxInstr attributes. Refer to the Limitations of the Limited Configuration Change Property topic for more details about the limitations of using this mode. |
| RFMXTDSCDMA_VAL_LIMITED_CONFIGURATION_CHANGE_FREQUENCY | 2 (0x2) | Signal configuration, other than center frequency and external attenuation, is locked after first Commit of the named signal configuration. Thereafter, only the RFMXTDSCDMA_ATTR_CENTER_FREQUENCY and RFMXTDSCDMA_ATTR_EXTERNAL_ATTENUATION attribute value changes will be considered by subsequent driver Commits or Initiates of this signal. Refer to the Limitations of the Limited Configuration Change Property topic for more details about the limitations of using this mode. |
| RFMXTDSCDMA_VAL_LIMITED_CONFIGURATION_CHANGE_REFERENCE_LEVEL | 3 (0x3) | Signal configuration, other than the reference level, is locked after first Commit of the named signal configuration. Thereafter only the RFMXTDSCDMA_ATTR_REFERENCE_LEVEL attribute value change will be considered by subsequent driver Commits or Initiates of this signal. If you have configured this signal to use an IQ Power Edge Trigger, NI recommends that you set the RFMXTDSCDMA_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE to Relative so that the trigger level is automatically adjusted as you adjust the reference level. Refer to the Limitations of the Limited Configuration Change Property topic for more details about the limitations of using this mode. |
| RFMXTDSCDMA_VAL_LIMITED_CONFIGURATION_CHANGE_FREQUENCY_AND_REFERENCE_LEVEL | 4 (0x4) | Signal configuration, other than center frequency, reference level, and external attenuation, is locked after first Commit of the named signal configuration. Thereafter only Center Frequency, Reference Level, and External Attenuation attribute value changes will be considered by subsequent driver Commits or Initiates of this signal. If you have configured this signal to use an IQ Power Edge Trigger, NI recommends you set the IQ Power Edge Level Type to Relative so that the trigger level is automatically adjusted as you adjust the reference level. Refer to the Limitations of the Limited Configuration Change Property topic for more details about the limitations of using this mode. |
| RFMXTDSCDMA_VAL_LIMITED_CONFIGURATION_CHANGE_SELECTED_PORTS_FREQUENCY_AND_REFERENCE_LEVEL | 5 (0x5) | Signal configuration, other than selected ports, center frequency, reference level, external attenuation, and RFInstr configuration, is locked after first Commit or Initiate of the named signal configuration. Thereafter only Selected Ports, Center Frequency, Reference Level, and External Attenuation attribute value changes will be considered by subsequent driver Commits or Initiates of this signal. If you have configured this signal to use an IQ Power Edge Trigger, NI recommends you set the IQ Power Edge Level Type to Relative so that the trigger level is automatically adjusted as you adjust the reference level. Refer to the Limitations of the Limited Configuration Change Property topic for more details about the limitations of using this mode. |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__cda.html language=enus -->
## TOPIC 00017: CDA

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__cda.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__cda.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsAveragingResultsGroup membersNameDescriptionRFMXTDSCDMA_ATTR_CDA_ALL_TRACES_ENABLEDSpecifies whether to enable the traces to be stored and retrieved after performing the code domain analysis (CDA) measurement. RFMXTDSCDMA_ATTR_CDA_BASE_SPREADING_FACTORSpecifies the base spreading factor for co

### CDA

#### Groups

- Averaging
- Results

#### Group members

| Name | Description |
| --- | --- |
| RFMXTDSCDMA_ATTR_CDA_ALL_TRACES_ENABLED | Specifies whether to enable the traces to be stored and retrieved after performing the code domain analysis (CDA) measurement. |
| RFMXTDSCDMA_ATTR_CDA_BASE_SPREADING_FACTOR | Specifies the base spreading factor for code domain analysis. |
| RFMXTDSCDMA_ATTR_CDA_IQ_GAIN_IMBALANCE_REMOVAL_ENABLED | Specifies whether to remove the I/Q gain imbalance before the code domain analysis (CDA) measurement. |
| RFMXTDSCDMA_ATTR_CDA_IQ_OFFSET_REMOVAL_ENABLED | Specifies whether to remove the I/Q offset before the code domain analysis (CDA) measurement. |
| RFMXTDSCDMA_ATTR_CDA_IQ_QUADRATURE_ERROR_REMOVAL_ENABLED | Specifies whether to remove the I/Q quadrature error before the code domain analysis (CDA) measurement. |
| RFMXTDSCDMA_ATTR_CDA_MEASUREMENT_CHANNEL_CHANNELIZATION_CODE | Specifies the channelization code of the code domain analysis (CDA) measurement channel. |
| RFMXTDSCDMA_ATTR_CDA_MEASUREMENT_CHANNEL_SPREADING_FACTOR | Specifies the spreading factor of the channel on which to perform the code domain analysis (CDA) measurement. |
| RFMXTDSCDMA_ATTR_CDA_MEASUREMENT_ENABLED | Specifies whether to enable the code domain analysis (CDA) measurement. |
| RFMXTDSCDMA_ATTR_CDA_MEASUREMENT_OFFSET | Specifies the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the RFMXTDSCDMA_ATTR_CDA_SYNCHRONIZATION_MODE attribute. |
| RFMXTDSCDMA_ATTR_CDA_NUMBER_OF_ANALYSIS_THREADS | Specifies the maximum number of threads used for parallelism for the code domain analysis (CDA) measurement. |
| RFMXTDSCDMA_ATTR_CDA_POWER_UNIT | Specifies the measurement unit of the code domain power (CDP) results. |
| RFMXTDSCDMA_ATTR_CDA_RRC_FILTER_ENABLED | Specifies whether to enable the RRC filter. |
| RFMXTDSCDMA_ATTR_CDA_SPECTRUM_INVERTED | Specifies whether the spectrum of the signal is inverted. |
| RFMXTDSCDMA_ATTR_CDA_SYNCHRONIZATION_MODE | Specifies the synchronization mode for the code domain analysis (CDA) measurement. Currently, only the Slot mode is supported. |

#### Attachments

None

Parent topic:

Attributes

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__cda_1ga28ecd9af9acfacfe16dcadae4338a7e0.html language=enus -->
## TOPIC 00018: RFMXTDSCDMA_ATTR_CDA_IQ_GAIN_IMBALANCE_REMOVAL_ENABLED

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__cda_1ga28ecd9af9acfacfe16dcadae4338a7e0.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__cda_1ga28ecd9af9acfacfe16dcadae4338a7e0.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to remove the I/Q gain imbalance before the code domain analysis (CDA) measurement. SyntaxRFMXTDSCDMA_ATTR_CDA_IQ_GAIN_IMBALANCE_REMOVAL_ENABLEDNumeric ValueData TypeAccessApplies To7417865int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this

### RFMXTDSCDMA_ATTR_CDA_IQ_GAIN_IMBALANCE_REMOVAL_ENABLED

Specifies whether to remove the I/Q gain imbalance before the code domain analysis (CDA) measurement.

#### Syntax

RFMXTDSCDMA_ATTR_CDA_IQ_GAIN_IMBALANCE_REMOVAL_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 7417865 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **False**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXTDSCDMA_VAL_CDA_IQ_GAIN_IMBALANCE_REMOVAL_ENABLED_FALSE | 0 (0x0) | The I/Q gain imbalance is not removed before the CDA measurement. |
| RFMXTDSCDMA_VAL_CDA_IQ_GAIN_IMBALANCE_REMOVAL_ENABLED_TRUE | 1 (0x1) | The I/Q gain imbalance is removed before the CDA measurement. |

Parent topic:

CDA

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__cda_1ga3415313f28c3e65396f73f44bb19d755.html language=enus -->
## TOPIC 00019: RFMXTDSCDMA_ATTR_CDA_NUMBER_OF_ANALYSIS_THREADS

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__cda_1ga3415313f28c3e65396f73f44bb19d755.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__cda_1ga3415313f28c3e65396f73f44bb19d755.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the maximum number of threads used for parallelism for the code domain analysis (CDA) measurement. SyntaxRFMXTDSCDMA_ATTR_CDA_NUMBER_OF_ANALYSIS_THREADSNumeric ValueData TypeAccessApplies To7417870int32Read/WriteN/ARemarks The number of threads can range from 1 to the number of physical co

### RFMXTDSCDMA_ATTR_CDA_NUMBER_OF_ANALYSIS_THREADS

Specifies the maximum number of threads used for parallelism for the code domain analysis (CDA) measurement.

#### Syntax

RFMXTDSCDMA_ATTR_CDA_NUMBER_OF_ANALYSIS_THREADS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 7417870 | int32 | Read/Write | N/A |

#### Remarks

The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations.

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 1.

Parent topic:

CDA

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__cda_1ga6e565a8975231dfed6e5dc12ca238765.html language=enus -->
## TOPIC 00020: RFMXTDSCDMA_ATTR_CDA_MEASUREMENT_ENABLED

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__cda_1ga6e565a8975231dfed6e5dc12ca238765.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__cda_1ga6e565a8975231dfed6e5dc12ca238765.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the code domain analysis (CDA) measurement. SyntaxRFMXTDSCDMA_ATTR_CDA_MEASUREMENT_ENABLEDNumeric ValueData TypeAccessApplies To7417856int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. R

### RFMXTDSCDMA_ATTR_CDA_MEASUREMENT_ENABLED

Specifies whether to enable the code domain analysis (CDA) measurement.

#### Syntax

RFMXTDSCDMA_ATTR_CDA_MEASUREMENT_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 7417856 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is FALSE.

Parent topic:

CDA

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__cda_1ga777255fcddd0ccf9077c601f4052d5e7.html language=enus -->
## TOPIC 00021: RFMXTDSCDMA_ATTR_CDA_RRC_FILTER_ENABLED

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__cda_1ga777255fcddd0ccf9077c601f4052d5e7.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__cda_1ga777255fcddd0ccf9077c601f4052d5e7.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the RRC filter. SyntaxRFMXTDSCDMA_ATTR_CDA_RRC_FILTER_ENABLEDNumeric ValueData TypeAccessApplies To7417868int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector String t

### RFMXTDSCDMA_ATTR_CDA_RRC_FILTER_ENABLED

Specifies whether to enable the RRC filter.

#### Syntax

RFMXTDSCDMA_ATTR_CDA_RRC_FILTER_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 7417868 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **True**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXTDSCDMA_VAL_CDA_RRC_FILTER_ENABLED_FALSE | 0 (0x0) | Disables the RRC filter in the measurement. |
| RFMXTDSCDMA_VAL_CDA_RRC_FILTER_ENABLED_TRUE | 1 (0x1) | Enables the RRC filter in the measurement. |

Parent topic:

CDA

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__cda_1gaa0ad174099ea90729c0159f629d43873.html language=enus -->
## TOPIC 00022: RFMXTDSCDMA_ATTR_CDA_BASE_SPREADING_FACTOR

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__cda_1gaa0ad174099ea90729c0159f629d43873.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__cda_1gaa0ad174099ea90729c0159f629d43873.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the base spreading factor for code domain analysis. SyntaxRFMXTDSCDMA_ATTR_CDA_BASE_SPREADING_FACTORNumeric ValueData TypeAccessApplies To7417860int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to

### RFMXTDSCDMA_ATTR_CDA_BASE_SPREADING_FACTOR

Specifies the base spreading factor for code domain analysis.

#### Syntax

RFMXTDSCDMA_ATTR_CDA_BASE_SPREADING_FACTOR

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 7417860 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 16. The valid values are 1, 2, 4, 8, and 16.

Parent topic:

CDA

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__cda_1gaf834eea76b8f1e9a45e7c68741f26308.html language=enus -->
## TOPIC 00023: RFMXTDSCDMA_ATTR_CDA_ALL_TRACES_ENABLED

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__cda_1gaf834eea76b8f1e9a45e7c68741f26308.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__cda_1gaf834eea76b8f1e9a45e7c68741f26308.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the traces to be stored and retrieved after performing the code domain analysis (CDA) measurement. SyntaxRFMXTDSCDMA_ATTR_CDA_ALL_TRACES_ENABLEDNumeric ValueData TypeAccessApplies To7417869int32Read/WriteN/ARemarks You do not need to use a selector string to configure or

### RFMXTDSCDMA_ATTR_CDA_ALL_TRACES_ENABLED

Specifies whether to enable the traces to be stored and retrieved after performing the code domain analysis (CDA) measurement.

#### Syntax

RFMXTDSCDMA_ATTR_CDA_ALL_TRACES_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 7417869 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is FALSE.

Parent topic:

CDA

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__cda__results.html language=enus -->
## TOPIC 00024: Results

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__cda__results.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__cda__results.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXTDSCDMA_ATTR_CDA_RESULTS_CHIP_RATE_ERRORReturns the chip rate error. This value is expressed in ppm. RFMXTDSCDMA_ATTR_CDA_RESULTS_FREQUENCY_ERRORReturns the frequency error averaged over all measured slots. This value is expressed in Hz. RFMXTDSCDMA_ATTR_CDA

### Results

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXTDSCDMA_ATTR_CDA_RESULTS_CHIP_RATE_ERROR | Returns the chip rate error. This value is expressed in ppm. |
| RFMXTDSCDMA_ATTR_CDA_RESULTS_FREQUENCY_ERROR | Returns the frequency error averaged over all measured slots. This value is expressed in Hz. |
| RFMXTDSCDMA_ATTR_CDA_RESULTS_IQ_GAIN_IMBALANCE | Returns the I/Q gain imbalance of the composite signal, averaged over all measured slots. This value is expressed in dB. |
| RFMXTDSCDMA_ATTR_CDA_RESULTS_IQ_ORIGIN_OFFSET | Returns the I/Q origin offset of the composite signal, averaged over all measured slots. This value is expressed in dB. |
| RFMXTDSCDMA_ATTR_CDA_RESULTS_IQ_QUADRATURE_ERROR | Returns the I/Q quadrature error of the composite signal, averaged over all measured slots. This value is expressed in degrees. |
| RFMXTDSCDMA_ATTR_CDA_RESULTS_MAXIMUM_PEAK_ACTIVE_POWER | Returns the maximum value among all averaging iterations of the maximum active code power measured in the code domain of the base spreading factor, normalized to the total code domain power (CDP). This value is expressed in dB, if you set the RFMXTDSCDMA_ATTR_CDA_POWER_UNIT attribute to dB, or in dBm, if you set the CDA Pwr Unit attribute to dBm. |
| RFMXTDSCDMA_ATTR_CDA_RESULTS_MAXIMUM_PEAK_INACTIVE_POWER | Returns the maximum value among all averaging iterations of the highest measured code power among the set of inactive channels in the code domain of the base spreading factor, normalized to the total code domain power (CDP). This value is expressed in dB, if you set the RFMXTDSCDMA_ATTR_CDA_POWER_UNIT attribute to dB, or in dBm, if you set the CDA Pwr Unit attribute to dBm. |
| RFMXTDSCDMA_ATTR_CDA_RESULTS_MAXIMUM_PEAK_SYMBOL_EVM | Returns the maximum value of the peak symbol EVMs, among all averaging iterations for the selected time slot and channel. This value is expressed as a percentage. |
| RFMXTDSCDMA_ATTR_CDA_RESULTS_MAXIMUM_TOTAL_ACTIVE_POWER | Returns the maximum value, among all averaging iterations, of total power measured in the code domain of the base spreading factor normalized to the total code domain power. This value is expressed in dB, if you set the RFMXTDSCDMA_ATTR_CDA_POWER_UNIT attribute to dB, or in dBm, if you set the CDA Pwr Unit attribute to dBm. |
| RFMXTDSCDMA_ATTR_CDA_RESULTS_MAXIMUM_TOTAL_POWER | Returns the maximum value of the power measured in the code domain of the base spreading factor among all averaging iterations. This value is expressed in dBm. |
| RFMXTDSCDMA_ATTR_CDA_RESULTS_MEAN_ACTIVE_POWER | Returns the average of the active code power measured in the code domain of the base spreading factor, normalized to the total code domain power (CDP). This value is expressed in dB, if you set the RFMXTDSCDMA_ATTR_CDA_POWER_UNIT attribute to dB, or in dBm, if you set the CDA Pwr Unit attribute to dBm. |
| RFMXTDSCDMA_ATTR_CDA_RESULTS_MEAN_INACTIVE_POWER | Returns the average code power measured among the set of inactive channels in the code domain of the base spreading factor, normalized to the total code domain power (CDP). This value is expressed in dB, if you set the RFMXTDSCDMA_ATTR_CDA_POWER_UNIT attribute to dB, or in dBm, if you set the CDA Pwr Unit attribute to dBm. |
| RFMXTDSCDMA_ATTR_CDA_RESULTS_MEAN_RMS_SYMBOL_EVM | Returns the RMS symbol EVM for the selected time slot and channel, averaged over all averaging iterations. This value is expressed as a percentage. |
| RFMXTDSCDMA_ATTR_CDA_RESULTS_MEAN_RMS_SYMBOL_MAGNITUDE_ERROR | Returns the RMS symbol magnitude error for the selected time slot and channel, averaged over all averaging iterations. This value is expressed as a percentage. |
| RFMXTDSCDMA_ATTR_CDA_RESULTS_MEAN_RMS_SYMBOL_PHASE_ERROR | Returns the RMS symbol phase error for the selected time slot and channel, averaged over all averaging iterations. This value is expressed in degrees. |
| RFMXTDSCDMA_ATTR_CDA_RESULTS_MEAN_SYMBOL_POWER | Returns the mean symbol power for the selected time slot and channel. This value is expressed in dB if you set the RFMXTDSCDMA_ATTR_CDA_POWER_UNIT attribute to dB, or in dBm if you set the CDA Pwr Unit attribute to dBm. |
| RFMXTDSCDMA_ATTR_CDA_RESULTS_MEAN_TOTAL_ACTIVE_POWER | Returns the total active code power measured in the code domain of the base spreading factor, normalized to the total code domain power (CDP). This value is expressed in dB, if you set the RFMXTDSCDMA_ATTR_CDA_POWER_UNIT attribute to dB, or in dBm, if you set the CDA Pwr Unit attribute to dBm. The total active code power is averaged over all averaging iterations. |
| RFMXTDSCDMA_ATTR_CDA_RESULTS_MEAN_TOTAL_POWER | Returns the total power measured in the code domain of the base spreading factor, averaged over all averaging iterations. This value is expressed in dBm. |

#### Attachments

None

Parent topic:

CDA

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__cda__results_1ga01a755041bd73ad55949ec487a15777b.html language=enus -->
## TOPIC 00025: RFMXTDSCDMA_ATTR_CDA_RESULTS_MEAN_INACTIVE_POWER

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__cda__results_1ga01a755041bd73ad55949ec487a15777b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__cda__results_1ga01a755041bd73ad55949ec487a15777b.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the average code power measured among the set of inactive channels in the code domain of the base spreading factor, normalized to the total code domain power (CDP). This value is expressed in dB, if you set the RFMXTDSCDMA_ATTR_CDA_POWER_UNIT attribute to dB, or in dBm, if you set the CDA Pw

### RFMXTDSCDMA_ATTR_CDA_RESULTS_MEAN_INACTIVE_POWER

Returns the average code power measured among the set of inactive channels in the code domain of the base spreading factor, normalized to the total code domain power (CDP). This value is expressed in dB, if you set the [RFMXTDSCDMA_ATTR_CDA_POWER_UNIT](group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__cda_1ga68e706878d05d27db97c7c3da7f3fed6.html) attribute to **dB**, or in dBm, if you set the CDA Pwr Unit attribute to **dBm**.

#### Syntax

RFMXTDSCDMA_ATTR_CDA_RESULTS_MEAN_INACTIVE_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 7417885 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for the default signal and result instances. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__cda__results_1ga14c024e42a04c0ecb001782afcb546ac.html language=enus -->
## TOPIC 00026: RFMXTDSCDMA_ATTR_CDA_RESULTS_MAXIMUM_TOTAL_POWER

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__cda__results_1ga14c024e42a04c0ecb001782afcb546ac.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__cda__results_1ga14c024e42a04c0ecb001782afcb546ac.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum value of the power measured in the code domain of the base spreading factor among all averaging iterations. This value is expressed in dBm. SyntaxRFMXTDSCDMA_ATTR_CDA_RESULTS_MAXIMUM_TOTAL_POWERNumeric ValueData TypeAccessApplies To7417892float64Read-OnlyN/ARemarks You do not nee

### RFMXTDSCDMA_ATTR_CDA_RESULTS_MAXIMUM_TOTAL_POWER

Returns the maximum value of the power measured in the code domain of the base spreading factor among all averaging iterations. This value is expressed in dBm.

#### Syntax

RFMXTDSCDMA_ATTR_CDA_RESULTS_MAXIMUM_TOTAL_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 7417892 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for the default signal and result instances. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__cda__results_1ga57d6d65964c5666a479ad4ce2363f5e0.html language=enus -->
## TOPIC 00027: RFMXTDSCDMA_ATTR_CDA_RESULTS_IQ_GAIN_IMBALANCE

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__cda__results_1ga57d6d65964c5666a479ad4ce2363f5e0.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__cda__results_1ga57d6d65964c5666a479ad4ce2363f5e0.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the I/Q gain imbalance of the composite signal, averaged over all measured slots. This value is expressed in dB. SyntaxRFMXTDSCDMA_ATTR_CDA_RESULTS_IQ_GAIN_IMBALANCENumeric ValueData TypeAccessApplies To7417877float64Read-OnlyN/ARemarks You do not need to use a selector string to read this r

### RFMXTDSCDMA_ATTR_CDA_RESULTS_IQ_GAIN_IMBALANCE

Returns the I/Q gain imbalance of the composite signal, averaged over all measured slots. This value is expressed in dB.

#### Syntax

RFMXTDSCDMA_ATTR_CDA_RESULTS_IQ_GAIN_IMBALANCE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 7417877 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for the default signal and result instances. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__cda__results_1ga5f969e5f2f0ae6fe1591c74b22f48936.html language=enus -->
## TOPIC 00028: RFMXTDSCDMA_ATTR_CDA_RESULTS_MEAN_TOTAL_ACTIVE_POWER

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__cda__results_1ga5f969e5f2f0ae6fe1591c74b22f48936.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__cda__results_1ga5f969e5f2f0ae6fe1591c74b22f48936.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the total active code power measured in the code domain of the base spreading factor, normalized to the total code domain power (CDP). This value is expressed in dB, if you set the RFMXTDSCDMA_ATTR_CDA_POWER_UNIT attribute to dB, or in dBm, if you set the CDA Pwr Unit attribute to dBm. The t

### RFMXTDSCDMA_ATTR_CDA_RESULTS_MEAN_TOTAL_ACTIVE_POWER

Returns the total active code power measured in the code domain of the base spreading factor, normalized to the total code domain power (CDP). This value is expressed in dB, if you set the [RFMXTDSCDMA_ATTR_CDA_POWER_UNIT](group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__cda_1ga68e706878d05d27db97c7c3da7f3fed6.html) attribute to **dB**, or in dBm, if you set the CDA Pwr Unit attribute to **dBm**. The total active code power is averaged over all averaging iterations.

#### Syntax

RFMXTDSCDMA_ATTR_CDA_RESULTS_MEAN_TOTAL_ACTIVE_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 7417882 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for the default signal and result instances. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__cda__results_1ga6e7d92551fd270344a0c92bffc411fb2.html language=enus -->
## TOPIC 00029: RFMXTDSCDMA_ATTR_CDA_RESULTS_MAXIMUM_PEAK_INACTIVE_POWER

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__cda__results_1ga6e7d92551fd270344a0c92bffc411fb2.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__cda__results_1ga6e7d92551fd270344a0c92bffc411fb2.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum value among all averaging iterations of the highest measured code power among the set of inactive channels in the code domain of the base spreading factor, normalized to the total code domain power (CDP). This value is expressed in dB, if you set the RFMXTDSCDMA_ATTR_CDA_POWER_UN

### RFMXTDSCDMA_ATTR_CDA_RESULTS_MAXIMUM_PEAK_INACTIVE_POWER

Returns the maximum value among all averaging iterations of the highest measured code power among the set of inactive channels in the code domain of the base spreading factor, normalized to the total code domain power (CDP). This value is expressed in dB, if you set the [RFMXTDSCDMA_ATTR_CDA_POWER_UNIT](group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__cda_1ga68e706878d05d27db97c7c3da7f3fed6.html) attribute to **dB**, or in dBm, if you set the CDA Pwr Unit attribute to **dBm**.

#### Syntax

RFMXTDSCDMA_ATTR_CDA_RESULTS_MAXIMUM_PEAK_INACTIVE_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 7417897 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for the default signal and result instances. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__cda__results_1gaa11148379f5ae2a6ff5afd14cb4fd18a.html language=enus -->
## TOPIC 00030: RFMXTDSCDMA_ATTR_CDA_RESULTS_MEAN_RMS_SYMBOL_PHASE_ERROR

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__cda__results_1gaa11148379f5ae2a6ff5afd14cb4fd18a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__cda__results_1gaa11148379f5ae2a6ff5afd14cb4fd18a.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the RMS symbol phase error for the selected time slot and channel, averaged over all averaging iterations. This value is expressed in degrees. SyntaxRFMXTDSCDMA_ATTR_CDA_RESULTS_MEAN_RMS_SYMBOL_PHASE_ERRORNumeric ValueData TypeAccessApplies To7417875float64Read-OnlyN/ARemarks You do not need

### RFMXTDSCDMA_ATTR_CDA_RESULTS_MEAN_RMS_SYMBOL_PHASE_ERROR

Returns the RMS symbol phase error for the selected time slot and channel, averaged over all averaging iterations. This value is expressed in degrees.

#### Syntax

RFMXTDSCDMA_ATTR_CDA_RESULTS_MEAN_RMS_SYMBOL_PHASE_ERROR

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 7417875 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for the default signal and result instances. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__cda__results_1gac3132d4600be4e6d709fa347c504f4a5.html language=enus -->
## TOPIC 00031: RFMXTDSCDMA_ATTR_CDA_RESULTS_MAXIMUM_PEAK_SYMBOL_EVM

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__cda__results_1gac3132d4600be4e6d709fa347c504f4a5.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__cda__results_1gac3132d4600be4e6d709fa347c504f4a5.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum value of the peak symbol EVMs, among all averaging iterations for the selected time slot and channel. This value is expressed as a percentage. SyntaxRFMXTDSCDMA_ATTR_CDA_RESULTS_MAXIMUM_PEAK_SYMBOL_EVMNumeric ValueData TypeAccessApplies To7417889float64Read-OnlyN/ARemarks You do

### RFMXTDSCDMA_ATTR_CDA_RESULTS_MAXIMUM_PEAK_SYMBOL_EVM

Returns the maximum value of the peak symbol EVMs, among all averaging iterations for the selected time slot and channel. This value is expressed as a percentage.

#### Syntax

RFMXTDSCDMA_ATTR_CDA_RESULTS_MAXIMUM_PEAK_SYMBOL_EVM

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 7417889 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for the default signal and result instances. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__cda__results_1gac78f69a2fc489f4fd4b008d8930c68e9.html language=enus -->
## TOPIC 00032: RFMXTDSCDMA_ATTR_CDA_RESULTS_MEAN_RMS_SYMBOL_MAGNITUDE_ERROR

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__cda__results_1gac78f69a2fc489f4fd4b008d8930c68e9.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__cda__results_1gac78f69a2fc489f4fd4b008d8930c68e9.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the RMS symbol magnitude error for the selected time slot and channel, averaged over all averaging iterations. This value is expressed as a percentage. SyntaxRFMXTDSCDMA_ATTR_CDA_RESULTS_MEAN_RMS_SYMBOL_MAGNITUDE_ERRORNumeric ValueData TypeAccessApplies To7417874float64Read-OnlyN/ARemarks Yo

### RFMXTDSCDMA_ATTR_CDA_RESULTS_MEAN_RMS_SYMBOL_MAGNITUDE_ERROR

Returns the RMS symbol magnitude error for the selected time slot and channel, averaged over all averaging iterations. This value is expressed as a percentage.

#### Syntax

RFMXTDSCDMA_ATTR_CDA_RESULTS_MEAN_RMS_SYMBOL_MAGNITUDE_ERROR

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 7417874 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for the default signal and result instances. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__cda__results_1gace9fc5ba21ca64b20b8103ffc55ea84b.html language=enus -->
## TOPIC 00033: RFMXTDSCDMA_ATTR_CDA_RESULTS_MAXIMUM_TOTAL_ACTIVE_POWER

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__cda__results_1gace9fc5ba21ca64b20b8103ffc55ea84b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__cda__results_1gace9fc5ba21ca64b20b8103ffc55ea84b.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum value, among all averaging iterations, of total power measured in the code domain of the base spreading factor normalized to the total code domain power. This value is expressed in dB, if you set the RFMXTDSCDMA_ATTR_CDA_POWER_UNIT attribute to dB, or in dBm, if you set the CDA P

### RFMXTDSCDMA_ATTR_CDA_RESULTS_MAXIMUM_TOTAL_ACTIVE_POWER

Returns the maximum value, among all averaging iterations, of total power measured in the code domain of the base spreading factor normalized to the total code domain power. This value is expressed in dB, if you set the [RFMXTDSCDMA_ATTR_CDA_POWER_UNIT](group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__cda_1ga68e706878d05d27db97c7c3da7f3fed6.html) attribute to **dB**, or in dBm, if you set the CDA Pwr Unit attribute to **dBm**.

#### Syntax

RFMXTDSCDMA_ATTR_CDA_RESULTS_MAXIMUM_TOTAL_ACTIVE_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 7417893 | float64 | Read-Only | N/A |

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__cda__results_1gaf9872be2a9bfba43d12b08e5f2a2430c.html language=enus -->
## TOPIC 00034: RFMXTDSCDMA_ATTR_CDA_RESULTS_MEAN_TOTAL_POWER

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__cda__results_1gaf9872be2a9bfba43d12b08e5f2a2430c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__cda__results_1gaf9872be2a9bfba43d12b08e5f2a2430c.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the total power measured in the code domain of the base spreading factor, averaged over all averaging iterations. This value is expressed in dBm. SyntaxRFMXTDSCDMA_ATTR_CDA_RESULTS_MEAN_TOTAL_POWERNumeric ValueData TypeAccessApplies To7417881float64Read-OnlyN/ARemarks You do not need to use

### RFMXTDSCDMA_ATTR_CDA_RESULTS_MEAN_TOTAL_POWER

Returns the total power measured in the code domain of the base spreading factor, averaged over all averaging iterations. This value is expressed in dBm.

#### Syntax

RFMXTDSCDMA_ATTR_CDA_RESULTS_MEAN_TOTAL_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 7417881 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for the default signal and result instances. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__cda__results_1gafed078ec01db83c64e81ec0920e38f89.html language=enus -->
## TOPIC 00035: RFMXTDSCDMA_ATTR_CDA_RESULTS_FREQUENCY_ERROR

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__cda__results_1gafed078ec01db83c64e81ec0920e38f89.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__cda__results_1gafed078ec01db83c64e81ec0920e38f89.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the frequency error averaged over all measured slots. This value is expressed in Hz. SyntaxRFMXTDSCDMA_ATTR_CDA_RESULTS_FREQUENCY_ERRORNumeric ValueData TypeAccessApplies To7417879float64Read-OnlyN/ARemarks You do not need to use a selector string to read this result for the default signal a

### RFMXTDSCDMA_ATTR_CDA_RESULTS_FREQUENCY_ERROR

Returns the frequency error averaged over all measured slots. This value is expressed in Hz.

#### Syntax

RFMXTDSCDMA_ATTR_CDA_RESULTS_FREQUENCY_ERROR

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 7417879 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for the default signal and result instances. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__channel.html language=enus -->
## TOPIC 00036: Channel

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__channel.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__channel.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsUser DefinedGroup membersNameDescriptionRFMXTDSCDMA_ATTR_CHANNEL_CONFIGURATION_MODESpecifies whether to detect the channels automatically or to use a specified channel configuration. AttachmentsNone

### Channel

#### Groups

- User Defined

#### Group members

| Name | Description |
| --- | --- |
| RFMXTDSCDMA_ATTR_CHANNEL_CONFIGURATION_MODE | Specifies whether to detect the channels automatically or to use a specified channel configuration. |

#### Attachments

None

Parent topic:

Attributes

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__channel_1gaccad066733fbfbee5fceec4996afa266.html language=enus -->
## TOPIC 00037: RFMXTDSCDMA_ATTR_CHANNEL_CONFIGURATION_MODE

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__channel_1gaccad066733fbfbee5fceec4996afa266.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__channel_1gaccad066733fbfbee5fceec4996afa266.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to detect the channels automatically or to use a specified channel configuration. SyntaxRFMXTDSCDMA_ATTR_CHANNEL_CONFIGURATION_MODENumeric ValueData TypeAccessApplies To7340048int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for

### RFMXTDSCDMA_ATTR_CHANNEL_CONFIGURATION_MODE

Specifies whether to detect the channels automatically or to use a specified channel configuration.

#### Syntax

RFMXTDSCDMA_ATTR_CHANNEL_CONFIGURATION_MODE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 7340048 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **Auto Detect**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXTDSCDMA_VAL_CHANNEL_CONFIGURATION_MODE_AUTO_DETECT | 0 (0x0) | RFmx TD-SCDMA detects the channels automatically. |
| RFMXTDSCDMA_VAL_CHANNEL_CONFIGURATION_MODE_USER_DEFINED | 1 (0x1) | The channel configuration is defined manually. This mode increases measurement speed because no time is spent on channel detection. |

Parent topic:

Channel

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__channel__user__defined.html language=enus -->
## TOPIC 00038: User Defined

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__channel__user__defined.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__channel__user__defined.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXTDSCDMA_ATTR_CHANNELIZATION_CODESpecifies the channelization code of the user-defined channel. This attribute is used only when you set the RFMXTDSCDMA_ATTR_CHANNEL_CONFIGURATION_MODE attribute to User Defined. RFMXTDSCDMA_ATTR_CHANNEL_TYPESpecifies the chan

### User Defined

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXTDSCDMA_ATTR_CHANNELIZATION_CODE | Specifies the channelization code of the user-defined channel. This attribute is used only when you set the RFMXTDSCDMA_ATTR_CHANNEL_CONFIGURATION_MODE attribute to User Defined. |
| RFMXTDSCDMA_ATTR_CHANNEL_TYPE | Specifies the channel type of the user-defined channel. This attribute is used only when you set the RFMXTDSCDMA_ATTR_CHANNEL_CONFIGURATION_MODE attribute to User Defined. |
| RFMXTDSCDMA_ATTR_MODULATION_TYPE | Specifies the modulation type of the user-defined channel. This attribute is used only when you set the RFMXTDSCDMA_ATTR_CHANNEL_CONFIGURATION_MODE attribute to User Defined. |
| RFMXTDSCDMA_ATTR_NUMBER_OF_CHANNELS | Specifies the number of user-defined channels. This attribute is used only when you set the RFMXTDSCDMA_ATTR_CHANNEL_CONFIGURATION_MODE attribute to User Defined. |
| RFMXTDSCDMA_ATTR_SLOT_FORMAT | Specifies the spreading factor, the number of TFCI code words, the number of transmit power control bits, and the number of synchronization shift bits. This attribute is used only when you set the RFMXTDSCDMA_ATTR_CHANNEL_CONFIGURATION_MODE attribute to User Defined. |
| RFMXTDSCDMA_ATTR_SLOT_INDEX | Specifies the slot index of the user-defined channel. This attribute is used only when you set the RFMXTDSCDMA_ATTR_CHANNEL_CONFIGURATION_MODE attribute to User Defined. |

#### Attachments

None

Parent topic:

Channel

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__channel__user__defined_1ga08db62fd826576ca63c701b04677cb4d.html language=enus -->
## TOPIC 00039: RFMXTDSCDMA_ATTR_CHANNELIZATION_CODE

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__channel__user__defined_1ga08db62fd826576ca63c701b04677cb4d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__channel__user__defined_1ga08db62fd826576ca63c701b04677cb4d.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the channelization code of the user-defined channel. This attribute is used only when you set the RFMXTDSCDMA_ATTR_CHANNEL_CONFIGURATION_MODE attribute to User Defined. SyntaxRFMXTDSCDMA_ATTR_CHANNELIZATION_CODENumeric ValueData TypeAccessApplies To7340057int32Read/WriteChannelRemarks Use

### RFMXTDSCDMA_ATTR_CHANNELIZATION_CODE

Specifies the channelization code of the user-defined channel. This attribute is used only when you set the [RFMXTDSCDMA_ATTR_CHANNEL_CONFIGURATION_MODE](group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__channel_1gaccad066733fbfbee5fceec4996afa266.html) attribute to **User Defined**.

#### Syntax

RFMXTDSCDMA_ATTR_CHANNELIZATION_CODE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 7340057 | int32 | Read/Write | Channel |

#### Remarks

Use "channel<i><n></i>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute.

The default value is 1.

Parent topic:

User Defined

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__channel__user__defined_1ga489586d460ccf85eb17f90490396c253.html language=enus -->
## TOPIC 00040: RFMXTDSCDMA_ATTR_SLOT_INDEX

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__channel__user__defined_1ga489586d460ccf85eb17f90490396c253.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__channel__user__defined_1ga489586d460ccf85eb17f90490396c253.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the slot index of the user-defined channel. This attribute is used only when you set the RFMXTDSCDMA_ATTR_CHANNEL_CONFIGURATION_MODE attribute to User Defined. SyntaxRFMXTDSCDMA_ATTR_SLOT_INDEXNumeric ValueData TypeAccessApplies To7340053int32Read/WriteChannelRemarks Use "channel<i><n></i>

### RFMXTDSCDMA_ATTR_SLOT_INDEX

Specifies the slot index of the user-defined channel. This attribute is used only when you set the [RFMXTDSCDMA_ATTR_CHANNEL_CONFIGURATION_MODE](group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__channel_1gaccad066733fbfbee5fceec4996afa266.html) attribute to **User Defined**.

#### Syntax

RFMXTDSCDMA_ATTR_SLOT_INDEX

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 7340053 | int32 | Read/Write | Channel |

#### Remarks

Use "channel<i><n></i>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute.

The default value is 0.

Parent topic:

User Defined

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__channel__user__defined_1gabab9f50a99048a66144c64ad1b7a5afa.html language=enus -->
## TOPIC 00041: RFMXTDSCDMA_ATTR_NUMBER_OF_CHANNELS

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__channel__user__defined_1gabab9f50a99048a66144c64ad1b7a5afa.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__channel__user__defined_1gabab9f50a99048a66144c64ad1b7a5afa.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of user-defined channels. This attribute is used only when you set the RFMXTDSCDMA_ATTR_CHANNEL_CONFIGURATION_MODE attribute to User Defined. SyntaxRFMXTDSCDMA_ATTR_NUMBER_OF_CHANNELSNumeric ValueData TypeAccessApplies To7340052int32Read/WriteN/ARemarks You do not need to use a

### RFMXTDSCDMA_ATTR_NUMBER_OF_CHANNELS

Specifies the number of user-defined channels. This attribute is used only when you set the [RFMXTDSCDMA_ATTR_CHANNEL_CONFIGURATION_MODE](group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__channel_1gaccad066733fbfbee5fceec4996afa266.html) attribute to **User Defined**.

#### Syntax

RFMXTDSCDMA_ATTR_NUMBER_OF_CHANNELS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 7340052 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 0.

Parent topic:

User Defined

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__channel__user__defined_1gacf119f1e110dec472f4891435e059347.html language=enus -->
## TOPIC 00042: RFMXTDSCDMA_ATTR_SLOT_FORMAT

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__channel__user__defined_1gacf119f1e110dec472f4891435e059347.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__channel__user__defined_1gacf119f1e110dec472f4891435e059347.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the spreading factor, the number of TFCI code words, the number of transmit power control bits, and the number of synchronization shift bits. This attribute is used only when you set the RFMXTDSCDMA_ATTR_CHANNEL_CONFIGURATION_MODE attribute to User Defined. SyntaxRFMXTDSCDMA_ATTR_SLOT_FORM

### RFMXTDSCDMA_ATTR_SLOT_FORMAT

Specifies the spreading factor, the number of TFCI code words, the number of transmit power control bits, and the number of synchronization shift bits. This attribute is used only when you set the [RFMXTDSCDMA_ATTR_CHANNEL_CONFIGURATION_MODE](group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__channel_1gaccad066733fbfbee5fceec4996afa266.html) attribute to **User Defined**.

#### Syntax

RFMXTDSCDMA_ATTR_SLOT_FORMAT

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 7340056 | int32 | Read/Write | Channel |

#### Remarks

Use "channel<i><n></i>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute.

Refer to the 3GPP TS 25.221 V11.0.0 standard for detailed information about slot format.

The default value is 0.

Parent topic:

User Defined

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__chp.html language=enus -->
## TOPIC 00043: CHP

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__chp.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__chp.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsAveragingRBW FilterResultsSweep TimeGroup membersNameDescriptionRFMXTDSCDMA_ATTR_CHP_ALL_TRACES_ENABLEDSpecifies whether to enable the traces to be stored and retrieved after performing the CHP measurement. RFMXTDSCDMA_ATTR_CHP_INTEGRATION_BANDWIDTHReturns the CHP carrier integration bandwidth

### CHP

#### Groups

- Averaging
- RBW Filter
- Results
- Sweep Time

#### Group members

| Name | Description |
| --- | --- |
| RFMXTDSCDMA_ATTR_CHP_ALL_TRACES_ENABLED | Specifies whether to enable the traces to be stored and retrieved after performing the CHP measurement. |
| RFMXTDSCDMA_ATTR_CHP_INTEGRATION_BANDWIDTH | Returns the CHP carrier integration bandwidth. This value is expressed in Hz. |
| RFMXTDSCDMA_ATTR_CHP_MEASUREMENT_ENABLED | Specifies whether to enable the CHP measurement. |
| RFMXTDSCDMA_ATTR_CHP_NUMBER_OF_ANALYSIS_THREADS | Specifies the maximum number of threads used for parallelism for the CHP measurement. |

#### Attachments

None

Parent topic:

Attributes

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__chp_1ga06e66c8778787c96a70500b61224e24a.html language=enus -->
## TOPIC 00044: RFMXTDSCDMA_ATTR_CHP_MEASUREMENT_ENABLED

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__chp_1ga06e66c8778787c96a70500b61224e24a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__chp_1ga06e66c8778787c96a70500b61224e24a.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the CHP measurement. SyntaxRFMXTDSCDMA_ATTR_CHP_MEASUREMENT_ENABLEDNumeric ValueData TypeAccessApplies To7352320int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector St

### RFMXTDSCDMA_ATTR_CHP_MEASUREMENT_ENABLED

Specifies whether to enable the CHP measurement.

#### Syntax

RFMXTDSCDMA_ATTR_CHP_MEASUREMENT_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 7352320 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is FALSE.

Parent topic:

CHP

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__chp_1ga527573d72ec1d9628fde4dc840fa6f84.html language=enus -->
## TOPIC 00045: RFMXTDSCDMA_ATTR_CHP_ALL_TRACES_ENABLED

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__chp_1ga527573d72ec1d9628fde4dc840fa6f84.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__chp_1ga527573d72ec1d9628fde4dc840fa6f84.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the traces to be stored and retrieved after performing the CHP measurement. SyntaxRFMXTDSCDMA_ATTR_CHP_ALL_TRACES_ENABLEDNumeric ValueData TypeAccessApplies To7352340int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for

### RFMXTDSCDMA_ATTR_CHP_ALL_TRACES_ENABLED

Specifies whether to enable the traces to be stored and retrieved after performing the CHP measurement.

#### Syntax

RFMXTDSCDMA_ATTR_CHP_ALL_TRACES_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 7352340 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is FALSE.

Parent topic:

CHP

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__chp_1ga80d0921d5ff6b1a786fad3e9897af24b.html language=enus -->
## TOPIC 00046: RFMXTDSCDMA_ATTR_CHP_NUMBER_OF_ANALYSIS_THREADS

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__chp_1ga80d0921d5ff6b1a786fad3e9897af24b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__chp_1ga80d0921d5ff6b1a786fad3e9897af24b.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the maximum number of threads used for parallelism for the CHP measurement. SyntaxRFMXTDSCDMA_ATTR_CHP_NUMBER_OF_ANALYSIS_THREADSNumeric ValueData TypeAccessApplies To7352323int32Read/WriteN/ARemarks The number of threads can range from 1 to the number of physical cores. The number of thre

### RFMXTDSCDMA_ATTR_CHP_NUMBER_OF_ANALYSIS_THREADS

Specifies the maximum number of threads used for parallelism for the CHP measurement.

#### Syntax

RFMXTDSCDMA_ATTR_CHP_NUMBER_OF_ANALYSIS_THREADS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 7352323 | int32 | Read/Write | N/A |

#### Remarks

The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations.

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 1.

Parent topic:

CHP

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__chp_1gad6ce4e0e99f8c5bf6ad7afb2a59a9223.html language=enus -->
## TOPIC 00047: RFMXTDSCDMA_ATTR_CHP_INTEGRATION_BANDWIDTH

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__chp_1gad6ce4e0e99f8c5bf6ad7afb2a59a9223.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__chp_1gad6ce4e0e99f8c5bf6ad7afb2a59a9223.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the CHP carrier integration bandwidth. This value is expressed in Hz. SyntaxRFMXTDSCDMA_ATTR_CHP_INTEGRATION_BANDWIDTHNumeric ValueData TypeAccessApplies To7352322float64Read-OnlyN/ARemarks You do not need to use a selector string to read this attribute for the default signal and result inst

### RFMXTDSCDMA_ATTR_CHP_INTEGRATION_BANDWIDTH

Returns the CHP carrier integration bandwidth. This value is expressed in Hz.

#### Syntax

RFMXTDSCDMA_ATTR_CHP_INTEGRATION_BANDWIDTH

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 7352322 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this attribute for the default signal and result instances. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

Parent topic:

CHP

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__chp__averaging.html language=enus -->
## TOPIC 00048: Averaging

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__chp__averaging.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__chp__averaging.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXTDSCDMA_ATTR_CHP_AVERAGING_COUNTSpecifies the number of acquisitions used for averaging when you set the RFMXTDSCDMA_ATTR_CHP_AVERAGING_ENABLED attribute to True. RFMXTDSCDMA_ATTR_CHP_AVERAGING_ENABLEDSpecifies whether to enable averaging for the CHP measure

### Averaging

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXTDSCDMA_ATTR_CHP_AVERAGING_COUNT | Specifies the number of acquisitions used for averaging when you set the RFMXTDSCDMA_ATTR_CHP_AVERAGING_ENABLED attribute to True. |
| RFMXTDSCDMA_ATTR_CHP_AVERAGING_ENABLED | Specifies whether to enable averaging for the CHP measurement. |
| RFMXTDSCDMA_ATTR_CHP_AVERAGING_TYPE | Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the CHP measurement. |

#### Attachments

None

Parent topic:

CHP

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__chp__averaging_1ga9aabfa6ee971e5559da2617e2654fce6.html language=enus -->
## TOPIC 00049: RFMXTDSCDMA_ATTR_CHP_AVERAGING_COUNT

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__chp__averaging_1ga9aabfa6ee971e5559da2617e2654fce6.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__chp__averaging_1ga9aabfa6ee971e5559da2617e2654fce6.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of acquisitions used for averaging when you set the RFMXTDSCDMA_ATTR_CHP_AVERAGING_ENABLED attribute to True. SyntaxRFMXTDSCDMA_ATTR_CHP_AVERAGING_COUNTNumeric ValueData TypeAccessApplies To7352326int32Read/WriteN/ARemarks You do not need to use a selector string to configure or

### RFMXTDSCDMA_ATTR_CHP_AVERAGING_COUNT

Specifies the number of acquisitions used for averaging when you set the [RFMXTDSCDMA_ATTR_CHP_AVERAGING_ENABLED](group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__chp__averaging_1ga9bf9274405e40cfa9ff2d5a56b611550.html) attribute to **True**.

#### Syntax

RFMXTDSCDMA_ATTR_CHP_AVERAGING_COUNT

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 7352326 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 10.

Parent topic:

Averaging

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__chp__averaging_1ga9bf9274405e40cfa9ff2d5a56b611550.html language=enus -->
## TOPIC 00050: RFMXTDSCDMA_ATTR_CHP_AVERAGING_ENABLED

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__chp__averaging_1ga9bf9274405e40cfa9ff2d5a56b611550.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__chp__averaging_1ga9bf9274405e40cfa9ff2d5a56b611550.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable averaging for the CHP measurement. SyntaxRFMXTDSCDMA_ATTR_CHP_AVERAGING_ENABLEDNumeric ValueData TypeAccessApplies To7352327int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the

### RFMXTDSCDMA_ATTR_CHP_AVERAGING_ENABLED

Specifies whether to enable averaging for the CHP measurement.

#### Syntax

RFMXTDSCDMA_ATTR_CHP_AVERAGING_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 7352327 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **False**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXTDSCDMA_VAL_CHP_AVERAGING_ENABLED_FALSE | 0 (0x0) | The measurement is performed on a single acquisition. |
| RFMXTDSCDMA_VAL_CHP_AVERAGING_ENABLED_TRUE | 1 (0x1) | The CHP measurement uses the RFMXTDSCDMA_ATTR_CHP_AVERAGING_COUNT attribute as the number of acquisitions over which the CHP measurement is averaged. |

Parent topic:

Averaging

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__chp__averaging_1gad51abca6de825b84477ac6ea2b0d9ee9.html language=enus -->
## TOPIC 00051: RFMXTDSCDMA_ATTR_CHP_AVERAGING_TYPE

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__chp__averaging_1gad51abca6de825b84477ac6ea2b0d9ee9.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__chp__averaging_1gad51abca6de825b84477ac6ea2b0d9ee9.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the CHP measurement. SyntaxRFMXTDSCDMA_ATTR_CHP_AVERAGING_TYPENumeric ValueData TypeAccessApplies To7352329int32Read/WriteN/ARemarks You do not need to use a selector string to configure or r

### RFMXTDSCDMA_ATTR_CHP_AVERAGING_TYPE

Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the CHP measurement.

#### Syntax

RFMXTDSCDMA_ATTR_CHP_AVERAGING_TYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 7352329 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **RMS**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXTDSCDMA_VAL_CHP_AVERAGING_TYPE_RMS | 0 (0x0) | The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. |
| RFMXTDSCDMA_VAL_CHP_AVERAGING_TYPE_LOG | 1 (0x1) | The power spectrum is averaged on a logarithmic scale. |
| RFMXTDSCDMA_VAL_CHP_AVERAGING_TYPE_SCALAR | 2 (0x2) | The square root of the power spectrum is averaged. |
| RFMXTDSCDMA_VAL_CHP_AVERAGING_TYPE_MAXIMUM | 3 (0x3) | The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. |
| RFMXTDSCDMA_VAL_CHP_AVERAGING_TYPE_MINIMUM | 4 (0x4) | The lowest power in the spectrum at each frequency bin is retained from one acquisition to the next. |

Parent topic:

Averaging

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__chp__rbw__filter.html language=enus -->
## TOPIC 00052: RBW Filter

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__chp__rbw__filter.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__chp__rbw__filter.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXTDSCDMA_ATTR_CHP_RBW_FILTER_AUTO_BANDWIDTHSpecifies whether the measurement calculates the RBW. RFMXTDSCDMA_ATTR_CHP_RBW_FILTER_BANDWIDTHSpecifies the bandwidth of the RBW filter used to sweep the acquired signal when you set the RFMXTDSCDMA_ATTR_CHP_RBW_FIL

### RBW Filter

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXTDSCDMA_ATTR_CHP_RBW_FILTER_AUTO_BANDWIDTH | Specifies whether the measurement calculates the RBW. |
| RFMXTDSCDMA_ATTR_CHP_RBW_FILTER_BANDWIDTH | Specifies the bandwidth of the RBW filter used to sweep the acquired signal when you set the RFMXTDSCDMA_ATTR_CHP_RBW_FILTER_AUTO_BANDWIDTH attribute to False. This value is expressed in Hz. |
| RFMXTDSCDMA_ATTR_CHP_RBW_FILTER_TYPE | Specifies the shape of the digital RBW filter. |

#### Attachments

None

Parent topic:

CHP

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__chp__rbw__filter_1ga9e493864507a089a7b35755b5f55ad07.html language=enus -->
## TOPIC 00053: RFMXTDSCDMA_ATTR_CHP_RBW_FILTER_TYPE

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__chp__rbw__filter_1ga9e493864507a089a7b35755b5f55ad07.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__chp__rbw__filter_1ga9e493864507a089a7b35755b5f55ad07.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the shape of the digital RBW filter. SyntaxRFMXTDSCDMA_ATTR_CHP_RBW_FILTER_TYPENumeric ValueData TypeAccessApplies To7352334int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector String t

### RFMXTDSCDMA_ATTR_CHP_RBW_FILTER_TYPE

Specifies the shape of the digital RBW filter.

#### Syntax

RFMXTDSCDMA_ATTR_CHP_RBW_FILTER_TYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 7352334 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **FFT Based**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXTDSCDMA_VAL_CHP_RBW_FILTER_TYPE_FFT_BASED | 0 (0x0) | An RBW filter with a fast Fourier transform (FFT)-based response is applied. |
| RFMXTDSCDMA_VAL_CHP_RBW_FILTER_TYPE_GAUSSIAN | 1 (0x1) | An RBW filter with a Gaussian response is applied. |
| RFMXTDSCDMA_VAL_CHP_RBW_FILTER_TYPE_FLAT | 2 (0x2) | An RBW filter with a flat response is applied. |

Parent topic:

RBW Filter

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__chp__rbw__filter_1gab4c9aa4f26d30243164a080b68b10528.html language=enus -->
## TOPIC 00054: RFMXTDSCDMA_ATTR_CHP_RBW_FILTER_AUTO_BANDWIDTH

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__chp__rbw__filter_1gab4c9aa4f26d30243164a080b68b10528.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__chp__rbw__filter_1gab4c9aa4f26d30243164a080b68b10528.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement calculates the RBW. SyntaxRFMXTDSCDMA_ATTR_CHP_RBW_FILTER_AUTO_BANDWIDTHNumeric ValueData TypeAccessApplies To7352332int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the

### RFMXTDSCDMA_ATTR_CHP_RBW_FILTER_AUTO_BANDWIDTH

Specifies whether the measurement calculates the RBW.

#### Syntax

RFMXTDSCDMA_ATTR_CHP_RBW_FILTER_AUTO_BANDWIDTH

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 7352332 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **True**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXTDSCDMA_VAL_CHP_RBW_AUTO_FALSE | 0 (0x0) | The measurement uses the RBW you specify. |
| RFMXTDSCDMA_VAL_CHP_RBW_AUTO_TRUE | 1 (0x1) | RFmx TD-SCDMA automatically calculates the RBW. |

Parent topic:

RBW Filter

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__chp__rbw__filter_1gaba653e0bb4490ac32fad6c38fab4a747.html language=enus -->
## TOPIC 00055: RFMXTDSCDMA_ATTR_CHP_RBW_FILTER_BANDWIDTH

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__chp__rbw__filter_1gaba653e0bb4490ac32fad6c38fab4a747.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__chp__rbw__filter_1gaba653e0bb4490ac32fad6c38fab4a747.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the bandwidth of the RBW filter used to sweep the acquired signal when you set the RFMXTDSCDMA_ATTR_CHP_RBW_FILTER_AUTO_BANDWIDTH attribute to False. This value is expressed in Hz. SyntaxRFMXTDSCDMA_ATTR_CHP_RBW_FILTER_BANDWIDTHNumeric ValueData TypeAccessApplies To7352333float64Read/Write

### RFMXTDSCDMA_ATTR_CHP_RBW_FILTER_BANDWIDTH

Specifies the bandwidth of the RBW filter used to sweep the acquired signal when you set the [RFMXTDSCDMA_ATTR_CHP_RBW_FILTER_AUTO_BANDWIDTH](group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__chp__rbw__filter_1gab4c9aa4f26d30243164a080b68b10528.html) attribute to **False**. This value is expressed in Hz.

#### Syntax

RFMXTDSCDMA_ATTR_CHP_RBW_FILTER_BANDWIDTH

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 7352333 | float64 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 5.636 kHz.

Parent topic:

RBW Filter

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__chp__results.html language=enus -->
## TOPIC 00056: Results

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__chp__results.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__chp__results.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXTDSCDMA_ATTR_CHP_RESULTS_CARRIER_ABSOLUTE_POWERReturns the averaged CHP measured in the specified integration bandwidth. This value is expressed in dBm. AttachmentsNone

### Results

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXTDSCDMA_ATTR_CHP_RESULTS_CARRIER_ABSOLUTE_POWER | Returns the averaged CHP measured in the specified integration bandwidth. This value is expressed in dBm. |

#### Attachments

None

Parent topic:

CHP

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__chp__results_1ga1fbb344eaadcf886e792684f36dde089.html language=enus -->
## TOPIC 00057: RFMXTDSCDMA_ATTR_CHP_RESULTS_CARRIER_ABSOLUTE_POWER

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__chp__results_1ga1fbb344eaadcf886e792684f36dde089.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__chp__results_1ga1fbb344eaadcf886e792684f36dde089.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the averaged CHP measured in the specified integration bandwidth. This value is expressed in dBm. SyntaxRFMXTDSCDMA_ATTR_CHP_RESULTS_CARRIER_ABSOLUTE_POWERNumeric ValueData TypeAccessApplies To7352341float64Read-OnlyN/ARemarks You do not need to use a selector string to read this result for

### RFMXTDSCDMA_ATTR_CHP_RESULTS_CARRIER_ABSOLUTE_POWER

Returns the averaged CHP measured in the specified integration bandwidth. This value is expressed in dBm.

#### Syntax

RFMXTDSCDMA_ATTR_CHP_RESULTS_CARRIER_ABSOLUTE_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 7352341 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for the default signal and result instances. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__chp__sweep__time.html language=enus -->
## TOPIC 00058: Sweep Time

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__chp__sweep__time.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__chp__sweep__time.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXTDSCDMA_ATTR_CHP_SWEEP_TIME_AUTOSpecifies whether the measurement calculates the sweep time. RFMXTDSCDMA_ATTR_CHP_SWEEP_TIME_INTERVALSpecifies the sweep time when you set the RFMXTDSCDMA_ATTR_CHP_SWEEP_TIME_AUTO attribute to False. This value is expressed in

### Sweep Time

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXTDSCDMA_ATTR_CHP_SWEEP_TIME_AUTO | Specifies whether the measurement calculates the sweep time. |
| RFMXTDSCDMA_ATTR_CHP_SWEEP_TIME_INTERVAL | Specifies the sweep time when you set the RFMXTDSCDMA_ATTR_CHP_SWEEP_TIME_AUTO attribute to False. This value is expressed in seconds. |

#### Attachments

None

Parent topic:

CHP

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__chp__sweep__time_1ga9cf54a866da15bb783d1bb9ce2c5ecc8.html language=enus -->
## TOPIC 00059: RFMXTDSCDMA_ATTR_CHP_SWEEP_TIME_AUTO

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__chp__sweep__time_1ga9cf54a866da15bb783d1bb9ce2c5ecc8.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__chp__sweep__time_1ga9cf54a866da15bb783d1bb9ce2c5ecc8.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement calculates the sweep time. SyntaxRFMXTDSCDMA_ATTR_CHP_SWEEP_TIME_AUTONumeric ValueData TypeAccessApplies To7352337int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Sel

### RFMXTDSCDMA_ATTR_CHP_SWEEP_TIME_AUTO

Specifies whether the measurement calculates the sweep time.

#### Syntax

RFMXTDSCDMA_ATTR_CHP_SWEEP_TIME_AUTO

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 7352337 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **True**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXTDSCDMA_VAL_CHP_SWEEP_TIME_AUTO_FALSE | 0 (0x0) | The measurement uses the sweep time you specify in the RFMXTDSCDMA_ATTR_CHP_SWEEP_TIME_INTERVAL attribute. |
| RFMXTDSCDMA_VAL_CHP_SWEEP_TIME_AUTO_TRUE | 1 (0x1) | The measurement uses the default sweep time of .00066 seconds (s). |

Parent topic:

Sweep Time

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__chp__sweep__time_1gaca2673e23fd33f834c58bffdfa5f2099.html language=enus -->
## TOPIC 00060: RFMXTDSCDMA_ATTR_CHP_SWEEP_TIME_INTERVAL

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__chp__sweep__time_1gaca2673e23fd33f834c58bffdfa5f2099.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__chp__sweep__time_1gaca2673e23fd33f834c58bffdfa5f2099.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the sweep time when you set the RFMXTDSCDMA_ATTR_CHP_SWEEP_TIME_AUTO attribute to False. This value is expressed in seconds. SyntaxRFMXTDSCDMA_ATTR_CHP_SWEEP_TIME_INTERVALNumeric ValueData TypeAccessApplies To7352338float64Read/WriteN/ARemarks You do not need to use a selector string to co

### RFMXTDSCDMA_ATTR_CHP_SWEEP_TIME_INTERVAL

Specifies the sweep time when you set the [RFMXTDSCDMA_ATTR_CHP_SWEEP_TIME_AUTO](group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__chp__sweep__time_1ga9cf54a866da15bb783d1bb9ce2c5ecc8.html) attribute to **False**. This value is expressed in seconds.

#### Syntax

RFMXTDSCDMA_ATTR_CHP_SWEEP_TIME_INTERVAL

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 7352338 | float64 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 0.00066 s.

Parent topic:

Sweep Time

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__midamble.html language=enus -->
## TOPIC 00061: Midamble

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__midamble.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__midamble.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXTDSCDMA_ATTR_MIDAMBLE_AUTO_DETECTION_MODESpecifies the midamble auto detection mode. RFMXTDSCDMA_ATTR_MIDAMBLE_SHIFTSpecifies the midamble shift used when you set the RFMXTDSCDMA_ATTR_MIDAMBLE_AUTO_DETECTION_MODE attribute to Off. This value is expressed in

### Midamble

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXTDSCDMA_ATTR_MIDAMBLE_AUTO_DETECTION_MODE | Specifies the midamble auto detection mode. |
| RFMXTDSCDMA_ATTR_MIDAMBLE_SHIFT | Specifies the midamble shift used when you set the RFMXTDSCDMA_ATTR_MIDAMBLE_AUTO_DETECTION_MODE attribute to Off. This value is expressed in chips. |

#### Attachments

None

Parent topic:

Attributes

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__midamble_1ga9ebc0dd16dab65a552a57ce81f4f9fb8.html language=enus -->
## TOPIC 00062: RFMXTDSCDMA_ATTR_MIDAMBLE_SHIFT

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__midamble_1ga9ebc0dd16dab65a552a57ce81f4f9fb8.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__midamble_1ga9ebc0dd16dab65a552a57ce81f4f9fb8.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the midamble shift used when you set the RFMXTDSCDMA_ATTR_MIDAMBLE_AUTO_DETECTION_MODE attribute to Off. This value is expressed in chips. SyntaxRFMXTDSCDMA_ATTR_MIDAMBLE_SHIFTNumeric ValueData TypeAccessApplies To7409673int32Read/WriteN/ARemarks You do not need to use a selector string to

### RFMXTDSCDMA_ATTR_MIDAMBLE_SHIFT

Specifies the midamble shift used when you set the [RFMXTDSCDMA_ATTR_MIDAMBLE_AUTO_DETECTION_MODE](group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__midamble_1gac8cce16836802af5c55efad755a9c8ec.html) attribute to **Off**. This value is expressed in chips.

#### Syntax

RFMXTDSCDMA_ATTR_MIDAMBLE_SHIFT

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 7409673 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 8.

Parent topic:

Midamble

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__midamble_1gac8cce16836802af5c55efad755a9c8ec.html language=enus -->
## TOPIC 00063: RFMXTDSCDMA_ATTR_MIDAMBLE_AUTO_DETECTION_MODE

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__midamble_1gac8cce16836802af5c55efad755a9c8ec.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__midamble_1gac8cce16836802af5c55efad755a9c8ec.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the midamble auto detection mode. SyntaxRFMXTDSCDMA_ATTR_MIDAMBLE_AUTO_DETECTION_MODENumeric ValueData TypeAccessApplies To7409671int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector St

### RFMXTDSCDMA_ATTR_MIDAMBLE_AUTO_DETECTION_MODE

Specifies the midamble auto detection mode.

#### Syntax

RFMXTDSCDMA_ATTR_MIDAMBLE_AUTO_DETECTION_MODE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 7409671 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **Midamble Shift**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXTDSCDMA_VAL_MIDAMBLE_AUTO_DETECTION_MODE_OFF | 0 (0x0) | Auto detection of the midamble shift is disabled. The measurement uses the midamble shift value that you specify in the RFMXTDSCDMA_ATTR_MIDAMBLE_SHIFT attribute. |
| RFMXTDSCDMA_VAL_MIDAMBLE_AUTO_DETECTION_MODE_MIDAMBLE_SHIFT | 1 (0x1) | The midamble shift is automatically detected from K possible midamble shift values, where K is specified by the RFMXTDSCDMA_ATTR_MAXIMUM_NUMBER_OF_USERS attribute. The K possible midamble shift values are: Midamble Shift = k * floor(P/K), where P is the length of the basic midamble code, and k is an integer from 0 to K-1. |

Parent topic:

Midamble

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc.html language=enus -->
## TOPIC 00064: ModAcc

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsAveragingResultsGroup membersNameDescriptionRFMXTDSCDMA_ATTR_MODACC_ALL_TRACES_ENABLEDSpecifies whether to enable the traces to be stored and retrieved after performing the ModAcc measurement. RFMXTDSCDMA_ATTR_MODACC_IQ_GAIN_IMBALANCE_REMOVAL_ENABLEDSpecifies whether to remove the I/Q gain imb

### ModAcc

#### Groups

- Averaging
- Results

#### Group members

| Name | Description |
| --- | --- |
| RFMXTDSCDMA_ATTR_MODACC_ALL_TRACES_ENABLED | Specifies whether to enable the traces to be stored and retrieved after performing the ModAcc measurement. |
| RFMXTDSCDMA_ATTR_MODACC_IQ_GAIN_IMBALANCE_REMOVAL_ENABLED | Specifies whether to remove the I/Q gain imbalance before the ModAcc measurement. |
| RFMXTDSCDMA_ATTR_MODACC_IQ_OFFSET_REMOVAL_ENABLED | Specifies whether to remove the I/Q offset before the ModAcc measurement. |
| RFMXTDSCDMA_ATTR_MODACC_IQ_QUADRATURE_ERROR_REMOVAL_ENABLED | Specifies whether to remove the I/Q quadrature error before the ModAcc measurement. |
| RFMXTDSCDMA_ATTR_MODACC_MEASUREMENT_ENABLED | Specifies whether to enable the ModAcc measurement. |
| RFMXTDSCDMA_ATTR_MODACC_MEASUREMENT_LENGTH | Specifies the measurement length for the ModAcc measurement. This value is expressed in traffic slots. |
| RFMXTDSCDMA_ATTR_MODACC_MEASUREMENT_OFFSET | Specifies the measurement offset that is skipped by the ModAcc measurement from the synchronization boundary. This value is expressed in traffic slots. The synchronization boundary is specified by the RFMXTDSCDMA_ATTR_MODACC_SYNCHRONIZATION_MODE attribute. |
| RFMXTDSCDMA_ATTR_MODACC_RRC_FILTER_ENABLED | Specifies whether to enable the RRC filter in the ModAcc measurement. Use this attribute to disable the filter if the received signal is already RRC-filtered. |
| RFMXTDSCDMA_ATTR_MODACC_SLOT_TYPE | Specifies the type of the time slot for the ModAcc measurement. |
| RFMXTDSCDMA_ATTR_MODACC_SPECTRUM_INVERTED | Specifies whether the spectrum of the signal is inverted. |
| RFMXTDSCDMA_ATTR_MODACC_SYNCHRONIZATION_MODE | Specifies the synchronization mode for the ModAcc measurement. |

#### Attachments

None

Parent topic:

Attributes

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc_1ga017698cba60ec880f222ea6ae36eb13d.html language=enus -->
## TOPIC 00065: RFMXTDSCDMA_ATTR_MODACC_SLOT_TYPE

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc_1ga017698cba60ec880f222ea6ae36eb13d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc_1ga017698cba60ec880f222ea6ae36eb13d.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the type of the time slot for the ModAcc measurement. SyntaxRFMXTDSCDMA_ATTR_MODACC_SLOT_TYPENumeric ValueData TypeAccessApplies To7409670int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Sel

### RFMXTDSCDMA_ATTR_MODACC_SLOT_TYPE

Specifies the type of the time slot for the ModAcc measurement.

#### Syntax

RFMXTDSCDMA_ATTR_MODACC_SLOT_TYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 7409670 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **Traffic**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXTDSCDMA_VAL_MODACC_SLOT_TYPE_TRAFFIC | 0 (0x0) | The measurement is performed on the traffic time slot. The composite, data, and midamble ModAcc results are obtained when you select this slot type. |
| RFMXTDSCDMA_VAL_MODACC_SLOT_TYPE_PILOT | 1 (0x1) | The measurement is performed on the pilot time slot. The pilot ModAcc results are obtained when you select this slot type. |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc_1ga15d1c1973177fb66d30bd7cc804efa4d.html language=enus -->
## TOPIC 00066: RFMXTDSCDMA_ATTR_MODACC_MEASUREMENT_OFFSET

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc_1ga15d1c1973177fb66d30bd7cc804efa4d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc_1ga15d1c1973177fb66d30bd7cc804efa4d.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the measurement offset that is skipped by the ModAcc measurement from the synchronization boundary. This value is expressed in traffic slots. The synchronization boundary is specified by the RFMXTDSCDMA_ATTR_MODACC_SYNCHRONIZATION_MODE attribute. SyntaxRFMXTDSCDMA_ATTR_MODACC_MEASUREMENT_O

### RFMXTDSCDMA_ATTR_MODACC_MEASUREMENT_OFFSET

Specifies the measurement offset that is skipped by the ModAcc measurement from the synchronization boundary. This value is expressed in traffic slots. The synchronization boundary is specified by the [RFMXTDSCDMA_ATTR_MODACC_SYNCHRONIZATION_MODE](group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc_1ga1c3cfa23ee9d0c4afbd2eab70d1918cc.html) attribute.

#### Syntax

RFMXTDSCDMA_ATTR_MODACC_MEASUREMENT_OFFSET

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 7409667 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 0.

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc_1ga1c3cfa23ee9d0c4afbd2eab70d1918cc.html language=enus -->
## TOPIC 00067: RFMXTDSCDMA_ATTR_MODACC_SYNCHRONIZATION_MODE

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc_1ga1c3cfa23ee9d0c4afbd2eab70d1918cc.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc_1ga1c3cfa23ee9d0c4afbd2eab70d1918cc.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the synchronization mode for the ModAcc measurement. SyntaxRFMXTDSCDMA_ATTR_MODACC_SYNCHRONIZATION_MODENumeric ValueData TypeAccessApplies To7409666int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer

### RFMXTDSCDMA_ATTR_MODACC_SYNCHRONIZATION_MODE

Specifies the synchronization mode for the ModAcc measurement.

#### Syntax

RFMXTDSCDMA_ATTR_MODACC_SYNCHRONIZATION_MODE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 7409666 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **Slot**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXTDSCDMA_VAL_MODACC_SYNCHRONIZATION_MODE_SLOT | 0 (0x0) | The measurement uses the slot synchronization mode. The slot boundary in the acquired signal is detected, and the measurement is performed over the number of slots specified by the RFMXTDSCDMA_ATTR_MODACC_MEASUREMENT_LENGTH attribute, starting at the offset from the boundary specified by the RFMXTDSCDMA_ATTR_MODACC_MEASUREMENT_OFFSET attribute. If you set the RFMXTDSCDMA_ATTR_TRIGGER_TYPE attribute to Digital Edge, you should provide the trigger at the start of the slot from which the ModAcc Meas Offset attribute should be considered. If you set the Trigger Type attribute to IQ Power Edge, it is required that the received signal has either one traffic time slot or contiguous traffic time slots. Additionally, for this trigger type, the traffic time slot(s) in the received signal should be contiguous with the pilot time slot, if the pilot time slot is present. |
| RFMXTDSCDMA_VAL_MODACC_SYNCHRONIZATION_MODE_SUBFRAME | 1 (0x1) | The measurement uses the subframe synchronization mode. The first subframe boundary in the acquired signal is detected, and the measurement is performed over the number of slots specified by the ModAcc Meas Length attribute, starting at the offset from the boundary specified by the ModAcc Meas Offset attribute. If you set the Trigger Type attribute to Digital Edge, you should provide the trigger at the start of the subframe. If you set the Trigger Type attribute to IQ Power Edge, it is required that the received signal has either one traffic time slot or contiguous traffic time slots. Additionally, the traffic time slot should be contiguous with the active pilot time slot. |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc_1ga5f0c26ce6bcecb39c8a852cd86ea86d5.html language=enus -->
## TOPIC 00068: RFMXTDSCDMA_ATTR_MODACC_MEASUREMENT_ENABLED

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc_1ga5f0c26ce6bcecb39c8a852cd86ea86d5.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc_1ga5f0c26ce6bcecb39c8a852cd86ea86d5.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the ModAcc measurement. SyntaxRFMXTDSCDMA_ATTR_MODACC_MEASUREMENT_ENABLEDNumeric ValueData TypeAccessApplies To7409664int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selec

### RFMXTDSCDMA_ATTR_MODACC_MEASUREMENT_ENABLED

Specifies whether to enable the ModAcc measurement.

#### Syntax

RFMXTDSCDMA_ATTR_MODACC_MEASUREMENT_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 7409664 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is FALSE.

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc_1ga7805e2511632325b7fa7a017fec62904.html language=enus -->
## TOPIC 00069: RFMXTDSCDMA_ATTR_MODACC_SPECTRUM_INVERTED

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc_1ga7805e2511632325b7fa7a017fec62904.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc_1ga7805e2511632325b7fa7a017fec62904.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the spectrum of the signal is inverted. SyntaxRFMXTDSCDMA_ATTR_MODACC_SPECTRUM_INVERTEDNumeric ValueData TypeAccessApplies To7409674int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the S

### RFMXTDSCDMA_ATTR_MODACC_SPECTRUM_INVERTED

Specifies whether the spectrum of the signal is inverted.

#### Syntax

RFMXTDSCDMA_ATTR_MODACC_SPECTRUM_INVERTED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 7409674 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **False**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXTDSCDMA_VAL_MODACC_SPECTRUM_INVERTED_FALSE | 0 (0x0) | The measured spectrum is not inverted. |
| RFMXTDSCDMA_VAL_MODACC_SPECTRUM_INVERTED_TRUE | 1 (0x1) | The measured spectrum is inverted. |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc_1ga7bda404d207928c423c910581331ab69.html language=enus -->
## TOPIC 00070: RFMXTDSCDMA_ATTR_MODACC_MEASUREMENT_LENGTH

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc_1ga7bda404d207928c423c910581331ab69.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc_1ga7bda404d207928c423c910581331ab69.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the measurement length for the ModAcc measurement. This value is expressed in traffic slots. SyntaxRFMXTDSCDMA_ATTR_MODACC_MEASUREMENT_LENGTHNumeric ValueData TypeAccessApplies To7409668int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute f

### RFMXTDSCDMA_ATTR_MODACC_MEASUREMENT_LENGTH

Specifies the measurement length for the ModAcc measurement. This value is expressed in traffic slots.

#### Syntax

RFMXTDSCDMA_ATTR_MODACC_MEASUREMENT_LENGTH

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 7409668 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 1.

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc_1ga7c6cb362a3b58cfd1ac8196eeb248ec2.html language=enus -->
## TOPIC 00071: RFMXTDSCDMA_ATTR_MODACC_IQ_GAIN_IMBALANCE_REMOVAL_ENABLED

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc_1ga7c6cb362a3b58cfd1ac8196eeb248ec2.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc_1ga7c6cb362a3b58cfd1ac8196eeb248ec2.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to remove the I/Q gain imbalance before the ModAcc measurement. SyntaxRFMXTDSCDMA_ATTR_MODACC_IQ_GAIN_IMBALANCE_REMOVAL_ENABLEDNumeric ValueData TypeAccessApplies To7409681int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the

### RFMXTDSCDMA_ATTR_MODACC_IQ_GAIN_IMBALANCE_REMOVAL_ENABLED

Specifies whether to remove the I/Q gain imbalance before the ModAcc measurement.

#### Syntax

RFMXTDSCDMA_ATTR_MODACC_IQ_GAIN_IMBALANCE_REMOVAL_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 7409681 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **False**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXTDSCDMA_VAL_MODACC_IQ_GAIN_IMBALANCE_REMOVAL_ENABLED_FALSE | 0 (0x0) | The I/Q gain imbalance is not removed before the ModAcc measurement. |
| RFMXTDSCDMA_VAL_MODACC_IQ_GAIN_IMBALANCE_REMOVAL_ENABLED_TRUE | 1 (0x1) | The I/Q gain imbalance is removed before the ModAcc measurement. |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc_1ga81b61ea462ee59c94801f32db03428d3.html language=enus -->
## TOPIC 00072: RFMXTDSCDMA_ATTR_MODACC_ALL_TRACES_ENABLED

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc_1ga81b61ea462ee59c94801f32db03428d3.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc_1ga81b61ea462ee59c94801f32db03428d3.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the traces to be stored and retrieved after performing the ModAcc measurement. SyntaxRFMXTDSCDMA_ATTR_MODACC_ALL_TRACES_ENABLEDNumeric ValueData TypeAccessApplies To7409692int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribu

### RFMXTDSCDMA_ATTR_MODACC_ALL_TRACES_ENABLED

Specifies whether to enable the traces to be stored and retrieved after performing the ModAcc measurement.

#### Syntax

RFMXTDSCDMA_ATTR_MODACC_ALL_TRACES_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 7409692 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is FALSE.

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc_1ga81ed180b5091bb0f8f36965bb7e416b0.html language=enus -->
## TOPIC 00073: RFMXTDSCDMA_ATTR_MODACC_IQ_QUADRATURE_ERROR_REMOVAL_ENABLED

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc_1ga81ed180b5091bb0f8f36965bb7e416b0.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc_1ga81ed180b5091bb0f8f36965bb7e416b0.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to remove the I/Q quadrature error before the ModAcc measurement. SyntaxRFMXTDSCDMA_ATTR_MODACC_IQ_QUADRATURE_ERROR_REMOVAL_ENABLEDNumeric ValueData TypeAccessApplies To7409682int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for

### RFMXTDSCDMA_ATTR_MODACC_IQ_QUADRATURE_ERROR_REMOVAL_ENABLED

Specifies whether to remove the I/Q quadrature error before the ModAcc measurement.

#### Syntax

RFMXTDSCDMA_ATTR_MODACC_IQ_QUADRATURE_ERROR_REMOVAL_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 7409682 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **False**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXTDSCDMA_VAL_MODACC_IQ_QUADRATURE_ERROR_REMOVAL_ENABLED_FALSE | 0 (0x0) | The I/Q quadrature error is not removed before the ModAcc measurement. |
| RFMXTDSCDMA_VAL_MODACC_IQ_QUADRATURE_ERROR_REMOVAL_ENABLED_TRUE | 1 (0x1) | The I/Q quadrature error is removed before the ModAcc measurement. |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc_1ga8c03b6b8d1a547993cb03688e916873e.html language=enus -->
## TOPIC 00074: RFMXTDSCDMA_ATTR_MODACC_IQ_OFFSET_REMOVAL_ENABLED

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc_1ga8c03b6b8d1a547993cb03688e916873e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc_1ga8c03b6b8d1a547993cb03688e916873e.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to remove the I/Q offset before the ModAcc measurement. SyntaxRFMXTDSCDMA_ATTR_MODACC_IQ_OFFSET_REMOVAL_ENABLEDNumeric ValueData TypeAccessApplies To7409691int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal

### RFMXTDSCDMA_ATTR_MODACC_IQ_OFFSET_REMOVAL_ENABLED

Specifies whether to remove the I/Q offset before the ModAcc measurement.

#### Syntax

RFMXTDSCDMA_ATTR_MODACC_IQ_OFFSET_REMOVAL_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 7409691 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **False**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXTDSCDMA_VAL_MODACC_IQ_OFFSET_REMOVAL_ENABLED_FALSE | 0 (0x0) | The I/Q offset is not removed before the ModAcc measurement. |
| RFMXTDSCDMA_VAL_MODACC_IQ_OFFSET_REMOVAL_ENABLED_TRUE | 1 (0x1) | The I/Q offset is removed before the ModAcc measurement. |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc_1gafe7e3eeae0c70495449f249a44e748c6.html language=enus -->
## TOPIC 00075: RFMXTDSCDMA_ATTR_MODACC_RRC_FILTER_ENABLED

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc_1gafe7e3eeae0c70495449f249a44e748c6.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc_1gafe7e3eeae0c70495449f249a44e748c6.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the RRC filter in the ModAcc measurement. Use this attribute to disable the filter if the received signal is already RRC-filtered. SyntaxRFMXTDSCDMA_ATTR_MODACC_RRC_FILTER_ENABLEDNumeric ValueData TypeAccessApplies To7409683int32Read/WriteN/ARemarks You do not need to use

### RFMXTDSCDMA_ATTR_MODACC_RRC_FILTER_ENABLED

Specifies whether to enable the RRC filter in the ModAcc measurement. Use this attribute to disable the filter if the received signal is already RRC-filtered.

#### Syntax

RFMXTDSCDMA_ATTR_MODACC_RRC_FILTER_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 7409683 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **True**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXTDSCDMA_VAL_MODACC_RRC_FILTER_ENABLED_FALSE | 0 (0x0) | Disables the RRC filter in the ModAcc measurement. |
| RFMXTDSCDMA_VAL_MODACC_RRC_FILTER_ENABLED_TRUE | 1 (0x1) | Enables the RRC filter in the ModAcc measurement. |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc__averaging.html language=enus -->
## TOPIC 00076: Averaging

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc__averaging.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc__averaging.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXTDSCDMA_ATTR_MODACC_AVERAGING_COUNTSpecifies the number of acquisitions used for averaging when you set the RFMXTDSCDMA_ATTR_MODACC_AVERAGING_ENABLED attribute to True. RFMXTDSCDMA_ATTR_MODACC_AVERAGING_ENABLEDSpecifies whether to enable averaging for the Mo

### Averaging

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXTDSCDMA_ATTR_MODACC_AVERAGING_COUNT | Specifies the number of acquisitions used for averaging when you set the RFMXTDSCDMA_ATTR_MODACC_AVERAGING_ENABLED attribute to True. |
| RFMXTDSCDMA_ATTR_MODACC_AVERAGING_ENABLED | Specifies whether to enable averaging for the ModAcc measurement. |

#### Attachments

None

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc__averaging_1ga73e50de45265f6cdba1386d60547f7d2.html language=enus -->
## TOPIC 00077: RFMXTDSCDMA_ATTR_MODACC_AVERAGING_ENABLED

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc__averaging_1ga73e50de45265f6cdba1386d60547f7d2.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc__averaging_1ga73e50de45265f6cdba1386d60547f7d2.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable averaging for the ModAcc measurement. SyntaxRFMXTDSCDMA_ATTR_MODACC_AVERAGING_ENABLEDNumeric ValueData TypeAccessApplies To7409675int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer

### RFMXTDSCDMA_ATTR_MODACC_AVERAGING_ENABLED

Specifies whether to enable averaging for the ModAcc measurement.

#### Syntax

RFMXTDSCDMA_ATTR_MODACC_AVERAGING_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 7409675 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **False**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXTDSCDMA_VAL_MODACC_AVERAGING_ENABLED_FALSE | 0 (0x0) | The measurement is performed on a single acquisition. |
| RFMXTDSCDMA_VAL_MODACC_AVERAGING_ENABLED_TRUE | 1 (0x1) | The ModAcc measurement uses the value of the RFMXTDSCDMA_ATTR_MODACC_AVERAGING_COUNT attribute as the number of acquisitions over which the ModAcc measurement is averaged. |

Parent topic:

Averaging

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc__averaging_1ga79a1ff3e46db8ba70f8098b570e8fb44.html language=enus -->
## TOPIC 00078: RFMXTDSCDMA_ATTR_MODACC_AVERAGING_COUNT

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc__averaging_1ga79a1ff3e46db8ba70f8098b570e8fb44.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc__averaging_1ga79a1ff3e46db8ba70f8098b570e8fb44.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of acquisitions used for averaging when you set the RFMXTDSCDMA_ATTR_MODACC_AVERAGING_ENABLED attribute to True. SyntaxRFMXTDSCDMA_ATTR_MODACC_AVERAGING_COUNTNumeric ValueData TypeAccessApplies To7409677int32Read/WriteN/ARemarks You do not need to use a selector string to config

### RFMXTDSCDMA_ATTR_MODACC_AVERAGING_COUNT

Specifies the number of acquisitions used for averaging when you set the [RFMXTDSCDMA_ATTR_MODACC_AVERAGING_ENABLED](group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc__averaging_1ga73e50de45265f6cdba1386d60547f7d2.html) attribute to **True**.

#### Syntax

RFMXTDSCDMA_ATTR_MODACC_AVERAGING_COUNT

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 7409677 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 10.

Parent topic:

Averaging

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc__results.html language=enus -->
## TOPIC 00079: Results

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc__results.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc__results.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsDataDetected ChannelMidamblePilotGroup membersNameDescriptionRFMXTDSCDMA_ATTR_MODACC_RESULTS_CHIP_RATE_ERRORReturns the chip rate error. This value is expressed in ppm. RFMXTDSCDMA_ATTR_MODACC_RESULTS_COMPOSITE_RHOReturns the composite value of rho, averaged over all active time slots and all

### Results

#### Groups

- Data
- Detected Channel
- Midamble
- Pilot

#### Group members

| Name | Description |
| --- | --- |
| RFMXTDSCDMA_ATTR_MODACC_RESULTS_CHIP_RATE_ERROR | Returns the chip rate error. This value is expressed in ppm. |
| RFMXTDSCDMA_ATTR_MODACC_RESULTS_COMPOSITE_RHO | Returns the composite value of rho, averaged over all active time slots and all averaging iterations. |
| RFMXTDSCDMA_ATTR_MODACC_RESULTS_FREQUENCY_ERROR | Returns the frequency error averaged over all measured slots. This value is expressed in Hz. |
| RFMXTDSCDMA_ATTR_MODACC_RESULTS_IQ_GAIN_IMBALANCE | Returns the I/Q gain imbalance of the composite signal, averaged over all measured slots. This value is expressed in dB. |
| RFMXTDSCDMA_ATTR_MODACC_RESULTS_IQ_ORIGIN_OFFSET | Returns the I/Q origin offset of the composite signal, averaged over all measured slots. This value is expressed in dB. |
| RFMXTDSCDMA_ATTR_MODACC_RESULTS_IQ_QUADRATURE_ERROR | Returns the I/Q quadrature error of the composite signal, averaged over all measured slots. This value is expressed in degrees. |
| RFMXTDSCDMA_ATTR_MODACC_RESULTS_MAXIMUM_COMPOSITE_RHO | Returns the maximum value of the composite rho among all active time slots and averaging iterations. |
| RFMXTDSCDMA_ATTR_MODACC_RESULTS_PEAK_COMPOSITE_EVM | Returns the peak composite EVM among all active time slots and averaging iterations. This value is expressed as a percentage. |
| RFMXTDSCDMA_ATTR_MODACC_RESULTS_RMS_COMPOSITE_EVM | Returns the value of the time-slot based RMS of the composite EVM, averaged over all active time slots and all averaging iterations. This value is expressed as a percentage. |
| RFMXTDSCDMA_ATTR_MODACC_RESULTS_RMS_COMPOSITE_MAGNITUDE_ERROR | Returns the RMS of the composite magnitude error averaged over all active time slots and averaging iterations. This value is expressed as a percentage. |
| RFMXTDSCDMA_ATTR_MODACC_RESULTS_RMS_COMPOSITE_PHASE_ERROR | Returns the RMS of the composite phase error, averaged over all active time slots and averaging iterations. This value is expressed in degrees. |

#### Attachments

None

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc__results_1ga03b0baac40ff925af0e6f2b1b161e5c5.html language=enus -->
## TOPIC 00080: RFMXTDSCDMA_ATTR_MODACC_RESULTS_PEAK_COMPOSITE_EVM

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc__results_1ga03b0baac40ff925af0e6f2b1b161e5c5.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc__results_1ga03b0baac40ff925af0e6f2b1b161e5c5.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the peak composite EVM among all active time slots and averaging iterations. This value is expressed as a percentage. SyntaxRFMXTDSCDMA_ATTR_MODACC_RESULTS_PEAK_COMPOSITE_EVMNumeric ValueData TypeAccessApplies To7409793float64Read-OnlyN/ARemarks You do not need to use a selector string to re

### RFMXTDSCDMA_ATTR_MODACC_RESULTS_PEAK_COMPOSITE_EVM

Returns the peak composite EVM among all active time slots and averaging iterations. This value is expressed as a percentage.

#### Syntax

RFMXTDSCDMA_ATTR_MODACC_RESULTS_PEAK_COMPOSITE_EVM

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 7409793 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this attribute for the default signal and result instances. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc__results_1ga0703ce3ad8bc442a2d72db152118fc17.html language=enus -->
## TOPIC 00081: RFMXTDSCDMA_ATTR_MODACC_RESULTS_IQ_GAIN_IMBALANCE

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc__results_1ga0703ce3ad8bc442a2d72db152118fc17.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc__results_1ga0703ce3ad8bc442a2d72db152118fc17.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the I/Q gain imbalance of the composite signal, averaged over all measured slots. This value is expressed in dB. SyntaxRFMXTDSCDMA_ATTR_MODACC_RESULTS_IQ_GAIN_IMBALANCENumeric ValueData TypeAccessApplies To7409797float64Read-OnlyN/ARemarks You do not need to use a selector string to read thi

### RFMXTDSCDMA_ATTR_MODACC_RESULTS_IQ_GAIN_IMBALANCE

Returns the I/Q gain imbalance of the composite signal, averaged over all measured slots. This value is expressed in dB.

#### Syntax

RFMXTDSCDMA_ATTR_MODACC_RESULTS_IQ_GAIN_IMBALANCE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 7409797 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this attribute for the default signal and result instances. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc__results_1ga380b5f6f9828d0364ff60a0197ad6304.html language=enus -->
## TOPIC 00082: RFMXTDSCDMA_ATTR_MODACC_RESULTS_RMS_COMPOSITE_EVM

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc__results_1ga380b5f6f9828d0364ff60a0197ad6304.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc__results_1ga380b5f6f9828d0364ff60a0197ad6304.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the value of the time-slot based RMS of the composite EVM, averaged over all active time slots and all averaging iterations. This value is expressed as a percentage. SyntaxRFMXTDSCDMA_ATTR_MODACC_RESULTS_RMS_COMPOSITE_EVMNumeric ValueData TypeAccessApplies To7409792float64Read-OnlyN/ARemarks

### RFMXTDSCDMA_ATTR_MODACC_RESULTS_RMS_COMPOSITE_EVM

Returns the value of the time-slot based RMS of the composite EVM, averaged over all active time slots and all averaging iterations. This value is expressed as a percentage.

#### Syntax

RFMXTDSCDMA_ATTR_MODACC_RESULTS_RMS_COMPOSITE_EVM

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 7409792 | float64 | Read-Only | N/A |

#### Remarks

Values close to 0 indicate a good modulation accuracy. In a loopback setup, values of approximately 0.2 to 0.4 are typical.

You do not need to use a selector string to read this attribute for the default signal and result instances. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc__results_1ga3f5498126ba86a89b882fe628309f139.html language=enus -->
## TOPIC 00083: RFMXTDSCDMA_ATTR_MODACC_RESULTS_RMS_COMPOSITE_PHASE_ERROR

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc__results_1ga3f5498126ba86a89b882fe628309f139.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc__results_1ga3f5498126ba86a89b882fe628309f139.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the RMS of the composite phase error, averaged over all active time slots and averaging iterations. This value is expressed in degrees. SyntaxRFMXTDSCDMA_ATTR_MODACC_RESULTS_RMS_COMPOSITE_PHASE_ERRORNumeric ValueData TypeAccessApplies To7409795float64Read-OnlyN/ARemarks You do not need to us

### RFMXTDSCDMA_ATTR_MODACC_RESULTS_RMS_COMPOSITE_PHASE_ERROR

Returns the RMS of the composite phase error, averaged over all active time slots and averaging iterations. This value is expressed in degrees.

#### Syntax

RFMXTDSCDMA_ATTR_MODACC_RESULTS_RMS_COMPOSITE_PHASE_ERROR

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 7409795 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this attribute for the default signal and result instances. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc__results_1ga4d3ef8a49126d8dc1773ab3d10aa4240.html language=enus -->
## TOPIC 00084: RFMXTDSCDMA_ATTR_MODACC_RESULTS_MAXIMUM_COMPOSITE_RHO

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc__results_1ga4d3ef8a49126d8dc1773ab3d10aa4240.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc__results_1ga4d3ef8a49126d8dc1773ab3d10aa4240.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum value of the composite rho among all active time slots and averaging iterations. SyntaxRFMXTDSCDMA_ATTR_MODACC_RESULTS_MAXIMUM_COMPOSITE_RHONumeric ValueData TypeAccessApplies To7409843float64Read-OnlyN/ARemarks You do not need to use a selector string to read this attribute for

### RFMXTDSCDMA_ATTR_MODACC_RESULTS_MAXIMUM_COMPOSITE_RHO

Returns the maximum value of the composite rho among all active time slots and averaging iterations.

#### Syntax

RFMXTDSCDMA_ATTR_MODACC_RESULTS_MAXIMUM_COMPOSITE_RHO

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 7409843 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this attribute for the default signal and result instances. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc__results_1gabe9ba3081eed9a924092bd523c663d01.html language=enus -->
## TOPIC 00085: RFMXTDSCDMA_ATTR_MODACC_RESULTS_CHIP_RATE_ERROR

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc__results_1gabe9ba3081eed9a924092bd523c663d01.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc__results_1gabe9ba3081eed9a924092bd523c663d01.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the chip rate error. This value is expressed in ppm. SyntaxRFMXTDSCDMA_ATTR_MODACC_RESULTS_CHIP_RATE_ERRORNumeric ValueData TypeAccessApplies To7409833float64Read-OnlyN/ARemarks You do not need to use a selector string to read this attribute for the default signal and result instances. Refer

### RFMXTDSCDMA_ATTR_MODACC_RESULTS_CHIP_RATE_ERROR

Returns the chip rate error. This value is expressed in ppm.

#### Syntax

RFMXTDSCDMA_ATTR_MODACC_RESULTS_CHIP_RATE_ERROR

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 7409833 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this attribute for the default signal and result instances. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc__results_1gac17ac8a6cfed03b8cee187061df37a6f.html language=enus -->
## TOPIC 00086: RFMXTDSCDMA_ATTR_MODACC_RESULTS_IQ_ORIGIN_OFFSET

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc__results_1gac17ac8a6cfed03b8cee187061df37a6f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc__results_1gac17ac8a6cfed03b8cee187061df37a6f.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the I/Q origin offset of the composite signal, averaged over all measured slots. This value is expressed in dB. SyntaxRFMXTDSCDMA_ATTR_MODACC_RESULTS_IQ_ORIGIN_OFFSETNumeric ValueData TypeAccessApplies To7409796float64Read-OnlyN/ARemarks You do not need to use a selector string to read this

### RFMXTDSCDMA_ATTR_MODACC_RESULTS_IQ_ORIGIN_OFFSET

Returns the I/Q origin offset of the composite signal, averaged over all measured slots. This value is expressed in dB.

#### Syntax

RFMXTDSCDMA_ATTR_MODACC_RESULTS_IQ_ORIGIN_OFFSET

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 7409796 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this attribute for the default signal and result instances. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc__results_1gad8e275c3e4eac810a3e1581443596f0e.html language=enus -->
## TOPIC 00087: RFMXTDSCDMA_ATTR_MODACC_RESULTS_IQ_QUADRATURE_ERROR

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc__results_1gad8e275c3e4eac810a3e1581443596f0e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc__results_1gad8e275c3e4eac810a3e1581443596f0e.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the I/Q quadrature error of the composite signal, averaged over all measured slots. This value is expressed in degrees. SyntaxRFMXTDSCDMA_ATTR_MODACC_RESULTS_IQ_QUADRATURE_ERRORNumeric ValueData TypeAccessApplies To7409798float64Read-OnlyN/ARemarks You do not need to use a selector string to

### RFMXTDSCDMA_ATTR_MODACC_RESULTS_IQ_QUADRATURE_ERROR

Returns the I/Q quadrature error of the composite signal, averaged over all measured slots. This value is expressed in degrees.

#### Syntax

RFMXTDSCDMA_ATTR_MODACC_RESULTS_IQ_QUADRATURE_ERROR

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 7409798 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this attribute for the default signal and result instances. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc__results__data_1ga2ba8145f9651d679286fd4de51a25621.html language=enus -->
## TOPIC 00088: RFMXTDSCDMA_ATTR_MODACC_RESULTS_MAXIMUM_PEAK_DATA_CDE

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc__results__data_1ga2ba8145f9651d679286fd4de51a25621.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc__results__data_1ga2ba8145f9651d679286fd4de51a25621.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum peak code domain error (CDE) among all active time slots and averaging iterations. This value is expressed in dB. SyntaxRFMXTDSCDMA_ATTR_MODACC_RESULTS_MAXIMUM_PEAK_DATA_CDENumeric ValueData TypeAccessApplies To7409855float64Read-OnlyN/ARemarks You do not need to use a selector s

### RFMXTDSCDMA_ATTR_MODACC_RESULTS_MAXIMUM_PEAK_DATA_CDE

Returns the maximum peak code domain error (CDE) among all active time slots and averaging iterations. This value is expressed in dB.

#### Syntax

RFMXTDSCDMA_ATTR_MODACC_RESULTS_MAXIMUM_PEAK_DATA_CDE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 7409855 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this attribute for the default signal and result instances. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

Parent topic:

Data

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc__results__data_1ga4680453a9af75a6d3fb4b5ef2931d3f7.html language=enus -->
## TOPIC 00089: RFMXTDSCDMA_ATTR_MODACC_RESULTS_PEAK_DATA_ACTIVE_CDE_SPREADING_FACTOR

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc__results__data_1ga4680453a9af75a6d3fb4b5ef2931d3f7.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc__results__data_1ga4680453a9af75a6d3fb4b5ef2931d3f7.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the spreading factor used to retrieve the peak code domain error (CDE) of the active physical channel corresponding to the measured value of the RFMXTDSCDMA_ATTR_MODACC_RESULTS_MAXIMUM_PEAK_DATA_ACTIVE_CDE attribute. SyntaxRFMXTDSCDMA_ATTR_MODACC_RESULTS_PEAK_DATA_ACTIVE_CDE_SPREADING_FACTOR

### RFMXTDSCDMA_ATTR_MODACC_RESULTS_PEAK_DATA_ACTIVE_CDE_SPREADING_FACTOR

Returns the spreading factor used to retrieve the peak code domain error (CDE) of the active physical channel corresponding to the measured value of the [RFMXTDSCDMA_ATTR_MODACC_RESULTS_MAXIMUM_PEAK_DATA_ACTIVE_CDE](group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc__results__data_1gaed9132e623875591dae69a916f9856e5.html) attribute.

#### Syntax

RFMXTDSCDMA_ATTR_MODACC_RESULTS_PEAK_DATA_ACTIVE_CDE_SPREADING_FACTOR

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 7409819 | int32 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this attribute for the default signal and result instances. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

Parent topic:

Data

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc__results__data_1ga69351ee85bad30f5cafc4f0b21642d43.html language=enus -->
## TOPIC 00090: RFMXTDSCDMA_ATTR_MODACC_RESULTS_PEAK_DATA_EVM

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc__results__data_1ga69351ee85bad30f5cafc4f0b21642d43.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc__results__data_1ga69351ee85bad30f5cafc4f0b21642d43.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the peak data EVM among all active time slots and averaging iterations. This value is expressed as a percentage. SyntaxRFMXTDSCDMA_ATTR_MODACC_RESULTS_PEAK_DATA_EVMNumeric ValueData TypeAccessApplies To7409811float64Read-OnlyN/ARemarks You do not need to use a selector string to read this at

### RFMXTDSCDMA_ATTR_MODACC_RESULTS_PEAK_DATA_EVM

Returns the peak data EVM among all active time slots and averaging iterations. This value is expressed as a percentage.

#### Syntax

RFMXTDSCDMA_ATTR_MODACC_RESULTS_PEAK_DATA_EVM

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 7409811 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this attribute for the default signal and result instances. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

Parent topic:

Data

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc__results__data_1ga7121cc833028f96db640f454b3a93436.html language=enus -->
## TOPIC 00091: RFMXTDSCDMA_ATTR_MODACC_RESULTS_MAXIMUM_PEAK_DATA_RCDE

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc__results__data_1ga7121cc833028f96db640f454b3a93436.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc__results__data_1ga7121cc833028f96db640f454b3a93436.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum value of the peak relative code domain error (RDCE) among all active time slots and averaging iterations. This value is expressed in dB. SyntaxRFMXTDSCDMA_ATTR_MODACC_RESULTS_MAXIMUM_PEAK_DATA_RCDENumeric ValueData TypeAccessApplies To7409857float64Read-OnlyN/ARemarks You do not

### RFMXTDSCDMA_ATTR_MODACC_RESULTS_MAXIMUM_PEAK_DATA_RCDE

Returns the maximum value of the peak relative code domain error (RDCE) among all active time slots and averaging iterations. This value is expressed in dB.

#### Syntax

RFMXTDSCDMA_ATTR_MODACC_RESULTS_MAXIMUM_PEAK_DATA_RCDE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 7409857 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this attribute for the default signal and result instances. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

Parent topic:

Data

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc__results__data_1gaed03617a680992677f054f21cb4af719.html language=enus -->
## TOPIC 00092: RFMXTDSCDMA_ATTR_MODACC_RESULTS_PEAK_DATA_CDE_SPREADING_FACTOR

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc__results__data_1gaed03617a680992677f054f21cb4af719.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc__results__data_1gaed03617a680992677f054f21cb4af719.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the spreading factor used to retrieve the peak code domain error (CDE) of the channel corresponding to measured value of the RFMXTDSCDMA_ATTR_MODACC_RESULTS_MAXIMUM_PEAK_DATA_CDE attribute. SyntaxRFMXTDSCDMA_ATTR_MODACC_RESULTS_PEAK_DATA_CDE_SPREADING_FACTORNumeric ValueData TypeAccessApplie

### RFMXTDSCDMA_ATTR_MODACC_RESULTS_PEAK_DATA_CDE_SPREADING_FACTOR

Returns the spreading factor used to retrieve the peak code domain error (CDE) of the channel corresponding to measured value of the [RFMXTDSCDMA_ATTR_MODACC_RESULTS_MAXIMUM_PEAK_DATA_CDE](group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc__results__data_1ga2ba8145f9651d679286fd4de51a25621.html) attribute.

#### Syntax

RFMXTDSCDMA_ATTR_MODACC_RESULTS_PEAK_DATA_CDE_SPREADING_FACTOR

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 7409816 | int32 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this attribute for the default signal and result instances. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

Parent topic:

Data

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc__results__detected__channel_1ga8d54c95843414954fea56ea4c73ee99a.html language=enus -->
## TOPIC 00093: RFMXTDSCDMA_ATTR_MODACC_RESULTS_DETECTED_CHANNELIZATION_CODE

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc__results__detected__channel_1ga8d54c95843414954fea56ea4c73ee99a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc__results__detected__channel_1ga8d54c95843414954fea56ea4c73ee99a.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the channelization code of the selected channel within the set of active channels. If the averaging is enabled, this attribute refers to the last averaging iteration. SyntaxRFMXTDSCDMA_ATTR_MODACC_RESULTS_DETECTED_CHANNELIZATION_CODENumeric ValueData TypeAccessApplies To7409831int32Read-Only

### RFMXTDSCDMA_ATTR_MODACC_RESULTS_DETECTED_CHANNELIZATION_CODE

Returns the channelization code of the selected channel within the set of active channels. If the averaging is enabled, this attribute refers to the last averaging iteration.

#### Syntax

RFMXTDSCDMA_ATTR_MODACC_RESULTS_DETECTED_CHANNELIZATION_CODE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 7409831 | int32 | Read-Only | Channel |

#### Remarks

Use "channel<i><n></i>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result.

Parent topic:

Detected Channel

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc__results__detected__channel_1ga92a7404493d30a4e8e2577ff9dfad592.html language=enus -->
## TOPIC 00094: RFMXTDSCDMA_ATTR_MODACC_RESULTS_NUMBER_OF_DETECTED_CHANNELS

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc__results__detected__channel_1ga92a7404493d30a4e8e2577ff9dfad592.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc__results__detected__channel_1ga92a7404493d30a4e8e2577ff9dfad592.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the number of detected active channels. If the averaging is enabled, this attribute returns the number of detected channels of the last averaging iteration. SyntaxRFMXTDSCDMA_ATTR_MODACC_RESULTS_NUMBER_OF_DETECTED_CHANNELSNumeric ValueData TypeAccessApplies To7409827int32Read-OnlyN/ARemarks

### RFMXTDSCDMA_ATTR_MODACC_RESULTS_NUMBER_OF_DETECTED_CHANNELS

Returns the number of detected active channels. If the averaging is enabled, this attribute returns the number of detected channels of the last averaging iteration.

#### Syntax

RFMXTDSCDMA_ATTR_MODACC_RESULTS_NUMBER_OF_DETECTED_CHANNELS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 7409827 | int32 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for the default signal and result instances. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

Parent topic:

Detected Channel

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc__results__detected__channel_1gac94b1500cda66325fc9225ba32eea686.html language=enus -->
## TOPIC 00095: RFMXTDSCDMA_ATTR_MODACC_RESULTS_DETECTED_SPREADING_FACTOR

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc__results__detected__channel_1gac94b1500cda66325fc9225ba32eea686.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc__results__detected__channel_1gac94b1500cda66325fc9225ba32eea686.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the spreading factor of the selected channel within the set of active channels. If the averaging is enabled, this attribute refers to the last averaging iteration. SyntaxRFMXTDSCDMA_ATTR_MODACC_RESULTS_DETECTED_SPREADING_FACTORNumeric ValueData TypeAccessApplies To7409829int32Read-OnlyChanne

### RFMXTDSCDMA_ATTR_MODACC_RESULTS_DETECTED_SPREADING_FACTOR

Returns the spreading factor of the selected channel within the set of active channels. If the averaging is enabled, this attribute refers to the last averaging iteration.

#### Syntax

RFMXTDSCDMA_ATTR_MODACC_RESULTS_DETECTED_SPREADING_FACTOR

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 7409829 | int32 | Read-Only | Channel |

#### Remarks

Use "channel<i><n></i>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result.

Parent topic:

Detected Channel

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc__results__midamble.html language=enus -->
## TOPIC 00096: Midamble

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc__results__midamble.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc__results__midamble.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXTDSCDMA_ATTR_MODACC_RESULTS_MIDAMBLE_CODEReturns the midamble code. RFMXTDSCDMA_ATTR_MODACC_RESULTS_MIDAMBLE_POWERReturns the midamble power, averaged over all measured slots. This value is expressed in dBm. RFMXTDSCDMA_ATTR_MODACC_RESULTS_MIDAMBLE_RHOReturn

### Midamble

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXTDSCDMA_ATTR_MODACC_RESULTS_MIDAMBLE_CODE | Returns the midamble code. |
| RFMXTDSCDMA_ATTR_MODACC_RESULTS_MIDAMBLE_POWER | Returns the midamble power, averaged over all measured slots. This value is expressed in dBm. |
| RFMXTDSCDMA_ATTR_MODACC_RESULTS_MIDAMBLE_RHO | Returns the rho value of the midamble, averaged over all measured active time slots and averaging iterations. |
| RFMXTDSCDMA_ATTR_MODACC_RESULTS_MIDAMBLE_SHIFT | Returns the midamble code shift. This value is expressed in chips. |
| RFMXTDSCDMA_ATTR_MODACC_RESULTS_PEAK_MIDAMBLE_EVM | >Returns the peak midamble EVM among all active time slots and averaging iterations. This value is expressed as a percentage. |
| RFMXTDSCDMA_ATTR_MODACC_RESULTS_RMS_MIDAMBLE_EVM | Returns the RMS of the midamble EVM, averaged over all active time slots and all averaging iterations. This value is expressed as a percentage. |
| RFMXTDSCDMA_ATTR_MODACC_RESULTS_RMS_MIDAMBLE_MAGNITUDE_ERROR | Returns the RMS of the midamble magnitude error, averaged over all active time slots and averaging iterations. This value is expressed as a percentage. |
| RFMXTDSCDMA_ATTR_MODACC_RESULTS_RMS_MIDAMBLE_PHASE_ERROR | Returns the RMS of the midamble phase error, averaged over all active time slots and all averaging iterations. This value is expressed in degrees. |

#### Attachments

None

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc__results__midamble_1ga1b632ffa504024c55d1965ffc864234e.html language=enus -->
## TOPIC 00097: RFMXTDSCDMA_ATTR_MODACC_RESULTS_MIDAMBLE_SHIFT

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc__results__midamble_1ga1b632ffa504024c55d1965ffc864234e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc__results__midamble_1ga1b632ffa504024c55d1965ffc864234e.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the midamble code shift. This value is expressed in chips. SyntaxRFMXTDSCDMA_ATTR_MODACC_RESULTS_MIDAMBLE_SHIFTNumeric ValueData TypeAccessApplies To7409809int32Read-OnlyN/ARemarks You do not need to use a selector string to read this attribute for the default signal and result instances. Re

### RFMXTDSCDMA_ATTR_MODACC_RESULTS_MIDAMBLE_SHIFT

Returns the midamble code shift. This value is expressed in chips.

#### Syntax

RFMXTDSCDMA_ATTR_MODACC_RESULTS_MIDAMBLE_SHIFT

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 7409809 | int32 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this attribute for the default signal and result instances. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

Parent topic:

Midamble

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc__results__midamble_1ga2e76a3284a9409eceeb2a09e1b489cd3.html language=enus -->
## TOPIC 00098: RFMXTDSCDMA_ATTR_MODACC_RESULTS_MIDAMBLE_POWER

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc__results__midamble_1ga2e76a3284a9409eceeb2a09e1b489cd3.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc__results__midamble_1ga2e76a3284a9409eceeb2a09e1b489cd3.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the midamble power, averaged over all measured slots. This value is expressed in dBm. SyntaxRFMXTDSCDMA_ATTR_MODACC_RESULTS_MIDAMBLE_POWERNumeric ValueData TypeAccessApplies To7409807float64Read-OnlyN/ARemarks You do not need to use a selector string to read this attribute for the default si

### RFMXTDSCDMA_ATTR_MODACC_RESULTS_MIDAMBLE_POWER

Returns the midamble power, averaged over all measured slots. This value is expressed in dBm.

#### Syntax

RFMXTDSCDMA_ATTR_MODACC_RESULTS_MIDAMBLE_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 7409807 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this attribute for the default signal and result instances. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

Parent topic:

Midamble

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc__results__midamble_1ga39ed1e6329833a76b1c91d7b55516149.html language=enus -->
## TOPIC 00099: RFMXTDSCDMA_ATTR_MODACC_RESULTS_PEAK_MIDAMBLE_EVM

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc__results__midamble_1ga39ed1e6329833a76b1c91d7b55516149.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc__results__midamble_1ga39ed1e6329833a76b1c91d7b55516149.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: >Returns the peak midamble EVM among all active time slots and averaging iterations. This value is expressed as a percentage. SyntaxRFMXTDSCDMA_ATTR_MODACC_RESULTS_PEAK_MIDAMBLE_EVMNumeric ValueData TypeAccessApplies To7409803float64Read-OnlyN/ARemarks You do not need to use a selector string to

### RFMXTDSCDMA_ATTR_MODACC_RESULTS_PEAK_MIDAMBLE_EVM

&gt;Returns the peak midamble EVM among all active time slots and averaging iterations. This value is expressed as a percentage.

#### Syntax

RFMXTDSCDMA_ATTR_MODACC_RESULTS_PEAK_MIDAMBLE_EVM

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 7409803 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this attribute for the default signal and result instances. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

Parent topic:

Midamble

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc__results__midamble_1gaa5e12456d9f303612b8e62a7ddea0354.html language=enus -->
## TOPIC 00100: RFMXTDSCDMA_ATTR_MODACC_RESULTS_MIDAMBLE_RHO

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc__results__midamble_1gaa5e12456d9f303612b8e62a7ddea0354.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc__results__midamble_1gaa5e12456d9f303612b8e62a7ddea0354.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the rho value of the midamble, averaged over all measured active time slots and averaging iterations. SyntaxRFMXTDSCDMA_ATTR_MODACC_RESULTS_MIDAMBLE_RHONumeric ValueData TypeAccessApplies To7409806float64Read-OnlyN/ARemarks You do not need to use a selector string to read this attribute for

### RFMXTDSCDMA_ATTR_MODACC_RESULTS_MIDAMBLE_RHO

Returns the rho value of the midamble, averaged over all measured active time slots and averaging iterations.

#### Syntax

RFMXTDSCDMA_ATTR_MODACC_RESULTS_MIDAMBLE_RHO

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 7409806 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this attribute for the default signal and result instances. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

Parent topic:

Midamble

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc__results__midamble_1gaecfe33d6580c0fadf59ef3ba013cebd1.html language=enus -->
## TOPIC 00101: RFMXTDSCDMA_ATTR_MODACC_RESULTS_RMS_MIDAMBLE_EVM

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc__results__midamble_1gaecfe33d6580c0fadf59ef3ba013cebd1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc__results__midamble_1gaecfe33d6580c0fadf59ef3ba013cebd1.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the RMS of the midamble EVM, averaged over all active time slots and all averaging iterations. This value is expressed as a percentage. SyntaxRFMXTDSCDMA_ATTR_MODACC_RESULTS_RMS_MIDAMBLE_EVMNumeric ValueData TypeAccessApplies To7409802float64Read-OnlyN/ARemarks You do not need to use a selec

### RFMXTDSCDMA_ATTR_MODACC_RESULTS_RMS_MIDAMBLE_EVM

Returns the RMS of the midamble EVM, averaged over all active time slots and all averaging iterations. This value is expressed as a percentage.

#### Syntax

RFMXTDSCDMA_ATTR_MODACC_RESULTS_RMS_MIDAMBLE_EVM

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 7409802 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this attribute for the default signal and result instances. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

Parent topic:

Midamble

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc__results__pilot_1gaa85999a5de1e63e17eabf7f9fc521139.html language=enus -->
## TOPIC 00102: RFMXTDSCDMA_ATTR_MODACC_RESULTS_PEAK_PILOT_EVM

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc__results__pilot_1gaa85999a5de1e63e17eabf7f9fc521139.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc__results__pilot_1gaa85999a5de1e63e17eabf7f9fc521139.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum of the peak pilot EVM among the averaging iterations. This value is expressed as a percentage. SyntaxRFMXTDSCDMA_ATTR_MODACC_RESULTS_PEAK_PILOT_EVMNumeric ValueData TypeAccessApplies To7409839float64Read-OnlyN/ARemarks You do not need to use a selector string to read this result

### RFMXTDSCDMA_ATTR_MODACC_RESULTS_PEAK_PILOT_EVM

Returns the maximum of the peak pilot EVM among the averaging iterations. This value is expressed as a percentage.

#### Syntax

RFMXTDSCDMA_ATTR_MODACC_RESULTS_PEAK_PILOT_EVM

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 7409839 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for the default signal and result instances. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

Parent topic:

Pilot

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc__results__pilot_1gaeba1d595d1443d28e91880c2a299d7df.html language=enus -->
## TOPIC 00103: RFMXTDSCDMA_ATTR_MODACC_RESULTS_RMS_PILOT_MAGNITUDE_ERROR

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc__results__pilot_1gaeba1d595d1443d28e91880c2a299d7df.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__modacc__results__pilot_1gaeba1d595d1443d28e91880c2a299d7df.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the RMS of the pilot magnitude error, averaged over all the averaging iterations. This value is expressed as a percentage. SyntaxRFMXTDSCDMA_ATTR_MODACC_RESULTS_RMS_PILOT_MAGNITUDE_ERRORNumeric ValueData TypeAccessApplies To7409840float64Read-OnlyN/ARemarks You do not need to use a selector

### RFMXTDSCDMA_ATTR_MODACC_RESULTS_RMS_PILOT_MAGNITUDE_ERROR

Returns the RMS of the pilot magnitude error, averaged over all the averaging iterations. This value is expressed as a percentage.

#### Syntax

RFMXTDSCDMA_ATTR_MODACC_RESULTS_RMS_PILOT_MAGNITUDE_ERROR

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 7409840 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for the default signal and result instances. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

Parent topic:

Pilot

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__obw.html language=enus -->
## TOPIC 00104: OBW

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__obw.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__obw.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsAveragingRBW FilterResultsSweep TimeGroup membersNameDescriptionRFMXTDSCDMA_ATTR_OBW_ALL_TRACES_ENABLEDSpecifies whether to enable storage and retrieval of the traces after performing the OBW measurement. RFMXTDSCDMA_ATTR_OBW_MEASUREMENT_ENABLEDSpecifies whether to enable the OBW measurement.

### OBW

#### Groups

- Averaging
- RBW Filter
- Results
- Sweep Time

#### Group members

| Name | Description |
| --- | --- |
| RFMXTDSCDMA_ATTR_OBW_ALL_TRACES_ENABLED | Specifies whether to enable storage and retrieval of the traces after performing the OBW measurement. |
| RFMXTDSCDMA_ATTR_OBW_MEASUREMENT_ENABLED | Specifies whether to enable the OBW measurement. |
| RFMXTDSCDMA_ATTR_OBW_NUMBER_OF_ANALYSIS_THREADS | Specifies the maximum number of threads used for parallelism for the OBW measurement. |
| RFMXTDSCDMA_ATTR_OBW_SPAN | Returns the frequency span of the OBW measurement. This value is expressed in Hz. |

#### Attachments

None

Parent topic:

Attributes

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__obw_1ga8bb86366938ada20af91ff0b7629d709.html language=enus -->
## TOPIC 00105: RFMXTDSCDMA_ATTR_OBW_SPAN

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__obw_1ga8bb86366938ada20af91ff0b7629d709.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__obw_1ga8bb86366938ada20af91ff0b7629d709.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the frequency span of the OBW measurement. This value is expressed in Hz. SyntaxRFMXTDSCDMA_ATTR_OBW_SPANNumeric ValueData TypeAccessApplies To7364612float64Read-OnlyN/ARemarks You do not need to use a selector string to read this attribute for the default signal result instance. Refer to th

### RFMXTDSCDMA_ATTR_OBW_SPAN

Returns the frequency span of the OBW measurement. This value is expressed in Hz.

#### Syntax

RFMXTDSCDMA_ATTR_OBW_SPAN

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 7364612 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this attribute for the default signal result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

Parent topic:

OBW

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__obw__results.html language=enus -->
## TOPIC 00106: Results

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__obw__results.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__obw__results.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXTDSCDMA_ATTR_OBW_RESULTS_ABSOLUTE_POWERReturns the absolute power measured in the OBW. This value is expressed in dBm. RFMXTDSCDMA_ATTR_OBW_RESULTS_OCCUPIED_BANDWIDTHReturns the bandwidth that occupies 99% of the total signal power. This value is expressed i

### Results

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXTDSCDMA_ATTR_OBW_RESULTS_ABSOLUTE_POWER | Returns the absolute power measured in the OBW. This value is expressed in dBm. |
| RFMXTDSCDMA_ATTR_OBW_RESULTS_OCCUPIED_BANDWIDTH | Returns the bandwidth that occupies 99% of the total signal power. This value is expressed in Hz. |
| RFMXTDSCDMA_ATTR_OBW_RESULTS_START_FREQUENCY | Returns the start frequency of the OBW. This value is expressed in Hz. |
| RFMXTDSCDMA_ATTR_OBW_RESULTS_STOP_FREQUENCY | Returns the stop frequency of the OBW. This value is expressed in Hz. |

#### Attachments

None

Parent topic:

OBW

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__obw__sweep__time_1ga835228f0c8f3bff422bedafa3fed1f0e.html language=enus -->
## TOPIC 00107: RFMXTDSCDMA_ATTR_OBW_SWEEP_TIME_AUTO

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__obw__sweep__time_1ga835228f0c8f3bff422bedafa3fed1f0e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__obw__sweep__time_1ga835228f0c8f3bff422bedafa3fed1f0e.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement calculates the sweep time. SyntaxRFMXTDSCDMA_ATTR_OBW_SWEEP_TIME_AUTONumeric ValueData TypeAccessApplies To7364623int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Sel

### RFMXTDSCDMA_ATTR_OBW_SWEEP_TIME_AUTO

Specifies whether the measurement calculates the sweep time.

#### Syntax

RFMXTDSCDMA_ATTR_OBW_SWEEP_TIME_AUTO

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 7364623 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **True**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXTDSCDMA_VAL_OBW_SWEEP_TIME_AUTO_FALSE | 0 (0x0) | The measurement uses the sweep time that you specify in the RFMXTDSCDMA_ATTR_OBW_SWEEP_TIME_INTERVAL attribute. |
| RFMXTDSCDMA_VAL_OBW_SWEEP_TIME_AUTO_TRUE | 1 (0x1) | The measurement uses the default sweep time of .00066 seconds (s). |

Parent topic:

Sweep Time

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__pvt.html language=enus -->
## TOPIC 00108: PVT

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__pvt.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__pvt.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsAveragingResultsSegmentGroup membersNameDescriptionRFMXTDSCDMA_ATTR_PVT_ALL_TRACES_ENABLEDSpecifies whether to enable the traces to be stored and retrieved after performing the power versus time (PVT) measurement. RFMXTDSCDMA_ATTR_PVT_MEASUREMENT_ENABLEDSpecifies whether to enable the power ve

### PVT

#### Groups

- Averaging
- Results
- Segment

#### Group members

| Name | Description |
| --- | --- |
| RFMXTDSCDMA_ATTR_PVT_ALL_TRACES_ENABLED | Specifies whether to enable the traces to be stored and retrieved after performing the power versus time (PVT) measurement. |
| RFMXTDSCDMA_ATTR_PVT_MEASUREMENT_ENABLED | Specifies whether to enable the power versus time (PVT) measurement (Transmit ON/off time mask) according to the 3GPP TS 34.122 specification. |
| RFMXTDSCDMA_ATTR_PVT_MEASUREMENT_METHOD | Specifies the method for performing the power versus time (PVT) measurement. |
| RFMXTDSCDMA_ATTR_PVT_NUMBER_OF_ANALYSIS_THREADS | Specifies the maximum number of threads used for parallelism for the power versus time (PVT) measurement. |
| RFMXTDSCDMA_ATTR_PVT_NUMBER_OF_SEGMENTS | Returns the number of segments defined for the power versus time (PVT) measurement. |
| RFMXTDSCDMA_ATTR_PVT_RRC_FILTER_ENABLED | Specifies whether to enable the RRC filter. Use this attribute to disable the filter if the received signal is already RRC-filtered. |

#### Attachments

None

Parent topic:

Attributes

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__pvt_1gab6f6d601a4123953b86c1e4b8d45359e.html language=enus -->
## TOPIC 00109: RFMXTDSCDMA_ATTR_PVT_NUMBER_OF_ANALYSIS_THREADS

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__pvt_1gab6f6d601a4123953b86c1e4b8d45359e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__pvt_1gab6f6d601a4123953b86c1e4b8d45359e.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the maximum number of threads used for parallelism for the power versus time (PVT) measurement. SyntaxRFMXTDSCDMA_ATTR_PVT_NUMBER_OF_ANALYSIS_THREADSNumeric ValueData TypeAccessApplies To7368714int32Read/WriteN/ARemarks The number of threads can range from 1 to the number of physical cores

### RFMXTDSCDMA_ATTR_PVT_NUMBER_OF_ANALYSIS_THREADS

Specifies the maximum number of threads used for parallelism for the power versus time (PVT) measurement.

#### Syntax

RFMXTDSCDMA_ATTR_PVT_NUMBER_OF_ANALYSIS_THREADS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 7368714 | int32 | Read/Write | N/A |

#### Remarks

The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations.

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 1.

Parent topic:

PVT

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__pvt_1gaec3253564fc6fdd048ad22264580b019.html language=enus -->
## TOPIC 00110: RFMXTDSCDMA_ATTR_PVT_NUMBER_OF_SEGMENTS

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__pvt_1gaec3253564fc6fdd048ad22264580b019.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__pvt_1gaec3253564fc6fdd048ad22264580b019.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the number of segments defined for the power versus time (PVT) measurement. SyntaxRFMXTDSCDMA_ATTR_PVT_NUMBER_OF_SEGMENTSNumeric ValueData TypeAccessApplies To7368716int32Read-OnlyN/ARemarks You do not need to use a selector string to read this attribute for the default signal instance. Refe

### RFMXTDSCDMA_ATTR_PVT_NUMBER_OF_SEGMENTS

Returns the number of segments defined for the power versus time (PVT) measurement.

#### Syntax

RFMXTDSCDMA_ATTR_PVT_NUMBER_OF_SEGMENTS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 7368716 | int32 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 6.

Parent topic:

PVT

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__pvt_1gafe47c5fa90b3b938fbd054071cdbe84f.html language=enus -->
## TOPIC 00111: RFMXTDSCDMA_ATTR_PVT_MEASUREMENT_METHOD

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__pvt_1gafe47c5fa90b3b938fbd054071cdbe84f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__pvt_1gafe47c5fa90b3b938fbd054071cdbe84f.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the method for performing the power versus time (PVT) measurement. SyntaxRFMXTDSCDMA_ATTR_PVT_MEASUREMENT_METHODNumeric ValueData TypeAccessApplies To7368706int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instanc

### RFMXTDSCDMA_ATTR_PVT_MEASUREMENT_METHOD

Specifies the method for performing the power versus time (PVT) measurement.

#### Syntax

RFMXTDSCDMA_ATTR_PVT_MEASUREMENT_METHOD

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 7368706 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **Normal**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXTDSCDMA_VAL_PVT_MEASUREMENT_METHOD_NORMAL | 0 (0x0) | The PVT measurement acquires the spectrum using the same signal analyzer setting across frequency bands. Use this method when a higher measurement speed is preferred over a higher dynamic range. |
| RFMXTDSCDMA_VAL_PVT_MEASUREMENT_METHOD_DYNAMIC_RANGE | 1 (0x1) | The PVT measurement acquires the spectrum using the hardware-specific optimizations for different frequency bands. Use this method to get the best dynamic range.Supported Devices: PXIe-5644R/5645R/5646R/5840/5841/5842/5860 |

Parent topic:

PVT

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__pvt__results_1ga18248e06b08f87de1b2c629521639ce7.html language=enus -->
## TOPIC 00112: RFMXTDSCDMA_ATTR_PVT_RESULTS_MINIMUM_ABSOLUTE_POWER

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__pvt__results_1ga18248e06b08f87de1b2c629521639ce7.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__pvt__results_1ga18248e06b08f87de1b2c629521639ce7.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the minimum observed power of the measured burst, or the averaged bursts. This value is expressed in dBm. SyntaxRFMXTDSCDMA_ATTR_PVT_RESULTS_MINIMUM_ABSOLUTE_POWERNumeric ValueData TypeAccessApplies To7368723float64Read-OnlyN/ARemarks You do not need to use a selector string to read this res

### RFMXTDSCDMA_ATTR_PVT_RESULTS_MINIMUM_ABSOLUTE_POWER

Returns the minimum observed power of the measured burst, or the averaged bursts. This value is expressed in dBm.

#### Syntax

RFMXTDSCDMA_ATTR_PVT_RESULTS_MINIMUM_ABSOLUTE_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 7368723 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for the default signal and result instances. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__pvt__results_1ga1cc82b03c8cd9505e568db10dbfe9fee.html language=enus -->
## TOPIC 00113: RFMXTDSCDMA_ATTR_PVT_RESULTS_MEAN_ABSOLUTE_ON_POWER

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__pvt__results_1ga1cc82b03c8cd9505e568db10dbfe9fee.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__pvt__results_1ga1cc82b03c8cd9505e568db10dbfe9fee.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean ON power of the measured burst, or the averaged bursts. This value is expressed in dBm. SyntaxRFMXTDSCDMA_ATTR_PVT_RESULTS_MEAN_ABSOLUTE_ON_POWERNumeric ValueData TypeAccessApplies To7368720float64Read-OnlyN/ARemarks You do not need to use a selector string to read this result for t

### RFMXTDSCDMA_ATTR_PVT_RESULTS_MEAN_ABSOLUTE_ON_POWER

Returns the mean ON power of the measured burst, or the averaged bursts. This value is expressed in dBm.

#### Syntax

RFMXTDSCDMA_ATTR_PVT_RESULTS_MEAN_ABSOLUTE_ON_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 7368720 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for the default signal and result instances. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__pvt__results_1gaa4e6cfd60c9d25cfa64fae087f3f3f04.html language=enus -->
## TOPIC 00114: RFMXTDSCDMA_ATTR_PVT_RESULTS_MEASUREMENT_STATUS

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__pvt__results_1gaa4e6cfd60c9d25cfa64fae087f3f3f04.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__pvt__results_1gaa4e6cfd60c9d25cfa64fae087f3f3f04.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the overall status of the power versus time (PVT) measurement. SyntaxRFMXTDSCDMA_ATTR_PVT_RESULTS_MEASUREMENT_STATUSNumeric ValueData TypeAccessApplies To7368719int32Read-OnlyN/ARemarks You do not need to use a selector string to read this result for the default signal and result instances.

### RFMXTDSCDMA_ATTR_PVT_RESULTS_MEASUREMENT_STATUS

Returns the overall status of the power versus time (PVT) measurement.

#### Syntax

RFMXTDSCDMA_ATTR_PVT_RESULTS_MEASUREMENT_STATUS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 7368719 | int32 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for the default signal and result instances. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

| Name | Value | Description |
| --- | --- | --- |
| RFMXTDSCDMA_VAL_PVT_MEASUREMENT_STATUS_FAIL | 0 (0x0) | Indicates that the test has failed, and the measured power in at least one measurement segment violates the limit. |
| RFMXTDSCDMA_VAL_PVT_MEASUREMENT_STATUS_PASS | 1 (0x1) | Indicates that the test has passed and the measured power in all defined segments does not violate the limits. |

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__pvt__results_1gadf91e35a0560f23c7f69911470673ce2.html language=enus -->
## TOPIC 00115: RFMXTDSCDMA_ATTR_PVT_RESULTS_MAXIMUM_ABSOLUTE_POWER

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__pvt__results_1gadf91e35a0560f23c7f69911470673ce2.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__pvt__results_1gadf91e35a0560f23c7f69911470673ce2.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum power of the measured burst, or the averaged bursts. This value is expressed in dBm. SyntaxRFMXTDSCDMA_ATTR_PVT_RESULTS_MAXIMUM_ABSOLUTE_POWERNumeric ValueData TypeAccessApplies To7368722float64Read-OnlyN/ARemarks You do not need to use a selector string to read this result for t

### RFMXTDSCDMA_ATTR_PVT_RESULTS_MAXIMUM_ABSOLUTE_POWER

Returns the maximum power of the measured burst, or the averaged bursts. This value is expressed in dBm.

#### Syntax

RFMXTDSCDMA_ATTR_PVT_RESULTS_MAXIMUM_ABSOLUTE_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 7368722 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for the default signal and result instances. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__pvt__results_1gae5033ae4c6a2c436632f6967fada7e08.html language=enus -->
## TOPIC 00116: RFMXTDSCDMA_ATTR_PVT_RESULTS_BURST_WIDTH

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__pvt__results_1gae5033ae4c6a2c436632f6967fada7e08.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__pvt__results_1gae5033ae4c6a2c436632f6967fada7e08.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the time interval between the time positions where the signal amplitude has reached 90 percent of the full amplitude. This value is expressed in seconds. SyntaxRFMXTDSCDMA_ATTR_PVT_RESULTS_BURST_WIDTHNumeric ValueData TypeAccessApplies To7368724float64Read-OnlyN/ARemarks You do not need to u

### RFMXTDSCDMA_ATTR_PVT_RESULTS_BURST_WIDTH

Returns the time interval between the time positions where the signal amplitude has reached 90 percent of the full amplitude. This value is expressed in seconds.

#### Syntax

RFMXTDSCDMA_ATTR_PVT_RESULTS_BURST_WIDTH

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 7368724 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for the default signal and result instances. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__pvt__results__midamble.html language=enus -->
## TOPIC 00117: Midamble

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__pvt__results__midamble.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__pvt__results__midamble.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXTDSCDMA_ATTR_PVT_RESULTS_MIDAMBLE_CODEReturns the midamble code used for slot synchronization. RFMXTDSCDMA_ATTR_PVT_RESULTS_MIDAMBLE_SHIFTReturns the midamble code shift used for slot synchronization. This value is expressed in chips. AttachmentsNone

### Midamble

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXTDSCDMA_ATTR_PVT_RESULTS_MIDAMBLE_CODE | Returns the midamble code used for slot synchronization. |
| RFMXTDSCDMA_ATTR_PVT_RESULTS_MIDAMBLE_SHIFT | Returns the midamble code shift used for slot synchronization. This value is expressed in chips. |

#### Attachments

None

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__pvt__results__midamble_1ga94cde575be9c6b2c6a66de9544403d56.html language=enus -->
## TOPIC 00118: RFMXTDSCDMA_ATTR_PVT_RESULTS_MIDAMBLE_SHIFT

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__pvt__results__midamble_1ga94cde575be9c6b2c6a66de9544403d56.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__pvt__results__midamble_1ga94cde575be9c6b2c6a66de9544403d56.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the midamble code shift used for slot synchronization. This value is expressed in chips. SyntaxRFMXTDSCDMA_ATTR_PVT_RESULTS_MIDAMBLE_SHIFTNumeric ValueData TypeAccessApplies To7368735int32Read-OnlyN/ARemarks You do not need to use a selector string to read this attribute for the default sign

### RFMXTDSCDMA_ATTR_PVT_RESULTS_MIDAMBLE_SHIFT

Returns the midamble code shift used for slot synchronization. This value is expressed in chips.

#### Syntax

RFMXTDSCDMA_ATTR_PVT_RESULTS_MIDAMBLE_SHIFT

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 7368735 | int32 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

Parent topic:

Midamble

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__pvt__results__segment_1ga5604e6bc03b32e7f05263c72754c9105.html language=enus -->
## TOPIC 00119: RFMXTDSCDMA_ATTR_PVT_RESULTS_SEGMENT_MINIMUM_ABSOLUTE_POWER

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__pvt__results__segment_1ga5604e6bc03b32e7f05263c72754c9105.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__pvt__results__segment_1ga5604e6bc03b32e7f05263c72754c9105.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the minimum measured power of an individual power versus time (PVT) measurement segment. This value is expressed in dBm. SyntaxRFMXTDSCDMA_ATTR_PVT_RESULTS_SEGMENT_MINIMUM_ABSOLUTE_POWERNumeric ValueData TypeAccessApplies To7368733float64Read-OnlySegmentRemarks Use "segment<n>" as the Select

### RFMXTDSCDMA_ATTR_PVT_RESULTS_SEGMENT_MINIMUM_ABSOLUTE_POWER

Returns the minimum measured power of an individual power versus time (PVT) measurement segment. This value is expressed in dBm.

#### Syntax

RFMXTDSCDMA_ATTR_PVT_RESULTS_SEGMENT_MINIMUM_ABSOLUTE_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 7368733 | float64 | Read-Only | Segment |

#### Remarks

Use "segment<n>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result.

Parent topic:

Segment

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__pvt__segment_1gab4f0ba67fd384350c5fd71f0d0ce0deb.html language=enus -->
## TOPIC 00120: RFMXTDSCDMA_ATTR_PVT_SEGMENT_STOP

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__pvt__segment_1gab4f0ba67fd384350c5fd71f0d0ce0deb.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__pvt__segment_1gab4f0ba67fd384350c5fd71f0d0ce0deb.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the stop time of a specific power versus time (PVT) measurement segment. This value is expressed in seconds. The start time is defined relative to the burst start. SyntaxRFMXTDSCDMA_ATTR_PVT_SEGMENT_STOPNumeric ValueData TypeAccessApplies To7368718float64Read-OnlySegmentRemarks Use "segment<

### RFMXTDSCDMA_ATTR_PVT_SEGMENT_STOP

Returns the stop time of a specific power versus time (PVT) measurement segment. This value is expressed in seconds. The start time is defined relative to the burst start.

#### Syntax

RFMXTDSCDMA_ATTR_PVT_SEGMENT_STOP

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 7368718 | float64 | Read-Only | Segment |

#### Remarks

Use "segment<n>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this attribute.

Parent topic:

Segment

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__sem_1ga0120b591c23d57a283fc763c3d33bb85.html language=enus -->
## TOPIC 00121: RFMXTDSCDMA_ATTR_SEM_ALL_TRACES_ENABLED

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__sem_1ga0120b591c23d57a283fc763c3d33bb85.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__sem_1ga0120b591c23d57a283fc763c3d33bb85.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the traces to be stored and retrieved after performing the SEM measurement. SyntaxRFMXTDSCDMA_ATTR_SEM_ALL_TRACES_ENABLEDNumeric ValueData TypeAccessApplies To7372839int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for

### RFMXTDSCDMA_ATTR_SEM_ALL_TRACES_ENABLED

Specifies whether to enable the traces to be stored and retrieved after performing the SEM measurement.

#### Syntax

RFMXTDSCDMA_ATTR_SEM_ALL_TRACES_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 7372839 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is FALSE.

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__sem__carrier.html language=enus -->
## TOPIC 00122: Carrier

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__sem__carrier.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__sem__carrier.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXTDSCDMA_ATTR_SEM_CARRIER_INTEGRATION_BANDWIDTHReturns the SEM carrier integration bandwidth. This value is expressed in Hz. AttachmentsNone

### Carrier

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXTDSCDMA_ATTR_SEM_CARRIER_INTEGRATION_BANDWIDTH | Returns the SEM carrier integration bandwidth. This value is expressed in Hz. |

#### Attachments

None

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__sem__offset.html language=enus -->
## TOPIC 00123: Offset

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__sem__offset.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__sem__offset.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsRBW FilterGroup membersNameDescriptionRFMXTDSCDMA_ATTR_SEM_NUMBER_OF_OFFSETSReturns the number of SEM offset segments. RFMXTDSCDMA_ATTR_SEM_OFFSET_BANDWIDTH_INTEGRALReturns the bandwidth integral for a specific offset segment. A bandwidth integral greater than 1 indicates that an RBW filter of

### Offset

#### Groups

- RBW Filter

#### Group members

| Name | Description |
| --- | --- |
| RFMXTDSCDMA_ATTR_SEM_NUMBER_OF_OFFSETS | Returns the number of SEM offset segments. |
| RFMXTDSCDMA_ATTR_SEM_OFFSET_BANDWIDTH_INTEGRAL | Returns the bandwidth integral for a specific offset segment. A bandwidth integral greater than 1 indicates that an RBW filter of a narrower bandwidth is used for the offset segment measurement, and digital processing is used to achieve the RBW defined for the offset segment. The offset segment RBW is calculated using the following formula: |
| RFMXTDSCDMA_ATTR_SEM_OFFSET_START_FREQUENCY | Returns the start frequency of an SEM offset segment, relative to the carrier frequency. This value is expressed in Hz. |
| RFMXTDSCDMA_ATTR_SEM_OFFSET_STOP_FREQUENCY | Returns the stop frequency of an SEM offset segment, relative to the carrier frequency. This value is expressed in Hz. |

#### Attachments

None

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__sem__offset__rbw__filter_1ga230576ee183b1a3bcf7852e2bc934d9a.html language=enus -->
## TOPIC 00124: RFMXTDSCDMA_ATTR_SEM_OFFSET_RBW_FILTER_BANDWIDTH

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__sem__offset__rbw__filter_1ga230576ee183b1a3bcf7852e2bc934d9a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__sem__offset__rbw__filter_1ga230576ee183b1a3bcf7852e2bc934d9a.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the bandwidth of the RBW filter used to sweep the offset segment. This value is expressed in Hz. SyntaxRFMXTDSCDMA_ATTR_SEM_OFFSET_RBW_FILTER_BANDWIDTHNumeric ValueData TypeAccessApplies To7372823float64Read-OnlyOffsetRemarks Use "offset<n>" as the Selector String to read this attribute.

### RFMXTDSCDMA_ATTR_SEM_OFFSET_RBW_FILTER_BANDWIDTH

Returns the bandwidth of the RBW filter used to sweep the offset segment. This value is expressed in Hz.

#### Syntax

RFMXTDSCDMA_ATTR_SEM_OFFSET_RBW_FILTER_BANDWIDTH

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 7372823 | float64 | Read-Only | Offset |

#### Remarks

Use "offset<n>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this attribute.

Parent topic:

RBW Filter

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__sem__results_1ga6f7317c8f289d2e5da60b0c1e9273a1f.html language=enus -->
## TOPIC 00125: RFMXTDSCDMA_ATTR_SEM_RESULTS_MEASUREMENT_STATUS

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__sem__results_1ga6f7317c8f289d2e5da60b0c1e9273a1f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__sem__results_1ga6f7317c8f289d2e5da60b0c1e9273a1f.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the overall measurement status based on the measurement limits specified by the standard for each offset segment. SyntaxRFMXTDSCDMA_ATTR_SEM_RESULTS_MEASUREMENT_STATUSNumeric ValueData TypeAccessApplies To7372841int32Read-OnlyN/ARemarks You do not need to use a selector string to configure

### RFMXTDSCDMA_ATTR_SEM_RESULTS_MEASUREMENT_STATUS

Indicates the overall measurement status based on the measurement limits specified by the standard for each offset segment.

#### Syntax

RFMXTDSCDMA_ATTR_SEM_RESULTS_MEASUREMENT_STATUS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 7372841 | int32 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal and result instances. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

| Name | Value | Description |
| --- | --- | --- |
| RFMXTDSCDMA_VAL_SEM_MEASUREMENT_STATUS_FAIL | 0 (0x0) | The measurement failed according to the measurement limits and criteria you set. |
| RFMXTDSCDMA_VAL_SEM_MEASUREMENT_STATUS_PASS | 1 (0x1) | The measurement passed according to the measurement limits and criteria you set. |

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__sem__results__carrier.html language=enus -->
## TOPIC 00126: Carrier

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__sem__results__carrier.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__sem__results__carrier.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXTDSCDMA_ATTR_SEM_RESULTS_CARRIER_ABSOLUTE_INTEGRATED_POWERReturns the measurement absolute carrier power. This value is expressed in dBm. AttachmentsNone

### Carrier

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXTDSCDMA_ATTR_SEM_RESULTS_CARRIER_ABSOLUTE_INTEGRATED_POWER | Returns the measurement absolute carrier power. This value is expressed in dBm. |

#### Attachments

None

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__sem__results__lower__offset_1ga0517def031101515cc6495a3e25a5913.html language=enus -->
## TOPIC 00127: RFMXTDSCDMA_ATTR_SEM_RESULTS_LOWER_OFFSET_PEAK_FREQUENCY

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__sem__results__lower__offset_1ga0517def031101515cc6495a3e25a5913.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__sem__results__lower__offset_1ga0517def031101515cc6495a3e25a5913.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the frequency at which the peak power occurred in the lower offset segment. This value is expressed in Hz. SyntaxRFMXTDSCDMA_ATTR_SEM_RESULTS_LOWER_OFFSET_PEAK_FREQUENCYNumeric ValueData TypeAccessApplies To7372856float64Read-OnlyOffsetRemarks Use "offset<i><n></i>" as the Selector String to

### RFMXTDSCDMA_ATTR_SEM_RESULTS_LOWER_OFFSET_PEAK_FREQUENCY

Returns the frequency at which the peak power occurred in the lower offset segment. This value is expressed in Hz.

#### Syntax

RFMXTDSCDMA_ATTR_SEM_RESULTS_LOWER_OFFSET_PEAK_FREQUENCY

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 7372856 | float64 | Read-Only | Offset |

#### Remarks

Use "offset<i><n></i>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result.

Parent topic:

Lower Offset

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__sem__results__lower__offset_1ga14a1f6607e903e1302966331f63b4e4e.html language=enus -->
## TOPIC 00128: RFMXTDSCDMA_ATTR_SEM_RESULTS_LOWER_OFFSET_ABSOLUTE_INTEGRATED_POWER

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__sem__results__lower__offset_1ga14a1f6607e903e1302966331f63b4e4e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__sem__results__lower__offset_1ga14a1f6607e903e1302966331f63b4e4e.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the absolute power measured in the lower (negative) offset segment. This value is expressed in dBm. SyntaxRFMXTDSCDMA_ATTR_SEM_RESULTS_LOWER_OFFSET_ABSOLUTE_INTEGRATED_POWERNumeric ValueData TypeAccessApplies To7372852float64Read-OnlyOffsetRemarks Use "offset<i><n></i>" as the Selector Strin

### RFMXTDSCDMA_ATTR_SEM_RESULTS_LOWER_OFFSET_ABSOLUTE_INTEGRATED_POWER

Returns the absolute power measured in the lower (negative) offset segment. This value is expressed in dBm.

#### Syntax

RFMXTDSCDMA_ATTR_SEM_RESULTS_LOWER_OFFSET_ABSOLUTE_INTEGRATED_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 7372852 | float64 | Read-Only | Offset |

#### Remarks

Use "offset<i><n></i>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result.

Parent topic:

Lower Offset

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__sem__results__lower__offset_1ga315a052fb03db279926181da701a3839.html language=enus -->
## TOPIC 00129: RFMXTDSCDMA_ATTR_SEM_RESULTS_LOWER_OFFSET_MEASUREMENT_STATUS

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__sem__results__lower__offset_1ga315a052fb03db279926181da701a3839.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__sem__results__lower__offset_1ga315a052fb03db279926181da701a3839.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the lower offset segment measurement status based on the measurement limits specified by the standard. SyntaxRFMXTDSCDMA_ATTR_SEM_RESULTS_LOWER_OFFSET_MEASUREMENT_STATUSNumeric ValueData TypeAccessApplies To7372861int32Read-OnlyOffsetRemarks Use "offset<i><n></i>" as the Selector String to

### RFMXTDSCDMA_ATTR_SEM_RESULTS_LOWER_OFFSET_MEASUREMENT_STATUS

Indicates the lower offset segment measurement status based on the measurement limits specified by the standard.

#### Syntax

RFMXTDSCDMA_ATTR_SEM_RESULTS_LOWER_OFFSET_MEASUREMENT_STATUS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 7372861 | int32 | Read-Only | Offset |

#### Remarks

Use "offset<i><n></i>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result.

| Name | Value | Description |
| --- | --- | --- |
| RFMXTDSCDMA_VAL_SEM_LOWER_OFFSET_MEASUREMENT_STATUS_FAIL | 0 (0x0) | The lower offset segment measurement failed according to the measurement limits and criteria you set. |
| RFMXTDSCDMA_VAL_SEM_LOWER_OFFSET_MEASUREMENT_STATUS_PASS | 1 (0x1) | The lower offset segment measurement passed according to the measurement limits and criteria you set. |

Parent topic:

Lower Offset

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__sem__results__lower__offset_1gaa007a5fbb648a663bece5d9f09a22289.html language=enus -->
## TOPIC 00130: RFMXTDSCDMA_ATTR_SEM_RESULTS_LOWER_OFFSET_RELATIVE_INTEGRATED_POWER

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__sem__results__lower__offset_1gaa007a5fbb648a663bece5d9f09a22289.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__sem__results__lower__offset_1gaa007a5fbb648a663bece5d9f09a22289.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the power measured in the lower (negative) offset segment relative to the integrated power of the reference carrier. This value is expressed in dB. SyntaxRFMXTDSCDMA_ATTR_SEM_RESULTS_LOWER_OFFSET_RELATIVE_INTEGRATED_POWERNumeric ValueData TypeAccessApplies To7372853float64Read-OnlyOffsetRema

### RFMXTDSCDMA_ATTR_SEM_RESULTS_LOWER_OFFSET_RELATIVE_INTEGRATED_POWER

Returns the power measured in the lower (negative) offset segment relative to the integrated power of the reference carrier. This value is expressed in dB.

#### Syntax

RFMXTDSCDMA_ATTR_SEM_RESULTS_LOWER_OFFSET_RELATIVE_INTEGRATED_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 7372853 | float64 | Read-Only | Offset |

#### Remarks

Use "offset<i><n></i>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result.

Parent topic:

Lower Offset

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__sem__results__lower__offset_1gaa5e5c8d616b75e4fdae45f0b428139a5.html language=enus -->
## TOPIC 00131: RFMXTDSCDMA_ATTR_SEM_RESULTS_LOWER_OFFSET_MARGIN_RELATIVE_POWER

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__sem__results__lower__offset_1gaa5e5c8d616b75e4fdae45f0b428139a5.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__sem__results__lower__offset_1gaa5e5c8d616b75e4fdae45f0b428139a5.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the power at which the margin occurred in the lower (negative) offset segment relative to the integrated power of the reference carrier. This value is expressed in dB. SyntaxRFMXTDSCDMA_ATTR_SEM_RESULTS_LOWER_OFFSET_MARGIN_RELATIVE_POWERNumeric ValueData TypeAccessApplies To7372859float64Rea

### RFMXTDSCDMA_ATTR_SEM_RESULTS_LOWER_OFFSET_MARGIN_RELATIVE_POWER

Returns the power at which the margin occurred in the lower (negative) offset segment relative to the integrated power of the reference carrier. This value is expressed in dB.

#### Syntax

RFMXTDSCDMA_ATTR_SEM_RESULTS_LOWER_OFFSET_MARGIN_RELATIVE_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 7372859 | float64 | Read-Only | Offset |

#### Remarks

Use "offset<i><n></i>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result.

Parent topic:

Lower Offset

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__sem__results__upper__offset_1ga0480bb7d3dac1bde5afddc726741fec7.html language=enus -->
## TOPIC 00132: RFMXTDSCDMA_ATTR_SEM_RESULTS_UPPER_OFFSET_MARGIN

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__sem__results__upper__offset_1ga0480bb7d3dac1bde5afddc726741fec7.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__sem__results__upper__offset_1ga0480bb7d3dac1bde5afddc726741fec7.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the margin from the limit mask value specified by the standard. This value is expressed in dB. Margin is defined as the minimum distance between the spectrum and the limit mask. SyntaxRFMXTDSCDMA_ATTR_SEM_RESULTS_UPPER_OFFSET_MARGINNumeric ValueData TypeAccessApplies To7372870float64Read-Onl

### RFMXTDSCDMA_ATTR_SEM_RESULTS_UPPER_OFFSET_MARGIN

Returns the margin from the limit mask value specified by the standard. This value is expressed in dB. Margin is defined as the minimum distance between the spectrum and the limit mask.

#### Syntax

RFMXTDSCDMA_ATTR_SEM_RESULTS_UPPER_OFFSET_MARGIN

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 7372870 | float64 | Read-Only | Offset |

#### Remarks

Use "offset<i><n></i>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result.

Parent topic:

Upper Offset

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__sem__results__upper__offset_1ga1c296262f654bd6dc10d94e3aaf394d8.html language=enus -->
## TOPIC 00133: RFMXTDSCDMA_ATTR_SEM_RESULTS_UPPER_OFFSET_RELATIVE_PEAK_POWER

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__sem__results__upper__offset_1ga1c296262f654bd6dc10d94e3aaf394d8.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__sem__results__upper__offset_1ga1c296262f654bd6dc10d94e3aaf394d8.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the peak power measured in the upper (positive) offset segment relative to the integrated power of the reference carrier. SyntaxRFMXTDSCDMA_ATTR_SEM_RESULTS_UPPER_OFFSET_RELATIVE_PEAK_POWERNumeric ValueData TypeAccessApplies To7372868float64Read-OnlyOffsetRemarks Use "offset<i><n></i>" as th

### RFMXTDSCDMA_ATTR_SEM_RESULTS_UPPER_OFFSET_RELATIVE_PEAK_POWER

Returns the peak power measured in the upper (positive) offset segment relative to the integrated power of the reference carrier.

#### Syntax

RFMXTDSCDMA_ATTR_SEM_RESULTS_UPPER_OFFSET_RELATIVE_PEAK_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 7372868 | float64 | Read-Only | Offset |

#### Remarks

Use "offset<i><n></i>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result

Parent topic:

Upper Offset

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__sem__results__upper__offset_1gac875c1f94f618700b43b24f6c1b4510e.html language=enus -->
## TOPIC 00134: RFMXTDSCDMA_ATTR_SEM_RESULTS_UPPER_OFFSET_MARGIN_RELATIVE_POWER

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__sem__results__upper__offset_1gac875c1f94f618700b43b24f6c1b4510e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__sem__results__upper__offset_1gac875c1f94f618700b43b24f6c1b4510e.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the power at which the margin occurred in the upper (positive) offset segment. This value is expressed in dBm. SyntaxRFMXTDSCDMA_ATTR_SEM_RESULTS_UPPER_OFFSET_MARGIN_RELATIVE_POWERNumeric ValueData TypeAccessApplies To7372872float64Read-OnlyOffsetRemarks Use "offset<i><n></i>" as the Selecto

### RFMXTDSCDMA_ATTR_SEM_RESULTS_UPPER_OFFSET_MARGIN_RELATIVE_POWER

Returns the power at which the margin occurred in the upper (positive) offset segment. This value is expressed in dBm.

#### Syntax

RFMXTDSCDMA_ATTR_SEM_RESULTS_UPPER_OFFSET_MARGIN_RELATIVE_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 7372872 | float64 | Read-Only | Offset |

#### Remarks

Use "offset<i><n></i>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result.

Parent topic:

Upper Offset

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__sem__sweep__time.html language=enus -->
## TOPIC 00135: Sweep Time

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__sem__sweep__time.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__sem__sweep__time.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXTDSCDMA_ATTR_SEM_SWEEP_TIME_AUTOSpecifies whether the measurement calculates the sweep time. RFMXTDSCDMA_ATTR_SEM_SWEEP_TIME_INTERVALSpecifies the sweep time when you set the RFMXTDSCDMA_ATTR_SEM_SWEEP_TIME_AUTO attribute to False. This value is expressed in

### Sweep Time

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXTDSCDMA_ATTR_SEM_SWEEP_TIME_AUTO | Specifies whether the measurement calculates the sweep time. |
| RFMXTDSCDMA_ATTR_SEM_SWEEP_TIME_INTERVAL | Specifies the sweep time when you set the RFMXTDSCDMA_ATTR_SEM_SWEEP_TIME_AUTO attribute to False. This value is expressed in seconds. |

#### Attachments

None

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__slotpower.html language=enus -->
## TOPIC 00136: SlotPower

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__slotpower.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__slotpower.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXTDSCDMA_ATTR_SLOTPOWER_MEASUREMENT_ENABLEDSpecifies whether to enable the SlotPower measurement. RFMXTDSCDMA_ATTR_SLOTPOWER_MEASUREMENT_LENGTHSpecifies the measurement length for the SlotPower measurement. This value is expressed in slots. The SlotPower meas

### SlotPower

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXTDSCDMA_ATTR_SLOTPOWER_MEASUREMENT_ENABLED | Specifies whether to enable the SlotPower measurement. |
| RFMXTDSCDMA_ATTR_SLOTPOWER_MEASUREMENT_LENGTH | Specifies the measurement length for the SlotPower measurement. This value is expressed in slots. The SlotPower measurement assumes that there is only one active traffic time slot per subframe, and that the position of this active time slot is the same in each subframe. Additionally, it assumes that there are no pilots present in the received signal. |
| RFMXTDSCDMA_ATTR_SLOTPOWER_RRC_FILTER_ENABLED | Specifies whether the RRC filter should be enabled or not. |
| RFMXTDSCDMA_ATTR_SLOTPOWER_SPECTRUM_INVERTED | Specifies whether the spectrum of the signal is inverted. |

#### Attachments

None

Parent topic:

Attributes

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__slotpower_1ga583a5832e72ae323c76175a88de55c51.html language=enus -->
## TOPIC 00137: RFMXTDSCDMA_ATTR_SLOTPOWER_RRC_FILTER_ENABLED

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__slotpower_1ga583a5832e72ae323c76175a88de55c51.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__slotpower_1ga583a5832e72ae323c76175a88de55c51.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the RRC filter should be enabled or not. SyntaxRFMXTDSCDMA_ATTR_SLOTPOWER_RRC_FILTER_ENABLEDNumeric ValueData TypeAccessApplies To7376900int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to

### RFMXTDSCDMA_ATTR_SLOTPOWER_RRC_FILTER_ENABLED

Specifies whether the RRC filter should be enabled or not.

#### Syntax

RFMXTDSCDMA_ATTR_SLOTPOWER_RRC_FILTER_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 7376900 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **True**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXTDSCDMA_VAL_SLOTPOWER_RRC_FILTER_ENABLED_FALSE | 0 (0x0) | Disables the RRC filter in the SlotPower measurement. |
| RFMXTDSCDMA_VAL_SLOTPOWER_RRC_FILTER_ENABLED_TRUE | 1 (0x1) | Enables the RRC filter in the SlotPower measurement. |

Parent topic:

SlotPower

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__trigger.html language=enus -->
## TOPIC 00138: Trigger

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__trigger.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__trigger.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsDigital EdgeIQ Power EdgeMinimum Quiet TimeGroup membersNameDescriptionRFMXTDSCDMA_ATTR_TRIGGER_DELAYSpecifies the trigger delay time. This value is expressed in seconds. RFMXTDSCDMA_ATTR_TRIGGER_TYPESpecifies the trigger type. AttachmentsNone

### Trigger

#### Groups

- Digital Edge
- IQ Power Edge
- Minimum Quiet Time

#### Group members

| Name | Description |
| --- | --- |
| RFMXTDSCDMA_ATTR_TRIGGER_DELAY | Specifies the trigger delay time. This value is expressed in seconds. |
| RFMXTDSCDMA_ATTR_TRIGGER_TYPE | Specifies the trigger type. |

#### Attachments

None

Parent topic:

Attributes

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__trigger_1ga98a3bd7539515d5f94dfeaee65d746f6.html language=enus -->
## TOPIC 00139: RFMXTDSCDMA_ATTR_TRIGGER_TYPE

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__trigger_1ga98a3bd7539515d5f94dfeaee65d746f6.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__trigger_1ga98a3bd7539515d5f94dfeaee65d746f6.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the trigger type. SyntaxRFMXTDSCDMA_ATTR_TRIGGER_TYPENumeric ValueData TypeAccessApplies To7340036int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information about

### RFMXTDSCDMA_ATTR_TRIGGER_TYPE

Specifies the trigger type.

#### Syntax

RFMXTDSCDMA_ATTR_TRIGGER_TYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 7340036 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **IQ Power Edge**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXTDSCDMA_VAL_TRIGGER_TYPE_NONE | 0 (0x0) | No Reference Trigger is configured. |
| RFMXTDSCDMA_VAL_TRIGGER_TYPE_DIGITAL_EDGE | 1 (0x1) | The Reference Trigger is not asserted until a digital edge is detected. The source of the digital edge is specified using the RFMXTDSCDMA_ATTR_DIGITAL_EDGE_TRIGGER_SOURCE attribute. |
| RFMXTDSCDMA_VAL_TRIGGER_TYPE_IQ_POWER_EDGE | 2 (0x2) | The Reference Trigger is asserted when the signal changes past the level specified by the rising or falling slope, which is configured using the RFMXTDSCDMA_ATTR_IQ_POWER_EDGE_TRIGGER_SLOPE attribute. |
| RFMXTDSCDMA_VAL_TRIGGER_TYPE_SOFTWARE | 3 (0x3) | The trigger is not asserted until a software trigger occurs. |

Parent topic:

Trigger

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__trigger__digital__edge.html language=enus -->
## TOPIC 00140: Digital Edge

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__trigger__digital__edge.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__trigger__digital__edge.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXTDSCDMA_ATTR_DIGITAL_EDGE_TRIGGER_EDGESpecifies the active edge for the trigger. This attribute is used only when you set the RFMXTDSCDMA_ATTR_TRIGGER_TYPE attribute to Digital Edge. RFMXTDSCDMA_ATTR_DIGITAL_EDGE_TRIGGER_SOURCESpecifies the source terminal f

### Digital Edge

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXTDSCDMA_ATTR_DIGITAL_EDGE_TRIGGER_EDGE | Specifies the active edge for the trigger. This attribute is used only when you set the RFMXTDSCDMA_ATTR_TRIGGER_TYPE attribute to Digital Edge. |
| RFMXTDSCDMA_ATTR_DIGITAL_EDGE_TRIGGER_SOURCE | Specifies the source terminal for the digital edge trigger. This attribute is used only when you set the RFMXTDSCDMA_ATTR_TRIGGER_TYPE attribute to Digital Edge. |

#### Attachments

None

Parent topic:

Trigger

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__trigger__iq__power__edge_1ga37042d3e5cae867ed4434d14d9dec4b5.html language=enus -->
## TOPIC 00141: RFMXTDSCDMA_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__trigger__iq__power__edge_1ga37042d3e5cae867ed4434d14d9dec4b5.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__trigger__iq__power__edge_1ga37042d3e5cae867ed4434d14d9dec4b5.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the threshold above or below which the signal analyzer triggers, depending on the value of the RFMXTDSCDMA_ATTR_IQ_POWER_EDGE_TRIGGER_SLOPE attribute. This value is expressed in dB when the RFMXTDSCDMA_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE attribute is set to Relative or in dBm when the IQ

### RFMXTDSCDMA_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL

Specifies the threshold above or below which the signal analyzer triggers, depending on the value of the [RFMXTDSCDMA_ATTR_IQ_POWER_EDGE_TRIGGER_SLOPE](group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__trigger__iq__power__edge_1gaaf0294a3fa6d0298362733f947a9c002.html) attribute. This value is expressed in dB when the [RFMXTDSCDMA_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE](group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__trigger__iq__power__edge_1ga49e39d558dc91428f20921e97add78fa.html) attribute is set to **Relative** or in dBm when the IQ Power Edge Level Type attribute is set to **Absolute**.

#### Syntax

RFMXTDSCDMA_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 7340040 | float64 | Read/Write | N/A |

#### Remarks

The device asserts the trigger when the signal exceeds the level specified by the value of this attribute, taking into consideration the specified slope. This attribute is used only when you set the [RFMXTDSCDMA_ATTR_TRIGGER_TYPE](group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__trigger_1ga98a3bd7539515d5f94dfeaee65d746f6.html) attribute to **IQ Power Edge**.

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default of this attribute is hardware dependent.

Parent topic:

IQ Power Edge

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__trigger__iq__power__edge_1ga5d31837e9544b12749643b341037fc26.html language=enus -->
## TOPIC 00142: RFMXTDSCDMA_ATTR_IQ_POWER_EDGE_TRIGGER_SOURCE

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__trigger__iq__power__edge_1ga5d31837e9544b12749643b341037fc26.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__trigger__iq__power__edge_1ga5d31837e9544b12749643b341037fc26.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the channel from which the device monitors the trigger. This attribute is used only when you set the RFMXTDSCDMA_ATTR_TRIGGER_TYPE attribute to IQ Power Edge. SyntaxRFMXTDSCDMA_ATTR_IQ_POWER_EDGE_TRIGGER_SOURCENumeric ValueData TypeAccessApplies To7340039char[]Read/WriteN/ARemarks You do n

### RFMXTDSCDMA_ATTR_IQ_POWER_EDGE_TRIGGER_SOURCE

Specifies the channel from which the device monitors the trigger. This attribute is used only when you set the [RFMXTDSCDMA_ATTR_TRIGGER_TYPE](group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__trigger_1ga98a3bd7539515d5f94dfeaee65d746f6.html) attribute to **IQ Power Edge**.

#### Syntax

RFMXTDSCDMA_ATTR_IQ_POWER_EDGE_TRIGGER_SOURCE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 7340039 | char[] | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default of this attribute is hardware dependent.

Parent topic:

IQ Power Edge

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__advanced_1gabba15a2638cb29813562d7e167d1b818.html language=enus -->
## TOPIC 00143: RFmxTDSCDMA_ClearNamedResult

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__advanced_1gabba15a2638cb29813562d7e167d1b818.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__advanced_1gabba15a2638cb29813562d7e167d1b818.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Clears a result instance specified by the result name in the Selector String parameter. Syntaxint32 __stdcall RFmxTDSCDMA_ClearNamedResult(niRFmxInstrHandle instrumentHandle, char selectorString[])ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifies the

### RFmxTDSCDMA_ClearNamedResult

Clears a result instance specified by the result name in the **Selector String** parameter.

#### Syntax

int32 __stdcall RFmxTDSCDMA_ClearNamedResult(niRFmxInstrHandle instrumentHandle, char selectorString[])

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__advanced_1gad6578bf6c5abf19de693e29bd516219d.html language=enus -->
## TOPIC 00144: RFmxTDSCDMA_CreateSignalConfiguration

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__advanced_1gad6578bf6c5abf19de693e29bd516219d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__advanced_1gad6578bf6c5abf19de693e29bd516219d.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a new instance of a signal. Syntaxint32 __stdcall RFmxTDSCDMA_CreateSignalConfiguration(niRFmxInstrHandle instrumentHandle, char signalName[])ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifies the RFmx session refnum. This parameter is obtaine

### RFmxTDSCDMA_CreateSignalConfiguration

Creates a new instance of a signal.

#### Syntax

int32 __stdcall RFmxTDSCDMA_CreateSignalConfiguration(niRFmxInstrHandle instrumentHandle, char signalName[])

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| signalName | [in] | char[] | This parameter specifies the name of the signal. This input accepts the signal name with or without the "signal::" prefix.Example:"signal::sig1""sig1" |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__advanced_1gade024537f6d9ba5f5006dfa5f2feeca4.html language=enus -->
## TOPIC 00145: RFmxTDSCDMA_DeleteSignalConfiguration

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__advanced_1gade024537f6d9ba5f5006dfa5f2feeca4.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__advanced_1gade024537f6d9ba5f5006dfa5f2feeca4.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Deletes an instance of a signal that you specify in the Signal Name parameter. Syntaxint32 __stdcall RFmxTDSCDMA_DeleteSignalConfiguration(niRFmxInstrHandle instrumentHandle, char signalName[])ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifies the RFm

### RFmxTDSCDMA_DeleteSignalConfiguration

Deletes an instance of a signal that you specify in the **Signal Name** parameter.

#### Syntax

int32 __stdcall RFmxTDSCDMA_DeleteSignalConfiguration(niRFmxInstrHandle instrumentHandle, char signalName[])

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| signalName | [in] | char[] | This parameter specifies the name of the signal. This input accepts the signal name with or without the "signal::" prefix.Example:"signal::sig1""sig1" |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__advanced_1gaed8ab27ed618d48d325fe292d8743a41.html language=enus -->
## TOPIC 00146: RFmxTDSCDMA_GetAllNamedResultNames

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__advanced_1gaed8ab27ed618d48d325fe292d8743a41.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__advanced_1gaed8ab27ed618d48d325fe292d8743a41.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the named result names of the signal that you specify in the Selector String parameter. Syntaxint32 __stdcall RFmxTDSCDMA_GetAllNamedResultNames(niRFmxInstrHandle instrumentHandle, char selectorString[], char resultNames[], int32 resultNamesBufferSize, int32 *actualResultNamesSize, int32 *de

### RFmxTDSCDMA_GetAllNamedResultNames

Returns the named result names of the signal that you specify in the **Selector String** parameter.

#### Syntax

int32 __stdcall RFmxTDSCDMA_GetAllNamedResultNames(niRFmxInstrHandle instrumentHandle, char selectorString[], char resultNames[], int32 resultNamesBufferSize, int32 *actualResultNamesSize, int32 *defaultResultExists)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function or the RFmxInstr Initialize function with the option string as "AnalysisOnly=1". |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Examples:"""signal::sig1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| resultNames | [out] | char[] | This parameter returns an array of result names. |
| resultNamesBufferSize | [in] | int32 | Specifies the size of the resultNames array. Set the resultNamesBufferSize parameter to 0 to get the size of the resultNames array in the return value. |
| actualResultNamesSize | [out] | int32 * | Returns the actual size of the resultNames array, if you pass NULL to resultNames array parameter and set the resultNamesBufferSize parameter to 0. |
| defaultResultExists | [out] | int32 * | This parameter indicates whether the default result exists. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__advanced__analyze2.html language=enus -->
## TOPIC 00147: Analyze2

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__advanced__analyze2.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__advanced__analyze2.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxTDSCDMA_AnalyzeIQ1WaveformPerforms the enabled measurements on the I/Q complex waveform that you specify in the IQ parameter. Call this function after you configure the signal and measurement attributes. You can fetch measurement results using the Fetch func

### Analyze2

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxTDSCDMA_AnalyzeIQ1Waveform | Performs the enabled measurements on the I/Q complex waveform that you specify in the IQ parameter. Call this function after you configure the signal and measurement attributes. You can fetch measurement results using the Fetch functions or result attributes in the attribute node. Use this function only if the RFMXINSTR_ATTR_RECOMMENDED_ACQUISITION_TYPE attribute value is either IQ or IQ or Spectral. Note Query the Recommended Acquisition Type attribute from the RFmxInstr Attribute after calling the RFmxTDSCDMA_Commit function. |
| RFmxTDSCDMA_AnalyzeIQ1WaveformSplit | Performs the enabled measurements on the I/Q complex waveform that you specify in the IQ parameter. Call this function after you configure the signal and measurement attributes. You can fetch measurement results using the Fetch functions or result attributes in the attribute node. Use this function only if the RFMXINSTR_ATTR_RECOMMENDED_ACQUISITION_TYPE attribute value is either IQ or IQ or Spectral. Note Query the Recommended Acquisition Type attribute from the RFmxInstr Attribute after calling the RFmxTDSCDMA_Commit function. |
| RFmxTDSCDMA_AnalyzeSpectrum1Waveform | Performs the enabled measurements on the Spectrum waveform that you specify in the Spectrum parameter. Call this function after you configure the signal and measurement attributes. You can fetch measurement results using the Fetch functions or result attributes in the attribute node. Use this function only if the RFMXINSTR_ATTR_RECOMMENDED_ACQUISITION_TYPE attribute value is either Spectral or IQ or Spectral. Note Query the Recommended Acquisition Type attribute from the RFmxInstr Attribute after calling the RFmxTDSCDMA_Commit function. |

#### Attachments

None

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__advanced__analyze2_1ga0299936c6fc20739926001444da0a18d.html language=enus -->
## TOPIC 00148: RFmxTDSCDMA_AnalyzeIQ1WaveformSplit

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__advanced__analyze2_1ga0299936c6fc20739926001444da0a18d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__advanced__analyze2_1ga0299936c6fc20739926001444da0a18d.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs the enabled measurements on the I/Q complex waveform that you specify in the IQ parameter. Call this function after you configure the signal and measurement attributes. You can fetch measurement results using the Fetch functions or result attributes in the attribute node. Use this function

### RFmxTDSCDMA_AnalyzeIQ1WaveformSplit

Performs the enabled measurements on the I/Q complex waveform that you specify in the **IQ** parameter. Call this function after you configure the signal and measurement attributes. You can fetch measurement results using the Fetch functions or result attributes in the attribute node. Use this function only if the [RFMXINSTR_ATTR_RECOMMENDED_ACQUISITION_TYPE](/csh?context=rfmxinstr_rfmxinstrcref_attribute_recommended_acquisition_type) attribute value is either **IQ** or **IQ or Spectral**.

Note

Query the Recommended Acquisition Type attribute from the RFmxInstr Attribute after calling the [RFmxTDSCDMA_Commit](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__utility_1gabc14af37bc05dd6bdf1a3acf6252a9b0.html) function.

#### Syntax

int32 __stdcall RFmxTDSCDMA_AnalyzeIQ1WaveformSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], char resultName[], float64 x0, float64 dx, float32 iqI[], float32 iqQ[], int32 arraySize, int32 reset, int64 reserved)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function or the RFmxInstr Initialize function with the option string as "AnalysisOnly=1". |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and the result name. The result name can be specified either through this input or through the Result Name input. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name in this input, either the result name specified by the Result Name input or the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| resultName | [in] | char[] | This parameter specifies the name to be associated with measurement results. Provide a unique name, such as "r1", to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. The default value is "" (empty string), which refers to default result instance.Example:"""result::r1""r1" |
| x0 | [in] | float64 | This parameter specifies the start time of the input y array. This value is expressed in seconds. |
| dx | [in] | float64 | This parameter specifies the time interval between the samples in the input y array. This value is expressed in seconds. The reciprocal of dx indicates the I/Q rate of the input signal. |
| iqI | [in] | float32[] | This parameter specifies an array of complex-valued time domain data. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively. |
| iqQ | [in] | float32[] | This parameter specifies an array of complex-valued time domain data. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively. |
| arraySize | [in] | int32 | Specifies the size of the array. |
| reset | [in] | int32 | This parameter resets measurement averaging. If you enable averaging, set this parameter to TRUE for the first record and FALSE for the subsequent records. |
| reserved | [in] | int64 | Reserved for future use. Any value passed to this parameter will be ignored. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Analyze2

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__advanced__analyze2_1ga7e18bfb2c31a3ef1936370c16fb53e8f.html language=enus -->
## TOPIC 00149: RFmxTDSCDMA_AnalyzeSpectrum1Waveform

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__advanced__analyze2_1ga7e18bfb2c31a3ef1936370c16fb53e8f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__advanced__analyze2_1ga7e18bfb2c31a3ef1936370c16fb53e8f.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs the enabled measurements on the Spectrum waveform that you specify in the Spectrum parameter. Call this function after you configure the signal and measurement attributes. You can fetch measurement results using the Fetch functions or result attributes in the attribute node. Use this functi

### RFmxTDSCDMA_AnalyzeSpectrum1Waveform

Performs the enabled measurements on the Spectrum waveform that you specify in the **Spectrum** parameter. Call this function after you configure the signal and measurement attributes. You can fetch measurement results using the Fetch functions or result attributes in the attribute node. Use this function only if the [RFMXINSTR_ATTR_RECOMMENDED_ACQUISITION_TYPE](/csh?context=rfmxinstr_rfmxinstrcref_attribute_recommended_acquisition_type) attribute value is either **Spectral** or **IQ or Spectral**.

Note

Query the Recommended Acquisition Type attribute from the RFmxInstr Attribute after calling the [RFmxTDSCDMA_Commit](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__utility_1gabc14af37bc05dd6bdf1a3acf6252a9b0.html) function.

#### Syntax

int32 __stdcall RFmxTDSCDMA_AnalyzeSpectrum1Waveform(niRFmxInstrHandle instrumentHandle, char selectorString[], char resultName[], float64 x0, float64 dx, float32 spectrum[], int32 arraySize, int32 reset, int64 reserved)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function or the RFmxInstr Initialize function with the option string as "AnalysisOnly=1". |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and the result name. The result name can be specified either through this input or through the Result Name input. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name in this input, either the result name specified by the Result Name input or the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| resultName | [in] | char[] | This parameter specifies the name to be associated with measurement results. Provide a unique name, such as "r1", to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. The default value is "" (empty string), which refers to default result instance.Example:"""result::r1""r1" |
| x0 | [in] | float64 | This parameter specifies the start frequency of the spectrum. This value is expressed in Hz. |
| dx | [in] | float64 | This parameter specifies the frequency interval between data points in the spectrum. |
| spectrum | [in] | float32[] | This parameter specifies the real-value power spectrum. |
| arraySize | [in] | int32 | Specifies the size of the array. |
| reset | [in] | int32 | This parameter resets measurement averaging. If you enable averaging, set this parameter to TRUE for the first record and FALSE for the subsequent records. |
| reserved | [in] | int64 | Reserved for future use. Any value passed to this parameter will be ignored. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Analyze2

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__advanced__analyze2_1gaf1a6293e4207e68e4bbb409b306659e0.html language=enus -->
## TOPIC 00150: RFmxTDSCDMA_AnalyzeIQ1Waveform

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__advanced__analyze2_1gaf1a6293e4207e68e4bbb409b306659e0.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__advanced__analyze2_1gaf1a6293e4207e68e4bbb409b306659e0.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs the enabled measurements on the I/Q complex waveform that you specify in the IQ parameter. Call this function after you configure the signal and measurement attributes. You can fetch measurement results using the Fetch functions or result attributes in the attribute node. Use this function

### RFmxTDSCDMA_AnalyzeIQ1Waveform

Performs the enabled measurements on the I/Q complex waveform that you specify in the **IQ** parameter. Call this function after you configure the signal and measurement attributes. You can fetch measurement results using the Fetch functions or result attributes in the attribute node. Use this function only if the [RFMXINSTR_ATTR_RECOMMENDED_ACQUISITION_TYPE](/csh?context=rfmxinstr_rfmxinstrcref_attribute_recommended_acquisition_type) attribute value is either **IQ** or **IQ or Spectral**.

Note

Query the Recommended Acquisition Type attribute from the RFmxInstr Attribute after calling the [RFmxTDSCDMA_Commit](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__utility_1gabc14af37bc05dd6bdf1a3acf6252a9b0.html) function.

#### Syntax

int32 __stdcall RFmxTDSCDMA_AnalyzeIQ1Waveform(niRFmxInstrHandle instrumentHandle, char selectorString[], char resultName[], float64 x0, float64 dx, NIComplexSingle iq[], int32 arraySize, int32 reset, int64 reserved)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function or the RFmxInstr Initialize function with the option string as "AnalysisOnly=1". |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and the result name. The result name can be specified either through this input or through the Result Name input. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name in this input, either the result name specified by the Result Name input or the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| resultName | [in] | char[] | This parameter specifies the name to be associated with measurement results. Provide a unique name, such as "r1", to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. The default value is "" (empty string), which refers to default result instance.Example:"""result::r1""r1" |
| x0 | [in] | float64 | This parameter specifies the start time of the input y array. This value is expressed in seconds. |
| dx | [in] | float64 | This parameter specifies the time interval between the samples in the input y array. This value is expressed in seconds. The reciprocal of dx indicates the I/Q rate of the input signal. |
| iq | [in] | NIComplexSingle[] | This parameter specifies an array of complex-valued time domain data. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively. |
| arraySize | [in] | int32 | Specifies the size of the array. |
| reset | [in] | int32 | This parameter resets measurement averaging. If you enable averaging, set this parameter to TRUE for the first record and FALSE for the subsequent records. |
| reserved | [in] | int64 | Reserved for future use. Any value passed to this parameter will be ignored. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Analyze2

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__build__string.html language=enus -->
## TOPIC 00151: Build String

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__build__string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__build__string.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxTDSCDMA_BuildChannelStringCreates a selector string to use with channel-specific configuration or fetch attributes and functions. RFmxTDSCDMA_BuildOffsetStringCreates the offset string to use as the selector string with spectral emissions mask (SEM) and adja

### Build String

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxTDSCDMA_BuildChannelString | Creates a selector string to use with channel-specific configuration or fetch attributes and functions. |
| RFmxTDSCDMA_BuildOffsetString | Creates the offset string to use as the selector string with spectral emissions mask (SEM) and adjacent channel power (ACP) offset configuration or fetch attributes and functions. |
| RFmxTDSCDMA_BuildSegmentString | Creates the segment string to use as the selector string with the power versus time (PVT) segment configuration or fetch attributes and functions. |
| RFmxTDSCDMA_BuildSignalString | Creates a selector string to use with configuration or fetch attributes and functions. |

#### Attachments

None

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__build__string_1ga1445b39275e1673e78dbcf4581579615.html language=enus -->
## TOPIC 00152: RFmxTDSCDMA_BuildSegmentString

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__build__string_1ga1445b39275e1673e78dbcf4581579615.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__build__string_1ga1445b39275e1673e78dbcf4581579615.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates the segment string to use as the selector string with the power versus time (PVT) segment configuration or fetch attributes and functions. Syntaxint32 __stdcall RFmxTDSCDMA_BuildSegmentString(char selectorString[], int32 segmentNumber, int32 selectorStringOutLength, char selectorStringOut[])

### RFmxTDSCDMA_BuildSegmentString

Creates the segment string to use as the selector string with the power versus time (PVT) segment configuration or fetch attributes and functions.

#### Syntax

int32 __stdcall RFmxTDSCDMA_BuildSegmentString(char selectorString[], int32 segmentNumber, int32 selectorStringOutLength, char selectorStringOut[])

#### Remarks

Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| segmentNumber | [in] | int32 | This parameter specifies the segment number for building the selector string. |
| selectorStringOutLength | [out] | int32 | Specifies the length of the string that is returned by the selectorStringOut parameter. To get the minimum buffer size required to build the selector string, set the selectorStringOutLength parameter to 0. |
| selectorStringOut | [out] | char[] | This parameter returns the selector string you can use in the Selector String input for Configuration functions, Fetch functions, or the RFmxTDSCDMA_Initiate function. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Build String

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__build__string_1ga3f266a28806cd5de1a645af72addf615.html language=enus -->
## TOPIC 00153: RFmxTDSCDMA_BuildOffsetString

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__build__string_1ga3f266a28806cd5de1a645af72addf615.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__build__string_1ga3f266a28806cd5de1a645af72addf615.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates the offset string to use as the selector string with spectral emissions mask (SEM) and adjacent channel power (ACP) offset configuration or fetch attributes and functions. Syntaxint32 __stdcall RFmxTDSCDMA_BuildOffsetString(char selectorString[], int32 offsetNumber, int32 selectorStringOutLe

### RFmxTDSCDMA_BuildOffsetString

Creates the offset string to use as the selector string with spectral emissions mask (SEM) and adjacent channel power (ACP) offset configuration or fetch attributes and functions.

#### Syntax

int32 __stdcall RFmxTDSCDMA_BuildOffsetString(char selectorString[], int32 offsetNumber, int32 selectorStringOutLength, char selectorStringOut[])

#### Remarks

Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| offsetNumber | [in] | int32 | This parameter specifies the offset number for building the selector string. |
| selectorStringOutLength | [out] | int32 | Specifies the length of the string that is returned by the selectorStringOut parameter. To get the minimum buffer size required to build the selector string, set the selectorStringOutLength parameter to 0. |
| selectorStringOut | [out] | char[] | This parameter returns the selector string you can use in the Selector String input for Configuration functions, Fetch functions, or the RFmxTDSCDMA_Initiate function. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Build String

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__build__string_1ga7cda32d9e538e32434f2ed18b22d1d69.html language=enus -->
## TOPIC 00154: RFmxTDSCDMA_BuildChannelString

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__build__string_1ga7cda32d9e538e32434f2ed18b22d1d69.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__build__string_1ga7cda32d9e538e32434f2ed18b22d1d69.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a selector string to use with channel-specific configuration or fetch attributes and functions. Syntaxint32 __stdcall RFmxTDSCDMA_BuildChannelString(char selectorString[], int32 channelNumber, int32 selectorStringOutLength, char selectorStringOut[])RemarksRefer to the Selector String topic f

### RFmxTDSCDMA_BuildChannelString

Creates a selector string to use with channel-specific configuration or fetch attributes and functions.

#### Syntax

int32 __stdcall RFmxTDSCDMA_BuildChannelString(char selectorString[], int32 channelNumber, int32 selectorStringOutLength, char selectorStringOut[])

#### Remarks

Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| channelNumber | [in] | int32 | This parameter specifies the channel number for building the selector string. |
| selectorStringOutLength | [out] | int32 | Specifies the length of the string that is returned by the selectorStringOut parameter. To get the minimum buffer size required to build the selector string, set the selectorStringOutLength parameter to 0. |
| selectorStringOut | [out] | char[] | This parameter returns the selector string you can use in the Selector String input for Configuration functions, Fetch functions, or the RFmxTDSCDMA_Initiate function. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Build String

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__build__string_1ga95330930a294aa366435d752cb1bf811.html language=enus -->
## TOPIC 00155: RFmxTDSCDMA_BuildSignalString

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__build__string_1ga95330930a294aa366435d752cb1bf811.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__build__string_1ga95330930a294aa366435d752cb1bf811.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a selector string to use with configuration or fetch attributes and functions. Syntaxint32 __stdcall RFmxTDSCDMA_BuildSignalString(char signalName[], char resultName[], int32 selectorStringLength, char selectorString[])RemarksRefer to the Selector String topic for information about the strin

### RFmxTDSCDMA_BuildSignalString

Creates a selector string to use with configuration or fetch attributes and functions.

#### Syntax

int32 __stdcall RFmxTDSCDMA_BuildSignalString(char signalName[], char resultName[], int32 selectorStringLength, char selectorString[])

#### Remarks

Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| signalName | [in] | char[] | This parameter specifies the name of the signal when using Signal Configurations. This input accepts the signal name with or without the "signal::" prefix. The default value is "" (empty string).Examples:"""signal::sig1""sig1" |
| resultName | [in] | char[] | This parameter specifies the name of the result when performing Named Results. This input accepts the result name with or without the "result::" prefix. The default value is "" (empty string).Examples:"""result::r1""r1" |
| selectorStringLength | [in] | int32 | Specifies the length of the selector string. Set this parameter to 0 to get the minimum buffer size required to build the selector string. |
| selectorString | [in] | char[] | This parameter returns the selector string you can use in the Selector String input for Configuration functions, Fetch functions, or other functions that build selector strings. This string contains the signal and/or result names with their appropriate prefixes.Examples:"""signal::sig1""result::r1""signal::sig1/result::r1" |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Build String

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration.html language=enus -->
## TOPIC 00156: Configuration

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsACPCDACHPFrequencyModAccOBWPVTSEMSlotPowerTriggerGroup membersNameDescriptionRFmxTDSCDMA_AutoLevelExamines the input signal to calculate the peak power level and sets it as the value of the Reference Level attribute. Use this function to calculate an approximate setting for the reference level

### Configuration

#### Groups

- ACP
- CDA
- CHP
- Frequency
- ModAcc
- OBW
- PVT
- SEM
- SlotPower
- Trigger

#### Group members

| Name | Description |
| --- | --- |
| RFmxTDSCDMA_AutoLevel | Examines the input signal to calculate the peak power level and sets it as the value of the Reference Level attribute. Use this function to calculate an approximate setting for the reference level. |
| RFmxTDSCDMA_CfgChannelConfigurationMode | Configures RFmx TD-SCDMA to detect the channels automatically or to use a specified channel configuration. |
| RFmxTDSCDMA_CfgExternalAttenuation | Specifies external attenuation to be considered by RFmx TD-SCDMA measurements, such as the attenuation of a switch or cable connected to the signal analyzer RF IN connector. |
| RFmxTDSCDMA_CfgFrequencyReference | Configures the Reference Clock and the frequency reference source. |
| RFmxTDSCDMA_CfgMechanicalAttenuation | Configures the mechanical attenuation and the RFmx driver attenuation hardware settings. |
| RFmxTDSCDMA_CfgMidambleShift | Configures the Midamble Auto Detection Mode, Maximum Number of Users, and Midamble Shift parameters. |
| RFmxTDSCDMA_CfgNumberOfChannels | Configures the number of channels for the user-defined channel configuration when the channel configuration mode is set to User Defined. |
| RFmxTDSCDMA_CfgPilot | Configures the pilot code of the TD-SCDMA signal. |
| RFmxTDSCDMA_CfgRF | Configures the RF attributes of the signal specified by the Selector String parameter. |
| RFmxTDSCDMA_CfgRFAttenuation | Configures the nominal attenuation and the RFmx driver setting. |
| RFmxTDSCDMA_CfgReferenceLevel | Configures the reference level. The reference level represents the maximum expected power of an input RF signal. |
| RFmxTDSCDMA_CfgUplinkScramblingCode | Configures the scrambling code used for the uplink transmission. |
| RFmxTDSCDMA_CfgUserDefinedChannel | Configures an individual user-defined channel when the channel configuration mode is set to User Defined. |
| RFmxTDSCDMA_CfgUserDefinedChannelArray | Configures all user-defined channels when the channel configuration mode is set to User Defined. |
| RFmxTDSCDMA_SendSoftwareEdgeTrigger | Sends a trigger to the device when you use the RFmxTDSCDMA Configure Trigger function to choose a software version of a trigger and the device is waiting for the trigger to be sent. You can also use this function to override a hardware trigger. |

#### Attachments

None

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration_1ga0101a3252722cb49b039e66566c54064.html language=enus -->
## TOPIC 00157: RFmxTDSCDMA_CfgNumberOfChannels

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration_1ga0101a3252722cb49b039e66566c54064.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration_1ga0101a3252722cb49b039e66566c54064.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the number of channels for the user-defined channel configuration when the channel configuration mode is set to User Defined. Syntaxint32 __stdcall RFmxTDSCDMA_CfgNumberOfChannels(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 numberOfChannels)ParametersNameDirectionType

### RFmxTDSCDMA_CfgNumberOfChannels

Configures the number of channels for the user-defined channel configuration when the channel configuration mode is set to **User Defined**.

#### Syntax

int32 __stdcall RFmxTDSCDMA_CfgNumberOfChannels(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 numberOfChannels)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Examples:"""signal::sig1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| numberOfChannels | [in] | int32 | This parameter specifies the number of user-defined channels. The default value is 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration_1ga0bdf3faa546df2ed62062dc2b084822b.html language=enus -->
## TOPIC 00158: RFmxTDSCDMA_CfgPilot

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration_1ga0bdf3faa546df2ed62062dc2b084822b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration_1ga0bdf3faa546df2ed62062dc2b084822b.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the pilot code of the TD-SCDMA signal. Syntaxint32 __stdcall RFmxTDSCDMA_CfgPilot(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 pilotCode)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifies the RFmx session refnum. This pa

### RFmxTDSCDMA_CfgPilot

Configures the pilot code of the TD-SCDMA signal.

#### Syntax

int32 __stdcall RFmxTDSCDMA_CfgPilot(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 pilotCode)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Examples:"""signal::sig1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| pilotCode | [in] | int32 | This parameter specifies the SYNC-UL code used by the uplink pilot time slot (UpPTS). This code is used when the RFMXTDSCDMA_ATTR_MODACC_SYNCHRONIZATION_MODE attribute is set to Subframe, or the RFMXTDSCDMA_ATTR_MODACC_SLOT_TYPE attribute is set to Pilot. The default value is 0. The valid range is 0 to 255.The Code Group of the parameter is determined by the following formula:Code Group = floor (Pilot Code / 8)The code group of the parameter should match the code group of the RFMXTDSCDMA_ATTR_UPLINK_SCRAMBLING_CODE attribute. For more information on code allocations, refer to the Code Allocation in Section 8.3 of 3GPP TS 25.223, v.11.0.0 Release 11. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration_1ga0fd4808123b2b95f6e69aa3550d788bc.html language=enus -->
## TOPIC 00159: RFmxTDSCDMA_CfgReferenceLevel

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration_1ga0fd4808123b2b95f6e69aa3550d788bc.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration_1ga0fd4808123b2b95f6e69aa3550d788bc.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the reference level. The reference level represents the maximum expected power of an input RF signal. Syntaxint32 __stdcall RFmxTDSCDMA_CfgReferenceLevel(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 referenceLevel)ParametersNameDirectionTypeDescriptioninstrumentHandl

### RFmxTDSCDMA_CfgReferenceLevel

Configures the reference level. The reference level represents the maximum expected power of an input RF signal.

#### Syntax

int32 __stdcall RFmxTDSCDMA_CfgReferenceLevel(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 referenceLevel)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Examples:"""signal::sig1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| referenceLevel | [in] | float64 | This parameter specifies the reference level that represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices. The default of this parameter is hardware dependent. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration_1ga179032346117199b0d0f603dcb07eb35.html language=enus -->
## TOPIC 00160: RFmxTDSCDMA_CfgUserDefinedChannelArray

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration_1ga179032346117199b0d0f603dcb07eb35.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration_1ga179032346117199b0d0f603dcb07eb35.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures all user-defined channels when the channel configuration mode is set to User Defined. Syntaxint32 __stdcall RFmxTDSCDMA_CfgUserDefinedChannelArray(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 slotIndex[], int32 channelType[], int32 slotFormat[], int32 modulationType[],

### RFmxTDSCDMA_CfgUserDefinedChannelArray

Configures all user-defined channels when the channel configuration mode is set to **User Defined**.

#### Syntax

int32 __stdcall RFmxTDSCDMA_CfgUserDefinedChannelArray(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 slotIndex[], int32 channelType[], int32 slotFormat[], int32 modulationType[], int32 channelizationCode[], int32 numberOfElements)

#### Remarks

Use equal-sized arrays for **Slot Index**, **Channel Type**, and **Modulation Type**. You can configure up to two channels for the same index for multi-code transmission.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Examples:"""signal::sig1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| slotIndex | [in] | int32[] | This parameter specifies the slot index used for the current user defined channel configuration.The slot index is numbered according to the start time of the acquisition. For example, slot index 0 is the first slot detected in the acquired signal.Valid Values: 0 to 6 |
| channelType | [in] | int32[] | This parameter specifies the TD-SCDMA channel type. The default value is Idle.Name (value)DescriptionIdle (0)Specifies that the user-defined channel type is an empty slot.DPCH (1)Specifies that the user-defined channel is a dedicated physical channel (DPCH).EDCH (2)Specifies that the user-defined channel is an enhanced dedicated channel (EDCH).HSSICH (3)Specifies that the user-defined channel is a shared information channel for high-speed downlink. |
| Name (value) | Description |  |  |
| Idle (0) | Specifies that the user-defined channel type is an empty slot. |  |  |
| DPCH (1) | Specifies that the user-defined channel is a dedicated physical channel (DPCH). |  |  |
| EDCH (2) | Specifies that the user-defined channel is an enhanced dedicated channel (EDCH). |  |  |
| HSSICH (3) | Specifies that the user-defined channel is a shared information channel for high-speed downlink. |  |  |
| slotFormat | [in] | int32[] | This parameter specifies the spreading factor, the number of TFCI code words, the number of transmit power control bits, and the number of synchronization shift bits. Refer to the 3GPP TS 25.221 V11.0.0 standard for more information about slot format. The default value is 0. |
| modulationType | [in] | int32[] | This parameter specifies the modulation type of the corresponding channels.The default value is QPSK.Name (value)DescriptionQPSK (0)Specifies the QPSK modulation type is used.8PSK (1)Specifies the 8-PSK modulation type is used.16QAM (2)Specifies the 16-QAM modulation type is used. |
| Name (value) | Description |  |  |
| QPSK (0) | Specifies the QPSK modulation type is used. |  |  |
| 8PSK (1) | Specifies the 8-PSK modulation type is used. |  |  |
| 16QAM (2) | Specifies the 16-QAM modulation type is used. |  |  |
| channelizationCode | [in] | int32[] | This parameter specifies the channelization code assigned to the channel. The default value is 1. The valid values are 1 to 16. |
| numberOfElements | [in] | int32 | Specifies the number of elements in each array. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration_1ga294c94e8983cf9df018c471146f17838.html language=enus -->
## TOPIC 00161: RFmxTDSCDMA_CfgFrequencyReference

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration_1ga294c94e8983cf9df018c471146f17838.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration_1ga294c94e8983cf9df018c471146f17838.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the Reference Clock and the frequency reference source. Syntaxint32 __stdcall RFmxTDSCDMA_CfgFrequencyReference(niRFmxInstrHandle instrumentHandle, char channelName[], char frequencyReferenceSource[], float64 frequencyReferenceFrequency)RemarksThis function is a wrapper over the RFmx Inst

### RFmxTDSCDMA_CfgFrequencyReference

Configures the Reference Clock and the frequency reference source.

#### Syntax

int32 __stdcall RFmxTDSCDMA_CfgFrequencyReference(niRFmxInstrHandle instrumentHandle, char channelName[], char frequencyReferenceSource[], float64 frequencyReferenceFrequency)

#### Remarks

This function is a wrapper over the RFmx Instruments API, and calls the [RFmxInstr_CfgFrequencyReference](/csh?context=rfmxinstr_rfmxinstrcref_function_cfg_frequency_reference) function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxTDSCDMA_Initialize function. |
| channelName | [in] | char[] | Set this parameter to "" (empty string) or NULL. |
| frequencyReferenceSource | [in] | char[] | Specifies the frequency reference source.ValueDescriptionRFMXTDSCDMA_VAL_ONBOARD_CLOCK_STR ("Onboard Clock")PXIe-5663/5663E: The RFmx driver locks the PXIe-5663/5663E to the PXIe-5652 LO source onboard clock. Connect the REF OUT2 connector (if it exists) on the PXIe-5652 to the PXIe-5622 CLK IN terminal. On versions of the PXIe-5663/5663E that lack a REF OUT2 connector on the PXIe-5652, connect the REF IN/OUT connector on the PXIe-5652 to the PXIe-5622 CLK IN terminal.PXIe-5665: The RFmx driver locks the PXIe-5665 to the PXIe-5653 LO source onboard clock. Connect the 100 MHz REF OUT terminal on the PXIe-5653 to the PXIe-5622 CLK IN terminal.PXIe-5644R/5645R/5646R, PXIe-5840: The RFmx driver locks the device to its onboard clock.RFMXTDSCDMA_VAL_REF_IN_STR ("RefIn")PXIe-5663/5663E: Connect the external signal to the PXIe-5652 REF IN/OUT connector. Connect the REF OUT2 connector (if it exists) on the PXIe-5652 to the PXIe-5622 CLK IN terminal.PXIe-5665: Connect the external signal to the PXIe-5653 REF IN connector. Connect the 100 MHz REF OUT terminal on the PXIe-5653 to the PXIe-5622 CLK IN connector. If your external clock signal frequency is set to a frequency other than 10 MHz, set the frequencyReferenceFrequency parameter according to the frequency of your external clock signal.PXIe-5644R/5645R/5646R, PXIe-5840: The RFmx driver locks the device to the signal at the external REF IN connector.RFMXTDSCDMA_VAL_PXI_CLK_STR ("PXI_Clk")PXIe-5644R/5645R/5646R, PXIe-5663/5663E/5665, PXIe-5840: The RFmx driver locks the PXIe-5644R/5645R/5646R, PXIe-5663/5663E/5665 to the PXI backplane clock.RFMXTDSCDMA_VAL_CLK_IN_STR ("ClkIn")PXIe-5663/5663E: The RFmx driver locks the PXIe-5663/5663E to an external 10 MHz signal. Connect the external signal to the PXIe-5622 CLK IN connector, and connect the PXIe-5622 CLK OUT connector to the FREQ REF IN connector on the PXIe-5652.PXIe-5665: The RFmx driver locks the PXIe-5665 to an external 100 MHz signal. Connect the external signal to the PXIe-5622 CLK IN connector, and connect the PXIe-5622 CLK OUT connector to the REF IN connector on the PXIe-5653. Set the frequencyReferenceFrequency parameter to 100 MHz.PXIe-5644R/5645R/5646R, PXIe-5840: This configuration does not apply to the PXIe-5644R/5645R/5646R. |
| Value | Description |  |  |
| RFMXTDSCDMA_VAL_ONBOARD_CLOCK_STR ("Onboard Clock") | PXIe-5663/5663E: The RFmx driver locks the PXIe-5663/5663E to the PXIe-5652 LO source onboard clock. Connect the REF OUT2 connector (if it exists) on the PXIe-5652 to the PXIe-5622 CLK IN terminal. On versions of the PXIe-5663/5663E that lack a REF OUT2 connector on the PXIe-5652, connect the REF IN/OUT connector on the PXIe-5652 to the PXIe-5622 CLK IN terminal.PXIe-5665: The RFmx driver locks the PXIe-5665 to the PXIe-5653 LO source onboard clock. Connect the 100 MHz REF OUT terminal on the PXIe-5653 to the PXIe-5622 CLK IN terminal.PXIe-5644R/5645R/5646R, PXIe-5840: The RFmx driver locks the device to its onboard clock. |  |  |
| RFMXTDSCDMA_VAL_REF_IN_STR ("RefIn") | PXIe-5663/5663E: Connect the external signal to the PXIe-5652 REF IN/OUT connector. Connect the REF OUT2 connector (if it exists) on the PXIe-5652 to the PXIe-5622 CLK IN terminal.PXIe-5665: Connect the external signal to the PXIe-5653 REF IN connector. Connect the 100 MHz REF OUT terminal on the PXIe-5653 to the PXIe-5622 CLK IN connector. If your external clock signal frequency is set to a frequency other than 10 MHz, set the frequencyReferenceFrequency parameter according to the frequency of your external clock signal.PXIe-5644R/5645R/5646R, PXIe-5840: The RFmx driver locks the device to the signal at the external REF IN connector. |  |  |
| RFMXTDSCDMA_VAL_PXI_CLK_STR ("PXI_Clk") | PXIe-5644R/5645R/5646R, PXIe-5663/5663E/5665, PXIe-5840: The RFmx driver locks the PXIe-5644R/5645R/5646R, PXIe-5663/5663E/5665 to the PXI backplane clock. |  |  |
| RFMXTDSCDMA_VAL_CLK_IN_STR ("ClkIn") | PXIe-5663/5663E: The RFmx driver locks the PXIe-5663/5663E to an external 10 MHz signal. Connect the external signal to the PXIe-5622 CLK IN connector, and connect the PXIe-5622 CLK OUT connector to the FREQ REF IN connector on the PXIe-5652.PXIe-5665: The RFmx driver locks the PXIe-5665 to an external 100 MHz signal. Connect the external signal to the PXIe-5622 CLK IN connector, and connect the PXIe-5622 CLK OUT connector to the REF IN connector on the PXIe-5653. Set the frequencyReferenceFrequency parameter to 100 MHz.PXIe-5644R/5645R/5646R, PXIe-5840: This configuration does not apply to the PXIe-5644R/5645R/5646R. |  |  |
| frequencyReferenceFrequency | [in] | float64 | Specifies the Reference Clock rate, in Hz, when the frequencyReferenceSource parameter is set to RFMXTDSCDMA_VAL_CLK_IN_STR or RFMXTDSCDMA_VAL_REF_IN_STR. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration_1ga2a5a2fb7340b97ef31d94cea8596a3fc.html language=enus -->
## TOPIC 00162: RFmxTDSCDMA_CfgRF

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration_1ga2a5a2fb7340b97ef31d94cea8596a3fc.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration_1ga2a5a2fb7340b97ef31d94cea8596a3fc.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the RF attributes of the signal specified by the Selector String parameter. Syntaxint32 __stdcall RFmxTDSCDMA_CfgRF(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 centerFrequency, float64 referenceLevel, float64 externalAttenuation)ParametersNameDirectionTypeDescriptio

### RFmxTDSCDMA_CfgRF

Configures the RF attributes of the signal specified by the **Selector String** parameter.

#### Syntax

int32 __stdcall RFmxTDSCDMA_CfgRF(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 centerFrequency, float64 referenceLevel, float64 externalAttenuation)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Examples:"""signal::sig1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| centerFrequency | [in] | float64 | This parameter specifies the carrier frequency of the RF signal to acquire. The signal analyzer tunes to this frequency. This value is expressed in Hz. The default of this parameter is hardware dependent. |
| referenceLevel | [in] | float64 | This parameter specifies the reference level that represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices. The default of this parameter is hardware dependent. |
| externalAttenuation | [in] | float64 | This parameter specifies the level of external attenuation that is considered by the selected measurement. This value is expressed in dB. The default value is 0.For more information about attenuation, refer to the RF Attenuation and Signal Levels topic for your device in the NI RF Vector Signal Analyzers Help. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration_1ga320b342f8b24607daff768ff757afdc7.html language=enus -->
## TOPIC 00163: RFmxTDSCDMA_CfgRFAttenuation

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration_1ga320b342f8b24607daff768ff757afdc7.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration_1ga320b342f8b24607daff768ff757afdc7.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the nominal attenuation and the RFmx driver setting. Syntaxint32 __stdcall RFmxTDSCDMA_CfgRFAttenuation(niRFmxInstrHandle instrumentHandle, char channelName[], int32 rfAttenuationAuto, float64 rfAttenuationValue)RemarksThis function is a wrapper over the RFmx Instruments API, and calls th

### RFmxTDSCDMA_CfgRFAttenuation

Configures the nominal attenuation and the RFmx driver setting.

#### Syntax

int32 __stdcall RFmxTDSCDMA_CfgRFAttenuation(niRFmxInstrHandle instrumentHandle, char channelName[], int32 rfAttenuationAuto, float64 rfAttenuationValue)

#### Remarks

This function is a wrapper over the RFmx Instruments API, and calls the [RFmxInstr_CfgRFAttenuation](/csh?context=rfmxinstr_rfmxinstrcref_function_cfg_rf_attenuation) function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxTDSCDMA_Initialize function. |
| channelName | [in] | char[] | Set this parameter to "" (empty string) or NULL. |
| rfAttenuationAuto | [in] | int32 | Specifies whether the RFmx driver computes the RF attenuation.ValueDescriptionRFMXTDSCDMA_VAL_RF_ATTENUATION_AUTO_FALSE (0)Specifies that the RFmx driver uses the value configured using the rfAttenuationValue parameter.RFMXTDSCDMA_VAL_RF_ATTENUATION_AUTO_TRUE (1)Specifies that the RFmx driver computes the RF attenuation automatically. |
| Value | Description |  |  |
| RFMXTDSCDMA_VAL_RF_ATTENUATION_AUTO_FALSE (0) | Specifies that the RFmx driver uses the value configured using the rfAttenuationValue parameter. |  |  |
| RFMXTDSCDMA_VAL_RF_ATTENUATION_AUTO_TRUE (1) | Specifies that the RFmx driver computes the RF attenuation automatically. |  |  |
| rfAttenuationValue | [in] | float64 | Specifies the nominal attenuation setting, in dB, for all attenuators before the first mixer in the RF signal chain when the rfAttenuationAuto parameter is set to RFMXTDSCDMA_VAL_RF_ATTENUATION_AUTO_FALSE. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration_1ga32d81f58e8ae509153d9223f095e5522.html language=enus -->
## TOPIC 00164: RFmxTDSCDMA_AutoLevel

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration_1ga32d81f58e8ae509153d9223f095e5522.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration_1ga32d81f58e8ae509153d9223f095e5522.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Examines the input signal to calculate the peak power level and sets it as the value of the Reference Level attribute. Use this function to calculate an approximate setting for the reference level. Syntaxint32 __stdcall RFmxTDSCDMA_AutoLevel(niRFmxInstrHandle instrumentHandle, char selectorString[],

### RFmxTDSCDMA_AutoLevel

Examines the input signal to calculate the peak power level and sets it as the value of the Reference Level attribute. Use this function to calculate an approximate setting for the reference level.

#### Syntax

int32 __stdcall RFmxTDSCDMA_AutoLevel(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 measurementInterval, float64 *referenceLevel)

#### Remarks

1. Resets the mixer level, mixer level offset, and IF output power offset.
2. Sets the starting reference level to the maximum reference level supported by the device based on the current RF attenuation, mechanical attenuation, and preamplifier enabled settings.
3. Iterates to adjust the reference level based on the input signal peak power.
4. Uses immediate triggering and restores the trigger settings back to user setting after the execution.

You can also specify the starting reference level using the [RFMXTDSCDMA_ATTR_AUTO_LEVEL_INITIAL_REFERENCE_LEVEL](group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__advanced_1gad2db26d5e3d0a514deea8238c6df85a4.html) attribute.

When using NI 5663, 5665, or 5668R devices, NI recommends that you set an appropriate value for mechanical attenuation before calling the RFmxTDSCDMA Auto Level function. Setting an appropriate value for mechanical attenuation reduces the number of times the attenuator settings are changed by this function; thus reducing wear and tear, and maximizing the life time of the attenuator.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Examples:"""signal::sig1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| measurementInterval | [in] | float64 | This parameter specifies the acquisition length. This value is expressed in seconds. Use this value to calculate the number of samples to acquire from the signal analyzer. The default value is 5 ms.Auto Level function does not use any trigger for acquisition. It ignores the user-configured trigger attributes. NI recommends that you set a sufficiently high measurement interval to ensure that the acquired waveform is at least as long as one period of the signal. |
| referenceLevel | [out] | float64 * | This parameter returns the estimated peak power level of the input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration_1ga4a132140e505cfee4d7d4f61f162c688.html language=enus -->
## TOPIC 00165: RFmxTDSCDMA_CfgMidambleShift

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration_1ga4a132140e505cfee4d7d4f61f162c688.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration_1ga4a132140e505cfee4d7d4f61f162c688.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the Midamble Auto Detection Mode, Maximum Number of Users, and Midamble Shift parameters. Syntaxint32 __stdcall RFmxTDSCDMA_CfgMidambleShift(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 midambleAutoDetectionMode, int32 maximumNumberOfUsers, int32 midambleShift)Paramete

### RFmxTDSCDMA_CfgMidambleShift

Configures the **Midamble Auto Detection Mode**, **Maximum Number of Users**, and **Midamble Shift** parameters.

#### Syntax

int32 __stdcall RFmxTDSCDMA_CfgMidambleShift(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 midambleAutoDetectionMode, int32 maximumNumberOfUsers, int32 midambleShift)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Examples:"""signal::sig1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| midambleAutoDetectionMode | [in] | int32 | This parameter enables automatic midamble detection. The default value is Midamble Shift.Name (value)DescriptionOff (0)Automatic midamble detection is disabled.Midamble Shift (1)The midamble shift is automatically detected from K possible midamble shift values, where K is specified by the Maximum Number of Users parameter. The K possible midamble shift values are: Midamble Shift = k * floor(P/K),where P = 128, is the length of the basic midamble code, and k is an integer from 0 to K-1. |
| Name (value) | Description |  |  |
| Off (0) | Automatic midamble detection is disabled. |  |  |
| Midamble Shift (1) | The midamble shift is automatically detected from K possible midamble shift values, where K is specified by the Maximum Number of Users parameter. The K possible midamble shift values are: Midamble Shift = k * floor(P/K),where P = 128, is the length of the basic midamble code, and k is an integer from 0 to K-1. |  |  |
| maximumNumberOfUsers | [in] | int32 | This parameter configures the maximum number of users. The default value is 16.Name (value)Description2 (2)The maximum number of users are 2.4 (4)The maximum number of users are 4.6 (6)The maximum number of users are 6.8 (8)The maximum number of users are 8.10 (10)The maximum number of users are 10.12 (12)The maximum number of users are 12.14 (14)The maximum number of users are 14.16 (16)The maximum number of users are 16. |
| Name (value) | Description |  |  |
| 2 (2) | The maximum number of users are 2. |  |  |
| 4 (4) | The maximum number of users are 4. |  |  |
| 6 (6) | The maximum number of users are 6. |  |  |
| 8 (8) | The maximum number of users are 8. |  |  |
| 10 (10) | The maximum number of users are 10. |  |  |
| 12 (12) | The maximum number of users are 12. |  |  |
| 14 (14) | The maximum number of users are 14. |  |  |
| 16 (16) | The maximum number of users are 16. |  |  |
| midambleShift | [in] | int32 | This parameter specifies the midamble shift used when the Midamble Auto Detection Mode parameter is set to Off. This value is expressed in chips. The default value is 8. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration_1ga7848cd8c616073f8b98b539c66a4b297.html language=enus -->
## TOPIC 00166: RFmxTDSCDMA_CfgChannelConfigurationMode

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration_1ga7848cd8c616073f8b98b539c66a4b297.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration_1ga7848cd8c616073f8b98b539c66a4b297.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures RFmx TD-SCDMA to detect the channels automatically or to use a specified channel configuration. Syntaxint32 __stdcall RFmxTDSCDMA_CfgChannelConfigurationMode(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 channelConfigurationMode)ParametersNameDirectionTypeDescriptionins

### RFmxTDSCDMA_CfgChannelConfigurationMode

Configures RFmx TD-SCDMA to detect the channels automatically or to use a specified channel configuration.

#### Syntax

int32 __stdcall RFmxTDSCDMA_CfgChannelConfigurationMode(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 channelConfigurationMode)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Examples:"""signal::sig1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| channelConfigurationMode | [in] | int32 | This parameter specifies whether to detect the channels automatically or to use a specified channel configuration. The default value is Auto Detect.Name (value)DescriptionAuto Detect (0)RFmx TD-SCDMA detects the channels automatically.User Defined (1)The channel configuration is defined manually. This mode increases measurement speed because no time is spent on channel detection. |
| Name (value) | Description |  |  |
| Auto Detect (0) | RFmx TD-SCDMA detects the channels automatically. |  |  |
| User Defined (1) | The channel configuration is defined manually. This mode increases measurement speed because no time is spent on channel detection. |  |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration_1ga9c21dc143015b0c16b327ae4727efaa9.html language=enus -->
## TOPIC 00167: RFmxTDSCDMA_CfgMechanicalAttenuation

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration_1ga9c21dc143015b0c16b327ae4727efaa9.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration_1ga9c21dc143015b0c16b327ae4727efaa9.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the mechanical attenuation and the RFmx driver attenuation hardware settings. Syntaxint32 __stdcall RFmxTDSCDMA_CfgMechanicalAttenuation(niRFmxInstrHandle instrumentHandle, char channelName[], int32 mechanicalAttenuationAuto, float64 mechanicalAttenuationValue)RemarksThis function is a wr

### RFmxTDSCDMA_CfgMechanicalAttenuation

Configures the mechanical attenuation and the RFmx driver attenuation hardware settings.

#### Syntax

int32 __stdcall RFmxTDSCDMA_CfgMechanicalAttenuation(niRFmxInstrHandle instrumentHandle, char channelName[], int32 mechanicalAttenuationAuto, float64 mechanicalAttenuationValue)

#### Remarks

This function is a wrapper over the RFmx Instruments API, and calls the [RFmxInstr_CfgMechanicalAttenuation](/csh?context=rfmxinstr_rfmxinstrcref_function_cfg_mechanical_attenuation) function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxTDSCDMA_Initialize function. |
| channelName | [in] | char[] | Set this parameter to "" (empty string) or NULL. |
| mechanicalAttenuationAuto | [in] | int32 | Specifies whether the RFmx driver automatically chooses an attenuation setting based on the hardware settings.ValueDescriptionRFMXTDSCDMA_VAL_MECHANICAL_ATTENUATION_AUTO_FALSE (0)Specifies that the RFmx driver uses the value configured in the mechanicalAttenuationValue parameter.RFMXTDSCDMA_VAL_MECHANICAL_ATTENUATION_AUTO_TRUE (1)Specifies that the measurement computes the mechanical attenuation. |
| Value | Description |  |  |
| RFMXTDSCDMA_VAL_MECHANICAL_ATTENUATION_AUTO_FALSE (0) | Specifies that the RFmx driver uses the value configured in the mechanicalAttenuationValue parameter. |  |  |
| RFMXTDSCDMA_VAL_MECHANICAL_ATTENUATION_AUTO_TRUE (1) | Specifies that the measurement computes the mechanical attenuation. |  |  |
| mechanicalAttenuationValue | [in] | float64 | Specifies the level of mechanical attenuation, in dB, for the RF path when the mechanicalAttenuationAuto is set to RFMXTDSCDMA_VAL_MECHANICAL_ATTENUATION_AUTO_FALSE. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration_1gab66d0843e7b8c921295ec6733b9bccb6.html language=enus -->
## TOPIC 00168: RFmxTDSCDMA_CfgExternalAttenuation

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration_1gab66d0843e7b8c921295ec6733b9bccb6.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration_1gab66d0843e7b8c921295ec6733b9bccb6.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies external attenuation to be considered by RFmx TD-SCDMA measurements, such as the attenuation of a switch or cable connected to the signal analyzer RF IN connector. Syntaxint32 __stdcall RFmxTDSCDMA_CfgExternalAttenuation(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 ex

### RFmxTDSCDMA_CfgExternalAttenuation

Specifies external attenuation to be considered by RFmx TD-SCDMA measurements, such as the attenuation of a switch or cable connected to the signal analyzer RF IN connector.

#### Syntax

int32 __stdcall RFmxTDSCDMA_CfgExternalAttenuation(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 externalAttenuation)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Examples:"""signal::sig1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| externalAttenuation | [in] | float64 | This parameter specifies the level of external attenuation that is considered by the selected measurement. This value is expressed in dB. The default value is 0.For more information about attenuation, refer to the RF Attenuation and Signal Levels topic for your device in the NI RF Vector Signal Analyzers Help. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration_1gac1b10cffd82f7bbd6bb8456d74698687.html language=enus -->
## TOPIC 00169: RFmxTDSCDMA_CfgUplinkScramblingCode

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration_1gac1b10cffd82f7bbd6bb8456d74698687.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration_1gac1b10cffd82f7bbd6bb8456d74698687.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the scrambling code used for the uplink transmission. Syntaxint32 __stdcall RFmxTDSCDMA_CfgUplinkScramblingCode(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 uplinkScramblingCode)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter s

### RFmxTDSCDMA_CfgUplinkScramblingCode

Configures the scrambling code used for the uplink transmission.

#### Syntax

int32 __stdcall RFmxTDSCDMA_CfgUplinkScramblingCode(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 uplinkScramblingCode)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Examples:"""signal::sig1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| uplinkScramblingCode | [in] | int32 | This parameter specifies the scrambling code and the basic midamble code for uplink transmission. The default value is 0. The valid range is 0 to 127.The code group of the parameter should match the code group of the RFMXTDSCDMA_ATTR_PILOT_CODE attribute. For more information on code allocations, refer to the Code Allocation in Section 8.3 of 3GPP TS 25.223, v.11.0.0 Release 11.Code Group = floor (UL Scrambling Code / 4) |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration_1gae646fa5c0afc8439f44c32a369d7704a.html language=enus -->
## TOPIC 00170: RFmxTDSCDMA_CfgUserDefinedChannel

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration_1gae646fa5c0afc8439f44c32a369d7704a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration_1gae646fa5c0afc8439f44c32a369d7704a.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures an individual user-defined channel when the channel configuration mode is set to User Defined. Syntaxint32 __stdcall RFmxTDSCDMA_CfgUserDefinedChannel(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 slotIndex, int32 channelType, int32 slotFormat, int32 modulationType, int

### RFmxTDSCDMA_CfgUserDefinedChannel

Configures an individual user-defined channel when the channel configuration mode is set to **User Defined**.

#### Syntax

int32 __stdcall RFmxTDSCDMA_CfgUserDefinedChannel(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 slotIndex, int32 channelType, int32 slotFormat, int32 modulationType, int32 channelizationCode)

#### Remarks

Use "channel<n>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure this function.

A channel configuration is defined by the slot index it refers to, the channel type, and the modulation type.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and channel number. If you do not specify the signal name, the default signal instance is used. The default value is "channel0".Examples:"channel0""signal::sig1/channel0"You can use the RFmxTDSCDMA_BuildChannelString function to build the selector string. |
| slotIndex | [in] | int32 | This parameter specifies the index of a slot after the start of the acquisition. The default value is 0. |
| channelType | [in] | int32 | This parameter specifies the TD-SCDMA channel type. The default value is Idle.Name (value)DescriptionIdle (0)Specifies that the user-defined channel type is an empty slot.DPCH (1)Specifies that the user-defined channel is DPCH.EDCH (2)Specifies that the user-defined channel is EDCH.HSSICH (3)Specifies that the user-defined channel is HSSICH. |
| Name (value) | Description |  |  |
| Idle (0) | Specifies that the user-defined channel type is an empty slot. |  |  |
| DPCH (1) | Specifies that the user-defined channel is DPCH. |  |  |
| EDCH (2) | Specifies that the user-defined channel is EDCH. |  |  |
| HSSICH (3) | Specifies that the user-defined channel is HSSICH. |  |  |
| slotFormat | [in] | int32 | This parameter specifies the spreading factor, the number of TFCI code words, the number of transmit power control bits, and the number of synchronization shift bits. Refer to the 3GPP TS 25.221 V11.0.0 standard for more information about slot format. The default value is 0. |
| modulationType | [in] | int32 | This parameter specifies the modulation type of the corresponding channels. The default value is QPSK.Name (value)DescriptionQPSK (0)Specifies the QPSK modulation type is used.8PSK (1)Specifies the 8-PSK modulation type is used.16QAM (2)Specifies the 16-QAM modulation type is used. |
| Name (value) | Description |  |  |
| QPSK (0) | Specifies the QPSK modulation type is used. |  |  |
| 8PSK (1) | Specifies the 8-PSK modulation type is used. |  |  |
| 16QAM (2) | Specifies the 16-QAM modulation type is used. |  |  |
| channelizationCode | [in] | int32 | This parameter specifies the channelization code assigned to the channel. The default value is 1. The valid values are 1 to 16. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration_1gae9c95450fc79e4134999dc1260939a67.html language=enus -->
## TOPIC 00171: RFmxTDSCDMA_SendSoftwareEdgeTrigger

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration_1gae9c95450fc79e4134999dc1260939a67.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration_1gae9c95450fc79e4134999dc1260939a67.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sends a trigger to the device when you use the RFmxTDSCDMA Configure Trigger function to choose a software version of a trigger and the device is waiting for the trigger to be sent. You can also use this function to override a hardware trigger. Syntaxint32 __stdcall RFmxTDSCDMA_SendSoftwareEdgeTrigg

### RFmxTDSCDMA_SendSoftwareEdgeTrigger

Sends a trigger to the device when you use the RFmxTDSCDMA Configure Trigger function to choose a software version of a trigger and the device is waiting for the trigger to be sent. You can also use this function to override a hardware trigger.

#### Syntax

int32 __stdcall RFmxTDSCDMA_SendSoftwareEdgeTrigger(niRFmxInstrHandle instrumentHandle)

#### Remarks

- You configure an invalid trigger.
- You have not previously called the [RFmxTDSCDMA_Initiate](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1gaa56fe53b840183812166224dfb1bd11f.html) function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration__acp.html language=enus -->
## TOPIC 00172: ACP

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration__acp.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration__acp.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxTDSCDMA_ACPCfgAveragingConfigures averaging for the ACP measurement. RFmxTDSCDMA_ACPCfgMeasurementMethodConfigures the method for performing the ACP measurement. RFmxTDSCDMA_ACPCfgNoiseCompensationEnabledConfigures channel power compensation for the inherent

### ACP

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxTDSCDMA_ACPCfgAveraging | Configures averaging for the ACP measurement. |
| RFmxTDSCDMA_ACPCfgMeasurementMethod | Configures the method for performing the ACP measurement. |
| RFmxTDSCDMA_ACPCfgNoiseCompensationEnabled | Configures channel power compensation for the inherent noise floor of the signal analyzer. |
| RFmxTDSCDMA_ACPCfgNumberOfOffsets | Configures the number of offsets for the ACP measurement. |
| RFmxTDSCDMA_ACPCfgRBWFilter | Configures the RBW filter. |
| RFmxTDSCDMA_ACPCfgSweepTime | Configures the sweep time. |

#### Attachments

None

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration__acp_1ga384bba89c2bd6d8ed3d5aa0f209265b0.html language=enus -->
## TOPIC 00173: RFmxTDSCDMA_ACPCfgNumberOfOffsets

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration__acp_1ga384bba89c2bd6d8ed3d5aa0f209265b0.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration__acp_1ga384bba89c2bd6d8ed3d5aa0f209265b0.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the number of offsets for the ACP measurement. Syntaxint32 __stdcall RFmxTDSCDMA_ACPCfgNumberOfOffsets(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 numberOfOffsets)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifies the R

### RFmxTDSCDMA_ACPCfgNumberOfOffsets

Configures the number of offsets for the ACP measurement.

#### Syntax

int32 __stdcall RFmxTDSCDMA_ACPCfgNumberOfOffsets(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 numberOfOffsets)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Examples:"""signal::sig1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| numberOfOffsets | [in] | int32 | This parameter specifies the number of offset channels. The default value is 2. Valid values are constrained by the bandwidth of the signal analyzer. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ACP

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration__acp_1ga4ab942a5d31564a8890481e2cd9a1aa7.html language=enus -->
## TOPIC 00174: RFmxTDSCDMA_ACPCfgNoiseCompensationEnabled

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration__acp_1ga4ab942a5d31564a8890481e2cd9a1aa7.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration__acp_1ga4ab942a5d31564a8890481e2cd9a1aa7.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures channel power compensation for the inherent noise floor of the signal analyzer. Syntaxint32 __stdcall RFmxTDSCDMA_ACPCfgNoiseCompensationEnabled(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 noiseCompensationEnabled)ParametersNameDirectionTypeDescriptioninstrumentHandle

### RFmxTDSCDMA_ACPCfgNoiseCompensationEnabled

Configures channel power compensation for the inherent noise floor of the signal analyzer.

#### Syntax

int32 __stdcall RFmxTDSCDMA_ACPCfgNoiseCompensationEnabled(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 noiseCompensationEnabled)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Examples:"""signal::sig1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| noiseCompensationEnabled | [in] | int32 | This parameter enables the channel powers to compensate for the inherent noise floor of the signal analyzer. The default value is False.Name (value)DescriptionFalse (0)Disables compensation of the channel powers for the signal analyzer noise floor.True (1)Enables compensation of the channel powers for the signal analyzer noise floor. The noise floor of the signal analyzer is measured for the RF path used by the ACP measurement and cached for future use. If signal analyzer or measurement parameters change, noise floors are remeasured. Supported Devices: PXIe-5663/5665/5668R/5830/5831/5832/5842/5860 |
| Name (value) | Description |  |  |
| False (0) | Disables compensation of the channel powers for the signal analyzer noise floor. |  |  |
| True (1) | Enables compensation of the channel powers for the signal analyzer noise floor. The noise floor of the signal analyzer is measured for the RF path used by the ACP measurement and cached for future use. If signal analyzer or measurement parameters change, noise floors are remeasured. Supported Devices: PXIe-5663/5665/5668R/5830/5831/5832/5842/5860 |  |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ACP

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration__acp_1gaa712d94fd624d20f9d18f2b72a5d3714.html language=enus -->
## TOPIC 00175: RFmxTDSCDMA_ACPCfgMeasurementMethod

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration__acp_1gaa712d94fd624d20f9d18f2b72a5d3714.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration__acp_1gaa712d94fd624d20f9d18f2b72a5d3714.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the method for performing the ACP measurement. Syntaxint32 __stdcall RFmxTDSCDMA_ACPCfgMeasurementMethod(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 measurementMethod)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifies t

### RFmxTDSCDMA_ACPCfgMeasurementMethod

Configures the method for performing the ACP measurement.

#### Syntax

int32 __stdcall RFmxTDSCDMA_ACPCfgMeasurementMethod(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 measurementMethod)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Examples:"""signal::sig1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| measurementMethod | [in] | int32 | This parameter specifies the method for performing the ACP measurement. The default value is Normal.Normal (0)The ACP measurement acquires the spectrum using the same signal analyzer setting across frequency bands. Use this method when measurement speed is desirable over higher dynamic range.Dynamic Range (1)The ACP measurement acquires the spectrum using the hardware-specific optimizations for different frequency bands. Use this method to get the best dynamic range. Supported Devices: PXIe-5665/5668R.Sequential FFT (2)The ACP measurement acquires I/Q samples for a duration specified by the RFMXTDSCDMA_ATTR_ACP_SWEEP_TIME_INTERVAL attribute. These samples are divided into smaller chunks. The size of these chunks is defined by the RFMXTDSCDMA_ATTR_ACP_SEQUENTIAL_FFT_SIZE attribute, and FFT is computed on each of these chunks. The resultant FFTs are averaged to get the spectrum and is used to compute ACP. If the total acquired samples is not an integer multiple of the FFT size, the remaining samples at the end of acquisition are not used for the measurement. Use this method to optimize ACP measurement speed. Accuracy of the results may be reduced when using this measurement method.For accurate power measurements, when the power characteristics of the signal vary over time, Averaging is allowed.The following attributes have limited support when you set the ACP Meas Method attribute to Sequential FFT.PropertySupported ValueRFMXTDSCDMA_ATTR_ACP_RBW_FILTER_AUTO_BANDWIDTHTrueRFMXTDSCDMA_ATTR_ACP_RBW_FILTER_TYPEFFT BasedRFMXTDSCDMA_ATTR_ACP_AVERAGING_COUNT>=1RFMXTDSCDMA_ATTR_ACP_NOISE_COMPENSATION_ENABLEDFalseRFMXTDSCDMA_ATTR_ACP_NUMBER_OF_ANALYSIS_THREADS>=1Note For multi-span FFT, the averaging count should be 1. |
| Normal (0) | The ACP measurement acquires the spectrum using the same signal analyzer setting across frequency bands. Use this method when measurement speed is desirable over higher dynamic range. |  |  |
| Dynamic Range (1) | The ACP measurement acquires the spectrum using the hardware-specific optimizations for different frequency bands. Use this method to get the best dynamic range. Supported Devices: PXIe-5665/5668R. |  |  |
| Sequential FFT (2) | The ACP measurement acquires I/Q samples for a duration specified by the RFMXTDSCDMA_ATTR_ACP_SWEEP_TIME_INTERVAL attribute. These samples are divided into smaller chunks. The size of these chunks is defined by the RFMXTDSCDMA_ATTR_ACP_SEQUENTIAL_FFT_SIZE attribute, and FFT is computed on each of these chunks. The resultant FFTs are averaged to get the spectrum and is used to compute ACP. If the total acquired samples is not an integer multiple of the FFT size, the remaining samples at the end of acquisition are not used for the measurement. Use this method to optimize ACP measurement speed. Accuracy of the results may be reduced when using this measurement method.For accurate power measurements, when the power characteristics of the signal vary over time, Averaging is allowed.The following attributes have limited support when you set the ACP Meas Method attribute to Sequential FFT.PropertySupported ValueRFMXTDSCDMA_ATTR_ACP_RBW_FILTER_AUTO_BANDWIDTHTrueRFMXTDSCDMA_ATTR_ACP_RBW_FILTER_TYPEFFT BasedRFMXTDSCDMA_ATTR_ACP_AVERAGING_COUNT>=1RFMXTDSCDMA_ATTR_ACP_NOISE_COMPENSATION_ENABLEDFalseRFMXTDSCDMA_ATTR_ACP_NUMBER_OF_ANALYSIS_THREADS>=1Note For multi-span FFT, the averaging count should be 1. |  |  |
| Property | Supported Value |  |  |
| RFMXTDSCDMA_ATTR_ACP_RBW_FILTER_AUTO_BANDWIDTH | True |  |  |
| RFMXTDSCDMA_ATTR_ACP_RBW_FILTER_TYPE | FFT Based |  |  |
| RFMXTDSCDMA_ATTR_ACP_AVERAGING_COUNT | >=1 |  |  |
| RFMXTDSCDMA_ATTR_ACP_NOISE_COMPENSATION_ENABLED | False |  |  |
| RFMXTDSCDMA_ATTR_ACP_NUMBER_OF_ANALYSIS_THREADS | >=1 |  |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ACP

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration__acp_1gac8330be2569e97babc2e8aed63247a6d.html language=enus -->
## TOPIC 00176: RFmxTDSCDMA_ACPCfgAveraging

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration__acp_1gac8330be2569e97babc2e8aed63247a6d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration__acp_1gac8330be2569e97babc2e8aed63247a6d.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures averaging for the ACP measurement. Syntaxint32 __stdcall RFmxTDSCDMA_ACPCfgAveraging(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 averagingEnabled, int32 averagingCount, int32 averagingType)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis

### RFmxTDSCDMA_ACPCfgAveraging

Configures averaging for the ACP measurement.

#### Syntax

int32 __stdcall RFmxTDSCDMA_ACPCfgAveraging(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 averagingEnabled, int32 averagingCount, int32 averagingType)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Examples:"""signal::sig1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| averagingEnabled | [in] | int32 | This parameter enables averaging for spectrum measurements. The default value is False.Name (value)DescriptionFalse (0)The measurement is performed on a single acquisition.True (1)The ACP measurement uses the value of the RFMXTDSCDMA_ATTR_ACP_AVERAGING_COUNT attribute as the number of acquisitions over which the ACP measurement is averaged. |
| Name (value) | Description |  |  |
| False (0) | The measurement is performed on a single acquisition. |  |  |
| True (1) | The ACP measurement uses the value of the RFMXTDSCDMA_ATTR_ACP_AVERAGING_COUNT attribute as the number of acquisitions over which the ACP measurement is averaged. |  |  |
| averagingCount | [in] | int32 | This parameter specifies the number of acquisitions used for averaging when you set the Averaging Enabled parameter to True. The default value is 10. |
| averagingType | [in] | int32 | This parameter specifies the averaging type for averaging multiple spectrum acquisitions. RFmx uses the averaged spectrum for the measurement.The default value is RMS.Name (value)DescriptionRMS (0)The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor.Log (1)The power spectrum is averaged in a logarithmic scale.Scalar (2)The square root of the power spectrum is averaged.Max (3)The peak power in the spectrum at each frequency bin is retained from one acquisition to the next.Min (4)The lowest power in the spectrum at each frequency bin is retained from one acquisition to the next.Refer to the Averaging section of the Spectrum topic for more information about averaging types. |
| Name (value) | Description |  |  |
| RMS (0) | The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. |  |  |
| Log (1) | The power spectrum is averaged in a logarithmic scale. |  |  |
| Scalar (2) | The square root of the power spectrum is averaged. |  |  |
| Max (3) | The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. |  |  |
| Min (4) | The lowest power in the spectrum at each frequency bin is retained from one acquisition to the next. |  |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ACP

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration__acp_1gadcf37fd6efd616e8c2c058c9040cde57.html language=enus -->
## TOPIC 00177: RFmxTDSCDMA_ACPCfgRBWFilter

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration__acp_1gadcf37fd6efd616e8c2c058c9040cde57.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration__acp_1gadcf37fd6efd616e8c2c058c9040cde57.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the RBW filter. Syntaxint32 __stdcall RFmxTDSCDMA_ACPCfgRBWFilter(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 rbwAuto, float64 rbw, int32 rbwFilterType)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifies the RFmx session

### RFmxTDSCDMA_ACPCfgRBWFilter

Configures the RBW filter.

#### Syntax

int32 __stdcall RFmxTDSCDMA_ACPCfgRBWFilter(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 rbwAuto, float64 rbw, int32 rbwFilterType)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Examples:"""signal::sig1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| rbwAuto | [in] | int32 | This parameter specifies whether the measurement computes the RBW. The default value is True.Name (value)DescriptionFalse (0)The measurement uses the RBW that you specify in the RFMXTDSCDMA_ATTR_ACP_RBW_FILTER_AUTO_BANDWIDTH attribute.True (1)The measurement calculates the RBW.Refer to the RBW and Sweep Time section in the ACP topic for more information about RBW and sweep time. |
| Name (value) | Description |  |  |
| False (0) | The measurement uses the RBW that you specify in the RFMXTDSCDMA_ATTR_ACP_RBW_FILTER_AUTO_BANDWIDTH attribute. |  |  |
| True (1) | The measurement calculates the RBW. |  |  |
| rbw | [in] | float64 | This parameter specifies the bandwidth of the RBW filter used to sweep the acquired signal when you set the RBW Auto parameter to False. This value is expressed in Hz. The default value is 5.636 kHz. |
| rbwFilterType | [in] | int32 | This parameter specifies the shape of the digital RBW filter. The default value is FFT Based.Name (value)DescriptionFFT Based (0)An RBW filter with a fast Fourier transform (FFT)-based response is applied.Gaussian (1)An RBW filter with a Gaussian response is applied.Flat (2)An RBW filter with a flat response is applied. |
| Name (value) | Description |  |  |
| FFT Based (0) | An RBW filter with a fast Fourier transform (FFT)-based response is applied. |  |  |
| Gaussian (1) | An RBW filter with a Gaussian response is applied. |  |  |
| Flat (2) | An RBW filter with a flat response is applied. |  |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ACP

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration__acp_1gae53d28d88c3b0e6ee4c8b9f413ebbec6.html language=enus -->
## TOPIC 00178: RFmxTDSCDMA_ACPCfgSweepTime

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration__acp_1gae53d28d88c3b0e6ee4c8b9f413ebbec6.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration__acp_1gae53d28d88c3b0e6ee4c8b9f413ebbec6.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the sweep time. Syntaxint32 __stdcall RFmxTDSCDMA_ACPCfgSweepTime(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 sweepTimeAuto, float64 sweepTimeInterval)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifies the RFmx session

### RFmxTDSCDMA_ACPCfgSweepTime

Configures the sweep time.

#### Syntax

int32 __stdcall RFmxTDSCDMA_ACPCfgSweepTime(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 sweepTimeAuto, float64 sweepTimeInterval)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Examples:"""signal::sig1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| sweepTimeAuto | [in] | int32 | This parameter specifies whether the measurement computes the sweep time. The default value is True.Name (value)DescriptionFalse (0)The measurement uses the sweep time that you specify using the Sweep Time Interval parameter.True (1)The measurement uses the default sweep time of .00066 seconds (s).Refer to the RBW and Sweep Time section in the ACP topic for more details on RBW and sweep time. |
| Name (value) | Description |  |  |
| False (0) | The measurement uses the sweep time that you specify using the Sweep Time Interval parameter. |  |  |
| True (1) | The measurement uses the default sweep time of .00066 seconds (s). |  |  |
| sweepTimeInterval | [in] | float64 | This parameter specifies the sweep time when you set the Sweep Time Auto parameter to False. This value is expressed in seconds. The default value is 0.00066 s. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ACP

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration__cda.html language=enus -->
## TOPIC 00179: CDA

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration__cda.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration__cda.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxTDSCDMA_CDACfgAveragingConfigures averaging for the CDA measurement. RFmxTDSCDMA_CDACfgMeasurementChannelConfigures the physical channel to be analyzed using the Spreading Factor parameter and the Channelization Code parameter. RFmxTDSCDMA_CDACfgPowerUnitCon

### CDA

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxTDSCDMA_CDACfgAveraging | Configures averaging for the CDA measurement. |
| RFmxTDSCDMA_CDACfgMeasurementChannel | Configures the physical channel to be analyzed using the Spreading Factor parameter and the Channelization Code parameter. |
| RFmxTDSCDMA_CDACfgPowerUnit | Configures the unit of measurement for the measurement results. |
| RFmxTDSCDMA_CDACfgSynchronizationModeAndOffset | Configures the synchronization mode and the measurement offset for the code domain analysis (CDA) measurement. You can select a specific time slot for the measurement using this function. |

#### Attachments

None

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration__cda_1ga55d93ce6f5224f0b4197c3c888d1852c.html language=enus -->
## TOPIC 00180: RFmxTDSCDMA_CDACfgPowerUnit

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration__cda_1ga55d93ce6f5224f0b4197c3c888d1852c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration__cda_1ga55d93ce6f5224f0b4197c3c888d1852c.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the unit of measurement for the measurement results. Syntaxint32 __stdcall RFmxTDSCDMA_CDACfgPowerUnit(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 powerUnit)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifies the RFmx se

### RFmxTDSCDMA_CDACfgPowerUnit

Configures the unit of measurement for the measurement results.

#### Syntax

int32 __stdcall RFmxTDSCDMA_CDACfgPowerUnit(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 powerUnit)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Examples:"""signal::sig1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| powerUnit | [in] | int32 | This parameter specifies the measurement unit of the measured code domain power results. The default value is dB.Name (value)DescriptiondB (0)The measurement unit for code domain power results is dB.dBm (1)The measurement unit for code domain power results is dBm. |
| Name (value) | Description |  |  |
| dB (0) | The measurement unit for code domain power results is dB. |  |  |
| dBm (1) | The measurement unit for code domain power results is dBm. |  |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

CDA

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration__cda_1ga5f5109734a6fee01351e7a63ec1fabc3.html language=enus -->
## TOPIC 00181: RFmxTDSCDMA_CDACfgMeasurementChannel

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration__cda_1ga5f5109734a6fee01351e7a63ec1fabc3.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration__cda_1ga5f5109734a6fee01351e7a63ec1fabc3.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the physical channel to be analyzed using the Spreading Factor parameter and the Channelization Code parameter. Syntaxint32 __stdcall RFmxTDSCDMA_CDACfgMeasurementChannel(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 spreadingFactor, int32 channelizationCode)ParametersN

### RFmxTDSCDMA_CDACfgMeasurementChannel

Configures the physical channel to be analyzed using the **Spreading Factor** parameter and the **Channelization Code** parameter.

#### Syntax

int32 __stdcall RFmxTDSCDMA_CDACfgMeasurementChannel(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 spreadingFactor, int32 channelizationCode)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Examples:"""signal::sig1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| spreadingFactor | [in] | int32 | This parameter specifies the base spreading factor for code domain power (CDP) analysis. The default value is 16. |
| channelizationCode | [in] | int32 | This parameter specifies the channelization code of the code domain analysis (CDA) measurement channel. The default value is 1. The valid values are 1 to 16. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

CDA

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration__cda_1gaa1f13d7a303749155fc227c1189c598a.html language=enus -->
## TOPIC 00182: RFmxTDSCDMA_CDACfgSynchronizationModeAndOffset

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration__cda_1gaa1f13d7a303749155fc227c1189c598a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration__cda_1gaa1f13d7a303749155fc227c1189c598a.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the synchronization mode and the measurement offset for the code domain analysis (CDA) measurement. You can select a specific time slot for the measurement using this function. Syntaxint32 __stdcall RFmxTDSCDMA_CDACfgSynchronizationModeAndOffset(niRFmxInstrHandle instrumentHandle, char se

### RFmxTDSCDMA_CDACfgSynchronizationModeAndOffset

Configures the synchronization mode and the measurement offset for the code domain analysis (CDA) measurement. You can select a specific time slot for the measurement using this function.

#### Syntax

int32 __stdcall RFmxTDSCDMA_CDACfgSynchronizationModeAndOffset(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 synchronizationMode, int32 measurementOffset)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Examples:"""signal::sig1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| synchronizationMode | [in] | int32 | This parameter specifies the synchronization mode for the CDA measurement. Currently, only the Slot mode is supported.Name (value)DescriptionSlot (0)The measurement uses slot synchronization mode. The slot boundary in the acquired signal is detected, and the measurement is performed over one slot, starting from the boundary specified by the RFMXTDSCDMA_ATTR_MODACC_MEASUREMENT_OFFSET attribute. |
| Name (value) | Description |  |  |
| Slot (0) | The measurement uses slot synchronization mode. The slot boundary in the acquired signal is detected, and the measurement is performed over one slot, starting from the boundary specified by the RFMXTDSCDMA_ATTR_MODACC_MEASUREMENT_OFFSET attribute. |  |  |
| measurementOffset | [in] | int32 | This parameter specifies the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the Synchronization Mode parameter. The default value is 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

CDA

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration__cda_1gaa329f1ae3482b334d814ae5c8455e741.html language=enus -->
## TOPIC 00183: RFmxTDSCDMA_CDACfgAveraging

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration__cda_1gaa329f1ae3482b334d814ae5c8455e741.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration__cda_1gaa329f1ae3482b334d814ae5c8455e741.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures averaging for the CDA measurement. Syntaxint32 __stdcall RFmxTDSCDMA_CDACfgAveraging(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 averagingEnabled, int32 averagingCount)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifies

### RFmxTDSCDMA_CDACfgAveraging

Configures averaging for the CDA measurement.

#### Syntax

int32 __stdcall RFmxTDSCDMA_CDACfgAveraging(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 averagingEnabled, int32 averagingCount)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Examples:"""signal::sig1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| averagingEnabled | [in] | int32 | This parameter specifies whether to enable averaging for the CDA measurement. The default value is False.Name (value)DescriptionFalse (0)The measurement is performed on a single acquisition.True (1)The CDA measurement uses the value of the Averaging Count parameter as the number of acquisitions over which the CDA measurement is averaged. |
| Name (value) | Description |  |  |
| False (0) | The measurement is performed on a single acquisition. |  |  |
| True (1) | The CDA measurement uses the value of the Averaging Count parameter as the number of acquisitions over which the CDA measurement is averaged. |  |  |
| averagingCount | [in] | int32 | This parameter specifies the number of acquisitions used for averaging when you set the Averaging Enabled parameter to True. The default value is 10. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

CDA

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration__chp.html language=enus -->
## TOPIC 00184: CHP

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration__chp.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration__chp.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxTDSCDMA_CHPCfgAveragingConfigures averaging for the CHP measurement. RFmxTDSCDMA_CHPCfgRBWFilterConfigures the RBW filter. RFmxTDSCDMA_CHPCfgSweepTimeConfigures the sweep time. AttachmentsNone

### CHP

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxTDSCDMA_CHPCfgAveraging | Configures averaging for the CHP measurement. |
| RFmxTDSCDMA_CHPCfgRBWFilter | Configures the RBW filter. |
| RFmxTDSCDMA_CHPCfgSweepTime | Configures the sweep time. |

#### Attachments

None

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration__chp_1gabebf42ec4fc76d50f2c400685476ece3.html language=enus -->
## TOPIC 00185: RFmxTDSCDMA_CHPCfgRBWFilter

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration__chp_1gabebf42ec4fc76d50f2c400685476ece3.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration__chp_1gabebf42ec4fc76d50f2c400685476ece3.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the RBW filter. Syntaxint32 __stdcall RFmxTDSCDMA_CHPCfgRBWFilter(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 rbwAuto, float64 rbw, int32 rbwFilterType)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifies the RFmx session

### RFmxTDSCDMA_CHPCfgRBWFilter

Configures the RBW filter.

#### Syntax

int32 __stdcall RFmxTDSCDMA_CHPCfgRBWFilter(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 rbwAuto, float64 rbw, int32 rbwFilterType)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Examples:"""signal::sig1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| rbwAuto | [in] | int32 | This parameter specifies whether the measurement computes the RBW. The default value is True.Name (value)DescriptionFalse (0)The measurement uses the RBW you specify.True (1)RFmx TD-SCDMA automatically calculates the RBW.Refer to the RBW and Sweep Time section in the CHP topic for more information about RBW and sweep time. |
| Name (value) | Description |  |  |
| False (0) | The measurement uses the RBW you specify. |  |  |
| True (1) | RFmx TD-SCDMA automatically calculates the RBW. |  |  |
| rbw | [in] | float64 | This parameter specifies the bandwidth of the RBW filter used to sweep the acquired signal when you set the RBW Auto parameter to False. This value is expressed in Hz. The default value is 5.636 kHz. |
| rbwFilterType | [in] | int32 | This parameter specifies the shape of the digital RBW filter. The default value is FFT Based.Name (value)DescriptionFFT Based (0)An RBW filter with a fast Fourier transform (FFT)-based response is applied.Gaussian (1)An RBW filter with a Gaussian response is applied.Flat (2)An RBW filter with a flat response is applied. |
| Name (value) | Description |  |  |
| FFT Based (0) | An RBW filter with a fast Fourier transform (FFT)-based response is applied. |  |  |
| Gaussian (1) | An RBW filter with a Gaussian response is applied. |  |  |
| Flat (2) | An RBW filter with a flat response is applied. |  |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

CHP

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration__chp_1gabf82a47d57abcdd68e17bc140c307b6d.html language=enus -->
## TOPIC 00186: RFmxTDSCDMA_CHPCfgAveraging

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration__chp_1gabf82a47d57abcdd68e17bc140c307b6d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration__chp_1gabf82a47d57abcdd68e17bc140c307b6d.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures averaging for the CHP measurement. Syntaxint32 __stdcall RFmxTDSCDMA_CHPCfgAveraging(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 averagingEnabled, int32 averagingCount, int32 averagingType)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis

### RFmxTDSCDMA_CHPCfgAveraging

Configures averaging for the CHP measurement.

#### Syntax

int32 __stdcall RFmxTDSCDMA_CHPCfgAveraging(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 averagingEnabled, int32 averagingCount, int32 averagingType)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Examples:"""signal::sig1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| averagingEnabled | [in] | int32 | This parameter enables averaging for spectrum measurements. The default value is False.Name (value)DescriptionFalse (0)Disables averaging for the CHP measurement.True (1)The CHP measurement uses the RFMXTDSCDMA_ATTR_CHP_AVERAGING_COUNT attribute as the number of acquisitions over which the CHP measurement is averaged. |
| Name (value) | Description |  |  |
| False (0) | Disables averaging for the CHP measurement. |  |  |
| True (1) | The CHP measurement uses the RFMXTDSCDMA_ATTR_CHP_AVERAGING_COUNT attribute as the number of acquisitions over which the CHP measurement is averaged. |  |  |
| averagingCount | [in] | int32 | This parameter specifies the number of acquisitions used for averaging when you set the Averaging Enabled parameter to True. The default value is 10. |
| averagingType | [in] | int32 | This parameter specifies the averaging type for averaging multiple spectrum acquisitions. RFmx uses the averaged spectrum for the measurement.The default value is RMS.Name (value)DescriptionRMS (0)The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor.Log (1)The power spectrum is averaged in a logarithmic scale.Scalar (2)The square root of the power spectrum is averaged.Max (3)The peak power in the spectrum at each frequency bin is retained from one acquisition to the next.Min (4)The lowest power in the spectrum at each frequency bin is retained from one acquisition to the next.Refer to the Averaging section of the Spectrum topic for more information about averaging types. |
| Name (value) | Description |  |  |
| RMS (0) | The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. |  |  |
| Log (1) | The power spectrum is averaged in a logarithmic scale. |  |  |
| Scalar (2) | The square root of the power spectrum is averaged. |  |  |
| Max (3) | The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. |  |  |
| Min (4) | The lowest power in the spectrum at each frequency bin is retained from one acquisition to the next. |  |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

CHP

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration__chp_1gadad0e0e8243e48abc9c39f56dcfc5c32.html language=enus -->
## TOPIC 00187: RFmxTDSCDMA_CHPCfgSweepTime

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration__chp_1gadad0e0e8243e48abc9c39f56dcfc5c32.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration__chp_1gadad0e0e8243e48abc9c39f56dcfc5c32.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the sweep time. Syntaxint32 __stdcall RFmxTDSCDMA_CHPCfgSweepTime(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 sweepTimeAuto, float64 sweepTimeInterval)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifies the RFmx session

### RFmxTDSCDMA_CHPCfgSweepTime

Configures the sweep time.

#### Syntax

int32 __stdcall RFmxTDSCDMA_CHPCfgSweepTime(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 sweepTimeAuto, float64 sweepTimeInterval)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Examples:"""signal::sig1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| sweepTimeAuto | [in] | int32 | This parameter specifies whether the measurement computes the sweep time. The default value is True.Name (value)DescriptionFalse (0)The measurement uses the sweep time that you specify using the Sweep Time Interval parameter.True (1)The measurement uses the default sweep time of .00066 seconds (s).Refer to the RBW and Sweep Time section in the CHP topic for more details on RBW and sweep time. |
| Name (value) | Description |  |  |
| False (0) | The measurement uses the sweep time that you specify using the Sweep Time Interval parameter. |  |  |
| True (1) | The measurement uses the default sweep time of .00066 seconds (s). |  |  |
| sweepTimeInterval | [in] | float64 | This parameter specifies the sweep time when you set the Sweep Time Auto parameter to False. This value is expressed in seconds. The default value is 0.00066 s. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

CHP

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration__frequency.html language=enus -->
## TOPIC 00188: Frequency

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration__frequency.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration__frequency.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxTDSCDMA_CfgFrequencyConfigures the expected carrier frequency of the RF signal to acquire. The signal analyzer tunes to this frequency. RFmxTDSCDMA_CfgFrequencyChannelNumberConfigures the carrier frequency of the RF signal to acquire according to the given c

### Frequency

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxTDSCDMA_CfgFrequency | Configures the expected carrier frequency of the RF signal to acquire. The signal analyzer tunes to this frequency. |
| RFmxTDSCDMA_CfgFrequencyChannelNumber | Configures the carrier frequency of the RF signal to acquire according to the given channel number. The signal analyzer tunes to this frequency. |

#### Attachments

None

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration__frequency_1ga2b6d3e0643870ce1c1d2f498f917873a.html language=enus -->
## TOPIC 00189: RFmxTDSCDMA_CfgFrequencyChannelNumber

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration__frequency_1ga2b6d3e0643870ce1c1d2f498f917873a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration__frequency_1ga2b6d3e0643870ce1c1d2f498f917873a.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the carrier frequency of the RF signal to acquire according to the given channel number. The signal analyzer tunes to this frequency. Syntaxint32 __stdcall RFmxTDSCDMA_CfgFrequencyChannelNumber(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 channelNumber)ParametersNameDi

### RFmxTDSCDMA_CfgFrequencyChannelNumber

Configures the carrier frequency of the RF signal to acquire according to the given channel number. The signal analyzer tunes to this frequency.

#### Syntax

int32 __stdcall RFmxTDSCDMA_CfgFrequencyChannelNumber(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 channelNumber)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Examples:"""signal::sig1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| channelNumber | [in] | int32 | This parameter specifies the number of the channel to be measured. The center frequency is derived from this value. The default value is 5000. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Frequency

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration__frequency_1gaa1a2de1d1dbcc690179517bdb88d859c.html language=enus -->
## TOPIC 00190: RFmxTDSCDMA_CfgFrequency

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration__frequency_1gaa1a2de1d1dbcc690179517bdb88d859c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration__frequency_1gaa1a2de1d1dbcc690179517bdb88d859c.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the expected carrier frequency of the RF signal to acquire. The signal analyzer tunes to this frequency. Syntaxint32 __stdcall RFmxTDSCDMA_CfgFrequency(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 centerFrequency)ParametersNameDirectionTypeDescriptioninstrumentHandle

### RFmxTDSCDMA_CfgFrequency

Configures the expected carrier frequency of the RF signal to acquire. The signal analyzer tunes to this frequency.

#### Syntax

int32 __stdcall RFmxTDSCDMA_CfgFrequency(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 centerFrequency)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Examples:"""signal::sig1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| centerFrequency | [in] | float64 | This parameter specifies the carrier frequency of the RF signal to acquire. The signal analyzer tunes to this frequency. This value is expressed in Hz. The default of this parameter is hardware dependent. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Frequency

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration__modacc.html language=enus -->
## TOPIC 00191: ModAcc

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration__modacc.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration__modacc.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxTDSCDMA_ModAccCfgAveragingConfigures averaging for the ModAcc measurement. RFmxTDSCDMA_ModAccCfgSlotTypeConfigures the type of the Time Slot for ModAcc analysis. RFmxTDSCDMA_ModAccCfgSynchronizationModeAndIntervalConfigures the synchronization mode, measurem

### ModAcc

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxTDSCDMA_ModAccCfgAveraging | Configures averaging for the ModAcc measurement. |
| RFmxTDSCDMA_ModAccCfgSlotType | Configures the type of the Time Slot for ModAcc analysis. |
| RFmxTDSCDMA_ModAccCfgSynchronizationModeAndInterval | Configures the synchronization mode, measurement offset, and measurement length for ModAcc analysis. |

#### Attachments

None

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration__modacc_1ga1f9ac2ce0b913bb62f472c2d8afceb2b.html language=enus -->
## TOPIC 00192: RFmxTDSCDMA_ModAccCfgSynchronizationModeAndInterval

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration__modacc_1ga1f9ac2ce0b913bb62f472c2d8afceb2b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration__modacc_1ga1f9ac2ce0b913bb62f472c2d8afceb2b.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the synchronization mode, measurement offset, and measurement length for ModAcc analysis. Syntaxint32 __stdcall RFmxTDSCDMA_ModAccCfgSynchronizationModeAndInterval(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 synchronizationMode, int32 measurementOffset, int32 measurem

### RFmxTDSCDMA_ModAccCfgSynchronizationModeAndInterval

Configures the synchronization mode, measurement offset, and measurement length for ModAcc analysis.

#### Syntax

int32 __stdcall RFmxTDSCDMA_ModAccCfgSynchronizationModeAndInterval(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 synchronizationMode, int32 measurementOffset, int32 measurementLength)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Examples:"""signal::sig1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| synchronizationMode | [in] | int32 | This parameter specifies the synchronization mode for the ModAcc measurement. The default value is Slot.Name (value)DescriptionSlot (0)The measurement uses the slot synchronization mode. The first slot boundary in the acquired signal is detected, and the measurement is performed over the number of slots specified by the Measurement Length parameter, starting at the offset specified by the Measurement Offset parameter. If you set the RFMXTDSCDMA_ATTR_TRIGGER_TYPE attribute to Digital Edge, you should provide the trigger at the start of the slot from which the Measurement Offset parameter should be considered. If you set the Trigger Type attribute to IQ Power Edge, it is required that the received signal has either one traffic time slot or contiguous traffic time slots. Additionally, for this trigger type, the traffic time slot(s) in the received signal should be contiguous with the pilot time slot, if the pilot time slot is present.Subframe (1)The measurement uses the subframe synchronization mode. The first subframe boundary in the acquired signal is detected, and the measurement is performed over the number of slots specified by the Measurement Length parameter, starting at the offset from the boundary specified by the Measurement Offset parameter. If you set the Trigger Type attribute to Digital Edge, you should provide the trigger at the start of the subframe. If you set the Trigger Type attribute to IQ Power Edge, it is required that the received signal has either one traffic time slot or contiguous traffic time slots. Additionally, the traffic time slot should be contiguous with the active pilot slot. |
| Name (value) | Description |  |  |
| Slot (0) | The measurement uses the slot synchronization mode. The first slot boundary in the acquired signal is detected, and the measurement is performed over the number of slots specified by the Measurement Length parameter, starting at the offset specified by the Measurement Offset parameter. If you set the RFMXTDSCDMA_ATTR_TRIGGER_TYPE attribute to Digital Edge, you should provide the trigger at the start of the slot from which the Measurement Offset parameter should be considered. If you set the Trigger Type attribute to IQ Power Edge, it is required that the received signal has either one traffic time slot or contiguous traffic time slots. Additionally, for this trigger type, the traffic time slot(s) in the received signal should be contiguous with the pilot time slot, if the pilot time slot is present. |  |  |
| Subframe (1) | The measurement uses the subframe synchronization mode. The first subframe boundary in the acquired signal is detected, and the measurement is performed over the number of slots specified by the Measurement Length parameter, starting at the offset from the boundary specified by the Measurement Offset parameter. If you set the Trigger Type attribute to Digital Edge, you should provide the trigger at the start of the subframe. If you set the Trigger Type attribute to IQ Power Edge, it is required that the received signal has either one traffic time slot or contiguous traffic time slots. Additionally, the traffic time slot should be contiguous with the active pilot slot. |  |  |
| measurementOffset | [in] | int32 | This parameter specifies the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The default value is 0. |
| measurementLength | [in] | int32 | This parameter specifies the duration of the ModAcc measurement. The default value is 1. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration__modacc_1ga59473b78deae41adeda7afeb39ee501a.html language=enus -->
## TOPIC 00193: RFmxTDSCDMA_ModAccCfgAveraging

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration__modacc_1ga59473b78deae41adeda7afeb39ee501a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration__modacc_1ga59473b78deae41adeda7afeb39ee501a.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures averaging for the ModAcc measurement. Syntaxint32 __stdcall RFmxTDSCDMA_ModAccCfgAveraging(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 averagingEnabled, int32 averagingCount)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter spec

### RFmxTDSCDMA_ModAccCfgAveraging

Configures averaging for the ModAcc measurement.

#### Syntax

int32 __stdcall RFmxTDSCDMA_ModAccCfgAveraging(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 averagingEnabled, int32 averagingCount)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Examples:"""signal::sig1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| averagingEnabled | [in] | int32 | This parameter specifies whether to enable averaging for the ModAcc measurement. The default value is False.Name (value)DescriptionFalse (0)Disables averaging for the ModAcc measurement.True (1)The ModAcc measurement uses the Averaging Count parameter as the number of acquisitions over which the ModAcc measurement is averaged. |
| Name (value) | Description |  |  |
| False (0) | Disables averaging for the ModAcc measurement. |  |  |
| True (1) | The ModAcc measurement uses the Averaging Count parameter as the number of acquisitions over which the ModAcc measurement is averaged. |  |  |
| averagingCount | [in] | int32 | This parameter specifies the number of acquisitions used for averaging when you set the Averaging Enabled parameter to True. The default value is 10. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration__modacc_1gadae4d89af5e306d4788694c0f372e6c6.html language=enus -->
## TOPIC 00194: RFmxTDSCDMA_ModAccCfgSlotType

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration__modacc_1gadae4d89af5e306d4788694c0f372e6c6.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration__modacc_1gadae4d89af5e306d4788694c0f372e6c6.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the type of the Time Slot for ModAcc analysis. Syntaxint32 __stdcall RFmxTDSCDMA_ModAccCfgSlotType(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 slotType)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifies the RFmx session

### RFmxTDSCDMA_ModAccCfgSlotType

Configures the type of the Time Slot for ModAcc analysis.

#### Syntax

int32 __stdcall RFmxTDSCDMA_ModAccCfgSlotType(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 slotType)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Examples:"""signal::sig1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| slotType | [in] | int32 | This parameter specifies the type of the Time Slot for ModAcc analysis. The default value is Traffic.Name (value)DescriptionTraffic (0)The measurement is performed on the traffic time slot. The composite, data, and midamble ModAcc results are obtained when you select this slot type.Pilot (1)The measurement is performed on the pilot time slot. The pilot ModAcc results are obtained when you select this slot type. |
| Name (value) | Description |  |  |
| Traffic (0) | The measurement is performed on the traffic time slot. The composite, data, and midamble ModAcc results are obtained when you select this slot type. |  |  |
| Pilot (1) | The measurement is performed on the pilot time slot. The pilot ModAcc results are obtained when you select this slot type. |  |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration__obw.html language=enus -->
## TOPIC 00195: OBW

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration__obw.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration__obw.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxTDSCDMA_OBWCfgAveragingConfigures averaging for the OBW measurement. RFmxTDSCDMA_OBWCfgRBWFilterConfigures the RBW filter. RFmxTDSCDMA_OBWCfgSweepTimeConfigures the sweep time. AttachmentsNone

### OBW

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxTDSCDMA_OBWCfgAveraging | Configures averaging for the OBW measurement. |
| RFmxTDSCDMA_OBWCfgRBWFilter | Configures the RBW filter. |
| RFmxTDSCDMA_OBWCfgSweepTime | Configures the sweep time. |

#### Attachments

None

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration__obw_1ga05a658ac843c05afe392bba3b48c14e1.html language=enus -->
## TOPIC 00196: RFmxTDSCDMA_OBWCfgRBWFilter

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration__obw_1ga05a658ac843c05afe392bba3b48c14e1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration__obw_1ga05a658ac843c05afe392bba3b48c14e1.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the RBW filter. Syntaxint32 __stdcall RFmxTDSCDMA_OBWCfgRBWFilter(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 rbwAuto, float64 rbw, int32 rbwFilterType)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifies the RFmx session

### RFmxTDSCDMA_OBWCfgRBWFilter

Configures the RBW filter.

#### Syntax

int32 __stdcall RFmxTDSCDMA_OBWCfgRBWFilter(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 rbwAuto, float64 rbw, int32 rbwFilterType)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Examples:"""signal::sig1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| rbwAuto | [in] | int32 | This parameter specifies whether the measurement computes the RBW. The default value is True.Name (value)DescriptionFalse (0)The measurement uses the RBW you specify.True (1)RFmx TD-SCDMA automatically determines the RBW.Refer to the RBW and Sweep Time section in the Spectrum topic for more information about RBW and sweep time. |
| Name (value) | Description |  |  |
| False (0) | The measurement uses the RBW you specify. |  |  |
| True (1) | RFmx TD-SCDMA automatically determines the RBW. |  |  |
| rbw | [in] | float64 | This parameter specifies the bandwidth of the RBW filter used to sweep the acquired signal when you set the RBW Auto parameter to False. This value is expressed in Hz. The default value is 5.636 kHz. |
| rbwFilterType | [in] | int32 | This parameter specifies the shape of the digital RBW filter. The default value is FFT Based.Name (value)DescriptionFFT Based (0)An RBW filter with a fast Fourier transform (FFT)-based response is applied.Gaussian (1)An RBW filter with a Gaussian response is applied.Flat (2)An RBW filter with a flat response is applied. |
| Name (value) | Description |  |  |
| FFT Based (0) | An RBW filter with a fast Fourier transform (FFT)-based response is applied. |  |  |
| Gaussian (1) | An RBW filter with a Gaussian response is applied. |  |  |
| Flat (2) | An RBW filter with a flat response is applied. |  |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

OBW

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration__obw_1ga1b31f423f27137ef6ff8ca4db111b181.html language=enus -->
## TOPIC 00197: RFmxTDSCDMA_OBWCfgSweepTime

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration__obw_1ga1b31f423f27137ef6ff8ca4db111b181.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration__obw_1ga1b31f423f27137ef6ff8ca4db111b181.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the sweep time. Syntaxint32 __stdcall RFmxTDSCDMA_OBWCfgSweepTime(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 sweepTimeAuto, float64 sweepTimeInterval)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifies the RFmx session

### RFmxTDSCDMA_OBWCfgSweepTime

Configures the sweep time.

#### Syntax

int32 __stdcall RFmxTDSCDMA_OBWCfgSweepTime(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 sweepTimeAuto, float64 sweepTimeInterval)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Examples:"""signal::sig1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| sweepTimeAuto | [in] | int32 | This parameter specifies whether the measurement computes the sweep time. The default value is True.Name (value)DescriptionFalse (0)The measurement uses the sweep time that you specify using the Sweep Time Interval parameter.True (1)The measurement uses the default sweep time of .00066 seconds (s).Refer to the RBW and Sweep Time section in the OBW topic for more details on RBW and sweep time. |
| Name (value) | Description |  |  |
| False (0) | The measurement uses the sweep time that you specify using the Sweep Time Interval parameter. |  |  |
| True (1) | The measurement uses the default sweep time of .00066 seconds (s). |  |  |
| sweepTimeInterval | [in] | float64 | This parameter specifies the sweep time when you set the Sweep Time Auto parameter to False. This value is expressed in seconds. The default value is 0.00066 s. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

OBW

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration__obw_1ga8dade87a0bfbc26bd992a1bac7577e5d.html language=enus -->
## TOPIC 00198: RFmxTDSCDMA_OBWCfgAveraging

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration__obw_1ga8dade87a0bfbc26bd992a1bac7577e5d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration__obw_1ga8dade87a0bfbc26bd992a1bac7577e5d.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures averaging for the OBW measurement. Syntaxint32 __stdcall RFmxTDSCDMA_OBWCfgAveraging(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 averagingEnabled, int32 averagingCount, int32 averagingType)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis

### RFmxTDSCDMA_OBWCfgAveraging

Configures averaging for the OBW measurement.

#### Syntax

int32 __stdcall RFmxTDSCDMA_OBWCfgAveraging(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 averagingEnabled, int32 averagingCount, int32 averagingType)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Examples:"""signal::sig1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| averagingEnabled | [in] | int32 | This parameter enables averaging for spectrum measurements. The default value is False.Name (value)DescriptionFalse (0)Disables averaging for the OBW measurement.True (1)The OBW measurement uses the value of the RFMXTDSCDMA_ATTR_OBW_AVERAGING_COUNT attribute as the number of acquisitions over which the OBW measurement is averaged. |
| Name (value) | Description |  |  |
| False (0) | Disables averaging for the OBW measurement. |  |  |
| True (1) | The OBW measurement uses the value of the RFMXTDSCDMA_ATTR_OBW_AVERAGING_COUNT attribute as the number of acquisitions over which the OBW measurement is averaged. |  |  |
| averagingCount | [in] | int32 | This parameter specifies the number of acquisitions used for averaging when you set the Averaging Enabled parameter to True. The default value is 10. |
| averagingType | [in] | int32 | This parameter specifies the averaging type for averaging multiple spectrum acquisitions. RFmx uses the averaged spectrum for the measurement.The default value is RMS.Name (value)DescriptionRMS (0)The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor.Log (1)The power spectrum is averaged in a logarithmic scale.Scalar (2)The square root of the power spectrum is averaged.Max (3)The peak power in the spectrum at each frequency bin is retained from one acquisition to the next.Min (4)The lowest power in the spectrum at each frequency bin is retained from one acquisition to the next.Refer to the Averaging section of the Spectrum topic for more information about averaging types. |
| Name (value) | Description |  |  |
| RMS (0) | The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. |  |  |
| Log (1) | The power spectrum is averaged in a logarithmic scale. |  |  |
| Scalar (2) | The square root of the power spectrum is averaged. |  |  |
| Max (3) | The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. |  |  |
| Min (4) | The lowest power in the spectrum at each frequency bin is retained from one acquisition to the next. |  |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

OBW

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration__pvt.html language=enus -->
## TOPIC 00199: PVT

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration__pvt.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration__pvt.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxTDSCDMA_PVTCfgAveragingConfigures averaging for the power versus time (PVT) measurement. RFmxTDSCDMA_PVTCfgMeasurementMethodConfigures the measurement method for the power versus time (PVT) measurement. AttachmentsNone

### PVT

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxTDSCDMA_PVTCfgAveraging | Configures averaging for the power versus time (PVT) measurement. |
| RFmxTDSCDMA_PVTCfgMeasurementMethod | Configures the measurement method for the power versus time (PVT) measurement. |

#### Attachments

None

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration__pvt_1ga21693681c15f8cc97c8f7d61324c95f2.html language=enus -->
## TOPIC 00200: RFmxTDSCDMA_PVTCfgMeasurementMethod

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration__pvt_1ga21693681c15f8cc97c8f7d61324c95f2.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration__pvt_1ga21693681c15f8cc97c8f7d61324c95f2.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the measurement method for the power versus time (PVT) measurement. Syntaxint32 __stdcall RFmxTDSCDMA_PVTCfgMeasurementMethod(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 measurementMethod)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis

### RFmxTDSCDMA_PVTCfgMeasurementMethod

Configures the measurement method for the power versus time (PVT) measurement.

#### Syntax

int32 __stdcall RFmxTDSCDMA_PVTCfgMeasurementMethod(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 measurementMethod)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Examples:"""signal::sig1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| measurementMethod | [in] | int32 | This parameter specifies the method used for performing the PVT measurement. The default value is Normal.Name (value)DescriptionNormal (0)The PVT measurement acquires the spectrum using the same signal analyzer setting across frequency bands. Use this method when a higher measurement speed is preferred over a higher dynamic range.Dynamic Range (1)The PVT measurement acquires the spectrum using the hardware-specific optimizations for different frequency bands. Use this method to get the best dynamic range. Supported Devices: PXIe-5644R/5645R/5646R/5840/5841/5842/5860. |
| Name (value) | Description |  |  |
| Normal (0) | The PVT measurement acquires the spectrum using the same signal analyzer setting across frequency bands. Use this method when a higher measurement speed is preferred over a higher dynamic range. |  |  |
| Dynamic Range (1) | The PVT measurement acquires the spectrum using the hardware-specific optimizations for different frequency bands. Use this method to get the best dynamic range. Supported Devices: PXIe-5644R/5645R/5646R/5840/5841/5842/5860. |  |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

PVT

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration__pvt_1gad58c8aa6e642790864f3dfb1135eb13a.html language=enus -->
## TOPIC 00201: RFmxTDSCDMA_PVTCfgAveraging

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration__pvt_1gad58c8aa6e642790864f3dfb1135eb13a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration__pvt_1gad58c8aa6e642790864f3dfb1135eb13a.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures averaging for the power versus time (PVT) measurement. Syntaxint32 __stdcall RFmxTDSCDMA_PVTCfgAveraging(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 averagingEnabled, int32 averagingCount, int32 averagingType)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]n

### RFmxTDSCDMA_PVTCfgAveraging

Configures averaging for the power versus time (PVT) measurement.

#### Syntax

int32 __stdcall RFmxTDSCDMA_PVTCfgAveraging(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 averagingEnabled, int32 averagingCount, int32 averagingType)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Examples:"""signal::sig1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| averagingEnabled | [in] | int32 | This parameter specifies whether to enable averaging for the PVT measurement. The default value is False.Name (value)DescriptionFalse (0)The measurement is performed on a single acquisition.True (1)The PVT measurement uses the value of the Averaging Count parameter as the number of acquisitions over which the PVT measurement is averaged. |
| Name (value) | Description |  |  |
| False (0) | The measurement is performed on a single acquisition. |  |  |
| True (1) | The PVT measurement uses the value of the Averaging Count parameter as the number of acquisitions over which the PVT measurement is averaged. |  |  |
| averagingCount | [in] | int32 | This parameter specifies the number of acquisitions used for averaging when you set the Averaging Enabled parameter to True. The default value is 10. |
| averagingType | [in] | int32 | This parameter specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the PVT measurement. The default value is RMS.Name (value)DescriptionRMS (0)The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor.Log (1)The power spectrum is averaged on a logarithmic scale. |
| Name (value) | Description |  |  |
| RMS (0) | The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. |  |  |
| Log (1) | The power spectrum is averaged on a logarithmic scale. |  |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

PVT

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration__sem.html language=enus -->
## TOPIC 00202: SEM

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration__sem.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration__sem.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxTDSCDMA_SEMCfgAveragingConfigures averaging for the SEM measurement. RFmxTDSCDMA_SEMCfgSweepTimeConfigures the sweep time. AttachmentsNone

### SEM

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxTDSCDMA_SEMCfgAveraging | Configures averaging for the SEM measurement. |
| RFmxTDSCDMA_SEMCfgSweepTime | Configures the sweep time. |

#### Attachments

None

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration__sem_1ga33eb80682d957635fe32db4a2d07fb96.html language=enus -->
## TOPIC 00203: RFmxTDSCDMA_SEMCfgSweepTime

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration__sem_1ga33eb80682d957635fe32db4a2d07fb96.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration__sem_1ga33eb80682d957635fe32db4a2d07fb96.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the sweep time. Syntaxint32 __stdcall RFmxTDSCDMA_SEMCfgSweepTime(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 sweepTimeAuto, float64 sweepTimeInterval)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifies the RFmx session

### RFmxTDSCDMA_SEMCfgSweepTime

Configures the sweep time.

#### Syntax

int32 __stdcall RFmxTDSCDMA_SEMCfgSweepTime(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 sweepTimeAuto, float64 sweepTimeInterval)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Examples:"""signal::sig1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| sweepTimeAuto | [in] | int32 | This parameter specifies whether the measurement computes the sweep time. The default value is True.Name (value)DescriptionFalse (0)The measurement uses the sweep time that you specify using the Sweep Time Interval parameter.True (1)The measurement uses the default sweep time of .00066 seconds (s). |
| Name (value) | Description |  |  |
| False (0) | The measurement uses the sweep time that you specify using the Sweep Time Interval parameter. |  |  |
| True (1) | The measurement uses the default sweep time of .00066 seconds (s). |  |  |
| sweepTimeInterval | [in] | float64 | This parameter specifies the sweep time when you set the Sweep Time Auto parameter to False. This value is expressed in seconds. The default value is 0.00066 s. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration__sem_1ga46fcc6854dc3682df05d7217b87b2312.html language=enus -->
## TOPIC 00204: RFmxTDSCDMA_SEMCfgAveraging

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration__sem_1ga46fcc6854dc3682df05d7217b87b2312.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration__sem_1ga46fcc6854dc3682df05d7217b87b2312.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures averaging for the SEM measurement. Syntaxint32 __stdcall RFmxTDSCDMA_SEMCfgAveraging(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 averagingEnabled, int32 averagingCount, int32 averagingType)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis

### RFmxTDSCDMA_SEMCfgAveraging

Configures averaging for the SEM measurement.

#### Syntax

int32 __stdcall RFmxTDSCDMA_SEMCfgAveraging(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 averagingEnabled, int32 averagingCount, int32 averagingType)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Examples:"""signal::sig1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| averagingEnabled | [in] | int32 | This parameter enables averaging for spectrum measurements. The default value is False.Name (value)DescriptionFalse (0)Disables averaging for the SEM measurement.True (1)The SEM measurement uses the value of the RFMXTDSCDMA_ATTR_SEM_AVERAGING_COUNT attribute as the number of acquisitions over which the SEM measurement is averaged. |
| Name (value) | Description |  |  |
| False (0) | Disables averaging for the SEM measurement. |  |  |
| True (1) | The SEM measurement uses the value of the RFMXTDSCDMA_ATTR_SEM_AVERAGING_COUNT attribute as the number of acquisitions over which the SEM measurement is averaged. |  |  |
| averagingCount | [in] | int32 | This parameter specifies the number of acquisitions used for averaging when you set the Averaging Enabled parameter to True. The default value is 10. |
| averagingType | [in] | int32 | This parameter specifies the averaging type for averaging multiple spectrum acquisitions. RFmx uses the averaged spectrum for the measurement.The default value is RMS.Name (value)DescriptionRMS (0)The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor.Log (1)The power spectrum is averaged in a logarithmic scale.Scalar (2)The square root of the power spectrum is averaged.Max (3)The peak power in the spectrum at each frequency bin is retained from one acquisition to the next.Min (4)The lowest power in the spectrum at each frequency bin is retained from one acquisition to the next.Refer to the Averaging section of the Spectrum topic for more information about averaging types. |
| Name (value) | Description |  |  |
| RMS (0) | The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. |  |  |
| Log (1) | The power spectrum is averaged in a logarithmic scale. |  |  |
| Scalar (2) | The square root of the power spectrum is averaged. |  |  |
| Max (3) | The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. |  |  |
| Min (4) | The lowest power in the spectrum at each frequency bin is retained from one acquisition to the next. |  |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration__slotpower.html language=enus -->
## TOPIC 00205: SlotPower

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration__slotpower.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration__slotpower.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxTDSCDMA_SlotPowerCfgMeasurementLengthConfigures the measurement length for the SlotPower measurement. AttachmentsNone

### SlotPower

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxTDSCDMA_SlotPowerCfgMeasurementLength | Configures the measurement length for the SlotPower measurement. |

#### Attachments

None

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration__slotpower_1gac516d4ce61fb138585d6a86b1c29d72d.html language=enus -->
## TOPIC 00206: RFmxTDSCDMA_SlotPowerCfgMeasurementLength

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration__slotpower_1gac516d4ce61fb138585d6a86b1c29d72d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration__slotpower_1gac516d4ce61fb138585d6a86b1c29d72d.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the measurement length for the SlotPower measurement. Syntaxint32 __stdcall RFmxTDSCDMA_SlotPowerCfgMeasurementLength(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 measurementLength)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis paramete

### RFmxTDSCDMA_SlotPowerCfgMeasurementLength

Configures the measurement length for the SlotPower measurement.

#### Syntax

int32 __stdcall RFmxTDSCDMA_SlotPowerCfgMeasurementLength(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 measurementLength)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Examples:"""signal::sig1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| measurementLength | [in] | int32 | This parameter specifies the measurement length for the SlotPower measurement. This value is expressed in slots. The SlotPower measurement assumes that there is only one active traffic time slot per subframe, and that the position of this active time slot is the same in each subframe. Additionally, it assumes that there are no pilots present in the received signal.NI recommends you set a measurement length as a multiple of the number of slots per subframe, that is a multiple of 7. For example, when you set this attribute to 28 slots, the SlotPower measurement would report results for the 4 active time slots within the specified measurement length. In this example, 28 slots = 4 subframes.The start of the measurement is determined by the RFMXTDSCDMA_ATTR_TRIGGER_TYPE attribute. Although all the values of the Trigger Type attribute are supported for this measurement, it is recommended to set the Trigger Type attribute to Digital Edge with the following options: Digital trigger at the start of active slot, with the RFMXTDSCDMA_ATTR_TRIGGER_DELAY attribute set to 0 seconds Digital trigger at the start of the subframe, with the Trigger Delay attribute configured to a value which is equal to the time offset of the active time slot from the start of the subframe The table shows the values of the Trigger Delay attribute, when you specify the following active slots values:Active SlotTrigger Delay (microseconds)TS00TS1950TS21625TS32300TS42975TS53650TS64325If you cannot provide a digital trigger, you can set Trigger Type attribute to IQ Power Edge to ensure that the measurement starts at the start of an active time slot. To ensure this trigger works properly, NI recommends you complete the following steps: Set the RFMXTDSCDMA_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL attribute to allow triggering for any of the power levels in the active slots Run the RFmx measurement just before generating your signal If you set the Trigger type attribute to None, the measurement will automatically detect the start of the first burst and measure the traffic slot in that position in every subframe.You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.The default value is 28. The minimum value is 1. |
| Active Slot | Trigger Delay (microseconds) |  |  |
| TS0 | 0 |  |  |
| TS1 | 950 |  |  |
| TS2 | 1625 |  |  |
| TS3 | 2300 |  |  |
| TS4 | 2975 |  |  |
| TS5 | 3650 |  |  |
| TS6 | 4325 |  |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SlotPower

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration__trigger.html language=enus -->
## TOPIC 00207: Trigger

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration__trigger.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration__trigger.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxTDSCDMA_CfgDigitalEdgeTriggerConfigures the device to wait for a digital edge trigger to mark a reference point within the record. RFmxTDSCDMA_CfgIQPowerEdgeTriggerConfigures the device to wait for the complex power of the I/Q data to cross the specified thr

### Trigger

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxTDSCDMA_CfgDigitalEdgeTrigger | Configures the device to wait for a digital edge trigger to mark a reference point within the record. |
| RFmxTDSCDMA_CfgIQPowerEdgeTrigger | Configures the device to wait for the complex power of the I/Q data to cross the specified threshold to mark a reference point within the record. |
| RFmxTDSCDMA_CfgSoftwareEdgeTrigger | Configures the device to wait for a software trigger to mark a reference point within the record. |
| RFmxTDSCDMA_DisableTrigger | Configures the device to not wait for a trigger to mark a reference point within a record. This function defines the signal triggering as immediate. |

#### Attachments

None

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration__trigger_1ga18066e12fe9b9e74a59440e533bedbf0.html language=enus -->
## TOPIC 00208: RFmxTDSCDMA_CfgSoftwareEdgeTrigger

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration__trigger_1ga18066e12fe9b9e74a59440e533bedbf0.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration__trigger_1ga18066e12fe9b9e74a59440e533bedbf0.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the device to wait for a software trigger to mark a reference point within the record. Syntaxint32 __stdcall RFmxTDSCDMA_CfgSoftwareEdgeTrigger(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 triggerDelay, int32 enableTrigger)ParametersNameDirectionTypeDescriptioninstru

### RFmxTDSCDMA_CfgSoftwareEdgeTrigger

Configures the device to wait for a software trigger to mark a reference point within the record.

#### Syntax

int32 __stdcall RFmxTDSCDMA_CfgSoftwareEdgeTrigger(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 triggerDelay, int32 enableTrigger)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Examples:"""signal::sig1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| triggerDelay | [in] | float64 | This parameter specifies the trigger delay time. This value is expressed in seconds. The default value is 0. |
| enableTrigger | [in] | int32 | This parameter specifies whether to enable the trigger. The default value is TRUE. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Trigger

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration__trigger_1ga2f70fa02cb7daf06dbb4ff6bd913cc64.html language=enus -->
## TOPIC 00209: RFmxTDSCDMA_DisableTrigger

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration__trigger_1ga2f70fa02cb7daf06dbb4ff6bd913cc64.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration__trigger_1ga2f70fa02cb7daf06dbb4ff6bd913cc64.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the device to not wait for a trigger to mark a reference point within a record. This function defines the signal triggering as immediate. Syntaxint32 __stdcall RFmxTDSCDMA_DisableTrigger(niRFmxInstrHandle instrumentHandle, char selectorString[])ParametersNameDirectionTypeDescriptioninstru

### RFmxTDSCDMA_DisableTrigger

Configures the device to not wait for a trigger to mark a reference point within a record. This function defines the signal triggering as immediate.

#### Syntax

int32 __stdcall RFmxTDSCDMA_DisableTrigger(niRFmxInstrHandle instrumentHandle, char selectorString[])

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Examples:"""signal::sig1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Trigger

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration__trigger_1ga978c01fd079c6f470f376b8b25ee6412.html language=enus -->
## TOPIC 00210: RFmxTDSCDMA_CfgIQPowerEdgeTrigger

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration__trigger_1ga978c01fd079c6f470f376b8b25ee6412.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration__trigger_1ga978c01fd079c6f470f376b8b25ee6412.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the device to wait for the complex power of the I/Q data to cross the specified threshold to mark a reference point within the record. Syntaxint32 __stdcall RFmxTDSCDMA_CfgIQPowerEdgeTrigger(niRFmxInstrHandle instrumentHandle, char selectorString[], char iqPowerEdgeSource[], int32 iqPower

### RFmxTDSCDMA_CfgIQPowerEdgeTrigger

Configures the device to wait for the complex power of the I/Q data to cross the specified threshold to mark a reference point within the record.

#### Syntax

int32 __stdcall RFmxTDSCDMA_CfgIQPowerEdgeTrigger(niRFmxInstrHandle instrumentHandle, char selectorString[], char iqPowerEdgeSource[], int32 iqPowerEdgeSlope, float64 iqPowerEdgeLevel, float64 triggerDelay, int32 minimumQuietTimeMode, float64 minimumQuietTime, int32 iqPowerEdgeLevelType, int32 enableTrigger)

#### Remarks

To trigger on burst signals, specify a minimum quiet time. The minimum quiet time ensures that the trigger does not occur in the middle of the burst signal. The quiet time must be set to a value smaller than the time between bursts but large enough to ignore power changes within a burst.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Examples:"""signal::sig1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| iqPowerEdgeSource | [in] | char[] | This parameter specifies the channel from which the device monitors the trigger. The default of this parameter is hardware dependent. |
| iqPowerEdgeSlope | [in] | int32 | This parameter specifies whether the device asserts the trigger when the signal power is rising or when it is falling. The device asserts the trigger when the signal power exceeds the specified level with the slope you specify. The default value is Rising Slope.Name (value)DescriptionRising Slope (0)The trigger asserts when the signal power is rising.Falling Slope (1)The trigger asserts when the signal power is falling. |
| Name (value) | Description |  |  |
| Rising Slope (0) | The trigger asserts when the signal power is rising. |  |  |
| Falling Slope (1) | The trigger asserts when the signal power is falling. |  |  |
| iqPowerEdgeLevel | [in] | float64 | This parameter specifies the threshold above or below which the signal analyzer triggers, depending on the value of the IQ Power Edge Slope parameter. The value is expressed in dB if IQ Power Edge Level Type is set to Relative or in dBm if it is set to Absolute. The default of this parameter is hardware dependent. |
| triggerDelay | [in] | float64 | This parameter specifies the trigger delay time. This value is expressed in seconds. The default value is 0. |
| minimumQuietTimeMode | [in] | int32 | This parameter specifies whether the measurement computes the minimum quiet time used for triggering. The default value is Auto.Name (value)DescriptionManual (0)The measurement uses the minimum quiet time value you specify using the Minimum Quiet Time parameter.Auto (1)The measurement calculates the minimum quiet time used for triggering. |
| Name (value) | Description |  |  |
| Manual (0) | The measurement uses the minimum quiet time value you specify using the Minimum Quiet Time parameter. |  |  |
| Auto (1) | The measurement calculates the minimum quiet time used for triggering. |  |  |
| minimumQuietTime | [in] | float64 | This parameter specifies the duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. This value is expressed in seconds. If you set the IQ Power Edge Slope parameter to Rising Slope, the signal is quiet when it is below the trigger level. If you set the IQ Power Edge Slope parameter to Falling Slope, the signal is quiet when it is above the trigger level. The default of this parameter is hardware dependent. |
| iqPowerEdgeLevelType | [in] | int32 | This parameter specifies the reference for the IQ Power Edge Level parameter. This parameter is used only when you set the RFMXTDSCDMA_ATTR_TRIGGER_TYPE attribute to IQ Power Edge. The default value is Relative.Name (value)DescriptionRelative (0)The IQ Power Edge Level is relative to the reference level.Absolute (1)The IQ Power Edge Level specifies the absolute power. |
| Name (value) | Description |  |  |
| Relative (0) | The IQ Power Edge Level is relative to the reference level. |  |  |
| Absolute (1) | The IQ Power Edge Level specifies the absolute power. |  |  |
| enableTrigger | [in] | int32 | This parameter specifies whether to enable the trigger. The default value is TRUE. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Trigger

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration__trigger_1gafae8a24ed0a49eb8af47bc9c345434d2.html language=enus -->
## TOPIC 00211: RFmxTDSCDMA_CfgDigitalEdgeTrigger

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration__trigger_1gafae8a24ed0a49eb8af47bc9c345434d2.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__configuration__trigger_1gafae8a24ed0a49eb8af47bc9c345434d2.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the device to wait for a digital edge trigger to mark a reference point within the record. Syntaxint32 __stdcall RFmxTDSCDMA_CfgDigitalEdgeTrigger(niRFmxInstrHandle instrumentHandle, char selectorString[], char digitalEdgeSource[], int32 digitalEdge, float64 triggerDelay, int32 enableTrig

### RFmxTDSCDMA_CfgDigitalEdgeTrigger

Configures the device to wait for a digital edge trigger to mark a reference point within the record.

#### Syntax

int32 __stdcall RFmxTDSCDMA_CfgDigitalEdgeTrigger(niRFmxInstrHandle instrumentHandle, char selectorString[], char digitalEdgeSource[], int32 digitalEdge, float64 triggerDelay, int32 enableTrigger)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Examples:"""signal::sig1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| digitalEdgeSource | [in] | char[] | This parameter specifies the source terminal for the digital edge trigger. The default of this parameter is hardware dependent.Name (Value)DescriptionPFI0 (PFI0)The trigger is received on PFI 0.PFI1 (PFI1)The trigger is received on PFI 1.PXI_Trig0 (PXI_Trig0)The trigger is received on PXI trigger line 0.PXI_Trig1 (PXI_Trig1)The trigger is received on PXI trigger line 1.PXI_Trig2 (PXI_Trig2)The trigger is received on PXI trigger line 2.PXI_Trig3 (PXI_Trig3)The trigger is received on PXI trigger line 3.PXI_Trig4 (PXI_Trig4)The trigger is received on PXI trigger line 4.PXI_Trig5 (PXI_Trig5)The trigger is received on PXI trigger line 5.PXI_Trig6 (PXI_Trig6)The trigger is received on PXI trigger line 6.PXI_Trig7 (PXI_Trig7)The trigger is received on PXI trigger line 7.PXI_STAR (PXI_STAR)The trigger is received on the PXI star trigger line.PXIe_DStarB (PXIe_DStarB)The trigger is received on the PXIe DStar B trigger line. |
| Name (Value) | Description |  |  |
| PFI0 (PFI0) | The trigger is received on PFI 0. |  |  |
| PFI1 (PFI1) | The trigger is received on PFI 1. |  |  |
| PXI_Trig0 (PXI_Trig0) | The trigger is received on PXI trigger line 0. |  |  |
| PXI_Trig1 (PXI_Trig1) | The trigger is received on PXI trigger line 1. |  |  |
| PXI_Trig2 (PXI_Trig2) | The trigger is received on PXI trigger line 2. |  |  |
| PXI_Trig3 (PXI_Trig3) | The trigger is received on PXI trigger line 3. |  |  |
| PXI_Trig4 (PXI_Trig4) | The trigger is received on PXI trigger line 4. |  |  |
| PXI_Trig5 (PXI_Trig5) | The trigger is received on PXI trigger line 5. |  |  |
| PXI_Trig6 (PXI_Trig6) | The trigger is received on PXI trigger line 6. |  |  |
| PXI_Trig7 (PXI_Trig7) | The trigger is received on PXI trigger line 7. |  |  |
| PXI_STAR (PXI_STAR) | The trigger is received on the PXI star trigger line. |  |  |
| PXIe_DStarB (PXIe_DStarB) | The trigger is received on the PXIe DStar B trigger line. |  |  |
| digitalEdge | [in] | int32 | This parameter specifies the trigger edge to detect. The default value is Rising Edge.Name (value)DescriptionRising Edge (0)The trigger asserts on the rising edge of the signal.Falling Edge (1)The trigger asserts on the falling edge of the signal. |
| Name (value) | Description |  |  |
| Rising Edge (0) | The trigger asserts on the rising edge of the signal. |  |  |
| Falling Edge (1) | The trigger asserts on the falling edge of the signal. |  |  |
| triggerDelay | [in] | float64 | This parameter specifies the trigger delay time. This value is expressed in seconds. The default value is 0. |
| enableTrigger | [in] | int32 | This parameter specifies whether to enable the trigger. The default value is TRUE. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Trigger

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch.html language=enus -->
## TOPIC 00212: Fetch

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsACPCDACHPModAccOBWPVTSEMSlotPowerGroup membersNoneAttachmentsNone

### Fetch

#### Groups

- ACP
- CDA
- CHP
- ModAcc
- OBW
- PVT
- SEM
- SlotPower

#### Group members

None

#### Attachments

None

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__acp.html language=enus -->
## TOPIC 00213: ACP

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__acp.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__acp.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxTDSCDMA_ACPFetchAbsolutePowersTraceFetches the absolute powers trace for ACP measurement. RFmxTDSCDMA_ACPFetchCarrierAbsolutePowerReturns the absolute carrier power. RFmxTDSCDMA_ACPFetchOffsetMeasurementReturns the absolute and relative powers measured in th

### ACP

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxTDSCDMA_ACPFetchAbsolutePowersTrace | Fetches the absolute powers trace for ACP measurement. |
| RFmxTDSCDMA_ACPFetchCarrierAbsolutePower | Returns the absolute carrier power. |
| RFmxTDSCDMA_ACPFetchOffsetMeasurement | Returns the absolute and relative powers measured in the offset channel. The relative powers are measured relative to the integrated power of the power reference carrier. |
| RFmxTDSCDMA_ACPFetchOffsetMeasurementArray | Returns the absolute and relative powers measured in the offset channel. The relative powers are measured relative to the integrated power of the power reference carrier. |
| RFmxTDSCDMA_ACPFetchRelativePowersTrace | Fetches the relative powers trace for the ACP measurement. |
| RFmxTDSCDMA_ACPFetchSpectrum | Fetches the spectrum used for the ACP measurement. |

#### Attachments

None

Parent topic:

Fetch

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__acp_1ga27aba01143e5aea1f69aa348dcff85d0.html language=enus -->
## TOPIC 00214: RFmxTDSCDMA_ACPFetchOffsetMeasurement

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__acp_1ga27aba01143e5aea1f69aa348dcff85d0.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__acp_1ga27aba01143e5aea1f69aa348dcff85d0.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the absolute and relative powers measured in the offset channel. The relative powers are measured relative to the integrated power of the power reference carrier. Syntaxint32 __stdcall RFmxTDSCDMA_ACPFetchOffsetMeasurement(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 ti

### RFmxTDSCDMA_ACPFetchOffsetMeasurement

Returns the absolute and relative powers measured in the offset channel. The relative powers are measured relative to the integrated power of the power reference carrier.

#### Syntax

int32 __stdcall RFmxTDSCDMA_ACPFetchOffsetMeasurement(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *lowerRelativePower, float64 *upperRelativePower, float64 *lowerAbsolutePower, float64 *upperAbsolutePower)

#### Remarks

Use "offset<n>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, and offset number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used.Examples:"offset0""signal::sig1/offset0""result::r1/offset0""signal::sig1/result::r1/offset0"You can use the RFmxTDSCDMA_BuildOffsetString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| lowerRelativePower | [out] | float64 * | This parameter returns the lower offset channel power measured relative to the integrated power of the carrier. This value is expressed in dB. |
| upperRelativePower | [out] | float64 * | This parameter returns the upper offset channel power measured relative to the integrated power of the carrier. This value is expressed in dB. |
| lowerAbsolutePower | [out] | float64 * | This parameter returns the lower offset channel absolute power. This value is expressed in dBm. |
| upperAbsolutePower | [out] | float64 * | This parameter returns the upper offset channel absolute power. This value is expressed in dBm. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ACP

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__acp_1ga5f77670d8f867ad4b0b410addc6c9ccf.html language=enus -->
## TOPIC 00215: RFmxTDSCDMA_ACPFetchAbsolutePowersTrace

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__acp_1ga5f77670d8f867ad4b0b410addc6c9ccf.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__acp_1ga5f77670d8f867ad4b0b410addc6c9ccf.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the absolute powers trace for ACP measurement. Syntaxint32 __stdcall RFmxTDSCDMA_ACPFetchAbsolutePowersTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 traceIndex, float64 *x0, float64 *dx, float32 absolutePowersTrace[], int32 arraySize, int32 *actualAr

### RFmxTDSCDMA_ACPFetchAbsolutePowersTrace

Fetches the absolute powers trace for ACP measurement.

#### Syntax

int32 __stdcall RFmxTDSCDMA_ACPFetchAbsolutePowersTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 traceIndex, float64 *x0, float64 *dx, float32 absolutePowersTrace[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| traceIndex | [in] | int32 | Specifies the index of the trace to fetch. The traceIndex can range from 0 to (Number of carriers + 2*Number of offsets). |
| x0 | [out] | float64 * | This parameter returns the start frequency of the trace. This value is expressed in Hz. |
| dx | [out] | float64 * | This parameter returns the frequency bin spacing of the trace. This value is expressed in Hz. |
| absolutePowersTrace | [out] | float32[] | This parameter returns the absolute power trace measured in each channel. This value is expressed in dB. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ACP

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__acp_1ga61c5fecf78835a84b41a4647dce9235d.html language=enus -->
## TOPIC 00216: RFmxTDSCDMA_ACPFetchSpectrum

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__acp_1ga61c5fecf78835a84b41a4647dce9235d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__acp_1ga61c5fecf78835a84b41a4647dce9235d.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the spectrum used for the ACP measurement. Syntaxint32 __stdcall RFmxTDSCDMA_ACPFetchSpectrum(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 spectrum[], int32 arraySize, int32 *actualArraySize)ParametersNameDirectionTypeDescripti

### RFmxTDSCDMA_ACPFetchSpectrum

Fetches the spectrum used for the ACP measurement.

#### Syntax

int32 __stdcall RFmxTDSCDMA_ACPFetchSpectrum(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 spectrum[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| x0 | [out] | float64 * | This parameter returns the start frequency. This value is expressed in Hz. |
| dx | [out] | float64 * | This parameter returns the frequency bin spacing. This value is expressed in Hz. |
| spectrum | [out] | float32[] | This parameter returns the averaged power measured at each frequency bin. This value is expressed in dBm. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ACP

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__acp_1ga702ccb25392fb246cf6b0d3424c69fd2.html language=enus -->
## TOPIC 00217: RFmxTDSCDMA_ACPFetchRelativePowersTrace

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__acp_1ga702ccb25392fb246cf6b0d3424c69fd2.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__acp_1ga702ccb25392fb246cf6b0d3424c69fd2.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the relative powers trace for the ACP measurement. Syntaxint32 __stdcall RFmxTDSCDMA_ACPFetchRelativePowersTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 traceIndex, float64 *x0, float64 *dx, float32 relativePowersTrace[], int32 arraySize, int32 *actu

### RFmxTDSCDMA_ACPFetchRelativePowersTrace

Fetches the relative powers trace for the ACP measurement.

#### Syntax

int32 __stdcall RFmxTDSCDMA_ACPFetchRelativePowersTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 traceIndex, float64 *x0, float64 *dx, float32 relativePowersTrace[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| traceIndex | [in] | int32 | Specifies the index of the trace to fetch. The traceIndex can range from 0 to (Number of carriers + 2*Number of offsets). |
| x0 | [out] | float64 * | This parameter returns the start frequency of the trace. This value is expressed in Hz. |
| dx | [out] | float64 * | This parameter returns the frequency bin spacing. This value is expressed in Hz. |
| relativePowersTrace | [out] | float32[] | This parameter returns the relative power measured in each channel relative to power reference carrier. This value is expressed in dB. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ACP

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__acp_1gaa830e8e922f07509b13d86e7fad62529.html language=enus -->
## TOPIC 00218: RFmxTDSCDMA_ACPFetchCarrierAbsolutePower

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__acp_1gaa830e8e922f07509b13d86e7fad62529.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__acp_1gaa830e8e922f07509b13d86e7fad62529.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the absolute carrier power. Syntaxint32 __stdcall RFmxTDSCDMA_ACPFetchCarrierAbsolutePower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *carrierAbsolutePower)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter speci

### RFmxTDSCDMA_ACPFetchCarrierAbsolutePower

Returns the absolute carrier power.

#### Syntax

int32 __stdcall RFmxTDSCDMA_ACPFetchCarrierAbsolutePower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *carrierAbsolutePower)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| carrierAbsolutePower | [out] | float64 * | This parameter returns the absolute measured carrier power. This value is expressed in dBm. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ACP

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__acp_1gad0dc25139486f4664a1d8dcabf5981ad.html language=enus -->
## TOPIC 00219: RFmxTDSCDMA_ACPFetchOffsetMeasurementArray

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__acp_1gad0dc25139486f4664a1d8dcabf5981ad.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__acp_1gad0dc25139486f4664a1d8dcabf5981ad.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the absolute and relative powers measured in the offset channel. The relative powers are measured relative to the integrated power of the power reference carrier. Syntaxint32 __stdcall RFmxTDSCDMA_ACPFetchOffsetMeasurementArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float

### RFmxTDSCDMA_ACPFetchOffsetMeasurementArray

Returns the absolute and relative powers measured in the offset channel. The relative powers are measured relative to the integrated power of the power reference carrier.

#### Syntax

int32 __stdcall RFmxTDSCDMA_ACPFetchOffsetMeasurementArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 lowerRelativePower[], float64 upperRelativePower[], float64 lowerAbsolutePower[], float64 upperAbsolutePower[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| lowerRelativePower | [out] | float64[] | This parameter returns the array of lower offset channel powers measured relative to the integrated power of the carrier. This value is expressed in dB. |
| upperRelativePower | [out] | float64[] | This parameter returns the array of upper offset channel powers measured relative to the integrated power of the carrier. This value is expressed in dB. |
| lowerAbsolutePower | [out] | float64[] | This parameter returns the array of lower offset channel powers. This value is expressed in dBm. |
| upperAbsolutePower | [out] | float64[] | This parameter returns the array of upper offset channel powers. This value is expressed in dBm. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ACP

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__cda.html language=enus -->
## TOPIC 00220: CDA

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__cda.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__cda.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxTDSCDMA_CDAFetchCodeDomainPowerFetches the scalar code domain measurement results. RFmxTDSCDMA_CDAFetchIQImpairmentsReturns the I/Q origin offset, I/Q gain imbalance, and I/Q quadrature error. RFmxTDSCDMA_CDAFetchMaximumCodeDomainPowerTraceFetches the maximu

### CDA

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxTDSCDMA_CDAFetchCodeDomainPower | Fetches the scalar code domain measurement results. |
| RFmxTDSCDMA_CDAFetchIQImpairments | Returns the I/Q origin offset, I/Q gain imbalance, and I/Q quadrature error. |
| RFmxTDSCDMA_CDAFetchMaximumCodeDomainPowerTrace | Fetches the maximum hold trace of the power measured in the code domain of the base spreading factor. |
| RFmxTDSCDMA_CDAFetchMaximumSymbolEVMTrace | Fetches the maximum hold trace of the symbol EVM for the code domain analysis (CDA) measurement. |
| RFmxTDSCDMA_CDAFetchMaximumSymbolMagnitudeErrorTrace | Returns the maximum hold trace of the symbol magnitude error for the code domain analysis (CDA) measurement. |
| RFmxTDSCDMA_CDAFetchMaximumSymbolPhaseErrorTrace | Fetches the maximum hold trace of the symbol phase error for the code domain analysis (CDA) measurement. |
| RFmxTDSCDMA_CDAFetchMeanCodeDomainPowerTrace | Fetches the averaged trace value of the code powers measured in the code domain of the base spreading factor. |
| RFmxTDSCDMA_CDAFetchMeanSymbolEVMTrace | Fetches the averaged symbol EVM trace of the code domain analysis (CDA) measurement channel. |
| RFmxTDSCDMA_CDAFetchMeanSymbolMagnitudeErrorTrace | Fetches the averaged symbol magnitude error trace for the code domain analysis (CDA) measurement. |
| RFmxTDSCDMA_CDAFetchMeanSymbolPhaseErrorTrace | Fetches the averaged symbol phase error trace for the code domain analysis (CDA) measurement. |
| RFmxTDSCDMA_CDAFetchSymbolConstellationTrace | Fetches the symbol constellation trace of the code domain analysis (CDA) measurement channel. |
| RFmxTDSCDMA_CDAFetchSymbolConstellationTraceSplit | Fetches the symbol constellation trace of the code domain analysis (CDA) measurement channel. |
| RFmxTDSCDMA_CDAFetchSymbolEVM | Fetches the ModAcc related measurements for the configured measurement channel. |

#### Attachments

None

Parent topic:

Fetch

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__cda_1ga2e22b3419631f42137ff36302e6913f6.html language=enus -->
## TOPIC 00221: RFmxTDSCDMA_CDAFetchIQImpairments

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__cda_1ga2e22b3419631f42137ff36302e6913f6.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__cda_1ga2e22b3419631f42137ff36302e6913f6.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the I/Q origin offset, I/Q gain imbalance, and I/Q quadrature error. Syntaxint32 __stdcall RFmxTDSCDMA_CDAFetchIQImpairments(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *iqOriginOffset, float64 *iqGainImbalance, float64 *iqQuadratureError)ParametersNam

### RFmxTDSCDMA_CDAFetchIQImpairments

Returns the I/Q origin offset, I/Q gain imbalance, and I/Q quadrature error.

#### Syntax

int32 __stdcall RFmxTDSCDMA_CDAFetchIQImpairments(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *iqOriginOffset, float64 *iqGainImbalance, float64 *iqQuadratureError)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| iqOriginOffset | [out] | float64 * | This parameter returns the I/Q origin offset of the composite signal, averaged over all measured slots. This value is expressed in dB. |
| iqGainImbalance | [out] | float64 * | This parameter returns the I/Q gain imbalance of the composite signal, averaged over all measured slots. This value is expressed in dB. |
| iqQuadratureError | [out] | float64 * | This parameter returns the I/Q quadrature error of the composite signal, averaged over all measured slots. This value is expressed in degrees. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

CDA

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__cda_1ga444e32055fb1927d60301226f1d5985a.html language=enus -->
## TOPIC 00222: RFmxTDSCDMA_CDAFetchMaximumSymbolPhaseErrorTrace

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__cda_1ga444e32055fb1927d60301226f1d5985a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__cda_1ga444e32055fb1927d60301226f1d5985a.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the maximum hold trace of the symbol phase error for the code domain analysis (CDA) measurement. Syntaxint32 __stdcall RFmxTDSCDMA_CDAFetchMaximumSymbolPhaseErrorTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 maximumSymbolPhaseError[], int32 arraySi

### RFmxTDSCDMA_CDAFetchMaximumSymbolPhaseErrorTrace

Fetches the maximum hold trace of the symbol phase error for the code domain analysis (CDA) measurement.

#### Syntax

int32 __stdcall RFmxTDSCDMA_CDAFetchMaximumSymbolPhaseErrorTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 maximumSymbolPhaseError[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| maximumSymbolPhaseError | [out] | float32[] | This parameter returns an array of the maximum hold traces of the symbol phase error for the CDA measurement. This value is expressed in degrees. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

CDA

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__cda_1ga4611b3cf1e35e8bdcd32ae122e1ffa60.html language=enus -->
## TOPIC 00223: RFmxTDSCDMA_CDAFetchSymbolEVM

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__cda_1ga4611b3cf1e35e8bdcd32ae122e1ffa60.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__cda_1ga4611b3cf1e35e8bdcd32ae122e1ffa60.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the ModAcc related measurements for the configured measurement channel. Syntaxint32 __stdcall RFmxTDSCDMA_CDAFetchSymbolEVM(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *meanRMSSymbolEVM, float64 *maximumPeakSymbolEVM, float64 *frequencyError, float64 *

### RFmxTDSCDMA_CDAFetchSymbolEVM

Fetches the ModAcc related measurements for the configured measurement channel.

#### Syntax

int32 __stdcall RFmxTDSCDMA_CDAFetchSymbolEVM(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *meanRMSSymbolEVM, float64 *maximumPeakSymbolEVM, float64 *frequencyError, float64 *chipRateError, float64 *meanRMSSymbolMagnitudeError, float64 *meanRMSSymbolPhaseError, float64 *meanSymbolPower)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| meanRMSSymbolEVM | [out] | float64 * | This parameter returns the RMS symbol EVM for the selected time slot and channel, averaged over all averaging iterations. This value is expressed as a percentage. |
| maximumPeakSymbolEVM | [out] | float64 * | This parameter returns the maximum value of the peak symbol EVMs, among all averaging iterations for the selected time slot and channel. This value is expressed as a percentage. |
| frequencyError | [out] | float64 * | This parameter returns the frequency error averaged over all measured slots. This value is expressed in Hz. |
| chipRateError | [out] | float64 * | This parameter returns the chip rate error. This value is expressed in ppm. |
| meanRMSSymbolMagnitudeError | [out] | float64 * | This parameter returns the RMS symbol magnitude error for the selected time slot and channel, averaged over all averaging iterations. This value is expressed as a percentage. |
| meanRMSSymbolPhaseError | [out] | float64 * | This parameter returns the RMS symbol phase error for the selected time slot and channel, averaged over all averaging iterations. This value is expressed in degrees. |
| meanSymbolPower | [out] | float64 * | This parameter returns the mean symbol power for the selected time slot and channel. This value is expressed in dB if you set the RFMXTDSCDMA_ATTR_CDA_POWER_UNIT attribute to dB, and in dBm if you set the CDA Pwr Unit attribute to dBm. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

CDA

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__cda_1ga526c53a6d9bbf1de0d71e9fabf031b0e.html language=enus -->
## TOPIC 00224: RFmxTDSCDMA_CDAFetchMaximumCodeDomainPowerTrace

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__cda_1ga526c53a6d9bbf1de0d71e9fabf031b0e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__cda_1ga526c53a6d9bbf1de0d71e9fabf031b0e.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the maximum hold trace of the power measured in the code domain of the base spreading factor. Syntaxint32 __stdcall RFmxTDSCDMA_CDAFetchMaximumCodeDomainPowerTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 maximumCodeDomainPowers[], int32 arraySize,

### RFmxTDSCDMA_CDAFetchMaximumCodeDomainPowerTrace

Fetches the maximum hold trace of the power measured in the code domain of the base spreading factor.

#### Syntax

int32 __stdcall RFmxTDSCDMA_CDAFetchMaximumCodeDomainPowerTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 maximumCodeDomainPowers[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| maximumCodeDomainPowers | [out] | float32[] | This parameter returns an array of the max hold traces of the code powers measured in the code domain of the base spreading factor. This value is expressed in dB. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

CDA

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__cda_1ga5ab983861375e6d739da90e139a3665d.html language=enus -->
## TOPIC 00225: RFmxTDSCDMA_CDAFetchMeanCodeDomainPowerTrace

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__cda_1ga5ab983861375e6d739da90e139a3665d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__cda_1ga5ab983861375e6d739da90e139a3665d.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the averaged trace value of the code powers measured in the code domain of the base spreading factor. Syntaxint32 __stdcall RFmxTDSCDMA_CDAFetchMeanCodeDomainPowerTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 meanCodeDomainPowers[], int32 arraySize

### RFmxTDSCDMA_CDAFetchMeanCodeDomainPowerTrace

Fetches the averaged trace value of the code powers measured in the code domain of the base spreading factor.

#### Syntax

int32 __stdcall RFmxTDSCDMA_CDAFetchMeanCodeDomainPowerTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 meanCodeDomainPowers[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| meanCodeDomainPowers | [out] | float32[] | This parameter returns an array of the averaged code power traces measured in the code domain of the base spreading factor. This value is expressed in dBm. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

CDA

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__cda_1ga711fd5c25f26a27126d0abeb860636f9.html language=enus -->
## TOPIC 00226: RFmxTDSCDMA_CDAFetchMeanSymbolEVMTrace

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__cda_1ga711fd5c25f26a27126d0abeb860636f9.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__cda_1ga711fd5c25f26a27126d0abeb860636f9.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the averaged symbol EVM trace of the code domain analysis (CDA) measurement channel. Syntaxint32 __stdcall RFmxTDSCDMA_CDAFetchMeanSymbolEVMTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 meanSymbolEVM[], int32 arraySize, int32 *actualArraySize)Param

### RFmxTDSCDMA_CDAFetchMeanSymbolEVMTrace

Fetches the averaged symbol EVM trace of the code domain analysis (CDA) measurement channel.

#### Syntax

int32 __stdcall RFmxTDSCDMA_CDAFetchMeanSymbolEVMTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 meanSymbolEVM[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| meanSymbolEVM | [out] | float32[] | This parameter returns an array of the averaged symbol EVM traces for the configured measurement channel. This value is expressed as a percentage. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

CDA

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__cda_1ga89babf87a9db2ecd89b165e8605ea7ae.html language=enus -->
## TOPIC 00227: RFmxTDSCDMA_CDAFetchMaximumSymbolMagnitudeErrorTrace

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__cda_1ga89babf87a9db2ecd89b165e8605ea7ae.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__cda_1ga89babf87a9db2ecd89b165e8605ea7ae.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum hold trace of the symbol magnitude error for the code domain analysis (CDA) measurement. Syntaxint32 __stdcall RFmxTDSCDMA_CDAFetchMaximumSymbolMagnitudeErrorTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 maximumSymbolMagnitudeError[], i

### RFmxTDSCDMA_CDAFetchMaximumSymbolMagnitudeErrorTrace

Returns the maximum hold trace of the symbol magnitude error for the code domain analysis (CDA) measurement.

#### Syntax

int32 __stdcall RFmxTDSCDMA_CDAFetchMaximumSymbolMagnitudeErrorTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 maximumSymbolMagnitudeError[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| maximumSymbolMagnitudeError | [out] | float32[] | This parameter returns an array of the maximum hold traces of the symbol magnitude error for the CDA measurement. This value is expressed as a percentage. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

CDA

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__cda_1gadf4f2b0a9015b74552dc027fa10787a8.html language=enus -->
## TOPIC 00228: RFmxTDSCDMA_CDAFetchMeanSymbolMagnitudeErrorTrace

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__cda_1gadf4f2b0a9015b74552dc027fa10787a8.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__cda_1gadf4f2b0a9015b74552dc027fa10787a8.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the averaged symbol magnitude error trace for the code domain analysis (CDA) measurement. Syntaxint32 __stdcall RFmxTDSCDMA_CDAFetchMeanSymbolMagnitudeErrorTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 meanSymbolMagnitudeError[], int32 arraySize, i

### RFmxTDSCDMA_CDAFetchMeanSymbolMagnitudeErrorTrace

Fetches the averaged symbol magnitude error trace for the code domain analysis (CDA) measurement.

#### Syntax

int32 __stdcall RFmxTDSCDMA_CDAFetchMeanSymbolMagnitudeErrorTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 meanSymbolMagnitudeError[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| meanSymbolMagnitudeError | [out] | float32[] | This parameter returns an array of the averaged symbol magnitude error traces for the configured measurement channel. This value is expressed as a percentage. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

CDA

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__cda_1gaebdcc35b62da8a832123694af2b66808.html language=enus -->
## TOPIC 00229: RFmxTDSCDMA_CDAFetchMeanSymbolPhaseErrorTrace

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__cda_1gaebdcc35b62da8a832123694af2b66808.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__cda_1gaebdcc35b62da8a832123694af2b66808.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the averaged symbol phase error trace for the code domain analysis (CDA) measurement. Syntaxint32 __stdcall RFmxTDSCDMA_CDAFetchMeanSymbolPhaseErrorTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 meanSymbolPhaseError[], int32 arraySize, int32 *actual

### RFmxTDSCDMA_CDAFetchMeanSymbolPhaseErrorTrace

Fetches the averaged symbol phase error trace for the code domain analysis (CDA) measurement.

#### Syntax

int32 __stdcall RFmxTDSCDMA_CDAFetchMeanSymbolPhaseErrorTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 meanSymbolPhaseError[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| meanSymbolPhaseError | [out] | float32[] | This parameter returns an array of the averaged symbol phase error traces for the configured measurement channel. This value is expressed in degrees. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

CDA

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__cda_1gaeead0c8115354ef6f0cd04c39ff2838f.html language=enus -->
## TOPIC 00230: RFmxTDSCDMA_CDAFetchMaximumSymbolEVMTrace

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__cda_1gaeead0c8115354ef6f0cd04c39ff2838f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__cda_1gaeead0c8115354ef6f0cd04c39ff2838f.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the maximum hold trace of the symbol EVM for the code domain analysis (CDA) measurement. Syntaxint32 __stdcall RFmxTDSCDMA_CDAFetchMaximumSymbolEVMTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 maximumSymbolEVM[], int32 arraySize, int32 *actualArray

### RFmxTDSCDMA_CDAFetchMaximumSymbolEVMTrace

Fetches the maximum hold trace of the symbol EVM for the code domain analysis (CDA) measurement.

#### Syntax

int32 __stdcall RFmxTDSCDMA_CDAFetchMaximumSymbolEVMTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 maximumSymbolEVM[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| maximumSymbolEVM | [out] | float32[] | This parameter returns an array of the maximum hold traces of the symbol EVM for the CDA measurement. This value is expressed as a percentage. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

CDA

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__cda_1gaef669d6de69667cc7a634d967a7142cc.html language=enus -->
## TOPIC 00231: RFmxTDSCDMA_CDAFetchSymbolConstellationTrace

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__cda_1gaef669d6de69667cc7a634d967a7142cc.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__cda_1gaef669d6de69667cc7a634d967a7142cc.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the symbol constellation trace of the code domain analysis (CDA) measurement channel. Syntaxint32 __stdcall RFmxTDSCDMA_CDAFetchSymbolConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle symbolConstellation[], int32 arraySize, int32 *

### RFmxTDSCDMA_CDAFetchSymbolConstellationTrace

Fetches the symbol constellation trace of the code domain analysis (CDA) measurement channel.

#### Syntax

int32 __stdcall RFmxTDSCDMA_CDAFetchSymbolConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle symbolConstellation[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| symbolConstellation | [out] | NIComplexSingle[] | This parameter returns an array of the symbol constellation traces of the configured measurement channel. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

CDA

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__cda_1gaf0a04014edf7eb17ff94bd1485fb8e0b.html language=enus -->
## TOPIC 00232: RFmxTDSCDMA_CDAFetchSymbolConstellationTraceSplit

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__cda_1gaf0a04014edf7eb17ff94bd1485fb8e0b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__cda_1gaf0a04014edf7eb17ff94bd1485fb8e0b.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the symbol constellation trace of the code domain analysis (CDA) measurement channel. Syntaxint32 __stdcall RFmxTDSCDMA_CDAFetchSymbolConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 symbolConstellationI[], float32 symbolConstellatio

### RFmxTDSCDMA_CDAFetchSymbolConstellationTraceSplit

Fetches the symbol constellation trace of the code domain analysis (CDA) measurement channel.

#### Syntax

int32 __stdcall RFmxTDSCDMA_CDAFetchSymbolConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 symbolConstellationI[], float32 symbolConstellationQ[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| symbolConstellationI | [out] | float32[] | This parameter returns an array of the symbol constellation traces of the configured measurement channel. |
| symbolConstellationQ | [out] | float32[] | This parameter returns an array of the symbol constellation traces of the configured measurement channel. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

CDA

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__cda_1gafda5c80cbde62431ce9d4023b16b8fb0.html language=enus -->
## TOPIC 00233: RFmxTDSCDMA_CDAFetchCodeDomainPower

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__cda_1gafda5c80cbde62431ce9d4023b16b8fb0.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__cda_1gafda5c80cbde62431ce9d4023b16b8fb0.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the scalar code domain measurement results. Syntaxint32 __stdcall RFmxTDSCDMA_CDAFetchCodeDomainPower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *meanTotalPower, float64 *meanTotalActivePower, float64 *meanActivePower, float64 *maximumPeakActivePower,

### RFmxTDSCDMA_CDAFetchCodeDomainPower

Fetches the scalar code domain measurement results.

#### Syntax

int32 __stdcall RFmxTDSCDMA_CDAFetchCodeDomainPower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *meanTotalPower, float64 *meanTotalActivePower, float64 *meanActivePower, float64 *maximumPeakActivePower, float64 *meanInactivePower, float64 *maximumPeakInactivePower)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| meanTotalPower | [out] | float64 * | This parameter returns the total power measured in the code domain of the base spreading factor, averaged over all averaging iterations. This value is expressed in dBm. |
| meanTotalActivePower | [out] | float64 * | This parameter returns the total active code power measured in the code domain of the base spreading factor, normalized to the total code domain power (CDP). This value is expressed in dB, if you set the RFMXTDSCDMA_ATTR_CDA_POWER_UNIT attribute to dB, or in dBm, if you set the CDA Pwr Unit attribute to dBm. |
| meanActivePower | [out] | float64 * | This parameter returns the average of the active code power measured in the code domain of the base spreading factor, normalized to the total CDP. This value is expressed in dB, if you set the CDA Pwr Unit attribute to dB, or in dBm, if you set the CDA Pwr Unit attribute to dBm. |
| maximumPeakActivePower | [out] | float64 * | This parameter returns the maximum value among all averaging iterations of the maximum active code power measured in the code domain of the base spreading factor, normalized to the total CDP. This value is expressed in dB, if you set the CDA Pwr Unit attribute to dB, or in dBm, if you set the CDA Pwr Unit attribute to dBm. |
| meanInactivePower | [out] | float64 * | This parameter returns the average of the code power measured among the set of inactive channels in the code domain of the base spreading factor, normalized to the total CDP. This value is expressed in dB, if you set the CDA Pwr Unit attribute to dB, or in dBm, if you set the CDA Pwr Unit attribute to dBm. |
| maximumPeakInactivePower | [out] | float64 * | This parameter returns the maximum value among all averaging iterations of the highest measured code power among the set of inactive channels in the code domain of the base spreading factor, normalized to the total CDP. This value is expressed in dB, if you set the CDA Pwr Unit attribute to dB, or in dBm, if you set the CDA Pwr Unit attribute to dBm. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

CDA

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__chp_1ga7cf721719f0d569ad932c4ad85d69422.html language=enus -->
## TOPIC 00234: RFmxTDSCDMA_CHPFetchSpectrum

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__chp_1ga7cf721719f0d569ad932c4ad85d69422.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__chp_1ga7cf721719f0d569ad932c4ad85d69422.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the spectrum used for the CHP measurement. Syntaxint32 __stdcall RFmxTDSCDMA_CHPFetchSpectrum(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 spectrum[], int32 arraySize, int32 *actualArraySize)ParametersNameDirectionTypeDescripti

### RFmxTDSCDMA_CHPFetchSpectrum

Fetches the spectrum used for the CHP measurement.

#### Syntax

int32 __stdcall RFmxTDSCDMA_CHPFetchSpectrum(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 spectrum[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| x0 | [out] | float64 * | This parameter returns the start frequency. This value is expressed in Hz. |
| dx | [out] | float64 * | This parameter returns the frequency bin spacing. This value is expressed in Hz. |
| spectrum | [out] | float32[] | This parameter returns the averaged power measured at each frequency bin. This value is expressed in dBm. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

CHP

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__modacc_1ga0e3000a15b04255682f3bece6d8e741c.html language=enus -->
## TOPIC 00235: RFmxTDSCDMA_ModAccFetchMaximumCodeDomainErrorTrace

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__modacc_1ga0e3000a15b04255682f3bece6d8e741c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__modacc_1ga0e3000a15b04255682f3bece6d8e741c.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the maximum code domain error trace among all active time slots and averaging iterations for the ModAcc measurement. Syntaxint32 __stdcall RFmxTDSCDMA_ModAccFetchMaximumCodeDomainErrorTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 maximumCodeDomainE

### RFmxTDSCDMA_ModAccFetchMaximumCodeDomainErrorTrace

Fetches the maximum code domain error trace among all active time slots and averaging iterations for the ModAcc measurement.

#### Syntax

int32 __stdcall RFmxTDSCDMA_ModAccFetchMaximumCodeDomainErrorTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 maximumCodeDomainError[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| maximumCodeDomainError | [out] | float32[] | This parameter returns an array of the maximum code domain error traces among all active time slots and averaging iterations. This value is expressed in dB. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__modacc_1ga12aeb5803f33c6dd929e887e82baf76e.html language=enus -->
## TOPIC 00236: RFmxTDSCDMA_ModAccFetchMaximumMagnitudeErrorTrace

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__modacc_1ga12aeb5803f33c6dd929e887e82baf76e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__modacc_1ga12aeb5803f33c6dd929e887e82baf76e.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the maximum magnitude error trace on the chip level. Syntaxint32 __stdcall RFmxTDSCDMA_ModAccFetchMaximumMagnitudeErrorTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 maximumMagnitudeError[], int32 arraySize, int32 *actualAr

### RFmxTDSCDMA_ModAccFetchMaximumMagnitudeErrorTrace

Fetches the maximum magnitude error trace on the chip level.

#### Syntax

int32 __stdcall RFmxTDSCDMA_ModAccFetchMaximumMagnitudeErrorTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 maximumMagnitudeError[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| x0 | [out] | float64 * | This parameter returns the start time of the trace. This value is expressed in seconds. |
| dx | [out] | float64 * | This parameter returns the sampling time of the trace. This value is expressed in seconds. |
| maximumMagnitudeError | [out] | float32[] | This parameter returns an array of maximum magnitude error trace on the chip level. This value is expressed as a percentage. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__modacc_1ga180e1867224e5a19628af29e3febd593.html language=enus -->
## TOPIC 00237: RFmxTDSCDMA_ModAccFetchDataRCDE

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__modacc_1ga180e1867224e5a19628af29e3febd593.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__modacc_1ga180e1867224e5a19628af29e3febd593.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum value of the measured data relative code domain error (RCDE), along with the spreading factor and the channelization code of the corresponding channel. Syntaxint32 __stdcall RFmxTDSCDMA_ModAccFetchDataRCDE(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout

### RFmxTDSCDMA_ModAccFetchDataRCDE

Returns the maximum value of the measured data relative code domain error (RCDE), along with the spreading factor and the channelization code of the corresponding channel.

#### Syntax

int32 __stdcall RFmxTDSCDMA_ModAccFetchDataRCDE(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *maximumPeakDataRCDE, int32 *peakDataRCDESpreadingFactor, int32 *peakDataRCDECode)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| maximumPeakDataRCDE | [out] | float64 * | This parameter returns the maximum value of the peak RDCEs among all active time slots and averaging iterations. This value is expressed in dB.RFmx calculates the RCDEs by projecting the descrambled error vector onto the codes of each active channel. The RCDE is the ratio of the mean power of the projection onto that code to the mean power of the corresponding active channel in the reference waveform. |
| peakDataRCDESpreadingFactor | [out] | int32 * | This parameter returns the spreading factor of the channel corresponding to the value of the RFMXTDSCDMA_ATTR_MODACC_RESULTS_PEAK_DATA_RCDE attribute. |
| peakDataRCDECode | [out] | int32 * | This parameter returns the channelization code of the channel corresponding to the value of the RFMXTDSCDMA_ATTR_MODACC_RESULTS_PEAK_DATA_RCDE_CODE attribute. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__modacc_1ga3b64217f49d6a966a659bf3c52fdefab.html language=enus -->
## TOPIC 00238: RFmxTDSCDMA_ModAccFetchMaximumEVMTrace

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__modacc_1ga3b64217f49d6a966a659bf3c52fdefab.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__modacc_1ga3b64217f49d6a966a659bf3c52fdefab.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the maximum EVM trace values on the chip level. Syntaxint32 __stdcall RFmxTDSCDMA_ModAccFetchMaximumEVMTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 maximumEVM[], int32 arraySize, int32 *actualArraySize)ParametersNameDirec

### RFmxTDSCDMA_ModAccFetchMaximumEVMTrace

Fetches the maximum EVM trace values on the chip level.

#### Syntax

int32 __stdcall RFmxTDSCDMA_ModAccFetchMaximumEVMTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 maximumEVM[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| x0 | [out] | float64 * | This parameter returns the start time of the trace. This value is expressed in seconds. |
| dx | [out] | float64 * | This parameter returns the sampling time of the trace. This value is expressed in seconds. |
| maximumEVM | [out] | float32[] | This parameter returns an array of the maximum EVM trace values on the chip level. This value is expressed as a percentage. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__modacc_1ga44f07291ea96b771b2656f08d55c4e53.html language=enus -->
## TOPIC 00239: RFmxTDSCDMA_ModAccFetchPilotEVM

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__modacc_1ga44f07291ea96b771b2656f08d55c4e53.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__modacc_1ga44f07291ea96b771b2656f08d55c4e53.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the EVM measurement of the pilot time slot. Syntaxint32 __stdcall RFmxTDSCDMA_ModAccFetchPilotEVM(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *rmsPilotEVM, float64 *peakPilotEVM, float64 *pilotRho, float64 *rmsPilotMagnitudeError, float64 *rmsPilotPhas

### RFmxTDSCDMA_ModAccFetchPilotEVM

Fetches the EVM measurement of the pilot time slot.

#### Syntax

int32 __stdcall RFmxTDSCDMA_ModAccFetchPilotEVM(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *rmsPilotEVM, float64 *peakPilotEVM, float64 *pilotRho, float64 *rmsPilotMagnitudeError, float64 *rmsPilotPhaseError)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| rmsPilotEVM | [out] | float64 * | This parameter returns the RMS of the pilot EVM, averaged over all averaging iterations. This value is expressed as a percentage. |
| peakPilotEVM | [out] | float64 * | This parameter returns the maximum of the peak pilot EVM among the averaging iterations. This value is expressed as a percentage. |
| pilotRho | [out] | float64 * | This parameter returns the pilot Rho value, averaged over all averaging iterations. |
| rmsPilotMagnitudeError | [out] | float64 * | This parameter returns the RMS of the pilot magnitude error, averaged over all the averaging iterations. This value is expressed as a percentage. |
| rmsPilotPhaseError | [out] | float64 * | This parameter returns the RMS of the pilot phase error, averaged over all averaging iterations. This value is expressed in degrees. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__modacc_1ga4ea0290a5d5d62160a7a7070999c4a76.html language=enus -->
## TOPIC 00240: RFmxTDSCDMA_ModAccFetchDataEVM

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__modacc_1ga4ea0290a5d5d62160a7a7070999c4a76.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__modacc_1ga4ea0290a5d5d62160a7a7070999c4a76.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the EVM measurement of the data channel. Syntaxint32 __stdcall RFmxTDSCDMA_ModAccFetchDataEVM(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *rmsDataEVM, float64 *peakDataEVM, float64 *dataRho, float64 *rmsDataMagnitudeError, float64 *rmsDataPhaseError)Pa

### RFmxTDSCDMA_ModAccFetchDataEVM

Returns the EVM measurement of the data channel.

#### Syntax

int32 __stdcall RFmxTDSCDMA_ModAccFetchDataEVM(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *rmsDataEVM, float64 *peakDataEVM, float64 *dataRho, float64 *rmsDataMagnitudeError, float64 *rmsDataPhaseError)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| rmsDataEVM | [out] | float64 * | This parameter returns the RMS of the data EVM, averaged over all active time slots and all averaging iterations. This value is expressed as a percentage. |
| peakDataEVM | [out] | float64 * | This parameter returns the peak data EVM among all active time slots and averaging iterations. This value is expressed as a percentage. |
| dataRho | [out] | float64 * | This parameter returns the data rho value, averaged over all active time slots and all averaging iterations. |
| rmsDataMagnitudeError | [out] | float64 * | This parameter returns the RMS of the data magnitude error, averaged over all active time slots and all averaging iterations. This value is expressed as a percentage. |
| rmsDataPhaseError | [out] | float64 * | This parameter returns the RMS of the data phase error, averaged over all active time slots and all averaging iterations. This value is expressed in degrees. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__modacc_1ga5b991d99ba8b68e2378f61b741dabcb8.html language=enus -->
## TOPIC 00241: RFmxTDSCDMA_ModAccFetchEVMTrace

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__modacc_1ga5b991d99ba8b68e2378f61b741dabcb8.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__modacc_1ga5b991d99ba8b68e2378f61b741dabcb8.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the average of the EVM traces on the chip level. Syntaxint32 __stdcall RFmxTDSCDMA_ModAccFetchEVMTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 evm[], int32 arraySize, int32 *actualArraySize)ParametersNameDirectionTypeDescr

### RFmxTDSCDMA_ModAccFetchEVMTrace

Fetches the average of the EVM traces on the chip level.

#### Syntax

int32 __stdcall RFmxTDSCDMA_ModAccFetchEVMTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 evm[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| x0 | [out] | float64 * | This parameter returns the start time of the trace. This value is expressed in seconds. |
| dx | [out] | float64 * | This parameter returns the sampling time of the trace. This value is expressed in seconds. |
| evm | [out] | float32[] | This parameter returns the EVM trace values as a real value array. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__modacc_1ga63fa1d261368682b7091c5a1f6668c32.html language=enus -->
## TOPIC 00242: RFmxTDSCDMA_ModAccFetchDetectedChannelArray

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__modacc_1ga63fa1d261368682b7091c5a1f6668c32.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__modacc_1ga63fa1d261368682b7091c5a1f6668c32.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the detected channels. If you set the RFMXTDSCDMA_ATTR_CHANNEL_CONFIGURATION_MODE attribute to User Defined, the measurement returns the configured channels. If the averaging is enabled, this function returns the array of detected channels of the last averaging iteration. Syntaxint32 __stdca

### RFmxTDSCDMA_ModAccFetchDetectedChannelArray

Returns the detected channels. If you set the [RFMXTDSCDMA_ATTR_CHANNEL_CONFIGURATION_MODE](group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__channel_1gaccad066733fbfbee5fceec4996afa266.html) attribute to **User Defined**, the measurement returns the configured channels. If the averaging is enabled, this function returns the array of detected channels of the last averaging iteration.

#### Syntax

int32 __stdcall RFmxTDSCDMA_ModAccFetchDetectedChannelArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 detectedSlotIndex[], int32 detectedSpreadingFactor[], int32 detectedModulationType[], int32 detectedChannelizationCode[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| detectedSlotIndex | [out] | int32[] | This parameter returns an array of slot indexes of the detected channels. |
| detectedSpreadingFactor | [out] | int32[] | This parameter returns an array of spreading factors of the detected channels. |
| detectedModulationType | [out] | int32[] | This parameter returns an array of the modulation types for the detected channels.Name (value)DescriptionQPSK (0)The modulation type is QPSK.8PSK (1)The modulation type is 8-PSK.16QAM (2)The modulation type is 16-QAM. |
| Name (value) | Description |  |  |
| QPSK (0) | The modulation type is QPSK. |  |  |
| 8PSK (1) | The modulation type is 8-PSK. |  |  |
| 16QAM (2) | The modulation type is 16-QAM. |  |  |
| detectedChannelizationCode | [out] | int32[] | This parameter returns an array of channelization code numbers for the detected channels. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__modacc_1ga7a7a0fdb34a90597fadaf89aa493c81a.html language=enus -->
## TOPIC 00243: RFmxTDSCDMA_ModAccFetchMagnitudeErrorTrace

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__modacc_1ga7a7a0fdb34a90597fadaf89aa493c81a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__modacc_1ga7a7a0fdb34a90597fadaf89aa493c81a.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the average of the magnitude error trace on the chip level. Syntaxint32 __stdcall RFmxTDSCDMA_ModAccFetchMagnitudeErrorTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 magnitudeError[], int32 arraySize, int32 *actualArraySize

### RFmxTDSCDMA_ModAccFetchMagnitudeErrorTrace

Fetches the average of the magnitude error trace on the chip level.

#### Syntax

int32 __stdcall RFmxTDSCDMA_ModAccFetchMagnitudeErrorTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 magnitudeError[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| x0 | [out] | float64 * | This parameter returns the start time of the trace. This value is expressed in seconds. |
| dx | [out] | float64 * | This parameter returns the sampling time of the trace. This value is expressed in seconds. |
| magnitudeError | [out] | float32[] | This parameter returns the magnitude trace error values as a real value array. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__modacc_1ga838fc7e8a1f4c25dce9b8b652f00e258.html language=enus -->
## TOPIC 00244: RFmxTDSCDMA_ModAccFetchDataActiveCDE

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__modacc_1ga838fc7e8a1f4c25dce9b8b652f00e258.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__modacc_1ga838fc7e8a1f4c25dce9b8b652f00e258.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the peak value among the code domain errors (CDEs) of the active channels, as well as the code number, spreading factor, and branch that correspond to this peak value. Syntaxint32 __stdcall RFmxTDSCDMA_ModAccFetchDataActiveCDE(niRFmxInstrHandle instrumentHandle, char selectorString[], float6

### RFmxTDSCDMA_ModAccFetchDataActiveCDE

Returns the peak value among the code domain errors (CDEs) of the active channels, as well as the code number, spreading factor, and branch that correspond to this peak value.

#### Syntax

int32 __stdcall RFmxTDSCDMA_ModAccFetchDataActiveCDE(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *maximumPeakDataActiveCDE, int32 *peakDataActiveCDESpreadingFactor, int32 *peakDataActiveCDECode, int32 *peakDataActiveCDENumberOfChannels)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| maximumPeakDataActiveCDE | [out] | float64 * | This parameter returns the maximum value of the peak data active CDE among all active physical channels, active time slots and averaging iterations. This value is expressed in dB. The peak data active CDE value is averaged over all averaging iterations. |
| peakDataActiveCDESpreadingFactor | [out] | int32 * | This parameter returns the spreading factor used for retrieving the peak CDE of the active physical channel corresponding to measured value of the RFMXTDSCDMA_ATTR_MODACC_RESULTS_MAXIMUM_PEAK_DATA_ACTIVE_CDE attribute. |
| peakDataActiveCDECode | [out] | int32 * | This parameter returns the peak channelization code of the channel corresponding to the measured value of the RFMXTDSCDMA_ATTR_MODACC_RESULTS_MAXIMUM_PEAK_DATA_ACTIVE_CDE attribute. |
| peakDataActiveCDENumberOfChannels | [out] | int32 * | This parameter returns the number of channels used to determine the peak active CDE. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__modacc_1ga86126e20fae194f31596cab77dcac339.html language=enus -->
## TOPIC 00245: RFmxTDSCDMA_ModAccFetchMaximumPhaseErrorTrace

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__modacc_1ga86126e20fae194f31596cab77dcac339.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__modacc_1ga86126e20fae194f31596cab77dcac339.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the maximum phase error trace on the chip level. Syntaxint32 __stdcall RFmxTDSCDMA_ModAccFetchMaximumPhaseErrorTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 maximumPhaseError[], int32 arraySize, int32 *actualArraySize)Para

### RFmxTDSCDMA_ModAccFetchMaximumPhaseErrorTrace

Fetches the maximum phase error trace on the chip level.

#### Syntax

int32 __stdcall RFmxTDSCDMA_ModAccFetchMaximumPhaseErrorTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 maximumPhaseError[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| x0 | [out] | float64 * | This parameter returns the start time of the trace. This value is expressed in seconds. |
| dx | [out] | float64 * | This parameter returns the sampling time of the trace. This value is expressed in seconds. |
| maximumPhaseError | [out] | float32[] | This parameter returns an array of the maximum phase error traces on the chip level. This value is expressed in degrees. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__modacc_1ga8bb676015c4d0f7886bebdc65be781bc.html language=enus -->
## TOPIC 00246: RFmxTDSCDMA_ModAccFetchConstellationTrace

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__modacc_1ga8bb676015c4d0f7886bebdc65be781bc.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__modacc_1ga8bb676015c4d0f7886bebdc65be781bc.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the constellation trace of the received TD-SCDMA signal. If the averaging is enabled, this trace refers to the last averaging iteration.. Syntaxint32 __stdcall RFmxTDSCDMA_ModAccFetchConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingl

### RFmxTDSCDMA_ModAccFetchConstellationTrace

Fetches the constellation trace of the received TD-SCDMA signal. If the averaging is enabled, this trace refers to the last averaging iteration..

#### Syntax

int32 __stdcall RFmxTDSCDMA_ModAccFetchConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle constellation[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| constellation | [out] | NIComplexSingle[] | This parameter returns an array of complex chips of the corrected signal on which the ModAcc measurements are performed. You can use these chips to obtain the constellation diagram. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__modacc_1ga900ef98f1effb4237a4f8ffe3c720d79.html language=enus -->
## TOPIC 00247: RFmxTDSCDMA_ModAccFetchNumberOfDetectedChannels

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__modacc_1ga900ef98f1effb4237a4f8ffe3c720d79.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__modacc_1ga900ef98f1effb4237a4f8ffe3c720d79.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the number of detected channels. If the averaging is enabled, it returns the number of detected channels of the last averaging iteration. If you set the RFMXTDSCDMA_ATTR_CHANNEL_CONFIGURATION_MODE attribute to User Defined, the measurement returns the number of configured channels. Syntaxint

### RFmxTDSCDMA_ModAccFetchNumberOfDetectedChannels

Returns the number of detected channels. If the averaging is enabled, it returns the number of detected channels of the last averaging iteration. If you set the [RFMXTDSCDMA_ATTR_CHANNEL_CONFIGURATION_MODE](group____root__ni_r_fmx_t_d_s_c_d_m_a__attributes__channel_1gaccad066733fbfbee5fceec4996afa266.html) attribute to **User Defined**, the measurement returns the number of configured channels.

#### Syntax

int32 __stdcall RFmxTDSCDMA_ModAccFetchNumberOfDetectedChannels(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 *numberOfDetectedChannels)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| numberOfDetectedChannels | [out] | int32 * | This parameter returns the total number of the detected channels. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__modacc_1ga943c3a272acb9f845c030d10a64cdb57.html language=enus -->
## TOPIC 00248: RFmxTDSCDMA_ModAccFetchConstellationTraceSplit

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__modacc_1ga943c3a272acb9f845c030d10a64cdb57.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__modacc_1ga943c3a272acb9f845c030d10a64cdb57.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the constellation trace of the received TD-SCDMA signal. If the averaging is enabled, this trace refers to the last averaging iteration.. Syntaxint32 __stdcall RFmxTDSCDMA_ModAccFetchConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 c

### RFmxTDSCDMA_ModAccFetchConstellationTraceSplit

Fetches the constellation trace of the received TD-SCDMA signal. If the averaging is enabled, this trace refers to the last averaging iteration..

#### Syntax

int32 __stdcall RFmxTDSCDMA_ModAccFetchConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 constellationI[], float32 constellationQ[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| constellationI | [out] | float32[] | This parameter returns an array of complex chips of the corrected signal on which the ModAcc measurements are performed. You can use these chips to obtain the constellation diagram. |
| constellationQ | [out] | float32[] | This parameter returns an array of complex chips of the corrected signal on which the ModAcc measurements are performed. You can use these chips to obtain the constellation diagram. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__modacc_1ga947a9952073817954d025216d5b22a36.html language=enus -->
## TOPIC 00249: RFmxTDSCDMA_ModAccFetchMidambleEVM

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__modacc_1ga947a9952073817954d025216d5b22a36.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__modacc_1ga947a9952073817954d025216d5b22a36.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the midamble EVM measurement results. Syntaxint32 __stdcall RFmxTDSCDMA_ModAccFetchMidambleEVM(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *rmsMidambleEVM, float64 *peakMidambleEVM, float64 *midambleRho, float64 *rmsMidambleMagnitudeError, float64 *rms

### RFmxTDSCDMA_ModAccFetchMidambleEVM

Returns the midamble EVM measurement results.

#### Syntax

int32 __stdcall RFmxTDSCDMA_ModAccFetchMidambleEVM(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *rmsMidambleEVM, float64 *peakMidambleEVM, float64 *midambleRho, float64 *rmsMidambleMagnitudeError, float64 *rmsMidamblePhaseError)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| rmsMidambleEVM | [out] | float64 * | This parameter returns the RMS of the midamble EVM, averaged over all active time slots and all averaging iterations. This value is expressed as a percentage. |
| peakMidambleEVM | [out] | float64 * | This parameter returns the peak midamble EVM among all active time slots and averaging iterations. This value is expressed as a percentage. |
| midambleRho | [out] | float64 * | This parameter returns the rho value of the midamble, averaged over all measured active time slots and averaging iterations. |
| rmsMidambleMagnitudeError | [out] | float64 * | This parameter returns the RMS of the midamble magnitude error, averaged over all active time slots and averaging iterations. This value is expressed as a percentage. |
| rmsMidamblePhaseError | [out] | float64 * | This parameter returns the RMS of the midamble phase error, averaged over all active time slots and all averaging iterations. This value is expressed in degrees. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__modacc_1ga9a5025307e87d13172c0b11cddc2a1f1.html language=enus -->
## TOPIC 00250: RFmxTDSCDMA_ModAccFetchCompositeEVM

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__modacc_1ga9a5025307e87d13172c0b11cddc2a1f1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__modacc_1ga9a5025307e87d13172c0b11cddc2a1f1.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the composite EVM of all the channels in the ModAcc measurement. Syntaxint32 __stdcall RFmxTDSCDMA_ModAccFetchCompositeEVM(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *rmsCompositeEVM, float64 *peakCompositeEVM, float64 *compositeRho, float64 *frequenc

### RFmxTDSCDMA_ModAccFetchCompositeEVM

Returns the composite EVM of all the channels in the ModAcc measurement.

#### Syntax

int32 __stdcall RFmxTDSCDMA_ModAccFetchCompositeEVM(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *rmsCompositeEVM, float64 *peakCompositeEVM, float64 *compositeRho, float64 *frequencyError, float64 *chipRateError, float64 *rmsCompositeMagnitudeError, float64 *rmsCompositePhaseError)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| rmsCompositeEVM | [out] | float64 * | This parameter returns the value of the RMS of the composite EVM, averaged over all active time slots and all averaging iterations. This value is expressed as a percentage. Values close to 0 indicate a good modulation accuracy. In a loopback setup, values of approximately 0.2 to 0.4 are typical. |
| peakCompositeEVM | [out] | float64 * | This parameter returns the value of the peak composite EVM among all active time slots and averaging iterations. This value is expressed as a percentage. |
| compositeRho | [out] | float64 * | This parameter returns the composite value of rho, averaged over all active time-slots and all averaging iterations. A value of 1 indicates a perfectly modulated signal. Typical values for real signals in a loopback setup are slightly below 1.000000. |
| frequencyError | [out] | float64 * | This parameter returns the frequency error averaged over all measured slots. This value is expressed in Hz. |
| chipRateError | [out] | float64 * | This parameter returns the chip rate error. This value is expressed in ppm. |
| rmsCompositeMagnitudeError | [out] | float64 * | This parameter returns the value of the time-slot based RMS of the composite magnitude error averaged over all active time slots and averaging iterations. This value is expressed as a percentage. |
| rmsCompositePhaseError | [out] | float64 * | This parameter returns the time-slot based RMS of the composite phase error, averaged over all active time slots and averaging iterations. This value is expressed in degrees. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc
